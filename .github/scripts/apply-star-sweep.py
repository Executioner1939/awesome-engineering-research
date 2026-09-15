#!/usr/bin/env python3
"""Diff current GitHub stars (jsonl) against INDEX/tools.md and apply moves.

Inputs:
  --stars            /tmp/stars-current.jsonl  (one repo object per line)
  --tools            INDEX/tools.md
  --archived         _archived/tools.md
  --staleness-years  int (default 3)
  --report-md        path of the sweep report to write
  --queue            path for the curation queue (jsonl) consumed by the
                     Claude curation step (default /tmp/star-curation-queue.jsonl)
  --backlog          how many existing rows with category/kind `unsorted` or an
                     empty description to add to the queue per run (default 40)

Outputs:
  * updated INDEX/tools.md and _archived/tools.md
  * /tmp/star-summary.json  {added, removed, restored, stale, unchanged, queued}
  * /tmp/star-summary.md    human-readable summary (commit body / PR body)
  * curation queue jsonl    rows that need category / kind / labels / description

Rules:
  * Newly starred repo not present anywhere         -> new active row (category
    and kind = `unsorted` until the curation step classifies it)
  * Active row whose repo is no longer starred      -> archived, reason user_unstarred
  * Archived row (reason user_unstarred) starred again -> restored to active
  * Active row archived on GitHub                   -> archived, reason repo_archived
  * Active row with no push inside the window       -> archived, reason stale
  * Every remaining active row                      -> stars / last_pushed refreshed
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import date, timedelta
from pathlib import Path

TODAY = date.today().isoformat()
DESC_MAX = 200
_SPLIT = re.compile(r"(?<!\\)\|")


# --------------------------------------------------------------------------- #
# Markdown table helpers
# --------------------------------------------------------------------------- #
def parse_table(text: str) -> tuple[str, list[str], list[dict], str]:
    m = re.search(r"(.*?<!--\s*BEGIN:\s*rows\s*-->\s*\n)(.*?)(\n<!--\s*END:\s*rows\s*-->.*)$",
                  text, re.DOTALL)
    if not m:
        raise RuntimeError("rows marker missing")
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.strip().splitlines()
    header = [c.strip() for c in _SPLIT.split(lines[0].strip("|").strip())]
    rows = []
    for ln in lines[2:]:
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in _SPLIT.split(ln.strip().strip("|"))]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return prefix, lines[:2], rows, suffix


def cell(v: object) -> str:
    """Make a value safe inside a markdown table cell."""
    s = str(v if v is not None else "")
    s = re.sub(r"\s+", " ", s).strip()
    return s.replace("|", "\\|")


def render_rows(header: list[str], rows: list[dict]) -> str:
    cols = [c.strip() for c in header[0].strip("|").split("|")]
    out = list(header)
    for r in sorted(rows, key=lambda x: x.get("id", "")):
        out.append("| " + " | ".join(cell(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)


def bump_frontmatter(text: str, active: int, archived: int) -> str:
    text = re.sub(r"(?m)^updated: .*$", f"updated: {TODAY}", text, count=1)
    text = re.sub(r"(?m)^total_active: .*$", f"total_active: {active}", text, count=1)
    text = re.sub(r"(?m)^total_archived: .*$", f"total_archived: {archived}", text, count=1)
    return text


# --------------------------------------------------------------------------- #
# Row construction
# --------------------------------------------------------------------------- #
def slug(full_name: str) -> str:
    return full_name.lower().replace("/", "-")


def clean_description(raw: str | None) -> str:
    """First sentence of the GitHub description, emoji/noise trimmed, capped."""
    s = re.sub(r"\s+", " ", raw or "").strip()
    # Drop leading emoji / symbol clutter that many repos put in front.
    s = re.sub(r"^[^\w\[(\"'`]+", "", s)
    if len(s) > DESC_MAX:
        cut = s[:DESC_MAX]
        # Prefer to cut at a sentence or clause boundary.
        for sep in (". ", "; ", " - ", " — ", ", "):
            idx = cut.rfind(sep)
            if idx > DESC_MAX // 2:
                cut = cut[: idx + (1 if sep == ". " else 0)]
                break
        s = cut.rstrip() + ("" if cut.endswith(".") else "…")
    return s


DOMAINS = ("developer-tooling", "ai-applications", "infrastructure", "distributed-systems",
           "language-runtimes", "data-storage", "security", "observability", "frontend",
           "knowledge-systems", "web-extraction", "standards")

TOPIC_TO_LABELS = {
    "kubernetes": ("infrastructure", "kubernetes"),
    "k8s": ("infrastructure", "kubernetes"),
    "terraform": ("infrastructure", "terraform", "iac"),
    "opentofu": ("infrastructure", "terraform", "iac"),
    "helm": ("infrastructure", "helm"),
    "argocd": ("infrastructure", "argocd"),
    "docker": ("infrastructure", "docker"),
    "bazel": ("developer-tooling", "bazel"),
    "monorepo": ("developer-tooling",),
    "cli": ("developer-tooling", "cli-tooling"),
    "rust": ("language-runtimes", "rust"),
    "golang": ("language-runtimes", "go"),
    "scala": ("language-runtimes", "scala"),
    "python": ("language-runtimes", "python"),
    "typescript": ("language-runtimes", "typescript"),
    "javascript": ("language-runtimes", "javascript"),
    "java": ("language-runtimes", "java"),
    "kotlin": ("language-runtimes", "kotlin"),
    "wasm": ("frontend", "wasm"),
    "webassembly": ("frontend", "wasm"),
    "llm": ("ai-applications", "llm"),
    "rag": ("knowledge-systems", "rag"),
    "agents": ("ai-applications", "agents"),
    "ai-agents": ("ai-applications", "agents"),
    "mcp": ("ai-applications", "mcp"),
    "embeddings": ("knowledge-systems", "embeddings"),
    "knowledge-graph": ("knowledge-systems",),
    "vector-database": ("data-storage", "vector-db"),
    "graph-database": ("data-storage", "graph-db"),
    "database": ("data-storage", "databases"),
    "postgres": ("data-storage", "postgres"),
    "postgresql": ("data-storage", "postgres"),
    "kafka": ("data-storage", "kafka"),
    "nats": ("data-storage", "nats"),
    "observability": ("observability",),
    "tracing": ("observability", "tracing"),
    "opentelemetry": ("observability", "opentelemetry"),
    "metrics": ("observability", "metrics"),
    "logging": ("observability", "logging"),
    "profiling": ("observability", "profiling"),
    "security": ("security",),
    "cryptography": ("security",),
    "authentication": ("security",),
    "oauth": ("security", "standards"),
    "scraping": ("web-extraction",),
    "crawler": ("web-extraction",),
    "web-scraping": ("web-extraction",),
    "browser-automation": ("web-extraction",),
    "distributed-systems": ("distributed-systems",),
    "consensus": ("distributed-systems", "consensus"),
    "raft": ("distributed-systems", "consensus"),
    "event-sourcing": ("distributed-systems", "event-sourcing"),
    "cqrs": ("distributed-systems", "cqrs"),
    "microservices": ("distributed-systems", "microservices"),
    "react": ("frontend",),
    "frontend": ("frontend",),
    "ui": ("frontend",),
    "compiler": ("language-runtimes", "compilers"),
    "parser": ("language-runtimes", "parsers"),
    "async": ("language-runtimes", "concurrency"),
    "tokio": ("language-runtimes", "tokio", "async-runtimes"),
}

LANG_LABELS = {"rust", "go", "scala", "python", "typescript", "javascript", "java",
               "kotlin", "c", "cpp", "elixir", "ocaml", "shell"}
LANG_ALIASES = {"c++": "cpp", "jupyter notebook": "python"}


def derive_labels(repo: dict) -> list[str]:
    """Cheap first-pass labels from topics + language + description keywords.

    The curation step (Claude) refines these; this only guarantees that every
    row carries at least one valid domain label so the lint gate passes even
    when the curation step is unavailable.
    """
    labels: set[str] = set()
    topics = [t.lower() for t in (repo.get("topics") or [])]
    lang = (repo.get("language") or "").lower()
    lang = LANG_ALIASES.get(lang, lang)
    desc = (repo.get("description") or "").lower()

    for t in topics:
        if t in TOPIC_TO_LABELS:
            labels.update(TOPIC_TO_LABELS[t])
    if lang in LANG_LABELS:
        labels.update(("language-runtimes", lang))

    kw = {
        "kubernetes": ("infrastructure", "kubernetes"), "k8s": ("infrastructure", "kubernetes"),
        "terraform": ("infrastructure", "terraform"), "distributed": ("distributed-systems",),
        "consensus": ("distributed-systems", "consensus"), "replication": ("distributed-systems", "replication"),
        "llm": ("ai-applications", "llm"), "agent": ("ai-applications", "agents"),
        "rag": ("knowledge-systems", "rag"), "knowledge graph": ("knowledge-systems",),
        "vector": ("data-storage", "vector-db"), "database": ("data-storage", "databases"),
        "tracing": ("observability", "tracing"), "observability": ("observability",),
        "scrap": ("web-extraction",), "crawl": ("web-extraction",),
        "security": ("security",), "auth": ("security",), "encrypt": ("security",),
        "compiler": ("language-runtimes", "compilers"), "parser": ("language-runtimes", "parsers"),
        "awesome": ("knowledge-systems",), "curated list": ("knowledge-systems",),
    }
    for hint, lbls in kw.items():
        if hint in desc:
            labels.update(lbls)

    if not any(d in labels for d in DOMAINS):
        labels.add("developer-tooling")
    return sorted(labels)


def new_row(rid: str, r: dict) -> dict:
    return {
        "id": rid,
        "full_name": r["full_name"],
        "url": r["html_url"],
        "description": clean_description(r.get("description")),
        "language": r.get("language") or "",
        "stars": str(r.get("stargazers_count", 0)),
        "last_pushed": (r.get("pushed_at") or "")[:10],
        "category": "unsorted",
        "kind": "unsorted",
        "labels": ",".join(derive_labels(r)),
        "status": "active",
        "notes": "",
    }


def needs_curation(row: dict) -> bool:
    if row.get("notes", "").strip() == "second-pass uncertain":
        return False
    return (row.get("category", "unsorted") in ("", "unsorted")
            or row.get("kind", "unsorted") in ("", "unsorted")
            or len(row.get("description", "")) < 20)


# --------------------------------------------------------------------------- #
def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--stars", required=True)
    p.add_argument("--tools", required=True)
    p.add_argument("--archived", required=True)
    p.add_argument("--staleness-years", type=int, default=3)
    p.add_argument("--report-md", required=True)
    p.add_argument("--queue", default="/tmp/star-curation-queue.jsonl")
    p.add_argument("--backlog", type=int, default=40)
    args = p.parse_args()

    threshold = (date.today() - timedelta(days=365 * args.staleness_years)).isoformat()

    current: dict[str, dict] = {}
    for line in Path(args.stars).read_text().splitlines():
        if line.strip():
            repo = json.loads(line)
            current[slug(repo["full_name"])] = repo
    if not current:
        raise SystemExit("refusing to run: star list is empty (API failure?)")

    prefix, header, rows, suffix = parse_table(Path(args.tools).read_text())
    a_prefix, a_header, a_rows, a_suffix = parse_table(Path(args.archived).read_text())

    indexed_active = {r["id"]: r for r in rows}
    indexed_archived = {r["id"]: r for r in a_rows}

    added = removed = restored = stale = unchanged = 0
    new_rows: list[dict] = []
    new_arch: list[dict] = []
    queue: list[dict] = []  # rows for the curation step
    changes: dict[str, list[str]] = {"added": [], "removed": [], "restored": [], "stale": []}

    def archive(row: dict, reason: str, pushed: str | None = None) -> None:
        arch = dict(row)
        arch["status"] = "archived"
        arch["last_seen"] = TODAY
        arch["reason"] = reason
        if pushed:
            arch["last_pushed"] = pushed
        new_arch.append(arch)

    # Active sweep --------------------------------------------------------- #
    for rid, row in indexed_active.items():
        if rid not in current:
            archive(row, "user_unstarred")
            removed += 1
            changes["removed"].append(row["full_name"])
            continue
        r = current[rid]
        pushed = (r.get("pushed_at") or "")[:10]
        if r.get("archived"):
            archive(row, "repo_archived", pushed)
            stale += 1
            changes["stale"].append(f"{row['full_name']} (archived on GitHub)")
            continue
        if pushed and pushed < threshold:
            archive(row, "stale", pushed)
            stale += 1
            changes["stale"].append(f"{row['full_name']} (last push {pushed})")
            continue
        row["stars"] = str(r.get("stargazers_count", 0))
        row["last_pushed"] = pushed
        if not row.get("description"):
            row["description"] = clean_description(r.get("description"))
        if not row.get("language"):
            row["language"] = r.get("language") or ""
        new_rows.append(row)
        unchanged += 1

    # Archived sweep: restore rows the user un-starred and then starred again #
    for rid, arow in indexed_archived.items():
        r = current.get(rid)
        if r and arow.get("reason") == "user_unstarred" and not r.get("archived"):
            pushed = (r.get("pushed_at") or "")[:10]
            if pushed and pushed < threshold:
                new_arch.append(arow)  # starred again but stale: stays archived
                continue
            row = {k: arow.get(k, "") for k in
                   ("id", "full_name", "url", "description", "language", "stars",
                    "last_pushed", "category", "kind", "labels", "status", "notes")}
            row.update(status="active", stars=str(r.get("stargazers_count", 0)), last_pushed=pushed)
            row["category"] = row.get("category") or "unsorted"
            row["kind"] = row.get("kind") or "unsorted"
            if not row.get("description"):
                row["description"] = clean_description(r.get("description"))
            new_rows.append(row)
            restored += 1
            changes["restored"].append(row["full_name"])
        else:
            new_arch.append(arow)

    # Adds ---------------------------------------------------------------- #
    for rid, r in current.items():
        if rid in indexed_active or rid in indexed_archived:
            continue
        if r.get("archived"):
            # Starred but already archived upstream: record as tombstone directly.
            row = new_row(rid, r)
            archive(row, "repo_archived")
            stale += 1
            changes["stale"].append(f"{r['full_name']} (archived on GitHub)")
            continue
        row = new_row(rid, r)
        new_rows.append(row)
        added += 1
        changes["added"].append(r["full_name"])

    # Curation queue: every new row, then a bounded slice of the backlog ----- #
    fresh = {slug(n) for n in changes["added"]} | {slug(n) for n in changes["restored"]}
    backlog_budget = args.backlog
    for row in sorted(new_rows, key=lambda x: (x["id"] not in fresh, -int(x.get("stars") or 0))):
        is_fresh = row["id"] in fresh
        if not is_fresh:
            if backlog_budget <= 0 or not needs_curation(row):
                continue
            backlog_budget -= 1
        meta = current.get(row["id"], {})
        queue.append({
            "id": row["id"],
            "full_name": row["full_name"],
            "url": row["url"],
            "reason": "new" if is_fresh else "backlog",
            "current": {k: row.get(k, "") for k in ("category", "kind", "labels", "description")},
            "github": {
                "description": meta.get("description"),
                "language": meta.get("language"),
                "topics": meta.get("topics") or [],
                "stars": meta.get("stargazers_count"),
                "pushed_at": (meta.get("pushed_at") or "")[:10],
                "license": meta.get("license"),
            },
        })

    # Write --------------------------------------------------------------- #
    tools_text = bump_frontmatter(prefix + render_rows(header, new_rows) + suffix,
                                  len(new_rows), len(new_arch))
    arch_text = bump_frontmatter(a_prefix + render_rows(a_header, new_arch) + a_suffix,
                                 0, len(new_arch))
    Path(args.tools).write_text(tools_text)
    Path(args.archived).write_text(arch_text)
    Path(args.queue).write_text("".join(json.dumps(q, ensure_ascii=False) + "\n" for q in queue))

    summary = {"added": added, "removed": removed, "restored": restored, "stale": stale,
               "unchanged": unchanged, "queued": len(queue),
               "total_active": len(new_rows), "total_archived": len(new_arch)}
    Path("/tmp/star-summary.json").write_text(json.dumps(summary))

    def bullet_list(items: list[str], cap: int = 40) -> list[str]:
        out = [f"  - {i}" for i in items[:cap]]
        if len(items) > cap:
            out.append(f"  - … and {len(items) - cap} more")
        return out

    md = [
        f"# Star sweep ({TODAY})",
        "",
        f"- Newly starred → added: **{added}**",
        f"- Starred again → restored from archive: **{restored}**",
        f"- Unstarred → archived: **{removed}**",
        f"- Archived on GitHub or stale (>{args.staleness_years} y without a push): **{stale}**",
        f"- Refreshed in place: {unchanged}",
        f"- Sent to curation (new + backlog): {len(queue)}",
        f"- Totals after sweep: {len(new_rows)} active / {len(new_arch)} archived",
        "",
        f"Staleness threshold: `last_pushed >= {threshold}`",
        "",
    ]
    for key, title in (("added", "Added"), ("restored", "Restored"),
                       ("removed", "Unstarred"), ("stale", "Archived / stale")):
        if changes[key]:
            md += [f"## {title}", *bullet_list(sorted(changes[key])), ""]
    Path(args.report_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_md).write_text("\n".join(md))
    Path("/tmp/star-summary.md").write_text("\n".join(md))
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

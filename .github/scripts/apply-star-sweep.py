#!/usr/bin/env python3
"""Diff current GH stars (jsonl) against INDEX/tools.md, apply moves.

Inputs:
  --stars       /tmp/stars-current.jsonl
  --tools       INDEX/tools.md
  --archived    _archived/tools.md
  --staleness-years int (default 3)
  --report-md   path

Writes updated tools.md and _archived/tools.md.
Writes /tmp/star-summary.json (added, removed, stale counts) and /tmp/star-summary.md.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from datetime import date, timedelta


TODAY = date.today().isoformat()


def parse_table(text: str) -> tuple[str, list[str], list[dict], str]:
    m = re.search(r"(.*?<!--\s*BEGIN:\s*rows\s*-->\s*\n)(.*?)(\n<!--\s*END:\s*rows\s*-->.*)$",
                  text, re.DOTALL)
    if not m:
        raise RuntimeError("rows marker missing")
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.strip().splitlines()
    _split = re.compile(r"(?<!\\)\|")
    header = [c.strip() for c in _split.split(lines[0].strip("|").strip())]
    rows = []
    for ln in lines[2:]:
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in _split.split(ln.strip().strip("|"))]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return prefix, lines[:2], rows, suffix


def render_rows(header: list[str], rows: list[dict]) -> str:
    cols = [c.strip() for c in header[0].strip("|").split("|")]
    out = list(header)
    for r in sorted(rows, key=lambda x: x.get("id", "")):
        out.append("| " + " | ".join(str(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)


def slug(full_name: str) -> str:
    return full_name.lower().replace("/", "-")


def derive_labels(repo: dict) -> list[str]:
    """Tiny label-derivation pass — refined heuristics belong in the curator agent."""
    labels: set[str] = set()
    topics = repo.get("topics") or []
    lang = (repo.get("language") or "").lower()
    desc = (repo.get("description") or "").lower()

    topic_to_label = {
        "kubernetes": ("infrastructure", "kubernetes"),
        "terraform": ("infrastructure", "terraform"),
        "rust": ("language-runtimes", "rust"),
        "go": ("language-runtimes", "go"),
        "scala": ("language-runtimes", "scala"),
        "python": ("language-runtimes", "python"),
        "typescript": ("language-runtimes", "typescript"),
        "llm": ("ai-applications", "llm"),
        "rag": ("ai-applications", "rag"),
        "agents": ("ai-applications", "agents"),
        "vector": ("data-storage", "vector-db"),
        "graph-database": ("data-storage", "graph-db"),
        "observability": ("observability",),
        "tracing": ("observability", "tracing"),
        "security": ("security",),
        "monorepo": ("developer-tooling",),
        "cli": ("developer-tooling", "cli-tooling"),
    }
    for t in topics:
        for hint, lbls in topic_to_label.items():
            if hint in t:
                labels.update(lbls)

    if lang in {"rust", "go", "scala", "python", "typescript", "java"}:
        labels.add("language-runtimes")
        labels.add(lang)
    if "kubernetes" in desc or "k8s" in desc:
        labels.update(("infrastructure", "kubernetes"))
    if "distributed" in desc or "consensus" in desc or "replication" in desc:
        labels.add("distributed-systems")
    if "llm" in desc or "agent" in desc:
        labels.update(("ai-applications",))

    if not any(d in labels for d in ("developer-tooling", "ai-applications", "infrastructure",
                                     "distributed-systems", "language-runtimes", "data-storage",
                                     "security", "observability", "frontend", "knowledge-systems",
                                     "web-extraction", "standards")):
        labels.add("developer-tooling")
    return sorted(labels)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--stars", required=True)
    p.add_argument("--tools", required=True)
    p.add_argument("--archived", required=True)
    p.add_argument("--staleness-years", type=int, default=3)
    p.add_argument("--report-md", required=True)
    args = p.parse_args()

    threshold = (date.today() - timedelta(days=365 * args.staleness_years)).isoformat()

    current: dict[str, dict] = {}
    for line in Path(args.stars).read_text().splitlines():
        if not line.strip():
            continue
        repo = json.loads(line)
        repo_id = slug(repo["full_name"])
        current[repo_id] = repo

    tools_text = Path(args.tools).read_text()
    prefix, header, rows, suffix = parse_table(tools_text)
    arch_text = Path(args.archived).read_text()
    a_prefix, a_header, a_rows, a_suffix = parse_table(arch_text)

    indexed_active = {r["id"]: r for r in rows}
    indexed_archived = {r["id"]: r for r in a_rows}

    added = removed = stale = unchanged = 0
    new_rows = []
    new_arch = list(a_rows)

    # Active sweep: refresh, archive if stale or repo_archived
    for rid, row in indexed_active.items():
        if rid not in current:
            # No longer starred
            arch = dict(row)
            arch["status"] = "archived"
            arch["last_seen"] = TODAY
            arch["reason"] = "user_unstarred"
            new_arch.append(arch)
            removed += 1
            continue
        r = current[rid]
        if r.get("archived"):
            arch = dict(row)
            arch["status"] = "archived"
            arch["last_seen"] = TODAY
            arch["reason"] = "repo_archived"
            arch["last_pushed"] = (r.get("pushed_at") or "")[:10]
            new_arch.append(arch)
            stale += 1
            continue
        pushed = (r.get("pushed_at") or "")[:10]
        if pushed and pushed < threshold:
            arch = dict(row)
            arch["status"] = "archived"
            arch["last_seen"] = TODAY
            arch["reason"] = "stale"
            arch["last_pushed"] = pushed
            new_arch.append(arch)
            stale += 1
            continue
        # Refresh stars + last_pushed
        row["stars"] = str(r.get("stargazers_count", 0))
        row["last_pushed"] = pushed
        new_rows.append(row)
        unchanged += 1

    # Adds: newly starred
    for rid, r in current.items():
        if rid in indexed_active or rid in indexed_archived:
            continue
        new_row = {
            "id": rid,
            "full_name": r["full_name"],
            "url": r["html_url"],
            "description": (r.get("description") or "")[:120],
            "language": r.get("language") or "",
            "stars": str(r.get("stargazers_count", 0)),
            "last_pushed": (r.get("pushed_at") or "")[:10],
            "labels": ",".join(derive_labels(r)),
            "status": "active",
            "notes": "",
        }
        new_rows.append(new_row)
        added += 1

    Path(args.tools).write_text(prefix + render_rows(header, new_rows) + suffix)
    Path(args.archived).write_text(a_prefix + render_rows(a_header, new_arch) + a_suffix)

    summary = {"added": added, "removed": removed, "stale": stale, "unchanged": unchanged}
    Path("/tmp/star-summary.json").write_text(json.dumps(summary))

    md = [
        f"# Star sweep ({TODAY})",
        "",
        f"- Newly starred → added: **{added}**",
        f"- Unstarred → archived: **{removed}**",
        f"- Archived-on-GitHub or stale (>{args.staleness_years} y no push): **{stale}**",
        f"- Unchanged: {unchanged}",
        "",
        f"Threshold: `last_pushed >= {threshold}`",
    ]
    Path(args.report_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_md).write_text("\n".join(md))
    Path("/tmp/star-summary.md").write_text("\n".join(md))
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Regenerate top-level README.md from INDEX/sources.md and INDEX/tools.md.

Idempotent: running twice on unchanged inputs produces a byte-identical README.
Content between matching `<!-- BEGIN: <name> -->` and `<!-- END: <name> -->`
markers is replaced; everything outside the markers is preserved.

Sections rendered:
  badges, toc, stats, category-<domain>, archived, triage

Usage:
  regen-readme.py --sources INDEX/sources.md --tools INDEX/tools.md \\
                  --template .claude/templates/README.template.md \\
                  --taxonomy .claude/skills/research-standard/TAXONOMY/domains.md \\
                  --triage TRIAGE.md --output README.md
"""
from __future__ import annotations

import argparse
import re
from collections import defaultdict
from pathlib import Path
from datetime import date


DOMAINS = [
    "developer-tooling",
    "web-extraction",
    "knowledge-systems",
    "data-storage",
    "distributed-systems",
    "language-runtimes",
    "observability",
    "ai-applications",
    "frontend",
    "infrastructure",
    "security",
    "standards",
]

DOMAIN_BLURB = {
    "developer-tooling": "Build systems, monorepo tooling, package managers, version managers, formatters, linters.",
    "web-extraction": "Scraping, crawling, sitemap and link-graph extraction, browser automation.",
    "knowledge-systems": "Knowledge graphs, ontologies, RAG, retrieval, embeddings, agentic retrieval.",
    "data-storage": "Databases (relational, vector, graph, hybrid), search indexes, message stores, caches.",
    "distributed-systems": "Consistency, replication, consensus, idempotency, event sourcing, CRDTs.",
    "language-runtimes": "Rust, async runtimes, JVM, Node, Bun, Deno, compilers, type systems.",
    "observability": "Metrics, traces, structured logs, profiling, debugging.",
    "ai-applications": "LLM application architecture, prompt engineering, agent frameworks, evals, tool-use.",
    "frontend": "UI frameworks, component systems, accessibility, design systems, web performance.",
    "infrastructure": "Container orchestration, IaC, CI/CD, Kubernetes, service mesh.",
    "security": "Authn, authz, secrets, supply-chain, code-signing, cryptography.",
    "standards": "RFCs, specs, ISO / W3C / IETF / ECMA documents, interop conventions.",
}


def parse_table(md_text: str) -> list[dict]:
    """Extract a markdown table between `<!-- BEGIN: rows -->` and `<!-- END: rows -->`."""
    m = re.search(r"<!--\s*BEGIN:\s*rows\s*-->(.*?)<!--\s*END:\s*rows\s*-->", md_text, re.DOTALL)
    if not m:
        return []
    block = m.group(1).strip().splitlines()
    if len(block) < 2:
        return []
    _split = re.compile(r"(?<!\\)\|")
    header = [c.strip() for c in _split.split(block[0].strip("|").strip())]
    rows = []
    for line in block[2:]:  # skip header + separator
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in _split.split(line.strip().strip("|"))]
        if len(cells) != len(header):
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def parse_labels(s: str) -> list[str]:
    return [x.strip() for x in s.split(",") if x.strip()]


def group_by_domain(rows: list[dict]) -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        labels = parse_labels(r.get("labels", ""))
        domains_in_row = [l for l in labels if l in DOMAINS]
        if not domains_in_row:
            out["unlabeled"].append(r)
        else:
            for d in domains_in_row:
                out[d].append(r)
    return out


def render_repo_row(r: dict) -> str:
    desc = r.get("description", "").strip()
    if len(desc) > 110:
        desc = desc[:107] + "..."
    link = f"[{r['full_name']}]({r['url']})"
    lang = r.get("language", "") or "—"
    stars = r.get("stars", "0")
    pushed = r.get("last_pushed", "")
    return f"| {link} | {lang} | {stars} | {pushed} | {desc} |"


def render_source_row(r: dict) -> str:
    title = r["title"].strip()
    link = f"[{title}]({r['url']})"
    typ = r.get("type", "")
    published = r.get("published", "unknown")
    added = r.get("added", "")
    date_field = published if published != "unknown" else added
    other_labels = [l for l in parse_labels(r.get("labels", "")) if l not in DOMAINS]
    return f"| {link} | {typ} | {date_field} | {', '.join(other_labels[:4])} |"


def render_category(domain: str, sources: list[dict], tools: list[dict]) -> str:
    sources_in = [r for r in sources if domain in parse_labels(r.get("labels", ""))]
    tools_in = [r for r in tools if domain in parse_labels(r.get("labels", ""))]
    if not sources_in and not tools_in:
        return ""

    parts = [f"### {domain}\n", DOMAIN_BLURB.get(domain, ""), ""]

    if tools_in:
        tools_sorted = sorted(tools_in, key=lambda r: int(r.get("stars", 0) or 0), reverse=True)
        parts.append(f"<details><summary><strong>Repos</strong> ({len(tools_sorted)})</summary>\n")
        parts.append("| Repo | Language | Stars | Last pushed | Description |")
        parts.append("|---|---|---|---|---|")
        parts.extend(render_repo_row(r) for r in tools_sorted)
        parts.append("</details>\n")

    if sources_in:
        articles = [r for r in sources_in if r.get("type") == "article"]
        videos = [r for r in sources_in if r.get("type") == "video"]
        other = [r for r in sources_in if r.get("type") not in ("article", "video")]

        for label, group in (("Articles", articles), ("Videos", videos), ("Other reading", other)):
            if not group:
                continue
            group_sorted = sorted(group, key=lambda r: r.get("added", ""), reverse=True)
            parts.append(f"<details><summary><strong>{label}</strong> ({len(group_sorted)})</summary>\n")
            parts.append("| Title | Type | Date | Labels |")
            parts.append("|---|---|---|---|")
            parts.extend(render_source_row(r) for r in group_sorted)
            parts.append("</details>\n")

    return "\n".join(parts)


def render_unlabeled(rows: list[dict]) -> str:
    if not rows:
        return ""
    return (
        f"\n### Unlabeled\n\n"
        f"{len(rows)} rows do not yet carry a domain label and need triage. "
        f"See `INDEX/sources.md` and `INDEX/tools.md` for the full list — "
        f"any row whose `labels` does not include one of the 12 domain labels "
        f"lands here.\n"
    )


def render_toc(domains_with_content: list[str]) -> str:
    lines = []
    for d in domains_with_content:
        anchor = d.replace("-", "-")
        lines.append(f"- [{d}](#{anchor})")
    return "\n".join(lines)


def render_stats(src_active: int, src_arch: int, tool_active: int, tool_arch: int) -> str:
    return (
        f"- **Sources:** {src_active} active, {src_arch} archived\n"
        f"- **Repos:** {tool_active} active, {tool_arch} archived\n"
        f"- **Last regenerated:** {date.today().isoformat()}"
    )


def render_archived_summary(src_arch: int, tool_arch: int) -> str:
    return (
        f"- [_archived/sources.md](./_archived/sources.md) — {src_arch} dead links, "
        "kept as tombstones with `last_seen` and `reason`.\n"
        f"- [_archived/tools.md](./_archived/tools.md) — {tool_arch} archived/EOL/stale repos."
    )


def render_triage_preview(triage_path: Path) -> str:
    if not triage_path.exists():
        return "_TRIAGE.md not yet bootstrapped._"
    txt = triage_path.read_text()
    # Pull first 15 row-lines under any section header.
    rows = [l for l in txt.splitlines() if l.startswith("| ") and not l.strip().startswith("|---")]
    if not rows:
        return "_No candidates queued. Run `/triage-releases` to scan._"
    return f"Last {min(15, len(rows))} of {len(rows)} queued candidates — see [TRIAGE.md](./TRIAGE.md).\n"


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(
        rf"(<!--\s*BEGIN:\s*{re.escape(name)}\s*-->)(.*?)(<!--\s*END:\s*{re.escape(name)}\s*-->)",
        re.DOTALL,
    )
    if not pattern.search(text):
        return text  # marker absent; skip
    return pattern.sub(lambda m: f"{m.group(1)}\n{content}\n{m.group(3)}", text)


HARDCODED_README = """\
<!-- This file is regenerated from INDEX/ by `.github/scripts/regen-readme.py`. -->
<!-- Sections between `<!-- BEGIN: name -->` / `<!-- END: name -->` markers are -->
<!-- managed by the regen script. Edit the surrounding prose freely. -->

# awesome-engineering-research

A curated and machine-maintained reading + tools corpus covering distributed systems, language runtimes, functional programming, observability, infrastructure, AI applications, and adjacent areas. Sources and starred repos are deduplicated, labelled against a fixed taxonomy, periodically re-validated for liveness, and rendered to this README from `INDEX/`.

<!-- BEGIN: badges -->
<!-- END: badges -->

## Stats

<!-- BEGIN: stats -->
<!-- END: stats -->

## Table of contents

<!-- BEGIN: toc -->
<!-- END: toc -->

- [Triage queue](#triage-queue)
- [Archived](#archived)
- [How to contribute](#how-to-contribute)
- [Underlying model](#underlying-model)
- [License](#license)

## Categories

<!-- BEGIN: categories -->
<!-- END: categories -->

## Triage queue

<!-- BEGIN: triage -->
<!-- END: triage -->

## Archived

<!-- BEGIN: archived -->
<!-- END: archived -->

## How to contribute

Use the `add-source` skill:

- Slash command: `/add-source <url>` from inside this repo with Claude Code.
- Or open a PR adding a row to `INDEX/sources.md` or `INDEX/tools.md` following the column shape in `.claude/templates/source.md` / `.claude/templates/repo.md`. The `frontmatter-lint` workflow will validate it.

Dead links and EOL repos are never deleted — they move to `_archived/` with a `last_seen` date and a `reason`. See `.claude/skills/dead-link-sweep/SKILL.md` and `.claude/skills/star-sweep/SKILL.md`.

## Underlying model

This is an awesome-list face on top of an agent-readable knowledge graph. The canonical spec lives at `.claude/skills/research-standard/SKILL.md`. The label vocabulary is at `.claude/skills/research-standard/TAXONOMY/domains.md`. Seven GitHub Actions keep the corpus current: cron sweeps (`link-check`, `star-sweep`, `new-releases-triage`) open `agent-authored` PRs; an `auto-review` quality gate validates each PR against the relevant part of the standard, auto-merges on approval, or posts a `@claude` request-changes review that triggers `claude-respond` to apply the fixes — closing the loop without human intervention.

## License

CC0 1.0 Universal — see [LICENSE](./LICENSE).
"""


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sources", required=True)
    p.add_argument("--tools", required=True)
    p.add_argument("--template")  # currently unused; reserved
    p.add_argument("--taxonomy")  # currently unused; reserved
    p.add_argument("--triage")
    p.add_argument("--archived-sources", default="_archived/sources.md")
    p.add_argument("--archived-tools", default="_archived/tools.md")
    p.add_argument("--output", required=True)
    args = p.parse_args()

    sources = parse_table(Path(args.sources).read_text())
    tools = parse_table(Path(args.tools).read_text())
    arch_sources = parse_table(Path(args.archived_sources).read_text()) if Path(args.archived_sources).exists() else []
    arch_tools = parse_table(Path(args.archived_tools).read_text()) if Path(args.archived_tools).exists() else []

    # Build category blocks
    cat_blocks: list[str] = []
    domains_with_content: list[str] = []
    for d in DOMAINS:
        block = render_category(d, sources, tools)
        if block:
            cat_blocks.append(f'<a id="{d}"></a>\n\n{block}')
            domains_with_content.append(d)

    # Unlabeled overflow
    sources_unlabeled = [r for r in sources if not any(l in DOMAINS for l in parse_labels(r.get("labels", "")))]
    tools_unlabeled = [r for r in tools if not any(l in DOMAINS for l in parse_labels(r.get("labels", "")))]
    if sources_unlabeled or tools_unlabeled:
        cat_blocks.append(render_unlabeled(sources_unlabeled + tools_unlabeled))

    # Compose
    output_path = Path(args.output)
    base = output_path.read_text() if output_path.exists() else HARDCODED_README
    if "<!-- BEGIN: categories -->" not in base:
        base = HARDCODED_README

    base = replace_block(base, "badges", (
        "![link-check](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/link-check.yml/badge.svg) "
        "![star-sweep](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/star-sweep.yml/badge.svg) "
        "![lint](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/frontmatter-lint.yml/badge.svg)"
    ))
    base = replace_block(base, "stats", render_stats(len(sources), len(arch_sources), len(tools), len(arch_tools)))
    base = replace_block(base, "toc", render_toc(domains_with_content))
    base = replace_block(base, "categories", "\n\n".join(cat_blocks))
    base = replace_block(base, "triage", render_triage_preview(Path(args.triage)) if args.triage else "_no triage_")
    base = replace_block(base, "archived", render_archived_summary(len(arch_sources), len(arch_tools)))

    output_path.write_text(base)
    print(f"wrote {output_path} ({output_path.stat().st_size} bytes)")
    print(f"  domains rendered: {len(domains_with_content)}")
    print(f"  sources: {len(sources)} active, {len(arch_sources)} archived")
    print(f"  tools:   {len(tools)} active, {len(arch_tools)} archived")
    if sources_unlabeled or tools_unlabeled:
        print(f"  unlabeled overflow: {len(sources_unlabeled)} sources, {len(tools_unlabeled)} tools")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

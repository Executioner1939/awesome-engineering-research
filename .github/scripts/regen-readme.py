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


# Fine-grained categories in render order. Source-of-truth lives at
# .claude/skills/research-standard/TAXONOMY/categories.md; this list must stay
# in sync with that file.
CATEGORIES: list[tuple[str, str]] = [
    # (parent group label, category slug)
    ("Data plane", "relational-databases"),
    ("Data plane", "columnar-databases"),
    ("Data plane", "time-series-databases"),
    ("Data plane", "vector-databases"),
    ("Data plane", "graph-databases"),
    ("Data plane", "document-databases"),
    ("Data plane", "wide-column-databases"),
    ("Data plane", "kv-stores"),
    ("Data plane", "caches"),
    ("Data plane", "embedded-databases"),
    ("Data plane", "search-engines"),
    ("Data plane", "object-stores"),
    ("Data plane", "message-queues"),
    ("Data plane", "stream-processing"),
    ("Data plane", "multi-model-databases"),
    ("Language & runtime", "async-runtimes"),
    ("Language & runtime", "effect-systems"),
    ("Language & runtime", "compilers"),
    ("Language & runtime", "parsers"),
    ("Language & runtime", "static-analyzers"),
    ("Language & runtime", "type-checkers"),
    ("Language & runtime", "garbage-collectors"),
    ("Distributed systems", "consensus"),
    ("Distributed systems", "event-sourcing"),
    ("Distributed systems", "cqrs"),
    ("Distributed systems", "workflow-engines"),
    ("Distributed systems", "service-meshes"),
    ("Distributed systems", "api-gateways"),
    ("Distributed systems", "rpc-frameworks"),
    ("Distributed systems", "service-discovery"),
    ("Observability", "distributed-tracing"),
    ("Observability", "metrics"),
    ("Observability", "logging"),
    ("Observability", "profiling"),
    ("Observability", "continuous-profiling"),
    ("Observability", "apm"),
    ("Observability", "opentelemetry-libs"),
    ("AI / LLM", "agent-frameworks"),
    ("AI / LLM", "llm-app-frameworks"),
    ("AI / LLM", "rag-retrieval"),
    ("AI / LLM", "embeddings"),
    ("AI / LLM", "model-serving"),
    ("AI / LLM", "mcp-tooling"),
    ("AI / LLM", "llm-evaluation"),
    ("AI / LLM", "prompt-engineering"),
    ("AI / LLM", "llm-clients-sdks"),
    ("Infrastructure", "container-orchestration"),
    ("Infrastructure", "iac"),
    ("Infrastructure", "gitops"),
    ("Infrastructure", "build-systems"),
    ("Infrastructure", "monorepo-tooling"),
    ("Infrastructure", "container-runtimes"),
    ("Infrastructure", "package-registries"),
    ("Security", "authentication"),
    ("Security", "authorization-policy"),
    ("Security", "secrets-management"),
    ("Security", "supply-chain-security"),
    ("Security", "code-signing"),
    ("Security", "vulnerability-scanning"),
    ("Security", "cryptography-libs"),
    ("Security", "network-security"),
    ("Developer experience", "cli-frameworks"),
    ("Developer experience", "code-editors"),
    ("Developer experience", "linters-formatters"),
    ("Developer experience", "code-review-automation"),
    ("Developer experience", "documentation-generators"),
    ("Developer experience", "shells-terminals"),
    ("Developer experience", "dotfiles"),
    ("Functional programming", "algebraic-effects"),
    ("Functional programming", "optics-lenses"),
    ("Functional programming", "streaming-libs"),
    ("Functional programming", "property-based-testing"),
    ("Functional programming", "type-classes-prelude"),
    ("Frontend & web", "ui-frameworks"),
    ("Frontend & web", "component-systems"),
    ("Frontend & web", "design-systems"),
    ("Frontend & web", "web-performance"),
    ("Frontend & web", "wasm"),
    ("Frontend & web", "bundlers"),
    ("Frontend & web", "css-tooling"),
    ("Standards & specs", "rfcs"),
    ("Standards & specs", "w3c-specs"),
    ("Standards & specs", "oauth-oidc"),
    ("Standards & specs", "web-platform-specs"),
    ("Standards & specs", "cryptographic-standards"),
    ("Knowledge & curation", "awesome-lists"),
    ("Knowledge & curation", "knowledge-graphs"),
    ("Knowledge & curation", "learning-resources"),
    ("Knowledge & curation", "interview-prep"),
    ("Triage", "unsorted"),
]

# Acronym capitalisations for prettier humanised headings.
_ACRONYMS = {
    "iac": "IaC", "apm": "APM", "llm": "LLM", "rag": "RAG",
    "sdks": "SDKs", "cqrs": "CQRS", "rpc": "RPC", "cli": "CLI",
    "wasm": "WASM", "css": "CSS", "ui": "UI", "rfcs": "RFCs",
    "w3c": "W3C", "oidc": "OIDC", "oauth": "OAuth", "mcp": "MCP",
    "kv": "KV", "ci": "CI", "cd": "CD",
}


def humanize(category: str) -> str:
    words = []
    for w in category.split("-"):
        words.append(_ACRONYMS.get(w.lower(), w.capitalize()))
    return " ".join(words)


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
    labels = ", ".join(parse_labels(r.get("labels", ""))[:4])
    return f"| {link} | {typ} | {date_field} | {labels} |"


def render_repos_section(label: str, repos: list[dict]) -> list[str]:
    parts = [f"#### {label} ({len(repos)})\n",
             "| Repo | Language | Stars | Last pushed | Description |",
             "| :--- | :--- | ---: | :--- | :--- |"]
    parts.extend(render_repo_row(r) for r in sorted(repos, key=lambda x: int(x.get("stars", 0) or 0), reverse=True))
    parts.append("")
    return parts


def render_sources_section(label: str, sources: list[dict]) -> list[str]:
    parts = [f"#### {label} ({len(sources)})\n",
             "| Title | Type | Date | Labels |",
             "| :--- | :--- | :--- | :--- |"]
    parts.extend(render_source_row(r) for r in sorted(sources, key=lambda x: x.get("added", ""), reverse=True))
    parts.append("")
    return parts


def render_category(category: str, sources: list[dict], tools: list[dict]) -> str:
    sources_in = [r for r in sources if r.get("category") == category]
    tools_in = [r for r in tools if r.get("category") == category]
    if not sources_in and not tools_in:
        return ""

    parts = ["---", "", f"## {humanize(category)}", ""]

    # Sub-headings for repos, by kind
    by_kind: dict[str, list[dict]] = defaultdict(list)
    for r in tools_in:
        by_kind[r.get("kind", "unsorted")].append(r)
    for kind_label, kind_key in (("Tools", "tool"), ("Libraries", "library"),
                                 ("Frameworks", "framework"), ("Unsorted", "unsorted")):
        if by_kind.get(kind_key):
            parts.extend(render_repos_section(kind_label, by_kind[kind_key]))

    # Sub-headings for sources, by type
    by_type: dict[str, list[dict]] = defaultdict(list)
    for r in sources_in:
        by_type[r.get("type", "article")].append(r)
    if by_type.get("article"):
        parts.extend(render_sources_section("Articles", by_type["article"]))
    if by_type.get("video"):
        parts.extend(render_sources_section("Videos", by_type["video"]))
    other_source_types = [t for t in by_type if t not in ("article", "video")]
    if other_source_types:
        merged: list[dict] = []
        for t in other_source_types:
            merged.extend(by_type[t])
        parts.extend(render_sources_section("Other reading", merged))

    return "\n".join(parts)


def render_unlabeled(_rows: list[dict]) -> str:
    return ""


def render_toc(categories_with_content: list[str]) -> str:
    lines = []
    last_group = None
    group_by_cat = {c: g for g, c in CATEGORIES}
    for c in categories_with_content:
        g = group_by_cat.get(c, "Triage")
        if g != last_group:
            lines.append(f"\n**{g}**\n")
            last_group = g
        lines.append(f"- [{humanize(c)}](#{c})")
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
# awesome-engineering-research

A curated and machine-maintained reading + tools corpus covering distributed systems, language runtimes, functional programming, observability, infrastructure, AI applications, and adjacent areas. Sources and starred repos are deduplicated, labelled against a fixed taxonomy, periodically re-validated for liveness, and rendered to this README from `INDEX/`.

<!-- BEGIN: badges -->
<!-- END: badges -->

## Stats

<!-- BEGIN: stats -->
<!-- END: stats -->

---

## Table of contents

<!-- BEGIN: toc -->
<!-- END: toc -->

- [Triage queue](#triage-queue)
- [Archived](#archived)
- [License](#license)

---

## Categories

<!-- BEGIN: categories -->
<!-- END: categories -->

---

## Triage queue

<!-- BEGIN: triage -->
<!-- END: triage -->

---

## Archived

<!-- BEGIN: archived -->
<!-- END: archived -->

---

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
    categories_with_content: list[str] = []
    for _group, c in CATEGORIES:
        block = render_category(c, sources, tools)
        if block:
            cat_blocks.append(f'<a id="{c}"></a>\n\n{block}')
            categories_with_content.append(c)

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
    base = replace_block(base, "toc", render_toc(categories_with_content))
    base = replace_block(base, "categories", "\n\n".join(cat_blocks))
    base = replace_block(base, "triage", render_triage_preview(Path(args.triage)) if args.triage else "_no triage_")
    base = replace_block(base, "archived", render_archived_summary(len(arch_sources), len(arch_tools)))

    output_path.write_text(base)
    print(f"wrote {output_path} ({output_path.stat().st_size} bytes)")
    print(f"  categories rendered: {len(categories_with_content)}")
    print(f"  sources: {len(sources)} active, {len(arch_sources)} archived")
    print(f"  tools:   {len(tools)} active, {len(arch_tools)} archived")
    unsorted_sources = sum(1 for r in sources if r.get("category") == "unsorted")
    unsorted_tools = sum(1 for r in tools if r.get("category") == "unsorted")
    if unsorted_sources or unsorted_tools:
        print(f"  unsorted: {unsorted_sources} sources, {unsorted_tools} tools")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

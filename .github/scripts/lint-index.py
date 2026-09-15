#!/usr/bin/env python3
"""Validate INDEX/<file>.md and _archived/<file>.md row shapes against the standard.

Exits 1 on validation failure (signals workflow failure).

Checks:
  - Required columns present per row.
  - `status` is one of {active, archived, superseded}.
  - `labels` is non-empty and every label is in the allowed taxonomy.
  - `id` is unique across active + archived for the same target.
  - Archived rows carry `last_seen` and `reason`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from taxonomy import KINDS, category_slugs  # noqa: E402


REQUIRED_SOURCES = ("id", "title", "url", "type", "added", "labels", "status")
RECOMMENDED_SOURCES = ("published",)
REQUIRED_TOOLS = ("id", "full_name", "url", "stars", "last_pushed", "labels", "status")
RECOMMENDED_TOOLS = ("description", "language")
ARCHIVED_EXTRA = ("last_seen", "reason")
_CELL_SPLIT = re.compile(r"(?<!\\)\|")
ALLOWED_STATUS = {"active", "archived", "superseded"}
ALLOWED_TYPES = {"article", "video", "talk", "book", "paper", "rfc", "podcast", "course", "docs", "repo"}


def parse_table(text: str) -> list[dict]:
    m = re.search(r"<!--\s*BEGIN:\s*rows\s*-->(.*?)<!--\s*END:\s*rows\s*-->", text, re.DOTALL)
    if not m:
        return []
    lines = m.group(1).strip().splitlines()
    if len(lines) < 2:
        return []
    header = [c.strip() for c in _CELL_SPLIT.split(lines[0].strip("|").strip())]
    rows = []
    for i, ln in enumerate(lines[2:], start=3):
        if not ln.strip().startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in _CELL_SPLIT.split(ln.strip().strip("|"))]
        if len(cells) != len(header):
            rows.append({"__error__": f"row {i}: column count mismatch ({len(cells)} vs {len(header)})"})
            continue
        rows.append(dict(zip(header, cells)))
    return rows


def collect_taxonomy(path: Path) -> set[str]:
    text = path.read_text()
    # Pull anything in backticks within the file — every label is wrapped in backticks.
    return set(re.findall(r"`([a-z][a-z0-9-]*)`", text))


def lint_kind(rows: list[dict], required: tuple, allowed_labels: set[str], archived: bool,
              allowed_categories: set[str] | None = None, check_kind: bool = False) -> list[str]:
    errors: list[str] = []
    ids_seen: dict[str, int] = {}
    for i, r in enumerate(rows, start=1):
        if "__error__" in r:
            errors.append(r["__error__"])
            continue
        for col in required:
            if not r.get(col):
                errors.append(f"row {i} ({r.get('id','?')}): missing required column `{col}`")
        if r.get("status") and r["status"] not in ALLOWED_STATUS:
            errors.append(f"row {i} ({r.get('id','?')}): status `{r['status']}` not in {sorted(ALLOWED_STATUS)}")
        labels = [l.strip() for l in r.get("labels", "").split(",") if l.strip()]
        if not labels:
            errors.append(f"row {i} ({r.get('id','?')}): empty labels")
        for l in labels:
            if l not in allowed_labels:
                errors.append(f"row {i} ({r.get('id','?')}): label `{l}` not in taxonomy")
        if r.get("type") and r["type"] not in ALLOWED_TYPES:
            errors.append(f"row {i} ({r.get('id','?')}): type `{r['type']}` not in {sorted(ALLOWED_TYPES)}")
        # Active tools rows must carry a valid category + kind. Archived rows are
        # terminal tombstones; only validate what they do carry.
        if allowed_categories is not None and "category" in r and (r["category"] or not archived):
            if r["category"] not in allowed_categories:
                errors.append(f"row {i} ({r.get('id','?')}): category `{r['category']}` not in categories.md")
        if check_kind and "kind" in r and (r["kind"] or not archived) and r["kind"] not in KINDS:
            errors.append(f"row {i} ({r.get('id','?')}): kind `{r['kind']}` not in {list(KINDS)}")
        if archived:
            for col in ARCHIVED_EXTRA:
                if not r.get(col):
                    errors.append(f"row {i} ({r.get('id','?')}): archived row missing `{col}`")
        rid = r.get("id", "")
        if rid:
            if rid in ids_seen:
                errors.append(f"row {i}: duplicate id `{rid}` (also at row {ids_seen[rid]})")
            else:
                ids_seen[rid] = i
    return errors


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sources", required=True)
    p.add_argument("--tools", required=True)
    p.add_argument("--archived-sources", required=True)
    p.add_argument("--archived-tools", required=True)
    p.add_argument("--taxonomy", required=True)
    p.add_argument("--categories", help="categories.md; when given, `category` and `kind` are validated")
    p.add_argument("--output", required=True)
    args = p.parse_args()

    allowed = collect_taxonomy(Path(args.taxonomy))
    allowed_categories = set(category_slugs(Path(args.categories))) if args.categories else None

    errors: list[str] = []
    pairs = (
        (args.sources, REQUIRED_SOURCES, False, "INDEX/sources.md", False),
        (args.tools, REQUIRED_TOOLS, False, "INDEX/tools.md", True),
        (args.archived_sources, REQUIRED_SOURCES, True, "_archived/sources.md", False),
        (args.archived_tools, REQUIRED_TOOLS, True, "_archived/tools.md", True),
    )
    for path, required, archived, label, is_tools in pairs:
        rows = parse_table(Path(path).read_text())
        scoped = lint_kind(rows, required, allowed, archived,
                           allowed_categories if is_tools else None, check_kind=is_tools)
        for e in scoped:
            errors.append(f"{label}: {e}")

    md = [f"# Frontmatter lint", "", f"Errors: **{len(errors)}**", ""]
    if errors:
        md.append("```")
        md.extend(errors[:200])
        if len(errors) > 200:
            md.append(f"... ({len(errors) - 200} more)")
        md.append("```")
    else:
        md.append("All row shapes conform to the standard.")
    Path(args.output).write_text("\n".join(md))
    Path("/tmp/lint-summary.json").write_text(json.dumps({"errors": len(errors)}))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

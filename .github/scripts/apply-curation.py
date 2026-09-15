#!/usr/bin/env python3
"""Apply a curation decision file to INDEX/tools.md.

The curation step (Claude) does not edit the index by hand. It writes
/tmp/star-curation.json and this script applies it deterministically, so
the table never ends up with a broken shape or an invented vocabulary.

Decision file shape (one entry per row id):

    {
      "tokio-rs-tokio": {
        "category": "async-runtimes",
        "kind": "library",
        "labels": ["language-runtimes", "rust", "tokio", "async-runtimes"],
        "description": "Event-driven, non-blocking I/O runtime for writing reliable async applications in Rust.",
        "notes": ""                                  # optional
      },
      ...
    }

Validation (each failure is reported; --strict makes any failure exit 1):
  * category must exist in categories.md
  * kind must be one of tool | library | framework | content | unsorted
  * every label must exist in domains.md and at least one must be a domain label
  * description: 20..220 chars, single line, no leading emoji, no trailing period spam
Entries that fail validation are skipped (row keeps its previous values).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from taxonomy import KINDS, category_slugs, read_labels  # noqa: E402

DOMAINS = {"developer-tooling", "ai-applications", "infrastructure", "distributed-systems",
           "language-runtimes", "data-storage", "security", "observability", "frontend",
           "knowledge-systems", "web-extraction", "standards"}
_SPLIT = re.compile(r"(?<!\\)\|")


def parse_table(text: str):
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
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return prefix, lines[:2], rows, suffix


def cell(v) -> str:
    return re.sub(r"\s+", " ", str(v if v is not None else "")).strip().replace("|", "\\|")


def render_rows(header, rows) -> str:
    cols = [c.strip() for c in header[0].strip("|").split("|")]
    out = list(header)
    for r in sorted(rows, key=lambda x: x.get("id", "")):
        out.append("| " + " | ".join(cell(r.get(c, "")) for c in cols) + " |")
    return "\n".join(out)


def validate(rid: str, d: dict, cats: set[str], labels_ok: set[str]) -> list[str]:
    errs = []
    cat = d.get("category")
    if cat not in cats:
        errs.append(f"{rid}: category `{cat}` is not in categories.md")
    if d.get("kind") not in KINDS:
        errs.append(f"{rid}: kind `{d.get('kind')}` not in {KINDS}")
    labels = d.get("labels") or []
    if isinstance(labels, str):
        labels = [l.strip() for l in labels.split(",") if l.strip()]
    if not labels:
        errs.append(f"{rid}: labels empty")
    for l in labels:
        if l not in labels_ok:
            errs.append(f"{rid}: label `{l}` is not in domains.md")
    if labels and not any(l in DOMAINS for l in labels):
        errs.append(f"{rid}: no domain label among {labels}")
    desc = re.sub(r"\s+", " ", (d.get("description") or "")).strip()
    if not 20 <= len(desc) <= 220:
        errs.append(f"{rid}: description length {len(desc)} outside 20..220")
    if re.match(r"^[^\w\[(\"'`]", desc):
        errs.append(f"{rid}: description starts with a symbol/emoji")
    d["_labels"] = sorted(set(labels))
    d["_description"] = desc
    return errs


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--decisions", default="/tmp/star-curation.json")
    p.add_argument("--tools", default="INDEX/tools.md")
    p.add_argument("--categories", default=".claude/skills/research-standard/TAXONOMY/categories.md")
    p.add_argument("--taxonomy", default=".claude/skills/research-standard/TAXONOMY/domains.md")
    p.add_argument("--report", default="/tmp/star-curation-report.md")
    p.add_argument("--strict", action="store_true")
    args = p.parse_args()

    decisions = json.loads(Path(args.decisions).read_text())
    if not isinstance(decisions, dict):
        raise SystemExit("decision file must be an object keyed by row id")
    cats = set(category_slugs(Path(args.categories)))
    labels_ok = read_labels(Path(args.taxonomy))

    prefix, header, rows, suffix = parse_table(Path(args.tools).read_text())
    by_id = {r["id"]: r for r in rows}

    applied, errors, unknown = [], [], []
    for rid, d in decisions.items():
        if rid not in by_id:
            unknown.append(rid)
            continue
        errs = validate(rid, d, cats, labels_ok)
        if errs:
            errors.extend(errs)
            continue
        row = by_id[rid]
        row["category"] = d["category"]
        row["kind"] = d["kind"]
        row["labels"] = ",".join(d["_labels"])
        row["description"] = d["_description"]
        if "notes" in d and d["notes"] is not None:
            row["notes"] = str(d["notes"])
        applied.append(rid)

    Path(args.tools).write_text(prefix + render_rows(header, rows) + suffix)

    md = [f"# Curation apply", "", f"- applied: **{len(applied)}**",
          f"- rejected: **{len(errors)}**", f"- unknown ids: **{len(unknown)}**", ""]
    if errors:
        md += ["## Rejected", "```", *errors, "```", ""]
    if unknown:
        md += ["## Unknown ids", ", ".join(unknown), ""]
    Path(args.report).write_text("\n".join(md))
    print("\n".join(md))
    return 1 if (args.strict and (errors or unknown)) else 0


if __name__ == "__main__":
    raise SystemExit(main())

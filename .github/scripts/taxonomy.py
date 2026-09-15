#!/usr/bin/env python3
"""Shared readers for the taxonomy files.

categories.md is the source of truth for `category` values (grouped under
`## <group>` headings, one `| category | scope |` table per group).
domains.md is the source of truth for `labels` (every backticked slug).
"""
from __future__ import annotations

import re
from pathlib import Path

KINDS = ("tool", "library", "framework", "content", "unsorted")
_SPLIT = re.compile(r"(?<!\\)\|")


def read_categories(path: Path) -> list[tuple[str, str, str]]:
    """Return [(group, category, scope)] in file order."""
    out: list[tuple[str, str, str]] = []
    group = None
    in_cat_table = False
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            group = line[3:].strip()
            in_cat_table = False
            continue
        if line.startswith("|"):
            cells = [c.strip() for c in _SPLIT.split(line.strip().strip("|"))]
            if cells and cells[0].lower() == "category":
                in_cat_table = True
                continue
            if in_cat_table and cells and set(cells[0]) <= set("-: "):
                continue
            if in_cat_table and group and len(cells) >= 2:
                slug = cells[0].strip("`").strip()
                if re.fullmatch(r"[a-z][a-z0-9-]*", slug):
                    out.append((group, slug, cells[1]))
            continue
        in_cat_table = False
    return out


def category_slugs(path: Path) -> list[str]:
    return [c for _, c, _ in read_categories(path)]


def read_labels(path: Path) -> set[str]:
    return set(re.findall(r"`([a-z][a-z0-9-]*)`", path.read_text()))

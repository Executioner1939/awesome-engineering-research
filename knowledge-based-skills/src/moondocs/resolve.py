"""Entity resolution (pure local, no LLM).

The same field shows up as `deps`, `task.deps`, `Task.deps`,
`dependencies` across pages. We map all observed surface forms to one
canonical id before loading the graph.

Two-stage funnel for the PoC:
  1. String normalize -> exact-match buckets.
  2. Embed remaining heads with fastembed; merge pairs with cosine
     above the threshold (default 0.92).

The original spec called for a Sonnet tie-breaker on the ambiguous
0.85-0.92 band; that's now an explicit gap-report finding instead
(see queries.py).
"""
from __future__ import annotations

import json
import os
import re
from pathlib import Path

import numpy as np
from rich.console import Console

from .embed import embed
from .schema import CanonicalEntity

console = Console()
DATA_EXTRACTED = Path("data/extracted")

COSINE_HIGH = float(os.environ.get("RESOLVE_COSINE_THRESHOLD", "0.92"))


def _normalize(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[._\-/]+", ".", s)
    s = re.sub(r"\.+", ".", s).strip(".")
    return s


def _collect_entities() -> list[dict]:
    rows: list[dict] = []
    for p in sorted(DATA_EXTRACTED.glob("*.json")):
        if p.name.startswith("_") or p.name.endswith(".det.json"):
            continue
        data = json.loads(p.read_text())
        for e in data.get("entities", []):
            rows.append({**e, "url": data["url"]})
    return rows


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    denom = (np.linalg.norm(a) * np.linalg.norm(b)) or 1.0
    return float(np.dot(a, b) / denom)


def _resolve(rows: list[dict]) -> dict:
    buckets: dict[tuple[str, str], list[dict]] = {}
    for r in rows:
        key = (r["type"], _normalize(r["id"]))
        buckets.setdefault(key, []).append(r)

    canonicals: list[dict] = []
    surface_to_canon: dict[str, str] = {}
    for _, group in buckets.items():
        rep = min(group, key=lambda r: len(r["id"]))
        canon_id = _normalize(rep["id"])
        canonicals.append(
            {
                "canonical_id": canon_id,
                "type": rep["type"],
                "surface_forms": sorted({r["id"] for r in group}),
                "description": rep.get("description", ""),
                "first_seen_url": rep["url"],
            }
        )
        for r in group:
            surface_to_canon[r["id"]] = canon_id

    by_type: dict[str, list[dict]] = {}
    for c in canonicals:
        by_type.setdefault(c["type"], []).append(c)

    merge_map: dict[str, str] = {}
    for _, group in by_type.items():
        if len(group) < 2:
            continue
        texts = [f"{c['canonical_id']}: {c['description'][:200]}" for c in group]
        vecs = embed(texts)
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                if group[i]["canonical_id"] in merge_map or group[j]["canonical_id"] in merge_map:
                    continue
                if _cosine(vecs[i], vecs[j]) >= COSINE_HIGH:
                    merge_map[group[j]["canonical_id"]] = group[i]["canonical_id"]

    final: dict[str, dict] = {}
    for c in canonicals:
        cid = c["canonical_id"]
        while cid in merge_map:
            cid = merge_map[cid]
        if cid not in final:
            final[cid] = {
                "canonical_id": cid,
                "type": c["type"],
                "surface_forms": [],
                "description": c["description"],
                "first_seen_url": c["first_seen_url"],
            }
        final[cid]["surface_forms"].extend(c["surface_forms"])

    for sf, cid in list(surface_to_canon.items()):
        while cid in merge_map:
            cid = merge_map[cid]
        surface_to_canon[sf] = cid

    for f in final.values():
        f["surface_forms"] = sorted(set(f["surface_forms"]))

    canonical_list = [CanonicalEntity(**v).model_dump() for v in final.values()]
    return {"surface_to_canonical": surface_to_canon, "canonical_entities": canonical_list}


def main() -> None:
    rows = _collect_entities()
    console.print(f"[cyan]resolving {len(rows)} entity surface forms[/]")
    result = _resolve(rows)
    out = DATA_EXTRACTED / "_canonical.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    console.print(
        f"[green]canonicalised: {len(rows)} surface forms -> "
        f"{len(result['canonical_entities'])} canonical entities[/]"
    )


if __name__ == "__main__":
    main()

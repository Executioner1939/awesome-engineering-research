"""Gap-finding Cypher.

Each query name corresponds to one section in the gap report. Each
returns a list[dict] of findings; the markdown writer at the bottom of
this module composes them into reports/gaps-{ts}.md.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

from falkordb import FalkorDB
from rich.console import Console

console = Console()
REPORTS = Path("reports")


def _g():
    host = os.environ.get("FALKOR_HOST", "localhost")
    port = int(os.environ.get("FALKOR_PORT", "6379"))
    name = os.environ.get("FALKOR_GRAPH", "moondocs")
    return FalkorDB(host=host, port=port).select_graph(name)


# ---------------------------------------------------------------------------
# 1. Inferred-but-undocumented edges
# ---------------------------------------------------------------------------

def inferred_undocumented(limit: int = 50) -> list[dict]:
    g = _g()
    q = """
    MATCH (a:Entity)-[r]->(b:Entity)
    WHERE r.confidence < 0.6 OR r.evidence IS NULL OR r.evidence = ''
    RETURN a.canonical_id, type(r), b.canonical_id, r.confidence, r.evidence, r.page_url
    ORDER BY r.confidence ASC
    LIMIT $limit
    """
    res = g.query(q, params={"limit": limit})
    return [
        {
            "src": row[0],
            "rel": row[1],
            "dst": row[2],
            "confidence": row[3],
            "evidence": (row[4] or "")[:200],
            "page_url": row[5],
        }
        for row in res.result_set
    ]


# ---------------------------------------------------------------------------
# 2. Orphan ConfigField nodes (code-block evidence only, no prose)
# ---------------------------------------------------------------------------

def orphan_fields(limit: int = 50) -> list[dict]:
    g = _g()
    q = """
    MATCH (e:Entity {type: 'ConfigField'})
    OPTIONAL MATCH (e)-[r]-(o:Entity)
    WITH e, count(r) AS edge_count, collect(DISTINCT r.source) AS sources
    WHERE edge_count <= 1 OR ALL(s IN sources WHERE s = 'deterministic')
    RETURN e.canonical_id, e.description, e.first_seen_url, edge_count
    ORDER BY edge_count ASC, e.canonical_id
    LIMIT $limit
    """
    res = g.query(q, params={"limit": limit})
    return [
        {
            "canonical_id": row[0],
            "description": row[1] or "",
            "first_seen_url": row[2],
            "edge_count": row[3],
        }
        for row in res.result_set
    ]


# ---------------------------------------------------------------------------
# 3. Stale prose: structural pass disagrees with nano-graphrag pass
# ---------------------------------------------------------------------------

def stale_prose(limit: int = 50) -> list[dict]:
    """Surface canonical entities present in the structural pass but
    absent from the independent prose pass — or vice versa.
    Disagreement = candidate stale prose.
    """
    g = _g()
    # FalkorDB Cypher doesn't support EXISTS{MATCH ...} subqueries; use
    # OPTIONAL MATCH + WITH count = 0 instead.
    q = """
    MATCH (e:Entity)
    OPTIONAL MATCH (n:ProseEntity)
      WHERE toLower(n.pid) CONTAINS toLower(e.canonical_id)
         OR ANY(sf IN e.surface_forms WHERE toLower(n.pid) CONTAINS toLower(sf))
    WITH e, count(n) AS matches
    WHERE matches = 0
    RETURN e.canonical_id, e.type, e.first_seen_url
    LIMIT $limit
    """
    res = g.query(q, params={"limit": limit})
    return [
        {"canonical_id": row[0], "type": row[1], "first_seen_url": row[2], "missing_from": "prose_pass"}
        for row in res.result_set
    ]


# ---------------------------------------------------------------------------
# 4. Cross-link gaps: page references an entity by name with no markdown link
# ---------------------------------------------------------------------------

def cross_link_gaps(limit: int = 50) -> list[dict]:
    """For every Entity, find DocChunks whose markdown contains the
    canonical_id but where no REFERENCES edge points from that chunk's
    page to the entity.
    """
    g = _g()
    q = """
    MATCH (e:Entity), (c:DocChunk)
    WHERE c.markdown CONTAINS e.canonical_id
    OPTIONAL MATCH (:Entity)-[r:REFERENCES]->(e)
      WHERE r.page_url = c.url
    WITH e, c, count(r) AS link_count
    WHERE link_count = 0
    RETURN e.canonical_id, c.url, c.heading_path
    LIMIT $limit
    """
    res = g.query(q, params={"limit": limit})
    return [
        {"canonical_id": row[0], "page_url": row[1], "heading_path": row[2]}
        for row in res.result_set
    ]


# ---------------------------------------------------------------------------
# 5. Inheritance dark corners: INHERITS_FROM chains of length > 2 with
#    undocumented intermediate hops.
# ---------------------------------------------------------------------------

def inheritance_dark_corners(limit: int = 50) -> list[dict]:
    g = _g()
    q = """
    MATCH path = (a:Entity)-[:INHERITS_FROM*3..]->(b:Entity)
    WITH path, nodes(path) AS ns, relationships(path) AS rs
    WHERE ANY(r IN rs WHERE r.confidence < 0.7)
    RETURN [n IN ns | n.canonical_id] AS chain,
           [r IN rs | r.confidence] AS confidences,
           [r IN rs | r.evidence] AS evidences
    LIMIT $limit
    """
    res = g.query(q, params={"limit": limit})
    return [
        {"chain": row[0], "confidences": row[1], "evidences": [(e or "")[:120] for e in row[2]]}
        for row in res.result_set
    ]


# ---------------------------------------------------------------------------
# Report writer
# ---------------------------------------------------------------------------


def _section(title: str, findings: list[dict]) -> str:
    if not findings:
        return f"## {title}\n\n_No findings._\n"
    lines = [f"## {title} ({len(findings)})\n"]
    for f in findings:
        lines.append("- " + json.dumps(f, ensure_ascii=False))
    return "\n".join(lines) + "\n"


def main() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    sections = {
        "Inferred-but-undocumented edges": inferred_undocumented(),
        "Orphan ConfigField nodes": orphan_fields(),
        "Stale prose candidates": stale_prose(),
        "Cross-link gaps": cross_link_gaps(),
        "Inheritance dark corners": inheritance_dark_corners(),
    }

    total = sum(len(v) for v in sections.values())
    header = (
        f"# moondocs gap report — {ts}\n\n"
        f"_FalkorDB graph `{os.environ.get('FALKOR_GRAPH', 'moondocs')}`. "
        f"Total findings: {total}._\n\n"
    )

    body = "\n".join(_section(t, v) for t, v in sections.items())
    out = REPORTS / f"gaps-{ts}.md"
    out.write_text(header + body)
    console.print(f"[green]wrote {out}  ({total} findings)[/]")


if __name__ == "__main__":
    main()

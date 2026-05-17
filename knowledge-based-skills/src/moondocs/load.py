"""Load entities + relationships + chunks into FalkorDB.

Three node labels go in:
  - Entity (from data/extracted/_canonical.json + per-page entities)
  - DocChunk (with fastembed embedding)
  - ProseEntity (independent prose-pass output, source='prose' subagent)

Edges:
  - Relationship types from RelType with `evidence`, `confidence`,
    `source` properties. Confidence < 0.5 drops.
  - DOCUMENTS marker stored as a property on the rel (FalkorDB does not
    natively support relationship-to-node edges) — the chunk_id linked
    to each rel goes into r.doc_chunk_id when one matches.

After load: HNSW vector index on DocChunk.embedding.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from falkordb import FalkorDB
from rich.console import Console
from rich.table import Table

from .embed import embed

console = Console()
DATA_PARSED = Path("data/parsed")
DATA_EXTRACTED = Path("data/extracted")
DATA_PROSE = Path("data/prose")

EMBED_DIM = int(os.environ.get("EMBEDDING_DIM", "384"))
MIN_CONFIDENCE = float(os.environ.get("MIN_CONFIDENCE", "0.5"))


def _client() -> FalkorDB:
    return FalkorDB(
        host=os.environ.get("FALKOR_HOST", "localhost"),
        port=int(os.environ.get("FALKOR_PORT", "6379")),
    )


def _graph(client: FalkorDB):
    return client.select_graph(os.environ.get("FALKOR_GRAPH", "moondocs"))


def _chunk_id(url: str, heading_path: list[str]) -> str:
    h = hashlib.sha1(f"{url}|{'>'.join(heading_path)}".encode()).hexdigest()[:16]
    return f"chunk:{h}"


def _load_canonical() -> dict:
    p = DATA_EXTRACTED / "_canonical.json"
    if not p.exists():
        return {"surface_to_canonical": {}, "canonical_entities": []}
    return json.loads(p.read_text())


def _load_extracted() -> list[dict]:
    out = []
    for p in sorted(DATA_EXTRACTED.glob("*.json")):
        if p.name.startswith("_") or p.name.endswith(".det.json"):
            continue
        out.append(json.loads(p.read_text()))
    return out


def _load_prose() -> list[dict]:
    if not DATA_PROSE.exists():
        return []
    out = []
    for p in sorted(DATA_PROSE.glob("*.json")):
        if p.name.startswith("_"):
            continue
        try:
            out.append(json.loads(p.read_text()))
        except json.JSONDecodeError:
            pass
    return out


def _build_chunks() -> list[dict]:
    out: list[dict] = []
    for p in sorted(DATA_PARSED.glob("*.json")):
        if p.name.startswith("_"):
            continue
        data = json.loads(p.read_text())
        for hc in data["heading_chunks"]:
            if not hc["prose"].strip():
                continue
            out.append(
                {
                    "chunk_id": _chunk_id(data["url"], hc["heading_path"]),
                    "url": data["url"],
                    "heading_path": hc["heading_path"],
                    "markdown": hc["prose"],
                }
            )
    return out


def _embed_chunks(chunks: list[dict]) -> None:
    if not chunks:
        return
    texts = [f"{' > '.join(c['heading_path'])}\n\n{c['markdown']}" for c in chunks]
    vecs = embed(texts)
    for c, v in zip(chunks, vecs):
        c["embedding"] = [float(x) for x in v]


def main() -> None:
    console.print("[cyan]loading FalkorDB graph[/]")
    client = _client()
    g = _graph(client)
    try:
        g.delete()
    except Exception:
        pass
    g = _graph(client)

    # ---- canonical entities ----------------------------------------------
    canon = _load_canonical()
    canonicals = canon.get("canonical_entities") or []
    surface_to_canon: dict[str, str] = canon.get("surface_to_canonical") or {}

    if not canonicals:
        seen: dict[tuple[str, str], dict] = {}
        for pg in _load_extracted():
            for e in pg.get("entities", []):
                key = (e["type"], e["id"])
                seen.setdefault(
                    key,
                    {
                        "canonical_id": e["id"],
                        "type": e["type"],
                        "surface_forms": [e["id"]],
                        "description": e.get("description", ""),
                        "first_seen_url": pg["url"],
                    },
                )
        canonicals = list(seen.values())

    console.print(f"  - {len(canonicals)} canonical entities")
    for c in canonicals:
        g.query(
            "CREATE (:Entity {canonical_id: $cid, type: $type, surface_forms: $sf, "
            "description: $desc, first_seen_url: $url})",
            params={
                "cid": c["canonical_id"],
                "type": c["type"],
                "sf": c["surface_forms"],
                "desc": (c.get("description") or "")[:500],
                "url": c.get("first_seen_url", ""),
            },
        )

    # ---- doc chunks ------------------------------------------------------
    chunks = _build_chunks()
    console.print(f"  - {len(chunks)} doc chunks; embedding")
    _embed_chunks(chunks)
    for c in chunks:
        g.query(
            "CREATE (:DocChunk {chunk_id: $cid, url: $url, heading_path: $hp, "
            "markdown: $md, embedding: vecf32($emb)})",
            params={
                "cid": c["chunk_id"],
                "url": c["url"],
                "hp": c["heading_path"],
                "md": c["markdown"][:4000],
                "emb": c["embedding"],
            },
        )

    # ---- relationships (structural pass) ---------------------------------
    rel_count = 0
    doc_link_count = 0

    def canon_of(surface_id: str) -> str:
        return surface_to_canon.get(surface_id, surface_id)

    for pg in _load_extracted():
        url = pg["url"]
        for r in pg.get("relationships", []):
            if r["confidence"] < MIN_CONFIDENCE:
                continue
            src = canon_of(r["src"])
            dst = canon_of(r["dst"])
            rel_type = r["type"]

            # Best-effort chunk match for provenance.
            doc_chunk_id = ""
            chunk_match = g.query(
                "MATCH (c:DocChunk {url: $url}) WHERE c.markdown CONTAINS $needle "
                "RETURN c.chunk_id LIMIT 1",
                params={"url": url, "needle": r["evidence"][:80]},
            )
            if chunk_match.result_set:
                doc_chunk_id = chunk_match.result_set[0][0]
                doc_link_count += 1

            res = g.query(
                f"MATCH (a:Entity {{canonical_id: $src}}), (b:Entity {{canonical_id: $dst}}) "
                f"CREATE (a)-[:{rel_type} {{evidence: $ev, confidence: $conf, "
                f"source: $source, page_url: $url, doc_chunk_id: $ch}}]->(b)",
                params={
                    "src": src,
                    "dst": dst,
                    "ev": r["evidence"][:1000],
                    "conf": r["confidence"],
                    "source": r.get("source", "llm"),
                    "url": url,
                    "ch": doc_chunk_id,
                },
            )
            if res.relationships_created:
                rel_count += 1

    # ---- prose pass entities + relationships (parallel labels) -----------
    prose_pages = _load_prose()
    prose_entities = 0
    prose_rels = 0
    for pg in prose_pages:
        page_url = pg.get("url") or ""
        for e in pg.get("entities", []):
            if not e.get("id"):
                continue
            g.query(
                "CREATE (:ProseEntity {pid: $pid, type: $type, description: $desc, page_url: $url})",
                params={
                    "pid": e["id"],
                    "type": e.get("type") or "Concept",
                    "desc": (e.get("description") or "")[:500],
                    "url": page_url,
                },
            )
            prose_entities += 1
        for r in pg.get("relationships", []):
            if r.get("confidence", 1.0) < MIN_CONFIDENCE:
                continue
            rt = r.get("type")
            if not rt or not r.get("src") or not r.get("dst"):
                continue
            try:
                g.query(
                    f"MATCH (a:ProseEntity {{pid: $s}}), (b:ProseEntity {{pid: $d}}) "
                    f"CREATE (a)-[:{rt} {{evidence: $ev, confidence: $conf, source: 'prose', page_url: $url}}]->(b)",
                    params={
                        "s": r["src"],
                        "d": r["dst"],
                        "ev": (r.get("evidence") or "")[:1000],
                        "conf": float(r.get("confidence", 0.7)),
                        "url": page_url,
                    },
                )
                prose_rels += 1
            except Exception:
                # Bad relationship type or other Cypher rejection; skip.
                continue

    # ---- vector index ----------------------------------------------------
    try:
        g.query(
            f"CREATE VECTOR INDEX FOR (c:DocChunk) ON (c.embedding) "
            f"OPTIONS {{dimension: {EMBED_DIM}, similarityFunction: 'cosine'}}"
        )
    except Exception as e:
        console.print(f"[yellow]vector index create: {e}[/]")

    # ---- summary ---------------------------------------------------------
    summary = Table(title="FalkorDB load summary")
    summary.add_column("Label / type")
    summary.add_column("Count", justify="right")
    summary.add_row("Entity", str(g.query("MATCH (n:Entity) RETURN count(n)").result_set[0][0]))
    summary.add_row("DocChunk", str(g.query("MATCH (n:DocChunk) RETURN count(n)").result_set[0][0]))
    summary.add_row("ProseEntity", str(prose_entities))
    summary.add_row("structural relationships", str(rel_count))
    summary.add_row("prose relationships", str(prose_rels))
    summary.add_row("doc-chunk provenance links", str(doc_link_count))
    console.print(summary)


if __name__ == "__main__":
    main()

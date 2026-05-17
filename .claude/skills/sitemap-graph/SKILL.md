---
name: sitemap-graph
description: Build the URL link graph from a previously captured docs corpus, emitting Mermaid and JSON forms. Use after scrape-firecrawl when a topic needs sitemap visualisation or hub-and-leaf analysis of a docs site.
id: sitemap-graph
title: Build the sitemap graph
type: pipeline
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-17
related: [scrape-firecrawl, extract-knowledge-graph]
---

# Pipeline: Sitemap Graph

Build the URL-level link graph from a captured docs corpus. The graph reveals how information flows and consolidates across pages — which pages are hubs, which are leaves, which are isolated, where there are redirect chains, where the navigation diverges from the link graph.

## Inputs

| name | type | notes |
|---|---|---|
| `topic_id` | slug | the topic whose `20-sources/` to read |
| `sub_corpus` | slug | optional; if multiple corpora live in `20-sources/`, restrict to one |

## Outputs

Under `topics/<topic_id>/40-graphs/`:

- `sitemap.json` — `{ "nodes": [...], "edges": [...] }`.
- `sitemap.mmd` — Mermaid `flowchart LR` rendering for visual inspection.
- `sitemap-analysis.md` — derived metrics: hub pages (top-N in-degree), leaf pages, orphan pages, redirect chains, link-asymmetry.

## Procedure

1. **Collect nodes**. For every `_meta.md` in `20-sources/<sub_corpus>/`, emit a node:

    ```json
    { "id": "src_…", "title": "<title>", "url": "<url>", "type": "source", "depth": <int> }
    ```

2. **Collect edges**. For every `_meta.md`, for every URL in `links_out`:
   - Resolve to a node id by URL match (after canonicalisation: strip trailing slash, lowercase host, follow recorded redirects).
   - If the target URL is outside the captured corpus, emit a node with `type: external` and add an `external` flag.
   - Emit an edge `{ from: <src-id>, to: <target-id>, kind: "links-to" }`.
3. **Detect redirect chains** from `_meta.md`'s `canonical_url`. Emit `redirects-to` edges separately.
4. **Detect nav-of edges**. If a page lives in the site's navigation tree (heuristic: links from the site's index pages, plus a sustained pattern of mutual linking from siblings), tag the edges `nav-of` instead of `links-to`. This is heuristic; mark the analysis confidence accordingly.
5. **Emit `sitemap.json`** in the schema declared in [CONVENTIONS/diagrams.md](../CONVENTIONS/diagrams.md).
6. **Render `sitemap.mmd`**. Mermaid `flowchart LR` with one node per source, one edge per `links-to`. For corpora over ~150 nodes, generate a faceted set instead: `sitemap-by-section.mmd` per top-level URL prefix, since a 200+ node Mermaid graph is unreadable in every renderer.
7. **Compute `sitemap-analysis.md`**. Metrics:
   - **Hub pages** — top-N by in-degree. Often "concepts" or "overview" pages.
   - **Leaf pages** — out-degree zero (excluding external links). Often reference pages.
   - **Orphan pages** — in-degree zero. Suspicious; usually navigation-only entries or stale pages.
   - **Bidirectional clusters** — strongly connected components. Often "concept families" that mutually reference.
   - **Average path length** between any two nodes. Indicates how navigable the docs are.
   - **Link-asymmetry** — pages A and B where A links to B but B does not link back. Surfaces hierarchy.

## Verification

- Every node id in `sitemap.json` corresponds to an existing `_meta.md` (for `type: source` nodes) or is flagged `external`.
- Every edge's `from` and `to` resolve to a node in the graph.
- The Mermaid file parses (lint with `mmdc` or visually).
- Hub-page list passes the smell test — the obvious entry pages of the site appear near the top.

## Failure modes

| symptom | cause | fix |
|---|---|---|
| many `external` nodes | URL canonicalisation missed redirects | re-run with stricter canonicalisation |
| Mermaid file too large to render | corpus too big | switch to faceted output (`-by-section`) |
| orphans dominate | crawl did not start from the right root | inspect `_manifest.md`, re-crawl with corrected `base_url` |

## Use of the graph downstream

The sitemap graph is the navigation skeleton over which the knowledge graph hangs. Hub pages frequently coincide with concept-definition pages; leaf pages are often API reference. The downstream `extract-knowledge-graph` pipeline uses sitemap hub-rank as a hint for which pages to extract first.

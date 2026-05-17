---
id: src_memgraph-docs-vector
title: Memgraph vector search documentation
type: source
source_type: docs-page
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://memgraph.com/docs/querying/vector-search
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors: [Memgraph Ltd.]
grounds: [memgraph, vector-plus-graph]
topic: rag-ingestion-graph-stores
related: [src_memgraph-repo, src_memgraph-changelog, rag-ingestion-graph-stores]
tags: [memgraph, vector-search, procedure-call, query-planner-limitation]
---

# Meta

Memgraph's vector posture: procedure-call API (`vector_search.search()` / `vector_search.search_edges()`) returning nodes/edges with distance scores, then feed into a follow-on `MATCH`. The docs page explicitly flags the limitation that the **query planner does not currently use vector indices** — i.e. vector + graph is not yet planner-aware fusion; it is procedure-call-and-stitch.

---
id: src_falkordb-docs-vector
title: FalkorDB Vector Index documentation
type: source
source_type: docs-page
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://docs.falkordb.com/cypher/indexing/vector-index.html
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors: [FalkorDB org]
grounds: [falkordb, vector-plus-graph]
topic: rag-ingestion-graph-stores
related: [src_falkordb-repo, rag-ingestion-graph-stores]
tags: [falkordb, vector-index, procedure-call]
---

# Meta

FalkorDB exposes vector indexing via a procedure call `CALL db.idx.vector.queryNodes()`. The canon docs page does **not** show an example combining the procedure result with a `MATCH` graph traversal in a single Cypher statement — i.e. vector + graph is achieved by stitching procedure output to subsequent Cypher steps, not via a planner-aware inline operator.

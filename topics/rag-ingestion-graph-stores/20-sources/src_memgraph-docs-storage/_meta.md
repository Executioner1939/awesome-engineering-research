---
id: src_memgraph-docs-storage
title: Memgraph storage modes documentation
type: source
source_type: docs-page
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://memgraph.com/docs/fundamentals/storage-memory-usage
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors: [Memgraph Ltd.]
grounds: [memgraph, architecture]
topic: rag-ingestion-graph-stores
related: [src_memgraph-repo, rag-ingestion-graph-stores]
tags: [memgraph, storage, rocksdb, acid, analytical]
---

# Meta

Three storage modes settle the "in-memory only?" question (no — there is an on-disk mode), and the analytical mode trades ACID for ingest speed. Disconfirms prior-training memory that may describe Memgraph as in-memory-only.

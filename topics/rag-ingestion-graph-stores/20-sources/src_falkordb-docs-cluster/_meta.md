---
id: src_falkordb-docs-cluster
title: FalkorDB Cluster documentation
type: source
source_type: docs-page
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://docs.falkordb.com/operations/cluster.html
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors: [FalkorDB org]
grounds: [falkordb, architecture, deployment]
topic: rag-ingestion-graph-stores
related: [src_falkordb-repo, src_falkordb-releases, rag-ingestion-graph-stores]
tags: [falkordb, cluster, redis-cluster, sharding]
---

# Meta

Grounds two non-obvious architectural facts: (1) FalkorDB clustering is Redis Cluster (16,384 hash slots), not a graph-aware distributed engine; (2) each graph is one Redis key on one shard, so single graphs do not shard — only multi-graph workloads benefit from clustering.

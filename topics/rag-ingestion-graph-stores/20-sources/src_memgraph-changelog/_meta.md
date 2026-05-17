---
id: src_memgraph-changelog
title: Memgraph release notes (v3.9.0 → v3.10.1)
type: source
source_type: changelog
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://memgraph.com/docs/release-notes
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors: [Memgraph Ltd.]
grounds: [memgraph, recent-direction]
topic: rag-ingestion-graph-stores
related: [src_memgraph-releases, src_memgraph-docs-vector, rag-ingestion-graph-stores]
tags: [memgraph, release-notes, vector-index, ha-coordinator, raft, tenant-profiles]
---

# Meta

Two themes dominate the 2026 release work: (1) vector-index maturation — concurrent writers in 3.9.0, single-store edge-vector pattern in 3.10.0; (2) HA-coordinator hardening — Raft-first majority-ack semantics, periodic-snapshot suppression on coordinators, fine-grained `DENY` permissions, per-database memory tracking via Tenant Profiles, auto-created built-in roles (admin/readonly/readwrite).

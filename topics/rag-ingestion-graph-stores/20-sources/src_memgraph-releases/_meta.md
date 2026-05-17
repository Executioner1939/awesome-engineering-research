---
id: src_memgraph-releases
title: Memgraph current release (v3.10.1) — GitHub Releases + container --version
type: source
source_type: cli-capture
status: stable
confidence: verified
created: 2026-05-16
updated: 2026-05-16
url: https://api.github.com/repos/memgraph/memgraph/releases?per_page=3
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-bash
capture_kind: derived-summary
mime: application/json
crawl_depth: 0
authors: [Memgraph Ltd.]
grounds: [memgraph, version]
topic: rag-ingestion-graph-stores
related: [src_memgraph-repo, src_memgraph-changelog, rag-ingestion-graph-stores]
tags: [memgraph, version, cli-capture, raft-coordinator]
---

# Meta

Combined version-verification bundle for Memgraph as of 2026-05-16. Establishes: (1) `v3.10.1` published 2026-05-15 is the current release (under a day old at capture time), (2) cross-verified by container `--version` output, (3) the runtime container also emits a deprecation warning for the `instance_down_timeout_sec` flag, replaced by `SET COORDINATOR SETTING …` — confirming the Raft-coordinator HA model is the current path.

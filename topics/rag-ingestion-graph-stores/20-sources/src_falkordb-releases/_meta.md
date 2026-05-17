---
id: src_falkordb-releases
title: FalkorDB current release (v4.18.7) — GitHub Releases + container module list
type: source
source_type: cli-capture
status: stable
confidence: verified
created: 2026-05-16
updated: 2026-05-16
url: https://api.github.com/repos/FalkorDB/FalkorDB/releases?per_page=3
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-bash
capture_kind: derived-summary
mime: application/json
crawl_depth: 0
authors: [FalkorDB org]
grounds: [falkordb, version, release-direction]
topic: rag-ingestion-graph-stores
related: [src_falkordb-repo, src_falkordb-blog, rag-ingestion-graph-stores]
tags: [falkordb, version, cli-capture]
---

# Meta

Combined version-verification bundle for FalkorDB as of 2026-05-16. Two independent verifications:

1. GitHub Releases API enumeration of the three most recent tags — confirms `v4.18.7` published 2026-05-14T12:04:33Z as the current release, with a tight three-release cadence in the four days preceding.
2. Container module-list inspection via `docker run --rm falkordb/falkordb:latest` + `redis-cli MODULE LIST` — confirms `graph` module `ver 41807` (matching v4.18.7) loaded into Redis 8.6.3, with companion `vectorset` module `ver 1`.

The two captures cross-verify: the GitHub tag matches the container's module wire-version.

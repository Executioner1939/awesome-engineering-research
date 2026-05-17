---
id: store-three-way-falkor-surreal-memgraph
title: "Three-way comparison: FalkorDB, SurrealDB, Memgraph (May 2026)"
type: synthesis
synthesis_kind: comparison
status: reviewed
confidence: high
created: 2026-05-16
updated: 2026-05-16
covers: [rag-ingestion-graph-stores]
related:
  - src_falkordb-releases
  - src_falkordb-repo
  - src_falkordb-license
  - src_falkordb-docs-cluster
  - src_falkordb-docs-vector
  - src_falkordb-blog
  - src_surrealdb-releases
  - src_surrealdb-docs-overview
  - src_surrealdb-docs-vector
  - src_surrealdb-license
  - src_memgraph-releases
  - src_memgraph-repo
  - src_memgraph-license
  - src_memgraph-docs-storage
  - src_memgraph-docs-vector
  - src_memgraph-changelog
sources:
  - src_falkordb-releases
  - src_falkordb-repo
  - src_falkordb-license
  - src_falkordb-docs-cluster
  - src_falkordb-docs-vector
  - src_falkordb-blog
  - src_surrealdb-releases
  - src_surrealdb-docs-overview
  - src_surrealdb-docs-vector
  - src_surrealdb-license
  - src_memgraph-releases
  - src_memgraph-repo
  - src_memgraph-license
  - src_memgraph-docs-storage
  - src_memgraph-docs-vector
  - src_memgraph-changelog
tags: [comparison, falkordb, surrealdb, memgraph, vector-plus-graph, license]
---

# Three-way comparison: FalkorDB, SurrealDB, Memgraph (May 2026)

Sixteen canonical sources captured 2026-05-16 — GitHub Releases API, container CLI captures, repo READMEs, license files, and docs pages. Every claim below cites at least one captured source by `[[src_*]]` id.

## The headline

All three position themselves as the graph engine of choice for GraphRAG / agent-memory / LLM-context workloads ([[src_falkordb-repo]], [[src_memgraph-repo]], [[src_surrealdb-docs-overview]]). The workload narrative is shared. The architectures behind the pitch are not.

On the **vector + graph in one query** axis — which is the load-bearing capability for GraphRAG ingestion-and-retrieval — only SurrealDB demonstrates language-level fusion in canon. FalkorDB and Memgraph both expose vector as a procedure call that returns nodes, which the caller then stitches into a follow-on graph traversal.

On **deployment shape**, SurrealDB has the widest surface (embedded, WASM, edge, server, cluster). FalkorDB is locked to "Redis module on a Redis 8.x host". Memgraph is a standalone C/C++ engine with three storage modes (in-memory transactional default, in-memory analytical, on-disk transactional via RocksDB).

On **license**, all three are non-OSI. FalkorDB is the strictest (SSPL — MongoDB-derived). SurrealDB and Memgraph are both BSL 1.1 with Apache-2.0 conversion around 2030. Memgraph adds a separate MEL Enterprise tier.

## Side-by-side

| capability | FalkorDB | SurrealDB | Memgraph |
|---|---|---|---|
| **latest release (2026-05-16)** | v4.18.7 ([[src_falkordb-releases]]) | v3.0.5 ([[src_surrealdb-releases]]) | v3.10.1 ([[src_memgraph-releases]]) |
| **release cadence (last ~6mo)** | high — 3 releases in 4 days ([[src_falkordb-releases]]) | moderate — 3.x head + parallel 2.6.x LTS ([[src_surrealdb-releases]]) | moderate — 3.10.x in May, 3.9.x in March ([[src_memgraph-changelog]]) |
| **license** | SSPL v1 ([[src_falkordb-license]]) | BSL 1.1, → Apache 2.0 on 2030-01-01 ([[src_surrealdb-license]]) | BSL 1.1 (Community) + MEL (Enterprise) ([[src_memgraph-license]]) |
| **OSI open source** | no | no | no |
| **engine language** | C (built on GraphBLAS) ([[src_falkordb-repo]]) | Rust ([[src_surrealdb-docs-overview]]) | C/C++ ([[src_memgraph-repo]]) |
| **architecture** | Redis module loaded into Redis 8.6.3 ([[src_falkordb-releases]]) | single Rust binary, multi-model engine ([[src_surrealdb-docs-overview]]) | standalone in-memory-first engine, three storage modes ([[src_memgraph-docs-storage]]) |
| **query language** | openCypher + proprietary extensions ([[src_falkordb-repo]]) | SurrealQL (SQL + graph arrows + vector funcs) ([[src_surrealdb-docs-overview]]) | Cypher (Neo4j-compatible posture) ([[src_memgraph-repo]]) |
| **vector index** | yes — `vectorset` module loaded next to `graph` ([[src_falkordb-releases]]) | yes — first-class in SurrealQL ([[src_surrealdb-docs-vector]]) | yes — node and edge vector indexes ([[src_memgraph-docs-vector]]) |
| **vector + graph in single query** | no — procedure call `CALL db.idx.vector.queryNodes()` then stitch ([[src_falkordb-docs-vector]]) | **yes** — inline `WHERE vector::similarity::cosine(...)` inside `->edge->node` traversal ([[src_surrealdb-docs-vector]]) | no — procedure call `vector_search.search()` then stitch; docs explicitly note planner does not utilise vector indices ([[src_memgraph-docs-vector]]) |
| **distributed model** | Redis Cluster (16,384 hash slots, one graph = one key on one shard) ([[src_falkordb-docs-cluster]]) | distributed cluster (backing store not detailed in fetched canon) ([[src_surrealdb-docs-overview]]) | Raft-based HA coordinator cluster, hardened in 3.10.x ([[src_memgraph-changelog]]) |
| **single-graph sharding** | no — one graph lives on one shard ([[src_falkordb-docs-cluster]]) | not specified in fetched canon | not specified in fetched canon |
| **embeddable / in-process** | no | **yes** — Rust/JS/Python/Java SDKs include embedded mode; browser WASM ([[src_surrealdb-docs-overview]]) | no |
| **default persistence** | Redis (RDB / AOF inherited) | Surreal storage layer | in-memory + snapshots; on-disk via `ON_DISK_TRANSACTIONAL` (RocksDB) ([[src_memgraph-docs-storage]]) |
| **ACID** | per Redis semantics | yes (transactional) | yes in `IN_MEMORY_TRANSACTIONAL` and `ON_DISK_TRANSACTIONAL`; **not** in `IN_MEMORY_ANALYTICAL` ([[src_memgraph-docs-storage]]) |
| **explicit GraphRAG positioning on front page** | yes ([[src_falkordb-repo]]) | yes ([[src_surrealdb-docs-overview]]) | yes ([[src_memgraph-repo]]) |

## Where each one wins

### SurrealDB wins on

- **Unified query.** Only one of the three with language-level vector + graph fusion in canonical docs. The capability that closes the gap between "vector store + graph store stitched in code" and "one query, every model" ([[src_surrealdb-docs-vector]]).
- **Deployment surface.** Embedded library, browser WASM, edge, server, distributed cluster — only Surreal covers all five ([[src_surrealdb-docs-overview]]).
- **Single-store coherence.** Document + graph + relational + time-series + geospatial + KV in one engine, not stitched ([[src_surrealdb-docs-overview]]).
- **LTS posture.** Parallel 2.6.x line maintained alongside 3.x head; mature lifecycle thinking ([[src_surrealdb-releases]]).

### Memgraph wins on

- **Operational maturity.** Raft-based HA coordinator cluster with majority-ack semantics, fine-grained `DENY` permissions, per-database memory tracking (Tenant Profiles), built-in admin/readonly/readwrite roles auto-created ([[src_memgraph-changelog]]). The 3.10.x release notes read like an enterprise-features-first roadmap.
- **Storage flexibility.** Three storage modes — strict ACID transactional in-memory, fast analytical in-memory (no ACID), or transactional with RocksDB on disk — selectable per workload ([[src_memgraph-docs-storage]]).
- **Neo4j-compatible Cypher.** Lowest porting cost for existing Cypher-shaped codebases ([[src_memgraph-repo]]).

### FalkorDB wins on

- **GraphBLAS algebra performance ceiling.** Sparse adjacency matrix representation, linear-algebra primitives. Different ceiling than B-tree / pointer-chasing graph engines ([[src_falkordb-repo]]).
- **Redis-native deployment.** If the rest of the stack is already Redis 8.x, FalkorDB drops in as a module, not a new service to operate. Redis Cluster tooling works out of the box ([[src_falkordb-docs-cluster]]).
- **GraphRAG focus.** Tightest narrative — the project is explicitly chasing the "best knowledge graph for LLM" position, with a 2026 release cadence built around it (Snowflake integration, GraphRAG SDK 1.0, dedicated browser UI work) ([[src_falkordb-blog]]).

## Where each one loses

### FalkorDB

- **Lock-in to Redis as host.** Inherits Redis Cluster's "one key on one shard" model — a single large graph cannot shard across nodes ([[src_falkordb-docs-cluster]]). For multi-tenant / multi-graph workloads this is fine; for one large graph it caps horizontal scale at vertical capacity per shard.
- **SSPL is the strictest license** of the three — any third-party managed-service offering must release the service source code ([[src_falkordb-license]]). Most stringent if a future plan involves selling FalkorDB-as-a-Service.
- **Vector + graph is procedure-call-and-stitch.** No canonical example of inline fusion ([[src_falkordb-docs-vector]]).
- **No embedded form.** Always a service.

### SurrealDB

- **Multi-model breadth at the cost of graph depth.** SurrealDB does graph well, but it is not graph-first; if the workload is pure graph analytics at scale, dedicated graph engines (Memgraph, Neo4j, FalkorDB) likely have more graph-aware planner tooling.
- **Distributed-cluster backing store under-documented in fetched canon.** Prior-training memory suggests TiKV; the fetched docs page did not re-confirm. Flag for verification before committing to a cluster deployment.
- **BSL DBaaS restriction.** Cannot offer SurrealDB-as-a-Service to third parties without commercial license ([[src_surrealdb-license]]).

### Memgraph

- **Query planner does not utilise vector indices** (as the docs explicitly state) ([[src_memgraph-docs-vector]]). Vector + graph fusion is procedure-call-and-stitch. Two of the last two releases have invested heavily in vector-index machinery (concurrent writers, edge vectors), so this is being addressed — but as of v3.10.1 the planner-level fusion is not there.
- **No embedded form.** Always a service.
- **BSL restrictions plus a separate MEL Enterprise tier** ([[src_memgraph-license]]) — clarify which features are gated to MEL before assuming Community is sufficient.
- **Date string in BSL.txt is malformed** (`2030-15-05`) — not load-bearing but worth flagging as a license-document hygiene issue.

## Implications for the docs-knowledge-graph-pipeline output

The output of [[docs-knowledge-graph-pipeline]] is structurally a knowledge graph plus a vector-indexable text corpus. Which of these three is the natural fit depends on the dominant query shape:

- **If queries are "find similar concepts, then traverse to dependent APIs"** — SurrealDB's inline fusion wins. One statement does the whole thing. [[src_surrealdb-docs-vector]] is the existence proof.
- **If queries are graph-traversal-heavy with vector as a coarse filter** — FalkorDB or Memgraph both work; FalkorDB's GraphBLAS ceiling is the differentiator on dense traversal workloads, Memgraph's storage flexibility wins for mixed analytical / transactional workloads.
- **If the deployment is single-binary or in-process** (e.g. agent shipping with embedded corpus) — only SurrealDB qualifies.
- **If the deployment is already Redis** — FalkorDB is the no-new-service answer.

## What this comparison deliberately does not settle

- **Performance.** None of the captured sources is a benchmark. Real workload characteristics (corpus size, query shape, hardware, concurrency) dominate any synthetic number.
- **Cost.** Pricing pages for managed offerings were out of scope for this pass.
- **Ecosystem.** LangChain / LlamaIndex / Haystack adapter availability for each, GraphRAG / LightRAG / HippoRAG canonical backends for each — these are downstream questions, addressed in Phase 3.
- **Comparison to Neo4j or Qdrant.** Explicitly out of scope; covered in the broader Phase 2 sweep.

## Open verification items

Three items from this pass that warrant phase-2 follow-up:

1. SurrealDB v3.x distributed cluster backing store — TiKV or otherwise. Canonical docs page that confirms current state.
2. FalkorDB `vectorset` module provenance — is it Redis 8's `Redis Vector Sets`, or a FalkorDB fork.
3. Memgraph openCypher TCK conformance level — "compatible with Neo4j" is the README framing; canon for the specific subset was not fetched.

These are not blocking conclusions in this synthesis; they are noted for the next time this topic is touched.

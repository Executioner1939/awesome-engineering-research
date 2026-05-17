---
id: dec_surrealdb-as-runtime-store
title: "Decision: SurrealDB as the runtime store for graph + vector retrieval"
type: decision
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
decision_status: accepted
context: |
  The output of the docs-knowledge-graph-pipeline is a structurally explicit knowledge graph
  plus a vector-indexable text corpus. A runtime store is required to serve those artefacts
  to the eventual agent-facing retrieval layer (Phase 3). The candidate space is large; the
  three-way capture (FalkorDB, SurrealDB, Memgraph) on 2026-05-16 was sufficient to make
  the call without sweeping the remaining 8 stores in Phase 2.
options_considered:
  - tool_falkordb
  - tool_surrealdb
  - tool_memgraph
chosen: tool_surrealdb
consequences:
  - "Vector + graph composes in one SurrealQL statement — `WHERE vector::similarity::cosine(...)` inline inside graph traversal. No procedure-call-and-stitch."
  - "Widest deployment surface: embedded in-app, browser-WASM, edge, server, distributed cluster. Optionality to run the corpus embedded in an agent without operating a service."
  - "Multi-model engine (document + graph + relational + time-series + geospatial + KV). The KG, the markdown corpus, and any future log/timeseries observations sit in one store."
  - "BSL 1.1, converts to Apache 2.0 on 2030-01-01. Cannot offer SurrealDB-as-a-Service to third parties without commercial license — accepted, not a constraint on the intended use."
  - "Multi-model breadth comes at the cost of graph depth: pure graph-analytics workloads may run worse than on a dedicated graph engine. Mitigation: if the workload profile shifts toward heavy graph analytics, revisit with a benchmark against Memgraph or Neo4j."
  - "Distributed cluster backing store is under-documented in fetched canon as of 2026-05-16. Mitigation: before any cluster deployment, capture the canonical doc that names the backing store (TiKV or otherwise)."
  - "Phase 2 sweep for the remaining 8 stores (Qdrant, Weaviate, Milvus, LanceDB, Neo4j, Kuzu, ArangoDB, pgvector+AGE, sqlite-vec) is no longer required for store selection. May still be useful as background, but is not blocking Phase 3."
related:
  - store-three-way-falkor-surreal-memgraph
  - src_surrealdb-docs-vector
  - src_surrealdb-docs-overview
  - src_surrealdb-license
  - src_surrealdb-releases
sources:
  - src_surrealdb-docs-vector
  - src_surrealdb-docs-overview
  - src_surrealdb-license
  - src_surrealdb-releases
  - src_falkordb-docs-vector
  - src_memgraph-docs-vector
tags: [decision, surrealdb, runtime-store, accepted]
---

# Decision: SurrealDB as the runtime store for graph + vector retrieval

## Status

`accepted` — 2026-05-16.

## Context

The research pipeline at [[docs-knowledge-graph-pipeline]] produces structured artefacts (knowledge graph in JSON + Mermaid, markdown corpus, extract files). To serve those to the agent-facing retrieval layer (Phase 3), a runtime store must hold both the vector representations of the corpus and the knowledge graph in a way that can be queried together.

Three databases were captured in the three-way comparison ([[store-three-way-falkor-surreal-memgraph]]): FalkorDB, SurrealDB, Memgraph. The full Phase 2 sweep (Qdrant, Weaviate, Milvus, LanceDB, Neo4j, Kuzu, ArangoDB, pgvector+AGE, sqlite-vec) was not run. The three-way was sufficient because the decisive axis surfaced clearly: language-level vector + graph fusion.

## Options considered

| option | language-level vector+graph fusion | deployment surface | license |
|---|---|---|---|
| `tool_falkordb` | no — procedure call then stitch ([[src_falkordb-docs-vector]]) | service only, Redis module | SSPL v1 |
| `tool_surrealdb` | **yes** — inline `WHERE` predicate in graph traversal ([[src_surrealdb-docs-vector]]) | embedded, WASM, edge, server, cluster ([[src_surrealdb-docs-overview]]) | BSL 1.1 → Apache 2.0 (2030-01-01) ([[src_surrealdb-license]]) |
| `tool_memgraph` | no — procedure call then stitch; docs state "the query planner currently does not utilise vector indices" ([[src_memgraph-docs-vector]]) | service only | BSL 1.1 + MEL dual |

## Decision

SurrealDB.

## Why

Language-level fusion is the load-bearing capability for the eventual retrieval layer. The query pattern that GraphRAG / agentic-RAG retrieval needs ("find similar concepts then traverse to dependent APIs / sources") composes into a single SurrealQL statement on SurrealDB and into procedure-call-and-stitch on the other two. The difference is not cosmetic — it changes the retrieval policy from "agent orchestrates two stores" to "agent issues one query".

Deployment-surface optionality is the second-order win. The ability to ship the corpus embedded in an agent process (Rust SDK with embedded mode) or in-browser (WASM) is available on no other store in the captured comparison set. Even if the production deployment is the standalone server, retaining the embedded option for development, testing, and edge use cases is durable optionality.

Apache-2.0 conversion on 2030-01-01 means the license risk is bounded in time.

## What this decision is not

- Not a benchmark claim. SurrealDB has not been measured against the workload profile in this repo; benchmarks are deferred to when the corpus is large enough to matter.
- Not a foreclosure of Memgraph / Neo4j / FalkorDB. If a future workload shifts toward dense graph analytics and SurrealDB's planner does not keep up, the decision is revisitable; the [[store-three-way-falkor-surreal-memgraph]] synthesis is the starting point.
- Not a Phase 3 ingestion design. The store choice is upstream of ingestion shape; Phase 3 still needs to settle chunking, embedding, schema layout, and graph-update semantics on SurrealDB specifically.

## Follow-up items

1. **Verify the distributed-cluster backing store.** SurrealDB's overview ([[src_surrealdb-docs-overview]]) says "distributed cluster" without naming the backing store in the fetched canon. Capture the current docs page that establishes this before any cluster deployment.
2. **Capture SurrealDB 3.0.5 release notes** at page granularity. The releases capture ([[src_surrealdb-releases]]) was API-only.
3. **Open a Phase 3 sub-topic for SurrealDB ingestion shape.** Schema design (tables vs records for KG nodes, edges as graph arrows vs typed records), embedding column type, vector index parameters, incremental update semantics on re-ingest.

---
id: rag-ingestion-graph-stores-questions
title: Driving Questions and Verification Plan
type: synthesis
synthesis_kind: summary
status: seed
confidence: low
created: 2026-05-15
updated: 2026-05-15
covers: [rag-ingestion-graph-stores]
---

# Driving Questions and Verification Plan

| id | question | status |
|---|---|---|
| q-rag-taxonomy | What do the terms vanilla-RAG, graph-RAG, knowledge-RAG, agentic-RAG mean in May 2026 — which architectures, who coined them, and which usages have settled vs are still drifting? | open |
| q-graph-vs-vector | When does a graph store add value over vector-only retrieval — what kinds of question does graph traversal answer that nearest-neighbour does not? | open |
| q-ingestion-pipeline | What is the contemporary ingestion shape — chunking strategies, hierarchical chunking, entity-level extraction during ingestion, graph-update semantics on re-ingest? | open |
| q-agentic-retrieval | What does "agentic RAG" mean concretely — what's the policy loop, what tools does the retrieval agent get, and how is it evaluated? | open |
| q-live-vs-frozen | When the graph says "this concept exists but we have no extract for it", how does the retrieval layer decide to fetch live (firecrawl, package-registry, github) versus respond with "I don't know"? | open |
| q-conventions-2026 | What conventions has the field converged on (and where has it not) as of May 2026 — chunk sizes, embedding choice, hybrid search ranking, schema design for the KG? | open |

## Verification plan

These questions cannot be answered without verifying current state. Per the verification protocol, every claim that asserts a current name, version, library, or technique must cite either a CLI lookup (package-manager) or a fetched page (firecrawl-search / firecrawl-scrape).

### Phase 1 — Establish the terminology landscape

Sources to capture in `20-sources/`:

- Microsoft's GraphRAG paper, latest version on arXiv, plus its current GitHub README.
- The LightRAG paper and repo README.
- The HippoRAG paper and repo README.
- One canonical "agentic RAG" reference — likely a maintainer's blog (LangChain, LlamaIndex) plus the equivalent on the other framework. Cross-reference at least two authors.
- One survey paper on RAG (2024 or later) for the taxonomy baseline.

### Phase 2 — Establish the database landscape

Sources to capture:

- Latest release notes / current version of: Qdrant, Weaviate, Milvus, LanceDB (vector); Neo4j, Memgraph, Kuzu, FalkorDB (graph); SurrealDB, ArangoDB (hybrid); pgvector + Apache AGE (postgres extensions); sqlite-vec (sqlite extension).
- For each: feature support for hybrid search, graph + vector in one query, embedding-aware indexes, schema migrations, deployment shape.
- Verify currency via package-manager CLI where applicable (`npm view`, `cargo search`, `brew info`).

### Phase 3 — Establish the ingestion conventions

Sources to capture:

- LlamaIndex and LangChain ingestion-pattern docs.
- Anthropic's published guidance on retrieval (if any current page exists in May 2026).
- One or two production case studies (engineering blogs from companies running RAG in production).

### Phase 4 — Synthesise

Three syntheses in `50-syntheses/`:

- `rag-taxonomy.md` — settled definitions for vanilla / graph / knowledge / agentic RAG, with citations.
- `store-matrix.md` — comparison table of stores against capability requirements derived from this topic's questions.
- `ingestion-walkthrough.md` — concrete ingestion design that takes the [[docs-knowledge-graph-pipeline]] file outputs and produces queryable state in the chosen stores.

## Why not just decide now

The terminology has moved unstably enough that asserting today's meaning from prior-training memory is unsafe. The verification protocol is in force; speculation about the May 2026 landscape is a regression, not an optimisation. Every claim worth raising above `confidence: low` will have a captured source.

---
id: rag-ingestion-graph-stores
title: RAG, Graph Stores, and Ingestion (May 2026)
type: topic
status: draft
confidence: medium
domain: knowledge-systems
created: 2026-05-15
updated: 2026-05-16
questions: [q-rag-taxonomy, q-graph-vs-vector, q-ingestion-pipeline, q-agentic-retrieval, q-live-vs-frozen, q-conventions-2026]
related: [docs-knowledge-graph-pipeline, extract-knowledge-graph]
tags: [rag, graph-rag, agentic-rag, vector-db, graph-db, ingestion]
---

# RAG, Graph Stores, and Ingestion (May 2026)

The destination layer for [[docs-knowledge-graph-pipeline]]. Once the corpus, sitemap graph, and knowledge graph exist as files in `Research/`, an agent (or a developer) needs to query them. This topic surveys the May 2026 landscape of:

- **Ingestion patterns** — how the file-based corpus loads into a runtime store, what gets embedded, what gets graph-indexed.
- **Database options** — vector DBs, graph DBs, hybrid stores, full-text adjuncts.
- **RAG paradigms** — vanilla RAG, graph-RAG, knowledge-RAG, agentic-RAG. The naming has moved fast and the meanings are not stable across writers.
- **Conventions** — what the field has converged on (and where it has not) for chunking, embedding, schema-aware retrieval, and live-vs-frozen sources.

## Status

Phase 1 (terminology landscape) is complete: ten canonical sources captured under `20-sources/`, with the synthesis at `50-syntheses/rag-taxonomy.md` defining vanilla / advanced / modular / graph / agentic RAG against cited canon and flagging "knowledge-RAG" as not converged.

Phase 2 (database currency — vector / graph / hybrid stores as of May 2026) and Phase 3 (ingestion conventions) are not yet started. See `10-questions.md` for the verification plan.

## Out-of-scope for this topic

- Building the actual retrieval service. This topic is research, not implementation.
- Choosing a single store. The decision is per-deployment; this topic provides the option matrix and the tradeoffs.
- Embedding-model bake-offs. Embedding quality is its own topic — to be opened if needed.

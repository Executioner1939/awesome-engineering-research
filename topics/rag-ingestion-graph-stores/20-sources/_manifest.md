---
id: rag-ingestion-graph-stores-sources-manifest
title: Sources Manifest — RAG, Graph Stores, and Ingestion
type: index
status: stable
created: 2026-05-16
updated: 2026-05-16
sort: id
---

# Sources Manifest — RAG, Graph Stores, and Ingestion

Phase 1 (terminology landscape) and partial Phase 2 (FalkorDB / SurrealDB / Memgraph) captures. Remaining Phase 2 (vector stores, postgres extensions, sqlite extensions, Neo4j, Kuzu, ArangoDB) and Phase 3 (ingestion conventions) extend this manifest.

| id | title | source_type | status | url | retrieved_at | capture_kind | grounds |
|---|---|---|---|---|---|---|---|
| src_agentic-rag-survey-2025 | Agentic RAG Survey | paper | stable | https://arxiv.org/abs/2501.09136 | 2026-05-16 | excerpt | agentic-rag, vanilla-rag, graph-rag |
| src_anthropic-search-results-docs | Anthropic Search Results docs | docs-page | stable | https://platform.claude.com/docs/en/docs/build-with-claude/search-results | 2026-05-16 | excerpt | vanilla-rag |
| src_falkordb-blog | FalkorDB blog index — recent direction | docs-page | stable | https://falkordb.com/blog/ | 2026-05-16 | excerpt | falkordb, recent-direction |
| src_falkordb-docs-cluster | FalkorDB Cluster documentation | docs-page | stable | https://docs.falkordb.com/operations/cluster.html | 2026-05-16 | excerpt | falkordb, architecture, deployment |
| src_falkordb-docs-vector | FalkorDB Vector Index documentation | docs-page | stable | https://docs.falkordb.com/cypher/indexing/vector-index.html | 2026-05-16 | excerpt | falkordb, vector-plus-graph |
| src_falkordb-license | FalkorDB LICENSE.txt (SSPL v1) | docs-page | stable | https://github.com/FalkorDB/FalkorDB/blob/master/LICENSE.txt | 2026-05-16 | excerpt | falkordb, license |
| src_falkordb-releases | FalkorDB current release (v4.18.7) | cli-capture | stable | https://api.github.com/repos/FalkorDB/FalkorDB/releases?per_page=3 | 2026-05-16 | derived-summary | falkordb, version, release-direction |
| src_falkordb-repo | FalkorDB README | github-readme | stable | https://github.com/FalkorDB/FalkorDB | 2026-05-16 | excerpt | falkordb, architecture, query-language, positioning |
| src_graphrag-paper-2024 | From Local to Global: A Graph RAG Approach | paper | stable | https://arxiv.org/abs/2404.16130 | 2026-05-16 | excerpt | graph-rag, vanilla-rag |
| src_graphrag-repo | microsoft/graphrag README | github-readme | stable | https://github.com/microsoft/graphrag | 2026-05-16 | excerpt | graph-rag |
| src_hipporag-repo | OSU-NLP-Group/HippoRAG README | github-readme | stable | https://github.com/OSU-NLP-Group/HippoRAG | 2026-05-16 | excerpt | knowledge-rag, graph-rag |
| src_hipporag2-paper | HippoRAG 2 paper | paper | stable | https://arxiv.org/abs/2502.14802 | 2026-05-16 | excerpt | knowledge-rag, graph-rag |
| src_langchain-agentic-rag-docs | LangChain agentic-RAG docs | docs-page | stable | https://docs.langchain.com/oss/python/langgraph/agentic-rag | 2026-05-16 | excerpt | agentic-rag |
| src_lightrag-paper | LightRAG paper | paper | stable | https://arxiv.org/abs/2410.05779 | 2026-05-16 | excerpt | graph-rag, knowledge-rag |
| src_lightrag-repo | HKUDS/LightRAG README | github-readme | stable | https://github.com/HKUDS/LightRAG | 2026-05-16 | excerpt | graph-rag, vanilla-rag |
| src_llamaindex-agentic-retrieval-blog | LlamaIndex Agentic Retrieval Guide | blog-author-canonical | stable | https://www.llamaindex.ai/blog/rag-is-dead-long-live-agentic-retrieval | 2026-05-16 | excerpt | agentic-rag, vanilla-rag |
| src_memgraph-changelog | Memgraph release notes (v3.9.0 → v3.10.1) | changelog | stable | https://memgraph.com/docs/release-notes | 2026-05-16 | excerpt | memgraph, recent-direction |
| src_memgraph-docs-storage | Memgraph storage modes documentation | docs-page | stable | https://memgraph.com/docs/fundamentals/storage-memory-usage | 2026-05-16 | excerpt | memgraph, architecture |
| src_memgraph-docs-vector | Memgraph vector search documentation | docs-page | stable | https://memgraph.com/docs/querying/vector-search | 2026-05-16 | excerpt | memgraph, vector-plus-graph |
| src_memgraph-license | Memgraph BSL 1.1 (Additional Use Grant) | docs-page | stable | https://github.com/memgraph/memgraph/blob/master/licenses/BSL.txt | 2026-05-16 | excerpt | memgraph, license |
| src_memgraph-releases | Memgraph current release (v3.10.1) | cli-capture | stable | https://api.github.com/repos/memgraph/memgraph/releases?per_page=3 | 2026-05-16 | derived-summary | memgraph, version |
| src_memgraph-repo | Memgraph README | github-readme | stable | https://github.com/memgraph/memgraph | 2026-05-16 | excerpt | memgraph, architecture, positioning, license-summary |
| src_surrealdb-docs-overview | SurrealDB Overview documentation | docs-page | stable | https://surrealdb.com/docs/surrealdb | 2026-05-16 | excerpt | surrealdb, architecture, query-language, deployment |
| src_surrealdb-docs-vector | SurrealQL Vector data model | docs-page | stable | https://surrealdb.com/docs/surrealql/datamodel/vector | 2026-05-16 | excerpt | surrealdb, vector-plus-graph |
| src_surrealdb-license | SurrealDB LICENSE (BSL 1.1) | docs-page | stable | https://github.com/surrealdb/surrealdb/blob/main/LICENSE | 2026-05-16 | excerpt | surrealdb, license |
| src_surrealdb-releases | SurrealDB current release (v3.0.5) | cli-capture | stable | https://api.github.com/repos/surrealdb/surrealdb/releases?per_page=5 | 2026-05-16 | derived-summary | surrealdb, version, lts-branches |

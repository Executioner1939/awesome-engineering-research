---
id: src_hipporag2-paper
title: "From RAG to Memory: Non-Parametric Continual Learning for Large Language Models (HippoRAG 2)"
type: source
source_type: paper
status: stable
confidence: high
created: 2026-05-16
updated: 2026-05-16
url: https://arxiv.org/abs/2502.14802
retrieved_at: 2026-05-16
retriever: oracle-canon-reader-via-firecrawl
capture_kind: excerpt
mime: text/markdown
crawl_depth: 0
authors:
  - Bernal Jiménez Gutiérrez
  - Yiheng Shu
  - Weijian Qi
  - Sizhe Zhou
  - Yu Su
date_published: 2025-02-20
grounds: [knowledge-rag, graph-rag]
topic: rag-ingestion-graph-stores
related: [src_hipporag-repo, rag-ingestion-graph-stores]
tags: [paper, osu-nlp, knowledge-rag, icml-2025]
---

# Meta

HippoRAG 2 paper. ICML 2025; v2 dated 2025-06-19. Authors from Ohio State University with UIUC affiliations. Frames RAG-with-knowledge-graphs as a "long-term memory" mechanism for LLMs; algorithmic backbone is Personalized PageRank over an LLM-extracted entity graph. Closest canonical reference to a "knowledge-RAG" concept that fetched in this pass, but the paper does not use that exact term — it calls itself "RAG + Knowledge Graphs + Personalized PageRank" via the project README.

---
id: docs-knowledge-graph-pipeline
title: Docs to Knowledge Graph Pipeline
type: topic
status: draft
confidence: medium
domain: knowledge-systems
created: 2026-05-15
updated: 2026-05-15
questions: [q-sitemap-purpose, q-extract-strategy, q-poor-docs, q-graph-rendering, q-corpora]
related: [scrape-firecrawl, sitemap-graph, extract-knowledge-graph, rag-ingestion-graph-stores]
tags: [pipeline, scraping, knowledge-graph, sitemap, docs]
---

# Docs to Knowledge Graph Pipeline

The methodology for turning a docs site (or sparse cargo-doc, or repo README) into a navigable knowledge graph. Composed of three pipelines:

1. [[scrape-firecrawl]] — capture every page as markdown plus link metadata.
2. [[sitemap-graph]] — build the URL-level link graph from the captured corpus.
3. [[extract-knowledge-graph]] — extract structured nodes (concepts, APIs, tools, entities) and edges (relations).

This topic both **defines** that methodology and **applies** it to two case studies that the user has named as ones whose surface area is hard to internalise: Firecrawl itself (dogfood) and Moon.

## Structure

```
topics/docs-knowledge-graph-pipeline/
├── README.md                # this file
├── 00-overview.md           # scope, non-goals, success criteria
├── 10-questions.md          # driving questions, each with q_id
├── 20-sources/              # populated by scrape-firecrawl
│   ├── _manifest.md
│   ├── firecrawl-docs/      # sub-corpus from docs.firecrawl.dev
│   └── moon-docs/           # sub-corpus from moonrepo.dev/docs
├── 30-extracts/             # populated by extract-knowledge-graph
│   ├── concepts/
│   ├── apis/
│   ├── tools/
│   └── entities/
├── 40-graphs/               # populated by sitemap-graph and extract-knowledge-graph
├── 50-syntheses/            # walkthroughs per tool, comparison views
├── 60-decisions/            # tool-specific pipeline variants
└── 90-conclusions.md        # final findings — what each tool actually is
```

## Status

`draft`. The pipeline specs are stable; the corpus has not yet been captured. Next move is the user's call: run `scrape-firecrawl` against `https://docs.firecrawl.dev` and `https://moonrepo.dev/docs` and let the rest flow.

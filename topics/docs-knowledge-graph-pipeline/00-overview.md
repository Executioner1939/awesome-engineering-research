---
id: docs-knowledge-graph-pipeline-overview
title: Overview
type: synthesis
synthesis_kind: summary
status: draft
confidence: medium
created: 2026-05-15
updated: 2026-05-15
covers: [docs-knowledge-graph-pipeline]
---

# Overview

## The problem

A developer faced with a tool — Moon, Firecrawl, anything documented as a sprawl of pages plus a thin cargo doc — has three sources of truth, each partial:

- The docs site, organised by what the writers thought made a good narrative.
- The repository, organised by directory structure.
- The API surface, organised by language convention.

None of these is the structure the developer actually wants in their head, which is closer to: "what are the primary objects this tool reasons over, what operations exist on them, what are the relationships between objects, and where does the surface area thin out into 'go read the source'."

## The thesis

If we capture the docs as a corpus, build the link graph between pages, and extract a knowledge graph of concepts / APIs / tools / entities, then:

- The **sitemap graph** tells us how the writers consolidated information — where the hubs are, what the spine of the docs is.
- The **knowledge graph** gives us the cross-page object model the writers did not explicitly draw.
- The two together let us answer questions the docs do not directly answer: "what concepts depend on this concept", "what APIs operate on this type", "where are the islands — concepts mentioned without ever being defined".

## Scope

In scope:

- Defining the pipelines (done — see [[scrape-firecrawl]], [[sitemap-graph]], [[extract-knowledge-graph]]).
- Capturing two corpora: Firecrawl docs (dogfood — the scraper documenting itself), Moon docs.
- Emitting the sitemap and knowledge graphs for each.
- Producing per-tool synthesis walkthroughs from the graphs.

Out of scope (lives in [[rag-ingestion-graph-stores]]):

- Choosing the runtime database for serving the graph.
- Implementing the RAG retrieval layer on top.
- Designing the agent-facing query surface.

## Success criteria

This topic is `stable` when:

1. Both corpora are captured and the corpus manifests pass the verification checks in [[scrape-firecrawl]].
2. Both sitemap graphs are emitted and the hub-page lists pass the smell test.
3. Both knowledge graphs are emitted with non-trivial concept and API coverage.
4. Per-tool walkthrough syntheses in `50-syntheses/` cite back to extracts that cite back to sources, with no dangling claims.
5. A concrete list of "things Moon does that I previously could not have answered without re-reading the docs" exists in `90-conclusions.md`. Same for Firecrawl.

## Non-goals

- Recreating the docs. The corpus is captured for parsing, not republishing. Output is graphs and syntheses, not a docs rewrite.
- Generality across every doc shape. The pipeline is biased toward developer-tool docs (concept + API + CLI). Marketing sites, blogs, and academic-paper collections want different extraction strategies.
- Live updates. The corpus is snapshotted; the pipeline runs again to refresh.

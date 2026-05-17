---
id: docs-knowledge-graph-pipeline-questions
title: Driving Questions
type: synthesis
synthesis_kind: summary
status: draft
confidence: medium
created: 2026-05-15
updated: 2026-05-15
covers: [docs-knowledge-graph-pipeline]
---

# Driving Questions

| id | question | status |
|---|---|---|
| q-sitemap-purpose | What does the sitemap graph reveal about how the docs consolidate information that a flat read of the docs does not? | open |
| q-extract-strategy | What extraction strategy gives the best concept / API / relation coverage for developer-tool docs — heuristic-only, LLM-assisted per-page, structured-source-first? | open |
| q-poor-docs | How do we recover a knowledge graph when the prose docs are thin or absent and the source-of-truth is the repo (cargo-doc, source code, README)? | open |
| q-graph-rendering | At what corpus size does a single Mermaid file stop being useful, and what faceting strategy preserves comprehension past that point? | open |
| q-corpora | What signal does dogfooding Firecrawl on its own docs give us about the pipeline's blind spots, beyond what Moon will give us? | open |

Each question is referenced from extracts and syntheses by its `q-` id. A question is `resolved` when there is a synthesis or conclusion that answers it, cited back to extracts.

## Why these questions

`q-sitemap-purpose` is the load-bearing question of the whole topic. If the sitemap graph does not reveal structure that flat reading misses, the pipeline is dressed-up scraping.

`q-extract-strategy` is the engineering tradeoff. Heuristic extraction is cheap and re-derivable; LLM extraction is high-recall but non-deterministic and expensive. Structured-source-first (read `rustdoc.json` instead of the cargo-doc prose) is the highest-quality but only available for some surfaces.

`q-poor-docs` is the case the user explicitly named — many real tools (Moon being one) have surface area whose docs do not cover everything; the repo is the de-facto truth. The pipeline must handle this without falling apart.

`q-graph-rendering` is a practical question with a known wall: Mermaid past ~150 nodes is unreadable in every renderer. The interesting question is what facets carry meaning.

`q-corpora` is a sanity check: the two corpora should fail in different ways. Firecrawl's docs are well-tended; Moon's surface area is broader. If they fail the same way, the pipeline is missing a degree of freedom.

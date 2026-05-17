---
name: scrape-firecrawl
description: Capture every page of a target docs site via Firecrawl into a topic's 20-sources/ directory as cleaned markdown plus link metadata. Use when starting a new topic that needs a docs corpus as its source-of-truth.
id: scrape-firecrawl
title: Scrape via Firecrawl
type: pipeline
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-17
related: [sitemap-graph, extract-knowledge-graph]
---

# Pipeline: Scrape via Firecrawl

Capture every page of a target site via Firecrawl, persisting each page as cleaned markdown plus link metadata. The captured corpus is the source-of-truth for downstream pipelines — sitemap-graph and extract-knowledge-graph both read from it and never re-fetch.

## Inputs

| name | type | notes |
|---|---|---|
| `base_url` | URL | the root of the docs site to crawl |
| `topic_id` | slug | the topic this corpus belongs to |
| `include_paths` | list[regex] | optional; only URLs matching at least one regex are crawled |
| `exclude_paths` | list[regex] | optional; URLs matching are skipped |
| `max_depth` | int | crawl depth from `base_url` |
| `max_pages` | int | safety cap |
| `firecrawl_endpoint` | enum | `/scrape` (one URL) \| `/crawl` (recursive) \| `/map` (URL discovery only) |
| `formats` | list | typically `['markdown']`; add `'links'` to get explicit link metadata |

## Outputs

Under `topics/<topic_id>/20-sources/`:

- `_manifest.md` — appended row per captured page (linking table).
- `<src-id>/_meta.md` — provenance file (frontmatter only).
- `<src-id>/content.md` — cleaned markdown.

## Procedure

1. **Plan the crawl**. If the size of the site is unknown, run `firecrawl-map` first against `base_url` with the include/exclude regexes. Record the URL list. Estimate cost: `n_pages × per-page-rate`. Compare against the rate-limit budget; if it exceeds 15% of monthly budget, surface the cost-rethinker decision.
2. **Execute the crawl** via the chosen Firecrawl endpoint. Request `formats: ['markdown', 'links']`. Set `onlyMainContent: true` to drop nav and footer noise.
3. **Persist each page**:
   - Allocate `src_<ULID>` for the page.
   - Compute `content_hash = sha256(markdown)`.
   - Write `_meta.md` with the universal frontmatter plus the source-specific extensions (`url`, `retrieved_at`, `retriever: firecrawl-crawl`, `content_hash`, `mime: text/markdown`, `crawl_depth`, `links_out`, `canonical_url` if redirected). The body of `_meta.md` is optional; the frontmatter carries the metadata.
   - Write `content.md` with the markdown returned by Firecrawl, no transformation.
4. **Append to manifest**. Update `20-sources/_manifest.md` with one row per page (id, title, source_type, status, url, retrieved_at, crawl_depth, content_hash).
5. **Update the global sources index**. Append the same rows to `INDEX/sources.md` (or regenerate).
6. **Record any failed fetches** in the manifest with `status: seed` and a `failure_reason` frontmatter field for later retry.

## Verification

- The number of rows in `_manifest.md` equals the number of `_meta.md` files in `20-sources/`.
- Every `_meta.md` has a corresponding `content.md` (or is annotated with `failure_reason`).
- Every `content_hash` in a `_meta.md` matches the SHA-256 of its `content.md`.
- `links_out` arrays in `_meta.md` are populated for at least 80% of pages — if fewer, the `links` format was likely not requested.

## Failure modes and remediation

| symptom | likely cause | fix |
|---|---|---|
| pages return empty markdown | site is heavily JS-rendered, `/scrape` insufficient | switch to `/scrape` with `actions` or use the firecrawl-interact build-side skill |
| crawl exhausts budget early | depth or include too permissive | tighten `include_paths`, lower `max_depth` |
| pages return `403` / `429` | rate-limit or anti-bot | reduce concurrency, set `politeness_delay`, ask user before retrying |
| same content captured under multiple URLs | URL canonicalisation not applied | follow `canonical_url`, deduplicate by `content_hash` |

## Worked example

`topics/docs-knowledge-graph-pipeline/` uses this pipeline twice:

- `base_url: https://docs.firecrawl.dev` (dogfood — capture the scraper's own docs)
- `base_url: https://moonrepo.dev/docs` (the user's stated pain point)

Each becomes its own sub-corpus under `20-sources/firecrawl-docs/` and `20-sources/moon-docs/` respectively, with separate manifests.

## Notes on Firecrawl specifics

Firecrawl exposes `/scrape`, `/crawl`, `/map`, `/extract`, and `/interact` endpoints. For docs-site capture, `/crawl` plus `formats: ['markdown', 'links']` is the workhorse. `/extract` (LLM-driven schema extraction) is **not** used in this pipeline — extraction is a separate, deterministic step in `extract-knowledge-graph` so we can re-derive the KG without re-spending LLM tokens.

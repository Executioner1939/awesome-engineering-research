---
id: convention-linking-tables
title: Linking Tables
type: convention
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Linking Tables

A linking table is a GFM markdown table that registers a set of entities and the links between them. Two flavours exist: **indexes** (global, under `INDEX/`) and **manifests** (per-topic, e.g. `20-sources/_manifest.md`).

## Why GFM tables specifically

GFM tables are the lowest common denominator:

- Renderable by GitHub, every static-site generator, every markdown editor.
- Grep-able. An agent can `grep '^| cpt_' INDEX/concepts.md` to list every concept row.
- Diffable. Per-row changes show up cleanly in `git diff`.
- Authorable. An agent or human can append a row without breaking the file.

## Standard columns

Every linking table includes:

| col | required | notes |
|---|---|---|
| `id` | yes | The canonical id of the entity. Always the first column. |
| `title` | yes | Human-readable name. |
| `type` | yes | The taxonomy type. |
| `status` | yes | Lifecycle status. |
| `confidence` | when applicable | Required on extract / synthesis / conclusion rows. |
| `tags` | no | Comma-separated tag list. |

Index-specific extra columns are defined per index file. For example, `INDEX/tools.md` adds `ecosystem`, `current_version`, `repository`.

## Sort order

Linking tables sort by `id` ascending unless the table declares a different `sort:` in its frontmatter.

## Append-only by default

Rows are not edited in place once `status: stable`. Changes happen by:

1. Marking the existing row `status: superseded` and adding a `superseded_by:` reference.
2. Appending a new row with the new id.

This keeps the table behaviour predictable for both agents and humans.

## Example

```markdown
---
id: index-tools
title: Tools Index
type: index
status: stable
created: 2026-05-15
updated: 2026-05-15
sort: id
---

# Tools Index

| id | title | type | status | ecosystem | current_version | repository |
|---|---|---|---|---|---|---|
| tool_firecrawl | Firecrawl | extract:tool | stable | npm,docker,cloud | 1.x | https://github.com/firecrawl/firecrawl |
| tool_moon | moon | extract:tool | stable | npm | 1.x | https://github.com/moonrepo/moon |
```

## Per-topic manifests

A topic's `20-sources/_manifest.md` is a linking table with source-specific columns:

```markdown
| id | title | type | status | url | retrieved_at | crawl_depth | content_hash |
```

A topic's `30-extracts/concepts/_manifest.md` (optional, regenerable) registers the concepts extracted within that topic. Manifests are convenience artefacts — the source of truth is per-file frontmatter.

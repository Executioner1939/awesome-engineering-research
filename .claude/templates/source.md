---
name: source-template
description: Shape of a single row in INDEX/sources.md and _archived/sources.md. Source rows describe an article, video, talk, book, paper, or RFC.
type: template
applies_to: INDEX/sources.md, _archived/sources.md
---

# Source row shape

`INDEX/sources.md` is a single markdown table. Each row is one source entity. Per-source frontmatter files are not used — the table row is the entity.

## Required columns

| column | type | notes |
|---|---|---|
| `id` | slug | `src_<short-slug>`. Stable; never reused. |
| `title` | string | Human-readable title. |
| `url` | URL | Canonical URL. If the URL has moved, prefer the canonical / archived form. |
| `type` | enum | `article \| video \| talk \| book \| paper \| rfc \| podcast \| course \| docs` |
| `category` | slug | Exactly one value from `TAXONOMY/categories.md`. Determines the README section the row renders under. |
| `published` | ISO-8601 date or `unknown` | Publication date if known, derived from URL or page metadata. `unknown` allowed. |
| `added` | ISO-8601 date | Date this row was added to the index. |
| `labels` | comma-separated slugs | Refinement labels (language, framework specifics). Optional; can be empty. |
| `status` | enum | `active \| archived \| superseded` |
| `notes` | string | One-line freeform. Optional. |

## Status semantics

- `active` — link resolves, content is the original or a stable archive copy.
- `archived` — link is dead, paywalled, or removed; row has moved to `_archived/sources.md` with `last_seen` and `reason` columns appended.
- `superseded` — content was replaced by a newer version (`superseded_by: <id>` column appended).

## Example row

```markdown
| src_rethinking-monad-error | Rethinking MonadError | https://typelevel.org/blog/2018/04/13/rethinking-monaderror.html | article | effect-systems | 2018-04-13 | 2018-04 | fp-scala,typelevel,error-handling | active | typelevel blog |
```

## Archived row shape

Archived rows additionally carry:

| column | type | notes |
|---|---|---|
| `last_seen` | ISO-8601 date | Date the link last resolved. |
| `reason` | enum | `404 \| 410 \| parked \| paywalled \| repo_archived \| eol \| timeout \| ssl_failure \| dns_failure` |
| `wayback` | URL or empty | `https://web.archive.org/...` snapshot if one exists. |

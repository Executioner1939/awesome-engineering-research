---
id: convention-ids-and-slugs
title: IDs and Slugs
type: convention
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# IDs and Slugs

## Slugs

- ASCII, lowercase, kebab-case.
- Punctuation: hyphens only. No underscores, no dots, no spaces.
- Length: aim for under 40 characters; hard ceiling at 64.
- Reserved prefixes: none (slugs are namespaced by directory).

Examples: `docs-knowledge-graph-pipeline`, `firecrawl-scrape-endpoint`, `moon-task-runner`.

## ULIDs

Used for high-volume artefacts where slug collisions are likely. ULID is preferred over UUID because:

- Lexicographically sortable by creation time (the first 10 chars encode the timestamp).
- 26-char Crockford base32, URL-safe, copy-paste-safe.
- One ulid per artefact, generated once, never edited.

Format: `<type-prefix>_<26-char ULID>`. Prefixes:

| prefix | type | examples |
|---|---|---|
| `cpt_` | concept | `cpt_01HZX0K2P3M4N5T6Q7R8S9V0XA` |
| `api_` | API entry | `api_01HZX1…` |
| `tool_` | tool | `tool_firecrawl` (often a slug, ULID for ambiguous cases) |
| `src_` | source | `src_01HZX2…` |
| `ent_` | entity | `ent_rfc-7807` (slug when canonical, ULID otherwise) |
| `q_` | question | `q_01HZX3…` |
| `dec_` | decision | `dec_01HZX4…` |

Topic ids stay slug-form (`docs-knowledge-graph-pipeline`) — they are few, named deliberately, and ULID prefixes would obscure them.

## Filename derivation

- ULID-prefixed id → `<id>.md`
- Slug id, top-level → `<id>.md` or `<id>/README.md`
- Lifecycle-stage docs inside a topic (`00-overview.md` etc.) → the id is the slug without the numeric prefix, namespaced by topic id when cross-referenced from outside (`docs-knowledge-graph-pipeline/overview`).

## Why not auto-incrementing integers

They look orderly but they:

- Collide on parallel authoring.
- Carry no creation-time information.
- Get re-used when a doc is deleted.

ULIDs and slugs together avoid all three.

## Renaming

Don't. Once an id is allocated and referenced, it is permanent. To "rename" a doc:

1. Create a new doc with the new id.
2. Mark the old doc `status: superseded`, set `superseded_by: [new-id]`.
3. Update inline wikilinks lazily — readers reach the new doc via the supersession chain.

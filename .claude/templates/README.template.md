---
name: readme-template
description: Top-level README rendering template. The README is a generated awesome-list view of INDEX/sources.md and INDEX/tools.md, grouped by label and sub-grouped by type. The regeneration step replaces content between the BEGIN/END markers; everything outside the markers is hand-edited.
type: template
applies_to: README.md
---

# README rendering template

The top-level `README.md` is **regenerated** from `INDEX/sources.md` and `INDEX/tools.md` on every PR (see `.github/workflows/index-regen-and-review.yml`). The regen step replaces the content between marker pairs:

```
<!-- BEGIN: <section-name> -->
... auto-generated content ...
<!-- END: <section-name> -->
```

## Sections to render

| marker | source | grouping |
|---|---|---|
| `BEGIN/END: badges` | static block from this template | n/a |
| `BEGIN/END: toc` | derived from active labels in TAXONOMY | flat list of category links |
| `BEGIN/END: stats` | counts of active vs archived rows | one line each |
| `BEGIN/END: category-<slug>` | rows from INDEX with `labels` containing `<slug>` and `status=active` | sub-tables: articles, videos, repos, books, papers |
| `BEGIN/END: triage` | `TRIAGE.md` preview | last N entries linked |
| `BEGIN/END: archived` | counts and link to `_archived/` | one line |

## Sub-table column shape

Articles / videos / talks / books / papers — drawn from `INDEX/sources.md`:

```markdown
| Title | Type | Published | Labels |
|---|---|---|---|
| [Rethinking MonadError](https://typelevel.org/...) | article | 2018-04-13 | fp-scala, error-handling |
```

Repos — drawn from `INDEX/tools.md`:

```markdown
| Repo | Language | Last pushed | Description |
|---|---|---|---|
| [tokio-rs/tokio](https://github.com/tokio-rs/tokio) | Rust | 2026-05-10 | A runtime for writing reliable asynchronous applications. |
```

## Hand-edited sections (outside markers)

- Title and one-paragraph intro.
- "Why this exists" — research philosophy.
- "How to contribute" — points at `.claude/skills/add-source/`.
- "Underlying model" — points at `.claude/skills/research-standard/SKILL.md`.
- License.

## Regeneration contract

1. Parse `INDEX/sources.md` and `INDEX/tools.md` as markdown tables.
2. Filter `status == active`.
3. Group by label. A row with multiple labels appears under each.
4. Within a group, sub-group by `type` and sort by `published` (descending) or `last_pushed` (descending).
5. Replace each `BEGIN/END` block in `README.md` with the rendered content.
6. The regen is idempotent: running it twice on unchanged inputs produces a byte-identical README.

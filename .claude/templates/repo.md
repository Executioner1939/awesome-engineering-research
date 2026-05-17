---
name: repo-template
description: Shape of a single row in INDEX/tools.md and _archived/tools.md. Repo rows describe a starred GitHub repository or other tool entry.
type: template
applies_to: INDEX/tools.md, _archived/tools.md
---

# Repo row shape

`INDEX/tools.md` is a single markdown table. Each row is one repo / tool entity. Per-repo frontmatter files are not used at this layer.

## Required columns

| column | type | notes |
|---|---|---|
| `id` | slug | `<owner>-<repo>` lowercased. Stable; never reused. |
| `full_name` | string | `owner/repo` exact case. |
| `url` | URL | `https://github.com/owner/repo` |
| `description` | string | First sentence from the repo description. Truncated to ~120 chars. |
| `language` | string or empty | Primary language as reported by GitHub. Empty for multi-lang / docs-only repos. |
| `stars` | integer | Snapshot at last sync. |
| `last_pushed` | ISO-8601 date | `pushed_at` from the GitHub API. |
| `labels` | comma-separated slugs | Drawn from `TAXONOMY/domains.md`. At least one. |
| `status` | enum | `active \| archived \| superseded` |
| `notes` | string | One-line freeform. Optional. |

## Status semantics

- `active` — repo exists, is not archived on GitHub, and `last_pushed` is within the configured staleness window (default 3 years).
- `archived` — one of: repo `archived: true` on GitHub, 404, EOL flagged by maintainer, or `last_pushed` older than the staleness window.
- `superseded` — explicitly replaced by a successor repo (`superseded_by: <id>` column appended).

## Example row

```markdown
| tokio-rs-tokio | tokio-rs/tokio | https://github.com/tokio-rs/tokio | A runtime for writing reliable asynchronous applications with Rust. | Rust | 27500 | 2026-05-10 | fp-rust,async-runtimes,distributed-systems | active |  |
```

## Archived row shape

Archived rows additionally carry:

| column | type | notes |
|---|---|---|
| `last_seen` | ISO-8601 date | Date this row last passed liveness. |
| `reason` | enum | `404 \| repo_archived \| stale \| eol \| superseded` |
| `successor` | id or empty | The repo that replaced it, if any. |

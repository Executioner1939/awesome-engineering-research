# Contributing

This repo is a curated and machine-maintained reading + tools corpus. Most maintenance is automated. Manual contributions are welcome via the paths below.

## Adding an entry

**With Claude Code installed locally:**

```
/add-source https://example.com/article
```

The `add-source` skill at `.claude/skills/add-source/SKILL.md` validates the URL, derives metadata, picks labels from `.claude/skills/research-standard/TAXONOMY/domains.md`, and appends the row.

**Without Claude Code:**

Open a PR adding a row to `INDEX/sources.md` (articles, videos, talks, papers, books, podcasts, courses, RFCs, docs) or `INDEX/tools.md` (repos). Follow the column shape in `.claude/templates/source.md` or `.claude/templates/repo.md`. The `frontmatter-lint` workflow will validate it.

Required for every row:

- `id` — kebab-case slug, unique across active + archived.
- `url` — must resolve (no 4xx, no DNS failure).
- `labels` — at least one **domain** label from `TAXONOMY/domains.md`. Refinement labels welcome.
- `status: active`.

## Reporting dead links

Don't — `link-check` runs weekly and moves dead rows to `_archived/` with a tombstone. If you spot one in the meantime, open a PR moving the row yourself.

## Renaming labels

Open a PR that:

1. Updates `.claude/skills/research-standard/TAXONOMY/domains.md`.
2. Updates affected rows in `INDEX/sources.md` and `INDEX/tools.md`.
3. Updates the regen script if the label was special-cased.

## Style

- Lowercase, kebab-case labels.
- Description truncation at 120 chars for repos.
- Alphabetical row order by `id` within each table.

## CI

Five workflows under `.github/workflows/`:

| workflow | trigger | what it does |
|---|---|---|
| `link-check` | weekly Mon 06:00 UTC | HEAD-checks every URL, opens a PR moving dead ones to `_archived/` |
| `star-sweep` | weekly Mon 07:00 UTC | Diffs current GH stars against `INDEX/tools.md`, opens PR |
| `frontmatter-lint` | every PR | Validates new INDEX/ rows against the standard |
| `index-regen-and-review` | every PR | Regenerates `README.md` from `INDEX/`, then Claude reviews against the standard |
| `new-releases-triage` | daily 05:30 UTC | Surfaces new releases in interest areas into `TRIAGE.md` |

Workflows that use `anthropics/claude-code-action` (`index-regen-and-review` and `new-releases-triage`) authenticate via a Claude Code OAuth token stored as `CLAUDE_CODE_OAUTH_TOKEN` in repo secrets — generated locally with `claude setup-token`. No Anthropic API key required if your Claude Code subscription covers usage. The other three workflows (`link-check`, `star-sweep`, `frontmatter-lint`) need only the default `GITHUB_TOKEN`.

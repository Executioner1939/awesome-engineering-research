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

Seven workflows under `.github/workflows/` form a closed loop: cron sweeps open PRs labelled `agent-authored`, a quality gate reviews them against the standard, an @claude responder applies fixes, and the gate auto-merges once it passes.

| workflow | trigger | what it does |
|---|---|---|
| `link-check` | weekly Mon 06:00 UTC | HEAD-checks every URL; opens a PR moving dead rows to `_archived/`, tagged `agent-authored` |
| `star-sweep` | daily 07:00 UTC | Diffs current GH stars against `INDEX/tools.md`; opens a PR on non-zero delta, tagged `agent-authored` |
| `new-releases-triage` | daily 05:30 UTC | Surfaces new releases in interest areas into `TRIAGE.md`; opens a PR tagged `agent-authored` |
| `frontmatter-lint` | every PR | Validates INDEX/ row shapes against the standard |
| `index-regen` | every PR touching INDEX/ | Regenerates `README.md` from `INDEX/`, commits to the PR branch |
| `auto-review` | every PR with `agent-authored` label | Lint + Claude review against only the part of the standard the diff touches. Auto-approves and merges if clean. Posts a `@claude` request-changes review if not |
| `claude-respond` | `@claude` mention on `agent-authored` PR | Agent applies the requested fixes on the PR branch, which re-triggers `auto-review` until it passes or a human steps in |

**The loop**:

```
cron sweep -> PR opened (agent-authored)
              |
              v
       index-regen + frontmatter-lint + auto-review
              |
              +---- APPROVED ----> squash-merge, branch deleted
              |
              +---- CHANGES_REQUESTED + @claude ----> claude-respond
                                                          |
                                                          v
                                                  push fixes -> re-run auto-review
```

**Auth**:

The four workflows that use `anthropics/claude-code-action` (`index-regen`, `new-releases-triage`, `auto-review`, `claude-respond`) authenticate via a Claude Code OAuth token stored as `CLAUDE_CODE_OAUTH_TOKEN` in repo secrets — generated locally with `claude setup-token`. No Anthropic API key required if your Claude Code subscription covers usage. The other three workflows (`link-check`, `star-sweep`, `frontmatter-lint`) need only the default `GITHUB_TOKEN`. (`index-regen` does not actually call claude-code-action; it's pure Python — included in the OAuth list for accuracy only if you later extend it.)

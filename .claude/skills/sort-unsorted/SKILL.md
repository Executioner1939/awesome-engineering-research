---
name: sort-unsorted
description: Re-classify rows in INDEX/sources.md and INDEX/tools.md that landed in the `unsorted` bucket — either with `category=unsorted` or `kind=unsorted`. Re-applies the categories.md vocabulary and the kind heuristic with a fresh attempt, using GitHub topics, description, README excerpts. Use on demand or on a slow weekly schedule to drain the unsorted backlog.
---

# sort-unsorted

The classifying agent runs in `add-source` and `star-sweep` are intentionally conservative — when in doubt, a row lands with `kind=unsorted` or `category=unsorted`. This skill is the cleanup path: it takes a second, more careful look at those rows.

## Inputs

| input | type | notes |
|---|---|---|
| target | enum | `tools \| sources \| both`. Default `both`. |
| max_rows | int | Cap per run. Default 50. Prevents thrashing on a large backlog. |
| dry_run | bool | If true, write the proposal to `/tmp/sort-unsorted-proposal.md` and stop. Default false. |

## Procedure

1. **Snapshot.** Parse `INDEX/sources.md` and `INDEX/tools.md`. Collect rows where `category=unsorted` or `kind=unsorted` (active rows only — archived stays archived).

2. **Enrich each candidate row.** For repos, refetch `gh api repos/<owner>/<repo>` (description, topics, language, README excerpt — `gh api repos/<owner>/<repo>/readme` then base64-decode and keep the first 4000 chars). For sources, fetch the page title and meta description if not already present.

3. **Re-classify.** Apply the heuristic in `.claude/skills/research-standard/TAXONOMY/categories.md`:
   - **Category**: match against scope columns. Pick the most specific. Falls back to `unsorted` if still no fit.
   - **Kind** (tools only): topics → description verbs → README content (look for `[[bin]]` in Cargo.toml, `main` package in Go, `bin/` directory, CLI entry-point in `package.json`, "Usage" sections that show shell commands). Falls back to `unsorted` if no clear signal.

4. **Decide stay-or-move.**
   - If new classification differs from current → write the row update.
   - If new classification is also `unsorted` after second pass → leave as-is and mark with `notes: "second-pass uncertain"` so it isn't re-tried until something changes.

5. **Apply.** Write updates back to `INDEX/sources.md` and `INDEX/tools.md`. Keep id ordering. Bump the row's `last_seen` to today.

6. **Open a PR.** Branch `sort-unsorted/<YYYY-MM-DD>`. Labels `sort-unsorted,automated,agent-authored`. PR body: per-category re-distribution counts, list of rows still uncertain.

## Constraints

- Only operates on rows already in INDEX. Never adds new rows. Never archives.
- Never widens a category — once a row was sorted into a fine category, it stays there. `sort-unsorted` only narrows from `unsorted`.
- The heuristic is the same one in `categories.md` — read that file, do not invent rules.
- Respect `notes: "second-pass uncertain"`. Skip those rows; humans can re-tag them by editing `notes`.

## Verification checklist

- [ ] Total rows touched ≤ `max_rows`.
- [ ] No row moved from a fine category back to `unsorted`.
- [ ] Updates committed with a single branch and PR; the `auto-review` workflow gates the merge.

## Related

- `/sort-unsorted` — slash command wrapper.
- `add-source` — applies the same heuristic to a single new row.
- `star-sweep` — bulk add that may produce `unsorted` rows.

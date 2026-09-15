---
name: star-sweep
description: Diff your current GitHub stars against INDEX/tools.md, add newly-starred repos, archive unstarred/stale ones, have Claude classify and describe new and unsorted rows (extending the taxonomy when needed), regenerate the README and commit straight to master. Runs daily via the star-sweep GitHub Action.
---

# star-sweep

Keeps `INDEX/tools.md` in sync with the user's actual GitHub star list, and sweeps staleness.

## Inputs

| input | type | notes |
|---|---|---|
| user | string | GitHub login. Default `Executioner1939`. |
| staleness_window | duration | Default `3 years`. |

## Procedure (as run by `.github/workflows/star-sweep.yml`)

1. **Pull current stars** — `gh api "users/<user>/starred?per_page=100" --paginate` into `/tmp/stars-current.jsonl`. The run aborts if fewer than 50 stars come back (truncated list guard).

2. **Deterministic diff** — `.github/scripts/apply-star-sweep.py`:
   - `to_add` = starred − active − archived → new active row with `category=unsorted`, `kind=unsorted`, first-pass labels, cleaned GitHub description.
   - `to_unstar` = active − starred → `_archived/tools.md`, reason `user_unstarred`.
   - `to_restore` = archived with reason `user_unstarred` ∩ starred → back to active.
   - Active rows archived on GitHub → reason `repo_archived`; no push inside the staleness window → reason `stale`.
   - Every other active row gets `stars` / `last_pushed` refreshed.
   - Emits `/tmp/star-curation-queue.jsonl`: all new/restored rows plus up to `--backlog` (default 40) existing rows that are still `unsorted` or lack a description.

3. **Curation (Claude)** — `anthropics/claude-code-action` with the prompt in `.github/prompts/star-curation.md`. For every queued row it decides `category`, `kind`, `labels`, `description`, adding categories to `TAXONOMY/categories.md` or refinement labels to `TAXONOMY/domains.md` when a real gap shows up. Decisions go to `/tmp/star-curation.json` and are applied by `.github/scripts/apply-curation.py --strict`, which rejects anything not in the taxonomy. The step is `continue-on-error`: if Claude is unavailable the deterministic sync still lands.

4. **Lint gate** — `lint-index.py --categories …`. If lint fails after curation, the curation and taxonomy edits are reverted to the pre-curation snapshot and lint is run again on the deterministic result.

5. **Regenerate README** — `regen-readme.py` reads categories from `categories.md`, so new categories render without code changes.

6. **Commit to master** — `INDEX/`, `_archived/`, `README.md`, `TAXONOMY/`. A dated report `_archived/star-sweep-report-<YYYY-MM-DD>.md` is written only on runs that add/remove/restore/archive rows. Commit subject: `chore(stars): sync +<add> -<remove> restored <n> stale <n>, curation=<applied|skipped|reverted>`.

Why direct-to-master: PRs opened with `GITHUB_TOKEN` never trigger `pull_request` workflows, so the earlier PR-plus-auto-review loop stalled for four months with 120+ unmerged PRs. The lint gate is the merge check.

## Label derivation

For each new repo:

1. Start from the `topics` array (GitHub repo topics). Map each to the closest taxonomy label.
2. Add domain labels from `TAXONOMY/domains.md` by keyword matching on description + language.
3. Add refinement labels (e.g., `rust`, `async-runtimes`, `kafka`) where applicable.
4. Sort alphabetically, comma-separated.

## Constraints

- Never hard-delete rows from `INDEX/tools.md`. Always move to `_archived/`.
- `to_unstar` is a user intent signal — the user explicitly removed the star. Archive; restore only if the star comes back.
- Description: one sentence, 60–200 chars, saying what the repo is and what it is for (see `.github/prompts/star-curation.md`).
- Be respectful of GH API rate limits; the paginated listing is cheap (~5 calls for a few hundred stars), but per-repo refresh in step 4 hits per-repo endpoints — cap at 20/s.

## Verification checklist

- [ ] No row appears in both `INDEX/tools.md` and `_archived/tools.md`.
- [ ] Every moved row has `last_seen` and `reason`.
- [ ] Sweep report exists.
- [ ] Commit subject follows the convention above; `curation=` reflects what happened.
- [ ] Star counts in unchanged rows refresh to current values.

## Related

- `.github/workflows/star-sweep.yml` — daily runner.
- `.github/prompts/star-curation.md` — the curation prompt.
- `.github/scripts/apply-curation.py` — validating applier for curation decisions.
- `dead-link-sweep` — orthogonal sweep for source URLs.
- `new-releases-triage` — discovers candidates that may eventually become stars.

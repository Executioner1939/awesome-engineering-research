---
name: star-sweep
description: Diff your current GitHub stars against INDEX/tools.md, emit a PR adding newly-starred repos and flagging unstarred ones. Also re-checks staleness (last_pushed > 3 years or archived) and moves stale repos to _archived/tools.md. Use weekly via the star-sweep GitHub Action.
---

# star-sweep

Keeps `INDEX/tools.md` in sync with the user's actual GitHub star list, and sweeps staleness.

## Inputs

| input | type | notes |
|---|---|---|
| user | string | GitHub login. Default `Executioner1939`. |
| staleness_window | duration | Default `3 years`. |

## Procedure

1. **Pull current stars.**
   ```bash
   gh api users/<user>/starred --paginate \
     --jq '.[] | {full_name, html_url, description, language, stargazers_count, pushed_at, archived, topics, license: (.license.spdx_id // null)}' \
     > /tmp/stars-current.jsonl
   ```

2. **Snapshot existing tools.**
   - Parse `INDEX/tools.md` as a markdown table.
   - Build sets: `current_stars` (from API), `indexed_active` (rows with `status=active`), `indexed_archived` (rows with `status=archived`).

3. **Compute diff.**
   - `to_add` = `current_stars` − `indexed_active` − `indexed_archived` — newly starred since last sync.
   - `to_unstar` = `indexed_active` − `current_stars` — present in INDEX but no longer starred. These get moved to `_archived/tools.md` with reason `user_unstarred`.
   - `to_restar` = `indexed_archived` ∩ `current_stars` — previously unstarred but starred again. Move back from archive with reason `restarred`.

4. **Staleness re-check on `indexed_active`.**
   - For each existing active row, refresh `pushed_at` and `archived` from the API.
   - If `archived: true` → move to `_archived/` with reason `repo_archived`.
   - If `pushed_at < today − staleness_window` → move to `_archived/` with reason `stale`.

5. **Apply.**
   - For `to_add`: derive labels (see [Label derivation](#label-derivation)) and append rows to `INDEX/tools.md`.
   - For `to_unstar` and staleness hits: move rows to `_archived/tools.md` with tombstone columns.
   - For `to_restar`: move rows back to `INDEX/tools.md`, refreshing stars / pushed / labels.

6. **Generate sweep report.**
   - Write `_archived/star-sweep-report-<YYYY-MM-DD>.md`: counts (added, unstarred, restarred, stale, archived-by-maintainer), top languages added, total active after sweep.

7. **Commit.**
   - Branch: `star-sweep/<YYYY-MM-DD>`.
   - Title: `chore(stars): sync — +<add> -<remove> (<YYYY-MM-DD>)`.
   - Body: paste the sweep report.

## Label derivation

For each new repo:

1. Start from the `topics` array (GitHub repo topics). Map each to the closest taxonomy label.
2. Add domain labels from `TAXONOMY/domains.md` by keyword matching on description + language.
3. Add refinement labels (e.g., `rust`, `async-runtimes`, `kafka`) where applicable.
4. Sort alphabetically, comma-separated.

## Constraints

- Never hard-delete rows from `INDEX/tools.md`. Always move to `_archived/`.
- `to_unstar` is a user intent signal — the user explicitly removed the star. Archive, don't restore.
- Description truncation: first sentence or 120 chars.
- Be respectful of GH API rate limits; the paginated listing is cheap (~5 calls for a few hundred stars), but per-repo refresh in step 4 hits per-repo endpoints — cap at 20/s.

## Verification checklist

- [ ] No row appears in both `INDEX/tools.md` and `_archived/tools.md`.
- [ ] Every moved row has `last_seen` and `reason`.
- [ ] Sweep report exists.
- [ ] Branch and commit follow naming convention.
- [ ] Star counts in unchanged rows refresh to current values.

## Related

- `.github/workflows/star-sweep.yml` — weekly runner.
- `dead-link-sweep` — orthogonal sweep for source URLs.
- `new-releases-triage` — discovers candidates that may eventually become stars.

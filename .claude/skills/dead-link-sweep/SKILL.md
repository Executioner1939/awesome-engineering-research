---
name: dead-link-sweep
description: Sweep INDEX/sources.md (and optionally INDEX/tools.md) for dead links, moving entries with confirmed-dead URLs to _archived/ with tombstones (last_seen, reason, optional wayback link). Use weekly via the link-check GitHub Action, or on demand when the user wants a manual sweep. Never hard-deletes.
---

# dead-link-sweep

Validates URL liveness across `INDEX/sources.md` and (optionally) `INDEX/tools.md`, moves confirmed-dead rows to `_archived/`, and records a tombstone with `last_seen`, `reason`, and (where available) a Wayback Machine snapshot URL.

## Inputs

| input | type | notes |
|---|---|---|
| target | enum | `sources \| tools \| both`. Default `both`. |
| parallelism | int | Concurrent curl HEADs. Default 20. |
| timeout | int | Per-request seconds. Default 10, retry once at 30. |

## Procedure

1. **Snapshot the input.**
   - Read `INDEX/sources.md` and / or `INDEX/tools.md` into memory as a list of rows.
   - Filter to `status == active` — archived rows are not re-checked.

2. **Liveness probe.**
   - For each row, `curl -sIL -m <timeout> -w "%{http_code}|%{url_effective}" <url>`.
   - Run up to `parallelism` requests concurrently using xargs `-P` or a shell job pool.
   - Classify per [URL liveness rules](#url-liveness-rules) below.

3. **For confirmed-dead rows, fetch Wayback snapshot.**
   - `curl -sI "https://archive.org/wayback/available?url=<urlencoded>"` — extract `closest.url` if present.
   - Record as `wayback` column.

4. **Update tables.**
   - Move each dead row from `INDEX/<file>.md` to `_archived/<file>.md`.
   - Append columns `last_seen=<today>`, `reason=<code>`, `wayback=<url|empty>`.
   - Keep alphabetical order by `id` in both files.

5. **Generate sweep report.**
   - Write `_archived/sweep-report-<YYYY-MM-DD>.md` summarising: total checked, total moved, breakdown by reason, time elapsed.

6. **Commit.**
   - Branch name: `link-sweep/<YYYY-MM-DD>`.
   - Title: `chore(archive): sweep N dead links (<YYYY-MM-DD>)`.
   - Body: paste the sweep report.

## URL liveness rules

| condition | classification |
|---|---|
| 2xx | active |
| 3xx → final 2xx | active, update `url` to final |
| 3xx → final 4xx (not 401/403) | archived, reason from final |
| 401, 403 | active, note `auth_or_bot_block` |
| 404, 410 | archived, reason `404` / `410` |
| 5xx after one 30-s retry | active, note `5xx_at_last_check` (don't archive — could be transient) |
| DNS failure | archived, reason `dns_failure` |
| SSL failure | archived, reason `ssl_failure` |
| Connection refused / reset | archived, reason `connection_failure` |
| Timeout > 30 s on retry | archived, reason `timeout` |

## Tools target additions

When `target == tools`:

- Additionally call `gh api repos/<owner>/<repo>` for each repo (cheap; 5000 req/h limit; pace at 20/s).
- If `archived: true` → archive with reason `repo_archived`.
- If 404 → archive with reason `404`.
- If `pushed_at < today - 3 years` → archive with reason `stale`.

## Constraints

- Never hard-delete. Always move to `_archived/`.
- Never modify `_archived/` rows already there (those are tombstones — terminal state).
- If the same URL was previously archived but is now live again, leave the archived row in place and let `add-source` handle re-adding (preserves audit trail).
- Be polite: HEAD only, parallelism cap, User-Agent string `awesome-engineering-research/link-sweep`.

## Verification checklist

- [ ] No row appears in both `INDEX/<file>.md` and `_archived/<file>.md`.
- [ ] Every row moved has `last_seen` and `reason` set.
- [ ] Sweep report exists for this run.
- [ ] Branch and commit follow the naming convention.

## Related

- `.github/workflows/link-check.yml` — runs this skill weekly.
- `add-source` — the inverse operation (single-entry add).

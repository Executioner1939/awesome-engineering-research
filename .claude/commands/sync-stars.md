---
description: Diff your current GitHub stars against INDEX/tools.md. Adds newly-starred repos. Moves unstarred and stale (>3 years no push) repos to _archived/tools.md. Refreshes star counts and pushed dates on unchanged rows.
argument-hint: [user=Executioner1939] [staleness=3y]
---

# /sync-stars

Invoke the `star-sweep` skill at `.claude/skills/star-sweep/SKILL.md`.

Arguments parsed from `$ARGUMENTS`:
- `user=` — GitHub login. Defaults to `Executioner1939`.
- `staleness=` — staleness window. Defaults to `3y` (3 years). Accepts `1y`, `18m`, etc.

## Procedure

1. Read `.claude/skills/star-sweep/SKILL.md` for the full procedure.
2. Parse arguments.
3. Execute the skill: pull current stars, compute diff (to_add / to_unstar / to_restar), staleness re-check, apply, report, commit.
4. On completion, surface a summary: counts added / unstarred / restarred / stale / archived-by-maintainer, top languages added, total active after sweep, branch name.

## Constraints

- `gh` must be authenticated. If `gh auth status` reports unauthenticated, surface that and stop.
- Rate-limit per-repo refresh to 20 req/s.

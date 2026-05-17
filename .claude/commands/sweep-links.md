---
description: Sweep INDEX/sources.md (and optionally INDEX/tools.md) for dead URLs, moving confirmed-dead rows to _archived/ with tombstones. Never hard-deletes.
argument-hint: [target=sources|tools|both] [parallelism=20]
---

# /sweep-links

Invoke the `dead-link-sweep` skill at `.claude/skills/dead-link-sweep/SKILL.md`.

Arguments parsed from `$ARGUMENTS`:
- `target=` — `sources`, `tools`, or `both`. Defaults to `both`.
- `parallelism=` — concurrent HEAD checks. Defaults to 20.

## Procedure

1. Read `.claude/skills/dead-link-sweep/SKILL.md` for the full procedure.
2. Parse arguments.
3. Execute the skill: snapshot inputs, liveness probe, fetch Wayback snapshots, move rows, write sweep report, commit.
4. On completion, surface a summary: total checked, total moved, breakdown by reason, branch name.

## Constraints

- Never invoke without confirming the user wants destructive (move) action; the skill itself does the moves, so the command should warn before running on an unclean working tree.
- If parallelism > 50, cap and warn.

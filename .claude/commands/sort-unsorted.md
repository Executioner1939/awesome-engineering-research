---
description: Drain the unsorted backlog by re-classifying rows with category=unsorted or kind=unsorted using a more careful second pass (richer GitHub metadata, README excerpts). Opens an agent-authored PR with the proposed updates.
argument-hint: [target=tools|sources|both] [max=50] [dry-run]
---

# /sort-unsorted

Invoke the `sort-unsorted` skill at `.claude/skills/sort-unsorted/SKILL.md`.

Arguments parsed from `$ARGUMENTS`:
- `target=` — `tools`, `sources`, or `both`. Defaults to `both`.
- `max=` — cap per run. Defaults to 50.
- `dry-run` — write the proposal to `/tmp/sort-unsorted-proposal.md` without applying.

## Procedure

1. Read `.claude/skills/sort-unsorted/SKILL.md` for the full procedure.
2. Parse arguments.
3. Snapshot, enrich, re-classify, decide, apply, PR.
4. On completion, surface a summary: rows scanned, reclassified, still-uncertain, top categories assigned.

## Constraints

- Conservative — when uncertain after the second pass, leave as `unsorted` with `notes: "second-pass uncertain"` so the row isn't re-tried until manually edited.
- Cap at `max` rows per run.
- Single PR per run; `auto-review` gates the merge.

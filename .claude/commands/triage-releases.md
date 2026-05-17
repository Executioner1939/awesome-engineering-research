---
description: Scan configured release feeds for new libraries/frameworks/tools in the user's interest areas (Rust, distributed systems, observability, build tooling, FP, DevOps, knowledge-graph/RAG). Append candidates to TRIAGE.md for manual review. Never auto-adds to INDEX/.
argument-hint: [areas=rust,distributed-systems,...] [since=30d]
---

# /triage-releases

Invoke the `new-releases-triage` skill at `.claude/skills/new-releases-triage/SKILL.md`.

Arguments parsed from `$ARGUMENTS`:
- `areas=` — comma list of interest areas to scan. Defaults to all configured in `.claude/skills/new-releases-triage/sources.yml`.
- `since=` — only consider items published within this window. Defaults to `30d`.

## Procedure

1. Read `.claude/skills/new-releases-triage/SKILL.md` for the full procedure.
2. Parse arguments.
3. Auto-prune rows in `TRIAGE.md` older than 60 days into `_archived/triage-pruned-<YYYY-MM-DD>.md`.
4. Execute the skill: read source config, fetch feeds, filter, gather metadata, append to TRIAGE.md, report, commit.
5. On completion, surface a summary: per-source counts surveyed / filtered / appended, pruned count.

## Constraints

- Never auto-add to INDEX/. The user reviews TRIAGE.md and explicitly graduates entries with `/add-source`.
- Dedupe rigorously: never add a candidate already in INDEX/ (active or archived) or TRIAGE.md.
- Be polite to feeds: ETag / If-Modified-Since, rate-limit 1 req/s per host.

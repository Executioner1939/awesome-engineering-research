---
name: new-releases-triage
description: Scan configured release feeds for new libraries, frameworks, and tools in the user's interest areas (Rust, distributed systems, observability, build tooling, FP, DevOps, knowledge-graph / RAG). Append candidates to TRIAGE.md for manual review. Never auto-adds to INDEX/. Use daily via the new-releases-triage GitHub Action, or on demand.
---

# new-releases-triage

Surfaces newly released or newly notable libraries / frameworks / tools that match the user's interest areas. The output is a triage queue (`TRIAGE.md`); a human decides what graduates to `INDEX/tools.md` via `add-source`.

## Interest areas (configurable)

The default set, drawn from the user's profile:

| area | sources |
|---|---|
| Rust ecosystem | crates.io most-downloaded-this-week, lib.rs, this-week-in-rust newsletter, blessed.rs updates, github.com/trending/rust |
| Distributed systems | github.com/trending — filter description for `distributed`, `consensus`, `replication`, `event-sourcing`, `cqrs` |
| Observability | OpenTelemetry release feed, github.com/trending — filter for `tracing`, `metrics`, `profiling` |
| Build tooling | moonrepo.dev releases, Bazel registry, github.com/trending — filter for `monorepo`, `build`, `cargo`, `bazel` |
| FP | typelevel.org releases, Scala 3 changelog, this-week-in-rust FP-adjacent items |
| DevOps / IaC | OpenTofu releases, terraform registry trending, github.com/trending — filter for `terraform`, `iac`, `argocd`, `flux` |
| Knowledge-graph / RAG | github.com/trending — filter for `rag`, `knowledge-graph`, `vector-db`, `embeddings`, `graphrag` |
| LLM application architecture | Anthropic / OpenAI release notes, github.com/trending — filter for `llm`, `agents`, `mcp`, `tool-use` |

Configuration lives at `.claude/skills/new-releases-triage/sources.yml` (see Bootstrap below).

## Procedure

1. **Read source config.**
   - `.claude/skills/new-releases-triage/sources.yml` — each entry has `name`, `feed_url` (RSS / Atom / JSON), `interest_area`, `keywords` (additional filter).

2. **Fetch each feed.**
   - GET each `feed_url`. Cache via ETag / If-Modified-Since.
   - Parse as RSS / Atom / JSON depending on Content-Type.
   - For GitHub trending feeds, use the unofficial JSON endpoint or scrape the trending page (HTML → article rows).

3. **Filter.**
   - Discard items already present in `INDEX/tools.md` (active) or `_archived/tools.md` (already considered).
   - Discard items already present in `TRIAGE.md` (already queued).
   - Apply per-source keyword filter to title + description.
   - Apply staleness filter: published_at within last 30 days.

4. **For each surviving candidate, gather metadata.**
   - If URL points at GitHub, call `gh api repos/<owner>/<repo>` for: description, language, stars, license, last_pushed, topics.
   - If non-GitHub, fetch `<title>` and `<meta property="og:description">`.

5. **Append to `TRIAGE.md`.**
   - Section per interest area, oldest-first within section so reviewer sees backlog.
   - Each row: `| <added_at> | <name> | <url> | <interest_area> | <stars/desc> | [keep] [skip] |`.
   - The `[keep]` / `[skip]` markers are clickable in IDEs / are easy to filter when reviewing.

6. **Generate run report.**
   - Number of candidates surveyed per source.
   - Number that survived filters.
   - Number appended to TRIAGE.md.

7. **Commit.**
   - Branch: `triage/<YYYY-MM-DD>`.
   - Title: `triage: +<N> new candidates (<YYYY-MM-DD>)`.
   - Body: per-source counts.

## TRIAGE.md shape

`TRIAGE.md` lives at the repo root. Structure:

```markdown
# Triage queue

Candidates surfaced by `new-releases-triage`. Review and either:
- Run `/add-source <url>` to graduate to `INDEX/tools.md` (then delete the row here), OR
- Mark `[skip]` with a one-line reason (then delete the row here).

Rows older than 60 days that have not been actioned are auto-pruned by the workflow.

## Rust ecosystem

| Added | Name | URL | Stars | Action |
|---|---|---|---|---|
...

## Distributed systems
...
```

## Bootstrap

On first run, if `.claude/skills/new-releases-triage/sources.yml` does not exist, create it with the default set documented under [Interest areas](#interest-areas-configurable). The user edits this file to tune coverage.

## Constraints

- Never auto-add to `INDEX/`. Triage is human-in-the-loop.
- Never push rows to `TRIAGE.md` that are already in `INDEX/tools.md` or `_archived/tools.md` — the dedup step is non-negotiable.
- Be polite to feeds: use ETag / If-Modified-Since; rate-limit to 1 req/s per host.
- Auto-prune rows in TRIAGE.md older than 60 days at the start of each run, moving them to `_archived/triage-pruned-<YYYY-MM-DD>.md` for audit.

## Verification checklist

- [ ] No candidate already present in `INDEX/tools.md` is in `TRIAGE.md`.
- [ ] Each row has at least `added`, `name`, `url`, `interest_area`.
- [ ] Auto-prune log exists if any rows were dropped.
- [ ] Per-source counts in the run report sum correctly.

## Related

- `add-source` — the graduation path for a triaged candidate.
- `star-sweep` — alternative path: starring the repo on GitHub will get it picked up next sync.

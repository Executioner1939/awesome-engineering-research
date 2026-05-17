---
name: add-source
description: Add a new article, video, talk, paper, book, podcast, or repo to the corresponding INDEX/ table with correctly-shaped frontmatter, derived labels, validated URL, and provenance. Use whenever the user wants to add reading material or a new tool to the awesome list. Wraps the row shapes defined in `.claude/templates/{source,repo}.md`.
---

# add-source

Adds one entry to `INDEX/sources.md` (articles, videos, papers, books, talks, podcasts, courses, RFCs, docs) or `INDEX/tools.md` (repos / tools).

## Inputs

| input | type | notes |
|---|---|---|
| URL | string | The entry's canonical URL. Required. |
| type | enum | `article \| video \| talk \| book \| paper \| rfc \| podcast \| course \| docs \| repo` |
| labels | comma list | Optional. If omitted, derived from URL host + page metadata. |
| notes | string | Optional one-liner. |

## Procedure

1. **Resolve and validate URL.**
   - HEAD-check with `curl -sIL -m 10`.
   - If 4xx (not 401/403) or DNS/SSL failure → abort with an error stating the URL is dead. Suggest the user re-check.
   - Follow redirects; record the final URL as `url` if it differs from the input.
   - For `repo` type, additionally call `gh api repos/<owner>/<repo>` and verify `archived: false`. If archived, warn and ask whether to add anyway (will land in `_archived/` immediately).

2. **Derive metadata.**
   - `title` — for `repo`: `full_name` from GH API. For others: `<title>` of the page, fetched with a single GET if HEAD didn't include it.
   - `published` — for articles, parse from URL pattern (`/2024/07/...`), then page metadata `<meta property="article:published_time">`. For repos, `created_at` from GH API. For videos with `youtube.com/watch`, fall back to upload date in page metadata.
   - `description` — for repos, the GH `description` field, first sentence, ≤120 chars.
   - `language` — for repos, primary language from GH API.
   - `stars`, `last_pushed`, `archived`, `license` — for repos, all from GH API.

3. **Derive labels.**
   - Start from the user-supplied labels (if any).
   - Add domain labels from `TAXONOMY/domains.md` based on URL host + title keywords (article/video) or `topics` array + description + language (repo).
   - Add refinement labels (e.g., `fp-scala`, `kubernetes`, `event-sourcing`) where they apply.
   - Output a single canonical comma-separated string sorted alphabetically.

4. **Assign `id`.**
   - Articles/videos: `src_<slug-from-title>` truncated to 60 chars, kebab-case.
   - Repos: `<owner>-<repo>` lowercased.
   - Verify uniqueness against existing rows in the relevant INDEX file. If collision, append a `-2` discriminator.

5. **Append row.**
   - Use the row shape from `.claude/templates/source.md` or `.claude/templates/repo.md`.
   - Insert in alphabetical order by `id` (keeps diffs reviewable).
   - `added` = today (ISO date).
   - `status` = `active`.

6. **Commit message format.**
   `add(<type>): <title>` — e.g. `add(article): Rethinking MonadError`.

## When this skill rejects

- URL is dead (4xx not 401/403, or DNS/SSL/connection failure).
- ID collision after `-2` discriminator (rare; means three entries with identical slug).
- Required field cannot be derived (e.g., title fetch fails AND user did not provide title manually).

In all rejection cases, surface the reason and stop. Do not insert a partial row.

## Verification checklist

- [ ] New row matches the column order in the existing INDEX file.
- [ ] All required fields are non-empty.
- [ ] `labels` contains at least one domain label from `TAXONOMY/domains.md`.
- [ ] No other row shares the same `id`.
- [ ] `added` is today's date in ISO 8601.

## Related skills

- `dead-link-sweep` — periodic check that catches what add-source missed.
- `star-sweep` — bulk add of newly-starred repos.

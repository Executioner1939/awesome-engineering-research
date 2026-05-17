---
description: Add a new article, video, talk, paper, book, podcast, RFC, course, doc, or repo to the awesome-engineering-research corpus. Validates URL, derives metadata and labels, appends to INDEX/sources.md or INDEX/tools.md.
argument-hint: <url> [type=article|video|...|repo] [labels=label1,label2]
---

# /add-source

Invoke the `add-source` skill at `.claude/skills/add-source/SKILL.md`.

Arguments parsed from `$ARGUMENTS`:
- First positional: URL (required).
- `type=` keyword: entry type. Defaults to `repo` if URL host is github.com; `video` if youtube.com / vimeo.com; `paper` if arxiv.org; otherwise `article`.
- `labels=` keyword: comma-separated additional labels. Optional.
- `notes=` keyword: short freeform note. Optional.

## Procedure

1. Read `.claude/skills/add-source/SKILL.md` for the full procedure.
2. Parse the arguments above.
3. Execute the skill's six steps: validate URL, derive metadata, derive labels, assign id, append row, generate commit message.
4. On success, surface a 3-line summary: id, target file, label set.
5. On failure (dead URL, validation error), surface the reason and stop without inserting a partial row.

---
id: convention-admonitions
title: Admonitions
type: convention
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Admonitions

The GFM callout form is the default — native on GitHub since 2023 and Obsidian. MkDocs Material and Docusaurus render the same content via their admonition extensions.

## Form

```markdown
> [!note]
> Body of the note, can be multiple paragraphs.
>
> Including a second paragraph.
```

## Recognised tags

| tag | meaning |
|---|---|
| `note` | side-information, optional reading |
| `tip` | a non-obvious shortcut or trick |
| `important` | the reader will get the wrong result if they miss this |
| `warning` | doing this has cost — risk, performance, footgun |
| `caution` | doing this is destructive or hard to reverse |

## When to use

Sparingly. A callout is a visual claim that this paragraph matters more than the surrounding prose. If most paragraphs deserve a callout, none of them do.

## When not to use

For ordinary headings, conclusions, or "TL;DR" sections. Use a real heading. Callouts are for in-flow interruption, not for structure.

---
id: taxonomy-source-types
title: Source Types
type: taxonomy
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Source Types

The values `source_type:` draws from on `type: source` docs. The source type informs default confidence and how to interpret claims.

## Canonical sources

| value | default confidence | meaning |
|---|---|---|
| `docs-page` | high | an official documentation page (scraped) |
| `docs-site-index` | high | a navigation / index page from an official docs site |
| `spec` | verified | RFC / W3C / IETF / ECMA / ISO spec |
| `changelog` | high | official changelog / release notes |
| `release-page` | high | GitHub release / equivalent |
| `github-readme` | high | the canonical README of the project's own repo |
| `github-issue` | medium | a project issue thread |
| `github-pr` | medium | a pull-request thread |
| `github-discussion` | medium | a project discussion thread |
| `cargo-doc` | high | docs.rs / cargo doc rendering |
| `npm-readme` | high | npm package README |
| `man-page` | high | system man page / CLI `--help` capture |
| `source-code` | verified | the project's own source code |
| `commit-message` | medium | a commit message |

## Community sources

| value | default confidence | meaning |
|---|---|---|
| `blog-author-canonical` | high | the maintainer's own blog about their own project |
| `blog-third-party` | medium | a third-party explainer / tutorial |
| `forum-reddit` | low | a Reddit thread |
| `forum-hn` | low | a Hacker News thread |
| `forum-stackoverflow` | low | a Stack Overflow answer (treat accepted answers as medium when corroborated) |
| `forum-lobsters` | low | a Lobsters thread |
| `forum-discord` | low | a Discord excerpt (rare; respect channel privacy) |
| `talk-transcript` | medium | a conference talk transcript |
| `paper` | high | an academic paper (claims are claims, not facts) |
| `podcast-transcript` | low | a podcast transcript |

## Generated / derived

| value | default confidence | meaning |
|---|---|---|
| `cli-capture` | verified | the output of a CLI command captured in-session |
| `api-response` | verified | the output of an HTTP / RPC call captured in-session |
| `screen-capture` | medium | an image extract — claim is what the image shows, not what it implies |

## Why default confidence

The default is a starting point; individual extracts inherit confidence from their sources but can raise it (via corroboration across sources) or lower it (when the source is challenged). Confidence is set per-extract, not per-source.

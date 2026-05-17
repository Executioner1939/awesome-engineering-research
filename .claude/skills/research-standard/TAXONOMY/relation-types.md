---
id: taxonomy-relation-types
title: Relation Types
type: taxonomy
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Relation Types

Edges in the knowledge and sitemap graphs are labelled with a `kind:` drawn from this set. Closed set; additions go through a decision record.

## Structural

| kind | from → to | meaning |
|---|---|---|
| `is-a` | concept → concept | subtype relationship |
| `part-of` | concept → concept | composition |
| `instance-of` | entity → concept | this specific thing is an instance of a class |
| `defines` | source → concept | this source authoritatively defines this concept |
| `mentions` | source → concept | this source references this concept without defining it |

## Behavioural

| kind | from → to | meaning |
|---|---|---|
| `uses` | tool → concept | this tool uses this concept internally |
| `implements` | tool → protocol | this tool implements this protocol |
| `exposes` | tool → api | this tool exposes this API entry |
| `calls` | api → api | this API entry calls another |
| `returns` | api → concept | return type |
| `accepts` | api → concept | input type |
| `emits` | api → event | event emitted |
| `triggers` | event → api | trigger relationship |

## Lifecycle

| kind | from → to | meaning |
|---|---|---|
| `supersedes` | doc/api/tool → doc/api/tool | replaces |
| `superseded-by` | doc/api/tool → doc/api/tool | inverse |
| `deprecates` | api → api | marks the target deprecated |
| `migrates-to` | api → api | suggested replacement |
| `forks-from` | tool → tool | code lineage |

## Sitemap-specific

| kind | from → to | meaning |
|---|---|---|
| `links-to` | source → source | outbound hyperlink |
| `redirects-to` | source → source | HTTP redirect |
| `canonical-of` | source → source | canonical-URL relationship |
| `parent-of` | source → source | URL path parent (e.g. /docs/api → /docs/api/foo) |
| `nav-of` | source → source | navigation-menu relationship |

## Provenance

| kind | from → to | meaning |
|---|---|---|
| `extracted-from` | extract → source | this extract was derived from this source |
| `corroborated-by` | extract → source | additional source supporting this extract |
| `contradicts` | extract → extract | the two extracts disagree |

## Synthesis

| kind | from → to | meaning |
|---|---|---|
| `summarises` | synthesis → topic / extract+ | this synthesis distils the targets |
| `compares` | synthesis → tool / concept (multi) | comparison view |
| `walks-through` | synthesis → api / tool / pattern | step-by-step walkthrough |
| `decides` | decision → option (multi) | decision over alternatives |

---
id: taxonomy-concept-types
title: Concept Types
type: taxonomy
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Concept Types

The values that `type:` and `concept_type:` frontmatter keys draw from. Closed set — additions go through a decision record.

## Document type (`type:`)

| value | meaning |
|---|---|
| `topic` | the landing doc of a research topic |
| `source` | captured raw material (scraped page, README, paper, transcript) |
| `extract:concept` | a parsed concept node |
| `extract:api` | a parsed API surface entry |
| `extract:tool` | a parsed tool / library / framework entry |
| `extract:entity` | a parsed external entity (person, org, spec) |
| `graph` | a graph artefact (`.mmd` + `.json` companion) |
| `synthesis` | a derived view — MOC, walkthrough, comparison |
| `decision` | an ADR-style decision record |
| `conclusion` | the final-findings doc for a topic |
| `index` | a linking table |
| `convention` | a CONVENTIONS file |
| `taxonomy` | a TAXONOMY file |
| `pipeline` | a reusable pipeline spec |

## Concept subtype (`concept_type:`)

Applies on `type: extract:concept` docs.

| value | meaning |
|---|---|
| `primitive` | atomic, undecomposable in its domain (e.g. "URL", "merkle root") |
| `pattern` | a recurring shape (e.g. "leader-follower replication") |
| `protocol` | a coordination mechanism (e.g. "two-phase commit", "Raft") |
| `data-shape` | a schema or data structure |
| `algorithm` | a procedure with a name |
| `mechanism` | how something operates internally (e.g. "Tokio scheduler") |
| `convention` | a community-agreed practice |
| `metric` | a measurable quantity (e.g. "p99 latency") |
| `principle` | a normative rule (e.g. "parse, don't validate") |
| `taxonomy-element` | itself a category in some external taxonomy |

## API subtype (`api_kind:`)

Applies on `type: extract:api` docs.

| value | meaning |
|---|---|
| `function` | free-standing function |
| `method` | function bound to a receiver |
| `type` | concrete type definition |
| `trait` | trait / interface / protocol |
| `macro` | macro / template |
| `command` | CLI command |
| `flag` | CLI flag / option |
| `event` | emitted event |
| `schema-field` | configuration / data schema field |
| `endpoint` | HTTP / gRPC / RPC endpoint |
| `module` | namespace / module / package |

---
name: extract-knowledge-graph
description: Parse a captured docs corpus into structured concept, API, tool, and entity extracts with frontmatter, plus relation edges, and emit the knowledge graph in Mermaid and JSON forms. Use after scrape-firecrawl when a topic needs structured semantic extraction beyond the URL link graph.
id: extract-knowledge-graph
title: Extract the knowledge graph
type: pipeline
status: draft
confidence: medium
created: 2026-05-15
updated: 2026-05-17
related: [scrape-firecrawl, sitemap-graph]
---

# Pipeline: Extract Knowledge Graph

Parse the captured markdown corpus into structured nodes (concepts, APIs, tools, entities) and structured edges (relations), then emit the knowledge graph.

This pipeline is `draft` not `stable` because the extraction step itself has design tradeoffs that depend on the corpus shape and the target tool. The procedure below is the agreed default; tool-specific variants live in topic-level decision records.

## Inputs

| name | type | notes |
|---|---|---|
| `topic_id` | slug | the topic whose `20-sources/` to read |
| `sub_corpus` | slug | optional |
| `tool_id` | id | the tool the corpus describes (extracts are scoped to it) |
| `seeded_concepts` | list[id] | optional; concepts known a priori (e.g. from glossary) |
| `repo_clones` | list[path] | optional; cloned repos to read source code from |

## Outputs

Under `topics/<topic_id>/30-extracts/`:

- `concepts/<cpt-id>.md` — one file per concept.
- `apis/<api-id>.md` — one file per API entry.
- `tools/<tool-id>.md` — one file per referenced tool.
- `entities/<ent-id>.md` — one file per external entity.

Under `topics/<topic_id>/40-graphs/`:

- `knowledge.json` — full KG.
- `knowledge.mmd` — Mermaid view (faceted for large graphs).
- `knowledge-by-tool.mmd`, `knowledge-by-concept-type.mmd` — facet views.

## Procedure

### 1. Pass A — Candidate extraction

For each `content.md` in the corpus:

1. Identify candidate concept mentions. Heuristics: section headings, bold-introduced terms, definitional patterns ("X is a Y that ..."), glossary-table rows.
2. Identify candidate API mentions. Heuristics: code-fence languages (`rust`, `ts`, `bash`), function-call patterns, CLI invocations, schema fields in YAML/JSON blocks, headings shaped like signatures.
3. Identify candidate tool mentions. Heuristics: package-manager directives (`cargo add`, `npm install`), tool URLs, branded names matching the tool index.
4. Identify candidate entity mentions. Heuristics: RFC / spec references, person names in author byline, org references.

Output of Pass A is a per-page candidate list, not yet structured.

### 2. Pass B — Canonicalisation

1. Group candidates by canonical name. Aliases collapse into one entry with `aliases: [...]`.
2. Match against the existing concept / API / tool / entity indexes — if a candidate already has an id elsewhere in `Research/`, reuse it.
3. Allocate new ULIDs for unmatched candidates.
4. Write each as a `30-extracts/<kind>/<id>.md` file with frontmatter populated and a body stub.

### 3. Pass C — Relation extraction

For each (source, concept-mention) pair:

1. Emit `extracted-from` from concept to source.
2. If the source's page is the one where the concept is **defined** (heuristic: definitional sentence, "is a" pattern in heading or first paragraph), upgrade to `defines` (source → concept).
3. For API entries, link to their declaring tool with `exposes` (tool → api).
4. For each concept that depends on another concept (heuristic: mentioned within the body of the dependent concept), emit `uses` or `part-of` depending on context.

Relation extraction is the hardest pass. Default to `mentions` when uncertain — it is the weakest, safest edge.

### 4. Pass D — Cargo / repo enrichment

If `repo_clones` is provided:

1. For Rust repos: run `cargo doc --no-deps --document-private-items` and parse the JSON output (`cargo +nightly rustdoc -- --output-format json`). Extract every public item as an `extract:api`. Link items to their module path.
2. For other ecosystems: parse package metadata (`package.json` exports, `pyproject.toml`, etc.) and any generated docs.
3. For poorly-documented surfaces, the repo source IS the source. Mark extracts `confidence: high` (source-code source-type) and cite `path:line`.

### 5. Pass E — Graph emission

1. Build `knowledge.json` from all extracts and relations.
2. Render `knowledge.mmd`. For corpora over ~80 nodes, emit faceted views instead of one mega-graph.
3. Compute analysis metrics: most-referenced concept, most-connected API, isolated concepts (no in-edges — candidates for stub fixup or for "this is mentioned but never defined").

## Verification

- Every extract has `sources:` populated.
- Every API extract has `tool:` populated and the tool id exists in `INDEX/tools.md`.
- The KG has no dangling edges.
- For each `defines` edge, the target concept's `sources:` includes the source on the `from` side of the edge.

## Tool-specific variants

When a tool's surface area has a regular structure (e.g. an OpenAPI spec, a `rustdoc.json`, a structured CLI like `clap`-generated help), prefer the structured form over the prose docs. Tool-specific variants of this pipeline live in `topics/<topic>/60-decisions/`.

## Notes on the inevitable LLM step

Some extraction (especially relation extraction and definition detection) benefits from an LLM pass. The pipeline allows it but constrains it: the LLM is invoked **per page**, produces a structured JSON output, and that JSON is the only thing that lands in the extract files. Prose summaries from an LLM never enter the corpus — only structured nodes and edges, each cited back to the source. This keeps the corpus deterministic and re-derivable.

---
id: convention-frontmatter-schema
title: Frontmatter Schema
type: convention
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-15
---

# Frontmatter Schema

Every markdown file under `Research/` opens with a YAML frontmatter block. The block is fenced by `---` lines and is parsed by every modern static-site generator and most markdown editors.

## Universal keys

These keys apply to every doc, regardless of type.

```yaml
---
id: <string>              # canonical identifier
title: <string>           # human-readable title
type: <enum>              # see TAXONOMY/concept-types.md
status: <enum>            # seed | draft | reviewed | stable | archived | superseded
confidence: <enum>        # low | medium | high | verified (required on claim-bearing docs)
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
tags: [<slug>, ...]       # free-form classification
related: [<id>, ...]      # machine-readable cross-refs (parallel to inline [[id]])
sources: [<src-id>, ...]  # provenance for claims in this doc
supersedes: [<id>, ...]   # docs replaced by this one
superseded_by: [<id>, ...]
---
```

## Type-specific extensions

### `topic`

```yaml
domain: <slug>            # see TAXONOMY/domains.md
questions: [<q-id>, ...]  # questions driving this topic
```

### `source`

```yaml
source_type: <enum>       # see TAXONOMY/source-types.md
url: <url>
retrieved_at: <ISO 8601 datetime>
retriever: <slug>         # e.g. firecrawl-crawl, firecrawl-scrape, git-clone, oracle-canon-reader
content_hash: <sha256>
mime: <string>            # text/markdown, text/html, application/json
crawl_depth: <int>        # for crawled pages
links_out: [<url>, ...]   # outbound links discovered on this page
links_in: [<url>, ...]    # inbound links discovered (filled by sitemap builder)
canonical_url: <url>      # if redirected
capture_kind: <enum>      # excerpt | full-page | derived-summary
authors: [<string>, ...]  # when known (papers, blog posts)
date_published: <YYYY-MM-DD>  # author-attested publication date if visible
grounds: [<term>, ...]    # which terms or concepts this source authoritatively grounds
```

### `extract:concept`

```yaml
concept_type: <enum>      # see TAXONOMY/concept-types.md (entity, pattern, primitive, ...)
canonical_name: <string>
aliases: [<string>, ...]
defines: [<id>, ...]      # other concepts this one defines
depends_on: [<id>, ...]
tool: <id>                # the tool/library this concept lives in
```

### `extract:api`

```yaml
api_kind: <enum>          # function | method | type | trait | macro | command | flag | event | schema-field
canonical_name: <string>
signature: <string>       # raw declaration string
module_path: <string>     # e.g. firecrawl::client::Client::scrape
tool: <id>
version: <semver-range>   # version range in which this signature is current
stability: <enum>         # unstable | experimental | stable | deprecated
inputs: [<param>, ...]    # structured inputs
outputs: [<output>, ...]
errors: [<error>, ...]
references: [<id>, ...]   # other api entries referenced (e.g. return type)
```

### `extract:tool`

```yaml
canonical_name: <string>
homepage: <url>
repository: <url>
license: <SPDX-id>
ecosystem: <slug>         # e.g. cargo, npm, brew
current_version: <semver>
captured_at_version: <semver>
```

### `extract:entity`

```yaml
entity_kind: <enum>       # person | org | spec | rfc | paper | standard
canonical_name: <string>
```

### `graph`

```yaml
graph_kind: <enum>        # sitemap | knowledge | concept | dependency | apicall
node_count: <int>
edge_count: <int>
generated_from: [<id>, ...]   # source docs this graph was built from
generator: <slug>
```

### `synthesis`

```yaml
synthesis_kind: <enum>    # moc | walkthrough | comparison | timeline | summary
covers: [<id>, ...]       # nodes/topics this synthesis covers
```

### `decision`

```yaml
decision_status: <enum>   # proposed | accepted | rejected | superseded
context: <string>
options_considered: [<id>, ...]
chosen: <id>
consequences: [<string>, ...]
```

## Filename derivation

The filename is derived from `id`:

- For ULID-prefixed ids (e.g. `cpt_01HZX…`), the filename is `<id>.md`.
- For slug ids (e.g. `docs-knowledge-graph-pipeline`), the filename is `<id>.md` or the directory name for topic-level docs.
- For lifecycle-ordered docs inside a topic (`00-overview.md`, `10-questions.md`), the filename uses the numeric prefix and the `id` is the slug without the prefix (`overview`, `questions`) namespaced under the topic.

## Validation

A doc is well-formed if:

1. Frontmatter is valid YAML.
2. `id`, `title`, `type`, `status`, `created`, `updated` are present.
3. `type` matches a value in the taxonomy.
4. `status` is a recognised value.
5. Every entry in `related:`, `sources:`, `supersedes:`, `superseded_by:` resolves to an existing `id` in the tree.
6. `confidence` is present when `type` is `extract:*`, `synthesis`, or `conclusion`.

A topic is well-formed if its directory contains `README.md`, `00-overview.md`, `10-questions.md`, and the lifecycle stages it has reached.

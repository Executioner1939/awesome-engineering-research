---
id: taxonomy-domains
title: Subject Domains and Refinement Labels
type: taxonomy
status: stable
confidence: high
created: 2026-05-15
updated: 2026-05-17
---

# Subject Domains and Refinement Labels

The label vocabulary applied to rows in `INDEX/sources.md` and `INDEX/tools.md`. Every row carries at least one **domain** label; rows may additionally carry **refinement** labels for sub-area or technology specificity. New labels are added with an entry in this file and a row update; do not invent labels at the row level.

## Domain labels

A topic or row's coarse subject area. Twelve total.

| domain | scope |
|---|---|
| `developer-tooling` | build systems, monorepo tooling, package managers, version managers, formatters, linters, code-gen |
| `web-extraction` | scraping, crawling, sitemap and link-graph extraction, browser automation |
| `knowledge-systems` | knowledge graphs, ontologies, RAG, retrieval, embeddings, agentic retrieval, semantic search |
| `data-storage` | databases (relational, vector, graph, hybrid), search indexes, message stores, caches |
| `distributed-systems` | consistency, replication, consensus, idempotency, event sourcing, sagas, CRDTs |
| `language-runtimes` | Rust, async runtimes, JVM, Node, Bun, Deno, GC, compilers, type systems |
| `observability` | metrics, traces, structured logs, profiling, debugging, tracing infrastructure |
| `ai-applications` | LLM application architecture, prompt engineering, agent frameworks, evals, tool-use |
| `frontend` | UI frameworks, component systems, accessibility, design systems, web performance |
| `infrastructure` | container orchestration, IaC, CI/CD, deployment topologies, Kubernetes, service mesh |
| `security` | authn, authz, secrets, supply-chain, code-signing, cryptography, vuln-scanning |
| `standards` | RFCs, specs, ISO / W3C / IETF / ECMA documents, interop conventions |

## Refinement labels

Sub-area or technology specificity. May appear alongside any domain label. Grouped by family for readability — the labels themselves are flat in row data.

### Language / runtime
`rust`, `scala`, `go`, `python`, `typescript`, `javascript`, `java`, `kotlin`, `c`, `cpp`, `elixir`, `ocaml`, `shell`

### Functional-programming heritage
`fp-scala`, `fp-rust`, `typelevel`, `cats-effect`, `zio`, `scalaz`, `algebraic-effects`, `tagless-final`

### Concurrency / async
`concurrency`, `async-runtimes`, `tokio`, `loom`, `actor-model`

### Distributed-systems patterns
`event-sourcing`, `cqrs`, `sagas`, `consensus`, `replication`, `idempotency`, `cap-theorem`, `microservices`, `architecture-ddd`, `service-mesh`

### Data plane
`databases`, `kafka`, `rabbitmq`, `nats`, `postgres`, `vector-db`, `graph-db`, `time-series`, `kv-store`, `search`

### Infrastructure / DevOps
`kubernetes`, `terraform`, `iac`, `argocd`, `helm`, `ci-cd`, `docker`, `bazel`, `moonrepo`

### Observability detail
`tracing`, `metrics`, `profiling`, `logging`, `opentelemetry`

### AI / LLM
`llm`, `agents`, `rag`, `embeddings`, `mcp`, `tool-use`, `eval`

### Compilers / parsing / lang implementation
`compilers`, `parsers`, `static-analysis`, `serialization`, `kernel-systems`

### Web / frontend specifics
`web-perf`, `dom`, `wasm`

### Other
`cli-tooling`, `error-handling`, `interviewing`, `algorithms`

## Curation gaps

These labels are placeholders flagged for cleanup. The `add-source` skill should refuse to apply them on new entries.

| label | meaning | action |
|---|---|---|
| `misc` | parser failed to derive a label from URL host + title heuristics. 81 source rows currently carry this label. | Each `misc`-only row should be hand-reviewed and re-labelled; once cleared, this label is removed from the taxonomy. |

## Adding a new label

1. Add the row to the appropriate group above.
2. Update `.claude/skills/research-standard/TAXONOMY/domains.md` (this file).
3. If the label is a domain (not a refinement), add a one-paragraph note to `.claude/skills/add-source/SKILL.md` describing when to apply it.
4. Commit with message `taxonomy: add <label>` and a short reason.

## How rows pick labels

- **Sources** (articles, videos, papers, ...): heuristic from URL host + title keywords, plus user-supplied labels via `add-source`.
- **Tools** (repos): GitHub `topics` array first; fall back to keyword matching on description + language. `add-source` and `star-sweep` both apply this rule.
- **All rows** must carry at least one domain label. Refinement labels are optional but encouraged.
- Labels in a row are sorted alphabetically, comma-separated, lowercase.

---
id: taxonomy-categories
title: Fine-grained Categories
type: taxonomy
status: stable
confidence: high
created: 2026-05-18
updated: 2026-05-18
---

# Fine-grained Categories

The primary grouping vocabulary for rows in `INDEX/sources.md` and `INDEX/tools.md`. Each row carries exactly one `category:` value from the table below. Categories replace the 12 coarse `domain:` labels from [domains.md](./domains.md), which now serve only as readability groupings here — they are not stored in rows.

The README is rendered with one `## <category>` heading per non-empty category. Under each, sub-headings:

- **Tools** — repos where `kind = tool` (standalone server, daemon, CLI application)
- **Libraries** — repos where `kind = library` (embedded dependency)
- **Frameworks** — repos where `kind = framework` (opinionated structuring dependency)
- **Unsorted** — repos where `kind = unsorted` (heuristic was not confident; awaits `/sort-unsorted`)
- **Articles** — sources where `type = article`
- **Videos** — sources where `type = video`

Empty sub-headings are dropped. Empty categories are dropped.

## Data plane

| category | scope |
|---|---|
| `relational-databases` | Postgres, MySQL, CockroachDB, distributed SQL engines |
| `columnar-databases` | ClickHouse, DuckDB, Apache Druid, analytical warehouses |
| `time-series-databases` | InfluxDB, TimescaleDB, QuestDB, VictoriaMetrics |
| `vector-databases` | Qdrant, Weaviate, Chroma, Milvus, pgvector |
| `graph-databases` | Neo4j, Memgraph, FalkorDB, KuzuDB, SurrealDB (graph mode) |
| `document-databases` | MongoDB, CouchDB, Couchbase |
| `wide-column-databases` | Cassandra, ScyllaDB, HBase |
| `kv-stores` | Redis, etcd, FoundationDB, BadgerDB, RocksDB |
| `caches` | Memcached, Caffeine, Moka, in-process caches |
| `embedded-databases` | SQLite, DuckDB-embedded, LMDB, sled |
| `search-engines` | Elasticsearch, OpenSearch, Meilisearch, Typesense, Tantivy |
| `object-stores` | MinIO, Ceph, SeaweedFS, S3-compatible servers |
| `message-queues` | Kafka, RabbitMQ, NATS, Redpanda, Pulsar |
| `stream-processing` | Flink, Materialize, RisingWave, Bytewax |
| `multi-model-databases` | SurrealDB, FaunaDB, ArangoDB |

## Language & runtime

| category | scope |
|---|---|
| `async-runtimes` | Tokio, async-std, smol, Embassy, Java loom |
| `effect-systems` | cats-effect, ZIO, Kyo, Eff, fs2 |
| `compilers` | Compiler frontends, IRs, JITs |
| `parsers` | Combinator libs, generators (nom, chumsky, pest, ANTLR) |
| `static-analyzers` | rust-analyzer, clippy, ESLint plugins, Semgrep |
| `type-checkers` | mypy, pyright, ts-toolbelt |
| `garbage-collectors` | GC research, ZGC, Shenandoah, ZGC papers |

## Distributed systems

| category | scope |
|---|---|
| `consensus` | Raft, Paxos, etcd-raft, openraft |
| `event-sourcing` | Event-store implementations, EventStoreDB, KurrentDB |
| `cqrs` | CQRS framework libs |
| `workflow-engines` | Temporal, Cadence, Restate, AWS Step Functions clones |
| `service-meshes` | Istio, Linkerd, Cilium service mesh, Envoy proxy |
| `api-gateways` | Kong, Tyk, KrakenD, Traefik (gateway mode) |
| `rpc-frameworks` | gRPC, Twirp, tonic, Tarpc, Cap'n Proto |
| `service-discovery` | Consul, Eureka, Nacos, mDNS |

## Observability

| category | scope |
|---|---|
| `distributed-tracing` | Jaeger, Tempo, Zipkin, OpenTelemetry collectors |
| `metrics` | Prometheus, VictoriaMetrics (metrics), StatsD, Mimir |
| `logging` | Loki, ELK, Vector, Fluent Bit, structured-logging libs |
| `profiling` | Pyroscope, Parca, perf-tools, flamegraph |
| `continuous-profiling` | Profiling-as-a-service stacks |
| `apm` | Datadog, New Relic open-core, Glitchtip |
| `opentelemetry-libs` | OTel SDKs, instrumentation libraries |

## AI / LLM

| category | scope |
|---|---|
| `agent-frameworks` | LangGraph, AutoGen, CrewAI, smolagents, Agno |
| `llm-app-frameworks` | LangChain, LlamaIndex, Haystack, Semantic Kernel |
| `rag-retrieval` | RAG-specific libs, GraphRAG, HippoRAG, LightRAG |
| `embeddings` | Sentence-transformers, embedding model wrappers |
| `model-serving` | vLLM, TGI, Ollama, llama.cpp, sglang |
| `mcp-tooling` | MCP servers, MCP SDKs, MCP gateways |
| `llm-evaluation` | Inspect, DeepEval, promptfoo, ragas |
| `prompt-engineering` | Prompt libraries, prompt-as-code |
| `llm-clients-sdks` | Provider SDKs, unified clients |

## Infrastructure

| category | scope |
|---|---|
| `container-orchestration` | Kubernetes, Nomad, ECS clones |
| `iac` | Terraform, OpenTofu, Pulumi, Crossplane |
| `gitops` | ArgoCD, Flux, Image Updater |
| `build-systems` | Bazel, Buck, Pants, Earthly |
| `monorepo-tooling` | Moon, Nx, Turborepo, Lerna, Yarn workspaces |
| `container-runtimes` | containerd, runc, gVisor, Firecracker |
| `package-registries` | Verdaccio, Sonatype Nexus, Harbor |

## Security

| category | scope |
|---|---|
| `authentication` | Keycloak, Authelia, OIDC providers, WebAuthn libs |
| `authorization-policy` | OPA, Cedar, Casbin, RBAC libs, Oso |
| `secrets-management` | Vault, sops, age, SealedSecrets, Infisical |
| `supply-chain-security` | sigstore, cosign, syft, grype, OSV-scanner |
| `code-signing` | sigstore, gpg-tooling, notary |
| `vulnerability-scanning` | Trivy, Grype, Snyk OSS, Aikido |
| `cryptography-libs` | ring, age, rage, libsodium bindings, RustCrypto |
| `network-security` | WireGuard, mTLS tooling, Tailscale, Headscale |

## Developer experience

| category | scope |
|---|---|
| `cli-frameworks` | clap, cobra, oclif, click |
| `code-editors` | Zed, Helix, Lapce, Atom forks |
| `linters-formatters` | rustfmt, Prettier, Biome, dprint, ruff |
| `code-review-automation` | CodeRabbit, Reviewdog, danger-js |
| `documentation-generators` | mdBook, Docusaurus, MkDocs Material, Astro Starlight |
| `shells-terminals` | Nushell, Fish, Wezterm, Alacritty, Ghostty |
| `dotfiles` | Dotfile managers, chezmoi, stow |

## Functional programming

| category | scope |
|---|---|
| `algebraic-effects` | Effect systems implementations, Eff, Koka |
| `optics-lenses` | Monocle, fp-ts optics, accessors |
| `streaming-libs` | fs2, ZIO Streams, Akka Streams, fluvio |
| `property-based-testing` | ScalaCheck, proptest, Hypothesis, fast-check |
| `type-classes-prelude` | Cats, Scalaz, fp-ts, Effect-ts |

## Frontend & web

| category | scope |
|---|---|
| `ui-frameworks` | React, Vue, Svelte, Solid, Qwik, HTMX |
| `component-systems` | shadcn/ui, Radix, MUI, Chakra |
| `design-systems` | Token-based design systems, Theo, Style Dictionary |
| `web-performance` | Lighthouse, web-vitals, partial hydration libs |
| `wasm` | WASM toolchains, wasmtime, wasmer, JCO |
| `bundlers` | esbuild, Vite, Rollup, Turbopack, Rspack |
| `css-tooling` | Tailwind, PostCSS, UnoCSS, vanilla-extract |

## Standards & specs

| category | scope |
|---|---|
| `rfcs` | IETF RFCs, drafts |
| `w3c-specs` | DOM, CSS, WebAuthn, design-tokens |
| `oauth-oidc` | OAuth 2.0/2.1, OIDC, PKCE, DPoP |
| `web-platform-specs` | Fetch, Streams, Service Workers |
| `cryptographic-standards` | NIST, FIPS, PKCS, IETF crypto |

## Knowledge & curation

| category | scope |
|---|---|
| `awesome-lists` | Curated awesome-* repos |
| `knowledge-graphs` | KG implementations, ontology tooling |
| `learning-resources` | "build your own", system design primers, paper collections |
| `interview-prep` | Interview question collections, behavioural prep |

## Triage

| category | scope |
|---|---|
| `unsorted` | The classifying agent could not place this row with confidence. Awaits `/sort-unsorted` or manual reclassification. |

## Kind discriminator (repos only)

`INDEX/tools.md` carries a `kind:` column.

| kind | meaning | example signals |
|---|---|---|
| `tool` | Standalone application, daemon, server, or CLI you run | topics `cli`, `daemon`, `application`; description verbs "runs", "serves" |
| `library` | Embedded dependency consumed by your code | topics `library`, `crate`, `sdk`; description nouns "client", "binding" |
| `framework` | Opinionated structuring dependency | topics `framework`, `web-framework`; description "build X with", "opinionated" |
| `unsorted` | Heuristic was not confident | default when no clear signal |

The heuristic is intentionally conservative — when in doubt, `unsorted`. The `/sort-unsorted` skill is the cleanup path.

## Adding a category

1. Add the row to the appropriate group above.
2. Open a PR with a one-line rationale in the body.
3. The first row added under the new category should ideally be in the same PR.

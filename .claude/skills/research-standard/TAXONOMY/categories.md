---
id: taxonomy-categories
title: Fine-grained Categories
type: taxonomy
status: stable
confidence: high
created: 2026-05-18
updated: 2026-09-22
---

# Fine-grained Categories

The primary grouping vocabulary for rows in `INDEX/sources.md` and `INDEX/tools.md`. Each row carries exactly one `category:` value from the table below. Categories replace the 12 coarse `domain:` labels from [domains.md](./domains.md), which now serve only as readability groupings here — they are not stored in rows.

The README is rendered with one `## <category>` heading per non-empty category. Under each, sub-headings:

- **Tools** — repos where `kind = tool` (standalone server, daemon, CLI application)
- **Libraries** — repos where `kind = library` (embedded dependency)
- **Frameworks** — repos where `kind = framework` (opinionated structuring dependency)
- **Reading & references** — repos where `kind = content` (lists, courses, specs; nothing to run or import)
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
| `graph-processing` | Distributed graph compute engines: GraphScope, Apache GeaFlow, Giraph, GraphX, Pregel-style systems |
| `realtime-messaging` | Client-facing push and delivery: Centrifugo, Novu, Soketi, WebSocket/SSE fan-out and notification servers |
| `database-migrations` | Schema and data migration runners and their tooling: Flyway, Liquibase, Atlas, golang-migrate, grate |

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
| `state-machines` | Statechart and finite-state-machine libraries: XState, Stately, Spring Statemachine, statig, rust-fsm |
| `concurrency-primitives` | Non-async parallelism and shared-memory building blocks: Rayon, Crossbeam, parking_lot, papaya, lock-free collections |
| `serialization-formats` | Encoding, codec and cross-language data-exchange libraries: Fory, Protobuf, MessagePack, upickle, scodec |
| `data-structures` | General-purpose containers and algorithmic data structures: petgraph, fst, rtree2d, bumpalo, immutable collections |
| `date-time-libraries` | Date, time, calendar and duration handling: chrono, time-rs, ThreeTen, biweekly, tz database wrappers |
| `macros-codegen` | Macro systems and compile-time code generation for user types: derive_more, derive_builder, nutype, syn/quote, proc-macro helpers |
| `schema-validation` | Runtime validation of data against a schema or invariant set: JSON Schema validators, Zod, Pydantic, Valibot, Cerberus |
| `process-management` | Spawning, piping and supervising child processes from code: duct, xshell, commons-exec, subprocess wrappers, process supervisors |
| `rules-engines` | Business-rule and decision-table evaluation: Drools, Camunda DMN, json-rules-engine, Clara, decisions4s |
| `file-formats` | Detecting, identifying and handling file formats and their metadata: Apache Tika, simplemagic, infer, tree_magic, EXIF and container readers |

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
| `distributed-runtimes` | Sidecar and platform runtimes for building distributed applications: Dapr, Akka, Orleans, Service Weaver, Cloudstate |
| `identifier-generation` | Coordination-free unique ID generators and their implementations: KSUID, ULID, cuid, nanoid, Snowflake-style IDs |
| `resilience-patterns` | Circuit breakers, bulkheads, retries, timeouts and rate limiters for fault-tolerant clients: resilience4j, Polly, failsafe, rezilience, backoff |
| `job-scheduling` | Background job and recurring-task schedulers: Quartz, JobRunr, APScheduler, River, tokio-cron-scheduler |

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
| `incident-response` | On-call, alerting and runbook automation for operating services: PlayBooks, Grafana OnCall, Keep, Dispatch, alert enrichment and incident workflow tooling |

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
| `coding-agents` | Coding agent harnesses and CLIs: Claude Code-style TUIs, Aider, Claudable, grok-build, account/session tooling |
| `agent-skills` | Skill, command and plugin packs for agent harnesses: anthropics/skills, wshobson/agents, harness skill graphs |
| `llm-interfaces` | Chat and generative-UI front ends: Open WebUI, assistant-ui, LibreChat, tool-call rendering components |
| `agent-memory` | Persistent memory layers for agents: Hindsight, Memori, Mem0, Zep, Letta, long-term conversation and execution state |
| `design-agents` | Prompt-to-design agents that generate UI mockups, prototypes and decks: Superdesign, open-codesign, v0-style generators |

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
| `ci-cd` | Pipeline runners and CI tooling: act, Dagger, Woodpecker, Earthly CI, build caches for CI |
| `feature-flags` | Feature flag, remote config and experimentation platforms: Unleash, Flagsmith, GrowthBook, Flipt, OpenFeature |
| `cloud-cost-management` | FinOps and cost attribution for cloud and Kubernetes spend: Infracost, OpenCost, Kubecost, cloud budget and chargeback tooling |
| `container-management` | Day-to-day container and cluster management UIs and TUIs: lazydocker, k9s, Portainer, Lens, ctop |
| `code-sandboxes` | Isolated execution of untrusted code: Piston, E2B, Judge0, microsandbox, gVisor-backed runners |
| `chaos-engineering` | Fault injection and resilience testing against running systems: chaoskube, Chaos Mesh, LitmusChaos, Toxiproxy, Pumba |
| `cloud-sdks` | Provider client libraries and API bindings for cloud platforms: google-cloud-java, AWS SDK, Azure SDK, cloud storage and gateway clients |
| `backup-recovery` | Scheduled backup, snapshot and restore automation for stateful systems: Velero, gemini, restic, Kanister, VolumeSnapshot operators |

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
| `osint-reconnaissance` | Open-source intelligence and recon: SpiderFoot, maigret, subfinder, gau, dark-web and threat-intel collections |
| `offensive-security` | Pentest and red-team toolkits and payload corpora: SecLists, wordlists, Flipper Zero payloads, AI pentesting agents |
| `privacy-tooling` | PII redaction, anonymisation, browser-fingerprinting research, telemetry removal: Presidio, FingerprintJS, CreepJS |
| `runtime-security` | Kernel and runtime threat detection and enforcement: Tetragon, Falco, Tracee, eBPF security observability |
| `decentralized-identity` | Verifiable credentials, DIDs and self-sovereign identity toolkits: AnonCreds, ACA-Py, Credo-TS, walt.id, Hyperledger Indy tooling |
| `compliance-auditing` | Compliance-as-code and benchmark auditing: InSpec, OpenSCAP, CIS benchmark profiles, control evidence collection |

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
| `diagramming` | D2, Mermaid, Graphviz, Excalidraw, node-based diagram and flow UI libraries |
| `spec-driven-development` | Spec-first workflows for coding agents: GitHub spec-kit, OpenSpec, Spec Kitty, PRD-to-task pipelines |
| `dev-environments` | Local-to-cluster and reproducible development environments: mirrord, DevSpace, Telepresence, Tilt, devcontainers |
| `notebooks` | Computational notebook environments and kernels: Polynote, Jupyter, Marimo, Zeppelin, nbdev |
| `testing-frameworks` | Test runners, fixtures, harnesses and assertion libraries: rstest, pytest, JUnit, Testcontainers, contract-testing tools |
| `tui-libraries` | Terminal UI rendering primitives for building console interfaces: Ratatui, comfy-table, indicatif, kdam, AppCUI |
| `dependency-management` | Dependency update, version-bump and lockfile tooling: Renovate, Dependabot, cargo-outdated, cargo-edit, npm-check-updates |
| `release-automation` | Versioning, changelog generation and artifact publishing: semantic-release, release-please, auto-changelog, git-cliff, sbt-sonatype |

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
| `data-visualization` | Vega, D3, visx, deck.gl, Observable Plot, charting grammars |
| `graphics-3d` | three.js helpers, react-three-fiber/drei, glam, 3D asset collections and graphics math |
| `animation-libraries` | GSAP, Motion, anime.js, Lottie, scroll and timeline animation |

## Standards & specs

| category | scope |
|---|---|
| `rfcs` | IETF RFCs, drafts |
| `w3c-specs` | DOM, CSS, WebAuthn, design-tokens |
| `oauth-oidc` | OAuth 2.0/2.1, OIDC, PKCE, DPoP |
| `web-platform-specs` | Fetch, Streams, Service Workers |
| `cryptographic-standards` | NIST, FIPS, PKCS, IETF crypto |
| `interop-specs` | Community wire-format, identifier and protocol specs outside the RFC/W3C tracks: CloudEvents, AsyncAPI, ULID, CUID, Standard Webhooks |

## Knowledge & curation

| category | scope |
|---|---|
| `awesome-lists` | Curated awesome-* repos |
| `knowledge-graphs` | KG implementations, ontology tooling |
| `learning-resources` | "build your own", system design primers, paper collections |
| `interview-prep` | Interview question collections, behavioural prep |
| `investigative-data` | Open investigative datasets and platforms: OpenSanctions, OpenAleph, FollowTheMoney, EveryPolitician |

## Machine learning

| category | scope |
|---|---|
| `computer-vision` | Ultralytics YOLO, anomalib, object detection and segmentation stacks, 3D world models |
| `information-extraction` | GLiNER, spaCy pipelines, NER and schema-based structured extraction from text |
| `model-optimization` | Quantization, pruning, abliteration, low-memory inference: AirLLM, llm-compressor, heretic |

## Web extraction

| category | scope |
|---|---|
| `web-crawlers` | Crawlee, Scrapy, spider-rs, Firecrawl, crawl orchestration and fetch pipelines |
| `browser-automation` | Playwright/Puppeteer drivers, headless and anti-detect browsers, FlareSolverr, browser-use |
| `content-extraction` | trafilatura, newspaper3k, extruct, readability ports, boilerplate and metadata extraction |
| `document-extraction` | olmOCR, Chunkr, Docling, PDF/Office-to-text conversion for LLM and RAG pipelines |

## Geospatial

| category | scope |
|---|---|
| `routing-engines` | OSRM, Valhalla, GraphHopper, OpenTripPlanner |
| `geospatial-processing` | Apache Sedona, H3, GDAL, remote-sensing and spatial-analysis pipelines |
| `photogrammetry` | OpenDroneMap, WebODM, OpenSfM, COLMAP, Gaussian-splatting reconstruction pipelines |
| `mapping-libraries` | MapLibre, Leaflet, CesiumJS, OpenStreetMap tooling and resource collections |

## Embedded & radio

| category | scope |
|---|---|
| `embedded-firmware` | Meshtastic, openLRSng, ArduPilot, PX4, ESP32/STM32 device firmware |
| `radio-sdr` | SDR and RF tooling: ADS-B and AIS receivers, LoRa, SAR, WiFi sensing, SIM/cellular tooling |
| `uav-drones` | Drone flight stacks, FPV hardware, swarm coordination, UAV resource collections |
| `hardware-interfaces` | Host-side access to devices and peripherals: jSerialComm, serialport-rs, libusb and hidapi bindings, GPIO and I2C libraries |
| `iot-platforms` | Servers and clients for IoT device telemetry and sensor-data APIs: FROST-Server, OGC SensorThings implementations, ThingsBoard, Eclipse Ditto |

## Networking

| category | scope |
|---|---|
| `http-clients` | curl, reqwest, hyper, httpx, undici |
| `network-monitoring` | Sniffnet, ntopng, Wireshark tooling, packet capture and flow analysis |
| `network-protocols` | Low-level packet, socket and protocol implementation libraries: libpnet, smoltcp, quinn, ip4s, etherparse |
| `http-servers` | Server-side HTTP frameworks, routing DSLs and middleware: Akka HTTP, tower-http, Axum, Actix Web, CORS and compression directives |

## Applications & platforms

| category | scope |
|---|---|
| `content-management` | Directus, Strapi, Pimcore, Payload, headless CMS and PIM platforms |
| `payments` | Hyperswitch, Kill Bill, Lago, payment orchestration, billing and ledger platforms |
| `media-processing` | FFmpeg pipelines, image/video transcoding, streaming servers, transcription, image rendering services |
| `data-wrangling` | OpenRefine, data cleaning, reconciliation and messy-data transformation |
| `entity-resolution` | Nomenklatura, Splink, Zingg, record linkage and deduplication |
| `e-commerce` | Headless commerce backends and storefront platforms: Medusa, Saleor, Vendure, Spree, Sylius |
| `business-intelligence` | Semantic layers and analytics front ends: Cube, Metabase, Superset, Lightdash, metric-layer and embedded-analytics servers |
| `email-tooling` | Email templating, rendering and delivery: MJML, Maizzle, react-email, Postal, transactional mail libraries |
| `blockchain-tooling` | Wallet cores, chain clients, indexers and on-chain bot frameworks: wallet-core, Artemis, Rabby, Solana indexers |
| `low-code-platforms` | Config-driven internal-tool and admin-panel builders: Lowdefy, Appsmith, Budibase, ToolJet |
| `healthcare-platforms` | Health-data interoperability and clinical application platforms: Medplum, HAPI FHIR, OpenEMR, FHIR and HL7 servers and SDKs |
| `market-data` | Financial market data access, aggregation and trading infrastructure: borsa, OpenBB, ccxt, QuantLib, exchange and ticker SDKs |

## Scientific computing

| category | scope |
|---|---|
| `scientific-computing` | Symbolic mathematics, numerics and optimisation: Symbolica, SymPy, arbitrary-precision decimals, metaheuristic and solver libraries |
| `units-measures` | Physical quantities, units of measure and dimensional analysis: squants, coulomb, JSR-354 Moneta, alchemist, uom |
| `bioinformatics` | Biological and chemical data processing: BioJava, Biopython, htsjdk, sequence alignment, genomics and protein-structure toolkits |

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
| `content` | Reading material rather than software: awesome lists, courses, books, paper collections, specs, roadmaps | topics `awesome`, `awesome-list`, `learning`, `roadmap`; no build system, mostly markdown |
| `unsorted` | Heuristic was not confident | default when no clear signal |

The heuristic is intentionally conservative — when in doubt, `unsorted`. The `/sort-unsorted` skill is the cleanup path.

## Adding a category

1. Add the row to the appropriate group above.
2. Open a PR with a one-line rationale in the body.
3. The first row added under the new category should ideally be in the same PR.

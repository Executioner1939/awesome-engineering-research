# awesome-engineering-research

A curated and machine-maintained reading + tools corpus covering distributed systems, language runtimes, functional programming, observability, infrastructure, AI applications, and adjacent areas. Sources and starred repos are deduplicated, labelled against a fixed taxonomy, periodically re-validated for liveness, and rendered to this README from `INDEX/`.

<!-- BEGIN: badges -->
![link-check](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/link-check.yml/badge.svg) ![star-sweep](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/star-sweep.yml/badge.svg) ![lint](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/frontmatter-lint.yml/badge.svg)
<!-- END: badges -->

## Stats

<!-- BEGIN: stats -->
- **Sources:** 294 active, 44 archived
- **Repos:** 614 active, 65 archived
- **Last regenerated:** 2026-09-18
<!-- END: stats -->

---

## Table of contents

<!-- BEGIN: toc -->

**Data plane**

- [Relational Databases](#relational-databases)
- [Columnar Databases](#columnar-databases)
- [Time Series Databases](#time-series-databases)
- [Vector Databases](#vector-databases)
- [Graph Databases](#graph-databases)
- [Document Databases](#document-databases)
- [KV Stores](#kv-stores)
- [Caches](#caches)
- [Search Engines](#search-engines)
- [Object Stores](#object-stores)
- [Message Queues](#message-queues)
- [Stream Processing](#stream-processing)
- [Graph Processing](#graph-processing)
- [Realtime Messaging](#realtime-messaging)

**Language & runtime**

- [Async Runtimes](#async-runtimes)
- [Effect Systems](#effect-systems)
- [Compilers](#compilers)
- [Parsers](#parsers)
- [Static Analyzers](#static-analyzers)
- [Type Checkers](#type-checkers)
- [Garbage Collectors](#garbage-collectors)
- [State Machines](#state-machines)
- [Concurrency Primitives](#concurrency-primitives)
- [Serialization Formats](#serialization-formats)
- [Data Structures](#data-structures)
- [Date Time Libraries](#date-time-libraries)

**Distributed systems**

- [Consensus](#consensus)
- [Event Sourcing](#event-sourcing)
- [Workflow Engines](#workflow-engines)
- [Service Meshes](#service-meshes)
- [Api Gateways](#api-gateways)
- [RPC Frameworks](#rpc-frameworks)
- [Service Discovery](#service-discovery)
- [Distributed Runtimes](#distributed-runtimes)
- [Identifier Generation](#identifier-generation)

**Observability**

- [Distributed Tracing](#distributed-tracing)
- [Metrics](#metrics)
- [Logging](#logging)
- [APM](#apm)

**AI / LLM**

- [Agent Frameworks](#agent-frameworks)
- [LLM App Frameworks](#llm-app-frameworks)
- [RAG Retrieval](#rag-retrieval)
- [Model Serving](#model-serving)
- [MCP Tooling](#mcp-tooling)
- [LLM Evaluation](#llm-evaluation)
- [Prompt Engineering](#prompt-engineering)
- [Coding Agents](#coding-agents)
- [Agent Skills](#agent-skills)
- [LLM Interfaces](#llm-interfaces)
- [Agent Memory](#agent-memory)
- [Design Agents](#design-agents)

**Infrastructure**

- [Container Orchestration](#container-orchestration)
- [IaC](#iac)
- [Gitops](#gitops)
- [Build Systems](#build-systems)
- [Monorepo Tooling](#monorepo-tooling)
- [Container Runtimes](#container-runtimes)
- [Package Registries](#package-registries)
- [CI CD](#ci-cd)
- [Feature Flags](#feature-flags)
- [Cloud Cost Management](#cloud-cost-management)
- [Container Management](#container-management)
- [Code Sandboxes](#code-sandboxes)

**Security**

- [Authentication](#authentication)
- [Authorization Policy](#authorization-policy)
- [Supply Chain Security](#supply-chain-security)
- [Vulnerability Scanning](#vulnerability-scanning)
- [Cryptography Libs](#cryptography-libs)
- [Network Security](#network-security)
- [Osint Reconnaissance](#osint-reconnaissance)
- [Offensive Security](#offensive-security)
- [Privacy Tooling](#privacy-tooling)
- [Runtime Security](#runtime-security)
- [Compliance Auditing](#compliance-auditing)

**Developer experience**

- [CLI Frameworks](#cli-frameworks)
- [Code Editors](#code-editors)
- [Linters Formatters](#linters-formatters)
- [Code Review Automation](#code-review-automation)
- [Documentation Generators](#documentation-generators)
- [Shells Terminals](#shells-terminals)
- [Diagramming](#diagramming)
- [Spec Driven Development](#spec-driven-development)
- [Dev Environments](#dev-environments)
- [Notebooks](#notebooks)

**Functional programming**

- [Optics Lenses](#optics-lenses)
- [Streaming Libs](#streaming-libs)
- [Type Classes Prelude](#type-classes-prelude)

**Frontend & web**

- [UI Frameworks](#ui-frameworks)
- [Component Systems](#component-systems)
- [Design Systems](#design-systems)
- [Data Visualization](#data-visualization)
- [Graphics 3d](#graphics-3d)
- [Animation Libraries](#animation-libraries)

**Standards & specs**

- [RFCs](#rfcs)
- [OAuth OIDC](#oauth-oidc)
- [Cryptographic Standards](#cryptographic-standards)
- [Interop Specs](#interop-specs)

**Knowledge & curation**

- [Awesome Lists](#awesome-lists)
- [Knowledge Graphs](#knowledge-graphs)
- [Learning Resources](#learning-resources)
- [Interview Prep](#interview-prep)
- [Investigative Data](#investigative-data)

**Machine learning**

- [Computer Vision](#computer-vision)
- [Information Extraction](#information-extraction)
- [Model Optimization](#model-optimization)

**Web extraction**

- [Web Crawlers](#web-crawlers)
- [Browser Automation](#browser-automation)
- [Content Extraction](#content-extraction)
- [Document Extraction](#document-extraction)

**Geospatial**

- [Routing Engines](#routing-engines)
- [Geospatial Processing](#geospatial-processing)
- [Photogrammetry](#photogrammetry)
- [Mapping Libraries](#mapping-libraries)

**Embedded & radio**

- [Embedded Firmware](#embedded-firmware)
- [Radio Sdr](#radio-sdr)
- [Uav Drones](#uav-drones)

**Networking**

- [Http Clients](#http-clients)
- [Network Monitoring](#network-monitoring)

**Applications & platforms**

- [Content Management](#content-management)
- [Payments](#payments)
- [Media Processing](#media-processing)
- [Data Wrangling](#data-wrangling)
- [Entity Resolution](#entity-resolution)
- [E Commerce](#e-commerce)
- [Business Intelligence](#business-intelligence)
- [Email Tooling](#email-tooling)
- [Blockchain Tooling](#blockchain-tooling)
- [Low Code Platforms](#low-code-platforms)

**Triage**

- [Unsorted](#unsorted)
<!-- END: toc -->

- [Triage queue](#triage-queue)
- [Archived](#archived)
- [License](#license)

---

## Categories

<!-- BEGIN: categories -->
<a id="relational-databases"></a>

---

## Relational Databases

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [PeerDB-io/peerdb](https://github.com/PeerDB-io/peerdb) | Go | 3273 | 2026-09-18 | Fast, Simple and a cost effective tool to replicate data from Postgres to Data Warehouses, Queues and Storage |
| [GoogleCloudPlatform/cloudsql-upgrade](https://github.com/GoogleCloudPlatform/cloudsql-upgrade) | — | 7 | 2025-07-14 | The tool simplifies upgrading your Cloud SQL databases to newer major versions (MySQL 5.7 to 8.0 and PostgreSQL 9.6/10/1 |

#### Libraries (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [diesel-rs/diesel](https://github.com/diesel-rs/diesel) | Rust | 14177 | 2026-09-18 | A safe, extensible ORM and Query Builder for Rust |
| [apache/datafusion](https://github.com/apache/datafusion) | Rust | 9323 | 2026-09-18 | Apache DataFusion SQL Query Engine |
| [JetBrains/Exposed](https://github.com/JetBrains/Exposed) | Kotlin | 9287 | 2026-09-18 | Kotlin SQL Framework |
| [diesel-rs/diesel_async](https://github.com/diesel-rs/diesel_async) | Rust | 826 | 2026-09-18 | Diesel async connection implementation |

#### Unsorted (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [hit-box/hitbox](https://github.com/hit-box/hitbox) | Rust | 146 | 2026-06-01 | Async caching framework for Rust with Tower middleware, stale-while-revalidate, dogpile prevention, and pluggable backen |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Bye bye Mongo, Hello Postgres](https://www.theguardian.com/info/2018/nov/30/bye-bye-mongo-hello-postgres) | article | 2019-01 | data-storage, databases, misc |
| [At 22 years old, Postgres might just be the most advanced database yet](https://arcentry.com/blog/postgres-might-just-be-the-most-advanced-database-ever/#) | article | 2018-12 | data-storage, databases |


<a id="columnar-databases"></a>

---

## Columnar Databases

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | C++ | 49960 | 2026-09-18 | ClickHouse® is a real-time analytics database management system |
| [ClickHouse/clickhouse-operator](https://github.com/ClickHouse/clickhouse-operator) | Go | 293 | 2026-09-15 | Official Kubernetes Operator for ClickHouse® |

#### Libraries (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [pola-rs/polars](https://github.com/pola-rs/polars) | Rust | 39772 | 2026-09-18 | Extremely fast Query Engine for DataFrames, written in Rust |
| [ClickHouse/clickhouse-rs](https://github.com/ClickHouse/clickhouse-rs) | Rust | 559 | 2026-09-18 | Official typed Rust client for ClickHouse, with async row streaming over HTTP and derive-based schema mapping. |
| [delta-io/delta-kernel-rs](https://github.com/delta-io/delta-kernel-rs) | Rust | 362 | 2026-09-18 | Native Rust implementation of the Delta Lake protocol, giving any query engine a correct table reader and writer. |


<a id="time-series-databases"></a>

---

## Time Series Databases

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) | Rust | 6682 | 2026-09-18 | The open-source Observability 2.0 database |
| [apache/iotdb](https://github.com/apache/iotdb) | Java | 6401 | 2026-09-18 | Time-series database for IoT and industrial telemetry, with a device-oriented data model, columnar TsFile storage and SQL-like queries. |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [What is high cardinality, and how do time-series databases like InfluxDB and TimescaleDB compare?](https://blog.timescale.com/what-is-high-cardinality-how-do-time-series-databases-influxdb-timescaledb-compare/) | article | 2019-04 | data-storage, databases, frontend |
| [TimescaleDB 1.1 performance optimizations and PG11 Support](https://blog.timescale.com/timescaledb1-1-postgresql11-support-open-source-d108b2b244c3) | article | 2018-12 | data-storage, databases, language-runtimes |
| [TimescaleDB vs. InfluxDB: purpose built differently for time-series data](https://blog.timescale.com/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877) | article | 2018-09 | data-storage, databases, frontend |
| [Towards 3B time-series data points per day: Why DNSFilter replaced InfluxDB with TimescaleDB](https://blog.dnsfilter.com/3-billion-time-series-data-points-dnsfilter-replaced-influxdb-with-timescaledb-d9f827702f8b) | article | 2018-09 | data-storage, databases, frontend |


<a id="vector-databases"></a>

---

## Vector Databases

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [milvus-io/milvus](https://github.com/milvus-io/milvus) | Go | 46151 | 2026-09-18 | Cloud-native vector database for billion-scale ANN search, with HNSW and DiskANN indexes, hybrid filtering and a distributed storage-compute split. |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Rust | 34656 | 2026-09-18 | Vector search engine and database written in Rust, with HNSW indexing, payload filtering and hybrid search for retrieval and recommendation workloads. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [RyanCodrai/turbovec](https://github.com/RyanCodrai/turbovec) | Rust | 17197 | 2026-09-13 | Vector index built on TurboQuant quantisation, written in Rust with SIMD kernels and Python bindings for nearest-neighbour search. |


<a id="graph-databases"></a>

---

## Graph Databases

#### Tools (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | C | 6164 | 2026-09-18 | A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation |
| [memgraph/memgraph](https://github.com/memgraph/memgraph) | C++ | 4569 | 2026-09-18 | In-memory graph database with openCypher support, streaming ingestion from Kafka and a bundled algorithm library, aimed at real-time analytics and GraphRAG. |
| [typedb/typedb](https://github.com/typedb/typedb) | Rust | 4455 | 2026-09-18 | Strongly-typed database with a polymorphic schema and built-in reasoning, modelling entities, relations and rules rather than rows. |
| [memgraph/memgraph-docker-extension](https://github.com/memgraph/memgraph-docker-extension) | Dockerfile | 17 | 2026-09-14 | Docker extension for Memgraph, MAGE and Memgraph Lab |
| [memgraph/best-practices](https://github.com/memgraph/best-practices) | Cypher | 15 | 2026-07-08 | The shortest path to a successful project with Memgraph |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [neotypes/neotypes](https://github.com/neotypes/neotypes) | Scala | 176 | 2026-05-07 | Scala lightweight, type-safe, asynchronous driver for neo4j |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Journey Planning… And Why I Love Cypher](https://neo4j.com/blog/journey-planning-why-i-love-cypher/) | article | 2019-04 | data-storage, databases |
| [Neotypes (Part 1): Akka-http + neo4j](https://medium.com/neo4j/neotypes-part-1-akka-http-neo4j-6cab38d077d4) | article | 2019-03 | data-storage, databases, distributed-systems, fp-scala |


<a id="document-databases"></a>

---

## Document Databases

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [zeal18/zio-mongodb](https://github.com/zeal18/zio-mongodb) | Scala | 28 | 2026-09-12 | One more ZIO wrapper around the official MongoDB Java driver but better ;) |


<a id="kv-stores"></a>

---

## KV Stores

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [redis/redis](https://github.com/redis/redis) | C | 76399 | 2026-09-17 | For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-r |
| [etcd-io/etcd](https://github.com/etcd-io/etcd) | Go | 52273 | 2026-09-18 | Distributed reliable key-value store for the most critical data of a distributed system |
| [dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly) | C++ | 31592 | 2026-09-18 | A modern replacement for Redis and Memcached |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Why are we getting Streams in Redis?](https://blog.logrocket.com/why-are-we-getting-streams-in-redis-8c36498aaac5) | article | 2019-01 | data-storage, databases |
| [Clarifications on the Incapsula Redis security report](http://antirez.com/news/118) | article | 2018-07 | data-storage, databases |
| [Redis Lua scripting: several security vulnerabilities fixed](http://antirez.com/news/119) | article | 2018-07 | data-storage, databases |
| [Speeding up the HTTP service with Redis caching](https://blog.softwaremill.com/speeding-up-the-http-service-with-redis-caching-bb6980c1ae2d) | article | 2018-07 | data-storage, databases, fp-scala, language-runtimes |


<a id="caches"></a>

---

## Caches

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [moka-rs/moka](https://github.com/moka-rs/moka) | Rust | 2685 | 2026-08-09 | A high performance concurrent caching library for Rust |


<a id="search-engines"></a>

---

## Search Engines

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch) | Rust | 59323 | 2026-09-17 | A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications |
| [typesense/typesense](https://github.com/typesense/typesense) | C++ | 26571 | 2026-09-18 | Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch ⚡ 🔍 ✨ Fast, typo toleran |
| [valeriansaliou/sonic](https://github.com/valeriansaliou/sonic) | Rust | 21342 | 2026-09-15 | 🦔 Fast, lightweight & schema-less search backend |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [quickwit-oss/tantivy](https://github.com/quickwit-oss/tantivy) | Rust | 16110 | 2026-09-18 | Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Lucene: The Good Parts](https://blog.parse.ly/post/1691/lucene/) | article | 2018-08 | web-extraction |


<a id="object-stores"></a>

---

## Object Stores

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ceph/ceph](https://github.com/ceph/ceph) | C++ | 17054 | 2026-09-18 | Ceph is a distributed object, block, and file storage platform |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Big Data Storage Wars: Ceph vs Gluster](https://technologyadvice.com/blog/information-technology/ceph-vs-gluster/) | article | 2019-03 | data-storage |


<a id="message-queues"></a>

---

## Message Queues

#### Tools (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [nsqio/nsq](https://github.com/nsqio/nsq) | Go | 25777 | 2026-08-11 | Realtime distributed messaging platform with no central broker, offering per-topic queues, at-least-once delivery and horizontal scaling. |
| [nats-io/nats-server](https://github.com/nats-io/nats-server) | Go | 20744 | 2026-09-18 | High-Performance server for NATS.io, the cloud and edge native messaging system |
| [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda) | C++ | 12553 | 2026-08-22 | Redpanda is a streaming data platform for developers |
| [nats-io/nats.java](https://github.com/nats-io/nats.java) | Java | 679 | 2026-09-10 | Java client for NATS |
| [rabbitmq/rabbitmq-stream-java-client](https://github.com/rabbitmq/rabbitmq-stream-java-client) | Java | 72 | 2026-09-18 | RabbitMQ Stream Java Client |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [svix/omniqueue-rs](https://github.com/svix/omniqueue-rs) | Rust | 109 | 2026-09-14 | A Queue Abstraction Layer for Rust (Redis, RabbitMQ, SQS, etc.) |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Apache Kafka and MQTT: End-to-End IoT Integration](https://dzone.com/articles/apache-kafka-mqtt-end-to-end-iot-integration-githu) | article | 2019-02 | distributed-systems, kafka |
| [Understanding When to use RabbitMQ or Apache Kafka](https://content.pivotal.io/blog/understanding-when-to-use-rabbitmq-or-apache-kafka) | article | 2018-05 | distributed-systems, kafka, rabbitmq |


<a id="stream-processing"></a>

---

## Stream Processing

#### Tools (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [debezium/debezium](https://github.com/debezium/debezium) | Java | 13132 | 2026-09-18 | Change data capture for a variety of databases |
| [risingwavelabs/risingwave](https://github.com/risingwavelabs/risingwave) | Rust | 9332 | 2026-09-18 | Event streaming platform for agentic AI |
| [arkflow-rs/arkflow](https://github.com/arkflow-rs/arkflow) | Rust | 1304 | 2026-09-18 | High performance Rust stream processing engine seamlessly integrates AI capabilities, providing powerful real-time data |
| [SeaQL/sea-streamer](https://github.com/SeaQL/sea-streamer) | Rust | 370 | 2026-09-17 | 🌊 Stream processing toolkit for Redis & Kafka |


<a id="graph-processing"></a>

---

## Graph Processing

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [alibaba/GraphScope](https://github.com/alibaba/GraphScope) | C++ | 3557 | 2026-09-04 | One-stop graph computing system from Alibaba, unifying graph analytics, interactive Gremlin queries and graph neural networks at scale. |
| [apache/geaflow](https://github.com/apache/geaflow) | Java | 809 | 2026-09-14 | Distributed streaming graph computing engine from Apache, running incremental graph traversals over continuously changing data. |


<a id="realtime-messaging"></a>

---

## Realtime Messaging

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [novuhq/novu](https://github.com/novuhq/novu) | TypeScript | 40012 | 2026-09-18 | Notification infrastructure that orchestrates email, SMS, push and in-app inbox delivery from a single workflow API. |
| [centrifugal/centrifugo](https://github.com/centrifugal/centrifugo) | Go | 10765 | 2026-09-14 | Language-agnostic real-time messaging server delivering pub/sub over WebSocket, SSE and WebTransport as a self-hosted Pusher alternative. |


<a id="async-runtimes"></a>

---

## Async Runtimes

#### Libraries (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [tokio-rs/tokio](https://github.com/tokio-rs/tokio) | Rust | 33172 | 2026-09-18 | A runtime for writing reliable asynchronous applications with Rust |
| [smol-rs/smol](https://github.com/smol-rs/smol) | Rust | 5067 | 2026-08-03 | A small and fast async runtime for Rust |
| [tokio-rs/console](https://github.com/tokio-rs/console) | Rust | 4598 | 2026-08-08 | a debugger for async rust! |
| [tower-rs/tower](https://github.com/tower-rs/tower) | Rust | 4296 | 2026-06-22 | Rust abstraction for asynchronous request-response services, with composable middleware for timeouts, retries, load balancing and rate limiting. |

#### Unsorted (12)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [libpnet/libpnet](https://github.com/libpnet/libpnet) | Rust | 2591 | 2026-05-01 | Cross-platform, low level networking using the Rust programming language |
| [JelteF/derive_more](https://github.com/JelteF/derive_more) | Rust | 2138 | 2026-09-07 | Some more derive(Trait) options |
| [tqwewe/kameo](https://github.com/tqwewe/kameo) | Rust | 1387 | 2026-09-13 | Fault-tolerant async actors for Rust that scale seamlessly |
| [akka/akka-http](https://github.com/akka/akka-http) | Scala | 1351 | 2026-09-18 | The Streaming-first HTTP server/module of Akka |
| [rxRust/rxRust](https://github.com/rxRust/rxRust) | Rust | 1113 | 2026-09-04 | Zero-cost & Type-safe Reactive Extensions for Rust |
| [oconnor663/duct.rs](https://github.com/oconnor663/duct.rs) | Rust | 1043 | 2026-09-03 | a Rust library for running child processes |
| [ibraheemdev/papaya](https://github.com/ibraheemdev/papaya) | Rust | 945 | 2026-08-21 | A fast and ergonomic concurrent hashmap for read-heavy workloads |
| [zkat/cacache-rs](https://github.com/zkat/cacache-rs) | Rust | 721 | 2026-06-01 | A high-performance, concurrent, content-addressable disk cache, with support for both sync and async APIs |
| [lemastero/scala_typeclassopedia](https://github.com/lemastero/scala_typeclassopedia) | Scala | 385 | 2024-12-05 | Abstractions from Category theory with simple description & implementation, links to further resources. |
| [stav121/tasklet](https://github.com/stav121/tasklet) | Rust | 96 | 2026-08-24 | ⏱️ An asynchronous task scheduling library written in Rust |
| [borsaorg/borsa](https://github.com/borsaorg/borsa) | Rust | 24 | 2025-11-16 | Market data orchestrator for Rust with pluggable providers, data merging, and streaming |
| [but212/rustica](https://github.com/but212/rustica) | Rust | 18 | 2026-09-16 | Rustica is a functional programming library for the Rust language |

#### Articles (8)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Concurrency Glossary](https://slikts.github.io/concurrency-glossary/?id=scheduling-flow-control-temporal-composition) | article | 2018-12 | concurrency, language-runtimes |
| [Thread Pools](https://gist.github.com/djspiewak/46b543800958cf61af6efa8e072bfd5c) | article | 2018-11 | concurrency, language-runtimes |
| [Basics of Futexes](https://eli.thegreenplace.net/2018/basics-of-futexes/) | article | 2018-08 | concurrency, language-runtimes |
| [ES7 async functions](https://jakearchibald.com/2014/es7-async-functions/) | article | 2018-05 | concurrency, language-runtimes |
| [JavaScript Promises: an Introduction](https://developers.google.com/web/fundamentals/primers/promises) | article | 2018-05 | concurrency, language-runtimes |
| [On properly using volatile and synchronized](https://medium.com/google-developer-experts/on-properly-using-volatile-and-synchronized-702fc05faac2) | article | 2018-05 | concurrency, language-runtimes |
| [Why coroutines won’t work on the web](http://calculist.org/blog/2011/12/14/why-coroutines-wont-work-on-the-web/) | article | 2018-05 | concurrency, language-runtimes |
| [Asynchronous Programming and Scala](https://alexn.org/blog/2017/01/30/asynchronous-programming-scala.html) | article | 2018-04 | concurrency, fp-scala, language-runtimes |

#### Videos (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Concurrency Concepts in Java](https://www.youtube.com/watch?v=3_J3UZzDsgc) | video | 2018-05 | concurrency, language-runtimes |
| [The Event Loop](https://www.youtube.com/watch?v=0IsjjMRyIF8) | video | 2018-05 | misc |


<a id="effect-systems"></a>

---

## Effect Systems

#### Libraries (13)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [zio/zio](https://github.com/zio/zio) | Scala | 4420 | 2026-09-18 | ZIO — A type-safe, composable library for async and concurrent programming in Scala |
| [zio/zio-http](https://github.com/zio/zio-http) | Scala | 875 | 2026-09-18 | A next-generation Scala framework for building scalable, correct, and efficient HTTP clients and servers |
| [getkyo/kyo](https://github.com/getkyo/kyo) | Scala | 812 | 2026-09-18 | Toolkit for Scala Development |
| [zio/zio-prelude](https://github.com/zio/zio-prelude) | Scala | 472 | 2026-09-17 | A lightweight, distinctly Scala take on functional abstractions, with tight ZIO integration |
| [zio/zio-json](https://github.com/zio/zio-json) | Scala | 431 | 2026-09-15 | Fast, secure JSON library with tight ZIO integration |
| [zio/zio-kafka](https://github.com/zio/zio-kafka) | Scala | 367 | 2026-09-15 | A fast Kafka client for ZIO and ZIO Streams |
| [zio/zio-config](https://github.com/zio/zio-config) | Scala | 244 | 2026-09-17 | Easily use and document any config from anywhere in ZIO apps |
| [zio/zio-intellij](https://github.com/zio/zio-intellij) | Scala | 227 | 2026-07-21 | A companion IntelliJ IDEA plugin for the ZIO library ecosystem |
| [zio/zio-logging](https://github.com/zio/zio-logging) | Scala | 188 | 2026-09-13 | Powerful logging for ZIO 2.0 applications, with compatibility with many logging backends out-of-the-box |
| [zio/zio-redis](https://github.com/zio/zio-redis) | Scala | 136 | 2026-09-15 | A ZIO-based redis client |
| [zio/zio-telemetry](https://github.com/zio/zio-telemetry) | Scala | 124 | 2026-09-15 | ZIO-powered OpenTelemetry library |
| [zio/zio-cache](https://github.com/zio/zio-cache) | Scala | 87 | 2026-09-15 | A ZIO native cache with a simple and compositional interface |
| [bilal-fazlani/zio-ulid](https://github.com/bilal-fazlani/zio-ulid) | Scala | 11 | 2024-01-16 | zio implementation for https://github.com/ulid/spec |

#### Articles (16)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Using 47 Degree's Fetch library with ZIO](http://justinhj.github.io/2019/05/05/using-47degs-fetch-with-zio.html) | article | 2019-05 | fp-scala, language-runtimes, zio |
| [ZIO & Cats Effect: A Match Made in Heaven](http://degoes.net/articles/zio-cats-effect) | article | 2019-04 | cats-effect, fp-scala, language-runtimes, zio |
| [Data Modeling in FP vs OOP](http://degoes.net/articles/fp-vs-oop-part1) | article | 2018-09 | fp-scala, language-runtimes, zio |
| [Http4s error handling with Cats Meow MTL](https://typelevel.org/blog/2018/08/25/http4s-error-handling-mtl.html) | article | 2018-09 | cats-effect, error-handling, fp-scala, language-runtimes |
| [Scala Wars: FP-OOP vs FP](http://degoes.net/articles/fpoop-vs-fp) | article | 2018-09 | fp-scala, language-runtimes, zio |
| [Akka anti-patterns: Java serialization](https://manuel.bernhardt.io/2018/07/20/akka-anti-patterns-java-serialization/) | article | 2018-07 | architecture-ddd, distributed-systems, fp-scala |
| [Akka, Monix, ZIO - Part 1](https://blog.softwaremill.com/scalaz-8-io-vs-akka-typed-actors-vs-monix-part-1-5672657169e1) | article | 2018-07 | distributed-systems, fp-scala, language-runtimes, zio |
| [Akka, Monix, ZIO - Part 2 - Communication](https://blog.softwaremill.com/akka-vs-zio-vs-monix-part-2-communication-9ce7261aa08c) | article | 2018-07 | distributed-systems, fp-scala, language-runtimes, zio |
| [Akka, Monix, ZIO - Part 3 - Supervision & Error Handling](https://blog.softwaremill.com/supervision-error-handling-in-zio-akka-and-monix-part-3-series-summary-abe75f964c2a) | article | 2018-07 | distributed-systems, error-handling, fp-scala, language-runtimes |
| [Arrows, Monads and Kleisli — Part I](https://medium.com/virtuslab/arrows-monads-and-kleisli-part-i-6c2a35c27a6e) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Arrows, Monads and Kleisli — Part II](https://medium.com/virtuslab/arrows-monads-and-kleisli-part-ii-12ffd4da8bc9) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Extending RequestContext in akka-http for fun and profit](https://medium.com/iterators/extending-requestcontext-in-akka-http-for-fun-and-profit-ceb056964758) | article | 2018-07 | distributed-systems, fp-scala, standards |
| [Bifunctor IO: A Step Away from Dynamically-Typed Error Handling](http://degoes.net/articles/bifunctor-io) | article | 2018-05 | error-handling, fp-scala, language-runtimes, typelevel |
| [No More Transformers: High-Performance Effects in Scalaz 8](https://dzone.com/articles/no-more-transformers-high-performance-effects-in-s) | article | 2018-05 | fp-scala, language-runtimes |
| [Optimizing Tagless Final – Saying farewell to Free](https://typelevel.org/blog/2017/12/27/optimizing-final-tagless.html) | article | 2018-05 | fp-scala, language-runtimes, typelevel |
| [Rethinking MonadError](https://typelevel.org/blog/2018/04/13/rethinking-monaderror.html) | article | 2018-04 | error-handling, fp-scala, language-runtimes, typelevel |

#### Videos (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Monad transformers down to earth](https://www.youtube.com/watch?v=jd5e71nFEZM) | video | 2018-05 | fp-scala, language-runtimes, typelevel |


<a id="compilers"></a>

---

## Compilers

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [carbon-language/carbon-lang](https://github.com/carbon-language/carbon-lang) | C++ | 33896 | 2026-09-18 | Carbon Language's main repository: documents, design, implementation, and related tools |
| [scala/scala](https://github.com/scala/scala) | Scala | 14561 | 2026-09-09 | Scala 2 compiler and standard library |
| [scala/scala3](https://github.com/scala/scala3) | Scala | 6301 | 2026-09-18 | The Scala 3 compiler, also known as Dotty |

#### Articles (40)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Faster script loading with BinaryAST?](https://blog.cloudflare.com/binary-ast/) | article | 2019-05 | misc |
| [Project Valhalla: A First Look at L-World Value Types](https://dzone.com/articles/project-valhalla-a-first-look-at-l-world-value-typ?fromrel=true) | article | 2019-03 | misc |
| [What Is Project Valhalla?](https://dzone.com/articles/what-is-project-valhalla) | article | 2019-03 | misc |
| [Java Money and the Currency API](https://www.baeldung.com/java-money-and-currency) | article | 2019-01 | misc |
| [Scala Best Practices](https://nrinaudo.github.io/scala-best-practices/) | article | 2019-01 | fp-scala, language-runtimes |
| [Anatomy of a Scala quirk](https://blog.buildo.io/anatomy-of-a-scala-quirk-b8c086b56423) | article | 2018-12 | fp-scala, language-runtimes |
| [Using jlink to Build Java Runtimes for non-Modular Applications](https://medium.com/azulsystems/using-jlink-to-build-java-runtimes-for-non-modular-applications-9568c5e70ef4) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [90 New Features and APIs in JDK 11 (Part 1)](https://dzone.com/articles/90-new-features-and-apis-in-jdk-11) | article | 2018-10 | misc |
| [90 New Features and APIs in JDK 11 (Part 2)](https://dzone.com/articles/90-new-features-and-apis-in-jdk-11-part-2) | article | 2018-10 | misc |
| [Disambiguating 'this' in Scala, or what does 'self =>' mean?](http://enear.github.io/2018/10/08/self-arrow/) | article | 2018-10 | fp-scala, kernel-systems, language-runtimes |
| [JDK 12 News: Switch Expressions and Raw String Literals](https://dzone.com/articles/jdk-12-news-13-september-2018) | article | 2018-10 | misc |
| [A major release just around the corner — meet Kotlin 1.3-M2](https://blog.jetbrains.com/kotlin/2018/08/kotlin-1-3-m2/) | article | 2018-09 | language-runtimes |
| [Announcing Okio 2: Our fast + simple I/O library, Okio, has a new release that supports Kotlin](https://medium.com/square-corner-blog/okio-2-6f6c35149525) | article | 2018-09 | language-runtimes |
| [Are Scala Futures the past?](https://medium.com/@sderosiaux/are-scala-futures-the-past-69bd62b9c001) | article | 2018-09 | fp-scala, language-runtimes |
| [New pretty id generator in scala-id-generator](https://blog.softwaremill.com/new-pretty-id-generator-in-scala-commons-39b0fc6b6210) | article | 2018-09 | fp-scala, language-runtimes |
| [Simple Scala Stack](https://blog.softwaremill.com/simple-scala-stack-70fc786132b5) | article | 2018-08 | fp-scala, language-runtimes |
| [Why Scala?](https://blog.softwaremill.com/why-scala-a6ac8c98c541) | article | 2018-08 | fp-scala, language-runtimes |
| [How to turn ugly Java APIs into elegant, type-safe Scala APIs](https://medium.com/iterators/how-to-turn-ugly-java-apis-into-elegant-type-safe-scala-apis-9eab358e5fb2) | article | 2018-07 | ai-applications, fp-scala, language-runtimes |
| [Why Scala?](https://blog.softwaremill.com/why-scala-a6ac8c98c541) | article | 2018-07 | fp-scala, language-runtimes |
| [Android Studio 3.2 Beta](https://android-developers.googleblog.com/2018/06/android-studio-3-2-beta.html) | article | 2018-06 | language-runtimes |
| [Apprentice Blog of the Week: Did Java Break My byte?](https://8thlight.com/blog/dave-torre/2014/09/10/did-java-break-my-byte.html) | article | 2018-06 | observability |
| [Crushing boilerplate with Scala Macros](https://medium.com/iterators/crushing-boilerplate-with-scala-macros-754860551c98) | article | 2018-06 | fp-scala, language-runtimes |
| [Exploring Android P: Priority Buckets](https://medium.com/google-developer-experts/exploring-android-p-priority-buckets-d34d12059d36) | article | 2018-06 | language-runtimes |
| [Java Code To Byte Code - Part One](http://blog.jamesdbloom.com/JavaCodeToByteCode_PartOne.html) | article | 2018-06 | compilers, language-runtimes |
| [JVM Internals](http://blog.jamesdbloom.com/JVMInternals.html) | article | 2018-06 | compilers, language-runtimes |
| [Keys, Credentials and Storage on Android](https://code.tutsplus.com/tutorials/keys-credentials-and-storage-on-android--cms-30827) | article | 2018-06 | language-runtimes |
| [Scala 2.13 Collections Feature Freeze](https://www.scala-lang.org/blog/2018/06/05/collections-feature-freeze.html) | article | 2018-06 | fp-scala, language-runtimes |
| [Scala 2.13 Collections Rework](https://www.scala-lang.org/blog/2017/02/28/collections-rework.html) | article | 2018-06 | fp-scala, language-runtimes |
| [Scala 2.13’s Collections](https://www.scala-lang.org/blog/2018/06/13/scala-213-collections.html) | article | 2018-06 | fp-scala, language-runtimes |
| [Scala Vector operations aren't "Effectively Constant" time](http://www.lihaoyi.com/post/ScalaVectoroperationsarentEffectivelyConstanttime.html) | article | 2018-06 | fp-scala, language-runtimes |
| [Unsigned Integer Arithmetic API now in JDK 8](https://blogs.oracle.com/darcy/unsigned-integer-arithmetic-api-now-in-jdk-8) | article | 2018-06 | misc |
| [Warts of the Scala Programming Language](http://www.lihaoyi.com/post/WartsoftheScalaProgrammingLanguage.html) | article | 2018-06 | fp-scala, language-runtimes |
| [Macros: the Plan for Scala 3](https://www.scala-lang.org/blog/2018/04/30/in-a-nutshell.html) | article | 2018-05 | fp-scala, language-runtimes |
| [Scala Enumerations Hell](https://medium.com/@yuriigorbylov/scala-enumerations-hell-5bdba2c1216) | article | 2018-05 | fp-scala, language-runtimes |
| [uJson: fast, flexible and intuitive JSON for Scala](http://www.lihaoyi.com/post/uJsonfastflexibleandintuitiveJSONforScala.html) | article | 2018-05 | fp-scala, language-runtimes |
| [Writing an Internal DSL in Scala](https://mostafa-asg.github.io/post/writing-internal-dsl-in-scala/) | article | 2018-05 | fp-scala, language-runtimes |
| [Composing Service Layers in Scala](https://gist.github.com/aappddeevv/8509607) | article | 2018-04 | fp-scala, language-runtimes |
| [Scala, Cake Patterns and the Problem](https://gist.github.com/aappddeevv/8419494) | article | 2018-04 | architecture-ddd, fp-scala, language-runtimes |
| [The v28 Android Design Support Library](https://medium.com/exploring-android/exploring-the-v28-android-design-support-library-2c96c6031ae8) | article | 2018-04 | language-runtimes |
| [Towards Scala 3](https://scala-lang.org/blog/2018/04/19/scala-3.html) | article | 2018-04 | fp-scala, language-runtimes |


<a id="parsers"></a>

---

## Parsers

#### Libraries (8)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [google/libphonenumber](https://github.com/google/libphonenumber) | C++ | 18276 | 2026-09-10 | Google's common Java, C++ and JavaScript library for parsing, formatting, and validating international phone numbers |
| [Marwes/combine](https://github.com/Marwes/combine) | Rust | 1372 | 2026-09-18 | A parser combinator library for Rust |
| [keichi/binary-parser](https://github.com/keichi/binary-parser) | TypeScript | 955 | 2026-05-28 | A blazing-fast declarative parser builder for binary data |
| [scodec/scodec](https://github.com/scodec/scodec) | Scala | 816 | 2026-09-08 | Scala combinator library for working with binary data |
| [typelevel/jawn](https://github.com/typelevel/jawn) | Scala | 436 | 2026-09-14 | Jawn is for parsing jay-sawn (JSON) |
| [ada-url/rust](https://github.com/ada-url/rust) | Rust | 121 | 2026-09-01 | Rust bindings for the Ada URL parser, a WHATWG-compliant implementation used for fast URL parsing and normalisation. |
| [azam/ulidj](https://github.com/azam/ulidj) | Java | 121 | 2026-09-15 | ULID (Universally Unique Lexicographically Sortable Identifier) generator and parser for Java |
| [ArneCode/marser](https://github.com/ArneCode/marser) | Rust | 31 | 2026-07-08 | Parser-combinator library for PEG-style grammars in Rust, focused on useful diagnostics, error recovery and performance. |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Easy Parsing with Parser Combinators](http://www.lihaoyi.com/post/EasyParsingwithParserCombinators.html) | article | 2018-06 | fp-scala, language-runtimes, parsers |
| [Parsing JSON is a Minefield](http://seriot.ch/parsing_json.php) | article | 2018-06 | language-runtimes, parsers |
| [FastParse 1.0: Past, Present & Future](http://www.lihaoyi.com/post/FastParse10PastPresentFuture.html) | article | 2018-05 | fp-scala, language-runtimes, parsers |
| [Creating a Recursive Descent Parser](http://knuth.luther.edu/~leekent/tutorials/ll1.html) | article | 2018-04 | language-runtimes, parsers |


<a id="static-analyzers"></a>

---

## Static Analyzers

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep) | Rust | 15950 | 2026-09-17 | ⚡A CLI tool for code structural search, lint and rewriting |


<a id="type-checkers"></a>

---

## Type Checkers

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [microsoft/pyright](https://github.com/microsoft/pyright) | Python | 15647 | 2026-09-17 | Static Type Checker for Python |


<a id="garbage-collectors"></a>

---

## Garbage Collectors

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [For Better Computing, Liberate CPUs From Garbage Collection](https://spectrum.ieee.org/tech-talk/computing/hardware/this-little-device-relieves-a-cpu-from-its-garbage-collection-duties/) | article | 2019-05 | language-runtimes, misc |
| [Java's new Z Garbage Collector (ZGC) is very exciting](https://www.opsian.com/blog/javas-new-zgc-is-very-exciting/) | article | 2018-09 | language-runtimes |


<a id="state-machines"></a>

---

## State Machines

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [statelyai/xstate](https://github.com/statelyai/xstate) | TypeScript | 30125 | 2026-09-17 | State machine and statechart library for JavaScript and TypeScript that models complex application logic as actors with explicit transitions. |


<a id="concurrency-primitives"></a>

---

## Concurrency Primitives

#### Libraries (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [rayon-rs/rayon](https://github.com/rayon-rs/rayon) | Rust | 13321 | 2026-08-28 | Data-parallelism library for Rust that converts sequential iterator chains into work-stealing parallel ones with a one-word change. |
| [crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam) | Rust | 8577 | 2026-09-07 | Concurrency toolkit for Rust: channels, scoped threads, epoch-based memory reclamation and lock-free data structures. |
| [JCTools/JCTools](https://github.com/JCTools/JCTools) | Java | 3876 | 2026-08-18 | Lock-free and wait-free queues and maps for the JVM, with single- and multi-producer variants benchmarked for low-latency messaging paths. |


<a id="serialization-formats"></a>

---

## Serialization Formats

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apache/fory](https://github.com/apache/fory) | Java | 4551 | 2026-09-17 | Multi-language serialization framework using JIT-generated codecs and zero-copy layouts to move idiomatic objects between Java, Python, Go, Rust and JavaScript. |


<a id="data-structures"></a>

---

## Data Structures

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [petgraph/petgraph](https://github.com/petgraph/petgraph) | Rust | 4019 | 2026-09-13 | Graph data structures for Rust — adjacency list, matrix and stable variants — with traversal, shortest-path and other standard graph algorithms. |


<a id="date-time-libraries"></a>

---

## Date Time Libraries

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [chronotope/chrono](https://github.com/chronotope/chrono) | Rust | 3909 | 2026-09-07 | Date and time library for Rust, with time-zone-aware and naive types, parsing and formatting, and calendar-correct duration arithmetic. |


<a id="consensus"></a>

---

## Consensus

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [databendlabs/openraft](https://github.com/databendlabs/openraft) | Rust | 2057 | 2026-09-18 | rust raft with improvements |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [How we implemented consistent hashing efficiently](https://blog.ably.io/how-to-implement-consistent-hashing-efficiently-fe038d59fff2) | article | 2018-06 | distributed-systems |

#### Videos (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Distributed Systems In One Lesson](https://www.youtube.com/watch?v=OJwp4kroTM8) | video | 2018-05 | distributed-systems |
| [Don't trust Time](https://www.youtube.com/watch?v=ylfyezRhA5s) | video | 2018-05 | fp-rust, language-runtimes |


<a id="event-sourcing"></a>

---

## Event Sourcing

#### Libraries (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [kurrent-io/KurrentDB](https://github.com/kurrent-io/KurrentDB) | C# | 5853 | 2026-09-18 | KurrentDB is a database that's engineered for modern software applications and event-driven architectures |
| [serverlesstechnology/cqrs](https://github.com/serverlesstechnology/cqrs) | Rust | 497 | 2026-09-07 | A lightweight, opinionated CQRS and event sourcing framework |
| [kurrent-io/KurrentDB-Client-Rust](https://github.com/kurrent-io/KurrentDB-Client-Rust) | Rust | 63 | 2026-08-08 | KurrentDB Rust Client |

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Saga Pattern — How to implement business transactions using Microservices – Part I](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part/) | article | 2019-06 | architecture-ddd, distributed-systems, event-sourcing, microservices |
| [Saga Pattern — How to implement business transactions using Microservices – Part II](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part-2/) | article | 2019-06 | architecture-ddd, distributed-systems, event-sourcing, microservices |
| [Keep your domain clean in Event Sourcing](https://blog.softwaremill.com/keep-your-domain-clean-in-event-sourcing-5db6ddc26fe4) | article | 2018-08 | architecture-ddd, distributed-systems, event-sourcing, fp-scala |


<a id="workflow-engines"></a>

---

## Workflow Engines

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apache/incubator-seata](https://github.com/apache/incubator-seata) | Java | 26008 | 2026-09-13 | :fire: Seata is an easy-to-use, high-performance, open source distributed transaction solution |
| [temporalio/temporal](https://github.com/temporalio/temporal) | Go | 23150 | 2026-09-18 | Durable execution service that runs workflows and activities as replayable code, surviving process crashes, retries and long waits. |
| [apache/dolphinscheduler](https://github.com/apache/dolphinscheduler) | Java | 14484 | 2026-09-18 | Distributed data-orchestration platform with a low-code DAG editor for scheduling, monitoring and retrying large workflow pipelines. |


<a id="service-meshes"></a>

---

## Service Meshes

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [envoyproxy/gateway](https://github.com/envoyproxy/gateway) | Go | 3036 | 2026-09-18 | Manages Envoy Proxy as a Standalone or Kubernetes-based Application Gateway |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Service Mesh – A New Pattern, Not A New Technology?](https://konghq.com/blog/service-mesh-new-pattern-not-new-technology/) | article | 2018-08 | architecture-ddd, infrastructure, kubernetes, observability |

#### Videos (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Microservices, Service Mesh, and CI/CD Pipelines: Making It All Work Together](https://www.youtube.com/watch?v=6L15-GyYh6I) | video | 2018-05 | distributed-systems, infrastructure, kubernetes, microservices |


<a id="api-gateways"></a>

---

## Api Gateways

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Separating Control and Data Planes in Kong](https://konghq.com/blog/separating-data-control-planes/) | article | 2018-05 | infrastructure, kubernetes |


<a id="rpc-frameworks"></a>

---

## RPC Frameworks

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [GraphQL: A Retrospective](https://verve.co/engineering/graphql-a-retrospective/) | article | 2018-12 | standards, web-extraction |


<a id="service-discovery"></a>

---

## Service Discovery

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [superfly/corrosion](https://github.com/superfly/corrosion) | Rust | 1846 | 2026-09-17 | Gossip-based service discovery (and more) for large distributed systems |


<a id="distributed-runtimes"></a>

---

## Distributed Runtimes

#### Frameworks (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [dapr/dapr](https://github.com/dapr/dapr) | Go | 26098 | 2026-09-17 | Sidecar runtime giving services portable building blocks for pub/sub, state, secrets, service invocation and workflow across cloud and edge. |
| [akka/akka-core](https://github.com/akka/akka-core) | Scala | 13280 | 2026-09-17 | Actor-model toolkit for the JVM for building elastic, resilient distributed applications, with clustering, persistence and back-pressured streams. |
| [helidon-io/helidon](https://github.com/helidon-io/helidon) | Java | 3823 | 2026-09-18 | Java microservices runtime offering both a lightweight functional SE API and a MicroProfile implementation, built on virtual threads. |


<a id="identifier-generation"></a>

---

## Identifier Generation

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [segmentio/ksuid](https://github.com/segmentio/ksuid) | Go | 5270 | 2026-06-25 | Go implementation of KSUID, a 20-byte k-sortable unique identifier that embeds a timestamp so IDs sort chronologically without any coordination. |
| [paralleldrive/cuid](https://github.com/paralleldrive/cuid) | JavaScript | 3502 | 2026-09-15 | Original cuid collision-resistant ID generator for JavaScript, now deprecated in favour of cuid2 because its IDs leak timestamps and host fingerprints. |


<a id="distributed-tracing"></a>

---

## Distributed Tracing

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator) | Go | 1756 | 2026-09-18 | Kubernetes Operator for OpenTelemetry Collector |
| [hypertrace/hypertrace](https://github.com/hypertrace/hypertrace) | Shell | 519 | 2025-03-14 | An open source distributed tracing & observability platform |


<a id="metrics"></a>

---

## Metrics

#### Unsorted (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [DrDroidLab/PlayBooks](https://github.com/DrDroidLab/PlayBooks) | Python | 460 | 2025-11-10 | Runbook automation platform with deep observability integrations for SRE & On-Call Teams |
| [DataJunction/dj](https://github.com/DataJunction/dj) | Python | 161 | 2026-09-17 | A metrics platform |


<a id="logging"></a>

---

## Logging

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [daboross/fern](https://github.com/daboross/fern) | Rust | 914 | 2024-12-15 | Simple, efficient logging for Rust |


<a id="apm"></a>

---

## APM

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [SigNoz/signoz](https://github.com/SigNoz/signoz) | TypeScript | 32130 | 2026-09-18 | OpenTelemetry-native observability platform that puts logs, metrics and traces behind one UI, with APM, distributed tracing and infra monitoring. |
| [coroot/coroot](https://github.com/coroot/coroot) | Go | 7919 | 2026-09-17 | Coroot is an open-source observability and APM tool with AI-powered Root Cause Analysis |


<a id="agent-frameworks"></a>

---

## Agent Frameworks

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | Python | 96258 | 2026-03-26 | Harness for AI agents that autonomously run and evaluate training experiments on single-GPU nanochat models. |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | TypeScript | 3614 | 2026-03-30 | Self-hosted orchestrator running multiple teams of AI agents in isolated workspaces, reachable from Discord, WhatsApp, Telegram or a web dashboard. |
| [Cloudgeni-ai/opengeni](https://github.com/Cloudgeni-ai/opengeni) | TypeScript | 152 | 2026-09-18 | Self-hostable agent runtime with durable, replayable sessions, human approval gates and governed credentials inside managed sandboxes. |

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | TypeScript | 24330 | 2026-09-18 | The SDK For Browser Agents |
| [hyperledger-labs/acapy-java-client](https://github.com/hyperledger-labs/acapy-java-client) | Java | 18 | 2023-12-14 | Aries Cloud Agent Python Java Client Library |

#### Frameworks (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Python | 73181 | 2026-09-18 | Financial data platform for analysts, quants and AI agents |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Python | 41877 | 2026-09-18 | Build resilient agents |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Python | 30983 | 2026-09-17 | Build Real-Time Knowledge Graphs for AI Agents |
| [coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) | TypeScript | 21610 | 2026-07-29 | An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment lik |
| [google/adk-python](https://github.com/google/adk-python) | Python | 21568 | 2026-09-18 | Google's code-first Python toolkit for building, evaluating and deploying multi-agent LLM systems, with a runtime, tool layer and deployment paths. |
| [docker/docker-agent](https://github.com/docker/docker-agent) | Go | 3332 | 2026-09-18 | AI Agent Builder and Runtime by Docker Engineering |
| [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) | TypeScript | 3291 | 2026-09-18 | Framework to build resilient language agents as graphs |
| [liquidos-ai/AutoAgents](https://github.com/liquidos-ai/AutoAgents) | Rust | 755 | 2026-08-26 | Rust framework for building, deploying and coordinating multiple LLM agents with typed tools and pluggable runtimes. |
| [memgraph/skills](https://github.com/memgraph/skills) | — | 12 | 2026-08-05 | Agent skills that should help you build awesome stuff with Memgraph |

#### Unsorted (8)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) | — | 2353 | 2026-07-03 | Terraform & OpenTofu Skill for AI Agents - testing, modules, CI/CD, and production patterns |
| [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) | Python | 1836 | 2026-07-02 | Apple Silicon (MLX) port of Karpathy's autoresearch — autonomous AI research loops on Mac, no PyTorch required |
| [solana-foundation/pay](https://github.com/solana-foundation/pay) | Rust | 1776 | 2026-09-18 | Let your agents pay for any API |
| [lst97/claude-code-sub-agents](https://github.com/lst97/claude-code-sub-agents) | — | 1685 | 2025-08-15 | Collection of specialized AI subagents for Claude Code for personal use (full-stack development) |
| [FrancescoStabile/numasec](https://github.com/FrancescoStabile/numasec) | TypeScript | 791 | 2026-05-08 | The AI Agent for Cyber Security |
| [langtalks/swe-agent](https://github.com/langtalks/swe-agent) | Python | 641 | 2026-03-28 | 🤖 AI-powered software engineering multi-agent system with researcher and developer agents that automate code implementat |
| [zhsama/claude-sub-agent](https://github.com/zhsama/claude-sub-agent) | — | 590 | 2025-08-08 | AI-driven development workflow system built on Claude Code Sub-Agents |
| [bahdotsh/indxr](https://github.com/bahdotsh/indxr) | Rust | 73 | 2026-04-07 | A fast codebase indexer and knowledge wiki for AI agents |


<a id="llm-app-frameworks"></a>

---

## LLM App Frameworks

#### Frameworks (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 146587 | 2026-09-18 | The agent engineering platform |
| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | TypeScript | 18206 | 2026-09-18 | The agent engineering platform |
| [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | Python | 10735 | 2026-09-18 | An Open-Source Asynchronous Coding Agent |
| [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) | Rust | 8659 | 2026-09-18 | Rust framework for building LLM applications, with typed model clients, embeddings, vector-store adapters and agent pipelines. |

#### Unsorted (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | Dockerfile | 2567 | 2026-09-15 | AI coding workstation: Claude Code + web UI + 7 AI CLIs + headless browser + 50+ tools |
| [GWUDCAP/cc-sessions](https://github.com/GWUDCAP/cc-sessions) | JavaScript | 1554 | 2025-12-17 | an opinionated approach to productive development with Claude Code |
| [TheBushidoCollective/han](https://github.com/TheBushidoCollective/han) | TypeScript | 195 | 2026-09-08 | A curated marketplace of Claude Code plugins that embody the principles of ethical and professional software development |


<a id="rag-retrieval"></a>

---

## RAG Retrieval

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Python | 35711 | 2026-09-18 | Reasoning-based document index that builds a hierarchical tree over long PDFs so agents retrieve by navigating structure instead of vector similarity. |


<a id="model-serving"></a>

---

## Model Serving

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Python | 47495 | 2026-08-25 | Run frontier AI locally |


<a id="mcp-tooling"></a>

---

## MCP Tooling

#### Tools (7)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [oraios/serena](https://github.com/oraios/serena) | Python | 29562 | 2026-09-18 | MCP server that gives coding agents language-server-backed semantic code search and symbol-level editing across a whole repository. |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | TypeScript | 12540 | 2026-07-14 | MCP server that indexes a codebase into a vector store so coding agents retrieve semantically relevant code instead of grepping the tree. |
| [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) | TypeScript | 2993 | 2026-05-16 | A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with reac |
| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | Kotlin | 1459 | 2026-09-18 | The official Kotlin SDK for Model Context Protocol servers and clients |
| [bartolli/codanna](https://github.com/bartolli/codanna) | Rust | 742 | 2026-08-29 | Local code intelligence MCP server and CLI for AI coding agents |
| [stakpak/mcp](https://github.com/stakpak/mcp) | JavaScript | 18 | 2026-07-04 | Lightweight MCP server to give you access to the Stakpak API |
| [AikidoSec/aikido-claude-plugin](https://github.com/AikidoSec/aikido-claude-plugin) | — | 13 | 2026-09-11 |  |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [MCP-UI-Org/mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | TypeScript | 5167 | 2026-09-16 | SDK for serving and rendering interactive UI components over the Model Context Protocol, so MCP servers can return widgets instead of plain text. |

#### Unsorted (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ref-tools/ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp) | TypeScript | 1176 | 2026-09-14 | Helping coding agents never make mistakes working with public or private libraries without wasting the context window |


<a id="llm-evaluation"></a>

---

## LLM Evaluation

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | TypeScript | 25257 | 2026-09-18 | Declarative test runner for prompts, agents and RAG pipelines, with model comparison, red-teaming scans and CI integration. |


<a id="prompt-engineering"></a>

---

## Prompt Engineering

#### Reading & references (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [f/prompts.chat](https://github.com/f/prompts.chat) | HTML | 170635 | 2026-09-09 | Community collection of prompts for ChatGPT, Claude and Gemini, browsable on the web and self-hostable for a team. |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | — | 143702 | 2026-08-11 | Archive of published and leaked system prompts from Cursor, Devin, Claude Code, v0 and other commercial AI coding tools. |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Jupyter Notebook | 38223 | 2026-08-28 | Anthropic's hands-on tutorial teaching prompt engineering for Claude through progressively harder notebook exercises. |


<a id="coding-agents"></a>

---

## Coding Agents

#### Tools (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 106873 | 2026-09-18 | Agent toolkit with a unified LLM API, an agent loop, a TUI and a coding agent CLI you can embed in your own tools. |
| [xai-org/grok-build](https://github.com/xai-org/grok-build) | Rust | 26848 | 2026-09-17 | xAI's coding agent harness and fullscreen terminal UI, mouse-interactive and extensible with custom tools. |
| [generalaction/emdash](https://github.com/generalaction/emdash) | TypeScript | 5770 | 2026-09-18 | Desktop environment for running several coding agents in parallel, each isolated in its own git worktree or container, across any provider. |
| [anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable) | TypeScript | 4051 | 2026-04-11 | Open-source web app builder that drives local CLI coding agents such as Claude Code, Codex and Gemini CLI to build and deploy products. |
| [realiti4/claude-swap](https://github.com/realiti4/claude-swap) | Python | 2659 | 2026-09-08 | CLI and TUI for juggling multiple Claude Code accounts, rotating on rate limits and tracking usage across parallel sessions. |


<a id="agent-skills"></a>

---

## Agent Skills

#### Tools (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | JavaScript | 261549 | 2026-09-17 | Skill, instinct and memory pack that tunes coding-agent harnesses such as Claude Code, Codex and Cursor for research-first development. |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | JavaScript | 68883 | 2026-09-18 | Design guidance for AI coding agents: one skill, 24 commands and 61 deterministic detector rules that catch generic AI-generated frontend design. |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Python | 14996 | 2026-09-16 | Pipeline that converts documentation sites, GitHub repos and PDFs into Claude agent skills, flagging conflicts between the skills it generates. |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | Python | 3943 | 2026-01-26 | Claude Code extension pack of skills, sub-agents and hooks that persists session state in ledgers and handoffs so context survives compaction. |
| [Tiger3807861189/J-Space-Cognition-Suite](https://github.com/Tiger3807861189/J-Space-Cognition-Suite) | Python | 3010 | 2026-09-14 | Inference-time control suite of agent skills for deep reasoning, long-horizon work, verification and recovery across coding harnesses. |

#### Reading & references (14)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 264964 | 2026-09-18 | Matt Pocock's personal agent skills for real engineering work, published straight from his .agents directory. |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 176979 | 2026-09-10 | Anthropic's public Agent Skills repository, with reference skills for documents, frontend design and other common agent tasks. |
| [wshobson/agents](https://github.com/wshobson/agents) | Python | 39771 | 2026-09-14 | Marketplace of subagents, skills and plugins for Claude Code, Codex, Cursor, OpenCode and other coding harnesses. |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 34902 | 2026-09-16 | Reference Claude agents, skills and data connectors for investment banking, equity research, private equity and wealth-management workflows. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | JavaScript | 31301 | 2026-08-28 | Vercel's official collection of agent skills, packaging its framework and platform conventions for coding agents to follow. |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Python | 25484 | 2026-08-09 | Specification and documentation for the Agent Skills format, defining how portable skill packages are structured and loaded by agent harnesses. |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 25148 | 2026-09-18 | Plugin for Claude Code, Codex and Cursor that packages the Compound Engineering workflow as reusable planning, review and learning commands. |
| [google/skills](https://github.com/google/skills) | Python | 20119 | 2026-09-18 | Agent skills for Google products and technologies, packaging Google Cloud and developer-platform conventions for agent harnesses. |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | JavaScript | 11868 | 2026-09-14 | Coding-agent skill that runs a multi-phase security audit of a codebase and emits machine-readable findings, each independently verified before it is reported. |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | JavaScript | 6070 | 2026-01-06 | Reference Claude Code project configuration showing hooks, skills, subagents, slash commands and GitHub Actions workflows wired together. |
| [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | — | 4392 | 2025-10-30 | Pack of Claude Code sub-agent definitions arranged as an orchestrated development team, with role-specific agents for architecture, framework work and review. |
| [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) | Python | 3480 | 2026-09-17 | Searchable hub collecting community Claude skills, sub-agents, commands, hooks and plugin marketplaces for Claude Code, Claude Desktop and the Agent SDK. |
| [gokulsvision/Crewm8-Social-Media-Manager-Skill-Graph](https://github.com/gokulsvision/Crewm8-Social-Media-Manager-Skill-Graph) | — | 13 | 2026-05-01 | Agent-agnostic skill graph of 37 social media management skills covering content, analytics and community work across X, LinkedIn and TikTok. |
| [kurrent-io/skills](https://github.com/kurrent-io/skills) | JavaScript | 2 | 2026-07-15 | Agent skills for building with Kurrent, guiding coding assistants through event-sourced development on EventStore-style databases. |


<a id="llm-interfaces"></a>

---

## LLM Interfaces

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | 152457 | 2026-09-18 | Self-hosted chat interface for Ollama and OpenAI-compatible models, with RAG, tools, MCP and multi-user management. |
| [craft-ai-agents/craft-agents-oss](https://github.com/craft-ai-agents/craft-agents-oss) | TypeScript | 7188 | 2026-09-07 | Desktop agent workspace from the Craft team, built on the Claude Agent SDK, with parallel sessions, shareable runs and a document-centric UI. |

#### Libraries (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | Python | 15945 | 2026-09-18 | Agent-User Interaction protocol with SDKs for streaming agent state, tool calls and generative UI between backends and frontend applications. |
| [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) | TypeScript | 12201 | 2026-09-18 | React component library for AI chat interfaces, with streaming, tool-call rendering and shadcn and Radix primitives. |
| [thesysdev/openui](https://github.com/thesysdev/openui) | TypeScript | 9629 | 2026-09-18 | Open standard and runtime for generative UI, letting agents stream structured interface components instead of plain text. |
| [assistant-ui/tool-ui](https://github.com/assistant-ui/tool-ui) | TypeScript | 784 | 2026-08-31 | UI components for rendering AI tool calls and MCP results inside chat interfaces. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | TypeScript | 37405 | 2026-09-18 | Frontend stack for embedding agents in React, Angular and mobile apps, with generative-UI components and the AG-UI protocol it originated. |


<a id="agent-memory"></a>

---

## Agent Memory

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Python | 23884 | 2026-09-18 | Agent memory service with Python and TypeScript clients that distils past conversations and tool runs into memory an agent can learn from. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | Python | 16795 | 2026-09-18 | LLM-agnostic memory layer that turns agent conversations and execution traces into structured, persistent state on data infrastructure you already run. |


<a id="design-agents"></a>

---

## Design Agents

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | TypeScript | 7942 | 2026-09-17 | Local-first desktop app that turns a prompt into prototypes, slides or PDFs, using your own Claude, OpenAI, Gemini or Ollama credentials. |
| [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) | TypeScript | 6988 | 2026-06-29 | Open-source design agent for VS Code, Cursor and Windsurf that generates UI mockups, components and wireframes from natural-language prompts. |


<a id="container-orchestration"></a>

---

## Container Orchestration

#### Tools (17)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | Go | 127805 | 2026-09-18 | Production-Grade Container Scheduling and Management |
| [helm/helm](https://github.com/helm/helm) | Go | 30254 | 2026-09-17 | Package manager for Kubernetes that templates, versions, installs and rolls back application manifests as reusable charts. |
| [kedacore/keda](https://github.com/kedacore/keda) | Go | 10528 | 2026-09-18 | Kubernetes autoscaler that drives pod counts from external event sources such as queue depth, topic lag, cron or database queries, including scale to zero. |
| [stakater/Reloader](https://github.com/stakater/Reloader) | Go | 10417 | 2026-09-18 | A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with their associated |
| [kubernetes-sigs/external-dns](https://github.com/kubernetes-sigs/external-dns) | Go | 9092 | 2026-09-18 | Configure external DNS servers dynamically from Kubernetes resources |
| [k0sproject/k0s](https://github.com/k0sproject/k0s) | Go | 6484 | 2026-09-18 | Single-binary Kubernetes distribution with no host OS dependencies, aimed at edge, bare metal and embedded clusters. |
| [karmada-io/karmada](https://github.com/karmada-io/karmada) | Go | 5656 | 2026-09-18 | Kubernetes-native control plane that schedules and propagates workloads across many clusters and clouds behind a single API. |
| [devspace-sh/devspace](https://github.com/devspace-sh/devspace) | Go | 5187 | 2026-09-18 | Developer workflow CLI for Kubernetes that builds, deploys and hot-reloads your services directly inside a cluster. |
| [doitintl/kube-no-trouble](https://github.com/doitintl/kube-no-trouble) | Go | 3679 | 2026-09-17 | Scans live clusters, manifests and Helm releases for Kubernetes APIs deprecated or removed in a target version, so upgrades do not break workloads. |
| [kubernetes-sigs/kro](https://github.com/kubernetes-sigs/kro) | Go | 3040 | 2026-09-17 | Kubernetes Resource Orchestrator that groups related resources behind a single custom API with declarative dependency ordering. |
| [kubernetes-sigs/gateway-api](https://github.com/kubernetes-sigs/gateway-api) | Go | 2997 | 2026-09-18 | Repository for the next iteration of composite service (e.g |
| [kubernetes/git-sync](https://github.com/kubernetes/git-sync) | Shell | 2735 | 2026-07-28 | A sidecar app which clones a git repo and keeps it in sync with the upstream |
| [kubernetes-sigs/ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) | Go | 1046 | 2026-07-07 | Convert Ingress resources to Gateway API resources |
| [argoproj-labs/argocd-operator](https://github.com/argoproj-labs/argocd-operator) | Go | 889 | 2026-09-18 | A Kubernetes operator for managing Argo CD clusters |
| [gianlucam76/k8s-cleaner](https://github.com/gianlucam76/k8s-cleaner) | Go | 823 | 2026-09-17 | Cleaner is a Kubernetes controller that identifies unused or unhealthy resources, helping you maintain a streamlined and |
| [nats-io/nack](https://github.com/nats-io/nack) | Go | 253 | 2026-09-18 | Kubernetes controllers that manage NATS JetStream streams, consumers and accounts as custom resources. |
| [kubernetes-sigs/gwctl](https://github.com/kubernetes-sigs/gwctl) | Go | 135 | 2026-09-08 | gwctl is a command-line tool for managing and understanding Gateway API resources in your Kubernetes cluster |

#### Unsorted (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [philippemerle/KubeDiagrams](https://github.com/philippemerle/KubeDiagrams) | JavaScript | 2701 | 2026-09-01 | Generate Kubernetes architecture diagrams from Kubernetes manifest files, kustomization files, Helm charts, helmfiles, a |
| [linki/chaoskube](https://github.com/linki/chaoskube) | Go | 1938 | 2026-09-01 | chaoskube periodically kills random pods in your Kubernetes cluster |
| [hcavarsan/kftray](https://github.com/hcavarsan/kftray) | Rust | 1563 | 2026-09-18 | kubectl port-forward manager and reverse tunnel (ngrok-like) for exposing local services publicly, with TLS termination |
| [kubenetworks/kubevpn](https://github.com/kubenetworks/kubevpn) | Go | 1367 | 2026-09-17 | KubeVPN offers a Cloud Native Dev Environment that connects to kubernetes cluster network |
| [deggja/netfetch](https://github.com/deggja/netfetch) | Go | 448 | 2026-03-13 | Kubernetes tool for scanning clusters for network policies and identifying unprotected workloads |
| [FairwindsOps/gemini](https://github.com/FairwindsOps/gemini) | Go | 436 | 2026-09-16 | Automated backups of PersistentVolumeClaims in Kubernetes using VolumeSnapshots |
| [squat/generic-device-plugin](https://github.com/squat/generic-device-plugin) | Go | 387 | 2026-07-27 | A Kubernetes device plugin to schedule generic Linux devices |
| [doriordan/skuber](https://github.com/doriordan/skuber) | Scala | 332 | 2026-08-29 | A Scala Kubernetes client library |
| [DevOps-Nirvana/Kubernetes-Volume-Autoscaler](https://github.com/DevOps-Nirvana/Kubernetes-Volume-Autoscaler) | Python | 317 | 2024-05-30 | Autoscaling volumes for Kubernetes (with the help of Prometheus) |

#### Articles (6)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Get 3x the capacity for your Kubernetes Cluster for free, too good to be true?](https://medium.com/swlh/get-three-times-the-capacity-for-your-kubernetes-cluster-for-free-too-good-to-be-true-6f0c3032c296) | article | 2019-02 | infrastructure, kubernetes |
| [Scheduling in Kubernetes, Part 1: Node Affinity](https://medium.com/kokster/scheduling-in-kubernetes-part-1-node-affinity-b77c97556424) | article | 2019-02 | infrastructure, kubernetes |
| [Scheduling in Kubernetes, Part 2: Pod Affinity](https://medium.com/kokster/scheduling-in-kubernetes-part-2-pod-affinity-c2b217312ae1) | article | 2019-02 | infrastructure, kubernetes |
| [Kubernetes Chaos Engineering: Lessons Learned — Part 1](https://medium.com/skills-matter/kubernetes-chaos-engineering-lessons-learned-part-1-88c592cc670a) | article | 2018-11 | infrastructure, kubernetes |
| [Announcing the Kubernetes Ingress Controller for Kong](https://konghq.com/blog/kubernetes-ingress-controller-for-kong/) | article | 2018-05 | infrastructure, kubernetes |
| [Accessing Kubernetes Pods from outside the Cluster](http://alesnosek.com/blog/2017/02/14/accessing-kubernetes-pods-from-outside-of-the-cluster/) | article | 2018-04 | infrastructure, kubernetes |


<a id="iac"></a>

---

## IaC

#### Tools (12)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [hashicorp/terraform](https://github.com/hashicorp/terraform) | Go | 49684 | 2026-09-17 | Terraform enables you to safely and predictably create, change, and improve infrastructure |
| [opentofu/opentofu](https://github.com/opentofu/opentofu) | Go | 30212 | 2026-09-17 | OpenTofu lets you declaratively manage your cloud infrastructure |
| [gruntwork-io/terragrunt](https://github.com/gruntwork-io/terragrunt) | Go | 9838 | 2026-09-18 | Terragrunt is a flexible orchestration tool that allows Infrastructure as Code written in OpenTofu/Terraform to scale |
| [runatlantis/atlantis](https://github.com/runatlantis/atlantis) | Go | 9294 | 2026-09-17 | Terraform pull request automation that runs plan and apply from PR comments, with locking and approval gates so state changes stay reviewable. |
| [diggerhq/digger](https://github.com/diggerhq/digger) | Go | 5044 | 2026-09-15 | Digger is an open source IaC orchestration tool |
| [tfutils/tfenv](https://github.com/tfutils/tfenv) | Shell | 4969 | 2026-07-01 | Terraform version manager that installs multiple Terraform releases side by side and switches between them per directory from a .terraform-version file. |
| [terraform-docs/terraform-docs](https://github.com/terraform-docs/terraform-docs) | Go | 4825 | 2026-09-02 | Generate documentation from Terraform modules in various output formats |
| [antonbabenko/pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) | Shell | 3774 | 2026-09-17 | Collection of pre-commit hooks for Terraform repositories: formatting, validation, docs generation, linting and security scanning before a commit lands. |
| [cycloidio/terracognita](https://github.com/cycloidio/terracognita) | Go | 2391 | 2025-09-02 | Reads from existing public and private cloud providers (reverse Terraform) and generates your infrastructure as code on |
| [stategraph/stategraph](https://github.com/stategraph/stategraph) | OCaml | 1281 | 2026-09-18 | State backend for Terraform and OpenTofu that stores resources as a graph rather than one monolithic state file, removing whole-state locking. |
| [terraform-google-modules/terraform-google-bootstrap](https://github.com/terraform-google-modules/terraform-google-bootstrap) | HCL | 257 | 2026-09-08 | Bootstraps Terraform usage and related CI/CD in a new Google Cloud organization |
| [Azure/mapotf](https://github.com/Azure/mapotf) | Go | 60 | 2026-09-16 | Meta-programming tool for Terraform that matches HCL blocks and applies transformations, so users can patch settings like ignore_changes. |

#### Unsorted (7)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [busser/tfautomv](https://github.com/busser/tfautomv) | Go | 899 | 2026-09-02 | Generate Terraform moved blocks automatically for painless refactoring |
| [boltops-tools/terraspace](https://github.com/boltops-tools/terraspace) | Ruby | 720 | 2025-10-13 | Terraspace: The Terraform Framework |
| [leg100/otf](https://github.com/leg100/otf) | Go | 702 | 2026-07-16 | An open source alternative to terraform enterprise |
| [terralist/terralist](https://github.com/terralist/terralist) | Go | 520 | 2026-09-17 | Terraform Private Registry for modules and providers manageable from a REST API |
| [MatthewJohn/terrareg](https://github.com/MatthewJohn/terrareg) | Go | 347 | 2026-05-11 | Open source Terraform module registry with UI, optional Git integration and deep analysis |
| [shihanng/tfvar](https://github.com/shihanng/tfvar) | Go | 231 | 2026-03-11 | Terraform's variable definitions template generator |
| [busser/tftree](https://github.com/busser/tftree) | Go | 158 | 2026-08-28 | Display your Terraform module call stack in your terminal |


<a id="gitops"></a>

---

## Gitops

#### Tools (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | Go | 24179 | 2026-09-18 | Declarative Continuous Deployment for Kubernetes |
| [akuity/kargo](https://github.com/akuity/kargo) | Go | 3665 | 2026-09-18 | Continuous promotion engine for GitOps that models environments as stages and automates moving verified artifacts through them alongside Argo CD. |
| [terramate-io/terramate](https://github.com/terramate-io/terramate) | Go | 3630 | 2026-09-08 | Open-source Infrastructure as Code (IaC) orchestration platform: GitOps workflows, orchestration, code generation, obser |
| [argoproj/argo-rollouts](https://github.com/argoproj/argo-rollouts) | Go | 3584 | 2026-09-18 | Progressive Delivery for Kubernetes |
| [argoproj-labs/argocd-autopilot](https://github.com/argoproj-labs/argocd-autopilot) | Go | 1128 | 2025-12-16 | Argo-CD Autopilot |
| [argoproj-labs/terraform-provider-argocd](https://github.com/argoproj-labs/terraform-provider-argocd) | Go | 506 | 2026-09-17 | Terraform provider for Argo CD |
| [argoproj-labs/rollout-extension](https://github.com/argoproj-labs/rollout-extension) | TypeScript | 290 | 2026-06-30 | Argo Rollout visualization in Argo CD Web UI |
| [argoproj-labs/rollouts-plugin-trafficrouter-gatewayapi](https://github.com/argoproj-labs/rollouts-plugin-trafficrouter-gatewayapi) | Go | 160 | 2026-09-14 | The Argo Rollouts plugin implementing the Kubernetes Gateway API specification for using different traffic providers in |
| [SelfhostedPro/ArgoCD-Role-Composition](https://github.com/SelfhostedPro/ArgoCD-Role-Composition) | Smarty | 4 | 2025-11-04 | Example Repository utilizing roles to deploy applications to argo-cd clusters |


<a id="build-systems"></a>

---

## Build Systems

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [casey/just](https://github.com/casey/just) | Rust | 35858 | 2026-09-01 | Command runner that keeps project recipes in a justfile, in the spirit of make but without the build-system and dependency semantics. |
| [moonrepo/moon](https://github.com/moonrepo/moon) | Rust | 4107 | 2026-09-17 | A build system and monorepo management tool for the web ecosystem, written in Rust |
| [kunobi-ninja/kache](https://github.com/kunobi-ninja/kache) | Rust | 883 | 2026-09-18 | Content-addressed build cache for Rust and C/C++ that shares artifacts through local hardlinks and S3 instead of copying them. |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Parallelize tests in SBT on CircleCI](https://tanin.nanakorn.com/technical/2018/09/10/parallelise-tests-in-sbt-on-circle-ci.html) | article | 2018-09 | misc |
| [So, what's wrong with SBT?](http://www.lihaoyi.com/post/SowhatswrongwithSBT.html) | article | 2018-05 | fp-scala, language-runtimes |


<a id="monorepo-tooling"></a>

---

## Monorepo Tooling

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [moonrepo/proto](https://github.com/moonrepo/proto) | Rust | 1416 | 2026-09-17 | A pluggable multi-language version manager |


<a id="container-runtimes"></a>

---

## Container Runtimes

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Docker COPY: Dockerfile best practices](https://medium.com/the-code-review/docker-copy-dockerfile-best-practices-503704bee69f) | article | 2018-11 | infrastructure |
| [Digging into Docker layers](https://medium.com/@jessgreb01/digging-into-docker-layers-c22f948ed612) | article | 2018-10 | infrastructure |


<a id="package-registries"></a>

---

## Package Registries

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Publishing your Android, Kotlin or Java library to mavenCentral](https://medium.com/@vanniktech/publishing-your-android-kotlin-or-java-library-to-mavencentral-e22f343b9659) | article | 2018-06 | language-runtimes |


<a id="ci-cd"></a>

---

## CI CD

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [nektos/act](https://github.com/nektos/act) | Go | 72042 | 2026-08-09 | Runs GitHub Actions workflows locally in Docker containers, so a pipeline can be tested without pushing commits. |


<a id="feature-flags"></a>

---

## Feature Flags

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Unleash/unleash](https://github.com/Unleash/unleash) | TypeScript | 13813 | 2026-09-18 | Self-hosted feature flag platform with activation strategies, gradual rollouts, variants and SDKs for most server and client languages. |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | TypeScript | 8379 | 2026-09-18 | Warehouse-native feature flagging and A/B testing platform that runs experiment analysis directly against your existing data warehouse. |
| [Flagsmith/flagsmith](https://github.com/Flagsmith/flagsmith) | Python | 6560 | 2026-09-18 | Feature flag and remote config platform with segments, multivariate tests and client SDKs, run self-hosted or as a managed service. |


<a id="cloud-cost-management"></a>

---

## Cloud Cost Management

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [infracost/infracost](https://github.com/infracost/infracost) | Go | 12522 | 2026-09-17 | Estimates the cost delta of Terraform changes and posts the breakdown into pull requests, so cloud spend is reviewed before merge. |
| [opencost/opencost](https://github.com/opencost/opencost) | Go | 6750 | 2026-09-16 | CNCF project that allocates Kubernetes workload and cloud spend down to namespace, pod and label using Prometheus metrics. |


<a id="container-management"></a>

---

## Container Management

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker) | Go | 52859 | 2026-04-19 | Terminal UI for Docker and docker-compose that shows container state, logs and resource stats and runs common maintenance actions from one keyboard-driven view. |


<a id="code-sandboxes"></a>

---

## Code Sandboxes

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [engineer-man/piston](https://github.com/engineer-man/piston) | JavaScript | 2815 | 2026-07-31 | Code execution engine that runs untrusted snippets in isolated LXC containers across dozens of languages, behind a simple HTTP API. |


<a id="authentication"></a>

---

## Authentication

#### Tools (12)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [keycloak/keycloak](https://github.com/keycloak/keycloak) | Java | 36843 | 2026-09-18 | Open Source Identity and Access Management For Modern Applications and Services |
| [goauthentik/authentik](https://github.com/goauthentik/authentik) | Python | 25614 | 2026-09-18 | The authentication glue you need |
| [zitadel/zitadel](https://github.com/zitadel/zitadel) | Go | 15046 | 2026-09-18 | ZITADEL - Identity infrastructure, simplified for you |
| [ory/kratos](https://github.com/ory/kratos) | Go | 13880 | 2026-07-29 | Headless identity and user-management server covering registration, login, passkeys, OIDC, SAML, magic links and MFA through its own APIs. |
| [kanidm/kanidm](https://github.com/kanidm/kanidm) | Rust | 5385 | 2026-09-18 | Kanidm: A simple, secure, and fast identity management platform |
| [ory/oathkeeper](https://github.com/ory/oathkeeper) | Go | 3602 | 2026-07-27 | A cloud native Identity & Access Proxy / API (IAP) and Access Control Decision API that authenticates, authorizes, and m |
| [keycloakify/keycloakify](https://github.com/keycloakify/keycloakify) | TypeScript | 2578 | 2026-09-03 | 🔏 Keycloak theming for the modern web |
| [thomasdarimont/keycloak-extension-playground](https://github.com/thomasdarimont/keycloak-extension-playground) | Java | 725 | 2025-01-15 | Simple project environment for creating custom Keycloak extensions |
| [p2-inc/keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link) | Java | 427 | 2026-09-17 | Magic Link Authentication for Keycloak |
| [daniel-frak/keycloak-user-migration](https://github.com/daniel-frak/keycloak-user-migration) | Java | 374 | 2026-09-17 | A Keycloak plugin for migrating users from legacy systems |
| [cooperlyt/keycloak-phone-provider](https://github.com/cooperlyt/keycloak-phone-provider) | Java | 359 | 2025-03-04 | A Keycloak provider for phone and SMS |
| [adorsys/keycloak-ssi-deployment](https://github.com/adorsys/keycloak-ssi-deployment) | Shell | 14 | 2026-09-11 |  |

#### Videos (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [DevNation Live: A Deep Dive into Keycloak](https://www.youtube.com/watch?v=ZxpY_zZ52kU&feature=youtu.be) | video | 2019-01 | misc |


<a id="authorization-policy"></a>

---

## Authorization Policy

#### Tools (7)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [open-policy-agent/opa](https://github.com/open-policy-agent/opa) | Go | 12248 | 2026-09-18 | Open Policy Agent (OPA) is an open source, general-purpose policy engine |
| [kyverno/kyverno](https://github.com/kyverno/kyverno) | Go | 8165 | 2026-09-18 | Unified Policy as Code |
| [authzed/spicedb](https://github.com/authzed/spicedb) | Go | 7071 | 2026-09-17 | Google Zanzibar-inspired database that stores relationship tuples and answers fine-grained permission checks with consistency guarantees. |
| [permitio/opal](https://github.com/permitio/opal) | Python | 5511 | 2026-09-17 | Policy and data administration, distribution, and real-time updates on top of Policy Agents (OPA, Cedar, ...) |
| [kyverno/policy-reporter](https://github.com/kyverno/policy-reporter) | Go | 387 | 2026-09-18 | Monitoring and Observability Tool for the PolicyReport CRD with an optional UI |
| [kyverno/policy-reporter-ui](https://github.com/kyverno/policy-reporter-ui) | Go | 68 | 2026-09-14 | Policy Reporter UI |
| [Bisnode/opa-java-client](https://github.com/Bisnode/opa-java-client) | Java | 40 | 2024-10-28 |  |


<a id="supply-chain-security"></a>

---

## Supply Chain Security

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [renovatebot/renovate](https://github.com/renovatebot/renovate) | TypeScript | 22531 | 2026-09-18 | Home of the Renovate CLI: Cross-platform Dependency Automation by Mend.io |


<a id="vulnerability-scanning"></a>

---

## Vulnerability Scanning

#### Tools (7)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Go | 37970 | 2026-09-17 | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds and more |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | Go | 31283 | 2026-09-18 | Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on a simple YAML |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Go | 29373 | 2026-09-09 | Scanner that finds hardcoded secrets in git history, working trees and CI pipelines using configurable regex and entropy rules. |
| [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) | Python | 14833 | 2026-09-18 | Cloud security scanner that audits AWS, Azure, GCP and Kubernetes against CIS benchmarks and compliance frameworks, reporting hardening gaps. |
| [aquasecurity/tfsec](https://github.com/aquasecurity/tfsec) | Go | 7038 | 2026-03-25 | Tfsec is now part of Trivy |
| [opencve/opencve](https://github.com/opencve/opencve) | Python | 2838 | 2026-09-17 | Self-hosted CVE intelligence platform that ingests NVD and MITRE feeds and alerts on new or updated vulnerabilities matching your vendors and products. |
| [aquasecurity/trivy-operator](https://github.com/aquasecurity/trivy-operator) | Go | 1943 | 2026-09-16 | Kubernetes-native security toolkit |


<a id="cryptography-libs"></a>

---

## Cryptography Libs

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [InfiniteLoop360/Secure-Data-Transmission-System-SDTS---Defense-Grade](https://github.com/InfiniteLoop360/Secure-Data-Transmission-System-SDTS---Defense-Grade) | Python | 2 | 2025-12-19 | Demonstration secure transmission system combining AES-128 encryption, HMAC integrity checks and steganography in a Django app. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [openssl/openssl](https://github.com/openssl/openssl) | C | 30797 | 2026-09-18 | General-purpose TLS and cryptography library with command-line tooling, implementing SSL/TLS, X.509 and the common cipher and hash suites. |

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Cryptography—What Is It and How Does It Work?](https://medium.com/@ahjuice/cryptography-what-is-it-and-how-does-it-work-2a21a730d694) | article | 2018-10 | security |
| [The Empire Strikes Back with a Coordinated War on Crypto](https://hackernoon.com/the-empire-strikes-back-with-a-coordinated-war-on-crypto-bdd84fd2f854) | article | 2018-10 | security |
| [Secure Password Hashing](https://security.blogoverflow.com/2013/09/about-secure-password-hashing/) | article | 2018-04 | security |


<a id="network-security"></a>

---

## Network Security

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [cert-manager/cert-manager](https://github.com/cert-manager/cert-manager) | Go | 14082 | 2026-09-17 | Kubernetes controller that issues and renews X.509 certificates from Let's Encrypt, Vault or a private CA and keeps them current as Secrets. |

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Do VPNs Actually Protect Your Privacy?](https://medium.com/datadriveninvestor/do-vpns-actually-protect-your-privacy-5f98a9cec90a) | article | 2018-11 | security |
| [The CIA just lost control of its hacking arsenal. Here’s what you need to know.](https://medium.freecodecamp.org/the-cia-just-lost-control-of-its-hacking-arsenal-heres-what-you-need-to-know-ea69fc1ce38c) | article | 2018-11 | security |
| [How Spam Filtering Works: From SPF to DKIM to Blacklists](https://deliciousbrains.com/how-spam-filters-works/) | article | 2018-09 | security |


<a id="osint-reconnaissance"></a>

---

## Osint Reconnaissance

#### Tools (11)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [soxoj/maigret](https://github.com/soxoj/maigret) | Python | 37764 | 2026-09-18 | Collects a dossier on a person by checking a username against 3000+ sites and extracting whatever profile metadata it finds. |
| [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | Python | 22337 | 2026-04-13 | OSINT automation server that runs hundreds of reconnaissance modules to map an attack surface and enrich threat intelligence. |
| [projectdiscovery/subfinder](https://github.com/projectdiscovery/subfinder) | Go | 14450 | 2026-09-16 | Passive subdomain enumeration CLI that queries dozens of public sources to map a domain's attack surface. |
| [Datalux/Osintgram](https://github.com/Datalux/Osintgram) | Python | 14444 | 2026-09-14 | Interactive shell for analysing public Instagram accounts: followers, tagged photos, contact details and location history. |
| [jofpin/trape](https://github.com/jofpin/trape) | Python | 9009 | 2024-06-20 | People-tracking research tool that fingerprints and geolocates visitors, used to demonstrate OSINT and social-engineering exposure. |
| [lc/gau](https://github.com/lc/gau) | Go | 5096 | 2026-03-20 | Fetches every known URL for a domain from the Wayback Machine, Common Crawl and AlienVault OTX for recon and fuzzing. |
| [DedSecInside/TorBot](https://github.com/DedSecInside/TorBot) | Python | 4895 | 2026-09-18 | OSINT crawler for Tor hidden services that maps onion links and extracts page metadata, emails and phone numbers. |
| [IvanGlinkin/Fast-Google-Dorks-Scan](https://github.com/IvanGlinkin/Fast-Google-Dorks-Scan) | Shell | 1742 | 2025-07-10 | Automated Google dorking script that enumerates admin panels, exposed file types and path traversal candidates for a target site. |
| [MikeMeliz/TorCrawl.py](https://github.com/MikeMeliz/TorCrawl.py) | Python | 538 | 2026-06-29 | Crawls and extracts regular or onion web pages through the Tor network for investigative work. |
| [zuxu4n/Rosint](https://github.com/zuxu4n/Rosint) | JavaScript | 198 | 2026-08-26 | Reddit user intelligence tool that profiles an account's posting history, subreddits and activity patterns. |
| [thumpersecure/Telespotter](https://github.com/thumpersecure/Telespotter) | Rust | 79 | 2026-09-01 | Searches phone numbers across Google, Bing, DuckDuckGo and Dehashed, pulling names, locations and usernames out of the results. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [femiagbabiaka/shodan-rust](https://github.com/femiagbabiaka/shodan-rust) | Rust | 52 | 2024-08-05 | Rust client for the Shodan API, querying internet-wide host and service scan data from your own tools. |

#### Reading & references (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | — | 29608 | 2026-09-09 | Curated list of open-source intelligence resources covering people search, domain and IP recon, social media, and dark-web tooling. |
| [fastfire/deepdarkCTI](https://github.com/fastfire/deepdarkCTI) | — | 7285 | 2026-09-18 | Collection of cyber threat intelligence sources drawn from deep and dark web forums, markets and chat channels. |
| [Astrosp/Awesome-OSINT-List](https://github.com/Astrosp/Awesome-OSINT-List) | Shell | 4429 | 2026-09-16 | Curated catalogue of OSINT tools for reconnaissance, reverse search, red teaming and trust-and-safety work. |
| [apurvsinghgautam/dark-web-osint-tools](https://github.com/apurvsinghgautam/dark-web-osint-tools) | — | 2598 | 2026-08-07 | Curated list of OSINT tools and search engines for investigating dark web services and marketplaces. |


<a id="offensive-security"></a>

---

## Offensive Security

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [usestrix/strix](https://github.com/usestrix/strix) | Python | 63452 | 2026-09-17 | Open-source agents that run dynamic application penetration tests and report the vulnerabilities they can actually exploit. |

#### Reading & references (6)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | — | 120681 | 2026-07-26 | Index of awesome lists for hackers, penetration testers and security researchers, spanning fuzzing, reversing and bug bounty. |
| [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists) | PHP | 73586 | 2026-09-18 | Collection of wordlists, fuzzing payloads, default credentials and sensitive-data patterns used throughout security assessments. |
| [carpedm20/awesome-hacking](https://github.com/carpedm20/awesome-hacking) | — | 17087 | 2024-06-02 | Curated list of hacking tutorials, tools and resources spanning reverse engineering, exploitation, forensics and CTF practice. |
| [nagwww/s3-leaks](https://github.com/nagwww/s3-leaks) | Python | 458 | 2026-08-20 | Collection of documented S3 bucket misconfigurations and the techniques used to discover and exploit them. |
| [drtychai/wordlists](https://github.com/drtychai/wordlists) | — | 240 | 2024-06-25 | Aggregated wordlists pulled from common tools for discovery, enumeration, fuzzing and exploitation. |
| [bad-antics/nullsec-flipper-suite](https://github.com/bad-antics/nullsec-flipper-suite) | Python | 73 | 2026-03-11 | Collection of 430+ Flipper Zero files: BadUSB payloads, SubGHz captures, IR remotes and NFC and RFID dumps. |


<a id="privacy-tooling"></a>

---

## Privacy Tooling

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell | 57302 | 2026-09-10 | PowerShell script that removes pre-installed apps, disables telemetry and applies privacy and UI tweaks on Windows 10 and 11. |
| [abrahamjuliot/creepjs](https://github.com/abrahamjuliot/creepjs) | TypeScript | 2508 | 2026-06-11 | Browser fingerprinting research harness that surfaces device, engine and lie-detection signals to test anti-fingerprinting defences. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [fingerprintjs/fingerprintjs](https://github.com/fingerprintjs/fingerprintjs) | TypeScript | 28479 | 2026-09-17 | Browser fingerprinting library that derives a stable visitor identifier from device and browser signals for fraud detection. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio) | Python | 10929 | 2026-09-17 | Framework for detecting, redacting and anonymising PII across text, images and structured data using NLP and pattern recognisers. |


<a id="runtime-security"></a>

---

## Runtime Security

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [cilium/tetragon](https://github.com/cilium/tetragon) | C | 5011 | 2026-09-18 | eBPF-based runtime security observability for Kubernetes, recording process, file and network events in kernel space and enforcing policy at the syscall level. |


<a id="compliance-auditing"></a>

---

## Compliance Auditing

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [inspec/inspec](https://github.com/inspec/inspec) | Ruby | 3091 | 2026-09-18 | Compliance-as-code framework expressing infrastructure and security policy as executable Ruby tests, then auditing local or remote targets against those profiles. |


<a id="cli-frameworks"></a>

---

## CLI Frameworks

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [clap-rs/clap](https://github.com/clap-rs/clap) | Rust | 16711 | 2026-09-17 | A full featured, fast Command Line Argument Parser for Rust |
| [ksk001100/seahorse](https://github.com/ksk001100/seahorse) | Rust | 307 | 2026-05-07 | A minimal CLI framework written in Rust |


<a id="code-editors"></a>

---

## Code Editors

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [zed-industries/zed](https://github.com/zed-industries/zed) | Rust | 90478 | 2026-09-18 | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sit |
| [opral/flashtype](https://github.com/opral/flashtype) | TypeScript | 290 | 2026-09-09 | Markdown editor built to sit alongside Claude Code and Codex, editing the documents your coding agents write. |


<a id="linters-formatters"></a>

---

## Linters Formatters

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [terraform-linters/tflint](https://github.com/terraform-linters/tflint) | Go | 5817 | 2026-09-18 | A Pluggable Terraform Linter |
| [ayarotsky/diesel-guard](https://github.com/ayarotsky/diesel-guard) | Rust | 120 | 2026-09-14 | Linter for dangerous Postgres migration patterns in Diesel and SQLx |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Code formatting: scalafmt and the git pre-commit hook](https://medium.com/zyseme-technology/code-formatting-scalafmt-and-the-git-pre-commit-hook-3de71d099514) | article | 2018-09 | fp-scala, language-runtimes |


<a id="code-review-automation"></a>

---

## Code Review Automation

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [alibaba/open-code-review](https://github.com/alibaba/open-code-review) | Go | 36141 | 2026-09-18 | Code review service combining deterministic rule pipelines with an LLM agent to post line-level findings, shipping rulesets for NPE, thread-safety, XSS and SQL injection. |
| [mattzcarey/shippie](https://github.com/mattzcarey/shippie) | TypeScript | 2507 | 2026-09-13 | Extendable code review and QA agent that comments on pull requests and runs as a CI step or MCP-connected tool. |


<a id="documentation-generators"></a>

---

## Documentation Generators

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [octokatherine/readme.so](https://github.com/octokatherine/readme.so) | JavaScript | 4628 | 2026-03-13 | Drag-and-drop online editor for assembling project READMEs from prewritten markdown sections, with live preview and export. |
| [event-catalog/eventcatalog](https://github.com/event-catalog/eventcatalog) | TypeScript | 2900 | 2026-09-18 | Documentation site generator for event-driven architectures, cataloguing domains, services, events and schemas from AsyncAPI and OpenAPI definitions. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [juhaku/utoipa](https://github.com/juhaku/utoipa) | Rust | 4091 | 2026-09-16 | Code-first OpenAPI generation for Rust, deriving the schema from types and handler attributes at compile time and serving it through Swagger UI or RapiDoc. |


<a id="shells-terminals"></a>

---

## Shells Terminals

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [wavetermdev/waveterm](https://github.com/wavetermdev/waveterm) | Go | 22307 | 2026-09-10 | An open-source, AI-integrated, cross-platform terminal for seamless workflows |
| [direnv/direnv](https://github.com/direnv/direnv) | Go | 15451 | 2026-03-31 | Shell extension that loads and unloads environment variables per directory from an .envrc file, keeping project config out of your profile. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ratatui/ratatui](https://github.com/ratatui/ratatui) | Rust | 22638 | 2026-09-15 | A Rust crate for cooking up terminal user interfaces (TUIs) 👨‍🍳🐀 https://ratatui.rs |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Windows Command-Line: Backgrounder](https://blogs.msdn.microsoft.com/commandline/2018/06/20/windows-command-line-backgrounder/) | article | 2018-07 | misc |
| [Windows Command-Line: The Evolution of the Windows Command-Line](https://blogs.msdn.microsoft.com/commandline/2018/06/27/windows-command-line-the-evolution-of-the-windows-command-line/) | article | 2018-07 | misc |


<a id="diagramming"></a>

---

## Diagramming

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [d2lang/d2](https://github.com/d2lang/d2) | Go | 25459 | 2026-09-15 | Diagram scripting language and renderer that turns declarative text into architecture, sequence and entity diagrams. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [xyflow/xyflow](https://github.com/xyflow/xyflow) | TypeScript | 38416 | 2026-09-17 | React and Svelte libraries for node-based UIs such as flowcharts, pipeline editors and graph canvases, customisable out of the box. |

#### Reading & references (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 40999 | 2026-09-15 | 38 editorial diagram templates in self-contained HTML and SVG, for coding agents that need figures without Mermaid defaults. |


<a id="spec-driven-development"></a>

---

## Spec Driven Development

#### Tools (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [github/spec-kit](https://github.com/github/spec-kit) | Python | 137731 | 2026-09-17 | GitHub's toolkit for spec-driven development, generating the specs, plans and tasks that coding agents then implement. |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | TypeScript | 69065 | 2026-09-17 | Spec-driven development workflow for AI coding assistants, keeping change proposals and specs in the repo as the source of truth. |
| [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) | TypeScript | 3857 | 2025-09-07 | Spec-driven workflow for Claude Code that walks a feature from requirements to design, tasks and implementation, plus a shorter report-analyse-fix bug loop. |
| [spec-kitty/spec-kitty](https://github.com/spec-kitty/spec-kitty) | Python | 1632 | 2026-09-18 | Spec-driven development workflow for coding agents, with a Kanban dashboard, git worktrees and auto-merge across Claude, Cursor and Codex. |

#### Reading & references (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [snarktank/ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) | — | 7784 | 2025-11-05 | Markdown prompt workflow that turns a feature idea into a PRD and then a task list, which coding agents work through one checked item at a time. |


<a id="dev-environments"></a>

---

## Dev Environments

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [metalbear-co/mirrord](https://github.com/metalbear-co/mirrord) | Rust | 5333 | 2026-09-18 | Runs a local process as if it were a pod in a remote Kubernetes cluster, mirroring env vars, DNS, outgoing network and incoming traffic. |
| [txn2/kubefwd](https://github.com/txn2/kubefwd) | Go | 4171 | 2026-09-15 | Bulk port-forwards Kubernetes services to your workstation and maps them in /etc/hosts, so local code can call cluster services by their in-cluster names. |


<a id="notebooks"></a>

---

## Notebooks

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [polynote/polynote](https://github.com/polynote/polynote) | Jupyter Notebook | 4597 | 2026-01-27 | Polyglot notebook server built for Scala first, with editor-grade completions, reproducible dependency configuration and shared state across Scala, Python and SQL cells. |


<a id="optics-lenses"></a>

---

## Optics Lenses

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [optics-dev/Monocle](https://github.com/optics-dev/Monocle) | Scala | 1699 | 2026-09-05 | Optics library for Scala |


<a id="streaming-libs"></a>

---

## Streaming Libs

#### Articles (6)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [A streaming library with a superpower: FS2 and functional programming](https://medium.freecodecamp.org/a-streaming-library-with-a-superpower-fs2-and-functional-programming-6f602079f70a) | article | 2018-11 | misc |
| [Reactive Streams in Scala: Akka Streams vs Monix - Part 1](https://softwaremill.com/reactive-streams-in-scala-comparing-akka-streams-and-monix-part-1/) | article | 2018-09 | distributed-systems, fp-scala, frontend, language-runtimes |
| [Reactive Streams in Scala: Akka Streams vs Monix - Part 2](https://softwaremill.com/reactive-streams-in-scala-comparing-akka-streams-and-monix-part-2/) | article | 2018-09 | distributed-systems, fp-scala, frontend, language-runtimes |
| [Reactive Streams in Scala: Akka Streams vs Monix - Part 3](https://softwaremill.com/reactive-streams-in-scala-comparing-akka-streams-and-monix-part-3/) | article | 2018-09 | distributed-systems, fp-scala, frontend, language-runtimes |
| [Ring Buffer: The Data Structure Behind Disruptor](https://dzone.com/articles/ring-buffer-a-data-structure-behind-disruptor) | article | 2018-06 | distributed-systems |
| [Tagless Final Algebras and Streaming](https://typelevel.org/blog/2018/05/09/tagless-final-streaming.html) | article | 2018-05 | fp-scala, language-runtimes, typelevel |


<a id="type-classes-prelude"></a>

---

## Type Classes Prelude

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [arrow-kt/arrow](https://github.com/arrow-kt/arrow) | Kotlin | 6582 | 2026-09-17 | Functional companion library for Kotlin: typed errors and the Raise DSL, optics, immutable data helpers and structured-concurrency combinators. |
| [rust-num/num-traits](https://github.com/rust-num/num-traits) | Rust | 972 | 2026-07-07 | Numeric traits for generic mathematics in Rust, abstracting integers, floats and their operations behind shared interfaces. |

#### Articles (51)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [The Group Typeclass](https://www.inner-product.com/posts/define-group/) | article | 2019-05 | fp-scala, language-runtimes, typelevel |
| [Builder Pattern in Scala with Phantom Types](https://medium.com/@maximilianofelice/builder-pattern-in-scala-with-phantom-types-3e29a167e863) | article | 2019-01 | architecture-ddd, fp-scala, language-runtimes |
| [Type Erasure in Scala](http://squidarth.com/scala/types/2019/01/11/type-erasure-scala.html) | article | 2019-01 | fp-scala, language-runtimes |
| [Functors and Applicatives](https://hackernoon.com/functors-and-applicatives-b9af535b1440) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [Scrap Your Type Class Boilerplate (1/2)](http://aakashns.github.io/better-type-class.html) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [Scrap Your Type Class Boilerplate (2/2)](http://aakashns.github.io/better-type-class-2.html) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [The Contravariant Functor!](https://medium.com/@stephaneledorze/the-contravariant-functor-a7ae93e2eae0) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [The F-words: Functor and Friends](https://kubuszok.com/2018/the-f-words-functors-and-friends/) | article | 2018-12 | fp-scala, language-runtimes, typelevel |
| [Understanding Contramap](http://healsjnr.blogspot.com/2015/12/understanding-contramap.html) | article | 2018-12 | misc |
| [Explore Witnesses as an Alternative to Implicits](https://github.com/lampepfl/dotty/pull/5458) | article | 2018-11 | fp-scala, language-runtimes, typelevel |
| [Anatomy of a type class](http://geekocephale.com/blog/2018/10/05/typeclasses) | article | 2018-10 | fp-scala, language-runtimes, typelevel |
| [Anatomy of an algebra](http://geekocephale.com/blog/2018/10/06/algebras) | article | 2018-10 | misc |
| [Contravariant Functors — An Intuition](http://igstan.ro/posts/2013-10-31-contravariant-functors-an-intuition.html) | article | 2018-10 | fp-scala, language-runtimes, typelevel |
| [Chain – Replacing the List Monoid](https://typelevel.org/blog/2018/09/04/chain-replacing-the-list-monoid.html) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [How to translate your API with Shapeless](https://medium.com/azimolabs/how-to-translate-your-api-with-shapeless-2464337d31c0) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [Kinds of Types in Scala, Part 1: Types, what are they?](https://kubuszok.com/2018/kinds-of-types-in-scala-part-1/) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [Kinds of Types in Scala, Part 2: Take Type, return Type or Type parameters](https://kubuszok.com/2018/kinds-of-types-in-scala-part-2/) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [Kinds of Types in Scala, Part 3: Embedding some more info in a Type](https://kubuszok.com/2018/kinds-of-types-in-scala-part-3/) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [To tag a Type](https://medium.com/iterators/to-tag-a-type-88dc344bb66c) | article | 2018-09 | misc |
| [Traversing Object Graph with Shapeless (and Why You Should Write the Same Code Twice)](https://medium.com/@shanielh/traversing-object-graph-with-shapeless-and-why-you-should-write-the-same-code-twice-96fc09bc5be9) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [Typeclass Proposal](https://github.com/LukaJCB/typeclass-proposal) | article | 2018-09 | fp-scala, language-runtimes, typelevel |
| [Equivalence versus Equality](https://typelevel.org/blog/2017/04/02/equivalence-vs-equality.html) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [Generalized Algebraic Data Types in Scala](https://gist.github.com/smarter/2e1c564c83bae58c65b4f3f041bfb15f) | article | 2018-08 | fp-scala, language-runtimes |
| [Heterogeneous Lists and the Limits of the Java Type System](https://apocalisp.wordpress.com/2008/10/23/heterogeneous-lists-and-the-limits-of-the-java-type-system/) | article | 2018-08 | misc |
| [Higher-kinded types: the difference between giving up, and moving forward](https://typelevel.org/blog/2016/08/21/hkts-moving-forward.html) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [Tail Call Elimination in Scala Monads](https://apocalisp.wordpress.com/2011/10/26/tail-call-elimination-in-scala-monads/) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [Tail calls, @tailrec and trampolines](http://blog.richdougherty.com/2009/04/tail-calls-tailrec-and-trampolines.html) | article | 2018-08 | misc |
| [Typedapi](https://typelevel.org/blog/2018/06/15/typedapi.html) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [Who implements the typeclass instance?](https://typelevel.org/blog/2017/12/20/who-implements-typeclass.html) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [5 steps of creating your very first Type Class in Scala](https://medium.com/virtuslab/typeclasses-scala-be35c0ef0ee9) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Bits of Shapeless part 1: HLists](http://enear.github.io/2016/04/05/bits-shapeless-1-hlists/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Bits of Shapeless part 2: Generic Derivation](http://enear.github.io/2016/09/27/bits-of-shapeless-2/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 1: with type classes in min](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-1/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 1: with type classes in mind](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-1/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 2: implicit derivation](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-2/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 2: implicit derivation](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-2/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 3: conversions and implicit-based patterns](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-3/) | article | 2018-07 | architecture-ddd, fp-scala, language-runtimes, typelevel |
| [Implicits, type classes, and extension methods, part 4: understanding implicits](https://kubuszok.com/2018/implicits-type-classes-and-extension-methods-part-4/) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Rolling Your Own Monad To Deal With Nested Monads In Scala](http://www.geekabyte.io/2018/07/rolling-your-own-monad-to-deal-with.html) | article | 2018-07 | fp-scala, language-runtimes, typelevel |
| [Bits of Shapeless part 1: HLists](http://enear.github.io/2016/04/05/bits-shapeless-1-hlists/) | article | 2018-06 | fp-scala, language-runtimes, typelevel |
| [Bits of Shapeless part 2: Generic Derivation](https://enear.github.io/2016/09/27/bits-of-shapeless-2/) | article | 2018-06 | fp-scala, language-runtimes, typelevel |
| [Functors and things using Scala](http://blog.tmorris.net/posts/functors-and-things-using-scala/index.html) | article | 2018-06 | fp-scala, language-runtimes, typelevel |
| [The Aux Pattern](http://gigiigig.github.io/posts/2015/09/13/aux-pattern.html) | article | 2018-06 | architecture-ddd, frontend |
| [Type Classes and Generic Derivation](https://meta.plasm.us/posts/2015/11/08/type-classes-and-generic-derivation/) | article | 2018-06 | fp-scala, language-runtimes, typelevel |
| [Implicit Design Patterns in Scala](http://www.lihaoyi.com/post/ImplicitDesignPatternsinScala.html) | article | 2018-05 | architecture-ddd, fp-scala, language-runtimes, typelevel |
| [Implicit Implications (part 1): Implicit Parameters](https://functional.works-hub.com/learn/implicit-implications-part-1-implicit-parameters-098e0) | article | 2018-05 | fp-scala, language-runtimes, typelevel |
| [On Bifunctor IO and Java's Checked Exceptions](https://alexn.org/blog/2018/05/06/bifunctor-io.html) | article | 2018-05 | fp-scala, language-runtimes, typelevel |
| [Phantom Types in Scala](https://blog.codecentric.de/en/2016/02/phantom-types-scala/) | article | 2018-05 | fp-scala, language-runtimes |
| [Product with Serializable](https://typelevel.org/blog/2018/05/09/product-with-serializable.html) | article | 2018-05 | fp-scala, language-runtimes, typelevel |
| [Subtype type classes don't work](https://typelevel.org/blog/2016/09/30/subtype-typeclasses.html) | article | 2018-05 | fp-scala, language-runtimes, typelevel |
| [An ode to the Kind-Projector and Partial-Unification](https://www.ctheu.com/2018/04/12/an-ode-to-the-kind-projector-and-to-the-partial-unification-of-scala/) | article | 2018-04 | fp-scala, language-runtimes, typelevel |


<a id="ui-frameworks"></a>

---

## UI Frameworks

#### Frameworks (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | Rust | 39168 | 2026-09-16 | Rust framework for building fullstack web, desktop and mobile apps from one component tree, with SSR and hot reload. |
| [JetBrains/compose-multiplatform](https://github.com/JetBrains/compose-multiplatform) | Kotlin | 19368 | 2026-09-18 | Declarative Kotlin UI framework that shares one Compose codebase across desktop, Android, iOS and the web. |

#### Unsorted (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [medplum/medplum](https://github.com/medplum/medplum) | TypeScript | 2683 | 2026-09-18 | Medplum is a healthcare platform that helps you quickly develop high-quality compliant applications |
| [brightbeanxyz/brightbean-studio](https://github.com/brightbeanxyz/brightbean-studio) | Python | 2341 | 2026-09-18 | Open-source, self-hostable social media management platform |
| [openwallet-foundation/bifold-wallet](https://github.com/openwallet-foundation/bifold-wallet) | TypeScript | 204 | 2026-08-28 | Bifold is an extensible open-source React Native project designed to enhance the way we interact with digital identities |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Electron is a hulking monstrosity of a WORA framework, and it needs to be replaced.](https://medium.com/@boundarybreaker/electron-is-a-hulking-monstrosity-of-a-wora-framework-and-it-needs-to-be-replaced-25e9d849b0e) | article | 2018-10 | frontend |
| [Lessons learned from creating a rich-text editor with real-time collaboration](https://ckeditor.com/blog/Lessons-learned-from-creating-a-rich-text-editor-with-real-time-collaboration/) | article | 2018-10 | frontend |
| [What should replace Electron as a WORA framework?](https://medium.com/@boundarybreaker/what-should-replace-electron-as-a-wora-framework-911d969eddaa) | article | 2018-10 | frontend |
| [React Native: A retrospective from the mobile-engineering team at Udacity](https://engineering.udacity.com/react-native-a-retrospective-from-the-mobile-engineering-team-at-udacity-89975d6a8102) | article | 2018-07 | frontend |


<a id="component-systems"></a>

---

## Component Systems

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [longbridge/gpui-kit](https://github.com/longbridge/gpui-kit) | Rust | 14489 | 2026-09-18 | Cross-platform desktop UI component kit for Rust, built on the GPUI framework that powers the Zed editor. |
| [lodev09/react-native-true-sheet](https://github.com/lodev09/react-native-true-sheet) | TypeScript | 2063 | 2026-09-18 | React Native bottom sheet component backed by the platform's own sheet presentation on iOS and Android. |


<a id="design-systems"></a>

---

## Design Systems

#### Reading & references (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | — | 116483 | 2026-07-31 | Collection of DESIGN.md files distilled from well-known brand design systems, for steering coding agents toward a consistent UI. |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 27983 | 2026-09-14 | Specification for DESIGN.md, a file that gives coding agents a persistent, structured description of a product's visual identity and design system. |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [A developer’s guide to web design for non-designers](https://medium.freecodecamp.org/a-developers-guide-to-web-design-for-non-designers-1f64ce28c38d) | article | 2018-08 | frontend |
| [The UX behind designing better forms](https://uxdesign.cc/the-ux-behind-designing-better-forms-d6ebe7a817d2) | article | 2018-08 | frontend |


<a id="data-visualization"></a>

---

## Data Visualization

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [airbnb/visx](https://github.com/airbnb/visx) | TypeScript | 21053 | 2026-06-22 | Low-level React visualisation primitives built on D3, letting you compose charts from scales, axes and shapes. |
| [vega/vega](https://github.com/vega/vega) | JavaScript | 11991 | 2026-09-11 | Declarative visualisation grammar: JSON specifications compiled into interactive Canvas or SVG charts. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [visgl/deck.gl](https://github.com/visgl/deck.gl) | TypeScript | 14597 | 2026-09-18 | WebGL2 visualisation framework for large geospatial datasets, composing layered maps, point clouds and trip animations. |


<a id="graphics-3d"></a>

---

## Graphics 3d

#### Libraries (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [pmndrs/drei](https://github.com/pmndrs/drei) | JavaScript | 9874 | 2026-09-07 | Collection of helpers, abstractions and hooks for react-three-fiber: cameras, controls, loaders and materials. |
| [bitshifter/glam-rs](https://github.com/bitshifter/glam-rs) | Rust | 2052 | 2026-09-18 | Fast linear algebra library for games and graphics in Rust, with SIMD-accelerated vector, matrix and quaternion types. |
| [pmndrs/three-stdlib](https://github.com/pmndrs/three-stdlib) | JavaScript | 858 | 2026-06-26 | Stand-alone, transpilation-free port of the three.js examples - loaders, controls and post-processing - for Node and browsers. |

#### Reading & references (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [nasa/NASA-3D-Resources](https://github.com/nasa/NASA-3D-Resources) | — | 3792 | 2025-06-03 | NASA's public collection of 3D models, textures and images of spacecraft, instruments and planetary surfaces. |


<a id="animation-libraries"></a>

---

## Animation Libraries

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [greensock/GSAP](https://github.com/greensock/GSAP) | JavaScript | 28479 | 2026-04-13 | JavaScript animation platform for timeline-based motion, scroll-driven effects and SVG animation across browsers. |


<a id="rfcs"></a>

---

## RFCs

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [HTTP/3 Explained](https://http3-explained.haxx.se/en/) | article | 2018-12 | standards |
| [HTTP conditional requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Conditional_requests) | article | 2018-09 | standards |


<a id="oauth-oidc"></a>

---

## OAuth OIDC

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [polyvariant/sttp-oauth2](https://github.com/polyvariant/sttp-oauth2) | Scala | 80 | 2026-07-16 | OAuth2 client library implemented in Scala using sttp |

#### Articles (11)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [User Managed Access - UMA 2.0](https://medium.com/@dewni.matheesha/user-managed-access-uma-2-0-bcecb1d535b3) | article | 2019-03 | misc |
| [Identity, Claims, & Tokens – An OpenID Connect Primer, Part 1 of 3](https://developer.okta.com/blog/2017/07/25/oidc-primer-part-1) | article | 2018-10 | security, standards |
| [OAuth 2 Simplified](https://aaronparecki.com/oauth-2-simplified/) | article | 2018-10 | security |
| [OIDC in Action – An OpenID Connect Primer, Part 2 of 3](https://developer.okta.com/blog/2017/07/25/oidc-primer-part-2) | article | 2018-10 | security, standards |
| [What is the OAuth 2.0 Password Grant Type?](https://developer.okta.com/blog/2018/06/29/what-is-the-oauth2-password-grant) | article | 2018-10 | security, standards |
| [What's in a Token? – An OpenID Connect Primer, Part 3 of 3](https://developer.okta.com/blog/2017/08/01/oidc-primer-part-3) | article | 2018-10 | security, standards |
| [What the Heck is OAuth?](https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth) | article | 2018-09 | security, standards |
| [Refresh Tokens: When to Use Them and How They Interact with JWTs](https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/) | article | 2018-06 | security |
| [What Happens If Your JWT Is Stolen?](https://developer.okta.com/blog/2018/06/20/what-happens-if-your-jwt-is-stolen) | article | 2018-06 | security, standards |
| [Why JWTs Suck as Session Tokens](https://dzone.com/articles/stop-using-jwts-as-session-tokens) | article | 2018-06 | security |
| [JWT, JWS and JWE for Not So Dummies! (Part I)](https://medium.facilelogin.com/jwt-jws-and-jwe-for-not-so-dummies-b63310d201a3) | article | 2018-05 | security |

#### Videos (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [OAuth 2.0 and OpenID Connect (In Plain English)](https://www.youtube.com/watch?v=996OiexHze0) | video | 2018-10 | security |


<a id="cryptographic-standards"></a>

---

## Cryptographic Standards

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [ECDSA: The digital signature algorithm of a better internet](https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet/) | article | 2019-01 | algorithms, security |
| [The Illustrated TLS Connection](https://tls.ulfheim.net/) | article | 2018-10 | security |


<a id="interop-specs"></a>

---

## Interop Specs

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [reactive-streams/reactive-streams-jvm](https://github.com/reactive-streams/reactive-streams-jvm) | Java | 4880 | 2024-03-13 | Reactive Streams specification for the JVM, providing the Publisher/Subscriber interfaces and the TCK that Akka, RxJava and Project Reactor implement against. |

#### Reading & references (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ulid/spec](https://github.com/ulid/spec) | — | 10834 | 2024-07-20 | Canonical specification for ULID, a 128-bit lexicographically sortable identifier in Crockford base32, designed as a UUID replacement. |
| [cloudevents/spec](https://github.com/cloudevents/spec) | Python | 5905 | 2026-09-03 | CNCF specification for describing event data in a common envelope, with bindings for HTTP, Kafka, AMQP, MQTT and several SDKs. |
| [asyncapi/spec](https://github.com/asyncapi/spec) | JavaScript | 5306 | 2026-09-13 | Specification for describing event-driven APIs in a machine-readable document, covering channels, messages and bindings for Kafka, MQTT, AMQP and WebSockets. |


<a id="awesome-lists"></a>

---

## Awesome Lists

#### Reading & references (19)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | — | 507339 | 2026-09-02 | Root index of the awesome-list ecosystem, linking curated lists across languages, platforms and engineering disciplines. |
| [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | — | 79014 | 2026-09-17 | Topic-centric index of high-quality open datasets across science, government, finance and social data. |
| [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | Python | 74361 | 2026-09-17 | Curated list of machine learning frameworks, libraries and software, organised by programming language. |
| [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | Rust | 59411 | 2026-09-18 | Curated index of Rust libraries, applications and learning resources, organised by problem domain. |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | Python | 37829 | 2026-07-27 | Curated catalogue of 500 AI agent use cases by industry, each linked to an open-source implementation. |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | — | 30071 | 2026-08-21 | Curated list of autonomous AI agents and agent platforms, from the AutoGPT generation through current frameworks and commercial products. |
| [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | Python | 15599 | 2026-09-18 | Collection of runnable example AI applications — RAG pipelines, agents, MCP integrations and workflows — with full source for each use case. |
| [mfornos/awesome-microservices](https://github.com/mfornos/awesome-microservices) | — | 14514 | 2026-08-20 | Curated list of microservice architecture principles, patterns and technologies, organised by platform, language and infrastructure concern. |
| [dhamaniasad/awesome-postgres](https://github.com/dhamaniasad/awesome-postgres) | — | 12097 | 2026-08-31 | Curated list of PostgreSQL extensions, tooling, hosting options, client libraries and learning material across the ecosystem. |
| [lauris/awesome-scala](https://github.com/lauris/awesome-scala) | Python | 9244 | 2024-09-20 | Community-maintained list of Scala libraries, frameworks and tools organised by problem area, from web stacks to functional programming. |
| [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | HTML | 8886 | 2026-09-12 | Curated tracker of 3D Gaussian Splatting papers, code releases, datasets and viewers, kept in step with the research output. |
| [grpc-ecosystem/awesome-grpc](https://github.com/grpc-ecosystem/awesome-grpc) | — | 8358 | 2025-10-28 | Curated list of gRPC resources: implementations across languages, gateways, tooling, talks and protocol buffer ecosystem projects. |
| [shuaibiyy/awesome-tf](https://github.com/shuaibiyy/awesome-tf) | — | 6592 | 2026-09-09 | Curated list of Terraform and OpenTofu resources: modules, providers, testing and policy tools, CI integrations and learning material. |
| [korfuri/awesome-monorepo](https://github.com/korfuri/awesome-monorepo) | — | 5865 | 2024-08-16 | Curated list of monorepo build tools, version-control tooling and write-ups on how large organisations run a single repository. |
| [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | — | 5291 | 2026-09-16 | Long-running curated list of geospatial tooling and resources, spanning GIS libraries, earth-observation data, spatial analysis and remote-sensing machine learning. |
| [phodal/awesome-iot](https://github.com/phodal/awesome-iot) | Python | 4629 | 2026-09-16 | Curated list of IoT frameworks, libraries, operating systems and cloud platforms, organised across the device, gateway and backend layers. |
| [denji/awesome-http-benchmark](https://github.com/denji/awesome-http-benchmark) | — | 3774 | 2026-09-11 | Curated list of HTTP load-testing and benchmarking tools, from wrk and vegeta to HTTP/2 and HTTP/3 capable clients, plus REST debugging utilities. |
| [xyflow/awesome-node-based-uis](https://github.com/xyflow/awesome-node-based-uis) | — | 3676 | 2025-06-29 | Curated list of node-based UI resources: graph and flow editor libraries, visual programming environments, and write-ups on building node editors. |
| [mcxiaoke/awesome-kotlin](https://github.com/mcxiaoke/awesome-kotlin) | — | 2876 | 2026-08-05 | Curated list of Kotlin frameworks, libraries, tools and learning material, maintained with a regularly regenerated index by category. |

#### Unsorted (13)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ramnes/awesome-mongodb](https://github.com/ramnes/awesome-mongodb) | — | 2676 | 2026-09-18 | :leaves: A curated list of awesome MongoDB resources, libraries, tools and applications |
| [akuity/awesome-argo](https://github.com/akuity/awesome-argo) | — | 2490 | 2026-09-18 | A curated list of awesome projects and resources related to Argo (a CNCF graduated project) |
| [vaaaaanquish/Awesome-Rust-MachineLearning](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning) | JavaScript | 2268 | 2023-09-25 | This repository is a list of machine learning libraries written in Rust |
| [vonzosten/awesome-LangGraph](https://github.com/vonzosten/awesome-LangGraph) | JavaScript | 2000 | 2026-07-10 | An index of the LangChain + LangGraph ecosystem: concepts, projects, tools, templates, and guides for LLM & multi-agent |
| [passy/awesome-recursion-schemes](https://github.com/passy/awesome-recursion-schemes) | — | 1308 | 2024-04-25 | Resources for learning and using recursion schemes |
| [zed-industries/awesome-gpui](https://github.com/zed-industries/awesome-gpui) | Python | 1290 | 2026-09-18 | Awesome projects, built with or for GPUI! |
| [jbmusso/awesome-graph](https://github.com/jbmusso/awesome-graph) | — | 1273 | 2026-02-26 | A curated list of resources for graph databases and graph computing tools |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Python | 1237 | 2026-09-14 | Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them |
| [open-policy-agent/awesome-opa](https://github.com/open-policy-agent/awesome-opa) | — | 901 | 2026-09-18 | A curated list of OPA related tools, frameworks and articles |
| [philippemerle/Awesome-Kubernetes-Architecture-Diagrams](https://github.com/philippemerle/Awesome-Kubernetes-Architecture-Diagrams) | — | 571 | 2026-06-30 | Awesome Kubernetes Architecture Diagrams |
| [animo/awesome-self-sovereign-identity](https://github.com/animo/awesome-self-sovereign-identity) | — | 400 | 2025-11-11 | An awesome list of self-sovereign identity resources |
| [graphgeeks-lab/awesome-graph-universe](https://github.com/graphgeeks-lab/awesome-graph-universe) | — | 164 | 2025-08-26 | A curated list of resources for graph-related topics, including graph databases, analytics and science |
| [antonbabenko/awesome-terraform-compliance](https://github.com/antonbabenko/awesome-terraform-compliance) | — | 145 | 2026-07-29 | Awesome Terraform Compliance - tools, frameworks, and resources for implementing compliance, security, and governance co |


<a id="knowledge-graphs"></a>

---

## Knowledge Graphs

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Python | 119208 | 2026-09-16 | Turns a codebase with its docs, SQL schemas and PDFs into a queryable knowledge graph using deterministic AST parsing, exposed as a coding-agent skill. |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 47423 | 2026-09-18 | Client-side code intelligence engine that builds a queryable knowledge graph of a repository entirely in the browser. |

#### Reading & references (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) | TypeScript | 9230 | 2026-09-17 | Tools, agents and samples for Google Cloud Knowledge Catalog, which builds a metadata knowledge graph over structured and unstructured data. |


<a id="learning-resources"></a>

---

## Learning Resources

#### Reading & references (17)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 547996 | 2026-07-14 | Collection of step-by-step guides for rebuilding technologies from scratch: databases, git, compilers, shells and more. |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Python | 370597 | 2026-09-15 | Guide to designing large-scale systems, with worked examples, diagrams and Anki decks for system design interviews. |
| [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | Shell | 109821 | 2026-09-17 | Repository of computer science papers worth reading, organised by topic and used as the reading list for local chapters. |
| [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | — | 74031 | 2026-01-04 | Reading list of engineering blog posts and papers on the patterns behind scalable, reliable, large-scale systems. |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 66077 | 2026-09-18 | Worked examples and best practices for moving from ad-hoc prompting to disciplined agentic engineering with Claude Code. |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Jupyter Notebook | 52792 | 2026-09-16 | Notebooks and recipes from Anthropic showing practical Claude patterns: tool use, retrieval, vision and evaluation. |
| [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | — | 49771 | 2025-04-10 | Manual walkthrough of bootstrapping a Kubernetes cluster component by component, with no scripts or installers. |
| [DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns) | — | 48970 | 2024-10-25 | Curated list of software and architecture design patterns, from Gang of Four classics to cloud and microservice patterns. |
| [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | — | 46129 | 2026-07-08 | Course-style notes on designing systems at scale, covering storage, caching, messaging and interview preparation. |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | MDX | 32656 | 2026-09-15 | Hugging Face course on building LLM agents, working through smolagents, LangGraph and LlamaIndex with hands-on units and evaluations. |
| [dwmkerr/hacker-laws](https://github.com/dwmkerr/hacker-laws) | HTML | 27292 | 2026-09-10 | Reference collection of the laws, theories and principles developers cite — Conway, Brooks, Hyrum, Goodhart — each with a short explanation. |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | Jupyter Notebook | 21474 | 2026-09-17 | Code-first tutorials for taking GenAI agents from prototype to production, covering orchestration, memory, observability, evaluation and deployment. |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Jupyter Notebook | 20927 | 2026-09-18 | Notebooks for the book Machine Learning for Trading, running from data sourcing and feature engineering through backtesting to live execution. |
| [hmemcpy/milewski-ctfp-pdf](https://github.com/hmemcpy/milewski-ctfp-pdf) | TeX | 11693 | 2026-07-10 | Community-typeset PDF and LaTeX source of Bartosz Milewski's Category Theory for Programmers, which teaches category theory to working programmers. |
| [ryanburgess/engineer-manager](https://github.com/ryanburgess/engineer-manager) | JavaScript | 10725 | 2026-08-17 | Curated link collection for engineering managers covering one-on-ones, hiring, performance, career ladders and team-building. |
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | JavaScript | 10108 | 2026-09-02 | Collection of 45+ practical Claude Code tips from basics to advanced, plus a status line script and a plugin of everyday dev skills. |
| [sathishvj/awesome-gcp-certifications](https://github.com/sathishvj/awesome-gcp-certifications) | — | 4443 | 2026-03-30 | Collection of study material, practice questions and exam notes for Google Cloud certifications, organised per certification track. |

#### Unsorted (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ZoranPandovski/al-go-rithms](https://github.com/ZoranPandovski/al-go-rithms) | Jupyter Notebook | 1372 | 2024-06-18 | :musical_note: Algorithms written in different programming languages - https://zoranpandovski.github.io/al-go-rithms/ |
| [ZoranPandovski/design-patterns](https://github.com/ZoranPandovski/design-patterns) | Java | 391 | 2024-12-13 | :briefcase: Design patterns written in different programming languages :triangular_ruler: |

#### Articles (81)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Sending Millions of Webhooks in a smart way](https://medium.com/insiderengineering/sending-millions-of-webhooks-in-a-smart-way-f8b48fe2a5d) | article | 2023-08 | web-extraction |
| [Permutations as Functions](https://www.inner-product.com/posts/permutation-functions/) | article | 2019-05 | misc |
| [Solving the Rubik's Cube with Group Theory and Functional Programming](https://www.inner-product.com/posts/rubiks-intro/) | article | 2019-05 | algorithms |
| [Identify domain-model boundaries for each microservice](https://docs.microsoft.com/en-us/dotnet/standard/microservices-architecture/architect-microservice-container-applications/identify-microservice-domain-model-boundaries) | article | 2019-04 | architecture-ddd, distributed-systems, microservices |
| [Phone numbers must die](https://www.devever.net/~hl/e164) | article | 2019-04 | misc |
| [The 10 Operating System Concepts Software Developers Need to Remember](https://medium.com/cracking-the-data-science-interview/the-10-operating-system-concepts-software-developers-need-to-remember-480d0734d710) | article | 2019-04 | misc |
| [The Agile Crisis — a Primer](https://medium.com/@wischweh/the-agile-crisis-2016-9fb1c2f52af5) | article | 2019-03 | misc |
| [The Tao of Ticketing](https://tech.ticketmaster.com/2014/07/26/the-tao-of-ticketing/) | article | 2019-03 | misc |
| [Purely functional Parallelism in Scala](https://medium.com/@wiemzin/purely-functional-parallelism-in-scala-37ecb1e9999) | article | 2019-02 | fp-scala, language-runtimes |
| [The End Is Near for Mobile Apps - Part 1](https://medium.com/s/story/mobile-apps-will-disappear-soon-4b4e54f46eb8) | article | 2019-01 | misc |
| [The End is Near for Mobile Apps - Part 2](https://medium.com/predict/the-end-is-near-for-mobile-apps-part-2-926ec187e435) | article | 2019-01 | misc |
| [The TypeScript Tax](https://medium.com/javascript-scene/the-typescript-tax-132ff4cb175b) | article | 2019-01 | misc |
| [Why Open Source Failed](https://medium.com/@johnmark/why-open-source-failed-6cae5d6a9f6) | article | 2019-01 | misc |
| [You don’t understand your Software Engineers](https://medium.com/@amandoabreu/you-dont-understand-your-software-engineers-53442ca0805a) | article | 2019-01 | misc |
| [Good code is Short, Simple, and Robust](https://medium.com/swlh/good-code-is-short-simple-and-robust-52b0a0abf2e8) | article | 2018-12 | misc |
| [How To Handle Errors On JVM Faster](https://medium.com/@alexmaisiura/how-to-handle-errors-on-jvm-faster-a1449020739) | article | 2018-12 | compilers, language-runtimes |
| [Why x86 won’t survive](https://medium.com/datadriveninvestor/why-x86-wont-survive-220f94c6c5ef) | article | 2018-12 | misc |
| [5 themes for Scala programming in 2018](https://medium.com/skills-matter/5-themes-for-scala-in-2018-130148776fd8) | article | 2018-11 | fp-scala, language-runtimes |
| [Immutable State in Real World](https://medium.com/@wiemzin/immutable-state-in-real-world-e2a3eef2f1b4) | article | 2018-11 | misc |
| [Anatomy of functional programming](http://geekocephale.com/blog/2018/10/08/fp) | article | 2018-10 | misc |
| [Approaches to JSON internationalisation (i18n)](https://www.drzon.net/posts/approaches-to-json-internationalisation-i18n/) | article | 2018-10 | misc |
| [Blockchain is not only crappy technology but a bad vision for the future](https://medium.com/@kaistinchcombe/decentralized-and-trustless-crypto-paradise-is-actually-a-medieval-hellhole-c1ca122efdec) | article | 2018-10 | fp-rust, language-runtimes, observability |
| [Falsehoods Programmers Believe About Phone Numbers](https://github.com/googlei18n/libphonenumber/blob/master/FALSEHOODS.md) | article | 2018-10 | misc |
| [Git Workflows](https://medium.com/@jurtzmarcel/git-workflows-cb0c023ca88) | article | 2018-10 | misc |
| [Greedy, Brittle, Opaque and Shallow: The Downsides to Deep Learning](https://www.wired.com/story/greedy-brittle-opaque-and-shallow-the-downsides-to-deep-learning/) | article | 2018-10 | ai-applications, misc |
| [How Netflix works: the (hugely simplified) complex stuff that happens every time you hit Play](https://medium.com/refraction-tech-everything/how-netflix-works-the-hugely-simplified-complex-stuff-that-happens-every-time-you-hit-play-3a40c9be254b) | article | 2018-10 | misc |
| [Raytracing](https://tmcw.github.io/literate-raytracer/) | article | 2018-10 | misc |
| [Why the net giants are worried about the Web 3.0](https://medium.com/@matteozago/why-the-net-giants-are-worried-about-the-web-3-0-44b2d3620da5) | article | 2018-10 | misc |
| [Deep Dive into Math Behind Deep Networks](https://towardsdatascience.com/https-medium-com-piotr-skalski92-deep-dive-into-deep-networks-math-17660bc376ba) | article | 2018-09 | misc |
| [Effect Extensions Pattern](https://akmetiuk.com/posts/2018-08-18-effect-extensions.html) | article | 2018-09 | architecture-ddd |
| [GeoMapping and the Travelling Salesman Problem](https://crondev.blog/2018/08/17/geomapping-solution-by-solving-the-travelling-salesman-problem/) | article | 2018-09 | algorithms |
| [Markov Chains](http://setosa.io/ev/markov-chains/) | article | 2018-09 | algorithms |
| [Strings Are Evil](https://hackernoon.com/strings-are-evil-a803d05e5ce3) | article | 2018-09 | misc |
| [Strings are not the Type you are looking for](https://pedrorijo.com/blog/strings-as-types/) | article | 2018-09 | misc |
| [10 Common Software Architectural Patterns in a nutshell](https://towardsdatascience.com/10-common-software-architectural-patterns-in-a-nutshell-a0b47a1e9013) | article | 2018-08 | architecture-ddd |
| [Essential Cheat Sheets for Machine Learning and Deep Learning Engineers](https://startupsventurecapital.com/essential-cheat-sheets-for-machine-learning-and-deep-learning-researchers-efb6a8ebd2e5) | article | 2018-08 | ai-applications |
| [Goodbye, Object Oriented Programming](https://medium.com/@cscalfani/goodbye-object-oriented-programming-a59cda4c0e53) | article | 2018-08 | misc |
| [How to Automate Surveillance Easily with Deep Learning](https://medium.com/nanonets/how-to-automate-surveillance-easily-with-deep-learning-4eb4fa0cd68d) | article | 2018-08 | ai-applications |
| [How To Prevent Coding “Heroes” From Destroying The Team](https://hackernoon.com/thoughts-on-software-development-heroes-5ec656c2e31a) | article | 2018-08 | misc |
| [Machine Learning is Fun! Part 1 - What is machine learning?](https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 2 - Making Smarter Guesses](https://medium.com/@ageitgey/machine-learning-is-fun-part-2-a26a10b68df3) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 3 - Deep Learning and Convolutional Neural Networks](https://medium.com/@ageitgey/machine-learning-is-fun-part-3-deep-learning-and-convolutional-neural-networks-f40359318721) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 4 - Modern Face Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 5 - Language Translation with Deep Learning and the Magic of Sequences](https://medium.com/@ageitgey/machine-learning-is-fun-part-5-language-translation-with-deep-learning-and-the-magic-of-sequences-2ace0acca0aa) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 6 - How to do Speech Recognition with Deep Learning](https://medium.com/@ageitgey/machine-learning-is-fun-part-6-how-to-do-speech-recognition-with-deep-learning-28293c162f7a) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 7 - Abusing Generative Adversarial Networks to Make 8-bit Pixel Art](https://medium.com/@ageitgey/abusing-generative-adversarial-networks-to-make-8-bit-pixel-art-e45d9b96cee7) | article | 2018-08 | ai-applications |
| [Machine Learning is Fun! Part 8 - How to Intentionally Trick Neural Networks](https://medium.com/@ageitgey/machine-learning-is-fun-part-8-how-to-intentionally-trick-neural-networks-b55da32b7196) | article | 2018-08 | ai-applications |
| [Pros and cons of functional programming](https://itnext.io/pros-and-cons-of-functional-programming-32cdf527e1c2) | article | 2018-08 | misc |
| [Shared State in Functional Programming](https://typelevel.org/blog/2018/06/07/shared-state-in-fp.html) | article | 2018-08 | fp-scala, language-runtimes, typelevel |
| [The Angry Programmer](https://hackernoon.com/the-angry-programmer-52a93bfcbc3c) | article | 2018-08 | misc |
| [The Doctor And The Scalpel](https://hackernoon.com/the-doctor-and-the-scalpel-78656f508c9a) | article | 2018-08 | misc |
| [This is How Google will Collapse](https://hackernoon.com/how-google-collapsed-b6ffa82198ee) | article | 2018-08 | misc |
| [We fired our top talent. Best decision we ever made.](https://medium.freecodecamp.org/we-fired-our-top-talent-best-decision-we-ever-made-4c0a99728fde) | article | 2018-08 | misc |
| [Why Blockchain is Hard](https://medium.com/@jimmysong/why-blockchain-is-hard-60416ea4c5c) | article | 2018-08 | misc |
| [Why Developers Become Frustrated And Companies Can’t Find Talent](https://codeburst.io/why-developers-become-frustrated-and-companies-cant-find-talent-c4114d8b72ac) | article | 2018-08 | fp-rust, language-runtimes |
| [Why DRY can be misleading](https://medium.com/@cummingsi1993/why-dry-can-be-misleading-c3986ad1240e) | article | 2018-08 | misc |
| [Case Study - Solve Crosswords Puzzle](https://mostafa-asg.github.io/post/solve-hackerrank-crosswords-101/) | article | 2018-07 | misc |
| [How not to be a mediocre developer!](https://hackernoon.com/how-not-to-be-a-mediocre-developer-c59a49f97fc5) | article | 2018-07 | misc |
| [Loop vs System.arraycopy](https://faisalferoz.wordpress.com/2007/12/24/loop-vs-systemarraycopy/) | article | 2018-07 | misc |
| [Teaching Evolution With Genetic Algorithms](http://codeninja.blog/2018/teaching-evolution/) | article | 2018-07 | algorithms |
| [The Trove Library: Using Primitive Collections for Performance](http://java-performance.info/primitive-types-collections-trove-library/) | article | 2018-07 | language-runtimes |
| [Urban Performance legends - Revisited](https://www.ibm.com/developerworks/library/j-jtp09275/) | article | 2018-07 | language-runtimes |
| [Bitwise Operators in C and C++](https://www.cprogramming.com/tutorial/bitwise_operators.html) | article | 2018-06 | misc |
| [HEVC, VP9 and The Future of Video Codecs](https://headjack.io/blog/hevc-vp9-vp10-dalaa-thor-netvc-future-video-codecs/) | article | 2018-06 | misc |
| [How to navigate the deceptively simple Singleton pattern](https://www.javaworld.com/article/2073352/core-java/core-java-simply-singleton.html) | article | 2018-06 | architecture-ddd |
| [Rank Hotness With Newton’s Law of Cooling](https://www.evanmiller.org/rank-hotness-with-newtons-law-of-cooling.html) | article | 2018-06 | misc |
| [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets (No Excuses!)](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) | article | 2018-06 | misc |
| [The char Type in Java is Broken](https://codeahoy.com/2016/05/08/the-char-type-in-java-is-broken/) | article | 2018-06 | misc |
| [Understanding Bitwise Operators](https://code.tutsplus.com/articles/understanding-bitwise-operators--active-11301) | article | 2018-06 | misc |
| [10 Reasons to Learn Scala and FP](https://dzone.com/articles/10-reasons-to-learn-scala-and-functional-programmi?oid=facebook) | article | 2018-05 | fp-scala, language-runtimes |
| [Checked exceptions I love you, but you have to go](https://testing.googleblog.com/2009/09/checked-exceptions-i-love-you-but-you.html) | article | 2018-05 | misc |
| [Evolving away from Entities](http://www.michaelnygard.com/blog/2018/04/evolving-away-from-entities/) | article | 2018-05 | misc |
| [Google Duplex: An AI System for Accomplishing Real World Tasks Over the Phone](https://ai.googleblog.com/2018/05/duplex-ai-system-for-natural-conversation.html) | article | 2018-05 | ai-applications |
| [How Linux Programs are Executed](https://lwn.net/Articles/630727/) | article | 2018-05 | frontend, kernel-systems |
| [How Linux Programs are Executed: ELF Binaries](https://lwn.net/Articles/631631/) | article | 2018-05 | frontend, kernel-systems |
| [Services by Lifecycle](http://www.michaelnygard.com/blog/2018/01/services-by-lifecycle/) | article | 2018-05 | misc |
| [Tearing apart printf()](http://www.maizure.org/projects/printf/index.html) | article | 2018-05 | kernel-systems |
| [The Entity Service Antipattern](http://www.michaelnygard.com/blog/2017/12/the-entity-service-antipattern/) | article | 2018-05 | architecture-ddd |
| [The Magpie Developer](https://blog.codinghorror.com/the-magpie-developer/) | article | 2018-05 | misc |
| [Zero-Overhead Tree Processing with the Visitor Pattern](http://www.lihaoyi.com/post/ZeroOverheadTreeProcessingwiththeVisitorPattern.html) | article | 2018-05 | architecture-ddd, fp-scala, language-runtimes |
| [Types and Functions](https://bartoszmilewski.com/2014/11/24/types-and-functions/) | article | 2018-04 | misc |

#### Videos (12)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Microservices and Rules Engines – a blast from the past](https://channel9.msdn.com/Events/NDC/NDC-Oslo-2017/BRK03) | video | 2019-04 | distributed-systems, microservices |
| ["The Mess We're In" by Joe Armstrong](https://www.youtube.com/watch?v=lKXe3HUG2l4) | video | 2019-04 | misc |
| [How to Focus Intensely](https://www.youtube.com/watch?v=wfKv2qG8d_w) | video | 2019-01 | misc |
| [Visualising Software Architecture with the C4 Model](https://www.youtube.com/watch?v=1zYK615kepE) | video | 2018-11 | architecture-ddd |
| [Critical .zip vulnerabilities](https://www.youtube.com/watch?v=Ry_yb5Oipq0) | video | 2018-06 | misc |
| [Brad Whittington - Getting Superbalist.com through Black Friday](https://www.youtube.com/watch?v=syDY6HCZgRo) | video | 2018-05 | misc |
| [Existential Types — Make OOP Great Again!](https://www.youtube.com/watch?v=6j5kZj17aUw) | video | 2018-05 | misc |
| [Intervals: Unifying Uncertainty, Ranges, and Loops](https://www.youtube.com/watch?v=c5Q-BUPBQIY) | video | 2018-05 | misc |
| [Leveraging Spire for complex time allocation logic](https://www.youtube.com/watch?v=m663bWN8KkY) | video | 2018-05 | observability |
| [Spire by Example](https://www.youtube.com/watch?v=EGwVDyyEeI8) | video | 2018-05 | misc |
| [The Paved PaaS To NodeJS Microservices](https://www.youtube.com/watch?v=QcNqfvMeWow) | video | 2018-05 | distributed-systems, microservices |
| [Uniting Church and State: FP and OO Together](https://www.youtube.com/watch?v=IO5MD62dQbI) | video | 2018-05 | misc |


<a id="interview-prep"></a>

---

## Interview Prep

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Bet you can’t solve this Google interview question.](https://medium.freecodecamp.org/bet-you-cant-solve-this-google-interview-question-4a6e5a4dc8ee) | article | 2019-05 | interviewing |
| [How to conduct a good Programming Interview](http://www.lihaoyi.com/post/HowtoconductagoodProgrammingInterview.html) | article | 2018-06 | fp-scala, interviewing, language-runtimes |


<a id="investigative-data"></a>

---

## Investigative Data

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [opensanctions/opensanctions](https://github.com/opensanctions/opensanctions) | Python | 809 | 2026-09-18 | Crawlers and pipelines behind an open database of international sanctions targets, politically exposed persons and related companies. |
| [openaleph/openaleph](https://github.com/openaleph/openaleph) | JavaScript | 131 | 2026-09-16 | Investigative data platform that stores large document and entity collections and makes them searchable for collaborative research. |
| [opensanctions/everypolitician.org](https://github.com/opensanctions/everypolitician.org) | TypeScript | 22 | 2026-06-22 | Site and dataset mapping political office-holders across countries, published as reusable structured data. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [opensanctions/followthemoney](https://github.com/opensanctions/followthemoney) | Python | 99 | 2026-09-03 | Data model and toolkit for investigative entity graphs, used by OpenSanctions, OpenAleph and other financial-crime tools. |


<a id="computer-vision"></a>

---

## Computer Vision

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [NVlabs/PointWorld](https://github.com/NVlabs/PointWorld) | Python | 531 | 2026-05-17 | NVIDIA research release for scaling point-based 3D world models used in in-the-wild robotic manipulation. |

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Python | 61748 | 2026-09-18 | YOLO model family and training toolkit for object detection, segmentation, classification, pose estimation and tracking. |
| [open-edge-platform/anomalib](https://github.com/open-edge-platform/anomalib) | Python | 6171 | 2026-09-18 | Anomaly detection library for images, bundling current algorithms with experiment tracking and edge inference through OpenVINO. |

#### Reading & references (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [coderonion/awesome-yolo-object-detection](https://github.com/coderonion/awesome-yolo-object-detection) | — | 1789 | 2025-05-31 | Curated list of YOLO object detection projects, deployment runtimes and the datasets used to train them. |
| [visionxiang/awesome-camouflaged-object-detection](https://github.com/visionxiang/awesome-camouflaged-object-detection) | — | 489 | 2026-09-17 | Curated list of papers, datasets and benchmarks for camouflaged and concealed object detection. |
| [Awesome-COD/awesome-camouflage](https://github.com/Awesome-COD/awesome-camouflage) | — | 57 | 2026-09-01 | Curated list of research on camouflaged and concealed object detection, covering methods, datasets and benchmarks. |


<a id="information-extraction"></a>

---

## Information Extraction

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [urchade/GLiNER](https://github.com/urchade/GLiNER) | Python | 3790 | 2026-09-08 | Lightweight named-entity recognition model that extracts arbitrary entity types from text given only their labels. |
| [fastino-ai/GLiNER2](https://github.com/fastino-ai/GLiNER2) | Python | 1929 | 2026-09-15 | Schema-based information extraction model that unifies entity recognition, classification and structured field extraction in one pass. |


<a id="model-optimization"></a>

---

## Model Optimization

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [p-e-w/heretic](https://github.com/p-e-w/heretic) | Python | 31763 | 2026-09-05 | Automatic abliteration tool that removes refusal behaviour from transformer language models without retraining them. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | Jupyter Notebook | 34513 | 2026-09-18 | Layer-by-layer inference scheduler that runs 70B-parameter language models on a single 4GB GPU. |


<a id="web-crawlers"></a>

---

## Web Crawlers

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | TypeScript | 181846 | 2026-09-18 | Crawl, scrape and search API that turns websites into clean markdown or structured data for LLM and RAG pipelines. |
| [instaloader/instaloader](https://github.com/instaloader/instaloader) | Python | 13394 | 2026-09-06 | Python CLI and library that downloads Instagram posts, stories and profile metadata, including whole accounts, hashtags and saved feeds. |

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apify/crawlee](https://github.com/apify/crawlee) | TypeScript | 25833 | 2026-09-17 | Node.js crawling library with request queues, proxy rotation and storage, working across Playwright, Puppeteer, Cheerio and raw HTTP. |
| [spider-rs/spider](https://github.com/spider-rs/spider) | Rust | 2721 | 2026-09-16 | Low-latency web crawling library in Rust for collecting page data at scale, with optional headless Chrome rendering. |


<a id="browser-automation"></a>

---

## Browser Automation

#### Tools (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) | Rust | 27355 | 2026-09-18 | Headless browser built for AI agents and scraping, driving Chrome over CDP with anti-detection defaults. |
| [FlareSolverr/FlareSolverr](https://github.com/FlareSolverr/FlareSolverr) | Python | 15632 | 2026-09-12 | Proxy server that solves Cloudflare and anti-bot challenges in a real browser and hands the cleared session back to your scraper. |
| [daijro/camoufox](https://github.com/daijro/camoufox) | C++ | 11984 | 2026-09-14 | Firefox fork with patched fingerprinting surfaces, driven through Playwright for scraping sites that block headless browsers. |
| [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | JavaScript | 11082 | 2026-09-17 | Stealth headless browser for AI agents that drops into Puppeteer or Playwright and clears bot-detection and Cloudflare checks. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 115076 | 2026-09-15 | Python library that lets LLM agents drive a real browser, turning page state into observations and model output into actions. |


<a id="content-extraction"></a>

---

## Content Extraction

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [adbar/trafilatura](https://github.com/adbar/trafilatura) | Python | 6833 | 2026-09-11 | Python library and CLI that extracts main text, comments and metadata from web pages for corpus and RAG pipelines. |

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [codelucas/newspaper](https://github.com/codelucas/newspaper) | Python | 15162 | 2026-09-15 | Article extraction library for Python that pulls full text, authors, dates and images out of news pages. |
| [scrapinghub/extruct](https://github.com/scrapinghub/extruct) | Python | 972 | 2026-04-01 | Extracts embedded structured metadata from HTML: JSON-LD, Microdata, RDFa, Open Graph and microformats. |


<a id="document-extraction"></a>

---

## Document Extraction

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [allenai/olmocr](https://github.com/allenai/olmocr) | Python | 19627 | 2026-03-25 | Toolkit that linearises PDFs into clean, reading-order text for LLM training sets and retrieval pipelines. |
| [lumina-ai-inc/chunkr](https://github.com/lumina-ai-inc/chunkr) | Rust | 4146 | 2026-09-09 | Document ingestion service that segments complex PDFs with vision models and emits chunked, RAG-ready text and layout data. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [yfedoseev/office_oxide](https://github.com/yfedoseev/office_oxide) | Rust | 128 | 2026-09-18 | Fast Rust library for reading and writing DOCX, XLSX and PPTX files, with bindings for Python, Go, JS, C# and WASM. |


<a id="routing-engines"></a>

---

## Routing Engines

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Project-OSRM/osrm-backend](https://github.com/Project-OSRM/osrm-backend) | C++ | 8086 | 2026-09-13 | High-performance routing engine for OpenStreetMap data, serving shortest paths, isochrones and map matching over HTTP. |
| [valhalla/valhalla](https://github.com/valhalla/valhalla) | C++ | 6224 | 2026-09-17 | Tiled routing engine for OpenStreetMap supporting multi-modal directions, isochrones and time-distance matrices. |


<a id="geospatial-processing"></a>

---

## Geospatial Processing

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [HydroniumLabs/h3o](https://github.com/HydroniumLabs/h3o) | Rust | 543 | 2026-08-29 | Pure Rust implementation of Uber's H3 hexagonal geospatial indexing system, with no C bindings. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apache/sedona](https://github.com/apache/sedona) | Java | 2410 | 2026-09-18 | Cluster computing framework that adds spatial types, indexes and SQL to Spark and Flink for large-scale geospatial analysis. |

#### Reading & references (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [allenai/olmoearth_projects](https://github.com/allenai/olmoearth_projects) | Python | 85 | 2026-09-18 | Model configurations, platform tooling and tutorials for applying AI2's OlmoEarth foundation model to remote sensing tasks. |


<a id="photogrammetry"></a>

---

## Photogrammetry

#### Tools (6)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [OpenDroneMap/ODM](https://github.com/OpenDroneMap/ODM) | Python | 6477 | 2026-09-16 | Command-line photogrammetry toolkit that turns drone, balloon or kite imagery into orthophotos, point clouds, 3D models and DEMs. |
| [WebODM/WebODM](https://github.com/WebODM/WebODM) | Python | 4178 | 2026-09-11 | Web interface and processing server for OpenDroneMap, managing aerial imagery projects, tasks and generated map products. |
| [freddewitt/CorbeauSplat](https://github.com/freddewitt/CorbeauSplat) | Python | 178 | 2026-09-17 | End-to-end Gaussian splatting pipeline for Apple Silicon, taking raw video or photos to a trained, viewable 3D scene. |
| [qianmingduowan/Sat3DGen](https://github.com/qianmingduowan/Sat3DGen) | Python | 135 | 2026-08-25 | Research code for generating street-level 3D scenes from a single satellite image, from the ICLR 2026 paper. |
| [OpenSfM/OpenSfM](https://github.com/OpenSfM/OpenSfM) | Python | 93 | 2026-09-08 | Structure-from-motion pipeline that reconstructs camera poses and sparse 3D geometry from unordered image collections. |
| [WebODM/ODX](https://github.com/WebODM/ODX) | Python | 78 | 2026-09-14 | Faster fork of OpenDroneMap that generates maps, point clouds, 3D models and DEMs from aerial and ground imagery. |


<a id="mapping-libraries"></a>

---

## Mapping Libraries

#### Reading & references (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [maplibre/awesome-maplibre](https://github.com/maplibre/awesome-maplibre) | — | 1077 | 2026-09-14 | Curated list of projects, plugins and styles built on the MapLibre mapping libraries. |
| [osmlab/awesome-openstreetmap](https://github.com/osmlab/awesome-openstreetmap) | — | 990 | 2026-02-23 | Curated list of OpenStreetMap projects: editors, renderers, routing engines and data pipelines. |
| [CesiumGS/cesiumjs-ai-starter-app](https://github.com/CesiumGS/cesiumjs-ai-starter-app) | TypeScript | 8 | 2026-09-15 | Starter template for building LLM-powered 3D globe applications on CesiumJS, wired for tool calling and MCP clients. |


<a id="embedded-firmware"></a>

---

## Embedded Firmware

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [meshtastic/firmware](https://github.com/meshtastic/firmware) | C++ | 8311 | 2026-09-18 | Firmware for Meshtastic LoRa radios, forming off-grid encrypted mesh networks for text and position sharing. |


<a id="radio-sdr"></a>

---

## Radio Sdr

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ruvnet/RuView](https://github.com/ruvnet/RuView) | Rust | 94365 | 2026-09-18 | Turns commodity WiFi radios into spatial sensing: presence detection, pose estimation and vital-sign monitoring without cameras. |
| [osmocom/pysim](https://github.com/osmocom/pysim) | Python | 585 | 2026-09-10 | Python tool for exploring and programming SIM, USIM and ISIM cards, reading and writing the 3GPP file system. |
| [portapack-mayhem/MayhemHub](https://github.com/portapack-mayhem/MayhemHub) | TypeScript | 272 | 2026-03-14 | Browser-based control panel for HackRF/PortaPack devices: flash firmware, manage the SD card and drive the radio over WebSerial without installing anything. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [aisstream/ais-message-models](https://github.com/aisstream/ais-message-models) | Java | 26 | 2024-01-08 | OpenAPI definitions and generated client libraries for the AIS vessel-tracking message models served by aisstream.io. |

#### Reading & references (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [RadarCODE/awesome-sar](https://github.com/RadarCODE/awesome-sar) | — | 1204 | 2025-07-22 | Curated list of Synthetic Aperture Radar software, libraries, datasets and learning resources. |
| [rickstaa/awesome-adsb](https://github.com/rickstaa/awesome-adsb) | HTML | 382 | 2026-09-05 | Curated list of ADS-B receivers, decoders, feeders and flight-tracking projects. |


<a id="uav-drones"></a>

---

## Uav Drones

#### Reading & references (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Matthias84/awesome-flying-fpv](https://github.com/Matthias84/awesome-flying-fpv) | — | 704 | 2026-03-06 | Curated list of free software and open hardware for building remote-controlled copters and fixed-wing planes. |
| [janesmae/awesome-drones](https://github.com/janesmae/awesome-drones) | — | 652 | 2026-09-01 | Curated list of drone resources covering flight controllers, simulators, SDKs and research references. |
| [Ibtisam-Mohammad/awesome-defense](https://github.com/Ibtisam-Mohammad/awesome-defense) | Python | 27 | 2026-08-31 | Curated list of open-source resources for physical defence: unmanned systems, sensing, geospatial intelligence and command-and-control. |
| [brandonhimpfen/awesome-open-source-drone-firmware](https://github.com/brandonhimpfen/awesome-open-source-drone-firmware) | Python | 24 | 2026-09-06 | Curated list of open-source drone firmware, flight controllers and UAV development tooling. |
| [brandonhimpfen/awesome-swarm-drones](https://github.com/brandonhimpfen/awesome-swarm-drones) | Python | 12 | 2026-09-06 | Curated list of tools, papers and frameworks for swarm drones, multi-UAV systems and coordinated aerial robotics. |


<a id="http-clients"></a>

---

## Http Clients

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [curl/curl](https://github.com/curl/curl) | C | 42876 | 2026-09-18 | Command-line client and C library for transferring data over HTTP, FTP, SMTP, MQTT and dozens of other protocols. |


<a id="network-monitoring"></a>

---

## Network Monitoring

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Rust | 41148 | 2026-09-17 | Cross-platform desktop app for monitoring network traffic, charting live captures by protocol, host and geolocation. |


<a id="content-management"></a>

---

## Content Management

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [directus/directus](https://github.com/directus/directus) | TypeScript | 37931 | 2026-09-18 | Headless CMS and admin platform that wraps an existing SQL database with instant REST and GraphQL APIs, auth and a data studio. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [pimcore/pimcore](https://github.com/pimcore/pimcore) | PHP | 3847 | 2026-09-18 | PHP framework for product information, master data and digital experience management, combining PIM, DAM, CMS and commerce. |


<a id="payments"></a>

---

## Payments

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | Rust | 43620 | 2026-09-18 | Composable payments switch that routes transactions across gateways, vaults and fraud providers behind one API. |
| [getlago/lago](https://github.com/getlago/lago) | Go | 10573 | 2026-09-18 | Usage-based billing platform that meters events, applies subscription and pricing logic, and drives invoicing, payments and revenue analytics. |
| [killbill/killbill](https://github.com/killbill/killbill) | Java | 5747 | 2026-09-14 | Subscription billing and payment platform with a plugin architecture, covering catalogs, invoicing, dunning and gateway routing. |


<a id="media-processing"></a>

---

## Media Processing

#### Tools (6)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) | Python | 59851 | 2026-09-06 | Agentic video production system with 12 pipelines and 700+ skill files that turn a coding assistant into a video editing and generation studio. |
| [Zackriya-Solutions/meetily](https://github.com/Zackriya-Solutions/meetily) | Rust | 30905 | 2026-09-15 | Self-hosted meeting assistant that transcribes and diarises audio locally with Whisper or Parakeet and summarises it through Ollama. |
| [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) | C | 17464 | 2026-09-18 | Image manipulation suite with command-line tools and C APIs for converting, editing and compositing across 200-plus image formats. |
| [h2non/imaginary](https://github.com/h2non/imaginary) | Go | 6076 | 2025-11-08 | HTTP microservice for on-the-fly image processing — resize, crop, rotate, watermark and format conversion — backed by libvips. |
| [OvenMediaLabs/OvenMediaEngine](https://github.com/OvenMediaLabs/OvenMediaEngine) | C++ | 3276 | 2026-09-17 | Sub-second latency live streaming server that ingests RTMP or SRT and delivers WebRTC and Low-Latency HLS at scale. |
| [openinary/openinary](https://github.com/openinary/openinary) | TypeScript | 403 | 2026-09-18 | Self-hostable image and video transformation service with URL-based operations, backed by S3 or Cloudflare R2. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [kane50613/takumi](https://github.com/kane50613/takumi) | Rust | 3001 | 2026-09-17 | Renders Open Graph images and paged PDFs from JSX, HTML and CSS without a headless browser, on Node, Workers or Rust. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [GStreamer/gstreamer](https://github.com/GStreamer/gstreamer) | C | 3316 | 2026-09-18 | Pipeline-based multimedia framework that links source, codec, filter and sink elements into graphs for playback, transcoding, capture and streaming. |


<a id="data-wrangling"></a>

---

## Data Wrangling

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [OpenRefine/OpenRefine](https://github.com/OpenRefine/OpenRefine) | Java | 12002 | 2026-09-15 | Desktop-scale workbench for exploring, cleaning and reconciling messy tabular data against external identifier services. |


<a id="entity-resolution"></a>

---

## Entity Resolution

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [opensanctions/yente](https://github.com/opensanctions/yente) | Python | 178 | 2026-09-18 | Search and bulk-matching API over OpenSanctions data, implementing the Reconciliation API spec for screening entity lists. |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [opensanctions/nomenklatura](https://github.com/opensanctions/nomenklatura) | Python | 267 | 2026-09-14 | Framework and CLI for integrating FollowTheMoney entity streams from many sources, with deduplication and record linkage. |


<a id="e-commerce"></a>

---

## E Commerce

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [medusajs/medusa](https://github.com/medusajs/medusa) | TypeScript | 36366 | 2026-09-18 | Modular headless commerce platform for Node.js, with composable modules for carts, orders, payments, fulfilment and an admin UI. |


<a id="business-intelligence"></a>

---

## Business Intelligence

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [cube-js/cube](https://github.com/cube-js/cube) | Rust | 20864 | 2026-09-18 | Semantic layer that defines metrics once and serves them over SQL, REST and GraphQL to BI tools, embedded analytics and LLM agents. |


<a id="email-tooling"></a>

---

## Email Tooling

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [mjmlio/mjml](https://github.com/mjmlio/mjml) | JavaScript | 18243 | 2026-09-10 | Markup language and compiler that turns component-based templates into responsive email HTML that survives legacy mail clients. |


<a id="blockchain-tooling"></a>

---

## Blockchain Tooling

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [trustwallet/wallet-core](https://github.com/trustwallet/wallet-core) | C++ | 3569 | 2026-09-18 | Cross-platform C++ wallet library handling key derivation, address formats and transaction signing across many blockchains, with Kotlin, Swift and WASM bindings. |

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [paradigmxyz/artemis](https://github.com/paradigmxyz/artemis) | Rust | 2966 | 2024-03-05 | Rust framework for MEV bots, wiring blockchain event collectors, strategies and transaction executors into a modular async pipeline. |


<a id="low-code-platforms"></a>

---

## Low Code Platforms

#### Frameworks (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [lowdefy/lowdefy](https://github.com/lowdefy/lowdefy) | JavaScript | 3007 | 2026-09-17 | Config-driven web app framework where admin panels, CRUD apps and dashboards are declared in YAML and rendered by a Next.js runtime. |


<a id="unsorted"></a>

---

## Unsorted

#### Unsorted (110)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [facet-rs/facet](https://github.com/facet-rs/facet) | Rust | 2578 | 2026-09-16 | Rust reflection, serialization, deserialization, pretty printing, etc |
| [kpcyrd/sn0int](https://github.com/kpcyrd/sn0int) | Rust | 2536 | 2026-05-15 | Semi-automatic OSINT framework and package manager |
| [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir) | Java | 2402 | 2026-09-18 | 🔥 HAPI FHIR - Java API for HL7 FHIR Clients and Servers |
| [zhiburt/tabled](https://github.com/zhiburt/tabled) | Rust | 2362 | 2026-09-05 | An easy to use library for pretty print tables of Rust structs and enums |
| [fitzgen/bumpalo](https://github.com/fitzgen/bumpalo) | Rust | 2331 | 2026-09-16 | A fast bump allocation arena for Rust |
| [GoogleCloudPlatform/gcsfuse](https://github.com/GoogleCloudPlatform/gcsfuse) | Go | 2310 | 2026-09-18 | A user-space file system for interacting with Google Cloud Storage |
| [est31/cargo-udeps](https://github.com/est31/cargo-udeps) | Rust | 2138 | 2026-04-29 | Find unused dependencies in Cargo.toml |
| [BurntSushi/fst](https://github.com/BurntSushi/fst) | Rust | 2119 | 2024-09-25 | Represent large sets and maps compactly with finite state transducers |
| [googleapis/google-cloud-java](https://github.com/googleapis/google-cloud-java) | Java | 2098 | 2026-09-18 | Google Cloud Client Library for Java |
| [pravega/pravega](https://github.com/pravega/pravega) | Java | 2000 | 2025-03-02 | Pravega - Streaming as a new software defined storage primitive |
| [Swatinem/rust-cache](https://github.com/Swatinem/rust-cache) | TypeScript | 1918 | 2026-09-07 | A GitHub Action that implements smart caching for rust/cargo projects |
| [RabbyHub/Rabby](https://github.com/RabbyHub/Rabby) | TypeScript | 1893 | 2026-09-18 | The game-changing wallet for Ethereum and all EVM chains |
| [stakpak/agent](https://github.com/stakpak/agent) | Rust | 1789 | 2026-07-06 | Ship your code, on autopilot |
| [typelevel/spire](https://github.com/typelevel/spire) | Scala | 1772 | 2026-07-27 | Powerful new number types and numeric abstractions for Scala |
| [greyblake/nutype](https://github.com/greyblake/nutype) | Rust | 1770 | 2026-09-01 | Rust newtype with guarantees 🇺🇦 🦀 |
| [standard-webhooks/standard-webhooks](https://github.com/standard-webhooks/standard-webhooks) | Java | 1748 | 2026-09-17 | The Standard Webhooks specification |
| [java-json-tools/json-schema-validator](https://github.com/java-json-tools/json-schema-validator) | Java | 1644 | 2024-07-17 | A JSON Schema validation implementation in pure Java, which aims for correctness and performance, in that order |
| [la10736/rstest](https://github.com/la10736/rstest) | Rust | 1587 | 2026-09-06 | Fixture-based test framework for Rust |
| [colin-kiegel/rust-derive-builder](https://github.com/colin-kiegel/rust-derive-builder) | Rust | 1541 | 2026-01-02 | derive builder implementation for rust structs |
| [Fazecast/jSerialComm](https://github.com/Fazecast/jSerialComm) | C | 1522 | 2025-11-07 | Platform-independent serial port access for Java |
| [OpenSLO/OpenSLO](https://github.com/OpenSLO/OpenSLO) | Makefile | 1518 | 2025-11-25 | Open specification for defining and expressing service level objectives (SLO) |
| [softwaremill/sttp](https://github.com/softwaremill/sttp) | Scala | 1506 | 2026-09-18 | The Scala HTTP client you always wanted! |
| [json4s/json4s](https://github.com/json4s/json4s) | Scala | 1486 | 2026-09-18 | JSON library |
| [Danau5tin/multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) | Python | 1450 | 2025-11-03 | Reached #13 on Stanford's Terminal Bench leaderboard |
| [kbknapp/cargo-outdated](https://github.com/kbknapp/cargo-outdated) | Rust | 1422 | 2026-06-10 | A cargo subcommand for displaying when Rust dependencies are out of date |
| [cookpete/auto-changelog](https://github.com/cookpete/auto-changelog) | JavaScript | 1399 | 2026-09-05 | Command line tool for generating a changelog from git tags and commit history |
| [Nukesor/comfy-table](https://github.com/Nukesor/comfy-table) | Rust | 1393 | 2026-09-14 | :large_orange_diamond: Build beautiful terminal tables with automatic content wrapping |
| [time-rs/time](https://github.com/time-rs/time) | Rust | 1338 | 2026-09-17 | Date and time handling in Rust |
| [bbottema/simple-java-mail](https://github.com/bbottema/simple-java-mail) | Java | 1290 | 2026-09-18 | Simple API, Complex Emails (Jakarta Mail smtp wrapper) |
| [nst/JSONTestSuite](https://github.com/nst/JSONTestSuite) | C++ | 1168 | 2024-11-22 | A comprehensive test suite for RFC 8259 compliant JSON parsers |
| [com-lihaoyi/fastparse](https://github.com/com-lihaoyi/fastparse) | Scala | 1134 | 2026-08-20 | Writing Fast Parsers Fast in Scala |
| [edgurgel/poxa](https://github.com/edgurgel/poxa) | Elixir | 1085 | 2024-06-30 | Pusher server implementation compatible with Pusher client libraries |
| [scrapfly/scrapfly-scrapers](https://github.com/scrapfly/scrapfly-scrapers) | Python | 1080 | 2026-09-11 | Scalable Python web scraping scripts for +40 popular domains |
| [symbolica-dev/symbolica](https://github.com/symbolica-dev/symbolica) | Rust | 979 | 2026-09-15 | A modern computer algebra library for Python and Rust |
| [zalando/problem](https://github.com/zalando/problem) | Java | 951 | 2026-07-24 | A Java library that implements application/problem+json |
| [typelevel/squants](https://github.com/typelevel/squants) | Scala | 931 | 2026-09-03 | The Scala API for Quantities, Units of Measure and Dimensional Analysis |
| [tower-rs/tower-http](https://github.com/tower-rs/tower-http) | Rust | 913 | 2026-09-13 | HTTP specific Tower utilities |
| [everit-org/json-schema](https://github.com/everit-org/json-schema) | Java | 901 | 2025-08-01 | JSON Schema validator for java, based on the org.json API |
| [ocsf/ocsf-schema](https://github.com/ocsf/ocsf-schema) | — | 892 | 2026-09-17 | OCSF Schema |
| [softwaremill/magnolia](https://github.com/softwaremill/magnolia) | Scala | 802 | 2026-09-13 | Easy, fast, transparent generic derivation of typeclass instances |
| [RocketGod-git/flipper-zero-rf-jammer](https://github.com/RocketGod-git/flipper-zero-rf-jammer) | C | 775 | 2026-09-17 | Frequency and preset adjustable subghz radio frequency jammer for Flipper Zero |
| [com-lihaoyi/upickle](https://github.com/com-lihaoyi/upickle) | Scala | 767 | 2026-02-27 | uPickle: a simple, fast, dependency-free JSON & Binary (MessagePack) serialization library for Scala |
| [RocketGod-git/HackRF-Treasure-Chest](https://github.com/RocketGod-git/HackRF-Treasure-Chest) | C | 753 | 2024-11-13 | HackRF software and captures by everyone and for everyone |
| [oleg-py/better-monadic-for](https://github.com/oleg-py/better-monadic-for) | Scala | 710 | 2024-05-07 | Desugaring scala `for` without implicit `withFilter`s |
| [RocketGod-git/ProtoPirate](https://github.com/RocketGod-git/ProtoPirate) | C | 679 | 2026-09-18 | Flipper Zero Protocol Pirate |
| [scoverage/sbt-scoverage](https://github.com/scoverage/sbt-scoverage) | Scala | 653 | 2026-09-15 | sbt plugin for scoverage |
| [biojava/biojava](https://github.com/biojava/biojava) | Java | 632 | 2026-09-17 | :book::microscope::coffee: BioJava is an open-source project dedicated to providing a Java library for processing biolog |
| [sevenlabs-hq/carbon](https://github.com/sevenlabs-hq/carbon) | Rust | 624 | 2026-09-15 | Carbon is an indexing framework on Solana |
| [FGRibreau/spinners](https://github.com/FGRibreau/spinners) | Rust | 602 | 2026-05-02 | 🛎 60+ Elegant terminal spinners for Rust |
| [arcadesdude/BRU](https://github.com/arcadesdude/BRU) | PowerShell | 553 | 2026-01-05 | Bloatware Removal Utility, for automating removal of pre-installed, factory bloatware from devices running Windows 7-11 |
| [seancfoley/IPAddress](https://github.com/seancfoley/IPAddress) | Java | 538 | 2026-09-07 | Java library for handling IP addresses and subnets, both IPv4 and IPv6 |
| [aventrix/jnanoid](https://github.com/aventrix/jnanoid) | Java | 521 | 2023-12-21 | A unique string ID generator for Java |
| [KStateMachine/kstatemachine](https://github.com/KStateMachine/kstatemachine) | Kotlin | 511 | 2026-09-14 | Powerful Kotlin Multiplatform library with clean DSL syntax for creating complex state machines and statecharts driven b |
| [jchambers/java-otp](https://github.com/jchambers/java-otp) | Java | 504 | 2026-09-01 | A one-time password (HOTP/TOTP) library for Java |
| [openwallet-foundation/acapy](https://github.com/openwallet-foundation/acapy) | Python | 493 | 2026-09-15 | ACA-Py is a foundation for building decentralized identity applications and services running in non-mobile environments |
| [f4b6a3/ulid-creator](https://github.com/f4b6a3/ulid-creator) | Java | 462 | 2026-02-21 | A Java library for generating Universally Unique Lexicographically Sortable Identifiers (ULID) |
| [cloudevents/sdk-java](https://github.com/cloudevents/sdk-java) | Java | 446 | 2026-07-16 | Java SDK for CloudEvents |
| [CVEProject/cve-schema](https://github.com/CVEProject/cve-schema) | HTML | 443 | 2026-01-30 | This repository is used for the development of the CVE JSON record format |
| [ThreeTen/threeten-extra](https://github.com/ThreeTen/threeten-extra) | Java | 426 | 2026-09-15 | Provides additional date-time classes that complement those in JDK 8 |
| [gdt050579/AppCUI-rs](https://github.com/gdt050579/AppCUI-rs) | Rust | 402 | 2026-09-17 | AppCUI is a fast, cross-platform console and text-based user interface (CUI/TUI) framework for Rust |
| [ZerkerEOD/krakenhashes](https://github.com/ZerkerEOD/krakenhashes) | Go | 401 | 2026-09-14 |  |
| [velvia/links](https://github.com/velvia/links) | Scala | 383 | 2026-06-07 | Just a bunch of useful links |
| [JavaMoney/jsr354-ri](https://github.com/JavaMoney/jsr354-ri) | Java | 375 | 2026-07-11 | JSR 354 - Moneta: Reference Implementation |
| [JavaMoney/jsr354-api](https://github.com/JavaMoney/jsr354-api) | Java | 373 | 2026-05-27 | JSR 354 - Money and Currency API |
| [thatdot/quine](https://github.com/thatdot/quine) | Scala | 361 | 2026-09-18 | Quine • a streaming graph • https://quine.io • Discord: https://discord.gg/GMhd8TE4MR |
| [openwallet-foundation/credo-ts](https://github.com/openwallet-foundation/credo-ts) | TypeScript | 352 | 2026-09-17 | Typescript framework for building decentralized identity and verifiable credential solutions |
| [mangstadt/biweekly](https://github.com/mangstadt/biweekly) | Java | 348 | 2025-06-18 | biweekly is an iCalendar library written in Java |
| [xerial/sbt-sonatype](https://github.com/xerial/sbt-sonatype) | Scala | 341 | 2026-02-13 | A sbt plugin for publishing Scala/Java projects to the Maven central |
| [Trendyol/stove](https://github.com/Trendyol/stove) | Kotlin | 310 | 2026-09-14 | Stove: The easiest way of writing e2e/component tests for your JVM back-end app with Kotlin |
| [walt-id/waltid-identity](https://github.com/walt-id/waltid-identity) | Kotlin | 309 | 2026-09-18 | All-in-one open-source identity and wallet toolkit |
| [grate-devs/grate](https://github.com/grate-devs/grate) | C# | 297 | 2026-09-14 | grate - the SQL scripts migration runner |
| [GoogleCloudPlatform/jit-groups](https://github.com/GoogleCloudPlatform/jit-groups) | Java | 289 | 2026-09-14 | JIT Groups is an open source application that lets you implement secure, self-service access management for Google Cloud |
| [fraktalio/fmodel](https://github.com/fraktalio/fmodel) | Kotlin | 288 | 2026-09-11 | Functional, Algebraic and Reactive domain modeling with Kotlin (Multiplatform) |
| [neogenie/fastnum](https://github.com/neogenie/fastnum) | Rust | 260 | 2026-06-11 | Fixed-size decimal numbers implemented in pure Rust |
| [CVEProject/cve-services](https://github.com/CVEProject/cve-services) | JavaScript | 255 | 2026-09-17 | This repo contains the source for the CVE Services API |
| [lomigmegard/akka-http-cors](https://github.com/lomigmegard/akka-http-cors) | Scala | 251 | 2026-03-27 | Akka Http directives implementing the CORS specifications defined by W3C |
| [clitic/kdam](https://github.com/clitic/kdam) | Rust | 247 | 2026-01-06 | A console progress bar library for Rust |
| [j256/simplemagic](https://github.com/j256/simplemagic) | Java | 241 | 2026-06-15 | Simple file magic number and content-type library which provides mime-type determination from files and byte arrays |
| [Comcast/ip4s](https://github.com/Comcast/ip4s) | Scala | 232 | 2026-07-13 | Defines immutable, safe data structures for describing IP addresses, multicast joins, socket addresses and similar IP & |
| [FraunhoferIOSB/FROST-Server](https://github.com/FraunhoferIOSB/FROST-Server) | Java | 228 | 2026-09-17 | A Complete Server implementation of the OGC SensorThings API |
| [mgrachev/update-informer](https://github.com/mgrachev/update-informer) | Rust | 228 | 2026-03-27 | Update informer for CLI/GUI applications written in Rust 🦀 |
| [kevincianfarini/alchemist](https://github.com/kevincianfarini/alchemist) | Kotlin | 177 | 2026-09-15 | Type safe management and arithmetic of physical units |
| [svroonland/rezilience](https://github.com/svroonland/rezilience) | Scala | 164 | 2026-09-11 | ZIO-native utilities for making resilient distributed systems |
| [openwallet-foundation/acapy-vc-authn-oidc](https://github.com/openwallet-foundation/acapy-vc-authn-oidc) | Python | 157 | 2026-09-18 |  |
| [erikerlandson/coulomb](https://github.com/erikerlandson/coulomb) | Scala | 153 | 2026-08-07 | coulomb: unit analysis for Scala |
| [plokhotnyuk/rtree2d](https://github.com/plokhotnyuk/rtree2d) | Scala | 145 | 2026-09-12 | RTree2D is a 2D immutable R-tree for ultra-fast nearest and intersection queries in plane and spherical coordinates |
| [GoogleCloudPlatform/inspec-gcp-cis-benchmark](https://github.com/GoogleCloudPlatform/inspec-gcp-cis-benchmark) | Ruby | 137 | 2026-01-06 | GCP CIS 4.0.0 Benchmark InSpec Profile |
| [goSprinto/compliance-skills](https://github.com/goSprinto/compliance-skills) | — | 131 | 2026-05-26 |  |
| [disintegrate-es/disintegrate](https://github.com/disintegrate-es/disintegrate) | Rust | 122 | 2026-08-03 | Disintegrate Rust library |
| [scodec/scodec-bits](https://github.com/scodec/scodec-bits) | Scala | 120 | 2026-09-08 | Provides immutable datatypes for working with bits and bytes |
| [electrolux-oss/infrakitchen](https://github.com/electrolux-oss/infrakitchen) | Python | 118 | 2026-09-18 | InfraKitchen is an open source Developer Platform that brings Platform Engineering practices to infrastructure managemen |
| [irahulstomar/cosmo-tui](https://github.com/irahulstomar/cosmo-tui) | Python | 107 | 2026-04-28 | A terminal dashboard for NASA's open data |
| [hellgrenj/Rumpel](https://github.com/hellgrenj/Rumpel) | C# | 100 | 2023-10-27 | Simple, opinionated and automated consumer-driven contract testing for your JSON API's |
| [KaraZajac/KAT](https://github.com/KaraZajac/KAT) | Rust | 94 | 2026-06-24 | Keyfob Analysis Tool |
| [taiki-e/easy-ext](https://github.com/taiki-e/easy-ext) | Rust | 88 | 2026-09-06 | A lightweight attribute macro for easily writing extension trait pattern |
| [business4s/decisions4s](https://github.com/business4s/decisions4s) | Scala | 85 | 2026-09-10 | Simple, Business-friendly Decisions Engine for Scala |
| [Artem-Romanenia/o2o](https://github.com/Artem-Romanenia/o2o) | Rust | 79 | 2026-07-04 | Object to Object mapper for Rust |
| [tmattsson/gs1utils](https://github.com/tmattsson/gs1utils) | Java | 65 | 2024-01-26 | Utilities for GS1 barcodes |
| [fraktalio/fmodel-rust](https://github.com/fraktalio/fmodel-rust) | Rust | 61 | 2026-09-07 | Domain modeling |
| [VirgilSecurity/virgil-e3kit-js](https://github.com/VirgilSecurity/virgil-e3kit-js) | TypeScript | 61 | 2024-05-28 | E3Kit is a security framework that simplifies work with Virgil services and presents the easiest way to add full end-to- |
| [L-yang-yang/cugenopt](https://github.com/L-yang-yang/cugenopt) | Cuda | 49 | 2026-03-30 | A GPU-accelerated general-purpose metaheuristic framework for combinatorial optimization |
| [atholbro/paseto](https://github.com/atholbro/paseto) | Kotlin | 43 | 2026-07-01 | Java Implementation of Platform-Agnostic Security Tokens - https://paseto.io |
| [lasantosr/model-mapper](https://github.com/lasantosr/model-mapper) | Rust | 37 | 2026-07-27 | Derive macro to map between different types |
| [opencve/opencve-kb](https://github.com/opencve/opencve-kb) | — | 35 | 2026-09-18 |  |
| [jahwag/clem](https://github.com/jahwag/clem) | Go | 32 | 2026-08-08 | Continuously Looping Engineering Machines |
| [FraunhoferIOSB/FROST-Client](https://github.com/FraunhoferIOSB/FROST-Client) | Java | 31 | 2026-06-23 | Library implementing a client interface to the SensorThingsAPI |
| [bcgov/indy-tails-server](https://github.com/bcgov/indy-tails-server) | Python | 29 | 2026-08-26 | This software stores and makes available tails files for use with Hyperledger Indy |
| [thenativeweb/eventsourcingdb-client-rust](https://github.com/thenativeweb/eventsourcingdb-client-rust) | Rust | 18 | 2026-09-14 | The official Rust client SDK for EventSourcingDB |
| [the-codeboy/Piston4J](https://github.com/the-codeboy/Piston4J) | Java | 13 | 2025-12-27 | A Java Wrapper for Piston (https://github.com/engineer-man/piston) |
| [openwallet-foundation/acapy-plugins](https://github.com/openwallet-foundation/acapy-plugins) | Python | 10 | 2026-09-17 | aries-acapy-plugins |

<!-- END: categories -->

---

## Triage queue

<!-- BEGIN: triage -->
Last 9 of 9 queued candidates — see [TRIAGE.md](./TRIAGE.md).

<!-- END: triage -->

---

## Archived

<!-- BEGIN: archived -->
- [_archived/sources.md](./_archived/sources.md) — 44 dead links, kept as tombstones with `last_seen` and `reason`.
- [_archived/tools.md](./_archived/tools.md) — 65 archived/EOL/stale repos.
<!-- END: archived -->

---

## License

CC0 1.0 Universal — see [LICENSE](./LICENSE).

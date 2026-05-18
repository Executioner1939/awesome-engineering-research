# awesome-engineering-research

A curated and machine-maintained reading + tools corpus covering distributed systems, language runtimes, functional programming, observability, infrastructure, AI applications, and adjacent areas. Sources and starred repos are deduplicated, labelled against a fixed taxonomy, periodically re-validated for liveness, and rendered to this README from `INDEX/`.

<!-- BEGIN: badges -->
![link-check](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/link-check.yml/badge.svg) ![star-sweep](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/star-sweep.yml/badge.svg) ![lint](https://github.com/Executioner1939/awesome-engineering-research/actions/workflows/frontmatter-lint.yml/badge.svg)
<!-- END: badges -->

## Stats

<!-- BEGIN: stats -->
- **Sources:** 294 active, 44 archived
- **Repos:** 487 active, 53 archived
- **Last regenerated:** 2026-05-18
<!-- END: stats -->

---

## Table of contents

<!-- BEGIN: toc -->

**Data plane**

- [Relational Databases](#relational-databases)
- [Columnar Databases](#columnar-databases)
- [Time Series Databases](#time-series-databases)
- [Graph Databases](#graph-databases)
- [Document Databases](#document-databases)
- [KV Stores](#kv-stores)
- [Caches](#caches)
- [Search Engines](#search-engines)
- [Object Stores](#object-stores)
- [Message Queues](#message-queues)
- [Stream Processing](#stream-processing)

**Language & runtime**

- [Async Runtimes](#async-runtimes)
- [Effect Systems](#effect-systems)
- [Compilers](#compilers)
- [Parsers](#parsers)
- [Static Analyzers](#static-analyzers)
- [Type Checkers](#type-checkers)
- [Garbage Collectors](#garbage-collectors)

**Distributed systems**

- [Consensus](#consensus)
- [Event Sourcing](#event-sourcing)
- [Workflow Engines](#workflow-engines)
- [Service Meshes](#service-meshes)
- [Api Gateways](#api-gateways)
- [RPC Frameworks](#rpc-frameworks)
- [Service Discovery](#service-discovery)

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

**Infrastructure**

- [Container Orchestration](#container-orchestration)
- [IaC](#iac)
- [Gitops](#gitops)
- [Build Systems](#build-systems)
- [Monorepo Tooling](#monorepo-tooling)
- [Container Runtimes](#container-runtimes)
- [Package Registries](#package-registries)

**Security**

- [Authentication](#authentication)
- [Authorization Policy](#authorization-policy)
- [Supply Chain Security](#supply-chain-security)
- [Vulnerability Scanning](#vulnerability-scanning)
- [Cryptography Libs](#cryptography-libs)
- [Network Security](#network-security)

**Developer experience**

- [CLI Frameworks](#cli-frameworks)
- [Code Editors](#code-editors)
- [Linters Formatters](#linters-formatters)
- [Shells Terminals](#shells-terminals)

**Functional programming**

- [Optics Lenses](#optics-lenses)
- [Streaming Libs](#streaming-libs)
- [Type Classes Prelude](#type-classes-prelude)

**Frontend & web**

- [UI Frameworks](#ui-frameworks)
- [Design Systems](#design-systems)

**Standards & specs**

- [RFCs](#rfcs)
- [OAuth OIDC](#oauth-oidc)
- [Cryptographic Standards](#cryptographic-standards)

**Knowledge & curation**

- [Awesome Lists](#awesome-lists)
- [Learning Resources](#learning-resources)
- [Interview Prep](#interview-prep)

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
| [PeerDB-io/peerdb](https://github.com/PeerDB-io/peerdb) | Go | 3111 | 2026-05-17 | Fast, Simple and a cost effective tool to replicate data from Postgres to Data Warehouses, Queues and Storage |
| [GoogleCloudPlatform/cloudsql-upgrade](https://github.com/GoogleCloudPlatform/cloudsql-upgrade) | — | 6 | 2025-07-14 | The tool simplifies upgrading your Cloud SQL databases to newer major versions (MySQL 5.7 to 8.0 and Postgr... |

#### Libraries (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [diesel-rs/diesel](https://github.com/diesel-rs/diesel) | Rust | 14077 | 2026-05-17 | A safe, extensible ORM and Query Builder for Rust |
| [JetBrains/Exposed](https://github.com/JetBrains/Exposed) | Kotlin | 9239 | 2026-05-14 | Kotlin SQL Framework |
| [apache/datafusion](https://github.com/apache/datafusion) | Rust | 8766 | 2026-05-17 | Apache DataFusion SQL Query Engine |
| [diesel-rs/diesel_async](https://github.com/diesel-rs/diesel_async) | Rust | 809 | 2026-04-30 | Diesel async connection implementation |

#### Unsorted (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [hit-box/hitbox](https://github.com/hit-box/hitbox) | Rust | 143 | 2026-05-16 | Async caching framework for Rust with Tower middleware, stale-while-revalidate, dogpile prevention, and plu... |

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
| [ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse) | C++ | 47458 | 2026-05-17 | ClickHouse® is a real-time analytics database management system |
| [ClickHouse/clickhouse-operator](https://github.com/ClickHouse/clickhouse-operator) | Go | 239 | 2026-05-16 | Official Kubernetes Operator for ClickHouse® |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [pola-rs/polars](https://github.com/pola-rs/polars) | Rust | 38517 | 2026-05-15 | Extremely fast Query Engine for DataFrames, written in Rust |


<a id="time-series-databases"></a>

---

## Time Series Databases

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apache/iotdb](https://github.com/apache/iotdb) | Java | 6329 | 2026-05-17 | Apache IoTDB |
| [GreptimeTeam/greptimedb](https://github.com/GreptimeTeam/greptimedb) | Rust | 6269 | 2026-05-16 | The open-source Observability 2.0 database |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [What is high cardinality, and how do time-series databases like InfluxDB and TimescaleDB compare?](https://blog.timescale.com/what-is-high-cardinality-how-do-time-series-databases-influxdb-timescaledb-compare/) | article | 2019-04 | data-storage, databases, frontend |
| [TimescaleDB 1.1 performance optimizations and PG11 Support](https://blog.timescale.com/timescaledb1-1-postgresql11-support-open-source-d108b2b244c3) | article | 2018-12 | data-storage, databases, language-runtimes |
| [TimescaleDB vs. InfluxDB: purpose built differently for time-series data](https://blog.timescale.com/timescaledb-vs-influxdb-for-time-series-data-timescale-influx-sql-nosql-36489299877) | article | 2018-09 | data-storage, databases, frontend |
| [Towards 3B time-series data points per day: Why DNSFilter replaced InfluxDB with TimescaleDB](https://blog.dnsfilter.com/3-billion-time-series-data-points-dnsfilter-replaced-influxdb-with-timescaledb-d9f827702f8b) | article | 2018-09 | data-storage, databases, frontend |


<a id="graph-databases"></a>

---

## Graph Databases

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [FalkorDB/FalkorDB](https://github.com/FalkorDB/FalkorDB) | C | 4422 | 2026-05-17 | A super fast Graph Database uses GraphBLAS under the hood for its sparse adjacency matrix graph representation |
| [memgraph/memgraph-docker-extension](https://github.com/memgraph/memgraph-docker-extension) | Dockerfile | 17 | 2026-05-15 | Docker extension for Memgraph, MAGE and Memgraph Lab |
| [memgraph/best-practices](https://github.com/memgraph/best-practices) | Cypher | 12 | 2026-04-28 | The shortest path to a successful project with Memgraph |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [neotypes/neotypes](https://github.com/neotypes/neotypes) | Scala | 175 | 2026-05-07 | Scala lightweight, type-safe, asynchronous driver for neo4j |

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
| [zeal18/zio-mongodb](https://github.com/zeal18/zio-mongodb) | Scala | 27 | 2026-05-11 | One more ZIO wrapper around the official MongoDB Java driver but better ;) |


<a id="kv-stores"></a>

---

## KV Stores

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [redis/redis](https://github.com/redis/redis) | C | 74395 | 2026-05-15 | For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and m... |
| [etcd-io/etcd](https://github.com/etcd-io/etcd) | Go | 51707 | 2026-05-15 | Distributed reliable key-value store for the most critical data of a distributed system |
| [dragonflydb/dragonfly](https://github.com/dragonflydb/dragonfly) | C++ | 30487 | 2026-05-17 | A modern replacement for Redis and Memcached |

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
| [moka-rs/moka](https://github.com/moka-rs/moka) | Rust | 2547 | 2026-03-22 | A high performance concurrent caching library for Rust |


<a id="search-engines"></a>

---

## Search Engines

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [meilisearch/meilisearch](https://github.com/meilisearch/meilisearch) | Rust | 57606 | 2026-05-16 | A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications |
| [typesense/typesense](https://github.com/typesense/typesense) | C++ | 25824 | 2026-05-15 | Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch ⚡ 🔍 ✨ Fast,... |
| [valeriansaliou/sonic](https://github.com/valeriansaliou/sonic) | Rust | 21211 | 2026-05-15 | 🦔 Fast, lightweight & schema-less search backend |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [quickwit-oss/tantivy](https://github.com/quickwit-oss/tantivy) | Rust | 15204 | 2026-05-16 | Tantivy is a full-text search engine library inspired by Apache Lucene and written in Rust |

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
| [ceph/ceph](https://github.com/ceph/ceph) | C++ | 16601 | 2026-05-17 | Ceph is a distributed object, block, and file storage platform |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Big Data Storage Wars: Ceph vs Gluster](https://technologyadvice.com/blog/information-technology/ceph-vs-gluster/) | article | 2019-03 | data-storage |


<a id="message-queues"></a>

---

## Message Queues

#### Tools (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [nats-io/nats-server](https://github.com/nats-io/nats-server) | Go | 19829 | 2026-05-16 | High-Performance server for NATS.io, the cloud and edge native messaging system |
| [redpanda-data/redpanda](https://github.com/redpanda-data/redpanda) | C++ | 12100 | 2026-05-16 | Redpanda is a streaming data platform for developers |
| [nats-io/nats.java](https://github.com/nats-io/nats.java) | Java | 661 | 2026-05-12 | Java client for NATS |
| [rabbitmq/rabbitmq-stream-java-client](https://github.com/rabbitmq/rabbitmq-stream-java-client) | Java | 70 | 2026-05-16 | RabbitMQ Stream Java Client |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [svix/omniqueue-rs](https://github.com/svix/omniqueue-rs) | Rust | 102 | 2026-05-06 | A Queue Abstraction Layer for Rust (Redis, RabbitMQ, SQS, etc.) |

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
| [debezium/debezium](https://github.com/debezium/debezium) | Java | 12735 | 2026-05-16 | Change data capture for a variety of databases |
| [risingwavelabs/risingwave](https://github.com/risingwavelabs/risingwave) | Rust | 9017 | 2026-05-17 | Event streaming platform for agentic AI |
| [arkflow-rs/arkflow](https://github.com/arkflow-rs/arkflow) | Rust | 1274 | 2026-04-27 | High performance Rust stream processing engine seamlessly integrates AI capabilities, providing powerful re... |
| [SeaQL/sea-streamer](https://github.com/SeaQL/sea-streamer) | Rust | 362 | 2026-04-19 | 🌊 Stream processing toolkit for Redis & Kafka |


<a id="async-runtimes"></a>

---

## Async Runtimes

#### Libraries (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [tokio-rs/tokio](https://github.com/tokio-rs/tokio) | Rust | 32016 | 2026-05-17 | A runtime for writing reliable asynchronous applications with Rust |
| [smol-rs/smol](https://github.com/smol-rs/smol) | Rust | 4933 | 2026-05-13 | A small and fast async runtime for Rust |
| [tokio-rs/console](https://github.com/tokio-rs/console) | Rust | 4518 | 2026-04-09 | a debugger for async rust! |

#### Unsorted (23)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [statelyai/xstate](https://github.com/statelyai/xstate) | TypeScript | 29618 | 2026-05-15 | State machines, statecharts, and actors for complex logic |
| [terrastruct/d2](https://github.com/terrastruct/d2) | Go | 23706 | 2026-04-24 | D2 is a modern diagram scripting language that turns text to diagrams |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | TypeScript | 14161 | 2026-05-08 | A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persiste... |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | Python | 13595 | 2026-05-17 | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict... |
| [akka/akka-core](https://github.com/akka/akka-core) | Scala | 13279 | 2026-05-15 | A platform to build and run apps that are elastic, agile, and resilient |
| [crossbeam-rs/crossbeam](https://github.com/crossbeam-rs/crossbeam) | Rust | 8444 | 2026-02-22 | Tools for concurrent programming in Rust |
| [arrow-kt/arrow](https://github.com/arrow-kt/arrow) | Kotlin | 6549 | 2026-05-17 | The perfect companion for your Kotlin journey - Inspired by functional, data-oriented and concurrent progra... |
| [apache/fory](https://github.com/apache/fory) | Java | 4333 | 2026-05-17 | A blazingly fast multi-language serialization framework for idiomatic domain objects, schema IDL, and cross... |
| [tower-rs/tower](https://github.com/tower-rs/tower) | Rust | 4183 | 2026-02-24 | async fn(Request) -> Result<Response, Error> |
| [JCTools/JCTools](https://github.com/JCTools/JCTools) | Java | 3826 | 2026-04-24 |  |
| [libpnet/libpnet](https://github.com/libpnet/libpnet) | Rust | 2572 | 2026-05-01 | Cross-platform, low level networking using the Rust programming language |
| [JelteF/derive_more](https://github.com/JelteF/derive_more) | Rust | 2106 | 2026-05-09 | Some more derive(Trait) options |
| [akka/akka-http](https://github.com/akka/akka-http) | Scala | 1349 | 2026-05-06 | The Streaming-first HTTP server/module of Akka |
| [tqwewe/kameo](https://github.com/tqwewe/kameo) | Rust | 1307 | 2026-05-13 | Fault-tolerant async actors for Rust that scale seamlessly |
| [rxRust/rxRust](https://github.com/rxRust/rxRust) | Rust | 1090 | 2026-05-05 | Zero-cost & Type-safe Reactive Extensions for Rust |
| [oconnor663/duct.rs](https://github.com/oconnor663/duct.rs) | Rust | 1025 | 2025-11-18 | a Rust library for running child processes |
| [ibraheemdev/papaya](https://github.com/ibraheemdev/papaya) | Rust | 915 | 2026-04-16 | A fast and ergonomic concurrent hashmap for read-heavy workloads |
| [zkat/cacache-rs](https://github.com/zkat/cacache-rs) | Rust | 704 | 2024-11-26 | A high-performance, concurrent, content-addressable disk cache, with support for both sync and async APIs |
| [lemastero/scala_typeclassopedia](https://github.com/lemastero/scala_typeclassopedia) | Scala | 386 | 2024-12-05 | Abstractions from Category theory with simple description & implementation, links to further resources. |
| [utkarshkukreti/speculate.rs](https://github.com/utkarshkukreti/speculate.rs) | Rust | 275 | 2023-05-10 | An RSpec inspired minimal testing framework for Rust. |
| [stav121/tasklet](https://github.com/stav121/tasklet) | Rust | 91 | 2025-12-30 | ⏱️ An asynchronous task scheduling library written in Rust |
| [borsaorg/borsa](https://github.com/borsaorg/borsa) | Rust | 20 | 2025-11-16 | Market data orchestrator for Rust with pluggable providers, data merging, and streaming |
| [but212/rustica](https://github.com/but212/rustica) | Rust | 17 | 2026-05-17 | Rustica is a functional programming library for the Rust language |

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
| [zio/zio](https://github.com/zio/zio) | Scala | 4381 | 2026-05-13 | ZIO — A type-safe, composable library for async and concurrent programming in Scala |
| [zio/zio-http](https://github.com/zio/zio-http) | Scala | 869 | 2026-05-14 | A next-generation Scala framework for building scalable, correct, and efficient HTTP clients and servers |
| [getkyo/kyo](https://github.com/getkyo/kyo) | Scala | 772 | 2026-05-16 | Toolkit for Scala Development |
| [zio/zio-prelude](https://github.com/zio/zio-prelude) | Scala | 473 | 2026-05-11 | A lightweight, distinctly Scala take on functional abstractions, with tight ZIO integration |
| [zio/zio-json](https://github.com/zio/zio-json) | Scala | 433 | 2026-05-13 | Fast, secure JSON library with tight ZIO integration |
| [zio/zio-kafka](https://github.com/zio/zio-kafka) | Scala | 367 | 2026-05-16 | A fast Kafka client for ZIO and ZIO Streams |
| [zio/zio-config](https://github.com/zio/zio-config) | Scala | 241 | 2026-05-12 | Easily use and document any config from anywhere in ZIO apps |
| [zio/zio-intellij](https://github.com/zio/zio-intellij) | Scala | 226 | 2026-04-17 | A companion IntelliJ IDEA plugin for the ZIO library ecosystem |
| [zio/zio-logging](https://github.com/zio/zio-logging) | Scala | 187 | 2026-05-14 | Powerful logging for ZIO 2.0 applications, with compatibility with many logging backends out-of-the-box |
| [zio/zio-redis](https://github.com/zio/zio-redis) | Scala | 136 | 2026-05-13 | A ZIO-based redis client |
| [zio/zio-telemetry](https://github.com/zio/zio-telemetry) | Scala | 123 | 2026-05-13 | ZIO-powered OpenTelemetry library |
| [zio/zio-cache](https://github.com/zio/zio-cache) | Scala | 87 | 2026-05-07 | A ZIO native cache with a simple and compositional interface |
| [bilal-fazlani/zio-ulid](https://github.com/bilal-fazlani/zio-ulid) | Scala | 12 | 2024-01-16 | zio implementation for https://github.com/ulid/spec |

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
| [carbon-language/carbon-lang](https://github.com/carbon-language/carbon-lang) | C++ | 33703 | 2026-05-17 | Carbon Language's main repository: documents, design, implementation, and related tools |
| [scala/scala](https://github.com/scala/scala) | Scala | 14452 | 2026-05-13 | Scala 2 compiler and standard library |
| [scala/scala3](https://github.com/scala/scala3) | Scala | 6252 | 2026-05-17 | The Scala 3 compiler, also known as Dotty |

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

#### Libraries (6)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [google/libphonenumber](https://github.com/google/libphonenumber) | C++ | 18019 | 2026-05-07 | Google's common Java, C++ and JavaScript library for parsing, formatting, and validating international phon... |
| [Marwes/combine](https://github.com/Marwes/combine) | Rust | 1356 | 2026-02-03 | A parser combinator library for Rust |
| [keichi/binary-parser](https://github.com/keichi/binary-parser) | TypeScript | 950 | 2026-04-15 | A blazing-fast declarative parser builder for binary data |
| [scodec/scodec](https://github.com/scodec/scodec) | Scala | 815 | 2026-05-07 | Scala combinator library for working with binary data |
| [typelevel/jawn](https://github.com/typelevel/jawn) | Scala | 436 | 2026-05-12 | Jawn is for parsing jay-sawn (JSON) |
| [azam/ulidj](https://github.com/azam/ulidj) | Java | 118 | 2026-05-12 | ULID (Universally Unique Lexicographically Sortable Identifier) generator and parser for Java |

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
| [ast-grep/ast-grep](https://github.com/ast-grep/ast-grep) | Rust | 13840 | 2026-05-15 | ⚡A CLI tool for code structural search, lint and rewriting |


<a id="type-checkers"></a>

---

## Type Checkers

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [microsoft/pyright](https://github.com/microsoft/pyright) | Python | 15440 | 2026-05-12 | Static Type Checker for Python |


<a id="garbage-collectors"></a>

---

## Garbage Collectors

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [For Better Computing, Liberate CPUs From Garbage Collection](https://spectrum.ieee.org/tech-talk/computing/hardware/this-little-device-relieves-a-cpu-from-its-garbage-collection-duties/) | article | 2019-05 | language-runtimes, misc |
| [Java's new Z Garbage Collector (ZGC) is very exciting](https://www.opsian.com/blog/javas-new-zgc-is-very-exciting/) | article | 2018-09 | language-runtimes |


<a id="consensus"></a>

---

## Consensus

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [databendlabs/openraft](https://github.com/databendlabs/openraft) | Rust | 1913 | 2026-05-17 | rust raft with improvements |

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
| [kurrent-io/KurrentDB](https://github.com/kurrent-io/KurrentDB) | C# | 5792 | 2026-05-15 | KurrentDB is a database that's engineered for modern software applications and event-driven architectures |
| [serverlesstechnology/cqrs](https://github.com/serverlesstechnology/cqrs) | Rust | 480 | 2026-05-13 | A lightweight, opinionated CQRS and event sourcing framework |
| [kurrent-io/KurrentDB-Client-Rust](https://github.com/kurrent-io/KurrentDB-Client-Rust) | Rust | 62 | 2026-05-11 | KurrentDB Rust Client |

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Saga Pattern — How to implement business transactions using Microservices – Part I](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part/) | article | 2019-06 | architecture-ddd, distributed-systems, event-sourcing, microservices |
| [Saga Pattern — How to implement business transactions using Microservices – Part II](https://blog.couchbase.com/saga-pattern-implement-business-transactions-using-microservices-part-2/) | article | 2019-06 | architecture-ddd, distributed-systems, event-sourcing, microservices |
| [Keep your domain clean in Event Sourcing](https://blog.softwaremill.com/keep-your-domain-clean-in-event-sourcing-5db6ddc26fe4) | article | 2018-08 | architecture-ddd, distributed-systems, event-sourcing, fp-scala |


<a id="workflow-engines"></a>

---

## Workflow Engines

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [apache/incubator-seata](https://github.com/apache/incubator-seata) | Java | 25959 | 2026-05-14 | :fire: Seata is an easy-to-use, high-performance, open source distributed transaction solution |


<a id="service-meshes"></a>

---

## Service Meshes

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [envoyproxy/gateway](https://github.com/envoyproxy/gateway) | Go | 2722 | 2026-05-17 | Manages Envoy Proxy as a Standalone or Kubernetes-based Application Gateway |

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
| [superfly/corrosion](https://github.com/superfly/corrosion) | Rust | 1685 | 2026-05-14 | Gossip-based service discovery (and more) for large distributed systems |


<a id="distributed-tracing"></a>

---

## Distributed Tracing

#### Tools (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [temporalio/temporal](https://github.com/temporalio/temporal) | Go | 20320 | 2026-05-17 | Temporal service |
| [open-telemetry/opentelemetry-operator](https://github.com/open-telemetry/opentelemetry-operator) | Go | 1690 | 2026-05-16 | Kubernetes Operator for OpenTelemetry Collector |
| [hypertrace/hypertrace](https://github.com/hypertrace/hypertrace) | Shell | 520 | 2025-03-14 | An open source distributed tracing & observability platform |


<a id="metrics"></a>

---

## Metrics

#### Unsorted (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [DrDroidLab/PlayBooks](https://github.com/DrDroidLab/PlayBooks) | Python | 455 | 2025-11-10 | Runbook automation platform with deep observability integrations for SRE & On-Call Teams |
| [DataJunction/dj](https://github.com/DataJunction/dj) | Python | 149 | 2026-05-17 | A metrics platform |


<a id="logging"></a>

---

## Logging

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [daboross/fern](https://github.com/daboross/fern) | Rust | 912 | 2024-12-15 | Simple, efficient logging for Rust |


<a id="apm"></a>

---

## APM

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [coroot/coroot](https://github.com/coroot/coroot) | Go | 7645 | 2026-05-15 | Coroot is an open-source observability and APM tool with AI-powered Root Cause Analysis |


<a id="agent-frameworks"></a>

---

## Agent Frameworks

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [browserbase/stagehand](https://github.com/browserbase/stagehand) | TypeScript | 22687 | 2026-05-16 | The SDK For Browser Agents |
| [hyperledger-labs/acapy-java-client](https://github.com/hyperledger-labs/acapy-java-client) | Java | 18 | 2023-12-14 | Aries Cloud Agent Python Java Client Library |

#### Frameworks (8)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | Python | 67708 | 2026-05-17 | Financial data platform for analysts, quants and AI agents |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Python | 32251 | 2026-05-17 | Build resilient agents |
| [getzep/graphiti](https://github.com/getzep/graphiti) | Python | 26163 | 2026-05-14 | Build Real-Time Knowledge Graphs for AI Agents |
| [coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) | TypeScript | 20779 | 2026-04-20 | An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and d... |
| [opactorai/Claudable](https://github.com/opactorai/Claudable) | TypeScript | 3962 | 2026-04-11 | Claudable is an open-source web builder that leverages local CLI agents, such as Claude Code, Codex, Gemini... |
| [langchain-ai/langgraphjs](https://github.com/langchain-ai/langgraphjs) | TypeScript | 2927 | 2026-05-16 | Framework to build resilient language agents as graphs |
| [docker/docker-agent](https://github.com/docker/docker-agent) | Go | 2920 | 2026-05-15 | AI Agent Builder and Runtime by Docker Engineering |
| [memgraph/skills](https://github.com/memgraph/skills) | — | 7 | 2026-05-04 | Agent skills that should help you build awesome stuff with Memgraph |

#### Unsorted (38)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | JavaScript | 185560 | 2026-05-17 | The agent harness performance optimization system |
| [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) | — | 137591 | 2026-05-10 | FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable,... |
| [anthropics/skills](https://github.com/anthropics/skills) | Python | 136273 | 2026-05-15 | Public repository for Agent Skills |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | TypeScript | 121018 | 2026-05-17 | 🔥 Search, scrape, and clean the web for AI agents |
| [browser-use/browser-use](https://github.com/browser-use/browser-use) | Python | 94321 | 2026-05-15 | 🌐 Make websites accessible for AI agents |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | Python | 81523 | 2026-03-26 | AI agents running research on single-GPU nanochat training automatically |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | HTML | 53423 | 2026-05-17 | from vibe coding to agentic engineering - practice makes claude perfect |
| [earendil-works/pi](https://github.com/earendil-works/pi) | TypeScript | 50770 | 2026-05-17 | AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods |
| [wshobson/agents](https://github.com/wshobson/agents) | Python | 35544 | 2026-05-17 | Intelligent automation and multi-agent orchestration for Claude Code |
| [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) | TypeScript | 31485 | 2026-05-17 | The Frontend Stack for Agents & Generative UI |
| [ashishpatel26/500-AI-Agents-Projects](https://github.com/ashishpatel26/500-AI-Agents-Projects) | — | 30725 | 2026-01-13 | The 500 AI Agents Projects is a curated collection of AI agent use cases across various industries |
| [huggingface/agents-course](https://github.com/huggingface/agents-course) | MDX | 28687 | 2026-04-27 | This repository contains the Hugging Face Agents Course |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | JavaScript | 26706 | 2026-05-16 | Vercel's official collection of agent skills |
| [usestrix/strix](https://github.com/usestrix/strix) | Python | 25342 | 2026-05-11 | Open-source AI hackers to find and fix your app’s vulnerabilities |
| [oraios/serena](https://github.com/oraios/serena) | Python | 24314 | 2026-05-16 | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for you... |
| [google/adk-python](https://github.com/google/adk-python) | Python | 19675 | 2026-05-16 | An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents w... |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | Python | 18776 | 2026-04-22 | Specification and documentation for Agent Skills |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | Python | 14554 | 2026-05-15 | Memori is agent-native memory infrastructure |
| [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) | Python | 13600 | 2026-05-15 | Hindsight: Agent Memory That  Learns |
| [ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui) | Python | 13591 | 2026-05-17 | AG-UI: the Agent-User Interaction Protocol |
| [zilliztech/claude-context](https://github.com/zilliztech/claude-context) | TypeScript | 11293 | 2026-05-06 | Code search MCP for Claude Code |
| [google/skills](https://github.com/google/skills) | — | 9666 | 2026-05-15 | Agent Skills for Google products and technologies |
| [snarktank/ai-dev-tasks](https://github.com/snarktank/ai-dev-tasks) | — | 7719 | 2025-11-05 | A simple task management system for managing AI dev agents |
| [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) | TypeScript | 6472 | 2026-02-04 | AI Product Design Agent - Open Source |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | JavaScript | 5900 | 2026-01-06 | Comprehensive Claude Code project configuration example with hooks, skills, agents, commands, and GitHub Ac... |
| [generalaction/emdash](https://github.com/generalaction/emdash) | TypeScript | 4458 | 2026-05-17 | Emdash is the Open-Source Agentic Development Environment (🧡 YC W26) |
| [memgraph/memgraph](https://github.com/memgraph/memgraph) | C++ | 4042 | 2026-05-17 | High-performance open-source in-memory graph database for GraphRAG, AI memory, agentic AI, and real-time gr... |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | Python | 3773 | 2026-01-26 | Context management for Claude Code |
| [TinyAGI/tinyagi](https://github.com/TinyAGI/tinyagi) | TypeScript | 3563 | 2026-03-30 | TinyAGI is the agent teams orchestrator for One Person Company |
| [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) | Python | 2942 | 2026-05-14 | A single hub to find Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections to extend... |
| [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) | — | 1855 | 2026-05-17 | Terraform & OpenTofu Skill for AI Agents - testing, modules, CI/CD, and production patterns |
| [solana-foundation/pay](https://github.com/solana-foundation/pay) | Rust | 1679 | 2026-05-15 | Let your agents pay for any API |
| [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) | Python | 1590 | 2026-03-10 | Apple Silicon (MLX) port of Karpathy's autoresearch — autonomous AI research loops on Mac, no PyTorch required |
| [lst97/claude-code-sub-agents](https://github.com/lst97/claude-code-sub-agents) | — | 1563 | 2025-08-15 | Collection of specialized AI subagents for Claude Code for personal use (full-stack development) |
| [langtalks/swe-agent](https://github.com/langtalks/swe-agent) | Python | 631 | 2026-03-28 | 🤖 AI-powered software engineering multi-agent system with researcher and developer agents that automate cod... |
| [zhsama/claude-sub-agent](https://github.com/zhsama/claude-sub-agent) | — | 581 | 2025-08-08 | AI-driven development workflow system built on Claude Code Sub-Agents |
| [FrancescoStabile/numasec](https://github.com/FrancescoStabile/numasec) | TypeScript | 360 | 2026-05-08 | The AI Agent for Cyber Security |
| [bahdotsh/indxr](https://github.com/bahdotsh/indxr) | Rust | 64 | 2026-04-07 | A fast codebase indexer and knowledge wiki for AI agents |


<a id="llm-app-frameworks"></a>

---

## LLM App Frameworks

#### Frameworks (3)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Python | 136955 | 2026-05-17 | The agent engineering platform |
| [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) | TypeScript | 17675 | 2026-05-16 | The agent engineering platform |
| [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) | Python | 9809 | 2026-05-16 | An Open-Source Asynchronous Coding Agent |

#### Unsorted (10)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | JavaScript | 62725 | 2026-05-17 | A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Clau... |
| [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks) | Jupyter Notebook | 43179 | 2026-05-14 | A collection of notebooks/recipes showcasing some fun and effective ways of using Claude |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | TypeScript | 16883 | 2026-05-17 | Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more |
| [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) | JavaScript | 8325 | 2026-05-06 | 45 tips for getting the most out of Claude Code, from basics to advanced - includes a custom status line sc... |
| [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | TypeScript | 6032 | 2026-05-17 | Open-source Claude Design alternative |
| [Pimzino/claude-code-spec-workflow](https://github.com/Pimzino/claude-code-spec-workflow) | TypeScript | 3735 | 2025-09-07 | Automated workflows for Claude Code |
| [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) | HTML | 2394 | 2026-05-11 | Thirteen editorial diagram types for Claude Code |
| [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | Dockerfile | 2265 | 2026-04-10 | AI coding workstation: Claude Code + web UI + 7 AI CLIs + headless browser + 50+ tools |
| [GWUDCAP/cc-sessions](https://github.com/GWUDCAP/cc-sessions) | JavaScript | 1540 | 2025-12-17 | an opinionated approach to productive development with Claude Code |
| [TheBushidoCollective/han](https://github.com/TheBushidoCollective/han) | TypeScript | 152 | 2026-04-28 | A curated marketplace of Claude Code plugins that embody the principles of ethical and professional softwar... |


<a id="rag-retrieval"></a>

---

## RAG Retrieval

#### Unsorted (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [open-webui/open-webui](https://github.com/open-webui/open-webui) | Python | 137495 | 2026-05-15 | User-friendly AI Interface (Supports Ollama, OpenAI API, ...) |


<a id="model-serving"></a>

---

## Model Serving

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [exo-explore/exo](https://github.com/exo-explore/exo) | Python | 44749 | 2026-05-15 | Run frontier AI locally |


<a id="mcp-tooling"></a>

---

## MCP Tooling

#### Tools (5)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [Jpisnice/shadcn-ui-mcp-server](https://github.com/Jpisnice/shadcn-ui-mcp-server) | TypeScript | 2768 | 2026-05-16 | A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaita... |
| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk) | Kotlin | 1362 | 2026-05-15 | The official Kotlin SDK for Model Context Protocol servers and clients |
| [bartolli/codanna](https://github.com/bartolli/codanna) | Rust | 673 | 2026-05-16 | Local code intelligence MCP server and CLI for AI coding agents |
| [stakpak/mcp](https://github.com/stakpak/mcp) | JavaScript | 19 | 2025-03-25 | Lightweight MCP server to give you access to the Stakpak API |
| [AikidoSec/aikido-claude-plugin](https://github.com/AikidoSec/aikido-claude-plugin) | — | 8 | 2026-05-15 |  |

#### Unsorted (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [MCP-UI-Org/mcp-ui](https://github.com/MCP-UI-Org/mcp-ui) | TypeScript | 4818 | 2026-05-09 | UI over MCP |
| [ref-tools/ref-tools-mcp](https://github.com/ref-tools/ref-tools-mcp) | TypeScript | 1104 | 2026-05-06 | Helping coding agents never make mistakes working with public or private libraries without wasting the cont... |


<a id="container-orchestration"></a>

---

## Container Orchestration

#### Tools (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [kubernetes/kubernetes](https://github.com/kubernetes/kubernetes) | Go | 122318 | 2026-05-17 | Production-Grade Container Scheduling and Management |
| [stakater/Reloader](https://github.com/stakater/Reloader) | Go | 10049 | 2026-05-15 | A Kubernetes controller to watch changes in ConfigMap and Secrets and do rolling upgrades on Pods with thei... |
| [kubernetes-sigs/external-dns](https://github.com/kubernetes-sigs/external-dns) | Go | 8951 | 2026-05-17 | Configure external DNS servers dynamically from Kubernetes resources |
| [kubernetes-sigs/gateway-api](https://github.com/kubernetes-sigs/gateway-api) | Go | 2855 | 2026-05-15 | Repository for the next iteration of composite service (e.g |
| [kubernetes/git-sync](https://github.com/kubernetes/git-sync) | Shell | 2689 | 2026-04-27 | A sidecar app which clones a git repo and keeps it in sync with the upstream |
| [kubernetes-sigs/ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) | Go | 997 | 2026-04-29 | Convert Ingress resources to Gateway API resources |
| [argoproj-labs/argocd-operator](https://github.com/argoproj-labs/argocd-operator) | Go | 862 | 2026-05-15 | A Kubernetes operator for managing Argo CD clusters |
| [gianlucam76/k8s-cleaner](https://github.com/gianlucam76/k8s-cleaner) | Go | 780 | 2026-05-17 | Cleaner is a Kubernetes controller that identifies unused or unhealthy resources, helping you maintain a st... |
| [kubernetes-sigs/gwctl](https://github.com/kubernetes-sigs/gwctl) | Go | 126 | 2026-05-05 | gwctl is a command-line tool for managing and understanding Gateway API resources in your Kubernetes cluster |

#### Unsorted (21)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [helm/helm](https://github.com/helm/helm) | Go | 29823 | 2026-05-16 | The Kubernetes Package Manager |
| [dapr/dapr](https://github.com/dapr/dapr) | Go | 25758 | 2026-05-15 | Dapr is a portable runtime for building distributed applications across cloud and edge, combining event-dri... |
| [cert-manager/cert-manager](https://github.com/cert-manager/cert-manager) | Go | 13813 | 2026-05-17 | Automatically provision and manage TLS certificates in Kubernetes |
| [kedacore/keda](https://github.com/kedacore/keda) | Go | 10193 | 2026-05-14 | KEDA is a Kubernetes-based Event Driven Autoscaling component |
| [authzed/spicedb](https://github.com/authzed/spicedb) | Go | 6709 | 2026-05-17 | Open Source, Google Zanzibar-inspired database for scalably storing and querying fine-grained authorization... |
| [opencost/opencost](https://github.com/opencost/opencost) | Go | 6547 | 2026-05-15 | Cost monitoring for Kubernetes workloads and cloud costs |
| [k0sproject/k0s](https://github.com/k0sproject/k0s) | Go | 6141 | 2026-05-15 | k0s - The Zero Friction Kubernetes |
| [karmada-io/karmada](https://github.com/karmada-io/karmada) | Go | 5469 | 2026-05-15 | Open, Multi-Cloud, Multi-Cluster Kubernetes Orchestration |
| [cilium/tetragon](https://github.com/cilium/tetragon) | C | 4676 | 2026-05-15 | eBPF-based Security Observability and Runtime Enforcement |
| [txn2/kubefwd](https://github.com/txn2/kubefwd) | Go | 4109 | 2026-05-14 | Bulk port forwarding Kubernetes services for local development |
| [doitintl/kube-no-trouble](https://github.com/doitintl/kube-no-trouble) | Go | 3664 | 2025-10-16 | Easily check your clusters for use of deprecated APIs |
| [akuity/kargo](https://github.com/akuity/kargo) | Go | 3311 | 2026-05-17 | Application lifecycle orchestration |
| [philippemerle/KubeDiagrams](https://github.com/philippemerle/KubeDiagrams) | JavaScript | 2488 | 2026-05-15 | Generate Kubernetes architecture diagrams from Kubernetes manifest files, kustomization files, Helm charts,... |
| [linki/chaoskube](https://github.com/linki/chaoskube) | Go | 1922 | 2026-05-01 | chaoskube periodically kills random pods in your Kubernetes cluster |
| [hcavarsan/kftray](https://github.com/hcavarsan/kftray) | Rust | 1508 | 2026-05-17 | kubectl port-forward manager and reverse tunnel (ngrok-like) for exposing local  services publicly, with TL... |
| [kubenetworks/kubevpn](https://github.com/kubenetworks/kubevpn) | Go | 1313 | 2026-04-19 | KubeVPN offers a Cloud Native Dev Environment that connects to kubernetes cluster network |
| [deggja/netfetch](https://github.com/deggja/netfetch) | Go | 448 | 2026-03-13 | Kubernetes tool for scanning clusters for network policies and identifying unprotected workloads |
| [FairwindsOps/gemini](https://github.com/FairwindsOps/gemini) | Go | 433 | 2026-05-17 | Automated backups of PersistentVolumeClaims in Kubernetes using VolumeSnapshots |
| [squat/generic-device-plugin](https://github.com/squat/generic-device-plugin) | Go | 352 | 2026-05-15 | A Kubernetes device plugin to schedule generic Linux devices |
| [doriordan/skuber](https://github.com/doriordan/skuber) | Scala | 330 | 2026-05-08 | A Scala Kubernetes client library |
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

#### Tools (7)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [hashicorp/terraform](https://github.com/hashicorp/terraform) | Go | 48414 | 2026-05-16 | Terraform enables you to safely and predictably create, change, and improve infrastructure |
| [opentofu/opentofu](https://github.com/opentofu/opentofu) | Go | 28674 | 2026-05-17 | OpenTofu lets you declaratively manage your cloud infrastructure |
| [gruntwork-io/terragrunt](https://github.com/gruntwork-io/terragrunt) | Go | 9572 | 2026-05-17 | Terragrunt is a flexible orchestration tool that allows Infrastructure as Code written in OpenTofu/Terrafor... |
| [diggerhq/digger](https://github.com/diggerhq/digger) | Go | 4940 | 2026-05-13 | Digger is an open source IaC orchestration tool |
| [terraform-docs/terraform-docs](https://github.com/terraform-docs/terraform-docs) | Go | 4773 | 2026-05-10 | Generate documentation from Terraform modules in various output formats |
| [cycloidio/terracognita](https://github.com/cycloidio/terracognita) | Go | 2368 | 2025-09-02 | Reads from existing public and private cloud providers (reverse Terraform) and generates your infrastructur... |
| [terraform-google-modules/terraform-google-bootstrap](https://github.com/terraform-google-modules/terraform-google-bootstrap) | HCL | 248 | 2026-05-15 | Bootstraps Terraform usage and related CI/CD in a new Google Cloud organization |

#### Unsorted (11)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [infracost/infracost](https://github.com/infracost/infracost) | Go | 12304 | 2026-05-15 | Cloud cost estimates for Terraform in pull requests💰📉 Shift FinOps Left! |
| [runatlantis/atlantis](https://github.com/runatlantis/atlantis) | Go | 9076 | 2026-05-17 | Terraform Pull Request Automation |
| [tfutils/tfenv](https://github.com/tfutils/tfenv) | Shell | 4931 | 2026-05-01 | Terraform version manager |
| [antonbabenko/pre-commit-terraform](https://github.com/antonbabenko/pre-commit-terraform) | Shell | 3717 | 2026-05-15 | pre-commit git hooks to take care of Terraform configurations 🇺🇦 |
| [busser/tfautomv](https://github.com/busser/tfautomv) | Go | 896 | 2026-05-13 | Generate Terraform moved blocks automatically for painless refactoring |
| [boltops-tools/terraspace](https://github.com/boltops-tools/terraspace) | Ruby | 717 | 2025-10-13 | Terraspace: The Terraform Framework |
| [leg100/otf](https://github.com/leg100/otf) | Go | 676 | 2026-05-17 | An open source alternative to terraform enterprise |
| [terralist/terralist](https://github.com/terralist/terralist) | Go | 491 | 2026-05-17 | Terraform Private Registry for modules and providers manageable from a REST API |
| [MatthewJohn/terrareg](https://github.com/MatthewJohn/terrareg) | Go | 340 | 2026-05-11 | Open source Terraform module registry with UI, optional Git integration and deep analysis |
| [shihanng/tfvar](https://github.com/shihanng/tfvar) | Go | 231 | 2026-03-11 | Terraform's variable definitions template generator |
| [busser/tftree](https://github.com/busser/tftree) | Go | 158 | 2026-04-30 | Display your Terraform module call stack in your terminal |


<a id="gitops"></a>

---

## Gitops

#### Tools (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [argoproj/argo-cd](https://github.com/argoproj/argo-cd) | Go | 22905 | 2026-05-17 | Declarative Continuous Deployment for Kubernetes |
| [terramate-io/terramate](https://github.com/terramate-io/terramate) | Go | 3584 | 2026-05-13 | Open-source Infrastructure as Code (IaC) orchestration platform: GitOps workflows, orchestration, code gene... |
| [argoproj/argo-rollouts](https://github.com/argoproj/argo-rollouts) | Go | 3478 | 2026-05-06 | Progressive Delivery for Kubernetes |
| [terrateamio/terrateam](https://github.com/terrateamio/terrateam) | OCaml | 1226 | 2026-05-17 | Terrateam is open-source GitOps infrastructure orchestration |
| [argoproj-labs/argocd-autopilot](https://github.com/argoproj-labs/argocd-autopilot) | Go | 1117 | 2025-12-16 | Argo-CD Autopilot |
| [argoproj-labs/terraform-provider-argocd](https://github.com/argoproj-labs/terraform-provider-argocd) | Go | 501 | 2026-05-16 | Terraform provider for Argo CD |
| [argoproj-labs/rollout-extension](https://github.com/argoproj-labs/rollout-extension) | TypeScript | 283 | 2025-12-22 | Argo Rollout visualization in Argo CD Web UI |
| [argoproj-labs/rollouts-plugin-trafficrouter-gatewayapi](https://github.com/argoproj-labs/rollouts-plugin-trafficrouter-gatewayapi) | Go | 152 | 2026-05-12 | The Argo Rollouts plugin implementing the Kubernetes Gateway API specification for using different traffic ... |
| [SelfhostedPro/ArgoCD-Role-Composition](https://github.com/SelfhostedPro/ArgoCD-Role-Composition) | Smarty | 4 | 2025-11-04 | Example Repository utilizing roles to deploy applications to argo-cd clusters |


<a id="build-systems"></a>

---

## Build Systems

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [moonrepo/moon](https://github.com/moonrepo/moon) | Rust | 3858 | 2026-05-17 | A build system and monorepo management tool for the web ecosystem, written in Rust |

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
| [moonrepo/proto](https://github.com/moonrepo/proto) | Rust | 1275 | 2026-05-16 | A pluggable multi-language version manager |


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


<a id="authentication"></a>

---

## Authentication

#### Tools (11)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [keycloak/keycloak](https://github.com/keycloak/keycloak) | Java | 34440 | 2026-05-17 | Open Source Identity and Access Management For Modern Applications and Services |
| [goauthentik/authentik](https://github.com/goauthentik/authentik) | Python | 21500 | 2026-05-17 | The authentication glue you need |
| [zitadel/zitadel](https://github.com/zitadel/zitadel) | Go | 13790 | 2026-05-15 | ZITADEL - Identity infrastructure, simplified for you |
| [kanidm/kanidm](https://github.com/kanidm/kanidm) | Rust | 4959 | 2026-05-17 | Kanidm: A simple, secure, and fast identity management platform |
| [ory/oathkeeper](https://github.com/ory/oathkeeper) | Go | 3559 | 2026-05-15 | A cloud native Identity & Access Proxy / API (IAP) and Access Control Decision API that authenticates, auth... |
| [keycloakify/keycloakify](https://github.com/keycloakify/keycloakify) | TypeScript | 2457 | 2026-03-21 | 🔏 Keycloak theming for the modern web |
| [thomasdarimont/keycloak-extension-playground](https://github.com/thomasdarimont/keycloak-extension-playground) | Java | 723 | 2025-01-15 | Simple project environment for creating custom Keycloak extensions |
| [p2-inc/keycloak-magic-link](https://github.com/p2-inc/keycloak-magic-link) | Java | 404 | 2026-05-13 | Magic Link Authentication for Keycloak |
| [daniel-frak/keycloak-user-migration](https://github.com/daniel-frak/keycloak-user-migration) | Java | 370 | 2026-05-17 | A Keycloak plugin for migrating users from legacy systems |
| [cooperlyt/keycloak-phone-provider](https://github.com/cooperlyt/keycloak-phone-provider) | Java | 357 | 2025-03-04 | A Keycloak provider for phone and SMS |
| [adorsys/keycloak-ssi-deployment](https://github.com/adorsys/keycloak-ssi-deployment) | Shell | 14 | 2026-04-23 |  |

#### Videos (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [DevNation Live: A Deep Dive into Keycloak](https://www.youtube.com/watch?v=ZxpY_zZ52kU&feature=youtu.be) | video | 2019-01 | misc |


<a id="authorization-policy"></a>

---

## Authorization Policy

#### Tools (6)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [open-policy-agent/opa](https://github.com/open-policy-agent/opa) | Go | 11734 | 2026-05-13 | Open Policy Agent (OPA) is an open source, general-purpose policy engine |
| [kyverno/kyverno](https://github.com/kyverno/kyverno) | Go | 7755 | 2026-05-15 | Unified Policy as Code |
| [permitio/opal](https://github.com/permitio/opal) | Python | 5452 | 2026-05-13 | Policy and data administration, distribution, and real-time updates on top of Policy Agents (OPA, Cedar, ...) |
| [kyverno/policy-reporter](https://github.com/kyverno/policy-reporter) | Go | 367 | 2026-05-12 | Monitoring and Observability Tool for the PolicyReport CRD with an optional UI |
| [kyverno/policy-reporter-ui](https://github.com/kyverno/policy-reporter-ui) | Go | 58 | 2026-05-08 | Policy Reporter UI |
| [Bisnode/opa-java-client](https://github.com/Bisnode/opa-java-client) | Java | 39 | 2024-10-28 |  |


<a id="supply-chain-security"></a>

---

## Supply Chain Security

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [renovatebot/renovate](https://github.com/renovatebot/renovate) | TypeScript | 21542 | 2026-05-17 | Home of the Renovate CLI: Cross-platform Dependency Automation by Mend.io |


<a id="vulnerability-scanning"></a>

---

## Vulnerability Scanning

#### Tools (4)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [aquasecurity/trivy](https://github.com/aquasecurity/trivy) | Go | 35028 | 2026-05-15 | Find vulnerabilities, misconfigurations, secrets, SBOM in containers, Kubernetes, code repositories, clouds... |
| [projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei) | Go | 28705 | 2026-05-14 | Nuclei is a fast, customizable vulnerability scanner powered by the global security community and built on ... |
| [aquasecurity/tfsec](https://github.com/aquasecurity/tfsec) | Go | 7002 | 2026-03-25 | Tfsec is now part of Trivy |
| [aquasecurity/trivy-operator](https://github.com/aquasecurity/trivy-operator) | Go | 1867 | 2026-05-17 | Kubernetes-native security toolkit |


<a id="cryptography-libs"></a>

---

## Cryptography Libs

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Cryptography—What Is It and How Does It Work?](https://medium.com/@ahjuice/cryptography-what-is-it-and-how-does-it-work-2a21a730d694) | article | 2018-10 | security |
| [The Empire Strikes Back with a Coordinated War on Crypto](https://hackernoon.com/the-empire-strikes-back-with-a-coordinated-war-on-crypto-bdd84fd2f854) | article | 2018-10 | security |
| [Secure Password Hashing](https://security.blogoverflow.com/2013/09/about-secure-password-hashing/) | article | 2018-04 | security |


<a id="network-security"></a>

---

## Network Security

#### Articles (3)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Do VPNs Actually Protect Your Privacy?](https://medium.com/datadriveninvestor/do-vpns-actually-protect-your-privacy-5f98a9cec90a) | article | 2018-11 | security |
| [The CIA just lost control of its hacking arsenal. Here’s what you need to know.](https://medium.freecodecamp.org/the-cia-just-lost-control-of-its-hacking-arsenal-heres-what-you-need-to-know-ea69fc1ce38c) | article | 2018-11 | security |
| [How Spam Filtering Works: From SPF to DKIM to Blacklists](https://deliciousbrains.com/how-spam-filters-works/) | article | 2018-09 | security |


<a id="cli-frameworks"></a>

---

## CLI Frameworks

#### Libraries (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [clap-rs/clap](https://github.com/clap-rs/clap) | Rust | 16391 | 2026-05-11 | A full featured, fast Command Line Argument Parser for Rust |
| [ksk001100/seahorse](https://github.com/ksk001100/seahorse) | Rust | 306 | 2026-05-07 | A minimal CLI framework written in Rust |


<a id="code-editors"></a>

---

## Code Editors

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [zed-industries/zed](https://github.com/zed-industries/zed) | Rust | 83089 | 2026-05-17 | Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom... |


<a id="linters-formatters"></a>

---

## Linters Formatters

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [terraform-linters/tflint](https://github.com/terraform-linters/tflint) | Go | 5712 | 2026-05-17 | A Pluggable Terraform Linter |
| [ayarotsky/diesel-guard](https://github.com/ayarotsky/diesel-guard) | Rust | 113 | 2026-05-03 | Linter for dangerous Postgres migration patterns in Diesel and SQLx |

#### Articles (1)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Code formatting: scalafmt and the git pre-commit hook](https://medium.com/zyseme-technology/code-formatting-scalafmt-and-the-git-pre-commit-hook-3de71d099514) | article | 2018-09 | fp-scala, language-runtimes |


<a id="shells-terminals"></a>

---

## Shells Terminals

#### Tools (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [wavetermdev/waveterm](https://github.com/wavetermdev/waveterm) | Go | 20483 | 2026-05-15 | An open-source, AI-integrated, cross-platform terminal for seamless workflows |

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [ratatui/ratatui](https://github.com/ratatui/ratatui) | Rust | 20484 | 2026-05-14 | A Rust crate for cooking up terminal user interfaces (TUIs) 👨‍🍳🐀 https://ratatui.rs |

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Windows Command-Line: Backgrounder](https://blogs.msdn.microsoft.com/commandline/2018/06/20/windows-command-line-backgrounder/) | article | 2018-07 | misc |
| [Windows Command-Line: The Evolution of the Windows Command-Line](https://blogs.msdn.microsoft.com/commandline/2018/06/27/windows-command-line-the-evolution-of-the-windows-command-line/) | article | 2018-07 | misc |


<a id="optics-lenses"></a>

---

## Optics Lenses

#### Libraries (1)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [optics-dev/Monocle](https://github.com/optics-dev/Monocle) | Scala | 1694 | 2026-05-14 | Optics library for Scala |


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

#### Unsorted (11)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [DioxusLabs/dioxus](https://github.com/DioxusLabs/dioxus) | Rust | 36064 | 2026-05-14 | Fullstack app framework for web, desktop, and mobile |
| [directus/directus](https://github.com/directus/directus) | TypeScript | 35726 | 2026-05-15 | The flexible backend for all your projects 🐰 Turn your DB into a headless CMS, admin panels, or apps with a... |
| [medusajs/medusa](https://github.com/medusajs/medusa) | TypeScript | 33424 | 2026-05-15 | The world's most flexible commerce platform |
| [SigNoz/signoz](https://github.com/SigNoz/signoz) | TypeScript | 26919 | 2026-05-17 | SigNoz is an open-source observability platform native to OpenTelemetry with logs, traces and metrics in a ... |
| [JetBrains/compose-multiplatform](https://github.com/JetBrains/compose-multiplatform) | Kotlin | 19067 | 2026-05-15 | Compose Multiplatform, a modern UI framework for Kotlin that makes building performant and beautiful user i... |
| [getlago/lago](https://github.com/getlago/lago) | Go | 9682 | 2026-05-15 | Open Source Metering and Usage Based Billing API ⭐️ Consumption tracking, Subscription management, Pricing ... |
| [Flagsmith/flagsmith](https://github.com/Flagsmith/flagsmith) | Python | 6364 | 2026-05-15 | Flagsmith is an open source feature flagging and remote config service |
| [lowdefy/lowdefy](https://github.com/lowdefy/lowdefy) | JavaScript | 2967 | 2026-05-16 | Build apps that AI can generate, humans can review, and teams can maintain |
| [medplum/medplum](https://github.com/medplum/medplum) | TypeScript | 2366 | 2026-05-17 | Medplum is a healthcare platform that helps you quickly develop high-quality compliant applications |
| [brightbeanxyz/brightbean-studio](https://github.com/brightbeanxyz/brightbean-studio) | Python | 1678 | 2026-05-15 | Open-source, self-hostable social media management platform |
| [openwallet-foundation/bifold-wallet](https://github.com/openwallet-foundation/bifold-wallet) | TypeScript | 192 | 2026-05-12 | Bifold is an extensible open-source React Native project designed to enhance the way we interact with digit... |

#### Articles (4)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [Electron is a hulking monstrosity of a WORA framework, and it needs to be replaced.](https://medium.com/@boundarybreaker/electron-is-a-hulking-monstrosity-of-a-wora-framework-and-it-needs-to-be-replaced-25e9d849b0e) | article | 2018-10 | frontend |
| [Lessons learned from creating a rich-text editor with real-time collaboration](https://ckeditor.com/blog/Lessons-learned-from-creating-a-rich-text-editor-with-real-time-collaboration/) | article | 2018-10 | frontend |
| [What should replace Electron as a WORA framework?](https://medium.com/@boundarybreaker/what-should-replace-electron-as-a-wora-framework-911d969eddaa) | article | 2018-10 | frontend |
| [React Native: A retrospective from the mobile-engineering team at Udacity](https://engineering.udacity.com/react-native-a-retrospective-from-the-mobile-engineering-team-at-udacity-89975d6a8102) | article | 2018-07 | frontend |


<a id="design-systems"></a>

---

## Design Systems

#### Articles (2)

| Title | Type | Date | Labels |
| :--- | :--- | :--- | :--- |
| [A developer’s guide to web design for non-designers](https://medium.freecodecamp.org/a-developers-guide-to-web-design-for-non-designers-1f64ce28c38d) | article | 2018-08 | frontend |
| [The UX behind designing better forms](https://uxdesign.cc/the-ux-behind-designing-better-forms-d6ebe7a817d2) | article | 2018-08 | frontend |


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
| [polyvariant/sttp-oauth2](https://github.com/polyvariant/sttp-oauth2) | Scala | 80 | 2026-05-13 | OAuth2 client library implemented in Scala using sttp |

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


<a id="awesome-lists"></a>

---

## Awesome Lists

#### Unsorted (41)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | — | 467388 | 2026-05-05 | 😎 Awesome lists about all kinds of interesting topics |
| [f/prompts.chat](https://github.com/f/prompts.chat) | HTML | 162418 | 2026-05-17 | f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free and open sour... |
| [Hack-with-Github/Awesome-Hacking](https://github.com/Hack-with-Github/Awesome-Hacking) | — | 112382 | 2026-05-07 | A collection of various awesome lists for hackers, pentesters and security researchers |
| [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | — | 80305 | 2026-05-17 | A collection of DESIGN.md files inspired by popular brand design systems |
| [awesomedata/awesome-public-datasets](https://github.com/awesomedata/awesome-public-datasets) | — | 75477 | 2026-05-14 | A topic-centric list of HQ open datasets |
| [josephmisiti/awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning) | Python | 72497 | 2026-05-12 | A curated list of awesome Machine Learning frameworks, libraries and software |
| [binhnguyennus/awesome-scalability](https://github.com/binhnguyennus/awesome-scalability) | — | 71063 | 2026-01-04 | The Patterns of Scalable, Reliable, and Performant Large-Scale Systems |
| [rust-unofficial/awesome-rust](https://github.com/rust-unofficial/awesome-rust) | Rust | 57356 | 2026-05-17 | A curated list of Rust code and resources |
| [DovAmir/awesome-design-patterns](https://github.com/DovAmir/awesome-design-patterns) | — | 47391 | 2024-10-25 | A curated list of software and architecture related design patterns |
| [e2b-dev/awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents) | — | 27881 | 2025-02-26 | A list of AI autonomous agents |
| [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) | — | 26348 | 2026-05-17 | :scream: A curated list of amazingly awesome OSINT |
| [carpedm20/awesome-hacking](https://github.com/carpedm20/awesome-hacking) | — | 16349 | 2024-06-02 | A curated list of awesome Hacking tutorials, tools and resources |
| [mfornos/awesome-microservices](https://github.com/mfornos/awesome-microservices) | — | 14295 | 2026-01-17 | A curated list of Microservice Architecture related principles and technologies |
| [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps) | Python | 12276 | 2026-05-09 | A collection of projects showcasing RAG, agents, workflows, and other AI use cases |
| [dhamaniasad/awesome-postgres](https://github.com/dhamaniasad/awesome-postgres) | — | 11903 | 2026-03-28 | A curated list of awesome PostgreSQL software, libraries, tools and resources, inspired by awesome-mysql |
| [lauris/awesome-scala](https://github.com/lauris/awesome-scala) | Python | 9223 | 2024-09-20 | A community driven list of useful Scala libraries, frameworks and software |
| [MrNeRF/awesome-3D-gaussian-splatting](https://github.com/MrNeRF/awesome-3D-gaussian-splatting) | HTML | 8618 | 2026-05-07 | Curated list of papers and resources focused on 3D Gaussian Splatting, intended to keep pace with the antic... |
| [grpc-ecosystem/awesome-grpc](https://github.com/grpc-ecosystem/awesome-grpc) | — | 8314 | 2025-10-28 | A curated list of useful resources for gRPC |
| [shuaibiyy/awesome-tf](https://github.com/shuaibiyy/awesome-tf) | — | 6503 | 2026-05-14 | Curated list of resources on HashiCorp's Terraform and OpenTofu |
| [korfuri/awesome-monorepo](https://github.com/korfuri/awesome-monorepo) | — | 5808 | 2024-08-16 | A curated list of awesome Monorepo tools, software and architectures |
| [sacridini/Awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) | — | 5045 | 2026-05-15 | Long list of geospatial tools and resources |
| [phodal/awesome-iot](https://github.com/phodal/awesome-iot) | Python | 4590 | 2026-05-17 | Awesome IoT |
| [sathishvj/awesome-gcp-certifications](https://github.com/sathishvj/awesome-gcp-certifications) | — | 4394 | 2026-03-30 | Google Cloud Platform Certification resources |
| [vijaythecoder/awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | — | 4262 | 2025-10-30 | An orchestrated sub agent dev team powered by claude code |
| [denji/awesome-http-benchmark](https://github.com/denji/awesome-http-benchmark) | — | 3753 | 2026-05-05 | HTTP(S) benchmark tools, testing/debugging, & restAPI (RESTful) |
| [xyflow/awesome-node-based-uis](https://github.com/xyflow/awesome-node-based-uis) | — | 3556 | 2025-06-29 | A curated list with resources about node-based UIs |
| [mcxiaoke/awesome-kotlin](https://github.com/mcxiaoke/awesome-kotlin) | — | 2859 | 2026-03-22 | A curated list of awesome Kotlin frameworks, libraries, documents and other resources |
| [ramnes/awesome-mongodb](https://github.com/ramnes/awesome-mongodb) | — | 2639 | 2026-04-20 | :leaves: A curated list of awesome MongoDB resources, libraries, tools and applications |
| [akuity/awesome-argo](https://github.com/akuity/awesome-argo) | — | 2435 | 2026-02-28 | A curated list of awesome projects and resources related to Argo (a CNCF graduated project) |
| [vaaaaanquish/Awesome-Rust-MachineLearning](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning) | JavaScript | 2255 | 2023-09-25 | This repository is a list of machine learning libraries written in Rust |
| [vonzosten/awesome-LangGraph](https://github.com/vonzosten/awesome-LangGraph) | JavaScript | 1797 | 2026-05-15 | An index of the LangChain + LangGraph ecosystem: concepts, projects, tools, templates, and guides for LLM &... |
| [passy/awesome-recursion-schemes](https://github.com/passy/awesome-recursion-schemes) | — | 1292 | 2024-04-25 | Resources for learning and using recursion schemes |
| [jbmusso/awesome-graph](https://github.com/jbmusso/awesome-graph) | — | 1255 | 2026-02-26 | A curated list of resources for graph databases and graph computing tools |
| [xephonhq/awesome-time-series-database](https://github.com/xephonhq/awesome-time-series-database) | JavaScript | 885 | 2023-07-14 | :clock7: A curated list of awesome time series databases, benchmarks and papers |
| [open-policy-agent/awesome-opa](https://github.com/open-policy-agent/awesome-opa) | — | 884 | 2026-04-24 | A curated list of OPA related tools, frameworks and articles |
| [zed-industries/awesome-gpui](https://github.com/zed-industries/awesome-gpui) | — | 836 | 2026-05-11 | Awesome projects, built with or for GPUI! |
| [philippemerle/Awesome-Kubernetes-Architecture-Diagrams](https://github.com/philippemerle/Awesome-Kubernetes-Architecture-Diagrams) | — | 505 | 2026-05-03 | Awesome Kubernetes Architecture Diagrams |
| [animo/awesome-self-sovereign-identity](https://github.com/animo/awesome-self-sovereign-identity) | — | 392 | 2025-11-11 | An awesome list of self-sovereign identity resources |
| [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) | Python | 375 | 2026-05-16 | Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them |
| [graphgeeks-lab/awesome-graph-universe](https://github.com/graphgeeks-lab/awesome-graph-universe) | — | 147 | 2025-08-26 | A curated list of resources for graph-related topics, including graph databases, analytics and science |
| [antonbabenko/awesome-terraform-compliance](https://github.com/antonbabenko/awesome-terraform-compliance) | — | 124 | 2026-04-28 | Awesome Terraform Compliance - tools, frameworks, and resources for implementing compliance, security, and ... |


<a id="learning-resources"></a>

---

## Learning Resources

#### Unsorted (9)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) | Markdown | 502034 | 2026-02-21 | Master programming by recreating your favorite technologies from scratch |
| [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer) | Python | 349038 | 2026-03-20 | Learn how to design large-scale systems |
| [papers-we-love/papers-we-love](https://github.com/papers-we-love/papers-we-love) | Shell | 106257 | 2026-05-17 | Papers from the computer science community to read and discuss |
| [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | — | 48322 | 2025-04-10 | Bootstrap Kubernetes the hard way |
| [dwmkerr/hacker-laws](https://github.com/dwmkerr/hacker-laws) | HTML | 27138 | 2026-02-06 | 🧠 Laws, Theories, Principles and Patterns for developers and technologists |
| [NirDiamant/agents-towards-production](https://github.com/NirDiamant/agents-towards-production) | Jupyter Notebook | 19870 | 2026-05-15 | End-to-end, code-first tutorials for building production-grade GenAI agents |
| [ryanburgess/engineer-manager](https://github.com/ryanburgess/engineer-manager) | JavaScript | 10703 | 2026-03-02 | A list of engineering manager resource links |
| [ZoranPandovski/al-go-rithms](https://github.com/ZoranPandovski/al-go-rithms) | Jupyter Notebook | 1374 | 2024-06-18 | :musical_note: Algorithms written in different programming languages -  https://zoranpandovski.github.io/al... |
| [ZoranPandovski/design-patterns](https://github.com/ZoranPandovski/design-patterns) | Java | 387 | 2024-12-13 | :briefcase: Design patterns written in different programming languages :triangular_ruler: |

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


<a id="unsorted"></a>

---

## Unsorted

#### Tools (2)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [curl/curl](https://github.com/curl/curl) | C | 41896 | 2026-05-17 | A command line tool and library for transferring data with URL syntax, supporting DICT, FILE, FTP, FTPS, GO... |
| [ImageMagick/ImageMagick](https://github.com/ImageMagick/ImageMagick) | C | 16459 | 2026-05-17 | ImageMagick is a free, open-source software suite for creating, editing, converting, and displaying images |

#### Unsorted (165)

| Repo | Language | Stars | Last pushed | Description |
| :--- | :--- | ---: | :--- | :--- |
| [github/spec-kit](https://github.com/github/spec-kit) | Python | 101467 | 2026-05-15 | 💫 Toolkit to help you get started with Spec-Driven Development |
| [mattpocock/skills](https://github.com/mattpocock/skills) | Shell | 88756 | 2026-05-13 | Skills for Real Engineers |
| [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Python | 57237 | 2026-05-17 | Ultralytics YOLO 🚀 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | TypeScript | 48649 | 2026-05-14 | Spec-driven development (SDD) for AI coding assistants |
| [Raphire/Win11Debloat](https://github.com/Raphire/Win11Debloat) | PowerShell | 46352 | 2026-05-17 | A simple, lightweight PowerShell script that allows you to remove pre-installed apps, disable telemetry, as... |
| [karanpratapsingh/system-design](https://github.com/karanpratapsingh/system-design) | — | 43284 | 2026-04-02 | Learn how to design systems at scale and prepare for system design interviews |
| [juspay/hyperswitch](https://github.com/juspay/hyperswitch) | Rust | 42705 | 2026-05-17 | An open source payments switch written in Rust to make payments fast, reliable and affordable |
| [novuhq/novu](https://github.com/novuhq/novu) | TypeScript | 38986 | 2026-05-17 | The open-source notification infrastructure |
| [abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus) | TypeScript | 38731 | 2026-05-17 | GitNexus: The Zero-Server Code Intelligence Engine -       GitNexus is a client-side knowledge graph creato... |
| [GyulyVGC/sniffnet](https://github.com/GyulyVGC/sniffnet) | Rust | 37591 | 2026-05-15 | Comfortably monitor your Internet traffic 🕵️‍♂️ |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Jupyter Notebook | 35723 | 2026-03-01 | Anthropic's Interactive Prompt Engineering Tutorial |
| [casey/just](https://github.com/casey/just) | Rust | 33706 | 2026-05-17 | 🤖 Just a command runner |
| [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex) | Python | 31541 | 2026-05-15 | 📑 PageIndex: Document Index for Vectorless, Reasoning-based RAG |
| [openssl/openssl](https://github.com/openssl/openssl) | C | 30163 | 2026-05-15 | General purpose TLS and crypto library |
| [gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Go | 27052 | 2026-05-13 | Find secrets with Gitleaks 🔑 |
| [nsqio/nsq](https://github.com/nsqio/nsq) | Go | 25727 | 2025-07-13 | A realtime distributed messaging platform |
| [anthropics/financial-services](https://github.com/anthropics/financial-services) | Python | 24328 | 2026-05-15 |  |
| [cube-js/cube](https://github.com/cube-js/cube) | Rust | 19979 | 2026-05-17 | 📊 Cube Core is open-source semantic layer for AI, BI and embedded analytics |
| [mjmlio/mjml](https://github.com/mjmlio/mjml) | JavaScript | 18058 | 2026-05-12 | MJML: the only framework that makes responsive-email easy |
| [stefan-jansen/machine-learning-for-trading](https://github.com/stefan-jansen/machine-learning-for-trading) | Jupyter Notebook | 17339 | 2024-08-18 | Code for Machine Learning for Algorithmic Trading, 2nd edition |
| [direnv/direnv](https://github.com/direnv/direnv) | Go | 15082 | 2026-03-31 | unclutter your .profile |
| [apache/dolphinscheduler](https://github.com/apache/dolphinscheduler) | Java | 14272 | 2026-05-17 | Apache DolphinScheduler is the modern data orchestration platform |
| [prowler-cloud/prowler](https://github.com/prowler-cloud/prowler) | Python | 13829 | 2026-05-15 | Prowler is the world’s most widely used open-source cloud security platform that automates security and com... |
| [ory/kratos](https://github.com/ory/kratos) | Go | 13645 | 2026-05-15 | Headless cloud-native authentication and identity management written in Go |
| [Unleash/unleash](https://github.com/Unleash/unleash) | TypeScript | 13480 | 2026-05-15 | Open-source feature management platform |
| [rayon-rs/rayon](https://github.com/rayon-rs/rayon) | Rust | 13005 | 2026-04-23 | Rayon: A data parallelism library for Rust |
| [instaloader/instaloader](https://github.com/instaloader/instaloader) | Python | 12378 | 2026-04-15 | Download pictures (or videos) along with their captions and other metadata from Instagram |
| [hmemcpy/milewski-ctfp-pdf](https://github.com/hmemcpy/milewski-ctfp-pdf) | TeX | 11600 | 2026-04-08 | Bartosz Milewski's 'Category Theory for Programmers' unofficial PDF and LaTeX source |
| [longbridge/gpui-component](https://github.com/longbridge/gpui-component) | Rust | 11459 | 2026-05-17 | Rust GUI components for building fantastic cross-platform desktop application by using GPUI |
| [ulid/spec](https://github.com/ulid/spec) | — | 10738 | 2024-07-20 | The canonical spec for ulid |
| [microsoft/presidio](https://github.com/microsoft/presidio) | Python | 8102 | 2026-05-17 | An open-source framework for detecting, redacting, masking, and anonymizing sensitive data (PII) across tex... |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | TypeScript | 7781 | 2026-05-17 | Open Source Feature Flags, Experimentation, and Product Analytics |
| [h2non/imaginary](https://github.com/h2non/imaginary) | Go | 6050 | 2025-11-08 | Fast, simple, scalable, Docker-ready HTTP microservice for high-level image processing |
| [craft-ai-agents/craft-agents-oss](https://github.com/craft-ai-agents/craft-agents-oss) | TypeScript | 5993 | 2026-05-15 |  |
| [cloudevents/spec](https://github.com/cloudevents/spec) | Python | 5762 | 2026-05-07 | CloudEvents Specification |
| [killbill/killbill](https://github.com/killbill/killbill) | Java | 5539 | 2026-05-16 | Open-Source Subscription Billing & Payments Platform |
| [segmentio/ksuid](https://github.com/segmentio/ksuid) | Go | 5259 | 2023-10-04 | K-Sortable Globally Unique IDs |
| [asyncapi/spec](https://github.com/asyncapi/spec) | JavaScript | 5183 | 2026-05-08 | The AsyncAPI specification allows you to create machine-readable definitions of your asynchronous APIs |
| [metalbear-co/mirrord](https://github.com/metalbear-co/mirrord) | Rust | 5066 | 2026-05-17 | Run local code as if it were a pod in a remote Kubernetes cluster: real env vars, DNS, network, traffic |
| [reactive-streams/reactive-streams-jvm](https://github.com/reactive-streams/reactive-streams-jvm) | Java | 4876 | 2024-03-13 | Reactive Streams Specification for the JVM |
| [octokatherine/readme.so](https://github.com/octokatherine/readme.so) | JavaScript | 4637 | 2026-03-13 | An online drag-and-drop editor to easily build READMEs |
| [polynote/polynote](https://github.com/polynote/polynote) | Jupyter Notebook | 4596 | 2026-01-27 | A better notebook for Scala (and more) |
| [petgraph/petgraph](https://github.com/petgraph/petgraph) | Rust | 3905 | 2026-04-04 | Graph data structure library for Rust |
| [chronotope/chrono](https://github.com/chronotope/chrono) | Rust | 3854 | 2026-04-06 | Date and time library for Rust |
| [juhaku/utoipa](https://github.com/juhaku/utoipa) | Rust | 3842 | 2026-05-17 | Simple, Fast, Code first and Compile time generated OpenAPI documentation for Rust |
| [helidon-io/helidon](https://github.com/helidon-io/helidon) | Java | 3789 | 2026-05-15 | Java libraries for writing microservices |
| [trustwallet/wallet-core](https://github.com/trustwallet/wallet-core) | C++ | 3514 | 2026-05-15 | Cross-platform, cross-blockchain wallet library |
| [paralleldrive/cuid](https://github.com/paralleldrive/cuid) | JavaScript | 3507 | 2026-05-15 | Deprecated collision-resistant id spec |
| [GStreamer/gstreamer](https://github.com/GStreamer/gstreamer) | C | 3169 | 2026-05-16 | GStreamer open-source multimedia framework |
| [inspec/inspec](https://github.com/inspec/inspec) | Ruby | 3068 | 2026-05-15 | InSpec: Auditing and Testing Framework |
| [paradigmxyz/artemis](https://github.com/paradigmxyz/artemis) | Rust | 2941 | 2024-03-05 | A simple, modular, and fast framework for writing MEV bots in Rust |
| [event-catalog/eventcatalog](https://github.com/event-catalog/eventcatalog) | TypeScript | 2702 | 2026-05-15 | The architecture catalog for distributed systems |
| [opencve/opencve](https://github.com/opencve/opencve) | Python | 2695 | 2026-05-11 | Vulnerability Intelligence Platform |
| [engineer-man/piston](https://github.com/engineer-man/piston) | JavaScript | 2693 | 2026-03-26 | A high performance general purpose code execution engine |
| [facet-rs/facet](https://github.com/facet-rs/facet) | Rust | 2473 | 2026-05-11 | Rust reflection, serialization, deserialization, pretty printing, etc |
| [kpcyrd/sn0int](https://github.com/kpcyrd/sn0int) | Rust | 2437 | 2026-05-15 | Semi-automatic OSINT framework and package manager |
| [zhiburt/tabled](https://github.com/zhiburt/tabled) | Rust | 2333 | 2026-04-25 | An easy to use library for pretty print tables of Rust structs and enums |
| [hapifhir/hapi-fhir](https://github.com/hapifhir/hapi-fhir) | Java | 2327 | 2026-05-16 | 🔥 HAPI FHIR - Java API for HL7 FHIR Clients and Servers |
| [GoogleCloudPlatform/gcsfuse](https://github.com/GoogleCloudPlatform/gcsfuse) | Go | 2267 | 2026-05-15 | A user-space file system for interacting with Google Cloud Storage |
| [fitzgen/bumpalo](https://github.com/fitzgen/bumpalo) | Rust | 2203 | 2026-04-27 | A fast bump allocation arena for Rust |
| [est31/cargo-udeps](https://github.com/est31/cargo-udeps) | Rust | 2100 | 2026-04-29 | Find unused dependencies in Cargo.toml |
| [BurntSushi/fst](https://github.com/BurntSushi/fst) | Rust | 2088 | 2024-09-25 | Represent large sets and maps compactly with finite state transducers |
| [googleapis/google-cloud-java](https://github.com/googleapis/google-cloud-java) | Java | 2047 | 2026-05-17 | Google Cloud Client Library for Java |
| [pravega/pravega](https://github.com/pravega/pravega) | Java | 2003 | 2025-03-02 | Pravega - Streaming as a new software defined storage primitive |
| [RabbyHub/Rabby](https://github.com/RabbyHub/Rabby) | TypeScript | 1838 | 2026-05-15 | The game-changing wallet for Ethereum and all EVM chains |
| [Swatinem/rust-cache](https://github.com/Swatinem/rust-cache) | TypeScript | 1819 | 2026-05-12 | A GitHub Action that implements smart caching for rust/cargo projects |
| [typelevel/spire](https://github.com/typelevel/spire) | Scala | 1775 | 2026-05-10 | Powerful new number types and numeric abstractions for Scala |
| [greyblake/nutype](https://github.com/greyblake/nutype) | Rust | 1726 | 2026-05-03 | Rust newtype with guarantees  🇺🇦 🦀 |
| [standard-webhooks/standard-webhooks](https://github.com/standard-webhooks/standard-webhooks) | Java | 1665 | 2026-05-15 | The Standard Webhooks specification |
| [java-json-tools/json-schema-validator](https://github.com/java-json-tools/json-schema-validator) | Java | 1643 | 2024-07-17 | A JSON Schema validation implementation in pure Java, which aims for correctness and performance, in that o... |
| [la10736/rstest](https://github.com/la10736/rstest) | Rust | 1554 | 2026-03-26 | Fixture-based test framework for Rust |
| [stakpak/agent](https://github.com/stakpak/agent) | Rust | 1545 | 2026-05-16 | Ship your code, on autopilot |
| [colin-kiegel/rust-derive-builder](https://github.com/colin-kiegel/rust-derive-builder) | Rust | 1538 | 2026-01-02 | derive builder implementation for rust structs |
| [Fazecast/jSerialComm](https://github.com/Fazecast/jSerialComm) | C | 1512 | 2025-11-07 | Platform-independent serial port access for Java |
| [softwaremill/sttp](https://github.com/softwaremill/sttp) | Scala | 1504 | 2026-05-14 | The Scala HTTP client you always wanted! |
| [OpenSLO/OpenSLO](https://github.com/OpenSLO/OpenSLO) | Makefile | 1490 | 2025-11-25 | Open specification for defining and expressing service level objectives (SLO) |
| [json4s/json4s](https://github.com/json4s/json4s) | Scala | 1486 | 2026-05-11 | JSON library |
| [kbknapp/cargo-outdated](https://github.com/kbknapp/cargo-outdated) | Rust | 1397 | 2026-05-06 | A cargo subcommand for displaying when Rust dependencies are out of date |
| [cookpete/auto-changelog](https://github.com/cookpete/auto-changelog) | JavaScript | 1384 | 2026-05-05 | Command line tool for generating a changelog from git tags and commit history |
| [Danau5tin/multi-agent-coding-system](https://github.com/Danau5tin/multi-agent-coding-system) | Python | 1376 | 2025-11-03 | Reached #13 on Stanford's Terminal Bench leaderboard |
| [Nukesor/comfy-table](https://github.com/Nukesor/comfy-table) | Rust | 1337 | 2026-05-04 | :large_orange_diamond: Build beautiful terminal tables with automatic content wrapping |
| [time-rs/time](https://github.com/time-rs/time) | Rust | 1308 | 2026-05-09 | Date and time handling in Rust |
| [bbottema/simple-java-mail](https://github.com/bbottema/simple-java-mail) | Java | 1292 | 2026-04-01 | Simple API, Complex Emails (Jakarta Mail smtp wrapper) |
| [Priivacy-ai/spec-kitty](https://github.com/Priivacy-ai/spec-kitty) | Python | 1235 | 2026-05-17 | Spec-Driven Development for serious software developers |
| [nst/JSONTestSuite](https://github.com/nst/JSONTestSuite) | C++ | 1142 | 2024-11-22 | A comprehensive test suite for RFC 8259 compliant JSON parsers |
| [com-lihaoyi/fastparse](https://github.com/com-lihaoyi/fastparse) | Scala | 1135 | 2026-01-14 | Writing Fast Parsers Fast in Scala |
| [edgurgel/poxa](https://github.com/edgurgel/poxa) | Elixir | 1086 | 2024-06-30 | Pusher server implementation compatible with Pusher client libraries |
| [scrapfly/scrapfly-scrapers](https://github.com/scrapfly/scrapfly-scrapers) | Python | 980 | 2026-05-16 | Scalable Python web scraping scripts for +40 popular domains |
| [zalando/problem](https://github.com/zalando/problem) | Java | 946 | 2026-05-12 | A Java library that implements application/problem+json |
| [typelevel/squants](https://github.com/typelevel/squants) | Scala | 931 | 2026-05-12 | The Scala API for Quantities, Units of Measure and Dimensional Analysis |
| [everit-org/json-schema](https://github.com/everit-org/json-schema) | Java | 901 | 2025-08-01 | JSON Schema validator for java, based on the org.json API |
| [tower-rs/tower-http](https://github.com/tower-rs/tower-http) | Rust | 877 | 2026-05-14 | HTTP specific Tower utilities |
| [ocsf/ocsf-schema](https://github.com/ocsf/ocsf-schema) | — | 826 | 2026-05-13 | OCSF Schema |
| [softwaremill/magnolia](https://github.com/softwaremill/magnolia) | Scala | 796 | 2026-05-08 | Easy, fast, transparent generic derivation of typeclass instances |
| [symbolica-dev/symbolica](https://github.com/symbolica-dev/symbolica) | Rust | 771 | 2026-05-16 | A modern computer algebra library for Python and Rust |
| [com-lihaoyi/upickle](https://github.com/com-lihaoyi/upickle) | Scala | 766 | 2026-02-27 | uPickle: a simple, fast, dependency-free JSON & Binary (MessagePack) serialization library for Scala |
| [RocketGod-git/HackRF-Treasure-Chest](https://github.com/RocketGod-git/HackRF-Treasure-Chest) | C | 714 | 2024-11-13 | HackRF software and captures by everyone and for everyone |
| [oleg-py/better-monadic-for](https://github.com/oleg-py/better-monadic-for) | Scala | 712 | 2024-05-07 | Desugaring scala `for` without implicit `withFilter`s |
| [RocketGod-git/flipper-zero-rf-jammer](https://github.com/RocketGod-git/flipper-zero-rf-jammer) | C | 689 | 2026-05-10 | Frequency and preset adjustable subghz radio frequency jammer for Flipper Zero |
| [scoverage/sbt-scoverage](https://github.com/scoverage/sbt-scoverage) | Scala | 656 | 2026-05-12 | sbt plugin for scoverage |
| [biojava/biojava](https://github.com/biojava/biojava) | Java | 621 | 2026-05-05 | :book::microscope::coffee: BioJava is an open-source project dedicated to providing a Java library for proc... |
| [FGRibreau/spinners](https://github.com/FGRibreau/spinners) | Rust | 591 | 2026-05-02 | 🛎 60+ Elegant terminal spinners for Rust |
| [sevenlabs-hq/carbon](https://github.com/sevenlabs-hq/carbon) | Rust | 591 | 2026-05-03 | Carbon is an indexing framework on Solana |
| [arcadesdude/BRU](https://github.com/arcadesdude/BRU) | PowerShell | 547 | 2026-01-05 | Bloatware Removal Utility, for automating removal of pre-installed, factory bloatware from devices running ... |
| [RocketGod-git/ProtoPirate](https://github.com/RocketGod-git/ProtoPirate) | C | 539 | 2026-05-13 | Flipper Zero Protocol Pirate |
| [seancfoley/IPAddress](https://github.com/seancfoley/IPAddress) | Java | 532 | 2026-05-15 | Java library for handling IP addresses and subnets, both IPv4 and IPv6 |
| [aventrix/jnanoid](https://github.com/aventrix/jnanoid) | Java | 516 | 2023-12-21 | A unique string ID generator for Java |
| [jchambers/java-otp](https://github.com/jchambers/java-otp) | Java | 492 | 2026-05-01 | A one-time password (HOTP/TOTP) library for Java |
| [KStateMachine/kstatemachine](https://github.com/KStateMachine/kstatemachine) | Kotlin | 491 | 2026-01-23 | Powerful Kotlin Multiplatform library with clean DSL syntax for creating complex state machines and statech... |
| [openwallet-foundation/acapy](https://github.com/openwallet-foundation/acapy) | Python | 484 | 2026-05-12 | ACA-Py is a foundation for building decentralized identity applications and services running in non-mobile ... |
| [f4b6a3/ulid-creator](https://github.com/f4b6a3/ulid-creator) | Java | 448 | 2026-02-21 | A Java library for generating Universally Unique Lexicographically Sortable Identifiers (ULID) |
| [cloudevents/sdk-java](https://github.com/cloudevents/sdk-java) | Java | 438 | 2026-05-08 | Java SDK for CloudEvents |
| [ThreeTen/threeten-extra](https://github.com/ThreeTen/threeten-extra) | Java | 421 | 2025-08-20 | Provides additional date-time classes that complement those in JDK 8 |
| [CVEProject/cve-schema](https://github.com/CVEProject/cve-schema) | HTML | 407 | 2026-01-30 | This repository is used for the development of the CVE JSON record format |
| [ZerkerEOD/krakenhashes](https://github.com/ZerkerEOD/krakenhashes) | Go | 390 | 2026-05-16 |  |
| [velvia/links](https://github.com/velvia/links) | Scala | 384 | 2026-04-24 | Just a bunch of useful links |
| [gdt050579/AppCUI-rs](https://github.com/gdt050579/AppCUI-rs) | Rust | 371 | 2026-05-17 | AppCUI is a fast, cross-platform console and text-based user interface (CUI/TUI) framework for Rust |
| [JavaMoney/jsr354-api](https://github.com/JavaMoney/jsr354-api) | Java | 370 | 2026-05-01 | JSR 354 - Money and Currency API |
| [JavaMoney/jsr354-ri](https://github.com/JavaMoney/jsr354-ri) | Java | 369 | 2026-04-01 | JSR 354 - Moneta: Reference Implementation |
| [thatdot/quine](https://github.com/thatdot/quine) | Scala | 359 | 2026-05-15 | Quine • a streaming graph • https://quine.io • Discord: https://discord.gg/GMhd8TE4MR |
| [mangstadt/biweekly](https://github.com/mangstadt/biweekly) | Java | 347 | 2025-06-18 | biweekly is an iCalendar library written in Java |
| [openwallet-foundation/credo-ts](https://github.com/openwallet-foundation/credo-ts) | TypeScript | 343 | 2026-05-14 | Typescript framework for building decentralized identity and verifiable credential solutions |
| [xerial/sbt-sonatype](https://github.com/xerial/sbt-sonatype) | Scala | 341 | 2026-02-13 | A sbt plugin for publishing Scala/Java projects to the Maven central |
| [Trendyol/stove](https://github.com/Trendyol/stove) | Kotlin | 308 | 2026-05-11 | Stove: The easiest way of writing e2e/component tests for your JVM back-end app with Kotlin |
| [GoogleCloudPlatform/jit-groups](https://github.com/GoogleCloudPlatform/jit-groups) | Java | 287 | 2026-05-13 | JIT Groups is an open source application that lets you implement secure, self-service access management for... |
| [grate-devs/grate](https://github.com/grate-devs/grate) | C# | 287 | 2026-04-29 | grate - the SQL scripts migration runner |
| [fraktalio/fmodel](https://github.com/fraktalio/fmodel) | Kotlin | 282 | 2026-05-14 | Functional, Algebraic and Reactive domain modeling with Kotlin (Multiplatform) |
| [walt-id/waltid-identity](https://github.com/walt-id/waltid-identity) | Kotlin | 278 | 2026-05-16 | All-in-one open-source identity and wallet toolkit |
| [lomigmegard/akka-http-cors](https://github.com/lomigmegard/akka-http-cors) | Scala | 252 | 2026-03-27 | Akka Http directives implementing the CORS specifications defined by W3C |
| [neogenie/fastnum](https://github.com/neogenie/fastnum) | Rust | 252 | 2025-12-28 | Fixed-size decimal numbers implemented in pure Rust |
| [clitic/kdam](https://github.com/clitic/kdam) | Rust | 245 | 2026-01-06 | A console progress bar library for Rust |
| [CVEProject/cve-services](https://github.com/CVEProject/cve-services) | JavaScript | 244 | 2026-05-14 | This repo contains the source for the CVE Services API |
| [j256/simplemagic](https://github.com/j256/simplemagic) | Java | 241 | 2026-04-22 | Simple file magic number and content-type library which provides mime-type determination from files and byt... |
| [Comcast/ip4s](https://github.com/Comcast/ip4s) | Scala | 230 | 2026-05-13 | Defines immutable, safe data structures for describing IP addresses, multicast joins, socket addresses and ... |
| [mgrachev/update-informer](https://github.com/mgrachev/update-informer) | Rust | 225 | 2026-03-27 | Update informer for CLI/GUI applications written in Rust 🦀 |
| [FraunhoferIOSB/FROST-Server](https://github.com/FraunhoferIOSB/FROST-Server) | Java | 222 | 2026-05-17 | A Complete Server implementation of the OGC SensorThings API |
| [kevincianfarini/alchemist](https://github.com/kevincianfarini/alchemist) | Kotlin | 175 | 2026-05-14 | Type safe management and arithmetic of physical units |
| [svroonland/rezilience](https://github.com/svroonland/rezilience) | Scala | 163 | 2026-05-12 | ZIO-native utilities for making resilient distributed systems |
| [openwallet-foundation/acapy-vc-authn-oidc](https://github.com/openwallet-foundation/acapy-vc-authn-oidc) | Python | 157 | 2026-05-14 |  |
| [erikerlandson/coulomb](https://github.com/erikerlandson/coulomb) | Scala | 152 | 2026-05-04 | coulomb: unit analysis for Scala |
| [plokhotnyuk/rtree2d](https://github.com/plokhotnyuk/rtree2d) | Scala | 143 | 2026-05-04 | RTree2D is a 2D immutable R-tree for ultra-fast nearest and intersection queries in plane and spherical coo... |
| [GoogleCloudPlatform/inspec-gcp-cis-benchmark](https://github.com/GoogleCloudPlatform/inspec-gcp-cis-benchmark) | Ruby | 135 | 2026-01-06 | GCP CIS 4.0.0 Benchmark InSpec Profile |
| [disintegrate-es/disintegrate](https://github.com/disintegrate-es/disintegrate) | Rust | 121 | 2026-05-12 | Disintegrate Rust library |
| [scodec/scodec-bits](https://github.com/scodec/scodec-bits) | Scala | 119 | 2026-05-07 | Provides immutable datatypes for working with bits and bytes |
| [goSprinto/compliance-skills](https://github.com/goSprinto/compliance-skills) | — | 106 | 2026-05-08 |  |
| [hellgrenj/Rumpel](https://github.com/hellgrenj/Rumpel) | C# | 100 | 2023-10-27 | Simple, opinionated and automated consumer-driven contract testing for your JSON API's |
| [electrolux-oss/infrakitchen](https://github.com/electrolux-oss/infrakitchen) | Python | 97 | 2026-05-16 | InfraKitchen is an open source Developer Platform that brings Platform Engineering practices to infrastruct... |
| [irahulstomar/cosmo-tui](https://github.com/irahulstomar/cosmo-tui) | Python | 93 | 2026-04-28 | A terminal dashboard for NASA's open data |
| [taiki-e/easy-ext](https://github.com/taiki-e/easy-ext) | Rust | 88 | 2026-05-02 | A lightweight attribute macro for easily writing extension trait pattern |
| [business4s/decisions4s](https://github.com/business4s/decisions4s) | Scala | 82 | 2026-05-14 | Simple, Business-friendly Decisions Engine for Scala |
| [Artem-Romanenia/o2o](https://github.com/Artem-Romanenia/o2o) | Rust | 74 | 2025-11-20 | Object to Object mapper for Rust |
| [KaraZajac/KAT](https://github.com/KaraZajac/KAT) | Rust | 72 | 2026-05-17 | Keyfob Analysis Tool |
| [tmattsson/gs1utils](https://github.com/tmattsson/gs1utils) | Java | 64 | 2024-01-26 | Utilities for GS1 barcodes |
| [VirgilSecurity/virgil-e3kit-js](https://github.com/VirgilSecurity/virgil-e3kit-js) | TypeScript | 60 | 2024-05-28 | E3Kit is a security framework that simplifies work with Virgil services and presents the easiest way to add... |
| [fraktalio/fmodel-rust](https://github.com/fraktalio/fmodel-rust) | Rust | 57 | 2026-05-08 | Domain modeling |
| [L-yang-yang/cugenopt](https://github.com/L-yang-yang/cugenopt) | Cuda | 47 | 2026-03-30 | A GPU-accelerated general-purpose metaheuristic framework for combinatorial optimization |
| [atholbro/paseto](https://github.com/atholbro/paseto) | Kotlin | 41 | 2026-05-01 | Java Implementation of Platform-Agnostic Security Tokens - https://paseto.io |
| [lasantosr/model-mapper](https://github.com/lasantosr/model-mapper) | Rust | 35 | 2026-04-18 | Derive macro to map between different types |
| [opencve/opencve-kb](https://github.com/opencve/opencve-kb) | — | 32 | 2026-05-17 |  |
| [FraunhoferIOSB/FROST-Client](https://github.com/FraunhoferIOSB/FROST-Client) | Java | 30 | 2026-05-15 | Library implementing a client interface to the SensorThingsAPI |
| [bcgov/indy-tails-server](https://github.com/bcgov/indy-tails-server) | Python | 29 | 2026-04-13 | This software stores and makes available tails files for use with Hyperledger Indy |
| [thenativeweb/eventsourcingdb-client-rust](https://github.com/thenativeweb/eventsourcingdb-client-rust) | Rust | 18 | 2026-05-11 | The official Rust client SDK for EventSourcingDB |
| [the-codeboy/Piston4J](https://github.com/the-codeboy/Piston4J) | Java | 12 | 2025-12-27 | A Java Wrapper for Piston (https://github.com/engineer-man/piston) |
| [openwallet-foundation/acapy-plugins](https://github.com/openwallet-foundation/acapy-plugins) | Python | 10 | 2026-05-13 | aries-acapy-plugins |
| [jahwag/clem](https://github.com/jahwag/clem) | Go | 7 | 2026-05-17 | Continuously Looping Engineering Machines |

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
- [_archived/tools.md](./_archived/tools.md) — 53 archived/EOL/stale repos.
<!-- END: archived -->

---

## License

CC0 1.0 Universal — see [LICENSE](./LICENSE).

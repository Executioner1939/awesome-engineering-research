# moondocs

Ingests the moonrepo.dev documentation into a typed knowledge graph on
FalkorDB and surfaces undocumented behaviour by finding edges with no
source-prose backing.

## Run end-to-end

```
make up              # start FalkorDB
make scrape          # firecrawl -> data/raw/
make extract-structural   # deterministic + Sonnet -> data/extracted/
make extract-prose   # nano-graphrag -> data/prose/
make load            # both passes into FalkorDB
make gaps            # gap report -> reports/gaps-{ts}.md
```

Browse the graph at `http://localhost:${FALKOR_BROWSER_PORT}` and run
Cypher with graph name `moondocs`.

## Stack

- FalkorDB 4.18.x (graph + HNSW vector index)
- Firecrawl Python SDK 4.26
- nano-graphrag 0.0.8.2 wired to Claude Sonnet + local fastembed
- Anthropic SDK 0.102 (Sonnet subagents for structural extraction)
- fastembed BGE-small (resolution + chunk embeddings)

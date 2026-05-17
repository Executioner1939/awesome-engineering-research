.PHONY: help up down logs ps install scrape ingest parse extract-structural extract-prose resolve load query gaps run-all reset

PY ?= python -m moondocs

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-22s\033[0m %s\n", $$1, $$2}'

install: ## Install Python deps into the current env
	pip install -e .

up: ## Start FalkorDB in detached mode
	docker compose up -d
	@echo "FalkorDB on $${FALKOR_HOST:-localhost}:$${FALKOR_PORT:-6379}, browser on :$${FALKOR_BROWSER_PORT:-3000}"

down: ## Stop FalkorDB
	docker compose down

logs: ## Tail FalkorDB logs
	docker compose logs -f

ps: ## Show running containers
	docker compose ps

scrape: ## Firecrawl skill: download moonrepo.dev/docs+/guides -> .firecrawl/
	firecrawl experimental download https://moonrepo.dev \
	  --include-paths "/docs,/guides" --only-main-content --limit 500 -y

ingest: ## Adapt .firecrawl/ -> data/raw/{slug}.json
	$(PY) ingest

parse: ## Parse markdown -> data/parsed/
	$(PY) parse

extract-structural: ## Deterministic + Sonnet pass -> data/extracted/
	$(PY) extract-structural

extract-prose: ## nano-graphrag pass -> data/prose/
	$(PY) extract-prose

resolve: ## Entity resolution -> data/extracted/_canonical.json
	$(PY) resolve

load: ## Load both passes into FalkorDB
	$(PY) load

query: ## Open a Cypher REPL against the moondocs graph
	docker compose exec persistence-falkordb redis-cli GRAPH.QUERY moondocs 'MATCH (n) RETURN labels(n)[0] AS label, count(*) AS c'

gaps: ## Write gap-finding report -> reports/gaps-{ts}.md
	$(PY) gaps

run-all: ingest parse extract-structural extract-prose resolve load gaps ## Full pipeline after `make scrape`

reset: ## Tear down container, volume, and derived data
	docker compose down -v
	rm -rf data/parsed data/extracted data/prose reports/gaps-*.md

"""moondocs CLI.

Each subcommand is a thin wrapper that loads dotenv then dispatches to
the module's main(). The interesting work lives in the module files —
this is here so `make scrape`, `make load`, etc. all resolve through
`python -m moondocs <stage>`.
"""
from __future__ import annotations

import typer
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer(no_args_is_help=True, add_completion=False)


@app.command()
def ingest() -> None:
    """Convert .firecrawl/ download output -> data/raw/{slug}.json."""
    from . import ingest as m

    m.main()


@app.command()
def parse() -> None:
    """Parse markdown -> data/parsed/."""
    from . import parse as m

    m.parse_all()


@app.command("extract-structural")
def extract_structural() -> None:
    """Deterministic pass -> data/extracted/{slug}.det.json.
    The LLM pass runs as separate Sonnet subagents writing data/extracted/_llm/.
    """
    from . import structural as m

    m.main()


@app.command("merge-extracted")
def merge_extracted() -> None:
    """Union deterministic + subagent LLM output -> data/extracted/{slug}.json."""
    from . import structural as m

    m.merge()


@app.command()
def resolve() -> None:
    """Entity resolution -> data/extracted/_canonical.json."""
    from . import resolve as m

    m.main()


@app.command()
def load() -> None:
    """Push everything into FalkorDB."""
    from . import load as m

    m.main()


@app.command()
def gaps() -> None:
    """Run gap-finding queries -> reports/gaps-{ts}.md."""
    from . import queries as m

    m.main()


@app.command("run-tail")
def run_tail() -> None:
    """Run merge -> resolve -> load -> gaps after subagents have produced LLM output."""
    from . import structural, resolve, load, queries

    structural.merge()
    resolve.main()
    load.main()
    queries.main()


if __name__ == "__main__":
    app()

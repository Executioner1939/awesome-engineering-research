"""Adapt firecrawl output -> data/raw/{slug}.json records.

Firecrawl writes two different layouts depending on the subcommand:

  - `firecrawl experimental download` nests files:
        .firecrawl/<host>/<path>/index.md
  - `firecrawl scrape <url1> <url2> ...` flattens with dashes:
        .firecrawl/<host>-<path-with-dashes>.md

We handle both. URL reconstruction prefers the nested-path layout
(unambiguous). For flat files we use the sitemap (if available) as the
truth source for path-segment boundaries, since dashes can be either
literal characters or path separators.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

from rich.console import Console

console = Console()
FIRECRAWL_ROOT = Path(".firecrawl")
DATA_RAW = Path("data/raw")
SITEMAP_PATH = Path("/tmp/moonmap.json")


def slugify_url(url: str) -> str:
    from urllib.parse import urlparse

    p = urlparse(url)
    path = p.path.strip("/") or "index"
    return re.sub(r"[^a-zA-Z0-9._-]+", "_", f"{p.netloc}_{path}")


def _title_from_markdown(md: str) -> str | None:
    m = re.search(r"^#\s+(.+?)\s*$", md, flags=re.MULTILINE)
    return m.group(1).strip() if m else None


def _flat_filename_for(url: str) -> str:
    """firecrawl scrape flattens URLs by replacing : / with -."""
    from urllib.parse import urlparse

    p = urlparse(url)
    path = p.path.strip("/")
    parts = [p.netloc] + (path.split("/") if path else [])
    return "-".join(parts) + ".md"


def _load_sitemap_urls() -> list[str]:
    if not SITEMAP_PATH.exists():
        return []
    d = json.loads(SITEMAP_PATH.read_text())
    urls = d.get("links") or d.get("urls") or d.get("data", {}).get("links", []) or []
    norm: list[str] = []
    for u in urls:
        if isinstance(u, dict):
            norm.append(u.get("url") or u.get("href") or "")
        else:
            norm.append(u)
    return [u for u in norm if u]


def _url_for_path(md_path: Path, flat_lookup: dict[str, str]) -> str | None:
    rel = md_path.relative_to(FIRECRAWL_ROOT)
    parts = rel.parts

    if len(parts) >= 2:
        # Nested layout: .firecrawl/<host>/<...>/index.md
        host = parts[0]
        path_parts = list(parts[1:])
        if path_parts[-1] in ("index.md", "index.html"):
            path_parts = path_parts[:-1]
        elif path_parts[-1].endswith(".md"):
            path_parts[-1] = path_parts[-1].removesuffix(".md")
        url = f"https://{host}/" + "/".join(path_parts)
        return url.rstrip("/")

    # Flat layout: .firecrawl/<host>-<...>.md
    return flat_lookup.get(md_path.name)


def main() -> None:
    DATA_RAW.mkdir(parents=True, exist_ok=True)
    if not FIRECRAWL_ROOT.exists():
        console.print(f"[red]{FIRECRAWL_ROOT} not found — run `firecrawl experimental download` first[/]")
        return

    # Build a flat-filename -> canonical-url lookup from the sitemap.
    sitemap_urls = _load_sitemap_urls()
    flat_lookup = {_flat_filename_for(u): u for u in sitemap_urls}

    md_files = sorted(set(FIRECRAWL_ROOT.rglob("*.md")))
    converted: list[str] = []

    for md_path in md_files:
        url = _url_for_path(md_path, flat_lookup)
        if url is None:
            console.print(f"[yellow]skipping {md_path} (no URL match)[/]")
            continue

        markdown = md_path.read_text(encoding="utf-8")
        record = {
            "url": url,
            "title": _title_from_markdown(markdown),
            "markdown": markdown,
            "html": "",
            "links": [],
            "scraped_at": datetime.fromtimestamp(md_path.stat().st_mtime, tz=timezone.utc).isoformat(),
            "source_path": str(md_path),
        }

        slug = slugify_url(url)
        out = DATA_RAW / f"{slug}.json"
        out.write_text(json.dumps(record, ensure_ascii=False, indent=2))
        converted.append(url)

    manifest = {
        "ingested_at": datetime.now(timezone.utc).isoformat(),
        "url_count": len(converted),
        "urls": sorted(converted),
    }
    (DATA_RAW / "_manifest.json").write_text(json.dumps(manifest, indent=2))
    console.print(f"[green]ingested {len(converted)} pages -> data/raw/[/]")


if __name__ == "__main__":
    main()

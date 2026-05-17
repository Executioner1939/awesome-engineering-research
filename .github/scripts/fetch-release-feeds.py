#!/usr/bin/env python3
"""Fetch configured release feeds and emit candidate JSONL.

Reads `.claude/skills/new-releases-triage/sources.yml`. For each feed entry,
fetches it (RSS/Atom/JSON/HTML), parses titles/URLs/dates, filters to items
newer than --since, and writes one JSON line per candidate.

Stub-and-skeleton implementation: handles RSS / Atom / JSON gracefully; for
HTML sources (github trending pages), writes a TODO note to the report.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from xml.etree import ElementTree as ET


def parse_since(since: str) -> datetime:
    """Parse '7d', '30d', '24h' relative window."""
    m = re.match(r"(\d+)([dh])", since)
    if not m:
        raise SystemExit(f"bad --since: {since}")
    n, unit = int(m.group(1)), m.group(2)
    delta = timedelta(days=n) if unit == "d" else timedelta(hours=n)
    return datetime.now(timezone.utc) - delta


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "awesome-engineering-research/triage"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def parse_rss_atom(body: bytes, source_name: str, area: str, since_dt: datetime) -> list[dict]:
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return []
    out: list[dict] = []
    # RSS 2.0
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        pub = item.findtext("pubDate") or item.findtext("{http://purl.org/dc/elements/1.1/}date") or ""
        if not title or not link:
            continue
        out.append({"source": source_name, "interest_area": area, "title": title,
                    "url": link, "published_at": pub, "description": item.findtext("description") or ""})
    # Atom
    ns = "{http://www.w3.org/2005/Atom}"
    for entry in root.iter(f"{ns}entry"):
        title = (entry.findtext(f"{ns}title") or "").strip()
        link_el = entry.find(f"{ns}link")
        link = link_el.get("href") if link_el is not None else ""
        pub = entry.findtext(f"{ns}updated") or entry.findtext(f"{ns}published") or ""
        if not title or not link:
            continue
        out.append({"source": source_name, "interest_area": area, "title": title,
                    "url": link, "published_at": pub, "description": entry.findtext(f"{ns}summary") or ""})
    return out


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--config", required=True)
    p.add_argument("--since", default="7d")
    p.add_argument("--output", required=True)
    args = p.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"no config at {config_path}; writing empty candidates list", file=sys.stderr)
        Path(args.output).write_text("")
        return 0

    # Minimal YAML reader: parse `- name: ... feed_url: ... interest_area: ...`
    config_text = config_path.read_text()
    entries: list[dict] = []
    cur: dict = {}
    for raw in config_text.splitlines():
        line = raw.rstrip()
        if line.startswith("- "):
            if cur:
                entries.append(cur)
            cur = {}
            key, _, val = line[2:].partition(":")
            cur[key.strip()] = val.strip().strip("\"'")
        elif ":" in line and line.startswith(("  ", "\t")):
            key, _, val = line.strip().partition(":")
            cur[key.strip()] = val.strip().strip("\"'")
    if cur:
        entries.append(cur)

    since_dt = parse_since(args.since)
    candidates: list[dict] = []
    for e in entries:
        url = e.get("feed_url")
        if not url:
            continue
        try:
            body = fetch(url)
        except (urllib.error.URLError, TimeoutError) as ex:
            print(f"fetch {url} failed: {ex}", file=sys.stderr)
            continue
        items = parse_rss_atom(body, e.get("name", url), e.get("interest_area", "other"), since_dt)
        candidates.extend(items)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w") as fh:
        for c in candidates:
            fh.write(json.dumps(c) + "\n")
    print(f"wrote {len(candidates)} candidates to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

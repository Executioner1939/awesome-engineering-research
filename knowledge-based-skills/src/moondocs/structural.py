"""Deterministic structural extraction + merge with subagent LLM output.

This module does NOT call any LLM API. The LLM pass happens in this
Claude Code session via the Agent tool; each subagent writes its
results into `data/extracted/_llm/{slug}.json` matching the
ExtractionResult schema.

Order:
  1. `python -m moondocs extract-structural` writes the deterministic
     pass to `data/extracted/{slug}.det.json` for every parsed page.
  2. Claude (this session) dispatches Sonnet subagents in parallel to
     produce `data/extracted/_llm/{slug}.json`.
  3. `python -m moondocs merge-extracted` unions deterministic + LLM
     into `data/extracted/{slug}.json` (the canonical extraction output
     resolve.py and load.py consume).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import tomllib
import yaml
from pydantic import ValidationError
from rich.console import Console

from .parse import is_internal_moon_link
from .schema import Entity, EntityType, ExtractionResult, RelType, Relationship

console = Console()
DATA_PARSED = Path("data/parsed")
DATA_EXTRACTED = Path("data/extracted")
DATA_LLM = DATA_EXTRACTED / "_llm"

CONFIG_FILE_HINTS = {
    "workspace": EntityType.WORKSPACE,
    "project": EntityType.PROJECT,
    "task": EntityType.TASK,
    "tasks": EntityType.TASK,
    "toolchain": EntityType.TOOLCHAIN,
    "template": EntityType.CONFIG_FILE,
}


def _infer_parent_type(heading_path: list[str]) -> EntityType | None:
    joined = " ".join(heading_path).lower()
    for keyword, etype in CONFIG_FILE_HINTS.items():
        if keyword in joined:
            return etype
    return None


def _parse_config_block(lang: str, content: str) -> dict | None:
    try:
        if lang in {"yaml", "yml"}:
            data = yaml.safe_load(content)
        elif lang == "toml":
            data = tomllib.loads(content)
        elif lang == "json":
            data = json.loads(content)
        else:
            return None
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def deterministic(parsed: dict) -> tuple[list[Entity], list[Relationship]]:
    entities: list[Entity] = []
    relationships: list[Relationship] = []
    url = parsed["url"]

    for block in parsed["code_blocks"]:
        data = _parse_config_block(block["lang"], block["content"])
        if data is None:
            continue
        parent_type = _infer_parent_type(block["heading_path"])
        if parent_type is None:
            continue
        parent_id = parent_type.value.lower()
        for key in data.keys():
            if not isinstance(key, str):
                continue
            field_id = f"{parent_id}.{key}"
            entities.append(
                Entity(
                    id=field_id,
                    type=EntityType.CONFIG_FIELD,
                    parent=parent_id,
                    description=f"Field of {parent_type.value} (code-block evidence)",
                    source_chunk=f"```{block['lang']}\n{block['content'][:200]}\n```",
                    source="deterministic",
                )
            )
            relationships.append(
                Relationship(
                    src=field_id,
                    dst=parent_id,
                    type=RelType.BELONGS_TO,
                    evidence=f"top-level key `{key}` in `{block['lang']}` block under {' > '.join(block['heading_path']) or '(top)'}",
                    confidence=1.0,
                    source="deterministic",
                )
            )

    for link in parsed["links"]:
        if not is_internal_moon_link(link["href"]):
            continue
        target = re.sub(r"[#?].*$", "", link["href"]).rstrip("/").split("/")[-1]
        if not target:
            continue
        text = link["text"].strip()
        if not text:
            continue
        relationships.append(
            Relationship(
                src=url,
                dst=target,
                type=RelType.REFERENCES,
                evidence=f"link text `{text}` -> `{link['href']}` under {' > '.join(link['heading_path']) or '(top)'}",
                confidence=0.8,
                source="deterministic",
            )
        )

    return entities, relationships


def main() -> None:
    """Run the deterministic pass over every parsed page."""
    DATA_EXTRACTED.mkdir(parents=True, exist_ok=True)
    parsed_files = sorted(p for p in DATA_PARSED.glob("*.json") if not p.name.startswith("_"))
    console.print(f"[cyan]deterministic extraction over {len(parsed_files)} pages[/]")

    for p in parsed_files:
        parsed = json.loads(p.read_text())
        entities, relationships = deterministic(parsed)
        out = DATA_EXTRACTED / f"{p.stem}.det.json"
        out.write_text(
            json.dumps(
                {
                    "url": parsed["url"],
                    "entities": [e.model_dump() for e in entities],
                    "relationships": [r.model_dump() for r in relationships],
                },
                ensure_ascii=False,
                indent=2,
            )
        )

    n_ents = sum(len(json.loads(p.read_text())["entities"]) for p in DATA_EXTRACTED.glob("*.det.json"))
    n_rels = sum(len(json.loads(p.read_text())["relationships"]) for p in DATA_EXTRACTED.glob("*.det.json"))
    console.print(f"[green]deterministic: {n_ents} entities, {n_rels} relationships[/]")


def merge() -> None:
    """Union deterministic + subagent LLM outputs into data/extracted/{slug}.json."""
    DATA_EXTRACTED.mkdir(parents=True, exist_ok=True)
    det_files = sorted(DATA_EXTRACTED.glob("*.det.json"))
    console.print(f"[cyan]merging {len(det_files)} deterministic + LLM extractions[/]")

    merged_n_ents = 0
    merged_n_rels = 0

    for det_path in det_files:
        det = json.loads(det_path.read_text())
        slug = det_path.stem.removesuffix(".det")
        url = det["url"]

        entities = {e["id"]: e for e in det["entities"]}
        relationships: list[dict] = list(det["relationships"])

        llm_path = DATA_LLM / f"{slug}.json"
        if llm_path.exists():
            try:
                llm_data = json.loads(llm_path.read_text())
                llm = ExtractionResult.model_validate({**llm_data, "url": url})
                for e in llm.entities:
                    entities.setdefault(e.id, e.model_dump())
                relationships.extend(r.model_dump() for r in llm.relationships)
            except (ValidationError, json.JSONDecodeError) as exc:
                console.print(f"[yellow]bad LLM output for {slug}: {exc}[/]")

        out = DATA_EXTRACTED / f"{slug}.json"
        payload = {
            "url": url,
            "entities": list(entities.values()),
            "relationships": relationships,
        }
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        merged_n_ents += len(entities)
        merged_n_rels += len(relationships)

    console.print(f"[green]merged: {merged_n_ents} entities, {merged_n_rels} relationships[/]")


if __name__ == "__main__":
    main()

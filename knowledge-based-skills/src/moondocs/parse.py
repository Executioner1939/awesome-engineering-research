"""Markdown -> structured (heading-path, code-block, link) chunks.

Uses markdown-it-py's token stream (not the AST renderer) because we
need to track heading hierarchy as a path and associate code blocks /
links with the surrounding heading. Output is JSON-serialisable so
downstream stages can consume it without re-parsing.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path

from markdown_it import MarkdownIt
from rich.console import Console

console = Console()
DATA_RAW = Path("data/raw")
DATA_PARSED = Path("data/parsed")


@dataclass
class CodeBlock:
    lang: str
    content: str
    heading_path: list[str]


@dataclass
class Link:
    text: str
    href: str
    heading_path: list[str]


@dataclass
class HeadingChunk:
    """A heading and the prose under it, until the next heading of equal-or-higher level."""

    level: int
    heading_path: list[str]
    text: str
    prose: str


@dataclass
class ParsedPage:
    url: str
    title: str | None
    heading_chunks: list[HeadingChunk] = field(default_factory=list)
    code_blocks: list[CodeBlock] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)


def parse_markdown(url: str, title: str | None, markdown: str) -> ParsedPage:
    md = MarkdownIt("commonmark", {"html": True})
    tokens = md.parse(markdown)

    page = ParsedPage(url=url, title=title)
    heading_stack: list[tuple[int, str]] = []  # (level, text)
    current_chunk_buffer: list[str] = []
    current_chunk_meta: tuple[int, list[str], str] | None = None  # (level, path, heading_text)

    def flush_chunk() -> None:
        nonlocal current_chunk_buffer, current_chunk_meta
        if current_chunk_meta is not None:
            level, path, text = current_chunk_meta
            page.heading_chunks.append(
                HeadingChunk(
                    level=level,
                    heading_path=list(path),
                    text=text,
                    prose="".join(current_chunk_buffer).strip(),
                )
            )
        current_chunk_buffer = []
        current_chunk_meta = None

    i = 0
    while i < len(tokens):
        tok = tokens[i]

        if tok.type == "heading_open":
            flush_chunk()
            level = int(tok.tag[1])  # h2 -> 2
            inline = tokens[i + 1]
            heading_text = inline.content.strip() if inline.type == "inline" else ""
            while heading_stack and heading_stack[-1][0] >= level:
                heading_stack.pop()
            heading_stack.append((level, heading_text))
            current_chunk_meta = (level, [h[1] for h in heading_stack], heading_text)
            i += 3  # heading_open, inline, heading_close
            continue

        if tok.type == "fence":
            page.code_blocks.append(
                CodeBlock(
                    lang=(tok.info or "").strip().split()[0] if tok.info else "",
                    content=tok.content,
                    heading_path=[h[1] for h in heading_stack],
                )
            )
            current_chunk_buffer.append(f"\n```{tok.info}\n{tok.content}\n```\n")
            i += 1
            continue

        if tok.type == "inline":
            current_chunk_buffer.append(tok.content + "\n")
            # walk children for links
            for child in tok.children or []:
                if child.type == "link_open":
                    href = next(
                        (a[1] for a in (child.attrs.items() if hasattr(child.attrs, "items") else child.attrs) if a[0] == "href"),
                        "",
                    )
                    # Find the link text in the following text token
                    idx = (tok.children or []).index(child)
                    text_parts = []
                    for sub in (tok.children or [])[idx + 1 :]:
                        if sub.type == "link_close":
                            break
                        if sub.type == "text":
                            text_parts.append(sub.content)
                    page.links.append(
                        Link(
                            text="".join(text_parts),
                            href=href,
                            heading_path=[h[1] for h in heading_stack],
                        )
                    )

        i += 1

    flush_chunk()
    return page


def parse_all() -> None:
    DATA_PARSED.mkdir(parents=True, exist_ok=True)
    raw_files = sorted(p for p in DATA_RAW.glob("*.json") if not p.name.startswith("_"))
    console.print(f"[cyan]parsing {len(raw_files)} pages[/]")

    for p in raw_files:
        rec = json.loads(p.read_text())
        page = parse_markdown(rec["url"], rec.get("title"), rec.get("markdown", ""))
        out = DATA_PARSED / p.name
        out.write_text(
            json.dumps(
                {
                    "url": page.url,
                    "title": page.title,
                    "heading_chunks": [asdict(c) for c in page.heading_chunks],
                    "code_blocks": [asdict(c) for c in page.code_blocks],
                    "links": [asdict(l) for l in page.links],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    console.print(f"[green]parsed -> data/parsed/[/]")


def is_internal_moon_link(href: str) -> bool:
    if href.startswith("/docs") or href.startswith("/guides"):
        return True
    return re.match(r"^https?://moonrepo\.dev/(docs|guides)", href) is not None


if __name__ == "__main__":
    parse_all()

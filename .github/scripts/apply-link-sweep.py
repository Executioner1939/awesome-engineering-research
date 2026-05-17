#!/usr/bin/env python3
"""Process a lychee JSON report, move dead rows from INDEX/ tables to _archived/.

Writes:
  - the updated INDEX/<file>.md and _archived/<file>.md
  - /tmp/sweep-summary.json (machine-readable: checked, moved counts)
  - /tmp/sweep-summary.md   (PR body)

Lychee schema reference:
  https://github.com/lycheeverse/lychee/blob/master/lychee-lib/src/types/response.rs
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from datetime import date


TODAY = date.today().isoformat()


def parse_table(text: str) -> tuple[str, list[str], list[dict], str]:
    """Return (prefix_before_marker, header_lines, row_dicts, suffix_after_marker)."""
    m = re.search(r"(.*?<!--\s*BEGIN:\s*rows\s*-->\s*\n)(.*?)(\n<!--\s*END:\s*rows\s*-->.*)$",
                  text, re.DOTALL)
    if not m:
        raise RuntimeError("table markers not found")
    prefix, body, suffix = m.group(1), m.group(2), m.group(3)
    lines = body.strip().splitlines()
    _split = re.compile(r"(?<!\\)\|")
    header_cells = [c.strip() for c in _split.split(lines[0].strip("|").strip())]
    rows = []
    for line in lines[2:]:  # skip separator
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in _split.split(line.strip().strip("|"))]
        if len(cells) != len(header_cells):
            continue
        rows.append(dict(zip(header_cells, cells)))
    return prefix, lines[:2], rows, suffix


def render_rows(header_lines: list[str], rows: list[dict]) -> str:
    if not rows:
        return "\n".join(header_lines)
    column_order = [c.strip() for c in header_lines[0].strip("|").split("|")]
    out = list(header_lines)
    for r in sorted(rows, key=lambda x: x.get("id", "")):
        out.append("| " + " | ".join(r.get(c, "") for c in column_order) + " |")
    return "\n".join(out)


def reason_from_lychee_status(entry: dict) -> str | None:
    """Map a lychee result entry to one of our archive reasons, or None if it's OK."""
    status = entry.get("status", {})
    if isinstance(status, str):
        kind = status
    else:
        kind = status.get("text") or status.get("code") or ""
    kind_lower = str(kind).lower()
    if "ok" in kind_lower or "cached" in kind_lower:
        return None
    if "redirected" in kind_lower:
        return None  # treat redirects as OK (they reached a 2xx)
    if "excluded" in kind_lower:
        return None
    if "404" in kind_lower:
        return "404"
    if "410" in kind_lower:
        return "410"
    if "timeout" in kind_lower:
        return "timeout"
    if "dns" in kind_lower:
        return "dns_failure"
    if "ssl" in kind_lower or "certificate" in kind_lower:
        return "ssl_failure"
    if "connection" in kind_lower or "refused" in kind_lower:
        return "connection_failure"
    code = status.get("code") if isinstance(status, dict) else None
    if isinstance(code, int):
        if 400 <= code < 500 and code not in (401, 403):
            return f"{code}"
        if 500 <= code < 600:
            return None  # transient; leave active
    return None


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--report", required=True)
    p.add_argument("--sources", required=True)
    p.add_argument("--tools", required=True)
    p.add_argument("--archived-sources", required=True)
    p.add_argument("--archived-tools", required=True)
    p.add_argument("--report-md", required=True)
    args = p.parse_args()

    report = json.loads(Path(args.report).read_text())
    # Build url -> reason map for failed URLs.
    url_reasons: dict[str, str] = {}
    fail_count = 0
    total_checked = 0

    # Lychee JSON format: top-level dict with "fail_map" mapping file paths to list of failures.
    fail_map = report.get("fail_map") or {}
    success_map = report.get("success_map") or {}
    for src, items in fail_map.items():
        for item in items:
            url = item.get("url")
            if not url:
                continue
            reason = reason_from_lychee_status(item)
            fail_count += 1
            if reason:
                url_reasons[url] = reason
    for items in success_map.values():
        total_checked += len(items)
    total_checked += fail_count

    moved_total = 0
    for src_path, arch_path in (
        (args.sources, args.archived_sources),
        (args.tools, args.archived_tools),
    ):
        src_text = Path(src_path).read_text()
        prefix, header, rows, suffix = parse_table(src_text)
        arch_text = Path(arch_path).read_text()
        a_prefix, a_header, a_rows, a_suffix = parse_table(arch_text)

        keep = []
        for r in rows:
            url = r.get("url", "")
            if url in url_reasons:
                # Move
                r2 = dict(r)
                r2["status"] = "archived"
                r2["last_seen"] = TODAY
                r2["reason"] = url_reasons[url]
                # Fill missing archived-table columns
                arch_columns = [c.strip() for c in a_header[0].strip("|").split("|")]
                for c in arch_columns:
                    r2.setdefault(c, "")
                a_rows.append(r2)
                moved_total += 1
            else:
                keep.append(r)
        Path(src_path).write_text(prefix + render_rows(header, keep) + suffix)
        Path(arch_path).write_text(a_prefix + render_rows(a_header, a_rows) + a_suffix)

    summary = {"checked": total_checked, "moved": moved_total}
    Path("/tmp/sweep-summary.json").write_text(json.dumps(summary))

    md = [
        f"# Link sweep ({TODAY})",
        "",
        f"- URLs checked: **{total_checked}**",
        f"- Moved to `_archived/`: **{moved_total}**",
        "",
    ]
    if url_reasons:
        by_reason: dict[str, int] = {}
        for r in url_reasons.values():
            by_reason[r] = by_reason.get(r, 0) + 1
        md.append("## Breakdown by reason")
        md.append("")
        for reason, n in sorted(by_reason.items(), key=lambda x: -x[1]):
            md.append(f"- {reason}: {n}")
    Path(args.report_md).parent.mkdir(parents=True, exist_ok=True)
    Path(args.report_md).write_text("\n".join(md))
    Path("/tmp/sweep-summary.md").write_text("\n".join(md))
    print(json.dumps(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Auto-prune TRIAGE.md rows older than N days, moving them to _archived/triage-pruned-<date>.md."""
from __future__ import annotations

import argparse
import re
from datetime import date, timedelta
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--triage", required=True)
    p.add_argument("--max-age-days", type=int, default=60)
    p.add_argument("--pruned-out", required=True)
    args = p.parse_args()

    triage = Path(args.triage)
    if not triage.exists():
        print("no triage file; nothing to prune")
        return 0

    cutoff = (date.today() - timedelta(days=args.max_age_days)).isoformat()
    txt = triage.read_text()
    lines = txt.splitlines()
    keep, pruned = [], []
    for ln in lines:
        m = re.match(r"\|\s*(\d{4}-\d{2}-\d{2})\s*\|", ln)
        if m and m.group(1) < cutoff:
            pruned.append(ln)
        else:
            keep.append(ln)
    if pruned:
        out = Path(args.pruned_out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# Pruned triage rows ({date.today().isoformat()})\n\n" +
                       f"Rows older than {args.max_age_days} days; auto-removed from TRIAGE.md.\n\n" +
                       "\n".join(pruned) + "\n")
    triage.write_text("\n".join(keep) + "\n")
    print(f"pruned {len(pruned)} rows older than {cutoff}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

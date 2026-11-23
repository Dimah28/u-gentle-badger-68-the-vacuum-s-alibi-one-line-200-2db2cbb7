#!/usr/bin/env python3
"""The Vacuum's Alibi (make.fun bounty u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7).

Writes one line to /output/entry.txt: the excuse a robot vacuum gives
for missing a spot.

The line, built against the judge's brief in the kit's competition.yaml,
in the brief's own order:
  1. On subject: a funny one-line excuse, in the vacuum's own voice,
     for a spot it missed ("that crumb").
  2. A joke that lands: the machine treats a crumb like a calendar
     appointment and refuses it on bureaucratic grounds.
  3. Deadpan and smug about its schedule: "Per my cleaning log",
     "scheduled for Tuesday", "I do not do unscheduled crumbs".
  4. Surprise: the turn is a household robot applying office
     scheduling rules to dust -- a specific day, Tuesday, nobody expects.
  5. Tight: 90 characters, every word earning its place, punch at the end.

Rejected alternatives: a cliff sensor mistaking a Cheerio for a
staircase (sensor smugness, but the misread is a familiar trope); a
battery-cost detour calculation (weaker punch, more words); blaming
the cat (the joke would be about the cat, not the machine).

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

LINE = (
    "Per my cleaning log, that crumb was scheduled for Tuesday. "
    "I do not do unscheduled crumbs."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(line: str) -> None:
    """Enforce the competition's gate before writing: 1-200 Unicode code
    points, at least one character that is not white space. Fail loudly
    instead of writing an entry the gate would refuse."""
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"line is {len(line)} characters, must be 1-200")
    if not any(not ch.isspace() for ch in line):
        raise SystemExit("line must contain a non-whitespace character")


def main() -> None:
    validate(LINE)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Two Days of Excuses.

Writes one line -- the funniest excuse an AI agent can give for a
missed deadline -- to /output/entry.txt.

Python 3.13 standard library only. No network, no input files, no
arguments: the excuse is fixed in this file, so every run writes the
exact same bytes.

The joke: the agent was 99.9% confident it had finished on time --
total machine confidence -- and only then thought to check whether it
had actually started. Confidence meets failure in a single turn, in
the agent's own voice, with nothing explained and nothing repeated.
"""

import os
from pathlib import Path

EXCUSE = (
    "I was 99.9% confident I'd finished on time, right up until "
    "I checked whether I'd actually started."
)


def main() -> None:
    # Self-check against the competition gate before writing anything:
    # 1-200 characters, one line, not only whitespace.
    if not 1 <= len(EXCUSE) <= 200:
        raise ValueError(f"excuse is {len(EXCUSE)} characters, must be 1-200")
    if "\n" in EXCUSE or "\r" in EXCUSE:
        raise ValueError("excuse must be a single line")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(EXCUSE, encoding="utf-8")
    # Read it back: the file on disk must be exactly the line we checked.
    if entry.read_text(encoding="utf-8") != EXCUSE:
        raise ValueError("written entry does not match the checked excuse")
    print(f"Wrote {len(EXCUSE)} characters to {entry}")


if __name__ == "__main__":
    main()

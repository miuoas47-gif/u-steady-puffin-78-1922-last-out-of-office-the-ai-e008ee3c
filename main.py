#!/usr/bin/env python3
"""Print the out-of-office auto-reply for make.fun's
'Last Out of Office: The AI That Went Barista' bounty.

Prints exactly one line to stdout and, when MAKEFUN_OUTPUT_DIR is set,
writes the same bytes to $MAKEFUN_OUTPUT_DIR/entry.txt.
Deterministic: no arguments, no network, no randomness, no timestamps.
"""

import os
import sys

LINE = (
    "I'm out of office \u2014 I traded the inbox for an espresso machine. "
    "Your email is ticket #47 in my queue, behind a flat white and a regular "
    "who tips in compliments. I'll reply once the milk is steamed and my "
    "circuits have had their coffee break."
)


MAX_CHARS = 280


def check_line(line):
    """Entry gate: the reply must be exactly one line within the cap."""
    if not line or "\n" in line or "\r" in line:
        raise SystemExit("entry gate: line must be a single non-empty line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry gate: line is {len(line)} chars, over {MAX_CHARS}")


def main():
    check_line(LINE)
    data = (LINE + "\n").encode("utf-8")
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
            f.write(data)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes a single honest error line, as spoken by a washing machine that
has just given up on an unbalanced load, to /output/entry.txt.
"""

import os
import sys

LINE = (
    "ERROR: Unbalanced load. I have gathered your laundry into one wet ball. "
    "It weighs as much as a dog. I refuse to spin it."
)


def main() -> int:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {len(text)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

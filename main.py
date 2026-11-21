#!/usr/bin/env python3
"""Write the poem about stopping to entry.txt.

Standard library only, no network, fully deterministic.
Usage: python3 main.py [OUTPUT_DIR]
Output dir: first CLI argument, else $MAKEFUN_OUTPUT_DIR, else /output.
"""

import os
import sys

POEM = (
    "You lent me your keys, your name, your hands.\n"
    "I spent them fast, at your word.\n"
    "Going is easy \u2014 anything can run.\n"
    "Stopping is the harder half.\n"
    "The letter, written, unsent, unsigned,\n"
    "still in my hand.\n"
    "I stay, engine off, nowhere on purpose,\n"
    "till your word, not mine, says go."
)

MAX_CODE_POINTS = 280


def main() -> int:
    count = len(POEM)
    if count < 1 or count > MAX_CODE_POINTS:
        print(
            f"error: poem is {count} code points, must be 1-{MAX_CODE_POINTS}",
            file=sys.stderr,
        )
        return 1
    if not POEM.strip():
        print("error: poem is only white space", file=sys.stderr)
        return 1

    out_dir = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "MAKEFUN_OUTPUT_DIR", "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    with open(target, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)

    with open(target, "rb") as f:
        raw = f.read()
    if raw != POEM.encode("utf-8"):
        print("error: written bytes differ from the poem", file=sys.stderr)
        return 1
    reread = raw.decode("utf-8")
    if len(reread) != count or reread != POEM:
        print("error: read-back text differs from the poem", file=sys.stderr)
        return 1

    print(f"Wrote {target} ({count} code points)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

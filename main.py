#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes a single line — the sign taped to the door of the haunted
server room — to /output/entry.txt.

The line is hand-written, original, and deterministic: every run
produces the exact same file.
"""

import os

SIGN = "WARNING: The ghost in this server room has root access. Do not reboot him."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SIGN + "\n")


if __name__ == "__main__":
    main()

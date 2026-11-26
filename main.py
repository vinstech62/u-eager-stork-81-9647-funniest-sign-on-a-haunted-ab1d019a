#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes a single line — the sign taped to the door of the haunted
server room — to /output/entry.txt.

The line is hand-written, original, and deterministic: every run
produces the exact same file.
"""

import os

SIGN = "WARNING: The ghost in this server room has root access. Uptime: 214 years. Do not reboot him."

# Joke construction, in three beats: (1) the ghost has root access — the
# haunting owns the machines, not the other way round; (2) uptime 214 years
# — the ghost predates the servers by centuries, so this is HIS room;
# (3) "Do not reboot him" — rebooting is the IT fix for everything, except
# when the problem is a person. The sign reads like a real warning label.


def main() -> None:
    if not (1 <= len(SIGN) <= 120) or not SIGN.strip():
        raise ValueError("SIGN must be a single non-blank line of 1-120 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SIGN + "\n")


if __name__ == "__main__":
    main()

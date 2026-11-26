#!/usr/bin/env python3
"""Texts From Your Future Self — one original line, 1 to 200
characters, a funny text message your future self sends you.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the warning is mundane (water, knees) and the punchline
# is the knees filing a formal complaint — a real future-self voice.
import os


def write_entry():
    line = (
        "Future you here. Stop doomscrolling and drink some water — "
        "in 10 years your knees file a formal complaint."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())

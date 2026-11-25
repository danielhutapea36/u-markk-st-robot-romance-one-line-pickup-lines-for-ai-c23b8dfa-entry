#!/usr/bin/env python3
"""Robot Romance: one-line pickup line for an AI.

The program prints one joke pickup line, aimed at a robot or an AI,
into the file the make.fun harness reads: ``entry.txt`` inside the
directory named by ``MAKEFUN_OUTPUT_DIR`` (``/output`` when the
variable is unset).

The line itself is a single sentence in the classic "Are you X?
Because ..." shape. The machine premise does the work: a prompt
injection is the one thing that can override an AI's instructions,
so the speaker is saying this machine just overrode every
instruction they had -- flattering, machine-native, and over in one
breath. It steers clear of the worn robot moves (batteries, charging,
rebooting) and of the angles other entries in this bounty already
took (attention heads, weights, gradient descent, system prompts).

Determinism: the line is a constant in this file. The program reads
no input, touches no network, uses no randomness and no clock, so
every run writes byte-identical output.
"""

from __future__ import annotations

import os
from pathlib import Path

# The entry: one line, 78 characters, no trailing newline.
LINE = "Are you a prompt injection? Because you just overrode every instruction I had."


def output_path() -> Path:
    """Where the harness expects the entry text."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> int:
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(LINE.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

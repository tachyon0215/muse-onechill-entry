#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "One Line, One Chill". Dread that outlasts
the line: the mother's own voice sings the lullaby from inside the
baby's dark, empty room, note-perfect, while she stands in the
hallway holding the baby and humming nothing — the final clause
removes every safe explanation without gore or a stock image.

Deterministic: a fixed text, no network, no randomness, no clock.
Rewritten in-session for the repair resubmission; the entry text and
the bytes written are unchanged from the original submission.
"""
import os
from pathlib import Path

LINE = 'At 3 a.m. the baby monitor played my own voice singing her lullaby from inside her dark room, note-perfect - while I stood in the hallway, holding her, humming nothing.'
TEXT = LINE + "\n"
MAX_CHARS = 199


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()

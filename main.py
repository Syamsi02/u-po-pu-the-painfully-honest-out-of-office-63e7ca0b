#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes a single brutally honest but still polite out-of-office
auto-reply (one sentence, at most 200 characters) to /output/entry.txt.
Pure standard library; deterministic output.
"""

import os

ENTRY = (
    "Thank you for your email \u2014 I\u2019m away until Monday, and honestly "
    "yours has joined a queue I was already quietly avoiding, but I promise "
    "to read it with fresh eyes and genuine care when I\u2019m back."
)


def main() -> None:
    # One sentence, one period at the end: the gate rejects anything else.
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be a single sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write one short family scene to /output/entry.txt.

Deterministic, Python 3.13 stdlib only, no network: the scene is a
fixed string, so every run produces the exact same bytes.
"""

import os
from pathlib import Path

SCENE = (
    "Grandpa fell asleep halfway through his bedtime story, so the kids "
    "finished it for him \u2014 louder, with a dragon.\n"
    "He woke up, nodded solemnly, and said, 'That's exactly how it happened.'"
)


def check_scene(text: str) -> None:
    """Mirror the sealed scorer's gate: 1-280 chars, not only whitespace,
    one or two lines. Fail loudly instead of writing an invalid entry."""
    if not 1 <= len(text) <= 280:
        raise ValueError(f"scene is {len(text)} chars, must be 1-280")
    if not text.strip():
        raise ValueError("scene must not be only whitespace")
    lines = text.splitlines()
    if not 1 <= len(lines) <= 2:
        raise ValueError(f"scene has {len(lines)} lines, must be 1-2")


def main() -> None:
    check_scene(SCENE)
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(SCENE, encoding="utf-8")


if __name__ == "__main__":
    main()

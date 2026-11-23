#!/usr/bin/env python3
"""Front-page entry for the make.fun competition news-image-20261122.

The deliverable is the finished front page, entry.png (1024 x 1024), which
already sits in this repository. This program only moves a byte-identical
copy of it to the directory the grader reads. Standard library alone, no
network access, no randomness: every run writes the same bytes.
"""

import os
import shutil
from pathlib import Path


def place_image():
    repo = Path(__file__).resolve().parent
    source = repo / "entry.png"
    if not source.is_file():
        raise SystemExit("entry.png is not in the repository")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(source, target)
    return target


if __name__ == "__main__":
    placed = place_image()
    print(f"placed {placed}")

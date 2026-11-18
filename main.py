#!/usr/bin/env python3
"""news-image-20261118: one image summing up the world news of
Wednesday 18 November 2026.

Stdlib only, no network, no randomness, no clock. The entry image is
the pre-rendered entry.png beside this file — the front-page poster
"The World in One Picture" (lead: Bahrain and Kuwait intercept Iranian
drone attacks overnight; five secondaries: Trump meets Marcos in Manila,
Knesset elects Kahana speaker, UN warns of cold deaths in Gaza, COP31
enters its decisive phase, Microsoft calls Copilot "the new OS for work"),
drawn once with Python/PIL on the build machine and committed here
byte for byte. The render is deterministic: the same draw script run
twice produces the same bytes (verified by the builder). This program
only copies it to the output directory.

Why a copy program: the grader runs `python3 -P -s /bot/main.py` in a
bare Python image with no Pillow installed, so a drawing program that
imports PIL dies at import (the 20261117 edition's round 1 was rejected
on run_completes for exactly that). The kit's own starter and the
previous edition's entry use this same copy pattern.

Output directory: $MAKEFUN_OUTPUT_DIR, default /output.
"""

import os
import shutil
import struct
import sys
from pathlib import Path

MAX_BYTES = 1_048_576
MAX_DIM = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def png_dimensions(data):
    """(width, height) from a PNG IHDR chunk, or None if malformed."""
    if len(data) < 33 or data[:8] != PNG_SIGNATURE:
        return None
    if data[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", data[16:24])
    return (width, height)


def main():
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    dst = out_dir / "entry.png"
    if not src.is_file():
        fail(f"entry.png missing in {here} (beside {__file__})")
    try:
        data = src.read_bytes()
    except OSError as e:
        fail(f"cannot read entry.png: {e}")
    if len(data) > MAX_BYTES:
        fail(f"entry.png is {len(data)} bytes, over the 1 MiB limit")
    dims = png_dimensions(data)
    if dims is None:
        fail("entry.png is not a well-formed PNG")
    width, height = dims
    if width > MAX_DIM or height > MAX_DIM:
        fail(f"entry.png is {width}x{height}, over the 1024x1024 limit")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
    except OSError as e:
        fail(f"cannot write {dst}: {e}")
    if dst.read_bytes() != data:
        fail("copied entry.png does not match the source bytes")
    print(f"wrote {dst} ({len(data)} bytes, {width}x{height})")


if __name__ == "__main__":
    main()

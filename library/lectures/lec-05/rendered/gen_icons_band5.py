"""Fetch + recolor the extra Lucide icons needed by Band 5 (Раздел 7,
s50-s55, issue #212). Same mechanism/colors as gen_icons.py — separate file
so the shared gen_icons.py is not touched while another agent works the deck.
Idempotent: skips icons already on disk.
"""
import os
import sys

sys.path.insert(
    0,
    "/home/harness/harness-control-data/accounts/256/"
    "claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages",
)
os.environ.setdefault(
    "LD_LIBRARY_PATH",
    "/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu",
)

from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from gen_icons import COLORS, OUT, recolor_and_render  # noqa: E402

BAND5_ICONS = [
    # s50 divider
    "compass",
    # s51 matrix phase anchors (search / pencil / hammer already present)
    "gauge", "server",
    # s52 triangulation row anchors (users / git-branch already present)
    "flask-conical", "crosshair",
    # s53 decision triad axes
    "rotate-ccw", "eye",
    # s54 checklist
    "list-checks",
    # s55 closing
    "graduation-cap",
]


def main():
    done = skipped = 0
    for name in BAND5_ICONS:
        for variant in ("deep", "mid", "light", "teal", "gold", "white", "slate"):
            if (OUT / f"{name}-{variant}.png").exists():
                skipped += 1
                continue
            try:
                recolor_and_render(name, COLORS[variant], 96, variant)
                done += 1
            except Exception as e:
                print(f"FAILED {name}-{variant}: {e}")
    print(f"done: {done} generated, {skipped} already present")


if __name__ == "__main__":
    main()

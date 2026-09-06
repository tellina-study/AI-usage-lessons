"""Fetch + recolor Lucide SVG icons for lec-05 deck (band 1: s01-s13a first,
extended as later bands are wired). Requires network (unpkg.com CDN) +
cairosvg (needs LD_LIBRARY_PATH pointed at lo-sysroot's libcairo, see
render env in render.sh). Idempotent — skips icons already on disk.
"""
import os
import sys
import time
import urllib.request

sys.path.insert(
    0,
    "/home/harness/harness-control-data/accounts/256/"
    "claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages",
)
os.environ.setdefault(
    "LD_LIBRARY_PATH",
    "/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu",
)

from pathlib import Path
import cairosvg

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets/icons/src"
OUT = HERE / "assets/icons"
SRC.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

CDN = "https://unpkg.com/lucide-static@latest/icons/{name}.svg"

COLORS = {
    "deep": "21295C",
    "mid": "065A82",
    "light": "1C7293",
    "teal": "028090",
    "gold": "F0AB00",
    "white": "FFFFFF",
    "slate": "5B6678",
}

# icon names needed across the deck (extend as bands 2-4 are wired).
ICON_NAMES = [
    # s01 hook
    "clock", "funnel",
    # s02 cover
    "lightbulb", "cog",
    # s03 lecture-map
    "search", "pencil", "hammer", "ruler", "headphones", "scale",
    # s04 bridge
    "layers", "arrow-right",
    # s05/s06 keystone
    "bar-chart-3", "plane", "rocket", "repeat", "lock", "unlock",
    # s07 divider discovery
    "search-x", "file-text",
    # s08 customer development
    "route", "git-branch", "diamond",
    # s09 mom test
    "message-square-x", "history", "handshake",
    # s10 ai discovery tools
    "file-search", "layout-list", "database", "circle-check",
    # s11 ai limits discovery
    "smile", "shield-alert", "history",
    # s12 synthetic users failure
    "check-check", "x", "monitor-smartphone",
    # s13 fabricated research
    "file-x", "banknote",
    # s13a ibm watson
    "scale", "users", "user-x",
    # generic
    "triangle-alert", "circle-help", "sliders-horizontal", "shield-check",
]


def fetch_svg(name):
    path = SRC / f"{name}.svg"
    if path.exists():
        return path.read_text()
    url = CDN.format(name=name)
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
            with urllib.request.urlopen(req, timeout=15) as r:
                txt = r.read().decode("utf-8")
            path.write_text(txt)
            return txt
        except Exception as e:
            print(f"  retry {name}: {e}")
            time.sleep(1)
    raise RuntimeError(f"failed to fetch icon {name}")


def recolor_and_render(name, hexcolor, size_px, variant):
    svg = fetch_svg(name)
    svg = svg.replace('stroke="currentColor"', f'stroke="#{hexcolor}"')
    out_path = OUT / f"{name}-{variant}.png"
    cairosvg.svg2png(
        bytestring=svg.encode("utf-8"),
        write_to=str(out_path),
        output_width=size_px,
        output_height=size_px,
    )
    return out_path


def main():
    variants = [
        ("deep", "deep", 96),
        ("mid", "mid", 96),
        ("light", "light", 96),
        ("teal", "teal", 96),
        ("gold", "gold", 96),
        ("white", "white", 96),
        ("slate", "slate", 96),
    ]
    n_done = 0
    n_skip = 0
    for name in ICON_NAMES:
        for variant, colorkey, size_px in variants:
            out_path = OUT / f"{name}-{variant}.png"
            if out_path.exists():
                n_skip += 1
                continue
            try:
                recolor_and_render(name, COLORS[colorkey], size_px, variant)
                n_done += 1
            except Exception as e:
                print(f"FAILED {name}-{variant}: {e}")
    print(f"done: {n_done} generated, {n_skip} already present")


if __name__ == "__main__":
    main()

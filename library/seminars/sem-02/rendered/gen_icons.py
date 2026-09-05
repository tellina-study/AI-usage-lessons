"""Recolor+rasterize Lucide SVG icons for sem-02 deck. Run once before build_sem02.py.

Requires LD_LIBRARY_PATH set for cairosvg (see run instructions).
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, "/home/harness/harness-control-data/accounts/256/claude-code-klabulan-8da64c79/.local/lib/python3.12/site-packages")
os.environ.setdefault("LD_LIBRARY_PATH", "/home/harness/.local/lo-sysroot/usr/lib/x86_64-linux-gnu")

import cairosvg

HERE = Path(__file__).resolve().parent
SRC = HERE / "assets/icons/src"
OUT = HERE / "assets/icons/rendered"
OUT.mkdir(parents=True, exist_ok=True)

# (icon_name, hex_no_hash, size_px)
REQUESTS = [
    # Ocean palette icon needs across the deck
    ("server", "065A82", 96), ("server", "FFFFFF", 64), ("server", "1C7293", 72),
    ("search", "065A82", 96), ("search", "FFFFFF", 64), ("search", "1C7293", 72),
    ("network", "065A82", 96), ("network", "028090", 72),
    ("cog", "065A82", 96), ("cog", "FFFFFF", 64),
    ("repeat", "065A82", 96), ("repeat", "F0AB00", 64), ("repeat", "FFFFFF", 48),
    ("check-check", "FFFFFF", 64),
    ("circle-check", "F0AB00", 64), ("circle-check", "028090", 64),
    ("arrow-right", "F0AB00", 64), ("arrow-right", "1C7293", 48), ("arrow-right", "FFFFFF", 48),
    ("git-fork", "065A82", 96),
    ("workflow", "065A82", 96), ("workflow", "FFFFFF", 64),
    ("list-checks", "065A82", 96), ("list-checks", "028090", 64),
    ("route", "065A82", 96),
    ("funnel", "FFFFFF", 96), ("funnel", "065A82", 96), ("funnel", "F0AB00", 64),
    ("filter", "028090", 64), ("filter", "065A82", 96),
    ("monitor", "065A82", 96), ("monitor", "FFFFFF", 64),
    ("cloud", "065A82", 96), ("cloud", "FFFFFF", 64), ("cloud", "1C7293", 72),
    ("cloud-cog", "065A82", 96), ("cloud-cog", "21295C", 64),
    ("gauge", "028090", 64), ("gauge", "065A82", 96),
    ("folder-search", "028090", 64), ("folder-search", "065A82", 96),
    ("wrench", "FFFFFF", 64), ("wrench", "065A82", 96),
    ("key-round", "21295C", 64), ("key-round", "065A82", 96),
    ("bug", "21295C", 64), ("bug", "028090", 64),
    ("shield-alert", "21295C", 64), ("shield-alert", "065A82", 96),
    ("phone", "065A82", 96), ("phone", "028090", 64), ("phone", "FFFFFF", 64),
    ("building-2", "1C7293", 72), ("building-2", "065A82", 96),
    ("store", "065A82", 96), ("store", "028090", 64),
    ("zap", "F0AB00", 64), ("zap", "065A82", 96),
    ("package", "065A82", 96), ("package", "028090", 64),
    ("building", "1C7293", 72), ("building", "065A82", 96),
    ("banknote", "21295C", 64), ("banknote", "028090", 64),
    ("cable", "065A82", 96),
    ("ban", "21295C", 64), ("ban", "6B7685", 64),
    ("split", "065A82", 96), ("split", "028090", 64),
    # reuse existing but new colors/sizes if needed
    ("layers", "065A82", 96), ("layers", "FFFFFF", 64),
    ("database", "065A82", 96), ("database", "FFFFFF", 64), ("database", "028090", 64),
    ("cpu", "21295C", 64), ("cpu", "FFFFFF", 64),
    ("scale", "F0AB00", 64),
    ("search-x", "21295C", 64), ("search-x", "065A82", 96),
    ("shield-check", "065A82", 96), ("shield-check", "21295C", 64),
    ("file-code", "1C7293", 72), ("file-code", "FFFFFF", 64),
    ("file-text", "065A82", 96), ("file-text", "1C7293", 72), ("file-text", "FFFFFF", 64),
    ("users", "065A82", 96), ("users", "FFFFFF", 64),
    ("user-round", "FFFFFF", 64), ("user-round", "065A82", 96),
    ("briefcase", "065A82", 96), ("briefcase", "FFFFFF", 64),
    ("target", "065A82", 96), ("target", "028090", 64),
    ("x-circle", "21295C", 64), ("x-circle", "028090", 64),
    ("rotate-ccw", "028090", 64),
    ("alert-triangle", "21295C", 64), ("alert-triangle", "F0AB00", 64), ("alert-triangle", "065A82", 96),
    ("lock", "21295C", 64), ("lock", "065A82", 96), ("lock", "FFFFFF", 64),
    ("mail", "065A82", 96),
    ("hash", "065A82", 96), ("hash", "028090", 64),
    ("trophy", "F0AB00", 64), ("trophy", "065A82", 96),
    ("thumbs-down", "21295C", 64),
    ("thumbs-up", "065A82", 96), ("thumbs-up", "F0AB00", 64),
    ("sparkles", "F0AB00", 64), ("sparkles", "065A82", 96), ("sparkles", "1C7293", 72),
    ("smile", "028090", 64),
    ("book-open", "065A82", 96), ("book-open", "FFFFFF", 64), ("book-open", "028090", 64),
    ("clock", "065A82", 96), ("clock", "028090", 72),
    ("compass", "065A82", 96),
    ("flag", "21295C", 64), ("flag", "F0AB00", 64), ("flag", "065A82", 96),
    ("code-2", "065A82", 96), ("code-2", "1C7293", 72), ("code-2", "FFFFFF", 72),
    ("code", "065A82", 96), ("code", "028090", 64),
    ("factory", "1C7293", 72), ("factory", "FFFFFF", 72),
    ("truck", "1C7293", 72), ("truck", "FFFFFF", 72),
    ("landmark", "1C7293", 72), ("landmark", "FFFFFF", 72),
    ("stethoscope", "1C7293", 72), ("stethoscope", "FFFFFF", 72),
    ("scale", "028090", 72), ("scale", "065A82", 96),
    ("map", "065A82", 96),
    ("calendar", "065A82", 96), ("calendar", "028090", 64),
    ("message-square-quote", "028090", 72), ("message-square-quote", "065A82", 96),
    ("message-circle-question", "065A82", 96), ("message-circle-question", "028090", 64),
    ("handshake", "065A82", 96),
    ("check-circle-2", "21295C", 64), ("check-circle-2", "FFFFFF", 64), ("check-circle-2", "F0AB00", 64),
    ("bar-chart-2", "065A82", 96),
    ("hand", "F0AB00", 96), ("hand", "065A82", 96),
    ("toggle-left", "6B7685", 64),
    ("circle-check", "065A82", 96),
    ("quote", "1C7293", 64),
    ("hash", "028090", 96),
    ("zap", "F0AB00", 96),
    ("banknote", "065A82", 96),
    ("sparkles", "21295C", 64),
    # issue #182 -- 41-slide rebuild additions (s02 case list @64px, quote
    # role-icons, s24/s30/s31 icon-scene additions)
    ("file-text", "065A82", 64),
    ("shield-alert", "065A82", 64),
    ("monitor", "065A82", 64),
    ("store", "065A82", 64),
    ("list-checks", "065A82", 64),
    ("mail", "065A82", 64),
    ("phone", "065A82", 64),
    ("user-round", "F0AB00", 64),
    ("briefcase", "028090", 64),
    ("check-circle-2", "028090", 96),
    ("workflow", "21295C", 64),
    ("mail", "028090", 96),
    ("scale", "028090", 64),
    ("shield-alert", "21295C", 96),
    ("user-round", "028090", 64),
    ("message-square-quote", "1C7293", 72),
    ("cable", "065A82", 96),
    ("folder-search", "065A82", 96),
]


def recolor_and_render(name, hexcolor, size):
    src = SRC / f"{name}.svg"
    if not src.exists():
        print(f"MISSING SRC: {name}.svg")
        return
    out = OUT / f"{name}-{hexcolor}-{size}.png"
    if out.exists():
        return
    svg_text = src.read_text(encoding="utf-8")
    svg_text = svg_text.replace("currentColor", f"#{hexcolor}")
    tmp = OUT / f"_tmp_{name}_{hexcolor}.svg"
    tmp.write_text(svg_text, encoding="utf-8")
    cairosvg.svg2png(url=str(tmp), write_to=str(out), output_width=size, output_height=size)
    tmp.unlink()
    print(f"OK {out.name}")


if __name__ == "__main__":
    for name, hexc, size in REQUESTS:
        recolor_and_render(name, hexc, size)
    print("Done.")

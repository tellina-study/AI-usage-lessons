"""Block-3 EN visual-QA build (#172): ONLY the 12 slides this block owns.

Deck ids (= builder function names), in v4.5 display order:
    b2.s18b, b2.s19, b2.s20b, b2.s20c, b2.s20e, b2.s20d, b2.s20g, b2.s20f,
    b2.s20, b3.s22, b3.s23, b3.s24
which occupy display positions 25..36 of the 58-slide deck.

This exists so the block can run its Generate→Convert→Inspect→Fix loop without
touching build_lec04_en.py, whose builder list is shared with four other EN
blocks running in parallel worktrees. The full-deck assembler is rebased onto
the 58-slide order once all five blocks have merged — see iteration-log-en.md
§ "EN-Sync Block 3" for the exact ordering fragment this block contributes.

Build: python3 build_lec04_en_blk3.py  → lec-04-en-blk3.pptx (12 slides).
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers_en import setup_pres, ROOT, page_number  # noqa: E402
import slides_band2_en as b2  # noqa: E402
import slides_band3_en as b3  # noqa: E402

OUT = ROOT / "rendered/lec-04-en-blk3.pptx"

# (builder, real display position in the 58-slide deck)
BUILDERS = [
    (b2.s18b, 25),
    (b2.s19, 26),
    (b2.s20b, 27),
    (b2.s20c, 28),
    (b2.s20e, 29),
    (b2.s20d, 30),
    (b2.s20g, 31),
    (b2.s20f, 32),
    (b2.s20, 33),
    (b3.s22, 34),
    (b3.s23, 35),
    (b3.s24, 36),
]


def main():
    p = setup_pres()
    for fn, _pos in BUILDERS:
        fn(p)
    for slide, (_fn, pos) in zip(p.slides, BUILDERS):
        page_number(slide, pos, 58)
    n = len(p.slides.__iter__.__self__._sldIdLst)
    assert n == 12, f"expected 12 slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} ({n} slides)")


if __name__ == "__main__":
    main()

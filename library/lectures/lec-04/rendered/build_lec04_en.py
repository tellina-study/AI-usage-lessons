"""EN twin of build_lec04_v4.py — full English build of Lecture 4
"AI across the software development lifecycle (SDLC)".

Slide count tracks the RU deck (58 after round 6); the EN-parity rebuild is
landing block by block across five parallel worktrees (issue #172 / #162).

Issue #172 (Ф3): English re-render. Structure, layout, palette, motif, and
slide count are identical to the RU deck; only the rendered visible strings
and speaker notes are translated (per glossary-ru-en.md). Charts come from
assets/charts-en (EN-labeled twins), notes from slides-en/*.md.

Source-of-truth: deck.en.yaml + slides-en/*.md (visible content + readable
EN speaker notes). Builders live in slides_band{1..4}_en.py, importing from
_helpers_en.py (SLIDES_DIR=slides-en, CHARTS=charts-en, EN NAV/dividers/refs).

Build: python3 build_lec04_en.py  → lec-04-en.pptx.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers_en import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1_en as b1  # noqa: E402
import slides_band2_en as b2  # noqa: E402
import slides_band3_en as b3  # noqa: E402
import slides_band4_en as b4  # noqa: E402

OUT = ROOT / "rendered/lec-04-en.pptx"


def main():
    p = setup_pres()
    builders = []
    # display s01–s10
    builders += [b1.s01, b1.s02, b1.s03, b1.s04, b1.s05f,   # s05 foundations
                 b1.s06k,                                    # s06 keystone
                 b1.s06, b1.s07, b1.s08, b1.s09]             # s07..s10
    # display s11–s20
    builders += [b1.s10,                                     # s11
                 b2.s11, b2.s12, b2.s13, b2.s14, b2.s15,     # s12..s16
                 b2.s16, b2.s17, b2.s18, b2.s19]             # s17..s20
    # display s21–s30
    builders += [b2.s20,                                     # s21
                 b3.s21, b3.s22, b3.s23, b3.s24, b3.s25,     # s22..s26
                 b3.s26, b3.s27, b3.s28, b3.s29]             # s27..s30
    # display s31–s41 (+3 from the block-5 EN-parity rebuild, see below)
    builders += [b3.s30,                                     # s31
                 b4.s31, b4.s32, b4.s33]                     # s32..s34
    builders += [b4.s33b]                       # NEW (r3): BT Group / Azure
                                                # Triangle vs IaC insecurity
    builders += [b4.s34,
                 b4.s35b,                       # NEW (r2): §6.3 docs tooling
                 b4.s35,
                 b4.s36, b4.s37]
    builders += [b4.s37b]                       # NEW (r3): Uber + Kiro
                                                # dual-register bridge
    builders += [b4.s38, b4.s39, b4.s40]

    # EN parity with the 58-slide RU deck is landing block by block across five
    # parallel worktrees (issue #172 / #162 round 6). Until all five are merged
    # the count is checked softly so a partially-merged tree still renders.
    EXPECTED_FINAL = 58
    if len(builders) != EXPECTED_FINAL:
        print(f"note: {len(builders)} builders — EN parity target is "
              f"{EXPECTED_FINAL} (blocks still landing)")
    for fn in builders:
        fn(p)

    # Footer-less render for publication (issue #176): the muted «N / TOTAL»
    # page-number stamp is intentionally disabled. Ref-list / footer band
    # (left-aligned, x=0.55) and roadmap bar are unaffected.
    total = len(builders)

    n = len(p.slides.__iter__.__self__._sldIdLst)
    assert n == len(builders), f"expected {len(builders)} slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides")


if __name__ == "__main__":
    main()

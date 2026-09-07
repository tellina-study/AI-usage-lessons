"""Build of Lecture 5 "AI Product: the full lifecycle" — EN FULL DECK.

EN twin of build_lec05.py: same display order (divider -> overview(sNNb ELI5)
-> classical base -> AI capabilities -> AI limits -> failure case(s)), same
56-slide count. Only visible strings + speaker notes are translated; layout,
palette, motif, memes (EN captions), charts (EN labels) mirror the RU build.

Source-of-truth: deck.en.yaml + deck-part2.en.yaml + slides-en/*.md.
Issue #189 (Ф3 EN re-render) · Branch: hc/pldlc-lesson5-c5cc1586

Palette LOCKED: Ocean Gradient + Teal secondary + Gold >=1x/slide. Motif
"Ocean rounded box". Canvas 13.333"x7.5" (16:9).

Target 56 slides = 49 original IDs + s13a + 6 new sNNb ELI5 overviews.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers_en import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1_en as b1  # noqa: E402
import slides_band2_en as b2  # noqa: E402
import slides_band3_en as b3  # noqa: E402
import slides_band4_en as b4  # noqa: E402

OUT = ROOT / "rendered/lec-05-en.pptx"


def main():
    p = setup_pres()
    builders = [
        # -- Section 0. Introduction + keystone --
        b1.s01, b1.s02, b1.s03, b1.s04, b1.s05, b1.s06,
        # -- Section 1. Discovery --
        b1.s07, b1.s07b,
        b1.s08, b1.s09, b1.s10, b1.s11, b1.s12, b1.s13, b1.s13a,
        # -- Section 2. Design --
        b2.s14, b2.s14b, b2.s15, b2.s16, b2.s17, b2.s18, b2.s19, b2.s20,
        # -- Section 3. Build & Launch --
        b2.s21, b2.s21b, b2.s22, b2.s23, b2.s24, b2.s25, b2.s26, b2.s27,
        # -- Section 4. Measure --
        b3.s28, b3.s28b, b3.s29, b3.s30, b3.s31, b3.s32, b3.s33, b3.s34, b3.s35,
        # -- Section 5. Support --
        b3.s36, b3.s36b, b3.s37, b3.s38, b3.s39, b3.s40, b3.s41, b3.s42, b3.s43,
        # -- Section 6. Governance / finale --
        b4.s44, b4.s44b, b4.s45, b4.s46, b4.s47, b4.s48, b4.s49,
    ]
    builders = [b for b in builders if b is not None]

    for fn in builders:
        fn(p)

    total = len(builders)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, total)

    n = len(p.slides.__iter__.__self__._sldIdLst)
    assert n == total, f"expected {total} slides, got {n}"
    assert n == 56, f"target 56 slides, got {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides (EN FULL DECK)")


if __name__ == "__main__":
    main()

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

EN-Sync (issue #172, 5-way block split): the RU deck reached 58 slides over
rounds 1–6 and each EN block wired its own new builders here. This is the
assembly pass across all five blocks — the slide total is no longer hard-coded
per block: it is checked against the rendered RU deck (ru_slide_count), so a
partially merged tree still renders and reports the parity gap.
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
RU_DECK = ROOT / "rendered/lec-04.pptx"


def ru_slide_count():
    """How many slides the RU deck actually has — the EN parity target.
    Returns None when the RU deck has not been rendered in this tree."""
    if not RU_DECK.exists():
        return None
    import zipfile
    import re as _re
    with zipfile.ZipFile(RU_DECK) as z:
        return len([n for n in z.namelist()
                    if _re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])


def main():
    p = setup_pres()
    builders = []
    # --- EN-sync block 1 (#172): +b1.s03b (industry adoption, RU round 6) and
    # +b1.s09b (AWS Kiro vs 847 deployments, RU round 3). Both were missing
    # entirely from the Sept-19 EN baseline.
    builders += [b1.s01, b1.s02, b1.s03,
                 b1.s03b,                                    # NEW (RU round 6)
                 b1.s04, b1.s05f,                            # foundations
                 b1.s06k,                                    # keystone
                 b1.s06, b1.s07, b1.s08, b1.s09,
                 b1.s09b]                                    # NEW (RU round 3)
    # display s11–s20 (+3 from EN-Sync Block 2: b1.s11b · b2.s14b · b2.s17b —
    # the RU round-2/round-3/round-6 inserts, placed in the same order the RU
    # assembler uses: s11 → s11b → s12 → s13 → s14 → s15 → s14b → s16 → s17 →
    # s18 → s17b → s19).
    builders += [b1.s10,                                     # s11
                 b1.s11b,                                    # NEW (r2)
                 b2.s11, b2.s12, b2.s13, b2.s14,             # s12..s15
                 b2.s14b,                                    # NEW (r6 b1)
                 b2.s15,                                     # s16
                 b2.s16, b2.s17,                             # s17..s18
                 b2.s17b,                                    # NEW (r3)
                 b2.s18, b2.s19]                             # s19..s20
    # display s21–s30
    # EN-sync block 4 (issue #172 / #162): +b3.s25b (BDD + trunk-based) and
    # +b3.s25c (the agent's local test toolkit) after the testing-failure slide,
    # matching the RU deck's own round-2 insert / round-6 rebuild; +b3.s30b
    # (Amazon Q wiper) after the security-failure slide, matching the RU deck's
    # round-3 insert. Other EN-sync blocks add their own builders here too —
    # the count below is bumped per block, not owned by any one of them.
    builders += [b2.s20,                                     # s21
                 b3.s21, b3.s22, b3.s23, b3.s24,
                 b3.s25b, b3.s25c,                           # NEW (EN-sync b4)
                 b3.s25,
                 b3.s26, b3.s27, b3.s28, b3.s29]
    builders += [b3.s30b]                                    # NEW (EN-sync b4)
    # display s31–s41
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

    # Parity target: one EN slide per RU slide. The number is read from the RU
    # deck rather than hard-coded, so a partially merged tree still renders and
    # the gap is reported instead of crashing the build (EN-sync assembly pass).
    expected = ru_slide_count()
    if expected is not None and len(builders) != expected:
        print(f"WARNING: {len(builders)} EN builders vs {expected} RU slides "
              f"— EN/RU parity gap of {expected - len(builders)}")
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

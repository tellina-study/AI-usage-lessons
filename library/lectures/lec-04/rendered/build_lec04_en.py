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
    # Assembly pass across all five EN-sync blocks (#172 / #162 round 6).
    # The order below MIRRORS build_lec04_v4.py's own builders list 1:1 — the
    # RU deck is source of truth for sequence as well as content, so parity is
    # a property of this list, not a number someone remembered to bump.
    builders = []
    # display s01–s12
    builders += [b1.s01, b1.s02, b1.s03,
                 b1.s03b,                                    # NEW (r6 b5): industry adoption
                 b1.s04, b1.s05f,                            # foundations
                 b1.s06k,                                    # keystone
                 b1.s06, b1.s07, b1.s08, b1.s09]
    builders += [b1.s09b]                                    # NEW (r3): AWS Kiro vs 847 deployments
    # display s13–s24
    builders += [b1.s10,
                 b1.s11b,                                    # NEW (r2): requirements visualization
                 b2.s11, b2.s12, b2.s13, b2.s14,
                 b2.s14b,                                    # NEW (r6 b1): artifacts of the 4 practices
                 b2.s15,
                 b2.s16, b2.s17]
    builders += [b2.s17b]                                    # NEW (r3): Gemini CLI self-review
    builders += [b2.s18]                                     # four levels of agent context
    builders += [b2.s18b]                                    # NEW (r3): curation — honest limits
    builders += [b2.s19]                                     # harness gate
    # display s27–s32 (NEW, #162): Skills · MCP · task logging · git
    # conventions · secrets (Register) · git worktree. Presentation order
    # follows the RU r3 QA-fix swap: task logging (s20e) before git
    # conventions (s20d); the file/slide ids themselves are not renamed.
    builders += [b2.s20b, b2.s20c,
                 b2.s20e,
                 b2.s20d,
                 b2.s20g,                                    # NEW (r3): secrets/.env — Register case
                 b2.s20f]
    # display s33–s44
    builders += [b2.s20,                                     # the 70% problem
                 # b3.s21 (anti-hype benchmarks) REMOVED — RU round 6 block 3
                 # dropped it; the EN twin follows. Vendor skepticism is
                 # carried by s20 (70% problem) and s37/s38 (triangulation,
                 # risk triad).
                 b3.s22, b3.s23, b3.s24,
                 b3.s25b, b3.s25c,                           # NEW (r2): BDD/trunk-based · test tooling
                 b3.s25,
                 b3.s26, b3.s27, b3.s28]
    builders += [b3.s29]
    builders += [b3.s30b]                                    # NEW (r3): Amazon Q wiper
    # display s45–s58
    builders += [b3.s30,
                 b4.s31, b4.s32]
    builders += [b4.s33]
    builders += [b4.s33b]                                    # NEW (r3): BT Group / Azure Triangle vs IaC
    builders += [b4.s34,
                 b4.s35b,                                    # NEW (r2): docs tooling
                 b4.s35,
                 b4.s36]                                     # synthesis matrix (vendor column removed)
    builders += [b4.s37]                                     # triangulation
    builders += [b4.s37b]                                    # NEW (r3): Uber + Kiro dual register
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

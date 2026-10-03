"""Build of Lecture 5 "AI Product: the full lifecycle" — EN FULL DECK.

EN twin of build_lec05.py. Composition and display order are MIRRORED from
that file's `ORDER` constant position for position — 56 slides, same ids, same
sequence. Only the visible strings and the speaker notes are English; layout,
palette, motif, geometry, icons, memes (EN captions) and charts (EN labels)
mirror the RU build.

Order inside a phase (deck.yaml, rebuild of 2026-09-28, issue #212):
  divider -> the classical base in one defining line -> what AI changes ->
  practice (one to three) -> limits -> the failure of that phase.
The practice sits after the named classical base and before the failure, so
that it reads as the answer to the problem just shown. In Sections 4-6 there
is no separate "what AI changes" slide — the practices carry that work.

Source-of-truth: deck.en.yaml + deck-part2.en.yaml + slides-en/*.md (notes and
sources are pulled from the .md automatically via load_notes /
notes_with_sources; `_helpers_en.SLIDES_DIR` points at slides-en/).

Palette LOCKED: Ocean Gradient + Teal secondary + Gold >=1x/slide. Motif
"Ocean rounded box". Canvas 13.333"x7.5" (16:9).

EN PARITY REBUILD, issue #212 (2026-10-03). The EN deck previously carried a
DIFFERENT set of 56 slides — the pre-rebuild composition. Brought to the RU
`ORDER`:
  added (18) — s11a s11b s17a s24a s24b s24c s30a s31a s38a s38b s45a s45b
    (practice cards, slides_band6_en.py) · s14a s36c (new section slides) ·
    s50 s51 s53 s55 (Section 7 in full, slides_band5_en.py);
  rewritten under the same id (3) — s04 (bridge from Lecture 4 -> why a
    product needs a loop) · s13a (IBM Watson Health -> Humane AI Pin) ·
    s19 (Character.AI -> Tesla mode confusion);
  dropped (18) — s05 (removed by the owner) · s07b s14b s21b s28b s36b s44b
    (the ELI5 overviews, gone as a class) · s24 (absorbed by s24a) · s31
    (absorbed by s31a) · s38 (absorbed by s38a/s38b) · s09 s13 s16 s20 s30
    (superseded bases/failures) · s35 s43 (per-section syntheses) · s49
    (a duplicate of s47/s51/s55).
The 18/18 match is a coincidence, not a symmetry: by file name the divergence
is 21/21, because s04/s13a/s19 keep their number and change their content.
The dropped builder functions stay in slides_band1..4_en.py as dead code,
marked as such in place — the same convention build_lec05.py states.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _helpers_en import setup_pres, ROOT, page_number  # noqa: E402
import slides_band1_en as b1  # noqa: E402
import slides_band2_en as b2  # noqa: E402
import slides_band3_en as b3  # noqa: E402
import slides_band4_en as b4  # noqa: E402
import slides_band5_en as b5  # noqa: E402
import slides_band6_en as b6  # noqa: E402

OUT = ROOT / "rendered/lec-05-en.pptx"

# Practice slides (band6) — addressed by id, so that the order reads together
# with the rest.
P = {fn.__name__: fn for fn in b6.BUILDERS}


# Display order — a module-level constant, mirroring build_lec05.ORDER
# position for position.
ORDER = [
    # -- Section 0. Introduction + keystone --
    # issue #212: s05 removed by the owner; s04 rebuilt from "the bridge from
    # Lecture 4" into "why a product needs a loop and what happens without
    # one" (chapter.md §0.3a).
    b1.s01, b1.s02, b1.s03, b1.s04, b1.s06,
    # -- Section 1. Discovery --
    b1.s07,                      # divider
    b1.s08,                      # base: Customer Development
    b1.s10,                      # what AI changes (+ the Deloitte boundary)
    P["s11a"], P["s11b"],        # practices
    b1.s11,                      # limits
    b1.s12, b1.s13a,             # failures
    # -- Section 2. Design --
    # issue #212, owner review 2026-10-01: the section gained s14a — the
    # scope of the word "design" (surfaces of contact, the behaviour of the
    # system, the answer under uncertainty). It sits right after the divider
    # and before the base, so that the double diamond and the design system
    # read wider than the screen.
    b2.s14,                      # divider
    b2.s14a,                     # the scope of design: surfaces and behaviour
    b2.s15,                      # base: Double Diamond
    b2.s17,                      # what AI changes
    P["s17a"],                   # practice
    b2.s18,                      # limits (+ iTutorGroup as a neighbouring class)
    b2.s19,                      # failure
    # -- Section 3. Build and launch --
    b2.s21,                      # divider
    b2.s22,                      # base: MVP and the mechanics of a release
    b2.s23,                      # what AI changes
    P["s24a"], P["s24b"], P["s24c"],   # practices
    b2.s25,                      # limits
    b2.s26, b2.s27,              # failures
    # -- Section 4. Measurement --
    b3.s28,                      # divider
    b3.s29,                      # base: the controlled experiment and the OEC
    P["s30a"], P["s31a"],        # practices
    b3.s32,                      # limits
    b3.s33, b3.s34,              # failures
    # -- Section 5. Support and operations --
    # owner review 2026-10-01: the section was turned from "controlling AI
    # models" into "using AI in support". s36c was added — it introduces the
    # subject of the section (quality made of two halves) before the first
    # dive into numbers.
    b3.s36,                      # divider
    b3.s36c,                     # base 1: support as holding quality
    b3.s37,                      # base 2: the "system" half — the error budget
    P["s38a"], P["s38b"],        # practices
    b3.s39,                      # limits
    b3.s40, b3.s41, b3.s42,      # failures
    # -- Section 6. Governance --
    b4.s44,                      # divider
    b4.s45,                      # base: portfolio governance
    P["s45a"], P["s45b"],        # practices
    b4.s46,                      # the run-up to the failure
    b4.s47, b4.s48,              # failures
    # -- Section 7. Synthesis and the decision framework --
    b5.s50, b5.s51, b5.s53, b5.s55,
]


# The footer zone. Slide content starts above 7.00": below that mark only the
# sources line (top 7.02-7.04") and the page-number stamp (top 7.16")
# legitimately live. The hard floor for content is 7.16": the roadmap bar on
# the dividers legitimately reaches 7.13" (by design, see page_number), so the
# threshold is set by the stamp rather than by the sources line.
CONTENT_TOP = 7.00
CONTENT_FLOOR = 7.16


def report_overflows(pres):
    """Print overflows AFTER the full deck is assembled.

    Two different checks, because they are blind to different things
    (issue #212):

    1. `b6.WARN` — the guard over the practice-card bands. It compares the
       height the text needs against the height of its box.

    2. Footer geometry. Check 1 structurally cannot see the case where the
       text fits inside its box but the box itself has run off the bottom of
       the slide: the band height is computed by the same `est_h`, so there
       is no disagreement between them to catch. Here it is caught on the
       finished file: a shape that STARTS in the content zone and ENDS below
       the footer floor is an overflow.

    Bands 1-5 have no guard of their own at all; check 2 is so far the only
    thing that covers them.

    KNOWN BLIND SPOT (issue #212, caught on the RU deck at s24c): neither
    check measures a DIAGRAM CAPTION. The build printed "no overflows" while
    a word in a schema caption was clipped. Captions have to be looked at in
    the snapshots, by eye.
    """
    warns = list(b6.WARN)
    for i, slide in enumerate(pres.slides, start=1):
        for sh in slide.shapes:
            if sh.top is None or sh.height is None:
                continue
            top = sh.top / 914400.0
            bottom = top + sh.height / 914400.0
            if top < CONTENT_TOP and bottom > CONTENT_FLOOR:
                txt = ""
                if sh.has_text_frame:
                    txt = sh.text_frame.text.strip().split("\n")[0][:60]
                warns.append(
                    f"slide {i} ({ORDER[i - 1].__name__}): shape with top "
                    f"{top:.2f}\" runs down to {bottom:.2f}\" — into the "
                    f"slide footer" + (f" | {txt}" if txt else ""))
    if warns:
        print("--- overflows (heights need fixing) ---")
        for w in warns:
            print("  " + w)
    else:
        print("no overflows")


def main():
    p = setup_pres()
    builders = ORDER

    for fn in builders:
        fn(p)

    total = len(builders)
    for i, slide in enumerate(p.slides, start=1):
        page_number(slide, i, total)

    n = len(p.slides._sldIdLst)
    assert n == total, f"expected {total} slides, got {n}"
    # The slide count is NOT a literal: parallel sessions add and remove
    # slides, and a hard constant broke the build for every next one. We count
    # from ORDER — it is the source of truth about the deck's composition.
    assert n == len(ORDER), f"ORDER declares {len(ORDER)} slides, built {n}"
    p.save(str(OUT))
    print(f"saved {OUT} — {n} slides (EN FULL DECK)")
    report_overflows(p)


if __name__ == "__main__":
    main()

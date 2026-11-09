# Lecture 6 — EN Twin Visual Loop Iteration Log (Bilingual Production Rule, issue #172/#324)

**Deck:** "AI in Engineering Design and CAD/CAM" (EN twin) · 32 slides · 75.0 min
**Builder:** `build_lec06_en.py` — geometry-preserving EN twin of `build_lec06.py`
(RU-locked, 4 visual-loop iterations already passed, see `iteration-log.md`).
**Palette:** Ocean Gradient LOCKED v3 (identical to RU — no palette changes for the
EN twin). Motif: Ocean rounded box (radius 12, surface #F4F7FA, stroke #1C7293 1.5pt).
**Canvas:** 13.333" × 7.5" (16:9).

## Scope of this pass

This is NOT a redesign. The RU layout already passed 4 iterations of visual QA
(layout bugs in `two_col_compare`, `build_s11` timeline, `pipeline_row`, s02, s23,
s30 — all fixed and locked in the RU builder). This pass only translates visible
string literals and checks for EN-translation-induced regressions — primarily
text-fit problems, since English renders longer than Russian for equivalent
meaning at the same geometry/font size.

## Setup fixes (before first render)

- `ROOT` was hardcoded to a stale `/tmp/lec-06-wt/...` path from a prior session
  → changed to `Path(__file__).resolve().parent.parent` (resolves correctly inside
  this worktree).
- `SLIDES_DIR` → `slides-en` (so `load_notes()` picks up the EN speaker notes
  instead of the RU ones).
- `OUT` → `rendered/lec-06-en.pptx`.
- Source strings for every `build_sNN` function were translated against the
  already-locked EN artifacts (`deck.en.yaml`, `slides-en/sNN-*.md`,
  `speech.en.md`) rather than re-translated from scratch, to avoid terminology
  drift (locked terms: "spectral bias," "silent error," "seam between systems,"
  "fully-stressed structure," "OKB Sukhoi," "MS-21-300," "Federal Law 187/58,"
  course title `Course "AI Across Industries"`).

## Visual loop — min 3 iterations (performed 3)

### Iter 1 — baseline build + full-deck inspection (150 dpi)

- (a) Inspected: all 32 PNG snapshots, full read-through for EN-specific
  overflow/text-fit regressions (the #1 risk per brief point 4), since RU
  geometry/layout is already locked and proven.
- (b) Found:
  - **Typographic inconsistency** — the whole file used ASCII double-hyphen
    `--` instead of the em dash `—` that `deck.en.yaml`/`slides-en/*.md`/
    `speech.en.md` consistently use. Global replace `--` → `—` (107
    occurrences, comments + docstrings + visible strings) — not a layout bug,
    but a typographic-consistency fix needed before judging anything else.
  - **P1 overflow — s08** (3 vertical class cards, "alternative" segment):
    card 1 ("Generative AI / LLM assistant") alternative text — full-length
    translation "parametrics + deterministic topology optimization + FE
    validation; the normative base" — wrapped to 4 lines inside a 3-line-budget
    segment (`seg_h` fixed by `ch`/3), overflowing the card's own rounded-box
    border at the bottom. RU original used an abbreviated "параметрика +
    детерм. топ-оптимизация + КЭ; норматив" that fit in 3 lines at the same
    geometry — the literal EN translation was simply longer.
  - **P2 border-crossing — s18** (PINN stress-curve sketch, gold gap label):
    the gold "an underestimated\nstress" label textbox (fixed width 1.85",
    positioned at `gap_x+0.26`) extends past the ocean-box's own right edge by
    design (same geometry in RU and EN) — but the RU text ("занижение\n
    напряжения") was short enough not to visibly reach that edge, while the
    longer first line "an underestimated" visually touched/crossed the box's
    stroke.
  - Everything else (28 of 32 slides: cover, hook, lecture-map, all 6 section
    dividers, both `two_col_compare` comparison slides (s05/s10/s16/s21/s28),
    both matrix slides (s07/s12/s13/s17/s27), the s11 timeline, all `pipeline_row`
    slides (s14/s19/s22/s30-tree), s06 axis, s23 Mars dominant-block, s24
    range chart, s26 criteria table, s31 checklist+matrix, s32 Q&A) rendered
    clean — no overflow, no clipped text, no orphaned lines.
- (c) Checklist: comparison (s05/s10/s16/s21/s28) PASS; matrix (s07/s08/s12/
  s13/s17/s27) — s08 FAIL (overflow), rest PASS; timeline (s11) PASS; pipeline
  (s14/s19/s22/s30) PASS; schema_matrix (s26/s31) PASS; PINN sketch (s18) FAIL
  (border-crossing label).

### Iter 2 — targeted fixes (150 dpi, slides 8 + 18 only)

- (a) Inspected: s08, s18 (the two P1/P2 findings from iter 1) after rebuild.
- (b) Changed:
  - `build_s08`: card-1 alternative string shortened to "parametrics + det.
    topology optimization + FE check; norms" (meaning preserved, locked terms
    kept — "parametrics," "topology optimization" — only word choice
    compacted, matching the RU original's own level of abbreviation for this
    cell). No geometry/font-size change needed.
  - `build_s18`: gold gap label shortened from "an underestimated\nstress" to
    "underestimated\nstress" (drops only the leading article — meaning,
    units, and the numeric relationship shown by the arrow are unaffected).
- (c) Re-rendered only pages 8 and 18 (targeted) via `render_en.sh 8 18`.
  Checklist: **s08 PASS** — all 3 cards' alternative segments now fit cleanly
  in 3 lines inside their own rounded-box border, no overflow. **s18 PASS** —
  gold label now sits with clear margin inside the ocean box, no border
  overlap.

### Iter 3 — full-deck automated sweep + re-render (150 dpi)

- (a) Ran `tools/presentation-build/promah_polya.py` on both `lec-06.pptx`
  (RU) and `lec-06-en.pptx` to check for EN-introduced geometry drift: **both
  decks report byte-identical numbers** — `220/827 = 26.6%`, 19 distinct
  values, per-slide median 4.0, same value histogram. This confirms the EN
  twin changed zero shape positions/sizes (as required) — the pre-existing
  26.6% field-miss baseline is a RU-deck property carried over unchanged, not
  something introduced or worsened by translation.
- (b) Ran `tools/presentation-build/predgate_sweep.py` on `lec-06-en.pptx`:
  0 blocking hits across all 4 blocking groups (scaffold leaks, timing
  markers, methodology commentary, scientific-notation leaks), 0 slides
  without speaker notes, 0 notes under 150 words, 0 live hyperlinks (matches
  RU — this deck has no hyperlinked sources). The 5 "measurable statement"
  lines it flags for manual baseline-check (s02/s12/s12/s24/s24) are the same
  ones already carrying inline baselines in the RU original (e.g. "8 parts →
  1 · mass −~40% · >150 variants evaluated" — cascade-constrained, ranges not
  exact numbers per `deck.en.yaml` header).
- (c) Full clean re-render of all 32 pages (`render_en.sh` with no page args)
  to produce the final `lec-06-en.pptx` / `lec-06-en.pdf` / `snapshots/
  en-slide-NN.png` set. Spot-re-checked s08/s18 once more in the full-deck
  render (not just the targeted iter-2 render) to confirm the fix survived a
  full rebuild — confirmed clean.
- (d) Re-ran the Cyrillic self-check (`grep -nP '[а-яА-ЯёЁ]' build_lec06_en.py`)
  and slide-count check (`len(Presentation(...).slides._sldIdLst)`) on the
  final file: **0 Cyrillic hits, exactly 32 slides.**

## What did NOT need fixing (explicitly checked, found clean)

- Title textboxes with tight height budgets (`h=0.85`–`1.15`) that wrap to 2
  lines in EN where RU was sometimes 1 line (s06, s08, s12, s14, s23, s26) —
  all fit within their allotted height with margin; none clipped.
- `pipeline_row` stage headers that wrap to 3 lines in EN vs. 2 in RU (s19
  stage 1 "Hundreds of variants / at the search stage") — fits within
  `head_h=1.00"` with margin (3 lines × 15pt × 1.10 spacing ≈ 0.69" < 1.00").
- `gold_callout` boxes carrying longer EN sentences (s17, s22, s24) — all
  fit within their specified `h` with margin; checked individually against
  line-count × font-size × line_spacing budget.
- s31 checklist item 3 ("What's optimized, who set the constraints? Is the
  statement complete?") wraps to 3 lines vs. RU's 2 — tight against the next
  numbered circle's slot (`chy += 0.74`) but does not overlap it.

## Deviations from pure 1:1 geometry preservation

None. Both fixes applied (s08, s18) were **pure string-content edits** —
word-choice shortening within the same textbox geometry, font size, and line
spacing already locked by the RU builder. No position, size, color, or
image call was touched anywhere in the file.

## Self-check summary

- `grep -nP '[а-яА-ЯёЁ]' build_lec06_en.py` → 0 hits.
- `python3 build_lec06_en.py` → `Saved: .../lec-06-en.pptx (32 slides)`.
- `promah_polya.py` on `lec-06-en.pptx` → identical to RU baseline (26.6%,
  19 values, median 4.0) — no geometry drift from translation.
- `predgate_sweep.py` on `lec-06-en.pptx` → `ИТОГО блокирующих совпадений: 0`.
- Anti-anglicism / `deep_latin_scan.py` — **not applicable**: this deck's
  target language is English (Bilingual Production Rule explicitly scopes
  the RU-only Russification mandate out of EN artifacts).

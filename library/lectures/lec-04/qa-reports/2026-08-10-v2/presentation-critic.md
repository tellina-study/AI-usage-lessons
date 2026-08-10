VERDICT: APPROVE-WITH-POLISH

# Presentation Critic Report — Лекция 4 — Раздел 2 re-verification (2026-08-10, v2)

Re-verification pass of the 4 original P1 findings from the prior REVISE
verdict, after the fix pass in commit `a858c88` (which split old s13e
into s13e/s13f and renumbered old s13f/s13g → s13g/s13h). Method: fresh
render of slides s10-s13, s13a-h directly from the current
`library/lectures/lec-04/rendered/lec-04.pptx` (not from cached
`snapshots/final_v2/`, though the file sizes matched byte-for-byte,
confirming those caches were current) via
`render_slides_png_workaround.py`, independent pixel-level RGB gold scan
(PIL+numpy, tolerance ±30 on `#F0AB00`), direct XML font-run inspection
via `python-pptx` (not trusting `build_lec04.py` source `size=` args
alone — confirmed no `normAutofit` shrink), and vision inspection of all
8 fresh PNGs.

## Sanity check on the iteration-log self-report

`rendered/iteration-log.md`'s 2026-08-10 (v2) entry claims specific
pixel counts per slide. I independently re-derived these from scratch
(fresh render, fresh scan script, not copy-pasted) and got **identical
numbers**: s13a 2556, s13b 2573, s13c 48923, s13d 43776, s13e 6335,
s13f 47011, s13g 7766, s13h 40756. This is a good sign — the log's own
methodology this round (pixel-level, not visual-impression) is sound
and reproducible, unlike the prior round's false "deck-wide convention"
claim that this same log entry documents catching. Trust increased but
verification was still performed independently end-to-end, not by
accepting the printed numbers.

## Original 4 P1 findings — all CONFIRMED FIXED

### 1. s13e title anglicism — FIXED
Title now reads (verified via direct `python-pptx` text extraction from
the rendered PPTX, slide 19): **«Presence paradox» (парадокс присутствия
файла): само наличие — не гарантия пользы.** Gloss is inline,
immediately following the term, guillemets used consistently with
`chapter.md` §2.7's own convention. Visually confirmed on the rendered
PNG — clean, no wrapping, no overflow.

### 2. s13d zero gold — FIXED
Independent pixel scan: 43,776 gold-range pixels (4.75% of frame),
matching the log's claim exactly. Visually confirmed: the fix promoted
the closing "Файл, который никто не обновлял год…" line to a solid
gold-fill plate with dark (`DEEP`) text — genuine gold-fill, not
gold-text-on-light (the WCAG-defect pattern flagged in this project's
memory `project_ocean_palette_gold_contrast_defect`). Correct fix shape.

### 3. New s13f + s13g (post-split renumbering) zero gold — FIXED, both
Independent pixel scan: s13f (new, git-conventions) = 47,011 px
(5.10%), s13g (renumbered, task-log-three-patterns) = 7,766 px (0.84%).
Both confirmed visually: s13f has a large, unmissable gold-fill callout
bar ("Формат парсится программой…"); s13g has a smaller neutral gold
badge ("3 паттерна") deliberately kept off any single pattern card,
consistent with README anti-pattern #21 (inconsistent gold-emphasis
across same-tier cards) — correct design judgment, not a shortcut.

### 4. s13h (renumbered from old s13g) table font 9.7pt — FIXED
Verified via direct XML run inspection of the rendered PPTX (not the
`build_lec04.py` source arg) — every table body-cell text run measures
exactly **12.0pt**, header cells 12.5pt, no `normAutofit` scale
override found. Table was widened from 5 columns to 4 (merged
"Обнаруживаемость" + "Что ломается") to make room; visually the table
reads cleanly on the rendered PNG, no cramping, no overflow.

**All 4 original P1s are genuinely resolved, independently re-verified,
not just self-reported.**

## New finding from this pass

### Slide s13e — "Honest Lying" bare English term, zero Russian gloss
**Severity:** P1
**Issue:** The slide's second research-finding heading, "**Honest
Lying: риск самостоятельной правки агентом**," uses the bare English
term "Honest Lying" as a headline text run with no parenthetical
Russian gloss — the exact same defect class as the original P1 #1
("Presence paradox" bare title), which was fixed elsewhere on this same
slide. The Russian clause that follows ("риск самостоятельной правки
агентом") describes the *risk*, it does not translate the *term* the
way "(парадокс присутствия файла)" directly glosses "Presence paradox"
two lines above it on the same slide. A student reading only the slide
has no way to know what "Honest Lying" means as a name — it's not
decomposable from English cognates the way "presence paradox" almost
is. `chapter.md` line 421 also uses "«Honest Lying»" in guillemets
without an inline gloss, so this is not purely a slide-level
regression, but the slide is where the ENFORCED anti-anglicism rule
(`tools/presentation-build/README.md` §5.8) applies most directly to
student-facing visible body, and the fix pass demonstrably knew how to
apply this exact pattern one term above.
**Recommendation:** Add a parenthetical Russian gloss immediately after
"Honest Lying," matching the deck's own established pattern, e.g.
«Honest Lying» (правдоподобная, но неверная фиксация вывода) or
similar — something that names the *mechanism* (self-consistent
false belief that gets reinforced rather than corrected), not just the
risk description that already follows. Cross-reference `chapter.md`
line 421 for wording that could carry the same gloss back into the
chapter for consistency, though that's a `book-editor` follow-up, not
blocking for GATE B on the slide alone.
**Visual evidence:** Rendered PPTX slide 19 (s13e), fresh render this
session — text run "Honest Lying: риск самостоятельной правки агентом"
appears as a bold sub-heading with no parenthetical directly attached.

### Slide s13b — "structure + constraints + tests" unglossed pattern-name (minor)
**Severity:** P2
**Issue:** Closing callout line ends with "Прямая параллель паттерну
structure + constraints + tests" — three English words used as a named
pattern with zero gloss, in speaker-notes-adjacent visible body text.
**Recommendation:** Either gloss inline («паттерну «структура +
ограничения + тесты» (structure + constraints + tests)») or drop the
English entirely since the Russian equivalent is self-explanatory and
the callback value (matching earlier Lecture terminology) is weak here
compared to `context rot` / `self-authored`, which carry actual
technical specificity English alone conveys.
**Visual evidence:** Rendered PPTX slide 16 (s13b) bottom gold callout.

## Fresh full-section pass — s10, s13a-h (12 slides total: s10-s13, s13a-h)

- **Roadmap-bar discipline:** confirmed absent on all 8 of s13a-h via
  direct text-extraction grep (`'Раздел 0' in texts` = False on all),
  confirmed present on s10 (section divider) via visual inspection —
  correctly matches Lec-N-1 pattern (roadmap-bar only on dividers +
  cover).
- **s13e→s13f transition:** reads as two related-but-distinct topics,
  not a jarring cut. s13f's speaker notes explicitly bridge back
  ("Здесь работает тот же принцип, что и со steering-файлом…" /
  "Тот же принцип, что и у steering-файла в целом" in the closing
  line) — the split preserved narrative continuity rather than just
  mechanically dividing content.
- **s13f→s13g transition:** s13g broadens from "contract format" to
  "where to persist task state between sessions" — a natural widening
  of scope within the same "structure vs. freeform/ritual" throughline
  that runs through s13d→s13e→s13f→s13g. No orphaned reference found.
- **No duplicate/orphaned content across the split:** grepped s13e,
  s13g, s13h source `.md` files for "Conventional", "git-конвенц" —
  zero hits, confirming the git-conventions block was cleanly moved
  out to standalone s13f with nothing left behind and nothing
  duplicated.
- **Assertion coherence check (s13d→s13e→s13f→s13g assertions read in
  sequence):** anatomy of steering-file → does it actually help (RCT)
  + self-edit risk → git-conventions as a parallel machine-readable
  contract → task-log patterns as a third instance of the same
  structure-vs-freeform theme. Logical progression, no gap.
- **Duration math:** s13a-h `duration_min` sum = 2.5+2.5+2.5+3+3+2+2.5+3
  = 21.0, matches `deck-part2.yaml` line 407's claimed
  `slide_times_sum_min: 102.4` (80.9 base + 21.0 + prior deltas)
  exactly — no drift.
- **44 total slides confirmed** via direct `len(p.slides)` on the
  current PPTX.

## Сводка

- Раздел 2 span reviewed: 12 slides (s10, s11, s12, s13, s13a-h)
- Original P0/P1 issues: 4, all confirmed FIXED (0 remaining)
- New P1 this pass: 1 (s13e "Honest Lying" ungloss — same defect class
  as an issue already fixed one line above it on the same slide)
- New P2 this pass: 1 (s13b minor unglossed pattern name)

## Verdict rationale

1 new P1 + 1 P2, against a backdrop of all 4 original P1s cleanly and
verifiably resolved. Per the 4-level verdict scale: ≤3 cosmetic/P1
fixes with no P0 → **APPROVE-WITH-POLISH**, not REVISE. This is a
single narrowly-scoped miss (one term, one slide, mechanically
identical fix to one already applied two lines above), not a pattern
requiring a new revision round with re-render risk. Recommend applying
the one-line "Honest Lying" gloss fix (and optionally the s13b P2)
inline the same way the "Presence paradox" fix was applied, then
proceed to GATE B — does not warrant blocking the whole Раздел-2
expansion.

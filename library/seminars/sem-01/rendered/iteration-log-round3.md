# Iteration log — round 3 (point-fix round, 2026-08-07)

Continuation of `iteration-log.md` (split here — main file at 561/600 lines).
Source: 2 independent QA passes (presentation-critic + student-simulator,
2026-08-07) that each surfaced P0 `[TODO]` leaks independently, plus 2 P1
findings from the same pass. Task brief required point fixes only — no
unrelated slides touched.

## P0-1 — s03 visible `[TODO: платформа AI-тестирования]` (fixed)

**Root cause:** `build_s03()` hardcoded the visible text with a literal
`[TODO: ...]` suffix baked into the run — rendered verbatim on the PNG.
**Why it survived the earlier deep-latin-scan:** the scan's brand/UI-marker
allowlist classified the bare token `TODO` as legitimate alongside `AI`/`LIVE`
— a grep-pattern classification bug, not a content review miss. This round's
brief explicitly required a *separate* regex pass (`\[TODO`, `\[VERIFY`,
`\[FACT-CHECK`) instead of relying on the general deep-latin-scan.

**Fix:** removed the `— [TODO: платформа AI-тестирования]` suffix from the
`text_box` call in `build_s03()`. Visible text now reads simply "Тест на
платформе AI-тестирования". No layout change needed (text was already inside
a fixed-height box with room to spare).

**Verification:**
- iter1: rebuilt pptx, converted to PDF, extracted `snapshots/round3-s03-03.png`.
  Visual inspection: clean, no bracket text, no overflow, box proportions
  unchanged relative to step 2's card.
- iter2: confirmed `slides/s03-checkpoint-mechanics.md` `## Visual` section
  prose updated to match (no longer describes a `[TODO]` caption).
- iter3: full-deck grep sweep (see below) confirms 0 hits across all 19
  slides' visible text + speaker notes.

## P0-2 — s19 visible `[TODO: телеграм-канал курса]` + `[TODO: телеграм преподавателя]` (fixed)

**Fix:** removed both `text_box` calls entirely (not replaced with other
placeholder text, per brief instruction). Rebalanced the right-column
vertical rhythm: shifted "СПАСИБО" / title / subtext / chip block down and
re-spaced (0.9→1.35, 1.4→1.85, 3.65→4.1, 5.15→5.6) so the block reads as
intentionally centered in the 0.9–7.5" available height instead of leaving a
1.8" dead zone at the bottom where the two TODO lines used to sit.

**Verification:**
- iter1: rebuilt, extracted `snapshots/round3-s19-19.png`. Visual inspection:
  no TODO text, no dangling whitespace below the chip, hero photo collage
  (left 47%) untouched, GOLD-highlighted "Разработка / IT" tile still intact
  (bridges to Lecture 1 per s01 callback).
- iter2: checked visual mass balance — squint test: left photo collage vs
  right text block roughly balanced, no longer top-heavy-with-empty-bottom.
- iter3: confirmed `slides/s19-hero-closing.md` frontmatter `visual.primary`
  + `## Visual` section updated to drop "TODO-плейсхолдеры" from the
  description; speaker notes left as-is (already spoke about contacts
  appearing "здесь отдельно" — accurate, and speaker notes are exempt from
  the visible-body scaffold-leak rule).

## P1-1 — s14 reveal text described old removed painting's prompt (fixed)

**Root cause:** s14's reveal card A text still said "с горами, туманом,
характерным освещением" — leftover language from the pre-round-2 Shishkin/
Savitsky-style prompt ("сосновый лес, туман"). Round-2 swapped the real
painting to Velasco's "Долина Мехико с горы Санта-Исабель" (open valley,
lake, two distant snow-capped volcanoes, warm evening light, rocky
foreground with 2 figures — no fog, no pine forest) but the card A reveal
text was never updated to match.

**Fix:** rewrote the visible card A text in `build_s14()`:
old — "похожую композицию за секунды — с горами, туманом, характерным
освещением"; new — "похожую панораму долины за секунды — с дальними горами и
характерным тёплым светом". Also updated `slides/s14-calibration-image-a.md`
(`## Visual` + `## Speaker notes` — the notes' hypothetical prompt text
changed from "пейзаж, сосновый лес, туман, горы..." to "панорама долины,
дальние горы, вулканы на горизонте, тёплый вечерний свет...").

**Verification:**
- iter1: rebuilt, extracted `snapshots/round3-s14-14.png`. Visual inspection:
  reveal card A text now reads consistently with what's actually visible in
  card B's painting (valley panorama, distant mountains, warm light) — no
  mention of fog or pine forest anywhere on the slide.
- iter2: cross-checked s13 (question card, same painting) for the same
  "туман, сосновый лес" leftover language in its own AI-prompt card — found
  it (see P1-2 below, which replaced that entire card format, resolving this
  too).
- iter3: grepped both `slides/s13-*.md` and `slides/s14-*.md` for "туман"
  and "сосновый" — 0 hits in `## Visual` / `## Assertion` / `## Speaker
  notes` bodies (only in round-3 "point fix" explanatory prose documenting
  the removal, matching the project's existing convention from round-2's
  Shishkin/Savitsky removal notes).

## P1-2 — s13 card format asymmetry gave away the answer (fixed)

**Root cause:** card A (AI side) was icon + italic text description; card B
(human side) was a full-bleed real photograph. The presence/absence of an
actual image was itself the tell, independent of content.

**Fix (option chosen: stylized mockup image, not a real AI-generated file):**
attempted feasibility of a real AI-generated image first — no image-generation
tool is available in this environment/session, so went with the brief's
documented fallback: render card A as a full-bleed stylized landscape mockup
image, in the same footprint/position as card B's real image.

Built via `/tmp/.../gen_s13_mockup.py` (PIL only — no ImageMagick in this
sandbox per `notes/mcp-limitations.md`): vertical sky-to-ground gradient +
3 soft blurred mountain silhouette layers + light film-grain noise overlay,
sized to the exact aspect ratio of the real Velasco image (1280×879).
Deliberately generic/soft-focus (not a copy of Velasco's actual composition —
no lake, no volcano peaks, no figures) so it doesn't hint at or spoil the
real painting's content in either direction. Saved to
`rendered/assets/illustrations/s13-ai-landscape-mockup.png`.

`build_s13()`: card A now calls `add_image()` with this mockup at the same
`x, y, w, h` card B uses for the real photo (previously card A used `icon()` +
`text_box()`). Card A's "Изображение A" label header kept identical to card
B's "Изображение B" header for format symmetry.

**Verification:**
- iter1: rebuilt, extracted `snapshots/round3-s13-13.png`. Visual inspection:
  both cards now full-bleed images, same box dimensions, same corner radius,
  same padding — format is visually indistinguishable as "picture vs text"
  at a glance. Content clearly differs (soft gradient mockup vs detailed
  Velasco panorama) — that's the intended, content-level tell that surfaces
  only on closer look, not a structural giveaway.
- iter2: cropped and closely inspected card A alone
  (`/tmp/s13-cardA-zoom.png`) — image fills frame edge-to-edge, no
  transparency artifacts, no visible seams from the gradient-generation code,
  renders as a plausible (if intentionally generic) synthetic landscape.
- iter3: updated `slides/s13-calibration-image-q.md` `## Visual` +
  `## Speaker notes` to describe the new format-symmetric approach instead of
  the old text-card approach; removed the now-obsolete "сосновый лес, туман"
  prompt-text line entirely (card A no longer shows a literal prompt string).

**Reported per brief instruction ("отчитайся, какой вариант выбрал"):** chose
the stylized-mockup-image fallback, not a real AI-generated file — no
image-generation tool available in this session/environment. Documented here
as the honest choice rather than silently defaulting to it.

## P1-3 — s15 OWID chart leaked source identity before voting (fixed)

**Root cause:** `build_s15()` reused the exact same PNG file
(`assets/screenshots/s16-owid-internet.png`) that s16 (the reveal slide) uses
for disclosure. That PNG has the "Our World in Data" navy logo box, the
English title "Share of the population using the Internet", the English
subtitle, and a 2-line "Data source: ... OurWorldInData.org/internet | CC BY"
caption all baked into the raster image itself — all visible on the
question card, before the vote.

**Fix:** cropped a question-card-only version of the same PNG via PIL
(`Image.crop`), removing the top title/subtitle/logo band (y: 0–98px) and the
bottom source-caption band (y: 543–600px out of 600px total height), keeping
only the plot area (axes, gridlines, the two colored lines with their
"Russia"/"World" end-labels). Saved as
`rendered/assets/charts/s15-owid-internet-noattrib.png` (850×445, vs.
original 850×600). `build_s15()` now points at this cropped file instead of
the original; `build_s16()` (reveal) is untouched and still uses the original
full image with full attribution — disclosure stays where it belongs.

**Residual limitation (documented, not blocking):** the cropped chart still
shows English end-of-line labels "Russia" / "World" (baked into OWID's own
chart rendering, not a separate caption) next to the lines. This is a much
weaker tell than a logo + English title + explicit source caption (the
original 3 identifying elements the brief called out), and removing it would
require re-plotting from raw data rather than cropping the existing asset —
judged out of scope for a point fix. Flagged here for visibility per the
project's "report deviations" convention; not treated as blocking because the
brief's explicit ask (remove logo / caption / English title) is fully done.

**Verification:**
- iter1: rebuilt, extracted `snapshots/round3-s15-15.png`. Visual inspection:
  no OWID logo, no "Share of the population using the Internet" title, no
  source caption anywhere on the card. Chart B now visually reads as "just a
  line chart" like chart A.
- iter2: extracted `snapshots/round3-s16-16.png` (reveal slide, untouched
  logic) to confirm no regression — full OWID chart with logo/title/caption
  still renders correctly there, where disclosure is appropriate.
- iter3: confirmed the AI-generated chart (card A) legend
  "Пользователи AI-ассистентов, %" is in Russian while OWID's line labels
  are in English — a residual minor asymmetry, noted above, not fixed (out
  of scope, judged non-blocking).

## Bonus (optional, not blocking) — s17 pill-shaped verно/неверно chips

student-simulator flagged that the rounded-pill "верно"/"неверно" chips on
s17 visually echo the round-2-removed AI/человек pill-buttons, which could
read as "didn't we just remove these?" Fixed since it was a low-risk,
self-contained change: replaced the two `chip()` (rounded-pill,
filled-background) calls with flat, unbounded text labels ("верно" in TEAL,
"неверно" in SLATE) separated by a thin 0.014"-wide vertical divider bar —
no rounded outline, no fill background, a different shape language from the
removed pill buttons.

**Verification:**
- iter1: rebuilt, extracted `snapshots/round3-s17-17.png`. Visual inspection:
  labels read cleanly, divider bar thin and unobtrusive, no rounded-pill
  shapes remain anywhere on the slide, all 6 rows consistent.
- iter2: checked color contrast — TEAL "верно" and SLATE "неверно" both pass
  a quick eyeball WCAG check against the SURFACE (`#F4F7FA`) row background.
- iter3: confirmed no other slide in the deck (`grep -n "chip(" build_sem01.py`)
  uses this same pill style in a "click here" voting-adjacent context that
  could still cause the same confusion (s04's hand+camera explainer bar uses
  icons, not chips, for the voting mechanic; s19's "Лекция 1 → далее" chip is
  a navigation label unrelated to voting).

## Final grep sweep (round 3, all 19 slides)

```
$ python3 -c "from pptx import Presentation; ..." > /tmp/pptx-visible.txt   # 197 text runs
$ grep -nE '\[TODO|\[VERIFY|\[FACT-CHECK' /tmp/pptx-visible.txt
(no matches, exit 1)

$ python3 -c "... notes_slide.notes_text_frame.text ..." > /tmp/pptx-notes.txt  # 19 notes
$ grep -nE '\[TODO|\[VERIFY|\[FACT-CHECK' /tmp/pptx-notes.txt
(no matches, exit 1)

$ grep -n '\[TODO\|\[VERIFY\|\[FACT-CHECK' rendered/build_sem01.py
(no matches)

$ grep -n '\[TODO\|\[VERIFY\|\[FACT-CHECK' deck.yaml
(no matches)
```

0 hits across visible body + speaker notes + render source + deck.yaml.
Remaining hits in `slides/s03-*.md` / `slides/s19-*.md` are inside this
round's own "point fix" explanatory prose describing what was removed
(same historical-documentation convention as round-2's Shishkin/Savitsky
removal notes) — not rendered to students.

## duration_min regression check

`sum(duration_min across slides/*.md) == 75` (74.99999... floating point) —
unchanged from before this round; no slide's `duration_min` field was
touched by any of the 5 point fixes above.

## Round 4 (2026-08-08) — closed the P1-3 residual gap: "Russia"/"World" labels

**Root cause (recap from P1-3 above):** the round-3 crop removed the OWID
logo, English title/subtitle, and source caption, but the plot area itself
still had "Russia" (blue) / "World" (red) end-of-line labels baked into
OWID's own chart rendering — the one remaining tell that chart B was a
non-Russian source, explicitly logged as "out of scope for a point fix" in
P1-3 above.

**Fix:** no raw OWID CSV available locally, so re-plotting from scratch was
out of proportion for a point fix (per original P1-3 judgment) — instead
used PIL to paint two white rectangles directly over
`assets/charts/s15-owid-internet-noattrib.png` (850×445 RGBA), covering only
the label glyphs:
- Region 1 (`"Russia"`): `(771, 8)–(815, 27)` — pixel analysis showed the
  blue line's last data-point marker sits at x≈748-749 (y≈16-18), well
  clear of the paint region's left edge (x=771).
- Region 2 (`"World"`): `(771, 96)–(815, 117)` — the red line's stroke
  continues to x≈769 before the text starts at x≈773-774; paint region left
  edge (x=771) leaves a 2px buffer past the last confirmed line pixel.

Both regions filled with solid white (255,255,255,255) to match the chart's
plot-area background exactly (verified via pixel sampling — background is
pure white, not off-white). No crop was needed: the paint-over sits
entirely within existing right-margin whitespace, the 2025 tick label and
both lines' terminal markers are untouched and fully visible.

**Verification:**
- Pixel-level check before painting: sampled RGB values in the target
  region distinguished glyph pixels (saturated blue/red, e.g. `(76,106,156)`
  for "R", `(177,53,7)` for "d") from line/gridline pixels (light gray
  `(240-241,240-241,240-241)` gridline dashes, and the actual line strokes
  confirmed to terminate at x≈749 / x≈769 respectively via a directional
  column scan restricted to non-text y-ranges).
- Rebuilt `sem-01.pptx` via `python3 build_sem01.py` (19 slides, no errors).
- Re-rendered PDF via `soffice --headless --convert-to pdf`, extracted only
  page 15 (`pdftoppm -f 15 -l 15 -r 150 -png sem-01.pdf snapshots/s15-fix`)
  — visual confirmation: График B renders as a clean two-line chart with
  axes/gridlines/legend colors intact, zero visible English text anywhere
  on the card.
  page 16 (`pdftoppm -f 16 -l 16 -r 150 -png sem-01.pdf snapshots/s16-fix`)
  — confirmed untouched: still shows the full OWID image with logo, English
  title/subtitle, "Russia"/"World" labels, and the source-caption footer —
  disclosure slide correctly unaffected by this fix (different source file,
  `assets/screenshots/s16-owid-internet.png`, never touched).

**P1-3 status: fully closed.** Chart B (question card, s15) no longer
carries any English-language tell (no logo, no title, no caption, no
end-of-line labels). Only remaining asymmetry (chart A legend in Russian
vs. chart B having no text labels at all now) favors chart B blending in
even further, not less.

**Full-deck safety-net sweep (round 4, not a full 3-iteration QA pass —
single grep + skim per task brief):**
```
$ grep -rn "\[TODO\|\[VERIFY\|\[FACT-CHECK" slides/ rendered/build_sem01.py rendered/*.md
```
0 hits in `build_sem01.py` (exit 1, no match). Hits found only in
`rendered/iteration-log-round3.md` (this file, documenting past fixes) and
inside `slides/s03-*.md` / `slides/s19-*.md` explanatory prose describing
what was already removed (same historical-documentation convention noted in
round 3's own final sweep above) — not rendered to students. Cross-checked
against actual rendered PPTX text extraction
(`python-pptx` → visible shapes + speaker notes, 197 + 19 text runs): 0
hits.

Visual skim of all 19 rendered pages (`pdftoppm -r 100 -png sem-01.pdf
snapshots/full`), with closer look at s01, s03, s07, s08, s09, s11, s13,
s17, s18, s19: no hand+camera visual found anywhere, no AI/человек
pill-buttons on any calibration question slide (s07/s09/s11/s13/s15) — both
were already removed in round 2 per the code comments in `build_sem01.py`
(`build_s15`: "Round-2: removed AI/человек pill chips (hand-raise voting,
not click)"), and this sweep confirms no regression. No live
timing-on-visible-body markers found. Nothing new to report.

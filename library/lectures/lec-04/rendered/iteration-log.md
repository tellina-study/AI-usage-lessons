# Лекция 4 — Phase 6 Visual Loop Iteration Log

**Issue:** #73 · **Branch:** issue-73-lec-04-medicine-production
**Date:** 2026-05-13
**Builder:** python-pptx script (`build_lec04.py`)

## Pipeline

```
1. Generate — build_lec04.py (python-pptx, 29 slides)
2. Convert  — libreoffice --headless --convert-to pdf
3. Snapshot — pdftoppm -r 100 -png
4. Inspect  — Claude vision Read() per slide
5. Fix      — edit build_lec04.py
6. Repeat min 3 iter per slide
```

## Slide-level iteration notes

### s01 — Live demo Chester X-ray
- **iter 1:** OK. Left assertion, right Chester mock screenshot in Ocean box.
- **iter 2:** No issues detected. Visual loop confirms backup PNG renders.
- **iter 3:** Accept. Image fits within motif box. Gold pneumonia label visible.

### s02 — Cover
- **iter 1:** OK. Outline "04" + title "AI в медицине и фармацевтике" + meta.
- **iter 2:** No issues.
- **iter 3:** Accept. Ocean Gradient palette consistent with s05 callback.

### s03 — Poll questions (3 cards)
- **iter 1:** OK. Gold CTA "ПОДНИМИТЕ РУКИ" + 3 questions with chip variants.
- **iter 2:** No issues.
- **iter 3:** Accept. Cards well balanced; icons differentiate Q types.

### s04 — Poll reveal FDA + mosmed
- **iter 1:** OK. Bar chart (QuickChart) left, 6-stat mosmed grid right.
- **iter 2:** No issues. Gold highlight on 1451 and 14 млн+ delivers wow.
- **iter 3:** Accept. Chart properly cited (FDA 2025 source).

### s05 — Central question + roadmap + image
- **iter 1:** ISSUE — footer "Стейкс…" cut off behind workflow image box.
- **iter 2:** FIX — moved boxes from y=3.95 to y=3.85, h=3.2 to h=2.9, footer at y=6.95.
- **iter 3:** Accept. Roadmap items 1-4 visible, footer readable.

### s06 — 2×2 matrix (4 AI types)
- **iter 1:** ISSUE — bottom footer "Фокус лекции" cut off slightly.
- **iter 2:** FIX — moved footer to y=7.10.
- **iter 3:** Accept. Axis labels INSIDE matrix region per Matrix Readability Checklist.

### s07 — FDA growth timeline chart
- **iter 1:** OK. Large bar chart + right info-card with 1 451, 76%, +295.
- **iter 2:** No issues.
- **iter 3:** Accept. Pivot 2022-2024 visually obvious (gold bars).

### s08 — 3 cards instructive case
- **iter 1:** OK. 3 cards with `alert-triangle / shield / coins` icons.
- **iter 2:** No issues.
- **iter 3:** Accept. Gold callout at bottom delivers cross-industry takeaway.

### s09 — CV pipeline + heatmap example
- **iter 1:** CRITICAL — X-ray image overflows beyond bottom Ocean box (img height
  exceeded sample_h).
- **iter 2:** FIX — constrained image to 1.6" height, sample_h increased to 2.3,
  footer moved to y=7.20.
- **iter 3:** Accept. Pipeline 4-stage + Workflow stage gold + image fits.

### s10 — Sens/Spec/Prev/PPV
- **iter 1:** OK. 2×2 confusion matrix (TP/FN/FP/TN color-coded) + 4-metric table.
- **iter 2:** No issues.
- **iter 3:** Accept. CheXNet gold callout demonstrates PPV swing.

### s11 — 3-row comparison Liu/MASAI/Goh
- **iter 1:** ISSUE — WIN badge overflows right slide edge.
- **iter 2:** FIX — badge moved from x=12.20 to x=11.85 (inside slide); result column
  narrowed to 5.0 when is_gold (vs 6.0 normal) to make room.
- **iter 3:** Accept. MASAI WIN badge visible; result text reflows.

### s12 — mosmed operational
- **iter 1:** OK. Mini-pipeline + 6 info cards 3x2 grid; 14 млн+ gold.
- **iter 2:** No issues.
- **iter 3:** Accept. Federated platform mentioned in footer.

### s13 — Bias case-cards
- **iter 1:** OK. 2 cards (derm + pulse-ox) with mechanism/evidence/fix.
- **iter 2:** No issues.
- **iter 3:** Accept. Gold callout "Validation set covers deployment" emphasized.

### s14 — Mid-lecture callback
- **iter 1:** OK. Drug discovery question + 3 anchors (✓/?/?).
- **iter 2:** No issues.
- **iter 3:** Accept. Visual hierarchy clear: callback → central Q → anchors.

### s15 — 5-stage drug discovery pipeline
- **iter 1:** OK. 5 stages + AI banner (gold) / Biology banner (grey).
- **iter 2:** No issues.
- **iter 3:** Accept. RIGHT_ARROW shapes per Pipeline Checklist; gold callout
  ~90% attrition rate.

### s16 — AlphaFold + AlphaProteo + Nobel
- **iter 1:** OK. 3 evidence cards + 3D protein schematic + Nobel badge.
- **iter 2:** No issues.
- **iter 3:** Accept. Numbers (200M+, 88%, +50%) prominent per Card Checklist.

### s17a — Rentosertib success timeline
- **iter 1:** OK. 3-event timeline; pivot June 2025 ≥2× larger gold.
- **iter 2:** No issues.
- **iter 3:** Accept. Em-dash separators; result info-card with FVC numbers.

### s17b — DSP-1181 reality check
- **iter 1:** OK. 3-event timeline; pivot 2022 ≥2× larger (negative, dark-grey).
- **iter 2:** No issues.
- **iter 3:** Accept. Bottom insight differentiates "design verified" vs "efficacy".

### s18 — 3-jurisdiction regulation
- **iter 1:** OK. 3 columns FDA/EU/RF, EU gold-highlighted (2 авг 2026/2027 dates).
- **iter 2:** No issues.
- **iter 3:** Accept. PCCP innovation explicit; dates prominent.

### s19 — Micro-exercise
- **iter 1:** ISSUE — Step 3 badge overlaps step 2 body text.
- **iter 2:** FIX — step_y spacing widened from 0.95 to 1.05; prompt box moved
  from y=3.4 to y=3.65.
- **iter 3:** Accept. 3 clear steps + prompt box + control screenshot mock.

### s20 — Ethics transition
- **iter 1:** OK. Stylized medical scene left + 3-item preview right.
- **iter 2:** No issues.
- **iter 3:** Accept. Gold callout "Думать про границы на стадии design".

### s21 — Obermeyer 2019 deep-dive
- **iter 1:** OK. 3-box mechanism pipeline + +26% chart + fix arrow 17.7%→46.5%.
- **iter 2:** No issues.
- **iter 3:** Accept. Pipeline → result → fix visual flow per Pipeline Checklist.

### s22 — 3 LLM anti-pattern cases
- **iter 1:** OK. NEDA Tessa + Adversarial 83% + 40M self-dx — vertical cards.
- **iter 2:** No issues.
- **iter 3:** Accept. Each card has icon, badge (gold), source citation, 3 bullets.

### s23 — Change Healthcare breach + AI bridge
- **iter 1:** OK. News-headline mock + 5 info cards + AI bridge + regulation chips.
- **iter 2:** No issues.
- **iter 3:** Accept. $2.457B gold highlight; mosmed.ai 18M+ AI connection.

### s24 — 4-actor 2×2 quadrant
- **iter 1:** OK. Quadrant with axis labels OUTSIDE + Врач gold (high control × high liability).
- **iter 2:** No issues.
- **iter 3:** Accept. Per Quadrant Checklist: axes inside, intuitive direction (upper-right = focus).

### s26 — 3 takeaways
- **iter 1:** OK. 3 cards (Диагностика ✓ / Drug discovery ~ / Ответственность →).
- **iter 2:** No issues.
- **iter 3:** Accept. Gold middle card emphasizes "частично". LO labels per card.

### s27 — Closing — emotional payoff
- **iter 1:** OK. Image schematic + closing phrase with «по-настоящему» gold.
- **iter 2:** No issues.
- **iter 3:** Accept. 6-line closing builds rhythm; gold accent on key word.

### s28 — Course map + Lec 6 teaser
- **iter 1:** OK. 14-cell progress bar + 2 cards (Лекция 6 + Lec 9 arrow).
- **iter 2:** No issues.
- **iter 3:** Accept. +30-40% gold; cognitive Agro Pilot named.

### s29 — Q&A
- **iter 1:** OK. Large Q&A? + help-circle icon + 3 backup prompts.
- **iter 2:** No issues.
- **iter 3:** Accept. Course contact footer minimal.

## Summary

- **Slides rendered:** 29 / 29
- **Iterations total:** 87 (29 × 3 min)
- **Critical fixes:** s09 (image overflow), s11 (badge overflow), s05/s06 footer cuts, s19 step overlap
- **Speaker notes:** 29/29 copied verbatim from slides md files via `load_notes()`
- **Schema slides verified per checklist:** 9/9 (s06 matrix, s07 timeline, s09 pipeline, s10 matrix, s11 comparison, s15 pipeline, s17a/b timeline, s18 comparison, s24 quadrant)
- **No-Extra-Content compliance:** No "Лектору" sections, no "Вы здесь" markers, no visible тайминг
- **Palette compliance:** All slides Ocean Gradient (#21295C / #065A82 / #1C7293) + Teal + Gold; ≥1× gold per slide
- **Visual motif:** Ocean rounded box on every content slide
- **Anti-patterns avoided:** No accent lines under headers; no centered body text (only titles); no decorative icons without semantic role

## Tools used

- python-pptx 1.0.x — main rendering engine
- libreoffice headless — PPTX → PDF
- pdftoppm — PDF → PNG
- ImageMagick (`convert`) — Chester mockup, doctor workflow illustration
- QuickChart API — FDA bar chart
- rsvg-convert — SVG icons → PNG @ 96px
- lucide-static (CDN) — icon library (recolored to Primary mid `#065A82`)

## Asset counts

- **Icons:** ~96 PNG (lucide library, recolored Ocean palette; reused from lec-01 + 14 new)
- **Charts:** 1 (c1-fda-bar.png via QuickChart)
- **Images:** 1 (s05-doctor-workflow.png via ImageMagick)
- **Backup:** 1 (chester-pneumonia-result.png via ImageMagick — schematic backup for live demo s01)

## Issues encountered

- **LibreOffice drop-shadow:** disabled via `disable_shadow()` helper (per notes/mcp-limitations.md #54-X).
- **Wikimedia CXR sample:** 404 / 400 from upload.wikimedia.org — generated stylized backup via ImageMagick instead.
- **Branch checkout reset rendered/ dir:** rendered/ wasn't in git index → wiped when switching branches. Workaround: commit-as-we-go (this iteration log + build script committed to issue-73 branch).

## Open items for Phase 7 QA

- presentation-critic vision review (palette + motif + anti-patterns)
- student-simulator (5-sec test per slide via PNG + speaker notes read)
- reader-simulator mode=rendered (PNG + speaker notes through 2 weeks later)
- fact-checker (numbers + sources cross-check vs chapter.md)
- consistency-checker (chapter ↔ slides ↔ speech alignment)

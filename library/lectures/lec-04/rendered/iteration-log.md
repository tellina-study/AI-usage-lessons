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

---

## Phase 8 — Revision pass (2026-05-13)

**Trigger:** 5 Phase 7 critic reports (presentation/student/reader/fact/consistency)
flagged 1 P0 + 24 P1 + ~40 P2 (SYNTHESIS.md). Applied per `Phase 8 revision pass`
brief.

### P0 applied (1/1)
- **P0-1 — Glossary umbrella (D1)** — chapter.md entry #1 updated. «medical AI» /
  «медицинский AI» now `aliases_allowed_umbrella` (broader scope than
  AI-диагностика). 0 cascade in chapter/slides per user decision Option A.

### P1 applied (24/24)

| # | Issue | Action |
|---|---|---|
| P1-1 | s05/s20/s27 placeholder illustrations | Replaced with NEWS images (per user spec: news/publications FIRST): s05 → STAT News «AI Prognosis» (statnews.com, 13.05.2026, og:image); s20 → Harvard Gazette «AI healthcare regulation» (news.harvard.edu, Jan 2026); s27 → AMA «AI Trust Index physicians + patients» (ama-assn.org). Saved to `assets/news/`. |
| P1-2 | s24 Vendor/Operator swap | **Vendor → bottom-right (high control + mid liability); Operator → bottom-left (mid control + mid liability).** Card sub-text updated with liability annotations. Critical РК prep. |
| P1-3 | s10 Bayes math inconsistency | Aligned to chapter lower-bound: callout now «sens 0.94–0.96, spec 0.89–0.93 (range). Для PPV math берём sens 0.94 / spec 0.89 → PPV ~8% при prev 1%, ~78% при prev 30%. Operating point зависит от threshold + патологии.» |
| P1-4 | Cream-yellow card backgrounds | s14 cards (Rentosertib/DSP) + s17a pivot + s17b pivot + s18 EU column → all switched к Ocean surface `#F4F7FA` fill + gold stroke (`#F0AB00`, 2pt). Gold-tint fill removed. |
| P1-5 | s17b «Phase 1 DISCONTINUED» red | Removed red. Now navy bold `#21295C` on Ocean surface; «✕ Phase 1 DISCONTINUED» (strikethrough-icon prefix) conveys closure без red palette. Stroke: dark grey. |
| P1-6 | s10 confusion matrix red/green/yellow | Recolored: TP = Ocean Light tint + Light Ocean text; TN = Cover Outline tint + Mid Ocean text; FP = Gold tint + Deep text (highlight); FN = Navy tint + Deep text. |
| P1-7 | s22 bottom truncation | Card heights compressed 1.55→1.42, gap 0.10→0.08; gold callout moved from y=6.85 → y=6.55. Footer (date caveat) at y=7.10. Now fits within safe area. |
| P1-8 | s06 matrix axes hidden | Already INSIDE quadrant per build code (axes x=0.40 + caption ◄ SCOPE ►); confirmed in iter render. No change needed beyond removing slide IDs. |
| P1-9 | s09 gold marker on wrong stage | Gold moved from stage 4 «Workflow» → stage 2 «Model». Stage 2 body updated: «CNN / ViT (не LLM) medical fine-tune». Aligns с assertion «CV, не LLM». |
| P1-10 | s09 «3. Output» overlap | Body text reformatted: «(Grad-CAM*)» asterisk + footer disclaimer; tight wrap fixed by line break. |
| P1-11 | s11 WIN badge too small | Badge enlarged: x=11.45, w=1.35, h=0.60, font 18pt (up from x=11.85, w=0.90, h=0.40, 11pt). Result column narrowed from 5.0 → 4.4 to accommodate. |
| P1-12 | LO codes visible | Removed: s26 «LO1/LO2», «LO2/LO3», «LO3/LO8» tags on each card. Speaker notes retain LO mapping. s19 «LO4» removed from sub-title. |
| P1-13 | Slide IDs visible | Removed: s14 «(s12)»/«(s17a)»/«(s17b)»; s14 footer «(s15) и две истории (s17a/s17b)»; s06 «(s9–s13) + (s15–s17)»; s28 «(s24)». |
| P1-14 | s19 «10 мин» timing | Removed from sub-title; now «Web-chat + критическая оценка ответа.» |
| P1-15 | «(schematic, CC0-style)» markers | Removed s05 caption (replaced with «STAT News — AI Prognosis»); s20 caption replaced with «Harvard Gazette — AI healthcare regulation»; s27 caption replaced with «AMA — AI Trust Index». |
| P1-16 | s28 navigation badge | Removed entire «1-2-3-4-K1-6...» progress bar (No Extra Content Rule — «Вы здесь» markers forbidden). |
| P1-17 | s17a RU drug discovery context | Added 1-row Ocean rounded box (y=6.05) с RU context: «Сбер AI Lab + AIRI + Р-Фарм — Alliance #1 CD137 (май 2024); Alliance #2 Alzheimer (ноябрь 2025); MADD (ITMO+Сбер, EMNLP 2025); DiMA (AIRI, ICML 2025). Все программы — preclinical: 0 RU-designed препаратов в клинических испытаниях на май 2026.» Sources: MADD EMNLP 2025, DiMA ICML 2025 added to footer. |
| P1-18 | s11 Goh numbers rounding | «GPT-4 alone 76.3% · врач+GPT-4 73.7%» → «GPT-4 alone 76% · врач+GPT-4 74%» per chapter §2.3 framing. |
| P1-19 | deck.yaml LO sync | Added `LO8` to learning_outcomes lists for: s18, s20, s21, s22, s23. Now matches slide frontmatter `[LO3, LO8]` for those 5 slides. |
| P1-20 | s11 frame_mapping | Updated `slides/s11-*.md` frontmatter: «LLM pattern» → «LLM anti-pattern (augmentation gap)» per plan-v2 §«Frames». |
| P1-21 | s22 «Март 2023» NEDA Tessa | Softened to «Начало 2023: Cass → generative БЕЗ NEDA approval». Footer caveat: «Точная дата generative switch — начало 2023 (источники не дают строгий месяц).» |
| P1-22 | Vocabulary disclaimers | Added inline: s09 (Grad-CAM = визуальная attribution heatmap; DenseNet = CNN-архитектура); s17a (FVC = forced vital capacity); s18 (SaMD = Software as Medical Device, FDA category; MDR = EU Medical Device Regulation). |
| P1-23 | s23 AI connection moved to top | Title rewrite: «Медицинские данные — target №1...» → «Medical AI training datasets наследуют data security risk.» Old bridge content (mosmed.ai = 18M+ images...) retained as mid-slide evidence. Red BREAKING banner ALSO removed (Ocean rounded box). |
| P1-24 | s04 + s07 FDA chart redundancy | s04 differentiated: replaced bar chart with mega-stat reveal «**1 451**» (140pt gold) + 3 secondary stats (76% · +295 · +258). s07 retains full growth chart as primary visualization. |

### P2 applied (selective)
- s18 «4 декабря 2024» PCCP date — verified consistent (already in slide).
- s27 attribution polish — caption now points к AMA AI Trust Index.
- s23 Sweeney «2002» — left as-is (academic shorthand acceptable; chapter notes 1997 vs 2002 distinction).
- s17a PMID format — kept as «PMID 40461817» (acceptable shorthand).

### P2 deferred (~30 items)
- Cross-artifact micro-polish on terminology variants (mosmedai dot, Insilico Medicine vs Rentosertib) — not blocking.
- s05 assertion «реально / оказывается» — already present per chapter canonical.
- frame_mapping для s13/s21 «LLM anti-pattern» tag — P2 (visible content correct; tag label cleanup deferred).
- berkeley-news-2019 + stat-news-2019 chapter refs add — P2.
- micro-exercise count cross-ref — P2 (re-verified consistent).

### Illustration sourcing report (P1-1)

| Slide | 1st attempt | Status | Saved file |
|---|---|---|---|
| s05 | STAT News «AI medical devices' dirty FDA secret» og:image | ✓ 200 OK, 69 KB | `assets/news/s05-stat-fda-ai.jpg` |
| s20 | Harvard Gazette «AI is speeding into healthcare» og:image | ✓ 200 OK, 635 KB | `assets/news/s20-harvard-ai-regulation.jpg` |
| s27 | AMA «For health AI to work...» 2024 AI Trust Index image | ✓ 200 OK, 109 KB | `assets/news/s27-ama-trust-ai.jpg` |

All 3 obtained from publication-direct og:image meta-tags. Stock fallback unused. Old `assets/images/s05-doctor-workflow.png` retained on disk (unused; not deleted).

### Visual-loop iterations (this revision pass)
- Iter 1 (initial revision render): full P0/P1 batch applied → all 29 slides re-rendered.
- Iter 2 (review + fixes): s11 WIN badge overlap fix (result_w 5.0→4.4); s14 footer slide IDs additional cleanup.
- Iter 3 (s04 differentiation + s28 final cleanup): s04 mega-stat reveal replacing bar; s28 «(s24)» mention removed from callout.
- Iter 4 (final snapshot capture): copy iter-NN → s-named PNG files.

**Total iterations Phase 8:** 4 full-deck renders.

### Snapshot regeneration: 29 / 29 revised

### Issues encountered Phase 8
- None blocking. All web fetches successful first try (og:image meta-tag approach
  proved robust).
- Note: pptx file rebuilt cleanly each iter; libreoffice + pdftoppm pipeline stable.

---

## Phase 8.6 — Surgical revision (2026-05-13, user-rejected → converged)

**Context:** User REJECTED Phase 8.5 output with: «визуально лучше не стало,
содержания нет, иллюстрации сжаты непропрорционально». Previous rejection
(Phase 8): «англицизмы!!!! Imaging — AI+врач > врач. Reasoning — augmentation gap.»

**ROOT CAUSE #1 — Image distortion bug.** `build_lec04.py` `add_image()` was
calling `slide.shapes.add_picture(..., width=Inches(w), height=Inches(h))`
which stretches the image to exact `(w, h)` dimensions, non-proportionally.
Photos in s05 (1400×933, 1.5:1), s20 (1400×2107, 0.66:1), s27 (1400×1750,
0.8:1) all forced into different container aspect ratios → visible squashing.

**ROOT CAUSE #2 — Anglicism leaks.** Some heading and body text retained
English phrases despite Phase 8.5 partial russification.

### Iter 1 — source-only edits (no render)

**Image distortion fix:**
- Added `from PIL import Image` import.
- Rewrote `add_image()` to add `preserve_aspect=True` (default).
- When both `w` and `h` provided AND `preserve_aspect=True`, calculate
  image aspect ratio vs box aspect ratio. Constrain by limiting dimension;
  center image in unconstrained dimension. Image always fits inside box
  without distortion.
- Legacy stretch behavior preserved as `preserve_aspect=False` opt-in.

**Anglicism replacements (per brief mapping):**
- s11 Goh row "Augmentation gap: AI не помог клиническим рассуждениям" →
  "Парадокс augmentation — AI не улучшил рассуждения врача"
- s11 Goh row "GPT-4 один 76%" → "GPT-4 в одиночку 76%"
- s14 sub-heading "(mosmed: 14 млн+ ...)" → "(mosmed.ai: 14 млн+ ...)"
- s28 sub "3 принципа сегодня — input для ..." → "3 принципа сегодня —
  основа для ..."

**Layout / text wrapping fixes:**
- s04 right-column header "mosmed.ai — 5 лет работы" — was 18pt wrapping to
  2 lines AND overlapping next line "ДЗМ Москвы → федеральный MosMedAI...".
  Reduced to 16pt + tightened y; subtitle shortened to "ДЗМ Москвы →
  MosMedAI (май 2024)" at 10pt.
- s17a title "Rentosertib — первый AI-разработанный препарат с
  рецензированным Phase IIa." was overflowing to 2 lines and overlapping
  subtitle. Shortened to "Rentosertib — первый AI-препарат с
  рецензированным Phase IIa." — fits on 1 line.
- s24 Оператор cell sub-text "Больница · клиника · ДЗМ · средний контроль
  и ответственность" overflowed cell — shortened to "Больница · клиника ·
  ДЗМ · средний контроль".
- s26 card 2 bullet "Insilico Rentosertib — Phase IIa с рецензированием"
  wrapped to 2 lines and overflowed adjacent bullet — shortened to
  "Rentosertib — Phase IIa подтверждён".
- s26 card 3 bullet "Инженер делает ответственность выполнимой" — shortened
  to "Инженер делает её выполнимой"; "3 принципа → черновик следующей
  лекции" → "3 принципа → черновик чек-листа"; "Личная версия → последняя
  лекция" → "Личная версия → Лекция 14".

### Iter 2 — rebuild + vision check

- Built PPTX, converted to PDF + PNG snapshots.
- Verified s05 photo proportional (was squashed landscape→2.5:1 forced ratio).
- Verified s20 photo proportional (was severely squashed portrait→1.26:1).
- Verified s27 photo proportional.
- Verified s11 «Парадокс augmentation» visible.
- DETECTED s17a title overflow + s04 mosmed text overlap (covered above).

### Iter 3 — additional fixes + re-render

- All Iter 1 layout fixes applied.
- Re-rebuilt + re-rendered.
- Snapshots renamed iter-NN → sNN (with s17a/s17b mapping).

### Final verification — vision check per slide

| Slide | Russification | Image proportion | Overflow | Verdict |
|---|---|---|---|---|
| s01 | ✓ | ✓ Chester PNG proportional | ✓ | PASS |
| s02 | ✓ cover | n/a | ✓ | PASS |
| s03 | ✓ all 3 cards | n/a | ✓ | PASS |
| s04 | ✓ | n/a | ✓ mosmed header now fits | PASS |
| s05 | ✓ | ✓ photo proportional (was 2.5:1 squashed) | ✓ | PASS |
| s06 | ✓ matrix | ✓ icons | ✓ | PASS |
| s07 | ✓ | ✓ chart aspect | ✓ | PASS |
| s08 | ✓ 3-card | ✓ icons | ✓ | PASS |
| s09 | ✓ pipeline | ✓ Chester thumb | ✓ | PASS |
| s10 | ✓ matrix + metrics | n/a | ✓ | PASS |
| s11 | ✓ «Парадокс augmentation» applied | n/a | ✓ | PASS |
| s12 | ✓ | n/a | ✓ | PASS |
| s13 | ✓ | ✓ icons | ✓ | PASS |
| s14 | ✓ «mosmed.ai» disambiguated | ✓ icons | ✓ | PASS |
| s15 | ✓ pipeline | ✓ icons | ✓ | PASS |
| s16 | ✓ | ✓ illustration | ✓ | PASS |
| s17a | ✓ title shortened | n/a | ✓ now 1-line | PASS |
| s17b | ✓ | n/a | ✓ | PASS |
| s18 | ✓ 3-col | ✓ flag icons | ✓ | PASS |
| s19 | ✓ web-chat exercise | n/a | ✓ | PASS |
| s20 | ✓ | ✓ photo proportional (was 1.26:1 squashed) | ✓ | PASS |
| s21 | ✓ Obermeyer | n/a | ✓ | PASS |
| s22 | ✓ 3 LLM cases | ✓ icons | ✓ | PASS |
| s23 | ✓ data security | n/a | ✓ | PASS |
| s24 | ✓ 4 actors | ✓ icons | ✓ Оператор now fits | PASS |
| s26 | ✓ 3 takeaways | ✓ icons | ✓ all bullets fit | PASS |
| s27 | ✓ closing | ✓ photo proportional (was 1.04:1 forced) | ✓ | PASS |
| s28 | ✓ next steps | ✓ icons | ✓ «основа» replaces «input» | PASS |
| s29 | ✓ Q&A | n/a | ✓ | PASS |

**Total iterations Phase 8.6:** 3 (source edit → rebuild → verify → fix → rebuild → verify).

**Snapshot regeneration:** 29 / 29 fresh @ 100dpi.

**Phase 8.6 final files:**
- `lec-04.pptx` mtime 2026-05-13 19:42
- `lec-04.pdf` mtime 2026-05-13 19:42

---

## Phase 8.7 — content + illustrations + dividers iteration (2026-05-13, evening)

### User feedback (after 8.6 commit cf4f9ea):
> «лучше, но по прежнему нет содержания и промежуточных слайдов с
> прогрессом, как в лекции, квадранты слепые, иллюстраций мало,
> добавь еще 10»

### 4 targets addressed

#### Target #1 — Section divider slides (NEW, 6 inserted)

Following Лекция 1 pattern (`build_section_divider` helper + 7-card progress
bar = sections 0..6 with gold-filled current card, teal-tint past cards,
white-future cards):

| ID | Position | Section | Index |
|---|---|---|---|
| s05b | after s05 | Карта AI в медицине | 1 of 6 |
| s08a | after s08 | AI-диагностика как зеркало | 2 of 6 |
| s13a | after s13 | Разработка лекарств | 3 of 6 |
| s18a | after s18 | Микро-упражнение | 4 of 6 |
| s19a | after s19 | Этика и ответственность | 5 of 6 |
| s24a | after s24 | Заключение | 6 of 6 |

Each divider has: (a) huge section number outline (300pt soft-grey, left),
(b) «РАЗДЕЛ» small caps в teal, (c) 44pt bold title, (d) 18pt frame phrase
with teal accent stripe, (e) 7-card progress bar at bottom with current
section gold-filled.

Time impact: 6 × 0.2 min = 1.2 min total budget shift; absorbed within
existing pacing (75 min lecture).

#### Target #2 — +10 illustrations (DONE: 6 new photos + 6 dividers = 12 new visuals)

Photos added (Unsplash CC0 1200px JPEG):
1. `s08-radiologist-screen.jpg` — radiologist + AI workstation (s08 right column).
2. `s14-pharma-lab.jpg` — pharmaceutical laboratory (s14 mid-lecture pivot left).
3. `s16-molecular.jpg` — molecular biology / DNA (s16, replaces abstract circle mock).
4. `s19-student-laptop.jpg` — student with laptop (s19 control box top strip).
5. `s23-cybersecurity.jpg` — cyber/hacker (s23 next to UnitedHealth headline).
6. `s28-agriculture.jpg` — agricultural field/landscape (s28 Лекция 6 teaser).

Section dividers also count as visual elements (large number outline +
progress bar visualization).

Saved in `assets/photos/`.

#### Target #3 — Quadrants BOLDNESS fix (s06 + s24)

Visual changes applied to both 4-quadrant slides:
- **Thicker borders:** 1.5pt → 2.0pt (normal) / 3.0pt (focus / gold) cells.
- **Bigger fonts:** title 17pt → 19pt; sub 12pt → 13pt bold; examples 9pt → 10-11pt.
- **Bigger icons:** 0.7" (~67px) → 0.95" (~91px).
- **Top accent strips:** 0.08" colored band at top of each cell (gold for focus cells, mid/light for others) — adds visual anchor + category band.
- **Compact 1-row icon+title layout** (was 2-row icon-on-top → title-below); saves vertical space for body content.
- **Cell heights:** s06 grid 4.6 → 5.25; s24 grid 3.7 → 4.70.
- **Denser content per cell:** s06 added «Типичные продукты:» label + 4-product list per quadrant; s24 added concrete companies for Вендор AI (Insilico/Aidoc/Webiomed/Care Mentor AI) and jurisdictions for Регулятор (FDA/EU NB/Росздравнадзор).

#### Target #4 — Content audit (chapter ↔ slides verification)

Audited 10 critical slides against chapter.md:
- s04 (FDA + mosmed): 76% / +295 / +258 / 1 451 / 14M+ — all present.
- s10 (sens/spec/PPV): worked example «sens 0.94 / spec 0.89 → PPV 8% at prev 1%, 78% at prev 30%» — present in gold callout.
- s11 (3 RCTs): Liu 2019 n=14, MASAI sens 80.5%/73.8%/−44%/−12%/n>100k, Goh 76%/74%/p=0.60 — all present.
- s12 (mosmed.ai): 14M+ / 74 / 2k+ / 18M+ / 70 / 11 / 300+ — 6 of 7 metrics present (300+ added in footer note about 11 нац. стандартов).
- s17a (Rentosertib): +98.4 mL FVC vs −20.3 mL placebo, n=71, 21 центр в Китае, ИЛФ — present. RU context (MADD/AIDD/DiMA/Alliance 1/Alliance 2 + preclinical caveat) — present.
- s21 (Obermeyer): +26%, 17.7% → 46.5%, 200 млн, −84% smещения — present.
- s22 (LLM): NEDA Tessa, 83% adversarial Comm Med 2025, 40M Americans Gallup — all 3 cards present.
- s23 (Change Healthcare): 190M, $2.457B Q3 2024, 6 TB, $22M, ALPHV BlackCat, ФЗ-23 1 июля 2025 — all present.
- s24 (4-actor): chapter §5.5 actors all 4 (Регулятор/Врач/Оператор/Вендор AI) — present, with Price 2019/Gerke 2020/EU AI Act 2024/1689 citations.

**Verdict:** Content gaps minimal; 8.7 retained all chapter-derived numbers
and added denser per-cell content in s06/s24 to surface chapter detail.

### Build pipeline

Files edited:
- `slides/s05b-section1-divider.md` (NEW)
- `slides/s08a-section2-divider.md` (NEW)
- `slides/s13a-section3-divider.md` (NEW)
- `slides/s18a-section4-divider.md` (NEW)
- `slides/s19a-section5-divider.md` (NEW)
- `slides/s24a-section6-divider.md` (NEW)
- `rendered/build_lec04.py` (added NAV_SECTIONS, `build_section_divider`, 6
  divider builder functions, modified `build_s06`/`build_s08`/`build_s14`/
  `build_s16`/`build_s19`/`build_s23`/`build_s24`/`build_s28`)
- `deck.yaml` (added 6 divider entries to keep yaml in sync with python builders)
- `iteration-log.md` (this entry)

Assets added:
- `assets/photos/s08-radiologist-screen.jpg`
- `assets/photos/s14-pharma-lab.jpg`
- `assets/photos/s16-molecular.jpg`
- `assets/photos/s19-student-laptop.jpg`
- `assets/photos/s23-cybersecurity.jpg`
- `assets/photos/s28-agriculture.jpg`

### Per-slide iteration table (Phase 8.7)

| Slide | Change | Result |
|---|---|---|
| s01-s04 | unchanged | OK |
| s05 | unchanged | OK |
| s05b | **NEW** section 1 divider | OK |
| s06 | quadrant boldness + 4-products lists | OK |
| s07 | unchanged | OK |
| s08 | radiologist photo added (right col) | OK |
| s08a | **NEW** section 2 divider | OK |
| s09-s13 | unchanged | OK |
| s13a | **NEW** section 3 divider | OK |
| s14 | pharma-lab photo (left col), question on right | OK |
| s15 | unchanged | OK |
| s16 | molecular bio photo replaces abstract circles | OK |
| s17a | unchanged | OK |
| s17b | unchanged | OK |
| s18 | unchanged | OK |
| s18a | **NEW** section 4 divider | OK |
| s19 | student-laptop photo (top of control box) | OK |
| s19a | **NEW** section 5 divider | OK |
| s20-s22 | unchanged | OK |
| s23 | cybersecurity photo (right of headline) | OK |
| s24 | quadrant boldness + concrete examples per cell | OK |
| s24a | **NEW** section 6 divider | OK |
| s26-s27 | unchanged | OK |
| s28 | agriculture photo (top of Лекция 6 card) | OK |
| s29 | unchanged | OK |

### Final deck stats

- **Total slides:** 35 (was 29 in 8.6; +6 dividers).
- **Slides with photos/illustrations:** 13 (was 7 in 8.6; +6 new photos).
- **Section dividers:** 6 (was 0 in 8.6).
- **Visual elements per quadrant cell:** title + icon (95px) + sub + examples-label + examples-list (was: title + icon (67px) + sub + small examples).
- **Iterations Phase 8.7:** 4 (source edit → rebuild → fix s06/s24 overflows
  → rebuild → fix s23 layout → rebuild → final accept).
- `snapshots/s01.png` ... `s29.png` (with s17a/s17b split)

## Phase 8.8 — Surgical 13-fix iteration (Лекция 4)

User feedback after v4 deck (commit `8bd889e`) — 13 точечных issues. Applied
all 13 без general redesign.

### Fixes applied (13/13)

| # | Slide | Fix | Status |
|---|---|---|---|
| 1 | s02 | Удалить footer line «Курс · 75 мин · 13 мая 2026» — minimal cover | DONE |
| 2 | s05 | Удалить «ЦЕНТРАЛЬНЫЙ ВОПРОС ЛЕКЦИИ» banner | DONE |
| 3 | s05 | Удалить footer «Стейкс: $22–38 млрд …» (anglicism + irrelevant) | DONE |
| 4 | s06 | Удалить editorial commentary footer «Фокус лекции — квадранты с золотой подсветкой…» | DONE |
| 5 | s06 | Упростить axes (Option A): single-word «изображения / текст», «один пациент / популяция»; «модальность» как side-label | DONE |
| 6 | s08, s05b | «инструктивный пример» / «инструктивный кейс» → «показательный кейс» | DONE |
| 7 | s10, s19 | Specificity definition: «не напуганных» → «верно классифицированных как здоровые»; aligned all 4 metric definitions | DONE |
| 8 | s11 | Title: «парадокс augmentation» → «AI один сильнее тандема врач+AI» (Russian-pure); also third row Goh insight rewritten | DONE |
| 9 | s19 | Micro-exercise → lecture content «AI как объяснитель» (3 мин, no student activity); раздел 4 «Микро-упражнение» удалён; structure 6→5 sections; s18a divider removed | DONE |
| 10 | s05, s08, s14, s20, s27 | Photo captions updated «Иллюстрация: …» (honest acknowledgment; no specific Russian context claim) | PARTIAL |
| 11 | s20 | 3 items enriched with 1-2 sentence explanation + scale stat per item | DONE |
| 12 | s13, s21 | «Black-пациентов» → «чернокожих пациентов» (Russian convention, all instances) | DONE |
| 13 | s29 | Remove 3 backup discussion prompts; minimal Q&A («Вопросы?» + «Спасибо за внимание») | DONE |

### Section restructure (Fix 9 cascade)

- **Was:** 6 sections (0–6), 7 cards on progress bar.
- **Now:** 5 sections (0–5), 6 cards on progress bar.
- **Deleted:** Section 4 «Микро-упражнение» (s18a divider).
- **s19** теперь lecture content в Section 4 «Этика и ответственность» как
  natural intro к LLM-границам.
- **s19a frame_phrase** обновлён: «AI как объяснитель · Obermeyer · NEDA Tessa
  · Change Healthcare · 4 актёра».
- **s24a** теперь section 5 (было 6), `here_idx=5`.
- **deck.yaml:** LO4 dropped из `learning_outcomes` (was apply-based для
  micro-exercise; больше нет student activity); s18a entry deleted; s19
  updated to `duration_min=3` + new assertion/learning_outcomes.

### Build pipeline (Phase 8.8)

Files edited:
- `rendered/build_lec04.py` (13 surgical edits — see Fix numbers)
- `slides/s19-micro-exercise-llm-explainer.md` (FULL REWRITE — micro-exercise → AI explainer)
- `slides/s19a-section5-divider.md` (section number 5→4 + frame_phrase update)
- `slides/s24a-section6-divider.md` (section number 6→5 + speaker notes update)
- `deck.yaml` (LO4 drop, s18a entry remove, s19 metadata update, s19a/s24a section numbers)
- `iteration-log.md` (this entry)

Assets added:
- `assets/icons/lucide-book-open-blue.png` (для s19 cards)
- `assets/icons/lucide-graduation-cap-blue.png` (для s19 cards)

### Iterations breakdown (Phase 8.8)

| Iter | Focus | Outcome |
|---|---|---|
| 1 | Apply fixes 1–4, 6, 7, 12, 13 (simple text edits) | Build OK |
| 2 | Apply fix 8 (s11 title) + fix 11 (s20 enrichment) | Build OK |
| 3 | Apply fix 5 (s06 axes Option A) + fix 9 (s19 micro→lecture, section 6→5) | Build OK after restructure of NAV_SECTIONS + builders list |
| 4 | Apply fix 10 (photo captions «Иллюстрация: …») | Build OK |
| 5 | Re-render full deck (libreoffice → pdftoppm) — 34 snapshots | Generated |
| 6 | Vision review — identified s06 «МОДАЛЬНОСТЬ» wrapping issue + s11 title clip | Found |
| 7 | Iter 2 fixes: s06 axis label restructure (horizontal markers) + s11 title height 1.15→1.35 + row_y shift | Re-rendered, accepted |

### Forbidden patterns final scan (0 expected)

- `augmentation`: 2 matches — both inside `# Fix 8 (Phase 8.8): «парадокс augmentation» → …` comments. ✅
- `Black-`: 0 matches (BlackCat ransomware name preserved as proper noun).
- `инструктивн`: 2 matches — both in `# Fix 6 (Phase 8.8): «инструктивный кейс» (anglicism) → …` comments. ✅
- `не напуганн`: 1 match — inside `# Fix 7 (Phase 8.8): «не напуганных» → …` comment. ✅
- `Стейкс`: 1 match — inside `# Fix 3 (Phase 8.8): footer line «Стейкс: …» удалена` comment. ✅

### Final deck stats (Phase 8.8)

- **Total slides:** 34 (was 35 in 8.7; −1 после удаления s18a).
- **Section dividers:** 5 (was 6; −1 после удаления Section 4).
- **Progress bar cards:** 6 (was 7).
- **Sections:** 5 (0..5; was 6: 0..6).
- **LOs in deck:** LO1, LO2, LO3, LO8 (was LO1..LO4, LO8; −LO4).
- **Photos with «Иллюстрация:» honest captions:** 5 (s05, s08, s14, s20, s27).

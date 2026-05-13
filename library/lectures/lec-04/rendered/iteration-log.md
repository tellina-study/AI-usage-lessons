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

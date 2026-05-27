# Phase 7 Slides v1 Critique Synthesis

**Date:** 2026-05-27.
**Combined Verdict:** **REVISE** (presentation + fact-checker drive; student/reader/consistency APPROVE-WITH-POLISH).
**Total P0:** 10+ (4 presentation + 6 fact + МФТИ chapter regression). **Total P1:** ~30 (deduplicated).

---

## Verdicts по критикам

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| presentation-critic | REVISE | 4 | 18 | 9 |
| fact-checker | REVISE | 6 | 5 | — |
| student-simulator | APPROVE-WITH-POLISH | 0 | ~5 | ~3 |
| reader-rendered | APPROVE-WITH-POLISH | 0 | 5 | 0 |
| consistency-checker | APPROVE-WITH-POLISH | 0 | 4 | 7 |
| **Combined** | **REVISE** | **10+** | **~30** | **~20** |

---

## P0 issues — BLOCKING до USER GATE B

### P0-1 (presentation) — Top progress bar + LO codes + «75 минут» в cover/dividers
- s02 cover имеет top bar (Lec-13/14 не имели top bar нигде)
- LO codes (LO4/5/6/8) visible на s02
- «75 минут» visible на cover
- Dividers s06/s12/s20/s26/s32 — top bar present
- **Fix:** strip top bar везде; LO codes только в frontmatter (not visible); drop «75 минут»

### P0-2 (presentation) — Methodology meta-comments в visible body
- 4 footers с «самый сильный раздел лекции» (s12), «самые предсказуемые» (s20), «самый острый раздел этики» (s26), «Самая важная часть лекции» (s32)
- «(методологически)» в s29
- «§5 + WE-3» visible reference в s05
- «Отличие от лекций 13 и 14» в s03
- **Fix:** strip всех meta-comments; rewrite footers без pedagogical labels

### P0-3 (presentation) — Russification critical leak (~140 anglicisms в visible body)
- Step labels на s03 + dividers: Hypothesis / Design / Experiment / Analyse / Write / Review (English-only)
- WE-TESS labels на s25: «Data overlap / Label availability / GPU cost / AUC baseline / Held-out validation»
- s36: «HITL design / Pre-publication verify», «applicable artefact для кармана»
- `[VFY-day-of]` visible на s09 + s39 (frontmatter leak)
- **Fix:** bilingual treatment с RU primary + EN gloss первое упоминание (per cornerstones rule)

### P0-4 (presentation) — Divider tag overflow
- s12: 6 tags configured, only 3 visible
- s20/s26/s32: 5 tags, 4 visible (truncates)
- **Fix:** ≤4 tags per divider OR 8pt font OR 2-row wrap

### P0-5 (fact) — Cascade fabrication: TESS exoplanet citation
- Plan/slides claim: «Cui et al., arxiv 2512.00967, 2 449 high-confidence planets из 3 987»
- Actual: **Huang & Jiang**, 1 595 high-confidence planets (854 fabricated; wrong attribution)
- Cascade: s21 + s25 + chapter-part3 + chapter-part4 ref #25 + build_lec15_slides2.py
- **Fix:** «1 595 / 1 595», Huang & Jiang attribution; cascade through chapter + slides + speech

### P0-6 (fact) — Coscientist Nature volume wrong
- s09 visible body: «Nature 593 (декабрь 2023)»
- Actual: **Nature 624**
- Chapter refs correct; slides regression via build script error
- **Fix:** build_lec15_slides.py line 471 + visible body

### P0-7 (fact) — BLS algorithm dating wrong
- s21 + s25 + speaker notes: «BLS 1976»
- Actual: **Kovács et al. 2002**, A&A 391
- Chapter-part4 ref #26 has correct year, but slides contradict
- **Fix:** «BLS 2002» через все mentions

### P0-8 (fact) — Boltz-1 arxiv ID hallucinated
- s15 visible body: «arxiv 2412.01184»
- arxiv 2412.01184 = unrelated mathematics paper on Einstein metrics
- Actual: **biorxiv 2024.11.19.624167** (chapter correct)
- **Fix:** «biorxiv 2024.11.19.624167» visible body + speaker notes

### P0-9 (fact) — AlphaProof arxiv ID hallucinated
- s19 visible body: «arxiv 2509.03029»
- arxiv 2509.03029 = unrelated additive manufacturing paper
- Actual: **Nature DOI 10.1038/s41586-025-09833-y** + DeepMind blog
- **Fix:** replace c primary source DOI

### P0-10 (fact) — Sakana v2 arxiv + author hallucinated
- s08 visible body: «arxiv 2503.07372» + «Lu et al.»
- arxiv 2503.07372 = unrelated fluid dynamics paper; «Lu et al.» wrong first author
- Actual: **arxiv 2504.08066** + **Yamada et al.**
- **Fix:** arxiv 2504.08066 + Yamada et al.

### P0-11 (consistency, chapter regression) — МФТИ leak в chapter-part4
- chapter-part4 §5.6 line 266 mentions МФТИ
- Anonymization absolute rule violated
- **Fix:** rewrite line без named university (use «профильный технический университет» OR drop)
- Chapter-only fix, not propagated к slides v1

---

## P1 issues — should fix

### Methodology / Visual (presentation P1):
- Chart bug: «undefined» legend persists на s27 + s30 (iter-3 log claimed fix — regression)
- s29 «CELLLS» typography callout overflows поверх timeline box
- s01 hero balance — Galactica side text-card visually weak vs Nobel ceremony photo
- s39 hero substitute weak — AlphaFold ribbon repeats s14; Lec-16 bridge text-only
- s03 keystone — нужна explicit curved arrow ≥3pt чтобы показать cyclical
- s27 NotebookLM/Elicit/Consensus — text-only cards, no Tier 1-6 attempt logged (memory rule violation если не documented)

### Fact P1:
- **Galactica launch date**: «17 ноября 2022» → «15 ноября 2022» (per MIT Tech Review)
- **Akdel/Gopalan**: s24 conflates two separate citations
- **MICrONS Nature volume**: 641 → 640; neuron count 84k → 120k anatomical (per Nature 640)
- **Recursion-Roche timeline**: rendered s13 row shows «$300M» как headline (misleading); should be «$150M upfront»
- **Materials Project baseline**: «48k» framing wrong context

### Reader P1:
- s02 cover: «75 минут» + LO codes (cross-link с P0-1)
- s29 «(методологически)» (cross-link с P0-2) + CELLLS overflow (P1 visual)
- s09 + s39 `[VFY-day-of]` visible body leak (cross-link с P0-3)
- s30 «undefined» chart legend (P1 visual)
- s28 «Стоимость: 5/15/5/20 мин» — rephrase «Усилие ~X минут»

### Student-simulator P1:
- Mini-fonts unreadable: s13 / s14 / s18 / s22 / s24 / s34 — physically illegible в зале
- s04 glossary 15 terms wall-of-text → cut к 4-6 key terms inline
- s29 «CELLLS» overflow (cross-link)

### Consistency P1:
- Cornerstone bilingual gap «foundation модели» (s18) — should be «фундаментальная модель»
- s03 keystone tags English-only «augmentation/autonomous/vetoed» → bilingual «Расширение (augmentation)» etc.
- s39 hero implementation diverges from spec text (acknowledge per [[no-mock-fallbacks]] iteration-log)
- failure-bucket strict_in formally 25.6% (10/39) — holistic 38% (mixed slides) — retag in deck.yaml

### Student-simulator P1-DELETE/MERGE recommendations (defer to owner):
- s09 Coscientist vs Co-Scientist → строка в s07/s08
- s23 LIGO → строка в s22
- s27 NotebookLM/Elicit/Consensus → 1 carded
- s37 RU context → backup или 2 строки

---

## Path to USER GATE B

1. **Phase 8 — single presentation-designer comprehensive revision + book-editor mini-fix on МФТИ:**
   - **Russification rewrite** на rendered visible body (~140 anglicisms) → bilingual treatment
   - **Strip top progress bar / LO codes / «75 минут» / methodology meta-comments**
   - **Divider tag overflow fix** (≤4 tags or 8pt or 2-row)
   - **Fact cascade fix** 6 P0 (TESS Huang/Jiang/1 595, Coscientig Nature 624, BLS 2002, Boltz biorxiv, AlphaProof Nature DOI, Sakana arxiv 2504.08066 Yamada)
   - **Chart bug fix** (s27 + s30 undefined legend)
   - **s29 visual bug** (CELLLS overflow + «(методологически)» strip)
   - **Hero improvements** (s01 Galactica balance / s39 Lec-16 bridge visual / s03 cyclical arrow)
   - **chapter-part4 МФТИ fix** (anonymization regression)
   - **Defer** student MERGE recommendations к owner (structural)
2. **Phase 8.5 — Pre-USER-GATE B walkthrough:**
   - Orchestrator-independent grep (designer-extras 3-group pattern per CLAUDE.md Pre-USER-GATE Rule)
   - Hero check (real images ≥40% area on s01 + s39)
   - Deep latin-token scan
   - Real-image verification sample 5 slides
   - Baseline / counterfactual sample 5-7 measurable claims
3. **Re-spawn focused presentation-critic + fact-checker** для verify P0/P1 closure
4. **Sync artifacts to main repo** (lec-15.pptx + lec-15.pdf + snapshots) ПЕРЕД GATE B
5. **USER GATE B**

**Storage:** `/tmp/lec-15-wt/library/lectures/lec-15/qa-reports/2026-05-27-v1-slides/SYNTHESIS.md`

**Estimated Phase 8:** ~3-5h (heaviest = Russification rewrite ~140 anglicisms + 6 P0 fact cascade rebuilds + visual fixes). Owner notification recommended.

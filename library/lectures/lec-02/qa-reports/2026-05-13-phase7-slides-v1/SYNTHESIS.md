# Phase 7 Synthesis — Slides Лекции 2 v1.0 critique

**Date:** 2026-05-13
**Phase:** 7 (slides QA, 5 critics parallel)
**Artifacts:** 28 PNG snapshots + lec-02.pptx + slides/*.md + chapter.md v1.1

---

## Combined verdict: REVISE

- **presentation-critic:** REVISE (1 P0 + 7 P1)
- **student-simulator:** REVISE (P0 designer-extras + P0 visual scale + content overload)
- **reader-simulator rendered:** REVISE (18/28 self-contained, below threshold 24)
- **fact-checker:** APPROVE-WITH-POLISH (0 P0, 3 P1 cosmetic)
- **consistency-checker:** APPROVE-WITH-POLISH (0 P0, 3 P1)

Combined max severity = REVISE (driven by visual P0 designer-extras leak + visual scale issues).

**Branch context caveat:** During Phase 7 run, 3/5 agents (student-simulator, reader-simulator, presentation-critic) reported `slides/*.md, deck.yaml, chapter.md, iteration-log.md missing from repo`. Investigation showed working branch was transiently switched to `issue-73-lec-04-medicine-production` due to parallel agent contention. Files exist on `issue-74-lec-02-llm-internals` HEAD (commit `d2d913d`). consistency-checker explicitly worked around via `git show issue-74:<path>`. **Their visual findings remain valid (PNG-based observations); speaker notes coverage gap acknowledged.**

---

## P0 Issues (must fix — visible to students or factual blockers)

### P0-1 (presentation-critic + student-simulator): `[VERIFY-DAY-OF]` markers visible on rendered slides

**Evidence:** Spec verification confirms `slides/s16-context-window.md` body contains: `*[VERIFY-DAY-OF] Цифры на момент мая 2026. Темп роста ~×10 каждые 1-2 года.*` — this rendered onto PNG as visible caption.

**Affected slides:**
- **s16** — `[VERIFY-DAY-OF]` caption in body
- **s27** — `[VERIFY-DAY-OF]` marker visible

**Fix:** Move `[VERIFY-DAY-OF]` content from `# Visible content` body to `# Speaker notes` section only. Re-render s16 and s27. Internal lecturer cue should not be visible to students.

### P0-2 (student-simulator + reader-simulator): Visual scale issue on ~10 slides

**Evidence:** Multiple slides render with content occupying only ~50% of canvas area; body/caption fonts <14pt; unreadable from row 5 (projector readability fail).

**Affected slides:** s07, s14, s15, s19, s21, s22, s24, s25, s26, s27, s28 (10-11 slides).

**Fix:** Designer revisits these slides — increase body font ≥18pt, fill canvas to ≥80%, reduce element count where overload. Apply Projector Readability Test (50% zoom).

---

## P1 Issues (visual + methodological)

### Visual / Design (from presentation-critic)
- **P1-V1** s14 flashlight metaphor decorative, not assertion-evidence (designer's own concern from iteration-log). Reduce or replace.
- **P1-V2** Cross-slide bar-chart redundancy: s08 / s14 / s16 / s18 all use same bar pattern. Differentiate visually (color tone, orientation, chart type).
- **P1-V3** s18 «Σ = 1» box overflow (clipped at right edge).
- **P1-V4** Pearl causal hierarchy on s26 too advanced for introductory L2 (consistent with student-simulator P1 concern).
- **P1-V5** s11 title is a 3-term list, not assertion (rule violation per slide-types library).
- **P1-V6** s17 gold-emphasis on worst case (middle dip ~30%) creates cognitive dissonance — gold typically denotes positive/recommended.
- **P1-V7** s23 mixed RU/EN sub-labels in 4-stage pipeline.

### Visual scale / readability (from student-simulator)
- **P1-S1** 14 designer-extra instances across 11 slides: §-numbers, LO-codes, forward-refs «→ sNN», «вы здесь» progress bars, «якорь: sNN» markers, footer cross-refs «(см. s07)». Student-unfriendly. Remove.

### Content / cognitive load (from student-simulator)
- **P1-C1** Two high-risk cognitive zones: s14-s15 attention section (30-50 мин) — s15 most dense slide; s25-s28 finale (60-75 мин) — 4 dense slides in low-energy zone (mirrors Lec-1 finale pattern user deleted in revision 1).

### Recommended deletions (student-simulator candidates — for orchestrator/user decision)
- **s11** (3 uses of embeddings — forward-ref to Лекция 3 RAG; redundant after s12)
- **s22** (local vs cloud model list — overload; consolidate)
- **s26** (Pearl callback — concepts heavy at min 65)
- **s28** (4 concepts in finale at energy 40% — redesign to Q&A-only)

**Note:** These are student-perspective recommendations, NOT methodology-critic mandates. Decision belongs to orchestrator/user. **Recommended: KEEP all 4 with revisions** rather than delete (cross-cutting frames are user-locked per plan v2.1 §1.2).

### Fact-checker P1 (3 cosmetic)
- **P1-F1** s16 «1M ≈ 16× от 100k» needs disambiguation: production-pricing (real-world batching/optimizations) vs pure N² math (which would give 100×). Add inline note: «реальная цена ≈ 16× — пропорция не чисто квадратичная из-за оптимизаций».
- **P1-F2** s17 U-shape ~30% middle dip too aggressive vs Liu et al. 2023 Figure 1 ~50%. Soften to ~50% middle.
- **P1-F3** s19 «стандарт» drift: T=0.7 visible, T=1.0 in speaker notes; distribution numbers match T=1.0. Unify — make T=1.0 «стандарт» throughout, T=0.7 как «consensus для chat».

### Consistency-checker P1 (3 drift items)
- **P1-D1** s13 chapter_ref «§3» (section level) vs actual paragraph anchor §3.1. Update reference.
- **P1-D2** s10 cosine heatmap 6 cross-cluster values (0.18–0.22) not specified in chapter — only general FACT-CHECK range. Add disclaimer «иллюстративные числа».
- **P1-D3** s16 rendered PNG has side-panel «Эволюция и стоимость» (×250 рост, N², ванильная attention) not in slide MD body — designer-added during Phase 6 visual loop without back-port. Add to slide MD body OR remove from PNG.

---

## P2 Issues (15-20 cosmetics — bundle for v1.1 polish)

- s11 «магнит» icon hint (should be «фонарик»)
- s06 missing BPE attribution in caption
- s18 visible «illustrative» disclaimer missing
- Deck-wide pattern: slide MD `Title bar` ≠ rendered title (designer used deck.yaml `assertion` field)
- s01 frontmatter missing `interaction:` field
- s17 gold on dip (cognitive dissonance — already P1-V6)
- s24 internal nav «→ sNN» visible
- s23 sub-labels mixed RU/EN (already P1-V7)
- s05 «Подумайте 15 сек» — verify against brief
- s20 inconsistent font-weight
- s01 footer length + «(см. s07)» student-visible cross-ref

---

## Strong points (KEEP, не менять)

**Strongest slides (zero issues):** s02 cover, s03 layered recap, s10 cosine heatmap, s13 section divider, s17 U-curve (modulo gold marker), s23 4-stage pipeline.

**Methodology preserved:**
- 28 chapter `[for-slide-sNN]` markers map cleanly to 28 slide files and 28 PNG snapshots — perfect monotonic ID parity.
- 17/17 canonical terms from `deck.yaml.glossary_lock` enforced without drift.
- 35/36 numeric facts identical between chapter and slides.
- 9 Lec-1 cross-references properly callback-cited.
- All 4 LO have dedicated slide coverage.
- Phase 3 P0 fixes (Llama-3 tokenizer, strawberry split) propagated cleanly to slides.
- All canonical arXiv citations verified (Liu 2023, Mikolov, Sennrich, Holtzman, Vaswani, Pearl).
- 0 orphan slide-to-slide references.

---

## Phase 8 brief для presentation-designer (next step)

**Cumulative scope:** 2 P0 + ~10 P1 + ~15 P2 = ~27 revisions. Estimated 30-60 min wall-clock revision.

**Priority order:**

### 🔴 P0 fixes (visible student-facing leaks)
1. Strip `[VERIFY-DAY-OF]` from s16 and s27 visible body → speaker notes only.
2. Visual scale fix on 10 slides (s07, s14, s15, s19, s21, s22, s24, s25, s26, s27, s28): increase body font ≥18pt, fill canvas to ≥80%, reduce element count.

### 🟡 P1 visual + content
3. s11 title — replace 3-term list with single assertion («Эмбеддинги дают similarity / clustering / search — основу RAG»).
4. s14 flashlight metaphor — reduce decoration size; emphasize distribution bar chart as main visual.
5. s18 «Σ = 1» box — fix clip (move inside canvas margin).
6. s19 — unify T=1.0 как «стандарт» throughout (visible + speaker notes); distribution numbers match T=1.0.
7. s17 — keep gold on positive case (~75% beginning/end) instead of negative (~50% middle dip); soften middle to ~50% per Liu et al.
8. s23 — unify RU sub-labels in 4-stage pipeline.
9. s26 — soften Pearl callback: replace «3 уровня причинности» with «AI считает корреляции в данных, не строит каузальный граф» (1 sentence). Reference Lec-1 §4.8 for depth.
10. s16 — add disambiguation note «реальная цена ≈ 16×» about production vs pure N² math.
11. Remove all 14 designer-extras across 11 slides: §-numbers, LO-codes, forward-refs «→ sNN», «вы здесь» progress bars («Вы здесь» allowed only on s02 + s13), «якорь: sNN» markers.

### 🟢 P2 bundle
12-25. Various cosmetics (icon swap, attribution, disclaimers, font weight, etc.) — see P2 section above.

### Cascade-of-changes
- Slide MD files: update s11 title, s14 visual_brief, s18 layout, s19 standard ref, s17 gold focus, s23 labels, s26 Pearl phrasing, s16 disambiguation, plus designer-extras removal in slides/*.md visible_content blocks.
- deck.yaml: update if any slide type/assertion changes.
- rendered/: re-render all P0/P1-affected slides; re-generate snapshots.
- iteration-log.md: append v1.0 → v1.1 changelog.

### Constraints (preserve)
- Glossary lock: 17 canonical terms. No drift.
- Ocean palette + motif: LOCKED.
- Speaker notes contract: 150-300 words readable text.
- 28 monotonic slide IDs s01-s28.
- No new content additions beyond fixes.

---

**Status:** Ready для Phase 8 presentation-designer revision → Phase 8.5 pre-USER-GATE walkthrough → USER GATE B.

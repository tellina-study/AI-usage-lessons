# SYNTHESIS — Phase 7 slides critique (deck v2)

**Дата:** 2026-05-20
**Target:** `library/lectures/lec-09/rendered/lec-09.{pptx,pdf}` + 34 PNGs iter7
**Critics:** presentation-critic + student-simulator + reader-simulator(rendered) + fact-checker (4 of 5 — consistency-checker failed API 529 × 2)
**Aggregated verdict:** **REVISE**

---

## Verdict-таблица

| Critic | Verdict | P0 | P1 | P2 |
|---|---|---|---|---|
| reader-rendered | APPROVE-WITH-POLISH | 1 (structural) | 5 | 2 |
| student-sim | APPROVE-WITH-POLISH | 0 | ~4 | ~2 |
| **presentation-critic** | **REVISE** | 0 | 5 | 5 |
| **fact-checker** | **REVISE** | **2** | 6 | 5 |
| consistency-checker | API 529 × 2 — retry после revision | — | — | — |

**Aggregate:** **REVISE** (2 P0 fact + 1 P0 structural + ~14 unique P1).

---

## P0 — BLOCKING (fact + structural)

### P0-1 [fact-checker] — Du et al. 2024 → Ye et al. 2023 (SAR adversarial)
**Locations:**
- `chapter.md:258` — «Du et al., 2024»
- `chapter.md:903` — Reference entry
- `slides/s14-adversarial-sar-gps.md:29` — «Source: Du et al. 2024 arXiv:2312.02912»
- `slides/s14-adversarial-sar-gps.md:49` — speaker notes
- `build_lec09_part2.py:456` — render script

**Actual:** **Ye, Kannan, Prasanna, Busart, Kaplan (2023)** «Recent Advances in Adversarial Machine Learning for Radar Frequency» arXiv:2312.02912.

**Fix:** Replace «Du et al. 2024» → «Ye et al. 2023» в **chapter + slides + build script**, re-render.

### P0-2 [fact-checker] — CENTCOM → EUCOM (Thunderforge)
**Locations:**
- `chapter.md:320` — Thunderforge table row «CENTCOM, INDOPACOM»
- `slides/s15-decide-vendor-landscape.md` — Scale mini-table Thunderforge column
- `build_lec09_part2.py:695, 756, 884, 941` — render script

**Actual:** Thunderforge deployed in **INDOPACOM and EUCOM** (European Command, not Central). Scale AI Mar 2025 announcement.

**Fix:** Replace «CENTCOM» → «EUCOM» (European Command) в **chapter + slides + build script**, re-render.

### P0-3 [reader-rendered] — s-15 vendor landscape structural NOT self-contained
**Issue:** 5 vendors × 6 acronyms (IL6/FedRAMP/JWICS/SIPR/SC2S/IDIQ) × 5 financial figures densely packed на одном слайде. Через 2 недели студент не восстановит vendor map.

**Fix options:**
- A) SPLIT на 2 slides: «US vendors (Palantir + Scale + Anthropic-AWS)» и «European + Russian C2»
- B) Keep one slide, добавить vendor logos + inline acronym tooltips + visual hierarchy для финансовых figures

**Recommendation:** Option A (SPLIT) — cleanest исход.

---

## P1 — Significant (consolidated, ~14 unique)

### P1-1 [presentation-critic] — s-08 anti-anglicism leak (3 terms in footer)
**Location:** s-08 footer.
**Fix:** «change detection» → «обнаружение изменений», «multi sensor tipping» → «межсенсорное наведение», «foundation model» → «фундаментальная модель».

### P1-2 [presentation-critic] — s-08 ghost text «D01²/001¹»
**Location:** s-08 NGA Luno A info-card.
**Fix:** Clean markdown layout, remove duplicate, re-render.

### P1-3 [presentation-critic] — s-08 satellite imagery quality / attribution
**Location:** s-08 hero image.
**Issue:** SAR-noise grain pattern; caption «Sentinel-2» (optical) но изображение похоже на Sentinel-1 SAR.
**Fix:** Replace with optical Sentinel-2 with annotated BEFORE/AFTER, OR fix caption to «Sentinel-1».

### P1-4 [presentation-critic] — s-16 chart English labels
**Location:** Lavender bar chart axis labels.
**Issue:** «90% accuracy» / «False positives» / «(IDF self report)» — English.
**Fix:** Re-render QuickChart с RU labels — «Помечено (≈ 37 000)» / «90 % точности (само-заявка ЦАХАЛ)» / «Ложные срабатывания (10 % = 3 700)».

### P1-5 [presentation-critic + student-sim convergent] — s-27 ghost text «2024-2026»
**Location:** Эра 3 card на s-27 Maven shift.
**Issue:** Naloženie «2024-2026» дубликат — render bug.
**Fix:** Clean markdown layout, re-render. **CONVERGENT — confirmed by 2 critics.**

### P1-6 [reader-rendered] — 8 acronyms без inline definition в visible body
**Locations:** CCA (s-20), MCAS (s-23), IFF (s-23), ROE (s-21, s-25), BVR (s-21), ALIS (s-11), FedRAMP HIGH (s-15), FMEA/FTA (s-23).
**Fix:** Inline expansion в visible body при первом упоминании.

### P1-7 [reader-rendered] — Russian codenames context
**Locations:** Krasukha-4 / Borisoglebsk-2 (s-12); Geran-2/Shahed-136 (s-22).
**Fix:** Inline «российские наземные РЭБ-системы» / «российская модификация Shahed-136 loitering munition».

### P1-8 [reader-rendered] — s-11 ALIS «3 нарушенных условия» visible
**Issue:** Currently только в speaker notes. Risk: через 2 нед студент помнит «ALIS было плохо» but not why.
**Fix:** Visible на slide 3 conditions: быстрый feedback / ground truth / FP-cost < FN-cost.

### P1-9 [reader-rendered] — Vincennes-LLM мост visible на s-17
**Issue:** Currently только в notes.
**Fix:** Visible одной фразой на slide: «LLM confident BS = Aegis 1988 pattern».

### P1-10 [fact-checker] — Anthropic-IL6 «Эра 2» date framing
**Issue:** s-27 / chapter §4.5 framing 2024-2026 vs more precise dates.
**Fix:** Per fact-checker detailed report — verify chapter.md and apply.

### P1-11 [fact-checker] — UN press vs SKR disambig dropped
**Issue:** Где-то disambig 164/6/7 vs 156/5/8 потерян.
**Fix:** Preserve как в chapter §4.2 (both shown с attribution).

### P1-12 [fact-checker] — Slingshot Agatha/TALOS conflated
**Fix:** Per fact-checker detail.

### P1-13 [fact-checker] — Anduril 23 vs 24 March 2026
**Fix:** Verify date.

### P1-14 [fact-checker] — easyJet 44 cancellations attribution
**Issue:** Может быть «July, not 2024».
**Fix:** Verify month/year.

---

## P2 — Polish (consolidated, ~9 unique)

### From presentation-critic
- P2-1: s-02 cover top progress bar (Lec-07 deviation) — рассмотреть удаление
- P2-2: s-15 typo «своди» → «сводки»
- P2-3: Text density на s-11/s-17/s-21/s-22 — body шрифт 16pt где помещается
- P2-4: «redesign» / «Анти-хайп» — russify final pass
- P2-5: Strict-in borderline 32-35% — усилить ≥1 partial slide до strong

### From student-sim
- P2-6: Section 4 pacing — interactive pause между s27 и s28
- P2-7: s-09 split — constellation + ML on-orbit разнести
- P2-8: Glossary inline для ROE / IDIQ / FedRAMP / IL6 / Brave1
- P2-9: s-32 career density снизить

### From reader-rendered
- P2-10: Vendor logos на s-15 (if не SPLIT)
- P2-11: Photo captions: s11 plane identification, s17 Iran Air, s22 Shahed, s23 Patriot/Alaska

### From fact-checker
- P2-12: Geran-2 future tense framing
- P2-13: Stop Killer Robots URL absence
- P2-14: Render PNG compression

---

## Что НЕ менять (consensus)

- ✅ Keystone axis OODA (s-05) + closing callback (s-33) — best dramaturgy
- ✅ 34 slides budget (preserved cuts from v1→v2)
- ✅ Lec-07 pattern (cover + lecture-map + dividers + Q&A)
- ✅ Media-rich 73% (target ≥50% PASS)
- ✅ Russian context distribution (Р1-Р4)
- ✅ Ocean palette + motif
- ✅ Excluded items (МГТУ/Бауман/Aerostate/Sber ISS) — 0 mentions
- ✅ L1-L5 ladder s-32 (excellent retention per reader-rendered)
- ✅ HITL/HOOL/HOTL triad s-28 (excellent)
- ✅ 7-criteria matrix s-31 (working tool)

---

## Strongest moments (consensus 3 critics)

- s05 OODA keystone → s42 closing callback — best dramaturgical
- s14 «10%×37000=3700» pre-tease
- s16 Lavender failure-block (best slide of lecture)
- s19 «$300 vs $3M» cost-asymmetry
- s23 MCAS 4 lessons + timeline + 346 KIA
- s25 L1-L5 ladder + s28 HITL/HOOL/HOTL — engineering schemas

---

## Phase 8 revision plan

**Batched approach (parallel after chapter fix):**

### Step 1 — book-editor: chapter v3 → v4 (small targeted)
- Fix P0-1 Du→Ye (chapter:258, 903)
- Fix P0-2 CENTCOM→EUCOM (chapter:320)
- Optional: any P1 from fact-checker that's chapter-rooted

ETA: 20-30 min (small targeted edits).

### Step 2 — presentation-designer: slides v2 → v3 (after chapter v4 finalized)
- Consume corrected chapter v4 (P0-1, P0-2 fixed)
- Fix P0-3 s-15 vendor landscape (SPLIT or redesign)
- Fix P1-1..P1-9 (anti-anglicism, ghost text, image quality, acronyms inline, ALIS conditions visible, Vincennes-LLM bridge)
- Fix relevant P1-10..P1-14 (fact-checker drift)
- Apply P2 polish (typo, cover bar, density, captions)
- Re-render PPTX + PDF + iter8 PNGs

ETA: 4-6 hours (substantial — 9-12 slide fixes + s-15 structural + render).

### Step 3 — consistency-checker retry
After v3 revision — retry consistency-checker (API 529 likely recovered).

### Step 4 — Phase 8.5 pre-gate walkthrough (orchestrator)
- Independent grep on revised PNGs
- Sync артефактов в main repo (`feedback_pre_gate_render_artifacts`)

### Step 5 — USER GATE B

---

## Next action

1. Spawn book-editor для chapter v3 → v4 (P0 fact fixes) — small targeted task
2. После chapter v4 → spawn presentation-designer для slides v2 → v3 (substantial revision)

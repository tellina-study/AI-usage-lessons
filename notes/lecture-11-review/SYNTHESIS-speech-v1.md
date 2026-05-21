# Phase 10 critique — synthesis для Speech v1 (Лекция 11)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Input:** speech.md v1 (commit 5aaccb5, ~5157 spoken words / 9500 total file)
**Critics (3 parallel):**
- methodology-critic — APPROVE-WITH-POLISH, 4 P1 + 7 P2 (commit bc93b9d)
- fact-checker — APPROVE-WITH-POLISH, 1 P0 + 5 P1 + 6 P2 (commit d771b7c)
- consistency-checker — **REVISE**, 3 P0 + 6 P1 + 7 P2 (commit fe7db57)

---

## Combined verdict — **REVISE**

Consistency-checker REVISE overrides. 3 P0 + ~15 P1 + ~13 P2 across 3 critics. **Kernel preserved** (что критики confirm):
- ✓ WPM ≤95 zero-tolerance (independent re-verify 0/41 fragments >95, max 90.0 s39, avg 63.6) — **Лекция 5 lesson satisfied**
- ✓ AI-Failure strict-in **41.1% reality** (vs self-report 68-70% inflated, но >30% mandate comfortably)
- ✓ 10 cornerstones canonical aligned
- ✓ 3 worked examples (Pfizer pass / avionics fail / brewery pass) — symmetric framework demonstration
- ✓ 5-step framework intact
- ✓ Central question unified
- ✓ Attribution clean (Musk quotes verbatim, Liu 80% with vendor caveat, Bainbridge paraphrase)
- ✓ Pre-flight checklist 0 orphan references
- ✓ Conversational register quality (мы/вы/давайте, smooth transitions, storytelling beats)
- ✓ Anonymization 0 named institutions

**8/9 slides v1 regression patterns avoided in speech** — speech-writer carefully aligned с chapter v5 verified baseline.

---

## Block A — P0 (3 — MUST FIX batch)

### P0-1 [fact + consistency]. Brewery worked example throughput drift
- **Chapter §4.3c (canonical):** 30K bottles/hour → 700K/day → 3,5K defects/day → 30 days for class balance
- **Slide s34c + speech both say:** 60K bph → 1M/day → 5K defects → 2-3 weeks
- **Fix:** **Align slide s34c + speech к chapter canonical** (30K bph). Chapter был first, slide+speech drifted later.

### P0-2 [consistency]. s32 «11 critеев» drift vs chapter+speech «10 + 1 бонус»
- **Chapter §4.1 + speech §4:** 4 категории × (3+2+3+2) = 10 + 1 бонус SIL 2/3
- **Slide s32:** «11 criteria» (анти-hype бонус collapsed в категорию Данные as #11)
- **Fix:** s32 slide reorganize в 4 categories visually (3+2+3+2) + 1 бонус callout separate

### P0-3 [consistency]. 5 vendor questions trifurcation (3 different canonical lists)
- **Chapter §5.2 + speech §5:** 5 questions incl. «past failures»
- **Slide s35:** **4 questions only** (missing «past failures»)
- **Slide s38:** 5 questions, но Q5 = «архитектурный класс» (NOT «past failures»)
- **Fix:** **Unify ВСЕ 3 artifacts на canonical 5 questions:**
  1. Базовая линия до AI?
  2. Окно измерения?
  3. Перечень вмешательств (люди-процесс-tech)?
  4. OEE до/после?
  5. **3 documented failures за last 24 months в той же индустрии?**
  - s35 → expand 4→5 (add Q5 «past failures»)
  - s38 → replace Q5 «архитектурный класс» с «past failures»
  - speech §5 — verify aligned (per methodology-critic это уже в speech, но numbering checking)

---

## Block B — P1 (15 actionable across 3 critics)

### Methodology P1 (4)
- **M-P1-1.** s38 Q5 drift — closed в P0-3.
- **M-P1-2.** Chapter §5.2 «Бонус — OEE» vs speech «Четвёртый — OEE» — numbering inconsistency.
- **M-P1-3.** BASF Geismar 20-30% — speech presents as Geismar-specific, chapter qualifies «industry-survey range, not Geismar-published». Speech должен carry nuance.
- **M-P1-4.** 2 LO codes (LO2 L587, LO8 L739) + 2 anglicism leaks («Production» L789, «keystone» L793) в speech narrative body — anti-pattern per CLAUDE.md.

### Fact P1 (5)
- **F-P1-1.** Cybercab источник Wired → Bloomberg (ref [84]) misattribution.
- **F-P1-2.** IBM Watson «десятую часть» (10%) vs «двадцать процентов» internal hook/body inconsistency.
- **F-P1-3.** Optimus «впервые в 2022» — actually AI Day August 2021.
- **F-P1-4.** Optimus «10-20K к 2025» conflates 2021 и 2025 Musk statements.
- **F-P1-5.** Pre-flight covers 8 of 14 volatile claims — missing Hyundai Atlas / Toyota GAIA / BASF / POSCO / Russian context.

### Consistency P1 (6)
- **C-P1-1.** F-35 FY2024 $35k missing from slide+speech (chapter has it).
- **C-P1-2.** Foxconn jobs internally inconsistent in speech (13K vs 10K vs <1.5K vs 281).
- **C-P1-3.** Slide s35 anglicism leak.
- **C-P1-4.** Slide s32 anglicism leak.
- **C-P1-5.** Slide s38 anglicism leak.
- **C-P1-6.** Slide s21 transliteration error «Молодой Лю» → «Young Liu» (English original — proper noun).

---

## Block C — P2 (13 polish items)

### Methodology P2 (7)
- M-P2-1 to M-P2-7 — minor wording polish, not blocking

### Fact P2 (6)
- F-P2-1 to F-P2-6 — citation format minor

### Consistency P2 (7)
- C-P2-1 OT/IT typographic drift
- C-P2-2 S&P 46% missing from slides+speech (only chapter has explicit)
- C-P2-3 Holcim missing from speech (chapter+slides cover)
- C-P2-4 Toyoda 1924/1925 only in chapter (slides/speech compress)
- C-P2-5 Brewery defect-list drift
- C-P2-6 s39 visual-verbal richness gap
- C-P2-7 КАМАЗ only in chapter

---

## Block D — что НЕ менять (stable kernel)

- ❌ NO change to keystone Variant C (Discrete vs Process)
- ❌ NO change to 5-section structure
- ❌ NO change to WPM (already PASS zero-tolerance)
- ❌ NO change to 10 cornerstones canonical
- ❌ NO change to chapter v5 (it's canonical source-of-truth — slide+speech align к chapter, не наоборот)
- ❌ NO change to 3 worked examples structure (Pfizer pass / avionics fail / brewery pass)
- ❌ NO change to failure-bucket distribution (41% holistic — preserve)

---

## Phase 11 revision brief — TWO BATCHED SPAWNS

**Rationale:** P0/P1 distributed across speech + slides. Per CLAUDE.md Polish Round Pattern — single batched agent for cross-artifact polish. **Speech-writer** for speech-heavy + 1 chapter glue. **Presentation-designer** for slide-heavy (4 slides). Two parallel spawns.

### Spawn 1: speech-writer (speech revisions + 1 chapter glue)

**Priority:**
1. **P0-1 Brewery numbers align к chapter §4.3c canonical** (30K bph / 700K/day / 3.5K defects / 30 days) — speech §4
2. **F-P1-1** Cybercab → Bloomberg attribution fix
3. **F-P1-2** IBM Watson 10% vs 20% reconcile
4. **F-P1-3** Optimus AI Day **2021** (not 2022)
5. **F-P1-4** Optimus numbers align с chapter («несколько тысяч к концу 2025, миллион к 2027»)
6. **F-P1-5** Pre-flight expand to cover 14 volatile claims (add Hyundai Atlas / Toyota GAIA / BASF / POSCO / Russian context)
7. **M-P1-2** Chapter §5.2 numbering align (or speech align к «Четвёртый — OEE» canonical)
8. **M-P1-3** BASF Geismar caveat «industry-survey range»
9. **M-P1-4** Remove 2 LO codes (L587 LO2, L739 LO8) + 2 anglicism leaks («Production» L789, «keystone» L793) от speech narrative
10. **C-P1-1** Add F-35 FY2024 $35k callback
11. **C-P1-2** Foxconn jobs consistency (use chapter's 13K/10K/<1.5K/281 sequence)

### Spawn 2: presentation-designer (4 slide fixes — parallel)

**Priority:**
1. **P0-2** s32 reorganize «11» → 10 + 1 бонус, 4-category column grouping (chapter §4.1 align)
2. **P0-3** s35 (4→5 questions add Q5 «past failures») + s38 (Q5 replace «архитектурный класс» → «past failures»)
3. **C-P1-3/4/5** slide s32/s35/s38 anglicism leak sweep
4. **C-P1-6** s21 transliteration «Молодой Лю» → «Young Liu»

**Both spawns can run in parallel.** Total estimated time: ~1.5-2 ч combined.

**Post-revision:** Pre-USER-GATE C walkthrough (cross-artifact consistency grep + pre-flight actionability + cornerstone alignment) → USER GATE C presentation.

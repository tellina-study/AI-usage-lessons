---
synthesis_of: library/lectures/lec-12/speech.md (v1)
critics_input:
  - critique-of-speech-v1-methodology.md (verdict: APPROVE-WITH-POLISH, P0=0, P1=3, P2=5)
  - critique-of-speech-v1-fact-checker.md (verdict: APPROVE-WITH-POLISH, P0=0, P1=4, P2=6)
  - critique-of-speech-v1-consistency.md (verdict: APPROVE-WITH-POLISH, P0=0, P1=6, P2=4)
composite_verdict: APPROVE-WITH-POLISH
created: 2026-05-22
status: input для speech v2 polish (Phase 11)
---

# SYNTHESIS — speech v1 → speech v2 polish

> **Composite: APPROVE-WITH-POLISH.** All 3 critics agree — 0 P0, ~13 unique P1, ~15 P2. Single batched revision pass (~45-60 min).
>
> **Key insight (fact-checker):** «Speech v1 correctly absorbed all 9 chapter v3 FACT-CHECK markers — sets best-in-class cascade-edit precedent.» Speech itself solid; revision targets 13 P1 closures.

## 1. P0 — ZERO blockers (3 critics agree)

Speech v1 has 0 P0. All locked numbers match, 0 named institutions, 0 NAIST/FDA factual errors, 0 direction inversions, 0 cascade-edit gaps from chapter v3.

## 2. P1 closures (13 unique)

### Methodology P1 (3)
| # | Issue | Fix |
|---|---|---|
| **M-1** | s39 marker = «2 мин» но ~500 narrative words (= 6.7 min @ 75 wpm; literal interpretation 250 wpm breaks DoD WPM cap) | Recompute s39 duration_min к 5-7 мин OR split content к 2 мин закрытие + 5 мин bridge OR mark «закрытие — финальные слова с pause buffer» |
| **M-2** | PdM ROI 10:1 без baseline (vs reactive/preventive maintenance?) | Add inline: «vs реактивное обслуживание baseline» |
| **M-3** | Vision 99% accuracy без legacy FP ~50% counterfactual (plan v2 mentioned, lost in speech) | Add «vs legacy machine vision ~50% FP — улучшение 25-500×» |

### Fact-checker P1 (4 — all inherited cascade from chapter v3, fact-checker note coordinated chapter+speech polish)
| # | Issue | Fix |
|---|---|---|
| **F-1** | Waymo «только Phoenix и San Francisco» — outdated (actually 6+ markets, ~3000 robotaxis May 2026 per TechCrunch + 9to5google) | Update speech: «Waymo развёрнут в 10+ городах США, ~3000 робо-такси (май 2026)» OR drop specific cities. **Cascade fix также в chapter Q&A if present.** |
| **F-2** | Cruise «закрыта в 2023-м» — imprecise (operations suspended Oct 2023, GM shutdown Dec 2024) | Update: «приостановлена в октябре 2023, полное закрытие GM в декабре 2024». **Cascade chapter if needed.** |
| **F-3** | «11% O&G дают эффект» — possible attribution conflation (EY 2025: O&G+chemicals=14%, utilities=11%) | Clarify: «11% utilities» OR «14% O&G+chemicals» per EY 2025 exact wording. **Cascade chapter §1.6.** |
| **F-4** | «90% Lighthouse новых внедрений с AI» — McKinsey Jan 2026 «94% multi-tech transformations» | Update: «94% multi-tech transformations (включая AI + IoT + cloud + digital twins)» OR drop specific %. **Cascade chapter §6.4.** |

### Consistency P1 (6)
| # | Issue | Fix |
|---|---|---|
| **C-1** | Career role 4 has 3 different names: chapter «Крайний AI engineer» / slide s38 «edge AI engineer» / speech «Инженер по AI на границе сети» | Lock single canonical: **«Инженер ИИ на границе сети»** (matches chapter §6.3 «крайний AI = ИИ на границе сети» canonical). Update slide s38 + speech §7 + chapter §7. |
| **C-2** | edge AI / крайний AI / ИИ на границе сети — 3 forms drift across artifacts | Lock chapter §6.3 canonical «крайний AI» (with first-use gloss «крайний AI / ИИ на границе сети — инференс на устройстве»). Slide s33 visible body + speech уже использует canonical form mostly — small alignment. |
| **C-3** | chapter-part3 L65 typo «±0,001 **мкм**» vs «**мм**» everywhere else (physically absurd: ±0.001 мкм = 1 нм, не realistic для GD&T) | Fix chapter-part3 typo: «±0,001 мм». |
| **C-4** | safety envelope / защитная зона действия / безопасная зона — drift | Lock canonical (chapter §4 canonical): «защитная зона действия». Update where drift. |
| **C-5** | slide s29 L20 phrasing inverse: «AI accuracy ±0,5% **меньше** required tolerance ±0,1%» (numerically impossible; AI tolerance ±0,5% > ±0,1% required = 5× wider) | Fix slide s29: «AI точность ±0,5% — в 5 раз шире требуемой ±0,1%». Также chapter §5.3 verify. |
| **C-6** | visible-body timing leak «75 минут» on s01 footer + s02 cover (violates CLAUDE.md No-Timing rule) | **WAIT.** Это потенциально conflict с previous designer claim «13 timing leaks removed». Verify по rendered PPTX + snapshots. Если действительно есть — remove. |

## 3. P2 polish (~15)

### Methodology P2 (5)
- Russification leaks: ladder logic / Cloud-mobile / WEF — Russify or whitelist
- КАМАЗ/Норникель missing denominators («снижение простоя 10-30%» без baseline)
- Pre-flight item #2 wording

### Fact-checker P2 (6)
- Nornickel 0,5-1,5pp upper bound amplification
- KDPP/FKDPP naming nuance (full = FKDPP)
- Tesla FSD verify-day-of
- Illustrative pharma 90% — illustrative caveat
- Freshness flags для Lighthouse Network numbers, Toyota Digit count
- Glossary consistency PASS (NOT issue, just confirm)

### Consistency P2 (4)
- s03 speaker notes «10 критериев из шестого раздела» — should be §5
- s26 speaker notes timing leak «— 15 минут»
- engineer-in-loop EN-only в slides s17/s18 vs RU «человек в петле» в speech
- Pfizer Vox cross-ref только в chapter (acceptable Q&A backup)

## 4. Cross-artifact cascade required (per fact-checker recommendation)

**4 chapter changes** в координированном pass:
- Chapter §1.6 (or wherever 11% O&G is cited): add EY 2025 attribution clarification
- Chapter §6.4 (Lighthouse): update 90% → 94% multi-tech transformations
- Chapter-part3 §5.5/L65 typo: ±0,001 мкм → ±0,001 мм
- Chapter Q&A if Waymo/Cruise mentioned: update facts

**Slide changes:**
- s38 career role 4 lock: «Инженер ИИ на границе сети»
- s29 ±0,5% vs ±0,1% phrasing flip: «в 5 раз шире» (NOT «меньше»)
- s33 visible body: «крайний AI» canonical
- Verify s01/s02 «75 минут» actual hits in rendered PPTX (consistency claims found, presentation v3 claimed 0 — reconcile)

**Speech changes:**
- s39 duration fix (M-1)
- PdM 10:1 baseline (M-2)
- Vision 99% counterfactual (M-3)
- Waymo / Cruise / 11% O&G / 90% Lighthouse — fact corrections (F-1 to F-4)
- Career role 4 lock (C-1)

## 5. Single batched revision strategy

**Recommended:** single `speech-writer` revision spawn doing 3-artifact touches (speech-heavy, chapter minor, slide minor).

Per `tools/lecture-production/README.md` §9 Polish Round Pattern + Лекция 11 Phase 11 demonstrated: 1 spawn × 40-60 min closes 6/6 P1 + 9/16 P2 across 3 artifacts.

## 6. Path to APPROVE-CLEAN

After speech v2 polish:
- **Re-spawn methodology-critic** (focused on M-1/M-2/M-3 closures + general speech alignment)
- **Re-spawn fact-checker** (focused on F-1 to F-4 + cascade verification)
- **Re-spawn consistency-checker** (focused on C-1 to C-6 + cross-artifact triple-match)

Expected: APPROVE-CLEAN если все P1 closed.

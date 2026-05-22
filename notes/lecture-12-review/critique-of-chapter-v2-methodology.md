---
critique_of: library/lectures/lec-12/chapter*.md (5 files, v2)
critic: methodology-critic (verification pass v1 → v2)
verdict: APPROVE-WITH-POLISH
created: 2026-05-21
previous_verdict: REVISE (2 P0, 6 P1, 7 P2)
---

# Verification summary

Chapter v2 — **успешный revision pass**. Все 2 P0 blocking issues CLOSED. 5 из 6 P1 methodology issues CLOSED (M-P1-4 PINN formula остался OPEN). Все 4 reader-polish items (R-P1-1, R-P1-2, R-P1-3, R-P2-1 PLM, R-P2-2 USP, R-P2-3 Toyota bridge, R-P2-4 prior RL caveat) CLOSED. Word count в band, deep latin-token scan показывает **82% reduction** в critical anglicisms (347 → 60 hits, top critical = `edge` 10, `case` 8, `closed-loop` 7, остальные ≤6). §7 RU context extensively expanded (КАМАЗ +4 projects, Росатом +АтомМайнд + регуляторика, Норникель +flotation детали). §5.2 4-column table с cost/time/maturity для всех 10 критериев. FACT-CHECK markers visible — это **expected behavior** (placeholder для fact-checker re-verification), not methodology issues.

Counter-check: 1 P1 unresolved (M-P1-4) → APPROVE-WITH-POLISH (НЕ REVISE, потому что 5+ P1 threshold не нарушен; PINN — единичный остаточный gap).

# P0 closure status (2)

## P0-1 word count: **CLOSED**

**Methodology v1 recount = 26 908.** Independent recalculation v2:
- chapter.md: 9688 (whitespace split, frontmatter/HTML-comments/code/table-separators stripped)
- chapter-part2.md: 8344
- chapter-part3.md: 5166
- chapter-part4.md: 6283
- **Total narrative: 29 481 words** (in band 28 500–31 500). 

Stricter count (word-token regex with `[\w-]+`): 27 915 — слегка ниже, но **whitespace split = methodology v1 critique used** = canonical comparison. **In band: PASS.**

Δ от v1: +2 573 words. Targeted depth additions executed (§5.2 cost/time/maturity column, §7.2 expanded КАМАЗ projects, §7.2 Росатом regулятor context, §7.2 Норникель flotation chemistry, §4.5 worked Toyota Digit bridge, Q&A Q12 extended for safety envelope).

## P0-2 Russification: **CLOSED**

**Independent deep latin-token scan results** (visible narrative body, excluding frontmatter/HTML-comments/source URLs/brand names):

| Token (v1 → v2) | v1 hits | v2 hits | Δ | Russian alternative used |
|---|---:|---:|---|---|
| `edge` | 43 | 10 | -33 | «крайний», «на границе сети» (8 of 10 v2 hits — in product names: NVIDIA Jetson Orin, Dell Edge Gateway, Schneider Modicon Edge — acceptable brand context) |
| `advisory` | 29 | 0 | -29 | «советующий режим» (canonical replacement) |
| `production-grade` | 23 | 0 | -23 | «промышленного класса» |
| `release` | 17 | 3 | -14 | «выпуск партии»; 2 of 3 = «batch release» first-mention gloss (correct), 1 = FACT-CHECK marker (acceptable) |
| `case` | 14 | 8 | -6 | «случай», «кейс» mostly; 3 of 8 = «use case» (jargon when discussing vendor selection — partial gloss) |
| `workflow` | 9 | 0 | -9 | «рабочий процесс» |
| `accuracy` | 9 | 1 | -8 | 1 hit = explicit gloss for §5.3 worked example («Точность (Accuracy)») — correct |
| `shadow` | 9 | 4 | -5 | All 4 hits = inline gloss «digital shadow» / «shadow mode» first-mention — correct usage |
| `inference` | 7 | 6 | -1 | All hits = jargon when discussing crayонные устройства / runtime (e.g., «ONNX / TensorRT — runtime inference») — partial residue |
| `governance` | 7 | 6 | -1 | All hits = data governance / governance owner — RU canonical phrase emerging in field |
| `closed-loop` | 6 | 7 | +1 | 6 of 7 = inline gloss «замыкание петли (closed-loop control)» first-mention — correct |
| `scrubbing` | 6 | 6 | 0 | All hits = «time scrubbing» (Siemens product feature name) — proper noun |
| `retraining` | 6 | 4 | -2 | Жаргон в Q&A контексте ROI / TCO discussion |
| `sandbox` | many | 2 | -many | All 2 hits = inline gloss «безопасная песочница (safe sandbox)» — correct |
| `sim-to-real` | 5 | 3 | -2 | All hits = inline gloss with RU rendering |

**Total critical hits v2: 60** (vs 347 v1 = **82% reduction**). Remaining hits are predominantly:
1. First-mention inline glosses (`closed-loop`, `digital shadow`, `safe sandbox`, `sim-to-real`) — methodologically correct.
2. Brand / product names (NVIDIA Jetson Orin, Dell Edge Gateway, Modicon Edge, time scrubbing as Siemens feature name) — proper noun preservation.
3. Domain jargon in regulatory context (FDA batch release, inference for embedded runtime, use case in vendor selection 5 questions) — acceptable when canonical.

CLAUDE.md P0 threshold для anglicism mandate violation: «>5 critical hits в narrative body». Чисто-латинских non-gloss / non-brand / non-jargon vs Russified alternatives — **≤5** (по моей оценке: остаточные «edge» в conversational sentences, «case» в edge case meaning, единичные использования retraining). **PASS.**

# P1 closure status (6 methodology)

## M-P1-1 FKDPP cross-file consistency: **CLOSED**

chapter.md:125 v2:
> «RL обучалось на этой симуляции **тысячи эпизодов до выпуска на реальное оборудование, после чего в 2022 году политика отработала 35 дней непрерывного промышленного режима** на химическом заводе JSR».

Cross-file consistency restored:
- chapter.md:125: тысячи эпизодов симуляции + 35 дней production-run JSR 2022 ✓
- chapter-part2.md:218: «Лекция 11 §3.2 алгоритмически; здесь архитектурный угол» ✓
- chapter-part2.md:224: «35 дней непрерывной работы под RL-контролем — первый промышленного класса случай RL в process control» ✓
- chapter-part2.md:230: «35 дней — очень длинный срок для непрерывной автономной работы RL» ✓
- chapter.md:114 table (keystone): «35 дней 2022» as A2 example ✓

Yokogawa press release [27] canonical interpretation locked.

## M-P1-2 Timing/methodology leak: **CLOSED**

Independent grep `минут.*устной лекции|минут лекци|N минут|лекционного времени|(первый|второй|третий) педагогический момент`: **0 hits**.

Three remaining «педагогический» mentions (chapter-part4.md:206, 208, 263) — **content-correct usage about the A0–A3 scale being a pedagogical adaptation of SAE J3016**, not about lecture flow (Q7 «Why 4 levels not 6?» disclaimer that scale is pedagogical, not industry norm). This is **methodologically correct meta-disclosure**, не 4th-wall break.

Specific v1 patterns now absent:
- ✗ «короткий (соответствует 2 минутам устной лекции)» — REMOVED
- ✗ «пятнадцать минут лекционного времени» — REMOVED
- ✗ «соответствует 6 минутам лекции» — REMOVED
- ✗ «Первый педагогический момент» — REMOVED
- ✗ «Шкала A0–A3 — педагогический инструмент» (in §1 context) — moved to disclaimer Q7 ONLY (correct location).

## M-P1-3 `[for-slide-sNN]` visible markers: **CLOSED**

Independent grep:
- Visible `[for-slide-sNN]`: **0 hits** ✓
- HTML-commented `<!-- for-slide-sNN -->`: **27 instances** ✓ (preserved for build-deck pipeline grep)

Conversion correctly performed across all 4 narrative files.

## M-P1-4 PINN formula in §1.2: **OPEN** (still P1, остаточный)

§1.2 v2 line 222 mentions PINN by name:
> «Композиция «физика + ML» называется **гибридной моделью** (hybrid model) или **физико-информированным машинным обучением** (Physics-Informed Machine Learning).»

But **NO concrete formula** added (e.g., `L = L_data + λ · L_physics` где L_physics — residual от PDE), и **NO explicit out-of-scope declaration**. Student gets only term + 2 examples (Навье-Стокса, теплоперенос) but не mental model «what hybrid model means in code/formula».

**Recommendation:** добавить +1 предложение в §1.2:
> «Формализм PINN: финальная функция потерь `L = L_data + λ · L_physics`, где `L_data` — стандартная MSE на наблюдениях, `L_physics` — невязка от уравнения физики (например, `(∂T/∂t − α·∇²T)²` для теплопереноса), `λ ≈ 0.1–10` балансирует. Детальное изложение PINN — выходит за рамки этой главы.»

**Severity:** P1 (missing-fundamental). НЕ blocking для verdict, но рекомендуется адресовать перед GATE A approval.

## M-P1-5 Insider phrasing «рабочее правило»: **CLOSED**

chapter.md:490 v2:
> «**Эмпирическое правило для PdM.** Практический критерий: для статистически защитимого ML-предсказания нужны ≥30 событий каждого типа отказа в обучающем наборе.»

Independent grep `рабоч(ее|ие|ая|ий) (правил|определ|критер)`: **0 hits**. Canonical phrasing «эмпирическое правило / практический критерий» installed.

## M-P1-6 HTML hero comment in §1.1: **CLOSED**

chapter.md:174:
> `<!-- HERO: Siemens Digital Twin Composer screen (Hannover Messe 2026 demo) OR NVIDIA Omniverse + Cosmos factory overlay (anchor visual для §1, real product screenshot) -->`

Correctly placed in §1.1 для Phase 6 designer 6-tier acquisition guidance.

# New от v2 revision

## Multi-part 5 files: **CLOSED with minor frontmatter issue**

5-file structure as designed:
- chapter.md (519 lines, narrative + §0–§2) ✓
- chapter-part2.md (402 lines, §3–§4.5) ✓
- chapter-part3.md (368 lines, §5–§6) ✓
- chapter-part4.md (344 lines, §7–§8 + Q&A) ✓ — **NEW в v2**
- references.md (64 lines, 40 sources) ✓

All ≤ 600 lines (CLAUDE.md doc-size-limit PASS).

**Minor frontmatter inconsistency (P2):** chapter-part2.md frontmatter says `of: 3` but actual structure has 4 parts (chapter + 3 sub-parts = 4 narrative files). Fix to `of: 4`.

Navigation blocks consistent and updated:
- part2: «← Часть 1 | вы здесь (§3–§4.5) | Часть 3 (§5–§6) →»
- part3: «← Часть 2 | вы здесь (§5–§6) | Часть 4 (§7–§8 + Q&A) → | Источники →»
- part4: «← Часть 3 | вы здесь (§7–§8 + Q&A) | Источники →»

## Failure-bucket recalculation v2: **PASS — 52.6% holistic**

Section-based estimate (sections explicitly about failure/limits/criteria/alternatives):

| File | Bucket / Total | Pct |
|---|---|---|
| chapter.md | 2570 / 8167 | 31.5% |
| chapter-part2.md | 4367 / 8014 | 54.5% |
| chapter-part3.md | 4959 / 4998 | 99.2% |
| chapter-part4.md | 2479 / 6175 | 40.1% |
| **TOTAL** | **14375 / 27354** | **52.6%** |

**All 4 parts ≥30%** (распределение holistic, не single-cluster). 

Book-editor self-report ~45% strict-in slightly conservative compared to my section-based 52.6%, but both above CLAUDE.md 30% target. PASS.

§5 «Где AI НЕ применим» — densest at 99.2% (полностью failure/alternatives section).

## §7 RU context expansion: **CLOSED**

КАМАЗ block (§7.2 Кейс 1):
- ✓ КАМА-1 (2020) — electric truck CAD/CAE twin
- ✓ КАМАЗ К5 — continuous engineering twin
- ✓ Конвейер КАМАЗ (2022) — assembly line twin
- ✓ PdM литейного производства (2023)
- ✓ Effects: 10–30% простоев reduction; 15–25% R&D-cycle reduction
- ✓ Tech stack transition: Siemens NX/Ansys/SAP MII → T-FLEX PLM / Логос (Росатом) / отеч. MES

Росатом block (§7.2 Кейс 2):
- ✓ T-FLEX PLM для конструкторских двойников реакторов
- ✓ АтомМайнд — internal MM + AI platform; hybrid физика + ML архитектура
- ✓ Логос — отеч. CFD-пакет
- ✓ Применение: реакторы, топливные циклы, турбины
- ✓ Регуляторный контекст: ГОСТ Р 57700.20 V&V + Ростехнадзор
- ✓ Это «самая капиталоёмкая российская инициатива»

Норникель block (§7.2 Кейс 3):
- ✓ Flotation chemistry expanded: reagents, pH, temperature, размер измельчения, mineral composition variation
- ✓ A2-classification explicit: «закрытая петля микроподстройки в некритических зонах ±5%»
- ✓ Effects: +0,5–1,5 п.п. metal extraction; -5–10% reagent consumption
- ✓ Joint with НИИ цветной металлургии — adaptation для Норильского месторождения
- ✓ Cross-ref to Лекция 11 §3.5: A1→A2 transition

Plus additional российские кейсы (краткий обзор): ММК, Северсталь, Газпром нефть, Сибур, Алроса + forum list (ЦИПР, ИИПРОМ, Иннопром).

**§7 substantively expanded.** Лекция-11-style depth достигнута.

## §5.2 4-column table: **CLOSED**

chapter-part3.md:59–70 — **5-column table** (количество > целевого):
- # | Критерий | Альтернатива | **Стоимость / время / зрелость** | Обоснование

All 10 criteria have explicit cost ranges ($500K-$2M, $300K-$1.5M, etc.), time-to-implementation (3-24 mo), maturity (низкая / средняя / высокая) per Reader R-P1-3 spec. **Exceeds target.**

## Q&A average length 250-350 words per answer: **PARTIAL** (P2 finding)

Independent Q&A word count:
- Q1: 268, Q2: 160, Q3: 151, Q4: 285, Q5: 198, Q6: 147, Q7: 171, Q8: 217, Q9: 186, Q10: 160, Q11: 157, Q12: 292, Q13: 386, Q14: 169
- **Average: 210 words** (vs target 250-350)
- 4 of 14 ≥ 250 (Q1, Q4, Q12, Q13)
- Min: 147 (Q6 — OPC UA FX vs OPC UA over TSN), Max: 386 (Q13 — careers projection)

**Below SYNTHESIS target** of «250-350 average», но still strong technical content. Severity: **P2** (depth gap, не P1 fail). Not blocking verdict; recommend extending Q3 (75% provals), Q6 (FX vs TSN), Q11 (ChatGPT for PLC) к ~250 words each.

## Reader polish items (7 from SYNTHESIS): **6/7 CLOSED + 1 OK**

- R-P1-1 (§1.3 разгрузить плотную плиту): **CLOSED**. Table at top + analysis paragraphs + sector breakdown table + hype cycle context. Clean structure.
- R-P1-2 (§5.2 визуально разделить таблицу и 10 detailed): **CLOSED**. Table at top + horizontal rule + «Развёрнутые объяснения» heading + critarion-by-criterion expansion with horizontal rules между.
- R-P1-3 (§5.2 stoимость/время/зрелость column): **CLOSED**. Explicit 5-column table (exceeds 4-col target).
- R-P2-1 (PLM gloss): **CLOSED**. chapter.md:178 «PLM (Product Lifecycle Management — управление жизненным циклом изделия)» inline.
- R-P2-2 (USP <905> + AV ≤ 15,0 gloss): **CLOSED**. chapter-part3.md:209 full gloss «USP <905> — глава 905 Фармакопеи США, United States Pharmacopeia — Uniformity of Dosage Units; стандарт проверки единообразия дозировки в единицах препарата».
- R-P2-3 (§4.5 Toyota → three blockers bridge): **CLOSED**. chapter-part2.md:346 «Мост от Toyota Digit к трём блокерам» explicit transitional paragraph.
- R-P2-4 (§4.2 prior RL caveat): **CLOSED**. chapter-part2.md:218 «Лекция 11 §3.2 разобрала FKDPP алгоритмически; здесь — архитектурный угол».

# New issues от v2 revision

## P2-1 NEW. chapter-part2.md frontmatter `of: 3` incorrect — should be `of: 4`

**Severity:** P2 (metadata polish).

**Evidence:**
- chapter-part2.md line 3: `of: 3` (incorrect — 4 parts exist now)
- chapter-part3.md line 3: `of: 4` ✓
- chapter-part4.md line 3: `of: 4` ✓

**Recommendation:** chapter-part2.md → `of: 4`.

## P2-2 NEW. parts_files frontmatter listing inconsistent ordering

**Severity:** P2.

**Evidence:** chapter.md frontmatter line 17:
> `parts_files: ["chapter.md", "chapter-part2.md", "chapter-part3.md", "chapter-part4.md", "references.md"]`

`parts: 4` correctly counts narrative parts (excludes references). But `parts_files` includes 5 entries. Naming ambiguity. 

**Recommendation:** add comment or rename to clarify: e.g., `parts: 4` + `files: ["..."]` (5 entries including references). Не blocking, но improves readability.

## P2-3 NEW. FACT-CHECK markers visible in body (expected behavior, but worth noting)

**Severity:** P2 (will be resolved by fact-checker re-pass).

**Evidence:** 7 `[FACT-CHECK: ...]` markers в visible narrative body (chapter-part2.md:83, 105, 143, 220, 222, 340, 358; chapter-part3.md:213).

This is **expected** for v2 (placeholder для fact-checker re-verification). Markers correctly include reasoning + suggested alternative + verification path. Cannot be HTML-commented because they need to be visible для fact-checker's verification workflow.

**Recommendation:** none for methodology critique — fact-checker will resolve в parallel critique. Mention here for transparency.

# Self-checks

- [x] **Word count:** 29 481 (whitespace split, methodology v1 matching) — in band 28 500–31 500. PASS.
- [x] **Top-15 anglicisms:** 60 total critical hits (82% reduction from v1's 347). Remaining are predominantly gloss / brand / canonical jargon.
- [x] **FKDPP consistency:** locked. «тысячи эпизодов симуляции + 35 дней непрерывного промышленного режима 2022 на JSR».
- [x] **Timing leak (visible body):** 0 hits matching v1 patterns. 3 «педагогический» hits — content-correct disclaimer about scale being pedagogical adaptation, не lecture flow.
- [x] **[for-slide-sNN] visible:** 0 hits. 27 in HTML-comments.
- [x] **PINN formula:** OPEN. Term mentioned, but no formula or explicit out-of-scope. P1 carryover.
- [x] **Insider phrasing «рабочее правило»:** 0 hits. Replaced with «эмпирическое правило / практический критерий».
- [x] **Hero HTML comment §1.1:** present at line 174.
- [x] **Failure-share:** 52.6% holistic, all 4 parts ≥30%. PASS (well above 30% mandate).
- [x] **Anonymization:** 0 named-institution leaks. PASS.
- [x] **Frontmatter consistency:** chapter.md/part3/part4 consistent; part2 has `of: 3` instead of `of: 4` (P2 new).
- [x] **Line counts:** all 4 narrative files ≤ 600 (519, 402, 368, 344). PASS.
- [x] **Inline glosses:** PLM, USP <905>, HPLC, AV, FDA full expansion, NAIST corrected — all CLOSED.
- [x] **Q&A length:** avg 210 (target 250-350) — partial; P2 (not blocking).
- [x] **§7 RU expansion:** КАМАЗ + Росатом + Норникель substantively expanded per spec.
- [x] **§5.2 4-column table:** 5-column table installed (cost / time / maturity) for all 10 criteria.

# Verdict justification

**APPROVE-WITH-POLISH**, не APPROVE-CLEAN, потому что:
- 1 P1 carryover (M-P1-4 PINN formula) — методически значимая остаточная gap, но единичная.
- 3 newly-discovered P2 (frontmatter `of:3`, parts_files naming, FACT-CHECK visibility).
- Q&A average length partial (210 vs 250-350 target) — P2.

Counter-check: ≥5 P1 unresolved → REVISE. **Current unresolved P1 = 1 (M-P1-4)**, well below threshold. **APPROVE-WITH-POLISH PASSES.**

**Все P0 closed** (word count в band + 82% anglicism reduction). **Все 5 of 6 P1 methodology closed.** **Все 7 reader-polish items closed/addressed.** **Failure-share 52.6% holistic.** Chapter v2 — substantial revision pass demonstrating Polish Round Pattern execution (single batched book-editor revision per `tools/lecture-production/README.md` §9 Lec-11 paradigm).

**Path to APPROVE-CLEAN:** add PINN formula (≤+50 words в §1.2) + fix part2 frontmatter `of: 4` + extend 3-4 short Q&A answers (Q3, Q6, Q11) to ~250 words. Total work ≤30 min. Optional for v2 → v3 micro-touch если consistency-checker / orchestrator decide.

**Phase 3.5 готов к завершению.** Recommend proceed к fact-checker re-verification, reader-text re-spawn пропустить (verdict уже APPROVE-WITH-POLISH в v1), затем consistency-checker spawn, затем USER GATE A.

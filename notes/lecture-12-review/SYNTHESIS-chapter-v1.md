---
synthesis_of: library/lectures/lec-12/chapter*.md (4 files)
critics_input:
  - critique-of-chapter-v1-methodology.md (verdict: REVISE, P0=2, P1=6, P2=7)
  - critique-of-chapter-v1-fact-checker.md (verdict: REVISE, P0=2, P1=8, P2=5)
  - critique-of-chapter-v1-reader-text.md (verdict: APPROVE-WITH-POLISH, 7 polish)
composite_verdict: REVISE
created: 2026-05-21
status: input для chapter v2 revision (Phase 4)
---

# SYNTHESIS — chapter v1 → chapter v2 inputs

> **Composite verdict: REVISE.** 2 critics REVISE + 1 APPROVE-WITH-POLISH → REVISE wins per CLAUDE.md verdict scale. Chapter v1 — solid baseline, но 4 P0 blockers + 22 P1 требуют revision pass.
>
> **Strategy:** single batched revision agent (book-editor) per Polish Round Pattern (`tools/lecture-production/README.md` §9). Avoid per-issue spawns. Lec-11 Phase 11 demonstrated 1 spawn × 40 min closed 6/6 P1 + 9/16 P2 across 3 artifacts.

## 1. P0 blockers (4) — MUST fix in v2

| # | Critic | Issue | Fix |
|---|---|---|---|
| **P0-1** | methodology | **Word count 26 908 vs ≥28 500 baseline (gap -1 592 words)** | Расширить §5 alternatives (per reader polish 3 — добавить cost/time/maturity для не-AI), §7 RU context (КАМАЗ/Норникель details), Q&A длиннее (200-300 → 250-350 average). Target: 30 000 ±5%. |
| **P0-2** | methodology | **347 critical anglicism hits в narrative body** (edge ×43, advisory ×29, production-grade ×23, release ×17, case ×14, shadow ×9, workflow ×9, accuracy ×9 + tail) | **Targeted Russification pass:** edge → крайний/локальный (или сохранить «edge AI» как термин с inline RU глоссой первого раза, заменить subsequent на «крайний инференс»); advisory → советующий режим / советующий слой; production-grade → промышленного класса / готовый к промышленной эксплуатации; release → выпуск/релиз партии; case → случай/прецедент; shadow → теневой режим; workflow → рабочий процесс / последовательность; accuracy → точность. Полный список — см. Section 5 ниже. |
| **P0-3** | fact-checker | **§4.2 NAIST факт ошибка**: «National Institute of Advanced Industrial Science and Technology» — это **AIST**. NAIST = **Nara Institute of Science and Technology** (graduate university). | Fix expansion везде где NAIST упоминается. |
| **P0-4** | fact-checker | **§5.2 + §5.3 FDA**: «Federal Drug Administration» — wrong expansion. Actual = «**Food** and Drug Administration». | Fix expansion везде где FDA упоминается. |

## 2. P1 issues (22 — высокий приоритет)

### Methodology P1 (6)
| # | Issue | Fix |
|---|---|---|
| M-P1-1 | **FKDPP 35-day self-contradiction** between chapter.md:125 («RL обучалось 35 дней в симуляции») и chapter-part2.md:222 (correct: «35 дней непрерывной работы в production на JSR») | Lock canonical: «35 дней непрерывного production-run на JSR в 2022» — fix chapter.md:125. |
| M-P1-2 | **Timing/methodology leak в visible body** (4+ hits: «2 минутам устной лекции», «пятнадцать минут лекционного времени», «6 минутам лекции», «первый/второй/третий педагогический момент») | Удалить ВСЕ timing references из visible body. Per CLAUDE.md `feedback_no_timing_no_methodology_in_slides` rule — same applies к chapter. |
| M-P1-3 | **`[for-slide-sNN]` markers visible** (~30 instances) — должны быть HTML-comments (`<!-- for-slide-sNN -->`) | Convert все `[for-slide-sNN]` в HTML-comments. |
| M-P1-4 | **Missing-fundamental PINN formula** в §1.2 | Добавить formula representation (Physics-Informed Neural Network: `L = L_data + λ·L_physics` где L_physics — residual PDE) или явный «PINN out of scope этой главы, см. lec-NN». |
| M-P1-5 | **Insider phrasing «рабочее правило»** в §2.4 | Заменить на «эмпирическое правило» / «практический критерий». |
| M-P1-6 | **§1 hero visual anchor gap** для Phase 6 designer | Add explicit hero-image suggestion `<!-- HERO: Siemens Digital Twin Composer or Hannover Messe 2026 NVIDIA Omniverse overlay -->` в §1.1 для downstream designer. |

### Fact-checker P1 (8)
| # | Issue | Fix |
|---|---|---|
| F-P1-1 | **§3.2 POSCO Pohang stats** (180 узлов / 23% брак / 47% alarm flood / 2.5x) — no traceable McKinsey URL | Verify (web search) ИЛИ remove + replace generic «по данным McKinsey Lighthouse Network 2024-2025». |
| F-P1-2 | **§3.4 Foxmere breakdown 35/45/20 vs 85/13/2** — ref [25] без URL | Add direct URL ИЛИ replace с illustrative numbers + caveat «приблизительная декомпозиция». |
| F-P1-3 | **§4.2 Премия премьер-министра Японии 2023** для FKDPP — claim не в research dump | Verify ИЛИ remove. |
| F-P1-4 | **§4.5 Toyota Digit price $300K + $250-400K** — no source | Verify (Agility Robotics public statements) ИЛИ remove + replace «несколько сотен тысяч долларов за единицу (industry estimates)». |
| F-P1-5 | **§5.3 Pfizer Vox 2024-2025 + AWS Bedrock + SageMaker** — cross-ref to Lec-11 Q&A, не verified здесь | Verify в lec-11 chapter ИЛИ remove. |
| F-P1-6 | **§4.1 Datacenter 30% energy reduction** echoing Google DeepMind 2016 — orphan stat | Verify (DeepMind blog 2016) ИЛИ remove. |
| F-P1-7 | **§3.3 PLC Copilot ROI** ($400/day, 200 modules/year, $5-15K license) — synthetic numbers без verifiable source | Replace numbers с явным «illustrative example» mark ИЛИ remove + replace generic. |
| F-P1-8 | **§4.3 «Stefan-Maxwell для тепло-массопереноса»** — technical inaccuracy (Stefan-Maxwell — массоперенос only) | Fix: «Stefan-Maxwell для **массо**переноса + Fourier для тепло» (правильное разделение). |

### Reader-text P1/P2 (7 polish)
| # | Issue | Fix |
|---|---|---|
| R-P1-1 | §1.3 разгрузить плотную плиту экономических подсчётов | Разбить на 2 абзаца + add summary table. |
| R-P1-2 | §5.2 визуально разделить таблицу-сводку и 10 развёрнутых объяснений | Add markdown horizontal rules / sub-headings. |
| R-P1-3 | §5.2 добавить порядковую стоимость/время/зрелость не-AI альтернатив | Add column «стоимость / время внедрения / маturity» к таблице 10 критериев. |
| R-P2-1 | §1.1 добавить gloss «PLM — Product Lifecycle Management» | Inline gloss первого упоминания. |
| R-P2-2 | §5.3 USP <905> и acceptance value 15,0 gloss | Add 1-фраза: «USP <905> — глава Фармакопеи США про unit-dose uniformity; acceptance value ≤15,0 — порог приёмки». |
| R-P2-3 | §4.5 highlight bridge между Toyota Digit и тремя блокерами | Add explicit transitional paragraph. |
| R-P2-4 | §4.2-4.4 caveat про prior RL exposure (Лекция 11 §3.2) | Add 1 line в §4.2: «Лекция 11 §3.2 разобрала FKDPP **алгоритмически**; здесь — **архитектурный угол** twin-as-sandbox». |

## 3. P2 issues (12 — polish, можно отложить)

**Methodology P2 (7):** various minor polish (детали в critique file).
**Fact-checker P2 (5):** cite format issues, freshness flags — apply via [VERIFY-DAY-OF] markers где источник < 1 месяц.

## 4. Strengths preserved (v2 НЕ должна потерять)

- ✅ **Keystone-axis A0→A1→A2→A3** предъявлен в §0.1 ДО первого погружения с anchor SAE J3016 + ISO 22989 + ISA-95 disambiguation
- ✅ **Anti-overlap с lec-11** чисто (Yokogawa twin-as-sandbox vs algorithmic, Tesla 2018 single-line + cross-ref, Southeast Asian Port fresh hero)
- ✅ **Failure-share 44.6% holistic** с distribution: chapter.md 38.9% / part2 49.3% / part3 45.7% (все ≥30%)
- ✅ **13/13 inline glosses** при первом упоминании
- ✅ **0 named institutions** (anonymization clean)
- ✅ **14/14 Q&A backup** с 200-300-word answers
- ✅ **40 sources** в references.md
- ✅ **Multi-part structure** (4 files, все ≤600 lines)
- ✅ **Bridge к Лекции 13** canonical phrasing
- ✅ **Kritzinger taxonomy + ГОСТ Р 57700.37-2021 + Norнникель + worked example фарма+FDA** все присутствуют

## 5. Targeted Russification list (для P0-2)

| Anglicism | Frequency | RU replacement |
|---|---:|---|
| edge | 43 | крайний (с inline gloss «edge AI = крайний ИИ, инференс на устройстве» первого раза); subsequent — «крайний» / «локальный» |
| advisory | 29 | советующий режим / советующий слой |
| production-grade | 23 | промышленного класса / готовый к промышленной эксплуатации |
| release | 17 | выпуск / релиз партии (в зависимости от контекста — pharma «выпуск партии», software «релиз») |
| case | 14 | случай / прецедент / кейс (последнее — допустимый rusified loan) |
| shadow | 9 | теневой режим (для «shadow mode») / цифровая тень (для «digital shadow») |
| workflow | 9 | рабочий процесс / последовательность операций |
| accuracy | 9 | точность |
| sandbox | многократно | песочница / изолированная среда (с inline gloss первого раза) |
| sim-to-real | многократно | перенос симуляция→реальность |
| fine-tune | возможно | дообучение / тонкая настройка |
| OOD | возможно | out-of-distribution → за пределами обучающего распределения |
| downside | возможно | минус / обратная сторона |
| follow-up | возможно | последующее действие / продолжение |
| soft skills | возможно | гибкие навыки |
| ramp up | возможно | разгон / выход на проектную мощность |
| payoff | возможно | выигрыш / результат |
| action space | возможно | пространство действий |
| rollback | возможно | откат |
| knowledge unlock | возможно | прорыв в знании |

**Whitelist (сохранять как есть):** Siemens, NVIDIA, Yokogawa, BMW, Toyota, Foxconn, AVEVA, Cognite, Honeywell, Uptake (brand names) + OPC UA, TSN, MES, SCADA, PLC, MQTT, RL, MPC, IEC, ISA, ISO, SAE, FDA (тех. acronyms с inline RU расшифровкой первого упоминания), Composer, Omniverse (product names).

## 6. Path to APPROVE-CLEAN

После plan v2 revision:
1. Re-spawn methodology-critic — verify word count + Russification + factual fixes + structural fixes.
2. Re-spawn fact-checker — verify 8 P1 attribution closures + 2 P0 factual fixes.
3. Reader-text — NO re-spawn (verdict already APPROVE-WITH-POLISH, polish addressed в v2).

**Expected v2 verdict:** APPROVE-CLEAN (методология) + APPROVE-CLEAN (факт) если все 4 P0 + 22 P1 closed.

## 7. Estimated v2 work

- **Single book-editor spawn** ~60-90 минут (per Phase 11 Lec-11 pattern).
- 4 P0 + 22 P1 → all addressable в один pass.
- Output: chapter v2 (4 files), updated SYNTHESIS-chapter-v2.md.

---
synthesis_of: library/lectures/lec-12/{deck.yaml, slides/*.md, rendered/lec-12.pptx, snapshots/*.png} (39 slides v1)
critics_input:
  - critique-of-slides-v1-presentation.md (verdict: REVISE, P0=1, P1=14, P2=7)
  - critique-of-slides-v1-consistency.md (verdict: REVISE, P0=1, P1=2, P2=1)
  - critique-of-slides-v1-fact-checker.md (verdict: APPROVE-WITH-POLISH, P0=1, P1=3, P2=6)
  - critique-of-slides-v1-reader-rendered.md (verdict: APPROVE-WITH-POLISH, P1=3, density 9 slides)
  - critique-of-slides-v1-student-sim.md (verdict: APPROVE-WITH-POLISH, P1 rendering/pacing/designer-extras)
composite_verdict: REVISE
created: 2026-05-22
status: input для slides v2 revision (Phase 8)
---

# SYNTHESIS — slides v1 → slides v2 inputs

> **Composite verdict: REVISE.** 2 critics REVISE (presentation + consistency) wins over 3 APPROVE-WITH-POLISH per CLAUDE.md verdict scale. Presentation critic — 1 P0 Russification + 14 P1 (bright-line ≥5 P1 → REVISE). Consistency critic — 1 P0 PLC compile inversion.
>
> **Strategy:** single batched presentation-designer revision pass per Polish Round Pattern. 3 P0 + ~24 P1 unique addressable в one focused revision pass (~2 ч).

## 1. P0 blockers (3) — MUST fix in v2

| # | Critic | Issue | Fix scope |
|---|---|---|---|
| **P0-R** | presentation | **Russification structural fail:** 282 unique Latin tokens / 424 occurrences outside brand allowlist в rendered PPTX visible body (designer self-report ~140 was 2× understated). Top patterns: throughput loss, sort cost растёт, Surface fouling, Excursion, Verdict, AI accuracy < required tolerance, AI/ML engineer (industrial), Digital twin engineer, Edge AI engineer, GPU micro-servers, advisory, audit, dashboard, deployment, failure, framework, governance, hype, inference, etc. | **Full sed-based Russification pass** + rebuild PPTX. Apply extended replacement table (see Section 5 below). |
| **P0-C** | consistency | **s17 PLC compile message inverted:** «PLC откажется компилировать» contradicts chapter §3.4 explicit «код **скомпилируется** but уйдёт в STOP-mode at runtime» — это инверсия pedagogical message «AI выдаёт правдоподобный код, который компилируется, но не работает». | Update s17 visible body + speaker notes: «PLC скомпилирует код успешно, но в runtime получит STOP-mode из-за illegal address M99999 (max M65535)». Source: chapter-part2.md §3.4. |
| **P0-F** | fact-checker | **s20 Yokogawa cascade-edit gap:** «премия премьер-министра Японии 2023» asserted definitively. Chapter v3 §4.2 ослабило до generic «индустриальные награды» + `[FACT-CHECK]` marker. Slide НЕ synced. | Update s20 visible body + speaker notes к chapter wording «отмечено индустриальными наградами». Drop year + premier-minister specifics. Add inline caveat «pending public verification» если нужно. |

## 2. P1 issues (~24 — high-priority)

### Timing markers leak (ENFORCED — single-issue, multiple instances)
| Slides affected | Issue | Fix |
|---|---|---|
| s01 + s02 (cover) | «75 минут + Q&A» | Remove timing |
| 8 section dividers (s05/s11/s15/s19/s24/s26/s32/s36) | «10 минут», «15 минут — densest failure bucket», «1 слайд · 2 минуты», «5 слайдов · 10 минут» | Remove timing + remove «densest failure bucket» (methodology phrase) |
| s03 lecture-map cards | Per-section timings | Remove timing |

**13 visible timing leaks total.** Per ENFORCED `feedback_no_timing_no_methodology_in_slides` rule. User фиксит это в КАЖДОЙ лекции.

### Hero shortfall + bridge fail
- **P1-H1 s01 hero**: ≈39% area vs ≥40% threshold. Expand to ≥40% (lengthen by 0.5"-1" in either direction).
- **P1-H2 s39 hero CRITICAL**: currently generic Toyota Burnaston factory (Mercedes-style photo) — **NOT bridge к Лекции 13**. Plan v2 explicitly says **Toyota Digit RAV4** humanoid. Re-acquire image: Tier 1 Agility Robotics press kit / Tier 2 Wikimedia Commons «Digit robot» / Tier 3 Toyota newsroom / Tier 4 Reuters YouTube thumb / Tier 5 Wayback / Tier 6 Google Images filtered.

### Schema readability fails
- **s07 4-layer architecture:** Siemens HQ photo dominates, layers tiny. Rebuild — either reduce hero к 30-35% + expand layer cards 65-70%, OR remove Siemens HQ entirely + replace с pure vector diagram.
- **s18 pipeline:** Mixed RU/EN sub-labels — Russify sub-labels.
- **s23 RL/MPC comparison:** Lyapunov + SIL 10⁻⁶..10⁻⁷ small font at 50-min mark — increase font OR split content.
- **s28 ten criteria matrix:** Dense at 60-min — student-simulator suggests split s28a/s28b (5+5 criteria) for lower cognitive load в payoff moment.

### Phantom LO + attribution drift
- **P1-LO8** (consistency): «LO8» appears in 3 speaker notes (s03 + s28 + s39). Chapter declares only LO2/LO5/LO7. **Remove all LO8 mentions** в slides notes.
- **P1-A1 s09 attribution:** «context-clue.com 2026» — chapter v3 corrected к [41] Build in Digital. Update s09 attribution to chapter v3 wording.
- **P1-A2 s09 «5 разных источников данных»:** slide-only specificity vs chapter generic «фрагментированные источники». Either remove or add chapter parity.
- **P1-A3 s37 «снижение downtime 10-30%»:** consolidated-attribution без caveat. Add «по консолидированным отраслевым отчётам» qualifier.

### Visual density (student + reader overlap)
- **9 slides flagged:** s01, s07, s09, s16, s20, s21, s25, s27, s37 (some overlap с schema fails above). Strategies:
  - **Reduce body text** в правой колонке (smaller font OR fewer bullets)
  - **Increase canvas width** для charts (s12, s35 axis label truncation)
  - **Hero re-balance** (s01, s07, s09, s21, s25, s27 — некоторые имеют hero too dominant)

### Other P1
- **s04 keystone:** student-sim wants visual bridge-arrow между A1 и A2 (text-only якорь — нужен shape). Designer addition.
- **«densest failure bucket»** в s26 — methodology phrase, remove.
- **s28 split при 60-min mark** — структурное (book-editor decision OR keep с notes warning?).
- **Small text rendering 7-8 slides:** s01, s07, s09, s20, s21, s25, s27, s37, s39 — body text не читается с превью. If PPTX same — критично для проектора. Increase font ≥18pt для labels per Schema Readability checklist.

## 3. P2 polish (minor — после P0/P1)

- Hero acquisition: s12 BMW=Mercedes weak match, s13 PdM=torpedo backup — re-acquire с better queries
- Chart axis labels truncate в 1334×750 — increase canvas width to 1000px+
- Edge AI / Крайний AI surface form drift — lock single canonical form (chapter §6.3 = «Крайний AI», update s33 visible body match)
- Vendor refs (Jidoka, Wipro PARI, Dell edge, ЦИПР/ИИПРОМ) — add inline caveats
- Freshness flags для NVIDIA Omniverse / Agility Digit (verify day-of)

## 4. Strengths preserved (slides v2 НЕ должна потерять)

- ✅ **Lec-N-1 pattern compliance** (lecture-map s03, 8 section dividers, roadmap-bar discipline, dedicated Q&A merge pattern s31+s39)
- ✅ **Numbers 15/15 PASS** (locked metrics correctly propagated chapter → slides)
- ✅ **39/39 slides derive from chapter** (no orphan slides)
- ✅ **Hero acquisition Tier 2 real images** (21 Wikimedia CC-BY-SA documented в iteration-log)
- ✅ **Schema_matrix s28 100% fill** (designer choice good)
- ✅ **Other designer-extras 0 hits:** «Лектору» / «Вы здесь» / LO codes mostly clean / `lec-NN` / `§X.Y` / `→ sNN` / `[VERIFY-DAY-OF]` (только LO8 phantom — 3 hits in notes, fix below)
- ✅ **Speaker notes 30/39 in 150-300 word range** (8 dividers correctly short)
- ✅ **A0→A3 keystone** works as mental axis (student-simulator: «лучший слайд лекции»)
- ✅ **4 failure cases** technically deep + concrete (s09 Port $12M, s12 vision math, s17 ChatGPT MOV, s22 sim-real T-drift)
- ✅ **s28 10 criteria + s31 5 vendor questions** = карманный payoff-инструмент
- ✅ **s38 4 career roles** — best career-slide (student-simulator preferred)
- ✅ **AI-failure share** доминирует ~28% visual (соответствует 30%-правилу)

## 5. Russification extended replacement table (для P0-R)

Apply via sed pass. Brand allowlist preserved.

| Pattern (visible body) | RU replacement |
|---|---|
| throughput loss | потеря пропускной способности |
| sort cost растёт | растёт стоимость пересортировки |
| Surface fouling | поверхностное загрязнение |
| Excursion | выход за пределы |
| Verdict | вердикт |
| AI accuracy < required tolerance | точность ИИ < требуемого допуска |
| AI/ML engineer (industrial) | инженер ИИ/МО (промышленный) |
| Digital twin engineer | инженер цифровых двойников |
| Edge AI engineer | инженер ИИ на границе сети |
| MES integration specialist | специалист по интеграции MES |
| GPU micro-servers | GPU микросерверы |
| advisory | советующий режим |
| audit (general) | аудит |
| audit trail | журнал аудита |
| dashboard | панель мониторинга / приборная панель |
| deployment | развёртывание |
| failure (general) | сбой / провал |
| framework | каркас / основа |
| governance | управление / руководство |
| hype | завышенные ожидания |
| inference | инференс / вывод (term locked + gloss) |
| accuracy | точность |
| advisory mode | советующий режим |
| production-grade | промышленного класса |
| release | выпуск |
| case (general) | случай / прецедент / кейс (loan OK) |
| shadow mode | теневой режим |
| workflow | рабочий процесс |
| sandbox | песочница |
| sim-to-real | перенос симуляция→реальность |
| closed-loop | замкнутая петля |
| pipeline | конвейер / поток |
| rollback | откат |
| payoff | результат / выигрыш |
| densest failure bucket | плотный блок провалов (или удалить если methodology phrase) |
| Pub/sub broker для тысяч устройств | publish/subscribe брокер (с inline gloss) |
| lightweight | лёгковесный |
| HITL final authority | человек в петле как финальная инстанция (HITL = Human-in-the-Loop) |
| vendor question framework | каркас вопросов вендору |
| GPU micro-servers | GPU-микросерверы (с inline gloss «графические процессоры») |

**Brand allowlist (keep как есть):** Siemens, NVIDIA, Toyota, BMW, Yokogawa, Foxconn, ABB, AVEVA, Cognite, Honeywell, Uptake, Agility Robotics, Jidoka, Wipro PARI, Dell, Schneider, Allen-Bradley, Rockwell, Composer, Omniverse, Cosmos, RAV4, S7-1500, Wikimedia.

**Tech acronyms (with RU расшифровка at first mention):** OPC UA, TSN, MES, SCADA, PLC, MQTT, RL, MPC, IEC, ISO, SAE, FDA, GAMP, ATEX, USP, GMP, IIoT, PdM, HPLC, NAIST, ГОСТ, КИИ, AI/ИИ, ML/МО, OOD.

## 6. Path to APPROVE-CLEAN

After slides v2 revision pass:
1. **Re-spawn presentation-critic** — verify 3 P0 closure + Russification baseline + hero ≥40% + s07 fix + schema readability.
2. **Re-spawn consistency-checker** — verify s17 + LO8 + Yokogawa s20.
3. **Re-spawn fact-checker** — verify cascade-edit closures (s09 + s37 + s20 attribution).
4. **Reader-rendered + student-simulator:** NO re-spawn (verdict already APPROVE-WITH-POLISH, polish addressed в v2).

**Expected v2 verdict:** APPROVE-CLEAN если все 3 P0 + 20+ P1 closed. APPROVE-WITH-POLISH если 1-2 P1 unresolved.

## 7. Estimated revision effort

- **Russification sed pass:** ~30 min (extended replacement table) + rebuild PPTX
- **Timing removal (13 hits):** ~10 min
- **Hero expand s01:** ~10 min (lengthen frame)
- **Hero s39 re-acquire (Toyota Digit):** ~20 min (6-tier search)
- **s07 4-layer rebuild:** ~20 min (reduce Siemens HQ OR replace с pure vector)
- **s17 PLC text fix:** ~5 min (chapter-aligned wording)
- **s20 Yokogawa fix:** ~5 min (drop premier-minister)
- **s28 split decision (5+5 OR keep+notes):** ~10 min
- **s23 density fix:** ~10 min (increase font)
- **LO8 phantom removal (3 notes):** ~5 min
- **s09 + s37 attribution updates:** ~5 min
- **Schema readability fixes (s07, s18, s23, s28):** ~30 min
- **Total:** ~2-3 hours single batched designer revision spawn.

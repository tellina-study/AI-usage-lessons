# Лекция 11 — Content reflection

**Дата:** 2026-05-21
**Issue:** #131

## Финальные 3 артефакта

| Артефакт | Метрика | Качество |
|---|---|---|
| Chapter v5 (3 parts) | 30 930 слов / 1 511 строк / 105 references / 14 Q&A | Глубокий академический textbook-level reference, source-of-truth |
| Slides v2.2 | 41 слайд / 56% media coverage / 61% failure-bucket / Ocean palette / hero ≥40% s01+s39 | Schema readability passes, real Wikimedia images, 0 designer-extras |
| Speech v2 | 5 289 spoken words / 75 мин / 0/41 фрагмент >95 WPM / 14-item pre-flight | Conversational register, smooth transitions, storytelling beats |

## Содержательные сильные стороны

### Keystone — Variant C «Discrete vs Process»
- Двухколонная архитектура с failure-метками под обеими колоннами (Tesla 2018 / F-35 ALIS)
- Единый соединительный пояс «застревание на пилотной стадии 78%/5,5% McKinsey + 95% MIT»
- Confirmed valid обоими critics в Phase 1/3/4c
- НЕ дублирует lec-09 OODA (orthogonal taxonomy vs decision-loop)

### 3 worked examples (рамка-как-фильтр bi-directional)
1. **Pfizer Vox pass** — process, regulated, HITL augmentation copilot (canonical positive)
2. **Авиадвигатель MTBF 8 fail** — data scarcity + SIL 2/DO-178C regulatory blocker + no human escalation room (canonical negative)
3. **Brewery packaging CV-QC pass** — discrete, data abundance, ISO 22000 mild, operator escalation works (canonical positive light)

Bi-directional demonstration LO8 «когда AI не нужен» через 5-step framework filter. Это **сильнее** чем у L4/L5 production (там worked examples менее симметричны).

### 4 категории критериев — 10 + 1 бонус
- Данные (3) / Стоимость (2) / Регуляторика (3) / Человек (2) + 1 бонус SIL 2/3 anti-hype
- Aligned across chapter §4.1 + slide s32 (после Phase 11 fix) + speech §4
- Decision framework actionable

### 5 vendor questions
1. Базовая линия до AI?
2. Окно измерения?
3. Перечень вмешательств?
4. OEE до/после?
5. **3 documented failures за last 24 months в той же индустрии?**

Aligned chapter+slide s35+slide s38+speech. Q5 — самый ценный (отделяет mature vendor от marketing).

### Canonical failure cases
- **Tesla 2018** (Musk «excessive automation was a mistake; humans are underrated») + **2024 retreat from GigaCast single-piece** — двойная отмена в opening hook
- **GE Predix $4B+ writedown** 2017-2019
- **IBM Watson Health** $4B+ → продан за $1.065B Francisco Partners 2022 (Merative)
- **Foxconn Wisconsin** — Walker 13K / Assembly 10K / actual ~281 (NPR) / <1.5K (revised) → Microsoft Fairwater 2024
- **Boeing 737 MAX 9 door plug 2024** — CV inspection как «последняя линия защиты, не первая»
- **F-35 ALIS** $44K/час FY2018 → $35K FY2024 → ODIN replacement (PdM canonical anti-case)
- **Tesla Optimus** 2021 AI Day → 2024 Cybercab teleoperated → 2025-2026 «pilot deployments, не disclosed» (hardware harder than soft AI counter-pattern)
- **GM Hamtramck 1985-1990** predecessor Tesla 2018 (historical canonical)
- **Rethink Robotics Baxter** shutdown 2018 (cobot failure)
- **UAW Stand Up Strike 2023** + technology committee (cultural failure pattern)

10+ canonical failures distributed across §1 (hype-collapse trio + Optimus 4th) / §2 (Tesla + Boeing + GM Hamtramck + Rethink + UAW) / §3 (F-35 ALIS + RL drift + cultural).

### Russian context — verifiable, без overstatement
- Норникель flotation AI — «пилотная / ранняя промышленная стадия, OEE-критерий не верифицируем публично»
- СИБУР маркетплейс «объявлен Q1 2025» (не «launched»)
- ММК / Северсталь / НЛМК Smart Factory programs — generalized claims
- КАМАЗ Маяк-2.5 — М-11 trucks, regulatory status
- Газпром нефть Северо-Соленинское — отдельный кейс (не conflate с Норникель)

Aligned с feedback: РФ context publicly verifiable, no fabrication, anonymization 0 named institutions.

### Quote translations (M3 owner mandate)
5 quotes RU primary на slides + speech:
- Musk April 2018 «Yes, excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.» → «Да, чрезмерная автоматизация на Tesla была ошибкой. Точнее, моей ошибкой. Людей недооценивают.»
- Bainbridge 4 ironies (1983) — все 4 RU primary
- Foxconn Young Liu Computex 2025 «софт выполняет около 80% работы по настройке» — RU primary
- Trump 2018 «8th wonder of the world» → «восьмое чудо света» RU primary
- Toyota GAIA «AI-инструменты для рабочих, не вместо них» — RU primary

Это полезнее для RU аудитории, чем смешанный RU narrative + English quotes (что было анти-паттерном до Phase 8).

## Содержательные слабые стороны / gaps

### 1. Brewery numbers drift caught only на Phase 11.5
**Issue:** Chapter §4.3c имел 30K bph (canonical), но slide s34c v1 + v2 + speech v1 имели 60K bph. Phase 11 speech-writer fixed speech к canonical 30K, presentation-designer parallel scope не touched s34c.  
**Caught:** только independent walkthrough на Phase 11.5.  
**Lesson:** при production worked-example slides, **numbers должны cross-reference к chapter source-of-truth немедленно при добавлении slide**. См. workflow.md + improvements.md.

### 2. «Бонус» numbering inconsistency chapter §5.2 vs speech §5
**Issue:** Chapter §5.2 имел «Бонус — OEE» как 4-й/бонусный вопрос в 5-question list. Speech §5 имел «Четвёртый вопрос — OEE» (numbering different). Methodology-critic поймал в Phase 10.  
**Lesson:** numbering conventions нужно lock на Phase 1 plan + propagate как-is через all 3 artifacts.

### 3. Cornerstones not 100% in slides
**Issue:** Cornerstone «обучение с подкреплением» — chapter имеет 4 mentions full phrase, slides имеют 0 (используют acronym «RL»). Это acceptable per acronym convention, но если для completeness — нужен 1 explicit full-phrase introduction где-то в early slides.  
**Lesson:** «acceptable acronym substitution» — это OK при условии inline gloss первое упоминание. Verify где первое упоминание.

### 4. Hero closing s39 «возьмёмся в скобках в кулак» translation glitch
**Issue:** P2 polish item на s-41 closing hero bottom band — phrasing «возьмёмся в скобках в кулак» — это LLM translation glitch, должно быть «возьмёмся в кулак» или другое idiom.  
**Lesson:** owner Slack-tier polish после GATE C OK; structural P0 caught и closed.

### 5. Tesla Optimus AI Day year inconsistency between artifacts
**Issue:** Speech mentions «AI Day август 2021» (correct initial announcement). Slide s11 mentions «AI Day 2022, 2024, Cybercab». Different events listed, but speech focuses on initial 2021 + slide focuses on demo events 2022/2024.  
**Acceptable:** different scope (announcement vs demo events), не drift. But could be unified.

## Что нужно для следующих лекций

### Pattern carry-forward (positive)
- Variant C-style keystone (two-column taxonomy contrast) works well для отраслевых лекций
- 3 worked examples bi-directional filter — strong pedagogical demonstration
- 4-categories decision framework — actionable artifact студент носит в кармане
- 5 vendor questions — concrete deliverable
- Real Wikimedia CC-BY-SA Tier 2 acquisition — clean licensing pattern

### Anti-patterns to avoid (carry-forward для L10/L12+)
- ❌ Designer self-report trust — always independent verify
- ❌ Parallel revision spawns без cross-artifact alignment requirements — explicit cross-reference
- ❌ Numbers drift в worked examples — chapter is source-of-truth, slide+speech align к нему
- ❌ Hero size self-report — measure independently (PNG inspection + shape coordinates)

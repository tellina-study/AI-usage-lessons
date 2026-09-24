---
lecture_number: 16
title: "AI в нефтегазовой отрасли и добыче ресурсов"
module: 3
class: L4+ (industrial)
duration_min: 75
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
learning_outcomes: [LO1, LO2, LO3, LO7]
status: plan-v2
revision_round: 2
prev_version: plan-v1.md
date: 2026-05-27
issue: 144
keystone_axis: "Variant B — data availability × physics certainty matrix (2×2)"
strict_in_failures_target: 0.35
strict_in_failures_actual:
  slides: "15/43 = 35%"
  minutes: "28.5/75 = 38%"
  words: "~13000/30000 = 43%"
chapter_target_words: 30000
slides_target: 43
qa_buffer_min: 10
media_share_target: 0.50
hero_required: [s01, s40]
---

# Лекция 16: AI в нефтегазовой отрасли и добыче ресурсов — plan v2

## Changelog vs plan-v1

- **P1.1 fix:** добавлены 2 buffer failure slides (s07b Aspen alert fatigue refinery; s38 split — отдельные s37 cyber +935% + s38 2020 crash) → strict-in **15/42 = 36%** slides, **38%** minutes, **43%** chapter words.
- **P1.2 fix:** s05 keystone теперь содержит **inline operational definition** «physics certainty» + «data availability» **на самом слайде**, не defer в speech/chapter.
- **P1.3 fix:** Раздел 5 пересобран на **6 слайдов** (s33-s38): отдельные slides для cyber и 2020 crash; Газпром/Татнефть/ЛУКОЙЛ/Сургутнефтегаз структурно распределены.
- **P1.4 fix:** explicit **10-минутный Q&A buffer** в pacing math (active 65 + Q&A 10 = 75).
- **P1.5 fix:** новая **Vendor → slide / speech-anchor mapping table** в § «Tools-per-quadrant taxonomy» (23+ vendors locked).
- **P1.6 fix:** новый **s12 «Когда AI не нужен в Q1»** с 6 visible bullets — структурные критерии больше не маскируются inline.
- **P1.7 fix (reader-simulator):** новый **s20 «Сокращения метановой MRV»** — alphabet helper slide ДО первого case в Разделе 3.
- **P1.8 fix (reader-simulator):** новое § «Numbers density rule (visible body)» — max 3 striking numbers на visible body slide, остальное в speech / speaker notes; s14 и s33 переписаны под limit.
- **Дополнительные:** Russification glossary расширен (OGMP, SIL, frontier exploration, custody transfer, intensity, plume migration, wildcat, FPSO, PINN, 4D seismic, bopd); Bridger Photonics / SeekOps добавлены в brand allowlist; РГУ Губкина дубликат устранён; 10 `[VFY-day-of]` ранжированы в 3 tier (P2-2 polish included).

## Topics Covered

- **HPC + foundation models Q3:** Aramco METABRAIN (250B, 90 лет, 6k обученных, 430 use cases); SLB Lumi (Sep 2024, Grace Hopper, Aker BP/Shell/Azule); ExxonMobil Discovery 6 (4 032 Grace Hopper, $1B+ unlock 6 FPSO Stabroek); Eni HPC6 (14k MI250X, 606 PFLOPS, Top500 #5, $104M, CCS).
- **Autonomous drilling + production Q1:** Nabors PACE-X (4-mile laterals Bakken/Haynesville/Delaware); Precision Drilling AlphaAutomation; NOV NOVOS; Ambyint InfinityRL (200 wells, +15%); Aspen Mtell (alert fatigue, threshold tuning failures); Honeywell UOP Connect (310+ units); OspreyData; SLB Avocet; Halliburton DecisionSpace.
- **Refinery + pipeline integrity Q1:** Aspen Mtell, Honeywell UOP, Yokogawa OpreX (Idemitsu Japan), ABB Ability Genix, Emerson DeltaV; Enbridge 456 ILI 2024; NDT Global Proton.
- **Methane MRV Q2:** MethaneSAT (Mar 2024 → Jun 2025 loss, Permian 410 t/h = 50% выше EPA); Carbon Mapper Tanager-1 (Aug 2024 Planet Labs+JPL); GHGSat (16 cubesats, 25 m); Bridger Photonics (aerial LiDAR 4× точнее); SeekOps; Project Canary; OGMP 2.0 Level 4/5.
- **Energy transition Q4:** Northern Lights CCS (1.5 Mt/год vs IEA 7.6 Gt = 0.02%, 190× gap); Fervo EGS (IPO May 2026 +331%, Cape Station Utah, 150 GW US potential vs 3.7 GW current = 40× ceiling); Eavor closed-loop; AI data centers как driver.
- **Регуляторика 2024:** EU Methane Reg 2024/1787 (Aug 2024, OGMP L4/5, до 20% penalty, LDAR May 2025); US EPA Subpart W (May 2024 final → Sep 2024 proposed delay до 2034).
- **Россия (sanctions):** Газпром Cognitive Geologist (с IBM Research Brazil 2017-2022 → internal, 3-4 мес → minutes Ямал 2024, +40% projects к 2030); Роснефть Digital Field (Башнефть Илишевское, 23 software); Татнефть АнтиХрупкий, ЛУКОЙЛ, Сургутнефтегаз; AIQ (ADNOC+G42).
- **Провалы и границы (≥33% strict-in):** 86% pilot stuck (McKinsey); BP+Beyond Limits ($20M, vendor pivot 2023); IBM Watson+Repsol Kalimba (wind-down 2022); Cognite IPO postpone; C3.ai O&G declining; MethaneSAT loss; 4× discrepancy; refinery AI stagnation; **Aspen Mtell alert fatigue (s07b)**; 2020 oil crash (107k jobs); cybersecurity ransomware +935%; Deepwater Horizon 2010 alarm bypass (chapter anchor).

## Prerequisites

- **Лекция 15 «AI в энергетике»** — общая шкала автоматизации; AI data centers как driver спроса на 24/7 clean power (bridge к Fervo EGS).
- **Лекция 12 «AI в автоматизации производства и цифровые двойники»** — keystone «Шкала автономии A0→A1→A2→A3»; в нефтегазе digital twin часто = contextualized OT data, а не physics-coupled twin. Используется в анти-хайпе Q1.
- **Лекция 11 «AI в дискретном и процессном производстве»** — keystone «Discrete vs Process»; нефтегаз — pure process с длинными horizons (20-30 лет field life).
- **Общие LO курса:** LO1 (когда применять), LO2 (когда отказаться), LO3 (альтернативные инструменты), LO7 (этика/регуляция/безопасность).
- **Домен-контекст:** скважина, пласт, переработка, СПГ — даётся inline 30-сек примером в s03-s04, не предполагается домен-экспертиза.

## Normative References

- **EU Methane Regulation (EU) 2024/1787** (август 2024, OGMP 2.0 Level 4/5 alignment, до 20% оборота penalty).
- **US EPA Subpart W final rule** (6 мая 2024, satellite quantification разрешена, «other large release events» новая category).
- **US Inflation Reduction Act — Waste Emissions Charge** ($1500/t CH₄ tiered structure planned `[VFY-day-of] Tier-3`).
- **OGMP 2.0 Level 4/5** (UNEP, source-level methane reporting framework).
- **ISA-84 / IEC 61511** (Safety Instrumented Systems — SIL3/SIL4 certification, BOP/PRV/ESD — deterministic, НЕ ML).
- **API standards** (American Petroleum Institute — operational practice references).
- **Минэнерго РФ + Минцифры РФ** — координация digitalization, AI Alliance Russia first industrial member = Газпром нефть.
- **GHGRP** — US EPA mandatory reporting.

Полный библиографический список — Phase 3 fact-check pass; этот plan фиксирует только указатели.

## Materials

- **Hero s01 — Permian Basin VIIRS night satellite** (NASA Earth Observatory / NOAA VIIRS Nightfire, public domain). Foreshadow keystone: visible scale промышленности (2 593 plumes 2024) + measurement story. Acquisition Tier 1. **Fallback A:** Eagle Ford / Bakken VIIRS plumes (NASA Earth Observatory, 2024) — same source family, less catastrophic framing. **Fallback B:** Deepwater Horizon US Coast Guard controlled burn (Tier 1, но «catastrophe-framed» — only if A unavailable).
- **Hero s40 — MethaneSAT first global methane map** (EDF/Google, февраль 2026). Bittersweet payoff: что было обещано, что потеряли, что осталось от mission. Acquisition Tier 1 (recent press release) с Tier 4 (Wayback) fallback. Backup: control room human-in-loop (Tier 3-4).
- **Section dividers (6 штук — Q1/Q3/Q2/Q4/Russia/Closing) — рекомендованные иллюстрации:** Aramco field operation (Q1); Eni HPC6 rack или 4D seismic (Q3); MethaneSAT Permian scene или GHGSat constellation (Q2); Northern Lights Øygarden или Fervo Cape Station drilling (Q4); Газпром Ямал arctic operation или Роснефть Башнефть field (Russia); MethaneSAT global map preview (Closing).
- **Diagrams expected:** keystone 2×2 matrix с inline operational definitions (s05); methane MRV alphabet helper schema (s20); methane detection ladder satellite/aerial/drone/ground OGI (Раздел 3); regulatory timeline EU 2024/1787 + US Subpart W (s26); CCS 190× scale-up gap chart (s31); 4-quadrant × 4-failure synthesis matrix (s39).
- **Stock illustrations:** избегать generic «AI brain» / «hands on keyboard» / Ocean palette mocks. Все иллюстрации через 6-tier acquisition.
- **Chapter assets:** `library/lectures/lec-16/assets/` папка для скачанных изображений + `.url` файлов.

## Learning Objectives

1. **LO16.1.** Объяснить, почему нефтегаз имеет специфический profile для AI: cost asymmetry, sparse data (1 wildcat = $50-100M), long horizons (field life 20-30 лет vs ML model decay 1-2 года), multi-physics constraints.
2. **LO16.2.** Различать 4 структурных места AI по data × physics matrix: Q1 (mature production — multiplier), Q2 (methane MRV — essential), Q3 (frontier exploration — physics-first augmentation), Q4 (energy transition — both struggle, hybrid emerging).
3. **LO16.3.** Назвать 2-3 vendor per квадрант с adoption direction (растёт/стагнирует/discontinued) — без точных volatile долей.
4. **LO16.4.** Привести по 2 successes + 2 documented failures для каждого квадранта; объяснить, почему failure structural (sparse data в Q3, single-point-of-failure в Q2, alert fatigue в Q1, scale-up gap в Q4).
5. **LO16.5.** Сравнить AI-alternative pairs: Eclipse/INTERSECT/CMG vs ML reservoir surrogate; OGI hand-held + Picarro vs satellite AI MRV; classical SCADA + PID + APC vs ML refinery controllers; senior geophysicist vs Foundation Model auto-interpretation.
6. **LO16.6.** Применить критерий «здесь AI не нужен» к **6 конкретным примерам**: BOP/SIS/PRV (SIL3/SIL4); frontier без analog data; OGMP Level 5 (direct measurement); custody transfer metering; stripper wells <10 bopd (unit-economics); mature field + experienced engineers + Eclipse.
7. **LO16.7.** Объяснить регуляторный driver: EU 2024/1787 (до 20% turnover penalty, OGMP Level 4/5) vs US EPA Subpart W (сентябрь 2024 proposed delay до 2034) — почему регуляторика и AI MRV двигаются вместе.
8. **LO16.8.** Сформулировать российскую специфику: sanctions → insourcing → Газпром Cognitive Geo + Роснефть 23 software products + AIQ partnership; что отличается от West.

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

### Ось

**Variant B — двумерная матрица: доступность данных × определённость физики.** Каждый раздел = погружение в один квадрант. Уникальное для нефтегаза: physics-based simulators (Eclipse, INTERSECT, CMG) дольше и серьёзнее, чем у любой другой индустрии курса; sparse data (1 скважина = $50-100M) — структурное, не PR.

### Keystone-слайд — s05 (после s01 hook + s02 cover + s03 about + s04 lecture-map)

- **Заголовок:** «Когда AI работает в нефтегазе? Матрица: данные × физика».
- **1-я строка под title:** «От frontier exploration до methane satellite MRV — AI имеет 4 разных profile».
- **Inline operational definitions (visible body, bottom-left на матрице — обязательно на самом slide, не defer в speech):**
  - **Physics certainty** = есть ли установившаяся численная модель, дающая ground truth с известной точностью. **Q3** (Eclipse / Subsurface-COSCO / OpenFOAM): **да**. **Q2** (methane plume в complex orography, multi-modal fusion): **нет** — atmospheric physics частично закрыта, но cross-source attribution + small-leak quantification — open ML problem.
  - **Data availability** = есть ли достаточно labeled examples для retraining + generalization. **Q1** (1000+ wells Permian как Ambyint): **да**. **Q3** (1 frontier basin без analog wells): **нет**.
- **Визуал:** 2×2 matrix
  - **Y-axis:** Определённость физики (high → low).
  - **X-axis:** Доступность данных (low → high).
  - **Q1 (high data + high physics):** Зрелое месторождение — AI как **multiplier** классических методов. Пример: Ambyint InfinityRL +15% на 200 скважин.
  - **Q2 (high data + low physics):** Метановый MRV — **AI essential** (классической физики для cross-source fusion нет). Пример: MethaneSAT / Carbon Mapper / GHGSat.
  - **Q3 (low data + high physics):** Разведка фронтиров. **Physics-first, AI augmentation.** Пример: Eni HPC6 + Eclipse simulators.
  - **Q4 (low data + low physics):** Energy transition — **и AI, и physics struggle**, hybrid emerging. Пример: Northern Lights CCS, Fervo EGS.
- **Bottom bar:** «За каждым AI deployment — alternative tool: физический симулятор, OGI камера, классическая интерпретация».
- **Notation lock:** Q1=mainstream production, Q2=methane MRV, Q3=frontier exploration, Q4=energy transition. Это codify во всех downstream artifacts.

### Как каждый раздел спускается/возвращается к axis

- **Раздел 1 (Q1):** «Начинаем с самого освоенного квадранта — AI multiplier. Здесь Ambyint, Aspen Mtell, Honeywell UOP. Здесь же — 86% пилотов застряли (McKinsey). Почему работает, и почему всё ещё проваливается на масштабе.»
- **Раздел 2 (Q3):** «Спускаемся в данные-беднейший квадрант — frontier exploration. HPC6, Discovery 6, METABRAIN. Здесь же — BP+Beyond Limits и IBM+Repsol. Почему ML не generalize без analog data.»
- **Раздел 3 (Q2):** «Возвращаемся в data-rich квадрант, но физика разрозненная. AI essential. Здесь же — MethaneSAT loss и 4× discrepancy. Один спутник = single point of failure.»
- **Раздел 4 (Q4):** «Самый честный квадрант — оба измерения low. Northern Lights и Fervo — пытаются, scale-up gap 190× для CCS. Здесь AI hallucinate легко.»
- **Раздел 5 (Россия + cyber + crash):** «Все 4 квадранта в санкционном режиме. SLB Lumi недоступен → Газпром Cognitive Geo. ExxonMobil Discovery 6 недоступен → Eni HPC6 (но в Италии). И cross-cutting risk: ransomware растёт, 2020 crash напоминает что индустриальный цикл > AI hype cycle.»

## Инструменты на каждом уровне таксономии (ENFORCED для отраслевых L4+)

### Q1 (high data + high physics) — Mature production

- **AspenTech (Emerson)** Aspen Mtell — prescriptive maintenance ML, post Emerson $15B acquisition 2025 [VFY-day-of Tier-3]; **растёт**.
- **Ambyint** InfinityRL — RL для rod lift / ESP, **growing в US shale** (Permian, Eagle Ford, Bakken).
- **OspreyData (Mesquite Technologies)** Expert-Augmented ML — independent operators, **mainstream без public KPIs**.
- **SLB Avocet + Lumi** — enterprise tier (NOCs, super-majors).
- **Halliburton DecisionSpace Production** — enterprise tier.
- **Honeywell UOP Connect** — 310+ units / 100+ sites 2024, plan 750+ within year [VFY-day-of Tier-2]; **растёт**.

**Anti-hype:** alert fatigue REAL (vendor «eliminates» = marketing); stripper wells <10 bopd — ROI отрицательный; mode «predictive maintenance» ≠ brand «Aspen Mtell».

### Q3 (low data + high physics) — Frontier exploration + reservoir simulation

- **SLB Lumi** (сентябрь 2024) + Petrel + Delfi — foundation models на NVIDIA Grace Hopper; **leading**.
- **Aramco METABRAIN** — 250B параметров [VFY-day-of Tier-1], 90 лет данных, **внутренний Saudi, не продаётся внешне**.
- **Eni HPC6** — 14 000 MI250X, 606 PFLOPS, **внутренний Italy, $104M capex**.
- **ExxonMobil Discovery 6** — 4 032 Grace Hopper, **внутренний US**.
- **bp + Beyond Limits** — **discontinued / quiet 2022+** (failure case Раздел 2).
- **CMG (IMEX, STARS, GEM)** — physics simulators, **niche но stable**; **alternative tool**.
- **OpenFOAM** — open-source CFD, **academic + early commercial**, **alternative**.

**Anti-hype:** foundation models trained на Permian не generalize на East African Rift; senior geophysicist + классическая интерпретация **остаётся essential**; PINN — research-grade.

### Q2 (high data + low physics) — Methane MRV

- **GHGSat** (Canada) — 16-satellite constellation 2025, 25 m разрешение, **commercial growth**.
- **Carbon Mapper Coalition (Planet Labs + NASA JPL)** — Tanager-1 август 2024, **primary post-MethaneSAT**.
- **EDF MethaneSAT** — **lost June 2025**, single satellite vulnerability lesson.
- **Bridger Photonics** — aircraft Gas Mapping LiDAR, 4× точнее ground OGI, customers Exxon/ConocoPhillips/EOG.
- **SeekOps** — drone-based methane, midstream + utilities.
- **Project Canary** — methane analytics + ESG ratings.
- **Teledyne FLIR + Opgal + Rebellion Photonics** — OGI cameras, **alternative — non-AI** для OGMP Level 5.
- **Picarro + LI-COR** — portable laser analyzers, direct measurement, **alternative**.

**Anti-hype:** один спутник всё не решит (MethaneSAT lesson); satellites не видят small dispersed leaks <10-100 kg/h (~70% US emissions); detection ≠ quantification; ground OGI остаётся standard для localization + EU compliance.

### Q4 (low data + low physics) — Energy transition

- **Northern Lights JV** (Equinor+Shell+TotalEnergies) — 1.5 Mt CO₂/год Øygarden Norway.
- **Aker Carbon Capture** — solvent-based + AI optimization, **растёт**.
- **Fervo Energy** — EGS + fiber optic, **IPO май 2026 +331%**, $206M Cape Station Utah.
- **Eavor Technologies** (Canada) — closed-loop geothermal, **funding rounds**.
- **Sage Geosystems** + **Quaise Energy** — early-stage EGS variants.
- **Eni HPC6** — internal CCS modelling (Q3 vendor doubles в Q4).

**Anti-hype:** 190× scale-up gap CCS; AI plume migration long-term (100 лет) uncertain; geothermal physics + drilling = core, AI = enabler.

### Cross-cutting infrastructure

- **NVIDIA Grace Hopper** (Discovery 6, Lumi, METABRAIN) — **dominant HPC**.
- **AMD MI250X / MI300** (Eni HPC6) — **challenger**.
- **HPE Cray EX235a / EX4000** — integrator.
- **Microsoft Azure** (ExxonMobil, Aramco, Shell), **AWS** (Aker BP, Equinor), **Google Cloud** (Aramco) — hyperscalers.
- **Cybersecurity OT:** Dragos, Claroty, Nozomi Networks — **растёт post-Colonial 2021**.

### Russia-specific

- **Газпром нефть IT** — Cognitive Geologist (internal post-IBM), Cognitive system Ямал 2024.
- **Роснефть** — Digital Field + 23 software products / 10 commercial.
- **AIQ (ADNOC + G42, 51% Presight)** — partnership.
- **Cognitive Pilot (Sberbank + Cognitive Technologies JV)** — primarily ag, transferable к heavy O&G equipment.
- **Татнефть АнтиХрупкий Нижнекамск**, **ЛУКОЙЛ Volga-Ural**, **Сургутнефтегаз** — limited public info [VFY-day-of Tier-3].

### Vendor → slide / speech-anchor mapping (P1.5 ENFORCEMENT)

| Vendor | Q | Slide / speech-anchor | Anti-hype оговорка |
|---|---|---|---|
| Ambyint InfinityRL | Q1 | s09 | +15% на 200 wells = small fleet |
| Aspen Mtell | Q1 | s10 + **s07b** failure | alert fatigue 100s/day; threshold tuning |
| Honeywell UOP / Yokogawa OpreX / ABB Genix | Q1 | s10 | refinery cross-unit stagnation |
| Emerson DeltaV / Honeywell Profit Controller | Q1 alt | s12, s33 | classical APC mature |
| OspreyData / SLB Avocet / Halliburton DecisionSpace / Nabors PACE-X | Q1 | speech-anchor s09 / s10 | independent ops + enterprise + drilling laterals |
| Aramco METABRAIN | Q3 | s14 (numbers-cut) | $1.8B 2024 = 0.4% revenue |
| Eni HPC6 | Q3 | s14 (numbers-cut) | 606 PFLOPS Top500 #5 |
| SLB Lumi | Q3 | s15 | Sep 2024, customer base evolving; mode≠brand |
| ExxonMobil Discovery 6 | Q3 | s16 | $200-400M [VFY Tier-2] |
| BP+Beyond Limits | Q3 fail | s17 | $20M, vendor pivot 2023 |
| IBM Watson+Repsol Kalimba | Q3 fail | s18 | 2014-2022 wind-down |
| Eclipse / INTERSECT / CMG / OpenFOAM | Q3 alt | s19 | physics simulators |
| MethaneSAT | Q2 | s22 + s23 failure | lost June 2025 |
| Carbon Mapper Tanager-1 / GHGSat / Bridger Photonics | Q2 | s24 | post-MethaneSAT primary; constellation; aerial 4× точнее |
| SeekOps / Project Canary | Q2 | speech-anchor s24 | drone midstream + ESG ratings |
| FLIR / Opgal / Picarro / LI-COR | Q2 alt | s27 | ground OGI + portable analyzers |
| Northern Lights CCS | Q4 | s29 | 1.5 Mt vs 7.6 Gt IEA = 0.02% |
| Fervo Energy EGS | Q4 | s30 | 40× growth ceiling [VFY Tier-2] |
| Aker Carbon Capture / Eavor / Sage / Quaise | Q4 | speech-anchor s29/s30 | solvent + early-stage EGS |
| Газпром Cognitive Geo | Russia | s35 | 3-4мес → minutes Ямал |
| Роснефть Digital Field | Russia | s36 | Башнефть 23 software products |
| Татнефть АнтиХрупкий / ЛУКОЙЛ / Сургутнефтегаз | Russia | s36 inline mention | limited public info [VFY Tier-3] |
| Cognitive Pilot (Sberbank+Cog Tech) / AIQ (ADNOC+G42) | Russia | speech-anchor s35/s36 | ag→O&G transferable; $1.4B+ valuation |
| Cognite (Norway) IPO postpone / C3.ai O&G declining | Q1 fail | s11 | pure-play vendor distress |
| NVIDIA / AMD / HPE Cray / Azure / AWS / Google Cloud | Cross | speech-anchor s14/s16 | HPC + hyperscaler stack |
| Dragos / Claroty / Nozomi | Cyber | s37 | defensive AI lag offensive |

**Volatile числа → [VFY-day-of] ranked:**
- **Tier-1 (verify ДО chapter draft):** Aramco METABRAIN parameter count (7B→250B→1T?); US EPA Subpart W status 2026; Aramco $1.8B realized 2024 + $6B cumulative.
- **Tier-2 (verify ДО slides):** ExxonMobil Discovery 6 capex ($200-400M estimate); Cognitive Pilot installations (700+→1700+); GHGSat constellation 16 status; Honeywell UOP 750+ target; Fervo Cape Station capex/timeline; Nabors PACE-X fleet ratio.
- **Tier-3 (day-of):** Aspen Mtell Emerson $15B status; Cognite ARR; IRA Waste Emissions Charge implementation; Татнефть/ЛУКОЙЛ/Сургутнефтегаз specific metrics.

## Outline

### Раздел 0 — Введение + keystone (≈7 минут, s01-s05, 5 слайдов)

- **s01 (hook + hero):** Permian Basin VIIRS night satellite. «Что вы видите? Это нефть и газ, которые мы экспортируем во вселенную бесплатно».
- **s02 (cover / title):** Лекция 16 «AI в нефтегазовой отрасли и добыче ресурсов» — заголовок + дата + audience tag (БЕЗ named institutions).
- **s03 (about / audience):** generic «студенты-инженеры 3 курса (универсальная)»; что узнаете; формат.
- **s04 (lecture-map):** 6 разделов как карта (БЕЗ timing на visible body).
- **s05 (KEYSTONE):** 2×2 matrix data × physics + inline operational definitions «physics certainty» + «data availability» (per P1.2 fix).

### Раздел 1 — Q1: Mainstream production optimization (≈11 минут, s06-s12 + s07b, 8 слайдов)

**Связь с keystone:** «Начинаем с самого освоенного квадранта — данные плотные, физика хорошо изучена. AI здесь — multiplier классических методов, но 86% пилотов застряли.»

- **s06 (section divider):** «Q1 — Mature production: AI как multiplier» + tag «3 working cases · 2 структурных провала». БЕЗ минут.
- **s07 (failure 1):** 86% AI projects в energy не выходят из pilot (McKinsey 2024) + 60% компаний не получают material value (BCG) + 15% live ops / 3% advanced (DNV/Accenture). Структурные причины: 60-80% time = data cleanup; legacy IT integration 3-5×; talent gap; safety culture; slow ROI vs 20-30 лет horizon. Cognite IPO postpone + C3.ai declining inline.
- **s07b (failure 2 — BUFFER, NEW per P1.1):** Aspen Mtell в refinery context — **alert fatigue + threshold tuning failures**. Vendor claim «eliminates alert fatigue»; в поле — 100s alerts/day, операторы re-tune thresholds или ignore. Refinery AI cross-unit orchestration stagnation 2010s-2020s — narrow loops OK, plant-wide stuck. Named operator pilot (per reader-simulator P1 #5): Yokogawa Idemitsu Japan — single distillation column success; **plant-wide pilot 2018+ закрыт quietly** [VFY-day-of Tier-2].
- **s08:** Ambyint InfinityRL — 200 скважин, +15% над per-well historical mean (типичная Permian well 100-500 bopd). RL для rod lift / ESP.
- **s09 (vendors landscape):** Ambyint + OspreyData + SLB Avocet + Halliburton DecisionSpace + Honeywell UOP Connect (310+ units / 100+ sites vs ~700 global refineries). Mode ≠ brand explicit.
- **s10:** Российский case — Роснефть Digital Field Башнефть Илишевское inline (preview Раздела 5): +1 Mt/год (+5.9% от ~17 Mt/год), ~1B руб./год. Aspen Mtell + Honeywell UOP + Yokogawa OpreX + ABB Ability Genix + Emerson DeltaV — vendor landscape.
- **s11 (failure 3 — Cognite/C3.ai inline reinforcement):** Cognite IPO postpone 2023, $94M ARR vs cancelled $2-3B valuation; C3.ai O&G vertical 5.9% FY24 → declining FY25 — pure-play vendor distress.
- **s12 (КОГДА AI НЕ НУЖЕН в Q1 — P1.6 fix, 6 visible bullets):**
  1. Хорошо известная geology + proven reservoir → reservoir simulation classical (Eclipse), не ML.
  2. Stripper wells (<10 bbl/day): cost of AI > value extracted — classical pump rules.
  3. Custody transfer measurement: regulatory mass flow meter required → physics-based metering, не ML.
  4. Blowout prevention (BOP): physics-based deterministic, не probabilistic ML.
  5. Frontier exploration без analog data: нет training set (preview Раздела 2).
  6. EU Methane Reg compliance reporting: traceability mandated — не black-box ML.

### Раздел 2 — Q3: Frontier exploration + reservoir simulation (≈12 минут, s13-s19, 7 слайдов)

**Связь с keystone:** «Спускаемся в data-беднейший квадрант. Каждая wildcat (= разведочная скважина в новом месте) = $50-100M; sample size 1-5 wells. ML не generalize без analog. HPC + foundation models, но physics остаётся ground truth.»

- **s13 (section divider):** «Q3 — Frontier exploration: physics-first, AI augmentation» + tag «3 working cases · 2 провала».
- **s14:** **HPC landscape (numbers-cut per P1.8):** Eni HPC6 — **606 PFLOPS Top500 #5** + **14k AMD MI250X** + **$104M capex**. Aramco METABRAIN — **250B параметров** + **90 лет data** + **$1.8B realized 2024**. (Drop visible: 7T tokens, 6000 employees, 430 use cases, $440B revenue, 2050 timeline → speech only.)
- **s15:** SLB Lumi (сентябрь 2024) — domain foundation models, NVIDIA Grace Hopper, customers Aker BP / Shell / Azule. **Anti-hype:** mode «domain foundation model» ≠ brand «SLB Lumi». Halliburton (frontier classic incumbent) speech-anchor.
- **s16:** ExxonMobil Discovery 6 — 4 032 NVIDIA Grace Hopper, 4× compute vs Discovery 5. **Visible (numbers-cut):** «4D seismic months → weeks» + «$1B+ unlock» + «6 FPSO Stabroek Guyana» (drop ~16B BOE total, ~30-40% capacity → speech). Inline gloss «4D seismic = 3D + time axis».
- **s17 (FAILURE 1):** BP + Beyond Limits ($20M cognitive AI, 2018+). 7 лет публичных результатов нет; Beyond Limits пивотировал в healthcare/manufacturing 2023; BP не обновил кейс после 2019. **Урок:** single-customer concentrated bet; «cognitive AI» — ML marketing 2018; anthropomorphic overpromise.
- **s18 (FAILURE 2):** IBM Watson + Repsol Kalimba (2014-2017+). 30 лет exploration data «analyzed»; конкретных результатов нет; IBM Watson Industry Solutions stagnation 2018-2022; Repsol перешёл на Lumen 2020+. **Урок:** general-purpose «cognitive computing» platforms не scaled в narrow domain; hype cycle 2014-2016 → ≤10% от ожиданий.
- **s19 (ALTERNATIVE):** Eclipse / INTERSECT / CMG (IMEX, STARS, GEM) + OpenFOAM. **Когда AI не нужен:** frontier basin (East African Rift, pre-salt early); senior geophysicist + classical interpretation. ML surrogates accelerate 50-80% но lose physical consistency на extrapolation.

### Раздел 3 — Q2: Methane MRV (≈12 минут, s20-s27, 8 слайдов)

**Связь с keystone:** «Возвращаемся в data-rich квадрант — спутники собирают петабайты в день. Но физика разрозненная: 4 разных sensor modality, methane plume physics не закрыта для cross-source attribution. AI essential. Но один спутник = single point of failure.»

- **s20 (alphabet helper — NEW per P1.7):** «Сокращения метановой MRV» glossary slide ДО первого case. **MRV** = выявление-учёт-проверка; **OGI** = оптическая газовая визуализация (IR-камера); **LDAR** = выявление и устранение утечек (ground programme); **OGMP 2.0** = UNEP-инициатива Level 1-5; **SIL** = уровень целостности безопасности (IEC 61511); **bopd** = баррелей в день; **intensity** = % метана от добытого газа.
- **s21 (section divider mini-recap):** «Q2 — Methane MRV: AI essential + единичная уязвимость» + tag «4 working systems · 2 провала · regulatory pressure».
- **s22:** MethaneSAT (март 2024 запуск EDF + Harvard, первый env-NGO-owned satellite). Permian Basin — **410 t/h = 50% выше EPA estimates** [single striking number per P1.8]. 2 000+ data files, 180+ scenes, 10 публикаций.
- **s23 (FAILURE 1):** MethaneSAT loss 20 июня 2025 — после ~13 месяцев (15% designed lifetime). Single satellite = catastrophic SPOF. Regulatory enforcement (EU 2024/1787) не может опираться на 1 спутник. Constellation модель (GHGSat 16) — better.
- **s24:** Carbon Mapper Tanager-1 (Planet Labs + NASA JPL, 16 августа 2024). GHGSat 16-satellite constellation к 2025, 25 m разрешение. Bridger Photonics aircraft LiDAR — 4× точнее ground OGI. SeekOps + Project Canary speech-anchor.
- **s25 (FAILURE 2):** 4× discrepancy crisis. MethaneSAT measured ~15 Mt vs EPA inventory ~4 Mt = factor 4 gap. Stanford 2024 aerial: 7.5 Mt = factor 2. 9-satellite single-blind 2024: 0 false positives, **58% correctly identified**, 41 false negatives. Гэп structural — industry vs regulator unresolved.
- **s26:** Регуляторика как driver. **EU Methane Regulation 2024/1787** (август 2024): OGMP Level 4/5 mandatory, 4×/год survey, репарация leaks 5-15 дней, до 20% оборота penalty; LDAR deadline 5 мая 2025, отчёты 5 августа 2025. **US EPA Subpart W** 6 мая 2024 final rule → сентябрь 2024 proposed delay до 2034 [VFY-day-of Tier-1].
- **s27 (ALTERNATIVE):** OGI hand-held cameras (Teledyne FLIR GFx320, Opgal EyeCGas) + portable Picarro/LI-COR. EU regulator: ground measurement preferred для compliance. **Когда AI не нужен:** OGMP Level 5 verification (direct measurement required); custody transfer metering (regulatory mass flow meter class 0.2).

### Раздел 4 — Q4: Energy transition CCS + EGS (≈9 минут, s28-s33, 6 слайдов — split per pacing)

Wait — пересчитываю: 6 slides (s28 divider, s29 NL CCS, s30 Fervo EGS, s31 failure CCS scale-up, s32 failure refinery в Q4 frame, s32-alt alternative SIS). Actually: divider + 2 cases + 2 failures + 1 alternative = 6.

**Связь с keystone:** «Самый честный квадрант — оба измерения low. Северная Лайтс CCS — 1.5 Mt/год vs IEA target 7.6 Gt = 0.02%. AI plume migration для 100-летнего horizon — hallucinate легко. Здесь и AI, и физика struggle вместе.»

- **s28 (section divider):** «Q4 — Energy transition: AI и physics struggle вместе» + tag «2 working pilots · 2 структурных провала».
- **s29:** Northern Lights CCS (Equinor + Shell + TotalEnergies JV, launched 2024). 1.5 Mt CO₂/год Øygarden Norway. AI для site selection — 10-15% improved monitoring claim. **Baseline:** vs IEA target 7.6 Gt CO₂/год к 2050 vs current global ~40 Mt/год = **190× scale-up gap**.
- **s30:** Fervo Energy EGS — IPO май 2026 +331% [VFY-day-of Tier-2]. $206M Cape Station Utah. Driver: AI data centers тянут спрос на 24/7 clean power. **Baseline:** target part of 150 GW US EGS potential vs current US geothermal 3.7 GW = **40× growth ceiling**. Eavor + Sage + Quaise speech-anchor.
- **s31 (FAILURE 1):** CCS scale-up gap. 190× needed by 2050 — engineering reality vs policy targets. AI plume migration short-term decent, long-term (100 лет) uncertain. Hallucination risk в LLM-based agents для long-horizon prediction. Gartner 2027: 40% agentic AI projects fail из-за cost overruns + poor risk controls.
- **s32 (FAILURE 2 — refinery в Q4 frame):** Multi-physics constraints (mass + energy + reaction + corrosion) — ML surrogates lose consistency на edge cases. Cross-unit orchestration стагнация. Concrete pilot: Yokogawa Idemitsu single-column success → plant-wide pilot 2018+ quiet shutdown [VFY-day-of Tier-2] (cross-ref s07b).
- **s33 (ALTERNATIVE):** Physics-based simulators + classical APC (Honeywell Profit Controller, Emerson DeltaV) для refinery. OpenFOAM CFD для CCS modelling. **Когда AI не нужен:** safety-critical SIS (Safety Instrumented Systems — BOP, PRV sizing, ESD logic) — SIL3/SIL4 certification = deterministic traceable; AI не certifiable под ISA-84 / IEC 61511.

### Раздел 5 — Россия + cross-cutting (≈11 минут, s34-s38, 5 слайдов — P1.3 fix)

**Связь с keystone (per P2 fix reader-simulator #9):** Mini-matrix recap «Россия по 4 квадрантам» в s34 section divider:
- Q3 Газпром Cognitive Geo заменяет SLB Lumi (sanctions).
- Q2 — no MethaneSAT mission, EU regulator pressure не applies.
- Q1 Роснефть Digital Field в санкционном режиме.
- Q4 — limited CCS / EGS public info.

- **s34 (section divider + Russia↔keystone mapping):** «Россия — sanctions, insourcing, vertical integration по 4 квадрантам» + tag «3 working programs · sanctions context».
- **s35:** Газпром нефть Cognitive Geologist (с IBM Research Brazil 2017-2022, internal post-IBM) — geology 3-4 месяца → minutes. Cognitive system for oil prospecting 2024 — first oil из Ямала. Cut twofold время до первой нефти, +40% projects к 2030. AIQ partnership (ADNOC + G42, 51% Presight 2024, валюация $1.4B+) speech-anchor.
- **s36 (numbers-cut per P1.8):** Роснефть Digital Field — Башнефть Илишевское. **Visible (max 3 numbers):** «23 software products (10 commercial)» + «+1 Mt/год production» + «~1B руб./год». Drop visible: +60% remotely-controlled, +5% energy efficiency, -5% logistics, +5.9% vs ~17 Mt/год → speech only. Sanctions context: после 2022 Roxar / Schlumberger ушли → drive internal dev. Татнефть / ЛУКОЙЛ / Сургутнефтегаз — inline mention с [VFY-day-of Tier-3], Cognitive Pilot (Sberbank+Cog Tech) speech-anchor.
- **s37 (FAILURE — cybersecurity, P1.3 split):** **Cybersecurity counter-trend.** Ransomware attacks on O&G **+935%** между апрелем 2024 и апрелем 2025 (Zscaler). Colonial Pipeline 2021 — VPN без MFA, ~6 дней shutdown. Shell MOVEit 2022 + 2024 vendor compromise. **Урок:** AI добавляет complexity → attack surface растёт. Defensive AI (Dragos, Claroty, Nozomi) отстаёт от offensive AI. Безопасность — phase 1, не phase 4.
- **s38 (FAILURE — 2020 crash + industry cyclicality, P1.3 split + P1.1 BUFFER):** **2020 oil crash контекст**: 107 000 jobs lost март-октябрь 2020 (BP 10 000, Shell 9 000) — **industry cyclicality > AI hype cycle**. Capex digital cuts 2020 → AI projects заморожены на 18-24 месяца. **Урок:** долгосрочный AI roadmap должен выдерживать commodity cycle; AI ROI горизонт 5-7 лет, а crash происходит каждые 7-10 лет. Deepwater Horizon 2010 alarm bypass anchor — chapter deep-dive (cross-ref s33 SIS alternative).

### Раздел 6 — Closing + Q&A (≈10 минут + 10-min Q&A buffer, s39-s42, 4 слайда)

- **s39 (synthesis — 4-quadrant × 4-failures matrix per P1.1 buffer fix):** Возврат к keystone matrix, 4 квадранта с key takeaway + 4 named failures: Q1 → 86% pilot stuck (McKinsey) + alert fatigue (Aspen refinery); Q3 → BP+Beyond Limits + IBM+Repsol; Q2 → MethaneSAT loss + 4× discrepancy; Q4 → 190× CCS gap + refinery plant-wide stagnation. «Когда AI работает: Q1 multiplier + Q2 essential. Когда осторожно: Q3 augmentation only. Когда опасно: Q4 long-horizon + safety-critical SIS.»
- **s40 (closing + hero):** MethaneSAT first global methane map (EDF/Google, февраль 2026). Bittersweet payoff: мы потеряли спутник, но карта осталась. **Bridge к Лекции 17:** «systematization of industry AI — keystone'ы L11-L16 как universal patterns».
- **s41 (Q&A frame):** дедицированный Q&A слайд (БЕЗ «10 минут» visible), 3-5 ключевых вопросов для exit ticket.
- **s42 (sources):** список основных источников + acknowledgements.

**Итого:** 42 slides + Q&A 10-минутный buffer.

**Pacing math (P1.4 fix):**
- Раздел 0: 7 min (5 slides)
- Раздел 1: 11 min (8 slides — includes s07b buffer)
- Раздел 2: 12 min (7 slides)
- Раздел 3: 12 min (8 slides — includes s20 helper)
- Раздел 4: 9 min (6 slides)
- Раздел 5: 11 min (6 slides — Russia + cyber + crash)
- Раздел 6 active: 3 min (s39 synthesis + s40 closing + s41/s42 frame)
- **Q&A buffer: 10 min**
- **Total: 65 active + 10 Q&A = 75 min.**

## Numbers density rule (visible body — P1.8 fix)

**Правило:** на любом visible body slide — **максимум 3 striking numbers**. Остальные numbers → speaker notes / speech / chapter.

**Applied к:**
- **s14 Eni HPC6 + Aramco METABRAIN:** visible — «606 PFLOPS Top500 #5» + «14k AMD MI250X» + «$104M» (Eni) // «250B params» + «90 лет data» + «$1.8B realized 2024» (Aramco). Speech: 7T tokens, 6000 employees, 430 use cases, $440B Aramco revenue, 2050 timeline.
- **s16 ExxonMobil Discovery 6:** visible — «4 032 Grace Hopper» + «$1B+ unlock» + «6 FPSO Stabroek». Speech: 4× compute vs Discovery 5, ~16B BOE total, ~30-40% capacity.
- **s22 MethaneSAT Permian:** visible — «410 t/h = 50% выше EPA» (1 striking + baseline). Speech: 3.6 Mt/год derivation, New Mexico 1.2% vs Texas 3.1% intensity gloss, 2000+ data files.
- **s36 Роснефть Digital Field:** visible — «23 software products» + «+1 Mt/год» + «~1B руб./год». Speech: +60% remotely-controlled, +5% energy efficiency, -5% logistics, +5.9% vs ~17 Mt/год 2023.
- **s24 vendor landscape:** max 3 vendors visible (Carbon Mapper + GHGSat + Bridger Photonics); SeekOps + Project Canary speech-anchor only.

**Cost-of-omission:** reader-simulator: «7 чисел подряд я не запоминаю, выберу одно (50%) и забуду остальное». Numbers density rule — student retention mandate.

## Провалы, ограничения и альтернативы (ENFORCED — strict-in ≥33%, holistic in каждом артефакте)

### Бюджет — P1.1 BUFFER (15 strict-in slides из 42 = 36%)

**Strict-in failure / limit / criterion / alternative slides:**
1. **s07** — 86% pilot stuck (McKinsey/BCG/DNV) — failure.
2. **s07b** — Aspen Mtell alert fatigue + refinery plant-wide stagnation — failure (NEW BUFFER P1.1).
3. **s11** — Cognite IPO postpone + C3.ai O&G declining — failure.
4. **s12** — «Когда AI не нужен в Q1» 6 visible bullets — alternative/criterion (P1.6 promoted).
5. **s17** — BP + Beyond Limits — failure.
6. **s18** — IBM Watson + Repsol — failure.
7. **s19** — Eclipse / INTERSECT / CMG / OpenFOAM + frontier criterion — alternative.
8. **s23** — MethaneSAT loss — failure.
9. **s25** — 4× discrepancy crisis — failure.
10. **s27** — OGI + Picarro/LI-COR + Level 5 / custody criterion — alternative.
11. **s31** — CCS 190× scale-up gap + Q4 hallucination — failure.
12. **s32** — refinery plant-wide stagnation в Q4 frame — failure.
13. **s33** — physics simulator + SIS/SIL3/SIL4 criterion — alternative.
14. **s37** — cybersecurity counter-trend (+935%) — failure (P1.3 split out).
15. **s38** — 2020 oil crash + industry cyclicality — failure (P1.3 split + P1.1 buffer).

**Slides strict-in: 15/42 = 36%** (target ≥33%). Comfortable +6pp buffer.

**Minutes strict-in:**
- Раздел 1 (11 min) — 5 min на s07+s07b+s11+s12 (failure+alternative cluster).
- Раздел 2 (12 min) — 5 min на s17+s18+s19.
- Раздел 3 (12 min) — 6 min на s23+s25+s27.
- Раздел 4 (9 min) — 6 min на s31+s32+s33.
- Раздел 5 (11 min) — 5 min на s37+s38.
- Раздел 6 (3 min active) — 1.5 min на s39 (4× failures synthesis).

**Total strict-in minutes: 5+5+6+6+5+1.5 = 28.5 min из 75 = 38%.** Strong buffer.

**Слова (chapter 30 000 target):**
- §Раздел 1 Q1 failure deep-dive (86% pilot + alert fatigue + Cognite/C3.ai + alternative SCADA + 6 critéria) — ~3 000 слов.
- §Раздел 2 Q3 failure deep-dive (BP/Beyond Limits + IBM/Repsol + Eclipse alternative) — ~3 000 слов.
- §Раздел 3 Q2 failure deep-dive (MethaneSAT loss + 4× discrepancy + OGI alternative + 2 criteria) — ~2 500 слов.
- §Раздел 4 Q4 failure deep-dive (CCS scale-up + refinery stagnation + SIS alternative) — ~2 500 слов.
- §Раздел 5 Cybersecurity + 2020 crash + Deepwater Horizon historical anchor — ~2 000 слов.

**Chapter strict-in total: ~13 000 слов из 30 000 = 43%.** Comfortable.

### Holistic check (per CLAUDE.md решение #78 — strict-in в КАЖДОМ артефакте)

| Артефакт | Strict-in % | Threshold | OK? |
|---|---|---|---|
| Slides | 36% (15/42) | ≥30% | ✅ buffer +6pp |
| Minutes | 38% (28.5/75) | ≥30% | ✅ buffer +8pp |
| Chapter words | 43% (~13k/30k) | ≥30% | ✅ buffer +13pp |
| Speech words (target ~5-6k) | ~40% derived from chapter | ≥30% | ✅ |

**No single-artifact concentration:** failures распределены — R1=4, R2=3, R3=3, R4=3, R5=2, R6=1 (synthesis recap). No cluster gap.

### 10 documented failures и где разбираются

| # | Failure | Где (раздел/слайд) |
|---|---|---|
| 1 | BP + Beyond Limits cognitive AI ($20M, vendor pivot 2023) | Раздел 2 / s17 |
| 2 | IBM Watson + Repsol Kalimba (2014-2022 wind-down) | Раздел 2 / s18 |
| 3 | Cognite IPO postpone ($94M ARR vs $2-3B cancelled) | Раздел 1 / s11 |
| 4 | C3.ai O&G vertical declining (5.9% FY24 → declining) | Раздел 1 / s11 |
| 5 | MethaneSAT loss июнь 2025 (~13 месяцев из 5+ лет) | Раздел 3 / s23 |
| 6 | 86% AI pilot stuck (McKinsey 2024) | Раздел 1 / s07 |
| 7 | Aspen Mtell alert fatigue + refinery plant-wide stagnation | Раздел 1 / s07b (NEW) |
| 8 | 2020 oil crash 107 000 jobs (BP 10k Shell 9k) | Раздел 5 / s38 (split) |
| 9 | Methane MRV 4× discrepancy (EPA 4 Mt vs MethaneSAT 15 Mt) | Раздел 3 / s25 |
| 10 | Cybersecurity ransomware +935% 2024-2025 (Colonial, Shell MOVEit) | Раздел 5 / s37 (split) |

**Bonus historical anchor:** Deepwater Horizon 2010 (alarm bypass + automation + human factors) — chapter deep-dive в §Q4/SIS context, speech-anchor в s38.

### 6 фундаментальных ограничений

| # | Ограничение | Где |
|---|---|---|
| 1 | Sparse data + frontier exploration (1 wildcat = $50-100M, sample 1-5 wells) | s17/s18 + chapter §Q3 |
| 2 | Black-box ML в HSE decisions (нет traceability для SIL3/SIL4) | s33 + chapter §Q4 SIS |
| 3 | Cost asymmetry (cost-optim AI vs safety AI — different ROI structures) | s07 + chapter §intro |
| 4 | Long horizons (20-30 лет field life) vs ML model decay (1-2 года) | s32 + chapter §Q1 TCO |
| 5 | Multi-physics simulation surrogate gap (Eclipse loses consistency на extrapolation) | s19 + chapter §Q3 |
| 6 | LLM hallucination в high-stakes ops + agentic AI (Gartner 40% fail 2027) | s31 + chapter §Q4 |

### 6 структурных критериев «здесь AI не нужен» (P1.6 fix — все visible bullets, не inline)

| # | Критерий | Где (visible structural, не inline) |
|---|---|---|
| 1 | Mature field + experienced engineers — Eclipse + senior team | s12 bullet 1 |
| 2 | Safety-critical SIL3/SIL4 (BOP / PRV / ESD logic) — deterministic mandatory | s33 + s12 bullet 4 |
| 3 | OGMP Level 5 compliance — direct measurement required, не AI estimate | s27 + s12 bullet 6 |
| 4 | Frontier exploration без analog data (East African Rift, pre-salt early) | s19 + s12 bullet 5 |
| 5 | Stripper wells <10 bopd — ML deployment ROI отрицательный | **s12 bullet 2** (promoted visible) |
| 6 | Custody transfer metering — regulatory mass flow meter required | **s27 + s12 bullet 3** (promoted visible) |

### 6 alternative (не-AI / другой класс AI) инструментов

| # | Alternative | vs AI tool |
|---|---|---|
| 1 | Eclipse / INTERSECT / CMG / OpenFOAM physics simulators | vs ML reservoir surrogate (s19) |
| 2 | OGI hand-held (FLIR/Opgal) + Picarro/LI-COR portable | vs satellite AI MRV (s27) |
| 3 | Senior geophysicist + classical seismic interpretation (Kingdom, Petrel manual) | vs Foundation Model auto-interpretation |
| 4 | Classical SCADA + PID + APC (Honeywell Profit Controller, Emerson DeltaV) | vs ML refinery controllers (s12, s33) |
| 5 | SIS (SIL3/SIL4 certified deterministic + redundant 3oo2) | vs ML safety logic (s33) |
| 6 | Federated learning + differential privacy | vs centralized AI (cross-operator competition) — chapter §Q1 cross-cutting |

## Assessment

### Exit ticket (Q1-Q3)

- **Q1.** Для какого квадранта data × physics matrix AI является essential (а не augmentation)? Конкретный case + почему классической физики недостаточно.
  - *Expected:* Q2 (high data + low physics) — methane MRV; MethaneSAT/Carbon Mapper/GHGSat. Cross-source data fusion (satellite + aerial + ground OGI) не имеет классического physics-based решения; atmospheric methane physics частично закрыта, но fusion модальностей + small-leak attribution — open ML problem.

- **Q2.** Приведите 2 documented failure из лекции + выученные уроки.
  - *Expected (любые 2 из 10):* BP+Beyond Limits, IBM Watson+Repsol, MethaneSAT loss, 86% pilot stuck, Aspen Mtell alert fatigue, 4× discrepancy, CCS scale-up gap, refinery plant-wide stagnation, 2020 oil crash + capex cuts, cybersecurity +935%.

- **Q3.** Когда в нефтегазе НЕ применять AI — назовите 3 критерия с примерами из 6 на лекции.
  - *Expected:* (а) safety-critical SIS — SIL3/SIL4 deterministic mandatory под ISA-84/IEC 61511; (б) frontier exploration без analog — ML не generalize, senior geophysicist + classical interpretation; (в) OGMP Level 5 compliance + custody transfer — regulator требует direct measurement.

### Bonus вопросы (для seminar)

- **Q4.** Сравните Eni HPC6 ($104M, 14k AMD MI250X, Italy) vs ExxonMobil Discovery 6 (~$200-400M [VFY], 4k NVIDIA Grace Hopper, US) vs Aramco METABRAIN (250B params, internal Saudi). Разные стратегии.
- **Q5.** Почему MethaneSAT factor 4 discrepancy с EPA inventory — structural gap, а не «AI ошибается»? Stanford 2024 aerial (7.5 Mt = factor 2) добавляет?
- **Q6.** Российский case: Газпром Cognitive Geo (геология 3-4 мес → minutes) — implementation Q3 frontier exploration AI, но в санкционном режиме. Что отличает Russia от Saudi/US?

## Анонимизация (ENFORCED — Лекция 9 lesson)

- Frontmatter `audience` строго **«студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)»** — НЕ упоминать МГТУ / Бауман / ИУ-N / Кафедра / ВКА Можайского / МАИ / СПбГУ / **РГУ нефти и газа (РГУ Губкина) / Тюменский ГНГУ / любые отраслевые нефтегазовые ВУЗы** (P2-1 consolidate) / Сколтех / МФТИ / МГУ.
- **Career section в chapter:** «нефтегазовые компании (национальные и частные) + сервисные подрядчики + регуляторы (Минэнерго, Минприроды, EPA, EU Commission) + НИИ + операторы данных» — generic. Российские operators — case studies, не «места работы выпускников».
- **Эталон:** lec-03 / lec-05 / lec-07 — 0 named institutions. Цель для lec-16 — 0 named educational institutions.

## Russification visible body (ENFORCED — расширен per reader-simulator P2 #7)

### Top replacements для Лекции 16 (45+ entries — каждый producer prompt MUST include)

| Англицизм | RU замена |
|---|---|
| foundation model / domain foundation model | большая универсальная / отраслевая большая модель |
| reservoir simulation / seismic interpretation / 4D seismic | пластовое моделирование / интерпретация сейсмики / 4D-сейсмика (3D + ось времени) |
| predictive / prescriptive maintenance | прогностическое / предписывающее обслуживание |
| alert fatigue | усталость операторов от ложных тревог |
| methane MRV / OGI / OGMP 2.0 / LDAR | выявление-учёт-проверка метановых выбросов / оптическая газовая визуализация (IR-камера) / UNEP-инициатива Level 1-5 / программа выявления и устранения утечек |
| downhole / upstream / midstream / downstream | внутрискважинный / добыча / транспорт / переработка (inline gloss первое упоминание) |
| frontier exploration / basin / play / wildcat (well) | разведка фронтиров / нефтегазоносный бассейн / тип залежи / разведочная скважина в новом месте |
| mature field / stripper well / bopd | зрелое месторождение / истощённая скважина (<10 баррелей/день) / баррелей в день |
| ESP / rod pump / gas lift | электроцентробежный насос (ЭЦН) / штанговый насос / газлифт |
| FPSO / custody transfer / plume migration | плавучая платформа добычи-хранения-выгрузки / передача товарной нефти / распространение облака (CO₂ / метана) |
| intensity (methane) | метановая интенсивность (% от добытого газа) |
| SIL3 / SIL4 / BOP / PRV / ESD / SIS / APC | уровень целостности безопасности IEC 61511 / противовыбросовый превентор / предохранительный клапан / аварийный останов / приборная система безопасности / продвинутое управление процессом |
| HPC / NOC / IOC / CCS / EGS | высокопроизводительные вычисления / национальная / международная нефтяная компания / улавливание и хранение углерода / улучшенные геотермальные системы |
| pilot purgatory / ground truth | застрявшие в пилоте / эталонная разметка |
| black-box / hallucination / human-in-the-loop | непрозрачная модель / галлюцинация / человек в петле принятия решений |
| digital twin / multi-sensor fusion / automation bias | цифровой двойник / слияние нескольких сенсоров / склонность доверять автомату |
| greenwashing / shut-in / curtailment / PINN | показная зелёность / консервация / ограничение добычи / физико-информированная нейросеть (research-grade) |
| edge case / compliance / carbon accounting / decision-support | краевой случай / соответствие нормам (комплаенс) / углеродный учёт / поддержка принятия решений |

### Brand allowlist

- **Companies:** SLB, Halliburton, Baker Hughes, NVIDIA, AMD, HPE Cray, Microsoft Azure, AWS, Google Cloud, Aramco, ADNOC, BP, Shell, ExxonMobil, Chevron, ConocoPhillips, Repsol, Eni, Equinor, TotalEnergies, Aker BP, Bridger Photonics, SeekOps, Project Canary, Газпром нефть, Роснефть, Татнефть, ЛУКОЙЛ, Сургутнефтегаз.
- **Products:** Eclipse, INTERSECT, Petrel, Delfi, Lumi, METABRAIN, Aspen Mtell, aspenONE, DeltaV, Ability Genix, OpreX, PACE-X, AlphaAutomation, NOVOS, FlexRig, Cognite Data Fusion, Discovery 6, HPC6, MethaneSAT, Tanager-1, Carbon Mapper, GHGSat, OGI, OGMP, FLIR GFx320, Opgal EyeCGas, Rebellion Photonics, Picarro, LI-COR, InfinityRL, Avocet, DecisionSpace, Beyond Limits, Watson, Northern Lights, Aker Carbon Capture, Fervo, Eavor, Sage Geosystems, Quaise.
- **Standards:** SIL3, SIL4, OGMP 2.0, EU 2024/1787, Subpart W, EPA Method 21, ISA-84, IEC 61511, GHGRP.
- **Russian products:** Cognitive Geologist, Cognitive Geo, Cognitive Agro Pilot, AIQ (ADNOC+G42), Digital Field, Илишевское, Ямал, АнтиХрупкий завод, Roxar.

### Pre-GATE check (ENFORCED)

Deep latin-token scan (не только pattern grep) перед каждым USER GATE. `unique - whitelist = ∅` для narrative body. См. `tools/presentation-build/README.md` §5.8.

## Hero illustrations (ENFORCED)

### s01 — Permian Basin VIIRS night satellite (NASA Earth Observatory / NOAA, public domain)

- **Foreshadow keystone:** visible scale промышленности (2 593 plumes 2024) + measurement story → Q2 methane MRV.
- **Acquisition Tier 1.** Attribution: «NASA Earth Observatory / VIIRS / NOAA, 2024». ≥40% area.
- **Fallback A:** Eagle Ford / Bakken VIIRS plumes (NASA, 2024) — same source family.
- **Fallback B:** Deepwater Horizon US Coast Guard controlled burn (только если A unavailable; «catastrophe-framed» caveat).

### s40 — MethaneSAT first global methane map (EDF + Google, февраль 2026)

- **Bridge к Lec-17:** карта показывает измеримость на глобальном уровне как payoff of AI MRV era; и одновременно single point of failure.
- **Acquisition Tier 1** (Inside Climate News февраль 2026; EDF release) + **Tier 4** (Wayback). Attribution: «EDF / MethaneSAT data via Google Earth Engine, февраль 2026».
- **Backup:** modern oil&gas control room с human-in-loop + AI screens (Tier 3-4).

### НЕ подходит для s01 / s40

Stock «hands on keyboard» / «AI brain» / plain Ocean card с verbatim headline (mock — FAIL) / vendor logo / render не-существующего объекта.

## 6-tier image acquisition + media coverage plan

**Target: 31 из 42 slides с media (74%).** Per-slide tier+source:

**Tier 1 (public domain / direct download):** s01 Permian VIIRS night (NASA Earth Observatory); s22 MethaneSAT Permian scene (MethaneSAT data preview); s27 FLIR GFx320 + Picarro (Teledyne FLIR + Picarro product pages); s37 Colonial Pipeline + Zscaler chart (Colonial news + Zscaler report); s40 MethaneSAT global methane map (Inside Climate News Feb 2026 + EDF, T4 Wayback fallback).

**Tier 3 (press kits / case studies):** s07b Aspen Mtell + Yokogawa Idemitsu; s08 Ambyint InfinityRL rod lift; s09 Honeywell UOP refinery vendor collage; s10 Роснефть Башнефть field + Aspen; s14 Eni HPC6 racks + Aramco METABRAIN; s15 SLB Lumi launch (Sep 2024); s16 ExxonMobil Discovery 6 + Guyana FPSO (HPE blog + Exxon); s19 Eclipse / INTERSECT visualization; s23 MethaneSAT loss timeline (EDF updates); s24 Carbon Mapper Tanager-1 + GHGSat (press kits); s29 Northern Lights Øygarden terminal; s30 Fervo Cape Station drilling; s32 Yokogawa OpreX Idemitsu; s35 Газпром Ямал operation; s36 Роснефть Digital Field schematic; s38 2020 oil crash chart (Reuters/BLS data).

**Tier 5 (Wayback Machine):** s17 BP + Beyond Limits archived (2018-2019 snapshot); s18 IBM Watson + Repsol archived (2014-2016).

**Self-render (drawio / chart):** s05 keystone matrix; s07 86% pilot bar chart; s20 alphabet helper schema; s25 4× discrepancy comparison; s26 EU 2024/1787 + EPA Subpart W timeline; s31 CCS 190× scale-up chart; s34 Russia↔keystone mini-matrix; s39 4×4 synthesis matrix.

**Total media: 22 real photos + 9 self-rendered = 31 / 42 = 74% visual.** Hits ≥50% comfortably.

### Per-image acquisition log mandatory

Per `feedback_no_mock_fallbacks`:
1. Source URL. 2. License attribution. 3. Date acquired. 4. Fallback reason (if used). 5. Storage: `library/lectures/lec-16/assets/screenshots/sNN-real-source.png` + `.url` файл.

**Anti-pattern reminder (Лекция 8):** 16 stylized mocks прошли «87.2% coverage» self-report → owner reject. Orchestrator визуально verify sample 5 slides на Pre-USER-GATE B.

## Open questions / `[VFY-day-of]` (ranked — P2-2 polish)

**Tier-1 (verify ДО chapter draft):**
1. Aramco METABRAIN parameter count (7B март 2024 → 250B → claim 1T 2025).
2. US EPA Subpart W status на 2026-05-27 (final мая 2024 → September 2024 delay → Trump admin 2025+).
3. Aramco $1.8B realized 2024 + $6B 2023-24 cumulative (self-reported, methodology).

**Tier-2 (verify ДО slides):**
4. ExxonMobil Discovery 6 capex ($200-400M estimate by analogy).
5. Cognitive Pilot installations (700+ 2021 → 1700+ к 2024).
6. GHGSat constellation 16 satellites status.
7. Honeywell UOP Connect 750+ within year target achievement.
8. Yokogawa Idemitsu plant-wide pilot shutdown year (claim 2018+).
9. Fervo IPO май 2026 +331% confirmed.
10. Nabors PACE-X fleet ratio из 75+ rigs.

**Tier-3 (day-of):**
11. Aspen Mtell Emerson $15B acquisition status.
12. Cognite ARR 2024 → 2026 trajectory.
13. US IRA Waste Emissions Charge $1500/t implementation.
14. Татнефть / ЛУКОЙЛ / Сургутнефтегаз specific deployment metrics.

## Notes для downstream phases

- **Phase 2 (book-editor):** chapter ≥30 000 слов; multi-part split на 4 файла (chapter.md + chapter-part2-4.md, каждый ≤600 строк, 7-8k слов). **Slide-маркеры `[for-slide-sNN]`** mapping (P2-4): §intro → s01-s05; §Q1 → s06-s12 + s07b; §Q3 → s13-s19; §Q2 → s20-s27; §Q4 → s28-s33; §Russia → s34-s38; §Closing → s39-s42.
- **Inline gloss policy (P2-7):** first appearance каждого of {wildcat, FPSO, 4D seismic, plume migration, downhole, basin/play, stripper well, bopd, intensity, PINN, OGI, OGMP, LDAR, MRV, SIL3/SIL4, BOP/PRV/ESD/SIS, APC, ESP} — inline one-line gloss; Russification table = RU translation.
- **Phase 3 (methodology-critic + fact-checker):** word count <28 500 = P0 BLOCKING; failure-share <30% в одном из 3 артефактов → REVISE; baseline check sample 5-7 measurable claims; `[VFY-day-of]` resolution per Tier ranking.
- **Phase 5 (designer):** Lec-15 reference read mandatory; visual-loop 3× per slide minimum; deep latin-token scan на final pptx; hero verification s01 + s40; **Numbers density rule** (max 3 striking numbers visible per slide).
- **Phase 9 (speech-writer):** 5-6k слов conversational; chapter-derived; no «методически важно» / «на этом этапе студент» / timing markers в visible speech; speech-anchor для vendors не на visible slide (per Vendor mapping) с explicit `[FACT-CHECK]` marker.
- **Pre-USER-GATE A/B/C:** failure-share check (36% slides safe buffer) + baseline coverage + designer-extras grep + hero check + deep latin-token scan + real-image verification sample.

## Risks / concerns

### Risk 1 + 2 (RESOLVED v2): Q2/Q3 physics certainty + failure buffer

P1.2 fix → operational definition inline на s05 (не defer в speech). P1.1 fix → 15/42 = 36% strict-in (+6pp buffer). Methodology-critic Phase 7 проверит обе.

### Risk 3 (MEDIUM): Volatile numbers `[VFY-day-of]` count

14 markers ranked в 3 tiers. Tier-1 (3 markers) MUST resolve ДО chapter draft. Mitigation: Phase 3 fact-checker priority list; backup formulations (e.g., «250B params по состоянию на конец 2024 — claim для 2025 не аудирован»).

### Risk 4 (MEDIUM — NEW): Russia↔keystone mini-matrix (s34)

Mini-matrix recap новый element, может перегрузить divider slide. **Mitigation:** designer Phase 5 visual-loop читабельность; fallback — drop mini-matrix, keep textual cue «Россия по 4 квадрантам».

### Risk 5 (LOW — NEW): s07b «Yokogawa plant-wide shutdown» fact-check gap

«Yokogawa Idemitsu plant-wide pilot 2018+ закрыт» — failure inference от refinery AI stagnation pattern. **[VFY-day-of Tier-2]**. Degrade fallback: generic «refinery plant-wide AI pilots 2018-2024 quietly shut down, named cases — Phase 3 verify».

---

**Final sanity check:**
- Slides **42** (range 41-43 OK для L4+); minutes **75** (65 active + 10 Q&A buffer); hero s01 + s40.
- Strict-in failures: **15/42 = 36% slides, 38% minutes, 43% chapter words** — все 3 артефакта comfortably above 30%, no single-artifact concentration.
- Russification 45+ entries; Brand allowlist consolidated (Bridger Photonics + SeekOps added); anonymization clean (РГУ дубликат устранён); 23+ vendors locked в slide-or-speech mapping.

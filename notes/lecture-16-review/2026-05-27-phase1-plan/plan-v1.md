---
lecture_number: 16
title: "AI в нефтегазовой отрасли и добыче ресурсов"
module: 3
class: L4+ (industrial)
duration_min: 75
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
learning_outcomes: [LO1, LO2, LO3, LO7]
status: plan-v1
date: 2026-05-27
issue: 144
keystone_axis: "Variant B — data availability × physics certainty matrix (2×2)"
strict_in_failures_target: 0.30
chapter_target_words: 30000
slides_target: 40
media_share_target: 0.50
hero_required: [s01, s39]
---

# Лекция 16: AI в нефтегазовой отрасли и добыче ресурсов — plan v1

## Topics Covered

- **HPC + foundation models в E&P (Q3):** Aramco METABRAIN (250B параметров, 90 лет данных, 6 000 обученных сотрудников, 430 use cases), SLB Lumi (сентябрь 2024, domain foundation models на NVIDIA Grace Hopper), ExxonMobil Discovery 6 (4 032 Grace Hopper, 4D-сейсмика месяцы → недели, $1B+ unlock на 6 FPSO Stabroek), Eni HPC6 (14 000 AMD MI250X, 606 PFLOPS, Top500 #5, $104M, CCS modelling).
- **Autonomous drilling (Q1):** Nabors PACE-X (4-mile laterals Bakken/Haynesville/Delaware, 20 000 ft Haynesville lateral, 32 000 ft total depth), Precision Drilling AlphaAutomation, NOV NOVOS — autonomy без full-unmanned promise.
- **Production optimization (Q1):** Ambyint InfinityRL (200 wells, +15% production), Aspen Mtell (10 days production saved, alert fatigue caveat), Honeywell UOP Connect (310+ units, 100+ sites), OspreyData, SLB Avocet/Halliburton DecisionSpace.
- **Methane MRV (Q2):** MethaneSAT (март 2024 запуск → 20 июня 2025 потеря контакта; Permian 410 t/h = 50% выше EPA; 4× гэп US-wide), Carbon Mapper Tanager-1 (Planet Labs + JPL, август 2024), GHGSat (16 cubesats к 2025, 25 m разрешение), Bridger Photonics (aerial 4× точнее ground OGI), Project Canary, OGMP 2.0 Level 4/5.
- **Energy transition (Q4):** Northern Lights CCS (Equinor+Shell+TotalEnergies JV, 1.5 Mt CO₂/год vs IEA target 7.6 Gt = 0.02% needed), Fervo Energy EGS (IPO май 2026 +331%, $206M Cape Station Utah, 150 GW US potential vs current 3.7 GW = 40× growth), Eavor closed-loop, AI data centers как driver спроса на 24/7 clean power.
- **Регуляторика 2024 как driver:** EU Methane Regulation 2024/1787 (август 2024, OGMP 2.0 Level 4/5, до 20% turnover penalty, LDAR 5 мая 2025, отчёты 5 августа 2025), US EPA Subpart W (6 мая 2024 final rule, в сентябре 2024 proposed delay до 2034 — Trump-эра нестабильность).
- **Refinery + downstream (Q1):** Aspen Mtell, Honeywell UOP, Yokogawa OpreX (Idemitsu Japan demonstration), ABB Ability Genix, Emerson DeltaV — стагнация cross-unit orchestration, успех на narrow loops.
- **Pipeline integrity (Q1):** Enbridge 456 ILI 2024, NDT Global Proton, Integrity Engine + Energy Optimizer на Azure.
- **Россия — отдельный режим:** Газпром нефть Cognitive Geologist (с IBM Research Brazil, геология 3-4 месяца → минуты, Ямал 2024, +40% projects к 2030), Роснефть Digital Field (Башнефть Илишевское, 23 software products / 10 commercial, +1 Mt/год, ~1B руб./год), Татнефть АнтиХрупкий Нижнекамск, ЛУКОЙЛ, Сургутнефтегаз, AIQ partnership (ADNOC+G42).
- **Провалы и границы (≥30%):** 86% AI projects pilot stuck (McKinsey/BCG), BP+Beyond Limits ($20M cognitive AI, vendor pivot), IBM Watson+Repsol Kalimba (2014-2017+, тихо закрылся), Cognite IPO postpone, C3.ai O&G vertical declining (5.9% FY24 → declining), MethaneSAT loss, методологический 4× гэп MRV, refinery AI стагнация, 2020 oil crash (107k jobs lost), Deepwater Horizon 2010 alarm bypass.
- **Cybersecurity counter-trend:** ransomware +935% между апрелем 2024 и апрелем 2025 (Zscaler), Colonial Pipeline 2021 (VPN без MFA), Shell MOVEit 2022.

## Prerequisites

- **Лекция 15 «AI в энергетике»** — общая шкала автоматизации в сетях/генерации; AI data centers как driver спроса на 24/7 power (ссылка на Fervo Energy EGS bridge).
- **Лекция 12 «AI в автоматизации производства и цифровые двойники»** — keystone «Шкала автономии A0→A1→A2→A3»; в нефтегазе digital twin часто = contextualized OT data, а не physics-coupled twin. Используется в анти-хайпе Q1.
- **Лекция 11 «AI в дискретном и процессном производстве»** — keystone «Discrete vs Process» соотношение; нефтегаз — pure process с длинными horizons (20-30 лет field life).
- **Общие LO курса:** LO1 (когда AI применять), LO2 (когда отказаться), LO3 (альтернативные инструменты), LO7 (этика/регуляция/безопасность).
- **Минимальный домен-контекст:** что такое скважина, пласт, переработка, СПГ — даётся 30-сек примером в s03-s04, не предполагается домен-экспертиза.

## Normative References

- **EU Methane Regulation (EU) 2024/1787** (август 2024, OGMP 2.0 Level 4/5 alignment, до 20% годового оборота penalty).
- **US EPA Subpart W final rule** (6 мая 2024, satellite quantification разрешена, «other large release events» новая category).
- **US Inflation Reduction Act — Waste Emissions Charge** ($1500/t CH₄ tiered structure planned `[VFY-day-of]`).
- **OGMP 2.0 Level 4/5** (UN Environment Programme, source-level methane reporting framework).
- **ISA-84 / IEC 61511** (Safety Instrumented Systems — SIL3/SIL4 certification, BOP/PRV/ESD — deterministic, НЕ ML).
- **API standards** (American Petroleum Institute — operational practice references).
- **Минэнерго РФ + Минцифры РФ** — координация digitalization, AI Alliance Russia first industrial member = Газпром нефть.
- **GHGRP (Greenhouse Gas Reporting Program)** — US EPA mandatory reporting.

Полный библиографический список — Phase 3 fact-check pass; этот plan фиксирует только указатели.

## Materials

- **Hero s01 — Permian Basin VIIRS night satellite** (NASA Earth Observatory / NOAA VIIRS Nightfire, public domain). Foreshadow keystone: visible scale промышленности (2 593 plumes 2024) + measurement story. Acquisition Tier 1.
- **Hero s39 — MethaneSAT first global methane map** (EDF/Google, released February 2026). Bittersweet payoff: что было обещано, что потеряли, что осталось от mission. Acquisition Tier 1 (recent press release) с Tier 4 (Wayback) fallback. Backup s39: control room human-in-loop (Tier 3-4).
- **Section dividers (5 штук) — рекомендованные иллюстрации:**
  - Q1 (mainstream production): Aramco полевая операция или ESP схема.
  - Q3 (frontier exploration): Eni HPC6 rack photo или 4D seismic visualization (ExxonMobil).
  - Q2 (methane MRV): MethaneSAT Permian scene или GHGSat constellation diagram.
  - Q4 (energy transition): Northern Lights Øygarden terminal или Fervo Cape Station drilling site.
  - Россия: Газпром нефть Ямал arctic operation или Роснефть Башнефть field.
- **Diagrams expected:**
  - Keystone 2×2 matrix (data × physics) — s05.
  - Value chain map (upstream / midstream / downstream / ESG) с AI hotspots — s06 или s07 как поддержка keystone.
  - Time-scale ladder (decades / years / hours / seconds) — optional anchor для Раздел 1 anti-hype.
  - Methane detection ladder (satellite / aerial / drone / ground OGI) — Раздел 3.
  - Deepwater Horizon alarm-bypass diagram — Раздел 1 anti-hype или Раздел 6 closing если фокус на safety.
- **Stock illustrations:** избегать generic «AI brain» / «hands on keyboard» / Ocean palette mocks. Все иллюстрации через 6-tier acquisition.
- **Chapter assets:** `library/lectures/lec-16/assets/` папка для скачанных изображений + `.url` файлов с источниками.

## Learning Objectives

1. **LO16.1.** Объяснить, почему нефтегаз имеет специфический profile для AI: cost asymmetry (cost-optimization vs safety), sparse data (1 wildcat = $50-100M), long horizons (field life 20-30 лет vs ML model decay 1-2 года), multi-physics constraints (fluid+heat+chemistry+geomechanics).
2. **LO16.2.** Различать 4 структурных места AI в нефтегазе по data × physics matrix: Q1 (mature production — AI multiplier), Q2 (methane MRV — AI essential), Q3 (frontier exploration — physics-first AI augments), Q4 (energy transition — both struggle, hybrid emerging).
3. **LO16.3.** Назвать 2-3 vendor per квадрант с adoption direction словами (растёт/стагнирует) — без точных volatile долей: SLB Lumi + Aramco METABRAIN (Q3); MethaneSAT/Carbon Mapper/GHGSat (Q2); Aspen Mtell + Ambyint + Honeywell UOP (Q1); Northern Lights + Fervo Energy (Q4).
4. **LO16.4.** Привести по 2 successes + 2 documented failures для каждого квадранта; объяснить, почему failure не one-off, а structural (sparse data в Q3, single-point-of-failure в Q2, alert fatigue в Q1, scale-up gap в Q4).
5. **LO16.5.** Сравнить AI-alternative pairs: Eclipse/INTERSECT/CMG vs ML reservoir surrogate; OGI hand-held cameras + portable Picarro vs satellite AI MRV; classical SCADA + PID + APC vs ML refinery controllers; senior geophysicist + classical interpretation vs Foundation Model auto-interpretation.
6. **LO16.6.** Применить критерий «здесь AI не нужен» к 3-4 конкретным примерам: BOP/SIS/PRV (SIL3/SIL4 deterministic mandatory); frontier exploration в East African Rift без analog data; OGMP Level 5 compliance reporting (direct measurement required, не AI estimate); custody transfer metering (regulatory mass flow meter required).
7. **LO16.7.** Объяснить регуляторный driver: EU 2024/1787 (август 2024, до 20% turnover penalty, OGMP Level 4/5) vs US EPA Subpart W (май 2024, в сентябре 2024 proposed delay до 2034) — почему регуляторика и AI MRV двигаются вместе.
8. **LO16.8.** Сформулировать российскую специфику: sanctions → insourcing → Газпром нефть Cognitive Geo + Роснефть 23 software products + AIQ partnership; что отличается от западе.

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

<!-- Цена пропуска: Лекция 4 = ~5 циклов deck. methodology-critic Phase 1 + Pre-USER-GATE п.6 проверяют это. -->

### Ось

**Variant B — двумерная матрица: доступность данных × определённость физики.** Каждый раздел лекции = погружение в один квадрант. Несущая ось интегрирует **уникальное для нефтегаза**: physics-based simulators (Eclipse, INTERSECT, CMG) дольше и серьёзнее, чем у любой другой индустрии в курсе; sparse data (1 скважина = $50-100M) — структурное, не PR. Каждый квадрант имеет characteristic AI profile + structural failure.

### Keystone-слайд — s05 (после s01 hook + s02 cover + s03 about/anonymized + s04 lecture-map)

- **Заголовок:** «Когда AI работает в нефтегазе? Матрица: данные × физика»
- **1-я строка под title:** «От frontier exploration до methane satellite MRV — AI имеет 4 разных profile»
- **Визуал:** 2×2 matrix
  - **Y-axis:** Определённость физики (high → low)
  - **X-axis:** Доступность данных (low → high)
  - **Q1 (high data + high physics):** Зрелое месторождение — оптимизация производства, ESP/штанговый насос. AI работает как **ускоритель** классических методов. Пример: Ambyint InfinityRL +15% на 200 скважин.
  - **Q2 (high data + low physics):** Метановый MRV — слияние сателлит/самолёт/дрон/ground OGI. **AI essential** (классической физики для cross-source data fusion нет). Пример: MethaneSAT/Carbon Mapper/GHGSat.
  - **Q3 (low data + high physics):** Разведка фронтиров, новые бассейны. **Physics-first, AI augmentation.** ML не generalizes без analog data. Пример: Eni HPC6 + Eclipse simulators.
  - **Q4 (low data + low physics):** Energy transition — CCS plume migration (100 лет horizon), EGS geothermal. **И AI, и physics struggle**; hybrid emerging. Пример: Northern Lights CCS, Fervo EGS.
- **Bottom bar:** «За каждым AI deployment — alternative tool: физический симулятор, OGI камера, классическая интерпретация»

### Как каждый раздел спускается/возвращается к axis

- **Раздел 1 (Q1):** «Начинаем с самого освоенного квадранта — где AI multiplier, не магия. Здесь Ambyint, Aspen Mtell, Honeywell UOP. И здесь же — 86% пилотов застряли (McKinsey). Почему AI работает, и почему всё ещё проваливается на масштабе.»
- **Раздел 2 (Q3):** «Спускаемся в данные-беднейший квадрант — frontier exploration. Здесь HPC6, Discovery 6, METABRAIN. Здесь же — BP+Beyond Limits и IBM+Repsol. Почему ML не generalize без analog data.»
- **Раздел 3 (Q2):** «Возвращаемся в data-rich квадрант, но физика разрозненная. Здесь AI essential — нет классики для cross-source fusion. Здесь же — MethaneSAT loss и 4× discrepancy. Один спутник = single point of failure.»
- **Раздел 4 (Q4):** «Самый честный квадрант — оба измерения low. Northern Lights и Fervo — пытаются, но scale-up gap 190× для CCS. Здесь AI hallucinate легко.»
- **Раздел 5 (Россия + cross-cutting):** «Все 4 квадранта в санкционном режиме — что значит, что Россия не доступа к SLB Lumi, и что это значит для adoption.»

## Инструменты на каждом уровне таксономии (ENFORCED для отраслевых L4+ — Лекция 4 lesson)

<!-- Phase-0 research-бриф обязан размечать tools ПО УРОВНЯМ несущей таксономии, не общим обзором. -->

### Q1 (high data + high physics) — Mature production

**Доминирующие вендоры 2026 (mode ≠ brand):**

- **AspenTech (Emerson)** Aspen Mtell — prescriptive maintenance ML, mainstream post Emerson $15B acquisition 2025 [VFY-day-of]; **adoption растёт**.
- **Ambyint** InfinityRL — reinforcement learning для rod lift / ESP optimization, **growing в US shale** (Permian, Eagle Ford, Bakken).
- **OspreyData (Mesquite Technologies)** Expert-Augmented ML — independent operators, **mainstream но без public KPIs**.
- **SLB Avocet + Lumi** — enterprise tier (NOCs, super-majors).
- **Halliburton DecisionSpace Production** — enterprise tier.
- **Honeywell UOP Connect** — 310+ units / 100+ sites 2024, plan 750+ within year [VFY-day-of]; **growing**.

**Anti-hype:** alert fatigue REAL (Aspen «eliminates» — marketing); stripper wells <10 bopd — ROI отрицательный; mode «predictive maintenance» ≠ brand «Aspen Mtell».

### Q3 (low data + high physics) — Frontier exploration + reservoir simulation

**Доминирующие вендоры 2026:**

- **SLB Lumi** (сентябрь 2024) + Petrel + Delfi — foundation models на NVIDIA Grace Hopper; **leading, customers Shell Aker BP Azule** — **adoption растёт**.
- **Aramco METABRAIN** — 250B параметров, 90 лет данных, **внутренний Saudi, не продаётся внешне**.
- **Eni HPC6** — 14 000 MI250X, 600 PFLOPS, **внутренний Italy, $104M capex**.
- **ExxonMobil Discovery 6** — 4 032 Grace Hopper, **внутренний US**.
- **bp + Beyond Limits** — **discontinued / quiet 2022+** (failure case Раздел 2).
- **CMG (IMEX, STARS, GEM)** — physics simulators, **niche но stable**; **alternative tool**.
- **OpenFOAM** — open-source CFD, **academic + early commercial**, **alternative**.

**Anti-hype:** «AI обнаружит новый bonanza» — overclaim; foundation models trained на Permian не generalize на East African Rift; senior geophysicist + классическая интерпретация **остаётся essential**; PINN (physics-informed neural networks) — research-grade.

### Q2 (high data + low physics) — Methane MRV

**Доминирующие вендоры 2026:**

- **GHGSat** (Canada) — 16-satellite constellation 2025, 25 m разрешение, **commercial growth**.
- **Carbon Mapper Coalition (Planet Labs + NASA JPL)** — Tanager-1 август 2024, primary post-MethaneSAT.
- **EDF MethaneSAT** — **lost June 2025**, single satellite vulnerability lesson.
- **Bridger Photonics** — aircraft Gas Mapping LiDAR, 4× точнее ground OGI, **customers Exxon ConocoPhillips EOG**.
- **SeekOps** — drone-based methane, midstream + utilities.
- **Project Canary** — methane analytics + ESG ratings.
- **Teledyne FLIR + Opgal + Rebellion Photonics** — OGI cameras, **alternative — non-AI** for OGMP Level 5 compliance.
- **Picarro + LI-COR** — portable laser analyzers, direct measurement, **alternative**.

**Anti-hype:** «один спутник всё решит» = MethaneSAT lesson; satellites не видят small dispersed leaks <10-100 kg/h (~70% US emissions); wind sensitivity; detection ≠ quantification (false attribution risk); ground OGI **всё ещё standard** для localization + EU compliance.

### Q4 (low data + low physics) — Energy transition

**Доминирующие вендоры 2026:**

- **Northern Lights JV (Equinor+Shell+TotalEnergies)** — 1.5 Mt CO₂/год Øygarden Norway, **first commercial cross-border CCS hub**.
- **Aker Carbon Capture** — solvent-based capture + AI optimization, **growing**.
- **Fervo Energy** — EGS + fiber optic sensing, **IPO май 2026 +331%**, $206M Cape Station Utah.
- **Eavor Technologies** (Canada) — closed-loop geothermal, **funding rounds growing**.
- **Sage Geosystems** + **Quaise Energy** — early-stage EGS variants.
- **Eni HPC6** — internal CCS modelling (Q3 vendor doubles в Q4).

**Anti-hype:** 190× scale-up gap (current ~40 Mt/год CCS vs IEA target 7.6 Gt 2050); AI plume migration short-term decent, **long-term (100 лет) uncertain**; geothermal physics + drilling — core, AI = enabler не disruptor.

### Cross-cutting infrastructure

- **NVIDIA Grace Hopper** (Discovery 6, Lumi, METABRAIN training) — **dominant HPC**.
- **AMD MI250X / MI300** (Eni HPC6) — **challenger**.
- **HPE Cray EX235a / EX4000** — supercomputer integrator.
- **Microsoft Azure** (ExxonMobil, Aramco, Shell), **AWS** (Aker BP, Equinor), **Google Cloud** (Aramco) — hyperscalers.
- **Cybersecurity OT:** Dragos, Claroty, Nozomi Networks — **growing post-Colonial Pipeline 2021**.

### Russia-specific

- **Газпром нефть IT** — Cognitive Geologist (internal post-IBM), Cognitive system for oil prospecting (Ямал 2024).
- **Роснефть** — Digital Field + 23 software products / 10 commercial, Башнефть Илишевское.
- **AIQ (ADNOC + G42, 51% Presight)** — partnership Газпром нефть с Эмиратами.
- **Cognitive Pilot (Sberbank + Cognitive Technologies JV)** — primarily ag, но transferable к heavy O&G equipment.
- **Татнефть АнтиХрупкий Нижнекамск**, **ЛУКОЙЛ Volga-Ural**, **Сургутнефтегаз** — limited public info [VFY-day-of].

### Volatile числа → `[VFY-day-of]`

- Aramco METABRAIN parameter count (7B → 250B → claim 1T).
- Cognitive Pilot installations (700+ 2021 → 1700+ к 2024).
- SLB Lumi customer count.
- ExxonMobil Discovery 6 capex.
- Nabors PACE-X equipped ratio из 75+ fleet.
- Honeywell UOP Connect plan 750+ within year (target 2025 deadline).
- Татнефть/ЛУКОЙЛ/Сургутнефтегаз specific deployment data.

### Plan §-named speech-narrative → слайд check (Phase-5)

Каждый named vendor в этом списке появится **либо** на слайде, **либо** в spoken anchor с explicit `[FACT-CHECK]` маркером в speech.md.

## Outline

### Раздел 0 — Введение + keystone (≈8 минут, s01-s05, 5 слайдов)

- **s01 (hook + hero):** Permian Basin VIIRS night satellite. Question: «Что вы видите? Это нефть и газ, которые мы экспортируем во вселенную бесплатно».
- **s02 (cover / title):** Лекция 16 «AI в нефтегазовой отрасли и добыче ресурсов» — заголовок + дата + audience tag.
- **s03 (about / audience):** generic «студенты-инженеры 3 курса (универсальная)»; что узнаете; формат 75 минут.
- **s04 (lecture-map):** 6 разделов как карта (БЕЗ timings на visible body — timing только в frontmatter/deck.yaml).
- **s05 (KEYSTONE):** 2×2 matrix data × physics, 4 квадранта с примерами и vendors.

### Раздел 1 — Q1: Mainstream production optimization (≈12 минут, s06-s12, 7 слайдов)

**Связь с keystone:** «Начинаем с самого освоенного квадранта — где данные плотные, физика хорошо изученная. AI здесь — multiplier классических методов.»

- **s06 (section divider):** «Q1 — Mature production: AI как multiplier» + tag «3 working cases · 1 структурный провал». БЕЗ минут.
- **s07:** Ambyint InfinityRL — 200 скважин, +15% над per-well historical mean (типичная Permian well 100-500 bopd). Reinforcement learning для rod lift / ESP.
- **s08:** Aspen Mtell — 10 days production saved, compressor + bearing early detection. Caveat: «alert fatigue eliminated» — vendor claim, в поле часто перенастраивают thresholds.
- **s09:** Honeywell UOP Connect — 310+ units / 100+ sites 2024, plan 750+ within year [VFY-day-of]. Total global refineries ~700.
- **s10:** Российский case — Роснефть Digital Field Башнефть Илишевское: +1 Mt/год extra production (vs Башнефть total ~17 Mt/год 2023 = +5.9%), ~1B руб./год effect, +60% remotely-controlled objects, -5% logistics.
- **s11 (FAILURE):** 86% AI projects в energy не выходят из pilot (McKinsey 2024) + 60% компаний не получают material value (BCG) + 15% O&G professionals live ops / 3% advanced (DNV/Accenture). **Структурные причины:** 60-80% time = data cleanup; legacy IT integration 3-5× initial AI software cost; talent gap; safety culture; slow ROI vs 20-30 лет horizon.
- **s12 (ALTERNATIVE):** Classical SCADA + PID + APC (Honeywell Profit Controller, Emerson DeltaV) — proven, certifiable, regulator-friendly. **Когда AI не нужен:** mature field, experienced reservoir engineer, Eclipse достаточно.

### Раздел 2 — Q3: Frontier exploration + reservoir simulation (≈13 минут, s13-s19, 7 слайдов)

**Связь с keystone:** «Спускаемся в data-беднейший квадрант. Каждая wildcat — $50-100M; sample size 1-5 wells. ML не generalize без analog. Здесь HPC + foundation models, но physics остаётся ground truth.»

- **s13 (section divider):** «Q3 — Frontier exploration: physics-first, AI augmentation» + tag «3 working cases · 2 провала».
- **s14:** Eni HPC6 (декабрь 2024) — 14 000 AMD MI250X, 606 PFLOPS peak, $104M, Ferrera Erbognone Green Data Center. 9× мощнее HPC5. Top500 #5 из ~500 supercomputers = top 1%. CCS modelling + reservoir simulation.
- **s15:** ExxonMobil Discovery 6 (H1 2025) — 4 032 NVIDIA Grace Hopper, 4× compute vs Discovery 5. 4D seismic imaging: месяцы → недели. $1B+ value unlock на первых 6 FPSO Stabroek Block Guyana (total estimate ~16B BOE — 6 FPSO ≈ 30-40% capacity).
- **s16:** Aramco METABRAIN — 250B параметров (начально 7B март 2024); 7T токенов; 90 лет operational data. 6 000 employees trained, 430 use cases. $1.8B realized value 2024 (vs Aramco revenue $440B = 0.4%). SLB Lumi (сентябрь 2024) — domain foundation models, NVIDIA Grace Hopper, customers Aker BP / Shell / Azule.
- **s17 (FAILURE 1):** BP + Beyond Limits ($20M cognitive AI, 2018+). 7 лет публичных результатов нет; Beyond Limits пивотировал в healthcare/manufacturing 2023; BP не обновил кейс после 2019. **Урок:** single-customer concentrated bet; «cognitive AI» — ML marketing 2018; anthropomorphic overpromise («имитировать decision-making геологов»).
- **s18 (FAILURE 2):** IBM Watson + Repsol Kalimba (2014-2017+). 30 лет exploration data «analyzed»; конкретных результатов нет; IBM Watson Industry Solutions stagnation 2018-2022; Repsol перешёл на Lumen 2020+. **Урок:** general-purpose «cognitive computing» platforms не scaled в narrow domain; hype cycle 2014-2016 → ≤10% от ожиданий.
- **s19 (ALTERNATIVE):** Eclipse / INTERSECT / CMG (IMEX, STARS, GEM) — physics-based reservoir simulators. **Когда AI не нужен:** frontier basin (East African Rift без analog); pre-salt early exploration. Senior geophysicist + classical interpretation. ML surrogates accelerate 50-80% но lose physical consistency на extrapolation.

### Раздел 3 — Q2: Methane MRV (≈13 минут, s20-s26, 7 слайдов)

**Связь с keystone:** «Возвращаемся в data-rich квадрант — спутники собирают петабайты в день. Но физика разрозненная: 4 разных sensor modality, methane plume physics не закрыта. AI essential для cross-source fusion. Но один спутник = single point of failure.»

- **s20 (section divider):** «Q2 — Methane MRV: AI essential + единичная уязвимость» + tag «4 working systems · 2 провала · regulatory pressure».
- **s21:** MethaneSAT (март 2024 запуск EDF + Harvard, первый env-NGO-owned satellite). Permian Basin — 410 t/h = 3.6 Mt/год = **50% выше** официальных EPA estimates. New Mexico 1.2% intensity vs Texas 3.1% (NM ввёл regulation 2021, 98% gas capture к концу 2026). 2 000+ data files, 180+ scenes, 10 публикаций.
- **s22 (FAILURE 1):** MethaneSAT loss 20 июня 2025 — после ~13 месяцев (15% designed lifetime). Single satellite = catastrophic SPOF. Regulatory enforcement (EU 2024/1787) не может опираться на 1 спутник. Constellation (GHGSat 16) — better model.
- **s23:** Carbon Mapper Tanager-1 (Planet Labs + NASA JPL, 16 августа 2024, full ops лето 2025). Facility-level detection. Now primary post-MethaneSAT. GHGSat 16-satellite constellation к 2025, 25 m разрешение, commercial service. Bridger Photonics aircraft LiDAR — 4× точнее ground OGI.
- **s24 (FAILURE 2):** 4× discrepancy crisis. MethaneSAT measured ~15 Mt vs EPA inventory ~4 Mt = factor 4 gap. Stanford 2024 aerial: 7.5 Mt = factor 2. 9-satellite single-blind 2024: 0 false positives, **58% correctly identified**, 41 false negatives. **Гэп структурный**: industry vs regulator unresolved, нет agreed ground truth.
- **s25:** Регуляторика как driver. EU Methane Regulation 2024/1787 (август 2024): OGMP 2.0 Level 4/5 mandatory, операторы 4×/год survey, репарация leaks 5-15 дней, до 20% оборота penalty. EU LDAR deadline 5 мая 2025, отчёты 5 августа 2025. US EPA Subpart W 6 мая 2024 final rule (satellite разрешена) → **сентябрь 2024 EPA proposed delay до 2034** (Trump политическая нестабильность).
- **s26 (ALTERNATIVE):** OGI hand-held cameras (Teledyne FLIR GFx320, Opgal EyeCGas) + portable Picarro/LI-COR. EU regulator: **ground measurement preferred** для compliance reporting. **Когда AI не нужен:** OGMP Level 5 verification (direct measurement required, не AI estimate); custody transfer metering (regulatory mass flow meter).

### Раздел 4 — Q4: Energy transition (CCS + EGS) (≈10 минут, s27-s32, 6 слайдов)

**Связь с keystone:** «Самый честный квадрант — оба измерения low. Северная Лайтс CCS — 1.5 Mt/год vs IEA target 7.6 Gt = 0.02% needed. AI plume migration prediction для 100-летнего horizon — hallucinate легко. Здесь и AI, и физика struggle вместе.»

- **s27 (section divider):** «Q4 — Energy transition: AI и physics struggle вместе» + tag «2 working pilots · 2 структурных провала».
- **s28:** Northern Lights CCS (Equinor + Shell + TotalEnergies JV, launched 2024). 1.5 Mt CO₂/год capacity, Øygarden Norway terminal. AI для site selection — 10-15% improved monitoring accuracy claim. **Baseline check:** vs IEA target 7.6 Gt CO₂/год к 2050 vs current global ~40 Mt/год = **190× scale-up gap**. 1.5 Mt из 7600 Mt = 0.02% needed scale.
- **s29:** Fervo Energy EGS — IPO май 2026 +331% offering price. $206M financing июнь 2025 для Cape Station Utah. Driver: AI data centers тянут спрос на 24/7 clean power. **Baseline:** Fervo target part of 150 GW US EGS potential vs current US geothermal installed 3.7 GW = 40× growth ceiling. Eavor Technologies closed-loop, Sage Geosystems, Quaise Energy — early-stage variants.
- **s30 (FAILURE 1):** CCS scale-up gap. 190× needed by 2050 — engineering reality vs policy targets. AI plume migration short-term decent, **long-term (100 лет) uncertain**. Hallucination risk в LLM-based agents для long-horizon prediction. Gartner 2027: 40% agentic AI projects fail из-за cost overruns + poor risk controls.
- **s31 (FAILURE 2):** Refinery AI process control stagnation. Yokogawa Idemitsu — narrow loop demonstration (single column, one heater) — успешно. **Cross-unit plant-wide AI orchestration — стагнирует 2010s-2020s**. Multi-physics constraints (mass + energy + reaction + corrosion) — ML surrogates lose consistency на edge cases. SIL3/SIL4 safety logic — НЕ может быть ML; deterministic certified.
- **s32 (ALTERNATIVE):** Physics-based simulators + classical APC (Honeywell Profit Controller, Emerson DeltaV) для refinery. OpenFOAM CFD для CCS modelling. **Когда AI не нужен:** safety-critical SIS (Safety Instrumented Systems — BOP, PRV sizing, ESD logic) — SIL3/SIL4 certification = deterministic traceable; AI не certifable под ISA-84 / IEC 61511.

### Раздел 5 — Россия + cross-cutting (≈10 минут, s33-s37, 5 слайдов)

**Связь с keystone:** «Все 4 квадранта в санкционном режиме. SLB Lumi недоступен → Газпром Cognitive Geo. ExxonMobil Discovery 6 недоступен → Eni HPC6 как ближайший аналог (но в Италии). MethaneSAT не нужен → нет EU regulator pressure. Что значит no access для adoption.»

- **s33 (section divider):** «Россия — sanctions, insourcing, vertical integration» + tag «3 working programs · sanctions context».
- **s34:** Газпром нефть Cognitive Geologist (с IBM Research Brazil 2017-2022, internal post-IBM) — geology work 3-4 месяца → minutes. Cognitive system for oil prospecting 2024 — first oil из нового поля в Ямале. Цель: cut twofold время до первой нефти, +40% projects acceleration к 2030. AIQ partnership (ADNOC + G42, 51% Presight 2024, валюация $1.4B+).
- **s35:** Роснефть Digital Field — Башнефть Илишевское. 23 software products, 10 commercial. Метрики Башнефть scaling: +60% remotely-controlled, +5% energy efficiency, -5% logistics, +1 Mt/год production (vs Башнефть total ~17 Mt/год 2023 = +5.9%), ~1B руб./год economic effect (~$10-12M по курсу 2024). Sanctions context: после 2022 Roxar / Schlumberger ушли — drive internal dev.
- **s36:** Cognitive Pilot (Sberbank + Cognitive Technologies JV) — primarily agricultural (700+ installations 2021, 1700+ к 2024 [VFY-day-of]). 720 000 t crops harvested + 160 000 ha covered 2020-2021. **Применимость к нефтегазу:** heavy off-road equipment automation. Татнефть АнтиХрупкий Нижнекамск, ЛУКОЙЛ Volga-Ural, Сургутнефтегаз — limited public info [VFY-day-of].
- **s37 (FAILURE + CROSS-CUTTING):** **Cybersecurity counter-trend.** Ransomware attacks on O&G **+935%** между апрелем 2024 и апрелем 2025 (Zscaler). Colonial Pipeline 2021 — VPN без MFA, ~6 дней shutdown. Shell MOVEit 2022 + 2024 vendor compromise. **Урок:** AI добавляет complexity → attack surface растёт. Defensive AI (Dragos, Claroty, Nozomi) отстаёт от offensive AI. Безопасность — phase 1, не phase 4. 2020 oil crash контекст: 107 000 jobs lost март-октябрь 2020 (BP 10 000, Shell 9 000) — industry cyclicality > AI hype cycle.

### Раздел 6 — Closing + Q&A (≈9 минут, s38-s40, 3 слайда)

- **s38 (synthesis):** возврат к keystone matrix, 4 квадранта с key takeaway per квадрант. «Когда AI работает: Q1 multiplier + Q2 essential. Когда осторожно: Q3 augmentation only. Когда опасно: Q4 long-horizon hallucination + safety-critical SIS.»
- **s39 (closing + hero):** MethaneSAT first global methane map (EDF/Google, февраль 2026). Bittersweet payoff: мы потеряли спутник, но карта осталась. **Bridge к Лекции 17:** «systematization of industry AI — keystone'ы L11-L16 как universal patterns».
- **s40 (Q&A):** дедицированный Q&A слайд (БЕЗ «10 минут»), 3-5 ключевых вопросов для exit ticket. Источники списком.

**Итого: 40 слайдов, ~75 минут.** Тайминги: 8 + 12 + 13 + 13 + 10 + 10 + 9 = 75. Слайды: 5 + 7 + 7 + 7 + 6 + 5 + 3 = 40.

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

<!-- CLAUDE.md § AI-Failure & Judgment Content Rule. Холистически: ≥30% видно в chapter+slides+speech. -->

### Бюджет ≥30% — конкретный подсчёт

**Слайды (strict-in failure/limit/criterion/alternative):**
- s11 (86% pilot stuck + structural причины) — full failure slide.
- s12 (classical SCADA alternative + критерий «AI не нужен») — full alternative slide.
- s17 (BP+Beyond Limits) — full failure.
- s18 (IBM Watson+Repsol) — full failure.
- s19 (Eclipse/INTERSECT/CMG alternative + критерий) — full alternative.
- s22 (MethaneSAT loss) — full failure.
- s24 (4× discrepancy crisis) — full failure.
- s26 (OGI ground alternative + критерий) — full alternative.
- s30 (CCS scale-up gap + AI hallucination Q4) — full failure.
- s31 (refinery AI stagnation) — full failure.
- s32 (physics simulator alternative + критерий SIS/SIL) — full alternative.
- s37 (cybersecurity counter-trend + 2020 crash) — full failure.

**Итого strict-in: 12 слайдов из 40 = 30.0%.** На границе threshold. Если methodology-critic Phase 3 показывает <30%, добавить 1-2 partial slides → full (например, s07 Aspen Mtell caveat про alert fatigue).

**Минуты (strict-in):**
- Раздел 1 (12 мин) — 4 мин на s11+s12 (failure+alternative).
- Раздел 2 (13 мин) — 6 мин на s17+s18+s19.
- Раздел 3 (13 мин) — 6 мин на s22+s24+s26.
- Раздел 4 (10 мин) — 6 мин на s30+s31+s32.
- Раздел 5 (10 мин) — 3 мин на s37.

**Итого strict-in: 4+6+6+6+3 = 25 минут из 75 = 33.3%.**

**Слова (chapter 30 000 target):**
- §Раздел 1 Q1 failure deep-dive (86% pilot + alternative SCADA) — ~2 500 слов.
- §Раздел 2 Q3 failure deep-dive (BP/Beyond Limits + IBM/Repsol + Eclipse alternative) — ~3 000 слов.
- §Раздел 3 Q2 failure deep-dive (MethaneSAT loss + 4× discrepancy + OGI alternative) — ~2 500 слов.
- §Раздел 4 Q4 failure deep-dive (CCS scale-up + refinery stagnation + SIS alternative) — ~2 500 слов.
- §Раздел 5 Cybersecurity + 2020 crash + Deepwater Horizon historical anchor — ~1 500 слов.

**Итого strict-in chapter: ~12 000 слов из 30 000 = 40%.** Comfortable cushion.

### 10 documented failures и где разбираются

| # | Failure | Где (раздел/слайд) |
|---|---|---|
| 1 | BP + Beyond Limits cognitive AI ($20M, 2018+, vendor pivot) | Раздел 2 (Q3) / s17 |
| 2 | IBM Watson + Repsol Kalimba (2014-2017+, тихо закрылся) | Раздел 2 (Q3) / s18 |
| 3 | Cognite IPO postpone (2023+, $94M ARR vs cancelled $2-3B valuation) | Раздел 1 (Q1) / s11 inline; chapter deep-dive в §Q1 |
| 4 | C3.ai O&G vertical declining (5.9% FY24 → declining FY25) | Раздел 1 (Q1) inline; chapter §Q1 |
| 5 | MethaneSAT loss июнь 2025 (~13 месяцев из 5+ лет designed) | Раздел 3 (Q2) / s22 |
| 6 | 86% AI pilot stuck (McKinsey 2024) + structural причины | Раздел 1 (Q1) / s11 |
| 7 | 2020 oil crash (107 000 jobs, BP 10k Shell 9k) — industry cyclicality | Раздел 5 / s37 |
| 8 | Methane MRV 4× discrepancy (EPA 4 Mt vs MethaneSAT 15 Mt) | Раздел 3 (Q2) / s24 |
| 9 | Refinery AI process control stagnation (cross-unit orchestration) | Раздел 4 (Q4) / s31 |
| 10 | Cybersecurity ransomware +935% 2024-2025 (Colonial, Shell MOVEit) | Раздел 5 / s37 |

**Bonus historical anchor:** Deepwater Horizon 2010 (alarm bypass + automation + human factors) — chapter глубокий разбор в §Q4/SIS context, slide reference в s31 или speech-only якорь.

### 6 фундаментальных ограничений

| # | Ограничение | Где |
|---|---|---|
| 1 | Sparse data + frontier exploration (1 wildcat = $50-100M, sample 1-5 wells) | s17/s18 + chapter §Q3 |
| 2 | Black-box ML в HSE decisions (нет traceability для SIL3/SIL4 regulation) | s32 + chapter §Q4 SIS |
| 3 | Cost asymmetry (cost-optim AI vs safety AI — different ROI structures) | s11 + chapter §intro |
| 4 | Long horizons (20-30 лет field life) vs ML model decay (1-2 года) | s31 + chapter §Q1 TCO |
| 5 | Multi-physics simulation surrogate gap (Eclipse loses consistency on extrapolation) | s19 + chapter §Q3 |
| 6 | LLM hallucination в high-stakes ops + agentic AI (Gartner 40% fail 2027) | s30 + chapter §Q4 |

### 6 критериев «здесь AI не нужен / не применим»

| # | Критерий | Где |
|---|---|---|
| 1 | Mature field + experienced engineers — Eclipse + senior team достаточно | s12 |
| 2 | Safety-critical SIL3/SIL4 (BOP / PRV / ESD logic) — deterministic mandatory | s32 |
| 3 | OGMP Level 5 compliance — direct measurement required, не AI estimate | s26 |
| 4 | Frontier exploration без analog data (East African Rift, pre-salt early) | s19 |
| 5 | Stripper wells <10 bopd — ML deployment ROI отрицательный | s12 inline |
| 6 | Custody transfer metering — regulatory mass flow meter required | s26 inline |

### 6 alternative (не-AI / другой класс AI) инструментов

| # | Alternative | vs AI tool |
|---|---|---|
| 1 | Eclipse / INTERSECT / CMG physics simulators | vs ML reservoir surrogate (s19) |
| 2 | OGI hand-held cameras (FLIR/Opgal) + Picarro/LI-COR portable | vs satellite AI MRV (s26) |
| 3 | Senior geophysicist + classical seismic interpretation (Kingdom, Petrel manual) | vs Foundation Model auto-interpretation |
| 4 | Classical SCADA + PID + APC (Honeywell Profit Controller, Emerson DeltaV) | vs ML refinery controllers (s12, s32) |
| 5 | SIS (SIL3/SIL4 certified deterministic + redundant hardware 3oo2) | vs ML safety logic (s32) |
| 6 | Federated learning + differential privacy | vs centralized AI (cross-operator competition) — chapter §Q1 cross-cutting |

## Assessment

### Exit ticket (Q1-Q3)

- **Q1.** Для какого квадранта data × physics matrix AI является essential (а не augmentation)? Назовите конкретный case + почему классической физики тут недостаточно.
  - *Expected:* Q2 (high data + low physics) — methane MRV; MethaneSAT/Carbon Mapper/GHGSat. Cross-source data fusion (satellite + aerial + ground) не имеет классического physics-based решения; physics methane plume в atmosphere частично закрыта, но fusion модальностей — open ML problem.

- **Q2.** Приведите 2 documented failure из лекции + выученные уроки.
  - *Expected (любые 2 из):* BP+Beyond Limits (single-customer concentrated bet, vendor pivot, anthropomorphic overpromise); IBM Watson+Repsol (general-purpose cognitive platforms не scaled в narrow domain, hype cycle ≤10% от ожиданий); MethaneSAT loss (single satellite = catastrophic SPOF, constellation модель — better); 86% pilot stuck (60-80% time = data cleanup, legacy integration 3-5×, slow ROI vs 20-30 лет horizon).

- **Q3.** Когда в нефтегазе НЕ применять AI — назовите 3 критерия с примерами.
  - *Expected:* (а) safety-critical SIS (BOP/PRV/ESD) — SIL3/SIL4 deterministic mandatory под ISA-84/IEC 61511; (б) frontier exploration без analog data — ML не generalize, нужен senior geophysicist + classical interpretation + analog basin reasoning; (в) OGMP Level 5 compliance reporting + custody transfer metering — regulator требует direct measurement, не AI estimate.

### Bonus вопросы (для seminar)

- **Q4.** Сравните Eni HPC6 ($104M, 14k AMD MI250X, Italy) vs ExxonMobil Discovery 6 (~$200-400M [VFY], 4k NVIDIA Grace Hopper, US) vs Aramco METABRAIN (250B params, internal Saudi). Какие разные стратегии трёх операторов?
- **Q5.** Почему MethaneSAT factor 4 discrepancy с EPA inventory — это **structural gap**, а не «AI ошибается»? Что Stanford 2024 aerial study (7.5 Mt = factor 2) добавляет к этому?
- **Q6.** Российский case: Газпром нефть Cognitive Geo (геология 3-4 месяца → minutes) — это implementation of Q3 (frontier exploration AI), но в условиях санкций. Что отличает Россия от Saudi/US AI deployments?

## Анонимизация (ENFORCED — Лекция 9 lesson 2026-05-21)

<!-- Career angle / academic contour ОБЯЗАНЫ быть в родовой форме без named institutions. -->

- Frontmatter `audience` строго **«студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)»** — НЕ упоминать МГТУ / Бауман / ИУ-N / Кафедра / ВКА Можайского / МАИ / СПбГУ / РГУ Губкина / Сколтех / МФТИ / МГУ / РГУ нефти и газа / Тюменский ГНГУ.
- **Career section в chapter:** «нефтегазовые компании (национальные и частные) + сервисные подрядчики + регуляторы (Минэнерго, Минприроды, EPA, EU Commission) + НИИ + операторы данных» — generic без brand institutions. Российские operators (Газпром нефть / Роснефть / Татнефть / ЛУКОЙЛ / Сургутнефтегаз) — это **case studies**, не «места работы выпускников».
- **Эталон:** lec-03 / lec-05 / lec-07 chapters — 0 named institutions. lec-06 — единственная generic «профильные кафедры» (родовое). Для lec-16 цель — 0 named educational institutions.
- **Cost-of-omission lec-09:** 1 revision cycle (v2→v3) anonymization. Phase 3 methodology-critic + Pre-USER-GATE A check.

## Russification visible body (ENFORCED — memory rule `feedback_russification`)

### Top replacements для Лекции 16 (в КАЖДОМ producer prompt)

| Англицизм | RU замена |
|---|---|
| foundation model | большая универсальная модель / фундаментальная модель |
| reservoir simulation | пластовое моделирование |
| seismic interpretation | интерпретация сейсмики |
| predictive maintenance | прогностическое обслуживание / упреждающее ТО |
| prescriptive maintenance | предписывающее обслуживание |
| alert fatigue | усталость операторов от ложных тревог / выгорание от ложных срабатываний |
| methane MRV (monitoring/reporting/verification) | выявление-учёт-проверка метановых выбросов |
| downhole | внутрискважинный |
| upstream | добыча (поиск/разведка/добыча) — с inline gloss при первом упоминании |
| midstream | транспорт (трубопроводы/СПГ/хранение) |
| downstream | переработка (НПЗ/нефтехимия/сбыт) |
| greenwashing | экологический whitewash / показная зелёность |
| shut-in / curtailment | консервация / ограничение добычи |
| frontier exploration | разведка фронтиров / разведка новых геологических провинций |
| basin / play | нефтегазоносный бассейн / тип залежи |
| mature field | разработанное / зрелое месторождение |
| pilot purgatory | застрявшие в пилоте |
| ESP (electric submersible pump) | электроцентробежный насос (ЭЦН) — стандарт RU |
| artificial lift | искусственный лифт (нефтегазовый термин ОК на русском) |
| rod pump / sucker rod | штанговый насос |
| gas lift | газлифт |
| digital twin | цифровой двойник |
| ground truth | эталонная разметка |
| automation bias | склонность доверять автомату |
| multi-sensor fusion | слияние нескольких сенсоров |
| decision-support | поддержка принятия решений |
| edge case | краевой случай |
| compliance | соответствие нормам / комплаенс (RU вариант ОК) |
| carbon accounting | углеродный учёт |
| black-box model | непрозрачная модель / модель без интерпретации |
| hallucination (LLM) | галлюцинация / выдумка модели |
| human-in-the-loop | человек в петле принятия решений |

### Brand allowlist (keep-list для anti-Russification)

- **Companies:** SLB, Halliburton, Baker Hughes, NVIDIA, AMD, HPE Cray, Microsoft Azure, AWS, Google Cloud, Aramco, ADNOC, BP, Shell, ExxonMobil, Chevron, ConocoPhillips, Repsol, Eni, Equinor, TotalEnergies, Aker BP, Reliance, Diamondback, Pioneer (acquired), Marathon (acquired), Hess (acquired), Газпром нефть, Роснефть, Татнефть, ЛУКОЙЛ, Сургутнефтегаз.
- **Products:** Eclipse, INTERSECT, Petrel, Delfi, Lumi, METABRAIN, GAIA, Aspen Mtell, aspenONE, DeltaV, Ability Genix, OpreX, PACE-X, AlphaAutomation, NOVOS, FlexRig, Cognite Data Fusion, Cognite Atlas AI, AVEVA Insight, PI System, Discovery 6, HPC6, MethaneSAT, Tanager-1, Carbon Mapper, GHGSat, Bridger Photonics, SeekOps, Kairos Aerospace, Project Canary, OGI, OGMP, FLIR GFx320, Opgal EyeCGas, Rebellion Photonics, Picarro, LI-COR, InfinityRL, Avocet, DecisionSpace, Forge, Predix, Smart Signal, Beyond Limits, Watson, Northern Lights, Aker Carbon Capture, Fervo, Eavor, Sage Geosystems, Quaise.
- **Standards:** SIL3, SIL4, OGMP 2.0, EU 2024/1787, Subpart W, EPA Method 21, ISA-84, IEC 61511, GHGRP.
- **Russian products:** Cognitive Geologist, Cognitive Geo, Cognitive Agro Pilot, AIQ (ADNOC+G42), Digital Field, Илишевское, Ямал, АнтиХрупкий завод, Roxar.
- **Acronyms (с inline gloss первый раз):** FPSO (плавучая платформа добычи-хранения-выгрузки), CCS (улавливание и хранение углерода), EGS (улучшенные геотермальные системы), LDAR (Leak Detection and Repair / программа выявления и устранения утечек), MRV (выявление-учёт-проверка), BOP (противовыбросовый превентор), PRV (предохранительный клапан), ESD (Emergency Shutdown / аварийный останов), SIS (Safety Instrumented System / приборная система безопасности), APC (Advanced Process Control / продвинутое управление процессом), HPC (высокопроизводительные вычисления), NOC (национальная нефтяная компания), IOC (международная нефтяная компания), FPSO/CCS/EGS — с расшифровкой при первом появлении.

### Pre-GATE check (ENFORCED)

Deep latin-token scan (не только pattern grep) перед каждым USER GATE. `unique - whitelist = ∅` для narrative body. См. `tools/presentation-build/README.md` §5.8. Cost-of-omission lec-08: «обилие англицизмов! провал» owner reject → 3 revision passes.

## Hero illustrations (ENFORCED for all deck — memory rule `feedback_hero_images`)

<!-- Каждая презентация курса ОБЯЗАНА иметь hero-иллюстрацию на первом + последнем слайде. -->

### s01 — Permian Basin VIIRS night satellite (NASA Earth Observatory / NOAA, public domain)

- **Foreshadow keystone:** visible scale промышленности (2 593 plumes 2024) + measurement story → готовит почву для Q2 methane MRV в Разделе 3.
- **Acquisition Tier 1** (NASA Earth Observatory direct download, public domain).
- **Attribution label:** «NASA Earth Observatory / VIIRS / NOAA, 2024» visible на slide footer.
- **Area:** ≥40% slide area.
- **Fallback:** Deepwater Horizon US Coast Guard controlled burn (Tier 1, public domain) — caveat: может слишком «catastrophe-framed» для opening.

### s39 — MethaneSAT first global methane map (EDF + Google, February 2026)

- **Bridge к Lec-17 (systematization of industry AI keystones L11-L16):** карта показывает измеримость на глобальном уровне как payoff of AI MRV era; и одновременно single point of failure (satellite потерян в июне 2025).
- **Acquisition Tier 1** (Inside Climate News article February 2026; EDF accompanying release).
- **Fallback Tier 4** (Wayback machine snapshot of EDF page).
- **Attribution:** «EDF / MethaneSAT data via Google Earth Engine, February 2026».
- **Backup s39 candidate:** modern oil&gas control room с human-in-loop + AI screens (Tier 3-4, hyperscaler vendor case study).

### НЕ подходит для s01 / s39

- Stock «hands on keyboard» / «AI brain icon» — generic, AVOID.
- Plain Ocean palette card с verbatim headline — MOCK, FAIL (per `feedback_no_mock_fallbacks`).
- Vendor logo как hero — brochure feel, AVOID.
- Render не-existing satellite / installation — hallucination, FORBIDDEN.

## 6-tier image acquisition (ENFORCED — memory rule `feedback_no_mock_fallbacks`)

<!-- Для всех media-rich слайдов (минимум 20-22 на типичный 40-deck = ≥50%). Mock-fallback допустим ТОЛЬКО при documented 6/6 tier failure. -->

### Media coverage plan: ≥50% slides с реальными медиа

**Target: 22 из 40 slides с media (55%).** Список slides + planned acquisition tier:

| Слайд | Content | Tier | Source hint |
|---|---|---|---|
| s01 | Permian VIIRS night | T1 | NASA Earth Observatory direct |
| s05 | Keystone matrix | self-render | drawio/mermaid |
| s07 | Ambyint InfinityRL rod lift | T3 | Ambyint case study page |
| s08 | Aspen Mtell compressor | T3 | AspenTech case study |
| s09 | Honeywell UOP refinery | T3 | UOP press kit |
| s10 | Роснефть Башнефть field | T3 | Rosneft press / Башнефть |
| s14 | Eni HPC6 racks | T3 | Eni press kit / DCD article |
| s15 | ExxonMobil Discovery 6 + Guyana FPSO | T3 | HPE blog / ExxonMobil press |
| s16 | Aramco METABRAIN + SLB Lumi | T3 | Aramco press + SLB press |
| s17 | BP + Beyond Limits archived | T5 | Wayback Machine 2018-2019 page |
| s18 | IBM Watson + Repsol archived | T5 | Wayback Machine 2014-2016 |
| s19 | Eclipse/INTERSECT visualization | T3 | SLB Eclipse product page |
| s21 | MethaneSAT Permian scene | T1 | MethaneSAT data sneak peek |
| s22 | MethaneSAT timeline (loss June 2025) | T3 | EDF / MethaneSAT project updates |
| s23 | Carbon Mapper Tanager-1 + GHGSat constellation | T3 | Carbon Mapper press / GHGSat press |
| s25 | EU 2024/1787 + US EPA Subpart W timeline | self-render | timeline diagram |
| s26 | FLIR GFx320 OGI + Picarro | T1/T6 | Teledyne FLIR product + Picarro |
| s28 | Northern Lights Øygarden terminal | T3 | Northern Lights JV press kit |
| s29 | Fervo Cape Station drilling | T3 | Fervo Energy press |
| s31 | Yokogawa OpreX Idemitsu | T3 | Yokogawa press / Idemitsu |
| s34 | Газпром нефть Ямал operation | T3 | Gazprom Neft press |
| s35 | Роснефть Digital Field schematic | T3 | Rosneft press |
| s37 | Colonial Pipeline 2021 / Zscaler 2025 chart | T1/T3 | Colonial Pipeline news + Zscaler report |
| s39 | MethaneSAT global methane map | T1/T4 | Inside Climate News Feb 2026 + EDF |

**Self-render (charts/diagrams/matrices):** s04 lecture-map, s05 keystone matrix, s06/s13/s20/s27/s33 section dividers (text+small icon), s11 (86% pilot bar chart), s24 (factor 4 discrepancy comparison chart), s25 (regulatory timeline), s30 (CCS 190× scale-up gap chart), s38 synthesis matrix recall, s40 Q&A.

**Total media: 22 real photos / screenshots + 13 self-rendered charts / matrices = 35 / 40 = 87.5% visual.** Hits ≥50% media target comfortably.

### Per-image acquisition log mandatory

Per `feedback_no_mock_fallbacks`:
1. Source URL.
2. License attribution string.
3. Date acquired.
4. If fallback used — original failure reason.
5. Storage: `library/lectures/lec-16/assets/screenshots/sNN-real-source.png` + `.url` файл.

**Anti-pattern reminder (Лекция 8 cost):** 16 stylized mocks прошли «87.2% coverage» self-report → owner reject «это моканное говно». Orchestrator MUST visually verify sample 5 slides на Pre-USER-GATE B.

## Open questions / `[VFY-day-of]`

Для Phase 3 fact-checker (требуют day-of verification):

1. **Aramco METABRAIN parameter count progression** — 7B (март 2024) → 250B (конец 2024) → claim 1T (публикации 2025). Какое значение **актуально для лекции** и **аудированно** (Aramco self-reported, methodology не disclosed).
2. **Cognitive Pilot installations 2024** — 700+ (2021 confirmed) → 1700+ (2024 claim). Источник свежий? И что значит «installation» — combine vs sprayer vs custom?
3. **ExxonMobil Discovery 6 capex** — оценочно $200-400M (по аналогии с Eni HPC6 $104M на меньшую систему), но ExxonMobil не раскрывает. Заменить estimate или оставить «не раскрыто»?
4. **Nabors PACE-X fleet ratio** — из 75+ rigs (per 2024 8-K), сколько PACE-X-equipped? Public KPIs скудные.
5. **US EPA Subpart W status сентябрь 2024 → 2026** — final rule 6 мая 2024, в сентябре 2024 proposed delay до 2034, Trump admin 2025+. Какой actual statut на 2026-05-27 (день лекции)?
6. **Honeywell UOP Connect 750+ within year target** — это claim 2024 «к 2025». Достиг ли? Cite свежие numbers.
7. **Татнефть / ЛУКОЙЛ / Сургутнефтегаз** — specific deployment data minimum. АнтиХрупкий завод Нижнекамск Татнефти упоминается, но без verified deployment metrics. ЛУКОЙЛ Volga-Ural digital fields упоминается, без detail. Сургутнефтегаз — наиболее закрытая.
8. **GHGSat constellation 16 satellites к 2025** — состояние COP30 launch.
9. **US EPA Waste Emissions Charge** — $1500/t CH₄ tiered structure — implemented или only planned?
10. **Aramco $1.8B realized 2024 + $6B 2023-24 cumulative** — Aramco self-reported, non-audited; что методология подсчёта?

## Notes для downstream phases

- **Phase 2 (book-editor):** chapter target ≥30 000 слов; multi-part split на 4 файла (chapter.md + chapter-part2.md + chapter-part3.md + chapter-part4.md, каждый ≤600 строк, 7-8k слов). Каждый раздел = 6 500-8 500 слов. Slide-маркеры `[for-slide-sNN]` на каждом ≥150-слов разделе.
- **Phase 3 (methodology-critic + fact-checker):** word count check (<28 500 = P0 BLOCKING); failure-share check (если <30% strict-in в одном из 3 артефактов → REVISE); baseline check sample 5-7 measurable claims; `[VFY-day-of]` resolution.
- **Phase 5 (designer):** Lec-N-1 (Lec-15) reference read mandatory; visual-loop 3× per slide minimum; deep latin-token scan на final pptx; hero verification s01 + s39.
- **Phase 9 (speech-writer):** 5-6k слов conversational; chapter-derived; no «методически важно» / «на этом этапе студент должен» / timing markers в visible speech.
- **Pre-USER-GATE A/B/C:** failure-share check + baseline coverage check + designer-extras grep + hero check + deep latin-token scan + real-image verification sample.

## Risks / concerns

### Risk 1 (HIGH): Q2 (high data + low physics) — formulation tricky

Студент-инженер 3 курса может не понять, почему methane plume physics — «low certainty». Atmospheric methane physics частично закрыта (известны диффузия, photochemistry); но **cross-source fusion physics + multi-sensor methane attribution** — open. Keystone slide s05 ОБЯЗАН явно объяснить, что «physics certainty» в данном контексте = «есть ли установившаяся численная модель, дающая ground truth». В Q3 (Eclipse) — да; в Q2 (multi-modal methane fusion) — нет. Cost of confusion: лекция получит «методически странная» reject.

**Mitigation:** s05 keystone text expanded с definition; chapter §intro spends 500-700 слов на «physics certainty» explanation; methodology-critic Phase 1 review explicitly tests this confusion-risk.

### Risk 2 (MEDIUM): Failure-share на границе 30%

Slide count 12/40 = 30.0% exact. Если 1 slide реклассифицируется (например, s11 staкивается как «mixed» = pilot stuck + 86% claim — но claim ground truth по research'у solid), процент падает <30% → REVISE. **Strict-in mandate** требует full в каждом артефакте.

**Mitigation:** Phase 3 critic check; запас в word count (40% chapter, 33% minutes) — comfortable cushion. Если slides падают <30%, добавить s07 caveat slide → full failure slide OR convert s38 синтез matrix slide в «4 квадранта + 4 failures synthesis».

### Risk 3 (MEDIUM): Volatile numbers `[VFY-day-of]` count high

10 open questions для fact-checker — это много. Aramco METABRAIN параметры, Cognitive Pilot installations, ExxonMobil Discovery 6 capex, US EPA Subpart W status в 2026 — все потенциально outdated до лекции. Если fact-check resolution не успевает, придётся либо degrade specific claims к ranges, либо oставить `[VFY-day-of]` markers visible — что снижает trust.

**Mitigation:** Phase 3 fact-checker priority list; для критичных (METABRAIN, Subpart W status) — fresh web search before chapter draft submit; backup formulations подготовлены (e.g., «250B параметров по состоянию на конец 2024 — claim для 2025 не аудирован»).

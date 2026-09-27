# Сегменты и кейсы: AI в нефтегазе по этапам value chain

**Цель.** Per-segment cases с numbers + baseline. Каждый case = компания + AI-проект + год + результат + база.

Структура: Upstream (exploration/drilling/production) → Midstream → Downstream → ESG/MRV → Россия специфика. Внутри секций — by-vendor + by-operator.

## 1. UPSTREAM (exploration + drilling + production)

### 1.1. Seismic interpretation + exploration

#### SLB Petrel + Delfi (дальше + Lumi)

- **SLB Delfi** — облачная E&P платформа на AWS/Azure/GCP, основа для AI workflows.
- **Lumi (сентябрь 2024)** — AI-уровень над Delfi с domain foundation models.
- **Customers 2024 (известные):**
  - **Shell Offshore Inc.** — Wellbore Insights на Delfi в US Gulf of Mexico, cloud-based wellbore dynamics modelling.
  - **Aker BP** (Norway) — codevelop digital platform для subsurface workflows, цель «reducing costs и shortening planning cycles» (конкретные deltas не раскрыты [VFY-day-of]).
  - **Azule Energy** (bp + Eni Angola JV) — Delfi для всей E&P.
- **SLB digital revenue:** **$2B+ в 2024** (full-year) — это **~7-8% от $35B total SLB revenue 2024**. Direction: «further adoption of Delfi technology and customers embracing connected and autonomous drilling».

#### ExxonMobil + HPE + NVIDIA Discovery 6 (H1 2025)

- См. также 01-trends-2026.md §1.
- **4D seismic imaging:** time-lapse models underground reservoirs, processing **месяцы → недели**.
- **$1B+ value** unlock на первых 6 FPSO в Stabroek Block (Guyana). Baseline: total Stabroek estimate ≈ 16B BOE; первые 6 FPSO ≈ ~30-40% от планируемой capacity.
- **Capex Discovery 6 [VFY-day-of]:** не раскрыт, но HPE Cray EX4000 с 4 032 Grace Hopper — оценочно $200-400M по аналогии с Eni HPC6 ($104M на меньшую систему).

#### Aramco METABRAIN + GAIA fund (2024-2025)

- **METABRAIN 250B params** trained на 90 годах данных.
- **6 000 employees trained** на AI, **430 use cases** identified.
- **GAIA fund — $1B** для AI startups (anchor LP Aramco + partners).
- **Drilling plan analysis** — engineers query naturalным языком 90-летние records.
- **$4B technology realization 2024** (self-reported, non-audited).
- Baseline для $4B: vs **Aramco total revenue 2024 ≈ $440B** = 0.9% revenue. Vs **R&D budget $3.5B/год** = >100% R&D budget (suspicious — likely включает unrealized future value, не only realized).

#### Eni HPC6 (декабрь 2024)

- 606 PFLOPS peak, 14k MI250X GPUs, $104M.
- Применение: seismic processing + reservoir simulation + **CCS modelling**.
- Baseline: Top500 #5 из 500 supercomputers (top 1%). HPC6 в **9× мощнее** предшественника Eni (HPC5).

#### Repsol + IBM Watson Kalimba (2014-2017+)

- **2014:** start partnership; 30 лет exploration data analyzed.
- **2016:** early results expected; project announcement claims «cognitive computing».
- **Outcome 2017-2022:** результаты НЕ публично раскрыты; IBM пошагово сворачивал Watson industry verticals; Repsol перешёл на собственные ML tools (см. Repsol Lumen platform 2020+).
- **Lesson:** один из ранних cognitive AI partnerships, low public ROI traceability — типичный «pilot purgatory» case.

#### Russia: Газпром нефть Cognitive Geo (IBM Research Brazil)

- Partnership с **IBM Research Brazil** — ML + probabilistic reasoning для exploration.
- Cycle сокращён: geology work **3-4 месяца → minutes** для определённых tasks.
- **2024:** «Cognitive system for oil prospecting» → first oil из нового поля в Yamal.
- Цель: **cut twofold** время от первой нефти, accelerate major projects **+40% к 2030**.
- Baseline gap [VFY-day-of]: total geological projects Газпром нефти — N=? скольких из них AI применяется?

### 1.2. Drilling automation

#### Nabors PACE-X (см. 01-trends-2026.md §2)

- 4-mile laterals в Bakken, Haynesville (20k ft), Delaware Basin, Eagle Ford.
- ROP выше Nabors среднего.
- Baseline: Nabors had **75+ rigs** в 2024 (per 8-K filings); количество PACE-X-equipped — не раскрыто.

#### Precision Drilling AlphaAutomation, NOV NOVOS

- Аналогичные решения от competitors. Public KPIs скудные.

### 1.3. Production optimization (ESP, rod pump, gas lift)

#### Aspen Mtell

- **AspenTech** (acquired by Emerson 2025, ~$15B).
- **Mtell prescriptive maintenance** — early detection compressor + bearing failures.
- **Case study:** 10 days production saved, «alert fatigue eliminated» (vendor claim).
- aspenONE V14.3 (май 2024) + Aspen Inmation integration.

#### Honeywell UOP Connected Services

- 310+ units connected, 100+ customer sites, plan 750+ within year.
- Process+asset models + ML + dynamic analytics + 24/7 alert management.
- Customers: BP, Shell, Reliance, Aramco (некоторые публично).

#### Ambyint

- **InfinityRL** — rod lift optimization, reinforcement learning.
- **Case:** 200 wells deployed; average production **+15%** across optimized wells.
- Baseline gap: +15% от какой baseline production rate? Per-well average не раскрыт.
- Customer base: independents в Permian, Eagle Ford, Bakken.

#### OspreyData (acquired by Mesquite Technologies, ноябрь 2022)

- **Expert-Augmented Machine Learning** для ESP + Rod Pump + gas lift + plunger lift issues.
- Включено в Mesquite Taproot product line.
- Public KPIs не раскрыты [VFY-day-of].

#### Schlumberger Avocet, Halliburton DecisionSpace Production

- **Avocet** — production operations software; ML integrated 2020+.
- **DecisionSpace Production** — Halliburton's production optimization platform.
- Adoption: enterprise-tier customers (NOCs + super-majors). Specific KPIs не публичны.

### 1.4. Subsea + offshore production

#### Equinor + ARM (Norway)

- Compressor station optimization (см. midstream).

#### TechnipFMC, Subsea 7, Baker Hughes Subsea

- Subsea digital twins, condition monitoring. Mostly internal / customer-specific deployments.

## 2. MIDSTREAM (pipelines + compressor stations + storage)

### 2.1. Pipeline integrity

#### Enbridge (Canada/US)

- **456 inline inspections в 2024** (smart pigs, ILI).
- ILI data: **terabytes per inspection run**, millimeter precision metal loss / corrosion / cracks.
- **Integrity Engine + Energy Optimizer** AI models на Microsoft Azure.
- Partnership с **NDT Global** — next-gen crack inspection tool, Proton measurement.
- Baseline: 456 inspections vs total ~30 000 km Enbridge pipelines = inspection coverage ratio.

#### TC Energy

- ML applications для ILI defect assessment. Specific 2024 deployments не публично раскрыты [VFY-day-of].

#### Irth Solutions, GE Pipeline Integrity

- Vendor offerings для smaller operators.

### 2.2. Methane leak detection (MRV)

#### GHGSat (Canada) — satellite

- **16 satellites к 2025**, 25 m resolution, commercial service.
- Customers: operators в Permian, Marcellus, AB Canada; insurance companies; regulators.

#### Carbon Mapper Tanager-1 (Planet Labs)

- Запущен август 2024, full ops лето 2025.
- Facility-level detection.

#### Bridger Photonics

- Aircraft-based Gas Mapping LiDAR. 4× более точный чем regulated OGI surveys (BC validation study).
- Customers: ExxonMobil, ConocoPhillips, EOG Resources, Pioneer (теперь часть Exxon).

#### SeekOps

- Drone-based methane detection.
- Customers: midstream operators, gas utilities.

#### MethaneSAT (мёртв, см. ниже)

### 2.3. Compressor station + pipeline optimization

#### Equinor ARM

- Compressor station condition monitoring + production allocation.
- Norwegian Continental Shelf deployment.

#### Honeywell Forge

- Cross-vertical IIoT platform; oil&gas midstream applications.

## 3. DOWNSTREAM (refining + petrochemicals + marketing)

### 3.1. Refinery process optimization

#### Aspen Mtell, Honeywell UOP Connect — см. §1.3.

#### Yokogawa OpreX AI

- AI controllers — например, Idemitsu (Japan) deployment 2024 — partially autonomous unit operation.

#### ABB Ability Genix

- Industrial analytics + AI platform для process industries.

### 3.2. Demand forecasting + trading

#### Shell + Microsoft + C3.ai

- Shell partnership с C3.ai для process automation (announced 2018+, multi-year extensions).
- ML для demand forecasting, trading desk decisions.
- 2024 status [VFY-day-of]: contract still active per C3.ai filings, но revenue contribution to C3 smaller (Oil&Gas vertical 5.9% FY24 → declining).

#### ExxonMobil supply chain (с Microsoft)

- Generative AI optimizing supply chain operations real-time.

#### Cargill (oil/grain trading)

- См. Лекция 5 reference (financial sector).

### 3.3. Retail fuels + marketing

#### bp Pulse, Shell Recharge

- EV charging — AI для demand forecasting, dynamic pricing.

#### Convenience stores AI

- Out of scope for this lecture.

## 4. ESG / HSE / Methane MRV (separate dimension)

### 4.1. Satellites — см. §2.2.

### 4.2. Drone-based detection — SeekOps, Sniffer Robotics.

### 4.3. Ground OGI cameras + AI processing

- FLIR, Opgal, Rebellion Photonics cameras.
- AI video analytics поверх — Project Canary, Kairos Aerospace.

### 4.4. CCS site selection и monitoring

- **Northern Lights** (launched 2024) — Equinor + Shell + TotalEnergies JV.
- AI для site selection (10-15% better monitoring accuracy claim).
- Capacity 1.5 Mt CO₂/год.

### 4.5. Carbon accounting

- **Persefoni, Watershed, Sweep** — enterprise carbon accounting SaaS.
- Используют AI для category 3 emissions estimation.
- Контroversial: audits показывают misreporting risks (см. 03-failures-and-limits.md).

## 5. РОССИЯ — отдельный режим

### 5.1. Газпром нефть

- **Cognitive Geologist** (с IBM до 2022; продолжен internally) — exploration.
- **Cognitive system for oil prospecting (2024)** — Yamal.
- **Партнёрство с AIQ (ADNOC + G42 JV)** — commercialization digital tools 2023-2024.
- **AI alliance Russia** — первая industrial company-member.
- Claim CEO «без digital и AI добывали бы половину» — non-quantified, marketing.

### 5.2. Роснефть

- **Digital Field project** — Bashneft Ilishevskoye field.
- **23 software products**, 10 уже commercial. Industry-leading dev program (per company).
- Метрики Bashneft scaling:
  - Remotely-controlled objects **+60%**.
  - Energy efficiency **+5%**.
  - Logistics costs **-5%**.
  - Extra oil production **~1 Mt/год**.
  - Economic effect **~1B rubles/год** (~$10-12M).
- Baseline: Bashneft total production **~17 Mt/год** (2023) → +1 Mt = +5.9%.
- Sanctions context: после 2022 Россия pивотировала на internal software (Roxar отозван Equinor, Schlumberger ушёл).

### 5.3. Татнефть, ЛУКОЙЛ, Сургутнефтегаз

- **Татнефть «АнтиХрупкий завод» Нижнекамск** — упоминается (специфика unclear) [VFY-day-of].
- **ЛУКОЙЛ Volga-Ural digital fields** — упоминается [VFY-day-of].
- **Сургутнефтегаз** — наиболее закрытая, специфики deployment не публикует [VFY-day-of].

### 5.4. Cognitive Pilot (Sberbank + Cognitive Technologies JV)

- НЕ нефтегаз primary — agriculture (combines, tractors). Но vendor может быть relevant для off-road heavy equipment в нефтегазе.
- **720 000 tonn crops harvested** AI-combines в Russia (claim 2020-2021).
- Production fully self-driving tractors начало **2024**.
- Aggregate installations [VFY-day-of] — 700+ в 2021, направление на 1700+ к 2024 (нужна свежая верификация).

### 5.5. Российская специфика — что отличает

- **Sanctions:** доступ к western digital tools ограничен — drive towards internal vendors.
- **Vertical integration:** super-majors (Газпром, Роснефть) разрабатывают свой software, не покупают у SLB/Halliburton.
- **State driver:** Минэнерго, Минцифры, Минпромторг координируют industry-wide digitalization.
- **Talent:** AI-инженеры с opyt в нефтегазе uncommon; Cognitive Technologies, Сколтех, МФТИ, МГУ — основные источники.

## 6. Кросс-секторальные observations

### 6.1. Vendor concentration (2024-2026)

- **Big 3 oilfield services:** SLB, Halliburton, Baker Hughes — все pivot к AI/digital revenue stream.
- **Hyperscalers:** Microsoft (через ExxonMobil, Shell, Aramco), AWS (через Aker BP, Shell, Equinor), Google Cloud (через Shell, Saudi Aramco).
- **Chip vendors:** NVIDIA dominant в HPC (Grace Hopper, H100); AMD challenger через Eni HPC6.

### 6.2. Open-source / academia

- **OpenFOAM** — CFD open-source, базис для CCS modeling.
- **MIT Earth Resources Lab**, **Stanford Energy** — academic centres для ML+geology.

### 6.3. Hyperscaler counter-trend

- Microsoft+G42 ($1.5B 2024) — UAE как AI hub для energy.
- Saudi PIF (Public Investment Fund) — anchor LP для AI startups via GAIA.

## 7. По мере необходимости для plan

| Сегмент | Lead vendor 2026 | Direction | Anti-hype |
|---|---|---|---|
| Seismic AI | SLB Lumi + Aramco METABRAIN | Foundation models растут | «AI obnaruzhit novyy bonanza» — overclaim |
| Reservoir simulation | ExxonMobil Discovery 6 + Eni HPC6 | HPC growing; ML surrogate ускоряет | Physics-based simulators НЕ заменяются полностью |
| Autonomous drilling | Nabors PACE-X, Precision Drilling | Шаг за шагом автономность; full unmanned не promised | Compleх wells human override required |
| ESP / artificial lift | Ambyint, Aspen Mtell, OspreyData | Predictive maintenance mainstream | Alert fatigue REAL, не «eliminated» |
| Methane MRV | GHGSat, Carbon Mapper, Bridger | Satellite + aircraft growth | Ground OGI всё ещё нужен для localization |
| Refinery AI | Honeywell UOP, AspenTech (Emerson) | Process control mainstream | Stagnates в complex multi-physics |
| CCS | Northern Lights + Eni HPC6 modeling | Early-stage AI; scale-up to 7.6 Gt 2050 | 190× scale-up gap |
| Digital twin platforms | Cognite, Aveva, AspenTech | Slow but real adoption | Cognite IPO postpone — funding gap |

---

## Источники (см. также 01-trends-2026.md)

- [SLB Aker BP Delfi contract](https://www.sec.gov/Archives/edgar/data/0000087347/000119312524181280/d696444dex99.htm)
- [SLB Azule Energy Delfi](https://www.sec.gov/Archives/edgar/data/0000087347/000119312524239201/d837842dex99.htm)
- [SLB Shell Gulf of Mexico Wellbore Insights](https://www.sec.gov/Archives/edgar/data/0000087347/000119312524101633/d778868dex99.htm)
- [SLB digital revenue $2B 2024](https://www.sec.gov/Archives/edgar/data/0000087347/000119312524010748/d142783dex99.htm)
- [Enbridge AI integrity engine](https://www.klover.ai/enbridge-ai-strategy-analysis-of-dominance-in-energy-infrastructure/)
- [Ambyint InfinityRL 200 wells +15%](https://www.ambyint.com/case-studies/oil-well-optimization)
- [OspreyData acquired Mesquite](https://www.prnewswire.com/news-releases/mesquite-technologies-inc-acquires-ospreydata-inc-and-announces-entry-into-production-optimization-through-development-of-intelligent-control-product-offering-301669236.html)
- [Cognitive Agro Pilot installations](https://en.cognitivepilot.com/agriculture-2/cognitive-agro-pilot-provides-autonomous-combine-navigation/)
- [Cognitive Pilot 720k tonn harvested](https://en.cognitivepilot.com/agriculture-2/russian-ai-enabled-harvesters-reap-720000-tons-of-crops/)

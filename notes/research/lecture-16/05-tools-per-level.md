# Tools per taxonomy level — named vendors 2026

**Назначение.** ENFORCED — отраслевая лекция L4+ требует tools-per-taxonomy-level с **2-4 dominant vendors 2026 + adoption direction + anti-hype/boundary**. Mode ≠ brand. Volatile цифры → `[VFY-day-of]`.

Структура соответствует **Variant B keystone (data × physics matrix)** из `04-keystone-axis-options.md`.

---

## §1. Q1 — High data + high physics: Mature field production optimization

### 1.1. Production optimization (ESP / rod pump / gas lift)

**Dominant vendors 2026:**

| Vendor | Product | Mode | Adoption direction |
|---|---|---|---|
| **AspenTech (Emerson)** | Aspen Mtell | Prescriptive maintenance ML | Mainstream, integration после Emerson $15B acquisition 2025 [VFY-day-of] |
| **Ambyint** | InfinityRL rod lift, ESP optimization | Reinforcement learning | Growing в US shale (Permian, Eagle Ford, Bakken) |
| **OspreyData (Mesquite Technologies)** | Expert-Augmented ML для artificial lift | ML+expert hybrid | Independent operators в US |
| **SLB** | Avocet + Lumi | Production data platform + LLM | Enterprise tier (NOCs, super-majors) |
| **Halliburton** | DecisionSpace Production | Production optimization suite | Enterprise tier |

**Anti-hype / границы:**
- **Alert fatigue REAL.** Aspen Mtell claim «eliminates» — marketing. Field deployments часто перенастраивают thresholds после initial wave false positives.
- **Per-well economics:** stripper wells (<10 bopd) ML deployment ROI отрицательный. AI works для mid-tier (50-1000 bopd) wells.
- **Mode ≠ brand:** «Predictive maintenance» — это **mode**; «Aspen Mtell» — **brand**. Operators могут use multiple brands.

### 1.2. Refinery / petrochemical process control

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Honeywell UOP** | Connected Services | Process+asset models + ML | 310+ units connected 2024 → 750+ planned [VFY-day-of] |
| **AspenTech (Emerson)** | aspenONE V14.3+, Mtell | APC + ML | Mainstream post-Emerson acquisition |
| **Yokogawa** | OpreX AI | AI controllers (e.g., Idemitsu) | Demonstration-stage, narrow loops |
| **ABB** | Ability Genix | Industrial analytics platform | Mid-tier refineries |
| **Emerson** | DeltaV + APC | Distributed control + ML augmentation | Mainstream, post-AspenTech consolidation |

**Anti-hype:**
- **«Autonomous refinery» — overpromise.** Cross-unit AI orchestration stagnates 2010s-2020s. **Mid-2020s reality:** AI augments narrow loops (single column, one heater), не plant-wide.
- **Multi-physics constraints** (mass + energy + reaction kinetics + corrosion) — ML surrogates lose consistency на edge cases.
- **Regulatory:** SIL3/SIL4 safety logic — НЕ может быть ML; deterministic, certified.

### 1.3. Digital twin platforms (production + asset performance)

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Cognite (Aker ASA)** | Cognite Data Fusion, Cognite Atlas AI | Contextualization OT data + agentic AI | Slow growth, $94M ARR 2024 +40% YoY; IPO postpone [VFY-day-of] |
| **AVEVA (Schneider Electric)** | PI System, AVEVA Insight, Process Simulation | Real-time process data + simulation | Industry standard (acquisition Schneider 2023) |
| **AspenTech (Emerson)** | Mtell + Inmation V14.3 | Asset performance + data context | Post-acquisition integration |
| **GE Digital (Predix)** | APM, Smart Signal | Asset performance + predictive | Declining vs Cognite/Aveva [VFY-day-of] |
| **Honeywell** | Forge | Cross-industry IIoT platform | Stable |
| **Microsoft + Aramco** | Industrial Cloud | Internal Aramco platform on Azure | NOC-specific |

**Anti-hype:**
- **«Digital twin» — overused term.** Реальные deployments часто = contextualized OT data dashboards, не physics-coupled twins.
- **TCO model lifecycle:** keep data fresh, retrain — staffing burden often > savings.

### 1.4. Drilling automation

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Nabors** | PACE-X rigs | Autonomous drilling | Record laterals 4-mile в Bakken/Haynesville/Delaware 2024-2025 |
| **Precision Drilling** | AlphaAutomation | Autonomous drilling | Competitor; less public KPIs |
| **NOV** | NOVOS | Drilling control system | Mainstream OEM integration |
| **Helmerich & Payne** | FlexRig + autonomous packages | Autonomous + super-spec rigs | US shale dominant |

**Anti-hype:**
- **«Full unmanned rig» — NOT promised.** Operators retain crew для intervention.
- **Best results в predictable formations** (Permian, Bakken laterals); frontier offshore — much more human-supervised.

---

## §2. Q3 — Low data + high physics: Frontier exploration + reservoir simulation

### 2.1. Seismic interpretation + exploration AI

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **SLB** | Petrel, Delfi, Lumi (Sep 2024) | Foundation models + cloud | Lumi launch leading; Aker BP/Shell/Azule customers |
| **Halliburton** | DecisionSpace Geology + iEnergy | E&P cloud platform | Microsoft Azure-based |
| **Aramco + G42 / Microsoft** | METABRAIN, GAIA | 250B params LLM, 90 лет data | Internal Saudi Arabia |
| **CGG** | GeoSoftware, AI seismic | Imaging + interpretation | Service vendor, smaller scale |
| **Eni** | HPC6 + internal ML | Supercomputer-based | Self-contained Italy |
| **bp + Beyond Limits** | (Legacy) | Cognitive AI | **Discontinued / quiet 2022+** |

**Anti-hype:**
- **«AI обнаружит новый bonanza»** — overclaim. Generative models accelerate interpretation, не replace structural geology + analog reasoning.
- **Foundation models trained на Permian** → fail on East African Rift basin (no analog).
- **Senior geophysicist + classical interpretation** остаётся essential для frontier basins.

### 2.2. Reservoir simulation (physics + ML surrogate)

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **SLB** | Eclipse, INTERSECT | Industry standard physics simulators | Mainstream; ML surrogate как acceleration tool |
| **CMG** | IMEX, STARS, GEM | Compositional, thermal, EOR | Niche but solid |
| **TUPREP** | TU-E2CO v1.0 (2024) | Deep-learning surrogate | Research/academic |
| **OpenFOAM** | Open-source CFD | CCS modelling + general | Academic + early commercial |
| **ExxonMobil** | Internal proprietary + Discovery 6 | 4D seismic + physics | Internal, world-class HPC |

**Anti-hype:**
- **ML surrogates accelerate 50-80% calendar time** для history matching — but **lose physical consistency** на extrapolation.
- **Physics-informed neural networks (PINN)** — research-grade, не industrial-scale 2026.
- **Eclipse remains industry standard** — для regulatory submissions, partner allocations, custody allocations.

### 2.3. HPC + Foundation model infrastructure

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **NVIDIA** | Grace Hopper Superchip, H100 GPUs | HPC hardware | Dominant (Discovery 6 Exxon, SLB Lumi, Saudi G42) |
| **AMD** | MI250X, MI300 GPUs | HPC hardware | Challenger (Eni HPC6) |
| **HPE Cray** | EX235a, EX4000 | Supercomputer integrator | Top500 deployments |
| **Microsoft Azure** | Cloud + AI services | Hyperscaler | Partner ExxonMobil, Aramco, Shell |
| **AWS** | EC2 HPC + Bedrock | Hyperscaler | Aker BP, Equinor, Shell |
| **Google Cloud** | TPU + Vertex AI | Hyperscaler | Saudi Aramco, Shell |

**Anti-hype:**
- **«Build your own foundation model»** — only super-majors могут afford ($100M+ HPC + data infrastructure).
- **Most operators** lease cloud — это создаёт vendor lock-in concerns.

---

## §3. Q2 — High data + low physics: Methane MRV + ESG

### 3.1. Satellite methane detection

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **GHGSat** | 16-satellite constellation 2025 | Fabry-Perot spectrometer, 25 m res | Commercial growth, COP30 expansion [VFY-day-of] |
| **Carbon Mapper Coalition (Planet Labs + JPL)** | Tanager-1 (launched Aug 2024, full ops summer 2025) | NASA JPL spectrometer, facility-level | Primary post-MethaneSAT |
| **EDF MethaneSAT** | (Lost June 2025) | High-precision wide-area | **CONCLUDED** — single satellite vulnerability lesson |
| **NASA EMIT** | ISS-mounted spectrometer | Wide-area survey | Research/free data |
| **ESA Sentinel-5P TROPOMI** | Wide-area lower res (1500 ppm) | Continental scanning | Free public data |

**Anti-hype:**
- **No satellite covers small dispersed leaks** (<10-100 kg/h ~ 70% of US emissions per MethaneSAT data).
- **Wind sensitivity** — MethaneSAT 500 kg/h detection limit «in idealized conditions».
- **Detection ≠ quantification:** false attribution risk (thermal reflection, neighbor facility).

### 3.2. Aerial + drone methane detection

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Bridger Photonics** | Gas Mapping LiDAR (aircraft) | Active LiDAR | Customers ExxonMobil, ConocoPhillips, EOG |
| **SeekOps** | Drone-based methane | Drone + sensor | Midstream operators, utilities |
| **Kairos Aerospace** | Aircraft hyperspectral | Wide-area aerial | West Texas, Marcellus |
| **Carbon Mapper aircraft program** | GAO-based | Pre-Tanager era continued | California focus |

**Anti-hype:**
- **Aerial 4× более точный чем regulated OGI** (BC validation) — но не free; per-flight cost.
- **Ground OGI cameras** все ещё standard для localization + measurement verification.

### 3.3. Ground OGI + portable quantification (alternative — non-AI)

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Teledyne FLIR** | GFx320 OGI camera | Hand-held thermal IR | Compliance standard для EPA Method 21 |
| **Opgal** | EyeCGas, QOGI | Hand-held quantification | Growing для OGMP Level 5 |
| **Rebellion Photonics (Honeywell)** | Fixed hyperspectral cameras | Real-time site monitoring | Stationary deployments |
| **Picarro** | Portable laser analyzer | Direct measurement | High-accuracy CRDS |
| **LI-COR** | Portable methane analyzer | Direct measurement | Field surveys |

**Anti-hype:**
- **Hand-held OGI requires trained operator** — labour-intensive, but **best localization accuracy**.
- **EU regulator: ground measurement preferred** для compliance reporting.

### 3.4. Carbon accounting software

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Persefoni** | Climate disclosure platform | SaaS, Scope 1-2-3 | SEC + CA Climate disclosure ready |
| **Watershed** | Carbon management platform | SaaS | Enterprise tier |
| **Sweep** | ESG + carbon platform | SaaS | EU-focused, CSRD-aligned |
| **Normative** | Carbon accounting | SaaS | EU + UK |
| **SINAI** | Carbon platform | SaaS | Mid-market |

**Anti-hype:**
- **Category 3 emissions** часто estimated via AI proxies — vulnerable к audit challenges.
- **Greenwashing risk** — software vendors не immune к customer mismanagement.

### 3.5. AI-driven methane analytics (vendor-neutral)

| Vendor | Product | Mode |
|---|---|---|
| **Project Canary** | Methane analytics + ESG ratings | Continuous monitoring + analytics |
| **Highwood Emissions Management** | Methane research + bulletins | Analyst service |
| **OGMP 2.0** | International framework (UNEP) | Reporting standard reference |

---

## §4. Q4 — Both low: Energy transition (CCS + EGS + new vectors)

### 4.1. CCS modelling + monitoring

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Northern Lights JV (Equinor + Shell + TotalEnergies)** | Cross-border CO₂ transport+storage hub | Geologic storage North Sea | First commercial, 1.5 Mt/year capacity from 2024 |
| **Aker Carbon Capture** | Capture technology + AI optimization | Solvent-based capture | Growing |
| **SLB** | New Energy + Delfi for CCS | Modelling + monitoring | Early offerings |
| **Schlumberger New Energy** | (rebranded SLB) | Same | Same |
| **Eni HPC6** | Internal CCS modelling | Long-horizon plume migration | Internal Italy |

**Anti-hype:**
- **190× scale-up gap to IEA target** (~40 Mt/year current → 7.6 Gt/year 2050).
- **AI plume migration prediction** — short-term decent, **long-term (100 years) uncertain**.
- **Site selection AI** — accelerates initial screening, but final due diligence requires geologic field work.

### 4.2. Enhanced Geothermal Systems (EGS)

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Fervo Energy** | EGS + fiber optic sensing | Horizontal drilling adapted O&G | IPO May 2026 +331%; $206M financing June 2025 |
| **Eavor Technologies** | Closed-loop geothermal | Canadian engineered geothermal | Funding rounds growing |
| **Sage Geosystems** | EGS + energy storage | Pressure-based storage | Early stage |
| **Quaise Energy** | Millimeter-wave drilling | Deep drilling tech | Research/pilot |

**Adoption direction:** **Strong tailwind from AI data center demand** для 24/7 clean power. **«Geothermal renaissance»** label common 2024-2026.

**Anti-hype:**
- **Scale-up uncertain** — Fervo Cape Station Utah target $206M / **early-stage**.
- **AI is enabler, не disrupting tech** — geothermal physics + drilling are core.

### 4.3. Hydrogen + ammonia (early AI applications)

| Vendor | Product | Mode |
|---|---|---|
| **Aker Solutions, Yara, NEOM Green Hydrogen** | Various | Early-stage AI for process optimization |
| **HIF Global** | E-fuels production | Pilot stage |

**Anti-hype:** Hydrogen economy slow-walking; AI applications largely speculative beyond optimization of existing chemistry.

---

## §5. Cybersecurity — cross-cutting

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Dragos** | OT security platform | ICS/SCADA anomaly detection | Growing post-Colonial Pipeline |
| **Claroty** | OT/IoT security | Asset inventory + threat detection | Mainstream |
| **Nozomi Networks** | OT security | Anomaly detection | Mainstream |
| **CrowdStrike, SentinelOne** | IT-side endpoint security | EDR | Mainstream IT |

**Anti-hype:**
- **AI offensive** (LLM-aided reconnaissance, automated phishing) outpaces **AI defensive**.
- **Ransomware +935% 2024-2025** despite vendor maturity → enterprise gaps remain.

---

## §6. Russia-specific

| Vendor | Product | Mode | Direction |
|---|---|---|---|
| **Gazprom Neft IT** | Cognitive Geologist (internal continuation post-IBM), Cognitive system for oil prospecting | ML+probabilistic reasoning | Yamal new field 2024; +40% production projects к 2030 cycle target |
| **Rosneft** | Digital Field + 23 software products (10 commercial) | Internal platform Bashneft Ilishevskoye | +1 Mt/год extra production, ~1B rubles/год |
| **Cognitive Pilot (Sberbank + Cognitive Tech JV)** | Cognitive Agro Pilot | Autonomous farm equipment | 700+ installations 2021 → 1700+ к 2024 [VFY-day-of]; primarily ag, transferable к heavy O&G equipment |
| **AIQ (ADNOC + G42, 51% Presight)** | Joint venture | AI commercialization | Partnership с Газпром нефть |
| **Татнефть** | АнтиХрупкий завод Нижнекамск, others | Limited public info | [VFY-day-of] |
| **ЛУКОЙЛ** | Volga-Ural digital fields | Limited public info | [VFY-day-of] |
| **Сургутнефтегаз** | Closed | No public info | [VFY-day-of] |

**Russia-specific anti-hype:**
- **Sanctions cut access** к Western digital tools post-2022 — drive internal development.
- **Insourcing risk:** smaller Russian operators не имеют ресурсов как Газпром / Rosneft для internal AI dev.
- **Talent gap:** AI engineers с O&G domain expertise — Сколтех, МГУ, МФТИ, Cognitive Technologies primary sources.

---

## §7. Cross-cutting recommendations для plan

### Per-quadrant section должен включать:

1. **2-4 named vendors** с product names (mode ≠ brand).
2. **Adoption direction** in words (growing / mainstream / stagnating / declining) — без точных % если volatile.
3. **Anti-hype/boundary statement** — где этот vendor НЕ работает.
4. **At least 1 alternative tool** (не-AI или другой класс AI).
5. **At least 1 failure / limitation** documented (per AI-Failure rule integration).

### Volatile numbers → `[VFY-day-of]`:

- Cognite ARR (94M 2024 confirmed; trajectory uncertain).
- Cognitive Pilot installations (700+ confirmed 2021; 1700+ к 2024 needs verification).
- SLB Lumi customer count (growing, exact number not public).
- Aramco METABRAIN parameter count (was 7B, then 250B, claimed 1T — needs day-of verification).
- ExxonMobil Discovery 6 capex (estimate $200-400M, not public).

### Brand allowlist для anti-Russification:

Brands that may appear в visible body / speech (RU lecture):
- Companies: SLB, Halliburton, Baker Hughes, NVIDIA, AMD, HPE Cray, Microsoft Azure, AWS, Google Cloud, Aramco, ADNOC, BP, Shell, ExxonMobil, Chevron, ConocoPhillips, Eni, Equinor, TotalEnergies, Aker BP, Reliance, Газпром нефть, Роснефть, Татнефть, ЛУКОЙЛ.
- Products: Eclipse, INTERSECT, Petrel, Delfi, Lumi, METABRAIN, GAIA, Aspen Mtell, aspenONE, DeltaV, Genix, OpreX, PACE-X, AlphaAutomation, NOVOS, FlexRig, Cognite Data Fusion, AVEVA Insight, PI System, Discovery 6, HPC6, MethaneSAT, Tanager-1, Carbon Mapper, GHGSat, Bridger Photonics, OGI, OGMP.
- Standards: SIL3, SIL4, OGMP 2.0, EU 2024/1787, Subpart W, EPA Method 21, ISA-84, IEC 61511.
- Russian: Cognitive Geo, Cognitive Geologist, Cognitive Agro Pilot, AIQ, Digital Field, Ilishevskoye.

Russification обязательна для general terms (англицизмы должны переводиться):
- foundation model → большая базовая модель / фундаментальная модель
- artificial lift → искусственный лифт (нефтегазовый термин ОК на русском)
- ESP (electric submersible pump) → электроцентробежный насос (ЭЦН) — стандарт RU
- digital twin → цифровой двойник
- predictive maintenance → предиктивное обслуживание / упреждающее ТО
- alert fatigue → усталость от ложных срабатываний
- pilot purgatory → застрявшие в пилоте
- frontier exploration → разведка новых бассейнов
- mature field → разработанное / зрелое месторождение
- compliance → соответствие нормам / комплаенс
- carbon accounting → углеродный учёт

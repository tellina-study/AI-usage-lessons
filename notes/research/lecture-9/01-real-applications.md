# 01 — Real Applications: Where AI Actually Works in Aerospace & Defense (2024–2026)

**Цель файла.** Каталог конкретных кейсов AI/ML в аэрокосмосе и оборонке с компаниями, годами, методами и метриками. Использовать как pool для отбора 5–8 кейсов в plan лекции.

**Принцип отбора.** Каждый кейс — задокументированный (URL + год), с конкретным AI-методом (CV / ML / DL / RL / LLM / GAN / PINN / diffusion / RL-policy) и измеряемым результатом или конкретной capability. Никаких «AI помогает оптимизировать процессы».

**Volatile-цифры** (контракты, число систем в производстве, корпоративные оценки) помечены `[VFY-day-of]` — проверять в день лекции.

---

## 1. ISR / Satellite Imagery Analysis

### 1.1 Maxar Sentry — predictive intelligence suite (2025)
- **Что.** AI-software, мониторит сотни сайтов и судов глобально, выявляет аномалии до того, как событие развернётся.
- **Что под капотом.** ML-модели обучены на 250+ петабайт архива very-high-resolution имагери Maxar за 20+ лет; multi-sensor tipping & cueing (электро-оптика + SAR + AIS для судов).
- **Контракт.** NGA Luno A D01 task order: AI-генерируемая детекция самолётов, кораблей, машин в течение часов после съёмки.
- **Запущено:** 25 июня 2025.
- Источники: [Defense One](https://www.defenseone.com/technology/2025/06/maxar-launching-ai-powered-predictive-intelligence-spot-crises-they-happen/406326/), [BusinessWire](https://www.businesswire.com/news/home/20250625291245/en/Maxar-Launches-Sentry-a-Breakthrough-Persistent-Monitoring-Suite-that-Delivers-Predictive-Intelligence-at-Global-Scale), [Military Aerospace — NGA Luno](https://www.militaryaerospace.com/home/article/55300435/nga-taps-maxar-commercial-tech-for-ai-driven-object-detection).

### 1.2 BlackSky Gen-3 + Spectra AI (2025)
- **Что.** Constellation high-frequency + very-high-resolution → AI-derived insights на скорости конфликта.
- **Цифры.** Revenue 2024 = $102.1M (imagery & analytics $70.1M); прогноз 2025 +30%; $100M+ 7-летний international subscription contract на Gen-2+Gen-3.
- **Метод.** ML-классификация и change detection на потоке снимков; интеграция с правительственными клиентами.
- Источники: [BlackSky 8-K Q4 2024](https://www.sec.gov/Archives/edgar/data/0001753539/000175353925000005/exhibit991-blackskyq42024e.htm), [BlackSky 8-K Q2 2025](https://www.sec.gov/Archives/edgar/data/0001753539/000175353925000091/exhibit991-blackskyq22025e.htm).

### 1.3 Planet Labs — AI-powered global monitoring
- **Что.** Daily revisit на оптических снимках + ML-классификация для defence/intel customers (NRO contracts).
- **Контракт.** NRO Electro-Optical Commercial Layer (EOCL) — $146M первый этап + последующие traunches. `[VFY-day-of]` — цифры контрактов растут.
- **Метод.** CNN-based object detection (vehicles, ships, aircraft, construction); change detection через diff между revisits.
- Источники: [Planet Labs Investor Relations](https://investors.planet.com/).

### 1.4 Slingshot Aerospace Agatha + TALOS (2024–2025)
- **Что.** Photometric "fingerprinting" спутников через ML; Agatha (с DARPA) для LEO/MEO/GEO anomaly detection.
- **Цифры.** 204 сенсора в 21 локации на 5 континентах; TALOS launched 2025-07.
- **Метод.** ML-classification над high-volume photometric data + RNN/transformer-based anomaly detection.
- Источники: [Slingshot AMOS recap](https://www.slingshot.space/news/amos-recap-revolutionizing-space-situational-awareness-through-applied-ai-ml), [Slingshot TALOS launch](https://www.businesswire.com/news/home/20250729156425/en/Slingshot-Aerospace-Launches-TALOS-AI-Agent-for-Mission-Ready-Space-Operations-and-Strategy).

### 1.5 SAR analytics — Capella Space + ICEYE
- **Что.** Synthetic Aperture Radar — всепогодная съёмка → ML-классификация целей и infrastructure changes.
- **Применение.** Maritime surveillance (illegal fishing, Russian shadow fleet tracking), military infrastructure monitoring.
- Источник: [Capella](https://www.capellaspace.com/), [ICEYE](https://www.iceye.com/).

---

## 2. Predictive Maintenance — Aviation & Aerospace

### 2.1 Rolls-Royce IntelligentEngine + TotalCare (2018–2026)
- **Что.** Digital-twin + ML над telemetry с двух-сторонним real-time data flow с летающих двигателей.
- **Стек.** Microsoft Azure data lake → Databricks lakehouse → ML pipelines.
- **Метрика.** Предотвращает ~400 unplanned maintenance events в год по флоту; экономия миллионы евро.
- Источники: [Klover.ai — Rolls-Royce AI strategy](https://www.klover.ai/rolls-royce-ai-strategy-analysis-of-dominance-in-aerospace/), [CIO — Rolls-Royce digital twins](https://www.cio.com/article/188765/rolls-royce-turns-to-digital-twins-to-improve-jet-engine-efficiency.html), [Plant Services — IFS+Rolls-Royce](https://www.plantservices.com/technology/artificial-intelligence/article/33015653/case-study-ifs-and-rolls-royce-connect-the-automated-data-pipeline).

### 2.2 Airbus Skywise — predictive maintenance suite (2024–2026)
- **Что.** Cloud data platform для аэрокомпаний; ML-модели прогнозируют отказы компонентов.
- **Цифры.** ~11 600 самолётов подключены к концу 2024; ~40 customers на SFP+ ~1500 ВС; easyJet — 8.1 тонн экономия топлива/ВС/год; в июле 2024 easyJet избежал 44 отмены рейсов через SFP+.
- **Клиенты 2024.** Qantas/Jetstar (фев 2024), Korean Air (фев 2024), Philippine Airlines (нояб 2024).
- **2025 roadmap.** Расширение predictive maintenance на A220 и A350. `[VFY-day-of]`
- Источники: [Airbus — Qantas Skywise PM](https://aircraft.airbus.com/en/newsroom/press-releases/2024-02-qantas-and-jetstar-airways-to-optimise-operations-with-skywise), [Airbus — Korean Air](https://aircraft.airbus.com/en/newsroom/press-releases/2024-02-korean-air-enhances-operational-capability-with-skywise-digital), [Airbus — PAL](https://aircraft.airbus.com/en/newsroom/press-releases/2024-11-philippine-airlines-selects-airbus-for-predictive-maintenance), [Airbus — Skywise overview 2026](https://www.airbus.com/en/newsroom/stories/2026-04-with-skywise-airbus-is-re-imagining-the-digital-sky).

### 2.3 F-35 ALIS → ODIN transition (2020–2025)
- **Что.** ODIN — government-owned cloud-based logistics + predictive maintenance, заменяет ALIS.
- **Статус 2025.** ALIS final version выпущен в июне 2024; rollout ALIS-update в squadrons июль–ноябрь 2025; постепенный переход на ODIN к концу 2025. ODIN-hardware kits (29 шт.) от Lockheed Martin.
- **Capability.** Predictive maintenance over F-35 parts usage; работа в disconnected mode.
- Источники: [Air & Space Forces — F-35 dumps ALIS](https://www.airandspaceforces.com/f-35-program-dumps-alis-for-odin/), [Defense Daily — ODIN delay](https://www.defensedaily.com/start-of-f-35-odin-software-fielding-to-squadrons-delayed-until-2025/air-force/), [Military Aerospace — Lockheed 29 ODIN kits](https://www.militaryaerospace.com/computers/article/14223139/f-35-maintenance-software).

### 2.4 Delta TechOps + Airbus Skywise research (2025)
- **Что.** Совместное расширение predictive maintenance на дополнительные fleet types.
- Источник: [AI Science Talk — Delta TechOps + Airbus](https://aisciencetalk.blog/2025/12/04/predictive-maintenance-takes-off-what-delta-techops-airbus-and-new-research-tell-us/).

---

## 3. Generative Design / Topology Optimization для аэрокосмических компонентов

### 3.1 GE Aviation engine bracket challenge (2013→продолжение)
- **Что.** Public challenge → topology optimization + DMLS 3D-печать → 70% weight reduction в кронштейне.
- **Контекст.** Eliminating 1 lb на Boeing 737 = сотни тысяч $/год airline; $10M экономии при масштабировании на флот.
- Источники: [3D Systems case study](https://www.3dsystems.com/learning-center/case-studies/topology-optimization-and-dmp-combine-meet-ge-aircraft-engine-bracket), [MDPI — GE bracket macro/meso optimization](https://www.mdpi.com/2411-9660/5/4/77).

### 3.2 NASA additive manufacturing for spacecraft (2024–2025)
- **Что.** Topology optimization + lattice structures для spacecraft components.
- **Метрика.** 30–50% weight reduction → значительный fuel efficiency boost.
- **Метод.** Reinforcement Learning + topology optimization (Proximal Policy Optimization).
- Источники: [PMC — RL-based topology optimization 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12355488/), [ASME J. Mech. Des. 2026](https://asmedigitalcollection.asme.org/mechanicaldesign/article/148/1/014501/1218561/Topological-Optimization-and-Generative-Design-for).

### 3.3 Drone frame generative design (2025)
- **Что.** Generative design + simulation + 3D-печать рамы quadcopter → 18% weight reduction.
- Источник: [MDPI — quadcopter generative design 2025](https://www.mdpi.com/2076-3417/15/17/9647).

> Связь с lec-06 (CAD/CAM): generative design — общая техника. Lec-09 показывает, как aerospace-specific constraints (вакуум, экстремальные температуры, fatigue в полёте) меняют loss-functions и validation pipelines.

---

## 4. Mission Planning & Decision Support

### 4.1 Palantir Maven Smart System (MSS) (2024–2026)
- **История.** Project Maven начат 2017 для analysis drone footage; Google walkout 2018 → контракт не продлён → Anduril, Palantir и др. подобрали. MSS — Palantir's UI / orchestration layer over Maven AI.
- **Контракты.**
  - May 2024: первый IDIQ $480M на 5 лет.
  - Sept 2024: дополнительные $99.8M для расширения на все рода войск (Army, AF, Navy, Space Force, Marines).
  - May 2025: ceiling boost +$795M → суммарный ceiling **~$1.3B через 2029**. `[VFY-day-of]`
- **Capability.** Объединение мульти-source intel; AI-assisted target nomination; dashboards для commanders.
- Источники: [DefenseScoop — $1B+ MSS surge](https://defensescoop.com/2025/05/23/dod-palantir-maven-smart-system-contract-increase/), [DefenseScoop — $480M IDIQ](https://defensescoop.com/2024/05/29/palantir-480-million-army-contract-maven-smart-system-artificial-intelligence/), [GovConWire — $100M expansion](https://www.govconwire.com/articles/palantir-receives-100m-army-contract-for-maven-smart-system-expansion).

### 4.2 Anduril Lattice (2025–2026)
- **Что.** AI-powered mesh OS для autonomous systems; "fabric" соединяющая sensors-shooters в low-bandwidth environments.
- **Финансы.**
  - 2025 revenue ~$2B.
  - Funding raised to date >$6B (включая $2.5B round 2025).
  - Raising $4B round @ $60B valuation (a16z + Thrive Capital). `[VFY-day-of]`
- **Mega-контракт.** Март 2026: DoD ceiling **до $20B / 10 лет** консолидирует 120+ contract actions вокруг Lattice. (Ceiling — не гарантированная сумма.)
- **Manufacturing.** Arsenal-1 ($1B factory) в Pickaway County, Ohio — Roadrunner + Barracuda + Fury CCA.
- Источники: [Anduril Wikipedia](https://en.wikipedia.org/wiki/Anduril_Industries), [DroneXL — Army $20B](https://dronexl.co/2026/03/22/army-anduril-20b-ai-counter-drone/), [Army Recognition — $20B Lattice](https://www.armyrecognition.com/news/army-news/2026/u-s-army-awards-20b-anduril-to-deploy-lattice-ai-open-architecture-for-battlefield-integration), [JPost — Army modernization](https://www.jpost.com/defense-and-tech/article-889950).

### 4.3 Scale AI Donovan + Defense Llama + Thunderforge (2023–2025)
- **2023.** Scale Donovan — первый LLM в US classified network (XVIII Airborne Corps) — 100k+ страниц orders/SitReps/intel reports.
- **Nov 2024.** Defense Llama released — fine-tune Meta Llama 3 для national security use (operations planning, adversary vulnerabilities analysis).
- **Mar 2025.** Thunderforge — multimillion-$ DoD контракт на AI-planning движение войск, кораблей, самолётов.
- **Авторизация.** FedRAMP HIGH; deploys на SC2S SIPR+, DISA IL4, JWICS.
- Источники: [BusinessWire — XVIII Airborne deal](https://www.businesswire.com/news/home/20230510005630/en/Scale-AI-Partners-with-XVIII-Airborne-Corps-for-First-LLM-Deployment-to-a-U.S.-Government-Classified-Network), [DefenseScoop — Defense Llama](https://defensescoop.com/2024/11/04/scale-ai-unveils-defense-llama-large-language-model-llm-national-security-users/), [Scale Public Sector 2025 progress](https://scale.com/blog/scale-public-sector-building-on-our-progress-in-2025).

### 4.4 Helsing Altra + Centaur (2024–2025)
- **Altra.** AI fuses ISR-drone + spotter data для land combat → high-precision battlefield situation + targeting для indirect fire.
- **Centaur.** AI fighter pilot; June 2025 успешное тестирование на Saab Gripen E.
- **Финансы.** €600M Series D (June 2025) → valuation €12B; total capital €1.37B. Daniel Ek (Spotify) chairs Prima Materia (lead investor).
- **Manufacturing.** Acquired Grob Aircraft (German light aircraft maker) June 2025.
- **Ukraine.** Анонс производства тысяч strike drones для Украины (Feb 2025).
- Источники: [Helsing — Wikipedia](https://en.wikipedia.org/wiki/Helsing_(company)), [Aviation News EU — Helsing](https://aviationnews.eu/news/2025/07/germanys-ai-defense-revolution-meet-the-startup-building-robot-fighter-pilots-and-drone-walls/), [GINC — €600M Series D](https://www.ginc.org/helsing-raises-eu600m-series-d-to-accelerate-ai-driven-defense-innovation-across-europe/), [CNBC — UK/Germany AI defense boom](https://www.cnbc.com/2025/12/11/ai-defense-boom-in-uk-and-germany-as-new-wave-of-companies-emerge.html).

---

## 5. Autonomy / Drone Swarms / Collaborative Combat Aircraft

### 5.1 Shield AI V-BAT + Hivemind (2023–2026)
- **Платформа.** V-BAT — Group 3 VTOL UAS, 12+ ч endurance, ducted-fan design, heavy-fuel engine, EW-resistant.
- **Контракты.**
  - **July 2024.** $198M USCG contract — крупнейший maritime ISR contractor-owned/operated UAV deployment.
  - **Jan 2026.** Indian Army selects V-BAT + Hivemind license; JSW Defence строит $90M facility в Hyderabad.
  - **Other.** Licensed to Singapore, South Korea.
- **Финансы.** $2B round 2025 → valuation $12.7B (по другим источникам $5.6B). `[VFY-day-of]`
- **Hivemind capability.** Autonomous pilot — sense / decide / act; работает в GPS/comms-denied environments.
- Источники: [Shield AI — Indian Army selection](https://shield.ai/shield-ai-selected-to-provide-v-bat-unmanned-aircraft-systems-and-hivemind-autonomy-software-to-the-indian-army/), [Shield AI — V-BAT block upgrade](https://shield.ai/shield-ai-unveils-v-bat-block-upgrade-powered-by-hivemind-advanced-autonomy-satcom-and-heavy-fuel-engine-among-new-features/), [TheNextWeb — $2B raise](https://thenextweb.com/news/shield-ai-2-billion-hivemind-autonomous-defence), [Fortune — Shield AI inflection](https://fortune.com/2025/12/21/shield-ai-ukraine-defense-tech-gary-steele/).

### 5.2 Anduril Fury YFQ-44A — CCA (2024–2026)
- **Что.** Unmanned combat aerial vehicle, конкурент GA YFQ-42A в Air Force CCA Increment 1.
- **TTX.** до 50 000 фт, M 0.95, 9g, Williams FJ44-4M (4000 lbf thrust).
- **Milestones.** First flight 31 окт 2025; flying with AIM-120 AMRAAM; controlled by Shield AI Hivemind + Anduril Lattice; production starts 23 мар 2026 на Arsenal-1.
- Источники: [Anduril YFQ-44 — Wikipedia](https://en.wikipedia.org/wiki/Anduril_YFQ-44), [Air & Space Forces — Arsenal-1](https://www.airandspaceforces.com/look-anduril-new-factory-cca-production/), [TheAviationist — YFQ-44A production](https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/).

### 5.3 DARPA ACE — X-62A VISTA AI dogfight (2023–2024)
- **Что.** First in-air AI vs human dogfight test на modified F-16 (X-62A VISTA).
- **Milestones.**
  - Dec 2022 — testing begins.
  - Feb 2023 — 12 flights at Edwards.
  - Sept 2023 — first AI vs manned F-16 (defensive → offensive → 2000ft nose-to-nose @ 1200 mph).
  - May 2024 — USAF Secretary Kendall flies in AI-piloted X-62A.
- **Объём.** 100k+ lines of flight-critical software changes; 21 test flights в течение года.
- Источники: [DARPA ACE world first](https://www.darpa.mil/news/2024/ace-ai-aerospace), [Aviationist — X-62 VISTA dogfight](https://theaviationist.com/2024/04/18/ai-flew-x-62-vista-during-dogfight/), [Defense News — AI dogfights](https://www.defensenews.com/air/2024/04/19/us-air-force-stages-dogfights-with-ai-flown-fighter-jet/), [Lockheed — Kendall flies VISTA](https://news.lockheedmartin.com/2024-05-03-U-S-Air-Force-Secretary-Kendall-Flies-in-AI-piloted-X-62A-VISTA).

### 5.4 Lockheed Skunk Works AI battle management (2024–2025)
- **Nov 2024.** Airborne battle manager (на L-39 Albatros) назначает targets двум AI-controlled L-29 Delfin jets, побеждающим mock enemies. Третий test такого типа; первый с real-time human battle manager.
- **Dec 2025.** AI mission-contingency demo на Stalker XE Block 25 UAV + Alta X 2.0 — AI auto-reassigns mission tasks при fuel anomaly.
- Источники: [Lockheed — Skunk Works AI battle mgmt](https://news.lockheedmartin.com/2024-11-21-Skunk-Works-R-Demonstrates-Airborne-Battle-Management-of-AI-Controlled-Aircraft), [Lockheed — Stalker AI mission contingency](https://news.lockheedmartin.com/2025-12-04-Lockheed-Martin-Skunk-Works-R-Showcases-AI-Driven-Mission-Contingency-Management-on-an-Autonomous-UAV-Demonstration).

### 5.5 DoD Replicator program (2023–2025)
- **Цель.** Развернуть тысячи autonomous attritable систем к августу 2025.
- **Реальность (Sept 2025).** "Сотни" а не "тысячи" доставлены к deadline. Replicator-2 (Sept 2024) — counter-UAS focus. `[VFY-day-of]`
- **Уроки.** Persistent technical/integration issues; software для command-and-control тысячами разнородных drones — самое слабое звено.
- **2026.** DAWG (DoD Autonomous Weapons Group?) преемник Replicator с фокусом на larger UAS.
- Источники: [DefenseScoop — Replicator successful transition?](https://defensescoop.com/2025/09/03/dod-replicator-drone-tech-transition-fielding-questions-linger/), [Breaking Defense — DAWG successor](https://breakingdefense.com/2025/12/its-alive-biden-era-replicator-drone-initiative-lives-on-as-dawg-looking-at-bigger-uass/), [Responsible Statecraft — Replicator still waiting](https://responsiblestatecraft.org/replicator/).

### 5.6 Ukraine Saker Scout + Brave1 platform (2023–2026)
- **Saker Scout.** Identifies до 64 targets autonomously; 10 km range; CV для target ID; transmits coordinates под EW.
- **Brave1.** Гос-платформа Украины с апреля 2023 — 300+ AI-разработок registered; 70+ AI/CV systems в active battlefield use.
- **2024.** Закупки 10 000 AI-enhanced drones из ~2 млн drones, построенных Украиной.
- **Dec 2024.** Первый fully unmanned ground operation near Lyptsi (UGV + FPV drones, no infantry).
- **2025.** AI-mother-drone доставляющий 2 AI-FPV strike drones за 300 km behind enemy lines.
- Источники: [Modern War Institute — autonomous arms race](https://mwi.westpoint.edu/battlefield-drones-and-the-accelerating-autonomous-arms-race-in-ukraine/), [CSIS — Ukraine AI-autonomous warfare](https://www.csis.org/analysis/ukraines-future-vision-and-current-capabilities-waging-ai-enabled-autonomous-warfare), [Kyiv Independent — mother drone](https://kyivindependent.com/ukraines-ai-powered-mother-drone-sees-first-combat-use-minister-says/), [Brave1 Wikipedia](https://en.wikipedia.org/wiki/Brave1).

### 5.7 China CETC Atlas swarm + Jiu Tian mothership (2024–2025)
- **Atlas.** AI-coordinated swarm — 1 оператор с tablet → 96 drones полный combat cycle (recon / jamming / attack). Debut at Airshow China 2024; full functionality March 2026.
- **Jiu Tian SS-UAV.** High-altitude long-endurance drone "mothership" (25м wingspan) — 100–150 loitering munitions. First flight June 2025.
- **DeepSeek integration.** PLA интегрирует DeepSeek AI в drone swarms и robot dogs (Oct 2025 reporting).
- Источники: [WeAreTheMighty — Atlas swarm](https://www.wearethemighty.com/tactical/chinas-atlas-system-the-future-of-ai-swarm-warfare/), [Army Recognition — Jiutian](https://www.armyrecognition.com/news/aerospace-news/2025/china-flies-jiutian-worlds-largest-unmanned-aircraft-designed-to-deploy-100-drones), [DroneXL — China DeepSeek + swarms](https://dronexl.co/2025/10/28/china-military-deepseek-ai-drone-swarms-robot-dogs/), [CNA — PRC UAV swarms](https://www.cna.org/reports/2025/07/PRC-Concepts-for-UAV-Swarms-in-Future-Warfare.pdf).

### 5.8 China J-20S "quarterback" stealth + AI (2025)
- **J-20S.** Twin-seat variant оптимизирован для manned-unmanned teaming + drone swarm coordination + airborne command-node. Service entry mid-2025; 300+ J-20 единиц к Oct 2025; 50+ delivered в 2024–2025.
- **J-35 carrier-based.** CATOBAR certified Sept 2025 — первый 5th-gen с электромагнитной катапульты.
- **Lead designer Wang Yongqing (2025):** AI "генерирует новые идеи и подходы для aerospace development".
- **AI-driven production.** "Dark factory" — AI-assisted QC и автономный manufacturing; production rate doubled.
- Источники: [Wikipedia — J-20](https://en.wikipedia.org/wiki/Chengdu_J-20), [Interesting Engineering — J-20 AI upgrades](https://interestingengineering.com/military/china-to-enhance-j-20-stealth-fighter), [Asia Times — China AI for stealth](https://asiatimes.com/2025/07/chinas-ai-leap-elevating-stealth-fighter-ambitions/), [Defence Security Asia — Dark Factory](https://defencesecurityasia.com/en/china-ai-dark-factory-j20-stealth-fighter-production-pacific-airpower-balance/).

---

## 6. CFD / Wind-Tunnel Surrogate Models / PINNs

### 6.1 PINNs for transonic flows (DLR, 2025)
- **Что.** Physics-Informed NN для inviscid transonic flows around airfoils.
- **Опубликовано.** Physics of Fluids 2025; DLR Quantum Computing Initiative как HPC backer.
- **Tech.** Gradient-enhanced PINNs (gPINN) + volume-weighted (VW-PINN) — стабилизация loss minimization в aero benchmarks.
- Источник: [AIP Pubs — PINN transonic airfoil](https://pubs.aip.org/aip/pof/article/37/8/086169/3360261/Physics-informed-neural-networks-for-inviscid).

### 6.2 PINNs для real-time spacecraft thermal simulation (2024)
- **Что.** Hybrid model для real-time thermal-state prediction для autonomous space missions.
- Источник: [Investigations on PINNs for Aerodynamics — arXiv](https://arxiv.org/pdf/2403.17470).

### 6.3 ML-based wind-tunnel surrogates — Airbus, Boeing
- **Что.** Replace часть CFD-runs ML-surrogates → 10–100× faster preliminary design loop.
- Источник: [Klover — Lockheed AI factory](https://www.klover.ai/lockheed-martin-ai-strategy-analysis-of-dominance-in-aerospace-defense/) (как пример MLOps stack).

---

## 7. Mission Control / Space Science Decision Support

### 7.1 NASA Frontier Development Lab (FDL) (2016–2026)
- **FDL-X Heliolab 2024.** 4 challenges — geomagnetic forecasting (DAGGER++, SHEATH-DAGGER); thermospheric density (Karman).
- **2025.** FOXES — ML-модель predicts strength & location of solar flares from SDO EUV images.
- **Партнёры.** Google Cloud, NASA Ames, SETI Institute, DOE.
- Источники: [FDL 2024](https://fdl.ai/fdl2024), [FDL 2025](https://fdl.ai/heliolab25), [NASA on FDL](https://www.nasa.gov/missions/nasa-takes-a-cue-from-silicon-valley-to-hatch-artificial-intelligence-technologies/).

### 7.2 NVIDIA Earth-2 climate digital twin (2024–2026)
- **Что.** FourCastNet (Modulus + Omniverse) emulates + predicts hurricanes / atmospheric rivers ~45 000× быстрее classical.
- **Use case в aerospace.** Mission planning для launches; weather risk assessment для UAS / commercial aviation.
- Источники: [NVIDIA Earth-2 newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-earth-climate-digital-twin), [NVIDIA scientific DT platform](https://nvidianews.nvidia.com/news/nvidia-announces-digital-twin-platform-for-scientific-computing).

---

## 8. Space Situational Awareness / Missile Tracking

### 8.1 SDA Proliferated Warfighter Space Architecture (PWSA) — Tracking Layer (2025)
- **Что.** Сотни LEO-спутников для missile warning + tracking + fire-control quality tracks (особенно гиперзвук).
- **Контракт Dec 2025.** $3.5B / 4 contracts (Lockheed, Rocket Lab, Northrop Grumman, L3Harris) — 72 спутника Tranche 3; launch ~FY2029.
- **Capability.** Near-continuous global coverage для missile warning/tracking; половина constellation — missile-defense payloads.
- Источники: [SDA T3 awards](https://www.sda.mil/space-development-agency-makes-awards-to-build-72-tracking-layer-satellites-for-tranche-3/), [DefenseScoop — $3.5B 4 contracts](https://defensescoop.com/2025/12/19/sda-tranche-3-missile-tracking-layer-contract-awards/), [Spaceflight Now — SDA $3.5B](https://spaceflightnow.com/2025/12/20/space-development-agency-awards-roughly-3-5-billion-to-4-companies-for-72-missile-tracking-and-warning-satellites/).

### 8.2 Slingshot Aerospace + USSF GPS jamming/spoofing detection (2025)
- **Что.** Slingshot sensors + ML предоставляют USSF threat detection вокруг GPS jamming/spoofing.
- **Sovereign SDA platform.** Запущен Apr 2025 — нации могут быстро развернуть AI-driven SDA capability.
- Источники: [SatNews — USSF jamming detection](https://news.satnews.com/2025/01/16/slingshot-aerospace-to-provide-tech-to-ussf-to-detect-gps-jamming-spoofing-threats/), [Slingshot — Sovereign SDA](https://www.slingshot.space/news/slingshot-aerospace-debuts-worlds-first-rapid-space-domain-awareness-enablement-package).

### 8.3 LeoLabs orbital intelligence (2024–2026)
- **Что.** Phased-array radar network + ML — detect / track / characterize orbital objects (включая deorbit risks, hostile rendez-vous).
- Источник: [LeoLabs](https://leolabs.space/).

---

## 9. Synthetic Data & Training Simulators

### 9.1 Diffusion-based synthetic imagery для military object detection (2023–2024)
- **Что.** Stable Diffusion + DALL-E генерируют synthetic training data для CV-моделей в low-data domains (e.g., new military vehicle classes).
- **Метрика.** Class-specific diffusion models улучшают precision для object detectors в challenging domains.
- **DoD context.** Microsoft pitched DALL-E to DoD (2023) для battlefield management systems. OpenAI removed blanket ban on military use January 2024.
- Источники: [arXiv — class-specific diffusion military object detection](https://arxiv.org/html/2604.18076v1), [DALL-E Wikipedia](https://en.wikipedia.org/wiki/DALL-E), [ITEA — synthetic data for target acquisition](https://itea.org/journals/volume-45-4/synthetic-data-for-target-acquisition/).

### 9.2 NVIDIA Omniverse для defense simulation (2024–2025)
- **Что.** Real-time physics digital twins для aerospace/defense/manufacturing.
- **Capability.** 1200× faster simulations + real-time visualization; physics-AI frameworks.
- **Use case.** Synthetic training environments для autonomous systems перед field testing.
- Источники: [NVIDIA — Omniverse real-time physics DT](https://investor.nvidia.com/news/press-release-details/2024/NVIDIA-Announces-Omniverse-Real-Time-Physics-Digital-TwinsWith-Industry-Software-Leaders/default.aspx), [NVIDIA Mega Omniverse blueprint](https://blogs.nvidia.com/blog/mega-omniverse-blueprint/).

---

## 10. Cybersecurity / EW / GPS Spoofing Detection

### 10.1 Slingshot Aerospace — GPS jamming detection (см. 8.2)

### 10.2 Russian EW Krasukha-4 + Borisoglebsk-2 (used against Ukraine TB2)
- **Что.** Russian EW jamming/spoofing degraded Bayraktar TB2 navigation precision.
- **2024 data.** Latvia recorded 820 satellite signal interference cases (vs 26 в 2022).
- Источники: [PBS — Russia GPS jamming](https://www.pbs.org/newshour/world/what-to-know-about-russias-gps-jamming-of-a-european-officials-plane), [Stanford SCPNT — Russia spoofing 2023-24](https://web.stanford.edu/group/scpnt/gpslab/pubs/papers/Lo_ION_ITM_2025_Russia_Spoofing.pdf), [Foreign Policy — war-zone spoofing civil aviation](https://foreignpolicy.com/2024/03/19/war-zone-gps-spoofing-threat-civil-aviation-russia-iran/).

### 10.3 ATR adversarial defense via Bayesian NN (2024)
- **Что.** Uncertainty-aware SAR ATR — Bayesian NN flags adversarial inputs.
- Источники: [arXiv — Bayesian SAR ATR](https://arxiv.org/pdf/2403.18318), [arXiv — realistic scatterer SAR adversarial](https://arxiv.org/abs/2312.02912).

---

## 11. Supply Chain / Logistics

### 11.1 Lockheed Martin AI Factory + JADC2 (2024–2026)
- **Что.** Lockheed AI Center (LAIC) + "AI Factory" — MLOps backbone для enterprise-scale AI.
- **JADC2 contract.** AIR contract — AI tools для dynamic airborne missions.
- **JASSM contract.** $3.23B sole-source 2024 (не AI, контекст индустрии).
- Источники: [Klover — Lockheed AI strategy](https://www.klover.ai/lockheed-martin-ai-strategy-analysis-of-dominance-in-aerospace-defense/), [Army Recognition — Lockheed AI/ML](https://www.armyrecognition.com/news/aerospace-news/2024/lockheed-martin-utilizes-ai-and-machine-learning-to-transform-defense-and-space-technology).

---

## 12. eVTOL / Autonomous Air Mobility (gray-zone между civil & defense)

### 12.1 Wisk Aero Generation 6 (Boeing subsidiary, 2025–2026)
- **Что.** First-ever FAA-certified candidate для commercial autonomous passenger flight (no cockpit controls вообще).
- **Milestones.** Maiden flight Gen-6 Dec 16, 2025; second Gen-6 May 4, 2026; 1750+ test flights; supervisor model — 1 человек на 3 aircraft.
- **NASA partnership.** Non-reimbursable Space Act agreement — integration autonomous aircraft в NAS.
- **Certification target.** 2030.
- **Counterpoint.** Lilium bankrupt Oct 2024 — eVTOL сектор brutal capital burn.
- Источники: [FlyingMag — Wisk doubles autonomous fleet](https://www.flyingmag.com/boeing-wisk-2nd-autonomous-air-taxi-test-flight/), [Military Aerospace — Wisk + NASA](https://www.militaryaerospace.com/uncrewed/article/55292831/boeings-wisk-evtol-unit-partners-with-nasa-to-integrate-autonomous-aircraft), [Weekly Driver — Wisk $2B question](https://theweeklydriver.com/2025/12/wisk-aeros-autonomous-air-taxi-gen-6/), [DroneXL — Gen 6 May 2026](https://dronexl.co/2026/05/04/wisk-aero-gen-6-autonomous-evtol-flight/).

---

## 13. Wargaming & Strategic Planning

### 13.1 US Army LLM-wargaming (2024–2026)
- **Что.** GPT-4 Turbo / GPT-4 Vision для battlefield terrain + force composition анализ в CGSC wargames.
- **Safeguards.** Prompt discipline training; "open then closed" prompting; human override protocols.
- **Air Force.** Shadow Operations Center-Nellis (ShOC-N) capstone events 2024–2025 — AI для dynamic targeting.
- Источники: [SWJ — AI-enabled wargaming CGSC](https://smallwarsjournal.com/2026/01/16/ai-enabled-wargaming-cgsc/), [Foreign Affairs — Why military can't trust AI](https://www.foreignaffairs.com/united-states/why-military-cant-trust-ai), [arXiv — LLMs in national security applications](https://arxiv.org/html/2407.03453v1).

---

## Summary table — top-25 cases (для plan лекции)

| # | Кейс | Метод | Год | Метрика / Result |
|---|------|-------|-----|------------------|
| 1 | Maxar Sentry | ML over 250 PB archive | 2025 | NGA Luno contract; hours from capture to detection |
| 2 | BlackSky Gen-3 + AI | CNN + change-detection | 2025 | $100M+ subscription contract |
| 3 | Planet Labs NRO EOCL | CNN object detection | 2024–26 | NRO EOCL Phase 1 $146M |
| 4 | Slingshot Agatha + TALOS | ML photometric fingerprinting | 2024–25 | 204 sensors, 21 locations |
| 5 | Rolls-Royce IntelligentEngine | Digital twin + ML | 2018–26 | ~400 prevented events/year |
| 6 | Airbus Skywise | Cloud ML platform | 2018–26 | 11 600 aircraft, 8.1t fuel/aircraft/year |
| 7 | F-35 ODIN (after ALIS failure) | Cloud + predictive ML | 2025 | Transition Q4 2025; 29 ODIN kits |
| 8 | GE engine bracket | Topology opt + DMLS | 2013→ | 70% weight reduction |
| 9 | NASA RL-based topology opt | RL + PPO + topo opt | 2024 | 30–50% weight reduction |
| 10 | Palantir Maven Smart System | LLM + CV + orchestration | 2024–26 | $1.3B ceiling through 2029 |
| 11 | Anduril Lattice | AI-mesh OS | 2025–26 | $20B / 10y ceiling; $60B valuation |
| 12 | Scale AI Donovan + Defense Llama | Fine-tuned Llama-3 | 2023–25 | First LLM in US classified network |
| 13 | Scale AI Thunderforge | AI movement planner | 2025 | DoD multimillion-$ contract |
| 14 | Helsing Altra + Centaur | Multi-source fusion + RL pilot | 2024–25 | €12B valuation; Gripen test |
| 15 | Shield AI V-BAT + Hivemind | Sense/decide/act autonomy | 2024–26 | $198M USCG; Indian Army contract |
| 16 | Anduril Fury YFQ-44A | CCA autonomy + Lattice/Hivemind | 2025–26 | First flight Oct 2025; production Mar 2026 |
| 17 | DARPA ACE X-62A VISTA | RL air-to-air dogfight | 2023–24 | First AI vs manned F-16 |
| 18 | Lockheed Skunk Works AI battle mgmt | AI on L-29 jets | 2024–25 | AI vs mock enemies via L-39 manager |
| 19 | DoD Replicator | Attritable autonomous fielding | 2023–25 | "Hundreds" delivered; missed scale target |
| 20 | Ukraine Saker Scout | CV target ID | 2023–25 | 64 targets autonomous ID |
| 21 | Ukraine Brave1 ecosystem | 300+ AI dev; 70+ in field use | 2023–26 | First fully unmanned op Dec 2024 |
| 22 | China CETC Atlas swarm | Multi-agent RL coordination | 2024–26 | 96-drone swarm, 1 operator |
| 23 | NASA FDL Heliolab | ML for space science | 2016–25 | DAGGER++ geomagnetic; FOXES flare prediction |
| 24 | NVIDIA Earth-2 FourCastNet | Foundation model для weather | 2024–26 | 45 000× faster than CFD |
| 25 | SDA PWSA Tracking Layer T3 | LEO missile tracking constellation | 2025 | $3.5B for 72 sats; launches FY2029 |

---

## Volatile-цифры для re-verify в день лекции (`[VFY-day-of]`)
1. Anduril revenue / funding round / valuation (всё движется).
2. Anduril $20B ceiling contract — exact value & terms.
3. Shield AI valuation (5.6B vs 12.7B расхождение в источниках).
4. Palantir MSS ceiling через 2029.
5. DoD Replicator delivered count.
6. Russian Geran-2 production rate (Alabuga).
7. Ukrainian AI-drone fielding scale.
8. China Atlas / Jiu Tian operational status.


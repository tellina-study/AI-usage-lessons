---
lecture: 13
title: "AI в логистике и транспорте"
module: 3
duration_min: 75
learning_outcomes: [LO1, LO2, LO7]
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
status: planning
version: 1
created: 2026-05-21
issue: 135
branch: issue-135-lec-13-logistics
keystone_axis: "Лестница структурированности среды — 5 уровней от controlled warehouse к exception black-swan"
prerequisites:
  - "lec-09 AI в авиакосмосе и обороне (OODA + лестница автономии)"
  - "lec-11 AI в производстве (discrete vs process + pilot purgatory)"
  - "lec-12 AI в автоматизации производства и цифровые двойники"
estimated_chapter_words: 30000
references_count_target: 90
---

# Lecture 13: AI в логистике и транспорте

## Topics Covered

- **Robotaxi коммерциализация 2025-2026** — Waymo, Apollo Go, Pony.ai, Tesla Robotaxi Austin, Cruise exit.
- **Robotruck — survivor consolidation** — Aurora первая commercial L4 (Dallas-Houston май 2025), банкротства Argo / Embark / TuSimple / Waymo Via / Starsky ($20B+ сожжено).
- **Складская роботизация** — Symbotic + Walmart 400 APD, Amazon Sparrow / Sequoia / Proteus / Vulcan, Locus AMR, port automation.
- **Последняя миля** — Starship campus, Coco LA, Zipline Africa medical, Nuro pivot 2024.
- **ML-маршрутизация и dynamic pricing** — UPS ORION (OR, не RL), surge pricing Uber.
- **Black-swan failures** — Houthi Red Sea 2024 (90% drop), Suez Ever Given 2021 (12% world trade), COVID 2020 supply chain meltdown.
- **Канонические AV-провалы** — Uber Tempe 2018 (Elaine Herzberg, first AV pedestrian fatality), Tesla Autopilot 54 verified fatalities NHTSA, Cruise GM exit December 2024 ($10B → 0).
- **Российский контекст** — КамАЗ М-11 «Нева», Cognitive Pilot Agro (590K тонн зерна), Yandex SDG санкционный split.
- **Decision framework «AI или не AI в logistics»** — OR vs RL, EOQ vs ML inventory, human dispatcher vs full automation.

## Prerequisites

- **Lecture 9** — OODA-цикл (Sense → Decide → Act), L1-L5 лестница автономии, HITL/HOOL/HOTL. **Cross-reference:** для AV (CCA wingman ↔ robotruck) и для safety-critical mindset.
- **Lecture 11** — Pilot purgatory (95% GenAI pilots fail), automation paradox (Tesla 2018), «AI augments worker, не replaces» (Toyota Jidoka 2.0). **Cross-reference:** для AV-trucking consolidation и для humanoid hype в warehouse.
- **Lecture 12** — Digital twins, factory automation. **Cross-reference:** для controlled-environment warehouse + port automation.

## Normative References

- **SAE J3016 — Levels of Driving Automation** (canonical autonomy taxonomy для AV).
- **NHTSA Standing General Order (SGO) on Crash Reporting** — обязательная regulatory data для AV в US (база Tesla / Waymo / Cruise fatality numbers).
- **ICAO Annex 10** — air navigation; запрещает full automation in ATC.
- **IMO MASS (Maritime Autonomous Surface Ships) regulatory framework** — IMO работает над международным регулированием AUSV.
- **FAA Part 107** — small UAS commercial operations (для drone delivery legal limits).
- **EU AI Act** (2024) — для AV high-risk category классификация.
- **РФ:** ЭПР (Экспериментальный Правовой Режим) для беспилотного транспорта — даёт legal basis для КамАЗ М-11 «Нева» pilot.

## Materials

- **Slides:** `library/lectures/lec-13/rendered/lec-13.{pptx,pdf}` (планируется после Phase 7).
- **Diagrams:** `library/lectures/lec-13/assets/diagrams/keystone-environment-ladder.drawio` + sub-section diagrams (планируется Phase 2-5).
- **Hero images:** Waymo Jaguar (s01) + telecom NOC (s39) через 6-tier acquisition (см. research file 06).
- **Speech:** `library/lectures/lec-13/speech.md` (~5k слов, после Phase 9).
- **Chapter:** `library/lectures/lec-13/chapter.md` (≥30k слов per § Chapter Depth Baseline для L4+).

## Learning Objectives

1. **LO1 (Remember + Apply).** Назвать 5 уровней keystone-лестницы «структурированность среды» от controlled (warehouse, port) до exception (black-swan), для каждого — по 2-4 dominant AI-tools 2026 года + направление adoption.
2. **LO2 (Evaluate).** Критически оценить заявление вендора об «autonomous robotaxi/robotruck replacing X% drivers» — отделить демо/ODD от scaled production; применить framework «среда-успех» + ask о baseline / counterfactual / regulatory readiness; разобрать как минимум 3 anti-patterns (Cruise October 2023, Embark SPAC bust, Argo AI capital intensity).
3. **LO7 (Evaluate + Apply).** Описать регуляторный ландшафт (SAE J3016, NHTSA SGO, FAA Part 107, IMO MASS, ICAO Annex 10, EU AI Act, РФ ЭПР), сформулировать ≥4 категории критериев «AI не нужен / не работает в logistics» (среда / well-defined optimization / black-swan exception / labor-policy scale), применить к учебному кейсу, предложить альтернативу (OR, scenario planning, classical formulas, human-in-loop).

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

<!-- Цена пропуска: Лекция 4 = ~5 циклов deck. methodology-critic Phase 1 + Pre-USER-GATE п.6 проверяют это. -->

- **Несущая концептуальная ось лекции (лестница 5 уровней):** **«Структурированность среды vs хаос»** — главный предиктор success AI в transport/logistics, orthogonal к SAE levels / time horizons.
  - **Уровень 1 — Controlled** (warehouse, port terminal): AI mature, Symbotic / Amazon / ZPMC.
  - **Уровень 2 — Semi-structured highway** (Interstate / магистраль): AI emerging, Aurora / Mobileye / КамАЗ.
  - **Уровень 3 — Urban robotaxi** (city streets): AI emerging но fragile, Waymo выжил / Cruise обанкротилась.
  - **Уровень 4 — City last-mile** (sidewalks, drones): AI struggling в narrow niches, Coco / Starship / Zipline (medical only).
  - **Уровень 5 — Exception / black-swan**: AI fails by definition (out-of-distribution); human dispatcher + scenario planning.

- **Keystone-слайд в Разделе 0 ДО первого погружения** (заголовок про саму ось, НЕ recap/защита подхода):
  - **Slide title:** «Лестница среды: главный предиктор успеха AI в логистике».
  - **Layout:** 5-step ladder слева направо, controlled → chaos. На каждом шаге — представитель AI + измеримый эффект + типичный failure mode.
  - **Visual progression:** clean warehouse → highway → city streets → snowy sidewalk → storm at sea.
  - **Below ladder:** «Сегодня мы пройдём эту лестницу. У каждого уровня свой AI-стек, свои failure modes, свои альтернативы».

- **Каждый раздел = мотивированный спуск/подъём по оси** (не «всплывает»):
  - §1 = уровень 1 (controlled).
  - §2 = уровень 2 (highway).
  - §3 = уровни 3+4 (urban robotaxi + last-mile).
  - §4 = уровень 5 (exception) + decision framework.

## Инструменты на каждом уровне таксономии (ENFORCED для отраслевых L4+ — Лекция 4 lesson)

<!-- Phase-0 research-бриф разметил tools ПО УРОВНЯМ несущей таксономии в research/lecture-13/05-tools-per-level.md, не общим обзором. -->

- **Уровень 1 (controlled):** Symbotic (Walmart 400 APD), Amazon Sparrow / Sequoia / Proteus / Vulcan, Locus Robotics + GreyOrange + Geek+, ABB / Konecranes / ZPMC port.
- **Уровень 2 (semi-structured highway):** Aurora Driver (Aurora Innovation), Mobileye Chauffeur (L3 eyes-off), КамАЗ-54901 + Cognitive Pilot stack, Plus.ai supervised.
- **Уровень 3 (urban robotaxi):** Waymo (Alphabet), Apollo Go (Baidu), Pony.ai + WeRide (Китай), Tesla Robotaxi Austin.
- **Уровень 4 (last-mile):** Starship Technologies, Coco Robotics, Zipline (medical Africa + commercial pilots US), Nuro (pivot 2024), Avride (Yandex SDG спин-аут).
- **Уровень 5 (exception):** **НЕ-AI инструменты** — Human dispatchers (Maersk / FedEx / UPS exception teams), Scenario planning (Shell-style), OR (Gurobi, CPLEX, OR-Tools — UPS ORION example), classical formulas (EOQ, safety stock).

- **Adoption-направление словами (растёт / стагнирует — БЕЗ точных volatile-долей на видимом слое):**
  - Уровень 1: **растёт быстро** в крупных ритейлерах и 3PL; port automation **стагнирует в US East Coast** (ILA-strikes 2024).
  - Уровень 2: **первые коммерческие операции** (Aurora май 2025), рост медленный; стартапы — **дикая консолидация**.
  - Уровень 3: US **survivor consolidation** (3 игрока), Китай **3 крупных** (Apollo Go / Pony.ai / WeRide); Europe **отстаёт**; Россия — **operational прерван** на массовом уровне (санкции Yandex SDG).
  - Уровень 4: sidewalk robots **в campus + narrow neighborhoods**, **stuck в dense urban**; drone medical Africa **растёт быстро**; drone urban US **blocked**.
  - Уровень 5: scenario planning **растёт** после COVID + Houthi + Suez; OR **стабильно зрелое**; rule-based **mainstream**.

- **Anti-hype/границы-оговорка на уровень:**
  - Уровень 1: **humanoid роботы (Optimus, Figure, UBTech) = research/pilot stage** на 2026, не production; **«lights-out warehouse»** = миф для broad SKU.
  - Уровень 2: **«AV решит trucker shortage»** — math не работает (78K дефицит vs ~10 Aurora trucks); **end-to-end DNN без HD-map** — research-stage, не production-safe для L4.
  - Уровень 3: **«vision-only достаточно»** (Tesla) — **statistically not proven** vs Waymo HD-map + LiDAR; **«robotaxi прибылен»** — Waymo сама не profitable per-trip publicly; Cruise сожгла $10B.
  - Уровень 4: **«drones заменят trucks в city»** — acoustic + FAA = multi-decade timeline; **«last-mile robots profitable»** — profitability не доказана publicly.
  - Уровень 5: **«black-swan можно ML-предсказать»** — false (по определению out-of-distribution); **«AI заменит exception teams»** — false (нет accountability + reasoning).

- **Инфраструктура (HD-maps / LiDAR / compute / cloud / simulation) отделена от «уровень-инструмент»** — детали в research file 05.

- **Volatile числа / доли / «лидер» / benchmark → `[VFY-day-of]`** (на видимом слое только направление; см. research file 07 для full list).

- **Каждый plan §-named speech-narrative имеет слайд** (Phase-5 check ENFORCED). См. mapping в research file 05 § «Mapping plan §-named narrative → слайды».

## Outline

### Раздел 0 — Вход. Лестница среды (5 минут)

- **§0.1.** Hook — три картинки рядом:
  - Cruise GM exit December 2024: **$10 миллиардов → 0**.
  - Waymo март 2026: **500 000 поездок/неделю**.
  - Tesla Robotaxi Austin: **14 ДТП за 8 месяцев**.
  - Вопрос: «Почему Waymo выжила, Cruise разорилась, а Tesla только начинает? Дело не в технологии — дело в среде».
- **§0.2. Keystone slide** — лестница 5 уровней «структурированность среды» (визуально + 1 пример на уровень).
- **§0.3.** Шесть аббревиатур, без которых дальше не пройти: SAE (Society of Automotive Engineers), ODD (Operational Design Domain), AMR (Autonomous Mobile Robot), AV (Autonomous Vehicle), OR (Operations Research), HD-map (High-Definition map).
- **§0.4. Roadmap.** Что покажу: §1 controlled (где AI работает легко), §2 highway (где first L4 commercial), §3 urban (где Cruise пала), §4 exception (где AI не работает в принципе).

**Cross-link к chapter §0.**

### Раздел 1 — Controlled environment (15 минут)

- **§1.1.** Warehouse: Symbotic + Walmart 400 APD (Jan 2025, $5B backlog). Amazon Sparrow / Sequoia / Proteus / Vulcan (~750K роботов).
- **§1.2.** AMR (Autonomous Mobile Robots): Locus Robotics 5B+ picks, GreyOrange, Geek+. **Worker workload pushback** — union concerns UK + US.
- **§1.3.** Port automation: ABB, Konecranes, ZPMC. Maasvlakte II Rotterdam, Long Beach LBCT, Yangshan Shanghai. **ILA-strikes 2024 — labor pushback в US ports**.
- **§1.4.** Rail PdM: KONUX (Deutsche Bahn).
- **§1.5. Failures / границы (3 минуты).**
  - **Humanoid hype:** Tesla Optimus / Figure 02 / UBTech Walker S1 = research/pilot, не production scale.
  - **Capital intensity:** Symbotic / port automation = десятки $M на установку; малые ритейлеры / brownfield порты не могут.
  - **«Lights-out warehouse» миф** для broad SKU.

**Cross-link к chapter §1; tools-per-level slide.**

### Раздел 2 — Semi-structured highway (15 минут)

- **§2.1.** Aurora Innovation — **первая commercial driverless trucking US** Dallas-Houston (май 2025). Crawl-walk-run подход. Расширение Fort Worth-El Paso, Phoenix.
- **§2.2.** Mobileye Chauffeur L3 eyes-off — Polestar 4, premium European OEMs (launches к концу 2025).
- **§2.3.** КамАЗ-54901 + Cognitive Pilot stack на М-11 «Нева» (67 единиц 2024, 100 запланировано 2025), расширение М-12 + ЦКАД.
- **§2.4.** UPS ORION — **canonical OR success** (100M миль/год, $300-400M savings/год). **Pedagogical:** это **OR + heuristics**, не deep learning, не RL.
- **§2.5. Failure deep-dive (10 минут — главный failure-bucket контент).**
  - **Argo AI (Oct 2022).** $7B сгорело за 5 лет; Ford $2,7B impairment.
  - **Embark Trucks (Mar 2023).** 16 месяцев от $5B SPAC IPO до банкротства.
  - **TuSimple (Jan 2024).** Delisting; assets transferred to Chinese AIGC; 91%+ shareholder loss.
  - **Waymo Via (2023).** Alphabet закрыла trucking arm — даже бесконечный capital не нашёл profitable model.
  - **Starsky Robotics (Mar 2020).** Первая волна жертв; Stefan Seltz-Axmacher essay о sim-to-real gap.
  - **Cumulative:** **>$20 миллиардов сожжено** на AV-trucking + robotaxi non-survivors 2017-2024.
  - **Lesson:** AV survivor consolidation (10:1+) — что Waymo / Aurora / Mobileye выжили = exception, не правило.
  - **«AV решит trucker shortage» — false framing.** ATA 78K дефицит; Aurora 10 машин; math не работает.

**Cross-link к chapter §2; AV-bankruptcy timeline slide; tools-per-level slide.**

### Раздел 3 — Urban robotaxi + last-mile (15 минут)

- **§3.1. Robotaxi survivors.**
  - **Waymo:** 500K rides/неделю март 2026; 3 067 машин 5-го поколения; 14M cumulative 2025; 10+ городов. HD-map + LiDAR + remote ops + formal safety case.
  - **Apollo Go (Baidu):** 240M km globally; 17M+ orders; 22 cities (октябрь 2025).
  - **Pony.ai + WeRide:** позитивный operating profit per machine в Shenzhen (Feb 2025); +761% YoY revenue.
- **§3.2. Tesla Robotaxi Austin** — текущая разработка.
  - Старт 22 июня 2025; ~10 машин с safety monitor; vision-only без LiDAR без HD-map.
  - **14 ДТП в Austin к Feb 2026; 700K paid miles cumulative.**
  - **Comparison:** sample size слишком мал для conclusion «safer than Waymo»; **не доказано**.
- **§3.3. Last-mile.**
  - **Starship:** 9M+ доставок, 60+ campus US, 150+ локаций.
  - **Coco Robotics:** 1 000+ роботов LA, 500K+ доставок, цель 10K.
  - **Zipline:** 100M миль (март 2025), 2M доставок (январь 2026), 22M доз вакцин Африка, $7,6B valuation.
  - **Nuro pivot 2024:** exit B2C delivery → licensing autonomous-stack OEM.
- **§3.4. Failure deep-dive (10 минут — bulk of urban-section failure-bucket).**
  - **Cruise GM exit (December 2024) — centerpiece.** $10B → 0 за 8 лет. October 2023 dragging incident → DMV suspension → mass layoffs → final shutdown.
  - **Uber Tempe 2018 (Elaine Herzberg).** First AV-pedestrian fatality. Uber отключил factory AEB; backup driver watching TV; system detected 5,6s до удара но failed to classify pedestrian вне crosswalk.
  - **Tesla Autopilot fatalities.** NHTSA SGO: 65 reported, 54 verified; EA22002 — 13 fatal crashes с foreseeable misuse; 2024 SGO data о reduced-visibility crashes; новое investigation 2025 о ~2,9M Tesla vehicles.
  - **Tesla Austin 14 crashes** — текущая stat (без demonization, statistical sample).
  - **«Drones заменят trucks в city»** — acoustic + FAA = multi-decade; Zipline urban US — pilots only.

**Cross-link к chapter §3; Cruise timeline slide; tools-per-level slide.**

### Раздел 4 — Где AI не работает + decision framework (15 минут)

- **§4.1. Black-swan failures — где ML слепо по определению.**
  - **Houthi Red Sea 2024.** 90% drop в container shipping за 2 месяца (Dec 2023 → Feb 2024). +30% transit time через Cape of Good Hope. ML demand forecast полностью out-of-distribution.
  - **Suez Ever Given 2021.** 6 дней блокировки; 12% world trade; $9,6B held up; **AI не имела роли — physics + pilotage**.
  - **COVID 2020.** Supply chain meltdown; just-in-time + ML demand forecast = fragile system; human exception management спасла.
  - **Trucker shortage 78K (ATA 2024).** AV не решит на горизонте 2030: math не работает.
- **§4.2. Decision framework — «AI или не AI в logistics».** 5 критериев:
  1. **Среда controlled?** Yes → AI applicable (warehouse, port). No → continue.
  2. **Задача well-defined optimization (TSP, VRP, scheduling)?** Yes → **OR (Gurobi, CPLEX, OR-Tools) лучше RL/ML**. UPS ORION = canonical proof.
  3. **Demand pattern stationary?** Yes → **EOQ + safety stock + ABC classical formulas лучше ML**. Audit: какой % SKU реально требует ML?
  4. **Safety-critical с regulatory audit?** Yes → **rule-based + human-in-loop required**; black-box ML не работает (FDA, FAA, IMO).
  5. **Event в-distribution?** Yes → ML scoring. No → **human dispatcher + scenario planning**.
- **§4.3. Альтернативные инструменты — toolkit для logistics-engineer.**
  - **OR:** Gurobi, CPLEX, Google OR-Tools.
  - **Classical inventory:** EOQ, safety stock, ABC analysis.
  - **Scenario planning:** Shell-style war games.
  - **Rule-based vision:** controlled-env inspection.
  - **Hybrid CV + signal processing:** radar, ultrasonic.
  - **Human-in-the-loop:** exception handling, accountability.
- **§4.4. Anti-hype reset.** «GenAI agent сам распланирует supply chain» — vendor pitch без production. Demand: baseline, counterfactual, ROI metric, error budget, 6-month production track record.

**Cross-link к chapter §4; black-swan timeline slide; decision-framework slide.**

### Раздел 5 — Замыкание + мост к Лекции 14 (10 минут)

- **§5.1. Семь критериев «когда AI плохая идея в logistics» — финальный recap.**
- **§5.2. Карьерный угол.** Logistics + transport AI engineer в РФ: где работа? КамАЗ + Cognitive Pilot + Сбер + Wildberries + Деловые Линии + Yandex SDG (non-Russia split). Универсальные технические университеты + профильные кафедры в области инфокоммуникаций / транспортных систем + военно-космические академии (готовят инженеров с пересекающимися навыками — см. lec-09).
- **§5.3. Список для чтения.** ATA Driver Shortage Report 2024; NTSB Highway Accident Report HAR-19/03 (Uber Tempe); Stefan Seltz-Axmacher Medium essay «The end of Starsky Robotics»; Waymo Safety Report 2025; Aurora press May 2025; Goldman Sachs China robotaxi 2025.
- **§5.4. Замыкание.** Лестница среды — главный предиктор. Survivors = те, кто **уважает среду** + **остаётся в narrow ODD** + **не overpromise**. Cruise vs Waymo — обоим тот же стек, но Waymo выжил, потому что cautious в ODD expansion. Это **lesson инженерного смирения** — не arrogance.
- **§5.5. Мост к Лекции 14.** «Завтра — телекоммуникации, сетевая инфраструктура, кибербез. Это **другая среда** (cyber instead of physical), но та же логика: AI augments human SOC analyst, OR + rule-based threat detection остаётся, ML helps в-distribution и слепо out-of-distribution. Лестница среды переходит из физического мира в сетевой».

**Cross-link к chapter §5; closing hero NOC slide.**

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

<!-- CLAUDE.md § AI-Failure & Judgment Content Rule. Холистически: ≥30% видно в chapter+slides+speech. -->

### Документированный провал ИИ + выученный урок

- **Cruise GM exit December 2024.** $10B operating losses, <$500M revenue cumulative. Trust collapse после Oct 2023 dragging incident. Lesson: один incident + DMV trust violation = killing program. Lesson: hardware OEM (GM) → software-platform pivot = cultural anti-pattern (как GE Predix, см. lec-11).
- **Argo AI (Oct 2022).** $7B сгорело за 5 лет. Ford + VW pull funding одновременно. Lesson: «solve L4 robotaxi everywhere» — too big для startup-scale capital; OEM как investors fickle.
- **Uber Tempe 2018.** Elaine Herzberg, first AV-pedestrian fatality. Lesson: ODD critical (training data bias на pedestrians вне crosswalk); disabling factory safety systems — anti-pattern; safety driver attention не reliable.
- **Tesla Autopilot 54 verified fatalities NHTSA.** Lesson: naming matters («Autopilot», «Full Self-Driving» invite over-reliance); driver-monitoring обязателен; edge cases в perception (sun glare, parked emergency vehicles) — distribution shift.

### Фундаментальное ограничение / риск подхода

- **AV survivor consolidation 10:1.** Из 30+ серьёзных AV/AV-trucking стартапов 2015-2020 выжили 3-4 (Waymo, Aurora, Mobileye, Apollo Go). $20B+ сожжено. **AV-индустрия исторически = capital-intensive, slow, brutal Darwinian**.
- **Just-in-time + ML demand forecast = fragile.** COVID 2020, Houthi 2024 — distribution shift extreme, ML полностью out-of-distribution. Resilience требует redundancy.
- **Pure end-to-end DNN без HD-map для L4 = research-stage**, не production-safe (Wayve approach). Waymo HD-map + LiDAR + remote ops + formal safety case = доказанный pattern.
- **Sidewalk robots stuck в dense urban.** Snow, vandalism, package handoff, sidewalk regulation — narrow use cases, не universal.

### Критерий «здесь ИИ не нужен / не применим»

- **Задача well-defined optimization (TSP, VRP, scheduling)** → **OR (Gurobi, CPLEX, OR-Tools) лучше RL**. UPS ORION — canonical proof: $300-400M savings/год через OR + heuristics, не deep learning.
- **Demand pattern stationary + few external signals** → **EOQ + safety stock classical formulas лучше ML overkill**.
- **Black-swan event (geopolitical, pandemic, port-strike)** → **human dispatcher + scenario planning**; ML по определению out-of-distribution.
- **Physical infrastructure problem (Suez channel width, port crane capacity)** → **engineering, не AI** (Ever Given 2021 — AI не помогала).
- **Labor shortage at scale (78K trucker deficit)** → **policy + training + visa**, не AV-deployments (math не работает).
- **Safety-critical с regulatory audit (aviation control, pharma cold-chain)** → **rule-based + human-in-loop required**.
- **Drone delivery в dense urban US** → **acoustic + FAA = blocked**; medical Africa (Zipline) — единственный proven mass-deployment.

### Более правильный альтернативный инструмент (сравнение)

| Контекст | AI hype | Правильный инструмент |
|---|---|---|
| Routing well-defined (TSP, VRP) | RL marketing pitch | **OR** — Gurobi, CPLEX, Google OR-Tools (UPS ORION) |
| Stationary demand inventory | ML «smart inventory» | **EOQ + safety stock + ABC analysis** |
| Black-swan event | «AI agent dispatcher» | **Human dispatcher + scenario planning** |
| Suez Ever Given physical extraction | — | **Engineering: dredging + tug boats** |
| Trucker labor shortage | AV deployment | **Policy + training + visa + working conditions** |
| Safety-critical air traffic | «Autonomous ATC» | **Rule-based + human controller (ICAO requirement)** |
| L4 city robotaxi | Pure end-to-end DNN (Wayve) | **HD-map + LiDAR + remote ops + formal safety case (Waymo)** |
| Drone urban US delivery | «Drones for everyone» | **Wait for regulation + acoustic resolution** |

### Бюджет (слова / слайды / минуты) на этот блок ≥30%

**Chapter (target ≥30k слов для L4+):**
- §1 failure-content: ~1 500 слов (humanoid hype, capital intensity, lights-out myth) = **~5%**
- §2 failure-deep-dive: ~5 500 слов (Argo + Embark + TuSimple + Waymo Via + Starsky + survivor analysis) = **~18%**
- §3 failure-deep-dive: ~4 500 слов (Cruise centerpiece + Uber Tempe + Tesla Autopilot + Tesla Austin) = **~15%**
- §4 entire section на failure + decision framework + alternatives = ~6 500 слов = **~22%**
- **Total failure/judgement strict-in: ~18 000 / 30 000 = 60%** — comfortably > 30%.

**Slides (target ~40 слайдов):**
- §1 failure slides: 1-2 (humanoid hype) = **~4%**
- §2 failure slides: 5-6 (AV-bankruptcy timeline + Argo / Embark / TuSimple deep-dive + cumulative $20B chart) = **~14%**
- §3 failure slides: 5-6 (Cruise timeline + Uber Tempe + Tesla NHTSA fatalities + Tesla Austin comparison) = **~14%**
- §4 entire section failure: 5-6 slides (Houthi timeline + Suez Ever Given + decision-framework + alternatives table) = **~14%**
- **Total failure/judgement slides: 16-20 / 40 = 40-50%** — comfortably > 30%.

**Speech (target ~5k слов, 75 минут):**
- §1 failure: ~3 минуты = **4%**
- §2 failure: ~10 минут = **13%**
- §3 failure: ~10 минут = **13%**
- §4 entire failure + decision: ~13 минут = **17%**
- **Total failure/judgement minutes: ~36 / 75 = 48%** — comfortably > 30%.

**Counter-check (mandatory):** холистически (chapter+slides+speech) ≥30%, distributed evenly через §2, §3, §4 (не concentrated в одном артефакте). **PASS.**

## Assessment

### Семинарские вопросы (3 для семинара 13)

1. **(LO1 + LO2 — applied case judgment).** Учебный кейс: «Российская 3PL-компания планирует развернуть AV-trucking pilot для маршрута Москва-Казань. Топ-менеджер слышал про Aurora Dallas-Houston и хочет повторить. CFO спрашивает: что нужно проверить перед инвестированием $50M? Сформулировать чек-лист из ≥7 критериев со ссылками на конкретные failure cases (Argo / Embark / TuSimple / Waymo Via)».

2. **(LO2 + LO7 — failure-cause analysis).** Учебный кейс: «В декабре 2024 GM закрыла Cruise после 8 лет и $10B инвестиций. Проанализировать root causes: какие из них были (a) технические, (b) business model, (c) regulatory / trust, (d) cultural / organizational? Дать ranking 1-4 по importance + защитить с источниками. Что бы вы сделали по-другому, если бы стали CEO Cruise в 2020?»

3. **(LO7 — alternatives analysis).** Учебный кейс: «Логистическая компания планирует ML-based route optimization для своего fleet 500 trucks. Vendor показывает demo с +25% efficiency claim. Применить decision framework из §4 — какие 5 вопросов задать vendor'у перед закупкой? Когда OR (Google OR-Tools / Gurobi) был бы лучше? Когда EOQ + safety stock + ABC формулы достаточны? Сформулировать письменное recommendation для CTO».

## Анонимизация (ENFORCED — Лекция 9 lesson 2026-05-21)

<!-- Career angle / academic contour ОБЯЗАНЫ быть в родовой форме без named institutions. -->

- **Frontmatter `audience` строго universal:** «студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)» — НЕ «ИУ6 МГТУ Бауман / ВКА Можайского / МАИ».
- **Career section §5.2:** «универсальные технические университеты + профильные кафедры в области инфокоммуникаций / транспортных систем + военно-космические академии (готовят инженеров с пересекающимися навыками)» — **без названий** МГТУ / Бауман / ИУ-N / Кафедра / ВКА им. Можайского / МАИ / СПбГУ / bauman.ru / vka.mil.
- **Эталон:** lec-03 / lec-05 / lec-07 / lec-09 chapters — 0 named institutions. lec-06 — единственная generic «профильные кафедры» (родовое).
- **Cost-of-omission lec-09 reference:** 1 revision cycle (v2→v3) anonymization. Здесь — превентивно через lecture-outline.

## Russification visible body (ENFORCED — memory rule `feedback_russification`)

- **Anti-anglicism mandate.** В каждом producer-prompt (book-editor, presentation-designer, speech-writer) — explicit anti-anglicism + Russification таблица + pre-GATE deep latin-token scan check.
- **Top replacements specific к logistics + transport:**
  - **last mile** → последняя миля (mainstream RU term, OK to keep).
  - **ground truth** → эталонная разметка.
  - **automation bias** → склонность доверять автомату.
  - **multi-sensor fusion** → слияние нескольких сенсоров.
  - **decision support** → поддержка принятия решений.
  - **predictive maintenance (PdM)** → прогностическое обслуживание (PdM при первом упоминании).
  - **ADAS** → водитель-ассистент (ADAS при первом упоминании с расшифровкой Advanced Driver Assistance System).
  - **AMR (Autonomous Mobile Robot)** → автономный мобильный робот (АМR при первом упоминании).
  - **dynamic pricing** → динамическое ценообразование.
  - **network design** → проектирование сети маршрутов.
  - **fleet management** → управление автопарком.
  - **dispatch / dispatcher** → диспетчеризация / диспетчер.
  - **routing** → построение маршрутов / маршрутизация.
  - **black box** → чёрный ящик (mainstream RU term).
  - **edge case** → краевой случай.
  - **operational design domain (ODD)** → область штатной эксплуатации (ODD при первом упоминании).
  - **just-in-time** → точно-в-срок (JIT при первом упоминании).
  - **right of way** → преимущество проезда.
  - **lane keeping** → удержание в полосе.
  - **emergency braking** → экстренное торможение.
  - **eyes-off** → «без необходимости следить за дорогой» / «глаза могут быть оторваны от дороги».
- **Whitelisted (brand names + acronyms with RU расшифровкой):** Waymo, Aurora, Mobileye, Tesla, Apollo Go, Pony.ai, WeRide, Cruise, Symbotic, Amazon Sparrow/Sequoia/Proteus/Vulcan, Locus, Zipline, Starship, Coco, Nuro, КамАЗ, Cognitive Pilot, Yandex SDG, Avride, AB ABB, ZPMC, ATA, NHTSA, FAA, ICAO, IMO, SAE, AGM, NTSB, OR (с расшифровкой Operations Research), EOQ (с расшифровкой Economic Order Quantity), VRP (с расшифровкой Vehicle Routing Problem), TSP (с расшифровкой Travelling Salesman Problem).
- **Pre-GATE check (ENFORCED):** deep latin-token scan (не только pattern grep) — `unique - whitelist = ∅` для narrative body. См. `tools/presentation-build/README.md` §5.8.
- **Cost-of-omission lec-08:** «обилие англицизмов! провал» owner reject → 3 revision passes / ~3h. Здесь — превентивно через lecture-outline.

## Hero illustrations (ENFORCED for all deck — memory rule `feedback_hero_images`)

<!-- Каждая презентация курса ОБЯЗАНА иметь hero-иллюстрацию на первом + последнем слайде. Cost-of-omission lec-08: 6 min исправление, но owner заметил сразу. -->

- **s01 (ice-breaker / cover): Waymo Jaguar I-Pace на улице SF / LA** — real photograph, ≥40% area, acquisition Tier 3 (Waymo press kit) → Tier 2 (Wikipedia Commons) fallback. Attribution «Waymo press kit, 2025». Foreshadow keystone (городская среда = chaotic уровень, и Waymo это **выживший**).
- **s39 (closing / bridge): Telecom NOC (Network Operations Center) с AI overlay** — real photograph, ≥40% area, acquisition Tier 3 (Ericsson / Nokia / Huawei press) → Tier 2 (Wikipedia) → Tier 6 (Google stock) fallback. Attribution «Telecom NOC / Vendor press, 2025». Bridge к lec-14 (телеком, сетевая инфраструктура, кибербез).
- **Backup:** s01 backup — Aurora Class-8 truck (Aurora press May 2025); s39 backup — human dispatcher control room (FedEx / UPS / Maersk press).
- **НЕ подходит:** stock illustration с laptop+brain icon, generic «AI» visual, plain Ocean palette card, thank you slide на s39.

## 6-tier image acquisition (ENFORCED — memory rule `feedback_no_mock_fallbacks`)

<!-- Для всех media-rich слайдов (минимум 15-20 на типичный deck). Mock-fallback допустим ТОЛЬКО при documented 6/6 tier failure. -->

- **Per case-study slide acquisition plan** — см. research file 06 § «Case-study slides — 6-tier acquisition plan» (14 slides outlined с tier priority + URL kandidate).
- **Self-report «X% media coverage» НЕ trustworthy** без per-image source URL.
- **Educational fair use mandate** — для учебных лекций ANY copyrighted image OK с attribution.
- **Storage:** `library/lectures/lec-13/assets/screenshots/sNN-real-source.png` + `.url` файл per image.
- **Cost-of-omission lec-08:** 16 mocks прошли «87.2% coverage» check → owner reject «это моканное говно. все переделать» → ~1.5h cycle wasted. Здесь — превентивно через 6-tier plan в research file 06.

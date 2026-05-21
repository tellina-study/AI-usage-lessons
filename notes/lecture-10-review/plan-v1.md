# Лекция 10: AI в сельском хозяйстве — v1 plan

## Метаданные

- **Lecture:** 10 | **Module:** 2 (отраслевое применение) | **Duration:** 75 мин + Q&A (~5 мин буфер) | **LO:** LO1, LO2, LO5
- **Audience:** студенты-инженеры 3 курса (универсальная, не агро-специалисты)
- **Issue:** #126 | **Status:** v1 (Phase 1 critique pending) | **Date:** 2026-05-21
- **Keystone axis:** **Лестница AI-проникновения в АПК — от поля к полке** + injection «closed-loop vs open-environment AI» как объяснительный механизм провалов

## Topics Covered

Precision farming (See & Spray, LaserWeeder, xarvio, FieldView) / autonomous machinery (Monarch failure, Solinftec, Aigen, AGCO PTx) / livestock CV (SenseHub, CattleEye) / vertical farming collapse / agentic AI в supply chain (Cargill, Tract, Olam Mindsprint) / advisory chatbots + Plantix + ChatGPT hallucinations / connectivity & vendor lock-in (Мелитополь remote-brick, FTC v. Deere, GNSS-jamming) / РФ-контекст (Cognitive Pilot vs пыль, ИТЭЛМА, РСХБ, госпрограмма) / sustainability paradox / EU AI Act + USDA Climate-Smart cancellation.

## Prerequisites

- **Лекция 2** «Архитектуры современных моделей» — foundation models, edge inference.
- **Лекция 3** «Архитектуры AI-систем» — RAG, agentic patterns, on-device.
- **Лекция 7** «AI в медицине» — симметричный пример **closed-loop** среды (controlled environment, validated datasets, регуляторика). АПК — **зеркальный контраст**: open environment, шумные данные, regulatory вакуум.
- **Лекция 9** «AI в аэрокосмической и оборонной отрасли» — OODA-ось, satellite analytics, dual-use; в L10 berlapping элемент Sense (satellite for agriculture) трактуется кратко, без deep dive.

## Normative References

- **Международное.** EU AI Act (Regulation 2024/1689; высокий риск для autonomous agricultural machinery, AI literacy обязательства c февраля 2025). FAO AI roadmap for agrifood (April 2025 + October 2025 ATIO). UN ICRC position на autonomous agricultural robots (отсутствует — это **gap**).
- **США.** USDA AI Strategy FY 2025-2026; FTC v. Deere (2025-01); Climate-Smart Commodities cancellation (April 2025) → AMP rebrand; FCC ban DJI ag-drones (December 2025).
- **РФ.** Программа «АПК будущего» 2026–2030 (распоряжение Правительства от 31 декабря 2025); индекс цифровизации АПК 27,2 / 100 (Яков и Партнёры) против 75,5 у США.
- **Стандарты.** ISO 17532:2007 + ISO 19115 для farm data. Не «жёсткие» как DO-178C в Лекции 9 — это часть исторического vacuum в АПК.

## Learning Objectives

1. **LO1.** Назвать пять уровней лестницы AI-проникновения в АПК (поле / робот / животное / supply chain / потребитель) и для каждого — 2–4 named tools 2026 года + направление adoption (растёт / стагнирует / переоценено).
2. **LO2.** Критически оценить заявление вендора AgTech-решения (типа «autonomous tractor» или «AI-powered crop advisor») — отличить demo-condition от production-deployment; применить ≥3 теста к learning case.
3. **LO5.** Сформулировать ≥5 явных критериев «здесь AI не нужен / не применим» для агро-контекста; назвать конкретную не-AI или другой-AI альтернативу для каждого; объяснить, почему generic-LLM как farm advisor — антипаттерн категории.

---

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

### Ось: **Лестница AI-проникновения — от поля к полке**

Пять уровней. Снизу вверх — растёт **степень контроля среды**, падает **биологическая непредсказуемость**, растёт **measurable ROI**:

| Уровень | Среда | AI-проникновение 2026 | Канонический success | Канонический failure |
|---|---|---|---|---|
| **L1 — Поле** (open environment, биологическая) | dust, освещение, погода, патогены | низкое-среднее; «AI-augmented spray decisions» работает (See & Spray), generic robotics — нет | See & Spray 5M акров | Vertical farming collapse $1.37B+ |
| **L2 — Робот / машина** (semi-controlled, ограничено физикой машины) | вибрации, GNSS-jamming, отказ датчиков | низкое; autonomous tractor — pilot mode, не commercial scale | Carbon Robotics LaserWeeder (250k акров) | Monarch MK-V (иски 2025, layoffs) |
| **L3 — Животное** (semi-closed, индивидуальная вариативность) | заболевания, поведение, стресс | среднее; CV для здоровья работает, кормления — overfit | Allflex SenseHub 2M коров | Cainthus partnership — нет публичных метрик |
| **L4 — Supply chain** (controlled cargo, logistic flows) | currency, weather, regulatory | высокое; **agentic AI лидирует** | Cargill CMAX + 2026 BIG AI Award | USDA Climate-Smart cancellation tail risk |
| **L5 — Потребитель / retail** (fully controlled, цифровые данные) | demand patterns, inventory | очень высокое; полностью production | Walmart × Cropin (–20% waste); X5 «Перекрёсток» ML с 2020 | — (этот уровень reliably работает) |

**Главная закономерность:** **AI penetration ↑ как удаление от биологической непредсказуемости ↑**. Это **не идеология**, это **observation 2026** — и **главное объяснение, почему AgTech-инвестиции рекомендуют сейчас supply-chain agentic-плеи, а не on-farm robotics pilots**.

### Injection «closed-loop vs open-environment AI» как объяснительный механизм

Дополнительный механизм для объяснения провалов на L1-L2:
- **Closed-loop** (медтех L7, фабрика L11) — controlled environment, validated datasets, AI работает.
- **Open-environment** (AgTech L10) — dust, освещение, патогены вирусов внутри замкнутого контура, GNSS-jamming извне. AI **ломается на тех же задачах**, которые в industrial setting казались решёнными.
- Vertical farming казалась попыткой **переехать из open в closed** (контролируемое освещение, контролируемое питание, AI-оптимизация) — но **закон термодинамики** (LED ≈ 100× free sunlight) этого не позволил.

### Keystone slide в Разделе 0 (ДО первого погружения)

**Заголовок:** «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**».

Визуально: вертикальная лестница из 5 ступеней (L1 внизу — «Поле», L5 наверху — «Полка»). На каждой ступени — 1 строка «где AI работает» / «где ломается». Справа — стрелка «↑ controllability ↑ ROI» / «↓ биологическая непредсказуемость ↓».

**Это keystone-slide про саму ось** — не про устройство курса, не про защиту подхода, не про recap. Каждый следующий раздел = мотивированный подъём по одной ступени лестницы.

### Каждый раздел = мотивированный подъём по оси (не «всплывает»)

- Р1 → L1 «Поле».
- Р2 → L2 «Робот».
- Р3 → L3 «Животное».
- Р4 → L4 «Supply chain».
- Р5 → L5 «Потребитель» + meta-уровень «среда» (connectivity, vendor lock-in, regulatory, российский слой).

---

## Инструменты на каждом уровне таксономии (ENFORCED L4+ — Лекция 4 lesson)

> Принцип: каждый уровень — 2-4 dominating 2026 tools (вендор-режим), adoption-направление словами, anti-hype-оговорка, volatile-метрики → `[VFY-day-of]`. Bra режима ≠ название бренда (например, «See & Spray» = «AI-augmented selective spray», не «autonomous robot»).

### L1 — Поле (precision farming / agronomy decision support)

- **Tools 2026.** John Deere See & Spray Ultimate (Blue River acquisition); Bayer Climate FieldView; BASF xarvio FIELD MANAGER (130k фермеров, 20M га); Syngenta Cropwise (70M га, 30 стран); Taranis (leaf-level CV). **РФ:** ExactFarming (12 700 хозяйств, 9.8M га), АгроСигнал, ГК «Прогресс Агро» (+5% ROI на пшенице).
- **Adoption.** Растёт быстро в US Corn Belt + EU + AU. **Стагнирует** у smallholders (digital divide расширяется по данным Syngenta-IPSOS 2025). РФ — медленнее, индекс 27,2 vs США 75,5.
- **Anti-hype.** **Бренд ≠ режим работы.** «AI advisory» часто = rule-based agronomic recommendations + visualization, не deep learning. «Climate FieldView 250M акров» = подписки, не «AI оптимизирует каждый акр». Точность рекомендаций деградирует за пределами US Midwest (validation bias). Vendor lock-in — рекомендации tied to Bayer/Pioneer hybrids.
- **Инфраструктура** (отдельно от capability): satellite imagery (Planet Labs Dove 3m, ICEYE SAR), GNSS RTK ground stations, mobile connectivity на полях (см. провал F15 — 18% US farms без интернета вообще).
- **Volatile** (`[VFY-day-of]`): See & Spray acreage прирост; xarvio Japan rice yield guarantee 2025 результаты; ExactFarming actual user count.

### L2 — Робот / машина (autonomous machinery + harvest robotics)

- **Tools 2026.** Carbon Robotics LaserWeeder G2 ($1.4M / машина, 150+ deployed, 14 стран); Solinftec Solix (243% YoY US expansion); Aigen Element gen2 ($50k, solar + mechanical); AGCO PTx Trimble Outrun (retrofit-mode autonomy для mixed-fleet); Naïo Technologies Orio (в judicial recovery 2025); Bonsai Robotics AR 500 (orchard autonomy); Tevel Aerobotics (flying apple pickers); Saga Robotics Thorvald (UV-C ночные 150+ units, 20% UK strawberry market). **РФ:** Cognitive Agro Pilot (1200+ установок CV); ИТЭЛМА (спутниковый, конец 2025 на «Кировцах»); Геоскан 201 Агрогеодезия (БПЛА).
- **Adoption.** Растёт в **специализированных нишах** (strawberry UV-C, almond/citrus orchards, vegetable beds); **стагнирует** в broadacre (Monarch банкрот, FarmWise wind-down 2025, Naïo recovery). **РФ:** ИТЭЛМА — структурный сдвиг ландшафта 2026 (спутниковый стек vs CV-only).
- **Anti-hype.** **«Demo ≠ production»** — Monarch MK-V продал «autonomous» tractors, которые «unable to operate autonomously» (иск Burks Tractor ноябрь 2025). «Specialization побеждает generic» — universal farm robot не существует в 2026. Strawberry-harvesting robot $200-350k capex, addressable manual labor $50B, robots <5%.
- **Инфраструктура.** GNSS-jamming спойлит точное земледелие в Финляндии (>122k авиа-рейсов с interference Q1 2025); FCC ban DJI ag-drones (декабрь 2025) ломает 80% US ag-spray drone fleet.
- **Volatile**: LaserWeeder pricing, Solinftec deployments per state, Monarch fate (laid-off → liquidation pending), Cognitive Pilot total installations.

### L3 — Животное (livestock CV + biometrics)

- **Tools 2026.** Allflex SenseHub (MSD Animal Health, 2M коров mounted milestone 2025); CattleEye (GEA-acquired 2024; 60 ферм, 11 000 коров для lameness detection); DeLaval VMS V310 (robotic milking, 99.8% attachment rate, +15% North American installations); Connecterra IDA (Danone, Bayer, Kersia клиенты); Cainthus (Cargill partnership); Cargill Birdoo (CV для broiler weight, >95% accuracy). **РФ:** GEA Russia + Lely + DeLaval (impacted санкциями, частичное импортозамещение 2026); Connectome.ai (Сколково CV для контроля рождения телят).
- **Adoption.** Растёт стабильно (CV дёшев, dairy/poultry economic value высок); консолидация (GEA acquired CattleEye, MSD acquired Antelliq за $3.85B). РФ: ограничено санкциями + AI-функционал зарубежных систем требует firmware updates из Европы — уязвимая точка.
- **Anti-hype.** Algorithm tuned для Holstein / dairy breeds — для местных пород калибровка слабая. Subscription costs ($30/cow/year) для small dairies (<50 cows) — overkill. CV требует чистых barns + good lighting — tie-stall barns не подходят.
- **Инфраструктура.** Camera install (overhead для barn / parlour exit), cloud для analytics, mobile alerting для vets.
- **Volatile**: SenseHub deployed count, GEA Russia deliveries (sanctions impact), DeLaval VMS attachment-rate updates.

### L4 — Supply chain (agentic AI procurement + commodity trading + logistics)

- **Tools 2026.** Cargill CMAX + CarVe (2026 BIG AI Excellence Award); Tract (€18.6M Series A, 4 anchor customers Cargill+ADM+Olam+LDC); Olam Mindsprint (Procuresprint agentic procurement, Wipro 2026 large transformation); Bunge + Bangkok Produce blockchain (deforestation-free soy для Charoen Pokphand); ClimateAi (climate-adaptive crop planning agents); Revenue.ai (commodity trading agents, –25..35% hedge slippage); Cropin Cloud + Sage GenAI (>30M acres digitized; PepsiCo India, Walmart partnerships); Walmart × Cropin (–20% food waste); Tesco AI demand forecast (–30% food waste vs 2017). **РФ:** X5 «Перекрёсток» ML с 2020 (200 факторов прогноза спроса); Магнит F&R (in-house, Napoleon IT, 46 РЦ к январю 2026); РСХБ «Своё Фермерство» (10 000 партнёров, 1.25M товаров).
- **Adoption.** **Лидирует в production-deployment.** McKinsey: «traders measure outcome в basis-points, fast feedback loop». РФ-крупные ритейлеры (X5, Магнит) — мировой уровень in-house ML.
- **Anti-hype.** Agentic = пока **narrow** (hedge decision, procurement compliance), не end-to-end supply chain orchestrator. Tract — это **data backbone**, не agentic per se. Blockchain ≠ AI; integration AI-side всё ещё в pilot phase в Bunge. РФ: AI-сервисы РСХБ declared, **production-метрики не опубликованы**.
- **Инфраструктура.** Cloud-first (но РФ — частично on-premise после санкций 2022); FedRAMP / SOC2 + GDPR (компании, торгующие в EU); SAP / Oracle / 1С integration.
- **Volatile**: Tract customer count, Cargill ML deployments, X5 категории coverage, Магнит F&R SKU breadth.

### L5 — Потребитель / retail (demand forecast + waste reduction + traceability)

- **Tools 2026.** Walmart Eden ML (in-house, 2017+); Tesco AI demand forecast (–30% waste, 2017+); X5 «Перекрёсток» ML; Магнит F&R; AgriDigital (blockchain grain Australia, payments из 90 дней в 2 для Zambia/Zimbabwe smallholders). **РФ:** РСХБ «Своё Фермерство»; ЭФКО Hi! растительное мясо (AI в R&D, production метрики не открыты).
- **Adoption.** Очень высокое; reliably production. Это самый зрелый слой АПК-AI.
- **Anti-hype.** Большая часть этого слоя — **не agriculture-specific**, а general retail-supply. Это объясняет, почему успехи здесь не «доказывают» AI-готовность во всей АПК-цепи.
- **Инфраструктура.** ERP + WMS + POS + e-commerce — все standard retail-stack, на которые AI ставится сверху.
- **Volatile**: точные метрики reduction waste / yield prediction accuracy не верифицируются independent.

### Инфраструктура (cross-cutting, отделена от capability)

Connectivity (Starlink в РФ запрет апрель 2026; 18% US farms без интернета; GNSS-jamming); edge compute (TinyML на STM32 / ESP32; NVIDIA Jetson Orin Nano; Apple-style on-device); microelectronics санкционные ограничения (TSMC прекратил Эльбрус/Байкал 2022; AI-стек РФ зависит от серого импорта NVIDIA); regulatory (EU AI Act high-risk for autonomous machinery; USDA AI Strategy формальна; РФ «АПК будущего» 2026-2030 декларативна).

**Не AI capability** — плитка под капабилитис, **один слайд** (s35 «Среда: связь, электроника, регуляторика»).

---

## Outline

### Раздел 0 — Keystone + roadmap (5 мин)

**Цель.** Предъявить лестницу как карту лекции; зацепить hook'ом, который сразу показывает контраст «где AI работает / где провалился».

**Hook кандидаты.**
- **A.** **BEFORE/AFTER See & Spray на хлопке** — selective spray в дюзах + counter «–50% гербицидов, 5M акров». Evergreen, success-first, политически нейтрален. **Моя рекомендация.**
- **B.** **Plenty Compton facility** open vs closed (май 2023 → декабрь 2024) — failure-first hook. Драматичен, прямо служит AI-Failure rule, но mood депрессивный.
- **C.** **Cognitive Agro Pilot vs пыль** — РФ-кейс, иск фермера, видео с камерой не видящей кромку поля. Технически сильный, но узко-РФ.
- **D.** **Cargill 2026 BIG AI Award** — успех agentic в supply chain. Бизнес-сухо, для инженеров мало интересно.

**Рекомендация:** A primary; C fallback как «свой» бытовой контраст после A. B на keystone как «контр-пример» (одной строкой).

**Keystone slide.** Вертикальная лестница 5 уровней. Заголовок: **«Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом»**.

**Roadmap slide.** 5 содержательных разделов + 1 граничный + Q&A; LO сверху, тайминг внизу.

**Media-rich слайды:** (1) hook BEFORE/AFTER See & Spray (Deere press URL → og:image); (2) keystone лестница visualization (drawio); (3) roadmap — lecture-map.

### Раздел 1 — L1 «Поле»: precision agronomy + advisory (14 мин)

**Цель.** Показать самый нижний уровень — open environment, биологическая непредсказуемость; где AI работает (selective spray) и где ломается (vertical farming, generic LLM advisor).

**Working cases (4).**
- **John Deere See & Spray Ultimate** — 5M акров 2025; 36 камер, 2500 sq ft/sec; >95% Palmer amaranth detection; –50% non-residual herbicide; +2 bu/A urожайность.
- **BASF xarvio FIELD MANAGER** — 130k фермеров, 20M га, 100 стран; Japan rice yield guarantee 2025 (outcome-based, first в мире).
- **Climate FieldView (Bayer)** — 250M акров / 23 страны; >50% US corn/soy/cotton.
- **РФ-параллель: ГК «Прогресс Агро»** — дифференцированное внесение азота на 2 800 га, +5% рентабельности (внутренний замер, не peer-review, но публичная метрика).

**Strict-in failures (3, ~7 мин).**
- **F1. Vertical farming collapse** (1-минутный summary с указателями на Р2): $1.37B+ потерь в 2025 одних только; **AppHarvest ToBRFV** = «closed loop ↑ blast radius»; **Plenty** = «AI не закрыл energy gap»; **Bowery $32M оборудования никогда не запустили**. Урок: AI работает на знаменателе; если знаменатель (LED ≈ 100× free sunlight) фундаментально выше — ML бессилен. **Bridge:** «закон термодинамики важнее ML — мы вернёмся к этому в Р2».
- **F2. ChatGPT/Bard hallucinations в agronomy (Nature Food 2024)** — рекомендация неправильного окна применения гербицида → significant crop damage. «Confident wrong» опаснее «admitted don't-know». RAG-grounded в local regulator + явный отказ при low confidence + human-in-the-loop экстеншн-агент.
- **F3. Plantix 10–15% misdiagnosis** — даже 90% accuracy на 10M+ загрузок = сотни тысяч неправильных pesticide-рекомендаций. Threshold accuracy ≠ deployment readiness. Альтернатива: uncertainty-aware рекомендация с abstention.

**Russian context.** ExactFarming (12 700 хозяйств, 9.8M га); АгроСигнал (мониторинг ГСМ); ГК «Прогресс Агро» как успех. Indeks цифровизации АПК РФ 27,2 vs США 75,5 (Яков и Партнёры) — структурный gap, не выдумка пропаганды.

**Media-rich:** (4) See & Spray Ultimate в работе (Deere press); (5) xarvio Japan rice guarantee map; (6) Plantix UI screenshot + misdiagnosis breakdown QuickChart; (7) AppHarvest virus spread схема (mermaid); (8) ChatGPT hallucination screenshot из Nature Food paper.

### Раздел 2 — L2 «Робот / машина»: autonomous machinery (15 мин)

**Цель.** Показать промежуточный уровень — semi-controlled environment; где AI работает в узкой specialization (LaserWeeder, Solinftec, Saga UV-C), где ломается в generic (Monarch, FarmWise). Это самая густая failure-зона.

**Working cases (4-5).**
- **Carbon Robotics LaserWeeder G2** — 250k акров обработано, 15B weeds уничтожено, $1.4M/машина. Заменили химию физикой через CV. 240W лазер + 40M labeled images, distinguishes 100+ crop types. **G2 (Feb 2025)** — modular 6.6-60 ft boom, faster, lighter.
- **Solinftec Solix** — 243% YoY US expansion 2025; >100 robots в IL, IN, KS, IA, WI, TX; до 98% reduction в herbicide volume (vendor self-report — caveat); 24/7 solar-powered + self-refilling spray. 2025 features: Discovery Mode, Starlink integration, obstacle detection.
- **Aigen Element gen2** — $50k unit, 100% solar, 50 units в 2025 partnership с Bowles Farming. Дешёвая mechanical strike альтернатива к LaserWeeder.
- **Saga Robotics Thorvald** — 150+ units, 97% uptime, >200 000 autonomous km. 20% UK tabletop strawberry market; £8.4M raise; 13 leading UK growers; target 30% UK 2026.
- **AGCO PTx Trimble Outrun** — retrofit-mode autonomy для mixed-fleet (Fendt, Massey, Deere, CNH); альтернатива Deere closed-system; Tech Day 2025 demonstrated; goal full autonomous crop cycle by 2030.

**Strict-in failures (4, ~8 мин — densest failure section).**
- **F4. Monarch Tractor (ноябрь 2025)** — иск Burks Tractor: продали «defective» tractors 2024, unable to operate autonomously. 102 увольнения, риск shutdown. $220M raised, Foxconn lost. **Урок:** маркетинг как «autonomous» при том, что autonomy не выдержит судебной проверки = структурная trap для всей категории. Demo ≠ deployment. **Альтернатива:** supervised autonomy + явный disclosure capability / non-capability.
- **F5. FarmWise wind-down + Naïo Technologies judicial recovery** — FarmWise (CV-weed-robot, $30M+ raised) restructuring 2025; Naïo (Toulouse) judicial recovery June 2025, revenue €4M (2021) → €2.4M (2024). Структурная причина — «модели в тепличных условиях не работают в поле»: dust, освещение, тени, shadow bias. **Альтернатива:** механические weeders (Lemken, Kverneland) — менее «smart», но deterministically robust.
- **F6. Vertical farming deep-dive (часть 1 из распределённого блока)** — economics + closed-loop blast radius. Plenty bankruptcy: $940M потеряно; Compton 19 мес (открыт май 2023 → закрыт декабрь 2024); valuation $1.9B → <$15M (99%-коллапс). Лекционно ценное: AI-роботы Tortuga (acquired by Oishii март 2025) **технически работали** (50% reduction в harvest expenses), но категория проиграла unit-economics. **Bridge** к Р3: «технический успех не = коммерческий успех; теперь смотрим на L3, где economic value животноводства лучше выровнен».
- **F7. Strawberry-picking robot economics** — robot $200-350k capex; annualized $68-130k/год; США адресуемый ручной труд $50B; роботы <5%. CA picking-labor $43k на акр. «Harvesting is the last great unsolved problem». «Robots still struggle with tasks humans master in days». **Альтернатива:** H-2A guest worker programs + ergonomic improvements (стульчатые комбайны).

**Russian context (~2 мин).** Cognitive Agro Pilot 1200+ установок vs **4 иска фермеров на 12,7 млн ₽ (2025)** — пыль на полях не позволяла CV видеть кромку нескошенного. **ИТЭЛМА** (спутниковый стек) на «Кировцах» с конца 2025 — структурный сдвиг, «AI/CV не нужен, спутник проще». Геоскан 201 Агрогеодезия — пример узкого работающего решения (NDVI, multispectral).

**Media-rich:** (9) LaserWeeder G2 в поле (Carbon Robotics press); (10) Solinftec Solix robot photo (Solinftec press); (11) Monarch MK-V на лужайке + headline TechCrunch иск (real screenshot); (12) Plenty Compton ribbon-cutting May 2023 vs закрытие декабрь 2024 (split frame); (13) vertical farming bankruptcies 2022-2025 timeline (QuickChart); (14) Cognitive Pilot vs ИТЭЛМА сравнительная diagram (drawio).

### Раздел 3 — L3 «Животное»: livestock CV (10 мин)

**Цель.** Показать L3 как «AI работает стабильнее, чем на L1-L2», и почему — экономика животных concentrated и individual-level измеримая.

**Working cases (4).**
- **Allflex SenseHub** — 2M коров mounted (milestone 2025); reproductive, health, nutritional, wellbeing monitoring. SenseHub Cow Calf для beef breeding, SenseHub Feedlot. Partnership с Nestlé farms.
- **CattleEye + GEA acquisition (2024)** — low-cost CCTV + cloud AI для lameness detection при выходе из milking parlour. 60 ферм, 11 000 коров; через GEA channel — trusted by farms managing >250 000 cows worldwide.
- **DeLaval VMS V310 (robotic milking)** — 99.8% attachment rate; +15% North American installations 2025; VMS Batch Milking 20 ферм в 13 странах expected double каждый год; **Flow-Responsive Milking standard на новых V300 с июня 2025**.
- **Cargill Birdoo** — CV для broiler weight estimation; >95% accuracy без labour для clean/calibrate; saves 10-30g feed на bird; Americas-exclusive.

**Strict-in failures (2, ~3 мин).**
- **F8. Cainthus + tie-stall barns + small dairy economics** — CV требует чистых barns + good lighting; tie-stall с обилием silhouettes — challenging. SenseHub subscription $30/cow/year — overkill для small dairies (<50 cows). **Урок:** AI capability ≠ AI applicability; physical environment + economics определяют, какой % адресуемого рынка реально pays-out. **Альтернатива:** для small dairies — manual observation + cheap thermometers + 1 раз в полгода ветеринар.
- **F9. Russian dairy equipment uncertainty (DeLaval, GEA, Lely after sanctions 2022)** — AI-функционал зарубежных систем требует firmware updates + cloud services из Европы. Реальные кейсы отключения сервисов в РФ публично не задокументированы, но **architectural риск налицо**. **Альтернатива:** частичное импортозамещение (Лобня 2026, «Пакэйджинг Системс» 4 млрд ₽), но AI-стек пока без замены.

**Russian context.** GEA Russia + ограниченные поставки; Connectome.ai (Сколково CV для контроля рождения телят); Лобня производство молочного оборудования (март 2026).

**Media-rich:** (15) SenseHub на корове (Merck press); (16) CattleEye lameness detection UI (real screenshot if public); (17) DeLaval VMS V310 milking robot в работе (DeLaval press); (18) tie-stall vs free-stall barn diagram explaining CV-applicability.

### Раздел 4 — L4 «Supply chain»: agentic AI поднимается (12 мин)

**Цель.** Показать L4 как **place, где agentic AI лидирует в production-deployment в 2026**. Объяснить, почему: traders measure outcome в basis-points, fast feedback loop. Это контраст с L1-L2 где «сезон-длинный» feedback убивает ROI.

**Working cases (4-5).**
- **Cargill CMAX + CarVe (2026 BIG AI Excellence Award)** — predictive port + shipping logistics, optimizes grain flows; CV для protein supply chain yield, waste reduction; Brazil grain logistics AI-driven mixing. >150 stran, 1000+ facilities, 70 стран.
- **Tract (Cargill+ADM+Olam+LDC)** — €18.6M Series A 2025 (Dawn Capital). Bridge supplier data и procurement processes (compliance / scope-3 emissions / provenance). **4 anchor customers — конкуренты**, shared infrastructure для compliance.
- **Olam Mindsprint / Procuresprint** — Wipro 2026 «one of largest strategic transformation engagements». Farmsprint (plantation management), Procuresprint agentic procurement, Tradesprint commodity trading.
- **Walmart × Cropin + Tesco AI demand forecast** — Walmart –20% food waste, Eden ML algorithm; Tesco –30% food waste since 2017. Demonstrate retail AI поднимается на L5.
- **ClimateAI + agentic crop planning** — climate-adaptive recommendations; sold к commodity trading + large producers + financial institutions.

**Strict-in failures (2, ~4 мин).**
- **F10. USDA Climate-Smart Commodities cancellation (April 2025)** — $3.1B / 141 projects / 14 000 ферм / 3.2M acres pre-cancellation. Rebranded в AMP с pivots. **Урок:** federal policy = tail risk для AgTech business model. Companies over-rotated к public funding — exposed. **Альтернатива:** unit economics over policy-tailwind plays; investor sentiment 2025-26 уже shifted.
- **F11. Verra phantom credits — 94% rainforest offsets «worthless»** (Pachama project overestimated by 8×). AI-MRV для carbon-claims = inference с большой uncertainty, marketed как «precise measurement». Whitewashing carbon-credit + AI-veneer = scaled greenwashing. **Альтернатива:** direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact. **Note:** Indigo Ag НЕ в скандале — использует Climate Action Reserve, менее controversial; 2M tons verified, Microsoft 12-year 2.85M tons deal.

**Russian context (~2 мин).** X5 «Перекрёсток» ML с 2020 (200 факторов, plodовощная и молочная категории); Магнит F&R in-house с 2025 (46 РЦ к январь 2026); РСХБ «Своё Фермерство» (10 000 партнёров, 1.25M товаров). Заявленные AI-сервисы (РСХБ AI-прогноз урожайности, geno-селекция) — declared, production-метрики не опубликованы. Это **paritет в L4-L5 retail-supply** при отставании в L1-L2.

**Media-rich:** (19) Cargill BIG AI Award announcement (Cargill press); (20) Tract Series A coverage (real news screenshot); (21) Verra phantom credits Guardian investigation (real article screenshot); (22) USDA Climate-Smart cancellation announcement (USDA press); (23) X5 «Перекрёсток» dashboard / Магнит F&R архитектура (TAdviser source).

### Раздел 5 — L5 + среда: connectivity, vendor lock-in, regulatory, payoff (14 мин)

**Цель.** Закрыть лекцию meta-уровнем (где работают L5 retail-AI; где «среда» — connectivity, vendor lock-in, regulatory — определяет границы); собрать 5 явных «когда не AI»; career angle + reading list; callback к keystone.

**5.1. L5 «Потребитель / retail» — кратко (~3 мин).** Walmart × Cropin (–20% waste, Eden ML); Tesco AI demand forecast (–30%); X5 + Магнит — РФ-параллель мирового уровня. **Этот уровень reliably работает**: это **самый зрелый слой АПК-AI** и единственный, где «AI everywhere» — не hype.

**5.2. Среда: connectivity (~3 мин).** 18% американских ферм без интернета вообще; **>122 000 авиа-рейсов с GNSS-interference Q1 2025** (Stanford GPS Lab); финские поля «unfarmable using GNSS-based tractors» из-за российских EW-станций. **Урок:** edge-AI / TinyML / offline-first — единственная реалистичная архитектура для большинства farms. Cloud-first AI for agriculture = архитектурная ошибка.

**5.3. Среда: vendor lock-in + санкционный shock (~3 мин).** **FTC v. John Deere (январь 2025)** — десятилетние ограничения ремонта; trial 2026. **John Deere remote-brick Мелитополь май 2022** — 27 единиц техники на $5M удалённо отключены при попытке вывезти в Чечню. **Двойная оптика:** anti-theft success с одной стороны, vendor control surface с другой. Тот же mechanism применим к РФ-фермерам, у которых FieldView отключился после 2022. **Урок для всех стран периферии:** AI-зависимость = политический риск; российский опыт — natural experiment, что бывает, когда импортный AI-стек отключается. **FCC ban DJI ag-drones (декабрь 2025)** — 80% US ag-spray drone fleet под угрозой; альтернативы 2.5× дороже.

**5.4. Среда: regulatory (~2 мин).** EU AI Act high-risk для autonomous agricultural machinery — producers нуждаются в compliance teams; liability cascade (производитель + AI provider + фермер). USDA AI Strategy FY2025-26 формальна. РФ «АПК будущего» 2026-2030 декларативна, госпрограмма «Цифровое сельское хозяйство» 2019-2024 цель удвоения производительности не достигнута (АПК в 2024 −3,2%).

**5.5. 5 явных «когда не AI» (~2 мин).** Из failure-блоков формируем критерии:
1. **Закон термодинамики важнее ML** — когда фундаментальная экономика (energy / capex) в 10×+ от рыночной цены продукта, AI не закроет разрыв (vertical farming).
2. **Open environment + critical physical condition** — когда CV-система не выдерживает реальных условий применения (пыль для Cognitive Pilot; освещение для FarmWise); используй mechanical / GNSS-альтернативу.
3. **Threshold accuracy ≠ deployment readiness** — когда даже 90% accuracy на масштабе означает сотни тысяч ошибочных high-stakes решений (pesticide, lameness diagnosis); требуй uncertainty-aware + abstention.
4. **Generic LLM в advisory mode** — generic chatbot для smallholders с pesticide / fertilizer recommendations = категорический антипаттерн; используй RAG-grounded в local regulator + human-in-the-loop экстеншн-агент.
5. **Cloud-first для off-grid farm** — когда farm на 18% американских (без интернета) или в зоне GNSS-jamming; используй edge-AI / TinyML / offline-first.

**5.6. Career angle (~1 мин).** **Профильные технические университеты** предлагают программы по agro-IT / agro-engineering / digital agronomy. Магистратуры в области data science applied to agriculture. **Российские работодатели:** Cognitive Pilot, ИТЭЛМА, Геоскан, ЭФКО, Русагро Тех, РСХБ.цифра, Магнит digital, X5 Tech, ExactFarming. **Международные карьерные траектории:** John Deere, Bayer Crop Science Digital, BASF Digital Farming, Cargill AI lab, Cropin (India). **Civil path** — Sber AI for agriculture, Сколково AgTech-резиденты (Connectome.ai, СиСорт). **Без агитации.**

**5.7. Reading list (~1 мин).**
- Russell & Norvig **AIMA** 4th ed (общая AI base).
- McKinsey: «How agility and AI could rewire agriculture trading» (2025).
- Hannah Ritchie substack: «Vertical farming» (термодинамический gap).
- Foodlore.blog: «Why Vertical Farms Go Bankrupt» (14 bankruptcies 2025 catalogue).
- Яков и Партнёры: «Digitalizing Russia's Agricultural Sector» (2024) — индекс 27,2.
- FAO Agrifood Systems Technologies and Innovations Outlook (ATIO, October 2025).
- Stanford GPS Lab ITM 2025 paper «GNSS Spoofing in Russia 2023-2024».
- Cambridge EJRR: «EU AI Act applied to agrifood».

**5.8. Closing callback (~1 мин).** «Лестница пять уровней. AI поднимается от поля к полке, и работает по-разному на каждом. Инженер держит её в голове целиком — выбирая для каждой ступени правильный инструмент, и зная, где AI не работает».

**Media-rich:** (24) GNSS-jamming Финляндия карта (Stanford ITM paper figure); (25) FTC v. Deere press conference (real photo); (26) Мелитополь John Deere stolen tractors map (CSO Online graphic); (27) 5 критериев «когда не AI» — dense visual checklist (drawio); (28) career-map drawio (РФ + международные работодатели); (29) closing callback — keystone repeated as bookend.

### Раздел 6 (опциональный) — Q&A (10 мин)

Q&A слот для студенческих вопросов. Готовые backup-вопросы на типовые keys:
- Почему vertical farming не сработала — это AI fault или unit economics?
- Может ли LLM-advisor реально заменить агронома?
- Что произойдёт с РФ-АПК через 5 лет если санкции снимут?
- Будет ли autonomous tractor mass-deployed к 2030?
- Где этическая граница AI в АПК (с учётом 80% smallholders глобально)?

---

## Failure-bucket budget (strict-in ≥30%)

| Раздел | Минут | Strict-in минут | Bucket-класс |
|---|---|---|---|
| Р0 Keystone + roadmap | 5 | 0 | — |
| Р1 L1 «Поле» | 14 | 7 (F1 vertical farm summary, F2 ChatGPT hallucinations, F3 Plantix misdiagnosis) | hallucination / overpromise / collapse |
| Р2 L2 «Робот / машина» | 15 | 8 (F4 Monarch, F5 FarmWise+Naïo, F6 Plenty/Bowery deep, F7 strawberry economics) | overpromise / robotics-econ / collapse |
| Р3 L3 «Животное» | 10 | 3 (F8 Cainthus tie-stall, F9 РФ dairy uncertainty) | applicability gap / vendor-lock |
| Р4 L4 «Supply chain» | 12 | 4 (F10 USDA Climate-Smart cancellation, F11 Verra phantom credits) | regulatory / overpromise |
| Р5 L5 + среда + payoff | 14 | 8 (Connectivity ~3, vendor lock-in / Мелитополь / FCC DJI ~3, regulatory ~2) — все из failure-перспективы | connectivity / vendor-lock / regulatory |
| Q&A | 10 | — | — |
| **Total active (75 мин)** | **75 мин** | **30 мин** | — |

**Итого strict-in: 30 из 75 мин = 40%.** Margin над ≥30% comfortable. Распределено холистически по 5 разделам (не сконцентрировано в одном) — соответствует Лекция 9 lesson «доля видна в каждом артефакте отдельно».

**Counter-check.** Если на Phase 3/7 strict-in доля <30% или сконцентрирована в одном артефакте — verdict REVISE.

---

## Hero images plan для s01 + s39 (§3.7c)

### s01 hero (cover / ice-breaker)

- **Entity:** John Deere See & Spray Ultimate sprayer в работе на cotton field, видимы 36 камер и selective dyse activation.
- **Source candidate:** Deere press release deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/ (Nov 2025) → og:image (Tier 1).
- **Fallback Tier 2:** Wikipedia «John Deere» commercial-use photo.
- **Fallback Tier 3:** AgTechNavigator press 2025-11-10 hero image.
- **Foreshadow keystone:** напрямую показывает L1 «Поле» working state — visual proof, что AI на верхнем сегменте лестницы реально работает (не наобещанный hype).
- **Attribution label:** «John Deere See & Spray Ultimate, 2025. Источник: deere.com (press release).»

### s39 hero (closing / bridge к Лекции 11)

- **Entity bridge к L11 «Дискретное и процессное производство»:** робот в поле → шасси на конвейере → готовый продукт на полке. Pipeline visual.
- **Source candidate Tier 1:** Cargill BIG AI Award announcement page (cargill.com/2026/) — может содержать pipeline visual.
- **Альтернатива Tier 2:** Тип фотомонтаж «Solinftec Solix в кукурузном поле → готовый продукт на полке Магнита» — но это будет требовать licensing двух photos и compositing (риск).
- **Fallback Tier 3:** Single robot-in-field iconic image от Carbon Robotics (LaserWeeder G2 press release) — отдельно, без bridge montage, но визуально мощно.
- **Foreshadow Lec-11:** один frame «робот в АПК = роbот в фабрике; единая cyber-physical pipeline» (без vagueness, но без overclaim).
- **Attribution label:** «[Source: Carbon Robotics press release, 2025] или [Source: Cargill, 2026].»

---

## Media-coverage plan (≥50% mandate)

Из ~32 типичных слайдов планируется ~19-22 media-bearing (≥60%, comfortable margin над ≥50%).

| # | Slide | Media type | Source candidate | Acquisition Tier |
|---|---|---|---|---|
| 1 | s01 cover | hero photo | Deere See & Spray press | Tier 1 (og:image) |
| 2 | s02 keystone лестница | drawio diagram | — | own |
| 3 | s03 roadmap | drawio | — | own |
| 4 | s05 See & Spray в работе | photo | Deere press | Tier 1 |
| 5 | s06 xarvio Japan rice map | press image | BASF press 2025-10 | Tier 1 |
| 6 | s07 Plantix misdiagnosis | UI screenshot + QuickChart | Plantix.net + own chart | Tier 1+own |
| 7 | s08 AppHarvest virus spread | mermaid + photo | own + NCBI PMC9366064 | own+Tier 1 |
| 8 | s09 ChatGPT hallucination | screenshot from paper | Nature Food 2024 paper figure | Tier 1 (paper PDF) |
| 9 | s11 LaserWeeder G2 в поле | photo | Carbon Robotics press 2025-02 | Tier 1 |
| 10 | s12 Solinftec Solix | photo | Solinftec.com press | Tier 1 |
| 11 | s13 Monarch иск headline | screenshot | TechCrunch 2025-11-18 article | Tier 1 |
| 12 | s14 Plenty Compton split | photo | Plenty press May 2023 + TechCrunch closure 2024 | Tier 1 (2 sources) |
| 13 | s15 vertical farm bankruptcies timeline | QuickChart | own data viz | own |
| 14 | s16 Cognitive Pilot vs ИТЭЛМА | drawio | own | own |
| 15 | s17 SenseHub на корове | photo | Merck press 2025 | Tier 1 |
| 16 | s18 CattleEye lameness UI | screenshot if public | CattleEye.com / Fortune June 2025 | Tier 1-3 |
| 17 | s19 DeLaval VMS V310 | photo | DeLaval press April 2025 | Tier 1 |
| 18 | s21 tie-stall vs free-stall | diagram | own drawio | own |
| 19 | s23 Cargill BIG AI Award | screenshot | Cargill.com 2026 press | Tier 1 |
| 20 | s24 Tract Series A | news screenshot | Foodingredientsfirst 2025 | Tier 1 |
| 21 | s25 Verra Guardian investigation | screenshot | The Guardian Jan 2023 article | Tier 1 |
| 22 | s26 USDA Climate-Smart cancellation | press screenshot | USDA.gov 2025-04-14 | Tier 1 |
| 23 | s28 GNSS jamming Finland map | figure | Stanford ITM 2025 paper Figure | Tier 1 (paper) |
| 24 | s29 Мелитополь stolen tractors | map / graphic | CSO Online 572811 or The Register 2022-05 | Tier 1 |
| 25 | s30 FTC v Deere press conference | photo | FTC press 2025-01 | Tier 1 |
| 26 | s32 5 critеria «когда не AI» | drawio checklist | own | own |
| 27 | s33 career map | drawio | own | own |
| 28 | s39 closing | hero | Carbon Robotics LaserWeeder G2 или Cargill 2026 | Tier 1 |

**Total real-image-bearing slides:** ~21 из ~32 = **65%**.
**Own-diagrams:** ~7 (drawio + QuickChart + mermaid).
**Real-image-via-6-tier:** ~21 (всё Tier 1 / Tier 2 fallback documented если Tier 1 fails).
**Stylized Ocean-palette card с verbatim headline = mock, FAIL** — категорически избегаем.

---

## Анти-AI критерии (≥30% mandate component)

Минимум 5 явно сформулированных «здесь AI / LLM не нужен / не применим» с примером и альтернативой:

| # | Критерий | Пример | Альтернатива |
|---|---|---|---|
| AP1 | **Закон термодинамики важнее ML** — когда фундаментальная экономика (energy/capex) ≥ 10× рыночной цены продукта | Vertical farming для commodity leafy greens — LED ≈ 100× free sunlight (Hannah Ritchie / MDPI Sustainability) | Открытый грунт или greenhouse при энергии < $0.10/кВт·ч; vertical только для high-value crops |
| AP2 | **Open environment + critical physical condition** — когда CV-система не выдерживает реальных условий применения | Cognitive Pilot vs пыль (4 иска 12,7М ₽ 2025); FarmWise dust + lighting failure (wind-down 2025) | GNSS / RTK-based навигация (ИТЭЛМА), mechanical weeders (Lemken, Kverneland) |
| AP3 | **Threshold accuracy ≠ deployment readiness** — когда даже 90% accuracy на масштабе означает сотни тысяч ошибочных high-stakes решений | Plantix 10–15% misdiagnosis на 10M+ загрузок = сотни тысяч неправильных pesticide-рекомендаций в год | Uncertainty-aware рекомендация с abstention; «не уверен → спроси эксперта» |
| AP4 | **Generic LLM в advisory mode** — generic chatbot для фермеров с pesticide/fertilizer recommendations = категорический антипаттерн | ChatGPT/Bard рекомендация неправильного окна гербицида (Nature Food 2024) — significant crop damage | RAG-grounded в local regulator (USDA-EPA, EU-EFSA, Россельхознадзор) + human-in-the-loop экстеншн-агент |
| AP5 | **Cloud-first для off-grid farm** — когда farm на 18% американских (без интернета) или в зоне GNSS-jamming | 60% US фермеров на cellular/satellite; Финляндия unfarmable из-за российских EW; РФ Starlink запрет 30 апреля 2026 на 6 мес | Edge-AI / TinyML / offline-first; hybrid (cellular + LoRa + Starlink + RTK ground link) для redundancy |
| AP6 (бонус) | **«AI-driven equipment» = vendor lock-in trap** — чем больше AI и telematics в трактор, тем сильнее vendor control surface | FTC v. Deere 2025-01; Мелитополь remote-brick 2022; Bayer FieldView выход из РФ; FCC ban DJI ag-drones | Open-source farming hardware (Farm Hack); right-to-repair compliance; multi-vendor стратегия; mechanical fallbacks |
| AP7 (бонус) | **AI-MRV для carbon claims без direct measurement** — inference с большой uncertainty, marketed как «precise measurement» | Verra 94% phantom credits; Pachama overestimate 8×; Bowery $32M never-used equipment | Direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact |

Используются в Р5.5 (5 критериев слайд) — каждый строгий, с named каноническим примером.

---

## РФ-контекст блок (для anonymized аудитории)

РФ-слой **встроен в каждый уровень лестницы** как параллельный track (не отдельный раздел в конце — это сильнее для understanding):

- **L1 (Р1):** ExactFarming 12 700 хозяйств + 9.8M га; АгроСигнал; ГК «Прогресс Агро» +5% ROI. Индекс цифровизации 27,2 vs США 75,5 (Яков и Партнёры).
- **L2 (Р2):** Cognitive Agro Pilot 1200+ установок vs 4 иска фермеров на 12,7М ₽ за CV-сбои в пыли. ИТЭЛМА (спутниковый стек) на «Кировцах» с конца 2025 — структурный сдвиг. Геоскан 201 (БПЛА + NDVI).
- **L3 (Р3):** GEA / DeLaval / Lely impact санкциями; частичное импортозамещение (Лобня 2026, 4 млрд ₽); Connectome.ai (Сколково).
- **L4 (Р4):** X5 «Перекрёсток» ML с 2020 (200 факторов); Магнит F&R in-house с 2025; РСХБ «Своё Фермерство» (10 000 партнёров). Sber GigaChat «сдал» экзамен в КубГАУ — declared, production-внедрений нет.
- **L5 + среда (Р5):** Cognitive Pilot remote impact санкций; John Deere remote-brick Мелитополь 2022; Starlink запрет апрель 2026; госпрограмма «Цифровое сельское хозяйство» 2019-2024 цель удвоения производительности **не достигнута** (АПК в 2024 −3,2%); «АПК будущего» 2026-2030.

**Главный РФ-урок:** **AI-зависимость = политический риск; российский опыт после 2022 — natural experiment, что бывает, когда импортный AI-стек отключается**. Альтернатива «отечественная замена» работает медленно (Cognitive Pilot, ИТЭЛМА, ExactFarming) и в ограниченных сегментах. **Урок для всех стран периферии**, не только РФ.

---

## Anonymization carry-forward

- **Frontmatter `audience` chapter / slides / speech:** «студенты-инженеры 3 курса (универсальная, не агро-специалисты)» — НЕ «ИУ6 МГТУ Бауман» / «aerospace-специалисты» / «агрохимики».
- **Career section:** «профильные технические университеты + аграрные университеты» в родовой форме; без названий ВУЗов (МГТУ / Бауман / МСХА / Тимирязевка / Кубанский ГАУ / ИУ-N / Кафедра «...»).
- **Эталон pattern:** lec-03 / lec-05 / lec-07 chapters — 0 named institutions; lec-06 — единственная generic «профильные кафедры» (родовая).
- **Cost-of-omission lec-09:** 1 revision cycle (v2→v3) anonymization. Lec-10 — apply by default.

---

## Anti-anglicism carry-forward note

Plan **сам** пишется по-русски. Англицизмы только в whitelist:
- **Brand names:** John Deere, Bayer, BASF, Carbon Robotics, Solinftec, Cargill, Walmart, Tesco и пр.
- **Tech acronyms с RU расшифровкой при первом упоминании:** CV (компьютерное зрение), NDVI (индекс растительности), RTK (kinematic GNSS-коррекция), SAR (радар синтезированной апертуры), CRISPR, ML, LLM, RAG (генерация с поиском).
- **Legal jurisdiction terms:** EU AI Act, FCC, FTC, USDA, Chapter 11 — оставляем оригинал с пометкой при первом упоминании.

**Каноничные RU-замены** (применяются в chapter / slides / speech downstream):
- predictive maintenance → прогностическое обслуживание
- ground truth → эталонная разметка
- automation bias → склонность доверять автомату
- multi-sensor fusion → слияние нескольких сенсоров
- decision-support → поддержка принятия решений
- accuracy (метрика) → точность
- big-tech → большие ИИ-компании
- edge case → краевой случай
- precision agriculture → точное земледелие
- vertical farming → вертикальное земледелие
- right-to-repair → право на ремонт
- vendor lock-in → привязка к поставщику
- supply chain → цепочка поставок
- demand forecasting → прогнозирование спроса
- agentic AI → агентный ИИ

Pre-GATE: deep latin-token scan обязателен.

---

## Cornerstone concepts (cross-artifact glossary lock)

7 ключевых терминов, которые повторяются в chapter / slides / speech одинаково (после v1 plan approval glossary lock):

1. **Точное земледелие (precision agriculture / farming)** — система рекомендаций и автоматических действий, основанная на полевых данных (спутник, дрон, датчики), с цель выполнения переменных операций по полю.
2. **Open-environment vs closed-loop AI** — open-environment = реальные полевые условия (пыль, освещение, патогены); closed-loop = controlled (теплица, vertical farm, фабрика). Главное объяснение AgTech-провалов.
3. **Edge ML / TinyML** — машинное обучение на устройстве (датчик, гейтвей, трактор-кабина) без cloud-uplink; единственная реалистичная архитектура для off-grid farms.
4. **Tacit knowledge / hyperlocal context** — неявные знания фермера о его поле (микроклимат, дренаж, weed pressure, дед-сказал-сеять), приобретаемые годами наблюдения. AI не может построить из satellite + IoT за 1 сезон.
5. **Vendor lock-in / right-to-repair** — экономико-юридическая зависимость от поставщика; чем больше AI и telematics, тем сильнее lock-in (Deere FTC case, Мелитополь, FieldView в РФ).
6. **Foundation model + grounded reasoning** — общая pretrained модель (TerraMind, Prithvi-EO 2.0) + RAG-привязка к локальным данным/нормам; альтернатива generic-LLM hallucinations.
7. **Sustainability paradox** — «AI для устойчивости» имеет собственный environmental footprint (data centers в Айове vs irrigation; GPT-3 = 700 000 литров воды). Net-positive — не автоматически.

---

## Open questions для USER GATE 0

1. **Hook финал — A vs C?** A (BEFORE/AFTER See & Spray, evergreen success-first) vs C (Cognitive Pilot vs пыль, failure-first РФ-кейс). Рекомендую A primary + C как «свой» бытовой контраст в Р2 (не на hook).
2. **Vertical farming — насколько глубоко?** Сейчас распределено: F1 в Р1 как 1-min summary + F6 в Р2 как deep dive (~3 мин). Альтернатива: один сильный 5-минутный блок в Р2 целиком про vertical farming. Какой формат предпочитает владелец?
3. **Р4 «Supply chain» — 12 мин достаточно?** Текущая длительность не позволяет глубоко уйти в agentic-механизмы (Tract architecture, Procuresprint workflows). Если методолог скажет «недостаточно глубоко» — можно расширить за счёт Р3 (10→8 мин).
4. **РФ-блок — 15-20% объёма?** Сейчас рассыпан по всем 5 уровням; суммарно ~10-12 мин из 75 = **13-16%**. Это **ниже** L9 (22-25%). Это **намеренно**: L10 не имеет столь специфического РФ-narrative (как было ВКА Можайского в L9), но владелец может попросить усилить.
5. **EU AI Act — отдельный слайд или строка в Normative References?** Сейчас в Р5.4 как 2-минутный блок + одна строка в Normative References. Альтернатива — целый слайд (s31 «EU AI Act high-risk classification») как примера применённой регуляторики.
6. **L4 agentic AI — достаточно ли visual proof?** Cargill / Tract / Olam — concepts абстрактные для студентов 3 курса. Возможно нужен один conceptual слайд «как agent делает hedge: pseudo-flow» для grounding. Confirm with methodology-critic.

---

## Slide-budget превью (для Phase 5)

- **Total ~32-35 слайдов**; media-rich **19-22** (60-65%, comfortable над ≥50% порога с запасом 2-3 на licence-fail risk).
- **Section dividers:** 6 (Р0-Р5); cover + lecture-map + Q&A: 3; content: ~22-25; pacing ~2-2.5 мин/content slide.
- **Lec-N-1 pattern compliance:** match lec-09 (cover + lecture-map + section dividers + dedicated Q&A; top progress bar только на dividers + cover; hero on s01 + s39).
- **Schema-readability checklist:** для лестницы keystone (s02), Cognitive Pilot vs ИТЭЛМА (s16), 5 критериев (s32), career-map (s33) — обязательно designer + critic pass.

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

- **Документированные провалы ИИ + выученные уроки:** 11 strict-in failure блоков (F1-F11 в разделах + connectivity + vendor lock-in в Р5).
- **Фундаментальные ограничения / риски:** open-environment vs closed-loop (vertical farming); закон термодинамики vs ML; threshold accuracy ≠ deployment readiness; cloud-first для off-grid = архитектурная ошибка.
- **Критерии «здесь ИИ не нужен / не применим»:** 5 (+2 бонус) в Р5.5.
- **Более правильные альтернативные инструменты:** для каждого критерия указана альтернатива (mechanical weeders, RAG-grounded, edge-AI, open-source hardware, direct soil sampling).
- **Бюджет:** **30 из 75 мин = 40%** strict-in (см. failure-bucket budget table). Comfortable margin над ≥30%.

---

## Assessment

LO5 («сформулировать критерии когда AI не применим») покрывается всеми failure-блоками + явным сводом в Р5.5. LO1 (лестница 5 уровней + tools) — Р1-Р5. LO2 (критическая оценка вендор-claim) — каждый failure-блок (Monarch, Plantix, vertical farming, Cognitive Pilot).

Семинар sem-10 (если будет — отдельная задача, не в scope plan-v1): рекомендуемый case study на одном failure-блоке (Monarch demo-vs-production audit; или Cognitive Pilot vs пыль pre-purchase verification checklist).

---

## References (key sources, full list — research files 01-04)

- **AgTechNavigator** (2025-11-10) — John Deere See & Spray $31M gallons herbicide saved.
- **TechCrunch** (2025-03-24) — Plenty Chapter 11.
- **TechCrunch** (2025-11-18, 2025-11-19) — Monarch Tractor sued + layoffs.
- **The Guardian + Die Zeit + SourceMaterial** (Jan 2023) — Verra 94% phantom credits.
- **Stanford GPS Lab** (ITM 2025) — Russia GNSS Spoofing 2023-2024.
- **The Register** (2022-05-02) — John Deere disables Ukraine tractors.
- **FTC** press release (2025-01-15) — FTC Sues Deere.
- **Nature Food** (May 2024) — GPT inaccuracies in agriculture (West/Williams et al.).
- **NCBI PMC9366064** — Tomato brown rugose fruit virus (AppHarvest virus context).
- **Hannah Ritchie substack** — Vertical farming termodynamic gap.
- **Foodlore.blog** — 14 vertical farming bankruptcies 2025.
- **Яков и Партнёры** — «Digitalizing Russia's Agricultural Sector» (2024) + «AI in agriculture» (2024).
- **RTVI** — Cognitive Pilot фермеры суды (2025).
- **Фонтанка** (2026-01-26) — ИТЭЛМА на ПТЗ.
- **McKinsey** (2025) — How agility and AI could rewire agriculture trading.
- **Merck Animal Health** (2025) — 2 million cows monitored with SenseHub.
- **Cargill** (2026) — Cargill wins 2026 BIG AI Excellence Award.
- **Cambridge EJRR** — EU AI Act applied to agrifood.
- **CSIS / CSO Online** — Russia tractor remote-bricking analysis.
- **USDA** (2025-04-14) — Climate-Smart cancellation announcement.
- **Carbon Robotics** press (Feb 2025) — LaserWeeder G2 launch.
- **AgFunderNews** — Solinftec 243% YoY US expansion.
- **Future Farming** — Aigen Element gen2 + Bowles Farming partnership.
- **AgTechNavigator** (May 2026) — Oishii Series C $150M (vertical farming exception).

---

**Word count: ~3 350.**
**Cornerstone concepts: 7. Failure blocks: 11. Tools named: 50+. Strict-in: 40% (30/75 min).**

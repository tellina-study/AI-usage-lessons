# Лекция 10: AI в сельском хозяйстве — v2 plan

## Метаданные

- **Lecture:** 10 | **Module:** 2 (отраслевое применение) | **Duration:** 75 мин content (Р0-Р5) + 10 мин Q&A = 85 мин full session
- **Audience:** студенты-инженеры 3 курса (универсальная, не агро-специалисты)
- **Issue:** #126 | **Status:** v2 (Phase 1 revise applied) | **Date:** 2026-05-21
- **Keystone axis:** **Лестница AI-проникновения в АПК — от поля к полке** + injection «closed-loop vs open-environment AI» как объяснительный механизм провалов
- **Changes from v1:** см. блок «Changes vs v1» в конце документа.

## Topics Covered

Точное земледелие (See & Spray, LaserWeeder, xarvio, FieldView) / автономная техника (Monarch failure, Solinftec, Aigen, AGCO PTx) / livestock CV (SenseHub, CattleEye) / vertical farming collapse / агентный ИИ в цепочке поставок (Cargill, Tract, Olam Mindsprint) / advisory chatbots + Plantix + ChatGPT hallucinations / связь & привязка к поставщику (Мелитополь remote-brick, FTC v. Deere, GNSS-jamming) / РФ-контекст (Cognitive Pilot vs пыль, ИТЭЛМА, РСХБ, госпрограмма) / sustainability paradox / EU AI Act + USDA Climate-Smart cancellation.

## Prerequisites

- **Лекция 2** «Архитектуры современных моделей» — foundation models, edge inference.
- **Лекция 3** «Архитектуры AI-систем» — RAG, agentic patterns, on-device.
- **Лекция 7** «AI в медицине» — симметричный пример **closed-loop** среды (controlled environment, validated datasets, регуляторика). АПК — **зеркальный контраст**: open environment, шумные данные, regulatory вакуум.
- **Лекция 9** «AI в аэрокосмической и оборонной отрасли» — OODA-ось, satellite analytics, dual-use; в L10 overlapping элемент Sense (satellite for agriculture) трактуется кратко, без deep dive.

## Normative References

- **Международное.** EU AI Act (Regulation 2024/1689; высокий риск для autonomous agricultural machinery, AI literacy обязательства c февраля 2025). FAO AI roadmap for agrifood (April 2025 + October 2025 ATIO). UN ICRC position на autonomous agricultural robots (отсутствует — это **gap**).
- **США.** USDA AI Strategy FY 2025-2026; FTC v. Deere (2025-01); Climate-Smart Commodities cancellation (April 2025) → AMP rebrand; FCC ban DJI ag-drones (December 2025).
- **РФ.** Программа «АПК будущего» 2026-2030 (распоряжение Правительства от 31 декабря 2025); индекс цифровизации АПК 27,2 / 100 (Яков и Партнёры) против 75,5 у США.
- **Стандарты.** ISO 17532:2007 + ISO 19115 для farm data. Не «жёсткие» как DO-178C в Лекции 9 — это часть исторического vacuum в АПК.

## Learning Objectives

1. **LO1a (Remember).** Назвать пять уровней лестницы AI-проникновения в АПК (поле / робот / животное / цепочка поставок / потребитель) и для каждого — 2-4 dominating 2026 tools (вендоры + режимы).
2. **LO1b (Apply).** Для каждого уровня — оценить направление adoption (растёт / стагнирует / переоценено) с обоснованием через 2026-метрику и **anti-hype оговорку** (брéнд ≠ режим работы; demo ≠ deployment; declared ≠ measured).
3. **LO2 (Apply).** Критически оценить заявление вендора AgTech-решения (типа «autonomous tractor» или «AI-powered crop advisor») — отличить demo-condition от production-deployment; применить ≥3 теста к learning case.
4. **LO5 (Analyze).** Сформулировать ≥5 явных критериев «здесь AI не нужен / не применим» для агро-контекста; назвать конкретную не-AI или другой-AI альтернативу для каждого; объяснить, почему generic-LLM как farm advisor — антипаттерн категории.

---

## Несущая ось → keystone (ENFORCED — Лекция 4 lesson)

### Ось: **Лестница AI-проникновения — от поля к полке**

Пять уровней. Снизу вверх — растёт **степень контроля среды**, падает **биологическая непредсказуемость**, растёт **measurable ROI**:

| Уровень | Среда | AI-проникновение 2026 | Канонический success | Канонический failure |
|---|---|---|---|---|
| **L1 — Поле** (open environment, биологическая) | пыль, освещение, погода, патогены | низкое-среднее; «AI-augmented spray decisions» работает (See & Spray), generic robotics — нет | See & Spray 5M акров | Vertical farming collapse $1.37B+ |
| **L2 — Робот / машина** (semi-controlled, ограничено физикой машины) | вибрации, GNSS-jamming, отказ датчиков | низкое; autonomous tractor — pilot mode, не commercial scale | Carbon Robotics LaserWeeder (250k акров) | Monarch MK-V (иски 2025, layoffs) |
| **L3 — Животное** (semi-closed, индивидуальная вариативность) | заболевания, поведение, стресс | среднее; CV для здоровья работает, кормления — overfit | Allflex SenseHub 2M коров | Cainthus partnership — нет публичных метрик |
| **L4 — Цепочка поставок** (controlled cargo, logistic flows) | currency, weather, regulatory | высокое; **агентный ИИ лидирует** | Cargill CMAX + 2026 BIG AI Award | USDA Climate-Smart cancellation tail risk |
| **L5 — Потребитель / retail** (fully controlled, цифровые данные) | demand patterns, inventory | очень высокое; полностью production | Walmart × Cropin (–20% waste); X5 «Перекрёсток» ML с 2020 | — (этот уровень reliably работает) |

**Главная закономерность:** **AI penetration ↑ как удаление от биологической непредсказуемости ↑**. Это **не идеология**, это **observation 2026** — и **главное объяснение, почему AgTech-инвестиции рекомендуют сейчас supply-chain agentic-плеи, а не on-farm robotics pilots**.

«**Controllability**» в стрелке keystone = **насколько среда поддаётся стандартизации и измерению**. L1 поле — солнце, дождь, патогены неконтролируемы; L5 retail — каждая SKU имеет цифровой след, обороты, цену, остаток.

### Injection «closed-loop vs open-environment AI» — operational definition (наша рабочая формулировка для разделения сред — см. Cornerstone 2)

- **Closed-loop AI** = AI внутри **feedback-controlled cycle** в **controlled environment**, где (а) среда контролируется (теплица, фабрика, операционная), (б) feedback-data достоверны и timely, (в) AI-action возвращается в loop как next-cycle input. **Примеры курса:** медицина L7 (операционная — controlled, immediate feedback после хирургии), фабрика L11 (cyber-physical loop), Cargill commodity hedge L4 (basis-points feedback за минуты).
- **Open-environment AI** = AI вне controlled cycle: реальное поле, реальная погода, реальная биология, где (а) среда меняется неконтролируемо, (б) feedback delay по сезонам, (в) action-результат измеряется через много циклов. **Примеры курса:** L10 поле (большая часть AgTech), L9 дрон в неизвестной местности.
- **Применение к АПК:** vertical farming = **попытка перевести поле из open в closed** (LED + питание + климат под контролем); **Cognitive Pilot vs пыль** = open-environment ломает closed-loop CV assumptions; **Cargill commodity hedge** = closed-loop по basis-points (базисные пункты, 100 bp = 1%) feedback.

### Keystone slide в Разделе 0 (ДО первого погружения)

**Заголовок:** «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**».

Визуально: вертикальная лестница из 5 ступеней (L1 внизу — «Поле», L5 наверху — «Полка»). На каждой ступени — 1 строка «где AI работает» / «где ломается». Справа — стрелка «↑ controllability ↑ ROI» / «↓ биологическая непредсказуемость ↓».

**Это keystone-slide про саму ось** — не про устройство курса, не про защиту подхода, не про recap. Каждый следующий раздел = мотивированный подъём по одной ступени лестницы.

### Каждый раздел = мотивированный подъём по оси (не «всплывает»)

- Р1 → L1 «Поле».
- Р2 → L2 «Робот».
- Р3 → L3 «Животное».
- Р4 → L4 «Цепочка поставок».
- Р4-bis → meta-уровень «среда» (connectivity, vendor lock-in, regulatory) — **отделён** от L5 для чёткости.
- Р5 → L5 «Потребитель» + consolidation 5 критериев + payoff.

---

## Инструменты на каждом уровне таксономии (ENFORCED L4+ — Лекция 4 lesson)

> Принцип: каждый уровень — 2-4 dominating 2026 tools (вендор-режим), adoption-направление словами, anti-hype-оговорка, volatile-метрики → `[VFY-day-of]`. **Бренд режима ≠ название бренда** (например, «See & Spray» = «AI-augmented selective spray», не «autonomous robot»).

### L1 — Поле (precision farming / agronomy decision support)

- **Tools 2026.** John Deere See & Spray Ultimate (Blue River acquisition); Bayer Climate FieldView; BASF xarvio FIELD MANAGER (130k фермеров, 20M га); Syngenta Cropwise (70M га, 30 стран); Taranis (leaf-level CV). **РФ:** ExactFarming (12 700 хозяйств, 9.8M га), АгроСигнал, ГК «Прогресс Агро» (+5% ROI на пшенице).
- **Adoption.** Растёт быстро в US Corn Belt + EU + AU. **Стагнирует** у smallholders (digital divide расширяется по данным Syngenta-IPSOS 2025). РФ — медленнее, индекс 27,2 vs США 75,5.
- **Anti-hype.** **Бренд ≠ режим работы.** «AI advisory» часто = rule-based agronomic recommendations + visualization, не deep learning. «Climate FieldView 250M акров» = подписки, не «AI оптимизирует каждый акр». Точность рекомендаций деградирует за пределами US Midwest (validation bias). Привязка к поставщику — рекомендации tied to Bayer/Pioneer hybrids.
- **Инфраструктура** (отдельно от capability): satellite imagery (Planet Labs Dove 3m, ICEYE SAR), GNSS RTK ground stations, mobile connectivity на полях (см. провал F15 — 18% US farms без интернета вообще).
- **Volatile** (`[VFY-day-of]`): See & Spray acreage прирост; xarvio Japan rice yield guarantee 2025 результаты; ExactFarming actual user count.

### L2 — Робот / машина (autonomous machinery + harvest robotics)

- **Tools 2026.** Carbon Robotics LaserWeeder G2 ($1.4M / машина, 150+ deployed, 14 стран); Solinftec Solix (243% YoY US expansion); Aigen Element gen2 ($50k, solar + mechanical); AGCO PTx Trimble Outrun (retrofit-mode autonomy для mixed-fleet); Naïo Technologies Orio (в judicial recovery 2025); Bonsai Robotics AR 500 (orchard autonomy); Tevel Aerobotics (flying apple pickers); Saga Robotics Thorvald (UV-C ночные 150+ units, 20% UK strawberry market — обработка ультрафиолетом, **не** harvest). **РФ:** Cognitive Agro Pilot (1200+ установок CV); ИТЭЛМА (спутниковый, конец 2025 на «Кировцах»); Геоскан 201 Агрогеодезия (БПЛА).
- **Adoption.** Растёт в **специализированных нишах** (strawberry UV-C, almond/citrus orchards, vegetable beds); **стагнирует** в broadacre (Monarch банкрот, FarmWise wind-down 2025, Naïo recovery). **РФ:** ИТЭЛМА — структурный сдвиг ландшафта 2026 (sensor-fusion-AI на multi-GNSS вместо CV-only).
- **Anti-hype.** **«Demo ≠ production»** — Monarch MK-V продал «autonomous» tractors, которые «unable to operate autonomously» (иск Burks Tractor ноябрь 2025). «Specialization побеждает generic» — universal farm robot не существует в 2026. Strawberry-harvesting robot $200-350k capex, addressable manual labor $50B, robots <5%. **UV-C night treatment ≠ harvest** — Saga 20% UK = ночная обработка, не сбор.
- **Инфраструктура.** GNSS-jamming спойлит точное земледелие в Финляндии (>122k авиа-рейсов с interference Q1 2025); FCC ban DJI ag-drones (декабрь 2025) ломает 80% US ag-spray drone fleet.
- **Volatile**: LaserWeeder pricing, Solinftec deployments per state, Monarch fate (laid-off → liquidation pending), Cognitive Pilot total installations.

### L3 — Животное (livestock CV + biometrics)

- **Tools 2026.** Allflex SenseHub (MSD Animal Health, 2M коров mounted milestone 2025); CattleEye (GEA-acquired 2024; 60 ферм, 11 000 коров для lameness detection); DeLaval VMS V310 (robotic milking, 99.8% attachment rate — то есть доильный аппарат успешно подсоединяется к вымени 998 раз из 1000; +15% North American installations); Connecterra IDA (Danone, Bayer, Kersia клиенты); Cainthus (Cargill partnership); Cargill Birdoo (CV для broiler weight, >95% accuracy). **РФ:** GEA Russia + Lely + DeLaval (impacted санкциями, частичное импортозамещение 2026); Connectome.ai (Сколково CV для контроля рождения телят).
- **Adoption.** Растёт стабильно (CV дёшев, dairy/poultry economic value высок); консолидация (GEA acquired CattleEye, MSD acquired Antelliq за $3.85B). РФ: ограничено санкциями + AI-функционал зарубежных систем требует firmware updates из Европы — уязвимая точка.
- **Anti-hype.** **Holstein-bias** как separate lesson: algorithm tuned для Holstein / dairy breeds — для местных пород РФ (Холмогорская, Ярославская, Якутская) калибровка слабая, нужна **architecture asymmetry** в datasets. Subscription costs ($30/cow/year) для small dairies (<50 cows) — overkill. CV требует чистых barns + good lighting — tie-stall barns не подходят.
- **Инфраструктура.** Camera install (overhead для barn / parlour exit), cloud для analytics, mobile alerting для vets.
- **Volatile**: SenseHub deployed count, GEA Russia deliveries (sanctions impact), DeLaval VMS attachment-rate updates.

### L4 — Цепочка поставок (агентный ИИ procurement + commodity trading + logistics)

- **Tools 2026.** Cargill CMAX + CarVe (2026 BIG AI Excellence Award); Tract (€18.6M Series A, 4 anchor customers Cargill+ADM+Olam+LDC); Olam Mindsprint (Procuresprint **агентная закупка** = AI-агент выбирает поставщика по compliance + price + ETA правилам автоматически; Wipro 2026 large transformation); Bunge + Bangkok Produce blockchain (deforestation-free soy для Charoen Pokphand); ClimateAi (climate-adaptive crop planning agents); Revenue.ai (commodity trading agents, –25..35% **hedge slippage** = расхождение между ожидаемой ценой хеджа и фактически исполненной; меньше slippage = меньше потерь); Cropin Cloud + Sage GenAI (>30M acres digitized; PepsiCo India, Walmart partnerships); Walmart × Cropin (–20% food waste); Tesco AI demand forecast (–30% food waste vs 2017). **РФ:** X5 «Перекрёсток» ML с 2020 (200 факторов прогноза спроса); Магнит F&R (in-house, Napoleon IT, 46 РЦ к январю 2026); РСХБ «Своё Фермерство» (10 000 партнёров, 1.25M товаров).
- **Adoption.** **Лидирует в production-deployment.** McKinsey: «traders measure outcome в basis-points (базисные пункты, сотые доли процента — 100 bp = 1%), fast feedback loop». РФ-крупные ритейлеры (X5, Магнит) — мировой уровень in-house ML.
- **Anti-hype.** Агентный = пока **узкий** (hedge decision, procurement compliance), не end-to-end supply chain orchestrator. **Агентный ИИ** = ИИ-агент с inference-циклом + tool-use, не один-shot ответ, выполняет multi-step задачи автономно (см. Лекция 3). Tract — это **data backbone**, не agentic per se. Blockchain ≠ AI; integration AI-side всё ещё в pilot phase в Bunge. РФ: AI-сервисы РСХБ **заявлены** (declared), **подтверждённых production-метрик нет**.
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

### Раздел 0 — Keystone + hook (5 мин)

**Цель.** Предъявить лестницу как карту лекции; зацепить hook'ом failure-first, который сразу показывает контраст «где AI работает / где провалился».

**Hook primary — B: Plenty Compton split-frame ribbon-cutting май 2023 + закрытие декабрь 2024.** Split-frame: слева — фото ribbon-cutting церемонии в Лос-Анджелесе май 2023 с делегацией (CEO, мэр), справа — фото закрытого фасилитета декабрь 2024 (19 месяцев). Подпись: «**$940M потерь, valuation $1.9B → <$15M (–99%)**». 2026-evergreen, failure-first, прямо служит AI-Failure rule + course mission.

**Hook fallback — C: Cognitive Pilot vs пыль** (РФ-кейс, 4 иска фермеров на 12,7 млн ₽ за CV-сбои в пыли). Используется если split-frame визуал не сложился; удерживает audience attention через локальный контраст. **Не используется** одновременно с Plenty (один failure-hook на cover).

**Hook A (See & Spray BEFORE/AFTER)** — **перенесён в Р1** как opening working case (естественное место visual-wow «вот success на L1»). Не на cover.

**Keystone slide.** Вертикальная лестница 5 уровней. Заголовок: **«Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом»**. + Operational definition Closed-loop vs open-environment одной строкой.

**Roadmap slide.** 6 содержательных разделов + Q&A; LO сверху, тайминг внизу.

**Media-rich слайды (Р0):** (1) hook Plenty Compton split-frame; (2) keystone лестница visualization (drawio); (3) roadmap — lecture-map.

### Раздел 1 — L1 «Поле»: precision agronomy + advisory (14 мин)

**Цель.** Показать самый нижний уровень — open environment, биологическая непредсказуемость; где AI работает (See & Spray) и где ломается (vertical farming, generic LLM advisor).

**Opening working case — A (1 мин):** **John Deere See & Spray Ultimate BEFORE/AFTER** на хлопковом поле — selective spray в дюзах + counter «–50% non-residual гербицидов, 5M акров». Visual-wow success-first, переход к остальным L1 working cases.

**Working cases (3 дополнительно, 3 мин).**
- **BASF xarvio FIELD MANAGER** — 130k фермеров, 20M га, 100 стран; Japan rice yield guarantee 2025 (outcome-based, first в мире).
- **Climate FieldView (Bayer)** — 250M акров / 23 страны; >50% US corn/soy/cotton.
- **РФ-параллель: ГК «Прогресс Агро»** — дифференцированное внесение азота на 2 800 га, +5% рентабельности (внутренний замер, не peer-review, но публичная метрика). ExactFarming 12 700 хозяйств, 9.8M га.

**Strict-in failures (9 мин).**

**F1 + F6 consolidated → Vertical farming deep dive (5 мин).** Failure-flagship Р1 — closed-environment попытка переехать из L1 open в L1 closed:
- **AppHarvest 2022 + ToBRFV (Tomato Brown Rugose Fruit Virus = томатный коричневый шершавый плодовый вирус):** в закрытой теплице 60 акров вирус распространился по всему фасилитету за дни. «**Closed-loop ↑ blast radius**» = в контролируемой среде сбой имеет увеличенный радиус поражения, потому что нет естественных барьеров.
- **Plenty bankruptcy:** $940M потеряно; Compton 19 мес (открыт май 2023 → закрыт декабрь 2024); valuation $1.9B → <$15M (–99% коллапс).
- **Bowery $32M never-used equipment** + **14 банкротств vertical farms 2022-2025 catalogue ($1.37B+)** — Foodlore.blog systematic.
- **Tortuga (acquired by Oishii март 2025)** как footnote: «технический успех ≠ коммерческий» — narrow positive (50% reduction в harvest expenses на технической стороне) inside collapsed category. Это **business-model lesson**, не technical robotics lesson.
- **Урок:** AI работает на знаменателе; если знаменатель (LED ≈ 100× free sunlight, Hannah Ritchie / MDPI Sustainability) фундаментально выше — ML бессилен. «Закон термодинамики важнее ML».
- **Bridge Р1→Р2:** «AI не справляется в open-environment (failure F2-F3 ChatGPT+Plantix) И в попытке закрыть environment (vertical farming). Теперь смотрим на L2 — semi-controlled environment робота: где specialization работает / где generic ломается.»

**F2. ChatGPT/Bard hallucinations в agronomy (2 мин)** — Nature Food 2024 (West/Williams et al.). **Кто/что/масштаб:** исследователи протестировали GPT-3.5 / GPT-4 / Bard на 184 вопросах о применении пестицидов и гербицидов; модели **уверенно рекомендовали** неправильное окно применения для конкретных культур → если фермер выполнил бы — significant crop damage. Это **research finding** (controlled experiment), не documented real-world disaster — но **вес примера такой же**: confident wrong опаснее admitted don't-know. Альтернатива: **RAG-grounded** в local regulator (USDA-EPA, EU-EFSA, Россельхознадзор) + явный отказ при low confidence + human-in-the-loop экстеншн-агент.

**F3. Plantix 10-15% misdiagnosis (2 мин)** — даже 90% accuracy на 10M+ загрузок = сотни тысяч неправильных pesticide-рекомендаций. Источник 85-90% accuracy — **self-reported Plantix** (Frontiers in Plant Science 2020 study на dataset images), **не independent field validation**. **Threshold accuracy ≠ deployment readiness.** Альтернатива: uncertainty-aware рекомендация с abstention.

**Russian context.** ExactFarming (12 700 хозяйств, 9.8M га); АгроСигнал (мониторинг ГСМ); ГК «Прогресс Агро» как успех. Индекс цифровизации АПК РФ 27,2 vs США 75,5 (Яков и Партнёры) — структурный gap, не выдумка пропаганды.

**Media-rich:** (4) See & Spray Ultimate в работе (Deere press); (5) xarvio Japan rice guarantee map; (6) Plantix UI screenshot + misdiagnosis breakdown QuickChart; (7) AppHarvest virus spread схема (mermaid); (8) ChatGPT hallucination screenshot из Nature Food paper; (9) Plenty Compton split-frame (если не на cover).

### Раздел 2 — L2 «Робот / машина»: автономная техника (15 мин)

**Цель.** Показать промежуточный уровень — semi-controlled environment; где AI работает в узкой specialization (LaserWeeder, Solinftec, Saga UV-C), где ломается в generic (Monarch, FarmWise). F6 vertical farming **удалён** (consolidated в Р1).

**Working cases (4-5).**
- **Carbon Robotics LaserWeeder G2** — 250k акров обработано, 15B weeds уничтожено, $1.4M/машина. Заменили химию физикой через CV. 240W лазер + 40M labeled images, distinguishes 100+ crop types. **G2 (Feb 2025)** — modular 6.6-60 ft boom, faster, lighter.
- **Solinftec Solix** — 243% YoY US expansion 2025; >100 robots в IL, IN, KS, IA, WI, TX; до 98% reduction в herbicide volume (vendor self-report — caveat); 24/7 solar-powered + self-refilling spray. 2025 features: Discovery Mode, Starlink integration, obstacle detection.
- **Aigen Element gen2** — $50k unit, 100% solar, 50 units в 2025 partnership с Bowles Farming. Дешёвая mechanical strike альтернатива к LaserWeeder.
- **Saga Robotics Thorvald** — 150+ units, 97% uptime, >200 000 autonomous km. **20% UK tabletop strawberry market — UV-C ночная обработка, НЕ harvest.** £8.4M raise; 13 leading UK growers; target 30% UK 2026.
- **AGCO PTx Trimble Outrun** — retrofit-mode autonomy для mixed-fleet (Fendt, Massey, Deere, CNH); альтернатива Deere closed-system; Tech Day 2025 demonstrated; goal full autonomous crop cycle by 2030.

**Strict-in failures (7.5 мин — 50% Р2 strict-in distribution).**

**F4. Monarch Tractor (2.5 мин)** — иск Burks Tractor ноябрь 2025: продали «defective» tractors 2024, unable to operate autonomously. 102 увольнения, риск shutdown. $220M raised, Foxconn lost. **Урок:** маркетинг как «autonomous» при том, что autonomy не выдержит судебной проверки = структурная trap для всей категории. **Demo ≠ deployment.** **Альтернатива:** supervised autonomy + явный disclosure capability / non-capability.

**F5. FarmWise wind-down + Naïo Technologies judicial recovery (2.5 мин)** — FarmWise (CV-weed-robot, $30M+ raised) restructuring 2025; Naïo (Toulouse) judicial recovery June 2025, revenue €4M (2021) → €2.4M (2024). Структурная причина — «модели в тепличных условиях не работают в поле»: пыль, освещение, тени, shadow bias. **Альтернатива (AP2b — genuine не-AI):** mechanical weeders (Lemken Steketee EC-Weeder, Kverneland Onyx) — менее «smart», но deterministically robust.

**F7. Strawberry-picking robot economics (2.5 мин)** — robot $200-350k capex; annualized $68-130k/год; США адресуемый ручной труд $50B; роботы <5%. CA picking-labor $43k на акр. «Harvesting is the last great unsolved problem». «Robots still struggle with tasks humans master in days». **Альтернатива:** H-2A guest worker programs + ergonomic improvements (стульчатые комбайны).

**Russian context (~2 мин).** Cognitive Agro Pilot 1200+ установок vs **4 иска фермеров на 12,7 млн ₽ (2025)** — пыль на полях не позволяла CV видеть кромку нескошенного. **ИТЭЛМА** (multi-GNSS sensor-fusion-AI) на «Кировцах» с конца 2025 — **архитектурный выбор внутри AI domain** (см. P1-6 reframe ниже). Геоскан 201 Агрогеодезия — пример узкого работающего решения (NDVI, multispectral).

**Cognitive Pilot vs ИТЭЛМА reframe (КРИТИЧНО — P1-6).** Это **НЕ «AI vs не-AI»**, это **архитектурный выбор внутри AI-домена**: CV-AI хрупок в open-environment (пыль ломает edge-detection); sensor-fusion-AI на multi-GNSS («Итэлма Квадро» обрабатывает сигналы нескольких созвездий + RTK поправки + Kalman filtering) — другой класс AI, более робастный к пыли, но требует исправного спутникового приёма. **Эти два решения покрывают разные функции:** ИТЭЛМА = «**где я нахожусь**» (навигация по полю с точностью 2-5 см); Cognitive Pilot = «**что я вижу**» (CV-распознавание кромки нескошенного / препятствий). Это **разные классы решений** — нельзя их сравнивать как «один лучше другого».

**Media-rich:** (10) LaserWeeder G2 в поле (Carbon Robotics press); (11) Solinftec Solix robot photo (Solinftec press); (12) Monarch MK-V на лужайке + headline TechCrunch иск (real screenshot); (13) Cognitive Pilot vs ИТЭЛМА сравнительная diagram (drawio — **критичный schema-readability slide**).

### Раздел 3 — L3 «Животное»: livestock CV (12 мин — расширено из 10 в v1)

**Цель.** Показать L3 как «AI работает стабильнее, чем на L1-L2», и почему — экономика животных concentrated и individual-level измеримая.

**Working cases (4, 6 мин).**
- **Allflex SenseHub** — 2M коров mounted (milestone 2025); reproductive, health, nutritional, wellbeing monitoring. SenseHub Cow Calf для beef breeding, SenseHub Feedlot. Partnership с Nestlé farms.
- **CattleEye + GEA acquisition (2024)** — low-cost CCTV + cloud AI для lameness detection при выходе из milking parlour. 60 ферм, 11 000 коров; через GEA channel — trusted by farms managing >250 000 cows worldwide.
- **DeLaval VMS V310 (robotic milking)** — **99.8% attachment rate = success rate подключения доильного аппарата к вымени, 998 раз из 1000**; +15% North American installations 2025; VMS Batch Milking 20 ферм в 13 странах expected double каждый год; Flow-Responsive Milking standard на новых V300 с июня 2025.
- **Cargill Birdoo** — CV для broiler weight estimation; >95% accuracy без labour для clean/calibrate; saves 10-30g feed на bird; Americas-exclusive.

**Strict-in failures (3.5 мин).**

**F8. Cainthus tie-stall barns + small dairy economics + Holstein-bias (2 мин)** — три anti-hype урока в одном блоке:
1. CV требует чистых barns + good lighting; tie-stall barns (распространены в РФ, Восточной Европе) с обилием silhouettes + плохое освещение — challenging.
2. SenseHub subscription $30/cow/year — overkill для small dairies (<50 cows); ROI отрицательный.
3. **Holstein-bias** — algorithm tuned на dominantly Holstein dairy breeds (USA, EU); для местных пород РФ (Холмогорская, Ярославская, Якутская) калибровка слабая, нужна **architecture asymmetry** в datasets (transfer learning + локальные labeled data). 

**Урок:** AI capability ≠ AI applicability; physical environment + economics + breed-specific data determine deployable %. **Альтернатива:** для small dairies — manual observation + cheap thermometers + 1 раз в полгода ветеринар; для local пород РФ — local data collection + transfer learning перед deployment.

**F9. Russian dairy equipment uncertainty (1.5 мин)** — DeLaval, GEA, Lely after sanctions 2022. AI-функционал зарубежных систем требует firmware updates + cloud services из Европы. **Заявлено** (declared) — architectural риск; **подтверждённых публичных кейсов** отключения сервисов в РФ нет — **vapor risk**, не documented failure. **Альтернатива:** частичное импортозамещение (Лобня 2026, «Пакэйджинг Системс» 4 млрд ₽), но AI-стек пока без замены.

**Russian context.** GEA Russia + ограниченные поставки; Connectome.ai (Сколково CV для контроля рождения телят); Лобня производство молочного оборудования (март 2026).

**Media-rich:** (14) SenseHub на корове (Merck press); (15) CattleEye lameness detection UI (real screenshot if public); (16) DeLaval VMS V310 milking robot в работе (DeLaval press); (17) tie-stall vs free-stall barn diagram explaining CV-applicability + Holstein-bias visual.

### Раздел 4 — L4 «Цепочка поставок»: агентный ИИ поднимается (10 мин — сжато из 12 в v1)

**Цель.** Показать L4 как **place, где агентный ИИ лидирует в production-deployment в 2026**. Объяснить, почему: traders measure outcome в basis-points, fast feedback loop. Это контраст с L1-L2 где «сезон-длинный» feedback убивает ROI.

**Inline glossary (P0-3 fix — must при первом упоминании):**
- **Агентный ИИ** = ИИ-агент с inference-циклом + tool-use, не один-shot ответ, выполняет multi-step задачи автономно.
- **Basis-points (bp)** = базисные пункты, сотые доли процента (100 bp = 1%); единица measurement в финансах.
- **Hedge slippage** = расхождение между ожидаемой ценой хеджа и фактически исполненной (потери от исполнения).
- **Scope-3 emissions** = выбросы 3-го уровня (вверх и вниз по supply chain — не собственные операции компании; например, выбросы у поставщиков сырья и у потребителей продукта).
- **AI-MRV** = AI-системы для **измерения, отчётности, верификации** (Measurement, Reporting, Verification) carbon credits / выбросов (alternative to direct soil sampling).

**Working cases (5 мин, 4 кейса).**
- **Cargill CMAX + CarVe (2026 BIG AI Excellence Award)** — predictive port + shipping logistics, optimizes grain flows; CV для protein supply chain yield, waste reduction; Brazil grain logistics AI-driven mixing. 70+ стран, 1000+ facilities. **Pseudo-flow «как агент делает hedge»**: (1) Сенсор-уровень — мониторинг цен фьючерсов (CBOT corn, soybean) + погодных событий + currency; (2) Inference — модель оценивает направление цены через 5 / 30 / 90 дней + uncertainty bands; (3) Решение — открыть / закрыть / пере-балансировать хеджевую позицию **с явным human-in-the-loop утверждением** для крупных сделок (>$10M notional), автономно для малых; (4) Feedback — basis-points outcome за минуты-часы, обновление модели. Это **узкий агентный ИИ** (одно действие — hedge), не general autonomy.
- **Tract (Cargill+ADM+Olam+LDC)** — €18.6M Series A 2025 (Dawn Capital). Bridge supplier data и procurement processes (compliance / scope-3 emissions / provenance). **4 anchor customers — конкуренты**, shared infrastructure для compliance. **Tract = data backbone, не агентный per se** — это infrastructure layer над которой агенты работают.
- **Olam Mindsprint / Procuresprint** — Wipro 2026 «one of largest strategic transformation engagements». Farmsprint (plantation management), Procuresprint **агентная закупка** (агент выбирает поставщика по price + compliance + ETA автоматически), Tradesprint commodity trading.
- **Walmart × Cropin + Tesco AI demand forecast** — Walmart –20% food waste, Eden ML algorithm; Tesco –30% food waste since 2017. Demonstrate retail AI поднимается на L5.

**Strict-in failures (4 мин).**

**F10. USDA Climate-Smart Commodities cancellation (April 2025) (2 мин)** — $3.1B / 141 projects / 14 000 ферм / 3.2M acres pre-cancellation. Rebranded в AMP с pivots. **Урок:** federal policy = tail risk для AgTech business model. Companies over-rotated к public funding — exposed. **Альтернатива:** unit economics over policy-tailwind plays; investor sentiment 2025-26 уже shifted.

**F11. Verra phantom credits — 94% rainforest offsets «worthless» (2 мин)** — Pachama project overestimated by 8×. **AI-MRV** для carbon-claims = inference с большой uncertainty, marketed как «precise measurement». Whitewashing carbon-credit + AI-veneer = scaled greenwashing. **Альтернатива:** direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact.

**Russian context (~1 мин).** X5 «Перекрёсток» ML с 2020 (200 факторов, плодоовощная и молочная категории); Магнит F&R in-house с 2025 (46 РЦ к январь 2026); РСХБ «Своё Фермерство» (10 000 партнёров, 1.25M товаров). РСХБ AI-сервисы (AI-прогноз урожайности, geno-селекция) — **заявлены**, **production-метрики не опубликованы**. Это **паритет в L4-L5 retail-supply** при отставании в L1-L2.

**Media-rich:** (18) Cargill BIG AI Award announcement (Cargill press); (19) Tract Series A coverage (real news screenshot); (20) **«Как агент делает hedge» pseudo-flow diagram (drawio)** — критичный для grounding L4 абстракции; (21) Verra phantom credits Guardian investigation (real article screenshot); (22) USDA Climate-Smart cancellation announcement (USDA press); (23) X5 «Перекрёсток» dashboard / Магнит F&R архитектура (TAdviser source).

### Раздел 4-bis — Среда: связь, привязка к поставщику, регуляторика (8 мин — НОВЫЙ раздел)

**Цель.** Cross-cutting meta-уровень — **связь (connectivity)**, **привязка к поставщику (vendor lock-in)**, **регуляторика** — отделённый от L5 retail для чёткости (P1-2 fix). Все 3 sub-секции — strict-in (100% этого раздела) — failure-перспектива.

**4-bis.1. Связь (3 мин) [AP5 inline].** 18% американских ферм без интернета вообще; **>122 000 авиа-рейсов с GNSS-interference Q1 2025** (Stanford GPS Lab); финские поля «unfarmable using GNSS-based tractors» из-за российских EW-станций. Starlink в РФ **запрет апрель 2026 на 6 мес**. **Урок (AP5):** edge-AI / TinyML / offline-first — единственная реалистичная архитектура для большинства farms. Cloud-first AI for agriculture = архитектурная ошибка.

**4-bis.2. Привязка к поставщику + санкционный shock (3 мин) [AP6 inline reinforcement].** **FTC v. John Deere (январь 2025)** — десятилетние ограничения ремонта; trial 2026. **John Deere remote-brick Мелитополь май 2022** — 27 единиц техники на $5M удалённо отключены при попытке вывезти в Чечню. **Двойная оптика:** anti-theft success с одной стороны, vendor control surface с другой. Тот же mechanism применим к РФ-фермерам, у которых **Climate FieldView отключился после 2022** (Bayer вышел из РФ). **Урок для всех стран периферии:** AI-зависимость = политический риск; российский опыт — natural experiment, что бывает, когда импортный AI-стек отключается. **FCC ban DJI ag-drones (декабрь 2025)** — 80% US ag-spray drone fleet под угрозой; альтернативы 2.5× дороже.

**4-bis.3. Регуляторика (2 мин).** EU AI Act high-risk для autonomous agricultural machinery — **high-risk classification** означает: producers нуждаются в compliance teams; liability cascade (производитель + AI provider + фермер); mandatory pre-market conformity assessment; технический файл и логи. USDA AI Strategy FY2025-26 формальна. РФ «АПК будущего» 2026-2030 декларативна, госпрограмма «Цифровое сельское хозяйство» 2019-2024 цель удвоения производительности не достигнута (АПК в 2024 −3,2%).

**Media-rich:** (24) GNSS-jamming Финляндия карта (Stanford ITM 2025 paper figure); (25) FTC v. Deere press conference (real photo); (26) Мелитополь John Deere stolen tractors map (CSO Online graphic); (27) РФ-АПК-AI 2026 summary table (drawio — anchor для exam recall, P1-4 reader fix).

### Раздел 5 — L5 «Потребитель / retail» + 5 критериев + payoff (6 мин)

**Цель.** Закрыть лекцию L5 retail + consolidation 5 анти-AI критериев + career + reading + callback.

**5.1. L5 «Потребитель / retail» (2 мин).** Walmart × Cropin (–20% waste, Eden ML); Tesco AI demand forecast (–30%); X5 + Магнит — РФ-параллель мирового уровня. **Этот уровень reliably работает**: это **самый зрелый слой АПК-AI** и единственный, где «AI everywhere» — не hype.

**5.2. 5 критериев «когда не AI» (2 мин).** Consolidation slide с visual checklist (см. таблицу ниже).

**5.3. Career angle + reading + closing callback (2 мин).**
- **Career.** Профильные технические университеты предлагают магистратуры по agro-IT / agro-engineering / digital agronomy. Российские работодатели: Cognitive Pilot, ИТЭЛМА, Геоскан, ЭФКО, Русагро Тех, РСХБ.цифра, Магнит digital, X5 Tech, ExactFarming. Международные траектории: John Deere, Bayer Crop Science Digital, BASF Digital Farming, Cargill AI lab, Cropin (India). **Civil path** — Sber AI for agriculture, Сколково AgTech-резиденты (Connectome.ai, СиСорт). **Без агитации.**
- **Reading list.** Russell & Norvig AIMA 4th ed; McKinsey: «How agility and AI could rewire agriculture trading» (2025); Hannah Ritchie substack: «Vertical farming» (термодинамический gap); Foodlore.blog: «Why Vertical Farms Go Bankrupt» (14 bankruptcies 2025); Яков и Партнёры: «Digitalizing Russia's Agricultural Sector» (2024); FAO ATIO October 2025; Stanford GPS Lab ITM 2025; Cambridge EJRR: «EU AI Act applied to agrifood».
- **Closing callback.** «Лестница пять уровней. AI поднимается от поля к полке, и работает по-разному на каждом. Инженер держит её в голове целиком — выбирая для каждой ступени правильный инструмент, и зная, где AI не работает».

**Media-rich:** (28) 5 критериев «когда не AI» — dense visual checklist (drawio); (29) career-map drawio (РФ + международные работодатели); (30) closing callback — keystone repeated as bookend (s39 hero).

### Q&A слот (10 мин)

Готовые backup-вопросы (см. также Real Q&A reader-simulator):
- Почему vertical farming не сработала — это AI fault или unit economics?
- «Closed-loop vs open-environment» — это термин из ML literature или вы его вводите специально для лекции?
- Может ли LLM-advisor реально заменить агронома?
- Что произойдёт с РФ-АПК через 5 лет если санкции снимут?
- Agentic AI в supply chain — насколько agent реально автономен? Cargill CMAX сам открывает позиции на бирже?
- ИТЭЛМА vs Cognitive Pilot — это правда замена или они решают разные задачи?
- Vertical farming — Oishii выжила и привлекла $150M в 2026. Это исключение или поворот?
- Будет ли autonomous tractor mass-deployed к 2030?
- Где этическая граница AI в АПК (с учётом 80% smallholders глобально)?

---

## Failure-bucket budget (strict-in ≥30%) — после restructure

| Раздел | Минут content | Strict-in минут | % strict-in | Bucket-класс |
|---|---|---|---|---|
| Р0 Keystone + hook (failure-first) | 5 | 0 | 0% | — |
| Р1 L1 «Поле» (vertical farming consolidated 5 + ChatGPT 2 + Plantix 2) | 14 | 9 | 64% | overpromise / closed-loop blast / threshold accuracy |
| Р2 L2 «Робот» (Monarch 2.5 + FarmWise 2.5 + strawberry 2.5; F6 удалён) | 15 | 7.5 | 50% | overpromise / robotics-econ |
| Р3 L3 «Животное» (Cainthus tie-stall+Holstein-bias 2 + РФ dairy 1.5) | 12 | 3.5 | 29% | applicability gap / architecture asymmetry |
| Р4 L4 «Цепочка поставок» (USDA 2 + Verra 2) | 10 | 4 | 40% | regulatory / overpromise |
| Р4-bis Среда (connectivity 3 + vendor-lock 3 + regulatory 2) — все из failure-перспективы | 8 | 8 | 100% | connectivity / vendor-lock / regulatory |
| Р5 L5 + payoff (5 критериев consolidation 2 strict-in) | 6 | 2 | 33% | consolidation |
| Q&A | 10 | — | — | — |
| **Total active (75 мин content)** | **70 мин + 5 мин buffer** | **34 мин** | **48.6%** | — |

**Итого strict-in: 34 из 70 мин active = 48.6%.** Comfortable margin над ≥30%.

**Distribution check:** Р1 64%, Р2 50%, Р3 29%, Р4 40%, Р4-bis 100% (по definition meta-блок про failure), Р5 33%. Без Р4-bis (specialized failure section) — distribution Р1-Р5 = 64/50/29/40/33% = **холистично без single-section over-concentration**. Р4-bis 100% — это **дизайн раздела** про среду как failure-перспективу; не «over-concentration», а сам по себе failure-themed раздел.

**Counter-check.** Если на Phase 3/7 strict-in доля <30% или сконцентрирована в одном артефакте → verdict REVISE.

---

## Anti-AI критерии (≥30% mandate component)

**Финальная пятёрка для Р5.2 consolidation slide:**

| # | Критерий | Пример | Альтернатива |
|---|---|---|---|
| **AP1** | **Закон термодинамики важнее ML** — когда фундаментальная экономика (energy/capex) ≥ 10× рыночной цены продукта | Vertical farming для commodity leafy greens — LED ≈ 100× free sunlight (Hannah Ritchie / MDPI Sustainability) | Открытый грунт или greenhouse при энергии < $0.10/кВт·ч; vertical только для high-value crops |
| **AP3** | **Threshold accuracy ≠ deployment readiness** — даже 90% accuracy на масштабе = сотни тысяч ошибочных high-stakes решений | Plantix 10-15% misdiagnosis на 10M+ загрузок = сотни тысяч неправильных pesticide-рекомендаций в год | Uncertainty-aware рекомендация с abstention; «не уверен → спроси эксперта» |
| **AP4** | **Generic LLM в advisory mode** — generic chatbot для фермеров с pesticide/fertilizer recommendations = категорический антипаттерн | ChatGPT/Bard рекомендация неправильного окна гербицида (Nature Food 2024) — significant crop damage риск | **RAG-grounded** (Cornerstone 6) в local regulator (USDA-EPA, EU-EFSA, Россельхознадзор) + human-in-the-loop экстеншн-агент |
| **AP6** | **«AI-driven equipment» = vendor lock-in trap** — чем больше AI и telematics в трактор, тем сильнее vendor control surface | FTC v. Deere 2025-01; Мелитополь remote-brick 2022; Bayer FieldView выход из РФ; FCC ban DJI ag-drones | Open-source farming hardware (Farm Hack); right-to-repair compliance; multi-vendor стратегия; mechanical fallbacks |
| **AP7** | **AI-MRV для carbon claims без direct measurement** — inference с большой uncertainty, marketed как «precise measurement» | Verra 94% phantom credits; Pachama overestimate 8×; Bowery $32M never-used equipment | Direct soil sampling + transparent uncertainty bands; AI как hypothesis, не как fact |

**Дополнительные критерии inline в Р4-bis (не в основной пятёрке Р5 consolidation):**

| # | Критерий | Пример | Альтернатива |
|---|---|---|---|
| **AP2a** | **CV не выдерживает open-environment условий — используй другой класс AI** (architecture choice within AI domain) | Cognitive Pilot vs пыль (4 иска 12,7М ₽ 2025); FarmWise dust + lighting failure (wind-down 2025) | **Sensor-fusion AI на multi-GNSS** (ИТЭЛМА «Итэлма Квадро» — обработка сигналов нескольких созвездий + RTK + Kalman) — другой класс AI |
| **AP2b** | **Когда AI как класс не применим (термодинамика, fundamental physics) — используй mechanical / direct measurement** (genuine не-AI) | Vertical farming → открытый грунт; FarmWise → mechanical weeders Lemken Steketee / Kverneland Onyx | Mechanical hardware: deterministic, robust к open-environment, без AI-стека |
| **AP5** | **Cloud-first для off-grid farm** — когда farm на 18% американских (без интернета) или в зоне GNSS-jamming | 60% US фермеров на cellular/satellite; Финляндия unfarmable из-за российских EW; РФ Starlink запрет 30 апреля 2026 на 6 мес | Edge-AI / TinyML / offline-first; hybrid (cellular + LoRa + Starlink + RTK ground link) для redundancy |

**AP2a + AP2b** — explicit разделение P1-6 fix: «AI vs другой AI» (architecture choice) vs «AI vs не-AI» (genuine alternative). Это **критично для anti-hype message** — иначе студент сделает обратный вывод «значит no-AI всегда лучше».

---

## Cornerstone → Anti-AI critic mapping (P2-2 fix)

Явная связь cornerstone concepts → application через anti-AI критерии:

| Cornerstone concept | → | Anti-AI критерий (application) |
|---|---|---|
| #2 Open-environment vs closed-loop AI | → | **AP1** (термодинамика для closed попыток vs реальность) + **AP2a/AP2b** (open environment CV failures) |
| #3 Edge ML / TinyML | → | **AP5** (cloud-first off-grid = архитектурная ошибка) |
| #5 Vendor lock-in / right-to-repair | → | **AP6** (vendor lock-in trap) |
| #6 Foundation model + grounded reasoning | → | **AP4** (generic LLM альтернатива = RAG-grounded) |
| #7 Sustainability paradox | → | **AP7** (AI-MRV без direct measurement = scaled greenwashing) |
| #1 Точное земледелие | → | (применение, без anti-AI критерия — positive case) |
| #4 Tacit knowledge / hyperlocal context | → | (применение в AP4 как rationale для human-in-the-loop) |

В chapter каждый cornerstone развивается через свой anti-AI критерий как «application». Это превращает 2 list-а в **1 system** (concept → application → assessment).

---

## Cornerstone concepts (cross-artifact glossary lock)

7 ключевых терминов, которые повторяются в chapter / slides / speech одинаково (после v2 plan approval — glossary lock):

1. **Точное земледелие (precision agriculture / farming)** — система рекомендаций и автоматических действий, основанная на полевых данных (спутник, дрон, датчики), с целью выполнения переменных операций по полю.
2. **Open-environment vs closed-loop AI** — open-environment = реальные полевые условия (пыль, освещение, патогены); closed-loop = AI внутри feedback-controlled cycle в controlled environment (теплица, vertical farm, фабрика). При первом упоминании в chapter: «**наша рабочая формулировка для разделения сред**».
3. **Edge ML / TinyML** — машинное обучение на устройстве (датчик, гейтвей, трактор-кабина) без cloud-uplink; единственная реалистичная архитектура для off-grid farms.
4. **Tacit knowledge / hyperlocal context** — неявные знания фермера о его поле (микроклимат, дренаж, weed pressure), приобретаемые годами наблюдения. AI не может построить из satellite + IoT за 1 сезон.
5. **Vendor lock-in / привязка к поставщику + right-to-repair / право на ремонт** — экономико-юридическая зависимость от поставщика; чем больше AI и telematics, тем сильнее lock-in (Deere FTC case, Мелитополь, FieldView в РФ).
6. **Foundation model + grounded reasoning** — общая pretrained модель (TerraMind, Prithvi-EO 2.0) + RAG-привязка к локальным данным/нормам; альтернатива generic-LLM hallucinations.
7. **Sustainability paradox** — «AI для устойчивости» имеет собственный environmental footprint (data centers в Айове vs irrigation; GPT-3 = 700 000 литров воды). Net-positive — не автоматически.

---

## Misattribution warnings (P2-4 fix — отдельный раздел)

**Чтобы downstream chapter / slides / speech не сделали cascade misattribution из v1 footnotes:**

- **Indigo Ag НЕ в Verra-скандале.** Indigo использует **Climate Action Reserve** (не Verra), 2M tons verified, Microsoft 12-year 2.85M tons deal 2026. Pachama-style overstatement к Indigo неприменим.
- **Tract = data backbone, не агентный per se.** Tract — это infrastructure layer (supplier data + compliance). Агенты работают над ней, но сама Tract — это data plumbing, не autonomous agent. План L4 anti-hype уже учитывает.
- **Verra phantom credits affect rainforest offset projects**, не all AI-MRV. Agricultural soil-carbon — другая методология (Climate Action Reserve, ACR, Verra VM0042 v2). Не все AI-MRV — phantom; конкретно **rainforest offset методология** была раскритикована.
- **Saga Robotics 20% UK strawberry market = UV-C night treatment**, **не harvest**. Не путать с harvest robots (F7 strawberry-picking economics).
- **РСХБ AI-сервисы заявлены, подтверждённых production-метрик нет.** Не показывать как deployment success; формат: «заявлено N, метрик нет».

---

## Hero images plan для s01 + s39 (§3.7c)

### s01 hero (cover / ice-breaker) — Plenty Compton split-frame (Hook B primary)

- **Entity:** Plenty Compton facility — split-frame: ribbon-cutting май 2023 + закрытие декабрь 2024.
- **Source candidate Tier 1:** Plenty press release archive (Wayback Machine для май 2023) + TechCrunch / Bloomberg для декабрь 2024 closure photo.
- **Fallback Tier 2:** Wikipedia «Plenty Unlimited» commercial-use photo.
- **Fallback Tier 3:** Bloomberg / Forbes / TechCrunch hero image из article о closure.
- **Foreshadow keystone:** показывает L1 «Поле» закрытое попытку closed-environment AI fail — visual proof, что AI не справился с энергетикой LED vs sunlight.
- **Attribution label:** «Plenty Unlimited Inc. Compton facility, May 2023 / December 2024. Sources: Plenty press / TechCrunch.»

### s39 hero (closing / bridge к Лекции 11) — **PRIMARY: Carbon Robotics LaserWeeder G2** (P2-5 fix)

- **Primary:** Carbon Robotics LaserWeeder G2 iconic image (Tier 1 single source, visually strongest, single-frame). Foreshadow Lec-11 через подпись «**От поля до фабрики: AI-driven cyber-physical systems**».
- **Source candidate Tier 1:** Carbon Robotics press release Feb 2025 LaserWeeder G2 launch hero image.
- **Fallback Tier 2:** Cargill BIG AI Award 2026 page (less visual, but tied to Р4 как strongest L4 success).
- **Reject:** фотомонтаж «Solinftec → полка Магнита» — требует 2 lic + compositing risk.
- **Foreshadow Lec-11:** L2 robot в поле — пролог к L11 cyber-physical manufacturing.
- **Attribution label:** «Carbon Robotics LaserWeeder G2, February 2025. Source: carbonrobotics.com (press release).»

---

## Media-coverage plan (≥50% mandate)

Из ~32-35 типичных слайдов планируется ~21-23 media-bearing (≥60%, comfortable margin над ≥50%).

| # | Slide | Media type | Source candidate | Acquisition Tier |
|---|---|---|---|---|
| 1 | s01 cover | Plenty Compton split-frame hero | Plenty press May 2023 + TechCrunch Dec 2024 | Tier 1 (2 sources) |
| 2 | s02 keystone лестница | drawio diagram | own | own |
| 3 | s03 roadmap | drawio | own | own |
| 4 | s05 See & Spray в работе | photo | Deere press | Tier 1 |
| 5 | s06 xarvio Japan rice map | press image | BASF press 2025-10 | Tier 1 |
| 6 | s07 Plantix misdiagnosis | UI screenshot + QuickChart | Plantix.net + own chart | Tier 1+own |
| 7 | s08 AppHarvest virus spread | mermaid + photo | own + NCBI PMC9366064 | own+Tier 1 |
| 8 | s09 ChatGPT hallucination | screenshot from paper | Nature Food 2024 paper figure | Tier 1 (paper PDF) |
| 9 | s10 Plenty Compton split (если не на cover) | photo | Plenty May 2023 + TechCrunch 2024 | Tier 1 (2 sources) |
| 10 | s12 LaserWeeder G2 в поле | photo | Carbon Robotics press 2025-02 | Tier 1 |
| 11 | s13 Solinftec Solix | photo | Solinftec.com press | Tier 1 |
| 12 | s14 Monarch иск headline | screenshot | TechCrunch 2025-11-18 article | Tier 1 |
| 13 | s15 vertical farm bankruptcies timeline | QuickChart | own data viz | own |
| 14 | s16 Cognitive Pilot vs ИТЭЛМА | drawio (CV vs sensor-fusion-AI) | own | own |
| 15 | s18 SenseHub на корове | photo | Merck press 2025 | Tier 1 |
| 16 | s19 CattleEye lameness UI | screenshot if public | CattleEye.com / Fortune June 2025 | Tier 1-3 |
| 17 | s20 DeLaval VMS V310 | photo | DeLaval press April 2025 | Tier 1 |
| 18 | s22 tie-stall vs free-stall + Holstein-bias | diagram | own drawio | own |
| 19 | s24 Cargill BIG AI Award | screenshot | Cargill.com 2026 press | Tier 1 |
| 20 | s25 «Как агент делает hedge» pseudo-flow | drawio | own | own |
| 21 | s26 Tract Series A | news screenshot | Foodingredientsfirst 2025 | Tier 1 |
| 22 | s27 Verra Guardian investigation | screenshot | The Guardian Jan 2023 article | Tier 1 |
| 23 | s28 USDA Climate-Smart cancellation | press screenshot | USDA.gov 2025-04-14 | Tier 1 |
| 24 | s30 GNSS jamming Finland map | figure | Stanford ITM 2025 paper Figure | Tier 1 (paper) |
| 25 | s31 Мелитополь stolen tractors | map / graphic | CSO Online 572811 or The Register 2022-05 | Tier 1 |
| 26 | s32 FTC v Deere press conference | photo | FTC press 2025-01 | Tier 1 |
| 27 | s33 РФ-АПК-AI 2026 summary table | drawio (anchor для exam recall) | own | own |
| 28 | s36 5 critеria «когда не AI» | drawio checklist | own | own |
| 29 | s37 career map | drawio | own | own |
| 30 | s39 closing | Carbon Robotics LaserWeeder G2 hero | Carbon Robotics press 2025-02 | Tier 1 |

**Total real-image-bearing slides:** ~22 из ~35 = **63%**.
**Own-diagrams:** ~8 (drawio + QuickChart + mermaid).
**Real-image-via-6-tier:** ~22 (всё Tier 1 / Tier 2 fallback documented).
**Stylized Ocean-palette card с verbatim headline = mock, FAIL** — категорически избегаем.

---

## РФ-контекст блок (для anonymized аудитории)

РФ-слой **встроен в каждый уровень лестницы** как параллельный track + **anchor-summary в Р4-bis s33** (P1-4 reader fix — для exam recall):

- **L1 (Р1):** ExactFarming 12 700 хозяйств + 9.8M га; АгроСигнал; ГК «Прогресс Агро» +5% ROI. Индекс цифровизации 27,2 vs США 75,5 (Яков и Партнёры).
- **L2 (Р2):** Cognitive Agro Pilot 1200+ установок vs 4 иска фермеров на 12,7М ₽ за CV-сбои в пыли (**CV-AI**). ИТЭЛМА (**sensor-fusion-AI на multi-GNSS**) на «Кировцах» с конца 2025 — **архитектурный выбор внутри AI domain**, не «AI vs не-AI». Геоскан 201 (БПЛА + NDVI).
- **L3 (Р3):** GEA / DeLaval / Lely impact санкциями; частичное импортозамещение (Лобня 2026, 4 млрд ₽); Connectome.ai (Сколково); **Holstein-bias** = architecture asymmetry для local пород РФ explicit.
- **L4 (Р4):** X5 «Перекрёсток» ML с 2020 (200 факторов); Магнит F&R in-house с 2025; РСХБ «Своё Фермерство» (10 000 партнёров). Sber GigaChat «сдал» экзамен в КубГАУ — **заявлено**, production-внедрений нет.
- **Р4-bis среда:** John Deere remote-brick Мелитополь 2022; Climate FieldView выход из РФ 2022 (главная иллюстрация политического риска); Starlink запрет апрель 2026; госпрограмма «Цифровое сельское хозяйство» 2019-2024 цель удвоения производительности **не достигнута** (АПК в 2024 −3,2%); «АПК будущего» 2026-2030.
- **Anchor s33** (Р4-bis): **РФ-АПК-AI 2026 summary table** — что работает (X5, Магнит), что отстаёт (поле, робот), что под санкционным риском (GEA, DeLaval), какие есть отечественные альтернативы (Cognitive Pilot, ИТЭЛМА, ExactFarming, Connectome.ai). Это **anchor для exam recall**, не дублирует материал.

**Главный РФ-урок:** **AI-зависимость от импортного AI-стека = политический риск; российский опыт после 2022 — natural experiment, что бывает, когда импортный AI-стек отключается**. **Главные иллюстрации этого урока — Мелитопольский кейс + Climate FieldView выход**, не Cognitive Pilot vs ИТЭЛМА (это другая история — architecture choice CV vs sensor-fusion).

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
- **Tech acronyms с RU расшифровкой при первом упоминании:** CV (компьютерное зрение), NDVI (индекс растительности), RTK (kinematic GNSS-коррекция), SAR (радар синтезированной апертуры), CRISPR, ML, LLM, RAG (генерация с поиском), bp / basis-points (базисные пункты), MRV (Measurement-Reporting-Verification).
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

## Slide-budget превью (для Phase 5)

- **Total ~33-36 слайдов** (+1-2 за счёт нового Р4-bis и pseudo-flow hedge); media-rich **22-24** (63-67%, comfortable над ≥50%).
- **Section dividers:** 7 (Р0-Р5 + Р4-bis); cover + lecture-map + Q&A: 3; content: ~23-26; pacing ~2-2.5 мин/content slide.
- **Lec-N-1 pattern compliance:** match lec-09 (cover + lecture-map + section dividers + dedicated Q&A; top progress bar только на dividers + cover; hero on s01 + s39).
- **Schema-readability checklist:** для лестницы keystone (s02), Cognitive Pilot vs ИТЭЛМА CV vs sensor-fusion-AI (s16), «как агент делает hedge» pseudo-flow (s25), РФ-сводка (s33), 5 критериев (s36), career-map (s37) — обязательно designer + critic pass.

---

## Провалы, ограничения и альтернативы (ENFORCED — ≥30% содержания)

- **Документированные провалы ИИ + выученные уроки:** 11 strict-in failure блоков (F1-F11 в разделах + connectivity + vendor lock-in в Р4-bis).
- **Фундаментальные ограничения / риски:** open-environment vs closed-loop (vertical farming); закон термодинамики vs ML; threshold accuracy ≠ deployment readiness; cloud-first для off-grid = архитектурная ошибка; vendor lock-in = политический риск.
- **Критерии «здесь ИИ не нужен / не применим»:** 5 основных в Р5.2 (AP1, AP3, AP4, AP6, AP7) + 3 inline в Р4-bis (AP2a architecture choice, AP2b genuine не-AI, AP5 cloud-first off-grid).
- **Более правильные альтернативные инструменты:** для каждого критерия указана альтернатива (sensor-fusion AI / mechanical weeders / RAG-grounded / edge-AI / open-source hardware / direct soil sampling).
- **Бюджет:** **34 из 70 мин active = 48.6%** strict-in (см. failure-bucket budget table). Comfortable margin над ≥30%.

---

## Assessment

LO5 («сформулировать критерии когда AI не применим») покрывается всеми failure-блоками + явным сводом в Р5.2. LO1a (Remember лестницы + tools) — Р1-Р5. LO1b (Apply adoption направления) — каждый L-уровень. LO2 (критическая оценка вендор-claim) — каждый failure-блок (Monarch, Plantix, vertical farming, Cognitive Pilot vs ИТЭЛМА).

Семинар sem-10 (отдельная задача, не в scope plan-v2): рекомендуемый case study на одном failure-блоке (Monarch demo-vs-production audit; или Cognitive Pilot vs ИТЭЛМА architecture-choice pre-purchase verification checklist).

---

## Changes vs v1

| # | P-уровень | Fix | Location |
|---|---|---|---|
| 1 | P1-1 | LO1 разбит на LO1a (Remember) + LO1b (Apply); итого 4 LO | Learning Objectives |
| 2 | P1-2 | Раздел 5 (14 мин, 8 sub-сек) restructured → Р4-bis (8 мин среда) + Р5 (6 мин L5+5 критериев+payoff); distribution math = 5+14+15+12+10+8+6 = 70 мин + 5 buffer + 10 Q&A = 85 мин full session | Outline structure |
| 3 | P1-3 | Vertical farming consolidated в 1 deep dive (5 мин) в Р1; F6 удалён из Р2; bridge Р1→Р2 reformulated | Р1 / Р2 outline |
| 4 | P1-4 | Р3 расширен до 12 мин; Holstein-bias выделен как separate anti-hype lesson; architecture asymmetry для local пород РФ explicit | Р3 outline + anti-AI |
| 5 | P1-5 | Hook primary → B (Plenty Compton split-frame failure-first); Hook A (See & Spray) перенесён в Р1 как opening working case | Р0 + Р1 |
| 6 | P1-6 | Cognitive Pilot vs ИТЭЛМА reframed как «CV-AI vs sensor-fusion-AI architecture choice within AI domain»; AP2 split на AP2a (architecture) + AP2b (genuine не-AI); РФ-главный урок политического риска иллюстрируется Мелитополь + Climate FieldView, не ИТЭЛМА | Р2 / anti-AI критерии / РФ-блок |
| 7 | P0-1 reader | Closed-loop operational definition в Cornerstone #2 + inline gloss при первом упоминании | Keystone section |
| 8 | P0-3 reader | Inline glossary 5 jargon terms (agentic, basis-points, hedge slippage, scope-3, AI-MRV) в Р4 при первом упоминании | Р4 outline |
| 9 | P2-1 | AP6+AP7 в основной пятёрке Р5 (заменили AP2 + AP5 которые ушли в Р4-bis inline) | Anti-AI критерии table |
| 10 | P2-2 | Cornerstone → anti-AI mapping таблица explicit | Cornerstone → AP mapping section |
| 11 | P2-3 | Q&A budget consistency: 75 мин content + 10 мин Q&A = 85 мин full session | Метаданные |
| 12 | P2-4 | Misattribution warnings — отдельный раздел (Indigo Ag, Tract, Verra scope, Saga UV-C ≠ harvest, РСХБ vapor risk) | Misattribution warnings section |
| 13 | P2-5 | Hero s39 = Carbon Robotics LaserWeeder G2 primary; Cargill BIG AI Award fallback; фотомонтаж reject | Hero images plan |
| 14 | P3 typos | «berlapping» → «overlapping»; «Bra режима» → «Бренд режима ≠ название бренда»; «plodовощная» → «плодоовощная»; «urожайность» → «урожайность» | Prerequisites / L4 / Р4 RU / L1 |
| 15 | reader P1-2 | F1 ToBRFV расшифровано (Tomato Brown Rugose Fruit Virus = томатный коричневый шершавый плодовый вирус); «closed-loop ↑ blast radius» explained operationally | Р1 F1 vertical farming |
| 16 | reader P1-3 | Cognitive Pilot vs ИТЭЛМА — explicit «разные функции» (где я vs что я вижу) | Р2 Russian context |
| 17 | reader P1-4 | РФ-сводка anchor table в Р4-bis s33 для exam recall (не дублирует material) | Media plan + РФ-блок |
| 18 | reader P1-5 | F2 ChatGPT context: research finding (Nature Food West/Williams 2024), 184 questions, GPT-3.5/4 + Bard; controlled experiment | Р1 F2 |
| 19 | reader P1-7 | «Controllability» определена operationally в keystone section | Keystone |
| 20 | reader P2-1 | DeLaval 99.8% attachment rate расшифровано operationally | Р3 working cases |
| 21 | reader P2-4 | Plantix 85-90% accuracy source explicit: self-reported Plantix (Frontiers 2020), не independent | Р1 F3 |
| 22 | reader P2-6 | Saga 20% UK = UV-C night treatment, **не harvest** explicit | Р2 + Misattribution |
| 23 | reader P2-3 | РСХБ format: «заявлено N, подтверждённых метрик нет» | Р4 Russian context |
| 24 | RU-canonical | «supply chain» → «цепочка поставок» в названиях разделов и outline; «vendor lock-in» → «привязка к поставщику» при первом упоминании + английский в скобках | Outline structure + L4 |

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
- **Hannah Ritchie substack** — Vertical farming thermodynamic gap.
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
- **Frontiers in Plant Science** (2020) — Plantix accuracy self-report.
- **MDPI Sustainability** — LED vs sunlight energy gap analysis.

---

**Word count: ~3 900.**
**Cornerstone concepts: 7. Failure blocks: 11. Tools named: 50+. Strict-in: 48.6% (34/70 min active).**
**Sections: 7 (Р0, Р1, Р2, Р3, Р4, Р4-bis, Р5) + Q&A. Pacing math: 5+14+15+12+10+8+6 = 70 мин + 5 buffer + 10 Q&A = 85 мин full session.**

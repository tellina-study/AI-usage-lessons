---
part: 3
of: 4
parent: "chapter.md"
title: "Глава 16. Часть 3: Раздел 3 — Q2 метановая MRV + Раздел 4 — Q4 энергетический переход"
lecture_number: 16
length_words: ~8200
status: draft
version: v1
---

---
**Навигация:** [← Часть 1 (Введение + R0 + R1)](chapter.md) | [← Часть 2 (Раздел 2 — Q3)](chapter-part2.md) | **вы здесь** (R3 + R4) | [Часть 4 (R5 + Q&A + источники) →](chapter-part4.md)

---

## Оглавление (Часть 3)

- [§ Раздел 3. Q2 — метановая MRV: AI essential + единичная уязвимость](#-раздел-3-q2--метановая-mrv-ai-essential--единичная-уязвимость)
  - [§3.1. Возврат в data-rich квадрант, но физика разорвана](#31-возврат-в-data-rich-квадрант-но-физика-разорвана)
  - [§3.2. MethaneSAT: первый NGO-владелец спутника](#32-methanesat-первый-ngo-владелец-спутника)
  - [§3.3. MethaneSAT loss (20 июня 2025): единичная уязвимость в действии](#33-methanesat-loss-20-июня-2025-единичная-уязвимость-в-действии)
  - [§3.4. Постсателлитные игроки: Carbon Mapper, GHGSat, Bridger Photonics, SeekOps](#34-постсателлитные-игроки-carbon-mapper-ghgsat-bridger-photonics-seekops)
  - [§3.5. 4× discrepancy: industry vs регулятор](#35-4-discrepancy-industry-vs-регулятор)
  - [§3.6. Регуляторика как driver: EU 2024/1787 + EPA Subpart W](#36-регуляторика-как-driver-eu-20241787--epa-subpart-w)
  - [§3.7. Альтернатива: hand-held OGI + Picarro / LI-COR portable analyzer](#37-альтернатива-hand-held-ogi--picarro--li-cor-portable-analyzer)
  - [§3.8. Самопроверка по Q2](#38-самопроверка-по-q2)
- [§ Раздел 4. Q4 — энергетический переход: AI и физика struggle вместе](#-раздел-4-q4--энергетический-переход-ai-и-физика-struggle-вместе)
  - [§4.1. Самый честный квадрант](#41-самый-честный-квадрант)
  - [§4.2. Northern Lights CCS: 0,02% от needed scale](#42-northern-lights-ccs-002-от-needed-scale)
  - [§4.3. Fervo Energy EGS: 40× growth ceiling, IPO мая 2026 года](#43-fervo-energy-egs-40-growth-ceiling-ipo-мая-2026-года)
  - [§4.4. Провал 1: CCS 190× scale-up gap + AI long-horizon hallucination](#44-провал-1-ccs-190-scale-up-gap--ai-long-horizon-hallucination)
  - [§4.5. Провал 2: refinery plant-wide stagnation в Q4 frame](#45-провал-2-refinery-plant-wide-stagnation-в-q4-frame)
  - [§4.6. Альтернатива: physics simulators + SIS (приборные системы безопасности)](#46-альтернатива-physics-simulators--sis-приборные-системы-безопасности)
  - [§4.7. Самопроверка по Q4](#47-самопроверка-по-q4)

## § Раздел 3. Q2 — метановая MRV: AI essential + единичная уязвимость

<!-- for-slide-s20 -->

### §3.1. Возврат в data-rich квадрант, но физика разорвана

[for-slide-s21]

Q2 — это самый необычный квадрант на keystone-матрице. Доступность данных — **высокая**: спутники GHGSat собирают терабайты гиперспектрального изображения в день; самолёты Bridger Photonics с Gas Mapping LiDAR делают сотни тысяч измерений за один полётный сезон; ручные OGI-камеры на нефтепромыслах генерируют десятки тысяч кадров. **Физика — частично известная**: атмосферная физика метана хорошо описана для отдельной модальности (например, для гиперспектрального спутникового измерения один источник); **слияние нескольких сенсоров** (англ. **multi-sensor fusion** — слияние данных от разных типов измерений) и **атрибуция малой утечки к конкретному источнику** в сложной орографии — открытая ML-задача.

**Почему AI essential в Q2.** Классической **physics-based** методики, которая бы взяла наблюдения 4 типов (спутник, самолёт, дрон, ручная камера) и **слила их в одну согласованную оценку утечки на конкретном устье скважины** — не существует. Каждая модальность имеет свои systematic biases:

- **Спутник** видит широкое поле, но малые источники (<100 кг/час) теряются в шуме атмосферы.
- **Самолёт + LiDAR** даёт лучшее разрешение, но **дорого** для постоянного мониторинга всей площади бассейна.
- **Дрон** видит близко, но **локально** — нужны сотни полётов для покрытия одного нефтепромысла.
- **Ручная OGI-камера** — самая точная для локализации конкретного клапана, но **не quantifies** утечку без отдельного measurement.

Чтобы построить **integrated emissions inventory** — надо использовать **все четыре модальности и AI для их слияния**. Это и есть «AI essential» в Q2: альтернативы (только классическая физика) нет.

**Но единичная уязвимость.** Когда **AI essential**, и оператор полагается на один спутник как primary data source — что произойдёт, если спутник потеряют? Этот сюжет уже разыгрался в Q2 в реальном времени: **MethaneSAT, флагман методологии NGO-managed мониторинга, потерян 20 июня 2025 года** через **~15,5 месяцев после запуска** (запуск 4 марта 2024, объявление о потере связи 20 июня 2025). Это центральное событие Раздела 3, и мы разберём его в деталях.

**LO mapping для Раздела 3.** Раздел работает на LO1 (когда применять — Q2 как **essential** случай), LO2 (когда отказаться — OGMP Level 5 + custody transfer), LO3 (альтернатива — OGI + portable analyzers + LDAR programmes), LO7 (этика и регуляция — EU 2024/1787 + EPA Subpart W; 4× discrepancy crisis между industry и регулятором).

### §3.2. MethaneSAT: первый NGO-владелец спутника

[for-slide-s22]

**MethaneSAT** — спутник для мониторинга метана, разработанный и владевший NGO **Environmental Defense Fund (EDF)** в партнёрстве с **Harvard University Smithsonian Astrophysical Observatory** и **New Zealand Space Agency**. Запущен **4 марта 2024 года** на ракете SpaceX Falcon 9. Бюджет миссии — порядка $88 миллионов; пять лет дизайн-life. **Первый в истории спутник, владельцем которого является экологическая некоммерческая организация**.

**Что MethaneSAT отличало от других спутников.**

- **Wide-area coverage** — поле зрения примерно 200 × 200 км, что покрывает крупные нефтегазовые бассейны за один проход.
- **Высокая точность** — порог детекции порядка **500 кг/ч** при идеализированных условиях (низкая облачность, минимальный ветер); в реальности порог выше.
- **Open data policy** — все данные публиковались open access через **Google Earth Engine** (партнёрство с Google объявлено в 2021 году), что отличало MethaneSAT от commercial спутников типа GHGSat.
- **Mission design** — explicit фокус на нефтегазовом метане (90% emissions), не на широком GHG-мониторинге.

**Первый flagship результат — Пермский бассейн.** В 2024 году MethaneSAT измерил эмиссии метана в Пермском бассейне (США) и опубликовал результат: **примерно 410 тонн метана в час**, что соответствует ~3,6 миллионам тонн в год; **на ~50% выше официальной оценки EPA** для этого региона [24]. Дополнительные результаты — методановая интенсивность (англ. **methane intensity** — % метана, который теряется из добытого газа) **Нью-Мексико 1,2% vs Техас 3,1%**: пятикратный разрыв между двумя соседними штатами одного бассейна. Нью-Мексико ввёл регуляцию метана в 2021 году (требование 98% gas capture к концу 2026 года); Техас — нет. **Регуляция работает**, и MethaneSAT её количественно зафиксировал.

**Что MethaneSAT публиковал к моменту потери.**

- **~2 000 data files** через Google Earth Engine.
- **180+ scenes** конкретных нефтегазовых бассейнов.
- **10 научных публикаций** в рецензируемых журналах.

**Strategic implications для регуляторики.** EU Methane Regulation 2024/1787 (август 2024) явно разрешила использование **satellite measurements** как primary data source для **import обязательств** ЕС. EPA Subpart W в мае 2024 — аналогично разрешил satellite quantification как **OGI alternative**. Это создавало **режим, в котором MethaneSAT (и подобные спутники) становились центральной инфраструктурой compliance**. И именно поэтому потеря MethaneSAT — это не «один satellite mishap», это **regulatory infrastructure crisis**.

**Технологический стек MethaneSAT — что внутри.** Помимо самого спутника, MethaneSAT mission включала **четыре слоя AI-обработки**:

1. **Atmospheric retrieval** — преобразование исходных спектральных данных в оценку концентрации метана в каждом пикселе. Это **physics-based конвейер** с ML-augmentation для отсева облаков и аэрозольной коррекции.
2. **Plume detection** — идентификация регионов с anomalously высокой концентрацией метана. ML-классификатор, обученный на synthetic plume training set + real-world calibration campaigns.
3. **Emission quantification** — преобразование observed plume geometry в оценку source strength (тонн/час). **Inverse atmospheric modelling** с ML-acceleration; принципиально сложная задача из-за wind variance и ground reflection.
4. **Source attribution** — связывание detected plume с конкретным operational asset. Использует **dense Permian basin facility maps** + ML-based matching. Это самый AI-heavy слой; он же — самый ошибкоёмкий.

Когда MethaneSAT был потерян 20 июня 2025 года — **все 4 слоя стали бесполезны на новых данных**. Уже опубликованные 2 000+ data files остаются ценным datasets для retrospective analysis, валидации других спутников, академических исследований. Но **forward-looking monitoring** требует **новой satellite mission**, что — minimum 2–3 года lead time от commitment до launch.

### §3.3. MethaneSAT loss (20 июня 2025): единичная уязвимость в действии

[for-slide-s23]

**20 июня 2025 года команда MethaneSAT объявила потерю связи со спутником.** Через **~15,5 месяцев после запуска** (4 марта 2024 — 20 июня 2025) — что составляет примерно **~26% от designed lifetime** (5-летняя проектная миссия). Конкретная причина потери — публично детали не объявлены; в обновлении проекта команда указывает на «spacecraft anomaly».

**Чему этот провал учит — четыре фундаментальных урока.**

**Первый — single-satellite mission = catastrophic single point of failure для regulatory MRV infrastructure.** Когда EU Methane Regulation 2024/1787 предусматривает использование **satellite measurements** как accepted data source — и primary global satellite NGO-owned data source потерян — что делать с этой data infrastructure? Ответ к концу 2025 года: **scramble к alternative data sources** (Carbon Mapper Tanager-1 запущен 16 августа 2024, GHGSat constellation 13 спутников к середине 2025). Но **resilience matters from day one**: проектировать MRV infrastructure на одном спутнике — структурная ошибка.

**Второй — даже с успешным запуском и хорошими данными первого года hardware reliability — fundamental constraint.** MethaneSAT работал отлично 15,5 месяцев. Это не «технология провалилась»; это «спутник в космосе — это hardware с конечной reliability». Любой satellite mission имеет non-zero probability of failure, и для critical infrastructure нужно **constellation model** (multiple redundant satellites), не **single mission**.

**Третий — Regulatory enforcement не может опираться на 1 спутник.** EU regulator после MethaneSAT loss должен либо (a) принять GHGSat constellation как backup, (b) разрешить ground-only verification через OGI + portable analyzers (откатиться к Level 5 OGMP), либо (c) допустить delay в enforcement. На момент написания (май 2026) официальная позиция EU — **a + b combination**: regulator принимает GHGSat данные с осторожностью, и **приоритизирует ground OGI campaigns** для compliance. Это **усиливает позицию ground OGI** как альтернативного инструмента и **снижает зависимость от satellite AI MRV**.

**Четвёртый — AI без stable upstream data source не работает.** Это самый глубокий урок. MethaneSAT использовал AI для downstream processing (atmospheric retrieval, plume detection, emission quantification). Когда **upstream sensor stream исчезает** — все downstream ML-модели становятся бесполезны на новых данных. То же самое случилось бы при потере любой ключевой сенсорной модальности: AI зависит от data stability в источнике. Это применимо за пределами satellite MRV: ML-модели на сенсорах в производственной автоматизации, ML-модели на медицинских изображениях, ML-модели на video feeds — **все они дискредитируются при потере upstream sensor**. AI — это **слой над данными**, не **источник данных**.

**Какая фраза часто звучит в industry conversations.** «Если MethaneSAT — это $88 млн на 15,5 месяцев работы — это **~$5,7 миллионов в месяц** (vs предполагалось ~$1,5 млн/мес при 5-летнем lifetime, что и обосновывало миссию). На той же сумме можно было профинансировать год intensive OGI campaigns на 10 крупнейших Пермских операторах + Bridger Photonics aerial campaign + 100 SeekOps drone missions». Это **upper bound on cost effectiveness** для NGO-funded environmental monitoring; и тем фактом, что MethaneSAT всё равно был запущен (под предположением 5-year lifetime), показывает, что **strategic value мониторинга на global scale** перевешивает per-month cost calculus. Но при reduced lifetime — этот расчёт меняется драматически: **realized cost per month вырос в ~4×**.

**Что делать после MethaneSAT.** К концу 2025 года и в течение 2026 года в индустрии разворачиваются параллельные направления mitigation:

1. **Carbon Mapper Tanager-1 ускоренное commissioning** — full operations к началу 2026 (forward от planned mid-2026).
2. **GHGSat constellation расширение** — Canadian operator коммерческий, но рассматривает расширение public access tier.
3. **Bridger Photonics expansion regional campaigns** — больше aerial coverage в Пермском бассейне и Marcellus.
4. **EU 2024/1787 enforcement флексибилити** — регулятор принимает Level 4 (component quantification) как accepted compliance вместо Level 5 (direct measurement), пока satellite infrastructure восстанавливается.
5. **Planned MethaneSAT-2 successor mission** — EDF + partners объявили intention в Q4 2025, но funding и timeline неопределённы [VFY-day-of].

Это **typical pattern industrial AI infrastructure failure recovery** — никто single replacement; **portfolio of alternatives** покрывает gap. Урок для студента: при проектировании critical AI infrastructure всегда планировать **graceful degradation path** в случае primary system failure.

### §3.4. Постсателлитные игроки: Carbon Mapper, GHGSat, Bridger Photonics, SeekOps

[for-slide-s24]

**Carbon Mapper Tanager-1.** Карбоновый mapping satellite от коалиции **Planet Labs + NASA Jet Propulsion Laboratory + Carbon Mapper Inc.** (NGO). Запущен **16 августа 2024 года**, full operations summer 2025. Facility-level detection — то есть способный идентифицировать утечки на уровне отдельной установки (компрессорная станция, отдельный wellpad). Tanager-1 — **первый из планируемой constellation Tanager**.

**GHGSat (Канада).** Коммерческое созвездие из **13 спутников к середине 2025 года** (12 cubesats к началу 2024 + Vanguard в 2025; ранее планы анонсировались до 16 к концу 2025, но фактический запуск отстал от плана) [25]. **Разрешение 25 метров** — самое детальное среди коммерческих метановых спутников. Customers — операторы в Permian, Marcellus, Alberta; страховые компании; регуляторы. GHGSat — **commercial paid service**: оператор платит за inspection своих площадок, в отличие от MethaneSAT (open data) и Carbon Mapper (mixed model). Это **более устойчивая business model** для long-term operation.

**Bridger Photonics.** Американская компания (Бозман, Монтана), aircraft-based **Gas Mapping LiDAR**. Самолёт пролетает над нефтепромыслом на низкой высоте; LiDAR-сенсор измеряет концентрацию метана в каждой точке трассы. Согласно валидационной кампании British Columbia LDAR, **aerial measurements 4× более точные**, чем ground OGI survey на тех же сайтах [26]. Customers — ExxonMobil, ConocoPhillips, EOG Resources, Pioneer (после слияния — часть ExxonMobil). Bridger — **flagship aerial provider** в США.

**SeekOps.** Drone-based methane detection. Используется в midstream applications (compressor stations, газораспределительные сети) и для gas utilities (городское газоснабжение). Customers — TC Energy, ENGIE, gas utilities. Дроны — **самый дешёвый способ** охватить тонко-распределённую инфраструктуру (длинные трубопроводы, города), но **локальный охват** ограничивает применимость.

**Project Canary.** Methane analytics + ESG-рейтинги. Не сенсорный поставщик как таковой; агрегирует данные от других источников + добавляет сертификационный подход для операторов. Это пример **многослойной MRV-экосистемы**: сенсоры → ML → analytics → ratings → ESG-инвесторы.

**Сравнительная таблица сенсорных модальностей Q2.**

| Модальность | Разрешение | Cost per coverage | Применение |
|---|---|---|---|
| MethaneSAT (был) | ~200×200 км сцены | Низкое (open data) | Wide-area регуляторный исходный уровень |
| Carbon Mapper Tanager-1 | Facility-level | Средние (mixed) | Facility-level inventory |
| GHGSat constellation | 25 м | Среднее (commercial) | Operator-paid inspections |
| Bridger Photonics aerial | Sub-meter (LiDAR) | Среднее-высокое | High-precision pre-regulatory campaigns |
| SeekOps drone | Sub-meter | Низкое per site | Midstream + utility |
| Hand-held OGI | Sub-meter | Лоу per inspection | Compliance verification |
| Picarro / LI-COR portable | Point measurement | Лоу per point | Quantification ground truth |

**Что эта таблица показывает.** Q2 — это **стек нескольких модальностей**, а не «AI заменяет OGI». Эффективная MRV-программа комбинирует спутник (wide-area исходный уровень) + авиа (high-precision региональные кампании) + дрон (покрытие midstream) + наземный OGI (compliance и локализация) + переносной анализатор (эталонная разметка для количественной оценки). AI — это **слой fusion + интерпретации поверх всех модальностей**. Когда вендор продаёт «AI MRV solution» — спросить: **какие модальности он покрывает?** Single-modality «AI MRV» — это маркетинговая фраза.

### §3.5. 4× discrepancy: industry vs регулятор

[for-slide-s25]

Это центральный numerical conflict Раздела 3.

**MethaneSAT измерения:** US oil&gas методан-эмиссии **примерно 15 миллионов тонн/год**.
**EPA Inventory (официальная оценка):** **примерно 4 миллиона тонн/год**.
**Фактор разрыва:** **примерно 4×.**

**Параллельная Stanford 2024 study.** Опубликована в Nature в марте 2024 года [27]. Aerial campaign на US O&G basins; результат — **>6 миллионов тонн/год** (точная цифра в paper — около 6,2–7,5 Mt в зависимости от basin coverage и aggregation method). Это **фактор ~2 outlier EPA Inventory** — не такой большой, как MethaneSAT factor 4, но всё равно значительный.

**Aerial vs OGI на одних и тех же sites.** Aerial measurements (Bridger Photonics) **4× выше**, чем ground OGI на тех же sites (British Columbia LDAR validation study) [28]. Это означает: **ground OGI системно underestimates** утечки в сравнении с aerial — потому что OGI inspector проходит сайт за 10–20 минут и **физически не видит intermittent emissions**, которые случаются за пределами этого окна.

**9-satellite single-blind тест 2024.** Опубликован в Atmospheric Measurement Techniques (Copernicus) [29]. **0 false positives** (хорошо), но **только 58% correctly identified**; **41 false negatives** (пропущенных реальных утечек). Это означает: даже когда AI MRV technology хорошо настроена и тестируется в контролируемых условиях с known ground truth, она пропускает почти половину реальных эмиссий.

**Что этот конфликт означает.**

**Industry reporting based на EPA emission factors systematically underestimates.** EPA emission factors — это статистические multipliers по типам оборудования (compressor, valve, pneumatic device); они были откалиброваны 10–20 лет назад и **не отражают реальный operational mix** современного нефтегазового производства. MethaneSAT и aerial campaigns показывают, что real-world эмиссии выше — потому что они захватывают **intermittent superemitters** (отдельные сайты, которые временно эмитируют огромное количество метана: проблема может быть в одной нерабочей задвижке).

**Satellite + aerial AI detection methods inconsistent друг с другом.** Stanford 2024 (factor 2) и MethaneSAT (factor 4) дают разные ответы. Это не «один прав, другой нет» — это **methodological calibration difference**. Aerial campaigns ограничены тем, в какие дни они летают (краткие campaign windows); satellite campaigns ограничены тем, что они **видят сверху** (cloud cover, ветер, time of day). Разные методы → разные ответы.

**No agreed ground truth.** Это самое главное. У industry, регулятора, NGO, академии — **нет согласованного методологического стандарта** для measuring US O&G methane эмиссии. Каждый игрок имеет свою методологию; результаты расходятся в 2–4 раза; и **regulatory enforcement** не может опереться на ни один результат как «единственно правильный».

**Выученный урок (фундаментальный для LO7).**

**AI MRV — promising technology, но не ready для contract enforcement без cross-validation protocols.** То есть — да, satellite + aerial + drone + OGI можно использовать как **complement** для друг друга, но **не как single source of truth**. EU Methane Reg 2024/1787 — explicit на это — требует **OGMP 2.0 Level 4/5**, что де-факто mandates **triangulation** (satellite + aerial + ground). Это не «избыток bureaucracy»; это **engineering necessity**, чтобы избежать factor 2–4 systematic errors.

**Regulator-Industry disagreement на factor 4 — это structural gap, не engineering polish.** Это означает, что любой «AI MRV solution», который обещает уверенно решить проблему в 2026 году, **upsells** возможности технологии. К 2030 году эта картина может улучшиться (новые методы калибровки, новые satellite constellations, новые ML methods для cross-modality fusion). Но **в моменте 2026 года** — фундаментальный методологический gap.

### §3.6. Регуляторика как driver: EU 2024/1787 + EPA Subpart W

[for-slide-s26]

Q2 — это не только технологическая ниша, но и **регуляторно-управляемый рынок**. Структура регуляции определяет, какие сенсорные модальности и AI-методы становятся mainstream.

**EU Methane Regulation (EU) 2024/1787 — adopted 4 августа 2024 года** [30].

Это **первый comprehensive EU методан-закон** для нефтегазовой индустрии. Применяется к **production internal to EU + imports** (LNG, ископаемый газ, нефть, уголь). Ключевые требования:

- **OGMP 2.0 Level 4/5 alignment.** Operators обязаны отчитываться по Level 4 (квантификация по компонентам) или Level 5 (прямое измерение).
- **LDAR programme deadline — 5 мая 2025 года.** Annual emissions reports — **5 августа 2025 года**.
- **Penalty — до 20% annual turnover.** Для major majors (Shell, TotalEnergies) с EU оборотом — это **multi-billion EUR exposure**.
- **Operators обязаны 4×/год survey + repair leaks в течение 5–15 рабочих дней.**
- **Imports**: к 2027 году все imports газа в ЕС должны соответствовать EU methane intensity standards (≤0,2% по природному газу).

Это **самая жёсткая в мире методан-регуляция** на момент 2026 года. EU operator с пропущенной утечкой или непредставленным отчётом рискует штрафом, который может **превышать прибыль от добычи**.

**US EPA Subpart W final rule — 6 мая 2024 года.**

- **Allows satellite quantification** как primary data source для отчётности.
- **«Other large release events» — новая category** для intermittent superemitters.
- **September 2025 — Trump administration proposal**: EPA опубликовала proposed rule с delay Subpart W effective date **до 2034 года** [31]. Это **критический политический контекст** — Trump admin 2025+ ведёт review EPA regulations, и Subpart W в зоне неопределённости. Финальный статус **зависит от EPA leadership** и judicial review challenges; на момент написания (май 2026) **status uncertain** [VFY-day-of].

**US IRA Waste Emissions Charge** — fees на методан-outliers, $1500/тонна CH₄ с tiered structure (планируется но statutory implementation [VFY-day-of]).

**Структурный driver Q2.**

EU regulation **жесткая, mandatory, с короткими deadlines** → создаёт спрос на AI MRV solutions, которые **работают сейчас**. Это благоприятная среда для GHGSat (commercial subscription), Bridger Photonics (campaign-based), Carbon Mapper (mixed funding). Это **толкает рынок AI MRV в Европе**.

US regulation **мягче, политически неопределённа, с возможными delays** → создаёт **wait-and-see** среду. Operators не торопятся инвестировать в AI MRV, если возможно, что federal mandate сдвинется на 5–10 лет. Это **тормозит рынок AI MRV в США**.

**Эта асимметрия — структурный сдвиг рынка.** EU становится первичным рынком для AI MRV; US — secondary. И эта структура **противоположна** общему AI-рынку: в LLM, ML platforms, datasets — US лидирует, Европа догоняет. В methane MRV — обратно, и **по причинам не технологическим, а регуляторным**.

### §3.7. Альтернатива: hand-held OGI + Picarro / LI-COR portable analyzer

[for-slide-s27]

Это **критический раздел для LO3** в Q2. Альтернатива AI MRV — это **ground-based direct measurement campaigns**. Mainstream tools:

**Hand-held OGI cameras:**

- **Teledyne FLIR GFx320** — flagship industry standard hand-held OGI camera. Видит углеводородные газы как «облако» через IR-фильтр; цифровая запись для аудита. Используется EPA Method 21, EU LDAR programmes.
- **Opgal EyeCGas** — конкурент FLIR; добавляет **quantitative OGI** (QOGI) capability — то есть не только «видит утечку», но и приближённо измеряет её расход. Точность QOGI обсуждается, но это шаг от чисто визуального обнаружения к quantification.
- **Rebellion Photonics (Honeywell)** — fixed hyperspectral imaging system. Размещается стационарно на объекте, постоянный мониторинг 24/7.

**Portable laser analyzers:**

- **Picarro G2210-i / G2401** — cavity ring-down spectroscopy, измеряет концентрации метана и других газов с лабораторной точностью на месте измерения. Часто используется как **ground truth для калибровки OGI и aerial measurements**.
- **LI-COR LI-7810** — конкурент Picarro; полевые методан-сенсоры для научных и regulatory measurements.

**Когда AI не нужен в Q2 — два критерия.**

**Критерий A — OGMP 2.0 Level 5 verification.** Level 5 требует **прямого измерения всех источников эмиссии на operational asset**. ML estimate не приемлем как primary methodology — нужна direct measurement. Поэтому Level 5 operators **обязаны** иметь Picarro / LI-COR + OGI campaigns; AI здесь — **дополнение** для prioritization (где OGI inspector должен искать), не **замена**.

**Критерий B — custody transfer metering.** Тот же критерий, что в Q1 §1.8 (критерий 3). Регуляторно требуется **mass flow meter класса точности 0,2%**. Methane content в газовом потоке измеряется через **gas chromatograph** или **direct sampling** + лабораторный анализ. AI estimate **не приемлем** для custody transfer.

**Почему ground OGI остаётся standard.**

1. **Compliance under EPA Method 21 / EU LDAR — accepted protocol.** Regulator audits ground OGI procedures; AI MRV — только начинает accept в специфических scenarios.
2. **Localization to specific source.** Satellite видит «утечка в этом квадратном километре»; OGI inspector видит «утечка из этой задвижки», что необходимо для **ремонта**.
3. **Independence from data infrastructure failures.** MethaneSAT loss не влияет на ground OGI campaigns; OGI работает с любым уровнем компьютеризации.

**Заметка о combination tools.** **Aerial Bridger Photonics + ground OGI** — это **рабочий гибрид**: aerial делает wide-area screen, OGI inspector проверяет flagged sites. Это **не "AI vs OGI", а "AI + OGI"**. Это применимая модель для тех operators, которые не могут позволить себе сами satellite constellation, но хотят больше, чем чистый ground OGI.

**Структурный взгляд на LDAR programmes.** EU LDAR требует операторов проводить survey **4×/год** + ремонт утечек в течение **5–15 рабочих дней**. Это **operational обязательство**, и расходы на LDAR программу для крупного European operator — порядка $5–15 миллионов в год на один production cluster. AI MRV может **снизить эти расходы**:

1. **Aerial campaigns раз в 2 месяца** (вместо 4×/год ground) + **targeted ground OGI** на flagged sites = **снижение human-hours** в 3–5 раз для тех же inspections.
2. **Satellite-based prioritization** — какие sites должны быть в next quarterly survey. Снижает random sampling overhead.
3. **ML-assisted leak attribution** — какое equipment leaking, какие репарации нужны. Снижает diagnostic time.

Net эффект — **AI снижает operational cost LDAR на 20–40%** для well-equipped operator. Это **substantial value**, который не «эффектен в маркетинговой картине», но **practical** для compliance budgets крупных IOC / NOC, обязанных по EU 2024/1787.

**Picarro / LI-COR — точечные измерения как ground truth.** Portable laser analyzers — это **the most accurate methane sensors в индустрии** (точность порядка 0.5 ppb для атмосферных концентраций; разовые measurements делаются за минуты). Они используются преимущественно как:

1. **Calibration tool** — Bridger Photonics aerial campaigns регулярно калибруются against Picarro ground reference измерения для validation.
2. **High-stakes individual measurements** — когда конкретная утечка должна быть quantified для regulatory submission (OGMP Level 5).
3. **Science campaigns** — Stanford 2024 study aerial + ground combination использовала Picarro / LI-COR как ground reference.

Их **не используют для wide-area mapping** — они слишком медленны (один measurement за минуты vs satellite один scan за seconds покрывая ~200×200 km). Это **canonical example complementary technologies**: satellite — wide-area, Picarro — point-precision. AI integration двух модальностей — это **value AI в Q2**.

### §3.8. Самопроверка по Q2

1. **Почему AI essential в Q2 (а не augmentation, как в Q3)?** Объясните через структуру данных и физики. Какая «классическая физика» в Q2 не работает?

2. **MethaneSAT loss — четыре фундаментальных урока.** Перечислите. Для каждого, как смягчить риск (mitigation strategy)?

3. **4× discrepancy MethaneSAT vs EPA — structural gap или AI ошибается?** Обоснуйте, почему это **structural** problem, а не «один метод плохой».

4. **EU 2024/1787 vs EPA Subpart W — почему рынок AI MRV развивается по-разному в Европе и США?** Структурный анализ.

5. **Когда custody transfer requires direct measurement vs когда AI estimate приемлем?** Используйте регуляторный context (EPA Subpart W, EU Methane Reg, OGMP Level 4 vs 5) для structural reading. Можно ли AI вообще участвовать в custody transfer chain — в каком role?

6. **Экономика LDAR-программы с AI vs без.** Возьмите гипотетического Пермского оператора с 50 production sites. Стоимость традиционного наземного OGI LDAR (4×/год обходов) — $5–10M/год. Что добавляет AI MRV-стек (авиа + спутник + ML-assisted attribution) к этой картине? Где ожидаемая экономия, где ожидаемый рост затрат?

---

## § Раздел 4. Q4 — энергетический переход: AI и физика struggle вместе

<!-- for-slide-s28 -->

### §4.1. Самый честный квадрант

[for-slide-s28]

Q4 — это **самый честный квадрант** keystone-матрицы. Не «AI revolution», не «AI essential», не «AI augmentation» — а **«AI и физика struggle вместе»**. И данных мало (единицы CCS-проектов в мире, единицы EGS-проектов), и физика на длинных горизонтах не закрыта (миграция облака CO₂ через подземные формации на 100 лет, geomechanics нагрева в EGS на 30+ лет). Эта структура заставляет читателя смотреть на Q4 без иллюзий: технологии **обещают много**, **достижения единичны**, и **scale gap огромен**.

**Connection to keystone-оси.** В Q1 у нас были данные и физика — AI работал как мультипликатор. В Q3 — физика была, данных не было — AI работал как augmentation поверх симуляторов. В Q2 — данные были, физики не было — AI работал как essential (потому что классической альтернативы не было). В Q4 — **обе стороны слабые**: данных мало, физика на длинных горизонтах не закрыта. И AI **не может компенсировать** обе слабости одновременно.

**Что это значит для развёртывания AI.**

1. **Hybrid AI + physics — единственный workable путь.** Чистый ML — галлюцинирует на out-of-distribution; чистая физика — слишком медленно для практической инженерии; hybrid (PINN, physics-constrained ML) — research-grade, но **направление развития**.
2. **Long-horizon prediction — структурно уязвимо.** Predicted plume migration на 100 лет — это область, где даже classical physics имеет large uncertainty bands; AI на top — ещё больше. Hallucination risk для LLM-based agents в long-horizon planning — реальный.
3. **Scale gap огромен.** CCS — 190× меньше, чем нужно к 2050 для climate targets. EGS — 40× меньше потенциала US. Эти gap'ы **не закрываются AI**, и AI не уменьшает их magnitude — он уменьшает **per-unit cost**, но не **total scale**.

### §4.2. Northern Lights CCS: 0,02% от needed scale

[for-slide-s29]

**Northern Lights** — joint venture между **Equinor, Shell, TotalEnergies**; commercial launch в 2024 году. CCS-инфраструктура для приёма CO₂ от европейских emitters (преимущественно cement plants, нефтехимия) и захоронения в северо-морских offshore-формациях около Эугарден (Норвегия). **Capacity Phase 1 — 1,5 миллиона тонн CO₂/год.**

**Применение AI в Northern Lights.**

- **Site selection** — где буровать injection wells, как оценить geological storage capacity. ML augments classical geomechanics; типичный claim в industry reviews — **10–15% improved monitoring accuracy** [32].
- **Plume migration monitoring** — 4D-сейсмика + ML для tracking облака CO₂ после injection. Это **active R&D area** в 2024–2026.
- **AI на этапе capture (upstream от CCS-инжекции)** — оптимизация absorber-процесса; **10–20% снижение затрат** на проектах Mongstad (Норвегия) и Boundary Dam (Канада) [33]. Отраслевой исходный уровень затрат — $80–120/тонна captured CO₂; AI снижает до $65–100/тонна.

**Базовая контекстуализация — 190× scale-up gap.**

- **IEA «World Energy Outlook» 2024:** CCUS must scale to **7,6 Gt CO₂/год** к 2050 для net-zero targets.
- **Current global CCS capacity ~40 Mt/год** (Northern Lights — 1,5 Mt + примерно 30 других проектов мира).
- **Required scale-up: ~190×.**
- **Northern Lights 1,5 Mt / IEA target 7,6 Gt = 0,02% needed scale.**

**Что эта цифра означает.** Northern Lights — flagship проект CCS в Европе. Если **190× scale-up** должен произойти к 2050 — это означает **строительство примерно 190 проектов того же класса, что Northern Lights, в течение 25 лет**. Это **физически и финансово возможно**, но требует:

- Капитальных инвестиций порядка **триллионов долларов**.
- Государственной поддержки (carbon pricing, mandates).
- Регуляторного согласования геологического захоронения в десятках юрисдикций.

И AI **не решает ни одну из этих структурных задач**. AI улучшает per-project cost effectiveness на 10–20% — но **не масштабирует индустрию**. Это критический момент честности: **AI — это catalyst, не silver bullet** для climate transition.

**Тип-сцеплённость с Q4 (низкие данные × низкая физическая определённость).** Northern Lights — канонический Q4-кейс по двум причинам, и обе вытекают непосредственно из определений осей keystone-матрицы.

- **Низкая доступность данных.** CO₂ plume migration на 100-летнем горизонте захоронения имеет **ограниченные операционные аналоги**. Ни один CCS-проект мира не работал 100 лет — самые старые injection wells (Sleipner, Норвегия, 1996+) дают ~30 лет данных; всё, что дальше, — extrapolation. ML-модель, обученная на доступном historical CCS, **структурно не может валидироваться** для 100-летнего горизонта.
- **Низкая определённость физики.** CO₂-поведение в реальной геологии включает **многофазовое течение** (СО₂-сверхкритический, brine, dissolved CO₂), **геохимические реакции** с пластом (carbonate dissolution / precipitation, изменяющие проницаемость во времени), **геомеханические эффекты** (induced seismicity, caprock integrity). Каждая компонента имеет parameter uncertainty **~30–50% от laboratory values** при переходе к реальной геологии. Это **не «нужно больше моделировать»**; это **fundamental epistemic uncertainty**.

Поэтому в Q4 рабочий паттерн — **hybrid AI + physics** (PINN / ROM-augmented Eclipse + senior reservoir engineer judgment) — единственный возможный подход. Чистый ML не работает (data scarcity); чистая физика не работает (компьютационно недоступно для уплотнённых scenario-runs). Это **противоположно** Q1, где обе оси высокие и AI — мультипликатор; и противоположно Q3, где данных мало, но физика хорошо описана, поэтому работают **physics-first + AI screening**.

### §4.3. Fervo Energy EGS: 40× growth ceiling, IPO мая 2026 года

[for-slide-s30]

**Fervo Energy** — американский стартап (основан 2017, штаб-квартира в Хьюстоне) в области **enhanced geothermal systems** (EGS — улучшенные геотермальные системы, способ извлечения тепла из горячих пород на 3–5 км глубине через гидравлический фрекинг). Использует **fiber optic** для distributed temperature sensing + AI для модели thermal performance.

**Cape Station Utah project.** $206 миллионов финансирования в июне 2025 года [VFY-day-of]; объект — flagship EGS plant. Driver спроса — **AI data centers тянут спрос на 24/7 clean power**. Renewable solar/wind — intermittent (нужны batteries для 24/7), nuclear — slow build, geothermal — **only renewable baseload**, доступный при сегодняшних технологиях. Поэтому EGS получает venture capital в темпе, какого не было 20 лет.

**Fervo IPO 12 мая 2026 года — цена размещения $27 за акцию, привлечено $1,89 млрд, оценка $7,7 млрд при IPO** [VFY-day-of] [34]. **Стек финансирования (база для оценки масштаба).** Fervo Series D в феврале 2024 закрыла $244M (led by Devon Energy); Series E в 2025 — $462M (для ускорения разработки и выхода на surging energy demand); IPO мая 2026 — upsized размещение $1,89B. Суммарно: **>$700M частного капитала** перед IPO + $1,89B при выходе на биржу. Pre-IPO valuation ~$6,5 млрд (по данным TechMarketBriefs); IPO зафиксировал **up-round до $7,7 млрд** (+18% к last private round) — это **не markdown**, типичный для многих clean-tech 2025–2026, а наоборот, **uplift**. В первый день торгов акции открылись около **$35** = **~30% first-day pop** относительно offering price, не trip-digit премия. Это **flagship moment** для геотермальной индустрии: первый крупный clean-tech EGS IPO с устойчивым up-round и значимой premium. Параллельно — **Eavor Technologies** (Канада) closed-loop geothermal, **Sage Geosystems** и **Quaise Energy** в early-stage EGS variants.

**Scale gap к needed capacity — отдельная база.** Fervo в pipeline на 2026 год имеет ~400 MWe реализуемой capacity; IEA 2050 geothermal target — **200+ GWe** для achieve net-zero pathway. Это значит **0,2% от needed scale** — даже успешный IPO не закрывает structural gap [VFY-day-of]. AI помогает per-well cost effectiveness; scale-up к 200 GWe требует tens of thousands of wells и десятилетий.

**Базовая контекстуализация — 40× growth ceiling.**

- **US geothermal potential (EGS):** ~150 GW (US Department of Energy и MIT studies).
- **Current US geothermal installed:** ~3,7 GW (преимущественно California, Nevada — традиционные hydrothermal).
- **Growth ceiling: ~40×** относительно текущей capacity.

**Что это означает.** 40× growth — это **engineering reality**, не «cap из политических соображений». 150 GW EGS — это **физический предел** при сегодняшней технологии drilling и thermal recovery. Если технология улучшится (например, через **deeper drilling** до 7–10 км как продвигают Quaise) — ceiling может вырасти. Но в моменте 2026 года — 40× growth potential, не «100×».

**Driver — AI data centers.** Это **двойной механизм**:

1. **AI workloads потребляют 24/7 stable power.** ML training jobs — это **continuous compute** часами/днями/неделями; renewable intermittency делает их дорогими (нужны batteries). Geothermal — baseload, stable 24/7.
2. **Hyperscalers ищут geothermal contracts.** Google, Microsoft, Meta объявили signed contracts с Fervo, Ormat (другой геотермальный provider). Это **новая клиентская база** для geothermal — не utilities, а **technology buyers**, готовые платить premium за clean baseload.

**Параллель с CCS Northern Lights.** В обоих случаях — AI как **catalyst per-unit cost effectiveness**, не как **scale solution**. Fervo использует AI для thermal performance modelling, optimal well placement, fracture network design. Это снижает per-well cost на 10–20%. Но **build 150 GW EGS** — задача десятилетий, и AI не делает её десятикратно быстрее.

**Fervo + AI data centers — закрытый цикл.** Особенный аспект Fervo IPO 2026 — это **cross-industry coupling**: AI hyperscalers (Google, Microsoft, Meta) подписывают **long-term power purchase agreements** с Fervo для своих data centers. Это:

1. **Снижает risk для Fervo** — guaranteed offtake означает финансируемые EGS-проекты.
2. **Снижает risk для hyperscalers** — diversified 24/7 clean baseload vs intermittent solar/wind с дорогими batteries.
3. **Создаёт прямой механизм AI → energy demand → clean energy investment**. Это **системный фидбэк-эффект**: чем больше AI workloads, тем больше геотермальная capacity expansion.

Этот цикл — **противоположен** classical fossil-fuel pattern, где AI исторически использовался для **повышения** добычи. В Fervo сценарии AI **создаёт спрос на clean energy** через свой own workload requirement. Это **inversion** roles AI в индустрии, и стоит наблюдать, как она разворачивается.

**Eavor, Sage Geosystems, Quaise — early-stage variants.** Помимо Fervo, в Q4 EGS пространстве есть несколько technology variants на раннем этапе коммерциализации:

- **Eavor Technologies** (Canada) — **closed-loop geothermal**: вместо открытого фрекинга используется замкнутый U-образный контур, движется тепло без поверхностной воды. Pilot project в Rotliegend Германия, $42M funding round в 2024 году.
- **Sage Geosystems** (US) — **pressurized closed-loop** + энергохранилище в подземных формациях, double-purpose play.
- **Quaise Energy** (US) — **millimeter-wave drilling** для достижения hot dry rock на 7–10 км глубине (vs Fervo 3–5 км). Технологически highest-risk, но **highest-potential**: 7–10 км даёт доступ к hot dry rock на 70–80% территории США, что радикально увеличивает theoretical capacity.

Все три — **early-stage**, и **не один из них** ещё не доказал commercial scalability в 2026 году. Они представляют **option value** для следующей волны Q4 development; в моменте — Fervo единственный с промышленно-развёрнутыми (production-grade) deployments.

**Тип-сцеплённость с Q4 (низкие данные × низкая физическая определённость).** Fervo EGS — Q4-кейс по двум причинам, симметричным к Northern Lights:

- **Низкая доступность данных.** Enhanced geothermal в hard rock на глубине 3–5 км — **новая технология промышленного масштаба**. Сlassical hydrothermal geothermal (Larderello Italy с 1904; Geysers California с 1960) даёт 50–100 years operational history, но это **другая физика** (естественные resvoirs vs искусственно созданные через фрекинг). Для Fervo-class EGS первые commercial wells пробурены 2021–2024 — горизонт «обычно поведёт» составляет 3–5 лет, а проектные lifetimes — 30+ лет. ML-модель thermal performance декomposition обучается на **очень ограниченном датасете** и **не валидирована** для 30-летнего горизонта.
- **Низкая определённость физики.** **Coupled THMC** (thermo-hydro-mechanical-chemical) coupled-physics включает: thermal extraction (как остывает rock), hydraulic flow (как движется вода через искусственные fractures), mechanical fracture network evolution (раскрытие/закрытие fractures под thermal/pressure stress во времени), chemical scaling (mineral precipitation в fractures, blocking flow). Каждая из этих компонент — **open research question**. Industry-standard simulator для full THMC coupled physics на geological time scales **не существует** в production-grade.

Поэтому Fervo использует **fiber optic distributed temperature sensing** как **operational ground truth** для краткосрочной (днях-месяцах) валидации; на длинных горизонтах применяется **hybrid AI + physics + senior reservoir engineer judgment**. AI здесь — **catalyst per-unit cost effectiveness** (–10–20% per well через optimal placement и fracture design), не **scale solution**. **Build 150 GW EGS** требует tens of thousands wells — задача десятилетий, и AI не делает её десятикратно быстрее.

### §4.4. Провал 1: CCS 190× scale-up gap + AI long-horizon hallucination

[for-slide-s31]

Возвращаемся к центральному провалу Q4: **190× scale-up gap для CCS — engineering reality vs policy targets**. Это **structural gap**, не «AI плохо работает».

**Что AI обещает в CCS — что не доставляет.**

**Обещает:** improved monitoring accuracy 10–15%; capture cost reduction 10–20%; faster site selection. **Доставляет:** да, эти цифры в pilots — реальные. **Не доставляет:** scale. AI не масштабирует индустрию с 40 Mt/год к 7,6 Gt/год; даже с 100% improvement per-unit cost эта цель остаётся 95× за пределами достижения.

**Долгосрочная hallucination AI для plume migration на 100 лет.**

CCS injection хранит CO₂ под землёй **на сотни-тысячи лет**. Mandatory regulatory requirement — **monitoring + verification** that CO₂ stays underground, **на десятилетия**. Critical question: где будет CO₂ облако через 50, 100, 500 лет?

- **Classical physics-based modelling** (Eclipse + geomechanics) — имеет large uncertainty bands на 100-летнем горизонте. **Это известный gap** — geomechanics на длинных временных шкалах слабо валидирована.
- **AI-based prediction миграции облака CO₂** — наложения на классическую физику. Может ускорить предварительный сценарный отбор. Но на out-of-distribution сценариях (например, землетрясение разрушает caprock в год 47) — **галлюцинирует**.
- **Hallucination risk в LLM-based agents для long-horizon planning** — Gartner 2027 prediction: **40% агентных AI-проектов будут отменены** из-за cost overruns и poor risk controls [35].

**Связь между галлюцинациями LLM и долгосрочным прогнозированием CCS.** LLM-агенты в промышленном развёртывании — например, агенты Aramco METABRAIN, отвечающие на вопросы инженеров — могут давать **уверенные ответы на вопросы вне распределения обучающих данных**. На вопрос «где будет облако CO₂ через 100 лет?» — LLM сгенерирует ответ. Инженер не сможет легко отличить галлюцинированный ответ от ответа, основанного на физике. **Это присущий риск LLM в задачах высокой ответственности**, и для долгосрочного мониторинга CCS — этот риск материален.

**Mitigation — три направления.**

1. **Hybrid AI + physics** (PINN или physics-constrained ML) — встраивает physical conservation laws в loss function. Снижает hallucination, но дороже compute.
2. **Human-in-the-loop mandatory** для long-horizon predictions. AI generates scenarios, **senior reservoir engineer + geomechanics expert** делает QC и финальный judgment call.
3. **Multi-method triangulation** — не полагаться на одну ML-модель; всегда verifier через independent physics simulator + analog basin (если есть) + multiple time-step monitoring data.

**Деep-dive в PINN — physics-informed neural networks.** PINN — класс нейронных сетей, в которые **встроены physical conservation laws** прямо в loss function. Если ML loss обычно — это MSE против training data, то PINN loss добавляет дополнительный term: «насколько модель удовлетворяет уравнениям массового баланса, энергетического баланса, etc.». В теории — это решает основную слабость ML surrogates: PINN **не нарушает физику** на extrapolation, потому что нарушение физики напрямую penalize в loss.

В практике 2026 года PINN — **research-grade**:

- **Scale challenges.** Industrial reservoir model имеет ~10⁶–10⁷ grid cells; PINN тренируется на 10⁴–10⁵ collocation points. Difference в 2–3 orders of magnitude означает, что PINN **scaled down** относительно industrial Eclipse / INTERSECT, и неясно, как scale up.
- **Convergence issues.** PINN training часто сложнее сходится, чем pure ML, из-за конкурирующих loss terms (data fit vs physics constraint).
- **Limited validation на industrial cases.** Большинство PINN papers — synthetic benchmark problems; production-scale CCS / reservoir validation — единичные.

К 2030 году PINN может стать mainstream для специфических applications (особенно CCS plume migration medium-horizon prediction). В моменте 2026 — **не commercial product**, и AI-vendor pitches «PINN-based reservoir modelling» стоит относить к академическому уровню готовности.

**Альтернативные подходы.** Помимо PINN, существуют несколько других направлений hybrid AI + physics:

- **Operator learning** (DeepONet, FNO — Fourier Neural Operator) — обучают neural network представлять **оператор** между функциями (e.g., от initial conditions к solution); компактнее чем full PINN.
- **Reduced-order modelling (ROM) с ML augmentation** — классический ROM (POD — proper orthogonal decomposition) с ML для capturing residual nonlinearities.
- **Differentiable physics simulators** (JAX-MD, PhiFlow) — физический симулятор, написанный в авто-дифференцируемом подходе, что позволяет использовать градиентную оптимизацию для обратных задач.

Это **active R&D fronts**, и инженер курса с глубоким интересом к Q4 / energy transition должен следить за этой литературой. Но коммерчески mature deployments в нефтегазе — **5–10 лет вперёд**, не сейчас.

**Зачем вообще нужен ML-суррогат в Q4 — три инженерных мотивации.**

Если pure-ML галлюцинирует на длинных горизонтах, а PINN ещё не industrial-grade — почему индустрия не использует **только** классический physics simulator? Ответ — **compute-time trade-off**, который определяет, что вообще возможно делать в инженерном рабочем процессе.

- **Time-to-result.** Eclipse / INTERSECT full-order simulation для basin-scale CCS plume migration на 100-летнем горизонте — **2–6 недель wall-clock time** на high-end HPC (высокопроизводительный кластер). ROM-augmented суррогат — **минуты до часов**. Difference в 3–4 orders of magnitude. Это меняет инженерный рабочий процесс от «один run в месяц» к «10 000 scenario sweeps в день». Без surrogate уровня speed-up **scenario analysis на длинных горизонтах структурно невозможен** — невозможно ответить на вопрос «как изменится plume через 100 лет при 50 разных climate-change сценариях».
- **Calibration cycle.** Калибровка reservoir simulator к historical production data (history matching) требует тысяч forward simulations. С Eclipse — недели; с ML surrogate — часы. Это позволяет calibrate в **near-real-time** при поступлении новых data, что критично для active reservoir management.
- **Uncertainty quantification.** Modern reservoir management требует **Monte Carlo runs** для characterization parameter uncertainty (geological heterogeneity, fluid PVT uncertainty, fracture network realisation). 1000+ samples × full-order simulator = **infeasible**. С surrogate — feasible.

**Конкретные академико-индустриальные коллаборации hybrid AI + physics в нефтегазе 2024–2026.**

Ниже — задокументированные исследовательские коллаборации с указанием уровня публичной верификации. **Специфический scope каждого «production deployment»** в нефтегазе для PINN/DeepONet/FNO в 2026 году **публично не подтверждён** (большинство — research-grade с press release уровня general partnership, не named deployment); поэтому каждый кейс приводится как «направление R&D», а не «развёрнут в эксплуатации».

- **Saudi Aramco + KAUST PINN research** — broad academic-industrial collaboration на reservoir modeling (PINNeik paper для seismic eikonal solution в открытом доступе; общая Aramco-KAUST broader research programme задокументирована). **Specific «Aramco PINN-based reservoir model production deployment» в публичных press releases не найден** [FACT-CHECK: public source pending]. Реальное направление: исследовательский pipeline для **carbonate reservoir modeling**; commercial-grade deployment не объявлен.
- **ExxonMobil + Princeton Carbon Mitigation Initiative** — задокументированная broader collaboration на CCS hub research (CMI annual reports 2021+). **Specific DeepONet для Permian CCS plume migration в публичных источниках не подтверждён** [FACT-CHECK: public source pending]. Реальное направление: общая академическая работа по CCS, без named deployment.
- **TotalEnergies + NVIDIA PINO (Physics-Informed Neural Operator)** — **верифицированная коллаборация**, представленная на **NVIDIA GTC25** (March 2025): применение PINO/Modulus framework к **CCUS modeling** (sub-surface CO₂ migration prediction). Конкретный scope — research-grade demo, не general production deployment, но является **citable example** реального industrial-academic hybrid AI + physics направления.

**Что эти примеры показывают студенту.** Все три — **направления R&D**, не **scale deployments**. Это **отдельный** урок: даже flagship industrial-academic коллаборации в hybrid AI + physics 2024-2026 года остаются на исследовательском уровне готовности. Любой vendor pitch уровня «PINN-based reservoir model в production» в 2026 году требует **publicly citable case study** — иначе это marketing.

**Trade-off, который должен знать студент.** Hybrid AI + physics — это **speed × accuracy × physical consistency** triangle, где можно выбрать только 2 из 3. Full-order Eclipse — accuracy + physical consistency, медленно. Pure ML surrogate — speed + accuracy на training distribution, теряет physical consistency на extrapolation. PINN / ROM-augmented — speed + physical consistency, но accuracy ограничена сложностью embedded physics. Нет «free lunch». Инженер должен **явно выбрать**, какие два угла важнее для конкретной задачи, и принять trade-off третьего.

### §4.5. Провал 2: refinery plant-wide stagnation в Q4 frame

[for-slide-s32]

Этот провал мы видели в §1.3 в Q1 frame (Aspen Mtell alert fatigue, plant-wide stagnation). Здесь мы переформулируем его в Q4 frame — как **multi-physics constraint, который AI не закрывает на длинных временных горизонтах**.

**Что refinery process control share с Q4.**

- **Multi-physics constraints:** mass + energy + reaction kinetics + corrosion. То же, что в CCS.
- **Long horizons:** НПЗ работает 40–50 лет; ML model decay 1–2 года. Тот же gap, что в CCS plume migration.
- **Edge cases:** при изменении feedstock, при equipment wear, при regulatory changes — ML surrogates **lose consistency**.

**Cross-link к Yokogawa Idemitsu.** Yokogawa в 2018 году объявила пилот plant-wide AI process control на одном из НПЗ Idemitsu в Японии. **Пилот тихо закрыт после 2018 года** [VFY-day-of]; в публичных материалах остались только single-column success stories. Это типичный паттерн: AI хорошо берёт **локальную оптимизацию** (один column, один heater), плохо берёт **многоюнитную координацию**, где multi-physics constraints (mass + energy + reaction + corrosion) ломают ML-суррогаты на edge cases.

**Применимость к Q4.**

CCS injection plant — это **многоюнитная инсталляция**: capture unit + transport pipeline + injection wells + monitoring wells. Координация этих компонентов на 30–50-летнем горизонте requires multi-physics coupling. AI **может** делать узкую оптимизацию (например, один injection well rate, один capture absorber). AI **не может** делать координированное plant-wide управление с multi-decade outlook.

То же касается Fervo EGS — каждое EGS-устройство имеет capture + thermal extraction + power generation; multi-physics; long horizons. AI работает в каждой компоненте; **интегрированное plant-wide развёртывание AI** структурно неполное.

**Выученный урок (фундаментальный для LO2).**

**Когда задача требует multi-physics coupling + long horizons + краевых случаев — развёртывание AI затрудняется фундаментально, не из-за нехватки обучающих данных.** Это не «больше данных решит проблему»; это **ограничение самой ML-методологии** — обобщение нейронных сетей хорошо работает в режиме интерполяции, плохо — в режиме экстраполяции, **очень плохо — в режиме multi-physics экстраполяции**.

### §4.6. Альтернатива: physics simulators + SIS (приборные системы безопасности)

[for-slide-s33]

Это **критический раздел для LO3** в Q4. Альтернатива AI в long-horizon CCS / refinery / EGS — это **classical physics-based engineering + deterministic safety systems**.

**Physics-based simulators для CCS.**

- **Eclipse / INTERSECT** с CCS modules — реservoir-scale CO₂ migration.
- **OpenFOAM** — CFD around injection wells, multi-phase flow.
- **Geomechanics packages** — Visage (SLB), Abaqus (Dassault), Plaxis — для stress analysis в caprock.
- **CMG GEM** — compositional simulator для variable mixture CO₂-impurities scenarios.

Эти tools используются для **regulatory submissions** under EU CCS Directive 2009/31/EC и параллельных US/Canada regulations. Регулятор требует **physics-traceable modeling**; AI surrogate **не accept** в этом capacity.

**Physics-based + classical APC для refinery.**

- **Honeywell Profit Controller** — modelling APC standard для US refineries.
- **AspenTech aspenONE** — APC integrated в process simulation.
- **Emerson DeltaV PredictPro** — embedded APC в DCS.

**Когда APC > ML.** APC — это model-based predictive control, **детерминированное и certifiable**. ML controller для plant-wide refinery operation requires **safety case** that ML не приведёт к exceedance процессных пределов. **Safety case для ML — структурно сложнее**, чем для APC, потому что APC поведение **prove-able**; ML — empirical.

**SIS — Safety Instrumented Systems.**

Это **deterministic safety logic**, сертифицированная под **IEC 61511 / ISA-84** на уровень SIL3 или SIL4. Применения:

- **Blowout preventer (BOP)** — закрытие устья скважины при выбросе.
- **Pressure relief valve (PRV)** — выпуск давления при exceedance limit.
- **Emergency shutdown (ESD) logic** — координированное отключение технологии при критическом событии.
- **Fire & gas detection** — детерминированное срабатывание при концентрации горючих/токсичных газов.

**ML не сертифицируется под IEC 61511 в текущем фрейме.** Probability of failure on demand (PFD) для ML-модели **не доказывается аналитически** так же, как для дискретной логики; в дискретной логике мы перечисляем все возможные states и докажем, что failure occurs только в specific conditions; для ML это невозможно (state space слишком большой). **Альтернатива:** physics-based redundancy + 3oo2 voting (три датчика, действие при согласии двух), периодические proof tests (квартальная проверка каждой safety функции), fail-safe design (при отказе системы — состояние safe state).

**Когда AI не нужен в Q4 — три критерия.**

**Критерий 1 — Safety-critical SIS (BOP / PRV / ESD logic).** SIL3/SIL4 mandatory.

**Критерий 2 — Long-horizon prediction beyond 10–20 лет.** ML галлюцинирует на out-of-distribution. Hybrid AI + physics — в research stage.

**Критерий 3 — Plant-wide multi-physics coupling.** Узкие циклы — OK для AI; координация через десятки units — структурно сложно. Альтернатива: classical APC + senior operator.

**Перекрёстная ссылка на Deepwater Horizon 2010.** Этот случай мы разбираем в Части 4 §5.5 как исторический якорь Q4 SIS-альтернатив. Ключевой вывод: **культура обхода тревог** + недостаточная подготовка операторов + сложная автоматизация = катастрофа. AI добавляет сложность; для компенсации нужны инвестиции в **подготовку операторов + управление тревогами** + **safety case engineering** — не только в модели.

**Federated learning + privacy-preserving ML — emerging альтернативный путь.** Это **research-grade** в нефтегазе, но потенциально важное направление. В нефтегазовой индустрии data часто не shared между операторами по конкурентным причинам — Aramco не делится Permian data с ExxonMobil, Газпром нефть не делится Ямал data с ЛУКОЙЛ. Это создаёт **fundamental gap**: ML models учатся на одном operator data, что limits generalization и precludes cross-operator learning.

**Federated learning** решает это: вместо sharing raw data, операторы share **model updates** (gradient steps), которые aggregated централизованно. Это позволяет collectively обучить model без раскрытия конкретной production data. **Differential privacy** добавляет noise к outputs для prevent reverse-engineering individual data points.

В нефтегазе федеративная архитектура применима для:

1. **Cross-operator failure prediction** — predicting equipment failures на основе fleet-wide patterns без sharing detailed equipment data.
2. **Methane MRV calibration** — multiple operators sharing calibration data без revealing competitive production details.
3. **Drilling automation** — sharing learned drilling patterns между operators без revealing specific drilling locations.

В 2026 году коммерческие развёртывания federated learning в нефтегазе **редки** — есть пилоты, но масштабного развёртывания ещё нет. Продемонстрировано в банкинге (Visa cross-bank fraud detection), здравоохранении (NIH multi-institutional medical imaging). К 2030 году federated learning может стать **основным паттерном** для межоператорского AI в нефтегазе, особенно для метановой MRV, где регулятор требует триангуляции. Для студента — направление, за которым стоит следить.

### §4.7. Самопроверка по Q4

1. **Почему Q4 — «самый честный» квадрант?** Объясните через структуру keystone-оси: что значит «AI и физика struggle вместе».

2. **CCS 190× scale-up gap — AI helping или AI not enough?** Обоснуйте позицию.

3. **Long-horizon hallucination в LLM agents — почему это структурная проблема, а не «добавим больше training data»?** Используйте concept extrapolation vs interpolation.

4. **Назовите 3 критерия «здесь AI не нужен в Q4»** и для каждого приведите альтернативный инструмент.

5. **Fervo Energy + AI data centers — закрытый цикл или transient hype?** Обсудите, является ли coupling между AI workloads и geothermal capacity expansion **structural feedback loop** или **временной артефакт** rapid LLM era. Используйте US current 3,7 GW vs 150 GW potential как контекст.

6. **Federated learning для cross-operator AI в нефтегазе — почему это становится релевантным именно сейчас?** Используйте EU 2024/1787 triangulation requirement и competitive data restrictions между операторами как контекст.

---

**[→ Часть 4 (Раздел 5 — Россия + cross-cutting + закрытие + Q&A backup + источники)](chapter-part4.md)**

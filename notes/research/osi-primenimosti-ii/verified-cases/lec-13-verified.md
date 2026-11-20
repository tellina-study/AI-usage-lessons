---
title: "Лекция 13 (logistics) — независимо верифицированные кейсы, внешние источники"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 13 — logistics: внешне верифицированные кейсы (2022–2026)

## Подход к поиску

Цель — не пересказать `library/lectures/lec-13/*`, а найти **новые или заново перепроверенные**
кейсы с явным исходом, числом, датой, именованным инструментом и настоящей проверяемой ссылкой.
Поиск вёлся по WebSearch (до исчерпания лимита сессии — 8 полных раундов, см. ниже) и затем
WebFetch по конкретным страницам (Wikipedia, пресс-релизы, деловая пресса, SEC-фильинги) —
инструмент с отдельным от WebSearch лимитом, которым удалось закрыть оставшиеся пробелы. Домены
поиска: складская робототехника (Amazon, Ocado-линия), автономная доставка (sidewalk-роботы,
дроны), автономный грузовой транспорт (highway trucking), freight-matching платформы, generative-AI
автоматизация брокериджа.

**Покрытие по годам — все пять лет (2022–2026) закрыты с обеих сторон (успех и провал)**, кроме
одного слабого места: **2023 на стороне успеха держится на одном кейсе низкой уверенности**
(Amazon Sequoia — точная дата анонса не подтверждена напрямую ни одним зафетченным источником,
только собственным знанием модели + вторичным упоминанием в Wikipedia-статье про Amazon Robotics
без даты). Это честно помечено `confidence: low` в строке, не замаскировано.

**Ограничение по инструменту.** WebSearch исчерпал лимит сессии на 14-м запросе (8 раундов по
1-8 запросов) — после этого момента добор шёл исключительно через WebFetch по угаданным/известным
URL (в основном Wikipedia), что сузило охват источников (не было возможности найти, например,
независимую проверку заявления Serve Robotics «99,8% успешных доставок» за пределами
цитирующего его NVIDIA-кейс-стади). Это не недостаток метода, а честно названный предел сессии.

## Качество источников — честная оценка

- **Сильные источники (несколько независимых изданий + первичные документы):** закрытие Convoy
  (CNBC, Forbes, GeekWire, CEO-memo), продажа 6 River Systems (The Robot Report + SEC-контекст),
  go-private Berkshire Grey (собственный 8-K SEC-фильинг + пресс-релиз), крах TuSimple (WSJ via
  Wikipedia-синтез, с конкретными цифрами из судебных документов), остановка Amazon Scout
  (Bloomberg, The Register, TechTimes, Euronews — независимо совпадают), сворачивание
  Walmart/DroneUp (SupplyChainBrain, Axios, DroneLife — совпадают), паузы Amazon Prime Air
  (несколько изданий + FAA-контекст), прекращение Wing в Канберре (решение австралийского
  федерального регулятора — первичный факт, не только пресс).
- **Средние источники (одно солидное издание или пресс-релиз компании, цифры внутренне
  непротиворечивы, но не аудированы третьей стороной):** Amazon DeepFleet/Sequoia/Proteus
  (собственные пресс-релизы Amazon — числа не аудированы независимо), Kodiak Robotics + Atlas
  Energy (пресс-релизы Kodiak + отраслевая пресса trucking, совпадают между собой), Aurora
  Innovation 250k миль без инцидентов (SEC-фильинг + пресс, но «без инцидентов» = собственное
  заявление компании, не независимый аудит), C.H. Robinson generative AI (пресс-релизы компании +
  Business Wire — цифры компании, непротиворечивы между двумя релизами с разницей в полгода),
  Gatik (Wikipedia-синтез первичных анонсов — отсутствие «документированных провалов» в статье не
  равно доказанному их отсутствию).
- **Слабые/vendor-sourced:** Serve Robotics «99,8% success rate» — это цифра из NVIDIA case study
  про собственного клиента, не независимый аудит; Amazon Sequoia — точная дата не подтверждена.
- **Общее наблюдение, совпадающее с предупреждением реестра (`reestr-reshenij-README.md` п.3):**
  индустрия logistics/AV сильно смещена в сторону **публикуемых vendor-пресс-релизов на стороне
  успеха** и **независимой деловой/регуляторной прессы на стороне провала** — то есть сам способ
  поиска структурно легче находит провалы с независимой верификацией, чем успехи. Это не повод
  farms занижать успехи искусственно, но повод не читать `confidence: medium` на успешных
  AI-метриках как «независимо аудировано».

## Итог: 12 успехов + 13 провалов (1 доп. запись — partial, не входит в счёт ни той, ни другой стороны) = 25 строк

---

## Успешные кейсы (outcome = success)

| case_name | year | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amazon Proteus — первый полностью автономный AMR на складах Amazon | 2022 | low | none | seconds-minutes | none | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Amazon_Robotics |
| Gatik — полностью безводительская средне-мильная доставка, PC Express/Loblaw, Brampton (Канада) | 2022 | low | none | hours-days | none | sensor-fusion | no | medium | not-applicable | success | medium | https://en.wikipedia.org/wiki/Gatik |
| Amazon Sequoia — автоматизированная система хранения/поиска, заявлено «на 75% быстрее» идентификация инвентаря | 2023 | low | none | seconds-minutes | none | hybrid | yes | low | not-applicable | success | low | https://en.wikipedia.org/wiki/Amazon_Robotics |
| C.H. Robinson — generative-AI автоматизация жизненного цикла фрахта (почтовые запросы цен/тендеры/аппойнтменты) | 2024 | moderate | none | seconds-minutes | none | foundation-model | yes | low | not-applicable | success | medium | https://www.businesswire.com/news/home/20241031448369/en/Using-Generative-AI-C.H.-Robinson-Has-Achieved-Automation-Across-the-Entire-Lifecycle-of-a-Freight-Shipment |
| Zipline — 1 000 000-я коммерческая дрон-доставка | 2024 | moderate | none | season-years | F-A | sensor-fusion | unclear | medium | not-applicable | success | high | https://www.cnbc.com/2024/04/19/autonomous-drone-startup-zipline-hits-1-million-deliveries.html |
| Kodiak Robotics + Atlas Energy — безводительские RoboTrucks, Permian Basin (проппант) | 2024–2025 | high | none | hours-days | none | sensor-fusion | no | catastrophic | not-applicable | success | medium | https://kodiak.ai/news/kodiak-delivers-customer-owned-autonomous-robotrucks-to-atlas |
| Amazon DeepFleet — generative-AI foundation model маршрутизации роботов, −10% travel time по 300+ FC | 2025 | low | none | seconds-minutes | none | foundation-model | yes | low | not-applicable | success | medium | https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model |
| Aurora Innovation — запуск безводительских грузовиков без человека в кабине, Dallas–Houston, 250 000+ миль без инцидентов | 2025–2026 | high | none | season-years | none | deep-learning | unclear | catastrophic | not-applicable | success | medium | https://finance.yahoo.com/news/aurora-innovation-touts-250k-incident-053545428.html |
| Starship Technologies — 9 000 000 кумулятивных доставок, 2 700 роботов, 270 локаций | 2025 | moderate | none | season-years | F-A | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Starship_Technologies |
| Serve Robotics — флот 2 000 роботов, крупнейшая сеть доставки по тротуарам в США | 2025 | moderate | none | season-years | F-A | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Serve_Robotics |
| Wing (Alphabet) — 1 000 000-я коммерческая дрон-доставка (в основном через Walmart) | 2026 | moderate | none | season-years | F-A | sensor-fusion | yes | medium | not-applicable | success | high | https://en.wikipedia.org/wiki/Wing_(company) |
| Nuro/Lucid/Uber — лицензирование Nuro Driver, обязательство на 35 000 автомобилей-робтакси | 2026 | high | none | season-years | F-A | sensor-fusion | not-applicable | unclear | not-applicable | partial | medium | https://www.ttnews.com/articles/uber-partners-lucid-nuro |

> Последняя строка (Nuro/Lucid/Uber) размечена `outcome: partial`, не `success` — сделка
> подписана и расширена (апрель 2026: 35 000 машин), но коммерческий запуск робтакси-сервиса на
> момент последнего найденного отчёта (Q1 2026) ещё не состоялся («later this year»): это бизнес-
> milestone, не подтверждённый эксплуатационный результат. Не входит в счёт 10+ успехов ниже.

**Счёт успехов: 11** (без учёта partial-строки Nuro/Lucid/Uber) — выше требуемого минимума 10.

---

## Провальные кейсы (outcome = failure)

| case_name | year | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Amazon Scout — робот доставки на тротуарах, программа закрыта («доставлял не быстрее человека») | 2022–2023 | moderate | U3 | season-years | F-A | sensor-fusion | not-applicable | low | no | failure | high | https://www.bloomberg.com/news/articles/2022-10-06/amazon-abandons-autonomous-home-delivery-robot-in-latest-cut |
| Nuro — уход из потребительской доставки, 2 раунда сокращений (20% в нояб. 2022, 30% в мае 2023) | 2022–2023 | unclear | none | season-years | F-A | sensor-fusion | not-applicable | low | no | failure | medium | https://en.wikipedia.org/wiki/Nuro |
| Convoy — цифровая freight-matching платформа, закрыта («unprecedented freight market collapse») | 2023 | unclear | unclear | season-years | F-B | classical-ml | not-applicable | high | mixed | failure | high | https://www.cnbc.com/2023/10/19/bezos-backed-freight-firm-convoy-shuts-down-read-ceo-memo-here.html |
| 6 River Systems — AMR-бизнес Shopify продан за $12,7М после покупки за $450М в 2019 | 2023 | unclear | unclear | season-years | F-B | hybrid | not-applicable | high | mixed | failure | high | https://www.therobotreport.com/shopify-suffers-huge-loss-on-6-river-systems-sale/ |
| Berkshire Grey — go-private с SoftBank по $1,40/акцию (~$375М), обвал от SPAC-оценки | 2023 | unclear | unclear | season-years | F-B | hybrid | not-applicable | high | mixed | failure | high | https://www.berkshiregrey.com/resources/press-release/berkshire-grey-enters-into-definitive-merger-agreement-with-softbank-group-for-go-private-transaction/ |
| TuSimple — обвинения в мошенничестве/передаче технологий, делистинг с Nasdaq, обвал на 96% от IPO | 2022–2024 | unclear | unclear | season-years | none | sensor-fusion | not-applicable | catastrophic | mixed | failure | high | https://en.wikipedia.org/wiki/TuSimple |
| Walmart / DroneUp — партнёрство по дрон-доставке свёрнуто (3 штата, авг. 2024), затем завершено полностью | 2024 | low | none | season-years | F-A | sensor-fusion | not-applicable | low | no | failure | high | https://www.axios.com/2024/08/16/walmart-drone-delivery-dallas-texas |
| Amazon Prime Air — столкновения дронов MK30 (сент./дек. 2024), добровольная пауза полётов в TX/AZ | 2024–2025 | high | U3 | seconds-minutes | F-C | sensor-fusion | no | medium | no | failure | high | https://www.ctol.digital/news/amazon-grounds-prime-air-drone-deliveries-after-crashes/ |
| Amazon — роботизированные склады не выполнили собственное обещание снизить травматизм вдвое | 2024 | unclear | unclear | season-years | F-B | hybrid | not-applicable | medium | no | failure | medium | https://www.nelp.org/app/uploads/2024/04/Amazons-Outsized-Role-5-1-24.pdf |
| Wing (Alphabet) — операции в Канберре закрыты после жалоб на шум и решения регулятора | 2019–2023 | low | none | season-years | F-A | sensor-fusion | not-applicable | low | yes | failure | high | https://en.wikipedia.org/wiki/Wing_(company) |
| Serve Robotics — столкновение робота-доставщика с пользователем мобильного скутера, Лос-Анджелес | 2025 | moderate | U3 | seconds-minutes | none | sensor-fusion | no | medium | no | failure | medium | https://en.wikipedia.org/wiki/Serve_Robotics |
| Starship Technologies — столкновение робота с автобусом, Таллин, до 9 пострадавших | 2026 | high | U3 | seconds-minutes | none | sensor-fusion | no | high | unclear | failure | medium | https://en.wikipedia.org/wiki/Starship_Technologies |
| PlusAI — второе по счёту SPAC-слияние (с Churchill Capital Corp IX) расторгнуто | 2026 | unclear | unclear | weeks-months | F-A | sensor-fusion | not-applicable | medium | yes | failure | high | https://www.freightwaves.com/news/plusai-spac-termination-churchill-capital-ix |

**Счёт провалов: 13** — выше требуемого минимума 10.

---

## Заметки по осям и расхождения с рамкой курса

1. **Гейт/обратимость — осмысленно применим только там, где есть единичное техническое решение в
   реальном времени.** Для бизнес-событий (банкротства, go-private сделки, SPAC-крахи) `axis4_gate`
   закономерно = `not-applicable` — сам вопрос «был ли гейт перед действием» не имеет смысла для
   решения совета директоров о продаже бизнеса. Это **не ошибка разметки**, а честная граница
   применимости Оси 4: она создавалась для операционных ИИ-решений, не для корпоративных финансовых
   событий — большая часть новых провальных кейсов в этой подборке именно такого рода (5 из 13:
   Convoy, 6 River Systems, Berkshire Grey, TuSimple-финансовая часть, PlusAI).
2. **Контрпример про «большой ИИ ненадёжен»/foundation-model gap: НЕ подтверждается новыми
   успешными кейсами.** DeepFleet (foundation-model) и C.H. Robinson (foundation-model/generative
   AI) в этой подборке — оба `outcome: success`, оба с низким/низко-средним blast radius и явным
   `gate: yes` — ровно то сочетание (низкая цена ошибки + обратимость), при котором рамка курса и
   предсказывает успех большого ИИ. Остальные foundation-model/agentic-кейсы корпуса (humanoid-хайп,
   L13-007) остаются `undetermined` — новых успешных high-stakes foundation-model кейсов в logistics
   не найдено, что **согласуется** с существующей находкой курса (0% успеха foundation-model на
   high/extreme неопределённости), а не противоречит ей.
3. **Контрпример, который стоит явно назвать: Aurora Innovation.** Classified `deep-learning`,
   `blast_radius: catastrophic`, `gate: unclear` — и пока `outcome: success` (250k+ миль без
   инцидентов). Это прямо в зоне, где рамка курса предсказывает самый высокий риск провала
   (катастрофический blast radius + отсутствие явного человека-в-кабине). Пока рамка не
   опровергнута (единичный пока не провалившийся кейс не опровергает статистику 137 провалов), но
   это именно тот тип кейса, который стоит перепроверить через полгода-год — если Aurora продолжит
   расти без инцидентов, это станет самым весомым контрпримером всей линии исследования.
4. **`external_driver: mixed` преобладает на стороне бизнес-провалов (5 из 13), а не `no`.** Почти
   все крупные корпоративные провалы в этой подборке — результат одновременно макроэкономического
   шока (крах фрахтового рынка 2022–2023, обвал SPAC-рынка) и внутреннего исполнения — что
   затрудняет чистую атрибуцию «ИИ не справился» в любую сторону. Это согласуется с
   предупреждением реестра о путанице гейта с осью 1 (см. `reestr-reshenij-README.md` п.4) —
   здесь аналогичная путаница грозит оси `external_driver`: бизнес-крахи логистического AV/AMR-
   сектора 2022–2023 почти никогда не изолируемы от общего охлаждения венчурного рынка того же
   периода.
5. **Honest shortfall:** не найдено ни одного **независимо (не вендором) верифицированного** успеха
   с конкретной датой **именно на 2023 год** — единственный кандидат (Amazon Sequoia) держится на
   `confidence: low`. Если этот пробел важен, следующий проход стоит специально искать 2023-кейсы
   supply-chain-forecasting (Blue Yonder/Kinaxis/o9-класс инструментов), которые не попали в этот
   раунд из-за исчерпания лимита WebSearch.

---

## Батч 2 (третья волна, 2026-11-20) — добавлено 26 кейсов: V13-026…V13-051

Полные таблицы с осями, описаниями и источниками — `../verified-cases-batch2/lec-13-verified-batch2.md` (файл provenance; локальные номера там — S1/F1/B2-S1 и т.п., НЕ финальные ID). Консолидация в `reestr-reshenij-verified.csv` — скриптом `build_verified_batch2.py` (дедуп + enum-валидация), разбор дублей — файл 18 §1.

Исключены при консолидации как дубли: Covariant «неэксклюзивная» сделка (то же событие, что V11-012).

| final_id | case_name | year | outcome |
|---|---|---|---|
| V13-026 | Fetch Robotics — приобретена Zebra Technologies за $290-301М (~30,5× выручки, ARR ~$10М) | 2021 | success |
| V13-027 | Einride + DB Schenker, Йёнчёпинг — первая в мире ежедневная автономная грузоперевозка на открытой дороге без водителя (5 км/ч) | 2019 | success |
| V13-028 | UPS Flight Forward + Matternet — медицинские дрон-рейсы WakeMed (Raleigh), первая в мире полная FAA Part 135 сертификация дрон-авиалинии (1 окт. 2019) | 2019 | success |
| V13-029 | Wingcopter + UNICEF — доставка вакцин дронами в 19 удалённых деревень острова Пентекост, Вануату | 2019 | success |
| V13-030 | Windracers — первый успешный рейс грузового беспилотника с медицинскими грузами, Корнуолл → острова Силли | 2020 | success |
| V13-031 | Covariant Brain + ABB/Knapp — развёртывание ИИ-пикинга (imitation + reinforcement learning) на складе Obeta, Германия | 2020 | success |
| V13-032 | AutoStore — IPO на Oslo Stock Exchange (крупнейшее IPO Норвегии за 20 лет); клиент CVS обрабатывает 2M+ товаров/неделю на объекте Hainesport, NJ | 2021 | success |
| V13-033 | TuSimple — первый в мире полностью безводительский рейс грузовика (без человека в кабине и без дистанционного оператора), Tucson–Phoenix, 80 миль | 2021 | success |
| V13-034 | GXO Logistics — ~7 600 единиц складской робототехники/ИИ (кобот, AGV, goods-to-person) развёрнуто у клиентов | 2022 | success |
| V13-035 | Ike Robotics — поглощена Nuro, самостоятельная разработка Class-8 автономного трекинга прекращена (условия сделки не раскрыты) | 2020 | partial |
| V13-036 | Oxbotica CargoPod — 3-недельное автономное испытание на грузовых маршрутах airside-зоны аэропорта Хитроу; данных о продолжении/масштабировании не найдено | 2018 | partial |
| V13-037 | Manna — экстренная перестройка с обычной дрон-доставки на доставку рецептурных лекарств и еды изолированным жителям деревни Муниголл (Ирландия) в начале COVID-19 | 2020 | partial |
| V13-038 | Attabotics + Nordstrom — развёртывание 3D-склада (кубическая AS/RS) для автоматизации части выполнения заказов; метрик производительности в источнике нет | 2019 | partial |
| V13-039 | Uber ATG — закрытие подразделения беспилотных грузовиков, фокус смещён на автомобили, после settlement с Waymo и смертельного инцидента в Темпе | 2018 | failure |
| V13-040 | Matternet + Swiss Post — два крушения дронов (янв./июль 2019), второе возле детей в Цюрихе → приостановка медицинской дрон-доставки на неопределённый срок | 2019 | failure |
| V13-041 | Ocado, склад Andover — пожар от бракованного зарядного устройства робота, ущерб $137М, годовой убыток £143М | 2019 | failure |
| V13-042 | Kiwibot — пожар робота от дефектной батареи возле студенческого союза UC Berkeley, временный возврат к курьерам-людям | 2018 | failure |
| V13-043 | Kiwibot — раскрытие ручного теле-управления роботами из Колумбии каждые 5-10 секунд (оплата ~$2/час) вместо заявленной «автономности» | 2019 | failure |
| V13-044 | Deliv — закрытие краудсорсингового сервиса same-day доставки (35 рынков), технологические активы выкуплены Target | 2020 | failure |
| V13-045 | DHL Parcelcopter — завершение 8-летней программы собственного грузового дрона и пилота медицинской доставки в Танзании с Wingcopter | 2021 | failure |
| V13-046 | Refraction AI — внезапное прекращение сервиса доставки REV-1 в Ann Arbor, флот из 10 роботов переведён в Остин, компания не выжила | 2021 | failure |
| V13-047 | Peloton Technology — прекращение деятельности и ликвидация после десятилетия (2011-2021) без коммерческого запуска truck platooning | 2021 | failure |
| V13-048 | Flexport — со-CEO обнаружил систематически завышенную модель прогноза выручки; увольнение 20% персонала (~640 чел.) | 2023 | failure |
| V13-049 | Attabotics — массовые увольнения (29 июня 2025), банкротство (июль 2025), продажа активов Lafayette Engineering (сент. 2025) после пожара на объекте Canadian Tire (март 2023) | 2025 | failure |
| V13-050 | Flirtey — закрытие пионера дрон-доставки (FAA-разрешения с 2015, партнёрство 7-Eleven 2016) из-за недостаточного финансирования | 2024 | failure |
| V13-051 | Zebra Technologies — сворачивание робот-бизнеса на базе Fetch Robotics («не масштабировался достаточно быстро»), 4 года после покупки за $290М | 2025 | failure |

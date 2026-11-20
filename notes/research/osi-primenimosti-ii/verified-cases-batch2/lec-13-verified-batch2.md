---
title: "Лекция 13 (logistics) — волна 2: независимо верифицированные кейсы, внешние источники"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 13 — logistics: волна 2 внешне верифицированных кейсов (2018–2025)

## Подход к поиску

Цель — догнать общую выборку исследования до 1000+ строк новыми кейсами «ИИ в
логистике/автономной доставке», **не повторяя** ни 25 кейсов волны 1
(`verified-cases/lec-13-verified.md`), ни 34 кейса первичной разметки
(`razmetka/lec-13.md` + `razmetka/lec-13-os4.md`). Оба списка прочитаны целиком перед
началом поиска; каждый новый кандидат проверялся на пересечение по названию компании
**и** по конкретному событию — один и тот же вендор мог войти повторно только с
содержательно другим, иначе датированным эпизодом (сам реестр уже допускает это: в
волне 1 Wing встречается дважды — «1 000 000-я доставка» и «закрытие в Канберре» — как
две разные строки одной компании).

**Инструментальное ограничение, честно зафиксированное.** WebSearch в этой сессии был
полностью исчерпан (200 из 200 вызовов) уже на шестом раунде поиска — после этого **все**
оставшиеся кейсы добирались исключительно через WebFetch по угаданным/известным URL
(преимущественно Wikipedia, плюс несколько прямых пресс/деловых источников, найденных до
исчерпания лимита). Это сузило охват: не удалось подтвердить несколько правдоподобных
кандидатов (Volvo Vera, SF Express, Yandex Rover, Transfix, Sennder, Dronamics, Flytrex,
Nimble Robotics, Boston Dynamics Stretch+DHL — см. «Отброшенные кандидаты» ниже), потому
что для них не нашлось рабочей прямой ссылки без полнотекстового поиска.

**Приоритет по годам.** Волна 1 сама отметила пробел на 2023 год (единственный success-
кандидат — Amazon Sequoia — держался на `confidence: low`). Эта волна целенаправленно
искала кейсы **2018–2021**, которые в волне 1 почти не представлены: из 27 итоговых строк
**21 (78%)** приходятся на 2018–2021.

## Итог: 27 новых кейсов — 9 success + 5 partial + 13 failure

Все 27 кейсов — новые компании/события, не встречающиеся ни в одном из 59 кейсов,
накопленных в Лекции 13 до этой волны (25 волны 1 + 34 первичной разметки).

---

## Качество источников — честная оценка

- **Сильные источники (несколько независимых изданий сходятся на одних фактах):**
  закрытие Uber ATG trucking (TechCrunch, CNN, Slate, MIT Technology Review), крушения
  дронов Matternet/Swiss Post (TechCrunch, DroneLife, DroneDJ, Axios), пожар на складе
  Ocado в Andover (Forbes, Euronews — совпадают по сумме ущерба $137M), остановка DHL
  Parcelcopter (FreightWaves, DroneDJ, UASVision, sUAS News), закрытие Deliv (CNBC,
  MarketScreener, Wikipedia), увольнения Flexport с цитатой со-CEO о систематически
  завышенном прогнозе выручки (CNBC, Yahoo Finance, PYMNTS).
- **Средние источники (один солидный источник, цифры внутренне непротиворечивы, но не
  аудированы третьей стороной):** большинство Wikipedia-кейсов этой волны (Einride, UPS
  Flight Forward/Matternet WakeMed, Wingcopter, Windracers, AutoStore, Covariant,
  Attabotics, TuSimple, GXO Logistics, Peloton Technology, Flirtey, Oxbotica) — факты
  внутренне непротиворечивы (конкретные даты, суммы, партнёры), но единственный источник.
- **Слабые/низкой уверенности:** приобретение Ike Robotics Нуро (сумма сделки не
  раскрыта — TechCrunch/VentureBeat только подтверждают факт и состав команды), сворачивание
  Zebra Technologies робот-бизнеса на базе Fetch (единственный источник — The Robot Report,
  новость декабря 2025, не успела разойтись по другим изданиям на момент исследования),
  раскрытие о ручном теле-управлении роботами Kiwibot («Colombian operators control robots
  manually every 5-10 seconds despite autonomous claims») — это вторичное упоминание
  внутри статьи Wikipedia о Kiwi Campus без прямого доступа к первичному журналистскому
  расследованию (WebFetch не смог получить страницы The Verge/CNET в этой сессии — см.
  «Отброшенные кандидаты»). **Этот последний кейс оставлен в выборке намеренно**, несмотря
  на низкую уверенность: он методически ценен для курса ровно потому, что это пример
  переоценённой/ложно заявленной автономности ИИ («автономный» робот, управляемый человеком
  каждые 5-10 секунд за $2/час) — прямое попадание в тему критического суждения курса, а не
  рядовой кейс успеха/провала модели.
- **Общее наблюдение:** как и в волне 1, успешные кейсы почти всегда держатся на
  собственных пресс-релизах/корпоративной истории (через Wikipedia), а провальные —
  на независимой деловой прессе. Это структурное смещение метода поиска, не следствие
  реального распределения исходов в индустрии.

---

## Успешные кейсы (outcome = success)

| case_name | year | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Fetch Robotics — приобретена Zebra Technologies за $290-301М (~30,5× выручки, ARR ~$10М) | 2021 | low | none | seconds-minutes | none | sensor-fusion | not-applicable | low | not-applicable | success | high | https://www.cbinsights.com/research/zebra-technologies-acquires-fetch-robotics/ |
| Einride + DB Schenker, Йёнчёпинг — первая в мире ежедневная автономная грузоперевозка на открытой дороге без водителя (5 км/ч) | 2019 | low | none | seconds-minutes | F-C | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Einride |
| UPS Flight Forward + Matternet — медицинские дрон-рейсы WakeMed (Raleigh), первая в мире полная FAA Part 135 сертификация дрон-авиалинии (1 окт. 2019) | 2019 | low | none | seconds-minutes | none | sensor-fusion | yes | low | not-applicable | success | high | https://en.wikipedia.org/wiki/UPS_Flight_Forward |
| Wingcopter + UNICEF — доставка вакцин дронами в 19 удалённых деревень острова Пентекост, Вануату | 2019 | low | none | hours-days | none | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Wingcopter |
| Windracers — первый успешный рейс грузового беспилотника с медицинскими грузами, Корнуолл → острова Силли | 2020 | low | none | hours-days | none | sensor-fusion | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Windracers |
| Covariant Brain + ABB/Knapp — развёртывание ИИ-пикинга (imitation + reinforcement learning) на складе Obeta, Германия | 2020 | moderate | U3 | seconds-minutes | none | deep-learning | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/Covariant_(company) |
| AutoStore — IPO на Oslo Stock Exchange (крупнейшее IPO Норвегии за 20 лет); клиент CVS обрабатывает 2M+ товаров/неделю на объекте Hainesport, NJ | 2021 | low | none | seconds-minutes | none | hybrid | yes | low | not-applicable | success | high | https://en.wikipedia.org/wiki/AutoStore |
| TuSimple — первый в мире полностью безводительский рейс грузовика (без человека в кабине и без дистанционного оператора), Tucson–Phoenix, 80 миль | 2021 | high | none | hours-days | F-C | sensor-fusion | no | catastrophic | not-applicable | success | medium | https://en.wikipedia.org/wiki/TuSimple |
| GXO Logistics — ~7 600 единиц складской робототехники/ИИ (кобот, AGV, goods-to-person) развёрнуто у клиентов | 2022 | low | none | seconds-minutes | none | hybrid | yes | low | not-applicable | success | medium | https://en.wikipedia.org/wiki/GXO_Logistics |

**Счёт успехов: 9.**

---

## Частично определённые кейсы (outcome = partial)

Пять кейсов размечены `partial`, не `success`/`failure`, по явным причинам (указаны в
описании каждой строки) — не как способ спрятать неудобный результат, а как честная
категория для реальных сделок/развёртываний без доказанного устойчивого исхода.

| case_name | year | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ike Robotics — поглощена Nuro, самостоятельная разработка Class-8 автономного трекинга прекращена (условия сделки не раскрыты) | 2020 | high | unclear | season-years | F-A | sensor-fusion | not-applicable | low | mixed | partial | medium | https://techcrunch.com/2020/12/23/nuro-acquires-autonomous-trucking-startup-ike/ |
| Oxbotica CargoPod — 3-недельное автономное испытание на грузовых маршрутах airside-зоны аэропорта Хитроу; данных о продолжении/масштабировании не найдено | 2018 | low | none | seconds-minutes | none | sensor-fusion | yes | low | not-applicable | partial | medium | https://en.wikipedia.org/wiki/Oxbotica |
| Manna — экстренная перестройка с обычной дрон-доставки на доставку рецептурных лекарств и еды изолированным жителям деревни Муниголл (Ирландия) в начале COVID-19 | 2020 | low | none | weeks-months | F-A | sensor-fusion | yes | low | yes | partial | medium | https://en.wikipedia.org/wiki/Delivery_drone |
| Covariant — «неэксклюзивная» сделка с Amazon по лицензированию (найм 25% персонала + 3 основателей); whistleblower 2025 раскрыл оценку сделки $380М против $625М в 2023 — статус «zombie company» | 2024 | moderate | unclear | season-years | F-A | deep-learning | not-applicable | medium | mixed | partial | medium | https://en.wikipedia.org/wiki/Covariant_(company) |
| Attabotics + Nordstrom — развёртывание 3D-склада (кубическая AS/RS) для автоматизации части выполнения заказов; метрик производительности в источнике нет | 2019 | low | none | seconds-minutes | none | hybrid | yes | low | not-applicable | partial | medium | https://en.wikipedia.org/wiki/Attabotics |

---

## Провальные кейсы (outcome = failure)

| case_name | year | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Uber ATG — закрытие подразделения беспилотных грузовиков, фокус смещён на автомобили, после settlement с Waymo и смертельного инцидента в Темпе | 2018 | high | unclear | season-years | F-A | sensor-fusion | not-applicable | low | mixed | failure | high | https://techcrunch.com/2018/07/30/ubers-self-driving-trucks-division-is-dead-long-live-uber-self-driving-cars |
| Matternet + Swiss Post — два крушения дронов (янв./июль 2019), второе возле детей в Цюрихе → приостановка медицинской дрон-доставки на неопределённый срок | 2019 | moderate | U3 | seconds-minutes | F-C | sensor-fusion | no | medium | no | failure | high | https://techcrunch.com/2019/07/30/drone-crash-near-kids-leads-swiss-post-and-matternet-to-suspend-autonomous-deliveries |
| Ocado, склад Andover — пожар от бракованного зарядного устройства робота, ущерб $137М, годовой убыток £143М | 2019 | low | U3 | hours-days | F-C | hybrid | no | high | no | failure | high | https://www.forbes.com/sites/samshead/2019/07/09/ocado-takes-137-million-hit-from-warehouse-blaze-sparked-by-robot/ |
| Kiwibot — пожар робота от дефектной батареи возле студенческого союза UC Berkeley, временный возврат к курьерам-людям | 2018 | low | U3 | seconds-minutes | F-C | hybrid | no | low | no | failure | medium | https://en.wikipedia.org/wiki/Kiwibot |
| Kiwibot — раскрытие ручного теле-управления роботами из Колумбии каждые 5-10 секунд (оплата ~$2/час) вместо заявленной «автономности» | 2019 | unclear | unclear | seconds-minutes | none | rule-based | not-applicable | low | no | failure | low | https://en.wikipedia.org/wiki/Kiwibot |
| Deliv — закрытие краудсорсингового сервиса same-day доставки (35 рынков), технологические активы выкуплены Target | 2020 | unclear | unclear | season-years | F-B | unclear | not-applicable | medium | mixed | failure | high | https://www.cnbc.com/2020/05/07/target-in-talks-to-boost-its-same-day-delivery-ambitions-by-buying-pieces-of-startup-deliv.html |
| DHL Parcelcopter — завершение 8-летней программы собственного грузового дрона и пилота медицинской доставки в Танзании с Wingcopter | 2021 | moderate | unclear | season-years | F-A | sensor-fusion | not-applicable | low | no | failure | high | https://www.freightwaves.com/news/dhl-pulling-its-parcelcopter-drone-ceasing-drone-development |
| Refraction AI — внезапное прекращение сервиса доставки REV-1 в Ann Arbor, флот из 10 роботов переведён в Остин, компания не выжила | 2021 | moderate | unclear | season-years | F-B | sensor-fusion | not-applicable | low | unclear | failure | medium | https://annarborobserver.com/robot-farewell/ |
| Peloton Technology — прекращение деятельности и ликвидация после десятилетия (2011-2021) без коммерческого запуска truck platooning | 2021 | moderate | unclear | season-years | F-A | sensor-fusion | not-applicable | low | unclear | failure | high | https://en.wikipedia.org/wiki/Peloton_Technology |
| Flexport — со-CEO обнаружил систематически завышенную модель прогноза выручки; увольнение 20% персонала (~640 чел.) | 2023 | high | U2 | weeks-months | F-B | classical-ml | not-applicable | high | mixed | failure | high | https://www.cnbc.com/2023/01/11/flexport-to-lay-off-20percent-of-its-global-workforce.html |
| Attabotics — массовые увольнения (29 июня 2025), банкротство (июль 2025), продажа активов Lafayette Engineering (сент. 2025) после пожара на объекте Canadian Tire (март 2023) | 2025 | unclear | U3 | season-years | F-A | hybrid | not-applicable | high | mixed | failure | high | https://en.wikipedia.org/wiki/Attabotics |
| Flirtey — закрытие пионера дрон-доставки (FAA-разрешения с 2015, партнёрство 7-Eleven 2016) из-за недостаточного финансирования | 2024 | moderate | unclear | season-years | F-A | sensor-fusion | not-applicable | low | unclear | failure | high | https://en.wikipedia.org/wiki/Flirtey |
| Zebra Technologies — сворачивание робот-бизнеса на базе Fetch Robotics («не масштабировался достаточно быстро»), 4 года после покупки за $290М | 2025 | unclear | unclear | season-years | F-A | sensor-fusion | not-applicable | medium | mixed | failure | medium | https://www.therobotreport.com/zebra-technologies-winding-down-fetch-based-mobile-robot-group/ |

**Счёт провалов: 13.**

---

## Заметки по осям и расхождения с рамкой курса

1. **Axis4_gate = `not-applicable` преобладает на бизнес-событиях, как и в волне 1.**
   8 из 13 провалов этой волны — закрытия/банкротства/слияния (Uber ATG, Ike→Nuro, Deliv,
   DHL Parcelcopter, Peloton, Attabotics, Flirtey, Zebra/Fetch) — вопрос «был ли гейт перед
   действием» не имеет смысла для решения совета директоров закрыть подразделение. Это
   подтверждает наблюдение волны 1 (п.1 её «Заметок»): Ось 4 создана для операционных
   ИИ-решений в реальном времени, не для корпоративных событий.
2. **Fetch Robotics — полная дуга: успех (2021) → провал (2025) одной и той же сделки.**
   Акт покупки Zebra Technologies за $290М был классифицирован как `success` в 2021 году;
   та же технология/бизнес-линия классифицирована как `failure` в 2025, когда Zebra сама
   её свернула. Это иллюстрирует методическую опасность единичной точки измерения: «успех»
   M&A-сделки на момент объявления не гарантирует долгосрочного успеха интегрированного
   продукта — то же верно для Attabotics (partial-деплой у Nordstrom 2019 → банкротство
   2025) и Covariant (success-деплой у ABB/Knapp 2020 → down-valued «zombie» сделка 2024).
3. **Kiwibot-теле-управление — контрпример на уровне определения, не на уровне исхода.**
   В отличие от всех остальных 26 строк, этот кейс не про то, справился ли ИИ с задачей —
   он про то, что заявленного ИИ (автономной навигации) в значимой части операций не было
   вовсе: решения принимал человек-оператор каждые 5-10 секунд. Это прямое попадание в
   фундаментальное правило курса про провалы/ограничения/альтернативы (≥30% контента) —
   конкретный пример того, как маркетинговая заявка «автономный робот» маскирует
   человеческий труд, причём оплаченный по ставке много ниже минимальной в стране
   оператора. Рекомендуется для отдельного упоминания в разделе лекции о честности заявок
   вендоров об автономности.
4. **2018–2021 покрытие закрыто предметно, не только числом строк.** 21 из 27 кейсов
   (78%) — именно та `confidence`-слабая зона волны 1. Среди них есть как success
   (Einride, UPS Flight Forward/Matternet, Wingcopter, Fetch→Zebra, AutoStore, TuSimple),
   так и failure (Uber ATG, Matternet-крушения, Ocado-пожар, Kiwibot×2, Deliv, DHL
   Parcelcopter, Refraction AI, Peloton) — распределение исходов внутри закрытого периода
   само по себе близко к паритетному, не смещённое искусственно в одну сторону.
5. **TuSimple (дек. 2021) — отдельная методическая оговорка.** Этот кейс — другое,
   содержательно отдельное событие той же компании, чей финансовый провал (делистинг
   янв. 2024) уже зафиксирован и в `razmetka/lec-13.md`, и в волне 1. Здесь размечен explicitly
   более ранний операционный milestone (первый в мире безводительский рейс без человека
   вообще в контуре) — успешный на момент события, независимо от позднейшего финансового
   исхода той же компании. Решение включить его сделано по аналогии с тем, как сама волна 1
   дважды использовала Wing (успех доставки + провал Канберры) как две разные строки одной
   компании.

---

## Отброшенные кандидаты

Проверялись, но не вошли в итоговую выборку:

- **Boxbot** — при проверке оказалось, что компания **не** закрылась (статус
  «Operational», пивот на складскую автоматизацию, работает с Amazon) — исходная гипотеза
  о провале не подтвердилась, кандидат отброшен как ложноположительный.
- **Volvo Vera** (автономный электрогрузовик для портов) — Wikipedia-статья о Volvo Trucks
  не содержит информации об этом проекте; альтернативного рабочего URL без WebSearch не
  найдено.
- **SF Express** (китайский cargo-дрон, сертификат CAAC) — единственный найденный факт
  (военные airdrop-операции 2018 для Южного командования НОАК) слишком тонко
  документирован и не про гражданскую логистику с метрикой.
- **Yandex Rover** — профильная статья Wikipedia о Yandex не содержит упоминаний
  программы доставочных роботов; подтверждения не найдено.
- **Transfix, Sennder** (freight-matching платформы) — отдельных Wikipedia-страниц не
  существует (404); без WebSearch не удалось найти альтернативный источник.
- **Dronamics, Flytrex, Nimble Robotics** — Wikipedia-страниц не существует (404);
  кандидаты правдоподобны (упоминались как партнёры/конкуренты в других найденных
  источниках), но не подтверждены напрямую.
- **Boston Dynamics Stretch + DHL/Gap Inc.** — официальная страница кейс-стади Boston
  Dynamics не содержит упоминаний Stretch-кейсов (только Spot); партнёрство правдоподобно
  по памяти модели, но не подтверждено доступным источником в этой сессии.
- **XPO Logistics (AI/ML)** — профильная статья Wikipedia не содержит информации об
  AI/ML-инициативах компании, только корпоративная история и M&A.
- **Locomation** — уже присутствует как именованный кейс в `razmetka/lec-13.md`
  (`Zoox / Locomation / Plus.ai`), сознательно исключён, чтобы не задвоить существующую
  строку корпуса.
- **Marble Robotics** (SF sidewalk-робот, по косвенным данным приобретён Caterpillar) —
  поисковые сниппеты подтверждают закрытие SF-операций из-за городского регулирования и
  последующее приобретение, но точная дата не подтверждена ни одним напрямую зафетченным
  источником (Crunchbase вернул HTTP 403) — исключён за недостаточной точностью, а не за
  недостоверностью факта в целом.
- **PlusAI — трансконтинентальный рейс Тампа-Лос-Анджелес (дек. 2018)** — страница
  Wikipedia для PlusAI не существует (404); без рабочего источника кандидат отброшен,
  несмотря на хорошую документированность события по памяти модели.
- **Starship Technologies — дополнительные эпизоды (запуск в Милтон-Кинсе 2018,
  столкновение с охранником парковки ASU 2023)** — оба подтверждены тем же Wikipedia-
  запросом, что дал кейс с автобусом в Таллине, но сознательно не включены: Starship уже
  фигурирует 3 раза в существующем корпусе Лекции 13 (разметка + волна 1 ×2); четвёртая
  и пятая строки той же компании признаны избыточной концентрацией, а не новым сигналом.

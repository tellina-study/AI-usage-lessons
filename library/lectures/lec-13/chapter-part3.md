---
lecture: 13
title: "AI в логистике и транспорте — Часть 3"
parts_of: "chapter.md"
part: 3
---

# Глава 13. AI в логистике и транспорте — Часть 3

> **Многочастная структура.** Это часть 3 главы 13. Часть 1 — `chapter.md` (введение + §0 + §1 + §2). Часть 2 — `chapter-part2.md` (§3 + §4). Эта часть содержит §5 (замыкание + мост к Лекции 14) и Источники.

## Оглавление (Часть 3)

- [§5. Замыкание + мост к Лекции 14](#5-замыкание--мост-к-лекции-14)
  - [§5.1. Семь критериев «когда AI плохая идея в логистике» — финальный recap](#51-семь-критериев-когда-ai-плохая-идея-в-логистике--финальный-recap)
  - [§5.2. Карьерный угол: где работа инженера логистики и транспорта](#52-карьерный-угол-где-работа-инженера-логистики-и-транспорта)
  - [§5.3. Список для чтения: что прочесть после главы](#53-список-для-чтения-что-прочесть-после-главы)
  - [§5.4. Лекция инженерного смирения: Cruise vs Waymo](#54-лекция-инженерного-смирения-cruise-vs-waymo)
  - [§5.5. Мост к Лекции 14: что переносится, что — нет](#55-мост-к-лекции-14-что-переносится-что--нет)
  - [§5.6. Заключительная мысль](#56-заключительная-мысль)
- [Источники](#источники)

## §5. Замыкание + мост к Лекции 14

### §5.1. Семь критериев «когда AI плохая идея в логистике» — финальный recap

[for-slide-s36]

В конце главы выкристаллизуем семь практических критериев, по которым инженер может в первые тридцать секунд разговора с поставщиком отличить **разумное AI-предложение** от **маркетингового пика-питча**. Эти семь критериев — суть всей главы в компактной форме.

**Критерий первый. Среда контролируемая?** Если да — AI применим на уровне 1 (склад, порт, рельсы). Если нет — переходить к остальным критериям. Это **главный предиктор**, и он работает быстрее и надёжнее, чем любые другие. Маркер: контролируемые лед, известная геометрия, отсутствие пешеходов, известный SKU-каталог. Anti-маркер: city-streets, погода, эмерджентность.

**Критерий второй. Задача — well-defined optimization?** Если да — **OR (operations research) лучше, чем ML/RL**. UPS ORION, авиа yield management, vehicle scheduling — это всё **OR**, и Google OR-Tools открыт и бесплатен как baseline. Если поставщик не может предоставить сравнение с OR-baseline — настаивайте.

**Критерий третий. Demand pattern стационарный?** Если да — **EOQ + safety stock + ABC лучше, чем ML** для большинства SKU. Аудит-вопрос: какой процент SKU реально требует ML vs классических формул?

**Критерий четвёртый. Safety-critical с регуляторным аудитом?** Если да — **rule-based + human-in-the-loop требуется**. Чёрный ящик ML не работает в авиации, фарме, медицине, ядерной энергетике. Это **regulatory hard fact**, не предмет дискуссии.

**Критерий пятый. Событие в-distribution?** Если да — ML работает. Если нет (чёрный лебедь — geopolitical, pandemic, port-strike) — **human dispatcher + сценарное планирование**. Houthi 2024, Suez 2021, COVID 2020 — три урока за пять лет.

**Критерий шестой. Production track record шесть месяцев+?** Если да — продукт valid. Если нет — **pilot-purgatory риск**. Девяносто пять процентов GenAI-пилотов не доходят до production (MIT Sloan 2025). Поставщик без 6+ месяцев track record — pre-production, и инвестиция несёт значительно больший риск.

**Критерий седьмой. Baseline + counterfactual articulated?** Если поставщик не может назвать конкретную baseline и явное counterfactual сравнение — заявленный «AI экономит +25%» бессмысленен. Это **buyer-beware** маркер.

Эти семь критериев — **не пятиминутная теоретическая модель**, а **инженерный быстрый тест**, который инженер сможет провести в любой переговорной с поставщиком. Каждый критерий имеет конкретный ответ «да» или «нет», и в каждом случае есть **defensible альтернатива** — OR, EOQ, scenario planning, rule-based, human-in-loop, или просто отказ от инвестиции.

### §5.2. Карьерный угол: где работа инженера логистики и транспорта

[for-slide-s37]

Где инженер с пересекающимися навыками в AI + логистика + транспорт может строить карьеру в 2026 году? Я кратко обрисую ландшафт, без рекомендаций конкретных работодателей.

**В России** ландшафт включает несколько категорий компаний:

- **Производители грузового и пассажирского транспорта с автономным направлением.** КамАЗ (автономный КамАЗ-54901 с Cognitive Pilot стеком), несколько других автозаводов с pilot-программами.
- **Технологические компании с автономным стеком.** Cognitive Pilot (отделение Cognitive Technologies, специализация на восприятии для специальных рабочих сред — агросектор, магистральный transport), Yandex SDG до санкционного раздела 2024 года и её спин-аут Avride под голландской parent-компанией для non-Russia операций.
- **Логистические компании с in-house ML-инжинирингом.** Сбер (включая Сберлогистику), Wildberries (распределительные центры + last-mile), Деловые Линии (cargo classification + route optimization), Pony Express, СДЭК. Public production-метрики этих компаний ограничены, но adoption активный.
- **Военно-космические и оборонные интеграторы** с дуально-используемой autonomy технологией. Подробнее об оборонном контуре — в Лекции 9; в логистическом контексте они работают на cargo-доставку в труднодоступные зоны, военно-транспортную авиацию, специальные перевозки. Эти организации требуют специфической допуска и обычно не публичны в найме.

**В мире** ландшафт значительно шире:

- **AV-сurvivors:** Waymo (Alphabet), Aurora Innovation, Mobileye (Intel subsidiary), Apollo Go (Baidu), Pony.ai, WeRide, Tesla (с особенностями vision-only ставки). Также — Wayve (UK end-to-end), Plus.ai (supervised L2+/L3), Kodiak (defense + commercial dual).
- **Складская роботизация.** Symbotic, Amazon Robotics (внутренний), Locus Robotics, GreyOrange, Geek+, плюс integration-партнёры (Honeywell Intelligrated, KION Dematic, Vanderlande, Knapp).
- **Last-mile.** Starship Technologies, Coco Robotics, Zipline, Nuro (пивот в licensing), Wing (Alphabet), Manna (Ирландия), Serve Robotics (US).
- **OR-software vendors.** Gurobi Optimization, IBM ILOG CPLEX, Google (OR-Tools), Coupa (supply chain), Flexport (digital freight forwarder), C.H. Robinson, Convoy (распущена в 2023 году но активы куплены Flexport).
- **Telematics + SaaS.** Samsara, project44, FourKites, FreightWaves, Loadsmart.

**Образовательная подготовка.** Универсальные технические университеты готовят инженеров с пересекающимися навыками — control systems, machine learning, operations research, embedded systems. **Профильные кафедры в области инфокоммуникаций и транспортных систем** обычно дают сильную базу по сетям + транспортной логистике. **Военно-космические академии** готовят инженеров с экспертизой в дуально-используемой autonomy технологии (mission planning, real-time decision-making под пределами по latency, formal verification под регуляторным давлением), и эти навыки переносимы в гражданский сегмент через дуально-используемых интеграторов. Магистерские программы AI и Data Science в профильных технических университетах России и мира — путь продолжения обучения для инженера логистики с базовой инженерной подготовкой.

**Ключевые навыки для инженера логистики и транспорта 2026 года.** Я перечислю набор, который **не зависит** от конкретного работодателя:

- **Operations Research fundamentals** — линейное и целочисленное программирование, методы branch-and-bound, эвристики savings, simulated annealing, tabu search. Google OR-Tools как минимум практический инструмент.
- **Machine Learning fundamentals** — supervised learning, основные архитектуры (CNN для perception, transformers для sequential data, GNN для graph problems), distributional shift awareness.
- **Multi-modal sensor fusion** — лидар + камеры + радар, классические алгоритмы Kalman filtering, particle filtering, понимание trade-off между типами сенсоров.
- **Regulatory landscape** — SAE J3016, NHTSA SGO, ICAO Annex 10, IMO MASS, FAA Part 107, EU AI Act, российский ЭПР. Умение читать regulatory docs и говорить с регулятором.
- **Safety case engineering** — formal safety case, ISO 26262, ISO 21448 (SOTIF — Safety of the Intended Functionality), Mobileye Responsibility-Sensitive Safety (RSS), Waymo safety report methodology.
- **Critical judgment.** Это самый важный навык, и весь курс — про это. Умение задать правильный вопрос поставщику, отличить демо от production, разпознать buyer-beware маркеры.

### §5.3. Список для чтения: что прочесть после главы

[for-slide-s38]

Я предлагаю список из десяти источников, ранжированный по приоритету для инженера, серьёзно интересующегося областью AI в логистике и транспорте. Это **не исчерпывающий список**, и каждый источник имеет известные ограничения, но они **формируют базовый кругозор**.

**Высший приоритет — обязательное чтение для каждого инженера-логистика:**

1. **Stefan Seltz-Axmacher. «The end of Starsky Robotics» (Medium, март 2020).** Личное эссе основателя обанкротившегося AV-trucking стартапа. Точно объясняет sim-to-real gap, money-vs-progress gap, supervised ML overpromising. **Предсказал в марте 2020 года всё, что произошло с Argo, Embark, TuSimple в 2022–2024 годах.**
2. **NTSB Highway Accident Report HAR-19/03.** Официальный отчёт о Uber Tempe 2018 fatality. Defensible authority — это голос регулятора, не блогера. Учит, как regulator анализирует AV-инциденты.
3. **Waymo Safety Report 2025.** Самый подробный публичный safety case для L4 robotaxi. Демонстрирует метрики crash rate per million miles, разбор edge cases, ODD-дисциплину.

**Второй приоритет — для развития картины индустрии:**

4. **ATA Driver Shortage Report (2024).** Базовая статистика дефицита водителей в США + структурные причины + прогноз на десятилетие. Понимание, почему AV не решает эту проблему.
5. **Aurora Innovation press kit (май 2025).** Анализ first commercial L4 driverless trucking launch — crawl-walk-run methodology, ODD expansion strategy, financial backing.
6. **CNBC «How Ford and VW's multibillion-dollar self-driving car project failed» (март 2023).** Полный case study Argo AI shutdown — структурные причины, OEM-investor dynamics, talent costs.
7. **Goldman Sachs report China robotaxi 2025.** Прогноз китайского рынка на 2035 год, ландшафт Apollo Go, Pony.ai, WeRide.

**Третий приоритет — фундамент OR и классические инструменты:**

8. **Bertsimas, Tsitsiklis. «Introduction to Linear Optimization» (классический учебник).** Базовый учебник по OR. Глава о VRP — must-read для понимания, почему OR лучше RL для well-defined routing.
9. **INFORMS UPS ORION case study.** Полный case study, как UPS внедрила OR-based routing и достигла 300–400 миллионов долларов savings в год без deep learning.
10. **Hopp, Spearman. «Factory Physics» (классический учебник).** Не специфично для логистики, но содержит главу о just-in-time vs just-in-case + safety stock fundamentals. Помогает понять, почему JIT хрупкая в условиях черных лебедей.

**Дополнительные источники для специфических интересов:**

- Mobileye Responsibility-Sensitive Safety (RSS) framework whitepaper.
- ICAO Annex 10 (air traffic regulation).
- Wikipedia article «List of Tesla Autopilot crashes» (постоянно обновляемый, с references).
- J.P. Morgan supply chain research portal (для дальнейших обновлений Red Sea и black-swan ситуаций).

### §5.4. Лекция инженерного смирения: Cruise vs Waymo

[for-slide-s39]

Перед мостом к Лекции 14 — один заключительный урок. Он формулируется через сравнение Cruise и Waymo, которое было исходной рамкой главы.

Cruise и Waymo использовали **сравнимые технологические стеки**. Оба имели лидар + камеры + радар + HD-карту + remote ops backup. Оба работали в Сан-Франциско. Оба прошли California DMV regulatory framework. Оба имели доступ к **практически бесконечному капиталу** материнской корпорации (GM и Alphabet соответственно).

И тем не менее: **Cruise сожгла десять миллиардов и закрылась**. Waymo продолжает рост и делает пятьсот тысяч поездок в неделю. **Различие — не в технологии. Различие — в дисциплине ODD и в отношениях с регулятором**.

Cruise попыталась масштабироваться в SF быстрее, чем валидация ODD позволяла, не была полностью прозрачна с DMV после инцидента октября 2023 года, и доверие было нарушено. После нарушения доверия — независимо от качества технологии — программа не могла продолжаться, потому что регулятор не разрешал.

Waymo масштабируется медленно, методично, sun-belt-city by sun-belt-city, с явной валидацией каждого нового района перед открытием для коммерческой эксплуатации, и с публичной отчётностью о safety. Это **дисциплинированная стратегия**, и она победила в долгосрочной перспективе.

**Lesson инженерного смирения.** AV — это **не arrogance**, это **дисциплина**. Survivors — это те, кто **уважает среду**, **остаётся в narrow ODD**, **не overpromise**, **строит доверие с регулятором перед каждым расширением**. Cruise vs Waymo показывает, что разница между **выжившим и обанкротившимся** часто лежит **не в технологии**, а **в подходе**.

Это **универсальный урок инженерии**, не только AV. Любая сложная инженерная система — авиация, медицинское оборудование, ядерная энергетика, химическое производство, и теперь AV — требует одного и того же: **дисциплина ODD, прозрачность с регулятором, безоговорочный приоритет безопасности над скоростью масштабирования**. Это **дисциплина инженерного смирения**, и она — главный навык, который инженер AI в transport должен освоить.

### §5.5. Мост к Лекции 14: что переносится, что — нет

[for-slide-s40]

Следующая лекция переходит из физического мира в сетевой: телекоммуникации, сетевая инфраструктура, кибербезопасность. Это **другая среда** — cyber вместо physical — и поэтому многие конкретные инструменты, regulatory frameworks, и failure modes будут другими. Cyber-среда имеет своё устройство, которое Лекция 14 раскроет на собственных основаниях, не как «продолжение» нашей лестницы.

Что **переносится** — не таксономия среды (cyber-среда имеет своё устройство, которое Лекция 14 раскроет на собственных основаниях), а **вопросы критического суждения**:

- Где ML работает в-distribution, и где слепо out-of-distribution?
- Где OR / классические алгоритмы / rule-based методы остаются правильным выбором?
- Где human-in-loop обязательна, а где допустима полная автоматизация?
- Как отличить демо от production-proven system? Какие критерии baseline / counterfactual / denominator?
- Когда AI — wrong tool, а правильный — policy / engineering / classical method?

Эти **пять вопросов** — главный takeaway сегодняшней лекции, и они будут применимы и завтра. Что **не переносится** — конкретный список инструментов (Waymo / Aurora / Symbotic не имеют cyber-аналогов), конкретные регуляторные frameworks (NHTSA / FAA / IMO ≠ cyber regulation), и конкретные failure modes (Cruise dragging incident ≠ data breach).

Лекция 14 покажет, как пять вопросов адаптируются к cyber-домену. Ваша задача — слушая её, держать в голове эту лекцию как ground truth для физической логистики, и применять те же критерии к новому материалу, не предполагая, что выводы переносятся механически.

### §5.6. Заключительная мысль

[for-slide-s41]

Главу о AI в логистике и транспорте можно резюмировать одним предложением: **главный предиктор успеха AI в этой области — структурированность среды, а не амбиция стека и не объём капитала**.

В контролируемой среде (склад, порт) AI работает зрело, ROI измеряется, развёртывания массовые. В полуструктурированной (магистраль) — первые коммерческие операции 2025 года, рост медленный, выжившие компании немногочисленны. В городе — Waymo выжил, Cruise разорилась, Tesla только начинает; разница не в технологии, а в дисциплине ODD. В последней миле — узкие ниши, не общее решение. В чёрном лебеде — AI слеп по определению, и инструменты лежат в плоскости operations research, сценарного планирования, классических формул и человека в петле.

Семь критериев «когда AI плохая идея в логистике» — это **набор инструментов** для критической оценки любого AI-предложения в этой области. Каждый критерий имеет конкретный ответ «да или нет», и в каждом случае есть defensible альтернатива. Это **инструментарий инженерного критического суждения**, и его освоение — главная цель главы и одна из главных целей курса в целом.

В следующей лекции мы переходим в другую среду — сетевую. Конкретные инструменты будут другими; критическое суждение — тот же навык. Среда меняется, навык критического суждения — нет.

## Источники

> Источники сгруппированы по категориям. Каждая ссылка реально findable в открытых источниках на момент написания главы (май 2026). Для volatile-цифр и адресов рекомендуется `[VFY-day-of]` re-check на дату использования.

### Регулятивные и государственные документы

1. **NHTSA Standing General Order on Crash Reporting** (2021, обновлено 2024–2026). National Highway Traffic Safety Administration. Mandate сообщения о всех ADAS L2+ и AV L3+ авариях. https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting
2. **NTSB Highway Accident Report HAR-19/03.** Uber Tempe 2018 fatal pedestrian crash investigation. National Transportation Safety Board. https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1903.pdf
3. **SAE J3016 (2021 edition).** «Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.» SAE International.
4. **FAA Part 107.** Small UAS (drone) commercial operations regulations. Federal Aviation Administration.
5. **ICAO Annex 10.** International Civil Aviation Organization — Aeronautical Telecommunications regulatory framework.
6. **IMO Maritime Autonomous Surface Ships (MASS) regulatory framework.** International Maritime Organization phased regulatory development for autonomous shipping, 2018–2026.
7. **EU AI Act (2024).** European Union Regulation on Artificial Intelligence. High-risk category coverage AV applications.
8. **Russian Federation ЭПР (Экспериментальный правовой режим).** Постановление Правительства РФ о пилотной эксплуатации беспилотного транспорта на федеральных трассах.
9. **NHTSA EA22002 investigation documents.** Engineering Analysis on Tesla Autopilot foreseeable misuse and Emergency Vehicle incidents. https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf
10. **NHTSA PE21-020.** Preliminary Evaluation Tesla Autopilot stationary emergency vehicles (August 2021).
11. **FMCSA exemptions** для AV-trucking pilots, 2017–2026 (Aurora, Embark, TuSimple, Plus.ai).
12. **California DMV AV testing and deployment regulations.** Section 38750-38755 of California Vehicle Code.
13. **California DMV Cruise suspension order** (October 24, 2023). Public regulatory document citing «misrepresentation».
14. **BMVI L4-Verordnung** (Germany). Federal regulation for L4 vehicles on approved routes.
15. **KBA approval framework** (Germany). Federal Motor Transport Authority for Mercedes Drive Pilot и Mobileye Chauffeur.

### SEC и регулятивные filings

16. **Cruise / GM impairment disclosure Q4 2024 10-K.** General Motors Form 10-K, Cruise segment financial reporting.
17. **TuSimple SEC delisting filings (January-February 2024).** SEC EDGAR.
18. **Embark Technology Mar 2023 bankruptcy filings.** US Bankruptcy Court filings; SEC closure documentation.
19. **Ford Q3 2022 10-Q.** Argo AI impairment disclosure ($2.7B non-cash impairment).
20. **Volkswagen Group annual report 2022.** Argo AI write-down disclosure.
21. **Symbotic Inc. 10-K FY2024.** Symbotic Walmart contract details, financial reporting. SEC EDGAR.
22. **Aurora Innovation Inc. 10-Q May 2025.** Driverless commercial launch disclosure, cash position. SEC EDGAR.
23. **Pony.ai Holding Inc. 6-K filings (2024–2025).** Unit economics Shenzhen disclosure (338 RMB daily net income per vehicle). SEC EDGAR.
24. **WeRide Inc. 6-K Q3 2025.** Robotaxi revenue 35.3M yuan growth +761% YoY. SEC EDGAR.
25. **Mobileye Global Inc. 10-K FY2024.** Intel subsidiary, SuperVision deployment metrics, Chauffeur roadmap.
26. **Tesla Inc. 10-Q quarterly filings (2024–2025).** Autopilot/FSD revenue, fleet metrics.
27. **SEC TuSimple Schedule 13D** (November 2024). Asset transfer disclosure to Chinese entities. https://www.sec.gov/Archives/edgar/data/0001823593/000092189524002952/ex991to13d14283002_112724.pdf
28. **Wayve Series C/D announcement disclosures** (May 2024, February 2026).

### Корпоративные документы и press releases

29. **Waymo Safety Report 2025.** Annual public safety case document. https://waymo.com/safety/
30. **Waymo geographic expansion press releases 2024–2026.** Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando launch announcements.
31. **Aurora Innovation press release May 2025.** Dallas-Houston commercial driverless launch.
32. **Aurora Innovation crawl-walk-run technical white paper** (2024).
33. **Mobileye Chauffeur announcement** (2024–2025) для Polestar 4 и премиальных европейских OEM.
34. **Mobileye REM (Road Experience Management) white paper.** Crowdsourced HD-map methodology.
35. **Cruise October 2023 incident disclosure documents.** Initial communication к California DMV (partial footage); subsequent full disclosure under regulator pressure.
36. **GM Mary Barra Cruise exit statement** (December 10–11, 2024). Corporate communication.
37. **Apollo Go quarterly operating reports (Baidu).** 240M autonomous km global, 17M cumulative orders.
38. **КамАЗ-54901 М-11 deployment press release** (June 14, 2023 ПМЭФ).
39. **Cognitive Pilot company materials.** Stack architecture, Agro Pilot heritage, M-11 commercial pilot.
40. **Cognitive Pilot Agro reporting (2024).** 590 000 тонн зерновых с >130 000 гектаров.
41. **Pony.ai Robotaxi Shenzhen operating disclosure** (February 2025).
42. **WeRide Nasdaq IPO prospectus** (2024).
43. **Symbotic-Walmart contract expansion press** (January 2025). 400 APD multi-year, backlog +$5B.
44. **Amazon Robotics fulfillment center metrics** (cumulative robots in network annual updates).
45. **Locus Robotics 5B+ picks announcement** (2024).
46. **ABB Marine cargo automation white papers.**
47. **Konecranes container terminal automation case studies.**
48. **ZPMC (Shanghai Zhenhua Heavy Industries) port automation customer references.**
49. **KONUX Deutsche Bahn turnout monitoring case study.**
50. **Starship Technologies milestones press releases** (9M+ deliveries, 2700+ robots, 150+ locations, 60+ universities).
51. **Coco Robotics LA deployment data** (1000+ robots, 500K deliveries).
52. **Zipline annual updates** (100M autonomous miles 2025, 2M commercial deliveries January 2026, $7.6B valuation).
53. **Zipline-US State Department partnership press release** (November 2025).
54. **Nuro pivot announcement 2024** (B2C to licensing).
55. **Boeing 737 MAX MCAS reports** (Lion Air, Ethiopian Airlines, FAA Joint Authorities Technical Review).
56. **Avride launch press releases** (Seoul, Austin food delivery partnerships).

### Trade press и аналитика

57. **TechCrunch Argo AI shutdown coverage** (October 26, 2022). https://techcrunch.com/2022/10/26/ford-vw-backed-argo-ai-is-shutting-down/
58. **CNBC «How Ford and VW's multibillion-dollar self-driving car project failed»** (March 22, 2023). https://www.cnbc.com/2023/03/22/how-ford-and-vws-multibillion-dollar-self-driving-car-project-failed.html
59. **Crunchbase News on Embark closure** (March 2023). https://news.crunchbase.com/transportation/embark-trucks-closes-autonomous-vehicles/
60. **TechCrunch Embark layoffs and liquidation** (March 3, 2023). https://techcrunch.com/2023/03/03/embark-trucks-lays-off-workers-explores-liquidation-of-self-driving-truck-assets/
61. **Reuters TuSimple delisting coverage** (January 2024).
62. **Bloomberg Cruise GM divest analysis** (December 2024).
63. **Wall Street Journal Cruise dragging incident coverage** (October-November 2023).
64. **New York Times Uber Tempe coverage** (March 2018, follow-up 2019–2020).
65. **Financial Times Aurora commercial launch coverage** (May 2025).
66. **CNBC GM Cruise shutdown** (December 15, 2024). https://www.cnbc.com/2024/12/15/end-of-gm-cruise-driverless-robotaxi.html
67. **NPR — GM retreats from robotaxis** (December 11, 2024). https://www.npr.org/2024/12/11/g-s1-37700/gm-to-retreat-from-robotaxis-and-stop-funding-its-cruise-autonomous-vehicle-unit
68. **Smart Cities Dive — GM shuts Cruise** (December 2024). https://www.smartcitiesdive.com/news/general-motors-shuts-cruise-robotaxi-unit-mary-barra/735205/
69. **CNBC Tesla Robotaxi Austin coverage** (June 2025 launch + follow-ups).
70. **National Today — 14 Tesla Robotaxi crashes** (February 2026). https://nationaltoday.com/us/tx/austin/news/2026/02/19/tesla-robotaxis-involved-in-14-crashes-in-austin-since-2025-launch/
71. **Electrek Tesla FSD fatal crash NHTSA investigation** (October 2024). https://electrek.co/2024/10/18/fatal-tesla-crash-with-full-self-driving-supervised-triggers-nhtsa-investigation/
72. **Wikipedia — List of Tesla Autopilot crashes** (continuously updated reference). https://en.wikipedia.org/wiki/List_of_Tesla_Autopilot_crashes
73. **Wikipedia — Death of Elaine Herzberg** (Uber Tempe 2018 reference). https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg
74. **Wikipedia — Tesla Robotaxi** (operational metrics, launch dates). https://en.wikipedia.org/wiki/Tesla_Robotaxi
75. **Wikipedia — 2021 Suez Canal obstruction** (Ever Given incident reference). https://en.wikipedia.org/wiki/2021_Suez_Canal_obstruction
76. **Atlas Institute — Red Sea shipping crisis 2024–2025** (Houthi attacks reference). https://atlasinstitute.org/the-red-sea-shipping-crisis-2024-2025-houthi-attacks-and-global-trade-disruption/
77. **J.P. Morgan Insights — Red Sea shipping impacts.** https://www.jpmorgan.com/insights/global-research/supply-chain/red-sea-shipping
78. **University of Gothenburg — Cost of the Suez Canal blockage analysis.** https://www.gu.se/en/news/the-cost-of-the-suez-canal-blockage
79. **American Trucking Associations — Driver Shortage Report 2024.** https://www.trucking.org/news-insights/ata-releases-updated-driver-shortage-report-and-forecast
80. **Goldman Sachs China robotaxi market report 2025.** Projected $47B by 2035.
81. **McKinsey Future of Mobility 2025.**
82. **McKinsey Supply Chain Resilience 2024.**
83. **BCG transport AI report 2024.**
84. **Deloitte autonomous vehicles industry analysis 2025.**
85. **FreightWaves industry coverage of AV-trucking shutdowns 2023–2024.**
86. **Transport Topics quarterly market reports.**
87. **Robotics & Automation News — Starship milestones coverage.**
88. **Drone Girl Zipline coverage.**
89. **TechCrunch — Waymo growth coverage (2024–2026).**
90. **Carbon Credits / eWeek — Waymo 2025 cumulative metrics.**
91. **ComNews — КамАЗ + Cognitive Pilot M-11 «Нева» coverage.**
92. **IEEE Spectrum — Cognitive Pilot Agro coverage.**

### Академические источники и эссе

93. **Bertsimas, D., Tsitsiklis, J. (1997).** «Introduction to Linear Optimization.» Athena Scientific. Базовый учебник по OR.
94. **Bertsimas, D., Brown, D.B., Caramanis, C. (2011).** «Theory and Applications of Robust Optimization.» SIAM Review 53(3).
95. **Dantzig, G.B. (1954).** «The Traveling-Salesman Problem.» Operations Research 2(4). Founding paper TSP.
96. **Toth, P., Vigo, D. (eds.) (2014).** «Vehicle Routing: Problems, Methods, and Applications.» SIAM. VRP handbook reference.
97. **Bellman, R. (1957).** «Dynamic Programming.» Princeton University Press. Foundational text для DP applications в логистике.
98. **Russell, S., Norvig, P. (2021).** «Artificial Intelligence: A Modern Approach» (4th ed.). Pearson. RL chapter reference для OR vs RL comparison.
99. **Sutton, R.S., Barto, A.G. (2018).** «Reinforcement Learning: An Introduction» (2nd ed.). MIT Press.
100. **Hopp, W.J., Spearman, M.L. (2000, updated editions).** «Factory Physics.» McGraw-Hill. Little's Law, queueing theory для inventory + production planning.
101. **Stefan Seltz-Axmacher (March 2020).** «The end of Starsky Robotics.» Medium. https://medium.com/starsky-robotics-blog/the-end-of-starsky-robotics-acb8a6a8a5f5 — Personal essay основателя обанкротившегося AV-trucking startup. **Must-read for every AV-engineer.**
102. **Anca Dragan papers on AV-human interaction** (UC Berkeley research, 2018–2024). Game-theoretic safety models для interaction between AV and human drivers.
103. **Chris Urmson Aurora founder essays** (Medium, 2017–2024). Public reflections от Aurora CEO on AV industry direction.
104. **Waymo Safety Methodologies paper** (2020, обновлено). Formal safety case framework.
105. **Mobileye Responsibility-Sensitive Safety (RSS) whitepaper** (Shalev-Shwartz, Shashua, 2017). Mathematical framework для defining «safe driving». https://www.mobileye.com/responsibility-sensitive-safety/
106. **MIT Mobility of the Future report** (multi-year program reports).
107. **Pierre Wack — Shell scenario planning methodology** (Harvard Business Review reprint articles, 1985).
108. **PennLive / University of Pennsylvania — trucker real wage research** (2019).

### Industry analyst reports

109. **Frost & Sullivan AV market reports.**
110. **ABI Research warehouse robotics analysis.**
111. **Interact Analysis last-mile delivery reports.**
112. **LogisticsIQ supply chain technology market sizing.**
113. **Gartner Hype Cycle Mobility 2025.**
114. **Forrester transport AI 2024.**
115. **IDC supply chain technology 2025.**
116. **CB Insights AV startup tracking (2017–2026).**
117. **PitchBook AV venture analysis.**
118. **S&P Global automotive industry analysis (chip shortage impact).**
119. **J.D. Power AV consumer studies.**
120. **AAA Autonomous Vehicle public acceptance surveys.**
121. **Insurance Institute for Highway Safety (IIHS) AV crash data analysis.**
122. **Center for Auto Safety reports на Tesla Autopilot.**
123. **Consumer Reports Tesla Autopilot testing methodology and findings (2021–2025).**
124. **Statista last-mile cost percentage data 2018–2023.**

### Russian and CIS context references

125. **КамАЗ Press Service materials** (2023–2026). Autonomous КамАЗ-54901 deployment.
126. **Cognitive Pilot annual reports** (2023–2025).
127. **Yandex SDG 2024 split announcement** (sanctions-related entity restructuring).
128. **Sberlogistics automation press releases.**
129. **Wildberries automation case studies.**
130. **Russian Association of Trucking Companies (RATC) driver shortage report 2024.**
131. **Avride launch press materials** (post-Yandex spin-off, 2024).
132. **М-11 «Нева» и М-12 «Восток» — Госкомпания «Автодор» technical documentation.**
133. **ЭПР (Experimental Legal Regime) — постановления Правительства РФ** для беспилотного транспорта.
134. **Автостат — данные по российскому парку грузовых автомобилей** (2024).

### Open-source toolchain references

135. **Google OR-Tools documentation.** https://developers.google.com/optimization
136. **Gurobi Optimizer documentation.** https://www.gurobi.com/documentation/
137. **IBM CPLEX optimization studio.**
138. **INFORMS Impact: O.R. & Analytics Success Stories — UPS ORION case study.** https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/Optimizing-Delivery-Routes
139. **Apollo open-source autonomous driving platform** (Baidu). https://github.com/ApolloAuto/apollo
140. **Autoware open-source autonomous driving platform** (Tier IV, Tokyo University).

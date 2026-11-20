---
title: "Верифицированные внешние кейсы — Лекция 5 (product-lifecycle), волна 3 (batch 2)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 5 (product-lifecycle) — волна 3, усиление реестра (batch 2)

## Подход к поиску и честный итог

Это **третья** волна поиска по Лекции 5, после волны 1 (`verified-cases/lec-05-verified.md`,
19 кейсов) и независимо идущей волны про 2026 год. Тема взята широко, как задано оркестратором:
demand forecasting, PLM, ценообразование, рецептура/формуляция, генеративный дизайн продукта —
**не** узкая тема самой главы лекции 5 (которая про жизненный цикл AI-продукта-как-софта;
см. `reestr-reshenij.csv` lecture_num=5, 32 исходных кейса — ни один из них не пересекается с
темой этого файла, проверено построчно по `case_name`, см. ниже).

**Задача:** закрыть дефицит успешных кейсов волны 1 (там — только 4 успеха из 10 запрошенных) и
нарастить общую выборку. **Результат: 25 новых кейсов, ни один не дублирует 19 кейсов волны 1**
(список дан оркестратором явно и проверен построчно) **и не дублирует 32 исходных кейса
`lecture_num=5` реестра** (домены не пересекаются — там софт/чат-боты/легал-ИИ, здесь
ценообразование/рецептура/физический дизайн).

**Метод:** открытый WebSearch (≈24 запроса, до истощения общего лимита сессии — лимит общий на
все параллельные сессии волны, исчерпан в процессе работы, как и в волне 1) + после истощения —
WebFetch первоисточников и Wikipedia напрямую, плюс прямой `curl` там, где WebFetch получал 403
(урок `feedback-two-numbers-check-the-base` / правило курса «источника не существует по
отрицательному ответу WebFetch — проверяй прямым чтением» применено: минимум 4 кейса в этом
файле подтверждены именно прямым `curl`, а не WebFetch-пересказом).

**Итог по составу: 15 успех / 3 частично-смешанных / 3 неопределённых / 4 провал.** Успешная
корзина в этой волне — **самая большая во всём корпусе Лекции 5** (15 новых успехов против 4 у
волны 1), что прямо отвечает на запрос оркестратора «закрыть недостающие успешные кейсы». Это не
означает, что индустрия продуктового ИИ в среднем успешна чаще, чем провальна — это означает, что
при целенаправленном поиске именно успехов (рецептура/генеративный дизайн потребительских товаров,
где вендоры активно публикуют кейс-стади) находится много material, тогда как антитраст/ценовые
провалы (уже перевыполненные в волне 1) более одноразовые и громкие, а не частые.

**Качество источников — неоднородное, и это не скрыто.** 7 из 25 кейсов опираются на единственный
вторичный источник (трейд-пресса/блог) без независимого подтверждения — отмечено `confidence=low`
по каждому индивидуально, не усреднено. Один кейс (L'Oréal Perso/YSL) подтверждён фактом
прекращения поддержки **только личным техническим блогом**, не пресс-релизом — явно помечено как
риск, не скрыто под общим средним качеством.

## Покрытие по годам

| Год | Успех | Частично/неопределённо | Провал |
|---|---|---|---|
| 2018 | GM×Autodesk (кронштейн сиденья, май); Carbon×Riddell Diamond (сезон NFL); Il Makiage PowerMatch (релонч) | — | — |
| 2019 | McCormick×IBM «ONE» (запуск); IBM×Symrise×O Boticário Philyra (Egeo On Me/You) | — | — |
| 2020 | Climax Foods (seed-раунд, сент.) | — | — |
| 2021 | Firmenich Scentmate (запуск, июнь); Carbon×Adidas 4DFWD (релиз, авг.) | Danone×Brightseed (расширение партнёрства, авг.) | — |
| 2022 | NotCo×Kraft Heinz (СП) | — | — |
| 2023 | — | — | Немецкий бензиновый рынок (публикация исследования); Yardi (иск подан, сент.) |
| 2024 | Fetcherr×Azul (масштабирование); Meati×PIPA; Climax Foods (шеф-адопция) | — | Kroger ESL (письмо сенаторов, авг.) |
| 2025 | Analytical Flavor Systems→NielsenIQ (приобретение, апр.) | FIFA Club World Cup (турнир); Cadence Cerebrus (анонс); FTC surveillance pricing study (янв.) | — |
| 2026 | — | — | L'Oréal Perso/YSL (прекращение поддержки, февр.); Yardi (дело сужено, март) |
| дата не названа источником | Mondelez×Oreo; PepsiCo×Propel; FlavorMind; Shake Shack×NotCo (оценка года — см. оговорку по качеству источников) | — | — |

## Кейсы с успешным исходом (15)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | GM × Autodesk — генеративный дизайн кронштейна сиденья | 2018 | https://www.repairerdrivennews.com/2018/05/23/gm-autodesk-software-allows-artificial-intelligence-to-design-innovative-light-auto-parts/ | Облачный генеративный алгоритм (Autodesk) сгенерировал сотни вариантов, итог — кронштейн на 40% легче, на 20% прочнее, 8 деталей объединены в одну, напечатанную на 3D-принтере (май 2018) | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | medium |
| S2 | Carbon × Riddell — Diamond, вычислительно оптимизированный латтис-вкладыш шлема | 2018 | https://www.carbon3d.com/news/press-releases/riddell-carbon-produce-football-helmet | Carbon Lattice Engine проектирует индивидуализированный латтис-вкладыш (140 000+ стоек) на основе базы 5 млн ударов smart-шлемов Riddell; шлемы Diamond использовались игроками NFL в сезоне 2018, коммерчески доступны с 2019 | moderate | none | weeks-months | none | classical-ml | yes | medium | not-applicable | success | medium |
| S3 | Il Makiage — PowerMatch, AI-подбор оттенка тона кожи | 2018 | https://en.wikipedia.org/wiki/Il_Makiage | При релонче бренда (2018) внедрён алгоритм PowerMatch для AI-подбора оттенка тона по фото/квизу; Wikipedia связывает алгоритм с быстрым ростом и международной экспансией — без цифр | moderate | none | seconds-minutes | none | classical-ml | not-applicable | low | not-applicable | success | low |
| S4 | McCormick × IBM — AI-платформа «ONE» | 2019 | https://venturebeat.com/technology/ibm-and-mccormick-stir-new-spice-blends-with-ai | IBM Research AI for Product Composition анализирует 40 лет вкусовых данных McCormick; платформа «ONE» запущена в середине 2019 (Tuscan Chicken, Bourbon Pork Tenderloin), разработка в ~3 раза быстрее | moderate | none | weeks-months | none | hybrid | yes | low | not-applicable | success | medium |
| S5 | IBM Research × Symrise × O Boticário — Philyra, AI-парфюм | 2019 | https://www.symrise.com/newsroom/article/breaking-new-fragrance-ground-with-artificial-intelligence-ai-ibm-research-and-symrise-are-workin/ | AI-модель Philyra анализирует базу парфюмерных формул и предлагает новые комбинации; парфюмер Symrise доработал предложения; O Boticário выпустил Egeo On Me/On You — заявлены как первые «AI-powered fine fragrances» (2019) | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | medium |
| S6 | Climax Foods — Deep Plant Intelligence, растительные сыры | 2020 | https://www.fooddive.com/news/climax-foods-raises-75m-to-improve-plant-based-food-using-ai/584463/ | AI-платформа анализирует растительные ингредиенты на молекулярном уровне для замены сыра/казеина ($7,5M seed, сент. 2020); к 2024 — сыры Blue/Brie, принятые шеф-поваром с мишленовской звездой Dominique Crenn | moderate | none | season-years | none | classical-ml | yes | low | not-applicable | success | medium |
| S7 | Firmenich — Scentmate, AI-платформа создания аромата | 2021 | https://www.cosmeticsdesign-europe.com/Article/2021/07/01/Firmenich-Scentmate-AI-fragrance-tool-aims-to-empower-Indie-beauty-brands/ | AI-платформа Scentmate (запуск 24 июня 2021, только Европа) сокращает брифинг аромата с недель до минут для независимых брендов; curated предложения парфюмеров + ИИ, доставка образца за 48 часов | low | none | hours-days | none | hybrid | yes | low | not-applicable | success | medium |
| S8 | Carbon × Adidas — 4DFWD, data-driven генеративный латтис-мидсоль | 2021 | https://3dprintingindustry.com/news/adidas-and-carbon-unveil-latest-4d-midsole-4dfwd-to-bolster-running-performance-189558/ | Carbon Design Engine оценил 5 млн вариантов решётки по 18 годам данных реальных атлетов; выбранная bowtie-форма снижает пиковую тормозящую силу на 15%, втрое больше движения вперёд; релиз 12 авг. 2021 | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | medium |
| S9 | NotCo (Giuseppe AI) × Kraft Heinz — совместное предприятие | 2022 | https://corporateknights.com/food-beverage/ai-notco-plant-based-takeover-big-food/ | AI-алгоритм Giuseppe анализирует молекулярные свойства >300 000 растений; СП «The Kraft Heinz Not Company» (2022) разработало растительный mac&cheese за 8–10 мес. вместо оценочных 24; выпущены NotMac&Cheese, NotCheese Slices, NotMayo, Oscar Mayer NotHotDogs/NotSausages | moderate | none | season-years | none | hybrid | yes | low | not-applicable | success | medium |
| S10 | Fetcherr × Azul Airlines — первое масштабированное generative AI-ценообразование | 2024 | https://www.fetcherr.io/blog/dynamic-pricing-in-aviation | «Large Market Model» (генеративный ИИ) Fetcherr развёрнута Azul как первым «живым» клиентом; вендор заявляет «первую в мире полностью масштабированную систему генеративного ИИ-ценообразования» без публичного скандала (контраст с Delta/Wendy's из волны 1); $90M Series B привлечено в июне 2024 | high | none | seconds-minutes | F-C | foundation-model | no | medium | not-applicable | success | low |
| S11 | Meati Foods × PIPA — AI-оптимизация мицелиевой альтернативы мясу | 2024 | https://vegnews.com/ai-vegan-companies | Партнёрство с AI food-science компанией PIPA анализирует данные о свойствах мицелия для увеличения белка и снижения натрия в «цельнокусковых» стейках/котлетах Meati | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | low |
| S12 | Analytical Flavor Systems (Gastrograph AI) — приобретение NielsenIQ | 2025 | https://endlessfrontierlabs.com/startups/gastrograph/ | AI-платформа Gastrograph моделирует сенсорное восприятие вкуса/аромы/текстуры по данным из 16 стран; в апреле 2025 компания приобретена NielsenIQ для усиления AI-продуктовых инноваций — успешный коммерческий exit | moderate | none | season-years | none | classical-ml | not-applicable | low | not-applicable | success | medium |
| S13 | Mondelez — ML-ассистированная разработка рецепта Oreo | 2019 (оценка) | https://www.foodprocessing.com/product-development/article/55291643/big-and-small-ai-aids-product-development | Модель машинного обучения (разработана внутри Mondelez Alexia Ciarfella) ускорила перебор рецептурных прототипов печенья Oreo, сократив время итерации прототипа на 33%; точная дата не названа источником, оценена по контексту (до основания FlavorMind) | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | low |
| S14 | PepsiCo — AI-анализ соцсетей → линейка Propel | 2021 (оценка) | https://www.ift.org/food-technology-magazine/how-ai-is-revolutionizing-product-development | AI-инструмент проанализировал миллионы постов в соцсетях, выявив тренд на «иммунную поддержку»; на основе находки расширена линейка воды Propel; точная дата не названа источником | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | low |
| S15 | FlavorMind — AI-платформа реформуляции (сахар/отходы) | 2022 (оценка) | https://www.foodprocessing.com/product-development/article/55291643/big-and-small-ai-aids-product-development | AI-платформа (основана экс-разработчиком Mondelez) переформулировала тропический смузи со снижением сахара при сохранении вкуса и оптимизировала использование шпината в линейке продуктов, снизив отходы от порчи; клиент(ы) и точная дата не названы | moderate | none | weeks-months | none | classical-ml | yes | low | not-applicable | success | low |

## Кейсы со смешанным/неопределённым исходом (6)

Честно не форсированы в «успех»/«провал» — источники сами описывают незавершённый, расходящийся
или структурный (не привязанный к одному продукту) результат.

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Danone × Brightseed — Forager AI, расширенное партнёрство | 2021 | https://www.fooddive.com/news/danone-expands-partnership-with-ai-firm-brightseed-to-explore-health-benefi/604526/ | AI-платформа Forager выявила в 10 раз больше биоактивных соединений в растительном сырье Danone, чем было известно, и 7 новых «областей здоровья»; партнёрство расширено (авг. 2021) к цели утроить продажи растительных продуктов к 2025 — но выпущенный на рынок продукт на основе находок не подтверждён проверенным источником | high | none | season-years | none | classical-ml | yes | low | not-applicable | partial | medium |
| P2 | FIFA Club World Cup 2025 — динамическое ценообразование билетов | 2025 | https://en.wikipedia.org/wiki/2025_FIFA_Club_World_Cup | Продажа билетов турнира велась по динамическому ценообразованию, которое организаторы были вынуждены скорректировать на нескольких матчах прямо по ходу турнира для повышения посещаемости; конкретный ИИ-механизм источником не назван | unclear | unclear | hours-days | F-C | unclear | unclear | medium | mixed | partial | low |
| P3 | Cendyn/Rainmaker — алгоритмическое ценообразование отелей-казино, антитраст circuit split | 2023–2026 | https://www.paulweiss.com/insights/client-memos/third-circuit-revives-algorithmic-pricing-antitrust-claims-against-casino-hotels | ПО Rainmaker (Cendyn) агрегирует непубличные данные о ценах/занятости отелей Лас-Вегаса и Атлантик-Сити и рекомендует тарифы; 3-й округ (июль 2026) восстановил иск по Атлантик-Сити (hub-and-spoke), 9-й округ (авг. 2025) подтвердил отказ по похожему делу о Лас-Вегасе, Верховный суд США отклонил пересмотр дела о Лас-Вегасе — расходящийся исход между округами | moderate | none | hours-days | F-C | classical-ml | unclear | medium | yes | partial | high |
| U1 | Cadence Cerebrus — agentic AI для дизайна чипов | 2025 | https://en.wikipedia.org/wiki/AI-driven_design_automation | Cadence анонсировала (2025) AI-платформу Cerebrus/Cadence.ai для оптимизации цифрового дизайн-флоу чипов (аналог Synopsys DSO.ai из волны 1, S4); в отличие от DSO.ai («100+ коммерческих чипов к 2023»), конкретные метрики внедрения или выпущенные на базе инструмента чипы не раскрыты | moderate | none | unclear | none | agentic-llm | unclear | unclear | not-applicable | undetermined | low |
| U2 | FTC — исследование surveillance pricing (6(b) study) | 2025 | https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-surveillance-pricing-study-indicates-wide-range-personal-data-used-set-individualized-consumer | FTC изучила документы 6 посредников (Mastercard, Accenture, PROS, Bloomreach, Revionics, McKinsey), работающих с ≥250 клиентами ритейла; выявлено систематическое использование геолокации, движений мыши, брошенных корзин для индивидуального ценообразования (напр. косметика по типу кожи, детские товары — выше цена «новым родителям») — структурный кейс без привязки к одному продукту/исходу | unclear | unclear | unclear | unclear | classical-ml | no | high | yes | undetermined | high |
| U3 | Shake Shack × NotCo — безъяичная заварная основа | 2022 (оценка) | https://www.foodprocessing.com/product-development/article/55291643/big-and-small-ai-aids-product-development | Giuseppe AI применён для разработки безъяичной заварной (custard) основы для десертов Shake Shack; коммерческий результат (запуск, продажи) не указан источником | unclear | unclear | unclear | unclear | hybrid | unclear | unclear | unclear | undetermined | low |

## Кейсы с провальным исходом (4)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | Yardi (RENTmaximizer/Revenue IQ) — nationwide антитраст иск о фиксации арендной платы | 2023–2026 | https://www.multifamilydive.com/news/yardi-rent-pricing-antitrust-case-narrowed-washington/816504/ | ПО Yardi Revenue IQ (ранее RENTmaximizer) обвиняется в обмене непубличными конкурентно-чувствительными данными между арендодателями через алгоритм; иск подан сент. 2023, в дек. 2024 судья разрешил делу продолжаться («методы фиксации цен развивались вместе с технологией»), тестовый анализ показал среднюю надбавку 6% в некоторых почтовых индексах; в марте 2026 из дела исключены 10 внестатных управляющих компаний, но Yardi и вашингтонские операторы остаются ответчиками | moderate | none | season-years | F-B | classical-ml | no | high | no | failure | high |
| F2 | Алгоритмическое ценообразование на немецком рынке автозаправок — эмпирически подтверждённый tacit collusion | 2023 (публикация; софт с 2017) | https://discovery.ucl.ac.uk/id/eprint/10187765/1/draft_v15_JPE_main.pdf | Первое эмпирическое исследование внедрения алгоритмического ценообразования (ПО массово доступно с 2017) на немецком рынке бензина (Assad, Clark, Ershov, Xu); адопция повышает маржу на немонопольных станциях, а в дуополиях/триополиях маржа растёт только если ВСЕ станции рынка внедрили ПО — прямое эмпирическое доказательство способности алгоритмов обучаться тактическому сговору без явной координации | moderate | none | hours-days | F-C | classical-ml | no | high | no | failure | high |
| F3 | Kroger — электронные ценники и обвинения в «surge pricing», расследование сенаторов | 2024 | https://www.grocerydive.com/news/kroger-electronic-shelf-labels-instore-technology-senators-inflation/723939/ | Сенаторы Уоррен и Кейси (авг. 2024) направили письмо Kroger с обвинением, что электронные ценники (EDGE Shelf, с камерами и Microsoft facial recognition) готовят почву для «surge pricing» на базовые товары; Kroger публично отверг обвинение («никогда не занимались surge pricing»), но репутационный и политический ущерб остались | low | none | hours-days | F-C | unclear | no | medium | yes | failure | medium |
| F4 | L'Oréal Perso / YSL Rouge Sur Mesure — AI-устройство для подбора косметики, прекращение поддержки | 2020 (запуск) → 2026 (прекращение) | https://smallwat3r.com/blog/ysl-rouge-sur-mesure | AI-устройство Perso (анонс CES янв. 2020, запуск как YSL Rouge Sur Mesure янв. 2021) смешивает персонализированную помаду/skincare по ИИ-рекомендациям; в февр. 2026 L'Oréal прекратил поддержку приложения, без которого устройство не функционирует — рабочее железо осталось «кирпичом» через привязку к устаревающему софту | low | none | season-years | none | hybrid | not-applicable | low | no | failure | low |

## Замеченные противоречия и сигналы для рамки курса

- **Самый большой перекос этого файла по сравнению с волной 1 — именно в успешной корзине, и
  это намеренная коррекция, а не случайная находка.** 15 успехов этой волны почти целиком лежат в
  рецептуре/формуляции (food-tech, fragrance) и генеративном физическом дизайне (обувь, шлемы,
  автодетали) — областях, где **вендор публикует кейс-стади по умолчанию**, в отличие от
  ценообразования (почти всегда либо скрытое внутреннее «incredible success», либо публичный
  провал/иск). Это системное смещение источника, не распределения исходов в индустрии в целом —
  честно повторяет предупреждение волны 1 про тот же паттерн.
- **Ось 4 (гейт) снова — сильнейший предиктор, и снова с тем же уточнением, что в волне 1.** Во
  всех 4 чистых провалах этого файла (F1–F4) `axis4_gate=no` — отсутствие эффективного
  антимонопольного/регуляторного/репутационного контроля ДО или ВО ВРЕМЯ развёртывания, а не
  проблема самой ML-задачи (`axis1_mechanism=none` у всех четырёх). Немецкое исследование
  бензиновых цен (F2) особенно ценно методически: это **не единичный кейс одной компании**, а
  рыночный эксперимент на тысячах заправок, который прямо показывает, что сам факт «у алгоритма
  нет злого умысла, он просто учится оптимизировать» — не защита: тактический сговор возник без
  явной координации, просто из локальной оптимизации каждого актора.
- **Контраст Fetcherr/Azul (S10) vs Delta/Wendy's (волна 1, F3/F4) — тот же механизм
  ценообразования, разный результат, и разница — не в алгоритме.** Delta и Wendy's анонсировали
  планы AI-ценообразования публично и получили немедленный политический/медийный откат; Azul
  развернула концептуально такую же генеративную систему ценообразования без объявленного
  публичного скандала. Разница, по доступным источникам, — не в технологии (одна и та же Large
  Market Model Fetcherr), а в том, что Delta/Wendy's явно анонсировали персонализацию КОНЕЧНОМУ
  потребителю как публичную инициативу, тогда как авиационное динамическое ценообразование и так
  исторически нормализовано (ось 4 здесь — скорее «ожидания аудитории», чем формальный гейт).
  Это ценная методическая оговорка: **один и тот же `axis3_class=foundation-model` механизм
  ценообразования даёт разный исход в зависимости от того, насколько рынок УЖЕ привык к
  волатильности цены этого товара** — переменная, которую три формальные оси курса не фиксируют
  напрямую.
- **U1/U2 (Cadence Cerebrus, FTC-исследование) — два разных типа «неопределённости исхода», и
  их не стоит путать.** Cadence Cerebrus неопределён, потому что **вендор пока не раскрыл
  метрики** (может быть успехом, может не быть — просто рано). FTC-исследование неопределённо,
  потому что оно **структурное** — не про один продукт с одним исходом, а про целую практику
  индустрии (250+ клиентов посредников), и форсировать единый `outcome` для целой практики было
  бы той же ошибкой, которую волна 1 уже избегала с Mattel×OpenAI (B3).
- **F4 (L'Oréal Perso) — повторяет паттерн F7/F8 волны 1 (Local Motors, IBM Watson Health):
  AI-механизм работал как задумано (устройство смешивало персонализированные формулы), провал —
  в выборе хрупкой программной зависимости (app-locked hardware), не в самой ML-задаче.**
  Отдельная методическая ценность: единственный источник, подтверждающий сам факт прекращения —
  личный технический блог, не пресс-релиз L'Oréal/YSL — что объясняет `confidence=low`, а не
  `medium`, несмотря на то что запуск устройства подтверждён официальным пресс-релизом L'Oréal.

## Оговорка по качеству источников (обязательна к учёту)

- **Высокое качество (первичные источники, прочитаны напрямую):** F1 (прямое чтение судебного
  таймлайна через multifamilydive.com с датами и номерами дел), F2 (PDF академической статьи
  прочитан напрямую через `pdftotext`-эквивалент (`pymupdf`), аннотация и метод процитированы
  verbatim), U2 (официальный пресс-релиз FTC), P3 (юридическая аналитика Paul Weiss + Bloomberg
  Law с точными датами постановлений по округам).
- **Среднее качество (авторитетная отраслевая пресса/вендорские пресс-центры без третьего
  независимого аудита):** S1 (repairerdrivennews.com, подтверждён через WebFetch), S2
  (carbon3d.com — подтверждён прямым `curl` после 403 на WebFetch), S4–S9 (venturebeat.com, symrise.com, fooddive.com,
  cosmeticsdesign-europe.com, 3dprintingindustry.com, corporateknights.com), S12 (две независимые
  вторичные venture/accelerator-страницы, не пресс-релиз NielsenIQ напрямую), F3 (grocerydive.com
  + официальное письмо сенаторов, которое не удалось зафетчить напрямую из-за блокировки сайта
  senate.gov, но содержание подтверждено идентично в двух независимых пересказах).
- **Низкое качество/осознанно принятый риск:** S3 (Il Makiage) — Wikipedia как единственный
  источник, без количественных метрик роста. S10 (Fetcherr×Azul) — вендорский блог + формулировка
  «world's first» без независимой проверки; метрика «10% revenue uplift over three years» в
  источнике явно обобщённая, не Azul-специфичная — не включена в описание кейса намеренно.
  S11, S13–S15, U3 — единственный источник (foodprocessing.com/vegnews.com, трейд-пресса),
  **даты для S13–S15 и U3 — не названы источником напрямую и оценены по контексту** (явно
  помечено словом «оценка» в колонке year); это тот же класс риска, от которого волна 1
  явно отказалась для Zara/Walmart, но здесь компания и механизм достаточно конкретно названы
  (в отличие от отброшенных в волне 1 кандидатов), поэтому решено включить с `confidence=low`,
  а не отбросить — методическое отличие явно: там не находилось НИ ОДНОГО упоминания на
  официальных страницах компаний, здесь конкретный факт (кто, что, как) подтверждён отдельной
  отраслевой публикацией, просто без даты. F4 (L'Oréal Perso) — факт прекращения поддержки
  подтверждён только личным блогом; попытки найти официальное подтверждение (прямой `curl` на
  warren.senate.gov и поиск через Bing/DuckDuckGo) заблокированы anti-bot защитой сайтов —
  зафиксировано как техническое ограничение, не как основание отбросить кейс (сам факт запуска
  устройства и его архитектурной зависимости от приложения подтверждён официальными источниками
  L'Oréal/YSL, под вопросом только точная дата и факт прекращения).
- **Явно отброшенные кандидаты (не вошли в файл вообще):** Suntory AI-блендинг виски (не
  подтверждено ни одним источником при проверке — неверная память/галлюцинация, отброшено, не
  процитировано); Philips Sonicare × Autodesk generative design (ни один источник не подтвердил
  существование такого кейс-стади); McLaren F1 × Autodesk generative design брейк-дакта (найдена
  только общая формулировка о сотрудничестве без привязки к конкретной детали — отброшено как
  недостаточно специфичное); Zillow Offers/Zestimate и McDonald's×IBM — не кандидаты вовсе, это
  уже существующие строки исходного реестра `lecture_num=5` (L05-024, L05-014), не новые находки;
  Hackrod «La Bandita» и Volkswagen Type 20 — нет статьи Wikipedia, прямую первичную ссылку найти
  не удалось после истощения WebSearch, решено не включать по памяти без проверки (прямой урок
  курса: «источник не цитируется по памяти без проверки»); BCD iLabs «Innov8 OS» — упомянут в
  источнике без названия клиента-компании, не прошёл критерий «именованный, проверяемый кейс»;
  Function of Beauty (персонализированный AI-уход за волосами) — WebSearch истощился до
  подтверждения деталей, Wikipedia-страницы не существует, отброшен без замены по памяти.

---
title: "Внешне верифицированные кейсы — Лекция 10 (agriculture) — копия для discoverability"
source: "notes/research/osi-primenimosti-ii/verified-cases/lec-10-verified.md"
issue: "#349"
status: research-backup, not-reviewed
date_copied: 2026-11-20
---

> **Происхождение.** Это внешне верифицированное свидетельство реальных кейсов (деплойменты/
> исследования с явным исходом, метрикой, датой и именованным инструментом, 2018–2026),
> собранное в рамках research-задачи issue #349 (`notes/research/osi-primenimosti-ii/`).
> Это дополнительный справочный материал для deep-dive главы / backup для Q&A / самостоятельного
> изучения — **не методическая критика и не fact-check лекционного контента**: не прошло ревью
> `methodology-critic` или `fact-checker` как материал лекции, и **не заменяет собственные кейсы
> главы**, если только человек-редактор не решит сознательно включить конкретный кейс в
> `chapter.md`.
>
> Копия ниже — точная (verbatim) копия
> `notes/research/osi-primenimosti-ii/verified-cases/lec-10-verified.md` для обнаруживаемости из
> папки лекции; каноническая версия и её история — в `notes/research/`.

---

---
title: "Лекция 10 (agriculture) — независимо верифицированные кейсы, свежий веб-поиск"
type: research
issue: "#349"
date: 2026-11-20
lecture_num: 10
industry: agriculture
---

# Лекция 10 (agriculture) — верифицированные кейсы (независимый поиск, не из слайдов лекции)

## Подход к поиску

Весь материал ниже получен сегодня через `WebSearch`/`WebFetch` — ни один кейс не переписан из
`razmetka/lec-10.md` или слайдов лекции (хотя несколько названий вендоров неизбежно пересекаются
с реестром — AgTech-рынок маленький; в каждом таком случае ниже явно отмечено, что числа/источник
взяты заново, а не скопированы). Поиск вёлся по кластерам: (1) банкротства/закрытия vertical
farming 2022-2026, (2) автономная техника (тракторы, прополка, спрей), (3) генеративный ИИ для
фермеров-консультаций, (4) академические работы по прогнозу урожайности, (5) точечные попытки
закрыть пробелы по годам 2022 и 2026.

**Ограничение по бюджету.** Лимит `WebSearch` на сессию (200 вызовов) был исчерпан в процессе —
после этого добор шёл через `WebFetch` по уже известным URL и Wikipedia/SEC/arXiv напрямую.
Несколько попыток (Small Robot Company, Taranis wiki-страница, Hummingbird Technologies,
AGCO/Monarch Tractor newsroom, Climate Corporation современные метрики) не дали проверяемого
результата — соответствующие кандидаты не включены в таблицу, а не притянуты силой.

**Покрытие по годам — честно неполное.** 2023-2025 покрыты плотно (по 5-6 кейсов на год). **2022
— только один кейс** (и это кейс с интерпретативной, не дословной формулировкой провала — см.
примечание в таблице). **2026 — только один кейс**, и это академическая публикация с датой года,
выведенной из номера тома журнала (не подтверждённой напрямую через сам текст статьи — MDPI
`agriculture16050516` отдал HTTP 403 на прямой фетч). Отдельный кейс, PlantVillage Nuru, **лежит
вне окна 2022-2026** (опубликован 2020) — оставлен в таблице как кейс с лучшей независимой
(peer-reviewed, полевой) верификацией точности диагностического ИИ в сельском хозяйстве, который
удалось найти, с явной пометкой об исключении из окна.

## Честный недобор по корзине «успех»

Требование — ≥10 явно успешных кейсов. **Найдено и уверенно верифицировано 7.** Не досчитано 3.
Причина не в том, что успешных AI-кейсов в агротехе не существует (их много), а в том, что
большинство найденных формулировок — либо (а) без конкретной цифры/даты (общие обзорные статьи
про «69% adoption, 95%+ accuracy» без названного инструмента — отброшены как слишком общие), либо
(б) совпадали с источником, который при перепроверке давал другую цифру, чем первый
синтез-ответ `WebSearch` (см. случай с «corn R²=0.90/soybean R²=0.75» ниже — при прямой проверке
через `arXiv` эта цифра не подтвердилась ни в одном из проверенных препринтов и была отброшена,
а не вставлена). Решение — показать недобор явно, а не растянуть эти два источника до статуса
отдельных кейсов. Обе категории провала (10/10) выполнены без такого компромисса.

## Качество источников — по кейсу, не усреднённо

- **SEC 8-K (Valmont/Prospera)** — первичный регуляторный документ, самый сильный источник во
  всей таблице.
- **Судебные/пресс-материалы о банкротствах** (AeroFarms, AppHarvest, Infarm, Plenty, Bowery,
  FarmWise, Iron Ox) — высокое качество, но все вторичные (деловая пресса, не первичные судебные
  документы, кроме точек, где явно указан Bloomberg Law).
- **Академические препринты/журналы** (ADS 2023, MDPI 2026, arXiv RicEns-Net 2025) — качество
  методологии выше, но единичные исследования без независимой репликации; MDPI-кейс — год не
  подтверждён напрямую.
- **Вендорские пресс-релизы** (Verdant Robotics, Carbon Robotics) — наименее надёжный класс здесь:
  цифры эффекта («-96% химикатов», «250k акров») не из независимого аудита. Помечено `confidence:
  medium`, а не `high`.
- **Интерпретативные кейсы** (Raven/Smart Ag, Deere-2022) — это два случая, где сам источник не
  произносит слово «провал»; вывод о провале — моя собственная аналитическая интерпретация разрыва
  между заявленным и фактическим. Понижены до `confidence: low`/`medium` соответственно и отмечены
  как таковые в колонке примечаний.

## Таблица кейсов

### Провал / не-успех (10 обязательных + 1 доп.)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | AeroFarms — Chapter 11 | 2023 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | yes | Подала на банкротство 8 июня 2023 (после отмены SPAC-сделки в 2022); $238M привлечённых средств; вышла из процедуры в сентябре 2023, продав себя кредиторам/инвесторам за $500k + списание $32M долга. | [Bloomberg Law](https://news.bloomberglaw.com/bankruptcy-law/aerofarms-bankruptcy-plan-approved-following-sale-to-lenders), [just-food](https://www.just-food.com/news/aerofarms-moves-toward-chapter-11-bankruptcy-to-secure-survival/) |
| F2 | Infarm — неплатёжеспособность в Европе | 2023 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | yes | Объявила неплатёжеспособность в Великобритании (4 сент. 2023, Administration) и Нидерландах (19 сент. 2023); ушла со всех европейских рынков в 2023; потеряно >$600M привлечённого капитала за 10 лет; причина — энергокризис, добивший тонкую unit-экономику. | [Sifted](https://sifted.eu/articles/infarm-bankrupt-netherlands), [FoodBev](https://www.foodbev.com/news/infarm-s-dutch-branch-declared-bankrupt) |
| F3 | Iron Ox — прекращение операций | 2024 | failure | medium | low / none | season-years / none | sensor-fusion | not-applicable / medium | mixed | Остановила деятельность в июне 2024 после неудачи с привлечением финансирования; до этого — сокращение ~50 из 100 сотрудников в ноябре 2022; $102M привлечённых средств; статус — «Out of Business». Точная июньская дата синтезирована из нескольких вторичных источников, не из одного первичного пресс-релиза о закрытии — поэтому confidence medium, не high. | [TechCrunch 2022 layoffs](https://techcrunch.com/2022/11/03/iron-ox-lays-off-50-amounting-to-nearly-half-its-staff/), [AgFunderNews](https://agfundernews.com/another-blow-for-indoor-farm-robotics-as-iron-ox-lays-off-nearly-half-its-staff), [PitchBook profile](https://pitchbook.com/profiles/company/155954-53) |
| F4 | Prospera Technologies / Valmont — обесценение $137,3M | 2023 | failure | high | moderate / U3 | weeks-months / F-B | sensor-fusion | yes / low | no | SEC 8-K (23 окт. 2023): списание $137,3M (после налогов $133,3M) гудвилла/нематериальных активов Prospera; причина прямо названа в документе — «значительно более медленный рост агрономических AI-решений Prospera по сравнению с исходными финансовыми прогнозами»; привело к операционному убытку сегмента $99,7M за Q3 2023 и чистому убытку компании $49M за квартал. Важная деталь для анти-bias: источник сам называет причиной провал продукта/темпов внедрения ИИ-платформы, а не внешний макрошок — редкий в этой выборке случай `external_driver: no`. | [SEC 8-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/102729/000010272923000055/vmi-20231023xex99d1.htm) |
| F5 | Bowery Farming — остановка операций | 2024 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | yes | Остановила операции в начале ноября 2024 после привлечения >$700M (оценка >$2B в 2021 раунде); собственная AI-платформа BoweryOS анализировала фото урожая в реальном времени, но, по цитате источника, «никакая софт-оптимизация не могла закрыть разрыв между стоимостью LED-энергии и ценой салата $2 в супермаркете»; в нояб. 2025 грузинский завод ($70M) ушёл на ликвидацию. | [TechCrunch](https://techcrunch.com/2024/11/04/bowery-farming-is-ceasing-operations/), [Fertilizer Daily (2025 liquidation)](https://www.fertilizerdaily.com/20251114-bowery-farmings-70m-georgia-vertical-farm-heads-to-liquidation-as-startups-collapse-triggers-nationwide-sell-offs/) |
| F6 | FarmWise — свёртывание бизнеса | 2025 | failure | high | moderate / none | weeks-months / none | deep-learning | yes / low | yes | Свернула операции 1 апр. 2025 после привлечения ~$140M; активы (робот Vulcan) купила Taylor Farms через несколько дней. Источник явно пишет: AI-технология прополки «commercially ready» (т.е. технически рабочая) — причина закрытия названа как «макроэкономика, влияющая на решения фермеров» + падение венчурных инвестиций, НЕ техническая неудача ИИ. | [igrownews](https://igrownews.com/farmwise-latest-news/), [AgFunderNews](https://agfundernews.com/farmwise-ai-powered-weeding-tech-commercially-ready-despite-company-restructuring-and-wind-down) |
| F7 | AppHarvest — Chapter 11 | 2023 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | mixed | Подала на банкротство 24 июля 2023; чистый убыток $177M при продажах <$15M в последнем годовом отчёте; три «мега-теплицы» с ИИ и робототехникой не вышли на плановую продуктивность (вредители, недостижение прогнозных урожаев) — т.е. причина смешанная: и макро (рост цен на энергию/ставки), и собственные операционные провалы (не только внешний шок). | [Wikipedia](https://en.wikipedia.org/wiki/AppHarvest), [Crunchbase News](https://news.crunchbase.com/agtech-foodtech/vertical-farming-venture-capital-plenty-appharvest/) |
| F8 | Plenty Unlimited — Chapter 11 | 2025 | failure | high | low / none | season-years / none | hybrid | not-applicable / medium | mixed | Подала на (пре-пакетное) банкротство 23-25 марта 2025 в Южном округе Техаса; вышла из процедуры за 53 дня (29 мая 2025), но акционерный капитал обнулён — оценка упала >99% от пика $1,9B (январь 2022). Компания переориентировалась на премиальный рынок клубники. | [Bloomberg](https://www.bloomberg.com/news/articles/2025-03-24/bezos-softbank-backed-vertical-farmer-plenty-files-bankruptcy), [igrownews](https://igrownews.com/plenty-unlimited-news/) |
| F9 | Raven Industries/CNH — AutoCart «тихий» даунгрейд до driver-assist | 2024 | failure | low | moderate / U3 | seconds-minutes / F-C | sensor-fusion | unclear / high | no | Raven анонсировал (2020-2021) полностью беспилотный набор AutoCart для синхронизации тракторной тележки с комбайном — товар на предзаказ к урожаю 2021. К 2024 рыночный ролл-аут под брендом CNH вышел как «Cart Automation» — явно **driver-assisted** (водитель в кабине), а не беспилотная версия. **Это моя интерпретация, не прямая цитата источника** — ни один найденный материал не называет это «провалом» напрямую; источники просто документируют замену продукта на менее автономную версию без объяснения причины. Понижено до `confidence: low` именно по этой причине. | [DTN/Progressive Farmer](https://www.dtnpf.com/agriculture/web/ag/equipment/article/2023/10/09/raven-rolls-grain-cart-automation), [Raven pre-order release](https://www.oemoffhighway.com/electronics/smart-systems/automated-systems/press-release/21208420/raven-industries-inc-raven-industries-opens-preorder-for-autonomous-grain-cart-solution) |
| F10 | John Deere — обещание «полностью автономного трактора» (CES 2022) vs факт внедрения | 2022 | failure | medium | moderate / unclear | seconds-minutes / F-C | deep-learning | yes / medium | mixed | На CES в январе 2022 Deere анонсировал полностью автономный 8R, заявленный к коммерческой доступности на урожай 2022 г. К 2024 отчётность фиксирует: «только несколько десятков» тракторов из объявленной линейки реально в ежедневной эксплуатации, при цене ~$500k/ед. и «обширном взаимодействии с техническими специалистами Deere для настройки». **Также интерпретация**: источники не говорят буквально «провал обещания 2022 года» — это мой вывод из сопоставления даты анонса и даты отчёта о фактическом внедрении. `external_driver: mixed`, т.к. причины названы и экономические (цены на технику, высокие ставки, низкие цены на кукурузу/сою), и адопционные (доверие/настройка). | [FarmProgress (2022 launch)](https://www.farmprogress.com/technology/autonomous-tractor-bringing-a-new-definition-to-hands-free-), [FierceSensors (2024 adoption gap)](https://www.fiercesensors.com/electronics/farmers-arent-buying-many-tractors-autonomys-here-stay) |
| F11 (доп.) | AeroFarms — повторное закрытие (Вирджиния) | 2025 | failure | medium | low / none | season-years / none | hybrid | not-applicable / medium | mixed | Продолжение F1: после выхода из Chapter 11 в 2023 и двух прибыльных кварталов компания окончательно закрыла вирджинский завод в декабре 2025 — показывает, что «успешный выход из банкротства» не был устойчивым успехом. Не засчитан в обязательные 10 (тот же эмитент, что F1), добавлен отдельной строкой за ценность нюанса «восстановился → снова провалился». | [SupermarketNews](https://www.supermarketnews.com/grocery-technology/aerofarms-emerges-from-bankruptcy-names-new-ceo) |

### Успех (7 из требуемых 10 — честный недобор, см. выше)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | John Deere See & Spray Ultimate — сезон 2025 | 2025 | success | high | moderate / unclear | season-years / F-A | deep-learning | yes / low | not-applicable | >5 млн акров обработано технологией в 2025; сокращение гербицидов «почти на 50%» (31 млн галлонов экономии); независимые полевые испытания в 7 штатах показали +2 бушеля/акр в среднем на сое, до +4,8 бушеля/акр в отдельных испытаниях vs сплошное опрыскивание. | [Robotics & Automation News](https://roboticsandautomationnews.com/2025/11/05/john-deere-customers-use-autonomous-see-spray-technology-across-5-million-acres-in-2025/96266/), [Global AgTech Initiative](https://www.globalagtechinitiative.com/in-field-technologies/robotics-automation/john-deere-customers-use-see-spray-technology-across-five-million-acres-in-2025/) |
| S2 | Digital Green — Farmer.Chat (генеративный ИИ-консультант) | 2024 | success | high | high / unclear | weeks-months / F-B | foundation-model | yes / low | not-applicable | Развёрнут в 4 странах (Кения, Индия, Эфиопия, Нигерия) с окт. 2023; >15 000 активных фермеров, >300 000 запросов к началу 2024 (позже — ~250 000 пользователей, в среднем 18 обращений/мес/фермер); 70% применили рекомендации в течение 30 дней, 80% предприняли хоть какое-то действие по совету; оценка снижения стоимости консультации «в 100 раз» ($35 → $0,35 на фермера) против традиционной агроконсультации. Полнота ответа — не идеальна: только 67% ответов оценены как высокорелевантные, 18% — низкорелевантные (явно показано в самой публикации, не скрыто). | [arXiv 2409.08916v2](https://arxiv.org/html/2409.08916v2), [AI for Cause](https://aiforcause.org/stories/digital-green-farmer-chat) |
| S3 | Прогноз урожайности по спутниковым индексам + Random Forest | 2023 | success | medium | moderate / none | season-years / F-A | classical-ml | yes / low | not-applicable | Опубликовано в Advances in Space Research, ноябрь 2023: Random Forest даёt R²=0,77, RMSE=0,39 т/га, MAE=0,28 т/га на прогнозе урожайности по спутниковым вегетационным индексам. Единичное исследование без независимой репликации — отсюда `confidence: medium`, не `high`. | [ADS abstract](https://ui.adsabs.harvard.edu/abs/2023AdSpR..72.3998J/abstract) |
| S4 | RicEns-Net — ансамблевое глубокое обучение для прогноза урожайности риса | 2025 | success | medium | moderate / none | season-years / F-A | hybrid | yes / low | not-applicable | arXiv-препринт (подан 9 февр. 2025), датасет — EY Open Science Challenge 2023; модель-ансамбль «RicEns-Net»; средняя абсолютная ошибка (MAE) 341 кг/га — это ≈5-6% от самого низкого среднего урожая в регионе (явная база для интерпретации цифры, не абсолютное число без контекста). Препринт, не прошедший peer review на момент разметки — `confidence: medium`. | [arXiv 2502.06062](https://arxiv.org/pdf/2502.06062) |
| S5 | Verdant Robotics SharpShooter (канал AGCO) — коммерческий запуск | 2024 | success | medium | moderate / none | seconds-minutes / F-C | sensor-fusion | yes / low | not-applicable | Коммерческий запуск объявлен 21 окт. 2024 (дебют на FIRA 2024, 22-24 окт., Вудленд, Калифорния); вендор заявляет сокращение расхода химикатов >96% и затрат на ручную прополку в среднем на 65% против сплошной обработки. Это вендорский пресс-релиз, не независимый аудит — отсюда `confidence: medium`. | [BusinessWire](https://www.businesswire.com/news/home/20241021622688/en/Verdant-Robotics-Announces-Commercial-Launch-of-Sharpshooter) |
| S6 | Carbon Robotics LaserWeeder (G2) — накопленный коммерческий масштаб | 2024 | success | medium | moderate / none | seconds-minutes / F-C | deep-learning | yes / low | not-applicable | Серия D на $70M в окт. 2024 (лидер BOND, с участием NVIDIA NVentures — оценка ~$370M); накопленно (на момент раунда) >250 000 акров прополото, >15 млрд сорняков уничтожено на >100 видах культур на 3 континентах; датасет для детекции — >40 млн размеченных растений. Участие стратегического инвестора (NVIDIA) — некоторая независимая проверка интереса рынка, но сами эффект-цифры — вендорский self-report. | [GeekWire](https://www.geekwire.com/2025/carbon-robotics-releases-new-line-of-laser-weed-zappers-for-more-types-of-farms-and-budgets/), [AgricultureDive](https://www.agriculturedive.com/news/carbon-robotics-raises-70m-for-its-ai-powered-laserweeder/730725/) |
| S7 | Прогноз урожайности пшеницы/ячменя по Sentinel-2 — RF/XGBoost (Испания) | 2026* | success | medium | moderate / none | season-years / F-A | classical-ml | yes / low | not-applicable | MDPI *Agriculture*, DOI `10.3390/agriculture16050516`: 5 сезонов данных (2020-2024), Random Forest + XGBoost на 5 фенологических стадиях; за 15 дней до уборки модели дают R²=0,782. **Год публикации помечен звёздочкой — выведен из номера тома журнала (vol. 16), а не подтверждён напрямую** (прямой фетч страницы MDPI вернул HTTP 403); если нумерация томов MDPI *Agriculture* смещена, реальный год может быть 2025. | [DOI](https://doi.org/10.3390/agriculture16050516) |

### Дополнительные (не засчитаны в 10/10, но верифицированы и информативны)

| # | case_name | year | outcome | confidence | axis1_level / mechanism | axis2_bucket / mechanism | axis3_class | axis4_gate / blast_radius | external_driver | Что произошло (цифры) | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | PlantVillage Nuru — точность диагностики болезней кассавы (Восточная Африка) | 2020** | partial | high | high / U1+U2 | weeks-months / none | deep-learning | yes / low | not-applicable | Полевое исследование (Frontiers in Plant Science, опубл. окт. 2020, данные 2018-2019): Nuru диагностирует симптомы CMD/CBSD/CGM с точностью 65% (лучше агроконсультантов 40-58% и фермеров 18-31%), но точность по мягким/ранним симптомам падает до 13-37%; точность растёт до 74-88% при осмотре 6 листьев на растение вместо одного. **Год за пределами окна 2022-2026** — помечено звёздочками; оставлено в таблице как лучший найденный независимо верифицированный, полевой (не лабораторный) пример диагностической точности ИИ в АПК с честно показанным разбросом (не только агрегатное число). | [PMC7775399](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7775399/), [Frontiers](https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.590889/full) |
| P2 | Tortuga AgTech → поглощение Oishii | 2025 | undetermined | medium | moderate / none | weeks-months / none | deep-learning | yes / low | mixed | Независимые операции Tortuga AgTech завершились в марте 2025: Oishii (вертикальная ферма) купила IP, активы и часть инженерной команды; на момент сделки коммерческий парк — 150 роботов-сборщиков клубники. Это не чистое закрытие (технология и команда продолжили жить внутри Oishii) и не чистый успех (самостоятельная компания перестала существовать) — отсюда `outcome: undetermined`, а не `failure`/`success`. | [AgFunderNews](https://agfundernews.com/oishii-acquires-tortuga-agtechs-ip-assets-and-engineering-team-to-supercharge-its-vertical-farms) |

## Итог по годам

| Год | Провал | Успех | Доп. | Комментарий |
|---|---|---|---|---|
| 2020** | — | — | 1 (partial) | PlantVillage Nuru — вне окна, оставлен за качество источника |
| 2022 | 1 | 0 | — | Только интерпретативный кейс (F10); не нашёл верифицируемого *успешного* 2022-кейса в бюджет поиска |
| 2023 | 4 (F1,F2,F4,F7) | 1 (S3) | — | Самый плотный год по провалам (кластер банкротств vertical farming + SEC-импермент) |
| 2024 | 3 (F3,F5,F9) | 3 (S2,S5,S6) | — | Самый плотный год в целом |
| 2025 | 2 (F6,F8) + 1 доп.(F11) | 1 (S4) | 1 (P2) | |
| 2026* | 0 | 1 (S7) | — | Единственный 2026-кейс — дата не подтверждена напрямую (см. примечание к S7) |

**Не закрыто и не притянуто силой:** верифицируемый явный *успех*, независимо датированный 2022
годом, и любой кейс (успех или провал), уверенно датированный 2026 (единственный претендент на
2026 имеет непрямую, выводную дату). Это честные пробелы, а не случайность формулировки таблицы.

## Пересечение названий с существующим реестром (`reestr-reshenij.csv`)

Для прозрачности: кейсы **Carbon Robotics LaserWeeder** (S6) и **Verdant Robotics/AGCO** (S5, как
вендор-категория — в реестре присутствует общая категория автономной техники AGCO/Trimble) могут
пересекаться по названию вендора с уже существующими строками реестра лекции 10. Числа и источники
в этом файле получены сегодняшним независимым поиском, а не скопированы из `razmetka/lec-10.md` —
но при объединении в будущем общий реестр стоит проверить на содержательный, не только текстовый,
дубль по этим двум вендорам.

---

## Связанные канонические файлы исследования (issue #349)

- `notes/research/osi-primenimosti-ii/reestr-reshenij-verified.csv` — сводный CSV 248 внешне
  верифицированных кейсов по всем 12 лекциям.
- `notes/research/osi-primenimosti-ii/reestr-reshenij-verified-README.md` — README к нему.
- `notes/research/osi-primenimosti-ii/reestr-reshenij.csv` + `reestr-reshenij-README.md` —
  исходный канонический реестр 421 кейса из материалов самого курса (issue #349).

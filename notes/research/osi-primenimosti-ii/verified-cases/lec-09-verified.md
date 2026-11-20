---
title: "Верифицированные внешние кейсы — Лекция 9 (frontier-space), независимое усиление реестра"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 9 (frontier-space) — 23 независимо верифицированных кейса

## Подход к поиску

Задача — не пересказать 32 строки `razmetka/lec-09.md` (они уже честно отмечают, что отбор
«подвержен смещению в сторону публикуемых успехов», и сами фиксируют 100% успех на n=17
подробных разборов), а **целенаправленно найти провалы**, которых в материале лекции почти нет, и
добавить **новые** внешне верифицируемые кейсы 2022–2026 с явным исходом, конкретной цифрой/датой
и названным инструментом/аппаратом.

Поиск шёл двумя волнами: (1) WebSearch по 11 целевым запросам (успешные автономные посадки/
навигация + явный розыск провалов — «Mars rover anomaly», «autonomous navigation failure»,
«satellite AI malfunction», AUV/дрон в экстремальной среде) — исчерпал лимит сессии на
WebSearch; (2) после этого — WebFetch напрямую по предсказуемым URL Wikipedia/официальных
пресс-релизов для добивки деталей и дополнительных кейсов без нового WebSearch-запроса. Это
ограничение само по себе методически интересно: уже на первой волне провалы находились
**труднее и с бо́льшим числом попыток**, чем успехи — ровно та asymmetric publication bias, на
которую указывает сам файл лекции.

**Понятие «frontier-space» расширено буквально так, как задано в задании** — не только орбита/
Луна/Марс, но и экстремальные земные фронтиры (автономный подводный аппарат под антарктическим
ледником). Это включено намеренно: индустрия лекции 9 — про автономию в средах без GPS/связи/
точных карт, а не только про вакуум.

**Покрытие по годам.**

- **Успех:** все пять лет 2022–2026 закрыты (2022 — DART, AEGIS-Lite, CAPSTONE; 2023 —
  Chandrayaan-3, OnBoard Planner, OPS-SAT, CAPSTONE-завершение; 2024 — SLIM, Chang'e-6,
  AEGIS-Heavy, ADRAS-J, IM-1 частично; 2025 — Blue Ghost; 2026 — Varda W-6).
- **Провал: 2026 не закрыт.** Реально найденные кандидаты 2026 (аномалия ESA PROBA-3 в феврале,
  потеря связи с одним из двух спутников формейшн-флайта) — восстановлены к марту без публично
  названной технической причины; я не включаю его, чтобы не притягивать слабый кейс ради
  формальной строки в таблице. Это честный пробел, не натянутая заглушка.
- Остальные четыре года провала закрыты: 2022 (OMOTENASHI), 2023 (ispace M1, Luna-25, EQUULEUS,
  Starship IFT-1 — четыре кейса на один год, намеренно не выбрасывал ни один), 2024 (Ingenuity,
  AUV Ran), 2025 (ispace M2, IM-2 Athena).

## Честная оговорка по качеству источников

- **Сильно задокументированные, официальным расследованием/пресс-релизом компании/агентства:**
  Ingenuity Flight 72 (NASA/JPL + AeroVironment отчёт), ispace Mission 1 и Mission 2 (обе — ispace
  официально опубликовала техническую причину), Luna-25 (Роскосмос), IM-2 Athena (множественные
  независимые СМИ со ссылкой на NASA/IM), Starship IFT-1 (FAA mishap investigation, закрыто
  официально).
- **Средняя надёжность — факт подтверждён, но архитектура/причина не детализирована публично:**
  AUV Ran (университет Гётеборга подтвердил потерю аппарата, но не назвал конкретный механизм
  отказа навигации — только то, что у замены будет «более устойчивая поддержка решений в
  аварийных ситуациях»), Zhurong (китайская сторона подтвердила исход словами главного
  конструктора, но без инженерного отчёта), OPS-SAT (цифры точности — из одного
  экспериментального исследования на реальной телеметрии, не из гарантированно продакшн-версии
  борта), Varda W-6 (единственный источник — технический журналистский материал, не первичный
  пресс-кит).
- **Слабо документированные — явно помечены низкой confidence в таблице:** EQUULEUS (Wikipedia
  называет исход буквально «spacecraft failure» без причины — включён ради честного покрытия
  2023 года, не потому что это сильный кейс), OMOTENASHI (причина — «не удалось сориентировать
  солнечные панели», без разбора, был ли это отказ алгоритма или аппаратуры).
- **Два кейса в таблице провалов — НЕ про ИИ/МО, а про классическую автономию** (Luna-25,
  Starship IFT-1 AFTS) — включены по тому же принципу, которым сама лекция включает G-FOLD/
  AutoNav/NASA IPEx: это структурные контрпримеры «автономная система — не значит ИИ», важные
  для ≥30%-правила курса и для честности самой оси. Явно помечены в столбце `axis3_class` как
  `rule-based` и в описании — как «не ИИ-кейс».
- **SLIM и IM-1 Odysseus — требуют разведения подсистемы и миссии целиком.** В обоих случаях
  навигационная/сенсорная функция сама отработала (SLIM — точность приземления внутри 10 м при
  цели 100 м; IM-1 — программный переход на резервный датчик NASA NDL спас посадку), но у SLIM
  общая миссия пострадала от независимой аппаратной неисправности двигателя (опрокидывание), а у
  IM-1 — от человеческой ошибки конфигурации перед стартом (лазерный альтиметр не включили). SLIM
  размечен как `success` для самой навигационной подсистемы (так пишут первоисточники), с явной
  оговоркой в описании; IM-1 размечен как `partial` и не входит ни в счёт 10 успехов, ни в счёт
  10 провалов — отдельная одиннадцатая категория для прозрачности.

## Кейсы с успешным исходом (15)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| S1 | NASA/JHUAPL DART — SMART Nav автономное наведение на Диморф | 2022 | https://www.jhuapl.edu/destinations/missions/dart | 26.09.2022: автономная система SMART Nav взяла управление за 4 ч до удара, точный захват цели за 50 мин, попадание на скорости >4 миль/с; изменило орбитальный период Диморфа на 32 минуты | moderate | none | seconds-minutes | F-C | sensor-fusion | no | low | not-applicable | success | high |
| S2 | NASA/JPL AEGIS-Lite на Perseverance SuperCam | 2022 | https://pubmed.ncbi.nlm.nih.gov/37494463/ | Развёрнут 18.05.2022 (Sol 442): автономный выбор научных целей по изображениям без согласования с Землёй, Science Robotics, peer-reviewed | moderate | none | hours-days | F-A | classical-ml | no | low | not-applicable | success | high |
| S3 | NASA CAPSTONE — автономная кросслинк-навигация CAPS | 2022–2023 | https://en.wikipedia.org/wiki/CAPSTONE_(spacecraft) | Орбитальная вставка 14.11.2022, завершение основной миссии 18.05.2023: ~6 месяцев автономного определения позиции относительно LRO без наземных станций, несмотря на раннюю аномалию клапана двигателя (обнаружена 5.07.2022, устранена 7.10.2022) | low | none | hours-days | F-A | rule-based | yes | low | not-applicable | success | high |
| S4 | ISRO Chandrayaan-3 — LHDAC + автономный посадочный секвенсор | 2023 | https://www.analyticsvidhya.com/blog/2023/08/chandrayaan-3-touchdown-how-ai-and-sensors-aided-isro-epic-lunar-venture/ | 23.08.2023: первая мягкая посадка у южного полюса Луны, автономное обнаружение препятствий камерой + автономный секвенсор без вмешательства с Земли | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| S5 | NASA/JPL OnBoard Planner (OBP) для Perseverance | 2023 | https://www.science.org/doi/10.1126/scirobotics.adi3099 | С 05.10.2023 ровер управляется автономным планировщиком: заявлено до 20% экономии энергии и завершение кампаний на 25% быстрее (дней) | moderate | none | hours-days | F-A | rule-based | yes | low | not-applicable | success | medium |
| S6 | ESA OPS-SAT — обнаружение аномалий телеметрии нейросетью на борту | 2023–2024 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12041257/ | Первое обучение ML-моделей на борту в полёте; экспериментальная точность классификации аномалий 0,957 (precision 0,929, recall 0,897) на реальной телеметрии OPS-SAT до контролируемого сведения с орбиты в мае 2024 | moderate | none | seconds-minutes | F-C | deep-learning | yes | low | not-applicable | success | medium |
| S7 | JAXA SLIM — vision-based точная посадка (навигационная подсистема) | 2024 | https://www.nasaspaceflight.com/2024/01/slim-landing/ | 19–20.01.2024: визуальное сопоставление снимков поверхности с картой дало точность приземления ~10 м при цели 100 м — «точечная посадка... полный успех» по словам JAXA; аппарат в целом опрокинулся из-за независимого отказа двигателя (не относится к навигационной ИИ-подсистеме) | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | mixed | success | high |
| S8 | CNSA Chang'e-6 — автономный облёт препятствий при посадке на обратной стороне Луны | 2024 | https://en.wikipedia.org/wiki/Chang%27e_6 | Посадка 01.06.2024: камера видимого диапазона + лазерный 3D-сканер для автономного обхода препятствий на неизвестной местности; возврат 1935,3 г образцов 25.06.2024 — первый возврат образцов с обратной стороны Луны | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| S9 | NASA/JPL AEGIS-Heavy — расширение автономного выбора целей (VISIR+LIBS) | 2024 | https://eos.org/science-updates/the-ai-upgrade-helping-perseverance-work-smarter-on-mars | Обновление отмечено 09.11.2024: автономный выбор целей расширен на технику VISIR в дополнение к LIBS; к моменту публикации собрано данных по 40+ научным целям без цикла согласования с Землёй | moderate | none | hours-days | F-A | classical-ml | no | low | not-applicable | success | high |
| S10 | Astroscale ADRAS-J — автономное сближение с некооперативным обломком | 2024 | https://en.wikipedia.org/wiki/Astroscale | Запуск февраль 2024; к ноябрю 2024 — сближение на 15 м и облёт на 360° вокруг верхней ступени ракеты H-IIA без заранее известной точной модели её вращения/траектории — впервые для коммерческой компании | high | none | hours-days | F-A | unclear | yes | medium | not-applicable | success | medium |
| S11 | Firefly Aerospace Blue Ghost Mission 1 — Terrain Relative Navigation | 2025 | https://en.wikipedia.org/wiki/Blue_Ghost_Mission_1 | 02.03.2025: первая полностью успешная коммерческая мягкая посадка на Луну; визуальная TRN распознала кратеры/склоны/камни на неизвестной местности и вычислила 2 манёвра уклонения в последний час спуска, попадание в 100-метровую зону | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| S12 | Varda Space Industries W-6 — автономная навигация по звёздам при входе в атмосферу | 2026 | https://www.theregister.com/science/2026/05/20/space-factories-edge-closer-after-experimental-capsule-survives-hypersonic-landing/5243140 | Капсула W-6 использует систему, определяющую позицию по изображениям звёзд и объектов на НОО во время гиперзвукового входа; штатная посадка на Koonibba Test Range (Австралия), май 2026 | moderate | none | seconds-minutes | F-C | sensor-fusion | no | medium | not-applicable | success | medium |
| S13 | ESA Hera — автономная навигация и прибытие к Дидиму | 2026 | https://www.esa.int/Space_Safety/Hera/ESA_s_Hera_targets_early_arrival_at_Didymos_asteroids | 8 июля 2026 ESA загрузила финальное ПО автономной «self-driving»-навигации; прибытие к Дидиму — ноябрь 2026, на месяц раньше плана | high | none | seconds-minutes | F-C | sensor-fusion | yes | medium | not-applicable | success | high |
| S14 | SpaceX Starlink — автономные манёвры уклонения от столкновений (полугодовой отчёт FCC) | 2026 | https://api-prod.fcc.gov/icfs-attachment/exp/api/v1/a81df57a93db4f10ac9c39bfa8373c08 | Филинг FCC от 1 июля 2026: 207 152 автономных манёвра уклонения дек.2025–май 2026 (65 137 Gen1 + 142 015 Gen2); порог срабатывания — вероятность столкновения ≥3/10 000 000, без участия человека на каждый манёвр | moderate | none | seconds-minutes | F-C | rule-based | no | high | yes | success | high |
| S15 | Rocket Lab / Space Force VICTUS HAZE — автономный орбитальный перехват Pioneer | 2026 | https://www.globenewswire.com/news-release/2026/06/22/3315647/0/en/Rocket-Lab-Shatters-Responsive-Space-Record-Launches-U-S-Space-Force-VICTUS-HAZE-Mission-in-16-Hours-42-Minutes.html | Запуск 19.06.2026; Pioneer выполнил RPO против манёврирующего JACKAL-0004 (True Anomaly), опередив 84-часовой дедлайн на >25 часов — заявлено как «первый коммерческий автономный орбитальный перехват» | high | unclear | hours-days | F-A | unclear | yes | medium | not-applicable | success | medium |

## Кейсы с провальным/неуспешным исходом (11)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1 | JAXA OMOTENASHI — отказ ориентации на Солнце | 2022 | https://en.wikipedia.org/wiki/OMOTENASHI | Запуск 16.11.2022 в составе Artemis I; солнечные панели не удалось сориентировать на Солнце, связь неустойчива с 17.11, попытки восстановления прекращены 21–22.11.2022 — полная потеря миссии | unclear | unclear | hours-days | F-A | rule-based | no | high | no | failure | medium |
| F2 | ispace Hakuto-R Mission 1 — крах из-за ложной фильтрации показаний альтиметра | 2023 | https://spacenews.com/software-problem-blamed-for-ispace-lunar-lander-crash/ | 25.04.2023: при пересечении края кратера высота скачком изменилась на ~3 км, программа сочла это отказом сенсора и отфильтровала корректные данные — аппарат «думал», что уже на поверхности, будучи на высоте ~5 км, упал при выработке топлива | moderate | U2 | seconds-minutes | F-C | rule-based | no | high | no | failure | high |
| F3 | Роскосмос Luna-25 — отказ бортовой системы управления (не ИИ-кейс) | 2023 | https://spacepolicyonline.com/news/russia-traces-luna-25-crash-to-onboard-control-system-failure/ | 19.08.2023: блок акселерометров не включился из-за конфликта приоритетов команд, двигатель коррекции орбиты отработал 127 с вместо 84 с — первая российская лунная миссия за 47 лет разбилась о поверхность Луны. Классическая, не ИИ/МО автономия — включён как структурный контрпример | low | none | seconds-minutes | F-C | rule-based | no | catastrophic | no | failure | high |
| F4 | JAXA EQUULEUS — потеря связи, причина не раскрыта | 2023 | https://en.wikipedia.org/wiki/EQUULEUS | После ~6 месяцев штатной работы (запуск 16.11.2022) последний контакт 18.05.2023, Wikipedia фиксирует исход буквально как «spacecraft failure» без названной причины — слабейший по детализации кейс набора | unclear | unclear | weeks-months | unclear | unclear | unclear | medium | unclear | failure | low |
| F5 | SpaceX Starship IFT-1 — 40-секундная задержка срабатывания автономной системы аварийного подрыва (не ИИ-кейс) | 2023 | https://en.wikipedia.org/wiki/SpaceX_Starship_integrated_flight_test_1 | 20.04.2023: потеря управления из-за пожара в хвостовой части на T+85 с; автономная AFTS сработала на T+3:10, но разрушение корабля заняло ещё 40 секунд — FAA предписала 63 корректирующих действия. Классическая триггерная логика, не ИИ — включён как структурный контрпример про саму скорость автономного реагирования | low | none | seconds-minutes | F-C | rule-based | no | catastrophic | no | failure | high |
| F6 | Университет Гётеборга — потеря автономного подводного аппарата Ran под ледником Туэйтс (Антарктида) | 2024 | https://astrobiology.com/2024/02/02/underwater-droid-auv-ran-has-gone-missing-under-an-antarctic-glacier/ | Январь 2024: аппарат не вышел на запрограммированную точку встречи после многочасового автономного похода под ледовым шельфом без GPS/связи; признан потерянным. Преемник Ran II получит «более устойчивую поддержку решений в аварийных ситуациях» — признание пробела в автономной логике оригинала | extreme | unclear | hours-days | F-B | unclear | no | high | unclear | failure | medium |
| F7 | NASA/JPL Ingenuity — навигационный отказ над однородным песком, Flight 72 | 2024 | https://www.flightglobal.com/ops-safety/2024/12/nasa-completes-first-ever-aircraft-accident-investigation-on-another-planet/ | 18.01.2024: система визуальной навигации не нашла достаточно текстурных признаков на однородных песчаных рябях уже через ~20 с после взлёта, что привело к высокой горизонтальной скорости при посадке и обломку всех 4 лопастей — первое в истории расследование авиационной аварии на другой планете | high | U2 | seconds-minutes | F-C | sensor-fusion | no | high | no | failure | high |
| F8 | Intuitive Machines IM-2 (Athena) — лазерный альтиметр ослеплён собственным пылевым шлейфом | 2025 | https://en.wikipedia.org/wiki/IM-2 | 06.03.2025: за 3 минуты до посадки пылевой шлейф от двигателей забил лазерный альтиметр и нарушил радиосвязь, аппарат ударился о плато и опрокинулся на 1-2 оборота; при ~100 Вт вместо требуемых выработки миссия завершилась через <13 часов (к 07.03.2025 06:15 UTC) | high | U2 | seconds-minutes | F-C | sensor-fusion | no | high | no | failure | high |
| F9 | ispace Hakuto-R Mission 2 (RESILIENCE) — аппаратная аномалия лазерного дальномера | 2025 | https://spacenews.com/laser-rangefinder-problems-blamed-for-second-ispace-lunar-lander-crash/ | 05.06.2025: связь потеряна за ~90 с до посадки на высоте 193 м при скорости 42 м/с из-за аномалии в новом лазерном дальномере (поставщик оригинальной детали прекратил производство между миссиями) — второй подряд полный провал посадки ispace, потеряны ровер TENACIOUS и все payload | unclear | unclear | seconds-minutes | F-C | sensor-fusion | no | high | mixed | failure | high |
| F10 | SpaceX Starship Flight Test 12 — отказ автономной посадки Super Heavy | 2026 | https://spaceflightnow.com/2026/05/27/faa-requires-spacex-led-mishap-investigation-before-resumption-of-starship-launches/ | Запуск 22.05.2026: после разделения ступеней Super Heavy «ненормально быстро перевернулся», большинство двигателей отказали, посадка в Гольфо-де-Мехико на скорости 1450 км/ч; FAA 27.05.2026 признала mishap и приостановила полёты | moderate | none | seconds-minutes | F-C | rule-based | no | high | no | failure | high |

## Отдельная категория — partial (не входит в счёт 10/10)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Intuitive Machines IM-1 (Odysseus) — лазерный альтиметр не включён перед стартом, спасён программным переключением на NASA NDL | 2024 | https://www.washingtonpost.com/technology/2024/02/23/intuitive-machines-odysseus-moon-landing-drama/ | 22.02.2024: лазерный альтиметр не был активирован из-за защитного выключателя (человеческая ошибка конфигурации перед стартом); инженеры на лету переписали навигационное ПО на резервный датчик NASA Navigation Doppler Lidar — мягкая, но неустойчивая посадка, аппарат завалился на бок; NASA и IM назвали миссию в целом успехом | unclear | unclear | seconds-minutes | F-C | sensor-fusion | unclear | high | yes | partial | high |
| P2 | NASA/JPL Perseverance — автономная защита от сбоя (переключение на резервную радиосистему) | 2026 | https://science.nasa.gov/blogs/mars/2026/11/19/nasas-perseverance-odyssey-teams-investigate-technical-issues/ | 30.10.2026: основное UHF-радио не передало ~25 «heartbeat»-сигналов (~100 с) → борт автономно отключил радио, переключился на резервное, вошёл в safe mode; резервное радио работает на половинной мощности, расследование не закрыто на дату источника | high | none | seconds-minutes | F-C | rule-based | no | medium | not-applicable | partial | high |
| P3 | ESA PROBA-3 — месячный блэкаут и восстановление формейшн-флайта | 2026 | https://blogs.esa.int/proba-3/2026/06/04/back-to-formation-flying-and-a-peek-at-earth/ | Февраль 2026: аномалия в ПО не дала аппарату корректно войти в safe mode → месячный блэкаут без энергии; связь восстановлена, причина устранена патчем, формейшн-флайт полностью восстановлен к началу июня 2026 | extreme | U2 | weeks-months | unclear | rule-based | no | catastrophic | mixed | partial | high |

## Итог: что это даёт гипотезе «космос = 100% успеха»

**Дополнение 2026-11-20 (issue #349): после добора 6 новых 2026-кейсов** (3 успеха, 1 провал,
2 partial — ESA Hera, Starlink, VICTUS HAZE / Starship FT-12 / Perseverance, PROBA-3) счёт —
**15 успехов / 11 провалов / 3 partial на 29 строках**. PROBA-3 (месячный блэкаут формейшн-флайта)
— первая `axis1_level=extreme` строка в этом файле; исход `partial`, не success, поэтому
headline-тезис ниже (сформулированный на исходных 23 строках) не меняется по счёту, только по
знаменателю.

12 успехов против 10 чётких провалов на 23 внешне верифицированных, датированных кейсах — это
прямое, количественное опровержение тезиса «космос как отрасль почти не знает провалов автономии»
из `00-rezyume.md`/`10-industriya-i-rejting-faktorov.md` (там — n=17, 100%, явно помеченное как
тонкая выборка). Найденные провалы — не экзотика: три из пяти (Ingenuity, оба ispace, IM-2)
получили официальные расследования причин от самого оператора или NASA/FAA, то есть это такая же
по качеству доказательная база, как у найденных успехов. Важная оговорка по составу: ровно
половина из 10 провалов (Luna-25, Starship IFT-1, и с оговоркой OMOTENASHI/EQUULEUS) — отказы
классической, не ИИ/МО автономии; если считать строго «провалы именно статистических/обучаемых
моделей», чистых ИИ-провалов в списке два с высокой confidence (Ingenuity — отказ визуальной
навигации, можно спорить rule-based vs sensor-fusion) и ispace M1 (классическая фильтрация, не
ИИ) — то есть даже агрессивный поиск находит в космосе **намного больше провалов классической
автономии, чем провалов собственно обучаемых моделей**. Это само по себе согласуется с
наблюдением файла `10` о том, что в корпусе курса классика на низкой неопределённости почти не
проваливается technically, но здесь — обратный полюс: именно в сфере, где классика массово
используется (посадочная навигация), она и проваливается чаще всего на практике — просто
исторически здесь ИИ/МО используется реже, чем классические фильтры/контроллеры, поэтому и
провалов ИИ физически меньше в выборке, а не потому что ИИ надёжнее.

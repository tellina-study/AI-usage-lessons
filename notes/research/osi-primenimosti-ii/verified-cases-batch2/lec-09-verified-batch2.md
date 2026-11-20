---
title: "Верифицированные внешние кейсы — Лекция 9 (frontier-space), волна 2 (batch2)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 9 (frontier-space) — 28 независимо верифицированных НОВЫХ кейсов (волна 2)

## Подход к поиску

Это третья волна поиска для issue #349 (цель владельца курса — догнать общую выборку до 1000+
строк для проверки устойчивости закономерностей осей применимости ИИ). Задача этого файла —
**не пересекаться** с 22 кейсами первой волны (`verified-cases/lec-09-verified.md`, список дан в
задании оркестратором) и закрыть явно названный пробел: первая волна покрыла 2022–2026 плотно,
но 2018–2021 — почти не найдено. Эта волна целенаправленно искала именно 2018–2021 (хронологически
«до» первой волны) плюс добивала 2022–2025 новыми, не пересекающимися миссиями/событиями.

**Два этапа поиска.** (1) WebSearch по ~25 целевым запросам покрыл практически весь список ниже —
сессионный лимит WebSearch был исчерпан (200/200) к моменту, когда оставалось проверить 3-4
кандидата (Icefin, Boaty McBoat(y), Saildrone-детали, точная дата отчёта AEGIS на Curiosity).
(2) Эти последние кандидаты добивались WebFetch напрямую по Wikipedia/официальным страницам без
нового WebSearch-запроса — тот же приём, что использовала волна 1. Два кандидата, не прошедшие
верификацию на этом этапе (AUV Boaty McBoat(y)/Autosub Long Range на Thwaites — главная страница
Wikipedia отдала 404; BepiColombo — после прямой проверки оказалось, что это **чисто аппаратная**
авария без автономии/ИИ: «No autonomous systems or AI decision-making were involved — operators
detected and manually corrected the power delivery malfunction»), были **отброшены**, а не включены
слабо обоснованными.

**Понятие «frontier-space» расширено так же, как в волне 1** — помимо орбиты/Луны/Марса, включены
экстремальные земные аналоги (беспилотный парусный дрон в урагане, автономный подлёдный робот под
антарктическим ледником), по прямому прецеденту волны 1 (AUV Ran). Доля таких кейсов здесь — 3 из
28 (≈11%), сопоставимо с волной 1 (1 из 23 ≈ 4%).

## Покрытие по годам (главный результат этой волны)

| Год | Успех | Провал | Partial | Итого |
|---|---|---|---|---|
| 2018 | 1 (InSight EDL) | 0 | 0 | 1 |
| 2019 | 4 (Hayabusa2, Chang'e-4, Crew Dragon Demo-1, Saildrone Atlantic) | 4 (Chandrayaan-2, Beresheet, Starliner OFT-1, Soyuz MS-14) | 0 | 8 |
| 2020 | 4 (OSIRIS-REx TAG, Chang'e-5, MEV-1, AEGIS-Curiosity-отчёт) | 0 | 0 | 4 |
| 2021 | 5 (Zhurong-посадка, Perseverance TRN, Ingenuity-1й полёт, Saildrone-Sam, ELSA-d) | 0 | 0 | 5 |
| 2022 | 0 | 1 (Zhurong-спячка) | 1 (Rocket Lab catch-drop) | 2 |
| 2023 | 2 (Lucy/Dinkinesh, Icefin/Thwaites) | 0 | 0 | 2 |
| 2024 | 1 (Starship IFT-5 catch) | 2 (Starship IFT-3, Peregrine) | 0 | 3 |
| 2025 | 1 (New Glenn NG-2) | 1 (New Glenn NG-1) | 1 (Starship IFT-7) | 3 |
| **Итого** | **18** | **8** | **2** | **28** |

**Главный честный результат этой волны: 2018–2021 закрыт плотно (18 из 28 кейсов, 64%)** — именно
то, чего не хватало общей выборке. Асимметрия успех/провал в этой волне (18:8:2, против почти
1:1 в волне 1) объясняется тем, что задание этой волны не требовало целенаправленного перекоса в
сторону провалов — волна 1 уже закрыла эту задачу; эта волна оптимизировалась под покрытие годов и
неперекрытие с волной 1, а не под баланс исходов. Это зафиксировано как известное ограничение, не
скрыто.

## Честная оговорка по качеству источников

- **Сильно задокументированные официальным расследованием/первичным пресс-релизом агентства:**
  Chandrayaan-2 (ISRO Failure Analysis Committee, 16.11.2019), SpaceIL Beresheet (инженерный разбор
  Times of Israel с цитатами участников), Boeing Starliner OFT-1 (NASA/Boeing официальные брифинги),
  Astrobotic Peregrine (формальный failure review board, воспроизведено на стенде), Blue Origin
  New Glenn NG-1 (официальный FAA mishap report, закрыт), SpaceX Starship IFT-3/IFT-7 (официальные
  пресс-релизы SpaceX с указанием вероятной причины), OSIRIS-REx TAG (пресс-релиз NASA/University
  of Arizona), Ingenuity (JPL пресс-релиз), Perseverance TRN (NASA Science официальная технология),
  MEV-1 (множественные независимые СМИ + заявления Northrop Grumman), New Glenn NG-2 (заявление CEO
  Blue Origin).
- **Средняя надёжность — факт подтверждён, но инженерная деталь не раскрыта публично полностью:**
  Soyuz MS-14 (TASS сообщил о вероятной причине — отказ усилителя сигнала «Курс», без детального
  отчёта), Chang'e-5 docking (китайские источники подтверждают факт и дату, но не публикуют
  алгоритмическую архитектуру стыковки), Zhurong-посадка и Zhurong-спячка (через слова главного
  конструктора Чжан Жунцяо и подтверждение снимками MRO, без инженерного отчёта), ELSA-d (публичные
  материалы Astroscale подтверждают успешный первый тест, но не детализируют тип алгоритма
  распознавания цели), Rocket Lab Electron catch-drop (подтверждено множественными СМИ и прямой
  цитатой CEO, но причина «нагрузки на трос» не разобрана инженерно).
- **Слабее документированные — явно помечены medium/low confidence:** Saildrone Hurricane Sam и
  Atlantic double-crossing (источник — страница Wikipedia о компании Saildrone, не первичный
  пресс-кит NOAA; цифры по курсу/скорости не детализированы), Icefin/Thwaites (источник — раздел
  статьи Wikipedia о леднике Туэйтс, пересказывающий публикацию в Nature; сама публикация
  недоступна без подписки — не удалось свериться с первоисточником напрямую).
- **Кейсы, НЕ являющиеся ИИ/МО-провалами/успехами — классическая, не обучаемая автономия.**
  Как и в волне 1 (где это сделано для Luna-25 и Starship IFT-1), сюда явно включены структурные
  контрпримеры: Chandrayaan-2 (классический guidance-алгоритм, не ML), SpaceIL Beresheet
  (аппаратный сбой IMU + перезапуск компьютера), Boeing Starliner OFT-1 (программная ошибка
  таймера), Soyuz MS-14 (аппаратный отказ усилителя сигнала), Astrobotic Peregrine (отказ клапана),
  Blue Origin New Glenn NG-1/NG-2 и SpaceX Starship IFT-5/IFT-7 (классическая посадочная
  GNC-автоматика, не обучаемая модель), NASA InSight EDL (классическая EDL-последовательность).
  Это **9 из 28** кейсов волны — внесены намеренно для той же цели, что и в волне 1: «автономная
  система ≠ ИИ» должно быть видно количественно, а не только как оговорка в тексте.
- **Отброшенные кандидаты (не вошли в таблицу):** AUV Boaty McBoat(y)/Autosub Long Range на
  Thwaites Glacier (не удалось получить рабочую страницу-первоисточник в рамках WebFetch-бюджета
  после исчерпания WebSearch — решил не включать кейс без проверенного источника, а не натягивать
  слабую ссылку); BepiColombo thruster anomaly 2024 (при прямой проверке оказалось — чисто
  аппаратная авария электропитания, НЕ автономный/ИИ-кейс, восстановление выполнено наземной
  командой вручную, не бортовой логикой — явно не подходит под тему лекции, несмотря на
  первоначальную привлекательность как «провал 2024 года»).

## Кейсы с успешным исходом (18)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2-S1 | NASA InSight — автономный вход-спуск-посадка (не ИИ-кейс) | 2018 | https://en.wikipedia.org/wiki/InSight | 26.11.2018: классическая автономная последовательность EDL (парашют, ретро-ракеты, 3 контактных датчика на опорах) без связи с Землёй из-за задержки сигнала; скорость касания ~8 км/ч, штатная посадка | low | none | seconds-minutes | F-C | rule-based | no | high | not-applicable | success | high |
| B2-S2 | JAXA Hayabusa2 — автономная навигация по искусственному маркеру при касании Рюгу | 2019 | https://link.springer.com/article/10.1007/s42064-020-0070-0 | 21.02.2019 и 11.07.2019: переключение с ручного управления на автономное отслеживание сброшенного светоотражающего маркера на финальном участке спуска обеспечило точный сбор образцов (включая подповерхностные после создания искусственного кратера) | moderate | none | seconds-minutes | F-C | sensor-fusion | yes | medium | not-applicable | success | high |
| B2-S3 | CNSA Chang'e-4 — первая посадка на обратной стороне Луны с автономным избеганием препятствий | 2019 | https://www.eoportal.org/satellite-missions/chang-e-4 | 03.01.2019: посадка в кратере Фон Карман; на высоте ~100 м автономная пауза спуска для анализа препятствий/уклона камерой и выбора точки посадки по алгоритмам, унаследованным от Chang'e-3 | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| B2-S4 | SpaceX Crew Dragon Demo-1 — первая автономная стыковка коммерческого корабля с МКС | 2019 | https://www.space.com/spacex-crew-dragon-docks-space-station.html | 03.03.2019: автономная стыковка к модулю Harmony без экипажа на борту и без ручного управления со станции — первый такой случай для коммерческого пилотируемого корабля | low | none | hours-days | F-A | sensor-fusion | yes | high | not-applicable | success | high |
| B2-S5 | Saildrone — первое двустороннее автономное пересечение Атлантики (SD 1021) | 2019 | https://en.wikipedia.org/wiki/Saildrone | 08–10.2019: беспилотный парусный дрон совершил переход Бермуды→Великобритания и обратно без экипажа на солнечно-ветровой энергии — первый автономный аппарат, пересёкший Атлантику в обе стороны | moderate | none | weeks-months | F-A | rule-based | no | low | not-applicable | success | medium |
| B2-S6 | NASA OSIRIS-REx — Natural Feature Tracking при сборе образца на Бенну (TAG) | 2020 | https://www.eurekalert.org/news-releases/680651 | 20.10.2020: автономная навигация по сопоставлению снимков с картой поверхности подвела аппарат к точке касания Nightingale в пределах ~1 м от цели; 5 из 6 секунд контакта — активный сбор материала | moderate | none | seconds-minutes | F-C | sensor-fusion | yes | medium | not-applicable | success | high |
| B2-S7 | CNSA Chang'e-5 — первая автономная стыковка на лунной орбите без экипажа | 2020 | https://spaceflightnow.com/2020/12/05/chinese-mission-accomplishes-first-ever-robotic-docking-in-lunar-orbit/ | 05.12.2020: взлётный модуль с лунными образцами автономно состыковался с орбитальным модулем в 21:42 UTC — первая в истории беспилотная стыковка на орбите другого небесного тела; передача капсулы с образцами в 22:12 UTC | moderate | none | hours-days | F-A | unclear | yes | high | not-applicable | success | high |
| B2-S8 | Northrop Grumman MEV-1 — первая коммерческая автономная стыковка-продление ресурса спутника | 2020 | https://www.space.com/private-satellites-docking-success-northrop-grumman-mev-1.html | 25.02.2020: MEV-1 автономно подошёл и состыковался с выработавшим топливо Intelsat 901 в режиме автопилота — первая в истории стыковка двух коммерческих спутников на орбите, продление срока службы на 5 лет | moderate | none | hours-days | F-A | unclear | yes | medium | not-applicable | success | high |
| B2-S9 | NASA/JPL — отчёт по первым 4 годам AEGIS на Curiosity (Verma 2020) | 2020 | https://ai.jpl.nasa.gov/public/projects/aegis/ | Сол 1343–2830 (≈05.2016–01.2020): предпочтительная научная цель выбрана автономно в >86% случаев против <20% при случайном наведении, распознавание валунов/обнажений >90% против <40%, частота LIBS-измерений выросла с 255 до 311 выстрелов/сол | low | none | hours-days | F-A | classical-ml | no | low | not-applicable | success | high |
| B2-S10 | CNSA Tianwen-1/Zhurong — автономная посадка на Марс с избеганием препятствий | 2021 | https://www.eoportal.org/satellite-missions/tianwen-1 | 14-15.05.2021: посадка в Утопии («девять минут ужаса») — парашют + ретро-ракеты + автономное зависание и обход препятствий по камере на финальном участке; выезд ровера на поверхность 22.05.2021 | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| B2-S11 | NASA/JPL Mars 2020 Perseverance — первая посадка на Марс с Terrain-Relative Navigation | 2021 | https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/terrain-relative-navigation-landing-between-the-hazards/ | 18.02.2021: Lander Vision System впервые на Марсе определил положение по снимкам поверхности с точностью ~40 м за <10 с и автономно выбрал безопасную точку посадки в кратере Джезеро | moderate | none | seconds-minutes | F-C | sensor-fusion | no | high | not-applicable | success | high |
| B2-S12 | NASA/JPL Ingenuity — первый управляемый полёт летательного аппарата на другой планете | 2021 | https://www.jpl.nasa.gov/news/nasas-ingenuity-mars-helicopter-succeeds-in-historic-first-flight/ | 19.04.2021: подъём на 3 м, 30 с висения, автономная навигация по камере слежения за поверхностью, полное время полёта 39,1 с — первый полёт аппарата тяжелее воздуха на другой планете | high | none | seconds-minutes | F-C | sensor-fusion | no | medium | not-applicable | success | high |
| B2-S13 | Saildrone — беспилотный дрон внутри урагана Sam категории 4 (SD 1045) | 2021 | https://en.wikipedia.org/wiki/Saildrone | 09.2021: SD 1045 вошёл в центр урагана Sam и передавал видео/данные изнутри шторма в реальном времени — первое исследовательское судно в истории, уцелевшее внутри крупного урагана | extreme | none | hours-days | F-C | rule-based | no | low | not-applicable | success | medium |
| B2-S14 | Astroscale ELSA-d — первый тест автономного захвата/стыковки через магнитный механизм | 2021 | https://en.wikipedia.org/wiki/ELSA-d | 25.08.2021: сервисный аппарат автономно нашёл, приблизился и состыковался с клиентским модулем-целью на орбите через магнитный докинг-механизм — технологическая демонстрация для будущего удаления космического мусора | moderate | none | hours-days | F-A | unclear | yes | medium | not-applicable | success | medium |
| B2-S15 | SwRI/NASA Lucy — автономный трекинг цели выявил неизвестный спутник астероида Диункинеш | 2023 | https://www.swri.org/newsroom/press-releases/swri-led-lucy-observes-first-ever-contact-binary-orbiting-asteroid | 01.11.2023: терминальная система автономного трекинга при тренировочном пролёте успешно удержала цель в кадре и впервые обнаружила контактно-двойной спутник (Селам), не известный заранее | high | none | seconds-minutes | F-C | sensor-fusion | no | low | not-applicable | success | high |
| B2-S16 | Университет Georgia Tech/Cornell (ITGC) — робот Icefin под ледником Туэйтс выявил «быстрые трещины» | 2023 | https://en.wikipedia.org/wiki/Thwaites_Glacier | 2023 (9-месячное наблюдение через 587-метровую скважину): автономный подводный робот обнаружил, что трещины занимают 10% площади подошвы ледника, но дают 27% текущей потери льда; общее подтаивание идёт медленнее прогноза моделей из-за стратификации воды | high | none | weeks-months | F-B | sensor-fusion | no | low | not-applicable | success | medium |
| B2-S17 | SpaceX Starship IFT-5 — первая в истории ловля ускорителя башней («chopsticks») | 2024 | https://www.euronews.com/2024/10/13/spacex-catches-starship-rocket-booster-as-it-returns-to-earth | 13.10.2024: Booster 12 после возвращения на старт пойман механическими «палочками» башни через ~7 минут после старта — первая ловля орбитального ускорителя такого размера в истории | low | none | seconds-minutes | F-C | rule-based | no | catastrophic | not-applicable | success | high |
| B2-S18 | Blue Origin New Glenn NG-2 — первая успешная посадка ускорителя на морскую платформу | 2025 | https://www.space.com/space-exploration/launches-spacecraft/watch-blue-origins-huge-new-glenn-rocket-ace-its-epic-landing-on-a-ship-at-sea-video | 13.11.2025: первая успешная посадка первой ступени New Glenn на платформу в океане — вторая попытка подряд после неудачи NG-1 в январе; Blue Origin стала второй компанией в истории, посадившей такой крупный ускоритель на орбитальном полёте, и первой сделавшей это со второй попытки | low | none | seconds-minutes | F-C | rule-based | no | high | not-applicable | success | high |

## Кейсы с провальным/неуспешным исходом (8)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2-F1 | ISRO Chandrayaan-2 — крах лендера Vikram из-за программной ошибки guidance-алгоритма (не ИИ-кейс) | 2019 | https://www.space.com/india-admits-moon-lander-crash.html | 06.09.2019: на высоте 2,1 км на этапе «точного торможения» двигатели развили большую тягу, чем ожидалось, накопленная ошибка траектории превысила допуск программы коррекции ориентации — связь потеряна перед касанием; расследование ISRO (16.11.2019) назвало причиной программный сбой | low | none | seconds-minutes | F-C | rule-based | no | catastrophic | no | failure | high |
| B2-F2 | SpaceIL Beresheet — крах из-за сбоя IMU и перезапуска бортового компьютера (не ИИ-кейс) | 2019 | https://www.timesofisrael.com/5-6-attempts-to-restart-israeli-moon-landers-engine-failed-investigation-finds/ | 11.04.2019: на высоте ~14 км сбой акселерометра IMU вызвал перезапуск бортового компьютера и выключение главного двигателя; 5-6 попыток перезапуска частично удались, но скорость уже была слишком высокой — первый частный лунный аппарат разбился о поверхность | low | none | seconds-minutes | F-C | rule-based | no | catastrophic | no | failure | high |
| B2-F3 | Boeing Starliner OFT-1 — автономная система ошиблась фазой миссии из-за сбоя таймера (не ИИ-кейс) | 2019 | https://www.nasaspaceflight.com/2019/12/starliner-mission-shortening-failure-successful-launch/ | 20.12.2019: бортовой таймер MET считал время со сдвигом на 11 часов, автономная логика решила, что идёт другая фаза полёта, и израсходовала топливо на ненужные манёвры удержания ориентации — стыковка с МКС отменена, миссия сокращена с 8 до 3 дней | low | none | seconds-minutes | F-C | rule-based | no | high | no | failure | high |
| B2-F4 | Roscosmos Soyuz MS-14 — отказ усилителя сигнала автоматической системы стыковки «Курс» (не ИИ-кейс) | 2019 | https://spacenews.com/uncrewed-soyuz-aborts-iss-docking/ | 24.08.2019: беспилотный корабль с роботом Fedor не состыковался автоматически из-за отказа усилителя сигнала «Курс» на модуле «Поиск» МКС; стыковка перенесена и выполнена 27.08.2019 после ручной релокации другого корабля для освобождения исправного порта | low | none | hours-days | F-A | rule-based | yes | medium | no | failure | high |
| B2-F5 | CNSA Zhurong — ровер не вышел из плановой спячки из-за накопления марсианской пыли | 2022 | https://www.space.com/dust-preventing-china-mars-rover-zhurong-waking-up | Плановая спячка с 05.2022, пробуждение в 12.2022 не состоялось; к 07.02.2023 снимки MRO подтвердили, что ровер не сдвинулся — главный конструктор Чжан Жунцяо назвал вероятной причиной накопление пыли на солнечных панелях (при 40% покрытия — «game over»); до этого аппарат проехал 1921 м за 358 активных дней | unclear | U2 | weeks-months | F-A | rule-based | no | high | no | failure | medium |
| B2-F6 | SpaceX Starship IFT-3 — потеря управления по крену и разрушение на входе в атмосферу | 2024 | https://en.wikipedia.org/wiki/Starship_flight_test_3 | 14.03.2024: во время орбитальной фазы потеряно управление по крену (вероятная причина — засор клапанов), корабль вошёл в атмосферу в нештатной ориентации, перегрев вне теплозащиты и потеря телеметрии; автономная система аварийного завершения сработала при потере связи | high | U3 | seconds-minutes | F-C | rule-based | no | high | no | failure | high |
| B2-F7 | Astrobotic Peregrine Mission One — отказ клапана наддува разорвал топливный бак (не ИИ-кейс) | 2024 | https://spacenews.com/valve-problem-blamed-for-peregrine-lunar-lander-failure/ | 08.01.2024: клапан между гелиевым баком наддува и окислителем не закрылся повторно после срабатывания (вероятно, из-за вибрационного ослабления резьбы), гелий под высоким давлением разорвал топливный бак — потери топлива не позволили выполнить посадку, аппарат сведён с орбиты 18.01.2024 | low | none | hours-days | F-A | rule-based | no | catastrophic | no | failure | high |
| B2-F8 | Blue Origin New Glenn NG-1 — неудачная посадка ускорителя из-за сбоя повторного зажигания двигателей | 2025 | https://phys.org/news/2025-04-faa-blue-glenn-booster-failure.html | 16.01.2025: при посадочном тормозном манёвре не произошло штатного повторного зажигания части из семи двигателей BE-4, телеметрия потеряна на отметке T+7:55 — первый полёт New Glenn достиг орбиты успешно, но посадка ускорителя не удалась; FAA закрыла расследование с 7 корректирующими мерами | low | none | seconds-minutes | F-C | rule-based | no | high | no | failure | high |

## Отдельная категория — partial (не входит в счёт 18/8)

| # | case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2-P1 | Rocket Lab Electron — вертолёт впервые поймал ускоритель в воздухе, но пилот намеренно его отпустил | 2022 | https://spacenews.com/rocket-lab-launches-smallsats-catches-but-drops-booster/ | 02.05.2022, миссия «There and Back Again»: вертолёт впервые в истории поймал падающий на парашюте ускоритель Electron, но пилот почувствовал нехарактерную для тренировок нагрузку на трос и намеренно отпустил ступень в океан; CEO Питер Бек назвал результат «99% цели» | moderate | U3 | seconds-minutes | F-C | hybrid | yes | low | mixed | partial | high |
| B2-P2 | SpaceX Starship IFT-7 — вторая подряд успешная ловля бустера, но корабль разрушился на подъёме | 2025 | https://en.wikipedia.org/wiki/Starship_flight_test_7 | 16.01.2025: Booster 14 успешно пойман башней второй раз подряд, но корабль Ship 33 на подъёме потерял несколько двигателей (T+7:39), затем телеметрию (T+8:26) на высоте 146 км и взорвался над Тёркс и Кайкос — вероятная причина: усиленные вибрации вызвали утечку кислорода/топлива в полости над защитным кожухом двигателя | high | U3 | seconds-minutes | F-C | rule-based | no | catastrophic | no | partial | high |

## Итог: что это даёт общей выборке

**28 новых кейсов, ни один не дублирует 22 кейса волны 1** (сверено по названию аппарата/миссии и
дате события перед записью в таблицу). Главный вклад этой волны — не баланс успех/провал (который
специально не форсировался, в отличие от волны 1), а **хронологическое закрытие пробела 2018–2021**:
18 из 28 новых кейсов (64%) датированы именно этим периодом, который был почти не представлен ни в
волне 1, ни в основном `razmetka/lec-09.md`. Это даёт будущему анализу динамики по годам (ось
«историческая динамика», файл `04-istoricheskaya-dinamika.md`) заметно больше точек на раннем
участке временного ряда для Лекции 9 — до этой волны во внешне верифицированном слое практически
не было кейсов frontier-space раньше 2022 года.

Вторичный вклад — ещё 9 структурных контрпримеров «автономная система ≠ ИИ» (Chandrayaan-2,
Beresheet, Starliner OFT-1, Soyuz MS-14, Peregrine, New Glenn ×2, Starship IFT-5/IFT-7 с посадочной
автоматикой) по тому же принципу, которым волна 1 включила Luna-25 и Starship IFT-1 — это
количественно усиливает наблюдение волны 1, что в космической отрасли классическая (не обучаемая)
автономия проваливается на практике чаще, чем находится задокументированных провалов именно
статистических/обучаемых моделей — просто потому, что классические алгоритмы управления и посадки
исторически используются в разы чаще ИИ/МО-компонентов.

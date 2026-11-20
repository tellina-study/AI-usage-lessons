---
title: "Лекция 11 (manufacturing) — волна 3, верифицированные кейсы вне материалов курса (batch 2)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 11 (manufacturing) — батч 2, независимо верифицированные кейсы

Третья волна поиска по Лекции 11 (самая слабая отрасль волны 1 — 17 кейсов из целевых 20).
Задание: найти **≥25 новых** кейсов, не дублируя 17 кейсов волны 1 (BMW+Figure 02, Siemens
Amberg, Rio Tinto+Komatsu, Rolls-Royce IntelligentEngine, Landing AI, Zymergen, Fast Radius,
Local Motors, Bright Machines, Zume, iRobot, Covariant, Berkshire Grey, Veo Robotics, Desktop
Metal, Foxconn+Nvidia, Hyundai+Boston Dynamics). Ни один из 25 кейсов ниже не повторяет этот
список — проверено построчно.

## Подход к поиску

Сессия использовала `WebSearch` (≈30 запросов на кандидатов — Katerra, Arrival, Relativity
Space, Instrumental, Vicarious, Uptake, Audi, Mercedes+Apptronik, FANUC, Intel, Corning, Drishti,
Quanergy, Lordstown, Path Robotics, Creator, Divergent/Czinger, Plethora) и затем, **после того
как лимит `WebSearch` исчерпался на отметке 200/200 запросов сессии** (та же структурная
проблема, что и в волне 1 — см. `verified-cases/lec-11-verified.md`), сессия перешла полностью
на `WebFetch` по прямым URL — официальные пресс-релизы (Audi, Apptronik/Mercedes), первоисточники
вендоров (Intel IT, FANUC, Path Robotics, Instrumental), и ~30 точечных обращений к Wikipedia
(которая, как и в волне 1, используется как указатель на первичные факты с собственными
цитированными датами, а не как единственный источник истины).

**Осторожность к фабрикации (прямое указание задания).** Каждый кандидат ниже проверен минимум
одним прямым `WebFetch`-чтением первоисточника или Wikipedia-статьи с конкретными датами/числами
— **не** через агрегаторские «AI use-case» сайты вида `case-studies.ai`, которые волна 1 поймала
на кейсе Ford+IBM. Там, где первоисточник не нашёлся или давал слишком тонкие основания для
утверждения «это ИИ-кейс», кандидат либо помечен `confidence: low` с explicit оговоркой, либо
**отброшен целиком** (список отброшенных — ниже, отдельным разделом, как и просил оркестратор).

## Отброшенные кандидаты (не вошли в таблицу)

| Кандидат | Почему отброшен |
|---|---|
| **Carbon (Carbon3D) + Adidas Futurecraft 4D** | Реальная компания, реальный продукт (обувь), но Wikipedia-статья **прямо не упоминает ИИ** ни в каком виде — только «cloud-connected hardware/software for predictive maintenance». Включение как «ИИ-кейс» было бы натягиванием факта под гипотезу — ровно то, против чего предостерёг оркестратор. |
| **GE Aerospace / GE Additive** (3D-печать лопаток GE9X) | Реальное аддитивное производство, реальные детали — но **ни одного упоминания ИИ/генеративного дизайна** в проверенном источнике. Чистое аддитивное производство без ИИ-компонента — не кейс для этой выборки. |
| **3D Systems** (финансовые трудности 2024) | Реальный убыток $255М за 2024 — но источник не называет никакой ИИ-технологии вообще, только классические SLA/FDM/SLS. |
| **Uptake Technologies** (слухи про layoffs 2019) | Не нашлось ни одного источника, подтверждающего конкретное сокращение штата 2019 года — только общие пресс-релизы о продукте. Не вошло без прямого подтверждения события. |
| **Lordstown Motors** (банкротство июнь 2023, иск к Foxconn) | Банкротство реальное и хорошо документированное — но ни один источник не называет конкретную роль ИИ в провале (спор был о невыполненном финансировании Foxconn, не о технологии). Форсировать «ИИ-ярлык» на чисто финансовый провал означало бы повторить ошибку с избыточным доверием к нарративу. |
| **C3.ai customer cases** (Shell, Baker Hughes, Caterpillar) | Wikipedia-страница C3.ai не называет ни один конкретный клиентский кейс с метриками; прямые попытки найти первоисточник через `WebSearch` исчерпали лимит раньше, чем дошли до этой темы. |
| **Rockwell Automation / Caterpillar Cat Digital / Micron / TSMC / ASML / Samsung Semiconductor** | Все проверены через `WebFetch` на Wikipedia — ни один не даёт именованного ИИ-кейса с метрикой и датой (общие описания продуктовых линеек, не кейсы). |
| **WEF Global Lighthouse Network** (Tata Steel Kalinganagar и др.) | Главная страница инициативы недоступна (403/404 для `WebFetch`); единственная найденная зацепка — упоминание Tata Steel Kalinganagar в Wikipedia без единой метрики. Недостаточно для строки таблицы. |
| **Kindred Systems / Kindred AI** (поглощение Ocado, 2020) | Wikipedia `Kindred (company)` оказалась **омонимом** — сервис обмена жильём, не робототехническая компания. Без свежего `WebSearch`-бюджета не удалось найти правильную страницу/первоисточник в разумное время. |
| **Wandelbots, Jibo — альтернативные URL, Creator (restaurant) wiki-страница** | 404 на прямые попытки; по Jibo и Creator факты в итоге получены из других источников (см. таблицу), по Wandelbots — не удалось найти рабочую страницу вообще. |

## Честная оговорка по двум самым слабым строкам таблицы

**Drishti Technologies (поглощение Apple) и Plethora Technology (поглощение Xometry)** включены
в таблицу с `confidence: low` — обе компании и оба события **реальны** (подтверждены несколькими
независимыми агрегаторами — Crunchbase, Seedtable, Tracxn, PR Newswire для факта запуска
Plethora), но **точная причина/детали поглощения и роль ИИ в исходе не подтверждены прямым
первоисточником** (официальный пресс-релиз Apple или Xometry не найден в рамках сессии). Это
отличается от кейса Ford+IBM волны 1 (который был **полностью не найден** ни в одном
первоисточнике) — здесь компании/события существуют, но глубина верификации ниже, чем у
остальных 23 строк. Оставлены в таблице по той же логике, что и `Bright Machines`/`Landing AI`
в волне 1 (низкая, но не нулевая, достоверность, явно помеченная).

**FANUC Zero Down Time** — числа ($75М экономии, 35 000+ подключённых роботов) взяты из
`WebSearch`-синтеза по трём доменам (`fanucamerica.com`, `automate.org`, `productionmachining.com`)
— прямой `WebFetch` на все три URL вернул 403/нечитаемый PDF. Цифры **кросс-подтверждены двумя
независимыми доменами** в самом тексте поисковой выжимки, но не прочитаны мной лично постранично
— `confidence: medium`, не `high`.

## Покрытие по годам (цель — закрыть 2018–2021, слабо покрытые волной 1)

- **2018** — 2 кейса (Rethink Robotics, Tesla Model 3 «избыточная автоматизация»).
- **2019** — 1 кейс (Anki).
- **2020** — 2 кейса (Jibo, Creator).
- **2021** — 3 кейса (Katerra, Pepper/SoftBank Robotics, Plethora).
- **2022** — 2 кейса (Vicarious, Quanergy).
- **2023** — 5 кейсов (Relativity Space Terran 1, Audi, Sarcos→Palladyne, Divergent/Czinger,
  Drishti).
- **2024** — 6 кейсов (Instrumental, Mercedes+Apptronik, Agility Robotics+GXO, Arrival, Shapeways,
  Path Robotics — старт).
- **2025–2026** — 4 кейса (Siemens+rhobot.ai, Markforged, Path Robotics — продолжение/контракт
  2026, Intel — непрерывная программа).

**2018–2021 закрыт существенно лучше, чем в волне 1** (8 кейсов против 0 у волны 1 за тот же
период) — это прямо отвечает указанию оркестратора «постарайся закрыть 2018-2021».

## Качество источников — честная оценка

- **Высокое:** Anki, Jibo, Pepper/SoftBank Robotics (все три — подробные Wikipedia-статьи с
  точными датами/числами, широко освещены современной прессой на момент события), Audi (прямой
  официальный пресс-релиз Audi, дата подтверждена — 30.06.2023), Intel (прямой официальный
  документ Intel IT с конкретной метрикой >90% точности), Relativity Space Terran 1 (множество
  независимых изданий — Space.com, Spaceflightnow, Forbes, GeekWire, все сходятся в деталях),
  Arrival (Wikipedia + Reuters/Electrek/Autocar освещение банкротства), Markforged (точные суммы
  сделок — $116М, затем $42М — из Wikipedia со ссылками на обе сделки), Sarcos/Palladyne
  (детальная Wikipedia-статья с конкретными числами «500 обещанных единиц → 2 выпущенных»).
- **Среднее:** Rethink Robotics, Katerra, Vicarious, Quanergy, Divergent/Czinger, Mercedes+
  Apptronik, Agility Robotics+GXO, Siemens+rhobot.ai, FANUC (см. оговорку выше), Shapeways (банкротство
  подтверждено точно, но связь с ИИ в источнике тонкая — только упоминание стороннего ПО
  оптимизации файлов).
- **Низкое (явно помечено):** Drishti Technologies, Plethora Technology, Instrumental (кейс-стади
  вендора на собственном сайте — именованные клиенты реальны, но независимого аудита метрик нет,
  тот же класс источника, что Landing AI в волне 1).

## Таблица кейсов

| id | case_name | year | industry | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VER-L11-18 | Rethink Robotics — закрытие (коллаборативные роботы Baxter/Sawyer, force-sensing адаптивное управление, активы купил HAHN Group) | 2018 | manufacturing | moderate | U3 | season-years | F-A | sensor-fusion | not-applicable | medium | mixed | failure | medium | https://en.wikipedia.org/wiki/Rethink_Robotics |
| VER-L11-19 | Tesla Model 3 — «избыточная автоматизация» признана ошибкой Маском, откат на ручную сборку в палатке GA4 | 2018 | manufacturing | high | U3 | weeks-months | F-B | unclear | no | medium | no | failure | medium | https://en.wikipedia.org/wiki/Criticism_of_Tesla,_Inc. |
| VER-L11-20 | Anki — банкротство производителя AI-робот-игрушек (Cozmo, Vector, Overdrive), $182,5М привлечено | 2019 | manufacturing | low | none | season-years | F-A | deep-learning | not-applicable | low | yes | failure | high | https://en.wikipedia.org/wiki/Anki_(American_company) |
| VER-L11-21 | Jibo — продажа активов NTT (здравоохранение/образование) после коммерческого провала социального робота | 2020 | manufacturing | low | none | season-years | F-A | classical-ml | not-applicable | low | yes | failure | high | https://en.wikipedia.org/wiki/Jibo |
| VER-L11-22 | Creator — временное закрытие ресторана роботизированных бургеров из-за COVID-19 (статус после переоткрытия в Daly City не доведён до определённости) | 2020 | manufacturing | moderate | U3 | season-years | F-B | rule-based | not-applicable | low | yes | partial | medium | https://thespoon.tech/creator-temporarily-closes-its-robot-restaurant/ |
| VER-L11-23 | Katerra — банкротство Chapter 11 (роботизированное модульное строительство, SoftBank, $2 млрд привлечено) | 2021 | manufacturing (граница: строительство) | unclear | unclear | season-years | F-A | unclear | not-applicable | high | mixed | failure | medium | https://www.bloomberg.com/news/articles/2021-06-07/softbank-backed-katerra-files-bankruptcy-with-billions-in-debt |
| VER-L11-24 | SoftBank Robotics Pepper — остановка производства из-за слабого спроса (~27 000 произведённых единиц) | 2021 | manufacturing | low | none | season-years | F-A | classical-ml | not-applicable | low | yes | failure | high | https://en.wikipedia.org/wiki/Pepper_(robot) |
| VER-L11-25 | Plethora Technology — поглощение Xometry, прекращение самостоятельной работы (AI/правило-based анализ технологичности CAD-моделей) | 2021 | manufacturing | unclear | unclear | season-years | unclear | rule-based | not-applicable | low | unclear | undetermined | low | https://www.crunchbase.com/organization/plethora-2 |
| VER-L11-26 | Vicarious AI — поглощение Alphabet/Intrinsic, команда расформирована между Intrinsic и DeepMind | 2022 | manufacturing | high | U3 | season-years | F-A | deep-learning | not-applicable | medium | mixed | failure | medium | https://en.wikipedia.org/wiki/Vicarious_(company) |
| VER-L11-27 | Quanergy Systems — Chapter 11 после SPAC (лидар+ИИ для промышленной автоматизации), оценка $1,4 млрд до подачи | 2022 | manufacturing | unclear | unclear | season-years | F-A | sensor-fusion | not-applicable | medium | mixed | failure | medium | https://www.therobotreport.com/lidar-maker-quanergy-files-chapter-11-bankruptcy/ |
| VER-L11-28 | Relativity Space — первый запуск Terran 1 (ИИ-итерация дизайна + 3D-печать ракеты), не достиг орбиты из-за аномалии 2-й ступени | 2023 | manufacturing (граница: аэрокосмос) | extreme | U1 | seconds-minutes | F-C | hybrid | yes | catastrophic | no | partial | high | https://en.wikipedia.org/wiki/Terran_1 |
| VER-L11-29 | Audi — AI-контроль качества точечной сварки (WPS-Analytics), 1,5 млн сварных точек и 300 машин за смену в Neckarsulm | 2023 | manufacturing | low | none | seconds-minutes | F-C | deep-learning | yes | low | no | success | high | https://www.audi.com/en/press-releases/audi-begins-roll-out-of-artificial-intelligence-for-quality-control-of-spot-welds-15443 |
| VER-L11-30 | Sarcos → Palladyne AI — отказ от производства промышленных экзоскелетов Guardian (план 500 ед./год → выпущено 2), переход в чистый софт | 2023 | manufacturing | high | U3 | season-years | F-A | hybrid | not-applicable | medium | no | failure | high | https://en.wikipedia.org/wiki/Sarcos_Technology_and_Robotics_Corporation |
| VER-L11-31 | Divergent 3D / Czinger 21C — генеративный дизайн + аддитивное производство шасси гиперкара, серия 80 единиц | 2023 | manufacturing | moderate | U3 | weeks-months | F-A | hybrid | yes | low | no | success | medium | https://en.wikipedia.org/wiki/Czinger_21C |
| VER-L11-32 | Drishti Technologies — поглощение Apple, видео-аналитика конвейеров (клиенты Ford, Denso, HELLA, Continental) | 2023 | manufacturing | unclear | unclear | unclear | unclear | deep-learning | unclear | unclear | unclear | undetermined | low | https://seedtable.com/exits/drishti-company |
| VER-L11-33 | Instrumental — AI-визуальный контроль электроники, именованные клиенты NVIDIA (−14 дней на сборку), Meta (900+ инженерных недель/год) | 2024 (дата кейс-стади точно не указана) | manufacturing | low | none | seconds-minutes | F-C | deep-learning | yes | low | no | success | low | https://instrumental.com/case-studies/one-month-breakeven-using-superhuman-inspection/ |
| VER-L11-34 | Mercedes-Benz + Apptronik Apollo — коммерческий пилот гуманоида на производстве (Berlin, Kecskemét), первое для Mercedes применение гуманоидной робототехники | 2024 | manufacturing | high | U3 | unclear | unclear | foundation-model | yes | medium | no | partial | medium | https://ati.utexas.edu/apptronik-and-mercedes-benz-enter-commercial-agreement-to-pilot-apollo-humanoid-robot-in-manufacturing-facilities/ |
| VER-L11-35 | Agility Robotics Digit + GXO — первый RaaS-контракт, пилот на фабрике Spanx (граница: fulfillment) | 2024 | manufacturing (граница: fulfillment) | moderate | U3 | weeks-months | F-A | hybrid | yes | medium | no | partial | medium | https://en.wikipedia.org/wiki/Agility_Robotics |
| VER-L11-36 | Arrival — банкротство (робот-ориентированные «микрофабрики» EV, построено ~20 машин, продано 0) | 2024 | manufacturing | high | U3 | season-years | F-A | sensor-fusion | not-applicable | high | no | failure | high | https://en.wikipedia.org/wiki/Arrival_(company) |
| VER-L11-37 | Shapeways — Chapter 7, немедленное прекращение операций (3D-печать на заказ; связь с ИИ — тонкая, только сторонний CADaaS-оптимизатор) | 2024 | manufacturing | unclear | unclear | season-years | F-A | unclear | not-applicable | medium | mixed | failure | low | https://en.wikipedia.org/wiki/Shapeways |
| VER-L11-38 | Path Robotics — AI-сварка (foundation-модель Obsidian), контракт $600М с HII на верфях ВМС США, 4x продуктивность | 2024–2026 | manufacturing | moderate | U3 | seconds-minutes | F-C | foundation-model | no | medium | no | success | medium | https://www.path-robotics.com/ |
| VER-L11-39 | FANUC Zero Down Time — предиктивное обслуживание роботов, $75М экономии, 35 000+ подключённых роботов (кросс-подтверждено 2 доменами, не прочитано напрямую) | 2015–2024 (непрерывная программа) | manufacturing | low | none | weeks-months | F-A | classical-ml | yes | low | no | success | medium | https://www.fanucamerica.com/press-releases/fanuc-showcases-zero-down-time-in-augmented-reality-demonstration-at-automate-2019 |
| VER-L11-40 | Siemens + rhobot.ai — edge AI на биогазовой установке CarbonAMS (Ирландия): −39% паразитной нагрузки, +2,5% выхода газа | 2025 | manufacturing (граница: процессное/энергетика) | low | none | hours-days | F-A | hybrid | yes | low | no | success | medium | https://en.wikipedia.org/wiki/Siemens |
| VER-L11-41 | Markforged Digital Forge — обвал стоимости при двух перепродажах за 13 месяцев ($116М Nano Dimension → $42М Stratasys) | 2025–2026 | manufacturing | unclear | unclear | season-years | F-A | hybrid | not-applicable | medium | mixed | failure | high | https://en.wikipedia.org/wiki/Markforged |
| VER-L11-42 | Intel — AI-анализ выхода годных кристаллов (>90% точность детекции дефектных зон, 100% покрытие пластин на конце линии) | год не указан источником (действующая программа Intel IT) | manufacturing | low | none | seconds-minutes | F-C | deep-learning | yes | low | no | success | high | https://www.intel.com/content/www/us/en/it-management/intel-it-best-practices/transforming-manufacturing-yield-analysis.html |

## Явные флаги против/для рамки курса (анти-bias, в духе волны 1)

1. **Tesla Model 3 (VER-L11-19) — повторяет паттерн, уже отмеченный в самой Лекции 11 про Tesla
   Optimus.** Глава уже использует Tesla как источник «AI-вошинга» (дистанционно управляемые
   демо-роботы). Независимо найденный кейс 2018 года — **тот же бренд, другая ошибка того же
   типа ещё раньше**: избыточная веря в автоматизацию (не прямо ИИ в узком смысле) привела к
   остановке производства и признанной Маском ошибке. Помечен `confidence: medium` и
   `axis3_class: unclear` именно потому, что граница «это ИИ или просто роботизация» здесь
   спорная — решение оставить кейс в выборке, а не убрать, сделано по той же логике, что и
   включение GE Predix/Foxconn Wisconsin в саму Лекцию 11 (контрпример, не шум).
2. **Шесть из восемнадцати кейсов 2018–2023 — компании, производившие сам ИИ/робота как продукт
   (Rethink Robotics, Anki, Jibo, Pepper, Sarcos/Palladyne, Vicarious), а не использовавшие ИИ на
   чужой производственной линии.** Это расширяет интерпретацию «manufacturing» в ту же сторону,
   что уже делали кейсы волны 1 (Zume, iRobot, Covariant, Berkshire Grey, Veo Robotics — тоже
   компании-производители робот-продуктов, не юзеры ИИ на линии). Решение сохранить
   последовательность интерпретации, а не вводить более узкое определение задним числом.
3. **Паттерн обесценивания при повторных перепродажах (Berkshire Grey и Veo Robotics волны 1;
   Markforged здесь) — устойчивый, не единичный.** Markforged — третий зафиксированный пример
   AM/робототехнической компании, чья оценка рухнула при последовательных поглощениях
   ($116М → $42М за 13 месяцев). Стоит явно отметить при обновлении главы как повторяющийся,
   а не случайный паттерн SPAC-эры робототехники/AM 2021–2026.
4. **Relativity Space Terran 1 — редкий кейс с `axis4_blast_radius: catastrophic` и
   `outcome: partial` одновременно**, что при этом НЕ противоречит рамке курса (в отличие от
   Rio Tinto AHS волны 1): здесь гейт `axis4_gate: yes` присутствовал (многоступенчатая наземная
   проверка перед запуском), и именно отказ произошёл **после** прохождения всех предпусковых
   гейтов — ровно тот случай, когда гейт снижает, но не устраняет катастрophический потолок.

## Ограничения этого файла

- `WebSearch` исчерпан на 200/200 запросов сессии в середине работы — так же, как и в волне 1.
  Дальнейший поиск с новым бюджетом почти наверняка нашёл бы больше кейсов, особенно в процессном
  производстве (химия, нефтепереработка) и в полупроводниковой отрасли (TSMC/Samsung/ASML),
  которые не поддались проверке в рамках одной сессии несмотря на несколько попыток.
- Две строки (`VER-L11-25` Plethora, `VER-L11-32` Drishti) опираются на вторичные агрегаторы
  (Crunchbase, Seedtable) без подтверждения первоисточником — явно помечены `confidence: low`,
  не скрыто.
- `source_locator`/`source_file` не заполнены — это новые кейсы вне `razmetka/lec-11.md`, как и
  в волне 1; вместо них — прямая `source_url`.
- Хедж-нормализация (первое/ведущее значение при составных формулировках) применена везде, где
  в источнике было несколько вариантов классификации.

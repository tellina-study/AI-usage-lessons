---
title: "Лекция 11 (manufacturing) — независимо верифицированные кейсы, внешние источники"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 11 (manufacturing) — верифицированные кейсы вне материалов курса

## Подход к поиску

Цель — найти **независимо проверяемые** кейсы применения ИИ в производстве (предиктивное
обслуживание, визуальный контроль качества, робототехника на линии) с явным исходом, числом,
датой, названным инструментом и реальной ссылкой — не пересказ `library/lectures/lec-11/`.

Поиск шёл двумя инструментами: `WebSearch` (широкий поиск по компаниям/темам — Zymergen, Fast
Radius, Local Motors, Bright Machines, Zume, iRobot, Covariant, Berkshire Grey, Veo Robotics,
Desktop Metal, BMW+Figure, Siemens Amberg, Rio Tinto, Rolls-Royce, Foxconn+Nvidia, Hyundai+Boston
Dynamics, плюс попытки для TSMC/Intel/Micron/GE Aerospace/Caterpillar/ASML/Schaeffler/WEF Lighthouse
Network) и `WebFetch` (прямое чтение ~20 конкретных страниц — официальные пресс-релизы BMW,
Microsoft customer story, International Mining, Wikipedia, SEC-связанные источники — для проверки
дат и цифр после того, как `WebSearch` исчерпал лимит сессии в 200 запросов на середине работы).

**Важный отрицательный результат, который стоит знать явно: один найденный кейс был исключён как
вероятно сфабрикованный вторичным агрегатором.** Сайт `case-studies.ai` описал кейс «Ford + IBM
Maximo Visual Inspection» с очень подробными цифрами (150 млн инспекций, 26→0 браков на заводе Van
Dyke, ссылка на «WardsAuto, 10 июня 2026») — но прямая проверка (`ibm.com/case-studies`,
`wardsauto.com`, прямые URL пресс-релизов IBM) не нашла этой статьи ни в одном первичном источнике.
Сам домен `case-studies.ai` — по названию похож на кейс-стади, сгенерированные ИИ, а не
отредактированные журналистами. Кейс **не включён** в таблицу ниже — ровно по той причине, по
которой курс запрещает «кейсы из пальца»: источник не прошёл проверку, несмотря на правдоподобный
вид.

## Честный результат: нашёл 10 провалов, но только 5 успехов

**Задание требовало ≥10 успехов и ≥10 провалов. Провалов — 10, успехов — только 5.** Это не
подгонка слабых кейсов, это зафиксированный недобор после реального усилия (исчерпан лимит
`WebSearch`, дополнительно ~20 точечных `WebFetch` на правдоподобные URL официальных
пресс-релизов/Wikipedia/vendor case studies, несколько из которых дали 403/404 и не добавили
ничего). Структурная причина недобора, а не случайность поиска: **провалы AI/robotics-стартапов и
крах SPAC-сделок — заметно более «ищущийся» жанр новостей** (TechCrunch, Robot Report, SEC-фильтры
дают конкретные даты и суммы по самой природе события — банкротство, SPAC, расторжение сделки), в
то время как **успешные, продолжающиеся промышленные внедрения AI почти всегда документированы
только вендором** (Microsoft/AWS/Siemens/Landing AI customer stories) — лоссовый, самоотчётный
жанр источника, который либо не даёт точной даты, либо не называет клиента, либо даёт цифры без
независимого аудита. Два из пяти найденных успехов (Rio Tinto, Rolls-Royce) при этом пограничны по
отрасли или по качеству источника — см. колонку confidence и примечания под таблицей.

## Покрытие по годам

- **2022** — покрыт (3 провала: Zymergen, Fast Radius, Local Motors).
- **2023** — покрыт (2 провала: Bright Machines, Zume).
- **2024** — покрыт широко (4 провала: iRobot, Covariant, Berkshire Grey, Veo Robotics; 2 успеха:
  BMW+Figure 02, Rio Tinto AHS).
- **2025** — покрыт (1 провал: Desktop Metal; 1 успех: Rolls-Royce/Microsoft; 1 неопределённый:
  Foxconn+Nvidia Houston).
- **2026** — покрыт **только слабо**: нет ни одного нового события-провала или события-успеха,
  датированного именно 2026 годом с собственным исходом — есть только (а) академическая публикация
  2026 года *про* давно действующую систему Siemens Amberg (сама система — не новость 2026-го) и
  (б) неопределённый кейс Hyundai/Atlas (демо CES 2026, реальное внедрение — план на 2028). Честно:
  **2026 как год с собственным новым verified-исходом не закрыт.**

## Качество источников — честная оценка

- **Высокое:** Zymergen (SEC-фильтры + 2 независимых издания), Zume/iRobot/Berkshire Grey
  (Wikipedia + корпоративные пресс-релизы/SEC, широко подтверждено современной прессой), BMW+Figure
  02 (прямой официальный пресс-релиз BMW + 3 независимых отраслевых издания), Rolls-Royce (прямой
  официальный Microsoft customer story, дата подтверждена).
- **Среднее:** Fast Radius, Local Motors, Desktop Metal (Wikipedia без глубокой проверки
  AI-специфичности провала), Covariant, Veo Robotics (вторичная аналитика классифицирует как
  «провал», первичные факты по сделке подтверждены отдельно), Rio Tinto (сильные первичные цифры,
  но вендорская/корпоративная самоотчётность, плюс отраслевая граница — добыча, не производство).
- **Низкое:** Bright Machines (ключевое утверждение «рекламируемого AI не было» — из отзыва
  сотрудника на Glassdoor, не из независимой журналистики; факты о SPAC/увольнениях подтверждены
  отдельно), Siemens Amberg (цифры совпадают между двумя источниками, но один — факт-шит
  производителя, год системы и год публикации разошлись), Landing AI (кейс вендора, клиент не
  назван по имени, точная дата не дана).

## Таблица кейсов

| id | case_name | year | industry | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VER-L11-01 | BMW + Figure 02 (гуманоид, вставка деталей в кузовном цехе, Spartanburg) | 2024 | manufacturing | moderate | U3 | seconds-minutes | F-C | sensor-fusion | yes | low | no | success | high | https://newsroom.bmwgroup.com/americas/successful-test-of-humanoid-robots-at-bmw-group-plant-spartanburg |
| VER-L11-02 | Siemens Amberg Electronics Plant — AI-инспекция паяных соединений (edge, SIMATIC) | 2026 | manufacturing | low | none | seconds-minutes | F-C | deep-learning | yes | low | no | success | high | https://onlinelibrary.wiley.com/doi/10.1111/isj.70006 |
| VER-L11-03 | Rio Tinto + Komatsu AHS — автономные самосвалы Pilbara (300 шт., 10 участков) | 2024 | manufacturing (граница: добыча, не завод — см. примечание) | low | none | seconds-minutes | F-C | sensor-fusion | no | high | no | success | medium | https://im-mining.com/2024/08/12/komatsu-and-rio-tinto-herald-delivery-of-300th-autonomous-haul-truck/ |
| VER-L11-04 | Rolls-Royce IntelligentEngine / Azure Databricks — предиктивное обслуживание двигателей | 2025 | manufacturing | moderate | none | weeks-months | F-A | hybrid | yes | high | no | success | medium | https://www.microsoft.com/en/customers/story/23201-rolls-royce-azure-databricks |
| VER-L11-05 | Landing AI / LandingLens — CV-инспекция для неназванного японского автопроизводителя (через FPT) | 2023 (дата не указана источником, оценка) | manufacturing | low | none | seconds-minutes | F-C | deep-learning | unclear | low | no | success | low | https://case-studies.ai/use-cases/production-and-quality/PQ-001-manufacturing-quality-inspection/references/ |
| VER-L11-06 | Zymergen — крах IPO, продажа Ginkgo Bioworks за ~300 млн $ (пик $3 млрд) | 2022 | manufacturing | extreme | U1 | season-years | F-A | hybrid | no | high | no | failure | high | https://www.genengnews.com/news/synbio-synergy-ginkgo-to-acquire-troubled-zymergen-for-300m/ |
| VER-L11-07 | Fast Radius — банкротство Chapter 11 после SPAC (акции −95%+) | 2022 | manufacturing | unclear | unclear | season-years | unclear | unclear | not-applicable | high | mixed | failure | medium | https://en.wikipedia.org/wiki/Fast_Radius |
| VER-L11-08 | Local Motors — внезапное закрытие (Olli, IBM Watson, 3D-печать транспорта) | 2022 | manufacturing | unclear | unclear | season-years | F-A | hybrid | not-applicable | medium | unclear | failure | medium | https://en.wikipedia.org/wiki/Local_Motors |
| VER-L11-09 | Bright Machines — крах SPAC, смена CEO, увольнения (Израиль) | 2023 | manufacturing | unclear | unclear | season-years | unclear | unclear | not-applicable | medium | mixed | failure | low | https://www.calcalistech.com/ctechnews/article/b1fwyl009c |
| VER-L11-10 | Zume — полное закрытие (роботизированная «пицца в пути») | 2023 | manufacturing | moderate | U3 | season-years | F-B | rule-based | not-applicable | high | mixed | failure | high | https://en.wikipedia.org/wiki/Zume_Pizza |
| VER-L11-11 | iRobot — срыв сделки с Amazon из-за антимонопольных органов ЕС/США | 2024 | manufacturing | not-applicable | none | season-years | F-A | not-applicable | not-applicable | high | yes | failure | high | https://en.wikipedia.org/wiki/IRobot |
| VER-L11-12 | Covariant — «обратный acqui-hire» командой Amazon, независимая компания фактически прекратила существование | 2024 | manufacturing | moderate | U3 | season-years | F-A | foundation-model | not-applicable | medium | mixed | failure | medium | https://ideaproof.io/failure/covariant-ai |
| VER-L11-13 | Berkshire Grey — выкуп SoftBank за $375 млн (пик SPAC $2,7 млрд, −86%) | 2024 | manufacturing (граница: fulfillment-робототехника) | moderate | U3 | season-years | F-A | sensor-fusion | not-applicable | high | mixed | failure | high | https://en.wikipedia.org/wiki/Berkshire_Grey |
| VER-L11-14 | Veo Robotics — продажа Symbotic за $8,7 млн после $29 млн привлечённых | 2024 | manufacturing | low | none | season-years | F-A | sensor-fusion | not-applicable | medium | no | failure | medium | https://www.engineering.com/symbotic-acquires-veo-robotics/ |
| VER-L11-15 | Desktop Metal — Chapter 11 после покупки Nano Dimension (AI-генеративный дизайн Live Parts) | 2025 | manufacturing | unclear | unclear | season-years | F-A | hybrid | not-applicable | high | mixed | failure | medium | https://www.digitalengineering247.com/article/desktop-metal-files-for-bankruptcy |

### Дополнительные кейсы (не входят в счёт успех/провал — исход не определён)

| id | case_name | year | industry | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| VER-L11-16 | Foxconn + Nvidia Isaac GR00T — гуманоиды на заводе AI-серверов в Хьюстоне (анонс, запуск ожидается Q1 2026) | 2025 | manufacturing | unclear | unclear | unclear | unclear | foundation-model | unclear | unclear | no | undetermined | medium | https://www.theregister.com/2025/11/07/foxconn_humanoid_robots_nvidia_server/ |
| VER-L11-17 | Hyundai + Boston Dynamics Atlas — демо CES 2026 (дистанционное управление раскрыто), коммерческое внедрение заявлено на 2028 | 2026 | manufacturing | high | U3 | unclear | unclear | foundation-model | unclear | unclear | no | undetermined | high (на факте телеуправления) | https://bostondynamics.com/blog/ |

## Явные флаги против/для рамки курса (анти-bias)

1. **Rio Tinto AHS — прямой контр-пример «гейт — сильнейший предиктор».** `axis4_gate=no`
   (самосвал действует автономно без человеческой проверки перед каждым манёвром),
   `axis4_blast_radius=high` (многотонная техника в опасной среде) — и всё равно `outcome=success`
   с измеримыми цифрами (4,8 млрд тонн, +15% utilisation). По рамке файла `07-os4-gejt-i-vneshnij-shum.md`
   (83,3%→26,9%→13,3%→5,0% от низкого к катастрофическому blast radius без гейта) это должно было
   быть зоной провала — и это не так. Возможное объяснение (не проверено здесь) — многолетняя
   зрелость технологии (с 2008) и отраслевые инженерные гейты другого типа (остановка по датчикам
   препятствий), не учтённые колонкой `axis4_gate` в её текущем определении.
2. **Hyundai/Atlas — повторение паттерна Tesla Optimus из самой Лекции 11.** Глава уже использует
   Tesla Optimus (окт. 2024, роботы управлялись дистанционно) как «счётный случай AI-вошинга».
   Независимо найденный кейс Atlas/CES 2026 — **тот же паттерн на другом вендоре два года позже**:
   демонстрация, преподносимая как показатель автономности, раскрыта как управляемая дистанционно.
   Это не единичный инцидент одной компании, а, возможно, устойчивый паттерн жанра «гуманоид на
   производстве» — стоит явно отметить при обновлении главы.
3. **iRobot и Fast Radius — провалы, ортогональные всем трём осям курса**, в том же духе, что GE
   Predix/Foxconn Wisconsin уже зафиксированы в самой Лекции 11: iRobot упал не потому, что AI-модель
   отказала, а потому что антимонопольный регулятор заблокировал сделку (`external_driver=yes`);
   Fast Radius — крах SPAC-оценки, где роль самого AI в провале не установима из источника.
4. **Bright Machines — редкий кейс, где источник прямо утверждает, что заявленного AI не было
   вообще** («no clear vision… none of the advertised AI and so-called advanced technology» —
   отзыв сотрудника, не аудированный факт). Если это верно, это не «провал AI», а «провал
   AI-маркетинга без AI» — другая категория, которую три оси тоже не предназначены объяснять.

## Ограничения этого файла

- Результат получен за одну сессию с ограниченным бюджетом `WebSearch` (исчерпан на середине
  работы) — список НЕ претендует на полноту даже в рамках найденных 15 чистых + 2 неопределённых
  кейсов; дальнейший поиск с свежим бюджетом почти наверняка найдёт больше кейсов, особенно успехов.
- `source_locator`/`source_file` не заполнены — это новые кейсы, не из `razmetka/lec-11.md`;
  вместо этого дана прямая `source_url` (новая колонка, как и просил оркестратор).
- Хедж-нормализация (первое/ведущее значение) применена везде, где в источнике было составное
  утверждение — так же, как в каноническом реестре.

---

## Батч 2 (третья волна, 2026-11-20) — добавлено 21 кейсов: V11-018…V11-038

Полные таблицы с осями, описаниями и источниками — `../verified-cases-batch2/lec-11-verified-batch2.md` (файл provenance; локальные номера там — S1/F1/B2-S1 и т.п., НЕ финальные ID). Консолидация в `reestr-reshenij-verified.csv` — скриптом `build_verified_batch2.py` (дедуп + enum-валидация), разбор дублей — файл 18 §1.

Исключены при консолидации как дубли: Rethink Robotics — закрытие (то же событие, что L11-015); Tesla Model 3 «избыточная автоматизация» (то же событие, что L11-001/L12-001); Divergent 3D / Czinger 21C (дубль V05-003); Arrival — банкротство (тот же крах, что V12-017).

| final_id | case_name | year | outcome |
|---|---|---|---|
| V11-018 | Anki — банкротство производителя AI-робот-игрушек (Cozmo, Vector, Overdrive), $182,5М привлечено | 2019 | failure |
| V11-019 | Jibo — продажа активов NTT (здравоохранение/образование) после коммерческого провала социального робота | 2020 | failure |
| V11-020 | Creator — временное закрытие ресторана роботизированных бургеров из-за COVID-19 (статус после переоткрытия в Daly City не доведён до определённости) | 2020 | partial |
| V11-021 | Katerra — банкротство Chapter 11 (роботизированное модульное строительство, SoftBank, $2 млрд привлечено) | 2021 | failure |
| V11-022 | SoftBank Robotics Pepper — остановка производства из-за слабого спроса (~27 000 произведённых единиц) | 2021 | failure |
| V11-023 | Plethora Technology — поглощение Xometry, прекращение самостоятельной работы (AI/правило-based анализ технологичности CAD-моделей) | 2021 | undetermined |
| V11-024 | Vicarious AI — поглощение Alphabet/Intrinsic, команда расформирована между Intrinsic и DeepMind | 2022 | failure |
| V11-025 | Quanergy Systems — Chapter 11 после SPAC (лидар+ИИ для промышленной автоматизации), оценка $1,4 млрд до подачи | 2022 | failure |
| V11-026 | Relativity Space — первый запуск Terran 1 (ИИ-итерация дизайна + 3D-печать ракеты), не достиг орбиты из-за аномалии 2-й ступени | 2023 | partial |
| V11-027 | Audi — AI-контроль качества точечной сварки (WPS-Analytics), 1,5 млн сварных точек и 300 машин за смену в Neckarsulm | 2023 | success |
| V11-028 | Sarcos → Palladyne AI — отказ от производства промышленных экзоскелетов Guardian (план 500 ед./год → выпущено 2), переход в чистый софт | 2023 | failure |
| V11-029 | Drishti Technologies — поглощение Apple, видео-аналитика конвейеров (клиенты Ford, Denso, HELLA, Continental) | 2023 | undetermined |
| V11-030 | Instrumental — AI-визуальный контроль электроники, именованные клиенты NVIDIA (−14 дней на сборку), Meta (900+ инженерных недель/год) | 2024 | success |
| V11-031 | Mercedes-Benz + Apptronik Apollo — коммерческий пилот гуманоида на производстве (Berlin, Kecskemét), первое для Mercedes применение гуманоидной робототехники | 2024 | partial |
| V11-032 | Agility Robotics Digit + GXO — первый RaaS-контракт, пилот на фабрике Spanx (граница: fulfillment) | 2024 | partial |
| V11-033 | Shapeways — Chapter 7, немедленное прекращение операций (3D-печать на заказ; связь с ИИ — тонкая, только сторонний CADaaS-оптимизатор) | 2024 | failure |
| V11-034 | Path Robotics — AI-сварка (foundation-модель Obsidian), контракт $600М с HII на верфях ВМС США, 4x продуктивность | 2024 | success |
| V11-035 | FANUC Zero Down Time — предиктивное обслуживание роботов, $75М экономии, 35 000+ подключённых роботов (кросс-подтверждено 2 доменами, не прочитано напрямую) | 2015 | success |
| V11-036 | Siemens + rhobot.ai — edge AI на биогазовой установке CarbonAMS (Ирландия): −39% паразитной нагрузки, +2,5% выхода газа | 2025 | success |
| V11-037 | Markforged Digital Forge — обвал стоимости при двух перепродажах за 13 месяцев ($116М Nano Dimension → $42М Stratasys) | 2025 | failure |
| V11-038 | Intel — AI-анализ выхода годных кристаллов (>90% точность детекции дефектных зон, 100% покрытие пластин на конце линии) |  | success |

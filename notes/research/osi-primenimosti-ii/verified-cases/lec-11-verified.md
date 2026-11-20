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

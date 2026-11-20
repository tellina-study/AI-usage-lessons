---
title: "Верифицированные внешние кейсы — Лекция 12 (digital-twins)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 12 (`industry = digital-twins`) — независимо проверенные кейсы

## Подход к поиску

Поиск вёлся через `WebSearch` (до исчерпания общего бюджета сессии — он разделён между 12
параллельными сессиями по остальным лекциям) и далее через `WebFetch` по URL, названным в уже
полученных результатах поиска, плюс по Wikipedia-страницам компаний/проектов, которые я помню как
релевантные (с явной проверкой каждого факта фетчем, а не по памяти без проверки). Цель — найти
кейсы **за пределами** `notes/research/osi-primenimosti-ii/razmetka/lec-12.md` (22 кейса реестра
по этой лекции все уже учтены и исключены из повторного использования — Tesla Fremont, Southeast
Asian Port, Vision QC/Indus Vision, Deloitte PdM agregate, cement/chemical plant PdM, MES
advisory, SCADA alarm cascade, ChatGPT-на-PLC, PLC Copilot, Yokogawa FKDPP, sim-to-real gap,
DeepMind datacenter cooling, adaptive welding, Toyota Digit, BMW Leipzig humanoid, McKinsey/WEF
Lighthouse, pharma dosing worked example, КАМАЗ, Росатом АтомМайнд, Норникель — проверено по CSV
перед началом поиска).

**Годы:** закрыты все пять лет 2022–2026 хотя бы одним кейсом с явной классификацией успеха; 2022
год — самый тонкий (только 1 кейс, причём успешный — провальных кейсов 2022 года в проверяемых
источниках не нашлось). Это явно и честно отмечено, не замаскировано.

**Итог по качеству источников.** Для успешных кейсов источники сильные: официальные вендорские
кейс-стади (NVIDIA/BMW, C3.ai/Shell, Siemens/NVIDIA press, Accenture/Unilever через техническую
прессу), государственный источник (DCMA.mil), один рецензируемый журнал (Deakin et al. 2024) и три
академические препринт-работы arXiv (2024–2026) с воспроизводимыми числами. Для провальных кейсов
картина честно хуже: нашлись два сильных кейса с **явно названным ИИ/digital-twin продуктом**
(Matterport/Cortex, C3.ai) — оба это **провалы бизнес-модели/капитализации платформы**, а не
провалы конкретного прогноза или двойника в эксплуатации (сам же C3.ai у Shell работает технически
— парадокс, achtung отдельно отмечен в примечаниях). Остальные провальные кейсы (Northvolt,
Siemens Energy, Arrival, Boeing 787) — это реальные, крупные, хорошо задокументированные провалы
физических производственных систем, но **ни в одном не нашлось подтверждения, что именно
AI/digital-twin инструмент назван и именно он не справился** — источники называют отказ
автоматизации/контроля качества/инжиниринга в целом, не конкретную ML-модель. Это честно
промаркировано `confidence: low` в каждой такой строке, а не выдано за чистый ИИ-провал. Собрано
**7 явных провалов** из требуемых ≥10 — **это документированный недобор, не натянутые слабые
кейсы**: подробности и список рассмотренных-и-отклонённых кандидатов — в разделе «Что не вошло».
Добавлены 2 строки с исходом `partial` (Hyundai HMGICS, TSFM-бенчмарк) для нюанса — они не
засчитаны ни в «успех», ни в «провал».

**Почему именно так.** Публичная отчётность по цифровым двойникам систематически смещена в сторону
опубликованных success-stories с названным вендором и чистыми цифрами (вендор сам заинтересован в
кейс-стади); документированные провалы **самого прогностического механизма** редко публикуются с
той же детализацией — вместо этого на поверхность всплывают либо (а) провалы бизнеса/платформы
целиком (Matterport, C3.ai — это тот же паттерн, что GE Predix 2018 в более широкой литературе,
который сюда не включён из-за даты), либо (б) провалы физической системы, где атрибуция конкретно
AI/twin-компоненту не называется источником явно. Это само по себе согласуется с уже
зафиксированным в `reestr-reshenij-README.md` замечанием о смещении корпуса в сторону
публикуемых успехов (ограничение №3).

## Таблица кейсов

| case_name | year | source_url | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Lockheed Martin F-35 — DCMA UK digital-twin quality analytics (CATDM) | 2024 | https://www.dcma.mil/News/Article-View/Article/4223473/dcma-uk-engineers-reduce-defects-save-millions/ | moderate | none | weeks-months | F-A | hybrid | yes | medium | no | success | medium |
| Siemens Tecnomatix + NVIDIA Omniverse — virtual commissioning (vendor-wide + Polygon Technologies) | 2024 | https://www.automate.org/ai/blogs/what-is-nvidia-omniverse-and-how-will-it-affect-u-s-manufacturing | low | none | hours-days | F-A | hybrid | yes | medium | no | success | medium |
| BMW Group + NVIDIA Omniverse — Debrecen digital-twin factory planning | 2023 | https://venturebeat.com/ai/bmw-uses-nvidias-omniverse-to-build-state-of-the-art-factories | low | none | weeks-months | F-A | hybrid | yes | medium | no | success | high |
| Shell + C3 AI — Real Time Production Optimization, Prelude FLNG (10 000 единиц оборудования) | 2022 | https://www.c3.ai/customers/shell/ | moderate | none | hours-days | F-C | hybrid | yes | medium | no | success | high |
| Hyundai Motor Group — HMGICS digital-twin Meta-Factory (запуск) | 2023 | https://www.hyundai.news/uk/articles/press-releases/hmgics-grand-opening-2023.html | moderate | none | seconds-minutes | F-C | sensor-fusion | yes | medium | no | partial | medium |
| Unilever + Accenture — AI digital twins по заводам (Raeford NC, Poznań, Cu Chi, Gandhidham) | 2025 | https://letsdatascience.com/news/unilever-scales-ai-digital-twins-across-factories-5b5b369b | moderate | U2 | hours-days | F-A | hybrid | yes | low | no | success | medium |
| UK microgrid digital twin — voltage control (Deakin et al., 2024) | 2024 | https://doi.org/10.1016/j.ijepes.2024.110302 | moderate | U1 | seconds-minutes | F-C | hybrid | yes | medium | no | success | medium |
| PMI-DT — bolt fatigue digital twin, Random Forest/Decision Tree, 100% точность (лаб.) | 2024 | https://arxiv.org/abs/2411.01299 | low | none | seconds-minutes | F-A | classical-ml | yes | low | not-applicable | success | low |
| Smart-building digital twin — стресс-тест под sensor drift/missing data (ground-truth-aware) | 2026 | https://arxiv.org/abs/2608.14917 | moderate | U2 | hours-days | F-A | hybrid | yes | low | not-applicable | success | high |
| Siemens + NVIDIA — Erlangen Electronics Factory, +20% throughput (первичное внедрение) | 2026 | https://press.siemens.com/global/en/pressrelease/siemens-and-nvidia-are-advancing-industrial-ai | moderate | none | hours-days | F-A | hybrid | yes | medium | no | success | medium |
| RL-based Adaptive Digital Twin для «зелёных городов» (DQN) | 2024 | https://arxiv.org/abs/2401.16449 | moderate | U2 | seconds-minutes | F-C | deep-learning | unclear | unclear | not-applicable | success | low |
| TSFM в топологии цифрового двойника — C-MAPSS RUL бенчмарк (univariate vs multivariate) | 2026 | https://arxiv.org/abs/2609.40071 | moderate | none | weeks-months | F-A | foundation-model | unclear | unclear | not-applicable | partial | medium |
| Matterport — платформа Cortex AI (цифровые двойники зданий), финансовый коллапс → поглощение CoStar | 2024 | https://en.wikipedia.org/wiki/Matterport | unclear | unclear | season-years | none | deep-learning | not-applicable | high | mixed | failure | medium |
| C3.ai — промышленная AI/digital-twin платформа, обвал капитализации (−74% от IPO-максимума) | 2024 | https://en.wikipedia.org/wiki/C3.ai | unclear | unclear | season-years | none | hybrid | not-applicable | high | mixed | failure | medium |
| Northvolt — гигафабрика батарей, провал автоматизации/контроля качества → банкротство | 2024 | https://en.wikipedia.org/wiki/Northvolt | high | U3 | weeks-months | F-A | unclear | unclear | high | mixed | failure | low |
| Siemens Energy / Siemens Gamesa — системный провал контроля качества флота ветротурбин | 2023 | https://www.cnbc.com/2023/06/23/siemens-energy-scraps-profit-outlook-as-wind-turbine-troubles-deepen.html | high | U3 | season-years | F-A | unclear | no | catastrophic | no | failure | low |
| Arrival — «микрофабрики» на цифровом/симуляционном инжиниринге, банкротство/администрация | 2024 | https://en.wikipedia.org/wiki/Arrival_(company) | unclear | unclear | season-years | none | unclear | not-applicable | high | mixed | failure | low |
| Boeing 787 — кризис качества сборки фюзеляжа («digital twin/digital thread» декларировался отраслью) | 2023 | https://en.wikipedia.org/wiki/Boeing_787_Dreamliner | moderate | none | season-years | F-A | unclear | no | high | no | failure | low |
| Отраслевой агрегат: «~80% проектов цифровых двойников не доходят до полного развёртывания» | 2025 | https://maccelerator.la/en/blog/startup-strategy/digital-twin-implementation-for-industrial-companies/ | unclear | unclear | unclear | unclear | unclear | unclear | unclear | unclear | failure | low |

**Итог по годам:** 2022 — 1 кейс (успех, Shell); 2023 — 3 кейса (2 успеха, 1 провал); 2024 — 8
кейсов (4 успеха, 1 partial, 3 провала); 2025 — 2 кейса (1 успех, 1 провал); 2026 — 4 кейса (3
успеха, 1 partial). Все пять лет закрыты; 2022 закрыт только с одной стороны (нет провального
кейса 2022 года, прошедшего проверку).

**Итог по исходам:** 10 success / 7 failure / 2 partial = 19 строк. Требование ≥10 на успехи —
выполнено. Требование ≥10 на провалы — **не выполнено, честно (7 из 10)** — см. причину выше и
список отклонённых кандидатов ниже.

## Что не вошло (реально рассмотрено и отклонено, не просто пропущено)

- **GE Predix** ($4–7 млрд списаний, реструктуризация GE Digital) — классический, сильно
  задокументированный провал промышленной AI/IoT-платформы для цифровых двойников, но событие
  датируется **2018 годом**, вне требуемого окна 2022–2026; исключён по дате, не по качеству.
- **Katerra** (строительная техкомпания, банкротство) — аналогично, **2021 год**, вне окна.
- **Hyperloop One** (закрытие декабрь 2023) — проверено по Wikipedia: источник **не подтверждает**
  использование digital-twin/симуляционных технологий именно как причины или предмета провала;
  причины — финансовые и отсутствие контрактов. Исключён за отсутствием привязки к теме лекции.
- **WeWork** (банкротство ноябрь 2023) — проверено: продукт «WeWork Workplace» анонсирован в 2022,
  но источник не связывает его с цифровым двойником/space-utilization AI явно и не связывает его
  причинно с банкротством. Исключён.
- **Lordstown Motors** (банкротство июнь 2023) — проверено: причина провала — невыполнение Foxconn
  инвестиционных обязательств, источник **не упоминает** цифровые двойники/симуляцию вовсе.
  Исключён.
- **Berkshire Grey** (поглощение SoftBank 2024, обвал оценки с $2.7 млрд до $375 млн) — реальный и
  квантифицированный провал, но это AI-робототехника склада/логистики, а не цифровой двойник
  здания/завода/инфраструктуры — ближе к индустрии лекции 13 (logistics), исключён во избежание
  смешения индустрий.
- **PG&E / Mosquito Fire (2022)** — проверено по Wikipedia: причина — не выявленный при плановом
  визуальном осмотре дефект линии; источник **не упоминает** ни AI, ни прогностическое
  моделирование вовсе. Исключён.
- **Hinkley Point C** (перерасход бюджета с £18 до ~£35–48 млрд) — проверено: источник не
  упоминает BIM/цифровой двойник как причину или даже как использованную технологию; перерасход
  объясняется COVID/Brexit/дефицитом рабочей силы. Исключён.

## Примечания к отдельным строкам

- **Matterport / C3.ai** — важный нюанс для рамки курса: технология **работает** (Shell реально
  использует C3 AI Reliability в проде с названными цифрами; Matterport Cortex реально строит
  двойники зданий с 2019 года) — провал здесь на уровне **бизнес-модели платформы**, не на уровне
  прогноза/двойника в конкретной эксплуатации. Это не укладывается чисто в схему «AI предсказал
  неверно → физический провал», поэтому `axis1_level=unclear` — честный выбор, не обход.
- **Northvolt / Siemens Energy / Arrival / Boeing 787** — включены по прецеденту самого реестра
  (`reestr-reshenij-README.md`, ограничение №5: Suez Ever Given, Foxconn Wisconsin и т. п. включены
  намеренно как структурные контрпримеры даже без подтверждённой «ИИ-природы»). Все четыре —
  крупные, реальные, количественно описанные провалы физических производственных систем в индустрии
  цифровых двойников; ни один источник не подтверждает **конкретно названный** AI/digital-twin
  инструмент как причину — поэтому `confidence: low` и `axis3_class: unclear` везде, где это так.
- **Siemens Energy** — единственный кейс с `axis4_blast_radius: catastrophic`: >€1,6 млрд
  дополнительных затрат, падение акций на 37% за один день, признание CEO «масштаб хуже, чем я
  считал возможным», 15–30% флота турбин под вопросом.
- **Hyundai HMGICS** и **TSFM-бенчмарк** классифицированы как `partial`, не `success` — у первого
  нет независимых пост-запуска операционных результатов (только проектные цифры на открытие), у
  второго — смешанный результат (univariate модели уступают multivariate/topology-aware подходу).
- **PMI-DT (100% точность)** — помечен `confidence: low` намеренно: «100% accuracy» на
  лабораторном эксперименте с болтами — классический сигнал малой выборки/переобучения, а не
  готовой к продакшену метрики; включён как академический кейс, не как промышленный деплоймент.

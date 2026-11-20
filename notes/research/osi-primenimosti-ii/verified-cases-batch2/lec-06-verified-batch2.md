---
title: "Внешне верифицированные кейсы — Лекция 6 (CAD-CAM), волна 2 (батч 2)"
type: research
issue: "#349"
date: 2026-11-20
---

# Лекция 6 (CAD-CAM) — батч 2: 23 независимо верифицированных кейса

## Подход и честная оговорка по процессу

Задание на эту лекцию разбилось на три параллельные поднаправления (генеративный дизайн/
топологическая оптимизация; CAM/траектории/DFM-автоматизация; surrogate-CAE/LLM-копилоты/
документированные провалы). Третье поднаправление (генеративный дизайн) после двух раундов
собственной рекурсивной делегации нашло 11 реальных кандидатов (GE Jet Engine Bracket Challenge,
Bugatti брейк-суппорт, Renishaw+British Cycling, Northrop Grumman, MX3D мост, Atherton Bikes и
др.), но **не успело привести их к формату реестра** (нет полной классификации по всем осям) —
решение оркестратора: не форсировать классификацию под давлением времени, зафиксировать как
честную потерю, а не включать под risk ошибочной разметки. Ниже — только два поднаправления,
прошедшие полный цикл проверки и классификации без потерь.

Итог: **23 кейса вместо целевых 25** — таков был реальный результат после вычета недоведённой
до формата трети выборки. Это не недобор качества, а честный artifact процесса делегации.

## Кейсы: CAM / траектории / DFM-автоматизация (11)

Хронологическое покрытие **2021–2025**; 2018–2020 честно не закрыты (после истощения
WebSearch-бюджета сессии не удалось найти проверяемые именованные AI-CAM/DFM/quoting кейсы
этого периода через прямой WebFetch — более старые релевантные вещи это скорее классическая
алгоритмическая CAM-оптимизация без ML, например Celeritive VoluMill, сознательно не притянута
под «ИИ»).

| case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CloudNC CAM Assist — Frerotech | 2025 | https://www.cloudnc.com/case-studies/frerotech-exploring-ai-in-cam-programming | Нидерландский precision-машшоп (12 чел.) сократил время CAM-программирования на 60–95% с помощью AI-генератора траекторий CAM Assist | moderate | U3 | hours-days | F-A | hybrid | yes | low | no | success | high |
| CloudNC CAM Assist — Bedford CNC (Andy Soos) | 2025 | https://www.cloudnc.com/case-studies/andy-soos-cam-assist | Британский CNC-шоп автоматизировал до 80% CAM-программы за минуты, рост выручки за счёт большего потока заказов | moderate | U3 | hours-days | F-A | hybrid | yes | low | no | success | medium |
| CloudNC CAM Assist — Avalanche Energy | 2025 | https://www.cloudnc.com/news-room/cam-assist-now-used-by-over-1-000-machine-shops-globally-to-accelerate-cnc-programming-with-ai | Стартап термоядерной энергетики сэкономил 3 месяца программирования за 6 месяцев использования CAM Assist | moderate | U3 | hours-days | F-A | hybrid | yes | medium | no | success | high |
| CloudNC CAM Assist — Arcamed | 2024 | https://www.cloudnc.com/case-studies/arcamed-applying-cam-assist-to-accelerate-surgical-case-and-tray-production | Производитель хирургических кейсов/лотков автоматизировал 75% CAM-процесса с помощью AI, цель — 90–100% | moderate | U3 | hours-days | F-A | hybrid | yes | medium | no | success | high |
| CloudNC CAM Assist — Paragon Space Development | 2024–2025 | https://www.cloudnc.com/case-studies/paragon-space-development-increasing-throughput-in-space-manufacturing-with-cam-assist | Производитель систем жизнеобеспечения для пилотируемых космических аппаратов получил 40–50% роста эффективности программирования на 6 станках силами одного программиста | moderate | U3 | hours-days | F-A | hybrid | yes | high | unclear | success | high |
| CloudNC CAM Assist — Xeon NC | ~2024–2025 | https://www.cloudnc.com/case-studies/xeon-nc | CNC-шоп сократил программирование детали с ~60 до ~12 минут (≈80% экономии), избежав найма доп. программистов | moderate | U3 | hours-days | F-A | hybrid | yes | low | no | success | high |
| Paperless Parts AI-quoting — Harris Manufacturing | ~2022–2023 | https://www.paperlessparts.com/case-studies/harris-manufacturing-doubles-quote-turnaround-speed-reveals-critical-profit-margin-insights/ | Swiss-CNC производитель сократил срок выдачи квоты с ~1 недели до 1 дня, пропускная способность квотирования ×5 | moderate | U3 | weeks-months | F-B | hybrid | unclear | low | no | success | high |
| Paperless Parts AI-quoting — IA Engineers | 2022 | https://www.paperlessparts.com/case-studies/ia-engineers-grows-customer-base-by-4x-and-brings-win-rate-to-100-with-paperless-parts/ | Производитель автоматизированных машин поднял win-rate с 30–40% до 100% и выручку на 250% за 5 месяцев | moderate | U3 | weeks-months | F-B | hybrid | unclear | low | no | success | high |
| Paperless Parts AI-quoting — Pindel Global Precision | ~2021 | https://www.paperlessparts.com/case-studies/pindel-global-precision-doubles-its-number-of-annual-quotes-increases-win-rate-by-30-with-paperless-parts/ | Aerospace/medical/firearms CNC-производитель удвоил число квот (375→700/год), +30% win-rate, ускорение квоты с 60+ до ~10 минут | moderate | U3 | weeks-months | F-B | hybrid | unclear | low | no | success | high |
| Fictiv — Automated DFM for Injection Molding | 2024 | https://www.fictiv.com/articles/announcing-fictivs-automated-injection-molding-dfm | AI-платформа Fictiv добавила автоматический DFM-анализ литья в реальном времени при загрузке CAD; функционал подтверждён, числовой метрики эффекта нет | moderate | U3 | weeks-months | F-A | hybrid | yes | low | no | undetermined | medium |
| ModuleWorks / TU Wien / craftworks — SurfAIce | 2022–2024 | https://www.moduleworks.com/surfaice-roughness-prediction-through-a-self-learning-machine-tool/ | Госфинансируемый прикладной проект самообучающегося станка, предсказывающего шероховатость поверхности по параметрам резания; итоговых количественных результатов в открытом доступе не найдено | high | U2 | seconds-minutes | F-C | classical-ml | unclear | medium | yes | undetermined | medium |

**Отброшено явно (не включено):** Xometry AI instant quoting (противоречивые источники — один первоисточник прямо говорит, что движок не на AI/ML, второй с цифрами вернул 403), Machina Labs (эндорсменты без привязки к измеренному кейсу), Caron Engineering TMAC (анонимизированные кейсы без названия компании), Sandvik Coromant CoroPlus / Bystronic ByOptimizer / Siemens Analyze MyWorkpiece / Path Robotics / Fraunhofer IPT (404/навигация без контента).

## Кейсы: surrogate-CAE / LLM-копилоты / документированные провалы (12)

Все источники открыты лично через WebFetch (SEC EDGAR первичные 10-K, сайты вендоров, arXiv
abstracts) — после полного истощения WebSearch-бюджета сессии (0/200 осталось уже до первого
запроса). Баланс исхода: 4 success, 4 partial, 2 failure, 2 undetermined — 8 из 12 не являются
чистым success.

| case_name | year | source_url | Описание (1 строка) | axis1_level | axis1_mechanism | axis2_bucket | axis2_mechanism | axis3_class | axis4_gate | axis4_blast_radius | external_driver | outcome | confidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Neural Concept × MAHLE (EV-вентилятор) | 2025 | https://www.neuralconcept.com/case-studies/mahle | AI-surrogate CFD/тепловая модель для дизайна вентилятора EV-охлаждения MAHLE — заявлено +15% энергоэффективности за один цикл проектирования | moderate | U3 | seconds-minutes | F-A | deep-learning | yes | medium | no | success | medium |
| Neural Concept × Jaguar Land Rover (аэродинамика) | 2024–2025 | https://www.neuralconcept.com/ | AI-surrogate для аэродинамики JLR: число оцениваемых в продакшене дизайнов выросло с 50 до 1500 в сутки (×30) | moderate | U3 | seconds-minutes | F-A | deep-learning | yes | medium | no | success | medium |
| Neural Concept × General Motors (безопасность пешеходов) | 2024 | https://www.neuralconcept.com/ | AI-surrogate, обученный на данных 11 автомобильных программ GM, для анализа безопасности пешеходов — качественное улучшение без единой числовой метрики | high | U3 | weeks-months | F-A | deep-learning | yes | high | mixed | undetermined | low |
| PhysicsX × GB1 (яхта America's Cup) | 2024 | https://www.physicsx.ai/ | AI-surrogate для аэродинамической оптимизации британской лодки America's Cup — ускорение перебора вариантов, результат не квантифицирован | moderate | U3 | seconds-minutes | F-A | deep-learning | yes | medium | no | undetermined | low |
| Physics-Guided Spectral ROM (мех. трансмиссия / цикл Брайтона / вихри Кармана) | 2026 | https://arxiv.org/abs/2607.18133 | Академическая работа документирует, что обычные параметрические surrogate/ROM-модели «теряют надёжность» за пределами диапазона обучающих данных; физика-ориентированный метод даёт ошибку <1% в 2 из 3 систем | high | U2 | seconds-minutes | F-A | hybrid | not-applicable | unclear | no | partial | medium |
| Nonintrusive ROM — лопатка турбины высокого давления | 2018 | https://arxiv.org/abs/1812.07228 | Неинтрузивный ROM для лопатки турбины: экстраполяция циклической нагрузки за 6.5 часов вместо 9.5 суток эталонного расчёта (×35) | moderate | U3 | hours-days | F-A | hybrid | yes | high | no | success | medium |
| GenCAD-Self-Repairing | 2025 | https://arxiv.org/abs/2505.23287 | Базовая генеративная CAD-модель GenCAD выдаёт ~10% геометрически невалидных дизайнов; метод самовосстановления устраняет 2/3 таких случаев | moderate | U3 | seconds-minutes | F-A | deep-learning | yes | low | no | partial | high |
| Generative Design AI для шасси CubeSat (ADOT) | 2026 | https://arxiv.org/abs/2607.28217 | AI+FEA generative-design инструмент для шасси спутниковой миссии: полезен на этапе брейншторминга, но выход не готов к производству, «чёрный ящик», трудоёмкая настройка | high | U3 | weeks-months | F-A | hybrid | yes | medium | no | partial | medium |
| GNN-surrogate для краш-деформации B-стоек кузова | 2025 | https://arxiv.org/abs/2503.17386 | Графовая нейросеть-surrogate предсказывает краш-деформацию штампованных стальных B-стоек — на 52% точнее базовых методов | moderate | U3 | seconds-minutes | F-A | deep-learning | yes | high | mixed | success | medium |
| ML-модель краш-динамики на датасете Body-in-White | 2025 | https://arxiv.org/abs/2510.15201 | ML-surrogate на датасете Body-in-White (150 МКЭ-расчётов) ускоряет краш-симуляцию кузова, но «пока не достигает точности полного МКЭ-расчёта» | high | U3 | seconds-minutes | F-A | deep-learning | yes | high | mixed | partial | medium |
| Markforged — Blacksmith / Digital Forge | 2020–2026 | https://www.sec.gov/Archives/edgar/data/1816613/000095017025046869/mkfg-20241231.htm | «AI-powered» платформа запущена 2020 → SPAC 2021 (~$215М) → going concern в 10-K 2024 (убыток $85.6М) → продажа Nano Dimension за $116М (2025) → перепродажа Stratasys за ~$42М (2026) | unclear | none | season-years | none | hybrid | not-applicable | high | mixed | failure | high |
| Velo3D — Flow (CAM print-prep) + going concern | 2022–2024 | https://www.sec.gov/Archives/edgar/data/1825079/000182507924000008/velo-20231231.htm | ПО подготовки печати Flow описано в 10-K как «продвинутые вычислительные алгоритмы» (слова AI/ML в отчётности НЕТ); going concern 2022–2024 из-за нарушения финансовых ковенантов | unclear | unclear | season-years | none | unclear | not-applicable | high | mixed | failure | low |

**Отброшено явно:** Fast Radius (банкротство без установленной связи с ИИ — тот же антипаттерн, что прошлая волна уже поймала), Carbon 3D printing (нет доступной детальной Wikipedia-статьи), Markov/Google Nature chip-placement reproducibility (вне скоупа — EDA/чипы), PINN-кейс гибридного digital twin железобетонной балки (сознательно не включён — категория PINN уже использована).

## Сводка батча

23 кейса: **13 success, 4 partial, 4 undetermined, 2 failure** (пересчитано построчно при сборке
этого файла). Годы: 2018 (1),
2021 (1), 2022 (1), 2023 (1), 2024 (4), 2025 (8), 2026 (3), приблизительные годы (~2021–2025) у
3 кейсов Paperless Parts/CloudNC Xeon NC. Пересечений с 21 кейсом волны 1 и с существующим
`razmetka/lec-06.md` нет — проверено по названиям вручную при сборке этого файла оркестратором.

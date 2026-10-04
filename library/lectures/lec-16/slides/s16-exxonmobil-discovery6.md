---
id: s16
type: case_with_chart
duration_min: 2
assertion: "ExxonMobil Discovery 6 — 4 032 NVIDIA Grace Hopper. 4D-сейсмика месяцы → недели. Stabroek Block Гайана: $1B+ unlock на 6 FPSO."
learning_goal: "Q3 HPC + Stabroek case"
chapter_ref:
  parts: [chapter-part2.md]
  sections: ["§2.4 ExxonMobil Discovery 6"]
visual:
  type: image
  description: "Stabroek FPSO photo OR HPE Cray EX4000 + ExxonMobil announcement"
  source_url: "https://corporate.exxonmobil.com/news/news-releases"
  acquisition_tier: 3
visible_numbers: ["4 032 NVIDIA Grace Hopper", "$1 млрд+ unlock на 6 FPSO Stabroek", "4D-сейсмика: месяцы → недели"]
russification_check: "ExxonMobil, Discovery 6, NVIDIA, Grace Hopper, Stabroek, Guyana, HPE Cray, EX4000, Eni HPC6, Aramco — brand list; «4D-сейсмика» inline gloss = «3D + время»; «плавучая платформа добычи-хранения-выгрузки (FPSO)»."
speaker_notes_target_words: 230
---

# ExxonMobil Discovery 6: 4D-сейсмика — недели. Stabroek Guyana — $1B+ unlock.

## Visible content

Заголовок: «ExxonMobil Discovery 6 — 4D-сейсмика месяцы → недели» (28pt deep ocean).
Sub: «HPE Cray EX4000, 4 032 NVIDIA Grace Hopper, 4× compute vs Discovery 5. $200-400M capex (оценка, [VFY])» (16pt italic)

**Слева — Ocean rounded box «Что делает Discovery 6»:**

- **4D-сейсмика** (= 3D + ось времени) — модели подземных коллекторов **месяцы → недели** (gold).
- Активное управление пластом в реальном времени.
- **Stabroek Block Гайана** (ExxonMobil-operated): 9-11 млрд BOE recoverable estimate.
- Контекст для масштаба: Permian-Pioneer ExxonMobil = ~16 млрд BOE.
- **$1 млрд+ unlock value** на первых 6 FPSO Stabroek (= ~30-40% от планируемой capacity).

**Справа — Ocean rounded box «HPC-сравнение Q3»:**

| Параметр | Eni HPC6 | Discovery 6 | Aramco METABRAIN |
|---|---|---|---|
| Compute | 14k AMD MI250X | 4 032 Grace Hopper | Internal + 250B params |
| Capex | $104M | $200-400M [VFY] | Не раскрыт |
| Top500 | #5 декабрь 2024 | не входит публично | N/A |

**Bottom bar:**

«Anti-hype: «4× compute» ≠ «4× business value». ExxonMobil не публикует сравнительные результаты Discovery 5 vs 6 на одной задаче с той же business метрикой.»

## Speaker notes

В первой половине 2025 года ExxonMobil развернула Discovery 6 — суперкомпьютер на базе HPE Cray EX4000 с четырьмя тысячами тридцатью двумя NVIDIA Grace Hopper Superchip. Это четырёхкратное увеличение вычисления мощности относительно Discovery 5. Капитальные затраты публично не раскрыты, но по аналогии с Eni HPC6 — оценочно двести-четыреста миллионов долларов; требует уточнения.

Что Discovery 6 делает. Главное — 4D-сейсмика. Это 3D-сейсмика, повторяемая во времени; четвёртое измерение — время; используется для мониторинга движения флюида в пласте в процессе разработки. Обработка моделей подземных коллекторов сжимается с месяцев до недель. Это критично для активного управления пластом на действующих месторождениях.

Stabroek Block в Гайане. ExxonMobil — оператор Stabroek, одного из крупнейших offshore нефтяных открытий двадцать первого века. Stabroek estimate — девять-одиннадцать миллиардов BOE recoverable. Для контраста: Permian-Pioneer ExxonMobil после слияния 2024 — шестнадцать миллиардов BOE. Discovery 6 unlock — один миллиард плюс долларов value на первых шести плавучая платформа (FPSO); плавучая платформа (FPSO) — это плавучая платформа добычи, хранения, выгрузки нефти. Первые шесть плавучая платформа (FPSO) — это около тридцати-сорока процентов от планируемой кап.acity Stabroek.

Сравнение HPC (высокопроизводительные вычисления)-стратегий. Eni выбрал AMD как эффективный по затратам per FLOP. ExxonMobil выбрал NVIDIA Grace Hopper как доминирующий в ML workloads. Aramco — комбинация HPC (высокопроизводительные вычисления) плюс базовая модель. Все три — проприетарные. Это значит, что рынок HPC (высокопроизводительные вычисления) для нефтегаза не «коммодизируется», как hyperscaler cloud — каждый major имеет свой стек.

Anti-hype в HPC (высокопроизводительные вычисления)-гонке. Цифры вычисления мощности впечатляют, но не равны business value. «Четыре икс» означает только вычисления throughput, не business value.

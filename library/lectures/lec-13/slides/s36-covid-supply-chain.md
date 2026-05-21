---
id: s36
type: assertion_visual
duration_min: 2
assertion: "COVID 2020: глобальный обвал цепочек поставок. Точно-в-срок + ML прогноз спроса = хрупкая система. Человеческое exception-управление спасло."
learning_goal: "COVID supply chain meltdown + JIT fragility"
learning_outcomes: [LO2, LO7]
chapter_ref: "§4.1 — COVID 2020"
failure_bucket: strict_in
references: []
visual:
  pattern: failure_chronology_3_phases
  primary: "3 phases COVID supply chain: Mar 2020 shock / 2020-2021 chaos / 2022+ recalibration"
---

# COVID 2020: точно-в-срок не работает на black-swan

## Три фазы

- **Март-Апрель 2020. Initial shock.** Lockdowns в Wuhan → Italy → Spain → US → globally за 6 недель. Demand для consumer goods spike (toilet paper, electronics, home equipment). Demand для travel-related goods collapse.
- **2020-2021. Chaos.** Ports congested (Long Beach 109 ships waiting in October 2021). Container rates spike 5-10×. Just-in-time supply chains broke. PPE shortage. Microchip shortage shaping auto industry recovery.
- **2022+. Recalibration.** Companies built buffer inventory, multi-source supply, nearshoring (Mexico for US, Turkey/Vietnam for Europe). «Just-in-case» вместо «just-in-time».

## Что не работало

- **ML demand forecasting** — модели обучены на pre-COVID distribution. Точность упала на порядок.
- **Optimization solvers** для inventory — заданная stationary demand, реальность non-stationary.
- **Real-time analytics dashboards** — данные есть, но decisions требовались from human judgment.

## Что РАБОТАЛО

- **Human exception management.** Procurement teams вынуждены были manually rebuild supply chains через crisis.
- **Scenario planning.** Компании с pre-built сценариями (например, post-SARS планы на Asian disruption) могли respond быстрее.
- **Diversified supply base.** Multi-source не «inefficient redundancy» — это resilience.
- **Cash reserves.** Компании с buffer cash могли buy through scarcity.

## Lesson — JIT fragility

- **Just-in-time** — это zero-buffer inventory model, designed для stationary demand + reliable supply.
- **На black-swan distribution shift** — JIT превращается в shortage и lost sales.
- **Just-in-case** — это alternative с buffer inventory; cost higher, но resilient.

## Pedagogical point

«Inventory оптимизация через ML» — это marketing pitch для stationary world. В world с regular black-swans (COVID 2020, Houthi 2024, Suez 2021, US-China trade tensions, climate disruptions) **buffer + multi-source + scenario planning** работает лучше.

## Speaker notes

COVID 2020 — это очень knowable пример из живой истории. Я хочу остановиться на этом две минуты не потому, что мы все его помним — а потому, что lessons для логистики все ещё recurring.

Три фазы. Март-апрель 2020 — initial shock. Lockdowns в Wuhan, потом Italy, потом Spain, потом US, потом globally — за шесть недель. Demand для consumer goods spike — toilet paper, electronics, home equipment (work from home). Demand для travel-related collapse.

2020-2021 — chaos. Ports congested. Long Beach один — сто девять кораблей waiting в октябре 2021 года. Container rates spike в пять-десять раз. Just-in-time supply chains broke. PPE shortage. Microchip shortage shaping auto industry recovery — некоторые автопроизводители ждали месяцы для chip deliveries.

2022 и далее — recalibration. Companies built buffer inventory. Multi-source supply вместо single source. Nearshoring — Mexico для US, Turkey и Vietnam для Europe. «Just-in-case» вместо «just-in-time». Это структурный shift в supply chain philosophy.

Что не работало в COVID. ML demand forecasting. Модели были обучены на pre-COVID distribution — два-три года стабильного consumer behavior. После lockdowns distribution полностью изменилось. Точность упала на порядок. Не chic decline — это полный distribution shift.

Optimization solvers для inventory — то же. Они работают при stationary demand assumption. Реальность была extremely non-stationary.

Real-time analytics dashboards — данные были, но они показывали symptom (congestion, delays), а decisions требовались from human judgment. ML alerts «something is wrong» не помогали — все знали something is wrong.

Что РАБОТАЛО. Human exception management. Procurement teams вынуждены были manually rebuild supply chains через crisis. Это была неделя за неделей координация. Phone calls. Emergency negotiations. Manual updates в ERP.

Scenario planning. Компании с pre-built сценариями (например, post-SARS планы 2003 года на Asian disruption) могли respond быстрее. Это бенефит от длинной memory корпорации.

Diversified supply base. Multi-source не «inefficient redundancy» — это resilience. Compania, у которой два-три supplier для каждого critical SKU, выжили лучше, чем те, у которых один Asian supplier на каждый SKU.

Cash reserves. Компании с buffer cash могли buy through scarcity, paying premium для critical inputs. Без cash reserves — производство останавливалось.

Lesson — JIT fragility. Just-in-time — это zero-buffer inventory model. Designed для stationary demand плюс reliable supply. На black-swan distribution shift — JIT превращается в shortage и lost sales. Just-in-case — это alternative с buffer inventory. Cost higher, но resilient.

Pedagogical point. «Inventory оптимизация через ML» — это marketing pitch для stationary world. В world с regular black-swans — COVID 2020, Houthi 2024, Suez 2021, US-China trade tensions, climate disruptions — buffer plus multi-source plus scenario planning работает лучше, чем ML.

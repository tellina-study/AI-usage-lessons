---
id: s08
type: assertion_visual
duration_min: 2.5
assertion: "Maxar Sentry — predictive intelligence suite: ML над архивом ~250 ПБ + multi-sensor tipping (EO + SAR + AIS). Детекции в часах после съёмки."
learning_goal: "Главный коммерческий пример Sense + anti-hype: «AI-derived» = оркестрация классики + ML"
learning_outcomes: [LO1a, LO1b]
chapter_ref: "§1.2 — Спутниковая аналитика"
references: [defense-one-2025-maxar, businesswire-2025-maxar-sentry]
visual:
  pattern: assertion_visual
  primary: "BEFORE/AFTER satellite snippet + sidebar с метриками + anti-hype caveat"
---

# Maxar Sentry — predictive intelligence в часах, не днях

## Assertion

Maxar Sentry — predictive intelligence suite: ML над архивом ~250 ПБ + multi-sensor tipping (EO + SAR + AIS). Детекции в часах после съёмки.

## Visual

Слайд разделён на 2 колонки.

Слева (60%) — крупный BEFORE/AFTER pair satellite imagery, обрамлённый Ocean rounded box. На AFTER-снимке — нарисованные bounding boxes Primary mid 2pt с подписями «new structure», «coastline change» (12pt italic). Caption под парой: «Maxar Sentry · change detection · автоматическая cross-cueing» 12pt italic.

Справа (40%) — 4 info-card компактных, каждая Ocean rounded box:
- **250 ПБ** архив (gold-выделение числа) — высокого разрешения, 20+ лет
- **NGA Luno A D01** — главный контракт
- **3 сенсора → fusion** — EO + SAR + AIS
- **Часы после съёмки** — не дни (gold)

Внизу — caveat 12pt italic Primary light: «Anti-hype: "AI-derived" в маркетинге = suite оркестрации классической CV + change detection + multi-sensor tipping, не одна foundation model».

Source footer 12pt italic: «Defense One, BusinessWire — июнь 2025».

## Speaker notes

К 2026 году в коммерческой спутниковой аналитике сложилась устойчивая четвёрка игроков с похожими бизнес-моделями: запуск собственных спутников высокого разрешения, ML-надстройка над архивом снимков, продажа сервиса разведывательным агентствам и коммерческим клиентам. Maxar Sentry — самый яркий из них.

Sentry запущен 25 июня 2025 года как «predictive intelligence suite». Компания продаёт его как способность видеть кризисы до того, как они развернутся. Под капотом — ML-модели над архивом около 250 петабайт снимков плюс мульти-сенсорное cross-cueing: электро-оптика, радар с синтезированной апертурой и автоматическая идентификационная система судов. Главный контракт — NGA, National Geospatial-Intelligence Agency, программа Luno A D01, в рамках которой Maxar обязан выдавать AI-генерируемые детекции самолётов, кораблей и техники в часах после съёмки.

Теперь анти-hype оговорка, важная для инженерного слуха. Бренд «AI-derived detection» в этом сервисе часто означает не один LLM-class model, а оркестрацию из классических методов компьютерного зрения, change detection и multi-sensor tipping. Maxar Sentry — это suite, не одна модель; «AI-derived» в маркетинге не равно «foundation model under the hood». Это нормально и инженерно правильно — маркетинговый язык просто опережает технический. Когда вы будете оценивать вакансию или предложение к сотрудничеству от подобного вендора, помните: за словом «AI» может стоять и foundation model, и хорошо отлаженный pipeline классических методов. Это разные инженерные стеки и разные карьерные траектории.

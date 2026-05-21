---
id: s20
type: failure_case
duration_min: 2
assertion: "FarmWise wind-down 2025; Naïo €4M → €2,4M (–40%) judicial recovery 2025. Причина: CV-стек, обученный в тепличных условиях, ломается в пыль / shadow bias / переменное освещение. AP2b — mechanical weeders как deterministic альтернатива."
learning_goal: "AP2b genuine не-AI альтернатива vs AP2a"
learning_outcomes: [LO5]
chapter_ref: "§2.5 Часть 2 — Strict-in F5 FarmWise + Naïo"
references: [farm-progress-2025, arxiv-2508-shadow-bias, mdpi-agri-2024]
visual:
  pattern: cause_alternative_2col
  primary: "Слева — failure causes (CV в пыли + shadow bias + переменное освещение); справа — AP2b альтернатива mechanical weeders (Lemken, Kverneland)"
---

# FarmWise wind-down + Naïo recovery — open-environment ломает CV

## Assertion

FarmWise wind-down 2025; Naïo €4M → €2,4M (–40%) judicial recovery 2025. Причина: CV-стек, обученный в тепличных условиях, ломается в пыль / shadow bias / переменное освещение. AP2b — mechanical weeders как deterministic альтернатива.

## Visual

Двухколоночный layout.

**Левая колонка (50%) — Failure causes:**

Сверху — photo FarmWise робота (или Naïo Orio) в поле с visual occlusion от пыли. Caption 12pt italic: «FarmWise / Naïo — структурная причина wind-down».

Под фото — 3-mini-cards в Ocean rounded box:

1. **Пыль (visual occlusion)** — деградация качества изображения с CV-камер
2. **Переменное освещение** — тени от облаков меняют контраст за минуты
3. **Shadow bias** — модель классифицирует тени как растительность (arXiv 2508.19511)

Под mini-cards — финансовая динамика:
- **FarmWise** — wind-down 2025; машины в полях без сервиса
- **Naïo Technologies** (Toulouse) — judicial recovery июнь 2025
- Revenue: €4M (2021) → €2,4M (2024), **–40%** ★ gold accent

**Правая колонка (50%) — AP2b альтернатива:**

Photo механического weeder (Lemken Steketee EC-Weeder или Kverneland Onyx) обрамлённое Ocean rounded box. Caption: «Mechanical weeder · deterministic robust».

Под фото — callout в Teal-tint box:
- **AP2b. Genuine не-ИИ альтернатива.** Когда CV-стек структурно не выдерживает open-environment условий — mechanical weeders дают deterministic robust решение **без ИИ-стека**.
- Lemken Steketee EC-Weeder; Kverneland Onyx
- Менее «smart», но: устойчивы к пыли / дождю / теням; без firmware updates; без cloud dependency; без CV-failure modes

Под callout — **критическое различение AP2a vs AP2b**:
- **AP2a** = другой класс AI (sensor-fusion вместо CV)
- **AP2b** = НЕ-AI (механика вместо AI)
- Не путать!

Footer 12pt italic: «Источники: Farm Progress 2025; arXiv 2508.19511 (shadow bias); MDPI Agriculture systematic review 2024».

## Speaker notes

Второй L2-провал, структурно близкий к Monarch, но в другой нише: FarmWise и Naïo Technologies.

FarmWise — CV-weed-robot, основан 2016 году, привлёк более тридцати миллионов долларов — объявил wind-down в 2025-м. По сообщениям, заказчики оставлены в подвешенном состоянии, машины в полях без сервисной поддержки. Naïo Technologies — французская компания из Тулузы, autonomous weeding robots Oz, Dino, Orio — вошла в judicial recovery, французский эквивалент Chapter 11, в июне 2025-го. Финансовая динамика Naïo: выручка четыре миллиона евро в 2021-м, два и четыре десятых миллиона в 2024-м — падение примерно на сорок процентов.

Структурная причина обоих провалов — одна и та же, и она задокументирована в академической литературе: arXiv статья от августа 2025-го «Weed Detection in Challenging Field Conditions: Semi-Supervised Framework for Overcoming Shadow Bias» и обзор MDPI Agriculture 2024 года. Модели компьютерного зрения, обученные в тепличных условиях, плохо работают в реальном поле. Конкретные механизмы деградации: пыль создаёт визуальное перекрытие (visual occlusion) камер. Переменное освещение — тени от облаков меняют контраст за минуты. Shadow bias — модель учится классифицировать тени как растительность; это типичная ошибка при недостаточно разнообразном датасете. Морфологическое сходство культурных растений и сорняков на ранних стадиях роста. Деградация качества изображения приводит к классификационным ошибкам — снижение общей точности с заявленных девяноста процентов в тестах до пятидесяти-шестидесяти в реальном поле. Это именно та цифра, которая выводит unit-economics фермера в минус.

И вот здесь критическое разделение, которое мы будем использовать в следующих разделах. AP-два-б — genuine не-ИИ альтернатива. Когда CV-стек структурно не выдерживает open-environment условий — механические weeders дают deterministic robust решение без ИИ-стека. Lemken Steketee EC-Weeder; Kverneland Onyx — это менее «smart», но детерминистски устойчивы к пыли, дождю, теням; не требуют firmware updates; не зависят от cloud connectivity; не имеют CV-failure modes. Это категорически другой класс альтернативы, отличный от того, который мы рассмотрим через слайд — в случае Cognitive Pilot и ИТЭЛМА.

И ключевое различение, без которого студент сделает неправильный вывод. AP-два-а и AP-два-б — это разные вещи. AP-два-а — выбор архитектуры внутри ИИ-домена: CV против sensor-fusion-AI. AP-два-б — выбор не-ИИ альтернативы: механика вместо AI. Не путать. Студент, прочитавший только AP-два-а, может ошибочно заключить, что ИИ всегда побеждает, если правильно выбран класс. Студент, прочитавший только AP-два-б, может ошибочно заключить, что ИИ всегда хуже механики. Оба вывода неверны. Правильный вывод — выбор зависит от природы среды и характера задачи, и инженерное умение — распознать, какой из двух случаев перед нами в конкретной ситуации.

## Источники

- Farm Progress (2025).
- arXiv 2508.19511 (август 2025) — shadow bias.
- MDPI Agriculture systematic review (2024).

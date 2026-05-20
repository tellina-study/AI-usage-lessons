---
id: s23
type: assertion_visual
duration_min: 1.5
assertion: "Decide — когда не AI: 2 критерия. Long-tail edge cases + life-and-death без HITL."
learning_goal: "Критерии 3-4 для Decide — закрытие раздела"
learning_outcomes: [LO3]
chapter_ref: "§2.7 — Когда не AI для Decide"
references: []
visual:
  pattern: matrix
  primary: "2 criterion cards + закрывающий takeaway"
---

# Decide — два критерия «когда не AI»

## Assertion

Decide — когда не AI: 2 критерия. Long-tail edge cases + life-and-death без HITL.

## Visual

Под assertion — 2 равные крупные criterion cards в Ocean rounded box:

**Критерий 3 (long-tail)** — badge gold «#3»
- **Long-tail edge cases с low ML confidence**
- Иконка `circle-help` 48px
- «Если задача — decision в области, где модель часто встречается с примерами вне обучающего распределения, automation bias масштабирует ошибки»
- Нужен structured abstention: «AI говорит "не знаю" и эскалирует человеку»
- Engineering требование: calibrated uncertainty + explicit threshold + UI который показывает неуверенность

**Критерий 4 (life-and-death)** — badge gold «#4»
- **High-stakes life-and-death без HITL**
- Иконка `shield-alert` 48px
- «Cost-asymmetry FP↔FN слишком велика для чисто статистического решения»
- Lavender — канонический контрпример (3 700 ошибочно помеченных)
- Формальный HITL обязателен — и должен быть РЕАЛЬНЫМ, не вырожденным в 20-сек подпись
- Metric «сколько времени у оператора на review» = формальная категоризация системы

Внизу — закрывающий takeaway-row 18pt italic Primary mid: «Decide — звено самое тонкое. LLM-hype опаснее всего. AI — accelerator, не decision-maker».

## Speaker notes

Из разобранных провалов извлекаем два критерия для звена Decide — критерии 3 и 4 общей нумерации матрицы Раздела 5.

Критерий третий — long-tail. Long-tail edge cases с низкой ML confidence. Если задача — это decision в области, где модель часто встречается с примерами вне обучающего распределения, automation bias масштабирует ошибки. Здесь нужен structured abstention: AI говорит «не знаю» и эскалирует человеку, а не AI выдаёт наиболее вероятный класс. Это требует engineering: calibrated uncertainty, явный threshold для эскалации, UI который показывает неуверенность.

Критерий четвёртый — life-and-death без HITL. High-stakes life-and-death без редундантности или формального HITL. Cost-asymmetry FP↔FN слишком велика для чисто статистического решения. Lavender — канонический контрпример. Если потенциальная цена ошибки — человеческая жизнь, формальный HITL обязателен, и он должен быть реальным, а не вырожденным в 20-секундную подпись. Engineering metric «сколько времени у оператора на review» — это формальная категоризация системы.

Подытог раздела Decide. Звено, в котором LLM-хайп опаснее всего. Доступны мощные инструменты — Palantir MSS, Scale Donovan плюс Defense Llama, Helsing Altra, Anthropic Claude через Palantir IL6. Их рост быстрый, контракты крупные. Параллельно — задокументированные провалы: Lavender показывает, что «90% accuracy» — wrong metric для life-and-death; Lancet — что demo не равно production; Vincennes 1988 — что UI под стрессом ломается даже без AI, и этот урок применим к LLM-output под временным давлением. Российский слой представлен Svod и Glaz-Groza с явным single-source caveat. Два критерия «когда не AI» сформулированы для long-tail edge cases и для life-and-death без real HITL.

Дальше — третье звено цепи. Act.

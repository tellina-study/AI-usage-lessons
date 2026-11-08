---
id: s17
type: assertion_visual
duration_min: 1.5
assertion: "Decide — звено, где LLM-хайп опаснее всего. «Accuracy 90%» звучит хорошо до момента, когда 10% — это тысячи человек."
learning_goal: "Зачем Decide — самое тонкое звено OODA; multi-modal foundation models"
learning_outcomes: [LO1a, LO2]
chapter_ref: "§2.1 — Что такое «Decide»"
references: []
visual:
  pattern: assertion_visual
  primary: "Decide stack illustration + cost-asymmetry callout"
---

# Decide — звено, где LLM-хайп опасен

## Assertion

Decide — звено, где LLM-хайп опаснее всего. «Accuracy 90%» звучит хорошо до момента, когда 10% — это тысячи человек.

## Visual

Под assertion — главная композиция в 2 уровня.

Верхний уровень — горизонтальный pipeline: 4 input типа (text reports / image / map / telemetry) → fusion box → COA recommendation. Иконки Lucide 32px Primary mid. Стрелки RIGHT_ARROW.

Нижний уровень — gold callout-блок (gold-tint fill, gold stroke), занимает всю ширину слайда:
- Слева крупно «10% × 37 000 = 3 700» (60pt bold Primary deep, «3 700» в gold)
- Справа 16pt italic: «Lavender, Газа 2023-2024. 90% accuracy в life-and-death = 3 700 человек, помеченных по ошибке. Метрика была не той»

Под callout — sub-caption 14pt italic: «Если потенциальная цена ошибки — человеческая жизнь, "accuracy %" — это не показатель качества, это показатель того, сколько кошмаров вы готовы принять».

## Speaker notes

«Decide» в OODA — это переход от наблюдения к выбору действия. В аэрокосмическом и оборонном контексте это семейство задач: mission planning — планирование операций; target identification and nomination — идентификация и предложение цели; multi-source fusion — объединение разнородных источников разведки в одну картину ситуации; decision support для командира — краткие сводки, варианты с оценкой исходов.

В отличие от Sense, где ML опирается на обучаемые сенсорные features, в Decide LLM и foundation models обрабатывают смешанный input: текстовые отчёты, изображения, тактические карты, бортовые телеметрии. Это территория multi-modal foundation models, и именно сюда заходят все главные US labs — Anthropic, OpenAI; все Chinese labs — DeepSeek, Qwen в military context; и все классические defense-vendors — Palantir, Scale, Helsing.

Главный для нашего слуха момент я хочу проиллюстрировать одним числом: 10 процентов от 37 тысяч — это 3 700. Эта арифметика — это пред-просмотр канонического разбора Lavender, который мы сделаем через четыре слайда. Если модель ошибается в 10 процентах случаев и применяется к 37 тысячам человек, ошибка масштабируется в тысячи людей. И самое главное: «accuracy 90 процентов» в маркетинговых проспектах звучит хорошо. Но «accuracy» как метрика проектировалась под симметрию: FP и FN — равноценны. В life-and-death это никогда не правда. FP — это жизнь невинного человека, и эта жизнь дороже, чем «упустить оперативника». Метрика «accuracy» обнуляется в этом контексте как honest measure.

Anti-hype оговорка по всему разделу: инфраструктура — FedRAMP HIGH, IL4, IL6, SC2S, SIPR, JWICS — это authorization-стек, не модель. Вендор может пройти IL6 и при этом иметь слабую модель; модель может быть мощной и при этом не получить авторизацию. Эти две оси оценивают отдельно.

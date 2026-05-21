---
id: s30
type: assertion_visual
duration_min: 1.5
assertion: "Четыре типа провалов на процессном: RL drift / regulatory blocker / OT-IT раскол / vendor PR без metrics."
learning_goal: "Failure-pattern matrix процессного"
learning_outcomes: [LO2, LO8]
chapter_ref: "§3 wrap-up"
failure_bucket: strict_in
references: []
visual:
  pattern: failure_matrix_2x2
  primary: "Матрица 2×2 типов провалов процессного с примерами"
---

# Четыре типа провалов на процессном

## Тип 1: RL distribution drift

**Кейсы:** batch transitions; смена feedstock; seasonal shifts; equipment wear.

**Где видно:** любая попытка autonomous RL без CIRL-обвязки.

**Урок:** RL дополняет MPC на high-level scheduling. MPC — safe fallback.

## Тип 2: Regulatory blocker

**Кейсы:** FDA Part 11 запрещает autonomous batch release; ATEX Zone 0 запрещает non-certified hardware; Указ 250 требует domestic software на КИИ.

**Где видно:** фарма, химия в Zone 0, российская промышленность.

**Урок:** регуляторика already exists, AI fits existing frameworks. HITL + audit trail обязательны.

## Тип 3: OT/IT раскол на uncertain edge

**Кейсы:** LLM-задержка 100–500 мс не вмещается в PLC-цикл 1–10 мс. Eventually-consistent IT не работает в strong-consistency OT.

**Где видно:** любая попытка автоматизации низкого уровня (L0–L1 ISA-95) через облачные модели.

**Урок:** edge ML на копроцессоре, не LLM. Latency = determinism.

## Тип 4: Vendor PR без metrics

**Кейсы:** ММК / НЛМК / Северсталь общие декларации; некоторые западные вендоры тоже.

**Где видно:** там, где decline в публичном disclosure — крупные публичные компании в кризисный квартал.

**Урок:** три вопроса (baseline / окно / вмешательства). Если уклончивый ответ — red flag.

## Speaker notes

Резюме раздела 3 — failure-pattern matrix процессного производства. Симметрично разделу 2, четыре типа провалов.

Тип 1 — RL distribution drift. Мы разобрали детально на s26. Batch transitions, смена feedstock, seasonal shifts, equipment wear. Все четыре механизма ломают RL-политику без warning. Где видно: любая попытка autonomous RL без CIRL-обвязки. Урок: RL дополняет MPC на high-level scheduling. MPC — safe fallback на низкоуровневом замыкании контура.

Тип 2 — regulatory blocker. FDA Part 11 запрещает autonomous batch release в фарма; ATEX Zone 0 физически запрещает non-certified AI hardware; Указ 250 требует domestic software на КИИ-объектах в России. Где видно: фарма, химия в Zone 0, российская промышленность. Урок: регуляторика already exists. AI должен fit existing frameworks, не наоборот. HITL и audit trail обязательны в safety-critical контурах.

Тип 3 — OT/IT раскол на uncertain edge. LLM-задержка 100-500 миллисекунд не вмещается в PLC-цикл 1-10 миллисекунд. Eventually-consistent поведение IT не работает в strong-consistency мире OT. Где видно: любая попытка автоматизации низкого уровня — L0 и L1 ISA-95 — через облачные модели. Урок: edge ML на копроцессоре, не LLM. Latency = determinism, не только speed.

Тип 4 — vendor PR без metrics. ММК, НЛМК, Северсталь — общие декларации без конкретных цифр. Некоторые западные вендоры тоже — особенно те, кто в кризисный квартал. Где видно: там, где decline в публичном disclosure совпадает с corporate stress. Урок: три вопроса — baseline, окно, перечень вмешательств. Если ответы уклончивые — red flag, требует углубления.

Запомните эти четыре типа. В §4, на следующих слайдах, они станут конкретными критериями категорий «человек», «данные», «стоимость», «регуляторика». Failure-matrix процессного — это эмпирическая база для категорий рамки решения.

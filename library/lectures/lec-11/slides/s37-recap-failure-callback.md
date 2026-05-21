---
id: s37
type: assertion_visual
duration_min: 2
assertion: "Discrete: CV + коботы + копилоты. Process: мягкие сенсоры + MPC/RL + PdM + регуляторика. Общее: foundation models как дополнение, застревание на пилотной стадии universal."
learning_goal: "Recap + explicit failure-callback"
learning_outcomes: [LO1a, LO1b, LO2]
chapter_ref: "§5.1 recap"
failure_bucket: strict_in
references: []
visual:
  pattern: keystone_recap_with_callback
  primary: "Двухколонная схема (recap s05) + явный failure-callback ниже"
---

# Recap двухколонной схемы + failure-callback

## Дискретное (левая колонна) — что мы разобрали

CV-инспекция (BMW + TSMC + Boeing); эталонная разметка как cornerstone.

Прогностическое обслуживание + OEE callback.

Коботы + Toyota Jidoka 2.0.

**Failure-урок:** чрезмерная автоматизация (Tesla 2018) / сдвиг распределения / scarce labels / vendor self-claim.

## Процессное (правая колонна) — что мы разобрали

Мягкие сенсоры (BASF + Pfizer Vox).

MPC / RL гибрид + CIRL (Yokogawa-JSR).

PdM на границе + детерминизм edge-вывода (POSCO + Holcim).

Регуляторика (FDA / ATEX / Указ 250).

**Failure-урок:** RL distribution drift / regulatory blocker / OT-IT раскол / vendor PR.

## Общий слой

Foundation models как **augmentation, не controller** (3 причины: задержка, галлюцинации, сертификация).

**Застревание на пилотной стадии universal** — 95% не доходят до production (MIT Sloan 2025).

4 категории критериев + 5-step framework + 4 вопроса к вендору.

## Explicit failure-callback (формула)

**«Завтра вендор обещает –70% downtime — задайте 3 вопроса (baseline / окно / вмешательства) + 4-й OEE-вопрос.**

**Если ответы расплывчатые — это demo, не production.**

**95% пилотов не доходят до production не потому что AI плох, а потому что инженеры не задают эти вопросы.»**

## Speaker notes

Recap двухколонной схемы. Дискретное и процессное — две модели производства, AI входит в обе, но по-разному.

В дискретном мы разобрали: компьютерное зрение для контроля качества — BMW GenAI4Q, TSMC, Boeing fuselage. Эталонная разметка как cornerstone — стоимость разметки vs объём данных. Прогностическое обслуживание с OEE callback — vendor обещает –25% downtime, нужен OEE breakdown. Коботы и Toyota Jidoka 2.0 — augment, не replace.

Failure-урок дискретного: чрезмерная автоматизация — Tesla 2018; сдвиг распределения при смене продукта; scarce labels и class imbalance; vendor self-claim без baseline.

В процессном мы разобрали: мягкие сенсоры — BASF Geismar и Pfizer Vox. MPC / RL гибрид с CIRL — Yokogawa-JSR FKDPP. PdM на границе и детерминизм edge-вывода — POSCO 180 nodes. Регуляторика — FDA Part 11, ATEX, Указ 250.

Failure-урок процессного: RL distribution drift; regulatory blocker; OT-IT раскол на uncertain edge; vendor PR без metrics.

Общий слой для обеих колонн. Foundation models — Siemens IFM, FoxBrain — это augmentation для инженера, не autonomous controller. Три причины: задержка вывода 100-500 мс, галлюцинации, сертификация. Эти причины не уходят со временем.

Застревание на пилотной стадии — universal. 78 процентов используют AI, 5,5 процентов high performers. 95 процентов пилотов не доходят до production. Это не свойство одной отрасли, это структурная картина 2025-2026 года.

И теперь — explicit failure-callback. Я хочу, чтобы вы выучили это формулой и могли применить завтра.

«Завтра вендор обещает –70 процентов downtime. Задайте три вопроса: baseline до AI, окно измерения, перечень вмешательств. Плюс четвёртый вопрос про OEE — какой компонент эффективности улучшается. Если ответы расплывчатые — это demo, не production. 95 процентов пилотов не доходят до production не потому, что AI плох, а потому что инженеры не задают эти вопросы».

Это лекция была про то, как стать тем инженером, который задаёт. Не про AI-восторг. Не про AI-скептицизм. Про критическое суждение в применении AI к промышленности.

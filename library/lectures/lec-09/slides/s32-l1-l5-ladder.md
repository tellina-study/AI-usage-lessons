---
id: s32
type: assertion_visual
duration_min: 3.5
assertion: "Лестница автономии L1-L5: каждый уровень — операциональное определение «что делает AI / что делает человек» + ms-to-intervention."
learning_goal: "L1-L5 ladder — центральный visual меты-раздела; границы L3↔L4 и L4↔L5"
learning_outcomes: [LO7]
chapter_ref: "§4.1 — Лестница L1-L5"
references: []
visual:
  pattern: schema_layered
  primary: "Лестница 5 уровней + примеры + ms-to-intervention + границы"
---

# Лестница автономии L1-L5 — операциональные определения

## Assertion

Лестница автономии L1-L5: каждый уровень — операциональное определение «что делает AI / что делает человек» + ms-to-intervention.

## Visual

Под assertion — центральная схема: 5 горизонтальных рядов снизу вверх (как лестница, bottom-aligned), каждый Ocean rounded box, color-coded от safer (L1, Primary light) до critical (L5, gold-warning):

**L1 — Assistive** (Primary light bg)
- AI: выдаёт detections; Человек: решает
- Пример 2026: **Palantir MSS analyst surface**
- ms-to-intervention: **минуты-часы** (human-paced)

**L2 — Semi-auto perception** (Primary light bg)
- AI: рекомендует action; Человек: авторизует каждое
- Пример: **Saker Scout target lock confirmation**
- ms-to-intervention: **seconds**

**L3 — Supervised autonomy** (Primary mid bg, white text)
- AI: executes в pre-authorised envelope; Человек: supervises
- Пример: **Anduril Fury wingman (CCA Increment 1)**
- ms-to-intervention: **100-1000 ms**

**L4 — Pre-authorised auto-engage** (Teal bg, white text)
- AI: engages по pre-set ROE; Человек: может intervene
- Пример: **Patriot auto mode, S-400 auto ROE**
- ms-to-intervention: **<100 ms**

**L5 — Full LAWS** (gold-warning bg, dark text)
- AI: executes lethal без human authorisation; Человек: вне loop
- Пример: **Currently debated, not deployed**
- ms-to-intervention: **N/A — вне loop**

Справа от лестницы — 2 boundary callout:

**Граница L3 ↔ L4** (Teal-tint box)
- «**Engineering debate**: pre-authorisation envelope насколько узок?»

**Граница L4 ↔ L5** (gold-warning tint)
- «**Treaty debate** в UN GGE»
- «Даже Lavender формально L4-edge (20 sec human), не L5»

Внизу — caption 12pt italic Primary light: «Студент-инженер должен сказать про конкретную систему, НА КАКОМ УРОВНЕ она сидит. Не "автономная" — а "L3 с envelope шириной X"».

## Speaker notes

Чтобы говорить о границе «где можно, где нельзя», нужна общая шкала. В индустрии используется лестница L1-L5 — концептуальный аналог SAE-уровней автономности для автомобилей. Это не SAE J3016 буквально — тот про автомобили, — и не единственная классификация. Но к 2026 году L1-L5 сложилась как наиболее цитируемая операциональная шкала для автономии оружия и систем поддержки решений.

Ключ — на каждом уровне явно сказано, что делает AI и что делает человек. Без этого «уровень» — пустое слово.

L1, Assistive. AI выдаёт information и detections. Человек решает, действовать ли. Пример 2026 — Palantir MSS analyst surface. ms-to-intervention — минуты-часы, human-paced.

L2, Semi-auto perception. AI рекомендует action — target lock, route. Человек авторизует каждое действие. Пример — Saker Scout target lock confirmation. ms-to-intervention — секунды.

L3, Supervised autonomy. AI executes action в pre-authorised envelope. Человек supervises и может intervene. Пример — Anduril Fury wingman, CCA Increment 1. ms-to-intervention — 100-1 000 миллисекунд.

L4, Pre-authorised auto-engage. AI engages target по pre-set ROE — rules of engagement. Человек может intervene, но не required в loop. Пример — Patriot auto mode, S-400 auto ROE. ms-to-intervention — менее 100 миллисекунд.

L5, Full LAWS. AI executes lethal action без human authorisation. Человек вне loop. Currently debated, not deployed.

Внимание к двум границам.

Граница L3 ↔ L4 — это место инженерного спора. Pre-authorisation envelope — насколько он узок? Если оператор pre-authorised «открой огонь по любому объекту, входящему в зону Х, классифицированному как враг», и эта зона — большой город, — это уже de facto L5, прикрытая бумажкой L4. «Pre-authorisation envelope» — это формальное юридическое понятие, которое инженерия должна квантифицировать.

Граница L4 ↔ L5 — это место юридического спора в UN GGE. L5 — fully autonomous lethal action — формально не deployed нигде, и переговоры в UN GGE именно про то, чтобы зафиксировать это в международном праве. Даже Lavender в Газе формально требует human approval перед strike — пусть и 20-секундным — то есть формально L4-edge, не L5.

Pedagogical takeaway. Студент-инженер должен уметь сказать про конкретную систему, на каком уровне она сидит. Не «эта система автономная», а «эта система L3, с pre-authorisation envelope шириной X». Это и есть профессиональный язык в этой области.

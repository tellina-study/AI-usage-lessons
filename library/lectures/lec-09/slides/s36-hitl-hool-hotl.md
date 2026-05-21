---
id: s36
type: assertion_visual
duration_min: 3
assertion: "HITL / HOOL / HOTL — инженерная триада. Граница HOOL → HOTL формально определяется engineering decision «сколько ms у оператора на intervention»."
learning_goal: "Триада + mapping на L1-L5; engineering takeaway про ms-to-intervention"
learning_outcomes: [LO7, LO3]
chapter_ref: "§4.6 — HITL/HOOL/HOTL"
references: []
visual:
  pattern: schema_architecture
  primary: "3 human figures относительно AI-loop + mapping L1-L5"
---

# HITL / HOOL / HOTL — инженерная триада человеческого контроля

## Assertion

HITL / HOOL / HOTL — инженерная триада. Граница HOOL → HOTL формально определяется engineering decision «сколько ms у оператора на intervention».

## Visual

Под assertion — главная композиция: 3 panel layout horizontal Ocean rounded box, в каждой — stick figure человека относительно AI-цикла (визуализирован circle/loop):

**Панель 1 — HITL** (Primary light bg)
- Заголовок: «**Human-In-The-Loop**»
- Stick figure ВНУТРИ петли (icon-схема)
- AI cycle: detect → human approve → act → detect
- Description 14pt: «Человек в КАЖДОЙ decision-point. AI не действует без явной authorisation»
- **Mapping: L1, L2**
- Примеры:
  - Palantir MSS analyst
  - Saker Scout operator confirmation

**Панель 2 — HOOL** (Primary mid bg, white text)
- Заголовок: «**Human-On-The-Loop**»
- Stick figure НАД петлёй (supervises)
- AI cycle: detect → act → detect (без явного human gate)
- Description: «Человек supervises, может intervene, но НЕ required»
- **Mapping: L3, L4**
- Примеры:
  - Fury CCA wingman (pilot oversees)
  - Patriot auto ROE (operator monitors)

**Панель 3 — HOTL** (gold-warning bg, dark text)
- Заголовок: «**Human-Out-of-The-Loop**»
- Stick figure ВНЕ петли (за стенкой)
- AI cycle: detect → act (closed loop без человека)
- Description: «Человек ВНЕ execution-loop, нет real-time intervention»
- **Mapping: L5** (treaty-discussion)

Внизу — большой engineering callout (Teal-tint, full-width):
- **«Сколько ms у оператора на intervention» = ФОРМАЛЬНАЯ категоризация системы**
- 14pt italic: «10 секунд — HOOL. 200 мс — формально HOOL, фактически HOTL. 5 мс — инженерно HOTL. Это имеет правовые последствия в новом международном режиме»

Внизу — small italic 12pt: «Mitigation patterns: calibrated uncertainty · abstention pathways · structured outputs · mandatory human gates для kinetic».

## Speaker notes

Самая важная mental model этого раздела — триада уровней человеческого контроля над AI-циклом. Эта секция — продолжение L1-L5 ladder: те же уровни автономии, но взгляд с противоположной стороны. Что делает не AI, а человек.

HITL, Human-In-The-Loop. Человек в каждой decision-point. AI не действует без явной human authorisation. Mapping на L1-L5: L1, L2. Примеры: Palantir MSS analyst, Saker Scout operator confirmation.

HOOL, Human-On-The-Loop. Человек supervises AI-цикл, может intervene в любой момент, но не required в каждой decision-point. Mapping: L3, L4. Примеры: Fury CCA wingman — пилот oversees; Patriot auto ROE — оператор monitors.

HOTL, Human-Out-of-The-Loop. Человек вне execution-loop, не имеет real-time intervention capability. Mapping: L5 по определению treaty-discussion.

Что в этой триаде важно для инженера-выпускника? Граница HOOL → HOTL — это место, на которое заточены DoD Directive 3000.09 плюс UN GGE rolling text плюс ICRC position. И эта граница формально определяется engineering decision: сколько миллисекунд у оператора есть на intervention.

Если у оператора есть 10 секунд — это HOOL. Если у него 200 миллисекунд — формально HOOL, фактически HOTL: человек не успевает осознать, что происходит, тем более intervene. Если у него 5 миллисекунд — это уже инженерно HOTL.

Engineering takeaway. «Сколько миллисекунд у оператора на intervention» — это формальная категоризация системы, и она имеет правовые последствия в новом международном режиме. Если ваша система упирается в этот вопрос, ответ должен быть зафиксирован в системных требованиях, не в маркетинге.

Mitigation patterns. Calibrated uncertainty — модель показывает свою неуверенность, не скрывает. Abstention pathways — структурное «не знаю» с эскалацией. Structured outputs — вместо free-form generation. Mandatory human gates для kinetic action — UI намеренно создаёт фрикцию для критических решений.

Связь с разобранными провалами. Lavender — вырожденный HITL: 20 секунд — это HOTL под маской HITL. MCAS — отсутствие meaningful human override: пилот формально мог override, но информации, чтобы понять, что надо overriding, у него не было. Это в каждом случае — engineering failure на границе категоризации.

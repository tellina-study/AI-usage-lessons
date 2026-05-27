---
id: s05
type: keystone
duration_min: 3
assertion: "Матрица данные × физика даёт 4 квадранта. В каждом — свой профиль AI и своя стратегия применения."
learning_goal: "Keystone ось 2×2 + inline definitions «physics certainty» + «data availability»"
failure_bucket: partial
chapter_ref:
  parts: [chapter.md]
  sections: ["§0.1-§0.3 Keystone-ось матрица"]
visual:
  type: diagram
  description: "2×2 matrix центром, axes labeled inside as scale markers; 4 квадранта с примером per quadrant; inline operational definitions bottom-left"
  acquisition_tier: self_render
visible_numbers: ["+15% Ambyint", "$1,8B Aramco 2024", "190× CCS gap"]
russification_check: "Brand allowlist (Eclipse, INTERSECT, Ambyint, METABRAIN, MethaneSAT, Northern Lights, Fervo); domain inline gloss."
speaker_notes_target_words: 250
---

# Матрица данные × физика. Четыре квадранта — четыре стратегии AI.

## Visible content

Заголовок: «Когда AI работает в нефтегазе? Матрица данные × физика» (28pt deep ocean).
Sub: «От разведки фронтиров до спутникового метана — AI имеет 4 разных profile.» (16pt italic)

**Центр слайда — 2×2 matrix (50% площади):**

| | **Низкая определённость физики** | **Высокая определённость физики** |
|---|---|---|
| **Высокая доступность данных** | **Q2 — Methane MRV**<br/>AI **essential**<br/>MethaneSAT / Carbon Mapper / GHGSat | **Q1 — Mature production**<br/>AI **мультипликатор**<br/>Ambyint **+15%** на 200 wells |
| **Низкая доступность данных** | **Q4 — Energy transition**<br/>AI и физика **struggle вместе**<br/>Northern Lights / Fervo | **Q3 — Frontier exploration**<br/>**Physics-first**, AI augmentation<br/>Aramco METABRAIN / Eni HPC6 |

Цветовая разметка: Q1 = primary mid `#065A82` (зрелый), Q2 = secondary teal `#028090` (essential), Q3 = primary light `#1C7293` (frontier), Q4 = gold tint `#F0AB00` (струggle — самый честный).

**Bottom-left — inline operational definitions (gold tint):**

- **Доступность данных** = достаточно ли labeled examples для retraining + generalization. Q1: 1000+ wells = да. Q3: 1-5 wildcat wells = нет.
- **Определённость физики** = есть ли установившаяся численная модель с известной точностью. Q3 (Eclipse, INTERSECT): да. Q2 (multi-modal fusion): нет.

**Bottom bar (gold accent):**

«За каждым AI-внедрением — alternative tool: физический симулятор, OGI-камера, классическая интерпретация.»

## Speaker notes

Это keystone-слайд. Сюда мы будем возвращаться каждый раз, когда говорим про конкретный кейс. Две оси, четыре квадранта.

Первая ось — доступность данных. Это вопрос: есть ли у вас достаточно labeled examples, чтобы обучить модель и чтобы она обобщалась на новые случаи? В зрелом месторождении Пермского бассейна — тысяча скважин, петабайты данных за 30 лет, данных много. В разведке нового бассейна — одна-пять wildcat-скважин, данных структурно мало.

Вторая ось — определённость физики. Это вопрос: есть ли установившаяся численная модель, дающая эталонную разметку с известной точностью? Для пластовой симуляции — Eclipse, INTERSECT, CMG — физика описана с 1970-х, верифицирована тысячами проектов; физика определена. Для слияния спутник + аэро + дрон + ручная OGI-камера и атрибуции малой утечки к источнику — классического решения нет, физика частично известна.

Перекрестив две оси, получаем четыре квадранта. Q1 — зрелое производство, высокие данные плюс высокая физика — AI работает как мультипликатор классических методов; пример Ambyint InfinityRL даёт плюс пятнадцать процентов на двухстах скважинах. Q2 — методановая MRV, высокие данные но низкая физика — AI essential, потому что классической альтернативы нет; MethaneSAT, Carbon Mapper, GHGSat. Q3 — разведка фронтиров, данных мало но физика хорошо описана — physics-first, AI augmentation; Aramco METABRAIN, Eni HPC6. Q4 — энергетический переход, и данных мало, и физика на длинных горизонтах не закрыта — AI и физика struggle вместе; Northern Lights CCS, Fervo EGS.

И главное внизу: за каждым AI-внедрением в нефтегазе стоит alternative tool. Это структурный признак отрасли, не дисклеймер. К этому мы вернёмся в Разделе 7.

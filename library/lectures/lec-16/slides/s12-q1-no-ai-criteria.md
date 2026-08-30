---
id: s12
type: criteria_list
duration_min: 1
assertion: "Когда AI НЕ нужен в Q1 — 6 структурных критериев: зрелый пласт + Eclipse, stripper wells <10 bopd, custody transfer, BOP/SIS, frontier без аналогов, EU compliance reporting."
learning_goal: "LO2 criteria 6 visible bullets"
failure_bucket: strict_in
chapter_ref:
  parts: [chapter.md]
  sections: ["§1.8 Шесть критериев «здесь AI не нужен в Q1»"]
visual:
  type: diagram
  description: "6 numbered Ocean rounded cards с иконкой per критерий (X icon = «не нужен»); colour-coded по типу: technical / regulatory / economic"
  acquisition_tier: self_render
visible_numbers: ["<10 bopd stripper wells"]
russification_check: "«пластовый симулятор», «истощённая скважина», «передача товарной нефти», «противовыбросовый превентор», «разведка фронтиров», «соответствие нормам» — все RU; Eclipse, BOP, SIS — brand/standard list."
speaker_notes_target_words: 220
---

# 6 критериев «здесь AI не нужен» в Q1

## Visible content

Заголовок: «Когда AI НЕ нужен в Q1 — 6 структурных критериев» (28pt deep ocean).
Sub: «Distilled из практики последних 5 лет. Каждый — с конкретной альтернативой.» (16pt italic)

**6 numbered Ocean rounded cards в grid 2×3 (X-иконка слева от номера):**

1. **Зрелый пласт + опытная команда + Eclipse.** Senior engineer + классический симулятор дают надёжные ответы. ML — overhead без существенного прироста.
2. **Stripper wells <10 bopd** (gold accent). Прибавка +15% = +1,5 bopd; стоимость развёртывания > извлечённой ценности. Юнит-экономика отрицательная.
3. **Custody transfer metering** — передача товарной нефти. Регулятор требует mass flow meter класса точности 0,2%. Не black-box ML.
4. **BOP / PRV / ESD — Safety Instrumented Systems.** SIL3/SIL4 по IEC 61511 = детерминированно + сертифицируемо. ML не сертифицируется.
5. **Frontier exploration без analog data.** ML не на чем обучать (preview Раздела 2). Senior геофизик + классическая интерпретация.
6. **EU Methane Reg compliance reporting.** Traceability mandated — не black-box ML estimate.

**Bottom bar (gold tint):**

«LO2 — главный навык курса: уметь сказать «нет» там, где AI не нужен. 14% successful 86% pilot stuck — разница часто именно здесь.»

## Speaker notes

Это центральный пункт раздела по миссии когда отказаться. В Q1, то есть в высоко-data плюс высоко-physics квадранте, AI по умолчанию претендует на применение, и инженер должен уметь сказать «нет» там, где AI не нужен.

Критерий первый — зрелое месторождение плюс опытная команда плюс Eclipse. Когда у вас есть месторождение с историей тридцать с лишним лет и опытные инженеры-разработчики, использующие классические симуляторы — добавление ML-суррогата редко даёт существенный прирост.

Критерий второй — stripper wells, истощённые скважины с дебитом меньше десяти баррелей в день. Прибавка плюс пятнадцать процентов — это плюс полтора bopd; стоимость развёртывания плюс переобучения больше извлечённой ценности.

Критерий третий — custody transfer metering, передача товарной нефти. Регуляторно требуется mass flow meter класса точности ноль и две десятых процента. Methane content в газовом потоке измеряется через gas chromatograph или прямое sampling. AI estimate не приемлем.

Критерий четвёртый — приборные системы безопасности. Противовыбросовый превентор, предохранительный клапан, логика аварийного останова — SIL3/SIL4 по IEC 61511, детерминированно. ML не сертифицируется под этот стандарт.

Критерий пятый — разведка фронтиров без аналогов. ML не на чем обучать. Senior геофизик плюс классическая интерпретация. Мы развернём это в Разделе 2.

Критерий шестой — соответствие нормам EU Methane Reg. Traceability mandated — не black-box ML estimate.

Главный навык уметь сказать «нет». Разница между четырнадцатью процентами успешных и восьмьюдесятью шестью застрявших — часто именно здесь.

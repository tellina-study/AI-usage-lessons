---
id: s30
type: assertion_visual
duration_min: 1.5
assertion: "Act — когда не AI: 2 критерия. Автономия не нужна + COTS sensor дешевле."
learning_goal: "Критерии 5-6 для Act — закрытие раздела"
learning_outcomes: [LO3]
chapter_ref: "§3.6 — Когда не AI для Act"
references: []
visual:
  pattern: matrix
  primary: "2 criterion cards + закрывающий takeaway"
---

# Act — два критерия «когда не AI»

## Assertion

Act — когда не AI: 2 критерия. Автономия не нужна + COTS sensor дешевле.

## Visual

Под assertion — 2 равные крупные criterion cards в Ocean rounded box:

**Критерий 5 (autonomy не нужна)** — badge gold «#5»
- **Автономия не нужна; человек медленнее, но безопаснее**
- Иконка `user-check` 48px
- «Канонический контрпример — MCAS. Auto-correct trim был "решением" проблемы, которой могло не быть в первую очередь»
- «Если задача — auto-correct физическую проблему — СНАЧАЛА пересмотрите hardware»
- «Software для compensation hardware shortfall — это часто индикатор более глубокой проблемы»

**Критерий 6 (COTS sensor дешевле)** — badge gold «#6»
- **COTS sensor дешевле и надёжнее, чем ML на одном sensor**
- Иконка `hard-drive` 48px
- «COTS — Commercial Off-The-Shelf, готовый коммерческий компонент»
- «Не делайте ML на проблеме, которая решается hardware redundancy»
- «Второй AoA-сенсор на 737 MAX стоил бы порядки меньше всех trim-AI»
- «Вопрос инженерной приоритизации, не AI-возможностей»

Внизу — закрывающий takeaway-row 18pt italic Primary mid: «Act — звено, где hype далеко впереди реальности. Большинство strikes — operator-in-loop. Не путайте L3-supervised с L5-full-LAWS».

## Speaker notes

Из разобранных провалов извлекаем два критерия для звена Act — критерии 5 и 6.

Критерий пятый — автономия не нужна. Канонический контрпример — MCAS: автоматическая корректировка триммирования была «решением» проблемы, которой могло не быть в первую очередь. Если бы Boeing просто пересмотрел двигатели или изменил их положение, MCAS не понадобился бы. Это и есть главный инженерный вопрос: если ваша задача — auto-correct физическую проблему, сначала пересмотрите hardware. Software для compensation hardware shortfall — это часто индикатор более глубокой проблемы, и индустрия в авиации именно так и реагирует на 737 MAX лессоны.

Критерий шестой — COTS sensor дешевле. COTS — Commercial Off-The-Shelf, готовый коммерческий компонент. Если проблема решается hardware redundancy — второй AoA-сенсор, — не делайте ML на проблеме, которая решается железом. Второй AoA-сенсор стоил бы порядки меньше всех trim-AI на 737 MAX. Это вопрос инженерной приоритизации, не AI-возможностей.

Подытог Раздела 3. Act — звено, где hype далеко впереди реальности. Программы автономии растут быстро: Fury YFQ-44A в производстве с марта 2026, V-BAT в Индийской армии, X-62A VISTA в demo, Saker Scout combat-tested в Украине. Но большинство strikes остаётся operator-in-loop. Российский слой — Geran-2 evolution плюс Lancet rollback плюс supply chain через third countries; civilian dual-use Cognitive Pilot. Канонические провалы: 737 MAX MCAS — single sensor плюс opacity плюс software-patches-hardware; Patriot 2003 и 2024 — automation bias плюс IFF; Replicator missed scale — software отстаёт от железа. Два критерия «когда не AI» — про необходимость автономии и про COTS sensor redundancy.

Дальше — Раздел 4, и он отличается от первых трёх. Это мета-уровень: где звено Act обрезано регулированием.

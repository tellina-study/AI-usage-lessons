---
id: s21
type: assertion_visual
duration_min: 3.5
assertion: "IDF Lavender (Газа 2023-24): ~37 000 помечены, 90% accuracy → ~3 700 false positives. «Accuracy %» — не та метрика для life-and-death."
learning_goal: "Canonical Lavender — 3 урока (wrong metric + frictionless + degenerate HITL)"
learning_outcomes: [LO2, LO3]
chapter_ref: "§2.4 — Провал IDF Lavender"
references: [abraham-2024-972, lieber-2024, aoav-2025]
visual:
  pattern: data_chart
  primary: "Sankey/funnel 37k→3700 FP + 3 lesson cards"
---

# IDF Lavender — «accuracy 90%» обнуляется в life-and-death

## Assertion

IDF Lavender (Газа 2023-24): ~37 000 помечены, 90% accuracy → ~3 700 false positives. «Accuracy %» — не та метрика для life-and-death.

## Visual

Под assertion 28pt bold — главный visual: funnel / cascade chart в Ocean rounded box (60% слайда).

Funnel шаги вертикально:
1. **37 000** помечены как «подозреваемые» (Primary mid bar, 100% width)
2. **× 90% self-reported accuracy**
3. **~3 700 false positives** (gold-warning, 30% width, эмоциональный pivot)
4. **20 секунд** review per target (sub-callout)
5. **15-20 civilian casualties** authorized per junior operative (gold-warning, sub-callout)

Каждый шаг — отдельный bar/box, стрелки вниз RIGHT_ARROW.

Справа (40%) — 3 lesson cards stacked:

**Урок 1: «accuracy» — wrong metric**
- Правильная: FP consequence × population × frequency
- Cost-asymmetry FP↔FN неприемлемо большая

**Урок 2: AI снимает фрикцию**
- Темпы вырастают → качество deliberation падает
- В life-and-death катастрофично

**Урок 3: HITL ≠ Human-In-The-Decision**
- 20 sec review = формальный HITL, функциональный HOTL
- Engineering decision «сколько времени у оператора» — это категоризация системы

Под funnel — caption 12pt italic в Teal-tint: «Источники: Abraham, +972/Local Call (апрель 2024); 6 IDF intel officers; ICRC, Lieber Institute, AOAV — academic разборы; IDF официально опровергает».

## Speaker notes

Главный педагогический провал звена Decide в 2024-2026 годах — IDF Lavender, AI-система массовой идентификации целей в Газе 2023-2024.

Что произошло. Lavender — это AI-database, помечающая палестинских мужчин как «подозреваемых членов Хамас или PIJ» — Palestinian Islamic Jihad — по паттернам коммуникации, перемещения и связей. По свидетельствам шести офицеров израильской разведки, Lavender пометил около 37 000 человек. По собственному признанию ЦАХАЛ, точность около 90% — то есть 1 из 10, около 3 700 человек, false positive. Процесс верификации: «officers devoted almost no resources to double-checking targets, nor bystander locations», среднее время review одной цели — около 20 секунд. Авторизованный «сопутствующий ущерб» — до 15-20 гражданских жертв на одного оперативника низшего звена.

Реакция. Генсек ООН Гутерреш выразил «глубокую обеспокоенность». ЦАХАЛ официально опроверг публикацию: «claims are baseless». Параллельно появилось несколько академических разборов: Lieber Institute, AOAV — оба авторитетные juridical institutions — обозначили это как прецедент автоматизированных kill-lists и пример «лимита международного гуманитарного права при автоматизации».

Уроки три, и каждый — самостоятельный инженерный урок.

Урок первый. «Accuracy %» — не та метрика для life-and-death. Если модель ошибается в 10 процентах случаев и применяется к 37 тысячам человек, ошибка масштабируется в тысячи людей. Правильная метрика — false positive consequence умноженное на population умноженное на frequency. В медицине, в Лекции 7, мы видели похожий паттерн с раком: false negative значительно дороже false positive, поэтому система настраивается на высокую sensitivity. В Lavender — наоборот: false positive — это жизнь невинного человека, и она дороже, чем «упустить оперативника». Но система проектировалась под симметрию. Эту ошибку проектирования метрики я хочу, чтобы вы унесли как главный engineering takeaway.

Урок второй. AI снимает фрикцию, и это иногда плохо. Когда команда принимала решения «вручную», требовалось время, аналитический ресурс, командирская подпись. Это естественные тормоза. AI снижает стоимость принятия решения, темпы вырастают, качество deliberation падает. Снимая фрикцию, AI масштабирует не качество решения, а его скорость. В коммерческом контексте это OK — frictionless commerce. В life-and-death контексте — катастрофично.

Урок третий. Human-in-the-loop не равно human-in-the-decision. Lavender формально удовлетворял требованию «человек в петле»: каждое решение об ударе авторизовалось офицером. Но 20 секунд проверки — это не review, это формальное подтверждение. Если HITL вырождается в подпись без осмысления, это HOTL под маской HITL. Engineering decision «сколько времени у оператора на review» — это формальная категоризация системы. Мы вернёмся к этому в Разделе 4.6.

Альтернатива не «давайте сделаем Lavender точнее». Альтернатива — изменение архитектуры: AI ассистирует triage, ранжирование, сужение списка; human keeps authority — финальная авторизация за человеком с реальным временем на review. Calibrated uncertainty плюс явные abstention pathways. AI — accelerator, не decision-maker.

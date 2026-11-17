---
id: s25
type: anti_hype_grid
duration_min: 2.2
assertion: "Cainthus (Cargill 2018) — публичных production-метрик нет (анонс ≠ внедрение). Tie-stall barns ломают CV; алгоритм работает на free-stall + Holstein, не на местных породах РФ. AI capability ≠ AI applicability."
learning_goal: "AP3 в L3 — applicability gap + architecture asymmetry для local breeds"
learning_outcomes: [LO5]
chapter_ref: "§3.4 Часть 2 — Strict-in F8 Cainthus + tie-stall + Holstein-bias"
references: [chapter-v3-3-4-misattribution]
visual:
  pattern: 3row_anti_hype
  primary: "3-row schema (Cainthus — анонс ≠ внедрение / Tie-stall — физика ломает CV / Holstein-bias — архитектурная асимметрия) + tie-stall vs free-stall diagram"
---

# Cainthus, tie-stall barns, Holstein-bias — 3 anti-hype урока

## Assertion

Cainthus (Cargill 2018) — публичных production-метрик нет (анонс ≠ внедрение). Tie-stall barns ломают CV; алгоритм работает на free-stall + Holstein, не на местных породах РФ. AI capability ≠ AI applicability.

## Visual

Под assertion 28pt bold — 3-row schema, каждая строка — отдельный anti-hype урок в Ocean rounded box. Гибридный layout с photo / diagram где уместно.

**Row 1 — Cainthus: анонс ≠ внедрение.**
- Icon `megaphone` 32px Primary mid + label
- Cainthus (Дублин, IE) — приобретена **Cargill в 2018**; camera-based CV для feeding/drinking/lying/social behaviour коров
- **Публично опубликованных production-метрик нет**
- Misattribution warning: **Cainthus ≠ Connecterra IDA** (две независимые компании, разные архитектуры — neck-collar vs camera-based)
- Урок: пресс-релиз о партнёрстве ≠ промышленное внедрение

**Row 2 — Tie-stall: физика ломает CV.**
- Слева — mini-diagram tie-stall vs free-stall barn (Ocean palette schematic)
- Tie-stall barns (Восточная Европа, РФ, Канада, Висконсин) — корова привязана к стойлу
- CV-решения L3 (CattleEye, SenseHub) **плохо работают**: слабое освещение, силуэты перекрыты, нет «корова идёт по коридору»
- Урок: **AI capability ≠ AI applicability** — та же модель работает на free-stall в Висконсине, не работает на tie-stall в Калужской области

**Row 3 — Holstein-bias: архитектурная асимметрия.**
- Слева — mini-comparison Holstein (чёрно-белая) vs Ярославская / Якутская / Бестужевская (рыжие, разной формы)
- CV-модели L3 обучены на доминирующих породах (преимущественно Holstein)
- Для местных пород РФ — калибровка слабая (непривычная окраска, форма, походка)
- **Решение:** transfer learning + 5-10k локально размеченных изображений **до** внедрения, не после первого иска

Bottom callout 14pt italic в Teal-tint box: «**AP3 в L3 — пороговая точность ≠ готовность к внедрению.** Две формы: Plantix-форма (общая точность не говорит о краевых случаях) + applicability gap (физическая конфигурация / порода / сорт, для которых модель не обучена)».

Footer 12pt italic: «Источники: Chapter v3.1 §3.4; Cargill 2018 acquisition; Connecterra independent disambig».

## Speaker notes

L3 в целом стабильнее, но три anti-hype урока нужно проговорить явно — они задают границы применимости.

Первый урок — Cainthus: компания из Дублина, приобретённая Cargill в 2018 году, сейчас часть livestock vision portfolio Cargill. Camera-based CV для мониторинга feeding, drinking, lying, social behaviour коров — но публично опубликованных производственных метрик нет. Это не провал в смысле банкротства, но сигнал: анонс партнёрства не равен промышленному внедрению. При оценке вендора смотреть не на пресс-релизы, а на верифицируемые метрики — число ферм с внедрением, выручка сегмента, отзывы клиентов.

Важная оговорка: не путать Cainthus с Connecterra IDA — нидерландской компанией с продуктом Intelligent Dairy Assistant, neck-collar sensor плюс AI behaviour analysis; клиенты — Danone, Bayer, Kersia и несколько тысяч молочных хозяйств. Это независимая от Cainthus компания с другой архитектурой и клиентской базой — их часто путают в обзорах, и это misattribution инженер должен отлавливать на стадии due diligence.

Второй урок — tie-stall barns: содержание, при котором корова привязана к стойлу и доится на месте, а не ходит в milking parlour; распространено в Восточной Европе, России, части Северной Америки. CV-решения L3 — CattleEye, SenseHub — плохо работают здесь: освещение слабое, силуэты перекрыты конструкциями стойла, нет момента «корова идёт по коридору». AI capability не равна AI applicability: та же модель CattleEye, рабочая на free-stall ферме в Висконсине, не работает на tie-stall ферме в Калужской области — не из-за «российского контекста», а из-за физической конфигурации barn.

Третий урок — Holstein-bias: CV-модели L3 обучены преимущественно на доминирующей в США и Европе чёрно-белой породе Holstein. Для местных пород РФ — Холмогорская, Ярославская, Якутская, Бестужевская — калибровка слабая: непривычная окраска, форма тела, походка. Это архитектурная асимметрия датасетов, решается transfer learning с пятью-десятью тысячами локально размеченных изображений — и делать это нужно до внедрения, а не после первого иска.

Четвёртый практический момент — экономика для small dairies. SenseHub subscription — около тридцати долларов на корову в год; для хозяйства менее пятидесяти голов это полторы тысячи долларов — высокая фиксированная стоимость против альтернативы (визуальный осмотр ветеринаром), ROI отрицательный. Для хозяйств от пятисот голов экономика другая: пятнадцать тысяч в год на мониторинг тысяч коров — малая доля общих затрат.

Главный анти-ИИ критерий — AP-три: пороговая точность не равна готовности к внедрению, и здесь это проявляется в двух формах. Plantix-форма — общая точность на бенчмарке не говорит о качестве на краевых случаях. Applicability gap — хорошая модель не работает в физической конфигурации, для которой не обучена.

## Источники

- Chapter v3.1 §3.4 Часть 2.
- Cargill 2018 — Cainthus acquisition.
- Connecterra B.V. independent company info.

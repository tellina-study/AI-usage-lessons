---
id: s11
type: comparison
duration_min: 3
assertion: "Imaging — AI+врач > каждый alone (MASAI RCT). Reasoning — augmentation gap: врач+AI ≈ врач alone (Goh JAMA). Вопрос «AI или врач» поставлен неправильно."
learning_goal: "Сравнить 3 RCT/meta-analysis: imaging vs reasoning"
learning_outcomes: [LO2, LO3]
frame_mapping: ["Человек vs AI", "Другой AI", "LLM anti-pattern (augmentation gap)"]
chapter_ref: "§2.3 — AI vs радиолог: imaging vs reasoning"
references: [liu-2019-lancet, masai-2024-lancet, hofvind-2025-lancet, goh-2024-jama]
visual:
  pattern: matrix
  primary: "3-row comparison: study / domain / result. Gold marker на MASAI 80.5% vs 73.8% (winner); identical row structure"
  illustration:
    type: paper
    sources:
      - "Liu et al. 2019 Lancet Digital Health meta-analysis — https://doi.org/10.1016/S2589-7500(19)30123-2"
      - "MASAI Lancet Digital Health 2024 — https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00267-X/fulltext"
      - "MASAI Lancet 2025 interval cancer — https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(25)02464-X/abstract"
      - "Goh et al. JAMA Network Open 2024 — https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395"
    caption: "Liu 2019; MASAI 2024-2025; Goh 2024"
interaction: none
---

# Imaging — AI+врач > врач. Reasoning — augmentation gap.

## Assertion

Imaging — AI+врач > каждый alone (MASAI RCT). Reasoning — augmentation gap: врач+AI ≈ врач alone (Goh JAMA). Вопрос «AI или врач» поставлен неправильно.

## Visual

Три горизонтальных полосы (3-row comparison) на всю ширину слайда. Каждая полоса — Ocean rounded box, с identical structure: левая колонка «Study» (название + год + journal), центральная «Domain» (imaging / reasoning), правая «Result» (ключевые числа + visualization). Row 1 — Liu et al. 2019 (Lancet DH meta-analysis): imaging meta-analysis, pooled sens AI 0.87 vs radiologist 0.85. Row 2 — MASAI 2024–2025 (Lancet DH + Lancet): mammography RCT n>100 000, sens AI 80.5% vs standard 73.8% при spec 98.5%; cancer detection 6.4 vs 5.0 per 1000; 44% workload ↓; 12% interval cancer ↓. **Gold marker** на этой строке (winner). Row 3 — Goh 2024 (JAMA Net Open): clinical reasoning, GPT-4 alone 76.3% vs doctor+GPT-4 73.7% (p=0.60, n.s.) — augmentation gap.

## Speaker notes

Один из самых частых вопросов в популярной прессе — «AI уже превзошёл врачей?» Корректный ответ — «зависит от задачи, и нюансов больше, чем популярная пресса передаёт». Три эталонных исследования дают согласованную картину с разными ответами для разных задач.

Liu и соавторы (2019, Lancet Digital Health) — первый крупный мета-анализ AI-диагностических исследований, четырнадцать проспективных работ. Pooled sensitivity AI — восемьдесят семь процентов, у клиницистов — восемьдесят пять. Разница есть, но скромная; исторический контекст «AI на уровне врача» для некоторых задач уже к 2019 году.

MASAI Sweden RCT 2024–2025 — самое сильное peer-reviewed свидетельство клинической пользы AI-маммографии на сегодня. Дизайн — рандомизированное контролируемое исследование, более ста тысяч шведских женщин случайно распределялись на стандартное «двойное чтение» (два радиолога) или на AI-поддерживаемое чтение (один радиолог + AI). Чувствительность AI-поддерживаемого скрининга — восемьдесят целых пять десятых процента против семидесяти трёх и восьми у стандартного при одинаковой специфичности. Cancer detection rate — шесть и четыре против пяти на тысячу. Снижение нагрузки радиолога на сорок четыре процента. В follow-up 2025 года — снижение interval cancer rate на двенадцать процентов: дополнительные раки, найденные AI, — клинически значимые, не overdiagnosis.

Goh и соавторы (JAMA Network Open, октябрь 2024) — про диагностическое мышление, не imaging. Пятьдесят врачей с GPT-4 или без. Медиана score — семьдесят шесть процентов с GPT-4 против семидесяти четырёх без; разница незначима. Сюрприз: GPT-4 alone давал более высокий score, чем доктор-плюс-GPT-4. Этот феномен называется augmentation gap: пользователи недозагружают возможности AI, держат его на роли «второго мнения», которое можно проигнорировать. Вывод для инженера: вопрос «AI или врач» — неправильный; правильные — «какая задача?», «какой workflow?», «как AI и врач интегрированы?».

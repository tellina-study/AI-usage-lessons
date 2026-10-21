---
id: s15
type: process
duration_min: 2.5
assertion: "Drug discovery: 10-15 лет, $1-2 млрд, ~6.7% success. AI ускоряет stages 1-3 (discovery + preclinical); stages 4-5 (clinical) — биология."
learning_goal: "5-stage pipeline drug discovery + где AI помогает"
learning_outcomes: [LO1, LO2]
frame_mapping: ["Другой AI"]
chapter_ref: "§3.1 — Pipeline drug discovery и где AI помогает"
references: [dimasi-2016-jhe, wouters-2020-jama, mullard-2024-nrdd]
visual:
  pattern: pipeline
  primary: "5-stage pipeline (Target → Hit → Lead → Preclinical → Clinical I/II/III) с RIGHT_ARROW; AI-icons над stages 1-3, human-icon над 4-5"
  illustration:
    type: schematic
    sources:
      - "Self-generated 5-stage pipeline через PowerPoint shapes + RIGHT_ARROW (Ocean palette)"
      - "DiMasi et al. 2016 Journal of Health Economics (cost: $1-2B per approved drug)"
      - "Wouters et al. 2020 JAMA (updated cost estimate)"
      - "Mullard 2024 Nature Reviews Drug Discovery (~6.7% Phase 1→approval success rate)"
    caption: "Drug discovery pipeline; AI ускоряет stages 1–3"
interaction: none
---

# AI ускоряет discovery, не clinical trials

## Assertion

Drug discovery: 10–15 лет, $1–2 млрд, ~6.7% success. AI ускоряет stages 1–3 (discovery + preclinical); stages 4–5 (clinical) — биология.

## Visual

Горизонтальный 5-stage pipeline на всю ширину слайда. Каждая стадия — Ocean rounded box, соединены MSO_SHAPE.RIGHT_ARROW. Стадия 1 «Target identification» (Primary light, иконка `target`): AlphaFold, AlphaProteo. Стадия 2 «Hit discovery» (Primary mid, иконка `flask-conical`): Insilico, Exscientia, Generate Biomedicines. Стадия 3 «Lead optimization» (Primary mid, иконка `sparkles`): simulation + ML. Стадия 4 «Preclinical» (deep `#21295C`, иконка `microscope`): predicting toxicity. Стадия 5 «Clinical I/II/III» (deep `#21295C`, иконка `users`): patient stratification. Над stages 1–3 — gold banner «AI accelerates significantly»; над 4–5 — серый «AI helps marginally». Снизу gold-info: «~90% clinical attrition unchanged by AI». Caption: «DiMasi 2016, Wouters 2020 JAMA, Mullard 2024 NRDD».

## Speaker notes

Перед тем как обсуждать конкретные истории успехов и неудач AI в drug discovery, нужно понимать pipeline индустрии. Традиционная разработка нового лекарства — это путь длиной десять-пятнадцать лет и стоимостью один–два миллиарда долларов на каждый одобренный препарат. Большинство кандидатов отсеивается по пути: примерный шанс перейти от Phase 1 до одобренного препарата составляет около шести и семи десятых процента.

Pipeline разделяется на пять условных стадий. Первая — target identification. Какой биологический белок-мишень атаковать для лечения болезни? Здесь AI применяется для прогнозирования структуры белка (AlphaFold) и для дизайна белков-связывающих молекул (AlphaProteo). Вторая — hit discovery. Поиск молекулы-кандидата с initial activity signal. «Hit» — это молекула с начальным сигналом активности против цели. Здесь работают generative chemistry-модели: Insilico Chemistry42, Exscientia, Generate Biomedicines. Третья — lead optimization. «Lead» — это hit, доведённый до preclinical-readiness: улучшенная аффинность, селективность, стабильность. Между hit и lead — годы лабораторной работы; здесь AI ассистирует через симуляцию плюс ML. Четвёртая — preclinical: эксперименты на клетках и животных, ADMET-моделирование. Пятая — clinical Phase I, II, III: эксперименты на людях. Phase 1 — safety на малой когорте; Phase 2 — efficacy и dose-finding на средней; Phase 3 — confirmatory на большой.

И главный вывод: AI ускоряет стадии один–три значительно — с четырёх-пяти лет до двенадцати-восемнадцати месяцев в лучших случаях. Стадии четыре–пять остаются доменом биологии, а не алгоритма. Привычная фраза «AI ускорит drug в десять раз» смешивает две разные claim: AI ускоряет design — verified; AI ускоряет approval — не verified, потому что восемьдесят процентов drug timeline — это clinical trials.

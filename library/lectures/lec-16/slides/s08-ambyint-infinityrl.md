---
id: s08
type: case_with_chart
duration_min: 2
assertion: "Ambyint InfinityRL: +15% production на 200 скважинах Permian. RL поверх классического штангового насоса — augmentation, не замена."
learning_goal: "Working case: узкая ML-задача с verifiable baseline"
chapter_ref:
  parts: [chapter.md]
  sections: ["§1.4 Ambyint InfinityRL: +15% на 200 скважинах"]
visual:
  type: chart
  description: "Bar chart: 100-500 bopd baseline → +15% delta = +15-75 bopd per well; на 200 wells = +3000-15000 bopd total"
  acquisition_tier: self_render
visible_numbers: ["+15% production delta", "200 wells Permian/Eagle Ford/Bakken", "100-500 bopd baseline"]
russification_check: "Ambyint, InfinityRL — brand list; «обучение с подкреплением (RL)», «искусственный подъём», «штанговый насос», «электроцентробежный насос (ЭЦН)» inline gloss."
speaker_notes_target_words: 230
---

# Ambyint InfinityRL: +15% production. RL поверх классики — мультипликатор, не замена.

## Visible content

Заголовок: «Ambyint InfinityRL: +15% на 200 скважинах» (28pt deep ocean).
Sub: «Канадский стартап (Калгари, 2014); $25M Series B 2022. Reinforcement learning для оптимизации искусственного подъёма.» (16pt italic)

**Слева — Ocean rounded box «Cases»:**

- **Регионы:** Permian Basin + Eagle Ford + Bakken (US shale).
- **Тип скважин:** mature production, классические штанговые насосы + ESP (электроцентробежные насосы).
- **Baseline per-well:** 100–500 bopd (Permian variance очень широкая).
- **Delta:** **+15% над per-well historical mean** (gold accent).
- **На 200 скважинах:** +3 000–15 000 bopd дополнительной добычи total.

**Справа — Ocean rounded box «Почему это сильный кейс»:**

1. **Verifiable baseline** — «средняя по 200 скважинам с явным per-well historical mean», не «AI спас $10M» без знаменателя.
2. **RL поверх штангового насоса** — augmentation, не замена. AI — мультипликатор.
3. **Узкая область применения** — оптимизация искусственного подъёма, не «AI для всей разведки».

**Bottom bar:**

«Когда Ambyint **не работает**: stripper wells <10 bopd. +15% = +1,5 bopd; стоимость развёртывания > извлечённой ценности. Это критерий №5 из §1.8.»

## Speaker notes

Ambyint — канадский стартап, основан в Калгари в 2014 году. Серия B на двадцать пять миллионов долларов в 2022 году от Bessemer Venture Partners и Schlumberger Energy Ventures. Сфокусирован на оптимизации искусственного подъёма — это методы подъёма нефти из скважины с низким пластовым давлением: штанговый насос, электроцентробежный насос, газлифт. Продукт InfinityRL — система оптимизации на основе обучения с подкреплением.

Кейс. Развёрнут на около двухстах скважинах в Пермском бассейне, Eagle Ford и Bakken — все US shale. Средняя прибавка к производительности — плюс пятнадцать процентов над per-well historical mean. Это означает: для типичной скважины Пермского бассейна с дебитом сто-пятьсот баррелей нефти в день — прибавка пятнадцать-семьдесят пять bopd на скважину. На двухстах скважинах — три-пятнадцать тысяч bopd дополнительной добычи.

Почему это сильный кейс. Во-первых, цифра верифицируемая: Ambyint публикует её как «средняя по двумстам скважинам» с явным исходным уровнем — per-well historical mean. Это не «AI спас десять миллионов долларов» без знаменателя. Во-вторых, метод — обучение с подкреплением поверх классического штангового насоса, а не «AI заменяет штанговый насос». AI — мультипликатор, не замена. В-третьих, область применения узкая.

Когда Ambyint не работает — это stripper wells, скважины с дебитом меньше десяти баррелей в день. Истощённая скважина даёт десять bopd; плюс пятнадцать процентов — это полтора bopd; стоимость развёртывания плюс переобучения больше извлечённой ценности. Здесь окупаемость отрицательная. Это структурный критерий, к которому мы вернёмся через четыре слайда.

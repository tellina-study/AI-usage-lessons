---
id: s20
type: assertion_visual
duration_min: 1
assertion: "В медицинском AI ставки максимальны: ошибка модели = ошибка диагноза или назначения = вред пациенту. Что инженер должен знать про границы."
learning_goal: "Transition к ethics section — 3 темы next slides"
learning_outcomes: [LO3, LO8]
frame_mapping: ["Безопасность", "Человек vs AI"]
chapter_ref: "§4.1 — Зачем инженеру думать про границы medical AI"
references: []
visual:
  pattern: cover_distinct
  primary: "Stock photo medical team + 3-point preview списком (bias / LLM anti-pattern / data security + responsibility)"
  illustration:
    type: stock
    sources:
      - "Unsplash https://unsplash.com/s/photos/medical-team (CC0)"
      - "Pexels https://www.pexels.com/search/hospital%20technology/ (free)"
      - "Wikimedia Commons CC-BY — medical team / healthcare professionals"
    caption: "Медицинский AI — высокие ставки, не sandbox"
interaction: none
---

# В медицинском AI ставки максимальны

## Assertion

В медицинском AI ставки максимальны: ошибка модели = ошибка диагноза или назначения = вред пациенту. Что инженер должен знать про границы.

## Visual

Левая половина слайда — stock photo medical team (Unsplash CC0) в Ocean rounded box. Правая половина — вертикальный список из 3 пунктов в Ocean rounded box: 1. «Bias в medical AI: Obermeyer 2019 deep-dive» — иконка `scale` 32px. 2. «LLM anti-pattern в медицине: NEDA Tessa + 3 cases» — иконка `message-circle-warning`. 3. «Безопасность данных + responsibility framework» — иконка `shield-check`. Над списком — ассертион 24pt; внизу gold-strip: «Цель — научиться думать о границах сразу, на стадии design».

## Speaker notes

В медицинском AI ставки максимальны: ошибка модели — это ошибка диагноза или назначения, и она оборачивается реальным вредом пациенту. В отличие от других индустрий, где ошибку можно частично исправить или компенсировать, в медицине последствия часто необратимы: пропущенный рак, лишняя биопсия, осложнения от ненужной терапии.

В оставшейся части лекции мы разберём четыре темы, которые формируют профессиональный минимум для инженера, работающего в medical AI. Первая — bias в medical AI на примере Obermeyer 2019. Это золотой стандарт case study; одна из самых цитируемых работ в области, и она показывает, как выбор прокси-переменной в metric-driven модели становится выбором политики. Вторая — LLM анти-паттерны: NEDA Tessa, adversarial hallucination, массовое self-diagnosis. Здесь главное различие — LLM в медицинском контексте не то же самое, что medical AI; они требуют разных design countermeasures. Третья — безопасность медицинских данных: Change Healthcare breach и российское регулирование (ФЗ-152, ФЗ-23). И четвёртая — архитектура ответственности: кто отвечает, когда AI ошибается.

Тон последнего раздела — серьёзный, без алармизма. Цель — научить инженера думать о границах сразу, на стадии design, а не post-hoc после первого инцидента. Этика и ответственность — сквозная тема всех лекций курса, не отдельный раздел; три принципа отсюда станут входом в копилку персонального чек-листа. Финал синтеза — на финальной Лекции 17 «Систематизация знаний и навыков», где чек-лист собирается из всех отраслевых кейсов курса. Сегодня мы накапливаем материал для синтеза.

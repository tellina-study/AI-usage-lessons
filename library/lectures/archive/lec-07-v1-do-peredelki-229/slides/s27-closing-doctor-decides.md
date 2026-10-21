---
id: s27
type: assertion_visual
duration_min: 1.5
assertion: "Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать."
learning_goal: "Closing emotional payoff — callback к central question"
learning_outcomes: [LO8]
frame_mapping: ["Человек vs AI"]
chapter_ref: "§5.1 — закрывающая фраза"
references: []
visual:
  pattern: cover_distinct
  primary: "Stock photo doctor + patient (close-up emotional anchor) + большая closing-фраза в Ocean rounded box справа"
  illustration:
    type: stock
    sources:
      - "Unsplash https://unsplash.com/s/photos/doctor-patient (CC0, doctor explaining)"
      - "Pexels https://www.pexels.com/search/medical%20consultation/ (free)"
      - "Wikimedia Commons CC-BY — doctor patient consultation"
    caption: "Врач + пациент: human stays central (Unsplash CC0)"
interaction: none
---

# Врач решает. AI подсказывает. Инженер обеспечивает.

## Assertion

Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать.

## Visual

Слева — крупное stock photo «врач + пациент» (Unsplash CC0, close-up emotional anchor) в Ocean rounded box, занимает ~45% ширины. Справа — большой Ocean rounded box (~50% ширины), внутри центральная закрывающая фраза 32pt bold deep в три строки: «Врач ставит диагноз. / AI подсказывает. / Инженер делает так, чтобы врач мог по-настоящему решать». **Gold highlight** на слове «по-настоящему». Под фразой мелким (12pt italic): «Callback to central question — payoff lecture».

## Speaker notes

Возвращаемся к центральному вопросу лекции. Какие AI-обещания в медицине сбылись? AI-диагностика — да, и есть конкретные числа: mosmed.ai с четырнадцатью миллионами исследований, MASAI Sweden RCT со снижением нагрузки радиолога на сорок четыре процента. Drug discovery — частично: Rentosertib peer-reviewed в Nature Medicine; DSP-1181 discontinued. И главная часть вопроса — кто отвечает, когда AI ошибается. Ответственность всегда на враче. Это не уступка консерватизму и не недоверие к AI. Это структурное распределение: только врач имеет full context.

И отсюда — закрывающая фраза, на которой держится профессиональный смысл этой лекции для инженера. Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать. По-настоящему — это значит с пониманием того, что модель сделала и почему (transparency, Grad-CAM heatmap, confidence score); с уверенностью, что эта модель валидирована именно для той популяции, на которой её сейчас применяют; с возможностью восстановить, кто, когда, с какой версией модели получил такой output — это audit-trail. Эти три инженерных принципа и есть то, что вы построили сегодня в копилку персонального чек-листа. Финал — личный чек-лист на финальной Лекции 17 «Систематизация знаний и навыков», который собирается из всех отраслевых кейсов курса.

Если вы запомните одно предложение из этой лекции через две недели — пусть это будет именно оно. Врач решает. AI подсказывает. Инженер обеспечивает то, что делает первое предложение технически выполнимым.

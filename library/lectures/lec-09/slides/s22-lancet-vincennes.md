---
id: s22
type: assertion_visual
duration_min: 3
assertion: "Lancet ATR rollback — демо ≠ продакшен. USS Vincennes 1988 (290 KIA) — UI под стрессом, и почему этот урок про LLM."
learning_goal: "Lancet (LO2 canonical) + Vincennes (urok про UI и confident BS)"
learning_outcomes: [LO2, LO3]
chapter_ref: "§2.5, §2.6 — Lancet + Vincennes"
references: [csis-2025-lancet, usni-2018-vincennes, foreign-affairs-2024]
visual:
  pattern: matrix
  primary: "2 case cards: Lancet timeline + Vincennes UI"
---

# Lancet rollback + Vincennes 1988 — два урока про разрыв

## Assertion

Lancet ATR rollback — демо ≠ продакшен. USS Vincennes 1988 (290 KIA) — UI под стрессом, и почему этот урок про LLM.

## Visual

Под assertion — 2 равные case cards в Ocean rounded box.

**Слева — Russian Lancet ATR rollback** (2022-2024):
- Mini-timeline:
  - **2022-23** — маркетинг «autonomously find and hit target» · видео с «Target Locked» UI
  - **2024** — CSIS / MWI анализ: AI-guidance off · последние videos без autonomous-locking UI
- Иконка `triangle-alert` 48px Primary mid
- 14pt text: «Edge cases — это БОЛЬШАЯ ЧАСТЬ настоящего поля боя. Пыль, дым, EW, повреждённое оборудование, новые маскировки»
- Бейдж: **LO2 canonical case** (gold)
- Альтернатива: «Operator-in-the-loop + automated tracking-assist. Не autonomous engage до production hardening»

**Справа — USS Vincennes / Iran Air 655** (3 июля 1988):
- Mini-timeline:
  - **Aegis записал** track как climbing ✓
  - **Экипаж под стрессом доложил** «descending into attack» ✗
  - **2 ракеты SM-2** · 290 KIA (gold-warning)
- Иконка `eye-off` 48px Primary mid
- 14pt text: «Не баг алгоритма — automation корректно выполнил работу. Сбой — на интерфейсе человек-машина под combat stress»
- Bridge to LLM 14pt italic в Teal-tint: «LLM выдаёт fluent confident output → оператор склонен принять. Confident BS = high-risk confident BS в high-stakes»

Source 12pt italic: «CSIS 2025 Lancet rollback; USNI Proceedings July 2018 Vincennes; Foreign Affairs 2024».

## Speaker notes

Второй провал звена Decide — Russian Lancet ATR rollback, 2022-2024 годы — канонический кейс для учебной цели LO2: отличить демо от продакшена.

Что произошло. Lancet-3 — российский loitering munition производства «Калашников / ZALA Aero Group». Маркетинг 2022-2023 годов прямо обещал: «autonomously find and hit target». Видео содержали интерфейс «Target Locked» с bounding box на цели. Анализ Field 2023-2024 годов от CSIS, Modern War Institute показал: российская сторона выключила AI-guidance после первоначальных развёртываний. Последние video drops не имеют autonomous-locking UI. Беседы с украинскими технологическими специалистами подтверждают: terminal phase autonomy сомнительна.

Гипотеза. Premature product rollout с последующим product «recall». ATR работал в demo-conditions — узкое распределение, известные цели, отсутствие EW, — но не работал в реальных условиях: пыль, дым, EW-подавление, повреждённое оборудование, новые маскировки. Edge cases — это большая часть настоящего поля боя. Это урок не Lancet-specific и не Russian-specific. ML performance в narrow training distribution не переносится на full battlefield variance. Применимо ко всем ATR-системам, ко всем drone autonomy claims, ко всем «autonomous targeting» рекламам.

Студент-инженер должен уметь задать вопрос: в каких условиях демонстрировалась эта capability? Что меняется на продакшене? Какие edge cases исключены из demo? Без ответов на эти вопросы любое «autonomous» claim — это маркетинг, не инженерия.

Третий провал — USS Vincennes, 1988 год. И это не AI в строгом смысле, но урок прямо применим к современным LLM-системам.

Что произошло. 3 июля 1988 года крейсер USS Vincennes сбил иранский гражданский самолёт Iran Air Flight 655, Airbus A300, рейс Тегеран — Дубай, двумя ракетами SM-2. Погибли 290 человек. Aegis-система корректно записала track как climbing — характеристика гражданского самолёта, не атаки. Операторы под стрессом, в условиях напряжённого ожидания иранской атаки, доложили капитану «descending into attack». Manual correlation сбоит под стрессом плюс target fixation.

Корневая причина — не баг алгоритма. Automation выполнил свою работу. Сбой произошёл на интерфейсе человек-машина под combat stress. Экипаж интерпретировал данные против того, что показывала система.

Урок. Это не про автоматизацию, это про то, как тестировать UI. Если система предполагает «people will catch the error», нужно проектировать процесс под predicted human failure modes, а не под expectation of rationality. UI должен навязывать правильную интерпретацию, а не оставлять её на интуицию оператора в стрессе.

Почему это про LLM. В современных LLM-decision-support системах есть структурно похожая проблема: LLM выдаёт fluent, confident output — текст хорошо написан и звучит уверенно, — и оператор под временным давлением склонен принять этот output как правильный, не верифицируя источники. Confident BS равно high-risk confident BS в high-stakes. USS Vincennes — урок 1988 года, прямо применимый к 2026.

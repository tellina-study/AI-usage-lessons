---
id: s19
type: assertion_visual
duration_min: 10
assertion: "Используем AI для понимания AI. Но не доверяем без проверки."
learning_goal: "Apply LO4: студент использует web-chat + критически оценивает"
learning_outcomes: [LO4, LO2, LO3]
frame_mapping: ["LLM pattern", "LLM anti-pattern"]
chapter_ref: "§4.1 + §4.2 — Микро-упражнение"
references: []
visual:
  pattern: matrix
  primary: "Task card layout с 3 шагами (Step 1 3 мин / Step 2 3 мин / Step 3 4 мин) + готовый промпт visible + control screenshot baseline AI response справа"
  illustration:
    type: schematic
    sources:
      - "Self-generated 3-step task card layout через PowerPoint shapes (Ocean palette + chip-pills)"
      - "Control screenshot — Claude.ai or ChatGPT response, prepared by lecturer night before, saved в assets/control/s19-baseline-llm-response.png"
      - "Fallback PDF 3-5 sample responses (3 EN + 2 RU) — assets/control/s19-fallback-responses.pdf"
    caption: "Задача: попроси AI объяснить, потом проверь"
interaction: micro_exercise
---

# Используем AI для понимания AI — но проверяем

## Assertion

Используем AI для понимания AI. Но не доверяем без проверки.

## Visual

В центре слайда — большая task card в Ocean rounded box, разделённая на 3 numbered блока. Блок 1 (Primary light, gold-badge «3 мин»): «Открой web-chat (ChatGPT / Claude / YandexGPT / GigaChat). Промпт ниже». Под блоком — готовый промпт в monospace в Surface light подсветке: «Объясни мне, что такое sensitivity и specificity для AI-диагностики на конкретном примере (например, mammography screening). Объясни как для студента 2 курса техн. вуза, со знанием базовой probability.» Блок 2 (Primary mid, gold-badge «3 мин»): «Отметь карандашом 1 неточность ИЛИ 1 unverifiable claim ИЛИ 1 слишком абстрактное место». Блок 3 (deep, gold-badge «4 мин reveal»): «Лектор спросит — 2–3 студента читают (1 мин each). Лектор показывает control-ответ». Справа — control screenshot baseline AI response (Claude/ChatGPT) в маленькой Ocean rounded box.

## Speaker notes

Это микро-упражнение — единственное активное взаимодействие студента с AI за всю лекцию, и оно соответствует требованию курса о десяти минутах AI web-chat на занятии. Учебная цель — LO4: применить AI web-chat для разъяснения статистических понятий и критически оценить полученный ответ.

Шаг первый, три минуты. Откройте AI web-chat. На лекции у вас должны работать ChatGPT, Claude, YandexGPT или GigaChat — последние два удобны для русскоязычной работы. Введите готовый промпт; можно адаптировать по вкусу: «Объясни мне, что такое sensitivity и specificity для AI-диагностики на конкретном примере, например маммографический скрининг. Объясни как для студента второго курса технического вуза, со знанием базовой теории вероятностей». Этот формат — «объясни как студенту X курса» — один из самых стабильно работающих паттернов общения с LLM.

Шаг второй, три минуты. Прочитайте ответ. Отметьте — на бумаге, в notes-app, в комментарии в чате — одно из следующего: одну фактическую неточность; одно неподтверждённое утверждение, которое нельзя проверить; одно место, где объяснение слишком абстрактное и не помогает понять.

Шаг третий, четыре минуты. На лекции — два-три студента читают свои находки, лектор показывает свой control-ответ, заранее прогнанный накануне с того же промпта. Дискуссия: что AI сделал хорошо, что — поверхностно или подозрительно.

Если вы проходите этот материал в self-study режиме — выполните шаги один–два самостоятельно за пять минут. Главное: paragraph-level critique. «AI отлично объяснил для студента второго курса» — это LLM-паттерн сработал. «AI дал число sensitivity 0.95 без citation» — это анти-паттерн, не верьте автоматически. Эта дисциплина критической оценки — то, что мы будем тренировать весь курс; четвёртое микро-упражнение здесь, Практикум 1 будет на лекции 7.

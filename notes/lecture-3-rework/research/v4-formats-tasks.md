---
title: "Промпт-форматы и типовые паттерны задач (2026)"
lecture: lec-03
type: research-brief
version: v4
date: 2026-09-13
sources_count: 20
note: >
  Sourced brief for advanced audience (все вайбкодят, работают в ИТ). Skeptical,
  concrete, per-task architecture choice. Fast-moving claims flagged [VFY-day-of].
---

# Промпт-форматы и типовые паттерны задач (2026)

Брифинг для лекции об архитектуре ИИ-систем. Планка аудитории высокая — не «что такое промпт», а **когда какой формат/паттерн выбрать и почему, с цифрами и границами применимости**.

---

## Часть 1 — Форматы промпта: Markdown vs XML vs JSON vs plain text

### 1.0 Главный тезис (skeptical framing)

Формат промпта — это **не магия и не косметика**. Есть измеримый эффект, но он **зависит от трёх осей**: (1) поколение/размер модели, (2) тип задачи (reasoning vs classification vs extraction vs I/O), (3) вход vs выход (структурируем контекст-вход или требуем структуру выхода). Frontier-модели 2026 к формату входа почти нечувствительны; малые/open-модели — очень чувствительны. Отдельная и более острая проблема — **принуждение структуры на выходе (JSON/грамматика) роняет reasoning**.

### 1.1 XML-теги — рекомендация Anthropic для структурирования входа

Anthropic **прямо документирует** XML-теги как основной приём разграничения «инструкции / контекст / данные / примеры» в сложных промптах.

Дословно из官方 гайда (platform.claude.com, «Prompting best practices», актуально для Opus 5 / Sonnet 5 / Fable 5.x):
- «XML tags help Claude **parse complex prompts unambiguously**, especially when your prompt mixes instructions, context, examples, and variable inputs. Wrapping each type of content in its own tag (`<instructions>`, `<context>`, `<input>`) reduces misinterpretation.»
- Best practices: consistent descriptive tag names; **вложенность** при иерархии (`<documents>` → `<document index="n">` → `<document_content>` + `<source>`).
- Few-shot примеры оборачивать в `<example>` / `<examples>` — «so Claude can distinguish them from instructions».
- **Long context (20k+ токенов):** длинные документы — **вверх промпта**, запрос/инструкции — внизу. «Queries at the end can improve response quality by **up to 30%** in tests, especially with complex, multi-document inputs.» Каждый документ — в `<document>` с сабтегами `<document_content>`/`<source>`.
- **Grounding-приём:** просить Claude сначала вытащить релевантные цитаты в `<quotes>`, потом отвечать на их основе — фокусирует модель на нужном и снижает шум.
- Управление форматом **выхода** тоже через XML-индикаторы: «Write the prose sections in `<smoothly_flowing_prose_paragraphs>` tags» + «match your prompt style to desired output» (уберёшь markdown из промпта — меньше markdown в ответе).
- Источник: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices ; https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Почему XML именно у Claude:** это артефакт того, как модель тренировали/файнтюнили (провайдер-специфичная конвенция), а не универсальный закон. OpenAI и Google в своих гайдах тяготеют к **Markdown-заголовкам**. Разумная эвристика из практики: GPT ≈ +5–10% с Markdown, Claude ≈ +5–10% с XML на **своих** задачах (это эвристика сообщества/вендор-доков, не строгий бенчмарк — `[VFY-day-of]`). Источники: https://theneuralbase.com/prompt-engineering/learn/beginner/model-specific-formatting-preferences/ ; https://www.robertodiasduarte.com.br/en/markdown-vs-xml-em-prompts-para-llms-uma-analise-comparativa/

### 1.2 JSON — для машинного I/O, structured outputs, function calling

JSON — это **интерфейс между моделью и кодом**, не формат «для размышления».

**Механика надёжности (OpenAI):**
- **JSON mode** (старое) гарантирует лишь *валидный* JSON, но **не** соответствие схеме.
- **Structured Outputs** (июнь 2024, `response_format={"type":"json_schema", strict:true}`) гарантирует **схему** через **constrained decoding** (на каждом шаге разрешены только токены, не нарушающие грамматику). OpenAI: модель сама достигает ~93% на их бенчмарке schema-adherence, а constrained decoding добивает до **~100%**.
- Реализация — **context-free grammars (CFG)**, а не FSM: CFG выражает вложенность/рекурсию (правильно матчит скобки в глубоко вложенном JSON). В мае 2025 OpenAI публично отметили `llguidance` как фундамент.
- **Function calling** — более мягкий вариант: без `strict:true` возможны отклонения от схемы.
- Источники: https://openai.com/index/introducing-structured-outputs-in-the-api/ ; https://developers.openai.com/api/docs/guides/structured-outputs ; https://www.aidancooper.co.uk/constrained-decoding/ ; https://letsdatascience.com/blog/structured-outputs-making-llms-return-reliable-json

**Anthropic-эквивалент:** есть фича Structured Outputs (constrain к схеме) — рекомендованная замена старому «prefill JSON»-хаку (prefill на последнем assistant-turn с моделей 4.6+ вообще запрещён, возвращает 400). Для классификации Anthropic советует **tool с enum-полем** валидных меток либо structured outputs. Источник: тот же best-practices гайд, раздел «Migrating away from prefilled responses».

**Издержки JSON — три штуки, все важны:**
1. **Токен-overhead.** Скобки/кавычки/двоеточия/запятые = лишние токены. Отсюда волна «token-oriented» форматов — **TOON** (Token-Oriented Object Notation): заявляет **30–60% экономии токенов** vs JSON на однородных массивах объектов (табличная плотность CSV + отступы YAML). Но есть «prompt tax»: на коротких контекстах инструкция «как читать TOON» съедает выигрыш; сам TOON добавляет ~5–10% на заголовки полей/декларации массивов. Это **новый и волатильный** формат (сообщество, конец 2025) — `[VFY-day-of]`. Источники: https://github.com/toon-format/toon ; https://arxiv.org/abs/2603.03306 ; https://www.tensorlake.ai/blog/toon-vs-json
2. **Надёжность генерации валидного JSON** — решается constrained decoding (см. выше), но…
3. **«Reasoning tax» — принуждение структуры роняет рассуждение** (ключевой skeptical-факт, см. 1.4).

### 1.3 Markdown — человекочитаемые инструкции

Markdown (заголовки, списки, `##`) — «дефолт» для человекочитаемых инструкций; у OpenAI/Google — рекомендованный способ структурировать промпт. **Когда его достаточно:** простые/средние промпты, одна-две секции, чат-режим, когда нет смешения «данные+инструкции+примеры» в одном большом контексте. Нюанс от Anthropic: свежие модели (Fable 5.1) **сами форматируют меньше**, и жёсткие анти-markdown-блоки могут задавить нужную структуру — под модель надо калибровать. Источник: best-practices гайд, раздел «Control the format of responses».

Практическое правило: **Markdown для человека-читателя, XML — когда надо машинно-однозначно разграничить блоки, JSON — только на стыке с кодом.**

### 1.4 Исследования: измеримый эффект формата (с baseline)

**A. «Does Prompt Formatting Have Any Impact on LLM Performance?» (Microsoft, 2024, arXiv 2411.10541).**
Сравнивали plain text / Markdown / JSON / YAML.
- **GPT-3.5-turbo: разброс до ~40%** между шаблонами на code-translation.
- **GPT-4 — заметно робастнее** к формату (баланс: разброс существенно меньше).
- Вывод: **чем крупнее/новее модель, тем меньше чувствительность к формату входа**. (PDF отдавался 403 — цифры по вторичным источникам.) Источники: https://www.researchgate.net/publication/385920920 ; https://pith.science/paper/2411.10541

**B. «Let Me Speak Freely?» (EMNLP-Industry 2024, arXiv 2408.02442) — самый важный для skeptical-нарратива.**
Принуждение **формата ответа** (JSON/structured) vs natural language:
- **GSM8K (математика): GPT-3.5-turbo падает с 76.6% (NL) до 49.3% (format-restricted) — минус 27.3 п.п.**
- Общий вывод: строгие форматные ограничения на выходе **деградируют reasoning** («Reasoning Tax»); одна из причин — модель ставит поле «ответ» **до** поля «рассуждение» (ломается chain-of-thought).
- Парадокс: те же ограничения **улучшают** classification-задачи (парсинг однозначнее).
- Источники: https://aclanthology.org/2024.emnlp-industry.91.pdf ; https://ar5iv.labs.arxiv.org/html/2408.02442

**C. «The Format Tax» (2026, arXiv 2604.03616) — свежая репликация на моделях 2026.** `[VFY-day-of]`
Форматы: JSON Schema / XML / Markdown / LaTeX vs freeform. Модели: open (Qwen3, OLMo3, SmolLM3, Nemotron3) + closed (GPT-5-Nano, Claude-Haiku-4.5, Grok-4.1-Fast).
- **Open-модели стабильно деградируют:** MATH-500 в среднем **−6.6 п.п.**; ZebraLogic **−3.5 п.п.**; WritingBench **−6…−18 п.п.** под LaTeX.
- **Closed frontier-модели робастны:** Claude-Haiku-4.5 и Grok-4.1-Fast около нуля (**+1.2…+2.5 п.п.**).
- **~92% деградации** даёт **сам факт требования формата в промпте**, а constrained-decoding добавляет лишь маргинально.
- **Митигации:** «2-Turn» (сначала freeform, потом переформатировать) возвращает **+6.8 п.п.**; extended thinking **+9.2 п.п.** (но риск −15% на части задач).
- Источник: https://arxiv.org/html/2604.03616v1

**Синтез для лекции:** «формат входа» (как разложить промпт) и «формат выхода» (что принудить на генерации) — **разные проблемы**. Первое: frontier-модели терпимы, малые — нет. Второе: принуждение структуры **вредит рассуждению** на всех, лечится паттерном «сначала думай свободно → потом переформатируй» (двухходовка), а не «думай сразу в JSON».

### 1.5 Матрица «формат → задача → почему»

| Формат | Модели/кто | Когда применять (задача) | Почему |
|---|---|---|---|
| **Plain text** | любые | простой одиночный запрос, чат | нет смешения блоков — структура не нужна; frontier не выигрывает от неё |
| **Markdown** | GPT/Gemini предпочитают; универсально | человекочитаемые инструкции, средние промпты, документы | заголовки/списки читаемы людям; вендор-конвенция OpenAI/Google |
| **XML-теги** | Claude предпочитает; полезно всем | сложный промпт: инструкции+контекст+данные+примеры; long-context multi-doc | однозначное разграничение блоков; вложенность документов; grounding через `<quotes>` |
| **JSON (+ Structured Outputs / strict)** | все, кто интегрирует с кодом | **машинный I/O**, function calling, tool-схемы, классификация с фикс-набором меток | контракт для парсера; constrained decoding → ~100% schema-adherence |
| **JSON НА reasoning-ответе** | — (анти-паттерн) | НЕ применять к «подумай и реши» | «reasoning tax»: −27 п.п. на GSM8K у GPT-3.5; ломает CoT |
| **YAML / TOON** | экспериментально | большие однородные табличные данные во входе, экономия токенов | 30–60% меньше токенов vs JSON; но `[VFY-day-of]` — новьё, prompt-tax на коротких |

**Разные семейства предпочитают разное:** да. Claude → XML; GPT/Gemini → Markdown (вендор-доки). Но на frontier-2026 разница в **aggregate accuracy** от формата входа мала — она сильнее у малых/open. Единственный устойчивый большой эффект — **не насиловать reasoning структурой выхода**.

---

## Часть 2 — Типовые паттерны задач: как их реально строить

Сквозной принцип (Anthropic, «Building Effective Agents», дек. 2024, актуально): **начинай с простейшего, повышай сложность только по необходимости**. Workflow (LLM+инструменты по заранее заданным путям в коде) предсказуем; agent (LLM сам рулит своими шагами и инструментами) — гибок, но каждый автономный ход добавляет латентность, стоимость и шанс, что ранняя ошибка размножится. Агента — только там, где путь нельзя захардкодить, но **можно верифицировать прогресс** (кодинг с тестами, поддержка с tool-backed действиями, computer-use со скриншотами как ground truth). Источник: https://www.anthropic.com/engineering/building-effective-agents

### 2.1 Ассистент с инструментами: one-shot vs tool-use vs full agent

**Дерево решения:**
1. **One-shot (просто промпт → ответ)** — если модель уже знает ответ и внешние действия не нужны. Дёшево, быстро, детерминированнее.
2. **Single tool-use / workflow** — если нужен доступ к данным/действию (поиск, БД, API), но **последовательность шагов известна** и её можно задать кодом. Human oversight ставится в фикс-точках.
3. **Full agent (агентная петля)** — если шаги заранее неизвестны, нужно планирование и адаптация, и есть способ проверять прогресс. Цена: латентность + токены + распространение ошибок.

Реальные промпт-паттерны (из官方 гайда Anthropic):
- **Явность действия:** «Change this function…» вместо «Can you suggest changes…» — иначе модель только советует, не делает.
- **Параллельные вызовы:** для независимых tool-calls — блок `<use_parallel_tool_calls>` (до ~100% успеха), но зависимые — строго последовательно, без плейсхолдеров.
- **Баланс автономии/безопасности:** для необратимых действий (rm -rf, force-push, публикация) — просить подтверждение; локальные обратимые (правка файла, тесты) — делать сразу.
- **Anti-overengineering / anti-hallucination** блоки: «Never speculate about code you have not opened… read the file before answering».
- Источник: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices (разделы Tool use, Agentic systems)

### 2.2 Генерация текста в заданном тоне / «человекоподобно»

**Приёмы (что работает):**
- **Few-shot style transfer** — дать 3–5 образцов авторского текста + summary контента, просить сгенерировать в том же стиле. Anthropic: 3–5 примеров, relevant + diverse + wrapped in `<example>`. Самый надёжный рычаг для тона/структуры/голоса.
- **Persona vs tone.** Роль в system-промпте («You are a helpful coding assistant specializing in Python») фокусирует тон/поведение. Но — **важная граница**, см. ниже.

**Границы и скепсис (teach judgment):**
- **Persona НЕ улучшает фактическую точность.** «Playing Pretend: Expert Personas Don't Improve Factual Accuracy» (arXiv 2512.05858, `[VFY-day-of]`): на MMLU expert-persona **проигрывает** базовой модели во всех 4 категориях — **68.0% vs 71.6%**. Механизм: «act as an expert» активирует instruction-following/«звучать авторитетно», что мешает извлечению знаний. Persona помогает для **стиля/выравнивания тона**, вредит для **фактов**. Источники: https://arxiv.org/pdf/2512.05858 ; https://arxiv.org/pdf/2508.19764
- **LLM плохо имитируют «неявный» стиль обычных людей.** «Catch Me If You Can? Not Yet» (arXiv 2509.14543): модели неплохо копируют публичных персон/вымышленных героев, но буксуют на индивидуальном стиле рядового автора — личный стиль не сводится к нескольким «ползункам». Источник: https://arxiv.org/html/2509.14543v1

**Риски и детектируемость (это учит суждению — где ИИ-текст неуместен/опасен):**
- **AI-детекторы ненадёжны как единственное доказательство.** Все крупные (Turnitin, GPTZero, Originality) **сами** пишут в доках: не использовать как единственное свидетельство.
- Разброс огромный: вендор-исследования дают 92–100% (Turnitin AI), независимые — часть детекторов **ниже 80%** точности; точность **резко падает после перефразирования**.
- **False positives и bias:** тексты не-нейтивов флагаются как ИИ до **+30%** чаще; sentence-level false-positive у Turnitin ~4% (при заявленном <1% document-level).
- Вывод для лекции: генерировать «человекоподобный» текст технически можно, но (а) выдавать за своё — этический/академический риск, (б) детекторам нельзя доверять ни как «щиту», ни как «мечу». Источники: https://link.springer.com/article/10.1007/s40979-026-00213-1 ; https://originality.ai/blog/ai-detection-studies-round-up ; https://en.wikipedia.org/wiki/Artificial_intelligence_content_detection

### 2.3 Исследовательская задача / deep research

**Архитектурный паттерн (реальные продукты):**
- **OpenAI Deep Research** (2025): reasoning-LLM (o3) + **agentic RAG**. Петля: (1) уточнение интента → (2) автономный multi-step план → (3) web-browsing + retrieval + вычисления → (4) verification claims + citation tracking → (5) отчёт **1 500–20 000 слов, 15–30 источников с точными URL**. o3 задаёт нижнюю планку галлюцинаций ~8%. Источники: https://venturebeat.com/ai/out-analyzing-analysts-openai-deep-research-pairs-reasoning-llms-with-agentic-rag-to-automate-work-and-replace-jobs ; https://intuitionlabs.ai/articles/chatgpt-deep-research-guide-ai-agents-rag
- **Perplexity Deep Research** — свой ассистент (фев. 2025). **Claude Research** — аналогичный агентный research-режим Anthropic.
- Обобщённая архитектура (обзоры «Deep Research Agents», arXiv 2506.18096, 2508.12752): centralized orchestrating agent + интегрированные planning & verification + browsing/RAG/citation/doc-processing как встроенные модули.

**Как строить самому (паттерн):** RAG (retrieval релевантных чанков) + **агентная петля** (план → поиск → чтение → синтез → self-critique) + **verification/citation-слой** (проверять факты по нескольким источникам, привязывать к URL). Anthropic-промпт для этого: «develop several competing hypotheses, track confidence levels, regularly self-critique, update a hypothesis tree/research notes file». Источник: best-practices гайд, раздел «Research and information gathering».

**Failure mode №1 — галлюцинированные цитаты (критично, учит скепсису):**
«Detecting and Correcting Reference Hallucinations…» (arXiv 2604.03173, `[VFY-day-of]`):
- **3–13% URL-цитат сфабрикованы**; ещё **5–18% не резолвятся**.
- **Deep-research агенты ХУЖЕ обычного search-augmented: 10.7% галлюцинаций vs 4.8%** — потому что генерируют кратно больше цитат на запрос.
- Разброс по доменам ~2× (Business 5.4% → Theology 11.4%).
- Митигация: инструмент верификации URL (`urlhealth`) снижает нерезолвящиеся ссылки в **6–79×**, до <1%.
- Источник: https://arxiv.org/html/2604.03173v1

**Связка с правилом курса (baseline/counterfactual):** deep-research любит выдавать цифры **без базы** («−50%», «5M acres») и подпирать их правдоподобной, но несуществующей ссылкой. Инженерный вывод: **любую метрику из ИИ-ресёрча — перепроверять по резолвящемуся первоисточнику**, число без базы = красный флаг.

### 2.4 Ещё один полезный паттерн: структурированная экстракция в JSON (extraction / classification)

Выбран как контрапункт к 2.3 — здесь структура выхода **помогает**, а не вредит (в отличие от reasoning).

**Как строить:**
- **Schema enforcement** — фиксированный набор именованных полей как строки, `null` для отсутствующих. Стандарт продакшн-пайплайнов извлечения из документов.
- Реализации: OpenAI `response_format={"type":"json_schema"}`; Anthropic Structured Outputs / tool с enum; open-модели через vLLM + constrained decoding.
- **Классификация** — tool с `enum`-полем валидных меток (Anthropic-рекомендация) либо structured outputs. «Let Me Speak Freely?» показал: на classification форматное ограничение **улучшает** результат (парсинг однозначен).

**Границы / скепсис (Structured Output Benchmark, arXiv 2604.25359, `[VFY-day-of]`):**
- **Schema-compliance почти идеальна, а value-accuracy — нет:** лучшее exact-match значений **83.0% (текст), 67.2% (изображения), 23.7% (аудио)**. Валидный JSON ≠ правильные данные.
- **Anti-hallucination приём:** требовать **evidence spans / дословные цитаты** из источника — «трудно галлюцинировать цитату, которую надо вытащить verbatim».
- **Constrained-decoding gotcha:** большие enum'ы, узкие minItems/maxItems, много cross-field constraints → таймауты компиляции грамматики. Constrain только то, что реально нужно downstream.
- Валидация: семантические валидаторы в коде (проверять распределения значений, не только типы); мониторить распределение confidence по полям.
- Источники: https://arxiv.org/html/2604.25359v1 ; https://simonwillison.net/2025/Feb/28/llm-schemas/ ; https://collinwilkins.com/articles/structured-output

---

## Сводка выбора архитектуры по задаче

| Задача | Формат промпта/выхода | Паттерн | Главная граница/риск |
|---|---|---|---|
| Простой ответ | plain / Markdown | one-shot | — |
| Действие во внешнем мире, путь известен | Markdown+XML вход | tool-use / workflow | предсказуемость > гибкость |
| Путь неизвестен, нужна адаптация | XML вход | full agent + верификация прогресса | латентность, размножение ошибок |
| Рассуждение/математика | НЕ принуждать JSON | «think free → reformat» (2-Turn) | reasoning tax −27 п.п. |
| Тон/стиль/«человечность» | few-shot `<example>` | style transfer + persona для тона | persona ↓ факты (68 vs 72%); детекторы ненадёжны |
| Deep research | XML multi-doc + `<quotes>` | RAG + agentic loop + citation-verify | 3–13% фейковых цитат; числа без базы |
| Извлечение/классификация | JSON Schema / enum-tool | structured outputs + constrained decoding | value-accuracy ≤83%; verbatim-цитаты против галлюцинаций |

---

## Источники (полный список)

**Primary / вендор:**
- Anthropic prompt best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic — Building Effective Agents — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic — Effective context engineering — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI — Introducing Structured Outputs — https://openai.com/index/introducing-structured-outputs-in-the-api/
- OpenAI — Structured Outputs guide — https://developers.openai.com/api/docs/guides/structured-outputs

**Исследования — форматы:**
- Does Prompt Formatting Have Any Impact? (arXiv 2411.10541) — https://pith.science/paper/2411.10541
- Let Me Speak Freely? (EMNLP 2024, arXiv 2408.02442) — https://aclanthology.org/2024.emnlp-industry.91.pdf ; https://ar5iv.labs.arxiv.org/html/2408.02442
- The Format Tax (arXiv 2604.03616) `[VFY-day-of]` — https://arxiv.org/html/2604.03616v1
- TOON vs JSON benchmark (arXiv 2603.03306) `[VFY-day-of]` — https://arxiv.org/abs/2603.03306 ; https://github.com/toon-format/toon
- Constrained decoding explainer — https://www.aidancooper.co.uk/constrained-decoding/

**Исследования — задачи/паттерны:**
- Expert Personas Don't Improve Factual Accuracy (arXiv 2512.05858) `[VFY-day-of]` — https://arxiv.org/pdf/2512.05858
- Principled Personas (arXiv 2508.19764) — https://arxiv.org/pdf/2508.19764
- LLMs Struggle to Imitate Implicit Writing Styles (arXiv 2509.14543) — https://arxiv.org/html/2509.14543v1
- Reference Hallucinations in Deep Research (arXiv 2604.03173) `[VFY-day-of]` — https://arxiv.org/html/2604.03173v1
- Deep Research Agents survey (arXiv 2506.18096) — https://arxiv.org/pdf/2506.18096
- Structured Output Benchmark (arXiv 2604.25359) `[VFY-day-of]` — https://arxiv.org/html/2604.25359v1
- Simon Willison — LLM schemas — https://simonwillison.net/2025/Feb/28/llm-schemas/

**Deep research продукты:**
- VentureBeat — OpenAI Deep Research + agentic RAG — https://venturebeat.com/ai/out-analyzing-analysts-openai-deep-research-pairs-reasoning-llms-with-agentic-rag-to-automate-work-and-replace-jobs
- IntuitionLabs — ChatGPT Deep Research guide — https://intuitionlabs.ai/articles/chatgpt-deep-research-guide-ai-agents-rag

**AI-детекторы:**
- Springer IJEI — accuracy of AI content detectors — https://link.springer.com/article/10.1007/s40979-026-00213-1
- Originality.AI meta-analysis (16 studies, вендор — читать критично) — https://originality.ai/blog/ai-detection-studies-round-up
- Wikipedia — AI content detection — https://en.wikipedia.org/wiki/Artificial_intelligence_content_detection

**Model-specific format preferences (вторичные, эвристики):**
- Neural Base — model-specific formatting — https://theneuralbase.com/prompt-engineering/learn/beginner/model-specific-formatting-preferences/
- Markdown vs XML analysis — https://www.robertodiasduarte.com.br/en/markdown-vs-xml-em-prompts-para-llms-uma-analise-comparativa/

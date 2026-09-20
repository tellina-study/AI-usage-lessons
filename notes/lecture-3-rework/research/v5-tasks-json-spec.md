# v5 — «Типовые задачи»: формализация + JSON-extraction как техника (не мем)

Research pack для переработки слайдов «типовые задачи» лекции 3. Задачи владельца:
1. JSON-extraction слайд: мем → конкретная техника «как правильно задать JSON-вывод в промпте».
2. Формализовать остальные типовые задачи (ассистент-с-инструментами, текст в тоне / человекоподобный, deep research): input → метод → ключевые ручки → валидация → failure mode.
3. Разложить задачи по слоям: что реально prompt-level, а что architecture-level (deep research = RAG+agent).

Дата сбора: 2026-09-15. Волатильные факты помечены `[VFY-day-of]`.

---

## Часть 1. Как правильно задать JSON-вывод в промпте (техника вместо мема)

### 1.1. Два уровня контроля — это ключевая рамка слайда

Есть принципиальная разница между **«попросить JSON промптом»** и **«гарантировать JSON на уровне декодера»**. Это два разных механизма, и путать их — главная ошибка новичка.

| Уровень | Механизм | Что гарантирует | Что НЕ гарантирует |
|---|---|---|---|
| **Prompt-level** (промпт + few-shot) | Текстовая инструкция «верни JSON по схеме» | ничего жёстко — ~80% валидности у JSON mode | синтаксис, поля, типы |
| **Decode-level** (constrained decoding / structured outputs) | Схема компилируется в грамматику, маскирует токены при генерации | 100% синтаксически валидный JSON, совпадающий со схемой | **корректность значений** (см. §1.6) |

Ключевой инсайт для слайда: **валидный JSON ≠ правильные данные**. Constrained decoding убирает parsing-ошибки, но не убирает галлюцинации в значениях полей ([Towards Data Science: «Your JSON Is Valid but Your Data Is Wrong»](https://towardsdatascience.com/your-json-is-valid-but-your-data-is-wrong-five-failure-modes-llm-structured-outputs-wont-catch/)).

### 1.2. Как задать схему в промпте — три способа и их trade-offs

| Способ | Плюсы | Минусы | Когда |
|---|---|---|---|
| **Пример-объект** (образец JSON) | самый понятный модели; мгновенно читается человеком | неявные типы/enum'ы; нет описаний полей | простые плоские структуры, быстрый прототип |
| **JSON Schema** | машинно-проверяемый контракт; enums, required, типы, вложенность; напрямую скармливается в structured-output API | многословный; токены схемы едят input-бюджет; сложная схема → деградация (см. §1.6) | production, валидация в коде |
| **TypeScript-тип / Pydantic / Zod** | компактный и читаемый; type-safety в коде; SDK сами конвертят в JSON Schema | нужен рантайм-конвертер; не все конструкции переводятся 1:1 | инженерный код на TS/Python |

Практика: держи схему **минимальной**, размещай её **в конце промпта** и добавляй `Верни ТОЛЬКО JSON, без markdown-обёртки` — это заметно снижает лишнюю прозу и code-fence обёртки ([Arunabh Priyadarshi](https://www.arunabh.me/blog/prompt-engineering-structured-json); [Level Up Coding](https://levelup.gitconnected.com/prompt-engineering-best-practices-for-structured-ai-outputs-ee44b7a9c293)).

### 1.3. Что кладём в описание полей

- **Описания/аннотации полей** — в JSON Schema поле `description` реально влияет на заполнение; модель читает их как микро-инструкции.
- **Enums для ограниченных значений** — перечисляй КАЖДОЕ допустимое значение явно (`"status": "one of [open, closed, pending]"`). Это убирает свободную интерпретацию.
- **required vs optional** — явно указывай обязательные поля. У OpenAI strict-режим требует, чтобы все поля были в `required` (опциональность эмулируется через union с `null`).
- **Лимит глубины вложенности** — держи структуру плоской, насколько возможно. Глубокая вложенность и сотни полей резко повышают риск деградации (§1.6). У провайдеров есть внутренние лимиты на число ключей/глубину.

### 1.4. Few-shot: покажи точную форму вывода

2–3 примера пар «вход → ожидаемый JSON» демонстрируют форму лучше любого описания. Особенно важно для: формата дат, пустых значений (`null` vs `""` vs пропуск поля), единиц измерения, вложенных массивов. Немного примеров «edge-case» входов (пустой вход, неоднозначный вход) фиксируют поведение на границах ([Level Up Coding](https://levelup.gitconnected.com/prompt-engineering-best-practices-for-structured-ai-outputs-ee44b7a9c293)).

### 1.5. Гарантия на уровне декодера — provider support (2026)

Это самый «свежий» блок; проверить актуальность моделей `[VFY-day-of]`.

**Как это работает под капотом (единый принцип у всех):** схема компилируется в контекстно-свободную грамматику (CFG). На каждом шаге декодирования токены, нарушающие грамматику, получают logit = −∞ и не могут быть выбраны. Итог — модель физически не может сгенерировать невалидный токен ([Aidan Cooper: constrained decoding guide](https://www.aidancooper.co.uk/constrained-decoding/); [DEV: JSON mode, function calling, grammar-constrained decoding](https://dev.to/tech_nuggets/structured-output-from-llms-json-mode-function-calling-and-grammar-constrained-decoding-355d)).

| Провайдер / инструмент | Механизм | Статус (2026) `[VFY-day-of]` |
|---|---|---|
| **OpenAI Structured Outputs** | `response_format: { type: "json_schema", strict: true }` — constrained sampling; 100% schema adherence vs ~80% у legacy JSON mode | GA; legacy `json_object` (JSON mode) только гарантирует синтаксис ([OpenAI](https://openai.com/index/introducing-structured-outputs-in-the-api/)) |
| **Anthropic Claude** | два пути: (1) **structured outputs** — параметр `output_format` с JSON Schema; (2) **strict tool use** — `strict: true` в определении tool + pinned `tool_choice`, ответ приходит как `tool_use.input` (валидированный объект). Под капотом — constrained decoding (схема → грамматика) | **GA** нативно на Claude Developer Platform и в Amazon Bedrock для Sonnet 4.5 / Opus 4.5 / Haiku 4.5 (ранее public beta с ноября 2025, header `anthropic-beta: structured-outputs-2025-11-13`; GA снял beta-header и добавил сложные схемы) ([claude.com blog](https://claude.com/blog/structured-outputs-on-the-claude-developer-platform); [AWS](https://aws.amazon.com/about-aws/whats-new/2026/02/structured-outputs-available-amazon-bedrock/)) `[VFY-day-of]` |
| **Google Gemini** | generation-config: `responseMimeType: "application/json"` + `responseSchema` (OpenAPI-subset) или `responseJsonSchema` (JSON Schema); подмножество OpenAPI Schema | GA; но плохо тянет сложные/глубоко-вложенные схемы (§1.6) ([Firebase AI Logic](https://firebase.google.com/docs/ai-logic/generate-structured-output); [ai.google.dev](https://ai.google.dev/gemini-api/docs/structured-output)) |
| **Open-source: Outlines / Guidance / XGrammar** | токен-маскинг: JSON Schema/Pydantic → CFG → маска валидных токенов на каждом шаге. Предпочитать маскинг, а не resample-if-invalid (медленно) | зрелые; Outlines/xgrammar/llama.cpp не генерируют невалидный токен вообще ([Aidan Cooper](https://www.aidancooper.co.uk/constrained-decoding/)) |
| **llama.cpp / vLLM: GBNF-грамматики** | GBNF (GGML BNF) — расширенный BNF с классами символов и повторами; рантайм ограничивает декодинг напрямую. Даёт произвольные грамматики, не только JSON | стабильно; работает и для не-JSON DSL (напр. ассемблер под кастомный CPU) ([James Randall: GBNF](https://www.jamesdrandall.com/posts/gbnf-constrained-generation/); [Tian Pan](https://tianpan.co/blog/2026-04-16-grammar-constrained-generation-output-reliability)) |

**Ограничения decode-level гарантий (важно для честности слайда):**
- Не гарантирует **правильность значений** — только форму (§1.6, failure modes).
- Compiled-грамматика растёт с числом свойств, глубиной вложенности и мощностью массивов; для схем в сотни ключей автомат может упереться во внутренние лимиты провайдера или per-token overhead деградирует качество ([ExtractBench arXiv 2602.12247](https://arxiv.org/pdf/2602.12247)).
- Не для творческих/открытых задач — грамматика душит генерацию (см. §1.6 reasoning tax).
- У Gemini на дообученных (tuned) моделях structured output может **снижать качество** ([Google Cloud docs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output)).

### 1.6. Нюансы и подводные камни (ядро «настоящей техники»)

**1. «Reasoning tax» — не заставляй рассуждать в JSON.** Форматные ограничения деградируют качество рассуждений. Классика — [«Let Me Speak Freely?» (Tam et al., 2024, arXiv 2408.02442)](https://arxiv.org/pdf/2408.02442): 10–15% падение точности при жёстком JSON-mode против свободной генерации с последующей конвертацией. Более свежие работы — до 17% в среднем и до 26% на творческих задачах; жёсткая schema-enforcement давала 100% валидности, но −до 8.7 п.п. точности ответа. Причина — **premature serialization**: модель тратит внимание на соблюдение формата, а не на сам ответ.
   → **Рецепт: «think first, format later».** Отдели фазу рассуждения от фазы форматирования. Пусть модель сначала рассуждает свободным текстом, потом отдельным шагом (или отдельным полем в конце) выдаёт JSON. Сильные модели «поглощают» формат-налог лучше слабых — это про capacity, а не про сам формат ([«Capacity, Not Format» arXiv 2606.09410](https://arxiv.org/pdf/2606.09410)). `[VFY-day-of]` цифры процентов.

**2. Сложная схема → деградация точности.** Даже при валидном JSON точность извлечения падает: на ExtractBench pass-rate GPT-5 на кредитных договорах упал с 86.9% до 70.0% при жёстком structured mode; эффект сильнее на длинных извлечениях с cross-references и на схемах в сотни ключей ([ExtractBench arXiv 2602.12247](https://arxiv.org/pdf/2602.12247)). Gemini `responseSchema` «хорош для маленьких чистых выводов, но не тяни на нём сложные связи данных» ([Ubaidullah Omer](https://medium.com/@ubaidullahmomer/why-google-geminis-response-schema-isn-t-ready-for-complex-json-46f35c3aaaea)). JSON-Schema проиграл natural language в 5 из 6 задач на бенчмарке Shuffled Objects (>10 п.п. разрыв).
   → **Рецепт:** дроби большую схему на несколько вызовов; держи вложенность мелкой.

**3. Truncation длинного JSON.** Если вывод упирается в `max_tokens`, JSON обрывается на полуслове и не парсится. Рецепт: адекватный лимит токенов; для больших выборок — пагинация/чанкинг вывода; стриминг + инкрементальный парсер.

**4. Escaping / Unicode.** Кириллица, кавычки, переносы строк внутри строковых значений — источник невалидности при prompt-only подходе. Constrained decoding это снимает; при prompt-only — явно требуй корректного экранирования и валидируй в коде.

**5. Markdown-обёртка и лишние поля.** Самый частый provider-agnostic сбой prompt-only: JSON приходит в ```` ```json ```` fence, с лишними/недостающими полями или неверными типами. Рецепт: `Верни ТОЛЬКО JSON`, схема в конце, + defensive-парсинг (никогда не парси наивно).

**6. Когда НЕ форсить JSON.** Для творческих и reasoning-тяжёлых задач — дай свободный вывод, потом отдельным дешёвым шагом распарси/структурируй. Правило: **структура должна соответствовать capacity модели** — сильная модель вытянет, слабую формат уронит.

**Инвариант всех нюансов:** structured output никогда не заменяет валидацию в коде. Каждый JSON — валидировать перед использованием ([educative](https://educative.io/blog/what-is-prompt-engineering)).

### 1.7. Конкретный пример GOOD vs BAD (для слайда)

Задача: извлечь из текста отзыва структурированные поля.

**BAD-промпт (мем-уровень):**
```
Извлеки данные из отзыва и верни как JSON.

Отзыв: "Купил наушники за 5000 руб, звук огонь, но микрофон тихий. 4/5"
```
Проблемы: нет схемы; неясны имена полей, типы, enum'ы; нет формата рейтинга (4? 4.0? "4/5"?); модель обернёт в markdown, добавит болтовню, придумает поля.

**GOOD-промпт (техника):**
```
Ты извлекаешь структурированные данные из отзывов о товарах.
Верни ТОЛЬКО JSON по схеме ниже. Без markdown, без пояснений.

Схема:
{
  "product":   string  // название товара
  "price_rub": number  // цена в рублях, только число; null если не указана
  "rating":    number  // оценка 1-5, дробное допустимо; null если нет
  "sentiment": string  // one of ["positive","neutral","negative"]
  "pros":      string[] // короткие фразы; [] если нет
  "cons":      string[] // короткие фразы; [] если нет
}

Пример:
Вход:  "Отличный чайник, греет быстро, но крышка хлипкая. 4/5"
Выход: {"product":"чайник","price_rub":null,"rating":4,"sentiment":"positive","pros":["греет быстро"],"cons":["крышка хлипкая"]}

Отзыв: "Купил наушники за 5000 руб, звук огонь, но микрофон тихий. 4/5"
```
Что сделано правильно: явная схема с типами и комментариями; enum для `sentiment`; правило для отсутствующих значений (`null` / `[]`); few-shot с точной формой; `Верни ТОЛЬКО JSON`; схема в конце.

**Production-версия:** тот же контракт передать в decode-level гарантию (OpenAI `json_schema strict`, Anthropic `output_format` / strict tool, Gemini `responseSchema`) — тогда синтаксис гарантирован грамматикой, а промпт-инструкции работают на **корректность значений**.

---

## Часть 2. Формальный разбор остальных типовых задач

Единый шаблон: **вход → метод/архитектура → ключевые ручки → валидация → failure mode**.

### 2.1. Ассистент с инструментами (tool-using assistant / agent)

- **Вход:** запрос пользователя + набор определений инструментов (имя, описание, input_schema) + системная инструкция.
- **Метод/архитектура:** цикл **perceive → plan → act → observe**, повторяется до цели/стоп-условия. Доминируют два паттерна: **ReAct** (одна пара «мысль → действие → наблюдение» за шаг; reasoning и вызов инструментов чередуются) и **plan-and-execute** (план целиком вперёд, потом исполнение). Есть варианты ReWOO, Reflexion ([Atlan: agent loop](https://atlan.com/know/ai-agent/what-is-an-agent-loop/); [The AI Engineer: 4 single-agent patterns](https://theaiengineer.substack.com/p/the-4-single-agent-patterns)).
- **Ключевые ручки:** granularity инструментов (крупные vs атомарные); строгие input-схемы инструментов (валидация на границе); `tool_choice` (auto / forced / none); лимит итераций и бюджет токенов (защита от runaway-цикла); структурированные error-ответы от инструментов, которые модель может интерпретировать.
- **Валидация:** проверять аргументы вызова инструмента ДО обращения к внешнему API (reject invalid at boundary → структурированная ошибка); проверять, что финальный ответ опирается на результаты инструментов, а не на параметрическую память.
- **Failure mode:**
  - **Silent failure loop** — модель зациклилась на вызовах, молча жжёт токены (кейс: Claude Code инстанс сжёг 1.67 млрд токенов за 5 часов, июль 2025) `[VFY-day-of]`.
  - **Parametric fallback** — после сбоя инструмента модель решает, что «своих знаний хватит», и перестаёт искать (ломает саму гарантию tool-use для свежих данных).
  - **Plan abandonment** — модель бросает план (>50% случаев даже у сильных моделей по одному из бенчмарков) `[VFY-day-of]`.
  - End-to-end на многошаговых задачах: ведущие агенты закрывают лишь ~30–35% ([CMU 2025 benchmarks через Atlan](https://atlan.com/know/ai-agent/what-is-an-agent-loop/)) `[VFY-day-of]`.
  ([DEV: tool-use API design patterns](https://dev.to/adamo_software/tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures-f29))

### 2.2. Текст в заданном тоне / человекоподобный

- **Вход:** задача-контент + спецификация стиля (формальность, эмоциональная окраска, персона/роль, ограничения на длину и лексику).
- **Метод/архитектура:** **чистый prompt-level** — persona/role prompting + краткий style-guide. Роль в том же домене, что задача; описание персоны конкретное и детальное. Короткий style-guide (1–3 предложения) о формальности/сленге/эмодзи эмулирует манеру письма ([PromptHub: role-prompting](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference); [«From Instruction to Output» arXiv 2602.11179](https://arxiv.org/pdf/2602.11179)).
- **Ключевые ручки:** формальность («академический стиль» vs «дружелюбно и просто»); эмоциональная окраска; персона («как научный руководитель…»); few-shot образцов нужной манеры; явные запреты (без канцелярита / без эмодзи / без превосходных форм).
- **Валидация:** сложнее всего — стиль слабо формализуем. LLM-as-judge на соответствие тону; проверка на конкретные маркеры (длина предложений, наличие/отсутствие лексики); человеческая выборочная вычитка. Persona-augmented бенчмарки существуют, но fine-grained multi-attribute контроль остаётся открытой проблемой.
- **Failure mode:** **конфликт атрибутов** при fine-grained multi-attribute контроле — «формально, но тепло, но кратко, но с деталями» тянут в разные стороны, модель проседает по части измерений. Также: persona-дрейф на длинных диалогах; «AI-tell» фразы (шаблонные обороты), выдающие машину, несмотря на инструкцию. Role-prompting **не всегда** улучшает фактические/reasoning-задачи — эффект в основном на open-ended/стилевых ([PromptHub](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference)).

### 2.3. Deep research (это НЕ prompt-задача — см. Часть 3)

- **Вход:** исследовательский вопрос (широкий, многоаспектный) + доступ к источникам (web search, MCP-серверы, внутренние vector stores).
- **Метод/архитектура:** **architecture-level**, orchestrator-worker + agentic RAG. Ведущий агент декомпозирует вопрос на подзадачи и порождает 3–5 специализированных субагентов параллельно, затем синтез + отдельный citation-pass. У Anthropic такая схема дала +90.2% над single-agent Opus 4 на внутренних оценках `[VFY-day-of]`. Каждый субагент получает: цель, формат вывода, гайд по инструментам/источникам, границы задачи ([Anthropic: multi-agent research](https://www.anthropic.com/engineering/multi-agent-research-system)).
- **Отличие от классического RAG:** статический RAG — один заход «retrieve top-k → generate». Здесь — **agentic RAG**: reasoning-цикл, где LLM-оркестратор решает что искать, оценивает результаты, решает искать дальше или отвечать ([Towards Agentic RAG survey arXiv 2507.09477](https://arxiv.org/pdf/2507.09477); [The AI Engineer](https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep)).
- **Ключевые ручки:** число субагентов и их специализация; глубина/ширина поиска (сколько раундов, когда останавливаться); стратегия синтеза; отдельный citation-pass для трассируемости; retrieval interface (плоский vs иерархический).
- **Валидация:** citation-pass привязывает утверждения к источникам; adversarial-проверка claims; **synthesis gap** — умеет ли агент не только найти, но и организовать/синтезировать (отдельная метрика) ([«Synthesis Gap» arXiv 2601.12369](https://arxiv.org/pdf/2601.12369)).
- **Failure mode:** synthesis gap (нашёл, но не синтезировал); parametric fallback субагентов; координационные потери оркестратора; стоимость (много параллельных агентов = много токенов).

---

## Часть 3. Раскладка задач по слоям: prompt-level vs architecture-level

Владелец прав: **deep research не место в разделе про промпты** — это RAG+agent, т.е. архитектурная задача. Рамка для слайда-разделителя:

| Задача | Слой | Почему |
|---|---|---|
| Ассистент (простой Q&A / инструкция) | **Prompt-level** | один вызов, всё решает формулировка |
| Заданный тон / человекоподобный текст | **Prompt-level** | persona + style-guide в промпте, без внешней архитектуры |
| Извлечение (JSON-extraction) | **Prompt-level** (+опц. decode-level гарантия) | схема + few-shot в промпте; structured-output API — усиление, не смена слоя |
| Классификация | **Prompt-level** | enum-контракт + few-shot; один вызов |
| Суммаризация | **Prompt-level** | один вызов; длинные тексты → chunking, но это уже граница |
| **Ассистент С ИНСТРУМЕНТАМИ** | **Architecture-level** (пограничный) | нужен tool-loop, валидация на границе, лимиты цикла — это уже агент, не просто промпт |
| **Deep research** | **Architecture-level** | orchestrator-worker + agentic RAG + retrieval + citation-pass; промпт — лишь одна деталь |

**Рекомендация по структуре лекции:**
- **В разделе «Промпты»** оставить: ассистент (без инструментов), тон/человекоподобный текст, JSON-extraction, классификация, суммаризация. Это задачи, где рычаг — формулировка промпта.
- **Вынести за раздел промптов** (в раздел про RAG/агентов, который в лекции уже есть — см. `v5-rag-*.md`, `v5-agents-cases-mcp.md`): deep research и ассистент-с-инструментами. Для них промпт — необходимое, но далеко не достаточное; определяющее — архитектура (loop, retrieval, оркестрация, валидация на границах).
- Разделительная линия для слайда: **«меняешь строку промпта → меняется результат»** (prompt-level) vs **«нужен цикл/поиск/оркестрация/валидация вызовов»** (architecture-level). Tool-using assistant — честный пограничный случай: минимальный один инструмент ещё «почти промпт», но полноценный агентский цикл — уже архитектура.

Границей prompt→architecture служит момент, когда одного вызова модели перестаёт хватать: появляется цикл, внешний retrieval, несколько агентов или обязательная валидация вызовов инструментов.

---

## Источники

- OpenAI — [Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)
- Anthropic/Claude — [Structured outputs on the Claude Developer Platform (GA)](https://claude.com/blog/structured-outputs-on-the-claude-developer-platform)
- AWS — [Structured outputs now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/02/structured-outputs-available-amazon-bedrock/)
- Google — [Gemini structured output docs](https://ai.google.dev/gemini-api/docs/structured-output) · [Firebase AI Logic](https://firebase.google.com/docs/ai-logic/generate-structured-output) · [Vertex control generated output](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output)
- Constrained decoding — [Aidan Cooper: A Guide to Structured Generation](https://www.aidancooper.co.uk/constrained-decoding/) · [DEV: JSON mode, function calling, grammar-constrained decoding](https://dev.to/tech_nuggets/structured-output-from-llms-json-mode-function-calling-and-grammar-constrained-decoding-355d) · [James Randall: GBNF-constrained generation](https://www.jamesdrandall.com/posts/gbnf-constrained-generation/) · [Tian Pan: grammar-constrained generation](https://tianpan.co/blog/2026-04-16-grammar-constrained-generation-output-reliability)
- Reasoning tax / format tax — [«Let Me Speak Freely?» Tam et al. 2024 (arXiv 2408.02442)](https://arxiv.org/pdf/2408.02442) · [«Capacity, Not Format» (arXiv 2606.09410)](https://arxiv.org/pdf/2606.09410)
- Сложные схемы / extraction — [ExtractBench (arXiv 2602.12247)](https://arxiv.org/pdf/2602.12247) · [Ubaidullah Omer: Gemini responseSchema fails for complex JSON](https://medium.com/@ubaidullahmomer/why-google-geminis-response-schema-isn-t-ready-for-complex-json-46f35c3aaaea)
- Valid-but-wrong — [Towards Data Science: five failure modes](https://towardsdatascience.com/your-json-is-valid-but-your-data-is-wrong-five-failure-modes-llm-structured-outputs-wont-catch/)
- Prompt best practices — [Level Up Coding](https://levelup.gitconnected.com/prompt-engineering-best-practices-for-structured-ai-outputs-ee44b7a9c293) · [Arunabh Priyadarshi](https://www.arunabh.me/blog/prompt-engineering-structured-json)
- Agent loop / failure modes — [Atlan: AI agent loop](https://atlan.com/know/ai-agent/what-is-an-agent-loop/) · [DEV: tool-use API design patterns](https://dev.to/adamo_software/tool-use-api-design-for-llms-5-patterns-that-prevent-agent-loops-and-silent-failures-f29) · [The AI Engineer: 4 single-agent patterns](https://theaiengineer.substack.com/p/the-4-single-agent-patterns)
- Persona/tone — [PromptHub: role-prompting](https://www.prompthub.us/blog/role-prompting-does-adding-personas-to-your-prompts-really-make-a-difference) · [«From Instruction to Output» (arXiv 2602.11179)](https://arxiv.org/pdf/2602.11179)
- Deep research architecture — [Anthropic: multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system) · [The AI Engineer: Anthropic multi-agent deep research](https://theaiengineer.substack.com/p/how-anthropic-built-multi-agent-deep) · [Agentic RAG survey (arXiv 2507.09477)](https://arxiv.org/pdf/2507.09477) · [Synthesis Gap (arXiv 2601.12369)](https://arxiv.org/pdf/2601.12369)

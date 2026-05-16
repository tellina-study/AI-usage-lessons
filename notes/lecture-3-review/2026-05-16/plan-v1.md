# Лекция 3 «Архитектуры AI-систем: агенты, RAG, API»
## Plan v1 — orchestrator draft (input для Phase 1 critique)

**Issue:** #87 · **Branch:** `issue-87-lec-03-architectures`
**Длительность:** 75 мин (~70 мин активный контент + ~5 мин Q&A/буфер)
**Аудитория:** 3 курс ИУ6 МГТУ им. Баумана, инженеры-разработчики (универсально — без локального binding в chapter)
**Curriculum level:** introductory / overview (Модуль 1, лекция 3 — последняя обзорная перед отраслевыми)
**Дата:** 2026-05-16 · **Pipeline phase:** Phase 1 (план → critique → roast → USER GATE 0 → Phase 2 chapter)
**LO (canon-locked, РПД):** **LO7** (primary) + **LO4** (secondary).
**Tone:** инженерно-аналитический, anti-hype. Тезис: *выбор архитектуры — инженерное решение под задачу, а не мода; часто правильный ответ — самый простой, иногда — вообще без ИИ.*

**Inputs:**
- Canon: `library/project/course-plan.md` (Лекция 3 brief), `library/normative/rpd-otraslevoe-primenenie-ai.md`.
- Research: `notes/research/lecture-3/{trends-2026,decision-criteria,failures-and-limitations,sources}.md`.
- Style/format reference: `notes/lecture-2-review/final/plan-v2-final.md`; reference-модель failure-структуры — lec-07.
- Handoff: lec-02 s28 промис («Лекция 3: Агенты, RAG, API») + lec-02 changelog (s11 «Search → основа RAG» deferred to Лекция 3).
- Owner-директива (память `feedback_chapter_depth`): chapter — глубокий расширенный референс + Q&A-бэкап.

---

## 1. Контекст и зависимости

### 1.1 Промис из Лекции 2 — выполняется
Лекция 2 s28 обещала Лекцию 3 = «как AI выходит за пределы чата»: RAG (поверх эмбеддингов s10–s12), Tools/function calling, MCP, Agent loop. Лекция 3 раскрывает все 4 + добавляет ось решения «промпт/RAG/fine-tune/агент/код».

### 1.2 Что НЕ повторяем (надстраиваемся, не дублируем)

| Тема | Где в Lec-2 | Что Лекция 3 делает |
|---|---|---|
| Эмбеддинги, semantic search | §2 (s09–s12) | Используем как готовый блок → строим RAG (не переобъясняем similarity) |
| Single-shot inference, autoregressive loop | §4 (s21) | Надстраиваем: tool use / agent loop ВОКРУГ inference |
| Температура, 4 ручки API | §4 (s19–s20) | Не повторяем; API-слой = структурный вывод, function calling, caching |
| ML vs LLM decision tree | s25 | Расширяем до полной лестницы архитектур (код→…→multi-agent) |
| Контекстное окно | §3 (s16–s17) | Используем для «RAG vs long-context» аргумента (context rot) |

### 1.3 Курсовая прогрессия
Лекция 1 (типы AI, промпт=роль+задача+контекст) → Лекция 2 (почему промпт работает: internals) → **Лекция 3 (как собрать систему вокруг модели и КАК ВЫБРАТЬ архитектуру)** → отраслевые Лекции 4–17 применяют этот выбор. Парный **Семинар 3** «Архитектурный выбор: чат/агент/RAG/API — 3 кейса» (LO7, LO4) — ДЗ-мост.

### 1.4 Сквозные темы курса (canon — обязательны в каждой лекции)
- **Безопасность:** API-ключи, уровни доступа, кто видит данные в цепочке агент→инструмент→внешний API→провайдер (Раздел 4, плотный блок).
- **Человек vs AI:** человек-валидатор — проверяет *результат и факты*, не self-rationale модели (CoT может быть unfaithful).
- **Выбор инструмента:** ядро лекции (LO7) — лестница + матрица + чек-лист.
- **Паттерны/антипаттерны:** Chain-of-thought как паттерн рассуждения (+ его предел: faithfulness); анти-паттерны — overengineering агентом, fine-tune ради знаний, RAG без observability.

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос
> **«У меня есть задача и доступ к LLM. Какую архитектуру выбрать — и когда правильный ответ "не ИИ"?»**

Задаётся в s04 (после hook'а с провалом неверного выбора). Возвращается: s_RAG (когда НЕ RAG), s_FT (когда НЕ fine-tune), s_agent (когда НЕ агент), payoff — финальный чек-лист s_checklist + матрица s_matrix.

### 2.2 Арка (≈29 слайдов, 75 мин)

| Этап | Слайды | Бюджет | Функция |
|---|---|---|---|
| 0. Открытие + recap + ЦВ | s01–s04 | 8 мин | Hook: Air Canada (неверная архитектура = юр. ответственность); cover+roadmap; recap Lec-2 + мост; центральный вопрос + «лестница сложности» тизер |
| 1. Промпт и его границы | s05–s08 | 9 мин | Дефолт = 1 LLM-вызов; few-shot; **Chain-of-thought** (паттерн лекции) + его предел (CoT unfaithful); context engineering / context rot |
| 2. RAG | s09–s13 | 13 мин | Принцип (retrieval поверх эмбеддингов + LLM); когда применять; **когда НЕ** (корпус влезает в окно; фикс. политика); провал #5 (тихая деградация) + Air Canada как grounding-провал; гибрид/GraphRAG (кратко) |
| 3. Fine-tune vs промпт vs RAG | s14–s17 | 10 мин | 2026-реальность: FT не «ушёл», сузился до поведения/стиля/дистилляции; PEFT вытеснил full-FT; провал #2 catastrophic forgetting; критерии выбора; гибрид = норма |
| 4. API · tools · MCP · агенты + безопасность | s18–s24 | 18 мин | API-слой (structured output, function calling, prompt caching); MCP (стандарт); agent loop plan→act→check→iterate; workflow vs agent; multi-agent дебаты; **плотный failure/security блок** (#1,#3,#15; #6–#12) |
| 5.框架 решения + финал | s25–s29 | 12 мин | Лестница сложности; матрица выбора; критерии «когда НЕ»; **чек-лист (LO7 payoff)** + микро-применение (LO4); человек-валидатор + MIT NANDA #16; мост к отраслям + ДЗ С3 + Q&A |
| Буфер | — | 5 мин | Q&A |

Pacing: slide-times (~55 мин) + retrieval-моменты (~8 мин) + переходы (~7 мин) = 70 + 5 буфер = 75. Уточняется в v2 после Phase 1.

---

## 3. Learning Outcomes

| LO | Формулировка (canon) | Как достигается | Slide coverage |
|---|---|---|---|
| **LO7** | Обосновать выбор архитектуры AI (чат, агент, RAG, API, модель) для задачи | Лестница + матрица + критерии «когда НЕ» + чек-лист; каждый раздел заканчивается «когда НЕ применять» | s04, s08, s13, s17, s24, **s25–s28** (payoff) |
| **LO4** | Применить AI-инструменты для решения типовой аналитической задачи | Микро-применение чек-листа к 2 конкретным задачам (формат Семинара 3) в s28 + ДЗ | **s28** (in-lecture apply), s29 (ДЗ) |

LO4 — не отдельный «инструмент», а *применение аналитической рамки выбора* к задаче (это и есть «типовая аналитическая задача» инженера-архитектора). Согласовано с парным Семинаром 3.

---

## 4. Slide list (v1, s01–s29 monotonic — детализируется в chapter)

### Раздел 0 — Открытие (8 мин)
- **s01 Hook — Moffatt v. Air Canada (3 мин, `case_study`).** Assertion: «Чат-бот выдумал тарифную политику — трибунал (14.02.2024) обязал авиакомпанию платить. Неверная архитектура = юридическая ответственность.» Visual: timeline инцидента + «что было выбрано (генеративный чат) vs что было нужно (детерминированная страница политики)». Retrieval (30 сек): «какую архитектуру вы бы выбрали для "узнать правило тарифа"?»
- **s02 Cover + roadmap (0.5 мин, `cover`).** «Лекция 3. Архитектуры AI-систем: агенты, RAG, API». Roadmap-бар 0–5, gold-маркер «Раздел 0».
- **s03 Recap Lec-2 + мост (1.5 мин, `assertion_visual`).** «Лекция 2 — что внутри одного вызова. Лекция 3 — что строим ВОКРУГ него.» Visual: single-shot inference (из Lec-2 s21) в центре → 4 «обвязки»: контекст/RAG, инструменты, цикл-агент, дообучение.
- **s04 Центральный вопрос + лестница (3 мин, `assertion_visual`).** ЦВ крупно + тизер «лестницы сложности»: код → промпт → RAG → workflow → агент → multi-agent. Якорь: «подниматься на ступень только при необходимости».

### Раздел 1 — Промпт и его границы (9 мин)
- **s05 Дефолт = один вызов (2 мин, `assertion_visual`).** «Самая дешёвая надёжная архитектура — один LLM-вызов с хорошим промптом. Не усложняй без причины.» Когда хватает: знание в модели/промпте, задача одношаговая.
- **s06 Chain-of-thought — паттерн рассуждения (2.5 мин, `case_study`).** Паттерн ЛЕКЦИИ. «Пошаговое рассуждение повышает качество на многошаговых задачах.» Worked example: задача без CoT (неверно) vs с CoT (верно). Retrieval (30 сек).
- **s07 Предел CoT: текст ≠ мысль (2 мин, `case_study`, FAILURE).** «CoT-текст не обязан отражать реальную причину ответа. Claude 3.7 упоминал использованную подсказку лишь в 25% случаев, DeepSeek R1 — 39% (Anthropic, апр 2025); faithfulness падает на трудных задачах.» Урок: человек проверяет *результат*, не self-rationale. `[VFY]`.
- **s08 Context engineering, не prompt-tuning (2.5 мин, `assertion_visual`, JUDGMENT).** «Сдвиг 2025: курировать минимальный высокосигнальный контекст. "Положи всё в окно" ≠ работает — context rot (точность падает с длиной, Chroma 2025).» Когда НЕ нужен RAG: малый стабильный корпус → full-context + prompt caching.

### Раздел 2 — RAG (13 мин)
- **s09 Section divider + что такое RAG (1 мин, `section_divider`).**
- **s10 Принцип RAG (3 мин, `process`).** «retrieval (similarity из Лекции 2) → вставка в контекст → генерация с опорой на источник.» Visual: 4-шаговый конвейер; gold — «ответ с цитатой источника».
- **s11 Когда применять RAG (2.5 мин, `assertion_visual`).** Знание меняется/большое; нужна свежесть + провенанс/цитаты; приватная база.
- **s12 Когда НЕ RAG (2.5 мин, `comparison`, JUDGMENT).** Корпус < ~200k токенов → full-context+caching; фиксированная политика → детерминированный lookup; нет observability retrieval → скрытая бомба.
- **s13 Провал RAG на масштабе (4 мин, `case_study`, FAILURE).** «"Вернул что-то ≠ вернул правильное": legal-AI цитирует неверные прецеденты, medical-RAG смешивает пациентов — retrieval тихо сломался после ~10k док., система всё ещё *что-то* возвращает → модель галлюцинирует "в пробел".» + Air Canada revisited как grounding-провал. Альтернатива: retrieval-eval/observability, structure-aware chunking, hybrid+rerank. GraphRAG — 1 строка (deep-dive в chapter).

### Раздел 3 — Fine-tune vs промпт vs RAG (10 мин)
- **s14 Миф «fine-tuning ушёл» (2.5 мин, `assertion_visual`, JUDGMENT).** «Не ушёл — сузился. 2026: FT = поведение/стиль/формат/политика/дистилляция под латентность, НЕ знания. Знания → RAG+long-context+context-eng.»
- **s15 PEFT вместо full-FT (2 мин, `assertion_visual`).** LoRA/QLoRA — обновляются адаптеры, базовые веса заморожены; DPO (субъективное качество), RFT (однозначные reasoning-задачи).
- **s16 Провал: catastrophic forgetting (3 мин, `case_study`, FAILURE).** «Узкий агрессивный FT деградирует общие способности базовой модели; тяжелее с ростом масштаба. "Дообучить" — не бесплатно, можно сломать работавшее.» Альтернатива: PEFT/RAG; нет eval-петли+версии датасета → откат невозможен → не делай.
- **s17 Критерии: что куда (2.5 мин, `comparison`/decision, JUDGMENT, LO7).** Знание меняется → RAG (не FT). Поведение/тон/формат → FT(PEFT). Гибрид = норма 2026 (RAG для знаний + PEFT для поведения).

### Раздел 4 — API · tools · MCP · агенты + безопасность (18 мин)
- **s18 Section divider + работа через API (1 мин, `section_divider`).**
- **s19 API-слой (2.5 мин, `assertion_visual`).** Structured output (JSON-схема), function calling (LLM выдаёт JSON → внешняя система исполняет → результат назад), prompt caching (до ~90% стоимости / ~85% латентности, Anthropic `[VFY]`).
- **s20 MCP — стандарт подключения инструментов (2 мин, `assertion_visual`).** Anthropic 11/2024; принят OpenAI 03/2025, Google 04/2025; → Linux Foundation. «USB-C для инструментов LLM». Tool use → агент.
- **s21 Agent loop: plan → act → check → iterate (3 мин, `process`).** «Другой AI» лекции. ReAct (Yao 2022) / Reflexion. Visual: цикл с gold-точкой «check» = валидация.
- **s22 Workflow vs Agent (2.5 мин, `comparison`, JUDGMENT).** Anthropic «Building Effective Agents» (12/2024): найди простейшее, иногда агент не нужен. Предсказуемая многошаговая → workflow (фикс. пути). Непредсказуемая + ценность оправдывает 4–15× токенов → агент. Multi-agent дебаты: Cognition «Don't Build Multi-Agents» vs Anthropic (12–13.06.2025).
- **s23 Провалы агентов (3 мин, `case_study`, FAILURE).** #1 агент сжёг $4,200 за 63 ч в петле (нет budget/loop-лимитов); #3 reliability compounding (5×99%→95%, 10→90%); #15 multi-agent хрупкость на зависимых подзадачах. Альтернатива: budget/loop-gates, checkpoints, single-threaded для зависимостей.
- **s24 Безопасность цепочки (4 мин, `case_study`, FAILURE/SECURITY — сквозная тема).** «Кто видит данные: агент→инструмент→внешний API→провайдер.» Prompt injection: GitHub MCP heist (05/2025, #6); кража ключей mcp-remote CVE-2025-6514 (#7); tool poisoning/rug-pull (#8); MCP Inspector RCE CVE-2025-49596 (#9). Retention: NYT v. OpenAI — приказ хранить все логи (#11); граница ZDR Anthropic — third-party/MCP/Files вне ZDR (#12). Правила: least-privilege ключи, изоляция недоверенного контента, human-in-the-loop на write, карта данных по фиче. `[VFY]` метрики/CVE.

### Раздел 5 — Фреймворк решения + финал (12 мин)
- **s25 Лестница сложности (2 мин, `process`, JUDGMENT, LO7).** код(без ИИ) → промпт → RAG/context-eng → workflow → агент → multi-agent. «Подниматься только при необходимости.»
- **s26 Матрица выбора (3 мин, `matrix`, JUDGMENT, LO7).** Оси: объём знания · частота изменений · свежесть/провенанс · стоимость · латентность · аудируемость · риск недетерминизма. 6–7 архитектур × критерии (компактно из decision-criteria §2).
- **s27 Когда НЕ применять ИИ вовсе (2 мин, `assertion_visual`, JUDGMENT).** Детерминированная верифицируемая задача с чёткой спецификацией → обычный код. ИИ добавил бы только недетерминизм+стоимость+латентность+поверхность инъекции. MIT NANDA: ~95% GenAI-пилотов без измеримого ROI — дело в интеграции, не в модели (`[VFY]`, как отчёт).
- **s28 Чек-лист «прежде чем строить» + микро-применение (3 мин, `summary`+exercise, LO7 payoff + LO4).** 8 вопросов (decision-criteria §4). Тут же: класс применяет чек-лист к 2 задачам (формат С3: «поиск в 200 PDF» / «бот техподдержки на корп. базе»). Человек-валидатор: агент делает — человек проверяет результат и факты.
- **s29 Мост к отраслям + ДЗ С3 + Q&A (1.5 мин + ≤5 мин буфер, `summary`+`qa_minimal`).** «Эта рамка — база для Лекций 4–17: в каждой индустрии будем спрашивать "какая архитектура и почему".» ДЗ = Семинар 3. Q&A ≤5 мин.

---

## 5. AI-Failure & Judgment ≥30% (strict-in) — расчёт

Лекция по своей природе — про **суждение и отвержение** неподходящих архитектур (LO7). Strict-in bucket = слайды/минуты, *полностью* про провал+урок+альтернатива / фундаментальное ограничение / критерий «не применять» / сравнение с более правильным инструментом:

- **Полностью in-bucket слайды:** s01, s07, s08, s12, s13, s14, s16, s17, s22, s23, s24, s25, s26, s27, s28 = **15 из 29 ≈ 52%** по слайдам; по минутам ≈ 38–40 из 70 ≈ **~55%**.
- Распределение по артефактам (holistic): chapter — детальные кейсы #1/#4/#5/#11 + сводная таблица ограничений + deep-dive boxes; slides — 15 in-bucket слайдов (assertion-evidence); speech — нарратив #4 (hook), #1 ($4,200), #13/#14 (DPD/Chevrolet — speaker-level), критерии «когда НЕ».
- Waiver НЕ применяется (и не нужен — это спина лекции, не довесок). Цель ≥30% strict-in в КАЖДОМ артефакте перевыполняется по дизайну; methodology-critic проверяет holistic на Phase 3/7/10.

---

## 6. Glossary lock (черновой — финализируется после chapter, Phase 4)

| Канонично | Алиасы (1×) | Запрещено |
|---|---|---|
| архитектура AI-системы | — | «стек», «пайплайн» как синоним |
| промпт | — | prompt |
| few-shot (примеры в промпте) | — | фью-шот |
| Chain-of-thought (пошаговое рассуждение) | CoT (1× в скобках) | «цепочка мыслей» как термин |
| RAG (Retrieval-Augmented Generation) | поиск-дополненная генерация (1×) | «раг» |
| retrieval (поиск релевантного) | — | ретривал |
| fine-tuning (дообучение) | PEFT/LoRA (расшифровка 1×) | файнтюнинг (в chapter) |
| контекст-инжиниринг | — | промпт-инжиниринг (как синоним) |
| tool use / function calling | вызов инструментов (1×) | тулюз |
| MCP (Model Context Protocol) | — | эм-си-пи |
| агент (plan→act→check→iterate) | — | «бот» |
| workflow (предопределённые пути) | — | воркфлоу (в chapter — «рабочий поток»/«сценарий») |
| ZDR (Zero Data Retention) | — | — |
| least-privilege (наименьшие привилегии) | — | — |

Forbidden anglicisms (sync speech Англицизм Pass): пайплайн (→ конвейер), фоллбэк, эдж-кейс, инсайт.

---

## 7. Forbidden additions (No Extra Content Rule, lecture-specific)

Producer-агентам запрещено без explicit approval: формулы attention/трансформера (это Лекция 2); код реальных SDK длиннее 3 строк на слайде; глубокий разбор конкретного vendor-pricing (цифры волатильны → `[VFY]`, не на видимом слое); «Лектору»/«Вы здесь»/subtitle/тайминг на слайдах (кроме roadmap-маркера s02); slide add/delete без user request (REPORT); color-only highlight без текст-маркера; cross-slide мост-текст не запрошенный; footer-tax (источники/«методичка §X»/тайминг видимый студенту) — speaker notes only; глубокий MCP-протокол wire-format (deep-dive только в chapter); полный обзор RFT vs DPO математики (chapter deep-dive box).

---

## 8. Микро-упражнения / retrieval

| Слайд | Тип | Длит. | Активность |
|---|---|---|---|
| s01 | open question | 30 сек | «какая архитектура для "узнать правило тарифа"?» |
| s06 | think pause | 30 сек | предскажи, поможет ли CoT этой задаче |
| s13 | poll | 20 сек | «ваш RAG вернул ответ — как узнать, что он правильный?» |
| s28 | apply (LO4) | 2 мин | чек-лист к 2 задачам формата С3 |

Итого ≈ 5–6 мин, включено в бюджет §2.2.

---

## 9. Свежесть фактов (для fact-checker; freshness enforced)

| Факт | Источник | Cadence | Action |
|---|---|---|---|
| CoT faithfulness 25%/39% | Anthropic, апр 2025 | yearly | OK, cite + `[VFY]` точные числа |
| MCP принят OpenAI 03/2025, Google 04/2025, → Linux Foundation | vendor/press | quarterly | `[VFY-day-of]` |
| MCP adoption (~97M загрузок/мес, ~9.4k серверов) | реестр | quarterly | `[VFY-day-of]`, можно опустить точное |
| CVE-2025-6514 / 49596, GitHub MCP heist даты | AuthZed/Docker/Unit42 | as-is | OK (исторические), cite |
| NYT v. OpenAI retention timeline | Bloomberg Law/NatLawReview | quarterly | `[VFY]` статус |
| Anthropic ZDR-граница (Files/Batch/MCP) | Anthropic live doc | quarterly | `[VFY-day-of]` |
| prompt caching ~90%/85% | Anthropic | quarterly | `[VFY]`, vendor-published |
| catastrophic forgetting механизмы | arXiv 2026-01 preprint | n/a | `[FACT-CHECK]` preprint, framing «исследования показывают» |
| $4,200 agent loop | single-author postmortem 2026-04 | n/a | `[FACT-CHECK]`, framing illustrative |
| MIT NANDA ~95% | отчёт 2025-08 | yearly | cite как отчёт+методология, не закон |

`[VFY-day-of]`: s20, s24-metrics, retention. `[FACT-CHECK]`: catastrophic-forgetting preprint, $4,200, NANDA framing.

---

## 10. Открытые вопросы для USER GATE 0

1. **Hook:** Air Canada (юр./relatable) — ОК? Альтернатива: $4,200 agent loop (engineering/visceral). Рекомендация — Air Canada (рамка «неверная архитектура = последствие», universal).
2. **Slide count:** ~29 — ОК для 75 мин? (lec-02 = 28). Можно ужать Раздел 4 (самый плотный).
3. **Глубина chapter:** подтвердить целевой объём 16–22k слов (выше стандартного red-flag 15k) как явное owner-решение (память `feedback_chapter_depth`) — фиксируем в плане v2.
4. **LO4 реализация:** микро-применение чек-листа в s28 (2 мин) достаточно для «apply», или вынести отдельным слайдом-упражнением?
5. **Multi-agent дебаты** (Cognition vs Anthropic) — оставить как 1 строку в s22 + deep-dive в chapter, или отдельный слайд?

---

## 11. Source-of-truth chain
```
notes/lecture-3-review/2026-05-16/
├── plan-v1.md (ЭТОТ ФАЙЛ — orchestrator draft)
├── phase1-critique/ {methodology-critic.md, reader-text-only.md} (Phase 1)
└── ../final/plan-v2-final.md (после roast + Phase 1 + USER GATE 0)
library/lectures/lec-03/
├── chapter.md [PRIMARY] ← derives from plan v2 (глубокий референс, см. feedback_chapter_depth)
├── deck.yaml + slides/*.md ← derived from chapter
└── speech.md ← derived from chapter + slides
```

## 12. Phase 2 brief (preview, финализируется в v2)
book-editor пишет `library/lectures/lec-03/chapter.md` — **глубокий расширенный референс (ориентир 16–22k слов, red-flag >15k снят owner-решением для этой главы)**: 5 разделов (mirror §2.2) + deep-dive boxes «что не вошло, но важно» (GraphRAG internals, RFT vs DPO, MCP wire-format, ReAct/Reflexion/Plan-Execute, полный multi-agent дебат, vendor retention детали) + «вероятные вопросы аудитории + развёрнутые ответы» в конце разделов. LO7+LO4. Glossary §6, Forbidden §7 — ENFORCED. `[FACT-CHECK]`/`[VFY]` по §9. Tone: инженерно-аналитический, anti-hype, ≥30% strict-in holistic.

**Status:** v1 ready → orchestrator roast → Phase 1 critique (methodology-critic + reader-text-only) → USER GATE 0.

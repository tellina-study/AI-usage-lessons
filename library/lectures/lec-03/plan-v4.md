# Лекция 3 — план v4 (углубление под подготовленную аудиторию)

Issue: #196. База: v6.3 (55 слайдов, глава 44.1k, речь v3.1, EN-дубликат).
Тайминг: 100 мин + явный cut-order (owner decision).

## Change-sets (6 направлений owner-фидбека 2026-09-13)

### 1. Роли / системные промпты
- **REMOVE** `s05a` «Роль в промпте настраивает тон — не точность» (слайд про «роли = только тон»).
  - Тезис «персона ≠ точность» (Zheng et al. 2024) не теряем — сжимаем в 1 строку на `s05c` + в главу §1.2.
- **KEEP** `s05c` «Протокольные роли (system/user/assistant)» — это слайд про системные роли. Усилить графически (system vs user vs assistant, instruction hierarchy, spoofing).

### 2. Форматы промптов (NEW, §1)
- **ADD** `s-fmt` «Форматы промпта: Markdown / XML / JSON — есть ли разница, где, когда, кому, на каких задачах».
  - XML-теги (длинный структурированный контекст, Anthropic-стиль), JSON (машинный I/O, structured output), MD (человекочитаемые инструкции), plain. Матрица «формат → задача → эффект». [VFY-day-of] на конкретику вендоров.
  - Место: после `s05b` (разделители) — естественный переход от delimiters к форматам.

### 3. Типовые задачи (NEW cluster, §1 → мост к архитектурам)
Мини-раздел «Как это выглядит на реальных задачах» после `s08a` (чек-лист). 3 слайда, каждый: постановка → инструмент/архитектура → пример (реальный где есть, иначе явно «иллюстративный»):
- **ADD** `s-task-assistant` — ассистент с инструментами (tool use, когда one-shot, когда агент).
- **ADD** `s-task-tone` — генерация текста заданным тоном / «похоже на человека» (few-shot style, границы, детектируемость).
- **ADD** `s-task-research` — исследовательская задача / deep-research (RAG + агентный цикл + верификация).
- (опц. 4-й `s-task-extract` — структурированное извлечение в JSON; держим в резерве cut-order).

### 4. RAG — сильное расширение (§2: 6 → 12 слайдов)
Держим `s09`(div) / `s-classic-rag` / `s10`(принцип) / `s11`(когда) / `s12`(когда НЕ) / `s13`(провал Air Canada). ADD 6:
- **ADD** `s-rag-hybrid` — гибридный поиск: лексика (BM25) + плотные векторы + слияние (RRF) + reranking (cross-encoder).
- **ADD** `s-rag-stack` — стек: векторные БД (pgvector / Qdrant / Weaviate / Milvus / FAISS) + обвязки (LlamaIndex / LangChain). [VFY-day-of].
- **ADD** `s-rag-elastic` — Elastic и OpenSearch: где классического/семантического поиска достаточно, когда нужна выделенная векторная БД и спец-подходы.
- **ADD** `s-rag-chunk1` — чанкирование: стратегии (fixed / recursive / semantic / sentence-window / parent-document).
- **ADD** `s-rag-chunk2` — чанкирование: overlap, метаданные, как выбрать под задачу (+ провал плохого чанкинга).
- **ADD** `s-rag-design` — как меняется системный дизайн поиска: пайплайн индексации, freshness, eval (recall@k / MRR), latency/стоимость.
- Baseline/counterfactual на всех измеримых числах; anti-hype рамка (вектор ≠ всегда лучше BM25).

### 5. Агенты (§4: 18 → ~18, но плотнее и релевантнее)
- **REMOVE / MERGE (кандидаты — подтвердить на GATE B по PNG):** «слайды-вода» и «странные рассуждения про подумать прежде чем действовать».
  - Кандидаты на рез: `s22e` (presence paradox / «файл-инструкция всё починит» — musing), `s22c` (память — сжать до 1 или в notes).
  - Убрать явные повторы Лекции 1/2 в `s19`/`s20` (structured output / prompt caching уже были в L2 — оставить только L3-специфику: MCP N×M→N+M, trust pivot).
- **ADD** `s-agent-frameworks` — обзор фреймворков: LangGraph / CrewAI / AutoGen(AG2) / OpenAI Agents SDK / Claude Agent SDK / smolagents — когда какой. [VFY-day-of].
- **Workflow / agent / workflow-из-агентов** (несколько слайдов):
  - `s22` reframe → «Когда workflow: 5 паттернов (chaining / routing / parallelization / orchestrator-worker / evaluator-optimizer)» (Anthropic «Building Effective Agents»).
  - **ADD** `s-agent-when` — «Когда агент, а когда workflow из агентов» (открытая vs предсказуемая задача; p^n надёжность — сюда же fold `s22a_multi` или держать рядом).

### 6. Обучение (§3: 7 → 9)
- **ADD** `s-ft-cost` — обучение с нуля vs full-FT vs LoRA/QLoRA (vs промпт/RAG): стоимость / итерации / объём обучающих данных / компьют. Таблица с baseline.
- **ADD** `s-ft-eval` — как измерять результат обучения (нетривиально): бенчмарки / held-out / LLM-as-judge / human eval / task-metrics — и границы применимости каждого по задаче и ресурсам.

## Итоговый счёт слайдов (оценка)
§0=5 · §1=13 · §2=12 · §3=9 · §4≈18 · §5=9 → **≈66 слайдов** (было 55). 100 мин + cut-order.

## Каскад на chapter / speech / EN
- **chapter (RU):** +§1 (форматы + типовые задачи), +§2 (гибрид/стек/elastic/чанкинг/дизайн), +§3 (cost + eval), правки §4 (фреймворки + workflow-таксономия, вырезать L2-recap). 44.1k → ~50–52k. Возможен split part1 (§2 разрастётся) → 6 частей, каждая ≤600 строк.
- **speech:** перегенерировать [sNN] маркеры под новый набор, ≤95 WPM, 100 мин.
- **EN:** после approve RU — полный EN-дубликат под новую структуру (deck.en + slides-en + speech.en + ре-рендер), glossary lock новых терминов (hybrid search, chunking, RRF, LoRA/QLoRA, eval).

## Freshness / research (Phase 0)
Волатильно (2026) → web-research перед письмом: RAG-стек и векторные БД; agent-фреймворки версии; LoRA/QLoRA экономика; Elastic/OpenSearch векторные возможности. Все вендор-числа → [VFY-day-of] + anti-hype.

## Правила (must hold)
classic-base-first (новые слайды — это «AI adds / limits» внутри секций с уже существующим §N.0) · no-superlatives · no-timing/methodology в слайдах · meme-forward (мем на новых плотных слайдах, не переиспользовать шаблоны) · baseline/counterfactual на всех числах · AI-Failure ≥30% strict-in (компенсировать удаление s05a).

## Gates
GATE A (этот план) → Phase 0 research → chapter → **GATE (chapter)** → deck → **GATE (deck)** → speech + EN + рендер → **GATE (final)** → merge + manifest + site.

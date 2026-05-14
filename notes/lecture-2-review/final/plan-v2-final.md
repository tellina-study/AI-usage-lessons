# Лекция 2 «Как работают современные большие модели»
## Plan v2.1 — synthesized from plan v1 + Phase 1 critiques + user constraints

**Issue:** #74
**Branch:** `issue-74-lec-02-llm-internals`
**Длительность:** 75 минут (~70 мин активный контент + ~5 мин Q&A/буфер)
**Аудитория:** 3 курс ИУ6 МГТУ им. Баумана, инженеры-разработчики (универсально)
**Curriculum level:** introductory (модуль 1)
**Дата:** 2026-05-13
**Pipeline phase:** Phase 1 output → input для Phase 2 chapter draft
**Версия:** v2.1 (revision после Phase 1.7 methodology-critic re-check)

**Changelog v2 → v2.1:**
- [P1-N1] Clean renumber slide IDs: s01-s28 monotonic, no gaps (cleaner downstream automation).
- [P1-N2] s28 Q&A wording reconciled: «до 5 минут на вопросы», stays within 5-min buffer.
- [P1-N3] s20 warning row про T=0 softened: «практически детерминирует, микро-вариативность игнорируема».
- [P1-N4] s27 HF Playground tagged `[VERIFY-DAY-OF]` + fallback options + specific model.
- [P1-N5] §2.2 pacing footnote added: section budget = slide times + retrieval (~8 мин) + transitions (~7 мин).
- [P1-9] PARTS reference resolved: «Семинар 12 + Лекция 12» с Lec-1 §3.3 cite (Lec-1 §5.2 vs §3.3 internal contradiction flagged для отдельного issue).

**LO mix (user-locked):** LO1, LO4, LO6, LO7.
**Слайдов:** 28 (s01-s28 monotonic).
**Tone:** объяснительно-инженерный, без «магия LLM».

**Inputs synthesized:**
- `plan-v1.md` — base draft (609 строк).
- `plan-v2-constraints.md` — user-locked scope/title/LO.
- `2026-05-13-phase1-plan-critique/methodology-critic.md` — Phase 1, REVISE.
- `2026-05-13-phase1-plan-critique/reader-text-only.md` — Phase 1, REVISE.
- `2026-05-13-phase1-plan-critique/methodology-critic-v2.md` — Phase 1.7 re-check, REVISE (5 P1 mechanical, fixed in v2.1).
- `library/lectures/lec-01/chapter.md` v3.1.
- `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md`.

---

## 1. Контекст и зависимости

### 1.1 Промис из Лекции 1 §5.3 — выполняется полностью

4 концепта: **токены / эмбеддинги (векторные представления) / механизм внимания (attention) / температура**. Студент после лекции отвечает на 3 «почему»: (1) промпт с ролью лучше пустого, (2) AI плохо считает буквы, (3) один запрос даёт разные ответы.

### 1.2 Cross-cutting frames (user constraints §1, добавлены в v2)

3 frames, каждый = 1 слайд + callback к Лекции 1, **без повтора**:

| Frame | Слайд | Связь с Lec-1 | Время | Тип |
|---|---|---|---|---|
| Local vs cloud trade-off | **s22** | callback §4.2 (без повтора) | 1 мин | `assertion_visual` |
| ML vs LLM decision tree | **s25** | расширяет §1.4 (задача × модальность) | 1.5 мин | `summary` + decision tree |
| Human vs AI («attention ≠ понимание») | **s26** | callback §4.8 Pearl 3 уровня | 1 мин | `assertion_visual` |

### 1.3 Что Лекция 2 НЕ повторяет из Лекции 1

| Тема | Где в Lec-1 | Что Лекция 2 делает |
|---|---|---|
| Трансформер 2017, self-attention high-level | §1.3 | Раскрывает self-attention механически (s13-s17); §1.3 был «чёрный ящик» |
| Scaling laws, GPT-3, ChatGPT 2022 | §1.3 | Не повторяет историю; идёт на уровень внутрь |
| Inductive bias, классификация задача × модальность | §1.4 | Углубляет на ML vs LLM (s25) — расширение, не повтор |
| Модель = stateless inference pipeline | §3.2 | Уточняет: inference = autoregressive token-by-token (s21) |
| Канонические модели (YOLO, Whisper) | §3.2 | Не повторяет; фокус — LLM-семейство |
| Локальные vs облачные | §4.2 | Только callback в s22, без повтора |
| Pearl 3 уровня причинности | §4.8 | Только callback в s26 — «attention не понимает causality» |
| Контекстное окно как ограничение | §3.3.1 | Углубляет: квадратичность стоимости attention (s16) |

### 1.4 Industry context

Лекция 2 — **универсальная** (LLM internals технически нейтральны к индустрии), как Лекция 1 (диагностическая) и Лекция 17 (синтез). Tone — explanatory-engineering.

### 1.5 Курсовая прогрессия (промптинг)

Лекция 1 «промпт = роль + задача + контекст» → **Лекция 2 explains почему работает** (role в attention, T в sampling) → **Семинар 12 + Лекция 12 PARTS frameworks** (Persona / Action / Recipe / Template / Specification), Chain-of-Thought, Few-Shot, Self-Consistency, ReAct (см. Lec-1 chapter §3.3, §5.2 — note: Lec-1 §5.2 говорит «Лекция 12 = Автоматизация и цифровые двойники» что противоречит §3.3 reference на PARTS — **flagged для отдельного issue Lec-1 fix**; Лекция 2 cite только §3.3 phrasing).

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос

> **«Что происходит внутри LLM между моим запросом и ответом — и какие из этих внутренних механизмов меняют, как я её использую?»**

Задаётся в s04. Возвращается: s15 (attention → промпт с ролью), s06-s07 (токенизация → miscount), s19 (T → разные ответы). Payoff — s24 (3 «почему» из Лекции 1 §5.3).

### 2.2 Арка лекции (28 слайдов)

| Этап | Слайды | Time budget | Slide-times sum | Функция |
|------|--------|-------------|-----------------|---------|
| 0. Открытие + recap | s01–s04 | 8 мин | 5 мин | live tokenizer demo (static-first), cover+roadmap, recap Lec-1, центральный вопрос |
| 1. Токенизация | s05–s08 | 11 мин | 9 мин | как модель видит текст; BPE; «strawberry» retrieval; cross-language |
| 2. Эмбеддинги | s09–s12 | 11 мин | 9 мин | пространство смыслов; sentence-similarity; мост к RAG |
| 3. Механизм внимания | s13–s17 | 18 мин | 12.5 мин | attention как distribution; промпт-с-ролью; context window; long-context fails |
| 4. Сэмплинг | s18–s22 | 13 мин | 10.5 мин | distribution → token; температура; 4 ручки API; autoregressive; local vs cloud |
| 5. Заключение | s23–s28 | 9 мин | 9 мин | recap-bridge, payoff (3 «почему»), cross-cutting (ML vs LLM, Human vs AI), ДЗ, мост, Q&A |
| Буфер | — | 5 мин | — | Q&A + technical buffer |
| **Total** | **28 слайдов** | **75 мин** | **55 мин** | |

**Pacing footnote (P1-N5 fix):** Section `Time budget` = slide-times + retrieval moments (~8 мин cumulative по §7) + transitions/lecturer commentary (~7 мин). 55 (slide times) + 8 (retrieval) + 7 (transitions) = 70 мин активного контента + 5 мин буфер = 75 мин total. Math defensible.

---

## 3. Learning Outcomes (user-locked: LO1 + LO4 + LO6 + LO7)

| LO | Формулировка | Slide coverage |
|---|---|---|
| **LO1** | Описать четырёхэтапный конвейер inference LLM (токенизация → эмбеддинг → attention → сэмплинг) и назвать назначение каждого этапа | s03, s05, s09, s13, s18, s21, s23 |
| **LO4** | Подобрать параметры запроса (`temperature`, `top_p`, `max_tokens`, `system prompt`) под конкретный сценарий | s19 (T), **s20** (расширен: 4 ручки API), s27 (ДЗ playground) |
| **LO6** | Назвать минимум 3 ограничения LLM-инференса от архитектуры (**слепота к буквам**, конечное контекстное окно, стохастичность сэмплинга), привести инженерный кейс по каждому | s06 (буквы), s07 (cross-lang cost / strawberry), s17 (long-context fails), s26 (human vs AI) |
| **LO7** | Обосновать 3 «почему» через механизм: роль → attention, буквы → tokenizer, разные ответы → sampling при T>0 | s15 (роль), s06-s07 (буквы), s19 (T), **s24** (payoff card) |

**Терминология ограничений (P1-3 fix):** «слепота к буквам» (рабочий термин) ИЛИ «subword-агрегация» — НЕ «миопия токенизации» (insider). Locked в §5 glossary.

---

## 4. Slide list (28 слайдов, s01-s28 monotonic, P1-N1 fixed)

### Раздел 0. Открытие (8 мин, 4 слайда)

#### s01 — Live tokenizer demo (2 мин)
- **Тип:** `live_demo` с static fallback
- **Assertion:** «Модель видит ваш запрос не буквами и не словами — а токенами»
- **Visual primary:** static screenshot Tiktokenizer (4 примера: `cat`=1, `tokenization`=2, `клубника`=4, `🍓`=3 в `gpt-4o`-токенизаторе). **Primary = static**, live demo — optional «если интернет работает».
- **LO:** LO1.
- **Pre-flight:** screenshots в `assets/`, проверены за день до лекции.

#### s02 — Cover + roadmap merged (0.5 мин)
- **Тип:** `cover` с roadmap-баром внизу
- **Assertion:** «Лекция 2. Как работают современные большие модели»
- **Visual:** декоративная «02», hero motif, 5 пронумерованных микро-карточек roadmap внизу (0 / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал) с gold-маркером «Вы здесь — Раздел 0».

#### s03 — Recap Лекции 1 (1.5 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Сегодня углубляем слой "модель" из четырёх слоёв Лекции 1»
- **Visual:** маленькая копия nested layers из Lec-1 deck с подсветкой нижнего слоя «Модель» в gold. Справа bullet: «что мы знаем (модель = stateless inference из §3.2)» → «что узнаем сегодня (что внутри inference)».
- **Reader gap fix:** explicit bridge «помните pipeline preprocess → model → postprocess из Лекции 1 §3.2; сегодня — что внутри `model`».

#### s04 — Центральный вопрос (1 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Главный вопрос: что внутри LLM меняет то, как мы её используем?»
- **Visual:** центральный вопрос крупно + 3 промиса-якоря по нижнему краю:
  1. Почему промпт с ролью работает лучше? (Раздел 3)
  2. Почему AI плохо считает буквы? (Раздел 1)
  3. Почему один и тот же запрос даёт разные ответы? (Раздел 4)
- 3 промиса повторяются один раз в s24.

---

### Раздел 1. Токенизация (11 мин, 4 слайда)

#### s05 — Что такое токен (2 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Токен — id из словаря модели. Не буква и не слово; статистически частая подпоследовательность»
- **Visual:** 3 примера с разметкой: `cat` = `[cat]` (1 токен / 1 id); `tokenization` = `[token][ization]`; `клубника` = `[кл][уб][ни][ка]`. Внизу: «в среднем 1 токен ≈ 4 символа в EN ≈ 2 в RU».
- **Reader P0 fix:** explicit «токен — это id из словаря (число); мы пишем его в кавычках для удобства».
- **Inline note (v1 s09 merged here):** «То же про числа: `1234567` режется непредсказуемо. Для арифметики — Code Interpreter / Python, не чистый inference».
- **Inline poll (15 сек):** «как бы вы разрезали `сильнее` — 1, 2 или 3 токена? Почему?»
- **LO:** LO1.

#### s06 — BPE как компромисс (2 мин)
- **Тип:** `comparison` (без 3-step trace, P1-2 fix)
- **Assertion:** «BPE — компромисс между алфавитом и словарём; словарь строится один раз перед обучением»
- **Visual:** Before/After: `low / lower / newest / widest` → результат BPE-словаря: `low / er / new / est / wid`. БЕЗ пошаговой итерации.
- **Reader P0 fix:** explicit «BPE-словарь строится один раз на корпусе перед обучением модели. В inference токенизация — это lookup готовых merge-rules, не runtime-вычисление».
- **Note:** «Современные альтернативы: WordPiece (BERT), SentencePiece (LLaMA, T5). Различия — глубже на Лекции 17 / доп.чтение».
- **Speaker note:** trade-off «маленький словарь = много токенов / большой = больше памяти».

#### s07 — Почему AI плохо считает буквы (3 мин с retrieval)
- **Тип:** `case_study`
- **Assertion:** «AI ошибается в "сколько 'r' в strawberry" — потому что слова не из букв, а из 2-3 токенов»
- **Visual:** слева `strawberry` → `[straw][berry]` (модель видит 2 токена); справа 3 практических следствия (подсчёт букв, опечатки, регистр).
- **Retrieval moment** (1 мин): студенты на телефонах. **CRITICAL: pre-test day-of (P1-7).**
  - Если все 3 топовых модели (ChatGPT-5, Claude 4.7, GPT-5) правильно отвечают «3 r» — replace example: «сколько `о` в "методология"» / «зашифруй ROT-13 "strawberry"» / «переверни 'methodology' посимвольно».
  - Lecturer brief — explicit `[VERIFY-DAY-OF]` tag.

#### s08 — Cross-language unfairness (2 мин)
- **Тип:** `comparison`
- **Assertion:** «Один и тот же текст по-русски стоит в 2× дороже, чем по-английски»
- **Visual:** bar chart токены/символ — EN ~0.25, RU ~0.5, ZH ~0.8, Code(Python) ~0.4.
- **Gold callout:** «API-стоимость в RU ≈ 2× от EN. Инженерный вывод: для batch — переводить в EN, если допустимо».
- **Source:** OpenAI tokenizer benchmarks; **verify-on-day** (cadence: quarterly).

---

### Раздел 2. Эмбеддинги (11 мин, 4 слайда)

#### s09 — Что такое эмбеддинг (2 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Каждому токену в памяти модели сопоставлен вектор; он выучен на тренировке и затем фиксирован»
- **Visual:** Схема `[кот]` → lookup-arrow → вектор `[0.21, -0.45, 0.88, ..., 0.13]` (4-6 размерностей с многоточием).
- **Reader P0 fix:** explicit «откуда берётся вектор — lookup из learned embedding table». Mini-callout: «text-embedding-3-small 1536 dim; text-embedding-3-large 3072 dim; внутренний эмбеддинг GPT-4 — 12288 dim (по утечкам, `[FACT-CHECK]`)».
- **LO:** LO1.

#### s10 — Sentence similarity на современных embeddings (3 мин)
- **Тип:** `case_study` (P1-5 fix — replace Word2Vec king-queen → modern)
- **Assertion:** «Близость в пространстве эмбеддингов = семантическая близость; в 2026 это работает на уровне предложений»
- **Visual:** 5 коротких предложений → cosine similarity heatmap (или таблица 5×5):
  1. «Как настроить SSL»
  2. «Установка HTTPS-сертификата»
  3. «Деплой React-компонента»
  4. «Сборка React-приложения»
  5. «Рецепт борща»
  - Видно: 1↔2 ≈ 0.85 (синонимы домена), 3↔4 ≈ 0.78, что-то↔борщ ≈ 0.05-0.15 (разные домены). **Числа illustrative `[FACT-CHECK]` — empirically verify на target embedding model перед chapter draft.**
- **Speaker note:** Word2Vec king-queen (Mikolov 2013) — историческая отметка в 1 предложении, без отдельного слайда.
- **Inline disclaimer:** «cosine similarity — мера угла между векторами; ближе к 1 = более похожи».

#### s11 — Что даёт эмбеддинг (2 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «3 применения: similarity, clustering, search»
- **Visual:** 3 motif карточки: Similarity (cosine), Clustering (k-means — inline «алгоритм кластеризации»), Search (semantic).
- **Gold на Search:** «Основа RAG — Лекция 3».

#### s12 — Semantic search vs full-text (2 мин)
- **Тип:** `case_study`
- **Assertion:** «Semantic search находит то, что full-text пропустит»
- **Visual:** запрос `"клубника"` — full-text находит только слово, semantic находит «strawberry», «ягода», «лесная земляника», cross-lang.
- **Bridge to Лекция 3:** «base layer RAG; реализация — Лекция 3».

---

### Раздел 3. Механизм внимания (18 мин, 5 слайдов)

#### s13 — Section divider Раздел 3 (0.5 мин)
- **Тип:** `section_divider`
- **Assertion:** «Раздел 3 — Механизм внимания: как модель решает, что важно сейчас»
- **Visual:** Большое «Раздел 3» + roadmap-bar с gold-маркером «Вы здесь».
- **Note:** Single section divider в лекции (для самого плотного раздела). Разделы 1/2/4/5 переходят через title.

#### s14 — Что такое attention (3 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Attention выдаёт распределение весов на все токены контекста (сумма = 1) — какие токены важны сейчас»
- **Visual:** метафора «фонарик в тёмной комнате» + распределение весов внизу (bar chart по токенам, сумма = 1).
- **Reader P0 fix:** explicit «выдаёт распределение, сумма = 1, толстая стрелка = больший вес».
- **Без формул.** No Q/K/V terminology (forbidden §6.2).
- **Metaphor lock (P1-4 fix):** «фонарик» — единственная метафора. «Магнит» вычеркнут.
- **Speaker note:** «attention в реальной модели — ~64-128 параллельных голов в каждом слое; детали — Лекция 17 / доп.чтение». (multi-head упомянут только здесь, без отдельного слайда.)

#### s15 — Worked example + role-effect merged (5 мин с retrieval)
- **Тип:** `case_study` (v1 s17+s18 merged, Q5 fix)
- **Part A (2 мин):** worked example. Предложение `"Кот съел мышь, потому что она была голодна"`. Над `она` — стрелки разной толщины к `мышь` (толстая), `была` (средняя), `голодна` (тонкая).
- **Disclaimer над visual (P1-12 fix):** «упрощение: реальный attention map содержит сотни связей; здесь показаны 3 сильнейших. Модель не делает грамматический разбор — она статистически смотрит».
- **Retrieval (30 сек):** «куда смотрит модель в "Программа упала, потому что **она** забыла обработать null"?»
- **Part B (2.5 мин):** role-effect. Два контраста side-by-side:
  - Без роли: `"Объясни асинхронность"` → generic ответ.
  - С ролью: `"Ты эксперт по Python. Объясни асинхронность джуниору."` → role-токены подсвечены ярче (метафора «фонарик»).
- **Softer phrasing (P1-10 fix):** «На уровне attention мы видим, что role-токены имеют более высокий вес. Это упрощение — альтернативно объясняется через in-context steering».
- **Gold callout:** «1-е из 3 "почему" Лекции 1 §5.3».
- **Speaker note:** альтернативные механизмы (in-context steering, RLHF role-priming) — упомянуть, что explanation не settled science.

#### s16 — Контекстное окно (2 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «Контекстное окно — физический предел того, сколько модель "видит" одновременно»
- **Visual:** bar chart progression (P1-8 fix — **только 3 ключевых точки**):
  - GPT-3.5 (2022): 4k
  - Claude 3.5 (2024): 200k
  - Claude 4.7 (2026): 1M
- **Gold callout:** «стоимость attention растёт квадратично от длины контекста. 1M ≈ 16× дороже 100k».
- **Tag:** `[VERIFY-ON-LECTURE-DAY]` — все 3 точки.
- **Fallback speaker note:** «если на лекции цифры устарели — ОК сказать "уже больше; порядок 100k→1M остался, и квадратичная стоимость не зависит от точных цифр"».

#### s17 — Long-context fails (2 мин)
- **Тип:** `case_study`
- **Assertion:** «Большое контекстное окно ≠ хорошее использование контекста»
- **Visual:** U-shape график accuracy vs позиция факта в 100k контексте (~70-80% начало, провал до 30% середина, ~70-80% конец).
- **Source:** Liu et al. 2023 (arXiv:2307.03172) — verified, OK.
- **Gold callout:** «инженерный вывод: важное — в начало или в конец промпта, не в середину».

---

### Раздел 4. Сэмплинг (13 мин, 5 слайдов)

#### s18 — Распределение вероятностей (2.5 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «На каждом шаге модель выдаёт распределение вероятностей на ВСЕ токены словаря — затем выбирает один»
- **Visual:** Bar chart distribution для 10 кандидат-токенов после фразы «Сегодня я съел ...»:
  - `яблоко` 0.32, `пиццу` 0.19, `салат` 0.14, `булочку` 0.11, `огурец` 0.08, остальные < 0.05. **Числа illustrative**.
- Стрелка — «выбор» одного токена.

#### s19 — Температура + краткое top-p/k (3 мин)
- **Тип:** `case_study` (v1 s23 + s24 merged, Q7 fix)
- **Assertion:** «Температура — насколько "острым" будет выбор. T=0: argmax. T=1: стандарт. T=2: хаос»
- **Visual:** 3 копии distribution из s18 с разной T (T=0 детерминизм на `яблоко`; T=0.7 умеренное; T=2.0 почти плоское).
- **Inline disclaimer (Reader P1):** «argmax — выбор токена с самой высокой вероятностью».
- **Bottom line:** «Есть также **top-p (nucleus)** и **top-k** — альтернативные способы отрезать "хвост" редких токенов. На практике для start достаточно настраивать T; top-p/k — для тонкой настройки. См. ДЗ s27».
- **Gold callout:** «3-е из 3 "почему" Лекции 1 §5.3».
- **Live comparison (в составе 3 мин):** лектор показывает T=0 vs T=1.5 на одном промпте.

#### s20 — 4 ручки API (LO4 teaching slide, 2 мин)
- **Тип:** `summary` (но teaching, не recap; P0-3 fix)
- **Assertion:** «4 параметра под задачу: `temperature`, `top_p`, `max_tokens`, `system prompt`»
- **Visual:** Таблица 5×5 (заголовки + 4 строки сценариев):

| Сценарий | T | top_p | max_tokens | system_prompt |
|---|---|---|---|---|
| Классификация / точное извлечение | 0 | — | 50-200 | минимальный, схема |
| Кодогенерация | 0.2-0.3 | 0.9 | 1000+ | роль + контекст репо |
| Чат-объяснение | 0.7 | 0.9 | 500-1000 | роль + аудитория |
| Творческое письмо | 0.9-1.2 | 0.95 | 2000+ | роль + стиль |

- **Softened warning row (P1-N3 fix):** «`T=0` практически детерминирует выбор; в production может быть микро-вариативность из-за batching — для большинства задач игнорируема» (вместо raw «T=0 ≠ детерминизм»).
- **LO:** LO4 явно — это **teaching slide**, не recap. Каждая строка — actionable comb.

#### s21 — Авторегрессионная генерация (2 мин)
- **Тип:** `process`
- **Assertion:** «Loop: предсказали токен → добавили в контекст → предсказываем следующий»
- **Visual:** замкнутый цикл 5 шагов: текущий контекст → forward pass через слои → distribution → сэмплинг → новый токен добавлен → возврат к 1.
- **Inline note (Reader P2):** «forward pass = всё что мы проходили в s05-s19 (токенизация → эмбеддинг → attention → distribution) одним проходом».
- **Connection to Lec-1:** «уточнение к §3.2 (модель = stateless inference). Каждый шаг — stateless; "разговор" живёт в контексте».
- **Glossary lock (P1-11):** «авторегрессионный» canonical (не «авторегрессивный»). **VERIFY** перед chapter draft.

#### s22 — Local vs cloud (1 мин) — cross-cutting
- **Тип:** `assertion_visual` (P0-1 fix)
- **Assertion:** «Inference loop одинаков локально и в облаке — но размер модели определяет качество»
- **Visual:** двухколоночный compare:
  - **Local (Ollama, llama.cpp):** малая модель (1B-13B; Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B), приватность данных, медленнее на consumer hardware, ограниченный context.
  - **Cloud (OpenAI, Anthropic, Yandex, GigaChat):** большая модель (200B+), задержка 200-500ms, оплата за токены, данные через API.
- **Callback:** «глубже про trade-off — Лекция 1 §4.2. Сегодня — architecture одинакова, отличается размер и среда».

---

### Раздел 5. Заключение (9 мин, 6 слайдов)

#### s23 — Recap-bridge (1 мин)
- **Тип:** `assertion_visual`
- **Assertion:** «4 этапа inference сложились в pipeline»
- **Visual:** Pipeline 4-stage: Токенизация → Эмбеддинг → Attention → Сэмплинг. Каждый этап с одной строкой определения.
- **LO:** LO1 — final recap.

#### s24 — 3 ответа на 3 «почему» (2 мин) — payoff
- **Тип:** `summary`
- **Assertion:** «3 промиса Лекции 1 — 3 ответа из Лекции 2»
- **Visual:** 3 takeaway карточки:
  1. **Почему промпт с ролью лучше?** → На уровне attention role-токены получают более высокий вес — модель опирается на них при выборе следующих (softer P1-10).
  2. **Почему AI плохо считает буквы?** → Токенизатор объединяет несколько букв в один токен; модель не видит букв (s05-s07).
  3. **Почему один и тот же запрос даёт разные ответы?** → Сэмплинг из distribution при T > 0 (s18-s19).
- **LO:** LO7 — explicit payoff.

#### s25 — ML vs LLM decision tree (1.5 мин) — cross-cutting
- **Тип:** `summary` + decision tree (P0-1 fix)
- **Assertion:** «LLM — не всегда правильный инструмент. Decision tree: когда не LLM»
- **Visual:** простой decision tree (3-4 ветки):
  - Задача = классификация на маленьком фиксированном наборе категорий? → классический ML (логистическая регрессия / xgboost), не LLM.
  - Нужна интерпретируемость (regulated industry)? → классика / правила, не LLM.
  - Время отклика < 100ms критично? → специализированная маленькая модель, не LLM.
  - Иначе → LLM подходит (chat, RAG, generation).
- **Callback:** «расширяет ось задача × модальность из Лекции 1 §1.4».
- **Lecturer note:** «это decision tree верхнего уровня; реальный выбор глубже — Лекции 4-12 по индустриям».

#### s26 — Human vs AI: attention ≠ понимание (1 мин) — cross-cutting
- **Тип:** `assertion_visual` (P0-1 fix)
- **Assertion:** «Attention статистически смотрит на токены — не понимает причинности. Это объясняет, почему AI на уровне 1 Пёрла (см. Лекция 1 §4.8)»
- **Visual:** Side-by-side:
  - **Человек:** «X произошло, потому что Y» — модель причинности (Pearl уровни 2-3).
  - **AI:** «X следует за Y в данных» — статистическая корреляция (Pearl уровень 1).
- **Callback:** «Лекция 1 §4.8 разбирала 3 уровня Пёрла. Теперь понимаем механизм: attention считает веса в данных, не строит каузальный граф».
- **Tone:** factual, без alarmism.

#### s27 — Задание к Семинару 2 (2 мин)
- **Тип:** `summary` (homework)
- **Assertion:** «Принесите 1 запрос × 3 температуры × 3 запуска × анализ»
- **Visual:** 3-шаговая инструкция:
  1. Возьмите типовую задачу (1 запрос ChatGPT/Claude).
  2. Запустите её **в playground**: T=0, T=0.7, T=1.5 — **по 3 запуска каждой T** для оценки variance.
  3. Принесите одностраничный разбор: что изменилось / осталось / какую T для production.
- **Playground (P1-N4 fix, `[VERIFY-DAY-OF]`):**
  - **Primary:** Hugging Face Inference Playground (free, T slider), модель `Meta-Llama-3-8B-Instruct` для всех студентов apples-to-apples.
  - **Fallback 1:** Together.ai playground (free tier).
  - **Fallback 2:** Ollama локально с llama3 (если HF недоступен).
  - **NOT:** ChatGPT free / Claude.ai (нет T slider в UI).
  - Lecturer brief — verify playground availability за день до лекции.
- **Бонусный челлендж:** «сколько 'р' в "строгая регуляризация"» — разные модели ответят разно; объясните через s05-s07.

#### s28 — Что в Лекции 3 + Q&A (1.5 мин contents + ≤5 мин Q&A в буфере)
- **Тип:** `summary` + `qa_minimal`
- **Assertion:** «Лекция 3: "Агенты, RAG, API: как AI выходит за пределы чата"»
- **Visual:** 4 концепта Лекции 3 (с inline disclaimer'ами):
  - **RAG (Retrieval-Augmented Generation)** — embedding similarity (s10-s12) + LLM → ответ из вашей базы.
  - **Tools / Function calling** — LLM генерирует **специальный JSON**, который выполняет внешняя система; результат возвращается модели.
  - **MCP (Model Context Protocol)** — открытый стандарт подключения инструментов к LLM (Anthropic, 2024; см. Lec-1 §2.2).
  - **Agent loop** — act (LLM решает действие) → observe (видит результат) → reflect (решает что дальше).
- **Bridge:** «все 4 надстраиваются над single-shot inference из s21. Multimodal embeddings (CLIP) — там же в RAG».
- **Q&A reconciled (P1-N2 fix):** «До 5 минут на вопросы в зале. Дополнительные — приносите на Семинар 2 / e-mail». Q&A fits в 5-min буфер.

---

## 5. Glossary lock (15 терминов, terminology-only mode enforced)

| Канонично | Допустимые алиасы | Запрещённое | Источник |
|---|---|---|---|
| токен | — | tokens, единица | новый |
| токенизация | — | tokenization (англ.) | новый |
| BPE (Byte-Pair Encoding) | BPE-токенизация | — | новый (расшифровка строго 1× в chapter) |
| эмбеддинг | «векторное представление» (1×) | embedding (англ.) | новый |
| семантическое сходство | similarity (1× в скобках) | — | новый |
| cosine similarity | — | косинусная близость (в slides) | новый — locked как канонический в s10 (англицизм допустим в technical inference context) |
| **механизм внимания** | **внимание** (1× после introduction); attention (1× в скобках при intro) | внимательность | Lec-1 §1.3 |
| контекстное окно | — | context window | Lec-1 §3.3.1 |
| in-context (текущий контекст в цикле inference) | — | — | новый — disambiguation от «контекстное окно» (size limit) |
| сэмплинг | «выбор следующего токена» (1×) | sampling | новый |
| температура | — | temperature | Lec-1 §5.3 |
| top-p (nucleus sampling) | — | — | новый |
| top-k | — | — | новый |
| `max_tokens` | — | — | новый |
| **авторегрессионный** (LOCKED) | autoregressive (1× в скобках) | авторегрессивный; авто-регрессионный | **VERIFY** перед chapter draft (P1-11) |
| распределение вероятностей | — | probability distribution | новый |
| **слепота к буквам** (рабочий) | subword-агрегация | «миопия токенизации» | P1-3 fix (NOT canonical в литературе) |

**Из Лекции 1 (используем без переопределения):** LLM, трансформер, self-attention, scaling laws, few-shot, RAG, MCP (1 предложение определения в s28).

**Forbidden anglicisms (sync с speech-writer Англицизм Cleanup Pass):** workflow, pipeline (использовать «конвейер»), edge case, fallback, инсайт.

---

## 6. Forbidden additions (No Extra Content Rule, lecture-specific)

Producer-агентам (book-editor, presentation-designer, speech-writer) **запрещено** добавлять без явного approval:

1. **Формулы attention** (softmax(QK^T/√d) V) — описываем словами и распределением.
2. **Матрицы Q/K/V как термины** — слишком тяжело для introductory.
3. **Архитектурная диаграмма transformer block** (skip connections, layer norm, FFN) — overhead.
4. **Глубокий разбор позиционного кодирования** — упоминание в 1 предложении максимум.
5. **Обзор pretraining vs fine-tuning vs RLHF** — другая лекция.
6. **Сравнение CNN vs RNN vs Transformer** — мы только трансформеры.
7. **Karpathy-style "let's build a mini-GPT"** — другой формат.
8. **Footer-tax** (источники, ссылки, «методичка §X», тайминг видимый студенту) — speaker notes only.
9. **«Вы здесь» / «Лектору» / subtitles** на слайдах (кроме s02 roadmap-маркера) — Pre-USER-GATE walkthrough это ловит.
10. **Слайд-deletion / addition без user request** — REPORT orchestrator, не apply.
11. **Multi-head attention deep-dive** (s14 speaker note only, 1 предложение).
12. **Word2Vec king-queen как central visual** — historical note в s10 speaker only.
13. **Pearl 3 уровня deep dive** — только callback в s26, 1 предложение.
14. **Color-only highlight без text marker** — single mechanism per signal.
15. **Decorative SVG/icons без semantic role** — visual noise.
16. **Cross-slide bridge text не запрошенный** («как мы видели на s10», «вспомним»).
17. **«Section-NN» footer markers** на слайдах.

---

## 7. Микро-упражнения и retrieval moments

| Слайд | Тип | Длительность | Что делают студенты |
|---|---|---|---|
| s01 | static demo + open question | в составе 2 мин | смотрят на 4 примера; «как разрезалось бы X?» |
| s05 | inline poll | 15 сек | «как бы вы разрезали `сильнее` — 1, 2 или 3 токена? Почему?» |
| s07 | live attempt | 1 мин | телефоны: «сколько 'r' в strawberry?» (`[VERIFY-DAY-OF]` required) |
| s15 | think pause | 30 сек | «куда смотрит модель в "Программа упала, потому что она забыла обработать null"?» |
| s19 | live comparison | в составе 3 мин | лектор показывает T=0 vs T=1.5 на одном промпте |

**Итого:** 5 интерактивных моментов, ≈8 мин cumulative — included в section time budgets §2.2.

---

## 8. Связь с учебной программой

### 8.1 Прогрессия промптинга

Лекция 1 «промпт = роль + задача + контекст» → **Лекция 2 explains почему**: role в attention (s15), T в sampling (s19), 4 ручки (s20) → **Семинар 12 + Лекция 12 PARTS frameworks** (см. Lec-1 chapter §3.3).

### 8.2 Сквозные принципы (нейтральный tone, P1-6 fix)

- ✅ **«От знакомого к незнакомому»** — Лекция 2 объясняет «почему», что студенты уже сталкивались.
- ✅ **«Микро-упражнения на каждой лекции»** — 5 моментов.
- ✅ **«Ошибки AI — не баг, а фича обучения»** — `strawberry`-miscount + ДЗ с T=1.5.
- (REMOVED:) «промптинг — сквозной навык» phrasing — заменено на нейтральное «промпт-параметры (роль, температура) разбираются на уровне механики; систематизация — Лекция 12 / Семинар 12 PARTS».

### 8.3 Industries

Лекция 2 — **универсальная** (не привязана к индустрии). Как Лекция 1 (диагностическая) и Лекция 17 (синтез сквозных паттернов).

---

## 9. Свежесть фактов (для fact-checker, freshness-check enforced)

| Факт | Источник | Cadence | Risk | Action |
|---|---|---|---|---|
| GPT-4 vocab ~100k токенов | OpenAI `cl100k_base` | yearly+ | low | OK |
| BPE словарь LLaMA — SentencePiece | Meta docs | yearly+ | low | OK |
| `text-embedding-3-small` 1536 dim | OpenAI API docs | yearly+ | low | OK |
| `text-embedding-3-large` 3072 dim | OpenAI API docs | yearly+ | low | OK |
| GPT-4 internal emb 12288 dim | leak | high | mark `[FACT-CHECK]` | softer phrasing |
| Claude 4.7 1M context | Lec-1 §1.3 | quarterly | medium | already cited |
| GPT-3.5 4k context | OpenAI archive | yearly+ | low | OK |
| Claude 3.5 200k context | Anthropic docs | yearly+ | low | OK |
| RU vs EN tokenization 2× | OpenAI benchmarks | quarterly | medium | empirical verify |
| "Lost in the middle" Liu et al. 2023 | arXiv: 2307.03172 | yearly+ | low | OK |
| `strawberry` miscount works for top-3 models | empirical | weekly | high | **day-of pre-test** |
| Cosine similarity numbers (s10 example) | empirical | yearly+ | low | derive empirically |
| HF Inference Playground availability + free Llama-3-8B-Instruct | HuggingFace platform | quarterly | medium | **day-of verify** + fallback Together.ai / Ollama |
| Context window timeline (s16, 3 points) | various | quarterly | medium | **day-of verify** + fallback narrative |

**Action для fact-checker:** verify week-of перед production lecture; `[FACT-CHECK]` для unverified specifics; **day-of pre-test для s07 / s16 / s27 playground**.

---

## 10. Closed (decided) open questions из v1 §15

| # v1 | Q | v2.1 decision | Reasoning |
|---|---|---|---|
| Q1 LO mix | LO6 add? | LO1+LO4+LO6+LO7 (user-locked) | user constraint §3 |
| Q2 Hook | tokenizer demo vs CV callback? | tokenizer demo, static-first | critic P0-5 + user lean |
| Q3 Word2Vec | mix или replace? | **REPLACE only modern** (sentence-similarity) | methodology P1-5 strong reasoning |
| Q4 s14 multimodal | 2 vs 1 мин? | **CUT entirely**, 1 строка в s28 | methodology Q4 + budget |
| Q5 s17+s18 | merge? | **MERGE** в s15 | both critics + user lean |
| Q6 s21 long-context | keep? | **KEEP**, 2 мин max, → s17 | both critics |
| Q7 s24 top-p/k | merge? | **MERGE** в s19 | both critics + user lean |
| Q8 Tone | explanatory vs wow? | **explanatory-engineering** | Lec-1 alignment |
| Q9 Slide count | 31 → 28-30? | **28** final | both critics |
| Q10 ML vs LLM placement | s30? | **s25 between s24 and s26** | narrative pivot после payoff |

---

## 11. Source-of-truth chain

```
notes/lecture-2-review/
├── plan-v1.md (initial draft)
├── plan-v2-constraints.md (user-locked, 2026-05-13)
├── 2026-05-13-phase1-plan-critique/
│   ├── methodology-critic.md (Phase 1)
│   ├── reader-text-only.md (Phase 1)
│   └── methodology-critic-v2.md (Phase 1.7 re-check)
├── final/
│   └── plan-v2-final.md (THIS FILE, v2.1, ready for chapter draft)

library/lectures/lec-02/
├── chapter.md (Phase 2-4, ~10-12k слов) [PRIMARY] ← derives from this plan
├── deck.yaml + slides/*.md (Phase 5-6) ← derived from chapter
└── speech.md (Phase 9-10, ~5k слов) ← derived from chapter + slides
```

**При conflict** chapter ↔ slides/speech — fix downstream (правило `tools/lecture-production/README.md` §1).

**Slide ID map:** s01-s28 monotonic, no gaps (P1-N1 fixed).

---

## 12. Phase 2 brief для book-editor (next step)

**Goal:** Написать `library/lectures/lec-02/chapter.md` ~8-12k слов, academic tone, derived from this plan v2.1.

**Constraints:**
- Title: «Глава 2. Как работают современные большие модели»
- LO: LO1+LO4+LO6+LO7 (см. §3)
- Structure: 5 разделов (mirror арки §2.2): Введение/Цели → Раздел 1 Токенизация → Раздел 2 Эмбеддинги → Раздел 3 Внимание → Раздел 4 Сэмплинг → Раздел 5 Заключение (5 разделов в chapter + Введение + Учебные цели).
- Cross-reference Lec-1 §3.2 / §3.3.1 / §4.2 / §4.8 / §5.3 без повтора (см. §1.3 этого плана).
- Glossary lock §5 этого плана — ENFORCED.
- Forbidden additions §6 этого плана — ENFORCED.
- Self-check вопросы в конце каждого раздела (retrieval practice).
- Speaker-notes markers `[for-slide-sNN]` на параграфах, которые будут основой для slide speaker notes. **Slide IDs s01-s28 monotonic.**
- Mark unverified specifics с `[FACT-CHECK]` — см. §9 freshness table для enumerated items.
- Tone: explanatory-engineering, не «магия LLM», не triumphalist.

**Critic readiness:**
После draft — Phase 3 (3 critics parallel: methodology-critic + fact-checker + reader-simulator mode=text-only).

---

**Конец plan v2.1.** Status: ready for Pre-USER-GATE walkthrough → USER GATE plan approval → Phase 2 chapter draft.

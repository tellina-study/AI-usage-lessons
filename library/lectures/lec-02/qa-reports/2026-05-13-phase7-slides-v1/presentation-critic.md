# Presentation-Critic Report on Slides Лекции 2 v1.0 — 2026-05-13

VERDICT: REVISE

## Summary

Deck Лекции 2 (28 слайдов, 75 мин, introductory) — содержательно сильная: hook→cover→recap→agenda, чёткий 4-stage pipeline (токенизация → эмбеддинг → внимание → сэмплинг), хорошие callbacks к Лекции 1 (s03, s22, s23, s26), payoff на 3 вопроса (s24). Палитра Ocean выдержана, gold-акцент используется системно (как «лидер» на s08 / «pivot» на s17 / «выбранный токен» на s18). Однако deck **не готов к показу**: (1) высокая визуальная плотность на ~10 слайдах приводит к font-size <14pt на body — projector-illegible с 5-го ряда; (2) на 2 слайдах студенту видны placeholder-маркеры `[VERIFY-DAY-OF]` (s16, s27) — методический эпиграф для лектора попал в видимую зону; (3) несколько метафор/иллюстраций (s14 «фонарик в тёмной комнате» с декоративными точками) добавляют визуальную нагрузку без новой информации; (4) overflow в Top-5 box на s18 (`Σ = 1` обрезан рамкой); (5) Лекция 2 — introductory, но s10 cosine similarity heatmap + s17 Lost-in-the-middle U-curve + s18 P(next token) bar chart + s19 3-температуры триптих + s20 4-ручки matrix создают cognitive overload (4 концептуально разные диаграммы в 30 минут раздела «Внимание+Сэмплинг»). Найдено **7 P1 → counter-check: REVISE**.

Сильные слайды: s01 (live demo), s02 (cover), s03 (recap layers), s05 (token definition cards), s06 (BPE before/after), s10 (heatmap, gold-accent на не-1.00 cells), s13 (section divider), s17 (U-curve чистая), s23 (4-stage pipeline self-contained и крупный).

Слабые: s07, s14, s15, s19, s21, s25, s26, s27 — слишком много контента → шрифты <14pt → projector-illegible.

## P0 Issues (visual blockers)

### P0-1 — `[VERIFY-DAY-OF]` placeholder marker visible to students on s16 и s27
**Slides:** s16, s27
**What:** В нижней части слайдов виден текстовый маркер `[VERIFY-DAY-OF] Цифры на момент мая 2026...» (s16) и `[VERIFY-DAY-OF] доступность HF Playground на день семинара` (s27). Это методический cue для лектора (проверить актуальность данных в день показа), который попал в видимую зону слайда.
**Why P0:** (a) нарушает «No Extra Content Rule» — методические маркеры в speaker notes или на отдельном лист; (b) выглядит unprofessional на проекторе — студент увидит «техническую пометку».
**Fix:** Удалить `[VERIFY-DAY-OF]` markers со слайдов; переместить cue в speaker notes / iteration-log. Если нужно сохранить provenance — мелкая 9pt caption внизу типа «данные актуальны на май 2026».

## P1 Issues (≥5 → REVISE per counter-check)

### P1-1 — Projector readability fail: 10 слайдов имеют body/caption font <14pt (≈ <7pt при 50% zoom)
**Slides:** s07, s14, s15, s19, s21, s24, s25, s26, s27, s28
**What:** Эти слайды плотно заполнены 3-4 параллельными блоками (cards / decision-tree / cross-frame). При canvas 1734×975 fonts тела/caption отрендерены ~12-14pt, что при проекторе на 50% эффективного zoom = ~6-7pt. С задних рядов аудитории читаются только заголовки и крупные shape-labels.
**Why P1:** Anti-pattern #22, #30 («Projector-distance illegibility», hard min ≥18pt body, ≥14pt axis).
**Examples:**
- s07 strawberry — правая колонка «(1) Подсчёт символов / (2) Опечатки / (3) Регистр и пробелы» с разъяснениями ~12pt.
- s14 — caption под метафорой «без формул; Multi-head; QKV — доп. чтение (Vaswani et al. 2017)» ~10pt.
- s15 worked example — sub-labels «толстая — главный вес», «средняя», «тонкая» под цветными pills ~9pt.
- s19 3 температуры — caption под каждой панелькой «3-е из 3 "почему" Лекции 1 §5.3 — payoff на s24» ~10pt.
- s25 decision tree — caption внутри ветки «Классическая ML logistic, XGBoost, LightGBM, BERT fine-tuned» ~11pt.
- s26 cross-cutting frame — 3 уровня Перла per side ~11pt.
- s27 final-step boxes «Конкретно: воспроизводимый запрос (не "помоги думать")» ~10pt.
- s28 — Q&A footer и подписи под 4 cards ~10pt.
**Fix:** Reduce visual density (split каждый из этих слайдов на 1-2 более крупных), или enforce min ≥16pt body, ≥14pt caption. На критичных — abbreviate sub-labels.

### P1-2 — Overflow на s18: «Σ = 1» обрезан рамкой Top-5 box
**Slide:** s18
**What:** В правой Ocean rounded box «Top-5 кандидатов»: «… остальные ~200k токенов: каждый <0.05 Σ = 1» — последняя строка пересекает нижнюю границу box. «Σ = 1» partially clipped.
**Why P1:** Anti-pattern #20 «Equal-height boxes для unequal content». Caption длиннее, чем height box позволяет.
**Fix:** Либо увеличить высоту правого box, либо вынести «Σ = 1» в отдельную мелкую строку под bar chart.

### P1-3 — Designer-added metaphor visual без semantic role на s14
**Slide:** s14 attention bars
**What:** Левая половина слайда — иллюстрация «Метафора: фонарик в тёмной комнате» с декоративными точками (silver/gray spheres) и треугольником жёлтого света. Метафора **не работает на assertion** «Attention выдаёт распределение весов на все токены контекста (сумма = 1)» — fонарик метафорически про focus, а сумма = 1 не считывается с конуса света.
**Why P1:** Anti-patterns #4 «Text-only слайды без визуала» — здесь обратное: визуал есть, но он decorative, не proof. Anti-pattern про assertion-evidence alignment.
**Designer's own flag in spec:** iteration-log упоминает «s14 flashlight metaphor decorative-ness» как concern — confirmed.
**Fix:** Заменить «фонарик» на функциональную диаграмму weights distribution (bar chart attention weights на каждый input token прямо встроенный, без метафоры). Или удалить левую половину, оставить только правый bar chart крупнее.

### P1-4 — Cognitive overload в Разделе 3-4: 4 разные диаграммы за 30 мин
**Slides:** s14 (attention bars), s17 (Lost-in-Middle U-curve), s18 (P next token bar chart), s19 (3 температуры триптих)
**What:** За один раздел (~30 мин) студенту-introductory предъявлены: (1) bar chart attention weights, (2) line chart accuracy vs position, (3) bar chart probability distribution, (4) три параллельных bar charts температуры. Все четыре — разная семантика, разная X-axis, разная Y-axis. Студент должен мысленно переключаться между «веса в attention», «accuracy в %», «вероятность token», «частота samples».
**Why P1:** Curriculum relevance — для Лекции 2 (introductory) 4 разные диаграммы probability-related идей в 30 мин = высокий когнитивный shift. Anti-pattern #16 cross-slide chart similarity не точно дублирует но создаёт «графики мерцают».
**Fix:** Либо унифицировать визуальный язык (все 4 — same chart type, e.g. bar chart с разной семантикой осей объяснено явно), либо вычеркнуть один из них (s14 attention bars можно заменить на словесный recap «attention = weighted sum» без графика, sample-распределение из s18 — на простую таблицу).

### P1-5 — Cross-slide redundancy: bar chart на s08, s14 (right), s16 (left), s18 — 4 раза
**Slides:** s08 (RU/EN token cost), s14 (attention bars), s16 (context window log-scale), s18 (P next token)
**What:** 4 слайда используют одинаковый bar chart layout (vertical bars с подписями category). Differentiation **есть** (разные данные / axes), но визуально студент видит «одна и та же диаграмма с разными числами» — это притупляет восприятие.
**Why P1:** Anti-pattern #16 «Cross-slide chart duplication». В Лекции 1 v3 эта проблема обозначилась на s04 + s17.
**Fix:** На s18 заменить bar chart на pie/donut (более семантичный для «распределение вероятности на токены»). Или на s14 уйти от bar chart в пользу heatmap-row (1×N attention weights с цветовой градацией).

### P1-6 — Curriculum mismatch: Pearl causality (s26) — advanced concept для introductory лекции 2
**Slide:** s26 cross-cutting frame human vs AI
**What:** Правая колонка «AI (через attention) — Уровни Перла: 1. Ассоциация — да, 2. Вмешательство — частично, 3. Контрфактуальность — нет». Pearl's causal hierarchy — concept Лекции 6+ (causal AI), не Лекции 2 (how models work mechanically). Студент только что узнал что такое токен и attention — Pearl ladder = 3-step abstraction поверх.
**Why P1:** Anti-pattern «curriculum mismatch» (CLAUDE.md «Concept jump»). Plan v2.1 lists this как callback Lec-1 §4.8 Pearl — но если callback на материал, который сам по себе advanced для introductory, callback не работает.
**Fix:** Либо удалить упоминание уровней Перла на s26 (оставить простое «AI видит корреляцию, не причину»), либо вынести в опциональный «Доп. чтение» speaker notes. На слайде student-visible — только human vs AI contrast без Pearl-абстракции.

### P1-7 — Assertion-body alignment fail на s11
**Slide:** s11 «3 применения эмбеддингов: similarity, clustering, search»
**What:** Заголовок — список из 3 терминов, не assertion (полное предложение-тезис). По правилу assertion-evidence (§4 README) каждый заголовок должен быть полное предложение, доказываемое визуалом.
**Why P1:** Anti-pattern #2 «Title+Body универсально» / assertion-evidence rule violated. Сравни s10 «Близость в пространстве эмбеддингов = семантическая близость» (правильно), s17 «Большое контекстное окно ≠ хорошее использование контекста» (правильно).
**Fix:** Переписать заголовок как тезис: «Эмбеддинги работают на трёх задачах: similarity, clustering, search — все три в курсе ниже» или «Эмбеддинги — основа Лекции 3 (RAG): similarity + clustering + search».

## P2 Issues

### P2-1 — Inconsistent footer nav: s13 имеет «1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал», s02 имеет «0 Открытие / 1 ... / 5 Финал»
**Slides:** s02, s13
**What:** Footer pill-nav style выдержан, но section dividers (s13 видно) есть только на s13 (Раздел 3) — нужно проверить наличие аналогичных дивайдеров для Разделов 1, 2, 4 (текущий PNG-набор показывает только s13).
**Fix:** Verify presence + consistency 5 section dividers (Раздел 1-4 + Финал) с одинаковой структурой.

### P2-2 — `(см. s07)` cross-reference в подписи s01 — служебная нотация для студента
**Slide:** s01
**What:** В подписи «Пример 3 — слово strawberry (см. s07)» — внутренняя ссылка между слайдами видна студенту.
**Why P2:** No-Extra-Content rule; внутренние reference обычно держим в speaker notes.
**Fix:** Убрать `(см. s07)` или заменить на «(детали далее)».

### P2-3 — gold-emphasis inconsistency на s17 results
**Slide:** s17 Lost-in-the-Middle
**What:** «Середина: ~30%» — gold-emphasized; «Начало: ~75%» и «Конец: ~75%» — обычным dark blue. Семантически gold = «pivot» (worst case middle), но визуально gold обычно reads как «win/leader» — здесь «loser». Cognitive dissonance.
**Why P2:** Anti-pattern #29 «Inconsistent gold-emphasis across same-tier cards».
**Fix:** Либо использовать red/coral для «середина — worst», либо оставить gold но добавить explicit label «дно U-curve» рядом.

### P2-4 — «BPE-словарь строится один раз...» footer text на s06 повторяет italic подзаголовок сверху
**Slide:** s06
**What:** Сверху italic «Словарь строится один раз перед обучением; в inference — lookup», внизу Ocean callout «BPE-словарь строится один раз до обучения. В inference — lookup готовых правил, не runtime-вычисление.»  
**Why P2:** Текстовая редундантность — те же два утверждения. Anti-pattern #29 «one mechanism per signal».
**Fix:** Удалить italic подзаголовок (оставить только Ocean callout), либо заменить italic на более специфичное «Алгоритм Sennrich et al. 2016».

### P2-5 — Mixed RU/EN sub-labels на s23 pipeline
**Slide:** s23
**What:** Sub-labels на 4 stages: «Текст → id из словаря (BPE)», «id → вектор из learned table», «Распределение весов на контекст», «Распределение → один токен (T/p/k)». RU+EN mix — «learned table», «T/p/k».
**Why P2:** Anti-pattern #17, #26 «Mixed RU/EN sub-labels in pipeline».
**Fix:** Либо «learned table» → «обученной таблицы»; «T/p/k» → «temperature / top_p / top_k».

### P2-6 — `0.7 / 0.9 / 0.95` font-weight inconsistency на s20 table
**Slide:** s20
**What:** В столбце temperature: «0» (gold bold), «0.2-0.3» (dark bold), «0.7» (dark bold), «0.9-1.2» (teal bold). В столбце top_p: «—», «0.9», «0.9», «0.95» — все плоские. Inconsistency между столбцами bold-emphasis.
**Why P2:** Visual mass uneven; gold emphasis на «0» оправдан (LO4 anchor), но между остальными ячейками — нет signal.
**Fix:** Унифицировать: либо все ячейки bold, либо только gold accent ячейка bold.

### P2-7 — s01 footer «Источник: tiktokenizer.vercel.app (o200k_base, GPT-4o). Live demo доступен, статическая версия — fallback.» — длинный, не главный
**Slide:** s01
**What:** Footer ~3 строки текста. Live demo backup-info — методический cue для лектора (плана), не для студента.
**Fix:** Сократить footer до «tiktokenizer.vercel.app · GPT-4o o200k_base». Backup-info → speaker notes.

## Per-slide visual issues (table)

| sNN | Issue | Severity |
|---|---|---|
| s01 | Footer длинный + `(см. s07)` cross-ref student-visible | P2-2, P2-7 |
| s02 | Cover чистый, motif выдержан | — |
| s03 | Schema layered (4 layers) — выдержан bottom-anchor; gold ободок на «МОДЕЛЬ» правильно. Strong. | — |
| s04 | Central question + 3 anchor cards — strong. Мини-callout «3 ответа — payoff на s24» — лёгкая designer-add (см. P2 если cross-ref студенту не нужен) | — |
| s05 | Token cards 3 примера + footer + reflection prompt «Подумайте 15 сек» — designer-added activity prompt? Plan brief упоминает 15-sec think? Если да — OK; если нет — flag. | P2 (verify brief) |
| s06 | BPE before/after; gold ободок на After — OK, header redundancy P2-4 | P2-4 |
| s07 | Strawberry tokenization — высокая плотность right column, фонты caption <12pt | P1-1 |
| s08 | Chart + table — OK; gold bar для RU выделен правильно | — |
| s09 | Embedding lookup схема — readable; правый callout corner может содержать чуть длинный sub-text но в пределах | — |
| s10 | Cosine heatmap — strong; gold accent на «0.85» SSL/HTTPS pair правильно (correlation pair) | — |
| s11 | Title — 3 термина, не assertion | P1-7 |
| s12 | Semantic vs full-text — strong; Cross-ref «Базовый слой RAG — реализация в Лекции 3 (Retrieval-Augmented Generation)» footer чист | — |
| s13 | Section 3 divider — clean | — |
| s14 | Flashlight metaphor — decorative; right bar chart small; caption <11pt | P1-1, P1-3, P1-4 |
| s15 | Worked example: 3 size pills (толстая/средняя/тонкая) с captions <10pt | P1-1 |
| s16 | `[VERIFY-DAY-OF]` placeholder visible | **P0-1**, P1-5 |
| s17 | Lost-in-Middle U-curve clean; gold-emphasis «~30%» = worst case (semantic mismatch) | P2-3 |
| s18 | P(next token) bar chart, Top-5 box overflow на Σ = 1 | P1-2, P1-5 |
| s19 | 3 температуры triptych — мелкие caption под каждой панелью | P1-1, P1-4 |
| s20 | 4-ручек table — OK; inconsistent font-weight | P2-6 |
| s21 | Autoregressive cycle 5-step с captions <11pt + return arrow | P1-1 |
| s22 | Local/Cloud comparison 2 cards — OK | — |
| s23 | 4-stage pipeline — strong, крупный, читабельный (designer's strongest) | P2-5 (mixed RU/EN) |
| s24 | Payoff 3 промиса — strong; cross-ref `→ s15`, `→ s05–s07`, `→ s18–s19` student-visible — verify brief | P2 (verify) |
| s25 | Decision tree 3 ветки + captions <11pt | P1-1 |
| s26 | Human vs AI + Pearl уровни — Pearl advanced for intro | P1-1, P1-6 |
| s27 | 3-step homework + `[VERIFY-DAY-OF]` visible | **P0-1**, P1-1 |
| s28 | 4 outlook cards (RAG / Tools / MCP / Agent loop) + Q&A footer мелкий | P1-1 |

## Schema Readability per custom-schema slide

| sNN | Subtype | Checklist pass? |
|---|---|---|
| s03 | `schema_layered` (4 layers) | PASS — bottom-anchor, per-layer label, gold ободок на «active» layer (МОДЕЛЬ) |
| s05 | `schema_pipeline` (3 example rows) | PASS — RIGHT_ARROW per row, parallel structure, unified language |
| s06 | `schema_comparison` (Before/After columns) | PASS — equal columns, gold accent на After-side |
| s08 | `data_chart` + table comparison | PASS — readable, gold accent на RU, table parallel |
| s09 | `schema_pipeline` (id → vector lookup) | PASS — single-line flow |
| s10 | `schema_matrix` (5x5 cosine heatmap) | PASS — diagonal 1.00 dark + off-diagonal high pair gold; fill rate 100% |
| s11 | `schema_comparison` (3 cards) | **FAIL on assertion alignment** (P1-7) — schema sound but title not assertion |
| s12 | `schema_comparison` (Full-text / Semantic) | PASS — equal columns, checkmark/cross visual symbol |
| s14 | `schema_metaphor + bar chart` (split) | **FAIL** — metaphor decorative, bar chart undersized (P1-3, P1-1) |
| s15 | `schema_worked_example` (3 size pills) | **FAIL on projector readability** — sub-labels <11pt (P1-1) |
| s16 | `schema_data_chart` (log-scale + side panel) | PASS structure; **FAIL** content (`[VERIFY-DAY-OF]`) |
| s17 | `schema_line_chart` (U-curve) | PASS — gold pivot на «середина», y-axis explicit |
| s18 | `schema_data_chart` + side `Top-5` | **FAIL on overflow** (P1-2) |
| s19 | `schema_comparison` (3 triptych) | **FAIL on projector readability** (P1-1) |
| s20 | `schema_table` (4 rows × 5 cols) | PASS structure; gold accent на T=0 правильно |
| s21 | `schema_cycle` (5-step + return arrow) | PASS — explicit return arrow «↻ возврат к шагу (1)»; **FAIL on projector readability** (P1-1) |
| s22 | `schema_comparison` (Local / Cloud) | PASS |
| s23 | `schema_pipeline` (4 stage) | **PASS — strongest schema of deck**; RIGHT_ARROW shapes proper, large, readable; minor P2 mixed RU/EN |
| s25 | `schema_decision_tree` (3 branches) | PASS structure; **FAIL on projector readability** (P1-1) |
| s26 | `schema_comparison` (Human/AI 3 levels each) | **FAIL on curriculum** (P1-6) + projector readability |
| s27 | `schema_pipeline` (3 step + bonus) | **FAIL** (`[VERIFY-DAY-OF]` + projector) |
| s28 | `schema_grid` (4 outlook cards 2×2) | PASS structure; **FAIL on projector readability** Q&A footer |

## Cross-Slide Redundancy detected

1. **Bar chart layout** на s08 (RU/EN cost), s14 (attention weights), s16 (context window log-scale), s18 (P(next token)) — 4 раза одинаковый visual (vertical bars + side panel). Differentiated by data ✓ but layout pattern repeated. **Fix:** заменить s18 на pie/donut, или s14 на heatmap-row.

2. **«Pipeline 4-step»** на s02 (cover footer Tk→Em→At→Sm) + s23 (4-stage pipeline full slide). s23 это раскрытие s02, что **сильно** — но проверить, что s02 footer не дублирует визуально и не показывается «преждевременно». На самом деле s02 cover footer micro-pipeline = тизер на s23 payoff = OK pattern.

3. **Footer pill-nav** на s02, s13 (других section dividers нет в snapshot set — verify completeness Разделов 1, 2, 4, Финал) — consistent.

4. **«strawberry»** cross-reference: использован в s01 (live tokenizer example), s07 (полная case study), s24 (payoff #2 «→ s05-s07»). Многократное упоминание оправдано — anchor concept для tokenization section. OK.

5. **Lost-in-the-middle data + bar chart** **не дублируются** между слайдами. Каждый chart — distinct concept. ✓ (false alarm).

6. **«T/p/k» / «temperature / top_p / max_tokens»** упомянуты в s18, s19, s20, s23 — 4 раза. s20 — full table (правильно), s19 — 3 temp values triptych (правильно), s18 — caption «дальше — температура», s23 — sub-label «T/p/k». Согласовано, не редундантно.

## Designer-added extras

| Slide | Extra | Severity | Authorized? |
|---|---|---|---|
| s05 | «Подумайте 15 сек: "сильнее" — 1, 2 или 3 токена?» activity prompt | P2 verify | Verify plan brief — if not — P1 «designer-added activity» |
| s04 | Mini-callout «3 ответа — payoff на s24» — навигация внутри slide | P2 | Допустимо, но проверить |
| s16 | `[VERIFY-DAY-OF] Цифры на момент мая 2026. Темп роста ~×10 каждые 1-2 года.` | **P0** | Definitely not for student |
| s27 | `[VERIFY-DAY-OF] доступность HF Playground на день семинара` | **P0** | Definitely not for student |
| s01 | «(см. s07)» cross-ref в подписи Пример 3 | P2 | Internal nav exposed |
| s24 | «→ s15» / «→ s05–s07» / «→ s18–s19» small text refs | P2 | Internal nav exposed — keep if compatible with plan brief; otherwise hide |

**Не найдено:** «Лектору» секций, «Вы здесь» textual markers, тайминг минут на видимом контенте, decorative SVG без semantic role (за исключением s14 flashlight metaphor — обозначено как P1-3).

## 5-Second Test fails

При 5-секундном просмотре каждого PNG, mental simulation студента с 5-го ряда:

| Slide | 5-sec take-away | Pass? |
|---|---|---|
| s01 | Tokenizer demo 4 примера | PASS |
| s02 | Лекция 2: 4 этапа inference | PASS |
| s03 | Сегодня углубляем «модель» из 4 слоёв | PASS |
| s04 | Главный вопрос лекции + 3 ответа на s24 | PASS |
| s05 | Токен = id из словаря, не буква, не слово | PASS |
| s06 | BPE: до и после, словарь строится 1 раз | PASS |
| s07 | AI плохо считает буквы (strawberry) | PARTIAL — bullets right col <5sec illegible |
| s08 | RU тексты в 2× дороже EN | PASS |
| s09 | Каждый токен → вектор | PASS |
| s10 | Близость векторов = семантическая близость | PASS |
| s11 | 3 применения эмбеддингов | PARTIAL — title list, no thesis |
| s12 | Semantic search > full-text | PASS |
| s13 | Раздел 3: Внимание | PASS |
| s14 | Attention распределяет веса на все токены | PARTIAL — left flashlight метафора путает |
| s15 | Role tokens получают высокий вес | PARTIAL — 3 examples densely |
| s16 | Контекстное окно — физический предел; растёт 2022-2026 | PASS (но `[VERIFY-DAY-OF]` отвлекает) |
| s17 | Большое окно ≠ хорошее использование (Lost in Middle) | PASS |
| s18 | Модель выдаёт распределение, выбирает один | PASS (но overflow Σ=1) |
| s19 | T меняет острота / стандарт / хаос | **FAIL** — 3 triptych charts <14pt, не считается за 5 сек |
| s20 | 4 ручки API под сценарий | PASS (table читается) |
| s21 | Autoregressive loop — пересказы добавляем по 1 токен | PASS |
| s22 | Local 1-13B vs Cloud 200B+ — качество разное | PASS |
| s23 | 4 этапа inference сложились в pipeline | PASS — strongest |
| s24 | Лекция 1 promises payed off | PASS |
| s25 | LLM — не всегда правильный инструмент | PARTIAL — 3 ветки <12pt |
| s26 | Attention ≠ causality | PARTIAL — Pearl ladder advanced |
| s27 | ДЗ Семинар 2: apply LO4 + LO6 + LO7 | PARTIAL — 3 шага плотные |
| s28 | Лекция 3: RAG, Tools, MCP, Agent loop | PARTIAL — 4 cards <11pt |

**5-Second Test fail:** s19 — концепт «температура → распределение» не считывается за 5 сек, нужно ≥15.

## Projector Readability fails (50% zoom test)

| Slide | Fail elements |
|---|---|
| s07 | Right column bullets (1)(2)(3) разъяснения <12pt |
| s14 | Caption под метафорой, X-axis labels на bar chart <11pt |
| s15 | Sub-labels «толстая — главный вес» <10pt |
| s17 | y-axis labels OK, footer caption ОК; но «arXiv:2307.03172» caption <10pt — низкокритично |
| s18 | Top-5 right side `… остальные ~200k …` <11pt |
| s19 | All 3 panel captions <11pt; X-axis labels <10pt |
| s20 | Footer note «T = 0 практически детерминирует выбор…» <11pt |
| s21 | All 5 step sub-captions <11pt; return arrow label <10pt |
| s25 | Branch descriptions <11pt; bottom note «Иначе — LLM подходит…» <11pt |
| s26 | Pearl-ladder уровни 1/2/3 на каждой стороне <11pt; footer «Lec-1 §4.8 разбирала 3 уровня Перла» <10pt |
| s27 | Step descriptions <11pt; PlayBox footer <10pt |
| s28 | 4-card descriptions <11pt; Q&A footer <11pt |

**Verdict:** **10/28 слайдов имеют projector-readability fail** в роли body/sub-label. Должно быть 0.

## Speaker notes sample audit

⚠ **Speaker notes файлов (slides/sNN-*.md) НЕ доступны в текущей репозитории** — папка `library/lectures/lec-02/slides/` отсутствует на момент ревью (2026-05-13 17:51 UTC). Snapshot-set присутствует, но source slides + deck.yaml + chapter.md — нет. Это означает:

- Невозможно проверить «150-300 word readable text» rule.
- Невозможно проверить «no «Лектору» sections», «no director's cues», «no тайминг».
- Designer's iteration-log тоже отсутствует — нельзя сравнить flagged weaknesses (s14 flashlight, s23 final arrow) с моими находками независимо.

**Recommendation orchestrator'у:** перед Phase 8 fix-итерацией сначала восстановить `slides/*.md` + `deck.yaml` + `chapter.md` в repo (либо из git history, либо из chat artifact). Без them — невозможно sync slides ↔ chapter ↔ speech (consistency-checker phase).

## Counter-check

- P1 issues counted: **7** (P1-1 projector readability, P1-2 overflow s18, P1-3 s14 metaphor, P1-4 cognitive overload R3-R4, P1-5 cross-slide bar charts, P1-6 Pearl curriculum, P1-7 s11 assertion).
- 7 ≥ 5 → REVISE per counter-check rule. (Not APPROVE-WITH-POLISH.)
- P0 issues counted: **1** (`[VERIFY-DAY-OF]` placeholder on s16 + s27).
- Any P0 → at least REVISE. Verdict consistent.

**Final verdict: REVISE.** Fix P0-1 (placeholder removal) + 7 P1 in next iteration before USER GATE.

## Top-N приоритизированные правки for Phase 8

1. **[P0] Remove `[VERIFY-DAY-OF]` placeholders** from visible content of s16 and s27. Move provenance/freshness notes to speaker notes only. (Effort: 5 min)

2. **[P1-1, P1-4] Reduce projector readability fails on 10 slides** via splitting or font-size bumps. Concrete:
   - **s07** — split в 2 слайда: (1) examples table + general rule «1 token ≈ 4 chars EN», (2) «AI плохо считает буквы» правила (1)(2)(3) в крупном тексте.
   - **s14** — drop flashlight metaphor; keep ONLY attention bar chart, blow up к 60% canvas width; assertion-bullets справа крупнее.
   - **s15** — abbreviate role-token sub-labels («высокий», «средний», «низкий» одним словом); bump font ≥16pt.
   - **s19** — split 3 температуры на 2 слайда (T=0 + T=0.7) и (T=2.0 + summary); OR keep one big chart с T=0.7 и table с deltas T=0/T=2.0.
   - **s21** — drop bullet captions under each step, keep just numbered labels «1. Контекст», «2. Forward», «3. Distribution», «4. Sample», «5. Append» + 1-line summary внизу.
   - **s25, s26, s27, s28** — drop sub-description under each card; keep card title + ONE 1-line takeaway per card; cluster sub-text in speaker notes.
   (Effort: 2-3 hours total)

3. **[P1-2] Fix Top-5 box overflow на s18** — extend box height OR move «остальные ~200k токенов: каждый <0.05 Σ = 1» в footer mini-caption ниже chart. (Effort: 10 min)

4. **[P1-3] Replace s14 flashlight metaphor with functional attention diagram** (e.g. token sequence горизонтально, weight bars вертикально per token, sum = 1 callout). (Effort: 1 hour)

5. **[P1-5] Differentiate visualizations** между s08/s14/s16/s18 bar charts — на s18 use donut/pie для «вероятность распределена» (более семантично). (Effort: 30 min, QuickChart)

6. **[P1-6] Remove Pearl-ladder reference from s26 visible content** — keep simple «AI: корреляция / Human: причинность» binary contrast. Pearl detail в speaker notes / chapter.md. (Effort: 20 min)

7. **[P1-7] Rewrite s11 title from list to assertion**: «Эмбеддинги — основа Лекции 3 (RAG): similarity, clustering, search». (Effort: 5 min)

8. **[P2 batch] Misc polish** — s17 gold-emphasis recolor middle = red/coral (not gold for worst case); s23 RU/EN sub-label unify («T/p/k» → «temperature/top_p/top_k»); s06 remove duplicate italic header; s05 verify «Подумайте 15 сек» activity prompt is in brief (else remove); s24 verify cross-refs «→ s15» / «→ s05-s07» / «→ s18-s19» permitted (else remove). (Effort: 1 hour batch)

9. **[Required pre-fix] Restore missing source files** — `slides/*.md`, `deck.yaml`, `chapter.md`, `iteration-log.md` in `library/lectures/lec-02/`. Without these, Phase 8 designer cannot make targeted edits to specific slides without rebuilding from scratch.

10. **[P2] Verify section dividers exist** for Разделы 1, 2, 4 + Финал — only s13 (Раздел 3) visible in current snapshot set. If absent, add 4 more dividers consistent with s13.

**Total effort estimate:** 5-7 hours for designer + 30 min for orchestrator/critic re-review.

**Re-run critic + student-simulator + reader-simulator after fixes.** Counter-check P1 count must drop ≤4 для APPROVE-WITH-POLISH, или 0 для APPROVE-CLEAN.

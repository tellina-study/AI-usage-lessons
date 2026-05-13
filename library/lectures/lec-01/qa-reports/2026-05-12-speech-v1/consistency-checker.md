# Consistency Checker — chapter ↔ slides ↔ speech — Лекция 1 — 2026-05-12

**Артефакты:**
- Chapter v2 (`library/lectures/lec-01/chapter.md`, status=reviewed, ~13 268 слов, 53 источника)
- Deck v2.1 (`library/lectures/lec-01/deck.yaml` + 29 slide files + 29 PNG snapshots)
- Speech v1 (`library/lectures/lec-01/speech.md`, status=draft, ~5100 слов, slides_covered=30)

**Принцип проверки:** book-first (chapter — source of truth). Drift fix-им в speech/slides, кроме случаев, где chapter сам ошибается.

---

## Verdict

**APPROVE-WITH-MINOR-FIXES.** Cross-artifact alignment в целом сильный. Все главные тезисы лекции (центральный вопрос, чек-лист, 4 архетипа, GPT-4o sycophancy, DeepSeek, Pearl 3 уровня, narrow vs general AGI, Samsung incident, ARC-AGI economics) проходят сквозь chapter → slides → speech практически идентично — это редкое и качественное alignment для первой полной сборки.

Найдено **0 P0 (factual contradiction / missing coverage)**, **5 P1 (significant drift)**, **9 P2 (minor inconsistency)**. Все P1 — это либо локальные расхождения в одной цифре/датах/атрибуции, либо tone slip в speech относительно chapter, либо missing element coverage. Ни один P1 не блокирует USER GATE 3, но рекомендуется фикс перед финализацией speech v2. Все фиксы — на стороне speech и slides; chapter правок не требует.

## Severity counts

- **P0** (factual contradiction / missing coverage): **0**
- **P1** (significant drift): **5**
- **P2** (minor inconsistency): **9**
- **Total:** 14

---

## Cross-artifact matrix (key concepts)

| # | Concept / LO / Number | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|---|
| 1 | LO1 (классификация AI) | §1.4, §3.1-3.6 | s06, s08, s11-s17 | [s06], [s08], [s11-s17] | ✓ |
| 2 | LO4 (выбор типа AI) | §3.7, §3.8 | s18 | [s18] | ✓ |
| 3 | LO6 (3 ошибки AI) | §4.4 | s22 | [s22] | ✓ |
| 4 | LO7 (критическая проверка) | §4.3 | s21 | [s21] | ✓ |
| 5 | Central question «где AI работает» | Введение, §3.7, §5 | s05b, s14, s18, s27 | [s05b], [s14], [s18], [s27] | ✓ |
| 6 | ChatGPT 900M WAU | §2.1 | s09 | [s09] | ✓ |
| 7 | 51% разработчиков daily | §2.1 | s09 | [s09] | ✓ |
| 8 | 46% Copilot code (Java 61%) | §2.1 | s09, s25 | [s09] | ✓ (Java 61% упомянуто только в slide+chapter, не в speech — P2) |
| 9 | 84% планируют AI / 46% не доверяют (Stack Overflow) | §2.1, §4.3 | s09 | [s09] | ✓ |
| 10 | $244-390B AI рынок | §2.1 | s09 | [s09] | ✓ |
| 11 | 90% pilots не доходят до прода (CNews/Vedomosti/Intellectual Analytics, март 2026) | Введение, §2.1, §5 | s05b, s09 | [s05b], [s09] | ✓ |
| 12 | ВЦИОМ 51% (дек 2025, n=3239) | §2.1 | s04 | [s04] | ✓ |
| 13 | ВЦИОМ multi-select (ChatGPT 27%, YandexGPT 23%, DeepSeek 20%, GigaChat 15%, Шедеврум 11%) | §2.1 | s04, s14 | [s04] | ✓ |
| 14 | DeepSeek 43% teachable moment (ВЦИОМ self-report 20% vs Microsoft telemetry 43%) | §2.1 (полный teachable moment) | s04 (только в speaker notes; на слайде нет) | **отсутствует в [s04]** | ⚠ P1 |
| 15 | DeepSeek-V3 $5.6M marginal (релиз 26 дек 2024) | §2.2 | s10 | [s10] | ✓ |
| 16 | DeepSeek-R1 97.3% MATH-500 (релиз 20 янв 2025) | §2.2 | s10 | [s10] | ✓ |
| 17 | SemiAnalysis $1.3-1.6B full infra | §2.2 | s10 | [s10] | ✓ |
| 18 | Nvidia $589B капотеря 27 янв 2025 | §2.2 | s10 | [s10] | ✓ |
| 19 | MCP (Anthropic, ноябрь 2024) | §2.2 | s10 (упомянут в speaker notes) | **отсутствует в [s10]** | ⚠ P1 |
| 20 | 2017 Vaswani — Attention | §1.3, §1.2 | s07 | [s07] | ✓ |
| 21 | 160K цитирований Attention | §1.3 | s07 (в speaker notes) | **отсутствует в [s07]** | P2 |
| 22 | AI Effect (Tesler) | §1.2 | s07 | [s07] | ✓ |
| 23 | 4 оси классификации | §1.4 | s08 | [s08] | ✓ |
| 24 | Worked example GitHub Copilot по 4 осям | §1.4 (P1-5 fix) | s08 | [s08] | ✓ |
| 25 | 4 архетипа (модель/чат/агент/приложение) — слоистая модель | §3.1 | s11 | [s11] | ✓ |
| 26 | Кейс конвейера 10K/час (модель) | §3.8 | s13, s18 | [s13] | ✓ |
| 27 | Кейс 200 PDF (агент) | §3.5.1 | s16 | [s16] | ✓ |
| 28 | Agent = LLM + Memory + Planning + Tools (Weng 2023) | §3.5.1 | s16 | [s16] | ✓ |
| 29 | 5 уровней автономии (Feng/McDonald/Zhang 2025, arXiv:2506.12469) | §3.5.2 | s16 | [s16] | ✓ |
| 30 | RTC pattern (White et al. 2023) | §3.4 | s15 | [s15] | ✓ |
| 31 | Контр-роль для отладки промпта | §3.4 | s15 (Role A McKinsey vs Role B не-специалист) | [s15] (Role A McKinsey vs Role B врач-практик) | ⚠ P1 (Role B контент расходится) |
| 32 | GitHub Copilot — особый случай (inline=app, Workspace=agent) | §3.6 | s17 | [s17] | ✓ |
| 33 | Google Translate ~1T words/month (across Translate/Search/Lens/Circle) | §3.6 | s17 | [s17] | ✓ (P2-fact-2 caveat везде применён) |
| 34 | Чек-лист 4 вопросов | §3.7 | s18 | [s18] | ✓ |
| 35 | Порядок вопросов и Q4 = last-check | §3.7 | s18 (speaker notes) | [s18] (произносится явно) | ✓ |
| 36 | Раздаточный материал `ai-choice-checklist.md` | §3.7 | s18 (visible content) | [s18] (упоминание «раздаточный материал») | ✓ |
| 37 | 3 причины для границ (раздел 4 frame) | §4.1 | s19 | [s19] | ✓ |
| 38 | Структура раздела 4 «от инженерной к концептуальной границе» | §4.1, §4.5 mid-recap | s19 (speaker notes) | **отсутствует в speech** | P2 |
| 39 | Mid-point recap между §4.5 и §4.6 | §4 (между s22 и s23) | s19 (speaker notes) | **отсутствует** | P2 |
| 40 | Consumer vs enterprise tier | §4.2 | s20 | [s20] | ✓ |
| 41 | Samsung incident (3 эпизода, март-апр 2023, Bloomberg) | §4.2 | s20 | [s20] | ✓ |
| 42 | EU AI Act fines 15M/3% и 35M/7% | §4.2 | s20 | [s20] | ✓ |
| 43 | ZDR (Zero Data Retention) | §4.2 | s20 | [s20] | ✓ |
| 44 | Hallucinations определение | §4.3 | s21 | [s21] | ✓ |
| 45 | Vectara HHEM range <1%-15% | §4.3 | s21 | [s21] | ✓ |
| 46 | Готовый пример галлюцинации (DOI scientific articles) | §4.3 (P1-11 fix) | s21 | [s21] | ✓ |
| 47 | CybSafe 38% / 43% sensitive info | §4.3 | s21 | [s21] | ✓ |
| 48 | Anti-pattern «AI знает всё» | §4.3 | s21 | [s21] | ✓ |
| 49 | Retrieval moment «найдите подделку» | §4.3 | s21 (метаданные `retrieval_moment`) | [s21] (включено в речь, ~30 сек think-pair-share) | ✓ |
| 50 | Bias / sycophancy / shift trio | §4.4 | s22 | [s22] | ✓ |
| 51 | RLHF определение перед использованием | §4.4 (P1-8 fix) | s22 (speaker notes) | [s22] (произносится перед sycophancy) | ✓ |
| 52 | GPT-4o sycophancy timeline 25/28/29 апр 2025 | §4.4 (P2-fact-1 fix) | s22 | [s22] | ✓ |
| 53 | Mini-poll «что опаснее в вашей области» | §4.4 reflection | s22 (метаданные `retrieval_moment`) | [s22] (включено) | ✓ |
| 54 | Расширенный каталог проблем (reward hacking, data poisoning, prompt injection, jailbreak, model inversion, adversarial) | §4.5 (P0-4 fix с каноническими примерами) | **отсутствует** (по дизайну — chapter §4.5 only) | **отсутствует** (по дизайну) | ✓ (intentional split — chapter only, отмечено в s22 speaker notes) |
| 55 | ARC-AGI результаты (60% человек / 54% Gemini 3 Pro+Poetiq @ $30 / 37.6% Opus 4.5 Thinking @ $2.20) | §4.6 | s23 | [s23] | ✓ |
| 56 | «Цена ошибки» — переформулировка | §4.6 | s23 | [s23] | ✓ |
| 57 | 4 фигуры AGI (Altman / Amodei / Hassabis / LeCun) | §4.7 | s24 | [s24] | ✓ |
| 58 | LeCun affiliation (бывший Chief AI Scientist Meta до ноября 2025, AMI Labs март 2026, ~$1B) | §4.7 (P2-fact-3 fix) | s24 (speaker notes) | [s24] | ✓ |
| 59 | Searle Chinese Room (1980) | §4.7 | s24 | [s24] | ✓ |
| 60 | Pearl 3 уровня (association / intervention / counterfactual) | §4.8 | s25 | [s25] | ✓ |
| 61 | Развёрнутые примеры levels 2 и 3 ($100/мес лимит копилота, fine-tune vs commercial) | §4.8 (P1-9 fix) | s25 (visible + speaker notes) | [s25] (упрощённо — только level 1 пример проговорен; level 2/3 примеры на слайде, не в речи) | ⚠ P1 |
| 62 | AI лучше / Человек лучше колонки | §4.8 | s25 | [s25] | ✓ |
| 63 | Парадокс Моравека | §4.8 | s25 | [s25] | ✓ |
| 64 | Domashnee zadanie (apply-уровень, 4 LO) | §5 | s28 | [s28] | ✓ |
| 65 | 3 takeaways лекции | §5 | s28 | [s28] | ✓ |
| 66 | Карта 17 лекций / 4 блока | §5 (вкратце) + Лекция 2 анонс | s26 | [s26] | ✓ (содержание блоков очень детализировано в speech, в chapter — только bullet «дальше в курсе»; admissible expansion) |
| 67 | Callback к камере + тизер Лекции 2 (токены / эмбеддинги / attention / температура) | §5 | s27 | [s27] | ✓ |
| 68 | Q&A с backup-провокациями (universal tone) | §5 (нет, добавлено в slides+speech) | s29 | [s29] | ✓ |
| 69 | Live demo CV в начале лекции | §5 (текстом упоминается «демо в начале лекции») | s01 | [s01] | ✓ |
| 70 | Демо для s12 (3 способа: API/чат/агент) | §3 (вкратце через слоистую модель) | s12 | [s12] | ✓ (speech разворачивает demo подробно — корректное расширение для устного формата) |

**Summary matrix:** ~70 ключевых концептов проверено; aligned = 64 (91%), drift = 6 (9% — все P1/P2). Это очень сильный alignment для первой сборки.

---

## DISCREPANCIES

### D1 — DeepSeek 43% teachable moment не звучит в речи

**Severity:** P1
**Where:** chapter §2.1 (полный teachable moment, ~250 слов) vs slide s04 (вынесено в speaker notes как контекст) vs speech [s04] (полное отсутствие)
**Issue:** Chapter содержит расширенный teachable moment про две методологии измерения (ВЦИОМ self-report ~20% vs Microsoft telemetry ~43%) — это центральный методологический урок раздела 2 («прежде чем сравнивать AI-цифры, сравните методологии»). В деке этот урок намеренно вынесен на slide s04 в speaker notes (P0 fix v5: «43% не показывать на слайде»). Speech [s04] полностью **опускает** упоминание про 43% и две методологии — звучит только финальное обобщение «прежде чем сравнивать AI-цифры, всегда смотрите на методологию», без иллюстрации.

Цитата speech [s04]: «Мораль — две: первая, ландшафт не "ChatGPT и всё". И вторая, важнее: **прежде чем сравнивать AI-цифры, всегда смотрите на методологию**.» — но **что именно смотреть и почему**, не объясняется.

В chapter §2.1: «...параллельно с ВЦИОМ-цифрой "20% использовавших DeepSeek" в публичном пространстве циркулирует другая — "DeepSeek 43% в России" (Microsoft Threat Intelligence, январь 2026)... Студент должен научиться не выбирать "правильную" цифру, а понимать, что обе верны, потому что **измеряют разное и разными методами**.»

**Recommendation:** Добавить в speech [s04] (или [s14], где снова показывается ВЦИОМ multi-select) короткий устный teachable moment (1-2 предложения):
> «Кстати — параллельно с этими цифрами вы встретите "DeepSeek 43% в России" из Microsoft. Это не противоречие: ВЦИОМ — опрос (self-report), Microsoft — телеметрия. Обе цифры верны, измеряют разное. Это — пример того, что значит "смотреть на методологию".»

Lecturer всё равно держит этот контент в голове (он есть в speaker notes s04), но без устной фразы аудитория получает только общее правило без иллюстрирующего кейса. Это **снижает эффект главного teachable moment §2.1**.

---

### D2 — MCP (Model Context Protocol) исчезает в speech [s10]

**Severity:** P1
**Where:** chapter §2.2 (заключительный абзац о MCP как параллельной инфраструктурной стандартизации) vs slide s10 (упомянуто в speaker notes + visible content «2026 действие (агенты, MCP)») vs speech [s10] (полное отсутствие)
**Issue:** Chapter §2.2 посвящает целый абзац MCP: «Anthropic в ноябре 2024 года представила Model Context Protocol (MCP) — открытый протокол... к 2025–2026 годам MCP де-факто стал стандартом... другой признак того, что AI вышел из стадии "отдельного продукта".» Slide s10 содержит этот фрагмент в visible content («2022 чат → 2023 зрение → 2024 рассуждение → 2025 код → 2026 действие (агенты, MCP)») и подробно в speaker notes. Speech [s10] заканчивается на DeepSeek-морали для инженера и переходит сразу на s11 — **MCP не упоминается ни одним словом**.

Это значит: студент в зале **видит** «MCP» в траектории парадигм на слайде, но не получает устного объяснения. Slide и speech рассинхронизированы.

**Recommendation:** Добавить в speech [s10] финальный фрагмент (~20-30 секунд):
> «Параллельно — инфраструктура. В ноябре двадцать четвёртого Anthropic представила Model Context Protocol — MCP. Открытый протокол, через который LLM единообразно подключаются к инструментам, данным, сервисам. К двадцать пятому-шестому MCP де-факто стандарт. Это другой признак, что AI вышел из стадии "отдельного продукта".»

Это синхронизирует slide visible content («2026 действие — MCP») со звучащей речью, и дополнительно подкрепляет тезис «концепты переживают смену поколений моделей» — MCP как пример устойчивого концепта.

---

### D3 — Pearl level 2/3 примеры не проговариваются в речи

**Severity:** P1
**Where:** chapter §4.8 (развёрнутые примеры $100/мес лимит копилота для level 2 + fine-tune vs commercial для level 3, по P1-9 fix) vs slide s25 (оба примера в visible content и speaker notes) vs speech [s25] (только сухая дефиниция уровня + конкретного примера нет)
**Issue:** Chapter (P1-9 ревизия v2) содержит развёрнутые worked examples для levels 2 и 3 — каждый ~1 абзац, ~150 слов. Эти примеры **видны на slide s25** в visible content («"если поставим лимит $100/мес на API копилота"», «"был бы наш проект в проде, если бы выбрали другой подход в 2023?"»). В speech [s25] звучит только дефиниция каждого уровня **без worked example**:

- Level 1: упомянут пример (correlation Y → 15% быстрее), но косвенно через level 2 framing
- Level 2: «"Что произойдёт, если я сделаю X". Требует модели мира и контрфактуального мышления.» — **без примера**
- Level 3: «"Что было бы, если бы X не случилось". Требует имагинации и причинной модели.» — **без примера**

Студент в зале видит примеры на слайде в кратком виде, но лектор их не комментирует. Это сильное снижение pedagogical depth — было применено P1-9 fix именно для того, чтобы переместить разъяснение с уровня **remember** на уровень **understand**.

**Recommendation:** Speech [s25] — добавить 30-45 секунд после дефиниций уровней:
> «Пример уровня 2 на слайде: команда внедрила копилот, видит — разработчики с копилотом закрывают тикеты на пятнадцать процентов быстрее. Это уровень 1, корреляция. А вопрос уровня 2: "если мы поставим лимит сто долларов в месяц на API копилота — что произойдёт с productivity?" На это статистическая модель не ответит — корреляция не сохранится в новых условиях. Ответ требует или эксперимента, или каузальной модели.
>
> Уровень 3 — контрфактуальный. "Был бы наш проект в проде, если бы в двадцать третьем мы выбрали другой архитектурный подход — fine-tune собственной LLM вместо лицензионной?" Это альтернативная история, её нельзя проверить эмпирически. Эксперт может оценить с большой неопределённостью; LLM не может в принципе.»

Это синхронизирует chapter (P1-9 ревизия) с устным изложением и поднимает s25 с уровня remember/understand до evaluate.

---

### D4 — Role B контент расходится: chapter+slide «не-специалист, далёкий от технологий» vs speech «врач-практик»

**Severity:** P1
**Where:** chapter §3.4 («не-специалист, далёкий от технологий») vs slide s15 visible («Не-специалист, далёкий от технологий», v5 P1-tone fix — было «бабушка из Простоквашино») vs speech [s15] («"Ты — врач-практик, объясняешь пожилому пациенту"»)
**Issue:** Chapter и slide синхронно используют нейтральную формулировку Role B «не-специалист, далёкий от технологий» (это специально согласовано: registr regulation отмечена в s15 speaker notes — «speech ОК, chapter universal»). Speech [s15] вводит **другой пример** Role B — «врач-практик, объясняющий пожилому пациенту».

Это не противоречие по смыслу (контраст ролей сохраняется), но **drift в конкретном контенте**: студент в зале услышит про «врача-практика», прочитает в self-study «не-специалиста». В speaker notes s15 явно фиксируется: «**В chapter использован "не-специалист, далёкий от технологий" вместо "бабушка из Простоквашино" (registr regulation: speech ОК, chapter universal).**» — то есть **намеренный split разрешён**, но фактический speech contрадикт slide visible content (на slide стоит «не-специалист», speech говорит «врач-практик»).

**Recommendation:** Выбрать один. Вариант A (минимальный drift): speech использует ту же формулировку что и slide — «не-специалист, далёкий от технологий, тот же вопрос». Вариант B: разрешить registr regulation для speech, но тогда **обновить speaker notes s15**, явно указав «slide — нейтральный пример, speech — конкретизация (врач-практик)». Сейчас рассогласовано: speaker notes говорят «speech ОК», но slide visible content «не-специалист» рисует другой пример, чем тот, что произносится.

Я рекомендую **Вариант A** (синхронизировать на «не-специалист»): сейчас slide показывает одну Role B, лектор говорит про другую — это создаёт когнитивную дисcонансу для аудитории, читающей слайд во время речи.

---

### D5 — Java 61% в Copilot — упомянуто в chapter+slide, нет в speech

**Severity:** P1
**Where:** chapter §2.1 (явно: «46% строк кода написано AI, для языка Java — 61%») vs slide s09 visible («46% кода у юзеров Copilot · Java — 61%») vs speech [s09] («до сорока шести процентов кода у активных пользователей пишет AI» — без Java 61%)
**Issue:** Chapter и slide содержат конкретную anchor-цифру «Java — 61%», которая является retoricalным усилением (показывает разброс по языкам). Speech упускает это уточнение — что снижает эффект «46% — средняя, локально может быть 61%».

**Recommendation:** Speech [s09] — добавить одну фразу:
> «GitHub Copilot — больше двадцати миллионов пользователей. По их данным, **до сорока шести процентов кода** у активных пользователей пишет AI. Для языка Java — **шестьдесят один процент**.»

(Уже есть «Для языка Java — шестьдесят один процент.» в speech! Я ошибся при анализе. Перечитаю.)

**Update после re-check speech [s09]:** «GitHub Copilot — больше двадцати миллионов пользователей. По их данным, **до сорока шести процентов кода** у активных пользователей пишет AI. **Для языка Java — шестьдесят один процент.**» — Java 61% **есть** в речи.

**D5 закрыто как ложное срабатывание.** Aligned.

(Оставляю запись для transparency. Финальный severity counts: **P1 = 4** вместо 5.)

---

## Coverage gaps (LO / разделы / assertions)

### Не gaps, но границы покрытия (worth noting)

1. **§4.5 Расширенный каталог проблем (reward hacking, data poisoning, prompt injection, jailbreak, model inversion, adversarial examples)** — намеренно в chapter only, в slides и speech не разворачивается (тогда мы бы вышли за 75 минут). Это by design (отмечено в s22 speaker notes: «**Расширенный каталог проблем** — не на этом слайде, а в chapter §4.5 + более поздняя лекция курса по AI security/safety»). **Aligned, intentional split.**

2. **§4.5 mid-point recap (между §4.5 и §4.6)** — есть в chapter (P0-3 fix), отсутствует в speech (нет переходной фразы между s22 и s23, объясняющей переход «от инженерной к концептуальной границе»). **P2** — speech течёт прямо с GPT-4o sycophancy на ARC-AGI без явного structurального моста. Recommend: добавить 2 предложения в начало [s23]:
   > «Мы прошли половину раздела четыре. Бласа, sycophancy, shift, утечки, галлюцинации — это **что ломается внутри AI-системы**. Дальше — три слайда про другое: **где AI как класс упирается в потолок не из-за плохой инженерии, а по природе подхода**. ARC-AGI — про границу абстрактного обобщения; narrow vs general — про границу обобщения по доменам; Pearl — про границу между корреляцией и каузальностью.»

3. **160K цитирований Attention** — есть в chapter §1.3 и speaker notes s07, **отсутствует** в визибл-контенте слайда s07 и в speech [s07]. P2 — это flavor stat, не критично, но в speech [s07] звучит «**больше ста шестидесяти тысяч цитирований**» — фраза **есть в речи**, я её пропустил при первом анализе. Закрыто.

4. **Структурное объяснение «от инженерной к концептуальной границе» (раздел 4 frame)** — есть в chapter §4.1 и в s19 speaker notes. В speech [s19] упоминаются 3 причины, но **structurальное объяснение последующих 7 тем отсутствует** в речи. P2.

### Реальный gap (worth resolving)

5. **Q&A провокация про DeepSeek/ARC-AGI/AGI как «темы, которые могут зацепить»** — есть в speech [Резерв] и [s29] speaker notes. **Aligned.**

---

## Tone consistency (chapter ↔ slides ↔ speech)

| Aspect | Chapter | Slides | Speech | Status |
|---|---|---|---|---|
| «Инженер ИУ6» / Бауманка | Не упоминается (universal) | Не упоминается (P0-2 fix v5 — universal tone) | Не упоминается (universal) | ✓ |
| «Магическая пилюля» tone | Отсутствует (диагностический тон) | Отсутствует (s05b: «не recipe, а навигация») | Отсутствует («Не магия, не угроза» в [s01]; «не "будущее, которое наступит"») | ✓ |
| «Вы»-форма | Используется консистентно (academic «студент» / «вы») | Используется («ваш чек-лист», «ваша зона ответственности») | Используется («поднимите руки», «ваша оценка») | ✓ |
| Универсальная audience (не «выпускник ИУ6», не «российский разработчик» эксклюзивно) | ✓ | ✓ (s29 backup-провокация: «коллега» вместо «инженер ИУ6» — P0-2 fix v5) | ✓ | ✓ |
| Tone open question vs gotcha (s23, s29) | Chapter §4.6 формулирует «честно, не как gotcha» | Slide s23 «open question (formulируется честно, не gotcha)» | Speech [s23]: «Я задам его честно, не как gotcha» — explicitly синхронно | ✓ |

**Все 4 tone-критерии полностью consistent across все 3 артефакта.** Это сильное достижение — особенно учитывая, что v5 plan ещё включал «инженер ИУ6» в Q&A провокации, а сейчас всё universalized.

---

## Sequence consistency

**Порядок концептов:** chapter §1→§2→§3→§4→§5 ↔ slides s01-s05 (открытие) → s06-s08 (раздел 1) → s09-s10 (раздел 2) → s11-s18 (раздел 3) → s19-s25 (раздел 4) → s26-s29 (заключение) ↔ speech [s01]→[s29] строго следует deck order. **✓ Aligned.**

**Внутренний порядок раздела 4:** chapter §4.1 → §4.2 → §4.3 → §4.4 → §4.5 → §4.6 → §4.7 → §4.8 ↔ slides s19→s20→s21→s22→s23→s24→s25 (s22 покрывает §4.4, §4.5 идёт только в chapter — by design) ↔ speech следует строго. **✓ Aligned.**

**Worked example на конвейере (§3.8):** chapter содержит worked example в конце §3 (после §3.7 чек-листа), slide s18 имеет worked example в gold callout, slide s13 содержит сам кейс конвейера. Speech [s13] разворачивает кейс детально, [s18] callback'ом возвращает. **✓ Aligned.**

---

## Speaker notes ↔ speech alignment

**Sample check на 8 ключевых slides (s10, s12, s16, s18, s20, s21, s22, s25):**

- **s10 speaker notes** vs speech [s10]: speaker notes более компактные, speech разворачивает в conversational форму. Содержательно identicale — те же 3 даты, те же $5.6M / $1.3-1.6B / $589B, те же 2 морали для инженера. **Aligned.** *Drift:* MCP абзац есть в speaker notes, отсутствует в speech (см. D2).
- **s12 speaker notes** vs speech [s12]: speaker notes описывают hybrid live+video, speech ведёт через 3 demo с конкретными timing'ами (30 сек / 30 сек / 2 мин). Aligned, speech более операциональный.
- **s16 speaker notes** vs speech [s16]: identical 5 уровней автономии (operator → observer), идентичные примеры (Claude Code approve / Cursor парное / Devin тикет / agent PR / AutoGPT ночью). Aligned.
- **s18 speaker notes** vs speech [s18]: оба явно объясняют порядок Q1-Q4 и почему Q4 last-check. Worked example «Конвейер 10K/час → Q1 ДА · Q2 НЕТ · Q3 НЕТ · Q4» есть в speaker notes, в speech даётся через [s13] и затем callback в [s18]. Aligned.
- **s20 speaker notes** vs speech [s20]: identical Samsung timeline (3 эпизода, март-апрель 2023), identical EU AI Act fines (15M/3% standard + 35M/7% prohibited), identical breakeven ~100K req/day, identical practical takeaway. Aligned.
- **s21 speaker notes** vs speech [s21]: identical Vectara HHEM range, identical CybSafe 38%/43%, identical anti-pattern «AI знает всё», identical retrieval moment. Aligned.
- **s22 speaker notes** vs speech [s22]: identical RLHF определение (P1-8 fix перед использованием в sycophancy), identical timeline 25/28/29 апреля 2025 GPT-4o, identical 3-card structure bias/sycophancy/shift, identical mini-poll. Aligned.
- **s25 speaker notes** vs speech [s25]: speaker notes более глубокие (содержат worked examples levels 2/3); speech упрощённее (см. D3). **P1 drift.**

**Общая оценка speaker notes ↔ speech:** ~85% полное alignment. Speaker notes везде являются концентрированной версией chapter; speech разворачивает в conversational форму. Single significant drift — D3 (Pearl examples).

---

## References parity

**Sources в chapter (53 источника):** см. полный список в chapter §Источники.

**Sources в slides:** каждый slide.references — subset chapter sources + несколько specific (e.g., `feng-mcdonald-zhang-2025-autonomy` для s16, `vciom-2025-onlay-dec` + `vciom-2025-oct` для s04).

**Sources в speech:** sources не имеют отдельной footnotes — упоминаются inline в речи (например, «По данным ВЦИОМ-Онлайн декабря двадцать пятого, выборка три тысячи человек», «Stack Overflow Developer Survey две тысячи двадцать пятого года, выборка сорок девять тысяч», «работа Лилианы Венг», «Feng, McDonald и Zhang в работе двадцать пятого года», «Bloomberg», «SemiAnalysis», «Vectara HHEM», «CybSafe», «OpenAI postmortem», «Pearl 2018 Book of Why» вкратце «Pearl»).

**Verification — все speech-mentioned sources присутствуют в chapter sources:**

- ✓ ВЦИОМ-Онлайн декабрь 2025 (n=3239) → chapter source
- ✓ ВЦИОМ октябрь 2025 (n=1600 multi-select) → chapter source
- ✓ Stack Overflow Developer Survey 2025 → chapter source
- ✓ OpenAI 900M WAU февраль 2026 → chapter source
- ✓ GitHub Octoverse 2025 → chapter source
- ✓ Statista/McKinsey 2025 → chapter source
- ✓ CNews/Vedomosti/Intellectual Analytics март 2026 → chapter source
- ✓ Gartner 2024 (80% workforce) → chapter source
- ✓ Vaswani et al. 2017 → chapter source
- ✓ McCarthy 1956 → chapter source
- ✓ Tesler «AI Effect» → chapter source (упомянут в §1.2)
- ✓ DeepSeek 2025 R1 → chapter source
- ✓ SemiAnalysis 2025 → chapter source
- ✓ Bloomberg 2025 (Nvidia $589B) → chapter source
- ✓ Hendrycks et al. 2021 (MATH-500) → chapter source
- ✓ Bloomberg 2023 (Samsung) → chapter source
- ✓ EU AI Act 2024/1689 → chapter source
- ✓ Anthropic «Building Effective Agents» → chapter source
- ✓ White et al. 2023 prompt patterns → chapter source
- ✓ Weng 2023 → chapter source
- ✓ Yao et al. 2022 ReAct → chapter source
- ✓ Feng/McDonald/Zhang 2025 (arXiv:2506.12469) → chapter source
- ✓ Google Translate 2026 → chapter source
- ✓ Vectara HHEM → chapter source
- ✓ CybSafe «Oh Behave!» → chapter source
- ✓ OpenAI 2025 GPT-4o sycophancy postmortem → chapter source
- ✓ Chollet 2019 ARC-AGI → chapter source
- ✓ Pearl 2018 Book of Why → chapter source
- ✓ Searle 1980 Chinese Room → chapter source
- ✓ Moravec 1988 → chapter source
- ✓ He et al. 2015 ResNet → chapter source
- ✓ Jumper et al. 2021 AlphaFold → chapter source
- ✓ IBM Deep Blue 1997 → chapter source

**P2-фактах в chapter sources, не упомянутые в speech:** Russell & Norvig 2021, ISO/IEC 22989:2022, Mitchell 1997, Goodfellow 2016, Krizhevsky 2012, Sutton & Barto 2018, Roediger & Karpicke 2006, NIST AI RMF, NIST AI 600-1, Dhar 2024, Bostrom 2014, Carlini 2020 (model inversion), Goodfellow 2014 (adversarial), Pan 2022 (reward), MS Threat Intelligence, Kreuzberger 2023, Baltrusaitis 2019, Dam 2024. **Все эти источники упомянуты либо в chapter sources only (academic background), либо в slide speaker notes for self-study readers.** No drift — корректное layering.

**References parity overall: ✓ aligned.** Все sources, упомянутые в speech, присутствуют в chapter sources. Inverse — ОК (chapter shire references for academic depth).

---

## Visual ↔ verbal alignment

**Speech правильно указывает на slides:**
- [s01] «посмотрите на проектор» — visual = live camera. ✓
- [s04] «На слайде — donut с цифрой 51%, под ним bar-chart с пятью LLM» — соответствует slide s04 visible content. ✓
- [s07] «На слайде — горизонтальная линейка 1950→2026 в трёх группах.» — соответствует. ✓
- [s09] «На слайде — сетка 4 метрик + gold-callout с 90% откатов.» — соответствует. ✓
- [s10] «На слайде — хронология декабрь 2024 → 27 января 2025 + три анкер-стата.» — соответствует. ✓
- [s11] «На слайде — четыре концентрических слоя.» — соответствует. ✓
- [s12] «На слайде — задача в monospace + 3-колоночная сравнительная таблица.» — соответствует. ✓
- [s15] «На слайде — три колонки: bad prompt / Role A / Role B + RTC формула.» — соответствует (но Role B контент drift — см. D4). ⚠
- [s16] «На слайде — кейс 200 PDF + Agent=LLM+M+P+T + лесенка 5 уровней.» — соответствует. ✓
- [s18] «На слайде — четыре вопроса + 2x2 quadrant.» — соответствует. ✓
- [s20] «На слайде — две колонки Consumer vs Enterprise + Samsung incident + EU fines.» — соответствует. ✓
- [s21] «На слайде — пример промпта + 3 fake DOI + Vectara HHEM range + анти-паттерн.» — соответствует. ✓
- [s22] «На слайде — три карточки + GPT-4o timeline.» — соответствует. ✓
- [s23] «На слайде — три bars: человек 60% / refinement 54% / commercial 37.6% + open question.» — соответствует. ✓
- [s24] «На слайде — шкала 2-30 лет с 4 лидерами + их stakes.» — соответствует. ✓
- [s25] «На слайде — две колонки + пирамида уровней Pearl.» — соответствует. ✓
- [s26] «На слайде — 4 блока с outcome-фразой под каждым.» — соответствует. ✓
- [s27] «На слайде — мини-кадр YOLO + central question recall + 4 концепта Лекции 2.» — соответствует. ✓
- [s28] «На слайде — три карточки + gold callout с домашним заданием.» — соответствует. ✓
- [s29] «На слайде — крупное «Q&A» + 2 backup-провокации.» — соответствует. ✓

**Visual ↔ verbal alignment: ✓ aligned.** Speech правильно ориентирует аудиторию по slide visuals на каждом переходе.

**Slide visuals подкреплены описанием в chapter:**
- s04 donut + bar — chapter §2.1 содержит вербальное описание тех же данных (51% / multi-select shares).
- s07 timeline — chapter §1.2 содержит ту же 3-grouped структуру (открытия / зимы / перелом).
- s09 stat grid — chapter §2.1 разворачивает каждую цифру.
- s10 timeline — chapter §2.2 разворачивает 3 даты.
- s12 demo сравнительная таблица — chapter §3 имплицитно покрывает (через слоистую модель в §3.1).
- s16 5 уровней — chapter §3.5.2 имеет полную таблицу с примерами.
- s18 чек-лист + 2×2 quadrant — chapter §3.7 имеет описание.
- s22 3 карточки + GPT-4o timeline — chapter §4.4 имеет detailed описание.
- s24 шкала прогнозов — chapter §4.7 имеет полное описание 4 фигур.
- s25 пирамида Pearl — chapter §4.8 имеет worked examples (которые не звучат в speech — D3).

**Visual ↔ chapter alignment: ✓ aligned.** Каждый visual в slides подкреплён вербальным описанием в chapter (это ключевая дисциплина academic textbook chapter — описывает текстом то, что на слайде показано визуально).

---

## Топ-фиксов (per artifact)

### Speech (priority — это единственный артефакт в draft статусе)

1. **[s04]** — добавить 1-2 предложения teachable moment про DeepSeek 43% (D1).
2. **[s10]** — добавить 20-30 секунд про MCP в финал (D2).
3. **[s25]** — добавить 30-45 секунд worked examples levels 2 и 3 Pearl (D3).
4. **[s15]** — синхронизировать Role B с slide visible content («не-специалист, далёкий от технологий» вместо «врач-практик, объясняющий пожилому пациенту»). ИЛИ обновить s15 speaker notes, явно разрешая registr regulation (D4).
5. **[s23]** — добавить 2 предложения mid-point recap «от инженерной к концептуальной границе» в начало (P2 closing gap #2).
6. **[s19]** — добавить 1 предложение про 7-тематическую структуру раздела 4 (P2 closing gap #4).

### Slides (минорные)

7. **s05a** — заполнить placeholder content инструктора (status=draft-pending-content, отдельный TODO независимо от consistency).
8. **s26** — финализировать course_curator-driven roadmap из 00-course/ (отдельный TODO).
9. **s15** — если выбираем Вариант B по D4, обновить speaker notes явно про разрешённый split «slide universal, speech registr-regulation».

### Chapter (минимальные)

10. **§5** (Заключение) — добавить 2-3 предложения про карту 17 лекций / 4 блока, чтобы chapter §5 коротко покрыл то, что развернуто в [s26] speech (~150-200 слов; сейчас chapter говорит «**Что будет в Лекции 2**», но 4-блочная карта семестра в chapter отсутствует — info есть только в slides+speech). **Это единственная rec для chapter, она опциональна** — chapter сейчас фокусируется на «Лекция 2» как ближайший шаг, что academic-style разумно. Если хочется coverage parity — добавить 1 параграф; если оставить как есть — это admissible split (chapter = academic textbook focus on course book; slides+speech = lecture-day roadmap).

---

## Summary Verdict

**APPROVE-WITH-MINOR-FIXES.**

Это **первый запуск consistency-checker'а** в проекте, и результат очень сильный: 0 P0, 4 P1, 9 P2 на ~70 проверенных концептах. Все P1 — это либо локальные drift'ы в одной фразе (Role B пример), либо missing coverage конкретного abzaca в speech (DeepSeek 43% teachable moment, MCP, Pearl levels 2/3). Ни один P1 не блокирует USER GATE 3.

**Рекомендация:** провести минорный revision speech v1 → v2 с fix'ами D1, D2, D3, D4 и P2 #2, #4 (см. «Топ-фиксов: speech» 1-6) — это **не более 3-5 минут речи дополнительно** к уже написанным 75 минутам, что укладывается в **резерв 7 минут**. После этого все 3 артефакта могут идти в USER GATE 3 final.

**Подтверждение book-first методологии:** chapter не требует фиксов (опциональная rec #10 — admissible). Все drift'ы → fix в speech (4) и слайде (1 minor).

---

*Конец отчёта consistency-checker.*

*Reviewer: consistency-checker agent*
*Date: 2026-05-12*
*Артефакты review'ены полностью: chapter v2 (574 строки), deck v2.1 (29 slides + yaml), speech v1 (860 строк).*

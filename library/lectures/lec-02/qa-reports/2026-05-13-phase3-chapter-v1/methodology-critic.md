# Methodology-Critic Report on Chapter Лекции 2 v1.0 — 2026-05-13

VERDICT: APPROVE-WITH-POLISH

## Summary

Chapter v1.0 — методически крепкая работа, точно реализующая plan v2.1. Все четыре LO (LO1, LO4, LO6, LO7) явно заявлены и систематически покрыты; четырёхэтапный конвейер (токенизация → эмбеддинг → внимание → сэмплинг) выдержан как сквозная спина главы; payoff из Лекции 1 §5.3 («три "почему"») доставлен в §5.2 explicitly и mechanism-grounded, без overclaim — каждое «почему» сопровождается softer-phrasing-оговоркой (in-context steering / RLHF / батчинг). Cognitive load для introductory уровня держится: формулы и Q/K/V вынесены за скобки, метафора «фонарик» — единственная (магнит вычеркнут, как и требовал план). Cross-references к Лекции 1 — действительно callback'и в 1-2 предложения, без повтора; никаких «возьмём ещё раз тему §X». Tone — объяснительно-инженерный, без триумфализма и без «магии LLM» (единственное упоминание слова «магия» — в негации, lines 125 + 326 — корректно). Anti-pattern grep чист: «промптинг — сквозной навык» / «магическая пилюля» / «УГАДАЙ» / «инженер ИУ6» отсутствуют; форбидден-список 17 пунктов из plan §6 соблюдён.

Главные оставшиеся методические недочёты — все на уровне P1/P2, не блокирующие: (1) одна inconsistency имени «Перл/Пёрл» внутри главы, (2) одна неточная ссылка на Lec-1 §3.3.1 (фраза «следствие 1» живёт в §3.3, не в §3.3.1), (3) пара insider-фраз («апельсинов-к-апельсинам», «анти-патология упрощения»), (4) гипотетический GPT-4 emb 12288 dim приведён в основном теле раздела 2.1, а не вынесен в speaker note (как просит plan §9 freshness — softer phrasing), (5) Word2Vec king-queen в §2.2 занимает не «1 предложение исторической отметки» (как предписывал план #12), а полноценный абзац с цитатой; границу с forbidden-additions item 12 ставит, но в полноту pure-passage не попадает. По стандартным критериям все эти замечания — polish, не block. Подлог не найден; tone-drift минимален; LO-mapping явный.

Counter-check: 4 P1 issues — verdict APPROVE-WITH-POLISH consistent (≤4 P1 правило).

## P0 Issues

Нет.

## P1 Issues

### [P1-1] Pearl spelling drift внутри главы
**Severity:** P1 (terminology lock breach, влияет на consistency).
**Location:** Введение line 79 — «три уровня причинности **Перла**» vs §5.4 line 506 — «три уровня причинности **Пёрла**».
**Evidence:**
- Line 79: «локальные vs облачные модели (§4.2), три уровня причинности Перла (§4.8).»
- Line 506: «возврат к одному из самых концептуально важных мест Лекции 1 (§4.8): **три уровня причинности Пёрла**.»
**Methodology issue:** Lec-1 throughout uses «Перла» (без ё) — это canonical в курсе. Глава 2 в одном месте использует «Перла», в другом — «Пёрла». Term-drift inside one document undermines glossary discipline и breaks reader trust.
**Recommendation:** Унифицировать на «Перла» во всех 2 местах (consistent с Lec-1). Если хотите перейти на «Пёрла» — это cascade rename, требующий fix также в Lec-1 §4.8 (4 случая), что выходит за scope текущей фазы.

### [P1-2] Cross-reference miss: «§3.3.1, следствие 1: контроль через системный промпт»
**Severity:** P1 (incorrect cite weakens cross-doc integrity).
**Location:** §4.3, line 386.
**Evidence:** «системный промпт … (см. Лекция 1 §3.3.1, "следствие 1: контроль через системный промпт").»
**Verification:** В Lec-1 §3.3.1 — это «Архитектура агента». «Следствие 1: контроль через системный промпт» — текст из Лекции 1 §3.3 (line ~327 chapter, цикл чата), а **не** §3.3.1.
**Methodology issue:** Студент, перейдя по ссылке, не найдёт «следствие 1» в §3.3.1 — это создаёт когнитивный разрыв («где это?»), который reader-simulator текстовый режим может flag отдельно. Также chapter §4.3 один раз использует именно эту фразу как точную цитату, что усиливает несоответствие.
**Recommendation:** Заменить «§3.3.1» на «§3.3» в этой ссылке (line 386). Альтернатива — переформулировать без точной цитаты: «(см. Лекция 1 §3.3 о роли системного промпта)».

### [P1-3] Word2Vec в §2.2 объёмом превышает предписанное «1 предложение исторической отметки»
**Severity:** P1 (forbidden-addition framing #12, plan §6).
**Location:** §2.2, lines 201-203.
**Evidence:**
> «Исторической отправной точкой для разговора об эмбеддингах — Word2Vec (Mikolov et al., 2013): первая широко известная модель, в которой выученные векторы слов демонстрировали аналогии вроде `король - мужчина + женщина ≈ королева`. Этот результат стал знаменитым и до сих пор приводится во многих учебниках. Для современной практики, однако, он скорее историческая отметка: с 2013 года поле прошло несколько поколений моделей…»
**Plan constraint:** §6 forbidden additions #12: «Word2Vec king-queen как central visual — historical note в s10 speaker only.» Plan §4 s10 «Speaker note: Word2Vec king-queen (Mikolov 2013) — историческая отметка в 1 предложении, без отдельного слайда.»
**Methodology issue:** В chapter ныне это **3 предложения и явная аналогия king-queen в основном теле** (с примером равенства). Это не запрещено для chapter (chapter — body of knowledge, шире слайдов), но воспроизводит то самое visual-аналогию, которую plan хотел сократить — а chapter — primary source, из которого speaker notes derive. Если оставить как есть, speaker note s10 может разрастись.
**Recommendation:** Option A (минимум): оставить факт упоминания Word2Vec, но убрать сам equation «король - мужчина + женщина ≈ королева» (оставить «выученные векторы слов демонстрировали семантические аналогии»). Option B (предпочтительно): сократить до 1 предложения: «Word2Vec (Mikolov et al., 2013) — историческая отправная точка; для современной практики аккуратнее работать на уровне sentence-эмбеддингов, ниже».

### [P1-4] «Апельсинов-к-апельсинам» — insider calque
**Severity:** P1 (insider phrasing, Term Canonical-Validity Check).
**Location:** §5.5, line 530.
**Evidence:** «Целевая модель для unified апельсинов-к-апельсинам сравнения — `Meta-Llama-3-8B-Instruct`.»
**Methodology issue:** «Apples-to-apples» — английская идиома; буквальная калька «апельсинов-к-апельсинам» не существует в русской технической литературе (и тем более apples ≠ апельсины — этот же фрагмент — orange, не apple). Это **insider phrasing**, которое: (1) не каноническое, (2) фактически смешивает apple и orange, (3) непонятно студенту без догадки об английском оригинале.
**Recommendation:** Заменить на «единообразного сравнения» / «прямого сравнения между студентами» / «чтобы у всех была одна и та же базовая модель». Например: «Целевая модель — `Meta-Llama-3-8B-Instruct`, чтобы у всех студентов было одинаковое основание для сравнения».

## P2 Issues

### [P2-1] «Анти-патология упрощения» — неестественный термин
**Severity:** P2 (мелкая стилистическая неточность, не блокирует учение).
**Location:** §3.2, line 278.
**Evidence:** «**Важная оговорка (анти-патология упрощения).**»
**Methodology issue:** «Антипатология» в русской медицинской литературе означает «противопоставление патологии» — не «анти-паттерн упрощения». Studen прочтёт как опечатку.
**Recommendation:** Заменить на «**Важная оговорка (против упрощения)**» или «**Важная оговорка: предостережение от упрощения**».

### [P2-2] GPT-4 emb 12288 dim приведён в основном теле, а не softer-phrasing'ом по plan §9
**Severity:** P2 (freshness/source-trust risk).
**Location:** §2.1, line 191.
**Evidence:** «Внутренний эмбеддинг токенов в GPT-4 (по архитектурным утечкам): около 12288 измерений [FACT-CHECK: cadence yearly; source = leak, точная цифра не подтверждена OpenAI].»
**Plan stance:** plan §9 для этой строки помечено «mark `[FACT-CHECK]` + softer phrasing». Chapter ставит `[FACT-CHECK]` корректно, но число 12288 фигурирует в основном перечне рядом с подтверждёнными `1536`/`3072` без визуальной дифференциации (например, отдельной строкой курсивом или в footnote-skinned параграфе).
**Methodology issue:** Студент, не дочитав до `[FACT-CHECK]`-маркера, может запомнить цифру 12288 как факт того же ранга, что и 1536/3072. Mild over-anchoring.
**Recommendation:** Перенести строку из bullet-списка в полноценный параграф ниже: «У внутренних embedding-таблиц больших LLM (например, GPT-4) размерности по различным архитектурным утечкам оцениваются в диапазоне 10–15 тысяч — это **неподтверждённая** оценка, и точная цифра OpenAI не публикуется» — то есть тон «диапазон по утечкам», а не «12288 как число».

### [P2-3] §1.1 inline poll «сильнее → 1/2/3 токена?» в chapter передан только как «полезное упражнение», без формат-маркера
**Severity:** P2 (методический сигнал слабоват для self-study).
**Location:** §1.1, line 112.
**Evidence:** «Полезное упражнение: попробуйте сами угадать, на сколько токенов разрежется слово `сильнее`…»
**Methodology issue:** plan §7 — «s05 inline poll, 15 сек, "как бы вы разрезали `сильнее` — 1, 2 или 3 токена? Почему?"» — это lecture-time retrieval moment. В chapter (book-format, self-study mode) это можно сделать сильнее: явно поставить выбор из 3 вариантов, и затем дать ответ через 1 параграф (retrieval practice). Сейчас вопрос задан как «попробуйте угадать», но ответа («сильнее обычно разрезается на 2-3 токена в современных токенизаторах») в тексте дальше нет.
**Recommendation:** Добавить в конец параграфа явный ответ с одним предложением: «Для большинства современных русскоязычных токенизаторов `сильнее` режется на 2-3 токена (например, `[силь][нее]` или `[си][ль][нее]`); точный результат проверяется на Tiktokenizer».

### [P2-4] §3.2 «маленькое упражнение для проверки интуиции» — тоже без ответа в тексте
**Severity:** P2 (та же модель — retrieval без resolution).
**Location:** §3.2, line 280.
**Evidence:** «Маленькое упражнение для проверки интуиции: куда смотрит модель в предложении "Программа упала, потому что **она** забыла обработать null"? Здесь та же грамматическая неопределённость…»
**Methodology issue:** Хорошо, что вопрос есть; но self-study reader, выполнив retrieval, не получает обратной связи внутри chapter. Reader-simulator текстовый режим может flag это отдельно (orphan question).
**Recommendation:** Добавить 1-2 предложения резолюции: «На большинстве современных моделей attention в этом предложении даёт максимум на `программа` (грамматически «она» по согласованию рода), но есть нетривиальные модели, где вес распределится между `программа` и `обработать` — это нормальная вариативность.»

### [P2-5] §4.2 краткое определение «логиты» — inline, но без подсветки
**Severity:** P2.
**Location:** §4.2, line 359.
**Evidence:** «Технически температура — это коэффициент, на который делят логиты перед softmax (логиты — внутренние "сырые" оценки вероятностей до нормализации); делать формулу здесь не будем, важно следствие.»
**Methodology issue:** Disambiguation in-line, но «логиты» — новый термин для introductory student, и он появляется только один раз. Студент, читающий бегло, может пропустить определение.
**Recommendation:** Минимум — перевести «логиты» в `курсив` или **bold** при первом появлении. Альтернатива — вынести в callout-блок «Что такое логиты?».

### [P2-6] §3.1 уровень детализации multi-head — на грани forbidden-addition #11
**Severity:** P2 (на границе).
**Location:** §3.1, line 271.
**Evidence:** «В реальной модели механизм внимания устроен сложнее: в каждом слое работает не один, а **несколько параллельных "голов" внимания** (multi-head attention; типично 32–128 голов в современных моделях), и каждая голова смотрит на свой аспект — кто-то ловит грамматические связи, кто-то семантические, кто-то длинные дальнодействующие зависимости. Слоёв в современной модели — десятки и сотни.»
**Plan constraint:** §6 #11: «Multi-head attention deep-dive (s14 speaker note only, 1 предложение).» В chapter это полноценный параграф с числовыми оценками и тремя примерами (грамматические / семантические / длинные зависимости).
**Methodology issue:** Chapter — длиннее слайдов, и расширение здесь оправдано. Но три семантических примера могут вылиться при derivation в slide notes в overload. Технически разрешено для chapter (forbidden — на slides), но maintenance riskо.
**Recommendation:** Оставить параграф, но в derived speaker note s14 явно держать только: «multi-head attention — несколько параллельных голов; типично 32-128 в современных моделях; детали — Лекция 17 / доп.чтение».

### [P2-7] §5.5 «бесплатный, T-slider есть в UI» — `[VERIFY-DAY-OF]` присутствует но цитата немного длинная для self-study
**Severity:** P2.
**Location:** §5.5, line 530.
**Methodology issue:** Параграф про HF Inference Playground содержит много specific tool names с verify-day-of caveat. Self-study reader, читая главу через 3-6 месяцев после лекции, может встретить устаревшую информацию.
**Recommendation:** Добавить в конец параграфа дополнение: «Если упомянутые конкретные сервисы окажутся недоступны на момент чтения, общий критерий выбора: любой playground с явным T-параметром и стабильным открытым доступом».

## LO coverage matrix

| LO | Sections | Adequate? | Note |
|----|----------|-----------|------|
| **LO1** (4 этапа inference) | Введение, §1.1, §2.1, §3.1, §4.1, §5.1 (recap) | ✓ | Каждый этап — отдельный раздел; §5.1 содержит recap-таблицу «этап → следствие». Strong coverage. |
| **LO4** (4 ручки API под сценарий) | §4.2 (температура), §4.3 (явная teaching-таблица 4 ручки × 4 сценария), §5.5 (ДЗ apply) | ✓ | §4.3 — настоящий teaching-slide (не recap), с обоснованием каждой строки таблицы. Strong. |
| **LO6** (3 ограничения от архитектуры) | §1.3 (слепота к буквам — explicit «LO6»), §3.3-§3.4 (контекстное окно + lost-in-middle), §4.2 (стохастичность T>0) | ✓ | Все три ограничения покрыты явно с инженерным следствием. |
| **LO7** (3 «почему» через механизм) | §3.2 (role-attention), §1.3 (буквы-токенизатор), §4.2 (T-сэмплинг), §5.2 (explicit payoff card) | ✓ | §5.2 — explicit payoff структура, по одному параграфу на «почему», с softer-phrasing-оговорками. Strong. |

**Cumulative:** All 4 LOs явно заявлены в §«Учебные цели», покрыты в основном тексте, подытожены в §5.1-§5.2, повторены в self-check вопросах каждого раздела. LO1 и LO4 — на уровне Apply (студент описывает / подбирает); LO6 и LO7 — на уровне Understand/Apply (студент объясняет механизм / приводит кейс). Подходит для introductory level.

## Curriculum relevance per section

| Section | Bloom level | Verdict | Note |
|---------|-------------|---------|------|
| §1.1 Что такое токен | Remember/Understand | **KEEP** | Foundational; necessary для всего остального. |
| §1.2 BPE как компромисс | Understand | **KEEP** | Объясняет mechanism без deep-dive в формулы. |
| §1.3 Почему AI плохо считает буквы | Understand/Apply | **KEEP** | Mechanism-grounded explanation; LO6 + LO7 anchor. |
| §1.4 Cross-language unfairness | Understand/Apply | **KEEP** | Engineer-relevant; cost-impact явно. |
| §2.1 Что такое эмбеддинг | Remember/Understand | **KEEP** | Foundational. |
| §2.2 Sentence similarity | Understand/Apply | **KEEP** (но P1-3 fix) | Word2Vec пассаж см. P1-3. |
| §2.3 3 применения | Understand | **KEEP** | Сразу даёт практический рамку для эмбеддингов. |
| §2.4 Semantic vs full-text | Understand/Apply | **KEEP** | Bridge к Лекции 3 RAG. |
| §3.1 Что такое attention | Understand | **KEEP** | Метафора «фонарик» удержана. |
| §3.2 Worked example + role-effect | Understand/Apply | **KEEP** | LO7 first «почему». Softer phrasing на месте. |
| §3.3 Контекстное окно | Understand | **KEEP** | Углубляет Lec-1 §3.3.1 (стоимость attention квадратична). |
| §3.4 Lost in the middle | Understand/Apply | **KEEP** | Engineer-actionable. |
| §4.1 Распределение вероятностей | Understand | **KEEP** | Foundational для §4.2. |
| §4.2 Температура + top-p/k | Understand/Apply | **KEEP** | LO7 third «почему». |
| §4.3 4 ручки API | Apply | **KEEP** | LO4 teaching-slide. |
| §4.4 Авторегрессионная генерация | Understand | **KEEP** | Связывает все 4 этапа в цикл; уточняет Lec-1 §3.2. |
| §4.5 Local vs cloud | Understand | **KEEP** (cross-cutting frame, не повтор Lec-1 §4.2) | Callback only — на месте. |
| §5.1 4 этапа сложились | Remember/Understand | **KEEP** | Recap. |
| §5.2 3 ответа на 3 «почему» | Understand | **KEEP** | LO7 payoff. |
| §5.3 ML vs LLM decision tree | Apply/Analyze | **REVIEW → KEEP** | Bloom-level Apply/Analyze для introductory — на верхней границе, но decision tree упрощён до 3-4 веток без deep dive в trade-offs; защитимо. |
| §5.4 Attention ≠ понимание | Understand | **KEEP** | Callback к Lec-1 §4.8 — properly framed. |
| §5.5 Задание + мост к Лекции 3 | Apply | **KEEP** | Apply задание, понятный мост. |

**Curriculum verdict:** Ни одна секция не overshoots для introductory level. §5.3 ML vs LLM decision tree — единственная, где Bloom-level Analyze, но содержание упрощённое (4 правила), и Decision matrix для introductory допускает «Analyze REVIEW» — здесь верифицировано как «упрощённое, KEEP».

## Cross-reference Lec-1 audit

| Cross-ref (chapter) | Type | Verified callback only? |
|---|---|---|
| Лекция 1 §1.3 (LLM, трансформер, self-attention существуют) | Reference | ✓ — 1 строка в Введении line 79, не повтор |
| Лекция 1 §1.4 (задача × модальность) | Extends (decision tree ML vs LLM в §5.3) | ✓ — расширяет, не повторяет (line 492) |
| Лекция 1 §2.2 (MCP) | Reference | ✓ — 1 строка в §5.5 line 541 (мост к Лекции 3) |
| Лекция 1 §3.2 (stateless inference) | Extends (§4.4 + §1 introduction) | ✓ — расширяется через autoregressive loop; «теперь не чёрный ящик» framing корректен (line 465) |
| Лекция 1 §3.3 (цикл чата) + §3.3.1 (контекстное окно) | Reference | ⚠ См. P1-2 — точная цитата ссылается на §3.3.1, but phrase лежит в §3.3 |
| Лекция 1 §3.4.1 (agent architecture) | Reference | ✓ — 1 строка в §5.5 line 542 (мост к Лекции 3 agent loop) |
| Лекция 1 §4.2 (local vs cloud) | Callback (§4.5) | ✓ — callback only, "глубже там же" framing (line 442) |
| Лекция 1 §4.8 (Pearl 3 уровня) | Callback (§5.4) | ✓ — callback only; «теперь у нас есть механистическое основание для этого тезиса» framing работает (line 506) |
| Лекция 1 §5.3 (3 «почему») | Payoff (§5.2) | ✓ — explicit payoff, mechanism-grounded; softer-phrasing-оговорки на каждом «почему» (lines 481-485) |
| Лекция 12 PARTS (через Lec-1 §3.3) | Forward-reference | ✓ — 1 строка в §3.2 line 292 |

**Cross-ref verdict:** 9 из 10 ссылок — clean callbacks или explicit extensions. Одна несоответствие — P1-2.

**Глагол «callback» используется в нужном смысле:** не повтор содержания, а ссылка на предыдущую секцию + новая надстройка. Это правильное chapter-to-chapter поведение.

## Glossary lock + Forbidden additions check

### Glossary lock (plan §5, 17 терминов)

| Term | Plan canonical | Chapter usage | Status |
|---|---|---|---|
| токен | токен | ✓ throughout | OK |
| токенизация | токенизация | ✓ throughout | OK |
| BPE | BPE (Byte-Pair Encoding) | ✓ §1.2 расшифровка 1×, далее BPE | OK |
| эмбеддинг | эмбеддинг (+ «векторное представление» 1×) | ✓ §2.1 line 183 — disambiguation 1× | OK |
| семантическое сходство | семантическое сходство (+ similarity 1×) | ✓ | OK |
| cosine similarity | cosine similarity (LOCKED каноничный) | ✓ §2.2 throughout; «косинус угла» — formal explanation 1×, не как термин-замена | OK |
| механизм внимания | механизм внимания | ✓ throughout; «внимание» допустимо 1× после introduction; «attention» 1× в скобках в §3.1 | OK |
| контекстное окно | контекстное окно | ✓ throughout | OK |
| сэмплинг | сэмплинг (+ «выбор следующего токена» 1×) | ✓ throughout | OK |
| температура | температура | ✓ throughout; (T) — alias допустим | OK |
| top-p (nucleus sampling) | top-p (nucleus sampling) | ✓ §4.2 line 369 расшифровка | OK |
| top-k | top-k | ✓ | OK |
| max_tokens | `max_tokens` | ✓ | OK |
| авторегрессионный | авторегрессионный LOCKED | ✓ §4.4 line 414 + терминологическая заметка line 431 — explicit canonical lock | **EXCELLENT** |
| распределение вероятностей | распределение вероятностей | ✓ throughout | OK |
| **слепота к буквам** | слепота к буквам (рабочий) + subword-агрегация alias | ✓ §1.3 line 134 — disambiguation as planned | OK |
| Перла (имя) | Перла (Lec-1 canonical) | ⚠ Two forms — see P1-1 | **FAIL** |

**Glossary verdict:** 16/17 — OK. Единственный fail — Pearl name (P1-1).

### Forbidden additions check (plan §6, 17 пунктов)

| # | Forbidden item | Verified absent? |
|---|----------------|------------------|
| 1 | Формулы attention softmax(QK^T/√d) | ✓ — §3.1 line 271 explicitly «детальный технический разбор … выходит за рамки этой главы» |
| 2 | Q/K/V как термины | ✓ — упомянуты в Введении line 77 в списке «оставляем за пределами» (правильное framing) |
| 3 | Архитектурная диаграмма transformer block | ✓ — упомянута в §Введение line 77 как «вне scope» |
| 4 | Глубокий разбор позиционного кодирования | ✓ — упомянуто 1 раз в Введении line 77 «вне scope» |
| 5 | Pretraining / fine-tuning / RLHF deep dive | ⚠ — RLHF упомянут в §3.2 line 292 (1 предложение alt explanation) + в §5.2 line 481; не deep-dive. OK |
| 6 | CNN vs RNN vs Transformer | ✓ |
| 7 | Karpathy mini-GPT | ✓ — упомянут только в «Дальнейшее чтение» |
| 8 | Footer-tax на слайдах | n/a для chapter |
| 9 | «Вы здесь» / «Лектору» | ✓ |
| 10 | Slide-delete/add без user | n/a для chapter |
| 11 | Multi-head deep-dive | ⚠ См. P2-6 — на границе, но в chapter допустимо |
| 12 | Word2Vec king-queen central | ⚠ См. P1-3 |
| 13 | Pearl 3 уровня deep-dive | ✓ — §5.4 — callback, без deep-dive (~150 слов про корреляция vs каузальность) |
| 14 | Color-only highlight | n/a для chapter |
| 15 | Decorative SVG без semantic | n/a для chapter |
| 16 | Cross-slide bridge «как мы видели на s10» | ✓ — chapter использует §-references (§1.4, §2.3), не slide-references |
| 17 | «Section-NN» footer markers | n/a |

**Forbidden additions verdict:** 14/17 fully clean; 2 на границе (P2-6 multi-head, P1-3 Word2Vec); 1 n/a. No actual violation.

### Anti-pattern grep (notes/decisions.md 2026-05-13 items 16-35)

| Anti-pattern | Result |
|---|---|
| «промптинг — сквозной навык» | ✓ ABSENT (replaced per plan §8.2 P1-6 fix) |
| «AI спасёт» / «революция» | ✓ ABSENT |
| «магия LLM» / «магическая пилюля» | ✓ ABSENT — «магия» появляется 1 раз в §1.2 line 125 в негации «токенизация — не магия» — корректно |
| «УГАДАЙ» / «ребят» / «короче» | ✓ ABSENT |
| «инженер ИУ6» / «студент Бауманки» | ✓ ABSENT |
| «рабочее определение» (без context) | ⚠ В §1.3 line 134: «"слепота к буквам" (рабочий термин; в литературе встречается также "subword-агрегация")» — это **разрешённый** случай: explicit dictionary disclaimer + canonical alternative «subword-агрегация» предоставлен. Plan §5 explicitly allows this combo. OK |
| Custom-coined terms без literature | ✓ — все custom phrases sourced или disclaimer'ом |
| Specific numbers без source | ⚠ §2.2 cosine similarity numbers — explicit `[FACT-CHECK]` line 212; §1.4 token-per-char — explicit `[FACT-CHECK]` line 108; §3.3 context window 4k/200k/1M — explicit `[FACT-CHECK]` line 299. All flagged. OK |

**Anti-pattern verdict:** No anti-pattern violations.

## Counter-check

**Counter-check rule (.claude/agents/methodology-critic.md):** «If ≥5 P1 issues but verdict = APPROVE-WITH-POLISH — STOP, change to REVISE.»

**Actual count:** P1 = 4 (P1-1 Pearl drift, P1-2 §3.3.1 reference error, P1-3 Word2Vec width, P1-4 апельсинов calque). 4 ≤ 4 → APPROVE-WITH-POLISH consistent.

**DoD enforcement:**
- Chapter length: 10,148 words ✓ (within 5k-15k)
- All sections present: Введение, Учебные цели, Раздел 1-5, Источники, Дальнейшее чтение ✓
- Sources inline `(Автор, Год)` ✓ (Sennrich 2016, Vaswani 2017, Mikolov 2013, Holtzman 2019, Liu 2023, Pearl 2018, Lewis 2020, Yao 2022 — all present)
- Self-check в конце каждого раздела ✓ (4 разделов × 3-4 вопроса)
- LO явно в §«Учебные цели» ✓
- `[for-slide-sNN]` markers — 28 markers, по 1+ на каждый из 28 слайдов ✓ (s01-s28 monotonic, no gaps)
- Glossary lock 16/17 ✓ (1 fail = P1-1)
- All DoD metrics meet except glossary Pearl name → P1-1 noted. Not DoD-blocking.

## Топ-приоритизированные правки

В порядке приоритета:

1. **[P1-1]** Унифицировать «Перла» (без ё) на line 506 (§5.4) — match Lec-1 canonical. 1-line fix.
2. **[P1-2]** Заменить «§3.3.1» на «§3.3» в §4.3 line 386 (точная цитата «следствие 1» живёт в §3.3, не §3.3.1). 1-line fix.
3. **[P1-3]** §2.2 Word2Vec passage: сократить до 1 предложения или убрать explicit equation «король - мужчина + женщина ≈ королева» (lines 201-202). 2-3 lines edit.
4. **[P1-4]** §5.5 line 530: заменить «unified апельсинов-к-апельсинам сравнения» на «одинакового основания для сравнения» (или эквивалент). 1-line fix.
5. **[P2-2]** §2.1 GPT-4 12288 dim: переместить из bullet-списка в отдельный параграф с «диапазон по утечкам» framing (line 191). 2-3 lines reword.
6. **[P2-3]** §1.1 line 112: добавить explicit ответ-resolution на упражнение «сильнее». 1 sentence add.
7. **[P2-4]** §3.2 line 280: добавить resolution на упражнение «Программа упала, потому что она…». 1-2 sentence add.
8. **[P2-1]** §3.2 line 278: заменить «анти-патология упрощения» на «против упрощения» / «предостережение от упрощения». 1-line fix.
9. **[P2-5]** §4.2 line 359: подсветить «логиты» курсивом или вынести в callout. 1-line fix.
10. **[P2-7]** §5.5 line 530: добавить fallback-criterion в конце параграфа. 1 sentence add.
11. **[P2-6]** §3.1 multi-head параграф: оставить как есть, но в derived speaker note s14 убедиться, что не разрастается. Note for downstream phase, not chapter edit.

**Estimated edit time:** 30-45 минут на все 11 правок. После правок повторный methodology re-check не требуется (P1 → P2 либо clean); fact-checker делает свою прогонку независимо.

---

**End of methodology-critic report v1, Phase 3.**

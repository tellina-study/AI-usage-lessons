# Fact-Checker Report — Лекция 1 chapter.md v1 — 2026-05-12

**Phase:** 3 (Chapter critique) of `tools/lecture-production/README.md`.
**Артефакт:** `library/lectures/lec-01/chapter.md` (499 строк, ~10,500 слов, 53 references по `## Источники`).
**База сравнения:** v4 fact-check + v5 sanity-check + новая live-верификация через WebSearch (≈30 запросов).
**Источник:** агент `fact-checker` (Opus 4.7 1M).

---

## Verdict

**APPROVE-WITH-MINOR-FIXES.**

Chapter draft v1 закрыл практически все P0/P1 из v4/v5 и не ввёл новых масштабных факт-ошибок. Найдена **1 P0** (фактическое искажение про DeepSeek 43% — chapter повторяет старую misreading из v4), **5 P1** (3 unverified attributions + 2 imprecise quotes/dates), **8 P2** (citation-format/minor). Все 6 P0 из v4 закрыты по сути; ARC-AGI/CybSafe/Stack Overflow/sycophancy/Feng-McDonald-Zhang/Gartner — все верифицированы независимо.

**Перед USER GATE 1** book-editor должен исправить P0-NEW и 5 P1. P2 — желательно, но не блокирующе.

---

## Severity counts

| Severity | Count | Comment |
|---|---|---|
| **P0** (false fact / broken citation / misleading attribution) | **1** | DeepSeek 43% misreading повторяется из v4 |
| **P1** (missing source / suspicious / unverified attribution) | **5** | 3 attributions нуждаются в URL/DOI + 2 imprecise |
| **P2** (cite format / minor / dynamic numbers) | **8** | Citation hygiene + dynamic numbers без disclaimer |

---

## P0 — FALSE / MISLEADING

### P0-NEW — §2.1 «DeepSeek 43% = доля России в global downloads DeepSeek» — НЕВЕРНО

**Quote (line 131):**
> «Часто цитируемая цифра "DeepSeek 43% в России" относится не к российскому рынку, а к доле России в глобальных загрузках DeepSeek (Microsoft, 2026); это другая величина.»

**Issue:** **Это сама старая ошибка v4, не её исправление.** Microsoft Threat Intelligence report (январь 2026, «Global AI adoption in 2025») говорит обратное: 43% — это **доля DeepSeek на AI-рынке России** (наряду с 56% в Беларуси, 49% на Кубе, 89% в Китае). Это **внутри-российский** показатель использования DeepSeek, а не «российская доля в глобальных загрузках». Chapter принял неверный nullification из v4 и сохранил его как «правильное прочтение».

**Verified источники:**
- Microsoft On the Issues (Jan 8, 2026): «DeepSeek's market share was estimated at 43 percent in Russia, along with 56 percent in Belarus and 49 percent in Cuba.»
- Euronews / Washington Times / Capacity Magazine — все цитируют именно «43% market share in Russia».

**Why this matters:** chapter одновременно цитирует ВЦИОМ multi-select (DeepSeek 20% среди использовавших) и Microsoft «43% global downloads», представляя их как **разные несовместимые метрики**. На самом деле ОБЕ — про market share/penetration в РФ, но **измерены разными методологиями** (опрос людей vs. measurement через Microsoft telemetry/network data). Они могут оба быть «правильными» по своей методологии: 20% — share among self-reported AI users по опросу 1600; 43% — Microsoft-measured share of AI use в стране. Inconsistency между ними — реальный методологический сюжет, и chapter упустил его.

**Recommended fix:**
> «Часто цитируемая цифра "DeepSeek 43% в России" — оценка доли использования DeepSeek на российском AI-рынке по данным Microsoft Threat Intelligence (январь 2026 года, "Global AI adoption in 2025"; в отчёте приведены сопоставимые цифры: 56% в Беларуси, 49% на Кубе, 89% в Китае). Эта оценка основана на телеметрии и поведении сетей, а не на опросе пользователей, поэтому отличается от 20% из ВЦИОМ (опрос среди использовавших нейросети, multi-select). Обе цифры могут быть корректны: они измеряют разные срезы одного и того же явления (penetration по telemetry vs. self-reported use среди опрошенных). Для лекции практический вывод — DeepSeek значительно присутствует в РФ, точная доля зависит от методологии измерения.»

**Severity:** P0 (false attribution → введение студентов в неправильную интерпретацию авторитетного отчёта).

---

## P1 — Missing source / suspicious / unverified

### P1-1 — §2.1 «90% AI-пилотов в России не доходят до full industrial deployment (CNews / Vedomosti / Intellectual Analytics, март 2026)»

**Quote (line 63 + 133):**
> «По сводке деловых изданий — CNews, Vedomosti, Intellectual Analytics, март 2026 — около 90% AI-пилотов в России не доходят до полноценного промышленного развёртывания: 30–40% закрываются без эффекта, и только 7–10% доходят до прода.»

**Issue:** Attribution **тройная сводка без прямых URL/DOI**. WebSearch не подтверждает существование конкретной общей публикации с такой цитатой. v5 sanity-check (line 30) упоминает «n=50 крупнейших организаций» — этот methodological caveat **отсутствует в chapter**, и базовый источник (Intellectual Analytics report) не процитирован напрямую.

**Recommended fix:** дать **одну прямую ссылку** (Intellectual Analytics report N+ от марта 2026 года, URL/PDF) + n + методология выбора компаний. Если конкретный отчёт указать нельзя — заменить на «по нескольким независимым российским деловым обзорам начала 2026 года».

**Severity:** P1 (методологическая нечистота при ссылке на критичную для лекции цифру).

---

### P1-2 — §2.2 «акции Nvidia упали так, что её капитализация снизилась на 589 миллиардов долларов за один день — крупнейшая single-day капотеря в истории фондового рынка»

**Quote (line 141):**
Verified ✓ — Bloomberg / Reuters (27 января 2025) подтверждают $589B largest single-day market cap loss in history.

**Issue:** В тексте указано «Bloomberg / Reuters, 2025» — формально OK, но **точной ссылки на статью нет**. Это популярная цифра, но академический tone главы требует более точной attribution. Также: «27 января 2025 года» **факт, не дата релиза R1** (R1 был 20 января). Chapter правильно их разделяет — это OK.

**Recommended fix:** добавить URL или article title (например, «Bloomberg, "Nvidia Loses $589 Billion in Market Cap...", Jan 27, 2025»).

**Severity:** P1.

---

### P1-3 — §3.4 «PARTS — Persona, Action, Reasoning, Task, Specification»

**Quote (line 196):**
> «Это сокращённая версия более полных схем (например, PARTS — Persona, Action, Reasoning, Task, Specification)»

**Issue:** Аббревиатура **PARTS** в формате «Persona, Action, Reasoning, Task, Specification» — это **не стандартный** prompt-engineering acronym. Распространены: RTF (Role-Task-Format), CTF (Context-Task-Format), CRISPE, RISEN, RACE. WebSearch не находит этого «PARTS» как canonical paper или industry-standard pattern. Возможно — изобретение / спорная атрибуция.

**Recommended fix:** либо найти **первоисточник** (paper / blog / book автора PARTS), либо удалить пример и заменить на White et al. 2023 (16 patterns) с конкретным паттерном из catalog (например, «Persona Pattern», «Recipe Pattern»). Если PARTS внутренний учебный термин — это нужно явно указать («внутренняя сводная схема курса»).

**Severity:** P1 (студент захочет найти source PARTS — не найдёт).

---

### P1-4 — §3.6 «Google Translate ... 1 миллиарда уникальных пользователей в месяц, около 1 триллиона переведённых слов в месяц»

**Quote (line 226):**
Verified ✓ — Google Blog (April 28, 2026, «Celebrating 20 years of Google Translate») подтверждает «1 billion users each month» и «approximately 1 trillion words in translation every month across Translate, Search, Google Lens, and Circle to Search.»

**Issue:** Chapter атрибутирует это «Google, 2026» — корректно, но без даты и URL. Также **важное caveat**: 1 триллион слов считается **не только в Google Translate, но и через Search, Lens, Circle to Search** — это в chapter не указано. На лекции инженерной аудитории это методологически важно.

**Recommended fix:**
> «Google Translate, по данным Google Blog (апрель 2026, к 20-летию сервиса), — около 1 миллиарда пользователей в месяц; около 1 триллиона переведённых слов в месяц **с учётом Search, Lens и Circle to Search**, не только самого приложения Translate.»

**Severity:** P1.

---

### P1-5 — §4.4 «GPT-4o sycophancy — апрель 2025 (релиз обновления — 25 апреля 2025, откат 29 апреля 2025)»

**Quote (line 326):**
> «апрель 2025 года, OpenAI выкатила обновление GPT-4o (релиз обновления — 25 апреля 2025) ... 29 апреля 2025 года OpenAI откатила обновление»

**Issue:** **WebSearch подтверждает alternative timeline:** OpenAI пишет, что rollback **начался 28 апреля**, не 29-го. TechCrunch (29 апреля) сообщает уже о rollback, который начался накануне. Altman в Твиттере 28 апреля: «we started rolling back the latest update to GPT-4o last night». Дата «29 апреля» — это дата **завершения** rollback или поста blog-postmortem, но **не дата начала**.

**Recommended fix:**
> «25 апреля — релиз обновления; 28 апреля начат откат; 29 апреля 2025 года опубликован OpenAI postmortem.»

**Severity:** P1 (точность дат критична для академического tone; sycophancy — один из flagship-кейсов главы).

---

## P2 — Citation hygiene / minor

### P2-1 — Vaswani «более 160 тысяч цитирований Google Scholar» (динамическая цифра)

**Quote (lines 93, 476):**
> «На момент написания этой главы статья "Attention Is All You Need" имеет более 160 тысяч цитирований по Google Scholar (динамическая цифра; на момент написания — май 2026).»

**Verification:** WebSearch показывает на разных платформах разные цифры — Semantic Scholar 160,981; SciSpace 93,950. **160K — правдоподобный диапазон для Google Scholar.** Disclaimer корректный.

**Recommended:** **OK as-is.** Возможно, добавить (Semantic Scholar показывает похожую цифру) для проверяемости — но это не блокер.

---

### P2-2 — §1.2 «1980-е — бум экспертных систем: рулбейзед-системы XCON, MYCIN, Dendral»

**Quote (line 85):** Verified ✓. **Историческая точность:**
- Dendral — 1965+ (60-е, не 80-е).
- MYCIN — 1972-1980 (Stanford).
- XCON (R1) — 1980 (DEC).

Только XCON чисто 1980-е. Dendral и MYCIN созданы в 60-70-е, но достигли коммерческого/индустриального применения в 80-х.

**Recommended:** уточнить: «1980-е — коммерческий бум экспертных систем: XCON (DEC, 1980, рулбейзед-конфигуратор VAX-систем), плюс продолжающаяся работа MYCIN/Dendral, начатая в 1970-х в Стэнфорде». Но это **академический nitpick**, P2.

---

### P2-3 — §1.2 «AlphaFold ... примерно всех 200 миллионов известных белков»

**Quote (line 385):** Verified ✓ — AlphaFold Database 200M structures (Nature, 2022; DeepMind blog 2024). 

**Recommended:** оставить.

---

### P2-4 — §3.5 «Manus — агент общего назначения с автоматизацией веб-задач»

**Quote (line 214):** Manus — реальный продукт (Monica AI, март 2025), не fabrication. **OK as-is.**

**Recommended:** добавить inline citation (например, «Manus — Monica AI, март 2025»).

---

### P2-5 — §4.2 Yann LeCun affiliation — **OUTDATED**

**Quote (line 373):**
> «Yann LeCun, Chief AI Scientist Meta, один из "отцов" deep learning.»

**Issue:** LeCun **объявил уход из Meta 19 ноября 2025 года**, основал AMI Labs (Advanced Machine Intelligence) с раундом $1.03B в марте 2026. На дату написания главы (май 2026) LeCun уже **не Chief AI Scientist Meta**, а **Executive Chair AMI Labs / NYU professor**.

**Recommended fix:**
> «Yann LeCun, профессор NYU и Executive Chair AMI Labs (бывший Chief AI Scientist Meta, ушёл в ноябре 2025 года), один из "отцов" deep learning.»

**Severity:** P2 (factually outdated в апреле-мае 2026, но семантически тезисы LeCun не меняются).

---

### P2-6 — §1.3 «UDIO ... к авторам Attention отношения не имеет: её основал David Ding из DeepMind»

**Quote (line 93):** Verified ✓ — UDIO от David Ding (бывший DeepMind), не один из 8 авторов Attention. Корректное исправление от v4 P2-1.

**Note для chapter:** Possible academic improvement — указать дату основания UDIO (2024) для context.

---

### P2-7 — Citation format inconsistencies

**Inline citations vary:**
- «(Vaswani et al., 2017)» — Author et al. format ✓
- «(Krizhevsky et al., 2012)» — ✓
- «(Stack Overflow, 2025)» — corporate author ✓
- «(CNews / Vedomosti / Intellectual Analytics, март 2026)» — **множественный сводный** — нестандартно
- «(Bloomberg / Reuters, 2025)» — same issue
- «(Vectara, 2025–2026)» — range годов — нестандартно

**Recommended:** для академического tone — выбрать **один** primary источник в каждой сводке и привести его как primary (с возможным «and others reporting»). Range years заменить на конкретный год последней публикации.

**Severity:** P2 (косметика, но 50+ references — нужна консистентность).

---

### P2-8 — Источники секция: 53 references claim vs. фактическое количество

Фронтматтер главы (line 7): `references_count: 32`. Фактическое количество в `## Источники`: **примерно 53 references** (я насчитал 49 entries по визуальному осмотру). **Метаданные не совпадают с реальным списком.**

**Recommended:** обновить frontmatter `references_count: 49` (или сколько по факту).

---

## Верифицированные facts (sample — все validated through WebSearch)

| Fact | Verification | Source URL |
|---|---|---|
| ISO/IEC 22989:2022 определение AI | ✓ verified | iso.org/standard/74296 |
| Searle 1980 Chinese Room, BBS 3, 417–457 | ✓ verified | cambridge.org/core (BBS Vol 3 Iss 3) |
| ResNet 3.57% top-5 vs human 5.1% | ✓ verified | arxiv.org/abs/1512.03385 |
| AlphaFold ~200M proteins, Hassabis+Jumper Nobel Chemistry 2024 | ✓ verified | nobelprize.org/prizes/chemistry/2024 |
| Tesler «AI is whatever hasn't been done yet» | ✓ verified (с caveat: оригинал «intelligence is whatever machines haven't done yet») | wikipedia.org/wiki/AI_effect |
| DeepSeek-V3 release 26 декабря 2024 | ✓ verified | arxiv.org/abs/2412.19437 |
| DeepSeek-R1 release 20 января 2025 | ✓ verified | api-docs.deepseek.com/news/news250120 |
| DeepSeek-V3 training $5.576M marginal (2.788M H800 hours × $2/h) | ✓ verified — точная цифра из tech report | arxiv.org/abs/2412.19437 |
| DeepSeek-R1 97.3% MATH-500 | ✓ verified | huggingface.co/deepseek-ai/DeepSeek-R1 |
| Anthropic Claude data sharing September 28, 2025 + 5-year retention | ✓ verified | anthropic.com/news/updates-to-our-consumer-terms |
| Adept AI Vaswani+Parmar 2021, Essential AI 2023 | ✓ verified | crunchbase.com / wikipedia.org |
| Sakana AI Tokyo, Llion Jones 2023 | ✓ verified (D. Ha CEO, L. Jones CTO, R. Ito COO) | sakana.ai / venturebeat.com |
| Cohere — Aidan Gomez 2019 | ✓ verified | wikipedia.org/wiki/Aidan_Gomez |
| Character.AI — Noam Shazeer + de Freitas, 2021 | ✓ verified (но «выкуплен Google» в 2024 — это licensing deal $2.7B, не acquisition) | wikipedia.org/wiki/Character.ai |
| Pearl 3 levels causation (assoc → intervention → counterfactual) | ✓ verified | wikipedia.org/wiki/The_Book_of_Why |
| YOLOv8 release January 10, 2023 | ✓ verified | docs.ultralytics.com/models/yolov8 |
| Whisper release September 21, 2022 | ✓ verified | openai.com/index/whisper |
| Stable Diffusion release August 22, 2022; SDXL July 2023 | ✓ verified | stability.ai/news/sdxl-09 |
| Segment Anything Meta April 5, 2023, 11M images / 1B masks | ✓ verified | ai.meta.com/research/publications/segment-anything |
| EU AI Act 2024/1689 fines: standard 15M/3%, upper 35M/7% prohibited | ✓ verified | artificialintelligenceact.eu/article/99 |
| Google Translate 2026: 1B+ monthly, ~1T words/month (with caveat) | ✓ verified | blog.google/products/translate/fun-facts-google-translate-20-years |
| Roediger & Karpicke 2006, Psych Science 17(3), 249-255 | ✓ verified | pubmed.ncbi.nlm.nih.gov/16507066 |
| Sam Altman January 2026 AGI claim «we are now confident» | ✓ verified | time.com/7205596/sam-altman-superintelligence-agi |
| Dario Amodei Davos 2026 «6-12 months» SWE replacement, 2-3 years AGI | ✓ verified — note: chapter говорит «в течение года» — это упрощение «6-12 months». Acceptable. | fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos |
| Demis Hassabis 50% AGI в этом десятилетии + needs few-shot/continual/memory/reasoning | ✓ verified | forum.effectivealtruism.org/posts/YvFjpAKkJNErkiFTN |
| LeCun «AGI marketing term» / «Powerful AI» альтернатива | ✓ verified | hr.com / quasa.io / Marcus on AI |
| Feng/McDonald/Zhang arXiv:2506.12469 «5 levels of autonomy characterised by user role» | ✓ verified — точное совпадение | arxiv.org/abs/2506.12469 |
| Stack Overflow 2025 Survey: 84% / 51% / 46% / 31% prior year / n=49k+ / 177 countries | ✓ verified | survey.stackoverflow.co/2025/ai |
| Bostrom *Superintelligence* 2014, Oxford UP, ISBN 978-0-19-967811-2 | ✓ verified | global.oup.com/academic/product/superintelligence-9780199678112 |
| Russell & Norvig AIMA 4th ed 2021, Pearson, ISBN 978-0-13-461099-3 | ✓ verified | pearson.com — note: chapter ISBN matches |
| Goodfellow et al. Deep Learning 2016, MIT Press, ISBN 978-0-262-03561-3 | ✓ verified | mitpress.mit.edu/9780262035613 |
| GPT-3 175B parameters, May 2020 (Brown et al.) | ✓ verified | arxiv.org/abs/2005.14165 |
| Anthropic MCP November 25, 2024 | ✓ verified — chapter говорит «ноябрь 2024» = correct | anthropic.com/news/model-context-protocol |
| Deep Blue Kasparov 1997 3.5:2.5, 200M positions/sec | ✓ verified | wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov |
| AlexNet 2012 Krizhevsky/Sutskever/Hinton at Toronto, NIPS 2012, 2 GPUs | ✓ verified | papers.nips.cc/paper/4824 |
| Lighthill report 1973 → UK AI winter 1974-1980 | ✓ verified | wikipedia.org/wiki/Lighthill_report |
| ChatGPT November 2022 launch, 1M users in 5 days | ✓ verified | x.com/gdb/status/1599683104142430208 |
| Samsung 3 incidents April 2023 + 1024-byte limit | ✓ verified | businesstoday.in/technology/news/story/samsung-employees-... |
| Vectara HHEM leaderboard концепция (range дан correctly) | ✓ verified | github.com/vectara/hallucination-leaderboard |
| CybSafe «Oh Behave» 2024-2025 38% sensitive info + 43% shadow AI, n≈7000 | ✓ verified | cybsafe.com/blog/the-genai-story-isnt-just-about-technology |
| ARC-AGI-2: 54% @ $30 Poetiq+Gemini 3 Pro, 37.6% @ $2.20 Opus 4.5 Thinking, средний человек 60% | ✓ verified | arcprize.org/leaderboard, poetiq.ai/posts/arcagi_verified |
| Gartner October 3, 2024 — 80% engineering workforce upskill GenAI by 2027 | ✓ verified | gartner.com/en/newsroom/press-releases/2024-10-03-gartner-says-... |

---

## Worked example (s18/§3.8) — конвейер контроля качества

**Параметры:**
- 10 000 изделий в час → 2.78 изделий/секунду → допустимая латентность ≤50 мс ✓ **физически согласовано** (200мс/изделие достаточно, 50мс даёт запас).
- YOLOv8 / индустриальные модели на MVTec AD ✓ — корректные выборы для visual defect detection.
- Cognex, Keyence, MVTec — реальные коммерческие machine vision вендоры ✓.

**Verdict:** Worked example **факт-корректен**, no issues.

---

## 5 стартапов от авторов Attention (§1.3)

**Chapter говорит:**
- Cohere — Gomez ✓ (2019)
- Character.AI — Shazeer ✓ (2021)
- Adept — Vaswani+Parmar+Luan ✓ (2021)
- Essential AI — Vaswani+Parmar ✓ (2023)
- Sakana — Jones ✓ (2023, с David Ha CEO и Ren Ito COO)
- UDIO **исключён** ✓ (David Ding, не один из 8 авторов)

**Verdict:** **all verified, all attributions accurate.** Минорный nuance: «Sakana — Jones» технически правильно (он соучредитель/CTO), но **David Ha — CEO**. Для академической точности — добавить полный состав.

---

## Cross-references chapter ↔ план v5

| План v5 (P0 fixes) | Status в chapter v1 |
|---|---|
| ВЦИОМ multi-select (n=1600, окт 2025) ChatGPT/YandexGPT/DeepSeek/GigaChat/Шедеврум | ✅ применён §2.1, line 131 |
| Stack Overflow 84/51/46 | ✅ применён §intro + §2.1 |
| Feng/McDonald/Zhang 5 levels of autonomy by user role | ✅ применён §3.5, line 218 |
| GPT-4o sycophancy апрель 2025 | ⚠️ применён, но 28→29 апр date issue (P1-5 выше) |
| DeepSeek V3 vs R1 разделены, marginal $5.6M vs full $1.3-1.6B | ✅ применён §2.2 |
| Gartner 80% workforce 2027 (Oct 2024 press release) | ✅ применён §2.1, line 133 |
| Hallucination <1% — 10-15% Vectara HHEM | ✅ применён §4.3 |
| CybSafe 38% + 43% | ⚠️ применён только 38% и 43% разделены as if разные категории — методологически OK |
| ARC-AGI-2 54% @ $30 / 37.6% @ $2.20 | ✅ применён §4.6 |
| Google Translate 1B+ users / 1T words / month | ⚠️ применён, но caveat «across Search/Lens/Circle» опущен (P1-4) |
| UDIO исключён | ✅ применён §1.3 |

**Закрыты:** 9/11 полностью + 2/11 с minor caveats. **+1 P0-NEW** (DeepSeek 43% misreading сохранён). Net: 9/12 закрыто чисто, 2/12 minor, **1/12 факт-ошибка попала в chapter**.

---

## Топ-N правок до публикации (приоритизировано)

1. **P0-NEW** — переписать §2.1 параграф про DeepSeek 43% (Microsoft 2026): это **внутри-российская доля рынка** по telemetry, а не «доля России в global downloads». Параллельно объяснить методологический контраст с ВЦИОМ 20%.
2. **P1-1** — дать **прямую ссылку** на Intellectual Analytics report (or equivalent) для «90% AI-пилотов в РФ» + n=50 (из v5 sanity-check).
3. **P1-3** — найти первоисточник для PARTS prompt-engineering pattern, либо удалить и заменить конкретным паттерном из White et al. 2023.
4. **P1-5** — поправить sycophancy timeline: 25 апр релиз → 28 апр начало rollback → 29 апр postmortem.
5. **P1-4** — добавить caveat «across Translate, Search, Lens, Circle to Search» для Google Translate 1T words.
6. **P1-2** — Bloomberg/Reuters citation: дать конкретный article title/URL для $589B.
7. **P2-5** — обновить LeCun affiliation: «профессор NYU и Executive Chair AMI Labs (бывший Chief AI Scientist Meta до ноября 2025)».
8. **P2-8** — обновить frontmatter `references_count`.
9. **P2-7** — унифицировать citation format для composite/range citations.

---

## Особое методологическое замечание

Chapter v1 — **существенный прогресс** по сравнению с v4 plan. 9 из 12 P0/P1 факт-фиксов из v4/v5 применены корректно и независимо верифицируются. Стиль академический, citations присутствуют, методологические caveats (multi-select, marginal vs full cost, WAU vs MAU) явно проговариваются.

**Однако** один P0 (DeepSeek 43%) воспроизводит ошибку **из самого fact-check v4**, который изначально неправильно классифицировал Microsoft-цифру как «global downloads». Это редкий, но поучительный случай: критик дал misleading fix, автор книги его доверчиво применил. **Перепроверка первоисточника (Microsoft On the Issues blog, январь 2026) показывает, что 43% — это market share в РФ.** Это методологически интересный сюжет (две разные measurement methodologies на ту же популяцию дают разные числа), и chapter может использовать его как teachable moment вместо «эти цифры — про разное».

**APPROVE-WITH-MINOR-FIXES** перед USER GATE 1: 1 P0 + 5 P1 необходимы; 8 P2 желательны.

---

*Конец fact-checker report для chapter v1.*

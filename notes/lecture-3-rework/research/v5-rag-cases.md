# v5 — Типичные, реальные RAG-кейсы (для слайдов-примеров + speaker notes)

**Дата:** 2026-09-15
**Задача:** Дать конкретные, преподаваемые примеры RAG-задач (сейчас в деке не хватает concrete RAG task examples). Каждый кейс = задача → устройство retrieval → что делает её трудной → типичный провал → как хорошая реализация чинит → baseline/counterfactual.
**Правило меток:** где деталь взята из источника — стоит ссылка; где деталь придумана для наглядности — помечена **(иллюстративный)**.

---

## Опорная цифра всей лекции (anchor)

Anthropic (инженерный блог, «Contextual Retrieval») даёт полную лесенку улучшений на одной задаче ретрива — это единый количественный якорь для слайдов про chunking / hybrid / rerank:

| Дизайн retrieval | Доля **проваленных** ретривов (top-20 не содержит нужного) |
|---|---|
| Базовые embeddings (naive dense) | **5.7 %** |
| + контекстуализация чанков (Contextual Embeddings) | 3.7 % (−35 %) |
| + гибрид с BM25 (Contextual Embeddings + BM25) | 2.9 % (−49 %) |
| + реранкер (cross-encoder поверх) | **1.9 % (−67 %)** |

Дополнительно из того же источника (пригодится как факты для нот):
- Оптимально извлекать **top-20** чанков (тестировали 5/10/20 — 20 лучший).
- Контекст к чанку — **50–100 токенов**; стоимость его генерации с prompt caching **$1.02 / 1M токенов документов** (разово).
- Порог «RAG вообще не нужен»: если база **< 200 000 токенов (~500 страниц)** — просто положи всю базу в промпт, RAG не нужен.

Источник: [Anthropic — Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval).

> Преподавательский вывод одной строкой: **naive dense-RAG проваливает ретрив ~40 % времени** по данным практиков ([kapa.ai, «RAG Best Practices»](https://www.kapa.ai/blog/rag-best-practices); [Towards Data Science, «Hybrid Search and Re-Ranking»](https://towardsdatascience.com/hybrid-search-and-re-ranking-in-production-rag/)) — три приёма (контекст чанка + гибрид + rerank) закрывают большую часть этого.

---

## Кейс A — Ассистент поддержки / внутренней базы знаний (customer support / internal KB)

**Задача.** Пользователь (клиент или сотрудник) задаёт вопрос на естественном языке; система находит нужные куски документации / статей поддержки и генерирует ответ **со ссылками на источники**, либо честно отказывается («не нашёл»).

**Реальные реализации.** kapa.ai обслуживает docs-ассистентов для Docker, CircleCI, Reddit, Monday.com, OpenAI, Logitech и др. ([kapa.ai](https://www.kapa.ai/blog/rag-best-practices)). Stripe Dashboard Assistant — RAG поверх docs + support-статей ([Stripe docs](https://docs.stripe.com/assistant)).

**Устройство retrieval.**
- Chunking: по смысловым границам (раздел/подраздел), не по фиксированным N символам.
- Index: гибрид — dense embeddings **+ BM25** (лексический), чтобы ловить точные термины (коды ошибок, имена флагов).
- Rerank: cross-encoder поверх объединённых кандидатов.
- Refresh: **delta-обновление** (по аналогии с git diff) — переиндексируется только изменённое; у Stripe docs — десятки правок в день ([kapa.ai](https://www.kapa.ai/blog/rag-best-practices)).

**Что делает трудным.** Технические синонимы и близкие-но-разные термины; частые обновления базы; необходимость role-based доступа (не показать сотруднику чужой раздел).

**Типичный провал.** Embeddings решают, что «exponential backoff» и «dead-letter queue threshold» семантически близки, и ассистент уверенно выдаёт **неверную** политику ретраев ([Towards Data Science](https://towardsdatascience.com/hybrid-search-and-re-ranking-in-production-rag/)). Класс ошибки: retrieval подтянул не тот документ, а генератор всё равно ответил уверенно.

**Как чинит хорошая реализация.** Гибрид (BM25 ловит точный термин, который dense «замылил») + reranker переупорядочивает + порог «нет достаточно релевантного → откажись». Плюс кураторство источников: не сваливать всю базу, приоритет первичным (docs, API-ref, release notes), Slack/форумы — фильтровать по свежести/авторитетности ([kapa.ai](https://www.kapa.ai/blog/rag-best-practices)).

**Baseline / counterfactual.**
- Без гибрида+rerank: ~5.7 % проваленных ретривов → после — 1.9 % (в 3 раза меньше) ([Anthropic](https://www.anthropic.com/engineering/contextual-retrieval)).
- Без RAG вообще (fine-tune на FAQ): модель не обновляется при десятках правок/день — устаревает мгновенно.
- Экономика docs-бота маленького масштаба: ~200 docs → эмбеддинги ~$1–2 и 5 мин; ~300 запросов/мес ≈ $10 API ([Intlayer](https://intlayer.org/blog/rag-powered-documentation-assistant)). **(иллюстративный порядок величин для малого проекта, не enterprise)**

---

## Кейс B — Q&A по документации / developer-docs

**Задача.** «Как сделать X в SDK/продукте?» — ответ строго из актуальной документации, с цитатой и ссылкой; отказ, если в docs этого нет.

**Реальные реализации.** Vercel AI SDK docs-copilot (retrieve → rerank → answer with sources **или refuse**; 25-кейсовый eval-набор в CI) ([GitHub Alla-N/docs-copilot](https://github.com/Alla-N/docs-copilot)). Vercel публикует `llms.txt` (тонкий индекс для real-time ассистентов) + `llms-full.txt` (полный экспорт для ingestion в RAG) ([Mintlify](https://www.mintlify.com/blog/real-llms-txt-examples); [Vercel KB](https://vercel.com/kb/guide/what-is-rag)).

**Устройство retrieval.** Chunk по секциям docs; dense-index; rerank кандидатов; жёсткий контракт «answer with sources or refuse». Eval-suite в CI ловит регрессии ретрива при обновлении docs.

**Что делает трудным.** Docs меняются ежедневно (нужен refresh-pipeline); много версий API (легко подтянуть устаревший синтаксис); нужна честность отказа вместо выдумки.

**Типичный провал.** Ассистент цитирует старую версию API или «додумывает» несуществующий параметр (statement hallucination — ответ расходится с процитированным источником).

**Как чинит.** (1) Свежесть — delta-reindex; (2) reranker + порог отказа; (3) **eval-suite в CI** как gate: без метрик «vibe check» пропускает регрессии ([kapa.ai](https://www.kapa.ai/blog/rag-best-practices)).

**Baseline / counterfactual.** Без eval-набора регрессия ретрива после обновления docs уходит в прод незамеченной. Без «refuse»-контракта система галлюцинирует вместо «не нашёл» — хуже, чем пустой ответ, т.к. подрывает доверие ко всем ответам.

---

## Кейс C — Поиск по кодовой базе / Q&A по репозиторию (codebase RAG)

**Задача.** «Где реализована аутентификация?», «Что сломает изменение этой функции?» — найти релевантный код в большом репозитории и дать контекст ассистенту/агенту.

**Реальные реализации.** Cursor индексирует кодбазу эмбеддингами и делает RAG по коду ([Towards Data Science, «How Cursor Actually Indexes Your Codebase»](https://towardsdatascience.com/how-cursor-actually-indexes-your-codebase/)). Sourcegraph Cody исторически строился на эмбеддингах для контекста ([Sourcegraph, «How Cody understands your codebase»](https://sourcegraph.com/blog/how-cody-understands-your-codebase)).

**Устройство retrieval.** Chunk **по смысловым границам кода** (функция/класс, а не N строк); dense-index кода; постоянный refresh по мере изменения репо.

**Что делает трудным.** Код — не проза: точные идентификаторы важнее семантической близости; монорепо (>100k репозиториев) взрывают стоимость и поддержку вектор-индекса; отправка кода в сторонний embedding-API — риск безопасности.

**Типичный провал.** Dense-эмбеддинги «замыливают» точное имя символа; на масштабе монорепо вектор-поиск становится дорогим и медленным, multi-repo контекст не строится ([Sourcegraph docs, embeddings](https://docs.sourcegraph.com/cody/core-concepts/embeddings)).

**Как чинит хорошая реализация.** Cody на Enterprise **отказался от эмбеддингов** и заменил их на Sourcegraph Search (лексический/структурный поиск): безопаснее (код не уходит в чужой API), дешевле в поддержке, масштабируется на 100k+ репо, качество ретрива равное или лучше ([Sourcegraph docs](https://docs.sourcegraph.com/cody/core-concepts/embeddings)). Урок: для кода **классический поиск часто бьёт dense-RAG**.

**Baseline / counterfactual.** Vs эмбеддинги: приходилось слать весь код в OpenAI-API, хранить/обновлять векторы, а на >100k репо поиск деградировал — переход на search снял и стоимость, и security-риск, и потолок масштаба ([Sourcegraph docs](https://docs.sourcegraph.com/cody/core-concepts/embeddings)). Это одновременно **и кейс C, и живой пример «RAG-как-dense-vectors был не тем инструментом»** (см. раздел «Когда RAG — не тот инструмент»).

---

## Кейс D — Юридический / договорный / policy-поиск

**Задача.** Найти релевантные нормы/пункты договоров/прецеденты и дать ответ с цитатой на конкретный источник права.

**Реальные реализации + документированный провал.** Preregistered-исследование Stanford (HAI + RegLab) по коммерческим legal-AI: инструменты LexisNexis (Lexis+ AI) и Thomson Reuters (Westlaw AI-Assisted Research, Ask Practical Law AI) — **все на RAG** — галлюцинируют **17–33 % запросов**, несмотря на маркетинг «hallucination-free» ([Stanford RegLab](https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/); [VentureBeat](https://venturebeat.com/ai/stanford-study-finds-ai-legal-research-tools-prone-to-hallucinations); [Legal Dive](https://www.legaldive.com/news/legal-genai-tools-mislead-17-percent-of-time-stanford-HAI-hallucinations-incorrect-law-citations/717128/)).

**Устройство retrieval.** Гибрид (точные цитаты статей/номеров дел критичны → BM25 обязателен) + dense + rerank; жёсткая привязка ответа к извлечённому источнику.

**Что делает трудным.** Цена ошибки высочайшая (юрист несёт ответственность); «правдоподобная» ложь опаснее пустого ответа; точные цитаты (номер дела, статья) должны совпадать буквально.

**Типичный провал.** Две формы: (1) **citation hallucination** — сам источник выдуман; (2) **statement hallucination** — ссылка реальна, но утверждение расходится с её содержанием. RAG **снижает**, но **не устраняет** галлюцинации ([Stanford RegLab](https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/)).

**Как чинит.** Верификация цитат постфактум (проверить, что процитированный текст реально существует и подтверждает утверждение), обязательный человек-в-петле, отказ при низкой уверенности ретрива. Урок лекции: **RAG уменьшает, но не обнуляет** галлюцинации; в high-stakes без верификации выпускать нельзя.

**Baseline / counterfactual.** Vs чистый LLM без RAG — галлюцинации были бы ещё выше; но 17–33 % с RAG всё равно означает: **маркетинговое «0 % галлюцинаций» ложно**, и без верификации/человека применять нельзя.

---

## Кейс E — Deep-research по корпусу (агентный RAG) — переезжает из раздела промптов сюда

**Задача.** Один сложный вопрос («сравни рынок X по 5 измерениям, со ссылками») → система сама планирует под-вопросы, много раз ищет, читает источники, синтезирует отчёт с цитатами.

**Как реально устроены системы (архитектурный паттерн-кейс).**
- **Reasoning-LLM + агентный цикл RAG:** reasoning-driven retrieval — рассуждение направляет поиск, новые находки уточняют рассуждение (closed loop) ([arxiv 2507.09477, «Towards Agentic RAG with Deep Reasoning»](https://arxiv.org/pdf/2507.09477)).
- **OpenAI Deep Research:** одна мощная reasoning-модель (спец-версия o3) проходит весь цикл — план → поиск → backtrack → синтез ([VentureBeat](https://venturebeat.com/ai/out-analyzing-analysts-openais-deep-research-pairs-reasoning-llms-with-agentic-rag-to-automate-work-and-replace-jobs)).
- **Perplexity:** RAG по вебу в реальном времени, «citations — лучший способ связать поиск и LLM» (Aravind Srinivas), ответ аннотирован источниками ([VentureBeat](https://venturebeat.com/ai/out-analyzing-analysts-openais-deep-research-pairs-reasoning-llms-with-agentic-rag-to-automate-work-and-replace-jobs); [Aaron Tay, обзор](https://aarontay.substack.com/p/the-rise-of-agent-based-deep-research)).

**Обобщённый паттерн (для слайда-схемы):** `план под-вопросов → (поиск → чтение → уточнение рассуждения)×N → синтез → верификация цитат`.

**Документированный провал — фабрикация цитат.**
- В retrieval-augmented режиме **3–13 % URL сфабрикованы** ([arxiv 2604.03173, «Detecting and Correcting Reference Hallucinations»](https://arxiv.org/html/2604.03173v1)).
- DRBench (100 PhD-уровня задач): точность цитат **78 % (OpenAI DR) … 94 % (Claude с поиском)** — т.е. даже сверху 6–22 % проблемных ([arxiv, DRBench в 2601.22984](https://arxiv.org/html/2601.22984v1)).
- DRACO (100 задач из реального использования Perplexity, 2026): citation quality и factual accuracy — самые слабые оси; лучший результат **65 % citation quality / 68 % factual accuracy** ([arxiv 2602.11685, DRACO](https://arxiv.org/pdf/2602.11685)).
- Формы ошибок: выдуманные имена авторов, рассогласованные цитаты, битые/выдуманные ссылки.

**Как чинит.** Отдельный слой **verification** после синтеза: проверить, что каждый URL резолвится и что процитированный текст реально подтверждает утверждение (см. также кейс D).

**Baseline / counterfactual.** Vs ручной аналитик — быстрее и дешевле, НО без верификационного слоя 3–13 % ссылок ложны → в high-stakes отчёте это дороже, чем медленный человек. Урок: агентный RAG ускоряет ресёрч, но **citation verification — обязательный, а не опциональный слой**.

---

## Кейс F — Enterprise-поиск по смешанным данным (документы + таблицы)

**Задача.** «Сколько мы потратили на облако в Q3 и какая политика это регламентирует?» — ответ требует **и** структурных данных (таблица/БД), **и** текста (policy-документ).

**Реальные подходы.** Glean — multi-modal enterprise search (docs, images, code, structured data) через RAG ([Glean](https://www.glean.com/perspectives/best-rag-features-in-enterprise-search)). eSapiens — единый NL-интерфейс: **Text-to-SQL планировщик** для структурного + гибридный RAG для неструктурного ([arxiv 2506.16768](https://arxiv.org/pdf/2506.16768); паттерн также у [LlamaIndex](https://www.llamaindex.ai/blog/combining-text-to-sql-with-semantic-search-for-retrieval-augmented-generation-c60af30ec3b)).

**Устройство retrieval.** Роутер: числовой/агрегирующий вопрос → **Text-to-SQL** к БД; текстовый → dense+BM25+rerank по документам; ответ синтезирует оба. Плюс authorization (не показать строки БД вне прав).

**Что делает трудным.** Таблицы нельзя «эмбеддить как прозу» — вопрос «сумма за Q3» требует SQL-агрегации, а не похожих чанков; нужны другие метрики качества: **корректность запроса, соответствие схеме, авторизация, entity resolution** — вместо трёх метрик document-RAG ([arxiv 2608.19235](https://arxiv.org/html/2608.19235v1)).

**Типичный провал.** Naive-RAG эмбеддит строки таблицы и «находит похожие», но не может сложить/сгруппировать → неверные числа. Text-to-SQL на сложной схеме выдаёт **невалидный SQL**: синтаксис, не тот столбец, пропущенный фильтр ([AI21](https://www.ai21.com/knowledge/rag-for-structured-data/)).

**Как чинит.** Роутинг «структурный vs текстовый»; валидация/самопроверка SQL + fallback; отдельное измерение query correctness; авторизация на уровне строк.

**Baseline / counterfactual.** Vs чистый document-RAG по таблицам: агрегирующие вопросы просто неотвечаемы (нельзя «найти похожую сумму»). Vs ручной аналитик с SQL: быстрее, но при кривой схеме без валидации SQL молча даёт неверное число — хуже, чем «не знаю».

---

## Отдельно: «Когда RAG — НЕ тот инструмент» (real case + урок)

**Кейс-1 (dense-RAG → классический поиск): Sourcegraph Cody.** Cody **убрал эмбеддинги** на Enterprise и вернулся к Sourcegraph Search. Причины: код уходил в сторонний API (security), векторы надо хранить/обновлять (tech debt), на >100k репозиториев вектор-поиск дорог и не масштабируется, multi-repo контекст не строился. Итог: search дал **равное или лучшее** качество ретрива дешевле и безопаснее ([Sourcegraph docs](https://docs.sourcegraph.com/cody/core-concepts/embeddings)). **Урок:** для кода/точных идентификаторов классический (лексический/структурный) поиск часто побеждает dense-RAG.

**Кейс-2 (RAG → long-context):** при окне 1M токенов + prompt caching (~10 % цены) для **статичного корпуса < ~200k токенов (~500 страниц)** проще и дешевле положить всю базу в промпт, чем строить RAG ([Anthropic](https://www.anthropic.com/engineering/contextual-retrieval); [dev.to «RAG, Fine-Tuning, or Long Context?»](https://dev.to/gursharansingh/rag-in-practice-part-6-rag-fine-tuning-or-long-context-36je)). RAG выигрывает, только когда корпус **больше** окна, **часто меняется**, нужен **per-doc доступ** или **цитаты**. Оговорка: long-context на больших объёмах в проде **20–24× дороже** RAG — хорош для прототипа, плох для потока ([Medium, Dewoolkar](https://medium.com/@officialpreksha2166/rag-vs-fine-tuning-vs-long-context-when-to-use-what-and-why-most-teams-get-it-wrong-388cc446ff3c)).

**Кейс-3 (RAG → fine-tuning):** для внутреннего code-gen на **проприетарном фреймворке** fine-tuning научил модель фирменному синтаксису/паттернам, которых нет в базовой модели — качество кода заметно выше, чем GPT-4 + RAG **(порядок «10×» из вторичного источника — иллюстративный, не строгий бенчмарк)** ([Medium, Dewoolkar](https://medium.com/@officialpreksha2166/rag-vs-fine-tuning-vs-long-context-when-to-use-what-and-why-most-teams-get-it-wrong-388cc446ff3c); [IBM «RAG vs Fine-Tuning»](https://www.ibm.com/think/topics/rag-vs-fine-tuning)). **Урок:** RAG даёт **что** знать (факты), fine-tuning — **как** рассуждать/в каком стиле. Стиль/поведение через RAG не чинится.

**Кейс-4 (RAG → обычный запрос к БД):** вопрос «сумма расходов за Q3» — это `SELECT ... GROUP BY`, а не «найди похожие чанки». Эмбеддить таблицу и искать похожее → неверные агрегаты. **Урок:** числовой/агрегирующий вопрос по структурным данным → SQL/BI, а не dense-RAG (см. кейс F).

**Сквозной урок раздела (≥30%-bucket контент):** RAG — не «магическая пилюля». Он **уменьшает, но не обнуляет** галлюцинации (17–33 % в legal, 3–13 % фабрикованных цитат в deep-research); для кода/точных идентификаторов классический поиск часто лучше; для статичного малого корпуса — long-context; для стиля/поведения — fine-tuning; для чисел — просто БД. Критерий выбора инструмента важнее самого RAG.

---

## Мэппинг кейсов → слайды (подсказка для деки)

| Кейс | Слайд-тип | Ключевая цифра для нот |
|---|---|---|
| Anchor-лесенка | schema / table | 5.7 % → 1.9 % (−67 %) |
| A Support/KB | example + failure | backoff↔DLQ mix-up; ~40 % naive retrieval fail |
| B Docs-Q&A | example | «answer with sources or refuse» + eval в CI |
| C Codebase | example + «wrong tool» | Cody убрал эмбеддинги → search |
| D Legal | failure (30%-bucket) | 17–33 % галлюцинаций (Stanford) |
| E Deep-research | architecture diagram + failure | 3–13 % фабрикованных URL; DRACO 65 % |
| F Enterprise mixed | schema (router) | text-to-SQL + hybrid RAG |
| «Wrong tool» | judgment slide (30%-bucket) | <200k токенов → long-context; long-ctx 20–24× дороже |

---

## Источники (сводно)

- [Anthropic — Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
- [kapa.ai — RAG Best Practices (100+ teams)](https://www.kapa.ai/blog/rag-best-practices)
- [Towards Data Science — Hybrid Search and Re-Ranking in Production RAG](https://towardsdatascience.com/hybrid-search-and-re-ranking-in-production-rag/)
- [Towards Data Science — How Cursor Actually Indexes Your Codebase](https://towardsdatascience.com/how-cursor-actually-indexes-your-codebase/)
- [Sourcegraph — How Cody understands your codebase](https://sourcegraph.com/blog/how-cody-understands-your-codebase) · [Sourcegraph docs — Embeddings](https://docs.sourcegraph.com/cody/core-concepts/embeddings)
- [Stripe — Dashboard Assistant](https://docs.stripe.com/assistant) · [Vercel — What is RAG](https://vercel.com/kb/guide/what-is-rag) · [GitHub Alla-N/docs-copilot](https://github.com/Alla-N/docs-copilot) · [Mintlify — real llms.txt](https://www.mintlify.com/blog/real-llms-txt-examples) · [Intlayer — RAG docs assistant](https://intlayer.org/blog/rag-powered-documentation-assistant)
- [Stanford RegLab — Hallucination-Free? (legal AI)](https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/) · [VentureBeat](https://venturebeat.com/ai/stanford-study-finds-ai-legal-research-tools-prone-to-hallucinations) · [Legal Dive](https://www.legaldive.com/news/legal-genai-tools-mislead-17-percent-of-time-stanford-HAI-hallucinations-incorrect-law-citations/717128/)
- [VentureBeat — OpenAI Deep Research + agentic RAG](https://venturebeat.com/ai/out-analyzing-analysts-openais-deep-research-pairs-reasoning-llms-with-agentic-rag-to-automate-work-and-replace-jobs) · [Aaron Tay — Rise of agent-based deep research](https://aarontay.substack.com/p/the-rise-of-agent-based-deep-research) · [arxiv 2507.09477 — Agentic RAG with Deep Reasoning](https://arxiv.org/pdf/2507.09477)
- [arxiv 2604.03173 — Reference Hallucinations](https://arxiv.org/html/2604.03173v1) · [arxiv 2601.22984 — DRBench context](https://arxiv.org/html/2601.22984v1) · [arxiv 2602.11685 — DRACO](https://arxiv.org/pdf/2602.11685)
- [AI21 — RAG for Structured Data](https://www.ai21.com/knowledge/rag-for-structured-data/) · [arxiv 2608.19235 — Structured Enterprise Data](https://arxiv.org/html/2608.19235v1) · [LlamaIndex — Text-to-SQL + semantic](https://www.llamaindex.ai/blog/combining-text-to-sql-with-semantic-search-for-retrieval-augmented-generation-c60af30ec3b) · [Glean — RAG enterprise search](https://www.glean.com/perspectives/best-rag-features-in-enterprise-search) · [arxiv 2506.16768 — eSapiens](https://arxiv.org/pdf/2506.16768)
- [Medium (Dewoolkar) — RAG vs Fine-tuning vs Long Context](https://medium.com/@officialpreksha2166/rag-vs-fine-tuning-vs-long-context-when-to-use-what-and-why-most-teams-get-it-wrong-388cc446ff3c) · [dev.to — RAG, Fine-Tuning, or Long Context?](https://dev.to/gursharansingh/rag-in-practice-part-6-rag-fine-tuning-or-long-context-36je) · [IBM — RAG vs Fine-tuning](https://www.ibm.com/think/topics/rag-vs-fine-tuning)

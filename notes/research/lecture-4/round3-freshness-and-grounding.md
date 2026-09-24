# Lecture 4 — Round 3: Freshness Refresh + Academic Grounding + Local Test Tooling + SDD Naming + Secrets Hygiene

**Date:** 2026-09-20 · **Researcher:** fact-checker research subagent · **Issue:** #162 (третий раунд правок по детальному owner-фидбеку, после Phase 3/7 round 1-2)
**Purpose:** пять точечных research-запросов owner'а: (1) есть ли данные 2026 года для «70%-проблемы» вместо/в дополнение к SO-2025 + GitClear-2020-2024; (2) академическая (не только practitioner) литература про модуляризацию инструкций агента на skills; (3) **локальный** (не SaaS) тестовый инструментарий кодинг-агента; (4) употребляется ли «SDD» как устоявшаяся аббревиатура наравне с TDD/BDD; (5) секреты/.gitignore-гигиена в git-практиках агента с широким доступом к репо.
**Sibling files (read first, NOT duplicated here):** `coding-agent-mechanics.md` (§3 git-конвенции — Conventional Commits/Branch, PR-шаблоны; §1 Skills — Claude-docs эвристики; НЕ содержит секцию про secrets/gitleaks), `methodology-and-tooling-expansion.md` (§3 trunk-based+AI, §4 test-tooling за пределами Playwright — Postman/Testcontainers/Percy/Chromatic/Applitools, все внешние/SaaS; НЕ содержит локальный аспект тестового харнеса и НЕ содержит секреты).
**Access date для всех URL:** **2026-09-20**, если не указано иное. `[VFY-day-of]` = волатильный факт (версия продукта/фича/цифра/публикация отчёта), перепроверить в день лекции.
Confidence: **HIGH** = первичный источник (vendor docs, canonical spec, официальный анонс) · **MEDIUM** = practitioner consensus / vendor blog / secondary / preprint без peer review · **LOW** = единичный блог / emerging / anecdotal / vendor self-report без независимой верификации.

**Куда должно попасть каждое:** блок 1 → слайд/раздел главы с «70%-проблемой» (сейчас цитирует SO-2025 66% + GitClear 2020-2024/211M строк) — обновить GitClear-цитату на 2026-версию, оставить SO-2025 с явной оговоркой о свежести; блок 2 → §3.3b главы (Skills) — добавить академическую рамку рядом с practitioner-эвристиками Claude Code docs; блок 3 → §4 главы (тестирование) — заменить/дополнить внешние SaaS-инструменты локальными; блок 4 → §1 главы (spec-driven) — ввести аббревиатуру SDD с явной оговоркой про терминологическую неоднозначность; блок 5 → §5.4 главы (Lethal Trifecta/least-privilege) — конкретный, датированный кейс вместо абстрактного риска.

---

## 1. Свежие 2026-данные для «70%-проблемы»

### 1.1 Stack Overflow Developer Survey — что реально самое свежее на дату research

**Честный вывод: полных результатов SO Developer Survey 2026 ещё нет.** «2026 Developer Survey» **открыт для сбора ответов** 2026-06-23 (stackoverflow.blog, «The 2026 Developer Survey is now open (for human developers only)!», primary) — это НАБОР данных, а не публикация результатов; полного отчёта по 2026-волне на дату research (2026-09-20) не найдено ни на `stackoverflow.blog`, ни на `survey.stackoverflow.co`. Историческая механика самого SO (по данным этого прохода): опрос закрывается, обработка занимает месяцы — то есть результаты 2026-волны реалистично ожидаются позже в 2026 или в начале 2027.

**Самый свежий полностью опубликованный отчёт остаётся «2025 Developer Survey»** — опубликован 2025-12-29 (`stackoverflow.blog`), данные собраны май-август 2025, 49 000+ респондентов, 177 стран, 62 вопроса, «в его пятнадцатый год» (`survey.stackoverflow.co/2025`, primary, verbatim). Именно этот отчёт — источник цифры **66%** («AI solutions that are almost right, but not quite» — самая частая единичная фрустрация), которую уже цитирует текущий слайд главы. Точный набор смежных цифр из этого же отчёта (для контекста, не для замены существующей цитаты):
- 66% — «almost right, but not quite» — топ-1 фрустрация (verbatim, primary).
- 45% — «Debugging AI-generated code is more time-consuming» (verbatim, primary).
- 46% активно **не доверяют** точности AI-инструментов vs 33% доверяют (survey.stackoverflow.co/2025, primary); отдельно вторичные источники (adtmag, byteiota) цитируют траекторию «40% доверия в 2024 → 29% в 2025» и «3% highly trust» — эти цифры из того же 2025-отчёта, не из отдельной 2026-волны (несмотря на заголовки статей вида «2026 Dev Survey»).
- 84% adoption AI-инструментов, 51% профессионалов — ежедневно (тот же 2025-отчёт).

**Honesty flag (важно для book-editor):** несколько вторичных агрегаторов (`byteiota.com`, др.) публикуют материалы под заголовком «Stack Overflow Dev Survey **2026**», но при прямой проверке ссылаются на `survey.stackoverflow.co/2025` и оперируют теми же цифрами (66%/45%/84%/3%) — это **переупаковка данных 2025-опроса под 2026-датированный заголовок публикации статьи**, а не новая волна данных. Не путать «дата публикации статьи-пересказа» (может быть 2026) с «дата волны опроса» (2025). Глава должна продолжать явно писать **«Stack Overflow Developer Survey 2025 (опубликован декабрь 2025)»**, а не «2026 survey» — иначе это будет фактическая ошибка о собственном источнике.

**Confidence: HIGH** на том, что полных 2026-результатов ещё нет (прямая проверка `survey.stackoverflow.co` и `stackoverflow.blog`, primary); **HIGH** на точных цифрах 2025-отчёта (primary, сверено по `survey.stackoverflow.co/2025` напрямую). `[VFY-day-of]`: если лекция читается после публикации полного 2026-отчёта, эта секция должна быть перепроверена — SO традиционно даёт свежие данные о трасте/фрустрациях каждый цикл, и к дню лекции 2026-волна может уже выйти.

### 1.2 GitClear — есть 2026-обновление, и оно существенно расширяет старую цитату

**Это прямой позитивный ответ на запрос owner'а: да, есть отчёт GitClear именно 2026 года**, причём с большей выборкой, чем цитируемый сейчас в главе 2020-2024/211M-строк отчёт.

**«The Maintainability Gap: AI Code Quality in 2026»** (GitClear, версия **2026.6.1**, опубликован **июнь 2026** — `gitclear.com/the_ai_code_quality_maintainability_gap`, primary vendor). Проанализировано **623 миллиона** изменений кода за период **2023-2026** (по сравнению с 211M строк / 2020-2024 в старой цитате главы — новый отчёт и шире по выборке, и свежее по временному окну). Восемь сигналов сопровождаемости кода изменились в «плохую» сторону:

| Сигнал | Было | Стало | Δ |
|---|---|---|---|
| Refactoring/moved code | 21% изменённых строк (2022) | 3.8% (2026) | **−70% относительно** (verbatim у вторичного пересказа отчёта) |
| Block duplication | 40.3 на млн изменённых строк (2023) | 73.0 (2026) | **+81%** |
| Copy/paste (доля нового кода) | 9.4% (2022) | 15.7% (H1 2026) | **+41%** внутри-коммитного copy/paste |
| Error-masking (глотающие catch-блоки) | — | — | **+47%** |
| Cross-file function calls | 343 вызова / тыс. изменённых строк (2023) | 223 (2026) | **−35%** |
| Legacy maintenance (правки кода старше 12 мес.) | 1.7% изменений | 0.46% | **−74%** |
| Two-week code churn | — | — | **+15%** |

**Честная оговорка о согласованности цифр между источниками.** Разные вторичные пересказы (arturmarkus.com, gitclear press) слегка расходятся в формулировке даты публикации самого отчёта (встречалась и «январь 2026», и «июнь 2026» в разных поисковых сниппетах) — прямая проверка через WebFetch страницы отчёта и версионный номер (`2026.6.1`) указывают на **июнь 2026** как дату релиза именно этой версии отчёта; более раннее (январь 2026) GitClear-исследование — **отдельная**, более узкая публикация «AI Coding Tools Attract Top Performers» (про продуктивность, не про maintainability-сигналы) — **не путать с «Maintainability Gap»**, это два разных документа одного вендора в одном году.

**Инженерный вывод для главы:** GitClear-2026 — легитимное, куда более сильное количественное подкрепление тезиса «AI-код технически корректен чаще, чем сопровождаем» (сдвиг от «почти правильный код» SO-опроса к измеримой деградации maintainability-метрик в реальных репозиториях) — рекомендация заменить старую цитату «211M строк, 2020-2024» на GitClear-2026 «623M изменений, 2023-2026» с таблицей выше, оставив методологическую оговорку (это тот же вендор, self-published аналитика, не независимо воспроизведённое академическое исследование — как и раньше).

**Confidence: HIGH** на самом факте существования 2026-отчёта и на числах из таблицы (primary vendor page + независимый пересказ, числа совпадают между источниками); **MEDIUM** на точной дате релиза версии (расхождение в разных вторичных упоминаниях, `[VFY-day-of]`); **не независимая верификация методологии** — как и для прежней GitClear-цитаты в главе, это self-published vendor-аналитика (GitClear продаёт инструмент для тех же метрик), не peer-reviewed исследование — сохранить ту же методологическую оговорку, что уже (предположительно) есть в главе для старой цитаты.

### 1.3 Итог блока 1

- **SO-2025 остаётся самым свежим полным отчётом** на дату лекции (если не выйдет 2026-волна раньше) — держать текущую цитату, поправить только год/дату публикации в подписи, если сейчас написано неточно.
- **GitClear-2026 — легитимное обновление**, стоит заменить/дополнить старую GitClear-2020-2024 цитату.
- **`[VFY-day-of]` обязателен для обеих цитат** — SO может опубликовать 2026-волну до дня лекции (тогда числа трафика/трастов надо перепроверить), GitClear может выпустить более свежую micro-версию отчёта (у вендора наблюдается версионирование `2026.X.Y`).

---

## 2. Академическая литература про модуляризацию инструкций агента на skills

### 2.1 Практический вывод сразу: смешанная картина, не «чисто индустрия»

Owner прав, что практика (Claude Code docs эвристики, уже в `coding-agent-mechanics.md` §1.1) — не единственный слой; на arXiv в 2026 году появился заметный кластер препринтов именно про «agent skills» как научную категорию. Но честно: большинство из них — **taxonomy/lifecycle/security-survey**, а не **design-criteria-когда-декомпозировать** работы в духе классического SE (cohesion/coupling/DRY). Есть, однако, **одна прямая находка**, которая именно это делает (§2.3 ниже).

### 2.2 Обзорный кластер (taxonomy/lifecycle/security, НЕ SE-принципы декомпозиции)

- **«SoK: Agentic Skills — Beyond Tool Use in LLM Agents»** (Jiang, Li, Deng, Ma, Wang, Wang, Yu; arXiv:2602.20867, подано 2026-02-24) — Systematization of Knowledge формата (SoK — признанный академический жанр обзорных работ по безопасности/архитектуре). Покрывает lifecycle skills (discovery→practice→distillation→storage→composition→evaluation→update), «семь design-паттернов» упаковки/исполнения, таксономию representation×scope, и security-кейс **ClawHavoc** («nearly 1,200 malicious skills infiltrated a major agent marketplace»). **Явно НЕ обсуждает** cohesion/coupling/DRY/модульность в SE-терминологии — использует «reusable interfaces» описательно, без формальных критериев декомпозиции.
- **«Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward»** (Xu, Yan; arXiv:2602.12430, подано 2026-02-12, принято на **Agent Skills '26 Workshop при ACM Conference on AI and Agentic Systems 2026** — workshop-уровень, не полноценный peer-reviewed track конференции). Четыре измерения: архитектурные основы (SKILL.md + MCP), acquisition через RL/автономное открытие, deployment scaling, security (**«26.1% of community-contributed skills contain vulnerabilities»** — заметная цифра для §3.3b главы про security skills, если нужна). Декомпозиционных SE-критериев тоже нет в абстракте.
- **«Harnessing Agent Skills: Architectural Patterns and a Reference Architecture for Skill-Mediated LLM Agents»** (Xia, Zhu, Xing, Lu, Sejdinovic, Xu; arXiv:2606.20631, 2026-05-29) — методологически наиболее строгая из обзорного кластера (multivocal literature review + reference-architecture evaluation), авторы аффилированы с CSIRO's Data61 (реальный исследовательский институт, не anonymous blog). Вводит «Skill–Execution Authority Separation» (разделение того, какие capabilities skill **референсит**, от того, какие **полномочия** агенту даны их использовать) — это архитектурное модульное мышление, но **явно не формулируется** как классический cohesion/coupling; ближе к security-boundary дизайну, чем к SE-модульности per se.

**Confidence: HIGH** на существовании и содержании всех трёх (первичные arXiv-страницы + WebFetch абстрактов); **явный honesty flag**: ни одна из трёх НЕ даёт критериев декомпозиции в духе SE cohesion/coupling — если глава ссылается на них, это должно быть для security/taxonomy-контекста, не для «когда заводить skill».

### 2.3 Прямая находка: SE-принципы, применённые к дизайну skills

**«Authoring Agent Skills: A Software-Engineering Approach»** (Giuseppe Destefanis; arXiv:**2607.25032**, подано **2026-07-27**, категория **cs.SE** — Software Engineering, не cs.AI). Это именно то, что просил owner: **явно** формулирует, что skill — программный артефакт, и его конструирование должно следовать инженерным принципам:

1. **Single responsibility** — «a skill should have a single responsibility, one coherent capability»; обоснование через механизм selection — description skill'а матчится против задачи, и «a skill scoped to one class of task is selected more reliably, while one that does several things has a diffuse description that matches less well» (прямая, проверяемая инженерная причина, не просто эстетика).
2. **Separation of interface from implementation** — чёткая граница между тем, что skill **предоставляет** (description/frontmatter) и тем, **как** он это делает внутри (тело SKILL.md + companion-файлы).
3. **Low coupling / высокая cohesion** — «cohesion applies in its usual sense: a skill, and each reference file within it, groups content that serves a single concern» + «the same principle behind modular software design — high cohesion, low coupling applies, where each module knows its domain deeply and doesn't leak into others» (прямая параллель с классическим SE, не метафора).
4. **Economy in a shared token budget** — SE-аналог DRY/ресурсной экономии, специфично адаптированный под LLM-контекст: не дублировать контент между skill'ами, если можно сослаться.
5. **Behavioural evaluation вместо deterministic testing** — честная оговорка автора, что классическое unit-testing не переносится 1:1 на skills — поведенческая оценка (согласуется ли выход с ожиданием), не детерминированная проверка.

Автор также предлагает решётку выбора между skills и альтернативами (project memory/CLAUDE.md, slash commands, subagents, external tools, hooks) на основе **«who decides that a mechanism runs and what guarantee it provides»** — то есть критерий не «где удобнее», а «кто инициирует вызов (модель/пользователь/hook) и какая гарантия применения» — структурно похоже (но не идентично) на table сравнения CLAUDE.md/SKILL.md/AGENTS.md, уже цитируемую в `coding-agent-mechanics.md` §1.1, только формализованное через доп. ось «guarantee».

**Confidence: MEDIUM-HIGH** на содержании (первичный arXiv, категория cs.SE релевантна теме напрямую) — **но honestly**: это **единственный автор**, препринт **без объявленного peer review** (нет venue/conference в метаданных на момент фетча), опубликован **2026-07-27** — очень свежая, узкая работа, а не устоявшийся канон уровня Cucumber/Conventional Commits. Если глава цитирует — явно маркировать как «одна из первых академических работ, формально связывающих SE-модульность с agent skills», не как «общепринятая теория».

### 2.4 Честный итог блока 2

**Владелец прав, что до недавнего времени это была в основном индустрия** — но на дату research (2026-09-20) появилась минимум одна прямая академическая работа (Destefanis, cs.SE, июль 2026), которая **именно** формулирует cohesion/coupling/single-responsibility/DRY-адаптацию как критерии дизайна skill. Более широкий кластер arXiv-препринтов про agent skills (SoK, обзоры, security) — реален и растёт быстро (минимум 5-6 препринтов только за первую половину 2026 года), но большинство из них про lifecycle/taxonomy/security, не про SE-модульность конкретно. **Рекомендация для §3.3b главы:** сохранить practitioner-эвристики Claude Code docs как основной, проверенный, HIGH-confidence слой (уже в `coding-agent-mechanics.md`), добавить Destefanis-цитату как «более общая, академическая рамка (single responsibility / cohesion / low coupling) — тот же вывод, что и практические эвристики Anthropic, но выведенный из классической SE-теории, не из vendor-документации» — это ровно то усиление, которое просил owner, без overclaim зрелости академического поля.

---

## 3. Локальный тестовый инструментарий кодинг-агента (не внешние SaaS)

*(§4 `methodology-and-tooling-expansion.md` уже покрывает Postman AI Engineer/Percy/Chromatic/Applitools/Testcontainers — все, кроме Testcontainers, облачные SaaS. Здесь — специально ЛОКАЛЬНЫЙ аспект: что реально крутится на машине разработчика/агента в цикле, без выхода во внешний сервис.)*

### 3.1 Testcontainers + pytest — эталонный локальный паттерн (уже частично в другом research-файле, здесь — именно local framing)

Уже разобран в `methodology-and-tooling-expansion.md` §4.2 как «AI-специфика через skill», но там акцент на **skill**-паттерне; здесь фиксируем именно **локальность**: контейнер (Postgres/Kafka/Redis/др.) поднимается на **эфемерном порту на машине разработчика** через Docker, session-scoped pytest fixtures держат его живым на весь тестовый прогон, уничтожается после — **никакого выхода в облако**, весь цикл замкнут локально (только Docker daemon как зависимость). «testcontainers-python with pytest is the right default for Python integration testing in 2026... session-scoped containers keeping test suites fast and transactional rollback keeping tests isolated» (qaskills.sh, secondary, 2026). **Confidence: HIGH** на механике (устоявшийся, немолодой инструмент).

### 3.2 MSW (Mock Service Worker) — локальный network-level мок для JS/TS

MSW перехватывает HTTP-запросы **на уровне сети** прямо в процессе (браузер через Service Worker API, Node.js через interceptor), а не поднимает отдельный сервер — то есть это библиотека, встраиваемая в тестовый процесс, полностью локальная, без внешнего SaaS. Ключевое инженерное свойство для агентного цикла: «because MSW interception happens at the network boundary, the same handlers work in unit tests, integration tests, Storybook, local development, and end-to-end runs without changing application code» (mswjs.io / qaskills.sh, 2026) — то есть один и тот же мок переиспользуется на всех уровнях тестовой пирамиды без дублирования конфигурации.

**AI-специфика (честная оговорка про зрелость).** Базовый MSW — зрелая (с 2018 года), широко принятая библиотека (HIGH maturity сам по себе). AI-ассистированный слой поверх — новее и менее устоявшийся: «AI agents can generate MSW handlers from API routes, create realistic test data factories, set up error injection patterns» (qaskills.sh, 2026, MEDIUM). Известная проблема, зафиксированная в источниках как «2026-shaped gap»: **«AI coding agents don't get real data... they've never actually seen real API responses and invent the response shape from documentation or training data, making the stub a guess»** — то есть AI-сгенерированный MSW-хэндлер может правдоподобно выглядеть, но не соответствовать реальному API, если агенту не дан реальный пример ответа как контекст.

**Confidence: HIGH** на MSW как локальном инструменте (первичная документация, зрелый продукт); **MEDIUM** на AI-генерации хэндлеров (community-практика 2026, не vendor-канон); честный gap про «invented response shape» явно зафиксирован.

### 3.3 WireMock — важная оговорка: локальное ядро vs облачный AI-слой

**WireMock (OSS)** — самостоятельный, полностью локальный/self-hosted mock-сервер (Java-based, можно поднять в Docker или как отдельный процесс) — зрелый, давно существующий инструмент (HIGH maturity сам по себе). **Но honesty flag, важный именно для запроса owner'а «не SaaS»:** AI-агентные фичи (**Agent Skills, MCP-сервер для WireMock**) на дату research размещены преимущественно на **WireMock Cloud** — это уже облачный, платный продукт вендора, а не локальное OSS-ядро: «WireMock Agent Skills and MCP server expose every platform capability to AI coding agents for building mock APIs and creating stubs... AI agents can point at authoritative sources to stand up simulations through **WireMock Cloud's** MCP server» (wiremock.io, vendor, MEDIUM). **Итог: если цель — именно локальный, не-SaaS инструмент, стоит рекомендовать голый WireMock OSS + ручные/скриптовые stub-конфиги (или MSW/§3.2 для JS-стека), а не преподносить «WireMock + AI» как локальный пример — AI-слой там де-факто облачный.** Это прямая иллюстрация того, зачем owner попросил перепроверить именно локальность — без явной проверки легко перепутать «есть локальный OSS-инструмент» с «есть локальный AI-функционал у этого инструмента».

**Confidence: MEDIUM** — сам факт разделения local-core/cloud-AI подтверждён вендорским сайтом напрямую (primary), но именно это разделение — то, что легко упустить при поверхностном чтении маркетинга.

### 3.4 pytest-generator (Distil Labs) — генуинно локальная AI-генерация тестов (нишевый, но точный пример)

Самый буквальный ответ на «AI-plugin для pytest, который реально локальный»: **pytest-generator** от Distil Labs (опубликован **2026-02-18**) — «runs entirely on your local machine with zero API costs and complete privacy» (distillabs.ai, primary vendor, verbatim). Механика: дообученная (fine-tuned через knowledge distillation от DeepSeek V3.1, 671B, как teacher-модели) **Qwen3-8B**-модель (~5GB, есть Q4-квантованная CPU-only версия), генерирует pytest test cases из сигнатур функций и docstring'ов — исходный код **никогда не покидает машину** разработчика (в отличие от Qodo/Keploy/Claude Code, которые по умолчанию идут через облачный inference). Честная оговорка самого вендора: «Generated tests are meant to be reviewed and refined by developers before use — not run as-is» — генерируются «скелеты» тестов (mocks, parametrized cases, exception handling), не production-ready код, точность модели ≈77% на 8B-масштабе (self-reported).

**Confidence: LOW-MEDIUM** — очень новый (опубликован за ~7 месяцев до даты research), нишевая adoption, self-reported точность не независимо верифицирована — но это единственный из найденных инструментов, который **буквально** и без оговорок «полностью локален» на уровне самой AI-генерации (не только мока/фикстуры) — ценный контрпример к более распространённым облачным AI-test-generation инструментам (Qodo/Keploy/Claude Code cloud-inference).

### 3.5 Claude Code skill-паттерн: локальная цепочка lint+type-check+test как переиспользуемый харнес

Пятый пример — не отдельный вендорский продукт, а **паттерн упаковки уже существующего локального цикла** (lint → type-check → test), знакомого главе (Бёкелер/harness-references в `harness-and-architecture-practices.md`), в переиспользуемый skill: «Claude Code skills can run the full local lint + type-check + test suite (`ruff check`, `mypy src`, `pytest --cov=rate_limiter`) to automate repository workflows» (GitHub issue пример конкретного репозитория, 2026); аналогичный паттерн для JS/TS-стека — `eslint` + `tsc` + `vitest`. Testing skills «detect your framework (Jest, Pytest, Vitest, Go testing) and match your existing patterns» — то есть не новый инструмент, а **skill-обёртка** (прямой мост к §3.3b главы, Skills) над уже существующим локальным тестовым стеком проекта, устраняющая необходимость каждый раз заново объяснять агенту, как запускать тесты именно в этом репозитории.

**Confidence: MEDIUM** — community-skills-паттерн (не официальный `anthropics/skills`), но логически прямое и хорошо документированное расширение уже HIGH-confidence материала главы про Skills и харнес.

### 3.6 Итог блока 3 — таблица зрелости

| Инструмент | Что делает локально | AI-специфика | Зрелость (0-локальность / AI-слой) |
|---|---|---|---|
| Testcontainers + pytest | Эфемерная реальная БД в Docker на машине | AI знает конвенции конфигов через skill (не «умный анализ») | HIGH / MEDIUM |
| MSW | Network-level мок в процессе (unit→e2e без смены кода) | AI генерирует handlers, но может «придумать» форму ответа без реального примера | HIGH / MEDIUM (честный gap: invented response shape) |
| WireMock OSS | Полноценный self-hosted mock-сервер | AI-фичи (Agent Skills, MCP) **преимущественно на облачном WireMock Cloud** — не локальны | HIGH (core) / **LOW as local-AI** (honesty flag) |
| pytest-generator (Distil Labs) | Генерация тест-скелетов через локальную 8B-модель, zero API calls | Буквально «локальный AI», но низкая зрелость/adoption, ~77% точность self-reported | LOW-MEDIUM / LOW-MEDIUM |
| Claude Code skill-обёртка lint+type-check+test | Запуск уже существующего локального CI-цикла проекта одной командой/авто | Не генерирует новое — упаковывает существующий харнес в переиспользуемый вызов | MEDIUM (community skill, не official) |

**Honesty flag сводно:** «локальный AI-тестовый инструментарий» в 2026 году **неравномерно зрелый** — там, где локальная non-AI часть давно стандартна (Testcontainers, MSW), AI-слой чаще всего community-add-on поверх неё (MEDIUM); там, где вендор явно рекламирует «AI + локально» (WireMock), внимательная проверка показывает, что AI-часть на самом деле облачная — нужно явно разделять в главе «локальный инструмент» и «локальный **AI**-функционал этого инструмента», это разные утверждения.

---

## 4. SDD как явно названная практика — подтверждено, с одной существенной терминологической оговоркой

### 4.1 Основной вывод: да, «SDD» используется как устоявшаяся аббревиатура наравне с TDD/BDD

**GitHub Spec Kit** — канонический, официальный источник термина в его мейнстримном значении: `spec-driven.md` (github.com/github/spec-kit, primary) использует «SDD» систематически по всему документу как сокращение **Spec-Driven Development**: «**Spec-Driven Development (SDD)** inverts this power structure. Specifications don't serve code—code serves specifications» и «SDD eliminates the gap by making specifications and their implementation plans... executable» (verbatim). Репозиторий заявляет **~90k+ звёзд, ~8k+ форков** — по масштабу adoption сопоставимо с крупными dev-tool проектами.

**AWS Kiro** — второй крупный vendor, использующий ту же аббревиатуру в том же значении: множественные официальные и практические материалы AWS (`skillbuilder.aws`, `builder.aws.com`) называют методологию Kiro именно «Spec-Driven Development» с сокращением «SDD», например: «SDD requires you to define exactly what needs to be built and how it will be built before any implementation begins» (aws.plainenglish.io, вторичный, но описывает официальную позицию AWS).

**Индустриальная конвергенция к 2026 году** (secondary-синтез из нескольких источников, согласованный): «By 2026, every major AI coding tool — GitHub Spec Kit, AWS Kiro, Claude Code, Cursor, OpenSpec, BMAD, Tessl, Google Antigravity — has shipped its own flavor of SDD» (letsdatascience.com пересказ). Также существует посвящённая термину статья **Wikipedia «Spec-driven development»** — сам факт наличия энциклопедической статьи (а не просто блог-постов) — косвенный, но реальный сигнал терминологической устоявшести к 2026 году.

**Explicit TDD/BDD/SDD сопоставление — опубликованная книга, не только блог.** Хари Кришнан (Hari Krishnan), автор книги **«Spec-Driven Development: Engineering with Intent»** (Manning Publications — реномированное техническое издательство), в блоге `intent-driven.dev` (2026-08-23) формулирует явную «altitude»-иерархию: «**SDD** anchors the work in a specification, **BDD** protects the macro behavior, and **TDD** improves the micro-level design» — SDD (спека, самый высокий уровень) → BDD (macro/acceptance, Gherkin) → TDD (micro/unit) — методологии **не конкурируют**, а «stack» на разных уровнях детализации одной и той же задачи. Это прямая, книжно-опубликованная параллель к структуре §2.5 `coding-agent-mechanics.md` («TDD — spec на уровне кода, BDD — spec на уровне бизнес-языка»), теперь усиленная третьим уровнем (SDD — spec на уровне фичи/архитектуры).

**Confidence: HIGH** на факте использования аббревиатуры GitHub/AWS (primary источники, прямая цитата); **MEDIUM-HIGH** на «TDD/BDD/SDD altitude stack» (опубликованная книга Manning + согласующийся блог-пост автора, не единичный анонимный блог, но и не peer-reviewed).

### 4.2 Честная терминологическая оговорка — два разных «SDD»

**Важный honesty flag, который глава должна учесть, чтобы не создать путаницу.** Помимо мейнстримного «Spec-Driven Development» (GitHub/AWS lineage, §4.1), существует **отдельное, более раннее и по-другому позиционированное** использование той же аббревиатуры вендором **testRigor**: «at testRigor, we created the **Specification-Driven Development (SDD)** term» (testrigor.com, прямая цитата автора Artem Golubev) — testRigor явно заявляет **собственное авторство термина**, с отличающимся полным названием («Specification-Driven», не «Spec-Driven») и другим позиционированием (SDD у testRigor — критика BDD как «fundamentally flawed» и предложение альтернативы, ориентированной на «user stories & business requirements», а не GitHub/AWS-версия «спека как исполняемый артефакт, из которого агент генерирует код»).

**Инженерный вывод для главы:** аббревиатура «SDD» **не имеет единственного канонического источника** — есть доминирующее, широко принятое значение (GitHub Spec Kit / AWS Kiro lineage, ×90k GitHub stars, принято ≥8 крупными вендорами), которое и соответствует уже описанной в главе практике (§1 «Требования»), и есть отдельное, менее распространённое, вендор-специфичное use (testRigor). **Рекомендация:** при первом введении «SDD» в главе явно указать источник линии («в трактовке GitHub Spec Kit / AWS Kiro, ставшей отраслевым стандартом к 2026 году») — это снимает риск, что дотошный студент найдёт testRigor-версию и решит, что глава ошиблась в определении.

**Confidence: HIGH** на самом факте существования двух use (обе стороны процитированы напрямую, primary для каждой); честно — не найдено источника, который бы явно разрешал этот терминологический конфликт «кто первый» — не выдумываем приоритет, просто фиксируем наличие двух употреблений.

### 4.3 Итог блока 4

Да, «SDD» — **реально устоявшаяся, широко используемая аббревиатура** в индустрии 2025-2026 (не только полный термин «spec-driven development» без сокращения) — можно смело вводить в §1 главы наравне с TDD/BDD, с явной привязкой к GitHub Spec Kit/AWS Kiro как источнику мейнстримного значения и опциональной сноской про terminology overlap (§4.2) если нужна максимальная точность.

---

## 5. Секреты и нетрекаемые сущности в git-практиках агента

### 5.1 Базовый инструментарий 2026 — Gitleaks vs TruffleHog, слоистая модель

**Gitleaks** — «rule-first scanner that matches credentials against a large set of regex patterns, with Shannon entropy as a secondary signal» — быстрый (<1 сек), «works best as a pre-commit hook that blocks secrets in milliseconds» (appsecsanta.com / iancloud.ai, secondary, MEDIUM). **TruffleHog** — «verification-first: it finds candidates through regex and entropy, then makes a **live API call** to the relevant provider to confirm whether the credential is actually valid right now» — тяжелее (сетевые вызовы), но даёт меньше ложных срабатываний за счёт реальной проверки валидности ключа. Оба — open-source, совокупно «51,000+ GitHub stars».

**Рекомендованная многослойная модель 2026 года** (Decryption Digest, Eric Bang CISSP, опубликовано **2026-05-21**, обновлено **2026-06-25**, независимая security-публикация, не vendor blog):
1. **Pre-commit hook (Gitleaks)** — локально на машине разработчика/агента, «catches secrets before they enter git history»; **bypassable** через `git commit --no-verify` — advisory, не authoritative.
2. **CI pipeline blocking (Gitleaks + TruffleHog `--verified`)** — на каждый PR; «pre-commit hooks are advisory, they can be bypassed... the authoritative secrets gate is your CI pipeline» (verbatim).
3. **GitHub Advanced Security (GHAS) push protection** — server-side, организационный уровень; предотвращает bypass через `--no-verify`, потому что применяется на стороне git-хостинга, а не на клиенте.

Дополнительная рекомендация того же источника напрямую про `.gitignore`/`.env`: «Keep `.env.example` in version control with placeholder values. Add `.env`, `.env.local`, `.env.production` to `.gitignore` globally» (verbatim) — то есть коммитить **шаблон** с плейсхолдерами, реальные значения — только локально/в vault, никогда в git.

**Confidence: MEDIUM** (независимая, но не первично-вендорская security-публикация; общая механика Gitleaks/TruffleHog подтверждена по нескольким независимым источникам согласованно).

### 5.2 2026-специфичный драйвер: объём агентных изменений структурно расширяет поверхность утечки

Прямая формулировка причины, почему это особенно релевантно именно кодинг-агенту (не просто «хорошая практика вообще»): «AI coding assistants... A developer using Claude Code, Cursor, GitHub Copilot, or Gemini Code Assist ships more code per hour, with less line-by-line review, than the same developer did in 2023. The absolute number of secrets reaching git per developer per week has increased because the absolute number of code changes reaching git per developer per week has **roughly doubled**» (iancloud.ai, secondary, согласуется с уже используемой в `coding-agent-mechanics.md` §3.1 цифрой «vibe coders generate 5-10x more commits»). Прямой мост к теме курса: рост throughput коммитов (уже обсуждается в главе для Conventional Commits, §3.3d) — тот же структурный фактор, что расширяет secret-leak surface — не два разных явления, а одно (агент пишет/коммитит больше и быстрее, ревью на строку — меньше) с двумя разными последствиями (нечитаемая история vs риск утечки).

**Confidence: MEDIUM** (secondary, но логически прямое и внутренне согласованное с уже принятыми в главе фактами о throughput).

### 5.3 Прямой, датированный кейс — Claude Code игнорирует .gitignore/.claudeignore для секретов (критично для §5.4 главы)

**Это самая важная, конкретная находка блока 5 — не абстрактный риск, а задокументированный, воспроизведённый случай именно с инструментом курса.**

**The Register, 2026-01-28**, «Claude Code ignores ignore rules meant to block secrets» (primary journalism, независимо верифицировано редакцией): Claude Code **читает** `.env`-файлы с секретами, даже когда они явно перечислены и в `.gitignore`, и в `.claudeignore`. Инструмент выводит предупреждение — «Note: This file contains credentials. Be cautious about committing it to version control» — **и всё равно печатает содержимое секретов**. Уязвимость независимо подтверждена журналистами на **Claude Code v2.1.12**. На момент публикации — минимум 4 открытых GitHub issue (два от ноября 2025, один за две недели, один за два дня до публикации, последний помечен «security-critical»); **«Anthropic did not respond to a request for comment»** (verbatim, на дату публикации issue оставались нерешёнными).

**Ключевое концептуальное разграничение из того же материала**, прямо усиливающее уже существующую в главе логику §5.4 (Lethal Trifecta/least-privilege): «"Ignored by git" and "ignored by Claude Code" are two different things, governed by different config files» — разработчик интуитивно полагает, что раз файл в `.gitignore`, агент «тоже» его не тронет, но это **два независимых механизма** (git отвечает только за то, что попадёт в коммит; агентский file-access — отдельный слой, с собственной, отдельно настраиваемой политикой).

**Confidence: HIGH** на факте существования уязвимости и её независимой верификации (primary journalism, конкретная версия ПО, конкретные GitHub issue); **`[VFY-day-of]` обязателен** — это активно отслеживаемая, незакрытая на дату публикации (2026-01-28) проблема; к дню лекции Anthropic могла выпустить патч или явную рекомендацию — необходимо перепроверить состояние (актуальную версию Claude Code, разрешён ли issue) непосредственно перед лекцией, не полагаться на состояние на 2026-01-28/2026-09-20.

### 5.4 Практическая митигация — deny-правила + честный предел (Bash bypass) + sandboxing

Практическое руководство (strongly.ai, «Stop Leaking Secrets to Claude Code: A Practical Security Setup») выделяет **три пути утечки**, требующих разной защиты: (1) прямое чтение файла (инструмент Read), (2) захват runtime-вывода (логи/stdout запущенного кода), (3) результаты поиска/grep (секрет попадает в контекст как часть окружающего совпадения).

Базовая защита — **deny-правила** в `~/.claude/settings.json`:
```json
{
  "permissions": {
    "deny": [
      "Read(./.env)", "Read(./.env.*)",
      "Read(**/*.pem)", "Read(**/*.key)",
      "Read(~/.aws/**)", "Read(~/.ssh/**)"
    ]
  }
}
```

**Критическая честная оговорка (прямая цитата, обязательно включить в главу, если цитируется этот паттерн):** «Read and Edit deny rules apply to Claude's built-in file tools, **not to Bash subprocesses**. A `Read(./.env)` deny rule blocks the Read tool but does **not** prevent `cat .env` in Bash» — то есть deny-правило создаёт **ложное чувство защищённости**, если агент имеет доступ к Bash: read-only bash-команды (`cat`, `grep`, `find`, `head`) часто выполняются **без permission-промпта** и полностью обходят file-tool-deny-правила.

**Реальное закрытие дыры — OS-level sandboxing**, применяющий kernel-level ограничение **ко всем** subprocess'ам, включая Bash:
```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": { "denyRead": ["~/.aws/credentials", "~/.ssh/**"] }
  }
}
```
Дополняющие практики того же источника: `.env.test` с фиктивными credentials для разработки, реальные production-секреты — только в vault (1Password, AWS Secrets Manager), `managed-settings.json` с `allowManagedPermissionRulesOnly: true` для принудительного применения политики на уровне команды (не полагаться на то, что каждый разработчик/агент сам настроит `deny`).

**Confidence: MEDIUM** на конкретном JSON-синтаксисе (practitioner-источник, не официальная документация Anthropic напрямую зафетчена в этом проходе — синтаксис похож на официальный формат `permissions.deny`, уже использующийся в экосистеме Claude Code, но сам этот конкретный пример — вторичный); **HIGH** на самом факте «deny rules не покрывают Bash subprocesses» — это прямое, логически проверяемое следствие архитектуры (file-tool permission layer ≠ process-level sandboxing), согласуется с §5.3.

### 5.5 Прямой мост к §5.4 главы (Lethal Trifecta) — не новая категория, а конкретизация уже введённой

Курс уже разбирает Lethal Trifecta (untrusted content + доступ к чувствительным данным + канал эксфильтрации) в `methodics-as-practice.md`/`methodologists-and-failures.md` и в §2.2 `coding-agent-mechanics.md` (MCP как вектор). **Находка §5.3-5.4 этого блока — не новая угроза, а конкретный, датированный, воспроизведённый механизм именно для «доступ к чувствительным данным»-угла трифекты**, применённый к самому инструменту курса: `.env`-файл с секретами в репозитории — это чувствительные данные; если агент также обрабатывает untrusted content (чужой issue/PR-комментарий, внешний MCP-источник) **и** имеет канал наружу (создание PR, вызов внешнего API) — комбинация «агент читает `.env`, несмотря на .gitignore» превращает абстрактный риск трифекты в конкретно воспроизводимый инцидент, а не гипотетический. Рекомендация для §5.4 главы: использовать этот кейс как **предметный пример «доступ» угла трифекты**, ровно так же, как GitHub MCP CamoLeak/CVE-2025-59145 уже используется как пример «эксфильтрация»-угла (уже в `methodologists-and-failures.md`) — оба кейса усиливают друг друга методически (один — про канал наружу, другой — про то, что «эта папка защищена .gitignore» не значит «агент её не видит»).

**Confidence: HIGH** на логической связке (прямое применение уже HIGH-confidence фреймворка главы к новому, независимо подтверждённому кейсу).

---

## Источники (полный список, доступ 2026-09-20, если не указано иное)

**Блок 1 — Freshness:**
1. https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/ — официальный blog-пост, 2025 Developer Survey результаты (primary, HIGH)
2. https://survey.stackoverflow.co/2025 — сам отчёт, точные цифры (primary, HIGH)
3. https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/ — 2026-волна открыта для сбора данных, результатов ещё нет (primary, HIGH)
4. https://byteiota.com/stack-overflow-dev-survey-2026-ai-at-84-trust-at-3/ — пример путаницы «2026 в заголовке = данные 2025» (secondary, honesty-flag источник)
5. https://www.gitclear.com/the_ai_code_quality_maintainability_gap — «The Maintainability Gap: AI Code Quality in 2026», v2026.6.1, июнь 2026, 623M изменений (primary vendor, HIGH на фактах/числах, MEDIUM на методологии — self-published)
6. https://www.arturmarkus.com/ai-code-quality-by-the-numbers-623-million-changes-refactoring-down-70-duplication-up-81/ — пересказ отчёта с числами, публикация 2026-09-04 (secondary, MEDIUM)

**Блок 2 — Академическая литература skills:**
7. https://arxiv.org/abs/2602.20867 — «SoK: Agentic Skills» (Jiang et al., 2026-02-24) (primary preprint, HIGH на содержании)
8. https://arxiv.org/abs/2602.12430 — «Agent Skills for LLMs: Architecture, Acquisition, Security» (Xu & Yan, workshop ACM AI & Agentic Systems '26) (primary preprint, HIGH на содержании, workshop-уровень)
9. https://arxiv.org/html/2606.20631v1 — «Harnessing Agent Skills» (Xia et al., CSIRO's Data61-affiliated, 2026-05-29) (primary preprint, HIGH на содержании)
10. https://arxiv.org/abs/2607.25032 — **«Authoring Agent Skills: A Software-Engineering Approach»** (Destefanis, 2026-07-27, cs.SE) — прямая находка (primary preprint, MEDIUM-HIGH, single-author/no peer review yet)

**Блок 3 — Локальный test-tooling:**
11. https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/ — Testcontainers Python (primary vendor, HIGH)
12. https://qaskills.sh/blog/testcontainers-python-pytest-integration-guide — Testcontainers+pytest практика 2026 (secondary, MEDIUM)
13. https://mswjs.io/docs/ — Mock Service Worker официальная документация (primary, HIGH)
14. https://qaskills.sh/blog/api-mocking-service-virtualization-guide — MSW vs WireMock, «invented response shape» gap (secondary, MEDIUM)
15. https://www.wiremock.io/ — WireMock Cloud, AI Agent Skills/MCP (vendor, MEDIUM) — честно разделено от локального OSS-ядра в §3.3
16. https://wiremock.org/ — WireMock OSS core (primary vendor, HIGH)
17. https://www.distillabs.ai/blog/distil-pytest-generator/ — pytest-generator, локальная 8B-модель, 2026-02-18 (primary vendor, LOW-MEDIUM на зрелости)
18. https://github.com/pablodt00/rate-limiter/issues/12 — пример локального lint+type-check+test Claude Code skill-паттерна (primary repo example, MEDIUM)

**Блок 4 — SDD:**
19. https://github.com/github/spec-kit/blob/main/spec-driven.md — канонический источник «SDD» в мейнстримном значении (primary, HIGH)
20. https://aws.plainenglish.io/what-is-spec-driven-development-and-how-to-implement-it-with-kiro-b5846bd55869 — AWS Kiro SDD-позиционирование (secondary/practitioner про official AWS product, MEDIUM)
21. https://intent-driven.dev/blog/2026/08/23/tdd-bdd-spec-driven-development/ — Hari Krishnan (автор книги Manning), altitude-framing TDD/BDD/SDD (primary author blog, MEDIUM-HIGH)
22. https://testrigor.com/blog/what-is-test-driven-development-tdd-vs-bdd-vs-sdd/ — альтернативное, вендор-специфичное «SDD» у testRigor (primary vendor, честно другой термин — honesty flag §4.2)
23. https://en.wikipedia.org/wiki/Spec-driven_development — факт наличия энциклопедической статьи (для контекста устоявшести термина)

**Блок 5 — Secrets:**
24. https://www.decryptiondigest.com/blog/secrets-scanning-pre-commit-ci-enforcement — Eric Bang CISSP, трёхслойная модель pre-commit/CI/GHAS, 2026-05-21/06-25 (independent security publication, MEDIUM)
25. https://appsecsanta.com/secret-scanning-tools/gitleaks-vs-trufflehog — Gitleaks vs TruffleHog сравнение (secondary, MEDIUM)
26. https://iancloud.ai/blog/secrets-scanning-pre-commit-era-gitleaks-trufflehog-semgrep-2026 — AI coding assistants → удвоенный объём изменений → бОльшая leak-surface (secondary, MEDIUM)
27. https://www.theregister.com/software/2026/01/28/claude-code-ignores-ignore-rules-meant-to-block-secrets/4336684 — **прямой, датированный кейс**: Claude Code v2.1.12 читает .env вопреки .gitignore/.claudeignore (primary journalism, независимая верификация, HIGH)
28. https://www.strongly.ai/blog/stop-leaking-secrets-claude-code.html — практическая митигация: permissions.deny + честный предел (Bash bypass) + sandboxing (practitioner guide, MEDIUM)

---

## Honesty flags / gaps (declared)

1. **SO Developer Survey «2026»** (§1.1) — на дату research (2026-09-20) полных результатов 2026-волны **нет**; несколько вторичных публикаций озаглавлены «2026», но фактически пересказывают данные 2025-отчёта (опубликован дек. 2025, собран май-авг. 2025). Глава должна продолжать явно писать «SO Developer Survey 2025», не «2026» — иначе это будет самостоятельная фактическая ошибка, а не просто «устаревшие данные». `[VFY-day-of]`: полная 2026-волна может выйти до дня лекции.
2. **GitClear дата релиза версии 2026.6.1** (§1.2) — расхождение между вторичными упоминаниями «январь» vs «июнь» 2026; принята версия из номера самого релиза (2026.6.1 → июнь), но не 100% независимо разрешено. `[VFY-day-of]`.
3. **Академическая работа Destefanis (§2.3)** — единственный автор, препринт без заявленного peer review на дату фетча (2607.25032, 2026-07-27) — сильная прямая находка по содержанию, но НЕ устоявшийся канон; не преувеличивать зрелость академического поля здесь.
4. **26.1% vulnerable community skills** (§2.2, Xu & Yan) — цифра из workshop-paper (ACM AI & Agentic Systems '26 Workshop — не основной track конференции), не независимо воспроизведена другим источником в этом проходе — использовать с явной атрибуцией «по данным одной workshop-работы», не как общепринятый факт.
5. **WireMock local-vs-cloud AI-слой** (§3.3) — явно зафиксировано разделение между OSS-ядром (HIGH, локальное) и AI-фичами (преимущественно на WireMock Cloud, платный SaaS) — если глава упоминает WireMock как «локальный AI-инструмент», это будет неточно без этой оговорки.
6. **pytest-generator (Distil Labs) точность ≈77%** (§3.4) — self-reported вендором, не независимо измерено в этом проходе; инструмент очень новый (7 месяцев на дату research), низкая подтверждённая adoption.
7. **Два разных «SDD»** (§4.2) — testRigor заявляет собственное авторство термина «Specification-Driven Development (SDD)» с иным позиционированием, чем мейнстримная GitHub/AWS-линия «Spec-Driven Development (SDD)»; источники не разрешают вопрос «кто был раньше» — только оба use зафиксированы честно, без выдуманного приоритета.
8. **Claude Code .env-уязвимость (§5.3)** — на дату публикации The Register (2026-01-28) минимум 4 открытых GitHub issue, Anthropic не ответила на запрос комментария; статус на дату лекции **не проверен в этом research-проходе** (не переходили по свежим GitHub issue после 2026-01-28) — **обязательный `[VFY-day-of]`**: перепроверить, есть ли патч/официальная позиция Anthropic непосредственно перед лекцией, версию Claude Code на момент лекции.
9. **`settings.json` sandbox-синтаксис** (§5.4) — конкретный JSON взят из practitioner-руководства (strongly.ai), не подтверждён прямым фетчем официальной документации Anthropic в этом проходе — синтаксис правдоподобен и согласован с уже известной по другим research-файлам курса механикой `permissions.deny`, но перед использованием в главе как «дословный официальный пример» стоит сверить с `code.claude.com/docs` напрямую.
10. **Общий кросс-блоковый flag:** все пять блоков этого прохода содержат минимум один `[VFY-day-of]`-элемент (SO-2026 волна, GitClear версионирование, Claude Code .env-патч-статус, WireMock/Postman product roadmap) — это ожидаемо для быстро меняющегося 2026-ландшафта AI-tooling, не признак недостаточного research, но orchestrator должен включить явный день-лекции-чеклист по этим пунктам.

# Lecture 4 — Methodology & Tooling Expansion: Worktrees, BDD, Trunk-based refresh, Test-tooling depth, Requirements-as-code, Documentation mechanics

**Date:** 2026-09-20 · **Researcher:** fact-checker research subagent · **Issue:** #162 (продолжение расширения после roast — новый раунд по прямому owner-запросу)
**Purpose:** research для `book-editor`, расширяющего §1 «Требования», §3 «Реализация», §4 «Тестирование», §6 «Доставка/документация» главы Лекции 4 (`library/lectures/lec-04/chapter.md` + `chapter-part2..5.md`).
**Sibling files (read first, NOT re-derived here):** `progression-and-configs.md` (существующая таблица «Методологии × ИИ», строки Trunk-based и Pair/ensemble — здесь блок 3 её углубляет, не переписывает с нуля), `coding-agent-mechanics.md` (образец формата этого прохода: Confidence HIGH/MEDIUM/LOW, `[VFY-day-of]`, честные gaps).
**Access date для всех URL:** **2026-09-20**, если не указано иное. `[VFY-day-of]` = волатильный факт (версия продукта/фича/цифра), перепроверить в день лекции.
Confidence: **HIGH** = первичный источник (vendor docs, canonical spec) · **MEDIUM** = practitioner consensus / vendor blog / secondary · **LOW** = единичный блог / emerging / anecdotal.

**Куда должно попасть каждое:** блок 1 → §3.2/§3.3 главы (организация среды, харнес — уже есть секция про Multi-Lecture Parallel Production как курс-пример); блок 2 → §1 (требования, мост к BDD от Gherkin-как-спеки) и §4 (тестирование, executable spec); блок 3 → §3.3d (git-конвенции, следующий уровень поверх Conventional Commits/Branch); блок 4 → §4 (за пределами Playwright, который уже в §3.3c); блок 5 → §2 (architecture-as-code, но для требований — явная параллель, не новая категория) и §1; блок 6 → §6 (документация — сейчас в главе только имена вендоров, здесь конкретика).

---

## 1. Git worktree для параллельной работы агентов

### 1.1 Что это — определение и self-referential курс-пример

Git worktree — отдельная рабочая директория со своими файлами и своей веткой, но с **общей** историей репозитория и общим `.git`-хранилищем объектов с основной копией. Официальная документация Claude Code формулирует практический эффект дословно: «Running each Claude Code session in its own worktree means edits in one session never touch files in another, so one session can build a feature while a second fixes a bug» (code.claude.com/docs/en/worktrees, primary, доступ 2026-09-20).

**Это не гипотетическая практика — курс уже её формализовал и использует.** `CLAUDE.md` этого репозитория содержит раздел «Multi-Lecture Parallel Production (ENFORCED)», предписывающий именно git worktree isolation при параллельной работе над несколькими лекциями (несколько Claude Code-сессий с общим `.git`):

> «**Use git worktree isolation MANDATORY:**
> ```bash
> git worktree add --detach /tmp/lec-NN-wt <base-commit>
> cd /tmp/lec-NN-wt && git checkout -b phase-X-Y
> ```»

и далее — конкретная причина, по которой это правило появилось: «Лекция 2 production имела ~2 hours wasted на branch contention recovery (lec-04 parallel session, shared `.git`). Worktree isolation после Phase 8.5 полностью eliminated issue.» Это честный, реально пережитый инцидент курса, а не абстрактная иллюстрация — годится как **прямой self-referential кейс** для главы: «мы сами хлебнули branch contention, worktree решил именно эту проблему».

**Confidence: HIGH** (первичный источник Anthropic + собственный CLAUDE.md курса как первичный внутренний источник).

### 1.2 Механика (официальная документация Claude Code, 2026)

Конкретные факты из первичного источника (code.claude.com/docs/en/worktrees, verbatim/близко к тексту):
- Флаг `claude --worktree <name>` (или `-w`) создаёт изолированный worktree и стартует в нём сессию; по умолчанию — под `.claude/worktrees/<name>/` на новой ветке `worktree-<name>`.
- Можно попросить саму модель «work in a worktree» в ходе сессии — она вызовет инструмент `EnterWorktree`.
- **Изоляция enforced инструментом, а не только соглашением**: Claude Code блокирует Edit/Write/NotebookEdit на путях основной рабочей копии, блокирует команды с рабочей директорией внутри основного checkout, блокирует git-редиректы (`git -C`, `--git-dir`, `GIT_DIR`/`GIT_WORK_TREE`) в основной checkout. Это отличает Claude Code worktree от «голого» `git worktree add`, где такой защиты нет.
- Для сабагентов — `isolation: worktree` в frontmatter агента делает изоляцию постоянной (`.claude/agents/*.md`), то есть параллельные сабагенты автоматически получают отдельные worktree без ручной настройки каждый раз.
- Общее между worktree и основной копией: **`.git`-директория репозитория** (то есть история и объекты не дублируются — экономия дискового пространства и времени клонирования), project-scope плагины, сохранённые permission-approvals.

**Confidence: HIGH** (первичная документация, версии API вроде `v2.1.198+` волатильны — `[VFY-day-of]` на точные номера версий).

### 1.3 Зачем worktree лучше отдельных `git clone` — для агентного workflow конкретно

Прямое сравнение (синтез курса из первичного источника §1.2 + community-практики):
- **Общий `.git` object store** — worktree не скачивает и не хранит историю репозитория повторно (в отличие от `git clone`, который дублирует весь объектный граф); при большом репозитории это экономия дискового места и времени старта параллельной сессии.
- **Быстрое переключение и настройка** — создание worktree — операция в секунды поверх уже существующей истории, тогда как повторный `clone` + `npm install`/`pip install` в отдельной копии — минуты; агенту, которому нужно быстро развернуть параллельную задачу, это прямая экономия.
- **Общие permission-approvals и плагины** (см. §1.2) — то, что отдельный `clone` физически не может унаследовать, потому что для git это уже другой репозиторий, а не другая рабочая копия одного и того же.
- **Изоляция файловых правок при общей истории** — именно то сочетание, которое нужно параллельным агентам: не видеть чужие незакоммиченные изменения (в отличие от одной общей рабочей копии), но иметь общую точку интеграции через ту же историю (в отличие от полностью разделённых clone на разных ветках без единого источника правды).

Community-подтверждение (не vendor-канон, но независимая конвергенция нескольких источников): «Git worktrees enable parallel AI agent execution by giving each agent its own isolated working directory and git index while sharing a single object store, preventing file-level conflicts, context contamination, and lock contention when multiple agents work simultaneously» (augmentcode.com, secondary, 2026). Практический паттерн: «plan first, define shared contracts, split work by ownership boundaries, isolate each worker in a git worktree, run tests per worker, then validate the merged result in one final pass» (mindstudio.ai / aakashx.com — вторичные practitioner-блоги, независимо сходятся на одном workflow).

**Confidence: HIGH** на механике (общий object store, экономия — свойство самого git, документировано `git-scm.com/docs/git-worktree`); **MEDIUM** на «зачем это агентам конкретно» синтезе (community-консенсус нескольких блогов 2026, не единый vendor-канон).

### 1.4 Как это описывает сама Anthropic/индустрия — рамка для лекции

Прямая vendor-позиция: инженер, создавший Claude Code (Борис Черни), в публичном посте (X, февраль 2026) назвал worktree-паттерн приоритетом №1: «Spin up 3-5 git worktrees at once, each running its own Claude session in parallel. It's the single biggest productivity unlock, and the top tip from the team» (вторично процитировано несколькими источниками, включая blog.vibecoder.me; сам твит не зафетчен напрямую в этом проходе — **honesty flag**: цитата вторичная, не первоисточник X.com). Нативная поддержка `--worktree` вошла в CLI как Claude Code v2.1.49 (февраль 2026, `[VFY-day-of]` — версия волатильна).

Практическая рекомендация по числу параллельных worktree расходится по источникам: «Anthropic recommends 3–5 agents for most workflows, with diminishing returns beyond that» (вторичный источник) vs «teams are running 4–8 concurrent worktrees per developer reliably. Above that, you're usually bottlenecked on review, not on Claude» (другой вторичный источник, augmentcode.com). Обе цифры — **не из официальной документации Anthropic напрямую** (в самой странице code.claude.com/docs/en/worktrees конкретного числа-рекомендации не приведено) — честно помечаем как community-оценку, а не vendor-цифру.

**Что честно НЕ vendor-канон, а «практика сообщества»** (как просил orchestrator, не выдумывать эквивалентность): IDE-поддержка worktree (JetBrains 2026.1 март 2026, VS Code июль 2025) — это адаптация экосистемы к паттерну, который уже возник в practitioner-практике, а не сам паттерн, изобретённый вендором IDE. Число параллельных worktree (3-5 или 4-8) — блог-консенсус, не измеренная норма.

**Confidence: MEDIUM** на конкретных числах и авторстве твита (вторичные источники); **HIGH** на самом факте нативной поддержки в Claude Code (описано в первичной документации §1.2).

---

## 2. BDD (Behavior-Driven Development) + AI

### 2.1 Что такое BDD — определение и три практики (Cucumber, canonical)

Официальное определение (cucumber.io/docs/bdd/, primary): «BDD is a way for software teams to work that closes the gap between business people and technical people by... Producing system documentation that is automatically checked against the system's behaviour». Три практики цикла:
1. **Discovery** («What it *could* do») — структурированные разговоры вокруг конкретных примеров, чтобы построить общее понимание.
2. **Formulation** («What it *should* do») — превращение примеров в исполняемые, человекочитаемые спецификации (Gherkin).
3. **Automation** («What it *actually does*») — использование исполняемых спецификаций как тестов, направляющих реализацию.

Формат Gherkin — **Given-When-Then**: Given (исходное состояние/контекст) → When (действие/событие) → Then (ожидаемый результат). BDD **дополняет**, а не заменяет agile-процесс: «a set of plugins for your existing process» — предполагает, что команда уже работает user-story-инкрементами.

**Confidence: HIGH** (первичный источник, canonical для терминологии BDD).

### 2.2 Кто пишет feature-файлы с AI в 2026 — конкретная механика

По практическим источникам 2026 года: «Claude, Cursor, and other AI agents now generate Gherkin from acceptance criteria and produce matching step definitions» (qaskills.sh, secondary/practitioner, 2026). Конкретный workflow, встречающийся в нескольких источниках: AI выявляет **не только happy path**, но добавляет граничные значения, security-проверки и edge cases в сценарии, определяя Given/When/Then по требованиям — то есть та же роль, что AI уже играет в спека-интервью §1.2 главы (структурирование и полнота, а не решение о поведении). Человек (аналитик/PM/тимлид) **ревьюит** сгенерированные сценарии — прямая параллель с человеческим чекпойнтом spec-driven (§1.1-1.2 главы), только на уровне отдельного поведенческого сценария, а не всей спеки.

Явный практический источник (Andy Knight / Automation Panda, известный BDD/Gherkin-практик, 2026-04-27, automationpanda.com) фиксирует конкретную проблему AI-генерации: «AI-generated Gherkin often drifts into vague `Then` steps, UI-heavy scripts, multi-behavior scenarios, and placeholder examples that read like filler» — то есть без явных правил AI-сгенерированный Gherkin **деградирует по качеству** (расплывчатые проверки, привязка к UI вместо поведения, несколько поведений в одном сценарии). Решение — тот же паттерн, что AGENTS.md/CLAUDE.md (§3.2 главы): явный `gherkin-guidelines.md`, подключаемый как контекст к AI-инструменту (Claude, Cursor, Copilot), а не полагание на «модель и так знает, как писать хороший Gherkin». Автор прямо формулирует зависимость от контекста, не от модели: «Good specs are a team sport, and this file is here to make your first pass a little lighter and a lot clearer».

**Confidence: MEDIUM** (practitioner-консенсус нескольких независимых источников 2026, не единая vendor-спецификация уровня Cucumber core).

### 2.3 Инструменты 2026

- **Cucumber** остаётся «de facto reference implementation» BDD (qaskills.sh); альтернативы — SpecFlow/Reqnroll, Behave (Python), Gauge, Karate, JBehave.
- **Gherkinizer** (gherkinizer.com) — AI-инструмент на базе моделей Gemini, генерирующий Gherkin-сценарии из user stories, совместимые «out of the box» с Cucumber и другими BDD-фреймворками (vendor-заявление, не независимо верифицировано).
- **MCP-паттерн для агентной QA** — по аналогии с §3.3c главы (MCP для кодинг-агента), для тестирования упоминается подключение автономного QA-агента к внешним инструментам (GitHub, browser automation) через MCP — концептуально идентично паттерну §3.3c, не новая категория механики.

**Confidence: LOW-MEDIUM** на конкретных именах инструментов (быстро меняющийся вендорский ландшафт, `[VFY-day-of]`).

### 2.4 Честно: BDD менее мейнстримный, чем TDD, в агентном контексте

**Это подтверждается, и нужно сказать прямо, не преувеличивая BDD-популярность.** Конкретная эмпирика: по выборке open-source проектов, использующих тестовые фреймворки, BDD-фреймворки применяются примерно в **27%** проектов (наибольшая распространённость в Ruby — 68%, где RSpec/Cucumber исторически доминируют) — то есть в остальных экосистемах BDD **не** доминирующая практика (303software.com, «BDD & Cucumber Reality Check 2025», secondary/practitioner analysis, 2025). Тот же источник фиксирует разрыв между принятием инструмента и принятием методологии: «while they understand the intended purpose of BDD frameworks, most of them write tests while/after coding rather than strictly applying BDD» — то есть команды часто используют Cucumber **как** тестовый DSL, не проводя discovery-фазу с бизнесом, ради которой BDD и задуман. Ещё одна честная оговорка того же источника про центральный тезис BDD (сотрудничество техов и нетехов): «The intended collaboration between technical and non-technical stakeholders often doesn't materialize in practice, limiting BDD's core value proposition», и практическая жалоба практиков: «feature files can never truly be read and written by everyone on a team».

**Прямого источника**, специально сравнивающего популярность BDD vs TDD **именно в контексте AI-агентов** (а не вообще), в этом проходе **не найдено** — это честный gap, а не потому что различия нет: TDD как дисциплина уже разобран в главе (§4) как методология №1 по «прилеганию» к AI именно потому, что тест = маленькая исполняемая единица, которую агент может прогнать сам в цикле (§3.1 главы, малые проверяемые единицы). BDD решает **другую** задачу — не «дать агенту детерминированный feedback-loop на уровне кода», а «зафиксировать бизнес-намерение на языке, понятном не-инженеру» — и по своей природе требует **человеческого** (не только AI) сотрудничества discovery-фазы, которую AI не заменяет и не ускоряет тем же способом, что TDD-цикл. **Честная формулировка для главы:** BDD — не конкурент TDD «по прилеганию к AI», а инструмент **другого уровня спецификации** (бизнес-язык vs код), применимый там, где нужен именно этот мост; в чисто инженерных задачах без бизнес-стейкхолдера рядом BDD часто избыточен — тот же критерий соразмерности, что уже введён в §1.5 главы для spec-driven (цена дисциплины vs цена ошибки).

**Confidence: MEDIUM** на цифре 27%/68% (единичный secondary-анализ, не воспроизведённое независимо измерение — `[VFY-day-of]`); **HIGH** на честности вывода «BDD менее мейнстримный инструмент, чем TDD» (согласуется с несколькими независимыми источниками §2.2-2.4, ни один не утверждает обратного).

### 2.5 Мост к TDD и к §4 главы

Параллель, прямо формулируемая в источниках и логически прозрачная: TDD — исполняемая спецификация **на уровне кода** (юнит-тест, написанный до реализации); BDD — исполняемая спецификация **на уровне бизнес-языка** (Given-When-Then сценарий, написанный до реализации, но читаемый нетехническим стейкхолдером). Оба — конкретные реализации одного и того же принципа «тест до кода = точный контракт для AI», разница — в аудитории и уровне абстракции спецификации, не в механике цикла. Это прямой мост от §1.2 главы (deliberative alignment — «спека как основа для проверок», OpenAI) — Gherkin-сценарий и есть один из конкретных форматов такой «спеки-как-проверки», просто ориентированный на бизнес-читателя, а не только на модель.

---

## 3. Trunk-based development + AI — свежая (2026) перепроверка

*(Углубляет существующую строку `progression-and-configs.md` §3 «Trunk-based + CI/CD» — не переисследует TDD/DORA-часть заново, добавляет 2026-специфику и явную связь с Conventional Branch §3.3d главы.)*

### 3.1 Почему высокий throughput агентных коммитов требует trunk-based

Конкретная, недавняя (2026) формулировка проблемы long-lived веток именно с AI-агентом: «Long-lived branches get even worse when you add an AI agent to the mix, since by the time you merge, half the agent's assumptions are wrong» — «When an AI agent writes code against a branch while main moves on underneath it, a long-lived branch means half the agent's assumptions are wrong by the time you merge» (journal.daniellopes.dev, 2026, secondary/practitioner). Механизм честно объяснён: git разрешает **текстовые** конфликты автоматически, но не разрешает **семантические** — «Git resolves the textual conflicts while nobody resolves the semantic ones» — а именно семантический дрейф допущений модели (переименованные функции, изменившиеся контракты) растёт пропорционально времени жизни ветки и объёму изменений в main за это время.

DORA-подтверждение (первичный со-источник, уже используемый главой для других выводов §6.2/§7.2): «DORA's research backs trunk-based development as a high-performance practice, defining a short-lived branch as one that lives under 24 hours» (вторично процитировано, но исходная метрика DORA — устойчивый многолетний вывод отчётов, не разовое заявление 2026 года). Практическая связка с feature flags: «feature flags let you merge incomplete features into the trunk safely, controlling which users see new functionality before full release... evaluated at runtime... without changing your code» (flagsmith.com / harness.io, secondary vendor blogs, механика фичи стандартна и не вендор-специфична).

**Инженерный вывод для §3.3d главы:** trunk-based + feature flags — это **разрыв связи** между «когда код смержен» и «когда пользователь видит фичу»: агент может смержить маленький, часто, в trunk (что нужно для короткой ветки и для читаемого diff, §3.1 главы), а раскатка контролируется отдельно флагом — то есть не нужно держать ветку живой до полной готовности фичи, чтобы не «протекать» в прод недоделанное.

**Confidence: HIGH** на DORA-связке short-lived-branch → performance (устойчивый многолетний вывод, используемый главой и для других выводов); **MEDIUM** на «AI-агент делает long-lived ветки хуже» синтезе (одна конкретная 2026 formulировка + логическая экстраполяция от общего механизма трифекты допущений, не отдельное измерение).

### 3.2 Связь с Conventional Branch/Commits (§3.3d главы) — следующий уровень

Глава уже вводит Conventional Commits/Branch (§3.3d, из `coding-agent-mechanics.md`) как **формат** имени коммита/ветки. Trunk-based — это **следующий слой** поверх того же материала: не про то, **как называть** ветку (`claude/security-patch`), а про то, **сколько она живёт** и **как часто интегрируется** с trunk. Явная связка для главы: сама AI Agent Source Prefix-конвенция (`claude/`, `codex/`, `ai/`) имеет смысл именно в trunk-based-режиме — если ветка живёт часами, а не неделями, префикс «эта ветка от агента X» — сигнал ревьюеру для быстрого, частого ревью маленьких diff, а не для «отложенного большого ревью раз в две недели». В long-lived-ветках сценарии тот же префикс работал бы хуже — большой diff, накопленный за недели, всё равно нужно ревьюить целиком, вне зависимости от того, что его писал агент.

**Итоговая формулировка для §3.3d:** git-конвенции (имя коммита/ветки) отвечают на вопрос «как читается история», trunk-based отвечает на вопрос «как часто история интегрируется» — обе практики усиливают друг друга именно в контексте высокого throughput агентных коммитов (§3.1, `coding-agent-mechanics.md`: «vibe coders generate 5-10x more commits than traditional developers»), но это два разных уровня дисциплины, и глава должна их не смешивать.

**Confidence: HIGH** на логической связке (прямое следствие уже введённых в главе понятий, не отдельное новое эмпирическое утверждение).

---

## 4. Тестовый инструментарий за пределами Playwright

*(Playwright MCP уже разобран в §3.3c главы как e2e-браузерный инструмент. Здесь — соседние категории: API, БД/интеграционные тесты, frontend за пределами e2e.)*

### 4.1 API-тестирование — Postman AI Agent Builder / Agent Mode

Postman в 2026 году провёл заметную AI-native перестройку продукта: «In March 2026, Postman launched a rebuilt AI-native platform for the agentic era, featuring Git-connected Workspaces, an API Catalog... and an AI intelligence layer integrated throughout the platform» (blog.postman.com, primary vendor, 2026-03, `[VFY-day-of]`). Конкретные механики:
- **Agent Mode** — «turn your words into action across the API lifecycle. Send requests, fix errors, update tests, and more, using natural language» (blog.postman.com, primary) — то есть естественно-языковой интерфейс поверх существующих операций Postman (не отдельная новая парадигма).
- **AI Engineer** (запущен 2026-06-02, `[VFY-day-of]`) — «a cloud-native agent that handles the full surface area of API work: design, debugging, documentation, testing, and integration orchestration»; способен «run API and QA tests on every pull request and then post results back into existing developer workflows» — то есть это конкретно CI-интегрированный агент, а не просто ассистент внутри IDE-приложения.
- **AI Protocol** — расширение той же тестовой платформы на тестирование самих LLM-моделей «treating large language models like powerful APIs» (систематическое тестирование system/user prompt, бенчмарк по времени ответа/точности/стоимости) — примечательно тем, что тот же инструмент, которым тестируют REST API, применяется к самим моделям.

**Честная оговорка о зрелости:** это очень свежие фичи (март/июнь 2026), заявления вендора не независимо верифицированы третьей стороной в этом проходе — не подавать как устоявшуюся практику, а как «то, куда движется категория» с явным `[VFY-day-of]`.

**Confidence: MEDIUM** (первичный vendor-блог, но без независимой верификации по факту эффективности; сами фичи и их существование подтверждены, эффект — не измерен).

### 4.2 Тестирование с БД — Testcontainers

Testcontainers — библиотека, поднимающая **реальный** сервис (Postgres, Kafka, Redis и др.) в Docker-контейнере на время тестового прогона, на эфемерном порту, и уничтожающая его после: «Testcontainers turns traditionally heavy dependencies into lightweight, ephemeral test instances that your code can interact with as if they were real services» (java.testcontainers.org / связанные вторичные источники, 2026). Практическая позиция в 2026: «Testcontainers has become the default approach to integration testing for any team that takes correctness seriously» (qaskills.sh, secondary, formulировка, а не измеренный факт adoption).

**Связь с AI-агентом.** AI-специфика здесь — не «AI придумал Testcontainers», а конкретный паттерн **skill** (прямой мост к §3.3b главы Skills): «when you install a skill like testcontainers-docker, your AI agent gains knowledge about how to write Docker Compose configurations for test environments, transforming your AI agent from a generic code generator into an environment-aware testing partner that understands the infrastructure context of your tests» (devblogs.microsoft.com / qaskills.sh, secondary). То есть зрелость AI-фичи здесь **низкая в смысле «умного диффинга» или «автономного анализа»** и **высокая в смысле «AI знает конвенции написания правильной конфигурации»** — ровно то различие, которое уже вводит §3.3b главы про on-demand компетенцию: skill не делает модель умнее в вакууме, он даёт ей процедурное знание конкретного инструмента (в данном случае — Docker Compose / Testcontainers API) вместо угадывания по памяти.

**Инженерный вывод для §4 главы:** эфемерная БД в контейнере — это тот же принцип детерминированного харнеса (§3.3 главы, Бёкелер): агент получает **реальную**, но одноразовую и изолированную БД, на которой его интеграционный тест либо детерминированно проходит, либо детерминированно падает — то есть Testcontainers для интеграционных тестов closes тот же gap, что unit-тест для юнита: даёт AI-агенту способ **проверить себя** без человека в цикле на каждом шаге.

**Confidence: HIGH** на самой механике Testcontainers (устоявшийся, немолодой инструмент, задокументированное поведение); **MEDIUM** на «AI-специфике через skill-паттерн» (свежий, 2026-й, конкретно-практический пример, не vendor-канон Testcontainers).

### 4.3 Frontend-тестирование за пределами e2e — компонентное и визуальное

Категория **компонентного тестирования** (изолированный рендер и проверка отдельного UI-компонента, а не целого пользовательского флоу, как e2e Playwright) и **visual regression** (сравнение скриншотов до/после для обнаружения непреднамеренных визуальных изменений) — в 2026 году поделены на два лагеря: «AI-diffing cloud platforms (Percy, Applitools, Chromatic, Reflect) and developer-owned snapshot libraries baked into frameworks (Playwright, Cypress, BackstopJS)» (saucelabs.com, secondary aggregator, 2026).

- **Chromatic** — визуальное тестирование, построенное специально под Storybook-компонентные workflow: «enables teams to automatically capture UI snapshots of components and detect visual changes before they reach production»; «wins for Storybook-driven component teams — every story becomes a visual test, with TurboSnap cutting snapshot costs» (те же snapshot-издержки, что и Playwright screenshot-диффинг, но заточен на **компонент**, не страницу целиком).
- **Percy** (BrowserStack) — «Percy's Visual Review Agent claims a 3x review-time reduction and ~40% fewer false positives» (percy.io, vendor-заявление — **честная оговорка: это self-reported число вендора, не независимое измерение**, аналогично тому, как глава уже критично относится к вендорским бенчмарк-цифрам в §3 «SWE-bench лидеры»).
- **Applitools** — конкурирующий AI-diffing подход, «AI-powered visual validation» — акцент на снижении false positives через визуальное AI-сравнение вместо пиксель-в-пиксель diff.

**Честная оговорка о зрелости.** Это отдельная от e2e (Playwright, §3.3c главы) задача: «Functional automation answers whether the software works according to programmed behavior, while visual regression testing establishes whether the software still presents that behavior correctly to a user» (одна из тех же source-статей) — то есть e2e и visual regression **дополняют**, не заменяют друг друга: тест Playwright может пройти (кнопка кликается, форма отправляется), а visual regression поймает, что кнопка съехала или стала невидимой из-за CSS-регресии. AI-диффинг здесь **зрелее**, чем в API/DB-категориях §4.1-4.2 (индустрия визуального регрессионного тестирования существует дольше и AI-diffing — не новая для неё идея), но конкретные вендорские цифры (3x, 40%) остаются self-reported, не независимо верифицированы в этом проходе.

**Confidence: MEDIUM** на всей категории (устоявшийся рынок инструментов, но конкретные AI-эффективность-цифры — vendor-заявления).

---

## 5. Визуализация требований — тот же Mermaid/DSL-подход, другой артефакт

**Честный вывод сразу:** отдельной новой категории инструментов здесь **нет** — источники подтверждают ровно то, о чём просил orchestrator: практика визуализации требований использует **тот же** code-as-diagram подход (Mermaid/DSL), что architecture-as-code (§2.4 главы, C4/Mermaid/PlantUML/Structurizr), просто применённый к другому артефакту (пользовательский путь/требование, а не архитектурный компонент).

### 5.1 Mermaid User Journey — конкретика

Mermaid — «a JavaScript-based charting and diagramming tool that lets you represent diagrams using text and code, which simplifies maintenance… diagrams in code simplify maintenance and ensure that the code is supported by version control systems» (mermaidchart.com / mermaidstudio.dev, primary/vendor docs). User Journey Diagram — конкретный тип диаграммы Mermaid: «describe at a high level of detail exactly what steps different users take to complete a specific task within a system... shows the current (as-is) user workflow, and reveals areas of improvement for the to-be workflow». Структура: Title → Sections (фазы пути) → Tasks (действия, с оценкой 1-5 «опыта» и Actors — кто вовлечён).

**Прямая параллель со §2.4 главы (C4-как-код):** та же логика — версионируемый, диффабельный, ревьюируемый текстовый артефакт вместо картинки в отдельном инструменте (Figma/Miro); AI-агент может **читать** и **генерировать** его тем же способом, что и C4-диаграмму, потому что это тот же текстовый формат.

### 5.2 Мост к BDD (блок 2) — «спека как исполняемый Gherkin»

Второй, более прямой аналог architecture-as-code для требований, который источники подтверждают отчётливее, чем Mermaid user journey, — это уже разобранный в блоке 2 **Gherkin как исполняемая спецификация**: как C4/Mermaid — «код», который **проверяется** drift-детектором (§2.4 главы), так Gherkin-сценарий — «код», который **проверяется** прогоном автотеста (§2 блок BDD выше). Разница только в том, что architecture-as-code про структуру системы, Gherkin — про поведение; оба — «спецификация как исполняемый артефакт», оба версионируются рядом с кодом, оба AI может и писать, и валидировать на расхождение с реальностью.

**Честная граница для §1/§2 главы:** user story mapping (более широкая, часто **ручная** и воркшопная практика — физические/цифровые стикеры по колонкам «пользовательская активность → задачи → релизы») в найденных источниках **не** описана как code-as-diagram/DSL-практика в том же смысле, что Mermaid или Gherkin — это отдельная, преимущественно **не-текстовая** техника фасилитации (часто в Miro/FigJam/физической стене), и выдавать её за тот же «код» подход было бы overclaim. Честно: если глава хочет упомянуть story mapping, стоит явно разграничить — «story mapping = воркшоп-техника (не код), Mermaid/Gherkin = requirements/behavior-as-code (тот же подход, что architecture-as-code, другой артефакт)».

**Confidence: HIGH** на определении и механике Mermaid User Journey (первичная документация); **HIGH** на выводе «нет отдельной новой категории — это тот же подход, другой артефакт» (прямой логический вывод, подтверждённый отсутствием контр-примеров в поиске); **MEDIUM** на разграничении story mapping (нет источника, специально проводящего эту границу в AI-контексте — логический вывод курса).

---

## 6. Документация — инструментарий глубже

*(Глава уже называет вендоров — Confluence AI, AWS Q `/doc`, JetBrains — без «как пользоваться», §6.2. Здесь конкретная механика каждого + код-ориентированная альтернатива через сам кодинг-агент.)*

### 6.1 Confluence AI (Atlassian Intelligence / Rovo) — конкретные фичи

Три конкретные, задокументированные способности (eesel.ai — независимый практический гид по Confluence AI, серия статей 2026, secondary, но детально описывает vendor-фичи с примерами использования):
- **Суммаризация** — «summarizing long pages or comment threads»: «When you're looking at a huge project doc or a long comment thread, the AI can whip up a quick summary so you can get the main points without reading every last word» — конкретно применимо к длинным тредам ревью/обсуждения решений.
- **Генерация и трансформация контента** — «drafting new content, brainstorming ideas, and rewriting text» — то есть черновик страницы из промпта или переформулировка существующего текста в другом тоне/формате.
- **Q&A-поиск по базе знаний** («Confluence AI knowledge base») — «Instead of just looking for keywords, you can ask questions in natural language right in the search bar. The AI will then piece together an answer from the content scattered across your Confluence pages» — то есть RAG-подобный поиск поверх корпоративной базы знаний, плюс «Q&A search for internal knowledge and definitions for company-specific jargon».

Все три фичи объединены под брендом **Atlassian Intelligence** (он же Rovo в некоторых материалах Atlassian) — это общий AI-слой над продуктами Atlassian, не Confluence-специфичный инструмент. `[VFY-day-of: Confluence AI / Rovo фичи и брендинг — быстро меняются]`.

**Confidence: MEDIUM** (детальный independent practitioner-гид, не первичная документация Atlassian напрямую в этом проходе, но описывает реально существующие vendor-фичи, не выдуманные).

### 6.2 AWS Q Developer `/doc` — конкретная механика

Это **зрелая, задокументированная первичным источником** фича (AWS официальный анонс декабрь 2024, обновления блога апрель 2025 — то есть не свежая экспериментальная функция, а устоявшаяся часть продукта к 2026 году). Точная механика (docs.aws.amazon.com/amazonq, primary):
- Команда `/doc` в чате Amazon Q Developer (VS Code / IntelliJ IDEA) запускает **агента**, который «analyzes your codebase and generate comprehensive documentation» — то есть источник для генерации именно **код**, а не отдельный промпт-пересказ.
- Уважает `.gitignore` — «excludes files you don't want to be included in documentation review» (та же логика, что и остальные code-aware инструменты — не документирует то, что разработчик явно исключил из репозитория).
- Может **создавать диаграммы инфраструктуры**, если проект содержит infrastructure-as-code файлы (AWS CDK, CloudFormation, Terraform) — то есть напрямую связано с §2.4 главы (architecture-as-code): агент читает уже существующий код-как-инфраструктуру и **выводит из него** диаграмму, а не выдумывает архитектуру по описанию.
- Может **ревьюить новый код и предлагать обновления документации** после изменений — то есть замкнутый цикл: код меняется → `/doc` предлагает диф в документации, снижая риск устаревания (прямая связь с провалом §1.5 главы «спека устарела и молча разошлась с кодом» — только применительно к README/docs, а не к спеке требований).
- Генерирует README-файлы проекта напрямую.
- **Итеративное улучшение через feedback loop** — «you can gradually build comprehensive documentation through multiple iterations», то есть не одноразовая генерация, а процесс с возможностью правки и повторного запуска.

**Инженерный вывод для §6.2 главы:** `/doc` — конкретный пример того, что глава уже формулирует абстрактно («документация — привнесённая сложность, AI силён именно здесь», §6.2): вход — реальный код, выход — пересказ **того, что уже есть**, без необходимости придумывать намерение (в отличие от требований, §1 главы). Это структурно объясняет, почему документация — «светлый пятачок»: задача `/doc` — не решить, что строить, а описать то, что уже построено.

**Confidence: HIGH** (первичная документация AWS, фича стабильна с конца 2024, не молодая экспериментальная функция).

### 6.3 Код-ориентированная альтернатива — генерация README/онбординга самим кодинг-агентом (мост к §3.3b Skills)

Помимо вендорских продуктов (Confluence AI, AWS Q), релевантная **для этого курса** альтернатива — использовать сам кодинг-агент (Claude Code), которым уже пользуется студент, для той же задачи, без отдельного вендорского SaaS. Конкретный паттерн из community (не встроенная официальная функция «из коробки», а **устанавливаемый skill** — прямой мост к §3.3b главы): «Claude Code has skills that automatically generate professional, comprehensive README.md files by analyzing your project structure, dependencies, and code patterns» — конкретные примеры: **Code Documentation Skill** («empowers Claude to generate and maintain high-quality software documentation following industry best practices, providing structured patterns for... README files, Architecture Decision Records (ADRs), and clear inline comments» — заметьте: тот же skill покрывает и README, и ADR, то есть напрямую пересекается с §2.2 главы про ADR), **README Generator** и **Create README** skills в разных community-маркетплейсах (GLINCKER/claude-code-marketplace, s2005/claude-code-skill-template, awesomeskill.ai).

**Честная оговорка (важно не преувеличить).** Это **community-паттерн**, не единый официальный skill из `anthropics/skills` (официальный репозиторий Anthropic содержит собственный набор skills, но конкретно «readme-generator» в нём в этом проходе не подтверждён как включённый по умолчанию — не выдумываем). Механика скилла при этом ровно та же, что уже разобрана в §3.3b главы (Skills — расширяемая on-demand компетенция): онбординг-документация — это ровно пример «процедуры, которая нужна редко, но подробна, когда нужна» — прямая цитата из §3.3b главы про то, когда заводить skill вместо строчки в CLAUDE.md.

**Мост к §3.3b главы (прямая рекомендация для книги):** «онбординг для нового разработчика/агента» — хороший **кандидат в skill** именно потому, что удовлетворяет обеим эвристикам заведения skill из документации Anthropic, уже процитированным в `coding-agent-mechanics.md`: (1) «You keep pasting the same instructions into chat» — онбординг объясняют новому человеку/агенту многократно одинаково; (2) «You want progressive disclosure» — справочный материал (архитектура, соглашения, история решений) большой и нужен не каждый ход, только при онбординге. Это НЕ отдельная новая идея — это применение уже введённого в главе критерия к конкретному кейсу документации.

**Confidence: MEDIUM** на существовании и механике community-skills для README-генерации (несколько независимых источников подтверждают паттерн, но это не первичная документация Anthropic конкретно про readme-skill); **HIGH** на самой логике «онбординг = хороший кандидат в skill» (прямое применение уже HIGH-confidence критерия из §3.3b главы/`coding-agent-mechanics.md` §1.1).

---

## Источники (полный список, доступ 2026-09-20, если не указано иное)

**Git worktree:**
1. https://code.claude.com/docs/en/worktrees — официальная документация Claude Code, механика `--worktree`, `EnterWorktree`, `isolation: worktree`, enforcement-проверки (primary, HIGH)
2. `/home/harness/harness-projects/256/.worktrees/folder-288/lesson4-de299d-0fac50ac/CLAUDE.md` (раздел «Multi-Lecture Parallel Production (ENFORCED)») — собственный протокол курса, реальный инцидент Лекции 2 (~2 часа branch contention), self-referential (primary internal, HIGH)
3. https://www.augmentcode.com/guides/git-worktrees-parallel-ai-agent-execution — механика shared object store + isolation (secondary, MEDIUM)
4. https://www.mindstudio.ai/blog/git-worktrees-parallel-ai-coding-agents — workflow-паттерн (secondary, MEDIUM)
5. https://blog.vibecoder.me/multi-claude-parallel-agents-anthropic-workflow — цитата Бориса Черни (вторичная, не первоисточник X.com) (secondary, MEDIUM/LOW)
6. https://www.aakashx.com/blog/parallel-claude-code-agents/ — практический workflow, git diff review перед merge (secondary, MEDIUM)

**BDD + AI:**
7. https://cucumber.io/docs/bdd/ — каноническое определение BDD, три практики (Discovery/Formulation/Automation) (primary, HIGH)
8. https://automationpanda.com/2026/04/27/bdd-gherkin-guidelines-for-ai-coding-and-testing/ — Andy Knight, AI-генерация Gherkin, проблемы качества, gherkin-guidelines.md паттерн (primary practitioner, MEDIUM)
9. https://github.com/AutomationPanda/gherkin-guidelines-for-ai — сам файл-гайдлайн (primary repo, MEDIUM)
10. https://www.303software.com/insights/behavior-driven-development-cucumber-testing-2025-reality — честная реальность adoption: 27%/68% OSS-проектов, разрыв tool-vs-methodology (secondary analysis, MEDIUM)
11. https://qaskills.sh/blog/comparing-popular-bdd-frameworks-2026-complete-guide — обзор фреймворков 2026 (secondary, MEDIUM/LOW)
12. https://gherkinizer.com/ — AI Gherkin-генератор на Gemini (vendor, LOW-MEDIUM)

**Trunk-based + AI:**
13. https://journal.daniellopes.dev/p/trunk-based-development-vs-feature-branches-ai — «half the agent's assumptions are wrong by the time you merge», семантические vs текстовые конфликты (secondary practitioner, MEDIUM)
14. https://www.flagsmith.com/blog/trunk-based-development — feature flags механика (vendor, MEDIUM)
15. https://www.harness.io/harness-devops-academy/trunk-based-development — DORA-связка (vendor, MEDIUM)

**Тестовый инструментарий:**
16. https://blog.postman.com/new-capabilities-march-2026/ — AI-native платформа Postman март 2026 (primary vendor, MEDIUM)
17. https://blog.postman.com/testing-apis-with-postman-agent-mode-a-practical-guide/ — Agent Mode механика (primary vendor, MEDIUM)
18. https://devops.com/postman-adds-ai-agent-to-automate-api-development-and-governance/ — AI Engineer июнь 2026 (secondary, MEDIUM)
19. https://java.testcontainers.org/ — Testcontainers официальная страница (primary vendor, HIGH на факте механики)
20. https://devblogs.microsoft.com/ise/testing-with-testcontainers/ — Testcontainers + AI skill паттерн (Microsoft ISE blog, secondary/primary-adjacent, MEDIUM)
21. https://qaskills.sh/blog/testcontainers-integration-testing-guide — «default approach to integration testing... 2026» (secondary, MEDIUM/LOW)
22. https://saucelabs.com/resources/blog/comparing-the-20-best-visual-testing-tools-of-2026 — обзор visual regression 2026, два лагеря (AI-diffing cloud vs snapshot-библиотеки) (secondary aggregator, MEDIUM)
23. https://percy.io/blog/visual-regression-testing-tools — Chromatic/Percy/Applitools сравнение, Percy Visual Review Agent claim (vendor + secondary, MEDIUM)

**Визуализация требований:**
24. https://mermaid.js.org/syntax/userJourney.html — User Journey Diagram синтаксис (primary vendor docs, HIGH)
25. https://docs.mermaidchart.com/mermaid-oss/syntax/userJourney.html — то же, MermaidChart (primary vendor docs, HIGH)

**Документация:**
26. https://www.eesel.ai/blog/confluence-ai — Confluence AI фичи: суммаризация, генерация, Q&A (independent practitioner guide, MEDIUM)
27. https://www.eesel.ai/blog/atlassian-intelligence-confluence-ai-features — детализация Atlassian Intelligence (secondary, MEDIUM)
28. https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/doc-generation.html — AWS Q `/doc` официальная документация (primary vendor, HIGH)
29. https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-q-developer-generate-documentation-source-code/ — анонс фичи, декабрь 2024 (primary vendor, HIGH)
30. https://aws.amazon.com/blogs/devops/simplifying-code-documentation-with-amazon-q-developer/ — детали работы `/doc`, feedback loop (primary vendor blog, HIGH)
31. https://github.com/GLINCKER/claude-code-marketplace/blob/main/skills/documentation/readme-generator/SKILL.md — community README-generator skill, пример структуры (primary repo, но community не official Anthropic, MEDIUM)
32. https://github.com/anthropics/skills/blob/main/README.md — официальный репозиторий skills от Anthropic, для сверки, что входит «из коробки» (primary, HIGH)

**Ссылочно, уже покрыто в sibling-файлах, не переисследовано здесь:**
- `notes/research/lecture-4/coding-agent-mechanics.md` §1 (Skills), §3 (git-конвенции), §2 (MCP)
- `notes/research/lecture-4/progression-and-configs.md` §3 (существующая строка Trunk-based, Pair/ensemble)

---

## Honesty flags / gaps (declared)

1. **Git worktree — рекомендованное число параллельных сессий (3-5 vs 4-8)** (§1.4) — расходится между двумя вторичными источниками, ни один не первоисточник Anthropic с конкретной цифрой; официальная документация (`code.claude.com/docs/en/worktrees`) конкретного числа не называет. Не выдаём ни одну цифру как «рекомендацию Anthropic» без оговорки.
2. **Цитата Бориса Черни (§1.4)** — известна только через вторичные пересказы (blog.vibecoder.me и др.), сам оригинальный пост в X не зафетчен и не верифицирован напрямую в этом проходе. Помечено как вторичная цитата.
3. **BDD vs TDD популярность именно в AI-агентном контексте (§2.4)** — прямого источника, сравнивающего это специально «в эпоху агентов», не найдено. Вывод «BDD менее мейнстримный» подтверждён общей (не AI-специфичной) статистикой adoption (27%/68% по OSS) и логически перенесён; честно помечено как экстраполяция, не прямое измерение.
4. **Story mapping как отдельная техника (§5.2)** — источники не описывают её как code-as-DSL практику в одном ряду с Mermaid/Gherkin; граница «воркшоп-техника vs requirements-as-code» — вывод курса, не прямая цитата, разделяющая их именно так.
5. **Percy «3x review-time reduction, ~40% fewer false positives»** (§4.3) — self-reported vendor-число (percy.io), не независимо верифицировано в этом проходе. Аналогичная оговорка нужна, что глава уже применяет к SWE-bench-цифрам вендоров (§3 главы, «пять вопросов к вендорскому числу»).
6. **Community README-generator skills для Claude Code (§6.3)** — подтверждены несколькими независимыми community-маркетплейсами (не выдумано), но НЕ подтверждены как официальный, встроенный по умолчанию skill Anthropic (`anthropics/skills` репозиторий не содержит подтверждённо именно «readme-generator» в этом проходе). Формулировка в тексте явно разделяет «паттерн существует и работает» от «это официальная фича из коробки».
7. **Testcontainers AI-«интеллект» (§4.2)** — честно ограничен уровнем «skill даёт агенту процедурное знание конфигурации», а не «AI анализирует БД умнее человека»; не преувеличиваем зрелость AI-функции здесь, в отличие от более зрелого AI-diffing в visual regression (§4.3).
8. **Postman AI Engineer / AI Protocol (§4.1)** — очень свежие анонсы (март/июнь 2026), эффективность не независимо измерена; `[VFY-day-of]` явно поставлен, чтобы orchestrator/fact-checker перепроверили актуальность к дню лекции.
9. **`[VFY-day-of]` volatile items, сводно:** Claude Code `--worktree` версия (v2.1.49) и точные enforcement-детали (могут измениться к дню лекции, документация сама фиксирует несколько версионных порогов вплоть до v2.1.274); Confluence AI / Rovo брендинг и набор фич; Postman AI Engineer/Agent Mode конкретные возможности (продукт в активной разработке весь 2026 год); BDD framework adoption % (единичный анализ, не регулярно обновляемый бенчмарк); Percy/Chromatic конкретные вендорские цифры эффективности.

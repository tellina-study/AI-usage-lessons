# Lecture 4 — Coding-agent mechanics: Skills, MCP-for-coding, Git-as-contract, Task-logging patterns

**Date:** 2026-09-19 · **Researcher:** fact-checker research subagent · **Issue:** #162 (расширение §3 «Реализация» главы Лекции 4)
**Purpose:** углубить `library/lectures/lec-04/chapter-part3.md` §3 конкретной механикой кодинг-агента — Skills, MCP-для-кодинга, git-конвенции как контракт, паттерны логирования задач.
**Sibling files (read first, NOT duplicated here):** `anthropic-sdlc-kit.md` (Skills row в summary table + сайд-бар про CLAUDE.md vs AGENTS.md), `harness-and-architecture-practices.md` (AGENTS.md/Cursor rules/harness engineering, AREA 1-2), `sources.md`, `methodics-as-practice.md` + `methodologists-and-failures.md` (Lethal Trifecta уже разобран целиком).
**Access date for all URLs:** **2026-09-19**. `[VFY-day-of]` = волатильный факт (версия продукта/фича/цифра), перепроверить в день лекции.
Confidence: **HIGH** = primary source (vendor docs, canonical spec) · **MEDIUM** = practitioner consensus / vendor blog / secondary · **LOW** = single blog / emerging / anecdotal.

---

## 1. Skills — расширяемая on-demand компетенция агента

### 1.1 Что это и чем отличается от CLAUDE.md/AGENTS.md

Skill — папка с файлом `SKILL.md` (YAML-frontmatter + markdown-инструкции), которую агент подгружает **только когда она релевантна задаче** — в противоположность CLAUDE.md/AGENTS.md, которые сидят в контексте **всегда**, каждый ход. Формулировка из официальной документации: «Unlike CLAUDE.md content, a skill's body loads only when it's used, so long reference material costs almost nothing until you need it» (code.claude.com/docs/en/skills). Это тот же принцип, что JIT-retrieval из context-engineering (см. `harness-and-architecture-practices.md` A1) — но применённый не к произвольным файлам кода, а к самим инструкциям агента.

**Когда заводить skill вместо строчки в CLAUDE.md/AGENTS.md** (эвристики из документации, дословно):
- «You keep pasting the same instructions into chat» — повторяющаяся ручная инструкция → кандидат в skill.
- «A section of CLAUDE.md has grown into a procedure» — секция CLAUDE.md разрослась в многошаговую процедуру → выносить, иначе она грузится в каждый ход зря.
- «You want progressive disclosure» — справочный материал нужен редко и он большой → skill, а не всегда-on файл.

Таблица сравнения (verbatim, code.claude.com/docs/en/skills):

| Aspect | CLAUDE.md | SKILL.md | AGENTS.md |
|---|---|---|---|
| Loading | Always in context | Loads only when invoked | Defines subagent behavior |
| When to use | Facts, conventions, setup | Multi-step procedures, reference material | Subagent personalities/tools |
| Cost | Ongoing token drain | Zero cost until invoked | N/A |

**Confidence: HIGH** (первичный источник, дата фетча 2026-09-19).

### 1.2 Формат SKILL.md — конкретика

Минимальный skill — два элемента: YAML-frontmatter (опционален, но рекомендован) между `---` и markdown-тело с инструкциями. Ключевые frontmatter-поля (таблица, code.claude.com/docs/en/skills, verbatim перевод сути):

| Поле | Обязательное | Назначение |
|---|---|---|
| `name` | нет | Отображаемое имя (default = имя директории) |
| `description` | рекомендовано | По этому полю агент решает, когда авто-подгрузить skill |
| `disable-model-invocation` | нет | `true` = только пользователь может вызвать (`/skill-name`), модель — нет |
| `user-invocable` | нет | `false` = только модель может вызвать, пользователь — нет |
| `allowed-tools` | нет | Предодобрить инструменты для этого хода без permission-промпта |
| `paths` | нет | Glob-паттерны, ограничивающие авто-загрузку конкретными путями (полезно в монорепо) |

Три способа вызова: (1) прямой — `/skill-name` от пользователя; (2) авто — модель сама решает по совпадению с `description`; (3) stacked — `/skill1 /skill2 argument` грузит оба сразу с общим аргументом. Skills лежат по путям с приоритетом (enterprise > personal > project), плюс nested-паттерн для монорепо (`apps/web/.claude/skills/` → `/apps/web:deploy`).

**Практический лимит:** документация рекомендует держать сам `SKILL.md` <500 строк, вынося детали в companion-файлы (`reference.md`, `scripts/`), которые грузятся по ссылке только при реальной необходимости — тот же progressive-disclosure принцип на уровень глубже.

**Confidence: HIGH.**

### 1.3 Vendor-neutral рамка — Agent Skills open standard

Claude Code — не единственный, кто читает `SKILL.md`: формат officially adopts **Agent Skills open standard** (agentskills.io) — «works across multiple AI tools». Vendor-neutral подмножество frontmatter-полей: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools` — именно они допускаются, когда skill пакуется для распространения через claude.ai Skills API (`package_skill.py` явно отклоняет non-spec поля, например `argument-hint`, с ошибкой «Unexpected key(s) in SKILL.md frontmatter»). Всё остальное (`disable-model-invocation`, `context: fork`, `paths`, `arguments` и др.) — Claude Code-специфичные расширения поверх стандарта.

Похожие концепты у других инструментов (аккуратно, без выдумывания эквивалентности): OpenAI Codex CLI имеет собственный механизм **skills** (developers.openai.com/codex/skills) поверх того же open standard, плюс отдельно — **custom instructions** через AGENTS.md (developers.openai.com/codex/concepts/customization); GitHub Copilot называет свой смежный механизм «agent skills system»; Cursor и другие инструменты читают AGENTS.md как always-on слой (тот же уровень, что CLAUDE.md), но нативного on-demand skill-механизма, тождественного Claude Skills, в источниках не подтверждён для Cursor — там основной инструмент того же назначения — **Cursor rules** (`.cursor/rules/*.mdc`, 4 типа применения: Always Apply / Apply Intelligently / Apply to Specific Files / Apply Manually), уже разобранные в `harness-and-architecture-practices.md` A1. **Честно:** «skills» как отдельный on-demand-vs-always-on концепт — общая тенденция экосистемы 2026 года (built поверх agentskills.io standard), но конкретная реализация (progressive disclosure, автозагрузка по description) в источниках подтверждена именно для Claude Code + OpenAI Codex; для остальных инструментов не выдумываем детали без прямой цитаты.

**Confidence: MEDIUM** (кросс-вендорная adoption — подтверждена частично, но темпы/полнота adoption волатильны). `[VFY-day-of]`.

---

## 2. MCP — специфично для кодинг-агента

*(Общее определение протокола MCP — уже в Лекции 3, здесь НЕ повторяется. Фокус — зачем это конкретно кодинг-агенту.)*

### 2.1 Что MCP даёт кодинг-агенту практически

Кодинг-агент по умолчанию видит только то, что ему открывают явные инструменты (файловая система рабочей копии, shell). MCP расширяет это на **внешние системы**, которые не являются файлами в репозитории: issue-трекер, живой браузер для e2e-проверки, деплой-таргет, CI/CD API. Без MCP агент либо не может выполнить действие вообще, либо инженер вручную копирует контекст туда-обратно между агентом и внешней системой — MCP убирает этот ручной мост.

**Конкретные примеры, релевантные разработке:**

- **GitHub MCP server** (`github/github-mcp-server`, официальный от GitHub) — даёт агенту инструменты по toolset'ам: `issues`, `pull_requests`, `repos`, `actions`, `code_security`, `dependabot`, `discussions`, `git` (low-level) и др. Явный **read-only режим**: «write tools are skipped if `--read-only` is set, even if explicitly requested via `--tools`» — это конкретный, включаемый администратором технический переключатель read-only vs write-capable сервера, а не просто рекомендация. Документация отдельно советует по токенам: «Only grant necessary permissions», «Minimum scopes» (`repo`, `read:packages`, `read:org`), «Separate tokens» на проект, регулярная ротация, никогда не коммитить креды. (github.com/github/github-mcp-server, [VFY-day-of] — набор toolset'ов и версии меняются часто).
- **Playwright MCP server** (`microsoft/playwright-mcp`, официальный от Microsoft) — даёт агенту браузер для e2e: агент открывает страницу, читает **структурное accessibility-дерево** (а не скриншот — «Instead of asking a vision model to guess where a button is in a JPEG, the agent receives a structured, text description of every interactive element»), кликает, заполняет формы, генерирует Playwright-тест, воспроизводящий сделанное. Практический нюанс для выбора инструмента: у высокопроизводительных кодинг-агентов растёт предпочтение CLI+Skills над MCP там, где нужна экономия токенов (MCP-схемы инструментов и accessibility-деревья тяжелее, чем узкая CLI-команда) — «Use CLI when your agent has filesystem access… and MCP when it doesn't» (источник — практический блог, не vendor-канон). **Confidence: MEDIUM** на этом конкретном компромиссе (нет первичного источника от Anthropic/Microsoft с таким явным правилом).
- **Filesystem MCP** — паттерн, а не единственный сервер: даёт read/write доступ к файлам вне текущей рабочей директории агента (например, другой репозиторий, shared-диск), когда сам агент («Claude Code» и аналоги) уже имеет встроенный native filesystem-доступ к своей рабочей копии — то есть filesystem MCP актуален в первую очередь для агентов/раннеров, у которых встроенного файлового доступа нет.

**Tool discovery:** MCP-сервер публикует список своих tools (имя + JSON-schema аргументов + описание) при подключении; агент видит их как обычные функции-инструменты и решает, когда вызывать, по тому же механизму, что и встроенные tools — то есть это тот же tool-use loop, просто с расширяемым источником инструментов, а не фиксированным набором.

**Confidence: HIGH** для GitHub MCP toolsets и read-only флага (первичная документация); **MEDIUM** для Playwright MCP механики (vendor + practitioner blend); **MEDIUM** для «filesystem MCP» как обобщённого паттерна (нет единого канонического сервера-эталона — это класс, а не продукт).

### 2.2 Мост к безопасности — MCP как вектор Lethal Trifecta

Полный разбор Lethal Trifecta (untrusted content + доступ к чувствительным данным + канал эксфильтрации) уже есть в `methodics-as-practice.md` (строка про Security) и `methodologists-and-failures.md` (CamoLeak CVE-2025-59145 кейс) — **не дублируется здесь**. Что нужно добавить именно в MCP-контексте: MCP-сервер сам по себе часто закрывает сразу два угла трифекты одним подключением — он даёт **доступ к данным** (issues, приватные репо, файлы) и одновременно может быть **каналом действия наружу** (создать PR/comment, вызвать API), а третий угол (untrusted content) прилетает через сам обрабатываемый контент — например, текст чужого issue или PR-комментария, который агент читает через тот же MCP-инструмент. GitHub MCP server — предметный пример из источников: «GitHub's MCP server enabled attackers to access private repositories by submitting nefarious issues to public repositories. These issues included prompt injection instructions that could exfiltrate data via pull requests» (arcjet.com/learn/lethal-trifecta, вторично цитирует Willison). Отсюда прямое инженерное следствие для конфигурации: read-only MCP по умолчанию (см. §2.1 read-only флаг) там, где агенту не нужна запись, и осознанное решение о write-scope как security-decision, а не default.

**Confidence: HIGH** на механизме (подтверждено в нескольких независимых источниках, включая существующий research лекции), **MEDIUM** на конкретно GitHub MCP как иллюстрации (secondary source, не официальный GitHub security-advisory).

---

## 3. Git-конвенции как часть контракта с агентом

*(Тема отсутствует в existing research — новый блок.)*

### 3.1 Commit-message конвенции: Conventional Commits

**Формат** (conventionalcommits.org v1.0.0, canonical spec): `<type>[optional scope]: <description>` + опциональные body/footer. Два **обязательных** типа по спецификации: `feat` (новая функциональность) и `fix` (исправление бага); остальные типы (`build`, `chore`, `ci`, `docs`, `style`, `refactor`, `perf`, `test`) — распространённое расширение (`@commitlint/config-conventional`), не часть ядра спеки.

**Связь с semver** — прямая и машинно-читаемая: `fix` → PATCH, `feat` → MINOR, `BREAKING CHANGE` (в footer или через `!` перед двоеточием, напр. `feat!:`) → MAJOR.

**Зачем это релевантно именно для агента** (не для человека) — пять заявленных в спецификации выгод, из которых для агента особенно значимы первые две: (1) автоматическая генерация CHANGELOG, (2) автоматическое определение semver-бампа по типам закоммиченных изменений, (3) коммуникация характера изменений команде, (4) триггер build/publish процессов, (5) более структурированная история для контрибьюторов. Ключевой инженерный смысл для агента: агент, в отличие от человека, **пишет коммиты систематически и в большом объёме** («vibe coders generate 5-10x more commits than traditional developers», practitioner-источник 2026) — при таком объёме именно машинная разбираемость (не читаемость для человека вручную) определяет, можно ли автоматизировать changelog/semver вокруг агентной работы или нет. Conventional Commits — конкретный, проверяемый пример того, как **структурированный** машиночитаемый формат превращает объём коммитов из проблемы (много шума) в актив (автоматизируемый сигнал).

Практикуемое дополнение для агентных коммитов (не входит в спецификацию Conventional Commits, отдельная практика): «keep the commit subject human-readable… then add a Co-Authored-By trailer naming the model» — то есть сама структура типа/scope остаётся человекочитаемой, а атрибуция агента идёт отдельным footer-трейлером, не в теле сообщения.

**Confidence: HIGH** на самой спецификации (canonical source), **MEDIUM** на «зачем агенту» синтезе (практикующие блоги 2026, не первоисточник Anthropic/GitHub).

### 3.2 Branch-naming конвенции как часть steering-файла

**Conventional Branch v1.1.0** (conventionalbranch.org) — открытая спецификация `<type>/<description>`, lowercase + цифры + дефисы, без последовательных дефисов/точек и без них в начале/конце описания. Purpose-типы: `feature`/`feat`, `bugfix`/`fix`, `hotfix`, `release`, `chore`. **Релевантная для агентов часть — v1.1.0 добавила «AI Agent Source Prefixes»**: `ai/` (родовой), `claude/`, `codex/`, `copilot/`, `cursor/` — явный сигнал ревьюеру «эта ветка сгенерирована агентом X» ещё до открытия диффа, и точка, на которую можно повесить отдельные branch-protection правила именно для агентной работы. Пример из источника: `claude/security-patch` (родовой вариант без указания вендора — `ai/refactor-auth-flow`; live-проверка conventionalbranch.org — тикет-стиля `AUTH-42` на сайте нет, это была фабрикация).

Практическое правило, независимо подтверждённое несколькими источниками: **агент никогда не коммитит напрямую в общую ветку** — каждая агентная задача получает свою feature-ветку (то же требование, что и Mandatory Git Rules этого курса — совпадение независимое, не заимствование).

Branch-naming и commit-конвенции обычно **прописываются как часть steering-файла** (CLAUDE.md/AGENTS.md — см. §1.1 и `harness-and-architecture-practices.md` A1 про AGENTS.md `## PR instructions` секцию): «Codifying git commit message formats and branch naming conventions ensures the AI doesn't have to guess. When a developer asks an AI to add a feature, the AI can see from documentation that feature branches are named feat/…». Это прямая иллюстрация «git-конвенции как часть контракта» — конвенция сама по себе не работает, пока она не записана туда, откуда агент её читает каждый раз.

**Confidence: HIGH** на Conventional Branch спецификации (первичный источник фетчен напрямую); **MEDIUM** на «no direct commit to shared branch» как universal best practice (несколько независимых practitioner-источников, не единый канон); `[VFY-day-of]` на adoption-темп AI Agent Source Prefixes (фича 2026 года, молодая).

### 3.3 PR-описания и шаблоны как agent-producible артефакт

PR-описание, сгенерированное агентом — не просто текст, а **agent-producible reviewable артефакт**, если следует фиксированной структуре. Из практических источников 2026 года выделяется устойчивый шаблон полей: **Intent** (одно-два предложения простым языком, зачем изменение) → **Changed** (какие файлы/поведение изменились) → **Not changed** (важные исключения — что намеренно не тронуто) → **Validation** (какие команды прогнаны и с каким результатом) → **Risks** (допущения, непроверенные ветки, риски раскатки) → **Follow-ups** (что осознанно оставлено за скобками). Смысл фиксированной структуры именно для агентных PR: «every agent-written PR should carry the same shape of proof so reviewers know where to look» — ревьюер тратит время не на угадывание, что проверять, а на саму проверку.

Механика: PR-шаблон (`.github/pull_request_template.md`) передаётся агенту тем же способом, что и остальной steering-контекст (CLAUDE.md/AGENTS.md/skill) — «Give the PR template to the AI and tell it to use the whole session for the original request, decisions, tradeoffs, and tests». Это делает PR-шаблон таким же элементом «контракта с агентом», как commit/branch-конвенции из §3.1-3.2 — разница в том, что PR-шаблон верифицируется человеком-ревьюером напрямую в моменте, а commit/branch-конвенции — постфактум и часто автоматизированно (CI-линтер формата коммита).

**Confidence: MEDIUM** (устойчивый практический консенсус 2026 года из нескольких независимых источников, но нет единого canonical-стандарта уровня Conventional Commits — сами источники это не оформляют в спецификацию, а в набор практик).

### 3.4 Честно: когда git не подходит контексту

Здесь у нас **мало устоявшейся практики** — говорим прямо, не выдумываем эквивалент.

- **Notebook-driven / Jupyter-окружения.** Классический `.ipynb` плохо дружит с git (JSON-diff нечитаем, output-ячейки шумят в диффах). Подтверждённая альтернатива — **marimo**: notebooks «are reproducible, execute reactively… stored as pure Python, and versionable with Git» — то есть решение здесь не «отказ от git», а смена формата хранения (Python-файл вместо JSON) так, чтобы git снова стал применим. Прямого решения «как агенту коммитить именно `.ipynb`» в источниках не найдено.
- **Монорепо с нестандартным workflow.** Здесь источники, наоборот, говорят о **схождении**, а не расхождении: «AI coding agents optimize for full-codebase context, atomic changes, and connected dependency graphs — properties that monorepo provides by default… monorepos provide unified context for powerful agentic workflows, while AI helps navigate and automate monorepo complexity» (monorepo.tools/ai). То есть монорепо с точки зрения источников — не проблемный случай для git-конвенций агента, а благоприятный; проблема нестандартного workflow (напр. Perforce/large-binary-monorepo без git вовсе) в найденных источниках не покрыта — честно помечаем как **UNVERIFIABLE** для этого курса без дополнительного узкого поиска.
- **Git commits как замена task-log** (контрпример из §4): один из найденных практиков прямо выбирает НЕ заводить отдельный task-tracking файл, а полагаться на частые атомарные git-коммиты как единственный лог: «I commit early and often… After each small task or each successful automated edit, I'll make a git commit with a clear message» — «No explicit criteria comparing folder-per-task versus single-log approaches are provided» у этого источника. Это валидный, но нигде не формализованный четвёртый паттерн («git history как единственный лог») — упоминаем в §4 как контраст к трём основным.

**Confidence: LOW-MEDIUM** на этом подразделе целиком — тема сама по себе honestly emerging, не canonical.

---

## 4. Слой логирования / трекинга задач — 3 паттерна, критерии выбора

*(Growth-ladder-style: без единственно правильного ответа — цель для §3 главы дать инженеру критерии, не рецепт.)*

### 4.1 Три паттерна — определения

- **(а) Отдельная папка с набором файлов на задачу** — каждая задача получает свою директорию (`tasks/TASK-42/` или аналог), внутри — несколько файлов: план, заметки, промежуточные артефакты, итоговый отчёт. Соответствует стилю multi-file per-task research/production структур (сам этот research-файл + sibling-файлы в `notes/research/lecture-4/` — конкретный пример этого паттерна в собственном репозитории курса).
- **(б) Единый общий лог** — один файл (`CHANGELOG.md`, `.changelog/CHANGELOG.md`, `decisions.md`-стиль) на весь проект/агента, куда каждая задача **дописывается** append-only. Практический пример из источников: «Append to `{repo}/.changelog/CHANGELOG.md`. Create the `.changelog/` directory and file if they don't exist» — простейшая, наиболее часто встречающаяся реализация. Курс сам использует этот паттерн для `notes/decisions.md` и `notes/mcp-limitations.md` (ENFORCED update rule в CLAUDE.md).
- **(в) Общая папка с одним файлом на задачу** — промежуточный паттерн: одна плоская директория (`tasks/` или `backlog/`), внутри — **по одному** markdown-файлу на задачу (не поддиректория с несколькими файлами, как в (а)). Конкретный, задокументированный пример — **Backlog.md** (`MrLesk/Backlog.md`, MIT, активный OSS-проект 2026): «Everything is stored as human-readable Markdown in a project-local backlog folder… Each task file follows a structured format with metadata fields». Явно сформулированный принцип выбора именно этой гранулярности: «each task = one context window = one PR. Diffs stay a size a human can actually read» — то есть размер файла-на-задачу здесь **намеренно** привязан к размеру одного PR/одного контекстного окна агента, а не к произвольному удобству. Агенты подключаются двумя способами — CLI (`backlog task create/edit/list`) и MCP (`backlog://workflow/overview` в Claude Code, Codex, Gemini CLI, Kiro).

### 4.2 Как это делает сам Claude Code — валидный пример паттерна (б)/сессионный

Встроенный механизм Claude Code — **TodoWrite** (легаси) и его преемник — четыре инструмента **TaskCreate / TaskUpdate / TaskGet / TaskList** (актуально с Claude Code v2.1.268+). Принципиальное отличие от всех трёх паттернов §4.1: это **не файл на диске вообще** — состояние живёт только в контекстном окне текущей сессии. Прямая цитата из официальной документации: «TodoWrite is session-scoped and lives in the context window—close the terminal, restart, compact the context, and it's gone with nothing touching disk» (вторичный практический источник, сверено по смыслу с первичной документацией code.claude.com/docs/en/agent-sdk/todo-tracking). Жизненный цикл задачи: `pending` → `in_progress` → `completed` → (опционально) `status: "deleted"`. Критерий заведения тудушки, по документации: «Complex multi-step tasks requiring three or more distinct actions», списки задач от пользователя, длинные операции, явный запрос.

**Инженерный вывод для §3 главы:** встроенный task-tracking агента (TodoWrite/Task*) — это **не** замена ни одному из трёх файловых паттернов §4.1: он решает другую задачу (live-прогресс внутри одной сессии для UI/наблюдателя), не даёт **межсессионной персистентности** и не годится как **аудит-след** (ничего не пишется на диск). Если нужна персистентность за пределами одной сессии — необходим один из паттернов (а)/(б)/(в) поверх или вместо встроенного механизма; они не взаимоисключающи (Claude Code может параллельно вести TodoWrite для live-прогресса текущей сессии И писать в файловый task-log для истории).

**Confidence: HIGH** на самом механизме и жизненном цикле (первичная документация); **MEDIUM** на точной формулировке «session-scoped… nothing touching disk» (перефразировано из вторичного источника, но не противоречит первичному).

### 4.3 agent-harness-registry (workain) — что реально подтверждено про task-log

Курс уже использует `github.com/workain/agent-harness-registry` как источник для Лекции 3 (§4.4-4.9 главы Л3: «presence paradox», «Honest Lying», таксономия памяти/skills/subagents/engines — см. `library/lectures/lec-03/chapter-part4.md`, `chapter-part5.md`). **Точечная, а не структурная цитата** (per lecence-условие задачи): в текущем research-проходе прямой раздел про «per-task file vs shared log vs per-task-folder» паттерны **в README/документации реестра не обнаружен** — раздел про «memory» как категорию harness-оснастки присутствует (это и есть источник для §4.5 главы Л3 «плоская память»), но конкретно task-logging taxonomy как отдельная ось сравнения там не описана. **Честно:** не выдумываем цитату оттуда для этого конкретного раздела — используем реестр только для того, что он реально покрывает (память как категория экипировки, уже процитировано в Л3), а таксономию task-log-паттернов (§4.1 выше) строим из независимых источников (Backlog.md, changelog-практики, Claude Code TodoWrite).

Связь с существующими находками курса из Л3 (не повторяем детали, только мост): «Honest Lying» (Dixit, Kamal, Oates, arXiv:2605.29463) показал, что self-authored память/журнал может **закреплять** неверное убеждение агента вместо его исправления. Это прямо релевантно выбору между паттернами §4.1 — любой из трёх файловых паттернов, если агент **сам** пишет и **сам же** читает свои прошлые записи без верификации человеком, потенциально наследует тот же риск entrenchment, что описан в «Honest Lying» — независимо от того, это один общий лог (б) или файл на задачу (в). Инженерный вывод для §3: аудит-след полезен человеку-ревьюеру именно потому, что **читает его не только сам агент** — если лог используется исключительно как self-context агента без внешней верификации, риск закрепления ошибки не снимается фактом наличия лога.

**Confidence: MEDIUM** на связи с «Honest Lying» (логическая экстраполяция, не прямое исследование именно task-log-паттернов); **явный honesty-flag**: agent-harness-registry НЕ подтверждён как источник конкретно для task-logging taxonomy, несмотря на то, что он релевантен смежной теме (память) в Л3.

### 4.4 Критерии выбора — таблица

| Критерий | (а) Папка + набор файлов на задачу | (б) Единый общий лог | (в) Общая папка, 1 файл на задачу |
|---|---|---|---|
| **Solo vs команда** | Solo/small team — не создаёт merge-конфликтов на общем файле, но плодит директории | Команда — все видят общую хронологию в одном месте, но общий файл = частые git-конфликты при параллельной работе | Команда среднего размера — конфликтов меньше чем (б) (разные файлы), обзор проще чем (а) (плоская структура) |
| **Single-session vs multi-session/долгоживущая задача** | Долгоживущая, сложная задача — несколько артефактов (план/заметки/отчёт) естественно расходятся по файлам | Короткие, частые задачи — расход на файл-на-задачу не оправдан, важнее непрерывная хронология | Задача среднего размера, укладывающаяся в «один PR» (см. Backlog.md rationale «each task = one context window = one PR») |
| **Нужен ли аудит-след** | Да, детальный — множественность файлов сохраняет промежуточные шаги, не только итог | Да, хронологический — общий лог даёт «что и когда», но не глубину по конкретной задаче | Частично — один файл на задачу даёт итог + основные поля, но не пошаговую историю внутри задачи |
| **Сложность задачи** | Высокая — оправдывает накладные расходы на структуру директории | Низкая-средняя — оверхед одной строки/секции в общем файле мал | Средняя — структурированный frontmatter (status/id/acceptance criteria) без глубины (а) |
| **Машинная обрабатываемость** (semver/changelog-автоматизация, ср. §3.1) | Низкая по умолчанию — нужен отдельный индекс, чтобы агрегировать | Высокая, если формат единообразен (как Conventional Commits для коммитов) | Средняя-высокая — frontmatter на файл даёт структурированный запрос по всем задачам (как в Backlog.md `task list`) |
| **Персистентность за пределами сессии** | Да | Да | Да |
| **Пример из источников** | `notes/research/lecture-N/*.md` этого курса; типичный research/production паттерн | `.changelog/CHANGELOG.md` append-паттерн; `notes/decisions.md` этого курса (ENFORCED в CLAUDE.md) | Backlog.md (`backlog/*.md`, MIT, MrLesk) |
| **НЕ файловый паттерн (контраст)** | — | — | — Claude Code TodoWrite/Task* — session-scoped, диска не касается (§4.2); git-commit-history как единственный лог (§3.4) — оба не подходят ни под одну из трёх колонок |

**Как читать таблицу для §3 главы:** нет одного «правильного» паттерна — критерий выбора всегда composite (solo+короткие задачи чаще тянут к (б); команда+долгие сложные задачи — к (а); команда+задачи размером с PR — к (в)). Главное методическое сообщение — **осознанный выбор под три оси (кто, как долго, зачем аудит-след)**, а не default по привычке.

**Confidence: MEDIUM** на таблице целиком — синтез курса из независимо подтверждённых фрагментов (каждая ячейка либо цитирует источник §4.1-4.3, либо явно логический вывод из них), не готовая taxonomy из одного источника.

---

## 5. Обзорный ландшафт инструментов (для лёгкого упоминания, не для глубины §3)

Отдельный от механики курса (Skills/MCP/git/логирование) слой — **какими программами** это всё запускается. Agentic IDE (Cursor и класс — VS Code форки со встроенным агентным циклом: Windsurf, аналоги) — отдельная категория инструмента от терминального кодинг-агента (Claude Code/Codex CLI), уже частично покрыта в `tools-landscape.md` (не переисследуем здесь). **Sub-agents как примитив** — уже разобран в `anthropic-sdlc-kit.md` (Cross-cutting таблица, строка «Custom sub-agents (`.claude/agents/*.md`)» — «Isolated context + own tool allowlist + own model; delegate research/review without cluttering main context», code.claude.com/docs/en/sub-agents) — здесь просто ссылка, не повторное исследование. Для §3 главы этот раздел — материал для отдельного лёгкого «обзор инструментов» абзаца, не для глубокого разбора наравне с блоками 1-4.

**Confidence: N/A** (ссылочный раздел, не новое исследование).

---

## Источники (полный список, все доступны 2026-09-19)

**Skills:**
1. https://code.claude.com/docs/en/skills — SKILL.md формат, frontmatter-поля, Skills vs CLAUDE.md vs AGENTS.md, Agent Skills standard (primary, HIGH)
2. https://agentskills.io — Agent Skills open standard (referenced by #1, не fetch напрямую в этом проходе)
3. https://developers.openai.com/codex/skills — OpenAI Codex skills (secondary поиск, MEDIUM)
4. https://developers.openai.com/codex/concepts/customization — OpenAI Codex custom instructions / AGENTS.md (secondary поиск, MEDIUM)

**MCP для кодинга:**
5. https://github.com/github/github-mcp-server — toolsets, read-only флаг, token security guidance (primary, HIGH)
6. https://github.com/microsoft/playwright-mcp — Playwright MCP server (primary repo, HIGH на факте существования/назначения; MEDIUM на CLI-vs-MCP token-efficiency claim из вторичного блога)
7. https://arcjet.com/learn/lethal-trifecta — MCP как вектор lethal trifecta, GitHub MCP инцидент-пример (secondary, MEDIUM)
8. https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ — первоисточник термина (уже в `references-and-req-engineering.md` курса, не дублируется здесь как новая находка)

**Git-конвенции:**
9. https://www.conventionalcommits.org/en/v1.0.0/ — Conventional Commits canonical spec (primary, HIGH)
10. https://conventionalbranch.org/ — Conventional Branch v1.1.0, AI Agent Source Prefixes (primary, HIGH)
11. https://www.buildmvpfast.com/blog/git-workflow-ai-assisted-development-agent-commits-2026 — «5-10x commits», «never commit to shared branch» (secondary blog, MEDIUM/LOW)
12. https://dev.to/jackm-singularity/ai-code-review-packet-make-agent-written-pull-requests-easy-to-trust-2c0g — PR review packet структура (secondary, MEDIUM)
13. https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/ — GitHub официальный блог про ревью агентных PR (primary-adjacent, MEDIUM-HIGH)
14. https://marimo.io/features/vs-jupyter-alternative — notebook-as-Python-file, git-friendly альтернатива Jupyter (primary vendor, MEDIUM)
15. https://monorepo.tools/ai — монорепо + AI agents convergence (secondary aggregator, MEDIUM)
16. https://addyosmani.com/blog/ai-coding-workflow/ — git commits как единственный лог, «commit early and often» (primary practitioner blog, MEDIUM)

**Task-logging паттерны:**
17. https://github.com/MrLesk/Backlog.md — паттерн (в), «each task = one context window = one PR» (primary repo, HIGH)
18. https://code.claude.com/docs/en/agent-sdk/todo-tracking — TodoWrite/Task* механика, session-scoped, жизненный цикл (primary, HIGH)
19. https://streamkap.com/resources-and-guides/decision-traces-ai-agents — append-only CHANGELOG-паттерн (secondary, MEDIUM)
20. https://github.com/workain/agent-harness-registry — использован курсом в Л3 (память-категория); **проверено в этом проходе на предмет task-log taxonomy — не найдено**, honesty-flag зафиксирован в §4.3 (primary repo, но не покрывает эту конкретную тему)

**Landscape (ссылочно, не переисследовано):**
- `notes/research/lecture-4/tools-landscape.md` (existing)
- `notes/research/lecture-4/anthropic-sdlc-kit.md` — sub-agents row (existing)

---

## Honesty flags / gaps (declared)

1. **Vendor-neutral skills-эквивалентность** (§1.3) — подтверждена для OpenAI Codex (собственный `skills` механизм поверх agentskills.io standard); для Cursor/остальных инструментов в найденных источниках чёткого on-demand-skill-эквивалента (в противовес always-on rules/AGENTS.md) не обнаружено — не выдумываем, явно помечено как отсутствие подтверждения.
2. **Playwright MCP «CLI+Skills лучше MCP для высокой пропускной способности»** (§2.1) — вторичный практический блог, не первичная позиция Microsoft/Anthropic; помечено MEDIUM, не выдавать за консенсус.
3. **Git-конвенции для non-git контекстов** (§3.4) — честно признано «мало устоявшейся практики»: Jupyter/marimo решение — смена формата хранения, а не альтернатива git; нестандартный монорепо-workflow без git вообще — UNVERIFIABLE в этом проходе, источники не покрывают.
4. **agent-harness-registry и task-logging** (§4.3) — прямо проверено WebFetch на предмет наличия task-log-taxonomy в репозитории; **не найдено** в текущем содержимом README/докс на дату фетча. Реестр остаётся валидным источником для Л3 (память-категория), но НЕ используется здесь как источник для §4.1-4.4 taxonomy — эта таксономия построена из независимых источников (#17-19).
5. **PR-описание шаблон** (§3.3) — устойчивый практический консенсус 2026 года из нескольких независимых блогов/GitHub-блога, но нет единого canonical-стандарта уровня Conventional Commits; помечено MEDIUM.
6. **Критериальная таблица §4.4** — синтез курса, не готовая taxonomy одного источника; каждая ячейка либо прямая цитата, либо явный логический вывод — не выдаётся за первоисточник.
7. **`[VFY-day-of]` volatile items:** GitHub MCP toolset-список (быстро меняется по версиям), Conventional Branch AI Agent Source Prefixes adoption-темп (фича 2026 года, молодая), SKILL.md frontmatter-поля состав (Claude Code-специфичные расширения могут добавляться/убираться), TodoWrite/Task* API — точные имена инструментов и версия перехода (v2.1.268) могут измениться к дню лекции.

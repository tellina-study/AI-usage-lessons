# Lecture 4 — Harness/env-org practices + Architecture-with-AI practices

**Date:** 2026-08-30 · **Researcher:** research subagent · **Lecture:** «AI в жизненном цикле разработки ПО (SDLC)» (МГТУ ИУ6, 3rd year, RU, 2026), methodology-first pivot (practices over tools).
**Purpose:** fill two gap areas the prior research under-covered — (1) как организовать среду/репозиторий/harness для эффективной и безопасной AI-agent SDLC; (2) как формировать, контролировать и поддерживать архитектуру в AI-native SDLC.
**Sibling files (read first, no duplication):** `anthropic-sdlc-kit.md`, `methodologists-and-failures.md`, `failures-and-limitations.md`, `sources.md`.
**Access date for all URLs:** **2026-08-30**. Primary sources prioritized.
`[VFY-day-of]` = volatile (product/version/ring-label/annual-number) — re-verify on lecture day.

---

# AREA 1 — Организация среды / репозитория / harness для AI-agent SDLC

**Сквозная ось (through-line):** детерминированный каркас (линтеры, структурные тесты, PR-гейты, guardrails) **оборачивает** недетерминированную модель → контекст **курируется** (JIT, компакция, память, борьба с context rot) → **AGENTS.md / rules** = слой постоянных инструкций → **Spec-Kit** дробит работу на малые проверяемые задачи → **agentic workflows** обеспечивают least-privilege / sandbox / egress / PR-as-gate → **evals из реальных провалов** замыкают цикл. Одна идея повторяется: **constrain, verify, feed failures back.**

## A1. Практики — что делать → зачем → источник

| Практика | Суть (что делать и зачем) | Первичный источник | Volatile? |
|---|---|---|---|
| **AGENTS.md — открытый стандарт** | Единый предсказуемый Markdown-файл с контекстом проекта для агента. Сайт стандарта НЕ навязывает схему («just standard Markdown. Use any headings you like»); собственный пример использует `## Setup commands`, `## Code style`, `## Dev environment tips`, `## Testing instructions`, `## PR instructions`. Принцип: «anything you'd tell a new teammate». | agents.md | no (контент); adoption [VFY-day-of] |
| **AGENTS.md — build/test как явные команды** | Пример: `Install deps: pnpm install` / `Run tests: pnpm test`; code-style как правила (`TypeScript strict mode`, `Single quotes, no semicolons`). Даёт агенту детерминированный способ собрать/проверить работу — без этого он галлюцинирует setup (ср. Böckeler onboarding). | agents.md | no |
| **AGENTS.md — adoption / экосистема** | «Over 60,000 open-source projects» + читают OpenAI Codex, Google Jules, Aider, goose, Zed, Warp, VS Code, Devin, JetBrains Junie, Cursor, GitHub Copilot и др. — вендор-нейтральное имя, к которому сходится индустрия. | agents.md | **[VFY-day-of]** |
| **CLAUDE.md vs AGENTS.md** | CLAUDE.md — Anthropic-native, авто-читается; AGENTS.md — tool-agnostic имя того же слоя. CLAUDE.md держит «most frequently repeated general conventions that apply to the whole project» (e.g. «we use yarn, not npm»). agents.md сам НЕ описывает связь с CLAUDE.md — источник связи Cursor + Böckeler (honesty flag). | code.claude.com/docs/en/memory; martinfowler.com …/context-engineering-coding-agents.html | no |
| **Cursor rules — что содержать** | «Encode domain-specific knowledge…; automate project-specific workflows or templates; standardize style or architecture decisions.» 4 типа: Always Apply · Apply Intelligently · Apply to Specific Files (glob) · Apply Manually (@-mention). Формат `.mdc` в `.cursor/rules/`, версионируется. | cursor.com/docs/context/rules | no (types [VFY]) |
| **Cursor rules — что делает правило хорошим** | «Good rules are focused, actionable, and scoped.» <500 строк, дробить большие, давать конкретные примеры, писать «like clear internal docs». **Избегать:** копировать весь style-guide («use linters instead»), документировать каждую CLI-команду, дублировать то, что уже в коде. Cursor называет AGENTS.md «a simpler markdown alternative… when structured rules overhead isn't needed». | cursor.com/docs/context/rules | no |
| **Harness engineering (Böckeler)** | «The harness» = система tooling + practices, удерживающая агентов надёжными и обслуживаемыми at scale. Эффективная AI-разработка = **сужение solution space** явной структурой и верификацией, а не максимизация свободы генерации. 3 функциональные категории: (1) context engineering (базы знаний + динамический контекст); (2) **architectural constraints** — детерминированные линтеры + структурные тесты рядом с недетерминированными LLM-агентами; (3) entropy management — периодические «garbage collection» агенты, ловящие несогласованности. | martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html (2026-02-17) | no |
| **Harness — feedback loop** | «When the agent struggles, we treat it as a signal: identify what is missing — tools, guardrails, documentation — and feed it back.» Каждый сбой агента → апдейт каркаса. | там же | no |
| **Harness — честное ограничение** | Каркас (линтеры + структурные тесты) оборачивает модель, но сам **не** подтверждает поведенческую корректность («lacks verification of functionality and behaviour»). → нужны отдельные behavior-тесты + человек. | там же | no |
| **Context engineering — минимум высокосигнальных токенов** | Цель: «the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome». Производительность деградирует по мере заполнения окна. | anthropic.com/engineering/effective-context-engineering-for-ai-agents (2025-09-29) | no |
| **JIT-retrieval** | Хранить лёгкие идентификаторы (пути, запросы), «dynamically load data into context at runtime using tools»; «each interaction yields context that informs the next decision». Не грузить всё заранее. | там же | no |
| **Compaction (компакция)** | «taking a conversation nearing the context window limit, summarizing its contents, and reinitiating a new context window with the summary». | там же | no |
| **Agentic notes / persistent memory** | «the agent regularly writes notes persisted to memory outside of the context window. These notes get pulled back into the context window at later times». Cookbook-протокол: «ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE… Your context window might be reset at any moment.» Демо: 172k токенов пик с памятью vs 334k без. | anthropic.com …/effective-context-engineering…; platform.claude.com/cookbook/…context-engineering-tools | no; токены/типы [VFY-day-of] |
| **Три примитива по типу bloat (decision rule)** | Compaction (диалог, который нельзя пере-запросить) · Tool-result clearing (большой **пере-запрашиваемый** вывод — дешевле всего, lossless) · Memory tool (кросс-сессионное знание). «If your context bloat is mostly re-fetchable tool output, clearing is cheaper and lossless… If it's dialogue and reasoning that can't be re-fetched, compaction is the right fit.» | platform.claude.com/cookbook/…context-engineering-tools | API-строки [VFY] |
| **Строить контекст инкрементально (Böckeler)** | «build context like rules files up gradually, and not pump too much stuff in there right from the start»; конфиги полугодовой давности могут стать лишними по мере роста моделей; не дублировать, не создавать противоречий. Прозрачность заполнения окна — «a crucial feature». | martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html (2026-02-05) | no |
| **Context rot (первоисточник)** | 18 frontier-моделей: точность recall падает **нелинейно** с ростом входа даже на тривиальном retrieval — деградация начинается **до** переполнения окна. «what matters more is how that information is presented» → курировать и структурировать, не сваливать. | trychroma.com/research/context-rot (Chroma, 2025-07-14) | no |
| **Runbooks / operational history как контекст агента** | *Emerging practice (нет канонического первоисточника — honesty flag).* Кодировать прошлые инциденты/how-to как **retrievable структурированные доки** (detection→investigation→remediation) + human-approval gates + audit trail, чтобы агент переиспользовал операционное знание. Механизм — memory/note-taking примитивы (выше), а не отдельный стандарт. | (secondary: incident.io, ilert; OSS: github.com/Runbook-Agent/RunbookAI) | **[VFY-day-of]** |
| **Task tracking — spec-driven декомпозиция** | Workflow: `/constitution` (принципы) → `/specify` (что/зачем) → `/plan` (архитектура) → `/tasks` (дискретные задачи) → `/implement` → `/analyze`+`/converge` (cross-artifact согласованность). Конституция+спека+план — постоянный контекст, наследуемый каждой задачей. | github.blog …/spec-driven-development-with-ai…; github.com/github/spec-kit | namespace `/speckit.*` [VFY] |
| **Малые проверяемые единицы** | «Each task should be something you can implement and test in isolation; this is crucial because it gives the coding agent a way to validate its work.» Конкретика вместо абстракции: не «build authentication», а «create a user registration endpoint that validates email format». | github.blog …/spec-driven-development-with-ai… | no |
| **PR-as-gate + least-privilege (agentic workflows)** | Агент читает состояние через read-only MCP, «cannot write anything directly — not even add a comment». Записи буферизуются через **Safe Outputs** и мапятся на «pre-approved, reviewable GitHub operations such as creating a pull request or adding a comment» → PR/коммент = видимый человеку гейт, «instead of silent mutation». | github.blog …/under-the-hood-security-architecture-of-github-agentic-workflows/ (2026-03-09) | no |
| **Evals из реальных провалов** | ~20–50 простых задач из реальных сбоев; «your bug tracker and support queue are your best source material». Проверять **исход/состояние** (тесты прошли, записи изменились, side-effects совпали), а не только финальный текст. «Design tasks that two experts would grade identically.» | anthropic.com/engineering/demystifying-evals-for-ai-agents | no |

## A2. Провалы / пределы (Area 1) — для правила ≥30% strict-in

- **Poisoned context** (Böckeler): ассистент «cannot distinguish high-quality code from poor code» → усиливает доминирующий в кодбазе паттерн, даже тот, от которого уходят. **Урок:** плохой контекст → плохая генерация. **Альтернатива:** курировать open files / rules, AI-friendly modular design. martinfowler.com/articles/exploring-gen-ai/04-coding-assistance-how-in-the-way.html
- **Context rot** (Chroma): больше токенов ≠ лучше; recall падает до переполнения. **Урок:** «kitchen-sink» сессии активно деградируют вывод. **Альтернатива:** JIT + compaction + memory + минимум высокосигнальных токенов. trychroma.com/research/context-rot
- **Harness сам не проверяет поведение** (Böckeler): детерминированные линтеры/структурные тесты не подтверждают функциональную корректность. **Урок:** guardrails ≠ верификация. **Альтернатива:** отдельные behavior-тесты + человек-в-гейте.
- **Governance decay** (Anthropic security, sibling-file): «if a skill goes stale… the whole structure degrades». **Урок:** незаряжаемые context-файлы молча гниют. **Альтернатива:** активное обслуживание, sampling решений.
- **Runbooks-as-context — нет зрелого стандарта.** **Урок:** практика emerging, не settled; не выдавать вендор-блоги за канон. **Альтернатива:** опираться на memory/note-taking примитивы.

---

# AREA 2 — Архитектура и дизайн С ИИ: как формировать, контролировать, поддерживать

**Коррекция к прежней позиции.** Прежний тезис «нет вендор-продукта для архитектуры → архитектура вне AI-SDLC» — **wrong-emphasis.** Правильный фрейм: архитектура — **человеко-владеемый слой durable-контекста и governance**, вокруг которого AI генерирует код. Есть зрелые практики: ADR, fitness functions, architecture-as-code/C4, sequencing «архитектура ДО кода».

## B1. Практики — что делать → зачем → источник

| Практика | Суть (что делать и зачем) | Первичный источник | Volatile? |
|---|---|---|---|
| **ADR — Architecture Decision Records** | Фиксировать «architecturally significant» решения (влияют на структуру, non-functional, зависимости, интерфейсы). 5 секций: **Title · Context** (силы: тех/полит/соц/локальные) **· Decision** (в active voice) **· Status** (proposed/accepted/deprecated/superseded) **· Consequences** (все, не только позитивные). | cognitect.com/blog/2011/11/15/documenting-architecture-decisions (Nygard) | no (canonical) |
| **ADR — почему lightweight** | «Large documents are never kept up to date. Small, modular documents have at least a chance at being updated.» 1–2 страницы, одна декизия на запись, **timestamped, immutable** (supersede, не переписывать). | cognitect.com/…; github.com/joelparkerhenderson/architecture-decision-record; adr.github.io | no |
| **ADR — хранить в source control** | Thoughtworks Radar (**ADOPT**): «store these details in source control, instead of a wiki or website… a record that remains in sync with the code itself». | thoughtworks.com/radar/techniques/lightweight-architecture-decision-records | ring [VFY] |
| **ADR как durable-контекст для AI** *(emerging, 2026 practitioner consensus — не канон)* | Код хранит **что** изменилось, git не хранит **почему** — «the reasoning is the part nothing stores»; ADR = «the one artifact that survives» между stateless-сессиями агента. Классический ADR писался для человека, читающего изредка; «an agent reads all of them, every session, under a token budget, and acts on them literally» → писать ADR под агента (кратко, однозначно). | braingrid.ai/blog/architecture-decision-records-for-ai-coding-agents; actual.ai/blog/agent-optimized-adrs | **[VFY-day-of]** |
| **Fitness functions (определение)** | «A fitness function is used to summarize how close a given design solution is to achieving the set aims»; архитектурная FF «provides an objective integrity assessment of some architectural characteristics» — сохранять характеристики «in an automated, continual manner» (unit-тесты, метрики, мониторы). | thoughtworks.com/radar/techniques/architectural-fitness-function | ring/дата [VFY] |
| **Evolutionary architecture (3 принципа)** | Incremental development · fitness functions · support for change. «Evolutionary architectures make it explicit what 'fit' means with as much automation as possible.» | evolutionaryarchitecture.com (Ford/Parsons/Kua) | no |
| **FF как governance для AI-кода** | FF = «your definition of good»; объективность — суть (Parsons: «you and I will never disagree on whether it passes or not»). Использовать genAI, чтобы **писать** FF; и FF — чтобы валидировать, что сгенерированный/подменённый код держит latency, cost, bias. Deterministic FF стерегут «dependency direction, contract shape, latency budgets, security posture»; «agentic judgment layer» для субъективного, но «do not replace deterministic fitness functions or architects». | thoughtworks.com/insights/podcasts/…/how-fitness-functions-help-govern-measure-ai (2025-03-06); infoq.com/articles/agentic-fitness-functions-evolutionary-architecture/ (2026-08-17) | infoq дата [VFY] |
| **C4 model** | «developer friendly approach to software architecture diagramming», notation- и tooling-independent. 4 уровня зума: **Context** (система+пользователи+внешние) · **Container** (deployable units) · **Component** (логические группы внутри контейнера) · **Code** (классы). | c4model.com (Simon Brown) | no |
| **Diagrams-as-code / models-as-code** | Диаграммы из текста → version control + diff. PlantUML, Mermaid — format-locked; **Structurizr DSL** = «models as code» (одна модель → много рендеров). Radar «Diagrams as code» (Trial). | dev.to/simonbrown/diagrams-as-code-20eo; thoughtworks.com/radar/techniques/diagrams-as-code; plantuml.com; mermaid.js.org; structurizr.com | ring [VFY] |
| **Architecture-as-code, читаемая AI + drift-detection** | «LLMs excel at generating text — the Structurizr DSL is text-based, version controllable, and diff-friendly.» Model-based DSL авто-энфорсит C4-иерархию (не даёт AI сделать невалидную диаграмму) + MCP-сервер + **AI drift detection** (модель vs код). | docs.structurizr.com/ai | **[VFY-day-of]** |
| **Essential vs accidental complexity (Brooks)** | Essence = «difficulties inherent in the nature of the software» (data sets, relationships, algorithms, invocations); accidents = «not inherent». Трудное — «specification, design, and testing of this conceptual construct, not the labor of representing it». → AI режет accidental (boilerplate/синтаксис), НЕ essential (что строить, концептуальный дизайн) — это остаётся за человеком. | sunnyday.mit.edu/16.355/BrooksNoSilverBullet2.html; cs.unc.edu/techreports/86-020.pdf | no (canonical) |
| **Modularity держит контекст AI управляемым** | «modularity and abstractions keep AI's context manageable by limiting necessary changes»; «AI coding assistants also perform better with well-factored codebases». | thoughtworks.com/radar/techniques/ai-friendly-code-design | ring [VFY] |
| **Ревью AI-дизайнов** | Настороженность: «growing complacency with AI-generated code, and developers becoming reluctant to review large AI-made change sets» → держать change-sets малыми (ср. spec-kit «test in isolation»), человек владеет дизайн-решениями. *(Нет одного standalone-первоисточника «humans must own design» — строится из Brooks + этого блипа.)* | thoughtworks.com/radar/techniques/ai-friendly-code-design + Brooks | no |
| **Sequencing: архитектура ДО кода** | Spec-Kit: `/plan` = архитектурный шаг («provide your tech stack and architecture choices»), генерит `data-model.md`, `contracts/`, `research.md` **до** `/tasks`+`/implement`. Kiro: `requirements.md` (что) → **`design.md`** («technical architecture, sequence diagrams… documented before moving to task implementation») → `tasks.md`. Архитектура-до-кода — **структурный гейт**, не привычка. | github.com/github/spec-kit (+ spec-driven.md); kiro.dev/docs/specs/ | commands [VFY] |

## B2. Провалы / пределы (Area 2) — для правила ≥30% strict-in

- **Poisoned context** (Böckeler): «We call this a poisoned context, and we don't really have a good way to mitigate this yet.» Неописанная/плохая архитектура → AI амплифицирует антипаттерны. **Урок:** архитектуру нужно **описать и управлять**, иначе AI её эродирует. **Альтернатива:** ADR + fitness functions + architecture-as-code. martinfowler.com/…/04-coding-assistance-how-in-the-way.html
- **Codebase cognitive debt** (Radar v34, апр 2026): «the growing gap between a system's implementation and a team's shared understanding of how and why it works»; в отличие от техдолга (в коде) — cognitive debt «resides in the minds of the developers». Усугубляется «coding agent swarms». **Remedy названо: architectural fitness functions.** **Урок:** генерация обгоняет понимание. **Альтернатива:** FF + ограничить темп + shared understanding. thoughtworks.com/radar/techniques/codebase-cognitive-debt; press: thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34
- **Complacency with AI-generated code** (Radar **Hold**): GitClear — дубликаты↑, рефакторинг↓; Microsoft — «AI-driven confidence often comes at the expense of critical thinking»; «AI now generates larger change sets that are harder to review». **Урок:** AI-код ревьюить БОЛЬШЕ. **Альтернатива:** малые change-sets + обязательный human-review. thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code
- **Architecture erosion (академ. определение)**: «a growing gap between the intended and the implemented architecture» → деградация maintainability (OpenStack code-review study). **Урок:** дрейф реализации от намерения. **Альтернатива:** fitness functions + drift-detection (Structurizr AI). arxiv.org/pdf/2201.01184
- **AI ухудшает архитектуру (документир. кейс, SIG, май 2026 — [VFY])**: AI-вывод «1.7 times more issues» vs человек; adoption растит техдолг «30–41%»; FastRender: 3M+ строк AI-Rust → «1.3/5 for maintainability, 2.1/5 for architecture quality». «Like a very clever and super-fast intern, but not with a lot of experience.» **Урок:** скорость генерации ≠ качество архитектуры. **Альтернатива:** human-owned дизайн + governance. softwareimprovementgroup.com/blog/architectural-debt-ai/ **[VFY-day-of]**
- **«AI slop»** (Willison, primary): «unwanted AI-generated content»; «if it's mindlessly generated and thrust upon someone who didn't ask for it, slop is the perfect term». *Honesty: «AI slop architecture» — не канон-термин; фреймить как пересечение «AI slop» + «architecture erosion».* simonwillison.net/2024/May/8/slop/

---

# TOP-8 первичных источников (для final message; access 2026-08-30)

1. https://agents.md — AGENTS.md open standard (recommended sections, adoption)
2. https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html — Böckeler, harness engineering (2026-02-17)
3. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — JIT / compaction / agentic notes / context rot
4. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ — Spec-Kit: малые проверяемые задачи, `/plan`=архитектура
5. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions — Nygard, ADR (canonical)
6. https://www.thoughtworks.com/radar/techniques/architectural-fitness-function — fitness functions (canonical def)
7. https://c4model.com — C4 model (architecture-as-code AI can consume)
8. https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt — documented failure: gen обгоняет понимание, remedy = FF (2026)

---

# Полный список URL (all accessed 2026-08-30)

**AREA 1:**
- https://agents.md
- https://cursor.com/docs/context/rules
- https://code.claude.com/docs/en/memory
- https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html
- https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- https://www.trychroma.com/research/context-rot
- https://platform.claude.com/cookbook/tool-use-context-engineering-context-engineering-tools
- https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
- https://github.com/github/spec-kit
- https://github.blog/ai-and-ml/generative-ai/under-the-hood-security-architecture-of-github-agentic-workflows/
- https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- (secondary/illustration only) https://incident.io/blog/runbook-automation-tools-2026-the-complete-guide · https://www.ilert.com/blog/runbooks-are-history · https://github.com/Runbook-Agent/RunbookAI

**AREA 2:**
- https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- https://adr.github.io
- https://github.com/joelparkerhenderson/architecture-decision-record
- https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records
- https://www.braingrid.ai/blog/architecture-decision-records-for-ai-coding-agents [VFY]
- https://www.actual.ai/blog/agent-optimized-adrs [VFY]
- https://www.thoughtworks.com/radar/techniques/architectural-fitness-function
- https://evolutionaryarchitecture.com
- https://www.thoughtworks.com/insights/podcasts/technology-podcasts/how-fitness-functions-help-govern-measure-ai
- https://www.infoq.com/articles/agentic-fitness-functions-evolutionary-architecture/ [VFY]
- https://c4model.com
- https://dev.to/simonbrown/diagrams-as-code-20eo
- https://docs.structurizr.com/ai [VFY]
- https://www.thoughtworks.com/radar/techniques/diagrams-as-code
- http://sunnyday.mit.edu/16.355/BrooksNoSilverBullet2.html · https://www.cs.unc.edu/techreports/86-020.pdf
- https://www.thoughtworks.com/radar/techniques/ai-friendly-code-design
- https://github.com/github/spec-kit/blob/main/spec-driven.md · https://kiro.dev/docs/specs/
- https://martinfowler.com/articles/exploring-gen-ai/04-coding-assistance-how-in-the-way.html
- https://www.thoughtworks.com/radar/techniques/codebase-cognitive-debt · https://www.thoughtworks.com/about-us/news/2026/combat-ai-cognitive-debt-radar-v34
- https://www.thoughtworks.com/en-us/radar/techniques/complacency-with-ai-generated-code
- https://arxiv.org/pdf/2201.01184
- https://www.softwareimprovementgroup.com/blog/architectural-debt-ai/ [VFY]
- https://simonwillison.net/2024/May/8/slop/

---

# Honesty flags / gaps (declared)

1. **agents.md не описывает связь с CLAUDE.md/.cursorrules** — связь из Cursor docs + Böckeler.
2. **Harness-memo не покрывает sandboxing/egress** — least-privilege/PR-gate из GitHub Agentic Workflows security post.
3. **Runbooks-as-agent-context — нет канонического первоисточника**; только вендор/secondary блоги + один OSS README. Подавать как emerging practice, механизм = memory/note-taking примитивы.
4. **ADR-for-AI framing** — 2026 practitioner-blog consensus, НЕ Nygard/Thoughtworks канон. Подавать как emerging.
5. **Нет канон-термина «AI slop architecture»** — пересечение «AI slop» (Willison) + «architecture erosion» (arXiv).
6. **Нет одного standalone-первоисточника «humans must own design in AI era»** — строится из Brooks + AI-friendly-code-design блипа.
7. **Radar volume-номера + ring-labels** расходятся search vs fetch → все `[VFY-day-of]`.
8. **SIG-метрики** (1.7×, 30–41%, FastRender 1.3/2.1) частично re-cite secondary → verify перед слайдом.
9. **[VFY-day-of] версионное:** agents.md adoption counts/tool-list; Spec-Kit namespace `/speckit.*`; Claude memory/compaction API-строки и токен-цифры; Structurizr AI wording; arXiv preprints (2510.22787).

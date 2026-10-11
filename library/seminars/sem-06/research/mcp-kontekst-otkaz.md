# Отказ от загрузки описаний MCP-инструментов в контекст — проверка по первоисточникам

**Дата чтения всех источников: 2026-10-07.** Метод: веб-поиск применялся только для нахождения URL.
Каждая цитата ниже прочитана на странице первоисточника. Для всех ключевых утверждений сделано
**два независимых прохода**: (1) WebFetch, (2) прямое скачивание страницы (`curl`) с извлечением
текста и дословным поиском подстроки. Расхождения между проходами отмечены явно.

## Главный вывод, который нельзя искажать

**Ни одна из проверенных компаний не отказалась от протокола MCP.** Отказ во всех
подтверждённых случаях касается **одной конкретной практики** — загружать описания всех
инструментов в контекст заранее. MCP-серверы при этом сохраняются; меняется способ, которым
описания доходят до модели. Формулировка «крупные компании отказались от MCP» первоисточниками
**не подтверждается ни в одном случае**.

Второй вывод, важный для занятия: **единого отраслевого решения нет.** Anthropic и Cloudflare
ушли в исполнение кода; GitHub/Microsoft — в маршрутизацию по эмбеддингам и сокращение набора;
Manus прямо **отвергла** загрузку инструментов по требованию и выбрала маскирование логитов.
Три разных ответа на одну задачу.

---

## Случай 1. Anthropic, инженерный блог — VERIFIED

**Что утверждается:** прямая загрузка определений инструментов перегружает контекстное окно;
решение — представлять MCP-серверы как кодовое API, которое агент читает по требованию.

- **URL:** https://www.anthropic.com/engineering/code-execution-with-mcp
- **Заголовок (дословно со страницы):** «Code execution with MCP: Building more efficient agents»
- **Дата публикации (на странице):** «Published Nov 04, 2025»
- **Статус: VERIFIED.** Оба прохода совпали дословно, включая число 98.7% и тире-em-dash.

Дословные цитаты (язык оригинала):

> «As MCP usage scales, there are two common patterns that can increase agent cost and latency:
> Tool definitions overload the context window; Intermediate tool results consume additional tokens.»

> «Most MCP clients load all tool definitions upfront directly into context, exposing them to the
> model using a direct tool-calling syntax.»

> «In cases where agents are connected to thousands of tools, they'll need to process hundreds of
> thousands of tokens before reading a request.»

> «This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%.»

> «Every intermediate result must pass through the model. In this example, the full call transcript
> flows through twice. For a 2-hour sales meeting, that could mean processing an additional 50,000
> tokens. Even larger documents may exceed context window limits, breaking the workflow.»

Что предложено взамен:

> «With code execution environments becoming more common for agents, a solution is to present MCP
> servers as code APIs rather than direct tool calls. The agent can then write code to interact with
> MCP servers. This approach addresses both challenges: agents can load only the tools they need and
> process data in the execution environment before passing results back to the model.»

> «Progressive disclosure. Models are great at navigating filesystems. Presenting tools as code on a
> filesystem allows models to read tool definitions on-demand, rather than reading them all up-front.
> Alternatively, a search_tools tool can be added to the server to find relevant definitions.»

**Важная оговорка для слайда.** Число 150 000 → 2 000 относится к конкретному разобранному в статье
примеру (серверы Google Drive и Salesforce), а не к измерению «в среднем по индустрии». На странице
нет указания на методику замера. Подавать как «пример из статьи Anthropic», а не как отраслевую норму.

**Проверено отдельно:** в статье есть прямая отсылка к Cloudflare —
> «Cloudflare published similar findings, referring to code execution with MCP as "Code Mode."»

---

## Случай 2. Anthropic, официальная документация API («tool search tool») — VERIFIED

Это **отдельный от блога первоисточник** с другими числами. Самый пригодный для слайда, потому что
числа привязаны к названному набору серверов.

- **URL:** https://docs.claude.com/en/docs/agents-and-tools/tool-use/tool-search-tool
- **Дата публикации:** на странице **не указана** (живая документация). Идентификаторы инструментов
  содержат дату `20251119`, то есть механизм датируется не ранее 19.11.2025.
- **Статус: VERIFIED** (дословный поиск подстроки по скачанной странице).

> «The tool search tool lets Claude work with hundreds or thousands of tools by discovering and
> loading them on demand. Instead of loading all tool definitions into the context window up front,
> Claude searches your tool catalog (including tool names, descriptions, argument names, and argument
> descriptions) and loads only the tools it needs.»

> «Loading every tool definition up front causes two problems as a tool library grows: Context bloat:
> A typical multiserver setup (GitHub, Slack, Sentry, Grafana, and Splunk) can consume ~55k tokens in
> definitions before Claude does any work. Tool search typically reduces this by over 85 percent,
> loading only the 3–5 tools Claude needs for a given request. Tool selection accuracy: Claude's
> ability to pick the right tool degrades once you exceed 30–50 available tools.»

Механизм (дословно):

> «You provide every tool definition in the tools array and set defer_loading: true on the tools that
> shouldn't load up front. At least one tool, normally the tool search tool itself, must stay
> non-deferred. Initially, Claude's context contains only the tool search tool and any non-deferred
> tools.»

**Честная оговорка.** В цитате про ~55k сказано «multiserver setup», а **не** «MCP servers» —
перечислены GitHub, Slack, Sentry, Grafana, Splunk. Слово «MCP» в теле этого абзаца отсутствует
(встречается только в навигации страницы). На слайде писать «набор из пяти серверов (GitHub, Slack,
Sentry, Grafana, Splunk)», а не приписывать документации слово «MCP» в этом месте.

**Два числа Anthropic не смешивать.** 150 000 → 2 000 (98.7%) — из блога, про исполнение кода.
~55k → «over 85 percent» — из документации, про tool search. Это **разные механизмы и разные
сценарии**, не два замера одного и того же. Ставить на один слайд как «одно и то же» — ошибка.

---

## Случай 3. Cloudflare «Code Mode» — VERIFIED, но гипотеза о причине НЕ ПОДТВЕРЖДЕНА

- **URL:** https://blog.cloudflare.com/code-mode/
- **Заголовок:** «Code Mode: the better way to use MCP»
- **Авторы:** Kenton Varda, Sunil Pai
- **Дата публикации:** `datePublished":"2025-09-26T13:00:00.000Z"` (из разметки страницы)
- **Статус: VERIFIED по тому, что сказано. Гипотеза «причина — переполнение контекста»
  НЕ ПОДТВЕРЖДЕНА.**

**Опровержение гипотезы, замер.** Прямой поиск по тексту страницы: словосочетание
**«context window» не встречается ни разу**. Слово «context» во всём тексте встречается 4 раза
(1 × `context`, 3 × `Context`) и ни разу не в значении «переполнение контекстного окна».
Причина, которую Cloudflare называет сама, — **распределение обучающих данных**, а не объём контекста:

> «The special tokens used in tool calls are things LLMs have never seen in the wild. They must be
> specially trained to use tools, based on synthetic training data. They aren't always that good at
> it. If you present an LLM with too many tools, or overly complex tools, it may struggle to choose
> the right one or to use it correctly.»

> «LLMs have seen a lot of code. They have not seen a lot of "tool calls".»

> «Making an LLM perform tasks with tool calling is like putting Shakespeare through a month-long
> class in Mandarin and then asking him to write a play in it. It's just not going to be his best work.»

Что делают взамен:

> «Most agents today use MCP by directly exposing the "tools" to the LLM. We tried something
> different: Convert the MCP tools into a TypeScript API, and then ask an LLM to write code that
> calls that API.»

> «We found agents are able to handle many more tools, and more complex tools, when those tools are
> presented as a TypeScript API rather than directly.»

> «our agent is presented with just one tool, which simply executes some TypeScript code. The code is
> then executed in a secure sandbox. The sandbox is totally isolated from the Internet. Its only
> access to the outside world is through the TypeScript APIs representing its connected MCP servers.»

Механизм изоляции — «the Worker Loader API», динамическая загрузка изолятов V8.

**Числа: НЕТ.** Ни токенов, ни процентов, ни числа инструментов. Фраза «The results are striking»
не сопровождается ни одной количественной величиной. Оба прохода согласны. **На слайде нельзя
приписывать Cloudflare никакие цифры.**

---

## Случай 4. Официальный GitHub MCP Server — VERIFIED, но с разворотом: механизм существовал и был УДАЛЁН

Это самый ценный случай для занятия по проверке фактов: гипотеза подтверждается **исторически** и
**опровергается для текущей версии**. Сниппет поиска, скорее всего, покажет флаг как действующий.

### 4.1. Текущее состояние (прочитано 2026-10-07)

- **URL:** https://raw.githubusercontent.com/github/github-mcp-server/main/README.md
- Файл 119 251 байт. Дословный поиск: **слово «dynamic» — 0 вхождений** (без учёта регистра).
  `enable_toolset`, `list_available_toolsets`, `get_toolset_tools` — **0 вхождений**.
- Дерево репозитория на `main` (GitHub API `git/trees?recursive=1`): файлов с «dynamic» в пути нет.
  Файлы `cmd/github-mcp-server/main.go` и `internal/ghmcp/server.go` скачаны и проверены — слово
  «dynamic» отсутствует. То есть удалено **из кода**, а не только из документации.
- **Статус: флаг `--dynamic-toolsets` в текущей версии НЕ СУЩЕСТВУЕТ.**

Что в README есть сейчас (это **статические** наборы, другой механизм):

> «The GitHub MCP Server supports enabling or disabling specific groups of functionalities via the
> `--toolsets` flag. This allows you to control which GitHub API capabilities are available to your
> AI tools. Enabling only the toolsets that you need can help the LLM with tool choice and reduce the
> context size.»

### 4.2. Историческое состояние — механизм был

Проверено дословным поиском по README на тегах (все прочитаны 2026-10-07):

| Тег | вхождений «dynamic» |
|---|---|
| v0.2.0 | 6 |
| v0.5.0 / v0.9.0 / v0.15.0 / v0.20.0 | 6 |
| v0.26.0 / v0.33.1 / v1.0.0 | 11 |
| v1.1.0 … v1.13.0 | **0** |
| v1.14.0 / v2.0.0 | **0** |

Удалено между **v1.0.0** и **v1.1.0**.

Дословно из README **v1.0.0** (https://raw.githubusercontent.com/github/github-mcp-server/v1.0.0/README.md):

> «## Dynamic Tool Discovery
>
> **Note**: This feature is currently in beta and is not available in the Remote GitHub MCP Server.
> Please test it out and let us know if you encounter any issues.
>
> Instead of starting with all tools enabled, you can turn on dynamic toolset discovery. Dynamic
> toolsets allow the MCP host to list and enable toolsets in response to a user prompt. This should
> help to avoid situations where the model gets confused by the sheer number of tools available.»

> «When using the binary, you can pass the `--dynamic-toolsets` flag.»
> `./github-mcp-server --dynamic-toolsets`
> `-e GITHUB_DYNAMIC_TOOLSETS=1`

**Деталь, подтверждающая подлинное чтение:** в v0.2.0 та же фраза содержала опечатку
«the **shear** number of tools available»; к v1.0.0 исправлено на «sheer».

Мета-инструменты — из `pkg/github/dynamic_tools.go` на теге v1.0.0 (файл скачан, 8 071 байт),
дословные описания:

- `enable_toolset` — «Enable one of the sets of tools the GitHub MCP server provides, use
  get_toolset_tools and list_available_toolsets first to see what this will enable»
- `list_available_toolsets` — «List all available toolsets this GitHub MCP server can offer,
  providing the enabled status of each. Use this when a task could be achieved with a GitHub tool and
  the currently available tools aren't enough. Call get_toolset_tools with these toolset names to
  discover specific tools you can call»
- `get_toolset_tools` — «Lists all the capabilities that are enabled with the specified toolset, use
  this to get clarity on whether enabling a toolset would help you to complete a task»

### 4.3. Чем именно удалено — первоисточник

- **PR:** https://github.com/github/github-mcp-server/pull/2512
- **Заголовок:** «refactor: remove dynamic toolsets and deprecated closure constructor»
- **Автор:** SamMorrowDrums · создан 2026-05-20, **merged: true** · 24 файла, +51 / −942

Дословно из описания PR:

> «Removes the dynamic toolset discovery feature (the `--dynamic-toolsets` / `GITHUB_DYNAMIC_TOOLSETS`
> switch and the meta-tools `enable_toolset`, `list_available_toolsets`, `get_toolset_tools`) along
> with the deprecated closure-based `NewServerToolWithDeps` constructor that only existed to support it.
>
> This is **tech debt cleanup**:
>
> - Dynamic mode was local-only — never offered by the remote server.
> - It carried real complexity: a separate config flag plumbed through stdio + http configs, a
>   parallel registration path, four inventory methods […], three meta-tools, and a chunk of
>   conformance/CI matrix.»

**Урок для занятия.** Причина удаления, названная самим автором, — **не** «идея плохая», а
«режим был только локальным и дорого обходился в поддержке». Приписывать GitHub вывод
«динамическая выдача описаний не работает» — подмена: такого утверждения в PR нет.

### 4.4. Что НЕ подтвердилось по этому случаю

Предполагавшаяся формулировка **«avoid filling the context window with unnecessary tools»**
в README **не найдена ни в одной версии** (ни в v0.2.0, ни в v1.0.0, ни в текущей). Реальные
формулировки две, и они разные:
- про динамический режим — «the model gets confused by the sheer number of tools available»
  (про путаницу модели, не про объём контекста);
- про статические наборы — «reduce the context size» (про объём, но это другой флаг).
Цитировать их нельзя вперемешку.

---

## Случай 5. GitHub / Microsoft — VS Code и Copilot — VERIFIED, с числами

### 5.1. Инженерный блог GitHub

- **URL:** https://github.blog/ai-and-ml/github-copilot/how-were-making-github-copilot-smarter-with-fewer-tools/
- **Заголовок:** «How we're making GitHub Copilot smarter with fewer tools»
- **Авторы и дата (со страницы):** «Anisha Agarwal & Connor Peet November 19, 2025 | 7 minutes»
- **Статус: VERIFIED.**

> «In VS Code, GitHub Copilot Chat can access hundreds of tools through the Model Context Protocol
> (MCP) that range from codebase analysis tools to Azure-specific utilities. But giving an agent too
> many tools doesn't always make it smarter. Sometimes it just makes it slower.»

> «To fix that, we've built two new systems—embedding-guided tool routing and adaptive tool
> clustering—and we're rolling out a reduced toolset that trims the default 40 built-in tools down to
> 13 core ones. Across benchmarks like SWE-Lancer and SWEbench-Verified with both GPT-5 and Sonnet
> 4.5, these changes improve success rates by 2-5 percentage points. In online A/B testing, it
> reduces response latency by an average of 400 milliseconds.»

> «In benchmarks, the embedding-based approach achieved 94.5% Tool Use Coverage, outperforming both
> LLM-based selection (87.5%) and the default static tool list (69.0%). Offline, this approach
> resulted in a 27.5% absolute improvement in coverage.»

Почему отказались от кластеризации силами LLM (дословно):

> «Initially we fed all the available tools into an LLM and asked it to group and summarize them. But
> this had two big issues: We couldn't control the number of groups created, and it sometimes exceeded
> model limits. It was extremely slow and incurred a huge token cost.»

**Дефект самого первоисточника, зафиксировать честно.** В блоге аббревиатура TTFT раскрыта
**дважды по-разному** в одном предложении:

> «an average decrease of 190 milliseconds in TTFT (Time To First Token), and an average decrease of
> 400 milliseconds in TTFT (Time to Final Token, or time to complete model response)»

Это ошибка на стороне источника. На слайде либо не использовать эту пару чисел, либо указать
оговорку. Хороший материал для разбора «первоисточник тоже бывает неаккуратен».

### 5.2. Документация VS Code — жёсткий предел 128 инструментов

- **URL:** https://code.visualstudio.com/docs/copilot/agents/agent-tools (прочитано 2026-10-07)
- **Статус: VERIFIED.**

> «I'm getting an error that says "Cannot have more than 128 tools per request." A chat request can
> have a maximum of 128 tools enabled at a time. If you see an error about exceeding 128 tools per
> request: Open the tools picker in the Chat view and deselect some tools or entire MCP servers to
> reduce the count. Alternatively, enable virtual tools with the
> `github.copilot.chat.virtualTools.threshold` setting to automatically manage large tool sets.»

- **URL:** https://code.visualstudio.com/updates/v1_103 — «July 2025 (version 1.103)»,
  в списке ключевых изменений: «Enable more than 128 tools per agent request».

> «Tool grouping (Experimental). Setting: `github.copilot.chat.virtualTools.threshold`. The maximum
> number of tools that you can use for a single chat request is currently 128. Previously, you could
> quickly reach this limit by installing MCP servers with many tools, requiring you to deselect some
> tools in order to proceed. In this release of VS Code, we have enabled an experimental tool-calling
> mode for when the number of tools exceeds the maximum limit. Tools are automatically grouped and the
> model is given the ability to activate and call groups of tools.»

---

## Случай 6. Manus — ОБРАТНЫЙ случай, VERIFIED

Команда **попробовала** загрузку инструментов по требованию и **отказалась** от неё. Это ломает
удобную, но ложную рамку «все пришли к одному решению».

- **URL:** https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
- **Заголовок:** «Context Engineering for AI Agents: Lessons from Building Manus»
- **Автор и дата (со страницы):** Yichao 'Peak' Ji, «2025/7/18»
- **Статус: VERIFIED.**

> «As your agent takes on more capabilities, its action space naturally grows more complex—in plain
> terms, the number of tools explodes. The recent popularity of MCP only adds fuel to the fire. If you
> allow user-configurable tools, trust me: someone will inevitably plug hundreds of mysterious tools
> into your carefully curated action space. As a result, the model is more likely to select the wrong
> action or take an inefficient path. In short, your heavily armed agent gets dumber.»

> «A natural reaction is to design a dynamic action space—perhaps loading tools on demand using
> something RAG-like. We tried that in Manus too. But our experiments suggest a clear rule: unless
> absolutely necessary, avoid dynamically adding or removing tools mid-iteration.»

Две названные причины — дословно:

> «1. In most LLMs, tool definitions live near the front of the context after serialization, typically
> before or after the system prompt. So any change will invalidate the KV-cache for all subsequent
> actions and observations. 2. When previous actions and observations still refer to tools that are no
> longer defined in the current context, the model gets confused. Without constrained decoding, this
> often leads to schema violations or hallucinated actions.»

Что взамен — раздел называется «Mask, Don't Remove»:

> «Rather than removing tools, it masks the token logits during decoding to prevent (or enforce) the
> selection […]»

Число из той же статьи: «In Manus, for example, the average input-to-output token ratio is around 100:1.»

---

## Случай 7. OpenAI, официальная документация — VERIFIED

- **URL:** https://platform.openai.com/docs/guides/function-calling (прочитано 2026-10-07; дата
  публикации не указана — живая документация)
- **Статус: VERIFIED.**

> «Keep the number of initially available functions small for higher accuracy. Evaluate your
> performance with different numbers of functions. Aim for fewer than 20 functions available at the
> start of a turn at any one time, though this is just a soft suggestion. Use tool search to defer
> large or infrequently used parts of your tool surface instead of exposing everything up front.»

> «Token Usage. Under the hood, functions are injected into the system message in a syntax the model
> has been trained on. This means callable function definitions count against the model's context
> limit and are billed as input tokens. If you run into token limits, we suggest limiting the number
> of functions loaded up front, shortening descriptions where possible, or using tool search so
> deferred tools are loaded only when needed.»

> «If your application has many functions or large schemas, you can pair function calling with tool
> search to defer rarely used tools and load them only when the model needs them. Only gpt-5.4 and
> later models support `tool_search`.»

**Жёсткого предела «128 функций» на этой странице НЕ НАЙДЕНО** — см. раздел «Что не подтвердилось».
Подтверждён только мягкий ориентир «fewer than 20».

---

## Случай 8. Спецификация MCP — VERIFIED частично, не переоценивать

- **URL:** https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- **Статус: механизмы существуют (VERIFIED), но это НЕ отложенная выдача описаний.**

> «listChanged indicates whether the server will emit notifications when the list of available tools
> changes.»

> «To discover available tools, clients send a `tools/list` request. This operation supports
> pagination.» — с параметром `"cursor": "optional-cursor-value"`.

**Честная оценка, обязательная к сохранению.** `listChanged` — уведомление о том, что список
изменился; пагинация — разбиение выдачи списка на страницы. **Ни то, ни другое не является
механизмом «отдать описание только когда понадобится»**: клиент по-прежнему способен собрать весь
список и положить его в контекст. Выдавать пагинацию за решение проблемы контекста — именно та
натяжка, которую занятие должно научить ловить.

---

## Числа, пригодные для слайда

Только то, что прочитано на странице первоисточника. Каждое — с указанием, **чьё** оно: смешивать
нельзя.

| Число | Дословная привязка | Чей / где | Статус |
|---|---|---|---|
| **150 000 → 2 000 токенов, экономия 98.7%** | «from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%» | Anthropic, блог, 04.11.2025 | VERIFIED. Только как пример из статьи (Google Drive + Salesforce), не отраслевая норма |
| **~55 000 токенов на 5 серверов; сокращение >85%; остаётся 3–5 инструментов** | «can consume ~55k tokens in definitions before Claude does any work. Tool search typically reduces this by over 85 percent, loading only the 3–5 tools» | Anthropic, документация API | VERIFIED. Набор: GitHub, Slack, Sentry, Grafana, Splunk |
| **Точность выбора падает после 30–50 инструментов** | «degrades once you exceed 30–50 available tools» | Anthropic, документация API | VERIFIED |
| **+50 000 токенов** на промежуточный результат | «For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens» | Anthropic, блог | VERIFIED |
| **128 инструментов — жёсткий предел на запрос** | «Cannot have more than 128 tools per request» | VS Code, документация | VERIFIED |
| **40 → 13 встроенных инструментов** | «trims the default 40 built-in tools down to 13 core ones» | GitHub blog, 19.11.2025 | VERIFIED |
| **+2–5 п.п. успешности** (SWE-Lancer, SWEbench-Verified; GPT-5 и Sonnet 4.5) | «improve success rates by 2-5 percentage points» | GitHub blog | VERIFIED |
| **−400 мс задержки** в онлайн A/B | «reduces response latency by an average of 400 milliseconds» | GitHub blog | VERIFIED |
| **Tool Use Coverage: 94.5% / 87.5% / 69.0%** | эмбеддинги / выбор силами LLM / статический список | GitHub blog | VERIFIED |
| **Ориентир «меньше 20 функций» на начало хода** | «Aim for fewer than 20 functions available at the start of a turn» | OpenAI, документация | VERIFIED, названо «soft suggestion» |
| **Соотношение вход/выход ≈ 100:1** | «the average input-to-output token ratio is around 100:1» | Manus, 18.07.2025 | VERIFIED |

**Числа, которых НЕТ и которые нельзя изобретать:** у Cloudflare — ни одного.
У GitHub MCP Server — ни одного (ни в README, ни в PR об удалении).

---

## Что НЕ подтвердилось

1. **«Крупные компании отказались от MCP».** НЕ ПОДТВЕРЖДЕНО ни одним источником. Anthropic и
   Cloudflare прямо сохраняют MCP-серверы: Cloudflare — «the TypeScript APIs representing its
   connected MCP servers»; Anthropic — «present MCP servers as code APIs». Отказ касается загрузки
   описаний в контекст, не протокола.

2. **Cloudflare объясняет Code Mode переполнением контекста.** НЕ ПОДТВЕРЖДЕНО, опровергнуто
   замером: «context window» — 0 вхождений на странице. Названная причина — обучающее распределение
   («never seen in the wild»), плюс «too many tools… may struggle to choose the right one».

3. **У Cloudflare есть количественные результаты.** НЕ ПОДТВЕРЖДЕНО: ни токенов, ни процентов.
   «The results are striking» без единой величины.

4. **Флаг `--dynamic-toolsets` действует в GitHub MCP Server.** НЕ ПОДТВЕРЖДЕНО для текущей версии:
   удалён из README **и из кода**, PR #2512 (merged 2026-05-20). Подтверждён только для версий
   до v1.0.0 включительно.

5. **Формулировка «avoid filling the context window with unnecessary tools» в README GitHub MCP
   Server.** НЕ ПОДТВЕРЖДЕНО: не найдена ни в одной проверенной версии. Реальные формулировки —
   «the model gets confused by the sheer number of tools available» (динамический режим) и
   «reduce the context size» (статические наборы).

6. **GitHub удалил динамические наборы, потому что подход не работает.** НЕ ПОДТВЕРЖДЕНО: в PR
   названы «tech debt cleanup», «local-only — never offered by the remote server» и сложность
   поддержки. Вывода о неработоспособности в первоисточнике нет.

7. **Жёсткий предел 128 функций у OpenAI.** НЕ НАЙДЕНО на странице function-calling. Подтверждён
   только мягкий ориентир «fewer than 20». Предел 128 подтверждён у **VS Code**, не у OpenAI.

8. **`listChanged` / пагинация в спецификации MCP как средство отложенной выдачи описаний.**
   Механизмы существуют, но такой функции НЕ выполняют — см. случай 8.

9. **Block / Goose.** НЕ ПРОВЕРЕНО: https://block.github.io/goose/docs/getting-started/using-extensions/
   вернул пустой ответ (86 байт). Рабочего первоисточника не найдено. Не использовать.

10. **Shopify, Stripe, Vercel, Sourcegraph / Amp.** НЕ ПОДТВЕРЖДЕНО: публичных заявлений этих команд
    по теме на первоисточниках в этом проходе не найдено. Не упоминать как примеры.

11. **Документированный предел числа определений инструментов у Google.** НЕ ПРОВЕРЕНО в этом
    проходе. Не утверждать ни в одну сторону.

---

## Точные написания флагов, переменных и идентификаторов (для артефакта слайда)

Проверено посимвольно на первоисточнике. Регистр и подчёркивания значимы.

**GitHub MCP Server — действует сейчас (main, 2026-10-07):**
- `--toolsets` · переменная `GITHUB_TOOLSETS`
- `--tools` · переменная `GITHUB_TOOLS`
- Переменная окружения имеет приоритет над аргументом: «The environment variable `GITHUB_TOOLSETS`
  takes precedence over the command line argument if both are provided.»

**GitHub MCP Server — удалено (было до v1.0.0 включительно, нет в v1.1.0+):**
- `--dynamic-toolsets` · переменная `GITHUB_DYNAMIC_TOOLSETS=1`
- мета-инструменты: `enable_toolset` · `list_available_toolsets` · `get_toolset_tools`

**Anthropic API (tool search):**
- поле определения инструмента: `defer_loading: true`
- инструменты поиска: `tool_search_tool_regex_20251119` · `tool_search_tool_bm25_20251119`
- блоки результата: `tool_reference` · `tool_search_tool_result`

**OpenAI:**
- `tool_search` («Only gpt-5.4 and later models support `tool_search`»)

**VS Code / Copilot:**
- настройка: `github.copilot.chat.virtualTools.threshold`
- текст ошибки дословно: `Cannot have more than 128 tools per request.`

**Спецификация MCP:**
- возможность сервера: `listChanged` (внутри `capabilities.tools`)
- метод: `tools/list` · параметр пагинации: `cursor`

---

## Методическая заметка: расхождения между проходами

Задание предупреждало о самопротиворечивости веб-выборки. Зафиксировано по факту:

- **Содержательных расхождений между проходами не возникло** ни по одному числу: все ключевые
  величины (150 000 / 2 000 / 98.7% / ~55k / 85% / 128 / 40 → 13 / 94.5%) подтверждены дословным
  поиском подстроки по скачанному тексту страницы, а не пересказом.
- **Одно ложное расхождение разобрано и снято.** Поиск подстроки «50,000» в статье Anthropic выдавал
  две разные находки, одна из которых выглядела как «50,000 tokens to 2,000 tokens» — то есть как
  конкурирующее число к 150 000. При извлечении абзаца целиком выяснилось, что это **совпадение
  внутри строки «150,000»**, а «50,000 tokens» отдельно относится к другому утверждению (двухчасовая
  встреча). Урок для занятия: поиск подстроки без чтения окружающего абзаца порождает
  несуществующие противоречия.
- **Один раз сводка модели разошлась с текстом страницы.** Первый проход (WebFetch) по README
  GitHub MCP Server сообщил, что динамического обнаружения инструментов в документации нет, —
  и это оказалось **верно для текущей версии**, но из такой сводки невозможно было узнать, что
  механизм существовал и был удалён. Историю дало только чтение README по тегам и PR. Вывод:
  ответ «такого нет» требует отдельной проверки «а было ли».

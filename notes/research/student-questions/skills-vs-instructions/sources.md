# Skills vs Instructions — Sources (механика)

**Date:** 2026-10-02 · **Access date:** 2026-10-02 · **Issue:** #217
**Researcher:** research-субагент (механика/стоимость контекста)

Confidence: H=высокая (первоисточник вендора) · M=средняя (вторичный блог/агрегатор с явной ссылкой на первоисточник) · L=низкая (блог/форум без проверки)
Freshness: **W**=недельная волатильность (номера версий, пороги) · Y=стабильно

Все URL открыты лично в этой сессии через WebFetch/WebSearch 2026-10-02.

| # | URL | Издание | Дата доступа | Тип | Fresh | Conf | Используется для |
|---|---|---|---|---|---|---|---|
| 1 | https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview | Anthropic (Claude Platform Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Agent Skills: структура SKILL.md, 3 уровня progressive disclosure, таблица token cost, required fields name/description, где Skills работают (API/claude.ai/AWS/Foundry), security |
| 2 | https://code.claude.com/docs/en/skills | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Claude Code: создание Skills, слияние slash-команд со skills, `/skill-doctor`, `disable-model-invocation`, пути хранения, лимиты токенов (1%, 5000/25000, 1536 симв.) |
| 3 | https://code.claude.com/docs/en/memory | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | CLAUDE.md: иерархия (managed/user/project/local), `@path`-импорты (глубина 4), рекомендация <200 строк, порядок конкатенации, AGENTS.md: нативная поддержка, таблица приоритетов, hooks InstructionsLoaded |
| 4 | https://code.claude.com/docs/en/hooks | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Полный список hook-событий, exit-коды (0/2), JSON permissionDecision, что из stdout/stderr попадает в контекст модели, места конфигурации |
| 5 | https://code.claude.com/docs/en/slash-commands | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Slash-команды: расположение, явный человеческий триггер, `$ARGUMENTS`/`$0`/`$1`, нулевая стоимость контекста до вызова, слияние с Skills |
| 6 | https://code.claude.com/docs/en/features-overview | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Сводная таблица «Context cost by feature», попарные сравнения (Skill vs Subagent, CLAUDE.md vs Skill, Hook vs Skill, MCP vs Skill), «Build your setup over time» |
| 7 | https://code.claude.com/docs/en/sub-agents | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Субагенты: YAML-фронтматтер, что грузится при старте (fresh vs fork), лимит описаний 15 000 токенов, сравнение с Skills |
| 8 | https://code.claude.com/docs/en/agent-sdk/tool-search | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Tool search / deferred tools: пороги (10%/30-50 инструментов), режимы auto/auto:N/true/false, лимиты (10 000 инструментов, топ-5 результатов) |
| 9 | https://code.claude.com/docs/en/how-claude-code-works | Anthropic (Claude Code Docs) | 2026-10-02 | Документация вендора (первоисточник) | **W** | H | Агентный цикл: вызов инструмента — решение модели, а не харнесса; context window overview |
| 10 | https://agents.md/ | agents.md (OpenAI/Google/Cursor/Factory/Sourcegraph консорциум) | 2026-10-02 | Документация вендора/консорциума (первоисточник стандарта) | **W** | H | Кто создал AGENTS.md, список поддерживающих инструментов (20+), freeform-markdown без обязательных полей, Linux Foundation / AAIF |
| 11 | https://www.infoq.com/ (поиск, не открыт напрямую — цитата через агрегированный WebSearch) | InfoQ | 2026-10-02 | Вторичный источник (новость) | Y | M | Дата формализации AGENTS.md (авг. 2025), донейшн в Linux Foundation (дек. 2025) — корроборация |
| 12 | https://github.com/anthropics/claude-code/issues/27208 | GitHub Issues (anthropics/claude-code) | 2026-10-02 | Народная практика / отчёт сообщества | **W** | M | Предложение иерархического deferred tool discovery для очень больших MCP-серверов (не входит в текущую документацию — помечено как нереализованное) |
| 13 | https://github.com/anthropics/claude-code/issues/31002 | GitHub Issues (anthropics/claude-code) | 2026-10-02 | Народная практика / отчёт сообщества | **W** | L | Отчёт о недокументированном переводе встроенных системных инструментов за ToolSearch — иллюстрирует, что механизм деплоится быстрее, чем документируется |
| 14 | https://medium.com/@joe.njenga/claude-code-merges-slash-commands-into-skills-dont-miss-your-update-8296f3989697 | Medium (Joe Njenga) | 2026-10-02 | Вторичный блог (корроборация вендорской доки) | **W** | M | Независимое подтверждение факта слияния slash-команд и Skills, совпадает текстуально с источником #2 |
| 15 | https://tessl.io/blog/anthropic-brings-mcp-tool-search-to-claude-code | Tessl blog | 2026-10-02 | Вторичный блог (корроборация) | **W** | M | Корроборация механизма tool search / ~500 токенов на сам Tool Search Tool |

**Важное предупреждение о волатильности:** номера версий Claude Code (v2.1.206, v2.1.211, v2.1.213, v2.1.217, v2.1.221, v2.1.227, v2.1.252, v2.1.277, v2.1.280, v2.1.281, v2.1.283), пороги (1%, 5%, 10%, 25 000 токенов, 15 000 токенов, 1536 символов) и само существование `/skill-doctor` и «slash-команды слиты со skills» — всё это задокументированное, но **очень недавнее и быстро меняющееся** поведение продукта. Помечено `[VFY-day-of]` везде в основном файле.

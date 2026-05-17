# Lecture 4 — AI в разработке ПО — Tools Landscape 2026

**Date:** 2026-05-16 · **Researcher:** fact-checker research subagent · **Issue:** #99

> Adoption-данные, не маркетинг. Freshness: market-share **quarterly**; feature-наборы **monthly**; leaderboard-числа **weekly [VERIFY ON DAY OF LECTURE]**.
> Главный первоисточник adoption: **JetBrains Research, «Which AI Coding Tools Do Developers Actually Use at Work?», 2026-04, n>10 000 проф-разработчиков, baseline сент 2025**; кросс-проверка — Pragmatic Engineer «AI Tooling for Software Engineers in 2026».

---

## 1. Рынок (контекст)

- AI coding assistant market: **$12.8B (2026)** → прогноз $30.1B (2032), CAGR ~27%, YoY-рост ~65% (2025-26). Источник: ideaplan.io/blog (2026). **Confidence: MEDIUM (market-research, vendor-aggregated, quarterly).**
- Общий AI-tool usage среди разработчиков: **90%** регулярно используют ≥1 AI-инструмент (JetBrains 2026-04; согласуется с DORA 90% и SO 84% used/plan).
- Паттерн **tool-stacking**: 2–4 инструмента одновременно; доминирующая связка — **Cursor (редактирование) + Claude Code (сложные задачи)**. Источник: thenewstack.io/ai-coding-tool-stack; pragmaticengineer (2026).

---

## 2. Adoption по инструментам (JetBrains, янв 2026, n>10k; work-adoption / awareness)

| Инструмент | Work adoption | Awareness | Тренд | Деталь |
|---|---|---|---|---|
| **GitHub Copilot** | **29%** | **76%** | ⚠️ **Stalled** (рост awareness И adoption застопорился YoY) | Всё ещё #1 по охвату, но не растёт |
| **Cursor** | **18%** | 69% | ↗ растёт, но **замедлился** | $2B ARR, >1M платящих, +35% за 9 мес; highest-revenue category-native |
| **Claude Code** | **18%** | 57% | 🚀 **быстрый рост** | ~3% (апр–июнь 2025) → 18% (янв 2026) = **6×**; US/Canada 24%; CSAT **91%**, NPS **54** (highest loyalty) |
| **ChatGPT** (chatbot для кода) | 28% | — | популярен | универсальный, не IDE-native |
| **JetBrains AI Assistant** | 9% | — | ↗ растёт | + **Junie 5%** (11% combined awareness) |
| **Gemini** (chatbot) | 8% | — | — | |
| **Claude** (chatbot) | 7% | — | — | |
| **Google Antigravity** | 6% | — | 🆕 новый вход | агентный IDE |
| **OpenAI Codex** | 3% | 27% | ↘ nascent/declining (в этой выборке) | по другим данным используется как агент-CLI |

---

## 3. Что РАСТЁТ (востребованные, с датами)

1. **Claude Code** — самый быстрорастущий: 3%→18% за ~9 мес (6×), #1 по loyalty (CSAT 91%/NPS 54). [JetBrains 2026-04; Pragmatic 2026] **[quarterly]**
2. **Cursor** — лидер по выручке ($2B ARR, >1M платящих), +35%/9 мес. [JetBrains; getpanto.ai cursor-stats 2026]
3. **Spec-driven IDE / агентные среды** — AWS Kiro (mid-2025), Google Antigravity (новый, 6%), GitHub Spec Kit, BMAD, Tessl. [infoworld.com 2026]
4. **AGENTS.md-экосистема** — 20k→40k+ репо (авг–дек 2025), де-факто стандарт. [infoq.com 2025-08]
5. **AI code-review** (Greptile/CodeRabbit/Bugbot) и **AI-SAST** (Semgrep Assistant, Snyk Agent Fix, Veracode Fix, Copilot Autofix, Corgea) — растущий сегмент. [greptile.com; corgea.com 2025-26]
6. **JetBrains AI Assistant + Junie** — растут в JetBrains-экосистеме (9%/5%).
7. **Legacy-migration агенты** — AWS Transform (GA май 2025), Morgan Stanley DevGen.AI. [aws.amazon.com 2025]

## 4. Что СТАГНИРУЕТ / УХОДИТ (с датами + честная оговорка)

1. **GitHub Copilot — стагнация (не смерть).** Остаётся #1 по охвату (29%/76%), но **рост awareness и adoption застопорился YoY** (JetBrains 2026-04: «its growth … has stalled since last year»; Pragmatic Engineer 2026). Формулировка для лекции: «не уходит, но **теряет лидерство по динамике** — обгоняется Claude Code/Cursor по росту». **[quarterly]**
2. **OpenAI Codex** — в JetBrains-выборке всего 3% work / 27% awareness, помечен «declining/nascent». ОГОВОРКА: в других контекстах Codex живёт как CLI-агент — НЕ утверждать «умер», говорить «низкая и невыросшая доля в проф-выборке JetBrains».
3. **Tabnine, Codeium/Windsurf, Amazon CodeWhisperer** — **выпали из топ-данных** свежих 2026-выборок (JetBrains/Pragmatic их не раскрывают; в arXiv:2510.26103 CodeWhisperer/Tabnine — 0.52%/0.46% объёма анализа). **Честная оговорка: точных decline-чисел НЕТ → говорить «маргинализированы / не фигурируют в свежих топ-данных», НЕ "мертвы".** Это важно для fact-checker downstream — не overclaim.

## 5. Явный ответ «что уходит из инструментов»

- **Уходит как доминанта по динамике:** GitHub Copilot (стагнация роста — но всё ещё крупнейший по охвату; точная формулировка обязательна, иначе P0-misstatement).
- **Маргинализированы (не подтверждено как «умерли»):** Tabnine, Codeium/Windsurf, CodeWhisperer, standalone-Codex — не в топ свежих adoption-данных. Помечать MEDIUM/LOW confidence, не утверждать смерть.
- **Уходит как практика:** «freeform vibe coding без тестов/спеки/гейтов» — источник большинства failure-кейсов (curl-slop, Lovable, Replit). Не инструмент, но паттерн, который индустрия отвергает.

---

## 6. Confidence-сводка

| Утверждение | Confidence | Freshness |
|---|---|---|
| Claude Code 3%→18% (6×), CSAT 91% | HIGH (JetBrains n>10k primary) | quarterly |
| Copilot 29%/76%, рост stalled | HIGH (JetBrains) | quarterly |
| Cursor $2B ARR / >1M платящих | MEDIUM (vendor/press) | quarterly |
| Market $12.8B/2026 | MEDIUM (market-research) | quarterly |
| AGENTS.md 20k→40k репо | HIGH (infoq + agents.md) | monthly |
| Tabnine/Codeium «уходят» | LOW (отсутствие данных ≠ decline) | — НЕ overclaim |
| Любой leaderboard (SWE-bench) | weekly **[VERIFY ON DAY]** | weekly |

---

# 2026-05-17 update: тулы по уровням автономности A/B/C/D

**Researcher:** lecture-4 research subagent · **Issue:** #99 · WebSearch verify 2026-05-17.
**Цель раздела:** смаппить ландшафт строго на канон-лестницу лекции (A — автодополнение, B — мелкие задачи в чате/inline, C — кодинг-агент, D — оркестратор+трекер). Числа из §2 подтверждены свежей выборкой (JetBrains «Which AI Coding Tools…», янв 2026, n>10k — перепроверено 2026-05-17, без изменений). SO 2025 (опубл. дек 2025): 84% use/plan, 51% проф. ежедневно, доверие 29% (↓11 п.п. YoY), 66% — «почти верно, но не совсем». DORA 2025: 90% используют AI, медиана 2 ч/день.

## Что подтвердилось / изменилось с 2026-05-16 версии

- **Подтвердилось (без изменений):** Copilot 29%/76% adoption/awareness, рост stalled; Cursor 18%, рост замедлился; Claude Code 18% (US/Canada 24%), CSAT 91%/NPS 54, 6× за ~9 мес; ChatGPT-чат 28%; JetBrains AI Assistant 9% + Junie 5%; Antigravity 6%; Codex 3%/27%.
- **Новое (2026-05-17):** Copilot — **4.7M платных подписчиков, +75% YoY** (volume-лидер) [ideaplan.io 2026]. Claude Code **«most-loved» 46%** vs Cursor 19% vs Copilot 9% [JetBrains 2026-04]. Сегментный сплит: **стартапы → Claude Code ~75%**, **энтерпрайз 10k+ → Copilot ~56%** [ideaplan.io 2026]. Multi-agent волна **февр 2026**: Grok Build (8 паралл. агентов), Windsurf (5), Claude Code Agent Teams, Codex CLI + Agents SDK [theplanettools.ai 2026]. GitHub Copilot coding agent **GA** (issue→draft PR через GitHub Actions); масштаб «17M PRs, 5 outages, kill switch» — anti-hype-якорь [danilchenko.dev 2026-04, github.blog].
- **Не изменилось по «уходящим»:** Tabnine / Codeium / Windsurf / CodeWhisperer по-прежнему НЕ в топ-данных свежих выборок → формулировка «маргинализированы / не фигурируют», НЕ «мертвы» (LOW confidence, не overclaim).

## Таблица: уровень → доминирующие тулы 2026

> Колонка «Диапазон» = реальный спан режимов одного продукта. «Первично» = режим, по которому тул якорится на лекции. Adoption — work-adoption (JetBrains янв 2026) если не указано иное; volatile → `[VFY-day-of]`.

### Уровень A — автодополнение (inline / tab; человек фильтрует каждый токен)

| Тул | Вендор | Первично / Диапазон | Adoption-сигнал 2026 | Растёт/уходит | Anti-hype-оговорка |
|---|---|---|---|---|---|
| **GitHub Copilot** (inline/ghost-text) | GitHub/Microsoft | A / A→C (есть chat + coding agent) | 29% work, 76% aware, 4.7M платных `[VFY-day-of]` | Volume-#1, но **рост stalled YoY** | «#1» = охват, НЕ динамика; обгоняется по росту |
| **Cursor Tab** (autocomplete) | Anysphere | A / A→C (Tab→Chat→Composer) | 18% work, индексирует весь проект | ↗ замедлился | Tab-completion ≠ «агент»; сильнее Copilot по multi-line, но это всё ещё уровень A |
| **JetBrains full-line completion / AI Assistant** | JetBrains | A / A→B | AI Assistant 9% work | ↗ в JB-экосистеме | Локальная line-completion ≠ агент |

Якорь лекции для A — **класс Copilot inline/tab-completion** (корректно: это режим, не продукт; Cursor Tab — тот же уровень).

### Уровень B — мелкие задачи в чате/inline (функция/фикс по запросу; человек ставит задачу и ревьюит)

| Тул | Вендор | Первично / Диапазон | Adoption-сигнал 2026 | Растёт/уходит | Anti-hype-оговорка |
|---|---|---|---|---|---|
| **ChatGPT** (чат для кода) | OpenAI | B / B (не IDE-native) | **28% work** — самый массовый чат-для-кода | стабильно высокий | Универсальный чат, не агент; copy-paste-петля |
| **Copilot Chat / inline-chat** | GitHub | B / A→C | в составе Copilot 29% | с Copilot | «Edit/Ask» режим — B, не путать с coding agent |
| **Cursor Chat / Cmd-K** | Anysphere | B / A→C | в составе Cursor 18% | с Cursor | inline-edit ≠ многофайловый агент |
| **Claude / Gemini чат** | Anthropic / Google | B / B | Claude-чат 7%, Gemini-чат 8% | — | чат-режим; Claude Code (C) — отдельный продукт |

Якорь B — **ChatGPT-as-coding-chat** (массовость) + **Copilot/Cursor inline-chat** (IDE-native B).

### Уровень C — кодинг-агент (многофайловая задача, сам гоняет тесты, plan→act→check→iterate)

| Тул | Вендор | Первично / Диапазон | Adoption-сигнал 2026 | Растёт/уходит | Anti-hype-оговорка |
|---|---|---|---|---|---|
| **Claude Code** | Anthropic | C / C→D (Agent Teams) | 18% work (24% US/CA), CSAT 91%, NPS 54, «most-loved» 46% `[VFY-day-of]` | 🚀 **самый быстрый рост** (6× / ~9 мес) | SWE-bench 80.9% — `[VFY-day-of]`, leaderboard волатилен weekly; benchmark ≠ прод |
| **Cursor (Composer / Agent Mode)** | Anysphere | C / A→C | 18% work, $2B ARR, >1M платящих `[VFY-day-of]` | ↗ замедлился | «most autonomous mode» — vendor-формулировка; всё равно нужен human-review |
| **Codex (CLI / Cloud)** | OpenAI | C / C→D (async, Agents SDK) | 3% work / 27% aware в JB-выборке | низкая доля в проф-выборке (НЕ «умер» — живёт как CLI-агент) | async-агент ≠ автономия; узкие well-scoped задачи |
| **Windsurf (Cascade)** | Cognition | C / B→C | НЕ в топ JB-данных → маргинализирован (LOW) | данных нет — не overclaim | Cascade-демо ≠ массовый прод-adoption |

Якорь C — **Claude Code** (рост+loyalty) + **Cursor Composer** (revenue+охват). Codex — пример «низкая доля в одной выборке ≠ смерть» (честная оговорка для fact-checker).

### Уровень D — оркестратор + трекер (issue→PR; человек = стратегия/approval/merge; multi-agent)

| Тул | Вендор | Первично / Диапазон | Adoption-сигнал 2026 | Растёт/уходит | Anti-hype-оговорка |
|---|---|---|---|---|---|
| **GitHub Copilot coding agent** | GitHub | D / C→D | **GA 2026**; issue→draft PR via Actions; «17M PRs» масштаб `[VFY-day-of]` | ↗ растёт (но 5 outages + kill switch — задокументировано) | «assign issue → PR» — реальность с гейтами, НЕ автономный инженер; качество PR требует ревью |
| **Devin (2.0, Interactive Planning)** | Cognition | D / C→D | press/vendor, $500/мес `[VFY-day-of]` | присутствует, но cost-per-PR «rough» | **Главный anti-hype-кейс:** «fully autonomous engineer» = vendor-claim; frontier-модели + scaffolding обгоняют исходные Devin-скор; consistency varies |
| **Google Jules** | Google | D / C→D | вышел из public beta, GA; GitHub-интеграция, GCP VM | ↗ растёт | plan→self-review демо ≠ guarantee; async ≠ без надзора |
| **OpenAI Codex Cloud (async)** | OpenAI | D / C→D | 3% work (как Codex) | ниша | overnight-PR — батч-сценарий, не дефолт |

Якорь D — **GitHub Copilot coding agent** (GA + трекер-интеграция, реальные числа+инциденты) + **Devin** (как anti-hype-эталон «overclaimed автономии»). Multi-agent (Claude Code Agent Teams, Grok Build 8×, Windsurf 5×) — верхняя кромка D, февр 2026, **emerging — не mainstream**.

## Граничные случаи (как атрибутировать, не упрощая лживо)

1. **Один продукт = несколько уровней.** Copilot = A (ghost-text) + B (chat) + C (Copilot agent mode) + D (coding agent GA). Cursor = A (Tab) + B (Cmd-K) + C (Composer). Claude Code = C (дефолт) + D (Agent Teams). **Правило лекции:** маппить **РЕЖИМ, не бренд**. На слайде показывать «Copilot» в 3-4 клетках — корректно и педагогически честнее, чем «Copilot = уровень A».
2. **C↔D размыта.** Codex / Jules / Cursor background = «C, запущенный async из трекера» ≈ D. Критерий разделения для лекции: **источник задачи** (человек в IDE → C; тикет из трекера + PR-выход → D), а не «насколько умный».
3. **B↔C размыта.** Inline-chat, который «сам тронул 3 файла», — пограничье. Критерий: **гоняет ли тесты и итерирует сам** (да → C; нет, один проход → B).
4. **Чат-LLM (ChatGPT/Claude/Gemini) — строго B**, даже если «может агентно»: в проф-практике используется как copy-paste-чат (SO: 81% юзают OpenAI-чат-модели). Не повышать до C без агент-обвязки.

## Анти-хайп факты (vendor-claim слабо подтверждён) — для AI-Failure правила

- **Devin «fully autonomous software engineer»** — самый растиражированный overclaim. Реальность: frontier-модели со scaffolding обогнали исходные Devin SWE-bench-скор; consistency varies; $500/мес → cost-per-успешный-PR «rough» если не батчить overnight [stepchange-blog 2026, theplanettools.ai 2026]. **`[VFY-day-of]`** для любых текущих скор.
- **SWE-bench как «доказательство автономии»** — методологически дырявый: ~10% issue содержат полное решение в тексте, 4.3% — gold-patch в описании, ~28.4% «прошедших» патчей некорректны под расширенными тестами [arxiv 2506.17208; cognition.ai]. Лекция: leaderboard-число ≠ прод-готовность, **weekly-волатильно `[VFY-day-of]`**.
- **«AI = +50% скорость»** vs замер: реалистично net cycle-time **+8–13%**, не 50% [stepchange-blog 2026]. Маркетинг-инфляция.
- **DORA 2025 контр-сигнал:** при росте adoption — **+91% время ревью, +154% размер PR, рост delivery-instability**; «AI усиливает, а не чинит» слабые команды [DORA 2025, infoq 2026-03]. Прямой AI-Failure-материал: агентность без гейтов = усиление дисфункции.
- **Agentic AI на Peak of Inflated Expectations** (Gartner 2026): только ~17% организаций развернули агентов; «fully autonomous» не готов для большинства энтерпрайз-кейсов [gartner.com 2026].
- **GitHub Copilot agent инциденты:** 5 outages + kill switch при масштабе 17M PRs [danilchenko.dev 2026-04] — D-уровень в проде ≠ «set and forget».
- **Trust gap (SO 2025):** 84% используют, но доверие 29% (↓11 п.п.), 66% жалуются на «почти верно, но не совсем» → debugging-налог. Adoption ≠ доверие.

## Инфраструктура ≠ уровень-тул (отделять на лекции)

Это НЕ ступени лестницы автономности — это **обвязка**, которая делает A/B/C/D безопасными. Путать с per-level тулами нельзя.

| Категория | Примеры 2026 | Роль | Сигнал |
|---|---|---|---|
| **Контекст-стандарт** | `AGENTS.md`, `CLAUDE.md`, `REVIEW.md` | Кормит агент проектными конвенциями; де-факто стандарт | AGENTS.md 20k→40k+ репо (авг–дек 2025); CodeRabbit/Claude авто-читают CLAUDE.md `[VFY-day-of]` |
| **AI code-review** | CodeRabbit, Greptile, Cursor Bugbot, Macroscope, Claude Code Review, Qodo | Гейт на PR, не «пишет фичу» | Bug-detect bench: Macroscope 48% / CodeRabbit 46% / Bugbot 42% / Greptile 24% `[VFY-day-of]` |
| **AI-SAST / security-fix** | Semgrep Assistant, Snyk Agent Fix, Veracode Fix, Copilot Autofix, Corgea, SonarQube | Скан + autofix уязвимостей; quality-gate в CI | растущий сегмент 2025-26 |
| **CI/CD quality-gates** | Snyk/SonarQube блок-мерж по порогам, 40+ линтеров в CodeRabbit | Жёсткий гейт перед merge | «2026 = год AI-quality/governance» |
| **Legacy-migration агенты** | AWS Transform (GA май 2025), Morgan Stanley DevGen.AI | Узкий вертикальный агент (миграция), не general coding | enterprise-ниша |

**Формулировка для лекции:** лестница A→D = *кто пишет код и с какой автономией*. Инфраструктура = *что не даёт автономии навредить* (gate/scan/context). На слайде §4 s27 их разносить в разные блоки, иначе студент решит, что «CodeRabbit — это уровень выше Copilot». Это разные оси.

## Источники с датами (для `[VFY-day-of]`)

| Источник | Дата | Используется для | Freshness |
|---|---|---|---|
| JetBrains «Which AI Coding Tools Do Developers Actually Use at Work?» (n>10k проф.) | опубл. 2026-04, baseline янв 2026 | adoption/awareness/CSAT/most-loved по всем тулам | quarterly |
| JetBrains State of Developer Ecosystem 2025 (n=24 534, опрос апр–июнь 2025) | опубл. 2025-10 | 85% regular, 44% integrated, use-cases | annual |
| Stack Overflow Developer Survey 2025 | опубл. 2025-12 | 84% use/plan, 51% daily, trust 29%, «почти верно» 66%, OpenAI-чат 81% | annual |
| DORA «State of AI-assisted Software Dev 2025» | опубл. 2025-12 / InfoQ 2026-03 | 90% adoption, 2ч/день, +91% review, +154% PR, instability | annual |
| ideaplan.io «AI Coding Assistant Market Share 2026» | 2026 | $12.8B рынок, Copilot 4.7M/+75%, сегмент-сплит | quarterly (market-research, MEDIUM) |
| theplanettools.ai «AI Coding Agents 2026: We Tested 6» | 2026 | multi-agent волна февр 2026, тест-реальность | monthly |
| danilchenko.dev «GitHub's AI Agent Problem» | 2026-04 | Copilot agent: 17M PRs, 5 outages, kill switch | event-dated |
| github.blog / community#159068 | 2026 | Copilot coding agent GA, issue→draft PR via Actions | event-dated |
| stepchange-blog.ghost.io «How Do AI SWEs Compare to Humans» | 2026 | Devin consistency/cost, net +8–13% vs +50% | quarterly |
| arxiv 2506.17208 + cognition.ai SWE-bench tech report | 2025-26 | SWE-bench методологические дыры (~28.4% error) | stable |
| gartner.com «Hype Cycle for Agentic AI» | 2026 | ~17% deployed, Peak of Inflated Expectations | annual |
| coderabbit / findskill.ai / dev.to code-review state | 2026-04/05 | bug-detect bench, CLAUDE.md auto-read, quality-gate | monthly |

**Правило волатильности:** любое конкретное число adoption/ARR/benchmark/подписчиков на слайде → пометить `[VFY-day-of]`, в речи давать **направление** («Claude Code — самый быстрый рост», «Copilot — крупнейший по охвату, но рост встал»), не зачитывать цифру как вечную. Leaderboard (SWE-bench) — **weekly**, остальное — quarterly.

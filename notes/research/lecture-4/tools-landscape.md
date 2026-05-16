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

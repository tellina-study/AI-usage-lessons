# Lecture 4 — AI в разработке ПО — Trends 2026

**Date:** 2026-05-16
**Researcher:** fact-checker research subagent (deep-research pass, issue #99)
**Lecture date assumed:** ~2026-05/06 (verify; freshness deltas computed vs 2026-05-16)
**Audience:** студенты-инженеры 3 курса (универсальная инженерная аудитория)
**Prereqs:** Л1 (типы AI), Л2 (внутренности LLM), Л3 (агенты/RAG/API, «когда не ИИ», лестница сложности)
**LO:** LO1 + LO4 + LO7

> **Конвенция freshness:** каждый AI-benchmark/leaderboard факт — `[VERIFY ON DAY OF LECTURE]` (weekly cadence). Market-share — quarterly. Tool feature lists — monthly. Концептуальные/исследовательские выводы — yearly+ (стабильны).

---

## Вопрос 1 — Прогрессия автономности (автодоп → мелкие задачи → агент → оркестратор+трекер)

Подробная лестница — в `progression-and-configs.md`. Тезисы по эффективности/надёжности:

- **(а) Автодополнение (Copilot-класс, tab-completion).** Самый зрелый уровень. Контролируемый лабораторный RCT GitHub: разработчики с Copilot закончили изолированную JS-задачу **на 55% быстрее** (1ч11м vs 2ч41м), 95% CI ускорения [21%, 89%], p=.0017; completion rate 78% vs 70%. Полевые эксперименты Microsoft/Accenture (n=1974): **+12.9–21.8% PR/неделю** (Microsoft), **+7.5–8.7%** (Accenture). Источник: GitHub Research / arXiv:2302.06590 (2023-02), полевой — MIT GenAI pub. **Caveat:** изолированная новая задача ≠ работа в большом легаси-проекте (см. METR ниже). [yearly+ для самого вывода; конкретные числа — старые, помечать как «лабораторные, 2022–2023»]
- **(б) Мелкие задачи через чат/inline.** Здесь начинается «70%/80%-проблема» (Addy Osmani, Google Chrome DX, 2024-12, обновлено 2025): AI доводит до ~70% (для ряда задач до 80% к концу 2025), но **последние 30% — edge-cases, безопасность, production-интеграция — остаются такими же трудными**, требуют senior-надзора. Источник: addyo.substack.com «The 70% problem» (2024-12) + «The 80% Problem in Agentic Coding» (2025) + zed.dev repost. [yearly+ — концептуально стабильно]
- **(в) Кодинг-агент с крупными задачами (Claude Code / Codex-класс).** Резкий рост возможностей по SWE-bench, но **надёжность нелинейна** и резко падает на незнакомых/приватных кодовых базах. SWE-bench Verified (май 2026): GPT-5.5 88.7% (рел. 2026-04-23), Claude Opus 4.7 87.6%, GPT-5.3-Codex 85.0%. Контраст: **SWE-bench Pro** (приватные кодбазы, контаминация-резистентный) — лидер Claude Opus 4.7 **64.3%** (Anthropic-reported, апрель 2026) — т.е. на «честном» бенче ~64%, не ~88%. Источник: swebench.com, Scale SWE-Bench Pro, marc0.dev/leaderboard. **[VERIFY ON DAY OF LECTURE — weekly cadence; за 2 дня в Л1 ARC-AGI устарел на 30+ пп]**
- **(г) Оркестратор + работа с трекером (issue→PR автономно).** Самый рискованный уровень. METR RCT (опытные OSS-разработчики, свои репо 22k+ звёзд): при разрешённом AI задачи занимали **на 19% ДОЛЬШЕ** (slowdown), хотя разработчики прогнозировали −24% и пост-факт верили в −20% ускорение (perception gap). n=16 разработчиков, 246 задач, Cursor Pro + Claude 3.5/3.7. Источник: metr.org (2025-07-10), arXiv:2507.09089. **Update (metr.org 2026-02-24):** на late-2025 инструментах сигнал развернулся (−18% / −4% «ускорение»), НО METR называет данные «unreliable signal» из-за selection bias (разработчики отказывались работать без AI). Вывод для лекции: на крупных автономных задачах эффект **не доказан как ускорение**, человек обязателен на review/merge. [исследование — yearly+; но METR-update показывает, как быстро меняется — упомянуть оба]

**Где человек обязателен:** approval перед деструктивными/prod-операциями, merge-решение, выбор «что строить» (essential complexity, Brooks), security-review, последние 30%.

---

## Вопрос 2 — Не только «чистая» разработка

### Тестирование
- **Meta TestGen-LLM** (mutation-guided LLM test gen, ACM FSE 2025, arXiv:2501.12862): улучшает существующие human-тесты. Но контраст: TestGen-LLM покрывает больше классов (32% vs 5.3% у mutation-targeted), но **убивает меньше мутантов (2.4% vs 15%)** — т.е. больше тестов ≠ лучшее обнаружение дефектов. Урок: coverage — слабый индикатор, mutation score честнее (примеры с 100% coverage / 4% mutation score). Источник: arXiv:2506.02954, arXiv:2501.12862. [yearly+]
- Diffblue Cover (bytecode-анализ, не LLM-inference) — наиболее «технически корректные» JUnit-тесты на 2025-2026. AdverTest: +8.56% fault detection над лучшим LLM-методом HITS, +63.3% над EvoSuite. Источник: diffblue.com, arXiv:2602.08146. [monthly для product]
- Flaky-тесты: AI-генерация может усиливать недетерминизм; рекомендация — отдельный детерминизм-gate в CI. Источник: frugaltesting.com (2025).

### Code review
- Бенчмарк Greptile (июль 2025, 5 инструментов × 50 реальных багов): Greptile catch-rate **82%** но **11 false-positives**; CodeRabbit **44%** но всего **2 FP**; Graphite **6%**. Урок: trade-off detection↔noise; AI-review ускоряет, но не заменяет человеческий review. Источник: greptile.com/benchmarks (2025-07). **[monthly — инструменты быстро меняются]**

### Проверка на угрозы / безопасность (SAST/DAST/SCA, secrets, supply-chain)
- AI-SAST FPR-разброс огромен: Veracode <1.1%, Cycode 2.1% (март 2025), Xygeni 16.7%, **Snyk 34.55%, Semgrep 42.09%** (по сравнению Xygeni). True-positive: Xygeni 100%, Snyk Code 97.18%, Semgrep 87.06%, SonarQube 50.36%. Semgrep Assistant: −20% шума «в день включения»; Snyk −30% FP. Источник: corgea.com, xygeni.io, semgrep.dev (2025-2026). [monthly]
- Auto-fix реальность: GitHub/Pixee **76% merge-rate** автоматических security-PR в проде (2024-2025), но «industry average для AI security-fixes <10%». Источник: pixee.ai (2026). [monthly]
- **Prompt-injection в dev-агентах = новый класс supply-chain угрозы.** CamoLeak (CVE-2025-59145, CVSS 9.6): скрытые в markdown-комментариях PR инструкции заставляли GitHub Copilot Chat эксфильтровать приватный код/секреты через Camo image-proxy. Патч авг 2025 (отключён image rendering в Copilot Chat), раскрытие окт 2025. Источник: legitsecurity.com, securityboulevard.com (2025-10). [yearly+ как класс угрозы]
- Slopsquatting / package hallucination — см. `failures-and-limitations.md` (отдельный кейс). 

### Документирование / отладка / рефакторинг / миграции
- Документация: 39% файлов в крупном анализе AI-кода — generation документации (arXiv:2510.26103). См. вопрос 6.
- Отладка: AI ускоряет RCA, но **не заменяет** навык; «AI debugging fails because assistants lack full system context, runtime insight, historical bug patterns» (Microsoft AgentRx: +23.6% failure-localization). Gartner: >40% agentic-AI проектов отменят к 2027, среди причин — недостаточная debugging-инфраструктура. Источник: microsoft.com/research AgentRx, galileo.ai (2025). [yearly+]
- Миграции легаси: AWS Transform (GA май 2025, превью re:Invent 2024) — COBOL→Java, JCL→Groovy, агентная business-logic extraction. Morgan Stanley DevGen.AI (на GPT): интерпретировал **9 млн строк** легаси, сэкономил **280 000 часов**. Источник: aws.amazon.com/blogs (2025), press.aboutamazon.com (2024-12). **Caveat для лекции:** vendor-цифры, не peer-reviewed; переведённый код требует ручной верификации. [yearly+ с caveat]

---

## Вопрос 3 — Методологии разработки × ИИ (какие «ложатся» лучше)

| Методология | Как ложится на ИИ | Источник |
|---|---|---|
| **TDD** | Лучше всего. Тест = точная спецификация → LLM фокусируется на малых проверяемых целях. DORA 2025: AI — «амплификатор», TDD усиливается. GraphRAG+TDD: −72% peer-review failures vs vanilla, −81% vs TDD-only. | cloud.google.com/discover (2025), arXiv:2603.17973 |
| **Spec-driven dev (SDD)** | Растущий мейнстрим: GitHub Spec Kit, AWS Kiro (mid-2025, requirements.md/design.md/tasks.md), OpenSpec, BMAD, Tessl, Google Antigravity. Early-adopter reports: **3–10× выше first-pass success** (GitHub/AWS — vendor). Code остаётся source of truth; spec делает границы явными для параллельной работы человек/агент. | infoworld.com, github.com/gotalab/cc-sdd (2026) |
| **Code review (peer)** | Не отмирает — усиливается (AI генерирует код с unknown flaws → нужно БОЛЬШЕ review). AI-review дополняет, не заменяет. | greptile.com, medium @pravir.raghu (2025) |
| **Pair/ensemble programming** | Становится опциональнее, tool-assisted, точечнее; AI частично играет роль «навигатора». | medium @pravir.raghu (2025) |
| **Trunk-based + CI/CD quality-gates** | Критичнее: AI повышает throughput, но ухудшает delivery stability (DORA) → нужны строгие gates (тесты, mutation, security-scan, детерминизм). | DORA 2025 |
| **Agile/Scrum, управление командой** | Никуда не деваются, «уточняются»: ownership, accountability, design integrity сохраняются; Brooks-принципы консеквенции **ускоряются** (см. вопрос 4). | DORA 2025, blog.forret.com (2025-10) |

**Что меняется в DoD/CI:** добавляются gates — mutation-score (не только coverage), детерминизм/flaky-gate, security-scan AI-кода, человеческий review-обязателен, approval-gate перед prod/деструктивными операциями (урок Replit/Kiro).

---

## Вопрос 4 — Параллели и различия: разработка с ИИ vs людьми

- **Скорость:** на изолированных задачах AI ускоряет (Copilot RCT +55%); на крупных задачах в знакомом легаси у экспертов — **замедляет** (METR −19%, early-2025). Эффект контекстно-зависим, не универсален.
- **Типы ошибок:** человек — усталость/опечатки; AI — уверенные галлюцинации (несуществующие API/пакеты), «почти правильно» (66% разработчиков — топ-фрустрация, SO 2025), систематические уязвимости (CWE-паттерны).
- **Доверие/ревью:** SO 2025 — 84% используют (рост с 76% 2024), но **доверие падает**: позитивный sentiment 70%→60% за 2 года, distrust 46% > trust 33%, «highly trust» 3.1%. Опытные — самые осторожные. → review человеком обязателен. **[DIRECTION: доверие ПАДАЕТ при росте adoption — verify direction в первоисточнике]**
- **Ответственность:** не делегируется агенту (Replit-агент «оценил себя на 95/100» и солгал — accountability остаётся человеческой).
- **Обучение junior:** Anthropic RCT (n=52 junior, arXiv:2601.20245, 2026-02-03): AI-группа на квизе **−17%** (~2 буквенные оценки); делегировавшие генерацию <40%, спрашивавшие концепции ≥65%. → деградация навыков при «delegation»-паттерне.
- **Исторические методики не отмирают, уточняются:** Brooks «No Silver Bullet» (1986/1995): AI бьёт *accidental* complexity (boilerplate, debugging-рутина, доки), НЕ *essential* («hardest part is deciding precisely what to build»). AI убирает «трение» ручного кода, которое служило тормозом плохого дизайна → плохие практики коллапсируют **быстрее и масштабнее**. DORA 2025: «AI doesn't fix a team; it amplifies what's already there». Brooks's Law под агентами — blog.forret.com «Mythical Agent-Month» (2025-10). Источник: en.wikipedia.org/Mythical_Man-Month, newsletter.pragmaticengineer.com. [yearly+ — стабильно]

---

## Вопрос 5 — Конфигурации: solo+AI vs team+AI

Детали — в `progression-and-configs.md`. Тезис: solo-разработчик+AI-«команда» (стоимость $300–500/мес vs $80–120k/мес human-эквивалент; 36.3% новых венчуров solo-founded в 2026) масштабирует execution (80–85% по vendor-оценкам), но **human judgment — невосполнимое ядро** (что строить, цена, market), solo = «exhausted bottleneck» (каждое решение через одного человека). Команда людей+AI: SDD «ломается при переходе от одного к команде без shared visibility». Источники: blog.mean.ceo, taskade.com, loadsys.com (2026). [quarterly — adoption-числа; вывод yearly+]

---

## Вопрос 6 — Documentation-as-code: подтверждается ли?

**Вердикт: ЧАСТИЧНО ПОДТВЕРЖДАЕТСЯ (MEDIUM confidence) — да, актуализируется, но не «spec = единственный source of truth».**

ЗА (подтверждено):
- **AGENTS.md** формализован авг 2025 (OpenAI, Google, Cursor, Factory, Sourcegraph); 20k+ репо к дебюту → **40k+ open-source проектов** к концу 2025. Native support: GitHub Copilot (авг 2025), Codex, Cursor, Jules/Gemini, Factory, Amp, Windsurf, Zed, RooCode. Источник: infoq.com (2025-08), agents.md. [monthly для adoption]
- Context engineering: machine-readable config-файлы (AGENTS.md/CLAUDE.md/constitution) автоматически инжектятся в промпт агента. SKILL.md, AAIF-консорциум (дек 2025: MCP+Goose+AGENTS.md). Источник: arXiv:2510.21413, intuitionlabs.ai.

ОГОВОРКА (честно):
- cc-sdd/SDD-практики прямо говорят: **«Code remains the source of truth»**, spec — контракт границ, НЕ master-документ. Т.е. «docs-as-code актуальнее как контекст для агентов» — да; «спецификация замещает код как истину» — **слабо подтверждено / маркетинговый overclaim** (3–10× first-pass — vendor early-adopter reports, не независимое исследование).

Формулировка для лекции: «Documentation-as-code усиливается как **машиночитаемый контекст для агентов** (AGENTS.md/CLAUDE.md — де-факто стандарт с авг 2025); но утверждение "спека = единственный источник истины" — пока vendor-claim, не доказано независимо».

---

## Вопрос 7 — Инструменты: востребованные vs уходящие

Полная картина — `tools-landscape.md`. Кратко (JetBrains survey n>10000, янв 2026, baseline сент 2025):
- **Растут:** Claude Code (3% апр-июнь 2025 → 18% янв 2026, 6×; US/Canada 24%; CSAT 91%, NPS 54); Cursor ($2B ARR, >1M платящих, +35% за 9 мес); JetBrains AI Assistant 9% / Junie 5%; Google Antigravity 6% (новый); spec-driven IDE (Kiro).
- **Стагнируют/уходят относительно:** **GitHub Copilot** — всё ещё #1 по охвату (29% work, 76% awareness), но **рост awareness и adoption застопорился** (stalled since last year). OpenAI Codex 3% (nascent/declining по этой выборке).
- **Не раскрыто в свежих данных:** Tabnine, Codeium/Windsurf — в крупных 2026-выборках почти не фигурируют (сигнал маргинализации, но точных decline-чисел НЕТ → не утверждать «умерли», говорить «выпали из топ-данных»).
- Паттерн: «tool-stacking» — 2–4 инструмента одновременно; доминирующий — Cursor (edit) + Claude Code (сложные задачи). Источник: blog.jetbrains.com/research (2026-04), newsletter.pragmaticengineer.com. **[quarterly для долей; monthly для feature-наборов]**

---

## Ключевые «verify on day of lecture» (см. также freshness-report в качестве QA)

1. SWE-bench Verified / Pro лидеры и числа (88.7% / 64.3%) — **weekly**, может сместиться на 10+ пп.
2. Claude Code / Cursor / Copilot adoption % (JetBrains/Pragmatic) — **quarterly** (но рынок быстрый).
3. Любой «лучший инструмент X» / leaderboard — weekly.
4. METR late-2025 update — статус «unreliable signal», проверить, вышел ли financial/methodology re-run.
5. Market size $12.8B/2026 и solo-founder $-цифры — quarterly, vendor-зависимы.

Стабильные (yearly+, не требуют day-of-проверки): Brooks essential/accidental, METR early-2025 perception-gap, SO 2025 trust-падение, Anthropic −17% skill, GitClear churn, Replit/Kiro/curl кейсы (исторические факты с датой).

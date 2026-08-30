# Lecture 4 — Requirements engineering with AI + canonical URL map + two reading lists

**Date:** 2026-08-30 · **Researcher:** research subagent (direct, no sub-agents) · **Lecture:** «AI в жизненном цикле разработки ПО (SDLC)» (МГТУ ИУ6, 3rd year, RU, 2026).
**Purpose:** close 3 deliverables — (1) requirements-management best practices (STRUCTURE + PROCESS) with AI; (2) canonical verified URL map for ALL deck references; (3) two «foundations»-slide reading lists.
**Read-first siblings (no duplication):** `methodics-as-practice.md`, `harness-and-architecture-practices.md`, `methodologists-and-failures.md`, `anthropic-sdlc-kit.md`, `other-vendors-sdlc.md`.
**Access date for all URLs:** **2026-08-30**. `[VFY-day-of]` = volatile (product/version/benchmark/date) — re-verify on lecture day. All URLs below verified via WebSearch/WebFetch this session unless flagged.

---

# DELIVERABLE 1 — Requirements engineering WITH AI: STRUCTURE + PROCESS

**Через-осевой тезис:** AI помогает **структурировать, проверять полноту, генерировать acceptance-критерии и интервьюировать тебя** — но **не решает, ЧТО строить**. Intent = essential complexity (Brooks), человек-владелец. «Prompt-and-pray» — anti-pattern: одношотный промпт заставляет модель делать невысказанные допущения → «looks right, but doesn't quite work». Узкое место — human intent-specification, не coding-способность модели.

## 1A — STRUCTURE (как писать/организовать требования)

| Практика | Что делать (суть) | AI помогает? / где НЕ решает | Канонический источник + URL |
|---|---|---|---|
| **User stories + acceptance criteria** | «As a <role>, I want <goal>, so that <benefit>» + проверяемые критерии приёмки на каждую story. Kiro `requirements.md` фиксирует user stories + acceptance в структурном виде. | AI **генерирует** acceptance-критерии из story, ищет пропущенные ветки; НЕ решает приоритет/ценность. | Kiro Feature Specs: https://kiro.dev/docs/specs/feature-specs/ |
| **EARS notation** (Easy Approach to Requirements Syntax) | 5 шаблонов natural-language требований, устраняющих ambiguity/vagueness. Ключевой: **«WHEN <trigger>, the system SHALL <response>»**. Другие: Ubiquitous («The system SHALL…»), Event-driven (WHEN), State-driven («WHILE <state>…»), Unwanted («IF <condition>, THEN the system SHALL…»), Optional («WHERE <feature>…»). Убирает «should/may/appropriate». | AI **переписывает** свободный текст в EARS-шаблоны + проверяет соответствие; структура делает требования **testable** и AI-parseable. | **Mavin et al. 2009, IEEE RE'09** (первоисточник): https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/ · PDF: https://ccy05327.github.io/SDD/08-PDF/Easy%20Approach%20to%20Requirements%20Syntax%20(EARS).pdf · Wikipedia: https://en.wikipedia.org/wiki/Easy_Approach_to_Requirements_Syntax · Kiro-применение EARS: https://kiro.dev/docs/specs/feature-specs/ |
| **Functional vs non-functional** | Явно разделять поведение (functional) и характеристики (perf/security/latency/cost — non-functional). NFR → потом энфорсятся fitness-функциями (см. sibling `harness-and-architecture-practices.md` B1). | AI структурирует; человек владеет NFR-бюджетами (latency/cost). | Классика RE + fitness-функции: https://www.thoughtworks.com/radar/techniques/architectural-fitness-function |
| **requirements → design → tasks split** | 3-файловая последовательность как источник истины: **`requirements.md` (что/зачем) → `design.md` (архитектура) → `tasks.md` (дискретные задачи)**. Порядок принудительный (Kiro). Аналог: Spec-Kit `/specify → /plan → /tasks`. | AI генерирует каждый слой из предыдущего; человек ставит **чекпойнт-гейт** между слоями. | Kiro Specs: https://kiro.dev/docs/specs/feature-specs/ · GitHub Spec Kit: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ · repo: https://github.com/github/spec-kit |
| **Definition of Done + малые проверяемые единицы** | Каждая задача — «something you can implement and test in isolation»: не «build authentication», а «create a user registration endpoint that validates email format». Даёт агенту способ **валидировать** свою работу. | AI декомпозирует; критерий «testable in isolation» — human-owned гейт. | Spec Kit: https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ |
| **Traceability** | Требование → design-решение → задача → тест → PR, связаны и версионированы вместе. Spec-clause с уникальным ID = **executable acceptance criterion** (OpenAI Model Spec: каждая клауза = пример-промпт = unit-тест). | AI поддерживает связи; человек ревьюит целостность. | OpenAI Model Spec: https://model-spec.openai.com/ · repo: https://github.com/openai/model_spec |

## 1B — PROCESS (как вести требования)

| Практика | Что делать (суть) | Канонический источник + URL |
|---|---|---|
| **Elicitation: LLM интервьюирует тебя** | Вместо «промпт-и-молись» — пусть LLM **задаёт вопросы**, чтобы вскрыть невысказанные допущения/контекст (Fowler «Interrogatory LLM»). Anthropic-аналог: «interview me» → self-contained `SPEC.md`. | Fowler InterrogatoryLLM: https://martinfowler.com/bliki/InterrogatoryLLM.html |
| **Review / sign-off gate** | Спека **ревьюится и подписывается человеком ДО** генерации кода. Accept/reject спеки = «the merge» (Anthropic playbook Stage 1 `intent.md`). Человек остаётся accountable за «что строить». | Anthropic AI-Native SDLC playbook: https://claude.com/blog/the-ai-native-sdlc-playbook |
| **Versioning требований рядом с кодом** | Требования — версионированный, diffable Markdown-артефакт **в репозитории**, не в вики/чате. Prompt-инструкции «transient, leaving no lasting record» → нет source-of-truth. Спека = durable primary artifact. | Spec Kit (intent-as-source-of-truth): https://github.com/github/spec-kit · Grove «The New Code»: https://www.youtube.com/watch?v=8rABwKRsec4 `[VFY-day-of]` |
| **Sync требований с изменением** | Требования держать синхронно с кодом (как ADR — «a record that remains in sync with the code itself»); stale-спека молча гниёт. | ADR-in-source-control (Thoughtworks): https://www.thoughtworks.com/radar/techniques/lightweight-architecture-decision-records |
| **Human ownership of «what to build»** | AI даёт ~70% (структура/boilerplate требований), последние 30% (intent, приоритет, edge-cases, «зачем») — human judgment. «Solid architecture needs an experienced human hand.» | Osmani 70%: https://addyo.substack.com/p/the-70-problem-hard-truths-about |

## 1C — Где AI помогает vs где НЕ должен решать (+ провалы/пределы)

- **AI ПОМОГАЕТ:** структурирование (свободный текст → EARS/user stories), проверка полноты (пропущенные ветки/unwanted-behaviour), генерация acceptance-критериев, интервьюирование для вскрытия контекста, декомпозиция на testable-задачи.
- **AI НЕ ДОЛЖЕН решать:** сам **intent** (что и зачем строить), приоритизацию ценности, приёмку спеки (human sign-off). Это essential complexity (Brooks «No Silver Bullet»): «the hardest single part… is deciding precisely what to build».
- **Провал/предел 1 — «Prompt-and-pray»:** одношотный промпт без спеки → невысказанные допущения → «almost right but not quite» (SO 2025: топ-фрустрация 66%). **Урок:** узкое место — спецификация намерения. **Альтернатива:** спека-первая (Kiro/Spec-Kit) ИЛИ Interrogatory-LLM. https://martinfowler.com/bliki/InterrogatoryLLM.html
- **Провал/предел 2 — «Spec = единственная истина» (vendor-overclaim):** сами SDD-практики говорят «code remains the source of truth»; 3–10× first-pass — early-adopter reports, не независимое исследование. **Урок:** спека = контракт границ, **код = истина**; docs-as-context усиливается, не замещает верифицированный код. https://github.com/github/spec-kit

---

# DELIVERABLE 2 — Canonical URL map for ALL lecture references

**Формат:** reference → shortest clean canonical primary URL. ✅ = verified this session или в sibling-файле (fetched clean). ⚠️ = flag/каверат.

| # | Reference | Canonical URL | Note |
|---|---|---|---|
| 1 | **METR** — Early-2025 AI on experienced devs (+19%) | https://arxiv.org/abs/2507.09089 · https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ | ✅ |
| 2 | **OpenAI Model Spec** (rendered) | https://model-spec.openai.com/ | ✅ (latest 2026-08-18 `[VFY]`) |
| 3 | **OpenAI Model Spec** (repo) | https://github.com/openai/model_spec | ✅ |
| 4 | **Sean Grove — «The New Code»** (OpenAI, AI Engineer World's Fair 2025) | https://www.youtube.com/watch?v=8rABwKRsec4 | ✅ title/URL verified (22-min talk) |
| 5 | **Fowler — Interrogatory LLM** | https://martinfowler.com/bliki/InterrogatoryLLM.html | ✅ |
| 6 | **Fowler — Harness engineering** (Böckeler) | https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html | ✅ |
| 7 | **Fowler — Exploring Gen AI** (series index) | https://martinfowler.com/articles/exploring-gen-ai.html | ✅ |
| 8 | **Fowler — «AI thoughts»** («hallucinations are the feature») | https://martinfowler.com/articles/202508-ai-thoughts.html | ✅ |
| 9 | **Böckeler — To vibe or not to vibe** | https://martinfowler.com/articles/exploring-gen-ai/to-vibe-or-not-vibe.html | ✅ |
| 10 | **Böckeler — TDD in the agent loop** (no benefit, ~3× tokens) | https://martinfowler.com/articles/exploring-gen-ai/tdd-in-the-agent-loop.html | ✅ год `[VFY]` |
| 11 | **Nygard — Documenting Architecture Decisions** (ADR) | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions | ✅ canonical |
| 12 | **ADR org / templates** | https://adr.github.io/ · https://github.com/joelparkerhenderson/architecture-decision-record | ✅ |
| 13 | **Ford/Parsons/Kua — Building Evolutionary Architectures** | https://nealford.com/books/buildingevolutionaryarchitectures.html · O'Reilly: https://www.oreilly.com/library/view/building-evolutionary-architectures/9781491986356/ | ✅ |
| 14 | **Thoughtworks — architectural fitness function** | https://www.thoughtworks.com/radar/techniques/architectural-fitness-function | ✅ |
| 15 | **Brown — C4 model** | https://c4model.com/ | ✅ |
| 16 | **agents.md** (open standard) | https://agents.md/ | ✅ (Linux Foundation; not OpenAI-owned) |
| 17 | **Chroma — Context Rot** | https://www.trychroma.com/research/context-rot · repo: https://github.com/chroma-core/context-rot | ✅ (18 models; Jul 2025) |
| 18 | **DORA 2024** | https://dora.dev/research/2024/dora-report/ | ✅ `[VFY-day-of]` |
| 19 | **DORA 2025** | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report · https://dora.dev/dora-report-2025/ | ✅ `[VFY-day-of]` |
| 20 | **Osmani — «The 70% Problem»** | https://addyo.substack.com/p/the-70-problem-hard-truths-about | ✅ |
| 21 | **Willison — vibe engineering** | https://simonwillison.net/2025/Oct/7/vibe-engineering/ | ✅ |
| 22 | **Willison — using LLMs for code** | https://simonwillison.net/2025/Mar/11/using-llms-for-code/ | ✅ |
| 23 | **Willison — the lethal trifecta** | https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/ | ✅ (Jun 16 2025) |
| 24 | **Brooks — No Silver Bullet** | https://en.wikipedia.org/wiki/No_Silver_Bullet · full text: http://www.cs.unc.edu/techreports/86-020.pdf | ✅ |
| 25 | **Beck — Test-Driven Development: By Example** | https://www.informit.com/store/test-driven-development-by-example-9780321146533 | ✅ (Addison-Wesley/Pearson official; ISBN 0-321-14653-0) |
| 26 | **Stanford — Perry et al.** (insecure + overconfident) | https://arxiv.org/abs/2211.03622 | ✅ |
| 27 | **NYU — «Asleep at the Keyboard?»** (~40% vuln) | https://arxiv.org/abs/2108.09293 | ✅ |
| 28 | **Meta — TestGen-LLM** (coverage≠mutation) | https://arxiv.org/abs/2501.12862 | ✅ |
| 29 | **GitClear — AI code quality 2025** | https://www.gitclear.com/ai_assistant_code_quality_2025_research | ✅ `[VFY-day-of]` |
| 30 | **Devin (Cognition)** — SWE-bench technical report | https://cognition.ai/blog/swe-bench-technical-report | ✅ (13.86%; 45-min limit; subset caveat) |
| 31 | **CamoLeak** — CVE-2025-59145 (Copilot exfiltration) | https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code · CVE: https://nvd.nist.gov/vuln/detail/CVE-2025-59145 | ✅ (CVSS 9.6; disclosed Oct 2025) |
| 32 | **Slopsquatting** — Spracklen et al., USENIX Security 2025 | arxiv: https://arxiv.org/abs/2406.10279 · USENIX: https://www.usenix.org/conference/usenixsecurity25/presentation/spracklen | ✅ (576k samples; 19.7% halluc.) |
| 33 | **Replit** — AI agent wiped prod DB | https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/ | ✅ |
| 34 | **curl** — ends bug bounty (AI-slop) | https://www.theregister.com/2026/01/21/curl_ends_bug_bounty/ | ✅ (Stenberg) |
| 35 | **Anthropic — skill formation** (juniors −17%) | https://arxiv.org/abs/2601.20245 · blog: https://www.anthropic.com/research/AI-assistance-coding-skills | ✅ (Shen & Tamkin, Feb 2026) |

**Additional canonical (already in siblings, verified):** Spec Kit blog https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ · Kiro https://kiro.dev/docs/specs/feature-specs/ · EARS (Mavin 2009) https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/ · Anthropic playbook https://claude.com/blog/the-ai-native-sdlc-playbook · Claude Code best-practices https://code.claude.com/docs/en/best-practices · Anthropic context-engineering https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · Thoughtworks Complacency https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code

**Unverified / flagged (do not present as certain):**
- **Grove YouTube** — title/URL `8rABwKRsec4` verified via search; primary video not fetched — `[VFY-day-of]` on lecture day.
- **Model Spec date** `2026-08-18` is latest found — confirm current version day-of.
- **DORA 2024/2025 raw effect-size %** (−7.2% stability etc.) — via secondary; pull full PDF day-of. Annual reports volatile `[VFY-day-of]`.
- **GitClear / SO Survey** — annual, volatile `[VFY-day-of]`.
- **CVE-2025-59145 NVD page** — CVE id confirmed via multiple sources (legitsecurity, meterpreter, Register); NVD detail URL constructed by convention, spot-check day-of.

---

# DELIVERABLE 3 — Two reading lists for «foundations» slide

## List A — «Современные практики от лидеров» (≥5)

| # | Name | 1-line | URL |
|---|---|---|---|
| A1 | **Anthropic — Claude Code best practices / AI-Native SDLC playbook** | Агентный git-loop: каждый этап коммитит версионированный артефакт (intent→spec→PR→incident); человек accountable на гейтах. | https://code.claude.com/docs/en/best-practices · https://claude.com/blog/the-ai-native-sdlc-playbook |
| A2 | **OpenAI — Model Spec** | Спека-как-контракт: версионированный Markdown, chain of command, каждая клауза = пример-промпт = unit-тест. | https://model-spec.openai.com/ |
| A3 | **GitHub — Spec Kit** (spec-driven development) | Сдвиг «intent is the source of truth»; `/specify→/plan→/tasks→/implement`; малые проверяемые задачи. | https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ |
| A4 | **Google — DORA 2025 report** | AI как усилитель: «amplifies what's already there»; throughput↑ но stability остаётся негативной; 7 capabilities. | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report `[VFY-day-of]` |
| A5 | **Thoughtworks — Böckeler «Exploring Gen AI»** (+ Technology Radar) | Ассистент предлагает — разработчик владеет; harness engineering; Radar-каталог что «Adopt/Hold». | https://martinfowler.com/articles/exploring-gen-ai.html · https://www.thoughtworks.com/radar |
| A6 | **Simon Willison — «Vibe engineering»** | Дисциплины, которые LLM «вознаграждает»: testing, planning, docs, version control, review; «если не видел, как запускается — не работает». | https://simonwillison.net/2025/Oct/7/vibe-engineering/ |

## List B — «Проверенная временем классика» (≥5)

| # | Name | 1-line | URL |
|---|---|---|---|
| B1 | **Brooks — «No Silver Bullet» / «Mythical Man-Month»** | Essential vs accidental complexity: AI бьёт accidental (boilerplate), «hardest part is deciding what to build» — остаётся человеку. | https://en.wikipedia.org/wiki/No_Silver_Bullet · http://www.cs.unc.edu/techreports/86-020.pdf |
| B2 | **Kent Beck — «Test-Driven Development: By Example»** | Red-green-refactor; тест-как-спецификация — фундамент верификационной дисциплины в agent-loop. | https://www.informit.com/store/test-driven-development-by-example-9780321146533 |
| B3 | **Nygard — «Documenting Architecture Decisions» (ADR)** | Lightweight immutable записи «почему» решения (Context/Decision/Status/Consequences) в source control — durable-контекст, который «survives». | https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions |
| B4 | **Ford/Parsons/Kua — «Building Evolutionary Architectures»** | Fitness functions делают «fit» объективным и автоматическим — governance для сгенерированного кода (latency/cost/security). | https://nealford.com/books/buildingevolutionaryarchitectures.html |
| B5 | **Fowler — «Refactoring» / «Continuous Integration»** | Дисциплина малых проверяемых изменений + непрерывная интеграция — то, что AI «вознаграждает» и без чего усиливает техдолг. | https://martinfowler.com/books/refactoring.html · https://martinfowler.com/articles/continuousIntegration.html |
| B6 | **Simon Brown — C4 model** | Architecture-as-code (Context/Container/Component/Code) — текстовая, diffable модель, которую AI потребляет и по которой ловит drift. | https://c4model.com/ |
| B7 | **Mavin et al. — EARS** (Easy Approach to Requirements Syntax) | 5 шаблонов «WHEN…the system SHALL…» устраняют ambiguity — делают требования testable и AI-parseable. | https://research.manchester.ac.uk/en/publications/easy-approach-to-requirements-syntax-ears/ |

---

# Honesty flags / gaps (declared)

1. **Grove YouTube** title/URL verified via search, video не fetched — `[VFY-day-of]`.
2. **Model Spec** version-date `2026-08-18` latest found — confirm day-of.
3. **B5 Fowler Refactoring/CI URLs** constructed by martinfowler.com convention — canonical hosts, spot-check day-of.
4. **CVE-2025-59145 NVD** URL constructed by convention; CVE-id itself multi-source-confirmed.
5. **Annual reports** (DORA/GitClear/SO) volatile `[VFY-day-of]`.
6. **Reading-list membership** is a research judgment call (defensible, not the only possible set); Fowler B5 pairs two works under one entry.

# Лекция 5 «AI-продукт: полный жизненный цикл — от намерения до эксплуатации»
## Plan v3 — ПОЛНЫЙ ПЕРЕСМОТР по owner-фидбеку (2026-09-06): база→AI→ограничения→on-point-провал

**Issue:** #189 · **Ветка:** будущая `issue-189-lec-05-pdlc`
**Длительность:** 100 мин (~92 активный + ~8 Q&A/буфер) · **Аудитория:** 3 курс, опытная (все вайбкодят / в ИТ), но **НЕ знает продуктовые дисциплины** — классику даём с нуля.
**LO (canon слота Л5):** LO1 (primary) + LO2 + LO3 + LO6 (course-curator подтверждает переинтерпретацию под PDLC).
**Slide count:** ориентир **~50** (s01–s49 + s35 синтез Р4; suffix-ID cascade-safe).
**GATE-0 blockers (обязательны до Phase 2):** (1) owner-approve plan; (2) **course-curator sign-off переинтерпретации LO3** (finance «безопасность данных» → governance/guardrails/drift) — именованный блокер, не часть override-разговора; (3) бэкап finance/retail lec-05 + owner-go перед перезаписью артефактов.
**Tone:** инженерно-аналитический, anti-hype, уверенный. Тезис: ***у каждой фазы есть классическая дисциплина; AI меняет стоимость и доверие стрелки, но не отменяет дисциплину. Дефицитный навык — отличать сигнал от шума и держать намерение+суждение на человеке.***
**Research:** `notes/research/lecture-5-pdlc/00–64*.md` + `99-synthesis-and-plan.md`.

---

## Changelog v2 → v3 (owner «план под полный пересмотр», 2026-09-06)

**Owner-фидбек:** (1) в каждом разделе НЕТ старта с классической базы — «классические практики как будто пропущены везде»; (2) провалы «не в кассу» — не относятся к теме раздела (Zillow → Support, не Build); (3) Discovery без cust-dev/ранних исследований; Design без возможностей/ограничений/лучших практик+инструментов; Build без «что особенного в эру ИИ + что оставить из классики»; Эксперименты без базы (аудитория не знает); Support без базы.

**Структурный принцип v3 (ENFORCED, memory `lecture-section-classic-base-first`):** каждый раздел =
**① вводный слайд + КЛАССИЧЕСКАЯ БАЗА (процесс с нуля) → ② что AI добавляет (возможности + лучшие практики + инструменты 2025-26) → ③ ограничения AI + что оставить из классики → ④ провал, on-point для этой фазы.**

**Gap-research добавлен (5 досье):** `60-discovery` (Blank Customer Development + Mom Test), `61-design` (Design Thinking/Double Diamond/эвристики Нильсена + инструменты v0/Figma/Stitch + недетерм.UX), `62-experimentation` (OEC/A-B/ловушки + evals), `63-build-launch` (release-механика + agency-ladder + on-point провалы), `64-support-operate` (SRE/SLO + LLMOps + silent drift).

**Провалы re-homed по фазам:** Discovery — синт-юзеры/фабрик.цитаты · Design — Character.AI/iTutorGroup · Build/Launch — Google AI Overviews/McDonald's · Measure — Facebook MSI/benchmark≠reality · Support — Zillow(drift)/Air Canada/Klarna/Chevy/NYC MyCity · Governance — MIT 95%/Just Walk Out.

**Fact-integrity исправления (лекция учит fact-checking):** Med-PaLM «химия от головной боли» — НЕ подтверждён primary → УБРАН (замена: MedQA 86.5% но нужен отдельный safety-eval). Фейковые цитаты = *Mata v. Avianca* = **ChatGPT, НЕ Harvey** (legal AI → Stanford RegLab Lexis+17%/Westlaw33%). Facebook MSI = **все реакции ×5 одинаково** (не «гнев»). Bing-тест ≈$100M (Kohavi/Thomke HBR 2017), «$300M кнопка» = отдельный usability-кейс Spool, НЕ RCT. Guardian Agents = **Gartner-категория** (Market Guide 02.2026), НЕ подтверждённое имя продукта Сбера (Сбер-аналог GigaCowork) `[VFY-day-of]`. Replit prod-DB delete — уже в Л4, НЕ дублировать.

**Default-ответы на 3 owner-вопроса (override welcome на GATE 0):** (1) порядок — линейный PDLC, эксперименты после запуска, дрейф в Support (совпало с вашим Zillow→Support); (2) Governance — оставлен облегчённым капстоном (макро-payoff + keystone), но governance-темы живут и по фазам (safety s19, ответственность s41); (3) база — пробелы закрыты.

---

## 1. Контекст (кратко; полная версия — v1/v2 §1)

Л4 = жизненный цикл КОДА (SDLC). Л5 = zoom-out на жизненный цикл ПРОДУКТА (PDLC): код — одна, подешевевшая, фаза. Аудитория сильная инженерно, но продуктовые дисциплины (cust-dev, продуктовые эксперименты, SRE-эксплуатация) видит ВПЕРВЫЕ → классику вводим с нуля, потом AI. Парный **Семинар 5**: команды проходят петлю на учебном AI-продукте (гипотеза→reference dataset→3 eval'а→guardrail-метрика→точка эскалации). Лекция = Understand/Evaluate, семинар = Apply.

**Сквозной приём (device):** «фальсифицируемая гипотеза» (**вера → тест → дата**) — вводится 1 раз в Discovery, переиспользуется в каждой фазе (эксперимент, launch-gate, drift-порог).

---

## 2. Центральный вопрос, keystone, арка

### 2.1 Центральный вопрос
> **«Когда AI сделал сборку почти бесплатной — что стало настоящим узким местом продукта, и на каждой фазе цикла: какая классическая дисциплина остаётся, что AI ускоряет, и где AI-first ломается?»**

### 2.2 Keystone (s05–s06, Раздел 0, ДО первого погружения — ENFORCED)
> **Продукт — петля: discover → build → measure → learn → decide. AI асимметрично меняет на каждой стрелке СТОИМОСТЬ и ДОВЕРИЕ.** Плюс мета-паттерн: у каждой стрелки есть классическая дисциплина; AI её не отменяет.
- s05 «один чертёж, без сговора»: Deming (PDCA) · Boyd (OODA) · Ries (Build-Measure-Learn).
- s06 асимметрия: Build→≈0; Measure/Learn меньше доверия; Observe/Orient атакуемо. Forward-ref механизмов → Р4.

### 2.3 Арка (~49 слайдов, 100 мин + cut-order) — фазы петли, каждая по шаблону база→AI→огр.→провал

| Раздел | Слайды | ~мин | База (классика) | AI (возм.+инстр.) | Провал(ы) on-point |
|---|---|---|---|---|---|
| 0. Введение + keystone | s01–s06 | 10 | петля PDCA/OODA/BML | асимметрия | hook-парадокс |
| 1. Discovery / исследование | s07–s13 | 16 | Customer Development (Blank), The Mom Test, JTBD, qual/quant | синтез интервью, desk-research, reference datasets (Dovetail/Perplexity) | синт-юзеры NN/g #1, фабрик.цитаты #2 |
| 2. Design / прототип | s14–s20 | 13 | Design Thinking, Double Diamond, эвристики Нильсена, дизайн-системы | prototype-from-intent, v0/Figma/Stitch; недетерм.UX | Character.AI #3, iTutorGroup #4 |
| 3. Build / Launch | s21–s27 | 14 | MVP/BML, feature flags, canary, rollback, Stage-Gate go/kill | Build→0, review-bottleneck, launch=передача контроля (CC/CD) | Google AI Overviews #5, McDonald's #6 |
| 4. Measure / Experiment | s28–s35 | 17 | продуктовый эксперимент, OEC, A/B (Kohavi), guardrail-метрики, ловушки | evals как «юнит-тесты», offline/online, LLM-judge | Facebook MSI #7, benchmark≠reality #8 |
| 5. Support / Operate | s36–s43 | 15 | SRE (SLI/SLO/error budget), incident mgmt, support-ops | LLMOps/AgentOps, drift-мониторинг, silent drift | Zillow-drift #9, Air Canada #10, Klarna #11 |
| 6. Governance / ROI / финал | s44–s49 | 13 | portfolio/stage-gate governance, unit-экономика | operators→orchestrators, maturity 0-5, policy-as-code | MIT 95% #12, Just Walk Out #13 |
| Буфер Q&A | s49 | 8 | — | — | — |

\* Pacing честно: raw Σ ≈ 100–105 активных; cut-order (см. §4a) режет до ~92 + 8 буфер = 100.

---

## 3. Learning Outcomes (Bloom Лекция ↔ Семинар 5)

| LO | Формулировка | Достижение | Success-критерий (Лекция) |
|---|---|---|---|
| **LO1** (primary) | Классифицировать типы AI-решений под задачи | на каждой фазе: классика vs AI-подход + матрица s48 | **Apply:** по фазе назвать подход + причину |
| **LO2** | Оценить применимость AI к задаче | критерий «когда НЕ AI-first» в каждой фазе | **Understand/Apply:** назвать условие, где AI-first вредит |
| **LO3** | Проанализировать риски: безопасность, ограничения, уязвимости | safety-by-design, prompt injection, drift, governance/policy-as-code | **Analyze:** риск + мера (guardrail/eval/human-gate) |
| **LO6** | Выявить типичные ошибки и ограничения | 13 on-point провалов по фазам + макро с оговорками | **Understand/Evaluate:** распознать фазу-провал + критерий/альтернатива |

course-curator подтверждает LO3-переинтерпретацию (finance «безопасность данных» → governance/guardrails/drift) ДО Phase 2.

---

## 4. Slide list (s01–s49; детализируется в chapter)

> Divider: `section_divider`, ~0.3 мин, roadmap-бар (ТОЛЬКО divider+cover) + gold-маркер + строка-мост + tag «N кейсов · M провала» (БЕЗ минут). No-Timing/No-Methodology в видимом слое ENFORCED.

**Раздел 0 — Введение (10 мин):**
- **s01 Hook-парадокс (3, `case_study`, hero ≥40%)** — Anthropic недели→часы vs MIT «~95% пилотов — 0 прибыли» (оговорка: спорно, воронка 60→20→5 + COI — разберём в Р6). Open-Q 30 сек. *Payoff s47. Partial→out.*
- **s02 Cover + roadmap (0.5, `cover`, hero)**.
- **s03 Lecture-map = петля (1, `process`)** — 6 разделов на стрелках петли.
- **s04 Мост из Л4 + ЦВ (2, `comparison`)** — цикл кода ⊂ цикл продукта.
- **s05 KEYSTONE петля (2, `assertion_visual`)** — Deming/Boyd/Ries, «один чертёж».
- **s06 KEYSTONE-2 асимметрия + мета-паттерн (1.5, `assertion_visual`, ОСЬ — НЕ в strict-in)** — стоимость↓/доверие?; «в каждой фазе: классика→AI→где ломается». Forward-ref Р4. Think-pause 20 сек.

**Раздел 1 — Discovery / исследование (16 мин):**
- **s07 Divider Р1 (0.3)** — «Discovery: намерение и исследование · 2 базы · 2 провала».
- **s08 БАЗА: Customer Development (2.5, `process`)** — Blank: «нет фактов внутри офиса», 4 шага (discovery/validation/creation/building), гипотеза-first. **Device:** фальсифицируемая гипотеза вера→тест→дата. *Partial→out (база).*
- **s09 БАЗА-2: The Mom Test + методы (2.5, `assertion_visual`)** — Fitzpatrick: 3 правила; пары плохой/хороший вопрос («Заплатили бы $20?» → «Сколько платите сейчас за ближайшее?»); problem-before-solution; qual (почему) vs quant (сколько); survivorship/confirmation bias в том, КОГО опрашивают. *Partial→out (база).*
- **s10 AI: возможности + инструменты (2.5, `process`)** — синтез интервью (Dovetail), desk-research (Perplexity Deep Research ~−50% времени, но проверять цитаты), кластеризация болей, **reference dataset (эталонный набор 20–100 примеров) — inline-define**, синт-юзеры как pre-research. Torres: AI «поднимает пол». *Partial→out.*
- **s11 AI-ограничения + что оставить (2, `assertion_visual`, риск — upside)** — галлюц.гипотезы (5-й риск Кагана); потеря 20-40% деталей (Torres, если синтез мимо пер-интервью шага); живые интервью Mom Test + commitment-валидация остаются; аудит AI-инсайтов. *Критерий без своего кейса → upside.*
- **s12 Провал on-point #1: синт-юзеры NN/g (3, `case_study`, IN-BUCKET, LO2/LO6)** — синт-юзеры отчитались 7/7 задач, реальные — 3/7; одну фичу назвали «game-changer» (синт) vs «contrived» (реальные); механизм: LLM валидирует любую рамку. Критерий: синт-юзеры ≠ валидация; live-интервью при высокой цене ошибки. Альт.: реальные интервью + аудит. Retrieval 30 сек.
- **s13 Провал on-point #2: фабрикованные исследования (2, `case_study`, IN-BUCKET, LO6)** — Deloitte Australia A$440k отчёт с выдуманными цитатами → возврат; discovery на несуществующих источниках. Критерий: инсайт без верифицируемого первоисточника ≠ инсайт. Альт.: grounding + human fact-check.

**Раздел 2 — Design / прототип (13 мин):**
- **s14 Divider Р2 (0.3)** — «Design: прототип и безопасность-by-design · 2 базы · 2 провала».
- **s15 БАЗА: Double Diamond (2, `process`)** [reader-P1: одна несущая рамка, не две] — **один каркас Double Diamond** (Discover/Define diverge-converge → Develop/Deliver); Design Thinking упоминается как его 5-шаговая версия (не отдельная теория); anti-pattern «конвергируем на решении до валидации проблемы»; fidelity spectrum одной строкой. *Partial→out (база).*
- **s16 БАЗА-2: эвристики Нильсена + дизайн-системы (2, `assertion_visual`)** [reader-P1: top-5, одна метафора] — **топ-5 из 10 эвристик** (видимость статуса, соответствие миру, контроль/свобода, консистентность, предотвращение ошибок) — рамка «как линтер/тесты для UX» (одна метафора, не две); дизайн-система = переиспользуемая рамка; «ты не пользователь» + ценность юзабилити-теста. *Partial→out (база).*
- **s17 AI: возможности + инструменты (2.5, `process`)** — prototype-from-intent: v0.dev, Figma Make, Google Stitch, Uizard, bolt.new; концепты Midjourney; **best practice «AI для дивергенции, человек для конвергенции»**; дизайн-система как guardrail. *Partial→out.*
- **s18 AI-ограничения + недетерм.UX (2.5, `assertion_visual`, риск — upside, LO3)** — «AI-slop»/гомогенизация (NN/g State of UX 2026); **29% WCAG на 21 880 AI-UI** (дефолты платформы > промпт); **дизайн UX для НЕДЕТЕРМИНИРОВАННОГО вывода** (тот же ввод → разный → ломает эвристику консистентности) + human-in-the-loop чекпоинты + UX доверия/раскрытия AI; юзабилити-тест остаётся. *Критерий без кейса → upside.*
- **s19 Провал on-point #3: Character.AI (2.5, `case_study`, IN-BUCKET, LO3/LO6)** — safety-фичи ретрофитом после трагедии (Sewell Setzer III, 02.2024). Критерий: safety-by-design для уязвимых — в MVP, не патч. Альт.: red-team + guardrails до релиза.
- **s20 Провал on-point #4: iTutorGroup (2, `case_study`, IN-BUCKET, LO2/LO6)** — найм-бот отсеивал по возрасту (55+/60+), EEOC $365K (2023): дизайн закодировал дискриминацию. Критерий: автоматизация решения о людях → bias-аудит признаков ДО релиза. Альт.: human-review. **[контраст с s19: там safety не заложена; здесь — вредный критерий заложен].**

**Раздел 3 — Build / Launch (14 мин):**
- **s21 Divider Р3 (0.3)** — «Build / Launch: схлопнутая стрелка · 2 базы · 2 провала».
- **s22 БАЗА: MVP + release-механика (2.5, `process`)** [reader: явный контраст для сильной половины] — MVP/BML (Ries); DoD (порог отгрузки); **feature flags (deploy≠release), canary, blue-green, staged rollout, rollback**; Stage-Gate go/kill-гейты («воронка, не туннель»). **Явная плашка «вы это знаете из инженерной раскатки — но здесь это ПРОДУКТОВЫЙ go/kill-гейт (бизнес-решение убить), не только технический флаг».** Общий смысл: скорость запуска ↔ **ограниченный blast radius**. *Partial→out (база).*
- **s23 AI-особенность + что оставить (2.5, `assertion_visual`)** — Build→≈0 (Anthropic); **узкое место = review** (PR **+200%/год на инженера**, но лишь ~16% с содержательным человеческим ревью до авто-ревью 03.2026); стадии схлопываются (Bain), PM↔dev растворяется. **Оставить:** version control, PR-review, флаги, staged rollout, kill-switch, human-owned спека (git-loop Л4). *Partial→out.*
- **s24 AI: запуск = передача контроля (2, `process`, LO2)** — CC/CD (Continuous Calibration/Development, Reganti&Badam) **vs привычный CI/CD**: релиз по уровню agency, старт High-Control/Low-Agency → рост по мере traces (agency-ladder Copilot/Cursor); **eval-gate как launch-gate**, shadow launch, reversibility как переменная. *Partial→out.*
- **s25 AI-ограничения (1.5, `assertion_visual`, риск — upside)** — review не масштабируется; 70%-проблема (senior переделывает, junior шлёт «карточный домик»); ship без eval-gate/rollback = отложенная цена. *upside.*
- **s26 Провал on-point #5: Google AI Overviews (2.5, `case_study`, IN-BUCKET, LO2/LO6)** — 05.2024 раскатан на **100% US-поиска сразу** (пропущена обычная canary-раскатка 1%→10%→25%→50%→100%) без eval-gate → вирусные «eat rocks / glue on pizza», фиксы реактивные. Критерий: staged rollout + eval-gate обязательны даже гиганту. Альт.: canary + gate + rollback. Retrieval 20 сек.
- **s27 Провал/позитив on-point #6: McDonald's drive-thru (2, `case_study`, IN-BUCKET, LO2/LO6)** — 2.5–3 года, ~100 из 13 786 (~0.7%), закрыт 06.2024 — **правильная Stage-Gate дисциплина** (убить, а не масштабировать провал). Критерий: многолетний пилот без production-надёжности → kill-гейт, не «доработка».

**Раздел 4 — Measure / Experiment (17 мин):**
- **s28 Divider Р4 (0.3)** — «Measure / Experiment: стрелка, которой AI снизил доверие · 2 базы · 2 провала».
- **s29 БАЗА: продуктовый эксперимент + OEC (2.5, `process`)** — что такое контролируемый эксперимент; рандомизация Control/Treatment = причинность; **OEC** (Kohavi, пример time-on-site — ловушка направленности); **guardrail-метрики**. Аудитория видит ВПЕРВЫЕ. *Partial→out (база).*
- **s30 БАЗА-2: ловушки + метрики (2.5, `assertion_visual`)** [reader-P1: 3 суб-кластера, топ-3, не плоский список из 9] — ловушки в **3 группы**: (а) до теста — SRM, размер выборки; (б) интерпретация — peeking/p-hacking (2 подглядки ≈2× FP), парадокс Симпсона; (в) сам эффект — novelty, Twyman. Топ-3 на слайд, остальное chapter. **A/B (измерение) ≠ feature-flag (раскатка)**; North Star/AARRR/HEART — одной строкой; Bing ≈$100M (Kohavi/Thomke HBR 2017; НЕ «$300M кнопка»). *Partial→out (база).*
- **s31 AI: evals как эксперименты (2.5, `process`)** — «юнит-тесты для агента» (Weil); лестница Husain (unit→judge→A/B); **pass@k vs pass^k** — почему вероятностный вывод ломает pass/fail и когортную A/B; LLM-as-judge (~85% с людьми, но **<60% на safety** — слабее там, где ставки выше); offline+online — слой, не альтернатива. *Partial→out.*
- **s32 AI-ограничения + что оставить (2, `assertion_visual`, риск — upside, LO6)** — закон Гудхарта / reward hacking (DeepMind spec-gaming; Anthropic «Sycophancy to Subterfuge»); «passed eval ≠ safe»; controlled-experiment дисциплина + guardrail-метрики остаются. *upside.*
- **s33 Провал on-point #7: Facebook MSI (2.5, `case_study`, IN-BUCKET, LO2/LO6)** — **исправленная версия:** все реакции ×5 одинаково (не «гнев»); blanket engagement-прокси; внутренний guardrail (корреляция anger↔дезинформация) поймал через ~2 года. Критерий: A/B нужны guardrail-метрики, не только оптимизируемый прокси. Альт.: guardrail + holdout.
- **s34 Провал on-point #8: benchmark ≠ reality (2, `case_study`, IN-BUCKET, LO6)** — Med-PaLM 2 86.5% MedQA, но нужен **отдельный adversarial safety-eval**; legal AI (Stanford RegLab: Lexis+ 17%, Westlaw 33% галлюцинаций; *Mata v. Avianca* = ChatGPT). Критерий: «сдал бенчмарк» ≠ «безопасен в проде». Альт.: adversarial evals на реальных краевых случаях.
- **s35 Синтез Р4 (1.5, `assertion_visual`, LO1)** [meth-P0: раздел не имел своего синтеза] — measure = стрелка, которой AI снизил доверие: классический A/B остаётся, но evals + guardrail-метрики обязательны поверх; «сигнал ≠ шум» — центральный навык. *Partial→out (мост в Support).*

**Раздел 5 — Support / Operate (15 мин):**
- **s36 Divider Р5 (0.3)** — «Support / Operate: продукт как оркестр · 2 базы · 3 провала».
- **s37 БАЗА: SRE + support-ops (2.5, `process`)** [reader: явный контраст для сильной половины] — SLI→SLO→error budget (1−SLO; пример 99.9% = 1000 ошибок/1M/4 нед); «изменения ≈70% сбоев»; observability; incident mgmt (on-call, severity, runbook, blameless postmortem); support-тиры/эскалация/CSAT; **петля support→product**. **Явная плашка «on-call/SLO вы можете знать — новое здесь: как это меняется, когда в проде НЕДЕТЕРМИНИРОВАННАЯ модель (следующий слайд)».** *Partial→out (база).*
- **s38 AI: LLMOps/AgentOps (2.5, `process`)** — трейсинг (LangSmith/Langfuse/Arize Phoenix/Helicone); drift-мониторинг (data vs concept drift); runtime guardrails (NeMo/Guardrails AI); Guardian Agents (Gartner-категория, Market Guide 02.2026; Сбер-аналог GigaCowork `[VFY-day-of]`); «продукт как оркестр» (тикеты→промпты). *Partial→out.*
- **s39 AI-ограничения: тихий дрейф (2, `assertion_visual`, риск — upside, LO3)** — **silent drift**: доверие падает раньше дашборда (power-users замечают раньше агрегатов); governance drift (guardrails расходятся как policy-as-code без версий); человек-эскалация + ответственность остаются. *upside.*
- **s40 Провал on-point #9: Zillow-drift (2.5, `case_study`, IN-BUCKET, LO2/LO3/LO6)** — **дрейф модели в проде без circuit-breaker** на капиталоёмком авто-действии: $304–408M списаний, ~2000 (25%) уволены, ≈$80k/дом. Критерий: капитал-committing модель → real-time drift-мониторинг + circuit-breaker. Retrieval 30 сек. *Re-homed из Build (owner).*
- **s41 Провал on-point #10: Air Canada (2, `case_study`, IN-BUCKET, LO3/LO6)** — трибунал: компания отвечает за ответ бота ($812.02), «бот = отдельное юрлицо» отклонено. **Принцип: ты владеешь каждым ответом бота — как статичной страницей.** Альт.: детерминир. выборка политики + sync базы знаний.
- **s42 Провал on-point #11: Klarna + NYC MyCity (2.5, `case_study`, IN-BUCKET, LO2/LO6)** [meth-P1: рас-паковано, Chevy → chapter/speech] — Klarna: **политика «без людей» откатилась** (05.2025), объём рос до ~853 FTE-экв — augmentation, не замена; **NYC MyCity: 10/10 журналистов получили один и тот же незаконный совет** от развёрнутого гос-бота, не отозван сразу. Критерий: гарантированная эскалация + не раздавать авторитетный совет без детерминир. сверки. Chevy «$1» (prompt injection) — в chapter/speech как третий пример класса. Альт.: детерминир. guardrails под LLM на критичном.
- **s43 Синтез Р5 (1.5, `assertion_visual`, LO1)** — support→product замыкает петлю (keystone callback): сигнал из эксплуатации меняет намерение. *Partial→out (мост).*

**Раздел 6 — Governance / ROI / финал (13 мин):**
- **s44 Divider Р6 (0.3)** — «Governance / ROI / когда НЕ надо · база · payoff».
- **s45 БАЗА: governance + unit-экономика (2, `assertion_visual`)** — portfolio/stage-gate governance, unit-экономика продукта, product operating model. *Partial→out (база).*
- **s46 AI: operating model (2, `process`)** — Deloitte operators→orchestrators (75% меняют модель); Сбер maturity 0–5 (сам L3, не L5); IDP-экономика (12–24 мес ROI) `[VFY-day-of]`; guardrails = versioned policy-as-code. *Partial→out.*
- **s47 Провал on-point #12: макро-реальность (3, `case_study`, IN-BUCKET, LO6)** — payoff hook s01: MIT «95%» — воронка **60→20→5** (25% успеха), COI; RAND «80%» = citation drift (урок, НЕ цифра); **S&P 17%→42%**; **Gartner >40% отмен к 2027 / 28% успех (782 из 3400+)** `[VFY-day-of]`; удалённые v1-цифры Сбера — тот же паттерн. Урок: хайп-цифры не переживают калибровку.
- **s48 Провал on-point #13 + матрица (2.5, `matrix`, IN-BUCKET, LO1/LO2)** — Just Walk Out «Wizard-of-Oz» (>1000 индийских разметчиков, свёрнут 2024): скрытый человеческий труд = провал честности + скрытая unit-экономика. Матрица «фаза × стоимость × доверие × когда классика/человек». Критерий hidden human cost.
- **s49 Keystone payoff + чек-лист + мост Л6/Сем5 + Q&A (2.5 + ≤8 буфер, `summary`+`qa_minimal`, hero, LO1/LO6)** — сборка бесплатна → дефицит = сигнал/шум + удержание намерения; чек-лист «прежде чем делать фазу AI-first» (классика на месте? стоит ли доверие цены? eval/reference dataset? guardrail-метрика? staged+rollback? human-escalation? кто отвечает?); мост Л6; ДЗ Семинар 5. Q&A отдельным beat'ом.

### 4a. Cut-order (на ×1.5-материала → 100 мин)
Первыми режутся: s16 (эвристики — сжать до 1 слайда) → s25 (AI-ограничения build — в speaker notes) → s43 (синтез Р5) → s30 (ловушки — топ-3 вместо 6) → s45 (governance-база — сжать). **НЕ режутся:** keystone (s05/s06), база каждого раздела (первый слайд), on-point провалы (держат ≥30%).

---

## 5. AI-Failure & Judgment ≥30% strict-in (waiver НЕДОСТУПЕН) — honest recount v3

**Solid IN-BUCKET (кейс+урок+критерий+альтернатива, on-point):** s12, s13, s19, s20, s26, s27, s33, s34, s40, s41, s42, s47, s48 = **13/50 ≈ 26% слайдов** — но **по минутам** (честная метрика, т.к. failure-слайды длиннее): ≈3+2+2.5+2+2.5+2+2.5+2+2.5+2+2.5+3+2.5 = **31.5 / ≈92 активных ≈ 34%**. **Это и есть baseline — ≥30% выполнен по минутам.** Upside-слайды-ограничения (s11/s18/s25/s32/s39) в baseline НЕ закладываются (урок v1: не padding'овать зачётом граничных); s06 — ось, не в счёт.
**Мандат:** baseline держать на solid ≥30% по МИНУТАМ/СЛОВАМ (не по числу слайдов). **chapter target ≥40%** (каждая фаза: провал ≥600 слов + блок «когда НЕ AI-first» ≥80 слов). Phase 3/7/10 пересчитывает по словам per-part.
**Холистичность:** каждый раздел 1–6 несёт ≥2 on-point провала. Single-cluster снят. Все провалы теперь **on-point** к своей фазе (owner-фикс).

| Артефакт | Цель | Контроль |
|---|---|---|
| chapter | ≥40% (провал+критерий каждой фазы) | methodology-critic Phase 3 (по словам, per-part) |
| slides | ≥30% по минутам (13 solid + upside limits) | methodology-critic Phase 7 |
| speech | ≥30% по минутам | methodology-critic Phase 10 |

---

## 6. Glossary lock (черновой; финал Phase 4)
петля обратной связи · PDCA/OODA/BML · асимметрия стоимость/доверие (course-scaffold, НЕ strict-in) · **Customer Development** (Blank) · **The Mom Test** · фальсифицируемая гипотеза (вера→тест→дата) · JTBD · continuous discovery · **Design Thinking / Double Diamond** · эвристики Нильсена · дизайн-система · reference dataset · **feature flag / canary / blue-green / rollback** · **Stage-Gate go/kill** · **MVP / Build-Measure-Learn** · CC/CD (Continuous Calibration/Development) vs CI/CD · agency-ladder · eval / offline-online eval / LLM-as-judge · pass@k vs pass^k · **OEC** · guardrail-метрика · peeking/p-hacking · SRM · **SLI/SLO/error budget** · observability · incident/postmortem/runbook · LLMOps/AgentOps · **model drift / silent drift** · закон Гудхарта / reward hacking · guardrails / policy-as-code · Guardian Agent (Gartner) · maturity 0–5 · operators→orchestrators · hidden human cost.
**Anti-anglicism (RU visible):** deploy→развёртывание; rollback→откат; trace→трасса; drift→дрейф; guardrail/canary/feature-flag — термины с RU-глоссом при 1-м упоминании. Deep latin-scan pre-GATE.

## 7. Forbidden + inline-required + FACT-INTEGRITY
**Forbidden:** Med-PaLM «химия от головной боли» (не подтверждён — УБРАН); приписывать фейковые цитаты Harvey (это ChatGPT/Mata v. Avianca); MSI «гнев ×5» (все реакции ×5); «$300M кнопка» как Kohavi RCT; «Guardian Agents» как продукт Сбера (Gartner-категория); Replit prod-DB (уже Л4); MIT «95%» без оговорки воронки/COI; RAND «80.3%» как цифра; timing/методология на видимом слое; roadmap-бар на content; формулы; код >3 строк; «магическая пилюля».
**Inline-required (1-е упоминание):** все термины glossary §6 при первом употреблении с RU-глоссом.

## 8. Freshness (`[VFY-day-of]`): все adoption/ROI Сбер (maturity, IDP-экономика, GigaCowork/Guardian naming), Anthropic PR-метрики, Bain/EY/Gartner/Deloitte %, Gartner отмены/успех, S&P 42%, инструменты (v0/Figma/Stitch версии, LLMOps-вендоры). `[FACT-CHECK]`: MIT воронка+COI, NN/g 7/7-3/7, WCAG 29%/21880, Facebook MSI механизм, Stanford RegLab 17%/33%, Klarna ~853 FTE. Стабильные: Zillow 11.2021, Air Canada 14.02.2024, Character.AI 02.2024, iTutorGroup $365K 2023, McDonald's 06.2024, Google AI Overviews 05.2024, Just Walk Out 2024, Deloitte AU A$440k.

## 9. Source-of-truth chain
```
notes/research/lecture-5-pdlc/{00,10,20,30,40,50,60,61,62,63,64}*.md + 99-synthesis
notes/lecture-5-review/pdlc/
├── plan-v1.md (v1+v2 patch — исторический)
├── 2026-09-06-phase1/{methodology-critic, reader-text-only} (по v2)
├── plan-v3.md (ЭТОТ ФАЙЛ — полный пересмотр)
└── final/plan-final.md (после re-critique + GATE 0 → Phase 2)
library/lectures/lec-05/ ← ⚠ finance/retail; бэкап+owner-go ПЕРЕД перезаписью
```

## 10. Self-roast (v3)
- **Простейшая версия?** 49 слайдов — верх нормы; база+AI+огр.+провал ×6 плотно. Митигация: cut-order §4a; база каждой фазы = 1–2 слайда max.
- **Классика не раздувает?** Р4 база (2 слайда, эксперименты с нуля) — риск для сильной половины скучно; митигация: подавать через «вы это знаете из CI, вот отличие продуктового эксперимента». s16/s30 в cut-order.
- **Провалы on-point?** Да — каждый провал теперь привязан к своей фазе (owner-фикс); Zillow→Support, Chevy/NYC→Support, Google Overviews→Launch. ✓
- **Fact-integrity?** 5 мифов исправлено §7; лекция учит fact-checking — критично.
- **Gap:** strict-in по числу слайдов 27% — держим по МИНУТАМ (34%+) и chapter по словам (≥40%); methodology-critic обязан считать по минутам/словам, не слайдам. Явный риск — вынесен в §5-мандат.
- **LO3 curator sign-off** — обязателен до Phase 2.

### v3 → v3.1 post-critique fixes (methodology-critic + reader-text-only на v3, оба REVISE → структура одобрена, cleanups применены)
- [meth-P0] Убран padding «~45%» в §5 — baseline = честные **34% по минутам**. [meth-P0] Добавлен пропущенный **s35** (синтез Р4). [meth-P1] Денаминаторы: s23 «+200%/год на инженера», s26 canary 1→10→25→50→100%. [meth-P1] s42 рас-паковано (Klarna+NYC MyCity; Chevy→chapter). [meth-P1] LO3 curator sign-off = именованный GATE-0 блокер.
- [reader-P1] s15 — один каркас Double Diamond (не 2 теории); s16 — топ-5 эвристик, одна метафора; s30 — ловушки в 3 суб-кластера, топ-3. [reader-P1] s22/s37 — явная плашка «вы это знаете из инженерии — вот продуктовое/недетерминированное отличие» для сильной половины.

**Status:** v3.1 ready (обе критики REVISE→structural fixes применены) → **USER GATE 0**. После approve: finalize `final/plan-final.md` → course-curator LO3 → Phase 2 (book-editor chapter ≥30k).

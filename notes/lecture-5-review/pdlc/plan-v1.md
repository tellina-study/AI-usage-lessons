# Лекция 5 (новый вариант) «AI-продукт: полный жизненный цикл — от намерения до эксплуатации»
## Plan v1 — orchestrator draft + self-roast (→ methodology-critic + reader-text-only → USER GATE 0)

**Issue:** #189 · **Ветка:** будущая `issue-189-lec-05-pdlc`
**Длительность:** 100 мин (~93 активный + ~7 Q&A/буфер) · **Аудитория:** 3 курс, опытная (все вайбкодят / в ИТ; универсально, без local binding)
**Curriculum level:** Модуль 1, лекция 5 — **zoom-out после Л4**: Л4 = жизненный цикл КОДА (SDLC), Л5 = жизненный цикл ПРОДУКТА (PDLC). **L5 ∈ L4–L17 → owner-waiver ≥30% failure-content НЕДОСТУПЕН (Решение #82).**
**LO (сохраняем canon РПД слота Л5):** **LO1 (primary)** + LO2 + LO3 + LO6. (course-curator подтверждает после смены темы — маппинг чистый, см. §3.)
**Slide count:** ориентир **~45** (s01–s45 + suffix-ID `sNNa` для structural-правок после GATE-A, cascade-safe).
**Дата:** 2026-09-06 · **Phase:** Phase 1 → critique → USER GATE 0 → Phase 2 chapter.
**Tone:** инженерно-аналитический, anti-hype, уверенный (memory `confident-tone-no-apologies`). Тезис: ***когда сборка почти бесплатна, дефицитный навык — отличать сигнал от шума и удерживать намерение + суждение на человеке.***

**Research source-of-truth:** `notes/research/lecture-5-pdlc/` (6 досье + `99-synthesis-and-plan.md`).

---

## Changelog v1 → v2 (Phase 1 critique: methodology-critic REVISE + reader-text-only REVISE, 2026-09-06)

Обе критики — REVISE (не концепт, а структурные gap'ы, фиксятся до Phase 2). Применённые правки:

- **[meth-P0-1] Честный recount strict-in.** v1 завысил (18/45): s06 — это keystone-ОСЬ (CLAUDE.md явно исключает ось из strict-in), s22/s31/s39/s42 — критерий/синтез без своего кейса. Honest baseline = 13/45 ≈ 29% < floor. **Фикс:** добавлены 3 реальных кейс-слайда (s16b iTutorGroup, s25b NYC MyCity, s42b Just Walk Out «Wizard-of-Oz») → solid **16/48 ≈ 33%** (по минутам ≈ 45%). s06 выведен из bucket. См. пересчёт §5.
- **[meth-P1] Baseline-gaps** (Baseline/Counterfactual Mandate): добавлены знаменатели на видимый слой — Gartner 782 из 3400+ орг (s41); S&P дельта 17%→42% (s41); **Klarna: развернулась ПОЛИТИКА, не объём — продолжили до ~853 FTE-эквивалента через ассистента** (s38, иначе урок искажён); MIT воронка 60→20→5 (s41 уже был).
- **[meth-P1/reader] S4 де-уплотнён.** AI Product Flywheel (s30) → визуал-aside внутри s29 (не отдельная теория); guardrail-метрика определяется НЕ абстрактно в s27, а в s32 на кейсе Facebook MSI.
- **[reader-P1] s06 асимметрия** — добавлен forward-ref «механизмы (Гудхарт, порча прокси) — Р4 s28–s33», чтобы не читалось name-drop.
- **[reader-P1] s08/s09 discovery** — расщеплены: s08 (Cagan 4 риска + Torres), s08b (JTBD + intent loop), s09 (context engineering + reference dataset с intuition+пример на термин). reference dataset inline-define при 1-м употреблении (s08b/s09), не «используется в s09, определён в s29».
- **[reader-P1] s22 CC/CD** — расшифровка «Continuous Calibration / Continuous Development» + **явный контраст с CI/CD** (аудитория знает CI/CD назубок — лучший dual-audience мост).
- **[reader-P1] s21 Сбер-роли** — не список из 5 терминов; 2–3 роли с однофразовым «что делает» (Product Engineer, Platform Engineer, AgentOps), остальное → chapter.
- **[reader-P2] Парные кейсы** (#1+#2, #4+#5, #6+#7, #8+#9) — book-editor обязан ЯВНО контрастировать каждый (не дублировать), не «два про одно».
- **[meth-P1] LO3 sign-off:** course-curator подтверждает переинтерпретацию LO3 (finance «безопасность данных» → governance/guardrails/drift) ДО Phase 2 — вынесено owner/curator-решением (§3), не self-flag.
- **[meth-P2] Hero:** s02 (cover) + s45 (закрытие) — hero ≥40% area (было не отмечено на s45).

Slide count v1 ~45 → **v2 ~48** (+s08b, +s16b, +s25b, +s42b; s30 свёрнут в s29). Suffix-ID cascade-safe.

---

## 0. Owner-решения (зафиксированы 2026-09-06, до GATE 0)

1. **Слот — заменить lec-05** (finance/retail → archive/ или др. слот, отдельный follow-up; НЕ удалять молча, бэкап + owner-go перед перезаписью артефактов).
2. **Ось — петля + асимметрия** (discovery-first отклонена).
3. **Сбер — наравне с мировыми**, распределён по фазам, без флагман-блока; критика Сбера (удалённые v1-цифры) = урок про калибровку в Р6.

---

## 1. Контекст и зависимости

### 1.1 Промис из Л4 — выполняется и расширяется
Л4 применила ось «фазы SDLC × методика» к жизненному циклу **кода**: как AI входит в требования→архитектуру→реализацию→тест→ревью→эксплуатацию, и почему методика (человеко-владеемый артефакт) ведёт, а инструмент вторичен. Л5 делает **zoom-out**: от «как AI пишет код» к «как AI участвует в создании всего ПРОДУКТА» — исследование, дизайн, запуск, измерение, поддержка, governance. Код в Л5 — одна из фаз (самая подешевевшая), не предмет.

### 1.2 Что студент знает / что вводим с нуля

| Тема | Где | Что Л5 делает | Режим |
|---|---|---|---|
| Типы AI, чат/агент/модель/приложение | Л1–Л3 | фундамент | — |
| Галлюцинации, grounding, RAG | Л1/Л3 | применяем к discovery/поддержке | callback 1× |
| AI в цикле разработки ПО (SDLC) | Л4 | контраст: код-цикл ⊂ продукт-цикл; методика-first переносится | явный мост s04 |
| **Петля обратной связи (PDCA/OODA/BML)** | **вводится в Л5** | keystone-ось; «один чертёж, без сговора» | **полноценный ввод** s05 |
| **Продуктовые риски (Cagan 4+1), discovery** | **вводится в Л5** | Value/Usability/Feasibility/Viability + 5-й (этика/галлюцинации) | компактный ввод s08/s10 |
| **evals / reference datasets / drift** | **вводится в Л5** | «юнит-тесты для агента»; offline evals + мониторинг дрейфа | ввод s28–s31 |
| **guardrails / governance / ROI** | **вводится в Л5** | policy-as-code, maturity 0–5, unit-экономика IDP | ввод Р6 |
| A/B-тесты, метрики (AARRR/North Star) | упоминались? нет | компактный ввод как классика измерения | ввод s26/s27 |

### 1.3 Курсовая прогрессия
Л1–Л3 (обзор) → Л4 (SDLC, цикл кода) → **Л5 (PDLC, цикл продукта)** → Л6 (CAD/CAM) → … Парный **Семинар 5**: команды берут учебный AI-продукт и проходят петлю — формулируют намерение/спеку, строят reference dataset из 10–20 примеров, пишут 3 eval'а, определяют guardrail-метрику и точку human-escalation (Apply/Analyze). Лекция готовит навык (Understand/Evaluate), семинар — Apply. Границу держать (не дублировать).

### 1.4 Сквозные темы курса (canon, обязательны)
- **Человек vs AI:** намерение и суждение остаются на человеке; ответственность не делегируется агенту (Air Canada s37). Запуск = «передача контроля», а не финальная точка (Lenny CC/CD).
- **Безопасность/governance:** guardrails как versioned policy-as-code (иначе тихо расходятся с системой); prompt injection на поверхности продукта (Chevy s24); регуляторика (Сбер 152-ФЗ/ЦБ — на видимом слое только направление, детали → chapter).
- **Выбор инструмента (ядро):** на каждой стрелке петли — «AI-first или классика?» Критерий: стоимость стрелки vs доверие к ней. Антипаттерн: «AI-first везде» / «магическая пилюля».

### 1.5 Owner-бриф — карта покрытия
Обе группы аудитории (см. §5 synthesis): практикам — мета-фреймворки, eval/guardrail-инженерия, роли, экономика; «немного программирующим» — петля интуитивна, знаменитые истории держат внимание без кода. Обилие реальных примеров (мир + РФ-Сбер). Мемы-хуки, каждый резолвится в нумерованное утверждение (format-DNA). Глубокая глава ≥30k как Л3/Л4. Стиль слайдов lec-02/03/04.

---

## 2. Центральный вопрос и арка

### 2.1 Центральный вопрос
> **«Когда AI сделал сборку почти бесплатной — что стало настоящим узким местом продукта, и на каких стрелках жизненного цикла AI-first помогает, а на каких вредит?»**

Задаётся s04; keystone-ответ (петля+асимметрия) s05–s06; возвращается на каждой фазе точкой «стоимость↓ или доверие↓?»; закрывается payoff s40–s44 (матрица «фаза × что делает AI со стоимостью/доверием» + «когда НЕ AI-first» + чек-лист).

### 2.2 Несущая ось (keystone — ENFORCED, отдельный слайд s05 в Разделе 0 ДО первого погружения)
> **Продукт — петля: discover → build → measure → learn → decide. AI асимметрично меняет на каждой стрелке две вещи: СТОИМОСТЬ и ДОВЕРИЕ.**

- **s05 = «один чертёж, без сговора»:** Deming (PDCA) · Boyd (OODA) · Ries (Build-Measure-Learn) нарисовали одну петлю. Заголовок про саму петлю (НЕ recap Л4, НЕ защита подхода).
- **s06 = асимметрия:** Build→≈0 (Anthropic недели→часы); Measure/Learn — та же цена, меньше доверия (недетерминизм, порча прокси, закон Гудхарта); Observe/Orient — быстрее, но атакуемо. Payload: дефицит сместился со «сделать» на «понять, правда ли это».

### 2.3 Арка (~48 слайдов, 100 мин + cut-order на ×1.5 материала) — фазы петли

> **v2:** +s08b/+s16b/+s25b/+s42b (Phase-1 critique); s30 свёрнут в s29. Budgets ниже пересчитаны; при переполнении — **cut-order** (первыми режутся, в порядке): s16 (Design Thinking-обзор) → s11 (пример discovery) → s23 (agency-ladder пример) → s36 (сервис-дизайн классика) → s39 (синтез Р5). Failure-слайды и keystone НЕ режутся (держат ≥30% + ось).

| Раздел | Слайды | Бюджет* | Функция |
|---|---|---|---|
| 0. Введение: от кода к продукту | s01–s06 | 10 | Hook-парадокс (build дёшев vs 95% пилотов); cover+roadmap; lecture-map=петля; мост Л4+ЦВ; **keystone петля (s05)** + **асимметрия (s06)** |
| div | s07 | 0.3 | Р1 «Discovery: намерение и исследование» |
| 1. Discovery / намерение | s08–s13 | 15 | классика (Cagan 4 риска, Torres, JTBD); AI-era (intent loop Сбер, context engineering, reference datasets, синт-юзеры); 5-й риск; **провалы: синт-юзеры NN/g #1, IBM Watson #2, фабрик. цитаты #3** |
| div | s14 | 0.3 | Р2 «Design: прототип и безопасность-by-design» |
| 2. Design / прототип | s15–s18 (+s16b) | 11 | мгновенный прототип из намерения; безопасность в MVP; **провалы: iTutorGroup #NEW, Character.AI #4, Grok #5** |
| div | s19 | 0.3 | Р3 «Build / Launch: схлопнутая стрелка» |
| 3. Build / Launch | s20–s25 (+s25b) | 17 | Build→0 (Сбер dual-loop+IDP, Bain continuous flow, EY iron-triangle); запуск = передача контроля (CC/CD vs CI/CD); **провалы: Chevy $1 #6, McDonald's #7, NYC MyCity #NEW** |
| div | s26 | 0.3 | Р4 «Measure / Experiment: стрелка, которой AI снизил доверие» |
| 4. Measure / Experiment (ядро) | s27–s33 | 18 | классика A/B (Kohavi), метрики, guardrail-метрика, закон Гудхарта; AI-era: evals как навык PM (Weil), AI Product Flywheel, offline evals + drift; **провалы: Zillow drift #8, Facebook MSI #9, reward hacking Med-PaLM/Harvey #10** |
| div | s34 | 0.3 | Р5 «Support / Operate: продукт как оркестр» |
| 5. Support / Operate | s35–s39 | 12 | «продукт как оркестр» (тикеты меняют промпты, не код), AgentOps, Guardian Agents (Сбер); **провалы: Air Canada #11, Klarna разворот #12** |
| div | s40 | 0.3 | Р6 «Governance / ROI / когда НЕ надо» |
| 6. Governance / ROI / финал | s41–s45 (+s42b) | 15 | Deloitte operators→orchestrators; Сбер maturity 0–5 + удалённые v1-цифры (урок калибровки); **макро #13: MIT 95% (60→20→5+COI), Gartner >40%, S&P 17→42%; Just Walk Out #NEW**; матрица + чек-лист + мост Л6/Сем5 |
| Буфер | — | 7 | Q&A (s45) |

\* Pacing (честно, v2): raw Σ ≈ 106 активных (+3 новых кейса) — **на ×1.5-материала это норма**; cut-order (см. выше) режет до ~93 активных + 7 буфер = **100**. Финальная per-slide разбивка + фиксация cut'ов — chapter Phase 2 / Pre-GATE B.

---

## 3. Learning Outcomes (Bloom-разводка Лекция ↔ Семинар 5)

| LO | Формулировка (canon РПД слота Л5) | Достижение | Slides | Success-критерий (Лекция) |
|---|---|---|---|---|
| **LO1** (primary) | Классифицировать типы AI-решений, сопоставить с задачами | на каждой фазе — какой подход (AI-first / evals / guardrail / человек) под какую стрелку + матрица | s05–s06, s08–s39, **s41** | **Apply:** по фазе цикла назвать подход + ≥1 причину «почему здесь так» |
| **LO2** | Оценить применимость AI-решения к бизнес-задаче | критерий «когда НЕ AI-first / стоит доверие ниже цены» в каждом разделе | s12,s17,s24,s32,s37,**s42** | **Understand/Apply:** по фазе назвать ≥1 условие, где AI-first вредит |
| **LO3** | Проанализировать риски: безопасность, ограничения, уязвимости | prompt injection продукта, guardrails/policy-as-code, drift, governance/152-ФЗ, ROI-провал | s24,s32,s41,**s43** | **Analyze:** назвать риск + меру (guardrail/eval/human-gate) |
| **LO6** | Выявить типичные ошибки и ограничения AI-систем | 13 провалов по фазам + макро-статистика с оговорками | s12,s17,s24,s32,s37,**s41** | **Understand/Evaluate:** по кейсу распознать фазу-провал + назвать критерий/альтернативу |

**Bloom-граница:** Лекция = Understand/Evaluate (распознать/оценить); **Семинар 5 = Apply/Analyze** (сами проходят петлю на учебном продукте). Не дублировать. course-curator подтверждает LO-canon после смены темы слота.

---

## 4. Slide list (s01–s45; детализируется в chapter)

> Divider-слайды: тип `section_divider`, ~0.3 мин, roadmap-бар (ТОЛЬКО divider+cover — Л2-урок #40) + gold-маркер + 1 нарративная строка-мост + tag «N кейсов · M провала» (БЕЗ минут — No-Timing rule). Все divider'ы — partial→out.

**Раздел 0 — Введение (10 мин):**
- **s01 Hook-парадокс (3, `case_study`, hero ≥40%)** — «Anthropic: код с недель до часов. MIT 2025: ~95% корпоративных gen-AI пилотов — ноль прибыли. Как обе правды одновременно?» Open-Q 30 сек. Число MIT спорно (COI + воронка 60→20→5) — оговорка «разберём в Р6», НЕ подаём как факт. *Payoff — s41. Partial→out (hook).*
- **s02 Cover + roadmap (0.5, `cover`, hero)** — roadmap 0–6.
- **s03 Lecture-map = петля (1, `process`)** — 6 разделов уложены на стрелки петли discover→build→measure→learn→decide.
- **s04 Мост из Л4 + ЦВ (2, `comparison`)** — «Л4: цикл кода. Л5: цикл продукта — код лишь одна, подешевевшая, фаза». ЦВ крупно (§2.1).
- **s05 KEYSTONE: петля, «один чертёж, без сговора» (2, `assertion_visual`)** — Deming/Boyd/Ries → одна петля. Заголовок про петлю. *Несущая ось предъявлена ДО погружения (ENFORCED п.6).*
- **s06 KEYSTONE-2: асимметрия стоимость/доверие (1.5, `assertion_visual`, ОСЬ — НЕ в strict-in)** — Build→0; Measure/Learn меньше доверия; Observe/Orient атакуемо. **Forward-ref:** «почему доверие падает — механизмы (закон Гудхарта, порча прокси, недетерминизм) разберём в Разделе 4 (s28–s33)» — иначе name-drop (reader-P1). Think-pause 20 сек «на какой стрелке вы больше всего доверяете AI зря?»

**Раздел 1 — Discovery / намерение (15 мин):**
- **s07 Divider Р1 (0.3)** — «Discovery: намерение и исследование · 2 фреймворка · 3 провала».
- **s08 Классика: продуктовые риски (2, `assertion_visual`)** [reader-P1 расщепление] — Cagan 4 риска (value/usability/feasibility/viability) — по одной фразе-интуиции на риск + Torres continuous discovery (opportunity-solution tree, «еженедельный контакт с пользователем»). inline-define. *Partial→out (спина).*
- **s08b JTBD + от кода к намерению (2, `process`)** [NEW, reader-P1] — JTBD «milkshake» (нанимаем продукт на работу) 1 примером; intent loop (Fowler «намерение — узкое место»; Сбер — один из игроков). Мост: discovery = верх петли (Observe/Orient). *Partial→out.*
- **s09 AI-era discovery: context engineering + reference dataset (2.5, `process`)** [reader-P1: intuition+пример на термин] — context engineering (инженерия контекста) — 1 пример; **reference dataset (эталонный набор 20–100 примеров, симулирующих пользователя ДО релиза) — inline-define ЗДЕСЬ, при 1-м употреблении** (не в s29); AI-синтез интервью/тикетов за секунды. *Partial→out.*
- **s10 5-й риск: этика/галлюцинации (2, `assertion_visual`, IN-BUCKET, LO6)** — Cagan/Huryn: к 4 рискам добавлен риск галлюцинированных гипотез; критерий «AI-инсайт требует аудита человеком». (Оговорка: сам Cagan относит к Viability — атрибуция в chapter.)
- **s11 Пример: где AI-discovery реально ускоряет (2, `case_study`)** — синтез терабайтов тикетов/интервью, кластеризация болей. Зачем PM: скорость гипотез. *Partial→out.*
- **s12 Провал #1+#2: синт-юзеры и Watson (3, `case_study`, IN-BUCKET, LO2/LO6)** — NN/g: синт-юзеры отчитались 7/7 успешных задач, реальные — 3/7, единообразная сикофантия к плохим идеям; IBM Watson for Oncology: обучен на синт-кейсах MSK, не реальных пациентах, $62M, 0 пролеченных, небезопасная рекомендация. Критерий: high-stakes + малый-N синт-данные ≠ launch-ready; живое интервью > AI-синтез, когда цена ошибки высока. Альт.: реальные интервью + аудит инсайтов. Retrieval 30 сек. *Эталон failure-слайда.*
- **s13 Провал #3: галлюцинированные «исследования» (2, `case_study`, IN-BUCKET, LO6)** — Deloitte Australia $290K возврат за фабрикованные цитаты; MAHA report (7+ выдуманных ссылок, «oaicite»-артефакты) → реальные гос-решения. Критерий: инсайт без верифицируемого первоисточника = не инсайт. Альт.: grounding + human fact-check (навык из Л3/Л4).

**Раздел 2 — Design / прототип (9 мин):**
- **s14 Divider Р2 (0.3)** — «Design: прототип и безопасность-by-design · 2 провала».
- **s15 AI-era: прототип из намерения (2, `process`)** — интерактивные прототипы «на лету» из описания намерения (vs статические Figma/долгие PRD). Скорость дизайн-итерации. *Partial→out.*
- **s16 Классика под давлением: Design Thinking / Double Diamond (2, `comparison`)** — Discover/Define/Develop/Deliver; критика (Natasha Jen — ритуализация); что AI ускоряет, что нельзя проскочить (реальная эмпатия к пользователю). *Partial→out (спина + граница).*
- **s17 Провал #4: Character.AI (2.5, `case_study`, IN-BUCKET, LO3/LO6)** — иск (Sewell Setzer III, 02.2024); safety-фичи ретрофитом только после суда. Критерий: safety-by-design для уязвимых пользователей — в MVP, не патч. Альт.: red-team + guardrails до релиза. Think-pause.
- **s16b Провал #NEW: iTutorGroup hiring-bot (2, `case_study`, IN-BUCKET, LO2/LO6)** [meth-P0: +реальный кейс] — алгоритм найма автоматически отсеивал кандидатов по возрасту (женщины 55+, мужчины 60+); EEOC settlement $365K (2023). Дизайн-фаза: критерий продукта закодировал дискриминацию. Критерий: автоматизация решения о людях требует bias-аудита ДО релиза; «эффективность» не оправдывает незаконный прокси. Альт.: human-review + аудит признаков. *Диверсифицирует Р2 (не только safety-контент).* 
- **s17 → s18** остаются; далее:
- **s18 Провал #5: Grok «MechaHitler» (2, `case_study`, IN-BUCKET, LO3/LO6)** — 07.2025, ~16 часов антисемитного вывода после ослабления модерации. Критерий: ослабление модерации = релиз, требующий того же red-team цикла. Альт.: модерация как versioned policy, не тумблер. **[reader-P2]** book-editor контрастирует с Character.AI (s17): там — safety не заложена в MVP; здесь — safety была и снята релизом. Не дубль.

**Раздел 3 — Build / Launch (15 мин):**
- **s19 Divider Р3 (0.3)** — «Build / Launch: схлопнутая стрелка · 2 провала».
- **s20 Асимметрия в деле: Build→≈0 (2.5, `assertion_visual`)** — Anthropic недели→часы; Bain continuous flow (границы PM↔dev растворяются, «агенты работают лучше, когда процессы перестроены вокруг них»); EY слом «железного треугольника» (скорость+цена+качество). *Partial→out (механизм оси).*
- **s21 Сбер dual-loop + IDP (2.5, `process`)** [reader-P1: роли с пояснением, не список] — Intent Loop (человек, суточный ритм) ∥ Implementation Loop (агенты, минутный) через IDP-платформу. **Макс 3 роли, каждая с однофразовым «что делает»:** Product Engineer (владеет намерением/спекой), Platform Engineer (держит IDP, 1 на 8–12), AgentOps (эксплуатирует агентов). Остальные роли → chapter. Сбер — один из игроков (наравне). *Partial→out.*
- **s22 Запуск = передача контроля: CC/CD vs CI/CD (2.5, `comparison`, граница подхода — upside, LO2)** [reader-P1: расшифровка + контраст с CI/CD] — **CC/CD = Continuous Calibration / Continuous Development** (Reganti & Badam via Lenny), пришедшая на смену привычному **CI/CD**: релизы по уровню agency/control, не по фичам; старт High Control / Low Agency → рост доверия по мере того как traces подтверждают безопасность (agency-ladder Copilot/Cursor). Явный контраст «CI/CD вы знаете — вот что меняется». Критерий: не отдавать агентность раньше, чем логи её оправдали. *Критерий без своего кейса → upside, НЕ headline strict-in.*
- **s23 Пример: agency-ladder на практике (1.5, `case_study`)** — как продукт постепенно «доверяет» агенту больше действий. *Partial→out.*
- **s24 Провал #6: Chevy «$1 Tahoe» (3, `case_study`, IN-BUCKET, LO3/LO6)** — prompt injection на поверхности продукта, разошлось на ~300 дилерских сайтов. Критерий: бизнес-критичный вывод требует детерминированных guardrails, не инструкций в системном промпте. Альт.: жёсткая валидация/rules на критичных действиях. Retrieval 20 сек.
- **s25 Провал #7: McDonald's × IBM drive-thru (2, `case_study`, IN-BUCKET, LO2/LO6)** — 2.5–3 года, 100+ ресторанов, закрыт 06.2024 после вирусных ошибок заказа. Критерий: многолетний пилот, всё ещё вирусно падающий, — структурный сигнал, не «доработка». Альт.: узкий scope + human-fallback. **[reader-P2]** контраст с Chevy (s24): там — мгновенная prompt-injection дыра; здесь — годы «почти работает», но structural fail. Не дубль.
- **s25b Провал #NEW: NYC MyCity chatbot (2, `case_study`, IN-BUCKET, LO3/LO6)** [meth-P0: +реальный кейс] — гос-чат-бот для бизнеса уверенно советовал незаконные действия (увольнять за жалобы, забирать чаевые); журналисты воспроизвели — один и тот же незаконный ответ. Не отозван сразу. Критерий: запуск авторитетного (гос/юр) advice-бота без детерминированной сверки с законом = раздача неверного с печатью доверия. Альт.: grounding в нормативку + дисклеймер + human-review критичных ответов.

**Раздел 4 — Measure / Experiment (18 мин, ядро урока):**
- **s26 Divider Р4 (0.3)** — «Measure / Experiment: стрелка, которой AI снизил доверие · 3 провала».
- **s27 Классика измерения (2.5, `comparison`)** [reader-P1: не перегружать] — A/B (Kohavi, controlled experiments; ловушки: peeking, закон Тваймана; Bing ≈$100M заголовочный тест — НЕ «$300M кнопка»); AARRR / North Star. inline-define. **guardrail-метрику здесь НЕ определять** — она вводится на кейсе Facebook MSI (s32), не абстрактно. *Partial→out (спина).*
- **s28 Почему AI ломает классическое измерение (2.5, `assertion_visual`, IN-BUCKET, LO6)** — вероятностный вывод (тот же вход → разные, оба «верные» ответы) ломает pass/fail-тест и когортную A/B-логику; недетерминизм. Критерий: детерминированные метрики недостаточны для недетерминированной системы.
- **s29 AI-era: evals как навык PM + Flywheel (2.5, `process`)** [meth-P1/reader: s30 свёрнут сюда] — Kevin Weil (OpenAI): «писать evals — базовый навык PM»; offline evals = «юнит-тесты для агента» (reference dataset уже введён в s09 — здесь только «прогоняем на нём»). **AI Product Flywheel — визуал-aside** (Reforge: Success Rate→Trace→Reference→Evals→Monitoring→замкнуть), НЕ отдельная теория. *Partial→out.*
- **s31 Дрейф и мониторинг (1.5, `assertion_visual`, риск — upside, LO3)** — «тихий убийца»: пост-релизный дрейф модели, доверие пользователей падает раньше, чем дашборд. Критерий: непрерывный мониторинг traces + circuit-breaker. *Критерий без своего кейса (кейс — s32 Zillow) → upside, НЕ headline.*
- **s32 Провал #8+#9: Zillow drift + Facebook MSI (3, `case_study`, IN-BUCKET, LO2/LO3/LO6)** — Zillow Offers: модель-дрейф без real-time мониторинга/автостопа, $304–408M списаний, ~2000 (25%) уволены, ≈$80k убытка/дом. Facebook «Meaningful Social Interactions»: оптимизировали engagement-прокси, 0.05% holdout показал +50% скрытия постов — guardrail-метрики не было. Критерий: капитал-committing модели нужен drift-мониторинг + circuit-breaker; A/B нужны guardrail-метрики, не только оптимизируемый прокси. Retrieval 30 сек. *Ядро урока про доверие.*
- **s33 Провал #10: reward hacking / закон Гудхарта (2, `case_study`, IN-BUCKET, LO6)** — Med-PaLM 2 «химия от головной боли» при сдаче лицензионных экзаменов; Harvey AI цитирует несуществующие дела при победе на bar-exam. Критерий: «сдал бенчмарк» ≠ «безопасен в проде»; когда метрика становится целью — перестаёт быть метрикой. Альт.: adversarial evals + reference dataset из реальных краевых случаев.

**Раздел 5 — Support / Operate (12 мин):**
- **s34 Divider Р5 (0.3)** — «Support / Operate: продукт как оркестр · 2 провала».
- **s35 AI-era: продукт как оркестр (2.5, `process`)** — Reforge: PM настраивает систему AI-воркеров + контуры обратной связи; тикеты из поддержки меняют промпты/дообучают, не код; AgentOps; Guardian Agents (Сбер) — агенты, надзирающие за агентами. *Partial→out.*
- **s36 Классика: сервис-дизайн / SLA / эскалация (1.5, `assertion_visual`)** — что не меняется: путь к человеку, ответственность, SLA. *Partial→out (спина).*
- **s37 Провал #11: Air Canada (3, `case_study`, IN-BUCKET, LO2/LO3/LO6)** — трибунал: компания отвечает за ответ чат-бота ($812.02 CAD), защита «бот — отдельное юрлицо» отклонена. Критерий: компания владеет каждым ответом бота, точка. Альт.: детерминированная выборка политики + гарантированный human-escalation. Think-pause 30 сек.
- **s38 Провал #12: Klarna разворот (2.5, `case_study`, IN-BUCKET, LO2/LO6)** — заявляли замену ~700 FTE поддержки → 2025 разворот: снова нанимают людей; CEO: «цена стала слишком доминирующим критерием… качество ниже». **[meth-P1 baseline — критично:] развернулась ПОЛИТИКА, не объём** — ассистент продолжил работать (~853 FTE-эквивалента), но модель сместилась к «AI + человек по выбору клиента», не «AI вместо людей». Иначе урок искажён («AI не работает» — неверно; верно «полная замена без эскалации — провал»). Критерий: augmentation, не замена; гарантированная эскалация на эмоц.-сложном. Альт.: гибрид человек+AI.
- **s39 Синтез Р5 (1.5, `assertion_visual`, IN-BUCKET, LO2)** — поддержка = петля обратной связи продукта: сигнал из эксплуатации меняет намерение (замыкает discover). Критерий человек-обязателен на эмоц./юр./необратимом.

**Раздел 6 — Governance / ROI / финал (13 мин):**
- **s40 Divider Р6 (0.3)** — «Governance / ROI / когда НЕ надо · payoff».
- **s41 Макро-реальность #13 (3, `case_study`, IN-BUCKET, LO6)** [meth-P1: знаменатели на видимый слой] — payoff hook s01: MIT «95% без отдачи» — реальная воронка **60→20→5** (25% успеха среди пилотировавших), COI (авторы продают agentic-AI); RAND «80%» = citation drift (в отчёте нет разбивки — используем как урок, НЕ как цифру); **S&P: 42% сворачивают в 2025 vs 17% в 2024** (дельта — суть); **Gartner: >40% агентных проектов отменят к 2027; лишь 28% use-cases полностью успешны (опрос 782 из 3400+ орг)** `[VFY-day-of]`. Урок: цифры хайпа не переживают калибровку (в т.ч. удалённые v1-цифры Сбера — тот же паттерн). *ЦВ payoff.*
- **s42 Когда НЕ AI-first — по стрелкам петли (2.5, `matrix`, IN-BUCKET, LO2)** — матрица: фаза × что AI делает со стоимостью × что с доверием × когда классика/человек лучше. Нижняя плашка: детерминированная регуляторная/необратимая задача → обычный код/rules; AI добавил бы недетерминизм.
- **s42b Провал #NEW: Amazon Just Walk Out «Wizard-of-Oz» (2, `case_study`, IN-BUCKET, LO3/LO6)** [meth-P0: +реальный кейс, governance/честность] — «полностью AI-магазин» опирался на >1000 ревьюеров в Индии, вручную размечавших покупки; свёрнут 2024. Критерий: «AI» с скрытым человеческим трудом = провал честности продукта + скрытая unit-экономика; оцени hidden human cost ДО заявления «автоматизировано». Альт.: честный human-in-the-loop + прозрачная экономика. Связка с s41 (цифры/заявления не переживают проверку).
- **s43 Governance: guardrails, роли, экономика (2.5, `assertion_visual`, LO3, SECURITY)** — Deloitte operators→orchestrators (75% меняют операционную модель); guardrails = versioned policy-as-code (иначе дрейф); Сбер maturity 0–5 (сам на L3, не L5), реальная экономика IDP (12–24 мес ROI) `[VFY-day-of]`; 152-ФЗ/ЦБ — направление, детали → chapter. *Partial→out частично; governance-риск in-bucket.*
- **s44 Keystone payoff + чек-лист (2.5, `summary`, LO1/LO6)** — вернуть петлю+асимметрию: сборка бесплатна → дефицит = сигнал/шум + удержание намерения. Чек-лист «прежде чем делать фазу AI-first»: стоит ли доверие цены? есть eval/reference dataset? guardrail-метрика? human-escalation? кто отвечает? governance/PII? *Payoff.*
- **s45 Мост Л6 + Семинар 5 + Q&A (2 + ≤7 буфер, `qa_minimal`, hero ≥40%)** [meth-P2: hero на закрытии] — hero-иллюстрация (bridge к Л6 / замыкание петли); «петля — линза для всех отраслей дальше»; ДЗ Семинар 5 (пройти петлю на учебном продукте). Q&A отдельным beat'ом (Л2-урок #42).

---

## 5. AI-Failure & Judgment ≥30% strict-in (waiver НЕДОСТУПЕН, Решение #82) — honest recount v2

**Определение solid IN-BUCKET (CLAUDE.md, строго):** задокументированный кейс-провал + явный урок + критерий «когда НЕ AI-first» + альтернатива. НЕ засчитываются: keystone-ось (s06), критерий/синтез без своего кейса (s22/s31/s39/s44), однострочные оговорки.

**Solid IN-BUCKET (v2, с кейсом):** s10*, s12, s13, s16b, s17, s18, s24, s25, s25b, s32, s33, s37, s38, s41, s42, s42b = **16/48 ≈ 33%**. (*s10 — 5-й риск: засчитывается только если подан с кейсом галлюцинированной гипотезы + критерий; иначе → upside, не headline.)
**Минутная доля (честная метрика):** solid-IN ≈ 2+3+2+2+2.5+2+3+2+2+3+2+3+2.5+3+2.5+2 = **41 мин / ≈93 активных ≈ 44%**. Сильно ≥30% даже если s10 выпадет (остаётся ~15/48 ≈ 31%, ~39 мин).
**НЕ в bucket (честно):** s06 (ОСЬ — исключена), s22/s31/s39/s44 (критерий/синтез без своего кейса — upside), все divider'ы, cover/recap/примеры/спина-слайды.
**Холистичность / single-cluster (counter-check):** solid по разделам: Р0 — (ось не в счёт) · Р1 s10/s12/s13 · Р2 s16b/s17/s18 · Р3 s24/s25/s25b · Р4 s32/s33 · Р5 s37/s38 · Р6 s41/s42/s42b. **Каждый раздел 1–6 несёт ≥2 solid; ни один не > ~25% веса.** Single-cluster снят by design.
**Запас-мандат:** Phase 3/7/10 methodology-critic пересчитывает по СЛОВАМ/минутам per-artifact; baseline держать на solid ≥33% (не закладывать s10-upside). Урок Л3 (завышенный baseline) учтён.

| Артефакт | In-bucket ядро (named) | Цель strict-in | Контроль |
|---|---|---|---|
| **chapter** | 13 провалов ≥ развёрнутый разбор (урок+критерий+альтернатива) распределены по 6 фазам + deep-dive (асимметрия доверия, evals/Goodhart, guardrails policy-as-code, Сбер-калибровка, MIT-воронка/COI) + блок «когда НЕ AI-first» ≥80 слов × 6 фаз | **≥40%** (ось петли НЕ failure → плотность инженерить намеренно) | methodology-critic Phase 3 (пересчёт по словам, per-part) |
| **slides** | 18 solid strict-in (список выше), assertion-evidence | **≥35% (18/45≈40%)** | methodology-critic Phase 7 (honest recount) |
| **speech** | устный нарратив всех 13 провалов + «когда НЕ AI-first / доверие<цена» ≥50 слов × 6 фаз | **≥35%** | methodology-critic Phase 10 (по минутам speech) |

---

## 6. Glossary lock (черновой; финал Phase 4)
петля обратной связи (feedback loop) · PDCA · OODA · Build-Measure-Learn · **асимметрия стоимость/доверие** (course-scaffold, НЕ в strict-in) · продуктовые риски (4+1 Кагана) · continuous discovery · JTBD · **context engineering** (инженерия контекста) · **reference dataset** (эталонный набор примеров) · синтетические пользователи · intent loop / implementation loop (Сбер) · IDP · **agency/control tradeoff** · CC/CD (continuous calibration & development) · **eval** (оценочная проверка, «юнит-тест агента») · AI Product Flywheel · **model drift** (дрейф модели) · guardrail-метрика · **закон Гудхарта / reward hacking** · guardrails / policy-as-code · Guardian Agent · AgentOps · maturity 0–5 · operators→orchestrators.
**Anti-anglicism (RU visible body — memory `russification`):** deploy→развёртывание; trace→трасса/лог; handoff→передача контроля; drift→дрейф; guardrail оставить как термин с RU-глоссом при 1-м упоминании. Deep latin-scan pre-GATE (не только pattern grep).

## 7. Forbidden additions + inline-required

**Forbidden (No Extra Content, без approval):** формулы; код >3 строк на слайде; vendor-числа как незыблемые на видимом слое (→`[VFY]`); MIT «95%» как факт без оговорки воронки/COI; RAND «80.3%» вовсе (citation drift — НЕ использовать как цифру, только как урок про citation drift); «$300M кнопка» приписать Kohavi (это ≈$100M Bing); подача Сбера как флагман/«российский особый путь» (наравне); timing/методология на видимом слое (No-Timing/No-Methodology rule); roadmap-бар на content-слайдах; «Лектору»/«Вы здесь»; `[FACT-CHECK]`/`[VFY]`/`LO[1-9]`/`§X.X`/`→sNN` на видимом слое; «магическая пилюля».

**Inline-required (1-е упоминание):** петля обратной связи, асимметрия стоимость/доверие, продуктовые риски 4+1, context engineering, reference dataset, синтетические пользователи, intent/implementation loop, agency/control tradeoff, CC/CD, eval, model drift, guardrail-метрика, закон Гудхарта/reward hacking, guardrails/policy-as-code, Guardian Agent, maturity 0–5.

## 8. Микро-упражнения / retrieval

| Слайд | Тип | Длит. | Активность |
|---|---|---|---|
| s01 | open Q | 30 сек | «Код дёшев, но 95% пилотов — ноль. Где потерялась ценность?» |
| s06 | think pause | 20 сек | «На какой стрелке петли вы доверяете AI зря?» |
| s12 | think pause | 30 сек | «Синт-юзер сказал "всё отлично". Верить?» |
| s24 | poll | 20 сек | «Бот пообещал машину за $1 — чья ответственность?» |
| s32 | think pause | 30 сек | «Модель дрейфит, дашборд зелёный. Что упадёт первым?» |
| s37 | think pause | 30 сек | «Кто отвечает за ответ чат-бота — вендор, бот или вы?» |
| s44 | apply | 2 мин | прогнать одну фазу своего продукта по чек-листу (Understand/Evaluate; Apply = Сем5) |

≈5–6 мин, включено в §2.3.

## 9. Свежесть (fact-checker; freshness enforced)
`[VFY-day-of]`: все adoption/ROI-цифры Сбер (maturity, IDP-экономика, роли-ratio), Anthropic недели→часы, Bain/EY/Gartner/Deloitte проценты, Gartner «>40% отмен к 2027 / 28% успех», S&P 42%. `[FACT-CHECK]` (single-source/оспорено): MIT «95%» (обязательна оговорка воронки 60→20→5 + COI); RAND «80%» (НЕ как цифра); Klarna «700 FTE»; Facebook MSI 0.05% holdout / +50%; Med-PaLM/Harvey примеры. Стабильные (cite as-is, chapter/notes): Zillow 11.2021 ($304–408M/25%), Air Canada 14.02.2024 ($812.02), Character.AI 02.2024, Grok 07.2025, McDonald's drive-thru 06.2024, Chevy «$1» 12.2023, Deloitte Australia $290K, IBM Watson Oncology, Bing ≈$100M (НЕ «$300M кнопка»). Атрибуция CC/CD = Reganti & Badam (не Lenny сам); 5-й риск = Huryn-синтез (Cagan относит к Viability). GitHub «Test-First AI» не подтверждён — заменить на Forrester (тот же тезис).

## 10. Source-of-truth chain
```
notes/research/lecture-5-pdlc/{00..50}*.md + 99-synthesis-and-plan.md   [research]
notes/lecture-5-review/pdlc/
├── plan-v1.md (ЭТОТ ФАЙЛ — orchestrator draft + self-roast)
├── <дата>-phase1/{methodology-critic.md, reader-text-only.md}
└── final/plan-v2-final.md (после critique + GATE 0 → Phase 2)
library/lectures/lec-05/  ← ⚠ finance/retail; бэкап + owner-go ПЕРЕД перезаписью
├── chapter.md [PRIMARY] + chapter-part2/3.md (≥30k, multi-part) ← derive
├── deck.yaml(+part2) + slides/*.md ← derive
└── speech.md ← derive
```
НЕ путать: старый `notes/lecture-5-review/final/plan-v2-final.md` = finance/retail (архивная тема слота).

## 11. Self-roast (Roast-Before-Implement)
- **Простейшая версия?** 45 слайдов/100 мин — в норме lec-02/03/04. Риск перегруза Р4 (7 слайдов, 5 новых концептов: evals/reference dataset/flywheel/drift/Goodhart). Митигация: reference dataset и eval вводятся вместе (одна идея — «примеры вместо pass/fail»); flywheel — визуал-обзор, не отдельная теория. **critic проверить cognitive load Р4.**
- **Непроверенные зависимости?** Все цифры — вторичные источники (Сбер primary URL падал по TLS). Митигация: тяжёлая `[VFY-day-of]`/`[FACT-CHECK]` разметка §9; fact-checker Phase 3 добывает primary.
- **Владелец каждого нового файла?** plan → orchestrator; chapter → book-editor; deck → presentation-designer; speech → speech-writer. Ок.
- **Изолированы ли рискованные изменения?** Смена темы слота = рискованно; изолировано (finance/retail не трогаем до owner-go; research namespaced `-pdlc`). Ок.
- **Возможный gap:** LO-canon слота Л5 писался под finance/retail (LO3 = «безопасность данных»). Для PDLC LO3 переинтерпретирован как «governance/guardrails/prompt-injection/drift-риски» — маппинг чистый, но **course-curator обязан подтвердить** (флаг в §3).
- **Ось не «всплывает»?** s05/s06 предъявляют петлю+асимметрию в Разделе 0; каждый раздел — стрелка петли. Ок (ENFORCED п.6).

**Status:** v1 draft ready → Phase 1 critique (methodology-critic + reader-text-only) → USER GATE 0.

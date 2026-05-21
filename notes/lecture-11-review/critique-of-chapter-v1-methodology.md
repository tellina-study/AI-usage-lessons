# Methodology Critic Report — Лекция 11 Chapter v1 — 2026-05-21

**VERDICT: REVISE**

Counter-check: 7 P1 issues ⇒ verdict ≠ APPROVE-WITH-POLISH. Forced REVISE. Plus: lec-11 — **intermediate**, owner waiver unavailable (только L1–L3), strict-in DoD applies as P0/REVISE-grade gate. Strict-in доля проходит (~66%), но holistic distribution имеет один thin section, и есть значимые structural issues, которые foreshadow downstream pain в slides+speech, если не закрыть на Phase 3.

---

## Top-line summary

Chapter v1 — структурно крепкая, методически грамотная глава, которая **landed** все шесть P1 правок из Phase 1 critique (worked example Pfizer Vox развёрнут, §4 4 категории + matrix + 5-step + worked example, OEE как cornerstone и сквозная метрика, 3 причины «augmentation, не controller», recount-таблица honest, hero plan documented). Independent strict-in recount даёт **66.4% failure-bucket** (vs self-claim в plan-v2 ~43.5% для лекции в минутах — chapter намного «гуще» по причине того, что academic-reference формат естественно тяготеет к развёрнутым lesson-блокам). Однако глава имеет семь P1 issues, две из которых структурные: (1) **OT/IT divide** mandated как fundamental, но получил ровно **одно** упоминание из пяти insert-points плана (§1.1 bullet #4) — это thin coverage, не fundamental status; (2) **Russification depth** недостаточна — Latin-density narrative density ≥30% в десятках абзацев (англицизмы baseline×19, production×38, audit trail×8, controller×6 и т.д.), включая опечатку «Манfacturing» (русская М + латинское «anufacturing») и непереведённые subheaders «Diffused strategy», «Cloud blunder», «Pivot 2017», «Cultural mismatch», «Demo-to-production gap», «Marketing-driven sales of immature tech», «Generalist vs specialist», «Honest reality check». Это — narrative body, не URL/brand. Деривация slides+speech унаследует drift, если не закрыть здесь. Остальные пять P1 — менее структурные, но carry-forward risk для downstream phases.

---

## P0 issues (BLOCKING — фундаментально мешают Phase 4)

**Нет P0.** Все шесть P1 правок Plan v2 landed концептуально: keystone в §0 до первого погружения с правильным заголовком про ось, hero plan documented, worked example развёрнут (493 слова в §4.3), OEE сквозной, 3 причины «augmentation» explicit, anonymization absolute (0 named institutions), failure-bucket distributed по 5 разделам без single-artifact concentration.

Двинуться к Phase 4 (slides build) можно после P1 fixes на Russification + OT/IT thinness + Russified subheaders.

---

## P1 issues (значимые — должны быть адресованы перед Phase 4)

### P1-1. Russification depth недостаточна (≥30% Latin narrative density в десятках абзацев; явная опечатка «Манfacturing»)

**Что не так.** Per CLAUDE.md anti-anglicism mandate + memory rule `feedback_russification` + lec-08 deep-scan lesson, narrative body должен иметь Latin tokens только в whitelist (brand names, established acronyms с inline gloss, URLs). Pattern-narrow grep по top blacklist даёт: **baseline×19, production×38 (вне brand context), controller×6, audit trail×8, foundation model×4, distribution shift×3, pilot purgatory×7, rolled-back×2, hype×0 (good), workaround×2, gap×3, edge×14, continuous×6, autonomous×14**. Этих токенов **нет в whitelist для narrative body** — это полноценные английские слова с canonical RU-эквивалентами (производство, контроллер, аудит-след, фундаментальная модель, сдвиг распределения, застревание на пилотной стадии, обходное поведение, разрыв, граница сети, непрерывный, автономный).

Дополнительно — **опечатка**: L138 «Манfacturing — не исключение». Это русская «М» + латинское «anufacturing», hybrid character без legitimate cause. Если speech-writer derive из этого fragment'а — слово прочтётся как «Manufacturing», деформирует Russification дальнейшего downstream.

**Subheader-level англицизмы** (особенно видимо в §1.3 GE Predix): bold-маркеры списка «Diffused strategy», «Cloud blunder», «Pivot 2017», «Cultural mismatch» — это не «brand names с inline gloss», а **полноценные английские концептуальные ярлыки** в visible body. Аналогично §1.3 IBM Watson: «Demo-to-production gap», «Marketing-driven sales of immature tech», «Generalist vs specialist». §2.2 PdM: «Honest reality check» как subheader. §3.1: «Pfizer Vox станет worked example в §4.3» — «worked example» в visible body. §3.4: «Что работает / Что не работает» (good RU) сочетается с «Generic audience phrasing OK (anonymization не нарушено)».

**Evidence.** Deep latin-token scan: `https`×70 (OK — URLs), `com`×48 (OK — URLs), но также: `production`×23 (вне URL), `control`×21, `autonomous`×14, `baseline`×14, `edge`×14, `detection`×14, `CFR`×12, `manufacturing`×11, `pilot`×11, `data`×11, `drift`×11, `Step`×11, `Vox`×10 (OK — brand), `automation`×10, `cost`×10, `cloud`×10, `distribution`×10. Whitelist purge: всё что после строки `Vox` — body anglicisms, не brand.

**Why критично.** Lec-08 lesson: producer self-report «0 hits» при deep scan 919 hits → owner reject «трындец! провал» → 3 revision passes wasted. Lec-11 chapter — book-editor self-report «Russification mandate applied» (frontmatter), deep scan показывает significant drift. Speech и slides derive из chapter; англицизмы каскадно усиливаются.

**Recommendation для Phase 4 revision pass.**
1. **Deep latin-token scan + replace-pass** на chapter перед slides build. Каноничные замены:
   - baseline → исходный уровень / опорный показатель / база
   - production (вне brand) → производственная эксплуатация / промышленная эксплуатация
   - controller → контроллер (already RU; в hybrid усиливать)
   - audit trail → аудит-след
   - distribution shift → сдвиг распределения
   - pilot purgatory → застревание на пилотной стадии (RU-canonical уже использован параллельно — drop English)
   - rolled-back → откатил / откат
   - workaround → обходное поведение / обходной путь
   - foundation model → фундаментальная модель (already RU; дроп англ. parens после первого упоминания)
   - autonomous → автономный
   - edge → граница сети / периферия
   - feedback loop → петля обратной связи
2. **Subheader fixes** §1.3 и §1.3 trio: «Diffused strategy» → «Размытая стратегия», «Cloud blunder» → «Облачная авантюра», «Pivot 2017» → «Разворот 2017», «Cultural mismatch» → «Культурный разрыв», «Demo-to-production gap» → «Разрыв между демо и эксплуатацией», «Marketing-driven sales of immature tech» → «Маркетинг-driven продажи незрелой технологии» → «Маркетинговые продажи незрелой технологии», «Generalist vs specialist» → «Универсальное vs специализированное», «Honest reality check» → «Честная сверка с реальностью».
3. **Опечатка L138** «Манfacturing» → «Производство — не исключение». Mandatory P1 fix.
4. **Keep-list rationale**: «pilot purgatory (англ. оригинал)», «soft sensor (англ.)», «edge AI (англ.)» — допускается **только в parens после RU-canonical**, не как самостоятельный термин в narrative. Lec-08 lesson.

### P1-2. OT/IT divide получил один thin bullet вместо fundamental status

**Что не так.** Plan v2 P1-5 mandated OT/IT divide как fundamental с insert-points §1.1 + §4.2. Chapter v1 имеет **одно** упоминание — bullet #4 в §1.1 pilot-purgatory root causes: «Operational technology (PLC, SCADA, детерминированные циклы) и Information technology (облако, AI, eventually-consistent системы) — это разные миры по культуре, цикле обновлений, требованиям к безопасности. AI приходит из IT в OT и упирается в этот раскол. Этот фундаментальный structural divide объясняет половину pilot-purgatory.» 3 строки в bullet — это **mention, не fundamental**.

Plan v2 строка 132: «**NEW: OT/IT раскол** (30 сек) — фундаментальный structural divide... AI приходит из IT в OT и упирается в этот раскол. Готовит §3.4 регуляторные блокеры.» Plan мандировал structural anchor + connection к §3.4 регуляторике. Chapter §3.4 (Регуляторный ландшафт) **не возвращается** к OT/IT divide. Связь FDA Part 11 / ATEX / Указ 250 → OT/IT (cloud AI vs on-premise edge, eventually-consistent vs deterministic, audit trail across OT/IT boundary) **не делается explicit**.

**Why критично.** Per Missing-Fundamentals Check: один из 5 mandated fundamentals имеет thin coverage. Студент уносит «OT/IT — это абстрактный фактор pilot-purgatory», не «OT/IT — это lens, через который читается вся регуляторика и edge AI architecture». §3.3 «детерминизм edge-вывода» **должен** связаться с OT/IT explicitly (PLC = OT, edge ML coprocessor = OT-side, cloud LLM = IT) — связи нет.

**Recommendation.** Phase 4 chapter revision pass:
1. **§3.3** — добавить 60-80 слов на «OT/IT lens на edge AI»: «POSCO архитектура работает в OT-side: PLC + edge ML coprocessor — оба deterministic, traceable, on-premise. Cloud AI — IT-side: eventually-consistent, network-dependent, не вписывается в OT timing budget. Это **OT/IT раскол на архитектурном уровне**.»
2. **§3.4** — добавить opening sentence: «Регуляторика FDA Part 11 / ATEX / Указ 250 — это формализация OT/IT раскола: audit trail OT-side, AI-обработка IT-side, и регулятор требует traceability across boundary. Black-box ML на IT-side не даёт чистый audit trail для OT-side decision.»
3. Альтернатива (если §3 уже плотная) — **§4.1 категория C (Регуляторика)** добавить explicit ссылку «Каждый критерий категории C — это формулировка OT/IT раскола в регуляторных терминах».

### P1-3. §1.3 trio collapses имеет 3 непереведённых subheader-блока (методический drift, не только Russification)

**Что не так.** §1.3 — strict-in canonical block с 3 кейсами × 3 урока каждый. Уроки сформулированы английскими subheader-фразами: GE Predix — «Diffused strategy», «Cloud blunder», «Pivot 2017» — это **методические якоря** для read-out-loud формул, как «CV — последняя линия защиты, не первая» в §2.5. Read-out-loud formula должна быть на языке аудитории, иначе студент не запоминает и не использует. «Diffused strategy» как memorable phrase для российского инженера — слабее, чем «Размытая стратегия» или «Быть всем для всех».

**Связано с P1-1**, но методически отдельная проблема: это не «один из многих англицизмов в narrative», это **read-out-loud formulae**, которые должны быть memorable RU-фразами.

**Why критично.** Бэк-эффект на slides: presentation-designer возьмёт subheader как slide-title. Если subheader = «Diffused strategy», slide title = «Diffused strategy» — это leak англицизма в visible body на slide. Lec-08 lesson: visible body anglicisms → owner reject.

**Recommendation.** Phase 4 revision: 9 subheader-фраз в §1.3 (3 × 3 урока) → RU read-out-loud формулы. Например:
- GE Predix: «Размытая стратегия» / «Облачная авантюра» / «Поздний разворот»
- IBM Watson: «Разрыв между демо и эксплуатацией» / «Продажа незрелой технологии под маркетингом» / «Универсальное vs специализированное»
- Foxconn WI: «Политика + AI-buzzwords ≠ жизнеспособность» / «"AI-завод" как marketing-shield» / «"Восьмое чудо света" — анти-сигнал»

### P1-4. §4.3 worked example Pfizer Vox имеет 4 «Pass» без проблемного шага → демонстрация не учит «когда не работает»

**Что не так.** §4.3 worked example прогоняет Pfizer Vox через 4 категории и Step 4-5, и получает **все pass**. Lesson сформулирован: «5-step framework работает ретроспективно» + counter-example hypothetical autonomous batch (короткий параграф). Это — **демонстрация пройдённого кейса**, не **демонстрация рамки как фильтра**.

Plan v2 P1-1 worked example был мандирован «Pfizer Vox ретроспективно через рамку» — landed. Но методически рамка показывает свою ценность, когда **отсекает неподходящий случай**. 4 pass подряд — это «AI here makes sense, of course Pfizer applied AI» — студент уходит с впечатлением «рамка валидирует решение, которое уже сделано».

Counter-example в §4.3 («Hypothetical: Pfizer попробовал autonomous batch release без HITL → провал на Step 3 категория C») — это **3 строки**, не развёрнутый second-pass. Plan v2 не мандировал second worked example, но методически он нужен для LO8 Apply+Create.

**Evidence.** §4.3 — 493 слова, из них 3 строки на counter-example (≈30 слов = 6%). §4.5 self-check Q3 ставит hypothetical «AI for autonomous control давления в Zone 0 реактора» — это **правильный** вопрос, но **не worked**.

**Why критично.** Bloom Apply+Create требует студенту самостоятельно применить рамку. Если worked example — это «4 pass + 3-строчный counter», студент не видит, как именно отсекается кейс. Self-check Q3 — это для упражнения, не для демонстрации.

**Recommendation.** Phase 4 revision: расширить counter-example в §4.3 до **second mini-worked-example** (~150-200 слов): «Hypothetical: Завод-производитель аккумуляторов хочет AI-PdM на их battery formation cells (MTBF 8 лет, defect rate 0.1%, FP cost = остановка линии = $500K/час, SIL 2 safety). Apply рамка:
- Step 1: дискретное (assembly).
- Step 2: alternatives — preventive maintenance + CBM + SPC.
- Step 3 categories: A. Данные ✗ MTBF 8 лет → 1 событие отказа / 8 лет / cell = недостаточная выборка. B. Стоимость ✗ FP cost $500K/час → катастрофическая асимметрия. C. Регуляторика ⚠ SIL 2 → ML certification сложнее. D. Человек ✓.
- **Останов на Step 3 категория A (Данные).** AI-PdM не подходит. Alternative: CBM + preventive по графику.»
Этот second example **завершает рамку как фильтр**, не валидатор.

Альтернатива: оставить §4.3 как есть + развернуть §4.5 Q3 в Q&A backup как worked answer (вместо краткого).

### P1-5. AB InBev «rolled-back несколько AI-инициатив» — claim без verifiable source, помечен FACT-CHECK, но **используется как урок в strict-in section**

**Что не так.** §3.6 «Культурный провал — AB InBev и Toyota» строит strict-in lesson: «AB InBev откатил несколько AI-инициатив на цеховом уровне из-за недоверия операторов и поведения обхода». Это конкретный claim о rollback и worker-buy-in. Footnote [43] помечен `[FACT-CHECK: AB InBev rolled-back specific case]` — book-editor честно признаёт unverified.

Strict-in lesson требует documented failure + lesson. Если конкретный rollback **не verified**, мы либо имеем (a) anecdotal generic-pattern без specific case = partial credit, не strict-in; либо (b) factual claim с FACT-CHECK gate = pending verification.

**Why критично.** §3.6 — это failure-bucket bridge для культурного слоя. Если AB InBev rollback не подтверждается в Phase 3 fact-checker pass, lesson нужно либо переформулировать (как generic-pattern по research literature), либо заменить на documented case. Methodology-critic не должен полагаться на unverified claims для strict-in credit.

**Recommendation.** Phase 4 (after fact-checker pass на Phase 3):
1. **Если fact-checker confirms** rollback (research/04 §1 trio collapses может иметь supporting evidence) — оставить как есть, drop FACT-CHECK marker.
2. **Если не confirms** — переформулировать §3.6 culture-frame: drop AB InBev specific, replace с documented worker-buy-in pattern: «Foxconn 80% configuration self-claim (§2.3) принимается без worker-feedback — это reporter pattern, не proof adoption. Toyota контр-pattern (§2.3) ставит worker-buy-in в центр.» Это shifts strict-in lesson на documented case (Foxconn LO2 hook), сохраняет culture-frame.

### P1-6. F-35 ALIS callback — 1 строка по plan, в chapter — short paragraph, но **дублирует** содержание lec-09

**Что не так.** Plan v2 мандировал F-35 ALIS как «сокращён до 1 строки per reader-feedback #5» — в speech / slides 1 строка. В chapter v1 §3.3 ALIS callback занимает **полный параграф** (5 строк, 80 слов) с повторением «44 000 долларов за лётный час, заменён на ODIN, частота ложных срабатываний» — это **дублирование** lec-09 §3.2 (mission-critical PdM).

**Why критично.** Chapter — academic reference, поэтому more verbose чем speech — это естественно. Но повторение lec-09 specific numbers + lesson нарушает **overlap-minimization** между лекциями. Студент, читающий chapter после lec-09 chapter, видит повтор. Лучше: «помните ALIS (lec-09 §3.2): 44 000 долларов за лётный час → ODIN; гражданское PdM учит тому же» — 1 строка с ref-callback, не re-derivation.

**Recommendation.** Phase 4 — сжать §3.3 ALIS callback с 80 слов до 25-30: «Помните F-35 ALIS из Лекции 9 (44 000 долларов за лётный час, false-positive rate подорвал доверие): гражданское прогностическое обслуживание учит тому же — обратная связь должна быть быстрой, эталонная разметка доступна, стоимость FP ≤ стоимости FN.»

### P1-7. Q&A backup количество — 10 вопросов, **больше**, чем мандировано (8); один (Q9 «маленький завод») заходит на curriculum drift к управленческой теме

**Что не так.** Plan v2 §5.3 Q&A — «2-3 мин Типичные вопросы». Chapter §Q&A — 10 вопросов на 634 слова. Q1-Q8 — на тему лекции. **Q9** («А если завод маленький, и у нас один PLC и три HMI») — это **управленческий decision-support вопрос** (sizing, ROI), не методический вопрос на материал лекции. **Q10** («Что точно НЕ автоматизировать AI'ем в производстве 2026») — overlap с §4 + §5.1 callback. По plan'у Q&A backup имеет другую функцию — bridge для нестандартных вопросов студентов, не повторение material.

Self-report task spec говорит «10 вопросов» — book-editor добавил Q9 + Q10. Это **scope creep**, не critical issue, но Q9 — slightly off-topic.

**Why критично.** Q9 — это пример «AI-skepticism reflected» (хорошо), но curriculum-relevance check: для intermediate-lecture (L4-L12) about manufacturing, **«Apply» Bloom level** на «sizing decision» — это **management** material, не engineering. Q9 может остаться, но methodically он **soft-target**.

**Recommendation.** Phase 4 polish: оставить Q9 (small-plant scenario — реальный для junior engineer), но переформулировать ответ на engineering-judgment (а не cost-benefit): «AI на маленьком заводе оправдан, когда (а) собрано 1 000+ labeled examples за разумное время, (б) есть OEE-baseline, (в) операторы готовы валидировать рекомендации. Без этих условий — SPC + Six Sigma даст 70-80% эффекта за on-order-of-magnitude меньшей complexity.» Это shifts на engineering criteria.

Альтернатива: drop Q9, оставить 9 вопросов. Решение — owner choice.

---

## P2 issues (polish — carry-forward в Phase 4)

### P2-1. §3.5 КАМАЗ упомянут как «отдельный кейс на пересечении дискретного и процессного» — но автономные грузовики **не** в этом пересечении

КАМАЗ автономные грузовики Level-3 ADAS — это **продукт автопроизводителя**, не AI на производственной линии. §3.5 явно says так («это не про AI на производственной линии, а про автономный продукт»), но **тогда зачем он в §3 chapter про процессное производство**? Это curriculum drift. Recommendation: drop из §3, упомянуть в Q&A backup Q5 как пример «public-verifiable adoption в РФ» — там он уже есть.

### P2-2. §0.2 глоссарий «6 must-know × 2 колонки» — chapter включает **6 терминов** (ISA-95, PLC, SCADA, MES, OEE, soft sensor)

Plan v2 §0.4 мандировал 6 must-know × 2 колонки. Chapter §0.2 имеет именно 6 + строка «остальные acronyms (CV, PdM, RL, MPC, FDA, ATEX, КИИ) раскрываются inline». Принимается, **но**: SPC, DOE, RCM, CBM, PINN, CIRL — fundamental concepts §4, и они **тоже** не в glossary. Inline gloss работает, если впервые упомянуто в §4 chapter — но для slide-of-the-day чтения students могут пропустить. Recommendation: в speaker notes к §4 slides — explicit inline gloss для SPC/DOE/RCM/CBM.

### P2-3. §1.2 «структурный мегапровал» — Honeywell aviation MRO упомянут как roadmap, без specific status

§1.2 строка 159: «GE Aerospace и Honeywell обсуждают подобные модели для aviation MRO». «Обсуждают» — vague. Это **rumor-level claim**. Если verifiable — добавить date + source. Если не — drop. Lec-08 lesson on freshness.

### P2-4. §3.2 mermaid diagram CIRL — chapter включает mermaid syntax в код-блоке, **но** chapter — academic reference, не slide draft

Mermaid raw syntax (строки 365-374) в chapter body — это **scaffold для slides**, не readable text. Студент, читающий chapter PDF/Google Doc, увидит сырой ASCII tree. Recommendation: либо (a) render mermaid → PNG embedded в chapter; либо (b) replace mermaid raw на text-description ASCII-art или structured prose; либо (c) move mermaid в slide spec, замените в chapter на text-description.

### P2-5. §4.2 матрица альтернатив — таблица в Markdown без visualization

§4.2 содержит 6×5 markdown table. Принимается для chapter (academic reference), **но**: slides будут rendering этой таблицы как 6×5 grid — это много текста. Slide-design issue, не chapter-issue. Recommendation: в speech-writer brief explicit «§4.2 матрица — slide rendering как 2D-grid с iconographic markers, не raw table».

---

## Failure-bucket strict-in independent recount

**Self-claim (plan v2 §300):** ~43.5% strict-in для лекции (минуты).

**Independent recount (chapter words):** 

| Раздел | Words | Strict-in | Partial | Out | % Strict-in |
|---|---|---|---|---|---|
| Преамбула + LO | 236 | 0 | 165 | 71 | 0% (LO = partial credit) |
| Введение «Две отмены Tesla» | 395 | 395 | 0 | 0 | **100%** (canonical strict-in: Tesla 2018+2024 + GE+IBM+Foxconn WI + statistics + central question) |
| §0 (Keystone + glossary + roadmap) | 682 | 0 | 260 | 422 | **0%** strict-in; keystone — failure-метки = partial |
| §1 (Adoption + foundation + trio) | 1635 | 1579 | 0 | 56 | **96.6%** (canonical strict-in каждая subsection) |
| §2 (Дискретное) | 2077 | 1691 | 333 | 53 | **81.4%** strict-in |
| §3 (Процессное) | 2094 | 1133 | 478 | 83 | **54.1%** strict-in |
| §4 (Рамка решения) | 1572 | 1517 | 0 | 55 | **96.5%** strict-in |
| §5 (Замыкание) | 501 | 328 | 0 | 173 | **65.5%** strict-in |
| Q&A backup | 634 | 634 | 0 | 0 | **100%** (10 questions answered с explicit limits, alternatives, architectural choices) |
| Источники | 874 | 0 | 0 | 874 | 0% |
| Оглавление | 259 | 0 | 0 | 259 | 0% |
| **TOTAL** | **10959** | **7277** | **1636** | **2046** | **66.4% strict-in** |

**Sampled paragraphs (per spec — 5-7 random):**

1. **§1.2 «Critical boundary»** (lines 162-171, ~250 words) — **strict-in**. 3 fundamental reasons (latency / hallucinations / certification) с physics-grounded mechanism + architectural class distinction (decision-support vs autonomous controller) + LO7 mapping. Canonical.

2. **§2.4 «Корневая причина IMD»** (lines 290-294, ~95 words) — **strict-in**. Tesla 2018: «zones of variability — feature, не bug» + automation paradox (Bainbridge 1983) + Jidoka alternative + Hard rule. Full strict-in.

3. **§3.4 «FDA 21 CFR Part 11»** (lines 425-440, ~280 words) — **strict-in**. «Что работает / Что не работает / Что дополнительно требуется» — explicit boundary с lesson + GAMP®5 / XAI alternatives + audit trail mandate.

4. **§3.5 «КАМАЗ»** (lines 457, ~80 words) — **out / partial**. Curriculum drift; описание без failure-lesson.

5. **§4.1 «B. Асимметрия стоимости»** (lines 498-502, ~135 words) — **strict-in**. 2 criteria + 2 alternatives (SPC, RCM, PLC, formal verification). Compact strict-in.

6. **§5.1 «Explicit failure-callback»** (lines 618, ~120 words) — **strict-in**. «95% пилотов не доходят до production не потому что AI плох, а потому что инженеры не задают эти вопросы» — это explicit judgment с alternative path.

7. **§2.3 «Toyota культурная позиция»** (lines 270-271, ~150 words) — **strict-in subset**. Toyota Jidoka 2.0 vs Foxconn replacement narrative — culture-frame с explicit anti-thesis.

**Holistic check (per CLAUDE.md mandate ≥30% per artifact).** Chapter v1: **66.4%** strict-in. **Passes** with margin ~36 п.п. Distributed по 5 разделам: min §0 = 0% (preamble), min content-§ = §3 54%, max = §1 96.6% и §4 96.5%. **§0 thin** (0%) — единственный thin section; объяснимо: §0 — это keystone + glossary + roadmap, концептуально meta-section, не deep-dive. **Принимается.**

**Counter-flag:** Self-claim в plan v2 был 43.5% для **лекции минутами**. Chapter words → 66.4%. Расхождение объяснимо (chapter формат естественно verbose в lesson-блоках), не «inflated self-report». **Honest.**

**Verdict:** ≥30% mandate **met**, holistic distribution **OK** (с пометкой §0 = 0% — acceptable для meta-section). Single-artifact concentration — нет.

---

## Keystone consistency assessment

**Verdict:** Keystone consistently anchored. ✓

**Pass criteria checked:**
- [x] Keystone predстаvлен в **§0 ДО первого погружения** (§0.1 line 95-105).
- [x] Заголовок «Keystone: две модели производства» — про **саму ось**, не про устройство курса / защиту подхода / recap. ✓
- [x] Belt declared one concept: «застревание на пилотной стадии универсально: 78% / 5.5%» — strict ONE-concept belt per plan v2 P1-1 keystone-belt-cram fix. ✓
- [x] **§2 opening line 205**: «Дискретное производство — левая колонна нашего keystone» — explicit reference.
- [x] **§3 opening line 336**: «Процессное производство — правая колонна keystone» — explicit reference.
- [x] **§4.3 worked example Step 1**: «Колонна правая в нашем keystone» — explicit.
- [x] **§5.1 recap** ось разбита на 3 уровня (discrete / process / общее) — explicit closing callback.
- [x] **No structural copy of lec-09 OODA**: лекция-11 keystone — vertical taxonomy of production types; lec-09 — horizontal stage-chain (OODA). Different mental object. ✓

**Minor concern (P2-level):** **§5.3 bridge к Лекции 12** — заявляет «другая лекция» о digital twins, но не возвращает к keystone discrete/process explicitly. Студент уносит «keystone Лекции 11 — production types» + «keystone Лекции 12 — digital twins», без connection. Может быть улучшено в speech (1 строка на «keystone Лекции 11 + 12 сшиваются: цифровой двойник применим к обеим колоннам, но иначе»).

---

## Missing fundamentals check (5 mandated — per Plan v2 P1-5)

| Fundamental | Plan insert-points | Chapter coverage | Status |
|---|---|---|---|
| **OEE** (Overall Equipment Effectiveness) | §1.1 + §2.2 + §3.4 | §0.2 glossary def + §1.1 «3rd vendor question OEE» + §2.2 «OEE-callback» + §3.4 «OEE-замыкание» + §4.1 «4-й OEE-вопрос» + §5.1 callback + §5.2 «Бонус — OEE-вопрос». **6 insert-points landed.** | ✅ **Deeply covered as cornerstone**. Sequential build + reuse + applicable artifact. Best fundamental of 5. |
| **Эталонная разметка** (ground truth) | §2.1 + §4.1 | §2.1 «(в) Эталонная разметка дорого» + inline gloss + LO8 anchor + §2.6 «дорогая эталонная разметка» + §3.3 «эталонная разметка доступна» + §4.1 криterий A.3 | ✅ **Deeply covered as cornerstone**. Promoted from secondary → main per plan. |
| **OT/IT раскол** (OT/IT divide) | §1.1 + §4.2 | **Только §1.1 bullet #4** (3 строки, 60 слов). Plan мандировал «structural divide» с connection к §3.4. **§3.4 не возвращается** к OT/IT explicitly. | ⚠️ **Thin coverage**. P1-2 above. |
| **Детерминизм edge-вывода** (latency-determinism) | §3.3 | §3.3 «Детерминизм edge-вывода — fundamental concept» + read-out-loud formula «Latency = determinism, не только speed» + 4 reasons edge vs cloud (latency / resilience / bandwidth / privacy) | ✅ **Covered**. Read-out-loud formula explicit. |
| **Стоимость разметки vs объём данных** (label cost vs data volume) | §2.1 + §4.1 | §2.1 «(в) Эталонная разметка — дорого» = «labels требуют domain expert × hours = дорого» + LO8 mention + §4.1 criterion A.3 «defect rate < 1%, дорогие метки» | ✅ **Covered** (intertwined with ground truth). |

**Summary:** 4 из 5 mandated fundamentals — deeply covered. 1 (OT/IT раскол) — thin coverage; P1-2 fix required.

**Nice-to-have additional fundamentals** (per Phase 1 critique):
- Model drift vs distribution shift distinction — **partially covered** (§3.2 «4 conditions RL drift» + §3.6 «distribution drift»; «drift» и «shift» используются как synonyms, что может confused students).
- Anomaly detection vs SPC — **covered implicitly** (§4.2 SPC + §3.1 anomaly detection в Pfizer Vox).
- CBM definition — **inline gloss** в §2.2 («condition-based monitoring (CBM)»).

---

## LO coverage matrix

| LO | Bloom level | Section coverage | Status |
|---|---|---|---|
| **LO1a (Remember)** «два типа производства + 3-4 dominating tools each» | Remember | §0.1 keystone + §2.1-2.3 (discrete: CV, PdM, cobots, copilots) + §3.1-3.3 (process: soft sensors, MPC/RL, edge PdM) | ✅ |
| **LO1b (Apply)** «для кейса определить колонну, AI-стек, структурный риск» | Apply | §4.3 Pfizer Vox worked example Step 1 + §4.5 Q3 self-check + Q&A Q1 | ✅ |
| **LO2 (Evaluate)** «оценить vendor-claim, 3 вопроса» | Evaluate | §1.1 «OEE 3rd question» + §2.3 Foxconn FoxBrain 80% hook + §4.1 «3 уточняющих вопроса + 4-й OEE» + §5.2 «artifact для кармана» | ✅ **Central pedagogical hook**, multiple anchor points |
| **LO7 (Evaluate)** «regulatory landscape + decision support vs autonomous controller» | Evaluate | §1.2 «3 reasons augmentation, not controller» + §3.4 FDA/ATEX/Указ 250 + §4.3 «Архитектура AI = decision-support, не controller» | ✅ **Explicit mapping** per Phase 1 critique requirement |
| **LO8 (Apply+Create)** «≥4 категории критериев + non-AI альтернатива» | Apply+Create | §4 целиком (§4.1 4 категории + §4.2 6 alternatives + §4.3 worked example + §4.4 5-step framework) + §4.5 self-check applies | ✅ **Central payoff**, fully covered |

**LO coverage:** ✅ all 5 LOs covered with explicit anchor points. LO7 (caveat в Phase 1) — теперь **explicit** в §1.2 + §3.4 + §4.3. LO8 — central payoff в §4.

**Bloom level match:** intermediate-lecture (L4-L12) → all 5 LOs соответствуют lecture-level (Apply / Evaluate / Apply+Create — все 3 в acceptable range для intermediate).

---

## Curriculum relevance check

**Lec-11 curriculum slot:** intermediate (L4-L12), Module 2.

**Overlap with prior lectures:**
- **Lec-03** (архитектуры AI-систем) — referenced как prereq для edge AI / foundation models / augmentation-vs-controller. §1.2 строит на lec-03 architecture taxonomy. ✓ Healthy callback.
- **Lec-06** (generative CAD/CAM) — referenced как «AI до производства vs AI в производстве» граница. **Не overlap'ает**: lec-06 — design-stage, lec-11 — production-stage. ✓ Clean boundary.
- **Lec-07** (HITL, FDA, GxP) — referenced в §4.1 «(доказано Toyota, см. lec-7 HITL)». ✓ One-line callback, не deep-dive.
- **Lec-09** (mission-critical AI, OODA, F-35 ALIS) — F-35 ALIS callback в §3.3 — see P1-6 above (80 слов вместо 1 строки). ⚠️ Minor overlap.

**Foreshadow к будущим лекциям:**
- **Lec-12** (digital twins) — §5.3 bridge + §0.2 ГОСТ Р 57700.37-2021 foreshadow + §3.5 Holcim cement digital twin **leave at boundary**, не deep-dive. ✓
- **Lec-13** (supply chain AI) — §5.3 «четвёртая колонна, которую мы упомянем, но не разворачиваем». ✓

**Curriculum drift candidates:**
- **§3.5 КАМАЗ autonomous trucks** — это автомобильный продукт (overlap с lec-06 или standalone «AI-products», не lec-11 manufacturing). **Drop рекомендуется** (P2-1 above).
- **Q&A Q9 «маленький завод»** — soft management territory, не engineering. См. P1-7.

**Verdict:** Curriculum relevance — strong. Minor drift в §3.5 КАМАЗ и Q9 — adjustable.

---

## Length & pacing reality check

- **11 350 слов** — comfortably в plan target 10-12k.
- 5 sections + Q&A + Sources + LO + Оглавление — все present, all required parts.
- Self-check questions: §1.4 (3 Q), §2.7 (3 Q), §3.7 (4 Q), §4.5 (3 Q) — **4 self-check blocks**, 13 questions. Adequate для 5 разделов (один self-check на каждый кроме §0 и §5; §0 — meta, §5 — closure — это acceptable).
- ~30-45 страниц A4 = 30-60 мин self-study read = adequate для 75-мин лекции backing. ✓
- §1 (1635 words), §2 (2077), §3 (2094), §4 (1572) — balanced, нет overflow.
- Q&A 634 слов = 10 questions × ~63 слов / answer = adequate brevity for lecturer-backup.

**Не overload.** ✓

---

## Anti-pattern compliance check

- [x] **No «магическая пилюля»** — 0 hits на promise-tone scan.
- [x] **No «AI спасёт» / революци** — 0 hits.
- [x] **No named institutions** — 0 hits для МГТУ / ИУ6 / Бауман / кафедра.
- [x] **No insider phrasing** «рабочее определение» / «прикладное X» — 0 hits.
- [x] **No designer-extras** «Лектору» / «Вы здесь» / тайминг — 0 hits.
- [ ] **Anti-anglicism mandate** — **VIOLATED** (P1-1, P1-3).
- [x] **Anonymization absolute** — confirmed.
- [x] **`[VFY-day-of]` markers** — 11 hits, all on volatile claims (statistics, market estimates, recent product releases). Adequate.
- [x] **`[FACT-CHECK]` markers** — 4 hits: Deloitte 2025 survey (footnote [11]), Tata rollback (footnote [24]), Указ 250 ссылка (footnote [38]), AB InBev rollback (footnote [43]). Adequate honesty; fact-checker pass needed in Phase 3.

**Verdict:** Anti-pattern compliance — strong except Russification (P1-1, P1-3).

---

## Recommendations for Phase 4 revision

### Carry-forward (what's good — keep as is)

1. **Keystone consistency** — Variant C anchored across §0/§2/§3/§4.3/§5.1. ✓ Lock.
2. **§4 worked example Pfizer Vox** (493 words) — central LO8 payoff, well-developed. Keep + add second mini-example for «когда не работает» (P1-4).
3. **OEE как сквозная метрика** — 6 anchor points, applicable artifact для LO2. Best-executed fundamental. ✓ Lock.
4. **Эталонная разметка** promoted к cornerstone — landed правильно. ✓ Lock.
5. **3 причины augmentation, не controller** (§1.2) — physics-grounded, explicit. ✓ Lock.
6. **5-step framework** (§4.4) + worked example (§4.3) — applicable, не recitation. ✓ Lock.
7. **Failure-bucket distribution** (66.4% strict-in) — passes ≥30% margin comfortably; holistic. ✓ Lock.
8. **Anonymization absolute** — 0 violations. ✓ Lock.
9. **LO coverage matrix** — все 5 LO explicit-mapped. ✓ Lock.
10. **Hero plan + 6-tier acquisition** documented в plan-v2 mandates carry-forward checklist. ✓ Carry to Phase 4.

### Fix before Phase 4 (P1 — required)

1. **P1-1. Russification depth.** Deep latin-token scan + replace-pass на narrative body (≥30% Latin density abzace должны → ≤10%). Опечатка «Манfacturing» (P1) mandatory fix. Critical anglicism count target: <20 occurrences для top blacklist (baseline / production / controller / audit trail / pilot purgatory / etc.) в visible body.
2. **P1-2. OT/IT divide.** §3.3 + §3.4 — добавить 60-80 слов explicit connection «OT-side архитектура (PLC + edge ML) vs IT-side (cloud LLM); регуляторика — formalization OT/IT раскола». OT/IT mention count: 1 → ≥3 anchor-points.
3. **P1-3. §1.3 subheader Russification.** 9 subheader-фраз в GE Predix / IBM Watson / Foxconn WI → RU read-out-loud формулы.
4. **P1-4. §4.3 worked example.** Расширить counter-example до ~150-200 слов **second mini-worked-example** где рамка **отсекает** кейс (battery PdM, MTBF 8 лет, SIL 2 → fail на Step 3.A).
5. **P1-5. AB InBev rollback claim** — pending Phase 3 fact-checker pass. Если не verified — переформулировать §3.6 culture-frame на documented case (Foxconn 80% + Toyota counter).
6. **P1-6. §3.3 ALIS callback** — сжать 80 слов → 25-30, one-line с ref-callback к lec-09 §3.2.
7. **P1-7. Q&A backup Q9** — adjust answer на engineering-judgment criteria, не management cost-benefit. Or drop.

### Polish (P2 — optional, carry-forward acceptable)

- **P2-1.** §3.5 drop КАМАЗ или move to Q&A Q5 (where it's already mentioned).
- **P2-2.** SPC/DOE/RCM/CBM glossary — добавить inline gloss в speaker notes к §4 slides.
- **P2-3.** §1.2 «Honeywell aviation MRO обсуждают» — verify or drop.
- **P2-4.** §3.2 mermaid CIRL — replace raw mermaid в chapter на text-description; mermaid moves to slide spec.
- **P2-5.** §4.2 матрица — brief в speech-writer для 2D-grid rendering.

### Cascade-of-changes warning

Russification fixes (P1-1, P1-3) must cascade to:
- `library/lectures/lec-11/slides/*.md` headers и body when generated (Phase 4 slides build).
- `library/lectures/lec-11/speech.md` derivation (Phase 9 speech-write).
- Subheader-фразы используются как slide titles → если remain English, leak в visible body → lec-08 owner-reject pattern repeats.

Phase 4 orchestrator должен ensure presentation-designer + speech-writer briefs включают «chapter v2 RU-canonical subheaders как slide titles», не «chapter v1 English subheaders».

---

## Top-3 issues (приоритизировано)

1. **P1-1 + P1-3. Russification depth + subheader-фразы** — критично для downstream slides+speech. Lec-08 lesson cost ~83 мин revision. Address ПЕРЕД Phase 4 slides build, не reactively.
2. **P1-2. OT/IT divide thin** — 1 mention вместо fundamental status. Структурный gap для Missing-Fundamentals check.
3. **P1-4. §4.3 worked example second pass** — LO8 Apply+Create требует рамку как фильтр, не только как валидатор. Counter-example 30 слов → 150-200 слов.

**P1-5, P1-6, P1-7** — менее структурные, lower priority. **P2** — все carry-forward acceptable.

---

**Конец Methodology Critic Report. Verdict REVISE.**

**Next steps:**
1. Orchestrator merges с fact-checker pass + reader-simulator critique-of-chapter-v1.
2. Phase 3.5 — spawn book-editor для chapter v2 turn (P1-1 to P1-7 fixes).
3. Phase 3 re-run methodology-critic on chapter v2 — verify Russification deep-scan + OT/IT coverage + counter-example second worked.
4. USER GATE A — present chapter v2 + critic reports.
5. Phase 4 — slides build на chapter v2 (NOT v1) с RU-canonical subheaders.

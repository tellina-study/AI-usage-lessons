# Presentation Critic Report — Лекция 11 «AI в дискретном и процессном производстве» — slides v1

**VERDICT: REJECT**

**Date:** 2026-05-21  | **Reviewer:** presentation-critic  |  **Issue:** #127  |  **Source:** `library/lectures/lec-11/rendered/snapshots/s-{01..39}.png` (39 PNG, 1334×750)

---

## 1. Top-line summary

Дек структурно собран по правильному lec-09 pattern (cover s02 + lecture-map s03 + glossary mini s04 + keystone s05 + 5 section dividers + dedicated Q&A s38 + 2 hero slides). Failure-bucket strict-in насыщен (~24/39 ≈ 61%). Failure-pattern matrices (s22 + s30) симметричны §2/§3, что pedagogically сильно. Schema-слайды (s09 OT/IT split, s25 CIRL, s32 4 категории, s33 6×5 alternatives matrix, s34 5-step worked example, s35 framework) хорошо читаются.

**Однако: deck НЕ готов к показу.** Три структурных gap'а блокируют production:

1. **Hero structural gap.** s01 = **31% площади** (6.5×4.8 in / 13.33×7.5 in canvas); s39 = **32.5% площади** — оба ниже mandatory ≥40% ([[hero-images-required]]). Designer self-report «≥40% area ✓» неверен. Cost-of-omission lec-08: 1 owner-интервенция.

2. **Deep latin-token scan: 1149 occurrences / 620 unique tokens вне whitelist** в PPTX visible body. Это **превышает Лекцию 8 v1 (224 unique)** в 2.8×. Critical anglicism leak на ~28/39 слайдов. Designer self-report «Russification check: body на русском» — verifiably false; pattern-narrow grep маскировал depth. Cost-of-omission lec-08: 3 revision passes, ~3h.

3. **Designer-extras grep: 15+ hits в visible body** через orchestrator-INDEPENDENT regex. Designer self-report «0 hits» неверен. Hits: `[VFY-day-of]` на s07/s08; `LO1/LO2/LO7/LO8` коды на s02 cover + s08 + s21 + s29 + s32; `§4` cross-refs на s16/s22/s24/s30; `callback s16` на s20; `возвращаемся в разделах 1, 2, 4` на s04. Cost-of-omission lec-04: ~5 циклов.

**Counter-check passed:** 11 P1 issues + 3 P0 → REVISE absolute floor; structural gaps на hero + Russification + designer-extras = REJECT (не «polish», three concurrent structural gaps).

---

## 2. Per-slide visual notes (39 slides)

| # | Slide | 5-sec test | Visual evidence | Notes |
|---|---|---|---|---|
| s01 | Hero Tesla Giga Press | FAIL | Image занимает левую половину ≈31% area. Заголовок «Tesla отступила дважды. Компании не учатся один раз.» + 2 цитаты + central question под изображением | Hero <40%. Image cropped/обрезан в правой части. Attribution мелкий — `Tesla Giga Press · Idra OL 6100 CS · Fremont, 2020 · Wikimedia CC-BY-SA` нечитаем. |
| s02 | Cover | PASS | Декоративная «11» outline + title + LO summary в Ocean rounded box | LO1/LO2/LO7/LO8 коды на body — designer extra. Roadmap-bar сверху корректен. «AI» в title как «AI в дискретном…» — приемлемо в whitelist. |
| s03 | Lecture-map | PASS | 5 крупных section cards с номерами, нумерация 1-5 цветами Ocean → Gold → Navy gradient | Карточки equal-height + одинаковая структура. Sub-label `Раздел 4 — PAYOFF лекции` нормально (highlights central section). |
| s04 | Glossary mini | PASS | 6 терминов × 2 колонки, deep-Ocean badge + description | «возвращаемся в разделах 1, 2, 4» — designer extra (foreshadow scaffold visible). `Cornerstone процессного` в Soft sensor description — анг. |
| s05 | Keystone | PASS | Two columns ДИСКРЕТНОЕ + ПРОЦЕССНОЕ; gold belt снизу с 78%/5,5%/95% | Schema_quadrant compliant. «excessive automation a mistake» в gold belt — quote оставлен на английском под markdown convention. |
| s06 | Section 1 divider | PASS | Декоративная «1» background + 4 точки тематики | «foundation models · трио hype-collapse» — анг. в subtitle. |
| s07 | Adoption gap | PASS visual | Hero 5,5% gold callout + bar chart 95%/80%/42% + 3 источника | **[VFY-day-of] visible** в footer — designer extra. Бар chart Ocean colors correctly. «high performers · EBIT impact >5% от AI» — анг. в callout. |
| s08 | Market estimates | PASS visual | Bar chart 4.5× divergence + Gold callout right | **[VFY-day-of] visible**. «methodology, scope радикально различаются» — анг. в body. Хороший контраст 4.5× — assertion работает. |
| s09 | OT/IT split | FAIL spelling | Two columns OT + IT с 5 параметрами каждая | **«Sertification»** TYPO ×2 в body — должно быть «Сертификация». Critical defect. Также: structural divide, strong, eventually-consistent, audit trail, control loop, output, SaaS-обновления — массовый anglicism leak. |
| s10 | Foundation models | FAIL | Left photo Siemens HQ + right 3 cards «3 причины» | Photo очень крупный (~50% column) — отвлекает от 3 причин справа. Hannover Messe март 2025 — анг. «augmentation, НЕ controller — два разных архитектурных класса» снизу gold. |
| s11 | Tesla Optimus | PASS | Two cards ДЕМО + PRODUCTION (gold) + tagline | «Recurring pattern: capability в контролируемой среде vs reliability 99,9% в неконтролируемой» — массовый anglicism в subtitle. «production-сборке» в body — англицизм. |
| s12 | Hype-collapse trio | PASS | 3 cards с одинаковой structure: company / period / money / lesson | Хороший symmetric layout. «Industrial AI ≠ general cloud AI», «Демо ≠ production», «measured production metrics» — анг. в lesson cards. |
| s13 | Section 2 divider | PASS | Декоративная «2» + 6 тематик | «PdM · коботы · Tesla 2018 · границы» — нормальный mix. |
| s14 | CV inspection cases | PASS | 3 cards (BMW + TSMC + Boeing); TSMC с реальным фото | После iter-2 placeholders заменены на icons. Однако в всех 3 cards bullets на анг: «Bespoke catalogue per vehicle», «Post-door-plug crisis», «Photo-driven part validation», «defect rate 1–2% → class imbalance». TSMC photo маленький (~3.6×1.5 in). |
| s15 | Boeing 737 | PASS | Real photo Alaska Air 737 MAX 9 left + 4-section story right | Strong layout. Bottom callback formula `«CV — последняя линия защиты, не первая. Без upstream sign-off + audit trail AI не починит.»` мощный. Attribution мелкий. |
| s16 | Label cost | PASS | Two columns ДЁШЕВО + ДОРОГО (gold) + альтернативы bottom | **«Первый критерий категории "данные" в §4 — есть ли разметка adequate volume»** — §4 cross-ref + adequate volume англицизм. Class imbalance, Defect rate 1%, Storage — анг. |
| s17 | PdM vs reality | FAIL | Real photo Tata Steel left + vendor claims + McKinsey reality check + OEE callback | Photo маленький (4.2×2.1 in). «VENDOR ОБЕЩАЕТ» / «reactive maintenance» / «MCKINSEY 2025 REALITY CHECK» / «EBIT-impact» — масса англицизмов. Хорошая formula «–25% downtime ≠ +25% OEE». |
| s18 | Cobots Toyota Jidoka | PASS | 3 cards Hyundai-BD + Toyota GAIA + Toyota Jidoka 2.0 с icons | Icons (cog/users/wrench) приемлемые. Однако «Spot для exterior QC», «no data scientists. 10 000 hours saved/year», вся цитата Jidoka на анг. |
| s19 | Tesla 2018 | PASS visual | Гарнирный gold quote callout наверху + 3 cards | Strong. Цитата Маска на англ — оставлено как канонический quote (приемлемо). Однако «automation paradox», «Ironies of Automation», «miles of edge cases», «Production hell», «variability — feature, не bug» — массовый leak. |
| s20 | CV limits | PASS visual | Two columns ГДЕ CV ЛОМАЕТСЯ + АЛЬТЕРНАТИВЫ | «Low-contrast defects», «Scarce defect labels», «Physical signal amplification», «60–70% inspection workloads в controlled env. Validated за неделю», «Hybrid (рекомендуется): Физика → rules → ML» — массовый leak. **«callback s16»** — cross-ref leak. |
| s21 | Foxconn FoxBrain | PASS visual | Полная цитата Liu + 4 вопроса к вендору | Quote Foxconn на анг (приемлемо). Заголовок «80% configuration work — vendor self-claim, не metric» — нужно: «"80% работы по настройке" — заявка вендора, не метрика». **«LO2 hook»** в subtitle — designer extra. |
| s22 | Discrete failure matrix | PASS schema | 2×2 grid с 4 типами провалов + Tesla 2018 + CV модель A→B + Boeing 737 + Foxconn 80% | Solid schema_matrix subtype. Однако: «Scarce labels + class imbalance», «Vendor self-claim без baseline», «physical signal · rules ДО ML», «augment, не replace · Jidoka», «план дообучения · rules-fallback» — анг. **«критериев §4»** — cross-ref leak в subtitle и footer. |
| s23 | Section 3 divider | PASS | Декоративная «3» + 4 тематики | OK. |
| s24 | Soft sensors BASF + Pfizer | PASS visual | Real photo BASF Ludwigshafen left + Pfizer card right | Real photo BASF appropriate. «–30% batch defects | без увеличения тестирования | R&D formulation 18 мес → 3 нед», «GenAI на AWS Bedrock + SageMaker», «+20 000 doses per batch | "Recommend", не autonomous — FDA Part 11 consistent» — массовый leak. **«Pfizer Vox станет worked example в §4»** в footer — §4 cross-ref leak. |
| s25 | MPC RL CIRL | PASS schema | Yokogawa photo left + CIRL architecture mermaid-style diagram right | Solid schema_architecture. Однако: «PID controller (baseline) детерминированный», «Deep RL · учит policy с PID как baseline в loss function», «RL adds value в нелинейных зонах», «Что НЕ есть CIRL: ✗ Не "RL вместо PID" ✗ Не "два контура параллельно"», «MPC dominates process control: Explicit model · объясним · validated · реагирует на drift автоматически», «high-level scheduling. На замыкании контура — MPC» — массовый leak. Schema читается, но текст-на-английском больше, чем по-русски. |
| s26 | RL distribution drift | PASS schema | 2×2 4 механизма + safe-fallback bottom | Strong matrix layout. «Batch transitions», «OOD inputs», «Stale policy», «Seasonal shifts», «Equipment wear», «Дрейф объекта», «RL обучен на steady-state. Переходный режим — out-of-distribution», «Состав сырья меняется. Policy на одном — stale на другом», «Внешняя среда», «Safe-fallback», «MPC mandatory на замыкании контура» — массовый leak. |
| s27 | Edge PdM determinism | PASS visual | Real photo POSCO + latency bar chart 1ms/10ms/300ms | Bar chart effective. «Latency = determinism, не только speed» formula сильна. «F-35 ALIS callback (Лекция 9): $44 000/час, заменён ODIN. Defense PdM учит тому же, что промышленный» — chapter-level callback, но в visible body на анг. |
| s28 | Regulatory blockers | PASS | 3 cards FDA + ATEX + Указ 250 с явной цветовой кодировкой | Хорошая Ocean → Teal → Gold gradient для разделения jurisdictions. «Audit trail + validated systems + traceable changes», «Black-box ML — нет audit trail. AI не может быть final decision-maker», «Hardware certified для zones (0, 1, 2). Zone 0: non-certified AI hardware ФИЗИЧЕСКИ запрещён. Не вопрос ПО — вопрос hardware», «Deploy AI в РФ-промышленности», «predictive monitoring gas/temp/dust», «AI помогает в predictive monitoring gas/temp/dust — не заменяет ATEX hardware», «foreshadow к Лекции 12» — массовый leak. |
| s29 | Russian context | PASS visual | Two columns Норникель + СИБУР/ММК; real photo Bystrinsky Mine | Real photo present. «industrial-operation stage», «AI на flotation / grinding — не пилот, production», «СИБУР Marketplace технологического моделирования», «PEDAGOGICAL POINT (LO2)», «Public-disclosure скудна — это анти-pattern в reporting, НЕ доказательство absence adoption», «**LO2 — различать PR statement и измеримый эффект**» — массовый leak + **LO2 code leaks**. |
| s30 | Process failure matrix | PASS schema | 2×2 4 типа провалов на процессном | Symmetric с s22 — strong pedagogy. Однако: «RL distribution drift», «Batch transitions / feedstock / сезон / wear», «Regulatory blocker», «Vendor PR без metrics», «public-verifiable ROI», «red flag», «Регуляторика already exists. HITL + audit trail mandatory», «Edge ML на копроцессоре, не LLM. Latency = determinism» — массовый leak. **«§2; основа для критериев §4»** — cross-ref. |
| s31 | Section 4 divider | PASS | Декоративная «4» + «PAYOFF лекции» в subtitle | OK. |
| s32 | 4 категории критериев | PASS schema | 2×2 cards с alternatives badges | Solid schema_matrix 75%+ fill. «MTBF >1 года · недостаточно failures», «FP cost >10× FN · SPC лучше», «SIL 2/3 safety-critical · ML cert hard», «Audit-trail обязателен (FDA, GAMP)», «ATEX Zone 0 · hardware restriction», «Operator distrust → workaround», «Pilot без go-criteria · pilot purgatory», «Demo-hype без 6-mo production», «Альт-вы: physics-based sim · DOE · SPC / explainable ML · hybrid · on-premise / Six Sigma · Jidoka · structured pilots» — массовый leak. Заголовок цели **«payoff лекции (LO8)»** — LO code leak. |
| s33 | Alternatives matrix | PASS schema | 6×5 таблица + hybrid patterns bottom | Solid schema_matrix. «univariate, стабильные», «Не multi-variate», «Causal inference», «Не online», «Explicit model, reacts к drift», «Нужна точная модель», «Объяснимый, calibrated», «Не learning», «Обобщается, CFD/FEA/kinetics», «controlled env», «Validated за неделю», «Не справляется с variability», «HYBRID PATTERNS», «PINN (Physics-Informed NN) — physics constraints в ML loss», «ML over SPC — статистический baseline + ML на остатке», «PLC + edge ML coprocessor (POSCO pattern)» — массовый leak. |
| s34 | Pfizer Vox worked example | PASS schema | 5 steps × 5 columns equal-width | Solid 5-step layout. «Identify class», «Map alternatives», «Apply 4 cats», «Pilot + go-criteria», «Production + HITL», «ПРОЦЕССНОЕ — continuous bioprocessing», «mRNA-вакцины: batch process», «SPC: univariate baseline (недостаточен)», «DOE: not suitable (online)», «MPC: control, не покрывает rare anomalies», «Данные ✓ много batch data + разметка из QC», «Стоимость ✓ FP cost manageable», «Регул. ✓/✗ FDA → recommend mode», «+20 000 doses per batch — baseline известен», «Go-criterion: baseline + ROI within 12 mo.», «Vox recommends actions to operators», «Architecture: decision-support, не controller», «Audit trail для FDA Part 11 — satisfied», «Lesson: 5-step framework работает ретроспективно — готовый инструмент для оценки новых проектов» — массовый leak. |
| s35 | 5-step framework | PASS schema | Top: 5 numbered cards (gold circles 1-5) + Bottom: 4 vendor-question cards | Solid layout. «Identify class · discrete / process? какая физика, регуляторика?», «Map alternatives · SPC / DOE / MPC / RCM / physics-sim / rules-vision», «Apply 4 categories», «Pilot + go-criteria · baseline + measure window + go/no-go threshold ДО старта», «Production + HITL · recommend mode safety-critical validated, traceable», «Baseline до AI», «Окно измерения», «Перечень вмешательств», «ОЕЕ-канал · Availability / Performance / Quality — какой компонент?» — heavy leak. |
| s36 | Section 5 divider | PASS | Декоративная «5» + 3 тематики | «5 вендор-вопросов · bridge к Лекции 12» — bridge англицизм. |
| s37 | Recap + failure-callback | PASS | 2 cards Discrete + Process + bottom общий слой + failure callback formula navy | Symmetric layout. «Foundation models = augmentation, не controller · 95% не доходят до production · 4 категории + 5-step framework + 4 вопроса» в общем слое — массовый leak. Strong callback formula. |
| s38 | Q&A vendor questions | PASS | 5 numbered cards top + 3 typical Q&A bottom | Pocket-card structure work. «Запишите на стикер, наклейте на монитор · работает на любом vendor pitch», «Chat-помощник для оператора или autonomous controller?», «Q. "Мне говорят внедрить AI на нашем процессе, но я не уверен" → Пройдите 5-step framework. Если хотя бы шаг не проходит — отчитайтесь руководству. Не запускайте pilot без go-criteria.», «Q. "SPC vs ML — что выбрать?" → FDA + univariate → SPC. Multi-variate + recommend mode + audit trail → ML. Hybrid: SPC + ML over residuals — defensible перед регулятором.», «Q. "RL vs MPC — что лучше?" → MPC dominates control loop. RL дополняет MPC на high-level scheduling. Safe-fallback к MPC mandatory.» — массовый leak. |
| s39 | Closing hero BMW | FAIL | Real BMW Welt image left ~50% + 3 cards right с bridge text | Hero 32.5% area < 40%. Image presented narrower than full canvas. Заголовок крупный «Сшивка инструментов в production-fabric» — «production-fabric» англицизм. «Цифровые двойники как унифицирующая абстракция · AI в автоматизации как production-fabric · ГОСТ Р 57700.37-2021», «BMW: 30+ plants. Holcim world-first cement DT · Foxconn-NVIDIA Omniverse», «Спасибо · Лекция 11 · AI в дискретном и процессном производстве», «Запишите 5 вопросов к вендору — это самая практическая вещь сегодня» — массовый leak. **«Modul 2»** TYPO в Russian content. |

---

## 3. P0 issues (блокеры)

### P0-1 — «Sertification» typo ×2 на s09
**Severity:** P0 (visible spelling error на видимом body).
**Location:** s09 OT column + IT column. Source `slides/s09-ot-it-split.md` строки 28, 40.
**Issue:** должно быть **«Сертификация»** или **«Certification»** (англ. транслит). Не «Sertification».
**Recommendation:** замените на «Сертификация» (русское) в обоих столбцах. Это критический баг — слайд из core содержательного блока s09 показывает безграмотность.

### P0-2 — `[VFY-day-of]` маркер visible в body на s07 + s08
**Severity:** P0 (designer-extra leak в visible body, students видят internal scaffold).
**Location:** s07 footer «Источники: McKinsey 2025, MIT Sloan 2025, RAND 2025, Deloitte 2025 · [VFY-day-of]»; s08 footer «Markets and Markets · Precedence · Fortune Business Insights · Gartner 2025 · [VFY-day-of]».
**Issue:** `[VFY-day-of]` — orchestrator-internal scaffolding marker (per anti-pattern catalog). Не должен visible на student-facing PNG.
**Recommendation:** удалить маркер из footer на обеих слайдах. Перенести в frontmatter speaker_notes если нужен напоминать.

### P0-3 — Hero structural gap: s01 + s39 < 40% area
**Severity:** P0 ([[hero-images-required]] mandate violated; cost-of-omission lec-08 ~1 owner-интервенция).
**Location:** s01 hero Tesla Giga Press 6.5×4.8 in = **31% area**; s39 hero BMW Welt 6.5×5.0 in = **32.5% area** (canvas 13.33×7.5 = 100 sq in).
**Issue:** mandate ≥40% площади slide для hero на s01 + s39. Designer self-report в iteration-log.md «≥40% area ✓» неверен.
**Recommendation:** resize hero images:
- s01: рекомендую 8.0×5.5 in = 44% или 13.33×4.5 = 60% full-bleed top half с текстом overlay снизу.
- s39: те же варианты.

---

## 4. P1 issues (важные)

### P1-1 — Designer-extras leak: LO codes visible на 5 слайдах
**Severity:** P1 (course-scaffold leak, lecture-of-lectures pattern).
**Locations:**
- s02 cover body «LO1 — назвать инструменты дискретного и процессного AI · LO2 — критически оценить vendor-claim · LO7 — различить chat-помощник vs autonomous controller · LO8 — сформулировать "когда AI не нужен"»
- s08 attribution «Урок для инженера: читайте methodology, не верьте одной цифре» (внутренне OK, но subtitle plan ref leak)
- s21 subtitle «Young Liu, Foxconn chairman, Computex май 2025 — **LO2 hook**»
- s29 attribution **«LO2 — различать PR statement и измеримый эффект»** + body «PEDAGOGICAL POINT (LO2):»
- s32 subtitle **«Данные · Стоимость · Регуляторика · Человек — payoff лекции (LO8)»**
**Issue:** Lec-09 reference pattern — LO коды живут в frontmatter / speaker_notes, не в visible body. Student-facing PNG не должен показывать LO1a/LO1b/LO2/LO7/LO8.
**Recommendation:**
- s02: заменить body LO1/LO2/LO7/LO8 строки на содержательные цели на русском («Назвать инструменты для каждого типа производства · Критически оценить заявку вендора · Различить помощник оператора и контроллер · Сформулировать "когда AI не нужен"»).
- s21: убрать «— LO2 hook» из subtitle, заменить на «— заявка vs метрика».
- s29: убрать «(LO2):» из header «PEDAGOGICAL POINT». Убрать «LO2 — различать PR statement...» из чип-pillа.
- s32: убрать «(LO8)» из subtitle.

### P1-2 — Designer-extras leak: §4 cross-references на 4 слайдах
**Severity:** P1 (forward-reference scaffold leak).
**Locations:**
- s04 footer «OEE — самая важная метрика лекции · **возвращаемся в разделах 1, 2, 4**»
- s16 subtitle «Первый критерий категории «данные» **в §4** — есть ли разметка adequate volume»
- s22 subtitle «Failure-pattern matrix — эмпирическая база **для категорий §4**» + footer «Эти четыре типа становятся критериями категорий «человек», «данные», «стоимость» **в §4**»
- s24 footer «Pfizer Vox станет **worked example в §4**»
- s30 subtitle «Failure-pattern matrix — симметрично §2; **основа для критериев §4**»
**Issue:** ссылки на «§4» — chapter-internal scaffold. Lec-09 pattern: cross-section refs могут жить в speaker notes, но не в visible footer/subtitle.
**Recommendation:** заменить «в §4» → «в Разделе 4» (читаемое для студента). «возвращаемся в разделах 1, 2, 4» убрать (это designer extra).

### P1-3 — Designer-extras leak: cross-slide reference `callback s16` на s20
**Severity:** P1 (slide-id reference leak — most explicit anti-pattern).
**Location:** s20 «Scarce defect labels: Defect rate 1% + редкие типы → модель не видит rare defects (**callback s16**).»
**Issue:** `(callback s16)` — slide reference notation. Student не должен видеть s-numbers.
**Recommendation:** заменить на «(см. слайд "Эталонная разметка — дорого")» или просто убрать (содержание ясно без callback).

### P1-4 — Deep latin-token scan: 620 unique anglicisms / 1149 occurrences в visible PPTX body
**Severity:** P1 (top-end of P1, near-P0 — [[russification]] mandate).
**Evidence:**
- Raw scan: `python3 tools/presentation-build/deep_latin_scan.py /tmp/lec-11-pptx-visible.txt` → 620 unique / 1149 occurrences.
- **Comparison: Лекция 8 v1 — 224 unique** (3 revision rounds к 0). Lec-11 = **2.8× worse**.
- Top critical hits (top-30 blacklist match): production×13, baseline×10, controller×7, framework×7, autonomous×6, downtime×7, automation×4, mistake×5, vendor×5, edge×6, cost×4, drift×5, trail×9, audit×5, models×4, process×6, output, methodology, scope, capability, reliability, augmentation, Recurring pattern, structural divide.
- Specific examples on each slide (см. §2 per-slide notes выше).
**Issue:** Designer self-report «Russification check: body content RU; whitelist applied» в iteration-log.md verifiably false. Pattern-narrow grep missed depth — same failure mode как Лекция 8 v1.
**Recommendation:** русифицировать body content per Russification table (§5.8 README):
- production → промышленное применение / производство / линия
- baseline → базовый уровень / отправная точка
- controller → контроллер (русифицированный)
- framework → рамка / каркас
- autonomous → автономный (русифицированный)
- downtime → простой / простой времени
- audit trail → журнал аудита / след аудита
- methodology / scope → методология / охват
- vendor → поставщик / вендор (русифицированный)
- safety-critical → критичный к безопасности
- production-fabric → производственная ткань / промышленная инфраструктура
- defect rate / class imbalance → доля брака / дисбаланс классов
- adequate volume → достаточный объём
- structural divide → структурное разделение
- augmentation → дополнение
- capability / reliability → возможность / надёжность

**Approach:** не «русифицировать всё подряд», а:
1. Keep brand names (BMW, TSMC, Tesla, Foxconn, BASF, Pfizer и т.п.).
2. Keep established acronyms (CV, PdM, OEE, MPC, RL, CIRL, PLC, FDA, GAMP, ATEX, HITL, SPC, DOE, RCM, ISA-95, SCADA, MES, KPI, ROI) с inline gloss при первом упоминании.
3. Keep mode-name patterns (text-to-text, etc.) — не релевантно для производства.
4. Replace narrative anglicisms на канонические RU из таблицы.

Target после revision: **0 critical anglicism hits** в top-30 blacklist; deep scan unique - whitelist = «brand names + acronyms + URLs + case names only».

### P1-5 — Russification typo «Modul 2» на s39
**Severity:** P1 (visible typo).
**Location:** s39 speaker_notes (Markdown), bottom card body «Спасибо · Лекция 11 · AI в дискретном и процессном производстве».
**Issue:** В speaker notes написано «Modul 2» — это не русский «Модуль 2» и не английский «Module 2». Может быть transcription typo.
**Recommendation:** «Лекция 11 · Модуль 2 · AI в дискретном и процессном производстве».

### P1-6 — Cover s02 subtitle «Модуль 2 · 75 минут + Q&A» имеет смешанную графику
**Severity:** P1.
**Location:** s02 cover.
**Issue:** Слово «модуль» с маленькой М, а «Q&A» оставлено как латиница. На cover ожидается consistency.
**Recommendation:** «Модуль 2 · 75 минут · вопросы-ответы» (либо принять «Q&A» в whitelist, если есть convention).

### P1-7 — s10 layout: photo dominates over 3 reasons
**Severity:** P1 (visual hierarchy reversed).
**Location:** s10 «Фундаментальные модели = augmentation, НЕ controller».
**Issue:** Photo Siemens HQ занимает ~half left column. Три причины (1. Задержка вывода, 2. Галлюцинации, 3. Сертификация) — главный assertion слайда — справа, но визуально подавлены большим изображением. Photo == decorative (Siemens HQ — это not evidence-of-three-reasons; это просто Siemens identity).
**Recommendation:** уменьшить photo до thumbnail ~3×2 in в верхнем углу column 1 (с Siemens IFM + Foxconn FoxBrain text вокруг). 3 причины делать главным визуальным focal point — крупнее body text, gold underline под номером.

### P1-8 — Cross-slide redundancy: s35 «4 вендор-вопроса» дублирует s38 «5 вендор-вопросов»
**Severity:** P1 (cross-slide chart duplication anti-pattern #16).
**Location:** s35 содержит 4 numbered vendor questions карточки (Baseline / Окно / Перечень вмешательств / OEE-канал). s38 содержит 5 numbered vendor questions карточек (те же 4 + 5-я «Архитектурный класс»).
**Issue:** На s35 visible 4 cards с теми же questions, на s38 — те же 4 + одна. Студент видит дубль через 3 слайда.
**Recommendation:** на s35 убрать 4 vendor-question cards (5-step framework — main focus); сохранить только в s38. Альтернатива: на s35 показать только 5-step + один «3 вопроса» bullet pointer.

### P1-9 — Foxconn quote s21: full English quote dominates slide
**Severity:** P1.
**Location:** s21 hero callout «After plugging AI tools into Foxconn's workflows, software now performs roughly 80 percent of the work required to configure equipment for a fresh production run.»
**Issue:** Длинная цитата на английском доминирует над визуалом. Это assertion-evidence anti-pattern (heavy text-only callout без RU translation).
**Recommendation:** показать русский перевод как primary, английский — мелким fine-print под подписью (или убрать английский). Например: «После подключения AI-инструментов к рабочим процессам Foxconn — программа теперь выполняет около 80% работы по настройке оборудования под новый прогон» — Юнг Лю, Foxconn chairman.

### P1-10 — Roadmap-bar не on s05 keystone
**Severity:** P1 (Lec-N-1 pattern deviation check).
**Location:** s05 keystone — отсутствует top roadmap-bar.
**Issue:** Lec-09 pattern: roadmap-bar на cover (s02) + section dividers (s06/s13/s23/s31/s36). Keystone s05 не должен иметь roadmap-bar в Lec-09 reference, но cover s02 имеет. Подтверждение: cover (s02) shows «1. Общее» highlighted gold. Это корректно. Confirmed: keystone s05 без roadmap-bar — pattern compliant. **P1 удалён.** Strike P1-10.

### P1-11 — Хедер s39 «Лекция 12 — bridge» mixed RU/EN
**Severity:** P1.
**Location:** s39 right column header «Лекция 12 — bridge | Сшивка инструментов в production-fabric».
**Issue:** «bridge» + «production-fabric» — англицизмы в визуальном фокусе.
**Recommendation:** «Лекция 12 — мост · Сшивка инструментов в производственную ткань» или «Лекция 12 — переход · Сшивка инструментов в промышленную инфраструктуру».

### P1-12 — Footer attribution на s14 cropped в snapshot
**Severity:** P1.
**Location:** s14 bottom footer «BMW Press 2025 · TSMC · Boeing · Wikimedia CC-BY-SA».
**Issue:** Attribution line обрезан на bottom edge snapshot. Может быть rendering artifact или text overflow.
**Recommendation:** проверить top margin footer (move up на 0.2 in). Verify visible на final render.

### P1-13 — s11 subtitle: «Recurring pattern: capability в контролируемой среде vs reliability 99,9%»
**Severity:** P1 (subtitle главный читаемый элемент после assertion — англицизмы доминируют).
**Recommendation:** «Повторяющийся паттерн: возможности в контролируемой среде vs надёжность 99,9% в неконтролируемой».

### P1-14 — s17 layout: photo crowded, 3 sections cramped
**Severity:** P1.
**Location:** s17 PdM на дискретном.
**Issue:** Real photo Tata Steel мелкий (4.2×2.1 in), и 3 контентные секции (VENDOR ОБЕЩАЕТ / MCKINSEY REALITY CHECK / OEE CALLBACK) ютятся друг к другу.
**Recommendation:** убрать VENDOR ОБЕЩАЕТ card (vendor claims можно в bullet form в один card), сохранить REALITY CHECK + OEE CALLBACK как два crisp card.

---

## 5. P2 issues (косметика)

### P2-1 — s07 chart legend «% projects fail» на английском
**Recommendation:** «% проектов провалились» или просто убрать legend (3 источника подписаны на X-оси).

### P2-2 — s08 chart legend «$B 2025» на английском, X-axis в латинице
**Recommendation:** «$ млрд 2025» + Markets and Markets / Precedence / Fortune кириллицей как «Markets» (brand allow) с inline gloss.

### P2-3 — s27 chart legend «Latency ms»
**Recommendation:** «Задержка, мс».

### P2-4 — Footer attribution на s17 «Tata Steel Port Talbot · Wikimedia» слишком мелкий и обрезан
**Recommendation:** увеличить font 10pt → 11pt + проверить bottom margin.

### P2-5 — s28 carde Указ № 250: «Защита критической информационной инфраструктуры (КИИ)»  заголовок очень короткий
Body выпадает out of card region — verify в render. **Acceptable as-is**.

### P2-6 — Cards с разной высотой в section dividers (s06 / s13 / s23 / s31 / s36)
Sub-labels «Раздел 1 · 12 мин · 6 слайдов» varies length. Minor.

### P2-7 — Brand name «Yokogawa» vs «Yokogawa-JSR» — обе variants visible
Minor consistency.

---

## 6. Schema Readability per-schema assessment

| Slide | Subtype | Pass | Notes |
|---|---|---|---|
| s05 keystone | quadrant-like 2-col | PASS | Two columns visually balanced; gold belt снизу anchors. Failure-метки явные. |
| s09 OT/IT | comparison_2col | PASS structurally | **Sertification typo blocks accept**. Иначе: Ocean header + Teal header + параллельные строки work. |
| s22 discrete failure matrix | schema_matrix 2×2 | PASS | 4 cases × 4 type structure clear; case chips gold; color-coded левая граница. Fill rate ≥75%. |
| s25 CIRL architecture | schema_architecture | PASS | PID controller + Deep RL + arrow showing "в loss function" — explicit. RL recall good. |
| s26 RL drift | schema_matrix 2×2 | PASS | 4 mechanisms × OOD / Stale / External / Drift chip badges. Safe-fallback bottom. |
| s30 process failure matrix | schema_matrix 2×2 | PASS | Symmetric с s22. Fill rate good. |
| s32 4 categories | schema_matrix 2×2 | PASS | Cards numbered A/B/C/D + alternatives badges gold. 3 criteria per card. |
| s33 alternatives matrix | schema_matrix 6×5 | PASS | Большая table — все 30 ячеек заполнены. Reg-friendly column → checkmarks. |
| s34 Pfizer 5-step | schema_pipeline 5-col | PASS | 5 equal-width columns, Ocean → Teal → Ocean → Gold → Navy gradient на header — direction of progression visible. |
| s35 5-step framework | schema_pipeline + nested cards | PASS | Top 5 numbered (gold circles) + bottom 4 vendor-Q numbered (gold circles). Clear. Однако P1-8 — redundancy с s38. |
| s37 recap | comparison_2col + bottom callback | PASS | Two columns Discrete / Process + общий слой + failure-callback navy bottom. |

**Overall schema-readability:** все schemas pass on geometry. Однако content в schema cells = массовый anglicism leak (см. P1-4). **Schema geometry OK; schema text НЕ OK.**

---

## 7. Media coverage verification

**Designer self-report:** «Total media-rich ≈ 22/39 ≈ 56%» (≥50% target ✓).

**Independent verification:**
- Real photos (Tier 2 Wikimedia CC-BY-SA): 10 confirmed (s01, s10, s14, s15, s17, s24, s25, s27, s29, s39).
- QuickChart PNG charts: 4 confirmed (s07 pilot failure bar, s08 market divergence, s27 latency, plus s07 5,5% hero).
- Mermaid/composed shape diagrams: ~6 confirmed (s05 keystone columns, s09 OT/IT, s25 CIRL architecture, s32 4-cat grid, s33 6×5 table, s34 5-step + s35 5-step).
- Lucide icons (Ocean recolor): 3 slides (s14, s18, s24).

**Total media-rich (real photos + charts + diagrams, excl. iconography in boxes):** ~20-22 / 39 ≈ **51-56%** ✓ (within self-report range).

**Caveat:** s14 has small photo (3.6×1.5 in) + 2 icons → counts as media-rich, но icons shouldn't count per anti-pattern. Strict count = 18/39 ≈ 46% (just below 50%).

**Verdict:** **PASS with caveat.** Media coverage acceptable, но multiple photos are too small для full impact (s17 4.2×2.1, s14 TSMC 3.6×1.5, s27 1.5×1.5).

---

## 8. Hero check s01 + s39

**FAIL.** Both heroes < 40% area mandate.

| Slide | Image size (inches) | Slide area (inches²) | Hero area (inches²) | % |
|---|---|---|---|---|
| s01 | 6.5 × 4.8 = 31.2 in² | 13.33 × 7.5 = 99.98 in² | 31.2 in² | **31.2%** ❌ |
| s39 | 6.5 × 5.0 = 32.5 in² | 99.98 in² | 32.5 in² | **32.5%** ❌ |

**Required:** ≥40% per [[hero-images-required]] mandate.
**Designer self-report:** «s01 + s39 both have hero ≥40% area real image with attribution visible ✓» — verifiably false.

**Recommendation:** resize images to ≥9×6 in (54%) или 13.33×4.5 full-bleed top (60%) с текстом ниже.

Attribution labels: **PRESENT** (s01 «Tesla Giga Press · Idra OL 6100 CS · Fremont, 2020 · Wikimedia CC-BY-SA»; s39 «BMW Welt / Group · Wikimedia · BMW Digital Twin · NVIDIA GTC Paris 2025»). ✓ Visible, attribution OK.

**Tier acquisition log:** documented в iteration-log.md ✓.

**Verdict on hero check: P0 fail on area; pass on attribution + acquisition.**

---

## 9. Designer-extras grep result (orchestrator-INDEPENDENT)

**Regex:** `(Лектору|Вы здесь|тайминг|VFY-day|FACT-CHECK|VERIFY-DAY|LO[1-9]|§[0-9]|→ s[0-9]+|\(s[0-9][0-9]\)|course-scaffold|не вводи|возвращаемся|— в главе|в материалах лекции|это payoff)`

**Designer self-report:** «0 hits in visible body».

**Independent scan result (visible PPTX body extract, frontmatter excluded):**

| Pattern | Hits | Locations |
|---|---|---|
| `LO[1-9]` | 9 | s02 cover body (LO1/LO2/LO7/LO8), s21 «LO2 hook», s29 «PEDAGOGICAL POINT (LO2)» + «LO2 — различать», s32 «(LO8)» |
| `§[0-9]` | 4 | s16 «в §4», s22 «§4» ×2, s24 «в §4», s30 «§2; основа для критериев §4» |
| `→ s[0-9]+` или `(s[0-9][0-9])` | 1 | s20 «(callback s16)» |
| `VFY-day` | 2 | s07 footer, s08 footer |
| `возвращаемся` | 1 | s04 footer «возвращаемся в разделах 1, 2, 4» |
| **TOTAL** | **17** | 9 unique slides affected |

**Verdict: FAIL.** Designer self-report unreliable. Cost-of-omission lec-04 ~5 циклов if not caught now.

---

## 10. Deep latin-token scan result

**Tool:** `tools/presentation-build/deep_latin_scan.py` (broad regex + brand allowlist).

**Designer self-report:** «assertion + body содержание на русском. Whitelisted: tech-acronyms + brand names + direct quotes.»

**Independent scan result:**
```
=== /tmp/lec-11-pptx-visible.txt ===
  total occurrences: 1149
  unique tokens:     620
```

**Verdict: FAIL — 2.8× worse than Лекция 8 v1 (224 unique).**

**Top critical anglicisms** (top-30 blacklist hits — pattern-narrow scan would also flag):
- production (13×), Tesla (16× ok-brand), baseline (10×), controller (7×), framework (7×), autonomous (6×), downtime (7×), automation (4×), models (4×), mistake (5×), vendor (5×), trail (9×), audit (5×), edge (6×), cost (4×), loss (5×), drift (5×), STEP (5×), process (6×), CIRL (7× ok-brand-derivative), BASF (6× ok-brand), batch (7×), Pfizer (6× ok-brand), Foxconn (8× ok-brand), Boeing (7× ok-brand), BMW (9× ok-brand), McKinsey (4× ok-source).

**Non-brand critical hits to fix:** production, baseline, controller, framework, autonomous, downtime, automation, models, mistake, vendor, trail, audit, edge, cost, loss, drift, process, batch + multi-word: «high performers», «structural divide», «augmentation», «Recurring pattern», «capability», «reliability», «adequate volume», «class imbalance», «defect rate», «production-fabric», «production-сборке», «control loop», «out-of-distribution», «out-of-band», «PR statement», «hype-collapse», «pilot purgatory», «safety-critical», «recommend mode», «Hybrid».

**Pattern-narrow grep would catch ~50 hits (per Лекция 8 baseline 32). Deep scan caught 620 unique. Same failure mode как Лекция 8 v1.**

**Recommendation:** see P1-4 above. Phase 7 polish round must re-run deep scan and target `unique - whitelist ≤ 30` (только brand names + acronyms + case names + URLs).

---

## 11. Lec-N-1 pattern compliance matrix

Reference: Лекция 9 «AI в авиакосмосе/обороне» (PR #120 merged 2026-05-21).

| Element | Lec-09 reference | Lec-11 v1 | Compliance |
|---|---|---|---|
| Slide count | 39 (с keystone + lecture-map + glossary + 5 dividers + Q&A + 2 hero) | 39 | ✓ |
| Cover (s02) | crown numeral «9» + title + LO summary + roadmap-bar | crown «11» + title + LO summary + roadmap-bar | ✓ (LO codes still visible — see P1-1) |
| Lecture-map slide | s03 5 horizontal section cards | s03 5 horizontal section cards с time markers | ✓ |
| Glossary mini | s04 6 must-know × 2 col | s04 6 terms × 2 col | ✓ |
| Keystone slide | s05 OODA loop visualization | s05 two-model schema (discrete vs process) | ✓ different keystone, structurally compliant |
| Section dividers | 5 (s06 / s13 / s23 / s31 / s36) | 5 (s06 / s13 / s23 / s31 / s36) | ✓ symmetric |
| Roadmap-bar | only on cover + dividers, NOT on content | only on cover + dividers (verified s07-s12, s14-s22, s24-s30, s32-s35, s37-s38) | ✓ correct |
| Dedicated Q&A slide | s38 | s38 «5 вопросов к вендору + 3 typical Q&A» | ✓ |
| Hero cover (s01) | Hero ≥40% real image with attribution | Hero 31% area — **FAIL** ([[hero-images-required]]) | ❌ P0-3 |
| Hero closing (s39) | Hero ≥40% bridge to Lec-N+1 + attribution | Hero 32.5% area — **FAIL** | ❌ P0-3 |
| Section count | 5 sections per lecture | 5 sections | ✓ |
| Failure-bucket strict-in | ~30%+ | ~61% (24/39 strict-in) | ✓ |

**Pattern compliance: 10/12 PASS, 2/12 FAIL (hero area both s01 + s39).**

Pattern-divergence severity: **P0** (structural mandate violated).

---

## 12. Recommendations for Phase 8 revision

### Critical (P0 — must fix before APPROVE)

1. **Fix typo «Sertification» → «Сертификация» на s09** (2 occurrences, source `slides/s09-ot-it-split.md`).
2. **Remove `[VFY-day-of]` markers с visible body на s07 + s08** footer (move to speaker notes if needed).
3. **Resize hero images s01 + s39 к ≥40% area** (target 9×6 in = 54% или full-bleed 13.33×4.5 = 60%).

### Important (P1 — should fix before APPROVE)

4. **Remove LO codes from visible body** на s02 cover, s21 subtitle, s29 attribution + body, s32 subtitle. Заменить codes на содержательные RU фразы.
5. **Replace §4 cross-references** с «в Разделе 4» на s16, s22, s24, s30; убрать «возвращаемся в разделах 1, 2, 4» с s04.
6. **Remove `callback s16`** с s20 (substitute «(см. слайд "Эталонная разметка")»).
7. **Deep Russification pass.** Target после revision: `python3 deep_latin_scan.py` показывает unique - whitelist ≤ 30 (только brands + acronyms + case names + URLs). См. P1-4 для translation table prefix.
8. **Fix s39 «Modul 2» → «Модуль 2»**.
9. **Cover s02 subtitle** «модуль» → «Модуль»; «75 минут + Q&A» → «75 минут · вопросы-ответы» (или принять Q&A в whitelist через convention).
10. **Resize s10 photo Siemens HQ к thumbnail** (3 reasons должны быть focal point, не photo).
11. **Remove 4 vendor-question cards с s35** (avoid cross-slide redundancy с s38; keep only 5-step framework на s35).
12. **Add RU translation для Foxconn quote на s21** (English как fine-print под подписью).
13. **Fix s39 right column header** «Лекция 12 — bridge | Сшивка инструментов в production-fabric» → «Лекция 12 — переход · Сшивка инструментов в промышленную ткань» (или «инфраструктуру»).
14. **Verify s14 footer attribution** не cropped (move up 0.2 in if needed).
15. **Russify s11 subtitle** «Recurring pattern: capability... reliability...».
16. **Reduce s17 crowding** (убрать VENDOR ОБЕЩАЕТ card, оставить REALITY CHECK + OEE CALLBACK).

### Cosmetic (P2 — optional)

17-21. См. §5.

### Verification после Phase 8 revision

1. Re-run **independent deep latin-token scan** — target unique - whitelist ≤ 30.
2. Re-run **independent designer-extras grep** — target 0 hits с regex выше.
3. Re-verify **hero area** через measure tool — target ≥40% площади на s01 + s39.
4. Re-snapshot all 39 PNG → visual sweep:
   - s01: hero доминирует визуально, foreshadow Tesla retreat = key emotional anchor.
   - s39: hero доминирует, bridge к Лекции 12 readable.
   - s09: «Сертификация» typo fixed.
   - s07/s08: no [VFY-day-of] markers.
   - s02/s21/s29/s32: no visible LO codes.

### Verdict для Phase 8 spawn

**REJECT current v1.** Spawn presentation-designer Phase 8 with these inputs:
1. This critique report.
2. Russification table (per §5.8 README).
3. Deep latin scan tool reference.
4. Hero resize spec (9×6 in или full-bleed 13.33×4.5).
5. Designer-extras independent grep regex (для self-verify).

Target Phase 8 deliverable: re-rendered 39 PNG passing all 4 verification gates выше (deep scan + extras grep + hero area + typo check).

---

## Сводка

- **Всего слайдов:** 39
- **P0 issues (блокеры):** 3 (Sertification typo, [VFY-day-of] leak, hero <40% area)
- **P1 issues (важные):** 13 (LO leaks ×5, §4 leaks ×4, callback leak ×1, deep latin scan, Modul typo, cover mixed, s10 layout, s35-s38 redundancy, Foxconn quote, s39 mixed, s14 footer, s11 subtitle, s17 crowding)
- **P2 issues (косметика):** 7

**Counter-check:** 13 P1 + 3 P0 → verdict floor REVISE. Three concurrent structural gaps (hero + Russification + designer-extras) → REJECT.

**VERDICT: REJECT.** Spawn Phase 8 polish round с этим отчётом.

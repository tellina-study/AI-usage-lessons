# Methodology Critic Report — Лекция 11 speech v1 — 2026-05-21

**VERDICT: APPROVE-WITH-POLISH**

(4 P1 issues, 7 P2 issues. Counter-check: <5 P1 → APPROVE-WITH-POLISH valid. Зачёт; small polish required перед speech v2 freeze.)

---

## Severity counts

- **P0:** 0 (методически непригодных — нет)
- **P1:** 4 (заметно вредят / структурные шероховатости — починить в полировке)
- **P2:** 7 (мелочи)

---

## Top-line summary

Speech v1 — **методически крепкий, конверсационный, structurally well-aligned с chapter v5 + slides v2.1**. Producer self-report по большинству DoD-метрик independently воспроизводится (WPM, cornerstones, 10 pre-flight items, 3 worked examples, 5 vendor questions в speech body, conversational register). Несколько структурных шероховатостей:

1. **Q5 vendor question structurally drifts** между speech (3 documented failures) и slide s38 (Architectural class) — speech и chapter согласованы, slide расходится. **Это slide-side P1 для consistency-checker**, не speech bug — но в этом review speech-narrative последовательнее, чем slide.
2. **2 LO-codes в narrative body** (LO2 на L587, LO8 на L739) — methodology leaks, должны переехать в speaker_notes / frontmatter (≠ visible body anti-pattern из CLAUDE.md).
3. **3 anglicism leaks в narrative body**: «Production с человеком в цикле» (L789), «уровне keystone» (L793) — должны быть rusified или взять в кавычки как brand-quotes.
4. **BASF Geismar «20-30% снижения брака»** — speech narrative преподносит как specific cite Geismar, тогда как chapter явно qualifies «industry survey range, точная цифра по Geismar не приводится». Baseline-attribution gap.

Failure-bucket strict-in **41.1%** (independently recounted) — significantly above 30% threshold, distributed по всем 5 разделам (min 30.9%, max 69.9%). Producer claim 68-70% преувеличена (вероятно, partial counted as strict-in); 42% claim в frontmatter accurate.

WPM independent re-verification: **0/41 fragments > 95 WPM, max 90.0 wpm (s39)**, average 63.6 — producer report (max 89.5, avg 63.7) воспроизводится с <1% drift (мелкая разница на counting policy для bracketed directions).

---

## 1. WPM independent re-verification

Methodology: parsed speech.md fragments между `### [Слайд N — ...]` headers (non-greedy regex, DOTALL); stripped bracketed `[...]` + parenthetical `(...)` stage directions + markdown emphasis; counted Cyrillic+Latin word tokens; divided by `duration_min` from `deck.yaml`. Script: `/tmp/wpm_analyze.py` (reproducible).

| Slide | Words | Dur(min) | WPM | Status |
|---|---|---|---|---|
| s01 | 225 | 3.0 | 75.0 | OK |
| s02 | 12 | 1.0 | 12.0 | OK |
| s03 | 67 | 1.0 | 67.0 | OK |
| s04 | 63 | 1.0 | 63.0 | OK |
| s05 | 130 | 2.0 | 65.0 | OK |
| s06 | 9 | 0.5 | 18.0 | OK |
| s07 | 148 | 2.0 | 74.0 | OK |
| s08 | 75 | 1.5 | 50.0 | OK |
| s09 | 83 | 1.5 | 55.3 | OK |
| s10 | 191 | 2.5 | 76.4 | elevated |
| s11 | 114 | 1.5 | 76.0 | elevated |
| s12 | 204 | 3.0 | 68.0 | OK |
| s13 | 7 | 0.5 | 14.0 | OK |
| s14 | 142 | 2.5 | 56.8 | OK |
| s15 | 166 | 2.0 | 83.0 | elevated |
| s16 | 92 | 1.5 | 61.3 | OK |
| s17 | 128 | 2.0 | 64.0 | OK |
| s18 | 150 | 2.0 | 75.0 | OK |
| s19 | 242 | 3.0 | 80.7 | elevated |
| s20 | 119 | 2.0 | 59.5 | OK |
| s21 | 92 | 1.5 | 61.3 | OK |
| s22 | 68 | 1.5 | 45.3 | OK |
| s23 | 7 | 0.5 | 14.0 | OK |
| s24 | 166 | 3.0 | 55.3 | OK |
| s25 | 188 | 3.0 | 62.7 | OK |
| s26 | 120 | 2.0 | 60.0 | OK |
| s27 | 171 | 2.5 | 68.4 | OK |
| s28 | 177 | 2.5 | 70.8 | OK |
| s29 | 171 | 2.5 | 68.4 | OK |
| s30 | 84 | 1.5 | 56.0 | OK |
| s31 | 10 | 0.5 | 20.0 | OK |
| s32 | 213 | 4.0 | 53.2 | OK |
| s33 | 143 | 2.5 | 57.2 | OK |
| s34 | 172 | 3.0 | 57.3 | OK |
| s34b | 199 | 2.5 | 79.6 | elevated |
| s34c | 210 | 2.5 | 84.0 | elevated |
| s35 | 129 | 2.0 | 64.5 | OK |
| s36 | 5 | 0.5 | 10.0 | OK |
| s37 | 119 | 2.0 | 59.5 | OK |
| s38 | 160 | 3.0 | 53.3 | OK |
| s39 | 180 | 2.0 | 90.0 | **WARN >85** |

**Total:** 5151 words / 81.0 min = **63.6 wpm average**. **0 violations > 95 wpm.** Max = s39 (90.0 wpm, 5 wpm от cap).

Producer self-report (avg 63.7, max 89.5, 0/41 > 95) **reproduces** с <1% drift на counting policy (bracketed directives стрипованы при подсчёте).

**Acceptance:** PASS zero-tolerance Лекция-5 hard cap.

**P2-9.** s39 closing hero — 90.0 wpm близко к cap. Эмоционально оправдано (closing arc, не контент-heavy), но рекомендую +20-30 секунд воздуха для финального impact или 10-15% сокращение.

---

## 2. AI-Failure strict-in independent recount

Methodology: tokenize speech narrative (post-frontmatter, post-pre-flight, post-Q&A-reserve) на параграфы ≥60 chars. Strict-in = paragraph contains failure-indicator AND (alternative OR criterion) OR failure-indicator alone (cornerstone failures count). Partial = только indicator без urok/alternative. Out = чисто descriptive content.

| Section | Strict-in words | Total words | Strict-in % |
|---|---|---|---|
| Раздел 0 (вход + keystone) | 342 | 489 | **69.9%** |
| Раздел 1 (общее) | 449 | 808 | **55.6%** |
| Раздел 2 (дискретное) | 366 | 1185 | **30.9%** |
| Раздел 3 (процессное) | 347 | 1069 | **32.5%** |
| Раздел 4 (рамка решения) | 395 | 1008 | **39.2%** |
| Раздел 5 (замыкание) | 197 | 484 | **40.7%** |
| **Overall** | **2060** | **5007** | **41.1%** |

**Acceptance:** ≥30% per-section met everywhere (min 30.9% in Раздел 2 — наименее failure-heavy в pictures), holistic 41.1% well above threshold.

**Producer self-report «68-70%»** — methodology divergence:
- Producer вероятно counted **partial** paragraphs (14.8% partial-bucket в моём счёте) как strict-in: 41.1 + 14.8 = 55.9%. Возможно plus indirect references (alternatives без явного failure-link) → 68-70%.
- **Authoritative metric — strict-in 41.1%** per CLAUDE.md AI-Failure & Judgment Content Rule § «strict-in only».
- Producer frontmatter `strict_in_share: "~42%"` accurate; speech-writer summary message inflated.

**No P-issue** — actual share above 30% threshold. P2-1 «producer overstated self-report; align to 42% не 68-70% для honest reporting».

---

## 3. Cornerstones consistency (10 + 0 drift)

10 canonical cornerstones expected per plan v2 + chapter:

| Cornerstone | Speech hits | Status |
|---|---|---|
| дискретное / процессное | 3 / 5 | ✓ |
| прогностическое обслуживание (PdM) | 4 | ✓ |
| компьютерное зрение (CV) для QC | 4 | ✓ |
| мягкий сенсор | 2 | ✓ |
| обучение с подкреплением (RL) | 1 expanded form + многократно RL | ✓ |
| ISA-95 | 3 | ✓ |
| OEE | 11 | ✓ |
| эталонная разметка | 3 | ✓ |
| застревание на пилотной стадии | 2 (+ описательные) | ✓ |
| раскол ОТ/ИТ | 3 | ✓ |

**Drift checks:**
- «предиктивное обслуживание» (vs канонического PdM): 0 — clean.
- «непрерывное производство» (drift с «процессного»): 0 — clean.
- «фундаментальная модель» (vs «foundation model»): 1 (s10 narrative) — canonical RU equivalent. ✓

**Producer claimed «11/11 present»** — мой счёт 10/10 canonical. 11-й, возможно, считается «бутылочное горлышко» / «парадокс автоматизации Bainbridge» — это **structural cornerstones**, не из base-10 lock-list. Acceptable extension если intentional, но не «11/11 canonical».

**P2-2.** Reconcile producer count: либо 10 (per plan v2) либо 11 с явным dispsis (Bainbridge paradox как 11-й).

---

## 4. Conversational register quality

**Метрики:**
- 12 явных «мы с вами» distributed по speech (target: ≥10) — ✓
- «давайте» в Разделе 0 (L189) + другие 4× — ✓
- «запомните» (L139, L181, L500) — ✓
- «вы будете задавать» (L843) + «мы с вами уносим» (L395, L500) — ✓
- «разберём» (L105) — ✓

**Storytelling beats для canonical cases:**
- **Tesla 2018**: «производственный ад», прямая цитата Маска dramatically read, IMD root cause, Bainbridge tie-back, Tesla 2024 callback — fully narrative. ✓ Excellent.
- **GE Predix**: 11 sentences, конкретные цифры + lesson. ✓
- **Boeing 737**: chronological storytelling 5 января 2024, NTSB findings, three reasons — strong narrative. ✓
- **IBM Watson Jeopardy → manufacturing → продан**: arc storytelling. ✓
- **Yokogawa-JSR FKDPP 35 дней**: precedent framing + premiumship. ✓

**Smooth transitions:**
- `[Переход на sNN]` markers consistent (40+ instances).
- Section dividers oratorically integrated («Раздел 1 из пяти»).

**P2-3.** Раздел 2 раздел divider L279 just «**Второй раздел из пяти.** Дискретное производство глубоко.» — minimal compared to other sections. Acceptable but could add 1 sentence ramp.

**No issues at register level. Strong.**

---

## 5. Pre-flight checklist actionability

**Counts:**
- **Day-before items:** 8 freshness-verify + 2 procedural (rehearse + paper-checklist) = 10. ✓ Producer claim accurate.
- **30-min-before items:** 4 (laptop, presenter mode, water, phone).
- **Recovery cards:** 3 (fact-check fail, projector fail, Q&A drift).
- **Day-of refresh:** 3 (market data, Tesla Optimus, Microsoft Fairwater).

**Actionability assessment:**
- All 8 freshness items have URL + specific check criterion («подтвердить 78% / 5,5%», «35 дней», «80% configuration claim»). ✓
- Live-data items explicit: McKinsey, market estimates, Tesla Optimus, Foxconn Wisconsin, Microsoft Fairwater. ✓ Matches volatility tier.
- 0 orphan references к удалённым slides (verified: s01, s07, s08, s11, s12, s21, s25, s28 all present in deck.yaml).

**`[VFY-day-of]` coverage:**
- Speech itself не содержит inline `[VFY-day-of]` markers (правильно — это для chapter); pre-flight section собирает их в actionable items.
- 8 critical volatile facts covered: McKinsey 78%/5,5%, market estimates 5×, Optimus deployment, Wisconsin/Fairwater milestones, FoxBrain 80%, FKDPP 35 days, FDA guidance, RAND 80,3%. ✓

**P2-4.** Recovery cards могли бы включить **«если фрагмент превышает timing — какой sentence skip-able»** — это была проблема Лекции 9. Не critical, но useful.

---

## 6. 3 worked examples coverage

| Example | Coverage | Steps | Verdict |
|---|---|---|---|
| Pfizer Vox PASS (s34) | Full ~3 min | 5/5 шагов explicit | ✓ |
| Авиадвигатель MTBF 8 FAIL (s34b) | Full ~2.5 min | 5/5 шагов (3 проваливают), explicit lesson | ✓ |
| Brewery packaging CV-QC PASS (s34c) | Full ~2.5 min | 5/5 шагов, baseline 0,3% → 0,2% pilot criterion explicit | ✓ |

**Bi-directional рамка-as-filter demonstration:**
- L771-772: «**Сквозной урок трёх примеров.** Рамка работает как **фильтр в обе стороны**. Pfizer проходит — режим рекомендации. Авиадвигатель не проходит — данных мало, сертификация блокирует. Пивоварня проходит — асимметрия правильная.»
- Explicit framing preserved. ✓

**P2-5.** Brewery example wpm 84.0 (elevated, не violation). Если worry о rate, можно сократить «12 камер, вывод ИИ на границе сети» (architectural detail) до one phrase.

---

## 7. 5 vendor questions alignment (CRITICAL FINDING)

### Speech (L829-837, §Раздел 5 / s38):
1. **Базовая линия.** Какая метрика была до развёртывания и как мерилась?
2. **Окно измерения.** За один запуск, среднее за месяц или лучший случай?
3. **Перечень вмешательств.** Что именно изменилось — люди, процесс, технология?
4. **OEE-вопрос.** В какую компоненту OEE добавляется эффект?
5. **Прошлые провалы.** Дайте мне три документированных провала вашей системы за последние 24 месяца в той же индустрии.

### Chapter §5.2 (chapter-part3.md L283-296):
1. Базовая линия ✓
2. Окно измерения ✓
3. Перечень вмешательств ✓
4. **«Бонус — OEE-вопрос»** (помечен как «бонус», не явно «4-й»)
5. **«Вопрос 5 — Прошлые провалы»** ✓ same as speech.

### Slide s38 (s38-qa-vendor-questions.md L19-27):
1. Baseline до AI ✓
2. Окно измерения ✓
3. Перечень вмешательств ✓
4. OEE-канал (availability/performance/quality) ✓
5. **«Архитектурный класс»** (chat-помощник vs autonomous controller) — **DIFFERENT FROM SPEECH/CHAPTER Q5**

**P1-1 (critical structural drift):** Slide s38 Q5 = «Архитектурный класс». Speech + chapter Q5 = «3 documented failures». **Speech narrative aligned with chapter**, but slide s38 narrative-mismatch.

This is a **slide-side bug** (s38 designed before final chapter Q&A consolidation). Speech v1 is correctly aligned to chapter v5. **Recommendation:** consistency-checker должен flag s38 для re-alignment, **not** change speech.

**P1-2.** Chapter §5.2 frames Q4 as «бонус» — слабее, чем «Q4 of 5». Speech makes it 4-of-5 hard. Inconsistency в naming/numbering. Resolve в chapter glue (rename to «Q4. OEE-канал», drop «бонус»).

---

## 8. Baseline / counterfactual mandate check (ENFORCED)

**Sample 15 measurable claims** в speech body:

| # | Claim | Speech context | Baseline/counterfactual? | Verdict |
|---|---|---|---|---|
| 1 | «–47% простоев, –48% брака» IBM Watson | L261 | «Внедрений масштаба не материализовалось» — explicit counterfactual ✓ | ✓ |
| 2 | «4 миллиарда сожжено» GE Predix | L259 | «vs цель к 2020 — 15 миллиардов; реальность — 12» — баланс есть ✓ | ✓ |
| 3 | «3 миллиарда субсидий... менее 1,5 тыс рабочих» Foxconn | L99, L263 | «vs обещанные 10 миллиардов / 13 тыс» — explicit ✓ | ✓ |
| 4 | «78% / 5,5%» McKinsey | L101, L171 | denominator clear (organisations using AI / high-performers) ✓ | ✓ |
| 5 | «380% overrun, 14 мес» MIT | L173 | average + median framed; baseline implicit (vs planned) ✓ | ⚠ partial |
| 6 | «80,3%» RAND | L101, L173 | «not delivering claimed value» — counterfactual implicit ✓ | ✓ |
| 7 | «20-30% снижения брака» BASF Geismar | L471 | «по индустриальным обзорам» — но не attributed Geismar-specific; chapter qualifies «точная цифра не приводится». **Speech doesn't carry that nuance.** | **✗ P1-3** |
| 8 | «+20 000 доз вакцины» Pfizer | L473 | «Заявка» — vendor-claim framing ✓ implicit baseline=plant-claim | ⚠ partial |
| 9 | «35 дней автономного контроля» FKDPP | L493 | event-historical, не «X% better than PID» — баланс не нужен ✓ | ✓ |
| 10 | «–25% простоев не равно +25% OEE» | L181, L349 | EXPLICIT counterfactual rule ✓ | ✓ |
| 11 | «–20% простоев» Tata Steel | L343 | «в горячей прокатке» context, no period baseline | ⚠ partial |
| 12 | «1-10 ms vs 100-500 ms» PLC vs LLM | L227, L541 | explicit ratio baseline ✓ | ✓ |
| 13 | «5-15% улучшение выхода годного» TSMC | L289 | «отраслевая оценка, не финансовая отчётность» — explicit qualifier ✓ | ✓ |
| 14 | «12% снижение энергозатрат» VW Познань | L293 | «на заводе в Познани» — site-specific, no period | ⚠ partial |
| 15 | «25-40% / 15-20% / 5-10% / 0-2%» McKinsey quartiles | L345 | EXPLICIT distribution baseline ✓ excellent |  ✓ |

**Score:** 11/15 explicit baselines, 4 partial. **P1-3** is real (BASF Geismar nuance lost in speech). Tata Steel + VW Познань — partial — minor risk if students cite without context.

**P2-6.** Add «base period» framing to Tata Steel + VW Познань если речь reviewer flags.

---

## 9. No-timing / no-methodology in narrative check

**Timing in narrative body:**
- Slide-header lines `### [Слайд N — title] hh:mm–hh:mm` — **OK** (lecturer directive, not body).
- Pre-flight section: timing references «За день», «За 30 минут до» — OK (frontmatter zone).
- **Narrative body** «Сейчас 12 минут раздела» / «На этом этапе» / «методически важно» — **0 hits**. ✓ Clean.

**Methodology leaks in narrative body:**
- L587: «Различать заявление для прессы и измеримый эффект — часть учебной цели **LO2**.» — **LO2 visible** in body.
- L739: «Это и есть критическое суждение — главная цель **LO8**.» — **LO8 visible** in body.

**P1-4 (anti-pattern, per CLAUDE.md «No Extra Content Rule»):** 2 LO-codes leak visible to student. Move to speaker_notes / frontmatter; replace in narrative с descriptive phrasing («это и есть критическое суждение, которому учит курс» / «различать декларацию и эффект — навык, который мы тренируем»).

**Anglicism leaks in narrative body** (post-allowlist filtering, see /tmp/deep_scan_body.py):
- L789: «**Production** с человеком в цикле» → «Промышленная эксплуатация с человеком в цикле».
- L793: «Сквозной вывод на уровне **keystone**» → «уровне несущей оси» / «keystone-оси».
- L499: «**Control-Informed RL**, 2024-2026» — canonical term, acceptable, но добавить inline gloss («контролируемое посредством PID RL»).

**P1-5 (rolled into P1-4 anti-pattern bucket):** 3 anglicism leaks в visible body. Russification check Лекция-8 mandate.

**Other Latin tokens checked:** ISO, FDA, GAMP, ATEX, SIL — established RU industrial acronyms, OK. Brand names (Tesla, BMW, Pfizer и т.д.) — allowlisted. «GitHub» (L583) — used as metaphor для СИБУР marketplace; acceptable.

---

## 10. Anti-pattern checks

- **«Магическая пилюля» tone:** every AI-benefit framed с границей. ✓ Examples: L221-231 (foundation models = augmentation, not controller), L317 «ИИ обнаруживает дефекты, но не создаёт качество», L477-479 «рекомендация, не автономия», L767 «фильтр в обе стороны». Strong.
- **Speech reads chapter verbatim?** No — speech is conversational paraphrase. Examples: chapter L272 «BASF Geismar (Луизиана, США) — крупнейший интегрированный химический комплекс...» vs speech L471 «**BASF Geismar.** Крупнейший интегрированный химический комплекс BASF в США. Мягкие сенсоры в реальном времени.» — paraphrased, shorter. ✓
- **Speech ignores slides?** No — every `### [Слайд N — ...]` header references; `[На слайде — ...]` directives describe visual; transitions explicit. ✓
- **Designer-extras leak?** N/A для speech, but speech respects slide-structure (no orphans).

---

## P0 / P1 / P2 Issues

### P0 (0)
*None.*

### P1 (4)

**P1-1. Q5 vendor question drift between slide s38 ↔ speech/chapter.**
Speech (L837) + chapter §5.2 Q5 = «3 documented failures за последние 24 месяца». Slide s38 Q5 = «Архитектурный класс» (chat vs controller). Source of truth (chapter) aligned to speech. **Slide is wrong**, not speech.
**Recommendation:** Fix slide s38 — replace Q5 «Архитектурный класс» с «Прошлые провалы». consistency-checker должен flag.

**P1-2. Chapter §5.2 frames Q4 as «бонус», speech makes it Q4-of-5 hard.**
Chapter L289 «**Бонус — OEE-вопрос**». Speech L835 «**Четвёртый — OEE-вопрос**». Reader sees inconsistent numbering. Resolve в chapter glue: rename to «Вопрос 4. OEE-канал» (drop «бонус» framing) или в speech smooth «И четвёртый — OEE-вопрос (его иногда называют бонусным)».

**P1-3. BASF Geismar baseline attribution lost in speech.**
Speech L471 «По индустриальным обзорам — двадцать-тридцать процентов снижения брака партий» (presented as Geismar-specific). Chapter L272 explicitly: «точная цифра по конкретно заводу Geismar в открытых документах BASF не приводится». **Speech loses the qualifier.**
**Recommendation:** Speech update L471 — «По индустриальным обзорам внедрений мягких сенсоров в нефтехимии — двадцать-тридцать процентов снижения брака; конкретная цифра по Geismar в открытых документах BASF не приводится».

**P1-4. LO-codes (LO2, LO8) + anglicism leaks («Production», «keystone») visible в narrative body — anti-pattern per CLAUDE.md.**
**Recommendation:**
- L587 «учебной цели LO2» → «учебной цели курса — различать декларацию и эффект».
- L739 «главная цель LO8» → «главная цель курса».
- L789 «Production с человеком в цикле» → «Промышленная эксплуатация с человеком в цикле».
- L793 «на уровне keystone» → «на уровне несущей оси лекции».

### P2 (7)

**P2-1.** Producer self-report «68-70% failure-bucket» преувеличен (recount = 41.1%). frontmatter `strict_in_share: ~42%` accurate. Reconcile producer report message.

**P2-2.** Cornerstones count: producer says «11/11 present»; canonical 10 (per plan v2). Either reconcile to 10 или explicitly name 11-й (Bainbridge paradox?).

**P2-3.** Раздел 2 divider L279 minimal («**Второй раздел из пяти.** Дискретное производство глубоко.»). Acceptable, но could add ramp sentence.

**P2-4.** Recovery cards могли бы включить «если timing превышен — какие sentences skip-able» — lesson из Лекции 9.

**P2-5.** s34c brewery 84.0 wpm (elevated). Не violation, но 12-камер architectural detail можно сократить.

**P2-6.** Tata Steel «–20% простоев в горячей прокатке» + VW Познань «12% энергозатрат» — partial baselines. Add «за период N» если producer хочет polished.

**P2-7.** s39 closing 90.0 wpm — near zero-tolerance cap. Add 20-30 sec breathing or 10-15% trim.

---

## Recommendations for Phase 11 revision

Polish-batch для speech-writer (или book-editor batched per multi-artifact rule):

1. **Fix P1-4 anti-pattern (Russification + LO codes):** 5 line edits (L587, L739, L789, L793, optional L499).
2. **Fix P1-3 BASF baseline:** 1 line edit (L471).
3. **Cross-artifact P1-1 + P1-2 (vendor Q5 + Q4 framing):**
   - Slide s38: replace Q5 «Архитектурный класс» → «Прошлые провалы» (matches chapter+speech).
   - Chapter §5.2: rename «Бонус — OEE-вопрос» → «Вопрос 4. OEE-канал».
4. **Producer message reconciliation (P2-1, P2-2):** clarify strict-in 41% (not 68-70%); cornerstones 10 canonical (Bainbridge как 11-й — call it).
5. **Optional polish (P2-3 — P2-7):** at owner's discretion.

Phase 11 single-batch revision agent (book-editor) handles speech + chapter glue + s38 fix together — Anti-pattern «Per-artifact spawns for polish rounds» из CLAUDE.md.

---

## Acceptance summary

| DoD metric | Producer claim | Independent verify | Status |
|---|---|---|---|
| WPM ≤ 95 per fragment | 0/41 violations | 0/41 violations (max 90.0) | ✓ PASS |
| AI-Failure strict-in ≥30% | «68-70%» (inflated) | **41.1%** (per-section min 30.9%) | ✓ PASS, claim reconciled |
| Cornerstones 10 | «11/11» | 10/10 canonical present | ✓ PASS, count reconciled |
| Pre-flight ≥10 items actionable | 10 | 10 day-before + 4 30-min + 3 recovery + 3 day-of | ✓ PASS |
| 3 worked examples full | yes | Pfizer + avionics + brewery full + bi-directional explicit | ✓ PASS |
| 5 vendor questions aligned | yes | Speech ↔ chapter aligned; **slide s38 Q5 drift** | ✗ P1-1 (slide-side) |
| Russification ≤ 6 unique Latin tokens | yes (6) | 21 non-allowlisted; 3 narrative-body leaks (Production/keystone/Control-Informed) | ⚠ P1-4 (3 fixable leaks) |
| Conversational register | 12 inclusive markers | 12 + storytelling beats verified | ✓ PASS |
| No timing/methodology в narrative body | yes | 2 LO leaks (L587, L739) | ⚠ P1-4 |
| Baseline/counterfactual for measurable claims | n/a producer-reported | 11/15 explicit, 4 partial, 1 lost qualifier (BASF) | ⚠ P1-3 |

**Verdict reaffirmed: APPROVE-WITH-POLISH.** Speech v1 — ready for Phase 11 polish-batch; не нужен полный re-spawn.

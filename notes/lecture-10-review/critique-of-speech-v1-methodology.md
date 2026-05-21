# Methodology critique — lec-10 speech v1

**Date:** 2026-05-21
**Reviewer:** methodology-critic
**Target:** `library/lectures/lec-10/speech.md` (860 строк / 5,729 слов narrative + 432 Q&A / 75 мин)
**Source-of-truth:** `chapter.md` v3.2 + chapter-part2/3 + `deck.yaml` v2 + 43 slides v2

## VERDICT

**APPROVE-WITH-POLISH** (2 P1 + 6 P2). Speech v1 готов к USER GATE C **с двумя корректировками перед записью**: glossary alignment (s04) + Cainthus pacing (s25 = 95.1 wpm, на 0.1 над cap). Все ENFORCED-mandate проверки пройдены независимо: strict-in 46.5% holistic (cap 30%), baseline coverage 10/10 (100%), keystone-axis explicit в s05, LO1a tools-per-level полный 25/25, LO5 criteria все 5 названы, misattribution warnings 5/5 carry-forward, anonymization clean, pacing 76.4 wpm avg.

Speech фактически выполнен на уровне deliverable-ready. Counter-check: 2 P1 < 5 P1 threshold → APPROVE-WITH-POLISH корректно (не REVISE).

---

## Counter-check results (независимая верификация)

### 1. Strict-in distribution (ENFORCED ≥30% holistic, distributed)

**Self-report:** ~42% strict holistic distributed across §1-§6.
**Independent (slide-level bucketing):** **46.5% strict-in** (20/43), 11.6% partial (5/43), 41.9% out (18/43).

Per-section breakdown:

| Раздел | Slides | Strict-in | Partial | % strict |
|---|---|---|---|---|
| Р0 (s01-s06) | 6 | 2 | 1 | 33% |
| Р1 (s07-s15) | 9 | 5 | 1 | 56% |
| Р2 (s16-s21+s17) | 6 | 4 | 0 | 67% |
| Р3 (s22-s26) | 5 | 2 | 0 | 40% |
| Р4 (s27-s32) | 6 | 1 | 2 | 17%  ← lowest, but covered by §4-bis adjacent |
| Р4-bis (s33-s35) | 4 | 3 | 0 | 75% |
| Р5 (s36-s38) | 7 | 3 | 1 | 43% |

**Verdict:** PASS. **Никакой single-cluster concentration**: failure-блоки + criteria + alternatives распределены по 7 секциям. Р4 = 17% local low, но context: Р4 содержит CMAX worked example (operationally tied к LO5 через бизнес-модельный урок), а strict-in материал концентрирован в смежной Р4-bis (75%). Combined Р4+Р4-bis = 4/10 = 40%. OK.

L10 = L4-L17 (intermediate) → waiver НЕ доступен; mandate 30% MET.

### 2. Baseline / Counterfactual coverage (NEW ENFORCED)

Sample 10 measurable claims проверен:

| Claim | Headline present | Baseline/denominator inline |
|---|---|---|
| See & Spray 5M acres | YES | YES (~полпроцента 900M, -50% гербицидов, +2 bu/A) |
| Plenty $940M loss | YES | YES (с $1.9B до <$15M, -99%) |
| Plantix 10M downloads | YES (десять миллионов) | YES (120M Indian farms, ~8% покрытия, ~100k bad recs/year) |
| Cognitive Pilot 1700+ | YES | YES (130k комбайнов России, ~1.3%) |
| Магнит 46 РЦ | YES | YES (пилот 3 РЦ, план 10-20 к 2027) |
| Cargill $32k savings | YES | YES ($8M hedge, 45 bp manual baseline → 8 bp CMAX) |
| SenseHub 2M cows | YES | YES (265M global, 3/4%) |
| Carbon Robotics 250k acres | YES | YES (3-4 years payback, $1.4M cost, 14 стран) |
| Verra 94% phantom | YES | YES (Pachama 8×, rainforest scope) |
| USDA $3.1B program | YES | YES (0.36% US пашни, 14k ферм, 3.2M acres) |

**Verdict:** PASS 10/10 = 100%. Все measurable claims произнесены WITH baseline/counterfactual/denominator. **Lec-9 lesson «baseline mandate» соблюден exemplary.**

### 3. Anti-anglicism deep scan (independent)

**Self-report:** «<30 critical narrative hits после finalize pass».
**Independent broad-regex deep scan:** **43 critical hits** в narrative body (тонкий стационарный grep по top-30 blacklist + L10-specific). Distribution:

- `AI-MRV` / `MRV` — 12 (term, used as canonical в академическом дискурсе voluntary carbon, defensible BUT 4 of these можно RU-glose: «системы верификации»)
- `notional` — 4 (financial term, defensible с inline gloss «номинальная сумма» при первом упоминании; speech не glossing)
- `Edge ML` / `edge-AI` / `Edge-AI` — 5 (technical term)
- `closed-loop` / `open-environment` — 5 (course-scaffold per cornerstone §7.2, defensible)
- `unit-economics` — 2 (canonical RU «юнит-экономика» или «структурная экономика», используется ad-hoc)
- `production` (1x) / `production-внедрений` (1x) / `production` ещё 2 — 4 (RU = «промышленная эксплуатация», уже используется в других местах speech как RU; **inconsistency**)
- `vendor lock-in` / `Vendor-self-report` — 2 (RU = «привязка к поставщику» уже используется параллельно — drift)
- `Demo not equal deployment` — 1 (как анг.-цитата pattern, в финале §s19 — лектор произносит англ. термин без RU перевода)
- `customer references`, `regulatory filings` — 2 (в s35c checklist; RU = «отзывы клиентов», «отчёты регуляторам»)
- `commodity` — 1 (RU = «биржевой товар» / «сырьё»)
- `takeaway` — 1 (в s38s, RU = «главный вывод»)
- `specialization`, `compliance teams`, `compliance` — 4 (compliance используется 2× alongside «соответствие нормам» — drift)
- `supply chain` — 1 (используется при том, что весь deck использует RU «цепочка поставок» — drift)
- `deployment` — 1
- `predictive maintenance` — 0
- `accuracy`, `edge case`, `baseline`, `pipeline`, `tradeoff`, `insight`, `best practice`, `use case`, `verbatim` — все 0

**Verdict:** **PARTIAL FAIL** — self-report underestimated by ~43%. 43 hits vs «<30». **Severity P1 (not P0):** все 43 hits — либо canonical-defensible (AI-MRV в Раздел 4 strict-in, closed-loop как cornerstone), либо узкий drift (1-2 occurrences); НЕ массовое invasion как Лекция 8 v1 (919 hits). Speech v1 — приемлемо для GATE C, **но self-report «<30 critical» — flag «inflated self-report»** (Лекция 8 pattern). Speech v2 / pre-record pass должен прицельно убрать 10-15 hits: production → «промышленная эксплуатация» (4 swaps), vendor lock-in → «привязка к поставщику» (1 swap), compliance / compliance teams → «соответствие/команда compliance» с RU framing (4 swaps), customer references / regulatory filings → «отзывы клиентов / отчёты регуляторам» (2 swaps в s35c), notional → «с номинальной суммой» при первом упоминании (s29 + s31 + s35c — 4 swaps), takeaway → «главный вывод» (1 swap), supply chain → «цепочка поставок» (1 swap), unit-economics → «структурная экономика» (2 swaps), specialization → «специализация/узкая ниша» (1 swap), commodity → «биржевой товар» (1 swap), «Demo not equal deployment» → «Демо не равно промышленному внедрению» (1 swap). Это атомарные правки, не структурная переработка.

### 4. Keystone-axis presentation (ENFORCED)

s05 «Keystone: лестница пяти уровней» — **explicit + standalone**. Заголовок «Keystone: лестница» + первые 5 предложений несут саму ось (пять уровней, типы сред, working/failure case per level), не защищают курс / не делают recap. Closing s37 callback к s05 + s01 explicit «Лестница — карта инженерных решений». **Verdict: PASS.**

Bonus: paradox enthymeme в s05 — «Венчурные инвестиции в AI для поля и роботов обвалились — минус 91% YoY. Инвестиции в агентный AI растут двузначно. Причина — скорость обратной связи» — соединяет ось с экономикой отрасли. Это сильное methodological hook на ось.

### 5. AP2a framing (Cognitive Pilot vs ИТЭЛМА)

s17: **explicitly framed** как «архитектурный выбор внутри AI-домена» с явным contrast against FarmWise («где альтернатива — вообще не AI»). Цитата: «Иногда правильный выбор — другой класс AI. Иногда — не AI вообще. ... Это архитектурный выбор внутри AI-домена. Отличается от FarmWise, где альтернатива — вообще не AI». **Verdict: PASS** — методически корректно зафиксировано, AP2a inline в speech body (не только в chapter §2.7), студент в зале слышит framing.

### 6. Hook + closing callback

s01 hook — dramatic, time-evergreen (2023→2024→2025 timeline, не volatile model benchmark), engaging «delegation→empty warehouse» visual + suspended question. **PASS.**

s37 closing payoff — verbatim explicit «Plenty не закрылась из-за плохого AI. Закрылась из-за термодинамики LED» + recap «контроллер работал, CV распознавал, модели обучены» + AP1 наименование + bridge на каждый L → «карта инженерных решений». **PASS.**

s37 Bridge к Lec-11: «cyber-physical manufacturing... ближе к L4-L5 по контролю, но с физическим контактом AI с продуктом как в L2». Foreshadow + framework continuity явные. **PASS.**

### 7. Misattribution warnings carry-forward

Chapter §8 lists 7 warnings; **5/5 critical ones preserved в speech body** (3 верифицированы explicit, 2 в Q&A):

- Indigo Ag НЕ в Verra-скандале → s31 verbatim
- Tract = data backbone, НЕ агентный → s30 «Tract — не агентный AI. Это data backbone»
- Cainthus ≠ Connecterra → s25 «Cainthus и Connecterra — разные компании»
- Saga UV-C ≠ harvest → s18 «Saga делает ультрафиолетовую обработку клубники ночью... Не сбор клубники. В обзорах часто путают»
- Verra phantom = rainforest, не all AI-MRV → s31 «Verra phantom credits относятся к rainforest offset projects»
- Nature Food Tzachor (НЕ West/Williams) → s12 «Главный автор — доктор Асаф Цахор»
- РСХБ AI заявлено, метрик нет → s32 «AI-сервисы анонсирует... независимая верификация метрик отсутствует»

**Verdict: PASS 7/7.**

### 8. Pacing (≤ 95 wpm cap mandate)

Per-slide WPM scan (43 slides):
- Avg WPM: **76.4** (target ≤85, comfortable)
- Slides over 95 cap: **1/43** — s25 «Cainthus, tie-stall, Holstein-bias» = **95.1 wpm** (на 0.1 над cap)
- Self-report «0/43 over 95» — **off by 0.1 wpm** на одном слайде

**Top-3 heaviest slides:**
- s17 (Cog vs ИТЭЛМА): 91.2 wpm — heaviest concept slide, под cap но tight
- s31 (USDA + Verra): 91.2 wpm — двойной failure, под cap
- s30b (Мелитополь двойная оптика): 91.6 wpm — под cap
- s29 (CMAX worked): 90.0 wpm — концептуально heavy, под cap
- s25 (Cainthus tie-stall Holstein): 95.1 wpm — **OVER CAP**

**Verdict: NEAR-PASS** — single 0.1 wpm violation на s25; trivial fix: split 1 предложение / добавить 1 пауза = -3 wpm под 92.

### 9. Anonymization

Independent grep на МГТУ / Бауман / ИУ6 / МСХА / Тимирязевка — **0 hits в body** (1 hit на каждый pattern попал в frontmatter excluded_items, который сам декларирует «0 hits» — ложная позитивная тревога grep на негативную самопроверку). **PASS.**

Career section §s36c — родовая форма: «профильные технические и аграрные университеты с магистерскими программами по agro-IT» — анонимизирована корректно.

### 10. Cornerstone glossary alignment (cross-artifact)

Chapter §7 lists 7 cornerstone concepts. Speech glossary slide (s04) covers only 2/7 (closed-loop vs open-environment + AI-MRV частично).

**Speech glossary s04 actually presents:**
1. open-environment / closed-loop AI ✓
2. Агентный AI ← НЕ в chapter cornerstone (новый термин в s04)
3. Базисные пункты ← НЕ в chapter cornerstone
4. Расхождение хеджа ← НЕ в chapter cornerstone
5. Выбросы третьего уровня ← НЕ в chapter cornerstone
6. AI-MRV ✓

**Chapter cornerstone MISSING from speech body:**
- ✓ Точное земледелие (упоминается в body «прецизионного земледелия»)
- ✓ Edge ML / TinyML (упоминается в s34 body)
- **NO «Tacit knowledge / hyperlocal context»** — никогда не упомянуто в speech (потерянная концепция)
- ✓ Vendor lock-in / right-to-repair (упоминается в s30b body)
- ✓ Foundation model + RAG (s09 body)
- **NO «Sustainability paradox»** — никогда не упомянут в speech, а Раздел 4-bis §5.4 chapter — целый блок про это с numerical illustration (data centers в Айове)

**Verdict: PARTIAL FAIL** — speech добавляет 4 новых термина в glossary (L4-relevant: agentic, basis-points, hedge slippage, scope-3), что нормально (это L4 vocabulary, нужное для s28-s31), но **полностью теряет 2 cornerstone concepts**: Tacit knowledge + Sustainability paradox. Chapter §7.4 «tacit knowledge — структурная причина того, что обобщённый AI-агроном — антипаттерн» — это часть AP4 explanation; в speech AP4 (s12) этой причинной цепочки нет. Chapter §5.4 sustainability paradox (data centers потребляют billions of gallons) — стратегический урок класса «AI carbon footprint paradox», который нужен для AP7 framing.

**Severity P1.** Recommended fix:
- Add 1 sentence в s12 (ChatGPT-агроном): «Tacit knowledge фермера — неявные знания о конкретном поле, годами наблюдаемые — AI не строит из satellite и IoT за один сезон; это структурная причина provala generic LLM как агронома».
- Add 1 sentence или mini-block в s32 / s37 на sustainability paradox: «И ещё критерий: AI для устойчивости имеет собственный экологический след — data centers в Айове потребляют миллиарды галлонов воды в год; net-positive — не автоматическое свойство, его нужно специально считать».

### 11. Pre-flight checklist actionability

Все 10 items в «Подготовка перед лекцией (за 24-48 часов)» — operational: file paths, URLs concrete, callback-points named, fallback plan two-tier (PDF → paper). Time-budgeted («за 24-48 часов»). **PASS.**

### 12. Scaffold leak check (slide cross-references)

Independent regex на `[VERIFY-DAY-OF]` / `[FACT-CHECK]` / `LO[1-9]` / `§\d` / `AP[1-9]` / `L\d.\d` codes в visible body — **0 hits.** Speech использует natural «как видите на слайде» / «давайте посмотрим на цифры» / «к этому переходим» / «Переход на s06» (stage direction в []) — корректно. **PASS.**

### 13. Conversational tone

«Мы с вами» — **13 occurrences** distributed: s03 («навык, который мы с вами тренируем»), s07 («увидим много раз»), s08 («давайте мы с вами на них посмотрим»), s17 («давайте мы с вами посмотрим»), s25 («должны явно проговорить»), s29 («давайте мы с вами разберём»), s30b («должны её проговорить»), s34 («Обратите внимание»), s35 («которое мы с вами проговорим»), s37 («возвращаемся»), s37 («Лестница — карта»), s38s («соберём в одну матрицу»), s35c («уносим из лекции»). **PASS** (target ≥10).

Rhetorical questions/pauses: «[пауза 3 секунды]» / «[медленно, центральная мысль]» / «[пауза, пример]» — stage directions consistent. PASS.

---

## P0 issues (mandatory fix)

**None.** Speech v1 проходит все ENFORCED-mandate gates.

---

## P1 issues (2)

### P1-1. Cornerstone glossary cross-artifact gap — 2 missing concepts

**Issue:** Speech body теряет 2 из 7 cornerstone concepts из chapter §7 — **Tacit knowledge / hyperlocal context** + **Sustainability paradox** — никогда не произносятся. AP4 (generic LLM antipattern) теряет одно из своих 2 structural объяснений (tacit knowledge), AP7 теряет parallel концепцию (sustainability paradox).
**Evidence:**
- chapter §7.4: «ИИ не может построить эти знания из satellite + IoT за один сезон. Это структурная причина того, что "обобщённый AI-агроном" — антипаттерн» → speech s12 (AP4) этой причины не называет.
- chapter §5.4: целый раздел «Sustainability paradox + AI-MRV» (data centers в Айове, GPT-3 training water) → speech полностью пропускает.
**Recommendation (speech v2):**
- s12 (ChatGPT-агроном) — добавить 1 предложение после «critical разбор»: «Структурная причина — tacit knowledge: неявные знания фермера о конкретном поле, годами наблюдаемые, AI не строит за один сезон из спутника и IoT. Это и есть категорический антипаттерн».
- s37 (closing payback) или новый mini-block в s31/s32 — добавить sustainability paradox: «Шестой критерий, оставшийся за скобками: AI для устойчивости имеет собственный экологический след. Data centers в Айове потребляют миллиарды галлонов воды в год. Net-positive — не автоматическое свойство, его нужно специально считать».
**Cost:** ~50-80 слов добавки на 2 spots, нет structural risk; WPM impact <1 на обоих слайдах.

### P1-2. Anti-anglicism inflation in self-report

**Issue:** Self-report «<30 critical narrative hits» при independent count **43**. Не critical sub-failure типа Лекция 8 (где 919 hits в speech), но pattern «inflated self-report» — флаг по Лекция 8 lesson. Drift в consistency: production / vendor lock-in / compliance / supply chain используются BOTH как RU AND как англицизм в одном артефакте (внутренняя несогласованность).
**Evidence:**
- s07: «промышленных внедрений» (RU) ↔ s35c: «production-внедрений» (англ.) — drift на одной и той же концепции.
- s12: «categorический антипаттерн» (RU) ↔ s35c «compliance teams» (англ.) — drift.
- s38s: «главный takeaway» — единственный случай в speech, без RU alternative; должен быть «главный вывод».
- s30b: «vendor control surface» используется параллельно с «привязка к поставщику» — non-issue (canonical в FTC context) но drift в narrative weight.
**Recommendation (speech v2):** атомарные swaps ~15 hits на RU equivalents с canonical exception list (AI-MRV в strict-in §31, closed-loop / open-environment как cornerstone, RAG, edge-AI как технический термин). Все остальные 13-15 hits — drift к RU. См. список в counter-check #3.
**Cost:** atomic find-replace, ~10 минут, не требует pacing recompute.

---

## P2 nits (6)

### P2-1. s25 «Cainthus, tie-stall, Holstein-bias» pacing 95.1 wpm (cap 95)
**Issue:** 0.1 wpm над cap. Self-report «0/43 over 95» off by единичная epsilon.
**Fix:** split последнее предложение Holstein-bias на 2 + добавить «[пауза]» = -3 wpm. ~30 секунд работы.

### P2-2. Slide ordering anomaly (s17 после s21)
**Issue:** Slide order в speech body: s16 → s18 → s19 → s20 → s21 → s17 → s22. **s17 (Cognitive vs ИТЭЛМА) физически last в Разделе 2**, но IDs из deck.yaml suggest natural order s16-s17-s18. Speech перевернул, чтобы s17 был finale Раздела 2 как «самый методически важный кейс».
**Verdict:** **OK by design** (это lectur-narrative reorder, deck visual order остается), но рекомендуется добавить inline note в pre-flight checklist `[ORDER]` для лектора: «s17 идёт ПОСЛЕ s21, не между s16 и s18 — narrative reason: финализирует Раздел 2 на самой важной AP2a мысли».
**Cost:** 1 строка в чеклист.

### P2-3. s05 keystone «-91% YoY» — нужен `[VFY-day-of]` marker
**Issue:** «Венчурные инвестиции в AI для поля и роботов обвалились — минус девяносто один процент год к году». AgFunder source — 2024-2025; в speech как 2026 факт. Volatile, требует verify-on-day per chapter changelog markers.
**Fix:** add to pre-flight checklist: «[s05 freshness] подтвердить «-91% YoY» индекс indoor farming для season 2025-2026 (AgFunder 2026 H1 update)».

### P2-4. s09 foundation models — «два-три foundation models» под-pace и over-claim
**Issue:** «Концентрация на двух-трёх foundation models — IBM, NASA, ESA». В chapter §1.3 namesake list — TerraMind (IBM+ESA), Prithvi-EO 2.0 (NASA+IBM), AgriFM (HKU+Wuhan), Crop Wizard (Illinois RAG). По числу — 4+ распределённых vendors, не «два-три IBM/NASA/ESA». Speech упрощает narrative до западного big-tech concentration.
**Fix:** s09 body: «Концентрация на нескольких foundation models. Большая часть — IBM, NASA, ESA orbit; есть и University of Hong Kong (AgriFM), Иллинойс (Crop Wizard RAG)».
**Cost:** +6 слов; pacing impact <1 wpm.

### P2-5. s32 «Sber GigaChat agronomy exam» mini-fragment без contextualizing critic
**Issue:** «Sber GigaChat в одном эпизоде был представлен как "сдавший экзамен по агрономии". Демо, не промышленное внедрение». Это правильное critic-framing, но «один эпизод» — vague: год / scope не дан. Студент может неверно интерпретировать как «GigaChat = AI агроном in production РФ».
**Fix:** «В одном промо-эпизоде Сбера 2024 GigaChat был представлен как "сдавший экзамен по агрономии". Это демо-уровень, не промышленное внедрение в АПК».
**Cost:** +5 слов; chapter §4.7 part 2 имеет date — sync to speech.

### P2-6. Q&A backup секция (832-863) не озаглавлена как **«for lecturer only»**
**Issue:** Speech ends с «Q&A — запасные тезисы для лектора» (line 832). Reasonable для лектора, но если speech используется как handout для студентов — backup тезисы могут быть прочитаны как авторитетные ответы. Add visible marker:
**Fix:** заголовок «## Q&A — запасные тезисы для лектора **[НЕ ДЛЯ РАЗДАЧИ СТУДЕНТАМ]**».
**Cost:** 1 строка.

---

## What works well (top 5 strengths)

1. **Strict-in distribution exemplary.** 46.5% holistic, 7-section spread (33-75% per section), нет single-cluster. Failure-блоки F1-F11 организованы 1.5-2 на раздел; criteria AP1-AP7 распределены по 7 разделам; alternatives к каждому failure named. По методическому mandate курса — образцовое исполнение «учить говорить нет» (AI-Failure & Judgment Rule).

2. **Baseline coverage 10/10 = 100%.** Каждая measurable claim произнесена WITH denominator/baseline/counterfactual словами: «5M акров — полпроцента 900M пашни США», «1700 установок — 1.3% от 130k комбайнов», «2M коров — три четверти процента от 265M». Lec-9 lesson «baseline mandate» — implemented exemplary.

3. **Keystone-axis presentation strong + late-bound callback.** s05 standalone keystone (заголовок про ось, первые 5 предложений несут лестницу), затем callback в s37 explicit «Лестница — карта инженерных решений». Между ними — paradox enthymeme («-91% YoY поле vs двузначный рост агентного AI») как methodological hook на ось. Это not «course-scaffold», а live conceptual анализ.

4. **AP2a vs AP2b framing precision.** s17 (Cognitive vs ИТЭЛМА) явно отделён от FarmWise (AP2b genuine non-AI): «Иногда правильный выбор — другой класс AI. Иногда — не AI вообще. Это архитектурный выбор внутри AI-домена. Отличается от FarmWise». Это устраняет частый misframing «AI vs не-AI» в речи лектора.

5. **Hook→payoff closure tight.** s01 hook («что именно сделал AI в этом провале — и в каком смысле не смог сделать?») явно re-opened в s37: «Мы спросили: что сделал AI в этом провале... Ответ. Plenty не закрылась из-за плохого AI. Закрылась из-за термодинамики LED». Чистый методический arc, не «магическая пилюля», не academia monologue.

---

## Recommendations для speech v2

**Если speech v2 запрашивается (не обязателен для USER GATE C):**

1. **P1-1 fix (cornerstone gap):** добавить 2 mini-fragments — tacit knowledge в s12 (~25 слов) + sustainability paradox в s37 или s31 (~40 слов). Total ~65 слов; WPM impact +0.5-1 wpm на затронутых слайдах.

2. **P1-2 fix (anglicism polish):** ~13-15 atomic swaps в narrative body. Time ~10-15 минут. Validate с repeat deep latin-token scan; target hits ≤25.

3. **P2-1 fix (s25 pacing):** разбить final Holstein-bias предложение, добавить [пауза]; -3 wpm = 92 wpm.

4. **P2-3,4,5 fixes (factual freshness):** add 3 line items в pre-flight checklist (s05 -91% YoY verify, s32 GigaChat year clarification, s09 vendor list expand).

5. **P2-2,6 fixes (orderings/labels):** 2 line additions (s17 reorder note + Q&A backup label).

**Если speech v1 остаётся как-is для GATE C:** все 2 P1 + 6 P2 — на pre-record pass; speech лектора-ready как deliverable.

---

## USER GATE C ready (combined w/ chapter v3.2 + slides v2)?

**YES** — APPROVE-WITH-POLISH; speech v1 deliverable-ready с 2 P1 (cornerstone + anglicism) на pre-record polish pass. Combined с chapter v3.2 (approved) + slides v2 (approved) — все 3 артефакта соответствуют DoD. Strict-in mandate cleared at speech level (46.5%). Baseline mandate cleared at speech level (10/10). Misattribution carry-forward 7/7. Keystone-axis preserved. Lec-N+1 bridge present. Conversational tone genuine. Anti-anglicism slight self-inflation (43 vs <30) но не P0/REVISE threshold.

**Top 3 concerns for record day:**
1. Cornerstone glossary gap — sustainability paradox + tacit knowledge missing (P1-1).
2. Anti-anglicism drift на ~13-15 narrative tokens (P1-2).
3. s25 pacing 95.1 wpm на самом краю cap (P2-1).

**Top 3 strengths:**
1. Strict-in 46.5% with no single-cluster.
2. 100% baseline coverage на measurable claims.
3. Hook→payoff arc + AP2a precise framing + bridge к Lec-11.

---

**Severity counts:** P0=0 · P1=2 · P2=6 · Total: 8 issues.
**Verdict:** **APPROVE-WITH-POLISH** (2 P1 < 5 threshold per Pre-USER-GATE Walkthrough Rule).

# Methodology Critic Report — Лекция 11 Chapter v3 — 2026-05-21

**VERDICT: REVISE**

Counter-check: 7 P1 + 2 P0 ⇒ verdict не APPROVE-WITH-POLISH. Forced REVISE — два P0 (дублирование секции в §3.5 и порядковая инверсия §4.4 ↔ §4.5) являются структурными дефектами expansion v3, не cosmetic; их обязательно закрыть перед GATE A.

---

## Top-line summary

Chapter v3 expansion 13,4k → 29,8k слов **методически удался** на уровне kernel: keystone (Variant C, Discrete vs Process) сохранён, 5-разделовая структура + §0 + Q&A + Источники не реорганизованы, 5 LO покрыты, 8 cornerstone-терминов сохранены, 5 mandated fundamentals (OEE, эталонная разметка, OT/IT, edge determinism, label cost) deeply covered + 4 новых fundamentals (Sim2Real, Constrained RL, V-model validation, DO-178C) properly explained. **Failure-bucket strict-in** на NEW v3-контенте по независимому recount = **95,8%** (23/24 sample-блока strict-in, 1 partial); общая chapter-доля **comfortably > 30% mandate**. Worked example набор расширен с 2 до 3 (Pfizer Vox pass + авиадвигатель fail + brewery pass) — рамка теперь работает в обе стороны на 3 кейсах, не на 2. Q&A backup расширен с 8 до 14 (6 new questions — все engineering-релевантные, не management drift).

Однако expansion ввёл два P0 структурных дефекта: (a) §3.5 содержит **дублированные verbatim параграфы** «СИБУР маркетплейс» и «ММК/НЛМК/Северсталь» (lines 815/819 ≡ 823/825 — buffer-copy artifact); (b) §4.4 и §4.5 поменялись местами в body относительно TOC (TOC: §4.4 → §4.5; body: §4.5 на line 1068 → §4.4 на line 1084 → §4.6). Плюс — typo «глаz» в line 139 (hybrid Cyrillic «гла» + Latin «z», карбонная копия Лекции 1 «Манfacturing»), повтор «застревание на пилотной стадии (застревание на пилотной стадии)» в line 112 (artifact v2 Russification sweep). Pacing — chapter ≈ 3-4 ч глубокого чтения для 75-мин лекции явно overload как backing, но это **намеренно**, owner decision PR #129. **Russification** — depth fading в v3 NEW content (101 anglicism-hits в narrative body по детальному скану — больше, чем в v2 после P1-1/P1-3 fixes); особенно в Q10/Q11/Q13/Q14, §3.4 FDA warning letters, §3.6 RL drift detection методы, edge inference taxonomy. Это **regression** относительно v2 closed-P1, и требует focused sweep на v3-added блоки.

---

## P0 issues (BLOCKING — обязательно перед GATE A)

### P0-1. §3.5 содержит дублированные verbatim параграфы (buffer-copy artifact expansion)

**Что не так.** Lines 815–819 и lines 823–825 — **identical verbatim**:
- Line 815: «**СИБУР — маркетплейс технологического моделирования.** Запуск первой версии **объявлен** компанией на первый квартал 2025 года…»
- Line 823: тот же текст слово-в-слово.
- Line 819: «**ММК / НЛМК / Северсталь.** Общие декларации применения AI без конкретных производственных метрик…»
- Line 825: тот же текст слово-в-слово.

Это **scope-creep artifact expansion**: вставлен углублённый блок «*ММК / НЛМК / Северсталь — детали.*» между двумя инстансами, и оригинальные параграфы остались внизу, не удалёны. Студент при чтении §3.5 встречает один и тот же параграф дважды через 100 слов — это **disrespectful для читателя** и breaks chapter authority.

**Why критично.** Это не tone polish — это видимый структурный дефект, который любой reader / book editor поймает в первой проверке. Карбонная копия Lec-08 16-mock fallout pattern (self-report PASS, но видимая структурная проблема при reading).

**Fix.** **Удалить duplicate** — оставить либо первый блок (lines 815/819) ДО углублённого блока, либо второй блок (lines 823/825) ПОСЛЕ; **рекомендуется удалить второй** (lines 823–825), чтобы повторение не разрывало flow §3.5.

### P0-2. §4.4 ↔ §4.5 поменялись местами в body (TOC ≠ body)

**Что не так.** TOC (lines 50–56) объявляет порядок:
- §4.1 Четыре категории
- §4.2 Матрица альтернатив
- §4.3 Worked example
- **§4.4 5-шаговая рамка**
- **§4.5 Матрица типичных режимов провала**
- §4.6 Self-check

Body имеет:
- §4.1 (line 892)
- §4.2 (line 947)
- §4.3 (line 987)
- **§4.5 (line 1068)** — Матрица типичных режимов провала **первая**
- **§4.4 (line 1084)** — 5-шаговая рамка **после §4.5**
- §4.6 (line 1098)

Это **payoff-секция главы** (LO8 central anchor). Студент, идущий по TOC, дойдёт до §4.4 и наткнётся на §4.5, что подрывает читательскую навигацию. 5-шаговая рамка должна быть payoff-замыканием §4 ДО матрицы провала (которая — summary tool на основе уже усвоенной рамки) — это **методически правильный** порядок (TOC verdict), и body нарушает его.

**Why критично.** §4 — payoff главы для LO8. 5-шаговая рамка — главный artifact для кармана; должна стоять перед матрицей failure-pattern (которая её summary-tool). Сейчас читатель видит summary-tool до самой рамки.

**Fix.** Переставить body: §4.3 → §4.4 (5-шаговая рамка) → §4.5 (матрица провала) → §4.6 (self-check). Соответствует TOC и pedagogical sequence. Альтернатива (если §4.5 действительно нужна до §4.4 как мост) — обновить TOC. Рекомендуется **первый вариант** (rearrange body), потому что §4.5 матрица — summary, не bridge.

---

## P1 issues (значимые — должны быть адресованы)

### P1-1. Russification depth regression на v3 NEW content (101 anglicism-hits в narrative body)

**Что не так.** v2 closed P1-1 + P1-3 Russification sweep; v3 expansion ввёл significant fresh anglicism load. Deep latin-token scan на narrative body:
- Канонические термины (legitimate): `baseline×10`, `production×56`, `controller×2`, `pilot purgatory×7`, `foundation model×3`, `autonomous×13`, `audit trail×4`, `edge×69` (mostly canonical «edge AI / edge-узлы» — OK), `cloud×20` (OK — «облако/cloud» dual).
- **Anglicism leak в v3 NEW content** (101 detailed hits): `Tier 1-5×18` (taxonomy §3.3), `failure mode×7`, `drift detection×4`, `safety layer×4`, `sample efficiency×4`, `false-positive×4`, `real-time×4`, `eventually-consistent×2`, `feedstock×3`, `production hell×3`, `sign-off×3`, `reward hacking`, `reward shaping`, `frozen models`, `frozen process`, `closed-loop`, `open-source`, `go/no-go`, `plug-and-play`, `hi-mix`, `low-volume`, `top-quartile`, `cross-domain`, `safe rollback`, `safety supervisor`, `feed quality`, `culture issues`, `culture of distrust`, `Inspection sequence design`, `Cross-functional inspection`, `Aesthetic judgment`, `time pressure`, `predetermined change protocol`, `Strategic decision`, `Trust gap`, `Training data gap`, `false confidence`, `engineering-grade`, `organisational adoption`, `labelled failures`, `sensor coverage`, `selective accuracy`, `Reliability diagram`, `Expected Calibration Error (ECE)`, `Covariate shift / Concept shift / Concept drift` (subheaders), `diversity sampling`, `Bottom quartile`, `Tier 1/2/3/4 — Hybrid edge + cloud` block (full English), `archive analytics`, `MC/DC coverage`, `stakeholder fragmentation`, `Truven Health Analytics / Phytel / Explorys` (OK — brand names), `Roboflow / NVIDIA Isaac Sim` (OK — brand), `production-ready`, `proposed configuration / autonomous configuration`.
- Bold-as-subheader anglicisms (heaviest): «**(a) Задержка вывода (inference latency).**», «**Анти-кейс: Honeywell aviation MRO copilot.**», «**Volkswagen DPP.**», «**Siemens Senseye — кейс "predictive maintenance as SaaS".**», «**Real FDA warning letters для AI/ML systems.**», «**Three classes методов обнаружения drift.**».
- Q&A — **самая тяжёлая secционно**:
  - Q9: «AI vendors редко показывают baseline OEE»
  - Q10: «formal verification», «manual review by certified engineer», «autonomous code generation»
  - Q11: «прирост EBITDA», «marginal contribution per unit», «annual production», «payback period», «scale-up plan», «comparable case», «conservative ROI estimate»
  - Q12: «advisory mode», «autonomous batch release», «predetermined change control plans»
  - Q13: «modelling errors», «noise characteristics», «domain randomization», «fine-tuning on real data», «conservative safety layers», «runtime monitors»
  - Q14: «Read-only mode», «Setpoint advisory», «Closed-loop с safety layer», «runtime monitor», «communication interface», «augment, не replace»

**Why критично.** Lec-08 lesson: producer self-report «0 hits» при deep scan 919 hits → owner reject. v3 self-report «0 narrative anglicisms outside whitelist» — **не соответствует** независимому deep-scan. Speech-derivation унаследует это; slides-derivation унаследует subheader-фразы как title leaks.

**Recommendation.** Targeted Russification sweep на v3-added блоки. Mapping:
- `Tier 1/2/3/4` → «Уровень 1/2/3/4» (taxonomy переименовать; brand остаётся в parens после)
- `failure mode/rate` → «режим/частота отказов»
- `drift detection` → «обнаружение дрейфа»
- `safety layer` → «защитный слой» / «слой безопасности»
- `sample efficiency` → «эффективность выборки»
- `false-positive` → «ложное срабатывание»
- `real-time` → «в реальном времени»
- `eventually-consistent` → «с конечной согласованностью» (термин canonical в распределённых системах)
- `feedstock` → «сырьё»
- `sign-off` → «подпись/одобрение»
- `closed-loop` → «замкнутый контур»
- `open-source` → «открытый исходный код»
- `go/no-go criteria` → «критерии продолжения / закрытия» (уже частично используется)
- `top-quartile` → «верхний квартиль»
- `Strategic decision` → «стратегическое решение»
- `Trust gap` → «разрыв доверия»
- `Q&A` — отдельный sweep для каждого нового Q (Q9-Q14)

Q&A — приоритет, потому что Q&A = устный материал лектора, наиболее sensitive к anglicism leak.

### P1-2. Worked examples balance — 3 examples, но 2 pass + 1 fail (asymmetric)

**Что не так.** v3 добавил третий worked example (brewery packaging CV-QC, pass). Распределение теперь: **Pfizer Vox pass + авиадвигатель fail + brewery pass** = 2 pass + 1 fail. Pedagogical balance смещён в сторону «AI fits»; рамка как фильтр (LO8 main payoff) предствляется в 33% случаев vs «AI fits» в 67%.

Counter-thought: brewery pass демонстрирует **разные критерии прохождения** (food safety vs FDA, дискретное vs процессное, asymmetry в сторону FN), что **расширяет** mental model студента. То есть it's not just redundancy.

**Why это P1 (не P2).** §4 — LO8 payoff. LO8 — «умение сказать "нет" неподходящему AI». Если 2 из 3 worked examples показывают «AI fits», a 1 из 3 — «AI не fits», читатель уносит **valence**, а не «фильтр». Это subtle, но carry-forward в slides + speech: лектор будет тратить 2 слайда на pass-кейсы, 1 на fail-кейс.

**Recommendation.** Один из двух подходов:
1. **Reorder**: переставить порядок worked examples — Pfizer Vox pass → авиадвигатель fail (показать фильтр) → brewery pass (показать pass с другими критериями). Сейчас порядок: Pfizer (pass) → авиадвигатель (fail) → brewery (pass) — уже близко к этому, но §4.3 не делает explicit transition. Добавить connective sentence перед brewery: «*Чтобы показать, что pass-кейс — не один сценарий, рассмотрим третий пример, где критерии прохождения комбинируются иначе.*»
2. **Add 4th brief**: 4-й мини-кейс fail для разности доменов (например, «AI-PdM на ядерном реакторе primary loop» — fail на категории C регуляторика). Это restores 2 pass + 2 fail balance.

Acceptable также: оставить как есть **только если** brewery explicit framing — «pass с разными критериями относительно Pfizer» — добавлено в narrative.

### P1-3. Russian-cyrillic typo «глаz» (line 139)

**Что не так.** Line 139: «*Если читаете глаz первый раз — не пытайтесь запомнить каждую цифру.*»

«глаz» = русское «гла» + латинское «z». Это hybrid character — карбонная копия Лекции 1 «Манfacturing» typo. Скорее всего, artifact case-rewrite («главу» → «глаz») или ошибка ввода.

**Why это P1, не P2.** Это **читательский trust-blocker**: в первый параграф «Как читать главу» (методическая инструкция), и студент при чтении первого раздела увидит typo. Особенно неудачное место — методический «вводный совет».

**Recommendation.** Replace на «*Если читаете главу первый раз…*».

### P1-4. Recursive parenthetical «застревание на пилотной стадии (застревание на пилотной стадии)» (line 112)

**Что не так.** Line 112: «*застревание на пилотной стадии (застревание на пилотной стадии) универсально*»

Скобки повторяют сам термин verbatim — artifact v2 Russification sweep (англ. «pilot purgatory» был в скобках после канонического RU; sweep заменил английский на канонический, но не убрал parens).

**Why это P1, не P2.** §0.1 keystone-слайд. **«Read-out-loud belt declaration»** — самое заметное место главы. Студент проходит мимо «загадочной» рекурсии в keystone и теряет confidence в авторитете chapter.

**Recommendation.** Replace: «*застревание на пилотной стадии* (англ. *pilot purgatory*) *универсально*» — это правильный Russification pattern (RU-canonical + английский original в parens первого упоминания). Или просто удалить parens: «*застревание на пилотной стадии универсально*».

### P1-5. Q&A Q11 (CFO ROI) curriculum drift к management

**Что не так.** Q11 спрашивает «*Как доказать ROI от AI на shop floor финансовому директору?*» — ответ переходит на финансовую методологию (OEE → EBITDA conversion, payback period, scale-up plan, comparable case). Это **management decision-support**, а не engineering criteria.

Сравнение с v1 Phase 3 critique P1-7: оригинальный Q9 «маленький завод» был flagged как curriculum drift к управленческой теме; ответ был переформулирован в engineering-judgment («собрано 1000+ labeled examples, OEE-baseline, операторы готовы…»). v3 Q11 — **возвращает** этот drift в более явной форме.

**Why это P1, не P2.** v3 NEW content, по spec расширяет Q&A с 8 до 14 для **engineering-релевантности**. Q11 — слабейший методически из 6 новых (Q9 OEE-vendor, Q10 LLM-SCADA, Q12 FDA-pharma, Q13 Sim2Real, Q14 legacy PLC — все engineering depth; Q11 — финансовый).

**Recommendation.** Один из двух подходов:
1. **Reframe** Q11 как engineering: «*Какая инженерная метрика убедит CFO?*» → ответ через OEE-разбивку, baseline-методологию, документированный pilot scope, а не финансовые termины (payback, EBITDA). Это **shifts question to engineering criteria**.
2. **Drop** Q11. 13 questions — adequate; Q9/Q10/Q12/Q13/Q14 — engineering depth достаточно для backup.

### P1-6. Tier 1-4 edge inference taxonomy в §3.3 — full English subheaders

**Что не так.** §3.3 (Pre-§3.4 регуляторика) содержит «*Edge inference architecture — taxonomy.*» с 4 subheader-блоками:
- «**Tier 1 — Rule-based on PLC.**»
- «**Tier 2 — Classical ML on edge gateway.**»
- «**Tier 3 — Deep learning on edge AI accelerator.**»
- «**Tier 4 — Hybrid edge + cloud.**»

Это **методические якоря** (read-out-loud formulae taxonomy edge), как «CV — последняя линия защиты, не первая» в §2.5. Студент должен запоминать эту taxonomy как 4-уровневый mental model. Subheader на английском — слабее для запоминания, чем «**Уровень 1 — правила на PLC**».

Аналогичная проблема — «**Tier 1-2-3-4 — Hybrid edge + cloud.**» в §3.3 block (full English). Параллельно §3.6 «**Three classes методов обнаружения drift**» (hybrid English/Russian — Three classes английский).

**Why это P1, не P2.** Carry-forward в slides: presentation-designer возьмёт subheader как slide-title. Если subheader = «Tier 3 — Deep learning on edge AI accelerator», slide title = «Tier 3 — Deep learning on edge AI accelerator» — leak англицизма visible body на slide. Lec-08 lesson.

**Recommendation.** RU-canonical formulations:
- Tier 1 → «**Уровень 1 — правила на PLC.**»
- Tier 2 → «**Уровень 2 — классическое ML на edge-шлюзе.**»
- Tier 3 → «**Уровень 3 — глубокое обучение на ускорителе.**»
- Tier 4 → «**Уровень 4 — гибрид edge + облако.**»

«**Three classes методов обнаружения drift.**» → «**Три класса методов обнаружения дрейфа.**»

### P1-7. §3.4 FDA warning letters блок — мост между real FDA findings и speculation, без явной верификации источников

**Что не так.** §3.4 содержит block «*Real FDA warning letters для AI/ML systems.*» с **3 named-organization claims**:
- Eli Lilly 2022 Form 483 — «data integrity issues в ML-based quality prediction»
- Pfizer 2023 Form 483 — «issues с computerized systems validation для AI-related processes»
- «Несколько generic manufacturers 2023–2024» — «issues с проверкой electronic batch records»

Footnote [36] — IntuitionLabs guide + BioPharm International — это **обзоры**, не первичные FDA FOIA records. Phrasing «(paraphrased)» в Eli Lilly entry — signals that book-editor не имел прямого access к full Form 483 text.

Если эти 3 named-organization claims не verified в первичных FOIA records, это **anti-bucket** (не documented failure + lesson, а speculation+paraphrase). Это direct echo P0-2 из Phase 3 critique (AB InBev rollback unverified).

**Why это P1, не P0.** Fact-checker domain — но methodology-критик flag because (a) если речь о named org, фактически не verified, это превращает strict-in block в partial; (b) book-editor честный label «(paraphrased)» smal помогает, но studeenт это не читает.

**Recommendation.** Один из двух подходов:
1. **Verify** через FDA FOIA / Warning Letter Search Portal — confirm Eli Lilly 2022 + Pfizer 2023 Form 483 содержат AI/ML-related findings. Если verified — drop «(paraphrased)» marker, добавить direct link.
2. **De-name** — заменить на generic-pattern phrasing: «*В период 2022-2024 FDA выпустила несколько Form 483 / Warning Letters fragмаков, где упоминались data integrity issues в ML-based quality prediction systems; конкретные исключения не раскрываются здесь для предотвращения непреднамеренной репутационной атрибуции, но pattern — public-record в FDA FOIA Warning Letter database.*» Это сохраняет strict-in lesson (FDA mandate AI validation как software) без unverified named-org claims.

---

## P2 issues (polish — carry-forward)

### P2-1. Tesla Optimus 4th hype case в §1.3 — overlap с потенциальным s09b slide

§1.3 теперь содержит **4 кейса трио провалов**: GE Predix / IBM Watson / Foxconn WI **+ Tesla Optimus**. Section heading все ещё «Трио провалов» (line 228) — должно быть «Четыре провала» либо «Трио + один».

**Recommendation.** Rename section header → «**§1.3. Четыре кейса провалов: GE Predix, IBM Watson, Foxconn WI, Tesla Optimus**» (или сохранить «Трио» и переместить Tesla Optimus в Q&A backup как Q1 ответ).

### P2-2. GM Hamtramck 1985 — referenced в §1.1 + §2.4, два раза

GM Hamtramck упомянут в §1.1 (line 149, в blок «Историческая преемственность волн автоматизации» как CIM example 1985) + §2.4 (line 449, как «GM Hamtramck (1985–1989) — предшественник Tesla 2018»). Два места — overlap.

**Recommendation.** Keep §2.4 (где это central — Hamtramck это direct precursor к Tesla 2018 lesson); из §1.1 — превратить в 1-line cross-ref «*предшественник Hamtramck — детали в §2.4*».

### P2-3. ATEX equipment categories block (lines 757–769) — heavy English markers

«**Pepperl+Fuchs ExTech edge devices**», «**R.Stahl certifications**», «**Remote inference architecture**» — brand names allowed, but full English descriptions: «purpose-built industrial PCs, Ex zoned, with limited ML inference capability (предназначены для…)».

**Recommendation.** Russify описания, keep brand names в parens.

### P2-4. Bainbridge 4 ironies (lines 429–438) — strong, but heading-как-якорь не русифицирован

«**Ирония 1: Автоматизация удаляет лёгкие задачи, оставляя сложные.**» — OK RU. «**Ирония 4: "Перепроектировать систему так, чтобы было место для человека" сложнее, чем "автоматизировать всё".**» — OK RU. Но «**Применение к современному AI.**» (line 439) — OK; «**AI co-pilot paradox в современных терминах**» — anglicism «co-pilot» в narrative, мог бы быть «помощник» / «пилотный AI».

### P2-5. Edge inference 4-tier overlaps с §4.2 матрица альтернатив

§3.3 даёт 4-уровневый taxonomy edge inference (Tier 1-4); §4.2 даёт 6 non-AI инструментов; они **не overlap концептуально** (taxonomy архитектурного уровня vs taxonomy non-AI инструментов), но студент может смешивать. **Recommendation**: в §4.2 добавить one-line cross-ref «*4-уровневая taxonomy edge inference (§3.3) — про архитектурный слой; матрица инструментов ниже — про выбор non-AI инструмента*».

### P2-6. Третий worked example (brewery) расположен в *italics* как «*Третий проработанный пример*»

§4.3 имеет 3 worked examples: Pfizer (no italics, bold heading) + авиадвигатель (no italics, bold) + **brewery в italics + asterisk-italics heading**: «*Третий проработанный пример: brewery packaging line CV-QC.*»

Italics в chapter обычно signal сноску / commentary; здесь это **3-й main worked example**. Это inconsistent formatting.

**Recommendation.** Change «*Третий проработанный пример: brewery packaging line CV-QC.*» → «**Третий проработанный пример: пивоварня packaging line CV-QC.**» (no italics, bold). И «packaging line» → «линия упаковки» (Russification).

### P2-7. Optimus dating Q1 2026 — нужен [VFY-day-of]

§1.3 Tesla Optimus entry: «*Май 2026 (текущий момент) — промышленный масштаб `[VFY-day-of]`*» — OK marker present. Но «*на конец Q1 2026*» — также volatile; пометить тоже.

---

## Failure-bucket strict-in independent recount post-expansion

**Self-claim (book-editor v3):** ≥55% chapter words bucket.

**Independent recount по NEW v3 content (sampled 24 блока):**

| Sample block | Bucket classification | Justification |
|---|---|---|
| Tesla Optimus 4th hype case (§1.3) | **strict-in** | Documented PR/telepresence failure + lesson (independent audit / maintenance hours / stoppages) |
| Honeywell aviation MRO anti-case (§1.2) | **strict-in** | Roadmap-not-production + 3 structural reasons (DO-178C / fragmentation / data access) + lesson |
| GM Hamtramck 1985 (§1.1 + §2.4) | **strict-in** | Documented over-automation failure + lesson (companies don't learn) |
| Rethink Robotics Baxter (§2.3) | **strict-in** | Shutdown analysis + 3 causes + lesson (cobot ≠ cheaper industrial robot) |
| UAW Stand Up Strike 2023-2024 (§3.6) | **strict-in** | Documented worker resistance pattern + criterion D + alternative (joint committees) |
| ExxonMobil refinery AI (§3.2) | **strict-in** | Boundary (advisory mode only, no direct loop) + structural reason |
| Brewery worked example (§4.3) | **strict-in** | Positive pass + alternative non-ML baseline checked + criteria justified |
| FDA warning letters (§3.4) | **strict-in** | Real findings + criterion (audit trail mandatory) + alternative (explainable AI) |
| ATEX equipment categories (§3.4) | **strict-in** | Fundamental limit (physical prohibition Zone 0) + alternative (remote inference) |
| Q9 OEE-vendor pattern (Q&A) | **strict-in** | Failure pattern + criterion (require breakdown) |
| Q10 LLM SCADA HMI (Q&A) | **strict-in** | 3 failure modes + criterion (advisory only) |
| Q11 CFO ROI (Q&A) | **partial** | Methodology depth, но не failure/limit framing — financial decision support |
| Q12 FDA pharma 2024-2025 (Q&A) | **strict-in** | Per-tech limits + criterion (advisory mode only) |
| Q13 Sim2Real gap (Q&A) | **strict-in** | Fundamental limit + 3 mitigation alternatives |
| Q14 legacy PLC + edge AI (Q&A) | **strict-in** | Criterion (no replace) + 3 architectural patterns |
| §1.1 McKinsey/MIT/RAND differentiation | **strict-in** | Critical reasoning: each report measures different thing |
| §1.1 Historical waves of automation | **strict-in** | Pilot-purgatory is structural, not ML-specific |
| §1.1 OEE deconstruction | **strict-in** | Methodology fix for -25% downtime claim pattern |
| §2.4 Bainbridge 4 ironies | **strict-in** | Fundamental limit (automation paradox) + AI copilot 2026 application |
| §3.2 Vanilla Deep RL 4 problems | **strict-in** | 4 fundamental problems + solutions |
| §3.4 GAMP5 + ICH Q8-Q11 tension | **strict-in** | Fundamental QbD vs continuous learning + resolution |
| §3.6 RL drift 4 triggers + 3 detection methods | **strict-in** | 4 trigger conditions + 3 detection classes + safe rollback |
| §4.1 Numerical decision thresholds | **strict-in** | Engineering criteria explicit + alternatives per category |
| §3.5 Russian context cross-cutting | **strict-in** | Structural barriers + skepticism for public claims |

**Sample summary:** 23/24 strict-in = **95,8%** на NEW v3 content. 1 partial (Q11 CFO ROI — financial drift). Sample НЕ репрезентирует общую chapter percent; для общей доли требуется full chapter recount. v2 был 66,4% по full chapter; v3 added ~17,5k слов из которых ~95% strict-in → estimated full chapter strict-in **~75-80%**, comfortably > 30% mandate.

**Distribution post-expansion (per section).** §1 expansion heavy (1635 → 4731 — almost 3x), §2 (2077 → 6669 — 3x), §3 (2094 → 7735 — almost 4x), §4 (1572 → 3648 — 2.3x). Strict-in per section **estimated**: §1 ≈ 85%, §2 ≈ 75%, §3 ≈ 80%, §4 ≈ 95% (highest, payoff). **Min content-section ≈ 75% strict-in** — **passes** 20% per-section floor; no single-cluster concentration.

**Counter-check:** Self-claim ≥55% chapter words — likely conservative; actual ~75-80%. **Honest.**

**Verdict:** Failure-bucket ≥30% mandate **comfortably met**; distribution **OK**; no single-artifact concentration.

---

## Russification quality assessment on NEW v3 content (15 sampled paragraphs)

**Methodology:** sampled 15 параграфов из v3 expansion (Tesla Optimus, Honeywell MRO, GM Hamtramck, Rethink Baxter, UAW, ExxonMobil, Brewery, FDA letters, ATEX details, GAMP5, Указ 250, Bainbridge 4 ironies, Edge inference taxonomy, RL drift detection, Q&A 9-14).

| Paragraph | RU quality | Notes |
|---|---|---|
| Tesla Optimus 4th case | Mostly RU | «hype», «PR-демонстрация», «rolling deadline» — minor leak; «гуманоидной робототехнике» canonical |
| Honeywell aviation MRO | RU-mostly | «production», «foundation модели», «certification», «aerospace systems» — leak |
| GM Hamtramck | Strong RU | «factory of the future» (quote, OK), «канонический», «провальный эксперимент» — good |
| Rethink Baxter | **Heavy English** | «performance gap», «integration cost», «competition», «humanoid-like cobot», «simple assembly tasks», «slower и менее точным» — significant leak |
| UAW Stand Up Strike | **Heavy English** | «Historical pattern», «autoworkers union», «joint committees on technology» — many phrases keep English |
| ExxonMobil refinery | **Heavy English** | «Public-уровень disclosure», «competitive advantage», «deployment of AI-based predictive maintenance», «rotating equipment», «process control AI» — heavy |
| Brewery worked example | Mostly RU | «packaging line», «defect-rate», «chipped lip», «abstain queue» — Russification incomplete |
| FDA warning letters | **Heavy English** | «FDA проверка», «data integrity issues», «(paraphrased)», «computerized systems validation», «electronic batch records» |
| ATEX equipment categories | **Heavy English** | «Pepperl+Fuchs ExTech edge devices», «purpose-built industrial PCs», «explosion-protected enclosures», «Remote inference architecture» — but brands legitimately latin |
| Bainbridge 4 ironies | **Strong RU** | All 4 subheaders RU-canonical, examples translated; «AI co-pilot paradox» — minor leak |
| Edge inference taxonomy | **Heavy English subheaders** | «Tier 1-4», «Rule-based on PLC», «Hybrid edge + cloud» — see P1-6 |
| RL drift 4 triggers (§3.6) | RU-mostly | «Batch transitions», «Feedstock change», «Seasonal shifts», «Equipment wear» — subheaders English, body mostly RU |
| RL drift detection methods | **Heavy English** | «Statistical control charts на residuals», «Distribution distance metrics», «Out-of-distribution detection methods», «KL-divergence», «Wasserstein distance», «Mahalanobis distance в feature space» |
| Q&A Q9 | Mixed | «AI vendors», «baseline OEE», «honest OEE до пилота» |
| Q&A Q11 | **Heavy English** | «прирост EBITDA», «OEE prirost», «marginal contribution per unit», «annual production», «annual EBITDA impact», «payback period», «scale-up plan», «comparable case» — see P1-5 |
| Q&A Q13 | **Heavy English** | «Sim2Real gap», «modelling errors», «noise characteristics», «structured в реальности, в симуляторе — typically Gaussian», «domain randomization», «fine-tuning on real data», «conservative safety layers», «runtime monitors» |
| Q&A Q14 | **Heavy English** | «Read-only mode», «Setpoint advisory», «Closed-loop с safety layer», «runtime monitor», «communication interface» — full English block |

**Verdict:** Russification depth on v3 NEW content is **regressed** relative to v2 closed-P1 baseline. Особенно heavy в Q11/Q13/Q14, FDA warning letters, ExxonMobil, Rethink Baxter, UAW, RL drift detection methods, Edge inference taxonomy. **Targeted sweep required** на эти 7 sections.

---

## Worked examples assessment

**Three examples:** Pfizer Vox (pass) + авиадвигатель (fail) + brewery (pass).

**Pedagogical effectiveness checklist:**

| Example | LO8 Apply | LO8 Create | Cross-domain | Distinctive criteria |
|---|---|---|---|---|
| **Pfizer Vox (pass)** | ✓ | ✓ | Процессное / regulated | C-passes with recommendation mode arch |
| **Авиадвигатель (fail)** | ✓ | ✓ | Дискретное / aerospace | A-fails (data) + B-fails (cost) + C-fails (cert) — multi-category blocked |
| **Brewery (pass)** | ✓ | ✓ | Дискретное / food | C-passes with HACCP + asymmetry правильная сторона |

**Strengths:**
- Coverage 2 domains × 2 outcomes (pass/fail) actually 3 unique combinations (regulated process pass / aerospace discrete fail / food discrete pass)
- Filter demonstrated in both directions (LO8 Apply+Create)
- Three different category-failure modes shown (data / cost / regulatory)

**Weaknesses:**
- 2 pass + 1 fail balance — P1-2 flag (slight valence shift toward "AI fits")
- Brewery — formatted italics (P2-6) breaks consistency with first two
- No explicit cross-summary contrasting **rate of passage** — i.e., «*Pfizer passes because architecture, авиадвигатель fails because data+cost+cert, brewery passes because food-safety domain is gentler than aerospace*»

**Numerical sanity check (brewery):** 30 000 bottles/hour × 0.5% defect rate × 24/7 = ~3500 defects/day; 30 days → 105 000 labelled examples. Check: 30 000 × 24 = 720 000/day × 0.5% = 3 600 defects/day. ~3 500 ≈ 3 600 — OK. 105 000 labelled examples × 30 days = OK reasonable for ML training set baseline.

**Recommendation.** Reorder + add transition sentence per P1-2 + reformat brewery as bold (P2-6) + add cross-summary в §4.3 final paragraph.

---

## Pacing reality check для 75-мин лекции

**Total chapter:** 29 822 слов. **Estimated reading time** at 200 WPM (academic technical pace) = ~150 минут = **2.5 hours deep read**. At Russian-native fast read pace 300 WPM = 100 минут. Chapter explicitly framed как **расширенный референс**, не lecture script; в frontmatter «*Глава расширена относительно классического конспекта лекции и рассчитана на три уровня погружения*» (lines 137-138).

**Section budget by 3-level reading framework (per §0.3):**
- **Level 1 (75-min лектор):** §0 (concise) + §1 (concise) + §2 (concise) + §3 (concise) + §4 как payoff + §5. Estimated speaking time ~40 минут aloud; +1-2 minutes hook (Tesla); +10 минут Q&A → total ~50-60 минут. Adequate for 75.
- **Level 2 (студент к семинару):** §0 – §4 целиком + self-check. ~2.5 hours.
- **Level 3 (проектное чтение):** full reference, multiple sessions.

**Owner-decision baseline (PR #129):** chapter ≥ 30k baseline для L4+. v3 hits 29 822 = within ±5% target. ✓

**75-min lecture content selection** (for slides + speech derivation):
- **MUST cover:** §0 keystone (3 min) + §1.1 statistical adoption gap (4 min) + §1.2 augmentation vs controller (5 min) + §2.4 Tesla 2018 + Bainbridge (8 min) + §2.5 Boeing 737 (4 min) + §3.4 регуляторика (8 min) + §4 5-шаговая рамка (10 min) + §4.3 Pfizer worked (5 min) + §5.2 4 questions (3 min) + Q&A (10 min) = ~60 min + 15 min hook/transitions = 75 min. ✓
- **CHAPTER backup (не lecture):** §1.3 trio + Tesla Optimus details, §2.1 5 concepts + ECE / Dawid-Skene formal, §2.5 NTSB findings, §3.1 PLS/GP/NN classes, §3.2 vanilla Deep RL 4 problems, §3.3 4-tier edge taxonomy, §3.4 ATEX zones + GAMP5 deep, §4.1 numerical thresholds, §4.2 6 tools detail, §5.3 моsst Лекция 12 deeply, Q&A 14 questions. All adequate.

**Conclusion:** Chapter overload **намеренный** per owner PR #129. 30-40% extraction для slides feasible. Selected core ~30% = 9k слов adequate для 75-min lecture script. **Not a methodological problem**; structural design choice.

---

## Recommendations for Phase 4d revision (v3 → v4)

### Carry-forward (keep — strong)

1. **Keystone consistency** — Variant C anchored across §0/§2/§3/§4.3/§5.1 + worked examples reference. ✓ Lock.
2. **OEE как сквозная метрика + deconstruction in §1.1** — 6 anchor points + numerical example + vendor-pattern recognition. Best fundamental coverage. ✓ Lock.
3. **5 mandated fundamentals + 4 new** (OEE / эталонная разметка / OT/IT / edge determinism / label cost; Sim2Real / Constrained RL / V-model / DO-178C). All deeply covered. ✓ Lock.
4. **3 worked examples** — central LO8 payoff, рамка-как-фильтр demonstrated в обе стороны. ✓ Keep (with P1-2 reorder + P2-6 reformat).
5. **OT/IT divide** — теперь deep across §1.1 + §3.3 + §3.4 + §4.2 (per Plan v2 P1-2 mandate v2 fix carried). ✓ Lock.
6. **Q&A 14 questions** — engineering depth (kept Q9-Q14 substantive). ✓ Keep with P1-5 Q11 reframe.
7. **Bainbridge 4 ironies** + Toyota TPS historical depth — strong educational anchor. ✓ Lock.
8. **GAMP5 + V-model + ICH Q8-Q11 deep** — теперь properly covered (Plan v2 mandate v2 closed). ✓ Lock.
9. **Anti-pattern compliance** (no «магическая пилюля», no named institutions, no insider phrasing). ✓ Lock.
10. **Anonymization absolute** — confirmed for v3 expansion. ✓ Lock.

### Fix before GATE A (P0 + P1 — required)

1. **P0-1. §3.5 duplicate paragraphs** — удалить lines 823-825 (duplicate СИБУР + ММК/НЛМК/Северсталь).
2. **P0-2. §4.4 ↔ §4.5 ordering** — переставить body: §4.3 → §4.4 (5-шаговая рамка) → §4.5 (матрица провала) → §4.6 (self-check). Соответствует TOC.
3. **P1-1. Russification depth** — targeted sweep на 7 v3 sections (Rethink Baxter, UAW, ExxonMobil, FDA letters, Edge taxonomy, RL drift methods, Q11/Q13/Q14). Mapping table — см. above.
4. **P1-2. Worked example balance** — добавить transition sentence + reorder per P2-6 reformat to bold.
5. **P1-3. Typo «глаz»** (line 139) — replace с «главу».
6. **P1-4. Recursive parenthetical «застревание на пилотной стадии (застревание на пилотной стадии)»** (line 112) — fix.
7. **P1-5. Q11 CFO ROI** — reframe на engineering-judgment, не financial.
8. **P1-6. Tier 1-4 edge taxonomy** — RU-canonical subheaders.
9. **P1-7. FDA warning letters** — verify or de-name.

### Polish (P2 — optional, carry-forward acceptable)

- **P2-1.** §1.3 heading — «Трио» → «Четыре кейса» (Tesla Optimus added).
- **P2-2.** GM Hamtramck §1.1 → §2.4 cross-ref (deduplicate).
- **P2-3.** ATEX equipment categories — Russify descriptions.
- **P2-4.** «AI co-pilot paradox» → «парадокс AI-помощника».
- **P2-5.** §3.3 edge taxonomy + §4.2 alternatives — cross-ref clarification.
- **P2-6.** Brewery worked example formatting — bold consistent с Pfizer/авиадвигатель.
- **P2-7.** Tesla Optimus Q1 2026 date — [VFY-day-of].

### Cascade-of-changes warning

Russification fixes (P1-1, P1-6) must cascade to:
- **slides/*.md** (Phase 5 generation): subheaders → slide titles. RU-canonical mandatory.
- **speech.md** (Phase 9): narrative derivation. RU-canonical mandatory.
- **Q&A backup** Q11/Q13/Q14: speech-writer will need clean version.
- **Глоссарий** §0.2: Tier 1-4 если add — RU canonical.

Phase 4d orchestrator должен ensure book-editor v4 brief предусматривает specific 7-sections deep sweep, не one-pass.

---

## Top-3 issues (приоритизировано)

1. **P0-1 §3.5 duplicate paragraphs** — single biggest blocker for GATE A presentation; видно при first reading; читательский trust kill.
2. **P0-2 §4.4 ↔ §4.5 ordering** — payoff section of LO8 misordered relative to TOC; subtle but methodically wrong (summary tool before main framework).
3. **P1-1 Russification regression на 7 v3 sections** — carry-forward к slides (Phase 5) + speech (Phase 9); cost-of-omission Lec-08 ≈ 83 минут revision.

**P1-2 – P1-7** — менее структурные, can be batched с P0 fix.

**P2** — все carry-forward acceptable.

---

## Final verdict

**REVISE.** 2 P0 (structural expansion artifacts) + 7 P1 (Russification regression + worked example balance + typo + recursive parens + Q11 drift + Tier taxonomy + FDA letters) + 7 P2 (polish). Counter-check: 7 P1 ≥ 5 → REVISE forced per ENFORCED rule.

**Cannot present at GATE A as-is.** Required fixes:
- P0-1 §3.5 duplicate removal — **5 минут fix**.
- P0-2 §4.4 ↔ §4.5 reorder — **10 минут fix**.
- P1-1 Russification sweep — **estimated 30 минут focused sweep** with mapping table.
- P1-2 worked example balance — **15 минут**.
- P1-3 — P1-7 — **20 минут combined**.

**Total revision estimate:** ~1.5 hours single book-editor spawn.

**После Phase 4d:** Phase 4.5 pre-USER-GATE walkthrough → USER GATE A.

---

**Конец Methodology Critic Report. Verdict REVISE. P0 = 2, P1 = 7, P2 = 7. Failure-bucket strict-in на NEW content = 95,8% (24-sample), holistic distribution OK. Russification regression structural — closed-P1 from v2 reopened.**

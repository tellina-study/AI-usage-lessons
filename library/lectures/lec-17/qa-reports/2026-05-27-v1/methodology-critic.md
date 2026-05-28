VERDICT: APPROVE-WITH-POLISH

# Methodology Critic Report — Lec-17 Chapter v1 (4-part)
**Date:** 2026-05-27 | **Reviewer:** methodology-critic | **Branch:** issue-145-lec-17 | **Verdict:** APPROVE-WITH-POLISH

## Summary

Lec-17 capstone chapter (30 001 слов, 4 части, 2 168 строк total) — методически плотный, структурно правильно построенный артефакт. Keystone-axis (2D-плоскость «Применимость ИИ × Лестница автономии L0→L5») предъявлен корректно в Разделе 0 ДО первого погружения. Все 8 LO имеют покрывающий материал. Cornerstone glossary — 48 терминов (vs target 16-20) — избыточно широкий, но без вреда. AI-Failure & Judgment strict-in share holistically ≈ 32% (target 30%), распределён по 4 частям не идеально (Part 4 ~25-30%, на нижней границе). Cross-lecture coverage 16/16 формально ✓, но качество callbacks неоднородное: L1/L4/L5/L9/L13 — глубоко, L6/L16 — слабее (хотя в манифесте), L8/L12/L16 — orchestrator C5 anchors частично не материализованы. Document size compliance — на границе (part2/part3 = ровно 600 строк, лимит). Word count — ровно 30 001 (на границе с zero buffer).

Артефакт show-able для USER GATE A, но требует **4 P1 polish-фиксов** перед Phase 4 → revision. Отсутствие P0 issue.

## Compliance checks

| Check | Result | Notes |
|---|---|---|
| Word count ≥30 000 | **PASS (на границе)** | 30 001 total (7 663 + 8 751 + 5 833 + 7 754) — буфер 0. Per CLAUDE.md target window 28 500-31 500. |
| Multi-part split ≤600 lines/file | **PASS (на границе)** | part1=369, part2=600, part3=600, part4=599. Part2 и Part3 ровно на лимите — любая добавка потребует пересплита. |
| Strict-in % holistic ≥30% | **PASS** | ≈32% overall. Part1 ≈33%, Part2 ≈65% (Разделы 1+2.8), Part3 ≈75% (Раздел 4 целиком), Part4 ≈25-30% (borderline; cheat-sheet #3 + advisory career). |
| Keystone-axis в Разделе 0 ДО погружения | **PASS** | §0.3 (chapter.md строки 178-217) предъявляет 2D-плоскость до Раздела 1. Четыре квадранта явно описаны с примерами. Обоснование «почему 2 оси, а не 1 или 3» присутствует. |
| Mapping локальных шкал → единая L0-L5 | **PASS** | §2.7 (chapter-part2.md) — таблица из 6 колонок (L0-L5 × 5 local scales: L4 A/B/C/D, L9 L1-L5, L12 A0-A3, L14 Видит-Решает-Действует, L13 5-level). Также явно объясняется, почему mapping не precise. |
| LO1 — diagnostic question | **PASS** | §0.1, §0.4 — vопрос «Где AI работает, где — нет, и как это понять?» формулируется на старте и re-asked после roadmap. |
| LO2 — 7 критериев применение | **PASS** | §1.0-§1.5 — критерии + worked example (AquaOptima); §1.5 содержит дополнительный worked example «банк ипотека». |
| LO3 — placement на 2D | **PASS** | Раздел 3 — карта 16 отраслей с координатами; §3.7 — анализ пустых квадрантов как диагностика. |
| LO4 — 8+ канонических провалов с уроком + альтернативой | **PASS (с превышением)** | §4.1-§4.12 — 12 провалов, каждый со структурой «контекст + урок + альтернатива». |
| LO5 — лестница автономии + criteria подъёма | **PASS** | §2.1-§2.6 — каждая ступень с criteria подъёма + примеры + антипаттерны. |
| LO6 — 4 cheat-sheets | **PASS** | §5.1-§5.4 — 4 карточки структурированы (включая текст таблиц с примерами). |
| LO7 — career trajectory | **PASS** | §5.5 — 7 career paths (Solution Architect / Compliance / Product Engineer / Consultant / Domain Expert / Academic / VC). |
| LO8 — 16 отраслей как карта | **PASS** | §3.1-§3.3 — карта строится layer-by-layer; §3.4-§3.7 — кластерный анализ. |
| Cross-lecture coverage 16/16 | **PARTIAL (см. P1 #1)** | L1=93, L2=52, L3=65, L4=97, L5=97, L6=9, L7=30, L8=17, L9=41, L10=33, L11=32, L12=24, L13=49, L14=30, L15=23, L16=14. L6 и L16 формально присутствуют, но C5-specific anchors (L16 «pet-rock LLM-чатбот не заменит геолога / Subsurface knowledge vault») не материализованы как явный текст-anchor — только generic L16 references. L8/L12/L13 anchors из C5 присутствуют. |
| Cornerstone glossary 16-20 терминов | **PASS (с превышением)** | Appendix A содержит 48 терминов с lecture-back-references. Все обязательные cornerstones (AI Effect, Pearl 3 levels, OODA, HITL/HOOL/HOTL, ODD, pilot purgatory, closed-loop vs open, reliability compounding, slopsquatting, soft sensor, digital twin, foundation model, MITRE ATLAS, distribution shift, ground-truth feedback loop) присутствуют. |
| Pilot purgatory unification (C3) | **PASS** | §4.12 explicitly показывает три источника (РФ 9/10, MIT Sloan 5.5%, 75% twins) с контекстом методологии. |
| Anonymization (no ИУ-6 / МГТУ / etc.) | **PASS** | 0 hits на ИУ-6 / МГТУ / Бауман / МАИ / ВКА. §0.5 + §5.5 используют «профильные технические университеты» — родовое. |
| No timing/methodology markers в body | **PASS (с 1 P2 nitpick)** | 0 timing markers. 1 случай «одно методическое замечание» в §Введение (chapter.md строка 102) — допустимо в chapter narrative (правило относится к slides body + speaker notes). |
| Baseline mandate на measurable claims | **PARTIAL (см. P1 #2)** | See & Spray «50%+ от ~1 фунт/acre к ~0.5 фунта» — отлично. Plenty «$940M потерь при $940M привлечённого» — отлично. CrowdStrike «8.5M устройств» — есть. **Missing denominators:** «5M acres» без US ag total baseline (~900M = 0.55%); «Monarch 38% layoffs» без headcount denominator; «Zillow 25% layoffs» без headcount denominator; «20+ million users Copilot» без total dev population baseline; «46% кода AI» без denominator universe; «$5+ млрд ущерб CrowdStrike» без industry-loss baseline. |
| Document size ≤600 lines/file | **PASS (на границе)** | part2/part3 ровно 600 — zero buffer для будущих правок. |
| Concept fundamentals в narrative + glossary | **PASS** | AI Effect / Pearl 3 / OODA / HITL/HOOL/HOTL / ODD / pilot purgatory / closed-loop / reliability compounding / slopsquatting / soft sensor / digital twin / foundation model / MITRE ATLAS / distribution shift — все cornerstone-концепты раскрыты в narrative (§0, §1, §2, §4) ИЛИ закреплены в glossary (Appendix A). HITL design boring failure явно разобран в §2.3 + §4.4. |

## P0 issues

**Нет P0 issues.** Структура методически правильная; LO покрыты; keystone предъявлен корректно; chapter depth достигает baseline ≥30k.

## P1 issues

### P1 #1 — L16 specific anchor «pet-rock LLM-чатбот / Subsurface knowledge vault» не материализован

**Section:** chapter-part3.md §3.3 «Final batch» + Appendix A glossary.
**Evidence:** В §3.3 (строки 224-231) L16 разобрана как «quadrant-dependent по матрице 2×2 «data × process»» с подразделом на 4 квадранта (Q1-Q4). Это валидный general callback. Но **plan C5** требовал конкретный narrative anchor: «Subsurface knowledge vault — physics-informed AI границы; pet-rock LLM-чатбот не заменит геолога». Этот specific anchor (с «pet-rock» framing) не появляется ни в одной части chapter. Grep `pet.rock|subsurface|geolog` показывает 0 hits в narrative; только generic «нефтегаз» / ATEX / MethaneSAT.
**Why P1:** plan C5 explicitly approved orchestrator-correction; ненаправленное наследование = silent drift от approved plan. С точки зрения дидактики L16-pattern (regulated industry + physics-informed AI границы + «LLM не заменит specialised expert») — это **уникальный** урок L16, не покрываемый general «matrix 2x2». Без anchor студент не получит конкретный takeaway L16 на capstone-уровне.
**Recommendation:** в §3.3 после description Q1-Q4 L16 добавить параграф ~150 слов:
> «**L16 anchor — Subsurface knowledge vault.** В нефтегазе главный паттерн — physics-informed AI vs pure LLM. Один наглядный кейс: «pet-rock LLM-чатбот» — попытка построить chatbot для разведки субсёрфэйса на основе LLM без physical constraints — провалена, потому что LLM не имеет доступа к keystone уравнениям пористости/проницаемости/seismic interpretation. Геолога эта система не заменит. **Урок переноса:** в любой регулируемой инженерной индустрии (нефтегаз, авиакосмос, ядерная энергетика, фарма) generic LLM не заменяет physical/domain modeler — нужны PINNs (physics-informed neural networks) или hybrid физика+ML.»

### P1 #2 — Baseline / counterfactual missing на 5-6 measurable claims

**Section:** chapter.md §Введение строка 120, chapter-part2.md §1.1 строка 79, §1.2 строка 140, chapter-part3.md §3.2 строка 155, и др.
**Evidence:** Несмотря на отличный baseline coverage для See & Spray (kg/acre baseline) и Plenty ($940M loss = $940M raised context), несколько measurable claims без денoминатора:

| Claim | Where | Missing baseline |
|---|---|---|
| «5+ миллионов акров See & Spray» | §1.1, §3.2, §2.5 | US ag cropland baseline (~900M acres total) → 5M = 0.55% |
| «Monarch Tractor 38% layoffs 2025» | §Введение, §1.1, §3.2, §4.1 | 38% from какой peak headcount? |
| «Zillow 25% layoffs» | §Введение | 25% from peak headcount? (~8 000 employees pre-COVID per Zillow Q3 2021) |
| «20+ миллионов пользователей Copilot» | §1.2 | Из total developer population (~28M GitHub registered, ~100M global est.) → ≈70-20%? |
| «46% кода AI-generated» | §1.2 | На repositories с **активным** использованием Copilot vs all repos? Какова доля Copilot users? |
| «$5+ млрд ущерб CrowdStrike» | §1.2 | Vs annual cyber/IT losses industry baseline? Vs Delta annual revenue? |
| «$25M Hong Kong deepfake» | §4.8 | Vs total fraud losses Hong Kong annual? |
| «8.5M устройств CrowdStrike» | §1.2 | Вот это, кстати, **хорошо** — это absolute, в context broad blast radius table — это уже сравнение. |
| «$940M потерь Plenty» | §0.1, §3.2, §4.1 | **PASS** — есть «при $940M привлечённого капитала». |

**Why P1:** CLAUDE.md § «Baseline / Counterfactual Mandate» — measurable claim без denominator/baseline = P1 «missing denominator». Особенно critical для capstone, потому что студенты унесут эти цифры. «5M acres = 0.55% US ag» дает **другую перспективу**, чем просто «5M acres звучит впечатляюще».

**Recommendation:**
- §1.1 См. & Spray: добавить «(0.55% от ~900M US ag cropland, по USDA NASS 2023)».
- §Введение строка 120, §3.2, §4.1 Monarch: добавить «38% from ~150 человек peak Q2 2024 (per press reports)» или [VFY-baseline].
- §Введение Zillow «25% layoffs»: добавить «(~2000 из ~8 000 employees Q3 2021)».
- §1.2 Copilot «20+M users»: «(из ~28M GitHub registered devs)» + «46% кода **на repos с активным Copilot usage**, vs ~0% baseline на repos без Copilot».
- §1.2 CrowdStrike «$5+ млрд»: «(comparable to 2017 NotPetya estimate ~$10B)».

### P1 #3 — Part 4 strict-in share на нижней границе (25-30%); распределение не идеально холистическое

**Section:** chapter-part4.md §5.0-§5.5.
**Evidence:** Part 4 содержит cheat-sheets reveal (§5.1 — карточка 7-критериев, §5.2 — лестница, §5.3 — 12 провалов как карточка, §5.4 — карта). §5.3 (карточка #3 — 12 провалов) — 100% strict-in. Но §5.5 career trajectory (~1 500 слов) — advisory tone, не strict-in. §5.7 closing — не strict-in. Appendix A glossary — partial strict-in (включает antipattern terms — slopsquatting, Galactica, paper mill, prompt injection — но также non-strict items — RAG, foundation model, golden set, etc.).
**Approx breakdown:**
- §5.0-§5.4 cheat-sheets reveal: ~2 500 слов, ~50% strict-in = ~1 250 strict-in
- §5.5 career trajectory: ~2 000 слов, ~10% strict-in = ~200 strict-in
- §5.7 closing: ~500 слов, ~0% strict-in
- Appendix A: ~1 800 слов, ~40% strict-in = ~720 strict-in
- Appendix B Q&A: ~900 слов, ~30% strict-in (Q1+Q2+Q5+Q10 strict-in) = ~270 strict-in
- **Total Part 4 strict-in:** ~2 440 / 7 754 = ~31%

**Why P1:** Холистический check (per CLAUDE.md) — share **в каждом** артефакте отдельно ≥30%. Part 4 на самой границе. Если speech.md или slides понизят share Part 4-equivalent контента до 25%, потенциально fail.
**Recommendation:** добавить в §5.5 career trajectory **дополнительный block ~300-400 слов** про «common career failure modes» — типичные провалы выпускников ИИ-курсов (например: «AI-engineer без skepticism — early career trap; jumped to AI engineering без understanding границ → переоценил project applicability → ушёл в pilot purgatory; lesson learned»). Это закрепит дискриминационный навык и поднимет strict-in share Part 4 выше 32-33%.

### P1 #4 — Word count + line-count buffer = 0 (на лимитах)

**Section:** Vse 4 части.
**Evidence:** Total 30 001 слов (target 30 000, threshold 28 500). Файлы: part2 = 600 строк (CLAUDE.md лимит), part3 = 600 строк (на лимите). Любое исправление, добавляющее narrative (включая фиксы P1 #1, P1 #2, P1 #3) **обязательно** толкнёт part2 или part3 > 600 строк, и потребует пересплит.
**Why P1:** Структурный риск; не блокирующий, но требует attention при Phase 4 revision. Если orchestrator решит сделать revisions inline, нужно сразу планировать **сплит part2 → part2a + part2b** или **part3 → part3a + part3b** при добавлении контента.
**Recommendation:** При Phase 4 revision: book-editor должен заранее решить — (a) изъять/сократить менее важные параграфы в part2/part3 (например, §2.6 L5 discussion sometimes избыточен — 7-8 параграфов про теоретический L5), либо (b) сразу пересплитить на 5 частей. Best practice: добавить frontmatter `parts: 5` если split необходим.

## P2 issues

### P2 #1 — «одно методическое замечание» в §Введение

**Section:** chapter.md строка 102.
**Issue:** Фраза «одно методическое замечание про статус знания» — мета-комментарий вида, который запрещён в slides body. Для chapter narrative — допустимо (правило `[no-timing-no-methodology-in-slides]` явно относится к slides body + speaker notes, не к chapter).
**Severity:** P2 — informational, не блокирующее.
**Recommendation:** оставить как есть. При derivation slides — обязательно строго: не копировать эту фразу в speaker notes.

### P2 #2 — Glossary inflation (48 терминов vs target 16-20)

**Section:** chapter-part4.md Appendix A.
**Issue:** Glossary содержит 48 терминов, многие из которых (Sycophancy, Vectara HHEM, Reward hacking, Prompt injection, Adversarial examples, Data poisoning, Paper mill, Inverse design, Bayesian optimization, SAR, FMEA/FTA, ISA-95, PAT, ATEX/IEC 61508, ORCA benchmark, POD, BO+GP, Self-driving lab, Methane MRV, C2PA, SBOM, HD-map vs vision-only) не появляются в narrative body, либо появляются только мимоходом. Glossary becoming reference-page вместо «cornerstone терминов курса» как plan C2 требовал.
**Severity:** P2 — не блокирующее, но размывает фокус.
**Recommendation:** оставить как есть для Phase 4 (студент получает bonus reference); опционально в Phase 11 reflection — пометить ~20 cornerstones как «Tier 1 must-know», остальные как «Tier 2 reference» для navigation.

### P2 #3 — Heavy English-only insertions в narrative

**Section:** Все 4 части — множественные «AI fit», «chiseled task», «closed-world», «broad task», «long-tail», «proof-of-value», «vendor-lock-in», «overpromise», «engineering-agent», «sycophancy», «paper mill», «slopsquatting», «autonomous lab», «golden set».
**Issue:** Concept-density высокая; chapter — universal audience (профильные технические университеты), не специализированная аудитория. Студент 3-курса может потеряться. Не нарушает rule (chapter — не student-facing slides body), но reading-as-textbook-chapter качество умеренное.
**Severity:** P2.
**Recommendation:** в Phase 9-11 при derivation speech.md — обязательно русифицировать ключевые insertion'ы. В chapter — оставить как есть, потому что international terminology — стандарт для technical reference.

### P2 #4 — L13 5-level structuredness anchor — material light

**Section:** chapter-part3.md §3.3 (L13 — 3 точки на карте) + chapter-part2.md §2.7 mapping table («Контролируемая среда L1 ... Чёрный лебедь = вне L5»).
**Issue:** L13 5-level environment structuredness mapping присутствует, но **brief**. Plan C5 anchor «warehouse L4 vs urban L3 — ODD дисциплина» материализован через 3 точки в §3.3 и аннотацию в §3.7 (warning quadrant включает Cruise), но связь со специфической **L13 keystone — 5-level structuredness как scale** — могла бы быть более явная (одно phrase-аннотация в §3.3 «warehouse — L1 controlled, robotaxi — L3 urban, black swan — L5» хороший anchor, но коротко).
**Severity:** P2 — anchor присутствует, но не максимально prominent.
**Recommendation:** при Phase 9-11 — добавить в §3.3 cross-link одно phrase: «(см. лестницу среды L13 — это та же ось, что L0-L5 автономии: closed environment → автономия легче; open environment → автономия структурно блокирована)».

### P2 #5 — Cross-references в формате «(см. §X.Y в части N)» — partial

**Section:** Все 4 части.
**Issue:** Plan-mandated cross-reference format «(см. §X.Y в части N)» используется консистентно в Раздел 0 → Раздел 1-5; но обратные ссылки из Раздел 4 → Раздел 1 (например, «failure #1 ↔ критерий 1 + 2») явно не помечены. Студент при reading non-sequentially может пропустить связь.
**Severity:** P2 — minor.
**Recommendation:** в Phase 4 revision — добавить ~5-7 cross-refs из §4.1-§4.12 обратно в §1.1-§1.5 (формат «↑ нарушение критерия 1+2»).

## Recommendations для Phase 4 revision (priority order)

1. **P1 #1** — добавить explicit L16 «pet-rock LLM-чатбот / Subsurface knowledge vault» anchor (~150 слов в §3.3, chapter-part3.md). **Цена:** ~3 строки real growth → потенциальный split part3.

2. **P1 #2** — sweep всех measurable claims (Monarch 38%, Zillow 25%, Copilot 20M/46%, CrowdStrike $5B+, Hong Kong $25M, See & Spray 5M acres) и добавить inline baselines/denominators (~50 слов on average per claim). Это **наиболее частая исправляемая проблема** на capstone Phase 4.

3. **P1 #3** — добавить ~300-400 слов «common career failure modes выпускников AI-курсов» в §5.5 chapter-part4.md, чтобы повысить Part 4 strict-in share с ~31% до ~35-37%.

4. **P1 #4** — pre-planning: либо сократить «избыточные» параграфы в part2 §2.6 (теоретический L5 discussion — 7 параграфов), либо planировать split part2 → 2a+2b ИЛИ part3 → 3a+3b. Без этого P1 #1 + P1 #2 + P1 #3 механически нарушат 600-line limit.

5. **P2 #5** (опционально) — backward cross-references Раздел 4 → Раздел 1 (~5 минут работы).

**Total revision burden:** ~1 200-1 800 слов добавлений + 600-line split decision = **1-1.5 hours book-editor work** для Phase 4.

## Strengths to preserve в Phase 4 revision

1. **Keystone-axis presentation** — §0.3 текст «почему 2 оси, а не 1 или 3» — образцовый pedagogical move, надо beрelegere.
2. **Worked examples** — §1.5 (AquaOptima) + §2.9 (AI-помощник для экзаменов) — **сильно** работают на LO2. Чё-то очень похожее на canonical pedagogy.
3. **§2.7 mapping table** — главный «scientific артефакт» capstone, как и заявлено; **сохранить как есть**.
4. **§4.13 synthesis (3 mega-pattern)** — идеальная финальная свёртка 12 провалов в ментальный chunk.
5. **§5.5 career trajectory** — 7 paths + soft skills — практически и реалистично.
6. **Pilot purgatory unification** (§4.12) — три источника + разные методологии + контекст — модельная P1-fixов presentation.
7. **Closing «знать ИИ — значит знать его границы»** (§5.7) — мощный capstone закрывающий тезис.

## Verdict rationale

- 0 P0 issues (нет блокирующих структурных gaps)
- 4 P1 issues (≤4 → APPROVE-WITH-POLISH per 4-level scale)
- 5 P2 issues (informational; не влияют на verdict)
- Counter-check: 4 P1 < 5 → APPROVE-WITH-POLISH стоит, REVISE не требуется.

**Recommendation для USER GATE A:** orchestrator может представить GATE A с этими 4 P1 ↔ Phase 4 polish revision. Не показывать на GATE без revision (P1 #1 missing L16 anchor — visible structural gap; P1 #2 missing baselines — owner-mandated rule).

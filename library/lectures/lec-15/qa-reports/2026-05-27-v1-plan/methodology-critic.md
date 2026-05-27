# Methodology Critic Report — Лекция 15 plan v1 — 2026-05-27

**VERDICT: REVISE**

## Severity counts

- **P0:** 2 (методически непригоден к запуску в Phase 2 без правок)
- **P1:** 7 (заметно вредит обучению, должно быть исправлено до Phase 2 brief зашит в book-editor)
- **P2:** 6 (полировка)

**Counter-check:** ≥5 P1 issues найдено → verdict ≥ REVISE (per CLAUDE.md 4-level scale). Подтверждаю REVISE, не APPROVE-WITH-POLISH.

---

## Executive summary

План **сильный по охвату материала** (Nobel-tier AlphaFold + Sakana + NeurIPS — это всё canonical 2024-2026 случаи), **методически грамотный по AI-Failure & Judgment Share** (47% strict-in, явное распределение), **good на L4+ tools-per-taxonomy** (6 уровней с anti-hype оговорками). Hero «две стороны медали» — креативно, но рискованно (см. P1-3).

**Но есть 2 структурных P0 блокера** к Phase 2:
1. **Worked-examples crisis:** план claim'ит «4+ worked examples», но реально только **1 настоящий applicable worked example** (s34 catalyst pipeline) — остальные 5 это case studies / failure narratives. Для LO8 «применять и создавать» этого критически недостаточно (lec-13/14 baseline = 3-4 applicable).
2. **Keystone Variant A risk underaddressed:** план сам flagged R2 (Лестница похожа на lec-13/14), но **mitigation поверхностный** — «другой объект» утверждается, но не **operationally демонстрируется**. Сравнительная таблица «лестница цикла vs автономии vs среды» должна быть в plan ДО Phase 2 commit.

И **7 P1 issues**, главные из которых:
- §2 strict-in 23% (ниже 30%) — план пишет «компенсируется в §4-§5», но CLAUDE.md AI-Failure rule говорит «holistic ≥30% видно в **каждом** артефакте отдельно». Per-section компенсация — не санкционировано правилом; нужна явная owner-decision.
- Hero side-by-side pattern — pedagogical concern (split attention dilutes hook impact) — план сам признаёт risk, но defer-to-Phase-5 = поздно.
- Frontmatter не имеет явного chapter-depth target (план уверждает 30k в Phase 2 brief, но frontmatter `length_words` отсутствует).
- §4 + §5 = 24 минуты failure-heavy подряд (peak 87%); cognitive overload risk не addressed.
- §3 worked example s25 («классифицировать 10k спектральных сигналов») — pedagogically слабый, нет baseline / нет verification step.
- Frontmatter audience «студенты-инженеры 3 курса» — но Module 3 — это **обычно 4 курс** в РПД-каноне (lec-13/14 module 3 — проверить).
- Phase 2 brief carry-forward = single paragraph 350 слов — недостаточно guidance для 30k chapter (lec-14 brief был ~600+ слов).

---

## P0 findings (blocking — must fix before Phase 2)

### P0-1 — Worked-examples crisis: 1 applicable вместо обещанных «4+»

**Severity:** P0 (LO8 «применять и создавать» не покрывается без applicable practice)

**Issue:** План § «Worked examples» содержит 6 entries (AlphaFold success, AlphaProof success, GNoME mixed, Galactica failure, Frontiers failure, NeurIPS failure, Sakana failure), но **5 из 7 — это case studies / narratives**, не applicable worked examples в смысле «walk student through decision-making». Только **s34 catalyst pipeline** — настоящий applicable worked example (classify → map alternatives → apply 4 categories → HITL design → pre-publication verify).

Сравните lec-13 (3 applicable worked: VRP-routing задача → 7-criteria fit → tool selection → Yandex/Сбер пример; perishable food cold chain decision; 5-уровневая environment classification applied к last-mile robot delivery). Lec-14 (3 applicable: AIOps tier-3 alert triage walkthrough; SOC SIEM signal selection; Cloudflare config-cascade postmortem walkthrough).

**Lec-15 currently:** s25 «классифицировать 10 000 спектральных сигналов» (1 sentence, no baseline, no decision tree) + s34 catalyst pipeline (5 steps, applicable). Это **2** applicable worked examples — но s25 deeply underspecified.

**Evidence:** Plan строки 205-206 (s25): «**Worked example уровень 4**: "Вам нужно классифицировать 10 000 спектральных сигналов — взять supervised CNN, BO над hyperparameters, или classical signal-detection?" 3 уточняющих вопроса.» — Это **prompt**, не worked example. Нет walked-through reasoning, нет baseline, нет verification.

**Recommendation:**
1. **Reframe self-check claim:** план self-check строка 752 «≥4 worked examples с baseline/counterfactual — 6 worked examples» — это **неточно**, потому что 6 — это case studies. Переписать на «3 applicable worked examples + 4 case-study deep-dives».
2. **Добавить ≥2 applicable worked examples** в outline:
   - Раздел 1 (Hypothesis+Design): «Ваш PI просит идею для гранта в materials science. AI-Scientist v2 даст 50 candidates за вечер, ваш PhD-руководитель даст 3 за месяц. Через 6 шагов решите, какой путь использовать» — walked через decision tree.
   - Раздел 4 (Write+Review): «Коллаборатор присылает paper draft с LLM-generated bibliography. Какой 4-step verification workflow вы применяете?» — walked через actual verification mechanics.
3. **Развернуть s25** до полноценного worked example (≥150 words в plan): «исходные данные 10k spectra, baseline accuracy classical signal-detection (≈75% AUC, paper Smith 2018), decision: BO hyperparameter search показывает classical + tunable threshold лучше CNN на этом dataset, потому что training data label noise high; verify через test set 1k held-out spectra».
4. **s34 catalyst pipeline** — план R12 признаёт что нужно filled с specific catalyst в Phase 2. **Это нужно сделать СЕЙЧАС в плане**, иначе book-editor получит abstract guidance.

**Why P0:** LO8 — это «применять и создавать»; без 3+ applicable walked examples книга превращается в обзор-каталог, как lec-04 v1 (caught by methodology-critic тогда же). DoD на LO8 не выполняется.

---

### P0-2 — Keystone Variant A: risk R2 mitigation поверхностный

**Severity:** P0 (структурный — keystone-axis обеспечивает основу всей лекции; если ось слабо различима от lec-13/14, конструкция рушится)

**Issue:** План честно flagged R2 («Variant A слишком похожа на lec-13 Лестница среды и lec-14 Лестница автономии»), но mitigation = одно предложение: «фаза работы», не уровень среды и не уровень control. Это **claim**, не **operational distinction**.

CLAUDE.md «Keystone-axis (ENFORCED)» строки в methodology-critic checklist:

> «Несущая концептуальная ось предъявлена отдельным keystone-слайдом в Разделе 0 ДО первого погружения. Заголовок + 1-я строка — про саму ось, НЕ про устройство курса / защиту подхода. Если ось «всплывает» в середине, или Раздел 0 защищается/делает только recap вместо подачи оси как нового → REVISE.»

Для Variant A keystone-слайд s03 запланирован, но **сравнительная distinguishability vs lec-13/14 в плане не demonstrated**. Cost-of-omission lec-04 = ~5 циклов deck.

**Конкретный риск:** на лекции студент видит «лестницу из 6 ступеней» в lec-15 и думает «это та же лестница что в lec-14, только переименовали ступени». Если эти 2 лекции в близкие даты — confusion гарантирован. Owner подняли это сами в lec-12 production (issue #133): keystone differentiation должен быть **operationally** очевиден, не интерпретативно.

**Evidence:** Plan строка 717 (R2 mitigation): «Plan явно различает: "фаза работы", не "уровень среды" и не "уровень control". Mermaid-визуализация — vertical (vs lec-14 horizontal); 6 ступеней (vs lec-13 5 уровней, lec-14 3 уровня).»

**Это про визуальные форму-различия, не про concept-различия.** Vertical/horizontal — графический выбор; «6 vs 5 vs 3 ступеней» — счётное различие, но не sense-making различие.

**Recommendation:**
1. **Добавить в план таблицу «3 лестницы side-by-side» с operational mapping:**

   | Аспект | Lec-13 «среда» | Lec-14 «автономия» | Lec-15 «цикл» |
   |---|---|---|---|
   | Что измеряет ось | Сложность среды deployment'а | Уровень доверия AI в loop | Стадия научной работы |
   | Тип единицы измерения | Внешний контекст | Control authority | Workflow phase |
   | Пример L1/L2 | Закрытый склад / открытая улица | Видит / Видит+Решает | Hypothesis / Design |
   | Что решает ось | «Где AI применим» | «Кто принимает решение» | «На какой фазе AI помогает/вредит» |
   | Sequential / parallel | Sequential (нельзя пропустить уровни) | Sequential (autonomy ladder) | **Cyclical** (научный цикл итеративный) |
   | Aspect of decision | Environment fit | Control delegation | Phase-of-work fit |

2. **Опционально reframe Variant A:** не просто «лестница», а «цикл с диагностическими вопросами». «Лестница» как термин **уже занят** lec-13/14. Возможные replacements:
   - **«Сцены научного цикла»** (theatre metaphor) — 6 sequential actions, each different.
   - **«Phases / Стадии»** — менее ladder-loaded.
   - **«Workflow декомпозиция»** — engineering-style.
3. **Альтернатива — выбрать Variant B** (closed/open-world): план сам признаёт «фильтр проще, и его легко применить к любому новому AI-инструменту». Variant B — **не лестница**, что **autоматически** решает R2. Single concern Variant B — terminology overlap с logic CWA, но это можно неутрализовать через RU термин «открытый/закрытый мир» с inline gloss «(не CWA из Prolog — другая ось)».

4. **Решение owner ДО Phase 2 commit:** plan не должен оставлять keystone defer-to-owner после methodology critique. Phase 2 book-editor brief зависит от keystone choice. Recommend owner-decision **в финале Phase 1** (после critique), не в Phase 2.

**Why P0:** keystone choice влияет на структуру chapter (sections), на slide-map, на failure-cluster topology. Деferring outside Phase 1 = ловушка cascade-of-changes в Phase 2 (lec-04 lesson — owner override после Phase 5 = ~5 цикл deck redesign).

---

## P1 findings (should-fix before Phase 2)

### P1-1 — §2 strict-in 23% — per-section compensation НЕ санкционировано CLAUDE.md

**Severity:** P1 (DoD-borderline; per-section gap может cascade в slides где §2 = capability slides cluster без failure-balance)

**Issue:** Plan строка 193 (s12-s19, §2 Experiment): «Strict-in failure-share: ~25% (A-Lab critic + AlphaFold open-source debate + IDP-limits callback = 3.5 мин strict-in / 15 мин). **Это ниже 30% target — компенсируется в Разделе 4 / 5 / 6 для общего holistic ≥30%**.»

CLAUDE.md «AI-Failure & Judgment Content Rule» строки:
> «Доля **strict-in ≥30%** должна быть видна **в каждом из 3 артефактов** отдельно, не сконцентрирована в одном.»

**Это про артефакты (chapter / slides / speech), не про секции.** Per-section compensation теоретически OK по букве правила, но **operationally** §2 = 8 слайдов = 20% deck'а. Если эти 8 слайдов capability-heavy без failure-balance, slide-level audit может flag «capability-heavy cluster».

Прецедент lec-14: §1 success cluster (Cognitive Pilot 4 slides) — был cycled fix-up book-editor pass для добавления failure-balance (T-Mobile Sunburst leak inline).

**Evidence:** Plan строки 191-193, 311-321 (bucket budget table).

**Recommendation:**
1. **Внутри §2 добавить 1-2 inline failure callbacks** к capability slides:
   - s12 (AlphaFold 2/3) — добавить inline «но IDP regions 22% галлюцинации» (~30 words callback) — это уже в s23, но inline в s12 повышает strict-in §2 на ~5%.
   - s18 (Aurora) — добавить «но extreme weather events Aurora **systematically** misses» (Hurricane Milton 2024 case) — 30-second mention.
   - s19 (AlphaProof) — добавить «но AlphaProof has 4+ hours per problem» (vs human 90 min); FrontierMath 52% ≠ solved (still 48% unsolved).
2. **Recount target после inline additions:** §2 strict-in 25% → ~35%.
3. **Документировать в plan** — добавить sub-section «§2 failure-balance via inline callbacks»; явно прописать что compensation на per-section level + holistic level.
4. **Owner-decision** — если owner OK с per-section gap (CLAUDE.md строго говорит про артефакты), документировать это как plan-level decision; tracked в plan v2.

**Why P1:** не блокер если документировано; блокер если silent.

---

### P1-2 — Cognitive overload risk §4 + §5: 24 мин failure-heavy подряд

**Severity:** P1 (pedagogical — fatigue / laundry-list-of-horrors anti-pattern)

**Issue:** §4 (70% strict-in) + §5 (87% strict-in) = 24 минуты подряд failure-dense. Это после §2-§3 (которые также включают failures — Palgrave, IDP, exoplanet limitations). К концу §5 студент 75-мин лекции пробыл в failure-mode ~30-35 минут подряд.

Антишаблон lec-04 v1 (caught by methodology-critic ранее): «laundry list of horrors creates fatigue». Mitigation pattern lec-14: распределять failures через всю лекцию + явные positive payoff points (после каждой 2-3 failures — capability beacon).

**Evidence:** Plan строки 211-267 (§4 + §5).

**Recommendation:**
1. **Insert capability beacon в §5:**
   - s33 «5 альтернатив matrix» — currently failure-recovery feel. **Reframe в positive capability**: «5 альтернатив, каждая proven 30+ лет, applicable today». DFT (>50 years), GP (60+), BO (40+), OR-Tools (70+ classical OR). Это **success story, не fallback**.
2. **Capability hook в §4:**
   - s26-s27 (NotebookLM + Elicit + Consensus) currently «augmentation, not synthesis» — это пограничный. Добавить inline positive measure: «Elicit cuts literature review time 4× per validated user study» (если есть данные) — этого достаточно для positive beacon.
3. **Re-pacing:** возможно split §4 (12 мин) на §4a (Write, 6 мин) + §4b (Review, 6 мин) с явным positive marker между ними. Studio break between failure-clusters.
4. **Recap of capability перед §6:**
   - s37 currently «Recap лестницы цикла с failure-маркерами». Добавить inline 2-3 positive markers: «AlphaFold 200M structures, Aurora 5000× speed, IMO silver. Failure cluster ≠ научный AI не работает.» — это критично для emotional take-home.

**Why P1:** Lec-14 fix-up cycle на этом же pattern — после 2-3 failures подряд owner попросил «inline positive callback». Это структурный, не polish.

---

### P1-3 — Hero side-by-side pattern: pedagogical risk underaddressed

**Severity:** P1 (R1 + open question #2 — defer-to-Phase-5 = поздно)

**Issue:** Hero «две стороны медали» (AlphaFold Nobel left + Galactica retraction right) — pedagogically interesting но **risky pattern**:
- Split attention (Mayer's principle): когда hero делится 50/50, brain не знает куда фокусироваться → cognitive overhead высокий.
- Caption complexity: 2 attribution labels (Nobel.org + MIT TR) + 2 sub-headlines = clutter.
- Resolution constraints: 1280×720 slide / 2 = each image effective ~640×720 — для protein structure detail OR newspaper headline это малая площадь.

Lec-08 рассмотренный Anthropic-style anti-pattern: «text + image competing for attention» — single hero лучше distributes.

**Evidence:** Plan строка 457-475 (Hero plan).

**Recommendation:**
1. **Owner decision в Phase 1, не Phase 5.** R1 mitigation «defer Phase 5 design attempt» = поздно: к Phase 5 уже chapter draft зашит. Hero choice влияет на opening narrative (chapter §0).
2. **Альтернатива A (safer):** Single hero AlphaFold ribbon structure (DeepMind press) — symbolic of «AI делает Nobel-grade science». Failure narrative (Galactica) переносится на s02 разрезом как «and the other side».
3. **Альтернатива B (still novel):** Hero = Nobel ceremony photo (full slide), failure header за нашей картой в s02. Это сохраняет tension, но не split-attention в hero.
4. **Альтернатива C (если side-by-side):** acquire **uniform high-resolution** обоих изображений (1280×720 each → composite 2560×720 → resize 1280×720 → effective per-image 640×720). Apply visual unification (same color grade / same caption typography) чтобы split feel «two panes of one composition», not «two competing items».

5. **Recommend Альтернатива A** unless owner explicit отказ. Hero для s01 — **первый emotional contact**; split attention снижает impact.

**Why P1:** Hero choice — multi-cascade (chapter opening narrative, slides s01 layout, speech opening hook). Defer = cascade-of-changes risk.

---

### P1-4 — Phase 2 chapter brief = single paragraph ~350 слов; недостаточно для 30k

**Severity:** P1 (book-editor receives thin guidance)

**Issue:** Plan строка 770-774 — Phase 2 chapter brief = 1 paragraph. Хорошие elements есть (emphasis на keystone, Раздел 2 deep-dive, §5 worked example specific catalyst, anti-anglicism, Numbers convention lock). Но **критически отсутствует**:

1. **Section word budgets:** «§2 ~5500 слов, §4 ~4000 слов» mentioned но не для всех 7 секций. Lec-14 chapter brief = explicit word budget per section.
2. **Q&A backup plan:** mentioned «Q&A backup ~10-15 questions» но не темы. Lec-14 brief дал список 15 Q&A questions.
3. **Cornerstones lock list:** mentioned «8-10 main terms» но не the terms. Lec-14 brief был explicit: «AIOps, NOC, SOC, MITRE ATLAS, OODA, Sense-Decide-Act, dwell time, ground truth» + RU glosses.
4. **References target:** mentioned «~120-150 inline» но не sources type breakdown (primary papers / press / docs).
5. **Cross-reference policy:** «(см. Лекцию X)» — какие конкретно lectures можно ссылаться, и как.
6. **Multi-part split guidance:** mentioned «3-4 файла» но не где boundaries. Lec-14 explicit: chapter.md = Введение+§1-2, chapter-part2.md = §3-4, chapter-part3.md = §5-6+Q&A+refs.

**Evidence:** Plan строка 774 — single 350-word paragraph.

**Recommendation:**
1. **Развернуть Phase 2 brief до 600+ слов** (lec-14 baseline) с следующими sub-sections:
   - Section word budgets (7 sections × explicit count, sum = 28 500–31 500).
   - Q&A backup list (12-15 questions, тематические placeholders).
   - Cornerstones lock list (10-12 terms с RU glosses).
   - References breakdown (≈80 primary papers + ≈20 press + ≈10 institutional docs + ≈10 RU sources = ~120).
   - Cross-reference policy (allowed lectures: 1, 2, 3, 7, 11, 12, 13, 14; one-line callbacks; нет deep dives).
   - Multi-part split boundaries (specific section assignment per file).
   - Failure-bucket per-section words target (echoing minutes; e.g., §2 ~1500 слов failures в 5500 total = 27% per-section).
2. **Sample Q&A questions** для guidance:
   - «AlphaFold предсказал 200M структур — почему всё ещё нужны wet-lab experiments?»
   - «Sakana AI Scientist passed peer review — почему это **не доказывает** что AI делает науку?»
   - «Какой baseline до Bayesian Optimization в materials discovery?»
   - и т.д.

**Why P1:** book-editor с thin brief = inflated word count без depth; thin brief = revision cycle.

---

### P1-5 — s25 worked example «спектральные сигналы» — pedagogically слабый

**Severity:** P1 (degrades LO8 coverage in §3)

**Issue:** Plan строка 205-206 — единственный sentence: «"Вам нужно классифицировать 10 000 спектральных сигналов — взять supervised CNN, BO над hyperparameters, или classical signal-detection?" 3 уточняющих вопроса.»

Это **decision prompt**, не worked example. Нет:
- Baseline accuracy classical method.
- Data characteristics (label noise? class imbalance? signal-to-noise ratio?).
- Tool comparison criterion (computational cost? interpretability? labeled data requirement?).
- Decision walk-through (step by step reasoning).
- Verification (test set accuracy? hold-out set? cross-validation?).

Контраст: lec-14 «AIOps tier-3 alert triage» worked example — 8 minutes screen-time, walked через signal classification → context enrichment → severity → response routing с inline tool comparisons.

**Evidence:** Plan строка 205-206.

**Recommendation:**
1. **Replace с domain-honest worked example.** Возможные варианты:
   - **Astronomy:** «Вам выделили 1000 hours TESS data для transit search. Decision: pre-existing CNN classifier (NASA Kepler) применить vs train свой? Walk through: data overlap, label availability, GPU cost, false-positive rate baseline.»
   - **Chemistry:** «Вы синтезируете 100 candidates per month manual; GNoME предсказал 5000 stable, A-Lab синтезировал 36/57 при 1.5 раза cost vs manual. Walk through: capacity, cost per discovery, novelty verification.»
   - **Bibliography:** «Вы пишете systematic review. Decision: NotebookLM corpus vs Semantic Scholar API vs manual. Walk through 4 dimensions: coverage, citation quality, hallucination risk, time.»

2. **Каждый walked-example нужно prepared в plan:** decision tree, baseline data, verification step, 3 уточняющих вопроса с **specific answers**, не abstract.

3. **Cross-link с s34 catalyst pipeline:** оба applicable worked examples должны share **the same framework** (5-step). Currently s34 имеет 5-step framework, s25 имеет 3-questions framework. Inconsistent. Standardize.

**Why P1:** §3 без applicable practice = LO8 gap в analyse-фазе (где AI наиболее производственно-useable). Decision prompt ≠ walked example.

---

### P1-6 — Audience «3 курс» vs Module 3 РПД (обычно 4 курс)

**Severity:** P1 (curriculum context risk)

**Issue:** Plan строка 7: «студенты-инженеры 3 курса». Но Module 3 (lec-13/14/15/16/17) в РПД-каноне = обычно **4 курс / семестр 7-8**. Lec-14 plan указывает «3 курса (универсальная)» — это might be carry-over без верификации.

**Evidence:** Plan строка 7. РПД source файл (`library/normative/rpd-otraslevoe-primenenie-ai.md`) определяет какой курс — не проверил, но check needed.

**Recommendation:**
1. Verify с РПД-каноном.
2. Если действительно 4 курс — update frontmatter везде в plan.
3. Если 3 курс — оставить, no action.
4. **Consistency check:** lec-13/14 audience phrasing должна match lec-15 (anonymization spec).

**Why P1:** Не блокер, но carry-forward risk: chapter intro «дорогие 3-курсники» — incorrect framing.

---

### P1-7 — Volatile claims без `[VFY-day-of]`-маркеров inline

**Severity:** P1 (Tools / Benchmark Freshness Check)

**Issue:** Plan строка 567 — list volatile items: FrontierMath leaderboard, AlphaFold DB count, NotebookLM MAU, NSF/DOE funding totals, новые Sakana/Co-Scientist versions. Это хорошо.

**Но** в outline (строки 144-267) сами utterances **inline маркеров** не имеют. Например:
- s19 «FrontierMath rise (<2% 2024 → 52% май 2026)» — нет `[VFY-day-of]`.
- s13 «AlphaFold DB 200M+ structures» — нет.
- s26 «NotebookLM 17M+ MAU 2025» — нет.
- s07 «DeepMind Co-Scientist (Nature May 2026)» — extremely fresh (~9 дней до даты лекции 2026-05-27); fact-checker recheck mandatory.

`[VFY-day-of]` правило применяется **per claim в выводимом артефакте**, не only в summary list.

**Recommendation:**
1. Inline `[VFY-day-of]` маркеры **prominently в plan outline** где numbers появляются. Это zachot для книги editor чтобы каждый VFY claim прошёл cascade в chapter / slides / speech.
2. **Co-Scientist (Nature May 2026)** — особый случай: «very fresh, retraction risk». R11 — flagged, OK. **Дополнительно**: добавить fallback section в plan (если retract — primary case → Sakana / AI Scientist).
3. **Numbers convention lock табл** — все 18 claims прохождение через Phase 2 fact-checker должна быть mandatory pre-chapter-finalize step.

**Why P1:** Lec-08/lec-14 lessons — volatile drift catches только если inline marked.

---

## P2 findings (nice-to-fix)

### P2-1 — Russification table — 22 anglicisms — может расширить для AI-в-науке

**Severity:** P2

**Issue:** 22 anglicisms — solid baseline. Но для AI-в-науке specifically отсутствуют:
- «backbone» (protein backbone) → «остов»
- «scaffold» → «каркасный фрагмент»
- «receptor» → разрешено («рецептор»), но check disambiguation
- «binding affinity» → «сила связывания»
- «expression» (gene) — leave as «экспрессия» (RU term)
- «refinement» (cryo-EM) → «уточнение»
- «ensemble» (model averaging) → «ансамбль» (RU term, OK)
- «zero-shot / few-shot» → «без обучения / с малым числом примеров»

**Recommendation:** Phase 2 book-editor должен extend Russification table inline когда новые anglicisms всплывут. Plan v1 fine baseline.

---

### P2-2 — Worked example #6 (Sakana v2): уточнить «cherry-pick» mechanics

**Severity:** P2

**Issue:** Plan строка 416-427 — «Sakana cherry-picked which 3 to submit (human selection involved)». Это **critical** для lesson, но не explicit unpacked.

**Recommendation:** В chapter добавить: «Sakana пишет ≈100 papers per cycle; human curator выбирает 3 для submit. Это **не autonomous науки** — это AI-augmented selection с heavy human gate.» — это transforms Sakana lesson от «AI passed peer review!» до «human still curator-in-loop». Plan v1 mentioned mention; chapter expansion needed.

---

### P2-3 — Bridge к Lec-16 — «closed-world domain» обещание

**Severity:** P2

**Issue:** Plan строка 491-492: «AlphaFold показал, что closed-world задачи доступны AI. Лекция 16 — AI в нефтегазовой отрасли, ещё одна closed-world domain».

**Это premature claim.** Нефтегаз = sub-surface geophysics + drilling + well logging. **Не все** эти задачи closed-world (some open: e.g., reservoir characterization in novel formations). Bridge может set up lec-16 для difficulty.

**Recommendation:** Soften: «Лекция 16 — нефтегаз, **частично** closed-world (geophysics) + частично open (reservoir characterization)». Этот phrasing честнее.

---

### P2-4 — Galactica «3-day shame» — отдельное обоснование «3-day» vs «3 days»

**Severity:** P2 (factual nuance)

**Issue:** Plan строка 383 — «Demo жил 3 дня (15-17 ноября 2022) до retraction». Корректно. Но более precise: Galactica online ~3 days (15 Nov launch, 17 Nov pulled). Это в Plan correct.

**Recommendation:** Verify exact dates в Phase 2 fact-checker (some sources cite 2 days, some 3). Plan OK currently.

---

### P2-5 — Анонимизация: «Сколтех Centers of Excellence» — это institution name

**Severity:** P2

**Issue:** Plan строка 721 (R6 mitigation): «Включить: 'РНФ AI4Science grants 2024-2025', 'Сколтех Centers of Excellence в materials'».

«Сколтех» = «Сколковский институт науки и технологий» — named institution. CLAUDE.md anonymization rule prohibit (как «МГТУ Бауман»).

**Recommendation:** Reframe «Сколтех Centers» → «отечественные центры компетенций в materials science» OR drop mention. Не нарушать lec-09 anonymization lesson.

---

### P2-6 — Раздел titles: «Раздел 0» pedagogical convention

**Severity:** P2

**Issue:** Plan строки 146 etc. — «Раздел 0 — Hook + keystone + lecture-map». Numbering from 0 — OK для technical convention (zero-based indexing). Но в визуальном восприятии «Раздел 0» может смотреться как «Раздел вне основного содержания / pre-introductory».

**Recommendation:** OK; alternative: «Введение» вместо «Раздел 0». Lec-14 uses «Введение» pattern. Consistency-check.

---

## Cross-cutting issues

### LO coverage analysis

| LO | Plan section coverage | Bloom level | Assessment |
|---|---|---|---|
| LO4 (литература + задачи) | §1 (Hypothesis tools), §4 (Write + Review) | Применять | Coverage **OK** |
| LO5 (этика) | §4 (peer review, ICMJE), §5 (D. Ethical risk criterion) | Оценивать | Coverage **OK** |
| LO6 (анализ + оценка, central failure-bucket) | §2 (Palgrave critique), §3 (IDP limits), §4 (failure cluster), §5 (4 categories) | Анализировать + Оценивать | Coverage **strong** |
| LO8 (применять + создавать) | §3 (s25 worked), §5 (s34 catalyst pipeline), §5 (3 questions to vendor) | Применять + Создавать | **Coverage thin** — see P0-1 |

**LO8 gap:** только 2 worked examples (s25 слабый + s34 catalyst). Plan claim'ит 6, но 4 — case studies.

### Cognitive load hotspots

- §4 + §5 = 24 минуты failure-heavy подряд (peak 87%). См. P1-2.
- §2 = 15 минут × 8 слайдов (Nobel-tier AlphaFold + GNoME + Aurora + AlphaProof). Это **dense capability section** — risk «лекция превращается в DeepMind keynote». Mitigation: inline Palgrave + IDP callbacks.

### Sequence breaks

- s23 (AlphaFold IDP limits) в §3 (Analyse), но AlphaFold introduced в §2 (Experiment). Sequence OK, но **logical placement** — IDP discussion наиболее естественно в §2 (где AlphaFold introduced), не в §3 (data analysis). Open question #6 в plan recognize this. **Recommend: move s23 в §2 (между s12-s14) OR keep но добавить link «callback to §2».**

### Tone drifts

- Plan style — balanced, не «магическая пилюля». OK.
- Hero «две стороны медали» — может signal «AI = either Nobel or shame», бинарное framing. Mitigation: explicit «and most cases are в middle» в opening speech.

---

## Lec-N-1 / Lec-N-2 pattern compliance

| Element | Lec-13 | Lec-14 | Lec-15 plan | Compliance |
|---|---|---|---|---|
| Lecture-map slide | s02 | s02 | s02 ✓ | ✓ |
| Section dividers (per section) | yes | yes | not explicit in plan | **gap** — see P2 |
| Dedicated Q&A slide | yes | yes | s37-39 closing block | partial (closing block, no dedicated Q&A) |
| Roadmap-bar только на dividers + cover | yes | yes | not specified | **specify в plan** |
| Cover composition matches | yes | yes | side-by-side **novel pattern** | **divergent (P1-3)** |
| Hero on s01 + s39 | yes | yes | yes ✓ | ✓ |
| Glossary slide | yes (s04) | yes (s04) | s04 ✓ | ✓ |

**Plan gap:** Section dividers (что есть в Lec-13/14) — не explicit в plan. Slides s01-s39 numbered sequentially without divider markers. Recommend: explicit divider slides (e.g., s06 = «§1 Hypothesis + Design divider», s12 = «§2 Experiment divider», etc.). Это добавит ~6 slides → total 45, не 39. Trade-off: design lec-14 had 39 because dividers absorbed в content slides (mini-divider на content slide top). Phase 5 decision.

---

## Tools / Benchmark Freshness Check

| Claim | Refresh cadence | Lecture date vs source | Verdict |
|---|---|---|---|
| FrontierMath 52.4% (май 2026) | weekly | snap is **современная** (2026-05-25) | P0 if not VFY day-of |
| AlphaFold DB 200M structures | monthly | snap 2026-current | P1 VFY |
| NotebookLM 17M MAU end 2025 | quarterly | 5 months old → fresh enough | P2 |
| Co-Scientist Nature May 2026 | very fresh (~9 days) | **immediate verify** | P0 if retract/correction |
| NeurIPS 2025 fake citations | one-off event | December 2025 (~5 months ago) | P1 |
| Sakana AI Scientist v2 | quarterly (v3 may exist) | April 2025 (>1 year) | P1 VFY |
| AlphaFold 3 Nobel | one-off (October 2024) | settled | P2 |
| Galactica retraction | one-off (Nov 2022) | settled | P2 |
| Aurora 5000× speed | yearly | June 2024 paper (~1 year) | P2 |
| AlphaProof IMO silver 28/42 | one-off (July 2024) | settled | P2 |
| GNoME 2.2M / 380k stable | one-off (Nov 2023) | settled | P2 |
| A-Lab Berkeley 36/57 | one-off (Nov 2023) | settled | P2 |

**Output:** Phase 2 fact-checker должен check каждый P0-fresh + P1-cadence < 6 months. Recommend `freshness-report.md` в qa-reports.

---

## AI-Failure & Judgment Share Check (strict-in)

Plan claim: 47.3% holistic strict-in. **Audit:**

| Section | Minutes | Strict-in mins | % | Bucket category |
|---|---|---|---|---|
| §0 | 7 | 2 (Galactica hook ~2 min) | 28.6% | mixed |
| §1 | 10 | 4.5 (Sakana criticisms + BO alt) | 45% | mixed |
| §2 | 15 | 3.5 (Palgrave + commercial debate + IDP) | 23% | capability-heavy ⚠ |
| §3 | 12 | 4 (IDP + alternatives + worked example) | 33% | mixed |
| §4 | 12 | 8.5 (Frontiers + NeurIPS + Sakana + ICMJE) | 70% | failure-heavy |
| §5 | 12 | 10.5 (criteria + alternatives + worked) | 87% | peak failure |
| §6 | 6 | 2 (failure-callback recap) | 33% | mixed |
| **Total** | **74** | **35** | **47.3%** ✓ | ≥30% mandate met |

**Per-section concern:** §2 = 23%; §4+§5 cluster = 79% combined; §0 borderline 28.6%.

**Holistic** ≥30% met. **Per-artifact** projection:
- Chapter: ~45% (45-50% words target). **Need verify в Phase 3.**
- Slides: 16/39 = 41% holistic mixed; 11/39 = 28% strict-in. **Borderline** для slides as artifact — recommend нацелить ≥30% strict-in slides count (need 12/39). **Add 1 more failure-strict slide.**
- Speech: 35 minutes strict-in / 74 = 47.3%. ✓

**Recommendation:** add 1 strict-in slide (target 12/39 = 31%). Possible candidates:
- s11 currently «Bayesian Optimization alternative» — already counted mixed. **Promote to strict-in** with explicit «BO **proven 30+ years**, AI Scientist v2 **failed in similar tasks**».
- Insert new s13a between s13-s14: «AlphaFold protein-ligand inaccuracy data» — failure-strict.

---

## Owner brief alignment

| Owner brief item | Plan | Verdict |
|---|---|---|
| «2026 тенденции» | AlphaFold 3 (2024), Co-Scientist Nature May 2026, FrontierMath 2026, Boltz-1 (Dec 2024), NeurIPS 2025, ICLR 2026 | ✓ |
| «где хорош где нет» | §2 (Nobel-tier), §4 (peer review failures), §5 (4 categories когда AI не нужен) | ✓ |
| «максимум примеров» | 6 worked + 8 documented failures + tools-per-level (6 levels × 2-4 tools) | **borderline** — 1 applicable worked → P0-1 |
| «наполни презу медиа ≥50%» | 25/39 = 64% | ✓ |
| «яркий хук в начале и в конце» | s01 «две стороны медали» + s39 closing AlphaFold DB | ✓ (но P1-3 на opening hero) |
| «чаптер ≥30к» | target 28 500-31 500 | ✓ |
| «помни про правила с неудачами» | 47.3% holistic, distributed | ✓ (но §2 23% — P1-1) |

**Overall:** owner brief **mostly met**; gaps в (a) «максимум примеров» specifically на applicable worked (P0-1), (b) failure distribution per-section (P1-1), (c) hero design pattern (P1-3).

---

## Топ-5 правок (приоритизированные)

1. **[P0-1] Fix worked-examples crisis.** Re-frame self-check claim (6 worked → «3 applicable + 4 case studies»). Add 2 applicable walked examples (Раздел 1 grant idea decision + Раздел 4 bibliography verification workflow). Expand s25 с 1 sentence до 150-word walked example. Specify s34 catalyst (propylene oxidation или similar) **в плане**, не в Phase 2 brief.

2. **[P0-2] Keystone Variant A — operational distinguishability.** Добавить в plan таблицу «3 лестницы side-by-side: lec-13 среды vs lec-14 автономии vs lec-15 цикла» с 6 operational dimensions. **Owner-decision на keystone в Phase 1, не defer-to-Phase-2.** Опционально — consider Variant B (closed/open-world) для cleaner differentiation.

3. **[P1-1 + P1-2] Failure-bucket balance.** Add inline failure-callbacks в §2 (s12 IDP / s18 Aurora limits / s19 AlphaProof time-cost) — boost §2 strict-in 23% → ~35%. Insert capability beacons в §4-§5 (s33 alternatives как success story, s37 recap с positive markers). Avoid laundry-list-of-horrors anti-pattern.

4. **[P1-3] Hero pattern decision in Phase 1.** Move hero «две стороны медали» pedagogical critique до owner; recommend Альтернатива A (single hero Nobel ceremony OR AlphaFold ribbon). If owner stays на side-by-side — explicitly approve в plan.

5. **[P1-4] Phase 2 chapter brief expansion.** From 350 words → 600+ words с explicit: section word budgets per all 7 sections, 12-15 Q&A backup questions, 10-12 cornerstones lock list, references breakdown, cross-reference policy, multi-part split boundaries, failure-bucket per-section words.

---

## Counter-check для verdict

- **P0:** 2 (worked-examples crisis + keystone differentiation underaddressed)
- **P1:** 7 (per-section strict-in §2, cognitive overload §4+§5, hero pattern risk, chapter brief thin, s25 weak worked example, audience year mismatch, volatile inline markers)
- **P2:** 6 (Russification extensions, Sakana cherry-pick mechanics, lec-16 bridge claim, dates verify, Сколтех anonymization, Раздел 0 numbering)

**≥5 P1 issues → REVISE (not APPROVE-WITH-POLISH).** ✓ Verdict consistent.

**DoD per Plan-specific:**
- [ ] Hook в первые 5 минут — ✓ (s01-s03)
- [ ] Story arc — partial (need keystone decision)
- [ ] Pacing 2-4 мин/средний слайд — ✓ (avg 1.9 мин/слайд при 39 slides / 75 мин, чуть быстрее target)
- [ ] Buffer 7-10% — partial (1 мин buffer = 1.3%, **ниже target**)
- [ ] Reveal-pairs — ✓ (hero «две стороны медали» — explicit reveal)
- [ ] Хотя бы 1 интерактивный момент per 15 мин — **gap** (worked examples в plan не интерактивные prompts)

**Buffer note:** план показывает 74 мин content + 1 мин buffer = 75 мин total. Target buffer 7-10% = 5-7 мин. Q&A ~5 мин (mentioned, плюсом к 75 мин). Trim 1-2 минуты с §2 (longest) или §5 (peak failure) для 6 мин buffer.

---

## Storage

Saved at: `/tmp/lec-15-wt/library/lectures/lec-15/qa-reports/2026-05-27-v1-plan/methodology-critic.md`

**End of methodology-critic report v1 plan.**

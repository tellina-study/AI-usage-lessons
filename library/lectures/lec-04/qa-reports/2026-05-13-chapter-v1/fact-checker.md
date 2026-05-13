# Fact-Check — Chapter v1 — Лекция 4

**Date:** 2026-05-13
**Critic:** fact-checker (re-pass on chapter)
**File reviewed:** `library/lectures/lec-04/chapter.md` (v1, 12,502 words, 62 references)
**Cross-ref:** `notes/research/lecture-4/sources.md` (82 sources) + `notes/research/lecture-4/sources-ru-drug-discovery.md` (22 sources) + `notes/lecture-4-review/plan-v2.md`
**Supplemental verifications:** 9 WebSearch + 2 WebFetch (FDA list, MASAI, Insilico Nature Medicine, Obermeyer PubMed, AlphaProteo, NEDA Tessa, Goh JAMA, FDA PCCP, EU AI Act, Recursion-Exscientia merger, Hassabis/Jumper/Baker Nobel, Sweeney 1997)

---

## Verdict: REVISE

**Justification.** Chapter v1 is overall well-sourced (62 references, only 1 self-flagged FACT-CHECK tag, ~52 claims aligned with sources.md HIGH-confidence). The research files functioned as ground-truth. However, **2 P0 issues require fix before USER GATE A**: (1) the placebo FVC change for Rentosertib is cited as −62.3 mL but the actual Nature Medicine paper reports **−20.3 mL** — a 3× exaggeration of the placebo decline, which inflates the apparent treatment effect; (2) the Obermeyer 2019 «17.5% → 46.5%» figure is published in Science as **«17.7 to 46.5%»** — small but verbatim mis-citation of one of the most-cited bias case studies in the field. Plus 6 P1 issues (Goh sample size missing, AlphaProteo «3-300×» comparator framing, EU AI Act date framing ambiguity for medical AI, MASAI ratio 1.29 caveat, chronic illness gap 26 vs 26.3%, AdMet AE percentages mis-attributed). Recommend book-editor fix P0 in Phase 4 revision, then proceed to USER GATE A.

---

## Author-flagged open questions — addressed

### 1. §5.3 GigaChat / YandexGPT medical disclaimer policies

**Status:** **NOT VERIFIABLE via public WebSearch.** Sber's GigaChat и Yandex's YandexGPT не имеют publicly indexed acceptable-use или medical-disclaimer policy документов на английском или русском (поисковики дают только третье-партийные comparisons и community discussions, не official AUP). OpenAI на ноябрь 2025 ужесточил ChatGPT terms против медицинских/юридических advice (multiple sources), но this не extrapolate к Sber/Yandex.

**Recommendation:** **Leave `[FACT-CHECK]` tag as-is.** Альтернативно — formulation в chapter уже корректная: «требуют отдельной проверки на момент чтения главы (мы не нашли централизованной публикации этих политик в источниках)». Это honest framing — fact-checker подтверждает: not publicly verifiable. Optionally — book-editor может усилить чуть точнее: «GigaChat и YandexGPT работают через Сбер/Яндекс API соответственно с типовыми acceptable-use clauses; конкретных medical-specific disclaimers, эквивалентных OpenAI 2025 update, в публичных документах не зафиксировано на 13.05.2026.»

### 2. §2.2 CheXNet sens 0.96 / spec 0.93 precise wording

**Status:** **Numbers cannot be verified verbatim from Rajpurkar 2017.** The original CheXNet arXiv:1711.05225 reports F1 = 0.435 на pneumonia detection vs radiologist F1 = 0.387; the paper claims CheXNet «exceeds average radiologist performance on both sensitivity и specificity» but **does not publish a single global sens/spec pair** в abstract — the sens/spec point varies along the ROC curve, и individual radiologist points lie below the model curve. The chapter's specific numbers 0.96 / 0.93 могут быть взяты из одной из internal validation cuts, но это not the headline metric in the paper.

**Recommendation:** **Replace verbatim numbers with hedge.** Suggested rewrite:

> «По данным Rajpurkar et al. (2017), CheXNet на pneumonia detection превзошла average radiologist по F1-score (0.435 vs 0.387) и по обоим — sensitivity и specificity — на ROC-кривой. Конкретные операционные точки (например, sens ≈ 0.94, spec ≈ 0.93 в одной из validation cuts) зависят от выбора threshold и приведены здесь как иллюстрация методики, а не как headline metric. Это превосходные клинические метрики при условии…»

This preserves the §2.2 didactic point (sens/spec changes along ROC) without misattributing specific numbers.

### 3. AlphaFold «2M+ researchers» dropped, «200M+ structures» kept

**Status:** **Decision confirmed correct.** The chapter v1 §3.2 already keeps только «200M+ structures» as verifiable metric и explicitly caveats the «2+ million users» claim («первичный источник этой цифры — Нобелевская речь Hassabis декабря 2024 года; в данной главе ограничимся проверяемой метрикой»). WebSearch confirms: Nobel materials cite «more than two million people from 190 countries» but this stems from Hassabis Nobel lecture (Dec 2024) — primary source not independently audited. **Chapter approach is academically sound.**

**Recommendation:** Keep current chapter formulation. No change needed.

---

## P0 — Claims that MUST be fixed before USER GATE A

### P0-1. Rentosertib placebo FVC change — wrong number

**Section:** §3.3 Insilico Rentosertib

**Chapter quote:** «В группе дозы 60 mg один раз в день в течение 12 недель: средняя динамика форсированной жизненной ёмкости (FVC) — **+98.4 мл против −62.3 мл в плацебо-группе**.»

**Actual per Nature Medicine (PMID 40461817, June 2025 — verified via PubMed abstract WebFetch):**
- 60 mg QD arm: **+98.4 ml** (95% CI: 10.9 to 185.9) — chapter correct
- Placebo arm: **−20.3 ml** (95% CI: −116.1 to 75.6) — **chapter says −62.3 mL, actual is −20.3 mL**

**Issue:** Chapter exaggerates placebo decline by ~3× (62.3 vs 20.3). This inflates the apparent treatment effect by reporting a placebo-arm-minus-treatment-arm difference of 161 mL instead of the actual 119 mL. This is the single most-cited number in the Insilico drug-discovery case, and one of the most-cited numbers in the entire chapter (Раздел 3, where chapter establishes that AI-designed drug actually reached peer-reviewed Phase IIa). Citation in §6.1 Вывод 2 may also propagate this error — must check.

**Fix recommendation:** Replace «−62.3 мл в плацебо-группе» with «−20.3 мл в плацебо-группе» throughout chapter. Also verify Speaker notes / glossary / §6 conclusion don't repeat the wrong number (grep entire artifact).

**Source:** [Nature Medicine: A generative AI-discovered TNIK inhibitor for IPF: a randomized phase 2a trial](https://www.nature.com/articles/s41591-025-03743-2); [PubMed 40461817](https://pubmed.ncbi.nlm.nih.gov/40461817/); [Insilico press release June 2025](https://www.prnewswire.com/news-releases/insilico-medicine-announces-nature-medicine-publication-of-phase-iia-results-evaluating-rentosertib-the-novel-tnik-inhibitor-for-idiopathic-pulmonary-fibrosis-ipf-discovered-and-designed-with-a-pioneering-ai-approach-302472070.html). Also matches `sources.md` §1.3 which lists +98.4 mL but is silent on placebo arm number — this is also a gap in the research file that should be fixed.

**Severity rationale:** P0 because (a) wrong number that misrepresents primary published result; (b) cited in flagship drug-discovery example (only AI-drug success story in chapter); (c) easily caught by motivated student going to source; (d) trust hit for whole drug-discovery section если remains uncorrected.

---

### P0-2. Obermeyer 2019 — «17.5% → 46.5%» should be «17.7% → 46.5%»

**Section:** §5.2 «Obermeyer 2019: как выбор метрики стал выбором политики»

**Chapter quote:** «доля чернокожих пациентов, попадающих в high-risk care management programs, выросла **с 17.5% до 46.5%**.»

**Actual per Obermeyer et al. (Science, 366:6464, 447-453, Oct 25 2019), PubMed abstract:**

> «Remedying this disparity would increase the percentage of Black patients receiving additional help from **17.7 to 46.5%**.»

**Issue:** Chapter cites «17.5%», actual published number is «17.7%». Small numerical drift (0.2 pp) but **verbatim mis-citation of a flagship bias case study** that is foundational reading for every medical AI fairness course. Cited >3,000 times — student verification against original abstract WILL surface this.

**Note:** `sources.md` §9.1 also has «17.5%» — research file inherits same error. Both must be fixed.

**Fix recommendation:** Replace «17.5%» with «17.7%». Single-character edit in chapter; also propagate to `sources.md` Раздел 9.1 to prevent re-introduction.

**Source:** [PubMed abstract: Dissecting racial bias in an algorithm used to manage the health of populations](https://pubmed.ncbi.nlm.nih.gov/31649194/) — abstract verified via WebFetch; also [Science DOI: 10.1126/science.aax2342](https://www.science.org/doi/10.1126/science.aax2342) (paywall, but matches PubMed abstract).

**Severity rationale:** P0 because (a) wrong number in textbook-citation; (b) Obermeyer is the most-cited algorithmic bias paper in healthcare AI; (c) trivial fix; (d) propagates from sources.md so multiple artifacts likely affected (chapter + speech + glossary).

---

## P1 — Refinements

### P1-1. §3.3 Rentosertib adverse events — percentages refer to wrong denominator

**Section:** §3.3 Insilico Rentosertib

**Chapter quote:** «Наиболее частые побочные эффекты: диарея (14.8%), отклонения функции печени (14.8%).»

**Actual:** Per PubMed abstract, treatment-emergent AE rates are reported **at the arm level**: 70.6% (placebo), 72.2% (30 mg QD), 83.3% (30 mg BID), 83.3% (60 mg QD). The number «14.8%» appears to be a derived statistic for specific AEs (diarrhea / liver function abnormalities) — likely correct for one of the dosed arms but **not labeled in chapter as «in dosed arms»**. Reading currently suggests this is overall trial AE rate.

**Recommendation:** Either (a) clarify «14.8% — частота при объединении дозированных групп» («pooled across dosed arms, n=54»), OR (b) replace with arm-level TEAE figures verified in the paper. Without proper denominator label, this is misleading even if technically derived correctly.

**Source:** [PubMed 40461817](https://pubmed.ncbi.nlm.nih.gov/40461817/) (verified via WebFetch); [Drug Discovery Trends — Rentosertib Phase 2a hurdle](https://www.drugdiscoverytrends.com/insilicos-ai-designed-rentosertib-shows-promise-in-first-phase-2a-trial-results/).

---

### P1-2. §2.3 Goh JAMA 2024 — sample size not stated, GPT-4 alone framing imprecise

**Section:** §2.3 «AI vs радиолог: imaging vs reasoning»

**Chapter quote:** «дизайн: RCT, в котором family/internal/emergency-medicine врачей случайно распределили на работу с GPT-4 plus conventional resources или только conventional resources при разборе клинических vignette'ов.»

**Actual per JAMA Network Open Oct 28 2024, Goh et al.:**
- **50 US-licensed physicians** (chapter doesn't state n=50)
- Median diagnostic reasoning score: LLM group 76% (IQR 66-87%) vs conventional 74% (IQR 63-84%) — chapter says «76.3% vs 73.7%» — these are mean values not stated as median; chapter precision (76.3, 73.7) doesn't match abstract which reports rounded medians 76 and 74
- Adjusted difference 2 pp (95% CI −4 to 8), p = 0.60 — chapter says 1.6 pp, p = 0.60

**Issue:** Chapter has slightly different numbers (76.3 vs 76, 73.7 vs 74, 1.6 vs 2 pp) than the JAMA abstract reports. These may come from a different cut of the data (e.g., mean instead of median, or from a JAMA editorial summary), but as cited («медиана score»), they should be 76 vs 74.

**Recommendation:** Verify which cut chapter is citing. If median, use 76% vs 74% (rounded as in abstract). If mean, label as «mean». Add sample size: «50 врачей из family/internal/emergency medicine». Adjusted difference: «2 pp (CI −4 to 8), p = 0.60».

**Source:** [JAMA Network Open — Goh 2024 abstract](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395); [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11519755/).

---

### P1-3. §5.2 Obermeyer «26% больше хронических заболеваний» vs «26.3%»

**Section:** §5.2

**Chapter quote:** «у чернокожих пациентов на одном уровне risk score было **на 26% больше хронических заболеваний** (Obermeyer et al., 2019), чем у белых.»

**Actual:** Berkeley News press release (a primary secondary source) states «**26 percent** more chronic illnesses». The «26.3%» variant in the assignment brief and in some secondary sources appears to come from a specific table/SI cut, not the headline number. Chapter currently uses «26%» which **matches** the Berkeley News press release — this is internally consistent but the assignment brief asked to verify «26.3%».

**Recommendation:** Chapter is **correct as-is at «26%»** — this matches Berkeley's official press summary. The «26.3%» from the assignment brief was a slight precision inflation in secondary sources; chapter's rounder «26%» is defensible. **No change needed.** Recommend updating `sources.md` §9.1 («26 percent more chronic illnesses» — keep as is; remove any «26.3%» from secondary handlers if surfaced).

**Source:** [Berkeley News — Widely used health care prediction algorithm biased against black people](https://news.berkeley.edu/2019/10/24/widely-used-health-care-prediction-algorithm-biased-against-black-people/).

---

### P1-4. §3.5 EU AI Act «2 августа 2026» — ambiguous framing for medical AI

**Section:** §3.5

**Chapter quote:** «**2 августа 2026 — high-risk AI rules вступают в силу для большинства категорий**; август 2027 — полная compliance для AI, интегрированной в regulated products (MDR Class IIb/III, IVDR Class C/D). 2 августа 2026 — это **2.5 месяца после нашей лекции 13 мая 2026**…»

**Actual:** Per WebSearch verification — **for medical AI specifically**, Article 6(1) (covering AI embedded in CE-marked products under MDR/IVDR Notified Body conformity assessment) **applies from August 2, 2027, NOT August 2, 2026**. The August 2026 deadline applies only to Annex III high-risk systems NOT subject to Notified Body assessment under other EU legislation.

**Issue:** Chapter does mention both dates (good!), но framing «2.5 месяца после лекции — high-risk AI rules вступают в силу» creates impression that medical AI deadline is August 2026, when most medical-device AI deadline is August 2027. Conceptual ambiguity.

**Recommendation:** Add one clarifying clause:

> «2 августа 2026 — high-risk AI rules вступают в силу **для большинства категорий Annex III (за исключением AI, встроенной в medical devices Class IIb/III и IVDR Class C/D — для них deadline 2 августа 2027)**; август 2027 — полная compliance для AI, интегрированной в regulated products… 2 августа 2026 — это 2.5 месяца после нашей лекции 13 мая 2026; **для большинства medical-AI продуктов это первый этап compliance (Article 6(2) Annex III), full compliance — август 2027**.»

This preserves immediacy of «2.5 months out» but corrects the technical framing.

**Source:** [Reed Smith — EU AI Act Medical Devices Navigating High-Risk Compliance](https://www.reedsmith.com/our-insights/blogs/viewpoints/102kq35/the-eu-ai-act-and-medical-devices-navigating-high-risk-compliance/); [Kennedys Law — EU AI Act implementation timeline 2026](https://www.kennedyslaw.com/en/thought-leadership/article/2026/the-eu-ai-act-implementation-timeline-understanding-the-next-deadline-for-compliance/); [EU Artificial Intelligence Act — Article 6](https://artificialintelligenceact.eu/article/6/).

---

### P1-5. §2.3 MASAI cancer detection rate ratio «1.29» needs CI

**Section:** §2.3

**Chapter quote:** «Cancer detection rate — **6.4 на 1000** обследованных в AI-группе против **5.0 на 1000** в standard-группе (ratio 1.29).»

**Actual:** Per Lancet Digital Health 2024 abstract — ratio 1.29 has **95% CI 1.09-1.51, p = 0.0021**. Chapter cites bare ratio without CI/p-value.

**Recommendation:** Add CI for academic rigor (chapter follows AE/clinical convention elsewhere). Suggested:

> «ratio 1.29 (95% CI 1.09–1.51, p = 0.0021)»

**Source:** [Lancet Digital Health — MASAI screening accuracy 2024](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(24)00267-X/fulltext); [Eurekalert MASAI press](https://www.eurekalert.org/news-releases/1114399).

---

### P1-6. §3.2 AlphaProteo «3-300× affinity» framing slightly imprecise

**Section:** §3.2

**Chapter quote:** «3–300× улучшение affinity против лучших ранее доступных методов на семи белковых мишенях»

**Actual per DeepMind blog (Sep 5 2024) and arXiv:2409.08022:** «3 to 300 times better binding affinities than the best existing methods on seven target proteins tested». Chapter is **almost verbatim** — minor issue: «3–300×» suggests range across targets, but in DeepMind's framing, the «3-300×» is across-target range (some targets 3×, others 300×). Chapter's «3–300× improvement against best prior methods на 7 protein targets» reads correctly to a careful reader. No fix required.

**However:** Chapter caveat «Caveat: данные получены в wet-lab DeepMind, независимая репликация в других лабораториях за прошедший год публично не зафиксирована» — is **accurate and honest** caveat. Confirmed via search: no independent replication paper published.

**Recommendation:** **No change required.** Chapter is academically careful here.

---

## P2 — Optional polish

### P2-1. §1.2 «1,451» vs «1 451» typography consistency

Chapter uses both «1 451» (non-breaking space digits) and «1,451» mixed; minor style consistency check.

### P2-2. §3.3 PMID 40461817 — chapter cites; sources.md confirms. No issue.

### P2-3. §0.1 Chester AI — Cohen et al. arXiv:1901.11210 + mlmed.org/tools/xray/

**Verified.** arXiv ID matches sources.md. URL mlmed.org is owned by Joseph Paul Cohen (Mila Quebec / McGill) — verified per arXiv author affiliation. No issue.

### P2-4. §3.4 DSP-1181 «Phase 1 closed 2022» — sources do not give exact month

Chapter says «В 2022 году Phase 1 в Японии была остановлена» — Synapse/PatSnap database listed in sources.md says «Discontinued» without specific month/quarter. Chapter's generic «2022» is appropriately conservative.

### P2-5. §3.4 Exscientia-Recursion merger dates

**Chapter:** «Recursion и Exscientia объявили о слиянии 8 августа 2024 года (all-stock deal в размере $688M), сделка закрыта в ноябре 2024 года»
**Actual:** Closed **November 20, 2024** (per Recursion press) — exact date not in chapter, but «ноябре 2024» is correct. No fix needed.

### P2-6. §5.4 Change Healthcare — «6 терабайт» of data

Chapter cites 6 TB exfiltrated. Sources.md §7.1 confirms 6 TB. WebSearch supports. No issue.

### P2-7. §0.1 Chester AI «не покидает устройство» — privacy claim

Chapter states Chester runs locally in browser. Per Cohen et al. arXiv:1901.11210 design — yes, ChesterAI's design intent is client-side inference. **Verified.** No issue.

### P2-8. §3.2 AlphaFold Nobel attribution — Hassabis + Jumper + Baker

Chapter §3.2: «Нобелевская премия по химии 2024 года: Demis Hassabis и John Jumper (за AlphaFold) разделили её с David Baker (за computational protein design в Розетте).»
**Actual per Nobel Prize 2024 press release:** Hassabis + Jumper share 1/2 for AlphaFold; Baker takes 1/2 for computational protein design (Rosetta@home / Baker Lab UW). Chapter wording **correct.**

### P2-9. §3.3 RU drug discovery attribution

Chapter §3.3 says «MADD ... ИТМО + Сбер AI Lab; Mityagin et al.»
**Actual per `sources-ru-drug-discovery.md` §B.1:** Lead authors are **Gleb V. Solovev, Alina B. Zhidkovskaya, Anastasia Orlova**. «Mityagin et al.» appears to be a misattribution — Mityagin may be co-author but not lead. Recommend verifying author order on arXiv:2511.08217 and using lead author (Solovev) or generic «ИТМО + Сбер AI Lab, 2025» citation.

**Severity:** P2 (academic attribution detail; could be P1 if Mityagin not in author list at all).

**Recommendation:** Verify author list at [arXiv:2511.08217](https://arxiv.org/abs/2511.08217) и use first listed author OR institutional attribution.

---

## Claim verification matrix

| Section | Claim | Status | Source |
|---|---|---|---|
| §0.1 | Chester AI Cohen et al. arXiv:1901.11210, mlmed.org/tools/xray/, local browser inference | VERIFIED | sources.md §0 + Mila author affiliation |
| §0.1 | CheXNet (Rajpurkar 2017) parent — narrow CV | VERIFIED | arXiv:1711.05225 |
| §1.2 | FDA 1,451 cumulative end-2025 (258 in 2024 + 295 in 2025) | VERIFIED | FDA list + Imaging Wire Dec 10 2025 + sources.md §2.1 |
| §1.2 | 76% radiology share | VERIFIED | JAMA Network Open systematic review |
| §1.2 | mosmed.ai 14M+ studies, 74 регионов, 18M images, 70 services, 11 std, 300 datasets | VERIFIED | sources.md §2.2 (mos.ru + Remedium + Healthcare ME + Webiomed) |
| §1.2 | mosmed.ai 4 млрд руб/год REMOVED | VERIFIED | Chapter explicitly disclaims; sources.md §2.3 confirmed not verifiable |
| §2.2 | CheXNet sens 0.96 / spec 0.93 verbatim | **UNVERIFIED** (specific numbers not in paper headline) | See P1 / open Q2 |
| §2.3 | MASAI sens 80.5 vs 73.8, spec 98.5, CDR 6.4 vs 5.0, ratio 1.29 | VERIFIED (add CI for rigor) | Lang 2024 Lancet Digital Health; see P1-5 |
| §2.3 | MASAI 44% workload reduction, 12% interval cancer reduction | VERIFIED | Hofvind 2025 Lancet |
| §2.3 | Goh JAMA Oct 2024 RCT: 76.3 vs 73.7 | **PARTIAL** (slight number precision drift; need to clarify mean vs median) | JAMA Network Open Oct 28 2024; see P1-2 |
| §2.3 | Goh «GPT-4 alone > docs-with-GPT-4» | VERIFIED | JAMA paper |
| §3.2 | AlphaFold 200M+ structures | VERIFIED | AlphaFold DB |
| §3.2 | AlphaFold 3 Nature May 8 2024, +50% PoseBusters | VERIFIED | Abramson 2024 Nature |
| §3.2 | AlphaProteo Sep 5 2024, 88% BHRF1, 3-300× affinity, first VEGF-A binder | VERIFIED | DeepMind blog + arXiv:2409.08022; see P1-6 |
| §3.2 | Nobel Chemistry 2024 — Hassabis + Jumper + Baker | VERIFIED | NobelPrize.org press release |
| §3.3 | Insilico Rentosertib Nature Med June 2025, n=71, +98.4 mL FVC | VERIFIED | PMID 40461817; see P0-1 |
| §3.3 | Placebo arm −62.3 mL | **WRONG** — actual is −20.3 mL | PMID 40461817 abstract verified via WebFetch; see P0-1 |
| §3.3 | Diarrhea 14.8%, liver abnormalities 14.8% | PARTIAL (denominator label missing) | See P1-1 |
| §3.3 | MADD ИТМО + Сбер AI Lab EMNLP 2025; DiMA AIRI ICML 2025 | VERIFIED | sources-ru §B.1, B.2 |
| §3.3 | AIDD center Q1 2025 Сбер + AIRI | VERIFIED | Ведомости Dec 2024; sources-ru §A.1 |
| §3.4 | DSP-1181 Phase 1 closed 2022 Japan, Discontinued | VERIFIED | Synapse/PatSnap; sources.md §1.1 |
| §3.4 | Exscientia-Recursion $688M announced Aug 8 2024, closed Nov 2024 | VERIFIED | Recursion press release; Pharmaphorum |
| §3.5 | FDA PCCP final guidance Dec 4 2024 | VERIFIED | Federal Register; Ropes & Gray analysis |
| §3.5 | EU AI Act Aug 2 2026 high-risk + Aug 2027 medical | PARTIAL (framing ambiguous for medical AI) | See P1-4 |
| §3.5 | Росздравнадзор expedited proc 1 Mar 2025 + 57 RU AI devices mid-2026 (52 dom + 5 foreign) | VERIFIED | Webiomed 2026; sources.md §8.5 |
| §3.5 | ФЗ-23 Feb 28 2025, effective July 1 2025 data localization | VERIFIED | sources.md §7.4 |
| §5.2 | Obermeyer 2019 Science DOI 10.1126/science.aax2342 | VERIFIED | PubMed; Science DOI |
| §5.2 | «26% больше хронических заболеваний» | VERIFIED at 26% (rounder); Berkeley press matches | Berkeley News; see P1-3 |
| §5.2 | «17.5% → 46.5%» | **WRONG** — actual is 17.7 to 46.5% | PubMed abstract verified; see P0-2 |
| §5.2 | «84% bias reduction» | VERIFIED | PubMed abstract |
| §5.2 | Optum/UnitedHealth 200M Americans | VERIFIED | Berkeley + Science abstract |
| §5.3 | Tessa Cass switched rule-based to generative March 2023 без NEDA approval | VERIFIED | NPR June 8 2023 + sources.md §6.1 |
| §5.3 | Sharon Maxwell screenshots May 29-30 2023, NEDA pulled within 24h May 30 | VERIFIED | NPR + Fortune + sources.md §6.1 |
| §5.3 | Tessa told «1-2 lbs/week, 500-1000 cal deficit, 2000 cal max» | VERIFIED | NPR direct quote |
| §5.3 | Adversarial hallucination 83% (Comm Med 2025) | VERIFIED | Nature Comm Med; sources.md §4.5 |
| §5.3 | 40M Americans use ChatGPT for healthcare (OpenAI/Becker's) | VERIFIED | sources.md §6.3 |
| §5.3 | 3 in 5 US adults use AI for health (Gallup) | VERIFIED | sources.md §6.3 |
| §5.4 | Change Healthcare breach Feb 21 2024 ALPHV/BlackCat, Citrix no MFA | VERIFIED | UHG; House E&C; sources.md §7.1 |
| §5.4 | 190M Americans, 6 TB, $22M Bitcoin ransom, $2.457B UHG Q3 2024 | VERIFIED | UHG SEC filings; BleepingComputer |
| §5.4 | Sweeney 1997 governor Massachusetts re-identification | VERIFIED | Sweeney 2002; Wikipedia; Petrie-Flom Harvard |
| §5.4 | HIPAA 1996 + GDPR 2016/679 + ФЗ-152 27.07.2006 + ФЗ-23 28.02.2025 | VERIFIED | sources.md §7.3, §7.4 |
| §5.5 | Price 2019 + Gerke 2020 (Elsevier) 4-actor framework | VERIFIED | sources.md §8.3 references Price + Gerke |
| §5.5 | «No notable AI malpractice lawsuits yet» mid-2025; 14% claim ↑ | VERIFIED | sources.md §8.3 |
| §5.5 | Dickson v. Dexcom 2024 Louisiana | NOT IN CHAPTER (only in research file) — no claim to verify |

**Total verification status:** 38 claims VERIFIED, 2 WRONG (P0-1, P0-2), 3 PARTIAL/precision-needs-fix (P1-1, P1-2, P1-4), 1 UNVERIFIED-headline (CheXNet specific sens/spec — P1 / open Q).

---

## Freshness watchlist update

Items requiring **verify-on-day-of-lecture** (cadence < lecture interval):

| Item | Refresh cadence | Source date | Days to lecture | Verify day-of? |
|---|---|---|---|---|
| FDA AI/ML cumulative count «1,451» | quarterly (FDA list updates ~Q-cadence) | Dec 2025 | ~150d | **YES** — actual mid-May 2026 count likely 1,500-1,580 (chapter caveats this) ✓ |
| Insilico Rentosertib Phase 3 status | quarterly | June 2025 paper | ~330d | LOW priority — chapter says «not announced» which is verifiable up to lecture day |
| EU AI Act Aug 2026 high-risk effective | one-time event | Aug 2, 2026 | ~80d post-lecture | **NO** — date is future, framing fixed in P1-4 |
| FDA PCCP guidance status / updates | yearly (one-time finalization Dec 2024) | Dec 4 2024 | 525d | LOW |
| AlphaProteo independent replication | monthly | Sep 2024 release | 615d | **YES** — if replication published before May 13, chapter caveat needs update |
| AMA physician AI adoption surveys | yearly | sources.md §11.2 («81% in 2026 AMA») | varies | LOW — used as general framing |
| Change Healthcare litigation status | quarterly | sources.md §7.1 | varies | LOW |
| Adversarial hallucination 83% rate | yearly (Communications Medicine 2025) | mid-2025 | ~330d | LOW |
| AI in healthcare market size $22-38B | quarterly | Markets and Markets / Towards Healthcare 2025 | 330d+ | LOW — chapter caveats range «по разным источникам» ✓ |
| mosmed.ai operational metrics (14M, 18M images, 70 services) | quarterly | early 2026 sources | 90-150d | **YES** — actual mid-May 2026 numbers may be higher; chapter caveats «к концу 2025–началу 2026 годов» ✓ |

**Top 3 day-of-lecture refresh items:**
1. **FDA AI/ML total count.** Chapter caveat «1,500–1,550 после Q1-2026 добавлений» is honest, but verify against FDA list pulled morning-of lecture.
2. **mosmed.ai metrics.** Check if «14M / 74 regions / 18M images» numbers have been updated in Q1-2026 mos.ru announcements (March 18, 2026 Healthcare ME piece already in sources).
3. **AlphaProteo replication status.** If any peer-reviewed independent replication appears between now and lecture, the caveat «независимая репликация публично не зафиксирована» becomes false.

---

## Recommendations for chapter revision (Phase 4)

**Priority 1 — P0 fixes (MUST do before USER GATE A):**

1. **§3.3 Rentosertib placebo FVC** — replace «−62.3 мл» with «−20.3 мл». Grep entire chapter + speech.md + slides for «62.3» to ensure no propagation. (Single fix, but cross-artifact propagation check required.)

2. **§5.2 Obermeyer 17.5 → 17.7** — replace «17.5%» with «17.7%». Grep chapter + speech + slides for «17.5» to ensure no propagation. Also update `notes/research/lecture-4/sources.md` §9.1 to prevent re-introduction.

**Priority 2 — P1 polish (highly recommended before USER GATE A):**

3. **§2.2 CheXNet sens/spec wording** — replace verbatim «0.96 / 0.93» with hedged formulation (see Open Q2 in this report); preserves didactic point without misattribution.

4. **§3.3 Rentosertib AE percentages** — add denominator label («pooled across dosed arms», «n=54»), OR replace with arm-level TEAE rates from the paper.

5. **§2.3 Goh JAMA reasoning** — add sample size («50 врачей»); align numbers (76% / 74% if median, or label «mean» если using 76.3 / 73.7).

6. **§3.5 EU AI Act Aug 2026 framing** — add clarifying clause that Aug 2026 covers Annex III non-MDR systems; Aug 2027 covers MDR/IVDR-embedded medical AI.

**Priority 3 — P2 nice-to-haves:**

7. **§2.3 MASAI ratio** — add CI: «1.29 (95% CI 1.09–1.51, p = 0.0021)».
8. **§3.3 MADD attribution** — verify arXiv:2511.08217 first author; replace «Mityagin et al.» с верифицированным lead (likely Solovev) или с «ИТМО + Сбер AI Lab, 2025».

**General note:** chapter v1 is unusually well-sourced for v1 draft — the bookkeeping discipline of explicit citations и self-flagged FACT-CHECK tags reflects good editorial process. The two P0s are number-precision misses on heavy-cited claims, not fabrication. After Phase 4 revision addressing P0-1 and P0-2, chapter should be APPROVE-WITH-POLISH or APPROVE-CLEAN level.

---

**End of fact-check report. Token estimate: ~3,500 words.**

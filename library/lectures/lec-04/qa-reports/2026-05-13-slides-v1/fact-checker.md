# Fact-Check — Slides v1 — Лекция 4 (AI в медицине и фармацевтике)

**Date:** 2026-05-13
**Phase:** 7 (slides fact-check pass)
**Artifact:** `library/lectures/lec-04/rendered/snapshots/sNN.png` + `library/lectures/lec-04/slides/sNN-*.md`
**Baseline:** Chapter v2 (fact-checked Phase 3, commit `5c4b06c`) + `notes/research/lecture-4/sources.md` + `sources-ru-drug-discovery.md`
**Verdict:** **APPROVE-WITH-POLISH**

## Severity counts
- P0 (false fact / broken citation / direction inversion): **0**
- P1 (numeric inconsistency / schema placement / missing attribution): **3**
- P2 (cite format / minor polish): **4**

Все ключевые цифры, на которые брифинг указал в Specific claims to verify (s04 FDA, s08 EU AI Act, s10 CheXNet, s11 MASAI+Goh+Liu, s12 mosmed.ai operational, s17a Rentosertib, s17b DSP-1181, s18 PCCP+EU AI Act, s21 Obermeyer, s22 Tessa+adversarial+40M, s23 Change Healthcare+ALPHV, s24 4-actor) — **верифицированы против sources.md + chapter**. Два Phase 3 P0 fixes (Rentosertib `−20.3` mL placebo, Obermeyer `17.7%`) корректно пропагированы в slides. Slide s12 корректно **исключает** unverified «4 млрд руб/год» — operational metrics only. Найдены 3 P1 issues (один — numeric inconsistency Bayes на s10; один — schema quadrant misplacement на s24; один — date attribution для NEDA Tessa generative switch).

---

## Claim verification matrix

| Slide | Claim (on PNG or in notes) | Source check | Status |
|---|---|---|---|
| **s04** | «1 451 FDA-устройств кумулятивно end-2025» (PNG + notes) | sources.md §2.1 «1,451 cumulative authorized devices через конец 2025» | ✓ VERIFIED |
| s04 | «258 новых в 2024 + 295 новых в 2025» (notes) | sources.md §2.1 «258 AI devices authorized in 2024; 295 new authorizations in 2025» | ✓ VERIFIED |
| s04 | «76% — радиология (CV-based)» (PNG caption) | sources.md §2.1 «Radiology = 76% всех authorizations (1,104 devices)» | ✓ VERIFIED |
| s04 | mosmed.ai info-card: «14 млн+ исследований / 74 регион / 2 000+ медорг / 18 млн+ изображений / 70 AI-сервисов / 11 нац. стандартов» (PNG) | sources.md §2.2 — all six values verified word-for-word | ✓ VERIFIED |
| s04 | mosmed.ai «федеральный MosMedAI (май 2024)» (PNG caption) | sources.md §2.2 «в мае 2024 — federal launch как «MosMedAI» nationwide service» | ✓ VERIFIED |
| **s07** | «За 10 лет — от ~6 до 1 451 AI-устройств» (PNG title) | sources.md §2.1 «В 2015 — ~6 AI/ML-устройств; 1,451 cumulative end-2025» | ✓ VERIFIED |
| s07 | «76% — радиология» (PNG right-card) | sources.md §2.1 verified | ✓ VERIFIED |
| s07 | «+295 новых в 2025» (PNG right-card) | sources.md §2.1 verified | ✓ VERIFIED (freshness watchlist — partial-year as of late-2025) |
| s07 | Chart axis labels 2015/2018/2020/2022/2024/2025 — 2022 bar shows cumulative ~400 (visually estimated) | sources.md «2023 alone — 221 devices»; missing 2023 label but bar height plausible for end-2022 cumulative ~520. Approximate visualization, not flagged as error. | ⚠️ P2 — label 2023 не показан, но эстетический выбор |
| **s08** | «EU AI Act — 2 августа 2026 deadline для high-risk» (speaker notes) | sources.md §8.2 «August 2026 — high-risk AI systems rules» | ✓ VERIFIED |
| s08 | «Через 2.5 мес после нашей лекции» (notes; consistent с lecture date May 2026) | 2 авг 2026 − 13 май 2026 = ~2.5 месяца | ✓ VERIFIED arithmetic |
| **s10** | «CheXNet: sens 0.96 · spec 0.93» (PNG gold-info-card) | sources.md §1.1+§2.5 cross-ref (CheXNet paper). Chapter §2.2 says «sens ≈ 0.94–0.96, spec ≈ 0.89–0.93» — slide picks upper-bound | ⚠️ P1 NUMERIC INCONSISTENCY (см. ниже) |
| s10 | «PPV ~8% при prev 1% / ~78% при prev 30%» (PNG gold-info-card) | Chapter §2.2 says PPV ~8% computed with sens 0.94, spec 0.89 (lower bound). With slide's sens 0.96 / spec 0.93 → recomputed PPV = **~12% (prev 1%) / ~85% (prev 30%)** | ⚠️ P1 — числа inconsistent с stated sens/spec |
| **s11** | Liu et al. 2019 — «pooled sens AI 0.87 · врач 0.85» (PNG row 1) | sources.md §11 ref list + chapter §2.3 «Pooled sensitivity AI — 87%, клиницистов — 85%» | ✓ VERIFIED |
| s11 | Liu 2019 — «meta-analysis 14 prospective» (PNG row 1) | Chapter §2.3 «14 проспективных работ» | ✓ VERIFIED |
| s11 | MASAI — «sens 80.5% (AI) vs 73.8% (стандарт)» (PNG row 2 + speaker notes) | sources.md §2.5 «Sensitivity 80.5% (AI) vs 73.8% (standard) at same specificity 98.5%» | ✓ VERIFIED |
| s11 | MASAI — «workload −44%» (PNG row 2) | sources.md §2.5 «44% reduction in radiologist workload» | ✓ VERIFIED |
| s11 | MASAI — «interval cancer −12%» (PNG row 2) | sources.md §2.5 «12% reduction in interval breast cancers» | ✓ VERIFIED |
| s11 | MASAI — «n > 100 000 (Sweden)» (PNG row 2) | sources.md §2.5 «>100,000 women (Apr 2021 – Dec 2022)» | ✓ VERIFIED |
| s11 | Goh et al. 2024 — «GPT-4 alone 76.3% · врач+GPT-4 73.7% (p=0.60)» (PNG row 3) | sources.md §4.3 «Median diagnostic reasoning score 76.3% (GPT-4) vs 73.7% (conventional)... p=0.60» (note: slide invertирует «GPT-4 alone» vs «врач+GPT-4» — см. ниже) | ⚠️ P1 — see «direction nuance» note |
| s11 | Goh — «n=50 врачей» (PNG row 3, speaker notes) | Chapter §2.3 «RCT с 50 врачами»; sources.md §4.3 describes the RCT — n=50 widely reported для JAMA Net Open 2024 study | ✓ VERIFIED |
| **s12** | «14 млн+ исследований / 74 регион / 2 000+ медорг / 18 млн+ изображений / 70 AI-сервисов / 11 нац. стандартов» (PNG 6 info-cards) | sources.md §2.2 — все 6 значений verified word-for-word | ✓ VERIFIED |
| s12 | **«NO 4 млрд руб/год»** — slide correctly omits | sources.md §2.3 «UNCERTAIN; не использовать» — корректно исключено | ✓ VERIFIED — корректно исключено |
| s12 | «300+ datasets» (PNG bottom-card) | sources.md §2.2 «300+ reference datasets» | ✓ VERIFIED |
| s12 | «43 области» (PNG AI-анализ box) | sources.md §2.2 «~70 AI services across 43 clinical areas» | ✓ VERIFIED |
| s12 | «федеральный MosMedAI (май 2024)» (notes) | sources.md §2.2 verified | ✓ VERIFIED |
| s12 | «Federated platform: Сбер AI Lab, Care Mentor AI, Третье Мнение, Webiomed» (PNG bottom caption) | Sources confirm всех 4 vendors; integration pattern verified в §10.2-10.7 | ✓ VERIFIED |
| **s17a** | «+98.4 mL FVC vs −20.3 mL placebo» (PNG result-box) | sources.md §1.3 «+98.4 mL FVC (95% CI: 10.9–185.9) vs −20.3 mL placebo (95% CI: −116.1–75.6)» — Phase 3 P0 fix correctly propagated | ✓ VERIFIED |
| s17a | «Δ ~118 mL» (PNG result-box) | sources.md §1.3 «treatment effect ~118 mL» | ✓ VERIFIED |
| s17a | «60 mg QD» (PNG result-box) | sources.md §1.3 «Доза 60 mg QD (n=24)» | ✓ VERIFIED |
| s17a | «n=71» (PNG event-3 box) | sources.md §1.3 «n=71 patients across 21 China sites» | ✓ VERIFIED |
| s17a | «21 China sites» (PNG event-3 box) | sources.md §1.3 verified | ✓ VERIFIED |
| s17a | «PMID 40461817» (PNG badge) | sources.md §1.3 «PubMed: A generative AI-discovered TNIK inhibitor for IPF: Phase 2a trial» — PMID 40461817 verified | ✓ VERIFIED |
| s17a | «Nature Medicine, июнь 2025» (PNG header) | sources.md §1.3 «Nature Medicine, June 2025» | ✓ VERIFIED |
| s17a | «~18 мес vs 4–5 лет» (PNG event-1 box) | sources.md §1.9 «target ID → preclinical candidate в <18 месяцев» (Insilico self-reported) — slide корректно flagged в speaker notes как «self-reported» | ✓ VERIFIED w/ caveat |
| s17a | AE 14.8% diarrhea & abnormal liver (speaker notes) | sources.md §1.3 «diarrhea 14.8%, abnormal liver function 14.8%» | ✓ VERIFIED |
| s17a | TEAE 83.3% vs 70.6% (brief required — NOT on PNG nor in notes) | sources.md §1.3 «TEAE rate 83.3% (60 mg QD) vs 70.6% (placebo)» — omission OK (not asserted on slide → no claim to verify) | ⚪ Not asserted (intentional omission) |
| **s17b** | «Phase 1 discontinued 2022» (PNG event-2 box) | sources.md §1.1 «Phase 1 в Японии stopped 2022» | ✓ VERIFIED |
| s17b | «OCD · Japan» (PNG event-1 caption) | sources.md §1.1 «обсессивно-компульсивное расстройство... Sumitomo Dainippon, январь 2020» | ✓ VERIFIED |
| s17b | «12 мес vs 4–5 лет» (PNG bottom info) | sources.md §1.1 + §1.9 — verified | ✓ VERIFIED |
| s17b | «Discontinued» status May 2026 (PNG event-3) | sources.md §1.1 «Текущий R&D статус — Discontinued» | ✓ VERIFIED |
| s17b | «Recursion + Exscientia merger Aug 2024» (PNG bottom caption) | sources.md §1.2 «8 августа 2024 объявили о слиянии» | ✓ VERIFIED |
| **s18** | «FDA PCCP final 4 декабря 2024» (PNG col-1) | sources.md §8.1 «December 4, 2024: FINAL guidance — Marketing Submission Recommendations for PCCP» | ✓ VERIFIED |
| s18 | «EU AI Act — 2 авг 2026 (Annex III high-risk non-MDR)» (PNG col-2) | sources.md §8.2 «August 2026 — high-risk AI systems rules» | ✓ VERIFIED |
| s18 | «EU AI Act — 2 авг 2027 (MDR full compliance)» (PNG col-2) | sources.md §8.2 «August 2027 — full compliance для AI in regulated products» | ✓ VERIFIED |
| s18 | «57 AI-медизделий (52 RF + 5 foreign) к mid-2026» (PNG col-3) | sources.md §8.5 «per Webiomed updated data — 57 to mid-2026 (52 Russian + 5 foreign)» | ✓ VERIFIED |
| s18 | «Expedited 1 марта 2025 (ПП РФ № 1684)» (PNG col-3) | sources.md §8.5 «С 1 марта 2025 — new государственная регистрация rules; expedited procedure» | ✓ VERIFIED |
| s18 | «Webiomed, 3 апреля 2020» (PNG col-3) | sources.md §10.2 «Первый AI software официально зарегистрированный 3 апреля 2020» | ✓ VERIFIED |
| s18 | «ФЗ-23, 1 июля 2025» (PNG col-3 data-localization) | sources.md §7.4 «С 1 июля 2025 (Federal Law N 23-ФЗ, 28 февраля 2025): personal data... cannot be processed/stored on databases located outside Russia» | ✓ VERIFIED |
| **s21** | «Commercial AI для 200M Americans» (PNG subtitle) | sources.md §9.1 + chapter §5.2 «применяемый ежегодно для примерно двухсот миллионов американцев» (Obermeyer 2019) | ✓ VERIFIED |
| s21 | «+26% больше хронических заболеваний» (PNG left-card) | sources.md §9.1 «у них было на двадцать шесть процентов больше хронических заболеваний» (chapter §5.2 cross-ref); Obermeyer 2019 Science verbatim | ✓ VERIFIED |
| s21 | «17.7% → 46.5%» (PNG right-card) | sources.md §9.1 «from 17.7 to 46.5%» Science abstract verbatim — Phase 3 P0 fix correctly propagated | ✓ VERIFIED |
| s21 | «−84% bias» (PNG right-card sub-caption) | sources.md §9.1 «Retraining with proxy + chronic conditions reduced disparity by 84%» | ✓ VERIFIED |
| s21 | «Black: −$1 800/y (access disparities)» (PNG mechanism-box) | sources.md §9.1 «Black patients spent $1,800/year less than equally-sick white patients» | ✓ VERIFIED |
| s21 | «Science 366, 447 (2019); DOI 10.1126/science.aax2342» (PNG footer) | sources.md §9.1 «Science Vol 366 (Oct 2019)»; DOI verified | ✓ VERIFIED |
| **s22** | «May 2023 NEDA Tessa scandal» (PNG card-1) | sources.md §6.1 — verified | ✓ VERIFIED |
| s22 | «30 мая 2023: Maxwell screenshots → suspended 24h» (PNG card-1 timeline) | sources.md §6.1 «NEDA pulled Tessa May 30, 2023» | ✓ VERIFIED |
| s22 | «Март 2023: Cass → generative БЕЗ NEDA approval» (PNG card-1 timeline) | sources.md §6.1 says «Cass changed Tessa без NEDA's approval», но **точная дата March 2023 в sources.md не указана** — обычно цитируется «в начале 2023», иногда «February 2023» (per NPR retrospectives); March 2023 is plausible но не in sources | ⚠️ **P1 — Date not explicitly in sources** (см. ниже) |
| s22 | «6 ведущих LLM, 300 clinical vignettes» (PNG card-2) | sources.md §4.5 «6 leading LLMs on 300 clinical vignettes» | ✓ VERIFIED |
| s22 | «83% halluc. rate» (PNG card-2) | sources.md §4.5 «models repeat/elaborate on fake error in up to 83% of cases» | ✓ VERIFIED |
| s22 | «Communications Medicine 2025 (Nature)» (PNG card-2 attribution) | sources.md §4.5 «Multi-model assurance LLMs adversarial hallucination» published в Communications Medicine (Nature portfolio) 2025 | ✓ VERIFIED |
| s22 | «Mitigation prompt halves but ≠ zero» (PNG card-2 bullet) | sources.md §4.5 «Mitigation prompt halves rate but not eliminates» | ✓ VERIFIED |
| s22 | «~40M Americans use ChatGPT для health past 3 months» (PNG card-3) | sources.md §6.3 «40 million Americans use ChatGPT for healthcare questions» (но «past 3 months» — это OpenAI/Gallup survey wording, может быть не строго exact match — допустимая paraphrase) | ✓ VERIFIED (paraphrase OK) |
| s22 | «3 из 5 US adults» (PNG card-3) | sources.md §6.3 «3 in 5 US adults used AI tools for health past 3 months» | ✓ VERIFIED |
| s22 | «OpenAI / Gallup 2025» (PNG card-3 attribution) | sources.md §6.3 (Gallup AI healthcare survey verified) | ✓ VERIFIED |
| **s23** | «190M Americans affected (~57% US pop)» (PNG info-card-1) | sources.md §7.1 «190 million Americans PHI stolen»; 190M / ~334M US pop = ~57% | ✓ VERIFIED |
| s23 | «$2.457B recovery cost UHG Q3 2024» (PNG info-card-2 gold) | sources.md §7.1 «$2.457 billion total cost (UHG Q3 2024)» | ✓ VERIFIED |
| s23 | «6 TB exfiltrated» (PNG info-card-3) | sources.md §7.1 «6 TB of data exfiltrated» | ✓ VERIFIED |
| s23 | «$22M ALPHV/BlackCat ransom» (PNG info-card-5) | sources.md §7.1 «$22M Bitcoin ransom paid» + «ALPHV BlackCat ransomware group» | ✓ VERIFIED |
| s23 | «21 февраля 2024» attack date (speaker notes) | sources.md §7.1 «Attack date 21 февраля 2024» | ✓ VERIFIED |
| s23 | «multi-week disruption» (PNG info-card-4) | sources.md §7.1 — implied; multiple sources confirm weeks of disruption to US claims processing | ✓ VERIFIED |
| s23 | «Sweeney 2002 re-identification governor MA» (PNG bridge-card) | sources.md §7.3 «1997: Sweeney re-identified Governor of Massachusetts medical records» — note **1997 act, 2002 publication of k-anonymity formalisation** | ⚠️ P2 — Slide formulation «Sweeney 2002» refers to publication date of formal k-anonymity paper; the actual re-identification incident was 1997. Acceptable shorthand but ambiguous. |
| s23 | «ФЗ-152 + ФЗ-23 (1 июля 2025)» (PNG regulation chip) | sources.md §7.4 verified | ✓ VERIFIED |
| s23 | «GDPR (EU, 2016/679)» (PNG regulation chip) | Public knowledge — GDPR is EU regulation 2016/679, adopted 2016, applied May 2018 | ✓ VERIFIED |
| s23 | «HIPAA (US, 1996)» (PNG regulation chip) | Public knowledge — HIPAA enacted 1996 | ✓ VERIFIED |
| **s24** | Caption «Price 2019, Gerke 2020» (PNG footer) | sources.md §8.5 cross-ref via «4-actor framework Price 2019, Stanford Technology Law Review; Gerke et al. 2020, Artificial Intelligence in Healthcare, Elsevier» (chapter §5.5) | ✓ VERIFIED attribution |
| s24 | Quadrant axis labels: «liability low/high (Y)» × «technical control low/high (X)» | Speaker notes describe 4 actors with combination scheme: Врач (high control + high liability), Operator (mid+mid), Vendor (high control + low-mid liability), Regulator (low control + high oversight). | ⚠️ **P1 — Vendor placement** (см. ниже) |
| s24 | Central line: «Врач ставит диагноз. AI подсказывает. Final clinical responsibility — undivided» | sources.md §8.3 + §8.4 «доктор остаётся юридически ответственным; final clinical responsibility undivided» | ✓ VERIFIED principle |

---

## P0 issues

**Нет.** Все ключевые цифры из брифинга verified; оба Phase 3 P0 fixes (Rentosertib placebo −20.3 mL, Obermeyer 17.7%) корректно пропагированы в slides.

---

## P1 issues

### P1-1 — s10 numeric inconsistency: CheXNet sens/spec vs PPV outputs не сходятся

**Quote on PNG:** «CheXNet (Rajpurkar 2017): sens 0.96 · spec 0.93 → PPV ~8% при prev 1% (skрининг) · ~78% при prev 30% (госпиталь)».

**Issue:** С указанными sens=0.96 и spec=0.93 байесовская формула даёт:
- PPV(prev 1%) = 0.96 × 0.01 / (0.96 × 0.01 + 0.07 × 0.99) = 0.0096 / 0.0789 = **~12.2%**, не ~8%.
- PPV(prev 30%) = 0.96 × 0.3 / (0.96 × 0.3 + 0.07 × 0.7) = 0.288 / 0.337 = **~85.4%**, не ~78%.

Числа «~8%» и «~78%» в chapter §2.2 рассчитаны с **sens=0.94, spec=0.89** (нижняя граница диапазона CheXNet). Slide picked headline-cifры sens/spec из upper-bound, но keep PPV outputs из lower-bound. Это nontrivial illustrative-error: интуиция «sens/spec высокие → PPV всё равно низкий при низкой prevalence» сохраняется, но конкретные числа на слайде self-inconsistent.

**Speaker notes** (s10-...md): «sens 0.94-0.96 и spec 0.89-0.93. В больничной выборке с prevalence 30 процентов PPV получается около семидесяти восьми процентов» — использует **lower-end sens/spec** для расчёта PPV. Согласовано с chapter, но slide visual highlight «0.96/0.93» не согласован.

**Severity:** P1 (numeric inconsistency — not a false fact about CheXNet itself, but a math error на учебном слайде про Bayes intuition).

**Recommendation (один из двух):**
- (A) Изменить headline sens/spec на «sens 0.94 · spec 0.89» (lower-bound, согласовано с chapter и PPV-числами); или
- (B) Сохранить «sens 0.96 · spec 0.93», но обновить PPV outputs на «~12%» (prev 1%) и «~85%» (prev 30%).

Option A более pedagogically consistent с chapter; option B preserves «headline» CheXNet metric. Either acceptable; current state mixes two.

### P1-2 — s24 4-actor quadrant: Vendor mispositioned относительно speaker notes

**Quote (PNG):** 2×2 quadrant. Y-axis = «LIABILITY low ↓ high ↑»; X-axis = «◄ low control · TECHNICAL CONTROL · high control ►». Cards positioned:
- Top-left: Regulator (high liability, low control)
- Top-right: Врач (high liability, high control)
- Bottom-left: Vendor (low liability, low control)
- Bottom-right: Operator (low liability, high control)

**Issue:** Speaker notes (s24-4actor-responsibility.md, lines 41-43) explicitly state: «AI-vendor — **высокий control**, низкая-средняя liability. Дизайнит модель, делает safety claims... Если model design имеет defect — vendor несёт liability по product liability.» По этому описанию vendor должен быть **bottom-RIGHT** (high control + low-mid liability), а operator — **center / bottom-middle** (mid control + mid liability). Sources.md §8.4 + chapter §5.5 also describe vendor как «high technical control over model design» — это intuitively верно (vendor написал код, поставщик и есть архитектор).

Placement Vendor в bottom-LEFT и Operator в bottom-RIGHT — **обратная пара**: faktично the slide implies vendor has LESS technical control than operator, which contradicts the speaker notes' own framing.

**Severity:** P1 (schema/diagram misplacement — distortive for the lesson «who has what control»).

**Recommendation:** Swap Vendor and Operator positions in the quadrant (Vendor → bottom-right, Operator → bottom-left), OR re-label X-axis so что existing placement makes sense (но тогда axis labels должны быть rewritten — менее clean fix).

### P1-3 — s22 NEDA Tessa generative switch date «Март 2023» не в sources.md

**Quote (PNG s22 card-1 timeline):** «Март 2023: Cass → generative БЕЗ NEDA approval».

**Issue:** sources.md §6.1 detail: «Cass (developer) changed Tessa без NEDA's approval to use generative AI / Q&A feature» — но **точная дата generative switch не зафиксирована в sources**. Public reporting (NPR June 2023, AI Incident DB 545) puts Maxwell's screenshots at May 2023; the actual switch could have happened any time в Q1–Q2 2023. Chapter §5.3 line 478 says «В марте 2023 года Cass самовольно сменила» — это chapter assertion, not from a sourced citation.

**Verification attempt:** Open-source reporting on Tessa scandal typically cites either «early 2023» or «February-March 2023» для switch date; the exact month is fluid in secondary sources. The earliest reports of altered Tessa behavior (Maxwell's tested interactions) span late April — early May 2023. «Март 2023» is consistent with the timeline but not strictly verifiable from sources.md.

**Severity:** P1 (citation gap — слайд claim not directly supported by sources.md; may be derived from chapter writer's general knowledge, not from cited reference).

**Recommendation:** Soften to «начало 2023 / Q1-Q2 2023» (no specific month claim), OR find primary source for March 2023 specifically (e.g., NEDA internal comms reports, Vice/Wired investigative pieces). If primary source found — add explicit citation to sources.md and keep slide claim. If not — soften the assertion.

---

## P2 issues

### P2-1 — s07 chart missing 2023 label
Chart x-axis labels: 2015, 2018, 2020, 2022, 2024, 2025 — but speaker notes emphasize «в 2023 одобрено около 221 нового устройства». Acceptable visualization choice (showing major pivots), но «pivot 2022-2024 acceleration» framing slightly misleading без 2023 marker visible.

**Recommendation:** Optional — add 2023 label (with ~221 new) для educational completeness. Low priority.

### P2-2 — s11 Goh «GPT-4 alone 76.3% vs врач+GPT-4 73.7%» framing nuance
Slide shows: «GPT-4 alone 76.3% · врач+GPT-4 73.7% (p=0.60)». Original Goh JAMA Net Open 2024 RCT was «doctor+GPT-4 vs doctor+conventional» (76.3% vs 73.7%, p=0.60) — это **primary comparison**. «GPT-4 alone scored higher» — это **secondary side-test** finding (sources.md §4.3 «Surprising finding: GPT-4 alone scored higher than doctors-with-GPT-4 in side test»). Speaker notes (s11 line 43) корректно объясняют: «Сюрприз: GPT-4 alone давал более высокий score, чем доктор-плюс-GPT-4» — но slide PNG row 3 «GPT-4 alone 76.3% · врач+GPT-4 73.7%» reads как if «GPT-4 alone» is the primary comparison row.

**Это не false claim**, но framing slightly misleading. Speaker может объяснить, но student reading silently увидит wrong interpretation.

**Recommendation:** Optional rephrase to «врач+GPT-4 76.3% · врач только 73.7% (p=0.60); side-test: GPT-4 alone > обоих». Low priority — speaker notes correctly carry the nuance.

### P2-3 — s23 «Sweeney 2002» ambiguous (act 1997 vs publication 2002)
PNG bridge-card: «Анонимизация ≠ anonymity (Sweeney 2002 re-identification governor MA)». Actual re-identification of Governor Weld was 1997 (Sweeney's MIT thesis era); k-anonymity formalisation published 2002 (Sweeney, "k-Anonymity: A Model for Protecting Privacy"). Slide formulation conflates act-date with publication-date.

**Recommendation:** Optional — either «(Sweeney 1997 re-id; k-anonymity 2002)» or «(Sweeney's work, 1997-2002)». Low priority — academic shorthand accepted in many texts.

### P2-4 — s17a «PMID 40461817» badge
PNG header badge says «PMID 40461817». PMID format usually rendered «PMID: 40461817». Cosmetic. Verified — that's the actual PubMed ID for the Insilico Rentosertib paper (sources.md §1.3).

**Recommendation:** Optional formatting fix only.

---

## Russian-source attribution check

| Source | Slide(s) | Attribution adequacy |
|---|---|---|
| `mosmed.ai / mos.ru / Remedium` | s04, s12 | ✓ Adequate — multiple sources cited in footer |
| `Webiomed` (RU AI registered devices) | s18 | ✓ Adequate — corporate name + date |
| `Сбер AI Lab / Care Mentor AI / Третье Мнение` | s12 federated platform | ⚠️ Listed but without specific source URL on slide. Adequately covered by mosmed.ai overarching attribution. |
| `Insilico Medicine` (Hong Kong company с РФ corporate trace) | s17a | ✓ Adequate — Nature Medicine citation, no false «российская компания» claim. |
| `АНО Цифровая экономика / Gartner / ВЦИОМ` | (none on slides) | N/A — not used. |
| `ALPHV/BlackCat «русскоязычная группа»` | s23 (in speaker notes, not on PNG) | ✓ Adequate — chapter §5.4 frames nuance carefully; speaker notes carry «русскоязычная группа, по данным правоохранительных органов». No direct anti-RU framing on visible PNG. |

---

## Cross-artifact consistency (slides ↔ chapter)

| Claim | Chapter | Slides | Consistent? |
|---|---|---|---|
| 1 451 cumulative FDA end-2025 | §1.2, §6.1 (takeaway) | s04, s07 | ✓ |
| 14M+ исследований mosmed.ai | §1.2, §2.4 | s04, s08, s12 | ✓ |
| MASAI 80.5% vs 73.8% | §2.3 | s11 | ✓ |
| Goh 76% / 74% / p=0.60 | §2.3 «76% vs 74%» (rounded) | s11 «76.3% vs 73.7%» (precise) | ✓ (different precision — both correct) |
| Rentosertib +98.4 mL vs −20.3 mL | §3.3 (Phase 3 P0 fix) | s17a | ✓ |
| DSP-1181 2022 discontinued | §3.4 | s17b | ✓ |
| FDA PCCP 4 декабря 2024 | §3.5 | s18 | ✓ |
| EU AI Act 2 авг 2026 / 2027 | §3.5, §1 intro | s08, s18 | ✓ |
| Obermeyer 17.7 → 46.5%, 84% reduction, 26% chronic illness gap | §5.2 (Phase 3 P0 fix) | s21 | ✓ |
| NEDA Tessa scandal | §5.3 «март 2023» | s22 «Март 2023» | ⚠️ (P1-3 — chapter and slide both assert same date; neither cited in sources.md) |
| Change Healthcare 190M / $2.457B / ALPHV-BlackCat | §5.4 | s23 | ✓ |
| 4-actor framework Price 2019 + Gerke 2020 | §5.5 | s24 | ✓ attribution (quadrant placement issue is P1-2) |
| CheXNet sens/spec/PPV | §2.2 (sens 0.94, spec 0.89, PPV ~8%) | s10 (sens 0.96, spec 0.93, PPV ~8%) | ⚠️ (P1-1) |

---

## Freshness watchlist updates

| Claim | Source date | Refresh cadence | Days delta (to lecture 2026-05-13) | Verify-on-day-of-lecture? |
|---|---|---|---|---|
| FDA cumulative 1 451 (end-2025) | Dec 2025 | quarterly | ~135 days | **YES** — verify FDA list current count |
| FDA «295 new в 2025» | end-2025 | quarterly | ~135 days | YES — partial-year may have shifted |
| Aidoc «1,600+ medical centers; FDA foundation model Jan 2026» | Jan 2026 | quarterly | ~100 days | (not visualized in slides; chapter ref only) |
| MASAI Lancet 2025 interval cancer | 2025 | yearly+ | ~365 days | NO |
| Goh Nature Medicine 2025 (management reasoning) | 2025 | yearly+ | ~365 days | NO |
| mosmed.ai 14M+ / 74 regions | mar 2026 | quarterly | ~60 days | YES — federal expansion ongoing |
| Insilico Rentosertib Nature Medicine June 2025 | jun 2025 | yearly+ | ~330 days | NO — peer-reviewed permanent |
| Change Healthcare $2.457B (UHG Q3 2024) | Q3 2024 | yearly+ | ~600 days | NO — historical |
| EU AI Act 2 авг 2026 deadline | regulatory fixed | n/a | ~80 days forward | NO — fixed date |
| FDA PCCP final 4 дек 2024 | regulatory fixed | n/a | ~525 days back | NO — fixed date |
| Webiomed 57 registered AI medical devices | mid-2026 | quarterly | ~30 days | **YES** — likely changed |
| AMA «81% physicians в 2026» (background, not on visible slides) | 2026 | quarterly | varies | flag for chapter context refresh |
| 40M Americans ChatGPT для health | OpenAI/Gallup 2024-2025 | quarterly | varies | maybe refresh |
| Adversarial hallucination 83% (Communications Medicine 2025) | 2025 | yearly+ | ~365 days | NO — peer-reviewed |

**Top-3 items needing day-of-lecture refresh:**
1. **FDA cumulative count** (s04, s07): «1 451 end-2025» — check FDA AI/ML list on May 12-13, 2026 для current cumulative count. If grown materially (>50 new since end-2025), update both slides + speech.
2. **Webiomed 57 registered** (s18): RU registration list updates monthly; verify count на день лекции.
3. **mosmed.ai operational metrics** (s04, s08, s12): «14M+ / 74 regions / 18M+» — verify against mosmed.ai dashboard, mos.ru news, Remedium. Federal expansion может означать дополнительные регионы / новые сервисы за 60 дней с marzo.

---

## Top recommendations (priority order)

1. **(P1-1) Fix s10 PPV / sens-spec inconsistency.** Either lower sens/spec на slide visual to 0.94/0.89 (chapter-consistent) OR update PPV outputs на ~12% / ~85% (slide-consistent). Recommended: option A (lower numbers, chapter sync).
2. **(P1-2) Fix s24 quadrant: swap Vendor ↔ Operator positions** (Vendor → high-control / low-mid liability = bottom-right; Operator → mid-control = bottom-left or center). Critical for «who has what technical control» learning point.
3. **(P1-3) s22 Tessa generative switch date «Март 2023»:** either find primary source citation and add to sources.md, or soften slide to «начало 2023». Same fix should propagate to chapter line 478.
4. (P2-1) Optional — add 2023 label to s07 bar chart for completeness (~221 new в 2023).
5. (P2-2) Optional — s11 Goh row clarify primary vs secondary comparison: «врач+GPT-4 76.3% · врач только 73.7% (p=0.60)» с side-test «GPT-4 alone > обоих» как badge.
6. (P2-3) s23 «Sweeney 2002» — optional clarify к «(Sweeney's work, 1997 re-id / 2002 k-anonymity paper)».
7. **(Freshness — day-of-lecture)** Re-verify FDA cumulative count + Webiomed registration count + mosmed.ai operational dashboard ≤24h before lecture delivery.

---

## Verification methodology used

1. **Sources baseline:** Read `notes/research/lecture-4/sources.md` (460 lines) + `sources-ru-drug-discovery.md` (183 lines). Cross-checked Phase 3 fact-checker fixes (commit 5c4b06c) для Rentosertib placebo −20.3 mL and Obermeyer 17.7% propagation.
2. **PNG vision:** Read 13 critical PNGs (s04, s07, s08, s10, s11, s12, s17a, s17b, s18, s21, s22, s23, s24) using Claude vision. Extracted all numeric and date claims visible на slide.
3. **Speaker notes:** Read full markdown for 12 slides — extracted claims, attribution, cross-references.
4. **Chapter cross-check:** Grepped chapter.md для each headline claim. Verified Phase 3 P0 fixes (Rentosertib, Obermeyer) propagated correctly to slides.
5. **Math verification:** Independently computed Bayes PPV для s10's stated sens/spec — found inconsistency (P1-1).
6. **Quadrant logic check:** Cross-checked s24 PNG card positions against speaker notes' verbal description of control/liability levels per actor — found Vendor ↔ Operator mispositioned (P1-2).
7. **Date attribution audit:** Verified every date and number on slides against sources.md sections. NEDA Tessa generative-switch month is the only one where slide+chapter claim a date (March 2023) not directly anchored в sources (P1-3).

---

**Final Verdict: APPROVE-WITH-POLISH.** Все ключевые цифры брифинга verified, оба Phase 3 P0 fixes корректно пропагированы, slides показывают clean factual hygiene. Три P1 issues являются полишингом, не критическими ошибками: один — Bayes math inconsistency на учебном слайде (P1-1, easy fix), один — quadrant placement (P1-2, swap two cards), один — date citation gap (P1-3, soften or anchor). Никаких false facts, никаких broken citations, никаких direction inversions, никаких curriculum hallucinations. Slides готовы к Phase 8 после трёх P1 fixes + (опционально) day-of-lecture freshness refresh для FDA/Webiomed/mosmed counts.

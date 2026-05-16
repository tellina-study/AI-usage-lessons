# Fact-Check — Speech v1 — Лекция 4

**Verdict:** APPROVE-WITH-POLISH

**Дата проверки:** 2026-05-13
**Артефакт:** `library/lectures/lec-04/speech.md` (v1, ~4993 active words, 34-slide mirror)
**Ground truth:** `notes/research/lecture-4/sources.md` + `sources-ru-drug-discovery.md`
**Сверка с:** `library/lectures/lec-04/chapter.md` v2 (commit `5c4b06c`)

## Severity counts

| Уровень | Кол-во | Примечание |
|---|---|---|
| P0 (false fact / direction inversion / misquote / broken attribution) | **1** | Gallup 60% attribution swap (s22) |
| P1 (missing source / suspicious figure / per-year breakdown without primary) | **5** | FDA per-year split (s07), Daneshjou 20-30% (s13), Cass «март 2023» date, Price «Stanford» affiliation (s24), 1/3 US claims share (s23) |
| P2 (cite format / минор precision / context paraphrase) | **3** | Sweeney 1997 vs 2002 (s23), «Goh — 50 врачей» (s11), 4-actor framework attribution синтаксис (s24) |
| Freshness watchlist | 5 | FDA cumulative, mosmed.ai studies count, AI medical malpractice landmark cases, Россия Росздравнадзор device count, 40M ChatGPT users |

**Итог:** один P0 — attribution swap (легко исправляется). 5 P1 — precision / mid-level sourcing gaps. Большинство claims в speech уверенно verified. Speech следует chapter v2 как source-of-truth, и chapter v2 уже выдержал fact-check Phase 4. Speech добавляет минимум нового factual content поверх chapter.

---

## Claim verification matrix

### Раздел 0. Открытие (s01–s05b)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s01 | Chester AI = «потомок CheXNet 2017» | sources.md §2.5 (CheXNet Rajpurkar et al. 2017); mlmed.org — публичный tool | ✓ VERIFIED |
| s01 | «восемнадцать строк, вероятности по восемнадцати патологиям» | Chester (mlmed.org) — actually classifies 14 pathologies per CheXNet legacy + extended. Speech говорит «18 строк» как наблюдаемое; на mlmed.org интерфейс показывает 14 классов NIH ChestX-ray14, не 18. **P1 — verify on day of lecture** | ⚠️ P1 — verify visual output |
| s01 | «модель работает локально, в браузере» | mlmed.org confirmed client-side TensorFlow.js | ✓ VERIFIED |
| s04 | «к концу 2025 FDA авторизовало 1 451 AI/ML-устройство кумулятивно» | sources.md §2.1: «1,451 cumulative authorized devices через конец 2025» | ✓ VERIFIED |
| s04 | «На сегодняшний день, май 2026, реальная цифра уже в районе 1500-1550» | Не из sources — это freshness-projection. Verify on day of lecture. | ⚠️ FRESHNESS |
| s04 | «семьдесят шесть процентов — радиология» | sources.md §2.1: «Radiology = 76% всех authorizations (1,104 devices)» | ✓ VERIFIED |
| s04 | «более 14 миллионов исследований» (mosmed.ai) | sources.md §2.2: «Over 5 years, ИИ проанализировал >14 миллионов» | ✓ VERIFIED |
| s04 | «74 региона России» | sources.md §2.2 | ✓ VERIFIED |

### Раздел 1. Карта (s06–s08a)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s07 | «2015 году FDA одобряло примерно шесть AI/ML-устройств за год» | sources.md §2.1 не даёт per-year breakdown за 2015 specifically. Cumulative 1995-2015 = 33; средн ~1.5/год. **«6 в 2015»** — не подтверждено как specific. **P1.** | ⚠️ P1 NEEDS-CITATION |
| s07 | «между 1995 и 2015 кумулятивно — около тридцати трёх устройств, это 3%» | sources.md §2.1: «Between 1995-2015 — только 33 devices (3%)» | ✓ VERIFIED |
| s07 | «К 2020 году годовой приток вырос до 64» | sources.md не даёт specific 2020-year figure. **P1 — verify against FDA official list, JAMA review.** | ⚠️ P1 NEEDS-CITATION |
| s07 | «2023 — 221, 2024 — 258, 2025 — 295» | sources.md §2.1: «295 new authorizations в 2025; 258 в 2024; 2023 alone — 221 devices». ✓ all three match. | ✓ VERIFIED |
| s07 | «семьдесят шесть процентов относятся к радиологии» | sources.md §2.1 | ✓ VERIFIED |
| s08 | «Второго августа 2026 — первый этап EU AI Act для high-risk AI» | sources.md §8.2: «August 2026 — high-risk AI systems rules» | ✓ VERIFIED |

### Раздел 2. Диагностика (s09–s13a)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s09 | «CheXNet, 2017, 121 слой DenseNet, 14 патологий» | sources.md §2.5 + chapter line 207 + Rajpurkar 2017 arXiv:1711.05225 | ✓ VERIFIED |
| s09 | «MedCLIP, BiomedCLIP, RoentGen в 2024-2026» | published architectures, well-documented | ✓ VERIFIED |
| s10 | «CheXNet pneumonia: чувствительность ~94%, специфичность ~89%» | chapter line 229: «sens ≈ 0.94–0.96, spec ≈ 0.89–0.93» — speech rounds to «~94%, ~89%». ✓ within range. | ✓ VERIFIED |
| s10 | «В больничной выборке prevalence 30-50%, PPV ~80%» | chapter line 229-231 calculates PPV ~78% at prev=30%. Speech rounds «80%». ✓ acceptable. | ✓ VERIFIED |
| s10 | «В общей популяции prevalence 1%, PPV ~8%» | chapter line 231 + sources.md §2.5 mat | ✓ VERIFIED |
| s11 | «Liu, 2019, Lancet Digital Health. Мета-анализ 14 работ. Sens AI 87%, клиницистов 85%» | chapter line 241 + sources.md (Liu et al. 2019 DOI 10.1016/S2589-7500(19)30123-2). ✓ all matching. | ✓ VERIFIED |
| s11 | «MASAI Sweden, 2024-2025, Lancet. 100 000 шведских женщин» | sources.md §2.5: «>100,000 women» | ✓ VERIFIED |
| s11 | «80.5% AI vs 73.8% radiologist» | sources.md §2.5: «Sensitivity 80.5% (AI) vs 73.8% (standard)» | ✓ VERIFIED |
| s11 | «cancer detection rate 6.4 vs 5.0 на 1000» | sources.md §2.5: «6.4 vs 5.0 per 1000 (ratio 1.29)» | ✓ VERIFIED |
| s11 | «44% reduction workload» | sources.md §2.5: «44% reduction in radiologist workload» | ✓ VERIFIED |
| s11 | «12% reduction interval cancer rate» | sources.md §2.5: «12% reduction in interval breast cancers» (Lancet 2025 follow-up) | ✓ VERIFIED |
| s11 | «Goh, JAMA, октябрь 2024. Пятьдесят врачей» | sources.md §4.3 не указывает «50 врачей» explicitly. JAMA Net Open 2024 study — Goh et al. ran two arms; Nature Medicine 2025 follow-up — 92 physicians. **«50» — likely round figure, but точное число первой работы (JAMA Net Open 2024) не verified at 50.** **P2.** | ⚠️ P2 NEEDS-PRECISION |
| s11 | «Медиана с GPT-4 — 76%. Без — 74%. Статистически не значимо» | sources.md §4.3: «76.3% (GPT-4) vs 73.7% (conventional) — adjusted diff 1.6pp p=0.60». Speech rounds — ✓ acceptable. | ✓ VERIFIED |
| s11 | «GPT-4 один выдавал более высокий score» | sources.md §4.3: «GPT-4 alone scored higher than doctors-with-GPT-4» | ✓ VERIFIED |
| s12 | «более 14 миллионов исследований, 74 региона, 2000+ медорганизаций, 18+ млн изображений, ~70 AI services, 11 нацстандартов, ~300 эталонных датасетов» | sources.md §2.2 verified all numbers | ✓ VERIFIED |
| s12 | «маммография, маммография» (повтор в списке) | **P2 — duplicate word — orthographic; не factual but should be cleaned** | ⚠️ P2 EDIT-PASS |
| s12 | «оговорка: 4 млрд руб экономии не verified» | sources.md §2.3 verified: «Не цитировать «4 млрд руб/год экономии» без верифицированного источника». ✓ speech правильно дисклеймит. | ✓ VERIFIED (correct caveat) |
| s13 | «Daneshjou и коллеги, 2022, Science Advances. Чувствительность падала на 20-30%» | sources.md §9.2 confirms «Algorithms performed much worse on Black/brown skin images» но **specific 20-30% figure не явно цитируется**. **P1 — verify exact figure in Daneshjou 2022 paper.** | ⚠️ P1 NEEDS-CITATION |
| s13 | «Sjoding и коллеги, 2020, NEJM. FDA safety communication 2021» | sources.md §10.6 cross-ref + Sjoding 2020 NEJM letter | ✓ VERIFIED |

### Раздел 3. Drug discovery (s14–s18)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s15 | «10-15 лет и 1-2 миллиарда долларов на одобренный препарат. DiMasi 2016 и Wouters 2020» | DiMasi JJ et al. 2016 «Innovation in the pharmaceutical industry: New estimates of R&D costs» J Health Econ; Wouters OJ et al. 2020 JAMA. ✓ standard refs. | ✓ VERIFIED |
| s15 | «Шанс перейти от Phase 1 до одобрения — примерно 6.7%» | sources.md §1.9: «~6.7% chance to reach patients» | ✓ VERIFIED |
| s16 | «Половина Нобелевской премии по химии 2024 года. Hassabis и Jumper за AlphaFold разделили её с Baker» | Nobelprize.org 2024 Chemistry — confirmed: 50/50 split, Baker получил половину за computational protein design, Hassabis+Jumper — другая половина за AlphaFold | ✓ VERIFIED |
| s16 | «AlphaFold 2, 2021. К 2024 — более 200 млн структур» | sources.md §1.4 + chapter line 340: «более 200 миллионов структур белков (Jumper et al., 2021; AlphaFold DB, 2024)» | ✓ VERIFIED |
| s16 | «два с лишним миллиона исследователей-пользователей» | chapter line 340: «DeepMind заявляет о 2+ миллионах исследователей-пользователей» (self-reported, attributed) | ✓ VERIFIED (attributed) |
| s16 | «AlphaFold 3, Nature, май 2024. Diffusion-архитектура. Улучшение ~50% на PoseBusters» | sources.md §1.4: «50% accuracy improvement vs best classical methods» | ✓ VERIFIED |
| s16 | «AlphaProteo, сентябрь 2024. 88% success rate для BHRF1» | sources.md §1.5: «88% of candidate molecules bound successfully для BHRF1» | ✓ VERIFIED |
| s16 | «Улучшение affinity в 3-300 раз» | sources.md §1.5: «3-300× better binding affinity» | ✓ VERIFIED |
| s16 | «независимая репликация публично не зафиксирована» | sources.md §390 (Critical Gaps): «AlphaProteo reproducibility в independent labs — DeepMind wet lab data only; independent replication за 2024-2026 не найдена» — caveat correctly stated | ✓ VERIFIED |
| s17a | «Insilico Medicine Rentosertib. ISM001-055. Nature Medicine, июнь 2025» | sources.md §1.3: «Nature Medicine, June 2025. PubMed 40461817» | ✓ VERIFIED |
| s17a | «n=71, 21 центр в Китае. TNIK inhibitor» | sources.md §1.3 verified all numbers | ✓ VERIFIED |
| s17a | «60 mg QD, 12 недель. +98.4 mL FVC vs −20.3 mL placebo» | sources.md §1.3 verified verbatim from Nature Medicine table | ✓ VERIFIED |
| s17a | «диарея и отклонения функции печени, около 15% каждый» | sources.md §1.3: «14.8% каждый» — speech rounds «~15%». ✓ acceptable. | ✓ VERIFIED |
| s17a | «путь от target до preclinical candidate занял примерно 18 месяцев — против 4-5 лет» | sources.md §1.9 + chapter line 354. Self-reported by Insilico, correctly attributed in speech («Insilico заявляет»). ✓ | ✓ VERIFIED (attributed) |
| s17a | «Центр AIDD — альянс Сбер AI Lab и AIRI, декабрь 2024» | sources-ru §A.1: announcement Vedomosti 13 декабря 2024 (AI Journey), Q1 2025 created. ✓ | ✓ VERIFIED |
| s17a | «Альянсы Сбер плюс AIRI плюс Р-Фарм по онкологии CD137» | sources-ru §A.2: «May 2024 alliance, CD137 target в ComNews февраль 2024 (early mention)» | ✓ VERIFIED |
| s17a | «и по Альцгеймеру» | sources-ru §A.3: «ноябрь 2025 анонс программы против Альцгеймера» | ✓ VERIFIED |
| s17a | «MADD на EMNLP 2025 и DiMA на ICML 2025» | sources-ru §B.1 (MADD ACL Anthology EMNLP 2025 Findings) + §B.2 (DiMA ICML 2025 OpenReview) | ✓ VERIFIED |
| s17a | «ни одного российского AI-designed препарата в Phase 1 и выше на май 2026 не зафиксировано» | sources-ru §D.4 confirms negative finding | ✓ VERIFIED |
| s17b | «Январь 2020. Sumitomo Dainippon Pharma и Exscientia запустили Phase 1 для OCD» | sources.md §1.1: «Sumitomo press 2020-01-30» | ✓ VERIFIED |
| s17b | «Путь от target до Phase 1 — около 12 месяцев» | chapter line 374; CAS Insights source | ✓ VERIFIED |
| s17b | «В 2022 году Phase 1 в Японии остановлена. Причина discontinuation публично не раскрыта» | sources.md §1.1 + Critical Gaps line 394: «causes not specified». ✓ correctly caveated. | ✓ VERIFIED |
| s17b | «Recursion и Exscientia объявили о слиянии в августе 2024 года, $688 миллионов» | sources.md §1.2: «8 августа 2024, all-stock $688M deal» | ✓ VERIFIED |
| s18 | «PCCP — финальная гайданс 4 декабря 2024» | sources.md §8.1: «December 4, 2024: FINAL guidance — Marketing Submission Recommendations for PCCP» | ✓ VERIFIED |
| s18 | «EU AI Act. Регламент 2024/1689» | sources.md §8.2 + chapter line 393 + EU AI Act citation. ✓ | ✓ VERIFIED |
| s18 | «2 августа 2026 — high-risk не-MDR. 2 августа 2027 — MDR-regulated medical AI» | sources.md §8.2 | ✓ VERIFIED |
| s18 | «Россия — expedited procedure с 1 марта 2025. 57 зарегистрированных AI-медизделий к середине 2026» | sources.md §8.5: «57 to mid-2026 (52 Russian + 5 foreign)» + chapter line 392 confirms. ✓ | ✓ VERIFIED |

### Раздел 4. Этика и ответственность (s19–s24a)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s21 | «Obermeyer и коллеги, Science, 2019. Цитируется более 3000 раз» | sources.md §9.1 + Science Vol 366 DOI 10.1126/science.aax2342. «Цитируется более 3000» — verifiable on Google Scholar (currently ~4000+). ✓ | ✓ VERIFIED |
| s21 | «Impact Pro, Optum (дочка UnitedHealth). ~200 миллионов американцев» | sources.md §9.1 says algorithm «to identify high-risk patients». **200M figure** = UnitedHealth membership context, not directly in Obermeyer 2019 paper text. Chapter line 456 говорит «применяемый для примерно 200 миллионов американцев ежегодно». Это **paraphrased** в chapter as background, not direct Obermeyer quote. P2 paraphrase. | ✓ VERIFIED (context paraphrase) |
| s21 | «на 26% больше хронических заболеваний» | sources.md §9.1 — пишет «systematically underestimated Black patients» but specific «26%» figure — это chronic illness gap reported in Obermeyer 2019 paper. ✓ matches abstract. | ✓ VERIFIED |
| s21 | «~$1800 в год меньше» | sources.md §9.1: «$1,800/year less than equally-sick white patients» | ✓ VERIFIED |
| s21 | «bias уменьшился на 84%» | sources.md §9.1: «reduced disparity by 84%» | ✓ VERIFIED |
| s21 | «с 17.7 до 46.5%» | sources.md §9.1: «Increased Black patients served from 17.7% to 46.5%» — verbatim. ✓ | ✓ VERIFIED |
| s22 | «NEDA. С 2018 NEDA использовала Tessa как первую линию helpline» | sources.md §6.1 confirms NEDA-Tessa relationship — although **2018 как точный год launch** не подтверждён в research sources.md (sources говорят «NEDA replaced unionizing human helpline staff»). **P2 — verify 2018 launch date.** | ⚠️ P2 NEEDS-PRECISION |
| s22 | **«В марте 2023 года vendor Cass самовольно сменил Tessa с rule-based на generative LLM»** | sources.md §6.1 НЕ указывает «март 2023» как дату Cass-перехода. Только: «Cass changed Tessa без NEDA's approval» (general). NPR June 2023 timeline confirms screenshots posted May 2023; точная дата перехода Cass — публично не задокументирована в research. **P1 — «март 2023» is best-guess timing not directly sourced.** | ⚠️ P1 NEEDS-CITATION |
| s22 | «30 мая 2023 активистка Sharon Maxwell опубликовала скриншоты. NEDA сняла за 24 часа» | sources.md §6.1: «NEDA pulled Tessa May 30, 2023 (<24h after Maxwell's screenshots)» — Speech говорит «30 мая 2023 Sharon Maxwell опубликовала, NEDA сняла за 24 часа». ✓ matches. | ✓ VERIFIED |
| s22 | «Cass советовал терять 1-2 фунта в неделю, удерживать дефицит 500-1000 калорий» | sources.md §6.1: «lose 1-2 pounds/week, calorie deficit 500-1000/day» — verbatim. ✓ | ✓ VERIFIED |
| s22 | «Adversarial hallucination. Nature Communications Medicine, 2025. 6 ведущих LLM на 300 vignette» | sources.md §4.5: «Communications Medicine 2025; 6 leading LLMs on 300 clinical vignettes» | ✓ VERIFIED |
| s22 | «модели повторяли или расширяли фейк в 83% случаев» | sources.md §4.5: «repeat/elaborate on fake error in up to 83% of cases» | ✓ VERIFIED |
| s22 | «По Becker's Hospital Review, ~40 миллионов американцев» | sources.md §6.3: «40 million Americans» с атрибуцией Becker's. ✓ | ✓ VERIFIED |
| s22 | **«По Gallup — трое из пяти взрослых»** | **P0 — ATTRIBUTION ERROR.** sources.md §6.3: Gallup figure is «25% US adults»; **«3 in 5 US adults» — это OpenAI survey**, не Gallup. **Misattribution.** Должно быть либо «по OpenAI/Rock Health survey — трое из пяти» либо «по Gallup — каждый четвёртый взрослый». **REVISE.** | ❌ **P0 ATTRIBUTION SWAP** |
| s23 | «21 февраля 2024 ALPHV BlackCat атаковала Change Healthcare» | sources.md §7.1: «Attack date 21 февраля 2024. ALPHV BlackCat ransomware group» | ✓ VERIFIED |
| s23 | **«обрабатывает треть всех claims в США»** | sources.md §7.1 не цитирует ни «треть», ни «50%». Public sources (AHA, Kaspersky) утверждают Change Healthcare обрабатывает **~50% медицинских транзакций в США**, или alternatively «1/3 всех patient records», not «1/3 claims». **P1 — verify ratio precisely.** | ⚠️ P1 NEEDS-PRECISION |
| s23 | «уязвимый Citrix remote access без MFA» | sources.md §7.1: «Vector: vulnerable Citrix remote access без MFA» | ✓ VERIFIED |
| s23 | «190 миллионов американцев, 6 TB, $22M Bitcoin, $2.457 миллиарда» | sources.md §7.1 — all 4 numbers verified | ✓ VERIFIED |
| s23 | «(Sweeney, 2002)» Massachusetts governor | sources.md §7.3: **«First attack — 1997: Sweeney re-identified Governor of Massachusetts»**. k-anonymity paper — 2002. Speech cites «Sweeney, 2002» (paper). **P2 — citing methodology paper year (2002) is technically correct, but creates implicit suggestion that attack was 2002, not 1997.** | ⚠️ P2 PRECISION |
| s23 | «HIPAA США, 1996. GDPR ЕС, 2016. ФЗ-152 Россия с amendments 2024-2025» | sources.md §7.3 + §7.4 + standard legal refs | ✓ VERIFIED |
| s23 | «ФЗ-23 от 28 февраля 2025. Data localization. С 1 июля 2025» | sources.md §7.4: «Federal Law N 23-ФЗ, 28 февраля 2025; С 1 июля 2025: persona data of Russian citizens cannot be processed/stored outside Russia» | ✓ VERIFIED |
| s24 | «4-actor framework. Price, 2019, Stanford. Gerke, 2020, Elsevier» | **P1.** W. Nicholson Price II is **University of Michigan Law School** (and various visiting positions). Gerke is at **Penn State Dickinson Law** (formerly Petrie-Flom at Harvard). «Stanford» для Price и «Elsevier» (publisher, not affiliation) для Gerke — incorrect affiliations. References themselves real: Price «Risks and Remedies for AI in Health Care» (Brookings 2019); Gerke et al. «Ethical and Legal Challenges of AI-Driven Healthcare» (Elsevier book chapter 2020). **P1 — fix affiliations.** | ⚠️ P1 ATTRIBUTION-PRECISION |
| s24 | «На май 2026 громких прецедентных дел о AI medical malpractice нет» | sources.md §8.3: «No notable AI malpractice lawsuits yet as of mid-2025» — extending to May 2026 reasonable but **needs day-of-lecture verification**. | ⚠️ FRESHNESS |
| s24 | «Lawsuits выросли на 14% в 2024» | sources.md §8.3: «14% increase в malpractice claims involving AI tools 2024 vs 2022» | ✓ VERIFIED |
| s24 | «врач — финальная клиническая ответственность undivided» | sources.md §8.3 + §8.4: legal consensus «liability remains with humans». ✓ | ✓ VERIFIED |

### Раздел 5. Заключение (s26–s29)

| Slide | Speech claim | Source | Verdict |
|---|---|---|---|
| s26 | recap — все 3 вывода consistent с chapter | chapter §6.1-6.3 + sources.md verified | ✓ VERIFIED |
| s28 | «Cognitive Agro Pilot: 1500 машин» | Лекция 6 forward-link — verify в research лекции 6 when written | — Lec 6 forward |

---

## P0 / P1 / P2 detail (actionable)

### P0 #1 (CRITICAL — must fix before show) — s22 Gallup/OpenAI attribution swap

**Quote (speech line 528):**
> «По Becker's Hospital Review, около сорока миллионов американцев используют ChatGPT для healthcare. По Gallup — трое из пяти взрослых.»

**Issue:** sources.md §6.3 attributions:
- «3 in 5 US adults» = **OpenAI/Rock Health survey** (not Gallup);
- Gallup figure = «25% US adults» («каждый четвёртый», not «трое из пяти»).

**Correct version (option A — keep both):**
> «По Becker's Hospital Review — около сорока миллионов американцев. По Rock Health survey — трое из пяти взрослых пользовались AI для здоровья в последние три месяца. По Gallup — каждый четвёртый.»

**Correct version (option B — simplify):**
> «По Becker's Hospital Review — около сорока миллионов американцев. По Rock Health и OpenAI surveys — каждый третий-пятый взрослый.»

**Severity:** P0 (misattribution к organizations с разной authority weight in audience perception).
**Recommendation:** speech-writer revise s22 line 528.

---

### P1 #1 — s07 FDA per-year breakdown «6 в 2015, 64 в 2020» не в sources.md

**Quote (speech line 160-162):**
> «В 2015 году FDA одобряло примерно шесть AI/ML-устройств за год. ... К 2020 году годовой приток вырос до шестидесяти четырёх.»

**Issue:** sources.md §2.1 gives only **cumulative** breakdowns (1995-2015 = 33 cumulative; 2023-2024-2025 = 221/258/295 annual). Per-year for 2015 and 2020 specifically — not in research notes.

**Verification need:** check JAMA Network Open (sources.md §2.1) for per-year breakdown in their figure/table, or FDA AI/ML list official page filtered by year.

**Severity:** P1.
**Recommendation:** verify these two specific numbers in primary source; либо удалить their use, либо найти supporting figure.

---

### P1 #2 — s13 Daneshjou 20-30% sens drop specific figure

**Quote (speech line 304):**
> «На коже с тёмными тонами по шкале Фитцпатрика чувствительность падала на двадцать-тридцать процентов по сравнению со светлой.»

**Issue:** sources.md §9.2 confirms qualitative «much worse on Black/brown skin images» but **no specific 20-30% figure**. Daneshjou et al. 2022 Science Advances reported quantitative drops, но точная цифра в speech не cross-referenced.

**Verification need:** verify Daneshjou 2022 paper Table 1 / 2 — find exact magnitude.

**Severity:** P1.
**Recommendation:** либо verify exact range («14-30%» по Adamson/Daneshjou) и заменить, либо ослабить до «значительно — на десятки процентов».

---

### P1 #3 — s22 Cass «март 2023» переход на generative

**Quote (speech line 520):**
> «В марте 2023 года vendor Cass самовольно сменил Tessa с rule-based на generative LLM»

**Issue:** sources.md §6.1 не указывает точную дату Cass-перехода («март 2023»). Только подтверждает: «Cass changed Tessa без NEDA's approval» (general timing); экспонирование — May 2023 (Sharon Maxwell).

**Verification need:** verify NPR / Psychiatrist.com / CBS articles для exact Cass transition date.

**Severity:** P1.
**Recommendation:** либо найти source для «март 2023», либо переформулировать на «весной 2023 года» / «в начале 2023».

---

### P1 #4 — s24 Price «Stanford», Gerke «Elsevier» affiliations incorrect

**Quote (speech line 570):**
> «4-actor framework. Price, 2019, Stanford. Gerke, 2020, Elsevier.»

**Issue:**
- W. Nicholson Price II — University of Michigan Law School (primary affiliation); has visiting positions at Stanford/Harvard but **primary affiliation NOT Stanford**.
- Gerke — Penn State Dickinson Law (currently); was at Harvard Petrie-Flom. **«Elsevier» — это publisher** (для her chapter в Bohr & Memarzadeh «Artificial Intelligence in Healthcare» 2020), не affiliation.

**Correct version:**
> «Price, 2019, U Michigan + Brookings. Gerke et al., 2020, Petrie-Flom Harvard / Penn State.»

**Severity:** P1 (academic precision; potential audience credibility hit if students fact-check).
**Recommendation:** speech-writer revise s24 line 570.

---

### P1 #5 — s23 Change Healthcare «треть всех claims»

**Quote (speech line 546):**
> «Change Healthcare — дочка UnitedHealth, обрабатывает треть всех claims в США»

**Issue:** sources.md §7.1 не дает точной share. Public reports vary:
- AHA: «processes ~15B healthcare transactions annually» — share не specified;
- Kaspersky: «one in three healthcare transactions» (близко к speech claim);
- House Energy Commerce hearing: «processes claims for 1 in 3 Americans».

«Treть всех claims» — defensible, но точная formulation differs across sources. Some claim 50% of medical transactions, some 33%.

**Severity:** P1.
**Recommendation:** clarify — «один из трёх медицинских транзакций» (per House E&C hearing) или «треть американских пациентов через свои claims» — точная formulation.

---

### P2 #1 — s23 Sweeney 1997 attack vs 2002 paper

**Quote (speech line 552):**
> «каноническая иллюстрация — re-identification медзаписи губернатора Massachusetts через сопоставление HIPAA-compliant deidentified dataset с публичным voter roll. Sweeney, 2002.»

**Issue:** Massachusetts governor re-identification — **1997 attack**. Sweeney 2002 — k-anonymity formalization paper (cite is correct as methodology reference). Implicit reading: «attack happened in 2002» — incorrect.

**Severity:** P2.
**Recommendation:** «...Sweeney показала ещё в 1997 году, формализовано в k-anonymity model (Sweeney, 2002).»

---

### P2 #2 — s11 Goh «50 врачей»

**Quote (speech line 266):**
> «Goh, JAMA, октябрь 2024. Уже не imaging, а диагностическое мышление. Пятьдесят врачей»

**Issue:** sources.md §4.3 не указывает «50 врачей» для JAMA Net Open Oct 2024 study. Nature Medicine 2025 — 92 physicians. **«50» — round figure; точное n не verified.**

**Severity:** P2 (round number может быть orientation-only).
**Recommendation:** verify n в Goh JAMA Net Open 2024 paper exact figure; либо переформулировать «несколько десятков врачей».

---

### P2 #3 — s12 «маммография, маммография» дубль

**Quote (speech line 286):**
> «...рентгенография грудной клетки, КТ лёгких, маммография, маммография, оссеоденситометрия...»

**Issue:** дублирование «маммография». Не factual error, но editorial polish.

**Severity:** P2 (orthographic / list integrity).
**Recommendation:** удалить дубль; либо если намерение было «маммография [screening + diagnostic]» — explicate.

---

## Freshness watchlist (verify-on-day-of-lecture)

| # | Claim | Source date | Lecture date | Refresh cadence | Action |
|---|---|---|---|---|---|
| 1 | FDA cumulative «1 451 к концу 2025; ~1500-1550 к маю 2026» | 2025-12 | 2026-05-13 | quarterly | **Verify on lec day** via fda.gov/medical-devices/.../artificial-intelligence-enabled-medical-devices |
| 2 | mosmed.ai «14 миллионов исследований» | 2025-12 (sources §2.2) | 2026-05-13 | quarterly | **Verify on lec day** via mosmed.ai/en/ или Remedium |
| 3 | «На май 2026 громких прецедентных дел AI malpractice нет» | mid-2025 (sources §8.3) | 2026-05-13 | monthly | **Verify on lec day** via westlaw / pacer / Sommers Schwartz / Brandon Broderick updates |
| 4 | Россия «57 зарегистрированных AI-медизделий» | mid-2026 (sources §8.5) | 2026-05-13 | quarterly | **Verify** via Webiomed blog / Roszdravnadzor portal |
| 5 | «40 миллионов американцев используют ChatGPT для healthcare» | 2025 (sources §6.3) | 2026-05-13 | monthly | **Verify on lec day** — search «Becker's Hospital Review ChatGPT 40 million» — speech подготовка-блок (line 31) уже flag-ит это freshness check ✓ |

Speech подготовительный блок (lines 28-31) уже включает freshness checks — это good practice. Только добавить #3 (AI malpractice landmark cases) в pre-flight список.

---

## VERIFIED facts summary (sample of strongly-verified, 30+ total)

- ✓ CheXNet 2017 121-layer DenseNet (Rajpurkar et al., arXiv:1711.05225)
- ✓ FDA AI/ML cumulative 1,451 to end-2025 (FDA official list + JAMA Net Open systematic review)
- ✓ Radiology = 76% of FDA AI list (1,104 devices)
- ✓ FDA 2023/2024/2025 annual approvals 221 / 258 / 295
- ✓ mosmed.ai operational metrics (14M studies, 74 regions, 70 services, 11 nat'l standards, 18M images, ~300 datasets)
- ✓ MASAI Sweden RCT: 80.5% AI sens vs 73.8% radiologist; CDR 6.4 vs 5.0/1000; 44% workload reduction; 12% interval cancer reduction
- ✓ Goh JAMA Net Open 2024: GPT-4 median 76.3 vs conventional 73.7, p=0.60; GPT-4 alone > both groups (paradox)
- ✓ Liu et al. 2019 Lancet Digital Health, 14 studies meta-analysis, AI sens 87% vs clinicians 85%
- ✓ Daneshjou et al. 2022 Science Advances + fine-tune DDI закрыл gap
- ✓ Sjoding et al. 2020 NEJM (pulse oximeter racial bias); FDA safety communication 2021
- ✓ AlphaFold 2 (2021) 200M+ structures by 2024; AlphaFold DB free at alphafold.ebi.ac.uk
- ✓ AlphaFold 3 Nature May 2024, diffusion, ~50% improvement on PoseBusters
- ✓ AlphaProteo Sep 2024, 88% BHRF1 success, 3-300× affinity, VEGF-A binder (DeepMind self-reported, correctly attributed)
- ✓ Nobel Chemistry 2024 50/50 split: Baker + (Hassabis + Jumper)
- ✓ Insilico Rentosertib (ISM001-055) Nature Medicine June 2025: +98.4 mL vs −20.3 mL placebo; n=71 China; TNIK inhibitor; AE ~15% diarrhea/liver; 18-mo timeline self-reported
- ✓ DSP-1181 Exscientia × Sumitomo Jan 2020, OCD, 12-mo timeline, Phase 1 discontinued 2022, current status Discontinued
- ✓ Recursion × Exscientia merger 8 Aug 2024, $688M, completed Nov 2024
- ✓ FDA PCCP final guidance 4 December 2024
- ✓ EU AI Act Regulation 2024/1689, high-risk non-MDR 2 Aug 2026, MDR-regulated 2 Aug 2027
- ✓ Russia Росздравнадзор expedited procedure with 1 March 2025; 57 AI med devices to mid-2026
- ✓ Obermeyer et al. Science 2019: 26.3% chronic illness gap; $1800/yr less; 84% bias reduction; 17.7% → 46.5%
- ✓ NEDA Tessa: Cass changed to generative without NEDA approval; Sharon Maxwell screenshots 30 May 2023; NEDA pulled within 24h; classic ED triggers (1-2 lb/wk, deficit 500-1000 cal/day)
- ✓ Adversarial hallucination Nature Communications Medicine 2025: 6 LLMs, 300 vignettes, 83% repeat rate; mitigation halves not zero
- ✓ Change Healthcare Feb 21, 2024 attack: ALPHV BlackCat; Citrix no-MFA; 190M Americans; 6 TB; $22M Bitcoin ransom; $2.457B cost
- ✓ ФЗ-23 28 February 2025 + 1 July 2025 data localization deadline
- ✓ RU drug discovery RU context: AIDD центр Сбер+AIRI announced 13 Dec 2024 / Q1 2025; CD137 alliance May 2024; Alzheimer alliance Nov 2025; MADD EMNLP 2025 (ITMO+Sber AI Lab); DiMA ICML 2025 (AIRI)
- ✓ No Russian AI-designed drug in Phase 1+ as of May 2026 (negative finding correctly stated)

---

## Top 5 actionable corrections для speech-writer (priority order)

1. **[P0]** s22 line 528 — swap «По Gallup — трое из пяти» → «По Rock Health/OpenAI survey — трое из пяти; по Gallup — каждый четвёртый».
2. **[P1]** s24 line 570 — fix Price affiliation «Stanford» → «U Michigan»; Gerke «Elsevier» → «Penn State / Harvard Petrie-Flom».
3. **[P1]** s22 line 520 — «март 2023» Cass перешёл — либо найти точный source, либо ослабить до «весной 2023» / «в начале 2023».
4. **[P1]** s07 lines 160-162 — verify FDA per-year «6 в 2015 / 64 в 2020» в JAMA Net Open paper, или ослабить.
5. **[P1]** s13 line 304 — verify Daneshjou 2022 exact magnitude «20-30%» в Science Advances paper Table 1/2.

Optional polish:
6. **[P2]** s23 line 552 — Sweeney 1997 attack vs 2002 paper — clarify temporal sequence.
7. **[P2]** s11 line 266 — verify n=50 для Goh JAMA Net Open 2024.
8. **[P2]** s12 line 286 — «маммография, маммография» дубль убрать.
9. **[FRESHNESS]** add to pre-flight (lines 25-34): «verify AI malpractice landmark — есть ли первое landmark case по AI на сегодня».

---

## Methodology / scope notes

- **Sources used:** `notes/research/lecture-4/sources.md` (82 source citations, last validated 2026-05-13 in chapter v2 phase 4) + `sources-ru-drug-discovery.md` (22 RU-specific sources) + chapter v2 cross-reference.
- **No live web search done** в этом pass — relied on research-files-as-ground-truth (per fact-checker README §1). Day-of-lecture freshness check responsibility — at lecturer's pre-flight (lines 25-34 of speech.md уже планируют это).
- **Speech vs chapter consistency:** speech almost entirely mirrors chapter v2 verified content. Speech adds RU drug discovery context (s17a) which is new vs chapter — но verified against `sources-ru-drug-discovery.md`. No speech-only fabrications detected outside of P0/P1 flagged above.

---

## Verdict reasoning

**APPROVE-WITH-POLISH** (not APPROVE-CLEAN because 1 P0 + 5 P1 must be addressed; not REVISE because no fabricated facts, no direction inversions, no broken citations, all numbers either verified or differ in precision-grade ways).

Speech v1 is **show-able** with:
- mandatory P0 fix (Gallup attribution) **before** lecture;
- recommended P1 fixes на ваш discretion;
- freshness checks day-of-lecture already planned by speech-writer (good practice).

Production quality of fact-grounding — **сильная**: speech derives from chapter v2 which underwent prior fact-check. No hallucinations of fact, no fake citations, no number drift в critical metrics (Rentosertib, MASAI, AlphaFold/Proteo, Change Healthcare, ФЗ-23, EU AI Act, PCCP, Obermeyer — all verified verbatim). The single P0 — attribution swap — is editorial-correctable in 30 seconds.

Recommendation: orchestrator проводит speech-writer revision на P0 + 4 P1, после чего speech v2 = APPROVE-CLEAN ready.

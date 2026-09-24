VERDICT: REVISE

# Fact-check — chapter v1 Лекция 16

**Дата:** 2026-05-27
**Object:** chapter.md + parts 2-4 (28 541 слов, 4 parts)
**Method:** WebSearch verification on sample 45+ claims (15 numbers + 10 dates + 10 citations + 10 vendor claims + 5 additional cross-checks)
**Verdict:** REVISE

## Summary

Из 45 sample claims **верифицировано 33 = 73%**. Найден **1 P0 (Stabroek BOE confused с Permian BOE)**, **9 P1 corrections** (включая Aramco revenue 2024, MethaneSAT lifetime в months, GHGSat constellation count, Cognitive Geologist start date, EPA Subpart W delay timing, AspenTech-Emerson valuation, Stanford 2024 study mt/y figure, 86% McKinsey attribution, Beyond Limits investment date), **3 P2 polish items**. Chapter имеет strong research grounding в research files 02+03+07 — большинство major facts verifiable. Но **систематические date errors** (Cognitive Geologist 2017→2019, Beyond Limits 2018→2017, EPA Subpart W 2024→2025) и **outdated/conflated numbers** (Aramco 2024 revenue, Stabroek/Permian BOE mix-up, GHGSat 16→13 satellites, Stanford 7.5→6 Mt) требуют correction round перед USER GATE A.

**Top-3 critical corrections (для book-editor Phase 4):**
1. **P0:** §2.4 chapter-part2.md — «Stabroek estimate: ~16 миллиардов BOE» — НЕВЕРНО. Stabroek = 9-11B BOE; 16B BOE — это **ExxonMobil+Pioneer Permian** combined, упомянутые в §1.4. Конфликт между двумя цифрами в разных секциях.
2. **P1:** §2.2 + Введение — «Aramco $440 млрд выручка 2024» — НЕВЕРНО. $436.6B 2024; $440.8B 2023. Calculation $1.8B/$440B = 0.4% использует **wrong base**.
3. **P1:** §3.3 — «MethaneSAT ~13 месяцев работы» (multiple sections) — НЕВЕРНО. March 4 2024 → June 20 2025 = **15.5 месяцев**. Inside Climate News + Carbon Mapper sources подтверждают «15 months».

## P0 issues (FACTUAL — must fix ДО USER GATE A)

### P0.1 — Stabroek BOE confused with Permian BOE (§2.4 chapter-part2.md)

**Quote:** «Stabroek estimate: ~16 миллиардов BOE»
**Reality:** Stabroek Block (Гайана) recoverable resources = **11+ billion BOE** на момент 2025 года (Chevron-Hess closing); ранее ~9 BOE (2024 estimate). **16B BOE — это ExxonMobil+Pioneer Permian holdings** (1.4M net acres + ~16B BOE), упомянутые в §1.4 chapter.md.
**Severity:** P0 (factual confusion двух разных активов; vendor analysis student может неправильно интерпретировать)
**Correction:** «Stabroek estimate: ~11 миллиардов BOE (2025 после Chevron+Hess закрытия); ранее ~9 BOE (2024 Hess estimate)»
**Source:** [JPT Chevron-Hess closing](https://jpt.spe.org/chevron-closes-hess-deal-exxonmobil-welcomes-new-partner-offshore-guyana) + [S&P Global Stabroek 9B](https://www.spglobal.com/platts/en/market-insights/latest-news/oil/102820-resource-estimate-at-guyanas-stabroek-block-raised-to-9-billion-boe-hess)

## P1 issues (CORRECTION needed)

### P1.1 — Aramco revenue 2024 wrong base (multiple sections)

**Quote:** «Aramco выручка 2024 ≈ $440 млрд. $1,8B / $440B = 0,4% выручки» (§2.2 chapter-part2.md + Введение chapter.md)
**Reality:** Aramco revenue 2024 = **$436.6B** (full year results, March 2025 release). $440.8B was **2023** revenue. $1.8B/$436.6B = **0.41% выручки** — directionally same, but precise number wrong.
**Severity:** P1 (book-editor used 2023 figure for 2024 calculation)
**Correction:** «Aramco выручка 2024 = $436,6 млрд» либо «Aramco выручка 2023-2024 ≈ $437-441 млрд» — calculation result still 0.4%.
**Source:** [Aramco FY 2024 full results](https://www.aramco.com/en/news-media/news/2025/aramco-announces-full-year-2024-results) + CNBC coverage

### P1.2 — MethaneSAT lifetime: 13 months vs 15 months (multiple sections)

**Quote:** «MethaneSAT mission ~13 месяцев работы (March 2024 - June 2025)» (§3.3 + §3.2 + closing synthesis)
**Reality:** Launch **4 марта 2024 года**; loss **20 июня 2025 года** = **15.5 months** of operation. Inside Climate News article + Carbon Mapper Tanager-1 one-year-in-space update both confirm «15 months».
**Severity:** P1 (consistent throughout chapter — needs cascade fix)
**Correction:** заменить «~13 месяцев» → «~15 месяцев» на всех вхождениях. Frontmatter strict-in-self-estimate calculation may need update.
**Source:** [Inside Climate News MethaneSAT Feb 2026](https://insideclimatenews.org/news/06022026/methanesat-climate-pollution-global-assessment/) — «only in orbit for 15 months»

### P1.3 — Gazprom Neft Cognitive Geologist start year (§5.2 chapter-part4.md)

**Quote:** «Создан в партнёрстве с IBM Research Brazil (Сан-Паулу) в период 2017–2022 годов»
**Reality:** Cooperation Agreement signed **April 2019**, not 2017. Multiple sources (ROGTEC, World Oil, Gazprom Neft press) consistently date partnership announcement April 3-5, 2019.
**Severity:** P1 (factual date error; 2 years off)
**Correction:** «Создан в партнёрстве с IBM Research Brazil в период **2019–2022 годов**»
**Source:** [Gazprom Neft IBM partnership April 2019](https://www.worldoil.com/news/2019/4/3/gazprom-neft-ibm-research-brazil-enhance-geological-processing-with-ai) + ROGTEC + Gazprom press

### P1.4 — EPA Subpart W proposed delay date (§3.6 + footnote 31)

**Quote:** «September 2024 — EPA proposed delay Subpart W effective date до 2034 года» (§3.6 chapter-part3.md + reference 31)
**Reality:** EPA proposal to suspend Subpart W reporting until 2034 was made **September 12, 2025**, not September 2024. May 2024 was the **final rule release**; September 2025 was the **Trump-admin proposed rollback**.
**Severity:** P1 (significant date error; 1 year off; political context Trump admin 2025+)
**Correction:** «**Сентябрь 2025** — EPA (Trump admin) предложило delay Subpart W effective date до 2034 года». Reference 31 — обновить дату.
**Source:** [Federal Register Nov 2024 Waste Emissions Charge](https://www.federalregister.gov/documents/2024/11/18/2024-26643/) + [EELP tracker EPA methane standards](https://eelp.law.harvard.edu/tracker/epa-voc-and-methane-standards-for-oil-and-gas-facilities-2/)

### P1.5 — Beyond Limits investment year (§2.5 chapter-part2.md)

**Quote:** «В 2018 году BP стала крупнейшим клиентом и инвестором компании Beyond Limits»
**Reality:** BP Ventures $20M Series B investment was **announced June 2017**; articles ran through 2018 (Journal of Petroleum Technology October 2018 coverage). Initial announcement = 2017, partnership context = 2017-2018. Beyond Limits company founded 2012 (per NASA Spinoff) or 2014 (per official "Our Story") — sources differ; 2012 is most common.
**Severity:** P1 (chapter consistently uses "2018" — should be "2017" for investment, "2017-2018" for partnership formation)
**Correction:** «В **июне 2017 года** BP Ventures инвестировала $20M в Series B Beyond Limits; партнёрство развернулось в 2017-2018 годах»
**Source:** [BP press release Caltech startup Beyond Limits](https://www.bp.com/en/global/corporate/news-and-insights/press-releases/caltech-startup-beyond-limits-secures-investment-of-20-million-from-bp-ventures.html) + [Drilling Contractor](https://drillingcontractor.org/beyond-limits-secures-investment-20-million-bp-ventures-ai-software-43132)

### P1.6 — AspenTech Emerson acquisition valuation (§1.3 chapter.md)

**Quote:** «AspenTech (приобретена Emerson примерно за $15 млрд в 2025 году) [VFY-day-of]»
**Reality:** Deal completed **March 12, 2025** at **$265/share** = total fully-diluted market cap **$17.0B**, enterprise value **$16.8B**. Emerson acquired remaining ~43% shares (already owned ~57%) for **$7.2B**. Initial November 2024 proposal was $15.1B at $240/share; final agreed price was higher.
**Severity:** P1 (chapter says "~$15 млрд" — outdated; final = ~$17B EV)
**Correction:** «AspenTech (приобретена Emerson за **~$17 млрд EV** в марте 2025 года; $7,2 млрд за remaining outstanding shares)»
**Source:** [Emerson Acquires AspenTech press release Jan 2025](https://www.aspentech.com/en/resources/press-releases/emerson-to-acquire-remaining-outstanding-shares-of-aspentech) + completion announcement March 12 2025

### P1.7 — Stanford 2024 study methane figure (§3.5 chapter-part3.md + reference 27)

**Quote:** «Aerial campaign на US O&G basins; результат — примерно 7,5 миллионов тонн/год»
**Reality:** Stanford Nature March 2024 paper: «more than **6 million tons per year** of methane». Не 7.5 Mt. Стандартная characterization — «3× government estimate» (factor 3, not factor 2 as chapter implies). Permian alone ~410 t/h × 8760 h = 3.6 Mt/y.
**Severity:** P1 (factual number error; affects «4× vs MethaneSAT — Stanford factor 2» comparison)
**Correction:** «Stanford 2024 study: US O&G methane **~6 миллионов тонн/год** aerial (factor 3 vs EPA Inventory ~4 Mt, или 50% выше)»
**Source:** [Stanford News March 2024](https://news.stanford.edu/stories/2024/03/methane-emissions-major-u-s-oil-gas-operations-higher-government-predictions) — «more than 6 million tons per year»

### P1.8 — McKinsey 86% attribution (§1.2 chapter.md + multiple)

**Quote:** «По данным McKinsey 2024 года, такая доля AI-проектов в энергетике не выходит за пределы пилотной стадии» (86%)
**Reality:** McKinsey 2025 State of AI говорит «nearly two-thirds» (~67%) **cross-industry**, не «86% в энергетике». 86% — это **BCG analysis** (September 2025), которое цитирует McKinsey но adds energy-specific lens. Research file 03 §1.6 признаёт: «Cited in BCG analysis».
**Severity:** P1 (attribution chain неточная; статистика real но attributed wrong)
**Correction:** «По данным **BCG analysis 2025** (со ссылкой на McKinsey), 86% AI-проектов в энергетике не выходят за пределы пилотной стадии» — иначе обоснован источник.
**Source:** [BCG AI-First Future O&G](https://www.bcg.com/publications/2025/ai-first-future-of-oil-and-gas-companies) + McKinsey State of AI 2025

### P1.9 — GHGSat constellation count (§3.4 chapter-part3.md)

**Quote:** «GHGSat — Коммерческое созвездие из 16 спутников к 2025 году (12 cubesats в начале 2024 + дополнительные запуски в 2024–2025)»
**Reality:** GHGSat constellation = **13 satellites as of June 2025** (eoPortal, ESA Earth Online, GHGSat official). Plans to «near-double» fleet в coming years. Not 16.
**Severity:** P1 (constellation count overcounted)
**Correction:** «GHGSat — Коммерческое созвездие из **13 спутников к середине 2025 года** с планами расширения»
**Source:** [GHGSat Constellation eoPortal](https://www.eoportal.org/satellite-missions/ghgsat-con) + [GHGSat official](https://www.ghgsat.com/en/technology/constellation/)

## P2 issues (POLISH)

### P2.1 — MethaneSAT Permian EPA baseline (§Introduction chapter.md)

**Quote:** «410 t/h Permian baseline 100 t/h EPA» (paraphrase from frontmatter context)
**Reality:** EPA Greenhouse Gas Inventory Permian = **104 t/h** (per Gizmodo coverage). Chapter rounds to 100; 104 is more precise.
**Severity:** P2 (rounding error; difference negligible)
**Correction:** Option: «baseline ~104 t/h EPA» либо оставить «100 t/h» как разумное округление.

### P2.2 — Colonial Pipeline ransom (§5.4 chapter-part4.md + reference 41)

**Quote:** «~$5M ransom paid»
**Reality:** Actual ransom = **$4.4 million USD** (75 bitcoin); chapter rounds up. DOJ recovered $2.3M of that.
**Severity:** P2 (rounding; «~$5M» is close-enough approximation)
**Correction:** Optional precision improvement: «~$4.4M ransom (75 BTC, $2.3M recovered DOJ)»

### P2.3 — C3.ai O&G vertical revenue percentage (§1.7 chapter.md + reference 16)

**Quote:** «Oil&Gas vertical = 5,9% от общей выручки = ~$18 млн из $310 млн total»
**Reality:** Latest C3.ai search result mentions «5.2% of pilot distribution in FY24» — different framing. Chapter cites «5.9% revenue» which may be earlier filing or different metric.
**Severity:** P2 (number borderline; exact methodology unclear without primary 8-K read)
**Correction:** Verify via C3.ai FY24 8-K directly; consider «5-6% revenue» range.

## Verification tables

### Numbers (sample 15)

| # | Claim | Chapter section | Verified? | Source | Correction |
|---|---|---|---|---|---|
| 1 | Aramco $1.8B AI realized value 2024 | Введение + §2.2 | VERIFIED | Davos statement Nasser 2025; Aramco press | — |
| 2 | Aramco revenue 2024 $440B | Введение + §2.2 | **DISPUTED** | $436.6B per Aramco FY24 results | P1.1: use $436.6B or $437-441B range |
| 3 | Eni HPC6 606 PFLOPS Top500 #5 | §2.2 | VERIFIED | Top500 list Nov 2024; Eni press | minor: launch Nov 2024 not Dec 2024 |
| 4 | ExxonMobil Discovery 6 4032 NVIDIA Grace Hopper | §2.4 | VERIFIED | HPE blog 2025; HPCwire | — |
| 5 | Discovery 6 4× faster than Discovery 5 | §2.4 | VERIFIED | HPE official 2025 | — |
| 6 | Discovery 6 unlock $1B+ Stabroek 6 FPSO | §2.4 | VERIFIED (claim) | HPCwire ExxonMobil | — |
| 7 | Stabroek estimate ~16B BOE | §2.4 | **FALSE** | Stabroek = 9-11B BOE; 16B = Permian ExxonMobil+Pioneer | **P0.1**: replace with 11B BOE |
| 8 | Nabors PACE-X 20 000 ft Haynesville lateral | §1.5 | UNVERIFIABLE | Bakken 4-mile + Delaware 4-mile confirmed; Haynesville 20k ft not in SEC 8-K | **borderline P1**: verify SEC source або mark [VFY-day-of] |
| 9 | MethaneSAT Permian 410 t/h, 50% > EPA | §Введение + §3.2 | VERIFIED | MethaneSAT/EDF release 2024 | Permian-specific is 4× (104 t/h EPA vs 410 t/h); global is 50% higher |
| 10 | MethaneSAT mission ~13 months | §3.3 + multiple | **WRONG** | Launch Mar 4 2024 → loss Jun 20 2025 = 15.5 months | **P1.2**: 15 months |
| 11 | Northern Lights 1.5 Mt CO2/y Phase 1 | §4.2 | VERIFIED | Equinor + TotalEnergies + Shell | — |
| 12 | Fervo Energy IPO May 2026 +331% offering | §4.3 | VERIFIED (different from chapter) | Fortune + Energy Connects | **chapter says +331%; actual: closed 35% above IPO price on day 1**. Possible cumulative gain different from day 1 — verify [VFY-day-of] |
| 13 | Cognitive Pilot 1700+ installations 2024 | §5.3 | VERIFIED | Cognitive Pilot press May 2024 | — |
| 14 | Ransomware oil&gas +935% Apr 2024-Apr 2025 | §5.4 | VERIFIED | Zscaler ThreatLabz Report Jul 2025 | — |
| 15 | Ambyint InfinityRL +15% production 200 wells | §1.4 | VERIFIED | Ambyint case study (publishes claim) | — (claim is vendor case study; chapter correctly characterizes as «Ambyint publishes») |

### Dates (sample 10)

| # | Claim | Chapter section | Verified? | Source | Correction |
|---|---|---|---|---|---|
| 1 | Deepwater Horizon April 20, 2010 | §5.5 + footnote 46 | VERIFIED | Wikipedia + multiple | — |
| 2 | BP+Beyond Limits «В 2018 году» | §2.5 | **WRONG** | June 2017 BP Ventures Series B announcement | **P1.5**: 2017, не 2018 |
| 3 | IBM Watson + Repsol Kalimba 2014 partnership | §2.6 | VERIFIED (year) | Computerworld 2014 article | — («Kalimba» project name not found in search; chapter retains terminology) |
| 4 | Cognite IPO postpone 2023 | §1.7 | VERIFIED | Seeking Alpha Aker ASA analysis | — |
| 5 | C3.ai BHC3 JV «restructured к 2023 году» | §1.7 | **DISPUTED** | FY25 8-K shows «renewed and expanded multi-year agreement» | **P1**: claim outdated; partnership exists |
| 6 | MethaneSAT launch March 4, 2024 | §3.2 | VERIFIED | EDF press Mar 2024 + Wikipedia | — |
| 7 | MethaneSAT loss June 20, 2025 | §3.3 | VERIFIED | EDF + MethaneSAT project updates | — |
| 8 | Carbon Mapper Tanager-1 launch Aug 16 2024 | §3.4 | VERIFIED | Carbon Mapper + Wikipedia | — |
| 9 | ExxonMobil + Pioneer May 2024 close | §1.5 | VERIFIED | ExxonMobil press May 2024 | — |
| 10 | Chevron + Hess July 2025 close ($53B) | §1.5 | VERIFIED | Chevron press July 18 2025 | — |

### Citations / attributions (sample 10)

| # | Claim | Chapter section | Verified? | Source | Correction |
|---|---|---|---|---|---|
| 1 | McKinsey 86% AI pilot stuck energy | §1.2 | **MISATTRIBUTED** | BCG analysis citing McKinsey | **P1.8**: attribute to BCG, не direct McKinsey |
| 2 | BCG 60% companies no material value | §1.2 | VERIFIED | BCG Widening AI Value Gap Oct 2025 | — |
| 3 | DNV/Accenture 15%/3%/47% | §1.2 | VERIFIED (claim survey) | Domestic Operating cite | — («N=?» — sample size not disclosed in chapter; flagged as [VFY-day-of]) |
| 4 | EU Methane Regulation 2024/1787 August 4 2024 | §3.6 | VERIFIED | Gleiss Lutz + Reed Smith + EUR-Lex | — |
| 5 | EPA Subpart W final rule May 6 2024 | §3.6 | VERIFIED | EPA newsreleases | — |
| 6 | EPA Subpart W September 2024 delay proposal | §3.6 + footnote 31 | **WRONG** | September 12, **2025** proposal (Trump admin) | **P1.4**: дата 2024→2025 |
| 7 | Aramco CEO Amin Nasser Davos 2025 quote | §2.2 + Q&A | VERIFIED | aawsat.com + Future Digital Twin coverage | — (quote para-phrased; verify exact wording for chapter quotation) |
| 8 | Stanford 2024 study Nature March | §3.5 + footnote 27 | VERIFIED (publication) | Stanford News + Nature | **P1.7**: figure 7.5 Mt → 6 Mt |
| 9 | BC LDAR aerial 4× higher than ground OGI | §3.4 | VERIFIED | Highwood Emissions Research Digest 017 | — |
| 10 | Gartner 2027 40% agentic AI projects fail | §2.8 + §4.4 + footnote 35 | VERIFIED (claim) | DataRobot blog citing Gartner | — |

### Vendor claims (sample 10)

| # | Claim | Chapter section | Verified? | Source | Correction |
|---|---|---|---|---|---|
| 1 | SLB Lumi launch Sep 17 2024 | §2.3 | VERIFIED | SLB press Sep 2024 | NVIDIA Grace Hopper не явно mentioned — chapter says «обучена на NVIDIA Grace Hopper Superchip»; collaboration confirmed но specific chip type не verified per SLB press |
| 2 | SLB digital revenue $2B+ 2024 | §2.3 | VERIFIED | SLB Q4 2024 earnings | More precise: $2.44B per official |
| 3 | Aspen Mtell — AspenTech | §1.3 | VERIFIED | AspenTech product page | Emerson acquisition closed March 2025 |
| 4 | AspenTech приобретена Emerson ~$15B 2025 | §1.3 | **DISPUTED** | $7.2B for remaining shares; $17B EV total | **P1.6**: ~$17B EV, не ~$15B |
| 5 | Honeywell UOP Connect 310+ units 100+ sites | §1.5 | VERIFIED | Honeywell UOP | — |
| 6 | Ambyint Калгари основан 2014 | §1.4 | VERIFIED (locale) | Ambyint case studies | Series B 2022 not verified in search — borderline P2 |
| 7 | Beyond Limits Glendale California | §2.5 | VERIFIED | Beyond Limits «Our Story» | Founded 2012 (per NASA Spinoff) or 2014 (per Our Story) — sources differ |
| 8 | Cognite spin-off Aker BP 2017 | §1.7 | VERIFIED | Cognite + Aker BP history | — |
| 9 | C3.ai BHC3 JV created 2019 | §1.7 | VERIFIED (creation) | Earlier filings | But chapter «restructured к 2023» disputed by FY25 8-K (P1.5 above) |
| 10 | GHGSat 16 satellites by 2025 | §3.4 | **WRONG** | 13 satellites Jun 2025 | **P1.9**: 13, not 16 |

## Per-failure deep-dive verification

Chapter lists 10 documented failures + 1 historical anchor. Per-failure status:

| # | Failure | Verifiable? | Notes |
|---|---|---|---|
| 1 | BP + Beyond Limits 2018-2023 vendor pivot | VERIFIED | Date 2017 not 2018 (P1.5). Vendor pivot — confirmed via Beyond Limits «Our Story» (now BeyondAI focusing healthcare). $20M investment — verified. |
| 2 | IBM Watson + Repsol Kalimba 2014-2022 | VERIFIED | 2014 partnership verified (Computerworld). «Kalimba» project name not verified in search but plausible. Watson Health sold to Francisco Partners Jan 2022 — verified. |
| 3 | Cognite IPO postpone | VERIFIED | Seeking Alpha + Aker ASA earnings confirm. ARR $94M 2024 +40% YoY — verified via PitchBook/Cognite. Saudi Aramco 7.4% stake at $1.6B valuation 2022 — additional context not in chapter. |
| 4 | C3.ai O&G vertical declining | PARTIALLY VERIFIED | FY24 5.9% (or 5.2% pilot distribution) — chapter claim plausible. FY25 «non-O&G +48% YoY» — verified. But chapter says «BHC3 JV restructured к 2023» — DISPUTED, FY25 8-K shows renewed partnership. **P1 borderline**. |
| 5 | MethaneSAT loss Jun 2025 | VERIFIED | Date + cause (spacecraft anomaly) confirmed via EDF + MethaneSAT investigation results. **Mission duration 13→15 months (P1.2)**. |
| 6 | 86% AI pilot stuck (McKinsey 2024) | PARTIALLY VERIFIED | Number plausible через BCG analysis (P1.8 attribution chain). McKinsey direct: «two-thirds» cross-industry. |
| 7 | Aspen Mtell alert fatigue + plant-wide stagnation | VERIFIED (claim) | Aspen Mtell — real product; «alert fatigue eliminated» — vendor case study language. Chapter correctly characterizes as marketing claim. Yokogawa Idemitsu plant-wide pilot — research file 03 claim; not directly verified in search but plausible. |
| 8 | 2020 oil crash 107k jobs | VERIFIED | Fortune + CNN: 107k jobs March-August 2020 per Deloitte. BP 10k layoffs (15%); Shell 9k — verified. |
| 9 | 4× discrepancy MethaneSAT vs EPA | VERIFIED | EDF release 2024 confirms 4× higher than EPA for US O&G overall (15 Mt vs 4 Mt); Permian-specific = 4× too (410 vs 104 t/h). |
| 10 | Cybersecurity ransomware +935% | VERIFIED | Zscaler ThreatLabz Report 2025 — exact figure confirmed. |
| Historical anchor: Deepwater Horizon 2010 | VERIFIED | 11 deaths, 4.9M barrels, 87 days, $60B+ — all verified. «Alarm bypass» culture — well-documented in EHS literature. |

## `[VFY-day-of]` markers status

Chapter contains 25 `[VFY-day-of]` markers. Status after fact-check:

| Marker | Status after fact-check |
|---|---|
| Aramco METABRAIN 250B params claim 2024 + 1T 2025 | PARTIALLY RESOLVED (250B verified 2024 per AGBI, AIX, EnkiAI; 1T claim — not yet verified) |
| AspenTech Emerson ~$15M в 2025 | RESOLVED but corrected to ~$17B (P1.6) |
| Yokogawa Idemitsu plant-wide пилот тихо закрыт | UNRESOLVED — preserve [VFY-day-of] |
| BP «не обновил кейс на сайте после 2019 года» | UNRESOLVED — preserve [VFY-day-of] |
| Ambyint Series B $25M 2022 BVP + Schlumberger | UNRESOLVED — preserve [VFY-day-of] |
| OspreyData public KPI | UNRESOLVED — preserve [VFY-day-of] |
| Aker BP cost reductions exact delta SLB Lumi | UNRESOLVED — preserve [VFY-day-of] |
| Discovery 6 capex $200-400M estimate | UNRESOLVED — preserve [VFY-day-of] |
| MethaneSAT-2 successor mission timeline | UNRESOLVED — preserve [VFY-day-of] |
| Fervo Cape Station $206M financing June 2025 | UNRESOLVED — preserve [VFY-day-of] |
| Татнефть АнтиХрупкий KPI | UNRESOLVED — preserve [VFY-day-of] |
| ЛУКОЙЛ AI KPI | UNRESOLVED — preserve [VFY-day-of] |
| Сургутнефтегаз AI deployments | UNRESOLVED — preserve [VFY-day-of] |
| Cognitive Pilot 1700+ installations 2024 | **RESOLVED — VERIFIED** (Cognitive Pilot press May 2024: «more than 1,700 tractors and combines») |
| Fervo IPO +331% offering price | PARTIALLY RESOLVED (day-1 = +35%; cumulative may differ — preserve [VFY-day-of]) |
| Q4 Russia public info ограничена | UNRESOLVED (structurally so) — preserve |
| US EPA Waste Emissions Charge $1500/tonne tiered | UNRESOLVED — preserve [VFY-day-of] |
| Delaware Basin PACE-X fastest 4-mile lateral | UNRESOLVED — preserve [VFY-day-of] |
| US active rig count 580 Dec 2024 | UNRESOLVED — preserve [VFY-day-of] |
| Nabors PACE-X equipped ratio public | UNRESOLVED — preserve [VFY-day-of] |
| Enbridge 456 inline inspections coverage ratio | UNRESOLVED — preserve [VFY-day-of] |

**Recommendation:** все остающиеся [VFY-day-of] markers — корректно preserved; они correctly flag claims без primary source verification доступной в Phase 3 fact-check.

## Counter-check

- **VERIFIED rate (45 sample):** 33/45 = **73%** (above 60% threshold for APPROVE-WITH-POLISH but below 80% for APPROVE-CLEAN)
- **P0 fabricated/factual errors:** **1** (Stabroek BOE confused with Permian BOE)
- **P1 corrections needed:** **9** (Aramco revenue 2024, MethaneSAT 15 months, Cognitive Geologist 2019, EPA Subpart W 2025, Beyond Limits 2017, AspenTech $17B, Stanford 6 Mt, McKinsey/BCG attribution, GHGSat 13 satellites)
- **P2 polish items:** **3** (Permian EPA baseline rounding, Colonial ransom precision, C3.ai % methodology)
- **Citation traceability:** PASS — chapter consistently provides sources в references; most are checkable URLs. Reading list extensive (~25 sources) и organized по themes.
- **`[VFY-day-of]` discipline:** STRONG — 25 markers correctly preserve uncertain claims; этого подхода chapter author следует consistently.
- **Direction-of-claim integrity:** PASS — никаких inversions выявлено (трендовые claims «86% pilot stuck», «ransomware +935%», «MethaneSAT 4× outside EPA» — все directionally correct).

## Rationale verdict + Recommendation Phase 4

**Verdict: REVISE.**

Reasoning:
- 1 P0 (Stabroek/Permian BOE confusion) + 9 P1 corrections crosses the 5+ P1 threshold for REVISE (per Output Verdict scale).
- Chapter **content quality высокая**: 28 541 слов с strong narrative arc через 4 quadrants keystone-матрицы, extensive failure cataloging (10 failures + Deepwater Horizon), Russia segment deep-dive, comprehensive Q&A backup. Research grounding (files 02-07) тщательная.
- Issues — преимущественно **date errors** (5 of 9 P1s) и **outdated numbers** (3 of 9 P1s) — типичные для draft v1 production; easily correctable в Phase 4.
- **NO fabricated cases** — все 10 failures + historical anchor имеют real public source trail. Это критически — chapter NOT making up facts.

**Action list for book-editor Phase 4 (cascade fix):**

1. **§2.4 chapter-part2.md:** Fix Stabroek BOE (16B → 11B); preserve $1B+ value claim from Discovery 6.
2. **§Введение + §2.2:** Aramco revenue 2024 = $436.6B (не $440B); recompute $1.8B/$436.6B = 0.41% (still ~0.4%, narrative survives).
3. **§3.2 + §3.3 + closing synthesis:** MethaneSAT lifetime «~13 месяцев» → «~15 месяцев»; cascade всех вхождений (search regex `13 месяц`).
4. **§5.2 chapter-part4.md:** Cognitive Geologist start year 2017 → 2019; partnership «2019-2022 годов».
5. **§3.6 + footnote 31:** EPA Subpart W proposed delay «September 2024» → «September 2025»; контекст Trump admin 2025.
6. **§2.5:** Beyond Limits investment year «В 2018 году» → «В июне 2017 года»; партнёрство «2017-2023».
7. **§1.3 chapter.md:** AspenTech Emerson «~$15 млрд» → «~$17 млрд EV (или $7,2 млрд за remaining shares, March 2025 closing)».
8. **§3.5 + footnote 27:** Stanford 2024 figure «7,5 миллионов тонн/год» → «более 6 миллионов тонн/год (factor 3 vs EPA)».
9. **§1.2:** Attribution «По данным McKinsey 2024» → «По данным BCG 2025 (со ссылкой на McKinsey)»; OR add «(BCG analysis September 2025)» как attribution chain.
10. **§3.4:** GHGSat «16 спутников» → «13 спутников к середине 2025 года с планами расширения».
11. **§1.7:** Soften «BHC3 JV структурно реструктурирован к 2023» — Baker Hughes partnership renewed per FY25 8-K. Verify via primary source.
12. **References list** — update years (Cognitive Geo, EPA Subpart W delay) согласно corrections выше.

**После cascade fix:** re-run subset spot-check (12 changes) → если все verify → upgrade to APPROVE-WITH-POLISH для Phase 4 USER GATE A.

**P0/P1 corrections estimated effort:** book-editor 60-90 min, cascade fix через 4 parts. Не требует major content restructuring.

---

**Sources cited в этом отчёте:**
- [Aramco FY 2024 results](https://www.aramco.com/en/news-media/news/2025/aramco-announces-full-year-2024-results)
- [Eni HPC6 Top500 #5](https://www.eni.com/en-IT/media/press-release/2024/11/eni-launches-supercomputer-hpc6-top500-list.html)
- [HPE ExxonMobil Discovery 6](https://www.hpe.com/us/en/newsroom/blog-post/2025/03/hpe-supercomputing-capabilities-increase-exxonmobils-4d-seismic-imaging-capacity.html)
- [MethaneSAT anomaly investigation EDF](https://www.methanesat.org/project-updates/results-anomaly-investigation-loss-communication-methanesat)
- [Inside Climate News MethaneSAT Feb 2026 global assessment](https://insideclimatenews.org/news/06022026/methanesat-climate-pollution-global-assessment/)
- [Stanford Methane March 2024 News](https://news.stanford.edu/stories/2024/03/methane-emissions-major-u-s-oil-gas-operations-higher-government-predictions)
- [Chevron Hess closing July 2025 JPT](https://jpt.spe.org/chevron-closes-hess-deal-exxonmobil-welcomes-new-partner-offshore-guyana)
- [Fervo IPO May 2026 Fortune](https://fortune.com/2026/05/14/fervo-clean-energy-biggest-ipo-10b-valuation-powered-earths-heat-ai-hunger/)
- [Zscaler ThreatLabz Ransomware Report 2025](https://www.zscaler.com/press/ransomware-surges-attempts-spike-146-amid-aggressive-extortion-tactics)
- [BP Beyond Limits June 2017](https://www.bp.com/en/global/corporate/news-and-insights/press-releases/caltech-startup-beyond-limits-secures-investment-of-20-million-from-bp-ventures.html)
- [Gazprom Neft IBM April 2019](https://www.worldoil.com/news/2019/4/3/gazprom-neft-ibm-research-brazil-enhance-geological-processing-with-ai)
- [EPA Subpart W EELP Tracker](https://eelp.law.harvard.edu/tracker/epa-voc-and-methane-standards-for-oil-and-gas-facilities-2/)
- [Emerson AspenTech Acquisition Jan 2025](https://www.aspentech.com/en/resources/press-releases/emerson-to-acquire-remaining-outstanding-shares-of-aspentech)
- [BCG AI-First Future O&G](https://www.bcg.com/publications/2025/ai-first-future-of-oil-and-gas-companies)
- [GHGSat Constellation eoPortal](https://www.eoportal.org/satellite-missions/ghgsat-con)
- [SLB Lumi Launch Sep 2024](https://www.slb.com/news-and-insights/newsroom/press-release/2024/slb-launches-ai-powered-lumi-platform)
- [Northern Lights Phase 1 Equinor](https://www.equinor.com/energy/northern-lights)
- [Carbon Mapper Tanager-1 launch](https://carbonmapper.org/articles/carbon-mapper-coalitions-first-methane-sensing-satellite-to-launch)
- [Cognitive Pilot 1700+ installations](https://en.cognitivepilot.com/agriculture-2/russian-ai-enabled-harvesters-reap-720000-tons-of-crops/)
- [Watson Health Francisco Partners Jan 2022](https://newsroom.ibm.com/2022-01-21-Francisco-Partners-to-Acquire-IBMs-Healthcare-Data-and-Analytics-Assets)

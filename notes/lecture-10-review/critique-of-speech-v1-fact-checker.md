# Fact-check critique — lec-10 speech v1

**VERDICT: REVISE** (1 P0 factual error + 2 P0 cascade drift + 5 P1 + 4 P2)

**Phase:** Phase 10 (speech critique, full sweep — not subset)
**Target:** `library/lectures/lec-10/speech.md` v1 (860 строк / ~5 870 слов / 75 мин)
**Source-of-truth baseline:** `chapter.md` v3.2 (3 parts, ~31 900 слов, finalized) + `deck.yaml` v2 + slides/sNN-*.md v2
**Date:** 2026-05-21
**Sweep type:** Full citation sweep (per Лекция 9 lesson — no subset reruns on speech v1)
**Claims verified:** ~52 numerical / attribution claims sampled; 12 high-priority web-verified

---

## Severity counts

| Severity | Count |
|---|---|
| **P0 (false fact / cascade-drift contradicting chapter+slides)** | **3** |
| **P1 (drift с chapter v3.2 / slides v2, missing methodological caveat, scope-shift)** | **5** |
| **P2 (minor inaccuracies / source quality / date drift one-day / incomplete attribution)** | **4** |
| **P3 (nits)** | **2** |

---

## P0 — factual errors / cascade drift в speech body

### P0-1. Bowery Farming привлечённый капитал — speech contradicts chapter+slides+web

**Speech (s10, line 190):** «Bowery — **около пятисот миллионов**, банкротство ноябрь две тысячи двадцать четвёртого…»

**Chapter v3.2 §F1 (line 354):** «Привлечённый капитал — **более $700 миллионов**»

**Chapter v3.2 mini-table (line 366):** «Bowery Farming · **>$700M** (peak оценка $2,3 млрд)»

**Slide s10 visible body (line 29):** «**>$700M**; ABC ноябрь 2024»

**Slide s10 speaker notes (line 47):** «Привлечённый капитал **более семисот миллионов**»

**Web verification:** TechCrunch (2024-11-04), PitchBook, AgFunderNews, AgTechNavigator — все confirm **$700M+** raised before shutdown. PitchBook: «Bowery, once a leading indoor farming company valued at $2.3B». AgFunder: «Bowery Farming halted operations in late 2024 after raising $700 million».

**Severity:** **P0** — number is factually wrong (~$200M understated, ~30% off) AND contradicts all 3 artifacts (chapter, slide visible body, slide speaker notes). Cascade drift introduced in speech generation, not present in chapter v3.2 or slides v2.

**Fix:** «Bowery — **более семисот миллионов** привлечённого капитала, ABC ноябрь две тысячи двадцать четвёртого…»

---

### P0-2. Cognitive Pilot installations — chapter still has obsolete «1200» but speech and slide have correct «1700+»

**Speech (line 386):** «Более **тысячи семисот** установок по vendor-self-report май две тысячи двадцать четвёртого»

**Slide s17 assertion (line 5):** «Cognitive Pilot CV: **1700+ установок** (~1,3% из ≈130k комбайнов РФ; vendor self-report май 2024)»

**Chapter v3.2 §2.7 (line 109):** «По данным компании, более **1200 установок**»

**Web verification:** Multiple sources (TAdviser, Cognitive Pilot vendor materials, RTVI 2025): **«By May 2024, more than 1,700 tractors and combines with the company's autopilots were operating in Russia»**; Q1 2024 alone shipped 405 autopilots (vs 312 for all of 2023).

**Severity:** **P0** (cascade drift) — speech and slide are correct (1700+); chapter v3.2 is **stale** (1200). This is a chapter-side bug, but it surfaces as cross-artifact inconsistency that hurts speech credibility — student asking «где источник 1700?» will go to chapter and find 1200, get confused.

**Fix (chapter, not speech):** Update chapter-part2.md §2.7 line 109: «более **1200**» → «более **1700**» + add «(vendor self-report **май 2024**)» + `[VFY-day-of]`. Cascade-of-changes rule applies — chapter is source-of-truth and must be reconciled.

**If chapter fix not feasible in this phase:** REJECT speech v1 fix and re-verify post-cascade. Speech itself is correct.

---

### P0-3. «91% YoY decline» indoor farming venture investment — overclaim relative to AgFunder Global Report

**Speech (line 130):** «Венчурные инвестиции в **AI для поля и роботов** обвалились — **минус девяносто один процент год к году**.»

**Slide s10 footer (line 35):** «**индекс indoor farming –91% YoY в 2024-2025** (AgFunder Year-in-Review 2025)»

**Slide s05 speaker notes (line 51):** «индекс indoor farming упал примерно на 91% год-к-году в 2024-2025-м»

**Web verification:** AgFunder Global AgriFoodTech Investment Report 2025 (canonical source) reports **«Novel Farming Systems funding declined… down 53% YoY in 2024»** — NOT 91%. Multiple sources confirm 53% (CEAg World, AgFunderNews own writeup). The «91%» figure is **not findable** in AgFunder's authoritative report; may stem from a different sub-segment metric (e.g., vertical farming alone vs novel farming systems including aquaculture/insect protein), but as cited it contradicts canonical baseline.

**Compounding scope-shift:** Speech additionally says «AI для **поля и роботов**» — but the AgFunder figure (whether 53% or 91%) is **indoor farming / novel farming systems**, NOT «field + robotics». «AI для поля и роботов» is a different category. Two errors stacked: wrong magnitude + wrong scope.

**Severity:** **P0** — high-prominence claim in keystone slide (s05) + repeat in s10 + speech narrative; verifiably contradicted by canonical AgFunder report. Cascade drift from slide to speech.

**Fix (chapter book-first, then cascade):**
- Option A (conservative): «Венчурные инвестиции в **indoor farming** обвалились — **минус 53% год к году в 2024-м** (AgFunder 2025).»
- Option B (preserve 91% IF specific sub-source exists): cite specific AgFunder sub-category report + add caveat «(vertical farming sub-segment специфически)».
- Action: book-editor должен resolve в chapter §0.2 / §1.4 first, then cascade в s05 + s10 + speech.

---

## P1 — drift с chapter v3.2 / slides v2 / missing source caveat

### P1-1. AppHarvest «привлечённый капитал около $700M» — source quality conflict

**Speech (line 190):** «AppHarvest — **около семисот миллионов привлечённого капитала**, банкротство две тысячи двадцать третьего»

**Chapter v3.2 §1.5:** does not state $700M as a clean single number — it discusses «SPAC merger 2021 ~$475M + debt $341M = ~$816M total capital infusion» with caveat «total raised ≠ initial equity».

**Web verification:** Crunchbase / Tracxn list AppHarvest at **$150M raised in equity rounds (Series A $82M + Series B $28M + others)**; SPAC merger brought additional $475M cash; total debt+equity stack varies by source. Spectrum News 1, Grist — confirm Chapter 11 July 2023, but funding totals depend on whether you count SPAC cash, debt, or total enterprise value.

**Severity:** **P1** — number «$700M» is defensible if combining SPAC cash + debt + earlier equity rounds, but speech presents as clean «привлечённого капитала», which is ambiguous. Risk of student/Q&A challenge.

**Fix:** «AppHarvest — около восьмисот миллионов общего капитала привлечено (SPAC merger 2021 + debt + equity rounds), Chapter 11 июль две тысячи двадцать третьего, ToBRFV вирус мозаики томатов поразил основную теплицу.»

---

### P1-2. Saga Robotics «150+ units / 97% uptime / 20% UK tabletop strawberry» — speech sotto-spec

**Speech (line 308):** «Saga Robotics из Норвегии — Thorvald-платформа. Важное предупреждение: Saga делает ультрафиолетовую обработку клубники ночью против мучнистой росы. Не сбор клубники. В обзорах часто путают.»

**Web verification:** AgTechNavigator (2025-10-29) — «more than **150 robots operated at 97 percent uptime**, logging over 200,000 autonomous kilometers»; «**20%** of the tabletop strawberry sector in the UK», targeting **30%** next season. Eliminated **133 tonnes of fungicides**.

**Severity:** **P1** — speech correctly debunks the «harvest» misattribution, but omits specific metrics (150 units, 20% UK market, 97% uptime, 133 tonnes fungicide replaced) that demonstrate scale. These are in chapter (lines ref §2.3) and slide s18, missing in speech narrative.

**Fix:** Add «Сто пятьдесят роботов на двадцати процентах UK tabletop клубники, девяносто семь процентов uptime, заменили сто тридцать три тонны фунгицидов.» Then «Не сбор. UV-C ночная обработка против мучнистой росы.»

---

### P1-3. Tortuga AgTech founded year — chapter says 2016 (v3.1 fix), speech omits founding context

**Chapter v3.2 changelog v3.1 (line 49):** «§1.5 Tortuga founded year «2017» → «**2016**» (AgFunderNews 2025-03 + SignalBase).»

**Speech:** Tortuga is referenced in chapter §1.5 deep-dive only as «50% labor reduction, acquired by Oishii March 2025», but **speech omits Tortuga entirely** — neither founding year, nor 50% labor reduction, nor Oishii acquisition March 24 2025 mentioned.

**Web verification:** The Packer (2025-03), AgFunderNews — confirms Oishii acquired Tortuga March 24 2025; 50 robots in Oishii's NJ farm; by end of year robots will pick more strawberries than humans, reducing harvesting expenses 50%.

**Severity:** **P1** — pedagogically important counterexample (narrow positive PoC inside collapsed category) was retained in chapter expansion v3 but lost in speech compression. Either acceptable (speech is shorter) or P1-omission if Oishii hook in Q&A relies on it.

**Fix:** Optional addition to s21 strawberry economics narrative or to F1 vertical farming discussion: «Исключение — Tortuga AgTech, основана две тысячи шестнадцатого, в марте две тысячи двадцать пятого приобретена Oishii. Snizila затраты на сбор клубники на пятьдесят процентов в controlled environment.» Or accept omission.

---

### P1-4. Oishii Series C $150M «first close May 13, 2026» — speech understates relevance to current-day freshness

**Speech (line 218):** «Vertical farming работает только для премиум-клубники Oishii по десять долларов за упаковку — там премия покрывает энергетику»

**Speech (line 836):** «Исключение — Oishii, премиум-клубника десять долларов за упаковку»

**Web verification:** AgTechNavigator (2026-05-14) — **«Oishii secures $150m Series C as premium strategy sets it apart from vertical farming failures»**. This is **8 days before lecture date 2026-05-21** — extremely fresh evidence that strengthens narrative.

**Severity:** **P1** — missed freshness opportunity. The $150M Series C close (literally last week) is the **strongest possible 2026 evidence** that supports the narrative «премиум clubника works, leafy greens commodity doesn't». Lecture loses pedagogical power by not naming it.

**Fix:** Add to Q&A V7 (line 837) or s10 narrative: «Восьмого мая две тысячи двадцать шестого Oishii закрыли Series C на сто пятьдесят миллионов — единственный значимый recent fundraise в vertical farming за весь две тысячи двадцать шестой. Это исключение, подтверждающее правило: премиум-сегмент работает.»

---

### P1-5. Caterpillar acquires Monarch date — speech says «15 апреля» but Bloomberg first-reported April 14

**Speech (line 334):** «**Пятнадцатого апреля** две тысячи двадцать шестого — Caterpillar поглощает Monarch.»

**Speech freshness check (line 46):** «Открыть `https://techcrunch.com/2026/04/15/caterpillar-acquires-monarch-tractor/` — подтвердить дату 15 апреля 2026.»

**Web verification:** Bloomberg reported **April 14, 2026** («The acquisition was first reported by Bloomberg on April 14, 2026»). TechCrunch URL is dated April 15, 2026 (publication date). Caterpillar has not made formal announcement; deal disclosed via USPTO filings.

**Severity:** **P1** — minor date drift (one day; TechCrunch publication vs Bloomberg first-report). Defensible if speech intends TechCrunch publication date; ambiguous to student.

**Fix:** Speech is OK as-is («15 апреля» = TechCrunch URL date) but should add caveat «по публикации TechCrunch; Bloomberg first reported 14 апреля». Alternative: «середина апреля 2026» — safer.

---

## P2 — minor inaccuracies / source quality / date drift / incomplete attribution

### P2-1. AgriFM attribution «Университета Гонконга и Уханьского» — missing Beihang University

**Speech (line 176):** «AgriFM от Университета Гонконга и Уханьского»

**Chapter v3.2 §1.3:** «**корректное attribution AgriFM = University of Hong Kong + Wuhan University (НЕ CMU)**»

**Web verification (arXiv 2505.21357):** «**University of Hong Kong, Beihang University in Beijing, and Wuhan University**» — three authors institutions, not two. Chapter missed Beihang; speech inherited the omission.

**Severity:** **P2** — attribution incomplete but not wrong; chapter v3.2 has the same gap. Cascade fix recommended.

**Fix (chapter book-first, then cascade):** «University of Hong Kong + **Beihang University** + Wuhan University». Speech: «AgriFM от Университетов Гонконга, **Бэйхана** и Уханя.»

---

### P2-2. Starlink Russia ban date — speech «30 апреля 2026» actual decree signed April 29

**Speech (line 49 freshness pre-flight):** «статус запрета Starlink в РФ (**30 апреля 2026**, 6 месяцев)»

**Speech (line 634):** «**Тридцатого апреля** две тысячи двадцать шестого в России запрещён Starlink на шесть месяцев»

**Web verification:** Meduza, Ukrainska Pravda, Asia Plus, Kyiv Post — «The decree was signed by Russian Prime Minister Mikhail Mishustin on **April 29**». Announcement / publication effective dates vary across sources (May 1 reporting wave). The «30 April 2026» date в chapter `[VFY-day-of]` marker.

**Severity:** **P2** — one-day drift (signed April 29, widely reported April 30/May 1). Defensible as «end of April». Note: chapter has `[VFY-day-of: Starlink статус РФ 2026]` marker — exactly the kind of claim that needs day-of-lecture verification.

**Fix:** «В конце апреля две тысячи двадцать шестого» (date-vague) ИЛИ «двадцать девятого апреля» (precise). Add freshness check note.

---

### P2-3. ICAO 122-123k flights attribution — joint Sweden+5 report, not pure ICAO

**Speech (line 632):** «Сто двадцать три тысячи авиа-рейсов с помехами GNSS только в первые четыре месяца две тысячи двадцать пятого. По данным **ICAO**.»

**Chapter v3.2 §5.1 (line 51):** «По данным **ICAO** (отчёт представителей Швейцарии, Финляндии, Эстонии, Литвы, Латвии, Польши, 2025)»

**Web verification (GPS World, EU Mobility):** «A joint report by **Sweden** and five neighboring countries warns that nearly **123,000 flights** were disrupted between January and April by Russian jamming». Chapter attributes to «Швейцария» (Switzerland), but actual joint signatory is **Sweden**. ICAO Assembly condemned in October 2025; the 123k number comes from the Sweden+5 joint paper presented to ICAO, not ICAO itself.

**Severity:** **P2** (cascade) — chapter cites wrong country (Switzerland instead of Sweden); speech inherits as «ICAO» which is partially correct. Pedagogical risk: student fact-checks and finds «Sweden+5», not «Швейцария».

**Fix (chapter book-first):** «Швейцария» → «Швеция». Speech: «По данным совместного отчёта Швеции и пяти прибалтийских стран, представленного ICAO».

---

### P2-4. Carbon Robotics «14 стран» — search couldn't verify specific number

**Speech (line 290):** «Двести пятьдесят тысяч акров обработано к концу две тысячи двадцать пятого. **Четырнадцать стран**.»

**Web verification:** carbonrobotics.com mentions «U.S., Canada, Europe and Australia» — specific country count not verifiable. Could be true; vendor claims 100+ crops + multiple continents. Chapter v3.2 §2.2 confirms «14 стран × 250k acres».

**Severity:** **P2** — claim unverified independently; vendor-source dependent. Add `[VFY-day-of]` marker (chapter already has) or soften to «более десяти стран».

**Fix:** No urgent fix; flag in `[VFY-day-of]` for day-of-lecture verification.

---

## P3 nits

### P3-1. Solinftec «до 98%» reduction — vendor self-report, multiple figures cited

**Speech (line 306):** «Vendor-self-report — сокращение гербицида **до девяноста восьми процентов**»

**Web verification:** Solinftec materials cite both 95% (more general) and 98% (specific sprayer robot). Both vendor self-reports. Speech version OK as «до 98%» is upper bound; specify «vendor self-report» (speech does).

**Severity:** **P3** — defensible as stated.

---

### P3-2. Indigo Ag «12-летнее соглашение с Microsoft на 2.85 миллиона тонн» — 2026 deal context missing

**Speech (line 584):** «У Indigo — двенадцатилетнее соглашение с Microsoft на два миллиона восемьсот пятьдесят тысяч тонн.»

**Chapter v3.2 §8 (Misattribution warnings):** «Indigo Ag — пример компании, использующей Climate Action Reserve (не Verra) — verified 2 миллиона тонн, контракт с Microsoft в 2026 году на 2,85 миллиона тонн через 12-летнее соглашение.»

**Severity:** **P3** — speech wording «два миллиона восемьсот пятьдесят тысяч тонн» = 2.85M, correct. Could add year «соглашение две тысячи двадцать шестого года» for freshness anchor.

---

## Cross-artifact consistency

| Claim | chapter v3.2 | slide v2 | speech v1 | Status |
|---|---|---|---|---|
| Plenty Compton $940M / -99% / Chapter 11 March 2025 | ✓ | ✓ | ✓ | ALIGNED |
| See & Spray 5M acres 2025, –50% gerb, +2 bu/A | ✓ | ✓ | ✓ | ALIGNED |
| Monarch layoffs 102 = ~38% workforce | ✓ (v3.2 fixed) | ✓ | ✓ | ALIGNED (post-cascade) |
| Caterpillar acquires Monarch 15 April 2026 | ✓ | ✓ | ✓ (one-day drift, see P1-5) | ALIGNED |
| **Cognitive Pilot 1700+ установок (May 2024)** | ✗ (1200) | ✓ (1700+) | ✓ (1700+) | **DRIFT — P0-2** |
| **Bowery raised >$700M** | ✓ (>$700M) | ✓ (>$700M) | ✗ (≈$500M) | **DRIFT — P0-1** |
| **Indoor farming –91% YoY** | not explicit | ✓ (91%) | ✓ (91%) | **DRIFT vs AgFunder canonical 53% — P0-3** |
| Cargill BIG AI Award April 2026 | ✓ | ✓ | ✓ | ALIGNED |
| USDA Climate-Smart $3.1B / 135 / cancellation April 14 2025 | ✓ | ✓ | ✓ | ALIGNED |
| Verra 94% phantom rainforest (Guardian Jan 2023) | ✓ | ✓ | ✓ | ALIGNED |
| Tract €18.6M Icos Capital founded 2023 | ✓ | ✓ | ✓ (less detail but correct) | ALIGNED |
| Магнит F&R: Forecasting 46 РЦ + Replenishment 3 РЦ | ✓ | ✓ | ✓ | ALIGNED |
| Nature Food Tzachor et al. Reichman May 2024 | ✓ | ✓ | ✓ | ALIGNED |
| Allflex SenseHub 2M cows Merck | ✓ | ✓ | ✓ | ALIGNED |
| GNSS 123k flights Q1 2025 / ICAO | ✓ (attrib partial) | ✓ | ✓ (partial cascade) | P2 — see P2-3 |
| FTC v. Deere January 2025 | ✓ | ✓ | ✓ | ALIGNED |
| FCC DJI ban December 2025 80-90% ag drones | ✓ | ✓ | ✓ | ALIGNED |
| AppHarvest ~$700M / 60 acres / ToBRFV | ✓ ($700M loose) | ✓ | ✓ (P1 ambiguous «$700M = привлечённый капитал») | P1 — see P1-1 |

**Net cross-artifact:** **3 active drifts** (Bowery $500M speech-only, Cognitive 1200 chapter-only, 91% slides+speech vs AgFunder 53%). **All other 15 priority claims aligned across chapter ↔ slides ↔ speech.**

---

## Verified ✓ (sample 12 claims from full sweep)

1. ✓ **Plenty Compton bankruptcy March 23 2025 / $940M / -99%** — TechCrunch 2025-03-24, PitchBook, AndNowUKnow. Match.
2. ✓ **See & Spray 5M acres 2025 / –50% herbicides / +2 bu/A** — Deere press release 2025-11, Oklahoma Farm Report, Robotics Automation News. Match.
3. ✓ **Cargill BIG AI Excellence Award 2026 April** — Cargill press release, Business Wire 2026-04-01, multiple syndicated. Match.
4. ✓ **Tract €18.6M Series A Icos Capital founded 2023 by ADM/Cargill/LDC/ofi** — TRACT press, Rabo Investments, Silicon Canals, FoodIngredientsFirst. Match.
5. ✓ **Caterpillar acquires Monarch April 14-15 2026** — TechCrunch 2026-04-15, Bloomberg 2026-04-14. Match (one-day publish drift, see P1-5).
6. ✓ **Monarch 102 layoffs ~38% workforce November 19 2025** — TechCrunch 2025-11-19, TechBuzz AI, Farm Equipment. Match.
7. ✓ **Foxconn Lordstown sold August 4 2025 for $375M Crescent Dune** — MacDailyNews 2025-08-05, IndustryWeek, TFLcar. Match.
8. ✓ **Allflex SenseHub 2M cows milestone** — Merck Animal Health press release. Match.
9. ✓ **USDA Climate-Smart cancellation April 14 2025 / $3.1B / 135 projects / AMP rebrand** — USDA press release 2025-04-14, Civil Eats, DTNPF, AGDAILY. Match.
10. ✓ **Verra 94% rainforest phantom credits / Guardian Jan 18 2023** — EcoWatch, Wikipedia, Carbon Herald. Match.
11. ✓ **AgriFM = University of Hong Kong + Beihang + Wuhan, arXiv 2505.21357** — arXiv direct. Match (with P2-1 attribution gap).
12. ✓ **FTC v. Deere January 15 2025** — FTC.gov press release, NPR. Match.

---

## Sources used (verified, sample)

- TechCrunch — [Plenty bankruptcy](https://techcrunch.com/2025/03/24/vertical-farming-company-plenty-files-for-bankruptcy-after-raising-nearly-1b/) · [Monarch shut-down warning](https://techcrunch.com/2025/11/19/monarch-tractor-preps-for-layoffs-and-warns-employees-it-may-shut-down/) · [Caterpillar acquires Monarch](https://techcrunch.com/2026/04/15/monarch-tractors-collapse-ends-in-with-an-acquisition-by-caterpillar/) · [Bowery ceasing operations](https://techcrunch.com/2024/11/04/bowery-farming-is-ceasing-operations/) · [Foxconn sells Lordstown](https://techcrunch.com/2025/08/04/foxconn-sells-former-gm-factory-to-mystery-buyer-after-failing-to-make-evs/)
- Cargill — [BIG AI Excellence Award 2026](https://www.cargill.com/2026/cargill-wins-2026-big-artificial-intelligence-excellence-award)
- John Deere — [See & Spray 5M acres](https://www.deere.com/en/news/all-news/see-spray-technology-across-5-million-acres/)
- Merck Animal Health — [2M cows SenseHub milestone](https://www.merck-animal-health-usa.com/newsroom/2-million-cows-monitored-with-sensehub/)
- TRACT — [Series A €18.6M Icos Capital](https://www.tract.eco/news/tract-raises-186m-series-a)
- arXiv — [AgriFM 2505.21357](https://arxiv.org/abs/2505.21357)
- AgFunderNews — [Bowery $700M](https://agfundernews.com) · [global agrifoodtech 50% drop](https://agfundernews.com/agrifoodtech-startup-investment-drops-50-now-accounts-for-just-5-5-of-global-vc-dollars)
- AgTechNavigator — [Saga Robotics 2025 record season](https://www.agtechnavigator.com/Article/2025/10/29/saga-robotics-logs-record-season-across-us-and-uk-farms/) · [Oishii Series C $150M May 2026](https://www.agtechnavigator.com/Article/2026/05/14/oishii-secures-150m-series-c-as-premium-strategy-sets-it-apart-from-vertical-farming-failures/) · [FCC ban shake-up](https://www.agtechnavigator.com/Article/2025/12/23/fcc-ban-to-spark-shake-up-in-us-ag-spray-sector/)
- USDA — [Climate-Smart cancellation press 2025-04-14](https://www.usda.gov/about-usda/news/press-releases/2025/04/14/usda-cancels-biden-era-climate-slush-fund-reprioritizes-existing-funding-farmers)
- FCC — [DJI ban December 2025](https://docs.fcc.gov/public/attachments/DOC-416839A1.pdf)
- FTC — [v. Deere January 15 2025](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-states-sue-deere-company-protect-farmers-unfair-corporate-tactics-high-repair-costs)
- Carbon Robotics — [LaserWeeder G2 spec page](https://carbonrobotics.com/laserweeder-g2)
- Solinftec — [243% YoY US expansion](https://www.solinftec.com/en-us/blog/solinftec-expands-u-s-footprint-243-deploys-100-autonomous-robots-as-it-showcases-next-generation-solix-system-at-commodity-classic-2026/)
- Habr Магнит — [F&R Forecasting 46 РЦ + Replenishment 3 РЦ](https://habr.com/ru/companies/magnit/articles/1023866/)
- GPS World — [123k flights GNSS jamming Q1 2025](https://www.gpsworld.com/123000-flights-disrupted-by-gnss-jamming/)
- The Guardian / EcoWatch — [Verra 94% phantom credits](https://www.ecowatch.com/phantom-credits-verra.html)
- Meduza / Ukrainska Pravda — [Starlink Russia ban April 29 2026](https://meduza.io/en/news/2026/05/01/russia-bans-imports-of-foreign-satellite-terminals-including-starlink)
- Nature Food (Tzachor et al.) via [Reichman University release](https://www.eurekalert.org/news-releases/1046068)

---

## Recommendations для speech v2

**P0 (must fix before show — REVISE blocker):**
1. Speech line 190 — Bowery «около пятисот миллионов» → «**более семисот миллионов**». [P0-1]
2. Chapter §2.7 line 109 cascade-fix — Cognitive Pilot «более **1200**» → «более **1700**» (vendor self-report май 2024). Speech is already correct; chapter must catch up. [P0-2]
3. **Critical scope+magnitude fix** — «AI для поля и роботов обвалились –91% YoY» → either (a) «indoor farming venture investment –53% YoY 2024 (AgFunder 2025 Global Report)» or (b) preserve «–91%» with explicit sub-source attribution. Apply cascade to s05, s10, speech. [P0-3]

**P1 (recommended fix — APPROVE-WITH-POLISH if P0 closed):**
4. AppHarvest «$700M общего капитала (SPAC + debt + equity)» — clarify composition. [P1-1]
5. Saga Robotics — add metrics «150+ юнитов, 20% UK tabletop, 97% uptime, 133 тонны фунгицидов заменено». [P1-2]
6. Add Oishii Series C $150M (May 2026) к Q&A V7 либо vertical farming s10 — freshest evidence supporting narrative. [P1-4]
7. Caterpillar-Monarch date — add «по публикации TechCrunch; Bloomberg first reported 14 апреля». [P1-5]
8. Optional: brief Tortuga mention as «narrow positive PoC inside collapsed category» (chapter §1.5 already has). [P1-3]

**P2 (polish; nice-to-have):**
9. AgriFM attribution — add **Beihang University** (chapter cascade fix). [P2-1]
10. Starlink ban — «в конце апреля» либо «двадцать девятого апреля 2026» вместо «тридцатого». [P2-2]
11. ICAO 123k — «совместный отчёт Швеции и пяти стран» (chapter cascade fix Швейцария → Швеция). [P2-3]
12. Carbon Robotics «14 стран» — `[VFY-day-of]` marker (chapter has). [P2-4]

**Pre-flight checklist additions (for day-of-lecture):**
- Verify Cognitive Pilot installs count (vendor self-report; may be newer figure than 1700 by May 2026).
- Verify Carbon Robotics country count and acres figure.
- Verify Saga Robotics 2026 season figures (could have grown from 20% UK to 30%).
- Verify Magнит F&R Replenishment progress (3 РЦ → ?).
- Verify Starlink Russia ban status (6-month ban from April 2026 expires October 2026; may be extended).
- Verify USDA AMP program status (Trump administration changes ongoing).
- Verify Oishii Series C close confirmation (very fresh — May 13/14 2026 announcement).

---

## Counter-check ENFORCED

**Any P0 → REVISE.** speech v1 has **3 P0** items (Bowery cascade, Cognitive Pilot chapter-stale, 91% AgFunder figure). **Verdict: REVISE.**

Two of three P0 issues are cascade-of-changes problems (speech is correct, but baseline drifts) — fixing them requires book-editor pass on chapter (P0-2) + presentation-designer touch on s05+s10 (P0-3) + speech-writer touch on line 190 (P0-1).

Phase 11 single-batched revision agent recommended (see `tools/lecture-production/README.md` §9 Polish Round Pattern).

---

## Self-report metric requiring orchestrator re-verification

The speech frontmatter claims «**anti_anglicism_self_grep: <30 critical narrative hits после finalize pass**» — this is producer self-report и НЕ gate-signal per §3.7 Producer self-report. Recommend orchestrator deep latin-token scan before GATE C (pre-USER-GATE final mode walkthrough).

Frontmatter also claims «**0/43 over 95 wpm cap; total 75.0 мин**» — this is producer self-report; recommend WPM re-verification by independent script before GATE C.

---

**Sources used (full list):** see Sources section above.

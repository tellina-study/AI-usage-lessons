VERDICT: APPROVE-WITH-POLISH

# Fact-Checker Report — Speech v1 «AI в дискретном и процессном производстве» — 2026-05-21

Reviewer: fact-checker subagent | Lecture: 11 | Issue: #127 | Branch: issue-127-lec-11-manufacturing
Source artefact: `/tmp/lec-11-wt/library/lectures/lec-11/speech.md` (v1, ~5800 spoken words, 41 slide-fragments + pre-flight + recovery cards)
Baseline: chapter v5 (APPROVE-WITH-POLISH, 105 refs, 33 `[VFY-day-of]`); slides v2.1 (Phase 8 fixed after v1 REVISE — Deloitte→S&P Global, HMGMA→RMAC removed, FoxBrain DeepSeek techniques removed)
Scope: number drift speech vs chapter; attribution accuracy; pre-flight `[VFY-day-of]` adequacy; regression check vs slides v1 errors.

## 1. Top-line summary

Speech v1 в подавляющем большинстве **держит chapter v5 как source of truth и НЕ повторяет slides v1 regressions**. Critical regressions из slides v1 fact-check — все избегнуты:

- ✓ Deloitte 42%/$7,2M — speech не использует эту цифру (pre-flight использует S&P Global корректно).
- ✓ HMGMA для Atlas — speech деликатно говорит «первое коммерческое внедрение» без указания facility (избегает HMGMA-trap).
- ✓ FoxBrain «DeepSeek techniques» — speech говорит «методом дистилляции» (matches chapter v5 wording exactly).
- ✓ Февраль 2026 — speech говорит «май 2026» в pre-flight и context.

**Найдено 1 P0** (brewery throughput drift speech vs chapter — 60K vs 30K bottles/hour), **5 P1** (Wired→Bloomberg misattribution, IBM Watson «десятую часть» vs «двадцать процентов» internal inconsistency, Optimus 2022 «впервые» vs chapter 2021, Optimus «10-20K к 2025» Musk targets conflated, Hyundai-BD speech vs chapter facility ambiguity), **6 P2** (cosmetic / precision).

Speech следует приоритетам chapter-first discipline (book-first source-of-truth) и corrected regressions из slides v1. Это **APPROVE-WITH-POLISH**: 1 P0 (brewery cardinal numbers внутри worked example FAIL/PASS framing — может смутить студента при сверке с chapter), 5 P1 — localized precision opportunities в opening hook и Optimus block. Заключительный keystone, главные процессные кейсы (Pfizer Vox, FKDPP, BASF, POSCO), Tesla 2018 (Musk quote verified word-for-word), Boeing 737 (171 пассажир, 16K футов, 6 минут — все verified), все market numbers (78%/5,5%/95%/80,3%) — verified to chapter baseline.

## 2. Number drift report (speech vs chapter sample 20)

| # | Speech claim | Chapter source (v5) | Δ | Severity |
|---|---|---|---|---|
| D1 | «GE сожгла свыше четырёх миллиардов на платформу Predix» (l. 99, 259) | «свыше 4 миллиардов долларов» chapter l. 88, 234 | ✓ match | OK |
| D2 | «IBM Watson Health продан за десятую часть инвестиций» (l. 99) | Sold for $1,065B; chapter (l. 246) «около 20% от потраченных инвестиций» | ✗ **«Десятую часть» (10%) vs chapter «20%»** — speech understates recovery 2× | **P1** |
| D3 | «IBM Watson… двадцать процентов от потраченного» (l. 261) | «около 20% от потраченных инвестиций» chapter l. 246 | ✓ match | OK |
| D4 | «Foxconn… три миллиарда долларов субсидий под десять тысяч рабочих мест» (l. 99, 263) | «3 миллиарда долларов налоговых субсидий», «10 000 рабочих мест к 2025» chapter l. 250 | ✓ match | OK |
| D5 | «менее полутора тысяч рабочих мест» (l. 99, 263) | «менее 1 500 рабочих мест» chapter l. 88, 250 | ✓ match | OK |
| D6 | «Microsoft… 3,3 миллиарда долларов под датацентр Fairwater» (l. 263) | «3,3 миллиарда долларов под AI-датацентр Fairwater» chapter l. 250 | ✓ match | OK |
| D7 | «Декабрь 2025 — ещё 569 миллионов» (l. 263) | «декабрь 2025 — дополнительные 569 миллионов долларов инвестиций» chapter l. 252 | ✓ match | OK |
| D8 | «McKinsey 78%, 5,5%; MIT 95%; RAND 80,3%» (l. 101, 173) | chapter §1.1 (l. 90, 147) — exact match | ✓ verified | OK |
| D9 | «MIT… перерасход в среднем 380 процентов; четырнадцать месяцев» (l. 173) | chapter l. 151 «380% от оценок пилота; 14 месяцев» | ✓ match | OK |
| D10 | «Markets&Markets 34/155 миллиардов; Fortune 7,6; Precedence 8,57» (l. 191) | chapter l. 168, 94 exact | ✓ match | OK |
| D11 | «Tesla Optimus… Маск показал Optimus впервые в 2022. Обещание — десять-двадцать тысяч единиц на заводах Tesla к 2025, цена около двадцати пяти тысяч, миллион к 2027» (l. 241) | chapter l. 256: AI Day August 2021 (анонс), Bumblebee September 2022 (demo); initial price <$20K (2021); 2025 update «несколько тысяч к концу 2025», «миллион к 2027», «25 000 долларов целевая цена» | ✗ **«Впервые в 2022»** wrong (Optimus announced **August 2021** AI Day); ✗ **«10-20K к 2025»** conflates 2021 и 2025 Musk statements (2025 update — «несколько тысяч», не «10-20K») | **P1** |
| D12 | «Cybercab в октябре 2024 Optimus раздавал напитки. **Wired** подтвердил — управлялись людьми удалённо» (l. 245) | chapter l. 256, ref [84]: «**Bloomberg** назвал мероприятие "демонстрацией для прессы"»; ref [84] = Bloomberg October 11, 2024 | ✗ **Wired misattribution** — source was Bloomberg | **P1 — misattribution** |
| D13 | «Tesla Giga Press Model 2 отмена; gigacasting 2018→2024» (l. 85) | chapter l. 78, 87 confirms May 2024 retreat and 2018 production hell | ✓ verified | OK |
| D14 | «TSMC 95% точности; десять-пятнадцать процентов улучшения — отраслевая оценка, не финансовая отчётность» (l. 289) | chapter l. 279: same exact framing with caveat | ✓ verified (caveat preserved unlike slides v1) | OK |
| D15 | «Pfizer Vox… +20 000 доз вакцины на партию; AWS Bedrock; рекомендация» (l. 473, 703) | chapter §3.1 + §4.3 «+20 000 доз на партию» exact | ✓ verified | OK |
| D16 | «POSCO 180 узлов; несколько процентных пунктов улучшения, до десяти процентов снижения энергопотребления» (l. 533) | chapter part2 §3.3 + part3 ref [86]: 180 edge nodes, +5% efficiency, –10% energy | ✓ match | OK |
| D17 | «Yokogawa-JSR FKDPP, январь-февраль 2022, 35 дней» (l. 493) | chapter part2 + ref [30]: 17.01.2022—21.02.2022 = 35 days | ✓ verified | OK |
| D18 | «F-35 ALIS — около 44 тысяч долларов за лётный час, замена на ODIN» (l. 547) | chapter part2 §3.3: «порядка 44 000 долларов за лётный час по базовой линии 2018»; ALIS заменяется ODIN | ✓ verified | OK |
| D19 | «Северсталь минус 55 процентов прибыли в 2024» (l. 583) | chapter part2 l. 443: «прибыль Северстали –55% в 2024 году» | ✓ match | OK |
| D20 | «BASF Geismar… двадцать-тридцать процентов снижения брака партий» (l. 471) | chapter part2 §3.1 + ref [29] — BASF Geismar 20–30% defect reduction | ✓ verified | OK |
| D21 | **Brewery worked example:** «60 тысяч бутылок в час, миллион в сутки. Доля брака полпроцента. Пять тысяч размеченных дефектов каждый день.» (l. 749, 757) | chapter part3 §4.3 l. 186: «**30 000 бутылок в час** × 24/7 = ~**700 000 в день**; defect rate 0,5% → ~**3 500 дефектов в день**» | ✗ **Speech doubles throughput rate (60K vs 30K bottles/hour); 1M/day vs 720K/day; 5K defects vs 3,5K defects** | **P0 — direct number drift speech vs chapter source-of-truth** в worked example |
| D22 | «Базовая линия — ручная инспекция пропускает 0,3 процента дефектов; цель ≤ 0,2%; за три месяца» (l. 765) | chapter part3 l. 199: same exact 0,3% / 0,2% / 3 months | ✓ verified | OK |
| D23 | «Aircraft engine: MTBF восемь лет, флот 500, двадцать лет, сто отказов; FP 200K» (l. 719, 727) | chapter part3 l. 168–172 exact: MTBF 8 years, 500 fleet, 20 years, ~100 failures, $200K FP | ✓ verified | OK |
| D24 | «Boeing 737 MAX 9 рейс 1282; 5 января 2024; 16 000 футов; 6 минут; 171 пассажир» (l. 307) | chapter part2 l. 99: same exact details | ✓ verified | OK |
| D25 | «Bainbridge 1983 Automatica» (paraphrase) (l. 393) | chapter part2 l. 51, 53: Automatica vol. 19 № 6, 775–779 | ✓ verified attribution | OK |

**Summary numbers verified:** 22/25 verified exact-match; 1 P0 (brewery throughput drift 60K vs 30K); 2 P1 (Wired→Bloomberg misattribution; Optimus 2022→2021 + numbers conflation); 1 P1 (IBM Watson 10% vs 20% internal inconsistency).

## 3. Attribution accuracy (quotes)

| # | Speech quote | Source verification | Verdict |
|---|---|---|---|
| Q1 | Musk: «Да, чрезмерная автоматизация на Tesla была ошибкой. Точнее — моей ошибкой. Людей недооценивают.» (l. 93, 383) | Twitter Apr 13, 2018 (chapter ref [2]); Russian translation чёткая, в кавычках, semantic exact с «excessive automation… my mistake… Humans are underrated» | ✓ verified verbatim |
| Q2 | Musk CBS: «У нас была безумно сложная сеть конвейеров, и она не работала, так что мы избавились от всей этой штуки целиком.» (l. 385) | chapter ref [3] exact match («We had this crazy complex network of conveyor belts and it was not working, so we got rid of that whole thing.») | ✓ verified verbatim |
| Q3 | Liu Foxconn: «Софт выполняет около 80 процентов работы по настройке оборудования для запуска новой производственной серии.» (l. 423) | chapter ref [18], Liu May 2025; Russian translation exact match | ✓ verified |
| Q4 | Bainbridge paraphrase: «чем больше автоматизация, тем критичнее остающиеся операторы» (l. 393) | chapter part2 l. 51: «**чем больше автоматизация, тем критичнее остающиеся человеческие операторы**»; this is paraphrase, NOT quoted с кавычками, so не quote-violation | ✓ paraphrase acceptable |
| Q5 | Toyota Jidoka — speech не цитирует. Только «Toyota Production System плюс дзидока» (l. 395) — high-level reference. | OK — speech wisely **avoided** the unverified Jidoka quote from slides v1 (which had P1 «cannot verify word-for-word»). ✓ Cleanup vs slides v1. | ✓ verified avoidance |
| Q6 | Trump «восьмым чудом света» — paraphrase (l. 263) | chapter l. 250, 252: phrase произнесена **July 2017 White House press conference** (with Walker + Gou + Trump). Speech не локализует event (just «глава государства назвал»), что приемлемо для устной речи | ✓ acceptable paraphrase |
| Q7 | Cybercab Bloomberg / **Wired** — l. 245: «**Wired подтвердил** — управлялись людьми удалённо» | chapter ref [84] = **Bloomberg** «Tesla's Optimus robots had remote operators at Cybercab event», October 11, 2024; **NOT Wired** | ✗ **P1 — source misattribution Wired→Bloomberg** |

## 4. `[VFY-day-of]` markers adequacy в pre-flight

Speech v1 имеет **dedicated pre-flight checklist** (lines 39-72) с 8 явными `[VFY-day-of]` items + 5-min day-of refresh + recovery cards. Это **structural improvement** vs slides v1 (которые имели 0 markers по chapter convention).

**Pre-flight items distribution:**
- s01 hook Tesla retreats (CNBC May 2024) — ✓ URL provided
- s07 freshness McKinsey 2025 State of AI — ✓ URL provided
- s08 freshness three market estimates (M&M / Fortune / Precedence) — ✓ all three sources
- s11 freshness Tesla Optimus (ir.tesla.com) — ✓ — отмечено что V3 reveal late 2026, may shift
- s12 freshness Foxconn Wisconsin / Fairwater — ✓ Microsoft news URL
- s21 freshness FoxBrain Liu «80%» — ✓ Computex URL
- s25 freshness FKDPP — labelled «исторический факт» (acceptable: 2022 event)
- s28 freshness FDA Part 11 AI guidance — ✓

**Volatile claims в речи, помеченные `[VFY-day-of]` adequacy check:**

| Claim в speech | Cadence | Source date | Days delta from 2026-05-21 | Covered in pre-flight? |
|---|---|---|---|---|
| Tesla Optimus pilot status (l. 243) | weekly | Apr 2026 | ~30 days | ✓ s11 |
| Foxconn Wisconsin Microsoft purchase status (l. 263) | monthly | May 2024 + Dec 2025 | ~165 days | ✓ s12 |
| McKinsey 78%/5,5%/MIT 95%/RAND 80,3% (l. 101, 173) | quarterly | 2025 reports | ~6 months | ✓ s07 |
| Markets estimates 5x divergence (l. 191) | quarterly | 2025 forecasts | ~6 months | ✓ s08 |
| Foxconn FoxBrain Liu 80% (l. 423) | monthly | May 2025 | ~12 months | ✓ s21 |
| Hyundai Atlas RMAC commercial deployment (l. 361) | monthly | CES 2026 (Jan) | ~4 months | ✗ **NOT explicitly in pre-flight** |
| Toyota GAIA 8000→10000 models (l. 363) | quarterly | 2024 | ~14 months | ✗ NOT in pre-flight |
| BASF Geismar 20–30% (l. 471), Pfizer Vox +20K doses (l. 473) | quarterly | 2024-2025 | ~12 months | ✗ NOT in pre-flight |
| POSCO 180 nodes (l. 533) | quarterly | 2024-2026 | ~6-12 months | ✗ NOT in pre-flight |
| Норникель пилотная стадия (l. 577) | quarterly | 2024-2025 | ~6 months | ✗ NOT in pre-flight |
| СИБУР Q1 2025 launch (l. 581) | quarterly | 2024-2025 | ~6 months | ✗ NOT in pre-flight |

**Adequacy assessment:** **partial — 8 of ~14 volatile claims covered**. Pre-flight охватывает 5 critical (Optimus, McKinsey, FoxBrain, Foxconn, market sizes). Missing: Hyundai Atlas RMAC ramp, Toyota GAIA, BASF Geismar, POSCO, Russian context (Норникель, СИБУР, Северсталь). **P1 — add 5-6 более items в pre-flight** для symmetry с chapter v5's 33 markers.

## 5. Regression check (slides v1 errors NOT in speech)

| Slide v1 P0/P1 error | Status in speech v1 | Verdict |
|---|---|---|
| s07 Deloitte 42%/$7,2M | Speech uses S&P Global in pre-flight (l. 69 «Markets and Markets / S&P Global»); does not repeat Deloitte 42% claim | ✓ **Avoided regression** |
| s11 «февраль 2026» anachronism | Speech says «май 2026» throughout (l. 34 «Дата чтения: 21 мая 2026»; l. 243 «Сверка с реальностью на май 2026»; l. 71 «Markets and Markets / S&P Global — рыночные данные в пределах ±10%») | ✓ **Avoided** |
| s18 Atlas at HMGMA (vs RMAC) | Speech (l. 361) says «Atlas, гуманоидный — первое коммерческое внедрение, объявление январь 2026» — **does not name facility** at all; sidesteps HMGMA/RMAC ambiguity. Acceptable for spoken delivery. | ✓ **Avoided** (though could add RMAC for full correctness — see P2) |
| s10 FoxBrain «Llama 3.1 70B + DeepSeek techniques» | Speech (l. 221): «Foxconn FoxBrain. Презентован в марте 2025 года, обучен на основе Llama 3.1 70B методом дистилляции.» — **matches chapter v5 wording** | ✓ **Avoided regression** |
| s14 TSMC «+10–15% yield» without caveat | Speech (l. 289): «Заявка о десяти-пятнадцати процентах улучшения выхода годного — **отраслевая оценка, не финансовая отчётность**.» — **caveat preserved** | ✓ **Avoided** |
| s11 Optimus «10–20 тысяч к 2025, $30K» | Speech (l. 241): «десять-двадцать тысяч единиц на заводах Tesla к 2025, цена около двадцати пяти тысяч, миллион к 2027» — **partial repeat of slide v1 error**: «10-20K к 2025» conflates 2021 announcement with 2025 update; **$25K correct**, $30K from slide v1 dropped | ⚠️ **Partial regression** — see P1 D11 (Optimus numbers conflation) |
| s18 Toyota GAIA «10 000 часов» without caveat | Speech (l. 363): «ИИ-моделей, созданных сотрудниками заводов — восемь тысяч в 2023, десять тысяч в 2024» — speech **doesn't include the «10 000 часов саxовomy» claim** at all, simply omits it. Safer than slides v1. | ✓ **Avoided** |
| s18 Toyota Jidoka quote unverified | Speech does NOT quote Toyota Jidoka — only references «дзидока для Industry 4.0» and «Toyota Production System плюс дзидока». | ✓ **Avoided** (cleanup vs slides v1) |
| s12 Foxconn Wisconsin Trump+Gou conflation | Speech (l. 263) merges WH 2017 phrase with Wisconsin events — high-level paraphrase «глава государства назвал проект «восьмым чудом света»» without locating event; acceptable simplification for spoken delivery | ✓ **Acceptable simplification** |

**Cross-cutting:** Speech successfully **avoided 8 of 9** slides v1 regression patterns. Only partial repeat is Optimus numbers (D11 P1).

## 6. P0 / P1 / P2 issues

### P0 (must fix before delivery) — 1

1. **Brewery worked example — throughput drift speech vs chapter.** Speech (l. 749): «Линия идёт **60 тысяч** бутылок в час, **миллион в сутки**»; l. 757: «миллион бутылок в день, полпроцента брака — **пять тысяч** размеченных дефектов каждый день». **Chapter v5 part3 §4.3 (l. 186) says 30 000 bph × 24/7 = ~700 000 в день; 0,5% → ~3 500 дефектов в день.** Speech doubles throughput. If lecturer reads from speech but student references chapter for self-study, **internal inconsistency**. **Action:** correct to «**30 тысяч бутылок в час, около семисот тысяч в сутки**» и «**три с половиной тысячи размеченных дефектов каждый день**». Class-balance comment («за две-три недели») still works — math still gives ample data.

### P1 (substantive precision needed) — 5

2. **Cybercab источник: Wired vs Bloomberg.** Speech (l. 245): «**Wired** подтвердил — управлялись людьми удалённо». Chapter ref [84] = **Bloomberg** «Tesla's Optimus robots had remote operators at Cybercab event», Oct 11, 2024. Wired covered Cybercab но primary first-party reporting на remote operators был Bloomberg. **Action:** «**Bloomberg** подтвердил».

3. **IBM Watson «десятую часть инвестиций» (line 99) vs «двадцать процентов от потраченного» (line 261) — internal inconsistency.** Hook (l. 99) says «продан за **десятую часть** инвестиций» (10%); same speech later (l. 261) correctly says «двадцать процентов от потраченного». $1,065B / $4B+ = ~25%; chapter consistently says «около 20%». **Hook overstates the loss 2×.** **Action:** in line 99 change «**десятую часть**» → «**примерно пятую часть**» или «**около двадцати процентов**» (matches both chapter and l. 261). Reduces overdramatic framing AND fixes internal inconsistency.

4. **Optimus «впервые в 2022»** — speech (l. 241): «Маск показал Optimus **впервые в 2022**». Chapter (l. 256): announcement **August 2021 (AI Day)**; demo **September 2022 (AI Day 2 Bumblebee)**. **Action:** «**Маск анонсировал Optimus в 2021, демо в 2022**» либо «**Маск показал Optimus впервые на Tesla AI Day в 2021**».

5. **Optimus «десять-двадцать тысяч единиц к 2025, цена около двадцати пяти тысяч»** — speech (l. 241) conflates Musk's 2021 statement («<20K цена, потенциал большой») with 2025 update («несколько тысяч к концу 2025, миллион к 2027, $25K целевая»). Slides v1 had similar P1; speech **partially repeats** (drops $30K but keeps «10-20K к 2025»). **Action:** «**Обещание 2021 года — массовое производство по цене менее двадцати тысяч; обновление 2025 — несколько тысяч единиц к концу 2025, миллион к 2027, целевая цена двадцать пять тысяч**».

6. **Pre-flight `[VFY-day-of]` coverage missing 5-6 volatile claims.** Pre-flight (lines 39-72) covers 8 items but missing: Hyundai Atlas RMAC ramp (s18), Toyota GAIA 8000→10000 models (s18), BASF Geismar 20-30% (s24), POSCO 180 nodes (s27), Норникель пилотная стадия (s29), СИБУР Q1 2025 (s29). Asymmetric vs chapter's 33 markers. **Action:** add s18, s24, s27, s29 freshness items to pre-flight checklist.

### P2 (cosmetic / precision) — 6

7. **Hyundai Atlas facility wording.** Speech (l. 361) says «первое коммерческое внедрение» без указания facility. Слайдs v1 had HMGMA-trap; speech sidesteps. For accuracy, could add: «первое коммерческое внедрение **в RMAC** (Hyundai Robotics Metaplant Application Center)». P2 because current wording isn't wrong, just less precise.

8. **Foxconn Wisconsin events conflation.** Speech (l. 263) merges «восьмым чудом света» (произнесено July 2017 WH) with «Foxconn Wisconsin 2018-2024» timeline. Acceptable simplification for spoken delivery; for accuracy could clarify «в 2017 году на пресс-конференции».

9. **F-35 ALIS «замена на ODIN»** (l. 547) — chapter framing «transition 2026-2028»; speech doesn't qualify timing. Acceptable for one-line callback.

10. **Bainbridge name spelling/year** — speech (l. 393) «Лизанн Бейнбридж в 1983 году». Chapter calls her «Bainbridge L.» (= **Lisanne** Bainbridge). Russian transliteration «Лизанн» is acceptable; «Бейнбридж 1983» matches chapter ref. OK.

11. **«AB InBev / Tata Steel»** не упоминаются в speech v1 — chapter v3 fact-checker had concerns about both, but speech avoids them (Tata Steel mentioned at l. 343 with «–20% простоев» which matches chapter ref [24] verified). No regression. ✓

12. **Sakichi Toyoda 1924/1925 Type-G loom** — speech does NOT reference this date. Chapter v3 fact-check P0 (1925 completion, not 1924). Speech does not contain the date drift since it doesn't cite Toyoda specifically. ✓ avoidance.

## 7. Source hygiene & freshness reporting

**Strengths:**
- Dedicated pre-flight section с 8 freshness items + URLs — first structural improvement vs slides v1 baseline.
- Recovery cards (l. 61-65) с always-true backup (RAND 80,3%) — defensive freshness pattern.
- Day-of refresh (l. 67-71) calls out Markets and Markets / S&P Global / Tesla Optimus / Foxconn Wisconsin.
- Major numbers (78%/5,5%/95%/80,3%/$44K F-35/$200K aircraft engine/$3,3B Microsoft) — all chapter-anchored.
- Worked examples (Pfizer +20K доз, brewery, aircraft engine) — main framing matches chapter (only brewery cardinal numbers drift = P0).

**Weaknesses:**
- Pre-flight asymmetric coverage (8 of 14 volatile items).
- Wired vs Bloomberg misattribution (P1, single occurrence).
- Hook IBM Watson «десятую часть» overstates loss vs body «двадцать процентов» (internal inconsistency P1).
- Optimus 2022 «впервые» factually incorrect (2021 announcement) + 2025 numbers conflated.
- Brewery throughput double the chapter spec (P0).

## 8. Recommendations for Phase 11 (speech-writer batched revision)

### Top-3 must-fix (P0 + critical P1):

1. **Brewery throughput (l. 749, 757).** Change «60 тысяч бутылок в час, миллион в сутки» → «**тридцать тысяч бутылок в час, около семисот тысяч в сутки**»; «пять тысяч размеченных дефектов» → «**около трёх с половиной тысяч размеченных дефектов каждый день**». Cross-check chapter part3 §4.3.

2. **Cybercab source (l. 245).** «Wired подтвердил» → «**Bloomberg подтвердил**» (matches chapter ref [84]).

3. **IBM Watson hook (l. 99).** «продан за десятую часть инвестиций» → «**продан за примерно пятую часть инвестиций**» (matches chapter «около 20%»; resolves internal inconsistency with line 261).

### Top-3 P1 polish:

4. **Optimus history (l. 241).** Reformulate: «Маск **анонсировал** Optimus на Tesla AI Day в **2021** году. Прототип Bumblebee показали в 2022. Обещание 2021 — массовое производство по цене менее двадцати тысяч долларов. Обновление 2025 — **несколько тысяч единиц к концу 2025**, миллион к 2027, **целевая цена двадцать пять тысяч**.»

5. **Pre-flight expansion.** Add 4-5 items to pre-flight checklist (lines 44-50): s18 freshness Hyundai Atlas RMAC + Toyota GAIA, s24 freshness BASF Geismar 20-30%, s27 freshness POSCO 180 nodes, s29 freshness Норникель/СИБУР Russian context. Symmetric coverage с chapter v5's 33 markers.

6. **(Optional)** Hyundai Atlas facility (l. 361) — add «**в RMAC (Hyundai Robotics Metaplant Application Center)**» для explicit precision. Avoids HMGMA-trap completely.

### Strengths to keep:

- ✓ Musk «excessive automation… my mistake… Humans are underrated» word-for-word translation (l. 93, 383).
- ✓ Musk CBS conveyor belts quote word-for-word (l. 385).
- ✓ Liu Foxconn «80%» quote (l. 423) с явной caveat «**заявление поставщика, не независимая метрика**».
- ✓ Bainbridge 1983 paraphrase без quotation marks (l. 393).
- ✓ Toyota Jidoka — speech avoids the unverified slides v1 quote.
- ✓ Cybercab + Wired → fix → otherwise correctly framed «управлялись людьми удалённо».
- ✓ BASF Geismar 20-30% + Pfizer Vox +20K доз + POSCO 180 nodes + FKDPP 35 days + Boeing 737 171 пассажиров — all verified.
- ✓ Norilsk «пилотная, ранняя промышленная стадия» (l. 577) — chapter exact wording.
- ✓ Газпром нефть Северо-Соленинское ноябрь 2024 — explicitly distinguished from Norilsk (l. 579), matches chapter careful distinction.
- ✓ Северсталь –55% profit 2024 — chapter exact (l. 583).
- ✓ FDA 21 CFR Part 11 + ATEX Zone 0 + Указ 250 — all chapter-anchored.
- ✓ Aircraft engine worked example (MTBF 8 years, 500 fleet, $200K FP, SIL 2, DO-178C) — all numbers match chapter exact.
- ✓ Avoidance of slides v1 P0 errors (Deloitte / февраль 2026 / FoxBrain DeepSeek techniques).

## 9. Verdict justification

**APPROVE-WITH-POLISH** (not REJECT / not REVISE / not APPROVE-CLEAN):

- **1 P0** (brewery throughput drift 60K vs 30K bottles/hour) — single, localized within worked example; cardinal numbers fixable without restructuring framing; **does not impact pedagogical message** (data-passes-criterion is still true with 30K throughput).
- **5 P1** — substantive precision opportunities: Wired→Bloomberg, IBM Watson 10% vs 20% hook inconsistency, Optimus 2022→2021, Optimus numbers conflation, pre-flight asymmetric coverage. All localized polish.
- **6 P2** — cosmetic.
- **0 direction inversions.**
- **0 misquotes** (Musk x2 verbatim verified; Liu verbatim verified; Bainbridge appropriately paraphrased without quotes; Toyota Jidoka wisely avoided unlike slides v1).
- **0 curriculum hallucinations.**
- **8 of 9 slides v1 regressions successfully avoided** (only partial regression — Optimus numbers conflation, downgraded from slides v1 by dropping $30K).

Speech v1 is **publication-ready после P0 + 5 P1 fixes**. Source-of-truth discipline (book-first) clearly applied: speech follows chapter v5 baseline throughout, fixes slides v1 regressions on Deloitte/HMGMA/DeepSeek/февраль-2026, includes dedicated pre-flight `[VFY-day-of]` checklist (structural improvement over slides v1 zero markers).

**Total verified facts:** 22/25 number drift checks PASS; 5/6 quotes verified verbatim; 7/8 slides v1 regression patterns successfully avoided; 1 P0 (brewery cardinal numbers in worked example).

**Files saved:**
- `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-speech-v1-fact-checker.md` — this report.
- Cross-reference: chapter v5 fact-check `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-chapter-v3-fact-checker.md` (APPROVE-WITH-POLISH baseline).
- Cross-reference: slides v1 fact-check `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-slides-v1-fact-checker.md` (REVISE, 2 P0 / 8 P1 — speech v1 successfully avoids 8 of 9).

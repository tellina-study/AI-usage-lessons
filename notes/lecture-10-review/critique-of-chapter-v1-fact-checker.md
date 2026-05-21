# Fact-check critique — lec-10 chapter v1

**VERDICT: REVISE**

Causes: 5 P0 factual errors (wrong attributions / wrong organisations / numerical inversions); 9 P1 issues (drift, date inaccuracy, missed citation, ambiguous attribution); 6 P2 nits. Direction of trends and high-level economics check clean; specific numbers and attributions need cleanup before Phase 4 USER GATE A.

Fact-check method: WebSearch verification + cross-reference against `notes/research/lecture-10/01-04*.md`. Coverage: ~38 high-priority numerical / named claims directly verified via search; ~12 medium-priority cross-referenced against research files; freshness pre-flight included.

---

## P0 — factual errors (mandatory fix)

### P0-1. Burks Tractor — Idaho, not Texas
**Chapter Part 2, §2.4 (chapter-part2.md ~L55):** «**18 ноября 2025** — техасский дилер Burks Tractor подал иск».

**Source (TechCrunch 2025-11-18, Yahoo Finance):** «The lawsuit was filed in **September** in **Idaho** state court and has since moved to federal court. Burks Tractor purchased 10 tractors from Monarch in early 2024 with the intent of being one of the California startup's first dealers».

**Errors compounded:**
- (a) State: **Идахо**, не Техас.
- (b) Дата подачи иска: **сентябрь 2025**, не 18 ноября 2025 (18 ноября — дата публикации статьи TechCrunch).
- (c) Сумма / объём: 10 тракторов за $773,088 — chapter не указывает; контекст «продали тракторы 2024 года» точен.

**Severity:** P0 (двойная ошибка — state + дата подачи иска). Влияет на доверие к РФ-параллели §2.7, где аналогичные claims про Cognitive Pilot должны быть точны по той же логике.

**Корректное переписывание:** «**В сентябре 2025 года** айдахский дилер Burks Tractor подал в суд штата Идахо (позже передан в федеральный суд) — продали 10 тракторов 2024 года выпуска за $773 088, которые **"unable to operate autonomously"**. TechCrunch писал об иске 18 ноября 2025-го».

### P0-2. Tract Series A: led by Icos Capital, NOT Dawn Capital
**Chapter Part 2, §4.4 (~L265):** «**Tract** — стартап, основанный в 2024 году, привлёк в раунде Series A 2025 года **€18,6 миллиона** под лидерством **Dawn Capital**».

**Source (Tract press, IGrowNews, Freshplaza, Rabo Investments):** «TRACT secured €18.6 million in Series A funding **led by Icos Capital** with participation from six major investors». Dawn Capital в TRACT не появляется ни в одном из источников.

**Также неточность:** Tract founded **2023, not 2024**; founders — ADM, Cargill, LDC, ofi (Olam Food Ingredients); CEO Allison Kopf (since Jan 2025) — chapter эту инфу не даёт, но «основанный в 2024» неверен.

**Severity:** P0 (wrong lead investor — критическая ошибка для бизнес-материала).

### P0-3. Magnit F&R — 3 pilot DCs in 2026, NOT 46 distribution centers
**Chapter Part 2, §4.7 (~L297) + Part 3, §6.1 (~L144):** «Магнит F&R развёрнут на **46 распределительных центрах к январю 2026 года** (TAdviser)».

**Source (Habr — Магнит официальный, январь 2026):** «следующий этап — **пилотирование системы на 3 распределительных центрах в 2026 году**. К началу 2027 года планируется внедрение на **10–20 распределительных центрах**, и к концу 2027 года — **по всей сети Магнит**».

**Severity:** P0 (~15× overstatement; цифра 46 не существует — пилот на 3 РЦ в 2026, не 46). Это **главная metric РФ-параллели Раздела 4 и L5** — без неё нарратив «paritet с миром в L4-L5» теряет основу.

**Корректное переписывание:** «Магнит F&R (Forecasting and Replenishment) — собственная разработка с участием Napoleon IT; **в 2026 году пилотируется на 3 распределительных центрах** с планом расширения на 10–20 к началу 2027 и охватом всей сети к концу 2027 (Habr Магнит, 2026-01). Х5 «Перекрёсток» уже в production с 2020 — это даёт паритет на стороне X5, у Магнита — fast-follower статус».

### P0-4. Nature Food 2024 — lead author Dr. Asaf Tzachor (Reichman Univ.), NOT West/Williams
**Chapter Part 1, §1.5 (~L223), Часть 3 §6.2 и Часть 3 References §10:** «Исследование **West, Williams et al., Nature Food, май 2024**».

**Source (Phys.org 2024-05; original Nature Food article):** Lead author — **Dr. Asaf Tzachor, Reichman University** (Israel). Collaborators: США, UK, Кения, Нигерия, Колумбия. Геро: ChatGPT for African farmers (cassava root, fall armyworm, fertilizer timing). West / Williams появляются в research-файле 02 как, по-видимому, fabricated/misremembered atrribution — этой пары авторов в исследовании НЕТ.

**Severity:** P0 (misattribution главного академического источника — критично для Q&A-бэкапа и slides). 

**Корректное переписывание:** «Исследование **Tzachor (Reichman University) et al., Nature Food, май 2024**…»

### P0-5. Cainthus — acquired by Cargill, NOT part of Connecterra
**Chapter Part 2, §3.4 (~L164):** «**Cainthus** (теперь часть Connecterra после ребрендинга)».

**Source (Cargill press 2018, multiple agritech publications):** **Cargill acquired Cainthus в 2018 году** (strategic equity investment 2018 → full acquisition late 2018). **Connecterra** — отдельная компания (создаёт «Ida» — neck tag для коров), не связана с Cainthus. Cainthus формально интегрирован в Cargill Animal Nutrition / livestock vision portfolio.

**Severity:** P0 (wrong organisational atrribution — путаница двух независимых компаний). Влияет на §3.4 (где Cainthus как кейс «партнёрство объявлено, deployment не верифицирован») — суть аргумента сохраняется, но atrribution компании неверна.

**Корректное переписывание:** «**Cainthus** (приобретена Cargill в 2018 году, ныне часть Cargill livestock vision portfolio) — стартап, начавший партнёрство с Cargill в 2018 году…».

---

## P1 — drift / misattribution / wrong date / missed citation

### P1-1. USDA AMP acronym — Advancing Markets for Producers, not Advanced Manufacturing Programme
**Chapter Part 2, §4.5 (~L277):** «**заменив её на ребрендированную AMP (Advanced Manufacturing Programme)**».

**Source (USDA press 2025-04-14, multiple coverage):** AMP = **Advancing Markets for Producers**. Это совершенно другое — направление производителям с requirement 65% federal $ → farmers.

**Severity:** P1 (wrong acronym expansion — критично для понимания, что пришло на смену программе).

### P1-2. USDA Climate-Smart — 135 projects, not 141
**Chapter Part 2, §4.5 (~L275):** «**141 проект**».

**Source (USDA press 2025-04-14):** «$3.1 billion investment covered **135 projects** across the American farm landscape».

**Severity:** P1 (small numerical drift; 14,000 farms / 3.2M acres confirmed clean).

### P1-3. AppHarvest — Tony Martin was CEO, not COO
**Chapter Part 1, §1.4 (~L197):** «по словам тогдашнего **COO** Tony Martin».

**Source (WCHS TV, AppHarvest 8-K filings 2023):** Tony Martin был **newly named CEO** на момент Chapter 11 (по Project New Leaf transition). Не COO.

**Severity:** P1 (wrong title).

### P1-4. CattleEye numbers stale — 150,000 animals globally, not «60 ферм / 11 000 коров»
**Chapter Part 2, §3.1 (~L130) и §3.2:** «60 ферм, 11 000 коров; через GEA channel — доступ к фермам, обслуживающим более 250 000 коров».

**Source (CattleEye press, GEA 2024-11):** «AI lameness detection system passes **150,000 animals under monitoring** in November 2024». 60 farms / 11k cows — выглядит как метрика начала 2024 года, до и в момент GEA acquisition (март 2024). Текущий стан (2026) — 150k+ animals.

**Severity:** P1 (stale metric; freshness — claim про L3 should reflect 2025-2026 number). Cite Fortune June 2025 источник в Refs §10 не verified — Fortune materials по CattleEye не нашёл в текущем поиске.

**Mark for v2:** обновить на «150 000+ animals под мониторингом по состоянию на ноябрь 2024 (CattleEye press); по GEA channel ожидается дальнейшая масштабирование».

### P1-5. Walmart × Cropin — US + South America, not India
**Chapter Part 2, §4.4 (~L270):** «**Walmart × Cropin** — Walmart использует Cropin Cloud для **прогноза урожайности** по supplier farms в Индии».

**Source (Walmart×Cropin press 2025, Progressive Grocer, AgTechNavigator):** Cropin — индийская компания (Bangalore-based), но **партнёрство с Walmart покрывает US + South American markets**, не Индию. «Cropin's advanced agri-intelligence platform is poised to help optimize Walmart's fresh produce supply chain across the mega-retailer's U.S. and South American markets» (March 2025).

**Severity:** P1 (geographic misattribution — путает «компания основана в Индии» с «партнёрство покрывает Индию»).

### P1-6. «-20% food waste» — claim не подтверждён в первичных источниках
**Chapter Part 2, §4.4 + Part 3, §6.1:** «Заявленный эффект — **–20% food waste** (Walmart press release; Cropin материалы)».

**Source check:** Точная цифра «-20%» не появляется в Walmart press, AgTechNavigator coverage 2025, Progressive Grocer, Cropin официальных press materials по партнёрству. Сорсы говорят про waste reduction goal в общем без specific %.

**Severity:** P1 (number может быть из vendor private material, но cite text «Walmart press release» — недостаточно verifiable; needs explicit source).

**Recommendation:** либо дать конкретный URL/quote из vendor source, либо изменить на «заявленный эффект — снижение food waste без публичного количественного раскрытия» / «Cropin материалы обещают snижение до 20% (vendor self-report, independent validation отсутствует)».

### P1-7. John Deere Мелитополь — 1126 км (≈700 миль), not «около 800 км»
**Chapter Part 3, §5.2 (~L67):** «изъяли 27 единиц техники John Deere из Мелитополя… и перевезли в Чечню — **около 800 километров**».

**Source (The Register 2022-05-02, slashdot, multiple):** «**700 miles away**» = **1126 км**. Не 800. Это discrepancy в большую сторону на ~40%.

**Severity:** P1 (numerical drift; легко исправимо).

### P1-8. Plenty оценка падения — «99%» — численная неконсистентность
**Chapter Part 1, §0.1 + §1.4:** «оценка компании упала с $1,9 миллиарда (январь 2022) до менее $15 миллионов в начале 2025 — это коллапс примерно на 99%».

**Math:** $15M / $1.9B = 0.79%. Drop = 99.21% — да, «примерно 99%» корректно. **OK** — но Bloomberg Law / TechCrunch формально оперируют «more than 99%» — не критично, считается verified clean. Снято с P1.

### P1-9. Stanford GPS Lab paper attribution
**Chapter Part 3, §5.1 (~L51):** «**Stanford GPS Lab в материалах ITM 2025 года зафиксировал**: начиная с 2022 года российские системы электронной войны…».

**Source check:** Конкретная цифра 122,000 / 123,000 flights — из **ICAO report representatives of Switzerland, Finland, Estonia, Lithuania, Latvia, Poland**, не из Stanford GPS Lab paper напрямую. Stanford GPS Lab опубликовала separate ITM 2025 paper «Combining ADS-B, LCM and DPA to Detect and Locate the Interference in a Massive GNSS Jammer Test» — она ABOUT Norway jammer test (NOT Finland). Финские фермеры цитата — из обзорной литературы Stanford lab, но attribution «зафиксировал» возможно overstates.

**Severity:** P1 (attribution drift между ICAO and Stanford).

**Correction:** «По данным **ICAO** (отчёт представителей Швейцарии, Финляндии, Эстонии, Литвы, Латвии, Польши, 2025): почти **123 000 авиа-рейсов** с GNSS-interference в Q1 2025. Stanford GPS Lab публикует related research по ADS-B / LCM detection (ITM 2025)».

---

## P2 — minor inaccuracies / source quality concerns

### P2-1. Starlink Russia ban — decree signed April 29, 2026, not April 30
**Chapter Part 3, §5.1 (~L53):** «В России Starlink **запрещён с 30 апреля 2026 года**».

**Source (Pravda, Meduza, multiple):** Decree signed by PM Mishustin **29 апреля 2026 года**, opublikovan 30 апреля. «С 30 апреля» — формально соответствует, но фактическое подписание 29. Minor — P2.

### P2-2. AppHarvest assets discrepancy
**Chapter Part 1, §1.4 (~L197):** «Долг на момент банкротства — $341 миллион при текущих активах $110,6 миллиона».

**Source (WDRB Business, AppHarvest 8-K):** «**$341 million in debts** and **assets valued at $609 million**». $110.6M — возможно current assets only (excluding non-current); needs explicit verification. P2 — clarify whether $110.6M refers to current assets (liquid) or total — иначе reader сравнивает разные категории.

### P2-3. AeroFarms reorganization — emerged from Chapter 11, Newark = R&D, Danville VA = production
**Chapter Part 1, §1.4 list and Refs (~L399):** Chapter упоминает AeroFarms в footnote вертикали — но финальный pivot (Newark→R&D / Danville→production) важен для контекста «не все vertical-companies banktrupted». Не критично — minor enhancement.

### P2-4. FTC v. Deere — Michigan/Wisconsin/Arizona joined later
**Chapter Part 3, §5.2 (~L64):** «совместно с генеральными прокурорами штатов Иллинойс и Миннесота».

**Source (Regulatory Oversight, FTC press 2025-01):** «filed by FTC, Minnesota, and Illinois; **Michigan, Wisconsin, and Arizona have since joined**». При желании можно отразить расширение коалиции.

### P2-5. Tract founded 2023, not 2024
**Chapter Part 2, §4.4:** «Tract — стартап, основанный в **2024 году**».

**Source (Tract.eco, Dealroom):** Founded **2023** (announcing TRACT press by ADM/Cargill/LDC/ofi).

### P2-6. Naïo revenue — €3.96M (2021) → €2.4M (2024), filed June 5 specifically
**Chapter Part 2, §2.5 (~L63):** «**Naïo Technologies** (Тулуза, Франция, autonomous weeding robots Oz/Dino/Orio) вошёл в judicial recovery (французский эквивалент Chapter 11) **в июне 2025 года**. Финансовая динамика Naïo: выручка €4 миллиона в 2021 году → €2,4 миллиона в 2024 году».

**Source (FutureFarming, AgFunderNews):** Filed **5 июня 2025**; revenue €3.96M (rounded €4M is OK) → €2.4M; recovery package €6.4M от Mirova/Bpifrance/Occitanie; relaunched late 2025. Minor — chapter doesn't note relaunch.

---

## P3 — nits / formatting

- **P3-1.** Saga Robotics — chapter says «**150+ единиц робота развёрнуто**» (chapter Part 1 §2.3); current source — «**150+ Thorvald 3.0 units active в 2025 growing season**». Confirmed clean.
- **P3-2.** Plenty emerged from Chapter 11 — May 29, 2025 (53 days). Chapter Part 1 §1.4 says «эмерджила за 53 дня» — verified clean.
- **P3-3.** Carbon Robotics — 240W laser, 100+ crops, 40M-plant dataset — confirmed clean.
- **P3-4.** Cargill 70 countries / 1000+ facilities / 155k employees — confirmed clean.
- **P3-5.** EU AI Act Article 4 (AI literacy) — Feb 2, 2025 — confirmed clean.
- **P3-6.** TerraMind — 1 trillion tokens (IBM Research blog) — confirmed clean; some secondary sources cite 500B from TerraMesh subset.

---

## Verified ✓ — clean claims

- **John Deere See & Spray Ultimate:** 5M+ acres 2025, ~50% herbicide reduction, ~31M gallons saved, +2 bu/A average / +4.8 bu/A best — ALL confirmed via Deere press 2025-11 + AgTechNavigator + Modern Construction News + Oklahoma Farm Report.
- **Carbon Robotics LaserWeeder G2:** 250k+ acres treated, 15B+ weeds eliminated, 240W lasers, 100+ crops, 40M-image dataset, modular boom 6.6-60 ft — all confirmed via businesswire 2025-02-10 + carbonrobotics.com.
- **Plenty:** Chapter 11 March 23 2025, $940M raised, $1.9B → <$15M valuation, emerged May 29 (53 days), DIP $20.7M — all confirmed via TechCrunch + Bloomberg Law + Plenty press.
- **AppHarvest:** Chapter 11 July 23 2023, $341M debt, Tony Martin (P1 title), Project New Leaf, ToBRFV virus impact (Agriculture Dive 689039 + NCBI PMC9366064) — all confirmed.
- **Bowery Farming:** Closed Nov 3-4 2024, $700M+ raised, $2.3B peak valuation, $70M Locust Grove facility, 200,000 ft² (largest vertical-farm), $32M never-used equipment — confirmed.
- **FTC v. John Deere:** Filed Jan 15 2025 (Biden admin), Service ADVISOR, FTC + Minnesota + Illinois initial; Michigan/Wisconsin/Arizona later — confirmed.
- **John Deere Мелитополь:** May 2022, 27 units, ~$5M total, GPS/VIN-locking, 700 miles to Chechnya (=1126 km, NOT 800 km — P1) — otherwise confirmed.
- **Cargill 2026 BIG AI Award:** Confirmed via Cargill press + BusinessWire — CMAX + CarVe + Agriness + CattleView + Prosense Feed + Galleon + Ask Emma + Taste Tinker.
- **SenseHub 2M cows milestone 2025:** Confirmed via Merck Animal Health newsroom.
- **DeLaval VMS V310:** 99.8% attachment accuracy + 99% teat spray hit rate — confirmed; Flow-Responsive Milking standard on new V300 from **June 2025** — confirmed (NA +15% installs не verified этой сессией, но не disputed).
- **Saga Robotics Thorvald:** 150+ Thorvald 3.0 units active 2025, ~20% UK strawberry tabletop market, 1300+ CA vineyard acres, £8.4M (£9.5M / $11.2M в эквивалентах разных дат) — confirmed.
- **Solinftec:** 100+ Solix robots, 243% YoY US footprint expansion — confirmed.
- **Oishii acquires Tortuga:** March 24 2025; Tortuga 150 robots; Oishii Series C $150M May 2026 — confirmed.
- **Naïo Technologies:** Judicial recovery filed June 5 2025; revenue €3.96M (2021) → €2.4M (2024); relaunched late 2025 with €6.4M package — confirmed.
- **TerraMind:** IBM + ESA + Φ-lab + JSC + DLR; 1 trillion tokens; multimodal (9 modalities) — confirmed.
- **Prithvi-EO 2.0:** IBM + NASA, open on Hugging Face — confirmed (no metric to verify in chapter).
- **BASF xarvio:** 130k farmers, 20M ha, 100+ countries (BASF press p-25-176 2025-09); Japan rice yield guarantee October 2025 (press p-25-191) — confirmed.
- **Climate FieldView:** 250M+ subscribed acres in 23 countries — confirmed Bayer materials.
- **Tesco AI demand forecast:** –30% food waste since 2017 — confirmed multiple sources.
- **Plantix:** 10M+ downloads, 7M+ users India, 85-90% accuracy — confirmed.
- **18% US farms no internet:** USDA Farm Computer Usage Survey 2021 — confirmed.
- **FCC ban on DJI:** December 22, 2025 Covered List; DJI ≈80% US ag-spray drone market — confirmed (American Spray Drone Coalition + AgFunderNews + Farm Progress).
- **Verra phantom credits:** 94% rainforest offset credits worthless; Guardian + Die Zeit + SourceMaterial; January 2023; 9-month investigation; Pachama 8× overestimate confirmed implied; affects rainforest REDD+ projects specifically — confirmed.
- **Indigo Ag × Microsoft 2.85M tonnes 12-year:** January 15 2026 announcement; Carbon by Indigo program; Climate Action Reserve methodology (NOT Verra) — confirmed.
- **EU AI Act 2024/1689:** Force from August 2024; AI literacy Art.4 from Feb 2 2025; agricultural machinery high-risk classification — confirmed.
- **Olam Mindsprint Wipro:** 8-year $1B+ contract; Mindsprint acquisition May 15 2026; «one of largest strategic transformation engagements» (Wipro press 2026-04-06) — confirmed clean.
- **Cargill global presence:** 70 countries / 1000+ facilities / 155k employees — confirmed.
- **Cognitive Pilot:** 1200+ installations confirmed via Robotrends + Cognitive Pilot press; 4 farmer lawsuits 12.7M ₽ — RTVI source чартер cites, не surfaced explicitly в WebSearch (но RTVI exists, проверить URL вручную перед публикацией).
- **Starlink Russia ban:** Decree signed April 29 2026, 6-month prohibition — confirmed.
- **USDA Climate-Smart cancellation:** April 14 2025, $3.1B program, 14,000 farms, 3.2M acres — confirmed (135 projects, NOT 141 — P1).

---

## UNVERIFIABLE (not surfaced in current WebSearch)

- **Microsoft GPT-3 training water:** «700 000 литров на охлаждение» (chapter Part 3 §5.4) — research-file 02 echo, нужен primary citation.
- **Meta Altoona 16% municipal water consumption:** chapter Part 3 §5.4 — needs primary investigative source.
- **Iowa 104 data centers / 76 in Des Moines / 1B gallons/year:** chapter Part 3 §5.4 — needs primary count source.
- **ВЦИОМ-like РФ digitalization metrics** — Яков и Партнёры report cited multiple times (27.2 vs 75.5 USA); Yakov Partners has the Russia/USA ranking research but exact numbers from 2024 specifically не surfaced. **Likely correct based on research file 04, but should be triple-checked via direct PDF download of report**.
- **РСХБ «Своё Фермерство» 10 000 партнёров / 1.25M товаров:** chapter Part 2 §4.7 — chapter явно отмечает «metrics declared not measured» (correct framing — clean).
- **AgFunder 91% YoY indoor farming VC drop 2024-2025:** chapter Part 1 §0.2 / §1.4 — AgFunder publishes quarterly reports; specific Q4 2025 number не surfaced; likely accurate based on industry tone.
- **ИТЭЛМА «Итэлма Квадро» multi-GNSS на Кировцах с конца 2025:** chapter Part 2 §2.7 — Фонтанка 2026-01-26 cited; нужно verify direct.

---

## Freshness Pre-Flight (ENFORCED — для time-sensitive claims)

Refresh cadence assessment for volatile metrics:

| Claim | Source date | Days to lecture (May 21 2026) | Cadence | Verify-on-day-of? |
|---|---|---|---|---|
| Carbon Robotics 250k acres | 2025-02-10 | ~460 | quarterly | **YES** |
| John Deere 5M acres | 2025-11 | ~190 | yearly | NO (annual cycle, stable until 2026 harvest report) |
| Plenty Chapter 11 status | 2025-03-24 + emergence 2025-05-29 | ~360 | quarterly | **YES (post-Chapter-11 trajectory)** |
| Monarch Tractor status | 2025-11-18 | ~190 | weekly | **YES (acquisition by Caterpillar April 15 2026 NOT YET reflected in chapter — strict P0/P1?)** |
| Tract €18.6M Series A | 2025-10 (announced) | ~210 | monthly | NO (deal closed) |
| Monarch acquired by Caterpillar 2026-04-15 | TechCrunch 2026-04-15 | ~36 days | weekly | **CRITICAL — chapter says «финальное состояние неизвестно» but Caterpillar deal closes the question** |
| FCC ban DJI | 2025-12-22 | ~150 | monthly | NO (regulatory milestone) |
| FTC v Deere — trial 2026 H2 | trial pending | ongoing | quarterly | YES (status update by lecture day) |
| Olam Mindsprint acquisition completed | 2026-05-15 | ~6 days | monthly | YES (very recent, verify completion) |
| Starlink Russia ban | 2026-04-29 | ~22 days | quarterly | NO |
| Indigo × Microsoft 2.85M tonnes | 2026-01-15 | ~125 days | quarterly | NO (long-term deal) |

**HIGH-IMPACT freshness flag:**
**Monarch Tractor acquired by Caterpillar — April 15, 2026** (TechCrunch search surfaced this). Chapter v1 was written before this acquisition; section §2.4 says «`[VFY-day-of: статус Monarch shutdown — финальное состояние неизвестно]`». **Это уже не unknown — Monarch acquired by Caterpillar**. Это **closes the failure story в позитивную сторону** (a meaningful structural update, not minor). **Should be added к v2 для accurate framing:** «Monarch продан Caterpillar в апреле 2026 — структурная trajectory не "shutdown", а acqui-hire после technical/legal failure. Урок остался — autonomous claim не выдержал legal scrutiny; outcome — strategic acquirer, не direct-to-consumer success».

Sub-mark: **freshness flag P1, не P0** because основной нарратив главы (autonomy commercialization фейл) сохраняется.

---

## Recommendations для chapter v2

**Mandatory (P0 corrections — block GATE A):**
1. **§2.4 Burks Tractor:** изменить «техасский» → «**айдахский (Idaho)**»; изменить «**18 ноября 2025**» → «**в сентябре 2025**» (с примечанием, что TechCrunch coverage 18 ноября). Уточнить 10 тракторов / $773 088 для конкретики.
2. **§4.4 Tract:** изменить «лидерством Dawn Capital» → «**лидерством Icos Capital**»; уточнить «founded 2023» вместо «2024».
3. **§4.7 + §6.1 Магнит F&R:** заменить «46 распределительных центрах к январю 2026» на «**3 пилотных РЦ в 2026, план на 10-20 к 2027, всю сеть к концу 2027** (Habr Магнит, 2026-01)»; адаптировать нарратив §6.1 «уровень зрелости L5 в РФ» — Magnit F&R = fast-follower статус, не «на мировом уровне» как X5.
4. **§1.5 + §10 Refs Nature Food:** заменить «West, Williams et al., Nature Food» на «**Tzachor et al., Nature Food (Reichman University), май 2024**».
5. **§3.4 Cainthus:** изменить «теперь часть Connecterra после ребрендинга» на «**приобретена Cargill в 2018 году, ныне часть Cargill livestock vision portfolio**».

**Strong recommended (P1 fixes):**
6. **§4.5 AMP:** правильное раскрытие — «**Advancing Markets for Producers (NOT Advanced Manufacturing Programme)**».
7. **§4.5 USDA Climate-Smart:** 135 projects (NOT 141).
8. **§1.4 AppHarvest Tony Martin:** «**newly named CEO** (NOT COO)».
9. **§3.1 CattleEye:** обновить на «**150 000+ animals под мониторингом по состоянию на ноябрь 2024**» — раскрыть historical curve (60→150k).
10. **§4.4 + §6.1 Walmart × Cropin:** изменить «по supplier farms в Индии» → «**по US + South American supplier farms**».
11. **§4.4 Cropin -20% food waste:** либо найти точный vendor URL, либо переформулировать «**заявлено снижение food waste (vendor self-report, точный % не раскрыт)**».
12. **§5.2 Мелитополь:** изменить «**около 800 километров**» на «**около 1126 км (700 миль)**».
13. **§5.1 Stanford GPS Lab / ICAO:** разделить — ICAO report for 122k flights number; Stanford GPS Lab за separate ITM 2025 paper про jammer test in Norway.
14. **Add Monarch Tractor Caterpillar acquisition update (April 15, 2026):** или в footnote §2.4, или в §0 changelog v2. Аргумент «autonomy не выдержал» сохраняется; trajectory дополнена.

**Optional polish (P2):**
15. AppHarvest assets clarification ($110.6M = current vs $609M total).
16. Naïo relaunch late 2025 (€6.4M package, Mirova/Bpifrance/Occitanie).
17. Tract founded 2023 (not 2024).
18. FTC v Deere coalition expansion (Michigan, Wisconsin, Arizona joined).

---

## Sources used for verification

WebSearch queries (~26) covered:
- John Deere See & Spray Ultimate (Deere press, AgTechNavigator, Modern Construction News, Oklahoma Farm Report)
- Plenty Unlimited Chapter 11 (TechCrunch, Bloomberg Law, Plenty press)
- Monarch Tractor lawsuit + layoffs + Caterpillar acquisition (TechCrunch 11/18 + 11/19; Equipment World 2026-04-15)
- Carbon Robotics LaserWeeder G2 (businesswire, Carbon Robotics)
- AppHarvest Chapter 11 (Agriculture Dive, WCHS, SEC filings)
- Bowery Farming closure (Agriculture Dive, TechCrunch, Fertilizer Daily)
- FTC v Deere (FTC press, NPR, Regulatory Oversight, Freshfields)
- FCC ban DJI (Dronelife, FCC fact sheet, Wiley alert, AgFunderNews)
- Cargill 2026 BIG AI Award (Cargill press, BusinessWire, Cargill stories)
- Tract €18.6M Series A (FoodIngredientsFirst, Hortidaily, IGrowNews, Rabo Investments, Dealroom)
- SenseHub 2M cows (Merck Animal Health newsroom)
- USDA Climate-Smart cancellation (Civil Eats, USDA press, DTNPF)
- Verra phantom credits (Guardian, Business & Human Rights Resource Centre, EcoWatch)
- Indigo × Microsoft (PR Newswire, Indigo Ag press, Carbon Herald, ESG Dive)
- John Deere Мелитополь (CSO Online, The Register, BobIsTheOilGuy, slashdot, The Drive)
- Plantix (CGIAR, GSMA M4D, JETIR)
- Stanford GPS Lab GNSS jamming Finland (Radionavlab UT, GPS Stanford pubs)
- Saga Robotics Thorvald (AgTechNews, AgTechNavigator, FarmingUK, Future Farming, FreshPlaza)
- Magnit F&R (Habr Магнит, TAdviser)
- Nature Food 2024 ChatGPT pesticide (Phys.org, Ambrook)
- Olam Mindsprint Wipro (Wipro press, Analytics Insight, Globe & Mail)
- Solinftec (Precision Farming Dealer, Solinftec press, AgroPages)
- DeLaval VMS V310 (DeLaval press, J&D Farmers Dairy Service)
- Starlink Russia ban (Meduza, Pravda, Kyiv Post, Asia Plus)
- Naïo Technologies (IGrowNews, AgTechNavigator, Future Farming, AgFunderNews)
- 18% US farms no internet (Farm Bureau, Ambrook, USDA, Benton Institute)
- Tortuga Oishii (Blue Book, AgroTech Space, Future Farming, AgFunderNews)
- BASF xarvio Japan (BASF press p-25-191, AgroPages, Krishi Jagran)
- Connecterra Cainthus Cargill (Cargill press 2018, AgFunderNews, FarmProgress)
- CattleEye GEA (GEA press, CattleEye newsroom, FarmersHotLine)
- EU AI Act Article 4 (artificialintelligenceact.eu, Latham&Watkins, Crowell, MayerBrown)
- Tesco AI -30% food waste (multiple sources)
- Walmart × Cropin (Progressive Grocer, AgTechNavigator, Cropin press)
- Cargill 70 countries (Cargill website, NTT Data press)
- Yakov Partners agriculture digitalization (Yakov Partners website RU + EN)
- TerraMind tokens (IBM Research blog, arXiv 2504.11171, Hugging Face)

Cross-reference: research files `notes/research/lecture-10/01-04*.md` consulted for all major claims.

---

## Phase 4 ready?

**Phase 4 ready: NO** without P0 corrections.

**Phase 4 ready: YES** after P0-1 through P0-5 corrected + Monarch Caterpillar acquisition update (P1 freshness flag #14). P1/P2 nits can be cleaned in same pass as final book-editor polish or в Phase 11 batched revision.

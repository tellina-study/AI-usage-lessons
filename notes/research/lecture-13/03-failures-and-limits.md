# 03 — Провалы, фундаментальные ограничения и анти-кейсы (failure-bucket ≥30%)

**Summary.** Цель файла — фундамент failure/judgment-блока лекции (≥30% strict-in контента, см. CLAUDE.md § AI-Failure & Judgment Content Rule). Каждый кейс содержит: (1) что произошло (документировано); (2) выученный урок; (3) правильная альтернатива / границы применимости / критерий «здесь AI не нужен / не работает». Структура — 6 разделов: (1) канонические fatalities и retreat-кейсы, (2) серия банкротств autonomous-trucking, (3) Cruise GM exit, (4) Tesla Robotaxi Austin — текущие инциденты, (5) black-swan disruptions и почему ML не предсказал, (6) фундаментальные «когда AI не нужен» + альтернативные инструменты.

**Принцип отбора.** Доступная публично документация. Никаких выдуманных цифр; если источник тяжело найти — помечено «требует дополнительной верификации». Каждый кейс дает защищаемый критерий **«здесь AI не нужен / не работает»**.

---

## 1. Канонические fatalities — Tesla Autopilot, Uber Tempe 2018, Boeing MCAS

### 1.1. Uber Tempe 2018 — first AV-pedestrian fatality (Elaine Herzberg)

- **Что произошло.** 18 марта 2018, ~22:00, Tempe (Arizona). **Elaine Herzberg**, 49 лет, переходила дорогу с велосипедом вне crosswalk. Uber test vehicle (Volvo XC90) в autonomous mode, скорость ~40 mph, ночь.
  - **System detected** Herzberg **за 5,6 секунд** до удара.
  - **Failed to classify** — bicyclist / pedestrian / unknown object.
  - **Не могла классифицировать как pedestrian вне crosswalk** (training data bias).
  - **Uber отключил** Volvo's factory automatic emergency braking system — полагался на human backup driver [1].
  - **Backup driver Rafaela Vasquez** — смотрела ТВ-шоу на телефоне; NTSB: была отвлечена 1/3 времени поездки [1].
- **Урок.**
  1. **Operational Design Domain (ODD) — критично**. Система работала за пределами своего training distribution (pedestrian вне crosswalk).
  2. **Safety driver attention — не reliable** при monotonous backup-роли (automation paradox).
  3. **Disabling factory safety systems** (Volvo AEB) ради «pure-AV evaluation» — анти-паттерн.
- **Правильная альтернатива.** Maintain factory AEB как защитный слой; ограничить ODD четко; multi-camera attention monitoring на safety driver'е (Tesla driver-monitor с 2022 — реакция на эту lesson).
- **Источники:** [Wikipedia — Death of Elaine Herzberg](https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg); [NBC News — Uber car did not recognize jaywalk](https://www.nbcnews.com/tech/tech-news/self-driving-uber-car-hit-killed-woman-did-not-recognize-n1079281).

### 1.2. Tesla Autopilot / FSD fatalities — NHTSA Standing General Order data

- **Числа (NHTSA + Wikipedia, к октябрю 2025).**
  - **65 reported fatalities** связанных с Autopilot / FSD (Full Self-Driving Supervised).
  - **54 verified** by NHTSA investigations / expert testimony [2].
  - NHTSA EA22002 investigation: **13 crashes с одним или несколькими fatalities**, где «foreseeable driver misuse of Autopilot played an apparent role» [2].
- **Конкретные patterns.**
  - **Reduced visibility crashes (2024 SGO data).** 4 crash reports — Tesla с FSD engaged въезжает в reduced visibility (sun glare, fog, dust); 1 fatality (pedestrian), 1 injury [3].
  - **Stationary emergency vehicles.** NHTSA investigation о неспособности Tesla Autopilot detect parked firetrucks/police cars (Aug 2021 — investigation start, expanded 2023).
- **NHTSA October 2025.** New investigation о ~2,9 миллионах Tesla vehicles с FSD по pattern reduced-visibility крашей [4].
- **Урок.**
  1. **Naming matters.** «Autopilot» / «Full Self-Driving» — terms which **invite over-reliance**; даже с safety disclaimers users полагаются больше, чем должны.
  2. **L2 driver-monitoring** — обязателен; ранние Tesla без strict driver-monitoring — overreliance pattern.
  3. **Edge cases в perception** (sun glare, parked emergency vehicles) — **distribution shift**, который сложно поймать в training.
- **Правильная альтернатива.** Strict L3 ODD definitions (Mobileye, Mercedes Drive Pilot); driver-monitoring camera + steering torque sensor; honest naming («Highway Pilot», не «Full Self-Driving»).
- **Источники:** [Wikipedia — List of Tesla Autopilot crashes](https://en.wikipedia.org/wiki/List_of_Tesla_Autopilot_crashes); [NHTSA EA22002](https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf); [Electrek — Fatal FSD crash NHTSA, окт 2024](https://electrek.co/2024/10/18/fatal-tesla-crash-with-full-self-driving-supervised-triggers-nhtsa-investigation/).

### 1.3. Boeing 737 MAX MCAS — 346 deaths, automation-trust failure

- **Что произошло.** Lion Air 610 (октябрь 2018, 189 deaths) + Ethiopian Airlines 302 (март 2019, 157 deaths). MCAS (Maneuvering Characteristics Augmentation System) — automated trim system, активировался по сигналу от **одного** angle-of-attack sensor (без redundancy), pushing nose down. Pilots не были tracked о существовании MCAS в training. Faulty AoA sensor → MCAS forced repeated nose-down trim → unrecoverable dive.
- **Урок (для logistics/transport AI).**
  1. **Automation без понятного pilot mental model** — recipe для disaster.
  2. **Single point of failure (один sensor) для safety-critical automation** — банально, но повторяется (cf. Tesla с одним forward camera в ранних моделях).
  3. **Human-in-the-loop трибуется только если human знает, что он in the loop**.
- **Связь с lec-13.** MCAS — не «logistics», но **canonical anti-pattern** для autonomous-vehicle design: **automation без disclosure + без redundancy = смерть**.
- **Source:** Wikipedia Boeing 737 MAX groundings; NTSB / FAA reports.

---

## 2. Серия банкротств autonomous-trucking — $10B+ сгорело за 2 года

### 2.1. Argo AI (Ford + VW) — октябрь 2022

- **Что произошло.** Argo AI основана 2016 ex-Google/Uber инженерами Bryan Salesky + Pete Rander. **$1 миллиард** Ford investment 2017. К 2020 — VW добавила; valuation ~$12,4B (2021).
- **Закрытие.** Октябрь 2022 — Ford + VW pull funding одновременно. **2 000+ employees** уволены. Ford recorded **$2,7 миллиарда non-cash impairment**, $827M net loss Q3 2022 [13].
- **Что сделали с активами.** Разделены: автономный stack — Ford & VW «in-house» (Latitude AI у Ford); reset to L2/L3 ADAS focus.
- **Корневые причины.**
  1. **Capital intensity AV-R&D** превысила terпение investors.
  2. **Robotaxi monetization timeline** — слишком далеко; OEM требуют ADAS roadmap, который cash flow generates сейчас.
  3. **Talent hyperexpensive** — Argo had 2 000 engineers, payroll alone ~$500M/year.
- **Урок.**
  1. **«Solve L4 robotaxi everywhere» — too big a problem для startup-scale capital.**
  2. **OEM как investors — fickle**; они вернулись к ADAS focus как только Wall Street начала спрашивать про cash burn.
- **Альтернатива.** Mobileye — listed company, focus на ADAS + Chauffeur (L3 narrow), positive operating cash flow. **Это пример того, как делать autonomy без сжигания капитала.**
- **Source:** [TechCrunch — Argo AI shutting down](https://techcrunch.com/2022/10/26/ford-vw-backed-argo-ai-is-shutting-down/); [CNBC — How Ford/VW Argo AI failed](https://www.cnbc.com/2023/03/22/how-ford-and-vws-multibillion-dollar-self-driving-car-project-failed.html).

### 2.2. Embark Trucks — март 2023, **16 месяцев от $5B IPO до банкротства**

- **Что произошло.** Embark — SF-based autonomous trucking. SPAC-merger ноябрь 2021, target market cap **$5,16 миллиарда**. CEO Alex Rodrigues (молодой founder).
- **Шестнадцать месяцев спустя.** Март 2023 — **230 employees уволены**, ликвидация активов. Сам CEO в press release: «The capital markets have turned their backs on pre-revenue companies» [16].
- **Урок.**
  1. **SPAC-IPO в hype-моменте** (2021) — позволяет raise capital без disclosing technology readiness.
  2. **Pre-revenue valuation $5B** для startup без production driverless — **price-irrational экосистемы** 2021.
  3. **Public-to-bust в год** — самая быстрая SPAC-AV смерть.
- **Альтернатива.** Stay private до production revenue; raise smaller rounds; align valuation с technical milestones.
- **Source:** [Crunchbase — Embark $5B to kaput in 16 months](https://news.crunchbase.com/transportation/embark-trucks-closes-autonomous-vehicles/); [TechCrunch — Embark layoffs](https://techcrunch.com/2023/03/03/embark-trucks-lays-off-workers-explores-liquidation-of-self-driving-truck-assets/).

### 2.3. TuSimple — delisting + China scandal (январь 2024)

- **Что произошло.** TuSimple — раньше leader US autonomous trucking. SEC investigation 2022-2023 о Chinese ties. Январь 2024 — delisting с Nasdaq. **Активы переведены в китайские entities** в AIGC (AI-generated content) gaming/animation — секторы, в которых **board members + officers имели personal interests**. Retail-investors потеряли **>91%** [17].
- **Урок.**
  1. **Governance матterс.** Технология может быть отличной — corporate structure уничтожит value.
  2. **Geopolitical alignment** — US-China tensions makes US-listed dual-jurisdiction AV companies vulnerable.
  3. **Asset stripping** — board members и officers могут выкачать value до того, как retail-investors замечают.
- **Source:** [SEC TuSimple SC 13D](https://www.sec.gov/Archives/edgar/data/0001823593/000092189524002952/ex991to13d14283002_112724.pdf).

### 2.4. Waymo Via — закрытие trucking arm (2023)

- **Что произошло.** Waymo Via — trucking arm Waymo, основан 2017–2018. 2023 — closed; refocus только на robotaxi. Reasoning Waymo: «trucking economics не worked at our cost structure» [public statement].
- **Урок.** Даже Alphabet, с unlimited capital, не нашёл profitable AV-trucking model. **Это не failure technology — это failure unit economics.**

### 2.5. Starsky Robotics — март 2020, **первая волна жертв**

- **Что произошло.** Starsky — pre-Argo, pre-Embark startup, **первая публично-видимая driverless truck demo** (без человека в кабине). Март 2020 — закрытие, runway закончился. Founder Stefan Seltz-Axmacher написал длинный post-mortem essay [«The end of Starsky Robotics»] — **must-read** для класса.
- **Урок (по essay).**
  1. **Supervised ML — slower than promised**, особенно edge cases.
  2. **Sim-to-real gap** в edge cases — недооценен.
  3. **Money-vs-progress gap** — investors хотят milestones каждый Q, ML breakthroughs не работают на Q-rhythm.
- **Source:** Medium «The end of Starsky Robotics» by Stefan Seltz-Axmacher.

### 2.6. Cumulative damage

- **Argo AI:** ~$7B (Ford $5B+, VW $2,6B стейк) [14].
- **Embark:** ~$300M IPO + private rounds.
- **TuSimple:** ~$1B + IPO proceeds.
- **Starsky:** ~$20M.
- **Cruise:** **$10B operating losses GM** (см. ниже).
- **Other (Aurora, Plus, Kodiak — survivors):** combined ~$2B+ raised, не сожжено.
- **Cумма:** **>$20 миллиардов** сожжено на autonomous-trucking + robotaxi non-survivors между 2017–2024.

**Lesson (структурный).** **AV-индустрия consolidated очень жестоко.** Из 30+ серьёзных AV/AV-trucking стартапов 2015–2020 — **выжили 3-4** (Waymo, Aurora, Mobileye на public-side; Apollo Go на Китайской стороне). Это означает: **студент, начинающий карьеру в AV в 2026, попадает в industry со survivorship bias 10:1**. Это **не «AI решает проблему» — это «AI сожрал капитал»**.

---

## 3. Cruise (GM) exit — **canonical robotaxi failure 2024**

### 3.1. Что произошло (timeline)

- **2016.** GM покупает controlling stake в Cruise за $581M.
- **2018–2023.** Cruise raises additional $5B+ (Honda, SoftBank Vision Fund, T. Rowe Price). Cumulative spend: ~$10B.
- **August 2023.** California DMV выдаёт Cruise commercial robotaxi license в SF — первая massive multi-thousand-vehicle deployment.
- **October 2, 2023.** **Pedestrian incident.** Pedestrian struck by **another vehicle**, отброшена под Cruise robotaxi; Cruise не остановилась немедленно — **dragged pedestrian 20 feet** (NTSB report). Серьёзные injuries.
- **October 24, 2023.** California DMV **suspended** Cruise license — citing «misrepresentation» (Cruise не show DMV full video footage initially).
- **2024 throughout.** Sequential closures по штатам; mass layoffs.
- **December 10–11, 2024.** GM announces **полный exit** из robotaxi-бизнеса. Cruise folded в broader tech team. Focus shift на Super Cruise (driver-assist на personal cars) [8][9].

### 3.2. Финансовая аналитика

- **Spent:** >$10 миллиардов operating losses (2016-2024) [8].
- **Revenue total:** **<$500 миллионов** за 8 лет [9].
- **Annual burn:** ~$1+ миллиард в year к 2023.
- **Analyst rationale GM exit:** «save more than $1 billion in capital annually» [9].

### 3.3. Корневые причины (multiple, structural)

1. **Trust collapse после October 2023 incident.** Cruise не остановилась немедленно при detecting pedestrian under vehicle — это **violation expected behavior**, и Cruise initial communication с DMV was **incomplete** (не показала full footage). Trust = **prerequisite** для regulatory permission.
2. **Cost structure unsustainable.** GM был ready покрывать $1B/year burn на R&D, но не на operations при <$500M revenue.
3. **Competitive pressure.** Waymo масштабировался быстрее, с лучшим safety record; Tesla готовил Robotaxi launch (Austin June 2025). Cruise был **squeezed между двумя гигантами**.
4. **Cultural mismatch.** GM — automotive OEM (DCF cycles); Cruise — SF-style fast-burn startup. **Hardware company → software-platform pivot — anti-pattern** (как GE Predix, см. lec-11 file 04).

### 3.4. Урок

1. **Один инцидент может убить bilion-dollar program**, если trust violated.
2. **«We can fix this» — недостаточно**, если regulators feel deceived.
3. **Single-state license = single point of regulatory failure**; распределение по multiple jurisdictions более резилиентно (Waymo стратегия).
4. **Robotaxi cost structure**: даже Waymo не profitable per-trip; **operations economics far harder than perception/control**.

### 3.5. Альтернатива

- **Waymo подход:** HD-map + LiDAR + remote ops + formal safety case + slow-and-steady geographic expansion. Doesn't try «universal» AV — focuses на city-by-city ODD.
- **Mobileye подход:** stay в ADAS + L3 Chauffeur narrow ODD; не attempt robotaxi пока unit economics не понятны.
- **Pony.ai подход (China):** позитивный operating profit per vehicle сначала в одном городе (Shenzhen Feb 2025), потом скейлинг — **economics first, scale second**.

### 3.6. Источники

- [CNBC — GM Cruise shutdown](https://www.cnbc.com/2024/12/15/end-of-gm-cruise-driverless-robotaxi.html); [NPR — GM retreats](https://www.npr.org/2024/12/11/g-s1-37700/gm-to-retreat-from-robotaxis-and-stop-funding-its-cruise-autonomous-vehicle-unit); [Smart Cities Dive — GM shuts Cruise](https://www.smartcitiesdive.com/news/general-motors-shuts-cruise-robotaxi-unit-mary-barra/735205/).

---

## 4. Tesla Robotaxi Austin — текущая инцидент-разработка (май 2026)

### 4.1. Что зарегистрировано

- **Старт:** июнь 22, 2025 в Austin, ~10 машин с safety monitor [5].
- **К февралю 2026:** **14 ДТП** в Austin с момента запуска [7].
- **Декабрь 2025:** начало unsupervised тестирования (с employees).
- **Январь 2026:** public unsupervised поездки.
- **Апрель 2026:** unsupervised в Houston, Dallas.

### 4.2. Pedagogical use (без demonization)

- **Comparison необходим.** 14 ДТП за 8 месяцев в Austin при ~10 машинах ≈ 1.75 ДТП/месяц/fleet. Waymo: ~500K поездок/неделю, NHTSA data показывает significantly lower crash rate per mile (но direct mile-comparison у Waymo больше, поэтому absolute number ДТП у Waymo тоже выше).
- **Что Tesla показала.** Vision-only (без LiDAR), без HD-map — **technically possible**. Что НЕ доказано: **safer than Waymo** (sample size слишком мал).
- **Lesson для лекции.** **Не делать категоричные выводы на основе 8 месяцев + 10 машин.** Студент должен знать **где сравнивать справедливо** (per-million-miles crash rate, не absolute count). Это **anti-confirmation-bias** lesson.

### 4.3. Источники

- [Wikipedia Tesla Robotaxi](https://en.wikipedia.org/wiki/Tesla_Robotaxi); [National Today — 14 crashes](https://nationaltoday.com/us/tx/austin/news/2026/02/19/tesla-robotaxis-involved-in-14-crashes-in-austin-since-2025-launch/).

---

## 5. Black-swan disruptions — где ML слепо

### 5.1. Houthi Red Sea 2024 — ML demand-forecast catastrophic failure

- **Что произошло.** С декабря 2023 атаки хуситов на коммерческие суда в Красном море. Major shipping lines (Maersk, MSC, Hapag-Lloyd) перенаправляют через Cape of Good Hope (+10–14 дней). К началу 2024 — **container shipping через Red Sea упал на 90%** (US Defense Intelligence Agency). Daily transit trading volume — с 4M метрических тонн до 1,7M (–57,5%) [Houthi-1].
- **Что не сработало в ML.** ML demand forecast models, обученные на 2010–2022 данных, **никогда не видели**: (a) 90% drop в Suez traffic; (b) +30% transit time от Asia к Europe; (c) +9% reduction в effective global container capacity. Distribution shift настолько extreme, что models **полностью out-of-distribution**.
- **Что сработало.** **Human dispatchers + carrier exception teams**. ML reverted к **planning support**, а не **decision-making**.
- **Урок.** **Black-swan = ML failure mode**. ML работает в-distribution; out-of-distribution — это **human judgment + scenario planning**.
- **Альтернатива.** **Scenario planning** (war-room style), **rule-based fallback** (force-rule manually disable routing through area), **insurance + reserve capacity** (operations research approach).
- **Источники:** [Atlas Institute — Red Sea crisis 2024-2025](https://atlasinstitute.org/the-red-sea-shipping-crisis-2024-2025-houthi-attacks-and-global-trade-disruption/); [J.P. Morgan — Red Sea shipping impacts](https://www.jpmorgan.com/insights/global-research/supply-chain/red-sea-shipping).

### 5.2. Suez Ever Given 2021 — physics + human pilotage failure (AI couldn't help)

- **Что произошло.** 23–29 марта 2021. **Ever Given** (400m container ship, ~200K тонн) — застрял в Suez canal на 6 дней из-за strong wind + pilot error. **12% world trade** прошло через Suez; **$9,6 миллиарда** goods held up; **$400M/час delay cost** estimates Bloomberg [Suez-1].
- **Что AI НЕ мог.** **Physical extraction** требовала dredging, tug boats. AI не имела роли. Wind prediction — да, но shipping company already had weather data.
- **Урок.** **Не всё в logistics — AI problem.** Часть задач — **физика, pilotage, port operations** — где AI **не релевантна**.
- **Альтернатива.** **Better wind-restriction policies для giant ships в narrow channels** (post-Ever-Given Suez Canal Authority introduced this). **Physical infrastructure investment** (Suez canal expansion).
- **Source:** [Wikipedia — 2021 Suez Canal obstruction](https://en.wikipedia.org/wiki/2021_Suez_Canal_obstruction); [Bloomberg estimate цитирован в University of Gothenburg](https://www.gu.se/en/news/the-cost-of-the-suez-canal-blockage).

### 5.3. COVID-19 supply-chain meltdown (2020–2022)

- **Что произошло.** Pandemic-induced demand shock + factory shutdowns + container shortage + port congestion → **ML demand forecasts полностью wrong для 2020–2021**.
- **Что сработало.** **Human exception management**, **emergency suppliers**, **strategic inventory hoarding** (anti-just-in-time). ML reverted to **decision support** при scenario uncertainty.
- **Урок.** **Just-in-time supply chains + ML demand forecast = fragile system**. Resilience требует **redundancy**, а не optimization to the edge.

### 5.4. Driver shortage не решён ИИ

- **ATA 2024 data.** **78 000 водителей** дефицит в US trucking; **1,2 миллиона новых нужны за десятилетие** [ATA].
- **Aurora 2026 status.** ~10 driverless trucks в commercial operation.
- **Math.** Даже если каждый survival AV-trucking startup deploy 1 000 единиц к 2030 — это **<10% от deficit**.
- **Урок.** **AV не масштабируется быстро enough**, чтобы решить human-labor problems за десятилетие. **Структурные labor solutions** (visa policies, training subsidies, working conditions) — это **другая** инструментарий.
- **Source:** [ATA Driver Shortage Report 2024](https://www.trucking.org/news-insights/ata-releases-updated-driver-shortage-report-and-forecast).

---

## 6. Где AI НЕ нужен / WRONG TOOL — фундаментальные критерии

### 6.1. OR (operations research) > RL для well-defined routing

- **Контекст.** Vehicle Routing Problem (VRP), Travelling Salesman (TSP) — **NP-hard, но десятилетиями optimized** через linear programming + heuristics (Gurobi, CPLEX, Google OR-Tools).
- **Что RL даёт хуже.** Approximation (без optimality guarantees), more compute, harder to debug. **UPS ORION = OR + heuristics, не RL** — это **самый успешный routing-AI в industry** [26].
- **Когда RL лучше.** Когда objective function unknown / changes dynamically (e.g., real-time demand surge с new pricing); когда state space too large для classical OR.
- **Lesson.** **RL — не magic bullet** для logistics routing. **OR — proven, defensible, explainable**. Vendor selling «RL routing» — **demand benchmark vs OR baseline**.
- **Sources:** Bertsimas + Tsitsiklis textbooks; [Google OR-Tools docs](https://developers.google.com/optimization).

### 6.2. EOQ / safety-stock formulas > ML для stationary demand

- **Контекст.** Economic Order Quantity (EOQ) — 1913 Harris formula. Safety stock = z × σ × √L. Эти **classical inventory formulas** работают для stationary demand (Gaussian / Poisson distributions).
- **Где ML overkill.** Если SKU имеет stable seasonal demand pattern (e.g., shampoo, toilet paper) — **classical forecasting + safety stock margins** лучше + дешевле + объяснимее.
- **Где ML лучше.** Highly variable demand с external signals (weather-driven, event-driven). New SKU без historical data — Bayesian approaches.
- **Lesson.** **«ML inventory optimization» как blanket solution = overengineering** для stable SKUs. Audit: какая % SKU действительно требует ML vs classical formulas?

### 6.3. Formal verification + HD-map + remote ops > pure end-to-end DNN для safety-critical AV

- **Контекст.** Waymo подход: HD-map (precomputed lane geometry, traffic signs, crosswalks) + multi-sensor (camera + LiDAR + radar) + remote operators backup + formal safety case (independent assessment).
- **Wayve подход (research):** pure end-to-end DNN, без HD-map.
- **Production-status 2026.** Waymo — 500K поездок/неделю, commercial. Wayve — pre-production, partnership stage. **End-to-end не доказан на L4 production safety**.
- **Tesla подход:** vision-only без LiDAR, без HD-map — **технически возможно, но 14 ДТП за 8 месяцев в Austin** ставит вопрос о comparability с Waymo.
- **Lesson.** Для **safety-critical** AV — **redundancy (multi-sensor) + formal verification + remote ops** доказаны. Pure DNN — research-stage; **promising но не production-safe**.
- **Source:** Waymo Safety Report; Mobileye Responsibility-Sensitive Safety (RSS) framework.

### 6.4. Human dispatcher > full automation для exception handling

- **Контекст.** Diversion при weather, accident, geopolitical crisis (Houthi Red Sea), port strike (ILA 2024 US East Coast).
- **Что full-automation не делает.** **Out-of-distribution decisions** — например, «route everything around Cape of Good Hope at 2× cost», когда training data никогда такого не видела.
- **Что human делает.** **Scenario reasoning**, organizational coordination, accountability.
- **Lesson.** **Exception handling = human-in-loop**; automation для routine; **switching threshold должен быть explicit**, не emergent.

### 6.5. Когда дрон НЕ подходит для доставки

- **Where drone works.** Rural Africa (Zipline) — large distances, no roads, medical urgency, low population density (sound + airspace issues minimal).
- **Where drone doesn't work.** Dense urban US — **acoustic complaints**, **FAA / EASA airspace regulations**, **package theft / vandalism**, **last-100-feet handoff** (как робот / дрон передаёт package в apartment в 10-этажке?).
- **Lesson.** **Modality fit к environment** — основной фактор. Drone успешный там, где альтернатива (truck) **значительно хуже**.

### 6.6. Когда LLM НЕ подходит для logistics

- **Что LLM работает.** Documentation parsing, conversational ETA queries, claim disputes (с human review), vendor email triage.
- **Что НЕ работает.** **Quantitative optimization** (routing, inventory) — LLM плохо в numerical reasoning по сравнению с OR; **safety-critical control** (AV) — LLM нет real-time guarantees; **decision-making с financial impact** без verification — LLM hallucinations.
- **Anti-pattern.** «GenAI agent сам распланирует supply chain» — vendor pitch без production deployment. **Demand: specific ROI metric, baseline comparison, error budget**.

---

## Summary — критерии «здесь AI не нужен / не работает» (для лекционного слайда)

> **AI не подходит / не нужен в logistics, если хотя бы один из:**
> 1. **Задача well-defined optimization** (TSP, VRP, scheduling) → **OR + Gurobi/CPLEX/OR-Tools лучше**.
> 2. **Demand pattern stationary** + few external signals → **EOQ / classical forecasting лучше**.
> 3. **Safety-critical с regulatory requirement audit-trail** (aviation control, pharma cold-chain) → **rule-based + human-in-loop required**.
> 4. **Black-swan event** (geopolitical, pandemic, port-strike) → **human dispatcher + scenario planning**.
> 5. **Physical infrastructure problem** (Suez channel width, port crane capacity) → **engineering, not AI**.
> 6. **Labor shortage at scale** → **policy + training, not just AV deployments** (math doesn't work).
> 7. **Pilot demonstration ≠ production-ready** → **ask о 6-month production track record**.
> 8. **Vendor unable to articulate baseline** «AI delivers –50%» без specific baseline / counterfactual → **buyer beware**.
> 9. **Dense urban regulatory complexity** (drone в US cities) → **wait for regulation, не deploy by default**.
> 10. **End-to-end DNN claim safety-critical L4** без redundancy / formal verification → **trust survivor approach** (Waymo HD-map + LiDAR), не disruptor pitch.

**Альтернативы — must-know toolset для logistics-engineer:**
- **OR (operations research)** — Gurobi, CPLEX, OR-Tools для routing, scheduling, network design.
- **Classical inventory** — EOQ, safety stock, ABC analysis для stationary demand.
- **Scenario planning** — Shell-style war games, war-room exercises для black-swan readiness.
- **Rule-based vision** — для controlled-environment inspection (port crane vision, conveyor inspection).
- **Hybrid CV + classical signal processing** — radar, ultrasonic, IR — там где DNN brittle.
- **Human-in-the-loop** — exception handling, regulatory audit, accountability for safety decisions.

---

## Источники cross-reference

- [Wikipedia — Death of Elaine Herzberg](https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg)
- [Wikipedia — List of Tesla Autopilot crashes](https://en.wikipedia.org/wiki/List_of_Tesla_Autopilot_crashes)
- [NHTSA EA22002 investigation](https://static.nhtsa.gov/odi/inv/2022/INCR-EA22002-14496.pdf)
- [Electrek — Tesla FSD investigation 2024](https://electrek.co/2024/10/18/fatal-tesla-crash-with-full-self-driving-supervised-triggers-nhtsa-investigation/)
- [CNBC — GM Cruise shutdown](https://www.cnbc.com/2024/12/15/end-of-gm-cruise-driverless-robotaxi.html)
- [NPR — GM retreats robotaxis](https://www.npr.org/2024/12/11/g-s1-37700/gm-to-retreat-from-robotaxis-and-stop-funding-its-cruise-autonomous-vehicle-unit)
- [TechCrunch — Argo AI shutdown](https://techcrunch.com/2022/10/26/ford-vw-backed-argo-ai-is-shutting-down/)
- [CNBC — Ford VW Argo AI failed](https://www.cnbc.com/2023/03/22/how-ford-and-vws-multibillion-dollar-self-driving-car-project-failed.html)
- [Crunchbase — Embark 16 months](https://news.crunchbase.com/transportation/embark-trucks-closes-autonomous-vehicles/)
- [SEC TuSimple SC 13D](https://www.sec.gov/Archives/edgar/data/0001823593/000092189524002952/ex991to13d14283002_112724.pdf)
- [Atlas Institute Red Sea crisis](https://atlasinstitute.org/the-red-sea-shipping-crisis-2024-2025-houthi-attacks-and-global-trade-disruption/)
- [J.P. Morgan Red Sea](https://www.jpmorgan.com/insights/global-research/supply-chain/red-sea-shipping)
- [Wikipedia Suez 2021](https://en.wikipedia.org/wiki/2021_Suez_Canal_obstruction)
- [ATA Driver Shortage](https://www.trucking.org/news-insights/ata-releases-updated-driver-shortage-report-and-forecast)
- [INFORMS UPS ORION](https://www.informs.org/Impact/O.R.-Analytics-Success-Stories/Optimizing-Delivery-Routes)
- [National Today Tesla 14 crashes](https://nationaltoday.com/us/tx/austin/news/2026/02/19/tesla-robotaxis-involved-in-14-crashes-in-austin-since-2025-launch/)

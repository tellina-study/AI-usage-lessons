# 04 — Keystone-axis options для Лекции 13

**Summary.** 4 варианта несущей оси с сопоставлением: что keystone-слайд покажет, как раскладываются 5 разделов 75-мин лекции, какие провалы локализуются на стыках, какой риск. В конце — рекомендация. Для Phase 1 plan; final axis выбирается на USER GATE A.

**Контекст:**
- **lec-09 (защита/космос)** использовал OODA (Sense→Decide→Act) с лестницей автономии L1–L5.
- **lec-11 (производство)** использовал Variant C: «Дискретное vs процессное — две модели».
- **lec-13 (логистика и транспорт)** — отраслевая модуль 3, focus на критическое суждение (когда AI работает / не работает). Должен быть unifying frame, который **подаёт failure-bucket ≥30% органично** и **не дублирует lec-09/lec-11 структурно**.

---

## Вариант A: «Лестница автономии × сегмент» — 5 SAE levels × 4 сегмента

### Идея

SAE J3016 — международный standard для автономии транспортных средств. 6 levels (0 = no automation, 5 = full driverless everywhere). Logistics + transport segments: road, warehouse, last-mile, sea-air-rail. Двумерная матрица: keystone-слайд показывает её, каждый раздел = column.

### Keystone-slide

Матрица: вертикаль — SAE levels (L0-L5), горизонталь — сегменты. Каждая клетка — пример. Зелёные клетки = mature production; жёлтые = pilot; красные = stuck / impossible. Видно, что **L5 нигде не достигнут**; **L4 — только в narrow ODDs**.

### Раскладка 75-мин:
- §0 (5 мин) — Hook + keystone (матрица).
- §1 (15 мин) — **L0–L2 (driver-assist + ADAS).** Mobileye SuperVision, КамАЗ Маяк-2.5, классический cruise control. Failures: Tesla Autopilot fatalities, automation paradox.
- §2 (15 мин) — **L3 (conditional automation).** Mercedes Drive Pilot, Mobileye Chauffeur, Aurora L3-pre-L4. Failures: edge cases в перехвате контроля.
- §3 (15 мин) — **L4 (high automation в narrow ODD).** Waymo, Aurora driverless, Apollo Go, port-cranes. Failures: Cruise, Tesla Robotaxi 14 ДТП Austin, Argo/Embark/TuSimple bankruptcies.
- §4 (15 мин) — **L5 — миф?** Что **никто не достиг**; почему «universal AV» — moving goalpost.
- §5 (10 мин) — Synthesis + bridge to lec-14.

### Плюсы
- **Industry-standard frame.** SAE известно инженерам, в automotive — lingua franca.
- **Clear maturity gradient.** L2 mainstream; L3 emerging; L4 narrow; L5 не существует.
- **Failure cases органично распределены** по levels (Tesla на L2 fatalities, Cruise на L4).

### Минусы
- **Только automotive applies cleanly.** Warehouse robots, drones, ships — **не fits SAE J3016**. Принуждение taxonomy создаёт false equivalencies.
- **Не показывает почему среда матерается** — SAE classifies vehicle, не environment.
- **Дублирует lec-09 структуру L1-L5** — там уже была лестница автономии.

### Риск
- **Лестница SAE как ось — слишком automotive-centric**, не universal для logistics.

---

## Вариант B: «Горизонт решения» — split-second → minutes → days → months

### Идея

AI в transport/logistics решает задачи на разных временных горизонтах. На разных горизонтах — разные ML approaches и разные failure modes.

- **Split-second (ms-sec):** perception, emergency braking, lane keeping. **DNN, vision, sensor fusion.** Failure: edge case perception (Uber Tempe, Tesla reduced-visibility).
- **Minutes:** dynamic routing, dynamic pricing, surge management. **RL, bandits, OR.** Failure: distribution shift при events (Houthi).
- **Hours-days:** ETA prediction, last-mile dispatching, exception handling. **ML + OR hybrid.** Failure: just-in-time fragility (COVID).
- **Weeks-months:** demand forecasting, fleet planning, capacity expansion. **Time-series ML, scenario planning.** Failure: black-swan (Suez, Houthi).
- **Years:** network design (где строить hubs), capital allocation, regulatory strategy. **Human + OR + scenario.** AI — assist, не decision.

### Keystone-slide

Horizontal axis = time horizon (logarithmic: ms → sec → min → hours → days → weeks → months → years). На каждом горизонте — иконка типа AI + dominant tool + canonical failure case. Зелёная-к-красной градация: ms-min (хорошо ML), months-years (плохо ML, exception handling).

### Раскладка 75-мин:
- §0 (5 мин) — Hook + keystone.
- §1 (15 мин) — **Split-second.** Perception, AV control, emergency braking. Cases: Mobileye, Waymo, Tesla. Failures: Uber Tempe, Tesla.
- §2 (15 мин) — **Minutes.** Dynamic routing, surge pricing, real-time replanning. Cases: UPS ORION (но OR!), Uber surge, Yandex Go. Failures: distribution drift на events.
- §3 (15 мин) — **Days.** Last-mile dispatching, exception handling. Cases: Locus / Coco / FedEx. Failures: just-in-time fragility, COVID.
- §4 (15 мин) — **Months / Years.** Demand forecast, network design. Cases: Maersk, P&G, Amazon hub planning. Failures: Houthi black-swan, Suez Ever Given.
- §5 (10 мин) — Bridge: где AI работает на каждом горизонте? → lec-14.

### Плюсы
- **Cross-segment unifying** — applies к road, warehouse, last-mile, sea одинаково.
- **Failure modes mapped к horizons** — distribution shift на longer horizons усиливается.
- **Pedagogical clarity** — студент уносит ось «horizon = predictor AI applicability».

### Минусы
- **Менее industry-natural** — engineers думают «warehouse vs road», не «split-second vs days».
- **Failure-bucket concentration на длинных горизонтах** (Houthi, Suez) — может быть hard to balance ≥30% strict-in.
- **Risk «too abstract»** — academic vs concrete.

### Риск
- Студент уходит с framework, но без specific tool knowledge. **Mitigation:** rich cases на каждом horizon.

---

## Вариант C: «Структурированность среды vs хаос» (РЕКОМЕНДУЮ)

### Идея

AI в transport/logistics работает дифференциально в зависимости от **структурированности среды**. Это **главный предиктор success**, и он orthogonal к SAE levels или временным horizons.

**Лестница среды (5 уровней):**
1. **Controlled (warehouse, port terminal, fab floor).** Closed environment, known SKU, no pedestrians, GPS работает. **AI mature: Symbotic, Amazon Sparrow, ZPMC port cranes.**
2. **Semi-structured highway (Interstate / магистраль).** HD-maps есть, lane geometry понятна, weather variation. **AI emerging: Aurora driverless trucks, КамАЗ Маяк-2.5.**
3. **Urban robotaxi (city streets).** HD-maps + remote ops + LiDAR; pedestrians, weather, exceptions. **AI emerging но fragile: Waymo (works), Cruise (collapsed), Tesla Austin (early).**
4. **City last-mile (sidewalks + entrances).** Edge: куда положить package? sidewalk regulation? **AI struggling: Coco, Starship work в narrow campus / specific neighborhoods.**
5. **Exception / black-swan (geopolitical crisis, port strike, pandemic).** Distribution shift extreme. **AI fails: Houthi 2024, Suez 2021, COVID 2020.**

### Keystone-slide

5-step ladder: слева controlled (warehouse iconography), справа chaos (storm + ships rerouting). На каждом шаге — представитель AI (Symbotic → Aurora → Waymo → Coco → human dispatcher), измеримый эффект, типичный failure mode.

### Раскладка 75-мин:
- §0 (5 мин) — Hook + keystone (лестница среды). Опен с Cruise inferno как наглядный show: $10B сожжено в самом chaotic уровне.
- §1 (15 мин) — **Уровень 1 — Controlled.** Warehouse + port. Cases: Symbotic + Walmart 400 APD, Amazon Sparrow/Sequoia/Proteus/Vulcan, Rotterdam Maasvlakte II, KONUX rail. **Что работает:** PdM, vision QC, AMR. **Failure для balance:** humanoid hype (Optimus / Figure не в production).
- §2 (15 мин) — **Уровень 2 — Highway robotruck.** Cases: Aurora Dallas-Houston май 2025, КамАЗ М-11 «Нева». **Что работает:** L3-L4 в narrow ODD, OR-routing (UPS ORION). **Failure deep-dive:** Argo AI Oct 2022 ($7B сгорело), Embark Mar 2023 ($5B IPO → kaput 16 мес.), TuSimple Jan 2024 delisting, Waymo Via shutdown.
- §3 (15 мин) — **Уровень 3 + 4 — Urban robotaxi + last-mile.** Cases: Waymo (500K/неделю), Apollo Go (17M заказов), Pony.ai, Coco LA, Starship campuses, Zipline Africa. **Failure deep-dive:** **Cruise GM exit Dec 2024** (centerpiece), Uber Tempe 2018, Tesla Austin 14 crashes, Tesla Autopilot 54 verified fatalities NHTSA.
- §4 (15 мин) — **Уровень 5 — Exception / where AI breaks.** Cases: Houthi Red Sea 2024 (90% traffic drop, ML demand forecast failed), Suez Ever Given 2021 (12% world trade), COVID 2020 supply chain meltdown, trucker shortage 78K (AV не решит). **Right tool:** human dispatcher + scenario planning + OR (UPS ORION = OR не RL); EOQ formulas > ML для stationary; formal verification + redundancy для safety-critical.
- §5 (10 мин) — Synthesis: где AI applicable как функция среды; bridge к lec-14 (telecom + кибербез — другая среда, другие правила).

### Плюсы
- **Industry-real frame.** Engineers сразу видят, почему warehouse AI mature а urban robotaxi — survivor-takes-all.
- **≥30% failure strict-in достижим органично.** §2 — 4 bankruptcy кейса; §3 — Cruise + Tesla + Uber Tempe; §4 — full failure section. Distributed evenly через 3 sections (not concentrated в одном артефакте).
- **Cross-modality** — works одинаково для road, warehouse, drone, ship.
- **Не дублирует lec-09 OODA** (там — sensor-loop) **или lec-11 discrete/process** (там — production-type).
- **Strong bridge from lec-12** (automation + digital twins — высоко-controlled environment) **and to lec-14** (telecom — different среда, different AI).
- **Keystone слайд visual-strong** — ladder с progressively chaotic images: clean warehouse → highway → city → snowy sidewalk → storm at sea.

### Минусы
- **«Структурированность» — не jargon-term**; нужен 2-3 минутный intro.
- **Граница уровней нечёткая** — где highway заканчивается, urban начинается? Mitigation: keystone слайд использует **canonical examples**, не precise definitions.
- **Risk «environment determinism»** — студент может уйти с «AI works where structured» как deterministic правило, забывая что **inside structured environments тоже бывают failures** (Symbotic capital-intensive, Amazon Vulcan compensates Sparrow gaps). Mitigation: явный disclaimer в keystone — «структурированность ≠ гарантия».

### Риск
- Если §4 too concentrated на failure cases, может feel «doom porn». **Mitigation:** §4 framing — «вот где AI breaks → вот правильные альтернативы (OR, scenario planning, human dispatcher)».

---

## Вариант D: «Volatile decision tree» — критерий-фрейм

### Идея

5-step decision tree:
1. **Is environment controlled?** Yes → warehouse/port AI. No → continue.
2. **Is path/route well-defined?** Yes → use OR (Gurobi, CPLEX). No → continue.
3. **Is task safety-critical with regulatory audit?** Yes → human-in-loop required. No → continue.
4. **Is task time-horizon < seconds?** Yes → DNN perception/control. No → continue.
5. **Is event in-distribution?** Yes → ML scoring. No → human dispatcher + scenario planning.

### Pros
- **Maximally aligned с failure-bucket philosophy** (каждый step — «can/can't apply AI»).
- **Pedagogically strongest** — student leaves with applicable framework.

### Cons
- **Меньше narrative, больше algorithm**. Может feel «academic».
- **Industry-кейсы как examples, не как backbone** — может lose visual impact.

---

## Рекомендация

**Брать Вариант C — «Структурированность среды».**

**Почему:**
1. **Failure-bucket ≥30% strict-in достижим органично** без single-artifact concentration. §2 (banking AV bankruptcies), §3 (Cruise + Tesla), §4 (black-swan).
2. **Industry-real frame.** Engineers реально think «warehouse vs road vs last-mile» — это natural mental model.
3. **Cross-modality applies** к всем 4 segmentам (road, warehouse, last-mile, sea/air/rail).
4. **Не дублирует lec-09 OODA или lec-11 discrete/process.**
5. **Bridges natural.** lec-12 (automation/digital twins) ↔ lec-13 (logistics environment ladder) ↔ lec-14 (telecom = different env).
6. **Keystone visual-strong** — ladder с progressively chaotic images создаёт visual punch.
7. **Hook потенциал.** Можно открыть с Cruise inferno ($10B → 0 за 8 лет) → вопрос «почему даже Alphabet Waymo делает 500K/неделю а Cruise обанкротился? Среда матерается».

**Hybrid recommendation:** Вариант C + усиление в §4 «когда не AI» через Вариант D decision-tree logic. То есть структура C-based, но §4 (15 мин) — это явно decision framework + alternatives, где Variant D logic incarnated. Это даёт **strongest failure-bucket + applicable judgement framework + environment-real backbone**.

**Финальная structure proposal для Plan v1:**
- **§0 (5 мин)** — Hook (Cruise $10B → 0 + Tesla 14 ДТП Austin + Waymo 500K/неделю juxtaposition) + keystone «лестница среды».
- **§1 (15 мин)** — **Controlled (warehouse + port).** Symbotic 400 APD, Amazon Sparrow/Sequoia/Proteus/Vulcan, KONUX, port automation. Что работает + границы (humanoid hype balance).
- **§2 (15 мин)** — **Semi-structured highway.** Aurora Dallas-Houston, КамАЗ М-11. OR-routing UPS ORION. **Failure deep-dive:** Argo AI / Embark / TuSimple / Waymo Via — $20B+ AV-trucking сгорел.
- **§3 (15 мин)** — **Urban (robotaxi + last-mile).** Waymo, Apollo Go, Coco, Starship, Zipline. **Failure deep-dive:** **Cruise GM exit** (centerpiece), Uber Tempe, Tesla NHTSA fatalities, Tesla Austin 14 crashes.
- **§4 (15 мин)** — **Exception / where AI breaks + decision framework.** Houthi 2024, Suez 2021, COVID, trucker shortage. **Альтернативы:** OR (UPS ORION = OR not RL), EOQ classical inventory, scenario planning, formal verification + redundancy, human dispatcher.
- **§5 (10 мин)** — Synthesis + bridge: lec-14 (telecom — другая среда, другие AI patterns).

**Failure-bucket budget (preview, см. plan для details):**
- §1: ~3 мин (humanoid hype balance, Symbotic capital risk).
- §2: ~10 мин (AV bankruptcies = bulk of section).
- §3: ~10 мин (Cruise + Tesla Austin + Uber Tempe).
- §4: ~13 мин (целиком failure / judgement).
- **Total strict-in failure/judgement contents: ~36 мин / 75 = 48%** — comfortably > 30%, distributed evenly через все sections (3, 10, 10, 13).

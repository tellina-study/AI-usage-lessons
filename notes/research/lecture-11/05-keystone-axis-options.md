# 05 — Keystone-axis options для Лекции 11

**Summary.** 4 варианта несущей оси лекции с сопоставлением: что keystone-слайд покажет, как раскладываются 5 разделов 75-мин лекции, какие провалы локализуются на стыках, какой риск. В конце — рекомендация. Для Phase 1 plan; final axis выбирается на USER GATE A.

**Контекст:** lec-09 (предшествует) использовал OODA (Sense→Decide→Act). Лекция 11 — отраслевая модуль 2, fokus на критическое суждение (когда AI работает / не работает). Должен быть unifying frame, который **подаёт failure-bucket ≥30% органично**, а не «нашлёпан сверху».

---

## Вариант A: «Цикл производства» = Sense → Decide → Act → Learn

### Идея
Production = continuous loop: **Sense** (sensors, vision) → **Decide** (model recommend / classify) → **Act** (actuator, operator, valve) → **Learn** (feedback to model). Этот цикл универсален для discrete и process; AI вторгается на каждом шаге.

### Keystone-slide
Картинка: 4-stage loop (стрелки замыкают цикл). На каждом этапе — пример AI и пример где AI ломается. В центре — «человек+машина», который держит loop honest.

### Раскладка 75-мин:
- §0 (5 мин) — Hook + keystone «cycle of production».
- §1 (15 мин) — **Sense.** Vision/sensors/soft-sensors. Кейсы: BMW GenAI4Q, BASF Geismar soft sensors, TSMC wafer CV. **Failures here:** low-contrast defects, distribution shift, mislabel.
- §2 (15 мин) — **Decide.** Anomaly detection, predictive maintenance, formulation suggestion. Кейсы: Pfizer Vox, POSCO 180 edge nodes, Holcim C3 AI kiln. **Failures here:** SPC vs ML false-positive, PdM pilot-purgatory, F-35 ALIS.
- §3 (15 мин) — **Act.** Robotic assembly, process control, agentic copilots. Кейсы: Foxconn FoxBrain, Toyota GAIA, Yokogawa-JSR FKDPP 35 days. **Failures here:** Tesla over-automation 2018, RL distribution drift, Boeing 737 door plug.
- §4 (15 мин) — **Learn / Don't.** Feedback loops, retraining, organizational rejection. Кейсы: GE Predix, IBM Watson, Foxconn Wisconsin, pilot purgatory stats. **Failures here:** все hype-collapses сюда.
- §5 (10 мин) — Synthesis + bridge to lec-12.

### Плюсы
- **Универсален для discrete + process.** Не разделяет artificially.
- **Failure cases органично распределены** по 4 этапам — ≥30% strict-in достижим без single concentrate.
- **Знаком студенту через lec-09 OODA** — продолжение проверенной структуры (cognitive consistency).
- Каждый из 4 этапов имеет clear vendor-tool examples + clear failure cases.

### Минусы
- Близок к lec-09 (OODA → Sense/Decide/Act). Студент может почувствовать «то же самое».
- «Learn» loop в production реже четко выделен — может потребовать convincing.

### Риск
- Plagiarism / copy-of-lec-09 perception. **Митигация:** явный contrast — defense (lec-09) vs production (lec-11). OODA — про boundary system; SDA-Learn — про continuous improvement loop.

---

## Вариант B: «Пирамида автоматизации ISA-95» — AI на каждом уровне

### Идея
ISA-95 — международный standard для enterprise-control integration. 5-уровневая пирамида:
- **Level 4** — ERP / business planning.
- **Level 3** — MES (Manufacturing Execution System), CMMS, scheduling.
- **Level 2** — SCADA / HMI.
- **Level 1** — PLC / control loops.
- **Level 0** — Process / production line (sensors, actuators).

AI вторгается на каждом уровне с разной зрелостью и разными failure modes.

### Keystone-slide
Пирамида ISA-95, на каждом уровне — иконка AI-application + дата зрелости + лидер. Сверху вниз: AI maturity decreases (highest ERP, lowest physical process). Сверху вниз: latency requirement increases (sec → ms).

### Раскладка 75-мин:
- §0 (5 мин) — Hook + ISA-95 keystone.
- §1 (15 мин) — **L4 ERP-уровень.** Supply chain, demand forecasting, agentic copilots. Кейс: Coca-Cola Microsoft $1.1B; foreshadow lec-13 (logistics).
- §2 (15 мин) — **L3 MES + scheduling.** Production planning, predictive maintenance, golden batch. Кейсы: Pfizer Vox, Toyota GAIA, Tata Steel. **Failures:** GE Predix, IBM Watson.
- §3 (15 мин) — **L2 SCADA + HMI.** Agentic copilots на operator-уровне, anomaly detection. Кейсы: Siemens IFM, Schneider Electric + Microsoft. **Failures:** F-35 ALIS, false-positive cost.
- §4 (20 мин) — **L1+L0 PLC + process.** Edge AI, RL process control, CV inspection. Кейсы: POSCO edge nodes, Yokogawa FKDPP, BMW GenAI4Q. **Failures:** Tesla over-automation, RL distribution drift, ATEX limits, FDA Part 11.
- §5 (5 мин) — Bridge: где зрелость по уровням расходится → lec-12 digital twins.

### Плюсы
- **Industry-standard frame.** ISA-95 знаком инженерам, в industry — lingua franca.
- **Clear maturity gradient.** AI зрелее на верхних уровнях; внизу — failure modes острее.
- **Regulatory mapping natural.** FDA Part 11 (L3-L4), ATEX (L0-L1) — это разные regulatory landscapes; ISA-95 frame показывает это.
- **Foreshadow lec-12 strong.** Digital twins нужны для соединения уровней.

### Минусы
- **Менее familiar для bachelors.** ISA-95 — это «индустриальная грамота», не все 3-курсники знают.
- **Failure bucket менее органично распределён.** Большая часть failures concentrate в L1-L0 (physical process); risk concentration → одни artifacts ≥30% strict-in, другие <.
- **Discrete vs process разница теряется** — оба используют ISA-95, но failure modes очень разные.

### Риск
- Студент не имеет contextual scaffold ISA-95; нужен 5-минутный intro в §0; cuts speech budget.

---

## Вариант C: «Discrete vs process — две модели»

### Идея
Производство — две parallel ветви с разными физическими, organizational, regulatory landscapes. AI применяется по-разному.

| Discrete (auto, electronics, aerospace) | Process (chem, steel, pharma, cement) |
|---|---|
| Дискретные единицы | Continuous flow |
| Assembly + QC inspection | Soft sensors + flow control |
| CV + robotics | MPC/RL + soft sensors |
| Worker-driven Lean | Reaction kinetics + safety |
| Tesla, BMW, Foxconn, Boeing | BASF, ArcelorMittal, Pfizer, Holcim |
| Failure mode: over-automation | Failure mode: distribution drift |

### Keystone-slide
Двухколонная схема: discrete vs process. Visual: на одной стороне Tesla Gigafactory; на другой — refinery. Под каждой — список AI-tools + failure mode. Middle line: что общее (foundation models, agentic copilots, pilot purgatory).

### Раскладка 75-мин:
- §0 (5 мин) — Hook + keystone двух моделей.
- §1 (15 мин) — **Что общее для двух моделей** (хайпа, цифры рынка, foundation models, pilot purgatory). Кейсы: Siemens IFM, McKinsey state of AI 2025. Failure cases: GE Predix, IBM Watson, Foxconn Wisconsin — hype-collapse universal.
- §2 (20 мин) — **Discrete production deep-dive.** CV inspection, robotic assembly, agentic copilots. Кейсы: BMW GenAI4Q, Foxconn FoxBrain, Boeing 737. **Failures:** Tesla over-automation, Boeing door plug, CV distribution shift.
- §3 (20 мин) — **Process production deep-dive.** Soft sensors, MPC/RL, predictive maintenance, regulatory weight. Кейсы: BASF Geismar, Yokogawa-JSR 35 days, Holcim AI kiln, POSCO edge. **Failures:** F-35 ALIS, RL drift, FDA Part 11, ATEX.
- §4 (10 мин) — **Когда AI не нужен — critical judgement.** Альтернативные инструменты (DOE, SPC, MPC, RCM, physics simulation). Hybrid patterns (PINN, CIRL).
- §5 (5 мин) — Bridge: где две модели **сходятся** → lec-12 digital twins; foreshadow lec-13 supply chain.

### Плюсы
- **Natural fault-line.** Студенту сразу очевидно, что failure modes разные; not awkward to introduce.
- **≥30% failure strict-in достигается органично.** §4 + значительная часть §2/§3 — про failures.
- **Industry-real.** Inженеры реально делят свою работу на discrete или process; это не academic frame.
- **Regulatory contrast clear.** FDA Part 11 (pharma process) vs CV inspection (discrete) — структурно разные.
- **Failure cases балансированы** — half в discrete (Tesla, Boeing), half в process (F-35 ALIS, GE Predix). Distributed naturally.

### Минусы
- **Не cycle-структура.** Менее «system thinking» feeling.
- **«Что общее» в §1 risk dilute** — нужен tight focus, иначе вода.
- **Не явно показывает progression** (Sense → Decide → Act).

### Риск
- Если §1 слабый — student feels split lecture без unifying glue. **Mitigation:** §1 короче (10-12 мин), focused on shared rapeg + failures.

---

## Вариант D (мой) — «Critical Judgement Frame»

### Идея
Лекция — не про **что делает AI в производстве**, а про **как инженер решает где AI нужен**. Несущая ось — **decision framework для применения AI**.

5-step decision process:
1. **Identify problem class** — discrete vs process; what's the «invisible variable»?
2. **Map alternatives** — какой не-AI инструмент уже работает? (DOE, SPC, MPC, RCM, physics-sim, rules-based vision).
3. **Apply «AI fit» criteria** — feedback loop fast? ground truth available? false-positive cost? regulatory? worker buy-in?
4. **Pilot with explicit go-criteria** — escape pilot purgatory.
5. **Production with human-in-loop + audit trail** — regulatory + organizational.

### Keystone-slide
5-step decision tree / flowchart. Each step — checklist с примерами.

### Раскладка 75-мин:
- §0 (5 мин) — Hook (одна цифра pilot-purgatory) + keystone framework.
- §1 (10 мин) — Step 1: discrete vs process (зацепить разницу + ключевые tools каждой ветки).
- §2 (15 мин) — Step 2: альтернативные инструменты (DOE, SPC, MPC, RCM, physics-sim). Когда они лучше AI.
- §3 (15 мин) — Step 3: AI-fit criteria. Деталь по 10 пунктам где AI не работает.
- §4 (15 мин) — Step 4-5: pilot, production. Successful cases (BASF Geismar, BMW GenAI4Q, Yokogawa-JSR). Failure cases (GE Predix, IBM Watson, Foxconn Wisconsin, Tesla over-automation).
- §5 (15 мин) — Application exercise / Q&A: студенты применяют framework к hypothetical scenarios. Bridge lec-12.

### Плюсы
- **Maximally aligned с failure-bucket philosophy** (≥30% — easy by design; почти все sections содержат «не нужен» logic).
- **Pedagogically strongest** — student leaves with applicable framework.
- **Course philosophy («когда AI и когда нет») явно incarnated**, не imposed.

### Минусы
- **Меньше narrative, больше framework.** Может feel «academic» / «листовка».
- **Industry-кейсы как examples, не как backbone** — может lose impact.
- **Сложнее найти strong hook** для §0 — abstract framework reluctance к pop-visuals.

### Риск
- Студент может уйти с «list» вместо «understanding». **Mitigation:** rich cases на каждом step; framework — выводится из cases, не наоборот.

---

## Рекомендация

**Брать Вариант C — «Discrete vs process».**

**Почему:**
1. **Failure-bucket ≥30% strict-in достижим органично без single-artifact concentration.** Half failures discrete (Tesla, Boeing, Foxconn Wisconsin), half process (F-35 ALIS, GE Predix), shared hype-collapses.
2. **Industry-real frame.** Инженеры реально делят свою работу так; не academic.
3. **Не дублирует lec-09 OODA** структурно (там — sensor-loop; здесь — production-type taxonomy).
4. **Bridges natural.** lec-09 (defense/aerospace mission systems) ↔ lec-11 (manufacturing discrete/process) ↔ lec-12 (digital twins + automation — где две модели сходятся) ↔ lec-13 (logistics).
5. **Regulatory landscape natural** — FDA Part 11 (pharma process), ATEX (chemical process), CV inspection (discrete) — структурно разные buckets.
6. **Слайд keystone visual-strong** — two columns с явно visualisable tools (Tesla robot vs refinery), middle middle — shared challenges. Студент видит main message за 5 секунд.

**Hybrid recommendation:** Вариант C + усиление в §4 «когда не AI» через Вариант D framework. То есть структура C-based, но §4 (15 мин) — это явно decision framework + alternatives, где Variant D logic incarnated. Это даёт **strongest failure-bucket + applicable judgement framework + industry-real backbone**.

**Финальная structure proposal для Plan v1:**
- §0 (5 мин) — Hook (pilot purgatory + Musk humans underrated quote) + keystone «discrete vs process».
- §1 (10 мин) — Что общее обеих моделей: foundation models (Siemens IFM), state of adoption (McKinsey 2025: 78%/5.5%), pilot purgatory как universal challenge. Hype-collapses (GE Predix, IBM Watson, Foxconn WI).
- §2 (20 мин) — Discrete deep-dive. CV inspection (BMW, TSMC), assembly robotics (Foxconn, Hyundai-BD), worker copilots (Toyota GAIA). Failures: Tesla 2018, Boeing 737.
- §3 (20 мин) — Process deep-dive. Soft sensors (BASF Geismar), MPC/RL (Yokogawa-JSR), predictive maintenance (Holcim, POSCO), regulatory (FDA Part 11, ATEX). Failures: F-35 ALIS, RL distribution drift.
- §4 (15 мин) — **Decision framework**: «Когда AI не нужен — 10 критериев + альтернативные инструменты». DOE, SPC, MPC, RCM, physics-sim, rules-vision. Hybrid patterns (PINN, CIRL).
- §5 (5 мин) — Bridge lec-12 (digital twins + automation) + closing keystone.

**Failure-bucket budget:**
- §1: ~5 мин hype-collapses (заявляем pilot purgatory honestly).
- §2: ~7 мин Tesla 2018 + Boeing 737 + CV limits.
- §3: ~7 мин F-35 ALIS + RL drift + regulatory.
- §4: ~13 мин — целиком failure / judgement.
- **Total strict-in failure/judgement contents: ~32 min / 75 = 42.6%** — comfortably > 30%, distributed evenly через все sections.

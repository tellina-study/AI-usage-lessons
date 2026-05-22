---
id: s39
type: assertion_visual
duration_min: 2.5
assertion: "Шесть альтернатив AI в логистике: OR (Gurobi/CPLEX/OR-Tools), классические запасы (EOQ/safety stock/ABC), сценарное планирование, rule-based, гибридные сенсоры, человек в петле."
learning_goal: "Alternative toolkit матрица — карман инструментов инженера-логиста"
learning_outcomes: [LO7]
chapter_ref: "§4.6 — Альтернативный инструментарий: что должен знать инженер логистики"
failure_bucket: strict_in
references: []
visual:
  pattern: alternatives_matrix_6_rows
  primary: "Таблица 6 строк × 4 колонки: инструмент / для какой задачи / vendor / пример"
---

# Альтернативный toolkit инженера-логиста

## Матрица

| Инструмент | Для какой задачи | Вендор / open source | Пример применения |
|---|---|---|---|
| **OR (Operations Research)** | Маршрутизация (TSP, VRP), scheduling, network design | Gurobi, CPLEX, Google OR-Tools | UPS ORION — $300-400M/год savings |
| **Классические запасы** | Inventory management при stationary demand | (формулы 1913+) | EOQ, safety stock, ABC analysis для большинства SKU |
| **Сценарное планирование** | Black-swan resilience | Shell-style, McKinsey scenario services | Maersk post-COVID redundancy planning |
| **Rule-based vision** | Controlled-env QC | OpenCV (open source), HALCON, Cognex | Bottle inspection на пивоварне (см. lec-11) |
| **Hybrid CV + signal processing** | Multi-sensor inspection | Cognex VisionPro + ultrasonic / radar | Container damage inspection в портах |
| **Human-in-the-loop (HITL)** | Exception handling, accountability | (workflow tools — Jira, ServiceNow) | Maersk exception teams для Red Sea rerouting |

## Когда применять что

- **OR:** когда задача — well-defined optimization (см. UPS ORION).
- **EOQ + safety stock:** когда demand stationary; audit показал, что <20% SKU требует ML.
- **Scenario planning:** для resilience к black-swans. Pre-build сценарии «что если Red Sea closed?» / «что если Suez blocked?»
- **Rule-based vision:** controlled-env с known defects (см. Boeing 737 door plug в lec-11 — где CV была last line, не first).
- **Hybrid sensors:** когда vision-only недостаточно (zerkalo, transparent packaging, deformation).
- **HITL:** при regulatory audit (FDA, FAA, IMO) и в black-swan events.

## Открытые источники

- **Google OR-Tools** — open source, бесплатный для VRP/TSP/scheduling.
- **OpenCV** — open source CV.
- **Pyomo** — Python framework для OR modeling.

## Pedagogical point

Инженер-логист, который знает только AI/ML — это incomplete engineer. Полный toolkit включает OR, classical formulas, scenario planning, rule-based vision, hybrid sensors, HITL. AI — это **один tool из шести**, не «универсальное решение».

## Speaker notes

Замыкая раздел четыре — alternative toolkit. Шесть классов инструментов, которые инженер-логист должен знать как альтернативы AI.

Первое — operations research. OR. Маршрутизация, scheduling, network design. Vendors — Gurobi и CPLEX commercial, Google OR-Tools open source. Pyomo — Python framework. UPS ORION — canonical proof success.

Второе — классические запасы. EOQ, safety stock, ABC analysis. Формулы 1913 года и далее, остаются relevant в 2026 году для большой доли SKU. Audit вашего inventory — какой процент SKU действительно требует ML? Часто менее двадцати процентов.

Третье — сценарное планирование. Это не software — это methodology. Shell использует scenario planning с 1970-х годов. McKinsey предлагает scenario planning services. Maersk post-COVID начал serious scenario planning для resilience.

Pre-build сценарии. «Что если Red Sea closed?» «Что если Suez blocked?» «Что если labor strike в Long Beach?» Когда event happens — у вас уже есть playbook.

Четвёртое — rule-based vision. OpenCV open source. HALCON и Cognex commercial. Используется в controlled-env с known defects. Bottle inspection на пивоварне — canonical example из лекции 11. Где CV была last line, не first line — это lesson Boeing 737 door plug.

Пятое — hybrid CV plus signal processing. Когда vision-only недостаточно. Container damage inspection в портах — vision plus ultrasonic plus radar. Multi-modal sensor fusion.

Шестое — human-in-the-loop. HITL. Workflow tools — Jira, ServiceNow. Используется при regulatory audit (FDA, FAA, IMO). И в black-swan events. Maersk exception teams handled Red Sea rerouting — это HITL в action.

Открытые источники. Google OR-Tools — open source, бесплатный для VRP и TSP. OpenCV — open source computer vision. Pyomo — Python framework для OR modeling. Все три — production-grade.

Pedagogical point. Инженер-логист, который знает только AI и ML — это incomplete engineer. Полный toolkit включает OR, classical formulas, scenario planning, rule-based vision, hybrid sensors, HITL. AI — это один tool из шести, не «универсальное решение».

Lesson для вас — будущих инженеров. Когда вы выходите на работу в логистическую компанию, ваша first ставка должна быть classical tools — OR plus EOQ plus rule-based. Если они не работают для конкретной задачи — тогда добавляете ML. Не наоборот. AI-first подход — это часто the wrong choice, и vendor proposals часто пытаются продать AI там, где OR-Tools достаточно.

Это вторая main payoff лекции. Carry это с собой.

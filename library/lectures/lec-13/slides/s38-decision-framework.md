---
id: s38
type: assertion_visual
duration_min: 3
assertion: "Пять критериев AI или не AI в логистике: среда / задача / спрос / безопасность / распределение."
learning_goal: "Decision framework 5 критериев — payoff лекции"
learning_outcomes: [LO7]
chapter_ref: "§4.2 — Decision framework"
failure_bucket: strict_in
references: []
visual:
  pattern: 5_criteria_decision_tree
  primary: "Decision tree 5 critical questions с примерами для каждого"
---

# Decision framework: 5 критериев AI/не AI в логистике

## Пять критериев

**1. Среда контролируемая?**
- Yes → AI applicable (warehouse, port, rail).
- No → continue.

**2. Задача — well-defined optimization (TSP, VRP, scheduling)?**
- Yes → **OR (Gurobi, CPLEX, OR-Tools) лучше RL/ML**.
- UPS ORION = canonical proof ($300-400M/год через OR + heuristics).

**3. Demand pattern stationary?**
- Yes → **EOQ + safety stock + ABC classical formulas лучше ML**.
- Audit: какой % SKU реально требует ML? Часто <20%.

**4. Safety-critical с regulatory audit?**
- Yes → **rule-based + human-in-loop required**.
- Black-box ML не работает (FDA, FAA, IMO).

**5. Event в-distribution?**
- Yes → ML scoring.
- No → **human dispatcher + scenario planning**.

## Применение

- Складская роботизация (Symbotic Walmart) — Criterion 1 yes, Criterion 4 partial → AI applicable + safety + HITL.
- UPS ORION маршрутизация — Criterion 2 yes (VRP) → OR, не ML.
- Houthi-style crisis demand forecast — Criterion 5 no → human dispatcher.
- FDA-regulated cold-chain pharma logistics — Criterion 4 yes → rule-based + HITL.
- Симфическая seasonal inventory ритейлера — Criterion 3 partial (mix stationary + spike) → hybrid EOQ + targeted ML на seasonal SKU.

## Pedagogical point

**Это не «всегда AI» или «никогда AI».** Это decision framework, который разбивает logistics workload на категории, и для каждой определяет proper tool.

## Speaker notes

Это центральный payoff раздела четыре и всей лекции. Пять критериев, которые позволяют инженеру решить, AI или не AI для конкретной логистической задачи.

Первый критерий — среда контролируемая или нет. Если warehouse, port, rail — yes, AI applicable. Это уровень один лестницы среды, и AI зрело работает. Symbotic, Amazon Robotics, KONUX — canonical examples.

Если nope — городские, magistral, exception — continue к следующему критерию.

Второй критерий — well-defined optimization задача. Travelling Salesman Problem, Vehicle Routing Problem, scheduling. Если yes — это OR territory. Gurobi, CPLEX, Google OR-Tools работают лучше, дешевле, объяснимее, чем RL или ML. UPS ORION — canonical proof, триста-четыреста миллионов savings в год через OR плюс heuristics, не deep learning.

Третий критерий — demand pattern stationary или non-stationary. Если spending pattern predictable по сезонам — это EOQ territory. Economic Order Quantity, safety stock, ABC analysis. Формулы 1913 года, simple, работают. Lesson — сделать audit вашего inventory: какой процент SKU реально требует ML? Часто less than двадцати процентов. Остальные — classical formulas достаточно.

Четвёртый критерий — safety-critical с regulatory audit. FDA для pharma cold-chain. FAA для aviation. IMO для shipping safety. ICAO для air traffic. Если yes — это rule-based plus human-in-loop territory. Black-box ML не работает в regulated industries, потому что audit trail обязателен.

Пятый критерий — event в-distribution или out. Если daily operations в normal demand distribution — это ML scoring territory. ML может оптимизировать на margins. Если black-swan event (хуситы, Suez, COVID) — это уровень пять лестницы. Human dispatcher plus scenario planning, не ML.

Application примеры. Складская роботизация — Criterion 1 yes, Criterion 4 partial (warehouse safety но lighter than pharma). AI applicable plus safety plus HITL.

UPS ORION маршрутизация — Criterion 2 yes, VRP с tens of thousands routes. OR, не ML.

Houthi-style crisis demand forecast — Criterion 5 no, completely out-of-distribution. Human dispatcher.

FDA-regulated cold-chain pharma logistics — Criterion 4 yes. Rule-based plus HITL.

Симфическая seasonal inventory ритейлера — Criterion 3 partial. Mix stationary plus spike. Hybrid EOQ plus targeted ML на seasonal SKU. Это не «полностью AI» или «полностью formula» — это hybrid с правильным choice tool на каждой категории SKU.

Pedagogical point. Это не «всегда AI» или «никогда AI». Это decision framework, который разбивает logistics workload на категории, и для каждой определяет proper tool. Lesson для инженера — когда вы оцениваете vendor proposal, проходите по этим пяти критериям. Какой критерий применим? Какой инструмент правильный для этой category?

Это framework, который останется с вами после лекции. Это main payoff лекции тринадцать.

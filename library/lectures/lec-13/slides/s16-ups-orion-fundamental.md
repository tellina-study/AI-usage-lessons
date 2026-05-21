---
id: s16
type: assertion_visual
duration_min: 3
assertion: "UPS ORION: 100 миллионов миль/год, $300-400 миллионов savings/год. Это операционные исследования (OR), не глубокое обучение и не RL."
learning_goal: "Canonical OR success как fundamental — anti-hype payoff"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.4 — UPS ORION: canonical OR success"
failure_bucket: strict_in
references: [informs-ups-orion, supply-chain-dive-ups]
visual:
  pattern: fundamental_concept_with_chart
  primary: "Hero photo: UPS truck + driver tablet. Справа — chart $300-400M savings/year + ключевая цитата"
  acquisition_tiers:
    - "Tier 3: UPS press kit"
    - "Tier 4: UPS YouTube"
    - "Tier 6: INFORMS / Supply Chain Dive press"
---

# UPS ORION: операционные исследования работают

## Цифры

- **~100 миллионов миль/год** — экономия пробега для всего парка UPS.
- **~10 миллионов галлонов топлива/год** — экономия.
- **~$300-400 миллионов savings/год**.
- **$320 миллионов cumulative savings к декабрю 2015** (INFORMS).
- **Original ORION** — снижение 8 миль/driver. **Dynamic ORION upgrade** — ещё 2-4 миль/driver.
- **Парк UPS** — ~125 000 машин.

## Что под капотом

- **Operations Research.** Целочисленное программирование + эвристики + Vehicle Routing Problem (VRP).
- **НЕ глубокое обучение.** НЕ reinforcement learning. НЕ GenAI.
- **Используемые инструменты:** Gurobi, CPLEX, Google OR-Tools.
- **Алгоритмы датируются 1950-60-ми** (теория графов, branch-and-bound, метаэвристики).
- **Деплоится Big Data + cloud-инфраструктура** — но решение задачи маршрутизации — классическое OR.

## Pedagogical point

UPS ORION — это **canonical anti-hype example**. Простой случай, когда well-defined optimization задача (TSP / VRP) решается через классическую математику лучше, чем через ML / RL.

**Когда задавать поставщику ML-маршрутизации вопросы:**

- Какие сравнения с OR-baseline? (Если нет — red flag.)
- Каков ваш VRP-solver? (Если «end-to-end deep learning» — спросите про объяснимость, edge cases, optimality gap.)
- Какие данные используете? Stationary demand или non-stationary? (При stationary — EOQ + safety stock + ABC лучше ML.)

## Speaker notes

UPS ORION — это canonical example операционных исследований, которые работают лучше глубокого обучения для well-defined задач маршрутизации. Я хочу остановиться на этом слайде на три минуты, потому что это один из главных fundamental слайдов лекции.

Цифры. UPS экономит примерно сто миллионов миль пробега в год для всего парка. Десять миллионов галлонов топлива. Триста-четыреста миллионов долларов в год экономии. Если посчитать кумулятивно — на декабрь 2015 года было триста двадцать миллионов долларов экономии по данным INFORMS. Парк UPS — около ста двадцати пяти тысяч машин.

Что важно. Под капотом ORION — это операционные исследования. Целочисленное программирование плюс эвристики плюс задача маршрутизации транспортных средств — VRP. Не глубокое обучение. Не reinforcement learning. Не GenAI. Используемые инструменты — это Gurobi, CPLEX, Google OR-Tools. Алгоритмы датируются 1950-60-ми годами — теория графов, branch-and-bound, метаэвристики.

Современная инфраструктура — Big Data, cloud, real-time data feeds — это всё есть. Но само решение задачи маршрутизации — это классическая математика, не ML.

Pedagogical point. UPS ORION — это canonical anti-hype example. Простой случай, когда well-defined optimization задача решается через классическую математику лучше, чем через ML или RL.

Когда вы — инженер — слышите от поставщика «наш ML-стек оптимизирует маршруты вашего флота с эффектом плюс двадцать пять процентов» — у вас должны автоматически возникать три вопроса.

Первый. Какие сравнения с OR-baseline? Если поставщик не показывает baseline Gurobi или OR-Tools — это red flag. Это означает, что либо они не делали такое сравнение, либо ML-решение не лучше классического OR, а сравнение просто скрыто.

Второй. Какой ваш VRP-solver? Если ответ «end-to-end deep learning» — спросите про объяснимость, про edge cases, про optimality gap. End-to-end RL для VRP — это active area research, но это не production-grade на 2026 год.

Третий. Какие данные используете? Stationary demand или non-stationary? При stationary — то есть когда спрос предсказуем по сезонам — EOQ плюс safety stock плюс ABC-анализ работают не хуже ML. Это формулы 1913 года, и они для большой доли SKU дают результаты, сопоставимые с ML.

Замечу для контекста: UPS ORION не единственный пример. FedEx использует Carrier-сторону аналогичных OR-методов. Maersk Line, ZIM, CMA CGM используют specialized OR-solver для container-ship routing — это другая задача (LCL/FCL + ETA + capacity), но математика та же. Walmart routing внутри distribution network — OR.

ML-маршрутизация имеет место в одном специфическом случае: когда данных много, спрос non-stationary, и есть real-time external signals (погода, traffic, события). Тогда ML-overlay поверх OR-solver может улучшить performance. Но pure ML без OR-baseline — почти всегда хуже.

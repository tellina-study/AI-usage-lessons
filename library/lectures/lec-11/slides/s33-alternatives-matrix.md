---
id: s33
type: assertion_visual
duration_min: 2.5
assertion: "Шесть альтернативных инструментов: SPC / DOE / MPC / RCM / physics-sim / rules-vision — каждый со своей нишей."
learning_goal: "Alternatives matrix (6 × 5)"
learning_outcomes: [LO8]
chapter_ref: "§4.2 матрица альтернатив"
failure_bucket: strict_in
references: []
visual:
  pattern: matrix_6x5
  primary: "Matrix 6 строк × 5 столбцов"
---

# Матрица альтернатив — что использовать ДО ML

## Шесть инструментов × пять столбцов

| Инструмент | Когда применим | Сильные стороны | Слабые стороны | Regulatory friendly |
|---|---|---|---|---|
| **SPC** (Statistical Process Control) | Univariate; стабильные параметры | Дёшево, объяснимо, 100 лет в промышленности | Не ловит multi-variate patterns | ✓ FDA / GAMP / ISO |
| **DOE** (Design of Experiments) | Эксплорация; малые партии | Causal inference; defensible | Не online; нужен domain expert | ✓ полностью |
| **MPC** (Model Predictive Control) | Process control; online | Explicit model; reacts к drift; dominates | Требует точную модель | ✓ известный объект для регулятора |
| **RCM** (Reliability-Centered Maintenance) | MTBF > 1 года; PdM impossible | Объяснимый; calibrated к физике | Не learning из новых отказов | ✓ полностью |
| **Physics-based sim** (CFD / FEA / kinetics) | Известная физика | Обобщается на новые конфигурации | Дорогая разработка модели | ✓ полностью |
| **Rules-based vision** | Controlled environments; простые правила | Validated за неделю; объяснимо | Не справляется с variability | ✓ полностью |

## Hybrid patterns (в одной строке)

**PINN** (Physics-Informed NN) — physics constraints в ML loss.

**CIRL** — PID внутри loss function deep RL (BASF).

**ML over SPC** — статистический baseline + ML на остатке.

**PLC + edge ML coprocessor** — POSCO pattern, edge inference рядом с детерминированным PLC.

## Speaker notes

Шесть альтернативных инструментов, которые вы должны рассматривать ДО того, как тянуться к ML. Каждый со своей нишей, каждый regulatory friendly.

SPC — Statistical Process Control. Применим где univariate параметры стабильны: например, температура в реакторе должна быть в диапазоне ±2 градуса. SPC рисует control chart, и оператор видит, когда параметр выходит за three-sigma пределы. Дёшево, объяснимо, регулятор воспринимает это как known object. Слабая сторона — не ловит multi-variate patterns. Если 10 параметров вместе создают anomaly, но каждый по отдельности в норме — SPC не увидит.

DOE — Design of Experiments. Это not control inструмент, это эксплоративный. Применим для маленьких партий, для R&D, для understanding какие переменные влияют на качество. Сильная сторона — causal inference, объяснимо, defensible перед регулятором. Слабая — не online, и нужен domain expert для дизайна эксперимента.

MPC — Model Predictive Control. Это хлеб с маслом process control. Применим для online управления процессом — реакторы, distillation columns, печи. Explicit model — оператор и регулятор знают, по какой модели контроллер реагирует. Reacts к drift автоматически, потому что каждый шаг переcчитывает оптимум. Dominates process control в 2026 году. Слабая сторона — требует точную модель, и моделирование сложного процесса само по себе работа.

RCM — Reliability-Centered Maintenance. Когда MTBF больше года и PdM на ML невозможен — RCM. Это расчёт оптимального интервала ТО на основе физики узла и истории отказов. Объяснимый, calibrated к физике. Слабая — не учится на новых отказах автоматически, нужен инженер для пересмотра графика.

Physics-based simulation. CFD для гидродинамики, FEA для механики, kinetics для химии. Когда физика известна — это надёжнее ML. Сильная сторона — обобщается на новые конфигурации, потому что физика та же. Слабая — разработка модели дорогая и требует domain expertise.

Rules-based vision. Простые правила: площадь, контур, цвет, geometric primitives. В controlled environments — освещение постоянное, ракурс зафиксирован — ловит 60-70 процентов inspection workloads. Validated за неделю, объяснимо. Слабая — не справляется с variability, любое отклонение от идеала ломает rule.

И теперь hybrid patterns, в одной строке. PINN — Physics-Informed Neural Networks — добавляет physics constraints в loss function ML. Снижает требования к данным, увеличивает generalization. CIRL — мы разобрали — PID внутри loss function deep RL, BASF паттерн. ML over SPC — статистический baseline ловит первые 70 процентов, ML добавляется на оставшихся 30 процентов сложности. PLC + edge ML coprocessor — POSCO pattern, который мы видели на s27, где edge inference работает рядом с детерминированным PLC, но не пытается его заменить.

Идея матрицы — у вас есть выбор. AI — не единственный инструмент. И часто не лучший.

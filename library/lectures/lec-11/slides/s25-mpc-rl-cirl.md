---
id: s25
type: assertion_visual
duration_min: 3
assertion: "Yokogawa-JSR FKDPP: 35 дней автономного RL в distillation column (2022). CIRL: RL расширяет PID, не замещает."
learning_goal: "MPC/RL гибрид; CIRL — PID внутри loss function (mermaid diagram)"
learning_outcomes: [LO1a, LO7]
chapter_ref: "§3.2 MPC/RL/CIRL"
references: [yokogawa-jsr-fkdpp-2022, basf-cirl-2024, japan-pm-prize-2023]
visual:
  pattern: cirl_architecture_diagram
  primary: "Mermaid diagram CIRL — PID baseline inside RL loss function"
---

# MPC / RL гибрид + CIRL

## Yokogawa-JSR FKDPP (Японский кейс, 2022)

**17 января — 21 февраля 2022.** 35 дней (840 часов) автономного RL-контроля distillation column в JSR plant.

Первый production-прецедент: RL разрешает компромисс **output quality / energy / throughput** в нелинейной системе — то, что традиционный PID и Advanced Process Control (APC) не могли.

**Japan Industrial Technology Prime Minister's Prize 2023.**

## CIRL — Combined Inverse RL (BASF + Royal Academy of Engineering, 2024–2026)

**PID внутри loss function deep RL.** Это не «RL вместо PID» и не «два контура параллельно». Это **RL расширяет PID, не замещает**.

Архитектура:
- PID контролер работает как baseline (детерминированный, валидируется регулятором).
- Deep RL учит policy, где PID — это baseline в loss function.
- RL adds value в нелинейных зонах, где PID плохо тюнится.

## RL distribution drift — когда ломается

Batch transitions (OOD входы).

Смена feedstock (stale policy на новой партии сырья).

Seasonal shifts (зимняя температура vs летняя).

Equipment wear (старение catalyst).

## Альтернатива: MPC

Explicit model, объясним, validated. **MPC dominates** process control. RL дополняет на high-level scheduling, не на низкоуровневом замыкании.

## Speaker notes

Это самый технически сложный слайд в лекции, и я расскажу медленно.

В январе-феврале 2022 года Yokogawa в партнёрстве с JSR Corporation провели первый production-прецедент полностью автономного контроля distillation column с использованием Reinforcement Learning. 35 дней без вмешательства человека, 840 часов. Алгоритм называется FKDPP — Factorial Kernel Dynamic Policy Programming. Это получило Japan Industrial Technology Prime Minister's Prize 2023.

Что важно. До FKDPP distillation column управлялся через PID — Proportional-Integral-Derivative контроллер — и Advanced Process Control (APC), которая надстраивает оптимизацию над PID. Эти инструменты отлично работают в линейных зонах. Но distillation в нелинейных зонах — например, при переходных режимах — компромисс между output quality, energy consumption и throughput становится сложным многомерным trade-off. Traditional control не справлялся. RL смог найти политику, которая разрешает этот компромисс лучше.

Теперь про CIRL — Combined Inverse RL. Это разработка BASF в партнёрстве с Royal Academy of Engineering, 2024-2026. Идея концептуально красива, и я хочу, чтобы вы запомнили формулу. CIRL — это PID внутри loss function deep RL. Это не «RL вместо PID». Это не «два контура параллельно». Это RL расширяет PID, не замещает.

Архитектура. PID контроллер работает как baseline — детерминированный, валидируется регулятором, понятен инженеру. Deep RL учит policy, и в её loss function — функции, которую алгоритм минимизирует — заложен PID-результат как baseline. RL может улучшить PID, но не имеет права радикально отклониться от него. RL добавляет ценность в нелинейных зонах, где PID плохо тюнится. В линейных зонах RL автоматически совпадает с PID, потому что loss function его туда тянет.

Эта архитектура — компромисс между регуляторной валидируемостью и эффективностью. Регулятор видит PID как известный объект — валидирует. RL — это «надстройка», которая улучшает performance, но не выходит за safety envelope PID. Это inженерное решение проблемы, которая иначе не решается.

И теперь про когда RL ломается. RL distribution drift — это структурная проблема RL в производстве. Алгоритм обучен на одном distribution данных, но в реальности данные меняются: batch transitions создают out-of-distribution входы; смена feedstock делает старую политику stale; seasonal shifts влияют на температуру окружающей среды; equipment wear — катализатор стареет, реактор теряет производительность. Любое из этих изменений ломает RL-политику без warning. PID — устойчив к этому, потому что он реагирует на текущие данные, не помнит обучения.

Альтернатива в большинстве кейсов — MPC, Model Predictive Control. Explicit model, объяснимый, валидированный. MPC dominates process control в 2026 году. RL — это дополнение на high-level scheduling, не замена низкоуровневого замыкания контура.

Это очень важный архитектурный выбор: где RL уместен, где нет. CIRL — наш современный ответ. PID — наш базовый ответ.

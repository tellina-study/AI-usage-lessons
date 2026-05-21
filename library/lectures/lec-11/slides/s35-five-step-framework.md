---
id: s35
type: assertion_visual
duration_min: 2
assertion: "Пять шагов: identify class → map alternatives → apply 4 категории → pilot с go-criteria → production с HITL + audit trail."
learning_goal: "5-step framework для кармана + 3 вопроса к вендору + OEE-вопрос"
learning_outcomes: [LO8]
chapter_ref: "§4.4 5-step framework closure"
failure_bucket: strict_in
references: []
visual:
  pattern: five_step_flow
  primary: "Пять шагов в горизонтальном flow + 4 вопроса к вендору"
---

# 5-step framework — ваш инструмент для кармана

## Пять шагов

**1 → Identify class.** Дискретное или процессное? Какая физика, какая регуляторика, какая культура?

**2 → Map alternatives.** SPC / DOE / MPC / RCM / physics-sim / rules-vision — что применимо до ML?

**3 → Apply 4 categories.** Данные ✓? Стоимость ✓? Регуляторика ✓? Человек ✓?

**4 → Pilot с explicit go-criteria.** Baseline + measure window + go/no-go threshold ДО старта.

**5 → Production с HITL + audit trail.** Recommend mode для safety-critical. Validated. Traceable.

## Четыре вопроса к вендору (для кармана)

**1.** Baseline до AI — на какой объём работы вы сравниваете?

**2.** Окно измерения — за какой период оценка?

**3.** Перечень вмешательств — какие задачи реально автоматизированы?

**4.** OEE-канал — в какой компонент OEE добавляется эффект (availability / performance / quality)?

## Гибридные паттерны (closure)

PINN (physics-informed NN) + CIRL (PID-в-RL) + ML over SPC + PLC + edge ML coprocessor — четыре examples hybrids.

## Speaker notes

Это финальный практический слайд лекции. Запомните этот framework — он работает на любом AI-проекте, который вы увидите в карьере.

Пять шагов.

Первый — identify class. Дискретное или процессное? Это первое разделение, и из него следует вся дальнейшая логика. Какая физика — штучные единицы или непрерывный поток? Какая регуляторика — ISO 9001 или FDA Part 11 или ATEX? Какая культура — Toyota Jidoka или Tesla replace?

Второй — map alternatives. Прежде чем тянуться к ML, перечислите неMLные инструменты. SPC, DOE, MPC, RCM, physics-based simulation, rules-based vision. Какие из них применимы к вашей задаче? Какие частично решают её?

Третий — apply 4 categories. Пройдите критерии: данные, стоимость, регуляторика, человек. Если все четыре галочки — AI применим. Если хотя бы одна категория проблематична — либо адаптируйте архитектуру, либо рассматривайте альтернативы из step 2.

Четвёртый — pilot с explicit go-criteria. До запуска pilot определите: baseline до AI, измерительное окно, go/no-go threshold. Если pilot стартует без этих трёх — он попадает в 80-95 процентов pilot purgatory. Это правило, которое исключает большинство неудач.

Пятый — production с HITL и audit trail. Если cвичите pilot и переходите в production: recommend mode для safety-critical контуров. Validated. Traceable. Audit trail для регулятора и для собственного контроля. Если вы не можете объяснить, почему модель приняла решение — это знак, что архитектуру нужно пересмотреть.

И параллельно — четыре вопроса к вендору. Я уже их повторял несколько раз сегодня, и сейчас повторю ещё раз, потому что они работают как формула в кармане.

Baseline до AI — что было раньше? Окно измерения — за какой период? Перечень вмешательств — что реально автоматизировано? OEE-канал — какой компонент эффективности улучшается?

Эти четыре вопроса в комбинации с 5-step framework — это всё, что вам нужно для критической оценки AI-проектов в производстве. Если ваш AI-projector сегодня знает только то, что мы разобрали — он будет в верхней группе инженеров по уровню профессионализма.

И последняя нота — hybrid patterns. PINN, CIRL, ML over SPC, PLC plus edge ML coprocessor. Это четыре примера того, как ML интегрируется с проверенными неMLными методами, а не пытается их заменить. Это правильный путь интеграции AI в production. Не «AI вместо PID», а «AI расширяет PID, не замещает».

---
id: s32
type: assertion_visual
duration_min: 4
assertion: "Четыре категории критериев «AI не подходит»: Данные / Стоимость / Регуляторика / Человек."
learning_goal: "LO8 центральный — payoff лекции"
learning_outcomes: [LO8]
chapter_ref: "§4.1 4 категории"
failure_bucket: strict_in
references: []
visual:
  pattern: four_categories_grid
  primary: "4 категории в 2×2 grid с примерами + альтернативами"
---

# Четыре категории критериев «AI не подходит»

## A. Данные (3 критерия)

1. **MTBF >1 года** — недостаточно failure events для PdM.
2. **Известная физика** (CFD / FEA / kinetics надёжнее ML).
3. **Эталонная разметка дорогая** (defect rate <1%, expensive labels).

**Альтернативы:** physics-based simulation, DOE, SPC.

## B. Стоимость (2 критерия)

4. **FP cost >10× FN** — SPC + RCM лучше (false alarm дороже missed defect).
5. **SIL 2/3 safety-critical** — ML certification сложнее.

**Альтернативы:** SPC, RCM, rules-based.

## C. Регуляторика (3 критерия)

6. **Audit-trail обязателен** (FDA Part 11, GAMP®5) — black-box не работает.
7. **ATEX Zone 0** — physical hardware restriction.
8. **Указ 250 / КИИ** — domestic software, ограничения cloud.

**Альтернативы:** explainable ML, hybrid с rules, on-premise.

## D. Человек (3 критерия)

9. **Operator distrust** — workaround неизбежен (Toyota proof, lec-7 HITL).
10. **Pilot без go-criteria** — 80–95% pilot purgatory.
11. **Demo-hype без 6-mo production track record** — buyer beware.

**Альтернативы:** Six Sigma, Jidoka, structured pilots.

## Три уточняющих вопроса к вендору (LO2 — для кармана)

1. **Baseline до AI** — на какой объём работы вы сравниваете?
2. **Окно измерения** — период оценки.
3. **Перечень вмешательств** — какие задачи реально автоматизированы?

**+4-й OEE-вопрос:** в какой компонент OEE добавляется эффект (availability / performance / quality)?

## Speaker notes

Это центральный слайд лекции. Запомните эти четыре категории, и каждый раз, когда будете оценивать AI-проект, проходите их в голове.

Категория A — данные. Три критерия. Первый: MTBF — Mean Time Between Failures — больше года. Если узел отказывает раз в год, у вас за пять лет 5 failure events. Для обучения PdM-модели этого недостаточно — не хватает данных, чтобы модель научилась распознавать pattern перед отказом. Здесь работает не AI, а RCM — Reliability-Centered Maintenance — расчёт оптимального интервала ТО на основе физики и MTBF. Второй: если физика процесса известна — CFD для гидродинамики, FEA для механики, kinetics для химии — это надёжнее ML, потому что обобщает на новые конфигурации. ML интерполирует на данных обучения. Третий: эталонная разметка дорогая — defect rate меньше 1 процента, разметка дорогая. Альтернативы для категории A: physics-based simulation, DOE для эксплоративных экспериментов, SPC для статистического контроля.

Категория B — стоимость. Два критерия. Четвёртый: false positive cost больше чем 10x false negative. Если ложная тревога дороже пропущенного дефекта — значит, мы скорее остановим линию по ошибочной AI-тревоге, чем пропустим дефект. Здесь работает SPC + RCM, которые предсказуемы и калибруются вручную. Пятый: SIL 2/3 safety-critical — это специальные уровни сертификации для контуров с риском для жизни. ML certification на SIL 2/3 — это очень дорого и долго, обычно нерентабельно. Альтернативы для B: SPC, RCM, rules-based.

Категория C — регуляторика. Три критерия. Шестой: audit trail обязателен — FDA Part 11, GAMP 5. Black-box ML здесь не проходит, нужен explainable ML, hybrid с rules или on-premise решение. Седьмой: ATEX Zone 0 — постоянное присутствие взрывоопасной смеси. Hardware restriction, non-certified AI запрещён физически. Восьмой: Указ 250 в России — domestic software на КИИ-объектах. SaaS-облака не подходят, нужно on-premise. Альтернативы для C: explainable ML, hybrid, on-premise.

Категория D — человек. Три критерия. Девятый: operator distrust. Если оператор не доверяет AI, он будет workaround — отключит, проигнорирует, найдёт способ обойти. Это структурный risk, особенно в смыслах, где операторы — союзная сторона, не противник. Toyota proof — augmentation, не replacement. Десятый: pilot без go-criteria. Если pilot не имеет explicit go/no-go critериев определённых до старта — он попадает в 80-95 процентов pilot purgatory. Одиннадцатый: demo-hype без 6-месячного production track record. Если вендор показывает только демо, не пускает в production-customer reference — buyer beware. Альтернативы для D: Six Sigma, Jidoka, structured pilots.

Это 11 критериев в 4 категориях. Запомните таксономию категорий — это первый шаг применения. Конкретные критерии вы будете adapt под свой контекст.

И параллельно — три вопроса к вендору. Запомните их как формулу. Baseline до AI, окно измерения, перечень вмешательств. Плюс четвёртый вопрос про OEE — какой компонент эффективности улучшается. Это инструмент для кармана, который работает на любом vendor pitch.

В следующем слайде — матрица альтернативных инструментов. Через слайд — worked example Pfizer Vox, где мы пройдём framework шаг за шагом.

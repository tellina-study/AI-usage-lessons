---
id: s34
type: assertion_visual
duration_min: 3
assertion: "Pfizer Vox проходит 5-step framework: процессное, SPC недостаточно, FDA Part 11 → recommend mode, HITL → готов к production."
learning_goal: "Worked example — рамка применима, не abstract theory"
learning_outcomes: [LO8]
chapter_ref: "§4.3 Pfizer Vox worked example"
failure_bucket: strict_in
references: [pfizer-vox-2024]
visual:
  pattern: five_step_walkthrough
  primary: "5 шагов framework + Pfizer Vox application"
---

# Pfizer Vox через 5-step framework

## Step 1 — Identify class

**Процессное (continuous bioprocessing).** mRNA-вакцины — не штучный продукт, это batch process с непрерывным мониторингом.

## Step 2 — Map alternatives

**SPC:** univariate — даёт baseline, но не ловит сложные multi-variate аномалии.

**DOE:** не подходит — too many variables, online.

**MPC:** есть для control, но не покрывает rare anomalies в batch quality.

## Step 3 — Apply 4 categories

**Данные** ✓ — вакцины: много batch data, эталонная разметка есть из QC.

**Стоимость** ✓ — FP cost manageable: operator review после AI-alert.

**Регуляторика** ✓/✗ — FDA Part 11 → **recommend mode**, не autonomous batch release. Архитектура: Vox рекомендует, оператор подписывает.

**Человек** ✓ — operators обучены, trust строится через recommend pattern.

## Step 4 — Pilot с go-criteria

Pfizer заявил **+20 000 doses per batch** — baseline до AI был известен.

Go-criterion: baseline doses per batch + ROI within 12 months.

## Step 5 — Production с HITL

**Vox recommends actions to operators** — explicit augmentation, не autonomous.

**Архитектура AI:** decision-support, не controller (LO7 mapping).

## Lesson

5-step framework работает ретроспективно — это **готовый инструмент**, не abstract theory.

## Speaker notes

Теперь пройдём 5-step framework на конкретном кейсе. Pfizer Vox.

Step 1 — identify class. Pfizer хотел детектировать аномалии в производстве mRNA-вакцин и рекомендовать действия оператору. Это процессное производство — continuous bioprocessing. Не штучный продукт, не сборочный конвейер. Batch process с непрерывным мониторингом параметров: температура, pH, концентрация. Класс определён сразу — процессное.

Step 2 — map alternatives. Какие неMLные инструменты применимы?

SPC — univariate. Даёт baseline для каждого параметра отдельно. Полезно как первый слой, но не ловит multi-variate аномалии, когда сочетание нескольких параметров вне нормы при том, что каждый по отдельности в норме. SPC недостаточен один.

DOE — design of experiments. Подходит для R&D на новых формуляциях, не для online мониторинга производства. Pfizer уже знает, какие переменные значимы. DOE не подходит для этого use case.

MPC — Model Predictive Control. У Pfizer уже есть MPC для control температуры и других параметров реактора. Но MPC не покрывает rare anomalies в batch quality — это другой класс задач. MPC контролирует процесс, не детектирует deviations в продукте.

Следовательно, ML здесь имеет место — для multi-variate anomaly detection поверх существующего SPC и MPC.

Step 3 — apply 4 категории.

Данные — галочка. Pfizer имеет годы batch data, эталонная разметка доступна из существующих QC-процессов: какие batches прошли release, какие провалили.

Стоимость — галочка. False positive cost manageable: если AI поднимет alert на нормальном batch, оператор делает review, дополнительные тесты. Это minute-level disruption, не batch-кill. False negative cost — это deviated batch, который проходит на склад. У Pfizer уже есть downstream QC, который ловит большинство этого, но AI-alert — дополнительный слой.

Регуляторика — половина галочки. FDA Part 11 запрещает autonomous batch release. Значит, архитектура AI должна быть recommend mode, не autonomous. Vox рекомендует, оператор оценивает и подписывает release. Это explicit decision-support architecture.

Человек — галочка. Operators в Pfizer обучены, и trust к AI строится через recommend pattern. Если оператор соглашается с рекомендацией Vox — он подписывает. Если не соглашается — он не подписывает. AI не противостоит оператору, AI помогает ему.

Step 4 — pilot с go-criteria. Pfizer запустил pilot с конкретным go-criterion: 20 тысяч дополнительных доз вакцины per batch. Baseline до AI был известен — статистика производства предыдущих лет. Pilot прошёл go-criterion и был переведён в production.

Step 5 — production с HITL. Vox recommends actions to operators. Audit trail полный: какая модель, какая версия, какой вход, какая рекомендация, кем подписано, когда. FDA Part 11 satisfied.

И lesson: 5-step framework работает ретроспективно. Pfizer Vox прошёл его шаг за шагом. Это значит, что framework — это готовый инструмент для оценки новых AI-проектов, а не abstract theory.

Завтра, когда вы пойдёте на встречу к вендору, который предлагает AI-решение — проходите через 5 шагов в голове. Если хотя бы один из шагов не проходит — это red flag.

---
# ЧЕТВЁРТЫЙ ПУНКТ В КАЖДОМ СТОЛБЦЕ ВЕРНУЛСЯ ПО ЛИЧНОМУ ПРОСМОТРУ PNG, а не по прогону:
# после того как из столбцов ушли пункты стадии ИССЛЕДОВАНИЯ, в обеих коробках осталось по три
# строки, и кадр вышел с полем пустоты в половину высоты. Сборка на это не жалуется — пустая
# коробка для неё так же законна, как полная. Оба добавленных пункта взяты из материала ЭТОЙ
# стадии (арбитраж на расхождениях — `s47`; неназначенная ступень участия — `s38`), а не
# придуманы под высоту.
# ВЫВОД ПРИВЕДЁН К СВОЕМУ РАЗДЕЛУ (переделка раздела 2 по канону PR #286, пп. 1 и 15 наряда).
# БЫЛО: заголовок «Вывод раздела: три места, где провалилось не чтение», а тело называло ПЯТЬ
# мест и закрывало две стадии сразу — «Раздел закрыл две стадии и один случай сверх них».
# Расхождение заголовка с телом — следствие слияния разделов: три провала (развёртывание, состав
# набора, цель) принадлежат стадии ИССЛЕДОВАНИЯ, и теперь их считает её собственный вывод `s33`;
# этой стадии принадлежат устройство процедуры и сдвиг распределения входов.
# СТАЛО: заголовок и тело считают одно и то же и только своё. Три отдельных дефекта разом:
# счёт «три против пяти», чужая стадия в своём выводе и фраза «Раздел закрыл» — наш
# производственный язык на видимом слое (§11.6).
# СТУПЕНЬ УЧАСТИЯ оставлена: это несущая мысль именно этой стадии, в разделе исследования
# человека рядом с моделью нет вовсе (§2.9 главы предъявляет этот прочерк прямо).
id: s50
local_id: s3-13
section: "3. Постановка диагноза"
type: comparison
title: "Section conclusion: one tool, opposite outcomes"
assertion: "Раздел закрывает две стадии и один случай сверх них: на исследовании провалились развёртывание, состав обучающего набора и определение цели, на постановке диагноза — устройство процедуры, а на непрерывном наблюдении сдвинулось распределение входов при оставленном пороге; модель даёт второй взгляд на поток целиком, постоянство и напоминание о редком диагнозе, а в одном устройстве процедуры и пару сильнее обеих сторон, но не умеет решить, годно ли измерение, назначить порог под цену ошибки, сохранить независимость двух мнений и удержать преимущество там, где человек сильнее; ступень участия человека нигде не записана"
source: "—"
media: ""
media_needed: "иллюстрации нет: противопоставление столбцами и строка форм держат слайд сами"
media_note: "полужирным набран прочерк — в нём сам вывод"
columns:
  left:  {head: "What works"
, items: ["a second look at the whole stream", "a reminder of a rare diagnosis", "the pair stronger than both sides — under one design of the procedure", "arbitration only on disagreements: the whole stream doesn't go to it"]}
  right: {head: "What doesn't work", items: ["preserving the independence of two opinions", "holding onto the advantage where the human is stronger", "noticing that the input distribution has shifted", "assigning a rung of involvement: no one writes it down"]}
pol_slov: 150   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 146 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
timing_min: 1.2
in_bucket: true
method_steps: ["вывод раздела"]
form: ["форма 4а", "форма 7", "форма 5", "форма 4", "форма 3"]
vfy: false
status: собран
---

## Visible slide text

**Six case studies at this stage produced opposite outcomes with the same tool.** The Swedish trial: one human reading on top of the model beats double reading. The surgeons: the same pair falls below both. What differs is the design of the procedure — whether the independence of the two opinions is preserved, and the order in which the suggestion is presented.

**What holds this up:** a threshold set against the cost of both errors, and arbitration on disagreements.

**The rung of involvement is written down nowhere. Left unassigned, it slides down to signing without looking.**

**Of the six input distortions, this section met four:** anchoring on an incorrect readout · narrowing · alert stream · disagreement as a standing step.

## Speaker notes

Six case studies at this stage, using the same tool, produced opposite outcomes, and what differs between them is the design of the procedure — whether the independence of two opinions is preserved, and the order in which the suggestion is presented.

What works. A second look at a stream no human could ever read in full: the model reads everything and doesn't lose sensitivity on a Friday evening. The reminder of a rare diagnosis works by the exact same mechanism through which a suggestion also does harm — it adds to the composition of the list, and a line a tired physician wouldn't have come up with gets added. And one design of the procedure where the pair is measurably stronger than both sides: sensitivity of eighty and a half against seventy-three and eight, at the same specificity.

What doesn't work. Independence is lost because of how the interface is built; the physician's attentiveness isn't the cause. Selectivity is a procedure the system lacks: no group got a tool that let them tell a correct suggestion from an incorrect one, and none of them managed the task. Explainability has a measured cost: a simplified explanation of an incorrect recommendation drops the choice below the line the same physician gives with no model at all.

What happened to the work. The load fell at the same spot — in the eye-tracking study, that was a cost; with the sign reversed, a gain; so the form itself carries no sign — the sign is set by whether the suggestion was right. The cost of error shifted: the model's miss became the reader's miss, and the human signs off on it. The performer changed: the model became the second reader, and the drop in human reading volume is a consequence of that change; it isn't an achievement on its own.

What holds this up. The order of presenting the suggestion is a controllable parameter with a measured cost: an interface that shows the marker alongside the image buys speed at a high price. Arbitration by a third reader, where the human and the model disagreed. And one thing written down nowhere: the human's rung of involvement. Left unassigned, under load, it slides down to signing without looking.

And the input mechanism this section ran into harder than any other: anchoring. The sixth case study, from Moscow, puts the model's suggestion at the TOP of the working screen before the physician has decided — setting the order of presentation to the riskiest position this stage allows. The same study measures how this turns out in the one spot where the suggestion makes any difference at all: in that fifth of cases where the physician and the model disagree, neither is right — the physician in sixty-four cases out of a hundred, the model in forty-five.

This link has to be said out loud: in the case study where the result fell, and in the control line where it rose, the exact same system from the same vendor was at work.

The figure behind the line on explainability is worth naming, because it runs against intuition. In a vignette study on antidepressant selection, an incorrect recommendation delivered with a simplified explanation dropped the share of correct choices from 35.7 to 26.2 out of a hundred — below what was achieved with no model at all. The explanation didn't help anyone tell a bad piece of advice from a good one; it helped the bad advice get through.

Two things hold this load up: the order of presenting the suggestion, which has a measured cost, and arbitration by a third reader — but only where the human and the model disagreed. We don't repeat the numbers behind the four vocabulary forms: each one already stood on its own case study, and repeating them here would turn the conclusion into a summary of the section. The same tool dragged the result down in one case study and raised it in the control line — what differed between them was the design of the procedure, and that's the conclusion of this stage.

How to say the four vocabulary forms that stand in a row. The load fell at the same spot — in the eye-tracking study — and the sign of this form is set by whether the suggestion was right: the same drop in scan coverage turned into a gain in the mirrored study. The cost of error shifted — the model's miss became the reader's miss, signed off by a human. The performer changed — the model became the second reader, and human reading volume fell as a consequence of that change, not as a goal in its own right. Same performer, now worse — the surgeon's own advantage on septic shock collapsed under the same workload; this form didn't exist in the vocabulary before this section, and it had to be added.

And about the bolded line. The human's rung of involvement is written down nowhere: not in the program's regulations, not in the product manual, not in the reader's job description. An unrecorded rung doesn't stay neutral — it slides downward, toward signing without looking, because that's the cheapest way to satisfy the requirement "a human makes the decision." The bill for this comes due in the section on licensing, oversight, and liability, and it's presented not to the interface, but to whoever failed to assign the rung.

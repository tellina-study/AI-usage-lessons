---
id: s20
local_id: s1-09
section: "1. Первичный скрининг и отбор на обследование"
type: summary
title: "Section conclusion: a gain in access, no added accuracy from the model"
assertion: "На стадии отбора модель снимает объём чтения и дотягивается до тех, кто иначе не придёт, и не умеет назначить порог, работать в открытом потоке и отвечать за годность снимка; взамен нагрузка переехала на другой шаг и сменился исполнитель, а держат эту нагрузку порог-документ и двойное чтение с арбитражем — и ни одна процедура не проверяет, что фильтр отсеял"
source: "—"
media: ""
media_needed: "иллюстрация не нужна: четыре шапки с пунктами держат слайд сами"
media_note: "полужирным набраны пункты, в которых лежит сам вывод: две названные формы словаря и прочерк в четвёртой шапке. Карта раздела вынесена на следующий кадр — таблицей, а не строкой"
pol_slov: 133   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 129 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
timing_min: 0.65
in_bucket: false
method_steps: ["вывод раздела"]
form: ["форма 1", "форма 5", "форма 3"]
vfy: false
status: собран
---

## Visible slide text

**What works:** reaching people who otherwise would not come — **22 → 100 out of 100** · cutting the volume of reading where the procedure is already dense — **44.3 percent less second reading**.

**What does not work:** setting the threshold — a signature stands behind it · an open-referral stream — the one attempt that actually happened ended in bankruptcy · answering for the gradability of the image.

**With the work:** the workload moved from triage to the visit, and there is now nobody to pay for it · the performer changed, and a step appeared — obtaining a gradable image.

**No procedure checks what the filter screened out. In screening, a human read every study; where the model decided, its "normal" never reached him.**

**Of the six distortions named at the opening, this section ran into one — disagreement:** arbitration grew two- and five-fold, and one review takes as long as five readings.

## Speaker notes

The outcome of the selection stage: the model cuts the volume of reading and reaches people who otherwise would not come, and it cannot set a threshold, work in an open-referral stream, or answer for the gradability of an image. The stage comes together around four questions that will also be asked at every stage after it. The numbers live on the breakdowns these generalizations were drawn from.

What works. The benefit in both breakdowns is measured in access — in how many people reached the exam and how many images a second human read. It is obtained two ways: cutting the volume of human reading where the procedure is already dense, and reaching people who otherwise would not come. The second way is stronger in this section, and the reason is simple: a test a person never reached has zero sensitivity. The model added no accuracy here, in a single breakdown.

What does not work. Three boundaries, and none of them is about the quality of the model. The model does not set the threshold: which is worse — a miss or an unnecessary call — is decided by whoever signs for it. In an open-referral stream, not one breakdown produced a benefit, and the one attempt that actually happened ended in bankruptcy. And autonomous reading does not answer for the gradability of the image: obtaining it falls to a person without specialized training. And one boundary that is easy to overextend where it does not belong: coverage gets published, the mechanics of the device do not. That does happen, but it does not split by country: the domestic radiology platform publishes coverage without the mechanics, and on that very same platform, in the Moscow mammography breakdown, the device is disclosed more fully than in any other case in this section — architecture, size of the training set, origin of the threshold, composition of the failures. The Swedish and German screening programs both publish the device's mechanics, and neither says anything about training or drift. So the split is not by country, it is by who is doing the reporting: the platform reports coverage, the device review reports mechanics.

What happened to the work. Two forms, named from the glossary. On the first-line service, the workload moved to a different step — from triage to the visit — and there turned out to be nobody to pay for the moved workload. In autonomous fundus screening, the performer changed: the decision moved entirely to the authorized device, and a derivative form appeared — a step that did not exist before. The third consequence is not a form but a property of the procedure: most of those examined no longer get a second, independent human.

What holds this up. An intervention threshold written down in a document long before any device existed. Double reading and arbitration on disagreement — where the second reader has not been replaced. And what is missing: a procedure that would check what the filter screened out. The answer to "who reviews what it filtered out" is most often "nobody", and that is not one organization's oversight — it is an empty spot in the order of work itself.

What carries forward — and this cannot be summed up in one phrase, tempting as that is. Where the model decides instead of a human, its "normal" really does not reach him: the chatbot itself answers "no need to go", and in fundus imaging the decision is made on the spot, without an ophthalmologist. But in both screening programs a human read EVERY study, and the bias there is of a different kind: he reads while seeing the model's score, and the second independent reading has been removed — so what is biased is not the composition of the stream, but the mechanics of reading. A selection error in the first case is only caught on the next cycle, by a different person on a different day; in the second, it is looked for at disagreement. That is why the next section opens with what "measured" even means.

And one mechanism out of the six named at the opening, this section genuinely ran into: "Disagreement." On the Moscow mammography stream, thirty-three radiologists pressed "disagree" one thousand seven hundred forty-five times out of eight thousand four hundred six responses — roughly every fifth time — and working through each such discrepancy is paid for in working time that, before the model, was not spent at this step.

The third consequence of the move is not a glossary form but a property of the procedure: most of those examined no longer get a second, independent human. And the answer to "who reviews what the filter screened out" is most often "nobody", and that is not one organization's oversight — it is an empty spot in the order of work itself.

What holds this workload up is an intervention threshold written down in a document long before any device existed, and double reading with arbitration on disagreement — where the second reader has not been replaced. In an open-referral stream, not one breakdown produced a benefit, and the one attempt that actually happened ended in bankruptcy.

The benefit in this section is obtained two ways, and the second is stronger: a test a person never reached has zero sensitivity, whatever it measures in the lab. So attendance here is not an organizational footnote — it is what the model's benefit at this stage is actually measured by.

And the tally on the course's own grid, which will keep growing section by section: at this step, three cells out of forty-two are filled, and none of them is about treatment. The difference between them is worth noting right away: a mode that makes the decision is adopted slowly, while modes that formalize a decision already made spread fast. Triaging a request in words has stood still since the case we broke down; autonomous decision-making without a physician is authorized only in a handful of cases, and only where the question is binary; and the model as a second reader is spreading wider than any of them — because it does not remove a single signature.

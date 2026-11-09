---
id: s64
local_id: s5-11
section: "4. Ведение медицинской документации"
type: summary
pol_slov: 143   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 139 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
# headline_number СНЯТ в круге 2 (#285, замечание владельца 8): крупным текстом кадра стояло само число «9,5 % времени в заметке», и владелец, открыв PDF до конца, вывода раздела не увидел вовсе — кадр читался как ещё одна цифра, а не как итог. Число никуда не делось: оно стоит первой плашкой со своей базой. Сбой ритма, ради которого число выносили в заголовок, в разделе остался — его держит кадр s60bab (сцена с журналом случаев 1819 года, без таблиц и плашек), то есть ровно тот приём, который канон называет первым: «один кадр без таблицы, с одной сценой»
title: "Section conclusion: what works, what doesn't, and where the load moved"
assertion: "Итог стадии тремя частями. Получается: черновик готов к концу приёма, и структуру документа больше не надо держать в голове при живом человеке. Не получается: активное время правки не сдвинулось ни у одного из двух инструментов, полнее человека документ не пишет, а вся измеренная экономия — 9,5 процента времени в заметке против контрольной группы, у одного инструмента из двух. Нагрузка переехала с набора на вычитку чужого текста, и дальше по циклу идёт то, чем эту вычитку удерживают, — подпись"
source: "—"
media: ""
media_needed: "иллюстрации нет: кадр держат полоса плашек и три названные части вывода"
media_note: "вывод подан тремя названными частями — что получается, что не получается, куда переехала нагрузка, — как требует шаг 5 строения раздела. Прежняя подача одним крупным числом снята: см. комментарий у снятого headline_number выше"
blocks:
  - {label: "The entire measured savings of the stage", value: "9.5% of note time", note: "against the control group, 4 min 22 s; absent for the second tool", key: true}
  - {label: "Active editing time", value: "did not shift for either tool"}
  - {label: "Document completeness: human → model", value: "4.13 → 3.72", note: "a blinded comparison of 100 hospitalizations"}
  - {label: "Domestic timing study of the report", value: "10 min 15 s → 8 min 2 s", note: "keyboard versus speech"}
timing_min: 0.6
in_bucket: false
method_steps: ["вывод раздела", "свод"]
form: ["форма 1", "форма 3", "форма 7"]
vfy: false
status: собран
---

## Visible slide text

**What works.** The draft is ready by the end of the visit; the structure no longer has to be held in your head while a living person is in front of you — the one step that was actually removed.

**What doesn't.** The model does not write more completely than a human. The claimed 15,791 hours have nothing to confirm them.

**The load moved** from typing to reviewing someone else's text; spot-checking of notes appeared, with its own staff. Next in the cycle is what holds that review in place: **the signature.**

*Nobody teaches this other kind of review anywhere.*

**Of the six input distortions, the section met one — correction: the physician corrects the machine's work.**

## Speaker notes

The conclusion of the documentation stage rests on one number, not two columns: after eight summaries of the same type in a row the room starts predicting the screen, and this number cannot be predicted.

And the stage's tally, so it lines up with what I've been saying along the way: there were four classical writing modes, two of them counted, and in different units — the physician's writing in minutes per note, carrying forward a prior note in a share of the chart's text. Of the stage's six actions, the model took over two and removed one. There are three breakdowns in the section: recording the visit, the discharge summary, and domestic voice dictation of the report. Nine and a half percent is about the first of the four modes and no other, and it is counted against the control group, not against zero.

Nine and a half percent is the entire measured savings of the stage for the foreign automatic visit-recording tool. Not "up to thirty percent," as people say at conferences, not fifteen thousand hours, as the health system reported: 9.5 percent of note time, in a randomized trial, for one of two tools. For the second tool, of the same mode and the same trial design, there are no savings at all — and that is the first thing to say right after the number, or the number will read as a property of the mode.

Active editing time did not shift for either of the two tools. The note is ready by the end of the visit, not by the end of the day, and the document's structure no longer has to be held in your head while a living person is there — this is a real gain, measured in a different quantity than the one it is sold in.

What happened to the work. The load moved from typing to reviewing someone else's text — the glossary form is named here and fits literally. A step appeared: spot-checking of notes, which has its own staff. And the cost of error shifted: a typo is visible, a plausible detail is not visible at all.

About the claimed savings. 15,791 hours on 63,000 visits — with no disclosed counting methodology. It cannot be confirmed, it cannot be refuted; a quarter of an hour per visit does not fit inside four minutes of work on the note, so a different quantity was being counted. A number like this does not belong next to measured ones — it is of a different nature.

The document does not write more completely than a human, and this is measured by the blinded comparison: completeness 3.72 against 4.13, unique errors 2.91 against 1.82. At the same time the potential harm of a single error is the same. The document comes out faster, reads more easily, and contains less of what is needed.

What holds this in place. Review and the physician's signature — nothing more, and that matters: no technical check mechanism appeared here. And right alongside it, stated plainly: nobody teaches this other kind of review, the kind that looks for a coherent statement with no basis in the chart. The procedure relies on a skill that is not in the training curriculum.

There are two task types in this stage, and they are worth telling apart: text generation — the visit's speech and the chart's fields go in, a draft note comes out; and audio recognition — domestic voice dictation, where the output is the text of what the physician said, and nothing beyond it. A draft awaiting review is exactly where the first mode operates, and it lands inside that same eighteen percent of characters the physician types by hand. The decision of what goes into the document, and the check that what went in was actually there, are not handed over to the machine.

Treatment gets prescribed off this document down the line — and when something goes wrong, it is the signature that gets examined. This is the bridge to the next section: it is about the signature itself, what it means, and who checks that the signer is capable of pushing back against the machine.

And one remark about the form of this slide itself, because it is transferable. Every other summary in the lecture is built on four headers: what works, what doesn't, what happened to the work, what holds it in place. Here, in their place, is one number set in large type. This is not for variety's sake: when the same form repeats six times, the room starts predicting the screen and stops reading. Breaking the rhythm brings attention back exactly at the point where this section has one number worth remembering in place of everything else.

Why nine and a half percent specifically, and not any other number in the section. It is the only quantity obtained by genuine randomization: three equal groups, random assignment, a control. Every other number in the section is either observational, or claimed, or measured in a different quantity. The next time you hear a figure of tens of percent about this stage, the first question will not be "where from," but "was there a control."

And what is deliberately absent from this conclusion. There is no conclusion "the tool is unnecessary": it removed a real load, and that is measured on the well-being scales. Nor is there a conclusion "the tool works": active editing time did not shift, and the document became less complete. The section ends with both of these things being true at the same time, and it is the one who signs who will have to choose between them.

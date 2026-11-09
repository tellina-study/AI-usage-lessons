---
id: s62
local_id: s5-07a
section: "4. Ведение медицинской документации"
type: case
title: "Example 1, cost: typing shrank, review appeared"
assertion: "Набор текста сократился, вычитка появилась отдельной обязательной операцией, и у неё теперь есть штатная служба контроля качества"
source: "A quality-control report on notes from one clinic · a three-arm randomized trial, medRxiv preprint 2025 — https://www.medrxiv.org/content/10.1101/2025.07.10.25331333"
media: ""
media_needed: "иллюстрация не нужна — схема двух дорожек строится, не ищется"
media_note: "—"
scheme:
  kind: dorozhki
  steps_arrows: true
  caption: "The physician's two tracks — and a third line: an operation someone else does"
  rows:
    - {label: "Before", steps: ["typing", "signature"]}
    - {label: "Now", steps: ["conversation", "draft", "review", "signature"]}
    - {label: "On top, by another hand", steps: ["spot-checking of notes"]}
blocks:
  - {label: "Gave", value: "note finished earlier, less fatigue"}
  - {label: "Required", value: "reviewing every draft, and a staffed department"}
  - {label: "Depends on the day of measurement", value: "7 → 16 out of 100", note: "observational; day of rollout → day 150"}
  - {label: "Net", value: "typing shrank, editing stayed the same", key: true}
pol_slov: 117  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 113 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 0.9
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало"]
form: ["форма 1", "форма 3"]
vizforma: "дорожки"
vfy: false
status: собран
---

## Visible slide text

**The physician used to hold the note's structure in his head with the patient there, type it up after the visit, and sign his own work.** Now he reviews someone else's.

**The control department's staffing — from an unpublished clinic report: this number has no address of its own.**

## Speaker notes

The cost of automatic visit recording, counted along the physician's two tracks of work: typing shrank, and review appeared as a separate, mandatory operation. Before, the physician held the document's structure in his head during the conversation and typed it up after the visit, signing his own work; now he speaks freely and then reviews someone else's text. The volume of work is comparable, the location changed — this is the form "the load moved to another step," and here it really is a move, not a disappearance.

A fifth operation is not done by the physician, and that is exactly why it stands as a separate third line on the diagram. In one clinic's report, a standing note-quality control department read more than 3,600 physician responses and collected 1,252 surveys — with its own permanent staff. The operation "spot-read machine drafts and collect feedback" did not exist in the previous process simply because there were no machine drafts. This is the form "a step appeared," and it has a measurable cost: staff. The engineer should pause here: this cost does not show up in any comparison of note time, because a different department pays for it.

One observation looks like a contradiction and is not: fatigue is lower, but active editing time is the same. What was removed was not time — it was the need to hold the document's structure in your head while talking to a person. This is a real gain, and it is measured; it is just measured in a different quantity than the one it is sold in. And this is exactly the case where the honest answer "the tool helped" and the honest answer "it did not save time" are both true at once.

The size of the effect also depends on when it's measured. A longitudinal before-and-after comparison with a control gives a reduction in note time of 7 out of 100 on the day of rollout and up to 16 out of 100 by day 150. From this come two cautions at once, pointing in opposite directions. A quick pilot underestimates: measuring the effect in the first week may miss what shows up by the fifth month, and reject a tool that actually works. And the reverse: part of the gain by day 150 is the person getting used to it, and an observational comparison cannot separate habituation from a property of the tool. So the question "how much does the tool give" has no single answer without naming the day of measurement, and a vendor who quotes one number is naming their favorite day.

For the second tool in the same trial, there was no change in time at all, under the same design and on the same population of physicians. So the measured effect belongs not to the mode of work as such, but to a specific implementation.

Let me read the diagram line by line, because the whole point of the slide is in it. The top line is how it was: type the text, sign. Two steps, both done by the physician. The middle line is how it is now: talk, get a draft, review it, sign. Four steps, all four also done by the physician. From this alone it is already clear that there are more operations, not fewer — even though one of them, typing, disappeared.

The third line stands apart, and it is the most important one here. Spot-checking notes is not done by the physician. It is a new department with new staff, and its work is not counted at all in note-time comparisons — because what gets counted is the physician's time, while the organization pays for the control. The engineer should carry this away as a rule: when an operation moves from one pair of hands to another, the savings are counted against the first pair, and the cost appears at the second, and in one report these two figures almost never meet.

The "gave — required — net" set reads off the plates left to right. Gave: note finished earlier, less fatigue. Required: reviewing every draft, and a staffed department. Net: typing shrank, editing stayed the same. None of the three plates cancels the other two, and the honest answer to "did the tool help" consists of all three at once.

Two forms from the glossary are named here explicitly. "The load moved to another step" — for typing and review. "A step appeared" — for spot-checking. The third form, "the performer is the same, but got worse," is not in this breakdown, and I will not invent it: nobody measured the quality of review before and after the rollout.

**Sources.** [a three-arm randomized trial, medRxiv preprint 2025.07.10.25331333](https://www.medrxiv.org/content/10.1101/2025.07.10.25331333)

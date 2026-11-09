---
id: s60b
local_id: s5-00
section: "4. Ведение медицинской документации"
type: divider
title: "4. Keeping the medical record"
pol_slov: 82  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 78 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
assertion: "Приём и госпитализация заканчиваются документом; раздел — про то, кто и как теперь пишет эту запись, и кто прочтёт её потом"
source: "—"
media: "rework/deck/assets/s60b-kartoteka-zapisey-patsientov.jpg"
media_needed: ""
media_note: "ВКРУЧЕН СНИМОК (круг 2, 2026-10-20): картотека записей пациентов во врачебной практике Whalsay Health Centre, 2012 — Викисклад, CC BY-SA 4.0, права и разбор отклонённых кандидатов в assets/s60b-kartoteka-zapisey-patsientov.url. Заказ был «рабочее место врача с черновиком заметки рядом с пациентом»; этого снимка в открытых источниках не нашлось не-студийным — оба найденных кандидата отклонены глазами как студийный сток (тот же признак, по которому images.md §14 уже отклонял такой кадр). Поставлена картотека: она показывает не способ письма, а предмет раздела — запись, которая переживает приём и которую читает потом другой человек"
timing_min: 0.55
in_bucket: false
method_steps: ["дивайдер"]
form: []
vfy: false
status: собран
---

## Visible slide text

# 4. Keeping the medical record

**Observation looked for deterioration in numbers. Here, the decision moves into text,** and it will be read by someone who never saw the patient. **A gap in the record and the absence of an event look the same to them.**

- **the visit note** — read by the patient themselves and the next physician
- **the discharge summary** — read by the local physician, the next hospital, the insurer

In order, and the case study first:

**Carrying forward a previous note: the heparin case and the four writing modes**

**Example 1: automated visit-note generation**

**Example 2: the discharge summary**

**Example 3: voice dictation of a radiology report**

## Speaker notes

Observation looked for deterioration in numbers; this work is built differently. The decision here isn't made by a device or a shift on duty — it's made by a person who reads the document later, sometimes months later, and never saw the patient in person. For them, the quality of the record isn't a matter of style; it's the only channel through which someone else's decision reaches them.

This work has four classical modes: the physician types the text by hand right after the visit; carries a previous note forward into a new one, editing what's changed; dictates to a live scribe; or edits a resident's draft under their own signature. Two of the four are counted, and in different units — the physician's own writing in minutes per note, carrying forward in a share of the chart's text; for the live scribe and the resident's draft, there's no figure in our sources, and the reason for each is named on the spot. The model enters this work from two directions. First — recording the visit itself: the tool listens to the conversation and hands back a draft note, which the physician proofreads and signs. Second — recording the outcome of the whole hospitalization: the model assembles the discharge document from the case history, the physician again proofreads and signs, and treatment is then ordered elsewhere from this document.

Both case studies rest on the same form. The classical mode is counted separately from the model's claimed effect; the measured effect comes from a randomized trial or a blinded comparison, not a self-report from people who chose the tool themselves; and each one names a pair — what became possible, and what it required.

The case study on the visit note shows how the claimed time savings and the measured result are two different quantities, counted in different units. The case study on the discharge summary goes further: the error count for the model and for the human is comparable, but the error is built differently — not a typo, but a plausible-sounding detail that was never in the history. The old proofreading habit of "reading it the way you'd read a colleague's note" doesn't carry over to this document.

This section ends with a document, and in medicine a document almost always sits under someone's signature. That's the bridge to the next section: what actually holds the cost of an error in check once a decision has already been made and recorded.

Let me say right away how this section is built differently from the last one. In observation, the subject was numerical: a trail of values, a score, a threshold. Here, the subject is text, and there's nothing to check it with except reading. A score has a threshold; a record doesn't: you can't say "this record is seventy percent complete" and make a decision on that number.

This section has two different readers, and they face a different cost of error. The visit note is read by the patient themselves and by the next physician — an error there costs a repeated workup or a mistaken continuation of treatment. The discharge summary is read by the local physician, the next hospital, and the insurer — an error there costs a decision made at a different institution, where there's no one left to ask. That's why this section has two case studies, not one: one tool, two stages, two different costs.

And one property worth holding in mind for the whole section, because it explains both costs. A gap in the record and the absence of an event look the same to a reader. If the document doesn't say a medication was given, the reader can't tell "it wasn't given" apart from "it was given and not recorded." No amount of careful reading fixes this: the distinction simply isn't in the document. From this follows something that isn't obvious to an engineer: completeness of the record matters more here than brevity, and any tool that makes a document shorter has to be checked against exactly that.

One last thing about the order of the two case studies. The visit note comes first because it has real randomization behind it — the strongest evidence in the whole lecture, and this stage deserves to open with it. The discharge summary comes second because it's heavier: treatment gets ordered from it at a different institution, and the error there is built differently — not a typo, but a plausible-sounding detail that was never in the case history. The old proofreading habit of "reading it the way you'd read a colleague's note" doesn't carry over to a document like this, and that will be this section's main finding.

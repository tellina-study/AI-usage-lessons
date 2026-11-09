---
# ПРИНЯЛ ОБЗОР ПО СТРАНАМ В ЗАМЕТКИ, Этап B прожарки сторителлинга (#293, П5): кадр `s60e`
# («Сколько пишут в разных странах и почему») снят по сокращению хвоста вечера, и его
# содержание перенесено сюда — в ЗАМЕТКИ, не на кадр. Перенесено всё, что было уникальным:
# длина амбулаторной заметки в США против заметки вне США при одном поставщике карты (вчетверо,
# больше 6 000 знаков против ~1 200), рост средней длины на 8,1 процента за три года после
# правки правил оплаты при падении времени на заметку на 11,1, состав записи в России,
# заданный приказом, и названное отсутствие сопоставимого российского замера длины. Адреса
# трёх работ дописаны в «Источники» настоящими ссылками. Вопрос залу того кадра («документ,
# который вы пишете для проверяющего») перенесён целиком: он про работу самого зала, и
# терять его незачем.
# ПОЧЕМУ В ЗАМЕТКИ, А НЕ НА КАДР. Кадр отвечает на вопрос «что модель заняла на этой стадии и
# чего не может», и обзор по странам в него не входит: он объясняет, ЧЕМ ЗАДАНА длина записи,
# то есть почему у этой стадии такой читатель. Это ровно тот материал, который лектор
# произносит, опираясь на одну строку тела («решает по записи тот, кто пациента не видел»), и
# место ему рядом с нею.
id: s60c
local_id: s5-01c
section: "4. Ведение медицинской документации"
type: norm
title: "What the model took over at the record-keeping stage, and what it still can't do"
assertion: "Из шести действий стадии обученная модель заняла два — набор записи и сборку выписного документа — и одно убрала: структуру будущего текста во время живого разговора теперь держит инструмент. Взамен появился новый шаг, вычитать чужое. Три места, где она не работает, названы поимённо: снять обязанность вычитки, сократить активное время правки, отличить правдоподобное от записанного. Шесть действий разложены кадром раньше и здесь не перечисляются заново"
source: "—"
media: ""
media_needed: "реальный снимок: врач после приёма дописывает запись в карту, экран и бумага рядом; постановочная улыбка в камеру не подходит"
media_note: "иллюстрация не добыта, нужен поиск"
blocks:
  - {label: "Of the six actions, the model took over", value: "two", note: "typing and assembling the document; it removed one — holding the structure in mind", key: true}
pol_slov: 114  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 110 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 0.6
in_bucket: false
method_steps: ["заземление", "①цена ошибки", "②классические режимы"]
form: []
vfy: true
status: собран
---

## Visible slide text

**Works:** typing up the note and assembling the discharge document. Holding the structure in mind during the live conversation has been taken off the person — the one place in this lecture where a step was actually removed for them.

**Doesn't work, in three places:** removing the obligation to proofread · cutting active editing time · telling the plausible apart from the actually recorded.

**Whoever decides from the record never saw the patient: a gap and the absence of an event look the same to them.**

- **record less than happened** — something already checked gets ordered again
- **record what never happened** — treatment gets ordered on a false basis

## Speaker notes

Let's break down the work of this stage before talking about tools. A twelve-minute visit: the patient talks, the physician asks, examines, prescribes — and in parallel holds the structure of the future note in mind. After the visit, or even by the end of the day, that structure gets typed into the chart; whatever didn't get done becomes homework with the chart in the evening.

The six actions of this stage are listed on the slide, and I'll add what each one actually involves. Holding the structure in mind — during the live conversation. Typing up the note — after the visit, or even by the end of the day. Proofreading and signing. Assembling the discharge document for the whole hospitalization. Handing it to the reader. Producing it if the case is reviewed.

The record isn't made for an archive, and that's the first thing worth saying. It has readers, and each one acts on it: the local physician a month later, the next hospital on readmission, another specialist at the same institution, a review committee when a case gets examined, and the patient themselves, who's entitled to a copy.

And right away, a measurement that shows how strongly the reader shapes this work. Three physicians who had implemented the same electronic record system in hospitals inside and outside the US took data from the vendor itself and counted the length of an outpatient note. The American one came out four times longer: over six thousand characters against roughly twelve hundred for specialists outside the US — with the same record vendor, the same fields, the same insertion tools. The difference can't be a difference in the product, since the product is the same; the authors name the cause outright — documentation outside the US is shorter because only what's clinically relevant goes into it, while the American note is bloated by also serving as a billing and audit document. I'll name the strength of this honestly: it's an editorial, not a study with a method, the figures were supplied by the vendor, and the sample and counting method aren't disclosed — it shows a direction and claims a magnitude. A second figure comes from the same source, with a separate sample: in the US in year twenty-one, the rules for billing a visit were revised specifically to remove documentation needed only for billing from the physician's plate; three years later, across one billion seven hundred million notes, average length didn't fall — it rose by eight and one tenth percent, while time per note fell by eleven and one tenth. People are writing faster, not shorter; length only fell at the institutions that cut back on auto-population and copying. These two series don't add up into one ledger — different samples, different years. And Russia: here, the composition of the record isn't left to an institution's discretion — standardized forms and the order they're kept in are approved by a Ministry of Health order, and the record is checked by a medical-care quality review, which looks at compliance with protocols, not at billing by volume of text. That's a different mechanism of pressure on length than the American one. There's no comparable measurement of note length for Russia: no publication with a character count, no departmental statistics — and I'm saying this outright, so that the next person who opens this question doesn't plug in a similar American number here.

**Question for the room** — about your own work: who here has a document you write not for a colleague but for an inspector, and how much longer is it than the substance actually requires?

From this comes a property of the stage that sets the cost of error: whoever decides from the record never saw the patient. A physician reading someone else's note can't tell "this didn't happen" apart from "this wasn't recorded." A gap and the absence of an event look identical to them, and no amount of careful reading fixes this — the distinction simply isn't in the document.

The cost of both errors is named before any figures. Recording less than happened — the next reader orders something already checked all over again, and at review, an action the physician actually took turns out to be unproven. Recording what never happened — treatment gets ordered on a false basis. Both errors are paid for by a person who wasn't part of this visit.

I've already presented the classical writing modes, and I won't recount them here. Briefly, as one package, so the tally doesn't drift: there are four modes; two are counted — the physician's own writing in minutes per note, and carrying forward a previous note in a share of the chart's text, fifty and one tenth percent of words; the live scribe and the resident's draft under the attending's signature are named, have no figures of their own, and the reason for each is named in the same place. The units of the two counted modes don't add up into one ledger: on time, the model is compared against the physician's own writing; with carrying forward, it converges on a different question — what happens to the reliability of the record when the document contains plausible-sounding text that no one actually said at this visit.

And a figure to hold onto whenever someone says "it got faster": in the control group, time per note fell on its own from four minutes twenty-two seconds to four minutes four. Those eighteen seconds belong to the passage of time and to practice, not to the tool.

Now the same field with the model. Of the six actions, the trained model took over two: typing up the note — a draft is ready by the end of the visit — and assembling the discharge document from the whole record. The first action was actually taken off the human: an instrument now holds the structure of the future note during the live conversation, and this is the one place in the whole lecture where a step was genuinely removed for the person. It wasn't removed for free — a new one appeared in its place, and it's heavier than it looks: proofreading someone else's text and finding in it what was never there. Three places where the model doesn't work: it can't remove the obligation to proofread — the signature stays human; it doesn't cut active editing time — typing fell, but editing stayed the same; and it can't tell the plausible apart from what was actually recorded, without tying every line back to its place in the source record.

The note on the woman with the letter is the report on her scan, plus the outcome line that will go out to her by mail. She isn't the one who reads that report: a different person reads it, two years later, when she's called back in, and they'll carry their own question — has anything changed. That's why completeness of the record is worth more than brevity here.

**Sources.** [a three-arm randomized trial, medRxiv preprint 2025.07.10.25331333, not peer-reviewed](https://www.medrxiv.org/content/10.1101/2025.07.10.25331333) · [trial registration NCT06792890](https://clinicaltrials.gov/study/NCT06792890) · [Downing, Bates, Longhurst, Annals of Internal Medicine 2018 — note length inside and outside the US](https://doi.org/10.7326/M18-0139) · [Epic Research, 1.7 billion notes, 2023 — length after the billing-rule change](https://www.epicresearch.org/articles/two-years-after-coding-changes-sought-to-decrease-documentation-notes-remain-bloated/) · [Russian Ministry of Health order No. 530n of 05.08.2022](https://www.consultant.ru/document/cons_doc_LAW_429359/)

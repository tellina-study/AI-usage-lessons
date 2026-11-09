---
# ХРОНИКА СЛУЧАЯ ПОДНЯТА В ВЕРХ КАДРА, прожарка сторителлинга #293, Этап C (П2.1). Случай
#   стоял ТРЕТЬИМ абзацем прозы под долей 50,1 % — то есть доля о частоте шла прежде
#   устройства, а само устройство читалось как ещё один абзац. Теперь порядок обратный и
#   показанный: лента «день 1 → дни 2–5 → после выписки» занимает верх кадра, доля и вклад
#   ошибок стоят под ней плашками. Примитив ленты — `build_lec07.draw_chronicle`, заведён этим
#   же этапом по образцу раскладки `udar` Этапа A.
# ЗАГОЛОВОК ПЕРЕНАЗВАН под то, что на кадре стоит первым (§5.18: название и первый блок задают
#   экспозицию): прежний «Без модели: четыре режима письма, посчитанные по-разному» называл
#   предмет НИЖНЕЙ половины кадра, и зал, прочитав его, не понимал, про что лента сверху.
# КЛАССИФИКАЦИЯ ЧЕТЫРЁХ РЕЖИМОВ СЖАТА, а не унесена: схема осталась (§5.13 требует оба
#   классических режима НА КАДРЕ, а не в заметках), но каждый шаг сведён в ОДНУ строку —
#   «имя — единица», — а строка о том, что единицы не складываются, живёт в заметках.
# ОДНОСТРОЧНЫЕ ШАГИ — НЕ УКРАШЕНИЕ, А УСЛОВИЕ, ЧТОБЫ КАДР СОБИРАЛСЯ. Двустрочные шаги держали
#   ряды схемы на 0,68" каждый; с лентой наверху подпись схемы (она рисуется ПОД рядами)
#   уходила на 6,96" при низе тела 6,82" и ложилась прямо в строку источника. Замерено по
#   собранному пакету, не на глаз. Сторож на это заведён в тот же круг — `[высота]` на сумму
#   примитивов, `build_lec07.content`; без него перелёт был молчаливым.
id: s60bb
local_id: s5-01b
section: "4. Ведение медицинской документации"
type: case
title: "Carrying forward a previous note: the heparin case and the four writing modes"
assertion: "Случай переноса предъявляется прежде доли: запись о профилактике, которой не было, переносилась из заметки в заметку пять дней, и каждый читавший считал её выполненной — после выписки тромбоэмболия. Доля под ним говорит о частоте: половина слов карты уже была написана об этом же пациенте раньше. На стадии записи работают четыре классических режима, посчитаны два и в разных единицах, у двух числа нет вовсе — причина пробела у каждого названа на месте"
source: "Tsou et al., Applied Clinical Informatics 2017 — https://doi.org/10.4338/ACI-2016-09-R-0150 · Steinkamp et al., JAMA Network Open 2022 — https://doi.org/10.1001/jamanetworkopen.2022.33348"
media: ""
media_needed: ""
media_note: "иллюстрация не нужна: верх кадра занимает лента случая, низ — плашки и схема режимов. Снимка у классического режима письма нет такого, который отличал бы перенос от набора, — именно это различение и есть содержание кадра"
chronicle:
  caption: "A patient on chemotherapy: a note on heparin prophylaxis"
  rows:
    - {when: "Day 1", text: "A note on heparin prophylaxis goes into the progress note. **No heparin was actually ordered.**"}
    - {when: "Days 2–5", text: "On transfer to another department, the note is carried forward from note to note. Everyone who reads it assumes the prophylaxis is being given."}
    - {when: "After discharge", text: "Pulmonary embolism, readmission.", key: true}
scheme:
  caption: "Four writing modes: who puts the text into the document"
  arrows: false
  rows:
    - {label: "Counted", steps: ["The physician writes it themselves — minutes per note", "Carrying forward a previous note — share of the chart's words"]}
    - {label: "Named, no figure", steps: ["A live scribe", "A resident's draft"]}
blocks:
  - {label: "Carried forward verbatim — share of the chart's WORDS", value: "50.1%", note: "104 million notes on 2 million patients", key: true}
  - {label: "Contribution of carry-forward errors", value: "2.6% of 190 errors", note: "190 across 212,165 visits"}
pol_slov: 140  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 136 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11). #293 Этап C: лента хроники вес подняла — переобъявляется по собранному PDF этапа
timing_min: 1.15
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы"]
form: []
vfy: true
status: собран
---

## Visible slide text

## Speaker notes

For a patient on chemotherapy with a previous pulmonary embolism, a note about ordering heparin for prophylaxis made it into the progress note. Heparin itself was never ordered. On transfer to another department, this note was carried forward five days running, and everyone who read it assumed the prophylaxis was being given — the note was the only thing anyone checked against. Shortly after discharge, the patient developed a pulmonary embolism and was readmitted.

The strength of this evidence: a single case report, the weakest kind there is. It shows how the error is built and says nothing about how often it happens — frequency is carried by the two figures below it, half the words in the chart, and two and six tenths percent of diagnostic errors found. The order matters: first you see how the error is built, then how often it occurs. The reverse order gives you shares behind which the room doesn't see a single person.

This is the second of the four classical writing modes — carrying forward a previous note. Before comparing the model against them, all four have to be presented and counted at the same cost: two of them are counted, in different units, and the other two have no named figure at all. Otherwise the model gets compared against an empty space, a comparison it always wins and that means nothing. The units of the two counted modes don't add up into one ledger either: on time, the model is compared against the physician's own writing; with carrying forward, it converges on a different question.

The modes are about who puts the text into the document. The five methods from the previous slide are about something else: where the characters in the note come from. Two different axes, and carrying forward a previous note belongs legitimately on both.

The first mode — the physician writes it themselves. It's counted inside the randomized trial itself: the trial has a control group that kept writing notes the old way, and their time per note is four minutes twenty-two seconds. That's the baseline for every time comparison in this section. The mode has its own drift too, and the plate carries it as a pair: over the observation period, time in the control group fell on its own to four minutes four seconds. Eighteen seconds is a small figure with a large meaning: every claim of "got faster" has to be measured against this drift, or those eighteen seconds of time simply passing get credited to the tool. The strength of this figure: a preprint, never peer-reviewed.

The second mode — carrying forward a previous note: the earlier note moves into the new one, whole or in blocks, with edits for what's changed. For a long time this was treated as a bad habit of individual physicians; measurement showed it's the main way text actually gets into the chart.

A full review of the records at one large health system over six years — a hundred four million notes on nearly two million patients — found that half of all the text in the chart, fifty and one tenth percent of the words, verbatim repeats something already written about the same patient before. The unit here has to be stated plainly: this is a share of words, not a share of notes — not "half the notes are copied," but "half of what's written had already been written." The share rises year over year: thirty-three percent for notes from year fifteen, fifty-four for notes from year twenty.

And one line without which the room will hear a contradiction where there isn't one: fifty and one tenth is a share of the chart's WORDS, forty-six a share of a note's CHARACTERS. Different units, different samples: the numbers don't contradict each other, and they don't add together.

The strength of this figure: a peer-reviewed measurement of a complete sample from one system, with a count reproducible from the published method. The weak side is named by the authors themselves: the signal is a verbatim match, so carrying forward with rewording is invisible to the count, and the share is more likely understated than overstated.

This mode's cost of error has been measured too. On diagnostic errors in primary care: out of two hundred twelve thousand visits over a year at two large urban centers, researchers pulled cases where unplanned care followed a visit within two weeks, and physician reviewers found a hundred ninety diagnostic errors. Carry-forward errors contributed two and six tenths percent of all those found. A caveat on attribution is needed here, and it's mandatory: the full text of the original study couldn't be accessed, and these figures were read from a systematic review that cites it; until checked against the original, the attribution runs explicitly through the review.

The third mode — a live medical scribe: a person at the visit, in the room or remote by connection, writing the note on the physician's behalf while they talk with the patient. This isn't exotic: this mode has its own market, its own cost per visit, and its own literature on saving physician time. It's named and not counted: it was never an arm of the randomized trial, and pulling its cost from a different study would mean combining two unrelated samples.

The fourth mode only applies to the discharge document: a resident writes the draft, the attending physician signs it. It's also named and also without a figure, and the reason is its own, named explicitly: the blinded comparison of a hundred hospitalizations, which this section comes to as its second case study, used the attending physician's own document, not the resident's. So the blinded comparison says nothing about this mode, and its numbers can't be substituted in here.

And the last thing to carry away from this slide. The model doesn't converge on the second mode by time — it converges on a question that turns out to be load-bearing for this whole section: what happens to the reliability of the record when the document contains plausible-sounding text that no one actually said at this visit.

**Sources.** [Tsou et al., Applied Clinical Informatics 2017](https://doi.org/10.4338/ACI-2016-09-R-0150) — the review the heparin case and the figures 7.4 · 35.7 · 2.6 are drawn from · [Steinkamp et al., JAMA Network Open 2022](https://doi.org/10.1001/jamanetworkopen.2022.33348) — the share of the chart's words carried forward verbatim

---
id: s63aa
local_id: s5-10
section: "4. Ведение медицинской документации"
type: case
title: "Example 3: voice dictation of the radiology report"
assertion: "Отечественный разбор, в котором классический режим и режим с моделью посчитаны В ОДНОЙ ЕДИНИЦЕ — хронометраж описания одного исследования: клавиатура 10 минут 15 секунд, распознавание речи 8 минут 2 секунды. Сорок лет до этого та же технология проигрывала клавиатуре вчетверо, и это стоит на кадре рядом с выигрышем"
source: "Kudryavtsev et al., Digital Diagnostics 2023 — https://doi.org/10.17816/DD321420 · Moscow City Health Department, 07.01.2023 — https://www.mos.ru/news/item/118060073/"
media: ""
media_needed: "реальный снимок: врач-рентгенолог описывает исследование в гарнитуру у рабочей станции"
media_note: "иллюстрация не добыта, нужен поиск"
scheme:
  caption: "Reporting a single study, two orders of work"
  arrows: true
  rows:
    - {label: "Without the model", steps: ["Image on screen", "Typing on the keyboard", "Editing and signature", "Report in the chart"]}
    - {label: "With the model", steps: ["Speech into the headset", {text: "The model recognizes it", ai: true}, "Editing and signature", "Report in the chart"]}
blocks:
  - {label: "Baseline: keyboard entry", value: "10 min 15 s per study", note: "one CT or MRI report"}
  - {label: "Speech recognition, same measurement", value: "8 min 2 s", note: "−2 min 13 s, 21.6% of the baseline", key: true}
  - {label: "Scale as of January 2023", value: "210,000 reports", note: "the vocabulary trained on 2.5 million reports"}
pol_slov: 142  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 138 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 0.95
in_bucket: true
method_steps: ["①цена ошибки", "②классические режимы", "③модель против них", "④как это устроено"]
form: ["форма 1"]
vfy: true
status: собран
---

## Visible slide text

*Speech recognition: the physician's speech goes in, the report's text comes out.*

**For forty years this technology lost to the keyboard:** in 1981, voice input took four times as long and produced 12 errors against zero.

**How it was measured.** Radiologists at seven polyclinics reported studies both ways; time was measured by stopwatch.

## Speaker notes

Radiologists at seven polyclinics reported radiology studies both ways, and time was measured by stopwatch. Keyboard entry — 10 minutes 15 seconds per report; speech recognition — 8 minutes 2 seconds. Minus 2 minutes 13 seconds, 21.6 percent of the baseline.

This is the only case in the whole section where the classical mode and the mode with the model are counted in the same unit, on the same physicians, and on the same work. And it is the only case all evening where you can see how one and the same technology failed to work for forty years, and then started to.

I'll start with the failure, not the win, and that is a deliberate reversal of the form. In 1981, keyboard and voice input were compared on sixty radiology reports. Report length did not depend on the method of entry — so the complexity of the studies described was similar too. And the time it took to fill out by voice exceeded the keyboard time fourfold, and the reports filled out by voice contained an average of twelve recognition errors, while the ones typed on a keyboard contained none. The systems of that time did not suppress outside noise, and physicians' speech was recognized poorly. Remember this pair of numbers: four times slower, and twelve errors per document. The same task, the same field, the same type of tool — and the opposite answer to today's.

Now the current measurement. The first study of speech-recognition effectiveness in radiology departments was carried out in 2020 at seven city polyclinics of the Moscow City Health Department, on the Voice2Med voice-input system from the TsRT group of companies — at that time still the version with 93 percent recognition accuracy. The study compared the speed of filling out documentation by keyboard versus speech recognition; radiologists filled out reports for CT and MRI studies. The timing study gave the following: average time to report one study by keyboard — 10 minutes 15 seconds; by speech recognition — 8 minutes 2 seconds.

Let's subtract it ourselves, out loud: two minutes thirteen seconds, that is, 21.6 percent of the baseline. Keep in mind that the baseline is named here, and it could be named — unlike half the numbers shown to us about this stage. By January 2023 the Moscow City Health Department reported more than 210,000 radiology reports filled out by voice, and a reduction in preparation time of "more than 20 percent." Notice something rare: the agency's figure and the independent timing study agree. That is not always the case — in this very section we saw a claim of fifteen thousand hours that agrees with nothing.

On the mechanics. Input is the physician's speech through a headset, during the study or right after it. Output is text that is automatically carried into the open report in the medical information system; the physician edits and signs it. What it is trained on: the medical-terms vocabulary was built on 2.5 million radiology reports, and the recognition accuracy of medical terminology in Russian rose from 93 percent to 98. Task type is recognition, modality is audio. This is a different cell of the course's grid than the two previous breakdowns: those were text generation, this is audio recognition. The model does not decide what goes into the document and proposes nothing — it turns speech into characters.

Now about the classical mode that our section was missing, and the domestic material closes that gap. The live scribe — the third writing mode — was named in our breakdown and never counted. In domestic healthcare, its closest relative, dictation transcription centers, was tried, but there are no publicly available scientific studies of its effectiveness, and no such centers remain in the current domestic system. The review's authors draw a cautious conclusion from this: the application turned out to be impractical. This is an honest refusal to deploy, and it is worth more than one more case of success: the mode existed, it was tried and dropped, and nobody left us a measurement after that.

**Sources.** [Kudryavtsev N.D., Bardasova K.A., Khoruzhaya A.N. Speech recognition technology in radiology diagnostics // Digital Diagnostics. 2023;4(2):185–195](https://doi.org/10.17816/DD321420) · [statistics from the Moscow City Health Department, January 7, 2023](https://www.mos.ru/news/item/118060073/)

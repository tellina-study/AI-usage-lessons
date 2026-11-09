---
id: s61a
local_id: s5-07aa
section: "4. Ведение медицинской документации"
type: case
title: "Example 1, Russia: a voice assistant fills out the visit note"
assertion: "Тот же инструмент, что на предыдущем кадре, но в отечественном развёртывании и с доказательством другой силы: московский голосовой помощник расшифровывает разговор врача с пациентом и сам заполняет поля протокола приёма; с сентября 2026 он у всех участковых врачей взрослых городских поликлиник — более трёх тысяч специалистов. Качество протокола эксперты оценили в 4,8 из 5 — столько же, сколько у заполненного человеком. Минутной базы нет ни у одного заявленного эффекта: «внимание выросло вдвое» дано без исходной величины, «от трети до половины приёма уходило на протокол» — оценка поставщика, а не замер"
source: "Moscow City Health Department, 09.09.2026 — https://www.mos.ru/news/item/175489073/ · Moscow City Health Department, 25.06.2026 — https://www.mos.ru/news/item/171864073/"
media: ""
media_needed: "реальный снимок приёма у участкового врача московской поликлиники, где на экране открыт протокол; постановочный сток не подходит"
media_note: "иллюстрация не добыта: кадр держат схема двух порядков и полоса плашек"
scheme:
  caption: "The same visit, two orders of work — a domestic deployment"
  arrows: true
  rows:
    - {label: "Without the model", steps: ["Conversation", "The physician types it up", "Signature"]}
    - {label: "With the model", steps: ["Conversation", {text: "The assistant sorts it into fields", ai: true}, "The physician reviews and corrects", "Signature"]}
blocks:
  - {label: "Moscow primary care physicians with the assistant", value: "more than 3,000", note: "all adult city polyclinics, since September 2026", key: true}
  - {label: "Note quality, per expert rating", value: "4.8 out of 5", note: "the same as a note filled out by a person"}
  - {label: "Physician's attention to the patient", value: "more than doubled", note: "among neurologists; the starting figure is not stated"}
pol_slov: 120
timing_min: 0.95
in_bucket: true
method_steps: ["③модель против них", "④как это устроено", "названный пробел"]
form: ["форма 1"]
vfy: true
status: собран
---

## Visible slide text

*Speech recognition: the visit conversation goes in, the note's fields come out.*

**How it was measured.** Expert rating of finished notes. No blinding and no control group.

**Trained on de-identified recordings of real visits.**

## Speaker notes

The same task — automatic recording of the visit — here at home. It should be read as a pair with the foreign measurement, which had randomization, a control group, and minus 9.5 percent of note time: the same tool, but a different deployment and evidence of a different strength.

What was done. The Moscow voice assistant runs in the background during the visit: it transcribes the conversation between physician and patient and enters the complaints, history, diagnoses, and recommendations — whatever was said out loud — into the note itself. At the end of the consultation the physician sees the finished document, checks it, corrects it if needed, and signs it. It is trained on de-identified data from real visits so that it can recognize medical terminology; the data and transcripts travel over the city medical system's secured channels.

On scale. It started with neurologists, and there the service is already in every adult city polyclinic. Since September 2026 it has covered every primary care physician — more than 3,000 specialists. A primary care visit is noticeably harder for this task than a neurology visit, and the city says so itself: people come in with all kinds of complaints, often with several conditions and a long history, and the service has to do more than recognize speech — it has to sort what it hears into the note's sections. The refinement work went on over the summer, with feedback from the physicians themselves.

Now to the numbers, and here one has to be careful, because the temptation to read them as a measurement is strong. Experts rated the quality of the prepared notes at 4.8 points out of 5 — and the first publication says something important: the same as if a person had filled out the note. This is the only number in the section where a domestic result is directly set against the human mode, and it is worth remembering next to the foreign breakdown of the discharge summary, where a blinded comparison gave, for completeness, not "the same" but worse: 3.72 against 4.13. The two results diverge, and they diverge not by country but by how they were measured: there, 22 reviewers read the documents blind, not knowing which text was machine-written; here, an expert rating with no declared blinding and no published protocol.

Next come two numbers that have no base, and I'll say so directly. First: the physician's time of focused attention on the patient more than doubled. Doubled from what — not stated: there is no starting figure in minutes in the publications. Second: filling out notes takes physicians anywhere from a third to half of the visit's time. That is an estimate from the head of a vendor company's division, not a stopwatch measurement, and it describes the "before," not the result. Compare it with the domestic breakdown that comes later: there, a timing study across seven polyclinics gave 10 minutes 15 seconds by keyboard against 8 minutes 2 seconds by speech recognition — both figures in the same unit. That is what a number with a base looks like, and that is what a number without one looks like.

What I looked for and did not find. Publications with a minute-level measurement of this Moscow service — neither in peer-reviewed journals nor in agency reports; as of today the sources on it are statements from the city health department. I record this as a fact of the section: the gap belongs to the measurement, not to the deployment, and minutes from the foreign trial cannot be substituted in here — that trial is in a different language, with a different visit note, and a different tool.

And the conclusion this slide stands next to the previous one for. Scale of deployment and strength of evidence are different things, and they grow apart. The foreign trial covered 238 physicians and delivered genuine randomization; the Moscow deployment covered more than 3,000 and delivered an expert rating. An engineer choosing such a tool will have to decide what weighs more for them: that the whole city already uses it — or that its effect has been measured by someone against a control group.

**Question for the room.** The notes were rated by experts, with no blinded comparison and no control group. Which way would such a rating skew the result — and why? Type one word in the chat.

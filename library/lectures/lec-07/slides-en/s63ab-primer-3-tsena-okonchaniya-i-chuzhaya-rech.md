---
id: s63ab
local_id: s5-10a
section: "4. Ведение медицинской документации"
type: case
title: "Example 3, cost: word endings, other people's speech, and a number with no base"
assertion: "Цена отечественного выигрыша названа конкретно: распознаются окончания слов и чужая речь, мешает шум работающего оборудования, приверженность зависит от возраста врача; 62,8 процента — это САМООТЧЁТ врачей, а не замер. Рядом — второе отечественное внедрение, где сокращение 27 процентов опубликовано БЕЗ минутной базы, и этот пробел назван на кадре"
source: "Kudryavtsev, Bardasova, Khoruzhaya, Digital Diagnostics 2023;4(2) — https://doi.org/10.17816/DD321420 · NIIOZMM (Moscow City Health Department's Research Institute for Healthcare Organization and Medical Management), \"Moskovskaya Meditsina\" (\"Moscow Medicine\"), endoscopy centers, 2022 — https://niioz.ru/moskovskaya-meditsina/zhurnal-moskovskaya-meditsina/luchshie-praktiki/funktsiya-raspoznavaniya-rechi-dlya-opisaniya-issledovaniy-v-endoskopicheskikh-tsentrakh/"
media: ""
media_needed: "иллюстрация не нужна — кадр держат полоса плашек и перечень того, что мешает распознаванию"
media_note: "—"
scheme:
  kind: dorozhki
  caption: "Two independent sources of result spoilage — and neither is in the model"
  rows:
    - {label: "What was said", steps: ["word endings", "other people's speech in the room"]}
    - {label: "What it was recorded with", steps: ["equipment noise", "a cheap microphone"]}
blocks:
  - {label: "Report an increase in their own efficiency", value: "62.8% of those surveyed", note: "2022 survey of radiologists; self-report, not a measurement of time", key: true}
  - {label: "Second deployment: two endoscopy centers", value: "−27% of report time", note: "180–200 studies a day per center; HOW MANY MINUTES IT USED TO TAKE — not published"}
pol_slov: 122  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf после добавления схемы «дорожки» (§11.3: кадр type=case без схемы — блокирующее). Перечень источников порчи переехал с тела на схему, тело сжато на его вес
timing_min: 0.85
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало", "названный пробел"]
form: ["форма 3"]
vfy: true
status: собран
---

## Visible slide text

**The physicians most willing to take up the tool are those aged 30–40.**

**62.8 percent is the share of physicians who THINK SO, not a measured time.**

**The second deployment claims −27% of report time. From how many minutes? Say it out loud — and we'll check it against what was published.**

## Speaker notes

The fourth and fifth steps of the breakdown: what moved, and what the win was paid for. I'll start with what is usually treated as a trifle, and for an engineer this is exactly the substance.

Word endings. This is not nitpicking about product quality, but a property of the Russian language, named by the developers as a separate challenge: the system has to choose case and number where English speech requires no such choice. For a document this matters more than it looks: "a lesion in the right lung" and "lesions in the right lungs" differ by exactly their endings, and an error here does not look like an error — it looks like text.

Other people's speech. Physicians reported situations where the system recognized someone other than them. Three people speak in a radiology room: the physician, the patient, and staff. A tool that puts what was said by someone other than the author into the document creates exactly the defect the whole section is concerned with — plausible text that nobody meant to put into this particular report.

Noise and microphone. Recognition quality is negatively affected by the operation of diagnostic equipment and by medical staff talking with the patient or with colleagues, as well as by low-quality audio recording devices. Remember this as a rule of transfer: for a tool that listens, part of the result lies not in the model but in three thousand rubles' worth of hardware and in the room's acoustics. Neither of these is usually described in a publication about the model.

Age and adoption. Younger specialists are more open to the technology, and physicians aged thirty to forty take it up more readily than others. This too is a cost: a tool whose effect depends on who is using it cannot be rolled out by directive and expected to deliver the publication's average result.

Now about a number that is easy to mistake for a measurement. A 2022 survey of radiologists found that 62.8 percent of respondents report an increase in the efficiency of their own work when using speech recognition. I'll say this slowly: 62 percent is the share of those who think so. Not the share of time saved, and not the share of reports filled out faster. Agreeing with a tool and benefiting from a tool are two different quantities, and the first is always higher than the second, because it includes the relief a person feels even when a stopwatch does not register it. We have a separate time measurement — the very timing study — and it gives 21 percent, not 62.

And the second domestic deployment, worth pausing on for a minute. In 2022, the same technology for reporting endoscopic studies was deployed at two Moscow endoscopy centers — at Botkin Hospital and Buyanov Hospital, each performing between 180 and more than 200 studies a day. A timing study of the average report-filling time before and after rollout was carried out, giving an average reduction of 27 percent, with recognition quality above 97 percent and full physician satisfaction.

And now what is missing from this publication, and this is exactly our course's business. How many minutes filling out the report used to take BEFORE the rollout — not published. Only the share is named. Twenty-seven percent of ten minutes and twenty-seven percent of two minutes are different things for planning, and there is no way to choose between them from this publication. Compare it with the previous slide: there, both 10 minutes 15 seconds and 8 minutes 2 seconds are named, and the share can be calculated yourself. Here there is nothing to calculate. This is not a reason to dismiss the rollout — it is real, on a real patient flow; it is a reason to know that a share with no base of its own does not transfer to another hospital.

The question for the room here is set up as a game, and the answer to it is a gap, not a number. I state the claim: minus twenty-seven percent of report time in the second deployment, two endoscopy centers, 180 to 200 studies a day per center. And I ask the room to say out loud how many minutes this is counted from: ten? two? Let at least one guess be voiced. After that I reveal it: the starting time was not published at all. Only the share is named. Twenty-seven percent of ten minutes and twenty-seven percent of two are different things for scheduling a visit, and there is no way to choose between them from the publication. By this point the room has usually already named its own number — and that is exactly what every reader does with a statement like this: fills in the base themselves, without noticing that they did.

**Sources.** [Kudryavtsev N.D., Bardasova K.A., Khoruzhaya A.N. Speech recognition technology in radiology diagnostics // Digital Diagnostics. 2023;4(2):185–195](https://doi.org/10.17816/DD321420) · [NIIOZMM of the Moscow City Health Department, "Moskovskaya Meditsina" ("Moscow Medicine"): speech recognition in endoscopy centers, 2022](https://niioz.ru/moskovskaya-meditsina/zhurnal-moskovskaya-meditsina/luchshie-praktiki/funktsiya-raspoznavaniya-rechi-dlya-opisaniya-issledovaniy-v-endoskopicheskikh-tsentrakh/)

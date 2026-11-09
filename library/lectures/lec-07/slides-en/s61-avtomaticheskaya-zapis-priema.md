---
id: s61
local_id: s5-07
section: "4. Ведение медицинской документации"
type: case
title: "Example 1: automatic recording of the visit"
assertion: "Заявленная экономия времени и измеренный рандомизированным испытанием результат — разные величины, посчитанные в разных единицах; активное время правки не изменилось"
source: "A three-arm randomized trial, medRxiv preprint 2025 — https://www.medrxiv.org/content/10.1101/2025.07.10.25331333"
media: ""
media_needed: "реальный снимок приёма, где врач говорит с пациентом, а экран в стороне, без постановочной улыбки в камеру"
media_note: "иллюстрация не добыта, нужен поиск"
scheme:
  caption: "The same visit, two orders of work: without the model on top, with it below"
  arrows: true
  rows:
    - {label: "Without the model", steps: ["Conversation", "Structure held in the head", "The physician types it up himself", "Signature"]}
    - {label: "With the model", steps: ["Audio of the visit", {text: "The model produces a draft", ai: true}, "Reviewing someone else's text", "Signature"]}
blocks:
  - {label: "Baseline: the physician writes it himself", value: "4 min 22 s per note", note: "control group; its own drift — 18 seconds"}
  - {label: "First tool against the control group", value: "−9.5% of note time", key: true}
  - {label: "Active editing time", value: "did not change for either tool"}
  - {label: "Claimed by the vendor, no methodology given", value: "15,791 hours on 63,000 visits", note: "a quarter hour per visit does not fit inside four minutes"}
pol_slov: 147   # ПЕРЕМЕРЕН (#293, Этап B): кадр получил строку-мост («первым на эту стадию пришёл инструмент, набирающий саму запись») после снятия обзора по странам между ним и кадром стадии. 143 слова замером по собранному PDF + запас 4. ПРЕЖНЯЯ ПРИЧИНА ПОЛА: ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 140 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 1.05
in_bucket: true
method_steps: ["③модель против них", "④как это устроено"]
form: ["вопрос залу"]
vfy: true
status: собран
---

## Visible slide text

**The first tool to reach this stage was one that writes the note itself.** *Text generation: audio of the visit goes in, a draft note comes out.*

**How it was measured.** 238 physicians, three equal groups: two tools and ordinary practice. **The second tool showed no change** — the effect belongs to the implementation, not the class.

## Speaker notes

The automatic visit-recording tool: audio of the visit goes in, a draft note comes out. It was the first tool to reach this stage. And the first thing said about it was a claim: a large health system reported saving 15,791 hours on 63,000 visits over ten weeks of work. The counting methodology was not disclosed.

Let's look for the base ourselves, out loud. 15,791 hours on 63,000 visits is about a quarter of an hour per visit. Now recall what unit the note's time is measured in: minutes and seconds, on the order of four minutes. Fifteen minutes of savings per visit do not fit inside four minutes of work on the note — you cannot save more than the whole operation cost. So the claim is counted in a different quantity, most likely total time spent in the chart altogether, and it cannot be set against the measured result.

From this comes a formulation worth carrying out of the lecture whole: a number with no stated counting methodology can neither be verified nor refuted — it is not a statement about the world. This is not nitpicking over the magnitude. Fifteen thousand hours might be true; the trouble is there is nothing to prove or disprove it with, and in the vendor's presentation it sits next to measured numbers in the same type size.

Now the measured result, and I'll name the strength of the evidence before the number: this is a preprint, it has not been through peer review, trial registration NCT06792890. A trial with genuine randomization and three equal groups covers 238 outpatient physicians across fourteen specialties: two commercial tools and ordinary practice. For the first tool, note time dropped by 9.5 percent relative to the control group; for the second, there was no significant change. Both tools affected the well-being scales — the overall professional well-being score rose by 2.76 on a scale from ten to fifty — and there was no difference between the two tools on these scales.

The control group's own baseline matters too: there, note time over the observation period dropped on its own from 4 minutes 22 seconds to 4 minutes 4 seconds. Eighteen seconds with no tool at all — that is practice and the passage of time, and every "it got faster" is counted against this figure, not against zero.

In a multicenter observation of emergency departments, the note was finished earlier, patients more often noted that they were being listened to, and the strain on attention fell — but the active time spent editing the note did not change. Typing shrank; editing stayed the same. This is what stands on the slide as the gold plate: of all the numbers in this breakdown, this is the one least convenient for selling and most useful for planning.

From this comes a conclusion stronger than either number: one design, one population of physicians, two products of the same mode — and one result significant, the other null. The measured effect belongs to the implementation, not to the tool's class, and the phrase "we deployed automatic visit recording" carries no information about the result.

About the mechanics, one also has to say what is missing from the trial. Input is the audio of the visit, output is a draft note that the physician reviews and signs; what either tool is trained on, the preprint does not disclose. They have no names in the trial either: they are called "the first" and "the second," and that is a limitation of the work, not of our retelling — there is no way to verify from this publication which product gave the significant result. The names of this mode are known, and I'll name them so the mode can be recognized: Abridge, Dragon Copilot, Nabla, Heidi. By task type this is text generation.

The question for the room is about their own work: who reads an automatic meeting note line by line before sending it out. For many in the room such a note is already written automatically, and the answer "I skim it" is exactly the review whose cost is being measured here.

**Sources.** [a three-arm randomized trial, medRxiv preprint 2025.07.10.25331333](https://www.medrxiv.org/content/10.1101/2025.07.10.25331333) · [trial registration NCT06792890](https://clinicaltrials.gov/study/NCT06792890)

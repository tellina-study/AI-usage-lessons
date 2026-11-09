---
id: s63a
local_id: s5-07c
section: "4. Ведение медицинской документации"
type: case
title: "Example 2, cost: a different kind of review"
assertion: "Вычитка не исчезла, она сменила предмет: искать надо не опечатку, а правдоподобную подробность, которой не было; а растиражированная тройка чисел об этом случае построчно не подтверждается ни одним из трёх открытых первоисточников"
source: "A prospective pilot, JAMA Network Open 2026 — https://doi.org/10.1001/jamanetworkopen.2026.16556 · Cureus 2026 — https://doi.org/10.7759/cureus.109247"
media: ""
media_needed: "иллюстрация не нужна — слайд держится на полосе плашек и двух абзацах"
media_note: "—"
scheme:
  caption: "Where review sits and what it looks for"
  arrows: true
  rows:
    - {label: "At night", steps: ["Chart and progress notes", "The model assembles a summary"], arrows: true}
    - {label: "During the day", steps: ["The physician reads it if he chooses to", "Looks for what wasn't there", "Signature"]}
blocks:
  - {label: "Machine-generated content was used", value: "in 219 of 384 discharges", note: "there were 1,274 summaries"}
  - {label: "Per hundred summaries", value: "25 omissions · 20 inaccuracies · 2 fabrications"}
  - {label: "Of a hundred unedited summaries", value: "88 with no potential for harm", note: "1 moderate · 0 severe"}
  - {label: "The trio of harm figures that reviews cite", value: "is not computed in any of the three studies", key: true}
pol_slov: 139   # ПЕРЕОБЪЯВЛЕН ПО ЗАМЕРУ в круге #285 §2.4 (механизмы искажений проведены в разделы 1–5): вес 135 по собранному PDF одиннадцати правленых кадров (parts-sec/krug285.pdf, pymupdf постранично) + запас 4. Не оценка по файлу кадра: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11).
timing_min: 1.05
in_bucket: true
method_steps: ["⑤что переехало", "пара дало–потребовало"]
form: ["форма 7"]
vfy: true
status: собран
---

## Visible slide text

**The discharge summary was written and signed by the attending physician**; at teaching hospitals a resident prepared the draft — a mode with no number attached.

**Correction, the sixth input distortion, works in our favor.** Review changed its target: the eye is tuned to catch a typo, but what it has to look for is a statement that was not in the medical record. **Nobody teaches this kind of reading.**

## Speaker notes

Review of a machine-written discharge summary did not disappear — it changed its target: the eye is tuned to catch a typo, but what it has to look for is a plausible detail that was not part of this hospitalization. This is how correction works, the sixth of the evening's six input distortions and the only one of them that works in our favor: the physician corrects the model's conclusion when he finds an error in it. Correction has a measured magnitude, and it was taken in a different field, on ECGs: out of 159,630 real records from one American clinic for 2011–2023, the physician corrected the machine's conclusion in 31.3 cases out of 100. That is, almost one in three — and this is the most direct answer available to the question of whether the human in the loop really works. Alongside it, from the same group of studies, stands the flip side: a suggestion accepted without checking is later corrected in 53 cases out of 100, against 18 if it was checked right away. Correction exists; it simply happens later than it should.

The fourth step of the breakdown is to name what moved. What moved here is review, and it moved not to a different place but to a different target.

The old review skill was built for human error. The eye is tuned to a typo, a cut-off sentence, a skipped section — to what a tired person leaves behind at the end of a shift. A machine error is built differently: it is a coherent, stylistically appropriate statement that was not in the medical record. The old skill cannot find it, and nobody yet teaches this new kind of reading — not in residency, not in continuing-education courses, not in the tool's own instructions.

How much of this review actually gets done was measured prospectively. For 384 discharges the system produced 1,274 summaries; physicians used the machine-generated content in 219 cases — 57 out of 100. The unit here has to be held firmly, and the plate names it: 57 out of 100 is the share of DISCHARGES, not the share of summaries produced. There were three times as many summaries as discharges, and if you take summaries as the denominator, the same event gives 17 out of 100. One and the same observation, two legitimate numbers, different denominators — and both can be printed without lying.

Per hundred summaries, omissions were found in 25, inaccuracies in 20, fabrications in 2. And of a hundred unedited summaries, 88 were judged to carry no potential for harm, one capable of causing moderate harm, with no cases of severe harm. The definitions here differ from those in the blinded comparison, and the two sets cannot be combined into one list.

Now about the trio, and this is the most transferable part of the section. A tidy trio of numbers circulates in reviews about this case, citing a "study of a hundred discharge summaries." A line-by-line reading of the three available primary sources does not produce it: no study counts in the definitions in which it is retold. Numbers that sound convenient live longer in retellings than in primary sources.

The practical conclusion for an engineer sounds the same in any industry, and it stands on the slide as its own line. When a review carries a number with a citation to a study, the citation has to be checked not for whether the study exists, but for whether the study actually computes this exact quantity under these exact definitions. Here it does not, and the three numbers held up only because nobody opened the primary source. A retelling is weaker evidence than a study even when their numbers happen to match.

And last, about the third source. A single-center before-and-after comparison in a rehabilitation unit was published in a journal with author fees and minimal peer review. I name it rather than hide it: the evidence is weak, and conclusions should not be built on it alone — but it helped check the trio exactly as much as the two strong studies did.

On conflict of interest. It is disclosed in the publications themselves: some of the authors work for the company that makes the model, or hold a patent on it. A disclosed conflict does not make the study worthless — it makes it a study that is read more carefully, and the first thing to check is who decided what counts as success. An undisclosed conflict is worse than a disclosed one for exactly this reason: it cannot be accounted for while reading.

**Sources.** [a prospective pilot, JAMA Network Open 2026](https://doi.org/10.1001/jamanetworkopen.2026.16556) · [a blinded comparison of 100 hospitalizations, JAMA Internal Medicine 2025](https://doi.org/10.1001/jamainternmed.2025.0821) · [a single-center comparison, Cureus 2026 — a journal with author fees and minimal peer review](https://doi.org/10.7759/cureus.109247)

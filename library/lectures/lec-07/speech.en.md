---
lecture: 7
title: "Lecture 7. Lecturer's Speech. The Decision About a Person: Who Looks, Who Signs, Who Pays"
length_words: 5580  # count: spoken words across all 43 fragments, excluding headers, markup, and bracketed stage directions (RU count; EN count given in the translation report)
length_min: 90
status: draft
version: v2
issue: 293
branch: lec07-rech-kaskad-293
date: 2026-10-22
pacing_target: "90-minute slot — owner decision #2: 80 minutes of content plus 10 for questions; a hard ceiling of 95 words per minute on any fragment"
pacing_actual: "81.65 minutes by the timing_min fields of 91 slides, consolidated into 43 fragments; average pace 68.3 words per minute, 0 of 43 fragments go over 95"
slot_overrun: "the deck's content runs 81.65 min against a slot budget of 80.00 (90 minus 10 for questions): an overrun of +1.65 min (was +7.3). The speech is written on top of the current timing_min fields; on any cut, it is removed together with its slide — cut order in rework/CUT-ORDER.md"
audience: "practicing third-year engineers, many of whom code with an assistant; no basic definitions are given. No questions are asked about the audience's own work"
slide_anchors: "91 slides"
source: "chapter.md + chapter-part1b…chapter-part5c (114,588 words, pass of 2026-10-20) · deck.yaml + deck-part2.yaml + deck-part3.yaml (91 slides, sum of timing_min 81.65) · slides/*.md"
keystone_axis: "The cost of error is held up by the procedure built around the human. Reading the data got cheaper — the cost now falls on four human steps: attention, skill, signature, arbitration"
refrain_1_99_seconds: "s05 · s38 · s106 — three times"
throughline_1_distortions:
  presented: "s01ad, Section 0 — six names given verbatim and WITHOUT measurements: Anchoring · Narrowing · Skill decay · Alert stream · Disagreement · Correction; the measurements are presented within their own sections"
  where_named_in_speech: "Disagreement — Section 1 (s13–s15a) · Narrowing — Section 3 (s41) · Anchoring — Section 3 (s44–s47 and s49/s49_1) · Alert stream — Section 3 (s49e–s49f) · Correction — Section 4 (s63–s63a) · Skill decay — Section 5 (s73f)"
  summary: "a dedicated summary slide was cut; the thread closes inside the ledger of payments on s102 — all six show up, and exactly one is named by its own name: skill decay"
throughline_2_misattribution_count:
  slide: "s98 in Takeaways"
  refrain_number: "13 of 21 — stated in Takeaways (s98) and repeated in the Closing (s105)"
  composition: "2 of 21 with no trained model involved at all · 7 of 21 come down to the threshold, the composition of the dataset, the stated goal, the order of presentation, or implementation · 4 of 21 grew in the retelling · 7 of 21 are domestic practice"
cases_total: 21
audience_questions: "11 predictions made on case material, revealed afterward — s01ad · s22a/s24 · s26 · s33a · s41 · s49→s49_1 · s61a · s63ab · s73c · s97 · s106 final. Not one question is about the audience's own work (owner decision 2026-10-22)"
---

# Lecturer's Speech · Lecture 7

**Slot:** 90 minutes — 80 of content and 10 for questions. The deck's content currently runs **81.65** minutes, an overrun of **+1.65**.
**Slides:** **91** across eight named sections, consolidated into **43** speech fragments.
**Spoken words:** 5,580; average pace 68.3 words per minute, the ceiling of 95 is not exceeded on a single fragment.
**Detailed cases:** 21, of which 7 are domestic practice.
**The through-line person of the evening:** a woman summoned by letter based on her year of birth. She appears in the Opening, and returns in Sections 1, 2, 3, 4, and in the Closing.

---

## Preparation before the lecture

- **[s01]** Open `library/lectures/lec-07/rendered/lec-07.pdf` on the first slide and hold it there until the first word. If the projector fails, hand out the paper printout `rendered/lec-07-notes.pdf`; the thread holds on the four payments named on slide `s05`.
- **[s01ac]** Decide the response channel ahead of time: they write in the chat. If the room stays silent for twenty seconds, name your own example from IT and move on.
- **[s01ad]** Read all six names aloud, verbatim — Anchoring, Narrowing, Skill decay, Alert stream, Disagreement, Correction — and add not a single number to any of them: the measurements belong to their own sections (`s15a`, `s41`, `s49_1`, `s49f`, `s63a`, `s73f`). Check against the slide that there really are no numbers on it.
- **[s19a]** Open the Roszdravnadzor registry (`roszdravnadzor.gov.ru`, search "Celsus Mammography") and check the status of the registration certificate. The figure "two years and nine months before insurance reimbursement" is as of the deck's build date; if it has changed, say the new figure out loud.
- **[s27a–s27b]** Check whether a follow-up to the Moscow study has come out covering 2025. The slide shows 575,549 images, May through September 2024. If a new period has been published, say it out loud.
- **[s49]** This slide is performed, not narrated: it and `s49_1` together take one minute. Strict order: set up with the baseline 84.86 / 86.38 → ask the question aloud twice → pause → reveal on `s49_1` in the same order it was asked. Have a closed-form, show-of-hands question ready: "the drop is less than fifteen points" versus "the drop is cut in half."
- **[s63b]** Open the Glass Health and Corti websites and check whether either one has published an accuracy measurement. Right now the slide shows a dash, and it is named as a dash.
- **[s73cb]** This slide stands first in Section 5, and that's its job: it sets the grade of evidence that both clinical cases ahead of it will be read against — the one place in the section where the no-assistant result is measured by randomization. It is delivered as a measurement taken in programming; the delivery makes no reference to the audience's own work.
- **[s98]** Memorize three numbers: 21 cases, 13 of 21, 7 of 21 domestic. This is the evening's refrain number — it is spoken twice.
- **[s102_1]** A dark slide with a single sentence: hold the pause silently for a few seconds, and do not correct the on-screen sentence with your voice. Right after the pause comes the caveat about screening (1.55 against 1.76 per thousand) — without it, the sentence isn't true.
- **Cut order** — `rework/CUT-ORDER.md`. It is not announced to the room: a slide canceled out loud devalues the slide you yourself chose to keep.
- **Leave five minutes for questions** deliberately. If the room stays silent, ask your own question from `s106`.

---

## Section 0. Opening: The Apparatus of Reading (s01 … s05 · 6.90 min)

### [s01 · 0.40 min] Cover

[The slide is already on screen. Don't read the subtitle.]

"Good afternoon. Today, someone's scan will be read before a human being ever looks at it.

[pause 3 seconds]

Lecture seven. The decision about a person: who looks, who signs, who pays."

### [s01_1 · 0.35 min] The hit: every third scan

[The whole screen changes — a dark slide.]

"England, the year to March 2024: 8.19 million chest X-rays. A trained model read about 2.8 million of them.

[pause 3 seconds]

It opens every third scan first. That's how the field lives now. The question for tonight is what the human does now."

### [s01a–s01aa · 1.70 min] The cycle of care and the gate of approval

"Medical care is an order of stages, each with its own decision. Before a decision: whether to call someone in for a look, what gets measured, how a finding gets explained. The decision gets made, and treatment follows. After the decision: noticing deterioration, and writing down what the next person will learn. Two more stages stand around that core — admission with oversight, and professional qualification. We'll walk through five stages of this cycle tonight.

The order rests on three supports. Only someone who was called in can be looked at. Rates are counted within the group that the selection process assembled. The "sick" threshold is set by a protocol calibrated to the cost of the outcome.

[diagram: the gate of approval]

The path to the patient runs through a gate of regulatory approval. Without a registration certificate, a device can't be used on a human being, and can't be bought with budget money. In the US there are two roads. The short one: a claim of similarity to something already approved — 97.5 out of 100 go this way. The full cycle, with clinical trials — 1.04. There is no short road in Russia.

By the registry: 1,553 devices out of 1,614 are approved by similarity, 21 by the full cycle. New approvals come in at 3.1 a year, with no acceleration. Registration in Russia runs end to end, costing anywhere from six hundred thousand to three million rubles, depending on class."

### [s01ab · 0.75 min] The makeup of the pool, and a cross-country row

[We've just counted the first counter — approved. This slide is about the same counter, in depth.]

"Now, the pool itself. Radiology: 1,230 out of 1,614. Psychiatry: zero. In 2025, a model sits inside every tenth new US medical device. In 2015, it was two per thousand.

[cross-country row]

Six rows per million population. Korea has two of its own: 1.70 by innovation status, 0.95 by reimbursement — that's 49 out of 549. Russia, across its entire registry, stands at 0.39 — higher than the US, Japan, and China. Our first ones were 2 out of 57.

There's no ranking here: each row has its own criterion of selection."

### [s01ac · 0.65 min] In use, and reimbursed

[The third counter in a row, and the three must not be confused: approved — in use — reimbursed.]

"Physicians with a model in their loop number around three million out of thirteen to fifteen million; in Russia, it's fifteen to twenty-five percent out of seven hundred seventy thousand. Approval is broader than reimbursement: a permanent reimbursement code exists for three devices out of 1,614, while in Korea reimbursement covers the same 49 out of 549.

[question to the room]

Who among you has a model sitting in their own loop — and who looks into its failures?"

[pause 20 seconds, answers in the chat; if the room stays silent, name your own example and move on]

### [s01ad · 0.80 min] Six distortions of the input: the names

"The frame for tonight: six names, with no numbers attached to them — the measurements belong to their own sections.

**Anchoring** — the conclusion drifts toward the hint. **Narrowing** — where the model stays silent, the eye doesn't linger. **Skill decay** — without the model, people find less. **Alert stream** — dismissal starts happening wholesale. **Disagreement** — a mismatch becomes a separate step of its own. **Correction** — the one that works in our favor: the physician corrects the model.

[lower your voice]

This frame isn't ours — it's drawn from a body of work on distortions that show up alongside a model. A warning doesn't help; action does.

[question to the room]

Which of the six will turn out to be the most costly for the physician — and which for the patient?"

[pause 20 seconds. The patient's side will not make it onto the screen tonight — that's a named gap, and it's worth acknowledging in one sentence if someone asks.]

### [s01b · 1.10 min] How it's decided without a model, and four rungs

"Data about a person gets gathered six ways: a visit, an examination, an instrumental study, a lab test, a review of documents, a remote study. With a model, the ways stay the same; what changes is who decides on the basis of what's obtained.

The classical modes — we'll keep coming back to them. Screening: double reading, arbitration by a third reader. Diagnostics: two rates against a protocol threshold. Diagnosis: a second opinion and a consilium. Monitoring: an early warning score. Documentation: record structure, proofreading, a signature. Oversight: a case review after the outcome.

The regulator requires that a human be the final link. The European standard says it more precisely: the human must retain the ability to disagree and to overrule. It doesn't require presence at every single decision. Notice what's missing from these foundations: accuracy. It has been measured that the human is often not more accurate.

[A ladder of four rungs of participation is on the slide; we'll sort the cases in Section 3 onto it — point to it now.]"

### [s05 · 1.15 min] The axis of the evening, and four addresses of payment

"Now for the measurement this whole evening stands on. Fifty practicing physicians each read five descriptions of real cases and built out their reasoning: hypotheses, justification, checks. They were scored blind. The model alone scored 92 out of 100, a human alone scored 74, a human on top of the model scored 76. The two-point difference is not significant.

[point to the scale, pause]

Three seconds and zero rubles, against forty-eight seconds of human reading. Different units — the comparison is by order of magnitude. Reading the data got cheaper — now it's the step the human performs that pays for it. Four addresses of payment: attention, skill, signature, arbitration. Remember them: at the end of the evening, we'll put a measurement under each one.

And the line at the bottom of the slide, which we'll come back to twice: checking a hint has been measured — a median of 1.99 seconds."

---

## Section 1. Primary Screening and Selection for Examination (s11 … s20b · 13.25 min)

### [s11–s12a · 2.60 min] What this stage is, and how it works without a model

"Section one of five. Primary screening: examining people with no complaints, by a formal criterion. Before anyone gets treated, someone decides who gets looked at.

What's known here is sparse: age, sex, interval. There's one question — whether to call someone in for a look. This stage comes first because nobody sees the person who was never called in, and the threshold gets set by a document before any accuracy measurement exists. Without a model, there are three classical orders: call people in by age, wait for a complaint, triage the people who showed up by severity.

[diagram: seven actions]

The stage has seven actions: set the threshold, call people in from a list, take the scan, have two people read it, arbitrate, report the outcome, triage the stream. A model takes over three of them. The threshold, the invitation, the imaging, and arbitration stayed with people, and one step got added: obtaining a usable scan.

The letter this lecture opened with came out of here: a program takes the list of residents, selects by age and sex, and mails out invitations. The person didn't come in on their own — they were called. Keep this woman in your head: we'll meet her four more times tonight."

### [s13–s15a · 2.80 min] Case one: the Swedish program, and who gets stuck with the second reading

"The World Health Organization's criteria from 1968 are still in force today, and not one of the ten is about the accuracy of an algorithm.

Case one, and let's start without a model. The Swedish program calls everyone in by age: two people read the scan, and a third arbitrates any mismatch. Per thousand screened, they find 5.1 cases; the program misses 1.76, and a symptom finds those later. The second classical order — wait for a complaint — is more widespread, and it doesn't come at zero cost: late-stage disease there runs 57 out of 100 found cases, against 39 among those who were invited.

Now, the same program with a model. The radiologist reads first and issues the report on their own; the model gives the scan a risk score from one to ten. At scores one through nine, there's no second reading; at a ten, double reading stays. The publication doesn't name the system; Transpara, Lunit INSIGHT MMG, and iCAD ProFound occupy this mode.

[pause]

And here's the price. A British trial counted **disagreement**, the fifth of our six distortions: there are more mismatches, and a third reader resolves each one. Arbitration consumes 3.9 out of 100 readings, against 9.4 at one center and 11.3 against 13.8 at another. Trust runs the opposite way from what you'd expect: a radiologist's finding gets double-checked three times as often as a model's finding, yet it's confirmed six times less often. And the raw count of disagreements — 3,449 arbitrations without the model, against 5,283 with it, on the same fifty thousand women.

Germany hasn't replaced a single human reading. The figure of 56.7 out of 100 that circulates about it is a recalculation under a hypothetical scenario."

### [s16–s16a · 1.85 min] Case two: a first-line chatbot, England

"Case two. England, a first-line triage service: a person describes a complaint, and the app returns a route. The classical mode is a telephone triage line.

The app passed an exam at 81, against 72 for physicians. That result was used to justify rolling it out into open traffic; nobody measured the quality of the triage itself.

Here's what happened. Round-the-clock triage — that's one. A loss on every patient: the commissioner paid an extra 10.5 million pounds a year on a registered list of around forty-nine thousand people, while the entire per-capita payment for that list was around 7.6 million — that's two. Bankruptcy in August 2023, after a valuation above four billion dollars, with assets of five hundred thousand pounds — that's three.

[lower your voice]

So what was actually inside it? Three people spoke up. Hugh Harvey, the company's head of regulatory affairs — inside, an if-then decision tree in a table. David Watkins, an outside physician, had been writing to the regulator about missed cases since 2017. The company itself, in a 2016 publication — a probability graph with rules layered on top. There is not a single independent audit. There was no trained model making decisions here."

### [s18–s18b · 2.55 min] Case three: the retina gets scanned at the visit

"Case three. Adolescents aged eight to twenty-one with diabetes are checked once a year for retinal damage. Missing it: symptom-free until vision loss. Calling someone in needlessly: a visit to a specialist who may not even be available locally. Both classical orders are counted in attendance: 22 out of 100 make it to an ophthalmologist once a year; doing no screening at all gets zero.

They started scanning the retina right at the primary-care visit — and 100 out of 100 made it to screening. This is one of the two figures the evening gives us in the positive column.

Now for the price. The executor changed by document — the one such case in the whole lecture: responsibility for a missed finding moved from the physician to the device. The first one approved, in 2018, was IDx-DR, now LumineticsCore: two images go in, one of three outcomes comes out — refer, normal with a repeat in a year, or image unfit for reading. And a stream appeared that the specialist never sees at all — 75.7 out of 100. Before, the normal cases used to reach them, and they could check."

### [s19–s20 · 2.65 min] Case four: Moscow, a second reader for mammograms, and the section's takeaway

"Case four, domestic. Moscow mammography screening: the device "Celsus Mammography" reads the scan first, the physician second. Four-view mammograms go in; a number from zero to one for each breast comes out. Faster R-CNN with a ResNet-50 backbone, trained on 3,641 images.

The area under the curve moved along a path: 0.73 — 0.81 — 0.94, where 0.5 is a coin flip and 1.0 is no misses at all. It took two years and nine months before the report became something insurance would actually pay for.

Accuracy was measured on a hundred studies out of 593,261, and the reference standard was the report of the very physician the model is meant to stand in for: it can't be measured as better than that by construction. The physician disagreed with the model 1,745 times out of 8,406 — disagreement again. There's no payoff in outcomes: detection rate, recalls, and interval cancers weren't collected, and the authors themselves say so.

[the section's takeaway]

What works: reaching people who otherwise wouldn't come in — 22 to 100 out of 100. What works: cutting the volume of reading — 44.3 percent less second reading. What doesn't work: setting the threshold — a signature stands behind that. What doesn't work: open-ended traffic — the one attempt ended in bankruptcy. And separately: nothing checks what the filter screens out."

### [s20b · 0.80 min] A glossary: nine forms the relocation of work takes

"Now, a glossary, and it comes here because four cases have already gone by. In place of the image "the load shifted to the right," each one of them gets a named form.

Nine forms the relocation of work can take: the load moved to a different step · a step disappeared · a step appeared · the load grew · the load shrank · the executor changed · the order of work changed · the cost of error shifted · the executor got worse. The row "got better" stays empty: there are no measurements to put under it."

[Transition: name the second stage.]

---

## Section 2. Instrumental and Laboratory Diagnostics (s22 … s33a · 13.85 min)

### [s22–s24 · 2.35 min] What this stage is, and how accuracy gets counted

"Section two of five. In screening, the decision was who gets looked at. Here, a person gets measured by an instrument, and their condition becomes a value that will be read somewhere else, at some other time.

There are four ways to capture that value, and one can't substitute for another: an instrument applied directly to the person; a lab test, when the person is no longer there; a functional test under a loading protocol; or remotely, when whoever reads it never saw the patient. A model has taken over two actions out of six, and not the hardest ones.

[question to the room]

A question for you. You're told the accuracy is 94 percent. What group was it measured on?

[pause 15 seconds]

And one more, before the slide turns over: the exact same configuration is about to be applied to two groups of ten thousand people each, differing only in the proportion who are sick. By how much will the share of true alarms diverge — by a quarter, by half, by a factor of ten?

[pause 10 seconds, collect guesses]

Let's work it out. Out of a hundred sick people the system finds 94; out of a hundred healthy people it scares 11 for nothing — and nothing inside the system itself changed at all. This is the operating threshold — the value above which the system declares "sick" — and it's the same one for both groups. The share of alarms that turn out to be real disease: 8 out of 100 in the population-wide stream, 79 in a specialist department. Almost a tenfold difference. It has a name — positive predictive value — and a physician sees it directly in clinic. Our woman with the letter stands in the population-wide stream: for her, it's 8 out of 100."

### [s26–s27_1 · 1.95 min] Input quality, throughput, and the hit: 55 out of 100

"The classical mode of this stage is a fitness-for-reading check on the measurement, and a technician at the machine decides it by the lab's own instructions. The instrument itself has no such rule built in. Let an unfit scan go through to reading, and a report gets issued on whatever is visible — and from there follow a wrong diagnosis, a repeat study, lost weeks. With a model, the fork splits in two: it can reject the unfit scan itself, and the person gets a repeat visit; or it doesn't reject it, and reads whatever it was given.

[question to the room]

Which of these two errors is more costly: rejecting a usable scan, or reading an unusable one?

[pause 10 seconds. There is no "correct answer" in general here, and that's the point: the cost of the outcome decides it, not the model.]

How much of the stream the model actually reads isn't really known: the English share has two official denominators floating around — sometimes 34 out of 100, sometimes 40 — while in the US, a number of this kind doesn't exist at all.

[dark slide, the whole screen changes]

But here's a number that is known exactly. Not a single physician opens 55 out of 100 preventive chest scans. That's 315,491 images out of 575,549, over five months of 2024, in Moscow.

[pause 3 seconds]"

### [s27a–s27b · 2.40 min] Case five: Moscow, the preventive scans no human reads

"Case five, domestic, and the heaviest one of the evening. Those same 55 out of 100 — now let's take apart how they came about. Fluorography and chest X-rays, three services, May through September 2024.

Here's how it's built. Sensitivity was set to one, specificity was declared irrelevant: an alarm gets raised on anything even partly resembling an abnormality. The operating threshold is derived from an extreme asymmetry in the cost of error. 45 scans out of 100 go into "not normal" — a radiologist reads those. The rest go straight into the chart with nobody reading them.

[pause 3 seconds]

Infiltrates and opacities missed: 266 out of 290.

Now the money. Reading one scan by a human got more expensive: 155.62 rubles against 132.98. A model's report: 6.9 rubles. Over five months, that came out to 43.1 million against 76.5 million — savings of 33.4 million. That entire saving comes straight out of exactly those 55 scans nobody reads.

And one more thing. The layer that found those 290 missed cases won't exist in routine operation: in the study itself, people reread every single "normal" under the study protocol. The miss rate will stay. There's no way left to see it."

### [s27c–s31 · 5.70 min] Cases six, seven, eight, and nine

"Case six, same Moscow, same circle of services — the opposite answer. Intracranial hemorrhage: 3,409 head CT scans, 67 clinics, from 2022 through 2024. Out of a hundred sick patients, the model finds 96, the physician 99; false alarms, 293 against 4. Autonomy was not granted. The cost of a false alarm decides this, not the model's quality.

Case seven. Thailand, eleven clinics, six months: nurses and technicians photographed the retina, the system read it on the spot in under a minute. It was trained on images selected for quality; in the field, selection is done by a human with no formal rule. 21 out of 100 get rejected for quality — 393 out of 1,838 — and each one is a repeat visit. The rollout failed. The reading itself worked.

Case eight. Skin. Three models on one validation set: 656 images with a confirmed diagnosis, 207 of them on dark skin tones. On dark skin, a model's ability to tell sick from healthy is 9 to 15 out of 100 worse, where 50 is a coin flip and 100 is no misses at all. The average across the whole set stays decent; the subgroup that was scarce in the training set pays for it.

Case nine. Selection for a high-risk care management program, the US. Which patients to flag for intensive monitoring used to be a physician's call — it became the call of a single number. That number was trained to predict future treatment spending, while the decision actually being made was about illness. Spending reflects how much care people seek, and at equal health that differs between groups. The result: at an equal risk score, chronic disease is 26 out of 100 more common, across 100,000 patient-years. The study didn't measure the effect on money or on health."

### [s33–s33a · 1.45 min] The section's takeaway, and five questions before the question of accuracy

"Let's pull the section together. You can go wrong in three places without the model itself ever being at fault: the instrument measures the input, a human assembles the dataset, a variable sets the goal. That's how three cases out of five failed; the fourth failed in the reading itself.

Of our six distortions of the input, this section hasn't run into a single one on the physician's side, and the reason is simple: the model reads the stream alone.

From this come five questions that we ask before the question of accuracy. What group were the rates computed on. What is the input measured by — an instrument shows normal, while a blood test shows oxygen deprivation: 12 out of 100 against 4, and there's no trained model anywhere in the instrument at all. What was the training set assembled from. What does the system treat as its goal. What does a false alarm cost. "What's its accuracy" is question number six.

[question to the room]

Which of these five, in your view, derails deployment most often?

[pause 10 seconds; the answer on the slide is three out of five derailed on deployment]"

---

## Section 3. Reaching a Diagnosis (s35 … s50 · 18.40 min)

### [s35–s38 · 2.80 min] What this stage is, the second opinion, and four rungs

"Section three of five, and by density of measurement, this is the core of the evening. The previous stage produced quantities. Here, a conclusion gets drawn from them, and a human puts their signature on it. They now read both the scan and the hint sitting next to it.

One framing device, for scale: a cough for three weeks, evening fevers, four kilograms lost. Out of four possible diseases, the scan and the blood test ruled out two; two remained, indistinguishable by the scan alone. The model occupies three actions out of seven — building the differential list, the second reading, and the signature. And it added one: deciding whether to trust the hint.

The classical mode here is a second opinion, and it rests on independence. The second reader is denied access to the first report, and a third resolves any mismatch. A "second opinion" from the very model that supplied the first one is never truly second: the error becomes shared, and it doubles instead of averaging out. The order of presentation here has been measured: the hint is given either before a person has formed their own opinion, or after.

[question to the room]

In which direction, and by how much, will treatment decisions diverge?

[pause 15 seconds, collect guesses]

8.9 points. Seventy physicians, 254 cases.

And the last instrument we'll carry into the cases ahead: four rungs of participation — reads first, reads second, reads only the disputed ones, signs without looking. Training doesn't move you up a rung: 44 trained physicians each read six clinical cases, and the share of correct reasoning across 264 readings went 84.9 → 73.3 out of 100 when part of the recommendations were wrong. And on the fourth rung, the formal requirement gets satisfied in 1.99 seconds — the very same number from the axis of the evening."

### [s41 · 1.90 min] Case ten: a measurement of the gaze

"Case ten. Ten radiologists read sixty mammograms twice: once on their own, once with a hint that was deliberately wrong in both directions. Alongside that, twelve radiologists in another program: 150 studies, also read twice, with the approved system Transpara 2.1.0 from ScreenPoint Medical.

Watch what the gaze did. 11.1 out of 100 of the scan's area was examined, against 9.5; readers lingered longer at the flagged spot — 4.4 seconds against 5.4. The search narrowed down to what was hinted at.

[question to the room]

Now place a bet on the outcome. Where the hint stayed silent, what happened to the miss rate — the same, less, more? And by what factor?

[pause 15 seconds, collect guesses]

Twice as much, more. On a subgroup of fourteen cases, missed cancers went to 61 out of 100 of those actually present, against 29. The price: treatment that comes later, and comes worse.

This is **narrowing**, the second of our six distortions: where the model stays silent, the eye doesn't linger, and a miss by the model becomes a miss by the reader.

A second study turned up the opposite sign: there, readers requested the annotation themselves, after their own reading, and the gain turned out not to be significant."

### [s44–s47 · 3.30 min] Cases eleven and twelve

"Case eleven. Eleven pathologists of varying experience distinguished two types of liver cancer across eighty digitized slides. Confusing the two tumor types means different treatment. Share of correct calls: the model alone, 0.842; the pathologist alone, 0.898; the pair, 0.914. Here the pathologist is stronger than the model, and the pair beats both sides. The pair's gain didn't hold up across the group, and the report states it as a single number: "no effect." Broken down by whether the hint was right, the effect runs fourfold in both directions: around 0.94 when the hint was correct, around 0.50 when it was wrong. The average is the same; the spread grew. This is **anchoring**, and a human still puts the signature on it.

Case twelve. A Swedish trial: 105,934 women randomized between two reading orders. In one, double human reading. In the other, a radiologist reads first, the model reads second, and any mismatch goes to an arbiter. Missed cancers: 20 out of 100 of those present, against 26. Interval cancers per thousand: 1.55 against 1.76, and the improvement isn't proven: a ratio of 0.88, with an interval from 0.65 to 1.18. The volume of human reading is 44.3 percent lower. **Disagreement** became a routine step, and recalls became neither more nor fewer."

### [s49–s49_1 · 1.00 min] An ECG with a machine interpretation: the room bets on the outcome

[This slide is performed. Strict order: the setup on `s49`, the reveal on `s49_1`.]

"Thirty trainees, fifteen each: cardiology residents and other specialties. A hundred ECGs, each read three times; the machine interpretation arrives before their own decision.

With a correct interpretation, both groups read almost identically: 84.86 and 86.38.

[question to the room; the question is asked twice, because it has two halves]

How far will these two numbers drop on an incorrect interpretation — by five points, by fifteen, in half? And for whom is the drop steeper?

[pause 15 seconds. If the room stays silent: a closed, show-of-hands question — "the drop is less than fifteen points" versus "the drop is cut in half." Count the hands out loud.]

Before I reveal it: the two groups' experience differs — thirty-six months versus twenty-eight. Specialty is what separates them.

[turn the slide]

41.66. And 27.43. Both drop, by half. The less expert group loses 15.75 points more. With an incorrect interpretation, agreement with it stood at 30.77 against 42.31, by median.

This is anchoring. Specialty protects, but it doesn't save you."

### [s49a–s49d · 4.10 min] A rule from 106 trials, and case thirteen

"These were individual cases. There's a general rule too, assembled by a preregistered systematic review: 74 studies, 106 trials, and only the ones that measured all three values — human alone, model alone, and the pair — were kept.

The headline number of the whole review is minus 0.23: on average, the pair is worse than the stronger of the two sides. Here's the part that matters most. Where the model is stronger than the human, the pair is 0.54 worse than the model — and at the same time, 0.74 better than the human alone. Both figures are measured on the same trials, and together they are the rule: the pair beats the weaker side. It never catches up to the stronger one.

Case thirteen is exactly about this. Thirty surgeons assessed risk from 150 written case descriptions, with outcomes followed forward for thirty days. Underestimate the risk, and the patient gets operated on as a routine case, with no reanimation standing by. Overestimate it, and the operation gets postponed — and in a thirty-day count, it no longer shows up at all.

On three outcomes out of four, the pair is more accurate than the surgeon alone — mortality, 0.870 against 0.841. But on septic shock, the pair gives 0.712 — lower than both the surgeon, at 0.820, and the model, at 0.816. Where the model's edge is largest, the pair added nothing at all: 0.834 against 0.833. Nobody examined the patient.

[the pulled-together answer]

Four measurements we've gone through, and one takeaway. The surgeons lost precisely where the human was stronger. Fifty physicians with a language model are indistinguishable from a reference book. The systematic review: the score runs against the stronger side. The gaze measurement: the sign is set by whether the hint was right. And in not one of the four did the human's decision actually reach the patient."

### [s49e–s49f · 2.10 min] Case fourteen: an early warning model for sepsis

"Case fourteen. A sepsis model built into the medical record — a penalized logistic regression; there's no deep network here at all. Retrospective, 27,697 patients. The cost of a miss: hours before reanimation. The cost of a false alarm: past a hundred of them, people start closing them without reading — that's time taken away from another patient.

The comparison has to be against the early warning score that's been standing there for decades. Confirmed out of alarms raised: the score gets 8 out of 100, the model gets 12. It didn't leave the same range.

An alarm comes up on 18 out of 100 admissions; 12 out of 100 raised alarms get confirmed — those are counted from different denominators, and you must not confuse them. To find one real case, you have to work through eight alarms. An independent validation measured an area under the curve of 0.63, against a claimed 0.76 to 0.83: 33 cases out of 100 actually caught. The authors' own conclusion, verbatim: "adds little to what clinicians already do."

This is **the alert stream**, the fourth distortion of the input. The distribution of inputs shifted; the threshold stayed put. And how many alarms a physician dismisses has been measured across a whole class of such systems: 90 out of 100. Only 0.5 were judged, after the fact, to have actually been warranted."

### [s49g–s50 · 3.20 min] Case fifteen: Moscow, AIDA, and the section's takeaway

"Case fifteen, domestic. Moscow, a general-practice visit. The device AIDA reads the whole medical record, and before the physician decides, it proposes a final diagnosis as a code. The entire record goes in: complaints, history, exam, labs, protocols. One code with an uncertainty score comes out. A Longformer, up to 8,192 tokens, 1.5 million records.

Where the physician and the model agree — 2,635 cases — both are right, 99 out of 100, and there's nothing left to decide. The entire price sits in the fifth of cases where they disagree: 697 cases, the physician right in 64 out of 100, the model in 45. One case out of five, and neither one is reliable.

The reference standard itself is unstable: on 168 cases out of 3,500, three experienced physicians failed to agree at all.

[the section's takeaway]

Six cases from one stage, one instrument — and opposite outcomes. The Swedish trial: one human reading on top of the model beats double reading. The surgeons: that same pair falls below both sides. What diverges is how the procedure itself is built — whether the independence of the two opinions is preserved, and in what order the hint gets shown. What holds this together is a threshold calibrated to the cost of both kinds of error, and arbitration on the mismatches. The rung of participation is nowhere written down, and whatever isn't assigned slides toward signing without looking.

Of our six distortions of the input, this section ran into four: anchoring, narrowing, alert stream, and disagreement as a routine step."

---

## Section 4. Maintaining Medical Documentation (s60b … s64 · 12.40 min)

### [s60b–s60c · 4.15 min] What this stage is, and how it's kept without a model

"Section four of five. The diagnosis has been made. Now that same decision moves into text, and a month from now it will be read by someone who never saw the patient.

There are two documents. A visit note gets read by the patient themselves and by the next physician: they listen to the conversation and put complaints, exam findings, diagnosis, and orders into text. A discharge summary gets read by the local physician, the next hospital, and the insurer: there's nothing to listen to — it's assembled from daily notes covering the whole hospitalization.

The stage doesn't add a measurement of its own. There are five ways to produce a note, and one of them is carrying the previous one forward. This stage comes after monitoring: the note gets read later, and it's read by a different person with their own question in mind.

Why it's kept at all. A decision about a person outlives the one who made it: a physician will change jobs, a patient will show up at a different institution a year later, and only the text travels between them.

[carrying notes forward]

Here's the classical mode of writing, measured before any model entered the picture. Half the words in a chart — 50.1 percent, across one hundred four million notes on two million patients — had already been written about that same patient before. Note length varies by multiples across countries, and its composition is set by regulation; those figures sit in the slide's notes.

How this plays out for one actual person. For a patient on chemotherapy, a note about heparin prophylaxis got carried forward into the next note. Heparin had not been ordered. It got carried forward for five days, and every reader assumed the prophylaxis was being given. After discharge: a pulmonary embolism.

What the model has taken over here: drafting the note and assembling the discharge document. Holding the structure in your head during a live conversation with the person has been lifted — the one place in this lecture where a step was actually taken off the human. What it can't do: remove the duty to proofread, shorten the active time spent correcting it, or tell the plausible apart from the actually recorded."

### [s61–s62 · 2.90 min] Case sixteen: automated transcription of the visit

"Case sixteen. The audio of a visit goes in, a draft note comes out. How it was measured: 238 physicians, three equal groups — two tools and ordinary practice.

Baseline: a physician writing it themselves — four minutes twenty-two seconds per note. The first tool gave minus 9.5 percent time against the control group. The second showed no change at all. Which means the effect belongs to the implementation, not to the class of tool. Active correction time didn't change for either one.

Alongside that, our own case. In Russia, a voice assistant fills out the visit protocol: a conversation goes in, protocol fields come out; it's trained on de-identified visit recordings. Since September 2026 it's been in use by more than three thousand primary-care physicians across Moscow's adult city clinics. Experts rated protocol quality at 4.8 out of 5 — the same as a human-filled protocol. "Attention doubled" is given with no baseline value behind it.

[question to the room]

The protocols were rated by experts, with no blind comparison and no control group. Which direction would such a rating push the result — and why? Write one word in the chat.

[pause 15 seconds]

And here's the relocation that has to be named precisely. The physician used to hold the note's structure in their head during the visit, type it up afterward, and sign their own work. Now they proofread somebody else's. The vendor claims 15,791 hours saved across sixty-three thousand visits — a quarter hour per visit. That doesn't fit inside the measured four minutes, and there's no methodology behind the number."

### [s63–s63a · 2.10 min] Case seventeen: the discharge summary

"Case seventeen. The medical history goes in, a draft narrative section comes out. A hundred hospitalizations, 22 reviewers, each document read blind by two of them.

The machine-written summary came out shorter and more coherent. And less complete: completeness, 3.72 against 4.13 on the reviewers' scale. Unique errors per document: 2.91 against 1.82. At least one error was carried by 9 machine summaries out of 11. The cost of error shifted: the same party writes it, the reader pays for it.

[lower your voice]

And here, for the first time this evening, a distortion works in our favor. **Correction** — the physician fixes the machine's output when they find an error. But proofreading changed its target. The eye is tuned to catch a typo; what you have to look for is a claim that never appeared in the medical history. Nobody trains anyone for that kind of reading. Correction has a measured magnitude, and it was taken from ECGs: out of 159,630 records at one clinic, the physician rewrote the machine's report 31.3 times out of 100. Almost every third one."

### [s63aa–s64 · 3.25 min] Case eighteen: voice input, the boundary of what counts as a medical device, and the takeaway

"Case eighteen, domestic. Radiologists at seven clinics described studies by keyboard and by voice, timed by stopwatch.

First, a bit of history, which does real argumentative work here. For forty years, this technology lost to the keyboard: back in 1981, voice input took four times as long and produced 12 errors against zero.

Now, the number this case is in the lecture for. 62.8 percent — the share of radiologists who THINK SO. A self-report from a 2022 survey, not measured time.

[question to the room]

And alongside it, a second rollout, two endoscopy centers: a claimed minus 27 percent in protocol time. Starting from how many minutes? Say it out loud, and we'll check it against what was actually published.

[pause 15 seconds, collect guesses]

Let's check: the baseline time was never published at all. The baseline given there is 180 to 200 studies a day per center, and not a single minute.

And here's the boundary we'll remember. It runs along the signature. Propose a code for the physician to check: that's documentation. Propose a diagnosis for the physician to check: that's already a medical device, even when the check is mandatory. Glass Health and Corti do exactly this, building out a tentative diagnosis in real time as the conversation happens. Neither one has a published accuracy measurement. The 46 percent figure that circulates about them is agreement between the physician and the suggestion, not accuracy.

The section's takeaway. A draft is ready by the end of the visit, and the structure no longer has to be held in your head while talking to a living person. The model doesn't write any more completely than a human does. The claimed 15,791 hours have nothing behind them that would confirm it. The load moved from drafting to proofreading someone else's work. Of our six distortions, this section ran into one — correction."

---

## Section 5. Professional Qualification: Upkeep and Decay (s73b … s73i · 8.35 min)

### [s73b–s73ca · 1.85 min] What gets measured here, and what keeps the form

"Section five of five. Up to now we've been measuring the work — here, we measure the human: are they in form.

Skill gets spent silently. Data on it comes from four sources: an audit of decisions — the share of procedures with a finding; time, by a stopwatch; a count of procedures per year; periodic recertification. Case review happens after the outcome, and doesn't count toward any of these. This stage sits here because decay accumulates across every stage at once.

[question to the room]

Of the four measures, one measures the outcome itself; the rest measure behavior and volume. Which one is which — and why is it easiest of all to substitute the other two for it?

[pause 15 seconds. Answer: the detection rate. It gets substituted by the withdrawal time of the scope — time is easier to track, and you can't will a finding past a fold through sheer effort.]

Form rests on three supports, and none of them asks the human anything: volume of practice, institutional accreditation, periodic recertification. In Russia: accreditation once every five years — 144 hours of coursework plus a portfolio, with the specialist writing their own report. There is no numerical threshold tied to outcomes.

A physician comes back after a year with no procedures — there was nothing on record to revoke their approval for. Their first procedure goes differently: the scope moves slower, the hand takes longer to find the angle, a fold gets passed right by. No complications, a protocol gets written up. And they don't even know it happened.

The model has taken over one action out of eight, and added one step of its own: whether to trust the overlay."

### [s73cb · 1.10 min] Case nineteen: developers on an unfamiliar library

[This slide stands first in the section, and that's its job: it sets the grade of evidence that the two clinical cases ahead will be read against.]

"Case nineteen. The subject being measured here is programming.

Fifty-two junior engineers, unfamiliar with the library, were randomized: half with an assistant, half by hand. By hand: 67 correct out of 100; with an assistant: 50. Effect size 0.738; no gain on time. Those who only asked about concepts scored above 65; those who handed off the whole task scored below 40.

[pause]

Remember what this was measured against: the no-assistant result comes from randomization. Neither of the two clinical cases ahead will be measured that rigorously.

The skill here was never established to begin with: nobody knew the library.

The same kind of decay happens without a model, too. In UK cytology, reading throughput fell by 80 to 85 out of 100, and the number of centers dropped from 45 to 8. Skill decays whenever volume gets handed off."

### [s73d–s73da · 1.80 min] Two classical modes of examination, and admission by country

"There are two classical modes here, both measured, and neither one free. Withdrawing the scope more slowly, nine minutes instead of six: procedures with a finding, 366 out of 1,000 against 271. Putting a second person, a nurse, at the screen as well: 457 against 393. The baselines are different, and the gains don't add up.

And now the line about admission to practice. The same detection rate sits at the base of it, and the consequence diverges. In the UK, it's used to admit people to screening work, with a threshold of 15 out of 100. In the US, the very same document that set a target level of 35 out of 100 forbids using its own benchmarks as a condition for admission. In Russia, there's no threshold at all."

### [s73f–s73g · 2.10 min] Cases twenty and twenty-one: the rate drops, and ArtInCol

"Case twenty: the first of two clinical cases, and the evidence here is weaker than what we just saw — observational, three-month windows, no replication, and the authors themselves make no claim of causation. At four centers in Poland, endoscopists were given an assistant that draws a box around a finding. Three months later, the same physicians' procedures without it were compared.

Before the assistant: 284 procedures with a finding out of 1,000 — 226 out of 795. After: 224 out of 1,000 — 145 out of 648. Minus sixty findings per thousand, in the same nineteen physicians, with an average of twenty-eight years of experience.

This is **skill decay**, the third of our six distortions, and it's the one named by its own name in this lecture. The publication doesn't name its own system.

Case twenty-one, domestic. ArtInCol: four institutions, Moscow and Ufa, 1,128 patients randomized. Procedures with a finding: 472 out of 1,000 against 413 — there is a gain, and it's measured stronger than the Polish one. The price: 1.23 false positives per study, where there used to be zero. That's how many times a physician looks at nothing at all. The largest rollout in the world by claimed numbers, and there's no measurement of the aftermath: nobody measured the physician after the assistant was taken away."

### [s73j–s73i · 1.50 min] Two modes of one class, and the section's takeaway

[`s73j` — two modes of one class; `s73i` — the stage's summary.]

"We've seen two modes of one class separately, and the difference between them isn't accuracy. A highlight on video: the physician drives the procedure, a box appears on the area, the place stays theirs — decay is measurable. A second reader for a scan: the model steps into the second person's spot, and the person gets removed from there entirely. Skill decays where the human formally stayed in place; where they were removed, decay can't be measured at all. No procedure, in any country, measures the physician without the assistant."

---

## Section 6. Takeaways (s96a … s102 · 4.80 min)

### [s96a–s97 · 1.55 min] All nine forms, in full

"The cases went by one at a time. Now they add up into a tally, and each takeaway answers its own question.

The nine forms of relocation we announced in the Opening — in full, with numbers attached. The load moved to a different step: note time, minus 9.5 percent against control. A step disappeared: no case came up. A step appeared: arbitration, 3.9 against 9.4 out of 100 readings. The load grew: 18 alarms per 100 admissions. The load shrank: reading down by 44.3 percent. The executor changed: attendance, 22 to 100 out of 100. The order of work changed: no count exists. The cost of error shifted: 26 out of 100 more disease. The executor got worse: findings, 284 to 224 out of 1,000.

Seven of the nine forms carry a count. Two dashes are named as dashes.

[question to the room]

Which of the nine, in your view, came up most often this evening — and which never came up at all?

[pause 15 seconds. Keep the answer ready: a step disappeared — no case came up; the order of work got rearranged, but as an order, it was never counted.]"

### [s98 · 0.90 min] The tally of misattribution

"And now the main number of the evening, and I'll ask you to remember it. Twenty-one detailed cases. In thirteen out of twenty-one, the credit or the blame doesn't actually belong to the trained model.

[pause 3 seconds]

The breakdown: two cases where there's no model in the mechanism at all; seven where the result comes down to the threshold, the dataset's composition, the stated goal, the order of presentation, or the implementation; four where the number grew in the retelling. Seven cases out of twenty-one are our own domestic practice.

A practice to take with you: for a claimed effect, ask what it was measured against; for anything retold secondhand, open the primary source."

### [s99 · 1.50 min] A map of task types and data types

"Now, a map, and we go through it once. Four rows of task type against three types of data — twelve cells. Four are named; across five sections, nobody went anywhere near the other eight.

Image classification works on a standardized scan, where fitness for reading gets decided before the model ever sees it; the subgroup scarce in the dataset pays for it. Recognition is good as a stream filter — deciding who gets read twice; it's no good as a basis for removing a reading altogether: the savings come straight out of what doesn't get read. Retrieval and generation on text: a draft exists by the end of the visit; human-level completeness doesn't. Forecasting on structured data: a signal next to the score exists; a decision doesn't — a variable sets the goal, and a document sets the threshold.

And outside this window, three more places exist: speech at the visit, video, and instrument signal, where there is no trained model at all, and yet bias is still present.

[lower your voice]

Look at the right-hand column: not one row in it is about the model's quality. All four are about fitness of the input, the composition of the data, the stated goal, and the assigned threshold."

### [s102 · 0.85 min] What was paid, and closing the thread

"The ledger is on the slide — I won't recite it. Four payments, named, each with a measurement under it, and they're paid unevenly: arbitration has two trials and the largest sample sizes behind it; attention has a subgroup of fourteen cases; skill has a single observation with no replication.

[lower your voice]

Now, the frame we started with. All six showed up. Five of them landed in four columns: anchoring and narrowing, under attention; decay, under skill; correction, under signature; disagreement, under arbitration. The alert stream got no column of its own. Only one was named by its own name this evening: skill decay. The other five went by unnamed."

---

## Section 7. Closing (s102_1 … s106 · 3.70 min)

### [s102_1 · 0.25 min] A pause: what the lecture measured

[Dark slide, one sentence filling the whole screen. Don't correct the on-screen sentence with your voice; hold the stop in silence.]

"What got measured was the human's work. What happened to the patient — that was not measured.

One rung got measured by screening: interval cancers, 1.55 against 1.76 per thousand. Not-worse, not better.

[pause 5 seconds]"

### [s103 · 1.60 min] Four rungs of participation, and three grounds for the signature

"Human participation is mandatory, and accuracy is not named among the grounds for it: it has been measured that the human is often not more accurate.

Four rungs. Reads first: reads on their own, the model is the second opinion, a mismatch goes to arbitration — randomized, 105,934 women. Reads second: attention narrows, a correct decision turns into an incorrect one. Reads only the disputed cases: 55 scans out of 100 that nobody reads. Signs without looking: in the seconds in which a hint cannot possibly be read.

All four showed up over one single woman, called in by a letter keyed to her year of birth: the screening, her mammogram, her lung scan, her discharge summary.

[pause]

There are three grounds. The right to sign: a case review evaluates the human's actions — the model isn't even a question there. It errs differently: across 106 trials, the sign of the pair's advantage depends on which side is stronger, and this ground has no magnitude attached to it at all. It can't be undone: an operation can't be undone after the fact, and a year of monitoring can't be replayed.

The standard is phrased as the ability to intervene. Presence alone doesn't satisfy it.

[lower your voice]

Not one of the four rungs has been measured all the way through to what the decision did to the patient."

### [s105 · 1.00 min] The device gets recalled; the decisions stay

"And one last thing. "In medicine, nothing is reversible" is a claim broader than what's actually been measured, and it's worth saying plainly: devices do get recalled — right there on the slide is the regulator's own record of it.

But the decisions made by that device over a year of its operation don't get recalled along with it. A procedure can't be redone, and a year of monitoring can't be replayed.

Thirteen cases out of twenty-one say the same thing from a different angle: it's the threshold, the dataset, the goal, and the order that decide — and people are the ones who set every one of those.

Ask your own system the same question: what in it gets recalled — and what stays.

[pause]

What it all came to for the woman with the letter — nobody measured that."

### [s106 · 0.85 min] Three checks, and a question

"Three checks, and we'll carry them with us into any field at all.

Is there an independent source of truth, other than the model's own explanation?

Has it been measured whether the human actually objects — and objects correctly? Two countable rates.

Does the human physically have enough time? The median time to check a hint is that same 1.99 seconds we heard on the axis of the evening; something accepted without a check gets corrected later 53 percent of the time, against 18 percent.

[final question to the room]

If you were putting a model into your own system tomorrow, what's the one check you'd make mandatory before switching it on?

[pause, collect answers; audience questions follow, 10 minutes]"

---

---

## Reserve for Q&A (10 min)

- **The question asked most often is about the 13 out of 21.** Keep the breakdown ready: 2 with no model, 7 down to the threshold and the dataset, 4 that grew in the retelling. The denominator itself is a judgment call, and the case registry says so itself: a different, equally reasonable way of carving it up would shift the number.
- **A measurement of anchoring that doesn't get said from the stage:** 23.6 correct conclusions out of 100, against 92.8, across two hundred twenty physicians. It only sits in the notes for `s01ad`; name it if someone asks about the size of the anchoring effect.
- **"So where are the successes?"** Two figures in the positive column: retinal-screening attendance, 22 → 100 out of 100, and ArtInCol findings, 413 → 472 out of 1,000. Both are named along with their own price.
- **The patient's side.** The deck has no stage dedicated to it, and that's a named gap. Five measurements of informed consent sit in the notes for `s01ad` — disclosure, isolation, asymmetry, cost, anonymity; they have different samples and different questions, and they cannot be added together.
- **Sections cut from the delivery** — prescribing and treatment, surgical care, drug development, oversight. They sit in the chapter; they don't run from the stage, because of the minute budget. Don't announce the cut order to the room.
- **Your own testimony** — if asked about personal experience, state explicitly: this is testimony, not a measured case.

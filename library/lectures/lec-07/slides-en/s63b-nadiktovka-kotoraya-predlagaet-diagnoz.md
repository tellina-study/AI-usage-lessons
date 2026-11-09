---
id: s63b
local_id: s5-10b
section: "4. Ведение медицинской документации"
type: norm
title: "Dictation that suggests a diagnosis: authorization and measurements"
assertion: "Системы, превращающие речь приёма в клиническое предложение, существуют за рубежом и не существуют в России; британский регулятор провёл границу медизделия по подписи — код под проверку врача остаётся документацией, диагноз под проверку ею быть перестаёт, — а независимых замеров точности самого предложения нет ни у одной из шестнадцати проверенных систем. Ближайшая отечественная публикует долю СОГЛАСИЯ врача с подсказкой, и это не точность"
source: "UK framework for ambient voice technology-enabled products, 29.07.2026 — https://www.gov.uk/government/publications/ambient-voice-technology-enabled-products/ambient-voice-technology-enabled-products · TOP-3 — https://sbermed.ai/our-algorithms/top-3"
media: ""
media_needed: "иллюстрация не нужна — кадр держат полоса плашек и граница по подписи"
media_note: "—"
blocks:
  - {label: "Foreign systems checked", value: "16", note: "authorizations to suggest from speech — zero; independent accuracy measurements — zero", key: true}
  - {label: "Domestic names with voice input checked", value: "13", note: "not one \"speech → suggestion\" system among them"}
  - {label: "Moscow TOP-3: physician agreement with the suggestion", value: "46% · 68%", note: "with one diagnosis offered and with a choice of three; it has no voice input"}
pol_slov: 140  # ПЕРЕОБЪЯВЛЕН ПО СОБРАННОМУ sec-3.pdf в круге #285 (раздел «Ведение документации»): вес 136 + запас 4. Прежнее значение ставилось до правок этого круга и к нынешнему кадру не относится. Канон: мера берётся с вывода, а не со входа (storozha-i-priyomka.md §11)
timing_min: 0.85
in_bucket: true
method_steps: ["упоминание", "названный пробел"]
form: []
vfy: true
status: собран
---

## Visible slide text

**The medical-device boundary is drawn at the signature.** Suggesting a **code** for the physician to check is documentation. Suggesting a **diagnosis** for the physician to check **is already a medical device**, even when the check is mandatory.

**Glass Health and Corti do this now** — they build out a presumptive diagnosis as live speech unfolds. *Neither has an accuracy measurement.*

**46% is physician agreement with the suggestion, not its accuracy.**

## Speaker notes

Systems that turn the visit's speech into a clinical suggestion — a recommendation or a diagnosis, not just a note — exist abroad; there are none in Russia, and nowhere in the world has the accuracy of the suggestion itself been independently measured. The UK regulator drew the medical-device boundary at the signature: a code for the physician to check remains documentation; a diagnosis for the physician to check is already a medical device.

First, about where such a system even sits. The six actions of the documentation stage that we have examined do not contain such a system at any point. Its input sits here, in documentation: it listens to the live visit. But its output sits at the diagnosis stage, that is, somewhere the lecture has already visited. This system sits between two stages at once. A tool that does not fit into the order of stages is an ordinary occurrence: a tool shows up later than the work has already taken shape, and the only honest reaction is to say which two stages it landed between.

Now the main thing, the reason this slide stands in a lecture about the signature. In July 2026 the UK regulator drew the medical-device boundary exactly at the spot this whole lecture is built around — at the signature. Transcribing the conversation, a retelling, a draft letter, suggesting a code for the physician to check — that is documentation, and it does not turn the product into a device. But suggesting a diagnosis or a treatment does, and it does so even when the suggestion goes out for mandatory physician review. Read that again: a physician's review does not soften the category. The regulator is saying that a diagnosis suggestion signed off by a physician is a device that has to be registered, with everything registration entails.

For an engineer, there is a transferable lesson here, and it is not about medicine. The line of responsibility runs not along the technology — the model is the same in both cases — but along exactly what the product puts under a person's signature. It is not the system's architecture that separates a code under signature from a diagnosis under signature, but the cost of error behind it. This is exactly what the lecture keeps repeating all evening: the model's class decides nothing; the procedure around the person does.

About a separate caveat that appears in no source, but has to be spoken aloud. The only domestic system close to the subject at hand is Moscow's TOP-3: it suggests three preliminary diagnoses and is registered as a medical device. Two things to note. First: the physician types the complaints into it by hand; it has no voice input, so it has nothing to do with the "by dictation" question. Second, and more important: its public figure — 46 percent with one diagnosis suggested and 68 percent with a choice of three — is the share of cases where the physician **agreed** with the suggestion. Agreement and accuracy are different quantities, and the difference here is not academic: if the physician and the model make the same mistake, agreement will be high and both will be wrong. The metric will not show this at all. There is no verified reference standard in the publications against which accuracy was computed; there is only the overlap of two opinions, one of which this very system also shaped.

And the count that stands as plates. Sixteen foreign systems were checked by name; fourteen of them claim to deliver more than a note — codes, orders, cues, a presumptive diagnosis. Not one has a regulator's authorization specifically to deliver a clinical suggestion from speech. Independent, peer-reviewed accuracy measurements of this suggestion: zero; what gets passed off as measurements measures something else — for one system, the trial counts billing codes as a consequence of a better note; for two others, time spent on the note, and that is the very trial on 238 physicians the section opened with. Thirteen domestic names with voice input were checked, and not one system of the "speech straight to clinical suggestion" class is among them: here, voice gives only text, and a diagnosis is suggested from the text of the chart that the physician typed in by hand. The two lines exist, and they are not connected.

What follows from this in practice. If you are shown a system that listens to the visit and delivers a presumption, the first question is not about accuracy, but about what it puts under a signature and whether it is registered for that. The second is what it was measured by: agreement with the physician, or accuracy against a verified diagnosis. The difference between these two questions is the difference between documentation and a medical device.

**Sources.** [UK framework for ambient voice technology-enabled products, 29 July 2026, sections 5.1–5.2](https://www.gov.uk/government/publications/ambient-voice-technology-enabled-products/ambient-voice-technology-enabled-products) · [TOP-3, manufacturer's page](https://sbermed.ai/our-algorithms/top-3) — the figures 46% and 68% were published in a statement by the Moscow City Government on July 14, 2021.

---
id: s37
local_id: "s37"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: analitika
title: "Breakdown: a voice for someone whose disease was taking it away"
grafa: "b — the classical mode is named, and has no number of its own"
assertion: "A person with amyotrophic lateral sclerosis is, by the classical route, required to record a large corpus of speech at the very moment speech is already deteriorating — and how many hours the clinical protocol requires is named by no source; this is said out loud. Synthesis is built on minutes of recordings that already exist, a professional license costs $1,200 a year and is given free to people with this diagnosis in the US, and what moved here is not the budget but the moment at which the decision has to be made"
source: "ElevenLabs Impact Program; Bridging Voice; Scott-Morgan Foundation"
chapter_ref: "chapter-part2.md §2.3"
media: "assets/screenshots/s37-peter-scott-morgan-portret.jpg"
media_note: "Peter Scott-Morgan, a scientist with amyotrophic lateral sclerosis; his foundation is one of two through which the speech-synthesis license is given away free. Wikimedia Commons, public domain, 539×424 — a small size, no other authentic images on this story could be found; provenance and the six tiers — images-log.md"
blocks_per_row: 3
blocks:
  - {label: "The price of both errors", value: "not in time — the voice is lost forever; recording too early — hours and strength spent in the worst period of a life", note: "after the moment of recording there is no going back; the second error has no money scale — that is a property of the case itself"}
  - {label: "Both classical modes", value: "no source has a number for either", note: "banking: no hours of protocol, no cost of care. A voice out of the box is cheap, but gives a different outcome — someone else's voice", key: true}
  - {label: "The model", value: "1–2 minutes of recording for a copy, 1–3 hours for fine-tuning", note: "license $1,200/year, free in the US with this diagnosis. What moved is not the budget but the moment of decision"}
itog:
  yarlyk: "What moved"
  text: "What moved is the moment of decision: who holds rights to a voice model after the person is settled by contract, not by law"
timing_min: 1.2
in_bucket: false
status: собран
---

## Visible slide text


## Speaker notes

This is the least disputable case in the whole lecture, and it is worth presenting exactly that way. In every other breakdown there is a side for whom the win came at a real cost; here there is no such side.

The case has no money scale, and that is a property of the case itself, not a gap in the measurement. The cost of the error "did not make it in time" is that a person loses their own voice forever: there is nowhere left to find enough recording to build a model from, past a certain point. The cost of the opposite error, "recorded too early," is hours spent on recording at a time when they were needed for something else, and the strength of a person who has little of it left to spend. This cannot be measured in dollars, and the frame says so directly.

The first classical mode is voice banking. A person with a diagnosis of amyotrophic lateral sclerosis, or motor neuron disease, records a large corpus of words and phrases while they can still speak clearly. The mode is named, it genuinely exists, clinics use it — and it has no number of its own. No source in our sample names either the hours of recording the protocol requires or the cost of the service. This is exactly what determines the completeness of the comparison: the second step of the form requires that both classical modes be counted in the same unit as the model, and here that condition is not met. One single number — how many hours the banking protocol requires — would have made the comparison complete; we looked for it and did not find it, and hiding that would be worse than saying so.

The second classical mode is a generic synthetic voice off the shelf. It exists, it is cheap, it has been available for a long time. It does not fold into the same unit, because it produces a different outcome: the person gets the ability to speak, but speaks in someone else's voice. The difference here does not run along price, and folding these two modes into one table would misrepresent what is actually being compared.

And separately — the circumstance that puts this breakdown on the border between two cases: for a person who has already lost speech, the first mode does not exist at all. Banking requires the ability to speak clearly, and by the time the diagnosis is made and absorbed, that ability is often already gone.

What the model gives. A copy is built from substantially fewer recordings than banking requires — this is the provider's own wording, and it does not give a number either, so the honest count here comes out one-sided, and it has to be presented as one-sided. What matters more is what can be checked: a professional license costs $1,200 a year, and it is given free to people with amyotrophic lateral sclerosis and motor neuron disease in the US under a program with two partner foundations. Alongside it, and free to everyone, is a personal-voice feature built into device accessibility settings, available since 2023.

The win here is earned honestly: the model works on material that is already recorded. For someone who has old videos, interviews, voice messages, work calls, the moment of decision shifts from "I need to record a corpus in time, while I can still speak" to "I need to gather what already exists."

How this works, the provider documents itself — a rare case in this section where the engineering is disclosed in full. Instant cloning: input is a recommended one to two minutes of audio, with a technical minimum of ten seconds total; the mechanism is described, word for word, as few-shot adaptation, in which the model uses the sample as a conditioning signal at the moment of inference, with no weight update at all. This is placement of knowledge, exactly the same kind as a document placed in a language model's context. Professional cloning: input is a minimum of one hour, ideally around three hours; training takes three to six hours and, in the provider's own wording, genuinely changes the model's parameters. This one is fine-tuning in the strict sense. The output in both cases is synthesized speech; singing is not supported, and the limitation is stated explicitly.

The barrier of entry and consent are set up stricter than is commonly assumed: a professional clone can only be made of one's own voice, and even with someone else's consent, someone else's voice cannot be cloned. The check is a voice captcha, and the provider itself states its limit: verification cannot guarantee that the recording belongs to the person requesting it — it confirms only that they were present and actively participated. A recognized limitation from the same source: a voice cloned from calm narration can sound different when asked to express a strong emotion — for someone planning to live with this voice for years, the caveat matters.

What is missing from the documentation: not a word about what happens to a voice model when the provider's underlying base model changes versions. The person ends up with a voice dependent on someone else's release cycle, and there is no public policy on voice versioning.

What moved. The moment of decision moved. Rights moved to the right: a voice model exists apart from the person and outlives them, and who controls it afterward is decided by a contract with the provider, because there is no norm on the matter. This is the same address as the next breakdown's, and the same as the case that closes the section.

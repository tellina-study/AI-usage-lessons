---
id: s34
local_id: "s34"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: live_demo
title: "One voice, two recordings. Which one is real?"
assertion: "Ten seconds of sound on the room's speakers — the original recording of a human voice and the synthesized copy of that same voice, back to back, with no captions and no answer on the frame: the main material of this frame sits outside the frame, and it is checked by ear, not by a table"
source: ""
chapter_ref: "chapter-part2.md §2.0, §2.2"
media: ""
media_needed: "a photograph has no place here by construction: the frame's material is sound on the speakers. The visual content — two identical-looking, unnamed audio tracks, labeled 'Recording A' and 'Recording B' — is built at assembly time. The six acquisition tiers were not applied: there is nothing to illustrate, since what is presented is not an image"
scheme:
  kind: dorozhki
  caption: "Both tracks are the same length and play back to back, with no caption and no pause between them"
  entry: "one and the same person"
  exit: "the answer — a raised hand"
  rows:
    - {label: "Recording A", steps: ["ten seconds of speech"]}
    - {label: "Recording B", steps: ["ten seconds of speech"]}
blocks:
  - {label: "There is no answer on the frame", value: "the room answers", note: "a raised hand for A or for B", key: true}
timing_min: 0.7
in_bucket: false
status: собран
---

## Visible slide text

**Two recordings of the same voice are about to play, back to back. One was recorded by a human, the other was built by a model.**

## Speaker notes

This frame exists for the sake of ten seconds of sound, and everything else on it is secondary. The two tracks are deliberately unlabeled, the order is deliberately not announced, and the answer is deliberately not shown: the moment a hint appears on screen, the check stops being a check.

What is worth knowing about the material that plays. A modern voice-cloning system builds a usable copy from one to two minutes of recording; the technical minimum stated by the provider drops to ten seconds of total audio. This parameter has been measured in the open literature. VALL-E, the system that reformulated speech synthesis as language modeling over discrete codes, published how recognizability depends on the length of the sample: a three-second prompt gives a voice similarity of 0.382, five seconds gives 0.423, ten seconds gives 0.484. The headline "cloning from three seconds," which is usually the figure quoted, is true and at the same time half the picture: three seconds works, ten works noticeably better, and the gap between them is visible in the measurement.

A second number explains why the copy sounds smooth. The intelligibility of synthesized speech — the share of words recognized incorrectly — is stated for Voicebox as 1.9 percent against 5.9 percent for the previous generation on the same test set. In other words, the error rate dropped threefold in one generation. The split of roles inside the system has been measured separately: without a text prompt, the word error rate is 19.6 percent; with it, 3.0 percent — meaning content comes from the text. Without an acoustic prompt, voice similarity drops from 0.585 to 0.236 — meaning identity comes from the sample. Two independent knobs, and each is responsible for its own part.

The mechanism by which the instant copy is built is worth naming precisely, because it carries over to everything else in the course. The provider describes it, word for word, as few-shot adaptation: the model uses the sample as a conditioning signal at the moment of inference, with no weight update at all. This is placement of knowledge, exactly the same kind as a document placed in a language model's context. Professional cloning is built differently: the input is a minimum of one hour, ideally around three hours of recording; training takes three to six hours and, in the provider's own wording, genuinely changes the model's parameters. Two different things hide under the one word "cloning," and confusing them is costly: which one is used determines both the quality and where, physically, the person's data ends up sitting.

What the copy cannot do is harder to hear than what it can, which is why it will not show up in the ten-second demonstration. A voice captured from calm narration sounds different when asked to express a strong emotion: the sample contained no strong emotion, and the system cannot derive one from the text. Professional cloning does not support singing at all — the limitation is stated by the provider in its own documentation. Both boundaries are examined further on in the section, and both follow from the design, not from a shortcoming of a particular version.

Finally, about the barrier to entry. A speech model with 82 million parameters, openly licensed for both code and weights, runs even in a browser; training it cost around a thousand dollars. A music model with 3.5 billion parameters fits in eight gigabytes of video memory and, on a gaming card, runs 34.5 times faster than real time — a minute of music in 1.74 seconds. On an Apple laptop, the same model gives 2.27 times real time. What is playing on the speakers requires neither a cloud nor a budget: it requires a laptop and ten seconds of someone else's voice. The rest of the section grows out of this — both the possibilities and the cost.

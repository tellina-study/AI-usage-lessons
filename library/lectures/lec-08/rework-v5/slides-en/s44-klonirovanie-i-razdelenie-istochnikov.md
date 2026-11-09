---
id: s44
local_id: "s44"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: assertion_visual
title: "Voice cloning and source separation are different tools"
assertion: "In source separation, what is sought is physically present in the input signal, there is a ground truth and an honest metric — a signal-to-distortion ratio, whose denominator is deviation from a known correct answer; generation has no ground truth by definition, and no metric of this kind can exist for it; that is why the song 'Now and Then' was made by separation, and not one of its notes was generated — the choice of tool decides what comes out at the end"
source: "Spleeter; Demucs; BS-RoFormer; WingNut Films, 2021"
chapter_ref: "chapter-part2b.md §2.6, §2.7"
media: ""
media_needed: "the visual content is a quality scale with the masking methods' upper bound marked on it; there is no genuine photograph of this subject, and a musician's portrait would tie the frame to a case instead of the distinction the frame exists for"
scheme:
  kind: shkala
  unit: "dB, signal-to-distortion on the vocal"
  base: "the ideal mask — the masking ceiling; Hybrid Demucs was the first to clear it, at 8.34 dB"
  caption: "The oracle is computed knowing the true tracks"
  marks:
    - {value: "5.91", label: "Spleeter"}
    - {value: "8.22", label: "Ideal mask", key: true}
    - {value: "9.20", label: "Sparse HT Demucs"}
    - {value: "11.99", label: "BS-RoFormer, 2023"}
columns:
  left:
    head: "Source separation"
    items:
      - "The mix is a sum of tracks, the task is to return the addends"
      - "A ground truth exists: the original isolated tracks"
      - "The model minimizes error against the ground truth"
      - "The oracle is the upper bound when the answer is known"
      - "\"Now and Then\": 1978–2023, failed in 1995 — 45 years"
  right:
    head: "Generation"
    items:
      - "No ground truth: there is no 'correct' song"
      - "There is nothing to compare the result against — no metric"
      - "Generation has no ideal oracle at all"
      - "What was recorded is retrieved; inventing is the wrong tool"
timing_min: 0.9
in_bucket: false
status: собран
---

## Visible slide text

**The boundary between restoration and invention runs along whether an oracle exists.**

## Speaker notes

This distinction is load-bearing for the whole course, and it has to be placed next to voice cloning, because the press calls both things by the same word.

John Lennon's 1978 demo existed on a home cassette, where the voice was physically mixed together with piano, television noise, and mains hum. An attempt to mix the song down was made in 1995 and failed: there was no way to separate the voice from the piano. In 2021, while working on a documentary series, a studio built a machine source-separation system, and in November 2023 the song came out — forty-five years after the demo was recorded.

The difference from generation sits in how the task is framed. In source separation, the mix is treated as a sum of tracks, and the task is to return the addends; the model is trained to minimize reconstruction error against an isolated track that exists as a ground truth. Generation has no ground truth by definition: there is no correct song for the prompt "a funky bass line," and there is nothing to compare the result against. Separation's metric — the signal-to-distortion ratio — literally has, in its denominator, the deviation from a known correct answer, and no metric of this kind can exist for generation.

The clearest proof of this is the oracle. The upper bound on quality for every method that works by masking a spectrogram is computed from the true tracks — that is, with the answer known — and it comes to 8.22 decibels. For a generative model, the notion of an ideal oracle does not exist at all: there is nothing to substitute for the answer.

The scale looks like this. Ideal mask — 8.22 decibels. Spleeter, the mass-market tool of the previous generation — 5.91. Hybrid Demucs — 8.34. Fine-tuned Sparse HT Demucs — 9.20. 2023-generation systems in the RoFormer class — up to 11.99. The story that follows from this: waveform and hybrid models have surpassed the mask oracle. This happened not because they became generative, but because they stopped being bound to one specific discriminative operation — multiplying a spectrogram by a real-valued mask. The current frontier still estimates masks, just complex-valued ones.

An honest caveat, so the claim does not land as dogma: there is a class of work on source restoration where generation does come back into separation. There the task is broader — to recover the original unprocessed tracks from a mixed-down and mastered recording, where production effects break the assumption of a linear sum. Once linearity is broken, pure discrimination is no longer enough, and you have to fill in something that is no longer present in the signal. The boundary, then, runs along the framing of the task; the technology on either side of it can turn out to be the same, and an engineer has to be able to tell which side their own case falls on.

How to check this on your own task. There is one question: does a correct answer exist for your input that could, in principle, be produced and shown? If yes, the task is restorative, and it has to be measured by distance to that answer — a generative model here will invent something plausible instead of something correct. If no, the task is generative, and demanding a precision metric from it makes no sense — you have to measure fitness for the client's purpose instead. The most expensive error in this pair is applying a generator where an answer actually existed: you get a plausible result that cannot be disproven by ear and that, at the same time, recovers none of what was recorded.

This same pair comes back later in the lecture, on different material: an ancient scroll read for the first time in two thousand years, and a film screening where more than ninety percent of the frame has been touched by a model. There, the boundary between restoration and invention runs along the same line, and it has to be set with the same question.

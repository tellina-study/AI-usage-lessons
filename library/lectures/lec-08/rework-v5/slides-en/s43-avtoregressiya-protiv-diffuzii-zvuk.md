---
id: s43
local_id: "s43"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: analitika
title: "Autoregression versus diffusion: a measured frame"
assertion: "Sound is the only modality where both families of generative model work side by side on the same task, and they can be compared by a measurement from a single paper: for autoregression, generation time grows linearly with length, from 6 minutes 38 seconds to 12 minutes 53 seconds on a doubling; for diffusion it holds at 13 seconds regardless of length, because the number of solver steps is fixed and does not depend on output size — and diffusion's quality on the same metric is more than twice as good"
source: "a comparative benchmark of Stable Audio 2 and MusicGen-large-stereo"
chapter_ref: "chapter-part2b.md §2.7"
media: ""
media_needed: "the visual content is two pairs of measurements in one table and two timelines; there is no photograph for this subject"
scheme:
  kind: dorozhki
  entry: "a minute of sound"
  rows:
    - {label: "Autoregression", steps: ["two minutes — 6 min 38 s", "4 min 45 s — 12 min 53 s", "grows linearly: every token, its own pass", "quality 204.03 and 218.02"]}
    - {label: "Diffusion", steps: ["two minutes — 13 s", "4 min 45 s — 13 s", "does not grow: a fixed number of solver steps", "quality 79.09 and 81.96"]}
columns:
  left:
    head: "Autoregression: its own task, one text does not have"
    items:
      - "Quantization: several streams, a transformer — just one"
      - "Flattened unrolling: 6,000 steps, quality 0.86"
      - "The delay pattern: s, s−1, s−2 — 1,500 steps, 0.96"
      - "A naive all-at-once approach: 1,500 steps, worse to the ear — 2.58"
  right:
    head: "Diffusion: its own task, one text does not have"
    items:
      - "A fixed-shape tensor — one single duration"
      - "Time as conditioning: the source's start and length"
      - "A 95 s window; the tail past the needed length is silence"
      - "The tail is trimmed; the 'set before launch' limit remains"
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

**The gap is structural: it follows from the design of both families, and the quality of the engineering work has nothing to do with it.**

## Speaker notes

Sound is the only modality where both breeds of generative model work side by side on the exact same task, and they can be compared by measurement rather than by argument. The table these numbers come from was published in a single paper, meaning both columns were produced by one methodology; comparing measurements from different papers would be exactly the kind of baseline-swap the course catches in every lecture.

Look at the time column, and at both rows for each model. For the autoregressive system, time grows linearly with length: two minutes of music takes 6 minutes 38 seconds to generate, four minutes forty-five seconds takes 12 minutes 53 seconds. For the diffusion system it stays put: 13 seconds either way. The reason is in the design. Autoregression makes one pass per generated token, so a twice-as-long output requires twice as many passes. Diffusion makes a fixed number of solver steps regardless of output size: lengthen the output, and the number of steps stays the same — each step just processes a larger tensor, and at these scales the growth is barely visible.

The sixty-fold gap here is structural: it follows from the design, and engineering quality has nothing to do with it. And the result is also more than twice as good for diffusion on the same metric: 79.09 and 81.96 against 204.03 and 218.02, where lower is better.

This is exactly the distinction the course introduced on language models: autoregression makes as many passes as there are tokens, diffusion makes a fixed number of passes regardless of output size. Here it is confirmed by a measurement in one paper's table, not by analogy.

Autoregression over audio tokens has its own task that text does not have, and its solution is instructive. Residual quantization gives several parallel token streams per frame, and an autoregressive transformer can only generate one stream. The naive solution — predicting all four codebooks at once — fails, because the codebooks are conditionally dependent: each encodes the residual of the one before, and predicting them independently loses that connection. This has been measured directly: with a flattened unrolling, where all codebooks are stretched into one long chain, you get 6,000 steps and a quality of 0.86 by the FAD metric; with a delay pattern, where step number s predicts the first codebook of frame s, the second codebook of frame s minus one, the third of frame s minus two, you get only 1,500 steps at a quality of 0.96; with a naive parallel variant you get the same 1,500 steps, but a quality of 2.58 and a noticeable drop in subjective rating. The authors' conclusion: comparable quality can be reached at a fraction of this cost with a simple delay-based approach.

Diffusion has its own problem, and its solution is also worth knowing. A diffusion model generates a fixed-shape tensor, meaning it outputs exactly one duration by construction. This is worked around by conditioning on time: when a training fragment is taken, the second it starts at and the total length of the source file are recorded, both numbers are turned into learned embeddings, and fed in alongside the text. In production, the user sets the length, and the model, always producing a 95-second window, is trained to fill the tail with silence from the specified point on; the silence is then trimmed. The mechanism is worth remembering: variable length is obtained here through training, and the underlying limitation — "size is set before launch" — has not gone anywhere; what it costs in practice is examined in a separate frame of this same section.

The engineering conclusion carries beyond sound. The choice between the two families is made by the task's profile. A long output with a hard time budget — diffusion: its cost does not depend on length. An output that needs to be grown as you go, with the ability to continue what has already been started — autoregression: it has a natural continuation of the sequence that diffusion does not. The question "is diffusion better than autoregression" has no meaning: the two classes guarantee different things and are counted differently, and what you should ask is which guarantee your task actually needs.

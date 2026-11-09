---
id: s41a
local_id: "s41a"
section: "2. Sound: Speech Synthesis, Performer Voice, and Music"
type: schema_pipeline
title: "The path from request to result: from text to sound"
assertion: "Text (and an acoustic sample, if there is one) enters as the shared prefix of one sequence of codec tokens: the first codebook is predicted by autoregression, codebooks two through eight are filled in by a non-autoregressive network, called seven times over the whole frame at once, and the codec's decoder assembles the waveform; the text stays as a condition across all these passes, just as with images, and the bottleneck is not the generator but the codec's own frame rate and cascade depth, because a generative model can never be better than its own decoder"
source: "VALL-E (Wang et al., 2023) · SoundStream · EnCodec"
chapter_ref: "chapter-part2b.md §2.7"
media: ""
media_needed: "the visual content is the diagram of the two tracks itself and a band of four numbers; there is no genuine photograph of the sound-generation process. The six tiers were not applied: the subject of the frame is a mechanism of operation, not a case"
scheme:
  kind: dorozhki
  entry: "request"
  exit: "result: sound"
  steps_arrows: true
  rows:
    - {label: "A plain request", steps: ["text — a condition, permanently", "codebook 1: autoregression", "codebooks 2–8: 7 passes", "decoder → waveform"]}
    - {label: "A request with a sample", steps: ["text + the sample's prefix", "codebook 1: timbre is in the prefix", "codebooks 2–8: the same 7 passes", "decoder → waveform, with the timbre"]}
blocks_per_row: 2
blocks:
  - {label: "Repeats, and how the request participates", value: "7 passes over the whole frame", note: "from the depth of the codec's cascade (8 codebooks), not from the generator's size; the text is a condition on every pass, not just at the start"}
  - {label: "What changes, the bottleneck", value: "codebook 1 — solved once; codebooks 2–8 — refine it", note: "the bottleneck is the codec's own frame rate and cascade depth: a generator is never better than its own decoder", key: true}
timing_min: 0.8
in_bucket: false
status: собран
---

## Visible slide text

**Text holds as a condition across all passes. Codebook 1 is solved once — codebooks 2–8 refine it over seven passes in a row.**

## Speaker notes

This is "from request to result" for sound: the previous frame (`s41`) showed the codec's design — what parts it is built from; here it is what actually happens to the request before it becomes a waveform.

The mechanism is described in the open literature, word for word. VALL-E reformulated speech synthesis as language modeling over discrete codes: the text's phonemes become the condition, and speech becomes a matrix of codec tokens (ten seconds of sound, with an EnCodec tokenizer at 75 Hz and eight quantization levels, is a 750×8 matrix). The autoregressive stage predicts only the first codebook — one frame per pass, like an ordinary language model. A non-autoregressive stage fills in codebooks two through eight: it is called seven times, and each time it revises the entire frame at once, not a single token — exactly the same principle of "the whole object in one pass, many times over" the course has already seen in image denoising, except here the number of repeats is not twenty to fifty but seven, and they are counted not as solver steps but as codebook levels.

Text participates not once at the start but on each of these eight passes: it sits in the sequence's shared prefix, and the model's attention counts back to it at every step of generation — the same design the course has already seen in image denoising (where the text is the Key and Value of cross-attention at each of the 20–50 denoising passes), except here the context grows token by token, as in an ordinary language model, rather than being held as a constant condition over a fixed latent.

The track with a sample differs not in mechanism but in the length of the input. An acoustic voice sample is encoded by the same codec and becomes a prefix of the same sequence — the model has already been told what to keep speaking in, and in what timbre; ablations show a clean split of roles: without the acoustic prompt, voice similarity drops from 0.585 to 0.236; without the text prompt, the word error rate rises from 3.0 to 19.6 percent. Content comes from the text, identity comes from the sample, and these are two different inputs into one and the same prefix, not two different mechanisms.

The bottleneck here is not the generator but the codec itself — exactly what the neighboring frame on frame rate examines. The lower a tokenizer's frame rate, the longer the possible output for the same generator context window; but a generative model can never be better than its own decoder: the 32-kilohertz codec inside one well-known music model is the worst in the comparative reconstruction table — a distance of 1.82 against 0.96 for another codec and 1.19 for a third system. At a bitrate of 2.2 kilobits per second, no transformer stacked on top will recover what the decoder has already lost. The murky upper-mid range by which machine-made music is recognized by ear most often belongs to the codec, not the generator — the audio tokenizer is tiny, the generator sitting on top of it is expensive, but it is the tokenizer that sets the ceiling on quality.

---
id: s19
section: "1. Still Image"
type: analitika
title: "A 1024×1024 Picture Is 4096 Tokens"
assertion: "The autoencoder works here as a tokenizer: it fixes the units the model sees the picture in, is trained separately and earlier, and the diffusion network will never step past its ceiling"
source: "Rombach et al., 2021 — the paper Stable Diffusion grew out of · the SD3 technical report, 2024 (the reconstruction-quality table)"
scheme_zakaz: "C4 and C5 — research/R2-part9-shemy.md"
refrain: "the main lever is the tokenizer; model size is secondary here. First utterance of three (s19 · s42 · s91; s62 removed 29.10.2026, content is in s59a's notes)"
scheme:
  caption: "Three compression stages: area is honestly proportional to the number of values"
  arrows: true
  rows:
    - steps:
        - "pixels: 1024 · 1024 · 3 = 3,145,728 numbers"
        - "latent, 16 channels: 128 · 128 · 16 = 262,144 numbers"
        - "transformer input, 2×2 patch: 64 · 64 = 4,096 tokens"
blocks:
  - {label: "What the autoencoder lost, measured", value: "25.12 dB on 4 channels against 28.62 dB on 16", note: "perceptual divergence 0.85 against 0.45; this is the ceiling the diffusion network physically can't step past"}
  - {label: "A direct comparison of units", value: "there, a token from a vocabulary of ~200k, fixed before training — here, a continuous vector, no vocabulary at all", note: "hence: there's nothing to mask, nothing to forbid", key: true}
  - {label: "What this delivered in practice", value: "65,536 numbers instead of 786,432 on every step", note: "one and a half orders of magnitude of compute, on each of dozens of steps — hence 512×512 on a 6–8 GB card in August 2022"}
media: ""
timing_min: 0.7
in_bucket: false
status: собран
---

## Visible slide text

**Quadratic cost hasn't gone anywhere.** 4,096 tokens — ≈16.8 million pairs per head per layer, 16,384 tokens — ≈268 million: doubling the picture's side increases attention's cost sixteen times.

**The main lever is the tokenizer; model size is secondary here.**

## Speaker notes

Before 2021, denoising was done directly on image pixels. For 512×512 this means a network that,
on each of a thousand steps, processes seven hundred eighty-six thousand numbers; hence both the
cost, and the fact that models of this class lived only with their own authors.

The observation this whole line grew out of: most of the bits in an image are perceptually
insignificant high-frequency detail, and denoising spends the bulk of its compute on exactly
that, even though the meaning of the picture lives in a far smaller number of dimensions. So it
makes sense to split the pipeline into two independently trainable pieces. The first — an
autoencoder that learns to map the picture to a compact representation and back; trained once,
separately. The second — a diffusion network that works entirely inside that representation; it
knows nothing whatsoever about the image's pixels.

This is the same decoupling as between a tokenizer and a model: the vocabulary is built once,
before the model is trained. The autoencoder plays the role of the tokenizer here — it fixes the
units the model sees the picture in, and it's trained separately and earlier. The consequence is
exactly the one the course already drew from strange tokens: the pipeline is built from
independent parts, and strange behavior at the seam is a systemic property, not a break in your
own integration. And from this comes a practical consequence: the diffusion network can't be
better than its autoencoder. The autoencoder sets a ceiling the network physically can't step
past.

The compression arithmetic is counted right on the slide. The original 1024×1024 picture in
three channels is three million one hundred forty-five thousand seven hundred twenty-eight
numbers. The spatial compression factor is eight: each side is divided by eight. With sixteen
channels, the latent is two hundred sixty-two thousand one hundred forty-four numbers, a
twelvefold compression. Next, the latent is cut into two-by-two patches, and each patch becomes
one transformer token: sixty-four by sixty-four gives four thousand ninety-six tokens, with a
dimensionality of sixty-four numbers each, before projection.

And here's the number the whole block rests on: a 1024×1024 picture is 4096 tokens. Exactly the
kind of tokens the every-against-every attention map is computed over. Plus the conditioning text
tokens: from seventy-seven to five hundred twelve depending on the generation.

Quadratic cost hasn't gone anywhere. The course formulated this as "doubling the context
quadruples the volume of attention compute"; here the same thing looks like this: four thousand
tokens give around sixteen point eight million pairs per head per layer, sixteen thousand tokens
give around two hundred sixty-eight million, that is, sixteen times more. Doubling the picture's
side quadruples the number of tokens and increases attention's cost sixteenfold. This is the
engineering answer to the question of why generating at quadruple resolution costs noticeably
more than four times as much.

What this delivered in practice can be counted outright: on every step the network processes
sixty-five thousand numbers instead of seven hundred eighty-six thousand — one and a half orders
of magnitude of compute, and on each of dozens of steps. This is also why the first version of
Stable Diffusion generates 512×512 on a consumer GPU with six to eight gigabytes of video memory,
and that happened in August 2022. It was this, not quality on its own, that launched the
grassroots ecosystem: local interfaces, thousands of community adapters, one-person "on my own
data" fine-tuning.

The ceiling the autoencoder sets is measured, and the numbers are worth knowing. At eightfold
spatial compression, reconstruction quality comes to twenty-five point twelve decibels on the
four-channel latent and twenty-eight point sixty-two on the sixteen-channel one; perceptual
divergence is zero point eighty-five against zero point forty-five. Read this as follows: even
if the diffusion network performs perfectly, the output picture still passes through a decoder
that, on four channels, gives twenty-five decibels — a loss visible to the eye.

And the loss is distributed unevenly — it's exactly what compresses poorly that suffers. Letters
are a high-frequency structure where every line matters; forty-eightfold compression blurs them,
hence the famous pseudo-letters of early models. Small faces in a frame with many people: at this
level of compression, a face in the background occupies a handful of cells. Regular small
textures — grids, lattices, striped fabric — produce the characteristic "boiling." Thin, long
structures — wires, spokes, strings — tear apart during decoding.

The boundary of the parallel with the tokenizer has to be named, or the audience will fill it in
wrong. A language model's tokenizer outputs a discrete identifier from a finite, enumerable
vocabulary, and decoding returns the exact original text. An autoencoder outputs a continuous
vector, its reversibility is lossy, and there's no vocabulary at all — nothing to mask. The line
about reversibility is load-bearing here: a picture that's passed through an autoencoder and back
is no longer identical to the original — and it's not identical even before any generative model
has touched it. This is worth checking by hand: run a photograph through encoding and decoding
with no generation at all, and look at the difference. A five-minute experiment that explains
half the artifacts you've seen in these tools.

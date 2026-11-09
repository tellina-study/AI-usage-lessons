---
id: s17
section: "1. Still Image"
type: schema_pipeline
title: "The path from request to result: denoising the latent"
assertion: "The request becomes the result over 20–50 identical passes of the same network: the text encoder holds the condition frozen on every pass, the 128×128 latent turns from pure noise — or from a partially noised original picture, the second track — into a clean image, the autoencoder unfolds the latent into pixels; the bottleneck is the number of passes itself, not the model's size, and distillation down to 4 passes delivers the same work 25 times faster"
source: "Ho, Jain, Abbeel, «Denoising Diffusion Probabilistic Models», 2020 · Rombach et al., 2021 · Ho and Salimans, «Classifier-Free Diffusion Guidance», 2022 · Karras et al., 2022 · Sadat et al., 2024"
chapter_ref: "chapter-part1c.md §1.9.1, §1.9.9"
media: ""
media_needed: "the visual content is the two-track diagram itself and a band of four numbers; there's no authentic photograph of a denoising process. The six acquisition tiers weren't applied: the slide's subject is how the mechanism works, not a case"
scheme:
  kind: dorozhki
  entry: "request"
  exit: "result"
  steps_arrows: true
  rows:
    - {label: "Pure request", steps: ["text — condition forever", "latent 128×128, pure noise", "denoising ×20–50", "to pixels"]}
    - {label: "Request with a reference", steps: ["text — condition forever", "image latent, partial noise", "denoising, fewer steps", "to pixels"]}
blocks_per_row: 2
blocks:
  - {label: "Repeats and the request's role", value: "20–50 passes", note: "set by the sampler, not the network size; the text is the condition on every one of them, not just the first; it was 1000 in 2020"}
  - {label: "What changes, the bottleneck", value: "the latent — every time; the condition — never", note: "the bottleneck is the number of passes itself: distillation down to 4 delivers the same work 25 times faster", key: true}
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

**The request goes in once and stays as a condition on each of the 20–50 passes — it's not the request that changes, it's the latent.**

## Speaker notes

This is the very "from request to result" that the section hasn't shown directly until now: the architecture diagram (`s16`) explained what parts the generator is built from, while here it's exactly what happens to the request before it becomes a picture.

The pure track. The text encoder (frozen, not trained at this step) turns the description into a set of vectors once, and from then on these vectors act as the Key and Value of cross-attention on each of the 20–50 denoising passes — exactly the same Q/K/V architecture the course introduced on language models, except here the Query comes from the image latent, not from text. The starting point is a 128×128 latent (with sixteen or four channels, depending on the autoencoder's generation), filled with pure Gaussian noise. The network predicts (depending on the parameterization) the noise, the original picture, or the velocity, and from this prediction the latent is nudged a little toward a clean image. The step repeats 20–50 times — the number is set by the sampler, not by the architecture or the network size: in 2020, an honest Markov chain required 1000 such passes; higher-order numerical methods brought this down to 20–50 with no loss of quality, and distillation (a student learns to reproduce in one pass what a teacher does in two, and this way 1000 comes down to 4) — down to 1–4. The last pass hands the latent to the autoencoder, which unfolds it into pixels.

The reference track differs in exactly one point — the start. Instead of pure noise, the latent is taken from the original picture, encoded by the same autoencoder, and noised not all the way but to level t on the noise schedule; the parameter that interfaces call "strength" is exactly the choice of which step of the schedule to start from. The less noise at the start, the fewer steps it takes to reach a clean image, and the closer the result stays to the original picture. The condition (the text) and the mechanics of each pass don't change; what changes is only the point on the latent trajectory the run started from. The same technique applies to a mask: noise is mixed in only inside the selected area, while outside it the latent reverts to the original, unchanged, at every step.

What the bottleneck costs. Each of the 20–50 passes is one full pass of the whole network over the latent, and with classifier-free guidance (CFG) switched on, that's two passes per step, not one: 50 steps give 100 network passes. An undistilled 1024×1024 model takes ≈20 seconds on a top-tier gaming card for this; a distilled relative of the same size — 4 steps, with the guidance already baked into the weights, 4 passes, ≈3 seconds. The difference is 25 times at exactly the same network size: it's the number of passes that decides it, not the model's weight. The price of distillation isn't free savings: the student converges on the teacher's averaged, good answer, and ten generations from one description with different starting noise come out more similar to each other than they would with an undistilled model. For a product pipeline that needs one decent frame a second, the trade is worth it; for creative exploration of variants, it's a loss of exactly the diversity the exploration was undertaken for.

And the boundary of the parallel with the language model, which is worth keeping next to this diagram. A language model's output is a probability distribution over a vocabulary: discrete, normalized, hence logits and temperature. Here, the output of every pass is a vector of the same dimensionality as the latent: continuous, unnormalized, with no probability. That's why an image generator has no measure of confidence in its own output and can't have one — whereas the text condition, unlike the latent, does have a measure of confidence, because it was predicted by a different model, not this one.

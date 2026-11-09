---
id: s60
local_id: "s60"
section: "3. Moving Image"
type: schema_architecture
title: "The Causal 3D Autoencoder"
assertion: "Compression runs over both space and time: moving from a 2D autoencoder to a 3D one lowers the flicker metric from 93.2 to 86.3; causality in time is implemented literally — all the convolution's padding is placed at the start, so that the future cannot affect the present and the past, and it's the same trick as a causal attention mask in a language model; the first frame is encoded on its own, which is where the formula 'latent frames equal frames divided by the factor, plus one' comes from, and the odd-looking frame counts in video-model interfaces — 49, 81, 121, 129, 257"
source: "CogVideoX; HunyuanVideo; Wan 2.1; Movie Gen; LTX-Video"
chapter_ref: "chapter-part2d.md §3.7"
media: ""
media_needed: "visual content — a diagram of causal convolution over time and a table of real compression ratios; there is no photograph for this subject"
arhitektura:
  blocks:
    - head: "Input: video frames"
      role: "input"
      lines:
        - "the first frame is encoded on its own"
        - "the rest are compressed over time"
    - head: "Causal convolution"
      role: "the work · bottleneck"
      uzkoe: true
      lines:
        - "padding at the start — the future doesn't affect the past"
        - "the same trick as an attention mask"
    - head: "Latent"
      role: "output"
      lines:
        - "frames = the rest ÷ factor + 1"
        - "'4/8 plus one': 49, 81, 121, 129, 257"
  vynoska:
    at: 1
    text: "flicker 93.2 → 86.3 when moving to a 3D autoencoder; at 16×16×8, 'convergence becomes extremely difficult'"
blocks_per_row: 2
blocks:
  - {label: "More channels", value: "from three to sixteen, up to 128 at the most aggressively compressing one", note: "compensates for the strength of compression", key: true}
  - {label: "Compression ratios", value: "4×8×8 at three models · 8×8×8 · 8×32×32", note: "time × height × width; the last one has no patch step at all"}
timing_min: 0.7
in_bucket: false
status: собран
---

## Visible slide text


## Speaker notes

A 3D autoencoder differs from an image-only one in three ways, and each is measured, not merely asserted.

First: the convolutions are three-dimensional, and compression runs over both space and time. The authors of one of the open models put it this way: the autoencoder compresses video along both the spatial and the temporal dimensions, and this strategy significantly shortens the sequence length and helps prevent flicker. The effect is counted in an ablation: moving from a 2D autoencoder to a 3D one lowers the flicker metric from 93.2 to 86.3. This is a measurement: remove one component, and the number gets worse.

Second: causality in time — literally. The authors write that they use a temporally causal convolution, which places all the padding at the start of the convolutional space, and this guarantees that future information does not affect present and past predictions. It's the same trick as a causal attention mask in a language model, just implemented in a convolution through asymmetric padding. The parallel here is exact: the same principle — "don't peek ahead" — in two layers built very differently.

A side effect — a small detail a student will check for themselves. The first frame is encoded on its own, spatially only, which is where the formula comes from: the number of latent frames equals the frame count divided by the factor, plus one. That's why video-model interfaces have odd-looking frame counts — 49, 81, 121, 129, 257 — all of the form "a multiple of four plus one" or "a multiple of eight plus one." When you see "129 frames," you now know why it isn't 128.

Third: more channels — from three up to sixteen, and up to 128 at the most aggressively compressing model, to compensate for the strength of compression. The logic here is simple: the harder we compress over space and time, the more information each remaining element has to carry, or the decoder won't be able to reconstruct what was there.

Where the limit of compression sits — measured. In the same ablation, the authors pushed to a compression ratio of sixteen by sixteen by eight and recorded the result: when spatiotemporal compression is too aggressive, even with a corresponding increase in channel count, model convergence becomes extremely difficult. There is no such thing as free compression, and here it's recorded as one row in a table, with no hand-waving.

What "causal" means for editing in practice. Temporal causality means the first frames of a clip are encoded without any regard for what follows, and two things follow from that. First: a clip can be encoded as a stream, without waiting for its end — meaning real-time operation and extending an existing fragment are both possible. Second: the first frame exists as a standalone unit, which is exactly why conditioning on the first frame works so well and so cheaply — it doesn't have to be pulled out of a shared compressed slice. From this comes a practical tip: if you need predictability, start with a frame and leave the description for the second step.

It's worth separately explaining why flicker shows up at all and why it's exactly temporal compression that cures it. If every frame is encoded and reconstructed independently, small reconstruction inaccuracies in neighboring frames turn out different: the same patch of background in two consecutive frames reconstructs slightly differently each time, and the eye reads that as a shimmer in the texture. When four frames are compressed into one latent slice, they share a single reconstruction error, and there's nothing left to shimmer: the differences between frames inside the slice are now set not by randomness but by whatever the model wrote into that slice. Flicker is exactly the price frame-by-frame processing pays, and it pays it even when every individual frame looks flawless.

And the other side of the same trick that an editor has to keep in mind. Because the frames inside a slice don't exist separately, exact frame-by-frame editing inside a generated fragment isn't possible the way footage is edited: you can't swap one frame out of four and leave the other three untouched, because that one frame doesn't exist in the latent representation. Editing happens either in whole fragments, or after decoding, on the finished image, by ordinary post-production means. For an editor, this means generated material behaves like something shot on film: you can cut it, but there's nothing to rewrite from the inside.

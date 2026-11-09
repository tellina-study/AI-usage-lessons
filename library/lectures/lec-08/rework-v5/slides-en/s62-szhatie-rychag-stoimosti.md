---
# Slide replaced 10/29/2026 (issue #301, per PUT-OT-ZAPROSA-K-REZULTATU.md):
# the former breakdown of Open-Sora 2.0's training cost was removed, its minutes (1.0) and
# place in the section were taken by the "path from request to result" slide — the owner's
# requirement: there are five device-of-the-mechanism diagrams in the deck (s16, s41, s59, s60,
# s83), and zero diagrams of the work itself. The former slide's content (the chain "raised the
# compression ratio → fewer tokens → training got cheaper," $200,000, the arithmetic re-check)
# is not lost: it moved in full into the notes of `s59a` (the slide about the cost of the link
# between frames, the same modality, the same Open-Sora 2.0 source) — see the edit from the same
# round. The refrain "the main lever is the tokenizer" (its third utterance out of four) was
# removed from this slide: the new content does not assert it. The refrain's count was
# reassembled onto three others — s19, s42, s91 — by an edit from the same round.
id: s62
local_id: "s62"
section: "3. Moving Image"
type: analitika
title: "The Path from Request to Result: Denoising Spacetime"
assertion: "Text starts the same denoising cycle as the still image, only over spacetime patches and with no cache at all: twenty to fifty passes of full 3D attention, with the request held through each of them via cross-attention; continuing a clip is the same cycle, except it starts not from noise but from a first frame encoded separately, and that is the only thing that changes between the two tracks"
source: "the Sora technical report; CogVideoX; HunyuanVideo"
chapter_ref: "chapter-part2d.md §3.7"
media: ""
media_needed: "visual content — a diagram of the path from request to result for video (denoising spacetime patches); a photograph explains nothing here. Published illustrations of a diffusion video model's denoising cycle (the Sora/CogVideoX technical blogs) — check through the six acquisition tiers before drawing this by hand"
scheme:
  kind: dorozhki
  entry: "REQUEST"
  exit: "RESULT"
  steps_arrows: true
  rows:
    - label: "Plain text"
      steps:
        - "text encoder, frozen"
        - "start: noise in the patch grid"
        - "denoising ×20–50, no cache"
        - "decoder → frames"
    - label: "+ with a seed frame"
      steps:
        - "+ first frame encoded separately"
        - "start: the first slice is the frame"
        - "the same cycle ×20–50"
        - "decoder → continuation"
blocks:
  - {label: "Step repeats", value: "20–50", note: "one range, with or without a seed frame"}
  - {label: "Where the request takes part", value: "at every step", note: "cross-attention holds the vector through the whole cycle"}
  - {label: "What changes / what stays the same", value: "patch values — yes; the grid and the decoder — no", note: "with a seed frame, only the start changes"}
  - {label: "Bottleneck", value: "3D attention with no cache, at every step", note: "factorized attention is 31 times cheaper but loses the link between frames", key: true}
blocks_per_row: 4
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

**The request holds every one of the twenty to fifty steps to the end; with a seed frame, only the start changes.**

## Speaker notes

This is the first diagram in the lecture of the work itself, not of a device — not what parts the model is built from, but exactly what happens to the request between input and the finished clip. The device of each part — spacetime patches and the causal 3D autoencoder — has already been broken down on the two previous slides; here those same details come together into one path, which the room has so far seen in fragments, not as a whole.

The path starts with the text encoder — the same frozen network as in the still image: it learns nothing new here, it only translates the words of the request into a vector. Next comes the start: latent spacetime patches, arranged into a grid of the needed size; without a seed frame they're filled with random noise, with a seed frame the first slice is fixed as a frame encoded separately, by the same method as in the causal autoencoder. This is exactly the structural difference the second track is meant to show: not a different mechanism, but a different starting point for the same mechanism.

The repeated step is denoising the whole block of patches at once, in a single pass through the network with full 3D attention, and it repeats twenty to fifty times regardless of whether there's a seed frame or not: the number of denoising steps doesn't know about the backstory, it only knows about the target quality. At each of these steps, the request's vector takes part again, through cross-attention — the same mechanism as in the image, stretched over the extra dimension of time. This is exactly the answer to "where does the request take part": not at the start, and not occasionally, but at every single step, from the first to the last, with no exceptions.

What changes and what stays the same is worth stating separately. The patch values change: at the first step they're almost pure noise or a fixed first frame; at the last, coherent content the decoder will turn into pixels. What doesn't change is the patch grid, the decoder, or how cross-attention reads the text vector. For the track with a seed frame, this rule holds literally: the only variable between the two paths is the content of the first slice at step zero.

There's one bottleneck, and it isn't in the model's size or in the encoder — it's in the attention mechanism itself. Full 3D attention with no cache at all means every one of the twenty to fifty passes recomputes the connections between all the patches from scratch, without carrying forward what was already computed on the previous step — exactly the price the course already named on the neighboring slide: attention factorized by space and time is thirty-one times cheaper, but that saving is paid for by the fact that a person's head in frame i+1 cannot directly attend to the head in frame i. The developers knowingly pay more for a direct link between frames — and it's exactly this bottleneck that explains why a clip runs seconds rather than minutes, regardless of which track it was launched from.

From here, a direct bridge to the section's next slides: the same diagram, the same cycle — and what comes next in the section is what this cycle can't do, and exactly how it's measurably limited.

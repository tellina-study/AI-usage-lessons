---
id: s22
section: "1. Still Image"
type: schema_timeline
title: "U-Net → DiT → MMDiT → Rectified Flow, and Adapters on Top of Any of Them"
assertion: "Over four years, generator architecture moved out of convolutional networks and into the same transformer the course has already taken apart — and it moved there because that's where scaling works. On top of the frozen base sits trainable control, and the way it's trained matches what the course already knows about language models"
source: "Ronneberger et al., 2015 (U-Net) · Peebles, Xie, 2022 (DiT) · the SD3 technical report, 2024 (MMDiT) · Liu, Gong, Liu, and Lipman et al., 2022 (rectified flow) · LoRA · textual inversion · DreamBooth · ControlNet · IP-Adapter"
scheme:
  caption: "Four generations of the load-bearing architecture, left to right — time"
  arrows: true
  rows:
    - steps:
        - "U-Net, 2015–2023: convolutions + transformer inserts"
        - "DiT, Dec. 2022: the latent is cut into patches → a vector"
        - "MMDiT, March 2024: text and image — one sequence"
        - "rectified flow, 2022→2026: noise and data — a straight line"
izmerenie:
  title: "Identical models, different patch size — ImageNet 256×256, 400k training steps"
  rows:
    - {model: "DiT-XL/8", tokens: "16", gflops: "7.39", params: "676M", rasstoyanie_freshe: "106.41"}
    - {model: "DiT-XL/4", tokens: "64", gflops: "29.05", params: "675M", rasstoyanie_freshe: "43.01"}
    - {model: "DiT-XL/2", tokens: "256", gflops: "118.64", params: "675M", rasstoyanie_freshe: "19.47"}
  conclusion: "The same number of weights — sixteen times more tokens. A sixteenfold increase in compute delivers a fivefold improvement in the metric at an UNCHANGED model size"
blocks:
  - {label: "The slide's measurement", value: "XL/8: 676M, 7.39 GFLOPs, Fréchet 106.41 · XL/2: 675M, 118.64 GFLOPs, 19.47", note: "the lever is in how the input was cut up, not in the number of weights", key: true}
  - {label: "Two kinds of add-ons", value: "LoRA/inversion/DreamBooth — train weights · ControlNet/IP-Adapter — leave them untouched", note: "the same ladder as for a language model; the add-ons stack — style + pose + face on one base"}
  - {label: "11 conditions for reproducibility", value: "11 items — from the weights to the GPU model", note: "it's different for a language model: 1000 requests to vLLM at T=0 gave 80 different answers (2025)"}
media: ""
timing_min: 0.8
in_bucket: false
status: собран
---

## Visible slide text

**16 times more tokens — the metric is 5 times better.**

**Adapters sit on top of the architecture: the base is frozen, the add-ons stack literally.**

## Speaker notes

This slide's plot in one sentence: over four years, generator architecture moved out of the
world of convolutional networks and into the same transformer the course has already taken
apart — and it moved there because that's where scaling works.

U-Net was invented for segmenting medical scans: a convolutional network reduces resolution
while growing the number of channels, then symmetrically reconstructs it, feeding the output of
each level of the contracting branch into the expanding branch. It suited denoising by
construction: the input and output are the same size, and you need work happening at every
scale. Text got in through blocks of cross-attention — transformer blocks were already there, as
inserts inside the convolutional frame, not as the frame itself. The field moved away from it
because a convolutional frame carries built-in assumptions about picture structure (locality,
shift invariance), which help on small data and get in the way on large data — the network stops
scaling predictably.

The paper proposing a transformer instead of U-Net came out in December 2022. The latent is cut
into patches, and each patch is linearly projected into a vector — the same input lookup table
the course already took apart, except that instead of a vocabulary lookup, here it's a linear
projection, because the input is continuous. A measurement from this paper's appendix is worth a
whole slide on its own: three models on the same dataset and training budget, with practically
identical parameter counts, differing only in patch size — how many tokens the same latent got
cut into. A sixteenfold increase in compute delivers a fivefold improvement in the metric at an
unchanged model size — direct confirmation of the course's thesis in a new domain: cost and
quality are determined by sequence length, not by the number of weights. Here the evening's
refrain is presented as a measurement: the lever sits in how the input was cut up.

The next generation, MMDiT, solved a specific problem: in earlier schemes, text was a
one-directional input, and that wasn't enough for complex descriptions. The solution — glue the
text and image tokens into one sequence and pass them through a single joint attention, with
separate normalization and projection weights for text and image; only the attention operation
itself is shared.

Rectified flow is, strictly speaking, no longer diffusion: diffusion travels from data to noise
along a curved path, the return path is curved too, and integrating it requires many steps.
Rectified flow connects noise and data with a straight line and teaches the network to predict
the velocity of motion along it — if the trajectory is straight, a large step introduces no
error, and in the limit, sampling is one step. In practice the ideal isn't reached, but the path
is noticeably straighter: 20–30 steps deliver what diffusion needs 50–100 for. Terminological
honesty: calling this diffusion today is, strictly speaking, inaccurate — there's no forward
noising process there, just training a vector field along a straight line; the industry keeps the
word out of inertia, and because the interfaces, samplers, and adapters are shared.

On reproducibility — two things, and the second matters more than the first. All the randomness
of a deterministic sampler is concentrated in the starting noise: the same weights, the same
sampler, the same number of steps give the same picture. This is one of the few points where a
media model is more reproducible than a language one — there, temperature set to zero doesn't
give determinism: a standard vLLM setup, 1000 requests with the same prompt at zero temperature,
gave 80 different answers (Thinking Machines Lab, "Defeating Nondeterminism in LLM Inference,"
September 2025, model Qwen3-235B-A22B; the culprit is compute kernels' dependence on batch size).
But "reproducible" means far more conditions than it looks like: the full list is 11 items, from
the autoencoder's version to the GPU model, and any one of them changes the result. From this
comes a direct requirement: a generative pipeline has to be versioned like a software build.

And what's completely absent inside — and every absence is meaningful. No causal mask: the image
looks in every direction, attention is bidirectional by construction. No key-value cache. No
vocabulary and no logits — the output is continuous. No output length as a variable — the size is
fixed before the run starts.

On top of any of these four architectures, the same fine-tuning approach works — the ladder the
course already introduced for language models (prompting, document retrieval, fine-tuning,
distillation), except the middle rung is richer here: besides "train an adapter" there's also
"plug in a ready-made control module," and that's often cheaper. LoRA — low-rank adapter matrices
in selected layers, with the base frozen, tens to hundreds of MB. Textual inversion — the most
economical technique: a single vector is trained, which becomes a "new word" in the text
encoder's vocabulary; the model itself doesn't change, the authors needed only 3–5 images of the
concept, the result is kilobytes. DreamBooth — fine-tuning the model itself, linking a rare
identifier to an object; in practice done on top of LoRA, otherwise it's gigabytes. ControlNet —
a trainable copy of the model's contracting half, taking in a structural condition through
zero-initialized convolutions — hundreds of MB. IP-Adapter — "a description, but as a picture":
the reference is encoded by a separate cross-attention running parallel to the text one; the
authors claim the quality of full fine-tuning at 22 million parameters, tens of MB.

The structural thesis is the same one the course has already formulated: the base is frozen, a
small add-on is trained, the add-ons are modular and they stack — here, literally: a style
adapter, a pose's structural condition, and a face reference all get hung on one base model at
the same time, and all three work together without getting in each other's way. It's exactly
this stackability that made open weights a working production tool: you can assemble a
configuration out of other people's pieces in hours instead of months.

The watershed that determines how much a solution will cost: ControlNet and IP-Adapter are
conditioning — work done at run time, the weights don't change, they sit on the side of "place
the knowledge." LoRA and DreamBooth sit on the side of "encode the behavior." The question "we
need to fine-tune the model for our character" gets closed, in half the cases, with a face
reference and zero hours of training — exactly like "we need to fine-tune the language model for
our documentation" gets closed, in half the cases, with document retrieval.

And separately — the very reason adapters belong in the technical block at all. Here the
parallel with language models works completely, and that has to be named as a coincidence, out
loud. The block already had several places where the transfer of knowledge turned out to be
false: temperature and CFG control different things, caching is impossible here, and feeding in a
source of truth doesn't exist. It's easy to conclude that nothing transfers — and that would be a
second mistake, mirroring the first one. Fine-tuning by adapter transfers without adjustment: the
same idea, the same economics, the same add-on sizes. The skill of telling apart where a transfer
is honest and where it's false is exactly the content of this technical block.

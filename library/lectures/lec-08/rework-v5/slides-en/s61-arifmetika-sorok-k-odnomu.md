---
id: s61
local_id: "s61"
section: "3. Moving Image"
type: analitika
title: "Quadratic Growth on Doubling a Frame's Side: the 'Forty-to-One' Arithmetic"
assertion: "Training on 129-frame video at a resolution of 768 points is forty times slower than at 256 points, and the gap arises from the quadratic computational complexity of self-attention as the token count grows; resolution tripled — training slowed down forty times, and this arithmetic is what everything said below about cost rests on: length, resolution, and frame rate are bought non-linearly, and price lists honestly reflect it — a ten-second clip costs exactly three times more than a five-second one"
source: "Open-Sora 2.0; a video-generation provider's price list"
chapter_ref: "chapter-part2d.md §3.7"
media: ""
media_needed: "visual content — breaking the factor of forty down between the linear and quadratic bounds; there is no photograph for this subject"
scheme:
  kind: shkala
  unit: "how many times slower training is when the frame's side triples"
  base: "129 frames at 256 points = one time"
  from: 0
  to: 90
  marks:
    - {value: "9", label: "Linear"}
    - {value: "40", label: "Measured", key: true}
    - {value: "80", label: "Quadratic"}
blocks_per_row: 1
blocks:
  - {label: "The price list reflects this", value: "a ten-second clip is three times the price of a five-second one", note: "there's no volume discount here, there's a markup", key: true}
itog:
  yarlyk: "Outcome"
  text: "Length, resolution, and frame rate are bought non-linearly: threefold by side becomes ninefold by pixels, and attention is quadratic"
timing_min: 1.0
in_bucket: false
status: собран
---

## Visible slide text

## Speaker notes

The quadratic nature of attention produces an effect worth remembering by number, because it explains almost the entire economics of this modality.

The capstone figure, from an open paper: training on 129-frame video at a resolution of 768 points is forty times slower than at 256 points. The authors name the cause themselves: the gap arises from the quadratic computational complexity of self-attention as the token count grows.

Let's explain exactly where the forty comes from: reproducing this count is more useful than memorizing the result. Tripling a frame's side means ninefold more points, and so roughly ninefold more patches. Attention is quadratic in the number of patches, which gives about eighty times. The rest of the network — convolutions, dense layers, normalization — grows linearly, that is, ninefold, and dilutes that multiplier. The measured forty sits between the linear ninefold and the quadratic eightyfold — exactly where it should sit for a network in which attention is a significant but not overwhelming share of the compute.

It's useful that this checks out. The arithmetic from the previous slide predicts the order of magnitude, and the published measurement confirms it. This is a rare situation: usually there's a multiplier between a back-of-the-envelope calculation and a hardware measurement that nobody can explain. Here, there's an explanation, and it's checkable.

Resolution tripled — training slowed down forty times. Everything said below about cost rests on this arithmetic: length, resolution, and frame rate are bought non-linearly. Price lists honestly reflect this: at one provider, a ten-second clip costs exactly three times the price of a five-second one, meaning a second of the longer clip is fifty percent more expensive. There's no volume discount here, there's a markup — the exact opposite of what compute pricing elsewhere has trained us to expect.

From here come three answers to the question a student asks first: why does a clip run five to ten seconds.

Quadratic growth. Doubling length under full 3D attention quadruples the cost of attention; the measured confirmation is the forty-to-one above.

Memory. A quarter million tokens for five seconds of high-definition video, at twenty to fifty denoising steps, runs into the limit of a single compute node; the leading model holds four kinds of parallelism at once just to manage it.

Data. The training clips themselves are short: in one open model's dataset, 35 million single-scene clips, each about six seconds on average. The model never saw long continuous scenes, and so it doesn't know how to do them. This is the answer most often missed, and it's the most mundane and the hardest to fix: even if compute were free, there would be nothing to learn a long scene from.

The developers state the trade-off directly: trading off motion dynamics for temporal visual quality, and limiting video duration to five to ten seconds in order to prioritize resolution. The actual limits of products as of October 2026 sit in this same band: four, six, or eight seconds for one family, up to twenty seconds for another, up to ten seconds with sound for a third, up to sixty seconds for a separate open-weight model optimized for compression.

Techniques for extending duration have gone through five generations in three years, and it's worth listing them, because each one cures the previous one's disease. Naive extension — build the clip onward from the last frame; it works, and it accumulates error. Sliding-window denoising — assign more noise to frames appearing later, reflecting greater uncertainty about the future. Independent noise levels per token — the most influential idea in this line: it joins the variable length natural to autoregression with the controllability of full-sequence diffusion. Causalization plus distillation — a bidirectional transformer is converted into an autoregressive one, a fifty-step model is distilled into a four-step one, a cache appears, and with it 9.4 frames per second on a single card. Importance-based frame packing — compress the context more aggressively the less important a frame is, and use that to hold thousands of frames inside a fixed window.

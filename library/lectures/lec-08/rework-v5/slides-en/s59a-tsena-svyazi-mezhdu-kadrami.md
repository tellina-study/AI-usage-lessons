---
id: s59a
local_id: "s59a"
section: "3. Moving Image"
type: analitika
title: "The Cost of the Link Between Frames: 62.1 Billion Pairs Against 2.01 Billion"
assertion: "Full 3D attention costs 30.9 times more than factorized attention by the number of attention pairs, and leading models knowingly pay that thirtyfold price: with factorized attention, a person's head in the next frame cannot attend directly to the head in the previous frame"
source: "the Sora technical report; CogVideoX"
chapter_ref: "chapter-part2d.md §3.7"
media: ""
media_needed: "visual content — numbers on plates and two comparison columns; a photograph explains nothing here"
itog:
  yarlyk: "Outcome"
  text: "A model engineering trade-off: consistency bought with compute, and the price paid is known"
blocks:
  - {label: "The cost of full 3D attention", value: "62.1B pairs against 2.01B", note: "for five seconds of high-definition video: 249,240 patches, a 31-by-8,040 grid; factorized attention is 30.9 times cheaper", key: true}
  - {label: "What that thirtyfold price buys", value: "a direct link between frames", note: "with factorized attention, 'the head of a person in frame i+1 cannot directly attend to the head in frame i' — only indirectly, through background patches"}
columns:
  left:
    head: "What's the same as in the still image"
    items:
      - "The autoencoder is the tokenizer; the model sits on top of it"
      - "Denoising rewrites every token at every step"
      - "No cache exists: language-model pricing economics doesn't carry over"
  right:
    head: "What gets added along with time"
    items:
      - "Compression — in both space and time"
      - "Encoding is triple: two spatial axes and time"
      - "'Full or factorized attention': the price is counted"
      - "The report discloses no details: the figure is a reconstruction"
timing_min: 0.3
in_bucket: false
timing_note: "split off from s59 by body height: 0.8 -> 0.5 (s59) + 0.3 (s59a). Section 3's total did not change"
status: собран
---

## Visible slide text

## Speaker notes

Why developers pay for full 3D attention is explained most clearly by a caption to a diagram in one of the papers: with factorized spatial and temporal attention, the head of a person in frame i+1 cannot directly attend to the head in frame i, and visual information is only passed implicitly, through other background patches. The mechanics are simple: factorized temporal attention looks along the same spatial position, and if the object shifted five tokens sideways between frames, there's no direct channel of "head here — head there."

The price is counted. For five seconds of high-definition video, the total patch count is 249,240, on a 31-by-8,040 grid. Full 3D attention gives 249,240 squared, that is, 62.1 billion pairs. Factorized attention gives 31 times 8,040 squared, plus 8,040 times 31 squared, that is, 2.01 billion pairs. Factorized is 30.9 times cheaper. Leading models knowingly pay a thirtyfold price in attention-pair count so that the head in the next frame can see the head in the previous one directly. This is a textbook engineering trade-off: they bought consistency with compute, and they know exactly what they paid for it.

An honest caveat, mandatory for this section. The technical report for the best-known video model states outright: model and implementation details are not included in this report. There's nothing in it about compression ratios, patch size, parameter count, or token counts. Any specific figure about it circulating online is a reconstruction. Everything countable below is therefore taken from open models that do publish their own parameters.

What has stayed exactly the same in this modality as in the still image is worth stating on its own — otherwise the section reads as a story about a new technique that isn't actually here. The autoencoder works as the tokenizer, with the model sitting on top of it. Denoising rewrites every token at every step, rather than appending them one at a time. There's no cache, and there can't be one, and the whole economics of language-model pricing, built on reusing already-computed context, does not carry over here by a single line.

Exactly three things get added along with time. Compression runs not just over space but over time too. Positional encoding becomes triple: two spatial coordinates and one temporal one, and the channels are split between the axes in a fixed proportion. And a choice appears between full 3D attention and factorized attention, with a priced cost. The first two additions are cheap; the third is the main expense of the whole modality.

The practical conclusion, which carries over beyond video: when an architecture offers a choice between "expensive and connected" and "cheap and disconnected," ask exactly what the connectedness costs and exactly what's lost without it. Here there are numbers for both questions — the thirtyfold price and the absence of a direct channel between frames — and that's what makes the conversation an engineering one. Where such numbers don't exist, the choice is made by taste, and that should be called by its own name.

How to check this calculation yourself, without taking it on faith. The patch count for five seconds of high-definition video is 249,240, on a 31-by-8,040 grid. Full 3D attention compares every patch with every other: 249,240 squared gives 62.1 billion pairs. Factorized attention compares patches within a frame and along time separately: 31 times 8,040 squared, plus 8,040 times 31 squared — that's 2.01 billion. The ratio is 30.9. The arithmetic fits in two lines, and that's exactly its value: a number you can recompute on paper stops being an advertising claim.

The same economics of the lever shows up in the cost of training too, and it's worth carrying over from the earlier slide about compression (removed in the 10/29/2026 reshuffle — the path from request to result took its place). The only full public breakdown of a video model's training cost belongs to Open-Sora 2.0: the paper is titled "training a commercial-level video model for two hundred thousand dollars," and the stage-by-stage breakdown gives 4,160 accelerator-days at a rate of two dollars per hour — 4,160 × 24 × 2 = $199,680, and the number checks out. The authors name the source of the savings directly: they raised the spatial compression ratio to 32, cutting tokens from 76,000 to 19,000 for five seconds, and got a fivefold increase in training throughput with the parameter count unchanged at 11 billion. The lever is the same autoencoder that also carries the cost of the link between frames on this very slide: one setting decides both how much training costs and how much attention costs.

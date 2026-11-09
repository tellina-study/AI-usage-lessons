---
# Source: chapter/chapter-part3b.md § 4.13. DreamFusion — Poole, Jain, Barron,
# Mildenhall, arXiv:2209.14988 (2022); TRELLIS — Microsoft Research, arXiv:2412.01506 (2024);
# second-generation Hunyuan3D — a neighboring line of the same family.
# Deviation from DECK-KARTA: the map's heading is "Native 3D diffusion…"; "native" is a
# calque (§5.21), the slide reads "diffusion straight in 3D." Content unchanged.
# The caveat "there's no human in this pair" stands ON THE SLIDE deliberately: without it
# the number changes meaning (§7.2 of the form canon — this isn't a caveat about measurement
# quality, it's part of the number itself).
id: s73
local_id: "s73"
section: "4. 3D Scenes and Real Time"
type: analitika
title: "Generating an object: diffusion straight in 3D versus optimization through rendering"
assertion: "An hour and a half per object in 2022 against roughly ten seconds in 2024 — a gap of roughly 500 times, and it didn't come from hardware: the first method starts every object from scratch and spends fifteen thousand steps of a full pass of a flat model on it, the second trained once on half a million objects and now does one forward pass; this is a comparison of two machine methods against each other, there's no human in this pair, and \"500 times faster than a modeler\" doesn't follow from it"
source: "Poole et al., arXiv:2209.14988; Microsoft Research TRELLIS, arXiv:2412.01506; https://arxiv.org/abs/2412.01506"
media: ""
media_needed: "the picture was moved to the neighboring design slide earlier in the section — here the diagram carries the same content in text"
media_note: "Wikimedia Commons, File:Neural radiance fields nerf pipeline.jpg, MIT license. Tier 2 (Wikimedia Commons). The diagram shows exactly the left half of the slide — the radiance field that gets rendered from an angle and compared to the target; the first of the two methods does precisely this fifteen thousand times in a row. The image illustrates one of the two methods, not both, and that's stated here honestly: no diagram showing both was found in the open"
blocks:
  - {label: "Optimization through rendering (DreamFusion, 2022)", value: "about 1.5 hours per object", note: "15,000 steps on a four-chip machine, rendering at 64×64 pixels"}
  - {label: "Diffusion straight in 3D (TRELLIS, 2024)", value: "about 10 seconds per object", note: "one forward pass after training on 500,000 objects"}
  - {label: "Gap", value: "roughly 500 times", note: "both numbers are machine numbers: this is 2022 against 2024 inside one engineering line, there's no human in the pair", key: true}
blocks_per_row: 3
scheme:
  kind: dorozhki
  caption: "The same output obtained by two different designs"
  steps_arrows: true
  rows:
    - label: "Fitting through rendering"
      steps:
        - "model doesn't change — a shape judge"
        - "15,000 rendering steps from random angles"
        - "output — an object in 1.5 hours"
    - label: "Diffusion in 3D"
      steps:
        - "trained once: 500K objects"
        - "one representation → three formats"
        - "output — an object in 10 seconds"
timing_min: 1.1
in_bucket: false
method_steps: ["design", "amortization"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The gap didn't come from hardware.** The first method starts every object from scratch and spends a full cycle of fitting on it; the second trained once on half a million objects — and the cost moved from output into training.

## Speaker notes

The second storyline in this design is about generating an object that doesn't exist. There's a measured gap of roughly five hundred times here, and it has to be handled carefully, or you get exactly the kind of false pair the course hits separately for elsewhere.

An hour and a half against ten seconds — a gap of roughly five hundred times. And a mandatory caveat, without which this number is misleading: this is a comparison of two machine methods against each other, there's no human in this pair. No claim of "five hundred times faster than a modeler" is made here, and none can be made — how long the same object takes a modeler isn't named in the sources. The pair compares 2022 with 2024 inside one engineering line, and that's its only content.

But this pair does have content, and here it is: the gap didn't come from faster hardware — both numbers were obtained on machines of the same class. Optimization through rendering starts every object from scratch and spends a full fitting cycle on it. Diffusion straight in 3D trained once on half a million objects and now does one forward pass. This is a textbook example of cost transfer: the computation hasn't disappeared, it moved from the moment of output to the moment of training, where it's paid once and divided across every later run. The course has already shown this same figure for language models and for flat generation; here it's visible in pure form and with a measured multiplier.

For an engineer, the practical question that follows is one worth asking any vendor: how much does your inference cost and how much did your training cost. A system with cheap inference almost certainly moved its cost into training — and that's fine for exactly as long as the task stays inside the corpus it was trained on. Past that boundary, a cheap forward pass starts producing plausible nonsense at the same speed it was producing usable results.

An hour and a half and ten seconds are worth breaking down by stage, to see exactly what's being paid for. In the first method, time is split roughly evenly between rendering the radiance field and running the flat diffusion model, and a full pass is made on every one of the fifteen thousand steps — with rendering at sixty-four pixels per side. In the second, a neighboring line of the same family gives an honest breakdown: about four seconds for the multi-view image and about seven for geometry reconstruction, roughly eleven total. Both breakdowns are published by the authors, and both are worth asking any vendor for: not "how long does the output take," but "what does that output break down into."

And a short warning against a common reading mistake. Five hundred times is not "the model got five hundred times smarter" and not "the work got five hundred times cheaper." It's the distance between two engineering decisions for the same task, separated by two years. There's no human in this pair at all, and any phrase of the form "five hundred times faster than an artist" built from this number comes from dividing a measured figure by a made-up one.

Remember this general figure too, because you'll meet it again. Cost in machine learning almost never disappears — it moves. From output to training, from computation to data, from the engineer's work to the labeler's work. The question "where did it move to" replaces the question "how much was saved," and the answer to it is far more honest.

And one question worth asking any vendor of such a system: how much does your inference cost and how much did your training cost. Cheap inference almost always means the cost has been moved into training — and that's fine for exactly as long as your task stays inside the corpus it was trained on.

---
# Slide replaced 2026-10-29 (issue #301, task PUT-OT-ZAPROSA-K-REZULTATU.md):
# the former "classical asset pipeline" slide was dropped, and its minutes (0.3) were taken
# by the "path from request to result" slide — the fifth and last of the six work diagrams
# (an owner requirement: the deck had five mechanism diagrams — s16, s41, s59, s60, s83 —
# and not one work diagram). The classical pipeline wasn't lost without a trace: which of the
# nine stages the model touches is shown next to it, on s68b, as an icon grid (the same
# revision round). The five ways of getting data about a real object are folded into one
# block on the same slide — photogrammetry, formerly the first of the five, became the
# second track of this very slide: the point cloud the old s68b talked about is the start
# of reconstruction right here.
id: s68a
local_id: "s68a"
section: "4. 3D Scenes and Real Time"
type: analitika
title: "The path from request to result: a 3D scene"
assertion: "Text and photographs launch loops that differ in nature but share one form: a diffusion-model judge or comparison against a real frame holds every step of the optimization, not just the start, and the number of steps needed is three to four orders of magnitude larger than denoising a ready-made model — fifteen thousand for text via DreamFusion, thirty thousand for Gaussian splatting from photographs — because there is no shared trained prior here, and every object learns from scratch"
source: "Poole, Jain, Barron, Mildenhall, 2022, https://arxiv.org/abs/2209.14988; Kerbl, Kopanas, Leimkühler, Drettakis, SIGGRAPH 2023, https://arxiv.org/abs/2308.04079"
chapter_ref: "chapter-part3b.md §§4.11–4.13"
media: ""
media_needed: "visual content needed — a diagram of the path from request to result for a 3D scene; a photograph explains nothing here. Published illustrations of the SDS optimization loop (the DreamFusion project site) or the Gaussian optimization loop (the 3D Gaussian Splatting project site) — check against the six tiers of acquisition before drawing by hand"
scheme:
  kind: dorozhki
  entry: "REQUEST"
  exit: "RESULT"
  steps_arrows: true
  rows:
    - label: "Text"
      steps:
        - "judge model, unchanged"
        - "start: random field"
        - "render → judge's score → step ×15k"
        - "mesh from the field"
    - label: "Object photographs"
      steps:
        - "camera calibration → point cloud"
        - "start: Gaussians from the cloud"
        - "render → compare to photo → step ×30k"
        - "mesh from Gaussians"
blocks:
  - {label: "Step repeats", value: "15,000 (text) · 30,000 (photographs)", note: "not denoising — optimization from scratch"}
  - {label: "Where the request takes part", value: "on every one of all the repeats", note: "the judge/comparison holds every step"}
  - {label: "What changes", value: "parameters — every step; the representation — no", note: "Gaussians are cloned, split, and deleted"}
  - {label: "Bottleneck", value: "3–4 orders of magnitude more repeats than a ready model", note: "no prior; a ready model takes 20–50 steps", key: true}
blocks_per_row: 4
timing_min: 0.3
in_bucket: false
method_steps: ["general description of the stage", "path from request to result"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Every step is held by a judge or a photograph — orders of magnitude more repeats than with a ready-made model.**

## Speaker notes

The fifth and last of the six work diagrams in this lecture, and the only one where the path from request to result is built not out of denoising a ready-made model but out of optimization from scratch. The difference is worth saying out loud, because the shape of the path is the same — request, start, a repeated step, result — while the numbers inside it differ by orders of magnitude, and that by itself is a lesson.

The text track is the DreamFusion method. A pretrained flat diffusion model doesn't change at all: it acts as a judge, scoring how plausible a randomly initialized radiance field looks from various angles. The repeated step is: render the field from a random angle, get a score from the judge, take an optimization step on the field's parameters toward a higher score. This step repeats fifteen thousand times, roughly an hour and a half on a four-chip machine, and the reason is the judge: a full pass of the diffusion model is made on every one of the fifteen thousand steps, not once at the start.

The photograph track is Gaussian splatting. Cameras are calibrated from photographs, and the calibration also yields a sparse point cloud as a byproduct — the same byproduct of photogrammetry. The cloud becomes the start: Gaussians — elongated, semi-transparent blobs with a position and a color — are initialized at its points. The repeated step is: render the scene from a known, already-shot angle, compare it to the real photograph, take an optimization step on the Gaussians' parameters, and every so often also adjust their count — clone where detail is missing, split where one blob took on too much, delete where there's no point in it. This step repeats thirty thousand times, roughly forty-one minutes on a single accelerator.

Where the request takes part — in both tracks the answer is the same, and it's non-trivial: not at the start, but on every one of all the repeats. For text that's a full pass of the judge model at every step; for photographs it's comparing the render to the real photograph at every step. This isn't cross-attention, as in image and video — it's a different mechanism, a training signal rather than a generation condition — but the role is the same: without the request being presented afresh at every step, the optimization doesn't know which way to move.

What changes and what stays the same: the representation's parameters — the field's coordinates and color, or the Gaussians' position, shape, and color — change at every step. The representation itself, meaning what kind of object counts as the scene, doesn't change, even though for Gaussians even their count changes.

This modality's bottleneck isn't the autoencoder and it isn't attention — it's the sheer scale of repetition. Where a ready-made diffusion model has a shared trained prior — shared knowledge accumulated over many previous objects — and twenty to fifty denoising steps are enough, here there is no prior: every object is optimized from scratch, and that costs three to four orders of magnitude more repeats. That very cost is exactly what native 3D diffusion, such as TRELLIS, discussed later in the section, removes: it trained once on half a million objects and now does one pass in seconds — the same amortization lesson the course has already shown for language models and for flat generation, except here you can see it as a direct contrast: fifteen thousand steps against one pass, on the same fifteen words of request.

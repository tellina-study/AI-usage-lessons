---
# Source: chapter/chapter-part3b.md §§ 4.11–4.12; Mildenhall et al., ECCV 2020,
# arXiv:2003.08934; Kerbl, Kopanas, Leimkühler, Drettakis, SIGGRAPH 2023, arXiv:2308.04079;
# Müller et al., SIGGRAPH 2022, arXiv:2201.05989.
# Four measures are laid out in two columns by method name, not as "before → after" pairs:
# we don't build pairs on this slide (§6.1 of the form canon), and here it's also more
# accurate — both methods are alive, this isn't a "before" and "after," it's two approaches
# chosen by task.
#
# CONSOLIDATION 2026-10-29 (issue #301, task "section 4: 19→10-11"): the slide absorbed s71a
# ("The radiance field and Gaussian splatting: two designs of one scene") and s72 ("Answer:
# paid for with scene size") whole. s72 added no new number — it repeated the same three
# measures (×70, ×2,200, ×85) already standing in the blocks here, dressed up as "opening
# the question to the room"; the question itself was dropped by the owner's decision of
# 2026-10-29 (SVEDENIE-KADROV.md §6), there's nothing left to open. S72's unique remainder —
# the methodological lesson "look for the fourth column" — has been moved into the speaker
# notes in full, not a sentence lost. The illustration was dropped: a slide with three blocks
# and a two-column diagram doesn't fit alongside a side image at any width (checked by the
# build up to the step "side illustration doesn't fit at any width up to 4.00″"); the fix is
# the same path as on s73 in this section. Minutes: 0.7 + 0.6 + 0.4 = 1.7 (no change to the
# section total).
id: s71
local_id: "s71"
section: "4. 3D Scenes and Real Time"
type: analitika
title: "NeRF and Gaussian splatting: what got traded for speed"
assertion: "The move from a radiance field to Gaussian splatting sped up scene training by roughly 70 times and rendering by roughly 2,200 times, at quality that didn't change (27.21 decibels against 27.69, and on the indoor set 29.41 against 29.40 — a wash), and the price for this is a single fourth figure: the scene takes up 734 megabytes instead of 8.6, roughly 85 times more; three measures improved at the expense of a fourth, and the fourth stood in the same table in the same paper"
source: "Kerbl et al., SIGGRAPH 2023, arXiv:2308.04079; Mildenhall et al., ECCV 2020, arXiv:2003.08934; https://arxiv.org/abs/2308.04079"
media: ""
media_needed: "the picture was dropped during consolidation: a slide with three blocks and a two-column diagram doesn't fit a side illustration at any width. Previously: 3dgs viewer QIBWA66MsC.jpg (Wikimedia Commons, CC BY-SA 4.0) — a viewer of a scene reconstructed by splatting"
blocks:
  - {label: "Training one scene", value: "roughly 70 times faster", note: "48 h for the radiance field against 41 min 33 s for splatting; same scene, same accelerator"}
  - {label: "Rendering the scene", value: "roughly 2,200 times faster", note: "0.06 frame/s against 134 — from a research project to an interactive display"}
  - {label: "Memory per scene", value: "roughly 85 times more", note: "8.6 MB against 734 — the very fourth figure that is the price", key: true}
blocks_per_row: 3
scheme:
  kind: dorozhki
  caption: "The difference is created by the scene's design, not the model's size"
  steps_arrows: true
  rows:
    - label: "Radiance field, 2020"
      steps:
        - "scene — one network: point and view → density and color"
        - "frame — 150–200 million network queries along a ray"
        - "48 hours · 0.06 frames/s · 8.6 MB"
    - label: "Gaussian blobs"
      steps:
        - "scene — elongated, semi-transparent blobs"
        - "frame — one projection per blob by a rasterizer"
        - "41 minutes · 134 frames/s · 734 MB"
timing_min: 1.7
in_bucket: false
method_steps: ["design", "the \"gave — took\" pair"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Quality didn't change: the difference is under half a decibel, invisible to the eye.** The economics changed — and in both directions at once.

## Speaker notes

Here starts the core of the section: a design backed up by peer-reviewed work with published measurements. It all starts with the 2020 paper on radiance fields. The idea fits in one sentence, and it's worth reading slowly: the scene is represented by one small, fully-connected network — there are no polygons and no point cloud in this representation. Asked "what's at this point in space, viewed from this direction," the network answers with two numbers — the density of matter and the color visible from that direction. Five numbers in, four numbers out. There's nothing else at all in the scene representation.

The numbers from the paper explain why the method stayed in the lab. Training one scene — one to two days on a single accelerator of that generation. Network queries per frame — one hundred fifty to two hundred million. Rendering one frame — about thirty seconds, meaning six hundredths of a frame per second. Size of the trained scene — five megabytes of weights. That last pair of numbers has to be read next to the classical baseline: a method of the same purpose, used before neural approaches, trained in under ten minutes and required more than fifteen gigabytes per scene. The radiance field fit the scene into five megabytes — roughly a three-thousand-fold compression — and paid for it with thirty seconds per frame against interactive display for the classical approach. This is the "gave — took" pair in its purest form, and it will be needed again immediately, because the next turn in the story is exactly the opposite trade.

An intermediate step shows where the lever is in this design. The work Instant-NGP cut training cost from days to seconds without touching the network itself: it changed the input encoding — placing a multi-resolution, learnable feature table next to the network and leaving the network a small job on top of it. Five minutes thirty-seven seconds of training, 11.7 frames per second, thirteen megabytes. The course's throughline sounds here for the third time on a third piece of material: the win came from changing the representation of the input, not from growing the network.

The picture is assembled by classical accumulation along a ray: from the camera, a ray is cast through every pixel, samples are taken along it, densities and colors are summed. The key to training is that this operation is differentiable: the network can be trained directly on a set of photographs with known camera positions — predict the picture, compare it to the real one, adjust the weights. The 2023 work changed the representation once more. The scene is represented by a large number of elongated, semi-transparent blobs — each has a position, shape and orientation, opacity, and a color that depends on the viewing direction. They start from that same sparse point cloud that's left over after camera calibration anyway — there's no empty space here. Display here is projecting the blobs onto the screen and blending them on an ordinary rasterization pipeline, the kind graphics cards have been designed for over the last thirty years; in a radiance field every pixel requires hundreds of network passes along a ray, here it's one projection per blob. The difference is in the nature of the operation, not in the volume of computation.

The quality column in this table shouldn't be lost. Twenty-seven point twenty-one against twenty-seven point sixty-nine — a difference under half a decibel, visually indistinguishable; on the indoor set the score is a dead wash. So quality didn't change. What changed was the economics, and it changed in both directions at once: training and display sped up by two to three orders of magnitude, while scene volume grew by almost two. The authors also name the image's defects themselves: elongated, blotchy blobs in poorly observed areas, sudden switches in blending order as the camera moves, and a complete absence of regularization — the method is obligated to reproduce the photographs, not to describe the scene in a physically meaningful way. A typical scene after thirty thousand steps is two to five hundred thousand Gaussians.

The full breakdown of the price, named by the authors themselves rather than by their critics, reads like this. When training large scenes, peak video memory usage, in their own words, "can exceed 20 gigabytes." Display requires a few hundred megabytes for the scene model itself and another thirty to five hundred megabytes for the rasterizer. That is the price, and it's worth reading as a template: in a peer-reviewed paper, the losing figure sat in the same table as a fourth column; in a press release it wouldn't have been there.

And the practical conclusion that will outlive both specific papers, and for which this slide used to get its own separate answer-slide. When you're shown a table of four columns and three of them improved, look for the fourth one first. If it's not in the table, that doesn't mean it doesn't exist in nature: it means whoever did the counting didn't show it. In a peer-reviewed paper the authors themselves put memory right next to speed — because a reviewer would have asked. In a press release there's nobody to ask.

For practice, comparing the two designs leads to a question worth asking before any other: in what form does the system store what it works with. The answer predicts speed, volume, and which operations turn out cheap and which impossible — long before you ever see anyone's measurement.

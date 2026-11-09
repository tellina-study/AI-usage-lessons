---
id: s16
local_id: s1-02
section: "1. Autonomous robots in space"
type: norm
title: "Where the classical approach handles it, where a model is needed"
assertion: "Geometry is solved by the classical approach with no training; recognizing an object against noise needs a trained model"
source: "—"
media: ""
media_needed: "Two columns: 'classical approach handles it' vs 'needs a model', with examples. Phase 6."
columns:
  left: {label: "The classical approach handles it, no training", items: ["Terrain traversability, cave mapping (AutoNav/GESTALT)", "Falcon 9 landing — convex optimization (G-FOLD)", "The physics of soil and optics is known in advance"]}
  right: {label: "Needs a trained model", items: ["Recognizing an artifact against Martian dust", "Features aren't known in advance, statistics from examples", "A lightweight classifier inside an otherwise classical pipeline"]}
in_bucket: true
status: draft
---

## Visible slide text

**The strongest example of this distinction lies outside surface navigation entirely.** Falcon 9's first-stage landing (G-FOLD) is convex optimization, **not a neural network**. It visually looks like a miracle of autonomy — and it is one, but its autonomy is built from math, not from learning.

## Speaker notes

This is the first and most important place in the lecture where we need to honestly separate "automation" from "a trained model": not everything that looks like autonomy is built from a neural network, and a significant share of this section's most impressive results doesn't use learning at all.

Geometric navigation is solved with no training whatsoever. Terrain traversability, building a map of a cave with no GPS — this is a classical algorithmic task: stereo vision, pose-graph optimization, fitting planes to a point cloud. This task was solved by classical methods long before deep learning became an engineer's tool, and moving it onto a neural network today would mean replacing a verifiable, deterministic algorithm with a less predictable one — with no gain that would justify such a swap. This is a direct, engineering-grounded criterion for "a trained model isn't needed here": the task is entirely geometric, and the physics of the soil and optics is known in advance.

The strongest example of this same principle lies outside surface navigation entirely. The Falcon 9 first-stage landing algorithm (G-FOLD, implemented as SCvx, CVXGEN) is a classical convex-optimization task, not a neural network. The decision of how much thrust to give the engines and when is settled by a mathematically provable algorithm, not by a model trained on examples of past landings. This is an important, honest distinction precisely because landing a rocket visually looks like a miracle of autonomy — and genuinely is one — but its autonomy is built from classical math, not from learning.

Recognizing an object against noise — where the classical approach can't manage alone. Spotting a scientifically interesting artifact against a background of uniform Martian dust is a task where features that aren't known in advance need to be extracted from the statistics of examples, rather than from an explicit physical model. This is where a lightweight trained model comes in — a random forest or a convolutional network — but this isn't a full-fledged deep network making an end-to-end decision; it's a narrow classifier embedded inside an otherwise classical pipeline. This boundary, named here in two paragraphs, will be broken down at the level of the mechanism itself on the next slide.

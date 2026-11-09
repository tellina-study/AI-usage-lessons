---
# Source: chapter/chapter-part3.md §§ 4.1 (three things under one word), 4.2 (entry and
# the question), 4.3 (five ways to get the data), 4.4 (which decision, and why here),
# 4.5 (the pipeline by name), 4.6 (real time before generation). Six parts of the stage
# description in canon order: (a) industry term → (b) the data and the question → (c) the
# ways → (d) the decision and its place → (e) the classical mode → (f) examples later in
# the section.
# Nine pipeline stages collapsed into three steps of the diagram: "no more than four steps
# in a row."
id: s68
local_id: "s68"
section: "4. 3D Scenes and Real Time"
type: assertion_visual
title: "What this work actually is, and how it was done without a model"
assertion: "3D graphics holds three different things under one word — the asset (an object made of four layers), the scene (a set of assets plus light and camera), and real time (not a property of the content but a budget: 16.7 milliseconds per frame at sixty frames per second, against minutes and hours per frame in film); the stage's decision is to lock in the shape before animation, cloth simulation, lighting, and render all build on top of it, and that is exactly why an error here gets more expensive at every step to the right"
source: "Mildenhall et al., ECCV 2020, arXiv:2003.08934; QuadGPT, arXiv:2509.21420"
chapter_ref: "chapter-part3.md §§ 4.1–4.6"
media: "assets/screenshots/s68-3d-model-stages.png"
media_needed: ""
media_note: "Wikimedia Commons, File:Hand-painted house 3D model stages.png, CC0 (public domain by the author's own dedication). Tier 2 (Wikimedia Commons). Four stages of one asset in one image: the geometry wireframe, the shaded form with no artwork, the unwrap with painted maps, and the finished object — exactly the four layers the slide lists. No source caption on the slide"
blocks:
  - {label: "Real-time frame budget", value: "16.7 milliseconds", note: "at sixty frames per second; geometry, light, shadows, effects, and the interface all have to fit inside it at once"}
  - {label: "Film frame budget", value: "minutes and hours", note: "the same object carries millions of polygons instead of tens of thousands"}
  - {label: "Gap between the two budgets", value: "four to five orders of magnitude", note: "it is what shapes the rest of the pipeline's whole design", key: true}
blocks_per_row: 3
timing_min: 0.6
in_bucket: false
method_steps: ["general description of the stage", "classical mode"]
form: []
vfy: false
status: собран
---

## Visible slide text

**The industry holds three different things under the words "3D graphics":** the asset, the scene, and the per-frame budget. The stage's decision is to lock in the shape before animation, cloth simulation, and lighting build on top of it.

## Speaker notes

3D graphics is the only modality of the evening where three different things walk around under one word, and confusing them is the first thing that derails any conversation about generative models in this area. They're worth separating right away and keeping apart for the whole section.

A 3D asset is an object, and it's made of layers, each with its own maker, its own schedule, and its own acceptance check in production. Geometry is the polygon mesh. The UV unwrap is cutting the surface along planned seams and laying it flat so artwork can be painted onto it. Materials and maps are color, roughness, reflectivity, micro-relief. The skeleton and rig are the bones, vertex weights, and controls by which the object is later moved. An asset only counts as done once all four layers are done.

A 3D scene is a set of assets plus whatever turns them into an image: lighting, camera, atmosphere, environment materials. The scene answers the question "what does this look like from here," and it answers it as many times as there are camera positions in the shot. Real time, unlike the first two, isn't about content at all — it's a budget. A frame either gets computed within its allotted time or it doesn't; at sixty frames per second it has 16.7 milliseconds, and every computation has to fit inside that window at once. A cinematic frame is computed in minutes and hours, and the gap of four to five orders of magnitude explains why the same object carries millions of polygons in film and tens of thousands in a game.

The stage's input comes in three kinds. The first is photographs of a real object or place plus the camera positions computed from them; the task is called reconstruction, and its question is stated exactly this way in the founding work on radiance fields: get any view, including ones nobody shot from. The second is a text description or a flat image; the task is called generation, and here there is no shot to check the result against, which means there's no notion of correctness at all — only fitness for purpose. The third is an already-built scene plus the engine's own service data: motion vectors and the depth buffer. This detail sets the third case apart from everything else in the lecture: the network doesn't guess motion from pixels here, it's told the motion. Where an image generator has only text at its input, here the input is geometrically exact service information, and that's exactly why the task is solved in a millisecond rather than half a minute.

The difference between the first and second input matters directly for judging the result. Reconstruction is verifiable: hold back some of the shots, reconstruct the scene from the rest, compare the predicted view with the held-back shot — you get a number. The industry measure is called peak signal-to-noise ratio and measures in decibels how closely the predicted picture matched the real one; twenty-seven decibels is a working level for a complex street scene, twenty-nine for an interior. Generation has no held-back shot, so it has no comparable measure.

The decision the stage makes deserves to be named on its own, because its place in the production order follows from it. The stage locks in the shape — and locks it in before every later piece of work builds on top of that shape. Animation deforms the mesh along the bones. Cloth simulation computes tension along the edges. Lighting is computed from the surface normals. Texture painting follows the UV unwrap. Each of these pieces of work treats the geometry as a given, so any error in the geometry travels right into everything downstream of it and gets more expensive at every step. Redoing the mesh after animation has already been rigged onto it means redoing the animation too. That's exactly why the 3D stage sits where it sits in production, and exactly why its unit of output is the most expensive in the evening's lineup of modalities: a flat frame only has to convince from one point of view, a video frame from one point of view over a span of a few seconds, while a 3D object has to be true from every side at once and in every pose — including poses other people will put it in six months from now, for a different scene.

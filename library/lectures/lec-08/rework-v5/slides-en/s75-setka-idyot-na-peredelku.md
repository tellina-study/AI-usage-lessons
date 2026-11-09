---
# Source: chapter/chapter-part3c.md § 4.17; chapter-part3.md § 4.5 (the pipeline by name).
# Quote — QuadGPT, Tencent Hunyuan together with the Hong Kong University of Science and
# Technology, arXiv:2509.21420 (2025): the authors of a commercial generator write this
# about their own product.
# A dedicated limitations slide, strict-in: the mechanism is named, the consequence is
# inevitable, the criterion "the generator doesn't close the work here" is checkable.
# Deviation from DECK-KARTA: the map uses the transliterated loanword for "mesh" — internal
# jargon banned by §5.21; the slide uses the plain RU word instead. English "mesh" is already
# the plain engineering term in both registers, so no further substitution is needed here.
#
# CONSOLIDATION 2026-10-29 (issue #301, task "section 4: 19→10-11"): the slide absorbed s75a
# ("What happens to the asset after 'eight seconds'") whole — following the same pattern as
# s71/s73/s74 in this section: blocks plus a pipeline diagram in one slide, visible text
# reduced to one punch line, both expanded prose versions stay in the speaker notes in full.
# The illustration was dropped: a slide with three blocks and a two-row diagram can't also
# carry a side picture. Minutes: 0.5 + 0.5 = 1.0 (no change to the section total).
id: s75
local_id: "s75"
section: "4. 3D Scenes and Real Time"
type: schema_pipeline
title: "The generated mesh goes in for rework: retopology, unwrapping, rigging"
assertion: "Geometry in 3D diffusion is born as an implicit function, and to get a polygon mesh out of the field, a regular grid is swept through space — from which equal polygon density, the absence of edge flow around bend points, and the impossibility of a production-ready UV unwrap follow inevitably; this isn't written by critics but by the authors of a commercial generator about their own product, and the practical upshot is that the generator closes the search for look and background objects, while preparing for production stays with people entirely"
source: "QuadGPT, Tencent Hunyuan and HKUST, arXiv:2509.21420 (2025); https://arxiv.org/abs/2509.21420"
chapter_ref: "chapter-part3c.md § 4.17"
media: ""
media_needed: "the picture was dropped during consolidation: blocks plus a pipeline diagram can't carry a side illustration. Previously: Wireframe 3D Model by Camille Kleinman (Wikimedia Commons, CC BY-SA 4.0) — exactly the defect the slide is about"
blocks:
  - {label: "What the generator delivers", value: "a first shape in a few seconds", note: "fit for viewing and for placement in the background"}
  - {label: "What's inevitably wrong with it", value: "uniform density, no edge flow, no unwrap", note: "follows from the surface-extraction method, not from an unfinished version", key: true}
  - {label: "How many stages stay with people", value: "three of nine — and the most expensive", note: "retopology, unwrapping, rigging; an auto-skeleton doesn't cancel this — bones are set onto the same mesh"}
blocks_per_row: 3
scheme:
  kind: dorozhki
  caption: "What happens to the asset after \"eight seconds\""
  steps_arrows: true
  rows:
    - label: "Generator"
      steps:
        - "shape in seconds"
        - "dense, unstructured"
    - label: "By hand"
      steps:
        - "retopology — mesh rebuilt from scratch"
        - "unwrap along seams"
        - "rigging — skeleton, vertex weights"
timing_min: 1.0
in_bucket: true
method_steps: ["the method's boundary", "mechanism", "refusal criterion"]
form: []
vfy: false
status: собран
---

## Visible slide text

**"An asset in eight seconds" and "ready to work with" are different things.** The three most expensive stages stay with people.

## Speaker notes

Here's the argument the section rests on, and it's confirmed by the authors of a commercial generator, not by its critics. A group releasing an industrial geometry-generation model writes in their 2025 paper that existing generative models produce quadrilateral meshes by first generating triangular ones and then merging triangles by certain rules, which usually gives quadrilateral meshes with poor topology; and that meshes are extracted by isosurface algorithms, which inevitably leads to unstructured, dense meshes.

The word "inevitably" is load-bearing here, and it's worth taking apart by mechanism rather than taking on faith. Geometry in 3D diffusion is born as an implicit function: the model outputs a field — distance to the surface, or density — and the surface is the set of points where the field takes a given value. To get a polygon mesh out of the field, a regular grid is swept through space, and a piece of surface is built in each cell. Everything else follows from this, and follows inevitably, not from an unfinished version.

First. Polygon density is set by the grid's step, not by the complexity of the shape. An artist places polygons densely where the shape bends and sparsely where it's flat. The grid places them uniformly everywhere. A flat wall ends up with as many triangles as a bent finger, and that isn't just wasteful — it makes the mesh unfit for manual editing.

Second. There is no edge flow. As a reminder of what that is: around bend points — a joint, a mouth, an eye, an eyelid — closed rings of edges are laid running across the direction of the bend, and the overall direction of the edges across the surface follows anatomy: along the muscles, along the folds, along the direction of deformation. This is exactly what determines how the object deforms during animation, and exactly what a human designs. In a mesh extracted by a grid, there are no such rings, and merging triangles into quadrilaterals by local rules doesn't create them — it creates quadrilaterals placed arbitrarily.

Third. There's no production-quality unwrap. You can't cut a dense, disconnected triangular mesh into pieces fit for manual editing: the seams will fall wherever, the scale of the artwork will drift, and painting color and micro-relief maps onto such an unwrap is pointless.

This is an exact analog of the boundary the course drew in the section on industrial use: a picture of an object isn't the same as a model of the object, and a mesh extracted by a grid isn't the same as a mesh fit for production. Both boundaries run along the same line — the difference between plausibility and fitness for purpose.

The practical upshot for the pipeline is exactly the one that was promised when we listed the nine stages. The generator closes concept, rough shape, and detailing — the entire search for the look. It closes background objects that aren't animated and don't come into a close shot: there the topology requirements drop along with the requirement of animation-readiness, and the generated mesh goes through as-is. Retopology, unwrapping, and rigging stay with people entirely, and the automatic rigging that's expanded over the past year to quadrupeds, birds, snakes, and aquatic creatures doesn't cancel this: it sets bones on top of whatever mesh already exists, along with all its defects. Retopology — a clean mesh is built from scratch on top of the one received, with edge loops around the joints, mouth, and eyelid. Unwrapping — along planned seams, so artwork can be applied without distortion. Rigging — a skeleton is set inside, and vertices are bound to the bones with weights.

From here follows a checkable formulation of the criterion for a working decision. If the object will be animated, deformed, or come into a close shot — the generator closes only the first third of the work, and the savings are counted from that third, not from the whole timeline. If the object sits motionless in the background — the generator closes the task entirely. That exact boundary runs between these two cases, and it sits in the requirements of the task, meaning on the engineer's side; the quality of the model won't budge it an inch.

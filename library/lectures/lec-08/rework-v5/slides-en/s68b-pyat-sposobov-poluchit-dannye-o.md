---
# Slide replaced 2026-10-29 (issue #301, task PUT-OT-ZAPROSA-K-REZULTATU.md):
# the former breakdown "five ways to get data about a real object" was dropped, and its
# minutes (0.3) were taken by a fun illustration — an owner instruction: "add more fun
# illustrations, like the one you made for how many people generate and how many select,
# for Coca-Cola" (s56, an icon grid). ATTEMPT #1 — an icon grid of 9 figures, 2 gold: BLOCKED
# by the build guard: `whole number 9 (< 10) — at this whole number the share reads as
# enumeration, not area` (piktogrammy.py, min_vsego=10). Nine stages — not to be stretched
# to a tenth just for the sake of form. A single-number slide (`figure:`) went up instead —
# also a form, never used anywhere else in the deck (see `RAZNARYADKA-FORM.md` §1), and
# also a large digit filling the frame, just without a grid of figures.
# The former slide's main observation — "the model didn't enter the pipeline whole: seven
# of the nine stages stayed exactly where they were" — isn't lost. The list of five classical
# ways to get the data is folded into one block at the bottom, all five named; photogrammetry
# and its byproduct — a sparse point cloud — are unpacked in full on the neighboring s68a,
# where they are the start of the second track of the path from request to result.
id: s68b
local_id: "s68b"
section: "4. 3D Scenes and Real Time"
type: assertion_visual
title: "The classical asset pipeline: what the model touched"
assertion: "Of the nine stages of the classical asset pipeline, a trained model touches two — it cheapens concept and blocking via a text description — while seven stages, the nine's most expensive, stay exactly where they were: retopology, unwrapping, texturing, rigging, animation, cloth simulation, render, and assembly; data about a real object is still obtained by the same five classical ways, and the model has only added a sixth — text"
source: "Mildenhall et al., ECCV 2020, arXiv:2003.08934; QuadGPT, arXiv:2509.21420"
chapter_ref: "chapter-part3.md §§ 4.1–4.6"
media: ""
media_needed: ""
figure:
  value: "2 of 9"
  unit: "pipeline stages touched by the model — concept and blocking"
blocks:
  - {label: "How data about the object is obtained", value: "photogrammetry · laser scanning · manual modeling · motion capture · ready-made libraries", note: "unchanged, plus a sixth input — text; 7 of 9 stages untouched: retopology, rigging, render…", key: true}
blocks_per_row: 1
timing_min: 0.3
in_bucket: false
method_steps: ["general description of the stage", "classical mode"]
form: []
vfy: false
status: собран
---

## Visible slide text

## Speaker notes

The classical 3D asset pipeline has nine stages, grouped into three segments: finding the look (concept, blocking, sculpting), preparing for production (retopology, unwrapping, texturing, rigging), and use (animation and cloth simulation, render and assembly). Naming them one by one matters for one reason — the generator's boundary of applicability runs exactly along this list.

A trained model touches two of the nine stages, and both are in the first, cheapest segment. Concept — an image or sketch used to decide "we do this or we don't" — can now be gotten from a text description in seconds instead of hours of sketching. Blocking — a rough shape made of boxes and spheres used to check silhouette and proportions — is sped up the same way: you see the rough shape sooner than before. Beyond that the model touches nothing: seven of the nine stages — precisely the seven most expensive — stay exactly where they were before it.

Why these particular seven don't give way. Retopology requires knowledge of anatomy and of how the object will move — a clean mesh is rebuilt from scratch on top of the sculpted shape, with edge loops around the joints. Unwrapping and texturing require discipline in laying out seams. Rigging — the skeleton and vertex weighting — is set on top of the finished mesh, and if the mesh wasn't built to anatomy, the bones end up wherever is convenient for the algorithm, not wherever the object actually bends; the automatic skeleton generators have been touting since 2026 doesn't close this stage, it sits on top of it. Animation, cloth simulation, and the final render all treat the geometry as a given — any error in it travels right and gets more expensive at every step.

Data about a real object is still obtained by the same five classical ways. Photogrammetry — the object is walked around with a camera and shot in hundreds of overlapping frames, and the calibration also yields a sparse point cloud as a byproduct. Laser scanning — the device measures distance directly, more precise on shape and poorer on color. Manual modeling — the only way to get an object that doesn't exist. Motion capture gives not the shape but how the object moves. Ready-made libraries are the cheapest and narrowest path. The model has added a sixth input — a text description — to these five, and cheapened the first of the five, photogrammetry: a set of photographs turns into a usable scene in minutes instead of days, rather than hours of manual processing. It hasn't touched the other four ways at all, and not one of the six inputs has added a single dimension: a laser scanner still measures size in meters just as it always has, and the output of a generative input is only plausible — and that's an asymmetry that won't be closed by the next version of the model, because it follows from how the method is built, not from its quality.

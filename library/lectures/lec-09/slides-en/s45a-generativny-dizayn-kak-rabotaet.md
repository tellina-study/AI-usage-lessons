---
id: s45a
local_id: s3-06-2
section: "3. Design and new capabilities"
type: case_study
title: "The five steps of the search"
assertion: "The engineer sets the loads and constraints; the algorithm searches through geometry within them on its own and delivers a finished shape"
source: "[NASA NTRS (citations/20230013955, Ryan McClelland)](https://ntrs.nasa.gov/citations/20230013955)"
media: "assets/razdel-3/generative-design/ntrs-slide10-how-it-works-process-diagram.jpg"
media_hero: true
media_hero_target: 0.50
media_hero_wcap: 9.5
media_caption: "Slide 10 of the NASA Goddard presentation: input mesh → topology optimization → finished geometry"
media_needed: "already downloaded (Tier 1, NASA NTRS). A large process illustration, added at the owner's instruction (Phase 9, issue #317) — the official diagram was downloaded earlier but had not been used large on any slide."
in_bucket: false
status: draft
---

## Visible slide text

**Five steps, not one leap from task to answer.** From loads and constraints at the input to a finished shape at the output.

**The engineer sets the goal, not the lines.** The algorithm finds the shape within the given boundaries.

1. Loads and constraints → 2. Spatial mesh → 3. Topology optimization → 4. Checking the result → 5. CAD model

## Speaker notes

The slide shows the official generative-design workflow diagram from NASA Goddard's presentation, authored by Ryan McClelland. It breaks down exactly what has already been named: here the model does not predict a number for an already-given configuration, the way the rocket engine surrogate does — it produces the geometry itself.

The process runs in five steps. First, the engineer sets the initial data: the loads the part must withstand, the mounting points that must not be touched, and the constraints on mass and manufacturability. Second, the space where the part's material can be located is divided into a fine spatial mesh, inside which the algorithm will search for a shape. Third, topology optimization is launched: the algorithm iteratively decides in which cells of the mesh material is needed and in which it can be removed, all while holding every goal set in the first step. Fourth, the intermediate result is checked against the original requirements. Fifth, the found shape is reconstructed into an ordinary CAD model, which can then be handed off to manufacturing.

This is the mechanical difference between a surrogate model and generative design, named on the neighboring slide as "number versus geometry": a surrogate answers the question "how good is this specific configuration," while generative search, shown here step by step, answers a different question — "what geometry can even exist here" — searching through options within the boundaries the engineer set, rather than evaluating one proposed option.

The organic shape, unfamiliar to the eye, that results from the fifth step is not a side effect of the algorithm, but a direct consequence of the fact that it is not bound by the straight edges and symmetry familiar to an engineer: it searches for a shape that satisfies all the goals at once, regardless of what the familiar part of the same purpose usually looks like.

---
# Source: chapter/chapter-part3c.md § 4.18; chapter-part3.md § 4.3 (a laser scanner
# measures size the same way it always has).
# A dedicated limitations slide, strict-in: the criterion "the model isn't the right tool
# here" is formulated in a checkable way.
# Deviation from DECK-KARTA: the map's heading is "There are no technical specs" — the
# slide names the missing thing with a word that needs no unpacking (§5.20).
id: s76
local_id: "s76"
section: "4. 3D Scenes and Real Time"
type: assertion_visual
title: "A generated object has no dimensions"
assertion: "The shape a generator outputs exists in dimensionless coordinates: it is \"this\" in proportion and nothing in particular in size, and the scale is assigned afterward by a human, by eye or against a neighboring object; an object output from the description \"load-bearing bracket\" looks like a bracket and carries neither a load, nor a material, nor a tolerance — not one feature letting you check whether it would hold anything — and the distance between such a generator and a computer-aided-design system is qualitative, not quantitative"
source: ""
chapter_ref: "chapter-part3c.md § 4.18; chapter-part3.md § 4.3"
media: ""
media_needed: "no real image was found at any of the six tiers. What was needed was a pair — 'an engineering drawing with dimensions and tolerances next to a generated shape of the same object' — and no such pair exists under a free license, because the second half of the pair requires running a commercial generator and publishing its output. Tried: (1) og:image of Autodesk and Dassault pages on generative design — decorative banners; (2) Wikimedia Commons — 'engineering drawing dimensions,' 'CAD parametric model,' 'technical drawing tolerances' return either digitized 1890s textbooks or someone else's exam sheets with no relevance to the topic; (3) developer announcement pages for generators — output is covered by terms of use; (4) video thumbnail — no canonical clip exists; (5) web archive — the same protected pages; (6) image search — everything under commercial license. The slide stays without a photo: the two columns are its own subject"
media_note: ""
blocks:
  - {label: "What coordinates does the shape live in", value: "dimensionless", note: "proportions exist, size doesn't"}
  - {label: "Dimensions fit for a drawing", value: "not one", note: "the model is trained on shapes; there were no measurements in training, and there's nowhere for a dimension to come from", key: true}
  - {label: "Of the five classical inputs, the model touched", value: "one, and added a sixth", note: "a laser scanner measures size the same way it always has"}
blocks_per_row: 3
scheme:
  kind: dorozhki
  caption: "Two tools at the same spot in the pipeline: one has no quantities, for the other quantities are the whole point"
  steps_arrows: true
  rows:
    - label: "Shape generator"
      steps:
        - "input — a text description"
        - "output — a surface in seconds, dimensionless coordinates"
        - "the human assigns scale by eye"
    - label: "Design system"
      steps:
        - "input — parameters and relations between them"
        - "dimensions, tolerances, material — part of the model itself"
        - "output — a drawing used to manufacture and accept the part"
timing_min: 1.0
in_bucket: true
method_steps: ["the method's boundary", "refusal criterion"]
form: []
vfy: false
status: собран
---

## Visible slide text

**Shape comes before calculation — the selection criterion stays with the human.** A "load-bearing bracket" looks like a bracket, but carries no load, no material, and no tolerance.

## Speaker notes

The second boundary is shorter and harder than the first. A generated object has no dimensions, and that's worth spelling out literally, because an engineering audience usually assumes the dimensions are there somewhere, just not shown on screen.

The shape a generator outputs exists in dimensionless coordinates: it is "this" in proportion and nothing in particular in size. The scale is assigned afterward, by a human, by eye or against a neighboring object in the scene. There is no dimension in the output that can be put on a drawing, and there's nowhere for one to come from: the model is trained on shapes, not on measurements. It has seen millions of objects whose training data carried not a single dimension, and it learned what such objects look like, not what they measure.

What follows from this matters more to an engineering audience than the fact itself. A 3D generator doesn't replace a computer-aided design system, and the distance between them is qualitative, not quantitative — meaning it won't shrink as the model gets better. A design system operates on parameters with tolerances, relations between those parameters, and checks: change the diameter, the fit recalculates; break a tolerance, you get a warning. A generator operates on the plausibility of a surface, and there isn't a single entity inside it you could assign a tolerance to.

This is the working criterion for "the model isn't the right tool here," and it fits in one line: wherever the result is checked by calculation, a shape generator stands before the calculation, not instead of it. It's suited to the stage where you're sorting through looks and discarding failed concepts; it's unsuited to the stage where the shape becomes a commitment to physics.

Worth placing next to it a counterexample from earlier in the evening: it shows what a correctly built form-automation looks like. Generative design, which in 2016 made the bionic partition for an airplane, works like this: an algorithm sweeps through shapes, and the selection criterion is set by physics — mass, stiffness, load — and checked by calculation at every step. The win there came from the criterion that was put in place; the sweep itself could have been anything, and the model didn't provide it. A 2024 generative model contains no selection criterion at all: the criterion stays outside, with the human, and in 3D that human additionally has to assign a scale that isn't in the output.

There's a third detail that ties this boundary to the stage description. Of the five classical ways of getting source data — photogrammetry, laser scanning, manual modeling, motion capture, ready-made libraries — the generative model has substantially cheapened one and added a sixth, a text description. A laser scanner measures size the same way it always has. This isn't an accident or a temporary state of affairs: a scanner answers the question "what is this object," while a generator answers "what does an object of this kind look like," and those are two different questions that no improvement to the model can reduce one to the other.

Separately — about a temptation that comes up for almost everyone here. You can import the output shape into a design system, and it will import — the file opens, the object appears in the scene, the dimensioning tool applies to it. From this it's easy to conclude the object does, after all, have dimensions. It doesn't: the dimensioning tool will measure whatever scale the human assigned on import, and show that number with the same confidence it would show a real measurement. A design system doesn't distinguish an assigned scale from a measured one — it doesn't know where the geometry came from at all. Checking "a dimension appeared on screen" confirms nothing here, and this is exactly where plausibility most successfully passes itself off as conformance.

For practice, this leads to a simple check before putting a generator to work. Ask yourself what the result will be checked against. If the check is a human glance ("looks like what I wanted"), the generator is suited to the job. If the check is a calculation, a measurement, or comparison against a drawing, the generator comes before that check and replaces nothing in it; and if someone proposes replacing that check with the generator, they're proposing to replace conformance with plausibility.

Worth not forgetting the other half of this picture: a shape generator delivers twenty variations of a look in half an hour where there used to be one sketch in half a day, and it delivers an object that doesn't exist in nature — with not a single photograph as input. The output shape is entirely fit for viewing and for placement in the background. There's no ban on the tool here; there's an exact place where it stops.

It stops at the relations between parameters. In a computer-aided design system, the model is dependencies: change the diameter, the fit recalculates, the tolerance changes. In the output surface there's nothing to change, because no relations are recorded in it. And the selection criterion stays outside, with the human — and in 3D that human additionally has to assign a scale that isn't in the output.

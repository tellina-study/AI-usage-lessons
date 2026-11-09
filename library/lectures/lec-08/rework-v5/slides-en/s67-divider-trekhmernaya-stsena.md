---
# Source: chapter/chapter-part3.md §§ 4.1, 4.4 (why this modality comes second-to-last
# and why its output unit is the most expensive). The case name on the divider matches
# s69's title verbatim — requirement of §5.16 of the form canon.
# Deviation from DECK-KARTA: the map records the tag as "frontier". On the slide it reads
# "leading edge": the calque is banned by §5.21.
id: s67
local_id: "s67"
section: "4. 3D Scenes and Real Time"
type: section_divider
title: "Section 4. 3D Scenes and Real Time"
assertion: "The evening's fourth modality is the most expensive per unit of output: a flat frame only has to convince from one point of view, a video frame from one point of view and over the span of a few seconds, while a 3D object has to be true from every side at once and in every pose — including poses other people will put it in six months from now, for a different scene; the requirement of completeness from every side pushes the unit cost up by an order of magnitude"
source: ""
chapter_ref: "chapter-part3.md §§ 4.1–4.7; chapter-part3b.md §§ 4.8–4.14"
media: "assets/screenshots/s67-sphere-vegas.jpg"
media_needed: ""
media_note: "Wikimedia Commons, File:The Las Vegas Sphere, Nevada (53349695459).jpg, CC BY-SA 2.0, author Harold Litwiler, shot 2023. Tier 2 (Wikimedia Commons, direct download via upload.wikimedia.org with User-Agent and Referer headers). Bottom 48 pixels cropped off: a visible attribution mark sat there. No source caption on the slide — provenance lives here and in images-log.md"
blocks:
  - {label: "Breakdowns with a traceable outcome", value: "1", note: "and strictly speaking it isn't even a 3D case — the breakdown's own slide says so"}
  - {label: "Mentions", value: "3", note: "the LED stage, the asset generator, the described environment"}
  - {label: "Cases with both sides costed", value: "not one", note: "and that is information about the modality's maturity, not a gap in preparation", key: true}
timing_min: 0.0
in_bucket: false
method_steps: ["divider"]
form: []
vfy: false
status: собран
---

## Visible slide text

# Section 4. 3D Scenes and Real Time

**We just counted the ratio of tries to a keeper on video. Here the unit of output is the most expensive in the lineup:** the object has to be true from every side at once and in every pose — including poses other people will put it in six months from now, for a different scene.

**1 breakdown · 3 mentions · the leading edge.** Not one case with both sides costed — and that is information about the modality's maturity.

In order: **Breakdown: "The Wizard of Oz" at Sphere — over 90% of the frame touched**

## Speaker notes

The section on moving image closed on a hidden cost of selection: three hundred tries for one keeper splice in "Air Head," hundreds of takes down to a few dozen in the Toys "R" Us edit. The 3D stage is next in the production order and the last of the evening's generative modalities. It differs from the previous three in one property, and that property is worth holding onto for the whole section: here the output doesn't have to be convincing from some one point of view — it has to be true from every side at once.

The difference isn't rhetorical, it converts directly into money. A flat image is checked with one glance: if the picture looks good in the form it will be shown in, the work is done. A video frame is checked with one glance stretched over a few seconds — the requirement adds only continuity over time. A 3D object is checked from who-knows-where: it will be placed into a different scene, under different light, in a different pose, possibly by different people, six months after it was delivered. So it counts as "done" not when it looks good, but when all of its layers are done — geometry, the UV unwrap for the artwork, materials, and the skeleton — and a broken last layer wipes out the value of the first three: a beautiful shape that tears at the elbow on the first bend doesn't go into production.

From this follows both the stage's place in the production order and its main property. The 3D stage decides what the shape will be before every later stage builds on top of that shape: animation deforms the mesh along the bones, cloth simulation computes tension along the edges, lighting is computed from the surface normals, texture painting follows the UV unwrap. Any error in the geometry travels right into everything downstream of it and gets more expensive at every step. Redoing the mesh after animation has already been rigged onto it means redoing the animation too.

The second thing that has to be said up front concerns the state of our evidence on the subject, and it's more honest to say it now than as a caveat at the end of the section. In the evening's other four modalities there are cases where both sides are costed: what it cost without the model and what it costs with one. In 3D, there is not a single such case in the open sources. How long the same object takes a modeler isn't named anywhere; there is no per-unit price for 3D generation at all. The modality is young — industrial use went mass only in 2024–2026, and measurements worth citing haven't been published yet.

This shapes the section's structure. The lean toward mechanism here is deliberate: 3D has an excellent, measured, peer-reviewed mechanism and a very poor record of cases. That imbalance can't be papered over with multipliers from press pages — a multiplier of the form "a thousand times faster than an artist" comes from dividing a measured number by an estimate pulled out of thin air. The absence of public measurements for a technology that is two years old is itself useful information: it says more about maturity than any beautiful number of unknown origin.

The section's only case with a traceable outcome is the screening of "The Wizard of Oz" on the spherical screen in Las Vegas. It has two inconvenient features, and both will be named on its own slide: strictly speaking it isn't a 3D case, and it's missing a significant part of what the form of a detailed breakdown requires. It's here because the modality has no other case with a traceable outcome, and because it's about the same property — about what counts as already shot.

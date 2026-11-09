---
id: s45b
local_id: s3-06-3
section: "3. Design and new capabilities"
type: case_study
title: "The organic part"
assertion: "The part the algorithm found looks grown, not drafted — it has no straight edges or symmetry at all"
source: "[NASA NTRS (citations/20230013955, Ryan McClelland)](https://ntrs.nasa.gov/citations/20230013955)"
media: "assets/razdel-3/generative-design/nasa-evolved-structure-bracket-closeup.jpg"
media_hero: true
media_hero_target: 0.50
media_caption: "Close-up of the geometry found by the algorithm, NASA Goddard"
media_needed: "already downloaded (Tier 1, NASA Goddard). A large illustration of the part, added at the owner's instruction (Phase 9, issue #317) — the photo was downloaded earlier but had not been used large on any slide; this photo was chosen over `nasa-excite-bracket-three-manufacturing-variants.jpg` — that file already carries a role on the neighboring `s45` slide (as a small side illustration), and repeating the same shot large nearby would read as a repeat, not a new angle."
in_bucket: false
status: draft
---

## Visible slide text

**A close-up of the very geometry the algorithm found.** Branching, uneven ribs instead of a flat panel and a straight stiffening edge.

**Not one straight edge where an engineer would normally draw a straight line.** Material is removed exactly where it's not needed for the load — not wherever is convenient for a cutting tool or mill.

## Speaker notes

The photo is a close-up of a part whose geometry was found by NASA Goddard's generative search — the same method and the same organization as on the neighboring slide with the five process steps, except here it's not the process but its result shown up close.

The difference from an ordinary engineered part is visible immediately, without explanation: where an engineer, designing a bracket by hand, would normally leave straight edges, flat panels, and symmetric stiffening ribs — because that's convenient to draw and easy to calculate load on by hand — this part has almost no straight lines at all. The ribs branch and taper unevenly, following not drafting logic but the shape the load actually travels through. Material is removed exactly at the points that carry no load, and left exactly where the load actually passes, and altogether this gives a shape that visually reads as "grown," not drafted with a ruler.

This is not an aesthetic choice by the algorithm — it is a direct consequence of how it searches for a solution. Classical design moves from familiar ready-made shapes (a beam, a panel, a rib) toward fitting them to the load; generative search moves in the opposite direction — from the load and constraints themselves toward any shape that satisfies them, regardless of whether it's recognizable to an engineer's eye or not. It is precisely for this unfamiliarity that the developers of the method pay a separate cost, named on the neighboring slide: organic geometry requires more engineering time to check before a part is cleared for flight.

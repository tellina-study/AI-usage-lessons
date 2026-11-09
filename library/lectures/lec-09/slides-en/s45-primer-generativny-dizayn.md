---
id: s45
local_id: s3-06
section: "3. Design and new capabilities"
type: case_study
title: "Example: NASA Goddard generative design of structures"
assertion: "NASA Goddard's generative design produces a part's geometry itself — not evaluating a finished one, but creating a new one"
source: "[NASA NTRS (citations/20230013955, Ryan McClelland)](https://ntrs.nasa.gov/citations/20230013955) · [Fast Company](https://www.fastcompany.com/90851698/nasas-new-generative-ai-designed-parts-look-like-theyre-from-an-alien-starship)"
media: "assets/razdel-3/generative-design/nasa-excite-bracket-three-manufacturing-variants.jpg"
media_needed: "already downloaded (Tier 1, NASA)."
graf: "b"
blocks:
  - {label: "Cost of manual CAD design", value: "iteration after iteration by hand", note: "four goals at once (mass, stiffness, heat, manufacturability) — hard for intuition"}
  - {label: "Cost of unfamiliar geometry", value: "harder to check before flight", note: "an organic shape needs more engineering time to analyze"}
  - {label: "Classical mode", value: "manual CAD, widely practiced", note: "no independently published number of its own — hours or cost per part"}
  - {label: "Model (Generative Design, NASA Goddard)", value: "a claimed 10x reduction", note: "the method author's own internal estimate, NOT an independently confirmed fact — applied on the Habitable Worlds Observatory", key: true}
in_bucket: true
status: draft
---

## Visible slide text

**The section's fourth breakdown — the exception to the 'up to three' rule.** A qualitatively new contribution: the model does not predict a number for an already-given configuration — **it produces the geometry itself.**

*Generation on structured data — the first time the 'generation × structured data' cell in the lecture's grid is filled.*

## Speaker notes

This breakdown is the fourth in the section, present by an explicit, named exception to the "up to three detailed breakdowns per section" rule: it carries a qualitatively different type of model contribution than the section's previous three breakdowns.

Manual structural design in CAD — an engineer fits a part's geometry by hand, iteration after iteration, holding mass, stiffness, thermal characteristics, and manufacturability all at once. Holding four goals at once by hand is a hard task for intuition: an overly conservative geometry saves time but pays with extra mass, and on the frontier every extra kilogram costs a separate slot in the cargo bay. The flip side of the cost: the geometry proposed by automated search is often unfamiliar to an engineer's eye and may be harder to manufacture or test.

Classical mode (column b): manual design is well known, but it has no independently published number of its own comparable to the model's claimed effect.

Model: Generative Design, a NASA Goddard program, method authored by Ryan McClelland. Unlike the Raptor surrogate, which predicts the characteristics of an already-given configuration, generative design produces the geometry itself: the algorithm explores the space of possible shapes, simultaneously optimizing mass, stiffness, thermal characteristics, and manufacturability, and delivers the engineer a finished shape that was not designed by hand step by step. It is applied right now to several real NASA mission concepts, including the Habitable Worlds Observatory — a future flagship telescope whose mission has not yet launched.

The claimed effect — a tenfold reduction in development time and cost — is the method author's own internal estimate, not an independently confirmed fact, and that honest caveat needs to be stated explicitly. Final engineering qualification and testing remain a separate classical step before flight — the same principle as with Raptor. Three selection conditions: the first is in the strongest form among the section's four breakdowns (without the model, the geometry would not have arisen the way it arose); the second is unconditional; the third is column b, with the caveat about an internal estimate.

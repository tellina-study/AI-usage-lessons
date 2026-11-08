---
id: s21
type: assertion_visual
duration_min: 2.8
assertion: "What's mature is an LLM as an interface to deterministic operations; generating geometry from text, in 2026, is a concept and an early beta."
learning_goal: "Landscape 2026 (marketing vs. maturity); cascade: ≤3 numbers / ≤4 names; the Autodesk quote not given verbatim"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.2 — Landscape 2026: marketing versus maturity"
references: [autodesk-bernini, autodesk-neural-cad]
visual:
  pattern: comparison
  primary: "Two maturity columns in an Ocean rounded box: the mature layer of LLM copilots vs. the immature layer of text-to-CAD; gold on Bernini's own vendor self-rating"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-column maturity contrast via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `terminal` (LLM copilot as interface), `flask-conical` (experimental neuro-CAD), 32px inline, recolored to Primary mid `#065A82`"
    caption: "Landscape 2026: a mature interface vs. immature geometry generation"
interaction: none
---

# Mature: LLM as an interface; geometry generation: a beta

## Assertion

What's mature is an LLM as an interface to deterministic operations; generating geometry from text, in 2026, is a concept and an early beta.

## Visual

Two columns in an Ocean rounded box. Left, heading "Mature layer: LLM as an interface" (icon `terminal`, Primary mid): "a text prompt → CAD commands over existing deterministic operations · under the engineer's control · e.g. Autodesk Assistant, Siemens Design Copilot." Right, heading "Immature layer: text-to-CAD / neuro-CAD" (icon `flask-conical`, Teal `#028090`): "3D geometry generation from text · e.g. Zoo.dev, Autodesk Bernini · commercial availability of neuro-CAD stated as 'upcoming,' no date." A gold plate (`#F0AB00` bold, 16pt): "The vendor itself labels Bernini 'strictly experimental, not for public use' — an honest maturity signal against the marketing 'AI designs for the engineer.'" No more than four product names on the slide.

## Speaker notes

Let's split the landscape into two layers that differ greatly in maturity. The first — LLM copilots on top of CAD. Autodesk Assistant in Fusion turns a text prompt into commands — "split this body," "extrude this face" — and can generate and execute scripts via the API. Siemens Design Copilot is an assistant built on the vendor's own knowledge, with a claimed auto-generation of a significant share of two-dimensional drawing views, based on an analysis of a corpus of user drawings. Mastercam Copilot is an assistant for machining programming. This is a relatively mature layer: an LLM as an interface to existing deterministic operations, under the engineer's control.

The second layer — text-to-CAD and neuro-CAD — and it is immature. Zoo.dev is an open text-to-CAD: text into 3D, exported to STEP or STL. Autodesk Project Bernini is a research generative 3D model, trained on the order of ten million 3D shapes; an essential detail: Autodesk itself labels Bernini as "strictly experimental, not for public use" — an honest maturity signal that contrasts with the marketing "AI designs for the engineer." Autodesk Neural CAD, with its announced goal of editable geometry from a single prompt, has its commercial availability stated as "upcoming," with no exact date — that is, not yet a generally available product. The academic frontier is active, but these are research works, not production tools.

Conclusion on the landscape: what's mature is an LLM as an interface to deterministic operations. Generating geometry from text, in 2026, is a concept and an early beta — confirmed even by the vendor's own labeling of Bernini.

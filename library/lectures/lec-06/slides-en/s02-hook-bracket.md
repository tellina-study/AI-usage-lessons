---
id: s02
type: assertion_visual
duration_min: 4
assertion: "This 'organic' bracket was not designed by generative AI but by a deterministic optimizer — a formulation going back to 1904."
learning_goal: "Concept-reveal hook: debunking 'AI came up with the part' → entry into the central question"
learning_outcomes: [LO1]
chapter_ref: "§0 — The bracket mistaken for the work of a neural network"
references: [autodesk-gm-bracket, michell-1904]
visual:
  pattern: assertion_visual
  primary: "Photo of the GM seat bracket (openwork 'organic' shape) in an Ocean rounded box; question overlay 'What kind of AI designed this?' → reveal block 'None. Deterministic optimization, 1904'"
  illustration:
    type: stock
    sources:
      - "Autodesk customer story — GM generative design seat bracket (https://www.autodesk.com/customer-stories/general-motors-generative-design)"
      - "Wikimedia Commons CC-BY — 'generative design bracket' / 'topology optimization' categories as fallback"
    caption: "GM seat bracket (Autodesk, 2018) — concept-reveal hook"
interaction: none
---

# What kind of AI designed this bracket?

## Assertion

This "organic" bracket was not designed by generative AI but by a deterministic optimizer — a formulation going back to 1904.

## Visual

At the center of the slide — a photo of a seat-mounting bracket: a light, openwork, branching structure, visually indistinguishable from a shape "grown" by artificial intelligence, in an Ocean rounded box (~55% of the width). Above the photo, in large type (28pt bold) — the question "What kind of AI designed this?" On the right — a reveal block: "No generative AI at all. A deterministic numerical optimizer. The problem statement — the year 1904." Gold highlight (`#F0AB00`) on "1904." At the bottom, a small fact caption: "8 parts → 1; mass −~40%; >150 variants evaluated."

## Speaker notes

Before us is a specific part that has become a canonical industry example: a seat-mounting bracket, designed by General Motors together with Autodesk and shown in 2018. Eight separate parts of the previous assembly were replaced by one; the chosen variant turned out to be about 40% lighter and noticeably stronger than before; the program generated more than 150 alternative variants, from which the engineer chose one.

The natural question an engineer asks on first seeing such a part: what kind of AI designed it? And here comes the first debunking turn. The correct answer: no generative AI at all. No neural network "came up with" this shape. It was produced by a deterministic numerical optimizer, solving a problem precisely posed by an engineer — minimize mass subject to a constraint on stresses and under given loads. The mathematical statement of this problem goes back to the work of the Australian engineer Anthony Michell in 1904 — a century before diffusion models and large language models existed.

This distinction is not pedantry. If you believe AI "came up with" the part, you lose your grip on the fact that the result is fully determined by physics and by the statement of the problem: the same inputs will give the same result, and any error in the statement will give a mathematically flawless but unusable answer. If instead it is clear that an optimizer stands before the engineer, it is clear where to look for the cause of a failure, and that responsibility for the statement and for the verification lies with the engineer. The whole rest of the lecture unfolds this distinction across the six classes of technology that marketing lumps together under the word "AI."

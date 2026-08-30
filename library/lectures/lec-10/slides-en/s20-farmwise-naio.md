---
id: s20
type: failure_case
duration_min: 2
assertion: "FarmWise wind-down 2025; Naïo €4M → €2.4M (–40%) judicial recovery 2025. Cause: a CV stack trained under greenhouse conditions breaks in dust / shadow bias / variable lighting. AP2b — mechanical weeders as a deterministic alternative."
learning_goal: "AP2b genuine non-AI alternative vs AP2a"
learning_outcomes: [LO5]
chapter_ref: "§2.5 Part 2 — Strict-in F5 FarmWise + Naïo"
references: [farm-progress-2025, arxiv-2508-shadow-bias, mdpi-agri-2024]
visual:
  pattern: cause_alternative_2col
  primary: "Left — failure causes (CV in dust + shadow bias + variable lighting); right — AP2b alternative mechanical weeders (Lemken, Kverneland)"
---

# FarmWise wind-down + Naïo recovery — the open environment breaks CV

## Assertion

FarmWise wind-down 2025; Naïo €4M → €2.4M (–40%) judicial recovery 2025. Cause: a CV stack trained under greenhouse conditions breaks in dust / shadow bias / variable lighting. AP2b — mechanical weeders as a deterministic alternative.

## Visual

A two-column layout.

**Left column (50%) — Failure causes:**

At the top — a photo of a FarmWise robot (or Naïo Orio) in the field with visual occlusion from dust. Caption 12pt italic: «FarmWise / Naïo — the structural cause of the wind-down».

Below the photo — 3 mini-cards in an Ocean rounded box:

1. **Dust (visual occlusion)** — degradation of image quality from the CV cameras
2. **Variable lighting** — cloud shadows change the contrast within minutes
3. **Shadow bias** — the model classifies shadows as vegetation (arXiv 2508.19511)

Below the mini-cards — the financial trajectory:
- **FarmWise** — wind-down 2025; machines in the fields without service
- **Naïo Technologies** (Toulouse) — judicial recovery June 2025
- Revenue: €4M (2021) → €2.4M (2024), **–40%** ★ gold accent

**Right column (50%) — AP2b alternative:**

A photo of a mechanical weeder (Lemken Steketee EC-Weeder or Kverneland Onyx) framed in an Ocean rounded box. Caption: «Mechanical weeder · deterministic robust».

Below the photo — a callout in a Teal-tint box:
- **AP2b. A genuine non-AI alternative.** When a CV stack structurally can't withstand open-environment conditions — mechanical weeders give a deterministic robust solution **without an AI stack**.
- Lemken Steketee EC-Weeder; Kverneland Onyx
- Less «smart», but: robust to dust / rain / shadows; no firmware updates; no cloud dependency; no CV failure modes

Below the callout — the **critical distinction AP2a vs AP2b**:
- **AP2a** = a different class of AI (sensor-fusion instead of CV)
- **AP2b** = NON-AI (mechanics instead of AI)
- Don't confuse them!

Footer 12pt italic: «Sources: Farm Progress 2025; arXiv 2508.19511 (shadow bias); MDPI Agriculture systematic review 2024».

## Speaker notes

The second L2 failure, structurally close to Monarch but in a different niche: FarmWise and Naïo Technologies.

FarmWise — a CV weed robot, founded in 2016, having raised more than thirty million dollars — announced a wind-down in 2025. Per reports, customers were left in limbo, machines in the fields without service support. Naïo Technologies — a French company from Toulouse, autonomous weeding robots Oz, Dino, Orio — entered judicial recovery, the French equivalent of Chapter 11, in June 2025. Naïo's financial trajectory: revenue of four million euros in 2021, two point four million in 2024 — a fall of about forty percent.

The structural cause of both failures is one and the same, and it's documented in the academic literature: an arXiv paper from August 2025 «Weed Detection in Challenging Field Conditions: Semi-Supervised Framework for Overcoming Shadow Bias» and a MDPI Agriculture review from 2024. Computer-vision models trained under greenhouse conditions perform poorly in a real field. The concrete degradation mechanisms: dust creates visual occlusion of the cameras. Variable lighting — cloud shadows change the contrast within minutes. Shadow bias — the model learns to classify shadows as vegetation; this is a typical error with an insufficiently diverse dataset. Morphological similarity of crop plants and weeds at early growth stages. Image-quality degradation leads to classification errors — a drop in overall accuracy from the claimed ninety percent in tests to fifty-to-sixty in a real field. This is precisely the figure that pushes the farmer's unit economics into the red.

And here is the critical distinction we'll use in the following sections. AP-two-b — a genuine non-AI alternative. When a CV stack structurally can't withstand open-environment conditions — mechanical weeders give a deterministic robust solution without an AI stack. Lemken Steketee EC-Weeder; Kverneland Onyx — this is less "smart", but deterministically robust to dust, rain, shadows; requires no firmware updates; doesn't depend on cloud connectivity; has no CV failure modes. This is a categorically different class of alternative, distinct from the one we'll examine a slide later — in the case of Cognitive Pilot and ITELMA.

And the key distinction, without which a student will draw the wrong conclusion. AP-two-a and AP-two-b are different things. AP-two-a — an architecture choice within the AI domain: CV versus sensor-fusion AI. AP-two-b — a choice of a non-AI alternative: mechanics instead of AI. Don't confuse them. A student who read only AP-two-a might erroneously conclude that AI always wins if the class is chosen correctly. A student who read only AP-two-b might erroneously conclude that AI is always worse than mechanics. Both conclusions are wrong. The correct conclusion — the choice depends on the nature of the environment and the character of the task, and the engineering skill is to recognize which of the two cases is before us in a concrete situation.

## Sources

- Farm Progress (2025).
- arXiv 2508.19511 (August 2025) — shadow bias.
- MDPI Agriculture systematic review (2024).

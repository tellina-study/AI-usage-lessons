---
id: s11
type: schema_chain
duration_min: 2
assertion: "ML optimizes on the denominator (efficiency 5-15%). The gap is in the numerator (LED energy vs free sunlight): 0.5 × 0.7 × 0.3 ≈ 10.5% end-to-end. This gap is two orders of magnitude; no model will close it."
learning_goal: "5-Why analysis as a method; AP1 operationally"
learning_outcomes: [LO5]
chapter_ref: "§1.4 Part 1 — 5-Why physical-economic logic"
references: [hannah-ritchie-2024-vertical, mdpi-sustainability-2024]
visual:
  pattern: chain_5step_horizontal
  primary: "5-step chain horizontal (Why 1→2→3→4→5), physics → economics → engineering architecture + numerical breakdown 0.5 × 0.7 × 0.3 = 10.5%"
---

# 5-Why — why ML did not close the thermodynamic gap

## Assertion

ML optimizes on the denominator (efficiency 5-15%). The gap is in the numerator (LED energy vs free sunlight): 0.5 × 0.7 × 0.3 ≈ 10.5% end-to-end. This gap is two orders of magnitude; no model will close it.

## Visual

Below the 28pt bold assertion — a vertical 5-step chain (Why → Why → Why → Why → Why), each step in an Ocean rounded box, the steps connected by downward arrows. The left column takes 65% of the width.

**Why 1.** Why did Plenty close Compton after 19 months? → Unit economics didn't add up: production cost > selling price.

**Why 2.** Why didn't unit economics add up? → **60-80% of OPEX = electricity** for LEDs + climate control.

**Why 3.** Why does LED dominate OPEX? → LED delivers **~100× less energy** per unit of area than free sunlight.

**Why 4.** Why didn't ML close the gap? → ML optimizes the **denominator** (efficiency 5-15%); the gap is in the **numerator** (energy required vs delivered).

**Why 5.** Why did the category keep raising $1.37B+? → SPAC capital + celebrity backing + the «AI revolution in agriculture» narrative masked the thermodynamic gap.

On the right (35%) — a numerical breakdown in an Ocean rounded box:
- **LED efficiency:** ~50% (physical limit of the semiconductor)
- **Grid availability:** ~70% (annual average)
- **Growing efficiency:** ~30% (PAR → biomass for leafy greens)
- **End-to-end:** **0.5 × 0.7 × 0.3 ≈ 10.5%** ★ gold accent
- vs solar outdoor: ~100% (free denominator)

Bottom callout 16pt italic in a Teal-tint box: «**AP1 — The law of thermodynamics matters more than ML.** ML works on the denominator; the gap is in the numerator. Alternative: open ground where energy < $0.10/kWh; vertical only for high-value crops».

Footer 12pt italic: «Source: Hannah Ritchie substack based on MDPI Sustainability 2024».

## Speaker notes

Let's apply a five-why analysis to the collapse of vertical farming, staying within a single causal chain: physics, then economics, then engineering architecture.

Why did Plenty close Compton nineteen months after opening? Because unit economics didn't add up — the cost of producing leafy greens in a closed farm turned out to be structurally higher than the selling price.

Why didn't unit economics add up? Because sixty to eighty percent of a closed farm's OPEX consists of electricity for LED lighting and climate control.

Why does LED energy so dominate OPEX? Because LED delivers roughly one hundred times less energy per unit of area than free solar radiation, and that difference has to be compensated with electricity from the grid.

Why didn't AI optimization close this gap? Because AI optimizes parameters within a given architecture — that is, it works on the denominator of the business model; the fundamental physical gap sits in the numerator, in the amount of energy that must be delivered to the plant. Optimizing efficiency by five, ten, twenty percent doesn't compensate for a two-orders-of-magnitude gap between grid LED energy and free sunlight. This is an arithmetic consequence, not a shortcoming of the model.

And the fifth step — the financial-narrative layer. Why did the category keep raising one billion three hundred seventy million plus before the collapse? SPAC capital of 2020-2022 provided a fast liquid exit for early investors before unit economics were verified. Celebrity backing — Martha Stewart at AppHarvest, Natalie Portman at Bowery — generated media attention. The AI-revolution-in-agriculture narrative of 2021-2023 crowded out the analysis of thermodynamics. Independent LED-versus-sunlight expertise on the investment side was insufficient. This is not physics — it's a story about how the financial-narrative layer is superimposed on the engineering one and goes uncorrected for a long time.

The numerical decomposition on the right is the breakdown of a vertical farm's end-to-end energy efficiency into components per Hannah Ritchie's analysis. LED lighting efficiency is about fifty percent: the rest is heat, IR radiation outside PAR. Grid electricity availability is about seventy percent on an annual average. Growing efficiency is about thirty percent for leafy greens under vertical conditions. End-to-end equals zero point five times zero point seven times zero point three, about ten and a half percent. Compared with free sun — that's about a hundredfold OPEX gap.

And the main conclusion. AP-one — the law of thermodynamics matters more than ML. This is the first of five anti-AI criteria we've arrived at. When the fundamental economics is an order of magnitude above the market price of the product, ML optimization doesn't close the gap, because it works on the denominator. The alternative: open ground where energy is under ten cents per kilowatt-hour; vertical farming is justified only for high-value crops where the premium covers the energetics.

## Sources

- Hannah Ritchie substack — Vertical farming thermodynamic gap.
- MDPI Sustainability journal (2024) — LED energy efficiency analysis.

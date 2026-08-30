---
id: s38s
type: schema_matrix
duration_min: 1.5
assertion: "AP1 thermodynamics > ML / AP3 accuracy threshold ≠ deployment / AP4 generic LLM as advisor = anti-pattern / AP6 AI-equipment = vendor lock-in / AP7 AI-MRV without direct measurement = greenwashing. + AP2a/AP2b/AP5 inline."
learning_goal: "The main consolidation takeaway of the lecture (LO5)"
learning_outcomes: [LO5]
chapter_ref: "§6.2 Part 3 — Five explicit «when not AI» — consolidation"
references: []
visual:
  pattern: schema_matrix
  primary: "Matrix 5 rows × 3 columns (# / Criterion / Example / Alternative) + 3 inline criteria below"
---

# Five «when not AI» criteria — the main takeaway

## Assertion

AP1 thermodynamics > ML / AP3 accuracy threshold ≠ deployment / AP4 generic LLM as advisor = anti-pattern / AP6 AI-equipment = vendor lock-in / AP7 AI-MRV without direct measurement = greenwashing. + AP2a/AP2b/AP5 inline.

## Visual

Below the 28pt bold assertion — a large matrix in an Ocean rounded box, 6 rows (header + 5 criteria) × 4 columns. Header row Primary mid with white text; row bodies alternate Surface light / White:

| # | Criterion | Example from the lecture | Alternative |
|---|---|---|---|
| **AP1** | **The law of thermodynamics matters more than ML** — the fundamental economics is an order of magnitude above the product price | Vertical farming — LED ≈ 100× free sunlight; Plenty $940M, Bowery $32M | Open ground where energy < $0.10/kWh; vertical only for high-value crops |
| **AP3** | **Threshold accuracy ≠ readiness for deployment** | Plantix 10-15% misdiagnosis × 10M+ = ~100k wrong recommendations/year | Calibrated confidence + abstention; «not sure → ask an expert» |
| **AP4** | **A generic LLM in advisor mode** for high-stakes = a categorical anti-pattern | ChatGPT/Bard recommending the wrong herbicide window (Tzachor 2024) | RAG-grounded in a local regulator + abstention + human in the loop |
| **AP6** | **«AI-driven equipment» = a vendor lock-in trap** | FTC v. Deere; Melitopol remote-brick; FieldView exit from Russia; FCC ban DJI | Open-source hardware (Farm Hack); right-to-repair; multi-vendor; mechanical fallback |
| **AP7** | **AI-MRV for carbon claims without direct measurement** = scaled greenwashing | Verra 94% phantom credits; Pachama 8×; Bowery $32M never-used | Direct soil sampling + transparent uncertainty bands; AI as a hypothesis, not fact |

**Gold accent** on criteria AP1 + AP6 (the two most "structural" — the law of thermodynamics + the vendor lock-in trap).

Below the matrix — a secondary table in a Teal-tint box: **Inline criteria (introduced in §2 and §5):**

| # | Criterion | Example | Alternative |
|---|---|---|---|
| **AP2a** | Architectural choice within the AI domain | Cognitive Pilot CV vs ITELMA sensor-fusion | A different class of AI (sensor-fusion instead of CV) |
| **AP2b** | A genuine non-AI alternative | FarmWise CV weeders → Lemken/Kverneland mechanical | Mechanical / direct measurement |
| **AP5** | Cloud-first for off-grid = an architectural error | 18% of US farms without internet; GNSS jamming in Finland; Starlink ban in Russia | Edge ML / TinyML; hybrid with redundancy |

Bottom callout 16pt italic in a gold-tint box: «**This is a working matrix for 2026. Run a proposed AI solution through the five criteria — if even one fires, a redesign is needed**».

## Speaker notes

Let's gather into one table the five explicit "AI isn't needed or isn't applicable here" criteria we examined over the whole lecture. This is the final consolidation for LO-five — analyze, formulate at least five explicit criteria for when AI isn't applicable.

The first criterion — AP-one. The law of thermodynamics matters more than ML. When the fundamental economics (energy or capital investment) is an order of magnitude above the market price of the product — ML doesn't close the gap, because it works on the denominator. The example from the lecture — vertical farming for commodity leafy greens: LED delivers about one hundred times more energy than free sunlight; Plenty lost nine hundred forty million, Bowery — thirty-two million of never-used equipment. The alternative — open ground where energy is under ten cents per kilowatt-hour; vertical only for high-value crops.

The second criterion — AP-three. Threshold accuracy does not equal readiness for deployment. Even ninety percent accuracy at scale is hundreds of thousands of wrong high-stakes decisions. Example: Plantix ten-to-fifteen percent misdiagnosis on ten million plus downloads — about one hundred thousand wrong pesticide recommendations per year. The alternative — an uncertainty-aware recommendation with abstention: not sure — ask an expert.

The third criterion — AP-four. A generic LLM in advisor mode for high-stakes decisions is a categorical anti-pattern. Example: ChatGPT and Bard recommendations of the wrong herbicide window in Tzachor et al. in Nature Food 2024. The alternative — RAG-grounded in a local regulator: USDA-EPA, EU-EFSA, Rosselkhoznadzor — plus explicit abstention under low confidence plus a human in the loop.

The fourth criterion — AP-six. AI-driven equipment is a vendor lock-in trap. The more AI and telematics in the equipment, the stronger the vendor control surface. Examples: the FTC versus Deere in 2025, the Melitopol remote-brick in 2022, the Climate FieldView exit from Russia, the FCC ban on DJI ag-drones. The alternative — open-source hardware Farm Hack, the right to repair, a multi-vendor strategy, mechanical fallback.

The fifth criterion — AP-seven. AI-MRV for carbon claims without direct measurement is inference with large uncertainty, marketed as precise measurement — that is, scaled greenwashing. Example: Verra ninety-four percent phantom credits, Pachama overestimation by eight times. The alternative — direct soil sampling of a meaningful share of projects plus transparent uncertainty bands; AI as a hypothesis, not as fact.

Plus three inline criteria we introduced in Sections 2 and 5 and actively use. AP-two-a — architectural choice within the AI domain: when CV doesn't work in the open environment, a different class of AI — sensor-fusion AI — may be more robust; the Cognitive Pilot versus ITELMA example. AP-two-b — a genuine non-AI alternative: when AI as a class isn't applicable, mechanical works; the example of vertical farming → open ground; FarmWise → Lemken Steketee. AP-five — cloud-first for off-grid is an architectural error; the alternative edge ML / TinyML.

The main thing about this matrix — it's a tool. When you're offered an AI solution for an agriculture task, run it through these five criteria plus the three inline. If even one fires — that doesn't mean "impossible", it means "a redesign is needed here". If several fire — it's worth reconsidering the fundamental choice of approach.

This matrix is not dogma. It works in 2026 with the data we have. In five years new criteria may appear, and the old ones may shift emphases. It's a working tool to update with experience.

## Sources

- Chapter v3.1 §6.2 Part 3.
- Lecture-wide synthesis of all failure blocks.

---
id: s12
type: assertion_visual
duration_min: 3
assertion: "GM's seat bracket and the Airbus bionic partition: a radical mass reduction obtained by numerical optimization and enumeration — not by a diffusion model."
learning_goal: "Real cases — the kind of AI is optimization+enumeration, NOT diffusion; cascade: ≤3 numbers / ≤4 product names"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.4 — Real industrial cases"
references: [autodesk-gm-bracket, airbus-bionic-partition]
visual:
  pattern: matrix
  primary: "2 case cards in an Ocean rounded box: GM seat bracket + Airbus bionic partition; ≤3 numbers per card; a kind-of-AI label on each"
  illustration:
    type: schematic
    sources:
      - "Self-generated 2-card layout via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `car` (GM), `plane` (Airbus), 32px inline, recolored to Primary mid `#065A82`"
      - "Wikimedia Commons CC-BY — generative bracket / aircraft partition photos as fallback"
    caption: "Real cases: optimization + enumeration, not diffusion"
interaction: none
---

# GM and Airbus: optimization and enumeration, not diffusion

## Assertion

GM's seat bracket and the Airbus bionic partition: a radical mass reduction obtained by numerical optimization and enumeration — not by a diffusion model.

## Visual

Two case cards side by side in an Ocean rounded box. Card 1 — "GM seat bracket" (icon `car`): no more than three numbers — "8 parts → 1," "mass −~40%," ">150 variants evaluated"; a label plate below: "kind of AI: numerical optimization + cloud-based enumeration." Card 2 — "Airbus bionic partition" (icon `plane`): no more than three numbers — "mass −~45%," "≈35 kg vs. ≈65 kg," "material Scalmalloy"; a label plate below: "kind of AI: topology/lattice optimization + enumeration." Below both — a gold plate (`#F0AB00`): "both parts require additive manufacturing — this is a constraint, not a coincidence." Text per cell ≤2 lines, ≥14pt.

## Speaker notes

Two cases have become canonical; let's examine them with the kind of AI specified. The first — the very seat bracket from General Motors that opened the lecture: eight parts of the assembly consolidated into one, the chosen variant about 40% lighter and noticeably stronger than before, the program generated more than 150 alternatives. Kind of AI: multi-criteria numerical optimization plus cloud-based enumeration of variants, under the goal "minimum mass subject to a stress constraint and a given manufacturing method." This is not a diffusion model; the "150 variants" are 150 points satisfying the optimality conditions under different weightings of the goals, not 150 samples from a neural network.

The second — the bionic cabin partition for the Airbus A320. Mass reduced by about 45 percent: around 35 kilograms versus about 65 for the standard one, a lattice "bone" structure, material Scalmalloy — an aluminum-magnesium-scandium alloy for laser sintering, the part assembled from many printed sections and titanium connectors. An estimate of fuel savings across the fleet appears in the press, but as an order-of-magnitude estimate, not a precisely measured fact, so it is not given here as an exact number. Kind of AI again: topology and lattice optimization plus evolutionary enumeration, not a generative model.

Notice the recurring pattern: both parts require additive manufacturing — 3D printing. This is not a coincidence but a constraint we will return to when we dissect the failure of this part: a beautiful "organic" shape is, by default, manufacturable only by layer-by-layer printing.

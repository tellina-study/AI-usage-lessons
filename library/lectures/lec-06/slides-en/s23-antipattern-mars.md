---
id: s23
type: assertion_visual
duration_min: 3.5
assertion: "Mars Climate Orbiter: $327M lost to an unchecked unit mismatch at a seam between systems — an LLM in a project is exactly such a 'seam.'"
learning_goal: "The LLM anti-pattern + historical failures (the FAILURE core); Mars LEADS, Gimli/Hyatt in one line each (cascade)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.4 — The anti-pattern and historical failures: Mars Climate Orbiter and its brethren"
references: [nasa-mco-mishap-1999, gimli-glider, hyatt-regency]
visual:
  pattern: assertion_visual
  primary: "A dominant Mars Climate Orbiter block in an Ocean rounded box; Gimli/Hyatt each in one line at the bottom"
  illustration:
    type: schematic
    sources:
      - "Self-generated dominant case block via PowerPoint shapes (Ocean palette)"
      - "Lucide icons https://lucide.dev — `satellite` (Mars Climate Orbiter), `plane` (Gimli), `building` (Hyatt), 32px / 96px hero for Mars, recolored to Primary mid `#065A82`"
      - "Wikimedia Commons CC — a Mars Climate Orbiter spacecraft image as fallback hero"
    caption: "Mars Climate Orbiter — a structural model of a failure at the seam between systems"
interaction: none
---

# Mars Climate Orbiter: a unit mismatch at the seam between systems

## Assertion

Mars Climate Orbiter: $327M lost to an unchecked unit mismatch at a seam between systems — an LLM in a project is exactly such a "seam."

## Visual

A dominant block (~70% of the slide) in an Ocean rounded box, with a 96px hero `satellite` icon: heading "Mars Climate Orbiter (1999)." Inside — 3 fact lines: "contact lost on Mars orbit insertion · mission cost ≈ $327M" (gold highlight `#F0AB00` on the sum); "the ground module output pound-force-seconds, the trajectory program expected newton-seconds — a mismatch of ×4.45"; "the conversion was performed by no one: each side assumed the other had done it." Below the facts — a projection arrow in a gold plate: "An LLM assistant = exactly such a seam between systems: it takes quantities from one context and passes them into another, and it CONFIDENTLY confuses units (psi and MPa, mm and inches)." At the bottom, in a narrow strip, one line each: "Gimli Glider (1983) — a manual fuel recalculation with the wrong coefficient" · "Hyatt Regency (1981) — a joint change 'by word of mouth,' with no independent recalculation." A caption (12pt): "the evidence — on the next slide."

## Speaker notes

The main case of this part is the Mars Climate Orbiter disaster, and it is examined at length because it is a precise structural model of how AI fails at a seam between systems. In September 1999, contact with the interplanetary station was lost during Mars orbit insertion; the mission's total cost was about 327 million dollars. The cause was not complex physics. The ground software module that computed thruster impulses output data in pound-force-seconds, while the trajectory-computation program expected newton-seconds — a mismatch of a factor of 4.45. The conversion was performed by no one: one side assumed the other had done it. The investigation board placed responsibility not on an error in a formula, but on the absence of an independent check that would have caught the mismatch at the interface between the two systems.

Let's project this onto today. An LLM assistant in an engineering process is exactly such a seam between systems: it takes quantities from one context and passes them into another, and it confidently confuses units — psi and megapascals, millimeters and inches, newton-meters and pound-feet. Accepting a number from AI without an independent dimensional check is a digital Mars Climate Orbiter. The lesson: dimensional control and independent verification at every interface with AI, not trust in a confident answer.

The same pattern is visible in two more classical cases. Gimli Glider — a Boeing 767 that ran out of all its fuel due to a manual recalculation with the wrong coefficient; the crew landed the plane by gliding. Hyatt Regency — the collapse of suspended walkways in a hotel after a suspension joint was changed late in the process, effectively without an independent recalculation. The thread connecting all three cases: not one catastrophe was caused by complex physics — all three are an undetected mismatch or an unchecked change at a seam where each side assumed someone else would check. An AI assistant creates exactly such seams in commercial quantities.

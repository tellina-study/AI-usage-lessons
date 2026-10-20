---
id: n43
type: mechanism_node_graph
duration_min: 1.0
assertion: "The algorithmic valuation as an input, not as the decision: a human underwriter above the risk threshold plus an explicit circuit breaker, checked weekly, not quarterly"
learning_goal: "Zillow's solution with no demo: someone else's halted system, not our own rig. The diagram WITH the gate is the same device as the one without it (n40), at a different scale of condition than 'Refund Approval'. Short caption under the figure, full unpacking in the notes (BRIEF-PROIZVODSTVO.md §2)."
visual:
  pattern: mechanism_node_graph
  figure: zillow-shema-s-geytom-en.png
  primary: >
    A one-row diagram: Zestimate (input) → human underwriter above the risk
    threshold → explicit circuit breaker, checked weekly → purchase or halt.
  backup: >
    EN mirror of the figure, generated from the same script
    (make_figures_zillow.py --lang en) via the fig_strings_en.py dictionary,
    the established pattern from sem-06. Content is a direct unpacking of
    "Наше решение (без демо)" from SETKA-KEYSOV-S8-part2.md, section
    "Zillow", with no details added. No demo, deliberately: someone else's
    halted system, not our own rig.
---

# An architectural alternative: an underwriter and a circuit breaker

## Assertion

For capital-intensive automated decisions, the discipline of an allowed error share applies to prediction quality in real time — not only to whether the server is responding.

## Visual

> Zestimate (algorithmic valuation, an input, not the decision) → a **human underwriter** makes the final purchase decision above the amount/risk threshold → an **explicit circuit breaker** on the deviation of the actual price from the forecast, checked weekly or more often — not quarterly.

## Speaker notes

There won't be a demo here — this isn't our own rig, it's someone else's, halted system. But the architectural solution is stated just as directly as in any of our own cases, and the diagram on screen is the same row we drew without the gate, just with two added nodes.

The architectural alternative has two parts, and both work together, not separately. First: the algorithmic valuation stays an input to the decision, not the decision itself — buying a home above a given risk-amount threshold requires a final decision from a human underwriter, right at the point the decision is made, not after the fact. Second: an explicit circuit breaker that trips when the deviation between the actual sale price and the forecast exceeds a threshold — checked weekly or more often, not quarterly. As soon as the actual deviation exceeds the threshold, automatic buying in that segment stops pending manual review, instead of continuing while waiting for the next report.

This is the same device we already saw in "Refund Approval": the decision is replaced by a deterministic condition wherever it can be expressed as a condition over a structured value — a risk amount, a price deviation. The difference is in the scale of the condition, and in the scale of the cost if the condition isn't put in place. At the training center, the gate was a single refund amount. At Zillow, the gate was every single home purchase, and the cost of the gap wasn't an awkward conversation with a customer, but a realized loss in the hundreds of millions of dollars.

It matters that neither of the two parts works on its own without the other. A human underwriter without a circuit breaker still only learns of a problem from reporting, unless someone has assigned them to check the forecast-versus-actual deviation on a regular basis. A circuit breaker without a person on large-stake decisions will stop the process, but won't explain what to do with purchases already under way. The two parts together give you exactly what the loop was missing: fast detection of the deviation, and a person who takes on the decision once the deviation is confirmed.

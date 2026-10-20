---
id: n42
type: answer_breakdown_table
duration_min: 1.5
assertion: "Calibration and external volatility are not an engineer's point of intervention; what's decisive is the absence of a short monitoring period and of a human on decisions with a large stake"
learning_goal: "Zillow breakdown: form A5 (two columns, no verdicts), the turn is on what actually was the cause versus what wasn't."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: option · what it does · what it doesn't do. Below it, the turn
    as a separate tile: what turned out to be decisive.
  backup: >
    Content is a direct unpacking of the breakdown from
    SETKA-KEYSOV-S8-part2.md, section "Zillow", recast into form A5 (two
    columns) instead of prose.
---

# What each option actually does

## Assertion

Neither calibration nor the market's volatility itself was a point where an engineer could have intervened. What's decisive is in the other two options.

## Visual

| Option | What it does | What it doesn't do |
|---|---|---|
| **calibrate the model more precisely** | improves accuracy on stable historical data | isn't related to the finding: the model was already calibrated correctly — what failed wasn't the calibration, but a market regime absent from the training history |
| **runtime drift monitoring with an automatic stop threshold** | catches a sharp jump in the error rate within hours or days, while the loss is still small | was never put in place on the real buying loop: the only control that remained was the quarterly SEC filing — an archive, not an observation period |
| **tie the decision above the risk threshold to a human underwriter** | returns the decision with a large stake to a person right at the point the decision is made | was never built in structurally: the algorithm decided on buying the home by itself, regardless of the risk amount |
| **know in advance that the market would behave unpredictably** | — | isn't an engineering solution but a wish: market volatility is an external fact that can't be controlled from the model's side |

> **What's decisive.** The model didn't fail — the loop around it did: there was neither a short monitoring period nor a structural tie between large decisions and a person. A decision controlling hundreds of millions of dollars remained probabilistic where it should long since have become gated.

## Speaker notes

Let's go through them one at a time, in the order they're listed.

Calibrate the model more precisely — the first thing that comes to mind, and the first thing that turns out not to have been the cause. The Zestimate model was calibrated correctly on historically stable data: before the pandemic, its error over a holding period of a few months fell comfortably within the range the company considered workable for everyday operation. The culprit was not the calibration itself — it was the market's own volatility, a regime of price behavior that simply was not present anywhere in the data the model had been trained on.

Runtime drift monitoring with an automatic stop threshold — that is what was actually missing. A production model controlling hundreds of millions of dollars in real-estate purchases had no short period for watching its own error rate as it happened — hours or days that would catch a sharp jump while the loss was still small and the segment could still be paused. The only control left standing was the quarterly SEC filing — that is, a historical archive, not a period in which anyone could actually stop.

Tie the decision above the risk threshold to a human underwriter — the second half of the same gap. The decision to buy a home above a given risk amount was never structurally tied to any specific person: the algorithm decided on its own, regardless of how large the stake was. This is exactly the same shape of gap we already worked through in "Refund Approval" — there too, a refund-amount threshold existed on paper, but it never became an algorithmic gate.

Knowing in advance that the market would behave unpredictably isn't an engineering solution at all — it's a wish dressed up as a fix. Pandemic-driven volatility was a real external factor, but it was never a point where an engineer, sitting inside the company, could have changed anything.

What's decisive here is that the model itself didn't fail — the loop built around it did: there was neither a short control period nor any structural tie between large-stake decisions and a human being. A decision controlling hundreds of millions of dollars kept being made probabilistically, in a place where it should long since have become gated. On the next screen is a diagram of that same loop, but this time with the gate in it.

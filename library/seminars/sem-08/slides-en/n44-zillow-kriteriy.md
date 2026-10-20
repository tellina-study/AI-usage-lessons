---
id: n44
type: criteria_checklist_and_boundary
duration_min: 1.5
assertion: "Scale back automation when the cost of a single error is real capital and the external regime is shifting; this is the same idea as in 'Refund Approval', at the scale of an entire company"
learning_goal: "Zillow's criterion in direct form plus an explicit tie to the 'Refund Approval' case — closes the bridge between the training-center scale and the corporate scale of the same design mistake."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A two-column table, below it the limit as a separate tile and an
    explicit tie to the "Refund Approval" case.
  backup: >
    The criterion is a direct quote from SETKA-KEYSOV-S8-part2.md, section
    "Zillow", paragraph "Критерий"; the tie to "Refund Approval" is the
    paragraph "Закрывает ту же мысль" of the same section, unchanged in
    content.
---

# When to scale back automation

## Assertion

The same decision threshold was skipped at a training center and at a company with billions in revenue — the only difference is what it costs.

## Visual

| Scale back automated decisions | Can keep scaling |
|---|---|
| the cost of a single error is tens or hundreds of thousands of dollars of real capital | the cost of a single error is one unpleasant conversation with a customer, not capital |
| external conditions show growing volatility relative to the regime the model was trained on | the market and the data are stable, the regime matches what the model saw in training |
| a decision above the amount or risk threshold isn't tied to any specific person | a decision above the threshold structurally goes through a person, and a working circuit breaker exists |
| the only quality control is reporting once a quarter | there's a short monitoring period (hours to days) with an automatic stop threshold |

> **The limit.** If the cost of a single model error is tens of thousands of dollars of real capital, and external conditions show growing volatility, scale back automated decisions until the model's robustness to the new regime is confirmed — don't keep scaling "until we see the quarterly numbers."

> **The same idea as in "Refund Approval", at a different scale.** There, the gate was the decision on a single refund request, and the cost of the error was an awkward conversation with a customer. At Zillow, the gate became every home purchase, and the cost of the missed threshold was a realized loss of hundreds of millions of dollars and roughly a quarter of the entire workforce. The threshold existed in both cases; it never became an algorithmic gate in either, until someone checked.

## Speaker notes

The criterion, in direct form, same as for every one of our cases.

You need to scale back automated decisions when the cost of a single model error is measured in tens or hundreds of thousands of dollars of real capital — not an abstract metric, but money the company literally pays. At Zillow, one error is a house bought at the wrong price, not a point on a chart.

Scale back when external conditions show growing volatility relative to the regime the model was trained on. The pandemic-era housing market of 2020–2021 didn't resemble the market whose history the model was calibrated on, and it was exactly that mismatch of regimes, not the model itself, that became the source of the error.

Scale back when a decision above a given amount or risk threshold isn't structurally tied to any specific person: without that tie, a large stake gets decided by the same probabilistic loop as a small one.

And scale back when the only quality control is reporting once a quarter. A quarter is an archive, not a period in which you can stop before the loss grows.

The flip side is symmetric: if the cost of an error is small, the regime is stable, large decisions go through a person, and working monitoring exists — you can keep scaling automation further.

And last, the reason we placed this filler right here. The idea is the same one we already worked through in "Refund Approval", just at a different scale. There, the gate was the decision on a single refund request, and the cost of the error was an awkward conversation with a customer. At Zillow, the gate became every home purchase, and the cost of the missed threshold was a realized loss of hundreds of millions of dollars and roughly a quarter of the company's entire workforce. The threshold existed in both cases. It never became an algorithmic gate in either — until someone checked, with a test run or with a filing before the SEC.

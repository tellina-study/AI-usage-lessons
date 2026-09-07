---
id: s40
type: case_study
section: "Section 5. Support / Operate"
duration_min: 2.5
assertion: "Zillow had no runtime circuit breaker on prediction-accuracy drift — $304-408M in write-downs, ~2,000 laid off"
learning_goal: "On-point failure #9: Zillow drift — a capital-committing model with no circuit breaker (LO2/LO3/LO6)"
learning_outcomes: [LO2, LO3, LO6]
chapter_ref: "§5.4 [for-slide-s40]"
in_bucket: true
interaction: none
verify_day_of: false
meme_or_visual: >
  case_study: a "house with a growing crack in the foundation" icon (concept drift — the market
  shifted) + a small crossed-out "circuit breaker" (the missing fuse). A large $304-408M figure
  in an Ocean rounded box.
source: "GeekWire (Nov 2021); SEC 10-K FY2021"
---

# Visible content

## Title bar
The model was calibrated correctly — there was no real-time fuse for drift

## Body
[A "house with a crack" icon + a crossed-out circuit breaker]

**Zillow Offers, November 2021**
- Write-downs: **$304-408M** · ~2,000 laid off (~25% of staff)
- 9,680 homes bought, 3,032 sold — a loss of **≈$80,000 per property**

[Gold callout]
There was no runtime monitoring of prediction-accuracy drift with an automatic circuit breaker

## Speaker notes

Zillow Offers bought and quickly resold homes based on an algorithmic valuation. On November 2, 2021, the business's shutdown was announced. Inventory write-downs were $304.4 million for the third quarter, reaching almost $408 million for the year. Staff was cut by roughly twenty-five percent. In the third quarter, 9,680 homes were bought but only 3,032 sold — an average loss of about $80,000 per property. The CEO said directly: the observed error rate turned out to be far more volatile than we ever thought possible.

The mechanism, tied to the Support/Operate phase: note that this is specifically an operations failure, not a measurement one. The model was calibrated correctly on historically stable data — experiment design and discovery have nothing to do with it. The failure was operational: a production model directing hundreds of millions of dollars in real-estate purchases had no runtime monitoring of prediction-accuracy drift with an automatic circuit breaker. Pandemic-era price volatility was a classic case of concept drift, and it wasn't caught in time because there was no working equivalent of an error budget for this specific model.

The lesson: for models directing capital-intensive automated decisions, error-budget discipline must apply to prediction quality in real time, not just to service uptime. The criterion: if the cost of a single error is tens of thousands of dollars of real capital, and external conditions show growing volatility, that's a signal to scale back automated decision volume until the model's stability is confirmed. The alternative: a hybrid architecture — algorithmic valuation as an input, a human underwriter making the final call above a risk threshold, plus an explicit circuit breaker checked weekly.

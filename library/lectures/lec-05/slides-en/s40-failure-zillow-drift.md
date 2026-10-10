---
id: s40
type: case_study
section: "Section 5. Support and operations"
duration_min: 2.5
assertion: "Zillow Offers bought homes on an algorithmic valuation; the market shifted and the business was shut down with $304-408M in write-downs and ~2,000 people cut — the model was calibrated correctly, what was missing was real-time monitoring of accuracy and an automatic stop"
learning_goal: "An operations failure: a model that commits money, with no fast observation window and no stop threshold"
learning_outcomes: [LO2, LO3, LO6]
chapter_ref: "§5.4 [for-slide-s40]"
in_bucket: true
interaction: none
protected: true
verify_day_of: false
revision: >
  issue #212, EN parity: brought to the Stage-6 RU source. The slide was rebuilt so it
  reads without the lecturer — "what happened" in plain words first (what the service
  was, what it did, how it ended, with figures and dates), the analysis second and
  named as the analysis. The previous EN title was the conclusion of the analysis
  ("the model was calibrated correctly — no real-time fuse"), so a reader met the
  verdict before knowing which case it was about. The "circuit breaker" framing was
  also removed here: that term is introduced on s42, and the RU source does not use it
  on this slide.
meme_or_visual: >
  case_study: a "what happened" bar with a real source image on the left. Below it, on
  the left, ONE chart (c-zillow.png) — 9,680 homes bought against 3,032 sold in a single
  quarter, both quantities in the SAME unit and therefore directly comparable; below
  right, a captioned analysis block. A gold callout at the bottom with the criterion and
  the alternative. The earlier TWO side-by-side charts ($M and $K on different scales)
  captioned "do not compare bar lengths directly" were removed on the RU side after a
  student review: two charts side by side read as a comparison whatever is written under
  them.
source: "GeekWire (Nov 2021); Zillow Group's 2021 annual report (Form 10-K)"
---

# Visible content

## Title bar
Zillow: algorithm bought homes, market moved, business shut

## Body
[A "what happened" bar with the source image; below it ONE chart "9,680 bought / 3,032 sold in the third quarter of 2021" and an analysis block. Money figures stay in the text, not on the chart.]

**WHAT HAPPENED**

Zillow Offers — a service that bought homes on an algorithmic valuation and resold them fast. In the third quarter of 2021 it bought 9,680 and sold 3,032. On the second of November 2021 it announced the shutdown: write-downs of **$304–408M**, a cut of about **2,000 people — 25% of staff**. Average loss — about **$80K per home**.

**ANALYSIS: OPERATIONS, NOT MEASUREMENT**

The model was calibrated correctly — on historically stable data, and experiment design has nothing to do with it. What was missing is different: real-time monitoring of prediction accuracy and an automatic stop when it falls. Price volatility shifted the very relationship between a property's features and its fair price.

Go back to the two observation windows: Zillow had neither. The short one — a sharp rise in error went unseen. The long one — quarterly reporting existed, but a report every three months is no observation window: it is a historical archive, and by publication the homes are bought and the capital is committed.

[Gold callout]
Criterion: a model that commits money on its own needs real-time monitoring of accuracy and a threshold at which it stops with no human involved. Alternative: the algorithmic valuation as an input, the decision above a risk threshold left to a person.

## Speaker notes

First, what happened — because a case is worth understanding whole before you take it apart.

Zillow Offers bought homes on an algorithmic valuation and resold them fast. In the third quarter of twenty twenty-one the service bought nine thousand six hundred and eighty homes and sold only three thousand and thirty-two. On the second of November that year the company announced it was shutting the service down. Inventory write-downs: three hundred and four million for the quarter, almost four hundred and eight for the full year. A cut of about two thousand people, roughly a quarter of the whole staff. The average loss came to about eighty thousand dollars per home. The chief executive said it plainly: the observed error rate turned out to be far more volatile than the company had ever thought possible.

Now the analysis, and it starts with where this case belongs. This is an operations failure. Measurement is not at fault: the model was calibrated correctly, on historically stable data, and experiment design has nothing to do with it at all. Something else was missing — real-time monitoring of prediction accuracy, and an automatic stop when that accuracy falls. And price volatility shifted the very relationship between a property's features and its fair price; the model stayed the same, the world underneath it changed.

Apply the two observation windows here literally. The short window was absent: a sharp rise in prediction error went unseen in real time. The long one formally existed — quarterly reporting. But a report every three months does not work as an observation window: it is a historical archive, and by the time it is published the homes have been bought and the capital is committed. Hence the exact diagnosis: what was missing was a fast layer with an automatic stop threshold, because "the model is calibrated, after all" was treated as a sufficient guarantee for an indefinite time ahead.

The lesson and the alternative. A model that commits money on its own requires real-time monitoring of accuracy and a threshold at which it stops with no human involved. The working alternative is hybrid: the algorithmic valuation as an input, the decision above a risk threshold left to a person.

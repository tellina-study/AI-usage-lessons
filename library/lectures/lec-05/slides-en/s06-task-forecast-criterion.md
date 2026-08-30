---
id: s06
type: assertion_visual
section: "Section 1. Time-series forecasting"
duration_min: 2.5
assertion: "Forecasting demand/cash-flow/churn requires a tabular model with a measurable error — 3 arguments why not an LLM: data structure, calibration, what breaks"
learning_goal: "Unfolded criterion «why classical statistics/ML, not an LLM» (in only with ≥3 arguments + alternative)"
chapter_ref: "§1.2"
visual_brief: "3 argument cards in Ocean rounded box + alternative card. Gold — «measurable error». Footer — PII/Federal Law 152-FZ caveat."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Why a tabular model here, not an LLM — three arguments, not a caveat.

## Body
[Ocean rounded box — 3 argument cards]

**Argument 1 — data structure**
Tabular numeric series: date, point of sale, product, quantity, price, features. Models for series extract trend and seasonality from this; converting the series into text for an LLM loses exactly the structure that needs to be used.

**Argument 2 — measurability and calibration**
The decision about the order size is built on a numeric error metric + a confidence interval. Classical models give this out of the box; an LLM does not.

**Argument 3 — what breaks with the wrong choice**
An LLM will give a plausible number with no justified uncertainty — yet the ordering decision still has to be made, and the cost of a systematic error is multiplied by the volume (the Zillow mechanism).

[teal callout — alternative and criterion]
The correct tool is a tabular predictive model with a measurable error. Even it is not enough in a non-stationary environment + an irreversible capital action without human control.

[Gold]
Task: demand forecasting (shelf/ordering), cash-flow (liquidity), **customer churn** (whom to retain).

## Speaker notes

Let's make the task concrete and take the choice argument all the way to an unfolded criterion. In retail, demand forecasting is the basis of the entire operational chain: how much product to order, how much to hold in the warehouse, when to launch a promotion. An error in one direction — an empty shelf and a lost sale; in the other — an overflowing warehouse and the write-off of expired goods. In finance the analog is forecasting the inflow and outflow of money to manage liquidity, and forecasting customer churn: who is highly likely to leave in the coming months, so there is time to retain them.

The unfolded criterion of why classical statistics and tabular ML, and not a language model, requires at least three arguments, not one caveat. First — data structure: this is tabular numeric series with a date, point of sale, product, quantity, and features like day of week, holiday, promotion. Models for series are designed to extract trend and seasonality from this; converting the series into text to feed a language model loses exactly the structure that needs to be used. Second — measurability and calibration: a forecast needs a numeric error metric and a confidence interval, because the decision about the order size and safety stock is built on these numbers; classical models give this out of the box, a language model does not. Third — what breaks with the wrong choice: if you choose an LLM, you get a plausible number with no justified uncertainty, and the ordering decision on that number still has to be made, and the cost of a systematic error is multiplied by the volume of orders — exactly the Zillow mechanism. The correct alternative is a tabular predictive model with a measurable error; the criterion under which even it is not enough is a non-stationary environment without human control over a capital action.

Separately — the through-going theme of data safety. If the series contain personal data of citizens of Russia, their processing is regulated by the personal-data law; sending such series to a public cloud service of a language model is not only a methodologically wrong choice of type of AI, but also a potential violation of localization requirements.

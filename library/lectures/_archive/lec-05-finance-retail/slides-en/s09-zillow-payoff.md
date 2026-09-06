---
id: s09
type: case_study
section: "Section 1. Time-series forecasting"
duration_min: 2
assertion: "Zillow: distribution shift × irreversible auto-action without a circuit breaker = loss of the line of business; Opendoor survived on the same type of AI — it is not the model that decides, but the harness"
learning_goal: "Model failure slide: payoff hook; distribution shift + asymmetry from scratch; Knight callback; criterion + alternative (CQ return 1)"
chapter_ref: "§1.5"
visual_brief: "Left — mechanism (distribution shift → asymmetry → 3 conditions) + Knight callback. Right — Zillow vs Opendoor + criterion + alternative. Gold — «same type, different harness»."
interaction: think_pause
verify_day_of: false
---

# Visible content

## Title bar
What ruined Zillow was not the model's drift, but what its output was wired to.

## Body
[Left — mechanism, Ocean rounded box]

**distribution shift**
the data in reality stopped resembling the training data — the 2020–2021 housing market became statistically different; the forecast went off where the patterns changed

**asymmetry of the error cost**
a recommendation error ≈ 0 · the same forecast error, on which a house was bought, = tens of thousands of $ × N, and **irreversible**

**Three things together = fatal:**
an irreversible capital action × automatically on the model's output × a non-stationary environment without a circuit breaker (auto-stop on an anomaly)

[Knight callback card]
Knight Capital, 2012: $440M in ~45 minutes on a deterministic algorithm — the same class: automation of the irreversible without a kill switch.

[Right — Ocean rounded box]
**Zillow vs Opendoor** — the same type of AI, the same period. Opendoor survived thanks to a more conservative spread and risk design.

[teal callout — criterion + alternative]
It is dangerous when all at once: (a) the output triggers a large irreversible action automatically, (b) the environment is non-stationary, (c) there is no circuit breaker. Alternative: a narrow segment + human gate + live error monitoring + circuit breaker.

[Gold callout, bottom]
The model did exactly what it was designed for. The error was the engineering decision of **where** to wire in its output. The same AI, a different judgment → bankruptcy of the line of business vs survival.

## Speaker notes

Now the central question returns edge-on for the first time, and we reveal what we started with. Zillow Offers was algorithmic iBuying based on home-value estimation models. The model forecast the future price of a home; based on the forecast, Zillow automatically made offers and bought homes across dozens of regions. In 2020–2021 the U.S. housing market went through anomalous volatility. The model, trained on a relatively stable preceding market, systematically overvalued the properties. The type of AI is a predictive regression model on tabular and geo data, not a language model.

Let's introduce here from scratch the load-bearing term of the entire line of failures. Distribution shift is when the data on which the model operates in reality stops resembling the data on which it was trained: the environment changed its regime faster than the model could adapt. The model learned on one world and works in another. But drift by itself does not bankrupt a company — models drift constantly. What ruined Zillow was what its output was wired to. Let's formulate the key concept: the asymmetry of the error cost. A forecast error in a recommendation costs about zero. The same-magnitude forecast error, on which a real home is automatically bought, costs tens of thousands of dollars and is irreversible. Zillow combined three things: an irreversible capital-intensive action, triggered automatically, in a non-stationary environment without a kill switch.

Here a brief return to Knight Capital is apt: in 2012 a trading firm lost four hundred forty million in forty-five minutes on a deterministic algorithm — not AI, but the same class of error: automation of an irreversible action without a kill switch. And the most instructive part: the competitor Opendoor survived the same period on the same type of AI thanks to a more conservative risk design. The same tool, a different judgment about what surrounds it. The lesson: a predictive model with an ordinary error, multiplied by an irreversible action without a kill switch, turns a routine inaccuracy into the loss of a line of business. Think for thirty seconds: where else is an irreversible auto-action on a forecast dangerous — name your own example.

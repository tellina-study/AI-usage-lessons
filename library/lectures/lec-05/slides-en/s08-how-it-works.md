---
id: s08
type: process
section: "Section 1. Time-series forecasting"
duration_min: 1.5
assertion: "Forecasting decomposes history into trend + seasonality + noise and extends the patterns of the past — hence the built-in vulnerability: strong as long as tomorrow resembles yesterday"
learning_goal: "Mechanics «plainly» + buyer analogy + planting the vulnerability (key to s09)"
chapter_ref: "§1.4"
visual_brief: "Left — d08 (trend+seasonality+noise). Right — buyer analogy + forecast→ordering chain + gold vulnerability card."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Forecasting extends the patterns of the past — here lie both its strength and its vulnerability.

## Body
[Left — d08 in Ocean rounded box: history = trend + seasonality + noise, 4 rows; + legend caption on the PNG: "any sales series = trend + seasonality + noise; the model extends the regular part"]

[Right — Ocean rounded box]

**What the model does — the same as the eye, but numerically**
- decomposes history into **trend** + **seasonality** + **noise**
- learns on regular patterns, extends them into the future
- adds corrections for known events (promotion, holiday)

**Forecast → action**
"demand for next week ≈ N units" → "order N + safety stock"

[Anchor analogy]
A forecasting model is like an experienced buyer: "take more for the weekend, much more before New Year's" — but for millions of "store × product" pairs at once and numerically.

[Gold callout, bottom]
Built-in vulnerability: a forecast is strong exactly to the degree that **tomorrow resembles yesterday**. When the environment changes qualitatively — the model confidently extrapolates patterns that no longer exist. This is the key to the next slide.

## Speaker notes

So that the type of AI does not remain a black box with a name, let's explain the mechanics of a series forecast through a vivid analogy, without formulas. Imagine a sales chart of a single product over two years — a broken line of daily points. The human eye almost immediately sees three things in it: a general slope, sales are growing overall — this is the trend; a regular comb, a peak every Saturday, a dip every Tuesday, and a big annual hump toward December — this is seasonality; and small trembling around it, random fluctuations — this is noise. A forecasting model does essentially the same, but numerically: it decomposes history into trend, seasonality, and noise, learns on regular patterns and extends them into the future, adding corrections for known events like a promotion or a holiday. Then the forecast turns into an action: demand for next week is about so many units, which means order so many plus safety stock. The anchor analogy: a forecasting model is like an experienced buyer who, looking at the sales history, says "take more for the weekend, much more before New Year's", only it does this for millions of "store-by-product" pairs at once and numerically.

Here too let's fix the built-in vulnerability of this type of AI, which will become the key to the next case. A forecast extends the patterns of the past into the future. As long as tomorrow resembles yesterday, this works beautifully. But if the environment changes qualitatively — a new market regime, a demand shock, a structural shift — the model keeps confidently extrapolating the old patterns that no longer exist. It does not understand that the world has changed — it sees only numbers and extends the regularity. This characteristic is not a defect of a specific implementation, but a property of the approach itself: a forecast is strong exactly to the degree that the future is statistically similar to the training past. Remember this idea — in a minute it will explain the half-billion-dollar failure.

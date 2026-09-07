---
id: s05
type: assertion_visual
section: "Section 1. Time-series forecasting"
duration_min: 1.5
assertion: "A series forecast predicts the next NUMBER with trend and seasonality; an LLM predicts the next TOKEN OF TEXT — these are structurally different tasks"
learning_goal: "Type of AI for forecasting = classical statistics/ML; «why NOT an LLM» operationalized"
chapter_ref: "§1.1"
visual_brief: "2-column in Ocean rounded box: LLM vs series forecast. Type of AI: ARIMA family / boosting. Gold — «structurally different tasks»."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
A series forecast and a language model solve structurally different tasks.

## Body
[Ocean rounded box — 2-column, parallel structure]

**Language model (LLM)** | **Time-series forecast**
- predicts the next **token of text** | predicts the next **number** in the series
- optimized for the **plausibility** of the wording | needs **numeric accuracy** + calibrated uncertainty
- has no internal notion of "seasonality" / "sales trend" | series = trend + seasonality + noise
- has seen texts *about* sales | sees the sales series itself as a series

[Card — type of AI]
Type of AI for forecasting: classical statistics and tabular ML — the ARIMA family, gradient boosting on features. **Not** a generative model, **not** an LLM.

[Gold callout, bottom]
If you hand "forecast the demand" to a text model, it will produce a plausible-sounding number with no connection to the product's seasonality: a hallucination in a numeric wrapper. The correct type of AI is determined by the **structure of the task**, not by the trendiness of the tool.

## Speaker notes

Time-series forecasting is the prediction of future values of a numeric quantity that is measured regularly over time: how much milk a store will sell next Tuesday, what the inflow of money into an account will be next month, how many customers will churn next quarter. The key word is series: a time-ordered sequence of numbers in which there is a trend (a long-term direction), seasonality (a repeating cycle), and noise (random fluctuations). The type of AI for this task is classical statistics and tabular machine learning: the ARIMA family of models, gradient boosting on features. This is not a generative model and not a language model.

Here it is worth unfolding the "why not an LLM" argument, because after Lectures 1–4 you develop the reflex "AI is ChatGPT". Let's break it down plainly. First: a language model is built to predict the next token of text — the most plausible continuation of a sequence of words. A series forecast is the prediction of the next number in a sequence of numbers with trend and seasonality. These are structurally different tasks: a language model in principle has no internal notion of "sales seasonality" — it has not seen your series as a series, it has seen texts about sales. Second: a forecast needs not the plausibility of the wording, but numeric accuracy and calibrated uncertainty. Third: what breaks with the wrong choice? Hand "forecast the demand" to a text model — it will produce a plausible-sounding number with no connection to the actual seasonality, and detecting that error is harder than detecting an obvious one. The intuition-conclusion: for a series of numbers over time you need a tool that can handle a series of numbers over time; the correct type of AI is determined by the structure of the task, not by what is currently on everyone's lips.

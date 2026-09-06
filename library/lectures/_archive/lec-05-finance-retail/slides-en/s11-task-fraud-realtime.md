---
id: s11
type: assertion_visual
section: "Section 2. Anomaly detection"
duration_min: 3
assertion: "Fraud is rare and drifts — learn «what a customer's normal looks like» (anomaly detection), not «what fraud looks like»; this is not series forecasting, not generation, not an LLM"
learning_goal: "Real-time fraud task; why anomaly detection; AML = an attribute (1 line); cloud + outlier analogy"
chapter_ref: "§2.1"
visual_brief: "Left — d11 (normal cloud + outlier). Right — why NOT classification/forecast/LLM. AML = 1 line. Gold — «learn the norm, not fraud»."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Learn "the customer's normal" and catch the deviation — rather than learn "what fraud looks like".

## Body
[Left — d11 in Ocean rounded box: normal cloud + outlier]

[Right — Ocean rounded box]

**Task:** catch a fraudulent transaction in real time, where almost all operations are legitimate and the share of fraud is extremely small.

**Type of AI — anomaly detection:** the model builds the customer's "normal" (amounts, geo, time, merchants) and flags deviations.

**Why exactly this one:**
- **not classification** "fraud/not fraud" — fraud is rare and constantly changes its form (a moving target)
- **not series forecasting** — the question is not "the next value", but "how much this operation does not resemble the norm"
- **not an LLM** — a transaction is structured, the task is geometric, not linguistic

[Attribute line]
*AML (anti-money-laundering) — a subset of the same anomaly-detection task; hard legislative thresholds are deterministic rules, not a model.*

[Gold callout, bottom]
The model does not "know" that this is fraud — it knows that this does **not resemble the norm**, and raises a flag for review.

## Speaker notes

The task of this section is the detection of fraudulent transactions in real time: a stolen card, an atypical payment, an attempt to withdraw funds — in a stream where the overwhelming majority of operations are legitimate, and the share of fraud is extremely small. The type of AI for this task is anomaly detection: the model builds a representation of normal behavior, how this customer usually pays by amounts, geography, time, merchants, and flags deviations. This is not series forecasting, because we are not predicting a future value, and not generation, because we are not producing anything; this is the calibration of the boundary "normal or anomalous".

Let's fix why exactly anomaly detection and not another type — this is an important fork. Why not ordinary classification "fraud or not fraud" trained on labeled examples? Because fraud is by definition rare and constantly changes its form: labeled examples are few, and they go stale as soon as the fraudster invents a new scheme. Learning "what fraud looks like" is fragile, because fraud is a moving target. Anomaly detection flips the task: learn not "what fraud looks like", but "what this customer's normal looks like", for which there is plenty of data — his entire legitimate history — and catch deviations. Why not series forecasting? Forecasting answers "what will the next value be", but here the question is different — "how much this specific operation does not resemble the norm". Why not a language model? A transaction is a structured record, not text; the task is geometric — how far the point is from the cloud of the norm — not linguistic.

In one line — about anti-money-laundering. From the standpoint of the type of AI it is a subset of the same anomaly-detection task, not a separate type; the fundamental difference is that part of the requirements are hard legislative thresholds, and they are implemented by deterministic rules, not by a probabilistic model. An analogy for the mechanics: imagine a cloud of points — a customer's ordinary transactions cluster together; the model outlines the cloud, and an operation that has fallen far beyond its edge is a candidate for an anomaly. The model does not know that this is fraud; it knows that this does not resemble the norm.

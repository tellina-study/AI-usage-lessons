---
id: s29
type: matrix
section: "Section 6. Framework"
duration_min: 3
assertion: "The matrix «task × AI type»: 6 tasks → the right type, why not an LLM, the typical failure; the bottom row — a deterministic regulatory task → ordinary code, NOT AI"
learning_goal: "LO1 payoff — the apparatus for choosing an AI type; the bottom row «when not AI at all» (transfer from L3–4)"
chapter_ref: "§6.1"
visual_brief: "A matrix of 6 rows × 3 columns in an Ocean rounded box. Icons per row. Bottom row gold. Single-line, fill 100%. Gold — the bottom row."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Name the type by the structure of the task — and sometimes the right type is not AI at all.

## Body
[Ocean rounded box — a matrix of 6 rows × 3 columns]

| Task | AI type · why this one | Typical failure |
|---|---|---|
| Demand / cash-flow / churn forecasting | Time-series forecast (ARIMA/boosting) — numbers with a trend, not text | distribution shift × irreversible auto-action (Zillow) |
| Fraud real-time / AML | Anomaly detection + rules engine — norm/deviation | FP at scale; accuracy lies under imbalance |
| Credit scoring | Tabular ML (logreg/GBM+SHAP) — explainability = law | proxy bias + opacity (Apple Card) |
| Support / voice / explanation | LLM (grounded) — a text-and-dialogue task | hallucination of a financial fact = legal liability (Air Canada) |
| Recommendations / pricing | Recsys; pricing — an optimizer within a frame | proxy ≠ goal: filter bubble (Wendy's) |
| **Deterministic regulatory task** (a hard AML threshold) | **Ordinary code / rules engine — NOT AI** — precision, audit, law ≠ probability | AI would add nondeterminism + an error surface |

[Gold callout, bottom]
The bottom row is deliberate. If the task = executing a hard verifiable regulatory rule, the right tool is **not AI, but deterministic code**: AI here does not «not hurt» but would add nondeterminism where precision and an audit are required.

## Speaker notes

Let us assemble five sections into one apparatus — this is the answer to the central question and the core of the skill of choosing an AI type. The matrix: a row is a task, the columns are the right AI type and why this one, and the typical failure. This is a compact packaging of five facts already proven in the lecture, not new material.

Forecasting demand, cash inflow, churn — the AI type is time-series forecasting, because these are numbers with a trend and seasonality, not text; the typical failure is distribution shift multiplied by an irreversible automatic action, as at Zillow. Fraud and anti-money-laundering in real time — anomaly detection plus deterministic rules, because the task is about norm and deviation, and the laundering threshold is law; the typical failure is false positives at scale and deception by an accuracy metric under imbalance. Credit scoring — classic tabular ML, because explainability is a regulatory requirement; the typical failure is bias through a proxy and opacity, as at Apple Card. Support, voice, explanation — a language model grounded on a source, because the task is text-and-dialogue; the typical failure is hallucination of a financial fact as legal liability, as at Air Canada. Recommendations and pricing — a recommender system, and price is an optimizer within a human frame; the typical failure is proxy is not equal to goal, a filter bubble, as at Wendy's.

The bottom row is deliberate. It answers the course's through-line question «when not AI at all» — a direct transfer of the principle of Lectures 3 and 4: if the task is executing a hard verifiable regulatory rule, the right tool is not AI, but deterministic code; AI here does not «not hurt» but would add nondeterminism and an error surface where precision and an audit are required. The matrix is not «pick a fashionable model» but naming the type by the structure of the task, and sometimes the right type is not AI at all. This is exactly the apparatus you must carry away from the lecture.

---
id: s24
type: assertion_visual
section: "Section 4. LLM in finance"
duration_min: 2
assertion: "Four AI types, one class of failure: the type was chosen correctly, it broke in the harness around it — the right type choice is necessary but NOT sufficient"
learning_goal: "Pivot S4→S5 (NOT a retro summary): a two-level conclusion + a bridge to the «harmless» type"
chapter_ref: "§4.5"
visual_brief: "PIVOT checkpoint (NOT a retro summary): a progress strip 4/5 types (✓×4 + →Recsys gold). Two-level conclusion (teal). Bridge card to recsys. Gold — FORWARD QUESTION «why is the most harmless type more dangerous?» (differentiated from s30-payoff and s19-criterion — the «necessary/insufficient» formula is NOT duplicated visibly)."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
Checkpoint: 4 of 5 types covered — a turn toward «human + harness».

## Body
[Progress strip across 5 types — 4 covered (✓), Recsys — next (gold)]
✓ Forecast (Zillow) · ✓ Anomalies (fraud-FP) · ✓ Scoring (Apple Card) · ✓ LLM (Air Canada) · → Recsys (next, gold)

[teal callout — two-level conclusion (the substance of the pivot, chapter §4.5)]
**Level 1** «which AI type» — is resolved by the structure of the task, most often unambiguously. **Level 2** «what surrounds the AI at the cost of the error» — is designed separately. The lecture's turn: from here attention shifts from the type to the harness.

[Bridge card — why the «harmless» type is next]
The last type — recsys / pricing — seems the most **harmless**: the cost of error is near zero. Precisely for that reason it is more dangerous than the others: the failure is **quiet** — the system reports success by its own metric.

[Gold callout, bottom — FORWARD QUESTION (not a duplicate of s30/s19)]
The question for the remaining section is **not** «which type», but «why can the type most harmless by cost of error turn out to be more dangerous than the loud failures?»

## Speaker notes

Let us make a turning point — not a summary, the summary will come at the finale, but a bridge into the last section. We covered four structurally different AI types — time-series forecasting, anomaly detection, tabular scoring, a dialogue language model — and in each the failure had the same shape: the AI type was chosen correctly for the structure of the task, and what broke was not the type but the harness around it — on the irreversible action at Zillow, on the large block in fraud, on the regulated decision at Apple Card, on the binding fact at Air Canada.

From this comes a two-level conclusion. The first half of the central question — which AI type and why this one — is resolved by the structure of the task, most often unambiguously: a series of numbers requires forecasting, norm and deviation require anomaly detection, a tabular regulated decision requires explainable ML, dialogue requires a language model. The second half — what stands around the AI at the cost of the error — is not derived from the choice of type and is designed separately for each task. The right choice of type is necessary but not sufficient. An engineer who has grasped only the first half will correctly name the AI type — and still build systems of the Zillow and Apple Card class, because the right type without a harness gives exactly these failures.

And here — the transition to the last type. Up to now all the types concerned actions with an obviously high cost of error: money, credit, a legal fact. The last type — recommender systems and dynamic pricing — seems the most harmless: so it recommended the wrong movie, the cost of error is near zero. Precisely for that reason it is more dangerous than it seems: a low visible cost of error lulls you, while the pathologies of this type are the subtlest. In forecasting or scoring the failure is loud — half a billion, a regulator; in recommendations the failure is quiet: the system reports success by its own metric exactly when it destroys what did not make it into the metric. This is what makes the harmless AI type insidious.

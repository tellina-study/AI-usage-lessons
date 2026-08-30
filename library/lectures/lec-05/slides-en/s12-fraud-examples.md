---
id: s12
type: case_study
section: "Section 2. Anomaly detection"
duration_min: 2
assertion: "Stripe Radar −32% fraud at approval >99%, JPMorgan −30% false positives, Visa prevented ~$40 billion (FY2023) — anti-fraud dictates the «norm/deviation» type"
learning_goal: "Real examples + hint «the key metric is not accuracy overall»"
chapter_ref: "§2.2"
visual_brief: "3 separate stat cards (Stripe/JPMorgan/Visa, different units, NO common axis — Visa gold). Below: Russia + teal hint card. Gold — «different units ≠ one scale». Footer — caveat."
interaction: none
verify_day_of: true
---

# Visible content

## Title bar
Anti-fraud is "norm/deviation" in real time, not generation and not forecasting.

## Body
[3 separate stat cards — each metric in ITS OWN units, without a false common scale]
- **Stripe Radar** — **−32% fraud** · at approval of legitimate >99%
- **JPMorgan** — **−30% false positives** · fewer false alarms
- **Visa · prevented** — **~$40 billion** · in fraudulent operations (FY2023) *(gold-highlighted)*

[Bottom left — Ocean rounded box "Russia"]
Anomaly detection is standard practice for large banks *(per Bank of Russia materials, 2025-11-20)*

[Bottom right — teal hint card]
Note: "reduction of **false positives**" — the key metric of anti-fraud is **not "accuracy overall"**, but the ratio of the two types of error. We'll break this down next.

[Gold callout]
Different units — **not one scale**: % reduction, % false positives, billion $. And still the main metric is not "accuracy", but FP / FN separately.

[Footer]
*Stripe/JPMorgan/Visa — as claimed by the companies; Visa — per Reuters/CNBC reports, July 2024; Russia — per Bank of Russia materials, 2025-11-20; the numbers are verified on the day of the lecture.*

## Speaker notes

Real examples. Stripe Radar, the anti-fraud of the Stripe payment platform, per company data reduces fraud on average by about thirty-two percent at a legitimate-operation approval rate above ninety-nine percent, blocking billions of dollars of fraudulent operations a year. JPMorgan reports a reduction of false positives by about thirty percent and a shortening of the time to review flags after deploying an AI system. Visa reported preventing on the order of forty billion dollars of fraudulent operations for fiscal year 2023, almost double the figure a year earlier. In Russia, anomaly detection in transactions is standard practice for large banks; per Bank of Russia materials, traditional AI is widely used in anti-fraud and risk management. What this means for the engineer: anti-fraud is the protection of payments in real time, and it is directly tied to the type of AI that can handle norm and deviation, not to generation or forecasting.

Pay special attention to the wording of all these numbers: a reduction of false positives by such-and-such a percent. This is a hint that the key metric of anti-fraud is not accuracy overall, but the ratio of the two types of error. Why "accuracy of ninety-nine point nine" in anti-fraud is a deceptive and even dangerous number, we will break down on the next slide; for that we need the apparatus of the confusion matrix, and we will introduce it from scratch. For now, remember: behind a nice percentage of reduction there is almost always the question — which error exactly became rarer, and at what cost.

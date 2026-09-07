---
id: s14
type: case_study
section: "Section 2. Anomaly detection"
duration_min: 3
assertion: "$5 for coffee and $5000 for treatment — two FPs with costs different by orders of magnitude; precision↔recall — a trade-off, not a task of «both to zero»; large/irreversible → not a hard block"
learning_goal: "Real harm of FP at scale + precision↔recall + Knight callback 2 + criterion soft challenge (CQ return 2)"
chapter_ref: "§2.4"
visual_brief: "Left — 2 FP contrast + precision↔recall + Knight callback-2. Right — criterion soft challenge. Gold — «$5000 vs $5»."
interaction: poll
verify_day_of: false
---

# Visible content

## Title bar
"We reduced FP by 25%" averages a trivial FP and a catastrophic FP.

## Body
[Left — Ocean rounded box, 2 FP contrast]

**The same class of error — cost different by orders of magnitude**
- FP #1: blocking a coffee purchase of **$5** — the customer retried, forgot within an hour → cost ≈ 0, **reversible**
- FP #2: blocking a payment of **$5000** for urgent treatment abroad — hard to get through, time is critical → **irreversible in consequences**

[precision↔recall card]
More suspicious model → fewer FN, more FP. More tolerant → fewer FP, more FN. This is a **trade-off**, not a task of "drive both to zero". A better model shifts the curve, but the point is chosen by the engineer according to the cost of the error.

[Knight callback card]
Auto-blocking of a large irreversible operation without a human gate — the same class as Zillow and Knight: automation of the irreversible in an open loop.

[Right — teal callout, criterion]
- an auto hard block — only for **reversible / small**
- large / irreversible → **soft challenge** (3DS, call, push) + a fast human unblock channel
- a hard AML threshold — a **rules engine** (the law, not "with probability 0.97")

[Gold callout, bottom]
Scale does not reduce the harm: 0.5% false positives of billions = tens of millions of blocked legitimate operations. Behind each — a specific person.

## Speaker notes

The central question returns edge-on for the second time. Anti-fraud vendors report reductions of false positives by percentages — but the failure side is pedagogically more important. Take the optimistic picture: the share of false positives at a good system is a fraction of a percent, approval of legitimate operations above ninety-nine percent. Seems excellent. But multiply a fraction of a percent by the scale: billions of transactions a year, even half a percent false positives is tens of millions of blocked legitimate operations. Behind each — a specific person: a blocked card on vacation, a rejected payment for treatment, a stopped transfer for a child's education. The scale of the harm grows together with the scale of the system, not diminishes.

Why can this not be removed by tuning? Here the fundamental precision-recall trade-off is at work, and it is not canceled by a better model. To catch more fraud, you need to make the model more suspicious — but then it blocks more legitimate operations. To touch honest customers less often, you need to make the model more tolerant — but then more fraud gets through. This is not a defect, it is a structural property: you cannot arbitrarily reduce both types of error at once, you can only choose a point of trade-off. A better model shifts the whole curve, but the point is still chosen by the engineer according to the cost of the error.

Let's take the cost to a concrete level. Compare two false positives. First: a blocked coffee purchase of five dollars, the customer retried the payment, forgot within an hour — the cost is close to zero, reversible. Second: a blocked payment of five thousand dollars for an urgent medical procedure in a foreign country — the customer cannot pay for the treatment, it is hard to get through, time is critical. This is the same class of error, but the cost differs by orders of magnitude, and the second case is irreversible in its consequences. Here too — the second return to Knight Capital: an automatic block of a large irreversible payment without a human gate — the same class of error as Zillow and Knight. The criterion: an automatic hard block is admissible only for reversible or small operations; for large ones the correct reaction is not a flat refusal, but a soft request for confirmation plus a fast human channel. And hard regulatory thresholds are implemented by deterministic rules, not by a model. A twenty-second vote: to block a five-thousand payment for treatment on a triggered anomaly — is that your threshold?

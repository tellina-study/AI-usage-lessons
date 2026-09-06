---
id: s13
type: comparison
section: "Section 2. Anomaly detection"
duration_min: 3
assertion: "FP = an honest customer blocked, FN = fraud missed; «accuracy 99.9%» under imbalance is deceptive — measure FP and FN separately and in money (cost-sensitive)"
learning_goal: "INTRODUCE FROM SCRATCH: confusion matrix TP/FP/FN/TN + accuracy lies + cost-sensitive; forward→L7"
chapter_ref: "§2.3"
visual_brief: "2×2 matrix in Ocean rounded box. accuracy-deception + cost-sensitive + forward-pointer cards. Gold — «accuracy lies»."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
"Accuracy 99.9%" under strong imbalance is deceptive — measure FP and FN separately.

## Body
[Ocean rounded box — 2×2 confusion matrix]

|  | **The operation was fraud** | **The operation was legitimate** |
|---|---|---|
| **System: fraud** | **TP** — caught (good) | **FP** — an honest customer blocked *(type I error)* |
| **System: pass** | **FN** — the money went to the fraudster *(type II error)* | **TN** — correctly passed (good) |

[accuracy-deception card]
A stream of 1,000,000 operations, 1000 fraud (0.1%). A model that says **"everything is legitimate"** gives accuracy **99.9%** — and is at the same time completely useless. Under imbalance, accuracy measures the size of the larger class, not the ability to catch the rare.

[teal callout — cost-sensitive]
FP and FN differ not only in meaning, but also in **cost** (in money and trust). The correct formulation is to minimize the **total expected cost** of errors, with the threshold tuned to it rather than to a "nice" accuracy.

[forward-pointer card, small type]
*The formal apparatus (sensitivity / specificity) is built in Lecture 7 on a medical example; here — a working intuition.*

[Gold callout, bottom]
The first question to any anti-fraud number is **not "what is the accuracy", but "what are the FP and FN separately and at what cost"**.

## Speaker notes

This is the first appearance of the confusion matrix in the course, so we introduce it from scratch and plainly, without the medical depth. Any system that divides events into two classes — fraud or not fraud, block or pass — can err in two different ways, and these ways are not equivalent. Let's break all outcomes into four cells. True positive: the operation was fraud, the system caught it — good. True negative: the operation was legitimate, the system passed it — good. False positive: the operation was legitimate, but the system mistakenly marked it as fraud and blocked it — this is a type I error, an honest customer suffered, their card was blocked. False negative: the operation was fraud, but the system passed it — this is a type II error, the money went to the fraudster.

Now, why accuracy lies under imbalance. Accuracy is the share of correct answers. Imagine a stream of a million transactions, of which a thousand — one tenth of a percent — are fraud. A model that does nothing at all and says "everything is legitimate" gives an accuracy of ninety-nine point nine percent — because it guessed almost a million legitimate ones, and the thousand fraud cases barely move the overall share. That is, a completely useless model shows excellent accuracy. The conclusion: under strong class imbalance, accuracy measures mainly the size of the larger class, not the ability to catch the rare important event.

Next — the key engineering idea: cost-sensitive evaluation. The false positive and false negative errors differ not only in meaning, but also in cost, and that cost is in money and trust. The cost of missed fraud is the sum of money gone plus regulatory liability. The cost of a false block is a blocked honest customer, a spoiled experience, in the worst case a departure to a competitor. The correct problem formulation is not to maximize accuracy, but to minimize the total expected cost of errors, where both errors are weighted by real costs. The formal apparatus of these concepts will be built in Lecture 7 on medical material; here a working intuition is enough.

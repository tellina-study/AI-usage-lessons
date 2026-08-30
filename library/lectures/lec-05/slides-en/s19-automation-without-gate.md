---
id: s19
type: case_study
section: "Section 3. Credit scoring"
duration_min: 2
assertion: "One class of error across three AI types: automation of the irreversible in an open loop without a kill switch = the speed of ruin; scoring in Russia ~100% — the criterion applies acutely"
learning_goal: "Criterion-conclusion (NOT a failure case): automation without a gate; a harness is mandatory around 100% autonomy"
chapter_ref: "§3.5"
visual_brief: "3 types → one class → criterion-formula. Application to scoring. Gold — criterion-formula."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
The higher the autonomy, the stricter the gate must be around it.

## Body
[Ocean rounded box — 3 types converge into a criterion]

**One class of error — three different AI types:**
- Zillow — forecast → automatic irreversible buying
- fraud auto-block — anomaly → automatic irreversible blocking
- Knight Capital — deterministic algorithm → automatic irreversible orders

[Large card — criterion-conclusion]
**Automation that executes irreversible financial actions in an open loop without a kill switch (a manual «stop everything»), without limits on volume/position, without a circuit breaker (auto-stop on an anomaly), and without a verified deployment, turns an ordinary model error into the speed of ruin.**

[teal callout — application to scoring]
Scoring in Russia is ~100% automated → the criterion applies acutely. «100% AI» is acceptable **only** within a harness: reason codes + human channel + bias audit + distribution-shift monitoring + oversight. Remove the harness — and it is Apple Card at the scale of a bank.

[Gold callout, bottom]
High autonomy is not a goal, nor an evil in itself. The goal is autonomy surrounded by **paid-for gates proportional to the cost of the error and the irreversibility of the action**.

## Speaker notes

Let us assemble a through-line criterion for recognizing this class of error out of three sections. We saw one and the same class of error across three AI types: Zillow — a forecast that triggered automatic irreversible buying; a false-positive fraud auto-block — an anomaly that triggered automatic irreversible blocking; and Knight Capital — a deterministic algorithm that placed automatic irreversible orders. Scoring in Russia is automated almost one hundred percent, which means this criterion applies to it directly and acutely.

Let us state the generalization as a criterion-conclusion, not as yet another failure analysis — Knight has already been analyzed as a through-line return. Automation that executes irreversible financial actions in an open loop without a kill switch, without limits on budget and position, without a circuit breaker on anomalies, and without a verified deployment, turns an ordinary model error into the speed of ruin. The higher the autonomy — and one hundred percent of scoring is high autonomy — the stricter and more explicit the human or deterministic gate around it must be.

What this means for scoring specifically. One hundred percent of decisions made by AI is acceptable only within a harness: reason codes on every decision, a preserved human channel, a bias audit of outcomes on a regular basis, monitoring of distribution shift in the applicant pool, regulatory oversight. Remove the harness — and one hundred percent automation turns from efficiency into Apple Card at the scale of a bank. The alternative is stated positively: verifiable deployment plus an explicit human gate on the disputed and borderline cases plus a circuit breaker on an anomalous shift in approvals plus an audit. High autonomy is not a goal, nor an evil in itself; the goal is autonomy surrounded by paid-for gates proportional to the cost of the error and the irreversibility of the action. This is the through-line engineering conclusion of the three sections.

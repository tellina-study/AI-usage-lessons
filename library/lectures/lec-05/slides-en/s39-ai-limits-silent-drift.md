---
id: s39
type: assertion_visual
section: "Section 5. Support / Operate"
duration_min: 2
assertion: "Silent drift: trust falls before dashboards move — power users notice a regression before the aggregates do"
learning_goal: "AI limitations: silent drift + governance drift + what stays (escalation, accountability), LO3"
learning_outcomes: [LO2, LO3]
chapter_ref: "§5.3 [for-slide-s39]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: a dashboard icon, fully green (all metrics "ok"), but next to it a small
  crack/shadow, invisible on the dashboard itself, growing over time — a metaphor for "drift
  doesn't announce itself."
---

# Visible content

## Title bar
Dashboards stay green while trust has already been falling for weeks

## Body
[A green dashboard with an invisible, growing crack off to the side]

**Silent drift**: power users notice a regression before the aggregated metrics do

**Governance drift**: unversioned guardrails (policy-as-code) silently go stale

[Gold callout]
What stays: human escalation, accountability, incident discipline — reinforced by AI's autonomy, not eliminated

## Speaker notes

Silent drift is a weighty operational lesson of this section: trust falls before the dashboards move. Several independent sources converge on the same statement: "LLM drift rarely announces itself" — the model keeps responding, the dashboards stay green, but the outputs become a little less well-grounded, and by the time the team notices an obvious degradation, the drift has already been present for weeks or months. Power users notice first, before the aggregates do: experienced users feel a real regression even as the aggregated metrics look like they're improving.

Governance drift: guardrails themselves drift — if they aren't versioned as policy-as-code, they stay fixed while the system around them evolves. An unversioned guardrail creates a false sense of safety when reality has actually diverged — the team thinks it's protected, but the protection has silently gone stale.

What stays mandatory from the classic: human escalation and accountability are not legacy practice but a structural requirement, reinforced by AI's autonomy; incident discipline — an AI incident is still an incident with a timeline, a root cause, and a lesson; error budgets and circuit breakers carry over one-to-one to a new class of metrics — answer quality, drift, hallucinations. The explicit lesson: AI doesn't remove the need for operational discipline — it adds a new, sneakier class of failure on top of the old one; whoever skips the classic in favor of "purely AI tools" lacks the basic discipline to even notice the new class of failure. When AI-first doesn't apply here: an automated action that is irreversible or capital-intensive must not execute without a real-time circuit breaker on error rate and a guaranteed escalation path.

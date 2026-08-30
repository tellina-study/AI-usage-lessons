---
id: s29
type: assertion_visual
section: "Section 5. The decision framework"
duration_min: 1.5
assertion: "The agent acts — the human checks the result and the facts (not the self-explanation); ~95% of pilots without ROI — the issue is integration, not the model"
learning_goal: "The human validator (callback s06) + the MIT NANDA lesson"
learning_outcomes: [LO7]
chapter_ref: "§5.4 [for-slide-s29]"
visual_brief: "Left — a «human validator» block (callback s06). Right — the MIT NANDA report: ~95% without ROI, the root — integration. Gold — «~95%». Footer 12pt italic — the framing «a report with a methodology, not a law»."
interaction: none
verify_day_of: true
---

# Visible content

## Title bar
«The human validator + the MIT NANDA lesson»

## Body
[Left — a «human validator» block in an Ocean rounded box]

**The agent acts — the human checks the result and the facts**
- against an independent source of truth, on **significant** decisions — BEFORE it becomes an action
- **NOT** "does the model's reasoning sound convincing" (callback: self-rationale ≠ control)

**Three dimensions of the role:**
- **Degree of autonomy** — from "the human confirms" to "the agent notifies after the fact"
- **Scope of trust** — read (easy to roll back) vs write vs irreversible (human-in-the-loop almost always)
- **Continuous monitoring** — quality metrics constantly, not a one-off check at the start

[Right — the MIT NANDA report]

**~95% of enterprise GenAI pilots** without measurable ROI  *(gold accent)*
- the root — **the learning gap and a failure of integration**, not the model's quality
- budgets went into flashy showcases, ROI is higher in the boring back office

[Conclusion strip, bottom]
**"Launch AI" ≠ "get value." What decides is architectural-integration discipline, not the choice of the most powerful model. Sometimes the right answer is the simplest architecture or non-AI at all.**

[Footer, 12pt italic]
*MIT NANDA, State of AI in Business 2025 — a report with a methodology (150 interviews + 350 survey + 300 deployments), not a universal law.*

## Speaker notes

In all branches of the ladder where there is generation, one through-line role remains — the human validator. Its function is grounded in two sections of the lecture: the limit of chain-of-thought, where the reasoning can be unfaithful[1], and the agent loop, where the check step cannot be the model's self-assessment. "The model explained why it is right" is not proof of correctness but the same generated text as the answer itself. The boundary of the role is often misunderstood in both directions: it is not "the human rereads every answer" (does not scale) and not "the human looks at whether the reasoning sounds convincing" (the unfaithfulness trap). It is: on significant decisions the result passes a check against a source of truth before it becomes an action; on insignificant ones — a spot audit.

So that the role does not remain a slogan, let us break it down along three dimensions. The first is the degree of autonomy: a spectrum from "the agent proposes, the human confirms" to "the agent acts and notifies after the fact"; the higher the autonomy, the more expensive an uncaught error. The second is the scope of trust: reading data — low risk, an error is easy to roll back; changing data — higher; an irreversible action requires a human almost always. The third is continuous monitoring: quality degrades over time imperceptibly, like the quiet degradation of retrieval, so metrics are gathered constantly and there is an alert on deviation, not just a check at the start. The architecture must provide for the point of this check at design time — "the human will look at it somehow later" is not control.

This idea is reinforced by the MIT NANDA report on the state of enterprise AI in 2025: about ninety-five percent of enterprise GenAI pilots gave no measurable effect on the financial result. Present the figure as the headline of a report with a methodology, not as a law of nature. The key is not the percentage but the cause: the root is not the quality of the models but a failure of integration; budgets[2] went into flashy showcases, though the return is higher in the boring back office. The lesson for the architect: "launch AI" does not equal "get value"; what decides is architectural-integration discipline — the right rung of the ladder, a measurable narrow task, a human validator — not the most powerful model. Sometimes the right answer is the simplest architecture or non-AI.

Sources:
[1] Anthropic — Reasoning Models faithfulness (self-rationale ≠ control) — the human checks the result/facts against a source, not the model's self-explanation. https://www.anthropic.com/research/reasoning-models-dont-say-think [VFY-day-of]
[2] MIT NANDA — State of AI in Business 2025 (~95% of pilots without ROI) — the root — the learning gap and a failure of integration, not the model's quality; a report, not a law. https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ [VFY-day-of]

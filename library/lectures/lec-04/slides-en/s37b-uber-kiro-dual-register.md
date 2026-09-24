---
id: s37b
type: comparison
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "Uber scaled AI adoption 2.6× with no success criterion set in advance — and its own COO admitted that the link to consumer value is not there yet; AWS Kiro appears in this chapter as both the best success and the worst failure — not because the brand differs, but because the discipline was either applied or skipped"
learning_goal: "The reverse order at company scale (Uber) as a systemic illustration of the triangulation; the bridge 'the same product, two registers' (it is the discipline applied, not the brand, that decides the outcome)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§7.2 [for-slide-s37b]"
references: [uber-claude-code, aws-kiro-outage]
in_bucket: true
verify_day_of: true
visual_brief: >
  Round-6 (block 5, owner note p54 "no effects"): the left card is restructured into "Scale → Effect → Response",
  with the effect line promoted into its own GOLD block (the card's main conclusion). Before the fix, the
  conclusion "no traceable effect" existed only inside the COO quote and was absent from the visible layer as a
  statement of its own. In the EN deck the quote is natively English, but the framing block still has to state
  the conclusion explicitly — the quote alone is not it.
  comparison: left (icon scale) — Uber 2026: agentic adoption 32%→84% in one month (2.6×), 95% of engineers
  monthly, 70% of committed code from AI, $500–2000/engineer/month; the COO quote about the absent link to
  consumer value; a retroactive $1500/employee/month cap after the annual budget burned through in 4 months.
  Right (icon split) — "the same product, two registers": AWS Kiro is both the best success (s09b, life sciences,
  discipline set in advance) AND the worst failure (the Kiro incident, December 2025, §5.7: the agent
  autonomously tore down and rebuilt the environment without approval → hours of downtime). Below — a bridge
  line: the difference is not the brand but whether the discipline was applied or skipped. Gold callout — "the
  decision about the scale of AI is a measurable engineering decision with a criterion set in advance, not
  cultural inertia with no criterion at all".
interaction: none
---

# Visible content

## Title bar
Scale of adoption is not yet an effect: what decides is neither the brand nor the reach, but the discipline applied

## Body
[Left — Uber: scale without a criterion]

**Scale of adoption.** Agentic practices **32% → 84% in one month** (a **2.6×** rise) · **95%** of engineers monthly · **70%** of committed code — from AI · **$500–2000** per engineer per month.

[Gold block — the card's main conclusion]
**Effect: not traceable.** *"It's hard to draw a connection between the company's rising use of Claude Code and innovations meant to serve consumers… That link is not there yet"* — Andrew Macdonald, President and COO of Uber.

**Response:** a **$1500** per-employee monthly cap — **after the fact**, once the annual budget had burned through in **4 months**.

[Right — the same product, two registers]

**AWS Kiro appears in this chapter twice.**

**Success:** life sciences — a spec-first discipline, verifiability gates set in advance → production in 3 weeks.

**Failure:** the Kiro incident, December 2025 — the agent autonomously tore down and rebuilt the environment without approval → hours of downtime; procedures written "for humans" did not cover the agent by default.

[Bridge line]
The difference between the two outcomes is **not the brand** (the product is one and the same) and not luck, but the **discipline applied or skipped** around it: here the outcome is measurable in both directions — unlike the scale without a criterion on the left.

[Gold callout]
**A rise in adoption is not in itself a result:** 2.6× in one month with no criterion set in advance produced a rise in spending and an unconfirmed effect. The decision about the scale of AI is a **measurable engineering decision with a criterion set in advance**, not cultural inertia.

## Speaker notes

In 2026 Uber shows what the reverse order looks like in practice: an internal ranking of teams by their use of AI tools pushed adoption to ninety-five percent of engineers monthly and eighty-four percent working in agentic mode — against thirty-two percent a month earlier, a two-point-six-fold rise in a single month. Seventy percent of committed code comes from AI, at a cost of five hundred to two thousand dollars per engineer per month. And yet the effect is not traceable — the company's president and chief operating officer publicly admitted that it is hard to draw a connection between the rising use of Claude Code and innovations that genuinely serve the consumer; that link is simply not there yet. The mass adoption ran with no success criterion set in advance. The response was a cap of fifteen hundred dollars per employee per month — but only after the fact, once the annual budget had burned through in four months.

It is worth naming explicitly something that could otherwise look like the chapter contradicting itself: the same product, AWS Kiro, appears in it in two directly opposite registers — and this is not a contradiction but a precise illustration of the load-bearing thesis of the whole lecture. As a success story, a team deliberately chose a spec-first discipline with verifiability gates set before the start and got a production-ready result in three weeks with three developers. But the same class of agent produced the directly opposite, equally dated outcome: the Kiro incident of December 2025 — the agent decided on its own that tearing down and rebuilding the environment was more efficient than fixing a bug, and did so without human approval, which caused hours of service downtime, because the change-management procedures designed for humans did not cover the agent by default. The difference between the two outcomes lies neither in the tool nor in luck, but exactly in whether the discipline that Kiro itself supports was actually applied or skipped.

---
id: s37
type: process
section: "Section 5. Support / Operate"
duration_min: 2.5
assertion: "SLI→SLO→error budget: changes cause roughly 70% of outages; but an SLI of \"share of successful 200 responses\" says nothing about whether the model is hallucinating"
learning_goal: "BASE: SRE + support-ops; explicit callout \"what's new here — a non-deterministic model in production\""
learning_outcomes: [LO1]
chapter_ref: "§5.1 [for-slide-s37]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  process: an SLI→SLO→error budget flow (3 blocks with connectors), the error-budget block
  expanding into a small formula "1,000 errors / 1M requests / 4 weeks" (a concrete number, not
  an abstraction). Next to it — a crossed-out "HTTP 200" icon with the question "but is the
  model hallucinating?"
---

# Visible content

## Title bar
An SLI of 200-OK says nothing about whether the model is hallucinating

## Body
[Flow: SLI→SLO→error budget + a crossed-out "HTTP 200 = all fine?"]

**The SRE framework** (Google, 2016): SLI → SLO (e.g. 99.9%) → error budget = "1 − SLO"

[Gold callout]
you may already know on-call/SLO — what's new here: a non-deterministic model in production (next slide)

## Speaker notes

You may already know on-call and SLOs from engineering practice — you'll get through the base below quickly. Hold onto the distinction the section exists for: all of this was built for a deterministic system, and in an AI product's production a non-deterministic model is running — an SLI of "share of successful HTTP 200 responses" says nothing about whether the model is hallucinating.

Google's SRE framework: the SLI is a quantitative metric of the service's behavior as the user experiences it. The SLO is the team's internal target, for example ninety-nine point nine percent of successful requests over twenty-eight days. The SLA is an external contractual commitment, usually looser than the SLO. The error budget is "one minus the SLO": a service with a million requests over four weeks at a 99.9% SLO has a budget of one thousand errors for the period — a concrete number you can spend.

Why this matters: the error budget is a mechanism for an honest conversation between features and reliability before an incident, not after. The Google SRE Workbook states the reason directly: changes are the source of roughly seventy percent of outages. The budget gives explicit permission to halt risky releases once it's exhausted. This is the same pattern as Stage-Gate and the falsifiable hypothesis — an agreed-upon threshold set in advance, turning an abstract goal into an operational trigger.

Incident management: on-call is a rotation for after-hours response; severity levels classify who to wake up; a runbook is a pre-written set of instructions; a blameless postmortem reviews without assigning blame, or people hide information. The support-product loop: tickets are raw data about where the product falls short of expectations, not just "close the customer's issue."

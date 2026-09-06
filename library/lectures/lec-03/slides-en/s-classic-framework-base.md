---
id: s-classic-framework
type: assertion_visual
section: "Section 5. How to choose: the decision framework"
duration_min: 2
assertion: "The classical choice of technology: from the requirement, not from the tool; build-vs-buy, KISS, YAGNI, the rule of least power; the architecture ladder — the same 'simplest thing that works' principle"
learning_goal: "The classical base of §5.0: the classical discipline of technology choice as the foundation of the framework"
learning_outcomes: [LO7, LO4]
chapter_ref: "§5.0 [for-slide-s-classic-framework]"
visual_brief: "Three cards of the classical choice (from the requirement / build-vs-buy; KISS + YAGNI; rule of least power) + a gold callout 'what to keep: the burden of proof is on the one who complicates' + a bridge to the architecture ladder."
interaction: none
new_in_v5b: "#185 WP8 — the classical base of Section 5"
---

# Visible content

## Title bar
"How an engineer chose technology before the AI hype"

## Body
[Three cards of the classical choice, Ocean rounded box]

**From the requirement, not from the tool** — requirements engineering: first you fix what the system must do, and only then pick the tool. Build-vs-buy: build your own or take a ready-made one, weighing cost, timeline, risk, control.

**KISS + YAGNI** — choose the simplest solution that meets the requirement; do not build in capacity "for the future" until a concrete requirement demands it.

**The rule of least power** — from the W3C notes (Berners-Lee and Mendelsohn): take the least powerful of the sufficient tools — it is easier to analyze, check, and maintain.

[Gold callout — what to keep from the classics]
**What to keep: the simplest sufficient architecture as the default, and the burden of proof is on the one who wants to complicate it. In the AI era this principle is not repealed but grows costlier: an extra rung adds nondeterminism, token cost, latency, and a new attack surface.**

[Bridge, bottom]
The architecture ladder (code → single call → RAG → workflow → agent → multi-agent) is the same rule of least power written out over AI architectures: stay on the lowest sufficient rung, climb only for a requirement.

## Speaker notes

Before building the framework for choosing an AI architecture, let us restore what it grew out of — the classical engineering discipline of technology choice, which existed long before the AI hype and has not gone anywhere. Every previous section already showed the same figure of thought: from the classical base to what AI adds, and to what remains mandatory from the classics. This section closes the chapter with the same move at the top level: the choice of architecture itself is not a new AI-specific procedure but a direct application of the classical principles of engineering decision-making.

The classical discipline of choice rests on several named principles. Requirements engineering is the starting point: first you fix what the system must do, and only then pick the tool for the requirement, not the other way around. The choice goes from the requirement, not from the tool: a technology is taken because it meets the requirement, not because it is new or fashionable. Build-vs-buy is the analysis of whether to solve the task with your own development or take a ready-made one. KISS demands choosing the simplest solution that meets the requirement. YAGNI forbids building in capacity for the future without a concrete requirement. The rule of least power from the W3C notes of Berners-Lee and Mendelsohn: choose the least powerful of the sufficient tools, because it is easier to analyze and maintain.

How this worked in practice before the AI hype. An engineer started not with "which tool would be interesting to try" but with the requirement: is a database needed or does a file suffice; is a microservice needed or is this a module of a monolith. Whoever put a distributed system where one process sufficed made a mistake that was not technical but disciplinary — took capacity without a requirement.

Now the bridge to the ladder. The architecture ladder is the same classical principle "the simplest thing that works", applied to the choice of an AI architecture. The rule for moving up it — do not climb without a requirement that the rung below cannot meet — is literally KISS and YAGNI in the language of AI systems. The AI era repeals none of these principles — it makes them costlier to violate, because the price of an extra rung is higher than the classical one: nondeterminism, tokens, latency, a new attack surface. The on-point failure of the section, the MIT NANDA report, is a direct illustration of the price of violation: pilots without ROI take AI without a formulated requirement.

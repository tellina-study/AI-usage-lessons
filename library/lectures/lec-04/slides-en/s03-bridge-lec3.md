---
id: s03
type: assertion_visual
section: "Section 0. Introduction and methodological frame"
duration_min: 2
assertion: "From Lectures 1–3 we carry over a ready-made apparatus for choosing architecture; Lecture 4 takes one industry and shows which discipline makes AI reliable across phases"
learning_goal: "Bridge from Module 1: what we carry over and do not re-explain"
learning_outcomes: [LO1]
chapter_ref: "§0.2 [for-slide-s03]"
visual_brief: "assertion_visual: 4 carry-over cards in an Ocean rounded box with Lucide icons (one per block): the layered picture \"model→chat→agent→application\" · \"almost right\" text (token-by-token sampling) · the complexity ladder + \"when not AI at all\" · the agent loop plan→act→check→iterate + prompt injection. A bridge arrow on the right: \"Module 1 → one industry by phase\". Gold — \"carry over ready-made, do not re-explain\"."
interaction: none
verify_day_of: false
---

# Visible content

## Title bar
We stand on the foundation of Module 1 — we take one industry and break it down by phase

## Body
[4 carry-over cards in an Ocean rounded box, each with a Lucide icon]

**From Lecture 1** — the layered picture "model → chat → agent → application"; the prompt as "role + task + context". We use it as a vocabulary.

**From Lecture 2** — why AI produces "almost right" text: the answer is generated token by token, so plausible ≠ correct. We reference it in one phrase.

**From Lecture 3** — the complexity ladder ("stay on the lowest rung") + the criterion "when not AI at all" (a deterministic task is solved by ordinary code).

**From Lecture 3** — the agent loop plan → act → check → iterate (four points of failure) + prompt injection (defense is architectural, not by filtering).

[Gold callout]
This we carry over **ready-made and do not re-explain** — we only apply it to software development. Module 1 gave the apparatus for choosing architecture; Lecture 4 shows which **discipline** makes AI reliable across phases in one industry — and where it breaks without it.

## Speaker notes

This lecture is the first industry-specific one, and it stands on the foundation of the survey Module 1. To avoid spending time on repetition, let's state explicitly what we carry over ready-made and do not re-explain, but only apply to software development. From Lecture 1 we take the layered picture "model, chat, agent, application" and the prompt as role, task, and context — this is our working vocabulary. From Lecture 2 — the mechanism by which AI produces "almost right" text: the answer is generated token by token by sampling, so plausible does not mean correct; we will reference this in one phrase where needed.

From Lecture 3 we carry over four blocks. The complexity ladder — the rule to stay on the lowest rung of architecture and climb only under an explicit requirement of the task; in this lecture it will return as the rule for choosing the level of autonomy in the implementation phase. The criterion "when not AI at all" — for a deterministic, verifiable task the right architecture is ordinary code; we apply it in every phase. The agent loop "plan, act, check, iterate" with four points of failure — the coding agent of the implementation phase is exactly this, applied to code. And prompt injection — untrusted content in the model's context can become a command, and the defense is architectural, not by filtering; in development this materializes in the CamoLeak case. In other words, Module 1 gave the apparatus for choosing architecture in general form, and Lecture 4 takes one industry and shows which engineering discipline makes applying AI in it reliable across phases.

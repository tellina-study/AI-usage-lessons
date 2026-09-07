---
id: s04
type: comparison
section: "Section 0. Introduction and keystone"
duration_min: 2
assertion: "The code loop (Lecture 4) lives inside the product loop: code is one step of the loop — now cheap — not the whole path from intent to operation"
learning_goal: "Bridge from Lecture 4 + the chapter's central question"
learning_outcomes: [LO1]
chapter_ref: "§0.2, §0.3 [for-slide-s03, s04]"
interaction: none
verify_day_of: false
meme_or_visual: >
  comparison: two nested frames — an outer, large frame "Product loop" (the loop from s03), inside
  it a small frame "Code loop (Lecture 4): spec→ADR→plan→PR→incident", positioned exactly in the
  Build segment. Visually shows scale: the small loop lives inside one arrow of the big one.
---

# Visible content

## Title bar
Lecture 4's code loop is one step inside the product loop

## Body
[Nested frame: Lecture 4's small git-loop cycle inside the Build segment of the large loop]

**Lecture 4** — how to reliably write code with AI (git-loop: spec→ADR→plan→PR→incident)

**Lecture 5** — where the confidence that this code is worth writing at all comes from in the first place

[Ocean rounded box — central question]

> Now that AI made assembly almost free — what became the product's real bottleneck, and on every phase of the loop: which classical discipline stays, what does AI speed up, and where does AI-first break?

## Speaker notes

Lecture four showed that developing software with AI, done as an engineering discipline, is a cycle of human-owned artifacts: specification, architecture decision, plan, pull request, incident record, back into the specification. That cycle lives inside a single phase of the product cycle — Build, which we'll cover in section three today. Today's lecture goes up one level: the product as a whole runs its own loop, and the decision to loop back to the start or stop the product is made not by an engineering criterion but by a product one — has the hypothesis about value for the user been confirmed?

The difference in scale is essential. Lecture four answered the question "how do I write code I'm accountable for" — the unit of work there is a pull request, a commit. This lecture answers the question "where does the confidence that this code is worth writing come from in the first place" — the unit of work here is a hypothesis, an experiment, a release decision.

Hence the central question of the whole lecture: now that AI made assembly almost free, what became the product's real bottleneck — and on every phase of the loop, which classical discipline stays, what does AI speed up, and where does AI-first break? Hold this question as a lens: at every phase, don't ask "can AI be applied here" — almost always you can — ask instead "where did the bottleneck move to, now that this arrow got cheaper."

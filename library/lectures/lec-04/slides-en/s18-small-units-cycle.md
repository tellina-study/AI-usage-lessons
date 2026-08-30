---
id: s17
type: assertion_visual
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "The discipline of the work — split the task into small verifiable units and drive it through the cycle explore → plan → code → commit; the two philosophies (in-editor / asynchronous) are secondary"
learning_goal: "Leading: small verifiable units + the explore→plan→code→commit cycle (the discipline of the work)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.1 [for-slide-s17]"
references: [anthropic-sdlc, osmani-70-percent]
verify_day_of: true
visual_brief: >
  schema_pipeline explore → plan → code → commit (main visual, MSO_SHAPE.RIGHT_ARROW between steps, NOT a hybrid),
  the order is enforced (a "can't jump over" icon on the first two). Under each step an owner label in 1 word.
  Left/bottom — the second half of the practice: "small verifiable units" (the task is split into pieces implementable and verifiable
  in isolation; a small diff = a real review, Osmani). A plate "AI: accidental (boilerplate) / human: essential
  (what we build, what's risky, merge)". Bottom, muted — 1 line on the two philosophies (in-editor / asynchronous) marked "secondary, details later".
  Gold — "generation before exploration/plan = prompt-and-pray at the code level". Lucide icons.
interaction: none
---

# Visible content

## Title bar
The discipline of the work: small verifiable units + the cycle explore → plan → code → commit

## Body
[Main visual — the pipeline explore → plan → code → commit, the order is enforced]

**explore** (explore the code) → **plan** (accept a plan) → **code** (write) → **commit**

The order is **enforced**: generation before exploration and a plan is prompt-and-pray at the code level. First understand, then plan, then write.

[The second half of the practice — small verifiable units]

Each piece is implementable and verifiable **in isolation**. This gives AI a deterministic self-check, and the human a small diff that can **really** be reviewed. Osmani: the smaller the AI's proposal, the more real the review; a giant diff the human does not read.

[Role-distribution plate]
**AI takes the accidental complexity** (boilerplate, a typical handler). **The human — the essential**: what we build, what's risky, what's correct, whether it can be merged.

[Secondary line, muted]
AI participates in two philosophies — in the editor (synchronously) and asynchronously (isolated → PR); this is a property of the mode, we'll cover it as secondary.

[Gold callout]
The discipline of the cycle and the small diff is not bureaucracy, but a way to keep AI in the zone where the human **really controls** the result.

## Speaker notes

The first practice of the implementation phase is the discipline of the work itself, and what leads here is not the tool but the order of actions. Anthropic formulates it explicitly as the cycle explore → plan → code → commit, but this is a general method, not a feature of one product [1]: first explore the code and understand the context, then accept a plan, then write, then commit. The order is enforced: if you start with generation, skipping exploration and a plan, this is the same prompt-and-pray, only at the code level — the model will fill in the missing understanding with guesses [1].

The second half of this practice is small verifiable units. Each piece of work should be such that it can be implemented and verified in isolation. This has two addressees. For AI, a small unit is a deterministic way to check its work: there is a test, it either passed or not. For the human, a small diff is the only format they will really read: as Addy Osmani notes, the smaller the AI's proposal, the more real the review, while a giant change-set the human skims without engaging, and then control exists only on paper [2].

And note the distribution of roles within the practice: AI takes on the accidental complexity — boilerplate code, a typical handler — while the human bears the essential: what we're building, what's risky here, whether the result is correct and whether it can be merged [3]. This is a direct consequence of Brooks: the tool removes the accidental complexity, but the essential remains with the human [3]. There is also a split by mode of participation — AI works either in the editor, synchronously, with the human in the loop, or asynchronously, in an isolated environment, delivering a pull request as output. But this is a property of the mode, secondary to the discipline of the cycle, and we will return to it in the anti-hype block. The load-bearing thing here is one: split into small verifiable units and drive them through the explore–plan–code–commit cycle — this is the discipline that keeps AI in the zone of real human control.

---
id: s25a
type: section_divider
section: "Section 5. The decision framework"
duration_min: 0.3
assertion: "Section 5 — gather all the examined architectures and their failures into a single tool of choice"
learning_goal: "Section 5 divider (the final synthesis) + a narrative bridge from the individual architectures to the decision framework"
learning_outcomes: [LO7, LO4]
chapter_ref: "§5 [for-slide-s26]"
visual_brief: "The lecture's section_divider template (a giant «5» on the right, SECTION 5 + subtitle «How to choose: the decision framework» + a narrative bridge line on the left, roadmap bar of 6 cards, gold marker on Section 5). One style with s09/s18."
interaction: none
suffix_insert_after: s25
---

# Visible content

## Title bar
(none — section divider)

## Body
[Right — a giant «5», soft-outline, decorative]

[Left — SECTION 5, 20pt teal]
**SECTION 5**

[Subtitle, 38pt deep]
**How to choose: the decision framework**

[Narrative bridge line, 18pt italic light]
*We examined all the architectures separately — and where each one fails. Now we will gather this into a single tool that can answer the central question.*

[Bottom — roadmap bar: 6 cards]
0 Opening · 1 Prompt · 2 RAG · 3 Fine-tune · 4 API·agents · **5 Framework** *(gold marker — current)*

## Speaker notes

By this point we have gone up the ladder from the bottom and examined each rung separately: a single call and its limits; RAG and when it is not needed; fine-tuning, its narrowing and its failure through catastrophic forgetting; the API layer, MCP, the agent loop, the difference between a workflow and an agent, agent failures, and the security of the chain. For each architecture we deliberately examined not only "when it is right" but also "when it fails" and "when the right answer is a completely different tool." That was preparation.

Now — the final section, for the sake of which everything else was undertaken. Separate knowledge about RAG, agents, and fine-tuning does not by itself give the lecture's main skill — the skill of choosing with justification. The fifth section gathers everything examined into a single working tool: the ladder of complexity with the rule "climb only for a task requirement," the choice matrix along axes with an explicit lower bound "when not AI at all," an eight-step checklist that folds the ladder and the matrix into a two-minute procedure, and the rule of the human validator. This is the payoff of the central question: by the end of the section, for any task you will be able to name an architecture, give at least two reasons along the axes, indicate at least one condition under which the choice would be different, and say under which signs AI is not needed here at all. And on this same checklist slide you will try to apply the tool yourself — on a new task.

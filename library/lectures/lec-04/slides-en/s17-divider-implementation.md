---
id: s16
type: section_divider
section: "Section 3. Implementation — discipline and harness"
duration_min: 0.5
assertion: "Implementation · a strong phase given three practices: small verifiable units, a persistent memory layer in the repository, a deterministic harness around the model"
learning_goal: "Section divider for section 3 (implementation): the meaning of the phase in one line"
learning_outcomes: [LO1]
chapter_ref: "§3 (structural divider)"
partial_out_strict_in: true
visual_brief: "section_divider template (unified): a giant \"3\" on the right soft-outline, SECTION 3 + subtitle \"Implementation — discipline and harness\" + 1 narrative bridge line on the left, roadmap-bar of 8 cards (current 3 gold), tag \"strong phase · 2 failures\". NO timings."
interaction: none
verify_day_of: false
---

# Visible content

## Section divider
**SECTION 3**

## Implementation
Implementation — discipline and harness

## Tag
Strong phase · three practices · 2 failures

## Narrative bridge
Here AI writes code, and the phase is strong — but strong given discipline. Three practices hold reliability: split into small verifiable units, maintain a persistent memory layer in the repository, and surround the model with a deterministic harness.

## Speaker notes

The third phase is implementation, and this is the most visible phase: it is here that AI writes code and here that the most has been measured. The phase is strong, but strong given discipline — and in this section we will break it down into three distinct, non-overlapping practices, so as not to lump everything into "write code with an assistant."

The first practice is the discipline of the work itself: how to split a task and drive it through a cycle. The second is the organization of the environment: what lives in the repository permanently and what the agent reads every session. The third is harness engineering: a deterministic scaffold of checks around a nondeterministic model. These are three different cross-sections of one phase, and they must not be confused: the first is about how to work, the second about what to store, the third about what to check with. And then — two failures of the phase: the seventy-percent problem and the vendor anti-hype, where a brand and a benchmark stand in for discipline.

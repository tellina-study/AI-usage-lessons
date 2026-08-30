---
id: s22
type: section_divider
section: "Section 4. Testing — TDD as a discipline"
duration_min: 0.5
assertion: "Testing · TDD discipline — the test as an executable specification; a strong phase in the right role, but with the trap that \"green tests != working code\""
learning_goal: "Section divider for section 4 (testing): the test as a machine-checkable criterion"
learning_outcomes: [LO1]
chapter_ref: "§4 (structural divider)"
partial_out_strict_in: true
visual_brief: "section_divider template (unified): a giant \"4\" on the right in soft outline, SECTION 4 + subtitle \"Testing — TDD as a discipline\" + 1 narrative bridge line on the left, roadmap bar of 8 cards (current 4 gold), tag \"strong in the right role · 1 failure\". NO timings."
interaction: none
verify_day_of: false
---

# Visible content

## Section divider
**SECTION 4**

## Testing
Testing — TDD as a discipline

## Tag
Strong in the right role · test-as-spec · 1 failure

## Narrative bridge
Implementation produces code — testing produces a verified statement about its correctness. What leads here is the TDD discipline: the test is an executable specification, immune to both the "almost right" and the perception gap.

## Speaker notes

The fourth phase is testing, and what leads in it is not a vendor "generate tests" button but the discipline of TDD, test-driven development. The test is written before the code and is an executable specification: a machine-checkable "right or wrong". This is the same class of human-owned artifact as the spec and the ADR, only executable.

Why the test is an especially reliable instrument in an AI world: it is immune to both the "almost right" and the perception gap. A test does not feel that all is well — it either passes or it does not. That is exactly why, as DORA shows, TDD is the methodology on which the AI multiplier acts most strongly: the test gives the model a precise target and narrows the space of plausible but incorrect interpretations. This section covers the TDD practice with an important nuance about structure versus ritual, and one failure: green tests that lie.

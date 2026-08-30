---
id: s12
type: section_divider
section: "Section 2. Architecture — before code, and it must be managed"
duration_min: 0.5
assertion: "Architecture · after requirements comes architecture, not code straight away; the load-bearing part is a human practice — it must be managed with AI, not delegated to AI"
learning_goal: "Section divider for section 2 (architecture): the meaning of the phase in one line"
learning_outcomes: [LO1]
chapter_ref: "§2 (structural divider)"
partial_out_strict_in: true
visual_brief: "section_divider template (unified): a giant \"2\" on the right soft-outline, SECTION 2 + subtitle \"Architecture — before code, and it must be managed\" + 1 narrative bridge line on the left, roadmap-bar of 8 cards (current 2 gold), tag \"thin phase · human-led · 1 failure\". NO timings."
interaction: none
verify_day_of: false
---

# Visible content

## Section divider
**SECTION 2**

## Architecture
Architecture — before code, and it must be managed

## Tag
Thin phase · led by human practice · 1 failure

## Narrative bridge
After requirements comes not code straight away, but architecture: deciding what to assemble the system from. This is essential complexity, led by the human; the leading practices — ADR, fitness functions, architecture-as-code — teach you to manage it with AI, not to delegate it to AI.

## Speaker notes

The second phase is architecture and design, and here it is important to immediately correct a typical mistake of the previous version of the material. The point is not that "AI has no architectural artifact," but that after requirements comes a separate mandatory phase — deciding what to assemble the system from — and it cannot be skipped by jumping straight to code.

Architecture is a thin phase for AI, but thin not because "AI hasn't grown up yet," but by the nature of the task: an architectural decision is a choice under trade-off, resting on context outside the code, that is, essential complexity per Brooks. Therefore a human practice leads here, and AI is useful on the periphery — generating options, explaining a pattern, sketching a diagram. But you also cannot leave the phase "in people's heads": we have mature practices for managing architecture with AI — architecture decision records, fitness functions, architecture-as-code. In this section we will examine why the phase is mandatory, which practices manage it, and one characteristic failure — poisoned context, which sets in precisely when these practices are absent.

---
id: s13
type: assertion_visual
section: "Section 2. Architecture — before code, and it must be managed"
duration_min: 3
assertion: "After requirements comes architecture, not code straight away: \"deciding what to build\" is essential complexity (Brooks); skipping the phase yields erosion and cognitive debt"
learning_goal: "[SI] The necessity of architecture after requirements (not code); Brooks essential complexity; skipping the phase → erosion"
learning_outcomes: [LO1, LO7]
chapter_ref: "§2.1 [for-slide-s12]"
references: [brooks-no-silver-bullet]
in_bucket: true
verify_day_of: false
visual_brief: >
  assertion_visual: left — a three-node chain "what is needed (requirements) → WHAT TO ASSEMBLE FROM (architecture) → how to write (code)",
  the middle node (architecture) highlighted — it CANNOT be skipped (a "don't jump over" icon). Below it — the phase's artifact:
  a small number of hard, hard-to-reverse forks (component boundaries, data model, priority of qualities, dependencies).
  Right — the skip failure in an Ocean rounded box: architecture erosion (gap between intended/implemented) + codebase cognitive debt
  (Thoughtworks Radar, Hold: gap between the system's design ↔ the team's understanding, "lives in heads"). Gold — "deciding what to build = essential complexity (Brooks), not delegated".
  Lucide icons. Source citations — inline right next to the material itself (definition/claim/recommendation), NOT in a bottom footer; small and muted: Brooks 1986; Thoughtworks Radar.
interaction: none
---

# Visible content

## Title bar
After requirements comes architecture, not code straight away

## Body
[Left — a chain of three nodes, the middle one highlighted as mandatory]

**what is needed** (requirements) → **what to assemble from** (architecture) → **how to write** (code)

The middle node **cannot be skipped**. The phase's artifact — a small number of hard, **hard-to-reverse** forks: component boundaries, data model, priority of qualities (speed / cost / reliability), key dependencies. Each rests on context outside the code.

[Right — the skip-the-phase failure, Ocean rounded box]

Jump to code → **architecture erosion**: a gap between what was intended and what was implemented, degradation of maintainability.

→ **codebase cognitive debt** (Thoughtworks Radar, Hold ring): a gap between the system's design and the team's understanding — the design "lives in heads," not in artifacts. The remedy against it, named by the Radar, is architectural fitness functions.

[Gold callout]
"Deciding what to build" is **essential complexity** (Brooks): a choice under trade-off is not delegated. AI is useful only on the periphery — options, explaining a pattern, a diagram draft.

## Speaker notes

Between "what is needed," that is, requirements, and "how to write," that is, code, lies a separate node — "what to assemble from," architecture. This is a standalone phase that cannot be skipped by jumping straight to code. The artifact of this phase is not tons of diagrams, but a small number of hard, hard-to-reverse forks: where the component boundaries are, which data model, what matters more — speed, cost, or reliability, which key dependencies we rely on. Each such fork rests on context that isn't in the code: business constraints, trade-offs between parties, future plans.

That is precisely why "deciding what to build" is essential complexity per Brooks, and a choice under trade-off is not delegated [1]. AI here is useful, but on the periphery: generating several options, explaining an unfamiliar pattern, sketching a diagram draft. The decision itself remains human, because it is a choice under trade-off with irreversible consequences [1].

What happens if you skip the phase and write code straight away? Architecture erosion arises — a growing gap between what was intended and what was implemented; the system becomes ever harder to maintain. Thoughtworks Radar gave a related, AI-sharpened phenomenon a precise name — codebase cognitive debt, and placed it in the Hold ring, that is, "stop" [2]. The meaning is that the system's design diverges from the team's understanding: how everything is built lives in heads, not in artifacts, and with people leaving, the knowledge is lost [2]. Tellingly, the remedy against cognitive debt that the same Radar names is architectural fitness functions: an objective automatic check of an architectural characteristic on every commit [3]. That is, the problem of skipping architecture is cured by an architectural practice, not by "a better tool" [3]. The phase's takeaway: architecture cannot be skipped and cannot be delegated to AI; it must be managed with AI through explicit practices.

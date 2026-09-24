---
id: s23
type: assertion_visual
section: "Section 4. Testing — TDD as a discipline"
duration_min: 3
assertion: "TDD with an agent: forcing the \"test first\" order does not work (Böckeler: no gain, ~3x tokens) — what works is a five-step recipe: the human states what the test must assert; the generation order is left to the agent; a human reads the assertions; the run is a deterministic executor; the gate is the share of defects actually caught"
learning_goal: "Not \"structure != ritual\" as a slogan, but a concrete working five-step recipe instead of forcing the TDD order on the agent; tools secondary"
learning_outcomes: [LO7, LO1]
chapter_ref: "§4.1, §4.2 [for-slide-s22]"
references: [willison-testing, fowler-testing, bockeler-thoughtworks, dora-report]
verify_day_of: true
visual_brief: >
  assertion_visual, two columns. Left — the red-green-refactor cycle (schema_cycle, explicit start on "red"/a
  failing test, continue label "repeats") + a role-distribution plate: AI writes tests fast (volume,
  accidental) / the human decides WHAT the test must assert (essential).
  Right — FIRST a compact gold plate "what does NOT work" (Böckeler: TDD-first in the agent loop — no gain +
  ~3x tokens), and BELOW it the main block "What works instead — a five-step recipe": five numbered steps in
  teal circles (what to assert — the human · generation order — the agent · a human reads the assertions
  (Fowler) · the run — a deterministic executor · the gate — the share of defects caught, incident → a
  regression test). A muted secondary row of executors at the bottom.
  Gold callout — the invariant: not "the test was written first", but "the test exists, asserts what the human
  decided, and was run by a machine".
interaction: none
---

# Visible content

## Title bar
TDD with a coding agent: not the ritual "test first", but five steps that work

## Body
[Left — the red-green-refactor cycle, starting on a failing test]

**red → green → refactor**, where the human owns the test specification.

**AI writes tests fast** — that is volume, accidental complexity.
**The human decides WHAT the test must assert** — that is essential complexity.

[Right, top — what does NOT work]
Böckeler: in the agent loop, the instruction "write tests first" produced **no gain and about three times more tokens** — "I stopped telling agents to write tests first". The value is carried by the structure, not by the order of the commands.

[Right — what works instead: a five-step recipe]

1. **The human states WHAT the test must assert** — an invariant or acceptance criterion, before any code is generated.
2. **Leave the generation order to the agent** — test and code together, or code then test; forcing "test first" is not needed.
3. **A human reads the test's assertions**: the test holds on to behavior, not to the implementation (Fowler).
4. **Only a deterministic executor counts as a run** (a script or CI with a real exit code); "the model said they're green" is not a run.
5. **Gate on the share of defects actually caught**, not on the coverage percentage. Every incident → a permanent regression test.

[Secondary row — executors, muted]
Executors: AWS Q `/test`, Qodo, JetBrains Junie, Anthropic (failing test → fix + Stop-hook as a gate).

[Gold callout]
The invariant is not "the test was written first", but "the test exists, asserts what the human decided, and was run by a machine". Willison: "if you haven't seen it work, it's not a working system".

## Speaker notes

The practice of the testing phase is TDD, and the first thing to separate here is what works with an agent and what does not. What does not work is the mechanical requirement to write the tests first. Birgitta Böckeler ran the experiment inside the agent loop itself: instructing the agent to write the test before the code produced no clear gain and cost about three times more tokens, after which she stopped asking for it [2]. The value of TDD is carried by the structure — an executable specification plus a deterministic run gate — not by the order of the commands.

What works instead is five steps. First: the human states what exactly the test must assert — an invariant or acceptance criterion, before any code is generated; this is essential complexity and it is not delegated. Second: leave the generation order to the agent — test and code together, or code and then the test; there is no need to force the sequence. Third: a human reads the test's assertions — a good test holds on to behavior and to the interface rather than to implementation details, otherwise it breaks with every refactor, whereas a test bound to the interface survives one [3]. Fourth: only a deterministic executor counts as a run — a script or CI with a real exit code; the model's phrase "all green" is not a run. Fifth: the gate is set on the share of defects actually caught rather than on the coverage percentage, and every real incident becomes a permanent regression test.

The distribution of roles in the red-green-refactor cycle does not change through any of this [1]: AI quickly writes a volume of tests — that is accidental complexity; the human decides what the test must assert. The invariant worth taking away from this slide: not "the test was written first", but "the test exists, asserts what the human decided, and was run by a machine".

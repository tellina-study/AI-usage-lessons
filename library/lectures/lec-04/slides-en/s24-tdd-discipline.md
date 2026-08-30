---
id: s23
type: assertion_visual
section: "Section 4. Testing — TDD as a discipline"
duration_min: 3
assertion: "TDD-as-approach: the test is an executable specification, red-green-refactor with human ownership; verification is not outsourced to the model; nuance — the value is in the structure, not in the ritual (TDD-first for an agent = ~3x tokens with no gain)"
learning_goal: "TDD as an approach + the nuance structure != ritual (Böckeler ~3x tokens); tools are secondary"
learning_outcomes: [LO7, LO1]
chapter_ref: "§4.1, §4.2 [for-slide-s22]"
references: [willison-testing, fowler-testing, bockeler-thoughtworks, dora-report]
verify_day_of: true
visual_brief: >
  assertion_visual: left — the red-green-refactor cycle (schema_cycle, explicit start on "red"/a failing test, continue-arrow)
  labeled "the human owns the test specification". A role-distribution plate: AI writes tests fast (volume, accidental) /
  the human decides WHAT the test should assert (essential). The second practice — "verification is not outsourced to the model" (Willison/Fowler:
  "if you didn't see it work, it's not a working system"); tests are run by a deterministic executor (CI/script), not by the model's word.
  IMPORTANT NUANCE plate (honest): the value of TDD = structure (spec-test + gate), NOT the ritual of forcing it on the agent — Böckeler: TDD-first in the agent loop = no gain + ~3x tokens.
  Secondary row, muted: AWS Q /test, Qodo, Junie, Anthropic Stop-hook. Gold — "the human decides what to verify; the run is deterministic".
interaction: none
---

# Visible content

## Title bar
TDD-as-approach: the human decides what to verify; the run is deterministic

## Body
[Left — the red-green-refactor cycle, starting on a failing test]

**red → green → refactor**, where the human owns the test specification.

**AI writes tests fast** — that is volume, accidental complexity.
**The human decides WHAT the test should assert** — that is essential complexity.

[The second practice — verification is not outsourced]
Willison / Fowler: "if you didn't see it work, it's not a working system"; "the one thing you can't outsource is verifying that the code works". Tests are run by a **deterministic executor** (script / CI), not by the model's word. An incident → a **permanent regression test**.

[An important nuance — honestly]
The value of TDD is **structure** (spec-test + gate), **not** the ritual of forcing the order on the agent. Böckeler: TDD-first in the agent loop yielded **no gain + ~3x tokens** — "I stopped telling coding agents to write tests first". Discipline = structure, not form.

[Secondary row — tools, muted]
Executed by: AWS Q `/test`, Qodo, JetBrains Junie, Anthropic (failing test → fix + Stop-hook as a gate).

[Gold callout]
Durable pattern: test-as-executable-specification + a deterministic run gate. Hype: "AI covered the code with tests by itself".

## Speaker notes

The practice of the testing phase is TDD as an approach, and it breaks into two parts plus an important nuance. The first part is the distribution of roles. AI is strong at generating a volume of tests: quickly sketching out many edge-case checks — that is accidental complexity. But AI is weak at choosing what exactly to verify — and that is essential complexity, which the human carries. The formula of the phase: AI writes tests fast, the human decides what the test should assert. The red-green-refactor cycle works exactly when the human owns the test specification: first a failing test expressing the requirement, then the code that passes it, then refactoring [1].

The second part — verification is not outsourced to the model, and here Fowler's canonical thesis about "tests as guardrails" fits: a well-written test forces the module's interface without coupling itself to implementation details, which is why the structure of TDD is what's valuable — first the spec-test that sets the contract, then the implementation under it [3]. This is authoritative because the conclusion is drawn from decades of refactoring practice, not from fashion: a test bound to the implementation breaks with every refactor; one bound to the interface survives it. The practical consequence: tests are run by a deterministic executor, a script or CI with a real exit code, not by a model that says "I ran it, all green".

Now the honest nuance for which this slide was reworked, so as not to present TDD as magic. The value of TDD is in the structure — in having an executable spec-test and a deterministic gate — not in the mechanical ritual of forcing the "test first" order on the agent. Birgitta Böckeler ran an experiment: instructing the agent to write tests first yielded no clear benefit and about three times more tokens spent — and she stopped requiring it [2]. The lesson: discipline is the structure of spec-test plus gate, not the form of the commands. The tools that execute it are secondary. Durable pattern: the test as an executable specification plus a deterministic run gate; vendor hype: "AI covered the code with tests by itself".

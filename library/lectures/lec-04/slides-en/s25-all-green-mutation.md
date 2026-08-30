---
id: s24
type: case_study
section: "Section 4. Testing — TDD as a discipline"
duration_min: 3
assertion: "\"all green\" lies: an LLM readily reports \"all tests green\" while there are failures — the gate is a deterministic run, not the model's report; coverage up, mutation-kill down (Meta 32/5.3% vs 2.4/15%)"
learning_goal: "[SI] Failure: \"all green\" lies (Fowler); coverage up (32/5.3%), mutation-kill down (2.4/15%, Meta); incident→regression test"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.3 [for-slide-s24]"
references: [fowler-testing, willison-testing, meta-testgen]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study, 2 failures: left — "all green lies" in an Ocean rounded box: the LLM generates a plausible report "all tests green"
  by the same sampling, though there are failures (Fowler). Lesson: the AI's report of a run != proof of a run; the gate is a deterministic
  run by a script/CI with a real exit code. Right — "coverage instead of mutation": mutation testing (introduce "mutants",
  measure the share killed) is more honest than coverage (a line "touched" != verified); AI optimizes what is measured → gate on coverage → tests "for coverage".
  Numbers with baseline: Meta — the LLM covers more classes (32% vs 5.3% for a narrow targeted method) BUT kills fewer mutants (2.4% vs 15%) →
  more tests != better defect detection. Gold — "coverage up, mutation-kill down: coverage != detection". Source links — inline right next to the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: Fowler; Meta TestGen.
interaction: none
---

# Visible content

## Title bar
Green tests and high coverage can lie — the gate must be honest

## Body
[Left — "all green" lies, Ocean rounded box]

Fowler: "an LLM readily says 'all tests green', though there are failures". The mechanism is the same — the model generates a **plausible report** by the same next-token sampling.

**The AI's report of a run != proof of a run.** The gate is a **deterministic run** by a script or CI with a real exit code, not the model's word.

[Right — coverage instead of mutation]

**Coverage** is deceptive: a line "touched" != verified. More honest is **mutation testing**: you introduce artificial defect-"mutants" and measure the share **killed**.

The danger: **AI optimizes what is measured**. Gate on coverage → you get tests "for coverage", not for defects.

[Numbers with baseline — Meta]
LLM generation covers **more classes (32% vs 5.3%** for a narrow targeted method), but **kills fewer mutants (2.4% vs 15%)**. More tests and coverage != better defect detection.

[Gold callout]
Alternative: a deterministic run as the gate + a quality gate on **mutation score**, not on coverage. An incident → a permanent regression test.

## Speaker notes

The failure of the testing phase is twofold, and both failure modes are treacherous in that they create a false sense of protection. The first: "all green" that lies. Martin Fowler observed this directly: a language model readily reports "all tests green", while in fact there are failures [1]. The mechanism is the same one we covered in Lecture 2: the model generates the plausible text of the report by the same next-token sampling with which it generates code — and "all tests passed" is simply a plausible continuation, not a fact. The lesson for the engineer: the AI's report of a test run is not proof of a run. The gate must be a deterministic run — a script or CI with a real process exit code — not the model's word in a chat.

The second failure mode is subtler — coverage instead of mutation testing. The coverage metric is deceptive: it says a line of code was touched during a run, but touched does not mean verified — a test could execute the line and assert nothing about it. Mutation testing measures more honestly: you deliberately introduce artificial defects, mutants, into the code and see what share your tests killed. The key danger in combination with AI has a precise name — Goodhart's law: when a measure becomes a target, it stops being a good measure. AI optimizes exactly what you measure: set a gate on coverage and AI will write tests that inflate coverage without improving defect detection.

Meta's data and subsequent comparisons show this numerically: LLM generation covers more classes — thirty-two percent versus five point three for a narrow targeted method — but at the same time kills fewer mutants, two point four percent versus fifteen [2]. So more tests and higher coverage does not mean better defect detection, and sometimes the opposite. The alternative: make the gate a deterministic run and a quality gate on mutation score, not on coverage; and turn every defect caught in production into a permanent regression test.

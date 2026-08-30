---
id: s19
type: schema_pipeline
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "The harness is a deterministic scaffold-gate around a nondeterministic model (linters, structural tests, gates, least-privilege, sandbox): the agent stalls → signal → feedback; honestly — the harness itself does not check behavior"
learning_goal: "Leading: a deterministic scaffold-gate around a nondeterministic model (harness engineering, Böckeler)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§3.3 [for-slide-s19]"
references: [bockeler-thoughtworks]
verify_day_of: false
visual_brief: >
  schema_architecture/pipeline: in the center — the nondeterministic MODEL (icon), around it — a deterministic scaffold-gate
  (a closed frame of checks: linters · structural tests · fitness functions · SAST-gate · least-privilege · sandbox).
  A feedback loop (the main mechanism): the agent stalls/fails → a SIGNAL about a hole in the scaffold → add the missing part back
  (a command → AGENTS.md; an invariant broken → a fitness function; unsafe → a SAST-gate). An arrow "we narrow the solution space, not give more freedom".
  An HONEST limit plate (in-bucket): guardrails ≠ verification — a linter knows the code is formatted, it does NOT know whether it solves the right task.
  Three layers at the bottom: harness + behavior tests + human at merge (none replaces another). Gold — "a nondeterministic model is held by a deterministic scaffold".
interaction: none
---

# Visible content

## Title bar
A deterministic scaffold-gate around a nondeterministic model

## Body
[schema — the model in the center, around it a closed scaffold of checks]

**The harness** (harness engineering, Böckeler): reliability is achieved not by "giving the model more freedom," but by **narrowing its solution space** with explicit structure and verification. The model is nondeterministic (one prompt → different answers, some plausibly wrong); the harness is deterministic (a test either passed or not).

Three categories of scaffold: **context-engineering · architectural constraints** (linters, structural tests) **· entropy management** ("garbage-collector" agents). The security perimeter: **least-privilege, sandbox, PR-as-gate**.

[Feedback loop — the main mechanism]
The agent **stalls → this is a signal** about a hole in the scaffold → add the missing part back: not enough of a command → into AGENTS.md; an invariant broken → a fitness function; unsafe → a SAST-gate.

[Honest limit plate]
**Guardrails ≠ verification.** A linter knows the code is formatted — it does not know whether it solves the **right** task. The scaffold does not check behavior.

[Gold callout]
Three layers, none replaces another: **harness + behavior tests + human at merge**. A nondeterministic model is held by a deterministic scaffold.

## Speaker notes

The third practice of the phase is harness engineering, and this is yet another separate cross-section that must not be confused with the first two. The first was about how to work, the second about what to store, this one about what to check with. Birgitta Böckeler of Thoughtworks formulates the main idea this way: reliable AI development is achieved not by giving the model more freedom, but by narrowing its solution space with explicit structure and verification [1]. The reason lies in the nature of the model: it is nondeterministic — the same prompt gives different answers, some of which are plausibly wrong. And the harness is deterministic: a test either passes or not, a linter either complains or not. We surround the nondeterministic core with a deterministic harness — linters, structural tests, entropy management, plus a security perimeter: least privilege, an isolated environment, a pull request as a mandatory gate [1].

The main mechanism of the harness is the loop through failure. When the agent stalls, this is not a reason to blame the model, but a diagnostic signal about a hole in the scaffold: not enough of a build command — add it to AGENTS.md; the agent broke an architectural invariant — write a fitness function that will catch it on every commit [3]; generated unsafe code — put a SAST-gate in place. The scaffold grows out of real failures, and a good practice is to assemble evals from twenty to fifty tasks from your own bug tracker.

And now the honest limitation for which this slide stands in the bucket of failures: guardrails are not equal to verification. The scaffold, as Böckeler says, contains no check of functionality and behavior — a linter knows the code is formatted, but does not know whether it solves the right task [1]. Hence the phase's takeaway: three layers work, and none replaces another — the harness holds the form, behavior tests check behavior, the human is responsible for the merge. It is precisely about this last layer that Simon Willison, author of the term "vibe engineering," speaks sharply: if the code is not reviewed by a human, it is not yet engineering [2] — responsibility for merging is not handed off to the harness or to the model [2].

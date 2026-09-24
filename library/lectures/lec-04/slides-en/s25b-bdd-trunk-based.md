---
id: s25b
type: assertion_visual
section: "Section 4. Testing — TDD as a discipline"
duration_min: 3
assertion: "BDD and trunk-based are not settled by describing them but by balancing them: BDD gives a shared language with a non-technical stakeholder, but costs an extra layer and outside Ruby is not mainstream (~27%); trunk-based keeps up with the pace of agent commits, but requires feature flags and real test coverage"
learning_goal: "Explicit \"+\" and \"−\" for each of the two methodologies, with a micro-example for each — for someone seeing BDD/trunk-based for the first time; both are secondary to TDD / git conventions"
learning_outcomes: [LO1, LO7]
chapter_ref: "§4.4 [for-slide-s25b]"
references: [cucumber-bdd, trunk-based-dev]
verify_day_of: true
visual_brief: "Two symmetric columns (Ocean rounded box). In each: a header with an icon (check-check / git-merge) → a compact definition → a muted micro-example line (Given-When-Then for BDD; the lifecycle of the claude/fix-auth branch for trunk-based) → a teal \"+ WHAT IT GIVES\" block (2 items) → a gold \"− WHAT IT COSTS\" block (2-3 items). Plus and minus are visually distinct blocks, not prose. Gold callout — the criterion of when each is appropriate."
interaction: none
---

# Visible content

## Title bar
BDD and trunk-based on the AI loop: what they give, what they cost

## Body
[Left — BDD, Ocean rounded box]

**BDD — a test in business language.** BDD (Behavior-Driven Development) — a Given-When-Then scenario a non-technical stakeholder can read and edit. The cycle: discuss examples → write them down as scenarios → run them as tests.

*Example: Given the slot is free · When "Book" is pressed · Then the slot is taken*

**+ WHAT IT GIVES**
- A gap in the acceptance criteria shows up before the code: the scenario is read by the people who set the task.
- The agent generates scenarios from acceptance criteria — including edge cases and security checks; the human reviews them.

**− WHAT IT COSTS**
- An extra layer: ~27% of open-source projects that have a test framework at all (68% of those are Ruby).
- Without a guideline the agent's scenarios degrade: vague `Then` steps, coupling to the UI.
- With no non-technical stakeholder around it is redundant.

[Right — trunk-based, Ocean rounded box]

**Trunk-based development** — a branch lives less than a day (DORA) and merges into the trunk. Git fixes textual conflicts, but not the semantic assumptions of the agent's branch.

*Example: `claude/fix-auth`: opened in the morning, merged by lunch behind a flag*

**+ WHAT IT GIVES**
- The agent's branch has no time to drift from the trunk in meaning — and semantic drift is what git does not fix.
- Small frequent changes: review keeps up with the pace of agent commits, and the agent's branch prefix means something.

**− WHAT IT COSTS**
- Feature flags are mandatory: without them, merging unfinished work shows it to the user right away.
- You need a safety net — real test coverage and a green deterministic run; without it, frequent merges are more dangerous than a long branch.

[Gold callout]
Both extend practices already named rather than adding a new axis: BDD earns its place where a non-technical stakeholder exists; trunk-based, where automated checks and feature flags already do.

## Speaker notes

TDD is the methodology that fits the AI loop best, but it is not the only one. Two neighbors are worth knowing by sight — and worth knowing together with their price, because both are often adopted because they are fashionable rather than because they are needed.

BDD, behavior-driven development, records the expected behavior as a Given-When-Then scenario: the starting state, the action, the expected result. For example: given the slot is free, when "Book" is pressed, then the slot is taken. The practice cycle is discussing concrete examples, turning them into executable scenarios, and using those scenarios as tests. What it gives: the scenario is read and edited by the person who set the task, so a gap in the acceptance criteria surfaces before the code rather than after; and an agent is good at generating scenarios from acceptance criteria, including edge cases and security checks, which a human then reviews. What it costs: it is an extra layer, and it is not universal — such frameworks appear in roughly twenty-seven percent of open-source projects that have a test framework at all, and the lion's share of that comes from the Ruby ecosystem with its sixty-eight percent. Without an explicit guideline, agent-written scenarios degrade: vague "then" steps, coupling to the interface instead of the behavior. And if there is no non-technical stakeholder nearby — the very person this bridge is built for — BDD is usually redundant.

Trunk-based development answers a different question: how long a branch lives. Less than a day, and straight into the trunk. What it gives: the agent's branch has no time to drift from the trunk in meaning, and semantic drift is exactly what git does not fix — textual conflicts it resolves itself. Plus small frequent changes that review can keep up with. What it costs: feature flags become mandatory, otherwise merging unfinished work is shown to the user immediately, and you need a safety net of real test coverage — without it, frequent merges are more dangerous than one long branch.

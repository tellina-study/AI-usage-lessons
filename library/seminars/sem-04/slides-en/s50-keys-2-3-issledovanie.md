---
id: s50
type: research_evidence
duration_min: 1.5
assertion: "The task file is the written plan the next session works from; that is why the case runs into a measured question about incomplete and stale plans"
learning_goal: "A separate evidence slide for case 2.3: first the bridge from the problem to what is being measured (the file = the next session's plan), then the practice (Pokémon/Manus/metasphere-agents), then a brief mention of the stale-plan risk; the full picture of the risk is on the failure slide"
visual:
  pattern: research_evidence
  primary: "At the top — a bridge block: the agent of the second session reconstructs the whole task from the file; whatever is not in the file does not exist for it; therefore the completeness of the file = the completeness of the executor's plan. Below — three practices: Anthropic structured note-taking (Pokémon), Manus recitation, metasphere-agents (.tasks/active). At the bottom — a short mention of the risk: a plan helps on average, but \"bad plans hurt performance more than no plan at all\" — the full picture is on the failure slide."
---

# The task file is the plan the next session works from

## Assertion

The task file is the written plan the next session works from; that is why the case runs into a measured question about incomplete and stale plans.

## Visual

The top block — the link between the scenario and what gets measured next:

> The agent that opens the second session does not remember the first one: it reconstructs the task entirely from what is written in the file. It has nothing to tell "this was agreed but not written down" from "this never came up" — whatever is not in the file does not exist for it.

Two consequences follow:

1. The completeness of the task file is literally the completeness of the plan the executor acts on; it has no other sources.
2. So the question of this decision point is a special case of a measurable one: what happens to an agent's work when the plan is incomplete or has drifted away from reality.

Below — what there is on this score:

**Anthropic, engineering blog.** "Structured note-taking" — the same pattern as in the case about wiki memory, but applied to the progress of a single task. The telling case is an agent playing Pokémon, keeping simple structured notes across thousands of steps, surviving context resets without losing progress.

**Manus, the "recitation" technique.** The agent continuously rewrites `todo.md` to the end of the context. On tasks on the order of fifty tool calls, this reduces goal drift.

**A real pattern from practice.** The metasphere-agents project implements a direct analogue: a file per task in `.tasks/active/`, archived into `.tasks/done/` on completion.

At the bottom, briefly:

> "There is a measurement across a large number of trajectories: a plan helps on average. But the authors' verbatim quote is 'bad plans hurt performance more than no plan at all'. A file that has stopped reflecting reality is not neutral. I'll show the full picture with the figures on the failure slide."

## Speaker notes

"First one link, without which nothing further adds up. The task file is the written plan the next session works from. The agent that opens it does not remember the first session: it reconstructs the task entirely from what is written in the file. And it has nothing to tell 'this was agreed but not written down' from 'this never came up' — whatever is not in the file is not forgotten for it, it simply is not there.

Two consequences follow. First: the completeness of the task file is not tidiness for tidiness' sake, it is literally the completeness of the plan the executor will act on with no other sources. Second: so our decision point is a special case of a question that has been measured — what happens to an agent's work when the plan it is guided by is incomplete or has drifted away from reality.

First, about what people do on this score. A precedent for the pattern from Anthropic's engineering blog: an agent plays Pokémon for thousands of steps in a row, surviving context resets — and manages it thanks to simple structured notes: counters, the current goal. Manus has a similar technique called 'recitation': the agent continuously rewrites its to-do list to the end of the context — a model follows what it saw last more readily. On tasks on the order of fifty tool calls this noticeably reduces goal drift. And there is an open project, metasphere-agents, where this is done exactly the way we are discussing: a file per task that moves to an archive on completion.

And now — why the file let us down in our scenario anyway, even though it was set up correctly and from day one. There is a measurement across a large number of trajectories: a plan helps on average. But the authors' verbatim quote is 'bad plans hurt performance more than no plan at all'. A file that has stopped reflecting reality is not neutral — it creates false confidence precisely where vigilance is needed. I'll show the full picture with the figures in a few minutes, on the failure slide — for now it's enough to understand the mechanism."

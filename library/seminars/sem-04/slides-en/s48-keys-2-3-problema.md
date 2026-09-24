---
id: s48
type: problem_scenario
duration_min: 1
assertion: "The task file was set up on day 0 and its plan is checked off for the first steps — but the agreement on how to do the next step, made in the middle of the first session, never made it into the file"
learning_goal: "The problem of case 2.3 — the state of a multi-step task at the entry into the second session. WITHOUT the question, WITHOUT the cards, WITHOUT the conclusion about what was missing: that is assembled after the vote"
visual:
  pattern: problem_scenario
  primary: "Scenario: the \"a file per task\" practice is set up on day 0; the first session closes two steps and, along the way, picks a way to store the wizard's state (sessionStorage, a single key); the session breaks off at context compaction; the second session does step 3 differently, the tests are green, the divergence surfaces during the manual check. At the bottom — a state line: what the second session has at its entry and what it does not. WITHOUT the question, WITHOUT the cards, WITHOUT any statement of the solution."
---

# The second session: the plan is there, the agreement is not

## Assertion

The task file was set up on day 0 and its plan is checked off for the first steps — but the agreement on how to do the next step, made in the middle of the first session, never made it into the file.

## Visual

Scenario:

> The "a file per task" practice is set up on day 0, together with `DECISIONS.md`: every multi-step task gets its own file with a plan and a progress log. The task: split the form into a step-by-step wizard — name, email, confirmation — keeping all the current validation intact. The file is created before the work starts, the plan is laid out in six steps.
>
> The first session closes steps 1-2. In the middle of step 2 it becomes clear that the field values have to be held somewhere between steps, and in the working discussion — not in the plan — a way is chosen: hold the wizard's state as a single object in `sessionStorage` under the key `signup-wizard`, so that reloading the page on the third step does not wipe the fields already filled in. In the plan, step 3 is written down as a single line: "State of the current step (JS)". The chosen approach never makes it into the progress log. The session breaks off in the middle of step 3 — the context is compacted.
>
> The second session. The agent opens the task file: the plan is there, steps 1-2 are checked off as done, step 3 is open. There is not a single line about `sessionStorage` in the file. The agent does step 3 the shortest way — holding the state in a module variable. Switching between steps works, step 5's tests are green. The divergence surfaces at step 6, during the manual check of the full walkthrough: a reload on the third step clears the form — exactly what `sessionStorage` was chosen for in the first session. Step 3 is redone from scratch.

A state line at the bottom, in a gold frame:

> "At the entry into the second session the agent has exactly what is in the file: six steps of a plan and two done marks. The agreement about storing the state stayed in the context of the first session, which no longer exists."

This slide has neither the question nor the option cards — they are on the next slide.

## Speaker notes

"The 'a file per task' practice is already set up on day 0 for us, next to the decision log: any task longer than one session gets its own file — a plan and a progress log. The task here is this: split the form into a step-by-step wizard — name, email, confirmation — keeping all the current validation intact. The file is created before the work starts, the plan is laid out in six steps.

The first session closes the first two steps. In the middle of the second step it becomes clear that the field values have to be held somewhere between steps, and right there in the work — not in the plan — a way is chosen: hold the wizard's state as a single object in sessionStorage, under the key signup-wizard, so that reloading the page on the third step does not wipe the fields already filled in. In the plan the third step is written down as a single line: 'state of the current step'; how exactly to do it is not said there. The chosen approach never makes it into the progress log. The session breaks off in the middle of the third step, the context is compacted.

The second session. The agent opens the file: the plan is there, two steps are checked off as done, the third is open. There is not a single line about sessionStorage in the file. The agent does the third step the shortest way — holds the state in a module variable, saving it nowhere. Switching between steps works, the fifth step's tests are green. The divergence surfaces only at the sixth step, during the manual check of the full walkthrough: a reload on the third step clears the form — exactly what sessionStorage was chosen for in the first session. The third step is redone from scratch, along with everything that had already been built on top of it.

At the entry into the second session the agent has exactly what is in the file: six steps and two marks. Everything else was in the context of the first session, which no longer exists."

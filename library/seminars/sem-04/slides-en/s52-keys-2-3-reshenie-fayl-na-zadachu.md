---
id: s52
type: code_artifact
duration_min: 1
assertion: "What is new in this case is not the file but three lines in CLAUDE.md: they tell the agent when to write into that file"
learning_goal: "The solution for case 2.3 — the \"Task memory\" block in CLAUDE.md (an instruction to the agent, not a reminder to a human) + .tasks/active/signup-wizard.md, in which the rule worked; the honest boundary \"a request, not a law\"; marked illustrative"
visual:
  pattern: code_artifact_illustrative
  primary: "On the left — a block of three lines in CLAUDE.md: a file per task, append an agreement right away, reconcile the plan at the start and at the end of a session. On the right — .tasks/active/signup-wizard.md: the plan, the progress log with the sessionStorage line written down in time, the results, the \"Reconciled\" line. Caption: an illustrative example + the caveat \"a request, not a law\" + the simplification down to a single file (it scales up to a folder)."
---

# Not a new file, but a line in the instructions

## Assertion

What is new in this case is not the file but three lines in `CLAUDE.md`: they tell the agent when to write into that file.

## Visual

On the left — what gets added to `CLAUDE.md`:

```markdown
## Task memory
- Every multi-step task gets a file `.tasks/active/<task>.md`:
  the plan, the progress log, the results.
- An agreement made in the course of the work goes into "Progress log"
  right away, in the same reply, not once the step or the session is over.
- At the start and at the end of a session, reconcile the plan with the
  state of the repository and add the line "Reconciled: <date>".
```

On the right — what this produces in the task file:

```markdown
# Task: split the form into a step-by-step wizard

## Plan
1. [x] Markup for the three steps (name / email / confirmation)
2. [x] Move the current validation over unchanged
3. [ ] State of the current step (JS)
4. [ ] "Back"/"Next" buttons
5. [ ] Tests for switching between steps
6. [ ] Manual check of the full walkthrough

## Progress log
- 2027-01-26: steps 1-2 closed. The wizard's state is held as a single
  object in sessionStorage, key signup-wizard: a reload on step 3 must
  not wipe the fields. Decided along the way, not in the plan.
- 2027-01-28: step 3 started, not finished — context compacted midway.

## Results (filled in on completion)
—

## Reconciled
2027-01-28, start of session: plan reconciled with the repository, no divergences.
```

Caption: "an illustrative example, not a captured artifact · a rule in text is a request, not a law · the simplification down to a single file — it scales up to a folder, more on that beyond this session".

## Speaker notes

"One file per task: the plan, the progress log, the results — it was already there from the first step, that is not the news of this case. The news is this block in CLAUDE.md, three lines. The first describes the file itself. The second says when to write into it: an agreement made in the course of the work goes into the log right away, in the same reply. The third says to reconcile the plan with the repository at the start and at the end of a session; we will come back to it in a minute, when we look at the numbers — that is where it came from.

On the right — what this produces in the task file itself: the agreement about sessionStorage made it into the log before the session broke off. The structure of the file is the same, the practice is the same — the difference is exactly whether it was written down in time or not. And it is the agent that writes it, following an instruction, not you from memory: forcing yourself to remember the log in the middle of the work is precisely the solution that does not work.

The honest boundary, the same as in the case about the readiness gate: these lines are a request in text. The agent reads them and can follow them; they give no guarantee that it appended every time. That is why the third line, about reconciling, stands right next to the first two: one request backs up the other, but neither of them becomes a barrier.

And an explicit caveat about scale: this is a simplified version of the pattern. In real practice it scales up to a folder per task — a separate plan, a separate log, a separate folder for the results, especially when the task is not linear. For today's session one file is enough — we are not complicating it."

---
id: s07
type: assertion_visual
duration_min: 1
assertion: "Besides the spec and the README, three more things go into the repository the same day — not one of them waited for a signal"
learning_goal: "The list of what is set up on the first day (0.5c) — closes the gap of where the artifacts of cases 1.2/2.1/2.3 came from, before they are met by name; placed after the breakdown of the two modes (0.5b) so as not to give away question 0.5"
visual:
  pattern: day_zero_checklist
  primary: "A list of four items (spec.md+README.md, CLAUDE.md with the gate, DECISIONS.md, the file-per-task practice), each with a \"why right away\" line. Under the list — one line about the cost of not having it. No decision points and no case outcomes — only the fact of what is set up."
---

# What is set up on the first day

## Assertion

Besides the spec and the README, three more things go into the repository the same day — not one of them waited for a signal.

## Visual

| What is set up | Why precisely right away |
|---|---|
| `spec.md` + `README.md` | what the result should be and how the repository is put together — in the first commit, before the task goes to the agent |
| `CLAUDE.md` | the instruction file for the agent. On the first day it holds one line: the "done" criterion and the requirement to check the result by hand. There is no description of how the repository is put together in it — there is no reason for one yet |
| `DECISIONS.md` | the project's decision log: what was decided and why. So that a rejected option does not have to be worked through again a month later |
| The file-per-task practice | for a multi-step task — a separate file with the plan and notes on the progress of the work |

A line under the list, in a gold frame:

> "Each of these costs one line today. The cost of not having it cannot be known in advance and is discovered after the fact: the signal that would have made it clear that it is time may never come at all."

Closing line (the transition, with no preview of the outcomes):

> "From here on all four are met by name in the work — each in its own decision point."

## Speaker notes

"Before we go further — what appeared in this repository on the first day, besides the code.

The spec and the README — we have already seen them, they went in with the first commit. The same day sets up `CLAUDE.md`, the instruction file for the agent. For now it holds one line: what counts as 'done' and the requirement to check the result by hand. There is no description of how the repository is put together in it — there is no reason for one yet. `DECISIONS.md` is set up, the decision log: what was decided and why. And the file-per-task practice is set up — for every multi-step piece of work, a separate file with the plan and notes.

Not one of these waited for a signal, and here is why. Each of them costs one line today. And the cost of not having it cannot be known in advance and surfaces after the fact: the signal that would have made it clear that it is time may never come at all — you find out at the moment when it is already too late to go looking.

From here on all four will be met by name in the work, each in its own decision point."

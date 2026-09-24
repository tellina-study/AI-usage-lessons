---
id: s16
type: problem_scenario
duration_min: 1.5
assertion: "The readiness gate has been in CLAUDE.md since day 0 — and twice in a row \"done\" was said before anyone checked by hand that the request had been delivered"
learning_goal: "The problem of case 1.2 — the state of the instruction file and what happened in the first week. NO question, NO cards, NO statement of a solution"
visual:
  pattern: problem_scenario
  primary: "Two blocks: (1) what has been in the file since day 0 — the gate line verbatim; (2) the first week: the client reports that the request never arrived; the test is green, \"done\" has been said, delivery has not been checked by hand — and two days later the same thing on a different bug. At the bottom — a state line with no judgment. NO question and no cards."
---

# The gate in the file since day 0 — and two "done"s with no check

## Assertion

The readiness gate has been sitting in `CLAUDE.md` since day 0 — and twice in a row "done" was said before the delivery of the request was checked by hand.

## Visual

Block 1 — what has been in the file since day 0: "The readiness gate was written into `CLAUDE.md` the same day as `spec.md`: 'Always run the tests and manually verify the result before you say "done"'."

Block 2 — the first week: "The client writes: I submitted a request — it never arrived. The agent reads the code, fixes the handler in `src/main.js`, runs the automated test — green — and reports: 'Done, the test passes.' The test checks exactly one thing: that the form does not submit with empty fields. It knows nothing about delivery.

The developer reminds it about the gate by hand — the agent opens the page manually, finds a second cause, fixes it. Two days later, in a new session, on a different bug — the same thing: automated test green, "done", nobody checked by hand."

The state line at the bottom, in a gold frame:

> "The gate line had been sitting in the file all those days and was loaded at the start of every session. Both times, "done" was said before the manual check."

There is neither a question nor option cards on this slide — they are on the next one.

## Speaker notes

"We write the readiness gate into the instruction file the same day as the spec: always run the tests and verify the result by hand before you say done. The line is cheap, and it has been in the file from the very beginning.

It is the first week. The client writes: I submitted a request from your site — it never arrived. The agent reads the code, finds the problem in the form submit handler, fixes `src/main.js`, runs the test. The test is green. The agent writes: done. And our test checks exactly one thing — that the form does not submit with empty fields. It knows nothing about delivery. You close the task, and the client writes again: it still is not arriving.

You remind the agent about the gate by hand — this time it opens the page manually, finds a second cause, fixes it. Two days later, in a new session, on a different bug — the same thing: automated test green, "done", nobody checked by hand.

The gate line had been sitting in the file all those days and was loaded at the start of every session. Both times, "done" was said before the manual check."

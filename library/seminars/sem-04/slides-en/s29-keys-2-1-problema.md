---
id: s29
type: problem_scenario
duration_min: 0.5
assertion: "End of the first week: a rejected decision about validation resurfaces — DECISIONS.md was set up on day 0, but there is no entry about that decision in it"
learning_goal: "The problem of case 2.1 — the state of the project and the decision point at the entrance. NO question, NO cards, NO statement of the decision: it is assembled after the vote"
visual:
  pattern: problem_scenario
  primary: "Scenario: end of the first week, the agent proposes pulling in a third-party validation library — the very one that was already discussed and rejected. Below — the state of the repository in one line: DECISIONS.md was set up on day 0, there is no entry about that decision in it. NO question, NO cards."
---

# A decision that was already rejected

## Assertion

End of the first week: a rejected decision about validation resurfaces — `DECISIONS.md` was set up on day 0, but there is no entry about that decision in it.

## Visual

Scenario:

> End of the first week of work on `signup-landing`. The client sent in a request with a typo in the email domain, and the form accepted it. The developer asks the agent to tighten the check. The agent reads the code and proposes pulling in a third-party form-validation library — the very one that was discussed and rejected a few days ago: the form has two fields, native `required`/`pattern` and twenty lines of your own code are enough.

Below — the state of the repository, on a separate line, in a gold frame:

> "`DECISIONS.md` was set up on day 0, the same day as `spec.md` and the README. There is no entry about the validation library in it: the decision was voiced in a working discussion and never made it to disk. Between calls the model stores not a single bit — what is not in a file does not exist in the second session."

There is neither a question nor option cards on this slide — they are on the next one.

## Speaker notes

"End of the first week. The client sent in a request with a typo in the email domain — and the form accepted it. You ask the agent to tighten the check. It reads the code and says: let's pull in a form-validation library, here's a suitable one. The very one you discussed and rejected a few days ago — the form has two fields, native `required` and `pattern` are enough.

The state of the repository at this moment: `DECISIONS.md` is there. It was set up on day 0, the same day as the spec and the README — like everything that is cheap and gets set up right away. There is no entry about the validation library in it. The decision was voiced in a working discussion, and between "we discussed this and decided" and "a line appeared in the file" there is a step that does not happen by itself.

And this is not "the agent forgot". The model has no state between calls: every request is processed independently, and what looks like a memory of the discussion is the text history sent in again. When the session ended, what was not written to disk was not forgotten. It is no longer there."

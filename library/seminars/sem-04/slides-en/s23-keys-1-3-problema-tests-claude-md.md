---
id: s23
type: problem_scenario
duration_min: 1.5
assertion: "Over the month two pieces of knowledge of different kinds have piled up — a convention for a whole folder and a detail about a single function — and the developer treats both the same way: he sets up nested instruction files"
learning_goal: "The problem in case 1.3 — the state of the repository a month in and the action the developer took. NO question, NO cards, NO judgment of the action"
visual:
  pattern: problem_scenario
  primary: "On the left — the two pieces of knowledge that piled up over the month, one under the other: the convention for the whole tests/ folder and the detail about a single function in src/main.js. On the right — what the developer did: both went off into nested instruction files, tests/CLAUDE.md and src/CLAUDE.md. At the bottom — a state line: the files sit in subfolders, the bet is on automatic pickup. NO question, NO cards, NO judgment."
---

# A month later: two pieces of knowledge

## Assertion

Over the month two pieces of knowledge of different kinds have piled up — a convention for a whole folder and a detail about a single function — and the developer treats both the same way: he sets up nested instruction files.

## Visual

On the left — what has piled up over the month, and is in neither the root file nor the project description:

> **The `tests/` folder convention** — how check files are named, and that the page is worked with through a page object rather than through selectors directly. Needed every single time someone touches the tests.
>
> **A detail about a single function** — `submitForm()` in `src/main.js` retries the request once on timeout, so the handler on the server has to be idempotent. Needed by whoever edits this function, and by nobody else.

On the right — what the developer did:

```
tests/CLAUDE.md     ← the folder convention
src/CLAUDE.md       ← the detail about the function
```

> "I'll move each one to where it applies — shorter, more relevant to the context, and the root file won't bloat."

A state line at the bottom, in a gold frame:

> "Both files sit in subfolders. The bet is that the agent will read them by itself when it works in those folders."

This slide has neither the question nor the option cards — they are on the next slide.

## Speaker notes

"A month of work on `signup-landing`. Over that time two pieces of knowledge have piled up in the repository that are in neither the root file nor the project description.

The first: in the tests folder an understanding has settled in — how check files are named, and that the page is worked with through a page object rather than through selectors directly. That is a rule for the whole folder: it is needed every single time somebody touches the tests.

The second piece is of a different kind. The form-submit function retries the request once on timeout — which means the handler on the server has to be idempotent, otherwise the application gets submitted twice. This knowledge is needed by exactly the person editing that function, and by nobody else.

The developer treats both the same way: he sets up `tests/CLAUDE.md` and `src/CLAUDE.md`. The bet is that the agent will read the file by itself when it works in that folder. That fixes the state; next comes the question."

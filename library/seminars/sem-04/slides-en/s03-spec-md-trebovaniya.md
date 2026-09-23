---
id: s03
type: code_artifact
duration_min: 1.5
assertion: "The requirements break down into functional and non-functional ones and go into spec.md in the first commit; README describes how the repository is put together and is set up in the same commit"
learning_goal: "A structured record of the requirements — an illustrative spec.md, explicitly marked as not a capture; README as a separate artifact of the product layer"
visual:
  pattern: code_artifact
  primary: "spec.md in full in a terminal_card — functional + non-functional requirements. Beside it / below it — a line about README as a separate artifact: the spec is about requirements on the product, the README is about how the repository is put together. Caption: \"an illustrative example, not a captured artifact\"."
---

# spec.md — the requirements before the first session

## Assertion

The requirements break down into functional and non-functional ones and go into `spec.md` in the first commit; README describes how the repository is put together and is set up in the same commit.

## Visual

```markdown
# spec.md — signup-landing

## Functional requirements
- A static landing page, a sign-up form for a demo lesson
- Fields: name (required), email (required)
- A submit button; no backend — the submission goes to an external form-intake service

## Non-functional requirements
- Acceptance criterion: the form actually delivers the submission — verified in
  prod, not just "the test is green"
- Boundary of action: do not deploy to prod without an explicit request
- Accessibility: the form is operable from the keyboard, the fields have labels
```

Caption under the file: "an illustrative example, not a captured artifact".

Below it — a line about the second artifact of the same commit:

> "`README.md` is set up right away, separately from the spec. The spec is the requirements on the product. The README is how the repository is put together, for whoever walks into it: a human or an agent."

## Speaker notes

"The first ten minutes of work on a project do not go into code. We break the client's wording down into functional requirements — what has to be there — and non-functional ones — what properties it has to have — and put them into `spec.md` in the first commit.

The 'acceptance criterion' line is worth a separate look. The client never said it; we derived it. Without it, 'done' is indistinguishable from 'the test is green', and those are different statements about the system.

The same commit sets up `README.md`. The spec answers the question of what the result should be; the README answers the question of how the repository is put together. The split is a practical one: two different readers, two different lifespans. Requirements change by agreement with the client; how the repository is put together changes as refactorings happen.

The task for the agent is now worded differently: not 'build a landing page with a form' but 'here is `spec.md`, initialize the repository and build the project from it'."

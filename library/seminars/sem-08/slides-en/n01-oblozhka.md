---
id: n01
type: hero_cover
duration_min: 0.5
assertion: "Every new step the chain picks up today is checked against one question: does the model decide this, or should code?"
learning_goal: "Cover slide. Names the session's topic and places it on the same arc rung as S7 — a chain, not a new rung."
visual:
  pattern: hero_cover
  primary: >
    Dark Ocean gradient, a large title, a thin gold bar, a subtitle line.
    No seminar number on screen (owner decision, sem-06/qa/oblozhka-bez-nomera.md).
  backup: >
    Third production wave (issue #274, the owner's extended feedback, 16
    points). The session's topic is verbatim from SETKA-KEYSOV-S8.md: "where
    in the chain the model decides, and where code must." Wave 1 (n01–n16):
    intro, axis, Case "Notifications".
---

# Where the model decides, and where code must

## Assertion

The chain from last time picks up four new steps. Each one gets the same question.

## Visual

> Large-language-model workflows: the second session of the arc.

## Speaker notes

Last session we ended with a working chain: a form, field extraction by the model, a lookup check against a reference list, a row written to the table, a results screen. Today we don't touch a single one of those nodes — we're giving the chain new steps it's about to pick up: a notification to the coordinator, a check for a repeat request, a decision on a refund, delivery of an image.

At each of these steps we'll ask the same question: should the model do this part of the work, or should code? The answer isn't always obvious in advance. Sometimes a model step sits where a simple substitution of already-known values would have been enough — and then the model is just extra weight, with its own cost and risk. And sometimes, the other way around, a text rule inside a prompt probabilistically stands in for what should have been a hard condition in code from the very start — and that doesn't surface right away, but in practice, the one time the rule slips exactly where the cost of a mistake is highest.

The session is practical, but built differently from last time. Last time I assembled the nodes live, in front of you. Today — for each case a ready pair of workflows was built and run ahead of time, with the model and without, and we look at what they actually did on the same requests from the same training center. For one of the cases we go even further and break down a whole experiment: dozens of runs with a measured error count, not a guess at how it should have worked.

We stay on the same rung of the ladder as last time — chain. Today we don't climb higher, we make it more thorough. By the end of the session you'll have, not one new node, but a criterion: how to look at any step of your own chain and decide who belongs there — the model or code.

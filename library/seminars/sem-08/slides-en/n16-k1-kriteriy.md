---
id: n16
type: criteria_checklist_and_boundary
duration_min: 2.0
assertion: "The model is needed when content genuinely varies; a template is enough when the form is fixed and every value is already structured — the first line of the axis is closed"
learning_goal: "Nuances (two classes) + criterion + closing the first axis line, in the same form as Seminars 6/7 (criteria_checklist_and_boundary). A transferable criterion, with no tool name."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A table of two nuances, below it the criterion as its own plate, and a
    line closing the first axis row.
  backup: >
    Text of the nuances and the criterion condensed from
    SETKA-KEYSOV-S8.md, sections "Nuances" and "Criterion." The
    axis-closing line is carried over verbatim rather than reworded.
---

# When you need the model, when a template is enough

## Assertion

An extra model step is a risk, not just a cost. And a template isn't permanently safe either, by itself.

## Visual

| Nuance | What it means |
|---|---|
| **An extra step is a risk, not just a cost** | Every model call is a point where a hallucination can appear — even in a trivial formatting task. |
| **A template isn't permanently safe** | If the message form ever needs genuine variability (different languages, different levels of detail), the template will have to be rewritten by hand for every new case — a different kind of cost, an engineering one. |

> **Criterion.** The model is needed when the content genuinely varies, or when a value requires interpreting text that wasn't interpreted at an earlier step. A template is enough when the message has one form and every value is already structured.

> **The first line of the axis is closed.** The message really did reach the coordinator — and the chain turned out shorter and cheaper without the model node. The LLM here was simply an extra step: the template produced the same result, without its cost or its risk.

## Speaker notes

Two nuances before we lock in the criterion, and both are about how neither version is permanently safe on its own.

The first nuance — an extra model step is a risk, not just an extra cost. It's easy to think that because the task is trivial — just assembling already-known words into one phrase — there's nothing to worry about. But we just saw: even on a trivial formatting task, calling the model stays a point where a hallucination can appear — that is, a detail that wasn't on the input. The cost in money and time isn't even the main thing here — the main thing is that what ends up in the text is, in principle, unpredictable.

The second nuance is exactly about the template, and it's there for balance. A template isn't permanently safe just because it's deterministic. If at some point the message form needs genuine variability — say, notifications have to be written in several languages, or with different levels of detail for different recipients — a static expression won't notice that on its own, and it'll have to be rewritten by hand for every new case. That's a different kind of cost, an engineering one, not a hallucination risk, but real all the same.

That gives us a criterion you can take with you and apply to any chain of your own, without remembering a single node name. The model is needed when the content genuinely needs variability, or when a value requires interpreting request text that wasn't interpreted at an earlier step. A template is enough when the message has one form and every needed value is already lying there structured.

And back to the session's axis. The first line: the message really did reach the coordinator, and that observation was true from the start. What it turned out to be: the chain came out shorter and cheaper without the model node at all — the same result, without its cost and without its risk.

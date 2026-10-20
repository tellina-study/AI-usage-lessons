---
id: n19
type: question_with_option_cards
duration_min: 2.5
assertion: "How to build a duplicate check — five actions, and all five show up in live systems"
learning_goal: "Question with no hints (A12): the cards are actions, not facts about a tool's capabilities (canon §5). The room designs the check's order on a real pair of phrasings, not guessing a pre-marked answer. The fifth card (a specialized service) was added per the 2026-10-20 voice edit — jev is now a full choice option, not just a row in the final measurement table (n20)."
visual:
  pattern: question_with_option_cards
  primary: >
    A pair of texts in an inset, the question in a gold frame, and a row of
    five action cards with no explanations.
  backup: >
    The first four cards are from SETKA-KEYSOV-S8.md, Case 2, section
    "Question to the Room", wording almost unchanged (the second card already
    names the classic vector approach explicitly, not "word comparison" — the
    deck's wording was already right here). The fifth card is new, added per
    the 2026-10-20 voice edit (issue #274): a specialized external service
    (jev) as a standalone option for the expensive step, alongside the
    general-purpose model, not only a row in the final measurement table.
    All five are actions (canon §5): "compare", "ask", "check" — verbs, not
    claims about a tool's properties. The pair of questions in the inset is
    known in the measurement methodology (n20 backup) as "Boris's pair" —
    fine here and in the notes, not named on the visible layer.
---

# How to Build a Duplicate Check

## Assertion

"When can I pay for the class?" and "how do I pay for the course" — one question, two phrasings, two hours apart. How do you build a step that tells a repeat apart from a new request?

## Visual

> **How do you build a duplicate check?**

`compare the texts literally — exact match after normalization` · `compare the texts by shared words — the classic vector approach with a threshold` · `ask a general-purpose model whether it's the same question, just phrased differently` · `ask a specialized question-comparison service instead of a general-purpose model` · `check exact match cheaply first, and only pass through what's left`

## Speaker notes

Here's the very pair exact match stumbled on: "how do I pay for the course" — a question asked two hours after "when can I pay for the class?". By meaning, it's the same question. Letter for letter, two different texts.

The question: how do you build a duplicate check.

Five cards, and this isn't theory — five real approaches that show up in live systems. Compare the texts literally — exact match after normalization, which we already saw on the previous screen. Compare the texts by shared words — the classic vector approach with a threshold, no trained model, but more serious than plain string comparison. Ask a general-purpose model whether it's the same question, just phrased differently. Ask a specialized service tuned specifically for comparing questions, rather than a model that can do practically anything. Or check exact match cheaply first, and only pass through what's left unresolved.

Notice the wording: all five describe an action you can take and implement, not a claim about what some tool can or can't do on its own. "Compare literally" is an action. "Ask the model" and "ask the specialized service" are also actions, not a ready-made conclusion like "the specialized service is more accurate than a general-purpose model". The difference matters: the question isn't which tool is smarter in principle, but which step you'd put first and which second in a chain that processes an entire training center's requests.

Four of the five cards are standalone solutions you can take and implement whole: literal comparison, word-based comparison, calling a general-purpose model, or calling a specialized service. The fifth isn't another separate tool but a way to combine the ones already named: cheap first, and the expensive one only on what the cheap step didn't resolve. If votes split between the first four options and the fifth, that's fine: the first four answer "what to compare with", the fifth answers "in what order".

Choose. There's more than one right answer here — all five are real engineering solutions. We'll break down what each one actually catches on our pair, what it doesn't, and what it costs.

Fifteen seconds, then we lock it in.

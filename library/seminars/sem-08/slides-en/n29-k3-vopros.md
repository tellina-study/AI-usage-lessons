---
id: n29
type: question_with_option_cards
duration_min: 2.0
assertion: "The rule has run for a month without a single complaint — the question is how to make sure the threshold decision is really never wrong"
learning_goal: "The question for Case 3: four action cards (down from five), each phrased as an imperative action rather than a claim about the model."
visual:
  pattern: question_with_option_cards
  primary: >
    A short reminder of the scene at the top. Below it, the question in a
    gold frame and a row of four equal-width cards. No arguments or hints
    next to the cards — the breakdown comes on a later screen.
  backup: >
    The "run it several times and take a majority vote" card was removed:
    the measured experiment (n31–n32) shows this option isn't merely
    limited, it is useless against the specific error found — a systematic
    one at the exact boundary, which majority voting cannot fix, since it
    only defends against random noise. The remaining four cards describe
    actions on the process, not facts about the model. Mirrors RU n29 after
    this round's edits (issue #274).
---

# How to make sure the threshold decision never errs

## Assertion

A month without complaints is a fact about silence, not about every decision being correct. Before trusting the rule any further, it's worth asking: how do you make sure it really never gets this wrong?

## Visual

> **How do you make sure the threshold decision is never made incorrectly?**

`write the rule more clearly in the prompt` · `give the model a calculator tool for comparing amounts` · `put an IF node after the amount is extracted` · `make the amount an explicit numeric field on the form`

## Speaker notes

Let's pause here for a second before moving on. The rule has run for a month, no complaints — and this is exactly the point where an engineer has to ask: is silence proof, or simply the absence of a reason to check?

The question worth asking: how do you make sure the threshold decision is genuinely never made incorrectly? Not "how to make things more reliable" in general, but specifically about this one point — comparing the amount with the threshold.

Four cards, and they are four different actions on the process, not four opinions about the model.

The first — write the rule more clearly in the prompt itself: rephrase the text to explicitly separate what happens exactly at the boundary from what happens on either side of it.

The second — give the model a calculator tool: let it not do the comparison in its head, but call a separate function to compare the numbers.

The third — put an `IF` node after the amount is extracted: let the model still pull out the amount, but let code do the comparison against the threshold.

The fourth — make the amount an explicit numeric field on the form: don't write it inside the free-text request, collect it as digits right at intake, in its own field.

As in the earlier cases: there is no single obviously wrong option here among the rest. All four are real engineering moves, and some of them carry a real limitation that doesn't show up right away. Think not about "what sounds more reliable," but about what removes the very possibility of the mistake, rather than just lowering how often it happens.

And one more hint for later — not about which card is correct, but about how to approach them. Two actions change SOMETHING about how the model makes the decision — a rewording, a tool. Two actions change WHERE the decision is made at all — moving it into code, or removing the need to extract anything in the first place. The difference between "do the same thing better" and "do it differently" will carry the whole breakdown that follows.

Fifteen seconds to choose, then we vote by raising hands — the breakdown is on the next screen.

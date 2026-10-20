---
id: n30
type: answer_breakdown_table
duration_min: 2.5
assertion: "Two actions reduce the error rate or shift the probabilistic part one step earlier (and are now actually measured — one well, one badly); two eliminate it structurally or don't need an accuracy measurement at all"
learning_goal: "The breakdown of all FOUR actions (down from five) right after the question, in a four-column form — Action · How it works · Advantage · Drawbacks. Every row carries a real live-rig measurement except the numeric-field row, where a different metric (applicability, not accuracy) applies instead."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: Action · How it works · Advantage · Drawbacks, four rows. Below
    it, a short bridge to the next beat: before choosing among the actions
    that eliminate the problem structurally, it's necessary to measure
    exactly how bad version 1 currently is.
  backup: >
    Each of the four cards carries a real measured result from the live rig
    except the numeric-field action (a different metric applies there).
    "Clearer rule": 100/100 on the extended hundred-request set, including
    all the boundary and ambiguous cases where version 1 scored 9 errors out
    of 101. "Calculator": 56/100 — worse than every other option, with
    detailed, real failure modes. "IF node" = version 2, measured this round
    on the extended set: 0 errors out of 101. "Explicit numeric field" — not
    measured as accuracy, and that's not a gap: this option has no
    extraction step at all, so "extraction accuracy" is trivial here (100%
    by construction). A separate honest finding this round, not among the
    four cards: the jev service, checked as an idea for amount extraction
    and rejected — see n30a. Mirrors RU n30 (issue #274).
---

# What each of the four actions delivers

## Assertion

No action is pointless, and now every one of them has a real measurement behind it, not just reasoning.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| **Write the rule more clearly in the prompt** | Reword the rule, explicitly separating "≤3,000 → approve" from ">3,000 → escalate" | Measured: version 1 erred 9/101 at the boundary; the clarified wording — **100/100** on the extended set | A fact about this specific set/model, not a structural guarantee — the decision is still made by text, not code; another wording or model could diverge again |
| **Give the model a calculator tool** | The model gets a number-comparison function instead of comparing "in its head," and decides itself whether to call it | In theory splits extraction and comparison into two operations | The model still extracts the amount from text first — the same probabilistic step — then probabilistically decides whether to call the tool: the probabilistic part doesn't disappear, it moves earlier. Measured: **56/100** — worst of all options; the calculator can't do comparisons (11/100 refusals), 30/100 answers don't reduce to a clean word, 9/100 errors scattered across the range |
| **Put an `IF` node after the amount is extracted** | The model still pulls out the amount, code compares it with the threshold — a condition, not a text call | Removes the probabilistic part from the decision point. Measured: **0/101** on the extended set, including boundary cases | The model still extracts the amount — an extraction error (not a comparison error) isn't closed by this node, though none turned up on this set |
| **Make the amount an explicit numeric field on the form** | Collect the amount as digits in a form field — never extract it from text at all | Removes the uncertainty earlier: there's nothing to extract, so there's no extraction-error risk | Works only if the form can be changed; an email/chat/other channel still requires extraction from text. The metric is applicability, not accuracy — there's no extraction step, so there's no accuracy to measure either |

> **Bridge ahead.** One action measurably fixed the specific finding, one measurably failed, one eliminates the risk structurally and is confirmed by measurement, one changes the input before the decision point and needs no accuracy metric at all. Which one is right here isn't decided by argument at the table — it's decided by the measurement you're already seeing in this table; the next beat shows how it was built.

## Speaker notes

Let's go through the four actions, and each one now has not just reasoning behind it, but a real run on the live rig.

Write the rule more clearly — explicitly separate what happens on either side of the boundary. We ran it on the extended set of a hundred requests, the same ones where version one erred nine times out of a hundred and one — zero errors. This is a measured fact, but not a structural guarantee: the decision is still made by text comprehension, not code, and another wording or another model could diverge from the rule again, just somewhere else.

Give the model a calculator tool — this one needs a more detailed explanation of why it doesn't solve the problem. Before the calculator can compare anything, the model still has to extract the amount from the text — the same probabilistic step as without the calculator. And after that, the model itself, also probabilistically, decides whether to call the tool and with which arguments. The calculator doesn't remove the probabilistic part — it adds another one where there wasn't one before. We assembled a real agent with a real calculator and ran it on the same hundred requests: fifty-six out of a hundred, the worst of all the options. n8n's built-in calculator can do arithmetic but not comparisons, and on "2,500 is less than 3,000" it honestly answered "I don't know how to do this" (11 out of 100). A third of the answers didn't reduce to a clean word — mixed alphabets, reasoning instead of an answer, one switch into Chinese. Almost a tenth of the errors were scattered across the whole range, not just at the boundary.

Put an `IF` node after extraction — the model still pulls out the amount, code does the comparison. On a hundred and one requests — zero errors, including every boundary case built into the set. What it fundamentally doesn't close is an extraction error itself; none turned up on this measurement, but architecturally that's not this node's job.

And last — an explicit numeric field on the form. Accuracy was deliberately not measured here: a step that doesn't exist has no accuracy to measure. The applicable metric is applicability: it works only if the form can be changed; otherwise extraction from text is still unavoidable.

Before choosing among the actions, we need to know exactly how bad things currently are, and exactly where version 1 goes wrong on the extended set. That measurement is the next beat.

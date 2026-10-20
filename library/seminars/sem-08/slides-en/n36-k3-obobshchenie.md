---
id: n36
type: answer_breakdown_table
duration_min: 1.5
assertion: "The model systematically misses exactly at the boundary of a condition, rather than erring probabilistically in general; the class of task — a decision formalizable as a condition over a number — is not a decision point for the model"
learning_goal: "The generalization of Case 3 — the precise wording of the task class, kept exact rather than smoothed into a generic 'the AI sometimes makes mistakes.'"
visual:
  pattern: answer_breakdown_table
  primary: >
    A short generalization banner at the top, below it the task class
    stated in one large phrase, highlighted in gold.
  backup: >
    The wording "the model systematically misses exactly at the boundary of
    the condition... flawless over the rest of the range" is kept exact —
    this is the safeguard against drifting into the generic "the model
    sometimes makes mistakes," which the course's AI-failure rule treats as
    not counting at all. Mirrors RU n36 (issue #274).
---

# Where the decision must be code

## Assertion

Where a decision can be expressed as a deterministic condition over an already-structured value, the decision must be made by code.

## Visual

> **The precise wording of the finding.** Not "the model sometimes errs probabilistically" — more precisely: **the model systematically misses exactly at the boundary of the condition**, where the rule's text and its formal interpretation diverge, while being flawless everywhere else in the range.

> **The class of task.** A decision formalizable as a condition over a number is **not a decision point for the model**. Boundary values are the first thing to check with a real run, before trusting any similar threshold rule.

## Speaker notes

Now the generalization — what should stay with you after the numbers of this particular case are forgotten.

The first thing worth dwelling on: the wording of the finding matters exactly, not approximately. It is wrong to say "the model sometimes errs probabilistically" — that's too vague and says nothing about where to look for the problem next time. The precise wording is different: the model systematically misses exactly at the boundary of the condition — where the rule's text and its formal interpretation diverge — while behaving flawlessly across the rest of the range. The difference between "sometimes errs" and "systematically misses at the boundary" is the difference between "you need more checks everywhere" and "you need to check exactly one point."

From this follows the class of task worth taking away. If a decision can be expressed as a condition over an already-structured value — a number greater or smaller than another number, a date earlier or later than another date, a status on a list or not — that decision is not a job for the model at the decision point. The model can stay necessary earlier in the chain, where free text still has to be parsed and a value pulled out of it. But the moment of comparison itself is code, and only code.

And the practical conclusion that works well beyond refunds: boundary values are the first thing to test with a real run, before trusting any similar rule built on a threshold. Not the middle of the range, where things are usually fine, but specifically the boundary — where the rule's wording and its interpretation diverge most often.

This is the same lesson that already came up in the notifications case and in the repeat-request case, only here it's stated more precisely thanks to measurement: not "test the model on edge cases in general," but specifically — at the point where a human phrasing of a rule and a literal condition can fail to match. Every threshold anyone has ever written in words has a point like this.

And one more detail that the measurement added to this generalization. A clearer rewording of the rule — one of the four actions reviewed — in practice removed this exact error entirely: a hundred out of a hundred on the extended set. This doesn't contradict the conclusion "the decision must be code" — it refines it. The improved wording is a measured improvement of a SPECIFIC prompt on a SPECIFIC set, not a structural guarantee: nothing in the architecture rules out that another phrasing, another model, or a future update to it will diverge from the rule again, just somewhere else. The `IF` node eliminates the whole category of this error: a number-to-number comparison in code doesn't need to be re-verified every time the wording or the model changes.

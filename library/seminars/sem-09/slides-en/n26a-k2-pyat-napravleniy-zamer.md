---
id: n26a
type: measured_outcome_table
duration_min: 1.5
assertion: "Five directions of prompt structuring were checked with 84 calls on questions that already confused the model back in Case 1 -- before looking at the outcome, here's what was tested and on what"
learning_goal: "Beat S2-1 for the case's second measurement (structure, no results, K2-16/K2-17/K2-18, review 2026-10-29). Owner edit 2026-10-27, a measurement of our own across five directions of prompt structuring. Rebuilt from the earlier edit, which showed structure and result on one frame -- a violation of S2."
visual:
  pattern: measured_outcome_table
  primary: >
    A five-row table of directions: what was compared · how many questions
    · a format/position example for each direction. No results on the
    frame at all -- no share of correct answers, no word "better".
  backup: >
    REBUILT (K2-16, K2-17, K2-18, review 2026-10-29). The earlier edit of
    this frame carried five rows, "direction · what was compared ·
    result", on one screen -- structure and outcome mixed together, a
    violation of S2 ("missing a description: how many questions, which
    blocks"; "each block, with examples, no result on this frame";
    "first the test structure -> a round-up table -> each block in
    detail"). The result column was dropped ENTIRELY from this frame and
    moved to n26b.

    The numbers are from `stend/zamery-k2/README.md`, measured 2026-10-27,
    executions 856-939, 84 calls, scenario `s9-k2-experiment`. The
    questions are a subset of Case 1's hard questions
    (`voprosy_zamer1.py`), for direct comparability: this is the same task
    the model already got confused on in the "Answer or Stay Silent"
    breakdown, and the five directions check whether restructuring the
    prompt fixes it -- not a fresh task from scratch.

    Model and settings (C5) -- the same for all 84 calls, the same node
    and the same model as the session's own rig (`qwen/qwen-2.5-7b-
    instruct` via n8n, a universal node, the prompt assembled entirely
    from code); this is named explicitly, unlike the earlier edit, where
    the model didn't appear on the structure frame at all.

    The samples are small (5-15 per direction) -- the frame names this
    directly, in the "questions" column, not hidden (C9 doesn't forbid
    naming the sample size -- it forbids a self-deprecating caveat on top
    of an already-named number, not the fact of a small sample itself).
---

# Measurement Structure: Five Directions of Prompt Structuring

## Assertion

Five directions, 84 calls, one model -- and the same questions that already confused the model in the last breakdown. No result on this frame yet.

## Visual

> **Model and call.** `qwen/qwen-2.5-7b-instruct`, one universal node, the prompt assembled entirely from code -- unchanged between directions, except for whatever the specific direction is testing.

| Direction | What was compared | Questions | Example |
|---|---|---|---|
| Knowledge-base format | an unformatted list · markdown headers · a detailed description of each item | 5 per format (15 total) | "refund -- 10 business days" vs. "## Refund\n10 business days" vs. "A refund is processed within 10 business days of the request" |
| Position of the needed item | start of the list · middle · end | 5 per position (15 total) | the same item on refunds is moved through ten positions in the list |
| Rule wording | ordinary prose · a strict conditional form | 12 per form (24 total) | prose: "amounts over 3,000 rubles go through a manager" vs. conditional: "IF amount > 3,000 rubles -> manager decides, ELSE -- no" |
| Repeating the client's question | no repeat · the question inserted both before and after the knowledge-base list | 5 per option (10 total) | the question "how many days for a refund" inserted before the knowledge base and repeated after it |
| Stability of the prompt's start | the start is identical call to call · the start is shuffled on every call | 10+10 calls | the same instruction-plus-knowledge-base text -- either in one fixed order always, or with items shuffled on every call |

## Speaker notes

We built a universal rig -- one node, the prompt comes entirely from code -- and ran five directions that keep coming up whenever people talk about prompt structure: knowledge-base format, position of the needed item, rule wording, repeating the question, stability of the prompt's start. Eighty-four calls on the same model, at least five per direction.

An important decision in this measurement: the questions weren't invented fresh. We took a subset of hard questions from the last breakdown, "Answer or Stay Silent" -- the very ones the model already got confused on. The idea is simple: if structuring the prompt helps, it should help exactly where the problem is already visible, not on a new, convenient task.

Each direction gets a concrete comparison. Knowledge-base format: a bare list against markdown headers against a detailed description of each item. Position: the same item about a refund moved through ten spots in the list, from first to last. Rule wording is where it gets more interesting: we take the rule about the 3,000-ruble threshold and rewrite it as an explicit conditional formula, "if the amount is more -- then, else -- no", against ordinary prose. Repeating the question: we insert the client's question text both before the knowledge base and after it, against mentioning it once. And stability of the start is a technical question about caching: we either keep the start of the prompt identical, or shuffle the order of the items before every call.

Each direction has a small sample -- from five to fifteen questions, and that's a fact about the measurement, not a caveat: the decision still shows the direction of the effect; you can't measure its size on a sample like this.

Why five directions at once, instead of one after another. Because in practice a prompt rarely gets changed with one single knob: someone fixes the format, someone moves an item, someone spells out a rule in more detail -- and each of these moves looks like a reasonable improvement on its own. If you check them one at a time, it's easy to conclude "this particular technique works" on a sample that just never ran into the real difficulty. So all five directions were run on the same hard questions, with the same model, to keep the comparison honest, not convenient.

What got confirmed and what didn't -- next screen, the round-up and the breakdown by direction.

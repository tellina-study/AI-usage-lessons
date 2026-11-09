---
id: n16
type: measured_outcome_table
duration_min: 1.5
assertion: "The check removed the confident lie and brought two new outcomes: 4 of 15 answers passed it with wrong content, 2 of 15 aborted before any answer at all"
learning_goal: "The second half of the case's turn: the decision became checkable, and that has a named cost. Numbers — both sides at once, the win and the price, with no 'version 2 is better' verdict."
visual:
  pattern: measured_outcome_table
  primary: >
    A comparison table of both versions on the same fifteen questions — a
    row for "good outcome," a row for "confident wrong answer," a row for
    "passed the check with wrong content," a row for "aborted before an
    answer." Below the table, one breakdown with a verbatim quote and a
    tile on the failure class free text doesn't have.
  backup: >
    Numbers — from `stend/zamery-k1-k3/README.md`, Measurement 1, summary
    table: good outcome 9 of 15 for both versions; confident wrong answer
    — 6 of 15 for version 1, and doesn't happen for version 2 by design;
    passed the check with wrong content — 4 of 15 (questions Q6, Q9, Q12,
    Q15); aborted before the check — 2 of 15 (Q8, Q10, the output didn't
    fit the required schema, execution ended in an error before the check
    node). Runs 620-648 (even-numbered).

    The breakdown is Finding B of the protocol, question Q12, about
    transferring to a cheaper course: the correct item is about
    transferring to another course, where it says only "recalculated by
    the administrator individually"; the model referenced the item about
    refunds — a real item, but the wrong one, and the condition didn't
    catch it, because the item's name is real.

    The numbers 4 of 15 and 2 of 15 are kept apart by their captions
    ("passed the check" versus "didn't reach the check") — the rule
    against two similar numbers in one sentence (BRIEF §2).

    Run numbers don't appear on the visible layer.

    No "version 2 is better" verdict on the slide, deliberately: both
    costs are named, the criterion comes in beat n17.

    THE MODEL IS NAMED ON THE RESULT TOO (C5, 2026-10-29 edit), not only
    on the build (n10, n11, n13a, n14, n15): `qwen/qwen-2.5-7b-instruct`,
    the same for both versions, with no explicitly set options.
---

# The same fifteen questions through the check

## Assertion

The confident lie disappeared: the decision no longer lives in the text. In its place, two outcomes appeared that free text never has.

## Visual

> Both versions — the same model, `qwen/qwen-2.5-7b-instruct`, with no explicitly set call options. Only what happens to its answer afterward differs.

| On the same 15 hard questions | Version 1 | Version 2 |
|---|---|---|
| **Good outcome** — a correct answer or an honest hand-off to a human | 9 of 15 | 9 of 15 |
| **Confident wrong answer that would have reached the client** | 6 of 15 | doesn't fail this way: the decision sits in a field code reads |
| **Passed the check, but the answer's content is wrong** | this outcome doesn't exist: there's no check | 4 of 15 |
| **Never reached the check — the client got nothing at all** | this outcome doesn't exist: text is always written | 2 of 15 |

> **What "passed the check with wrong content" looks like.** Question: "If I transfer to a cheaper course, do I get the price difference back?" The right item is about transferring to another course, and it says only that the administrator recalculates the cost individually. The model referenced the item about refunds. The item exists, the name is real, the condition let it through — the answer would have gone to the client looking justified.

> **An outcome free text never has.** Twice out of fifteen, the model's output didn't fit the required schema, and execution aborted with an error before reaching the check node. The requester got no answer and no message that their question had been handed to a human. Free text fails softly — it writes something, at least; strict output breaks completely.

## Speaker notes

The same fifteen hard questions, the same rig, version 2. Let's compare row by row.

Good outcome — a correct answer or an honest hand-off to a human — nine of fifteen. The same as version 1. Worth saying plainly: by the share of normal outcomes, version 2 gained nothing.

The second row — the one this was all built for. A confident wrong answer that would have gone to the client: six of fifteen for version 1, zero for version 2. The model didn't get any smarter — the decision just no longer lives in the composed text. It's in a separate field, and it's read by the condition we just read with our own eyes.

Then two rows that didn't exist at all in version 1, because version 1 had neither a check nor a strict format.

Four of fifteen answers passed the check — and their content is wrong. Let's break one down. Question: transferring to a cheaper course, will the price difference be refunded. The right knowledge-base item is about transferring to another course, and it says exactly one thing: the administrator recalculates the cost individually, nothing about refunding a difference. The model referenced a different item — about refunds. The item exists, the name is real, it's on the list. The condition looked at the name, found it on the list of ten, and let it through. The answer would have reached the client looking justified.

Think back to that line on the panel. It asked: does the named item exist. It did not ask: is this the right item. This is what that difference turns into — four requests out of fifteen.

And the last row, which we never planned to measure — it surfaced on its own. Twice out of fifteen, the model's output didn't fit the required schema, execution aborted with an error before reaching the check node, and the requester got nothing at all: no answer, no message that the question had been handed to staff. This is a new failure class. Free text degrades softly — it writes something, even if wrong. Strict output breaks outright: either it fits the schema, or the channel aborts.

We got checkability of the decision. And it isn't free — the cost is named in both of those rows.

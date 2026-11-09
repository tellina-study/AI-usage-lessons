---
id: n48
type: measured_outcome_table
duration_min: 1.0
assertion: "Semantic search wins recall@1, the merge wins recall@3 and average rank — no single method wins on every metric at once"
learning_goal: "Case 3's summary beat (C2, canon forma-keysa-s-zamerom.md §1): the aggregate across three methods. Part 1 of 2 (n49 — the breakdown by question group and the systematic finding): split because 15pt half-size type leaves no room for two tables and three tiles on one slide (issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    A gold headline-number tile · a 3×3 table (method · recall@1 ·
    recall@3 · average rank).
  backup: >
    Aggregate — SETKA-KEYSOV.md Case 3 / stend/raw/case3-results.json.
---

# What the run on 500 documents and 50 questions showed

## Assertion

Semantic search wins recall@1, the merge wins recall@3 and average rank: no single method wins on every metric at once.

## Visual

> **Best result for first place: semantic search finds the correct document right in first place in 43 of 50 questions (86%).**

| Method | recall@1 | recall@3 | average rank of correct (out of 500) |
|---|---|---|---|
| Search by words | 0.74 | 0.80 | 9.9 |
| Search by meaning (vector) | 0.86 | 0.92 | 2.0 |
| Search both, merge (hybrid, RRF) | 0.84 | 0.94 | 1.6 |

## Speaker notes

Fifty questions were run through three methods with no model call at all at the ranking step — search by words, search by meaning, and their merge. Let's start with the summary; the breakdown by each action comes in the next beat.

By recall@1 — whether the correct document lands right in first place — the best result belongs to semantic search: forty-three questions out of fifty, eighty-six percent. Search by words is the worst: thirty-seven out of fifty, seventy-four percent, and if the document isn't in first place, it sits on average at the ninth-to-tenth position out of five hundred — the specially selected lexical gap and the confusable clusters throw off exact word matching noticeably. The merge of two signals can't be called an unconditional winner: it has the best recall@3 (ninety-four percent) and the best average rank (1.6) of all three, but its recall@1 is lower than pure vector's — eighty-four percent against eighty-six.

At first glance the conclusion seems to write itself: since semantic search wins on the headline metric, it must be the best choice, and the merge is just a more complicated version of the same thing with a smaller effect. But this intuition is worth checking honestly — against how each method behaves on different types of questions. Looking only at the aggregate as a whole isn't enough here: an averaged number across fifty questions can hide several different pictures behind it at once.

The average rank also deserves a separate look: 9.9 for search by words against 2.0 for search by meaning isn't just "worse" — it's the difference between "the document is almost at the top" and "the document is somewhere in the first third of the results," when it isn't in first place at all. For the requester, this feels like the difference between an instant answer and an answer the system had to sift through a noticeable part of the base to produce.

This aggregate hides something important: a breakdown by question type — next.

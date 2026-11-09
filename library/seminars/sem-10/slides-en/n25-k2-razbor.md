---
id: n25
type: answer_breakdown_table
duration_min: 0.6
assertion: "Two fundamentally different ways to cut a document without overlap: by character count and by sentence boundaries"
learning_goal: "Qualitative breakdown of actions 1-2 of Case 2 right after the question (course owner's requirement: the breakdown follows the question directly — n24 → n25 → then the test structure and the result). The breakdown explains the mechanism and the qualitative pros/cons without a single result number, following the pattern of n62-k4-razbor.md; canon C2 is not violated — up to the test-structure beat there is no result on the frame at all. Action names repeat the n24 cards verbatim. Part 1 of 2 (n26 — actions 3-4: cheap patches on top of the first). Regrouped 2026-11-04 per the owner's note: it used to be 3+1 rows (visually read as '3 analyzed, the fourth tacked on'), now it's 2+2 — two fundamentally different ways kept apart from two patches on the first one, equal visual weight with n26 (issue #311)."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · advantage · drawbacks. Two rows — the
    two fundamentally different ways to cut without overlap (by character
    count, by sentence boundaries). No numbers on the frame.
  backup: >
    Text — the number-free version of n33-k2-razbor.md (the "How it
    works" column and the qualitative part of "Advantage"/"Drawbacks");
    every numeric value (shares of broken answers in percent) from the
    original table has been removed, leaving only the mechanism and the
    qualitative judgment.
---

# Two fundamentally different ways: by characters and by sentences

## Assertion

Two methods cut a document without overlap: by character count — blindly, by sentence boundaries — along a boundary of meaning. Which one breaks answers more often — next.

## Visual

| Action | How it works | Advantage | Drawbacks |
|---|---|---|---|
| Cut strictly by character count, without regard for the text | The document is chopped into pieces of a set length with no regard for the text inside | Simplest to implement — one parameter, one mechanical pass through the text | The cut can land exactly in the middle of the phrase holding the answer, regardless of the chosen chunk size; there's no way to tell in advance which size is "more convenient" without checking |
| Cut by sentence boundaries | The cut falls only where one sentence ends and the next begins | Chunks don't tear a phrase in half: the cut follows a boundary of meaning in the text — character count plays no role here | A bit more involved to implement: it needs a separate step that understands where a sentence ends in the given language — plain character counting isn't enough here; the quality of this step depends on the text |

## Speaker notes

Four actions, and all of them are real engineering choices — this beat explains how two fundamentally different ways of cutting without overlap actually work: both solve the same task, but start from a different cutting logic. Which one is better by the numbers, we'll see next.

Cutting strictly by character count, without looking at the text, is the simplest and cheapest to implement: one parameter setting the chunk's length, one mechanical pass through the text. The price for this simplicity is that the cut doesn't know where a thought ends in the text, and can land exactly in the middle of the phrase holding the answer to a future question, regardless of which chunk size was chosen. And without checking, you can't tell in advance which size is more convenient here: by eye, any option looks reasonable, because the chunk itself reads fine at any size.

Cutting by sentence boundaries is a bit more involved: a separate step is needed that first understands where one sentence ends and the next begins, and only then makes the cut. This is a dependency the first action doesn't carry at all — the quality of sentence splitting depends on the specific language and text. But the payoff comes back in the form of the cut holding to a boundary of meaning in the text — character count has nothing to do with it here — and so chunks less often tear a phrase in half. Two actions, two different trade-offs: one pays with accuracy for simplicity, the other pays with simplicity for accuracy.

A torn phrase flows downstream into a concrete failure. If the cut landed in the middle of the phrase with the answer, search afterward honestly finds the right chunk — and that chunk holds half the answer. The model gets a fragment and answers from the fragment: search formally worked, but the answer is incomplete. The third and fourth actions try to handle this differently, while staying within the same character-count-cutting principle — next frame.

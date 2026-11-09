---
id: n29
type: measured_outcome_table
duration_min: 1.0
assertion: "On the honest measurement of the final answer, version 2 answers correctly in 72% of cases at K=1 against 57% for version 1 — the gap holds even when the model gets several chunks, not one"
learning_goal: "Follow-up pass 2026-11-04 (issue #311), a direct instruction from the owner: 'for the chunking case we're missing measurements on the answers... we need a measurement of the final outcome.' Moved the same day to right after n28 (the owner's second note from the same round: 'this should be earlier, next to the measurements on question fragments' — the beat used to sit at the end of Case 2, after the solution architecture and the closing nuances, even though it logically continues the first direct measurement, not the solution breakdown). The previous beat (n28) measured a proxy — is the gold span intact inside ONE chunk; this beat measures the outcome of the full pipeline: question embedding → top-K search across ALL 60 documents → `gpt-4o-mini` answers from the retrieved chunks → checked by the same `contains_answer` criterion as Case 1 (not a new metric with a different threshold). Added an explicit statement of the measurement's basis (the round's third note: 'it's not clear, if we cut differently, how was this measured, on what' — the frame now states plainly that all four versions were run on the same base as the previous beat). Part 1 of 2 (n30 — the gap narrows but doesn't close): split because the 15pt floor size doesn't leave room for two definition tiles, a 5×4 table, and the conclusion about the narrowing gap on one frame."
visual:
  pattern: measured_outcome_table
  primary: >
    A "what we're measuring and what K means" tile, a headline-comparison
    tile at K=1, a 5×4 table (cutting version · K=1 · K=2 · K=3 · K=5,
    accuracy_strict).
  backup: >
    Numbers — stend/raw/case2_e2e_results.json::summary (1152 calls to
    gpt-4o-mini, 4 versions × 4 K × 72 questions), interpretation —
    stend/README.md "Case 2, follow-up pass 2026-11-04". Correctness
    criterion — `harness2.contains_answer`, the same function Case 1
    already uses (`accuracy_strict`, not a new metric). Fractions out of
    72 — the product of accuracy_strict × 72, a whole number with no
    remainder in each of the 16 cells (verified by direct count, not
    rounded by eye).
---

# What the measurement of the final answer showed

## Assertion

Version 2 answers correctly more often than version 1 at every one of the four tested K: this is the model's final answer, measured directly, without the chunk-break proxy.

## Visual

> **What we're measuring, and on what.** The outcome of the entire pipeline: top-K search among the same 60 documents and 72 questions as in the previous beat, then `gpt-4o-mini` answers from the retrieved chunks — scored by the same criterion as Case 1. The previous beat measured something different: span integrity inside one chunk. Here, only the cutting rule differs; the search model and the answering model are the same everywhere.
> **K — how many chunks are handed to the model.** K=1 — one, the most similar chunk. K=5 — five similar chunks at once.

> **At K=1**, version 2 answers correctly in 52 of 72 cases (72.2%) against 41 of 72 (56.9%) for version 1 — fifteen and three tenths percentage points of gap, the same criterion as in Case 1.

| Cutting version | K=1 | K=2 | K=3 | K=5 |
|---|---|---|---|---|
| v1 — by character count | 56.9% (41/72) | 59.7% (43/72) | 63.9% (46/72) | 73.6% (53/72) |
| v2 — by sentence boundaries | 72.2% (52/72) | 83.3% (60/72) | 77.8% (56/72) | 80.6% (58/72) |
| v3 — by word boundaries | 55.6% (40/72) | 58.3% (42/72) | 63.9% (46/72) | 63.9% (46/72) |
| v4 — character count + overlap | 55.6% (40/72) | 65.3% (47/72) | 66.7% (48/72) | 70.8% (51/72) |

## Speaker notes

The previous beat's proxy measurement answered the question "is the literal gold span intact inside one chunk". The course owner put the question more honestly: what happens to the final answer when the real pipeline pulls in several chunks at once? This beat measures exactly that.

Here's how the measurement is built. The documents and questions here are exactly the same as in the previous measurement — sixty documents and seventy-two questions, the same corpus preparation. Only the cutting rule changes: the documents, questions, and models themselves are the same across all four versions. The question is embedded by the same model as in Case 1, and it searches for the K most similar chunks by cosine similarity — among the chunks of all sixty rig documents at once, with the document holding the correct answer given no special treatment: the task is set up honestly, as it would be in production, where you don't know in advance which document to search in. The retrieved chunks are handed to `gpt-4o-mini`, the model answers, and the answer is checked by the same criterion this session's Case 1 already used — whether the answer contains the correct gold substring. That's one thousand one hundred fifty-two real calls to the model: four cutting versions, four values of K, seventy-two questions.

The parameter K here means one simple thing — how many chunks the model sees before answering. At K=1 it's one chunk, the one most similar to the question; at K=5 it's five of the most similar chunks at once, regardless of what else sits further down the similarity list.

At the headline K=1, the difference shows up right away: the version that cuts by sentence boundaries answers correctly on fifty-two of seventy-two questions — seventy-two and two tenths percent. The version that cuts by character count answers correctly on forty-one of seventy-two — fifty-six and nine tenths percent. The gap is fifteen and three tenths percentage points, and this is on the same strict criterion that already checked Case 1's answers — not a new metric with a different threshold that would give numbers you couldn't compare.

The table shows the same comparison across all four tested values of K. Version two answers correctly more often than version one at every single one of them without exception — from seventy-two to eighty-three percent for version two against a range of fifty-seven to seventy-four percent for version one. Versions three and four — both cheap fixes with no understanding of the boundary of meaning — behave similarly to each other and sit closer to version one than to version two.

Whether this gap changes as K grows, and by how much — next.

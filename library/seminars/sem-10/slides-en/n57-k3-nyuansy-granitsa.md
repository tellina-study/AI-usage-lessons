---
id: n57
type: criteria_checklist_and_boundary
duration_min: 0.5
assertion: "Hybrid search is needed on a large, heterogeneous base with a high cost of ranking error — on a small, uniform base the gain isn't visible"
learning_goal: "Case 3's hybrid boundary in direct form (A7): a small, uniform base is a candidate for cutting if the slot runs short. Part 1 of 2 (n58 — the reranker's boundary, closing the third axis line): split because 15pt half-size type leaves no room for two boundaries and the closing of the axis line on one slide (issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    The hybrid's boundary criterion, a "when it's needed · when it isn't"
    table.
  backup: >
    SETKA-KEYSOV.md / rework/section-3-chem-iskat.md, "Nuances."
---

# When the hybrid isn't needed, and when the reranker fails

## Assertion

"Smarter" doesn't always mean "finds more often": the result depends on which corpus and which questions it was given.

## Visual

> **Criterion.** Hybrid search is a candidate for cutting within Case 3 (item №2 of the general cutting order, after cutting the detailed perceptual-hash breakdown in Case 4) if the slot doesn't fit all the material: the method works correctly, but on a small, uniform base it isn't needed to the degree it's needed on a large, heterogeneous one.

| When it's needed | When it isn't |
|---|---|
| The base is large, and questions are phrased both with exact terms and in retellings in one's own words | The base is small and uniform in how its questions are phrased |
| The cost of a ranking error is high — the requester gets a wrong answer from the second- or third-ranked candidate | The difference between a single method and the merge of two is statistically indistinguishable on this base |

## Speaker notes

Two boundaries of the third case, both in direct form, without general caveats — let's start with the hybrid's boundary.

Hybrid search is needed when the base is large and heterogeneous in how its questions are phrased, and when the cost of a ranking error is high. It isn't needed when the base is small and uniform — there the difference between a single method and merging two is statistically indistinguishable, and the added complexity doesn't pay for itself. This is exactly why hybrid search is a candidate for cutting within Case 3 (item №2 of the general cutting order, after cutting the detailed perceptual-hash breakdown in Case 4) if the slot doesn't fit all the material: the method isn't bad, it's just that on a small base its gain isn't visible.

This boundary is a direct conclusion from this session's measurement: the difference between a single search method and merging two was statistically significant precisely because the corpus was deliberately toughened with confusable clusters and harsh phrasings. On a base of ten to twenty FAQ entries, the kind Olga's training center started last session with, that spread of phrasings and that cost of error may simply not exist — and then the extra rank-merging node in n8n adds process complexity without adding measurable benefit.

The boundary is named in direct form: the criterion names specific conditions on both sides — the size of the base, the diversity of phrasings, the cost of error — and each of these can be checked against your own situation, without relying on the general impression that "hybrid sounds smarter." This form doesn't let a general phrase like "added complexity sometimes doesn't pay off" into the text: instead there's a list of conditions you can apply to your own base and get an answer right away.

The second boundary belongs to the reranker, and it has two sides at once: both confirmed by the same measurement, with no assumptions here about how it should have behaved. Next.

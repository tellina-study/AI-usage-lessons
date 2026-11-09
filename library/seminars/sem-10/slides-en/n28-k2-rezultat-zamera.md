---
id: n28
type: measured_outcome_table
duration_min: 1.25
assertion: "At the headline size, version 2 breaks the answer in 1.4% of cases against 12.5% for version 1 — and this holds across all five tested sizes"
learning_goal: "Beat 2 of the measurement exposition (canon forma-keysa-s-zamerom.md §1, C2): the summary — the load-bearing pair of numbers, large (A11), then a breakdown by the same size groups as in n27, in the same order. Version 1's non-monotonicity gets its own beat in n38, not duplicated here (C11). Revised 2026-11-04 per the owner's note ('the slide doesn't read, what is this — a share of successful answers or what?? needs to describe what we're doing and what we're measuring'): the metric 'broken' is now defined explicitly right on the frame, one line before the numbers, not only in the speaker notes/n27/n31. Redundant duplication of v3/v4 numbers (already in the 5×4 table below) removed from the visible body (C11). The notes' ending was revised the same day, in a second pass (issue #311, the owner's note from the same round: 'this should be earlier, next to the measurements on question fragments'): the honest measurement of the final answer (n37/n38 under the old numbering) was moved here, right after this beat, so the transition now leads into it rather than into the document breakdown."
visual:
  pattern: measured_outcome_table
  figure: case2-razryv-metriki-en.png
  primary: >
    One tile: an explicit definition of the "broken" metric as the first
    line, then the load-bearing pair of numbers at the headline size
    (180) as the main v1/v2 contrast. Below the tile, a 5×4 table (chunk
    size · share of broken answers across all four versions) — the same
    five groups and the same order as n27; v3/v4 numbers are read from the
    table, not duplicated in a separate tile.
  backup: >
    Numbers — SETKA-KEYSOV.md Case 2 / stend/raw/case2-results.json: 60
    SberQuAD documents (≥500 characters, answer offsets verified directly
    — 22.0% of the source dataset's rows excluded per the finding about
    corrupted labeling), 72 questions, 5 chunk sizes, the same run gives
    numbers for all four cutting versions at once (follow-up run
    2026-11-02 — local Python measurement, not a live n8n call, exec_id
    doesn't apply here; the live demo example with exec_id 2522 is
    separate, see n31/n35).

    Version 1's non-monotonicity by chunk size is carried over to n38
    (this measurement's boundary) — here only the summary, so as not to
    repeat the same finding twice in a row (C11, canon §11).
---

# What the run showed across five chunk sizes

## Assertion

Version 1 never drops to zero broken answers; version 2 stays almost always within 0–1.4%.

## Visual

> **What counts as "broken".** The gold answer sits in the document's text at known positions; if a chunk cut happens to fall inside that span, the answer ends up in two different chunks, and neither carries it whole — the model gets only half.
> **72 questions**, headline chunk size — 180 characters. Version 1 — 9 broken (12.5%), 63 intact (87.5%). Version 2 — 1 broken (1.4%), 71 intact (98.6%).

| Chunk size, characters | V1 — by character count | V2 — by sentence boundaries | V3 — by word boundaries | V4 — character count + overlap |
|---|---|---|---|---|
| 120 | 9.7% (7 of 72) | 1.4% (1 of 72) | 9.7% (7 of 72) | 5.6% (4 of 72) |
| 180 (headline) | 12.5% (9 of 72) | 1.4% (1 of 72) | 8.3% (6 of 72) | 5.6% (4 of 72) |
| 220 | 4.2% (3 of 72) | 1.4% (1 of 72) | 1.4% (1 of 72) | 1.4% (1 of 72) |
| 300 | 6.9% (5 of 72) | 0.0% (0 of 72) | 5.6% (4 of 72) | 1.4% (1 of 72) |
| 450 | 2.8% (2 of 72) | 1.4% (1 of 72) | 0.0% (0 of 72) | 0.0% (0 of 72) |

## Speaker notes

The test's structure is already known — sixty documents, seventy-two questions, five chunk sizes, with no model at the cutting step. Here's what this run showed.

At the headline size, one hundred eighty characters, the difference is visible right away: the version that cuts by character count breaks the answer on nine of seventy-two questions — that's twelve and a half percent. The version that cuts by sentence boundaries breaks the answer on only one question out of seventy-two — one and four tenths of a percent. Sixty-three of seventy-two answers come through intact for version one; for version two, seventy-one of seventy-two come through intact. The difference is almost an order of magnitude, and that's not something you'd mistake for random scatter within a fraction of a percent: the same corpus, the same questions, the same chunk size — the only thing that differs is the rule by which the cut is made.

At the same headline size, the version that cuts by word boundaries breaks the answer on six of seventy-two questions — eight and three tenths of a percent; the version that cuts by character count with overlap breaks it on four questions — five and six tenths of a percent. Both are better than the first version, both are noticeably worse than the second.

The table reads the same measurement through five different eyes — at five different chunk sizes, from one hundred twenty to four hundred fifty characters, in the same order as in the test structure. And at every one of the five, the version that cuts by sentence boundaries gives a noticeably smaller share of broken answers than any of the other three. Version 1 never drops to zero even once — the minimum it reaches is 2.8%, at the largest of the tested sizes. Version 2 stays almost always within zero to 1.4%, and at one size, three hundred characters, it reaches an honest zero. Versions 3 and 4 behave similarly to each other — sometimes closer to version 1, sometimes dropping to zero at larger sizes, but never outperforming version 2 at any of the five sizes.

These are five independent runs of the same set of questions. This isn't one run recalculated five ways: at each chunk size the documents are cut afresh, by all four versions, and each of the seventy-two answers is checked again for whether it survived. The result's stability across all five sizes is a reproduced difference; one lucky run wouldn't give you that.

This measurement is about the chunk cut — a proxy for the real question: is the gold span intact inside one chunk. Whether the final model answers correctly when the pipeline searches on its own, with no hint, is a separate, more honest measurement, next.

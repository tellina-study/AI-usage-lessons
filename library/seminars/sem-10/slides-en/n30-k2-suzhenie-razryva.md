---
id: n30
type: measured_outcome_table
duration_min: 0.75
assertion: "Growing K narrows the gap between version 1 and version 2 by more than half, but version 2 remains the better version at every one of the four tested K without exception"
learning_goal: "Continuation of n29 — the answer to the course owner's hypothesis ('if we return several chunks, doesn't that compensate for the gap between the versions'). The hypothesis was partly confirmed: the gap in accuracy_strict narrows from 15.3 to 7.0 percentage points (more than 2×), but doesn't close to zero — version 2 stays the better version at every one of the four K, and version 1 needs to return roughly 5× more candidates (K=5) to approach what version 2 already delivers at K=1. Part 2 of 2 (continuing n29: the measurement's definition and the 5×4 table live there, not repeated here, canon C11). Moved together with n29 the same day to right after n28 (issue #311, the round's second note 2026-11-04 — see n29). The notes' ending was revised in the same round: the transition now leads into the breakdown on one real document (next beat), not into Case 3's divider. Letter-suffix pending deck finalization (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: measured_outcome_table
  primary: >
    Tile on the narrowing gap (15.3 → 7.0 p.p.), tile "version 2 remains
    the best at every K" comparing v1@K=5 and v2@K=1.
  backup: >
    Numbers — stend/README.md "Case 2, follow-up pass 2026-11-04",
    sections "The owner's hypothesis confirmed — at K≥3, not earlier" and
    "Second honest conclusion". Gap in accuracy_strict: 15.3 p.p. (K=1) →
    23.6 p.p. (K=2, breaks monotonicity — honest noise from a small
    sample: 72 questions, 1 question = 1.4 p.p., named separately in the
    notes, not hidden) → 13.9 p.p. (K=3) → 7.0 p.p. (K=5). v1@K=5 =
    73.6% (53/72), v2@K=1 = 72.2% (52/72) — a difference of one notch out
    of 72 questions, hence "roughly" in the frame's text.
---

# The gap narrows, but doesn't disappear

## Assertion

As K grows, version 1 catches up to version 2 noticeably — but version 2 remains the better version at every one of the four tested values without a single exception.

## Visual

> **The gap narrows by more than half.** At K=1, version 2 outruns version 1 by 15.3 percentage points (72.2% against 56.9%). At K=5 — by 7.0 percentage points (80.6% against 73.6%): more than twice as narrow.

> **Version 1 needs roughly five times more candidates.** To get close to the result version 2 already delivers at K=1 (72.2%, 52 correct answers out of 72), version 1 needs to return five candidates instead of one: at K=5 it reaches 73.6% (53 of 72) — nearly the same number, but at the cost of a fivefold increase in K. Version 2 remains the better version at every one of the four tested K without exception.

## Speaker notes

The hypothesis the course owner approached this measurement with went like this: if the pipeline returns several chunks anyway, does that smooth out the difference between careful and crude cutting? The answer is yes and also no at the same time, and the numbers show why.

Yes — the gap really does narrow, and noticeably. At K=1, the version that cuts by sentence boundaries outruns the version that cuts by character count by fifteen and three tenths percentage points. At K=5, the same gap is seven percentage points: more than twice as narrow. Growing K helps both versions at once, and helps the weaker one even more: version one grows from fifty-seven to seventy-four percent, version two grows from seventy-two to eighty-one. Version one's absolute gain is bigger precisely for this reason — that's where the narrowing of the gap between them comes from; version two keeps performing better at every step, it just grows more slowly in absolute numbers.

In fairness — the intermediate point K=2 breaks from this smooth narrowing: the gap there grows to twenty-three and six tenths percentage points, before falling again at K=3 and K=5. Seventy-two questions is a small sample, where one question is worth one and four tenths percentage points, and such a jump at one intermediate point is explained by honest sample noise; there's no directional trend in it. The stable direction — from K=1 to K=5, the gap shrinking by more than half — reads independently of this noise.

And no — narrowing doesn't mean closing. Version two remains the better version at every one of the four tested values of K without a single exception: the gap never flips in version one's favor anywhere. What's more, the numbers show the price of narrowing directly: for version one to give a result close to what version two already gives at K=1 — seventy-two percent correct answers — version one needs to return five candidates instead of one. At K=5, version one gives seventy-three and six tenths percent — nearly the same number, but version two got there at K=1, while version one needs five times more chunks returned to the model per question to get there, meaning a fivefold cost in calls.

The takeaway for Olga's training center: returning several chunks instead of one is a working, measured way to soften the consequences of crude cutting, but not a replacement for careful cutting by meaning. It buys back part of the lost quality at the price of a multiplied context volume per question — while good cutting gives a comparable result with a single, cheapest possible request.

The proxy measurement and the honest measurement of the final answer point in the same direction. What this looks like on one real document — next.

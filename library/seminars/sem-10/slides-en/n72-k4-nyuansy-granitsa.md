---
id: n72
type: criteria_checklist_and_boundary
duration_min: 0.5
assertion: "Perceptual hash confidently catches near-duplicates under recompression — and weakens noticeably under rotation, in places down to the level of a random stranger receipt"
learning_goal: "Case 4's perceptual-hash boundary in direct form (A7): the geometry of the shot, confirmed by a measured limit. Part 1 of 2 (n73 — when to try multimodal search, closing the session's fourth row): split, because the 15pt floor font size leaves no room for the table and three tiles on one slide (issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A table "soft duplicate · hard duplicate vs. random stranger," a tile
    for phash's boundary of applicability.
  backup: >
    SETKA-KEYSOV.md / rework/section-4-poisk-po-izobrazheniyam.md,
    "Nuances," verbatim. Numbers — stend/raw/case4-results.json, 6
    receipts.
---

# Where the exact-repeats method stops being reliable

## Assertion

In one case, a duplicate under rotation came out farther by distance (27 bits) than a random stranger receipt (14 bits) — the method is formally wrong.

## Visual

| Receipt | soft duplicate (bits out of 64) | hard duplicate | random stranger |
|---|---|---|---|
| receipt_07 | 1 | 27 | 14 |
| receipt_18 | 0 | 10 | 24 |
| receipt_17 | 0 | 30 | 35 |
| receipt_04 | 1 | 40 | 23 |
| receipt_11 | 0 | 10 | 44 |
| receipt_19 | 0 | 10 | 49 |

> **Boundary of applicability.** Under rotation, the distance grows to 10–40 bits — comparable to a random stranger receipt in half the receipts. The method solves the subclass "same scan, recompressed"; rotation doesn't fall into that subclass.

## Speaker notes

Perceptual hash is a working, clean result for a narrow class of task, and this result's boundary is a measured limit; calling it a general caveat would be wrong.

A controlled check on six receipts shows two transformations. A "soft" duplicate — recompression, a few-percent shrink, imitating a repeat scan of the same document — gives a distance of zero to one bit out of sixty-four possible, confidently distinguishable from the distance to a random stranger receipt. This is a working result with not a single call to a model.

A "hard" duplicate — a twelve-degree rotation plus edge cropping, imitating a photo shot at an angle with a phone — behaves differently. The distance grows noticeably, to ten-to-forty bits, and in half of the six checked receipts it ends up comparable to the distance to a randomly picked stranger receipt. In one case, receipt_07, the duplicate under rotation is even farther by distance — twenty-seven bits — than the random stranger receipt — fourteen bits. That means at this specific point the method is formally wrong: it's more likely to mistake this duplicate for a stranger document than for a repeat.

This is the method's substantive boundary, named in direct form — a general caveat of "sometimes works worse" won't cover for it here: perceptual hash solves the subclass "same scan, recompressed or slightly shifted," and stops being reliable where the shot's geometry changes: it isn't just about quality.

For Olga's training center, this means: if the requester sends a photo of the same form shot by phone at an angle (not a repeat scan of the same file), perceptual hash shouldn't be relied on for that task without extra processing — for example, aligning the frame's geometry before comparing hashes.

Next — the honest limit of the check itself, and when it's worth trying multimodal search directly at all.

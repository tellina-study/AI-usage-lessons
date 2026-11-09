---
id: n72b
type: measured_outcome_table
duration_min: 1.5
assertion: "The date reads at the quarter and no longer reads at the eighth — its boundary. The amount reads at the sixteenth and no longer reads at the thirty-second — its own boundary, one step smaller"
learning_goal: "Owner edit 2026-10-27, closing two deck gaps with an honest rerun (issue #299): (1) the zoom on the date in n72a sat on the EXTREMES of the range (full vs 1/32), not on the actual boundary — this beat zooms on exactly the quarter/eighth pair, where the threshold really passes; (2) a crop of the 'amount' field had not existed anywhere in the deck — after fixing the prompt leak, the amount turned out to have its own boundary too (sixteenth/thirtysecond), and it deserves the same close-up as the date's. Both crops are real files from the honest rerun of 2026-10-27, same method: a proportional crop of one region on two real resolution files, LANCZOS for the readable side, NEAREST for the blocky one."
visual:
  pattern: measured_outcome_table
  figure: k6-zoom-granitsy-oba-polya-en.png
  primary: >
    Two rows of crops, one above the other. Top — the "date" field: the
    quarter (424×518, last readable, 5 of 5) next to the eighth (212×259,
    first unreadable, 0 of 5). Bottom — the "amount" field: the sixteenth
    (106×129, last readable, 5 of 5) next to the thirty-second (53×64,
    first unreadable, 0 of 5) — the same "last readable / first
    unreadable" pair shape as the date above, just one step smaller on the
    compression scale.
  backup: >
    Numbers from `stend/zamery-k5-k6/README.md`, Measurement 4.1 (the
    honest rerun of 2026-10-27, already revealed by beats n70 and n71
    separately: amount 25 out of 30 — the threshold between sixteenth and
    thirtysecond; date 0 out of 15 starting at eighth). This beat
    introduces no new numbers — it shows the same two facts to the eye, on
    the receipt's own real pixels, `receipt-01`.

    Both crops come from
    `stend/zamery-k5-k6/receipts/resolution/receipt-01-*.png`, REAL files
    from the honest measurement (not re-compressed from full — each crop is
    cut from the file of its OWN resolution, meaning literally the same
    bytes that went into the model are being compared). The field's region
    on each file comes from coordinates, not from eyeballing: the text
    bounding box was first computed on a clean 1200×1600 canvas via a real
    font render (`ImageFont.getbbox`, the same coordinates as in
    `generate_receipts.py:draw_receipt`), then projected onto the photo via
    the receipt paper's own bounding box (a brightness threshold between
    the paper and the table, from the histogram). The result was checked
    visually before being locked into
    `stend/zamery-k5-k6/build_k6_field_crops.py`.

    Figure build (rebuilt 2026-10-27 after the honest rerun):
    `build_k6_field_crops.py` builds `k6-zoom-data-porog-granitsa.png`
    (date, boundary quarter/eighth — these numbers weren't touched by the
    leak and remain correct unchanged) and `k6-zoom-summa-granitsa.png`
    (amount, its OWN boundary sixteenth/thirtysecond — rebuilt from
    scratch after the honest rerun, replacing the previous crop), both
    composed onto one canvas, `k6-zoom-granitsy-oba-polya.png`, for this
    beat's `figure:` (the slide format carries one `figure:` per beat, see
    `deck_config.figure_for`). **The script no longer builds the old
    `k6-zoom-summa-melkaya.png`** (full vs thirtysecond, captioned "also
    reads, 5/5") — its caption became factually wrong after the honest
    rerun (`thirtysecond` for the amount is 0/5, not 5/5); the file stays
    on disk as a historical artifact, not quietly deleted, but is no longer
    used in the deck. An EN re-render is needed for this track (added for
    this EN track, issue #172/#319) — the underlying receipt crops carry
    printed Russian/Cyrillic receipt content that an EN deck needs
    re-rendered in English.

    Run numbers and execution identifiers don't appear on the visible
    layer (BRIEF §2, the same principle as on n68-n72a).
---

# The "date" field and the "amount" field, up close

## Assertion

The date's boundary falls between the quarter and the eighth. The amount's falls between the sixteenth and the thirty-second, one step smaller. Both fields break — just at a different character height.

## Visual

> **Threshold boundaries.** Date: quarter (424×518) — reads, 5 of 5; eighth (212×259) — no longer readable, 0 of 5. Amount: sixteenth (106×129) — reads, 5 of 5; thirty-second (53×64) — no longer readable, 0 of 5 — a gray, blocky patch with not a single recognizable digit, and all five of the model's attempts converge on the same wrong number.

## Speaker notes

Two crops from the same receipt, and now they share the same logic — because after the honest rerun of the measurement, both fields turned out to have their own boundary, just at a different character height.

The top pair is about the date, and shows its real boundary: a pair of neighboring compression steps between which the date stops reading. On the left — a quarter of the original size, four hundred twenty-four by five hundred eighteen pixels, and the date reads with not a single error, five out of five attempts. On the right — the next compression step, the eighth fraction, two hundred twelve by two hundred fifty-nine pixels, and the date no longer reads even once, zero out of five. The date's real threshold falls right between these two crops.

The bottom pair is about the amount, and here a crop was needed separately, because the deck didn't have one before. Before the prompt was honestly fixed, it looked like the amount had no threshold at all — it read correctly at all six sizes tested. After the fix, it turned out: there is a threshold, just one step smaller than the date's. On the left — the sixteenth fraction, one hundred six by one hundred twenty-nine pixels, the amount reads with not a single error. On the right — the thirty-second fraction, fifty-three by sixty-four pixels for the whole receipt frame. Look closely at this crop: a gray, blocky patch in which the human eye wouldn't confidently identify a single digit. And indeed — all five of the model's attempts at this resolution converged on the same wrong number.

Compare these two pairs directly. Both fields, on the same photo, in the same measurement, with the same compression step, have their own personal boundary. The date breaks a step earlier, the amount a step later, because the amount is set bigger and starts from a greater character height. But both have a boundary, and both crops show it on the receipt's real pixels — the table above gave only numbers, here you can see the image itself: on the right side of each pair — pixel mush, in which neither the human eye nor, judging by the outcome, the model finds any purchase anymore.

Why the amount's margin turned out bigger than the date's is a separate, honest question, and this measurement has no measured answer to it — only the hypothesis about the amount's large, stable font already named on previous screens. What matters here is something else: both facts from previous beats' tables are now visible not just in a "correct/wrong" column, but in the actual pixels the model really received.

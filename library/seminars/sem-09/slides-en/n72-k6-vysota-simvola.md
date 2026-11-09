---
id: n72
type: mechanism_field_contrast
duration_min: 1.0
assertion: "Two fields in the same file break at different steps of the same compression — because they have a different glyph height at the start, not because the file got smaller"
learning_goal: "The mechanism that explains the case's turn: the degradation threshold is tied to a specific field's glyph height, not to the file's overall megapixels or resolution. The honest rerun of 2026-10-27 (issue #299) gives this mechanism stronger support than the leaked run did: TWO DIFFERENT thresholds for two fields of different height, not one field with no threshold at all. The numbers 25 out of 30 (amount) and 0 out of 15 (date), already revealed by beats n70/n71, return here as glyph-height ranges."
visual:
  pattern: mechanism_field_contrast
  figure: k6-shema-vysota-simvola-en.png
  primary: >
    A two-column figure on one file: a "amount, bigger font size" column
    and a "date, smaller font size" column, the same compression scale
    top to bottom — the amount breaks only on the last step, the date on
    the last two. Below — two threshold ranges ("1.5–3.1 px" for the
    amount, "2.9–5.8 px" for the date) with an honest note that the ranges
    partly overlap, not split exactly in half.
  backup: >
    The mechanism follows SETKA-KEYSOV-S9-part2.md, section "Case 6,"
    subsection "Nuances," item 3: "the degradation threshold is tied to
    glyph height, not to the file's megapixels." After the honest rerun
    of 2026-10-27 (fixing the prompt leak, issue #299), this support got
    stronger, not weaker: BEFORE the fix the amount "didn't break at
    all," which looked like suspiciously stable behavior; AFTER the fix,
    two honest thresholds are visible for two fields of different height
    — exactly what the mechanism predicts.

    The amount's base font size at full resolution is 64 pixels, the
    date's base font size is 32 pixels (`stend/zamery-k5-k6/README.md`,
    Measurement 4.1): the date is set at half the size, and that's the
    baseline without which the two different thresholds aren't
    comparable. The actual glyph height (not the font size, but the
    measured font bounding box) at each compression step for the amount:
    49.0 / 24.5 / 12.2 / 6.1 / 3.1 / 1.5 px; for the date
    (`measure_date_glyph_height.py`, added 2026-10-27): 23.0 / 11.5 / 5.8
    / 2.9 / 1.4 / 0.7 px — exactly half the amount's height at every step,
    as expected from a font size half as large.

    The amount's threshold is strictly between `sixteenth` (3.1 px, 5/5
    correct) and `thirtysecond` (1.5 px, 0/5 correct), that is, in the
    range 1.5–3.1 px. The date's threshold is strictly between `quarter`
    (5.8 px, 5/5 correct) and `eighth` (2.9 px, 0/5 correct), that is, in
    the range 2.9–5.8 px. The ranges PARTLY OVERLAP (a shared zone of
    2.9–3.1 px) — this is not exactly half and not two separate zones, and
    the figure names this honestly rather than flattening it into a neat
    "half as much."

    What's deliberately not on the frame: the reason why the amount's
    margin is so much bigger than the date's (a stable money-amount
    pattern, a large monospace font) is a separate, NOT measured
    hypothesis from beat n70 — repeating it here as part of the
    "mechanism" would mean passing off a guess as a finding.
---

# Why two fields of one file break differently

## Assertion

The file compresses the same way for every field on it. The character height of the fields is different from the start — and that's exactly what decides at which compression step a field stops reading.

## Visual

> **Amount and date.** One file, one compression scale — the amount at font size 64, the date at font size 32. The amount holds its character height longer — **25 of 30**, threshold **1.5–3.1 px** (between the sixteenth and thirty-second fractions). The date starts closer to the edge — **0 of 15** at the three smallest resolutions, threshold **2.9–5.8 px** (between the quarter and the eighth fractions), two steps earlier.

> **Mechanism.** The file's size in megapixels plays no role — what decides is the specific field's character height. Two fields, one compression, two different thresholds (the ranges overlap in the 2.9–3.1 px zone) — because they started at a different character height.

## Speaker notes

The two previous screens showed a pair of facts that look odd at first glance: the same photo, the same compression — and the fields break at different steps. The difference comes down to one simple property of these two fields.

The amount on this receipt is set in a large font size — sixty-four pixels. The date is set noticeably smaller — thirty-two pixels, exactly half. When the file is compressed, both fields shrink in the same proportion: the whole file is compressed, the text on it isn't compressed separately. But their starting height is different, and after the same compression, the character height stays different too.

That's the whole mechanism. The amount, starting from a bigger height, only reaches the size where the symbol becomes indistinguishable on the very last of the tested steps — its threshold sits in the range from one and a half to three and one-tenth pixels of character height. The date, starting twice as small, reaches its critical height two steps earlier — its threshold sits in the range from two and nine-tenths to five and eight-tenths pixels. Notice: these two ranges didn't split exactly in half, as you might expect from a font size twice as different — they partly overlap, in a zone around three pixels. The device is honest, but not as neat as you'd want for a tidy formula.

From here follows the main conclusion that explains both previous findings at once. Readability degradation is a property of a specific field on this file: the character height it started from. The file's megapixels and its overall resolution play no role here. Two fields of the same photo, the same compression — two different thresholds, because they had a different height at the start.

The practical takeaway is simple: you can't name one general "safe resolution" for a document. Every field has its own personal boundary, and the boundary of the smallest field on the document decides the point at which the whole document starts to suffer, even if its bigger fields stay reliable for a while longer.

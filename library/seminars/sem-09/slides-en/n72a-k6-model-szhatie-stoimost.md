---
id: n72a
type: measured_outcome_table
duration_min: 1.5
assertion: "Tokens fall from full size down to one-eighth, and don't fall any further after that — and it's exactly past that threshold that the date stops reading correctly, not before"
learning_goal: "Owner edit 2026-10-27: a separate beat — which model, what the call costs at each resolution, and a zoom on the real pixels of the field that breaks (not an abstract scheme like n72, but a real receipt crop). The enlarged crop makes '6.1 pixels' visible, not just a number."
visual:
  pattern: measured_outcome_table
  figure: k6-zoom-data-porog-en.png
  primary: >
    A model card and a "resolution · tokens · cost" table across all six
    steps, below it a figure — a real crop of the "date" field from
    receipt-01, full size next to 53×64 px, both enlarged the same amount
    so the difference is visible to the eye, not inferred from a number.
  backup: >
    Numbers from `stend/zamery-k5-k6/results-k6-resolution.json`,
    executions 736–746 and the neighboring ones (all `by_resolution`
    records), real `usage.prompt_tokens`/`usage.cost` fields from the
    OpenRouter responses, not computed by hand. The model —
    `qwen/qwen3-vl-8b-instruct` (README.md, "Call Spend";
    `qwen/qwen2.5-vl-7b-instruct` from `research/07` is no longer a valid
    id as of the measurement, honestly noted in the README).

    Figure `k6-zoom-data-porog-en.png` — a real crop of the "date" field
    from `stend/zamery-k5-k6/receipts/resolution/receipt-01-full.png` and
    `receipt-01-thirtysecond.png` (53×64 px, a REAL measurement file, not a
    synthetic example), both enlarged 2× by the same method (left —
    LANCZOS for readability, right — NEAREST, so as not to smooth over or
    invent pixels that aren't in the file). An EN re-render of the
    underlying receipt crop is needed for this track (added for this EN
    track, issue #172/#319) — the left crop reads, the right one is
    exactly what the model gets at this resolution: a blocky gray patch
    with not a single recognizable symbol.
---

# The model, compression, and what the call costs

## Assertion

Tokens only fall with file size down to one-eighth — past that, it's the same bill regardless of how much smaller the picture gets. The date's readability threshold sits BEYOND this price threshold, further down the compression scale.

## Visual

| Resolution | Pixels | Tokens | Price |
|---|---|---|---|
| full | 1698×2074 | 3673 | $0.00096 |
| half | 849×1037 | 1092 | $0.00028 |
| quarter | 424×518 | 436 | $0.00012 |
| **1/8** | **212×259** | **300** | **$0.00009** |
| 1/16 | 106×129 | 300 | $0.00009 |
| **1/32** | **53×64** | **300** | **$0.00009** |

> **The model `qwen/qwen3-vl-8b-instruct`.** Down to 1/8, tokens drop by a factor of 12; past that, not one more token of savings. The date already breaks here; the amount breaks one step later, but in the same free zone. Compressing to the price floor is free in money — you still end up paying in accuracy.

## Speaker notes

Two facts that used to live on separate beats meet on one screen here. The model on this rig for reading pictures is the vision version of the same family that's been answering in text all session. The real bill for each of the six resolutions is taken directly from the fields of the OpenRouter response itself, not estimated on the back of an envelope.

Look at the tokens. Full size — a bit over three thousand six hundred. Half — a little over a thousand, three times less. Quarter — almost three times less again. And from there, from one-eighth down to the smallest resolution we checked — three hundred tokens, and that number doesn't change at all. Three files wildly different in size — one hundred six by one hundred twenty-nine and fifty-three by sixty-four pixels — cost exactly the same.

This is exactly the step we talked about in the breakdown: the provider has a technical threshold for automatic re-compression, and below it, saving on file size stops turning into saving on the bill. Put this together with what we've already seen: both fields on this same receipt end up breaking, right in this same zone where the price has already stopped dropping by a single cent — the date first, already at the eighth fraction, the amount later, only at the smallest resolution tested. Compressing past the eighth fraction is completely free in money, and it's exactly in this same zone that accuracy starts to suffer — one field first, then the other — and that savings can't buy it back.

And here's what that looks like on real pixels, with your own eyes. On the left — the "date" field at full size, reading with no effort at all. On the right — the same field on the fifty-three-by-sixty-four-pixel file, enlarged the same amount as the left one, with no smoothing at all. This isn't an abstract scheme — it's a real crop of a real file that actually went into the model on this measurement. A gray patch with not a single recognizable digit — this is what "six and one-tenth pixels of character height" means in practice.

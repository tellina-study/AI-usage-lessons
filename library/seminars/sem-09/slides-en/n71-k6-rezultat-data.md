---
id: n71
type: measured_outcome_table
duration_min: 1.5
assertion: "The date is set smaller than the amount and breaks cleanly at the step where the amount still holds without a single error — the amount only breaks two steps later, at the smallest size"
learning_goal: "The second half of the case's turn: it isn't compression in general that breaks — one specific field does, and it doesn't break as noise, but as a confident, almost always repeatable wrong guess. The rig's own measurement, verbatim answers, for the first time with the date glyph's own height (measured separately on 2026-10-27, issue #299)."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of the same six file sizes with the date digit's height at
    each and the outcome "date correct." Below it — a breakdown of the
    verbatim wrong answers and a card about how stable the error is
    (almost always the same wrong guess).
  backup: >
    Numbers from `stend/zamery-k5-k6/README.md`, Measurement 4.1, the
    table "date correct" across the same six sizes: original, half,
    quarter — 5 out of 5 each; eighth, sixteenth, and thirty-second — 0
    out of 5 each. The receipt's true date is 12.09.2026.

    The date digit's height was measured separately for the first time on
    2026-10-27 (`measure_date_glyph_height.py`, the same method as for
    the amount — a real render of the DejaVuSansMono-Bold font at size 32,
    bounding box; values recorded in `receipts-manifest.json` as
    `date_glyph_height_px`). By resolution: 23.0 / 11.5 / 5.8 / 2.9 / 1.4 /
    0.7 pixels — exactly half the amount digit's height at every step,
    because the date is set at font size 32 against the amount's 64.
    Before this edit, the "6.1 px" caption on `n72` mistakenly named the
    AMOUNT digit's height at the `eighth` step, not the date's (README,
    section "Files in This Folder," the entry on
    `measure_date_glyph_height.py`) — there had been no dedicated column
    for the date's own height in the deck until then.

    Verbatim wrong answers (`results-k6-resolution.json`, field `date`):
    at the "eighth" size, all 5 repeats (executions 1090–1094) —
    `12.04.2024`; at the "sixteenth," all 5 repeats (executions 1095–1099)
    — `18.09.2024`, a different value, also full unanimity; at the
    "thirty-second" (executions 1100–1104) — 4 of 5 repeats `05.04.2024`,
    1 of 5 (execution 1102) `05.04.2025`. Dates kept in the receipt's own
    DD.MM.YYYY form, byte-for-byte, not reformatted to ISO. The
    `raw_text_seen` field (what
    the model claims to see) is verbatim-correct for the amount at the
    sizes where the amount still reads correctly (eighth, sixteenth — beat
    n70); at thirtysecond both fields are already wrong, and there
    `raw_text_seen` matches verbatim the wrong number the model named —
    it doesn't confuse "I don't see it" with "I see it wrong," for either
    the date or the amount.

    Run numbers and execution identifiers don't appear on the visible
    layer.
---

# The date on the same six file sizes

## Assertion

The date on the same receipt breaks earlier than the amount — cleanly, starting at the eighth fraction, and almost always with the same confident wrong guess.

## Visual

| File size | Date digit height | Date correct | What the model answered |
|---|---|---|---|
| original (1698×2074 pixels) | 23.0 px | 5 of 5 | correct: 12.09.2026 |
| half (849×1037) | 11.5 px | 5 of 5 | correct: 12.09.2026 |
| quarter (424×518) | 5.8 px | 5 of 5 | correct: 12.09.2026 |
| eighth (212×259) | 2.9 px | 0 of 5 | wrong, all 5 repeats: 12.04.2024 |
| sixteenth (106×129) | 1.4 px | 0 of 5 | wrong, all 5 repeats: 18.09.2024 |
| thirty-second (53×64) | 0.7 px | 0 of 5 | wrong: 4× 05.04.2024, 1× 05.04.2025 |

> **This receipt's true date is 12.09.2026.** At the three largest sizes it's read correctly every time. Starting at the size shrunk eight times — the very step at which the amount still holds without a single error (the amount only breaks two steps later, at the smallest size) — the date breaks cleanly: not a single correct reading beyond this point, **0 out of 15** in total.

> **Not noise, but an almost always confident, repeatable guess.** At two of the three broken sizes — shrunk eight times and sixteen times — all five repeats independently converged on the same wrong date: one value at the first, a different one at the second. Only at the smallest size, shrunk thirty-two times, is there no full unanimity: four of five repeats match, one lands on a neighboring day. The model almost always substitutes one specific wrong figure and sticks to it. Meanwhile, the "what I see" field for the amount stays verbatim correct wherever the amount still reads correctly: the model doesn't confuse "I don't see it" with "I see it wrong" for either of the two fields.

## Speaker notes

Same receipt, same six sizes, same measurement order — but now the focus is the date, printed noticeably smaller on the same photo than the amount: half the font size, and half the character height at every step too.

At the three large sizes — original, halved, and quartered — the date reads correctly in every attempt, exactly like the amount. And from there on, something happens that never happened to the amount on these same files: the date breaks, and breaks noticeably earlier on the compression scale. At the size shrunk eight times, the date stops reading correctly completely: not one correct answer out of five, and this is exactly the step where the amount still holds without a single error. At two even smaller sizes — the same result: zero out of five at each. In total, past this boundary — zero correct date readings out of fifteen attempts in a row.

An important detail is exactly how the date breaks. It isn't scattered, where every repeat names something of its own. At the size shrunk eight times, all five repeats in a row named the same wrong date — the 12th of April, 2024. At the size shrunk sixteen times, full unanimity again, but now on a different wrong value — the 18th of September of the same year. And only at the smallest size, shrunk thirty-two times, is there no full unanimity at all: four of five repeats agreed on one date, one landed on a neighboring day. The model doesn't wander — it almost always confidently substitutes one specific wrong date and sticks to it, again and again.

And one more detail worth separate attention. In those same answers where the date is wrong, the field where the model honestly writes what it actually sees in the amount line stays verbatim correct — at the sizes where the amount still reads correctly. In other words, in the same answer it doesn't get confused about the amount, either in reading it or in describing what it sees, while it confidently gets the date wrong, with not a single sign of doubt in the text. "I don't see it" and "I see it wrong" are different states for it.

The date is set noticeably smaller than the amount — and that's not a random coincidence with where it broke first. Why that is — next screen.

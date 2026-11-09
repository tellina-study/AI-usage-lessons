---
id: n70
type: measured_outcome_table
duration_min: 1.5
assertion: "The amount is read correctly on five of the six file sizes tested — and breaks cleanly only on the smallest, where the digit on screen is under two pixels tall"
learning_goal: "The case's turn (P1): the plan expected the amount to stop reading correctly under compression. The honest rerun of 2026-10-27 (issue #299, after fixing a prompt leak) found this threshold — it just sits farther out than the plan expected, and farther out than the date's. The rig's own measurement, with no guessing at the reason for this margin."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of six sizes of the same file, with the amount digit's height
    at each and the outcome "amount correct." On the last row — a clean
    break: 0 out of 5. Below the table — a summary card (threshold found,
    but farther out than expected) and an honest caveat about a possible
    (unmeasured) explanation for the margin.
  backup: >
    Numbers from `stend/zamery-k5-k6/README.md`, Measurement 4.1 (the
    honest rerun of 2026-10-27, after fixing a prompt leak, issue #299 —
    see the README's section "Prompt Leak Found and Fixed"; the previous
    version of this beat rested on a leaked run, where the prompt
    contained receipt-01's real amount as a "format example" — the old
    numbers are archived in
    `results-k6-resolution-PROTECHKA-2026-10-27.json` and are no longer a
    source). One and the same aged receipt at six sizes (a plain resize of
    one file, no reshoot), 5 live calls at each of the six sizes, 30 calls
    in one honest run (executions 1075–1104, `results-k6-resolution.json`).
    The amount digit's height at full size — 49.0 pixels, measured by a
    real font render, not assumed.

    Outcome by size: full (1698×2074) — height 49.0, correct 5 out of 5;
    half (849×1037) — height 24.5, correct 5 out of 5; quarter (424×518)
    — height 12.2, correct 5 out of 5; eighth (212×259) — height 6.1,
    correct 5 out of 5; sixteenth (106×129) — height 3.1, correct 5 out of
    5; thirty-second (53×64) — height 1.5, correct **0 out of 5**. Total
    25 out of 30.

    On the thirty-second, all 5 repeats (executions 1100–1104) converge on
    the same wrong number: the model answers `1600` instead of the true
    `18990`, and the `raw_text_seen` field matches this same wrong number
    verbatim every time — `1600,00 ₽`, not `18 990,00 ₽`. Not noise — the
    same confident wrong guess five times in a row.

    A plausible explanation for why the amount's margin is so much bigger
    than the date's (a bold, monospace font, twice the size of the other
    fields, and a short, stable pattern "N NNN,00 ₽") is stated in the
    README as NOT measured separately — on the frame it's named plainly as
    an open question, not as a cause.

    Run numbers and execution identifiers don't appear on the visible
    layer (BRIEF §2).
---

# The amount across all six file sizes

## Assertion

Six sizes of the same file, from the original down to one-thirty-second — the amount reads correctly on five of six. The expected threshold was found, but farther out than the measurement plan assumed.

## Visual

| File size | Amount digit height | Amount correct |
|---|---|---|
| original (1698×2074 pixels) | 49.0 px | 5 of 5 |
| half (849×1037) | 24.5 px | 5 of 5 |
| quarter (424×518) | 12.2 px | 5 of 5 |
| eighth (212×259) | 6.1 px | 5 of 5 |
| sixteenth (106×129) | 3.1 px | 5 of 5 |
| thirty-second (53×64) | 1.5 px | **0 of 5** |

> **Outcome: a threshold for the amount was found — but it sits farther out than the measurement plan assumed.** Twenty-five correct readings out of thirty, with not a single error on five of the six resolutions tested — all the way down to a size where the digit occupies a mere three and one-tenth pixels of height on screen. The amount only breaks at the smallest of the tested sizes: there, the digit height drops to one and a half pixels, and all five repeats give the same wrong amount — 1,600 rubles instead of 18,990.

> **Honestly: why the margin is this big hasn't been measured separately.** A plausible explanation: the amount is set in a large, bold, monospace font, twice the size of the receipt's other fields, and has a short, stable look, something like "eighteen thousand nine hundred ninety rubles." That's closer to recognizing a familiar pattern than to reading text from scratch — and that may well be why the amount's threshold sits noticeably farther out than the date's. But that's a hypothesis, not something this measurement checked on its own.

## Speaker notes

The same receipt was shrunk six times in a row, from the original size down to thirty-two times smaller — the only thing changing was the file size. At each size, the same amount was asked to be read several times in a row.

The result fits conveniently into one table. At the original size, the amount digit occupies about forty-nine pixels of height on screen, and the amount is read correctly in every attempt. Shrinking by half, by a quarter, and by an eighth drops the digit height to twenty-five, twelve, and six pixels respectively — and the amount keeps reading correctly every time. Shrinking by a sixteenth drops the height to three and one-tenth pixels — and again, not a single error. But on the smallest of the tested sizes, where the digit height drops to one and a half pixels, the amount breaks cleanly: not one correct answer out of five.

The total across all six sizes together: twenty-five correct readings out of thirty. The threshold past which the amount stops reading correctly, within this range of sizes, has been found — it just sits farther out than the measurement plan assumed.

This is worth saying honestly: the plan expected the threshold to show up earlier, somewhere in the middle of the range. It showed up — but only at the last compression step. And the amount doesn't break raggedly: at the smallest size, all five repeats in a row give the same wrong number — one thousand six hundred rubles instead of eighteen thousand nine hundred ninety. The model honestly writes the same wrong number in the "what I see" field — it doesn't confuse "I can't see it" with "I see it wrong"; it confidently and reproducibly reads a pattern, but gets the actual digits wrong.

Why the amount holds out so much longer — longer than the date on the same photo — wasn't checked separately by the measurement. There's a reasonable guess: the amount is set in a large, bold font with uniform letter width, noticeably bigger than the receipt's other text, and it has a short, predictable look — a number, a space, two digits after the comma, a ruble sign. Perhaps the model needs far less detail for such a stable pattern than it does for free text, and that's why it has a bigger margin. That's a hypothesis — the measurement itself didn't check this question separately, and that's the honest boundary of this screen.

Before celebrating that margin, it's worth looking at a different field on the same photo — next screen.

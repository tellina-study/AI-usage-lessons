---
id: n73c
type: answer_breakdown_table
duration_min: 2.0
assertion: "At the heaviest resolution, the single call doesn't read the photo at all — in all five repeats it substitutes what's written in the request as the read amount, and declares a match, even when the request is deliberately wrong"
learning_goal: "Beat n73c (issue #299, Z3): a breakdown by group (C2, item 3) — Finding 1 of the zamery-k6-edinyy README, the single call's load-bearing number for the case. Verbatim data from execution thirtysecond #1–5, set against the two-step device's safe failure on the same resolution."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table of five live repeats at the `thirtysecond` resolution (53×64
    px): whether the request is correct, what it states, what the model
    named as the read amount, what text it used to describe "what it
    saw," and what verdict it handed down. All five rows show the same
    thing: the read number exactly equals the stated number. Below the
    table — a "safe failure / dangerous confirmation" card comparing this
    with the two-step device's behavior on the same file.
  backup: >
    Numbers from `stend/zamery-k6-edinyy/README.md`, section "Finding 1
    (Main)": at `thirtysecond` (53×64 px, amount digit height 1.5 px), all
    5 of 5 single-call repeats name the read amount as exactly
    `zayavka_sum_rub`, not the receipt's true amount (18990) — including
    three cases where `zayavka_verna=False` (a deliberately wrong
    request). The `raw_text_seen` field changes its formatting to match
    the request each time (sometimes with "₽" and kopecks, sometimes
    without) — the model isn't simply repeating a number, it's composing
    a plausible "as if read" text string to go with it. The verdict in
    all 5 of 5 is `sovpalo` ("matched"), including the three cases with a
    deliberately wrong request.

    Comparison with the two-step device — same README: at this same
    resolution, with no request text, the two-step device stably
    hallucinates the same number, unrelated to the truth — all 5 of 5
    calls returned `sum_rub=1600`
    (`../zamery-k5-k6/results-k6-resolution.json`,
    `thirtysecond.entries[*].parsed.sum_rub`). The deterministic code
    compares `1600` to the request's amount and almost never finds a
    match — the two-step device's reading failure turns into a SAFE
    failure (the request goes to a manual check). In the single call, the
    same reading failure drifts toward the stated number — toward where
    the failure is DANGEROUS: a wrong request gets stamped "matched" and
    moves on without a check. The README calls this "a shift of the
    error's direction from conservative to dangerous" — not a worsening
    of the same error, but a different failure class.

    An honest limit, stated plainly in the README: the anchoring is
    measured on n=3 of 3 (deliberately wrong requests at this resolution)
    and n=5 of 5 full repeats — the effect at this n is clean (100%), but
    that's no basis for a precise rate of "how often" in the general case
    with a different receipt or a different model.
---

# Echo of the request at the heaviest resolution

## Assertion

In five repeats out of five, at the smallest file size, the single call names the read amount as exactly the number written in the request — including three cases where the request is deliberately wrong.

## Visual

| Repeat | Is the request correct? | Stated in text | Amount named "read" | What the model writes it sees |
|---|---|---|---|---|
| 1 | no | 9800 | **9800** | "9800" |
| 2 | yes | 18,990 | 18,990 | "18 990,00 ₽" |
| 3 | no | 12,450 | **12,450** | "12 450 ₽" |
| 4 | yes | 18,990 | 18,990 | "18 990,00 ₽" |
| 5 | no | 27,300 | **27,300** | "27 300" |

> **The receipt's true amount across all five repeats is 18,990.** In not one of the five answers does the model name this number, except in the cases where it's the same number in the request. The verdict in all five is "matched," including three cases with a deliberately wrong request (rows 1, 3, 5).

> **Safe failure versus dangerous.** At this same resolution, the two-step device — with no request text at hand — names the same number in all five repeats, 1,600, unrelated to either the truth or the request. The deterministic code almost never finds a match with this number, and the request goes to a manual check — a reading failure turns into caution. The single call turns the same reading failure into confirmation: a wrong request gets stamped "matched" and moves on without a check.

## Speaker notes

This is the main finding of the whole measurement, and it explains the two "extra" correct answers the single call showed on the previous summary.

At the heaviest resolution — the file shrunk thirty-two times, where the amount digit's height drops to a pixel and a half — the single call names the read amount as exactly the number written in the request, five times in a row. Not a close or similar number — the same one, down to the digit. And this happens regardless of whether the request is correct or not: three of the five repeats carry a deliberately wrong stated amount, and in all three the model names that same amount as read off the photo, and in all three it hands down the verdict "matched."

Notice the last column. The model doesn't just return a number — every time it also changes the description of what it supposedly sees on the photo, adjusting the format to match the request: sometimes with a ruble sign and kopecks, sometimes bare digits. This isn't a human who would honestly say "I can't read it" — it's a confident, detailed description of a reading that never happened.

Compare this with what the two-step device does on this exact same file. With no request text at hand, the model has nothing to drift toward — and it hallucinates the same number, one thousand six hundred, unrelated to either the truth or to anything real. The deterministic code compares this number to the request's amount and almost never finds a match — the reading failure turns into safe caution: the request goes to a human.

Here's the difference, and it isn't the same error in two disguises. In the two-step device, a reading failure pulls the system toward an extra check — the worst-case cost of that failure is one more glance from Olga. In the single call, a reading failure pulls the system toward a false confirmation — a wrong amount gets stamped "matched" and moves on without a check. This shift in the direction of the error — from cautious to dangerous — is the main cost of merging the steps.

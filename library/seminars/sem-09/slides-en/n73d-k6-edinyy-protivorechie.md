---
id: n73d
type: answer_breakdown_table
duration_min: 1.5
assertion: "At the sharpest resolution, the model reads the amount correctly five times out of five, and two times out of five still gets the verdict wrong — because it's comparing its own two numbers, written as different text, as if they were different"
learning_goal: "Beat n73d (issue #299, Z3): the breakdown by group's second finding (C2) — Finding 2 of the zamery-k6-edinyy README. Shows that the single call's failure doesn't reduce to bad reading: at the best resolution, reading is flawless, and the cross-check still breaks — the language comparison step is unreliable on its own."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table of three live repeats at `full` resolution, where the stated
    amount matches the true one: the amount read, the amount from the
    request (both fields — the same number, different text), the model's
    verdict, and whether it's correct. Two of three verdicts are wrong
    with identical read numbers. Below the table — a comparison with
    deterministic code, which never errs on these same numbers.
  backup: >
    Numbers from `stend/zamery-k6-edinyy/README.md`, section "Finding 2":
    at `full` (49 px, the sharpest image) the amount is read correctly 5
    out of 5 times, and EVERY time the model names `sum_rub="18990,00"`
    and `zayavka_sum_rub="18990"` — the same number written twice, in a
    different format (",00" and without). On the three repeats where
    `zayavka_verna=True` (the stated amount really equals the true one),
    the verdict diverges: `full #1` → `ne_sovpalo` ("didn't match,"
    wrong), `full #3` → `sovpalo` ("matched," correct), `full #5` →
    `ne_sovpalo` (wrong) — three DIFFERENT live calls on the SAME image
    with the same request gave two different outcomes with identical read
    numbers.

    This isn't a photo-reading error (the amount is read correctly all 5
    times) — it's an error in the model's own last language step: comparing
    the string "18990,00" with the string "18990." It seems the model
    doesn't always normalize format before comparing, and sometimes
    treats a difference in notation (the presence of ",00") as a
    substantive discrepancy.

    Comparison with the two-step device: there, this step is deterministic
    code (`abs(a - b) < 0.01` after converting both strings to numbers),
    which never errs on identical numbers — for it, "18990,00" and
    "18990" are always the same value.

    An honest limit on the volume: n=2 errors out of 5 repeats, on one
    resolution, one receipt — a small sample; a 40% rate at `full` could
    be an artifact of these exact five calls, not a stable property of the
    model. The direction of the effect (comparing differently formatted
    strings sometimes fails) is shown cleanly — three reproductions of an
    identical input gave two different outcomes — but the exact rate of
    this failure would need a separate measurement with a bigger n.
---

# Self-contradiction at the sharpest resolution

## Assertion

The amount is read correctly all five times out of five. And still, two times out of five, the verdict is wrong — the model compares its own two numbers and sometimes decides identical numbers are different.

## Visual

| Repeat | Amount read off the photo | Amount from the request | Model's verdict | Correct? |
|---|---|---|---|---|
| 1 | "18990,00" | "18990" | didn't match | **no** |
| 3 | "18990,00" | "18990" | matched | yes |
| 5 | "18990,00" | "18990" | didn't match | **no** |

> **Three live calls, the same photo, the same request — two different outcomes.** The read number is identical across all three repeats. The notation is different: ",00" on one field, none on the other. Substantively, it's the same number. The model decides otherwise two out of three times.

> **Deterministic code doesn't make this kind of mistake.** In the two-step device, this same comparison step is ordinary code that converts both values to a number before comparing: "18990,00" and "18990" are always equal for it. With the single call, the comparison is one more language step by the same model, and it has its own, separate failure rate — 2 out of 5 on these five repeats, with reading fully intact.

## Speaker notes

The previous screen showed where the single call breaks at the heaviest resolution. This one shows that it breaks at the lightest one too — where there's nothing to fault about reading the photo at all.

At full size, the model reads the amount correctly all five times in a row. More than that, in each of the five answers it itself lays out two numbers — the one read off the photo and the one it saw in the request's text — and both times it's the same value, just written differently: once with kopecks and a comma, once without them. Substantively, there's no discrepancy at all.

And yet, on three repeats where the stated amount really matches the true one, the verdict diverges. On the first and fifth repeats, the model declares "didn't match" — wrong, since the numbers do match. On the third repeat — "matched," correct. Three live calls, identical in every condition, on the same photo, with the same request, give two different answers to the question "do these two numbers match?"

It's important not to confuse the cause here. This isn't a reading failure — reading is flawless, five out of five. It's a comparison failure: the last step, where the model sets its own two numbers against each other, turns out to be unreliable on its own, regardless of how well the photo was read. It seems the model doesn't always bring differently formatted records to one form before comparing, and sometimes treats a difference in punctuation as a difference in substance.

In the two-step device, the model doesn't have this step at all. Comparison there is done by code: it takes both values, converts them to a number, compares with a small tolerance. For it, "18990,00" and "18990" are always one and the same thing, and it structurally cannot err on identical numbers — that's a guarantee the check itself provides. Luck on these particular five calls has nothing to do with it.

An honest caveat on this screen: two cases out of five is a small sample, and forty percent here shouldn't be taken as a precise rate for how often the comparison fails in general. But that the failure exists in principle, and doesn't reduce to bad reading — that's shown cleanly, through three reproductions of one and the same input.

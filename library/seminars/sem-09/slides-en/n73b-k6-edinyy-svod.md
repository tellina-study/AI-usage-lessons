---
id: n73b
type: measured_outcome_table
duration_min: 1.5
assertion: "Both devices match on the number of correct verdicts — 25 out of 30. The reasons behind that match are different, and that's already visible at the reading level: the single call's formally more accurate amount rests on two cases of copying the request, not on reading the photo"
learning_goal: "Beat n73b (issue #299, Z3): a summary of the results BEFORE the breakdown by group (C2, item 2) — table 1 from the zamery-k6-edinyy README, both devices side by side, one unit of measurement (C6). Names the final score and announces the breakdown of its causes, without unpacking it fully — findings 1–3 stay for n73c–n73e."
visual:
  pattern: measured_outcome_table
  primary: >
    A "two steps / single call" × "amount correct · date correct · verdict
    correct" table, three columns of numbers for both modes (C6). Below
    it — a card with an honest warning: the single call's formal win on
    the amount (27 against 25) needs a breakdown before counting it as an
    advantage.
  backup: >
    Numbers from `stend/zamery-k6-edinyy/README.md`, section "Results —
    Table 1": two steps (`../zamery-k5-k6/results-k6-resolution.json`,
    compared by deterministic code) — amount 25/30, date 15/30, verdict
    25/30 (= the amount, the code is deterministic, the verdict error
    equals the reading error one for one). Single call
    (`results-k6-edinyy.json`, the model compares itself) — amount 27/30
    (2 of them are copying the request's amount, not reading, see "The
    Anchoring Finding" in the README), date 15/30 (the request carries no
    date text at all in this measurement — the single-call device can't
    influence the date by construction), verdict 25/30.

    "The verdict's final score matched (25 out of 30 in both modes), but
    for different reasons" — the README's core point, carried onto this
    frame explicitly: an identical number MASKS two different failure
    devices, broken down by beats n73c (echo of the request on the
    heaviest resolution) and n73d (self-contradiction on the best
    resolution).

    Date — the same threshold as in reading without a cross-check (n71):
    the request in this measurement carries no date text at all (the
    client at the training center today only types the payment amount as
    text, not the date — the K6 setup), so the single call can't "pull"
    the date toward the request the way it pulls the amount — the date
    simply has no second number nearby to drift toward. This limitation
    is stated honestly on the frame, not glossed over.
---

# Summary: the same final score, different reasons

## Assertion

Both devices converged on the number of correct verdicts — 25 out of 30. But the same number hides different failure devices, and the breakdown by group further on shows this.

## Visual

| Device | Amount correct | Date correct | Cross-check verdict correct |
|---|---|---|---|
| **Two steps** (model reads, code compares) | 25 of 30 | 15 of 30 | 25 of 30 |
| **Single call** (model reads and compares itself) | 27 of 30 | 15 of 30 | 25 of 30 |

> **The amount's formal win needs checking.** With the single call, the amount reads correctly twice as often as with the two-step device — 27 against 25. The breakdown on the next two screens shows: both extra "correct" answers come from the heaviest resolution — the model copied the number straight from the request instead of reading it off the photo.

> **The date doesn't change at all — and that's expected.** The request in this measurement only carries the payment amount; there's no date text in it. The single call simply has nothing to "pull" the date toward a stated value with — it has no second number nearby. The date's threshold holds in exactly the same place as in reading with no cross-check at all.

> **The verdict matches in count, the reasons diverge.** Both devices give 25 correct verdicts out of 30, but that's two different failures under one number: for the two-step code, the verdict error exactly equals the reading error; for the single call, there are its own new failure classes on top of reading.

## Speaker notes

A summary before the breakdown: how the two devices did on the three measured quantities — was the amount read correctly, was the date read correctly, was the final cross-check verdict correct.

The first number looks surprising. With the single call, the amount reads correctly twenty-seven times out of thirty; with the two-step device, twenty-five. Formally, the single call is more accurate. But it's too early to jump to a conclusion: before counting this as an advantage, it's worth looking at exactly where those two extra correct answers came from. The breakdown on the next two screens shows — both come from the heaviest resolution: the model copied the number straight from the request instead of reading it off the photo.

The second number doesn't change between the devices at all — fifteen out of thirty in both cases, the same threshold as in reading with no cross-check at all. This is expected: the request in this measurement only carries the payment amount, the client today doesn't type the date as text. The single call simply has nothing to pull the date toward a stated value with — next to the read date there's no second number it could slip toward. The effect visible with the amount is structurally impossible with the date.

The third number — the final verdict — matches in count between both devices: twenty-five correct decisions out of thirty in each. But this is a match of the count alone — the reasons behind it are different. For the two-step device, the code is deterministic, and its verdict error equals the reading error one for one — wherever reading was wrong, the verdict is wrong, and nothing beyond that. For the single call, the verdict is a separate language step by the same model, and, as we'll see next, it has its own new failure classes that a deterministic code simply can't have.

The same number, twenty-five out of thirty, on this frame is an invitation to the breakdown — the end of the story is still ahead. The next two screens show why the masking is more dangerous than it looks at first glance.

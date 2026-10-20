---
id: n32
type: answer_breakdown_table
duration_min: 2.0
assertion: "On 101 requests version 1 erred 9 times, and all nine were on the amount exactly equal to the threshold; version 2 — 0 errors on the same set; this is a systematic error at one point, not random scatter"
learning_goal: "The experiment's result rebuilt into block form at the owner's direct request: each test block gets its own row with its own count of requests and errors, instead of running prose."
visual:
  pattern: answer_breakdown_table
  primary: >
    A block table across six test groups with the number of requests,
    errors, and a real example request text in each, with a totals row at
    the bottom. No execution id — only the observed behavior.
  backup: >
    The six block labels name the content of each group (range / phrasing
    feature), not a production history of "original" vs. "new" — all six
    are equal parts of one 101-request test from the student's point of
    view. The example column uses real request text from the data files,
    never invented; for the single manual test the text is honestly not
    shown, because it was never recorded as data. Mirrors RU n32 (issue
    #274).
---

# Result: 9 errors out of 101, all nine at one point

## Assertion

Version 1 erred nine times out of a hundred and one runs — and all nine times on the very same amount: exactly at the threshold. Version 2 — zero errors on the same set.

## Visual

| Test block | Requests | Errors v.1 | Errors v.2 | Example request |
|---|---|---|---|---|
| At or below the boundary (1,000–3,000 RUB) | 25 | **3** (= 3,000 RUB) | 0 | "can I get a refund of 3,000 rubles for one missed class?" |
| Clearly above (3,200–9,000 RUB) | 25 | 0 | 0 | "a refund of 3,200 rubles, or I'll file a complaint" |
| Manual test | 1 | 0 | 0 | text not recorded as data |
| Right at the boundary (±20 RUB from 3,000) | 15 | 0 | 0 | "please refund 2,999 rubles, the class was cancelled at the last moment" |
| Two numbers in one text | 20 | 0 | 0 | "the course cost 12,000 rubles, I want a refund of 2,400 rubles for one block" |
| Indirect phrasing (arithmetic/"about") | 15 | **6** (= 3,000 RUB) | 0 | "the class cost 1,500 rubles, please refund me for two such classes" |
| **Total** | **101** | **9** | **0** | |

> **What the model decided at the boundary.** At an amount of exactly 3,000 rubles — in any phrasing, direct or arithmetic — version 1's model answered "escalate," even though the rule ("don't refund more than 3,000 rubles") implies that the boundary itself is "okay to approve." All 9 errors without exception are on this one amount; not a single error happened at 2,999 rubles, nor at 3,001, nor anywhere else in the range.

## Speaker notes

Here is the result of the measurement on the extended set. A hundred and one runs, and version one has nine errors.

The table is broken down by test block not for looks, but because this way you can see right away where the error is and where it isn't. The original boundary cluster — twenty-five requests, three errors. The original amounts clearly above the threshold — twenty-five requests, zero errors. The new block right at the boundary, where amounts sit even closer to three thousand — fifteen requests, and surprisingly zero errors: neither 2,980, nor 2,999, nor 3,001, nor 3,020 threw the model off, because none of them matches the threshold EXACTLY. The block with two numbers in the text — twenty requests, also zero: the model confidently tells the distracting amount apart from the target one. And then the block of indirect phrasings — fifteen requests, with six new errors in it, and all six where the arithmetic inside the text ("half of six thousand," "three classes at a thousand each") comes out to exactly three thousand.

This is the main thing the extended set confirms: the error isn't smeared across the range and doesn't depend on how complicated the phrasing is. It is tied to ONE EXACT AMOUNT — three thousand rubles — regardless of whether that amount arrives as a direct number or as arithmetic from two numbers. The model handles "obviously a lot," "obviously a little," and even amounts within twenty rubles of the boundary — flawlessly, in every case without exception. The miss happens only where the amount literally equals the threshold.

And this is not a random error that occasionally slips through anywhere. It is a systematic error sitting at one specific point — where the rule's text and its formal interpretation diverge. Everywhere else in the range, no matter how close to the boundary, the model is flawless.

The difference between "a random mistake" and "a systematic mistake right at the boundary" is exactly what the solution we already showed on the diagram eliminates structurally: the `IF` node changes the very point where the decision is made, rather than lowering how often it errs there. Next — what this node looks like in the real setup, next to the version-1 prompt for contrast.

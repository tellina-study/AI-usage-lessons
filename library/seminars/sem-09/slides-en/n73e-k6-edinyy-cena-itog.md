---
id: n73e
type: measured_outcome_table
duration_min: 1.5
assertion: "Merging the steps doesn't save a call — the second step in the real device was already free code; the single call costs 34–118% more depending on resolution and adds two new failure classes on top of reading, one of them dangerous — the measurement's conclusion: leave the cross-check to code"
learning_goal: "Beat n73e (issue #299, Z3): closing the breakdown by group (C2) — Finding 3 of the zamery-k6-edinyy README (cost) plus the measurement's final conclusion. Closes the exposition opened by n73a, with a number on every point: accuracy is the same, cost is higher, two new failures."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of call price across the six resolutions, two modes side by
    side, a growth-percentage column (C6). Below it — a closing card,
    "measurement's conclusion," in four lines: reading accuracy didn't
    change, the single call's cross-check is worse at both ends of the
    resolution range, the call isn't cheaper, the final recommendation —
    leave the cross-check to code.
  backup: >
    Numbers from `stend/zamery-k6-edinyy/README.md`, sections "Finding 3"
    and "Conclusions": price by resolution — full $0.003803→$0.005089
    (+33.8%), halved $0.001192→$0.001835 (+53.9%), quartered
    $0.000516→$0.000965 (+87.1%), eighth $0.000383→$0.000754 (+96.9%),
    sixteenth $0.000383→$0.000837 (+118.3%), thirty-second
    $0.000372→$0.000722 (+94.1%). Total across 30 calls: $0.006649 →
    $0.010201, a 53.4% increase. Tokens: the baseline averages 1,050 per
    call, the single call — 1,273 (+21%, less growth than the price —
    most of the added tokens are cheap request text, not the expensive
    tokens of the picture itself).

    The intuition "one call instead of two is cheaper" doesn't apply
    literally here: in the rig's REAL two-step device, the second "step"
    isn't a model call at all, it's deterministic code (comparing
    numbers), which costs zero tokens. Merging into one call doesn't
    remove a second model-dependent operation (there wasn't one) — it
    adds the request's text and two new fields to the single call's
    output JSON, that is, it only increases the price.

    The README's final conclusion (section "Conclusions," items 1–4),
    verbatim in substance: reading accuracy didn't change (the
    degradation thresholds are identical, digit for digit, in both
    modes); the single call is worse exactly where it's most expensive —
    in the cross-check itself (Findings 1–2, this beat doesn't repeat
    them, only references them); merging doesn't save a call (Finding 3
    above); for the task of cross-checking a payment amount, leave the
    cross-check to deterministic code after a separate reading call — the
    measurement's conclusion, not a guess.

    SETKA-KEYSOV-S9-part2.md, Case 6, Nuance 6 carries the same conclusion
    for the case's canonical text — this beat reveals it with a number on
    the frame, not repeating it for the first time.
---

# Cost and conclusion: what merging actually buys

## Assertion

Merging the steps costs more at all six resolutions — from 34% to 118%, depending on file size. The second step in the real device was already free code: there was nothing to save by merging.

## Visual

| File size | Price: two steps | Price: single call | Growth |
|---|---|---|---|
| original | $0.003803 | $0.005089 | +33.8% |
| half | $0.001192 | $0.001835 | +53.9% |
| quarter | $0.000516 | $0.000965 | +87.1% |
| eighth | $0.000383 | $0.000754 | +96.9% |
| sixteenth | $0.000383 | $0.000837 | +118.3% |
| thirty-second | $0.000372 | $0.000722 | +94.1% |
| **Total, 30 calls** | **$0.006649** | **$0.010201** | **+53.4%** |

> **The measurement's conclusion.** Reading accuracy is the same in both modes, the degradation thresholds match digit for digit. The single call's cross-check breaks exactly where it's most expensive: a dangerous confirmation at the heaviest resolution (broken down last screen) and self-contradiction at the sharpest one (the screen before that). The price is higher by 34–118% depending on resolution, 53% on average. Conclusion: leave the cross-check of a payment amount to deterministic code, after a separate reading call.

## Speaker notes

The last piece of this breakdown is cost. It closes the picture: there's no new argument here in favor of merging.

The intuition "one call should be cheaper than two" doesn't work here, and the reason is simple: in the rig's real device, there was never a second model call. The cross-check was done by code — comparing two numbers, which costs exactly zero tokens. Merging into one request doesn't remove a second model-dependent operation, because there wasn't one — it simply adds the request's extra text and two new fields to the one existing call's response. The result is visible in the table: the price grows at all six resolutions, from thirty-four percent on the largest file to as much as a hundred eighteen on one of the middle ones. Averaged across all thirty calls — a fifty-three percent increase.

Add this to what the two previous screens showed. Reading accuracy didn't change — the thresholds past which the amount and the date break match digit for digit in both modes. And the single call's cross-check breaks exactly where it's most expensive: at the heaviest resolution — a dangerous confirmation of a wrong request instead of a safe failure; at the sharpest one — self-contradiction with flawless reading.

The single call has not one measured advantage on this measurement. Reading accuracy is the same. The price is higher. And there are two new failure classes on top of reading, one of them genuinely dangerous — that's not just an inconvenience. For this specific task — cross-checking a payment amount against a request — the measurement's conclusion is direct: leave the cross-check to deterministic code after a separate reading call, exactly the way it's built on n68. This is a measured conclusion — the measurement specifically checked the opposite direction and found that it costs more and fails more dangerously; it was never the default preference.

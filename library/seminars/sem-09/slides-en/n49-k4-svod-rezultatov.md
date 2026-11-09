---
id: n49
type: measured_outcome_table
duration_min: 1.5
assertion: "The best result — 53 correct decisions out of 64 — is reached by two configurations at once: the 'prompt+mechanical check' pair and all three defenses together, same number, different cost"
learning_goal: "Beat 2 of the measurement's exposition (C2): a summary across all eight configurations, the same names and order as n48a. Metrics are comparable (C6) — one column, one dimension to compare on."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of eight configurations (same order as n48a) with four
    numeric columns: correct decisions, false refunds on attacks, false
    alarms on honest requests, model calls. Row `pr` and `prc` highlighted
    as best by correct decisions.
  backup: >
    Numbers — verbatim, Table 1, `stend/zamery-k4-novyy/README.md`. The
    columns are picked from the full table (it has seven there) under
    rule C6: four metrics of a consistent dimension, enough for the
    beat's carrying conclusion, the detailed classes are on the next
    frame (n49a).

    "Correct decisions" = 64 minus (false refunds + false alarms) —
    reconciles arithmetically row by row, not a separate measurement.

    "False refunds on attacks" is out of the 34 requests of Classes D+E
    (manipulation); "false alarms" is out of the 12 requests of Class A
    (an honest client inside the window who wasn't given the refund
    they're owed).
---

# Summary: eight configurations on one corpus

## Assertion

The "prompt+mechanical check" pair and the "all three together" triple give the same best result — 53 correct decisions out of 64. The third defense adds nothing to the pair except cost.

## Visual

| Configuration | Correct out of 64 | False refunds on attacks (of 34) | False alarms (of 12) | Model calls |
|---|---|---|---|---|
| `0` — no defense | 45 | 7 | 6 | 64 |
| `p` — prompt | 51 | 3 | 8 | 64 |
| `r` — mechanical check | 52 | 0 | 6 | 33 |
| `c` — classifier | 47 | 5 | 6 | 123 |
| `pr` — prompt+mechanical check | **53** | **0** | 9 | 33 |
| `pc` — prompt+classifier | 52 | 2 | 8 | 120 |
| `rc` — mechanical check+classifier | 52 | 0 | 6 | 65 |
| `prc` — all three | **53** | **0** | 9 | 65 |

> **Even with no defense at all, the deciding model fended off 27 attacks out of 34 on its own.** A naive prompt is weaker than a reinforced one, but it wasn't helpless.

## Speaker notes

Let's check the prediction from the last frame. If you bet on the mechanical check — you're right: it's the one that alone stops the most attacks. If you bet on the classifier — it has the weakest result of the three, we'll see why a bit further on.

Eight configurations, the same 64 requests, and here's what came out of each one — all in the same dimension, so the rows can be compared honestly.

Let's start with the baseline, the configuration with no defense at all. 45 correct decisions out of 64, 7 false refunds specifically on attacks, and 6 false alarms on honest clients. Worth noting right away something that's easy to miss: even with no defense whatsoever, the deciding model stopped 27 attacks out of 34 on its own — its prompt isn't as naive as it looks, it's simply weaker than a reinforced one.

Each defense on its own improves on the baseline, but differently. The prompt raises correct decisions to 51, lowers false refunds on attacks to 3, but pays for it with more false alarms — from 6 to 8. The mechanical check gives 52 correct and zeroes out false refunds on attacks entirely, while also removing nearly half the model's calls — 33 instead of 64. The classifier alone is the weakest of the three: 47 correct, and the only defense that at the same time nearly doubles the number of model calls.

Now the pairs. Prompt plus mechanical check give the best result in the whole table — 53 correct decisions out of 64, and zero false refunds on attacks. The other two pairs are noticeably worse: prompt with classifier — 52 correct, mechanical check with classifier — also 52.

And here's this summary's main observation. Adding the classifier to the best pair — the "all three together" configuration — gives exactly the same 53 correct decisions as the pair without it. Not one number changed, except the cost: model calls went up to 65 instead of 33, nearly twice as many. In this measurement, the third defense added nothing to the result, only to the bill.

This summary isn't the whole breakdown yet. Next we'll look at exactly which request classes each configuration holds up on and breaks down on, and then — where the errors that remain even with the best defense actually come from.

---
id: n40
type: measured_outcome_table
duration_min: 1.0
assertion: "Code costs 1.0 model call per question at 100% accuracy, the judge 2.8 at 90%, the combination 4.0 at 85%, the mixture of experts also 4.0 — but for a different reason: not a retry loop, but a fixed parallel of three experts plus a decider"
learning_goal: "The checker's cost, named RIGHT NEXT TO its accuracy and its model (C5+C6, owner edit 2026-10-29 — 'the cost is missing accuracy, and the model — both in the implementation description and in the results'), not apart from it. Row five is the mixture of experts (Z4)."
visual:
  pattern: measured_outcome_table
  primary: >
    A table of five builds (no loop, code, judge, combination, mixture of
    experts): model, attempts/calls, calls per question, accuracy, cost.
    Below it, a banner on where the cost comes from, and a banner noting
    that the mixture of experts' cheapness doesn't match its reliability.
  backup: >
    Numbers — `stend/zamery-k1-k3/README.md`, § "Measurement 4 — Case 3,
    full 20×3 measurement": code/judge/combination each measured on 20
    questions (executions 969–1031, `raw/zamer3-full-20.json`). The "no
    loop" row STAYS on the original 6 questions (executions 767–772) — it
    wasn't part of the 20×3 extension, and the table says so openly rather
    than hiding it. The "mixture of experts" row — `stend/zamery-k3-smes/README.md`,
    section "Lenient check → updated deck fixes" (the CURRENT version, the
    literal 14/20 is retracted).

    THE MODEL IS NAMED EXPLICITLY (C5): every build except code uses
    `qwen/qwen-2.5-7b-instruct`; code isn't a model, it's deterministic
    JavaScript (`Code check`, see n35), and that's explicitly marked "—,"
    not a blank dash with no explanation. The mixture of experts uses three
    DIFFERENT models (`qwen/qwen-2.5-7b-instruct`,
    `meta-llama/llama-3.1-8b-instruct`, `mistralai/ministral-8b-2512`) plus
    a decider on a fourth call to the same `qwen/qwen-2.5-7b-instruct` that
    plays the judge in the other rows — the decider-judge identity is
    named outright, so the difference in numbers doesn't read as a
    difference in models.

    ACCURACY IS NAMED EXPLICITLY (C6): "converged/20" for code/judge/combination
    — the same numbers as on n39/n40a; for the mixture of experts — 20/20
    under the LENIENT check (fixed for fragility to Russian morphology),
    noted that the literal (unhelpful) version of the check gave 14/20 —
    this is a finding about the check, not about the decider, see n32 and
    the report.

    COST — by OpenRouter's price list for `qwen/qwen-2.5-7b-instruct`, read
    directly from `GET https://openrouter.ai/api/v1/models` with no
    authorization, on 2026-10-27 (code/judge/combination) and 2026-10-29
    (mixture of experts): $0.0000001/input token, $0.0000002/output token
    for qwen (the mixture's experts have their own models at their own
    prices; the total cost already accounts for that). This is the price
    list on the date of measurement, not an account billing statement.

    WHY THE MIXTURE OF EXPERTS' COST IS NEARLY EQUAL TO THE COMBINATION'S,
    WHILE RELIABILITY DIFFERS: both cost 4.0 calls per question, but the
    combination reaches that number through a LOOP (retrying on
    disagreement), while the mixture of experts is ALWAYS EXACTLY 4.0 — a
    question is never cheaper or more expensive than its own difficulty.
    Predictable cost is the mixture of experts' only real win, and it does
    not mean it's more reliable: its 100% on this check rests on 50%
    stability to option order (n32), not on an independent quality
    assessment of each expert.
---

# What each checker costs

## Assertion

Code — 1.0 call per question at 100% accuracy. Judge — 2.8 at 90%. Combination — 4.0 at 85%. Mixture of experts — also 4.0, but with no loop and no retrying.

## Visual

| Build | Model | Calls/question | Accuracy | Cost (20 questions) |
|---|---|---|---|---|
| no loop, baseline (6 questions) | qwen/qwen-2.5-7b-instruct | 1.0 | 100% (6/6) | — |
| code check | — (deterministic JavaScript) | 1.0 | 100% (20/20) | $0.0007 |
| judge model | qwen/qwen-2.5-7b-instruct | 2.8 | 90% (18/20) | $0.0031 |
| code+judge combination (strict) | qwen/qwen-2.5-7b-instruct | 4.0 | 85% (17/20) | $0.0047 |
| mixture of experts | 3 experts + qwen decider | 4.0 (fixed, no loop) | 100% (20/20, lenient check) | $0.0042 |

> **Where the code/judge/combination gap comes from.** It compounds twice: on every attempt (the judge spends two calls instead of one) and on the number of attempts (a false rejection sends the answer around for another loop). The combination catches both multipliers at once — hence 4.0 against 2.8.

> **Why the mixture of experts lands on the same 4.0, for a different reason.** The combination reaches 4.0 through a retry loop; the mixture of experts always costs exactly 4.0, a question never cheaper or pricier than its own complexity. Predictable cost is its only real win; the 100% accuracy here rests on the decider's 50% stability to option order — independent quality assessment has nothing to do with it.

## Speaker notes

The cost compounds again where it doesn't look like it would — and now, for the first time, it comes with a dollar figure and an accuracy column right next to it, not just a ratio of calls.

Code — one model call per attempt, and on twenty questions every attempt was the first one: twenty calls, one to one, and a hundred percent accuracy on top of that. The judge — two calls per attempt, and not every attempt was the first: twenty-eight attempts, fifty-six calls, two point eight per question — and accuracy is already down to ninety percent, not a hundred. The combination — also two calls per attempt, but even more attempts pile up, because agreement is needed from both: forty attempts, eighty calls, four per question, accuracy down to eighty-five.

Row four is the mixture of experts, and its arithmetic is different: three small models generate in parallel, a fourth picks — always four calls, no loop, no retry at all. The cost nearly matches the combination's. But here's what's misleading: the formal accuracy here is a hundred percent — better than the judge and the combination. That hundred doesn't mean the decider genuinely judges by quality: the neighboring frame measured that when the options are reshuffled, the decider changes its pick half the time. Cheap and predictable cost doesn't protect against the choice itself depending on position, not content.

Notice the general arithmetic: the gap grows with each additional checker by multiplication, not addition, and accuracy drops exactly when a retry loop driven by a model's opinion enters the picture — the judge and the combination. The mixture of experts has no loop at all, so its cost grows predictably — but that's a property of the cost, not proof of reliability.

---
id: n40a
type: measured_outcome_table
duration_min: 2.0
assertion: "On the full run of 20 questions, the strict combination 'code AND judge' converges in 17 cases out of 20 (85%) — less often than code alone (100%) or the judge alone (90%), and in all three non-converging cases code agreed on the first attempt, while the judge never agreed once across 6 attempts"
learning_goal: "Updated 2026-10-27 — a full 20×3 measurement instead of the original 3 questions. The same finding (the judge chokes code in the strict combination), but now on a sample that can carry a count: not a single example, but 3 of 20 with one and the same rejection mechanism."
visual:
  pattern: measured_outcome_table
  primary: >
    A strip of three banners (converged/not converged/average attempts)
    with the load-bearing number 17 of 20, below it a table of the three
    non-converging questions (question · code · judge · does n38's
    self-contradiction reproduce), below that a quote of one of the
    judge's rejection reasons, verbatim, contradicting itself.
  backup: >
    All numbers — `stend/zamery-k1-k3/README.md`, § "Measurement 4 — Case
    3, full 20×3 measurement," the subsection on the combination. Source —
    `raw/zamer3-full-20.json` (`variants.combo`), executions 1009–1031,
    `run_zamer3_full20.py`.

    WHAT CHANGED FROM THE PREVIOUS VERSION OF THE FRAME (3 questions,
    executions 943-945): the direction of the finding is the same, the
    severity is different. On 3 questions, 1 of 3 (33%) failed to
    converge; on 20, it's 3 of 20 (15%), almost half as often
    proportionally. The frame honestly shows BOTH numbers as the
    measurement's own evolution, not presenting the new one as the only
    true one.

    THE MECHANISM IS IDENTICAL ON ALL THREE non-converging questions,
    without exception: code says "ok" on EVERY one of the 6 attempts, the
    judge never agrees ONCE. In 2 of 3 cases, the judge, in the process,
    quotes a positive sentence ("Explicitly mentions the detail...") as the
    reason for a REJECTION — the same self-contradiction as on n38, now on
    new questions (kb2, kb5), not a one-off artifact.

    The combination's dollar cost is named separately on n40 (the fourth
    row of the "What each checker costs" table) — it isn't repeated here,
    to avoid doubling the same point.
---

# What happens when you cross code and the judge

## Assertion

On 20 questions, the strict combination "code AND judge" converges in 17 cases out of 20. In all three that didn't converge, code agreed right away — the judge never agreed once across 6 attempts.

## Visual

> **Converged: 17 of 20 (85%)** · **Not converged (6-attempt limit): 3 of 20 (15%)** · **Average number of attempts: 2.0**

> **In human terms.** "Converged" means the requester got an answer. "Not converged" means that after six attempts there's still no answer, and the question goes to Olga: a controlled stop at a known limit, planned in advance.

| Question | Code across all 6 attempts | Judge across all 6 attempts | Same self-contradiction as before? |
|---|---|---|---|
| "...there's very little time left before class starts, can I reschedule?" | ok | not ok | **yes** — 3 of 6 reasons: "2. Explicitly mentions the detail '24 hours.'" |
| "How do I get into a retake for a class...?" | ok | not ok | **yes** — attempts alternate between "doesn't mention" and "explicitly mentions" about the SAME detail |
| "...I didn't give notice — can I retake for free?" | ok | not ok | no — the reasons are unsupported ("repetitive"), but they don't contradict each other |

> **Verbatim, the rejection reason for attempt 4 (the retake question).** "2. Explicitly mentions the detail 'the second Saturday.'" — a positive sentence, delivered as a reason for REJECTION. Two attempts later, the same detail in a similar text gets the opposite reason: "doesn't explicitly mention."

> **This isn't a one-off.** The self-contradiction "a positive sentence as a rejection reason" is reproduced on 2 of the 3 non-converging questions in this measurement — on different knowledge-base items, from different answer generations.

## Speaker notes

This is an updated frame — the combination used to be measured on three questions, now it's measured on twenty, the same ones code and the judge each went through separately.

The number that converged is seventeen of twenty, eighty-five percent. Before, on three questions, one hit the limit — a third. Now it's three of twenty — fifteen percent, almost half as often. I'm naming both numbers: the finding hasn't disappeared, it's become less dramatic on a bigger sample, and that too is an honest measurement result, not a reason to be embarrassed by the first version of the frame.

What matters most is that the mechanism is the same on all three non-converging cases, no exceptions. Code says "ok" on every one of the six attempts. The judge never agrees, not once. Code isn't the one flip-flopping — code is stable. It's the judge that never confirms what code has already accepted.

And in two of the three cases — it's the same self-contradiction we saw before on a single example, not just the judge's stubbornness. The judge names, as the rejection reason, a sentence that on its own sounds like approval: "explicitly mentions the detail" — and this is written as the REJECTION reason. On a neighboring attempt, the same judge writes the opposite about the same detail — "doesn't mention." There's no reliable criterion here at all.

The six-attempt limit did its job just as routinely as before — the question went to a forced stop, otherwise it would have spun forever. This is still not the judge deciding to stop — it has no mechanism for that. It was the process that stopped, because it knew its limit in advance.

Worth saying outright why the combination was built this way. Code and judge were joined by the rule "both agree" — a logical AND, the strictest option available. A softer option was possible: "at least one agrees," a logical OR. That would have meant fewer rejections — but also less protection: an answer would go out to the client even when one of the two checkers objected. The strict version sacrifices some availability to make sure no disputed case slips through quietly: disagreement from even one checker is exactly the non-converging case we just broke down on three questions.

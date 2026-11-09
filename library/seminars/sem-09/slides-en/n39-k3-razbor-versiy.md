---
id: n39
type: answer_breakdown_table
duration_min: 1.5
assertion: "On the full 20×3 measurement, code erred 0 times out of 20, the judge 19 times out of 20 with invented reasons; independent of that, code and judge also diverge as standalone checkers in a live loop: 28 attempts for the judge versus 20 for code on the same 20 questions"
learning_goal: "Breakdown of the versions AFTER the test (case-design canon §4), updated to 20×3 from the original 6. Both versions are compared on the run that found the problem; code's own mistake (zero, in this run) is stated honestly, not hidden for the sake of symmetry."
visual:
  pattern: answer_breakdown_table
  primary: >
    A two-column table, "the model checks" and "code checks," five
    comparison rows on the same run. Below the table, a banner of external
    measurements and a banner noting that code didn't make a single
    mistake on this run (not symmetric with the earlier version of the
    frame, stated outright).
  backup: >
    Our own numbers — `stend/zamery-k1-k3/README.md`, § "Measurement 4":
    judge-check (`raw/zamer3-judgecheck-20.json`, 20 questions) for rows
    1-3, independent loops `s9-m3-code`/`s9-m3-judge`
    (`raw/zamer3-full-20.json`, executions 969–1008) for row 5.

    CODE'S ONLY REJECTION WAS ON THE EARLIER SAMPLE (6 questions), NOT ON
    THIS ONE. On 20 questions, code converged on the first attempt on all
    twenty — zero rejections. The historical finding (a grammatical case in
    kb5) remains in the README as already fixed (regex, 6 of 6 on the
    2026-10-26 re-measurement) — it isn't repeated here as a "current"
    example, because THIS run simply has no material to show it with. Row
    2's asymmetry (code 0 false, model 19 false) is an honest result of
    this run, not tuning the table to look fair.

    The columns are named "the model checks" and "code checks," same as
    before — again the independent loops `s9-m3-judge`/`s9-m3-code`, not
    versions.
---

# Two checkers on one run

## Assertion

Code was wrong 0 times out of 20. The judge was wrong 19 times out of 20, and the reasons were invented.

## Visual

| What we're comparing | The model checks | Code checks |
|---|---|---|
| Verdict on the first 20 answers | rejected 19 | accepted 20, rejected 0 |
| How many verdicts turned out false | **19 of 20 (95%)** | **0 of 20 (0%)** |
| Where the rejection reason comes from | arrives as text from the model; in this run disproved 19 times by the answer itself, including a new class — a legitimate number called a violation | a line written in advance and sitting in the code |
| Verdict repeatability | a byte-for-byte identical text got "no," then "yes," on two attempts in a row | the same text gets the same verdict as many times as you run it |
| Attempts spent (independent loops) | 28 attempts on 20 questions | 20 attempts on 20 questions |

> **Honestly about the asymmetry.** On the earlier sample (6 questions) code also erred once — a grammatical case on kb5, already fixed and re-measured at 6 of 6. On THIS sample (20 questions) code made no mistake at all — there's nothing to balance the table with a code-rejection example, and the frame doesn't hide that.

> **The same ratio, measured externally, on different tasks.** Self-review with no external criterion: **95.5% right away, 91.5% after one retry round, 89.0% after two** (Huang et al.). A judge and option order: swap a pair's positions, and a strong model keeps its verdict **65.0% of the time**, a weak one **23.8%** (Zheng et al.).

## Speaker notes

Let's break down both builds on the full run — twenty questions instead of the earlier six.

First row. Code accepted all twenty first answers, the judge returned nineteen out of twenty. Second row — the same picture as a share of false verdicts: ninety-five percent for the judge, zero for code.

And here's the honest moment. On the earlier, small sample, code also made one mistake — remember, a grammatical case in the word for "Saturday," fixed since then. On this larger sample, code made no mistake at all. I'm not inventing a symmetric example to make the table look fairer to both sides — I'm naming what was measured: on this specific run, there's simply no material for a code rejection.

Row three, on where the rejection reason comes from — unchanged in substance, but a new error class was added: the judge rejected the legitimate number eighteen as "a number not in the base," even though it's a number from the base itself. Row four — repeatability, and here we now have a stronger example than before: a byte-for-byte identical text got opposite verdicts back to back, with not a single character changed.

Row five — the number of attempts in independent loops, where each checker works on its own, with no peeking at the other's verdict: twenty-eight for the judge versus twenty for code, on the same twenty questions.

And the same ratio, measured on other tasks by other people, hasn't gone anywhere: self-review with no external criterion sits around ninety percent and drops with every round of retrying; a judge whose pair gets swapped changes its decision noticeably more often than you'd want to trust. Our expanded run didn't uncover a new phenomenon — it confirmed the same one on a sample four times as large.

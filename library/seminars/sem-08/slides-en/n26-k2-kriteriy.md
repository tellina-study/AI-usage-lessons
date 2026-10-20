---
id: n26
type: criteria_checklist_and_boundary
duration_min: 2.5
assertion: "Exact match is enough for literal repeats, for free; the classic vector approach doesn't give a guaranteed improvement over it in Russian; a model is needed where rephrasings are expected, and its error rate is a cost, not zero"
learning_goal: "Case 2's criterion on measured numbers, plus closing the session axis's second row. A line on choosing the specific meaning-check tool was added (2026-10-20 voice edit) — jev named explicitly as an option, not just a row in the n20 measurement table."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A two-column criterion, with a closing-the-axis-row banner below it.
  backup: >
    The criterion text and the axis-row closing wording are from
    SETKA-KEYSOV-S8.md, Case 2, section "Criterion", carried over nearly
    unchanged: a line was added about choosing between a general-purpose
    model and a specialized service (jev) as a separate decision inside
    "the meaning check", the character is Olga instead of Svetlana (canon
    §A13), the client's name ("Boris") is kept only in the notes as the
    measurement methodology's pair, not on the visible layer — per the
    2026-10-20 voice edit, issue #274.
---

# When Exact Match Is Enough

## Assertion

What decides isn't "which tool is better in principle" but what kind of repeats you expect and what you have to pay for each tool's mistakes — a measured price, not an assumed one.

## Visual

| Exact match **is enough** | Meaning check **is needed on top** |
|---|---|
| repeats are mostly literal, like Boris's first question | rephrasings are expected, like his second question |
| you need a free, instant filter on the whole request stream | the cost of a missed duplicate is higher than the cost of one model call on the borderline cases |
| the classic vector approach isn't worth adding "just in case" — the measurement showed a result WORSE than hash, not the same | the frequency of the model's own errors is a measured cost (3 false positives out of 20 for us), not zero, and it has to be budgeted for too |
| — | neither hash nor the classic vector approach solves rephrasing in Russian on their own, in full |
| — | the specific meaning-check tool is also a choice: a cheap general-purpose model (17/20 on our test) or the specialized service jev (20/20) — not something to guess by default, it needs its own check |

> **Closes the axis's row.** It looked reliable: a request about the same question came in again — handled as new. What it turned out to be: without a duplicate check, every repeat request restarts the chain from scratch; neither hash nor the classic vector approach solves this entirely for live Russian text — a model is needed, with its own, measured price for being wrong.

## Speaker notes

A criterion, and it's not about which tool is better in principle — all three work; the question is what kind of repeats you expect and what you're willing to pay for each one's mistakes.

Exact match is enough for literal repeats — on our set that's 75 percent, 15 out of 20, for free and instantly. This is Boris's first question, asked twice in exactly the same words — for a case like that, hash handles it completely, and spending a model call on every single request doesn't pay off.

The classic vector approach isn't worth adding "just in case", counting on the similarity measure and a tunable threshold to deliver an improvement on their own. The measurement on 20 real pairs showed a result WORSE than hash — 13 out of 20 against 15: you can't treat it as a "smarter hash" without checking it on your own data — it can turn out worse than the simplest option.

A meaning check is needed on top exactly where rephrasings are expected — Boris's second question, asked in different words. The model is needed there, and it's important to remember: its own error rate — three false positives out of twenty for us, fifteen percent — is the price you pay for that accuracy, not zero. If the cost of a missed duplicate — the administrator's repeated work, a repeat call, the client's distrust like what Boris got — is higher than the cost of one extra model call on borderline cases, the meaning check earns its keep.

And a separate line in the criterion: which specific model to check meaning with is also a decision, not obvious by default. On our test, the cheap general-purpose model scored 17 out of 20, the specialized service jev scored 20 out of 20 and costs less by pricing. This doesn't mean "always take the specialized service": it means the choice of tool for this step is worth checking the same way we checked whether the step is needed at all — not guessed.

And now let's close the second row of our table. It looked reliable: a request about the same question came in again — formally that's just a new request, handled as new, a green run. What it turned out to be: without a duplicate check, every repeat request restarts the whole chain from scratch, as if the question had never been asked — exactly what happened with Olga and Boris. And this is the thing worth carrying forward: neither exact match nor the classic vector approach solve this task entirely on their own — a real rephrasing needs a meaning check, with its own measured, not imagined, price for being wrong, and that's exactly why in the final solution it stands as the second step, not the only one.

The case is closed: we went from Olga's need and her client's, through two unsuccessful or incomplete cheap approaches, an honest measurement on real texts, and choosing the right order of tools — to a concrete criterion for deciding whether the second, expensive layer is even needed at all, and with exactly which tool to build it. Next is this session's third case, and there the same fork between model and code will show up not in request text, but in a decision that directly controls money.

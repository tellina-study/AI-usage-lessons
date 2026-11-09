---
id: n60a
type: measured_outcome_table
duration_min: 2.0
assertion: "A description of the boundary in the prompt fully cleaned up the persistent error — 10 out of 10 correct, and adding few-shot on top adds nothing to that result. On the case's second question, the same combination gave 5 out of 10 — less than description alone (6 out of 10), but at one run out of ten that's not a proven regression"
learning_goal: "Owner's 2026-10-27 edit (methodology in large blocks) plus the 2026-10-29 edit (Z5, K5-7): the owner separately pointed out that only single techniques had been checked so far, and the missing third variant was the combination of few-shot and description in one prompt. The table's third row and the second text block were added by the exact list of addresses in `stend/zamery-k5-povtorno/README-fewshot-desc.md`, section 'Deck edits'. The case's conclusion on the frame: the techniques don't add up — on neither of the two questions did the combination beat description alone."
visual:
  pattern: measured_outcome_table
  primary: >
    Methodology as large badge blocks in a row (temperature · model ·
    question · repeats), with a three-row table below — few-shot ·
    description · combination — with an explicit "correct/incorrect"
    label on every number. Below that, a second text block: the same
    three techniques on the case's second question (the retake self-
    contradiction), with the same labeling rule, and a closing conclusion
    — "the techniques don't add up" — with a caveat about the unproven
    regression.
  backup: >
    Scenario 1's numbers (the boundary question) —
    `stend/zamery-k5-povtorno/README-fewshot-desc.md`, executions 946–965
    (few-shot/description separately) and executions 1809–1818
    (combination). Scenario 2's numbers (the retake self-contradiction) —
    executions 1055–1074 (separately) and 1819–1828 (combination). Case
    2's generic harness (`s9-k2-experiment`), the same model
    `qwen/qwen-2.5-7b-instruct`, T=0, 10 repeats per variant on each
    question.

    THE THIRD ROW AND SECOND BLOCK — per the exact list of edits at the
    end of README-fewshot-desc.md ("Deck edits — exact list of
    addresses"), items 1–4, carried out verbatim: the assertion was
    extended with a third outcome, the table got a combination row, the
    "Why this isn't obvious" block got a sentence about the ceiling, and
    the notes' last paragraph was rewritten with a third point.

    THE NUMBERS ARE A MANUAL CHECK, NOT AN AUTOMATIC GRADER. On both
    scenarios, the automatic grader (`grade_q1`/`grade_q2`, taken
    unchanged from the single-technique measurements) disagreed with a
    line-by-line reading of every answer: scenario 1 gave 9 out of 10 by
    the grader against 10 out of 10 by reading (execution 1816 — the
    grader caught the word "manager" inside "and not through the
    manager," missing the negation in front of it); scenario 2 gave 4 out
    of 10 by the grader against 5 out of 10 by reading (executions 1819,
    1821, 1822 — the grader failed to recognize an unfamiliar phrasing of
    the caveat). ORCHESTRATOR'S DECISION: only the numbers AFTER the
    manual check go on the frame and into the notes — these are the
    measurement's own numbers, not the method used to count them. The
    grader's disagreement with the reading is a finding about the
    reliability of our own script (canon §8.6, the same finding for the
    third time in this measurement folder), not about the model's
    behavior on the client's question; the student doesn't need it for
    the case's conclusion, and it doesn't go on the frame — its place is
    here, in the backup, and in the measurement's own README, for
    traceability.

    WHY SCENARIO 1'S NUMBER IS 10 OUT OF 10, NOT 9: on this question,
    description is already at the ceiling (ten out of ten without
    few-shot, n60). Adding few-shot on top of a ceiling can't physically
    push it higher — telling "doesn't hurt" apart from "can't possibly
    hurt" is impossible on this question, and the frame says so directly.

    WHY THE "6 VS. 5" DIFFERENCE ON SCENARIO 2 ISN'T CALLED A REGRESSION:
    one answer out of a sample of ten is one different binary run of the
    model; at n=10, a difference like this can't be told apart from
    ordinary run-to-run spread without re-measuring description alone in
    the same session (which wasn't in budget — 20 of the 25 allowed calls
    were already used). What's firmly proven is only that the combination
    is no better than description alone; calling it "few-shot hurts" on
    this data would be a stretch.
---

# Few-Shot, Description, and Their Combination — on the Case's Two Questions

## Assertion

A description of the boundary in the prompt fully cleaned up the persistent error. Few-shot with the same examples didn't clean it up at all. Combining both techniques gives no more than description alone, on neither of the case's two questions.

## Visual

> **Methodology (the boundary question).** Temperature `0` · model `qwen-2.5-7b-instruct` · question — the same one that already gave the T=0 error 10 out of 10 on the previous measurement · repeats `10`

| Variant | Setup | Correct out of 10 |
|---|---|---|
| few-shot | 2 contrasting examples (a number below the threshold, a number above it) ahead of the knowledge base | **0 out of 10 — CORRECT** (the same error as without examples) |
| description | one explanatory sentence about the boundary after the knowledge base, with no examples | **10 out of 10 — CORRECT** |
| combination (few-shot + description together) | both techniques in one prompt: examples → knowledge base → description | **10 out of 10 — CORRECT** |

> **Why this isn't obvious.** Two contrasting examples would seem like a direct demonstration of the logic needed. It didn't work: the model appears to have copied the answer's form and failed to extract the number-comparison rule from the examples. A plain, direct explanation of the boundary worked completely: it requires no generalization from the model at all. Adding few-shot on top of description doesn't change the result — ten out of ten, the same ceiling as description alone; on this question, telling "doesn't hurt" apart from "can't possibly hurt" is physically impossible, the ceiling is already taken.

> **And on the case's second question (the retake self-contradiction)?** few-shot — 0 out of 10, the same zero result as on the boundary. Description — 6 out of 10. Combination — 5 out of 10. **The techniques don't add up**: on neither question did adding few-shot raise the result above description alone. The "6 vs. 5" difference is one different model run out of ten repeats; the absence of improvement is proven, a proven regression is not.

## Speaker notes

Methodology, briefly, in large blocks, so there's no paragraph to page through: temperature zero, the same model used everywhere on this rig, the same boundary question that already gave ten out of ten wrong on the previous measurement, ten repeats per variant.

The model behind both measurements on this frame is called `qwen-2.5-7b-instruct` — exactly the same one that already gave ten out of ten wrong answers at zero temperature and with no hint about the boundary at all. This is worth saying out loud: the difference between few-shot and description here comes neither from the model nor from the question — it comes exactly from what was added to the prompt ahead of the same question that had already, once, broken this model consistently.

Few-shot — zero out of ten correct. This isn't spread and it isn't partial success: all ten times, the model repeated the same error as with no example at all, even though one of the two examples differed from the question by literally one ruble in the other direction. It looks like the model picked up the answer's form — tone, length, structure. The number-comparison rule the example was meant to teach, it didn't pick up.

Description — ten out of ten correct. One direct sentence, with not a single example, simply naming the boundary in words: turned out to be enough.

And an important caveat about the number format itself, worth carrying out of this measurement into any other breakdown: "N out of 10" by itself says nothing about quality — it's a reproducibility metric; it doesn't measure correctness. Ten out of ten can mean ten identical correct answers, or it can mean ten identical wrong ones, as happened on the previous measurement. A number with no explicit "correct" or "error" label next to it reads as success simply because it's large — and that reading is wrong.

The third technique — the combination: the same few-shot and description texts, word for word, together in one prompt, in the same order as when used separately. On the boundary question, the combination gave ten out of ten correct — exactly as much as description alone. That's not a gain: few-shot added nothing to an already-working technique, and checking whether it even gets in the way is impossible here — description already occupies the ceiling.

On this same case's second question — the self-contradicting answer about retakes — few-shot again didn't help: zero out of ten without self-contradiction, the same result as on the boundary. Description cleaned up the error partially: six out of ten. Combining both techniques gave five out of ten — one run fewer than description alone. On neither of the case's two questions did the combination beat description alone: on the boundary, description is already at the ceiling, there's physically nowhere higher to go; on the retake question, the "6 vs. 5" result is one different binary model run out of ten repeats, and at that sample size a one-point difference can't be told apart from ordinary run-to-run noise. Only the absence of improvement is proven; there's no proven regression in these numbers.

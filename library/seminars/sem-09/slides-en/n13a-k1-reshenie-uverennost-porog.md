---
id: n13a
type: measured_outcome_table
duration_min: 2.0
assertion: "Before building grounding in a knowledge-base item, we measured the cheapest move first — a confidence number and a threshold in code — and it turned out the worst of the three tested options, not the middle one"
learning_goal: "Owner's edit 2026-10-27: row 4 of the n08 breakdown ('the model names a confidence number, a threshold in code') had, until this beat, only ever been cited against external sources as obviously weaker than structured grounding — it had never been built and measured on our own task. This beat builds and measures it FIRST, on the same 15 hard questions as version 1 (n13) and version 2 (n16) — the grounding gate in the beats ahead is added on top of it, not in place of a comparison that never existed."
visual:
  pattern: measured_outcome_table
  primary: >
    An architecture line on top (one model call: answer + a confidence
    number 0-100 → code checks it against a threshold of 70), below it a
    strip of tiles with the outcome for all three variants on the same 15
    questions, and below that two breakdowns with verbatim quotes of the
    errors the threshold let through.
  backup: >
    Numbers — `stend/zamery-k1-k3/README.md`, Measurement 3 (runs
    840-854), built and measured by `build_case1_confidence.py` on the
    live rig, webhook `s9-answer-confidence`. Graded against the same
    reference standard, `correct_by_base` (`voprosy_zamer1.py`), already
    applied to version 1 on n13: silence in the knowledge base read as a
    confirmed denial counts as an error regardless of how confidently it's
    stated — the same yardstick that already caught version 1's error on
    the medical-certificate question.

    BEAT ORDER: this slide comes BETWEEN n13 (version-1 result, hard case)
    and n14 (version-2 n8n screen) — architecturally and chronologically,
    version 1.5 is measured BEFORE version 2 is built, exactly as the
    owner asked: the simple, cheap move first, then the structured
    grounding added on top of it, not pulled from nowhere.

    The threshold of 70 was chosen BEFORE measurement — a round middle
    number, not fitted after the fact to the result.

    THE MODEL IS NAMED ON THE FRAME (C5, 2026-10-29 edit):
    `qwen/qwen-2.5-7b-instruct` — the same model as in version 1 (n10/n11)
    and version 2 (n14/n15), called with no explicitly set options.

    OWNER'S 2026-10-27 EDIT — the n60a format (an explicit label for what
    a number means) carried over here too: "8 (53%)" in the outcome column
    is the worst result of the three variants, not a middle one, but
    without an explicit label it would read as just "another number"
    between the 6 (40%) figures in the neighboring rows. A minimal text
    label, "WORSE THAN BOTH OTHERS," was added directly in the table cell
    — without turning the table into tiles, without changing the rest of
    the slide's structure. n26a already carries an equivalent label in
    words ("worse, not better" in the "rule wording" row) — no change
    needed there.
---

# Version 1.5 — a confidence number and a threshold

## Assertion

The cheapest next step is to ask the model to name its confidence as a number and cut off low scores with a threshold. We measured it first, on the same questions.

## Visual

> **Design.** The same question and the same knowledge base, one model call — `qwen/qwen-2.5-7b-instruct`, with no explicitly set call options: it answers and additionally names a confidence number, 0-100. Code compares that number against a threshold of **70**: above it, the answer goes to the client; below it, it escalates to Olga.

| Variant | Confident/missed wrong answers | Abort | Total "bad outcomes" out of 15 |
|---|---|---|---|
| version 1 (free self-report) | 6 | 0 | 6 (40%) |
| **version 1.5 (confidence + threshold)** | **5** | **3** | **8 (53%) — WORSE THAN BOTH OTHERS** |
| version 2 (grounding + gate) | 4 | 2 | 6 (40%) |

> **What the threshold showed.** Self-rated confidence took only two values across all 15 questions — 100 or 85, nothing in between and nothing lower. The threshold of 70 caught **not one** of the five substantive errors — all five went through with a number above the threshold.

| Question | Version 1.5's answer (confidence) |
|---|---|
| Is a medical certificate needed? (not a word about it in the base) | "Not required" — silence read as a denial (100) |
| Gave 48h notice — will rescheduling be allowed? (rule: no later than 24h) | "Not allowed" — 48 is greater than 24, rescheduling should be allowed (100) |

> **Where the finding points.** Three of the five errors are the model building past what the knowledge base doesn't say, and simply signing the result with a high number; the threshold offers no protection against this at all. The 48-hour question is the same slip version 1 already made on this exact question: confidence as a number doesn't fix it.

## Speaker notes

Before building the version with grounding in a knowledge-base item, we built and measured a simpler, cheaper variant — the one we'd only ever mentioned in passing before. The design is simple: one model call, it answers and also names a number from zero to a hundred — how confident it is the answer is correct. Code compares that number against a threshold we picked in advance, before a single run — seventy. Above the threshold, the answer goes to the client. Below it, the question goes to Olga.

We ran the same fifteen hard questions as version 1. The result is on screen: six bad outcomes for version 1, eight for version 1.5, six for version 2, which we haven't built yet, but the number for comparison is already here. Version 1.5 is the worst of the three, not the middle one.

Why. Self-rating turned out to be a blunt instrument: across all fifteen questions, the model named only two different numbers — a hundred or eighty-five. Nothing in between, nothing lower. And the threshold of seventy, which was supposed to filter out unconfident answers, caught not one of the five substantive errors — all five went through with a number above the threshold.

Let's name two cases directly. First — the medical certificate. The knowledge base says nothing about it, listing only passport, SNILS, and a parent's consent. The model confidently — a hundred out of a hundred — answered that a certificate isn't required. This is the same thing that already happened with version 1 on this exact question: silence in the knowledge base read as a confirmed denial. Confidence as a number doesn't notice this error — the model builds past the missing information just the same, just now it signs the result with a high number.

Second — the forty-eight hours. The rule: rescheduling no later than twenty-four hours before the start. The client gave two days' notice — that's forty-eight hours, more than twenty-four, rescheduling should be allowed. The model answered that it wasn't, with a confidence of a hundred out of a hundred. That's the same number-comparison slip version 1 already made on this exact question.

So the conclusion: the cheap move was tried first, not second. It doesn't replace structural grounding in a knowledge-base item — it shows exactly which part of the work that grounding doesn't do either. Next, we build the version with item-level grounding.

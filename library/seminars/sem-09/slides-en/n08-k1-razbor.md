---
id: n08
type: answer_breakdown_table
duration_min: 2.0
assertion: "Three of the five actions leave the 'answer or hand off' decision exactly where there's nothing left to re-check it with"
learning_goal: "Breakdown right after the question (A1), 5-column form 'action · how it works · accuracy · advantage · drawbacks' (A5 plus a separate number column, C6, 2026-10-29 edit). No 'right/wrong' verdicts about our own measurement — it hasn't been shown yet (C2)."
visual:
  pattern: answer_breakdown_table
  primary: >
    A table: action · how it works · accuracy · advantage · drawbacks.
    Five rows (the fifth — external store — is added and immediately set
    aside by knowledge-base size). The "accuracy" column carries only
    EXTERNAL numbers or numbers from last session — this case's own
    measurement isn't on this frame, it belongs in n11a/n12/n13 (C2). No
    verdict column.
  backup: >
    The diagram "where each action sits on the 'decision in the model —
    decision in code' axis" (issue #303, Part B) is pulled out into its
    OWN frame BEFORE this breakdown (see n07a) — with the "accuracy" column
    added, the 5-column table is already at the floor of its type size
    (9pt, "the build can't go any lower," measured by a designer pass);
    adding the diagram to the same frame would push the table past that
    floor. Resolved per the task rule: "the diagram gets its own frame
    before the table, if they don't fit together."
    The breakdown text is condensed from SETKA-KEYSOV-S9.md, section
    "Case 1", subsection "Breakdown", and fit into the 4-column form
    without rewording its substance; THE FIFTH COLUMN AND FIFTH ROW were
    added by the 2026-10-29 edit (BREAKDOWN, K1-4 and K1-7 — both marked
    "repeat request").

    A RESOLVED COLLISION, flagged to the orchestrator by report:
    `forma-keysa-s-zamerom.md` §12 item 2 leaves open whether to add C6 as
    a fifth column to the A5 form or as a number on a separate tile. Here
    the first path was taken (fifth column) — a decision made by request
    frequency ("repeat request" twice), not a final close of the collision
    for every case: that stays explicitly left to the owner, in the same
    file.

    THE "ACCURACY" COLUMN CARRIES NO NUMBERS OF ITS OWN FROM THIS
    MEASUREMENT — a second deliberate departure from the letter of K1-7,
    also flagged by report. This measurement's own numbers (6 of 15, 4 of
    15, 2 of 15, 8 of 15) sit on frames n12/n13/n13a/n16 — the owner's
    voice edit 2026-10-20 (issue #274) on the equivalent beat last session
    forbids a breakdown from naming a run's outcome before the room sees
    the run itself (C2 requires the same: "a measured result before the
    test-structure frame" is forbidden). This column carries what CAN be
    said WITHOUT that spoiler: an external measurement (rows 1 and 4) and
    last session's own measurement, already shown to this room (row 2).

    Row 3 (model names the item, code decides) and row 5 (external store)
    get an "accuracy" cell that is empty and labeled in words, not just
    left blank: for row 3, because that is exactly what the rest of the
    case measures; for row 5, because the option is set aside, never
    built, never measured (C6: an empty cell is fine if labeled "not
    measured").

    Numbers remaining in the column: 73.0% → 36.1%, and "missed refusals
    4.3% against wrongful refusals 62.8%" — CHISLA-SVERENO.md, line 35
    (RefusalBench, arXiv:2510.10390, status VERIFIED; attribution per note
    No. 2 of the same file — these are GPT-4o's numbers, not GPT-3.5's).
    The calibrator at 56% against the 48% threshold at 80% precision —
    CHISLA-SVERENO.md, line 37 (Kamath et al., arXiv:2006.09462, status
    VERIFIED). "0 of 5 rephrasings against 15 of 20 pairs" — last
    session's own measurement, already shown to this room
    (`sem-08/slides/n20-k2-razbor.md`).

    Nothing taken from `research/*` (BRIEF §2 forbids it).

    THE MODEL IS NAMED ONCE, FOR THE WHOLE TABLE (C5): rows 1, 3, and 4
    call the model, and it's the same model everywhere in the case —
    qwen/qwen-2.5-7b-instruct, called with no explicitly set options
    (temperature and other parameters are the interface defaults,
    `stend/sborka.py`, `ANSWER_MODEL`). Named in a separate line before
    the table, not in every cell.
---

# What each of the five actions actually does

## Assertion

None of the five is a mistake by itself. The difference is whether it leaves behind a trace that can be shown and re-checked.

## Visual

> **The model, everywhere it's involved, is the same one: qwen/qwen-2.5-7b-instruct, with no explicitly set call options.**

| Action | How it works | Accuracy | Advantage | Drawbacks |
|---|---|---|---|---|
| **the model decides and answers freely** | gets the whole knowledge base and the question in one call, decides, and writes the answer | 73.0% → 36.1% on similar documents (RefusalBench, external measurement) | needs no breakdown of questions into topics | the decision is recorded nowhere separately from the text — there's nothing to re-check it with |
| **exact match against a topic list** | the string is compared against ready-made wordings, the model is never called | 15 of 20 repeats · 0 of 5 rephrasings (last session's measurement) | zero cost, same question → always the same outcome | a client rarely repeats the knowledge base's own wording word for word |
| **the model names an item, code decides** | the model puts a knowledge-base item (or nothing) in a "grounding" field, code decides by a condition | not measured here — in the beats ahead | the decision is recorded separately from the text, the same code checks it every time | the topic list has to be kept in step with the knowledge base; the check asks no more than what's written into it |
| **the model names confidence as a number** | a free answer plus a confidence number, a threshold in code decides | 56% against 48% at 80% precision (Kamath et al., external measurement) | needs no topic field, strictness is a single number | the threshold is weakest exactly where it's needed most — on unfamiliar questions |
| **search the needed item in an external store (RAG)** | the question searches for a similar fragment, only the found piece goes to the model | not applicable | scales to a knowledge base of any size | the knowledge base is ten items, it fits entirely in one field; a separate store adds its own source of error where none is needed |

## Speaker notes

Let's break down the five actions in order. None of them is foolish: each has a task where it would be the right choice. The question is which task we actually have — and the model, in all four where it's involved, is the same one, with no special call settings.

First — the model decides and answers freely. It gets the whole knowledge base and the question and does both things in one call: decides whether to answer or decline, and writes the text. The convenience is real — no preparation, any client wording works. But look at where the decision ends up afterward: inside the answer text, and nowhere else. This isn't a nitpick: the ability to answer and the ability to stay silent at the right moment are measured separately, and they grow independently in models. On a benchmark where the answer has to be found across several documents, the best verified models' score drops from seventy-three percent to thirty-six — an external measurement, not ours, but it warns of exactly the same imbalance.

Second — exact match, no model at all. Cheap, instant, and the same question always gets the same outcome. We already measured its weakness last session: fifteen of twenty pairs caught, zero of five rephrasings. A person doesn't repeat the knowledge base's wording word for word.

Third — the model names an item, code decides. The model does exactly one job: it puts the name of a knowledge-base item into a separate field, or admits that none fits. The decision ends up recorded separately from the text, and the same code checks it every time. The cost: the topic list has to be formalized in advance. We haven't seen this option's accuracy on our own task yet — it's in the beats ahead, and I'm deliberately not naming it early.

Fourth — confidence as a number. Looks like a compromise. The trouble is that raw model confidence works worst exactly where it's needed — on questions from unfamiliar territory: a separately trained calibrator, at eighty percent precision, answers fifty-six percent of questions; a threshold on raw confidence, at the same precision, answers only forty-eight. That's an external citation, and this same option's own measurement, further on in the case, doesn't overturn it.

Fifth — search the needed item in an external store instead of putting the whole knowledge base into the call. On our task it doesn't apply: the knowledge base is ten items, it all fits into one text field, and setting up a separate store for it means adding a source of error (a mismatched fragment found) where the original problem doesn't exist. This option is set aside right here: we won't be testing it.

Which action closes Olga's need — next screen.

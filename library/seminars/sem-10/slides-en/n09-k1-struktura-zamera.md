---
id: n09
type: measured_outcome_table
duration_min: 1.0
assertion: "The same set of ten questions runs through all three actions at each of four base sizes — not a single result on this frame"
learning_goal: "Beat S2 (measurement structure, canon forma-keysa-s-zamerom.md §1): the model and its settings, what varies in the measurement, an example question and the expected answer — BEFORE a single outcome number appears on the frame. Inserted between n07 (the audience question) and n10 (the summary) so the audience sees the test's structure before the first number (cost of skipping it — slide 12 of the Seminar 9 deck, the 2026-10-29 review: 'I don't understand whether it answered right or wrong,' when three beats are compressed into one)."
visual:
  pattern: measured_outcome_table
  primary: >
    A tile with the model and settings on top, below it a table of "what
    varies" (base size, action), below that a tile with an example
    question and the correct answer. Neither "correct," nor "incorrect,"
    nor a single accuracy/cost number is on this frame.
  backup: >
    A NEW BEAT, added by this edit (S2 canon: "the test's structure,
    before any results," `forma-keysa-s-zamerom.md` §1). Before this edit,
    n10 opened straight into a summary of results — with no separate
    frame for the test's structure before it, exactly the defect the canon
    names by quoting the owner about Seminar 9's slide 12.

    MODEL AND SETTINGS (C5): `openai/gpt-4o-mini` — forms the final answer
    from the passed-in text; `openai/text-embedding-3-small` — computes
    embeddings of the question and the documents for vector search. Both
    calls go through the same rig webhook (`s10-raw-openrouter`), with no
    explicitly set additional settings (temperature and other parameters
    are default): `stend/harness2.py`, `CHAT_MODEL`/`EMBED_MODEL`. The
    system instruction for the answer call is shown literally on n18 — it
    isn't repeated here, to avoid duplicating a frame.

    CORPUS AND WHAT VARIES: `stend/measure/case1_measure.py`. Ten SberQuAD
    questions (an open question-answering dataset built on Russian
    Wikipedia articles with gold-standard labeling) — THE SAME set across
    all twelve "base size × action" combinations. The corpus at each size
    consists of ten documents carrying the answers to these questions (the
    "needle") plus random distractor documents up to the needed volume:
    10 = needle only, 50/200/500 = needle + distractors.

    EXAMPLE — verbatim from `raw/case1-results.json`, qid `q1`, base size
    10 (the same question is asked, unchanged, at all four sizes). The
    expected answer is the protocol's own `reference_answer` field, not my
    own wording; `gold_doc_id` is the document that contains this answer.
    Case 1's questions were rebuilt on 2026-11-02 (issue #311) with
    lexical_gap/exact_match/neutral stratification — the same
    classification already used in Case 3 (`corpus/corpus_case1.json`,
    the `questions` field, `lexical_class`); q1 belongs to the
    lexical_gap class (overlap_ratio 0.2 — the question and the document
    share few words in their base form).

    NOT A SINGLE RESULT ON THE FRAME (C2): no accuracy, no cost, no
    recall, not the word "error." The test's structure in full — and it
    stops here.
---

# Measurement structure: ten questions, four sizes, three actions

## Assertion

Before looking at the numbers — what question was asked, against what, and what the correct answer to it is.

## Visual

> **Model and settings.** `gpt-4o-mini` — answer from the passed-in text; `text-embedding-3-small` — embedding for the search. Both with no explicitly set additional settings, the same call across all twelve combinations.

| What varies | Values |
|---|---|
| Base size | 10 · 50 · 200 · 500 documents |
| Action | the whole prompt · search by word → answer · search by meaning → answer |
| Questions | the same set of 10, identical across every size and action |

> **Example.** "What is the name of the circulation circuit that runs through the lungs?" — correct answer: "the pulmonary" (document `needle-1`, present in the base at all four sizes).

## Speaker notes

Before looking at what the model answered, let's lay out the test itself — the same order we already used last session: structure first, number second.

Ten questions from SberQuAD, an open question-answering dataset built on Russian Wikipedia articles with gold-standard labeling of which text fragment holds the correct answer. This is the same set of ten questions across all twelve combinations of the measurement — not a single question changes between base sizes or between actions. What changes is only what surrounds the question: how many documents are in the base and by what method the answer gets found among them.

Base size takes four values: ten, fifty, two hundred, and five hundred documents. At size ten, the base holds exactly the ten documents that carry the answers to all ten questions. At the larger sizes, random distractor documents get mixed in — the same SberQuAD corpus, just not containing the answer to any of our questions — until the base's total volume grows to the needed number.

Action is also three values, and they're exactly the three cards you just voted on: append the whole text of the base to the prompt, search for the right document by word match and then answer from it, search by meaning through embeddings and then answer from what was found. Four sizes by three actions makes twelve combinations, and every one of them runs across all ten questions.

Here's what one of these ten questions looks like, and what "correct" means here: "what is the name of the circulation circuit that runs through the lungs?" The correct answer is "the pulmonary [circuit]," and it's contained in one specific corpus document, called `needle-1` throughout the measurement — the "needle" that has to be found in a haystack of growing size. The document opens like this: "Circulation is the movement of blood through the body," and the fact we actually need, about the pulmonary circuit, sits further down in the text — it isn't in the opening sentence. The question and the document share few words in their base form between them — this is deliberately not an exact-match question. This document is present in the base at all four sizes without exception: once added, it never goes away as the base grows — only what surrounds it grows.

There isn't a single result on this frame. What each of the three actions produced at each of the four sizes, as a number — next beat.

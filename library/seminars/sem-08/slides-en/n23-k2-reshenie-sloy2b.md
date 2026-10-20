---
id: n23
type: mechanism_node_graph
duration_min: 2.5
assertion: "The expensive step isn't a text prompt — it's a structured request to a specialized service with a quantized 'yes/no with probability' question — and across all 20 real pairs the split is clean: duplicates 0.70–0.97, different questions 0.02–0.08"
learning_goal: "Layer 2b of the 'our solution' beat — fully rebuilt 2026-10-20: the judge model (free-text prompt) was replaced on the live rig by the jev node (a structured HTTP request with a typed yes/no-with-probability question). Shown with the full real distribution across all 20 test pairs, not two sample runs, with no system ids on screen."
demo: true
visual:
  pattern: mechanism_node_graph
  figure: k2-n8n-jev-real.png
  primary: >
    A real screenshot of the n8n canvas: the node `Jev decision
    (reworded?)` (`httpRequest`, globe icon) labeled `POST:
    https://openrouter.ai/...` on the production workflow's canvas. The
    request's structure (model, question type noul, criteria) and the real
    score distribution across the 20 pairs are given as a separate text
    block alongside, not inside the image (same as the prompts on
    neighboring slides of this case).
  backup: >
    The figure is a real screenshot, 2026-10-20: a crop from the same file
    as n22 (one canvas, two different nodes),
    stend/n8n-screenshots-raw/case2-dedup-prod-jev.png, the region (1010,
    742)–(1570, 908) of the source file, enlarged 2×. Saved as
    library/seminars/sem-08/rendered/figures/k2-n8n-jev-real.png. Partially
    visible at the top of the frame is the background node "Result screen ·
    not parsed" (the real, dense layout of the canvas, not a crop artifact
    — the same honesty as the n22 figure).

    The FIRST VERSION of this edit used a crop of the node's settings panel
    (case2-jev-node-config.png) as the figure — the portrait aspect ratio
    (752×1587) didn't fit the mechanism_node_graph layout: the builder
    (tools/seminar-build/build.py) returned blocking OVERFLOW/DOESN'T FIT
    warnings (the diagram shrank to 1.02″, the text and table spilled
    outside the working area). Replaced with this landscape canvas crop —
    every other -real.png figure in the case (n11, n14, n34, n50) is also
    landscape (roughly 4–5:1), which isn't a stylistic choice but a
    constraint of the slide layout. The settings panel
    (case2-jev-node-config.png) wasn't discarded as a source, though: the
    full JSON body text below in this field was read directly from it and
    cross-checked against the live API.

    The FULL, real JSON body of the node (verbatim, from the live API):
    `{model: "typesafe/jev-1.13", state: {previous_message:
    $json.recent_same_contact_text, new_message: $('Request
    form').item.json['Что нужно']}, questions: {same_question: {type:
    "noul", instructions: "Новое сообщение клиента учебного центра — это
    тот же вопрос, что и недавнее сообщение того же контакта, просто
    переформулированный (перефразировка), а не новый, другой по смыслу
    вопрос?", criteria: {true: "Это переформулировка того же вопроса,
    который уже был задан — смысл совпадает, слова разные.", false: "Это
    другой по смыслу вопрос, даже если тема или часть слов похожи."}}}}`.
    The instructions/criteria strings are kept verbatim in Russian, exactly
    as configured on the live node — they are the real, literal instruction
    text sent to jev, not a translation artifact (the same documented
    exception as n22a's field names). In English, that body reads:
    instructions — "Is the training center client's new message the same
    question as the same contact's recent message, just reworded (a
    rephrasing), rather than a new, different question?"; criteria.true —
    "This is a rephrasing of a question already asked — the meaning
    matches, the words differ."; criteria.false — "This is a different
    question in meaning, even if the topic or some words look similar."
    Read off the screenshot case2-jev-node-config.png and checked verbatim
    against the live n8n API (GET /workflows/c7evxIhox45tn127, node id
    "jev-prod") — both sources match word for word, no discrepancies.

    The results — verbatim from stend/duplicate-check-results.json →
    jev_measured: 20 pairs from stend/duplicate-check-test-pairs.json were
    run through the test webhook s8-case2-duptest (workflow
    stage-2-duptest.json, the same jev node as in the production chain, but
    in a test harness for a batch run — the methodology is identical to the
    node on screen). Classification threshold jev_noul >= 0.5 →
    "duplicate". Result: 20/20, a clean split — the duplicate pairs (id
    1–10) give jev_noul 0.70–0.97, the different-question pairs (id 11–20)
    give 0.02–0.08; the 0.5 threshold holds comfortably across the whole
    0.08–0.70 gap, and choosing a specific threshold within that interval
    doesn't change the final score. For context, on the same set: hash
    15/20, TF-IDF 13/20, LLM judge 17/20 — the same numbers as on n20/n21,
    not recalculated.

    An example of one pair for concreteness (id 6, a rephrasing, real texts
    from the set): "when can I pay for the class?" → "how do I pay for the
    course", jev_noul = 0.76 — above the threshold; jev correctly
    recognized the rephrasing exactly where hash and TF-IDF give 0 by
    construction (different strings, no shared meaningful words).

    Execution ids are never mentioned — not in the slide text, not in the
    notes, not on the figure (canon §3): instead of run numbers, the test
    set's pair id (1–20) is used — that's a data identifier, not a rig
    identifier.
---

# Configuration: A Structured Request Instead of a Text Prompt

## Assertion

The expensive step isn't free-form text for a model — it's a structured HTTP request to a specialized service: a closed "yes/no with probability" question, an explicit instruction, explicit criteria. Across all 20 real pairs, the split is clean.

## Visual

> **Node `Jev decision (reworded?)` (`httpRequest`).** `POST .../api/alpha/decisions`, model `typesafe/jev-1.13`. The question type is `noul`: "yes/no" with a probability, not free-form text. The criteria are given explicitly: "yes" — the same question in different words, "no" — a different question, even if the topics or some words look similar.

> **Result on 20 real pairs.** Duplicates — jev_noul **0.70–0.97**. Different questions — **0.02–0.08**. Threshold **≥ 0.5 → duplicate**, a clean gap across 0.08–0.70 — the score is **20 out of 20**.

## Speaker notes

Here's the second node — the one that only sees what the cheap filter didn't resolve unambiguously. And it's built fundamentally differently from what used to stand in this exact spot.

It used to be a request to a general-purpose model with a free-text prompt: describe the task in words, ask it to answer "yes" or "no". Now it's a structured HTTP request to the specialized service jev. The difference isn't just the tool — it's the very shape of the question: the service doesn't accept arbitrary text, it accepts an explicitly typed question — in this case type `noul`, a closed "yes or no" question, but not simply binary, with a probability attached. Both texts are passed along, plus an explicit instruction for what counts as "the same question", and two explicit criteria — what counts as a "yes", what counts as a "no". None of this has to be guessed from the tone of the wording, the way it would in a free-form prompt: the criteria are a separate, explicit field of the request.

The result was checked not on two illustrative runs but on all twenty pairs of the test set — the same one hash, TF-IDF, and the judge model were measured on earlier. The split came out clean: on the ten pairs where a duplicate was expected, the service returned a probability between 0.70 and 0.97. On the ten pairs where a different question was expected — between 0.02 and 0.08. Between these two groups there's an honest gap: the maximum among the "different" pairs is noticeably below the minimum among the "duplicate" pairs. The 0.5 threshold holds a wide margin here, and that matters: the result doesn't depend on a luckily chosen threshold — the service split the pairs apart confidently in both directions.

Let's take one pair for concreteness, so we're not left with only ranges. "When can I pay for the class?" and "how do I pay for the course" — different words, the same meaning. jev returned 0.76 — comfortably above the threshold. On this same pair, hash and TF-IDF give zero — not because they erred, but because by construction they have no shared meaningful words to compare: this is exactly the kind of task where mechanical comparison is blind in principle, and the meaning check isn't.

Now, after seeing both nodes of the real chain, — what this means for the architecture as a whole.

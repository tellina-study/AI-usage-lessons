---
id: n06
type: problem_scenario
duration_min: 1.5
assertion: "Olga wants the same accurate, cheap answer at any base size; version 1 is simply to keep appending the base to the same prompt with no ceiling"
learning_goal: "Case 1's scene beat: a live staging of the need — what Olga wants, which version 1 is the natural one, and what it risks as the base grows. No verdict and no run number (rule A6/C2: the finding belongs to the question beat and the breakdown, not here)."
visual:
  pattern: problem_scenario
  figure: case1-shema-postanovka-en.png
  primary: >
    On top — diagram S1 (case-design canon forma-keysa-s-zamerom.md §2):
    solid lines for the flow already working since last session (a
    question via the form → the whole knowledge-base text goes into the
    prompt in full → the model answers, seeing the whole base); a dashed
    gold arrow for what this case builds: a separate store and a search for
    the needed chunk, which will take the place of the "the whole
    knowledge base at once" node. Below the diagram — a tile with the need
    ("an accurate, cheap answer at any base size"), three solution-shape
    alternatives with no numbers and no verdicts, and the honest question
    the scene leaves open.
  backup: >
    The need and version 1 are verbatim from SETKA-KEYSOV.md / rework/
    section-1-khranenie-bazy.md, "Staging." Alongside version 1, two more
    genuinely considered methods are named (without a breakdown) — keyword
    search and a vector store, exactly as the staging of the whole case
    (not just the question) requires: there are no numbers and no
    advantages/drawbacks here, that's the job of the question beat (n07)
    and the breakdown (n10/n13).

    THE STAGING DIAGRAM (rule S1) is added by this edit: `rendered/
    make_figures_sem10.py::case1_shema_postanovka()`, a new function that
    doesn't touch the existing `case1_scheme`/`case2_scheme`/`case3_scheme`/
    `case4_scheme`. The solid row is the nodes that already exist and
    already work (the question form, the whole base's text in the prompt,
    the model's answer); they carry forward Seminar 9's own staging (`n05`,
    speaker notes: "the process learned to answer the requester on its own
    — from a knowledge base of ten items, written into the prompt in
    full"). The dashed arrow is the one element of the diagram that doesn't
    exist yet: it points at the "the whole knowledge base at once" node,
    because that is exactly what this case's solution will replace
    (confirmed by n15: "instead of handing the model the whole base...
    stores the base separately"). The tool's name (n8n, OpenRouter) is
    deliberately absent from this diagram — it's about the message flow,
    not the implementation; the implementation is layer 2, n16/n17/n18.

    THE MODEL IS NAMED RIGHT ON THE DIAGRAM (C5): the "Model answers" node
    carries the caption `gpt-4o-mini, whole base in the prompt` — the same
    name used everywhere in this case's measurement
    (`stend/harness2.py::CHAT_MODEL`). Unlike n15 (layer 1, the case's
    architectural formulation, deliberately without the tool's name AND
    without the model's name — it has to survive a change of both), this
    diagram is not the solution's architecture but the live message flow
    carrying Seminar 9 forward, and the model in it is already being
    called for real, so C5 applies to it literally.
---

# What Olga needs from a growing base

## Assertion

The answer stays accurate and cheap even once the base grows from ten items to hundreds of documents — the question is how to build that.

## Visual

> **The need.** The answer stays accurate and cheap even once the base grows from ten items to hundreds of documents.

1. Version 1 — the natural continuation of Seminar 9: keep appending the base to the same prompt, with no ceiling.
2. Two more real methods: search by word match; search by meaning — through a vector store.

> All three are real engineering options. Which one survives the base's growth is the next screen's question.

## Speaker notes

Olga's training center wants the same thing it wanted last session: an accurate, cheap answer to the requester. The difference is that the base the process relies on no longer stands still. Every week it gets a new regulation, an updated FAQ item, another disputed case worked through with the last cohort. Last session's ten items were the base as it stood when the process launched; from here it keeps growing.

Version 1 is the most natural continuation of what already worked: simply keep appending the base to the same prompt, with no ceiling. That's what was done last session, and that's what Olga assumes will keep being done — until someone checks what happens when the prompt holds several hundred documents instead of ten items. The convenience is obvious: nothing needs preparing in advance, no separate search step is needed, and any new item just gets appended to the end of the text.

Alongside this natural continuation stand two other, real ways to build the same thing. The first is to search the base by word match — classic full-text search with not a single call to the model: the question is compared against the documents' text, and whichever document shares the most words wins. The second is to search by meaning, through a vector store: the base is turned in advance into numeric representations of each document's meaning, so-called embeddings, and a query finds the document closest in meaning to the question.

All three are exactly what an engineer in the same situation would genuinely consider once the base starts growing. None of them is a strawman set up for contrast. The question the scene leaves open: which of the three survives the base's growth, and what happens to the cost and accuracy of the answer while it does. We'll check with a run on real questions with an already-known correct answer — next beat.

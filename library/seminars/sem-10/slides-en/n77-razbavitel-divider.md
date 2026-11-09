---
id: n77
type: case_divider_quote
duration_min: 0.5
assertion: "Today's four cases all taught finding the needed chunk — not one of them checked whether what was found was correct"
learning_goal: "Opening of the concept interlude. The form is the same as the case dividers (case_divider_quote), but it is NOT registered in the config's case_idx — the case track isn't drawn (the interlude sits outside case_track, ARCHITECTURE.md §4). Names the problem, not the solution."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, one action line, large. There is NO case track on
    this screen — the interlude isn't part of case_track (unlike
    n05/n22/n39/n59).
  backup: >
    The transition — SETKA-KEYSOV.md / rework/section-5-razbavitel-ai-
    overviews.md, "Why this is here," verbatim. sid n77 is deliberately
    absent from the config's case_idx — g_case_divider only draws the
    track if idx is found, otherwise it draws the divider without one.
---

# Relevant ≠ Correct

## Assertion

A search that found a topically relevant chunk did its job perfectly — and that says nothing about whether the chunk is correct.

## Visual

> Today's four cases all taught finding the needed knowledge-base chunk and putting it in the prompt before answering. The whole time, standing just offscreen, was an assumption never explicitly checked: that if the system found a chunk topically related to the question, the answer built on it would turn out correct.

## Speaker notes

Today's four cases all taught finding the needed knowledge-base chunk and putting it in the prompt before answering. The whole time, standing just offscreen, was one assumption that was never explicitly checked: that if the system found a chunk topically related to the question, the answer built on it would turn out correct.

Each of the four cases had its own reason why context preparation breaks, and those reasons are different. In the first case, prompt-stuffing lost a fact among a growing number of similar documents, even though the fact itself was physically sitting right there in the prompt text. In the second, cutting by character count tore a ready-made answer apart right at the chunk boundary, whenever the cut wasn't made along a sentence's meaning. In the third, documents deliberately assembled to split one and the same rare entity confused both exact word matching and semantic search, and only adding a reranker pushed them into the right place. In the fourth, an image embedding at the resolution of a real scan saw no difference at all between two obviously different receipts. These are four different failure mechanisms, but behind each of them stands the same second step: the chunk the system decided was the right one gets put into the prompt, and the answer is built on it as if its content were true by definition.

This short breakdown names directly why this assumption is wrong on its own terms, regardless of how well the search itself is built. Found and correct are different things. The semantic search system we measured and praised in the third case for its high rank scores how close a text chunk is in meaning to the question; whether the statement inside that chunk is true is a separate question, one that falls outside its scope. A chunk can be plausibly close to the question on topic and still contain a joke, outdated information, or an outright mistake. The search that found it did its job perfectly — it found a relevant chunk. Responsibility for whether that chunk is correct is not something the search takes on.

Two documented incidents will show exactly what this looks like in practice — in real systems that were already running for real users; this isn't limited to our own training rig.

The finding at issue here isn't specific to any one particular search mechanism — it concerns the very idea of "search and answer based on what's found," regardless of whether that's a vector store, a full-text index, or a combination of the two. This is a warning about the very architecture of the approach we've been working through all day; it can't be called a finding about any one specific tool.

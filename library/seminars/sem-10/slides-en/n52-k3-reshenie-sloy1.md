---
id: n52
type: mechanism_node_graph
duration_min: 1.0
assertion: "Search is a merge of at least two relevance signals, and after the merge comes an optional step of review by the model"
learning_goal: "Layer 1 of Case 3: the architecture with no tool name attached, including the optional rerank step. The n8n screen comes next."
visual:
  pattern: content
  primary: >
    A single formula tile with the architectural thesis in two parts:
    merging signals + optional review by the model.
  backup: >
    Wording — SETKA-KEYSOV.md Case 3, "Solution," layer 1, verbatim.
---

# Search is a merge of at least two signals

## Assertion

The solution is to use both search methods at once and bring the results together, rather than choosing one instead of the other.

## Visual

> Search is a merge of at least two different relevance signals: one signal alone isn't enough, before deciding which chunk to put in the prompt. One signal (words) has its own zone where it wins — exact matches, names, numbers; the other (meaning) has its own — retelling in one's own words. After merging the signals comes an optional extra step: hand the final order off for review by the model, if the price of the separate call and the added latency are justified by the cost of a ranking error.

## Speaker notes

This is the architecture layer, worded so that it stays true regardless of which search tool is swapped in.

The main idea of the breakdown we just went through: search is a merge of at least two different signals before deciding which chunk to put in the prompt — a single relevance signal, chosen once and for all, isn't enough. The word signal has its own zone of confidence — exact matches, names, numbers. The meaning signal has its own — retelling in one's own words, the absence of a literal lexical match. The solution is to use both methods at once and bring the results together; there's no need to choose one instead of the other here.

Once the signals are merged, an optional extra step arises: hand the final order off for review by the model. The word "optional" is key here — this isn't the next rung that always has to be climbed, but a decision that's only justified when the price of a separate model call and the added latency are smaller than the cost of a ranking error: the requester won't get the right answer if the first candidate in the results turns out to be the wrong document.

What this looks like on the real canvas — next beat.

This step is named optional on purpose: it isn't treated as a mandatory finish to any search chain. The decision whether to add it or not weighs one specific cost against one specific benefit, and for different tasks of the training center the balance can differ. Where the requester gets an answer to a non-urgent organizational question, an extra second of latency and a fraction of a cent mean almost nothing against the gain in accuracy. Where the process answers instantly to dozens of parallel requests, that same addition can turn into a noticeable expense item: a gain of a few percentage points in recall doesn't pay it back.

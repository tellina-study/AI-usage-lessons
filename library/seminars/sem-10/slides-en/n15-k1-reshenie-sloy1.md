---
id: n15
type: mechanism_node_graph
duration_min: 1.0
assertion: "Instead of handing the model the whole base, the process stores it separately and, on each question, finds only the chunks it needs"
learning_goal: "Layer 1 of the 'our solution' beat (case-design canon §2): architecture with not a single node name and not a single tool name. Layer 2 — the n8n screen, next slide."
visual:
  pattern: content
  primary: >
    One formula tile with the architectural thesis, with no tool name and
    no node name.
  backup: >
    Wording — SETKA-KEYSOV.md Case 1, "Solution," layer 1, verbatim. There
    are no node names, no orchestrator name, and no Latin script on this
    slide deliberately: canon §2 requires layer 1's wording to survive a
    change of tool. The real screen is n16.
---

# Where the base is stored and what the model sees

## Assertion

The model sees a narrow, relevant set of facts — not the training center's entire archive.

## Visual

> Instead of handing the model the whole base on every question, the process stores the base separately from the conversation. On every new query, it first finds several matching chunks in that separate store and puts only those into the prompt, leaving the rest of the base aside.

## Speaker notes

This is an architecture layer, phrased so that not one word in it would need to change if this chain were built tomorrow in a different tool than the one we're using today.

The idea is simple and already came up in the previous beat's breakdown — but let's restate it on its own, in one sentence: this is the principle that carries over to any future project. Instead of handing the model the whole base on every question — that is, instead of prompt-stuffing, which we just measured and saw doesn't scale — the process stores the base separately from the conversation with the model. This separate store doesn't take part in the dialogue directly: it simply waits for a query.

On every new question, the process first turns to this store and finds several matching chunks in it: exactly the fragments that are close to the given question by some criterion — the whole archive takes no part here. Only those chunks get put into the prompt before the question is handed to the model.

The model ends up answering with a narrow, relevant set of facts in front of it. That's exactly why the prompt stays small and cheap regardless of how many documents have piled up in the store — we already saw that as a number on the previous two screens.

There isn't a word about a specific tool in this formulation, nor a word about a specific way of finding matching chunks — not about search by word, not about search by meaning. Both methods we just went through fit this architecture equally well: the difference between them is only in HOW exactly the needed chunk gets found; the fact that it's stored separately is the same for both. What this looks like on a real screen — next beat.

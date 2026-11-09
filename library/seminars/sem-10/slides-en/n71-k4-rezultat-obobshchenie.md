---
id: n71
type: content
duration_min: 1.0
assertion: "Olga can see the boundary: semantic similarity needs one mechanism, literal similarity needs another, cheaper one"
learning_goal: "Case 4's result and generalization: what the requester sees vs. Olga, the portable principle (an architectural idea can be correct without a ready-made working realization with a specific provider)."
visual:
  pattern: content
  primary: >
    Two tiles side by side: "to the requester," "to Olga" — then a formula
    tile for the portable principle.
  backup: >
    Text — SETKA-KEYSOV.md Case 4, "Result and generalization," verbatim.
---

# What Olga sees, and what the requester sees

## Assertion

Skipping the controlled experiment with two different inputs means carrying out of the session an unworkable solution that looked workable on the first test.

## Visual

The requester doesn't see exactly how the process found a similar past form — they see that it found it, when that's possible by content, and that the system separately and reliably tells a literal repeat scan of the same request apart from a new document. Olga sees the boundary: for one class of similarity (semantic — "the same type of form") one mechanism is needed, and for another (literal — "the same document, just re-shot") a different one is needed, and it's cheaper.

> **A principle, portable to any orchestrator: the architectural idea "compare data in its own space, bypassing a retelling" can be correct and still have no ready-made working realization with a specific provider at a specific moment — checking this takes one controlled experiment with two different inputs, and skipping that experiment means carrying out of the session an unworkable solution that looked workable on the first test.**

## Speaker notes

The requester doesn't see the search mechanics at all — all they see is that a similar past form was found, when that's possible by content, and that the system separately and reliably tells a literal repeat scan of the same request apart from a genuinely new document. These are two different senses of benefit, and both are real — they're just produced by different mechanisms under the hood.

Olga sees something else — the boundary. For semantic similarity, when you need to understand "is this the same type of form we've seen before," one mechanism is needed — search by caption, reusing this session's entire text-search apparatus. For literal similarity, when you need to understand "is this the exact same document, just re-shot or recompressed," a different mechanism is needed, and it's cheaper at that — a short numeric fingerprint with not a single call to a model.

And here's the principle worth carrying out of this case beyond any specific tool. The architectural idea "compare data in its own space, bypassing a text retelling" can be correct in itself and still have no ready-made working realization with a specific provider at a specific moment. Checking this takes one controlled experiment — feed in two knowingly different inputs and compare the output — and skipping that experiment means carrying out of the session an unworkable solution that looked workable on the very first quick test.

This case stands apart from the session's four breakdowns exactly for this reason: it closes the binary-data line started two sessions ago with an honestly documented limit of the current tools; calling it a working finale would be wrong. This is exactly the discipline the day's opening promised; it isn't a weakness of today's breakdown: a gap named outright, left as an open question for the next run or for the course owner to decide whether it's worth looking for another provider — it wasn't papered over with a polished stand-in.

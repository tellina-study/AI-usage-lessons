---
id: n21
type: criteria_checklist_and_boundary
duration_min: 0.5
assertion: "A vector store is a copy of the base taken at indexing time: it holds no live link to the source, and an outdated regulation gets served back honestly, but outdated"
learning_goal: "A stale index as a typical problem of this rung (ARCHITECTURE.md §3), confirmed by logic, not by a separate measurement. The session axis's first line gets closed here. Part 2 of 2 (continuing n20 — the criterion and the boundary). Letter suffix brought to the deck's attention (tools/seminar-production/README.md §1, issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    A tile about the stale index, a tile closing the session axis's
    first line.
  backup: >
    SETKA-KEYSOV.md / rework/section-1-khranenie-bazy.md, "Nuances."
---

# A stale index — this rung's typical problem

## Assertion

A store is a copy of the base as of the moment it was put there, and reindexing doesn't happen on its own.

## Visual

> **A stale index is a typical problem of this rung, and this finding isn't specific to this one run.** A vector store is a copy of the base as of the moment it was put there: it holds no live link to the source. If the regulation in the source document has changed and reindexing hasn't run yet, the store honestly finds and hands back a chunk — just a stale one.

> **The session axis's first line is closed:** a modern model doesn't fail structurally as the base grows — it keeps getting steadily more expensive up to a certain volume, and then stops answering at all; an external store keeps cost and recall@1 = 1.0 constant at any of the sizes tested.

## Speaker notes

Separately — a stale index, a problem typical of this rung, one that doesn't need its own measurement to understand the mechanics of. A vector store is a copy of the base as of the moment it was put there: it holds no live link to the source. If the regulation in the source document has changed and reindexing hasn't run yet, the store honestly finds and hands back a chunk — just an outdated one. This is a direct consequence of the fact that the search runs against a copy. The specific implementation has nothing to do with it.

For Olga's training center, this means a store on its own doesn't solve the task of "the requester gets an up-to-date answer" — it only solves the task of "the requester gets an answer fast and cheap at any base size." Staying up to date is a separate concern: it needs a reindexing routine, run every time the source documents get updated — a single run at the store's initial build isn't enough. Skipping this step means silently getting a confident but stale answer, one that gives no sign at all of being stale: the store has no way to signal "this chunk is already three months old."

And here's the session axis's first line, the one we started today on: it looked reliable that if the base grew, we could just list all of it in the prompt, the way we did last session. It turns out: a modern model doesn't fail structurally the moment the base grows — it first gets steadily more expensive and loses accuracy, and then, past a certain threshold, stops answering entirely, physically rejecting the request. An external store doesn't notice that threshold at all: cost and recall@1 stay constant at any of the four sizes tested, including the one where prompt-stuffing has no working answer left.

Next — the session's second case: how to split a document into chunks so that a chunk doesn't lose its meaning.

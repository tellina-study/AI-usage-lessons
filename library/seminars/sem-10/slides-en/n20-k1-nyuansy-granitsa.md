---
id: n20
type: criteria_checklist_and_boundary
duration_min: 0.5
assertion: "A store pays for itself through the base's growth, not through its mere existence: at ten documents the difference is non-critical, at five hundred there's nothing to compare it against"
learning_goal: "Case 1's boundary in direct form (A7): 'when it's needed · when it isn't.' Part 1 of 2 (n21 — stale index and closing the session axis's first line): split because the 15pt type floor leaves no room for the boundary and two conclusions on one slide (issue #311)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    The criterion on its own tile at the top, a two-column table "when
    it's needed · when it isn't" below.
  backup: >
    The criterion and the boundary — SETKA-KEYSOV.md / rework/
    section-1-khranenie-bazy.md, "Nuances," numbers are the same four base
    sizes as n10/n13, without repeating the full table.
---

# When a store pays off, and when it doesn't

## Assertion

A store pays for itself through the base's growth, not through the mere fact that a base exists.

## Visual

> **Criterion.** An external store pays off when the base's growth makes prompt-stuffing either noticeably more expensive or structurally impossible — not through the mere fact that a base exists.

| When it's needed | When it isn't |
|---|---|
| The base grows noticeably faster than once a year, and the count runs into hundreds of documents | The base is the same ten-to-twenty FAQ items as last session, and isn't planning to grow |
| The call's cost is already measurably above zero and shows up on a monthly bill | The cost difference ($0.0002 vs. $0.00005) still doesn't justify a separate preparation step |
| The base's size could one day exceed the model's context | The context limit is far off, with no structural failure in sight |

## Speaker notes

The boundary — in direct form, both sides: when it's worth setting up a store, and when that's premature complexity.

A store is worth setting up when the base grows noticeably faster than once a year and the document count runs into the hundreds, when the call's cost is already visible on a monthly bill for model calls, and when the base's size could in principle one day exceed the model's context — that is, when that risk is no longer hypothetical: we just saw it happen at five hundred documents.

A store isn't needed when the base is the same ten-to-twenty FAQ items we worked with last session, and isn't planning to grow. At that base size, the cost difference between prompt-stuffing and a vector store — $0.0002 against $0.00005 per question — exists, but it isn't large enough to justify a separate data-preparation step before the first question even arrives. Setting up a separate store for ten FAQ items isn't justified by the mere fact that they exist.

The criterion is deliberately phrased around the base's GROWTH: the mere fact that it exists plays no role here — and that runs against the intuition that pulls toward setting up a store "for the future," in advance, just because a base exists at all. The engineering price of that foresight isn't zero: a separate chunking step, a separate embedding call for every chunk, separate storage infrastructure — and all of it before the first question that would actually require it ever arrives. The criterion answers the question of "when" — there's no "whether it's possible at all" question here, and that's exactly why it's phrased in direct form on both sides: not only when to set it up, but when to deliberately not set it up, without waiting for someone to ask "why don't we have a store?"

Next — a separate problem typical of this rung, one that doesn't depend on base size, and the closing of the session's first axis line.

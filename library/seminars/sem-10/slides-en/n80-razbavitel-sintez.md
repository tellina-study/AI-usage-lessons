---
id: n80
type: content
duration_min: 1.0
assertion: "None of today's four cases is automatically insured against this just by the fact that it uses search"
learning_goal: "The interlude's synthesis: why this concerns all four of the session's cases. The recall/rank metric criterion is explicitly named as insufficient on its own. A bridge to S12 (quality evaluation and the kill switch) is named, without revealing its mechanics."
visual:
  pattern: content
  primary: >
    A synthesis tile (why it concerns all 4 cases), a tile on why this
    isn't a reason to give up on search, a bridge tile to a future rung.
  backup: >
    SETKA-KEYSOV.md / rework/section-5, "Why this concerns everyone" +
    "A nuance for the interlude," verbatim. The mention of S12 —
    ARCHITECTURE.md §1 (rung 6 of the arc's ladder), without revealing
    the evaluation/kill-switch mechanics.
---

# Why This Concerns All Four of Today's Cases

## Assertion

An outdated regulation, a mislabeled document, a document that contradicts a newer one — any of them can be found with a high rank and offered up as grounds for an answer.

## Visual

Neither Case 1 (storage), nor Case 2 (chunking), nor Case 3 (search), nor Case 4 (image search) is automatically insured against this just by the fact that they use search instead of handing the model the entire volume of data at once. A search that correctly found the chunk closest in meaning — exactly what the recall and rank metrics measured across all four cases — only answers the question "is this similar to what was asked"; it doesn't touch the question "is this correct."

> This isn't a reason to give up on searching the knowledge base — giving it up would send the session back to prompt-stuffing, which Case 1 already showed to be a losing option as the base grows. This is a reason for a separate step that the next sessions on this arc build separately: quality evaluation and a kill switch for an answer built on material that was found.

## Speaker notes

An outdated regulation, a mislabeled document, a document that contradicts a newer one — any of them can be found by a search system with a high rank and offered to the model as grounds for an answer. None of today's four cases is automatically insured against this just by the fact that it uses search instead of handing the model the entire volume of data at once. The metrics we measured all day — recall and average rank — only answer the question "was a chunk similar in meaning found," and not one of them answers the question "is the content of that chunk correct."

It's important not to draw the wrong conclusion from this. This isn't a reason to give up on knowledge-base search, which we've worked through all day — giving it up would send the session back to prompt-stuffing, and Case 1 already showed with a number that this option doesn't survive the base growing. This is a reason for a separate step that this arc of sessions keeps building further on — it isn't bounded by today's scope: the previous session already started laying down answer-checking before sending, and one of this arc's next steps is quality evaluation and a kill switch for an answer built on material that was found. This is a separate rung that doesn't get built in automatically just because the search succeeded — it has to be built separately, and we'll do that in one of the coming sessions.

It's worth ending this breakdown with a practical observation you can take away right now, without waiting for future sessions. If you build a knowledge-base search system right now and add nothing else to it, the result will honestly work exactly within the bounds of what today's metrics measured — recall and average rank. These metrics answer a good and necessary question, but not the question that actually worries the requester: is the answer right. Keeping this difference in mind is already enough protection against the single most common perception mistake: mistaking "the process found a suitable document" for "the process gave a correct answer."

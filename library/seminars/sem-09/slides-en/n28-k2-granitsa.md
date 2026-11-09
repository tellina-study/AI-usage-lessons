---
id: n28
type: criteria_checklist_and_boundary
duration_min: 1.5
assertion: "Keeping the whole knowledge base in the prompt makes sense as long as three conditions hold at once: the base is small, it's edited rarely relative to the cache's lifetime, and it's split into blocks that don't burn the cache on every edit"
learning_goal: "Case 2's boundary, stated plainly (A7): 'when it's needed · when it isn't', three conditions and one shared conclusion if any is violated. The second and third conditions now rest on our own measurement (K2-19) -- the first is still outside, and that's named directly (a gap per form §5.17)."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    The criterion as its own banner on top, below it a two-column table,
    "when keeping it all in the prompt makes sense · when to separate
    storage" -- a strict contrast, three rows for the three conditions --
    then a banner naming the gap, and a line on the arc's next rung.
  backup: >
    THE THREE CONDITIONS -- from SETKA-KEYSOV-S9.md, section "Case 2",
    beat "Nuances", item 3, with an edit: the second and third conditions
    now have a number of their own (K2-19), the first stays outside --
    that gap is named with substance on the frame (§5.17), not with a
    "we probably missed something" caveat.

    THE FIRST CONDITION GOT A PARTIAL NUMBER (new compared to the earlier
    edit). We still have no run of our own on the reading effect (the
    middle's dip on short items). But we now have a number about SIZE: the
    session's real knowledge base (266 words, 10 items) is 851 tokens at
    Anthropic, 547 at Gemini, 549 at OpenAI
    (`stend/zamery-k2-kesh/README.md`, Table 7). This isn't a measurement
    of the reading effect -- it's a measurement of how SMALL the base is
    relative to the caching thresholds: at two providers out of three it's
    below the caching threshold, which is "small" in one sense and
    "unknown" in another (the reading effect isn't measured). Both facts
    stand on the frame separately, with no mixing.

    THE THIRD CONDITION WAS REWORDED under the K2-15 correction: the
    earlier edit only said "edited rarely relative to the cache's
    lifetime" -- now it adds "and split into blocks that don't burn the
    cache on an edit", because the measurement showed that edit frequency
    isn't the only variable: block layout alone makes a 9.8x difference at
    the same edit frequency.

    CHECKED WORD FOR WORD AGAINST THE SESSION'S BRIDGE. `n78-mostik-k-
    s10.md` carries the same three conditions in the same list -- the
    rename and the edit to conditions 1 and 3 are synced there in this
    same edit (K2-1, K2-19).

    RUNG 4 IS NAMED WORD FOR WORD per `sem-07/KONTSEPTSIYA-7-12.md` §6:
    the rung's name is "knowledge outside the prompt", the rung's question
    is "where does the process get its facts from, and why does it treat
    them as true".

    This frame has numbers of its own for the second and third conditions
    out of three; for the first, only a size number, not an effect number.
---

# When to Keep the Knowledge Base Whole in the Prompt

## Assertion

Three conditions, and they only work together. Break any one of them, and separating the knowledge base's storage from each call pays off better.

## Visual

> **Criterion.** Keeping the knowledge base whole in the prompt makes sense as long as all three conditions hold at once. The moment any one of the three breaks, it pays off better to separate the base's storage from each call.

| When keeping it all in the prompt makes sense | When to separate storage from the call |
|---|---|
| The base is small -- small enough that a dip from an item's position isn't visible yet. Our knowledge base (266 words) is below the caching threshold at two providers out of three -- small in the sense of size; the effect on READING hasn't been separately measured on it | The base has grown to a size where the middle of the list stops reading well, and it now has more items than a person is willing to rearrange by hand |
| The base changes rarely compared to the cache's lifetime, and the edit is laid out in blocks that don't burn the whole accumulated cache | The base is edited more often than the cache can pay for itself, or the edit sits inside the same block as the breakpoint: writes happen, reads don't, and every request costs more than it would with no cache at all -- a difference of up to 9.8x from block layout alone, at the same edit frequency |
| The model handles a direct answer from the base with no extra check | A direct answer isn't enough: you need to pick the right chunk, check the answer, or cite the source it was answered from |

> **Where this boundary has no number of our own.** The reading effect (the first condition) stays an outside measurement -- Liu and co-authors, a list of twenty documents of academic length, not our own ten everyday items. We know the direction of the effect; we don't know its size on our own material. Size (does our text reach the caching threshold) and edit price (block layout) now have a number of their own.

> **Where this leads.** The rung this boundary opens onto is called "knowledge outside the prompt", and it has one question: where does the process get its facts from, and why does it treat them as true. That's where the next session starts.

## Speaker notes

This is the breakdown's boundary, and I'll name both sides directly.

Keeping the knowledge base whole in the prompt makes sense as long as three conditions hold at once. The conditions only work together: break any one of them, and it pays off better to separate the base's storage from each call.

The first condition is that the base is small. Here we now have a partial number, and I'll keep the two senses of "small" apart so they don't get mixed up. Our real knowledge base -- two hundred sixty-six words -- weighs eight hundred fifty-one tokens at Anthropic, five hundred forty-seven at Gemini, five hundred forty-nine at OpenAI. The caching threshold at Gemini and OpenAI is above that number -- in the sense of "does it reach the caching threshold", our base is small at two providers out of three. But the effect on READING -- the dip in the middle of the list -- we haven't measured on short everyday items: size and the reading effect are two different questions, and the second still has no number of its own.

The second is that the base changes rarely compared to the cache's lifetime, and now I'm adding the second half of that condition: the edit has to be laid out in blocks that don't burn the whole accumulated cache. We measured that this isn't a minor detail: the same edit frequency costs 0.13 times a direct read with one block layout, and 1.27 times with another -- a difference of 9.8 times.

The third is that the model handles a direct answer from the base with no extra check. This breaks once a direct answer stops being enough: you need to pick out the right chunk, check the answer before sending it, or cite the item it was answered from.

And where the boundary leads. The rung that starts wherever any one of these three conditions breaks is called "knowledge outside the prompt". It has one question: where does the process get its facts from, and why does it treat them as true. That's exactly where the next session begins.

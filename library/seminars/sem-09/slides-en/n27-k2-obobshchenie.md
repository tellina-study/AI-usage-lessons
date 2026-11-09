---
id: n27
type: content
duration_min: 1.5
assertion: "Text inserted into a prompt whole has not only content but also a place -- for both reading and price -- and both properties survive even when the prompt gets only a retrieved chunk instead of the whole base"
learning_goal: "The case's conclusions (K2-20, review 2026-10-29: the earlier frame, 'task class: an item's placement in the prompt', was dropped entirely -- the owner called the case's ending wrong). Two conclusions -- reading and caching, each with its own baseline -- plus a mandatory caveat on applicability beyond today's small knowledge base."
visual:
  pattern: content
  primary: >
    Two conclusions as banners, one under the other (reading, price),
    below them a highlighted caveat on applicability to a large knowledge
    base and to RAG, and a closing line with the case's own tally.
  backup: >
    THE OLD FRAME WAS DROPPED ENTIRELY (K2-20): "Task class: an item's
    placement in the prompt", the framing around Lost-in-the-Middle theory
    (Salvatore and co-authors), and the tie-in to the session's axis. The
    owner called the case's ending wrong directly, without specifying what
    exactly was wrong -- everything was dropped, including the theory
    inset. The theoretical part (the U-shaped curve as a property of how
    the model was trained, not a bug in one architecture) MOVED into the
    fifth column of the n21 breakdown (K2-6), where it already sits next
    to the action it explains -- it isn't carried back here a second time.

    TWO CONCLUSIONS, not one: the case checked two different properties of
    the same text -- how it's READ (an outside measurement, Liu and
    co-authors, not our own run) and how much it COSTS (our own run, 119
    calls, five providers). Keeping them apart is mandatory: the first has
    no number of our own on our material, the second does, and mixing them
    would pass the first off as measured.

    THE MANDATORY CAVEAT (K2-2, K2-20): the findings stay relevant even
    once the knowledge base outgrows the prompt and only a retrieved chunk
    gets put in (RAG, next session's case) -- a list assembled from chunks
    has the same placement physics and the same cache breakpoint as a list
    sitting whole in the prompt. The only difference is who decides which
    chunks make it into the list -- not whether the same rules apply to
    that list.

    THE CASE'S TALLY closes this session's throughline the same way the
    other five breakdowns do: a number of cases named, a number of
    mismatches with the expectation named.
---

# The Case's Conclusions: Text Has Content, and It Has a Place

## Assertion

Text inserted into a prompt whole spoils an answer not only when the needed item is missing -- but also because of where that item sits. Placement has a reading price, and separately, a money price.

## Visual

> **Conclusion 1 -- reading.** The start and the end of a list read better than the middle; what reads worse is what IS in the list (Liu and co-authors, an outside measurement -- we have no run of our own on our knowledge base's short items).

> **Conclusion 2 -- price.** A cache read costs 0.107 of a direct read -- the savings are confirmed by our own run. But at Anthropic it only holds with a correctly set breakpoint: block layout changes the price of the same call by 9.8 times.

> **Applies beyond today's small knowledge base too.** A list assembled from retrieved chunks (lookup against an external store -- next session's topic) has the same placement physics and the same cache breakpoint as a list sitting whole in the prompt. The difference is in who decides which chunks make it into the list; the rules for the list itself are the same.

> **The case's tally.** Two separate measurements, 203 calls (119 -- caching, 84 -- the five structuring directions), and not one structuring direction cleaned up the number-comparison error found in Case 1.

## Speaker notes

Let's fold this breakdown into a statement you can take away and apply to your own process, without remembering a single node's name.

The first conclusion is about reading. Text inserted into a prompt whole spoils an answer not only when the needed fact is missing from it -- it also spoils the answer because of WHERE that fact sits. The start and the end of a list read better than the middle, and what reads worst is exactly what IS in the list. This is an outside work's measurement, not ours: we have no run of our own on our own knowledge base's short items, and I'm saying that directly, not masking it.

The second conclusion is about money, and here we do have a number of our own. A cache read costs one point zero seven hundredths of a direct read -- verified against real bills, not an expectation. But at Anthropic, that saving only turns on with a correctly set breakpoint: the same edit, depending on how the text is split into blocks, costs either 0.13 times a direct read or 1.27 times -- a difference of 9.8 times in the price of the same call.

And the mandatory caveat, without which these two conclusions would look like a case about a small knowledge base that's about to run out. That's not so. Imagine the knowledge base has grown large enough that it no longer fits whole into the prompt, and only a retrieved chunk makes it in for each question -- that's the next rung of the arc, lookup against an external store. A list assembled from retrieved chunks is built exactly the same way as a list sitting whole in the prompt: it has a start, a middle, and an end, and the same cache-breakpoint rule applies to it no less. The only difference is who and how decides which chunks make it into that list -- not whether the list obeys the same rules.

And last -- the tally. Two separate measurements in this case, two hundred three calls between them, and not one of the five tested directions of prompt structuring cleaned up the number-comparison error we found back in the session's first breakdown. A well-built prompt solves its own problems and doesn't solve someone else's.

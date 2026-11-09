---
id: n78
type: bridge_forward
duration_min: 2.0
assertion: "Today the whole knowledge base lived inside the request to the model; the next rung begins with the criterion at which holding it that way stops being reasonable"
learning_goal: "Closing out the session and setting up the next one. Rung 4 is named by its own name and its own question; what gets promised is exactly what's already guaranteed on S10 — the crossover criterion, named today. Separately stated: what S10 does not fix."
visual:
  pattern: bridge_forward
  primary: >
    The next rung's question on its own card, below it the three
    conditions of today's criterion as a list, below that a line on what
    moving the knowledge base outside does not fix.
  backup: >
    THE PROMISE'S CONTENT IS DELIBERATELY TRIMMED, and here's why. The S8
    bridge, in this exact spot, promised the room four topics ("condition
    versus switch, classification as a separate step, an input that fits
    no branch, visibility of parallel branches"), pulled from the draft
    distribution `sem-07/KONTSEPTSIYA-7-12.md` §7 — and all four were
    later removed by owner decision 2026-10-24; the slide
    `sem-08/slides/n57-mostik-k-s9.md` still promises what's been removed
    (an open item in `ARCHITECTURE.md` §2 and §9.2). So here, the slide
    carries only what's backed by decisions, not by a draft: (1) rung 4's
    name and question — VERBATIM from §6 of the same concept, and §6 was
    rewritten by a direct owner decision; (2) the crossover criterion —
    from the "nuances" beat of the "Prompt Optimization" case study
    (renamed K2-1, revision 2026-10-29; `SETKA-KEYSOV-S9.md`, Case 2, item
    3), meaning it was already named in this very session and the room
    has already heard it; §7 states outright that S10 begins with exactly
    this criterion.

    THE SECOND CONDITION WAS REWORDED (K2-15, K2-19): the previous version
    carried the blanket claim that "any edit made before the cache
    breakpoint busts the whole accumulated cache" — a rerun (119 calls)
    showed that's only true for the layout "knowledge base as a single
    block," and false as a general rule: with a knowledge base split into
    several blocks, with the breakpoint on the newest, last one, the old
    cache survives. The condition was checked word for word against n28.

    WHAT'S NOT HERE, AND WHY. The mechanics of the next session (vector
    storage, loops over items, the retrieval step) live in §7, marked
    "draft, still being refined" — they don't go on the slide, or S8's
    mistake would repeat. Conversation memory, a model with authority,
    and quality scoring for a step aren't mentioned at all: those are
    rungs 5 and 6, sessions S11 and S12.

    A SEPARATE, HONEST LINE states that moving the knowledge base outside
    does NOT fix the three findings from the "Answer Reproducibility"
    case study — verbatim from its own "nuances" beat, item 4
    (`SETKA-KEYSOV-S9-part2.md`): there's still no recalculation formula,
    the threshold still has to be applied, and the two knowledge-base
    items still have to be reconciled.
---

# What's Next

## Assertion

Today the knowledge base lived entirely inside the request. The next session begins exactly where holding it that way stops being reasonable.

## Visual

> **Where does the process get its facts from, and why does it treat them as true?**

Keeping the knowledge base entirely inside the request is reasonable for as long as all three conditions hold:

- the knowledge base is small enough that a dip caused by an item's position in it isn't visible yet;
- the knowledge base changes rarely compared to the cache's lifetime, and is laid out in blocks that don't burn the cache on an edit;
- the model handles a direct answer from it without needing an extra check.

> The moment any one of the three breaks, it becomes cheaper to separate the knowledge base's storage from every call. That's where the next session begins.

> And what this doesn't fix: there still won't be a recalculation formula in the knowledge base, the threshold will still have to be applied, and two knowledge-base items will still have to be reconciled.

## Speaker notes

What we're ending with, and what we were missing today.

All day, the training center's knowledge base sat inside the request to the model. That's a perfectly normal setup for the knowledge base we actually have: a few dozen short items that change once a semester. And it comes with exactly three conditions, and we named all three today while working out what breaks down in a large knowledge base before it even runs out of room.

Condition one: the knowledge base is small enough that it doesn't yet show a dip from an item's position in the list — and that dip shows up on a topic that IS in the knowledge base, precisely because of where it sits. Condition two: the knowledge base changes rarely compared to the cache's lifetime, and an edit is laid out in blocks that don't burn the whole accumulated cache — we measured this today: the cache holds or breaks depending on how the text was split into blocks before the edit. Condition three: the model handles a direct answer from this knowledge base, and no extra check on the answer is needed.

The moment any one of the three breaks, it becomes cheaper to separate the knowledge base's storage from every call. The question that comes up right then is exactly the fourth rung's question: where does the process get its facts from, and why does it treat them as true. Today, the answer to the second half of that question was simple: the facts sat right in front of us, in the text of the request, and we could read every one of them. The moment the knowledge base moves into a separate store, reading all of it at once is no longer possible, and a new kind of question appears — whether the right piece was found at all.

And I'll say one thing up front, so as not to leave a false promise standing. Not one of today's three findings about reproducibility gets fixed by the next session. A recalculation formula for missed classes won't appear in the knowledge base just because the knowledge base moved outside: it simply isn't there, and composing the answer will still have to happen. The three-thousand-ruble threshold will still have to be applied exactly the same way, and it still can't be left to the model to apply. Two knowledge-base items that contradict each other in a single answer will stay two items that need reconciling. What fixes this is exactly what we worked through today: a deterministic check of the content before sending, and an explicit refusal to answer where there's no answer to give. The next session solves a different problem — the knowledge base's size and how it gets updated — and confusing the two problems is expensive.

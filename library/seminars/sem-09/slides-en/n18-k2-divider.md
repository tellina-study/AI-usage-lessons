---
id: n18
type: case_divider_quote
duration_min: 0.5
assertion: "Some answers come back wrong not because the right item is missing from the knowledge base, but because of where in the prompt it sits"
learning_goal: "Case 2 divider (renamed K2-1: 'Knowledge Base in the Prompt' -> 'Prompt Optimization' -- the old name is now taken by Case 1 and means something else there). Text form is NUMBER (BRIEF §4a, P3). The number here sets up the problem (how much goes to the model on every request), not a measured outcome."
visual:
  pattern: case_divider_quote
  primary: >
    Dark background, a pair of numbers large on one banner -- the client's
    question against the knowledge base that travels with it. Below, the
    six-case track for the session, the second one highlighted.
  backup: >
    RENAMED (K2-1, owner review 2026-10-29). The old name "Knowledge Base
    in the Prompt" is dropped: it's already taken by Case 1 (there, the
    knowledge base is the subject of the first breakdown) and meant
    something different there. The new name, "Prompt Optimization", names
    the actual action the case is about: not "the base is growing", but
    "the prompt carrying that base has to be put together correctly".

    THE CASE'S MEANING WAS REWRITTEN (K2-2, K2-3). The old frame --
    "the knowledge base is growing, and it's unclear where to put a new
    item" -- is dropped as too soft. The real frame: THE PROBLEM is that
    some answers come back wrong; THE SOURCE is the knowledge base itself,
    not its absence (that's exactly what the breakdown on n21 shows: an
    item that IS in the knowledge base can be read worse than if it weren't
    there at all); THE HYPOTHESIS is that the prompt needs to be optimized
    -- how the knowledge base is laid out, where it sits, how it's handled.
    The knowledge base keeps growing and STILL fits whole inside the
    prompt -- this isn't a case about a small base kept small for
    simplicity; it's a case about text having a physical layout independent
    of its size: the same thing holds once the base outgrows the prompt and
    only a retrieved chunk makes it in (RAG) -- the assembled prompt still
    has to be laid out well.

    The divider NAMES the problem (A2) but doesn't give away the mechanism
    (why exactly placement spoils the answer) or a measured result -- that's
    n21 and onward.

    WHERE THE NUMBERS COME FROM. Both are computed from the real prompt
    text -- `stend/zamery-k2-kesh/baza.py` (Case 2's ten real items) and
    `stend/sborka.py`, function `kb_text`. The knowledge base as it sits in
    the prompt (header plus ten items, full text) -- 229 words, 1665
    characters (`stend/zamery-k2-kesh/README.md`, Table 7). The question on
    the banner is a real question from Case 1's first run
    (`stend/README.md`, `IN_KB_QUESTIONS`), six words.

    This is NOT a measurement of model behavior: there isn't a single run
    behind these two numbers -- they describe the size of what goes to the
    model. Case 2 NOW HAS its own measurement (K2-19, see the beats
    further on -- 119 calls across five providers on caching plus 84 calls
    on five structuring directions) -- but not on this frame; the divider
    doesn't present it.

    The name in the case track in `rendered/deck-config.yaml` (`case_track`)
    needs the same rename applied in sync -- flagged to the orchestrator
    separately.
---

# Case 2. Prompt Optimization

## Assertion

Some answers come back wrong -- and not because the right item is missing from the knowledge base. It's there. The problem is where it sits.

## Visual

> **6 words -- the client's question. 229 words -- the knowledge base riding along with it.**

> "How do I reschedule a class if I'm sick?" -- six words. To answer them, the process sends the model the whole knowledge base: a header, ten items, full text, on every single request. The knowledge base keeps growing -- and it still fits whole inside that same block of text.

## Speaker notes

The process learned to answer on its own, and in the last breakdown it honestly admitted when a topic wasn't in the knowledge base at all. Now let's take on a more uncomfortable question: what happens to the answer when the right item IS in the knowledge base.

The mechanics are simple. The model has no memory of past requests and no access to our files. The only way to let it know the training center's rules is to put those rules into the very same text the client's question travels in. So every single request sends one long message: first an instruction on who the model is and what it does, then the whole knowledge base, then the person's question.

Compare the two sizes. The question "how do I reschedule a class if I'm sick" is six words. The knowledge base riding along with it is two hundred twenty-nine words -- ten items, full text, with all the deadlines and caveats. This isn't a rare case or a hard question -- this is what every single request looks like, including the most trivial one.

The knowledge base keeps growing -- Olga keeps adding topics the process used to honestly answer "I don't know" to. And here's exactly why we're back on this topic. As long as the knowledge base lived in a document on someone's desk, the order of its items was a matter of convenience: a person would find what they needed anywhere in the list. Once that same knowledge base rides whole into the model as one block of text on every single request, an unpleasant thing turns up: some answers come out wrong not because the item isn't there, but because it sits in an unlucky spot in the list. A knowledge base that has content turns out to be a text that also has a location.

And this isn't a case about a small knowledge base you could just stuff into the prompt for simplicity. Our knowledge base is still small and fits in whole for now -- but the same mechanics are waiting for us once the knowledge base grows large enough that the whole text no longer fits in the prompt: only the chunk retrieved for the specific question will make it in. The assembled prompt still has to be laid out well -- the question of placement doesn't go away when the question of size does.

That's what this case is about: how the knowledge base is laid out inside the prompt, and what that layout actually decides.

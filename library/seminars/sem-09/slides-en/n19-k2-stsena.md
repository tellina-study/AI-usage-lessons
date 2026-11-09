---
id: n19
type: problem_scenario
duration_min: 1.5
assertion: "Olga adds new topics to the knowledge base following questions the process didn't answer -- and every item she adds travels to the model along with all the others, inside the same text the client's question rides in"
learning_goal: "Case 2's scene beat (renamed K2-1: 'Prompt Optimization'): a live staging of Olga's need plus the S1 schema -- solid for the process that already exists, dashed for what this case adds (Olga manually extends the knowledge base, which then enters the model call as part of the prompt). No solution version, no outside numbers: this is the setup, not the breakdown."
visual:
  pattern: problem_scenario
  figure: k2-shema-postanovka-en.png
  primary: >
    On top -- the S1 schema (issue #303, now a real PNG, not text panels):
    a solid line for request -> classify -> model answers from the
    knowledge base -> answer (the already-existing process, unchanged).
    Separately, dashed -- "Olga extends the knowledge base", a dashed arrow
    from this block feeding into the "model answers" block: this is exactly
    what the case is about to examine -- how the knowledge base's contents
    get into the call. Below that -- an inset frame with the setting, a
    numbered timeline of the knowledge base's growth, a closing banner on
    cost, and Olga's own line asking for help. Not a single run number on
    the frame.
  backup: >
    SCHEMA S1 ADDED (review 2026-10-29, K2-4): the frame used to open
    straight into the inset frame with no process schema -- a violation of
    S1 (`forma-keysa-s-zamerom.md` §2), flagged in BRIEF §2a as violated in
    Case 2. BROUGHT UP TO A PNG by the designer pass (issue #303, "half the
    cases open with a description instead of a schema"):
    `rendered/make_figures_k2.py` `postanovka()`, the same visual grammar as
    `k4-shema-postanovka.png` (solid teal for the existing process, dashed
    gold for what the case builds and examines). The text quote blocks
    "Existing process (solid blocks)" and "What we're adding (dashed)",
    which used to carry this device in prose, are dropped as duplicating:
    the same thing now reads straight off the schema.

    The dashed block is deliberately named as Olga's ACTION, not a property
    of the process: "Olga extends the knowledge base" -- what this case
    goes on to examine (how this addition physically ends up inside the
    model call), not a new node on the canvas. The canvas the room saw in
    Case 1 has no dashed block and never will -- K2-22/n24 separately says
    the canvas doesn't change at all.

    The dashed block is deliberately named as Olga's ACTION, not a property
    of the process: "Olga manually extends the knowledge base" -- what this
    case goes on to examine (how this addition physically ends up inside
    the model call), not a new node on the canvas. The canvas the room saw
    in Case 1 has no dashed block and never will -- K2-22/n24 separately
    says the canvas doesn't change at all.

    The need is from SETKA-KEYSOV-S9.md, section "Case 2", subsections
    "Entry form" and "Setup": Olga keeps extending the knowledge base
    (loyalty program, referral discount, demo class), the new item gets
    appended to the end of the current list, and nobody worries about the
    order items land in inside the prompt.

    The three new topics are named exactly as in the grid, and they're also
    the three out-of-base questions from Case 1's first run
    (`stend/sborka.py`, `OUT_OF_KB_QUESTIONS`). The seam inside the session
    comes free, with no stretch: the room already saw these three questions
    on screen during the "Answer or Stay Silent" breakdown.

    The character is Olga, the training-center administrator (A13), and
    the same workload as in Case 1's scene (`n06-k1-stsena.md`): twenty
    requests a day.

    THE FRAME WAS RESET AROUND A NEW PROBLEM (K2-2, K2-3): the scene now
    explicitly says the issue isn't just new items -- some answers about
    old, long-standing items can also come back wrong because of where
    they sit in the list. This is NOT measured on the scene frame -- the
    claim belongs to the breakdown (n21) and is measured there; here it's
    named as the need Olga puts into words as a question, not as our own
    experience.

    WHAT IS DELIBERATELY MISSING HERE. The grid in "Entry form" states it
    more strongly: "the base grew, and answers got worse on what's ALREADY
    in it". The numbers behind that claim come from an outside measurement
    (Liu and co-authors, breakdown on n21) -- the scene frame carries no
    outside name; that name shows up where the measurement itself does.

    Flagged to the orchestrator as a report: the softened entry-form wording
    is kept from the earlier edit (the number isn't ours), the problem frame
    has been reset (K2-3).

    EN FIGURE NOTE (Bilingual Production Rule, issue #172/#319): the EN
    slide uses k2-shema-postanovka-en.png, a direct English-text redraw of
    the same schema (same layout, same colors, same solid/dashed device),
    generated by running `python3 make_figures_k2.py --lang en` -- the
    same `postanovka()` function, driven by the shared `fig_strings_en.py`
    dictionary (`tools/seminar-build/fig_toolkit.py`), not a second,
    hand-written `_en()` function. This figure carries Russian-language
    labels in the original ("Ольга дополняет справочник", etc.) and needs
    redrawing, unlike n23's figure (a real screenshot of the live rig, kept
    unredrawn in both languages -- see glossary.en.yaml).
---

# The Knowledge Base After a Month of Work

## Assertion

Every question the process honestly didn't answer turns into a new knowledge-base item -- and some answers about what's already in the knowledge base still come back wrong.

## Visual

> A month later. Still twenty requests a day.

1. Every question the process didn't close, Olga works out by hand and writes up as a new knowledge-base item -- that's how the loyalty program, the referral discount, and the demo class got added over the month, exactly the three topics the process honestly said "I don't know" to.
2. She adds them to the end of the list, the way you'd add a line to any text file -- nobody decides exactly where an item lands: the knowledge base's order is just the history of what order Olga ran into the questions in.

> **What the training center pays for.** The knowledge base travels to the model whole, and you pay by its length -- the more topics, the longer even a trivial call gets.

> Olga says: "I just add it to the end, like a file. I don't get why it sometimes answers wrong about something that's definitely written down."

## Speaker notes

A month has passed. The process works: it answers questions from the knowledge base on its own, and for everything else it honestly says a human will answer and calls Olga in. Still the same twenty requests a day.

At the top of the screen is the same process we built in the last breakdown, in solid blocks: a request comes in, gets classified, the model answers from the knowledge base, the answer goes out. None of that changes today. Separately, dashed, is what we're actually going to dig into today: Olga manually extends the knowledge base by hand, and that addition enters the very same model call as everything else.

This work has a side effect, and it's a good one. Every question the process didn't close, Olga closes by hand -- she checks with her manager, looks at the contract, confirms with the academic office. And having worked it out, she does the obvious thing: she adds a new item to the knowledge base, so the process closes that question itself next time. Over the month this is how the loyalty program, the referral discount, and the free demo class appeared -- exactly the three topics we watched the process honestly say "I don't know" to.

The mechanics of adding are simple: Olga opens the field, scrolls to the end of the list, and adds a line. Exactly the way you'd add to a notebook or a text file. Nobody decides exactly where in the list an item lands -- the knowledge base's order is just the history of what order Olga ran into the questions in.

The cost of this is direct: the knowledge base travels to the model whole on every request, and you pay per request by the length of what you send. The better the process gets -- the more topics in the knowledge base -- the longer every call gets, including a call about a one-line question.

But there's a second part, and it's the reason we're here today, and it can't be explained away by the knowledge base simply growing. Olga notices: sometimes the process answers wrong even about something that's definitely in the knowledge base, has been there a while, and looks no different from any other item. As long as the knowledge base lived in a person's head or in a document, the order of its items meant nothing: Olga would find what she needed anywhere in it. The moment that same knowledge base became a block of text inside a call to the model, an item's place in that text started to have consequences -- and that's exactly what we're digging into today.

---
id: n03
type: taxonomy_compare_table
duration_min: 2.5
assertion: "Same rung as last time: chain. Today we are not climbing to the fifth rung — we are staying on the second."
learning_goal: "A short reminder of the arc ladder, not a new introduction — the audience already saw this screen in S7. Reinforces that the 'model or code' question lives inside one rung and does not require moving to the next one."
visual:
  pattern: taxonomy_compare_table
  figure: lestnitsa-dugi-en.png
  primary: >
    The same nine-rung ladder as last session, the gold bar sits in the
    same place as last time — it has not moved. A short caption instead of
    re-explaining the whole ladder.
  backup: >
    A reminder, not re-teaching: the full introduction of the ladder and
    the rule "don't climb without a requirement the rung below doesn't
    close" already happened in S7 (sem-07/slides/n02-lestnitsa-dugi.md).
    The figure lestnitsa-dugi.png already exists in this session's
    rendered/figures/ — it is reused, not redrawn.

    EN track note (this file, issue #172/#274): the English figure
    lestnitsa-dugi-en.png is produced by the same script
    (make_figures_lestnitsa.py --lang en) through fig_toolkit's own
    set_lang/T() mechanism, not drawn separately — see fig_strings_en.py
    for the translated row and label strings. Geometry, palette, and the
    gold-bar position are identical to the Russian figure; only the
    baked-in labels differ. Seminar numbers are abbreviated "S7"/"S9"/…
    (the 290px label slot does not fit "Seminar 7") — this is this
    seminar's first EN figure to need the convention; flagged to the
    orchestrator to keep it consistent across the rest of the course's EN
    track.
---

# Same rung: chain

## Assertion

Last session built the chain from scratch. Today we are not building the fifth rung — we are staying on the second.

## Visual

> The gold bar sits in the same place as last time. Today's four cases are not a climb higher — they are what happens inside one and the same rung when new steps get added to the chain.

## Speaker notes

A quick reminder here, not a new introduction — you have already seen this exact ladder in the last session, so I am not going to walk through all nine rungs all over again from scratch.

The short version, for anyone who has forgotten the details in between. Nine rungs, bottom to top, running from simple to complex. At the very bottom sits whatever a single model call, or a search over your own documents, is enough to close by itself — that part was already covered back in the lecture, not here. One rung up from that is chain: several steps in a known, fixed order, with data handed off between them along the way. We spent the entire last session standing on that rung, and we are staying on that same rung for the whole of today as well.

It is worth saying this outright, rather than leaving it implied, because it is an easy, intuitive mistake to think that four brand-new cases and one fairly elaborate experiment in a single session must mean we have climbed somewhere higher up the ladder. We have not climbed anywhere. Route, where the category of the input itself picks which path is taken; independent checks running in parallel; loops and subprocesses; an agent that decides its own order of steps; several agents working together — every one of those is a later session, a different and higher rung entirely. Today the chain stays exactly the same by design: step after step, in a known order, nothing more exotic than that. What changes between last time and today is not the height we are standing at, but the depth of the question — we are learning to put a far more precise question to the very same device, one step at a time.

And here is why this deserves a reminder of its own, not just a passing comment on the way to the first case. Because the rule for moving up this ladder, stated plainly back in the last session, reads exactly like this: never climb without a requirement that the rung below genuinely fails to close. And every one of today's four cases turns out to be exactly that kind of requirement — something the "chain" rung did not close automatically, on its own, just by existing: a notification that does not quietly mix up facts, a check that does not restart the whole thing from zero on every repeat, a refund decision you can actually stand behind in front of someone else, image delivery that does not silently break the run. Not one of the four requires climbing higher. All four close inside that same rung we are already standing on, provided you answer one single question correctly at each step along the way.

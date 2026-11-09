---
id: n03
type: arc_ladder_recap
duration_min: 2.0
assertion: "Six rungs of trust in the model, one per session; today's is the third, answering a human"
learning_goal: "A reminder of the arc ladder, not a re-introduction. The slide carries the ladder figure: six rungs, each named by its own question, today's circled in gold, the neighbors visible — so it's clear what this session still doesn't cover."
visual:
  pattern: arc_ladder_recap
  figure: lestnitsa-dugi-en.png
  primary: >
    The ladder figure spans the full width of the slide: six rungs from
    bottom to top, each with its name and its question on one line, today's
    circled in gold. Below the figure, one line on where we stand on this
    ladder.
  backup: >
    The figure's content is VERBATIM from `sem-07/KONTSEPTSIYA-7-12.md` §6
    (the ladder was rewritten by owner decision 2026-10-24, "rewrite the
    ladder"); the same table is repeated in `SETKA-KEYSOV-S9.md`, section
    "Opening," screen 2. Not a single wording has been paraphrased: the old
    ladder was built out of tool primitives, and the cases built on it
    ended up being about the tool — the rewritten one is held together by
    questions, and the question has to sound exactly as it does in the
    concept. This has to be checked against the drawing script's own source
    (`rendered/make_figures_lestnitsa.py`), not by grepping the deck: the
    labels inside the diagram are pixels (canon §7).

    REVISION 2026-10-29 (BREAKDOWN, S8/R-5): the opening line of the notes
    was removed — "you saw this ladder last session, so I won't walk
    through the whole thing again" relied on the room's memory of last
    session, exactly what S8 forbids ("don't assume students remember
    things word for word"). The figure and the full list of all six rungs
    in the notes stay as they were — that IS the re-description S8
    requires; only the line announcing an intent not to do it was removed.

    THE PATTERN AND THE TABLE — ORCHESTRATOR DECISION 2026-10-26, in favor
    of the figure. The slide's first pass stood on `recap_table` per brief
    §4 and carried the ladder as a table. `recap_table` maps, in
    `rendered/deck-config.yaml`, to the genre `axis_table`, and
    `axis_table` is not in `genres.DRAWS_FIGURE` — the figure would never
    have been drawn ("SCHEMA WON'T MAKE IT THROUGH"), and the table would
    have duplicated it with the same six names and the same six questions.
    The pattern was swapped to `arc_ladder_recap`: this name is
    deliberately absent from the `genres` table, so it falls through to
    the genre `content`, and `content` does draw figures (a working
    mechanism of the config, not a gap — `deck-config.yaml` needs no
    edit). The table was removed from the slide by the same decision;
    `recap_table` stayed with n76, where there is no figure and a table
    fits. The six rungs and their questions now live on the slide in
    exactly one place.

    EN TRACK NOTE (this file, issue #172/#319): the English figure
    `lestnitsa-dugi-en.png` is produced by the same script
    (`make_figures_lestnitsa.py --lang en`) through the fig_toolkit's own
    set_lang/T() mechanism, not drawn separately — geometry, palette, and
    the gold-bar position are identical to the Russian figure; only the
    baked-in labels differ. An EN version of this exact figure already
    exists for sem-08's own ladder
    (`sem-08/rendered/figures/lestnitsa-dugi-en.png`); this seminar's
    version carries six rungs instead of nine, with the rewritten
    (2026-10-24) names and questions, translated into English by the same
    mechanism.
---

# Six Rungs of Trust in the Model

## Assertion

One rung per session. Today closes the third: the process answers a human.

## Visual

> Today's rung is circled in gold. The ones below it, the course has already covered; the three above are later sessions, and tonight carries none of their content.

## Speaker notes

The ladder on screen shows all six rungs at once: today's only makes sense next to the rest, so let's go through it again, in order and quickly.

The axis of the whole arc of sessions reads like this: what the process hands off to the model, and what it vouches for in return. That's why every rung is named by a question. In session seven the process made one model call and recorded the answer, and the question was the simplest one there is: can this be relied on at all. In session eight there were several calls, with data flowing between them, and the question shifted: where in this chain does the model decide, and where must code decide. We spent the whole of last session asking exactly that — once for every new step.

Today's rung, the third, is called "answering a human," and you just heard its question: the process wrote to a human — who can vouch that it's safe to send. The difference from the last rung isn't the number of nodes. The last question could be closed by looking at how the process was built: here sits the model, here sits a condition in code, the boundary is named. Today's question isn't closed by how it's built, not at all. The process can be assembled correctly, the run can be green, the log can be clean — and sending what it wrote can still be the wrong call. Today's six case studies are exactly about that.

While you're at it, look at the two rungs above, so it's clear what this session doesn't cover. The fourth is knowledge outside the prompt: where the process gets its facts from, and why it treats them as true. That's the next session, and today our whole knowledge base sits entirely inside the request to the model. The fifth is a model with authority, one that doesn't just answer but acts; today ours only answers, with a single outgoing message, with no memory of the conversation. If at some point during the session you want to ask "why not just build an agent" — that's session eleven, and we'll get there once today's question is closed.

The rule for moving up the ladder stays the same, and it's simple: it's only worth climbing because of a requirement the rung below doesn't close. The ability to answer a human is exactly that kind of requirement. The chain's six nodes don't close it.

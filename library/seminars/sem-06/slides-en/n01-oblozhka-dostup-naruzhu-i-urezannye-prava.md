---
id: n01
type: hero_cover
duration_min: 0.75
assertion: "An agent that knew everything about the project starts missing — the work has run past the edge of its context; the seminar breaks down the two opposite moves that push that edge outward, and the cost of each"
learning_goal: "A hook, not a table of contents: the seminar opens with a miss on the very project the room built up over the previous two classes, with the cost named. The seminar's question is NOT asked here — it comes on n04, after the second miss, once the shortfall has already been felt"
visual:
  pattern: hero_cover
  figure: ramka-n01-hero-sem06-en.png
  primary: >
    A dark Ocean background, the same device as the previous class's cover. A large title, and
    under it two lines: first, as a quiet aside — what happened this week; then, in a gold
    box — a short riddle of a question that the seminar answers within the next three minutes.
    The seminar's question is not on the cover at all (it is on n04). The bottom third, full
    width, is the hero diagram (at least 40% of the slide's area): on the left, a dashed card
    "the agent's context" with two lines inside it — "the repository" and "the conversation
    with you" — and a caption underneath, "past that the agent sees nothing"; from it two
    arrows to two white cards on the right: "data from outside — MCP" and "trimmed
    permissions — subagent". Under that pair — a row of four segments: the first two (hook,
    skill) filled in a muted gray with the caption "closed last time", the next two (MCP,
    subagent) filled in gold with the caption "we settle these today".
  backup: >
    The diagram is drawn programmatically (the same figure renderer that built the previous
    class's illustration) — it is not a photograph and not a screenshot. That is a legitimate
    route for a hero illustration: a diagram drawn by code does not pass itself off as an
    external source and fakes nothing, unlike a stylized card with a caption standing in for a
    real image. The four segments of the bottom row are the seminar's axis (see n03/n61), not a
    separate invention: the same order of rows as on the axis and on the map.

    The owner's round of edits (issue 225, §A2): the previous illustration ("a message" against
    "a fact") was removed entirely, together with the question it carried. The axis row was cut
    from five segments to four (§A1): the process was taken off the diagram, and the seminar's
    ladder is hook · skill · MCP · subagent.

    The storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`, reason 3 — "the opening
    is a table of contents, not a hook"; rule P2 — "every case has a person and a cost in it").
    The cover carried the seminar's question and nothing else: the room was handed the question
    before it had felt the shortfall, and the first five slides narrated the construction of the
    seminar. The cover now carries the FIRST MISS of the running story: the same project, the
    same developer, the agent answering confidently and wide of the mark, because part of the
    truth lives outside the repository; the cost is named outright (a missed deadline and a
    conversation with the client). The seminar's question moved to n04 — to the point where
    there are already two misses with opposite causes behind it. In its place on the cover
    stands a short riddle of a question, and that riddle is the hook: the agent did not get
    dumber, so what stopped fitting.

    Layout mechanics: `g_cover` sorts the lines of a quote block by whether they end in a
    question mark — those go into the gold box, the rest into a quiet aside with a teal bar.
    That is why the aside and the question stand as SEPARATE blocks, each with its own pair of
    quotation marks: splitting one quote naively down the middle would leave the opening mark in
    one frame and the closing mark in the other (a live case, n04/n63 from the same build).

    What follows from this for the other sessions: `make_deck_yaml.py` pulls
    `deck.central_question` from the question in the gold box of the COVER. After this edit what
    stands there is the riddle, not the seminar's question; the discrepancy is named outright,
    and the decision belongs to the consolidation session.

    The tracker is deliberately NOT named here. The first miss says only "not in the
    repository": the mechanism — the client's tracker and a hand-carried transfer a few times a
    week — is presented by the scene of the first case (`n10`), and a repeat would eat it.

    The post-delivery consolidation (issue 225, `qa/svedenie-posle-provedeniya.md`): the
    seminar's title was replaced with the one the owner approved — "Access to the outside and
    trimmed permissions" instead of "Access to the outside and a trimmed role". The word "role"
    was removed across the whole seminar as ours rather than the lecturer's
    (`qa/RAZBOR-PROVEDENIYA.md` §A1); substituting "subagent" directly would have produced a
    tautology, and the phrase "trimmed permissions" already lives in the material (`n04`,
    `n05`). The same edit made the caption of the hero diagram's lower-right card "trimmed
    permissions — subagent" instead of "its own role, trimmed permissions — subagent": the
    point size went up from 26 to 28 — the line got shorter, and the card settled into the same
    shape as the one above it ("data from outside — MCP"). The slide's file was renamed to
    follow the title. The diagram is drawn by `make_figures_mostik.py`.
---

# Access to the outside and trimmed permissions

## Assertion

An agent that knew everything about the project starts missing: the work has run past the edge of its context.

## Visual

> Two weeks ago the agent knew everything about this project. On Monday it answered confidently and wide of the mark.

> "The agent did not get dumber — so what stopped fitting?"

## Speaker notes


The project the seminar stands on is the course's demonstration repository `signup-landing-demo`: a landing page in its third month, and a client who pays for the work. The person is the same developer who spent two classes in a row setting up the harness for an agent here. First the hook: a short script that the harness runs by itself on a particular event, and which here rejects a write to the main branch. Then the skill: a deployment procedure that lives in a file of its own and is pulled into the context by a trigger description. By the beginning of this week the agent knew everything about the project there was to know: forty lines of instructions in `CLAUDE.md`, the hook, the skill, the decision log, and the landing page's own code. It held all of that whole and almost never missed — and that matters for what came next: the miss the seminar opens with happened with a good agent and correct instructions.

The diagram in the lower part of the cover shows what that "everything" is made of. The agent's context — the dashed card on the left — is made of two things: the repository's files, which the agent reads by itself, and the conversation with you, in which you explained something or attached something. Past that the agent sees nothing. That boundary is not configurable and does not widen under persuasion: it is that way by construction, and the two previous classes set the harness up precisely inside it. As long as all the work lay inside, the harness was enough.

On Monday the developer asked it the thing people ask every week: which of the client's requests are still not closed. The agent answered confidently and to the point — by what lies in the repository: by the code, by the history of edits, by the decision log. Two of the requests were not in that answer at all. The client had not filed them in the repository: for a month now he has been keeping his tasks in a tracker — a separate system, which the developer himself invited him into so that edits would stop getting lost in a messenger. One of the two lost requests had been expected by Monday.

The cost is named right away, because without it the story stays an anecdote. A missed deadline — and a conversation with the client in which you have to explain why what he wrote down before the work did not make it through. That conversation did not have to happen.

The agent did not get dumber. It answered with exactly what it had, and inside its own boundaries it answered correctly. Something else changed: the work stopped fitting whole into what the agent sees. For two classes in a row everything it worked with lay inside the repository, and that was enough. On Monday part of the truth turned out to be outside, and a harness inside the repository does not reach that far — not the hook, not the skill, not any number of lines of instructions.

Hence the riddle on the cover: if the agent did not get dumber, then what stopped fitting? The answer is assembled by the next three screens. First — what the project already has and why it was enough: all four things that were set up lie inside. Then the same thought on the seminar's axis: both closed rungs work inside the repository, both of today's are about its edge. And then the second miss of the same week, whose cause is the opposite: there everything needed did fit inside, and it crowded out the work that session — one run of the agent, the one you talk to by hand — was opened for. Two misses with opposite causes are what give the seminar its question, and the two moves that answer it.

The row of four segments at the bottom of the cover is the ladder these classes climb: hook, skill, MCP, subagent. The first two were broken down and measured earlier, and their wording is not rewritten here. The two gold ones are closed today.

About how trustworthy the scene is, it is worth being direct. The project is real, the situation is assembled out of typical ones: this is a teaching scene, like every scene in the seminar. Checkable numbers stand separately in the seminar and always with a source — the scenes do not belong to them. Where exactly the client keeps his requests, and how people live with that today, is what the first case of the MCP section breaks down; here only as much is said as is needed: inside the repository they are not there.

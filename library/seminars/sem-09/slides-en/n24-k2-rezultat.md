---
id: n24
type: result_preview
duration_min: 1.0
assertion: "Nothing changes on screen -- not for the requester, not on Olga's canvas -- the whole decision fit into the order of lines inside one field"
learning_goal: "Case 2's result beat. Honestly named as the only breakdown in the session with no run of its own: what the decision delivers is stated via an outside measurement with the work's name on it; what it costs is stated plainly, in our own words."
visual:
  pattern: result_preview
  primary: >
    Two mockups side by side: the answer screen the requester sees (before
    and after -- indistinguishable), and the process canvas (before and
    after -- indistinguishable). Below them, a banner on what the decision
    rests on, and a banner on its cost.
  backup: >
    The content follows SETKA-KEYSOV-S9.md, section "Case 2", subsection
    "Result": no new node is added to the canvas, the contents of an
    already-existing prompt change; the requester sees no difference.

    THE GRID'S WORDING WAS DELIBERATELY SOFTENED, and that's the main
    decision on this slide. The grid says: "as the base grows, answers on
    frequent topics don't lose accuracy -- but they would if the order
    stayed historical." As a claim about OUR OWN process, this has never
    been measured: a dedicated check on our knowledge base's short items is
    designed and hasn't been run (`[MEASUREMENT NOT READY]`, the grid's
    "nuances" beat, item 3). So the frame carries what's actually true:
    what the decision rests on (an outside work, named) and what it
    doesn't have (a run of its own).

    RENAME (K2-1): the title and visible text are brought in line with the
    case's new name, "Prompt Optimization" -- the old "Knowledge Base in
    the Prompt" is already taken by Case 1.

    THE "NO RUN OF OUR OWN" BANNER IS PLACED SPECIFICALLY HERE, not at the
    end of the case, because this is the beat where the other five
    breakdowns all carry their own numbers. An absence is better named
    exactly where it's looked for. The wording is synced with the
    session's closing -- `n76-os-zakryta.md` says the same thing with the
    same words: "there's no run of our own on this rig, the support is
    outside."

    There are two before/after mockups, and they're deliberately
    indistinguishable: that IS the content of this beat. No new figure is
    needed to assemble them -- both states are shown as text, the same way
    Seminar 8's own `result_preview` did
    (`sem-08/slides/n12-k1-rezultat-preview.md`).

    Numbers on the frame: none of our own. The outside one is only a
    reference to the already-shown breakdown (n21), with no repeat of its
    figures.
---

# What Changes for the Requester and on the Canvas

## Assertion

The requester sees nothing new. The canvas doesn't change. The whole decision fit into the order of lines inside one field.

## Visual

> **The requester's screen, before and after.** "Question: how do I reschedule a class if I'm sick? Answer: you can reschedule a class no later than 24 hours before it starts -- through your account or by messaging the administrator." Indistinguishable.

> **The process canvas, before and after.** Form -> answer node -> write a row -> result screen. Not a single new node. Indistinguishable.

> **What actually changed.** The order of lines inside one text field, and nothing else. That is the whole decision.

> **What it rests on.** An outside measurement on a list of twenty documents (Liu and co-authors), which we broke down one screen ago. **We don't have a run of our own for this specific effect.** A check on "how this works on our knowledge base's ten short items" is designed and hasn't been run, so there's no number of our own here, and there won't be. The other half of this case -- request cost and caching -- did get a run of its own, and we look at it next.

> **What it costs.** Order now has an owner: someone decides what's "important" right now and comes back to it as the knowledge base grows. Manual work that goes stale silently. And the knowledge base still travels to the model whole on every request -- request length keeps growing with it.

## Speaker notes

Let's look at what we got. And the first thing that jumps out: nothing noticeable happened at all.

The requester sees no change. They asked about rescheduling a class and got the same answer about the 24-hour rule and their account. The result screen is the same, the text looks the same, no new line, no mark.

The canvas didn't change either. The same form, the same answer node, the same row write, the same screen. Not a single new node was added, not a single new connection appeared. If you opened the process before the fix and after it, you wouldn't find a difference until you dug inside the text field.

What changed in there is the order of the lines. That's the whole decision. For an engineer this feels unusual: a decision normally looks like a new box on the schema, and the schema itself proves the work was done. Here the work is done, and the schema stays silent about it.

Now, honestly, about what this decision rests on. It rests on the outside measurement we looked at one screen ago: a list of twenty documents, the right document moved around the list, and in the middle accuracy dips below the "no documents at all" mark. This is Liu and co-authors' work.

There's no run of our own for this specific effect. We designed a check that would measure it on our own knowledge base's ten short items, and we haven't run it. So there's no number of our own here, and we're not going to put someone else's number here pretending it's ours. That doesn't mean Case 2 has no measurement of its own at all -- the other half of the case, about request cost and about caching, did get a run of its own, and we'll get to it in one screen.

Let me say why this matters specifically here. The outside measurement was done on paragraphs from academic papers, and our items are three or four lines of everyday text. The effect on a knowledge base like ours could be noticeably smaller, or it could show up sooner. Until we've measured it, the honest statement is: we know the direction, and we don't know the size on our own material.

And the price of the decision. Order now has an owner: someone decides what's important right now, and revisits it as the base grows. And the knowledge base still travels whole on every single request.

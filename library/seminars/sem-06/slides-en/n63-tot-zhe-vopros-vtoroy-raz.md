---
id: n63
type: reflection_question
duration_min: 1.5
assertion: "The same opening question, verbatim, a second time in the class; the room answers again, and it gets said out loud whose answer changed and what exactly changed it"
learning_goal: "The closing of the loop opened on n04: the question is presented verbatim a second time, character for character, and it is answered by the room rather than by the lecturer. A full breakdown of what became checkable over the class is on the next slide"
visual:
  pattern: reflection_question
  primary: >
    A reminder of the first presentation — in the quiet form of a remark, and the same place says that the room
    answers out loud. The question itself — verbatim the same as on n04, in a gold frame, as one
    sentence. There are no option cards, as there were none at the first presentation.
  backup: >
    The source: `rework/block-3-os.md` §A.3. The wording is verbatim the same as on n04 of this
    seminar, under the idea of the owner's round of edits (issue 225, §A2): the agent runs up against the boundaries
    of its own context, part of the work requires data from outside, part a separate worker
    with trimmed permissions. The room answers: first, whose answer changed, then
    two or three voices — what exactly changed it. The lecturer does not name his own answer and does not grade anyone else's.

    Storytelling revision (issue 225, `PERESMOTR-STORITELLING.md`; the handover from the opening session —
    `qa/peresmotr-otkrytie.md` §3 and §7 item 1). The opening was rewritten: the seminar's question
    is now asked on `n04` after the two misses and sounds different — "The work has run past the agent's
    context — which do you set up first: bringing inside what is not inside, or carrying outside
    what does not fit inside?". This slide was carrying the former wording ("The agent sees only
    what is in the repository and in the conversation with you. Where does that context end — and what
    do you set up first: access to the outside or a separate worker with trimmed permissions?") —
    that is, the seminar's loop was broken: a different question was standing on the screen the second time. Brought into line
    character for character.

    The second edit of the same round — the layout. `g_question` in `build_sem06.py` splits the
    block quote into the scene and the question at the FIRST sentence with a question mark. The former text held
    the question across two sentences, and what arrived on the finished PNG was a stub: "The agent sees only what…"
    went off into the quiet remark, and into the gold box went "Where does that context end…"
    with no beginning, and with an unpaired guillemet inside it as well (checked against the pre-edit snapshot).
    Now the question is one sentence, entirely inside one pair of quotes; the split runs exactly
    along the boundary "reminder | question", and the gold box holds the seminar's full question.
    The addendum "What has changed in your answer — and what exactly changed it?" was taken off the screen and
    moved into the reminder above the question: two question marks in one gold box
    read as two different questions to the room.

    Literary editing (issue 225, qa/pravki-nahodok-svedeniya.md item 3). The gold box
    of this slide is `form_question`, the deck's one and only form for a question to the room, and in it stands the
    same question in the same weight as on `n04` at the first presentation: removing the bold here
    would mean separating two presentations of one question and breaking the grammar "one job —
    one form". The form is untouched. A repetition of the headline was removed: the reminder began with the words
    "This question has already been asked at the start of the class" under the headline "This question has already been asked", and the first
    clause repeated it word for word. It became "At the start of the class you kept your answer to it to yourself"
    — the same sense, no echo. The split into the reminder and the question runs in the same place, at the first sentence with a question mark.
---

# This question has already been asked

## Assertion

The same question, verbatim, a second time: whose answer has changed — and what exactly changed it?

## Visual

> "At the start of the class you kept your answer to it to yourself. Now out loud: whose answer has changed and what exactly changed it. The work has run past the agent's context — which do you set up first: bringing inside what is not inside, or carrying outside what does not fit inside?"

## Speaker notes


The question on the screen is the same one that stood at the start of the class, character for character: the work has run past the agent's context — which do you set up first, bringing inside what is not inside, or carrying outside what does not fit inside?

It has two legitimate answers, and that is a property of the question itself. "The work does not fit" describes two different states of affairs. In the first, what is needed is not inside at all: the data lives in a system that changes without you, and no size of context will bring it in there — you can only reach it with access. In the second, everything needed does go inside and takes up the room the work was sitting in: here what helps is somebody else's context, where the reading is done for you and a short result comes back. Which answer is right is determined by which of the two states you are in, and the criterion for that is what the class has been assembling for the whole hour.

What usually changes in the answer over that time. The first movement is from "I take what is at hand" to a choice by a sign: the data is physically lacking, so access to the outside; the reading eats the room and repeats from session to session, so a separate worker. The second movement is toward the cost. Before the breakdown both moves look free: a connection is one command, a subagent is one file. The material we worked through sets each one's bill beside it. For access to the outside that is somebody else's code inside your work, permissions you have to trim by hand before connecting, and standing room in the context for every connected server — for the one you did not use once over the session you pay exactly as much as for a working one. For a separate worker that is the definitions of all the connected servers, which its context inherits in full, the gap between two subagents' zones, which neither of their reports shows, and the shared working directory in which the workers write over each other's edits.

The answer "why choose at all, you can set up both" is worth taking apart separately. In a live project that is what happens, both work. The question is about the first move: the resources and the attention are single, and what gets set up first is what closes the shortage you already have. Setting up access to a system whose data you need once a month, and paying for it with standing room in the context of every session, is an ordinary mistake of order, and it costs exactly as much as the room taken up.

It also happens that the answer does not change at all. That is an honest outcome: a person who was choosing by what is lacking even before the class was choosing correctly. What usually changes for them is something else — their idea of what each of the two moves costs.

The question has no correct answer at the end either. It depends on what is lacking in the particular project: what is not inside at all, or the room taken up by reading. Over the class two criteria and two costs have appeared, named directly; the choice stays with whoever is looking at their own project.

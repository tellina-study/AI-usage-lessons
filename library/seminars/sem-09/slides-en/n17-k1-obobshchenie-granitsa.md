---
id: n17
type: criteria_checklist_and_boundary
duration_min: 1.5
assertion: "The 'answer or hand off' decision gets pulled into a separate field when the answer goes to a human with no second read; checkability of a decision is not the same thing as its correctness"
learning_goal: "Case 1's generalization and boundary, stated plainly (A7): 'when it's needed · when it isn't,' with a named limit of the technique itself and a documented case where the same error cost differently. The session's axis closes its first line here."
visual:
  pattern: criteria_checklist_and_boundary
  primary: >
    The criterion as its own tile at the top, below it a two-column table
    "when it's needed · when it isn't" — strictly for a contrast — then a
    tile on the technique's limit, a tile with a documented case carrying
    a "was → became" pair as one block, and a closing line for the first
    line of the session's axis.
  backup: >
    The criterion follows SETKA-KEYSOV-S9.md, section "Case 1", subsection
    "Generalization", a portable wording with no tool name.

    Both table columns rest on OUR OWN measurement: 2 aborts of 15 for
    strict output and 0 of 5 rephrasings for exact match, from last
    session.

    THE EXTERNAL CASE WAS RESTORED TO THE FRAME by an orchestrator
    decision mid-wave. The first draft of this slide didn't carry it — on
    an instruction the orchestrator then reversed as its own mistake: Air
    Canada was rejected by the owner (2026-10-24, "that example has come
    up several times already"), and the open gap remains only for a case
    from ENGINEERING practice. Case 1's boundary is held by Obermeyer et
    al., 2019 (`10.1126/science.aax2342`), exactly as assigned by
    ARCHITECTURE.md §6 and the grid's "Nuances" beat, item 3.

    Numbers are taken from the "Added by the orchestrator 2026-10-24"
    section at the end of CHISLA-SVERENO.md, where all six statements have
    status VERIFIED against the full original source (a 9-page PDF). The
    slide carries NO "per a secondary account" label and should not: line
    30 of that same file's table, which required it, was retired on
    2026-10-24 and itself points to this section.

    What made it onto the frame is exactly what this beat carries: what
    was predicted instead of what, the "was → became" pair as one block
    (48,772 → 7,758, which is the same 84%), and the load-bearing line —
    the fix changed neither the model, nor the training, nor the
    features, nor the sample. The rest of grid item 3 (26.3% at an equal
    score, 4.8 versus 3.8 chronic conditions, the manufacturer's own
    replication across 3,695,943 patients) is deliberately NOT carried
    over: four numbers on a closing frame stop being readable, and 4.8
    versus 3.8 is exactly the kind of pair of similar numbers in one
    sentence BRIEF §2 forbids. These details live in the presenter's own
    notes and in the grid.

    The scale of the stakes is named with our own number — "twenty
    requests a day" from scene n06, not the grid item 3's "forty": the
    session's own scene says twenty, and the frame has to agree with it,
    not with a draft.

    AN OPEN ITEM, not silently closed here: a documented case from
    ENGINEERING practice for this boundary still doesn't exist — Air
    Canada was rejected, no replacement found, inventing one is forbidden
    (case-design canon §4.3).

    The technique's limit is stated as a direct line, not a closing
    hedge: a field makes the decision checkable, but doesn't make it
    correct — exactly what's measured on n16 (4 of 15 passed the check
    with wrong content).
---

# When the decision needs to move into a checkable field

## Assertion

Checkability and correctness are different properties. A field gives you the first and promises nothing about the second.

## Visual

> **Criterion.** The "answer myself or hand off to a human" decision gets moved into a separate, checkable value when the answer goes directly to a human.

| When it's needed | When it isn't |
|---|---|
| The answer goes straight to a human, and nobody reads it before it's sent | A staff member reads the answer before sending it regardless — the model's decision is already checked by eye, a separate field adds nothing |
| A month from now, someone needs to be shown why a given request was answered on its own without calling in a human | There's no point sorting it out after the fact: the cost of a wrong answer is lower than the cost of an answer that never arrived at all |
| Questions arrive as arbitrary text, and a similar item always sits next to the right one | The whole set of questions is closed by a fixed list — then the model isn't needed here either, string comparison is enough |
| "Some answer, any answer" is worse than an honest "a staff member will answer" | Silence is more expensive than imprecision: strict output breaks outright, 2 aborts of 15, the client got nothing at all |

> **Limit of the technique.** A field makes the decision checkable — it doesn't make it correct: 4 of 15 passed the check with wrong content. A confidence-number threshold didn't close this limit either.

> **When it isn't twenty requests a day behind the automation.** Obermeyer et al., 2019: the algorithm selected patients for extra help honestly, but it predicted **treatment cost instead of severity of condition** — the metric was green, the check passed, and the wrong thing was predicted, exactly like our condition. The only thing changed: excess chronic conditions **went from 48,772 to 7,758**, −84%.

> **The session's first line, closed.** "The model will say so itself if it doesn't know" — it did, where the topic was entirely uncovered, and it didn't, where a similar item sat nearby.

## Speaker notes

Let's fold the case into one formulation you can carry out and apply to your own process, without remembering a single node name.

The criterion is this. The "answer myself or hand off to a human" decision can't be left inside the answer text: it goes into a separate value that code can check the same way on any next question. The reason isn't that the model is bad — we saw it's perfectly capable of honestly admitting it doesn't know. The reason is that a decision living inside composed text can neither be shown nor repeated.

Now the boundary, and I'll name both sides plainly.

Moving the decision into a field is needed when the answer goes straight to a human and nobody reads it before it's sent. When, a month from now, you'll have to explain why a specific request was answered on its own. When questions arrive as arbitrary text and a similar item always sits next to the right one — exactly where, as we saw, the self-report falls silent. And when "some answer, any answer" is worse for you than an honest "a staff member will answer."

Not needed — and this isn't a formality. These are four real cases. If a staff member reads the answer before sending it anyway, the model's decision is already checked by eye. If a wrong answer costs less than an answer that never arrives at all. If the whole set of questions is closed by a fixed list — then the model isn't needed here either. And a fourth, straight from our own measurement: strict output breaks outright, twice out of fifteen the client got nothing at all. Where a human is right there to catch it, free text is more honest — it will at least write something.

And the limit of the technique itself, worth carrying away as a separate thought. A field makes the decision checkable. It does not make it correct. The check answers exactly the question written into it, and no other — we read the condition with our own eyes and saw that it asks whether the item exists, not whether it's the right one. Four answers out of fifteen passed it with wrong content.

And one case from outside our own workshop — to see what the same error turns into at a different scale of stakes. We have twenty requests a day. The algorithm Obermeyer and colleagues studied had millions of insured people behind it: it selected patients for extra-help programs and honestly solved exactly the task it was set. The trouble was in the task itself — it predicted treatment cost instead of severity of condition. The most important part is how it was fixed: they changed neither the model, nor the training, nor the features, nor the sample. They changed only what was being predicted. Excess chronic conditions went from 48,772 to 7,758 — the bias dropped by 84 percent.

Recognize the shape? Green metric, confident automation, the check passes — and the wrong thing gets predicted. Our own condition behaved the same way: it answered its own question honestly and without error, the question just wasn't the right one.

The session's first line of its axis is closed. It looked reliable that the model would say so itself if it didn't know. It turned out: on grossly uncovered questions, it says so; on neighboring ones, it doesn't — and at the moment the answer goes out, there's nothing to check it with.

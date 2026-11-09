---
id: n23
type: mechanism_node_graph
duration_min: 1.0
assertion: "The real prompt field: the knowledge base sits inside it whole, all ten items in full text, between the instruction and the client's question"
learning_goal: "Layer 2 of the 'our solution' beat: a real screenshot of the settings panel. The room sees with its own eyes that the knowledge base isn't a separate store or an attachment to the request -- it's lines inside the very same text field as everything else."
visual:
  pattern: mechanism_node_graph
  figure: k2-promt-baza.png
  primary: >
    A real screenshot of the answer node's settings panel with the prompt
    field expanded: the full text is visible -- an intro line, the
    knowledge-base header, ten items in a row in full text, the client's
    question substitution, and the closing instruction. The emphasis is on
    the knowledge-base block, which takes up almost the whole frame.
  backup: >
    FRAME HONESTY STRENGTHENED (K2-7, review 2026-10-29: "a decision --
    unclear where it comes from"). This screenshot is the ORIGINAL state of
    the knowledge base, the very one the n21 breakdown used to find the
    middle's failure in the first place; the item order chosen in n22
    (frequent items to an edge) is NOT yet applied on this frame, and the
    visible text now says so directly, instead of leaving the reader to
    notice on their own that the item order here -- "payment first,
    contact with the instructor tenth" -- is a history of addition, not
    n22's decision.

    THE FIGURE'S SOURCE IS NAMED EXACTLY: `k2-promt-baza.png` is captured
    from the expanded prompt field of the node `Answer (free self-report)`
    -- the very node from Case 1, Version 1 (`stend/sborka.py`, function
    `case1_v1`), raw source frame
    `stend/n8n-screenshots-raw/case1-v1-prompt-expanded.png`. The figure
    already sits in `rendered/figures/`, and the frame has been read by
    eye: you can see the intro line, the line "Training center knowledge
    base:", all ten items in full text, the client's question
    substitution, and the closing instruction, "if you're not sure --
    honestly write that you don't know."

    THIS IS THE SAME FRAME AS CASE 1'S, AND THAT IS SAID OUT LOUD, not
    masked. The grid (subsection "Solution", layer 2) planned to capture
    the `Answer with grounding (structured)` node's panel before and after
    the item reorder. There's no "after reordering" screenshot on disk,
    and inventing one is forbidden ([[no-mock-fallbacks]]). The real,
    available frame was used instead, and the beat's subject doesn't
    suffer for it: what needs showing is that the knowledge base sits in
    the prompt WHOLE, and this frame shows exactly that better than any
    other. The open item remains and is flagged to the orchestrator again:
    there's no "item order reordered" frame for this session; n22 closes
    that gap with a before/after table and no new screenshot (K2-8).

    The emphasis is deliberately shifted relative to Case 1. There, the
    same screenshot carried the closing paragraph (the request to honestly
    admit not knowing), and the breakdown ran on that. Here, the middle of
    the frame carries the weight -- the knowledge-base block itself, its
    size, and the fact that every item is typed as plain text, like a note
    to a person.

    The short item labels are visible on the screenshot itself; they're
    not carried into the slide text (canon §7: a Russian sentence always
    comes before any Latin-script enumeration). There's no scenario name or
    run number on the frame (canon §3).

    EN FIGURE NOTE (Bilingual Production Rule, issue #172/#319): this
    figure is a real screenshot of the live rig's own settings panel --
    its content is the course's actual, real Russian-language knowledge
    base, exactly as entered into the running workflow. It is NOT redrawn
    for the EN track and keeps the same filename, k2-promt-baza.png, in
    both languages -- the same rule sem-08's own Case 2 applied to its
    real-screenshot figures (see glossary.en.yaml's closing notes): a real
    artifact of the actual rig is never faked into a language it wasn't
    captured in. The three generated schema figures elsewhere in this case
    (n19, n20a, n22, n25b) ARE redrawn, because those are diagrams we drew
    ourselves, not captured facts.
---

# The Prompt Field: the Knowledge Base Whole, in Its Original Order

## Assertion

The knowledge base isn't a separate store or an attachment to the request. It's lines inside the same field everything else lives in -- and on this frame, the order of those lines is still the history of addition, not the decision from the last breakdown.

## Visual

> **Frame BEFORE the reorder.** Ten items in a row, full text, in the order they were written -- payment first, contact with the instructor tenth. The last breakdown's decision (frequent items to an edge) hasn't been applied here yet.

## Speaker notes

This is the real settings panel of the same answer node we already opened, with the prompt field expanded. All the text that goes to the model is visible in full and reads straight off the screen.

At the top is the intro line: you're a training-center support assistant, below is the knowledge base you can use to answer. Then the line "Training center knowledge base:" and ten items in a row.

Look at how much room they take up. Almost the whole frame is the knowledge base: payment, rescheduling a class with the 24-hour condition, enrollment documents, a refund with ten business days and a 3,000-ruble threshold, retaking an exam, a missed class, a certificate, transferring to another course, holidays, contact with the instructor. Every item is typed as plain text, three or four lines, exactly the way Olga would explain it to a person. No markup, no schema, no keywords.

After the knowledge base comes the client's question substitution, and right at the very end sits the closing instruction: answer briefly, and if there's no answer and no confidence, honestly say you don't know.

Now the main reason we're back here. This is the very same field we opened in the last breakdown. Back then we read its last paragraph and talked about what the "answer or stay silent" decision rests on. And the knowledge base was sitting right here the whole time -- in the middle, between the instruction and the question, in full, on every single request.

And here's what's visible to the naked eye. First, the items have an order -- exactly the order they were written in: payment first, contact with the instructor tenth. Nobody chose this order, and the previous breakdown's decision -- frequent topics to an edge -- hasn't been applied on this screenshot yet: I'm showing the original field on purpose, so the difference between "how it sits now" and "what we decided" is visible on the actual text, not just in words. Second, adding an eleventh item takes exactly one motion: put the cursor after the tenth item and type a line. There's no form, no field, no separate spot reserved for a new item here, and none is planned.

And a third, less obvious thing. This field is everything the process knows. If the answer isn't found in these ten items, there's nowhere else for it to look: no file, no store, no memory of past requests. The knowledge base in the prompt is at once the process's entire knowledge base and all the baggage it carries on every single trip.

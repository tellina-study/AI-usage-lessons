---
id: n21
type: answer_breakdown_table
duration_min: 2.25
assertion: "Three of the four ways leave the knowledge base inside the prompt -- and then an item's position in the list stays a property of the process, either chosen or inherited from history"
learning_goal: "The breakdown right after the question (A1), a 5-column form -- form A5 (action · how it works · upside · downsides) gets a fifth column, 'what the research shows' (K2-6, review 2026-10-29: the theoretical grounding used to get lost inside 'downsides' in the old 4-column form and didn't read). No 'right/wrong' verdicts. Outside measurements are named by the work's own name -- this breakdown has no run of its own."
visual:
  pattern: answer_breakdown_table
  primary: >
    Table: action · how it works · upside · downsides · what the research
    shows. Five rows -- four actions plus a row on "base at the start /
    end of the prompt" below the table, no verdict column -- the decision
    comes on the next screen. The central pair of numbers is set as a
    banner, to read as one block instead of being hunted for inside a
    cell.
  backup: >
    THE "WHERE INSIDE THE PROMPT" SCHEMA (issue #303, Part B) -- a
    SEPARATE frame BEFORE this breakdown (see n20a), not on this same
    frame: this 5-column table already sits at the type-size floor (9pt)
    even without a schema, measured directly by the designer pass: with a
    schema on the same frame the table overflows even after shrinking
    ("OVERFLOW... cut content", "DID NOT FIT" -- text runs into the
    caption field). The fix, per the task rule: "schema on a separate
    frame before the table, if they don't fit together".

    A NAMED COLLISION WITH A5 (flagged to the orchestrator, not resolved
    silently). A5 locks exactly four columns in the owner's own verbatim
    wording (issue #274). K2-6, from the same review, asks for a separate
    column for theory. Resolved here by adding a fifth column explicitly
    for THIS breakdown, per the same review's new requirement: no other
    case's breakdown has it, and the extension isn't proposed as a general
    rule. The same collision is already named canonically for Case 6
    (`forma-keysa-s-zamerom.md` §12.2) -- the fifth column here resolves it
    the same way proposed for the number column there: a fifth column
    inside form A5, not a separate banner off to the side.

    The breakdown text is distilled from SETKA-KEYSOV-S9.md, section
    "Case 2", subsection "Breakdown", and fit into the 5-column form
    without rewriting the substance. The action wording is synced with
    K2-5 (the binary address of the choice inside each action, see n20).

    THE NUMBERS AND THEIR SOURCE. The pair of numbers on the frame --
    56.1% closed-book and a spread of more than 20 percentage points by
    document position -- CHISLA-SVERENO.md, line 42 (Liu and co-authors,
    arXiv:2307.03172, status "checked earlier by the orchestrator", on the
    slide "as is"). The baseline for the number is named right in the same
    cell: 56.1% is the same model's answers when it's given NO document at
    all, and that's exactly what a document placed in the middle is
    compared against. Nothing was taken from `research/*` (BRIEF §2).

    The fifth column carries SPECIFICALLY the theoretical frame: what this
    implies about the MECHANISM (trained this way -> this effect), not
    numbers -- numbers stay in "upside"/"downsides", where they already
    were and where they're visible next to the specific action.

    The third row (repeating the question around the list) is left almost
    number-free on purpose: both observations are from the same Liu et al.
    work, but there's no separate line for them in CHISLA-SVERENO.md,
    because the check there ran against numbers, and these two claims are
    qualitative. Putting a number on them would mean smuggling an
    unchecked figure onto the frame. Flagged to the orchestrator as a
    report.

    THERE IS NO RUN OF OUR OWN BEHIND THIS TABLE, and no cell pretends to
    be our own experience: wherever a measurement stands, the work's name
    is given.

    The fourth row is NOT called "next session" and isn't marked as the
    right one: in the breakdown it's weighed the same way as the other
    three -- by what it gives and what it costs with today's tool. What it
    is for the arc is stated by the boundary beat (n28).
---

# What Each of the Four Layout Options Does

## Assertion

None of the four is a mistake by itself. The difference is who stays responsible for an item's place in the list afterward.

## Visual

| Action | How it works | Upside | Downsides | What the research shows |
|---|---|---|---|---|
| **append to the end** | every new item becomes the next line of the current list | nothing to think through: that's how you keep any text file, no owner and no revisiting needed | a middle-positioned item in a growing list reads statistically worse: on a list of twenty documents, a middle document gives lower accuracy than **no document at all** -- **56.1%** | a U-shaped curve: the model reads the list's start and end noticeably better than its middle -- a training property, not one architecture's bug (Liu et al.) |
| **frequent items to the start or the end** | frequently asked or critical items move to one of the list's edges (which edge is a separate decision) | measurably reads better: list edges give better accuracy (same work) -- the only way to control placement without changing the process's design | needs someone to decide what's "important" and revisit the order as the knowledge base grows -- manual work that goes stale as topics change | the same edge effect; the gap between the best and worst position for the same document is **more than 20 percentage points** |
| **repeat the question -- before the list, after, or on both sides** | the client's question text is inserted at one or both edges of the knowledge-base list | nearly solves exact-keyword lookup: when the words match an item, repeating the question pulls the result through | on a question not phrased like a knowledge-base item, the device barely moves the trend: not universal, and it lengthens every request | the device works on exact keyword overlap, not meaning -- same work, no separate figure (unchecked) |
| **look up the item as a separate step** | the knowledge base is stored apart from the prompt; only the needed item is substituted into each request | an item's storage place no longer affects whether the model reads it, and requests stop growing with the knowledge base | can't be built with today's tool: the knowledge base is one text field. A new part of the process is needed -- a store plus a retrieval step -- built, filled, and fixed when a lookup misses | removes the question's premise entirely: if the request has no list at all, the list has no middle either |

> **Separately from the table: where the list itself sits.** All four rows are about order INSIDE the list. There's an orthogonal choice: where the list itself sits in the prompt as a whole -- right after the instruction (as now) or right before the client's question. Covered on the next frame, together with the decision.

## Speaker notes

Let's go through the four ways in turn. None of them is foolish -- each one has a task it would be the right choice for.

The first is appending to the end. Its main merit is real: it has no owner and no upkeep. Nobody decides, nobody revisits, a new line just lands next. The price only shows up under measurement, and here's the measurement. Models were given a list of twenty documents, one of which held the answer, and that document was moved around the list. When the right document sat in the middle, accuracy dropped below the mark the same model shows with no document at all -- below fifty-six percent. That is, a knowledge base in that position works worse than having none. The gap between the best and the worst position for the same document is more than twenty percentage points. This is Liu and co-authors' work, not our own run -- I'll say that again when we get to the outcome. And separately, why that happens: it's not a bug in one specific model. The authors explain it with a U-shaped attention curve that grows out of how models are trained to read long text.

The second is moving important items to one of the edges. The start and the end of the list read best in the same work, so the device leans on something measured. The price: order now has an owner -- someone has to know what's asked most right now and reorder items as that changes.

The third looks like a trick that sidesteps the question entirely: insert the client's question at one or both edges of the list. On an exact-keyword lookup task, this almost pulls the result through. The trouble is that clients phrase questions in their own words, not the knowledge base's words -- and on questions like that, the device barely shifts the trend. Plus every request gets longer.

The fourth pulls the ground out from under the question itself: if only the needed item gets substituted into the request, the order of the rest simply doesn't exist. We can't build this with today's tool -- our whole knowledge base is one block of text in one field.

And last, separate from the table. There's one more choice, of a different order: where the list as a whole sits relative to the rest of the text, not the order of items inside it. This isn't a fifth voting option -- it's a decision of a different level, and we break it down on the next screen, together with what we're taking on for Olga's need.

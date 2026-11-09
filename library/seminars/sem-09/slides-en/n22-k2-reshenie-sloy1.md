---
id: n22
type: mechanism_node_graph
duration_min: 2.0
assertion: "The knowledge base stays in the prompt whole, but the order of its items stops being a sediment of history and becomes a parameter of the process -- and that parameter now has an explicit reason behind it, not just taste"
learning_goal: "Layer 1 of the 'our solution' beat (§2 of the case-design canon): an architecture with no node name and no tool name. Edit K2-7/K2-8 (review 2026-10-29): the decision is now explicitly JUSTIFIED (not just presented as fact), and next to it stands a before/after table of visual rearrangement -- exactly what changes when an item is moved."
visual:
  pattern: mechanism_node_graph
  figure: k2-shema-promt-i-kesh-en.png
  primary: >
    A top-to-bottom prompt schema: instruction to the process -> the whole
    knowledge base -> a cache breakpoint -> the client's question. Below
    the schema -- one decision banner and a "before / after" table of three
    rearrangements (order of addition, important to the start, important
    to the end). Ocean palette, type no smaller than 7.5 pt.
  backup: >
    LAYOUT EDIT (2026-10-29, rebuild after Case 2 was split). The schema
    used to share a frame with SIX text blocks plus a table -- the
    composition didn't fit ("DID NOT FIT"/"PAST THE CANVAS EDGE"), the
    table fell to the floor of the type-size ladder, and the schema itself
    shrank to 50% width. Two blocks ("why the list sits exactly here",
    "what we don't change") were pulled off the visible frame -- both are
    already retold word for word in the speaker notes, so no fact is lost,
    only the duplicate. The table keeps the same three rows and three
    columns it had -- only the cell captions were shortened. The meaning
    and the numbers weren't touched.

    WHAT CHANGED (K2-7, K2-8, review 2026-10-29). The earlier edit
    presented the decision ("frequently asked items -- to the start or the
    end") with no explanation of where it came from -- the owner named this
    directly: "a decision, and it's unclear where it comes from" (about
    n23, the same solution beat, layer 2). The justification is now
    explicit: the decision follows from the breakdown on n21 -- the start
    and the end of the list read better than the middle (Liu and
    co-authors), so the order of items inside the list has to be a CHOICE,
    not a history of additions, or else the middle of the list fills up
    randomly, with whatever landed there by timing, rather than with
    whatever is safe to put there.

    VISUAL REARRANGEMENT OPTIONS (K2-8) are added as a before/after table
    directly below the schema -- without a new PNG: there's no "after
    rearrangement" screenshot on disk, and it's deliberately not drawn as a
    stylized fake ([[no-mock-fallbacks]]) -- instead it's built as a text
    comparison of three layouts of the same ten-item list. Turning this into
    a standalone figure is a decision for the designer pass, not this edit;
    flagged to the orchestrator as an open item.

    ON WHERE THE LIST ITSELF SITS (not the items inside it). n21 left this
    question orthogonal and carried it forward to here. The answer: the
    list stays exactly where it sits now -- between the instruction and the
    client's question, it does NOT move to the very end of the prompt. The
    reason: the same research points exactly here -- the client's question
    already sits at one of the "good" edges (the end of the prompt), and
    the instruction to the process occupies the other edge (the start);
    moving the list closer to the question would mean shifting it toward
    an already-occupied good edge while also pulling it away from the
    instruction, which also has to read reliably. The choice: keep the
    list between the two already-strong edges, and handle the middle of
    the list by rearranging the ITEMS inside it (see below), not by moving
    the whole block.

    A STALE FLAG WAS REMOVED. The earlier edit carried a long flag,
    "DECISION FOR THE ORCHESTRATOR: mismatch between the beat and the
    finished figure" -- by the date of this edit the mismatch is already
    closed: `make_figures_k2.py`'s third round (2026-10-26) split the two
    figures into functions `sloy1()` (this one, no numbers, no trap) and
    `kesh()` (`k2-shema-kesh-lovushka.png`, numbers and comparison); both
    figures on disk are dated to the same edit --
    `rendered/figures/k2-shema-promt-i-kesh.png`, 2026-10-26 08:14, the same
    time as the script. The figure on this beat is correct now; the flag
    no longer needs to be carried.

    The decision follows SETKA-KEYSOV-S9.md, section "Case 2", subsection
    "Solution", layer 1: the knowledge base lives in the prompt whole, but
    item order is an explicit parameter of the process -- frequent and
    critical topics to the start or the end of the list, not in order of
    historical addition. The prompt's structure is from the real text on
    the rig (`stend/sborka.py`, `case1_v1`).

    No node names, no orchestrator name, and no Latin script on the frame,
    deliberately: §2 of the canon requires layer 1's wording to survive a
    tool change. The real panel comes on the next screen.

    EN FIGURE NOTE (Bilingual Production Rule, issue #172/#319): the EN
    slide uses k2-shema-promt-i-kesh-en.png, a direct English-text redraw
    of the same schema (same layout, same colors, same numbers), generated
    by running `python3 make_figures_k2.py --lang en` -- the same
    `sloy1()` function, driven by the shared `fig_strings_en.py` dictionary
    (`tools/seminar-build/fig_toolkit.py`), not a second, hand-written
    `_en()` function.
---

# Where the Knowledge Base Sits in the Prompt -- and Why Exactly There

## Assertion

The knowledge base stays in the prompt whole. What changes is the order of its items -- and it changes based on what the breakdown showed, not on taste.

## Visual

> **What we're changing inside the list.** Item order is no longer the order of addition: frequent and critical topics move to the start or the end. Order now has an owner and gets revisited as the knowledge base grows.

| Layout | "Reschedule a class" (frequent) | "Working during holidays" (rare) |
|---|---|---|
| **order of addition** | 2nd of 10 (by chance) | 9th of 10 (middle) |
| **important -- to the start** | 1st, at the edge | in the middle |
| **important -- to the end** | 10th, at the edge | in the middle |

## Speaker notes

Look at this decision with no node name in it at all: if this chain gets rebuilt with a different tool tomorrow, not a single line here changes.

The prompt is built top to bottom from three parts. First, the instruction: who it is, what it does, how to answer. Then the knowledge base -- every item in a row, full text. Then the client's question. The whole construction goes out again on every single request.

Before changing the order of the items, let me answer the question that suggests itself: why not just move the whole list closer to the client's question, to that same good edge? Because that good edge is already taken -- by the question itself. And the other good edge, the start of the prompt, is taken by the instruction to the process, which also has to read reliably all the way through. The list stays exactly where it sits now, between two strong edges, and we handle the middle by rearranging the items inside the list, not by moving the whole block.

And here's what we're changing inside the list. Item order stops being a history of additions and becomes a decision. Look at the table: the item about rescheduling a class, which gets asked often, ended up second under order-of-addition almost by accident -- good placement, but not earned. The item about working during holidays, asked rarely, sits in the middle-to-end -- also by accident. If we deliberately move the frequent item to one of the edges, the rare one stays in the middle not because it was forgotten, but because the middle is exactly the spot where the cost of a mistake on a rare question is lower.

Now let me say separately what we're NOT changing, because it's easy to miss. No new step appears in the process. Not a single node gets added to the canvas. The knowledge base stays exactly where it lived, and still travels to the model whole. The entire decision is the order of the lines inside one text field.

And one last thing, the reason it's worth looking at this picture specifically as a structure. The start of the prompt -- the instruction and the knowledge base -- repeats word for word from call to call. The client's question at the end changes every time. That means on every single request we're sending the same long chunk of text again, and one short new one. This has a second side to it: first let's look at the real panel where this knowledge base lives, and then we'll break down what repeating it actually costs.

---
id: n23
type: problem_scenario
duration_min: 1.0
assertion: "Version 1 — cut the document into fixed-size chunks, by character count, without looking at where sentence boundaries fall"
learning_goal: "Case 2's scene beat: the need (the right chunk must not lose meaning after the cut) + version 1 as the first natural attempt. No run number (the breakdown comes in later beats, after the question)."
visual:
  pattern: problem_scenario
  figure: case2-shema-postanovka-en.png
  primary: >
    On top — diagram S1 (canon forma-keysa-s-zamerom.md §2): solid lines
    for chunk embedding and the store, already working since last session;
    dashed gold lines for splitting the document into chunks, the node
    this case builds, sitting BEFORE embedding. Below the diagram — a need
    tile, version 1 in plain prose, the honest question the scene leaves
    open.
  backup: >
    DIAGRAM S1 ADDED (owner, comparing Seminar 9 against Seminar 10:
    "bring S10 up to S9's level" — every case scene in S9 opens with a
    diagram of "where we're intervening", S10's Case 2 had no such
    diagram). `case2-shema-postanovka.png`, generator —
    `rendered/make_figures_sem10.py::case2_shema_postanovka()`.

    No tool names appear on the diagram deliberately (layer 1 — solution
    architecture, not an n8n screen); the real screen is n35/n36.

    The need and version 1 — from SETKA-KEYSOV.md Case 2, "Setup",
    verbatim.
---

# How to cut a document so a chunk doesn't lose meaning

## Assertion

The document needs to be cut so that search can later point precisely at the spot with the answer — not merely so the text fits into the store.

## Visual

> **The need.** Every chunk in the store carries one complete piece of meaning — the answer to a question must not end up torn between two neighboring chunks.

Version 1 — the natural first attempt: cut the document into fixed-size chunks, by character count, regardless of sentence boundaries.

> One parameter, one pass through the text. Whether this works for meaning — we check next.

## Speaker notes

The previous case decided that the knowledge base lives in a separate store. But the store doesn't swallow a document whole: a three-page regulation or a multi-page manual doesn't fit into one store chunk in a way that lets search later point precisely at the right spot. The document first needs to be cut into chunks — and where that cut falls decides whether the answer to a specific question stays intact inside one chunk or ends up torn between two neighbors.

Version 1 is the natural first attempt, the one you pick if you don't think about this separately: cut the document into fixed-size chunks — by character or token count, with sentence or paragraph boundaries left entirely out of account. This is the simplest implementation rule: one parameter is set — the chunk size — and the text is cut by it mechanically, one pass, with no regard for content.

Version 1's convenience is obvious: it requires minimal preparation and works on any text the same way, regardless of language or document structure. The question the scene leaves open: is this enough to keep the answer to a client's question from falling apart in half, right where a random cut happens to land?

It's worth noting that this version has no malicious intent and no carelessness in its implementation — it's exactly what any engineer would choose who's writing document-splitting code for the first time and hasn't yet run into what happens next. The parameter "cut every N characters" is literally one configuration line in the store node, and the temptation to stop there is very strong precisely because there seems to be nothing left to do: the chunks exist, you can move on to the next step. Today's breakdown is exactly what checks whether that temptation is justified.

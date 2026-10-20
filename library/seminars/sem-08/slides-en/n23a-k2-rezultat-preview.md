---
id: n23a
type: result_preview
duration_min: 0.75
assertion: "A literal repeat never reaches the requests table today — Olga doesn't see it; the same question in different words still gets logged as a new row, with no 'looks like a repeat' flag"
learning_goal: "New letter-tail slide between n23 and n24, per the 2026-10-20 voice edit requiring a result-preview mockup for every case. Honest architectural finding, confirmed from the workflow's graph connections, not assumed: the duplicate-match branch is a dead end (no record written), while the meaning-check branch writes unconditionally regardless of its verdict — so measuring the classifier's accuracy (20/20 here) isn't the same as proving it affects today's output."
visual:
  pattern: result_preview
  primary: >
    A mockup of three requests-table rows, not a chat (in this case the
    recipient reads a table, not a Telegram notification) — the first an
    ordinary request, the second row absent (the literal repeat is caught
    before being logged), the third row present and looking like an
    ordinary new request (the rephrasing is logged as-is).
  backup: >
    The artifact was chosen to match the scene: n18 — "Olga ... opens the
    requests table and sees a question from a client"; unlike Case 1 (n12,
    a Telegram chat), Case 2 has no recipient-notification node at all (the
    node list in stend/stage-2.json: Request form / Extract fields / Model
    / Vocabulary check / Write row / Result screen / Normalize+hash / Exact
    duplicate in window? / Same question, reworded? (LLM) / Model (dedup) —
    not a single Telegram node), so the mockup is built as rows of the
    `requests` table, not as a chat bubble.

    Checked against the connections (`python3 -c "import json; d=json.load(
    open('stend/stage-2.json')); print(d['connections'])"`): the node
    `Exact duplicate in window?` (IF) has an outgoing connection ONLY from
    branch 1 (false), leading to `Same question, reworded? (LLM)`; branch 0
    (true, a match found) has NO outgoing connection at all — a genuine dead
    end at the graph level, not a textual description of one. The node
    `Same question, reworded? (LLM)` (chainLlm, a node type with physically
    one output) leads unconditionally to `Write row` — the model's answer
    ("yes"/"no") is never read anywhere further down the graph, there's not
    a single Switch/IF after it. The columns of `Write row` (received_at/
    name/contact/request_text/topic/urgency/contact_from_text/status/
    extra_topics) contain no field for the meaning-check's result — the
    node's answer simply isn't saved. Today's replacement of that node with
    jev (n21/n23, issue #274) is a literal swap of one node for another
    with the same single outgoing connection; neither n21, nor n22, nor n23
    describe adding any branching after jev, and the orchestrator touched
    nothing but the node itself (n21 backup: "the node «Same question,
    reworded? (LLM)» and the model node «Model (dedup)» were removed,
    replaced by a new node «Jev decision (reworded?)»" — a node swap, not a
    change to the graph around it) — meaning that same unconditional
    connection survives the swap.

    Independent textual confirmation for the literal repeat —
    stend/README.md, section "Case 2 — dedup (first pass, 2026-10-18 —
    numbers lost)": "Execution 51 (literal repeat) — the node `Exact
    duplicate in window?` caught the match, the request went down the
    branch with no record and no reply; n8n marked the execution status
    success".

    The node's name, the 0.5 threshold, the word "jev", and the execution
    id are not surfaced on the mockup (canon §3,
    proektirovanie-keysa-i-voprosa.md) — the same decision as on
    n12/n34b/n52a: the visible layer shows only what Olga actually sees,
    not the mechanics of the solution. There's no figure on disk yet — the
    slide is built as a text representation of the table (a block quote),
    like the three preceding slides of this pattern, ready for the
    designer to render visually at the production stage.
---

# What Olga Sees on a Repeat Request — and What She Doesn't

## Assertion

A literal repeat today is caught before it reaches the table — no new row, Olga sees nothing. The same question in different words still becomes a new row anyway — identical to the first, with no flag at all.

## Visual

> **The requests table, that same morning.**
>
> Row 1 — "when can I pay for the class?" — an ordinary request.
>
> *(Two hours later the same text, word for word — there's no second row. The repeat was stopped before it reached the table.)*
>
> Row 2 — "how do I pay for the course" — logged, and looks exactly like an ordinary new request.

For the literal repeat, the scene's problem is solved completely: it simply never reaches Olga. For the very same rephrasing the case started with — it gets logged as-is, as a second row, no different from the first.

## Speaker notes

Before wrapping up the case, it's worth honestly looking not at the diagram and not at a node's settings, but at what Olga herself actually ends up seeing in the requests table she opens every morning.

Take the very pair this case started with. The first request — "when can I pay for the class?" — comes in as an ordinary row, like any other. If exactly the same text, word for word, arrives two hours later, no new row appears in the table at all: the cheap mechanical step stops it before it gets there, and the run itself still finishes normally. Olga won't see the repeat, or even a trace that it happened — for her, it simply didn't happen.

But if the same question in different words arrives two hours later — "how do I pay for the course", exactly the request the scene opened with — the picture is different. We just measured the meaning check on this step: it reliably tells this kind of rephrasing apart from a new question. But today that distinction has no connection at all to what ends up in the table: the second row gets logged anyway and looks exactly like the first — with no flag at all that it's probably a repeat. Olga will see two rows from the same contact two hours apart — exactly the picture the case opened with.

This isn't a slip in the accuracy measurement — the meaning check really does tell the two apart well on its own test. It's a boundary of what's actually built and carried through to the result today: reliably telling apart isn't the same as reliably not showing twice. What to do with a detected rephrasing — quietly let it through, log it with a flag, or stop it the same way as a literal repeat — is exactly the product question we already called a nuance: not every detected repeat has to disappear from the table. But today, by default, it doesn't disappear, and that's worth knowing in advance rather than discovering as a surprise when you open the table.

Back to what all of this means for the case's architecture as a whole.

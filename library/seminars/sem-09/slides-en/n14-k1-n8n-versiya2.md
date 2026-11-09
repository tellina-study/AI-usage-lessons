---
id: n14
type: mechanism_node_graph
duration_min: 0.75
assertion: "Version 2: the same decision is pulled out of the text into a separate field, and the canvas immediately shows a branch — two paths instead of one"
learning_goal: "Layer 2 for version 2: a real canvas screenshot. Before the Latin node names, a Russian-register line names the architectural change with no tool names (case-design canon §7); the slide map in §4 has no separate 'version-2 layer 1' beat of its own — the gap is flagged by report, not silently papered over with a different genre."
visual:
  pattern: mechanism_node_graph
  figure: k1-holst-v2-en.png
  primary: >
    A real screenshot of the live rig's n8n canvas: `Client question` →
    `Answer with grounding...` (with the model node hanging below) →
    `Grounded in known KB item?` — and from that node, two labeled
    branches: `true` upward, to writing the row and the answer screen;
    `false` downward, to notifying Olga, writing the row, and a separate
    screen.
  backup: >
    The screenshot is real: `stend/n8n-screenshots-raw/case1-v2-canvas.png`,
    taken by `stend/n8n_shots.py`. There is no stylized card standing in
    for the screenshot.

    EN figure `k1-holst-v2-en.png`: the SAME crop as the RU
    `k1-holst-v2.png`, renamed for EN-track asset-naming consistency
    (added for this EN track, issue #172/#319) — no relabeling needed, the
    real n8n interface's node titles and branch labels are already
    English.

    A CROP REQUIREMENT: on the source frame, a `Production Checklist`
    popup partially covers the `Client question` node on the left. The
    crop begins to the right of its edge; the breadcrumb naming the
    scenario isn't taken into the frame (canon §3, no service ids on
    screen).

    What's literally visible on the frame: eight nodes, three of them new
    compared with version 1 — the check node, the node notifying Olga, and
    a second answer screen; two labeled branches, `true` and `false`, off
    the check node; the model hangs off the answer node the same way it
    did in version 1 — it hasn't gone anywhere. The asterisk note under
    the answer node is visible on the screenshot (that's how the n8n
    interface is built), but the slide text doesn't comment on it (K1-9,
    2026-10-29 edit: "we've discussed this a hundred times").

    The first line of the visible layer is a Russian-register sentence
    that names the architectural change with not a single node name:
    case-design canon §7's requirement (a plain-language sentence before
    any Latin-script list). This same line is what carries version 2's
    layer 1, which §4's slide map never allocated a beat of its own to;
    the figure `k1-shema-geyt.png` from BRIEF §5 remains unplaced — the
    gap is flagged to the orchestrator by report, not silently closed by
    swapping in a different genre of slide.

    Presentation order is the story of one iteration (case-design canon
    §4): version 2 appears here AFTER version 1 has been measured, and as
    an answer to what was measured, not laid out next to it as a
    pre-arranged experiment.
---

# Version 2 on the rig: a branch after the model

## Assertion

The "answer or hand off" decision has been pulled out of the answer text into a separate field that code reads — and the canvas immediately grew a second branch.

## Visual

> **What changed.** The model still reads the knowledge base and writes an answer, but it's now also required to name, as a separate value, which knowledge-base item it's grounded in. Code makes the decision after that.

> Canvas: `Client question` → `Answer with grounding...` (the same model, `qwen/qwen-2.5-7b-instruct`) → `Grounded in known KB item?` → **`true`** to `Write row/Result screen (answered)`; **`false`** to `Notify Olga` → `Write row/Result screen (escalated)`. Three nodes that weren't in version 1: the check, notifying Olga, and a second answer screen.

## Speaker notes

This is the same rig and the same model, but a different scenario — version 2, built after we'd seen the first one's results.

First, about what changed in substance, with no node name at all. The model does exactly what it did before: it reads the knowledge base and writes an answer. One requirement was added — along with the answer, it must now name which knowledge-base item it's grounded in. Name it as a separate value, not in words inside the text. And the decision — answer the client or call in a human — is now made by code, checking that value.

Now look at the canvas, and the comparison with the previous one will be obvious. On the left, everything is the same: the question form, the answer node, the model hanging below — the same qwen-2.5-7b-instruct, still being called. And then a node appears that wasn't in version 1: `Grounded in known KB item?` — that is, "is the answer grounded in a known knowledge-base item."

And here's the main thing, visible with no explanation needed: two arrows come off this node, labeled `true` and `false`. In version 1, after the model there was one arrow, one path. Here there are two. The upper one is the ordinary path: write the row and show the answer to the requester. The lower one is the one that didn't exist before: tell Olga the question has been handed to her, write that as a separate row, and show the requester a different screen, saying a staff member will answer.

Three nodes on the canvas are new: the check, notifying Olga, and a second answer screen. Exactly the three that had nowhere to go in version 1 — because there was nothing after which to place them: the decision didn't exist separately from the text, and the branch had nothing to branch from.

Time to open the check node and read exactly what it asks.

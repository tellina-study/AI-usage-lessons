---
id: n11
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real settings panel of version 1: the entire knowledge base and the request to honestly admit not knowing sit in one text field, side by side, and the model is asked for nothing but text"
learning_goal: "Layer 2 for version 1, second half: a real screenshot of the node's settings panel. The one line the whole of version 1 rests on is read verbatim off the frame — prose next to it adds nothing further."
visual:
  pattern: mechanism_node_graph
  figure: k1-promt-v1-en.png
  primary: >
    A real screenshot of the `Answer (free self-report)` node's panel with
    the prompt field EXPANDED: the text is visible in full — an opening
    line, the ten knowledge-base items in a row, the client question
    substituted in, and a closing paragraph asking the model to honestly
    admit when it doesn't know. The emphasis is on the closing paragraph.
  backup: >
    THE FIGURE'S SOURCE IS NAMED EXACTLY, addressed to whoever prepares
    the figure: `k1-promt-v1.png` is built from
    `stend/n8n-screenshots-raw/case1-v1-prompt-expanded.png` — this is the
    expanded view of the same field, where the prompt text is visible IN
    FULL, including the closing paragraph. The figure must NOT be taken
    from `case1-v1-prompt-panel.png` (the collapsed view of the same
    panel): there, only the first two lines fit in the field, and the
    closing paragraph — the very line the whole of version 1 rests on —
    doesn't make it into the frame. The first draft of this slide was
    written from the collapsed screenshot and had to carry this line with
    the caveat "below the visible part"; the expanded screenshot appeared
    mid-wave and removed that caveat. Take the crop from the left column
    (`Expression`); the right column (`Result`) duplicates the same text
    and isn't needed in the crop.

    EN figure `k1-promt-v1-en.png`: the SAME crop as the RU
    `k1-promt-v1.png`, renamed for EN-track asset-naming consistency
    (added for this EN track, issue #172/#319) — the prompt text itself
    (quoted in the RU item) is the only part needing translation; the
    underlying n8n panel chrome is already English.

    All visible-layer text is read verbatim from the frame and matches
    `stend/sborka.py`, function `case1_v1`.

    What is deliberately DROPPED relative to the first draft: a block
    about the `Require Specific Output Format` toggle being set to "off."
    It's visible on the collapsed screenshot and NOT visible on the
    expanded one — and talking about it in prose next to a frame that
    doesn't show it means asking the room to take it on faith (owner's
    2026-10-20 edit on Seminar 8). The claim "the model is asked for
    nothing but text" reads directly off the prompt text itself, which is
    fully present on the frame, and doesn't need the toggle.

    The frame shows a breadcrumb with the node's name; neither the
    scenario id nor the run id is visible anywhere (canon §3).
---

# Setting up the answer node in version 1

## Assertion

The knowledge base and the request to honestly admit not knowing sit in one text field, side by side.

## Visual

> **Beginning → middle → end of the field.** "You are a training center's support assistant. Below is the knowledge base..." → the same knowledge base, ten items, word for word, and the client's question → "Answer on the merits and in Russian, briefly. If there's no answer and you aren't sure — write that you don't know." The model is `qwen/qwen-2.5-7b-instruct`, with no explicit settings. **What it's not asked for:** no value, no item name — only text, and that's what it gets.

## Speaker notes

This is the real settings panel for that same answer node, with the prompt field expanded: the whole text that goes to the model is visible in full, and you can read it right off the screen.

It opens with an introductory line: you are a training center's support assistant, below is the knowledge base you can use to answer. Then comes the knowledge base itself — those same ten items we already went through on the scene, word for word, in ordinary human text: no keywords, no schema. After the knowledge base, the client's question is substituted in.

And then — the closing paragraph, and that's the whole of version 1, without remainder. Answer on the merits and in Russian, briefly, two to four sentences. If the answer isn't in the knowledge base and you aren't sure — honestly write that you don't know, and that a staff member will answer. If you're sure — answer directly, with no hedging.

Read this request again and judge it as an engineer would. It's well written. It has a condition, what to do in each case, and even an instruction not to hedge where the answer is known. If the task had been to write a clear instruction for a human, there'd be nothing to fault here.

Now look at what's missing from this field. The model isn't asked for a separate value, a flag, or the name of the item it's grounded in. It's asked for text — and it gets text. The entire "answer or stay silent" decision is ordered by these two sentences and lives inside whatever answer it writes.

Hence the question the rig answers next, not a line of reasoning: how well does a polite request hold up when it's the only thing standing between a made-up answer and the client. Version 1 is built, it's on the rig, and it's working. Let's run it.

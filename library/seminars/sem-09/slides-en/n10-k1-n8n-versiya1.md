---
id: n10
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real canvas of version 1: four nodes on the main path and not a single branch after the model"
learning_goal: "Layer 2 for version 1 (case-design canon §2): a real snapshot of the live rig with real node names, not a stylized diagram. The frame shows the version's main property — after the model, there's only one path."
visual:
  pattern: mechanism_node_graph
  figure: k1-holst-v1-en.png
  primary: >
    A real screenshot of the live rig's n8n canvas, a wide crop of the
    main path: `Client question` → `Answer (free self-report)` →
    `Write row` → `Result screen`, with the model node
    `Model (answer, free)` hanging separately below.
  backup: >
    The screenshot is real: `stend/n8n-screenshots-raw/case1-v1-canvas.png`,
    taken by `stend/n8n_shots.py` on `n8n.lessons.tellian.io`. There is no
    stylized card standing in for the screenshot (BRIEF §5,
    [[no-mock-fallbacks]]).

    EN figure `k1-holst-v1-en.png`: this is the SAME crop as the RU
    `k1-holst-v1.png`, renamed for EN-track asset-naming consistency
    (added for this EN track, issue #172/#319) — no relabeling needed,
    because the real n8n interface's node titles (`Client question`,
    `Answer (free self-report)`, `Write row`, `Result screen`,
    `Model (answer, free)`) are already in English in the live screenshot
    itself.

    THE "MODEL*" NOTE WAS REMOVED FROM THE FRAME by the 2026-10-29 edit
    (BREAKDOWN, K1-9: "clear out the clutter: asterisks, 'model*' notes.
    We've discussed this a hundred times"). It's still visible on the
    canvas screenshot itself (that's a property of the n8n interface, the
    screenshot is untouched), but the slide text no longer comments on it
    — the paragraph about what the asterisk means is dropped entirely, not
    shortened.

    THE MODEL IS NAMED BY NAME (C5): `qwen/qwen-2.5-7b-instruct`, called
    with no explicitly set options — `stend/sborka.py`, `ANSWER_MODEL`.
    The canvas only shows the node's generic name, `Model (answer, free)`;
    the model's own name isn't visible in the image (it's in the node's
    credentials, not its label), so it's named in the slide text.

    A CROP REQUIREMENT, addressed to whoever prepares the figure: on the
    source frame, the left third is covered by a popup, the `Production
    Checklist` panel (three items about error-notification setup). It must
    NOT appear in the crop — the area to the left of the `Client question`
    node is cut off. The breadcrumb at the top names the scenario and is
    not included in the crop; the scenario id is not visible anywhere on
    the source frame (canon §3).

    What's literally visible on the frame, and so what can be said about
    it: four main-path nodes in a row, the model node hanging below, the
    `Model*` note under the answer node, and — the main point — not a
    single branch after the answer node: there's one arrow, and it leads
    straight to writing the row.

    What's NOT visible on the frame, and so is not claimed in prose next
    to it: the prompt text. The canvas shows node cards, not their open
    settings. The settings panel comes as a separate screen (n11), with
    its own screenshot. This is a direct consequence of the owner's
    2026-10-20 edit on Seminar 8: don't ask the room to trust the slide
    text where the screenshot doesn't show it.
---

# Version 1 on the rig: four nodes

## Assertion

After the answer node, there's not a single branch on the canvas — one arrow, leading straight to the requester's screen.

## Visual

> Main path: `Client question` → `Answer (free self-report)` → `Write row` → `Result screen`, with the model `Model (answer, free)` hanging below — `qwen/qwen-2.5-7b-instruct`, the same one throughout the case, with no explicit settings. **What's missing from the canvas:** after the answer node, not a single branch — one arrow, one path; there is no "hand off to a human" branch at all.

## Speaker notes

This is a real screenshot of the live rig, the exact screen that opens when you go into the version-1 scenario. Not a simplified diagram, not a drawing — the same interface we used to build the process in last session.

The main path reads in a single row. On the left, the form the client's question arrives in. Next, the answer node — it's called `Answer (free self-report)`, and the name says it plainly: a free-text answer, with self-report. Then writing the row, and the screen the requester sees.

Below the answer node hangs a separate circle — that's the model itself, `Model (answer, free)`. In this interface, the model is a separate entity, plugged into the node from the outside; that's why it's shown separately. I'll name it, because from here on it's the same one across every run of the case: `qwen/qwen-2.5-7b-instruct`, called with no explicit settings — temperature and the other parameters are left at default.

Now look at what's missing from the canvas — that matters more than what's there. There's no branch after the answer node. One arrow, one path: whatever the model writes, it goes on the same way — gets written as a row and shown to whoever asked. There's no "hand off to a human" branch on this canvas. No separate node that calls Olga, no second screen, no notification.

This is exactly the diagram we just broke down, now seen with your own eyes: the "answer or hand off" decision has no place of its own on the canvas. It lives entirely inside the text born in the answer node, and the process does nothing further with that text except show it.

What exactly this node asks the model for isn't visible on the canvas: the interface shows node cards collapsed, with no open settings. So the next screen is the real settings panel for this same node.

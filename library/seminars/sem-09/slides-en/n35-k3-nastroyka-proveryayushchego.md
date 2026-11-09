---
id: n35
type: mechanism_node_graph
duration_min: 0.75
assertion: "The checker's real panel: seventeen lines of code where the five requirements are written out literally, and each one returns its own rejection reason"
learning_goal: "Layer 2 of Case 3, second half: a real snapshot of the settings panel. It shows that the criterion is text you can read in full, and that a rejection comes with a reason written in advance, not composed at the moment of checking."
visual:
  pattern: mechanism_node_graph
  figure: k3-panel-proveryayushchego-en.png
  primary: >
    A real screenshot of the check node's code editor — eighteen numbered
    lines, visible in full, cropped TIGHTLY around the code block (no
    tabs/Mode-Language fields/interface hints — those are named in words on
    the frame, not duplicated from the screenshot).
  backup: >
    EN figure `k3-panel-proveryayushchego-en.png` — the live rig re-shot
    for this EN track (issue #172/#319) with its code comments and string
    literals set to English, same tight crop as the RU
    `k3-panel-proveryayushchego.png`
    (`stend/n8n-screenshots-raw/case3-code-check-panel.png`, cropped by
    `crop_k3_panel_tight.py`). The code logic and line count are identical
    to the RU version; only the Russian-language string literals inside it
    (the rejection-reason text) are translated for the EN screenshot — the
    underlying checks (length, detail, routing phrase, allowed numbers,
    Latin letters, Chinese characters) are unchanged.

    THE NODE NAME, MODE, AND LANGUAGE ARE NOT IN THE FRAME (cropped out
    along with the tabs): they're named in words on the slide itself —
    `Code check` (read off the n34 canvas, where it's visible), `Run Once
    for Each Item`, `JavaScript`. This isn't invented — it's carrying over
    a fact already shown in the slide's own text, not in the picture.

    What's literally visible on the frame: eighteen lines of code in full.
    The five requirements show up as six checks — "entirely in Russian"
    splits into two lines, one for Latin letters and one for Chinese
    characters.

    What's NOT claimed in prose next to it: anything about the judge
    model's prompt. Its panel is a separate frame, n35a, its own real
    screenshot (BRIEF §3).

    The line `const ok = reasons.length === 0` is named separately: that's
    the entire acceptance rule — the list of reasons is empty, so the
    answer is good enough.
---

# The checker's panel: seventeen lines

## Assertion

The acceptance criterion is text you can read in full and show to Olga.

## Visual

> **Node `Code check`, `Run Once for Each Item`, `JavaScript`.** Five requirements become six checks: length · detail · where to go next · no numbers outside the knowledge base · Latin letters · Chinese characters. The acceptance rule is the last line: the list of reasons is empty, so the answer is good enough.

## Speaker notes

This is the real code editor for that same check node from the previous frame — it's called simply and literally `Code check`, the name is visible on the n34 canvas. Mode: run once per item — every answer is checked separately, and the verdict applies to one specific text. Language: ordinary browser-script language, JavaScript.

Read what's actually written in the code on the frame. Length over two hundred eighty characters — the rejection reason is "longer than two hundred eighty characters." A key detail from the matching knowledge-base item is missing — the reason is "missing the detail," and then, in quotes, the detail itself. Where to go next isn't named: the check looks for any of five words in the text — administrator, personal account, staff member, and two others. There's a number that isn't in this knowledge-base item — the reason lists those numbers. And language: one line looks for Latin letters, a separate line looks for Chinese characters.

Five requirements became six checks, and that's normal: "entirely in Russian" naturally splits in two. For a person that sounds like one condition; for code, which has to decide this deterministically, it's two independent checks: no Latin letters at all, and no Chinese characters at all. A human phrasing, by default, glues together what a program needs split into separate lines — hence the difference: five items in the requirement, six lines of code.

The last line is the entire acceptance rule. The answer is good enough if and only if the list of reasons is empty. The node returns two values outward: good enough or not, and the reason string.

Here's what's worth looking at, from an engineering angle. The rejection reason is written in advance and sits in the code. You can read it without running the process. You can show it to Olga. It isn't composed at the moment of checking, and it doesn't depend on which variant of the text the checker happens to get. The same answer gets the same reason today, tomorrow, and on the thousandth run. Remember this property — the next frame shows the panel of a model-checker, which doesn't have it.

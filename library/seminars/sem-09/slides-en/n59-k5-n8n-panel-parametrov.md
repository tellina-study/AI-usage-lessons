---
id: n59
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real model node's settings panel: temperature is set to zero, and in the list of eight available fields, there's no seed parameter at all"
learning_goal: "Case 5's layer 2: a real screenshot of the settings panel of the very same node already standing in Case 1 and Case 3 — with no change to the graph (BRIEF §4a, deliberate rhythm break P4). The frame checks the provider and seed cards literally against the interface, not against the narration. 2026-10-29 edit: the inset text was shortened (the eight fields are listed in the screenshot and in the notes, not duplicated in the inset body) — freeing room for the diagram and removing the build warning 'SCHEMA SQUEEZED' (it had been 3% of the area)."
visual:
  pattern: mechanism_node_graph
  figure: k5-panel-parametrov.png
  primary: >
    A real screenshot of the model node's settings panel: the field
    `Credential`, the field `Model` with the value
    `qwen/qwen-2.5-7b-instruct`, the field `Sampling Temperature` with the
    value `0.0`, and the expanded `Add Option` list — eight items, all
    fully visible.
  backup: >
    The screenshot is real: `stend/n8n-screenshots-raw/case5-model-
    params.png`, taken by `stend/n8n_shots.py` on the live rig; the figure
    `k5-panel-parametrov.png` is assembled from it by cropping the
    parameters panel. No -en rename: the panel's own UI (field labels,
    buttons) is already English, and no Russian text appears anywhere in
    this crop — unlike the equivalent slide in the sem-08 EN track, there's
    no live-form field name baked into the screenshot that would need an
    explanatory exception.

    WHAT'S VISIBLE ON THE FRAME, LITERALLY. `Credential`: `OpenRouter
    account`. `Model`: `qwen/qwen-2.5-7b-instruct` — the same model as in
    Case 1 and Case 3. `Sampling Temperature`: `0.0`, not the node's
    default `0.7` (BRIEF and CHISLA-SVERENO.md, line 26: n8n
    `LmChatOpenRouter`'s default — `0.7`, `Top P` — `1`). The expanded
    `Add Option` list — exactly eight items in a row: `Frequency Penalty`,
    `Maximum Number of Tokens`, `Response Format`, `Presence Penalty`,
    `Timeout`, `Max Retries`, `Top P`, `Provider Routing`. The count was
    made directly from the screenshot, line by line.

    THE NODE'S NAME DIDN'T MAKE IT INTO THE FRAME: the crop runs into the
    expanded `Add Option` list, which covers the dialog's top line
    carrying the name. So the name is given in words on this same frame
    instead — read off the dialog header of the same screenshot before
    cropping, exactly the way Case 3's node name is read off a
    neighboring frame on n35, rather than invented.

    CHECKING THE BREAKDOWN'S SECOND AND THIRD CARDS AGAINST THIS SAME
    SCREENSHOT: `Provider Routing` is present in the available list, but
    not added — this node does have a provider-routing block in
    principle (card 2 rests on a real capability). The `seed` parameter
    isn't in the list in any form — not renamed, not hidden behind
    another word, simply absent (card 3 refers to something the node
    physically doesn't have).

    What is deliberately NOT shown: the prompt field's contents (it's the
    same as in Case 1, and already appeared on frame n11) and the model's
    answer itself — that comes in the following beats. The node id, the
    workflow id, and the webhook address aren't visible on the frame
    (canon §3).
---

# The Model Node's Parameters Panel: Eight Available Fields

## Assertion

The same model, the same node, as in Case 1 and Case 3 — the temperature is already set to zero, and it has no `seed` parameter at all.

## Visual

> Node `Model (T = 0)`: `qwen/qwen-2.5-7b-instruct`, the same node as in Cases 1 and 3, `Sampling Temperature`: `0.0` (not the default `0.7`). The `Add Option` list is expanded in full, eight fields: `Provider Routing` is there — you can pin a provider; `seed` isn't there under any name — that lever simply doesn't exist on this node.

## Speaker notes

This is the real settings panel of the model node — the very one that answers clients in Case 1 and checks other answers in Case 3. The process graph doesn't change today: we're looking inside an already-standing node, we're not adding a new one.

At the top — the credential and the model: `qwen/qwen-2.5-7b-instruct`, the same one it's been all day. Right below it — the field `Sampling Temperature`, set to `0.0`. It's worth saying plainly: zero here isn't the tool's own default — this node defaults to `0.7` — it's a value set deliberately. In other words, the first card from the previous question, lowering the temperature to zero, has already been done here, and we're looking right now at its consequences.

Below it — the `Add Option` button, and on the frame it's expanded in full: eight fields that can be added to this node. Let me name them in order — right now we're counting for ourselves, not taking anyone's word for it: frequency penalty, maximum number of tokens, response format, presence penalty, timeout, max retries, `Top P`, and provider routing.

Look closely at the last item on the list — provider routing. It's here, physically available with one button. This directly confirms the second card from the previous question: pinning the provider is a real setting on this very node, just not switched on yet.

Now look for the `seed` parameter with your own eyes — and you won't find it. It's not there under this name or under any other, not among the main fields and not in the expanded list. The third card from the previous question proposed pinning down something that, as a setting, physically doesn't exist on this node.

The node's own name didn't make it into this frame — the expanded field list covered the header line. But it's read off the same screenshot, just above, verbatim: the node is called `Model (T = 0)` — with no hidden meaning, a direct statement that its temperature is set to zero.

With the `seed` parameter ruled out and provider routing confirmed working, what's left is temperature, provider, and answer field order — three node-setting levers, plus two actions on the prompt itself, few-shot and description, which this panel doesn't check at all: this node simply receives the prompt as input. What all five actually give on the client's real questions — the next breakdown.

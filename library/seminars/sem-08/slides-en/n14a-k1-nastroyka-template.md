---
id: n14a
type: mechanism_node_graph
duration_min: 1.5
assertion: "The settings panel of the 'Compose notification (template)' node: one expression substituting ready values into a form written in advance — the whole text fits on screen with no scrolling"
learning_goal: "New slide (n14a), the template version's counterpart to n11a: a real screenshot of this node's open settings panel. Unlike n11a, the expression is fully visible with no scroll cutoff — cross-checked word for word against `stend/stage-1-after.json`, both sources agree."
visual:
  pattern: mechanism_node_graph
  figure: k1-n8n-versiya2-nastroyka-template.png
  primary: >
    A real screenshot of the "Compose notification (template)" node's
    settings panel (Parameters tab): Mode — "Manual Mapping," the "Fields
    to Set" field → `notification_text` (type String) with the full
    expression, "Include Other Input Fields" on, "Input Fields to Include"
    — All.
  backup: >
    **This screenshot is real, and the expression it shows manipulates
    Russian-language field values on purpose — read this before anything
    else.** The expression pulls from the live rig's real fields ("Имя" =
    name, plus the topic and extra-topics values) and produces Russian
    output text, because the live training center's requests, coordinator,
    and notifications are genuinely in Russian. This is NOT re-drawn or
    re-translated for the EN deck, for the same reason as n11a (see
    `glossary.en.yaml`'s mirror-check note): changing it would
    misrepresent what's actually configured in the live system. The
    expression, read in full from the frame and cross-checked against
    `stend/stage-1-after.json`: `=Новая заявка от {{ $('Request
    form').item.json['Имя'] }}: тема «{{ $('Vocabulary
    check').item.json.topic }}»{{ $('Vocabulary
    check').item.json.extra_topics ? ', также: ' + $('Vocabulary
    check').item.json.extra_topics : '' }}.` — screen and live API agree
    verbatim, no discrepancies.

    The node is `n8n-nodes-base.set` (`Edit Fields` / `Set`, blue-pencil
    icon), Mode "Manual Mapping" (not automatic expression mode — a
    hand-set single field). "Include Other Input Fields" is on, "Input
    Fields to Include" is "All": besides `notification_text`, the node
    passes every other request field onward unchanged — it doesn't just
    assemble the notification text, it also avoids losing data later
    nodes might need.

    This replaces the earlier form of presenting this (same as n11a):
    previously the same expression was quoted in prose next to a canvas
    crop that showed neither the panel nor the expression. The text match
    was exact even then, but the screenshot didn't confirm it; now the
    expression and its source are on the same frame.
---

# Node settings: the expression of the template version

## Assertion

Here is the actual settings panel. The screen below is real and its expression manipulates Russian field values on purpose — the live training center runs in Russian. One expression, written once by hand, substitutes ready values into a form fixed in advance. No model call at all.

## Visual

> **Node "Compose notification (template)" (`Set` / `Edit Fields`), Mode — Manual Mapping.** Field `notification_text` (String), real screen, Russian field names and output text — see Assertion above: «Новая заявка от `{{ $('Request form').item.json['Имя'] }}`: тема «`{{ $('Vocabulary check').item.json.topic }}`»`{{ $('Vocabulary check').item.json.extra_topics ? ', также: ' + $('Vocabulary check').item.json.extra_topics : '' }}`.» — in English, what this produces: "New request from {name}: topic '{topic}'{, also: {extra topics}, if present}."

> "Include Other Input Fields" — on, "Input Fields to Include" — All: the rest of the request's fields pass through the chain unchanged.

## Speaker notes

Here's the actual settings panel of the "Compose notification (template)" node — and it's worth comparing directly with the model version's panel we saw two screens ago, because the node serves the same purpose but is built in a fundamentally different way.

Mode here is "Manual Mapping": one field, `notification_text`, type String, and inside it, an expression written once by hand. It substitutes already-known values into pre-set places: the requester's name, the main topic, and, if present, the extra topics — with a condition built into the expression itself that adds the phrase "also: …" only when extra topics exist, and adds nothing if they don't. There's no separate model node anywhere near this one — in this version of the chain, no such node exists at all, which we already saw on the previous, general frame by the absence of the "Model*" marker.

Unlike the model version's panel, this expression is fully visible on screen, with no scrolling — it's shorter and fits the field without being cut off. Compare that with Version 1's prompt: there, the statement text is longer and part of it runs past the edge of the visible field area.

Worth noting separately: the "Include Other Input Fields" toggle is on, and "Input Fields to Include" is set to "All." That means the node doesn't just assemble the notification text into one new field — it also passes every other request field onward unchanged, so later nodes don't lose anything they might need.

The result of this expression is deterministic: given the same input values, the text always comes out exactly the same, with no variation — and, as a result, with no risk of inserting something into the message that wasn't in the request. The cost of that reliability is the flip side: if the message form ever has to change in meaning, not just in values, this expression has to be rewritten by hand, every single time. We ran both versions through the same requests — what follows from that is next.

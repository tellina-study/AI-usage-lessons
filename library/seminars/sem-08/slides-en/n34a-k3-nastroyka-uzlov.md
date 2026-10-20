---
id: n34a
type: mechanism_node_graph
duration_min: 1.5
assertion: "Inside the \"Extract amount\" node — a strict JSON schema with one required numeric field; inside \"IF\" — a single condition, the amount compared with 3000 literally, both parameters checkable right on screen, not just by the node's name"
learning_goal: "A new slide showing the settings panels of two version-2 nodes from the inside (open configuration), not just as named boxes on the canvas — real screenshots, not a paraphrase."
visual:
  pattern: mechanism_node_graph
  figure: k3-n8n-nastroyka-uzlov-en.png
  primary: >
    A composite of two real screenshots of open settings panels from the
    live rig, each with a caption above it: left, the "Extract amount" node
    (Information Extractor) — Parameters tab, showing the input JSON schema;
    right, the "Amount over threshold?" node (IF) — Parameters tab, showing
    the comparison condition. Both panels are real configuration screens,
    not a canvas with named boxes.
  backup: >
    The JSON schema of `Extract amount` reads literally: one required field,
    `amount_rub`, strictly numeric. The condition of `Amount over
    threshold?` reads: `{{ $json.output.amount_rub }}` is greater than
    `3000` — a single condition, with "Convert types where required"
    switched off. Mirrors RU n34a (issue #274).
---

# Settings panels: "Extract amount" and "Amount over threshold?"

## Assertion

The schema and the condition aren't a paraphrase in words — they are what actually sits in the settings fields of version 2's two nodes, in full, right on screen.

## Visual

> **Node "Extract amount" (Information Extractor).** Parameters tab, Schema Type — "Define using JSON Schema." Schema: `{"type": "object", "properties": {"amount_rub": {"type": "number", "description": "the refund amount in rubles, as stated in the text"}}, "required": ["amount_rub"]}`. One field, strictly of type `number`, required.

> **Node "Amount over threshold?" (IF).** Parameters tab, the one condition: `{{ $json.output.amount_rub }}` **is greater than** `3000`. "Convert types where required" is switched off — the comparison expects an already-ready number and converts nothing implicitly.

## Speaker notes

On the previous screen the `IF` node was visible from the outside — a card on the canvas with a name and two branches. Here is the same thing from the inside, exactly what an engineer sees when they double-click the node and open its settings.

On the left — the node that extracts the amount from the request text. It's called "Information Extractor," and its task is set not by a free-form prompt but by a strict JSON schema: one parameter, `amount_rub`, strictly of type number, and required. The model inside this node is not allowed to return text, a range, or the word "about" — the result either passes this schema, or the node is considered to have failed. This is the same extraction step that version 2 does not remove: the model still pulls out the amount, but the result of this step is now disciplined by format, not just by instruction. A free-form prompt can be read several different ways; a required, strictly typed field cannot — it either comes back as a valid number, or the step fails loudly instead of quietly guessing.

On the right — the node that replaced version 1's text-based decision. It has one condition, and it reads literally: the already-extracted number is compared to three thousand with the "greater than" operator. Not a paragraph of text about a threshold, but one comparison line in the interface, where the operator has no room for interpretation. The type-conversion switch is turned off deliberately: the condition needs a ready-made number, not a string that still has to be turned into one on the fly, risking a silent conversion error.

The difference between these two panels and the version-1 text prompt we saw earlier isn't a matter of word count — it's about where the meaning of the decision actually lives. In the prompt, the rule is dissolved in natural language, and the model has to re-read and interpret it every single time. Here, the rule is a strictly typed field in a settings form, which is either filled in correctly or flagged as an error before the run even happens. The rest of the chain, which we walked through on the diagram, hasn't changed — only what's visible on these two panels has.

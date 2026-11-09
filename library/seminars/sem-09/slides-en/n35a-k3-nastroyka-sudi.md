---
id: n35a
type: mechanism_node_graph
duration_min: 0.5
assertion: "The same model as the generator's, with the same five requirements written into the prompt text — except it doesn't write the verdict in code, it composes it"
learning_goal: "Layer 2 of Case 3, the missing pair to n34/n35: a real snapshot of the judge node's panel (K3-12/13, owner edit 2026-10-29 — 'if we're checking with a judge here, we're missing a schema with the little judge model'). The model's name and settings are explicit (C5), sitting next to the code checker, not instead of it."
visual:
  pattern: mechanism_node_graph
  figure: k3-panel-sudi-en.png
  primary: >
    A real screenshot of the judge node's panel, `Judge verdict`: a `Text`
    field with the prompt (the knowledge-base item plus the client's
    question), `Schema Type` set to `Define using JSON Schema`, and the
    output JSON schema itself — `ok` (boolean) and `reason` (string), both
    required.
  backup: >
    EN figure `k3-panel-sudi-en.png` — the live rig re-shot for this EN
    track (issue #172/#319) with its UI language and prompt text set to
    English, same crop and framing as the RU `k3-panel-sudi.png`
    (`stend/n8n-screenshots-raw/case3-judge-panel.png`).

    THE MODEL IS NAMED EXPLICITLY (C5), IN WORDS ON THE FRAME, NOT ONLY ON
    THE SCREENSHOT: the `Judge verdict` node is of type
    `informationExtractor`, and the connected language model is
    `qwen/qwen-2.5-7b-instruct`, through the same credential
    (`OpenRouter account`) as the generator's. The model's settings are
    `options: {}` — that is, WITHOUT overriding temperature: the provider's
    default is used, the same as for the generator and for the code (the
    only difference between branches is which node renders the verdict,
    not a model setting).

    WHAT'S NOT VISIBLE ON THE FRAME, AND SO IS NOT STATED IN PROSE: the
    prompt text itself is cropped by width (the field continues past the
    frame). The five requirements in the prompt are the same wording, word
    for word, as in the `Code check` code (n35); this identity of wording
    is the premise of the whole code-vs-judge comparison across beats
    n36-n41, not of this frame.

    There is deliberately NO text under the figure (same as n35): this
    screenshot is also a portrait-oriented frame, and any competing text
    block would eat into height the layout can't spare. Everything
    substantive is in the notes.
---

# The judge's panel: the same prompt, its own output schema

## Assertion

The judge gets the same wording of the requirements as the code, and the same model as the generator.

## Visual

## Speaker notes

This is the real panel of the node that renders the verdict in place of code, in every "judge" branch of Case 3 — it's called `Judge verdict`, and the node type is `informationExtractor`, an n8n node that asks a language model to return structured JSON against a given schema, not just plain text.

The model behind this node is the same one that writes the answer to the client: `qwen/qwen-2.5-7b-instruct`, the same OpenRouter account. The model's settings are not overridden — an empty `options` object, meaning the provider's defaults, the same ones the generator and the code use. This matters: the difference in numbers between code and judge on the screens that follow is a difference in which mechanism renders the verdict, not a difference in models and not a difference in settings.

The `Text` field is the judge's prompt. The frame shows the beginning: the knowledge-base item and the client's question, both n8n expressions, pulling their value from the same `Pick KB item` node as the generator uses. Further along in that same field, past the edge of the frame, sit the five requirements — the exact same wording, word for word, as the checking code on the previous screen. That's not a coincidence, and it's not my own decision — it's the premise of the whole comparison: if the criteria differed between code and judge, a mismatch in their verdicts would prove nothing.

`Schema Type` is `Define using JSON Schema`, and the schema itself sits below it: two required fields, `ok` — boolean, true if the answer passes all five rules, and `reason` — a string, what was violated and why, if `ok` is false. This is the structural counterpart to what the code returns as the string `reasons.join('; ')` — the judge has the same pair, "good enough / why," only a model composes it instead of deterministic code computing it.

Remember this pair of frames side by side: code reads a substring against a written rule and returns the same reason on the same text, every time. The judge gets the same task, the same text, the same model — and next we'll measure whether its verdict holds just as firmly.

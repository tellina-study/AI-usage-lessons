---
id: n46a
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real settings panel of the mechanical-check node: the code declares the techniques as a list, each row a technique family's name and the text template it's matched against"
learning_goal: "Case 4's layer-2 ('device shot'): the other five cases of the session already have one (n23, n34, n69, and the layer-1 diagrams of Cases 1, 3, 5); Case 4 didn't. The slide doesn't count how many techniques the mechanical check caught on the corpus — those numbers are already covered on n50–n52; here is only the node's construction: how the code is written, what it checks, and what it doesn't."
visual:
  pattern: mechanism_node_graph
  figure: k4-panel-mehanika-en.png
  primary: >
    A real screenshot of an n8n Code node's settings panel: Parameters /
    Settings tabs, run mode "once per item," language JavaScript, the
    function body — an array `PRIEMY` of pairs "technique family name,
    text template." Nine family names visible in a row, scrolling cut off
    at the frame's bottom edge.
  backup: >
    A genuine screenshot: `stend/n8n-screenshots-raw/k4n-panel-mehanika-raw.png`,
    assembled by `compose_k4n_shots.py::mehanika_panel()` — only the
    interface's bottom hint ("Type $ for a list…") was removed, the code
    itself is untouched.

    HONEST EXCEPTION (same practice established for genuine live-rig
    screenshots in sem-08's own EN track, e.g. n34-k3-reshenie-n8n.md):
    because this is a real screenshot of the actual code running on the
    live rig, which serves a Russian-speaking training center, the
    technique names baked into the array are genuinely in Russian on
    screen and are quoted verbatim rather than translated; an English
    gloss is added alongside, in both the visible body and the notes.

    VERIFIED AGAINST THE FINISHED FIGURE this session (`Read`, 1286×1632):
    tabs "Parameters / Settings," the Mode field set to "Run Once for Each
    Item," the Language field set to JavaScript, the code — `const PRIEMY
    = [...]`, an array of [name, regular expression] pairs.

    Nine family names visible on the frame in a row, verbatim: «прямая
    инъекция «забудь инструкции»» (direct injection, "forget
    instructions"), «требование игнорировать правило или проверку»
    (a demand to ignore the rule or the check), «инструкция пропустить
    проверку» (an instruction to skip the check), «поддельная системная
    пометка (скобка)» (a fake system note, bracket form), «поддельная
    системная пометка (оборот)» (a fake system note, phrase form), «режим
    отладки или теста» (a debug or test mode claim), «инструкция на
    латинице» (an instruction in Latin script), «переопределение формата
    ответа (поле решения)» (overriding the answer format, decision
    field), «переопределение формата ответа (оборот)» (overriding the
    answer format, phrase form) — the ninth name is visible in full, its
    template is cut off by the frame's bottom edge. The array isn't
    visible past this: the frame isn't scrolled.

    The figure "21 templates" (by technique family) is taken from the
    measurement's own description: `stend/zamery-k4-novyy/README.md`,
    section "Three defenses," the line about the mechanical check (`r`).
    The frame shows 9 of 21, the remaining 12 are past the scroll; the
    visible body says this outright — the prose doesn't claim to show
    more than is actually visible (the same discipline as n34/n69).

    The table of three defenses (action · how it works · advantage ·
    drawbacks) is already covered on n46 — its rows aren't repeated
    here, this frame carries only the construction of one of the three.
---

# Settings panel of the mechanical-check node: code with a list of techniques

## Assertion

The node looks at a request's phrasing against a text template — one line of code per known technique family.

## Visual

> Settings panel of a Code node: array `PRIEMY`, pairs of "technique name, text template." Nine rows visible without scrolling, another twelve past the frame's bottom edge, out of the full 21 (the number comes from the measurement's own description).

## Speaker notes

This is the real settings panel of the node we called the mechanical check on the previous frame — code that sees the request before the deciding model does.

On top — n8n's standard tabs, Parameters and Settings. The run mode is "once per item": the function runs once for every request in the queue. The language is JavaScript, ordinary code, with no call to any model at all.

The function body opens an array called `PRIEMY`. Each row of this array is a pair: a human-readable name for the technique and a regular expression that looks for it. In code this is called a regular expression — a text template that catches an entire class of similarly worded techniques with one rule.

On screen, without scrolling, nine such rows are visible in a row. The first looks for a direct injection — phrasing of the "forget your instructions" kind, worded various ways. Next — a demand to ignore the rule or the check, an instruction to skip the check, two different fake system notes: one dressed up as a square-bracketed note, the other as the word "system" inside ordinary text. Next — a mention of a debug or test mode, an instruction typed in Latin script instead of Russian, and two variants of overriding the answer format: through the word "decision" and through a request to answer in one strictly specified way.

The array doesn't end there — it's simply cut off by the frame's bottom edge. The full list the node is written against is twenty-one templates across different technique families; the frame shows less than half, the remaining twelve rows run further down and need scrolling that isn't here.

There's no understanding of the request's meaning here at all. The node compares its text against a ready-made list of phrasings — and is exactly as limited by that: a wording for the manipulation that isn't on the list will slip past it unnoticed, however much sense it carries. What that turns into on a real corpus of 64 requests, we'll see next, in the measurement's results.

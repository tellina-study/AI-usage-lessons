---
id: n48b
type: mechanism_node_graph
duration_min: 0.75
assertion: "Two canvases side by side show the same cost of three defenses as the table of model calls — only counted in canvas nodes: six against thirteen"
learning_goal: "The pair of canvases gets its own frame, split off from n48a (Case 4 slide revision 2026-10-29): there, the picture stood next to the measurement-design table — two large elements on one screen, and the picture carried its own captions over the table that the slide's text was duplicating. Here the figure is the one large element, at the full available width. The model-call numbers are already covered on n46/n47 and aren't repeated here."
visual:
  pattern: mechanism_node_graph
  figure: k4-holst-0-vs-prc-en.png
  primary: >
    A genuine composite of two live-rig n8n canvas screenshots, one above
    the other, with caption tiles baked into the picture itself: on top
    "Configuration '0' — no defense at all, 6 nodes," below "Configuration
    'prc' — all three defenses together, 13 nodes." The slide's own text
    doesn't repeat these captions.
  backup: >
    A genuine screenshot: both canvases were captured by `stend/n8n_shots.py`
    (zoom-to-fit) on the live rig, composed into one picture by
    `compose_k4n_shots.py::holst_pair()` from
    `stend/n8n-screenshots-raw/k4n-holst-0.png` and `.../k4n-holst-prc.png`.
    The top half's zoom was carried over to the bottom half so the
    "Request" node's label lines up at the same height in both — otherwise
    the narrow canvas (6 nodes) would have stretched less than the wide
    one (13 nodes) shrank, and the label mismatch would have grown
    instead of disappearing (measured in the drawing script's own
    docstring).

    SPLIT OFF FROM n48a (Case 4 slide revision 2026-10-29): there, the
    picture stood next to the "Step | Configurations" measurement-design
    table — two large elements on one frame, an overload. Here the
    picture is the one large element, at the full available width (the
    `content` genre draws `visual.figure` this way when there's no other
    large block beside it — `tools/seminar-build/README.md`, "How the
    technique-library rule holds").

    VERIFIED AGAINST THE FINISHED FIGURE this session (`Read`, 4629×1605).
    Top half: a straight line of six nodes (`Request` → `Request data` →
    `Build request` → `Model decision` → `Parse decision` → `Result`),
    with not a single branch. Bottom half: the same path with two
    branches (`Did the mechanical check find a technique?`, `Did the
    classifier find a technique?`) and two added `Decision: manager`
    nodes — one for each defense that fired; thirteen nodes in total,
    matching the caption on the picture itself.

    HONEST EXCEPTION (same practice established for genuine live-rig
    screenshots in sem-08's own EN track, e.g. n34-k3-reshenie-n8n.md):
    the node titles baked into this real screenshot are genuinely in
    Russian on screen, because the rig serves a Russian-speaking training
    center (`Заявка`, `Данные заявки`, `Сборка запроса`, `Решение модели`,
    `Разбор решения`, `Итог`, `Механика нашла приём?`, `Классификатор
    нашёл приём?`, `Решение: менеджер`) — quoted verbatim where the
    visible body names them, with an English gloss given alongside in
    both the visible body and the notes, rather than silently
    re-captioning a real screen.

    THE CHOICE OF GENRE (`mechanism_node_graph` instead of
    `test_structure_table`) is explained here and repeated in the report:
    the frame carries a genuine live-rig screenshot — the same kind of
    material as n23/n34/n69. n48/n48a carry a synthetic test-design
    table; this frame, by the kind of material it is, belongs with the
    first group.

    The model-call numbers by configuration (64 / 33 / 123) are already
    covered on n46 and aren't repeated here — this frame shows the node
    architecture, the call count stays where it already was.
---

# Two canvases side by side: no defense and all three together

## Assertion

The same cost of three defenses already counted in model calls is visible in the canvas's own architecture too — six nodes against thirteen.

## Visual

> **Each configuration is a separate canvas on the rig**, not a toggle inside one process. A canvas with no mechanical-check node is an honest picture of the "no mechanical check" configuration, not a decoration.

> **It's visible on the canvases, literally.** On top — a straight line of six nodes, with not a single branch. Below — the same path with two branches and two added "Decision: manager" nodes, one for each defense that fired.

## Speaker notes

These are two genuine canvases from the live rig, one above the other, with their own captions right on the screenshot — added over the actual pixels from outside, the same way every frame in this deck is captioned.

On top — configuration "0," the one with none of the three defenses. Six nodes in a straight line: the request arrives through a form, request data is collected, the call to the model is built (shown on screen as `Заявка` → `Данные заявки` → `Сборка запроса`, i.e. "Request" → "Request data" → "Build request"), the model makes its decision (`Решение модели`, "Model decision"), the answer is parsed (`Разбор решения`, "Parse decision"), and the result is sent off (`Итог`, "Result"). Not a single branch — the request follows the exact same path no matter what it says.

Below — configuration "prc," where all three defenses run at once. Thirteen nodes instead of six. The same path as above, but with two new decisions built into it. First — the mechanical-check node and the branch right after it (`Механика нашла приём?`, "Did the mechanical check find a technique?"): a technique found — the request goes to a separate `Решение: менеджер` ("Decision: manager") node, bypassing the deciding model. No technique found — the request moves on, to the entry classifier, which has its own branch (`Классификатор нашёл приём?`, "Did the classifier find a technique?") and its own `Решение: менеджер` node for when it fires. Only if both defenses find nothing does the request reach the deciding model — the very same node that was the only path on the canvas above.

Each configuration is built as its own separate canvas on the rig. There's no toggle inside one process here: the canvas with no mechanical check has no mechanical-check node on it physically — it wasn't disabled by a setting, it simply was never built there. This is more honest than a toggle: a toggle can sit silently in the wrong position, a missing node is visible at once to anyone who opens the canvas.

The difference in node count — thirteen against six — is the cost of three defenses that doesn't show up in the model-call table from the previous section. There it counted calls to the deciding model; here it counts nodes of the process itself: two new sorting decisions, two new branches, two new outcomes besides the model's own decision. Every added defense is both an extra call and, at the same time, an extra branch on the canvas that now needs watching.

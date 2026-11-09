---
id: n34
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real canvas of the loop: a fork after the check, a return path along the bottom edge, and two different endings — 'ok' and 'not converged'"
learning_goal: "Layer 2 of Case 3, first half (case-design canon §2): a real snapshot of the live rig with real node names. The frame shows what Case 1's canvas didn't have — a path back."
visual:
  pattern: mechanism_node_graph
  figure: k3-holst-tsikl-en.png
  primary: >
    A real n8n canvas screenshot of the live rig. The main row, left to
    right: `Client question` → `Pick KB item` → `Generate answer` →
    `Code check` → `Retry or finish?`; below the answer node hangs
    `Model (generate)`, with a `Model*` marker underneath. On the right, a
    second fork, `Converged?`, and two endings. At the bottom, `Prepare
    retry` and a long return arrow running along the bottom edge of the
    frame.
  backup: >
    EN figure `k3-holst-tsikl-en.png` — the live rig re-shot with its node
    naming set to English for this EN track (issue #172/#319), on the same
    canvas layout as the RU `k3-holst-tsikl.png`
    (`stend/n8n-screenshots-raw/case3-cycle-code-canvas.png`). One node
    name on the RU rig mixes English and Russian — `Result screen (не
    сошлось)` — because the facilitator typed that qualifier in Russian
    when naming the node; on the EN rig this is renamed to `Result screen
    (not converged)` so the EN screenshot shows a fully English canvas, not
    a mixed-language one. This specific rename is a translator's judgment
    call, flagged for the QA pass. No stylized card stands in for the
    screenshot here (BRIEF §5).

    What's literally visible on the frame, and so what can be said about
    it: seven nodes on the main path, a model node hanging below, a
    `Model*` marker, two forks labeled `true` and `false` on their outputs,
    two different final screens (`Result screen (ok)` and `Result screen
    (not converged)`), and an arrow that leaves `Prepare retry`, goes
    right, down, and then left along the whole bottom edge of the frame,
    back to the input `Pick KB item`.

    What's NOT visible on the frame, and so is not claimed in prose next to
    it: neither the generator's prompt text, nor the checker's code, nor
    the attempt counter. The canvas shows node cards, not their open
    settings. The checker's panel is a separate screen (n35), with its own
    screenshot.

    The scenario name in the breadcrumb is cropped out; neither the
    scenario id nor run ids appear anywhere on the frame (canon §3). The
    word "measurement" from the scenario's own name is not carried onto
    the visible layer (BRIEF §3).
---

# The loop on the rig: two forks and a path back

## Assertion

The main thing on this frame is the arrow along the bottom edge: that's what a retry is made of.

## Visual

> **The main row.** `Client question` → `Pick KB item` → `Generate answer` → `Code check` → `Retry or finish?`. The model hangs below, marked `Model*`.

> **The path back.** From `Prepare retry`, an arrow runs along the bottom edge back to the input — the same question, a new attempt. Next: `Converged?` and two endings: "ok" to the client, "not converged" to a human.

## Speaker notes

This is the real canvas of the live rig — the same interface we built the process in during past sessions, with no simplifications and no redrawing.

The main row reads left to right. A question arrives at the form. The matching knowledge-base item is picked up. The model writes an answer — the model itself hangs below this node, in its own separate circle, and under the node sits an asterisk marker: the node doesn't work without a model, this is a required parameter. Next, a check. Next, the first fork.

Now the main reason this frame exists at all. Look at the bottom edge: from the node that prepares a new attempt, a long arrow runs left across the whole screen and comes back to the input — to the point where the knowledge-base item is picked up. This is the retry, and it exists as a real, visible line on the canvas. The same question, the same item, a new attempt. There was nothing like this on Case 1's canvas: there, after the model, there was one arrow and one path forward.

The second fork's output leads to fork number two, and that one decides the answer's fate. One branch — the row gets written, the results screen says "done," the text went out to the person. The other — the row also gets written, but the screen is different: not converged. The answer went out to nobody; the question is waiting for a person.

Two different endings on one canvas — this is that same "not converged" branch from the schema, carried through to a real node. You can see it, you can look right at it, and the log later shows how many questions ended up there exactly.

The log deserves a separate word, because it's the other half of the solution. The requester sees one screen — either the answer, or a message saying a human will answer. Olga sees something else: a row with how many attempts it took and how the loop ended. A process where both endings are logged with equal care answers, a month from now, the question "how often does this actually work" with a number.

What the canvas doesn't show is exactly what the check node verifies. Node cards show names, not settings. The next screen is its real panel.

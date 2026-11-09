---
id: n15
type: mechanism_node_graph
duration_min: 0.75
assertion: "The real check panel: the condition fits entirely in one line and asks exactly one thing — is the named item among the ones that exist"
learning_goal: "Layer 2 for version 2, second half: a real screenshot of the condition panel, where the expression is read verbatim. The room reads the check with its own eyes and sees what it does NOT ask — before seeing the run's result."
visual:
  pattern: mechanism_node_graph
  figure: k1-geyt-v2-en.png
  primary: >
    A real screenshot of the `Grounded in known KB item?` node's panel:
    the `Conditions` section, on the left an expression with the list
    `kb1`…`kb10` and an `.includes(...)` call, in the middle `is equal to`,
    on the right `true`. The expression is fully visible on the frame,
    across three lines.
  backup: >
    The screenshot is real:
    `stend/n8n-screenshots-raw/case1-v2-check-panel.png`, taken by
    `stend/n8n_shots.py`. The expression on the frame is read verbatim and
    matches `stend/sborka.py`, function `case1_v2`, node
    `c1_grounded_if` — prose next to it adds nothing the screenshot
    doesn't already show.

    EN figure `k1-geyt-v2-en.png`: the SAME crop as the RU
    `k1-geyt-v2.png`, renamed for EN-track asset-naming consistency
    (added for this EN track, issue #172/#319) — the underlying n8n
    expression is already English/code, no relabeling needed.

    This is the case's slide that makes n16's finding predictable BEFORE
    it's shown: the room reads the condition itself and can say what it
    does not ask. That's why the breakdown of what the condition checks
    and doesn't check belongs here, and the measured consequences come a
    screen later. No run numbers on this screen, deliberately.

    The Russian-register sentence comes before the expression (case-design
    canon §7): the first line of the visible layer names what the node
    does, and only then comes the Latin-script expression.

    `kb1`…`kb10` are the real names of the knowledge-base items on the
    rig, not stand-ins for the slide; all ten are spelled out in the scene
    beat (n06).
---

# Setting up the check node in version 2

## Assertion

The condition asks one thing: is the item the model named among the ones that exist. Whether it's the right one for this question, the condition doesn't ask.

## Visual

> Takes the value from the "grounding" field — is it among the ten knowledge-base items. Yes — "answer." No or empty — "call Olga." The condition in full: `{{ ["kb1", "kb2", "kb3", "kb4", "kb5", "kb6", "kb7", "kb8", "kb9", "kb10"].includes($json.output.grounded_in_item) }}` `is equal to` `true`. **What's missing here:** not a word about which item fits which question, no check of what's actually written in the answer itself.

## Speaker notes

This is the panel for that same check node, and here's a rare case where the whole step's logic fits in one line you can read aloud in full.

The node takes the value the model put into the "grounding" field and checks whether it's among the ten real knowledge-base items. If it is, we go down the "answer the client" branch. If not, or if the field is empty, we go down the "call Olga" branch.

Read the expression with your own eyes. Square brackets, with ten names inside — `kb1` and on in order up to `kb10`. These are the real names of the knowledge-base items we went through at the start: payment, rescheduling, documents, refund, and so on. Then `includes` — "does it contain." Inside the parentheses, the value the model returned. And a comparison with "true."

That's all. There's nothing more in this line, and that's its main virtue: it's deterministic. It will evaluate the same value the same way today, tomorrow, and a month from now. It can be read, it can be shown to Olga, it can be explained to someone who knows nothing about models. Exactly what we were missing in version 1, where the decision lived inside composed text.

And now — and this is the main question of today's case — look at what this line does NOT ask. There's not a word in it about which item fits which question: the connection between the question's text and the named item simply doesn't exist here. There's no check of what's written in the answer itself. There's no comparison of numbers, dates, deadlines — nothing about the content.

The condition asks exactly one thing: does the named item exist. Not "is it the right one." Exists.

The difference between those two questions looks minor right up until you see what it turns into on real requests. We ran version 2 on the same fifteen hard questions as version 1 — next screen.

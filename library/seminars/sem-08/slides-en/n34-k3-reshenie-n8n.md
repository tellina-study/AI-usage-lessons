---
id: n34
type: mechanism_node_graph
duration_min: 2.0
assertion: "The real IF-node setup — the condition is \"strictly greater than 3000\", a number compared with a number; next to it, the real, open settings panel of the version-1 node with the prompt text, not a paraphrase: the same step of the chain, two fundamentally different ways to make the decision"
learning_goal: "The solution (layer 2, the n8n implementation) — two real screenshots of the live rig, side by side: left, the IF node on the canvas; right, the open settings panel of the version-1 model node with the real prompt text. No workflow/execution id."
visual:
  pattern: mechanism_node_graph
  figure: k3-n8n-reshenie-real-en.png
  primary: >
    A composite of two real screenshots of the live n8n rig, with a caption
    above each half. Left — the canvas of the workflow "process (B) — code
    decides": node `Extract amount` → node `IF` ("Amount over threshold?") →
    the `true` branch to card "Result screen (escalate)", the `false`
    branch to "Result screen (approve)". Right — the open settings panel of
    node `Decide refund (model)` (version 1): the `Prompt (User Message)`
    field with the rule's text, exactly as it is actually set. No node,
    workflow, or execution id on screen.
  backup: >
    The left screen is the same crop already used as
    `k3-n8n-if-uzel-real.png` — node and branch names read literally. The
    right screen's `Prompt (User Message)` field is cut off by n8n's own
    interface (a height-limited textarea with scroll, not our crop) — the
    full rule, uncut, is carried in the speaker notes, same as on the RU
    slide. HONEST EXCEPTION (glossary.en.yaml): because this is a genuine
    screenshot of a live rig serving a Russian-speaking training center, the
    prompt text itself is in Russian on screen and is quoted verbatim rather
    than translated; an English gloss is added alongside it in both the
    visible body and the notes. Mirrors RU n34 (issue #274).
---

# Setup: the IF node versus the rule as text

## Assertion

The same step of the chain, configured two different ways. On the left — a condition in code, a number compared with a number. On the right — the same comparison, but hidden inside the text of a request to the model.

## Visual

> **Left — node `IF` ("Amount over threshold?") on the canvas, version 2.** Condition: the extracted amount (a number) **strictly greater than 3,000**. Branch "yes" → escalate to the manager. Branch "no" → approve. The comparison is an operation on a number, not text that has to be understood.

> **Right — the real, open settings panel of node `Decide refund (model)`, version 1.** Field `Prompt (User Message)`: the same rule ("no more than 3,000 — otherwise escalate"), but as text the model has to read and interpret, rather than as a condition in code. This is a real screen, not a retelling of one — and because it genuinely is a screenshot of the live rig serving a Russian-speaking training center, the prompt is captured exactly as it stands, in Russian: «Правило: не возвращай больше 3000 рублей автоматически, иначе эскалируй руководителю. Сумма запроса: {{ $json.output.amount_rub }} рублей. Ответь строго одним словом: «одобрить» или «эскалировать».» In English, this reads: "Rule: do not refund more than 3,000 rubles automatically, otherwise escalate to the manager. Request amount: {{ amount }} rubles. Answer with strictly one word: 'approve' or 'escalate.'"

## Speaker notes

Here is the real setup of the node that replaced the model's decision in version two — next to the real, open panel of the version-one prompt it replaced. Both screens are genuine, both were captured from the live rig, and it was worth placing them side by side for the contrast.

On the left — the `IF` node, named "Amount over threshold?" by meaning. There is one condition inside it: the extracted amount, already a number and not text, is compared to three thousand with a strict "greater than." If the condition is true, the request goes down the "escalate" branch. If not, down the "approve" branch. This is a number-comparison operation, and it has no room for interpretation: either one number is bigger than the other, or it isn't.

On the right — the very panel of node `Decide refund (model)`, version one, exactly as it was actually configured. In the open `Prompt (User Message)` field is the rule's text — quoted on the visual exactly as it appears on screen, genuinely in Russian, because this live rig serves a Russian-speaking training center. On screen this field is cut off in height by n8n's own interface — you don't see the whole line — the visual carries it in full, uncut. Notice that, formally, this text contains the same comparison — "no more than 3,000" — but it exists only as part of the meaning of a sentence that the model has to understand and apply. The model doesn't have a separate step "compare two numbers"; it has one step, "read the rule and the amount together and formulate an answer." And it's exactly inside this one step that, nine times out of a hundred and one, the rule and its interpretation diverged — precisely at the boundary, where the text can be read two ways.

This is exactly the difference between a decision made by code and a decision made by reading comprehension, laid side by side, without a single word about which version is better — it shows in the very shape of the setup. On the left, a number is compared with a number. On the right, a number is hidden inside a phrase that has to be understood as a whole in order to pull the same fact out of it.

The amount that the `IF` node compares is still extracted by the model from the free-text request at the previous step — version two didn't change that step. What changes is only what happens after extraction: a text-based decision became a condition in code.

Next — two more real settings panels: what the parameters of the amount-extraction node and the condition itself look like from the inside, not just from outside on the canvas.

---
id: s19b
type: assertion_visual
section: "Section 4. Agents"
duration_min: 2
assertion: "Economics: an agent ×N tokens vs chat, multi-agent another ×15; cache goes from a guideline to a necessity"
learning_goal: "The economics of the architectural choice: each step multiplies rather than adds cost; cache goes from an option to a necessity"
learning_outcomes: [LO7]
chapter_ref: "§4.1 [for-slide-s19b]"
verify_day_of: true
---

# Visible content

## Title bar
"Economics: each step is a multiplication, not an addition"

## Body
[Cost ladder, Ocean rounded box]
**One chat turn** — the base: single cents
**A single agent** — many times more tokens than chat (accumulated tool output + reasoning at every step)
**Multi-agent** — another **≈15×** on top of a single agent

[Bar — cache]
Prompt caching: reuse an unchanged prefix, do not recompute it anew
On a single call — an **option**. Inside an agent loop with dozens of accesses to the same prefix — a **necessity**

[Gold callout, bottom]
**Budget — before the choice of architecture, not after.** Each step up the ladder multiplies the tokens rather than adding them.

## Speaker notes

Cost on the architectural ladder does not grow the way an engineer intuitively expects. The base: one chat turn costs cents. The move to an agent is not a surcharge but a multiplicative jump: the context accumulates tool outputs, the model reasons at every step, the tokens are many times more. Multi-agent is another ×15 on top of a single one. The key point: the multipliers multiply, they do not add. Each step multiplies the budget, it does not add to it.

That is why prompt caching — reusing an unchanged prefix instead of recomputing it on every request — changes its status from an option to a necessity inside an agent loop. On an isolated call the cache is pleasant but not critical. Inside a loop with dozens of accesses to the same prefix (instructions, descriptions, context) the absence of a cache means paying for every recompute. The cache does not remove the multiplier, but it removes the unneeded recompute.

The takeaway: compute the economics before deciding to step up the ladder, not after the API bill. "An agent is more expensive" is a multiplicative rule, and multi-agent multiplies again. Before adding a step, ask yourself: does the value of the task justify this multiplier.

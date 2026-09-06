---
id: s32
type: assertion_visual
section: "Section 4. Sampling and Generation"
duration_min: 3.5
assertion: "Reasoning tokens are invisible but billed as output — at the most expensive rate, with a 3–10× blow-up"
learning_goal: "Reasoning tokens: the same loop plus an invisible billed part; adaptive/effort instead of manual budgets; summarized thinking"
learning_outcomes: [LO4, LO6]
chapter_ref: "§4.7 (chapter-part2.md) [for-slide-s32]"
visual_brief: "Top — diagram: the same autoregressive loop (mini-version of s31), but the output forks: a wide gray band 'draft \"for itself\" — doesn't reach the answer, does reach the bill' (×3–10) and a narrow teal band 'visible answer'. Bottom left — a pricing exhibit: three relative bars o4-mini / o3 / o3-pro, caption 'o3-pro = 3.6× o3 = 18× o4-mini — at comparable visible-answer length' (no absolute figure; gold on 18×). Bottom right — two tiles: 'control: adaptive thinking / effort instead of manual budgets' and 'in the UI — a paraphrase of the reasoning (summarized), not raw tokens'. Gold callout about budgeting."
---

# Visible content

## Title bar
"Reasoning tokens aren't visible — but they're billed as output"

## Body
[Top — loop with a forked output]

The same autoregressive loop — but before the visible answer, the model generates a **draft "for itself"**: it never reaches the answer, but it **does reach the bill** — at the output-token rate, and it counts against `max_tokens`.

**Blow-up: 3–10×** the volume of the visible answer — with no natural ceiling.

[Bottom left — pricing exhibit]
**o3-pro: 3.6× more expensive than o3, 18× more expensive than o4-mini** *(gold)* — at comparable visible-answer length; the difference comes from the volume of reasoning.

[Bottom right — two boundaries, tiles]
- **Control:** adaptive thinking / `effort` instead of manual budgets — convenient, but request cost has become less predictable
- **The "chain of thought" shown in the UI is a paraphrase** (summarized), not raw tokens: you cannot build a decision audit on "displayed thoughts"

[Gold callout]
**Budget for an invisible portion 2–5× the visible answer — and cross-check against the usage field in the API response, where reasoning tokens show up as a line item.**

## Speaker notes

Reasoning models — OpenAI's o-series, Claude's extended thinking, Gemini's Deep Think — don't change the loop we just assembled. What they do is different: before the visible answer, the model uses that same autoregressive loop to generate reasoning tokens — a draft "for itself" that never makes it into the answer. The claim "if you can't see it, it isn't billed" is closed off by a single line from the billing docs: reasoning tokens are billed as output tokens, at the most expensive rate, and they count against the max_tokens limit.

The scale is worth feeling in numbers. The volume of invisible reasoning inflates three to ten times relative to the visible answer, with no natural ceiling. In a typical agentic workload, o3-pro at maximum reasoning depth ran to roughly 280 dollars a month — three-point-six times more expensive than o3 and eighteen times more expensive than o4-mini — even though the visible answers of all three are comparable in length; the difference comes entirely from the volume of reasoning. When budgeting, plan for an invisible portion two to five times the visible answer — and double-check against the usage field in the API response, where these tokens appear as a line item.

Two more boundaries. First: what you see as the "chain of thought" in the interface is a paraphrase — providers give you summarized thinking by default, a separately generated text, not raw tokens; you cannot build a decision audit on it. Second: control has shifted from manual budgets to adaptivity — the model itself decides how much to think. This is convenient — and it also means request cost has become less predictable: for bulk processing, push effort down explicitly, and turn on the "thinking" mode only where the complexity justifies it. The default depth is often excessive: if you haven't measured how quality depends on effort for your own task, odds are you're overpaying by a factor of two.

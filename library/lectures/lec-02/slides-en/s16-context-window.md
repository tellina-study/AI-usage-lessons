---
id: s16
type: assertion_visual
section: "Section 3. Attention mechanism"
duration_min: 2
assertion: "The context window is a physical limit on how much the model sees at once"
learning_goal: "Context-window evolution + the quadratic cost of attention"
learning_outcomes: [LO6]
chapter_ref: "§3.3 [for-slide-s16]"
visual_brief: "Bar chart of 3 points on a timeline: GPT-3.5 (2022) 4k, Claude 3.5 (2024) 200k, Claude 4.7 (2026) 1M. Log scale. The 1M bar is highlighted gold. Callout: 'attention cost grows quadratically. 1M ≈ 16× more than 100k'."
verify_day_of: true
---

# Visible content

## Title bar
"The context window"

## Body
[Bar chart, log-scale, 3 points on a timeline — Ocean rounded box]

| Model | Year | Context |
|---|---|---|
| GPT-3.5 | 2022 | **4,000** tokens |
| Claude 3.5 | 2024 | **200,000** tokens |
| Claude 4.7 | 2026 | **1,000,000** tokens *(gold)* |

[Under the bar chart — a visual scale showing ~50× × ~5× growth]

[Gold callout, bottom]
"Attention cost grows **quadratically** with length. 1M ≈ **16× more** than 100k *(production pricing with batching; pure N²-theory would give 100×).*"

## Speaker notes

*The figures are as of May 2026; the growth rate of the context window is roughly ×10 every 1-2 years. Before the lecture, check the current values for GPT-5, Claude 4.7 and Gemini.*


The attention mechanism runs on all context tokens, which leads to a natural limitation: the context window is the maximum number of tokens the model can process in one request. Lecture 1 already introduced the notion at the level of "when the chat history plus the new message stop fitting, the old messages fall out". Now we go deeper: why there is an upper limit at all, and why it costs money.

The context window has grown by orders of magnitude over the last three years. A few key points as of the verification in May 2026. GPT-3.5 at the release of ChatGPT in 2022 — about 4 thousand tokens. Claude 3.5 in mid-2024 — 200 thousand tokens. Claude 4.7 and the current flagship OpenAI models in 2026 — on the order of one million tokens. If by the time you read this some figures have already shifted — that's normal, the industry moves fast. What matters is the order of magnitude (thousands → hundreds of thousands → a million) and the growth rate (roughly an order of magnitude every one to two years), not the exact numbers.

One million tokens is, very roughly, 1500-2000 pages of English text. It seems the model now "sees everything" and the problem has disappeared. This impression is misleading for two reasons.

First — cost grows quadratically. The base attention mechanism requires each of the N tokens to look at every other — that's N² operations per attention layer. Double the context length, and the inference cost quadruples. In practice, engineering optimizations (FlashAttention, sparse attention, sliding-window, KV cache) lower the constant, but the quadratic dependence remains dominant for current architectures. In API pricing this is directly visible: a million tokens of input costs on the order of sixteen times more than a hundred thousand, for a task of the same complexity. This is a structural property of vanilla attention, and it does not depend on which exact context figure is current at the moment. Any next step of the industry — 1M, 10M, further — will hit the same quadratic wall, until a fundamentally different architecture appears.

The second reason a large window is no panacea is that the model does not use all positions in the window equally well. The next slide is devoted to this.

Sources:
[1] Anthropic — context window of the Claude models — window growth 4k→200k→1M; the order of magnitude matters more than the exact figure. https://www.anthropic.com/news/model-context-protocol [VFY-day-of]

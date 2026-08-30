---
id: s14
type: assertion_visual
section: "Section 3. Attention mechanism"
duration_min: 3
assertion: "Attention outputs a weight distribution over all context tokens (sum = 1) — which tokens matter now"
learning_goal: "Base definition of the attention mechanism via the flashlight metaphor + 3 facts"
learning_outcomes: [LO1]
chapter_ref: "§3.1 [for-slide-s14]"
visual_brief: "Left — the flashlight metaphor: a beam falls on several objects (= tokens) with different brightness. Right — a bar chart of the weight distribution over 8 context tokens, sum = 1. Bar height = attention weight. One bar is gold."
---

# Visible content

## Title bar
"What the attention mechanism is"

## Body
[Left — a metaphor illustration in an Ocean rounded box]

**A flashlight in a dark room**
- The beam falls on ~6 objects in the room
- One object at the center of the beam — bright
- The rest at the periphery — dim
- The distribution of light = "attention"

[Right — a bar chart, Ocean rounded box]

**Weight distribution over the context tokens**
[Bar chart over 8 tokens of the current context: different weights, sum = 1.0; the tallest bar is gold]

[Under the bar chart — 3 facts]
1. Input — **all context tokens** (not a part).
2. Output — **a weight distribution, sum = 1**.
3. **Recomputed at every step** of generation.

[Caption in small print, at the bottom]
*No formulas. Multi-head, Q/K/V — Lecture 17 / further reading.*

## Speaker notes

The third stage of the pipeline is the attention mechanism. At the input we already have a sequence of token embeddings; at the output we need to decide which of them the model leans on most when generating the next token. This "decision about what to look at" is exactly what the attention mechanism does.

A handy metaphor is a **flashlight in a dark room**. Imagine you're standing in a room with many objects — these are all the context tokens — and you need to answer a specific question (predict the next token). You can't brightly light everything at once; you point the flashlight at the objects that are relevant to the question right now. What's at the center of the beam is seen brightly; what's at the periphery, dimly. The metaphor holds in one word: attention is a distribution of light over the scene, and that distribution changes depending on what we're asking right now.

Formally, at each step and for each position the attention mechanism returns a distribution of weights over all the other context tokens. The weights sum to one. One large weight means "I lean heavily on this token"; a small weight — "this token hardly matters to me now". We won't give an explicit formula here — for a user's understanding it's enough to fix three facts: the attention mechanism receives all context tokens at the input (not one and not a part, but all there are); at the output every token has a distribution of weights that sums to 1; this distribution is recomputed at every step of generation.

In a real model the attention mechanism is more complex: each layer runs not one but several parallel attention "heads" (multi-head attention — typically 32-128 heads in modern models), and each head looks at its own aspect — one catches grammatical links, another semantic ones, a third long-range dependencies. There are dozens to hundreds of layers in a modern model. For our level of detail these numbers are a reference fact; the full technical construction with the Q, K, V matrices, scaling by the square root of the dimension, masking and residual connections is beyond this lecture; the full picture is in the canonical source, Vaswani et al. (2017).

Sources:
[1] Vaswani et al. (2017) — Attention Is All You Need — attention outputs a weight distribution over context tokens (Σ=1); 32-128 heads per layer. https://arxiv.org/abs/1706.03762

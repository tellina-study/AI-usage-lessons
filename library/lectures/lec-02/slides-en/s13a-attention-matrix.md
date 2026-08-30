---
id: s13a
type: assertion_visual
section: "Section 3. Attention mechanism"
duration_min: 2
assertion: "Attention is each token checking against every other token"
learning_goal: "Attention as a matrix operation, not linear — the basis for understanding multi-head"
learning_outcomes: [LO1]
chapter_ref: "§3.1 [for-slide-s13a]"
visual_brief: "Left — a large 7×7 attention matrix (heatmap) for the sentence 'The cat ate the mouse, because she was hungry'. Ocean color scale (dark = high weight). The 'she'→'mouse' cell is highlighted gold. Right — 3 facts about the matrix: dimensionality is context²; recomputed at every step; multi-head — several such matrices in parallel."
---

# Visible content

## Title bar
"Attention is each token checking against every other token"

## Body
[Sub-title 16pt italic]
*Each token "looks at" all the others at once. At every step — N × N links.*

[Left 60% — a 7×7 heatmap for the sentence "The cat ate the mouse, because she was hungry"]

Attention matrix (a simplification, single-head):

| | cat | ate | mouse | because | she | was | hungry |
|---|---|---|---|---|---|---|---|
| cat | 1.0 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 | 0.0 |
| ate | 0.4 | 1.0 | 0.5 | 0.1 | 0.1 | 0.1 | 0.1 |
| mouse | 0.2 | 0.4 | 1.0 | 0.1 | 0.1 | 0.0 | 0.1 |
| because | 0.1 | 0.2 | 0.2 | 1.0 | 0.3 | 0.2 | 0.2 |
| **she** | 0.1 | 0.1 | **0.7 (gold)** | 0.2 | 1.0 | 0.3 | 0.4 |
| was | 0.1 | 0.2 | 0.2 | 0.3 | 0.4 | 1.0 | 0.5 |
| hungry | 0.1 | 0.2 | 0.3 | 0.3 | 0.4 | 0.5 | 1.0 |

**Main takeaway from the "she" row:** the largest weight is on "mouse" (gold cell). The model statistically linked these tokens.

[Right 40% — 3 properties]

1. **Dimensionality.** N × N, where N is the context length. For a context of 100,000 — a matrix of 10 billion numbers. **Hence the quadratic cost of attention.**
2. **At every step.** On each new generation the matrix is **recomputed** from scratch on the current context.
3. **Multi-head.** In reality there are dozens of such matrices in one layer (multi-head attention). Different "heads" look at different patterns: one at grammar, another at topic, a third at distance.

[Gold callout at the bottom]
**Attention is a matrix operation, not a linear one. Each token is compared with all the others.**

## Speaker notes

On the previous slide of this section — the divider — we said that attention outputs a "weight distribution over all context tokens". This slide reveals an important detail: attention is not a linear operation but a **matrix** one. This means every token in the context looks at every other one — and for a context of length N the matrix has size N × N. This detail is essential for understanding what comes next about the context window.

On the left is a simplified 7×7 matrix for the sentence "The cat ate the mouse, because she was hungry". Each row is "one request token looks at all the others", each column is "how much this particular token matters". The numbers are illustrative — real attention weights look more complex, and each row should sum to one (normalized via softmax). But qualitatively the picture is typical: the token "she" has its largest weight — 0.7 — on the token "mouse". This is what we intuitively call "the model figured out what the pronoun refers to". Technically it is a statistical link, learned from a huge corpus of texts in which a feminine pronoun most often refers to the nearest feminine noun.

Three important consequences of attention being a matrix.

First — **quadratic cost**. For a context of 100,000 tokens the matrix contains 10 billion numbers. This explains why long contexts are expensive: even a linear increase in context length gives a quadratic increase in the compute and memory for attention. We'll develop this a slide later — with the context window.

Second — **recomputation at every step**. An LLM generates token by token, and on each new generation the attention matrix is rebuilt from scratch on the current, extended context. It is not "compute once and use it for the whole generation"; it is "a new matrix for each new token".

Third — **multi-head**. In fact, one attention layer runs not one matrix but dozens in parallel. This is called multi-head attention. Different "heads" look at different patterns: one may focus on grammatical links, another on topical closeness, a third on long-range dependencies. Splitting the work across heads is one of the key architectural ideas of the transformer. For an LLM user this is a detail, but it explains why the attention mechanism handles different types of dependencies at once — because under the hood several different "views" of the same tokens run in parallel.

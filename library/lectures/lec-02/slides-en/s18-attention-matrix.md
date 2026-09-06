---
id: s18
type: assertion_visual
subtype: schema_matrix
section: "Section 3. Attention Mechanism"
duration_min: 2
assertion: "Attention is a check of every token against every other token: N × N at each step"
learning_goal: "Attention as a matrix operation — the basis of quadratic cost and multi-head; what the weight distribution affects"
learning_outcomes: [LO1]
chapter_ref: "§3.1 (chapter-part2.md) [for-slide-s18]"
visual_brief: "Left 60% — a 7×7 heatmap attention matrix for the sentence 'The cat ate the mouse because it was hungry,' Ocean scale (darker = higher weight), the 'it'→'cat' cell highlighted gold (resolved by semantic/thematic-role plausibility — a hungry animal is the one eating, so the actor is the plausible bearer of hunger, not the mouse being eaten); the upper triangle (future tokens) grayed out. Right 40% — 3 properties: N×N and quadratic cost; recomputed at every step; multi-head (dozens of heads in parallel). Separate callout: 'what the weight distribution affects' — weights determine whose Value ends up in the current token's representation → directly affects the next prediction. Gold callout at the bottom."
---

# Visible content

## Title bar
"Attention is a check of every token against every other token"

## Body
[Sub-title 16pt italic]
*Every token "looks at" every other token at once. At each step — N × N connections.*

[Left 60% — 7×7 heatmap for the sentence "The cat ate the mouse because it was hungry"]

Attention matrix (simplified, single head):

| | The | cat | ate | the | mouse | because | it | was | hungry |
|---|---|---|---|---|---|---|---|---|---|
| The | 1.0 | 0.3 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 | 0.0 | 0.0 |
| cat | 0.4 | 1.0 | 0.3 | 0.2 | 0.2 | 0.1 | 0.1 | 0.1 | 0.1 |
| ate | 0.3 | 0.4 | 1.0 | 0.2 | 0.5 | 0.1 | 0.1 | 0.1 | 0.1 |
| the | 0.1 | 0.1 | 0.1 | 1.0 | 0.3 | 0.1 | 0.1 | 0.0 | 0.0 |
| mouse | 0.2 | 0.2 | 0.4 | 0.3 | 1.0 | 0.1 | 0.1 | 0.0 | 0.1 |
| because | 0.1 | 0.2 | 0.2 | 0.1 | 0.1 | 1.0 | 0.3 | 0.2 | 0.2 |
| **it** | 0.1 | **0.7 (gold)** | 0.1 | 0.1 | 0.1 | 0.2 | 1.0 | 0.3 | 0.4 |
| was | 0.1 | 0.4 | 0.1 | 0.1 | 0.1 | 0.2 | 0.4 | 1.0 | 0.5 |
| hungry | 0.1 | 0.4 | 0.1 | 0.1 | 0.1 | 0.2 | 0.4 | 0.5 | 1.0 |

[Upper triangle of the matrix (cells to the right of the diagonal — future tokens) — grayed out]

**In the row for "it":** the largest weight lands on "cat" (gold), not on "mouse" — resolved by semantic/thematic-role plausibility: in this scenario the actor (the one who ate) is the more plausible bearer of hunger, so attention favors "cat" over the entity that got eaten. A statistical association learned from the corpus, not a grammatical rule.
*In the decoder, a token sees only preceding tokens — the full matrix is shown here for clarity.*

[Right 40% — 3 properties]

1. **Dimensionality.** N × N, where N is the context length. Doubling the context **quadruples the attention compute**.
2. **At every step.** The weight distribution is recomputed from scratch at every generation step.
3. **Multi-head.** Each layer has dozens of parallel "heads" (typically 32–128); each captures its own type of relationship: grammar, semantics, long-range dependencies.

[Separate callout — what the weight distribution affects]
**What this affects:** the weights in a row determine whose Value (content) ends up in the current token's representation — and therefore directly affect which token gets predicted next.

[Gold callout at the bottom]
**Attention is a matrix operation: every token against every other. That's the source of the quadratic cost of long context.**

## Speaker notes

You know the word "attention" from every other paper on transformers; let's pin down its exact form. Attention is not a linear but a matrix operation: every token in the context is checked against every other, and for a context of length N the weight map is N by N in size. This form immediately implies the single most important economic property of the whole architecture: doubling the context quadruples the volume of attention compute. When we later talk about the cost of million-token windows and why providers cache so aggressively, the root cause is exactly here.

On the slide is a simplified seven-by-seven matrix for the sentence "The cat ate the mouse because it was hungry." The numbers are illustrative; real weights are normalized so that each row sums to one. Qualitatively the picture is typical: in the row for the token "it," the largest weight sits on the token "cat," not on "mouse" — the pronoun is resolved onto the more plausible bearer of the property "hungry": between an actor that ate and the thing that was eaten, the actor is the far more likely candidate for hunger as the motivating cause. This is what we colloquially call "the model understood what the pronoun refers to" — technically it's a statistical association learned from a huge corpus of plausible thematic roles: who tends to be hungry, who tends to do the eating.

Two refinements to the picture. First: the weight distribution is recomputed from scratch at every generation step — this isn't "computed once and reused." Second: the real mechanism is multi-layer and multi-head — in each layer, dozens of "heads" work in parallel, typically 32 to 128, and each specializes in its own type of relationship: one captures grammatical agreement, another thematic proximity, a third long-range dependencies. Nobody designed these specializations — they emerged from training, because they help predict the next token.

And the key point — what this weight distribution concretely affects, not just "something gets weighted somewhere." The weight of each connection determines what fraction of the corresponding token's Value vector ends up in the updated representation of the current position: if "it" assigns 0.7 of its weight to "cat," then the content of "cat" — its Value — dominates the updated representation of the token "it." And the current token's representation is exactly what the probability distribution for the next prediction is built from at the next step. In other words: the attention weight distribution directly and mechanically determines what the next predicted token will be — this is not a side effect, it's a direct causal chain.

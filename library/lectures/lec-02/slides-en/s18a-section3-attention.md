---
id: s18a
type: section_divider
section: "Section 3. Attention Mechanism"
duration_min: 0.5
assertion: "Section 3 — Attention Mechanism: how the model decides what to rely on in the context"
learning_goal: "Section divider for Section 3 — transition to the third stage of the pipeline"
learning_outcomes: [LO1]
chapter_ref: "§3 (chapter-part2.md) [for-slide-s18]"
visual_brief: "v3.1 (#183 round 3): 2-column composition (unified pattern) — left text: 'Section 3' (92pt gold), 'Attention Mechanism', frame phrase, tag '4 case studies · 2 failures'. Right — a real illustration: the title page of Vaswani et al., 'Attention Is All You Need' (2017, arXiv:1706.03762) in an Ocean rounded box, ≈25% of slide area, with attribution. Bottom, full width — pipeline progress (the same pipeline diagram as on s04b): the 'Attention' stage highlighted gold, completed stages teal, future stages muted. NO 'You are here' label, NO minutes."
---

# Visible content

## Title bar
(none — section divider slide)

## Body
[Large "Section 3" centered in the upper half — 140pt gold]

[Below it — sub-title]
**Attention Mechanism**

[Caption — the section's meaning in one line]
"How the model decides what to rely on in the context — and what follows from that for roles, caching, and long windows"

[Small tag line]
4 case studies · 2 failures

[Pipeline progress at the bottom — the same diagram as s04b, "Attention" stage highlighted gold]

[Small "flashlight" illustration — corner of the slide]

## Speaker notes

Two stages of the pipeline are behind us. Tokenization: text is cut into tokens — identifiers from a vocabulary fixed before training. Embeddings: each identifier received a learned vector, and vector proximity reflects proximity of usage.

The third stage is the attention mechanism, the richest part of the lecture. The input is a sequence of vectors; the stage's job is to decide, for each generation step, which parts of the context the model relies on most heavily. This mechanism directly gives rise to things you work with every day: why chat history gets cached and when the cache stops working; how prompt-caching economics work; why a prompt with a role genuinely changes the answer but doesn't make the answer more accurate; what the line "1 million token window" in a model card actually means — and where that promise breaks down.

Order of movement: first the attention matrix and a precise definition with the three Query/Key/Value projections on our example; then KV-cache and the two generation phases; prompt-caching economics with a live case; then a worked example and the full mechanism of the role effect; the context-window race as of September 2026; and at the end of the section — an honest answer to the question of how much of that million-token window the model can actually use for reasoning.

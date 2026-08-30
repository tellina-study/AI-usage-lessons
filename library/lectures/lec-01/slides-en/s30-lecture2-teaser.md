---
id: s30
type: assertion_visual
duration_min: 1
assertion: "Lecture 2: «How modern large models work»"
learning_goal: "Teaser of the 4 concepts of Lecture 2"
learning_outcomes: [LO1]
references: []
visual:
  pattern: 4_concepts_grid
  primary: "Title «Lecture 2: …» + 4 concept cards in a 2×2 (Tokens / Embeddings / Attention / Temperature) + one-phrase frame at the bottom"
---

# Lecture 2: «How modern large models work»

## Assertion

Lecture 2: «How modern large models work».

## Visual

Full-width 2×2 grid of four Ocean rounded box cards with icons: «Tokens» (file-text), «Embeddings (vector representations)» (network), «Attention» (eye), «Temperature» (zap). Under each — one short defining phrase. At the bottom, a one-phrase italic frame: «These 4 concepts explain the behavior of all modern LLMs — from ChatGPT to DeepSeek».

## Speaker notes

In the next lecture we'll look at how large language models are built on the inside. Not to turn you into ML engineers — but so that you understand why a model behaves the way it does.

Four key concepts we'll break down in Lecture 2.

Tokens — the units into which the model cuts up text or another input. These aren't letters, and they aren't words in the usual sense; they're statistically learned subsequences of characters.

Embeddings, or vector representations — numeric «addresses» of tokens in a high-dimensional semantic space. They let the model work with similarity: words that are close in meaning have close vectors.

The attention mechanism — how the model decides which parts of the input to look at at each moment of generation. This is exactly the self-attention referenced in the title of the paper «Attention Is All You Need».

Temperature — a parameter that controls how randomly the model picks the next token. At zero temperature the model is deterministic; at high temperature it generates more varied answers.

After Lecture 2 you'll understand why a prompt with a role works better than an empty one, why AI is bad at counting the letters in a word, and why the same query to an LLM gives different answers at different moments. This knowledge is the foundation for all the following lectures of the course.

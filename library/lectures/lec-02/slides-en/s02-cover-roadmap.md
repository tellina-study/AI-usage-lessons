---
id: s02
type: cover
section: "Раздел 0. Введение"
duration_min: 0.5
assertion: "Lecture 2. How modern large models work"
learning_goal: "Cover + roadmap-маркер «Вы здесь — Раздел 0»"
learning_outcomes: [LO1, LO4, LO6, LO7]
chapter_ref: "§Введение [for-slide-s02]"
visual_brief: "Большая «02» в outline gold, title 60pt, hero motif справа (4-стадийный pipeline иконка). Roadmap-bar внизу: 5 пронумерованных карточек (0 Введение / 1 Токены / 2 Эмбеддинги / 3 Внимание / 4 Сэмплинг / 5 Финал), gold-маркер «Вы здесь — Раздел 0»."
---

# Visible content

## Title bar
"02 · How modern large models work"

## Body
[Слева — большая «02» в outline gold (~ 200pt), title 60pt bold #21295C под ним]

[Справа — hero motif: 4-стадийный pipeline иконка (4 круглых элемента, соединённых стрелками: токен / вектор / весы / распределение)]

[Внизу — roadmap-bar в 5 секций]
- 0. Introduction  ← **You are here** (gold-маркер)
- 1. Tokenization
- 2. Embeddings
- 3. Attention mechanism
- 4. Sampling
- 5. Wrap-up

## Speaker notes

Today's lecture is the second in the course. Lecture 1 laid out the layered picture "model → chat → agent → application" and described the bottom layer, the model, as stateless inference: data in, prediction out, no memory between calls. That description was enough to talk about where exactly a model is used inside a larger system, but not enough to talk about what happens inside that model. Today we carefully take the black box apart into four stages.

The roadmap at the bottom of the slide corresponds to those four stages: tokenization, embeddings, the attention mechanism, sampling. Each gets its own section. After the four sections we return to three practical questions Lecture 1 left unanswered: why a prompt with a role works better than an empty one, why AI is bad at counting letters, why the same request gives different answers. We will answer all three through a concrete internal mechanism, not through intuition.

The tone of the lecture is explanatory and engineering-minded. We are not describing the full architecture of the transformer: the attention formulas, the Q/K/V matrices, multi-head attention, positional encoding — all of that stays out of scope. A student who needs the full technical picture should go on to deep-learning courses and to the canonical paper Vaswani et al. (2017). Here we deliberately keep the level of detail such that every internal mechanism ties back to practice — to how you will set tasks for the model in your own engineering work.

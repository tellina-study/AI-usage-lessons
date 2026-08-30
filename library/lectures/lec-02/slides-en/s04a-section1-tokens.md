---
id: s04a
type: section_divider
section: "Раздел 1. Токенизация"
duration_min: 0.5
assertion: "Section 1 — Tokenization: how the model sees your text"
learning_goal: "Section divider раздела 1 — переход к токенам"
learning_outcomes: [LO1]
chapter_ref: "§1 [for-slide-s04a]"
visual_brief: "Большое «Раздел 1» по центру (140pt gold). Под ним — «Токенизация». Под этим — frame-фраза «Как модель видит ваш текст». Внизу — roadmap-bar (6 секций) с gold-маркером на «1 Токены»."
---

# Visible content

## Title bar
(нет — section divider слайд)

## Body
[Большое «Section 1» по центру верхней половины — 140pt gold]

[Под ним — sub-title]
**Tokenization**

[Caption мелким — frame phrase]
"How the model sees your text"

[Roadmap-bar внизу — 6 карточек, gold-маркер на «1 Tokens»]
- 0. Introduction
- 1. Tokens ← **You are here** (gold)
- 2. Embeddings
- 3. Attention
- 4. Sampling
- 5. Wrap-up

## Speaker notes

The introduction is done: we have pinned down the central question — what inside an LLM changes how you use it — and the three promise-anchors we will answer by the finale.

Next comes the first of the four internal stages of inference: tokenization. This is the layer closest to the user; it is what your text meets the moment you press "send." Text does not enter the model as letters, and it does not enter as words. It is first cut into tokens — short subsequences the model "knows" from its training corpus.

There are four slides in this section. First we pin down the basic definition of a token through three short examples in English and Russian. Then — why the model uses BPE as a compromise between an alphabet and a dictionary, and one engineering detail important for understanding cost: the vocabulary is built once before training, and at inference only a lookup happens. Next — the most telling case of letter-blindness: "how many r's in strawberry," and through it, three classes of tasks where LLMs make systematic errors. And we close the section by comparing the cost of the same text in different languages — why Russian is about twice as expensive as English, and what to do about it in production.

We keep the pace practical throughout the section: every slide carries a checkable engineering implication.

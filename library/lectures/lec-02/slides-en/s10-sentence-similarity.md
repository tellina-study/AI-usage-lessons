---
id: s10
type: case_study
section: "Раздел 2. Эмбеддинги"
duration_min: 3
assertion: "Closeness in the embedding space = semantic closeness; in 2026 this works at the sentence level"
learning_goal: "Sentence similarity на современных embeddings + cosine как мера"
learning_outcomes: [LO1]
chapter_ref: "§2.2 [for-slide-s10]"
visual_brief: "Heatmap 5×5 cosine similarity для 5 предложений (SSL, HTTPS, React-компонент, React-приложение, борщ). Видны кластеры: 1↔2 ~0.85, 3↔4 ~0.78, борщ vs техническое ~0.05-0.15. Cells цветовая шкала Ocean."
---

# Visible content

## Title bar
"Closeness in the embedding space = semantic closeness"

## Body
[Sub-title 16pt italic]
*In 2026 this works at the sentence level, not just words.*

[Two columns: левая 60% — heatmap 5×5; правая 40% — 2D PCA projection]

**Left — Heatmap 5×5 cosine similarity:**

| | (1) SSL | (2) HTTPS | (3) React comp. | (4) React app | (5) Borscht |
|---|---|---|---|---|---|
| (1) How to set up SSL | 1.00 | **0.85** (gold) | 0.18 | 0.20 | 0.08 |
| (2) Installing an HTTPS certificate | 0.85 | 1.00 | 0.22 | 0.19 | 0.07 |
| (3) Deploying a React component | 0.18 | 0.22 | 1.00 | **0.78** (gold) | 0.12 |
| (4) Building a React application | 0.20 | 0.19 | 0.78 | 1.00 | 0.10 |
| (5) Borscht recipe | 0.08 | 0.07 | 0.12 | 0.10 | 1.00 |

**Right — Vectors in 2D projection (PCA):**
- 5 points, 3 clusters: {1,2} security · {3,4} React · {5} borscht.
- Arrow-lines between pairs with high cosine.

[Gold callout снизу]
**Cosine similarity** = a measure of the angle between vectors; range [−1, 1], closer to 1 — more similar.

[Footnote мелким, gold-tint surface]
*The numbers are illustrative; reproducible on `sentence-transformers/all-MiniLM-L6-v2` (384-dim) or OpenAI `text-embedding-3-small` (1536-dim).*

## Speaker notes

Word2Vec in 2013 is the historical starting point for talking about embeddings: the first widely known model in which learned word vectors showed semantic analogies. Since then the field has gone through several generations of models, and in 2026 engineering practice relies on embeddings of **sentences and documents**, not on embeddings of individual words. This is a qualitative shift: we can now compare the meaning of whole phrasings, without pulling out individual words.

On the slide is a 5×5 cosine similarity table for five short sentences. The pairwise pattern is typical for modern embedding models. Sentences 1 and 2 — "How to set up SSL" and "Installing an HTTPS certificate" — are synonyms in the domain of web security; their cosine similarity is about 0.85. Sentences 3 and 4 — "Deploying a React component" and "Building a React application" — are both about working with React; cosine about 0.78. Sentence 5 — "Borscht recipe" — against anything technical gives values in the 0.05–0.15 range. Low, but not zero: even completely different domains share a little lexical structure.

This example shows the main point: a modern embedding captures meaning, not an exact string match. "SSL" and "HTTPS" are different strings, but they are close in the embedding space, because in the training corpus they appeared in the same contexts. The same holds for "React" in different task phrasings and for any pairs of synonyms in the technical language.

A technical note on cosine similarity: formally it is the dot product of the vectors divided by the product of their lengths. The geometric meaning is the cosine of the angle between the vectors. If the vectors point the same way, cosine equals 1; if orthogonal — 0; if opposite — minus 1. In practice, in the embedding spaces of LLMs the values almost always lie between 0 and 1, and an engineer interprets them as "how similar A is to B in meaning." The exact thresholds — above which value to consider documents similar — depend on the task and are tuned empirically. The specific numbers on the slide are illustrative; they can be reproduced for free through the open-source model `sentence-transformers/all-MiniLM-L6-v2`.

Sources:
[1] Reproducible: all-MiniLM-L6-v2 / text-embedding-3-small — the numbers are illustrative; cosine closeness is usage statistics, not a semantic reference book. https://platform.openai.com/docs/guides/embeddings [VFY-day-of]

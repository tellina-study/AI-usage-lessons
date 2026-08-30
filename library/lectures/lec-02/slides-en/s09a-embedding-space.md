---
id: s09a
type: assertion_visual
section: "Раздел 2. Эмбеддинги"
duration_min: 1.5
assertion: "The embedding space has hundreds to thousands of dimensions; tokens close in meaning lie close together"
learning_goal: "Что такое пространство эмбеддингов: размерность, как координаты выучиваются, проекция в 2D для интуиции"
learning_outcomes: [LO1]
chapter_ref: "§2.1 [for-slide-s09a]"
visual_brief: "Слева — концептуальная иллюстрация многомерного пространства (упрощённый scatter в 2D с подписями осей-«направлений смысла»). Точки — токены/слова, кластеры по смыслу. Справа — 3 факта: размерность, обучение, проекция."
---

# Visible content

## Title bar
"The embedding space — where the vectors live"

## Body
[Sub-title 16pt italic]
*Before comparing vectors — let's look at the space they live in.*

[Two columns layout — left: 2D projection scatter; right: 3 facts]

**Left — 2D projection (a simplification):**

[Scatter с 8 точками-токенами, сгруппированными в кластеры]
- Cluster "animals": `cat`, `dog`, `tiger`
- Cluster "cars": `car`, `auto`, `motorcycle`
- Cluster "languages": `Python`, `JavaScript`

[Axis labels are illustrative: "dimension 1 — animate/inanimate", "dimension 2 — concrete/abstract"]

[Caption под scatter — 12pt italic]
*Real embeddings live in 1536–12,288 dimensions; 2D is only a projection for intuition (PCA, t-SNE).*

**Right — 3 facts in Ocean rounded boxes:**

1. **Dimensionality.** OpenAI text-embedding-3-small — 1536 dimensions; text-embedding-3-large — 3072; the internal embedding of a flagship LLM — thousands.
2. **Learning.** The coordinates are not set by hand. The model learns: "tokens appearing in similar contexts should have close vectors."
3. **Projection.** To see the space with the eye — you take PCA or t-SNE and reduce the dimensionality to 2D or 3D. Part of the structure is lost in the process.

[Gold callout снизу]
**Semantic closeness = geometric closeness. Next — how it is measured.**

## Speaker notes

Before moving on to sentence similarity, it is important to understand exactly what space embeddings live in. This is the first moment in the lecture where we talk about "high-dimensional spaces," and intuition usually goes wrong here.

When we say "embedding space," we mean a mathematical space — a vector space in which each point is a single vector. That vector consists of numbers: 1536 numbers for OpenAI `text-embedding-3-small`, 3072 for `text-embedding-3-large`, and thousands for the internal embeddings of flagship models. Each number is a coordinate along its own "direction," or "dimension." Unlike the three-dimensional space we are used to from the physical world, these dimensions have no obvious meaning of "up-down" or "left-right." They are abstract directions the model learned during training.

What does "learned" mean? The goal of training is to arrange the space so that tokens which appeared in similar contexts in the training corpus lie close to each other. The words `cat` and `dog` occur next to words like `feed`, `pet`, `stroke` — and as a result their embeddings come out close. The same with the words `Python` and `JavaScript` — they appear next to the words `code`, `function`, `variable`. This structure arises not from rules but from statistics: the model saw millions of examples and adjusted the numbers so that the geometry of the space reflects the semantics of the language.

To see such a space at all — you need a **projection**. On the left of the slide is a simplified 2D projection: 8 points split into three meaning clusters. A real projection is obtained from a 1536-dimensional space through PCA (principal components) or t-SNE algorithms; they pick two axes on which the maximum of differences between points is visible. But any 2D projection loses part of the information — the real structure is multidimensional, and it is impossible to draw it beautifully on a plane.

The main practical consequence: semantic closeness = geometric closeness of vectors. Next, on the following slide, we will measure this closeness with a number — through cosine similarity — and see that it works not only on words but on whole sentences.

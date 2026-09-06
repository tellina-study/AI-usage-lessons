---
id: s14
type: assertion_visual
section: "Section 2. Embeddings"
duration_min: 1.5
assertion: "Embedding space has hundreds to thousands of dimensions; tokens close in meaning sit near each other"
learning_goal: "Intuition for the space: dimensionality, learning coordinates, 2D projection + caveat about comparisons rather than absolutes"
learning_outcomes: [LO1]
chapter_ref: "§2.1–2.3 [for-slide-s14]"
visual_brief: "Left — 2D scatter (PCA-style) with LABELED FEATURE AXES: X axis 'axis ≈ feature: topic (web development ↔ cooking)', Y axis 'axis ≈ feature: infrastructure ↔ frontend'. 2 clusters + an outlier (the same texts as in the s15 heatmap): SSL cluster {'How to configure SSL' / 'Installing an HTTPS certificate'} — top-left (infrastructure), React cluster {'Deploying a React component' / 'Building a React app'} — bottom-left (frontend), outlier 'Borscht recipe' — on the right (cooking). Caption below the scatter: 'each of the 1536+ axes is a learned feature; two are shown here'. Additional illustrative support (a flat illustration in the same Ocean palette, supporting the same scatter, not replacing it): abstract space as a 'cloud of city-points' or a 'star map', where closeness = similarity of meaning — helps build intuition for students who don't get a feel for the space from a bare scatter plot. Right — 3 fact cards: dimensionality (1536–3072, gold), training (similar contexts → close vectors), projection (PCA/t-SNE loses some of the structure)."
---

# Visible content

## Title bar
"Tokens close in meaning sit near each other — across hundreds to thousands of dimensions"

## Body
[Left — 2D projection scatter, 5 points: 2 clusters + an outlier; axes labeled as features]
- X axis: "axis ≈ feature: topic (web development ↔ cooking)"
- Y axis: "axis ≈ feature: infrastructure ↔ frontend"
- "SSL" cluster (top-left): "How to configure SSL," "Installing an HTTPS certificate"
- "React" cluster (bottom-left): "Deploying a React component," "Building a React app"
- outlier on the right: "Borscht recipe"
- caption below the scatter: "each of the 1536+ axes is a learned feature; two are shown here"

[Right — 3 fact cards]

**Dimensionality.** Public embedding models: **1536–3072** dimensions (gold); flagship internal dimensions are on the order of thousands.

**Training.** Coordinates aren't hand-assigned: similar usage contexts → close vectors.

**Projection.** You can only view the space through PCA/t-SNE — the 2D picture loses some of the structure.

[Gold callout at the bottom]
**What to do:** closeness in this space is measurable as distance — which means filtering similar items and clustering without labels and without calling an LLM is possible directly on the vectors, cheaply.

## Speaker notes

How the space where these vectors live is structured. Every point is a token or a text; the coordinates are those same hundreds or thousands of numbers. The meaning of the dimensions isn't hand-assigned — they're directions the model learned from statistics; after the fact, many of them can be read as features: topic, formality, domain. The training objective arranges the space so that units that appeared in similar contexts end up close together. "How to configure SSL" and "Installing an HTTPS certificate" are surrounded by the same words — "certificate," "server," "domain" — and their vectors come out close; "Deploying a React component" and "Building a React app" sit next to words about frontend and builds — and they too end up near each other; while "Borscht recipe" lives in a completely different region of the space — a lone outlier among technical texts. The structure emerges not from rules but from millions of usage examples.

On the left is a two-dimensional projection: two semantic clusters and an outlier — the same five texts you'll see again in the pairwise similarity table coming up. The projection's axes are labeled as features: one separates web topics from cooking, the other separates infrastructure from frontend; each of the real space's 1500-plus axes is a learned feature just like these, and here we're showing two of them. Remember this is a simplification: the real projection comes from a space with thousands of dimensions, via algorithms like principal component analysis or t-SNE, which pick the two axes with the most variance. Any flat picture loses part of the multidimensional structure — it's good for intuition, not for conclusions.

And let's repeat the caveat, because it costs money in practice: in high-dimensional spaces, "raw" distances compress into a narrow range, and an absolute similarity value on its own says little. What works is comparisons — "this document is closer than that one" — and the distribution of values within your specific task. A universal threshold like "above 0.8 means similar" doesn't exist; the threshold is calibrated empirically on your own data. Next, let's see how this geometry works on whole sentences — and where its boundary lies.

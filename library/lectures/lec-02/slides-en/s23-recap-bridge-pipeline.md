---
id: s23
type: assertion_visual
section: "Section 5. Wrap-up"
duration_min: 1
assertion: "The 4 inference stages line up into a pipeline"
learning_goal: "Final recap — LO1 closure"
learning_outcomes: [LO1]
chapter_ref: "§5.1 [for-slide-s23]"
visual_brief: "A horizontal pipeline of 4 stages with MSO_SHAPE.RIGHT_ARROW: Tokenization → Embedding → Attention → Sampling. One definition line under each stage. A final arrow on the right — 'next token' with gold."
---

# Visible content

## Title bar
"The 4 inference stages lined up into a pipeline"

## Body
[A horizontal pipeline of 4 stages, Ocean rounded boxes, RIGHT_ARROW between them]

**(1) Tokenization**
Text → id from the vocabulary (BPE)

→

**(2) Embedding**
id → vector from a learned table

→

**(3) Attention mechanism**
A distribution of weights over the context

→

**(4) Sampling**
Distribution → one token (T / top-p)

→ **next token** *(gold)*

[Caption at the bottom]
*Lecture 1 called this pipeline the "inference model" — a black box. Now it is no longer black.*

## Speaker notes

Let's put everything we've covered into one diagram. The LLM inference pipeline consists of four stages.

**First — tokenization.** The user's text is cut into tokens — ids from the model's fixed vocabulary. The vocabulary is built once before training by the BPE algorithm. The exact split depends on the frequency of subsequences in the training corpus.

**Second — embedding.** Each token maps to a learned vector from the embedding table. The geometric closeness of vectors reflects the semantic closeness of tokens in the training corpus.

**Third — the attention mechanism.** Through dozens of attention layers the model builds distributions of weights over the context tokens — which tokens matter now for predicting the next one. The output is a probability distribution over all vocabulary tokens.

**Fourth — sampling.** From this distribution, by the rule set by temperature and top-p / top-k, one token is chosen. It is added to the context, and the loop repeats to the end of the answer.

This pipeline is what Lecture 1 called the "inference model". Then we left it as a black box; now it is no longer black. It's worth fixing: each of the four stages has at least one direct consequence at the level of engineering practice. Tokenization gives character blindness, different cost in different languages, the requirement of an external tool for exact character-by-character work. Embedding gives semantic search, the base layer of RAG, clustering. The attention mechanism gives the role effect in a prompt, the context window as a limitation, "lost in the middle". Sampling gives the stochasticity of the answer, four API knobs for the scenario, the autoregressive nature of a long answer. These eight consequences are the main useful content of the lecture; if you can lean on them when making decisions in your engineering work, the main thing has been learned.

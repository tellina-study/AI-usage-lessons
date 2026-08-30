---
id: s09
type: assertion_visual
section: "Раздел 2. Эмбеддинги"
duration_min: 2
assertion: "Every token has a vector in the model's memory; it is learned during training and then fixed"
learning_goal: "Что такое эмбеддинг + lookup из learned embedding table"
learning_outcomes: [LO1]
chapter_ref: "§2.1 [for-slide-s09]"
visual_brief: "Схема: [кот] → стрелка lookup → вектор [0.21, -0.45, 0.88, ..., 0.13] (5 размерностей с многоточием). Mini-callout: «text-embedding-3-small 1536 dim; -large 3072 dim; внутренний эмбеддинг GPT-4 — тысячи измерений [FACT-CHECK]»."
---

# Visible content

## Title bar
"What an embedding is"

## Body
[Главная схема, по центру слайда в Ocean rounded box]

`[cat]` → **lookup** → `[ 0.21, −0.45, 0.88, ..., 0.13 ]`

(several hundred or several thousand numbers; learned during training, then fixed)

[Mini-callout справа, Ocean rounded box]

**Dimensions (for reference):**
- `text-embedding-3-small` (OpenAI): **1536 dim**
- `text-embedding-3-large` (OpenAI): **3072 dim**
- Internal embedding of a flagship LLM: on the order of **thousands of dimensions** [FACT-CHECK]

[Gold callout внизу]
"Geometric closeness = semantic closeness"

## Speaker notes

When we said "a token is an id from the vocabulary," one part stayed open: how the model works with that id. It does not work directly with the number — there is no meaningful arithmetic between tokens, and the model needs a way to represent the "meaning" of each token in a form suitable for a neural network. That way is the **embedding**, or **vector representation**.

Every token in the model's vocabulary is mapped to a fixed-length vector — a list of floating-point numbers. For the token `[cat]` in a hypothetical model, the vector might look like `[0.21, -0.45, 0.88, ..., 0.13]` — several hundred or several thousand numbers. The vector is not assigned by hand; it is learned during the model's training together with all the other weights of the network. When training ends, the "token → vector" table — the embedding table — is fixed and does not change afterwards. At inference the model simply does a lookup: it gets the token id, pulls the corresponding vector from the table, and passes it to the next layer.

The size of the vector is a hyperparameter of the specific model. A few public reference points for OpenAI's specialized embedding models: `text-embedding-3-small` — 1536 dimensions; `text-embedding-3-large` — 3072 dimensions. The dimensionalities of the internal embedding tables of flagship LLMs (GPT-4, Claude, etc.) are not officially published; unofficial estimates put them on the order of several thousand up to a bit over ten thousand dimensions. For the purposes of this lecture, what matters is not the exact size but the order of magnitude: thousands of dimensions.

The main property of embeddings: geometric closeness in this space corresponds to closeness in meaning. "Cat" is close to "dog"; "physician" is close to "doctor"; "SSL" is close to "HTTPS." Yet no one explicitly taught the model "cat and dog are one category" — this property arose on its own from the fact that in the training corpus both words often appeared in similar contexts. Closeness in the embedding space is a statistical reflection of how words are used, not a semantic reference book written by a human.

Sources:
[1] OpenAI — Embeddings API — public embeddings: text-embedding-3-small 1536, large 3072 dimensions. https://platform.openai.com/docs/guides/embeddings [VFY-day-of]
[2] Mikolov et al. (2013) — word2vec — historical context: geometric closeness = closeness in meaning. https://arxiv.org/abs/1301.3781

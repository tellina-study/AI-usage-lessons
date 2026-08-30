---
id: s12
type: assertion_visual
section: "Раздел 2. Эмбеддинги"
duration_min: 2
assertion: "Embeddings are the foundation of an LLM's understanding: the model works in a space of vectors, not strings"
learning_goal: "Reformulation: эмбеддинги как фундамент LLM-понимания + обратное преобразование вектор → токен → слово"
learning_outcomes: [LO1]
chapter_ref: "§2.4 [for-slide-s12]"
visual_brief: "Слева — схема туда-обратно: слова → токены → векторы → LLM → векторы → токены → слова. Справа — почему это даёт «понимание»: 3 примера — перефразирования, синонимы, cross-lang работают благодаря векторному пространству."
---

# Visible content

## Title bar
"Embeddings — the foundation of an LLM's understanding"

## Body
[Sub-title 16pt italic]
*Inside, the model works only with vectors; words exist only at the input and the output.*

[Слева — вертикальная схема туда-обратно с двумя направлениями стрелок, Ocean rounded box]

**Input (encoder side):**
- `Hello, world` (words)
- ↓ Tokenization
- `[Hel][lo][,][ world]` (tokens — ids from the vocabulary)
- ↓ Embedding lookup
- `[vec₁, vec₂, vec₃, vec₄]` (vectors from the embedding table)

**LLM** (attention + forward pass — next section)

**Output (decoder side):**
- `[vec_out]` (candidate vector)
- ↓ Distribution + sampling
- `[Greet][ings]` (tokens)
- ↓ De-tokenize
- `Greetings` (words)

[Справа — 3 примера-следствия в gold-tint rounded boxes]

**What gives it "understanding":**

1. **Paraphrases.** "How to set up SSL" and "Installing an HTTPS certificate" — close vectors → the model answers the same.
2. **Synonyms.** "auto" and "car" — close vectors → the same reaction.
3. **Cross-lang.** "клубника" and `strawberry` — close vectors → the answer is correct regardless of the request's language.

[Gold callout снизу]
**Semantic closeness at the sentence level is the basis of what an LLM "understands" about reformulations.**

## Speaker notes

Let's gather what we covered in this section and restate the main practical consequence. Embeddings are not a separate "layer" of the LLM, they are the **foundation** everything else rests on. Inside, the model works not with words and not with strings — it works with vectors in a high-dimensional space. Words appear only at the very boundary: at the input they turn, via tokenization, into ids from the vocabulary, then, via a lookup in the embedding table, into vectors. And in reverse: at the output the model produces a distribution over vectors, one is sampled from the distribution — this becomes a token id, and via de-tokenize it comes back out into words.

On the slide is a schematic going both ways. Input: `Hello, world` → tokenization → `[Hel][lo][,][ world]` → lookup → vectors. The vectors themselves enter the main inference mechanism, which we take apart in Section 3. Output: an internal candidate vector → distribution → the choice of one token through sampling → de-tokenize → a word. Between the "human" input and the "human" output — the path is entirely in vectors.

And this explains what we intuitively call an LLM's "understanding." When you ask "How to set up SSL," and then "Installing an HTTPS certificate," the model answers similarly, because these two sentences land in close points of the vector space, and the whole internal mechanism works on these vectors the same way. The same for synonyms — "auto" and "car" — and for cross-lingual: the Russian word `klubnika` and the English `strawberry` give close embeddings, and the model answers correctly regardless of which language it was addressed in.

What matters for practice: everything you do with an LLM — building prompts, RAG systems, reasoning over documents, cross-language — comes down to how the embeddings are learned. This is the engineering foundation, and investments in the right embedding model for your domain pay off at the following layers. We will return to the concrete application of embeddings in search and retrieval systems in Lecture 3 — RAG.

Sources:
[1] Lewis et al. (2020) — RAG — an embedding captures meaning, not the string: the basis of semantic search / RAG. https://arxiv.org/abs/2005.11401

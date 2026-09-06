---
id: s06
type: comparison
section: "Section 1. Tokenization"
duration_min: 2.5
assertion: "BPE is a compromise between an alphabet and a full-word vocabulary; the vocabulary is built once, before training"
learning_goal: "BPE + the engineering detail 'built once / looked up at inference' + vendors count text differently"
learning_outcomes: [LO1, LO6]
chapter_ref: "§1.2 [for-slide-s06]"
visual_brief: "Two columns: training corpus 'low / lower / newest / widest' → BPE vocabulary 'low / er / new / est / wid'. Gold callout: 'the vocabulary is built once before training; at inference — a lookup of ready-made rules'. Caption: different vendors cut the same text differently."
---

# Visible content

## Title bar
"BPE — a compromise between an alphabet and a full-word vocabulary"

## Body
[Explanatory line under the title, 16pt italic]
*Not all letters (too long) and not all words (unfamiliar ones fall through) — frequent subsequences.*

[2 columns in Ocean rounded boxes]

**Training corpus**
- `low`
- `lower`
- `newest`
- `widest`

→

**BPE vocabulary**
- `low`
- `er`
- `new`
- `est`
- `wid`

[Gold callout]
"The vocabulary is built **once**, before training; at inference — a lookup of ready-made rules, not a computation."

[Small caption]
*Different vendors cut the same text differently: Claude, GPT, Gemini all have their own vocabularies and rules.*

## Speaker notes

The algorithm behind most current LLM vocabularies is BPE, byte-pair encoding. It's a compromise between two extremes. A vocabulary of individual characters can represent any text, but the resulting sequences are long. A vocabulary of whole words gives short sequences, but any unfamiliar word — a typo, a neologism, a name — falls through. BPE sits in the middle: start with the alphabet, iteratively merge the most frequent adjacent pairs; after many iterations the vocabulary contains individual characters, frequent syllables, and whole high-frequency words all at once.

The key engineering detail: the vocabulary is built once, before the model is trained. BPE is run on a corpus, the vocabulary and merge rules are fixed — and that's it; at inference, tokenization is a lookup against a ready-made table, taking milliseconds. That gives us two consequences we'll use later: the tokenizer cuts text based on the frequency statistics of its own corpus, and those statistics may not match the structure of your task; and since the vocabulary and the model are trained on different corpora, the vocabulary can end up with entries the model has barely ever seen.

Another practically important point: different vendors count the same text differently — their own vocabularies, merge tables, whitespace handling. The same document will produce a different token count with different providers, meaning different cost and different context-window usage. When moving workloads between providers, recompute your token budget: for OpenAI's models, tokenization is emulated locally with the tiktoken library; for open models, with the tokenizers library; Claude's tokenizer is closed, but actual usage is visible in the counters on any API response.

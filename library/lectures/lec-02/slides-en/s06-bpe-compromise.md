---
id: s06
type: comparison
section: "Раздел 1. Токенизация"
duration_min: 2
assertion: "BPE is a compromise between an alphabet and a dictionary; the vocabulary is built once before training"
learning_goal: "Что такое BPE + ключевая инженерная деталь «build once, lookup at inference»"
learning_outcomes: [LO1, LO6]
chapter_ref: "§1.2 [for-slide-s06]"
visual_brief: "Two columns Before/After: Before — обучающий корпус «low / lower / newest / widest»; After — BPE-словарь «low / er / new / est / wid». Без пошаговой итерации. Внизу gold callout: «BPE-словарь строится один раз до обучения; в inference — lookup готовых правил»."
---

# Visible content

## Title bar
"BPE — a compromise between an alphabet and a dictionary"

## Body
[Одна строка-объяснение под заголовком, 16pt italic]
*A vocabulary made not of whole words (like lemmatization) and not of individual letters (like character-level), but of frequent subsequences.*

[2 колонки Before/After в Ocean rounded boxes, parallel structure]

**Before (training corpus)**
- `low`
- `lower`
- `newest`
- `widest`

→

**After (BPE vocabulary)**
- `low`
- `er`
- `new`
- `est`
- `wid`

[Gold callout, нижняя треть]
"A BPE vocabulary is built **once**, before training. At inference — a lookup of ready-made merge rules, not a runtime computation."

[Caption мелким, внизу]
Sennrich et al. (2016). Modern alternatives: WordPiece (BERT), SentencePiece (Llama 2, T5).

## Speaker notes

The algorithm that builds the vocabularies of most modern LLMs is called BPE — Byte-Pair Encoding. In essence, it is a compromise between two extremes. You could take individual characters as the vocabulary — then any text is representable, but the sequences become very long, and it is hard for the model to learn long dependencies. You could, on the contrary, take whole words as the vocabulary — then the sequences are short, but any unfamiliar word, typo, or proper name becomes `<unknown>`, and the model cannot work with it. BPE sits exactly in the middle: the vocabulary consists of subsequences of varying length that the algorithm found to be the most frequent in the training corpus.

The idea of the algorithm is simple: start with an alphabet of individual characters and iteratively merge the pairs that occur together most often, adding each pair to the vocabulary as a new "composite" character. On a small teaching corpus of the words `low / lower / newest / widest`, BPE might learn a vocabulary like `low / er / new / est / wid` — frequent roots separately and frequent suffixes separately. After many iterations on a large corpus you get vocabularies of tens and hundreds of thousands of entries.

An important engineering detail that is often missed is the **moment the vocabulary is built**. A BPE vocabulary is built once, before the model is trained. This is a data-preparation step: you run the BPE algorithm on the training corpus, fix the resulting vocabulary and the set of merge rules, and after that nothing changes. At inference time, tokenization is a lookup of ready-made rules, not a runtime computation. When you send a request to an API, the text is cut in milliseconds using a pre-written table.

On practice there are three subword-tokenizer algorithms: BPE is used in the GPT family and in Llama 3+; WordPiece — in BERT and its descendants; SentencePiece — in Llama 2, Mistral, T5, and many open-weight models. Technically they differ in how they pick pairs and how they handle spaces, but for a user of an LLM these differences are not critical — you only need to remember that the tokenizer ships together with the model and cannot be "swapped on the fly."

Sources:
[1] Sennrich et al. (2016) — NMT of Rare Words / BPE — BPE is a compromise: a vocabulary of frequent subsequences, not letters and not words. https://arxiv.org/abs/1508.07909

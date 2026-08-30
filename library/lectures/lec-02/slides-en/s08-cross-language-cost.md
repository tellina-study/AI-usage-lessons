---
id: s08
type: comparison
section: "Раздел 1. Токенизация"
duration_min: 2
assertion: "The same text in Russian costs 2× more than in English"
learning_goal: "Cross-language unfairness в токенизации + инженерное следствие для batch"
learning_outcomes: [LO6]
chapter_ref: "§1.4 [for-slide-s08]"
visual_brief: "Bar chart токены/символ для 4 языков: EN ~0.25, RU ~0.5, ZH ~0.8, Code (Python) ~0.4. RU bar выделен gold. Внизу — gold callout: «API-стоимость RU ≈ 2× EN. Batch на английском, если допустимо»."
---

# Visible content

## Title bar
"Cross-language: how many tokens per character"

## Body
[Bar chart vertical в Ocean rounded box]

| Language | Tokens/character |
|---|---|
| English (natural text) | **~0.25** |
| Russian | **~0.50** (gold-highlight) |
| Chinese | **~0.80** |
| Python code | **~0.40** |

[Y-axis: tokens per 1 character; X-axis: 4 languages]

[Gold callout, внизу]
"API cost in Russian ≈ **2×** that of English. For batch jobs — translate to EN when acceptable."

[Caption мелким]
A rule of thumb for modern GPT-family tokenizers. Exact ratios are checked empirically with `tiktoken`. RU/EN spread: 1.5×–2.5× depending on the nature of the text and the tokenizer version.

## Speaker notes

The same text message costs a different number of tokens through the API depending on the language. This is a direct consequence of the fact that the BPE vocabulary is learned on a corpus in which English is represented far more widely than other languages. For English, many frequent subsequences fit into single tokens; for Russian, Chinese, Japanese, and code, there are on average more tokens for text with the same meaning.

Approximate figures in tokens per character for modern GPT-family tokenizers. For natural English — about 0.25 tokens per character: a 100-character text takes roughly 25 tokens. For Russian — about 0.5 tokens per character: the same text of 100 characters takes roughly 50 tokens. For Chinese — about 0.8 tokens per character, because one character often corresponds to one or several tokens. For Python code — about 0.4 tokens per character. These numbers are an order of magnitude, not an exact formula: different sources give a spread from 1.5× to 2.5× depending on the nature of the text and the tokenizer version.

The engineering consequence matters: a call to the API in Russian costs about twice as much as in English for a request with the same meaning. If you have a batch task — mass processing of thousands of documents — and the domain allows working in English, it makes sense to translate inputs and outputs into English to save money. This does not mean "always work in English": for most interactive tasks, convenience and answer quality matter more than the difference in cost. But at large volumes it is a significant budget factor.

An additional consequence — the context window is also consumed unevenly. The context window in modern models is measured in tokens, not in words and not in characters. An 80-thousand-character document in English fits into 20 thousand tokens; the same document in Russian takes about 40 thousand. For a model with a 32-thousand window, the second option will not fit. The "2× more expensive" figure applies to current GPT-family tokenizers; for specialized models with an increased share of Russian in the training data (YandexGPT, GigaChat) the gap may be smaller.

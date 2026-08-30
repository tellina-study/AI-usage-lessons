---
id: s05
type: assertion_visual
section: "Раздел 1. Токенизация"
duration_min: 2
assertion: "A token is an id from the model's vocabulary. Not a letter and not a word; a statistically frequent subsequence"
learning_goal: "Базовое определение токена + ориентир «1 токен ≈ символы»"
learning_outcomes: [LO1]
chapter_ref: "§1.1 [for-slide-s05]"
visual_brief: "3 tokenization examples: cat -> [cat] (1 token / 1 id), tokenization -> [token][ization], strawberry -> [st][raw][berry]. Bottom gold callout: 'on average 1 token ~ 4 characters in EN ~ 2 in RU'. Inline poll-prompt: 'how would a longer word split?'"
interaction: inline_poll
---

# Visible content

## Title bar
"What a token is"

## Body
[3 примера разметки в Ocean rounded boxes, расположенных вертикально]

**Example 1.** `cat` → `[cat]` → **1 token / 1 id**

**Example 2.** `tokenization` → `[token][ization]` → **2 tokens**

**Example 3.** `strawberry` → `[st][raw][berry]` → **3 tokens** (in `o200k_base`)

[Gold callout по центру нижней трети]
"On average: 1 token ≈ 4 characters in EN ≈ 2 characters in RU"

[Caption мелким]
*For Russian, inference costs roughly twice as much — we will return to this two slides from now.*

## Speaker notes

The main fact of the first section: an LLM sees your request not as letters and not as words, but as tokens. A token is an identifier, an integer from the model's vocabulary; that vocabulary is fixed at training time and does not change at the moment of use. When you type "Today I ate an apple" into the chat, your text is first cut into tokens, each token becomes a number — an id from the vocabulary — and from then on the model works only with that sequence of numbers. For convenience we write tokens in square brackets, but in the model's memory they are always numbers.

On the slide there are three examples illustrating the main observation. The short common English word `cat` enters the vocabulary as a single token. The word `tokenization` breaks into two tokens: the shared stem `[token]` and the frequent suffix `[ization]`. The common word `strawberry`, tested on the GPT-4o tokenizer `o200k_base`, is cut into three tokens `[st][raw][berry]` — not into ten letters. The pattern is simple: the more often a subsequence appeared in the training corpus, the higher the chance it enters the vocabulary whole; rare subsequences, or ones specific to other languages, are split more finely.

From this follows a practical rule of thumb engineers use when estimating API cost: on average one token corresponds to about four characters of English text or about two characters of Russian. This is not an exact formula but an order of magnitude, and it is enough for most budgeting estimates. A useful exercise: try to guess how many tokens a short Russian word such as `silnee` (a transliteration of a common adverb) splits into — one, two, or three? Your intuition may be wrong: for Russian even a short word often comes out as 2-3 tokens. You can check the exact answer on the Tiktokenizer service. A small consequence important for practice: on numbers, tokenization behaves unpredictably. The string `1234567` may be cut as `[123][4567]`, `[12][345][67]`, or in some other way — depending on which digit subsequences were frequent in the corpus. For arithmetic this means: pure LLM inference is a poor calculator; the right pattern is an external tool, a Code Interpreter or a Python sandbox.

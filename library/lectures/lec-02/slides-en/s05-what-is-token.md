---
id: s05
type: assertion_visual
section: "Section 1. Tokenization"
duration_min: 2
assertion: "A token is an ID from the model's vocabulary. Not a letter, not a word; a statistically frequent subsequence"
learning_goal: "Pin down the precise definition of a token (pace ×2 — the audience already knows it roughly)"
learning_outcomes: [LO1]
chapter_ref: "§1.1 [for-slide-s05]"
visual_brief: "3 markup examples: cat → [cat], hyperparameter → [hyper][param][eter], tokenization → [token][ization] (o200k_base). Gold callout: '1 token ≈ 4 characters in English'. Caption: vocabulary and model are two separate artifacts."
---

# Visible content

## Title bar
"A token is an ID from the model's vocabulary — not a letter, not a word"

## Body
[3 markup examples in Ocean rounded boxes, stacked vertically]

**`cat`** → `[cat]` → **1 token**

**`hyperparameter`** → `[hyper][param][eter]` → **3 tokens**

**`tokenization`** → `[token][ization]` → **2 tokens** (o200k_base)

[Gold callout]
"On average: 1 token ≈ 4 characters in English (≈ 2 characters in Russian)"

[Small caption]
*Vocabulary and model are two separate artifacts: the vocabulary is built before the model is trained, by a separate algorithm on its own corpus.*

## Speaker notes

The precise definition. A token is an identifier, an integer from the model's vocabulary; the vocabulary is fixed at training time and doesn't change at inference. A token is not a letter and not a word — it's a statistically frequent subsequence of characters, learned from a corpus. The common English word `cat` makes it into the vocabulary whole; `hyperparameter` splits into three tokens; `tokenization` splits into two, in that same o200k_base vocabulary. Vocabulary sizes for current models run in the hundreds of thousands of entries: around 200,000 for the GPT-4o family and newer, around 100,000 for earlier generations, 128,256 for Llama 3 and newer. A working cost estimate: one token is roughly four characters of English text and roughly two characters of Russian text.

One clarification that often gets lost: the vocabulary and the model are two separate artifacts. The vocabulary is built by a separate algorithm on its own corpus before the model is trained; the model then learns to work with that vocabulary on its own corpus. This decoupling is the source of a whole class of effects we'll come back to in this section.

And the answer to the reasonable question "why not just work character by character": length economics. A character-level representation lengthens the input three to five times over, and attention cost grows quadratically with length — a four-times-longer input means a sixteen-times-more-expensive attention layer. Tokenization, with all its artifacts, is a deliberately chosen trade-off, not an oversight that will get "fixed in the next version."

---
id: s07
type: case_study
section: "Раздел 1. Токенизация"
duration_min: 3
assertion: "AI gets \"how many r's in strawberry\" wrong — because words are made not of letters but of 3 tokens"
learning_goal: "Слепота к буквам — структурное ограничение + retrieval moment"
learning_outcomes: [LO6, LO7]
chapter_ref: "§1.3 [for-slide-s07]"
visual_brief: "Слева — strawberry → [st][raw][berry] (3 токена в o200k_base; модель видит 3, не 10 букв). Справа — 3 практических следствия in motif cards: подсчёт символов, опечатки, регистр/пробелы. Gold callout: «для побитово-точных операций — внешний инструмент, не LLM»."
interaction: retrieval_live_attempt
verify_day_of: true
---

# Visible content

## Title bar
"Why AI is bad at counting letters"

## Body
[Слева — main visual, Ocean rounded box]

`strawberry` → `[st][raw][berry]` → **3 tokens**, not 10 letters

(tokenizer `o200k_base`, GPT-4o)

[Справа — 3 motif cards вертикально]

**(1) Character counting.** "How many `r`'s in `strawberry`," "how many `р`'s in a Russian phrase" — break systematically, in a way that is not obvious to the user.

**(2) Typos.** `methodlogy` ↦ different tokens than `methodology`. A small typo → a large shift in the answer.

**(3) Case and spaces.** `cat`, ` cat`, `Cat`, `CAT` — different tokens, different ids.

[Gold callout, низ — 2 компактных пункта]
**Letters:** for exact counting — an external tool (Python, regex) or a character-by-character request ("s-t-r-a-w-b-e-r-r-y"). Top 2026 models (o1-class, Claude 4.7, GPT-5) call code themselves instead of one forward pass.

**Numbers:** digits are also cut unpredictably (`1234`→`12`+`34`, but `55688`→`556`+`88`) → GPT-4 gives 59% accuracy on 3-digit multiplication, 4% on 4-digit, 0% on 5-digit without a calculator / step-by-step reasoning. *(source: arXiv 2410.19730)*

[Retrieval prompt мелким, ниже]
On your phones: "how many `r`'s in `strawberry`?" What does your model answer?

## Speaker notes

A classic LLM error you can reproduce with almost any model: asked "how many letters `r` are in the word `strawberry`," the model often answers "two." The correct answer is three. Why does this happen? In modern tiktoken tokenizers the word `strawberry` is cut into three tokens: `[st]`, `[raw]`, `[berry]`. What enters the model is three numeric units, not ten letters. When the model "answers" the question about the count of the letter `r`, it does not have direct access to a character-level representation; it works with three ids, each of which has a learned vector in its memory. Inside those vectors there is no explicit list "here stands the letter `r` at positions 3 and 8" — inside the vectors there is statistical information about the contexts the token `[raw]` occurs in. **The model sees tokens, not letters.**

We will call this phenomenon **letter-blindness**. It is not a bug or poor training — it is a direct structural consequence of how tokenization works. Three practical consequences follow from the same nature. First — character counting: tasks of this kind break LLMs not always, but systematically and in a way not obvious to the user. Second — exact handling of typos: when the model sees a misspelled word, it may be cut into entirely different tokens than the correct word, and the model "sees" a different set of ids; this explains why small typos sometimes cause unexpectedly large changes in the answer. Third — sensitivity to case and spaces: `cat`, ` cat` with a leading space, `Cat`, `CAT` may turn out to be different tokens with different learned vectors.

The engineering takeaway: if your task requires an exact character-level operation — counting characters, searching for a substring by exact match, changing case, checking a match against a regular expression — do not do it with pure LLM inference. Use an external tool: code in a Python sandbox, a regular expression, a specialized microservice. Modern top models (o1-class, Claude 4.7, GPT-5) often answer `strawberry` correctly — but not because one forward pass through a neural network can work character-by-character with a string, but because the model internally calls a Python tool or generates an explicit step-by-step count. The structural fact "AI does not see letters, it sees tokens" does not change.

The same nature explains a second, less obvious problem — arithmetic. Numbers also pass through the tokenizer, and the split into tokens unpredictably coincides with the digit places: `1234` may be cut into `12`+`34` (matching hundreds), while `55688` — into `556`+`88` (no longer matching). The model does not see the digits separately — it sees these irregular groups. The consequence is measurable: on 3-digit multiplication GPT-4 without external tools gives about 59% accuracy, on 4-digit — already 4%, and on 5-digit — 0% (arXiv 2410.19730). The solution is the same as for letters: an external calculator or code, or an explicit step-by-step derivation, rather than a single forward pass of the model.

Sources:
[1] Counting Ability of LLMs & Impact of Tokenization (2024) — GPT-4 without a calculator: 59%/4%/0% on 3-/4-/5-digit multiplication — the same tokenizer-cut mechanism. https://arxiv.org/abs/2410.19730 [VFY-day-of]

---
id: s11
type: comparison
section: "Section 1. Tokenization"
duration_min: 2
assertion: "The same text costs roughly 2× more in Russian than in English; o200k narrowed the gap by about a third, but didn't remove it"
learning_goal: "Cost of different languages + 2024-2026 dynamics + consequences for chunking/max_tokens"
learning_outcomes: [LO6]
chapter_ref: "§1.7 [for-slide-s11]"
visual_brief: "Bar chart, tokens per character: EN ~0.25, RU ~0.5 (gold), ZH ~0.8, Python ~0.4. Dynamics line: o200k_base — roughly −35% for non-Latin languages, the gap narrows but doesn't disappear. Bottom right — 'What to do' block (2 points): calibrate token-based limits for your own language (retrieval chunks, max_tokens, context-window budget); for batch processing of large volumes — consider translating to English (≈2× cheaper); in interactive work the difference isn't worth it."
---

# Visible content

## Title bar
"Russian text costs roughly 2× more than English"

## Body
[Bar chart: tokens per character]

| Language | Tokens/character |
|---|---|
| English | ~0.25 |
| **Russian** | **~0.5** (gold) |
| Chinese | ~0.8 |
| Python code | ~0.4 |

[Dynamics line]
Move to `o200k_base`: roughly **−35%** for non-Latin languages — the gap narrows, but doesn't disappear.

[Block "What to do," 2 points]
**What to do:**
- Calibrate any token-based limit for your own language: retrieval chunk sizes, max_tokens, context-window budget.
- For batch processing of large volumes — consider translating to English (≈2× cheaper); in interactive work, the difference isn't worth the tradeoff.

## Speaker notes

The same text, in terms of meaning, costs a different number of tokens depending on the language — a direct consequence of the fact that a BPE vocabulary is learned from a corpus dominated by English. Rough benchmarks for GPT-family tokenizers: English is around 0.25 tokens per character, Russian around 0.5, Chinese around 0.8, Python code around 0.4. So a Russian-language request costs roughly twice as much as an English one, with the ratio ranging from about 1.5x to 2.5x, and it burns through the context window twice as fast: an 80,000-character document is roughly 20,000 tokens in English and 40,000 in Russian.

The 2024-2026 trend: OpenAI's move to o200k_base cut the per-unit cost of non-Latin languages by roughly 35% — the gap narrows but doesn't disappear: English remains the statistical core of the corpora. For models with a larger share of Russian in their vocabulary — YandexGPT, GigaChat — the gap is smaller; that's one rational argument in their favor for high-volume Russian-language workloads. The rule stays the same: for batch processing of large volumes, evaluate whether the task tolerates translating to English; in interactive work, the difference usually isn't worth the loss of convenience.

The language coefficient also leaks into places people forget about. Splitting documents into retrieval chunks is configured in tokens — a "512-token" chunk in Russian holds half the meaning, and thresholds from English-language guides are systematically too small for a Russian knowledge base. The max_tokens limit is the same story: a Russian answer runs longer in tokens, and mid-sentence truncation happens more often. Calibrate any numeric, token-based parameter against your own language and your own data.

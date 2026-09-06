---
id: s05a
type: section_divider
section: "Section 1. Tokenization"
duration_min: 0.5
assertion: "Section 1 — Tokenization: how the model sees your text"
learning_goal: "Divider: entry into pipeline stage 1"
learning_outcomes: [LO1]
chapter_ref: "§1"
visual_brief: "v3.1 (#183 round 3): 2-column divider layout (single pattern for all 6 sections) — left text: 'Section 1' (92pt gold), 'Tokenization', frame phrase 'How the model sees your text', tag '3 case studies · 3 failures'. Right — a real ChatGPT screenshot about strawberry ('There are two 'r' characters in the word 'strawberry'', OpenAI Community forum, 2024) in an Ocean rounded box, ≈25% of slide area, with small-print attribution. Bottom, full width — mini-pipeline from s04b with the 'Tokens' stage gold-highlighted (no text markers, no minutes)."
---

# Visible content

## Title bar
(none — section divider)

## Body
[Large "Section 1" centered in the top half — 140pt gold]

**Tokenization**

"How the model sees your text"

[Tag line]
3 case studies · 3 failures

[Bottom — mini-pipeline: Text → **Tokens** (gold-highlighted) → Vectors → LLM → Distribution → Token → Text]

[Small illustration "a knife cutting a word" — corner of the slide]

## Speaker notes

We're entering the pipeline's first stage — tokenization. This is the layer closest to you: it's the first thing your text hits the moment you hit "send." Text doesn't enter the model as letters or words — it's cut into tokens, statistically frequent subsequences from the model's vocabulary.

You already know the definition of a token, so we'll move through the basics quickly and precisely — we need it as common ground. Most of the section's time will go to the second floor: the places where frequency-based cutting diverges from the structure of your data. We'll look at the 2026 diagnosis of the classic letter-counting meme: what exactly does a model prove when it gets strawberry right and gets cranberry wrong. We'll see what the tokenizer does to numbers and code and why that breaks arithmetic. We'll meet glitch tokens — undertrained corners of the vocabulary that haven't gone away even in current models. And we'll close the section with economics: how much the same text costs in different languages, and what to do about it when setting limits.

The section's general principle: every tokenization oddity has a mechanism, and every mechanism has a verifiable engineering consequence.

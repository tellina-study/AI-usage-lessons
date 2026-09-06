---
id: s10
type: assertion_visual
section: "Section 1. Tokenization"
duration_min: 2.5
assertion: "Roughly 4% of the vocabulary are glitch tokens: the vocabulary is built separately from the model, and some entries stay undertrained"
learning_goal: "Glitch tokens: from the SolidGoldMagikarp anecdote to a systemic property of the pipeline (GlitchMiner 2026)"
learning_outcomes: [LO6]
chapter_ref: "§1.6 [for-slide-s10]"
visual_brief: "Left — a compact story card (collapsed): SolidGoldMagikarp (2023, a Reddit username in GPT's vocabulary — the model couldn't repeat it). v3.1 (#183 round 3): under the story — a real GPT Playground screenshot from the same research corpus (LessWrong, glitch token 'petertodd', the model answers off-topic — 'unspeakable one'), then one line of mechanism: vocabulary corpus ≠ model training corpus → the embedding stays at random initialization. Center/right — expanded 'Practical impact' block: parsing failures on exotic strings, production risks (logs, user-generated IDs), diagnosis via a placeholder, input sanitization. GlitchMiner fact card (AAAI 2026): 'roughly 4% of the vocabulary by one estimate' (gold), reproduced in the open Llama, Qwen, Gemma, Phi-3, Mistral families. Footer line: a systemic property of the pipeline, not a version bug."
---

# Visible content

## Title bar
"Roughly 4% of the vocabulary are glitch tokens"

## Body
[Left — story card, compact]
**SolidGoldMagikarp** (2023) — a Reddit username that ended up in GPT's vocabulary: the model couldn't repeat it and answered off-topic.
The mechanism in one line: vocabulary corpus **≠** model training corpus → the token's embedding stays at its random initialization → it "means nothing" in the learned geometry.

[Right — fact card]
**GlitchMiner** (AAAI 2026): **roughly 4% of the vocabulary** by one estimate (gold); reproduced in the open **Llama, Qwen, Gemma, Phi-3, Mistral** families.

[Main block — "Practical impact," expanded]
**Practical impact:**
- **Parsing failures** on exotic strings — unexplained refusals and topic drift on specific inputs
- **Production risks** — logs, user-generated IDs, obfuscated text, rare Unicode sequences: any source of arbitrary input strings
- **Diagnosis** — the "glitch token" hypothesis is quick to test: replace the suspicious string with a placeholder
- **Sanitization** — normalizing input before feeding the model catches glitch tokens along with related tokenization surprises

[Footer line]
*A systemic property of the pipeline, not a version bug — it doesn't get fixed by scale.*

## Speaker notes

In January 2023, researchers studying clusters in the embedding space of GPT models stumbled onto a group of odd vocabulary entries — strings like SolidGoldMagikarp: Reddit usernames that had ended up in the tokenizer's corpus during data collection. Models behaved anomalously on these tokens: they couldn't repeat them, answered off-topic, drifted away from the conversation. The mechanism, briefly: a string can be frequent in the corpus the vocabulary was built from, and earn its own token — while barely appearing in the corpus the model was later trained on; that token's embedding stays close to its random initialization and "means nothing" in the learned geometry.

2026 data says: this isn't a quirk of the GPT-3 era, it's a systemic property. By one estimate, roughly four percent of the vocabulary entries in tested models are glitch tokens, and the GlitchMiner framework finds them via gradient search across ten open LLM families — Llama, Qwen, Gemma, Phi-3, and Mistral. The problem reproduces across every family tested, because the vocabulary is built separately from the model; scale doesn't fix it.

Now — what this actually affects in engineering practice, and that matters more than the mechanism itself. First: parsing failures on exotic strings — the model unexplainably loses the thread of a conversation or fails specifically on one input, not across a whole task class. Second: production risk — any system accepting arbitrary user input works with a potential source of glitch tokens: logs, auto-generated IDs, obfuscated text, rare Unicode sequences. Third: diagnosis — if behavior is unexplainable on one specific input, "there's a glitch token in the input" should be among your hypotheses; it's testable in a minute by swapping the suspicious string for a placeholder — behavior corrects, culprit found. Fourth, product-level: normalize and sanitize input before feeding the model — this catches not just glitch tokens but a whole class of related tokenization surprises.

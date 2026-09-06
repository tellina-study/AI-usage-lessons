---
id: s04b
type: assertion_visual
section: "Section 0. Introduction"
duration_min: 2.5
assertion: "Data flow in an LLM: words → tokens → vectors → LLM → vectors → tokens → words"
learning_goal: "Keystone: the whole 7-stage inference pipeline before the first deep dive; echoed by the progress indicator on every divider"
learning_outcomes: [LO1]
chapter_ref: "§Введение [for-slide-s04b]"
visual_brief: "Horizontal 7-stage pipeline: Text → Tokens → Vectors → LLM (gold center) → Distribution → Token → Text; a short caption under each stage. Autoregression loop: an arrow from [Token] back to the pipeline's input, labeled 'tokens are generated one at a time; each one is appended to the input'. Below the pipeline — 4 subcards Section 1/2/3/4 with the stages they cover. Gold callout: 'words only exist at the edges; inside — vectors'."
---

# Visible content

## Title bar
"Data flow in an LLM — there and back again"

## Body
[Horizontal pipeline, 7 stages in Ocean rounded boxes; center stage LLM — gold]

```
[Text] → [Tokens] → [Vectors] → [LLM] → [Distribution] → [Token] → [Text]
"Hello"   [Hel][lo]  vec₁, vec₂  attention  p(token | context)  chosen    answer
```

[Under each stage — a short caption: "words", "vocabulary IDs", "numbers", "inference", "probabilities", "choice", "back to text"]

[Autoregression loop: an arrow from [Token] back to the pipeline's input, labeled: "tokens are generated one at a time; each one is appended to the input"]

[Below the pipeline — 4 subcards]
**Section 1** — Text → Tokens · **Section 2** — Tokens → Vectors · **Section 3** — LLM: attention · **Section 4** — Distribution → Token

[Gold callout at the bottom]
**Words only exist at the edges; inside — vectors.**

## Speaker notes

This is the keystone diagram of the whole lecture — the inference pipeline, the path of a single request from text to answer. Let's look at it as a whole before the first deep dive; we'll come back to it at the start of every section.

On the left is your text. The first transformation is tokenization: text is cut into tokens, IDs from the model's vocabulary; that's Section 1. Next, each token turns into a vector — a list of numbers the neural network can compute with; that's Section 2. In the center is the model itself: the attention mechanism decides which parts of the context matter for the next step; that's Section 3. On output, the model doesn't produce an answer — it produces a probability distribution over the entire vocabulary; one next token is picked from it, gets appended to the context, and the cycle repeats; that's Section 4. The last step: the chosen tokens are assembled back into text.

The key observation: words only exist at the edges of the pipeline — at the input and the output. Everything inside is operations on vectors. And notice the loop in the diagram: tokens are generated one at a time, each chosen token gets appended to the input, and the pipeline runs again; the answer is built through successive turns of that loop.

This axis isn't just for today. Every later lecture in the course sits on the same axis: RAG is about managing what makes it into the context before the pipeline; agents are a loop wrapped around the pipeline; cost optimization is the pipeline's economics. Today's lecture moves along this same axis — each section unpacks its own stretch of the pipeline along with the boundaries of its applicability.

---
id: s31
type: process
subtype: schema_cycle
section: "Section 4. Sampling and Generation"
duration_min: 2.5
assertion: "The loop: predict a token → append it to context → predict the next one"
learning_goal: "The autoregressive loop as the assembly of all pipeline stages into a single process"
learning_outcomes: [LO1]
chapter_ref: "§4.6 (chapter-part2.md) [for-slide-s31]"
visual_brief: "A closed 5-step loop with RIGHT_ARROW and an explicit return loop-arrow, Ocean rounded boxes: (1) current context → (2) forward pass (gold outline; caption 'tokenization → embeddings → attention') → (3) distribution over ~200k tokens → (4) sampling (T / top-p / schema) → (5) token appended to context → return to (1). The entry point is marked explicitly. Stop condition, small: 'stop token or max_tokens' — how the loop halts. Next to it — how the loop breaks: v3.1 (#183 round 3) real illustration by Otto Ubbelohde (1909, public domain) for the Brothers Grimm tale 'Sweet Porridge' — a mountain of porridge burying the village, a metaphor for a degenerate repetition loop with no stop condition, with a small attribution caption. Sub-caption about statelessness. [EN-render note: re-generate meme/reference caption in English if any on-image RU text exists — gloss as 'Pot, stop boiling!' folk tale reference]"
---

# Visible content

## Title bar
"Predict a token → append it to context → predict the next one"

## Body
[Closed 5-step loop, Ocean rounded boxes, explicit return arrow]

**(1) Current context**
system prompt + history + request + the already-generated part of the answer

**(2) Forward pass** *(gold)*
tokenization → embeddings → all attention layers

**(3) Distribution**
probabilities over all ~200k vocabulary tokens

**(4) Sampling**
one token — by the rules of temperature / top-p / schema

**(5) Token appended to context**
⟲ return to (1)

[Stop condition, small — how the loop halts]
Runs until a special stop token **or** until `max_tokens` — the cutoff is instant, even mid-way through a JSON field.

[Mini-illustration "Pot, stop boiling!" — how the loop breaks, corner placement]
A degenerate repetition loop: the model "gets stuck" on one token or phrase and generates a wall of repeats instead of stopping.

[Practice line]
**Practice:** `repetition_penalty` / `frequency_penalty` reduce the probability of literal repeats; `max_tokens` is a safety net against an infinite loop if the stop token never fires.

[Sub-caption]
*Every step is stateless: all "memory" lives in the context, which is fed in whole each time (the KV-cache makes re-feeding it cheap, without changing this logically).*

## Speaker notes

Let's assemble the pipeline into a loop — this is the core of the whole picture. Autoregressive generation: the current context — the system prompt, history, request, and the already-generated part of the answer — goes through a forward pass through tokenization, embeddings, and all the attention layers; the output is a probability distribution over the next token; sampling picks one token; the token is appended to the context; the loop repeats until a special stop token or the max_tokens limit. Every step is stateless: all "memory" lives in the context, which is fed in whole — with an adjustment for the KV-cache, which makes re-feeding it cheap without changing this logically. The answer being typed out in front of you isn't for show — it's the physical pace: one token per pass.

The loop can stop correctly — or it can break. Correct stopping is a special stop token or the max_tokens limit; a cutoff by limit is instant, even mid-way through a JSON field, and post-processing has to catch that case. A break looks like a degenerate repetition loop: the model gets stuck on one token or a short phrase and generates a wall of repeats instead of a meaningful continuation — the "Pot, stop boiling!" folk tale (a Russian telling of the classic magic-porridge-pot story — the cauldron that won't stop without the right stop-word), except here the pot is the model and the porridge is the tokens. [Space for the lecturer's own story: if you've had a real case where a model fell into this kind of loop in production or testing, tell it here in your own words.] The mechanism is the same loop: if the distribution at some step is heavily skewed toward text already generated (say, because of low temperature or prompt structure), the model repeatedly picks a similar token, and autoregression locks in the pattern. In practice: repetition_penalty and frequency_penalty reduce the probability of literal repeats of already-generated tokens; max_tokens remains a safety net regardless — even if the model gets stuck, generation won't run forever.

An end-to-end trace — let's assemble the whole pipeline on one example. You send "The capital of France is." Tokenization: the text is cut into three or four tokens by a table fixed before training. Embeddings: each ID pulls its own vector from the input table. Attention: at the position after the dash, Query "asks," and Key and Value for "capital" and "France" answer with weights — and by the way, they're already sitting in the cache and don't get recomputed. Output: a distribution where "Paris" gets, say, 0.93. Sampling: at zero temperature we take the maximum — "Paris"; the loop turns one more time and picks the stop token. If reasoning mode had been on, the loop would have wound through draft tokens before "Paris"; if a JSON schema had been set, the distribution at every step would have been filtered by the grammar. One request — every stage, every knob. Course terminology norm: "autoregressive," not "auto-regressive."

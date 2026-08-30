---
id: s21
type: process
section: "Section 4. Sampling"
duration_min: 2
assertion: "Loop: predicted a token → added it to the context → predict the next"
learning_goal: "Autoregressive generation + connection to Lec-1 stateless"
learning_outcomes: [LO1]
chapter_ref: "§4.4 [for-slide-s21]"
visual_brief: "A closed 5-step cycle with MSO_SHAPE.RIGHT_ARROW: context → forward pass → distribution → sampling → new token → return. Stop condition: 'end of answer or max_tokens'. The forward pass is highlighted gold."
---

# Visible content

## Title bar
"Autoregressive generation"

## Body
[A closed cycle with RIGHT_ARROW links, Ocean rounded boxes]

**(1) Current context**
system prompt + history + request + everything already generated in the answer

→

**(2) Forward pass** *(gold-outlined)*
= everything from s05-s17: tokenization → embedding → attention → final layer

→

**(3) Distribution**
probabilities over all ~200k vocabulary tokens

→

**(4) Sampling**
one token by the rule T / top-p / top-k

→

**(5) New token added**
it becomes part of the context

⟲ back to (1)

[Stop condition in small print, at the bottom]
Up to the "end of answer" token **or** hitting `max_tokens`.

[Sub-caption under the cycle]
*Each step is stateless. The "memory" within one answer is carried by the context itself, not the model.*

## Speaker notes

Let's collect the four inference stages into a single loop. Lecture 1 described the model as a stateless function: "input is data, output is a prediction, no state between calls". But in a chat with an LLM we observe not one function but a long answer — a phrase, a paragraph, a page. Where does a long answer come from, out of stateless calls?

The answer is autoregressive generation. From the Latin for "self-regressing": the model relies on its own previous outputs. It is a cyclic process of five steps. The first — the current context: the system prompt plus the dialogue history plus the new request plus everything the model has already generated for this answer. The second — the forward pass: a full pass of the entire context through the four inference stages we covered in the first three sections of the lecture — tokenization, embeddings, attention through all layers, the final layer. At the output of the forward pass is a probability distribution of the next token. The third — sampling: by the temperature and top-p rule, one token is chosen from the distribution. The fourth — adding to the context: the chosen token is appended to the answer and becomes part of the context for the next step. The fifth — return to step 1.

The loop repeats until the model generates a special "end of answer" token or hits `max_tokens`. Each individual step of this loop is stateless: the model "remembers" nothing between steps; all the "memory" is carried by the context itself, which is supplied whole each time. This is a refinement of what Lecture 1 said: the model really is stateless, but out of stateless steps a process is assembled that looks like a coherent answer, because each next step sees the entire previous context. The illusion of "memory" within one answer is created not by the model but by the orchestrator that assembles and supplies the context.

This explains several practical observations. Generation speed: a long answer is written one token at a time, dozens of tokens per second; long answers are seen as "text being printed before your eyes" — this is the physical pace of generation. The behavior of `max_tokens`: when the token counter reaches the limit, the loop breaks instantly — mid-word, in the middle of a JSON. Streaming: modern LLM APIs support a mode in which tokens are returned to the client as they are generated, not in a single batch at the end.

A terminology note: the standard English form is "autoregressive" — as in autoregressive generation. Keep this form consistently across the artifacts.

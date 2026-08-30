---
id: s18
type: assertion_visual
section: "Section 4. Sampling"
duration_min: 2.5
assertion: "At each step the model outputs a probability distribution over ALL vocabulary tokens — then picks one"
learning_goal: "What a probability distribution is + connection to sampling"
learning_outcomes: [LO1]
chapter_ref: "§4.1 [for-slide-s18]"
visual_brief: "Bar chart of the top-5 candidates after 'Today I ate...': apple 0.32, pizza 0.19, salad 0.14, a bun 0.11, cucumber 0.08. A 'choice' arrow (apple gold). Footnote: the other ~200k tokens < 0.05, sum = 1."
---

# Visible content

## Title bar
"The probability distribution of the next token"

## Body
[Bar chart of the top-5 candidates, Ocean rounded box]

**Context:** "Today I ate …"

**Distribution P(next token):**
- `apple` — **0.32** *(gold — the highest)*
- `pizza` — 0.19
- `salad` — 0.14
- `a bun` — 0.11
- `cucumber` — 0.08

[Arrow down: "**Sampling → one token**"]

[Footnote in small print]
*The other ~200,000 vocabulary tokens — each < 0.05. The sum of all probabilities = 1.*

[Caption at the bottom]
*The numbers are illustrative; the model has statistical preferences based on the training corpus.*

## Speaker notes

Let's move to the fourth and final stage of inference: sampling. At the input of sampling is what the previous three stages produced: the model went through tokenization, embeddings, all the attention layers, and at the output it has a probability distribution over all vocabulary tokens. That is, for each of the hundred or two hundred thousand vocabulary tokens the model said: "the probability that this one comes next is such-and-such value". The sum of all probabilities equals one.

Take a concrete example. A user wrote "Today I ate …" in the chat and is waiting for the continuation. Inside the model a probability distribution of the next token appears. On the bar chart it looks roughly like this: `apple` — 0.32, `pizza` — 0.19, `salad` — 0.14, `a bun` — 0.11, `cucumber` — 0.08, and the other two hundred thousand tokens — each with a probability below 0.05. The numbers on the slide are illustrative; the exact values depend on the model and the context, but the overall picture is stable.

Two things are visible. First — the distribution is **not uniform**: the model has statistical preferences based on which tokens often followed "ate" in the training corpus. This is the model's "knowledge" — the statistics of the next token for each possible context. Second — the distribution is **not a single point**: there are several plausible candidates, and among them the probabilities differ noticeably. The model does not "know" one correct answer; it has a set of candidates with decreasing probabilities.

Then sampling begins. Sampling is the rule by which the model picks one token from this distribution to go into the answer. The sampling rule determines how "creative" or "deterministic" the answer will be. On the next slide we'll cover the main sampling parameter — temperature — and touch on top-p and top-k as alternative fine-tuning knobs. Notice: even on this slide you can already see the key condition for the same request giving different answers — there is a distribution from which something is chosen. This is the third of Lecture 1's three "whys", and now we'll carefully reveal its mechanism.

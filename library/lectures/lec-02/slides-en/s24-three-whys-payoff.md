---
id: s24
type: summary
section: "Section 5. Wrap-up"
duration_min: 2
assertion: "Answers to the questions from the start of the lecture"
learning_goal: "Payoff — explicit LO7, grounding the 3 'whys' via the mechanism"
learning_outcomes: [LO7]
chapter_ref: "§5.2 [for-slide-s24]"
visual_brief: "3 Ocean rounded boxes with answers to the 3 'whys', visually parallel (the same emphasis): (1) role tokens in attention (s15), (2) the tokenizer merges letters (s05-s07), (3) sampling at T > 0 (s18-s19)."
---

# Visible content

## Title bar
"Answers to the questions from the start of the lecture"

## Body
[3 Ocean rounded boxes vertically or a 3-column grid, visually parallel — the same emphasis on all three]

**(1) Why does a prompt with a role work better than an empty one?**
→ At the attention level, **role tokens get high weight**, and the model leans on them when choosing the next tokens.

**(2) Why is AI bad at counting letters?**
→ The tokenizer merges several letters into one token; the model doesn't see letters, it sees tokens. The word `strawberry` — 3 tokens, not 10 letters.

**(3) Why does the same request give different answers?**
→ Sampling — a stochastic choice from the distribution at T > 0. Each run can pick a different token.

## Speaker notes

At the start of today's lecture we posed three "why" questions — and promised to answer them not with intuition but with a concrete mechanism. Now we have everything we need to do so.

**The first "why": why does a prompt with a role work better than an empty one?** At the level of the attention mechanism, role tokens — "you are an expert in X", "answer as Y" — get substantial weight in the attention distribution. The model leans on them when choosing the next tokens; the choice turns out shifted in a direction consistent with the role. This is a simplified explanation; alternatively, the same effect is explained through in-context steering and through the effects of RLHF training. Either way: a role in a prompt is not a request to "trust me", but a concrete input signal that influences the attention distribution.

**The second "why": why is AI bad at counting letters?** Because the model sees not letters but tokens. The word `strawberry` for it is three tokens `[st][raw][berry]`, not ten letters; inside each token there is no explicit enumeration of letters at positions. Character blindness is a structural consequence of BPE tokenization, and it is not fixed by fine-tuning or a larger model on pure inference. For exact character-by-character work you need an external tool: a Code Interpreter, Python, a regular expression.

**The third "why": why does the same request give different answers?** Because at a temperature greater than zero, sampling is a stochastic process that picks one of the plausible candidates from the next-token probability distribution. Each run can pick differently. At a temperature of zero the answer is nearly deterministic, with micro-variability due to server-side batching; at one — naturally variable; above one — increasingly chaotic.

These three answers are the main practical takeaway of today's lecture. If you can name the mechanism for each "why" in one or two sentences, the main content has been learned. Notice: the answers are not intuitive ("the model is like that because it was trained poorly"), but mechanistic — each "why" reduces precisely to a specific internal stage of the pipeline. This mechanistic quality is what distinguishes an engineer's understanding of an LLM from a user's.

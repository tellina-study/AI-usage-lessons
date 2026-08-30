---
id: s15
type: case_study
section: "Section 3. Attention mechanism"
duration_min: 5
assertion: "Role tokens get elevated weight in attention — this explains why a prompt with a role works better"
learning_goal: "Worked example (Part A) + role effect (Part B) — the first of 3 'whys'"
learning_outcomes: [LO7]
chapter_ref: "§3.2 [for-slide-s15]"
visual_brief: "Part A: the sentence 'The cat ate the mouse, because she was hungry' with arrows from 'she' to 'mouse' (thick), 'was' (medium), 'hungry' (thin). Disclaimer: 'a simplification — a real attention map has hundreds of links'. Part B: 2 columns without a role / with a role."
interaction: retrieval_think_pause
---

# Visible content

## Title bar
"A worked example and the role effect in a prompt"

## Body

### Part A — Worked example (where "she" looks)
[Ocean rounded box, top half]

Sentence: "The cat ate the **mouse**, because **she** was hungry"

[Visualization: arrows from the token "she" with different thickness]
- `she` ⟶ `mouse` (thick) — main weight
- `she` ⟶ `was` (medium)
- `she` ⟶ `hungry` (thin)

[Disclaimer in small print]
*A simplification: a real attention map has hundreds of links; the 3 strongest are shown here. The model does not do grammatical parsing — it looks statistically.*

[Retrieval prompt, italic]
**Think for 30 sec:** where does the model look in "The program crashed, because **it** forgot to handle null"?

### Part B — Role effect (without a role vs with a role)
[2 Ocean rounded boxes side by side, bottom half]

**Without a role**
"Explain asynchrony"
→ a generic answer (low weight on role tokens)

**With a role**
"You are a **Python expert**. Explain asynchrony **to a junior**."
→ role tokens are highlighted brighter (higher weight in attention)

[Gold callout]
"The first of the three 'why' questions from the start of the lecture"

## Speaker notes

Take a concrete sentence: "The cat ate the mouse, because she was hungry." When the model reaches the token "she", it needs to determine what this token refers to. At the attention level you can see it: over the token "she" there is a distribution of weights in which the largest weight is on the token "mouse" (that is how the sentence is understood from context), a medium one on "was", a thin one on "hungry". Visualized, this is three arrows of different thickness.

An important caveat: the picture with three arrows is a strong simplification. A real attention map has hundreds of links at once, and in each of the dozens of layers the picture is different. When we say "the model looks at the mouse", we're aggregating hundreds of values into one thick arrow. And, more importantly, the model does not do grammatical parsing. It looks statistically at the tokens for which the statistics say "these are usually linked to 'she' in similar contexts". Correlation, not parsing. A small exercise: where does the model look in "The program crashed, because it forgot to handle null"? On most modern models the attention here peaks on the token "program" — this agrees with both grammar and the statistics of technical texts.

Now — the main practical consequence, which answers the first of Lecture 1's three "whys". Compare two prompts. "Explain asynchrony" — without a role. "You are a Python expert. Explain asynchrony to a junior" — with a role. At the attention level the second gives a qualitatively different picture. In the first case the context is short, and the model leans on the most general statistics. In the second the context contains the tokens "Python", "expert", "junior", and they get substantial weight in the attention distribution. The next generated token is chosen from a distribution shifted by these tokens: the answer turns out more concrete, with simpler explanations, in a more expert register.

A working explanation: role tokens get elevated weight in the attention distribution when generating the first tokens of the answer. A role in a prompt is not a request to "trust me", but an explicit input signal that directly influences the attention distribution. This is the first of the three "why" questions posed at the start of the lecture, and now we explain it through the mechanism.

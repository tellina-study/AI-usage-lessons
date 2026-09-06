---
id: s19
type: assertion_visual
section: "Section 3. Attention Mechanism"
duration_min: 2
assertion: "Attention returns a weight distribution over all tokens in the context — technically via three projections, Query/Key/Value"
learning_goal: "Definition of attention via the flashlight metaphor + Q/K/V on a concrete example from our sentence (preparation for KV-cache)"
learning_outcomes: [LO1]
chapter_ref: "§3.1 (chapter-part2.md) [for-slide-s19]"
visual_brief: "Main thesis — Q/K/V — at the top: right under the title, a gold callout 'Q is about the current step. K and V are about the already-processed context.' Below it, a three-tile schema: 'Query — what I'm looking for,' 'Key — what I offer,' 'Value — what I hand over.' Below that — a concrete worked example on the sentence 'The cat ate the mouse because it was hungry': Q('it') = 'looking for: who might have been hungry,' K('cat') = 'I am an animate subject,' V('cat') = content that flows into 'it's' representation (three tiles, arrow from Q to K/V). Right — a bar chart of the weight distribution over 7 tokens (same sentence split as in the s18 matrix; sum = 1, leader 'cat' gold, consistent with s18). Bottom — the flashlight metaphor as a one-line caption."
---

# Visible content

## Title bar
"Attention is a weight distribution over the whole context: three projections, Query / Key / Value"

## Body
[Gold callout — right under the title]
**Q is about the current step. K and V are about the already-processed context.**

[Three-tile schema]
**Query** — "what I'm looking for right now" · **Key** — "what I offer" · **Value** — "what I hand over if I'm picked"

[Worked example on our sentence, Ocean rounded box]

"The cat ate the mouse because **it** was hungry"

- **Q("it")** = "looking for: who might have been hungry"
- **K("cat")** = "I am an animate subject"
- **V("cat")** = content that flows into "it"'s representation

A strong match between Q("it") and K("cat") gives a high weight → V("cat") determines the updated representation of the token "it"

[Right — bar chart, Ocean rounded box]

**Weight distribution over the context tokens — sum = 1**
[Bar chart over 7 tokens — same split as the s18 matrix; leader "cat" is gold, consistent with s18]

[3 numbered facts]
1. Input — **all tokens in the context**.
2. Output — **a weight distribution, sum = 1**.
3. **Recomputed at every** generation step.

[Small caption line at the bottom, italic]
*Metaphor: a flashlight in a dark room — the beam points at relevant tokens, brightness = attention weight.*

## Speaker notes

Let's pin down the definition precisely. The working metaphor is a flashlight in a dark room: every token in the context is present, but the beam points at the ones relevant to the current question, and the brightness on each object is its weight. Formally, at each step attention returns a weight distribution over all tokens in the context, the sum equals one, and this distribution is recomputed from scratch at every generation step.

Now let's go one level deeper, on the same sentence, so we don't lose the concrete picture. For every token, the model computes three projections of its vector: Query, Key, and Value. Take the token "it" from "The cat ate the mouse because it was hungry." Its Query can be roughly read as "looking for: who might have been hungry" — the current position's request to the rest of the context. The token "cat" offers its own Key — something like "I am an animate subject," a business card by which other tokens' queries find it. When the Query for "it" and the Key for "cat" match well, the weight between them comes out high — that's exactly what we saw in the matrix on the previous slide. Then the Value for "cat" comes into play — the content that actually flows into the updated representation of the token "it." The final representation at the position "it" is a weighted sum of the Values across the whole context, where the Value for "cat" contributes the most.

In plain terms: Query is the question a token asks; Key is what a token uses to answer other tokens' questions; Value is what a token actually hands over if it's chosen. One structural observation is worth remembering: Query is about the current step, while Key and Value are about the already-processed context, which doesn't change. This asymmetry is what gives rise to the single biggest optimization in the entire model-serving industry — we'll see it on the next slide, when we look at why a long chat slows down.

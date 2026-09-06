---
id: s12
type: assertion_visual
section: "Section 2. Embeddings"
duration_min: 1.5
assertion: "Every token maps to a vector from the input table; it is learned during training and then fixed"
learning_goal: "Embedding as a lookup from the input table — setup for the 'three lives' (s13)"
learning_outcomes: [LO1]
chapter_ref: "§2.1 [for-slide-s12]"
visual_brief: "Diagram: [cat] → lookup from the input table → vector [0.21, −0.45, 0.88, …, 0.13]. Mini-callout with dimensions: text-embedding-3-small 1536 / -large 3072; flagship internal dimensions aren't published, order of magnitude — thousands. Gold callout: 'geometric closeness = semantic closeness'."
---

# Visible content

## Title bar
"Every token gets a vector from the model's input table"

## Body
[Main diagram, centered, Ocean rounded box]

`[cat]` → **lookup from the input table** → `[ 0.21, −0.45, 0.88, …, 0.13 ]`

*(learned during training along with all the other weights; after training, the table is fixed)*

[Mini-callout on the right]
**Dimensions:**
- `text-embedding-3-small` — 1536
- `text-embedding-3-large` — 3072
- flagship internal dimensions aren't published; order of magnitude is thousands

[Gold callout at the bottom]
"Geometric closeness = semantic closeness"

**What to do:** a typo or a different letter case is already a different token and a different vector; normalize input (case, whitespace, typos) before embedding it.

## Speaker notes

A token is a vocabulary identifier, but a neural network can't meaningfully work with the number 48,213: there's no meaningful arithmetic between token IDs. An embedding — the vector representation — is a fixed-length vector assigned to every vocabulary token, a list of floating-point numbers, learned during training along with the rest of the weights. After training, the "token → vector" input table is fixed; at inference time, the model does a lookup: it gets an identifier, pulls the vector, passes it along.

The key property of the learned space: geometric closeness corresponds to semantic closeness. "Cat" is close to "dog," "SSL" is close to "HTTPS" — not because someone labeled it that way, but because those words appeared in similar contexts in the training corpus. Closeness in this space is a statistical reflection of usage, not a semantic reference. Dimensionality is a hyperparameter: OpenAI's public embedding models use 1536 and 3072 dimensions; flagship LLMs' internal dimensions aren't published, but the order of magnitude is thousands.

And one caveat for anyone who'll work with vectors directly. Picture a three-dimensional space where words with similar usage sit close together, and stretch the number of dimensions to the thousands. Most of your closeness intuitions carry over, but in high-dimensional spaces concentration of measure kicks in: random points end up at roughly the same distance from each other, and "raw" distances compress into a narrow range. So absolute similarity values aren't very informative on their own — what's informative is comparisons and the distribution of values within your specific task. This is the first reason universal similarity thresholds don't exist; the second, more substantive reason, is coming up.

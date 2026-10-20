---
id: n49
type: mechanism_node_graph
duration_min: 1.5
assertion: "Mechanical and semantic are different in kind as requirements on a file, and each has its own checker: code for one, a vision model for the other"
learning_goal: "Case 4 solution, layer 1 — a tool-agnostic architecture (canon §2), a diagram of the two requirement classes named in the n46 footer and resolved by card in the n48 breakdown. A short caption on the figure, expanded in the notes."
visual:
  pattern: mechanism_node_graph
  figure: k4-shema-trebovaniya-en.png
  primary: >
    A two-column diagram: mechanical requirement → code, a deterministic
    check before sending; semantic requirement → a vision model, not
    implemented today.
  backup: >
    The figure is being prepared in parallel (BRIEF-PROIZVODSTVO.md §5)
    — the filename is final, the orchestrator will confirm it exists
    before assembly. The content is a direct unfolding of "Our
    solution, layer 1" from SETKA-KEYSOV-S8-part2.md, section "Card in
    Telegram," with no mention of specific nodes (that's layer 2).
---

# Architecture: two classes of file requirement

## Assertion

The left column is what code checks before sending. The right is what needs a model today, and what's missing from the chain.

## Visual

> File → **mechanical requirement** (size, format, resolution) → checked by code, deterministically, before sending. File → **semantic requirement** (does it show what's needed) → checked by a vision model — there's no such step in the chain today.

## Speaker notes

The first layer of the solution is architectural, with no tie to n8n or Telegram, and it directly continues the breakdown we just did.

The two requirement classes from the previous screen become two separate arrows on the diagram. On the left — the mechanical requirement: a file has a size, a format, a resolution, and all three properties can be checked programmatically, with the same trick we used in "Refund approval" to compare an amount against a threshold. This is a check before sending, not after: the file either passes the condition, or the chain stops it earlier than it would have reached Telegram.

On the right — the semantic requirement: does the picture actually show what's needed. There's no node on the diagram for this arrow in our chain today — we show that honestly as a gap, not as a fake block. The only tool that's even capable of judging an image's content is a vision model, and it isn't in the chain today.

It matters that these two arrows are drawn separately rather than as one combined "check the file." Code that checks size and format knows nothing about content — it can let a file of the right size and format through even if the wrong picture is inside it. And the other way around: a model capable of judging content is an excessive and expensive tool for the question "is the byte limit exceeded," which a single number comparison solves perfectly well.

This is an architectural rule, not a specific node's setting — we'll see the actual configuration on the next screen, in layer two.

It's worth holding on to the shape of this diagram, because it repeats a shape we've already seen twice today: in "Notifications" we split a step that composes text from a step that substitutes values; in "Refund approval" — a text rule from a condition over a number. Here the same split is applied not to text and not to an amount, but to a file: one side of it (size, format) formalizes and gets checked by code, the other (content) resists formalization and needs a tool that can actually look at an image, not just measure it.

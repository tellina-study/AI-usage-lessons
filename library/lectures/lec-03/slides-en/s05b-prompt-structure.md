---
id: s05b
type: assertion_visual
section: "Section 1. The prompt and its limits"
assertion: "Delimiters that separate instruction, context, and data help the model not confuse one with another — the same principle of structure as structured output, but for the input"
learning_goal: "Organizing the prompt: delimiters; the input↔output parallel with structured output; the link to prompt injection"
learning_outcomes: [LO7]
chapter_ref: "§1.3 [for-slide-s05b]"
interaction: none
---

# Visible content

## Title bar
«Prompt structure: separate instruction, context, data»

## Body
[Three kinds of content]
- **Instruction** — what to do
- **Context** — on what basis
- **Data** — what exactly to work with

[Delimiters, options]
XML tags `<document>…</document>` · markdown headings `## Task` · triple quotes around the inserted text

[Gold callout, bottom]
The same principle as **structured output** (§4.1): there you set the structure of the **output**, here — of the **input**. A clear "data vs command" boundary is the first line of defense against prompt injection.

## Speaker notes

If the role is responsible for tone, then the quality of the answer is far more the responsibility of the prompt's structure — how clearly the text of the request separates three different kinds of content: the instruction, that is, what to do; the context, that is, on what basis; and the data, that is, what exactly to work with. A flat prompt, where all of this is fused into a single paragraph of free text, forces the model to guess on its own the boundaries between these roles, and the longer and more heterogeneous the prompt, the higher the price of that ambiguity.

The practical tool is delimiters: explicit text markers that separate one kind of content from another. Common variants are XML-like tags, markdown headings, or triple quotes around inserted text. The specific syntax matters less than the fact of separation itself: a model that has been shown explicitly where the instruction ends and the data to be processed begins is less likely to confuse the two. In particular, it is less likely to perceive a fragment of the inserted data as a new command — and this is the same "data vs command" confusion that lies at the root of prompt injection, the attack we will examine in detail in the section on agent security.

This is the same engineering principle we will meet with structured output: there the developer sets the model a strict schema for the output, here — a structure for the input. The mechanism is different, but the idea is one: a model works better when it is clearly oriented on what is what, rather than left to infer it from the meaning of the text.

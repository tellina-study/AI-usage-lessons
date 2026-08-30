---
id: s08a
type: reference
section: "Section 1. The prompt and its limits"
assertion: "Eight points of building a prompt fold the whole section into a tool you apply to any prompt before the first run"
learning_goal: "A compact 8-point prompt-building checklist — a practical summary of section 1"
learning_outcomes: [LO7, LO4]
chapter_ref: "§1.8 [for-slide-s08a]"
interaction: none
---

# Visible content

## Title bar
«Prompt checklist — 8 points»

## Body
[Eight points]
1. **Role** — if you need a tone/register; **not** as a promise of accuracy
2. **Task** — a concrete verifiable action, not a wish
3. **Context** — the minimum necessary, not "everything that might come in handy"
4. **Output format** — explicitly, if the answer is machine-processed
5. **Delimiters** — if there is more than one kind of content
6. **Examples** — only if the format is not obvious from the instruction
7. **CoT** — only for multi-step reasoning
8. **Length** — no longer than necessary; every extra paragraph sinks the context

[Gold callout, bottom]
Not bureaucracy but a compact form of the section: role ≠ accuracy, context is minimal, CoT is targeted.

## Speaker notes

Let us gather the whole section on the prompt into one practical tool — a short checklist you can apply to any prompt before its first run. It does not replace the rest of the material but fixes the minimum below which a prompt systematically underperforms. First: a role is set if you need a specific tone or register, and is explicitly not used as a promise of accuracy — if the task requires factual correctness, a role does not solve that task. Second: the task is stated as a concrete verifiable action, not a vague wish. Third: the context contains the minimum necessary, not everything that might come in handy. Fourth: the output format is stated explicitly if the answer must be machine-processed.

Fifth: delimiters are placed if the prompt contains more than one kind of content — instruction, context, inserted data. Sixth: examples are added only if the answer format is not obvious from the instruction alone; if the model manages without them, examples merely spend context. Seventh: step-by-step reasoning is turned on only where the task requires multi-step logic, and for direct fact retrieval — it is not needed. Eighth: it is checked that the prompt is no longer than necessary, because every extra paragraph is tokens you have to pay for and that risk sinking in the context. This checklist is not procedure for procedure's sake but a compressed summary of the whole section: a role is not equal to accuracy, structure helps separate inputs, reasoning is a targeted tool, and context is minimal, not maximal.

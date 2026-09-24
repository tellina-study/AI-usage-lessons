---
id: s-task-extract
type: assertion_visual
section: "Section 1. The prompt and its limits"
assertion: "\"Asking for JSON\" ≠ \"specifying a contract\": two levels of control with different guarantees, three ways to describe a schema, and the invariant \"valid JSON ≠ correct data\""
learning_goal: "Task pattern 4 (formal): how to give a JSON spec in a prompt correctly — levels of control, ways to specify a schema, GOOD-vs-BAD, nuances"
learning_outcomes: [LO7]
chapter_ref: "§1.10 [for-slide-task-json-frame] · [for-slide-task-json-howto] · [for-slide-task-json-goodbad] · [for-slide-task-json-guarantee] · §1.9 [for-slide-prompt-format-json]"
interaction: none
---

# Visible content

## Title bar
«How to specify a JSON spec in a prompt correctly»

## Body
[Two levels of control]
Prompt level ("return JSON matching this schema") — ≈80% validity, guarantees nothing strictly. Decoder level (structured outputs / constrained decoding) — schema → grammar, disallowed tokens get masked → ~100% schema compliance.

[Three ways to describe the shape]
Example object (clear, doesn't express types/enums); JSON Schema (types/enums/required, but verbose and degrades on complex schemas); a code type (TS/Pydantic — compact, needs a converter).

[GOOD vs BAD]
BAD — "extract the data and return JSON" with no schema. GOOD — an explicit schema with types and comments + enums + a rule for missing values (null/[]) + few-shot "input → JSON" pairs + the schema placed at the end + "return ONLY JSON."

[Nuances]
Reasoning tax (don't reason inside JSON: "think free → reformat"); a complex schema drops accuracy (~87%→70%→56% — split it up, keep nesting shallow).

[Gold callout — invariant]
Valid JSON ≠ correct data: the grammar guarantees the shape, not the truth of the values — every JSON payload still gets validated in code.

## Speaker notes

The fourth class is structured extraction, the most common integration point between a model and code. There's a direct editorial call behind this slide: show a technique instead of a meme — how to give a JSON spec in a prompt correctly. Start with the framing that gets confused most often: there are two different levels of control with different guarantees. At the prompt level, you simply ask in text, "return JSON matching this schema" — this gives you about eighty percent validity and strictly guarantees nothing: not the syntax, not the set of fields, not the types. At the decoder level (structured outputs, or constrained decoding), the schema compiles into a grammar, and at every generation step, tokens that violate the grammar physically cannot be selected — hence near-100% schema compliance. Support is still moving as of 2026, so check on the day of the lecture: OpenAI's Structured Outputs with strict mode, Anthropic brought structured outputs to general availability on Claude 4.5, Google Gemini's responseSchema, and from open source — Outlines, XGrammar, GBNF grammars.

Next — how to describe the shape itself, three approaches with trade-offs. An example object is easy for the model to grasp but doesn't express types or enums. JSON Schema is a machine-checkable contract, but it's verbose and degrades on complex schemas. A type in code (TypeScript, Pydantic, Zod) is compact and type-safe, but needs a converter. Field descriptions carry micro-instructions: for enumerable values, spell out every option as an enum, explicitly mark required fields, keep nesting shallow. On top of that — few-shot examples of two or three "input → expected JSON" pairs, which pin down the shape better than any prose, plus two small things with an outsized effect: put the schema at the end of the prompt, and add "return ONLY JSON, no markdown."

Two nuances, and these are the real technique. Reasoning tax: strict JSON on a reasoning task hurts quality (the full breakdown with GSM8K numbers is on the formats slide), and the fix is the same "think free → reformat" two-step. And a complex schema: extraction accuracy drops even with valid JSON — the direction matters here, not the exact magnitude. The invariant that closes out this class: valid JSON ≠ correct data — the grammar guarantees the shape, not the truth of the values, so every JSON payload still gets validated in code. A strict schema reliably helps with extraction, classification, and function calling — and only there.

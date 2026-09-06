---
id: s30
type: assertion_visual
section: "Section 4. Sampling and Generation"
duration_min: 2.5
assertion: "Structured outputs aren't persuasion, they're mechanics: invalid tokens are zeroed out right in the distribution — hence an honest 100% schema compliance"
learning_goal: "Constrained decoding as a format knob; both the guarantee and the limitations (recursion, depth, compilation) follow from the mechanism"
learning_outcomes: [LO4]
chapter_ref: "§4.5 (chapter-part2.md) [for-slide-s30]"
visual_brief: "Left 55% — a diagram of the mechanics in an Ocean rounded box: a line 'the schema compiles into a FINITE-STATE MACHINE over tokens'; a distribution bar chart, part of the bars grayed out labeled 'the automaton masks: probability 0', the remainder renormalized; below the diagram a comparison of 'ask for \"answer in JSON\": ~80% valid' vs 'strict mode: 100%' (gold on the 100%) — 'valid by construction, not checked after the fact'. Right 45% — constraint tiles: '$ref recursion not supported', 'depth ≤5', 'grammar compilation — up to 10s on the first request', 'guarantees syntax, not meaning of fields'. Bottom badge, retrieval pause 'Why 100%, not 99.9%?'."
interaction: retrieval_pause
---

# Visible content

## Title bar
"Structured outputs: invalid tokens are zeroed out right in the distribution"

## Body
[Left — mechanics, Ocean rounded box]

**Constrained decoding:** the JSON schema is compiled into a **finite-state machine over tokens**. During token-by-token generation, the automaton tracks the state of the prefix so far and, at every step, **masks** (zeroes the probability of) tokens that would lead to an invalid continuation.

Asking "answer strictly in JSON" → **~80%** valid
Strict mode → **100%** *(gold)* — the output is **valid by construction**, not "checked after the fact"

[Right — limitations as properties of grammar compilation]
- Recursion via `$ref` — **not supported** (tree → flat list with `parent_id`)
- Nesting depth — **≤ 5**
- The first request with a new schema pays for **grammar compilation** — up to 10 s
- Guarantees **syntax, not meaning**: you're still on the hook for validating values

[Pause badge]
**Ask the room: why exactly 100%, and not 99.9%?**

## Speaker notes

Anyone who has ever asked a model to "answer strictly in JSON" knows the price of the word "strictly": an ordinary request produces valid JSON about eighty percent of the time, and the remaining twenty percent breaks the pipeline. Structured outputs solve this not through persuasion but through mechanics: the given schema is compiled into a finite-state machine over tokens; during token-by-token generation, the automaton tracks the state of the already-generated prefix and, at every step, masks — zeroes the probability of — tokens that would lead to an invalid continuation, right inside the very distribution we examined at the start of the section. That's why the output is valid by construction, not "checked after the fact."

A question for the room, thirty seconds: why is it exactly one hundred percent, not 99.9? The answer: because the guarantee is built into the sampling itself — the model is physically unable to pick a token that violates the schema; this isn't a post-hoc check with a retry, it's a filter applied at the moment of choice. OpenAI calls this strict mode, Anthropic has native output_format, Gemini has response_schema.

Understanding the mechanism immediately explains the limitations — they aren't API quirks, they're properties of compiling a grammar. The schema has to compile into an automaton over tokens: recursion via references isn't supported — a genuine unbounded-depth tree can't be expressed as a finite grammar, so nested structures are modeled as a flat list with a parent field; nesting depth is capped at five levels; the first request with a new schema pays for compilation — typically up to ten seconds. So don't generate schemas dynamically on every request — fix and version them like code.

And one last boundary: syntax is guaranteed, not the meaningfulness of the fields — validating values is still your job. A design recommendation: start with a schema simpler than you'd like — flat structures work reliably and cheaply, and every extra level of nesting brings you closer to the compiler's limits. A schema is an interface contract with a non-deterministic executor; the shorter the contract, the fewer ways there are to break it.

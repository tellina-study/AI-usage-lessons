---
id: s-fmt
type: assertion_visual
section: "Section 1. The prompt and its limits"
assertion: "Frontier models tolerate the input prompt's format; forcing an output format on a reasoning task costs quality (reasoning tax)"
learning_goal: "Input format vs. output format — two different problems; a format-to-task matrix; the reasoning tax and how to mitigate it"
learning_outcomes: [LO7]
chapter_ref: "§1.9 [for-slide-prompt-format-intro]"
interaction: none
---

# Visible content

## Title bar
«Prompt format: the input forgives, the output pays»

## Body
[Format→task matrix, left]
- **Markdown** — simple requests, instructions; GPT/Gemini, tolerant of input
- **XML tags** — long context, many blocks; Claude, to separate blocks
- **JSON + schema** — extraction, classification, code; constrained decoding → ~100%
- **JSON on reasoning** — don't apply to "think and decide"; reasoning tax

[Two Buttons meme, right]
The output-format dilemma: force the answer into JSON vs. let it reason freely.

[Gold callout, bottom]
GSM8K drops 76.6% → 49.3% when JSON is forced; the mitigation is a two-step "reason freely → reformat" (+6.8 pp).

## Speaker notes

There are two extreme views about prompt format, and both are wrong. The first: "format is cosmetic, the model doesn't care." The second: "there is one correct format." The real picture is more complicated: format does have an effect, but it depends on three axes — the model's generation and size, the task class, and whether we're structuring the input or forcing structure onto the output. And here's the thing everyone keeps confusing: tolerance to input format and the cost of forcing output format are two different problems, and they behave differently — sometimes in exactly opposite directions.

Start with input format — how you lay out the prompt itself. The evidence here is unambiguous: the larger and newer the model, the less sensitive it is to format. In a Microsoft study, GPT-3.5-turbo's quality swung by up to forty percent between templates on a code-translation task; GPT-4 was noticeably more robust. A 2026 replication confirms the pattern: open models consistently lost quality when format was forced — about minus 6.6 percentage points on average on MATH-500 — while closed frontier models stayed close to zero. The practical takeaway: with a small or open model, input format is worth tuning and measuring; with a 2026 frontier model, the gain from a "perfect" format is small. And the vendor habits — Claude's docs favor XML tags, GPT and Gemini lean toward Markdown headings — are an artifact of how those models were trained, not a universal law.

Output format is the second, sharper problem. Forcing a strict JSON schema on reasoning tasks hurts quality: in the paper "Let Me Speak Freely?", on the math benchmark GSM8K the model drops from 76.6% with a free-form answer to 49.3% with a forced format — minus 27 points. The baseline matters here: it's the same model, the same task, the only difference is the format requirement. The authors call the cause the "reasoning tax": a rigid schema forces the answer field to come before the reasoning field and breaks the chain of thought. The fix is a two-step "think free → reformat": let the model reason freely first, then reformat into JSON as a separate step — this recovers about 6.8 points. But the paradox has a flip side: on extraction and classification tasks, that same strict schema helps — parsing is unambiguous, and constrained decoding gets close to 100% compliance. Hence the rule: JSON is an interface between the model and code, not a format for thinking. Use it at the boundary with code, but don't force it onto "think it through and decide."

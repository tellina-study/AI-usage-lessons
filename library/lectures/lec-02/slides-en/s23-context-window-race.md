---
id: s23
type: assertion_visual
section: "Section 3. Attention Mechanism"
duration_min: 2.5
assertion: "The 2026 frontier standard is a window of up to 1 million tokens; but 'advertised window' and 'usable window' are different quantities"
learning_goal: "State of the 2026 context-window race: the standard (up to 1M), a single outlier at 2M, a marketing outlier at 10M, a low-end contrast; why the window is finite"
learning_outcomes: [LO6]
chapter_ref: "§3.5 (chapter-part2.md) [for-slide-s23]"
visual_brief: "Bar chart on a log scale, Ocean rounded box: GPT-3.5 (2022) 4K → Claude 3.5 (2024) 200K → frontier standard up to 1M — Fable 5, GPT-5.6, Gemini 3.1 Pro and others (gold). Separately — a single outlier, Gemini 3.5 Pro at 2M (not the standard, one model). On the right, two contrasting bars: Llama 4 Scout '10M — advertised, no quality benchmarks, marketing' (hatched, muted) and YandexGPT 5 Pro 32K (low-end contrast). Bottom line about positional encoding. Gold callout about 'you pay for what you put in the window.'"
verify_day_of: true
---

# Visible content

## Title bar
"The 2026 frontier standard is a window of up to 1 million tokens. But advertised ≠ usable"

## Body
[Bar chart, log scale, Ocean rounded box]

| Model | Window |
|---|---|
| GPT-3.5 (2022) | 4K |
| Claude 3.5 (2024) | 200K |
| **Fable 5 · GPT-5.6 · Gemini 3.1 Pro (2026)** | **up to 1M — frontier standard** *(gold)* |
| Gemini 3.5 Pro (2026) | 2M — a single outlier model, not the standard |

[Two contrasting outliers, separate tiles]
- **Llama 4 Scout: "10M"** — advertised, marketing; no published benchmark confirms quality anywhere near the limit
- **YandexGPT 5 Pro: 32K** — one to two orders of magnitude below the frontier standard

[Small line]
*You can't just "stretch" the window: token position is encoded in a geometry trained on specific lengths — extending it (RoPE / YaRN) is separate engineering work.*

[Gold callout]
**You pay for what you put in the window, not for what the window can hold: 900K input tokens at $10/million ≈ $9 for a single call.**

[Action line]
**What to do:** choose a model by the task's effective window (verified on benchmarks without lexical shortcuts), not by the marketing maximum — "10M" without a quality confirmation doesn't count.

## Speaker notes

The context window — the maximum number of tokens per request — has grown three orders of magnitude in four years: 4,000 for GPT-3.5 at the launch of ChatGPT, 200,000 for Claude 3.5 in 2024, and the 2026 frontier standard — up to one million: Fable 5, GPT-5.6, Gemini 3.1 Pro and others hold this level, and for some of these models the full window is included in the standard price with no length surcharge. Two million for Gemini 3.5 Pro is not the standard but an outlier — for now the only model at this level, not a typical flagship; there are already more than a dozen models on the market with windows up to a million.

Two sobering outliers around the standard. On the high side — marketing: Llama 4 Scout advertises ten million tokens, but no published benchmark confirms that quality holds up anywhere near that limit; "advertised window" and "usable window" are different quantities, and we'll measure the gap between them a couple of slides from now. On the low side — a contrast: YandexGPT 5 Pro works with a 32,000-token window — for tasks with long documents, that's not a nuance, it's a defining constraint on model choice.

Why is the window finite, and why can't you "just increase it"? The first reason is familiar: the quadratic cost of attention plus a linearly growing cache. The second is subtler: token position is encoded in the model's geometry in a way trained on specific lengths, and naively stretching it breaks the mechanism; extension methods — RoPE, YaRN — are covered in the coursebook for self-study: the chapter, part 2 — the section on positional encoding.

And the money arithmetic that's worth doing once. The full window is tokens you pay for as input on every request: a call to a premium model at $10 per million input tokens, filled to 900,000, costs around $9 — for a single call; ten turns of dialogue run close to a hundred dollars without caching. The question "how much context does this task need" matters more economically than the question "how much can the model accept."

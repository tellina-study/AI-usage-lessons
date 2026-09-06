---
id: s29
type: summary
section: "Section 4. Sampling and Generation"
duration_min: 2.5
assertion: "Alongside the classic 'randomness + length' knobs, a new axis has appeared: 'reasoning depth + verbosity'"
learning_goal: "Table format 'parameter — range — what it affects — typical value' for all 5 key knobs; a lesson on API evolution using budget_tokens as the example"
learning_outcomes: [LO4]
chapter_ref: "§4.4 (chapter-part2.md) [for-slide-s29]"
visual_brief: "Main parameter table in an Ocean rounded box, format 'parameter — range — what it affects — typical value': temperature (0–2, determinism↔chaos), top_p (0.1–1, tail width), max_tokens (hard cutoff), effort/reasoning_effort (none→xhigh, thinking depth/cost), verbosity (low→high, answer length). The line 'memorize the axes' has been fully removed. (budget_tokens / 400 error — speaker notes only.)"
verify_day_of: true
---

# Visible content

## Title bar
"API knobs: reasoning depth has joined randomness and length"

## Body
[Parameter table, Ocean rounded box]

| Parameter | Range | What it affects | Typical value |
|---|---|---|---|
| `temperature` | 0–2 | Determinism ↔ chaos of token choice | 0 for classification, 0.7–1.2 for text |
| `top_p` | 0.1–1 | Width of the candidate tail during sampling | 0.9–0.95 |
| `max_tokens` | integer | Hard cutoff on generation — can stop mid-way | set per task, with headroom for JSON/code |
| `effort` / `reasoning_effort` | `none` → `xhigh` | Depth of internal reasoning — and its cost | `medium` by default for most providers |
| `verbosity` | `low` → `high` | Length of the visible answer, independent of thinking depth | `medium` |

[Action line]
**What to do:** start tuning with temperature and effort — these are the two main knobs; top_p/top_k/verbosity are fine-tuning on top.

## Speaker notes

The classic set — temperature, top_p, max_tokens — you already know; the parameter table on the slide pins down the range and typical value for each: zero for classification, 0.2–0.3 for code, around 0.7 for explanations, 0.9–1.2 for creative text.

The 2026 news is that reasoning models have grown two new knobs, and they control a different axis. Effort, or reasoning_effort, is the depth of internal reasoning: OpenAI has a scale from "none" to "xhigh," Anthropic has an effort parameter under adaptive thinking, Gemini has a thinking budget, where zero turns reasoning off and minus one hands the choice to the model. Verbosity is the length of the visible answer, independent of reasoning depth: you can ask the model to think deeply but answer briefly. The old pair "temperature controls randomness, max_tokens controls length" has been joined by the pair "effort controls thinking, verbosity controls wordiness."

A live example of API evolution — useful as an inoculation against memorizing parameters: in 2026, Anthropic broke backward compatibility for controlling thinking — the manual budget_tokens parameter now returns a 400 error on new models; in its place is adaptive thinking, where the model decides the depth itself. A detail at the intersection with caching: changing the thinking configuration between requests invalidates the prompt cache — it's part of the cacheable prefix.

And a related consequence: don't carry habits between providers and generations. Knobs with identical names behave differently, and recommendations flip sign: OpenAI explicitly recommends against giving reasoning models prompts in the style of "let's think step by step" — the model already reasons on its own, and manually padding out the chain just duplicates work and cost. A technique that was best practice for years has become an anti-pattern. When you switch models, read the parameters page as carefully as you'd read a library's breaking-changes list for a major upgrade.

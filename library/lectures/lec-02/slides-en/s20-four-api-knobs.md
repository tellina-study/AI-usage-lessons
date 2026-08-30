---
id: s20
type: summary
section: "Section 4. Sampling"
duration_min: 2
assertion: "4 parameters for the task: temperature, top_p, max_tokens, system prompt"
learning_goal: "LO4 teaching slide — 4 API knobs for 4 scenarios"
learning_outcomes: [LO4]
chapter_ref: "§4.3 [for-slide-s20]"
visual_brief: "A 5-column × 5-row table: header (Scenario | T | top_p | max_tokens | system_prompt) + 4 scenarios. Cells color-coded by T (gold for T=0 to teal for T=1.2). Subtitle: 'Pick parameters for the scenario deliberately'."
---

# Visible content

## Title bar
"4 API knobs for the task"

## Body
[A 5×5 table, Ocean rounded box]

| Scenario | `temperature` | `top_p` | `max_tokens` | system_prompt |
|---|---|---|---|---|
| Classification / exact extraction | **0** *(gold)* | — | 50–200 | Minimal, with an output schema |
| Code generation | 0.2–0.3 | 0.9 | 1000+ | Role + repository context |
| Chat explanation to the user | 0.7 | 0.9 | 500–1000 | Role + audience description |
| Creative writing | 0.9–1.2 *(teal)* | 0.95 | 2000+ | Role + style description |

[Footnote in small print, at the bottom]
`T = 0` makes the choice nearly deterministic; in production micro-variability from batching is possible — for most tasks it is negligible.

## Speaker notes

Let's collect the four main parameters an engineer uses to control an LLM through the API. These four parameters — `temperature`, `top_p`, `max_tokens`, and the **system prompt** — are the key practical goal of this section: after this slide you should be able to pick them for a specific scenario, not by guessing but with justification.

A brief definition of each. **Temperature** — the sharpness of sampling, from 0 to about 2. **Top_p** — the nucleus-cutoff parameter (typical values 0.9-0.95). **Max_tokens** — the maximum length of the model's answer in tokens (not words); if the answer hits the limit, it is cut off mid-word. **The system prompt** — a separate message that sets the model's role and constraints before the user request.

A summary table for four typical scenarios. The logic is consistent. **Classification.** When the task is to assign a document one of a finite set of labels, any stochasticity is harmful: if on the same document the model says "complaint" in one run and "question" in another, reproducibility is broken. T = 0 provides a deterministic argmax. Max_tokens is small — the answer is short. The system prompt is minimal but with an output schema: "answer in JSON format `{label: ..., confidence: ...}`", so post-processing can easily parse the result.

**Code generation.** Here you need a slightly non-zero temperature. T = 0 gives repetitive, sometimes overly "textbook" code; T = 0.2-0.3 leaves variability only in the choice between nearly equally good solutions. Top_p = 0.9 cuts off rare tokens, which in code almost always mean a syntax error. Max_tokens is large. The system prompt — role and repository context.

**Chat explanation.** The standard mode. T = 0.7 gives a variety of phrasings while preserving meaning; top_p = 0.9 keeps the natural options. The system prompt describes the role and the audience.

**Creative writing.** Stochasticity is a desired property. T = 0.9-1.2 gives unexpected turns of phrase and metaphors. Top_p = 0.95 loosens the tail cutoff. The system prompt — role and style.

This table is not a prescription; it is a reference. In real work you'll calibrate the values for your task. The important thing is to understand the frame: four knobs, and they're turned together — there's no point setting T = 0 and top_p = 0.5 (top_p at T = 0 is meaningless); no point setting T = 1.5 and max_tokens = 50 (the model will just get going and get cut off).

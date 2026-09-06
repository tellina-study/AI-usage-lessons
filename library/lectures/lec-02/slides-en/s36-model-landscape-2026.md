---
id: s36
type: summary
section: "Section 5. Model types and sizes"
duration_min: 3
assertion: "The September 2026 landscape: frontier and open weights have converged in quality — and diverged in price by three orders of magnitude"
learning_goal: "A map of models as of September 2026: frontier vs open weights, strength (IMO), price spread, speed of obsolescence"
learning_outcomes: [LO6]
chapter_ref: "§5.2 (chapter-part3.md) [for-slide-s36]"
visual_brief: "Two column camps in Ocean rounded boxes: 'Frontier (closed)' — GPT-5.6 (Luna/Terra/Sol), Claude Fable 5 / Opus 5, Gemini 3.5 Pro, Grok 4.3; 'Open weights' — DeepSeek V4, Qwen 3.8-Max, Kimi K2.6 / K3 (2.8T — largest open model). v3.1 (#183 round 3): before each row (except Kimi) — a real company logo (LobeHub icons-static-svg, recolored into the Ocean palette) as a visual anchor. Below the columns — an IMO 2026 exhibit strip: '6 models — 42/42 vs 7 of 666 humans' (gold). At the bottom, a price scale gradient: floor $0.03–0.2/M … premium $10/$50/M, with a highlighted pair 'Kimi K2.6 ≈ GPT-5.5 on SWE-bench Pro at −80% of the price' (gold)."
verify_day_of: true
---

# Visible content

## Title bar
"September 2026: quality has converged — prices have diverged by three orders of magnitude"

## Body
[2 column camps, Ocean rounded boxes]

**Frontier (closed weights)**
- OpenAI: GPT-5.6 — Luna → Terra → Sol
- Anthropic: Claude Fable 5 · Opus 5
- Google: Gemini 3.5 Pro (2M window, Deep Think)
- xAI: Grok 4.3

**Open weights**
- DeepSeek V4 (Pro 1.6T / Flash 284B)
- Qwen 3.8-Max — the first open model in the Max lineup
- Kimi K2.6 (1T) · **Kimi K3 (2.8T — the largest open model)**

[Exhibit strip]
**IMO 2026: six models — a perfect 42/42. Out of 666 human contestants — seven.** *(gold)*
The same systems miscount the letters in the word cranberry — "jagged intelligence" as a working characteristic.

[Price scale]
Market floor **$0.03–0.2 / M tokens** ←—————→ premium **$10 in / $50 out**
**Kimi K2.6 ≈ GPT-5.5 on the guarded SWE-bench Pro — at ~80% less** *(gold)*

[Action line]
**What to do:** revisit your model choice regularly — the landscape shifts on a scale of months, not years (GPT-5.2: release → retired from ChatGPT within half a year).

## Speaker notes

Let's fix the map of the terrain — as of September 2026; specific models and prices are the most perishable part of this lecture. The closed-weights frontier: OpenAI has the three-tier GPT-5.6 family — Luna, Terra, Sol; Anthropic has Claude Fable 5 with a million-token window at no markup and Opus 5 one tier down; Google has Gemini 3.5 Pro with a two-million window and Deep Think mode; xAI has Grok 4.3. Open weights: DeepSeek V4 in two variants, Qwen 3.8-Max — the first model in the Max line with published weights, and the Kimi pair — K2.6 at one trillion parameters and K3 at two-point-eight trillion, the largest open model in history. Remember the category from the previous slide: open giants are not local.

How strong they are. The signature result of the year: at the International Mathematical Olympiad, six models scored a perfect 42 out of 42 — while among 666 human contestants, only seven achieved a perfect score. For the first time, machines aced the olympiad — and these are the same systems that miscount the letters in the word cranberry: "jagged intelligence" isn't a metaphor, it's a working characteristic.

How much they cost: the spread is three orders of magnitude. The market floor starts at three cents per million input tokens; the premium tier is ten dollars in, fifty out. The most telling pair of the year: Kimi K2.6 matches GPT-5.5 on the leak-resistant SWE-bench Pro — at a price roughly 80% lower; we'll draw the conclusion from this pair at the end of the lecture — on the final slide about choosing a tool.

And the speed of obsolescence: GPT-5.2 went from release to full retirement from ChatGPT in half a year. Design for model churn as the norm: version your configs, version your prompts, treat your own eval set as a regression test. And remember: announcements are not releases — plan around models available today.

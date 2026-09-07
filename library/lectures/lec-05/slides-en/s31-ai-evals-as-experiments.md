---
id: s31
type: process
section: "Section 4. Measure / Experiment"
duration_min: 2.5
assertion: "Evals are \"unit tests for the agent\": pass@k trends toward 100%, pass^k collapses toward 0% at the same base probability"
learning_goal: "AI: evals as experiments for the agent — Hussain's 3-layer framework, pass@k vs pass^k, LLM-as-judge"
learning_outcomes: [LO1, LO2]
chapter_ref: "§4.3 [for-slide-s31]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  process: a 3-level ladder (Level 1 unit tests → Level 2 human/LLM judge → Level 3 A/B), the
  last rung labeled "only once the product is mature." Next to it — a diverging two-line
  chart: pass@k trends toward the top, pass^k collapses toward the bottom — visualizing the
  divergence at the same base probability.
source: "Hamel Husain framework; Anthropic 'Demystifying evals for AI agents' (9 Jan 2026)"
---

# Visible content

## Title bar
pass@k trends toward 100%, pass^k toward 0%: the same probability, a different question

## Body
[3-step eval ladder + diverging pass@k/pass^k chart]

**3 levels (Husain)**
1. Unit tests (fast, deterministic)
2. Human + LLM-as-judge
3. A/B — only once the product is mature

[Ocean rounded box]
pass@k = at least 1 success out of k · pass^k = **all** k successful — production reliability almost always requires pass^k

## Speaker notes

Kevin Weil, OpenAI's Chief Product Officer, states the key shift: writing evals will become a core skill for product managers. An eval is a "quiz for the model": a way to set the specific accuracy bar the product needs. Hamel Husain proposes a clean three-level framework: level one — unit tests, fast and deterministic; level two — human and model-based judging; level three — A/B testing, only once the product is mature enough. A/B isn't replaced by evals — it's the last rung of the ladder, not a discarded classical tool.

Why probabilistic output breaks pass/fail — a clear explanation for an audience starting from zero. Pass at k is the probability the agent produces at least one correct result in k attempts; pass hat k is the probability the agent succeeds on all k attempts. These two numbers can diverge dramatically at the same base probability: as k grows, pass at k trends toward one hundred percent, while pass hat k collapses toward zero. A vendor reporting "our agent succeeds ninety-five percent of the time" is answering different questions depending on which one is meant — and production reliability almost always requires pass hat k.

LLM-as-judge reaches about eighty-five percent agreement with humans on easy categories — but agreement can fall below sixty percent on hard categories, especially safety — the judge is least reliable exactly where the stakes are highest. Offline and online eval are layers, not alternatives: offline catches known regressions, online surfaces the long tail of inputs. Notion increased its fix throughput from three to thirty fixes a day after adopting systematic evaluation. An eval is a living artifact: if scores hit a ceiling, it has "saturated" and needs harder cases.

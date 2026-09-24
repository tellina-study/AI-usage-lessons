---
id: s-ft-eval
type: comparison_table
section: "Section 3. Fine-tuning"
duration_min: 2.5
assertion: "Evaluating a fine-tune is more expensive than training it and unsolved: none of the SIX methods is self-sufficient (MMLU ~29%, GSM8K→GSM1k −13 pp, judge position bias 75%, human κ≥0.6 $300–1200, BLEU r≈0.25–0.52); the lab→prod gap ~37% — a benchmark gain is a hypothesis, not a result"
learning_goal: "How each of the six evaluation methods works: how it works · when it's valid · when it breaks · cost (§3.7)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§3.7 [for-slide-ft-eval-benchmarks, ft-eval-heldout, ft-eval-judge, ft-eval-human, ft-eval-task, ft-eval-ab, ft-eval-gap]"
subtype: comparison_table
new_in_v4: "#196 WAVE 3 — training evaluation (failure/limitation)"
changed_in_v6d2: "#196 WAVE D2 owner #12 — DROP LeftExit meme; 5 methods → 6 (formally, schema how-it-works·when-valid·when-breaks·cost)"
---

# Visible content

## Title bar
«Evaluating a fine-tune costs more than training it — six methods, none self-sufficient»

## Body
[Table of six methods by scheme: method · how it works · when it breaks (number) · cost]

1. Public benchmark — accuracy on fixed Q&A; breaks on contamination (MMLU ~29%, GSM8K→GSM1k −13 pp); cost low, but deceptively so.
2. Held-out test set (gold) — frozen BEFORE training; breaks on leakage; highest ROI, ≈0 to re-run.
3. LLM-as-judge — >80% agreement with humans, BUT position bias up to 75%, self-preference +10–25%; cents + bias control.
4. Human evaluation — rubric + κ≥0.6; expensive, doesn't scale; $300–1200 per round.
5. Task metrics (BLEU/ROUGE) — n-grams; on open generation r≈0.25–0.52; near-zero.
6. A/B / online — canary + guardrails; ×4 samples due to non-determinism; engineering + risk.

[Gold] The lab→prod gap ~37% — a benchmark gain is a hypothesis, not a result.

## Speaker notes

Here the intuition flips: engineers worry about the cost of training, but the real budget line is evaluation. A useful 7B LoRA costs a few dollars, while a rigorous evaluation of that same adapter is $300–1200 of human labor for a single round — and it can still fail to predict production. Let's go through six methods, each on the same hard scheme: how it works step by step, when it's valid, when it breaks, what it costs.

First — public benchmarks: MMLU, GSM8K, HELM. A fixed set of questions with known answers, the metric is the share answered correctly, the run is cheap and needs no people. Valid for checking broad capabilities and catching forgetting. It breaks on two things. Contamination: test questions leaked into pretraining — about 29% of MMLU items showed signs of contamination[1], and on a clean mirror of GSM8K, that is GSM1k, accuracy drops by thirteen points[2], which means you're measuring memory, not reasoning. And irrelevance: a domain-specific LoRA can be better on your domain and worse on MMLU. Second — the held-out test set: you select and label examples from your own task before training, freeze them, and run every version against them. This is the only thing that measures your actual task — the highest ROI; it breaks only on leakage into training or drift. Third — LLM-as-judge: a strong model judges the output, pairwise is more reliable than pointwise. It gives over 80% agreement with humans, but it's systematically biased: position bias up to 75% preference for the first answer, self-enhancement adding 10–25% in favor of its own model family. The key point here: reproducibility of a verdict is not the same as its correctness.

Fourth — human evaluation: a rubric, two to three annotators, inter-rater agreement (kappa). There's a meaningful threshold — kappa no lower than 0.6, otherwise the rubric needs to be rewritten. The gold standard for open-ended quality, but expensive and doesn't scale: a set of 200 examples across three raters is $300–1200 per round. Fifth — task metrics: exact-match, F1, BLEU, ROUGE. Valid for closed tasks with a single correct answer. On open generation they break: they measure n-gram overlap, not meaning, correlation with humans is r from 0.25 to 0.52 — a correct paraphrase gets penalized. Sixth — A/B online: a canary on 1–5% of traffic with guardrail metrics. The only method that measures real behavior; it breaks because it's not applicable before production, and because of LLM non-determinism you need roughly four times more samples.

The through-line: no single method is self-sufficient. The cheap ones have the worst validity, the valid ones are expensive. The measured gap between a lab benchmark and production is about 37% — that's mechanics, not an anomaly: a benchmark gain is a hypothesis, not a result; only a clean held-out set plus A/B on real traffic confirm it, and you need to budget for that gap.

Sources:
[1] Pebblous — LLM Benchmark Contamination (MMLU ~29%) — about 29% of MMLU items show signs of contamination — a benchmark number without a leakage check is theater. https://blog.pebblous.ai/blog/llm-benchmark-contamination/en/ [VFY-day-of]
[2] Zhang et al. 2024 — GSM1k (clean mirror of GSM8K −13 pp) — a clean mirror drops accuracy by up to 13 points — trust the delta on the clean mirror. https://arxiv.org/abs/2405.00332 [VFY-day-of]

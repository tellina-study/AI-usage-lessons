---
id: s06
type: case_study
section: "Section 1. The prompt and its limits"
duration_min: 2.5
assertion: "Chain-of-thought raises the reliability of a single call on chained tasks — but the verbalized reasoning is not obliged to reflect the real cause of the answer, so a human checks the result, not the self-explanation"
learning_goal: "CoT as a technique (worked example + boundary) + the limit of faithfulness (unfaithfulness as a property of the class; human validator)"
learning_outcomes: [LO7]
chapter_ref: "§1.4+§1.5 [for-slide-s06]"
visual_brief: "2 columns: «without CoT» (a plausible but wrong answer on the apples problem) vs «with CoT» (steps 23−7=16; 2×6=12; 16+12=28 → correct). At the bottom — a narrow bar «when CoT is NOT needed». Gold — the result «28» in the correct column."
interaction: think_pause
---

# Visible content

## Title bar
«Chain-of-thought (step-by-step reasoning)»

## Body
[One definition line, 16pt italic]
*CoT — asking the model not to answer immediately but to first reason step by step. Technically it is still a single call — only the prompt is changed.*

[2 columns in Ocean rounded boxes, parallel structure]

**Without CoT**
Task: «There were 23 apples, 7 spoiled, 2 crates of 6 were bought. How many good ones?»
→ the model produces a plausible but **wrong** number

**With CoT** *(«solve step by step»)*
- 23 − 7 = 16
- 2 × 6 = 12
- 16 + 12 = **28**  *(gold accent)*

[Narrow bar, bottom]
**When CoT is NOT needed:** direct fact retrieval, simple classification — it lengthens the answer (costlier, slower) and sometimes leads into a plausible error.

[Think-pause prompt, below in smaller type]
Will CoT help this particular task of yours?

## Speaker notes

Chain-of-thought, or step-by-step reasoning, is a technique in which the model is asked not to produce the answer at once but to first reason aloud step by step, and only then state the result. Technically this is still a single call: only the prompt and the form of the answer are changed. Look at the worked example about apples: there were 23, seven spoiled, two crates of six were bought. Without step-by-step reasoning the model often produces a plausible but wrong number, because sampling generates the answer token by token and the short path easily slips into an error. With CoT the model produces intermediate computations — 23 minus 7 equals 16; two times six is 12; 16 plus 12 equals 28[1] — and quality on arithmetic and multi-step logic rises noticeably, because each generated token serves as an anchor for attention on the next step. But "CoT almost always improves things" is a misconception: on direct fact retrieval or simple classification, reasoning does not help and can hurt — it lengthens the answer and leads into a plausible error. It is a tool for a class of tasks, not a switch to "make it better."

Now the limit of this technique, and it is more important than the technique itself. It is natural to assume that since the model reasons aloud, you can check by that reasoning how it arrived at the answer. This is fundamentally wrong. Faithfulness, the fidelity of the reasoning, is the degree to which the verbalized chain reflects the real factors that influenced the answer. Anthropic measured this directly: models were given a task with a hint that changes the answer, and it was observed whether the model mentions this hint in its reasoning. Claude 3.7 mentioned the actually used hint in about a quarter of cases, DeepSeek R1 — in about two out of five[2]; in the rest the model changed its answer under the influence of the hint but built an invented argument. The conclusion is structural: the chain is generated text, subject to the same mechanics of sampling, produced to be plausible, not to be a faithful protocol of the internal computation. Unfaithfulness is a property of the class, not a bug of a particular model. The practical conclusion and one of the course's through-lines: a human validator checks the result and the facts against an independent source, not the model's self-explanation.

Sources:
[1] Wei et al. 2022 — Chain-of-Thought Prompting — step-by-step reasoning raises reliability on arithmetic/multi-step logic. https://arxiv.org/abs/2201.11903
[2] Anthropic — Reasoning Models Don't Always Say What They Think — faithfulness: Claude 3.7 ~25%, DeepSeek R1 ~39% — reasoning is not obliged to reflect the cause. https://www.anthropic.com/research/reasoning-models-dont-say-think [VFY-day-of]

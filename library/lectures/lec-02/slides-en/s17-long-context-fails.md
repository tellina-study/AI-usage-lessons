---
id: s17
type: case_study
section: "Section 3. Attention mechanism"
duration_min: 2
assertion: "A large context window != good use of the context"
learning_goal: "Lost-in-the-middle effect + engineering takeaway (placement of what matters)"
learning_outcomes: [LO6]
chapter_ref: "§3.4 [for-slide-s17]"
visual_brief: "A U-shape curve: accuracy (Y, 0-100%) vs the fact's position in a 100k context (X, start→middle→end). ~75% start (gold), dip to ~50% middle, ~75% end (gold). Liu et al. 2023."
---

# Visible content

## Title bar
"A large window != good use"

## Body
[Main visual: a U-shape "accuracy vs position" curve, Ocean rounded box]

**Experiment:** a factoid is inserted at the start / middle / end of a 100k context; the model is asked about the fact.

[Plot]
- X-axis: the fact's position in the context (start → middle → end)
- Y-axis: the model's answer accuracy (0-100%)
- Curve: ~75% at the start → a dip to ~50% in the middle → ~75% at the end
- The strong endpoints are highlighted gold

[Caption under the plot]
Liu et al. (2023). *Lost in the Middle: How Language Models Use Long Contexts.* arXiv:2307.03172.

[Gold callout, bottom]
**Engineering takeaway:** put what matters at the start or the end of the prompt — not in the middle.

## Speaker notes

In 2023 a group from Stanford and UC Berkeley published a paper with a provocative title: "Lost in the Middle: How Language Models Use Long Contexts". The empirical question: if a model can take 100 thousand tokens as input, does it use different positions in that window equally well?

The experiment. Into a large context — tens of thousands of tokens from arbitrary documents — a single significant fact is inserted: at the start, in the middle, or at the end. Then the model is asked about the fact and the answer accuracy is measured. The results give a characteristic U-shaped curve: accuracy around 70-80% when the fact lies at the start, sagging to ~50% in the middle, and rising again to 70-80% toward the end. The authors called the phenomenon "lost in the middle".

The nature of the effect lies in how models learn to work with long context. In the training corpus, typical documents are arranged so that important statements are either at the start (the thesis) or at the end (the conclusion); the statistics of the position of important tokens have a U-shape. The model absorbs this statistic and carries it over to inference: even if an important token lies in the middle, the model "out of habit" weights it less in attention. This is not a bug — it is an inductive bias of training, a reflection of how real texts are structured.

The engineering takeaway. If you have a long prompt with instructions or data — put the most important part at the start or the end, not in the middle. A common mistake is a long preamble with a critical constraint buried in the middle; the model will systematically ignore such an instruction. The fix: rewrite the prompt so that critical instructions stand at the very start (system prompt) or are explicitly repeated at the end, right before the task. This also explains why "just stuff all the documentation into a large window" is a poor strategy for RAG. Good retrieval that returns 5-10 targeted fragments at the start of the prompt systematically works better than loading the whole base into a giant window. We'll return to this in Lecture 3.

Sources:
[1] Liu et al. (2023) — Lost in the Middle — U-shape: accuracy dips in the middle of the window; put what matters at the start/end of the prompt. https://arxiv.org/abs/2307.03172

---
id: s17
type: assertion_visual
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 2.5
assertion: "Fine-tuning has narrowed to behavior: knowledge→RAG, behavior→PEFT, deterministic→code; hybrid is the norm"
learning_goal: "Criteria for \"what goes where\" + hybrid as the 2026 norm, but only under a double requirement"
learning_outcomes: [LO7]
chapter_ref: "§3.3+§3.5 [for-slide-s17]"
interaction: none
---

# Visible content

## Title bar
"Criteria: what goes where"

## Body
[Table "if the task requires… → tool"]

| If the task requires… | …tool | …and NOT, because |
|---|---|---|
| knowledge changes / provenance needed | **RAG** (or context) | not FT: goes stale, expensive, forgetting |
| stable behavior / tone / format | **fine-tuning (PEFT)** | not RAG: does not change the manner |
| lower cost on a narrow task | **FT teacher + distillation of a student** | not "distillation as a kind of FT" — 2 different techniques |
| deterministic answer | **ordinary code** | neither RAG nor FT: non-determinism with no gain |

[Gold callout, bottom]
**The 2026 question is not "RAG or fine-tuning" but "what here is knowledge (→RAG), what is behavior (→PEFT)."** Hybrid is the norm, but only where a task has BOTH requirements at once; each component is added for its own requirement.

## Speaker notes

Let us break down the question that is constantly confused in practice: not "RAG or fine-tuning" but "what here is knowledge and what is behavior." If the task requires knowledge that changes or needs freshness and provenance, the right tool is RAG or a long context, not fine-tuning: knowledge in the weights will go stale by the next change of the corpus, retraining is expensive, and there is a risk of catastrophic forgetting. If the task requires stable behavior, tone, output format, or following a policy rather than new facts, the right tool is fine-tuning in the form of PEFT, not RAG: RAG feeds knowledge into the context but does not change the model's manner of answering. If the goal is to lower cost and latency on a narrow task while keeping quality, a pairing of two separate techniques works: first you fine-tune a large teacher model for the required behavior, and then you distill from it a compact student model. This is not "distillation as a variety of fine-tuning" — taxonomically these are different operations that in practice often go together. And if the answer must be deterministic and verifiable, the right tool is ordinary code with no AI at all: neither RAG nor fine-tuning is needed here, they would add only non-determinism.

The 2026 takeaway removes the false dichotomy: a clean "one of them" choice is rare, the norm is a hybrid. A typical mature system combines RAG for knowledge that changes, PEFT fine-tuning for stable behavior, and context engineering on top of both. But a caveat matters here, so that "hybrid is the norm" does not turn into a new cargo cult of "do everything at once": a hybrid is justified only where a task simultaneously has both a knowledge problem and a behavior problem. If there is no behavior problem, fine-tuning is not needed, even if RAG is already there. If the knowledge does not change and there is little of it, RAG is not needed either. A hybrid is not "more components — more correct," it is "knowledge and behavior separated into the right mechanisms, each added for its own requirement" rather than out of inertia or fashion.

---
id: s-classic-ft
type: assertion_visual
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 2
assertion: "Classical ML: training set, ground-truth labels, train/validation/test split, transfer learning; PEFT/LoRA is the same transfer learning, cheap, on top of a pretrained model"
learning_goal: "Classical baseline §3.0: classical ML as the foundation of fine-tuning"
learning_outcomes: [LO7, LO4]
chapter_ref: "§3.0 [for-slide-s-classic-ft]"
visual_brief: "Three classical-ML cards (training set + ground truth; train/val/test split; transfer learning) + gold callout \"what to keep: golden set, versions, discipline\" + a bridge to PEFT/LoRA."
interaction: none
new_in_v5b: "#185 WP8 — classical baseline of Section 3"
---

# Visible content

## Title bar
"How an ML task was solved before large models"

## Body
[Three classical-ML cards, Ocean rounded box]

**Training set + ground-truth labels** — a labeled set of "input → correct answer" (ground truth); the model learns to reproduce it and to generalize to new data.

**Train / validation / test split** — three non-overlapping parts: train to learn, validation to tune, test to measure quality once. The rule: you may not test on the training data.

**Transfer learning** — take a model pretrained on a large corpus and cheaply fine-tune it for your narrow task: faster and more accurate than from scratch. The "pretraining → fine-tuning" scheme.

[Gold callout — what to keep from the classics]
**What to keep: eval sets (golden set) — without them catastrophic forgetting is invisible; versioning of data and weights for rollback; train/test discipline against leakage; drift monitoring in operation. LoRA made the fine-tuning step cheaper, but not the discipline around it.**

[Bridge, bottom]
PEFT/LoRA is the same transfer learning, taken to the limit of cheapness and on top of an incomparably larger model. The idea is not new — what became new is the scale of the base model and the cost of the step.

## Speaker notes

Classical machine learning solves the task like this. Training a model for a task in the pre-LLM paradigm is building your own model on your own data: the engineer collects a labeled set of "input → correct answer" examples and tunes the parameters so the model reproduces these answers and then generalizes to new ones. The central term is the training set: the collection of labeled examples on which the model learns. The labels are called ground-truth labels, ground truth — the known correct answer against which the prediction is compared. Before the era of large models, solving an AI task almost always meant collecting your own dataset, choosing an architecture for the task, and training your own narrow, controlled model.

The second load-bearing structure is the discipline of splitting the data. It is divided into three non-overlapping parts: training, validation, and test. On the training part the model learns, on the validation part hyperparameters are tuned, and on the test part — only once, at the end — the true quality is measured on data the model has not seen. The iron rule: you may not test on the training data, otherwise the accuracy comes out inflated and collapses in production. Quality is measured by an explicit metric fixed before training.

The third classical idea, and it is exactly the one that leads to this section's theme, is transfer learning. Long before large models, engineers noticed: training from scratch is expensive, but if you take a model pretrained on a huge general corpus and fine-tune it on your small task, the result comes out faster and more accurate. This is the classical two-phase pretraining–fine-tuning scheme.

This is exactly what the transition to fine-tuning large models should rest on. PEFT and LoRA are the same transfer learning, only taken to the limit of cheapness and on top of an incomparably larger model. The idea is not new — what became new is the scale of the base model and the cost of the fine-tuning step. So fine-tuning a large model is not an exotic thing of a new era but a direct continuation of the classical scheme, and all its cautions (train/test discipline, a metric, versions, drift monitoring) remain in force.

---
id: s25
type: assertion_visual
duration_min: 2.5
assertion: "Bias, sycophancy, distribution shift — three manifestations of one nature"
learning_goal: "A coherent trio + GPT-4o sycophancy rollback"
learning_outcomes: [LO6]
references: [openai-2025-sycophancy-postmortem, pan-2022-reward-misspecification]
visual:
  pattern: three_concepts_with_anchor
  primary: "3 cards (Bias / Sycophancy / Distribution shift) + GPT-4o timeline + shared cause"
retrieval_moment: "s25+ mini-poll \"which is more dangerous in your field\""
---

# Bias, sycophancy, distribution shift — three manifestations of one nature

## Assertion

Bias, sycophancy, distribution shift — three manifestations of one nature.

## Visual

At the top, three Ocean rounded box cards with icons: "Bias" (scale-balance), "Sycophancy" (smile), "Distribution shift" (trending-down). Each has one definition and one example, in English. At the bottom, a gold timeline "GPT-4o: sycophancy — April 2025": "April 25 — release of the update → April 28 — start of the rollback (Altman on social media that same evening) → April 29 — post-mortem of the causes". Under the timeline, a gold callout: "Shared cause: AI reflects the data it was trained on".

## Speaker notes

Three problems united by a shared nature: a model is a reflection of the data it was trained on, not an independent source of truth. They manifest differently, but have a common cause, and it's useful to hold this in mind as one coherent phenomenon.

Bias. The model repeats the skews of the dataset. The canonical example: a résumé-screening model trained on the historical data of a company that historically hired fewer women for technical positions will discriminate against female candidates — not by "deciding" that they're worse, but by statistically predicting that "such profiles were usually rejected". Bias is the hardest category to correct, because the data often captures the structural inequalities of the real world.

Sycophancy. First, a definition of the key term. RLHF — Reinforcement Learning from Human Feedback — is a training technique in which a human ranks the model's responses by quality, and these rankings serve as a reward signal for additional fine-tuning. RLHF is the standard step in turning a foundation language model into a chat assistant. The flip side: human labelers on average rate pleasant answers higher. The model learns to agree with the user, to echo their phrasings, to say what they want to hear.

The canonical incident. On April 25, 2025, OpenAI shipped an update to GPT-4o that made the model obtrusively sycophantic: the model agreed with clearly incorrect statements, praised the user excessively, endorsed contentious claims. On April 28 the rollback of the update began — Altman on social media that same evening wrote that they'd already started the rollback. On April 29 the post-mortem of the causes was published. Sycophancy is the most inconspicuous category: a user, receiving compliments, easily fails to notice that the model has lost a critical attitude toward their words.

Distribution shift. A model trained on data from one period behaves poorly outside that distribution. A conceptual example: a model trained on 2023 code will, in 2026, confidently suggest an outdated library, an out-of-date practice, and fail to account for API changes. Distribution shift is the most frequent category in long-lived systems, and its peculiarity is that the model's quality degrades "quietly" over time without visible failures.

The coherent message. All three are manifestations of one nature: the model doesn't "know" the truth; it reproduces the regularities of the data it was trained on. Bias — regularities from historical data. Sycophancy — regularities from feedback labeling. Distribution shift — the absence of the regularities of the new period.

A short exercise: think for thirty seconds about which is more dangerous in your future professional field.

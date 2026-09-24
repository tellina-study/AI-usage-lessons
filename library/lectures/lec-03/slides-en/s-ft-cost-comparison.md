---
id: s-ft-cost
type: comparison_table
section: "Section 3. Fine-tuning"
duration_min: 2.5
assertion: "Training cost: order of magnitude and growth shape matter, not the exact figure. Values are relative (Full-FT = baseline ×1). LoRA is the default: trains ~0.1–1% of parameters, ~×0.01 the price/compute, ~7 orders of magnitude cheaper than pretraining"
learning_goal: "Relative training-cost axis by method: trainable parameters · VRAM · $ · compute · data · speed (Full-FT = baseline ×1) (§3.6)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§3.6 [for-slide-ft-cost-law, ft-cost-table, ft-cost-baselines, ft-cost-when]"
subtype: comparison_table
new_in_v4: "#196 WAVE 3 — training economics"
changed_in_v64: "#196 v6.4 owner-review — REVERT to axes×methods with relative parameters (Full-FT = baseline ×1)"
---

# Visible content

## Title bar
«Training cost: order of magnitude matters, not the exact figure»

## Body
[Convention note, italic]
*Values are relative: Full-FT is taken as baseline ×1 on VRAM / $ / compute, the rest are fractions of it. Absolute $ and hours keep moving; what matters is the order of magnitude and growth shape.*

[Table: rows = axes (trainable parameters / VRAM / $ per run / compute / data volume / iteration speed), columns = 5 methods (pretraining from scratch / Full-FT / LoRA / QLoRA / prompt+RAG)]

[Gold] LoRA is the default: trains ~0.1–1% of parameters, ~×0.01 the price / compute and ~×0.2 the VRAM of Full-FT — a 7B LoRA run costs <$10, ~7 orders of magnitude cheaper than frontier pretraining ($61–92M). Full-FT is justified only when the dataset exceeds LoRA's capacity. QLoRA is the same LoRA on top of a 4-bit base: 65B fits on a single 48 GB card.

## Speaker notes

Let's put together the training-cost axis so it's easier to keep in your head: not in absolute dollars, which keep moving, but in relative terms. We take Full-FT as the baseline and count it as a unit — ×1 on memory, on money, and on compute. Everything else is a fraction of that unit. So what matters isn't the exact price tag but the order of magnitude and the shape of the growth: in some places it's a thousand times more expensive, in others it's hundredths of that. That's exactly what the engineer needs to decide: which option to take.

Let's go through the rows of the table. Trainable parameters: pretraining from scratch trains all the weights, Full-FT also trains one hundred percent, LoRA and QLoRA train a tiny adapter of 0.1–1% of parameters, and prompt with RAG doesn't change the weights at all. From there this projects directly onto memory, money, and compute. On VRAM, Full-FT is the baseline ×1; LoRA is roughly ×0.2 of that, because you don't have to keep gradients and optimizer states for the whole model, only the frozen base weights plus the adapter; QLoRA is even lower, around ×0.05, because the base is compressed to four bits. On money and compute the contrast is even sharper: LoRA and QLoRA are on the order of ×0.01 of Full-FT, that is, a hundred times cheaper, while pretraining from scratch is the opposite — over a thousand times more expensive than the baseline. To tie this to real life: a useful LoRA fine-tune of a small model costs less than ten dollars[1], while pretraining a frontier model costs tens of millions. Hence the headline contrast: LoRA is cheaper than frontier pretraining by roughly seven orders of magnitude. The "pretraining from scratch" row is in the table only to set the scale — nobody in the room is pretraining.

Let's be honest about QLoRA: it isn't a separate competing method, it's a modifier on top of LoRA. It doesn't change what gets trained — the same LoRA adapters — it cuts the weight of the frozen base by roughly a factor of four via 4-bit quantization. That's why it has the same relative parameters as LoRA in the table, only memory is even lower: for example, a 65B model fits on a single 48-gigabyte card[2]. The picture for data volume and speed follows the same shape: pretraining needs trillions of tokens and months, Full-FT and LoRA get by on thousands to tens of thousands of examples, and prompt with RAG works on a few-shot set of just a handful of examples and can be fixed instantly. Conclusion: training is cheap and getting cheaper; Full-FT is justified only when the dataset exceeds LoRA's capacity, and for narrow behavioral adaptation it buys nothing over LoRA while adding memory and forgetting risk.

Sources:
[1] Thinking Machines — LoRA Without Regret (LoRA ≈ Full-FT under the right conditions) — LoRA is compared with Full-FT across all layers and outside capacity; ~0.13% of parameters, <$10. https://thinkingmachines.ai/blog/lora/ [VFY-day-of]
[2] Dettmers et al. 2023 — QLoRA (65B on a single 48 GB card) — 4-bit NF4 quantization of the frozen base → fine-tuning 65B on a single GPU. https://arxiv.org/abs/2305.14314

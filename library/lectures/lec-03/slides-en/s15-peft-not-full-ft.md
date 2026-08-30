---
id: s15
type: assertion_visual
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 2
assertion: "PEFT (LoRA/QLoRA) is almost always better than full fine-tuning: cheaper, more modular, and noticeably lowers the risk of catastrophic forgetting"
learning_goal: "PEFT instead of full-FT — 3 reasons, the third architectural (reliability)"
learning_outcomes: [LO7]
chapter_ref: "§3.2 [for-slide-s15]"
visual_brief: "Left — a diagram: a large frozen «base weights (frozen)» + small «LoRA adapters». Right — 3 reasons. DPO/RFT — 1 line «the spectrum of methods — in the chapter». Gold — reason #3 (architectural)."
interaction: none
---

# Visible content

## Title bar
«PEFT instead of full fine-tuning»

## Body
[Inline-define, 16pt italic]
*PEFT (parameter-efficient fine-tuning) — the base weights are frozen, only a small set of adapters is trained. LoRA — low-rank adapter matrices; QLoRA — the same on top of a quantized model.*

[Left — a diagram in an Ocean rounded box]
a large block **«base weights (frozen)»** + small pluggable **«LoRA adapters»**

[Right — 3 reasons]

**1. Cheaper and faster** — millions of parameters are trained instead of billions; QLoRA — on a single GPU

**2. Modularity** — adapters are megabytes vs gigabytes; one base — many specializations

**3. ↓ Risk of catastrophic forgetting** *(catastrophic forgetting — degradation of general abilities, s16)* — the base is frozen, physically not overwritten under the new signal *(gold accent — architectural argument)*

[Baseline bar, bottom]
**98.4% of models tagged PEFT on the Hugging Face Hub use LoRA** *(out of 20,834 cards; HF PEFT team, 2026)* — a caveat: this is the share among those already tagged PEFT, not among all fine-tuning.

[Sub-caption, bottom, 12pt italic]
*The full spectrum of behavior-tuning methods (SFT / DPO / RFT) — in the chapter. In the narrative: full FT — almost never; PEFT — the workhorse of 2026.*

## Speaker notes

The phrase "fine-tune a model" for many is associated with updating all the weights — this is full fine-tuning. In 2026 this is almost never what is needed. PEFT, parameter-efficient fine-tuning, is a family of methods in which the base weights are frozen and only a small set of additional parameters, adapters, is trained[1]. The most widespread method is LoRA: small low-rank adapter matrices are added into selected layers, and only they are trained. QLoRA is the same idea on top of a quantized base model, which radically lowers memory requirements.

Why PEFT is almost always preferable to full fine-tuning — three reasons, and the third is the most important. First: cheaper and faster — millions of adapter parameters are trained instead of billions of weights; QLoRA allows fine-tuning large models on a single GPU. Second: modularity — the adapters are small, megabytes against gigabytes, and you can keep several adapters for different tasks on one frozen base. Third, the main architectural argument about reliability: the base weights are frozen, physically not overwritten under the new signal, so what the model could do before fine-tuning is largely preserved — the training lives in the small additional adapters. This directly lowers the risk of catastrophic forgetting, to which we will now turn.

How widespread LoRA is — not an eyeball estimate but a measurable fact. According to the Hugging Face PEFT team, among 20,834 model cards tagged PEFT, 98.4 percent[3] use LoRA specifically. A caveat is mandatory: this is the share among those already tagged PEFT, not among all fine-tuning — full fine-tuning is tagged less carefully and may not be visible in the sample. Nevertheless, among those who chose the parameter-efficient path, LoRA is practically the no-alternative default. And the boundary: both full FT and PEFT are a change of the weights, unlike RAG, the prompt, and the context, which do not touch the weights. This is the watershed between "place knowledge" — RAG and context — and "encode behavior" — PEFT. In the narrative it is enough: full FT — almost never, PEFT and LoRA — the workhorse of 2026.

Sources:
[1] Hu et al. 2021 — LoRA — the base weights are frozen, low-rank adapters are trained. https://arxiv.org/abs/2106.09685
[2] Dettmers et al. 2023 — QLoRA — LoRA on top of a quantized model → fine-tuning on a single GPU. https://arxiv.org/abs/2305.14314
[3] HF PEFT — Beyond LoRA (LoRA 98.4% out of 20,834 cards) — 98.4% of models tagged PEFT use LoRA; caveat: the share among those tagged PEFT. https://huggingface.co/blog/peft-beyond-lora [VFY-day-of]

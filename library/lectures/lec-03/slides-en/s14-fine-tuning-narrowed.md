---
id: s14
type: assertion_visual
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 2.5
assertion: "Fine-tuning did not «die» — it narrowed to behavior/style/format/policy; knowledge went to RAG; distillation is a separate technique in tandem, not a kind of fine-tuning"
learning_goal: "The domain of fine-tuning + criteria for what-goes-where; distillation as an independent technique"
learning_outcomes: [LO7]
chapter_ref: "§3.1+§3.3+§3.5 [for-slide-s14]"
visual_brief: "Inline-define at the top. Below — 2 zones: «left FT → RAG/long context: knowledge» vs «stayed with FT: behavior/style/format/policy/distillation». Gold — the word «narrowed» / the knowledge↔behavior boundary."
interaction: none
---

# Visible content

## Title bar
«Fine-tuning did not die — it narrowed»

## Body
[Reliance on s13b, 16pt italic]
*Fine-tuning (definition — the previous slide) changes the weights themselves. Among engineers the saying goes: "in 2026 it died — RAG solves everything." This is inaccurate — it did not die, it narrowed.*

[2 zones in an Ocean rounded box]

**Left fine-tuning** *(in 2026)*
→ knowledge, facts, what changes → **RAG / long context**
*(baking facts into the weights: you can't cite it, can't update it pointwise, can't delete one)*

**Stayed with fine-tuning** *(a narrow but important domain)*
behavior · style · output format · policy adherence

[A separate bar — distillation]
**Distillation** — an *independent* technique (Hinton et al., 2015), taxonomically **not** a kind of fine-tuning; in practice it goes in tandem: fine-tune teacher → distillation of student *(two separate techniques)*

[Gold callout, bottom]
**The real question of 2026 is not «RAG or fine-tuning» but «what here is knowledge (→ RAG), what is behavior (→ FT)».** FT narrowed, it did not disappear.

## Speaker notes

On the previous slide we fixed the definition: fine-tuning changes the weights themselves, whereas the prompt and RAG touch only the context. Relying on this, let us work through its domain of application in 2026. Among engineers the phrasing goes "in 2026 fine-tuning died — RAG and long context solve everything." This is inaccurate. Fine-tuning did not die — it narrowed[1] and stopped being the default setting. It narrowed precisely because it changes the weights: knowledge — facts, documents, everything that changes — lies poorly in the weights and went to RAG and long context, where it can be cited and updated. What stayed with fine-tuning is a narrow but important domain — stable behavior, style, output format, policy adherence, rather than the model's knowledge.

Separately and carefully about distillation[2,3], because here there is frequent confusion. Distillation is an independent technique of knowledge transfer and model compression (Hinton, Vinyals, Dean, 2015): a student model learns to imitate the outputs of a teacher model through a separate loss function. Taxonomically it is not a kind of fine-tuning — method surveys place them in different categories. In practice the two techniques are often combined: first the teacher model is fine-tuned for the desired behavior, and then a compact student model is distilled from it. Hold this as "fine-tune teacher, then distillation of student — two separate techniques in tandem," rather than "distillation as a kind of fine-tuning."

Hence the what-goes-where criterion. Knowledge changes or provenance is needed — RAG or long context, not fine-tuning: the knowledge will go stale, retraining is expensive, there is a risk of forgetting. You need stable behavior, tone, format, policy — this is fine-tuning in the form of PEFT, not RAG. You need to lower cost on a narrow task — the tandem of fine-tune teacher plus distillation of student. The answer is deterministic and verifiable — ordinary code without AI. In other words, fine-tuning in 2026 is a narrow tool for behavior, format, policy, and efficiency, not a way to teach the model a domain; "teach the domain" in the sense of facts is RAG, in the sense of manner is PEFT, and almost never full fine-tuning.

Sources:
[1] BigData Boutique — Fine-Tuning When RAG Isn't Enough — fine-tuning narrowed to behavior/style/format/policy; knowledge → RAG. https://bigdataboutique.com/blog/fine-tuning-llms-when-rag-isnt-enough [VFY-day-of]
[2] Hinton, Vinyals, Dean 2015 — Distilling the Knowledge — distillation is an independent technique, taxonomically NOT a kind of fine-tuning. https://arxiv.org/abs/1503.02531
[3] PEFT survey — a taxonomy of tuning methods — surveys place distillation and fine-tuning in different categories. https://arxiv.org/abs/2403.14608

---
id: s16
type: case_study
section: "Section 3. Fine-tune vs prompt vs RAG"
duration_min: 2.5
assertion: "Narrow aggressive fine-tuning breaks general abilities; without an eval loop and dataset versions — this is not a risk but a «do not do it» criterion"
learning_goal: "The catastrophic forgetting failure + discipline turns a risk into a criterion"
learning_outcomes: [LO7]
chapter_ref: "§3.4 [for-slide-s16]"
visual_brief: "Left — 2 diverging lines: the target metric ↑, general abilities ↓ (imperceptibly). Caption «harder as scale grows». Right — a criterion bar «no eval loop + versions → do NOT do FT». Gold — the word «imperceptibly». Footer 12pt italic — source + the framing «studies show»."
interaction: none
---

# Visible content

## Title bar
«Failure: catastrophic forgetting»

## Body
[Inline-define, 16pt italic]
*Catastrophic forgetting — degradation of the model's general abilities as a result of narrow aggressive fine-tuning.*

[Left — 2 diverging lines in an Ocean rounded box]
**The target metric ↑** — the model excellently classifies tickets into its format
**General abilities ↓** — reasoning, following complex instructions sag **imperceptibly**  *(gold accent)*

Caption: *harder as the model's scale grows — a large one has a higher starting level, it has "more to fall"*

[Right — a criterion bar]
**No eval loop on general tasks + no dataset/weight versions**
→ you won't see the breakage before production + you won't be able to roll back
→ **this is not a "risk" — it is a «do NOT do fine-tuning» criterion**

[Alternative, bottom]
*The right way: PEFT (frozen weights — lower risk); for changing knowledge — RAG, not FT at all.*

[Footer, 12pt italic]
*Empirically observed under continual fine-tuning (Luo et al. 2023). The mechanisms — «studies show» (preprint).*

## Speaker notes

Let us introduce the term through a documented failure. Catastrophic forgetting is the degradation of the model's general abilities[1] as a result of narrow aggressive fine-tuning: by training the model to be very good at one narrow task, you can break what it could do before that.

How this looks as a case. A team fine-tunes a model on a narrow dataset — for example, classifying tickets into their format. On the target metric there is growth: the model classifies excellently. In parallel, imperceptibly, general abilities sag: reasoning on non-target tasks, following complex instructions. On the graph these are two lines: the solid one going up — the target metric (rises), and the dashed one going down — general abilities (fall imperceptibly). If the team measured only the target metric, the degradation is invisible until the model starts being used on something other than the narrow task. And then "why did it suddenly get worse at reasoning?" turns out to be a consequence of a month-old fine-tuning, for which there are already neither the old weights nor the dataset version. Mechanically: training for a narrow task moves the weights toward it, and the parameters that encoded general abilities are overwritten under aggressive full-FT. This is empirically observed under continual fine-tuning (Luo et al., arXiv:2308.08747, 2023), moreover with a counterintuitive feature: as the model's scale grows, the severity of forgetting tends to increase. "Let's take a bigger model to be more reliable" here works in reverse.

Why this belongs in the section on the choice of architecture rather than among curiosities. Forgetting by itself is a manageable risk. What makes it catastrophic is the absence of engineering discipline: there is no evaluation loop that would show degradation on a representative set of general tasks; there is no versioning of the dataset and weights for a rollback. Without an eval loop you will not notice that you broke general abilities until it surfaces in production; without versioning you will not return to a working version. The rule: if there is no eval loop and dataset versioning — do not do fine-tuning. This is not a "risk," it is a criterion: there will be neither a signal of the breakage nor a rollback button. The right alternatives: PEFT, where frozen weights give a lower risk; and for changing knowledge — RAG, not fine-tuning at all.

Sources:
[1] Luo et al. 2023 — Catastrophic Forgetting in LLM Continual FT — narrow aggressive FT breaks general abilities; harder as the model's scale grows. https://arxiv.org/abs/2308.08747

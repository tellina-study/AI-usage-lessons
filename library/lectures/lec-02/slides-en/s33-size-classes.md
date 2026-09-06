---
id: s33
type: assertion_visual
subtype: schema_matrix
section: "Section 5. Model Types and Sizes"
duration_min: 3
assertion: "Four size classes — from laptop to cluster: the bigger the model, the fewer input formats it turns away, but the more expensive and less locally accessible it becomes"
learning_goal: "Classifying models by parameter size: small/medium/large/MoE giants — what they run on, examples of specific models, multimodality by class"
learning_outcomes: [LO1, LO6]
chapter_ref: "§5.x (chapter-part3.md) [for-slide-s33]"
verify_day_of: true
visual_brief: "4-column classification matrix in Ocean rounded boxes (one icon atop each column — laptop/single GPU/server/cloud-cluster). Column 1 'Small — up to 8–10B': Qwen3.8-4B/8B, Llama-class models; hardware — laptop/smartphone; multimodality — usually text-only or basic vision. Column 2 'Medium — around 30B': Muse Glimmer 30B (top of the medium class); hardware — a single 24–32 GB GPU; multimodality — often has vision. Column 3 'Large — 70B+': hardware — multi-GPU/server; multimodality — generally full (text+image+sometimes audio). Column 4 'MoE giants — 400B+' (gold outline): DeepSeek V4-Pro 1.6T, Kimi K3 2.8T; cloud/cluster only — don't fit on consumer hardware; multimodality — full, top quality. Bottom gold callout about the limiting factor — memory, not compute."
---

# Visible content

## Title bar
"Four model size classes — from laptop to cluster"

## Body
[4-column matrix, Ocean rounded boxes, an icon atop each column]

**Small — up to 8–10B** *(icon: laptop/smartphone)*
- Examples: Qwen3.8-4B / Qwen3.8-8B, Llama-class models
- Hardware: laptop, smartphone, edge device
- Multimodality: usually text-only or basic vision

**Medium — around 30B** *(icon: a single GPU)*
- Examples: Muse Glimmer 30B (top of the medium class)
- Hardware: a single 24–32 GB GPU
- Multimodality: often has vision

**Large — 70B+** *(icon: server)*
- Hardware: multi-GPU / server
- Multimodality: generally full (text + image, sometimes audio)

**MoE giants — 400B+** *(icon: cloud/cluster, gold outline)*
- Examples: DeepSeek V4-Pro (1.6 trillion), Kimi K3 (2.8 trillion)
- Hardware: **cloud or a dedicated cluster only** — they don't fit on consumer hardware in any form
- Multimodality: full, top quality

[Gold callout]
**The limiting factor in the choice is memory capacity, not compute. The bigger the model, the more multimodal capability it has — but the smaller the odds you can run it yourself.**

## Speaker notes

Before talking about where to run a model — locally or in the cloud — let's cover a different axis: the model's size itself. This isn't the same as "local or cloud": a small model can perfectly well run in the cloud, while a giant physically won't fit on your hardware under any circumstances. We'll classify by parameter count — from billions to trillions.

Small models — up to 8 to 10 billion parameters — are a class that genuinely runs on a laptop or smartphone: Qwen3.8 in its 4B and 8B variants, Llama-class models. In terms of multimodality, these are usually text-only models or ones with basic image support — the training set and architecture at this size limit the breadth of skills. Medium models — around 30 billion parameters — are represented by Muse Glimmer 30B, the upper bound of this class: such a model fits on a single gaming GPU with 24 to 32 gigabytes of memory, and full-fledged image input support is already common here.

Large models — from 70 billion parameters — require several GPUs or a full server; multimodality here is generally already full — text, image, sometimes audio. And a separate class is the giant models built on a mixture-of-experts architecture, from 400 billion parameters and up: DeepSeek V4-Pro at 1.6 trillion parameters, Kimi K3 at 2.8 trillion — the largest open model in history. Despite open weights, models like these physically don't fit on consumer hardware in any form — the only way to use them is a cloud API or your own expensive cluster. This class has full multimodality and, generally, the best quality on the market.

The general pattern worth taking away: the bigger the model, the broader its multimodal capability and answer quality, but the lower your odds of running it yourself — the limiting factor is always memory capacity, never raw compute power. This size criterion is an independent axis from the "local or cloud" question we'll cover on the next slide: there, we'll see that even the giants' open weights don't settle the question of local deployment.

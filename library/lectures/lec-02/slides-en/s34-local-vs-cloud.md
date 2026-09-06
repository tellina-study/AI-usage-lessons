---
id: s34
type: comparison
section: "Section 5. Model Types and Sizes"
duration_min: 2.5
assertion: "The loop is the same locally and in the cloud — but 'open weights' no longer means 'locally runnable'"
learning_goal: "Classification by deployment location (not by size — see the previous slide): the local pole has grown up, three categories instead of two"
learning_outcomes: [LO1, LO6]
chapter_ref: "§4.9 (chapter-part2.md) [for-slide-s34]"
visual_brief: "Three category columns in Ocean rounded boxes (instead of the old two): 'Truly local — up to ~30B' (one-line heading) (Qwen3.8-27B, Muse Glimmer 30B; hardware RTX 5090 32 GB / Apple unified 64–128 GB; limit — memory), 'Open-but-cloud-only giants' (Kimi K3 2.8T — the largest open model; DeepSeek V4-Pro 1.6T; don't fit on consumer hardware), 'Closed APIs' (flagships). The middle column highlighted as the 2026 categorical news (gold badge 'open ≠ local'). Bottom line on the reasons for choosing local."
verify_day_of: true
---

# Visible content

## Title bar
"'Open weights' no longer means 'locally runnable'"

## Body
[3 category columns, Ocean rounded boxes]

**Truly local — up to ~30B**
- Qwen3.8-27B (Apache 2.0, image+video input, 262K window), Muse Glimmer 30B
- Hardware: RTX 5090 (32 GB) · Apple unified 64–128 GB
- The limit is **memory capacity**, not compute

**Open-but-cloud-only giants** *(gold badge: open ≠ local)*
- Kimi K3 — 2.8 trillion parameters, the largest open model
- DeepSeek V4-Pro — 1.6 trillion
- **Don't fit on consumer hardware in any form**

**Closed APIs**
- Flagship-level quality — still lives here
- Pay per token, data flows through the provider

[Bottom line]
The reasons for choosing local haven't changed: data privacy · no per-token cost at volume · independence from the network. The decision should follow the data and the volume, not ideology.

[Gold callout]
**What to do:** if the task fits in ~30B and the data can't leave your perimeter — go local; if you need flagship quality — go with a closed API.

## Speaker notes

The inference loop is exactly the same in the cloud and on your own hardware; the choice between them isn't a choice of technology, it's a point on the "quality × privacy × cost" scale from Lecture 1. Let's update the facts for 2026.

The local pole has grown up noticeably. The past year's open models — Qwen3.8-27B with multimodal input and a 262-thousand-token window, Muse Glimmer 30B — cover most personal tasks and a chunk of enterprise ones in terms of capability. Hardware: an RTX 5090 with 32 gigabytes of video memory comfortably handles models in the 27–34 billion parameter class; Apple machines with 64 to 128 gigabytes of unified memory swallow models that discrete GPUs can't fit. The limiting factor is unchanged — memory capacity, not compute; when a model fits entirely in video memory, local speed is comparable to the cloud.

An important categorical correction for the year: "open weights" no longer means "locally runnable." Kimi K3 — two-point-eight trillion parameters, the largest open model in history — and DeepSeek V4-Pro don't fit on consumer hardware in any form; their openness is realized through hosting by providers or your own cluster. There are now three categories: closed APIs, open-but-cloud-only giants, and truly local models up to roughly thirty billion parameters. Base your local-deployment decision on the third category — and almost always for the same three reasons: data privacy, no per-token cost at large volumes, independence from the network; for flagship-level quality, you're still headed to the cloud.

And the general rule: the decision is made based on data and volume, not on "cloud versus local" ideology — for a product team, the real cost line item is often not tokens but the engineering time spent operating your own stack.

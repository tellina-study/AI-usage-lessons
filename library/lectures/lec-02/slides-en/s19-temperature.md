---
id: s19
type: case_study
section: "Section 4. Sampling"
duration_min: 3
assertion: "Temperature — how 'sharp' the choice is. T=0: argmax. T=1.0: standard. T=2.0: chaos"
learning_goal: "Temperature (main) + brief top-p/top-k — the 3rd of 3 'whys'"
learning_outcomes: [LO4, LO7]
chapter_ref: "§4.2 [for-slide-s19]"
visual_brief: "3 copies of the s18 distribution with different T: T=0 — argmax (determinism), T=1.0 — standard, T=2.0 — chaos. Bottom-line text about top-p (nucleus) and top-k. Gold: '3rd of 3 whys'."
interaction: live_comparison
---

# Visible content

## Title bar
"Temperature: how sharp the choice will be"

## Body
[3 versions of the distribution side by side, Ocean rounded boxes]

**T = 0** (argmax)
[Distribution: apple 1.00, all the rest 0]
A deterministic choice — `apple`. Repeat the request 10 times — the same.

**T = 1.0** (standard)
[Distribution: apple 0.32, pizza 0.19, salad 0.14, …]
Sampling proportional to the original probabilities. Natural variability. T = 0.7 — the consensus choice for chat tasks.

**T = 2.0** (chaos)
[The distribution is almost uniform]
The distribution is flattened; the model often picks unexpected options.

[Bottom-line, a thin line at the bottom]
**Alternative knobs:** **top-p (nucleus)** — cuts rare tokens by cumulative probability; **top-k** — cuts by the number of candidates. T is enough to start, top-p/k — for fine-tuning.

[Gold callout]
"Stochastic sampling at T > 0 gives different answers to the same request"

## Speaker notes

The main sampling parameter is temperature, denoted T. Temperature controls how "sharp" the choice will be. It's an API parameter: `temperature=0.0`, `temperature=0.7`, `temperature=2.0`. Technically, temperature is a coefficient by which the logits (the model's internal "raw" scores before normalization into probabilities) are divided before the normalization operation; we won't introduce the formula here, the consequence is what matters.

At T = 0 the model picks the token with the highest probability. This is the argmax operation — "take the one whose probability is maximal". In our "ate …" example the model will almost always pick `apple` (0.32 — the maximum). The answer is predictable and nearly deterministic — repeat the request ten times, you get the same thing. A small caveat: in production there can be micro-variability because server-side batching and floating-point on the GPU don't give bit-for-bit identical results between runs; for most tasks this variability is negligible.

At T = 1.0 — the standard mode. The model samples proportionally to the original probabilities: `apple` will be chosen about 32% of the time, `pizza` 19%, `salad` 14%, and so on. This gives natural variability — each run can return a different answer, but all answers lie within the plausible zone.

At T = 2.0 the distribution is "flattened": the difference between the most probable and the rare tokens shrinks, and the model starts to pick unexpected options more often. In extreme cases the answers become almost chaotic — tokens are chosen that are unlikely in real language after "ate".

Besides temperature there are two alternative knobs: top-p (nucleus sampling) — a parameter that cuts off the "tail" of rare tokens: the model keeps the minimal subset of the most probable tokens whose cumulative probability is at least p, and samples only from them. And top-k — a parameter limiting the number of candidates: the model keeps the top-k most probable tokens. In practice, for most tasks it's enough to tune temperature; top-p and top-k are a second layer of control.

This slide answers the third of the three "why" questions posed at the start of the lecture: why the same request gives different answers. The short answer: because at T greater than zero, sampling is a stochastic process, and from the same distribution each run can pick a different token. This is not a bug; it's an engineering decision that gives models natural variability, which for most interactive tasks is perceived as "human-likeness".

Sources:
[1] Holtzman et al. (2019) — nucleus sampling (top-p) — temperature and top-p control the shape of the distribution during sampling. https://arxiv.org/abs/1904.09751

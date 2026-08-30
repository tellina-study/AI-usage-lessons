---
id: s09
type: case_study
duration_min: 3
assertion: "The space is open: 4 breakthroughs of 2023–2026 from non-first players"
learning_goal: "Don't despair: serious breakthroughs come from different teams"
learning_outcomes: [LO1]
references: [mistral-7b-2023, deepseek-2025-r1, semianalysis-2025, bloomberg-2025-deepseek, openclaw-2025-steinberger, gerganov-llamacpp-2026]
visual:
  pattern: 4_episodes_horizontal_timeline
  primary: "4 episodes laid out horizontally: Mistral 7B (Apache 2.0) → DeepSeek R1 ($589B Nvidia drop) → OpenClaw (100K stars) → llama.cpp/ggml.ai (Georgi Gerganov, 100K+ stars)"
---

# The space is open: 4 breakthroughs of 2023–2026 from non-first players

## Assertion

The space is open: 4 breakthroughs of 2023–2026 from non-first players.

## Visual

Four cards laid out horizontally in Ocean rounded boxes, each with a date and one headline number / claim. Left to right: Mistral 7B (September 2023, Apache 2.0, beats Llama-2 13B). DeepSeek R1 (January 2025, $589B Nvidia drop in a single day, highlighted in gold). OpenClaw (November 2025, Steinberger's open-source agent: 100K★ in a quarter, 22 channels, 100 AgentSkills). llama.cpp / ggml.ai (Georgi Gerganov: solo project → joined Hugging Face on February 20, 2026 → 100,000+ GitHub stars in March 2026, faster than PyTorch and TensorFlow).

## Speaker notes

Looking at the numbers from the previous slide, it's easy to conclude that everything has already been done: OpenAI, Google, and Anthropic lead — the largest players with multibillion-dollar budgets. That impression is deceptive. Over the last three years the AI field has seen several high-profile events, each of which shows that the space of possibilities is open, and serious breakthroughs come not only from the first players.

Lesson: a small European team can ship a model at the level of the big players within a few months of the company's founding. Episode one — Mistral 7B, September 2023. The French lab Mistral AI, founded earlier that same year by alumni of Meta and Google DeepMind, released a model under the Apache 2.0 license — with no restrictions on commercial use. On benchmarks Mistral 7B outperformed Llama-2 13B, a model nearly twice its size.

Lesson: even a debatable cost-accounting methodology can trigger a real, measurable shock on the global market — check the claimed numbers, but don't ignore their effect. Episode two — DeepSeek R1, January 2025. A Chinese lab released a reasoning model at the level of OpenAI o1: ninety-seven point three percent on the MATH-500 benchmark versus ninety-six point four for o1. The published cost of a single final training run of V3 was about five point six million dollars, orders of magnitude less than Western estimates. The full infrastructure cost, according to SemiAnalysis, is one point three to one point six billion. These are different numbers: the cost of a single training run and the full infrastructure. On January 27 the market reacted — Nvidia's market capitalization fell by five hundred eighty-nine billion dollars in a single day, the largest single-day loss of market capitalization in history.

Lesson: one person with the right concept can ship an agent or product that changes the market within weeks. Episode three — OpenClaw, November 2025. Peter Steinberger, known for Mac development, single-handedly launched an open-source autonomous AI agent. The project changed names several times — Clawdbot, Moltbot — and settled on OpenClaw. By early 2026 the project had gathered more than a hundred thousand stars on GitHub (sixty thousand of them in the first seventy-two hours).

Lesson: one person with the right concept can build an infrastructure layer that thousands rely on — not a product for the end user, but a foundation on which the entire open ecosystem runs. Episode four — llama.cpp and ggml.ai, the story of Georgi Gerganov. The project began as a solo initiative by Gerganov — the author of whisper.cpp — and grew into a small independent team, ggml.ai. On February 20, 2026, the team, instead of raising venture funding, joined Hugging Face for infrastructure support while retaining full autonomy and technical leadership: the project stayed "one hundred percent open-source, community-driven, as it is now." In March 2026 llama.cpp crossed a hundred thousand stars on GitHub — faster than PyTorch or TensorFlow. By mid-year — about a hundred seventeen thousand stars, about twenty thousand forks, contributions from more than seven hundred developers.

Don't despair. The course prepares you to work with durable engineering concepts that outlive the turnover of model generations.

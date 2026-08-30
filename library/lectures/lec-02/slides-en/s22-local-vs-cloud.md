---
id: s22
type: assertion_visual
section: "Section 4. Sampling"
duration_min: 1
assertion: "The inference loop is the same locally and in the cloud — but model size determines quality"
learning_goal: "Cross-cutting frame 1: Local vs cloud (callback to Lec-1 without repetition)"
learning_outcomes: [LO1, LO6]
chapter_ref: "§4.5 [for-slide-s22]"
visual_brief: "2 Ocean rounded boxes side by side: Local (Ollama, llama.cpp) — small models, privacy. Cloud (OpenAI, Anthropic, Yandex) — large models, 200-500ms, pay per token."
---

# Visible content

## Title bar
"Local vs cloud: the same loop, a different size"

## Body
[2 Ocean rounded boxes side by side, parallel structure]

**Local (Ollama, llama.cpp, LM Studio)**
- Size: **1–13B parameters**
  - Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B
- **Data privacy** — requests do not go to a provider
- Slower on consumer hardware
- A limited context window
- No per-token charge

**Cloud (OpenAI, Anthropic, Yandex, Sber)**
- Size: **200B+ parameters**
- Response latency: 200–500 ms
- Context window: hundreds of thousands — 1M tokens
- **Pay per token**
- Data through the provider's API

[Sub-caption in small print, at the bottom]
*The inference architecture is the same. Size and environment differ. We discussed this trade-off in more depth in Lecture 1.*

## Speaker notes

The inference loop described above — tokenization, embeddings, attention, sampling, return to the start — is the same in cloud LLM services and in locally deployed models. From the mechanism's standpoint, ChatGPT, Claude, GigaChat, a local Llama 3.1 on a laptop, or Qwen 2.5 on an edge device work identically. They differ in model size (and, consequently, in answer quality) and in the execution environment.

Local deployment — Ollama, llama.cpp, LM Studio, vLLM — usually runs models of 1-13 billion parameters: Qwen 2.5 1.5B, Llama 3.2 1B, Llama 3.1 8B, Mistral 7B as of 2026. The advantages are data privacy (requests don't go to a third-party provider), no per-token charge, and independence from the internet. The drawbacks: speed on consumer hardware is noticeably lower than with cloud providers; local models often have a smaller context window; answer quality on hard tasks lags behind large models.

Cloud services — OpenAI, Anthropic, Google, the Russian Yandex and Sber — run models of a significantly larger size (on the order of hundreds of billions of parameters and more). Answer quality on hard tasks is higher; the context window is larger (hundreds of thousands and a million tokens); the typical response latency is 200-500 ms. This is paid for by sending data through the provider's API (with all the storage- and usage-policy questions we discussed in Lecture 1) and by paying per token — which for Russian text is higher than for English, as we saw earlier today.

The deep discussion of local vs cloud models — with a decision diagram, the break-even point by request volume, and regulatory aspects — was in Lecture 1 and is not repeated here. What matters to take away is one point: architecturally, inference looks the same; the differences are in model size and environment. When you choose between "local" and "cloud", you're choosing not between different technologies but between different points on the "quality × privacy × cost" scale, and that scale does not depend on how the inference loop is arranged inside.

Sources:
[1] Mistral AI — Mistral 7B — local open-weight models 1-13B vs cloud 200B+. https://mistral.ai/news/announcing-mistral-7b [VFY-day-of]

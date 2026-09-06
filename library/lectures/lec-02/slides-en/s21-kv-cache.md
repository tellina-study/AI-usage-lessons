---
id: s21
type: assertion_visual
subtype: schema_pipeline
section: "Section 3. Attention Mechanism"
duration_min: 4
assertion: "K and V for the context are cached; only Q is recomputed — hence two generation phases and 'long chats slow down'"
learning_goal: "KV-cache as the central inference optimization; the prefill/decode asymmetry and its observable consequences"
learning_outcomes: [LO1, LO6]
chapter_ref: "§3.3 (chapter-part2.md) [for-slide-s21]"
visual_brief: "Top — KV-cache schema: a row of context tokens, under each two tiles K and V (teal, with a 'cached' lock icon), on the right a new token with a single Q tile (gold) and arrows to the stored K/V. Middle — two phases side by side in Ocean rounded boxes: 'Prefill' (parallel processing of the prompt, compute-bound, determines the pause before the first character) vs. 'Decode' (sequential, token by token, memory-bound, determines typing speed). Between them a RIGHT_ARROW. Bottom — a vendor table: 'OpenAI — automatic,' 'Gemini — implicit (automatic),' 'DeepSeek — automatic disk-based,' 'Anthropic — explicit (cache_control)' [VFY-day-of]. Gold callout at the bottom on when the cache works vs. when it doesn't (not 'new chat = superstition,' but 'when the cache misses — it slows down and costs more')."
verify_day_of: true
---

# Visible content

## Title bar
"K and V are cached — only Q is recomputed"

## Body
[Top — schema: context tokens with K/V tiles "cached," new token with a Q tile]

**KV-cache:** the Key/Value of already-processed tokens are stored in accelerator memory. At each step, only the Q of the new token is computed — against the stored K/V.

[Bottom — two phases, 2 Ocean rounded boxes side by side]

**Phase 1 — prefill (processing the prompt)**
- All input tokens are known at once → K/V are computed **in parallel**
- Bound by **compute power**
- Determines the **pause before the first character of the answer** (TTFT)

**Phase 2 — decode (generating the answer)**
- Strictly **sequential**, token by token
- Every step reads **the entire accumulated cache** from memory
- Bound by **memory bandwidth** → "typing" speed

[Vendor table — who caches automatically, who requires an explicit marker]
| Provider | Cache |
|---|---|
| OpenAI | automatic |
| Gemini | implicit (automatic) |
| DeepSeek | automatic, disk-based |
| Anthropic | explicit — `cache_control` marker |

[Gold callout]
**A working KV-cache makes resubmitting history cheap and fast. "Slow and expensive" is what happens when the cache MISSES — not an inherent property of long chats.**

## Speaker notes

Recall the observation from the previous slide: Query is about the current step, Key and Value are about the already-processed context, which doesn't change. Generation is autoregressive: tokens come out one at a time, and a naive implementation would recompute the K and V of every token from scratch at every step — but they don't change. Hence the central optimization of all large-model inference — KV-cache: the Key and Value vectors of already-computed tokens are stored in accelerator memory, and at each step only the Q of the new token is computed, along with its products against the stored K/V.

Out of the cache grows the two-phase asymmetry you observe in every request. Prefill — processing the input prompt: all of its tokens are known at once, so their K/V are computed in parallel in one large matrix computation; this phase is compute-bound and determines the pause before the first character of the answer. Decode — generation: strictly sequential, and at every step you have to read the entire accumulated cache from memory; this phase is bound by memory bandwidth and determines the speed in tokens per second. That's why a long prompt mainly stretches out the pause before the first token, while a long context overall slows down every generation step.

The exact wording of the conclusion matters here, because it's easily distorted into the folk wisdom "new task → new chat." As long as the KV-cache works — that is, the history matches what's already been computed — resubmitting the history is cheap and fast: that's the whole point of the cache's existence. "Slow and expensive" doesn't happen as a property of long chats in general; it happens specifically when the cache misses — when the context changes at the beginning, when the session has expired, when the provider has evicted your cache from memory to serve someone else's load. The history is submitted to the model in full on every turn — the model is stateless, as we established in Lecture 1 — but that doesn't mean every turn is recomputed from zero.

Cache implementation differs across providers, and this directly affects what you need to do by hand. At OpenAI and DeepSeek the cache kicks in automatically — no special setup in the request; at DeepSeek it's also disk-based, not just in accelerator memory. Google Gemini has implicit caching, also on by default. Anthropic's cache is explicit: you need to place the `cache_control` marker at the right spots in the prompt yourself — otherwise the cache won't trigger, even if the content matches [VFY-day-of]. Practical takeaway: if you're on Anthropic and not seeing savings, check whether the marker is placed where it needs to be; on the other three, check the cache-hit-rate metrics in the API response, because "automatic" doesn't mean "guaranteed to trigger." Scale of the effect: at contexts of hundreds of thousands of tokens, one user's cache occupies gigabytes of accelerator memory — hence providers' aggressive batching and the premium pricing on long contexts.

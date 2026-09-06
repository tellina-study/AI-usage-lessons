---
id: s22
type: assertion_visual
section: "Section 3. Attention Mechanism"
duration_min: 3.5
assertion: "Prompt caching is a bet on reuse: reads cost 0.1× the rate, writes cost more than plain input, and one changed token invalidates everything after it"
learning_goal: "Prompt-caching economics via a schema of three sequential requests: write → cache hit → cache miss; the rule 'stable content first'"
learning_outcomes: [LO4, LO6]
chapter_ref: "§3.4 (chapter-part2.md) [for-slide-s22]"
visual_brief: "Left 55% — an Ocean rounded box with a schema of THREE sequential requests: Request 1 'prefix is written to the cache' (writes cost 1.25–2×, teal), Request 2 'same prefix → cache hit' (reads cost 0.1×, newest models — 0.025×, gold), Request 3 'a line was added at the front → prefix no longer matches → cache miss' (full price, red cross). Below them a mini-case $45,000 → $8,000 (−82%) as two bar columns. Right 45% — an exact-prefix schema: a strip of blocks 'system prompt | instructions | documents | ⚡new line | question,' the new-line block with a red cross breaks the green fill of every block after it (illustrating request 3). Bottom gold callout 'Stable content goes first, variable content goes last.'"
verify_day_of: true
---

# Visible content

## Title bar
"Prompt caching is a bet on reuse, not a discount"

## Body
[Left — schema of three requests, Ocean rounded box]

**Request 1 — write to cache**
Sent the prompt for the first time → the prefix (system + instructions + documents) is written to the cache. Costs **1.25–2× the base input rate** — more expensive than usual.

**Request 2 — cache hit**
Same prefix again → cache match. Reads cost **0.1× the base rate** (newest models — down to 0.025×).

**Request 3 — cache miss**
A line was added at the front of the prompt → the prefix no longer matches byte-for-byte → cache miss, the whole load is billed at **full price**, as if there had been no cache at all.

**Case:** 50,000 document analyses per month — **$45,000 without cache → $8,000 with cache (−82%)**

[Right — exact-prefix schema]

**Condition: exact prefix match.** One changed token invalidates the cache for everything after it.

[Strip: system prompt → instructions → documents → ⚡new line → question]
*(illustrates request 3: the "new line" block, marked with a red cross, breaks the green fill of every block after it)*

[Gold callout]
**Composition rule: stable content goes first (prompt, instructions, examples, documents), variable content goes last.**

## Speaker notes

KV-cache lives inside a single generation. Providers took the next step: if two different requests share the same prefix — the same system prompt, instructions, documents — their K/V can be reused across requests. This is prompt caching, and since 2025–2026 it's the main lever for optimizing the cost of LLM workloads.

Let's trace the mechanics through three sequential requests — it's clearer this way than through isolated numbers. First request: you send the prompt for the first time, there's no cache yet — the prefix is written to the cache, and writing costs more than a normal input, anywhere from 1.25 to 2 times the rate depending on the cache's time-to-live. Second request: you send the same prefix — say, the same system prompt and the same set of documents, only a new user question at the end — the prefix matches byte-for-byte, the cache hits, and you pay a tenth of the base input rate, on the newest models as low as a fortieth. Third request: someone added one line at the start of the prompt — say, the current date or an updated instruction — and now the prefix no longer matches what's in the cache starting from that line. Cache miss: the entire load is billed at full price, as if the cache had never existed, and if you're using explicit writes, you also pay the write surcharge on top. The cache isn't free — it's a bet on reuse: it pays off from the second or third hit onward, while a workload made of unique requests with no shared prefix only gets more expensive. The scale of the effect is real: a case of 50,000 document analyses per month — $45,000 without caching versus $8,000 with caching, an 82 percent saving.

The main technical condition is visible in the third request — an exact prefix match: the cache only hits if everything up to the checkpoint matches byte-for-byte. A classic self-inflicted wound is adding something variable to the start of the system prompt, like the current date and time: then no request will ever land in the cache.

Hence the composition rule: stable content first, variable content last. And a one-minute audit for a running pipeline: look at the cache-accounting fields in the API responses — if cache reads are zero despite a stable system prompt, you can almost certainly fix this in one evening by reordering the prompt. For multi-step agents, the cache isn't an optimization — it's a condition for profitability: we'll come back to that in the next lecture.

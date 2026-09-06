---
id: s41
type: summary
section: "Section 6. Wrap-up"
duration_min: 2
assertion: "Lecture 3 — how a model reaches beyond its context: RAG, tools, MCP, the agentic loop"
learning_goal: "A bridge to Lecture 3 anchored in today's material (role = tokens with attention weight → injection, the similarity boundary → RAG, cache → agent economics, thinking → budget)"
learning_outcomes: [LO1]
chapter_ref: "§5.7 (chapter-part3.md) [for-slide-s41]"
visual_brief: "v3.1 (#183 round 3, composition fix): hero illustration of a bridge — a HORIZONTAL STRIP under the title (not a background behind cards as before — the cards used to cover it, leaving only a stump visible). The image is cropped to content (empty top margin of the source PNG removed), the bridge silhouette reads in full: arch, cables, both towers, end anchors. Below — 4 Ocean rounded boxes in a 2×2 grid with icons — Lecture 3 concepts: RAG (magnifier+document), Tools / function calling (gear), MCP (connector), Agentic loop (loop). Each has a thin anchor line from today's lecture (teal, italic): for RAG — 'similarity ≠ relevance', for tools — 'structured outputs guarantee call format', for MCP — 'stable prefix → cache hit', for the loop — 'the agent reads external content → prompt injection'. Gold on the bridge title."
---

# Visible content

## Title bar
"Lecture 3: how a model reaches beyond its context"

## Body
[4 Ocean rounded boxes in a 2×2 grid, icons + anchor line]

**(1) RAG**
Semantic search over your own knowledge base → retrieved fragments go into the context.
*Anchor: similarity ≠ relevance — the main reason naive search disappoints.*

**(2) Tools / function calling**
The model generates a structured call → an external system executes it.
*Anchor: structured outputs guarantee call format reliability.*

**(3) MCP**
An open protocol for connecting tools.
*Anchor: stable prefix → cache hit, agent economics.*

**(4) Agentic loop**
Action → observation → correction.
*Anchor: instructions are just tokens with attention weight too → prompt injection; invisible tokens × number of steps.*

## Speaker notes

The pipeline we've assembled has a hard boundary: the model only sees its context and can't reach beyond it — not for fresh data, not for acting in the world. The next lecture — "Agents, RAG, API" — is about how this boundary gets crossed: semantic search over your own knowledge base with retrieved fragments substituted into the context — a direct extension of the embeddings from today's second section; tool calling, where the model generates a structured function call and reliability of the call format is guaranteed by the structured-output mechanism you already know; the open MCP protocol for connecting tools; and the agentic loop of "action — observation — correction."

Four anchors from today's lecture will be needed there. Since instructions to the model are just tokens getting weighted in attention like any other text, and an agent reads external content, prompt injection isn't exotic — it's a baseline threat mode for agentic systems; a detailed breakdown of protocol roles and their forgery is coming in the next lecture. Similarity does not equal relevance — the main reason naive semantic search disappoints, and the starting point for a conversation about quality. Agent economics are built on prompt caching — a multi-step loop with an unstable prefix ruins it. And every step of the loop can carry invisible reasoning tokens — an agent's budget that ignores them is off by a wide margin.

Before our next meeting — four short experiments, each ten to twenty minutes: counting letters on three available models; ten runs of the same query at zero temperature with a byte-for-byte comparison; the cosine similarity of the pair "configure SSL — disable SSL"; and an audit of your own project — is the cache working, and is reasoning turned on somewhere it isn't needed. The results will be needed in the conversation about agents — where the cost of each of these boundaries gets multiplied by the number of steps.

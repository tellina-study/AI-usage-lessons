---
id: s19
type: assertion_visual
section: "Section 4. Agents"
duration_min: 2.5
assertion: "3 mechanisms make the model a system component (structured output / function calling / prompt caching); MCP standardizes connection (N×M→N+M), but ease of connection does not equal the security of what is connected"
learning_goal: "The API layer (3 mechanisms) + MCP (N×M→N+M, the pivot of trust) at the assertion level (the walkthrough and privacy → notes/chapter)"
learning_outcomes: [LO7]
chapter_ref: "§4.1 [for-slide-s19]"
visual_brief: "3 equal cards, one thesis per mechanism. A bar at the bottom: «none makes the model more reliable». Gold — the connecting conclusion. The savings numbers are NOT on the visible layer."
interaction: none
---

# Visible content

## Title bar
«The API layer: the model as a system component»

## Body
[3 equal cards in an Ocean rounded box, one thesis each]

**Structured output**
the model is obliged to return an answer strictly by a schema (JSON), not free text
→ output = **valid data, not text to parse** → the model is *embeddable*

**Function calling** *(calling functions / tools)*
the model returns "call tool X with arguments Y"; **your code executes it, not the model**
→ the model is *active* in the system

**Prompt caching**
reuse the computed state of an unchanged prefix
→ don't overpay for the repeated part → the model is *economically viable*

[Conclusion bar, bottom]
**None of the three makes the model more reliable or auditable — they expand what the model can do without changing its nondeterministic nature. The rule of the ladder is not repealed.**  *(gold accent)*

## Speaker notes

For AI to become part of a system, three mechanisms of the API layer are needed. The first is structured output: a mode in which the model is obliged to return an answer strictly by a given schema, for example JSON, rather than free text. Technically the schema is compiled into a constraint on sampling, so the model cannot produce a structurally invalid answer; the output turns from text that has to be parsed with regexes into data guaranteed to be valid in form. This makes the model embeddable. A subtlety: validity of form is guaranteed, but not of content — a field may be factually wrong. The second is function calling: instead of answering with text, the model can return a request "call tool X with arguments Y," and your code executes the call, not the model. The model only states an intention — this makes it active and will be key for security. The third is prompt caching: reusing the already computed state of an unchanged prefix so as not to recompute it each time; the state is cached, not the text of the answer. This makes the model economically viable at volume and makes full-context for a small stable corpus a real competitor to RAG. None of the three makes the model more reliable or auditable — they expand capabilities without changing the nondeterministic nature, and they do not repeal the rule of the ladder.

There remains the question of how a tool connects to the model. Until the end of 2024, each integration solved this in its own way. MCP, the Model Context Protocol, is an open standard for a unified way to connect[1] tools to a model; the metaphor is "USB-C for tools." The essence is in the arithmetic: with N models and M tools, naively you need N times M integrations, and MCP reduces this to N plus M. But here is a critical pivot: standardizing connection does not mean the security of what is connected and even aggravates the trust problem. Every connected tool is code in your environment and a channel through which untrusted text enters the context. "Connect in a minute" and "trust what is connected" are different questions; MCP solved the first and made the second sharper. Ease of connection is not an argument for connecting.

Sources:
[1] Anthropic — MCP donation / Agentic AI Foundation (N×M→N+M) — MCP standardizes connection; ease of connection ≠ the security of what is connected. https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation [VFY-day-of]

---
id: s20
type: assertion_visual
section: "Section 4. Agents"
duration_min: 2.5
assertion: "MCP N×M→N+M; ~11% of the catalog is actually runnable; ease of connection ≠ security"
learning_goal: "MCP as a connection standard + critical reading of ecosystem scale + the trust turn"
learning_outcomes: [LO7]
chapter_ref: "§4.1 [for-slide-s20]"
verify_day_of: true
---

# Visible content

## Title bar
"MCP: a connection standard — not a guarantee of trust"

## Body
[Left — what MCP solves]
**MCP (Model Context Protocol)** — "USB-C for LLM tools"
N models × M tools = N×M integrations → MCP: **N+M**
Opened by Anthropic in 11/2024, adopted by OpenAI and Google in 2025

[Right — scale, read critically]
Catalogs claim "up to **90,000** servers", but the actually runnable ones are only **≈10,000 ≈ 11%**
The rest are duplicates, broken, stubs; and even the working ones are **not checked for security**

[Panel — the trust turn]
30+ CVEs in 60 days (**≈43%** — command injection); path traversal in **82%** of 2,614 scanned implementations

[Gold callout, bottom]
**Standardizing the connection does not mean the connected thing is secure — and it sharpens the trust problem.** Ease of connection is not an argument for connecting.

## Speaker notes

Function calling decides how the model formulates a call. MCP decides how the tool physically connects. Before 2024 each vendor solved this in its own way, producing a combinatorial explosion. MCP is an open standard: N models × M tools = N×M integrations → N+M. The metaphor: USB-C for tools. Anthropic opened it in November 2024, OpenAI and Google adopted it in 2025 — a de facto industry standard.

Read the scale critically. Catalogs name up to 90,000 servers, but the actually runnable ones number about 10,000 — 11%. The rest are duplicates, broken, stubs. Even the working ones are not checked for security.

The critical turn: standardizing the connection does not mean the connected thing is secure — it worsens the problem. Every tool is code that runs in your environment, a channel for untrusted text. Over 60 days: 30+ CVEs on MCP servers, 43% — command injection, 82% of implementations vulnerable to path traversal. "Connect it in a minute" and "trust the connected thing" are different questions. MCP solved the first and made the second sharper. Convenience is not an argument for connecting.

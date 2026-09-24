---
id: s-mcp-api
type: comparison_table
section: "Section 4. Agents"
duration_min: 2.5
assertion: "MCP or a direct API — not alternatives: MCP is a thin discovery/portability layer ON TOP of REST; N×M→N+M pays off only when N,M≥2–3; ~25% of the registry are unusable, 43.7% top MCP-Universe"
learning_goal: "When MCP pays off vs when a direct API is simpler and safer — a decision table (§4.1b)"
learning_outcomes: [LO7, LO4]
chapter_ref: "§4.1b [for-slide-mcp-api]"
subtype: comparison_table
new_in_v6d2: "#196 WAVE D2 owner #14 — MCP vs API decision table (after s20)"
---

# Visible content

## Title bar
«MCP or a direct API — these are not alternatives»

## Body
[Base] REST/gRPC is the transport that does the work; MCP is a thin standard layer ON TOP, for discovering and calling tools. In most deployments an MCP server wraps an existing REST API rather than replacing it. Threshold: N+M < N×M only when N, M ≥ 2–3.

[Decision table — 2 columns]
Take MCP: many agents × tools; discovery at runtime; portability across vendors; reuse by other teams; ready for a security review of every server.
Take a direct API: one app, 1–2 tools; a fixed set; one stack; a private integration; you need a small auditable surface now.

[Stat strip] ~25% of the registry unusable · 43.7% top MCP-Universe · injection/path traversal — see the slide on MCP (the trust pivot).

[Gold] MCP is an interoperability standard, not a performance upgrade.

## Speaker notes

Having introduced both function calling and MCP, let's honestly ask the question that comes up for an engineer right away: do I actually need MCP, or is it simpler to just hit the API directly? Let's start with the basics, because there's a common misconception here — "MCP replaces REST." That's wrong. REST and gRPC are the transport layer that actually does the work: it hits the database, calls the service. MCP is a thin standard layer on top, which lets an agent discover the available tools at runtime through a `tools/list` request and call them. In the overwhelming majority of real deployments, an MCP server wraps an already-existing REST API rather than replacing it. So the question isn't "MCP or API" — those aren't alternatives at the same level — it's "do I need a discovery-and-portability layer on top of the API, or is a hard-coded function call enough?"

The headline argument for MCP is integration arithmetic. Before MCP, to connect N applications with M tools, in the worst case you need N times M separate integrations. MCP makes it so each side implements the protocol once: the application becomes a client, the tool becomes a server, and all you need is N plus M implementations. But that also shows the threshold: the payoff only materializes once both N and M are at least two or three. For one application and one or two known tools, N times M equals two and N plus M equals three — so a direct function call is simpler. Below the threshold, MCP is pure overhead. What else the MCP layer gives you: dynamic discovery, when the catalog changes often; stateful sessions; portability across model vendors.

The flip side is the cost of the layer, and it isn't zero, which is why the decision goes by the table. An updated scan of all roughly 10,700 registry servers found that about a quarter of registry servers[2] are unusable, and the authors explicitly call this a floor, not a ceiling: part of it sits behind an auth wall and couldn't even be tested. Even among the ones that work, real-world success is low: on the MCP-Universe benchmark, the top-tested model scored forty-three point seven[1] percent successful tasks — meaning even the top result fails more than half of real MCP tasks. And security hasn't been settled either: the specific audit numbers (command injection, path traversal) we covered on the slide about MCP and the trust pivot — here it's enough to keep in mind that this is a separate trust boundary, not a solved question.

The one-line rule: MCP is an interoperability standard, not a performance upgrade. It pays off as a fleet and an ecosystem — many agents, many tools, reuse, switching vendors. For a single agent with a single tool, a plain function call is simpler, faster, and safer — and skipping MCP here is the correct engineering judgment, not a cut corner. This is exactly the ladder rule, applied to the connection layer.

Sources:
[1] MCP-Universe (arXiv:2508.14704) — top result 43.7% — the top model on real MCP servers scores 43.7% of tasks; >56% of real tasks fail. https://arxiv.org/abs/2508.14704 [VFY-day-of]
[2] DEV/theopslog audit 2026 — ~25% of registry servers unusable — ≈25% of registry servers are unusable (a floor, not a ceiling); injection 43% / path traversal 82%. [VFY: canonical URL not confirmed, present as data from an independent live-eval registry, not as a primary source]

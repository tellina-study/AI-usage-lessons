---
id: s-rag-research
type: assertion_visual
section: "Section 2. RAG"
assertion: "Deep research is RAG plus an agentic loop plus citation verification, not a «big prompt»; the typical failure is fabricating 3–13% of citations"
learning_goal: "Deep research as RAG case E (owner #2, relocated from §1): reasoning LLM + agentic RAG loop + citation-verify"
learning_outcomes: [LO7, LO4]
chapter_ref: "§2.12 [for-slide-rag-case-deepresearch] · §1.10 [for-slide-task-boundary]"
interaction: none
---

# Visible content

## Title bar
«Deep research is RAG + a loop, not a big prompt»

## Body
[Why this case belongs here]
The defining component is retrieval and orchestration, not prompt phrasing → this is a RAG case, not a prompting task. Like OpenAI Deep Research, Perplexity, Claude Research.

[Architectural pattern]
Reasoning LLM + agentic RAG loop: plan sub-questions → (search → read → refine the reasoning) × N → synthesize → verify citations. Reasoning steers the search, findings refine the reasoning — a closed loop.

[Gold callout — failure]
Citation fabrication: 3–13% of URLs are fabricated; counterintuitively, deep research is worse than plain search — 10.7% versus 4.8% per query. A number with no baseline is a red flag.

## Speaker notes

Here's an important reorganization from the course owner's feedback: we moved deep research out of the prompting section and into RAG. Why — deep research is often mistakenly filed under prompting tasks: «write one big prompt and it'll assemble the report.» That's wrong. The defining component here is retrieval and orchestration, not prompt phrasing — the prompt is just one detail in it. So this is a RAG case, and it belongs in the RAG section.

The setup: one complex question — «compare the market across five dimensions, with sources» — and the system plans its own sub-questions, searches many times, reads sources, and synthesizes a report with citations. The architectural pattern is a reasoning model plus an agentic RAG loop[1]: reasoning steers the search, new findings refine the reasoning, and it's a closed loop, unlike the static «retrieve top-k, then generate». The generalized schema for the slide: plan sub-questions, then several iterations of «search, read, refine the reasoning», then synthesis and a separate citation-verification step. OpenAI Deep Research runs one powerful reasoning model through a plan-search-backtrack-synthesize loop; Perplexity does real-time web RAG with source annotation. I'm naming products to illustrate the class, not as a recommendation.

The boundary of this class matters for judgment: deep-research agents fabricate citations. Measurements put it at three to thirteen percent of fabricated URLs. And a counterintuitive fact: a deep-research agent hallucinates citations worse than plain search with augmentation[2] — ten point seven percent versus four point eight percent. The baseline for comparison is the share of fake citations per query; the agent does worse precisely because it generates far more links. The fix is a separate verification layer after synthesis: check that every URL resolves and that the cited text actually supports the claim — exactly as in the legal case.

Against a human analyst, deep research is faster and cheaper, but without a verification layer, three to thirteen percent of the citations are false, and in a high-stakes report that's more expensive than a slower human. A direct tie-in to the course rule about baselines: deep research loves producing numbers with no baseline — «minus fifty percent», «five million acres» — and propping them up with a plausible but nonexistent link. The takeaway that closes this section: recheck any number from AI research against a resolving primary source, and treat a number with no baseline as a red flag, not a fact.

Sources:
[1] Anthropic — Multi-Agent Research System (agentic RAG loop) — reasoning LLM + agentic loop: reasoning steers the search, findings refine the reasoning. https://www.anthropic.com/engineering/multi-agent-research-system
[2] arXiv:2604.03173 — citation fabrication in retrieval-augmented systems (3–13%) — 3–13% of URLs are fabricated; deep research is worse than plain search, 10.7% vs 4.8% per query. https://arxiv.org/abs/2604.03173 [VFY-day-of]

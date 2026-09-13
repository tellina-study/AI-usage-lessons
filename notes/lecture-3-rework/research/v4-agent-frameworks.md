# V4 Research Brief: 2026 Agent Frameworks & the Workflow-vs-Agent Distinction

> Research for Lecture 3 (AI system architectures). Audience already builds with LLMs.
> Focus: judgment — when NOT to reach for agents. Skeptical, concrete, sourced.
> `[VFY-day-of]` = fast-moving version/number; re-verify before delivery.
> Compiled 2026-09-13.

---

## TL;DR (teach this framing)

- **Most "agent" problems are workflow problems.** Anthropic's own guidance: start with direct LLM API calls, graduate to workflows, and reach for a true agent only when the task genuinely needs dynamic, open-ended control flow.
- **Reliability compounds multiplicatively.** A step that is 95% reliable run 10× in sequence = ~60% end-to-end; 20× = ~36%. This `p^n` decay is the core engineering reason to minimize steps and autonomy.
- **Multi-agent buys performance by burning tokens, not by being clever.** Anthropic: multi-agent beat single-agent by 90.2% on research — but token usage explained ~80% of the variance, at ~15× the tokens of chat. If the task isn't embarrassingly parallel and quality-over-cost, it's the wrong tool.
- **Frameworks are an abstraction tax.** They obscure prompts/context, add token overhead, and can be replaced by "a few lines of code" for most patterns.

---

## 1. Framework Overview (2026 state)

For each: core abstraction · best-suited-for · maturity/adoption signal · one honest limitation.

### LangGraph (LangChain)
- **Core abstraction:** explicit **stateful graph** — nodes + edges + shared state, with durable execution and checkpointing. Lowest-level, most controllable of the mainstream frameworks. In 2026 added "Deep Agents" — a higher-level planning/subagent layer on top of the graph runtime (claimed ~65% reduction in input tokens on default-agent turns `[VFY-day-of]`).
- **Best for:** production apps needing precise control flow, persisted state, human-in-the-loop, and observability (LangSmith).
- **Maturity/adoption:** production workhorse. ~36.8k GitHub stars, ~34.5M monthly downloads `[VFY-day-of]`; Gartner attributed ~34% of agent-framework citations in production architecture docs at 1,000+ employee companies to LangGraph in Q1 2026 `[VFY-day-of]`.
- **Honest limitation:** steepest learning curve; you hand-build the graph. For a single tool-calling loop it is over-engineering.

### CrewAI
- **Core abstraction:** **role-based crews** — declare agents with roles/goals/backstories, assign tasks, they collaborate (sequential or hierarchical). Also a lower-level "Flows" API.
- **Best for:** fast multi-agent prototypes, role-decomposable workflows, teams that want something running in ~30 minutes.
- **Maturity/adoption:** large community — ~44.6k–55.2k stars `[VFY-day-of]`, claims 450M+ agentic workflows/month `[VFY-day-of]`, enterprise features (FedRAMP High, VPC, SSO). v1.x with native MCP + A2A.
- **Honest limitation:** the role-play abstraction can mask what's actually happening (which prompt, which context); multi-agent collaboration inherits the fragility in §3. Easy to spin up more agents than the task needs.

### AutoGen / AG2
- **Core abstraction:** **conversation between agents** — event-driven message passing, group chat, conversational orchestration.
- **Best for:** research/experimentation with conversational multi-agent patterns; AG2 for those wanting the original conversational model under independent (Apache 2.0) governance.
- **Maturity/adoption:** **AutoGen entered maintenance mode**; Microsoft merged AutoGen + Semantic Kernel into **Microsoft Agent Framework 1.0** (GA ~April 2026 `[VFY-day-of]`: YAML agent defs, graph workflows + checkpointing, native MCP + A2A). Community fork **AG2** continues active dev.
- **Honest limitation:** fragmentation/rename churn (AutoGen → AG2 / MS Agent Framework) is a real adoption risk; free-form agent conversation is hard to make reliable/debuggable in production.

### OpenAI Agents SDK (formerly Swarm)
- **Core abstraction:** **handoffs** — agents explicitly transfer control to each other carrying context; plus Tools, Guardrails (in/out validation), Sessions, Tracing. Deliberately thin: "5 clean primitives and gets out of the way."
- **Best for:** production agents on OpenAI models needing lightweight multi-agent handoff + tracing without a heavy framework.
- **Maturity/adoption:** GA-stable in early 2026 `[VFY-day-of]` (superseded experimental Swarm — Swarm is now reference-only, unmaintained). First-party OpenAI support.
- **Honest limitation:** OpenAI-centric; thin by design means less batteries-included (bring your own persistence, memory, RAG).

### Claude Agent SDK (formerly Claude Code SDK)
- **Core abstraction:** the **same agent loop that powers Claude Code**, callable as a library — built-in file ops, shell, web search, MCP; **subagents with context isolation**, lifecycle hooks, Skills, session-spanning context management. TS SDK adds a **Workflow tool** (orchestration runs as JS outside the conversation).
- **Best for:** coding/computer-use agents and long-running tasks where you want Anthropic's harness (context management, subagents) rather than rolling your own.
- **Maturity/adoption:** renamed late 2025 to signal general-purpose runtime. Python ~v0.1.48 (PyPI), TS ~v0.2.71 (npm) as of early 2026 `[VFY-day-of]`; concurrent subagents capped (e.g. 20 in 0.3.x builds) `[VFY-day-of]`.
- **Honest limitation:** Anthropic-model-centric; heavier harness (large system-prompt/context overhead — see §4 token cost) than a bare API call.

### smolagents (Hugging Face)
- **Core abstraction:** **code agents** — the agent writes and executes Python instead of emitting JSON tool calls. ~1,000 lines of core code; minimal abstraction, no built-in memory/RAG/graph.
- **Best for:** minimalist, code-execution agents; teams who want to read the whole framework in an afternoon.
- **Maturity/adoption:** HF-backed, growing. Claim: code-agents reduce steps/LLM calls by ~30% and improve on complex benchmarks vs JSON tool-calling `[VFY-day-of]`.
- **Honest limitation:** executing model-written code is a **security surface** (needs sandboxing); intentionally lacks the production scaffolding (persistence, HITL) bigger frameworks provide.

### LlamaIndex agents
- **Core abstraction:** **event-driven Workflows** + agents layered on a best-in-class **RAG/data** stack; "Agentic Document Workflows" for doc automation.
- **Best for:** the agent is a **knowledge worker over your data** — retrieval-heavy, document-centric pipelines.
- **Maturity/adoption:** mature data/RAG lineage (GPT Index, 2022); event-driven Workflows are the current orchestration model `[VFY-day-of]`.
- **Honest limitation:** its center of gravity is retrieval, not general agent orchestration — for non-RAG agents you're paying for machinery you don't use.

### Pydantic AI
- **Core abstraction:** **type-safe agent loop** — structured/validated I/O via Pydantic, dependency injection, tool calling, FastAPI-style DX; supports multi-agent.
- **Best for:** teams that want type contracts and validated outputs; faster debugging of production incidents via explicit schemas.
- **Maturity/adoption:** fastest-adopted in the Python ecosystem lately — ~16.5k stars, 2k+ forks (April 2026) `[VFY-day-of]`; multiple teams running thousands of daily interactions in prod.
- **Honest limitation:** younger than LangGraph/LlamaIndex; the type-safety focus is orthogonal to orchestration — for complex control flow you still assemble it yourself.

### When to pick each — or pick NONE (plain code)
| Situation | Pick |
|---|---|
| Precise control flow, persisted state, HITL, observability | **LangGraph** |
| Fast role-decomposed multi-agent prototype | **CrewAI** |
| Lightweight handoffs + tracing on OpenAI | **OpenAI Agents SDK** |
| Coding / computer-use / long tasks on Claude | **Claude Agent SDK** |
| Minimal code-execution agent, readable framework | **smolagents** |
| Agent over your documents/data (RAG-first) | **LlamaIndex** |
| Type-safe, validated outputs | **Pydantic AI** |
| Conversational multi-agent research/experiments | **AG2 / MS Agent Framework** |
| **Deterministic steps, ≤ a few LLM calls, no dynamic branching** | **NONE — plain code + direct API calls** |

**Anthropic's explicit guidance:** "many patterns can be implemented in a few lines of code" using LLM APIs directly; frameworks "often create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug." Only add framework complexity when it demonstrably improves outcomes.
Source: <https://www.anthropic.com/engineering/building-effective-agents>

---

## 2. Workflow vs Agent (Anthropic "Building Effective Agents" taxonomy)

**The precise distinction:**
- **Workflow** = "systems where LLMs and tools are orchestrated through **predefined code paths**." *You* write the control flow; the LLM fills in steps.
- **Agent** = "systems where LLMs **dynamically direct their own processes and tool usage**, maintaining control over how they accomplish tasks." The model decides the number and order of steps.

Source (primary): <https://www.anthropic.com/engineering/building-effective-agents>

### The 5 workflow patterns (what / when)
1. **Prompt chaining** — decompose into sequential steps, each LLM call processes the previous output. *When:* task cleanly splits into fixed subtasks; you'll trade latency for accuracy (can add gate checks between steps).
2. **Routing** — classify the input, then dispatch to a specialized follow-up. *When:* distinct input categories are better handled separately (e.g. easy → cheap model, hard → strong model).
3. **Parallelization** — run LLM calls simultaneously. Two flavors: **sectioning** (split into independent subtasks) and **voting** (run the same task N times, aggregate). *When:* subtasks are independent (speed) or you want confidence/diversity (voting).
4. **Orchestrator-workers** — a central LLM dynamically decomposes the task and delegates to worker LLMs, then synthesizes. *When:* subtasks can't be predicted up front (unlike static sectioning). This is the pattern behind Anthropic's Research feature.
5. **Evaluator-optimizer** — one LLM generates, another evaluates and gives feedback in a loop. *When:* you have clear eval criteria AND iterative refinement measurably helps (e.g. literary translation, complex search).

### When a TRUE agent is warranted
Open-ended problems where you "can't predict the required number of steps" and can't hardcode the path — the model must plan, act, observe, self-correct. Accept the trade: higher cost and **compounding error** (§3). Anthropic's rule of thumb: agents are for **flexibility + model-driven decision-making at scale**; workflows for **predictability + consistency** on well-defined tasks.

### When multi-agent / multi-agent orchestration IS vs ISN'T worth it
- **Worth it:** breadth-first, embarrassingly-parallel tasks where subagents explore independent directions with separate context windows, and **quality is worth ~15× the token cost**. Anthropic's example: "identify all board members of IT S&P 500 companies" — decomposes cleanly across subagents; the single agent bogs down in slow sequential search.
- **NOT worth it:** tasks requiring **shared, evolving context** and tightly-coupled decisions (e.g. most coding tasks), or where cost matters. Here parallel subagents make **conflicting implicit decisions** and the system gets *more* fragile, not more capable (§3).

---

## 3. Multi-Agent Reliability — the `p^n` compounding argument

**The math.** End-to-end success of `n` sequential steps each with reliability `p` ≈ `p^n`:
| per-step p | n=5 | n=10 | n=20 |
|---|---|---|---|
| 0.95 | ~77% | ~60% | ~36% |
| 0.99 | ~95% | ~90% | ~82% |

- 0.95^10 ≈ 59.9%; 0.95^20 ≈ 36%; even a (fictional) 0.99-per-step agent fails ~18% of 20-step tasks.
- **Worse than the clean math:** errors are correlated — agents **self-condition on their own earlier mistakes**, so errors *accelerate*, making `p^n` an optimistic upper bound.
- Sources: <https://tianpan.co/blog/2026/04/20/compound-accuracy-multi-step-agent-pipelines> · <https://www.mindstudio.ai/blog/multi-agent-reliability-compounding-problem-77-percent> · <https://prefactor.tech/blog/step-level-accuracy-compounding-failures-production>

**Real reliability data — τ-bench (Sierra).** The `pass^k` metric = probability an agent solves the SAME task on ALL k tries (reliability, not luck):
- GPT-4o: **61% pass@1 → 25% pass@8** on retail agent tasks. A ">half the time" agent succeeds every-time-out-of-8 only a quarter of the time. This is the reliability collapse the `p^n` argument predicts, measured on a real tool-agent-user benchmark.
- τ-bench → τ²-bench (June 2025, dual control) → τ³-bench (Feb 2026, audited tasks) `[VFY-day-of]`.
- Sources: <https://arxiv.org/abs/2406.12045> · <https://github.com/sierra-research/tau2-bench> · <https://qaskills.sh/blog/tau-bench-agent-evaluation-guide-2026>

**The two opposing 2025 primary sources (great teaching contrast — published within ~24h):**

- **Cognition, "Don't Build Multi-Agents" (Walden Yan, June 12 2025).** Argues multi-agent is fragile *by construction*. Two failure modes, illustrated with the **Flappy Bird example**: parallel subagents with no shared context built a Super-Mario-style background + a mismatched bird → "a bird and background with completely different visual styles."
  - Principle 1: "Share context, and share full agent traces, not just individual messages."
  - Principle 2: "Actions carry implicit decisions, and conflicting decisions carry bad results."
  - Recommendation: **single-threaded linear agent** by default (continuous context); for long tasks add an LLM **summarization/compression layer**, not more agents. "Running multiple agents in collaboration only results in fragile systems" (as of 2025).
  - Source: <https://cognition.com/blog/dont-build-multi-agents>

- **Anthropic, "How we built our multi-agent research system" (June 13 2025).** The pro-multi-agent case — but note *why* it works:
  - Multi-agent (Opus 4 orchestrator + Sonnet 4 subagents) **beat single-agent Opus 4 by 90.2%** on the internal research eval.
  - **Token usage explained ~80% of the performance variance** — i.e. it wins largely because it *spends more tokens*, not because coordination is magic.
  - Cost: **~15× the tokens of a normal chat** (single agents ~4× chat). Reserved for high-value, quality-over-cost tasks.
  - Architecture: orchestrator plans → spins up 3–5 parallel subagents (separate context windows) → separate citation pass.
  - Sources: <https://www.anthropic.com/engineering/multi-agent-research-system> (see also <https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent>, <https://www.zenml.io/llmops-database/building-production-multi-agent-research-systems-with-claude>)

**Synthesis the field reached by 2026:** a single orchestrator owns continuous context and spawns **ephemeral, read-only subagents** that return **compressed summaries** — i.e. keep Cognition's shared-context discipline, use Anthropic's parallelism only for read-only breadth-first fan-out.

---

## 4. Anti-Hype — when NOT to use an agent / framework

**Cost multipliers (with baselines):**
- **Baseline = 1×** a normal chat completion. **Single agent ≈ 4× tokens. Multi-agent ≈ 15× tokens** (Anthropic).
- Agentic workloads broadly: **5–30× token volume** vs chat (Spheron). Loop-based: 5-step loop ≈ 3.2× baseline, 50 steps > 30×, 200 steps > 100×.
- Microsoft + Stanford Digital Economy Lab: some agentic tasks consume **~1,000× more tokens** than a standard chat interaction `[VFY-day-of]`.
- Some sources cite up to **50× more tokens than chats** for agentic products (LeanOps) `[VFY-day-of]`.
- Sources: <https://www.spheron.network/blog/agentic-ai-inference-cost-2026/> · <https://leanopstech.com/blog/agentic-ai-cost-runaway-token-budget-2026/> · <https://spendark.com/blog/ai-agent-token-costs/>

**Framework overhead is real and measurable:**
- **Claude Code sends ~33,000 tokens** of system-prompt/context overhead *before* your prompt is even read; OpenCode ~7,000 for the same task — a **~4.7× overhead gap** between tools for identical work.
- Source: <https://prefactor.tech/blog/measuring-what-agents-actually-cost-hidden-token-overhead-and-efficien>

**Cost scaling can invert the unit economics (concrete failure):**
- A fintech fraud-detection agent: **$5,000/mo at 50 users (Nov 2025) → $15,000/mo at 500 users (Jan 2026)**; unit economics inverted somewhere between **700–1,000 concurrent users**, killing the project. Cost/user *climbs* with scale (concurrency → retries, longer contexts, more tool calls), the opposite of normal SaaS.
- **Gartner: >40% of agentic-AI projects will be cancelled by end of 2027** due to escalating costs `[VFY-day-of]`.
- Sources: <https://www.spheron.network/blog/agentic-ai-inference-cost-2026/> · <https://optimumpartners.com/insight/ai-token-costs-and-how-they-might-wreck-your-budget/>

**Fragility, not just cost:** frameworks "obscure the underlying prompts and responses, making them harder to debug" (Anthropic); multi-agent adds conflicting-decision failure modes (Cognition, §3). Abstraction churn is itself a risk — AutoGen → AG2 / MS Agent Framework, Swarm → OpenAI Agents SDK, Claude Code SDK → Claude Agent SDK all happened in ~12 months.

**Decision rule to teach:**
> Deterministic path + known steps + cost-sensitive → **plain code / workflow, no agent, no framework.**
> Dynamic path + unpredictable steps + quality-over-cost → **agent** (and only then, maybe a framework).
> Multi-agent → **only** for read-only breadth-first fan-out where you'll pay ~15× and can keep shared context. Otherwise a single-threaded agent (Cognition) or an orchestrator-workers *workflow* (Anthropic §2) is more reliable and cheaper.

---

## Primary sources (highest-value)
- Anthropic, *Building Effective Agents* — <https://www.anthropic.com/engineering/building-effective-agents>
- Anthropic, *How we built our multi-agent research system* — <https://www.anthropic.com/engineering/multi-agent-research-system>
- Cognition, *Don't Build Multi-Agents* — <https://cognition.com/blog/dont-build-multi-agents>
- Sierra τ-bench — <https://arxiv.org/abs/2406.12045> · <https://github.com/sierra-research/tau2-bench>

*Secondary/aggregator URLs inline above carry the version numbers and adoption stats flagged `[VFY-day-of]` — re-verify those live before the lecture, as they move week to week.*

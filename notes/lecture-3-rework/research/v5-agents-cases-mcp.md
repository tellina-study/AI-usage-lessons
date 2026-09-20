---
title: "Lecture 3 v5 — Agents research: MCP vs API, framework cons, agent cases, workflow-vs-agent-vs-multi-agent"
lecture: lec-03
purpose: research feed for owner's four v5 requests (MCP-vs-API slide; slide 48 framework cons; typical agent cases; slide 49 workflow/agent/multi-agent deeper logic, meme removed)
date: 2026-09-15
status: research-draft
volatility_note: "AI-agent landscape churns monthly. All model names, benchmark leaderboard numbers, and product statuses marked [VFY-day-of] must be re-checked at lecture delivery."
---

# Research v5 — Agents, cases, MCP

Four owner requests, one file. Each section is slide-ready: crisp claims, baselines inline, sources cited, volatile facts flagged `[VFY-day-of]`.

Cross-cutting framing for the whole lecture (owner memory `lecture-section-classic-base-first`): each topic goes **classic base first → what AI/agents add → limits & when NOT → on-point failure**. The four sections below already follow that shape.

---

## 1. MCP vs API — dedicated slide (pros / cons / when-which)

### 1.1 The one-sentence frame (classic base first)

MCP does **not** replace REST/gRPC. REST is the transport layer that actually does the work; **MCP is a thin standard layer on top that lets an LLM agent *discover* and *call* those tools at runtime**. In almost every real deployment an MCP server *wraps* an existing REST API. So the real question is never "MCP or API" — it's "do I need the discovery/portability layer, or is a hardcoded function-call enough?" ([futureagi](https://futureagi.com/blog/api-vs-mcp-difference-2025/), [Loginsoft](https://www.loginsoft.com/post/mcp-vs-api-whats-the-actual-difference-and-when-to-use-each))

### 1.2 What MCP actually adds (the "N×M → N+M" argument)

- **Integration math.** Before MCP, wiring N AI apps to M tools/data sources needed up to **N×M** custom integrations. MCP makes each side implement the protocol once → **N+M**. This is the load-bearing argument for MCP's existence. ([Medium/Amanatullah](https://medium.com/@amanatulla1606/anthropics-model-context-protocol-mcp-a-deep-dive-for-developers-1d3db39c9fdc))
  - *Baseline for the slide:* the win only materializes at scale. For N=1 app + M=2 tools, N×M=2 vs N+M=3 — direct function-calling is *fewer* pieces. The crossover is roughly when N×M > N+M, i.e. both N and M ≥ 2–3. Below that, MCP is net overhead.
- **Dynamic discovery.** Client calls `tools/list` at runtime and gets the current catalog + JSON schemas; a server can add a tool with **zero client change**. A REST-wired agent has to be told, at build time, which of its 20 endpoints to call. ([futureagi](https://futureagi.com/blog/api-vs-mcp-difference-2025/))
- **Stateful sessions.** MCP connection persists; server can push notifications; host accumulates context. REST is stateless per request. ([futureagi](https://futureagi.com/blog/api-vs-mcp-difference-2025/))
- **Portability / no vendor lock.** A standard tool protocol decouples the agent host from the model vendor — swap Claude↔GPT↔Gemini without rewriting integrations. ([EnhanceLearning.AI](https://enhancelearning.ai/articles/mcp-and-agent-portability-across-model-providers))
- **Ecosystem scale (context).** By Q2 2026, ~**9,400 published MCP servers** across the four major registries, **~1,300 production-ready** `[VFY-day-of]`. ([Requesty](https://www.requesty.ai/blog/agentic-coding-tools-compared-2026-claude-code-cursor-codex-aider))

### 1.3 Cons of MCP (the honest half — this is the ≥30% judgment content)

**Quality / maturity — the numbers the owner wants:**
- **~10% of servers in the official registry are outright broken** ("about 1 in 10", explicitly called *the floor, not the ceiling* — auth-walled servers couldn't even be tested). This is the real-world reframing of the owner's "~11% actually-runnable" note: the honest published figure is **~10% broken (floor)**, not "only 11% run". Use the broken-floor framing on the slide — it's the defensible number. ([DEV/theopslog audit](https://dev.to/theopslog/i-checked-every-mcp-server-in-the-official-registry-about-1-in-10-is-broken-1ehj)) `[VFY-day-of]`
- Even when servers *run*, **task success is low**: on **MCP-Universe** (real servers, 6 domains) the best model **GPT-5 = 43.7%**, Grok-4 = 33.3%, Claude-4.0-Sonnet = 29.4%. Best model still fails **>56%** of real MCP tasks. Baseline framing: "can call the tool" ≠ "completes the task". ([MCP-Universe arXiv 2508.14704](https://arxiv.org/html/2508.14704))
- Schema compliance is shaky too: audit of 50,000 manifests found **543 (~1.1%)** violate the registry's own schema. ([DEV/baobabcat](https://dev.to/baobabcat/i-scanned-50000-mcp-server-manifests-543-violate-the-registrys-own-schema-heres-the-data-d63))

**Security surface (large, teachable):**
- **Command injection in 43%** of tested servers (Equixly offensive-security assessment). ([Data Science Dojo](https://datasciencedojo.com/blog/mcp-security-risks-and-challenges/), [Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/))
- **Path traversal in 82%** of implementations (across 2,614 servers); **SSRF in 36.7%** of 7,000+ servers (BlueRock). ([Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/))
- **33% of 1,000 scanned servers had critical vulns** (Enkrypt AI, Oct 2025). ([Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/))
- **Auth is weak:** 88% require credentials but **53% use long-lived static secrets** (API keys / PATs); OAuth only **8.5%**. ([Astrix](https://astrix.security/learn/blog/state-of-mcp-server-security-2025/))
- **Real breach:** CVE-2025-6514 (OAuth-related) compromised **~437,000 developer environments**. ([Practical DevSecOps](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/)) `[VFY-day-of]`

**Overhead:** extra protocol layer + long tool catalogs eat context tokens as interaction steps grow (MCP-Universe explicitly flags the long-context blowup). For a single known tool, that's pure tax. ([MCP-Universe](https://arxiv.org/html/2508.14704))

### 1.4 Decision table (slide-ready)

| Use **MCP** when… | Use **direct API / function-calling** when… |
|---|---|
| Many agents × many tools (N×M explosion), N,M ≥ 2–3 | One app, one or two known tools (N+M ≥ N×M) |
| You want runtime **tool discovery** (catalog changes often) | Tool set is fixed and known at build time |
| You need **portability** across model vendors / hosts | You're committed to one model, one stack |
| Third parties / other teams will reuse the same servers | Integration is private, single-consumer, never shared |
| Conversational, stateful, multi-step tool use | Single stateless request/response |
| You can afford a **security review** of each server | You need a small, auditable, locked-down surface *now* |

**Rule of thumb for the slide:** MCP is an *interoperability standard*, not a performance upgrade. It pays off as a **fleet/ecosystem** play. For one agent + one tool, a plain function-call is simpler, faster, and has a smaller attack surface — and skipping MCP there is the *correct* judgment call, not a shortcut.

---

## 2. Agent framework cons — slide 48 additions

Landscape in scope: LangGraph, CrewAI, AutoGen (AG2), OpenAI Agents SDK, Claude Agent SDK, smolagents, LlamaIndex, Pydantic AI.

### 2.1 Anthropic's own guidance (the anchor claim)

Anthropic ("Building Effective Agents"): **start by using LLM APIs directly — many patterns are a few lines of code.** Frameworks "create extra layers of abstraction that can obscure the underlying prompts and responses, making them harder to debug, and can make it tempting to add complexity when a simpler setup would suffice." This is the headline for slide 48. ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents))

### 2.2 The five shared downsides (all frameworks, sourced)

1. **Behavior-customization limits.** High-abstraction frameworks (CrewAI especially) accumulate tech debt fast the moment you need to go **beyond the happy path** — override a built-in prompt, change control flow. "If your team has shipped LLM features before, the abstraction tax of CrewAI rarely pays off." ([tensoria benchmark](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))
2. **Transparency / debuggability ("abstraction tax").** Frameworks **hide the actual prompts and control flow**. Debugging a stuck agent in a multi-step crew is painful; "when you need to debug a failure in a five-agent pipeline, the abstraction becomes opaque." Anthropic's point restated. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison), [Anthropic](https://www.anthropic.com/engineering/building-effective-agents))
3. **Lock-in.** Provider SDKs bind you to one model ecosystem: **OpenAI Agents SDK is model-locked to OpenAI (no BYOM)**; Claude Agent SDK / Google ADK similarly favor their own stack. Portability costs a rewrite. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison), [morphllm](https://www.morphllm.com/ai-agent-framework))
4. **Version churn / instability.** "The LangChain ecosystem has had **too many API-breaking changes** over its lifetime, which erodes trust." Framework upgrades break working code. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))
5. **Performance / token overhead.** Measured: a 3-agent CrewAI crew used **~18% more tokens** than an equivalent LangGraph build (2026 benchmark). Abstraction isn't free at runtime either. Baseline: 18% *over* a hand-rolled/lighter-framework implementation of the *same* task. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))

### 2.3 Per-framework quick-notes (for speaker backup, not the slide)

- **LangGraph:** most control + best state inspection (LangSmith), but **state schema must be designed upfront** — one team refactored the schema 3× as requirements changed. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))
- **CrewAI:** highest abstraction → fastest to start, worst to debug/customize; +18% tokens. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))
- **OpenAI Agents SDK:** model-locked, no built-in checkpointing for long runs, coarse error handling. ([tensoria](https://tensoria.fr/en/blog/multi-agent-orchestration-comparison))
- **smolagents (HuggingFace):** minimalist, code-first, model-agnostic via LiteLLM, code-writing agents cut LLM calls ~30% — but positioned for **prototyping**, migrate to a robust framework for production. ([Langfuse](https://langfuse.com/blog/2025-03-19-ai-agent-comparison), [jangwook](https://jangwook.net/en/blog/en/python-ai-agent-library-comparison-2026/))
- **Pydantic AI:** type-safe, minimal abstraction; **but you often bolt on LangGraph/CrewAI for orchestration** — it's not a full orchestrator. ([morphllm](https://www.morphllm.com/ai-agent-framework))
- **LlamaIndex:** strong for RAG-centric agents; overkill outside retrieval. ([Langfuse](https://langfuse.com/blog/2025-03-19-ai-agent-comparison))

**Slide-48 takeaway line:** "A framework is a bet that its abstractions match your problem. When they don't, you pay the abstraction tax twice — once to fight it, once to debug through it. Anthropic's default: start with the raw API, adopt a framework only when it's *removing* real complexity, not adding it."

---

## 3. Typical agent CASES / tasks (owner: agents lack typical cases)

Six teachable, real, documented cases. For each: **task · loop shape · tools · where it breaks · would a workflow have been better?** (This last column is the judgment content.)

### Case A — Coding agent (Claude Code / Cursor / Aider) — *real*
- **Task:** implement/fix code across a repo from a natural-language ask.
- **Loop:** read repo → plan → edit files → run tests/shell → observe errors → iterate → open PR. Long-horizon, tool-heavy, self-correcting. ([Requesty](https://www.requesty.ai/blog/agentic-coding-tools-compared-2026-claude-code-cursor-codex-aider))
- **Tools:** filesystem read/write, shell/terminal, test runner, git, (MCP for extras).
- **Where it breaks:** large ambiguous refactors; silent wrong edits; runaway loops on flaky tests; context loss on huge repos. Cursor uses RAG-over-filesystem to fight context limits; Aider auto-commits so you can revert. ([Requesty](https://www.requesty.ai/blog/agentic-coding-tools-compared-2026-claude-code-cursor-codex-aider))
- **Workflow better?** No — genuine open-ended search over code *needs* agency. This is the canonical "agent earns its keep" case.

### Case B — Customer-support automation — *real, with documented failures*
- **Task:** answer customer questions, process refunds/returns/billing, escalate.
- **Loop:** classify intent → retrieve policy/order → decide (answer / act / escalate) → respond.
- **Tools:** knowledge base / RAG, order & billing APIs, refund action, escalation handoff.
- **Where it breaks — the teachable failures:**
  - **Air Canada:** support chatbot invented a 90-day bereavement-refund window (real policy 30 days). Tribunal held the airline liable — refund **plus** fees + interest. Policy hallucination became **binding, legally enforceable**. ([Respan](https://www.respan.ai/resources/support-ai-policy-hallucination))
  - **Klarna reversal:** publicly celebrated AI "replacing 700 agents" (2024), then **rebuilt human capacity through 2024–2025** because policy edge cases, escalation judgment, and trust needed humans back in the loop. ([Respan](https://www.respan.ai/resources/support-ai-policy-hallucination))
- **Workflow better?** Often **yes** for the risky slice. Refunds/policy answers want a **deterministic routing workflow with guardrails** (retrieve exact policy → template answer → hard-stop escalation on edge cases), not free agent generation. Air Canada is the poster child for "don't let a free-running agent speak policy."

### Case C — Data-pipeline / ETL agent — *real (emerging), mixed verdict*
- **Task:** ingest/transform data; adapt when a source schema or API changes.
- **Loop:** detect schema drift → analyze downstream impact → generate/patch transformation → validate → (guardrailed) apply. "Self-healing pipeline." ([Integrate.io](https://www.integrate.io/blog/agentic-ai-agents-rewriting-data-pipelines/), [Ampcome](https://www.ampcome.com/post/top-8-agentic-ai-use-cases-in-data-engineering))
- **Tools:** connectors (Fivetran/Airbyte/Matillion), schema catalog, transform engine, validation/tests.
- **Where it breaks:** silent bad transforms corrupt data at scale; non-determinism is dangerous in a pipeline you must *audit*; hard to reproduce.
- **Workflow better?** **Mostly yes.** The steady-state pipeline should stay **deterministic** (Fivetran-style). Reserve the *agent* for the narrow **schema-drift-repair** step (detect → propose → human/guardrail approve), then hand back to deterministic execution. Classic "agent for the adaptive edge, workflow for the trunk."

### Case D — Research agent (Deep Research: OpenAI / Gemini / Claude / Perplexity) — *real*
- **Task:** answer a broad question requiring many independent searches + synthesis.
- **Loop:** plan sub-questions → (fan-out) search → read/filter → synthesize → cite. Often orchestrator + parallel subagents. ([ByteByteGo](https://blog.bytebytego.com/p/how-openai-gemini-and-claude-use), [Anthropic multi-agent](https://www.anthropic.com/engineering/multi-agent-research-system))
- **Tools:** web search, page fetch/read, retrieval, citation pass.
- **Where it breaks:** cost blow-up (see §4 — ~15× tokens); shallow agency (follows search patterns, weak true reasoning); hallucinated citations.
- **Workflow better?** No for genuinely open breadth-first research (Anthropic's own justification for multi-agent here). Yes if the "research" is actually a fixed lookup — then it's a retrieval *workflow*, not an agent.

### Case E — Browser / computer-use agent (Operator / Claude Computer Use / Browser Use) — *real, brittle*
- **Task:** drive a real browser/desktop to complete a web task (book, fill forms, navigate).
- **Loop:** screenshot/DOM → plan next UI action → click/type → observe → repeat.
- **Tools:** browser automation, screen/DOM parsing, click/type primitives.
- **Where it breaks — the numbers:**
  - **OSWorld (desktop):** Operator **38.1%**; Claude Opus 4.7 **82.3%** on OSWorld-Verified `[VFY-day-of]` — even the best still fails **~1 in 5** desktop tasks. ([digitalapplied](https://www.digitalapplied.com/blog/computer-use-agents-2026-claude-openai-gemini-matrix), [coasty](https://coasty.ai/blog/ai-agent-platform-comparison-2026-fail-openai-operator))
  - **WebArena:** best single-agent **61.7%** (IBM CUGA, Feb 2025) vs **human 78%**. ([particula](https://particula.tech/blog/browser-use-vs-operator-vs-claude-computer-use-web-agents))
  - **Operator itself was deprecated** (shut down Aug 31, 2025) — a live "hype→retirement" lesson. ([Wikipedia/OpenAI Operator](https://en.wikipedia.org/wiki/OpenAI_Operator)) `[VFY-day-of]`
- **Workflow better?** For *any consequential action* (payments, submissions): **yes** — use a real API if one exists. Driving pixels is the fallback of last resort. "None reliable enough to run unattended on consequential actions." ([particula](https://particula.tech/blog/browser-use-vs-operator-vs-claude-computer-use-web-agents))

### Case F — SRE / ops incident agent — *real, low-autonomy*
- **Task:** triage/investigate a production incident, find root cause, suggest/apply fix.
- **Loop:** detect → gather telemetry (logs/metrics/traces) → hypothesize → check next dashboard → propose remediation → escalate. Read-only investigation is the sweet spot. ([Augment Code](https://www.augmentcode.com/guides/ai-sre-incident-management), [incident.io](https://incident.io/blog/ai-sre-agent-definition))
- **Tools:** observability APIs (APM/logs/traces), runbooks (RAG), GitHub MCP (trace error→code→PR), k8s.
- **Where it breaks — the number:** **ITBench (94 real IT scenarios): SOTA models autonomously resolve only 13.8% of SRE scenarios.** So today's real value is **narrowing the search space + automating investigation toil**, with humans on the judgment calls. ([Augment Code](https://www.augmentcode.com/guides/ai-sre-incident-management)) `[VFY-day-of]`
- **Workflow better?** For remediation itself: keep it **workflow + human approval** (typed tools, bounded actions). Agent for the *investigation* narrative, workflow-with-gates for the *action*.

**Cross-case pattern for the lecture:** the more consequential and auditable the action, the more you pull it back toward a **guarded workflow**; agency belongs in the *open-ended investigation / search* half, not the *irreversible action* half.

---

## 4. Workflow vs agent vs multi-agent — slide 49 expanded (meme removed, more studies)

### 4.1 Definitions (Anthropic, the base)

- **Workflow:** LLMs + tools orchestrated through **predefined code paths**. Predictable, consistent, cheaper, debuggable.
- **Agent:** LLM **dynamically directs its own process and tool use**. Flexible, but latency + cost + compounding error.
- **Anthropic's rule:** "**start simple, add agency only when flexibility outweighs latency, cost, and error compounding.**" Use the simplest thing that works; frameworks/agents only when they earn it. ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents), [Mervin Praison](https://mer.vin/2026/05/when-not-to-build-ai-agents-anthropics-workflow-vs-agent-playbook/))
- **Five workflow patterns** (know before reaching for an agent): Prompt Chaining, Routing, Parallelization, Orchestrator–Worker, Evaluator–Optimizer. ([Anthropic](https://www.anthropic.com/engineering/building-effective-agents))

### 4.2 The reliability math (this replaces the meme — it's rigorous and slide-worthy)

- **Sequential success compounds multiplicatively:** end-to-end = **p^n**.
  - 5 steps @ 95% → **77%**. 10 steps @ 95% → **~59%**. 20 steps → **~36%**. 100 steps → **99.4% failure**. ([MindStudio](https://www.mindstudio.ai/blog/multi-agent-reliability-compounding-problem-77-percent), [Zartis](https://www.zartis.com/the-compounding-errors-problem-why-multi-agent-systems-fail-and-the-architecture-that-fixes-it/))
- **Consistency (τ-bench pass^k):** pass^k = p^k. A model at **90% pass@1 → ~57% at k=8** — i.e. it solves a task on all 8 tries only 57% of the time. Reliability ≠ capability. ([τ-bench arXiv 2406.12045](https://arxiv.org/abs/2406.12045), [emergentmind](https://www.emergentmind.com/topics/tau-bench))
- **Architecture matters more than you'd think (2025, 180 controlled experiments, 4 benchmarks):** *independent/decentralized* multi-agent architectures **amplify errors 17.2×** vs single-agent baseline; **centralized** orchestration (one lead delegating) contains it to **4.4×**. So multi-agent isn't uniformly bad — *uncoordinated* multi-agent is. ([Towards a Science of AI Agent Reliability, arXiv 2602.16666](https://arxiv.org/html/2602.16666v2))

### 4.3 The two camps — put them head to head

**Cognition ("Don't Build Multi-Agents") — the skeptic:**
- Two principles: **(1) share as much context as possible across decisions; (2) don't split decision-making in ways that can conflict.**
- Naive parallel subagents each see only a slice → make individually-reasonable, collectively-incoherent implicit decisions (the "one builds a Mario background, the other builds a bird" example).
- Recommendation: **a single, linear agent in one continuous thread will get you surprisingly far in reliability.** ([Cognition](https://cognition.com/blog/dont-build-multi-agents))

**Anthropic (multi-agent research system) — the qualified proponent:**
- Their orchestrator + 3–5 parallel subagents **beat single-agent Opus 4 by 90.2%** on breadth-first research. ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system))
- **Cost:** agents ≈ **4× tokens** of chat; multi-agent ≈ **15× tokens** of chat. Token usage alone explains **80%** of performance variance. ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), [ZenML](https://www.zenml.io/llmops-database/building-production-multi-agent-research-systems-with-claude))
- **When it's worth 15×:** high-value, **breadth-first, parallelizable, read-mostly** work where total info exceeds one context window (due diligence, competitive intel, lit review). Consumer Q&A can't absorb the multiplier. ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system))
- **Reconciliation with Cognition:** Anthropic parallelizes **read/research** (independent, no shared writes needed); Cognition warns against parallelizing **decisions/writes** (need shared context). Both agree: **don't split conflicting decisions.** The multi-agent win is real for *fan-out reading*, not for *coordinated building*.

### 4.4 Cost multiplier — with baselines

| Mode | Token cost vs chat baseline | Cost risk |
|---|---|---|
| Single chat | 1× (baseline) | — |
| Single agent | ~4× | loops if unbounded |
| Multi-agent | ~15× | **compounds**: a recursive subagent or oversized tool result can add another **10×+**; Anthropic's published architecture has **no circuit breakers / per-run caps** |

([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system), [getnadir](https://getnadir.com/blog/multi-agent-orchestration-15x-token-cost/), [Augment Code](https://www.augmentcode.com/guides/multi-agent-cost-compounding))

### 4.5 Rigorous decision framework (replaces slide 49 meme)

Decide **top-down**, stop at the first "yes":

1. **Can a single prompt / RAG do it?** → do that. (No agent.)
2. **Is the path predictable?** → **Workflow** (chaining/routing/parallelization/orchestrator-worker/evaluator-optimizer). Predictable, cheap, debuggable.
3. **Does it need open-ended, model-driven decisions on a dynamic path?** → **Single agent.** Accept ~4× cost; bound the loop (max steps, cost cap).
4. **Only if** the work is **breadth-first + parallelizable + read-mostly** AND **task value > 15× token cost** AND you can keep decisions non-conflicting → **Multi-agent**, and prefer **centralized orchestration** (4.4× error) over decentralized (17.2× error).

**Guardrails baked into the frame (say these out loud):**
- More steps → multiply p^n; keep chains short, add validation/checkpoints.
- Never parallelize *conflicting decisions/writes*; parallelize independent *reads*.
- Multi-agent needs a **cost cap / circuit breaker** — the reference architecture ships without one.

**Slide-49 one-liner:** "Don't reach for multi-agent because it's impressive. Reach for a workflow by default, a single agent when the path is genuinely open, and multi-agent only when the task is worth 15× tokens, splits into independent reads, and never forces two agents to make conflicting decisions."

---

## Volatility / re-check list (`[VFY-day-of]`)
- MCP registry size (~9,400 servers / ~1,300 prod-ready) — churns.
- ~10% broken-server floor — audit is a snapshot.
- CVE-2025-6514 impact figure (~437k envs).
- MCP-Universe leaderboard (GPT-5 43.7% etc.) — models update.
- Computer-use scores (Operator 38.1%, Claude Opus 4.7 82.3% OSWorld) — model versions churn monthly.
- OpenAI Operator deprecation (shut Aug 31 2025) — confirm still-retired / successor product name.
- ITBench SRE 13.8% — new models may move this.
- Model names throughout (Opus 4.7, GPT-5, Grok-4) — verify current versions at delivery.

## Key sources
- Anthropic, *Building Effective Agents* — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic, *Multi-agent research system* — https://www.anthropic.com/engineering/multi-agent-research-system
- Cognition, *Don't Build Multi-Agents* — https://cognition.com/blog/dont-build-multi-agents
- MCP-Universe (arXiv 2508.14704) — https://arxiv.org/html/2508.14704
- τ-bench (arXiv 2406.12045) — https://arxiv.org/abs/2406.12045
- *Towards a Science of AI Agent Reliability* (arXiv 2602.16666) — https://arxiv.org/html/2602.16666v2
- MCP broken-server audit — https://dev.to/theopslog/i-checked-every-mcp-server-in-the-official-registry-about-1-in-10-is-broken-1ehj
- MCP security stats — https://www.practical-devsecops.com/mcp-security-statistics-2026-report/ ; https://astrix.security/learn/blog/state-of-mcp-server-security-2025/
- Framework benchmark/cons — https://tensoria.fr/en/blog/multi-agent-orchestration-comparison ; https://www.morphllm.com/ai-agent-framework
- Support failures (Air Canada / Klarna) — https://www.respan.ai/resources/support-ai-policy-hallucination
- Computer-use benchmarks — https://www.digitalapplied.com/blog/computer-use-agents-2026-claude-openai-gemini-matrix ; https://particula.tech/blog/browser-use-vs-operator-vs-claude-computer-use-web-agents
- SRE/ITBench — https://www.augmentcode.com/guides/ai-sre-incident-management
- ETL agents — https://www.integrate.io/blog/agentic-ai-agents-rewriting-data-pipelines/
- Cost multiplier — https://getnadir.com/blog/multi-agent-orchestration-15x-token-cost/
- MCP vs API — https://futureagi.com/blog/api-vs-mcp-difference-2025/ ; https://www.loginsoft.com/post/mcp-vs-api-whats-the-actual-difference-and-when-to-use-each

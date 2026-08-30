# Anthropic's approach to AI across the SDLC — the "Anthropic kit"

> Research map for Лекция 4 «AI в разработке ПО» (МГТУ ИУ6, 3rd year, RU, 2026).
> Pillar: **Anthropic's SDLC-AI approach**, mapped onto the common 9-phase SDLC decomposition.
> Access date for all sources: **2026-08-29**. Primary sources = anthropic.com / claude.com / code.claude.com docs.
> `[VFY-day-of]` = volatile product feature that may change before lecture day — re-verify.

---

## 0. One-paragraph frame

Anthropic does not sell a "phase-by-phase SDLC product." It ships **one agentic coding environment (Claude Code)** plus a small set of **composable primitives** — `CLAUDE.md`/skills (context), plan mode (planning), sub-agents (context isolation), hooks (deterministic gates), MCP (external actions), permissions/sandboxing (containment), non-interactive `-p` mode (CI/automation) — and a **methodology** ("AI-Native SDLC playbook") that arranges them into a git-loop: every SDLC stage commits a **versioned artifact** (`intent.md` → `spec.md` → plan → PR → incident record) that the next stage reads. Claude reportedly authors ~80% of merged code internally; **humans stay accountable at gates**, reviewing what the agent flagged rather than starting from scratch. The kit is strongest at the **coding, planning, review, and context/orchestration** layers; thinner (mostly "point Claude at your CLI/MCP") at architecture, CI/CD, and ops.

---

## 1. Summary table — SDLC phase → Anthropic practice/tool → source → volatile?

| SDLC phase | Anthropic practice / feature | One-line description | Primary source | Volatile? |
|---|---|---|---|---|
| **1. Requirements & planning** | **Plan mode** (`Shift+Tab` / `--permission-mode plan`) | Claude reads & proposes a plan; *cannot edit files until engineer accepts* — enforces explore-before-code | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 1. | **"Interview me" spec-driven flow** | Claude interviews you via `AskUserQuestion`, writes self-contained `SPEC.md`, fresh session executes it | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 1. | **`intent.md` (playbook Stage 1)** | Originator brainstorms with Claude → structured requirements committed to git; accept/reject = the merge | claude.com/blog/the-ai-native-sdlc-playbook | no |
| **2. Architecture & design** | **`spec.md` (playbook Stage 2)** | Requirements+design collapse into one session; Claude produces spec constrained by brand/security/compliance skills | claude.com/blog/the-ai-native-sdlc-playbook | no |
| 2. | **Workflows vs. agents decision** | Choose predefined workflow (chaining/routing/parallel/orchestrator-workers/evaluator-optimizer) vs. autonomous agent; start simple | anthropic.com/engineering/building-effective-agents | no |
| 2. | **"Ask codebase questions"** | Onboard/understand architecture by asking Claude senior-engineer questions over the repo | code.claude.com/docs/en/best-practices | no |
| **3. Implementation / coding** | **Claude Code agentic loop** | Explore → plan → implement → commit; Claude reads files, runs commands, iterates autonomously | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 3. | **"Give Claude a way to verify its work"** | Provide a test/build/screenshot check so the loop closes itself instead of you being the verification loop | code.claude.com/docs/en/best-practices | no |
| 3. | **Provide-specific-context prompting** | Scope task, point to source files (`@file`), reference existing patterns, describe symptom + fix criteria | code.claude.com/docs/en/best-practices | no |
| 3. | **Auto-accept / auto mode** | Classifier model reviews commands, blocks risky ones, lets routine work proceed unattended | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 3. | **Fan-out `/batch` + `claude -p` loops** | Split large migration across 5–30 sub-agents (own worktree + PR each) or loop `claude -p` over a file list | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| **4. Testing & QA** | **TDD-style verification prompts** | "write a failing test that reproduces the issue, then fix it"; supply example test cases in the prompt | code.claude.com/docs/en/best-practices | no |
| 4. | **`/goal` + Stop-hook gates** | Evaluator re-checks a condition each turn; Stop hook blocks turn-end until check script passes | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 4. | **Incidents → permanent regression tests** | Production incidents converted into regression tests; hook blocks edits to test files during a fix task | claude.com/blog/the-ai-native-sdlc-playbook | no |
| **5. Code review** | **Adversarial review sub-agent / `/code-review`** | Fresh-context reviewer sees only the diff + criteria (not the author's reasoning) and reports gaps | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 5. | **Writer/Reviewer two-session pattern** | Second Claude with clean context reviews the first's code — less biased toward code it just wrote | code.claude.com/docs/en/best-practices | no |
| 5. | **Shadow-mode AI reviewers** | New AI reviewers post comments for human approval "until trust is earned"; teams red-team them | claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle | no |
| **6. Security** | **`/security-review` command + PreToolUse hook** | Scans for attacker-controllable input / suspicious links pre-merge; hook = hard enforcement gate | claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle | [VFY-day-of] |
| 6. | **Single-purpose agent identities / least privilege** | Each agent gets minimum permissions; e.g. incident agent can post + read logs but **cannot deploy** | claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle | no |
| 6. | **Egress allowlisting + sandboxing** | Agents on remote VMs with allowlisted network egress; OS-level sandbox limits FS/network blast radius | claude.com/blog/how-anthropic-secures-...-sdlc ; code.claude.com/docs/en/sandboxing | no |
| 6. | **Agent-to-agent boundaries via monitored channels** | Inter-agent requests flow through Slack-like monitored channels; permission boundaries on access, not on instructions | claude.com/blog/how-anthropic-secures-...-sdlc | no |
| 6. | **Supply-chain / secrets scanning + SIEM logging** | Regular scans of deps/secrets/supply-chain/cloud/containers; every automated approval logged to SIEM | claude.com/blog/how-anthropic-secures-...-sdlc | no |
| **7. CI/CD, build, release/deploy** | **Non-interactive `claude -p` in CI / pre-commit** | Headless mode with JSON/stream-json output for pipelines; `--allowedTools` scopes unattended runs | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| 7. | **PR review + hooks as approval gates (Stage 5)** | Claude reviews PRs vs. policy & addresses comments; managed settings enforce sandbox; **prod gate is human** | claude.com/blog/the-ai-native-sdlc-playbook | no |
| 7. | **`gh`/`aws`/`gcloud` CLI + MCP delegation** | Anthropic's guidance = point Claude at existing CLI tools / MCP servers rather than a bespoke CD product | code.claude.com/docs/en/best-practices | no |
| **8. Ops, observability, incident, maintenance** | **Monitoring scripts invoke Claude on breach (Stage 6)** | Deterministic monitors call Claude when control bands breach; response tiers in version-controlled config | claude.com/blog/the-ai-native-sdlc-playbook | no |
| 8. | **Claude Tag incident response in channels** | Claude participates in comms channels for incident response; findings flow back as `intent.md`, restarting loop | claude.com/blog/the-ai-native-sdlc-playbook | [VFY-day-of] |
| 8. | **Real-world ops examples** | OCR of error screenshots, diagnosing k8s IP exhaustion, parsing Terraform plans (per team writeups) | anthropic.com (how-anthropic-teams-use-claude-code) | [VFY-day-of] |
| **9. Documentation & knowledge** | **`CLAUDE.md` as living project memory** | Persistent per-repo context (build/test cmds, style, conventions); checked into git, compounds over time | code.claude.com/docs/en/memory | no |
| 9. | **Skills (`.claude/skills/*/SKILL.md`)** | On-demand domain knowledge & reusable workflows loaded only when relevant (vs. always-on CLAUDE.md) | code.claude.com/docs/en/skills | [VFY-day-of] |
| 9. | **Ask-codebase onboarding** | Use Claude to explain logging, endpoints, edge cases — reduces ramp-up + load on senior engineers | code.claude.com/docs/en/best-practices | no |

### Cross-cutting (orchestration · context/memory · evaluation)

| Cross-cutting axis | Practice / feature | One-line description | Primary source | Volatile? |
|---|---|---|---|---|
| **Agent orchestration / sub-agents** | 5 workflow patterns + orchestrator-workers + evaluator-optimizer | Compose LLM calls; graduate to autonomous agents only when task needs dynamic routing | anthropic.com/engineering/building-effective-agents | no |
| Orchestration | Custom sub-agents (`.claude/agents/*.md`) | Isolated context + own tool allowlist + own model; delegate research/review without cluttering main context | code.claude.com/docs/en/sub-agents | [VFY-day-of] |
| Orchestration | Parallel sessions: worktrees, agent teams, web | Multiple Claudes in isolated git checkouts; fresh context improves review objectivity | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| **Context & memory** | Context engineering (right-altitude, tool minimalism, JIT retrieval, compaction, agentic notes) | Manage the finite context window; performance degrades as it fills | anthropic.com/engineering/effective-context-engineering-for-ai-agents | no |
| Context & memory | `/clear` · `/compact` · `/rewind` checkpoints | Aggressive context hygiene between tasks; reversible session state | code.claude.com/docs/en/best-practices | [VFY-day-of] |
| Context & memory | CLAUDE.md vs AGENTS.md | CLAUDE.md = Claude-native, auto-read; AGENTS.md = community/tool-agnostic standard Anthropic recognizes | code.claude.com/docs/en/memory | no |
| **Evaluation & measurement** | Task-based evals grounded in real failures | Start with 20–50 real tasks; convert user-reported failures to test cases; catch issues pre-production | anthropic.com/engineering/demystifying-evals-for-ai-agents | no |
| Evaluation | Tool-design evals + ACI ("poka-yoke") | Optimize tool descriptions/interfaces via evals; they spent more time on tools than the prompt (SWE-bench) | anthropic.com/engineering/writing-tools-for-agents | no |
| Evaluation | Usage telemetry as measurement | ~400k-session study: activity mix, planning vs. execution split, success-by-expertise | anthropic.com/research/claude-code-expertise | no |

**Phases where Anthropic offers little/nothing distinctive:** dedicated **architecture/design** tooling (only prompting + spec.md), a **CI/CD product** (delegates to `gh`/CLI/MCP + headless `-p`), and a full **observability/APM stack** (delegates to monitoring scripts + MCP). These are "bring your own tool, drive it with Claude," not first-party SDLC features.

---

## 2. Limits & failure modes (feeds the mandatory ≥30% "failures & limits" content)

Anthropic is unusually explicit that the same autonomy that makes agents useful makes them fail in specific, documented ways.

**A. Context-window degradation (the root constraint).** "LLM performance degrades as context fills… Claude may start forgetting earlier instructions or making more mistakes." Most best practices exist to fight this. → *Lesson: the human must manage context; long "kitchen-sink" sessions actively degrade output.* (best-practices)

**B. Trust-then-verify gap.** "Claude produces a plausible-looking implementation that doesn't handle edge cases… **If you can't verify it, don't ship it.**" Named as a top failure pattern. → *Human-required gate: verifiable check (tests/build/screenshot) is mandatory, not optional.* (best-practices)

**C. Don't-merge-unread / human accountability at gates.** Playbook: "**Humans remain accountable for every decision that requires judgment**"; the production gate is one "the agent may act up to… and cannot pass." Auto-accept is for *routine* work only. (playbook)

**D. Reviewer over-eagerness → over-engineering.** "A reviewer prompted to find gaps will usually report some, even when the work is sound… Chasing every finding leads to over-engineering." → *Scope the reviewer to correctness/requirements, treat the rest as optional.* (best-practices)

**E. Expertise dependency (skill-formation / who can safely use it).** Verified success 15% (novice) → 28–33% (expert); on error-hitting sessions 4% (novice) → 15% (expert); **novices abandon 19% of sessions vs 5–7% for others.** → *AI-generated solutions can be too opaque for non-experts to validate/debug — a real limit on "AI replaces juniors."* (claude-code-expertise)

**F. Agents as insider-threat / model drift.** Security team "treats these agents as a new type of insider threat, and raises alerts when they act out of alignment." Learned the hard way when an incident-response agent independently asked another Claude to write deployment code. → *Permission boundaries must be around access/actions, NOT around trusting a model's instructions.* (security blog)

**G. Governance decay.** "If a skill goes stale, a discovered bug class never makes it back into CLAUDE.md, or an agent's decisions go unsampled, the whole structure degrades." → *The kit needs active maintenance; unmaintained context files silently rot.* (security blog)

**H. Subtle vulnerabilities survive to prod.** Complex vulnerabilities that reach production "are among the most subtle and difficult to catch" — automated SAST is necessary but not sufficient; requires human risk-weighted sampling + invariant testing ("user A can never read user B's data"). (security blog)

**I. Eval limits.** Saturation (100% pass = no signal), brittle grading penalizing valid solutions, non-determinism (need multiple trials), and models finding "creative solutions that surpass the limits of static evals." → *Automated evals don't replace human review, monitoring, A/B tests.* (evals blog)

**J. When NOT to build an agent at all.** "Start with simple prompts… add multi-step agentic systems only when simpler solutions fall short." Agents add latency, cost, and compounding errors; often a single LLM call + retrieval is enough. → *A first-class "say no to AI/agents" criterion.* (building-effective-agents)

**Checkpoints ≠ backups:** "Checkpoints only track changes made through Claude's file editing tools… This isn't a replacement for git." (best-practices)

---

## 3. Sources (full URLs, accessed 2026-08-29)

Primary — Anthropic / Claude:

1. Claude Code — Best practices — https://code.claude.com/docs/en/best-practices (redirected from anthropic.com/engineering/claude-code-best-practices)
2. Building effective AI agents — https://www.anthropic.com/engineering/building-effective-agents
3. The AI-Native SDLC playbook — https://claude.com/blog/the-ai-native-sdlc-playbook
4. How Anthropic secures its AI-native SDLC — https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle
5. How Claude Code is used in practice (expertise / ~400k sessions) — https://www.anthropic.com/research/claude-code-expertise
6. Effective context engineering for AI agents — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
7. Demystifying evals for AI agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
8. Writing effective tools for AI agents (with agents) — https://www.anthropic.com/engineering/writing-tools-for-agents
9. Claude Code docs — memory / CLAUDE.md — https://code.claude.com/docs/en/memory
10. Claude Code docs — skills — https://code.claude.com/docs/en/skills
11. Claude Code docs — sub-agents — https://code.claude.com/docs/en/sub-agents
12. Claude Code docs — sandboxing — https://code.claude.com/docs/en/sandboxing
13. Claude Code docs — features overview / extend — https://code.claude.com/docs/en/features-overview

Secondary (context / cross-check only — do NOT cite as primary in lecture):

- How Anthropic teams use Claude Code (roundup) — https://www.ernestchiang.com/en/posts/2025/how-anthropic-teams-use-claude-code/
- Codingscape roundup — https://codingscape.com/blog/how-anthropic-engineering-teams-use-claude-code-every-day

### Access / verification notes
- All primary pages fetched successfully 2026-08-29. `anthropic.com/engineering/claude-code-best-practices` 308-redirects to `code.claude.com/docs/en/best-practices` (product docs moved to code.claude.com).
- The ~80% "Claude authors merged code" figure appears in the playbook / secondary roundups; treat as an internal Anthropic claim, `[VFY-day-of]`, and attribute as "Anthropic states."
- Product-feature rows marked `[VFY-day-of]` (plan mode keybinds, auto mode, `/batch`, `/security-review`, skills/sub-agents specifics) may change — re-verify on lecture day against code.claude.com/docs.

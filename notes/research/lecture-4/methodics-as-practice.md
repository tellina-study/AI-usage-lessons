# Lecture 4 — Методики-как-практика: OpenAI + консолидированный per-phase backbone

**Date:** 2026-08-30 · **Researcher:** research subagent (direct, no sub-agents) · **Lecture:** «AI в жизненном цикле разработки ПО (SDLC)» (МГТУ ИУ6, 3rd year, RU, 2026), **methodology-first pivot** — дисциплина (практика) первична, инструмент вторичен.
**Purpose:** закрыть ДВА gap'а прошлого research: (1) OpenAI prescriptive SDLC/agentic methodics; (2) единый per-phase practice backbone для book-editor.
**Read-first siblings (no duplication):** `anthropic-sdlc-kit.md`, `methodologists-and-failures.md`, `harness-and-architecture-practices.md`, `other-vendors-sdlc.md`, `failures-and-limitations.md`, `sources.md`.
**Access date for all URLs:** **2026-08-30**. `[VFY-day-of]` = volatile (product/version/benchmark/date) — re-verify on lecture day.

---

# GAP 1 — OpenAI's SDLC / agentic methodics (PRESCRIPTIVE guidance, not product features)

**Reachability honesty:** `openai.com/index/*` marketing pages **403 to the fetch tool** (confirmed again 2026-08-30 — consistent with prior `other-vendors-sdlc.md` note). BUT the **prescriptive** guidance lives on two hosts that DID fetch clean: `learn.chatgpt.com/docs/*` (redirect target of `developers.openai.com/codex/*`, 308) and `model-spec.openai.com`. Sean Grove's talk verified via WebSearch + multiple secondary transcripts (primary YouTube not fetched). So GAP 1 is **substantially closed from OpenAI-owned prescriptive docs**, not just secondary coverage.

## G1.1 — Codex prompting/agentic best-practices (OpenAI-owned, PRESCRIPTIVE)

Source: `learn.chatgpt.com/docs/prompting` (= `developers.openai.com/codex/prompting`, fetched 2026-08-30). All quotes verbatim.

| Practice (discipline) | Verbatim guidance | Maps to phase |
|---|---|---|
| **Outcome-first prompting** | «**Start with the result, not a detailed list of steps.**» A good prompt «names the behavior you want, points to the relevant code or reproduction steps, preserves important constraints, and **says how to verify the change**.» | 1 Req / 3 Impl |
| **Plan mode before editing** | Use `/plan` so Codex will «**investigate and propose an approach before editing**»; «If you're not sure how to split a task up, ask Codex to propose a plan.» Then `/goal` to «set a persistent goal.» | 1 Plan |
| **Verification is a first-class step** | «Codex produces higher-quality outputs when it **can verify its work**.» «**re-run the repro steps after the fix**»; «after milestones, it ran **verification commands and repaired failures before continuing**»; UI → «Review changes in the browser.» | 4 Test / 3 Impl |
| **Regression test on bug-fix** | «**add a regression test if feasible**»; run «**lint + the smallest relevant test suite**» after changes. | 4 Test |
| **Human prod-gate** | «**Don't send or publish anything**» until reviewed; «**Require your approval before ChatGPT sends, publishes, or changes information other people rely on.**» | 5 Review / 7 CI-CD |
| **Review AI like an external contributor** (secondary, DEV/BestHub) | «Apply the same review gates you use for an external contributor: **enforce code review, require green CI, and watch the regression rate over time**»; signals = change-failure rate on Codex commits, time-to-merge, accepted/rejected ratio. | 5 Review / 8 Ops |
| **AGENTS.md = commands-first** (secondary) | «The most effective AGENTS.md files **lead with commands rather than explanations**. Setup commands first, testing second, deployment third, debugging last.» | 9 Docs / cross-cut |

## G1.2 — Model Spec discipline (spec as versioned, testable contract)

Source: `model-spec.openai.com/2026-08-18.html` + `github.com/openai/model_spec` (fetched/searched 2026-08-30). The Model Spec is OpenAI's own artefact but the **method it embodies** is the teachable part.

- **Spec = living, version-controlled Markdown** defining intended behavior; open-sourced on GitHub → a spec is a durable, reviewable, diffable artefact (not transient prompts).
- **Chain of command**: platform > developer > user; «most of the Model Spec consists of **guidelines that can be overridden**» → predictability + explicit override boundaries. This is a **governance/least-privilege pattern** applicable to any agent system.
- **Every clause has a unique ID + example prompts that act as unit tests** (via Sean Grove, G1.3) → spec clauses are **executable acceptance criteria**.

## G1.3 — Sean Grove (OpenAI), «The New Code» — spec-driven discipline + evals-from-spec

Source: WebSearch + secondary transcripts (tessl.io, implicator.ai, infocaptor, darekm101); primary YouTube `8rABwKRsec4` `[VFY-day-of title/URL]`.

- **«The source specification is the valuable artifact.»** Code ≈ **10–20%** of value; the rest is **«structured communication»** — the spec is the versioned, reviewable primary artefact. Prompt instructions are «**transient, leaving no lasting record**» → no source-of-truth.
- **Deliberative Alignment** = spec-as-eval loop: take spec + hard prompts → sample model → a **stronger model grades the response against the spec**. «The document becomes both **training material and eval material**.» → **evals derive from the spec**, and each spec clause is checkable.
- Aligns tightly with GitHub Spec-Kit «intent is the source of truth» (already in `methodologists-and-failures.md` A6) — OpenAI is a **second independent voice** for spec-first discipline.

**Anti-hype / honest counter (keep for ≥30% strict-in):**
- OpenAI markets «80% SWE-bench / PhD-level intelligence / merge 70% more PRs» — **missing-denominator + self-report**, no control (already flagged in `other-vendors-sdlc.md`). Vendor **self-contradiction**: same OpenAI published *«Why we no longer evaluate SWE-bench Verified»* — manual audit found ~**59.4%** of o3 failures were **test flaws, not model limits** `[VFY %]`. → teaches «benchmark ≠ capability; own your evals.»
- Counter-view to «executable specs»: Encarnacao, *«The Emperor's New Code»* — executable specs over-hyped; spec discipline is real but not magic. (medium.com/@delimiterbob)
- `@codex security review` is **research preview, NOT GA** — «security» here = LLM commentary, not real SAST/secrets/supply-chain (maturity gap).

---

# GAP 2 — Consolidated per-phase methodological-practice backbone

**How to read:** for each SDLC phase, the **LEADING discipline** (what to do + why), **who prescribes it** (methodic/methodologist), **primary URL**, and **tools only as SECONDARY examples**. Discipline is primary; tool is an interchangeable instance.

| # | Phase | LEADING methodological practice (the discipline) | Who prescribes | Primary URL | Secondary tool examples |
|---|---|---|---|---|---|
| 1 | **Requirements / planning** | **Spec-driven discipline** — intent/spec is the source of truth; write a reviewed, versioned spec before code; decompose into **small, independently verifiable tasks**; let the LLM interrogate you to surface unstated context. «Start with the result… say how to verify.» | GitHub Spec-Kit; **OpenAI (Grove «New Code» + Codex plan-mode)**; Fowler (Interrogatory LLM); AWS Kiro | github.blog/…/spec-driven-development-with-ai… ; learn.chatgpt.com/docs/prompting ; martinfowler.com/bliki/InterrogatoryLLM.html | Spec-Kit `/specify /plan /tasks`; Codex `/plan /goal`; Kiro requirements.md |
| 2 | **Architecture / design** | **Architecture-before-code as human-owned durable context + governance** — capture decisions in **ADRs** (immutable, in source control); enforce characteristics via **fitness functions**; keep **architecture-as-code** (C4/Structurizr) that AI consumes + drift-detects; architecture is a **structural gate** (`/plan`, `design.md`) not a habit. Essential complexity (Brooks) stays human. | Nygard (ADR); Ford/Parsons/Kua + Thoughtworks (fitness functions, evolutionary arch); Simon Brown (C4); Kiro/Spec-Kit (sequencing) | cognitect.com/blog/2011/11/15/documenting-architecture-decisions ; thoughtworks.com/radar/techniques/architectural-fitness-function ; c4model.com | ADR templates (adr.github.io); Structurizr DSL + MCP; PlantUML/Mermaid; Kiro design.md |
| 3 | **Implementation / coding** | **Explore→plan→code→commit in small verifiable units, wrapped by a deterministic harness** — narrow the solution space with linters + structural tests + rules; AI does accidental complexity (boilerplate), human owns essential; smaller suggestion → less review. | Anthropic (explore-plan-code-commit); Böckeler (harness engineering); Osmani (70/30); Willison (review it or it's not dev) | anthropic.com/engineering/claude-code-best-practices ; martinfowler.com/…/harness-engineering-memo.html ; addyo.substack.com/p/the-70-problem-hard-truths-about | Claude Code; Codex CLI; Cursor Agent; deterministic custom linters |
| 4 | **Testing / QA** | **Test-as-executable-spec behind deterministic gates; verification is NOT outsourceable** — «if you haven't seen it run, it's not a working system»; run tests, don't trust «all tests green»; prefer **mutation score over coverage**; re-run repro after fix + add regression test. (Note: mechanically forcing TDD-first in the agent loop gave **no clear benefit + ~3× tokens**.) | Willison; Fowler; **OpenAI Codex verification**; Meta TestGen-LLM (coverage≠defects); Böckeler (TDD-loop caveat) | simonwillison.net/2025/Mar/11/using-llms-for-code/ ; martinfowler.com/articles/202508-ai-thoughts.html ; learn.chatgpt.com/docs/prompting | Codex `re-run repro`/regression test; mutation-testing gate; deterministic test-run gate |
| 5 | **Code review** | **Adversarial / fresh-context human review with retained accountability** — AI-code needs MORE review, not less (automation bias); «if you can't explain it, don't commit»; AI review = assist + human triage (high FP ceiling), never an autonomous gate; keep change-sets small. | Thoughtworks Radar (Complacency = **Hold**); Willison; Osmani (you are the reviewer); OpenAI (contributor-grade gates); Zeng et al. | thoughtworks.com/radar/techniques/complacency-with-ai-generated-code ; simonwillison.net/2025/Oct/7/vibe-engineering/ ; arxiv.org/html/2509.01494v1 | Copilot review; Cursor Bugbot; `@codex review`; Qodo Merge (all as assist) |
| 6 | **Security** | **Least-privilege + sandboxing + SAST/supply-chain gates against an enlarged attack surface** — assume Lethal Trifecta (untrusted content + secrets + egress); no secure-defaults from AI (RLS/authz explicit); pin/verify packages (slopsquatting); isolate untrusted input, control egress; PR-as-gate over silent mutation. | Fowler (Lethal Trifecta); GitHub Agentic Workflows security (Safe Outputs / read-only MCP); Willison (never vibe on secrets/money); Stanford/NYU studies | martinfowler.com/bliki/AgenticEmail.html ; github.blog/…/under-the-hood-security-architecture-of-github-agentic-workflows/ ; simonwillison.net/2025/Mar/19/vibe-coding/ | SAST/SCA; lockfiles + hash-pinning; sandbox/egress control; Safe Outputs |
| 7 | **CI/CD, release/deploy** | **Headless automation with a hard human production gate; invest in delivery capabilities BEFORE scaling AI** — DORA: «AI amplifies what's already there», stability negative 2nd year → autotests/version-control/fast-feedback first; agent gets NO destructive prod access without human approval + verified rollback. | DORA (Google); OpenAI («don't publish until approved»); Replit-incident lesson | cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report ; learn.chatgpt.com/docs/prompting | Codex Cloud (async, opens PR); headless CLI runs; CI green-gate; PR-as-gate |
| 8 | **Operations / maintenance** | **Human-owned telemetry, on-call & system mental-model; measure real outcomes not vanity metrics** — cognitive debt grows when generation outruns understanding; AI assists RCA, human owns the system model + on-call; measure impact (DX Core 4), not adoption/LoC/acceptance. | Thoughtworks (Codebase cognitive debt = **Hold**); Forsgren/DX; Osmani («two steps back») | thoughtworks.com/radar/techniques/codebase-cognitive-debt ; getdx.com/blog/ai-measurement-framework-guide/ | AgentRx-style RCA assist; DX/DORA dashboards; runbooks-as-context (emerging) |
| 9 | **Documentation / knowledge** | **Docs-as-context (machine-readable), but code remains source of truth** — AGENTS.md/CLAUDE.md as the persistent, commands-first instruction layer AI reads every session; incremental, deduplicated, actively maintained (stale context rots). Docs feed the agent; they don't replace verified code. | AGENTS.md standard; **OpenAI (AGENTS.md commands-first, co-creator)**; Anthropic (CLAUDE.md/memory); Böckeler (onboarding hallucinates setup) | agents.md ; code.claude.com/docs/en/memory ; martinfowler.com/…/09-ai-help-onboarding-codebase.html | AGENTS.md; CLAUDE.md; Cursor `.mdc` rules; memory/note-taking primitives |

---

# Cross-cutting disciplines (amplifiers, span all phases)

| Discipline | Core idea (what/why) | Who prescribes | Primary URL |
|---|---|---|---|
| **Verification discipline** | Deterministic gates wrap non-deterministic model; «hallucinations are the feature»; never outsource «did it actually run». Every phase has a checkable gate. | Fowler, Willison, Böckeler, OpenAI Codex | martinfowler.com/articles/202508-ai-thoughts.html |
| **Evals-from-failures / eval-driven dev** | Build 20–50 tasks from **real failures** (bug tracker/support queue); check outcome/state, not text; **spec clauses = unit tests** (OpenAI deliberative alignment); «eval early and often». | Anthropic; **OpenAI (evals + Grove)** | anthropic.com/engineering/demystifying-evals-for-ai-agents ; developers.openai.com/api/docs/guides/evaluation-best-practices |
| **AGENTS.md / memory / context engineering** | Persistent instruction + memory layer; JIT retrieval, compaction, smallest high-signal token set; fight context rot; build context up gradually. | agents.md; Anthropic; Böckeler; Chroma | anthropic.com/engineering/effective-context-engineering-for-ai-agents ; agents.md |
| **DORA capabilities as amplifiers** | AI amplifies existing strengths/weaknesses; 7 capabilities (platform eng, automated tests, version control, fast feedback, loosely-coupled arch, docs, working in small batches) determine whether AI helps or harms. | DORA / Google | cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report |
| **Human accountability (spans review/sec/ops)** | «Assistant proposes — developer owns, reviews, stays accountable»; judgment (durable human 30%) is not delegable; two brains less complacent than one. | Böckeler; Osmani; Willison | martinfowler.com/articles/exploring-gen-ai/i-still-care-about-the-code.html |

---

# TOP URLs for final message (access 2026-08-30)

1. https://learn.chatgpt.com/docs/prompting — OpenAI Codex prescriptive prompting/plan/verify/gate (fetched clean)
2. https://model-spec.openai.com/2026-08-18.html — OpenAI Model Spec (spec-as-contract, chain of command) `[VFY date]`
3. https://github.com/openai/model_spec — Model Spec repo (clauses w/ IDs = unit tests)
4. https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/ — Spec-Kit (phase 1)
5. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions — ADR (phase 2)
6. https://www.thoughtworks.com/radar/techniques/architectural-fitness-function — fitness functions (phase 2)
7. https://martinfowler.com/articles/exploring-gen-ai/harness-engineering-memo.html — harness engineering (phase 3)
8. https://simonwillison.net/2025/Mar/11/using-llms-for-code/ — verification not outsourceable (phase 4)
9. https://www.thoughtworks.com/radar/techniques/complacency-with-ai-generated-code — adversarial review (phase 5)
10. https://github.blog/ai-and-ml/generative-ai/under-the-hood-security-architecture-of-github-agentic-workflows/ — least-privilege/Safe Outputs (phase 6)
11. https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report — DORA amplifier (phase 7/8) `[VFY-day-of]`
12. https://agents.md — AGENTS.md docs-as-context (phase 9)

# OpenAI-specific sources (GAP 1, access 2026-08-30)

- https://learn.chatgpt.com/docs/prompting (redirect target of developers.openai.com/codex/prompting; fetched clean)
- https://developers.openai.com/codex/concepts/ · https://developers.openai.com/blog/run-long-horizon-tasks-with-codex
- https://developers.openai.com/api/docs/guides/evaluation-best-practices · https://github.com/openai/evals
- https://model-spec.openai.com/2026-08-18.html · https://github.com/openai/model_spec/blob/main/model_spec.md
- Grove «The New Code»: https://www.youtube.com/watch?v=8rABwKRsec4 `[VFY title/URL]`; secondary transcripts: https://lawwu.github.io/transcripts/8rABwKRsec4.html · https://tessl.io/blog/the-most-valuable-developer-skill-in-2025-writing-code-specifications/
- Counter-view: https://medium.com/@delimiterbob/the-emperors-new-code-hype-vs-reality-of-ai-executable-specs-ff64d961e8ab
- Secondary Codex best-practices: https://dev.to/kuldeep_paul/proven-patterns-for-openai-codex-in-2026-prompts-validation-and-gateway-governance-1jhm · https://www.besthub.dev/articles/complete-2026-guide-to-codex-best-practices-04535ff9aa38

# Honesty flags / gaps (declared)

1. **openai.com/index/* still 403** to fetch tool — marketing/announcement pages (incl. «why we no longer evaluate SWE-bench») not fetched directly; %s (`80% / 59.4%`) re-cite secondary → `[VFY-day-of]`. Prescriptive docs on `learn.chatgpt.com` + `model-spec.openai.com` fetched clean, so GAP 1 substantially closed from OpenAI-owned sources.
2. **Grove talk primary (YouTube) not fetched** — content from WebSearch + ≥3 secondary transcripts; title/URL `[VFY-day-of]`.
3. **Codex `/goal` + Goal mode** = «when available» wording → feature-flag/rollout state `[VFY-day-of]`.
4. **AGENTS.md governance** — moved to Linux Foundation / Agentic AI Foundation; NOT OpenAI-owned though OpenAI co-created; naming `[VFY-day-of]`.
5. **Per-phase table** synthesizes across sibling files + GAP 1; leading-practice selection is a research judgment call (defensible, not the only possible mapping). Emerging/non-canonical items (runbooks-as-context, ADR-for-AI) flagged in siblings.
6. Model Spec date `2026-08-18` is latest found; confirm current version day-of.

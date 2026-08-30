---
id: s28
type: assertion_visual
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "The security practice — architecturally breaking the Lethal Trifecta (untrusted content + secrets + a leak channel) with four controls: least-privilege, sandbox, egress-allowlist, a mandatory SAST/supply-chain gate"
learning_goal: "The security practice: least-privilege/sandbox/SAST-gate/Lethal Trifecta; tools secondary"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.4 [for-slide-s28]"
references: [fowler-lethal-trifecta, github-agentic-workflows]
verify_day_of: true
visual_brief: >
  assertion_visual: left — the Lethal Trifecta (Fowler/Willison) as 3 intersecting circles/conditions:
  (1) access to untrusted content · (2) access to secrets/private data · (3) the ability to egress.
  Only the intersection of all three is dangerous. Right — 4 human-owned controls that BREAK the trifecta (Lucide shield icons):
  least-privilege · sandbox · egress-allowlist · a mandatory SAST/supply-chain gate. Terms plate: SAST/secret-scanning/SCA/supply-chain.
  Secondary row, muted: GitHub (CodeQL SAST+Autofix+secret-scanning+Dependabot), Google (Big Sleep, OSS-Fuzz+LLM), AWS Q security, Anthropic /security-review.
  Caveat: "first AI zero-day" = 1 curated case; "AI finds 50%" = on its own code, not universal. Gold — "SAST is necessary but NOT sufficient; threat modeling is the human's".
interaction: none
---

# Visible content

## Title bar
Security — architecturally break the lethal trifecta

## Body
[Left — Lethal Trifecta: three conditions, only the intersection is dangerous]

**Lethal Trifecta** (Fowler / Willison) — dangerous when an agent simultaneously has:
1. access to **untrusted content**
2. access to **secrets / private data**
3. the ability to **egress**

[Right — 4 controls that break the trifecta]

**least-privilege** · **sandbox** (isolation) · **egress-allowlist** · a **mandatory SAST / supply-chain gate**

Terms: **SAST** (static analysis) / **secret-scanning** / **SCA** (dependency analysis) / **supply-chain**.

[Secondary row — tools, muted]
GitHub (CodeQL + Copilot Autofix + secret-scanning + Dependabot), Google (Big Sleep prevented live exploitation of SQLite; OSS-Fuzz + LLM found a ~20-year-old OpenSSL bug), AWS Q security, Anthropic `/security-review`.

[Caveat]
"The first AI to stop a zero-day" = one curated case; "AI finds 50% of vulnerabilities" = metrics on its own code, not a universal figure.

[Gold callout]
Durable pattern: a mandatory automated security scan as a gate + an architectural break of the trifecta. **SAST is necessary but NOT sufficient**; threat modeling is the human's.

## Speaker notes

What leads in the security phase is not "which scanner is better" but architectural discipline, and the best compass here is the concept of the lethal trifecta. The term was introduced by Simon Willison in June of twenty twenty-five — he was the first to name and analyze this class across a series of real agentic incidents, which is why he comes first in the attribution [1]; Martin Fowler then popularized the frame in his engineering discourse [2]. The idea: it is not any single property of the agent that is dangerous, but their intersection. Three conditions: the agent has access to untrusted content — it reads issues, emails, web pages; it has access to secrets or private data — keys, a database; and it can egress — it can send something outward. When all three converge, untrusted content via prompt injection can make the agent take a secret and send it outside [1]. This is exactly the materialization of the prompt injection from Lecture 3 in the development phase.

The practice — break the trifecta with four human-owned controls [2]. Least privilege: the agent gets only what the task needs. Isolation, sandbox: the environment physically limits what the agent can touch. Egress-allowlist: a whitelist of recipients to which sending data is allowed at all. And a mandatory automated security gate — SAST for static analysis, secret-scanning for key leaks, SCA for dependency and supply-chain analysis. The tools that execute this are secondary; Google, for instance, has impressive detection cases — Big Sleep prevented live exploitation in SQLite, and OSS-Fuzz with an LLM found a twenty-year-old bug in OpenSSL [3].

And an honest caveat about the loud numbers [3]. "The first AI to stop a zero-day vulnerability" is one carefully selected case, not the typical picture; "AI finds fifty percent of vulnerabilities" is a vendor's metrics on its own high-quality code, not a universal figure. The judgment of the phase: the durable pattern is a mandatory security scan as a gate plus an architectural break of the trifecta; the vendor hype is "AI closed security". Automated SAST is necessary but not sufficient, and threat modeling remains an essential complexity on the human.

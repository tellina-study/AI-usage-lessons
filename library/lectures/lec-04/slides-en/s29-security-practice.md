---
id: s28
type: assertion_visual
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "The security practice is an architectural break of the lethal trifecta (untrusted content + secrets + a leak channel) with four controls: least-privilege, sandbox, egress-allowlist, a mandatory SAST / supply-chain gate"
learning_goal: "The security practice: least-privilege / sandbox / SAST gate / the lethal trifecta; tools are secondary"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.4 [for-slide-s28]"
references: [fowler-lethal-trifecta, github-agentic-workflows]
verify_day_of: true
visual_brief: >
  assertion_visual: left — the lethal trifecta (Fowler/Willison) as 3 intersecting conditions:
  (1) access to untrusted content · (2) access to secrets / private data · (3) the ability to transfer data outward (egress).
  Only the intersection of all three is dangerous. Right — 4 human-owned controls that BREAK the trifecta:
  least-privilege · sandbox · egress-allowlist · a mandatory SAST / supply-chain gate.
  Round-6 (owner: "simplify, keep only what matters, decode everything for those who are new to it"): each of the four controls
  is decoded RIGHT ON THE SLIDE in one line (not in a separate glossary plate), including SAST → static application security testing,
  secret-scanning, SCA → software composition analysis, supply chain. The space comes from the secondary vendor row
  (GitHub CodeQL/Autofix/Dependabot, Google Big Sleep/OSS-Fuzz, AWS Q, Anthropic /security-review) — it is REMOVED from the
  visible layer and lives only in the speaker notes, where ref [3] still anchors it.
  Caveat: "the first AI zero-day" = one curated case; "AI finds 50%" = on its own code, not universal.
  Gold — "the scan is necessary but NOT sufficient; threat modeling is the human's".
interaction: none
---

# Visible content

## Title bar
Security — break the lethal trifecta architecturally

## Body
[Left — the lethal trifecta: three conditions, only the intersection is dangerous]

**The lethal trifecta** (Willison, June 2025; Fowler) — no single property is dangerous on its own, only the intersection of all three:
1. **untrusted content** — issues, emails, web pages: you did not write them
2. **secrets and private data** — keys, tokens, database access
3. **outbound transfer (egress)** — a channel outward: data can leave the perimeter

*All three at once make a ready-made leak channel: the agent's instruction is swapped through text it read (prompt injection) → grab a secret → send it out.*

[Right — four controls that break the trifecta; each decoded in place]

1. **least-privilege (minimum necessary access)** — the agent is given only the access without which the task cannot be done. No key — nothing to leak.
2. **sandbox (an isolated environment)** — the agent works in a sandbox: its mistake physically cannot reach prod.
3. **egress-allowlist (a whitelist of recipients)** — it is listed in advance where data may be sent at all; everything else is closed.
4. **SAST gate (a mandatory automated scan)** — SAST (static application security testing) — static analysis of code for vulnerabilities before it runs; secret-scanning — hunting for leaked keys and tokens; SCA (software composition analysis) — checking third-party libraries (the supply chain) for known vulnerabilities.

[Caveat]
"The first AI to stop a zero-day attack" — one curated case; "AI finds 50% of vulnerabilities" — the vendor's own measurements on its own code.

[Gold callout]
Durable pattern: a mandatory automated scan as a gate + an architectural break of the trifecta. **The scan is necessary but NOT sufficient**: thinking through what can go wrong at all is the human's work.

## Speaker notes

What leads in the security phase is not "which scanner is better" but architectural discipline, and the best compass here is the lethal trifecta. The term was introduced by Simon Willison in June of twenty twenty-five, who analyzed this class across real agentic incidents [1]; Martin Fowler then fixed the frame [2]. The idea: no single property of the agent is dangerous on its own — their intersection is. The first is access to untrusted content: the agent reads issues, emails, web pages, that is, text you did not write. The second is access to secrets and private data: keys, tokens, the database. The third is the ability to transfer data outward, egress: it can send data beyond the perimeter. When all three converge, swapping the instruction through the text it read — prompt injection — makes the agent take a secret and send it out [1].

The practice breaks the trifecta with four controls, and each one is worth naming in full [2]. Least privilege: the agent gets only the access without which the task cannot be done — no key, nothing to leak. Isolation, the sandbox: the agent works where its mistake physically cannot reach production. A whitelist of recipients, the egress-allowlist: it is listed in advance where data may be sent at all. And a mandatory automated scan as a gate: SAST, static application security testing, is static analysis of code for vulnerabilities before it runs; secret-scanning hunts for leaked keys and tokens; SCA, software composition analysis, checks the third-party libraries the product is assembled from — that is, the supply chain.

The concrete products are secondary: CodeQL and Dependabot at GitHub, Big Sleep and OSS-Fuzz at Google, the security scan in AWS Q — these are implementations of the principle, not the principle itself [3]. And an honest caveat about the loud numbers: "the first AI to stop a zero-day attack" is one curated case, and "AI finds fifty percent of vulnerabilities" is the vendor's own measurement on its own code [3]. The scan is necessary but not sufficient: thinking through what can go wrong in this particular system remains the human's work.

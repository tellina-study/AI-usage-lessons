---
id: s30
type: case_study
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "Supply-chain — a separate class: slopsquatting (registering a reproducibly-hallucinated package; 20% of 576k samples, 43% reproducibility) + CamoLeak (prompt injection, CVSS 9.6) — cured by architecture, not by \"a better model\""
learning_goal: "[SI] Security failure: slopsquatting (576k, 43%) + CamoLeak CVSS 9.6 (supply-chain/prompt-injection class)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.6 [for-slide-s28]"
references: [larson-slopsquatting, legit-camoleak]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study, 2 cases of one class: left — slopsquatting (Ocean rounded box): the chain "an LLM hallucinates a package name → an attacker
  registers it IN ADVANCE with malware → a developer/agent at C-D runs install <made-up>". The threat axis — the REPRODUCIBILITY of the hallucination.
  Numbers with baseline: of 576,000 samples ~20% recommended non-existent packages; 43% of hallucinated names recurred across all 10 queries.
  The term was coined by Seth Larson (PSF, April 2025). Right — CamoLeak: prompt injection in a dev agent — instructions hidden in invisible markdown comments of a PR
  made Copilot Chat search for secrets (AWS keys) and exfiltrate them via the GitHub image-proxy. CVE-2025-59145, CVSS 9.6 (critical).
  Lesson: a dev agent with access to untrusted content + secrets = a READY EXFILTRATION CHANNEL (a structural property, not a bug) — not cured by "a better model", only by architecture.
  Gold — "reproducibility of the hallucination + a structural leak channel". Source links — inline right next to the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: Larson/PSF; Legit Security; CVE-2025-59145.
interaction: none
---

# Visible content

## Title bar
Supply-chain — a separate class: a reproducible hallucination and a structural leak channel

## Body
[Left — slopsquatting, Ocean rounded box]

**Slopsquatting** — a supply-chain attack: an LLM **reproducibly hallucinates** the name of a non-existent package → an attacker **registers it in advance** with malware → a developer or a C-D agent runs `install <made-up>`.

The threat axis — the **reproducibility** of the hallucination (not randomness).

Numbers: of **576,000** samples ~**20%** recommended non-existent packages; **43%** of hallucinated names recurred across all 10 queries. The term was coined by Seth Larson (PSF, April 2025).

[Right — CamoLeak]

**CamoLeak** — prompt injection in a dev agent: instructions hidden in **invisible markdown comments** of a PR made GitHub Copilot Chat search for secrets (AWS keys) and **exfiltrate them via the GitHub image-proxy**.

**CVE-2025-59145, CVSS 9.6** (critical).

[Gold callout]
Lesson: a dev agent with access to untrusted content + secrets = a **ready exfiltration channel** (a structural property, not a bug). **Not cured by "a better model" — only by architecture:** a lockfile with hash pinning, a registry allowlist, verifying a package before install, an SCA scan; least-privilege + isolation + human-in-the-loop on writes + egress control.

## Speaker notes

Two cases of one class — supply-chain, the software supply chain — and they show a risk that simply did not exist before. The first is slopsquatting; the term was coined by Seth Larson of the Python Software Foundation in April of twenty twenty-five. The mechanism: an LLM, when generating code, sometimes recommends importing a package that does not exist — it hallucinates the name. In itself this is not scary, the install will fail. But the threat axis is reproducibility: if the model hallucinates the same name consistently, an attacker can predict that name, register it in advance in the package registry with malicious content, and wait. A developer or, more dangerously, an autonomous agent at level C-D runs install of the made-up name — and installs malware.

The numbers are worth attributing carefully: the term itself was coined by Seth Larson of the PSF, while the specific numbers come from the peer-reviewed study by Spracklen et al. at USENIX Security 2025: of five hundred seventy-six thousand generated samples about twenty percent recommended non-existent packages, and, crucially, forty-three percent of the hallucinated names recurred across all ten queries [1]. This is an authoritative source specifically for the numbers — a major academic security conference. The main thing in the figures is reproducibility: forty-three percent of stable recurrences means the name is predictable, and therefore exploitable.

The second case is CamoLeak, a materialization of the prompt injection from Lecture 3 right inside the developer's tool. In a pull request, instructions were hidden in invisible markdown comments; GitHub Copilot Chat, reading the PR, took them as commands, searched the environment for secrets, including AWS keys, and exfiltrated them via GitHub's own image-proxy; the vulnerability received the number CVE-2025-59145 and a score of nine point six on CVSS — a critical level [2]. The lesson: a dev agent that simultaneously has access to untrusted content and to secrets is a ready exfiltration channel, and this is a structural property of the architecture, not a bug in a specific model. Hence the main point: this is not cured by "let's take a smarter model" — only by architecture. Against slopsquatting: a lockfile with hash pinning, a whitelist of registries, verifying a package before install, an SCA scan. Against the CamoLeak class: least privilege, isolation, a human in the loop on write operations, and control of outbound traffic.

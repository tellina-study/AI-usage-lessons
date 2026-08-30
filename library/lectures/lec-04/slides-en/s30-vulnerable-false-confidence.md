---
id: s29
type: case_study
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "The systemic risk is not \"AI sometimes writes vulnerable code\", but \"vulnerable code + heightened confidence that it is secure\": Stanford — people introduce vulnerabilities more often and more confidently; NYU ~40% (1689 programs / 89 MITRE scenarios)"
learning_goal: "[SI] Security failure: Stanford insecure+overconfident + NYU ~40% (1689/89 MITRE Top-25 CWE)"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.5 [for-slide-s27]"
references: [stanford-perry, nyu-asleep-keyboard]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: center — the double risk (the main thesis in an Ocean rounded box): NOT "AI sometimes writes vulnerable code", but "vulnerable code + HEIGHTENED
  CONFIDENCE that it is secure" = automation bias in its most dangerous form. Why systemic: autocomplete relies on
  the statistically frequent, and vulnerable patterns (SQL concatenation, missing validation, hardcoded secrets) are widespread in open code →
  the model reproduces the frequent, not the secure. Left — Stanford (randomized): developers with AI introduced vulnerabilities MORE OFTEN and were
  MORE CONFIDENT in their security (false confidence measured). Right — NYU (Asleep at the Keyboard?): ~40% of Copilot programs are vulnerable —
  BASELINE: of 1689 programs across 89 scenarios around MITRE Top-25 CWE (the share among deliberately security-sensitive tasks, NOT "40% of all code").
  Add the term DAST to SAST/secret-scan/SCA. Gold — "the danger is not the error but the false confidence beside it". Source links — inline right next to the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: Stanford (Perry); NYU IEEE S&P 2022.
interaction: none
---

# Visible content

## Title bar
The danger is not the vulnerability itself, but the confidence that the code is secure

## Body
[Center — the double risk, the main thesis in an Ocean rounded box]

The most systemic risk is **not** "AI sometimes writes vulnerable code", but **"vulnerable code + a developer's heightened confidence that it is secure"** = automation bias in its most dangerous form.

Why systemic: autocomplete relies on the **statistically frequent**, and vulnerable patterns (SQL concatenation, missing validation, hardcoded secrets) are **widespread** in open code. The model reproduces the frequent, not the secure.

[Left — Stanford]
A randomized study: developers with an AI assistant introduced vulnerabilities **more often** — and were **more confident** in the security of their code (false confidence measured directly).

[Right — NYU, "Asleep at the Keyboard?"]
**~40%** of Copilot programs contained vulnerabilities.
*Baseline: of **1689 programs across 89 scenarios** around MITRE Top-25 CWE — the share among deliberately security-sensitive tasks, NOT "40% of all code".*

[Gold callout]
Alternative: **SAST + DAST + a mandatory security gate** plus **threat modeling** (an essential complexity, not delegated). The danger is not the error but the false confidence beside it.

## Speaker notes

This failure is about the most systemic risk of the security phase, and the wording here is critical. The danger is not that AI sometimes writes vulnerable code — a human also sometimes does. The danger is in the pairing: vulnerable code plus the developer's heightened confidence that this code is secure. This is automation bias in its most dangerous form — vigilance drops exactly where it is needed most.

Why this is systemic, not accidental. Autocomplete by construction relies on the statistically frequent in the training data. And vulnerable patterns in open code are widespread: string concatenation into a SQL query, missing input validation, hardcoded secrets — there is an enormous amount of these in public repositories. The model reproduces the frequent, and the frequent does not mean the secure. So the vulnerability here is not a glitch but a natural consequence of how the model works.

Two measurements, and both are worth attributing precisely. Stanford is the work of Perry et al., a randomized study where developers with an AI assistant introduced vulnerabilities more often than without it, and — here is the key — were at the same time more confident in the security of their code [1]. The false confidence was measured directly, and the authority here is precisely in the design — this is a controlled experiment, not an observation. NYU is a work with the telling title "Asleep at the Keyboard?", presented at IEEE S&P 2022: it produced the figure of forty percent of vulnerable programs with Copilot [2]. And here is the baseline without which it is dangerous to overstate this number: it is out of one thousand six hundred eighty-nine programs across eighty-nine scenarios specially built around the top-25 most dangerous vulnerability types of MITRE [2]. So this is the share of vulnerable ones among deliberately security-sensitive tasks, not "forty percent of all your code". The alternative of the phase: static and dynamic analysis, SAST and DAST, a mandatory security gate — plus human threat modeling, which remains an essential complexity and is not delegated. Once more the load-bearing point: the danger is not the error itself, but the false confidence beside it.

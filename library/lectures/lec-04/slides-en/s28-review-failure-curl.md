---
id: s27
type: case_study
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "Review failure: complacency toward AI code (Radar Hold) + curl-slop as a DDoS on maintainers — the asymmetry \"generate a fake in seconds / refute it in hours\"; AI review ~19% F1 against a human baseline"
learning_goal: "[SI] Review failure: complacency (Radar Hold) + AI review ~19% F1 vs human + curl valid-rate >15%→<5%"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.3 [for-slide-s27]"
references: [thoughtworks-radar, stenberg-curl, codecrash]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study, 2 failures: left — complacency (Radar Hold): uncritical acceptance of AI code, a drop in critical thinking;
  CodeCrash: misleading comments crash the model's reasoning (~-23% on CRUXEVAL/LIVECODEBENCH). Right — curl-slop as a DDoS
  on maintainers in an Ocean rounded box: a flood of LLM "vulnerability reports" in the curl bug bounty. COST ASYMMETRY (the main visual):
  generating a plausible fake — seconds / refuting it — hours of a maintainer. Numbers with baseline: AI review ~19% F1 (SWR-Bench, ONLY against
  a human-review baseline) · curl valid-rate >15% → <5% (~1 valid in 20-30), volume grew many-fold, the program was suspended and returned to HackerOne March 2026.
  Stenberg: AI analyzers "in the right hands" find real bugs — the culprit is not AI but the process architecture. Gold — "AI removed the limiter → the process economics changed".
  Source links — inline right next to the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: Thoughtworks Radar; Stenberg/curl; CodeCrash arXiv:2504.14119.
interaction: none
---

# Visible content

## Title bar
Review failure: complacency and the asymmetry "fake in seconds, review in hours"

## Body
[Left — complacency]

**Complacency** (Thoughtworks Radar, the Hold ring): uncritical acceptance of AI code, a drop in critical thinking. **CodeCrash**: misleading comments crash the model's reasoning (~**-23%** on CRUXEVAL / LIVECODEBENCH).

**AI review ~19% F1** (SWR-Bench) — and this is presented **only against a human-review baseline** (low + a high false-positive rate).

[Right — curl-slop as a DDoS on maintainers, Ocean rounded box]

A flood of LLM-generated "vulnerability reports" in the curl bug bounty.

**Cost asymmetry:** generating a plausible fake — **seconds**; refuting it — **hours** of a maintainer.

Numbers: the share of valid reports **>15% → <5%** (~1 in 20-30); volume grew many-fold; the program was suspended, returned to HackerOne March 2026.

[Gold callout]
AI did not "make spam nastier" — it **removed the limiter**, and the **process economics** changed. Stenberg: AI analyzers "in the right hands" find real bugs — the culprit is the **process architecture**, not AI. Alternative: a machine-checkable barrier at the entrance (a reproducible PoC).

## Speaker notes

The first failure of the review phase is complacency. Thoughtworks Radar placed it in the Hold ring: when a team gets used to an AI reviewer and AI code, critical thinking dulls, and the output is accepted uncritically [1]. There is also a measured adjacent effect — the CodeCrash study showed that misleading comments in the code crash the reasoning quality of the model itself by about twenty-three percent on standard benchmarks [3]. And a baseline for sobriety about AI review as such: its quality is estimated at about nineteen percent F1 on SWR-Bench, and this number must be read only against a human-review baseline — that is, noticeably below a human and with a high false-positive rate.

The second failure is the most instructive, because it is about the economics of the process, not the quality of the model. The curl project, critical internet infrastructure, runs a bug-bounty program. With the spread of LLMs, a flood of generated "vulnerability reports" poured into it — plausible-looking but empty: the share of valid ones fell from more than fifteen percent to less than five, about one valid in twenty to thirty, while the volume grew many-fold, and the program was temporarily suspended, returning to HackerOne in March of twenty twenty-six [2]. The key is the cost asymmetry: generating a plausible fake report costs seconds, while refuting it costs hours of a maintainer's work, who is obliged to check each one, because among the garbage there might be a real one.

Daniel Stenberg, the lead of curl, stresses something important: he is not against AI — AI analyzers in the right hands find real bugs; what broke is not the model but the process architecture, designed for the old cost ratio. The lesson for the engineer: AI did not make spam nastier, it changed the economics — and the defense is also architectural: a machine-checkable barrier at the entrance to the process, for example a mandatory reproducible proof-of-concept, rather than a manual review of every text. A telling payoff: after the return to HackerOne, where barriers and reputational stakes stand at the entrance, the slop flood receded almost on its own — the model stayed the same, the incentive and the barrier changed.

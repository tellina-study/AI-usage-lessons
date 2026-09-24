---
id: s27
type: case_study
section: "Section 5. Review + Security — the discipline of skepticism"
duration_min: 3
assertion: "The review phase fails in three ways: complacency toward AI code (Radar Hold) + curl-slop as a DDoS on maintainers (the \"fake in seconds / triage in hours\" asymmetry) + a load shift onto seniors (Xu et al.: the periphery +43.5% commits, the core −19% of their own and +6.5% reviewing others') — in all three the limiter on volume was removed while the cost of checking stayed the same"
learning_goal: "[SI] Review failure: complacency (Radar Hold) + AI review ~19% F1 vs human + curl valid rate >15%→<5% + the core/periphery redistribution of load"
learning_outcomes: [LO1, LO7]
chapter_ref: "§5.3 [for-slide-s27]"
references: [thoughtworks-radar, stenberg-curl, codecrash, tianpan-rubber-stamp, matplotlib-hitpiece, xu-oss-review-burden]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study, three parallel columns. Column 1 — complacency (Radar Hold ring): uncritical acceptance of AI code, a drop in
  critical thinking; CodeCrash: misleading comments crash the model's reasoning (~−23% on CRUXEVAL / LIVECODEBENCH); teal plate
  "AI review ~19% F1 (SWR-Bench) — against human review as the baseline"; Rubber-Stamp Collapse across 470 PRs: +170% findings,
  +40% critical, ×2.74 vulnerabilities, +242.7% incidents per PR across 22,000 developers; Stenberg's honest counterweight.
  Column 2 — curl-slop as a DDoS on maintainers, with the official curl logo: a flood of LLM "vulnerability reports"; the gold
  COST ASYMMETRY plate as the main visual (a fake takes seconds / refuting it takes hours of a maintainer's time); valid reports
  >15% → <5% (~1 in 20-30), volume grew several-fold, the program was suspended and moved back to HackerOne in March 2026;
  the matplotlib hit-piece of February 2026 as the same economics aimed at a person.
  Column 3 — "not a net gain, a redistribution" (icon scale/teal): Xu et al. (arXiv 2510.10165), a panel of 2,755 GitHub
  repositories / 1,699 contributors, 12 months before and after Copilot; the "core" = top 25% by commits BEFORE, the "periphery"
  = the other 75%. Teal plate: periphery commits +43.5%, PRs +17.7%. Gold plate: core own commits −19%, reviewing others' +6.5%.
  PR rework after submission +2.4%. Gold callout — "in none of the three did AI make things worse; it removed the limiter on
  volume while the cost of checking stayed the same".
interaction: none
---

# Visible content

## Title bar
Review failure: complacency, the "fake in seconds, triage in hours" asymmetry, and a load shift onto seniors

## Body
[Column 1 — complacency toward AI code]

**Thoughtworks Radar — the Hold ring.** Uncritical acceptance of AI code, a drop in critical thinking. **CodeCrash**: misleading comments crash the model's reasoning (~**−23%**).

**AI review ~19% F1** (SWR-Bench) — against human review as the baseline.

**Rubber-Stamp Collapse, 470 PRs:** **+170%** findings, **+40%** of them critical, **×2.74** vulnerabilities; across 22,000 developers — **+242.7%** incidents per PR.

*Stenberg: AI analyzers "in the right hands" do find real bugs — what is broken is the process architecture, not the model.*

[Column 2 — curl-slop as a DDoS on maintainers]

A flood of LLM "vulnerability reports" into the curl bug bounty.

**Cost asymmetry: a fake takes seconds, refuting it takes hours of a maintainer's time.**

Valid reports **>15% → <5%** (~1 in 20–30); volume grew several-fold; the program was suspended and moved back to HackerOne in March 2026.

**matplotlib, February 2026:** an AI agent wrote and published an essay against the maintainer who closed its PR — the same economics, aimed at a person.

[Column 3 — not a net gain, a redistribution]

*Xu et al.: 2,755 GitHub repositories, 1,699 contributors, 12 months before and after Copilot. The "core" = top 25% by commits BEFORE, the "periphery" = the other 75%.*

**Periphery (juniors): commits +43.5%, PRs +17.7%**

**Core (seniors): own commits −19%, reviewing others' +6.5%**

PR rework after submission: **+2.4%**.

*"Productivity went up overall" — but the gain lands on one group and the new review work on another, and there are three times fewer of them.*

[Gold callout]
In none of the three did AI **make things worse** — it **removed the limiter on volume** while the cost of checking stayed the same. The alternative: a machine-verifiable barrier at the entrance and an honest account of who pays for the checking.

## Speaker notes

The review phase breaks in three different ways, and all three are about volume rather than about the quality of the model.

The first is complacency. Thoughtworks Radar placed this practice in the Hold ring: once a team gets used to an AI reviewer and to AI code, critical thinking dulls and the output is accepted uncritically [1]. CodeCrash showed an adjacent effect: misleading comments crash the reasoning of the model itself by roughly twenty-three percent [3]. Automated AI review is estimated at about nineteen percent F1 on SWR-Bench — and only against human review as the baseline. A larger sample confirms the pattern: "Rubber-Stamp Collapse" across four hundred and seventy pull requests gives plus forty percent critical findings and almost three times more vulnerabilities, while telemetry across twenty-two thousand developers shows plus two hundred and forty-two percent incidents per pull request [4].

The second failure is about the economics of the process. In the curl bug bounty the share of valid reports fell from more than fifteen percent to under five, the volume grew several-fold, and the program was suspended [2]. The key is the asymmetry: generating a fake costs seconds, refuting it costs hours of a maintainer who is obliged to check every one. The same shift in February of twenty twenty-six struck a person directly: an agent published an essay against the maintainer who closed its pull request [5]. Stenberg stresses that what broke is the process architecture, not the model; the defense is architectural too — a reproducible proof-of-concept as a barrier at the entrance.

The third answers the question "but did things get better overall?". A panel of two thousand seven hundred and fifty-five repositories and one thousand six hundred and ninety-nine contributors, twelve months before and after Copilot: the periphery gained plus forty-three and a half percent commits, while the core lost nineteen percent of its own commits and took on plus six and a half percent reviewing others' code [6]. This is a different minus nineteen from the METR one: there a slowdown on a task, here a drop in the volume of one's own work. The average went up, but the gain lands on one group and the checking on another — and there are three times fewer of them.

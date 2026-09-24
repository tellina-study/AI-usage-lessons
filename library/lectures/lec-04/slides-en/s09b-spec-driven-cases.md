---
id: s09b
type: case_study
section: "Section 1. Requirements — the first artifact"
duration_min: 3
assertion: "Discipline applied in advance makes a measurable difference: where a spec-first workflow is built around a clear criterion, the result is fast and predictable; where AI is adopted without specifying intent, failure is a statistically expected outcome, not an exception"
learning_goal: "Contrast the two outcomes of the spec-driven discipline on concrete, honestly labelled figures; SDD as a named industry term"
learning_outcomes: [LO1, LO7]
chapter_ref: "§1.1 [for-slide-s08]"
references: [aws-kiro-lifesciences, sdd-terminology]
in_bucket: false
verify_day_of: true
visual_brief: >
  case_study, two equal columns (Visual Mass Balance 50/50). Left — an Ocean rounded box with the
  success accent (check-check gold): AWS Kiro, life sciences, spec-first workflow
  requirements→design→tasks→verification, "3 weeks / 3 developers to production" as a large number,
  and the honest label "MEDIUM confidence — a vendor-published case study, not an independent audit".
  Right — an Ocean rounded box with the warning accent (circle-x): "847 documented AI-agent
  deployments", "76% failed within 90 days", root cause a failure of specification rather than a
  technical inability of the model; the label "LOW-MEDIUM confidence — the sampling methodology is
  not disclosed, an illustration of the claim, not audited statistics". Below — a compact strip
  "SDD (Spec-Driven Development)": GitHub Spec Kit ~90k stars, ≥8 vendors by 2026 (convergence of the
  term). Gold callout — "discipline in advance → a fast, predictable result; AI without a specification
  of intent → a statistically expected failure, not a coincidence".
  All assets on this slide are language-agnostic; no image needed EN-specific regeneration.
interaction: none
---

# Visible content

## Title bar
Discipline in advance — a fast result; without it, failure is expected, not accidental

## Body
[Left — AWS Kiro, the discipline succeeding]

**AWS Kiro · life sciences (pharma/biotech, 2026).** A production-ready agent for therapeutic target discovery, built through a spec-first workflow: specification → step-by-step execution against milestones → verification against the spec.

**3 weeks, 3 developers** — not a drawn-out cycle of ad-hoc prompting.

*A vendor-published case study with the client anonymized — MEDIUM confidence, an illustration of the discipline, not generalizable statistics.*

[Right — the contrast, the discipline skipped]

**847 documented AI-agent deployments** (one aggregated review; the sampling methodology is not disclosed).

**76% failed within 90 days.** The root cause named by the source is a **failure of specification**, not an inability of the model.

*The sampling methodology is not disclosed — LOW-MEDIUM confidence, used only as an illustration of the direction of the claim, not as a measured fact.*

[Bottom — SDD as a term]
The industry calls this discipline **SDD (Spec-Driven Development)**: GitHub Spec Kit (~90k stars), and by 2026 at least **8** major tools with their own variant of the practice.

[Gold callout]
Discipline applied in advance is not a guarantee but a shift in probability: where a specification of intent is built around a clear criterion, failure becomes the exception rather than the statistically expected outcome.

## Speaker notes

Two examples side by side are not an accidental pairing but an illustration of one claim: the outcome depends not on whether AI was used, but on whether the spec-driven discipline was applied in advance. The published AWS case from life sciences describes a team that built a production-ready agent for therapeutic target discovery through a spec-first workflow — a specification, step-by-step execution against milestones, and verification of the result against the spec — and that fitted into three weeks with three developers [1]. The honest caveat: this is a vendor-published case study rather than an independently audited piece of research, and the specific client is anonymized. Hold it as a MEDIUM-confidence illustration of a discipline applied deliberately, not as a generalizable fact.

For contrast, the other side of the statistics, with the same caution about the source. One aggregated review names 847 documented AI-agent deployments and a share of seventy-six percent that failed within ninety days; the root cause it names is not a technical inability of the model but a failure of specification — the organization's intent was never specified precisely enough to be checkable at all. The sampling methodology is not disclosed by the source, so this figure cannot be cited as audited statistics, only as an illustration of the direction of the claim.

The pair of cases together is not a coincidence: where the discipline was built in advance around a clear criterion, the result is predictable and fast; where the decision to use AI was taken without specifying intent, failure is the statistically expected outcome. The industry calls this discipline SDD, Spec-Driven Development — GitHub Spec Kit and AWS Kiro set the mainstream meaning, and by 2026 at least eight major vendors had shipped their own variant of the practice [2].

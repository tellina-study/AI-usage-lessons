---
id: s24
type: process
section: "Section 3. Build / Launch"
duration_min: 2
assertion: "CC/CD versus CI/CD: a release is versioned by its level of agency, not its feature set — the agency ladder earns autonomy in stages"
learning_goal: "AI: launch as a transfer of control — CC/CD vs CI/CD, the agency ladder"
learning_outcomes: [LO2]
chapter_ref: "§3.4 [for-slide-s24]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  process/schema_pipeline: a 3-rung ladder (agency ladder) — v1 "high control/low agency" →
  v2 "proposes for approval" → v3 "automatic with fallback," each rung higher than the last,
  captioned "earned in stages."
source: "Reganti & Badam, Lenny's Newsletter (19 Aug 2025)"
---

# Visible content

## Title bar
Launch isn't "flip it on" — it's a staged transfer of control

## Body
[A 3-rung ladder: v1 high control → v2 approval → v3 fallback]

**CC/CD** (Continuous Calibration/Development) — versus the familiar CI/CD

- v1: routes, high control/low agency
- v2: proposes solutions for human approval
- v3: resolves automatically with fallback to a human

[Gold callout]
"If you haven't tested it under high control, you're not ready to give it high agency"

## Speaker notes

A notable reframing of the concept of "launch" for the AI era belongs to Aishwarya Reganti and Kiriti Badam: the CC/CD framework — continuous calibration and continuous development — set against the familiar CI/CD, because CI/CD assumes deterministic code that either passes tests or doesn't, and AI systems don't have that property.

The mechanics: the pre-launch phase — version releases by level of agency, not by feature set. Example: a support bot ships as version one — routes tickets, high control, low agency; version two — proposes solutions for human approval; version three — resolves automatically with fallback to a human. Build a reference dataset and design evals — applied metrics against the reference set before deployment. The post-launch phase — run evaluations on live data, analyze error patterns.

A named failure, stated plainly: if you haven't tested how the system behaves under high control, you're not ready to give it high agency. A bot that jumps straight to full autonomy risks a chain of failures that's hard to untangle after the fact. A real-world example: the agency ladder of GitHub Copilot and Cursor — from completions to blocks of code to entire pull requests, each rung unlocked only after the previous one proved reliable in practice. Major consultancies independently describe the same shift, but each one honestly names its own failure modes: bottleneck displacement, pilot proliferation, measurement gaps. The lesson for the launch phase: the consensus isn't "ship faster" — it's "rebuild the process around the agent while keeping human review at the critical checkpoints."

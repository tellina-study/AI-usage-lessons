---
id: s22
type: process
section: "Section 3. Build / Launch"
duration_min: 2.5
assertion: "You know feature flags/canary/rollback from engineering rollout — but here the same mechanics serve a product go/kill gate"
learning_goal: "BASE: MVP/BML + release mechanics + Stage-Gate go/kill; explicit callout for the stronger half"
learning_outcomes: [LO1]
chapter_ref: "§3.1, §3.2 [for-slide-s22]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  process: a horizontal flow "Feature flag → Canary → Staged rollout → Rollback" with
  connector arrows, over it a transparent callout layer "YOU KNOW THIS" crossing out the flow
  itself, pointing at a small separate "$ business decision kill/go" icon as the NEW content.
---

# Visible content

## Title bar
Same mechanics — but here the decision is to kill the product, not flip a flag

## Body
[Flow: Feature flag → Canary → Staged rollout → Rollback + a separate "business decision" icon]

**You know the primitives from CI/CD** — what's new here: whose decision they serve and by what criteria

- MVP (Ries) = learning, not shipping
- Stage-Gate go/kill (Cooper) — "a funnel, not a tunnel"; failure thresholds are written down as numbers in advance

## Speaker notes

Feature flag, canary, rollback are familiar to you from everyday engineering practice — you'll most likely skim the basic definitions. Hold onto one product-level distinction while you do, since it's the whole reason this section exists: here the same mechanics are built into a product go/kill gate, where the decision to kill a project is a business decision, not just a technical on/off flag.

A single thread runs through all of it: every practice trades a bit of launch speed for a limited blast radius. A feature flag separates deployment from release. Canary — the new version ships to a small share of traffic first. Staged rollout is a generalization of canary: one, ten, twenty-five, fifty, one hundred percent, with a go/no-go check at every step. Rollback — the ability to quickly return to the last working state.

Eric Ries's MVP is defined by learning, not shipping — a fast way to run the build-measure-learn cycle. Robert Cooper's Stage-Gate is five stages, each preceded by a go/kill/hold/recycle gate against criteria agreed in advance; its deliberate purpose is to force disciplined stop decisions early, before capital-intensive spending — "a funnel, not a tunnel." A go/no-go readiness gate for launch specifically requires: rollout phases with transition criteria, failure thresholds written down as numbers in advance, and a rollback plan with a named owner. Our cross-chapter device resurfaces here again — the falsifiable hypothesis, applied to a release decision. In the AI era, a new checklist line gets added: did it pass an eval gate against the reference dataset — the AI equivalent of a test suite.

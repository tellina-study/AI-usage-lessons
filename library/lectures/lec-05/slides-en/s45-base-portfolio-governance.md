---
id: s45
type: assertion_visual
section: "Section 6. Governance / ROI / finale"
duration_min: 2
assertion: "Portfolio governance is the same Stage-Gate go/kill, raised to the level of capital; an AI product's unit economics gains a new variable — cost per request"
learning_goal: "BASE: portfolio governance + unit economics + an operational financial KPI"
learning_outcomes: [LO1]
chapter_ref: "§6.1 [for-slide-s45]"
interaction: none
verify_day_of: false
partial_out_strict_in: true
meme_or_visual: >
  assertion_visual: a portfolio funnel — many incoming initiative-cards at the top, narrowing
  through several gate points to a few at the bottom (the same go/kill funnel from s22, but at
  the level of capital, not a single product). Next to it a small formula "cost/request vs
  value/request".
---

# Visible content

## Title bar
The same go/kill gate — but now it allocates capital across many initiatives

## Body
[Portfolio funnel: many cards → several gate points → few at the bottom]

**Portfolio governance** = Stage-Gate, raised to the level of capital

**An AI product's unit economics**: a new variable — **cost per request** vs value per request

[Ocean rounded box]
Financial KPI at pilot entry: "cut ticket cost from X₽ to Y₽ while CSAT ≥ Z; N tickets, M weeks, owner — Ivanov"

## Speaker notes

Portfolio governance is a classical product-management discipline: an organization runs not one product but a portfolio of initiatives, and decides which to fund, continue, or kill by criteria agreed in advance. A direct descendant of Stage-Gate, raised from the level of a single product to the level of a portfolio.

Unit economics for an AI product gains a new variable — cost per request: model calls are not free, and a product where cost per request exceeds value per request is economically unviable, no matter how impressive the demo. For classical SaaS, the marginal cost of serving one more user is close to zero; for an AI product, every call costs real money, and cost per request does not fall with scale the way classical SaaS cost did.

Let's make the requirement operational. A bad KPI is "improve support efficiency" — not measurable, direction unclear, just like Kohavi's time-on-site. A good one, written down before the pilot: we believe AI triage will cut cost per ticket from X rubles to Y while not degrading CSAT below threshold Z; we'll test it on N tickets over M weeks; the owner is a specific person tracking it weekly. This is simultaneously an OEC, guardrail metrics, and a threshold fixed in advance with a date and an owner — the same apparatus as the error budget and Stage-Gate, applied to the decision of whether to keep funding an AI initiative. Why this is the capstone's base: the macro-failure on the next slide will show that the root of most failures is not "the model isn't good enough," but the absence of exactly this criterion at pilot entry.

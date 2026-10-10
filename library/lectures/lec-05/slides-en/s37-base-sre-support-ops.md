---
id: s37
type: process
section: "Section 5. Support and operations"
duration_min: 1.5
assertion: "The \"system\" half: Google attributes about 70% of outages to its own changes, so the allowed number of failures is agreed in advance — a 99.9% objective on a million requests gives a budget of 1,000 errors — and the speed it is spent at is watched on two windows: 2% of the monthly budget burned in an hour wakes the on-call, 5% in six hours is a task for working hours"
learning_goal: "The \"reliability\" half in the scope the whole section leans on: the error budget as a number, and the two speeds it is spent at"
learning_outcomes: [LO1]
chapter_ref: "§5.1"
interaction: none
protected: true
verify_day_of: false
partial_out_strict_in: true
revision: >
  issue #212, EN parity pass — the EN twin still carried the pre-Stage-6 slide ("A 200 OK
  response says nothing about whether the model is hallucinating": an SLI→SLO→error-budget
  flow plus a struck-through HTTP 200 band), which is where the RU side had already been
  rebuilt on owner-review 2026-10-01 ("slide 37 — we start telling the SRE story from the
  middle"). The notion of reliability engineering moved out to the new preceding slide
  s36c together with the frame of the section; this slide now occupies one defined place
  inside that frame — the "system" half — and is marked with a teal tag so the place reads
  without words. The "why this work exists" block was compressed (its framing part went to
  s36c) and rewritten: 70% is given as a share of ALL outages with the remainder named,
  that is, with a baseline. The two burn speeds got their numbers from the Google SRE
  Workbook (2% of the monthly budget in an hour, 5% in six hours) — before, the two windows
  differed only in shape. The bridge at the end was rewritten: it leads to the "people"
  half and to AI inside it (the section's subject turned round by owner-review).
meme_or_visual: >
  process: a teal tag "the \"system\" half" under the title. At the top, a "why" band (the
  share of outages caused by changes, with the remainder named). Below it, on the left, a
  chain "indicator → objective → error budget" with the last block unfolded into a number:
  a million requests, 99.9%, 1,000 errors; under it a teal rule band. On the right, two
  horizontal window scales of different length, LABELLED and each carrying the number of
  budget burned: a short one with a sharp peak, a long one with a shallow rise. At the
  bottom, a gold band bridging to the "people" half.
source: "Google SRE Workbook — error budget policy: changes cause ≈70% of outages; a service with 1,000,000 requests in the period at a 99.9% objective has a budget of 1,000 errors; the multiwindow burn-rate alerting table: a burn rate of 14.4 over a 1-hour window = 2% of the monthly budget, a burn rate of 6 over a 6-hour window = 5%"
---

# Visible content

## Title bar
Error budget: the allowed number of failures, counted ahead

## Badge
[Teal tag under the title]
the "system" half

## Body
[A "why" block on top; below it the chain unfolded into a number; on the right two labelled observation windows]

**WHY THIS WORK EXISTS.** Google attributes about 70% of the outages of a running system to the team's own changes: a deploy, a prompt edit, a model version change. The rest is split between hardware failures and external causes. So failures come from the work the team does every day, and their allowed number is worth agreeing in advance: otherwise "faster or more reliable" is settled after the incident, for whoever is louder.

**Service level indicator (SLI) → service level objective (SLO) → error budget.** The indicator is a measure of the service's behaviour as the user sees it. The objective is the bar on that indicator. The budget is what is left: a 99.9% objective on a million requests in the period gives **1,000 errors** — what is left to spend.

**Rule:** budget exhausted — shipping new features stops. The speed-versus-reliability conversation happens before the incident, and it has a basis that rhetoric cannot argue with.

**Two alert windows, always both.** The short one catches a sharp spike: **2% of the monthly budget** burned in an hour — at that rate it is gone in two days, page the on-call now. The long one filters noise and catches a slow slide: **5% in six hours** — a task for working hours. On the short window a slide is indistinguishable from a random spike.

[Gold callout]
All this is built for a system where a request either works or it does not. A 200 — "delivered successfully" — arrives even when the model confidently makes things up. Next, the other half of quality: people, their tickets, AI in that work.

## Speaker notes

The "system" half, and we take from it exactly what the whole section leans on.

First, the reason this bookkeeping exists at all. Google went through its own outages and got a figure: about seventy percent of the failures of a running system are caused by changes the team itself makes — a deploy, a prompt edit, a model version change. The remaining thirty are split between hardware failures and external causes. The meaning of the figure is in the proportion: the source of most outages is the activity the team is busy with every working day. From there a direct consequence. If nobody agrees in advance how many failures are acceptable, the "faster or more reliable" argument will be settled after every incident, in favour of whoever is louder. The whole discipline exists so that this argument happens beforehand and on numbers.

The number itself is built in three steps. The service level indicator is a quantitative measure of the service's behaviour as the user sees it; in English sources it is shortened to SLI. The objective is the team's internal bar on that indicator, the SLO. The error budget is what is left: one minus the objective. A service with a million requests in the period, at an objective of ninety-nine point nine percent, has a budget of one thousand errors. That is a concrete remainder, and it is spent, and the whole value is in that: budget exhausted — shipping new features stops.

The second element is the speed it is spent at, and that is watched on two windows at once. The short one: two percent of the monthly budget burned in an hour. Simple arithmetic — at that rate the monthly budget will be gone in about two days, and that is grounds for waking someone now. The long window catches something else: five percent in six hours. The rate is noticeably lower, it does not justify a night call, but the slide is real, and it is a task for working hours. Alone the windows are blind: on the short one a slow slide is indistinguishable from a random spike, and the long one sleeps through a sharp jump.

And where we go from here. Everything listed is built for a system where a request either succeeds or it does not. A two hundred — "response delivered successfully" — arrives even when the model is confidently making things up. That half of quality will be needed again later; right now we move to the second one: to people, their tickets, and to what AI does with that work.

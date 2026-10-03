---
id: s24a
type: schema_matrix
section: "Section 3. Build and launch"
duration_min: 2.5
assertion: "Autonomy is handed to a system by levels rather than all at once; the move up to the next level is opened by evidence, not by elapsed time and not by good behaviour"
learning_goal: "Practice 1 of the phase: a release is versioned by the level of trust, and the move between levels has a checkable condition"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§3.4"
verify_day_of: true
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, the forms brought together after the methodology review of 2026-09-30: all
  twelve practice cards are reduced to ONE form — WHAT IT IS (the way in for a newcomer) /
  HOW IT WORKS (numbered steps + a labelled diagram) / WITH AI AND WITHOUT (rule R6) /
  WHERE IT BREAKS. There are no "artefact", "criterion" or "building on what has been
  covered" blocks, and no questions to the room. The earlier mismatched fourth blocks
  ("SCALE", "DIAGRAM", "PRACTICES 2026", "TOOLS 2026") are removed: diagrams live inside
  HOW IT WORKS, and the current tools in the "WITH AI" column.
  owner-review 2026-10-01: the example was reworked. A speculative support bot was replaced
  by a measured case — RADAR at Meta, where the level is set by a number (a risk threshold),
  the raising of the threshold is documented, and the consequences are measured against a
  named baseline. A boundary was added that separates this practice from the anti-pattern of
  Lecture 4 (§3.7/§5.2): RADAR has a deterministic check at the end of its chain, and merging
  on the verdict of an AI reviewer is a different thing. The orphaned reference to "the
  golden set on the next slide" was rewritten: the next slide is now about mutation testing.
meme_or_visual: >
  schema_matrix, the single practice card: WHAT IT IS · HOW IT WORKS (four numbered steps on
  the left + a labelled diagram on the right: three autonomy levels with arrows) · WITH AI
  AND WITHOUT (in the "WITH AI" column — the measured RADAR case with its numbers) · WHERE
  IT BREAKS (gold).
source: "Aishwarya Reganti (applied AI lead, Amazon) and Kiriti Badam (member of technical staff, OpenAI), 19 August 2025 — their review of more than 50 deployments at OpenAI, Google and Amazon · Meta RADAR (arXiv 2605.30208): 535,000 changes, the risk threshold moved from the 25th to the 50th percentile, 60.31% auto-approval, rollbacks 1/3 and production incidents 1/50 of the ordinary path"
---

# Visible content

## Title bar
The autonomy scale — the right to decide is handed over in parts

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

A feature is released by autonomy levels — from a hint, to a proposal that a person confirms, and on to a decision the system takes itself (the levels on the right). **A version here means the autonomy level the system has earned.**

**HOW IT WORKS**

1. Each level is **a separate release**: its own circle of users, its own set of observed signals, its own way to stop.
2. The move up is opened by **evidence written down as a number before the run**: the system copes with the cases the new level entrusts to it. The calendar does not count as grounds.
3. The evidence has to hold **across repeated attempts**. A single success does not give it.
4. It is set out in advance **how to put the system back a level**: who decides, on what signal, and within what time.

[Labelled diagram on the right: it hints (a person decides) → it proposes a solution (a person confirms) → it decides itself (and hands the hard cases back to a person); caption "the autonomy scale: product versions have nothing to do with it"]

**WITH AI AND WITHOUT**

| WITHOUT AI — rights have long been handed out in parts | WITH AI — the level is confirmed by measurement |
|---|---|
| To people and to automation alike: a newcomer is first allowed to watch, then to propose, then to decide alone. The level rests on time served without complaints. | A system gains no experience. Meta moved the risk threshold at which a change is merged without a person from the 25th percentile to the 50th: **60.31%** are approved automatically. Their rollbacks are **three times rarer**, and production incidents **50 times rarer**, than on the ordinary path (535,000 changes). |

[Gold callout — WHERE IT BREAKS]
"The operator has not corrected anything in ages" is not evidence: **an absence of remarks is an absence of measurement.** Automatic approval rests on **a deterministic check at the end of the chain**; merging on the verdict of an AI reviewer removes the only control there is. And the irreversible and the expensive are never raised to the top level: a binding offer to a customer, the deletion of working data, a release to everyone at once — those sit behind a hard rule placed above the model.

## Speaker notes

The word "launch" was redefined for the AI era by Aishwarya Reganti and Kiriti Badam, generalising from more than fifty deployments. Their point: the familiar pipeline assumes deterministic code, which either passes its tests or does not, and a system built on a model does not have that property. So a release has to be versioned by the level of control.

The measured example is RADAR at Meta — Risk Aware Diff Auto Review — the system that decides which code change can be merged without a person. The level here is set by a number: a risk threshold. A change travels down a funnel — provenance, static rules, a trained risk score, an AI review, and a deterministic check at the end. When the threshold was moved from the twenty-fifth percentile to the fiftieth, the share approved automatically reached sixty per cent. And here is what turns that into evidence: rollbacks on those changes turned out to be three times rarer, and production incidents fifty times rarer, than on changes down the ordinary path. The baseline is named, and the sample is five hundred and thirty-five thousand changes.

The verbatim wording of the failure, from the same review: if you have not checked how a system behaves under high control, you are not ready to give it high autonomy. A bot that jumps straight to the top level risks a chain of failures that is then hard to untangle — full autonomy removes the cheap checkpoints that a staged rollout exists for.

What the slide is silent about, and what is worth saying. The level of a feature, the date it was raised, the name of whoever decided and the rollback path live in a versioned file next to the code; the team's memory does not count as such a file — that is a continuation of the conventions from the last lecture. And the link to the next slide: the threshold that opens a level needs checking itself. If the set of checks you judge readiness by has never once caught a deliberately planted fault, its green colour proves nothing.

And the boundary that cannot be softened. Keep the difference from the last lecture in mind: there we said that handing the merge to an agent on the verdict of an AI reviewer means removing the only control there is. In RADAR the last word stays with a deterministic check, and the model supplies only one of the passes. And decisions that are irreversible by their nature are never raised to the top level: that is a structural limit, and the next generation of models will not lift it.

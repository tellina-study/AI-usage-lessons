---
id: s24c
type: schema_matrix
section: "Section 3. Build and launch"
duration_min: 2.5
assertion: "The blast radius is set by the team's decision before launch, and is not something found out afterwards: the share of users grows in stages with the stop signals named in advance, and the rollback path is written down and tested beforehand"
learning_goal: "Practice 3 of the phase: staged rollout and a rollback path written down in advance — the very practice both cases in the section put to the test"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§3.2, §3.4"
verify_day_of: false
partial_out_strict_in: true
interaction: none
protected: true
note: >
  issue #212, bringing the forms together after the methodological roast of 2026-09-30: all
  twelve practice cards are brought to ONE form — WHAT IT IS (an entry point for a newcomer) /
  HOW IT WORKS (numbered steps + a labelled diagram) / WITH AI AND WITHOUT (rule R6) /
  WHERE IT BREAKS. There are no "artefact", "criterion" or "link to what has been covered"
  blocks and no questions to the room. The previous mismatched fourth blocks ("SCALE",
  "DIAGRAM", "PRACTICES 2026", "TOOLS 2026") have been removed: diagrams live inside
  HOW IT WORKS, and the current tools live in the "WITH AI" column.
meme_or_visual: >
  schema_matrix, one practice card: WHAT IT IS · HOW IT WORKS (three numbered steps on the left
  + a labelled diagram on the right: four rollout stages and a gold "rollback path" arrow
  running bottom to top) · WITH AI AND WITHOUT · WHERE IT BREAKS (gold).
---

# Visible content

## Title bar
Staged rollout and the rollback path — how to set the cost of an error in advance

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

Something new is switched on gradually: first for a narrow circle, then wider. And the way to bring it all back is agreed in advance. **The blast radius — how many people get hurt if the new thing turns out to be bad — is set by the team itself, before launch.**

**HOW IT WORKS**

1. **Rollout stages** — which shares of the audience we go through, and in what order.
2. **Stop signal** — what is watched at each stage and what degree of worsening halts the move forward; with no signal named in advance, "it got worse" is argued about endlessly.
3. **Rollback path** — who takes the decision to go back, how long that takes, and whether anyone has checked that going back works at all.

[Labelled diagram on the right: narrow circle → small share → part of the audience → everyone, and a gold "rollback path" arrow running bottom to top; caption "the share of the audience grows in stages; the way back is written down before launch, not at the moment of the failure"]

**WITH AI AND WITHOUT**

| WITHOUT AI — the practice is several decades old | WITH AI — only the speed of the stages changes |
|---|---|
| Staged rollout and rollback were invented long before AI and are built in exactly the same way. **There is nothing to invent again**, you take what is already there. | An ordinary feature shows itself through errors and latency straight away, while worsening answers only come out at volume: every stage needs **hours of watching, minutes are not enough**. |

[Gold callout — WHERE IT BREAKS]
A rollout limits the radius, but **it does not replace the decision**. A long pilot on a tiny share that keeps failing has run into the ceiling of the approach; "a little more data" will not cure it. The opposite error is just as real: **the maturity of the product gives no right to skip the pilot** — it raises the cost of skipping it. And a rollback path that is written down but never once tested stays an intention.

## Speaker notes

This is the oldest practice in the section and the only one an engineer already uses: the feature flag, the canary release, switching on in stages, going back to the previous version. The novelty is elsewhere: here these primitives serve a product decision, and for a feature built on a model they are also set up differently.

A word about pace is worth saying. For an ordinary feature a rollout stage lives for minutes: errors and latency are visible straight away. For a feature built on a model the quality signal is noisy, and a stage lives for hours — worsening answers only come out at volume. A team that carries its habitual rollout pace over to a generative feature follows the procedure to the letter and sees nothing in the time it allows itself.

About the stop signal. The most common mistake is to roll out in stages without naming in advance what counts as worsening. Then at every stage an argument starts about whether it really did get worse, and that argument is won by whoever wants the release more. A signal named before the switch-on takes the argument away — exactly the same mechanics as a threshold written down as a number before the start.

About the rollback path. Describing it is not enough — it gets tested. A way back that nobody has tried reveals its problems at precisely the moment it is needed urgently. It is worth naming separately who exactly takes the decision to go back: if that decision has no owner, it falls by default to whoever is on night duty, and is taken on how they feel, with no signal at all. This is also where the lever for switching the feature off entirely is kept — a separate control that turns the feature off without waiting for the causes to be worked out.

Let me say plainly what comes from AI here. The practice itself is classical: staged rollout and rollback were invented long before models, and they are built in exactly the same way. Only the speed of the stages changes: an ordinary feature shows itself through errors straight away, while worsening answers only come out at volume, so every stage needs hours of watching.

And the limit that ties this slide to both of the cases ahead. A rollout bounds the cost of an error, and it does not take the decision for the team. A long pilot on a small share that keeps failing is a signal about the ceiling of the approach. It is not a request for "a bit more time". And the mirror image: the maturity of the main product is no reason to skip the pilot. Both cases on the next two slides are two different errors about one axis: one skipped the pilot altogether, the other went through it honestly and read the signal correctly.

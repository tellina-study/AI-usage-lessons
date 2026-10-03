---
id: s30a
type: schema_matrix
section: "Section 4. Measurement"
duration_min: 3
assertion: "Pre-registration is a note made before the experiment starts: it does not make the experiment right, it takes away the chance to pick the success criterion once the result is already visible; for a conversational product it gains a unit of assignment and a set of quantities in place of one"
learning_goal: "The practice of Section 4: what pre-registration is in plain words, what an AI product adds to it and where it stops helping"
learning_outcomes: [LO1, LO2, LO6]
chapter_ref: "§4.2"
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
source: "Ronny Kohavi, Diane Tang, Ya Xu (2020) · pre-registration in clinical research (ICMJE, 2005) · randomise by user, not by request, and a set of quantities in place of one for a conversational product — §4.2 of the chapter · illustrative calculation of 31,200 per group"
meme_or_visual: >
  schema_matrix, one practice card: WHAT IT IS · HOW IT WORKS (three numbered steps on the left
  + a labelled diagram on the right: a time axis where the mark for the note stands to the left
  of the first data point) · WITH AI AND WITHOUT · WHERE IT BREAKS (gold, with two labelled
  bars on the right, "needed per group" and "available per week"). No decorative shapes.
---

# Visible content

## Title bar
Pre-registration: the decision is written down before the result is seen

## Body
[what it is → how it works → with AI and without → where it breaks]

**WHAT IT IS**

A short note made **before** the experiment is launched: what exactly we measure, what result counts as success, when we stop. The practice came from medicine — there the protocol is registered before patients are recruited, otherwise the journal will not take the paper.

**HOW IT WORKS**

1. **Four things are written down before launch:** which quantity we take as the decision metric and which way it has to move; what we watch as a guardrail metric; what effect size counts as meaningful and how many observations it needs; under what condition we stop.
2. **The note is put where time is recorded** — with a date and an author. The whole mechanism is in that: the timestamp stands earlier than the first result.
3. **After launch the note is not rewritten** — the decision taken and its date are appended to it.

[Labelled diagram on the right: a time axis, the mark "note made" to the left of the mark "first result", the gap labelled "the success criterion was written down earlier than the first result". Below it: three traps — stop on a lucky point, trawl through metrics, move the threshold — **every one of them needs the success criterion to be choosable after the result.**]

**WITH AI AND WITHOUT**

| WITHOUT AI — the practice comes from medicine | WITH AI — what has to be written down on top |
|---|---|
| One decision metric, the sample size, the stopping rule — written down in advance. That is how clinical protocols and ordinary product experiments work. | **Randomise by user, not by request:** in a dialogue one person otherwise lands in both groups at once. And **several quantities at a time**: a score for the quality of the answer, the share of re-asks and corrections, the cost of a contact. |

[Gold callout — WHERE IT BREAKS]
**Pre-registration does not make an experiment right — it makes wrongness visible.** It does not cure the novelty effect: that needs a separate group held back from the change. And it is powerless where there are physically not enough observations: the honest way out is to change the question or the method; the sample will not help here.

[Labelled bars on the right: "needed per group" 31,200 against "available per week" 5,000 — more than three months of waiting for an answer]

## Speaker notes

Let me start with what this even is, because the word sounds heavier than the practice. Pre-registration is a short note made before the start: what we measure, what we count as success, when we stop. It comes from medicine: the protocol of a clinical study is registered before patients are recruited, and without such registration the leading journals simply do not publish the result. The reason is exactly ours.

Four things get written down. First — which single quantity is the basis of the decision and which way it has to move; the direction cannot be added afterwards, and that field is precisely what catches the trap of a metric whose meaning was never agreed. Second — what we monitor as a guardrail metric. Third — what effect size we count as meaningful and how many observations it needs. Fourth — under what condition we stop. Then the note is put where records have a date and an author: into version control. The whole mechanism is in that — the timestamp stands earlier than the first result. After launch it is not rewritten; the decision is appended to it.

Why this works is worth saying out loud: it sounds like paperwork and works like an engineering practice. The three most common traps — stopping on a lucky point, trawling through metrics and picking the one that fired, moving the significance threshold — all need one and the same thing: the success criterion has to be choosable once the result is visible. If it is written down earlier, there is nothing to choose from. This is not about honesty, it is about order in time.

Now what has to be added when the thing under test is a product built on a model. First — the unit of assignment. In a dialogue one person over one conversation otherwise lands in both groups at once, and the independence assumption falls apart; so you randomise by user, not by the separate request. Second — several quantities get written down at once: a score for the quality of the answer, the share of re-asks and corrections, the cost of a contact. For a product that answers differently every time, no single quantity on its own answers the question of whether it worked.

And the limit. Pre-registration does not make an experiment right, it makes wrongness visible. It does not cure the novelty effect. And it is powerless where there are not enough observations: thirty-one thousand per group with five thousand a week is more than three months of waiting. The honest way out is to change the question or the method; the sample will not help here.

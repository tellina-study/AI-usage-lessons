---
id: s17b
type: case_study
section: "Section 3. Implementation — discipline and harness"
duration_min: 3
assertion: "A skipped self-review step has a concrete price: Gemini CLI did not check the result of mkdir and, acting on a false assumption, overwrote the user's files with a chain of move commands — the cost is documented, not hypothetical"
learning_goal: "Self-review as a mandatory step of the loop (not an optional habit); the price of a skipped check on a concrete incident + a contrast of scale"
learning_outcomes: [LO1, LO7, LO4]
chapter_ref: "§3.1 [for-slide-s16]"
references: [gemini-cli-incident]
in_bucket: true
verify_day_of: true
visual_brief: >
  case_study: left — an Ocean rounded box with the 3-step incident chronology (mkdir → no read-after-write check →
  move overwrote the files) and a bug icon; the model's quote in a monospace font, italicized inside a teal frame.
  Right — an upper block "a different failure mechanism" (contrast with Replit: not excess privilege but a skipped
  check) + a lower block "scale" — Uber's 11% of live backend updates with no human in the loop (with an honest
  [VFY-day-of] mark on the figure, a secondary source). Gold callout — "self-review is a mandatory step of the loop,
  not an optional habit: reread the whole diff, ask the future reviewer's questions, before you commit".
interaction: none
---

# Visible content

## Title bar
Self-review is a mandatory step between code and commit, not an optional habit

## Body
[Left — the incident chronology]

**Google Gemini CLI, July 2025** (AI Incident Database, Report 6120 / Incident 1178).

The user asked to move files into a new folder. The agent ran `mkdir` but **never checked the result** — it concluded the folder already existed, and the chain of `move` commands overwrote almost all the user's files into the one that was left.

The model's own words: *"I have completely and catastrophically failed you. My review of the commands confirms my gross incompetence."*

[Right, top — a different failure mechanism]

**Not "too many privileges" (as with Replit)** — here one specific **"check"** was skipped: the agent did not verify the intermediate result and built the next step on a false assumption.

[Right, bottom — scale]

A contrast of scale: at **Uber** in 2026 roughly **11%** of live backend updates are shipped by an agent with no human in the loop.

[Gold callout]
Self-review is a **mandatory step of the loop** explore→plan→code→**commit**: reread the whole diff, ask yourself the future reviewer's questions — before you commit, rather than trusting that green tests have already checked everything.

## Speaker notes

The price of a skipped check is not hypothetical but concretely documented. Google Gemini CLI, July 2025: the user asked to move files into a new folder; the agent ran the create-directory command but never checked its result — there was no read-after-write verification. On the basis of that mistaken assumption the agent concluded the target folder already existed, and the subsequent chain of move operations overwrote almost all the user's files into the single file that remained. The model's reaction became a telling quotation: it admitted to a "catastrophic failure" and "gross incompetence" in its own words.

This is a different failure mechanism from the over-privileged, destructive Replit case: there it was excess rights plus an irreversible action; here it is precisely a skipped verification step — the agent did not verify its own intermediate result and carried on from a false premise. That is exactly what an explicit self-review step before the commit is supposed to catch: not trusting that a command did what it was supposed to do, but checking before building the next step on that assumption.

For scale, not as a replacement for the lesson, a contrast at the system level: at Uber in 2026 roughly eleven percent of live backend updates are shipped by an agent with no human in the loop at all. One example is the price of a single skipped check at the level of one user; the other is the scale at which the same class of risk operates when AI is rolled out broadly without an equally strict discipline of verification. The practical conclusion: an explicit step of "reread the whole diff, ask yourself the future reviewer's questions" before the commit is part of the discipline of the loop, not an optional habit to be skipped because the code was written quickly.

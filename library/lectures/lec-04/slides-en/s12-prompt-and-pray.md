---
id: s11
type: case_study
section: "Section 1. Requirements — the first artifact"
duration_min: 3
assertion: "prompt-and-pray is not a \"bad tool\" but a skipped discipline: the model silently fills in requirements with defaults; the root of the failure is the essential complexity of intent (Brooks), which is not delegated"
learning_goal: "[SI] The prompt-and-pray failure + ironic illustration; lesson human-intent = essential complexity; overclaim \"spec=truth\""
learning_outcomes: [LO1, LO7, LO4]
chapter_ref: "§1.3, §1.4 [for-slide-s10]"
references: [grove-new-code, emperors-new-code]
in_bucket: true
verify_day_of: false
visual_brief: >
  case_study: left — an ironic themed illustration (#258) for prompt-and-pray:
  find a CC/embeddable one in Phase 6 — e.g. a developer with fingers crossed / "praying" over a terminal,
  OR an iceberg (visible "works in the demo" / underwater "dozens of unstated assumptions"). Tag the visual_brief
  for Phase 6 acquisition (6-tier). Right — the case breakdown "build a booking system" in an Ocean rounded box:
  silently filled-in decisions (booking in the past? overlap? time zones?) + "the code is correct relative to the model's GUESS".
  Bottom — the second failure: overclaim "spec = truth" → "I'll regenerate the code" = a nondeterministic lottery; "the code remains the source of truth".
  Gold — "the bug is not in the code — it's in the unchecked requirement". Lucide icons.
interaction: none
---

# Visible content

## Title bar
prompt-and-pray: the bug is not in the code, but in a requirement no one checked

## Body
[Left — an ironic illustration for "prompt-and-pray" (visual_brief for Phase 6)]

**prompt-and-pray** — give the model one vague prompt ("build a booking system") and hope. This is a **skipped discipline**: no spec artifact, no human checkpoint between intent and code.

[Right — the case breakdown, Ocean rounded box]

The model silently fills in dozens of decisions: book in the past? what happens on overlapping bookings? who cancels someone else's booking? time zones? — for each it takes a **plausible default**. The system "works" in the demo and breaks on the first real conflict.

The insidious part: the code is **correct** relative to what the model assumed. The bug is not in the code — it's that **no one checked** the assumptions; you have to fix not the implementation but the unstated requirement, and that isn't visible in the code.

[Second failure — overclaim "spec = truth"]
The opposite extreme: "the spec = the single truth, you don't need to read the code." But the spec **under-specifies** behavior; "I'll regenerate from the spec" gives not the same product but a new guess. **The code remains the source of truth** — the spec-driven practitioners themselves acknowledge this.

[Gold callout]
The bottleneck is not the model's ability to write code, but the **precision of stating intent** (essential complexity, Brooks). The alternative is not "no AI" but restoring the **human checkpoint**: a spec that a human read and accepted before code.

## Speaker notes

Let's examine the main failure mode of the requirements phase as a separate block. The beginner's anti-pattern is prompt-and-pray: give the model one short, vague prompt "build me a booking system" and hope for the result. This is not a "bad tool" but a skipped discipline: no spec artifact, no human checkpoint between intent and code. Without a specification, the model is forced to silently fill in dozens of decisions — can you book in the past, what to do when two bookings overlap, who is allowed to cancel someone else's booking, how to handle time zones — and for each it takes a plausible default that looks reasonable but may not match what the organization needs.

And here is the insidious part: the system works in the demo and breaks on the first real booking conflict, while the code is correct relative to what the model assumed. The bug is not in the code, but in the fact that no one checked the assumptions. Debugging doesn't help here — you have to fix not the implementation but the unstated requirement, and that isn't visible in the code. The diagnosis the spec-first methodologists themselves gave: the bottleneck is not the model's ability to write code, but the precision of stating intent [1], that is, the essential complexity per Brooks, which is not delegated to the tool [1].

Hence the right alternative to prompt-and-pray is not "don't use AI," but restoring the human checkpoint: requirements before code, a specification that a human read and accepted before anything is generated [2]. Exactly this technique — instead of "prompt and pray," the model first asks clarifying questions and surfaces unstated assumptions, and the human aligns on them before generation [2]. The difference between prompt-and-pray and discipline is not "with AI or without AI," but "the human checked the intent before code or didn't."

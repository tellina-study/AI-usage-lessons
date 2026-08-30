---
id: s39
type: assertion_visual
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "The checklist 'when AI yes / when no' by phase — a distribution of the burden of proof; irreversibility/impact is the veto axis; Anthropic -17% (quiz 50% vs 67%, n=52) — when the goal is 'to learn', delegating generation is harmful"
learning_goal: "[SI] Checklist §7.4 (LO4 entry) + Anthropic -17% junior; a task without timing/methodology"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.4, §7.5 [for-slide-s39]"
references: [anthropic-skill-formation]
in_bucket: true
verify_day_of: true
visual_brief: >
  assertion_visual: left — the 8-item checklist in an Ocean rounded box (Lucide checkmark icons), irreversibility/impact marked as the VETO axis (gold marker).
  Right — the Anthropic -17% plate (a number with a baseline, the main one): RCT, 52 developers learning an unfamiliar library — the group with AI scored 50% on the quiz vs 67%
  without AI (~-17 pp); the split: those who delegated generation dropped, those who asked about concepts did not; the speed-up is NOT significant. The mechanism — a skill forms through active retrieval (retrieval practice).
  Gold — "-17% for the junior + irreversibility = the veto axis". NO timings on the slide, NO "think-pair-share", NO "mastery — Seminar 4" (these — in the speech Phase 9, not on the slide). Source references — inline right at the material (definition/claim/recommendation), NOT in a bottom footer; small and muted: Anthropic (Shen & Tamkin, 2026).
interaction: none
---

# Visible content

## Title bar
The checklist "when AI yes / when no" + what it means personally for you

## Body
[Left — the 8-item checklist in an Ocean rounded box]

**Checklist before the task:**
1. Which lifecycle **phase** is this? (the map says at once whether the benefit is strong)
2. Can it be solved **without AI** (deterministically)? If yes — do not add AI
3. **Essential or accidental** complexity? Essential → the human is required
4. Is the consequence **reversible**? Irreversible → hard human gate, autonomy ceiling down — the **veto axis**
5. Is there a **machine oracle** (test, SAST, run)? No → do not trust without review
6. Are **secrets / untrusted content** involved? Yes → least-privilege + isolation + egress
7. Who **reviews and merges**? Merge and accountability — always the human
8. Is the goal an **artifact or a skill**? A skill → do not delegate the generation

[Right — what this means personally for you]
**Anthropic** (RCT, 52 developers learning an unfamiliar library): the group with AI scored **50% vs 67%** without AI on the quiz (~-17 pp). Those who **delegated generation** dropped; those who **asked about concepts** ("how it works, why") show no degradation. The speed-up, meanwhile, is statistically **not significant**.

[Gold callout]
The checklist is a **distribution of the burden of proof**, not "always less AI": for a suitable task it will deliberately lead to high autonomy. Irreversibility and impact are the **veto axis**. In learning, the very act of going through the task is not delegated: AI's role is to explain and check, but you do the writing.

## Speaker notes

Let us fold the whole lecture into a working checklist — it applies to a dev task before you hand it to AI. First item: which phase is this — the map says at once whether the benefit is strong here. Second: can it be solved without AI deterministically — if yes, do not add AI, this is a direct transfer of the criterion from Lecture 3. Third: essential or accidental complexity — essential means the human is required. Fourth, and special: is the consequence reversible — an irreversible one requires a hard human gate, and this is the veto axis: one high irreversibility outweighs everything else. Fifth: is there a machine oracle — no means do not trust the output without review. Sixth: are secrets or untrusted content involved — yes means least privilege, isolation, egress control. Seventh: who reviews and merges — merge and responsibility are always the human. Eighth: is the goal an artifact or a skill. It is important to understand: the checklist is a distribution of the burden of proof, not a rule "always choose less AI": for a suitable task it will deliberately lead to high autonomy, for an unsuitable one it will explicitly say "lower" or "not AI".

Now the failure that is critical personally for you as students. Anthropic ran a randomized study: fifty-two developers learning an unfamiliar library, some with AI, some without, then a comprehension quiz; the group with AI scored on average fifty percent versus sixty-seven without AI — about minus seventeen points, roughly two letter grades [1]. The split is key: those who delegated generation, "write it for me", dropped more; those who asked about concepts, "how does this work, why so", showed no significant degradation [1], and the speed-up meanwhile was not statistically confirmed. A skill forms through actively retrieving the solution from memory, and by asking AI to write the code you get the right result while bypassing the effort that forms the skill. This is the perception gap in a personal dimension: it feels like "I figured it out", while the measured understanding is lower. For a student the cost of delegation is higher than for the METR expert: the expert loses time on the task, the learner loses competence. The conclusion of the eighth item: in learning, the very act of going through the task is not delegated — AI's role is to explain and check, but the writing must be yours.

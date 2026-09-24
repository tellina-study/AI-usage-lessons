---
id: s39
type: assertion_visual
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "Eight questions decide not 'apply AI or not' but how, where and with what control to apply it: the checklist issues a mode — high autonomy for a suitable task, a lower ceiling and mandatory measures for an unsuitable one; irreversibility/impact is the veto axis; Anthropic -17% (quiz 50% vs 67%, n=52) — when the goal is 'to learn', delegating generation is harmful"
learning_goal: "[SI] Checklist §7.4 as a setting of the mode and the level of autonomy (LO4 entry) + Anthropic -17% junior; a task without timing/methodology"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.4, §7.5 [for-slide-s39]"
references: [anthropic-skill-formation]
in_bucket: true
verify_day_of: true
visual_brief: >
  assertion_visual: left — the 8-item checklist in an Ocean rounded box (Lucide checkmark icons),
  irreversibility/impact marked as the VETO axis (gold marker).
  Right — the Anthropic -17% plate (a number with a baseline, the main one): RCT, 52 developers learning an
  unfamiliar library — the group with AI scored 50% on the quiz vs 67% without AI (~-17 pp); the split: those
  who delegated generation dropped, those who asked about concepts did not; the speed-up is NOT significant.
  The mechanism — a skill forms through active retrieval (retrieval practice).
  Round-6 (block 5, owner note p56): the eight questions are kept but rephrased as a setting of the mode rather
  than a binary barrier — the paired edit to s39 (chapter-part5 §7.4: "a distribution of the burden of proof,
  not always choose less AI").
  Gold — "-17% for the junior + irreversibility = the veto axis". NO timings on the slide, NO "think-pair-share",
  NO "mastery — Seminar 4" (these belong in the speech, Phase 9, not on the slide). Source references — inline
  right at the material, NOT in a bottom footer; small and muted: Anthropic (Shen & Tamkin, 2026).
interaction: none
---

# Visible content

## Title bar
Eight questions — not "AI or not", but how, where and with what control to apply it

## Body
[Left — the 8-item checklist in an Ocean rounded box]

**Eight questions before the task:**
1. Which lifecycle **phase** is this? It sets the failure mode
2. What is decided **deterministically** here? Ordinary code writes that part; AI is for analysis and checking
3. **Essential or accidental** complexity? Essential — the human decides, AI stays at the periphery
4. Is the consequence **reversible**? Irreversible → lower the autonomy ceiling, a hard gate — the **VETO axis**
5. Is there a **machine oracle** (test, SAST, run)? No → the oracle first, autonomy after
6. Are **secrets / untrusted content** involved? Yes → least privilege and isolation
7. Who **reviews and who merges**? Merging and accountability — always the human
8. Is the goal an **artifact or a skill**? A skill → do not delegate the generation

[Right — what this means personally for you]
**Anthropic** (RCT, 52 developers learning an unfamiliar library): the group with AI scored **50% vs 67%** without AI on the quiz (~-17 pp). Those who **delegated the generation** dropped; those who **asked about concepts** ("how it works, why") show no degradation. The speed-up, meanwhile, is statistically **not significant**.

[Right, under the Anthropic data]
When the goal is a skill, **you do the writing**; AI explains and checks.

[Gold callout]
The checklist **does not decide "apply AI or not"** — it issues a **mode**: for a suitable task it leads to high autonomy; for an unsuitable one it lowers the ceiling and names the mandatory measures. This is a **distribution of the burden of proof**, not "always less AI". Irreversibility and impact are the **veto axis**.

## Speaker notes

Let us fold the whole lecture into a working checklist — it applies to a task before you hand it to AI. First, about the question it answers: not "apply AI or not" — that argument is closed in the industry, we saw the numbers at the start. It answers how and with what control to apply it: which mode and which autonomy ceiling are appropriate here. The first item is which phase this is: it sets the failure mode. The second is what is decided deterministically: ordinary code writes that part, AI stays on analysis. The third is essential or accidental complexity: the essential part is decided by the human. The fourth, and special, is whether the consequence is reversible: the irreversible requires a hard gate, and this is the veto axis — one high irreversibility outweighs everything else. The fifth is whether there is a machine oracle: if not, then the oracle comes first. The sixth is secrets or untrusted content: if yes, then least privilege and isolation. The seventh is who reviews and merges: merging and accountability are always the human's. The eighth is whether the goal is an artifact or a skill. The checklist distributes the burden of proof rather than demanding "always less AI": for a suitable task it will lead to high autonomy, for an unsuitable one it will lower the ceiling and name the measures.

Now the failure that is critical personally for you as students. Anthropic ran a randomized study: fifty-two developers learning an unfamiliar library, some with AI, some without, then a comprehension quiz; the group with AI scored fifty percent against sixty-seven without AI — about minus seventeen points [1]. The split is key: those who delegated the generation dropped more, while those who asked about concepts, "how does this work, why so", showed no degradation [1]; the speed-up was not statistically confirmed. A skill forms through actively retrieving the solution from memory: by asking AI to write the code you get the right result while bypassing the very effort that forms the skill. For a student the cost of delegation is higher than for the METR expert: the expert loses time, the learner loses competence. The conclusion of the eighth item: in learning, the act of going through the task is not delegated — AI's role is to explain and check, and the writing must be yours.

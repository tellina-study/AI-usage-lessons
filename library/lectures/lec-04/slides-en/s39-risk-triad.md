---
id: s38
type: schema_quadrant
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "Böckeler's risk triad — a compact criterion 'when AI yes / no': probability × impact × detectability; vibe-coding is admissible only at low × low × high, otherwise — discipline"
learning_goal: "[SI] Böckeler's risk triad (probability×impact×detectability) as the decisive practice"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.3 [for-slide-s38]"
references: [bockeler-thoughtworks]
in_bucket: true
verify_day_of: false
visual_brief: >
  schema — three MULTIPLIED axes of the risk triad (Böckeler), visual: three "low → high" scales with an explicit direction arrow (scale markers INSIDE, not outside):
  (1) probability of error (grows with unfamiliarity — the SWE-bench Pro axis) · (2) impact of error (irreversibility, security, money, data) · (3) detectability (test oracle, SAST, review).
  A highlighted GREEN/gold admissible zone for vibe-coding: ONLY low × low × high (low probability × low impact × high detectability); any other combination → discipline.
  A plate "which axis to fix": impact↑ → hard gate; detectability↓ → machine oracle; probability↑ → senior review. Failure: vibe-coding "by feel" = ignoring all three axes (in it Replit, curl-slop, vulnerable code converge).
  Böckeler: "using generative AI is a continuous risk assessment". Gold — "vibe-coding admissible ONLY at low × low × high". Lucide icons. Axis font >=14pt.
interaction: none
---

# Visible content

## Title bar
The risk triad: "when AI yes / no" = probability × impact × detectability

## Body
[Three multiplied axes, each with a "low → high" scale]

**1. Probability of error** (low → high) — grows with the unfamiliarity of the task (this is the SWE-bench Pro axis).

**2. Impact of error** (low → high) — irreversibility, security, money, data.

**3. Detectability** (low → high) — is there a test oracle, SAST, or review that will catch the error.

[The highlighted zone — gold]
**Vibe-coding is admissible ONLY at low × low × high** — low probability × low impact × high detectability. Any other combination requires discipline.

[The plate — which axis to fix]
The triad tells you **what to fix**: impact ↑ → **hard human gate**, autonomy ceiling down · detectability ↓ → add a **machine oracle** · probability ↑ → **senior review**.

[Gold callout]
Böckeler: "using generative AI is a **continuous risk assessment**". The failure — vibe-coding "by feel": ignoring all three axes. In it all the lecture's cases converge: Replit (impact ↑), curl-slop (detectability ↓), vulnerable code (probability ↑).

## Speaker notes

The third synthesis tool is Birgitta Böckeler's risk triad, a compact criterion "when AI yes, when no" that folds everything covered into three multiplied axes. The first axis is the probability of error: how likely it is that AI errs on this task; it grows with unfamiliarity — on familiar public code the probability is lower, on unfamiliar and private code it is higher. The second axis is the impact of error: irreversibility, security, money, data; deleting a prod database is high impact, generating a draft comment is low. The third axis is detectability: will we catch the error if it happens — is there a test oracle, a SAST, a reviewer.

The key point is that the axes multiply rather than add: one high axis is enough to make the whole task risky. Hence the rule: vibe-coding, that is trusting AI by feel without discipline, is admissible only in one combination — low probability, low impact, high detectability. A one-off script that you run right away and see the result — go ahead. Any other combination requires the discipline of the previous sections.

And the main practical value of the triad — it tells you which axis exactly to fix. High impact — put a hard human gate and lower the autonomy ceiling. Low detectability — add a machine oracle, a test, or a scan. High probability — put an experienced reviewer on it. Böckeler formulates this as a stance: using generative AI is a continuous risk assessment, not a one-off decision "we are for AI" or "we are against" [1]. And note: the failure the triad describes is vibe-coding by feel, ignoring all three axes; it is precisely there that all the lecture's cases converge — Replit is a failure on the impact axis, curl-slop on the detectability axis, vulnerable code on the probability axis. And an important tie to the probability axis: do not transfer a vendor's number to your task — on your unfamiliar code with your harness the probability of error is almost always higher than the advertised one.

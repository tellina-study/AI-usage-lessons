---
id: s38
type: schema_quadrant
section: "Section 7. Synthesis — discipline by phase"
duration_min: 3
assertion: "The question is not 'AI or not' — AI is applied in one mode or another almost always; Böckeler's triad (probability × impact × detectability) computes which AUTONOMY CEILING is admissible and what pays for it: full vibe-coding only at low × low × high, any other combination means a lower ceiling and mandatory measures, not a ban on AI"
learning_goal: "[SI] Böckeler's triad (probability×impact×detectability) as the apparatus for computing the level of autonomy and its price"
learning_outcomes: [LO1, LO4, LO7]
chapter_ref: "§7.3 [for-slide-s38]"
references: [bockeler-thoughtworks]
in_bucket: true
verify_day_of: false
visual_brief: >
  schema — three MULTIPLIED axes of the risk triad (Böckeler), visual: three "low → high" scales with an explicit
  direction arrow (scale markers INSIDE, not outside):
  (1) probability of error (grows with the unfamiliarity of the task and the codebase) · (2) impact of error
  (irreversibility, safety, money, data) · (3) detectability (test oracle, SAST, review).
  A highlighted gold zone "where the autonomy ceiling is highest": full vibe-coding ONLY at low × low × high
  (low probability × low impact × high detectability); any other combination is not a ban on AI but a lower
  ceiling and mandatory measures.
  Round-6 (block 5, owner note p55): the title and the framing are rewritten — the "yes or no" question is
  removed; what is computed is the level of autonomy and its price. The mechanics of the triad are unchanged
  (chapter-part5 §7.3). The probability axis is self-contained — it names unfamiliarity of the task and the
  codebase directly, with no reference to the anti-hype benchmark slide that round 6 deleted.
  A plate "which axis to fix": impact↑ → hard gate; detectability↓ → machine oracle; probability↑ → senior
  review. Failure: vibe-coding "by feel" = ignoring all three axes (in it Replit, curl-slop and vulnerable code
  converge).
  Böckeler: "using generative AI is a continuous risk assessment". A teal band under the title carries the
  reframing: AI is applied almost always; what is computed is the ceiling. Lucide icons. Axis font >=14pt.
interaction: none
---

# Visible content

## Title bar
The question is not "AI or not" but which level of autonomy: probability × impact × detectability

[Teal band under the title]
AI is applied in one mode or another almost always — the triad answers not "yes / no" but which autonomy ceiling is admissible and what pays for it.

## Body
[Three multiplied axes, each with a "low → high" scale]

**1. Probability of error** (low → high) — grows with unfamiliarity of the task and codebase.

**2. Impact of error** (low → high) — irreversibility, safety, money, data.

**3. Detectability** (low → high) — is there a test oracle, SAST, review that will catch the error.

[Highlighted zone — gold]
**Where the autonomy ceiling is highest.** Full vibe-coding — only with the combination **low × low × high**: low probability of error, low impact, high detectability. Any other combination is **not a ban on AI** but a lower ceiling and mandatory measures. The axes multiply, they do not add.

[Plate — what a higher level is paid for with]
impact ↑ → a **hard human gate** · detectability ↓ → a **machine oracle** · probability ↑ → **line-by-line senior review**.

[Gold callout]
Böckeler: "using generative AI is a **continuous risk assessment**". The failure is vibe-coding "by feel": ignoring all three axes. Every case in the lecture converges on it: Replit (impact ↑), curl-slop (detectability ↓), vulnerable code (probability ↑).

## Speaker notes

The third synthesis tool is Birgitta Böckeler's risk triad. It is worth removing a superfluous question straight away: the triad answers not "apply AI or not" — in one mode or another it is applied almost always. It computes something else: which autonomy ceiling is admissible on a given task, and what that ceiling is paid for with. The triad folds everything we have covered into three multiplied axes. The first axis is the probability of error: it grows with the unfamiliarity of the task — lower on familiar public code, higher on unfamiliar private code. The second is the impact of the error: irreversibility, safety, money, data. The third is detectability: will we catch the error if it happens, is there a test oracle, a scan, a reviewer.

The axes multiply rather than add: one high axis is enough to make a task risky. Hence the rule: full autonomy, meaning trusting AI by feel without discipline, is admissible in exactly one combination — low probability, low impact, high detectability. A one-off script that you will run immediately and see the result of — by all means. Any other combination does not mean "AI is not allowed here": it means a lower autonomy ceiling, and the difference is closed by the measures from the previous sections.

And the main practical value of the triad is that it names the price: what exactly pays for each next level of autonomy. High impact — a hard human gate and a lower autonomy ceiling. Low detectability — a machine oracle. High probability — an experienced reviewer. Böckeler formulates this as a stance: using generative AI is a continuous risk assessment, not a one-off decision "we are for AI" or "we are against" [1]. The decision is not made once, and not about the tool as a whole, but on every task. The failure the triad describes is vibe-coding by feel, in which none of the three axes is computed; it is exactly where all the cases of this lecture converge: Replit fails on the impact axis, curl-slop on detectability, vulnerable code on probability. And one attachment to the probability axis: do not carry a vendor's number over to your own task — on your unfamiliar code it is almost always higher than the advertised figure.

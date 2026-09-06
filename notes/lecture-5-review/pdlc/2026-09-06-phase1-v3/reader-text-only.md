# Reader-simulator (text-only) — Lecture 5 PDLC, Plan v3

**Reader persona:** 3rd-year, vibe-codes, works in IT, has never formally studied product management (no CustDev, Mom Test, Design Thinking, product experimentation, or SRE/SLO exposure before this).
**Read:** `notes/lecture-5-review/pdlc/plan-v3.md` + skimmed `notes/research/lecture-5-pdlc/60/61/62/63/64*.md` for what the base slides will actually contain.

## Verdict: REVISE

The base→AI→limits→failure rhythm is a good structural idea and mostly works as a *reading experience of the plan*. But when I map the plan's slide budget onto the research files that will supply the actual base content, at least three of the six "classical base" pairs are asked to compress far more concept-density than 2 slides / ~2.5-5 minutes can carry for someone with zero prior exposure. This is a structural gap, not a polish note — same category CLAUDE.md already flags for chapter depth and keystone placement.

---

## Per-section reading notes

**s08/s09 — Customer Development + Mom Test (Discovery).** Landable. Blank's 4 steps + "no facts inside the building" is one clean idea, and the Mom Test's 3 rules + good/bad question pairs are concrete and memorable (I can immediately picture the bad "would you pay $20/month" question because I've probably asked it myself in a side-project). The falsifiable-hypothesis device slots in naturally here as a *fourth* rule that ties Blank and Fitzpatrick together. Risk: s08 alone carries Blank's 4-step model AND the device intro in 2.5 min — that's two new things at once, but both are simple enough to survive it.

**s15/s16 — Design Thinking + Nielsen heuristics (Design).** This is the first slide pair where I got lost reading the plan itself. s15 has to land: 5-stage Design Thinking, the Double Diamond diverge/converge shape, the "converging on a solution before validating the problem" anti-pattern, AND the fidelity spectrum — four distinct ideas in 2.5 min. s16 stacks 10 Nielsen heuristics (compressed to "defensive programming for UX" — nice hook, but 10 named heuristics is still 10 things) plus "design system = guardrail not component library" plus "you are not the user" plus why usability testing matters. Two frameworks + a 10-item list + 2 aphorisms in 4.5 minutes total, from zero. I would come out able to repeat the taglines but not actually apply either framework. This is the base slide most at risk.

**s22 — MVP + release mechanics (Build/Launch).** Dense but each piece is a single sentence I can hold: MVP/BML (already reinforced from Discovery), DoD, four release techniques (flags/canary/blue-green/staged rollout) stated as a list rather than deeply explained, Stage-Gate framed with one memorable metaphor ("funnel not tunnel — kill early"). Because most of the audience already does some CI/CD, "feature flags" and "canary" are recognition, not new learning, for at least half the room — that buys headroom. Landable for the strong half; borderline for someone who has genuinely never shipped past a personal repo, but the framing rescues it.

**s29/s30 — Product experiment + OEC + pitfalls (Measure/Experiment).** This is the second base pair I got lost in, and arguably worse than s15/16 because the concepts are less visually intuitive than a design framework. Reading the source research, s29 alone needs to seat: what randomization buys you causally, the 7-step experiment process, OEC (with the "time on site — good or bad?" teaching example), and guardrail metrics as a *distinct* concept from OEC — that's already a lot for 2.5 min. s30 then adds: peeking/p-hacking with actual multiplier numbers (2 peeks ≈2x FP, 5 peeks ≈3.2x), Twyman's Law, SRM, Simpson's Paradox with a segment-reversal example, novelty effect, holdouts, the flag-vs-canary-vs-A/B distinction (again, after already introducing flags in s22 — good reinforcement), AND North Star/AARRR/HEART as a footnote cluster of three more frameworks. That is roughly 9-10 named concepts in 5 minutes for an audience that, per the plan's own honest admission, "видит ВПЕРВЫЕ." I could follow individual sentences but would not be able to reconstruct "why do I need both an OEC and a guardrail metric" afterward without the chapter to fall back on. Cut-order in §4a already flags s30 for "top-3 instead of 6" — that instinct is correct, but I'd push it further: this pair is the single riskiest base slide in the whole deck.

**s37 — SRE/SLO (Support/Operate).** Reads well on paper: SLI→SLO→SLA→error budget is one clean causal chain, plus the concrete Google Workbook number (1,000,000 requests, 99.9% SLO = 1000-error budget) — a real worked example, which is exactly what s29/30 lack. Then observability triad, incident management (on-call/runbook/postmortem), support tiers, and the support→product loop are each single, self-contained ideas presented in sequence rather than simultaneously. This is the best-executed "base" slide of the six precisely because it uses one worked number as an anchor instead of stacking abstractions. Still a lot of vocabulary (7-8 named terms) for 2.5 min, but the causal chain structure (SLI causes SLO causes error budget causes decision) makes it easier to hold than s30's list-of-unrelated-pitfalls structure.

**s45 — Governance base (capstone).** Thin by design (2 min, already flagged as compressible in cut-order) — portfolio/stage-gate governance + unit economics stated at a high level, feeding into the payoff rather than teaching a new operational skill. Fine as a lighter capstone; not a place I'd expect deep new-to-me learning, and the plan doesn't pretend otherwise.

**Ranking, most at risk → least:**
1. **s29/s30** (experiment base) — highest concept count, least visual/causal structure, explicitly "видит впервые."
2. **s15/s16** (design base) — two frameworks + a 10-item list + two aphorisms in 4.5 min.
3. **s08/s09** (discovery base) — dense but rescued by concreteness (good/bad question pairs) and single-thread narrative.
4. s22 and s37 — dense but each held together by a strong causal/visual anchor (a picture I can draw: "flag → canary → 100%"; "SLI → SLO → budget → decision").

---

## Too obvious for the strong half

- **s22 (feature flags/canary/blue-green/rollback):** anyone doing real CI/CD at a job has shipped behind a flag or watched a canary rollout. The plan's mitigation — "you know CI/CD, here's the difference" — needs to actually show up as a *named contrast* on the slide (e.g., "you already do this for code; Stage-Gate go/kill applies the same discipline to the *decision to keep building*"), not just be implied. If the slide just restates flags/canary/rollback as definitions, the strong half checks out for 2.5 minutes.
- **s37 (SLI/SLO/error budget):** same risk, arguably sharper — a chunk of "works in IT" students may already be on-call somewhere and know error budgets cold. The Google Workbook's exact number (1000-error budget on 1M requests) is a good save here because it's a specific worked example, not just vocabulary review — worth leaning on that concreteness rather than the definitions.
- **s09 partially (qual vs quant, survivorship bias):** "ask people what they did, not what they'd do" is close to common-sense once stated, and confirmation/survivorship bias are terms most CS-adjacent students have heard even outside product contexts. The Mom Test's exact 3-rule framing and the concrete bad/good pairs are what keeps this novel even for the strong half — don't cut those in favor of the bias vocabulary, which is the less differentiated part.
- **The "you know X, here's the difference" framing is necessary but not sufficient** — it works as a promise in the plan, but its success depends entirely on whether the actual slide text states the *contrast* explicitly (a comparison callout) rather than just presenting the classical material and trusting the strong half to notice the parallel themselves. Flag this as a Phase-5 slide-drafting requirement, not just a plan-level intention.

---

## Rhythm: help or fatigue?

Mostly help, with one fatigue risk. Reading six repetitions of base→AI→limits→failure in the plan, the *shape* becomes genuinely predictable in a good way by Section 3 — I started anticipating "okay, now the failure will be on-point to this exact phase" and the plan delivers on that (a real improvement over the implied v2 problem where failures felt random). The meta-pattern stated in s06 ("each arrow has a classical discipline AI doesn't delete") gives me a reason to expect the rhythm before I hit it the first time, which is exactly what a keystone should do.

The fatigue risk is not the rhythm itself but that **not all four beats are equally sized every time**, and the plan doesn't signal that up front. Discovery and Design get 2 base + 1 AI-capability + 1 AI-limits + 2 failure slides; Build/Launch compresses AI-capability into two slides (schrinking + launch-as-control-transfer) which is actually a *fifth* beat, not four; Support/Operate gets 3 failures instead of 2. A reader following the plan cold might expect uniform pacing across sections and be thrown when Section 5 clearly runs longer/denser than Section 2. This is minor compared to the base-density risk above, but worth a one-line note in the section dividers' tag text (already partially there: "2 базы · 3 провала" on s36 — good, keep doing this consistently on every divider so the varying shape is signposted, not surprising).

---

## Where I got lost (concrete list)

1. Reading s30 cold: by the third pitfall (SRM) I had lost track of whether SRM was a prerequisite check or a type of error — the plan text doesn't distinguish "checks you run before trusting a result" (SRM, significance) from "biases in interpretation" (Twyman, Simpson's, novelty) from "process discipline" (peeking, holdouts). The research file has this structure; the plan's one-line slide description doesn't preserve it. Recommend the chapter/slide group these three sub-clusters explicitly rather than presenting six pitfalls as an undifferentiated list.
2. s16's jump from "10 heuristics = defensive programming for UX" straight to "design system = guardrail" is a metaphor pile-up — two different code metaphors (defensive programming, guardrail) for two different concepts in the same slide risks blending together in memory as "heuristics are guardrails," which is not quite right (heuristics are checks you run; design systems are constraints you build inside).
3. Minor: s23/s24 both claim the Build/Launch "AI" beat (capability, then AI-as-launch=control-transfer) — reading the table row-by-row I initially miscounted this section as having only 1 AI slide, then found the second one three rows later. Not a reader-comprehension problem so much as a plan-legibility one; a future draft could label these s23a/s23b conceptually in the table.

---

## Keystone check

After s05/s06, yes — I can restate the loop (discover→build→measure→learn→decide) and the asymmetry (build cost→~0, measure/learn trust drops) cleanly, because the plan gives it a strong single visual anchor ("один чертёж, без сговора" tying Deming/Boyd/Ries together) before the mechanism claims arrive. The meta-pattern ("each arrow has a classical discipline AI doesn't delete") is genuinely load-bearing for following the rest of the deck — it's the reason the rhythm reads as reinforcement rather than repetition. This is the strongest part of the plan.

## Falsifiable-hypothesis device

Lands, and reuse feels earned rather than forced — it's introduced once in s08 attached to Blank's own discipline (hypothesis before you leave the building), then reappears as: the AI-defense against sycophantic synthetic-user validation (Discovery limits), implicitly as the shape of an eval bar in Measure ("write a testable bar before you run the eval"), and explicitly as a launch-gate/drift-threshold format later. Because each reuse is doing genuinely different work (a discovery discipline → an AI-failure countermeasure → an experiment design principle → an ops threshold), it reads as "one good idea applied consistently" rather than a slogan stapled onto unrelated slides. This is one of the plan's clearer wins.

---

## Summary for return message

See below.

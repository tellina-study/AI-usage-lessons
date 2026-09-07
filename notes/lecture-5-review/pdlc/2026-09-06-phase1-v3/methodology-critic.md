# methodology-critic — Phase 1 re-critique of `plan-v3.md` (Lecture 5, AI-PDLC, full rewrite)

**Дата:** 2026-09-06 · **Reviewer:** methodology-critic · **Input:** `notes/lecture-5-review/pdlc/plan-v3.md` + `60`–`64-*-base-and-ai.md` (gap-research) + `50-failures-and-limits.md` + prior `2026-09-06-phase1/methodology-critic.md` (v1 review) + CLAUDE.md

---

## VERDICT: **REVISE**

v3 fixes the two structural complaints that got v1/v2 REVISE'd — every section now opens with a named classical base, and the failure roster is genuinely re-homed to on-point phases (Zillow→Support, Chevy/NYC→Support, Google Overviews→Launch, Facebook MSI→Measure all check out against the research dossiers). Fact-integrity corrections in §7 are accurate and complete against source material. But the plan repeats — in a new form — the exact self-serving-inclusion pattern that sank v1: it now argues past the 30% floor on slide-count by reclassifying non-strict-in "upside/limits" slides as near-equivalent to strict-in content (the "~45%" claim in §5), which is not honest accounting, and it ships with an unresolved slide-numbering gap (no s35) that means the published section-4 slide count doesn't match its own §2.3 table. Combined with 6 P1 findings, this clears the REVISE bar.

---

## P0 findings (blocking)

### P0-1 — §5's "up to ~45%" claim is a rationalization, not an honest recount; the true honest number is ≈31.5–34% by minutes, which is real and should be presented as-is, not inflated further

The plan does the hard, correct thing first: it recounts 13/49 ≈ 27% by slide count, then correctly argues slide-count undercounts because failure slides run longer, and recomputes by minutes: **31.0 min / ~92 active ≈ 33.7%** (independently recomputed here — see table below, plan's own "31.5/92≈34%" is right to within rounding). This is legitimate — CLAUDE.md's mandate is explicitly "holistic," "measured by minutes/words," not slide-count, and 33.7% clears the floor with a small margin.

The plan then goes further and adds: *"Плюс upside-слайды-ограничения (s06 ось не в счёт; s11/s18/s25/s32/s39 — 'AI-limits + что оставить') при развёрнутом критерии добавляют ≈10 мин → до ~45%."* This is the same move that got v1 REVISE'd (P0-2 in the prior review: axis/mechanism/limitation-only slides counted toward strict-in). CLAUDE.md is explicit: **"Засчитывается только полностью in-bucket контент: смешанные/частично-bucket блоки... не учитываются (partial → как out при подсчёте %)."** The plan's own slide list tags s11/s18/s25/s32/s39 as `риск — upside` — i.e., self-labels them as NOT solid IN — and then immediately re-includes them in the same paragraph to manufacture a bigger number nobody asked for once 33.7% already clears the bar. **This is not a fatal defect in the honest 33.7% number — it is the plan undermining its own credible number by also claiming an incredible one in the same breath, which is exactly the "self-serving inclusion" the counter-check exists to catch, and it signals the same accounting discipline problem will recur at Phase 3/7/10 chapter/slide word-counts if not corrected now.**

**Fix:** delete the "до ~45%" sentence from §5 entirely. State only: solid IN-BUCKET = 13/49 slides ≈ 27%, by minutes ≈ 31/92 ≈ **34%** (honest, floor-clearing, no padding needed). Keep the upside slides described as what they are — necessary "what to keep from classics" content that supports but does not count toward the mandate — exactly as their own `риск — upside` tag already says elsewhere in the plan. The 34% number is good enough; stop there.

### P0-2 — Missing slide s35: Section 4 (Measure) slide list only runs s28–s34 (7 slides), but §2.3's table claims s28–s35 (8 slides) and 17 min

Re-reading §4's actual slide list: Раздел 4 header says "s28–s35" is implied by the table (§2.3: "4. Measure / Experiment | s28–s35 | 17"), but the itemized list under "Раздел 4 — Measure / Experiment" jumps from **s34** (benchmark≠reality) directly to **s36 Divider Р5** with no s35 anywhere. Summing the actually-listed s28–s34 items gives 2.5+2.5+2.5+2.5+2+2.5+2 = **16.5 min for 7 slides**, not 8 slides/17 min as the table promises. Either a slide was dropped during drafting (likely candidate: a Р4 synthesis/bridge slide parallel to s43's Р5 synthesis, which Р4 currently lacks while every other section has one) or the numbering is simply wrong and cascades into every subsequent slide ID (s36 onward) being off-by-one from what a Phase-2 book-editor or Phase-5 designer would expect when cross-referencing this plan. **This is exactly the kind of "measurable rule without a defined counting method" error `notes/decisions.md` already flags as a recurring Lec-3/6 mistake, now showing up as a literal arithmetic/ID gap rather than a definitional one.**

**Fix:** before GATE 0, either (a) add the missing s35 as Р4's synthesis slide (parallel to s43, e.g. "evals+guardrails close back into product decision") and confirm the section sums to 17 min/8 slides, or (b) renumber s36→s49 down by one and correct §2.3's slide-count column. Either way, re-verify the total 49-slide count against the corrected numbering before Phase 2.

---

## P1 findings

### P1-1 — s39's "risk" framing partially collides with No-Timing/No-Methodology + the plan doesn't flag it, but the bigger issue is s39 is a synthesis slide about drift, not new failure content, and shouldn't be near strict-in accounting even implicitly

s39 ("AI-ограничения: тихий дрейф") is correctly tagged `риск — upside` (not counted, good) — no defect here per se, but see P0-1: this is precisely one of the five slides P0-1 flags as wrongly re-added to the "~45%" figure. Filing here only to make explicit that this is not a hypothetical concern — s39 genuinely reads as strong content (the "silent killer" framing from `64-support-operate-base-and-ai.md` §3.2 is the single best insight in the whole Support section), which is exactly why it's tempting to also count it toward strict-in. Resist the temptation; its strength is a reason to keep it, not a reason to double-count it.

### P1-2 — Baseline/Counterfactual Mandate: 3 of the plan's own headline claims still lack an inline denominator in the slide-level text, even though the underlying research dossier has one

Checking specific plan claims against dossiers:

| Claim (plan slide) | Denominator present in plan's slide text? | Denominator available in research | Fix |
|---|---|---|---|
| s23 "PR +200%/год, ~16% с содержательным ревью" | Partial — "+200%/год" has no base-year anchor stated on-slide (200% of *what starting volume*?) | `63-build-launch...md` §2.1: "code output per engineer rose ~200% year-over-year" — this IS the denominator (per-engineer YoY), just needs to say "per engineer" explicitly on-slide, not just "+200%/год" | Add "на инженера" to the slide bullet, not just chapter |
| s38 "Klarna: объём рос до ~853 FTE-экв" | **Yes**, plan already carries this correctly (P1-4 from v1 review is now fixed) | confirmed in `64-support-operate...md` §4.3 | none — confirmed good |
| s40 Zillow "$304–408M... ~2000 (25%)... ≈$80k/дом" | **Yes**, all three numbers carry denominators | confirmed in `64...md` §4.1 | none — confirmed good, best-in-class as before |
| s26 Google AI Overviews "раскатан на 100% US-поиска" | Denominator is implicit (100% = full US search base) but the *contrast* baseline — what a normal staged ramp would have looked like (1%→10%→25%...) — isn't stated on the slide, only the failure mode | `63...md` §2.7 has the canonical ramp numbers (1%→10%→25%→50%→100%) | Add "vs. типичный canary-ramp 1%→10%→25%→50%→100%" inline so students see what *should* have happened, not just that 100% was bad in the abstract |
| s27 McDonald's "~100 из 13 786 (~0.7%)" | **Yes** — exemplary, denominator inline | confirmed `63...md` §4.2 | none |
| s47 "Gartner >40% отмен к 2027 / 28% успех (782 из 3400+)" | **Yes**, denominator inline (carried over correctly from v1's P1-1 fix) | confirmed | none |

Net: 2 real gaps (s23 per-engineer base, s26 missing contrast-ramp baseline), both easy inline-text fixes, not structural. Everything else the mandate previously flagged is now fixed.

### P1-3 — s10's "reference dataset — inline-define" claim needs to actually happen at s10, not just be asserted as happening

The plan states s10 does "reference dataset (эталонный набор 20–100 примеров) — inline-define" — good, this closes the v1 P-finding about forward-reference (term used at s09 before being defined at s29). But the term is then reused at s24 (CC/CD eval-gate), s29 (Measure base... wait, s29 is BASE not AI so it shouldn't reuse "reference dataset" pre-AI-section), and s31 (evals). **Check needed at Phase 2:** does s29 (base slide, product experiment/OEC) accidentally use "reference dataset" before its AI-section reintroduction, given that in the classical A/B-testing base there's no equivalent concept (the classical base uses "control/treatment cohorts," not "reference dataset" — that term is CC/CD/eval vocabulary, i.e., AI-era). If s29's base content stays cleanly classical (Control/Treatment, OEC, guardrails) and doesn't reach for "reference dataset," this is fine; flagging as a P1 because the plan doesn't explicitly confirm the base/AI vocabulary boundary is respected at s29 the way it explicitly confirms it at s10.

### P1-4 — Section 4 lost its own synthesis/bridge slide (see P0-2) — this creates an actual pedagogical gap, not just a numbering one

Every other section (Р1 has none but is short; Р3 has none; **Р5 has s43 "Синтез Р5"**) — Section 4 (Measure/Experiment) is the densest section by the plan's own admission (§10 self-roast: "риск для сильной половины скучно... Р4 база... эксперименты с нуля") and is the one place a synthesis/bridge slide would do the most good (tying OEC+guardrails+evals+Goodhart back to "what carries into Support" — the natural forward-bridge to Р5's drift material). Its absence is likely the missing s35 from P0-2. **Fix:** make the missing-s35 fix in P0-2 double as this pedagogical fix — a genuine Р4 synthesis slide, not just a numbering patch.

### P1-5 — Klarna "runtime-инъекции" grouping at s42 folds three cases (Klarna + Chevy + NYC MyCity) into one 2.5-min slide, which is thin for two of the three

s42 packs Klarna (full case, correctly detailed) + "кратко Chevy '$1'" + "NYC MyCity" into a single 2.5-min slide. Per the research dossier (`63...md` §4.4 and `64...md` §4.2/§4.4), Chevy and NYC MyCity are each substantial, well-documented, on-point Support/Operate cases in their own right (NYC MyCity's "10/10 journalists got the identical illegal answer" is one of the strongest "systemic not edge-case" teaching moments in the entire research set, per `64...md` §4.4's own framing). Compressing both into "кратко" alongside Klarna on one slide risks under-teaching NYC MyCity's actual lesson (kill-switch-as-policy, not just "bot said wrong price"), and Chevy's distinct lesson (deterministic-guardrail-beneath-LLM architecture) gets no room to land. This is a pacing/depth tradeoff, not a structural violation, but worth flagging before Phase 2 — either split s42 into two slides (accepting the section runs slightly over budget, to be absorbed by cut-order) or explicitly demote Chevy/NYC to speech.md/chapter-only "also happened" mentions rather than claiming slide-level "on-point failure" credit for content that gets ~30-45 seconds combined.

### P1-6 — LO3 curator sign-off is still listed as a pre-req in §3 but not elevated to a hard GATE-0 blocker in the same explicit terms the prior v1 review demanded

§3 states "course-curator подтверждает LO3-переинтерпретацию... ДО Phase 2" — this is good and matches the v1 review's P1-2 fix request. But it is not restated in the plan's own §10 self-roast as a **hard pre-req for GATE 0** (opening GATE 0 without this signed off risks the same late-rework risk the v1 review flagged). The plan's Changelog point (3) even frames it as a "default answer... override welcome on GATE 0" for the *content* of governance, which could be misread as bundling the informal owner-override conversation with the formal curator LO3 sign-off — these are two different approvals from two different people and should not be collapsed into one GATE-0 conversation implicitly.

**Fix:** add one explicit line to §10 self-roast (it's already there — "LO3 curator sign-off — обязателен до Phase 2" — good) but also add it as a named gate in §9's source-of-truth chain or as a standalone checklist item so GATE 0 cannot be presented without it, matching the rigor already given to the strict-in recount.

---

## P2 findings (polish, non-blocking)

- **P2-1** — s01 hook payoff to s47 is well-flagged (`*Payoff s47. Partial→out.*`) and consistent with the keystone/counter-check discipline. Confirmed good, no fix needed.
- **P2-2** — Hero requirement: s01 and (implicitly) s49 are tagged `hero` — s49 is explicitly the closing slide type (`summary`+`qa_minimal`, `hero`). This resolves the prior v1 review's P2-5 finding (missing closing-hero designation). Confirmed good.
- **P2-3** — Divider tag style (e.g. s07 "Discovery: намерение и исследование · 2 базы · 2 провала," s36 "Support / Operate: продукт как оркестр · 2 базы · 3 провала") is compliant with No-Timing/No-Methodology and format-DNA item-count convention. Confirmed good.
- **P2-4** — The "3 owner-вопроса default-ответы" in the Changelog (linear PDLC order, Governance as light capstone, base-gaps closed) is a clean, low-risk way to present defaults with explicit override-invited framing at GATE 0 — good practice, no fix needed.
- **P2-5** — s24's "CC/CD (Continuous Calibration/Development) vs привычный CI/CD" risks a terminology collision with Lecture 4's CI/CD material — worth a one-line explicit bridge ("this is the SAME CI/CD you know from Л4, now versioned by agency level, not just by code change") to pre-empt confusion; currently implicit via "forward-ref Л4," not explicit enough per plan text. Minor, chapter-level fix sufficient (no slide-list change needed).
- **P2-6** — Glossary lock (§6) marks "асимметрия стоимость/доверие" explicitly as "course-scaffold, НЕ strict-in," which is the correct discipline the P0-1 finding above needs applied consistently to the upside-slide claim in §5 as well — currently §6 and §5 are inconsistent with each other (§6 is disciplined, §5's last sentence is not). Cross-reference these two sections directly once P0-1 is fixed.
- **P2-7** — s33's Facebook MSI "все реакции ×5 одинаково" correction reads clean and matches the Techdirt-corrected mechanism in `62-experimentation-base-and-ai.md` §4.1 precisely — confirmed good, no drift into the "anger ×5" myth anywhere else in the plan (grepped s01–s49 mentally against §7's forbidden list — clean).

---

## Structure-compliance table (Р1–Р6): base → AI → limits+keep → on-point failure

| Section | Base slide(s) present? | AI slide(s) + named tools? | Limits + what-to-keep slide(s)? | On-point failure(s)? | Verdict |
|---|---|---|---|---|---|
| **0. Intro/keystone** | N/A (not a phase section) | N/A | N/A | s01 hook (payoff, not strict-in) | Compliant by design — exempt from the 4-part template, correctly so |
| **1. Discovery** | **Yes** — s08 (Customer Development/Blank) + s09 (Mom Test) — two full base slides, named originators, concrete mechanics (4-step CustDev; 3 Mom Test rules w/ good/bad pairs) | **Yes** — s10: Dovetail, Perplexity Deep Research, reference-dataset inline-define, synth-users-as-pre-research (Torres-sourced) | **Yes** — s11: hallucinated hypotheses, Torres 20-40% detail loss, "what stays" (live interviews, commitment validation) | **Yes, on-point** — s12 (NN/g synthetic-user 7/7 vs 3/7, verified against `60-discovery...md` §7.1) + s13 (Deloitte AU fabricated citations, verified against `60...md` §7.2 and `50...md` #2) | **PASS** — template followed cleanly, both failures confirmed on-point |
| **2. Design** | **Yes** — s15 (Design Thinking/Double Diamond, 5-stage + 2-diamond, anti-pattern named) + s16 (Nielsen heuristics + design systems) | **Yes** — s17: v0.dev, Figma Make, Google Stitch, Uizard, bolt.new, Midjourney, "AI for divergence, human for convergence" best practice | **Yes** — s18: AI-slop/homogenization (NN/g State of UX 2026), 29% WCAG/21,880 assessments, non-deterministic UX | **Yes, on-point** — s19 (Character.AI, verified `61-design...md` §4/`50...md` #4) + s20 (iTutorGroup, verified `61...md` §4/`50...md` #3) | **PASS** |
| **3. Build/Launch** | **Yes** — s22: MVP/BML, DoD, feature flags/canary/blue-green/staged rollout/rollback, Stage-Gate go/kill | **Yes** — s23 (Build→0, review bottleneck, Anthropic 200%/16% figures) + s24 (CC/CD agency-ladder, Copilot/Cursor named, eval-gate-as-launch-gate) | **Yes** — s25: review doesn't scale, 70%-problem, ship-without-gate = deferred cost | **Yes, on-point** — s26 (Google AI Overviews, verified `63-build-launch...md` §4.3 — dossier explicitly names this Build/Launch, not Support) + s27 (McDonald's, verified `63...md` §4.2 — dossier explicitly frames this as "a GOOD example," matching plan's "провал/позитив" framing) | **PASS** — this is the section where re-homing mattered most (Chevy/NYC correctly moved OUT per dossier §4.4, replaced with two genuinely Build/Launch-native failures) |
| **4. Measure/Experiment** | **Yes** — s29 (controlled experiment logic, OEC w/ Kohavi's own time-on-site example) + s30 (peeking/p-hacking, Twyman, SRM, Simpson's, novelty, holdouts, A/B≠feature-flag, Bing correctly ≈$100M) | **Yes** — s31: evals-as-unit-tests (Weil), Husain's ladder, pass@k vs pass^k, LLM-as-judge ~85%/<60% safety | **Yes** — s32: Goodhart/reward hacking (DeepMind spec-gaming + Anthropic Sycophancy-to-Subterfuge), "passed eval ≠ safe" | **Yes, on-point** — s33 (Facebook MSI, corrected ×5-all-reactions version, verified `62-experimentation...md` §4.1) + s34 (benchmark≠reality: Med-PaLM 86.5%+adversarial-eval-needed, Stanford RegLab 17%/33%, Mata v. Avianca=ChatGPT correctly attributed, verified `62...md` §4.2) | **PASS content-wise, but see P0-2/P1-4** — missing s35 leaves this section without its own synthesis slide, unlike Р1(none needed, short)/Р5(has s43) |
| **5. Support/Operate** | **Yes** — s37: SLI/SLO/error budget (Google SRE Workbook, "70% of outages" quote), observability, incident mgmt, support tiers/CSAT, feedback loop | **Yes** — s38: LangSmith/Langfuse/Arize Phoenix/Helicone named, drift monitoring, Guardian Agents (correctly Gartner-category-framed per §7 fix), "product as orchestra" | **Yes** — s39: silent drift ("dashboards stay green"), governance drift/guardrails-as-versioned-policy | **Yes, on-point** — s40 (Zillow, correctly re-homed to drift/circuit-breaker framing per `64-support-operate...md` §4.1's explicit re-framing directive) + s41 (Air Canada) + s42 (Klarna + brief Chevy/NYC, see P1-5 on depth) | **PASS structurally, P1-5 depth concern on s42's triple-packing** |
| **6. Governance/ROI** | **Yes** — s45: portfolio/stage-gate governance, unit economics, product operating model | **Yes** — s46: Deloitte operators→orchestrators, Sber maturity 0-5 (correctly peer-not-flagship per Changelog), IDP economics `[VFY-day-of]`, policy-as-code | Implicit within s46/s47 rather than a dedicated limits slide (Governance section's template is explicitly "база · payoff" per its own divider tag, not the full 4-part template) | **Yes, on-point** — s47 (macro-reality: MIT funnel+COI, RAND-as-lesson-not-number, S&P 17%→42%, Gartner) + s48 (Just Walk Out, hidden human cost + matrix) | **PASS by design** — Governance is explicitly the "light capstone," 3-part not 4-part template, consistent with plan's own framing in Changelog point (3); acceptable deviation since it's declared upfront, not silently skipped |

**Overall: every section (0–6) satisfies the base→AI→limits→failure template it commits to, and every failure re-homing claimed by the owner (Zillow→Support, Chevy/NYC→Support, Google Overviews→Launch, MSI→Measure) is verified correct against the underlying research dossiers.** This is the real, substantive fix over v1/v2 and should be recognized as such at GATE 0.

---

## Strict-in-by-minutes recount (independent verification)

| Slide | Plan's stated min | Case verified against dossier? | In/Out (strict-in definition: case+lesson+criterion+alternative, on-point) |
|---|---|---|---|
| s12 | 3.0 | Yes (`60...md` §7.1) | **IN** |
| s13 | 2.0 | Yes (`60...md` §7.2) | **IN** |
| s19 | 2.5 | Yes (`61...md` §4 / `50...md` #4) | **IN** |
| s20 | 2.0 | Yes (`61...md` §4 / `50...md` #3) | **IN** |
| s26 | 2.5 | Yes (`63...md` §4.3) | **IN** |
| s27 | 2.0 | Yes (`63...md` §4.2) | **IN** |
| s33 | 2.5 | Yes (`62...md` §4.1, corrected version) | **IN** |
| s34 | 2.0 | Yes (`62...md` §4.2, corrected attributions) | **IN** |
| s40 | 2.5 | Yes (`64...md` §4.1, re-homed) | **IN** |
| s41 | 2.0 | Yes (`64...md` §4.2) | **IN** |
| s42 | 2.5 | Partial — Klarna yes, Chevy/NYC thin (P1-5) | **IN** (but flag depth risk) |
| s47 | 3.0 | Yes (macro-cluster, `50...md` cross-refs) | **IN** |
| s48 | 2.5 | Yes (Just Walk Out is a standard, well-documented case) | **IN** |
| **Total** | **31.0 min** | | **13/13 confirmed IN** |

**Recount result:** 31.0 min (plan says 31.5 — trivial rounding, immaterial) / ~92 active min (using the plan's own 100−8 buffer split) = **33.7%**. Using the raw pre-cut-order section sum of 94.8 min independently recomputed from §2.3's slide list: **32.7%**. **Both clear the 30% floor with real margin — this is a genuinely honest, defensible number and the plan should present it as its headline claim, dropping the "~45%" padding (P0-1).**

**Holistic distribution check:** every section carries ≥2 on-point failures (Р1: 2, Р2: 2, Р3: 2, Р4: 2, Р5: 3, Р6: 2) — no single-cluster concentration. **This passes cleanly and is a genuine improvement over the risk profile CLAUDE.md's counter-check is designed to catch.**

---

## Fact-integrity verification (§7 corrections)

Checked each claimed correction against the research dossiers:

1. **Med-PaLM "chemo for headache" dropped** — confirmed unsourced/untraceable per `62-experimentation-base-and-ai.md` §4.2 and §5.7 ("could not be traced to any primary source... should not be used as a factual claim"). Plan's replacement (86.5% MedQA + need for separate adversarial safety-eval) is exactly the dossier's recommended defensible substitute. **Correct and complete.**
2. **Mata v. Avianca = ChatGPT, not Harvey** — confirmed per `62...md` §4.2: "attorney Steven Schwartz... submitted a brief citing six entirely fabricated court cases generated by ChatGPT — not Harvey AI, a common misattribution." Plan's §7 forbidden-list entry matches verbatim. **Correct.**
3. **MSI = all reactions ×5, not "anger ×5"** — confirmed per `62...md` §4.1's Techdirt-sourced correction: "all five reactions were weighted equally at 5x when introduced — anger was not singled out." Plan's s33 description and §7 forbidden entry both state this correctly. **Correct.**
4. **Bing ≈$100M, not "$300M button"** — confirmed per `62...md` §1.13: Bing = genuine RCT, ~$100M/yr, 12% lift, HBR/Kohavi-Thomke sourced; "$300M button" = Jared Spool usability-research retelling, NOT a randomized experiment, different company/decade/methodology. Plan's s30 correctly separates these ("Bing ≈$100M (Kohavi/Thomke HBR 2017; НЕ '$300M кнопка')"). **Correct and appropriately cites the citation-hygiene lesson itself, matching dossier §5.7's meta-point.**
5. **Guardian Agents = Gartner category, not confirmed Sber product** — confirmed per `64-support-operate-base-and-ai.md` §2.5: "Прямого продукта под названием «Guardian Agents» у Сбера... не подтверждено... Рекомендация: либо явно пометить как открытый вопрос [VFY-day-of], либо использовать GigaCowork." Plan's s38 does exactly this ("Guardian Agents (Gartner-категория...); Сбер-аналог GigaCowork `[VFY-day-of]`"). **Correct, matches dossier's own recommended hedge precisely.**
6. **Replit not reused (already Л4)** — plan's §7 forbidden list explicitly states this; confirmed the plan's own on-point failure roster (s12/13/19/20/26/27/33/34/40/41/42/47/48) contains no Replit reference. **Correct, no leakage detected.**

**Remaining unsupported/needs-flag claims — checked against §8's freshness/fact-check tags:**
- **MIT "~95%"** — plan already carries the funnel+COI caveat inline (s01, s47) and tags `[FACT-CHECK]` in §8. Adequate.
- **NN/g "7/7 vs 3/7"** — this is the NN/g synthetic-user finding itself (`60-discovery...md` §6/§7.1: "real users completed 3 of 7... synthetic users falsely reported completing all 7"), which IS the primary, verified finding, not an unsupported claim — plan's `[FACT-CHECK]` tag on this in §8 is arguably over-cautious (it's a well-sourced NN/g study, not a circulating myth), but tagging it for day-of re-verification is harmless conservatism, not a defect.
- **WCAG 29%/21,880** — sourced to `61-design-base-and-ai.md` §3.2, ACM Web4All 2026 proceedings; dossier itself flags "*(Fetch blocked by paywall/403; findings corroborated via search-result abstract excerpt.)*" — this is a genuine primary-source-access gap, not a fabrication risk, but the plan's `[FACT-CHECK]` tag is the right call and should stay through Phase 2/3 (fact-checker should attempt direct access or find a second corroborating source before chapter finalization).
- **No new unflagged claims found.** The plan's forbidden-list (§7) and freshness list (§8) together cover every risk surfaced during this cross-check.

**Verdict on fact-integrity: APPROVE-CLEAN** — this dimension of the plan is fully ready; no additional fixes needed here.

---

## Pacing / cognitive load assessment

- **Total honest.** Independently resumming §2.3's per-slide list (excluding the P0-2 s35 gap) gives ≈94.8 raw active minutes across sections, matching the plan's own "raw Σ ≈ 100–105" claim closely enough (94.8 vs. self-reported ~100–105 — the plan is if anything slightly conservative, not inflated, a good sign). Cut-order (§4a) trims toward ~92 + 8 buffer = 100. This is honest.
- **Classical-base digestibility for the strong half:** the plan's own self-roast identifies the Р4 base (2 slides, experimental method from zero) as the main risk for boredom among the strong half, and proposes bridging via "you know this from CI, here's the product-experiment difference" — a sound mitigation given the audience already has A/B-adjacent intuition from software testing. Р2's Nielsen heuristics (s16) is explicitly the first cut-order casualty, which is the right slide to cut first (most redundant with the audience's existing "defensive programming" intuition, as the research dossier's own `61-design...md` §1.4 explicitly notes: "these map almost 1:1 onto things engineers already do for good API design"). **Cut-order judgment is sound.**
- **Cut-order sequence is defensible:** s16 (heuristics, most transferable-from-existing-knowledge) → s25 (limits, can live in speech notes without losing the point since s26/s27 cases carry the lesson anyway) → s43 (synthesis, lowest information-density loss if cut) → s30 (pitfalls, top-3 vs 6 preserves the highest-value items: peeking, SRM, Simpson's are the most teachable/citable; novelty and holdouts are more supplementary) → s45 (governance base, appropriate since Governance is explicitly the lightest-weight capstone section). **No objection.**
- **One gap the pacing analysis surfaces that content-review alone wouldn't:** because s35 is missing (P0-2), the "raw Σ ≈100-105" claim is actually being met with one fewer slide than the section table implies, meaning either the true raw sum is lower than claimed (less real risk) or a slide's content silently got dropped without updating the total.

---

## Keystone & LO assessment

- **Keystone (s05–s06):** clean, in Section 0, before first deep-dive (s08+). s06 is correctly excluded from strict-in accounting *within the slide list itself* (tagged "ОСЬ — НЕ в strict-in" directly on the slide) — this is the plan applying the v1-review's P0-2 fix correctly at the slide-tag level, which makes the §5 "~45%" backslide (P0-1) even more clearly an inconsistency within the plan's own document, not a genuine ambiguity about the rule. **PASS on keystone placement and axis discipline at the slide-tag level; the only failure is textual (§5's summary prose), not structural.**
- **LO1/LO2/LO3/LO6:** credible mapping, each tied to a concrete per-phase mechanic (LO1→matrix s48, LO2→"when NOT AI-first" criterion per phase, LO3→safety/drift/governance risk+mitigation, LO6→13 on-point failures). Bloom boundary vs. Seminar 5 (Apply/Analyze via team's own hypothesis→dataset→evals→guardrail→escalation loop) remains clean and non-duplicative, consistent with the v1 review's finding on this point — no new issue.
- **LO3 reinterpretation:** still correctly flagged as needing course-curator sign-off before Phase 2 (see P1-6 above for the process-rigor gap, not a content gap — the reinterpretation itself, per the v1 review, is "arguably closer to the literal LO wording than the original finance/retail reading," which still holds).

---

## Summary of required actions before USER GATE 0

1. **Delete the "~45%" claim in §5** (P0-1) — keep only the honest 27%-slides / 33.7%-minutes recount; cross-reference §6's own "course-scaffold, НЕ strict-in" discipline so §5 and §6 agree with each other.
2. **Fix the missing-s35 gap** (P0-2) — either add a genuine Р4 synthesis slide (recommended, also closes P1-4's pedagogical gap) or renumber and correct §2.3's slide count; re-verify total = 49.
3. **Add 2 missing inline denominators**: s23 "PR +200%/год" → "на инженера"; s26 Google Overviews → name the canary-ramp baseline (1%→10%→25%→50%→100%) it skipped, not just "100% без canary" in the abstract (P1-2).
4. **Resolve s42's triple-packing** (P1-5) — either split into two slides or explicitly demote Chevy/NYC to chapter/speech-only mentions rather than claiming slide-level on-point-failure credit for ~30-45 seconds combined content.
5. **Elevate LO3 curator sign-off to an explicit named GATE-0 pre-req**, distinct from the informal "3 owner-questions" override conversation (P1-6).

## What's now fixed vs. v1/v2

- Every section (Р1–Р6) now opens with a genuine, named classical base — the owner's core complaint (#1) is resolved and verified against research.
- All 13 on-point failures verified genuinely on-point to their phase against the underlying dossiers — the owner's second core complaint (Zillow→Build was wrong, etc.) is resolved; re-homing is correct in every case checked (Zillow, Chevy, NYC MyCity, Google Overviews, Facebook MSI).
- Fact-integrity corrections (Med-PaLM, Mata v. Avianca, MSI, Bing/$300M, Guardian Agents, Replit) are all verified accurate and complete against the dossiers — no gaps found.
- The strict-in honest recount (27% slides / 34% minutes) is a real, legitimate, floor-clearing number this time, not padded with axis/synthesis slides the way v1's 18/45≈40% was.
- Hero slide requirement now satisfied (s01 + s49), closing the v1 review's P2-5 gap.

## What's still weak

- The plan cannot resist re-inflating its own honest number one more notch (§5's "~45%") even when the honest number already clears the bar — this is a discipline problem, not a content problem, and it's the single most important thing to fix before it recurs at Phase 3 (chapter word-count) or Phase 7 (rendered-slide re-verification), where the stakes of the same instinct are higher.
- The missing s35 suggests the slide list was assembled/edited without a final structural pass reconciling the itemized list against the summary table — a 5-minute check that should be standard practice before any plan is presented for critique.
- Section 4 (Measure) remains the most cognitively dense section by the plan's own admission, and now also the one missing its synthesis slide — these two facts compound each other and deserve joint attention in the P0-2/P1-4 fix, not sequential patching.

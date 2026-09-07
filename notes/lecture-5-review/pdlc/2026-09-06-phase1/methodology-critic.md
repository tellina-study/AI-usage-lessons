# methodology-critic — Phase 1 review of `plan-v1.md` (Lecture 5, AI-PDLC)

**Дата:** 2026-09-06 · **Reviewer:** methodology-critic · **Input:** `notes/lecture-5-review/pdlc/plan-v1.md` + 6 research dossiers + `99-synthesis-and-plan.md` + CLAUDE.md + `tools/lecture-production/README.md` + `00-format-dna-lec234.md`

---

## VERDICT: **REVISE**

Counter-check triggered on two independent grounds:
1. **Strict-in recount fails the plan's own bar.** The plan's honest self-recount already shows the pattern flagged in `notes/decisions.md` (Lec-3/Lec-6 lesson): several "solid IN-BUCKET" slides are axis-mechanism / criterion-only / synthesis slides, not documented-failure slides. Honest recount below lands at **13/45 ≈ 29%** on the strict "case+lesson+criterion+alternative" definition — under the 30% floor once self-serving inclusions are removed. This is the exact failure mode CLAUDE.md's counter-check exists to catch.
2. **≥5 P1 findings** (listed below) — per the Anti-Patterns table, ≥5 P1 with a marginal verdict auto-escalates to REVISE, not APPROVE-WITH-POLISH.

The plan is strong in structure, sourcing, and self-awareness (the self-roast section correctly flags 3 of the 4 real risks). It is not yet gate-ready: the strict-in accounting needs to be redone honestly, Section 4 needs de-densifying, three baseline/counterfactual gaps need explicit `[VFY]`/callout treatment, and one keystone-adjacent risk (s06 doing double duty as both keystone and strict-in) needs a decision.

---

## P0 findings (blocking)

### P0-1 — Strict-in recount does not clear 30% on the plan's own definition
See full recount table in §"Strict-in recount" below. Six of the 18 claimed slides (s06, s10, s22, s31, s39, s42) are axis-mechanism, criterion-statement, or synthesis slides — not documented-failure slides with case+lesson+criterion+alternative. Removing them (or downgrading them to "supporting", not "solid IN") drops the honest count to 12–13/45 ≈ 27–29%, i.e. **below the mandatory 30% floor for L4+ (waiver unavailable, Decision #82)**. This is not a rounding issue — it repeats the exact Lec-3/Lec-6 mistake documented in `notes/decisions.md` line 522 ("book-editor 33% vs methodology 40%... variance большая") and line 366 ("измеримое правило без определения метода подсчёта → критики разъезжаются"). **Fix:** either (a) add 3–4 more concrete failure slides (candidates below) to genuinely clear 30% with margin, or (b) tighten the in-bucket definition in the plan itself and recount before GATE 0, explicitly separating "failure case" slides from "criterion/axis" slides in the accounting table.

### P0-2 — s06 cannot be both "keystone" and "strict-in failure content"
CLAUDE.md is explicit: the carrying axis itself is *not* failure content ("несущая ось петли+асимметрии... НЕ failure → плотность инженерить намеренно" — plan's own §5 table says this for chapter, but then plan's slide-list includes s06 in the strict-in slide count anyway, contradicting its own chapter-row logic). s06 states the asymmetry mechanism (Build→0, Measure/Learn less-trusted, Observe/Orient attackable) — this is the *lens*, not a failure. Counting it as strict-in slide #1 of 18 is exactly the "self-serving inclusion" pattern flagged for Lec-4 (`decisions.md`: "граничные s06/s16/s22 — upside, НЕ baseline"). **Fix:** remove s06 from the slide strict-in count; keep it as keystone-only. This alone drops the slide count to 17/45 ≈ 38% — still fine numerically, but combined with P0-1's other removals, insufficient.

### P0-3 — Section 4 (Measure) cognitive load: 5 new concepts in 7 slides / 18 min, self-flagged but not mitigated
Plan's own self-roast admits the risk and proposes a mitigation ("reference dataset and eval вводятся вместе... flywheel — визуал-обзор, не отдельная теория") but this mitigation is not reflected in the slide list. s27 (classic A/B + AARRR + North Star + guardrail-метрики — **4 concepts on one slide**, marked `comparison`, 2.5 min), s28 (non-determinism breaks pass/fail — 1 concept), s29 (evals as PM skill — 1 concept), s30 (AI Product Flywheel, 5-stage model — **1 slide for a 5-stage framework**, 2 min), s31 (drift — 1 concept), s32 (2 failure cases), s33 (Goodhart/reward hacking + 2 failure cases). That is **8 distinct concepts** (A/B, AARRR/NSM, guardrail-metric, non-determinism-breaks-testing, evals-as-PM-skill, 5-stage flywheel, drift, Goodhart) compressed into 7 slides / 18 min — worse than the plan's own count of "5". Lec-04's densest part (Ч4, per format-DNA) still spread comparable weight over more slides. **Fix:** either split s27 into two slides (classic funnel-metrics vs. guardrail-metric-as-concept, since guardrail-metric is doing heavy lifting later at s32/s42) or cut the Flywheel to a supporting visual folded into s29 rather than its own slide, freeing a slide for pacing.

---

## P1 findings

### P1-1 — Baseline/Counterfactual Mandate: at least 4 measurable claims lack an attached base in the plan as written
Per CLAUDE.md's mandate, every measurable claim needs an inline baseline or explicit `[VFY-baseline]` flag. Checking the plan's own claims:

| Claim (plan) | Baseline present in plan? | Gap |
|---|---|---|
| MIT "95%" / "воронка 60→20→5" (s01, s41) | **Yes** — plan explicitly carries the funnel + COI caveat. Good. | none |
| Gartner ">40% agentic projects cancelled by 2027 / 28% success" (s41) | Denominator given (782 I&O leaders / 3400+ orgs per research dossier) **but not surfaced in the plan's slide description** — s41 text doesn't mention sample size | Add "782 опрошенных I&O-лидеров" / "3400+ организаций" inline per research dossier `50-failures-and-limits.md` §16b |
| S&P "42% отказываются" (s41) | Dossier has "рост с 17% годом ранее" — **plan's slide description omits the 17%→42% delta**, stating just "S&P 42% сворачивают" | Add "с 17% в 2024" — the delta *is* the counterfactual, and it's already in dossier §16b; plan text (§2.3 table) has it but slide bullet (s41 description) doesn't carry it through — cascade risk if book-editor works from slide-list, not dossier |
| Zillow "$304-408М / 25% / ~2000" (s32) | Has denominator (~2000 = 25%, ~$80k/дом) — **good**, best-in-class in this plan | none |
| Klarna "700 FTE" (s38) | Plan mentions "заявляли замену ~700 FTE" but **omits the reversal-scale counterfactual**: dossier has automation *volume* kept growing to 853 FTE-equivalent by end of 2025 even as the "AI-only" *policy* reversed — this is the single most important nuance (automation didn't shrink, the no-human-escalation policy did) and the plan's one-line slide description risks collapsing it to a simpler "Klarna failed, hired people back" story that overstates the reversal | Make explicit in slide description, not just chapter: "853 FTE-эквивалент к концу 2025 (рост продолжился) — развернулась политика, не автоматизация"; otherwise LO2 (когда AI-first вредит) is taught on a mischaracterized case |
| Sber "IDP ROI 12-24 мес" (s43) | `[VFY-day-of]` tagged — acceptable, but the plan doesn't note that this number has **no denominator disclosed even in v2.0** (dossier explicitly: "документ убрал свои собственные метрики... где метрики внедрения у самого Сбера?") | s43 should teach *this itself* as the lesson (Сбер governance-cost numbers are aspirational-industry-figures, not Sber's own measured ROI) — currently plan's forbidden-additions list correctly bans presenting Sber numbers as flagship-proof, but the slide description for s43 doesn't yet carry the "no Sber-own-metric exists" caveat as explicit teaching content |
| Anthropic "недели→часы" (s01, s06, s20) | No denominator/sample given anywhere (Anthropic report has n= for other stats but "weeks→hours" is qualitative in the source dossier itself — `20-global-consultancies-labs.md` doesn't quantify it either) | Flag as `[VFY-day-of — qualitative claim, no n= in primary]`; do not present with false precision |

**Fix:** add an explicit baseline/counterfactual column to plan §9 (currently only lists `[VFY-day-of]`/`[FACT-CHECK]` tags, not denominators) — this is what Phase 2 book-editor will need to not silently lose the Gartner/S&P/Klarna nuances that already exist in the research dossiers but didn't make it into the plan's slide-level prose.

### P1-2 — LO3 reinterpretation flagged by plan itself as unconfirmed — this blocks, not just informs
Plan §11 self-roast correctly flags: "LO-canon слота Л5 писался под finance/retail (LO3 = «безопасность данных»)... course-curator обязан подтвердить." This is listed as a "possible gap," but LO3 is load-bearing for 4 slides (s24, s32, s41, s43) and the whole Governance section. Treating it as a soft flag risks a Phase-4/5 rework if course-curator rejects the reinterpretation late. **Fix:** this should be a **hard pre-req for GATE 0**, not a parallel-track item — get course-curator sign-off on the LO3 reinterpretation (governance/guardrails/drift/prompt-injection vs. original "data security") before Phase 2 chapter drafting starts, not after.

### P1-3 — "5th risk" attribution risk: plan hedges correctly but downstream drift risk is real
Plan correctly notes (s10) "сам Cagan относит к Viability — атрибуция в chapter" — good instinct. But research (`30-product-lifecycle-modern.md`) is more precise than the plan's phrasing: Cagan's SVPG essay discusses hallucination *risk* under Viability without proposing a standalone 5th category; the clean 5-way split is **Huryn's 2026 synthesis**, not "Cagan/Huryn" as the plan's slide list co-attributes it (s10: "Cagan/Huryn: к 4 рискам добавлен риск"). This co-attribution overstates Cagan's actual position and could mislead a fact-checker into approving a mis-citation. **Fix:** slide-list language should read "Huryn 2026 (расширяя Cagan)" not "Cagan/Huryn" as joint originators of the 5-risk model.

### P1-4 — Bing figure discipline: plan's forbidden-list is right but risk is in the classic-slide (s27), not just the myth-slide
Plan correctly forbids "«$300M кнопка» приписать Kohavi (это ≈$100M Bing)" in §7. Good. But s27's own description already states "Bing ≈$100M заголовочный тест" correctly — no issue there. Flagging only because this is a place where plan discipline is *already correct* and should be preserved verbatim into chapter/slide artifacts without drift (cite as a P1 "watch" item for Phase 3, not a plan defect).

### P1-5 — RAND "80%" handling: plan says "not as a number, only as a lesson about citation drift" — but s41 slide description doesn't yet operationalize this
Plan §7 forbidden list is unambiguous: "RAND «80.3%» вовсе (citation drift — НЕ использовать как цифру, только как урок про citation drift)." Good policy. But s41's own slide description (§4) doesn't show *how* RAND appears on the visible slide — if it's meant to appear at all as "here's an example of a fabricated-precision number," the slide-list should say so explicitly (e.g., "RAND «80% AI projects fail» — цифра растиражирована, в самом отчёте её нет: сама эта статистика — пример того самого citation drift, о котором говорили в Р1 (MAHA/Deloitte)"). As written, it's ambiguous whether RAND appears on s41 at all, and if it does whether the meta-lesson is delivered on-slide or only in chapter/speech (risking a single-artifact concentration for this specific meta-lesson, a nice payoff-callback to s13 that the plan hasn't yet locked in).

### P1-6 — Section 3 (Build/Launch) has the same borderline-inclusion issue as s06/s22
s20 "Асимметрия в деле: Build→≈0" and s21 "Сбер dual-loop + IDP" are both marked `partial→out` correctly by the plan itself (good self-discipline) — but s22 ("Запуск = передача контроля") is marked **IN-BUCKET** despite being a criterion/mechanism slide structurally identical to s20/s21, just with a "критерий: не отдавать агентность раньше чем логи её оправдали" appended. Compare to s31 (drift) — also criterion-only, no case — also marked IN-BUCKET. **This is the systemic issue, not two isolated slides**: the plan is counting "assertion_visual slide with a stated criterion" as equivalent to "failure case with lesson+criterion+alternative," which is a lower bar than the CLAUDE.md definition requires ("НЕ засчитывается: общие оговорки... смешанные/частично-bucket блоки"). See full recount table below — this pattern appears in 4 of the 18 claimed slides (s06, s22, s31, s39, in addition to s10, s42 which have adjacent issues).

### P1-7 — Speech/chapter strict-in targets stated but not distributed with the same rigor as slides
Plan §5's per-artifact table gives chapter/slides/speech targets (≥40%/≥35%/≥35%) but the chapter and speech rows list only the *mechanism* ("13 провалов ≥ развёрнутый разбор... распределены по 6 фазам") without a per-part breakdown table the way `00-format-dna-lec234.md` shows Lec-04 did ("Ч1 ~35.7% · Ч2 ~35.7% · Ч3 ~39.0% · Ч4 ~52.0% · Ч5 ~39.4%" — every part individually clears 30%). Given the chapter will be 4-5 parts at ≥30k words, the holistic check needs a **per-part plan**, not just a whole-chapter aspiration, or Phase 3 will discover a single weak part after the fact. **Fix:** add a per-chapter-part strict-in target row before Phase 2 drafting starts (can be done at chapter-outline stage, doesn't block GATE 0 itself, but should be a named Phase-2 deliverable).

---

## P2 findings (polish, non-blocking)

- **P2-1** — s01 hook uses the same MIT "95%" number that gets debunked at s41 — this is intentional (planned payoff) and well-flagged ("Партиал→out (hook)... разберём в Р6"), but the plan should make explicit in the s01 description that the *unresolved tension* itself is the retrieval hook question, not just "here's a number." Minor wording tightening only.
- **P2-2** — Glossary lock (§6) marks "асимметрия стоимость/доверие" explicitly as "course-scaffold, НЕ в strict-in" — good, consistent with P0-2's concern about s06, but this note should be cross-referenced directly next to the slide strict-in table in §5, not buried in §6, so a future reader doesn't reproduce the s06 mistake.
- **P2-3** — Divider tag style ("Discovery: намерение и исследование · 2 фреймворка · 3 провала") matches Lec-02/04 format-DNA (item-count, no minutes) — correctly compliant, no fix needed, noting as confirmed-good.
- **P2-4** — s45 "Q&A отдельным beat'ом (Л2-урок #42)" — correctly compliant with format-DNA dedicated-Q&A requirement. Confirmed good.
- **P2-5** — Hero requirement (s01, presumably last slide) — plan states "hero ≥40%" for s01 but the **closing slide is s44 (summary type) or s45 (qa_minimal type)**, neither explicitly tagged `hero`. Per CLAUDE.md's Hero-check (Pre-USER-GATE point 9) and the Anti-Patterns table ("Text-only s01... или s39... без hero"), the *last* content-carrying slide needs a hero too. **Fix before Phase 5**: tag either s44 or s45 explicitly as hero-bearing in the slide list (currently only s01/s02 mention hero).
- **P2-6** — Sber "naravne" (peer, not flagship) instruction is well-executed in the slide list — Sber material genuinely distributed across s09/s21/s35/s43, no flagship block. Confirmed good, no fix needed.
- **P2-7** — McDonald's duration claim ("2.5–3 года") in s25 is itself flagged `[VFY-day-of]` in dossier — plan carries the flag correctly into §9. Confirmed good.

---

## Strict-in recount (honest, slide-level)

Definition applied (per CLAUDE.md, strict-in only): **documented failure/case + explicit lesson + criterion "when NOT AI-first" + named alternative** — OR "fundamental limitation" with the same 4 components. Criterion-only or mechanism-only slides (no case) do not qualify; axis/keystone slides do not qualify regardless of framing.

| Slide | Plan's claim | Recount verdict | Reason |
|---|---|---|---|
| s06 | IN (keystone-2, "граница/риск подхода") | **OUT** (axis, not failure) | This is the keystone mechanism (asymmetry), explicitly excluded by CLAUDE.md's own logic that the axis is not failure content. Self-serving inclusion (Lec-4 pattern repeat). |
| s10 | IN (5th risk, LO6) | **BORDERLINE — count as supporting, not solid** | States a criterion ("AI-инсайт требует аудита") but no case *on this slide* — the cases are s12/s13. If s10 is retitled to explicitly reference NN/g+Watson inline (not just "coming up"), it could count; as written it's a risk-taxonomy slide, not a failure slide. |
| s12 | IN | **IN — confirmed** | NN/g case + IBM Watson case, explicit criterion, explicit alternative. Textbook strict-in slide, plan correctly calls it "эталон." |
| s13 | IN | **IN — confirmed** | Deloitte + MAHA cases, criterion, alternative. Solid. |
| s17 | IN | **IN — confirmed** | Character.AI case, criterion, alternative. Solid. |
| s18 | IN | **IN — confirmed** | Grok case, criterion, alternative. Solid. |
| s22 | IN ("граница подхода") | **OUT** (criterion/mechanism, no case) | CC/CD agency-ladder mechanism with a stated criterion, but no documented failure named on this slide (agency-ladder failure cases, if any, aren't here). Same class of error as s06. |
| s24 | IN | **IN — confirmed** | Chevy case, criterion, alternative. Solid. |
| s25 | IN | **IN — confirmed** | McDonald's case, criterion, alternative. Solid. |
| s28 | IN ("почему AI ломает измерение") | **BORDERLINE — count as supporting** | States a limitation (non-determinism breaks pass/fail) with a criterion, but this is a mechanism/limitation statement, not a case. Closer to qualifying than s06/s22 since it is a genuine "fundamental limitation" framing (CLAUDE.md allows this as an alternative to a case) — **keep IN if chapter gives it a concrete illustrative failure inline** (e.g., a specific eval that passed/failed inconsistently); as a bare mechanism claim it's thin. |
| s31 | IN ("риск") | **OUT** (criterion/mechanism, no case) | Drift-as-concept with criterion; the case is s32. Same pattern as s06/s22. |
| s32 | IN | **IN — confirmed** | Zillow + Facebook MSI, both with denominators, criterion, alternative. Best-in-class slide in the deck. |
| s33 | IN | **IN — confirmed** | Med-PaLM + Harvey, Goodhart's law lesson, criterion, alternative. Solid. |
| s37 | IN | **IN — confirmed** | Air Canada case, criterion, alternative. Solid. |
| s38 | IN | **IN — confirmed** (pending P1-1 fix on Klarna counterfactual) | Klarna case — solid structurally, but needs the 853-FTE nuance fix to avoid teaching a mischaracterized lesson. |
| s39 | IN ("синтез Р5") | **OUT** (synthesis, no new case) | Recaps s37/s38 into a criterion statement. Synthesis slides don't add new strict-in content — they restate prior cases' lessons. Not wrong to have, just shouldn't double-count. |
| s41 | IN | **IN — confirmed** | MIT/RAND/Gartner/S&P macro-failure case with explicit calibration lesson (per P1-5 fix). Solid, arguably the strongest "meta" failure slide in the deck. |
| s42 | IN ("когда НЕ AI-first — матрица") | **OUT** (checklist/synthesis, no new case) | This is the payoff matrix/checklist — valuable, and clearly "judgment content" in spirit, but it restates criteria from earlier slides rather than presenting new documented failures. Structurally a summary tool, same class as s39. |

**Honest recount: 13/45 confirmed IN (s12, s13, s17, s18, s24, s25, s28*, s32, s33, s37, s38, s41, plus s10 if retitled) ≈ 27–29%.**
*s28 kept provisionally IN per the "fundamental limitation" allowance — needs chapter to earn it with a concrete illustrative failure, else drops to 12/45 ≈ 27%.

**This is under the 30% floor.** Not by a wide margin, but the counter-check rule doesn't have a "close enough" exception, and the pattern (padding the count with axis/criterion/synthesis slides) is the documented Lec-3/Lec-6 mistake.

**Fix options for Phase 2:**
1. Add 2-3 more named failure slides. Strong unused candidates from the research dossiers not currently in the slide list: **iTutorGroup** (age-discrimination hiring bot, Discovery/Design boundary, $365k, clean criterion — currently *absent* from the slide list despite being in `50-failures-and-limits.md` #3), **NYC MyCity chatbot** (10/10 journalists got the same illegal answer — Support/Operate, very strong "systemic not edge-case" criterion, currently *absent*), **Amazon Just Walk Out** (Wizard-of-Oz disclosure failure — strong "honesty about autonomy claims" lesson, currently *absent*). Any one of these added as a genuine case-slide (not a criterion-only slide) closes the gap with margin.
2. Retitle s10 to include the NN/g+Watson cases inline (currently forward-referenced) rather than treating them as "coming up" — this alone would flip s10 from OUT to IN.
3. Recompute and update plan §5 with the corrected count before GATE 0 — do not carry the current 18/45≈40% figure into Phase 2 chapter briefs, since book-editor will use plan §5 as its target and will inherit the inflated number.

**Holistic distribution (still checked even though total is short):** distribution across sections is genuinely good — no single section carries the whole load (Р1: s12/s13; Р2: s17/s18; Р3: s24/s25; Р4: s32/s33 [+s28 provisional]; Р5: s37/s38; Р6: s41). This part of the plan's self-check is accurate and should be preserved once the count is corrected.

---

## Keystone-axis assessment

**PASS**, with one dependency on P0-2. The axis (loop + cost/trust asymmetry) is presented as two dedicated slides (s05, s06) in Section 0, strictly before the first deep-dive (s08 onward) — matches the Lec-02/03/04 pattern exactly (hook → cover → lecture-map → bridge → keystone). s05's framing ("один чертёж, без сговора" — Deming/Boyd/Ries converging independently) is a direct structural echo of Lec-04's git-loop keystone ("на этом скелете практики независимо сошлись Anthropic/OpenAI/DORA/Thoughtworks") — this is the right move, it's the same rhetorical device that worked for Lec-04. Title is about the axis itself ("петля, один чертёж"), not course scaffolding — compliant.

Each section does climb/descend the loop as claimed: Р1=discover, Р2=design(build-adjacent), Р3=build/launch, Р4=measure, Р5=support(operate/learn), Р6=decide/governance closes the loop back to discover (s44 payoff explicitly returns to s01's paradox). This is a clean, non-surfacing axis — no "axis appears mid-lecture" risk detected.

**One open dependency:** the axis's soundness as *keystone* is fine; the problem (P0-2) is purely about *also* counting it toward strict-in, which double-dips against CLAUDE.md's own stated logic.

## Pacing assessment

Honest-ish, with one soft spot. The math (78 active + 8 retrieval + 7 divider = 93 + 7 buffer = 100) is internally consistent and the per-slide time budget sums correctly against the section totals in §2.3's table (spot-checked: Р4 sums to 2.5+2.5+2.5+2+1.5+3+2=16, plan says 18 including the 0.3 divider + ~1.7 min unaccounted — close enough to not be a red flag, but Phase 2 should re-verify exact sums per section rather than trust the aggregate "~93 active" figure, per the `notes/decisions.md` lesson about not trusting self-reported metrics without independent re-verification).

Section 4 is the acknowledged dense section (P0-3 above) — 18 min for 8 concepts is tight even generously counted; recommend either trimming Flywheel to a visual-only aside or moving guardrail-metric-as-concept earlier (into s10's 5-risk slide, where "AI-инсайт требует аудита" already gestures at the same judgment) to reduce net-new-concept load in Р4 specifically.

## LO coverage / Bloom assessment

LO1/LO2/LO3/LO6 mapping is plausible and the Lecture(Understand/Evaluate)-vs-Seminar(Apply/Analyze) boundary is stated cleanly and not obviously duplicated — Seminar 5's described activity (build own reference dataset + 3 evals + guardrail metric + escalation point) is a clean Apply-level task that doesn't re-teach lecture content, it exercises it. Good boundary discipline.

**LO3 reinterpretation (see P1-2): plausible on its face** (governance/guardrails/drift/prompt-injection is a defensible reading of "проанализировать риски: безопасность, ограничения, уязвимости" — arguably *closer* to the literal LO wording than the original finance/retail "data security" reading was), but this is exactly the kind of judgment call that needs course-curator's explicit sign-off before Phase 2, not just orchestrator's self-assessment, per the plan's own flagged gap.

## Missing-fundamentals assessment

For an audience new to PM vocabulary specifically (not new to AI): Cagan's 4 risks get one slide (s08) with inline-define — adequate for "vibe-coder who's never touched PM theory," matches the "compact ввод" the plan promises. Evals get a reasonable ramp (s28 mechanism → s29 "unit tests for agent" analogy, which is a strong intuition-bridge for a CS-literate audience — good choice, echoes Lec-04's testing vocabulary directly). Drift gets one slide (s31) plus the Zillow case (s32) — probably sufficient given the audience already understands "model" as a concept from L1-L3/L4. Guardrails get spread across s22 (mechanism)/s24 (case)/s43 (governance) — reasonably scaffolded, not a missing-fundamental.

**One real gap:** "reference dataset" is used as a load-bearing term from s09 onward (intent-loop framing) through s29-s30 (evals framework) but its *first* inline-define doesn't happen until s29 per the glossary-lock table's "inline-required" list — if s09 uses the term before s29 defines it, that's a forward-reference violation of the plan's own inline-required rule (§7). **Fix:** either define "reference dataset" briefly at first use (s09) or delay the term until s29 and use a plain-language paraphrase at s09.

## Format-DNA compliance assessment

Compliant on the checked dimensions: lecture-map as loop-shaped diagram (s03, matches Lec-02's pipeline-shaped lecture-map pattern), dividers with item-count tags not minutes (confirmed, e.g. s07 "2 фреймворка · 3 провала"), dedicated Q&A slide (s45, folded with bridge per Lec-04's own precedent — acceptable), no-timing/no-methodology stated as a design constraint in §7's forbidden list (correctly present). Hero requirement only half-locked (P2-5) — needs an explicit closing-hero slide designation before Phase 5.

---

## Summary of required actions before USER GATE 0

1. **Recount and correct strict-in §5** using the honest per-slide table above; either add 2-3 real failure slides (iTutorGroup / NYC MyCity / Amazon JWO are ready-made from the research dossier) or retitle s10, and remove s06/s22/s31/s39/s42 from the "solid IN" count (they can remain as valuable criterion/synthesis slides, just not counted toward the 30% floor).
2. **Get course-curator sign-off on LO3 reinterpretation** before Phase 2 chapter drafting — currently a soft self-flagged gap, needs to be a hard pre-req.
3. **De-densify Section 4**: cut Flywheel to a visual aside or merge s27's 4-concept slide into two, and re-verify the per-slide time sums instead of trusting the aggregate.
4. **Fix the 3 baseline/counterfactual gaps** in slide-level prose (Gartner denominator, S&P 17%→42% delta, Klarna 853-FTE continuation) so they survive into Phase 2 rather than existing only in the research dossier.
5. **Lock a closing hero slide** (s44 or s45) and fix the "reference dataset" forward-reference (define at s09 or delay to s29).

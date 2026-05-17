# Лекция 5 — visual loop iteration log

Deck: 33 слайда (32 LOCKED s01–s32 + s04a divider Раздела 1).
Render: build_lec05.py → libreoffice→pdf → pdftoppm. Min 3 iter/slide,
max 7, escalate at 7. Snapshots: snapshots/iterN/s-NN.png (page order:
s01,s02,s03,s04,s04a,s05…s32 → page = idx+1).

Palette LOCKED Ocean + Teal + Gold ≥1×/slide. Motif Ocean rounded box.

---

## Iter 1 — full deck render + inspect (all 33)

- (a) inspected: s01 hook, s02 cover, s03 keystone, s08 timeseries,
  s09 Zillow, s12 fraud-chart, s13 confusion-matrix, s14 FP-contrast,
  s18 Apple Card, s26 collaborative, s29 task-matrix + spot-check rest.
- (b) findings:
  - s01: STRONG. gold $500M+, teal panel, bottom callout. accept-track.
  - s02: STRONG cover, roadmap-bar + gold Раздел 0. accept-track.
  - s03 KEYSTONE: **BUG** — 5-type cards: icon (y+0.14, h0.44) collides
    with 2-line label (y+0.58); center-align splits «Прогноз | рядов»
    around icon. FIX.
  - s08: STRONG. d08 diagram renders, товаровед analogy. accept-track.
  - s09 Zillow payoff: **CRITICAL OVERFLOW** — left ocean_box (lh=4.05):
    3 blocks @1.18 each + Knight plate spill out box bottom. Failure
    exemplar broken. RESTRUCTURE.
  - s12 fraud: chart OK; right teal «Заметьте формулировку» overflows
    its container bottom. FIX box height/position.
  - s13 confusion-matrix: STRONG schema (TP/TN teal, FP gold, FN deep),
    accuracy-lie + cost-sensitive + forward-pointer. Minor: FP cell text
    ~px overflow; right panel whitespace gap (mass). Polish.
  - s14 FP-contrast: left box precision↔recall+Knight overflow bottom;
    right teal callout huge empty bottom (mass imbalance 40%). FIX.
  - s18 Apple Card: GOOD, dense but contained. accept-track.
  - s26 collaborative: d26 matrix STRONG (gold «вы» row). caption clips
    box bottom 2px; center-align cells → awkward word-split. FIX align.
  - s29 task-matrix: EXCELLENT. icons/row, gold «не ИИ» row, 100% fill,
    single-line. Schema checklist PASS. accept-track.
  - Anti-leak grep: 0 hits (visible+notes). Notes 150–317 words OK.
- (c) checklist status: schema slides s13/s29 PASS readability; s03 5-type
  FAIL (icon collision); s26 schema PASS but align polish needed.
- Verdict: iter-2 fixes — s03, s09 (critical), s12, s13, s14, s26.
  accept-track (no fix iter-1): s01, s02, s08, s18, s29 + dividers.

---

## Iter 2 — targeted fixes (s03, s09, s12, s13, s14, s26)

- (a) inspected iter1 110dpi: confirmed s03 icon-collision, s09 overflow,
  s12 callout overflow, s13 FP-cell+whitespace, s14 box-overflow+mass,
  s26 caption-clip+center-split.
- (b) changed:
  - s03: 5-type cards — icon top-band + 2-line label band (anchor TOP).
  - s09: blocks 1.18→1.02 spacing, body 0.78→0.60, tighten text;
    Knight plate 0.46→0.62; right box 1.86→1.62 + teal 2.05→2.32.
  - s12: chart box 3.30→3.66; Россия box 1.66→1.70; teal 1.48→2.02
    with \n\n; gold moved 4.66→5.04.
  - s13: cell desc 2-line not 3; right panel divider line + cost-sensitive
    heading (balanced, no whitespace gap).
  - s14: FP plates 0.92→0.86; right teal 4.05 filled +1 line (no empty).
  - s26: cells left-align (no word-split); caption inside box; rows
    0.72→0.66; box fits.
- (c) checklist: s09 still appeared overflowed at 110dpi → re-render 150dpi
  to confirm ([#69-render-1]: 110dpi hides/false-positives layout).

## Iter 3 — 150dpi verify + s03 second fix (accept)

- (a) inspected iter2 150dpi (per [#69-render-1] final = 150dpi).
- (b) findings + change:
  - s09: 150dpi shows FITS — earlier "overflow" was 110dpi blur. RESOLVED.
  - s12/s13/s14/s26: all fit, balanced, \n\n renders as paragraph
    breaks correctly. RESOLVED.
  - s03: STILL icon/label collision (single-run \n + TOP anchor +
    wide box). Second fix: split label into 2 separate MIDDLE-anchored
    text_box per line (no \n), icon top-band. → re-render → PASS.
- (c) checklist final (150dpi):
  - Schema Readability — s03 keystone (matrix-bridge): PASS (single-line
    headers, ≥12pt, color-coded, fill 100%). s13 confusion-matrix
    (schema_matrix 2×2): PASS (TP/TN teal, FP gold, FN deep; axis labels;
    accuracy-lie+cost-sensitive; ≥12pt; ≤2 lines). s26 collaborative
    (schema_matrix): PASS (left-align cells, d26 diagram, fill ≥75%).
    s29 task-matrix (schema_matrix 6×3): PASS (icons/row, gold "не ИИ"
    row, single-line, 100% fill, ≥12pt, unified RU).
  - 5-Second Test: all 33 PASS — main message == assertion at 25%/50%
    zoom (verified per-slide vs YAML assertion).
  - Projector 50%: titles ≥21pt, body ≥11pt, schema ≥12pt — PASS.
  - Cross-slide redundancy: 0 duplicate assertions; chart types distinct
    (c12 fraud-bar ≠ c27 recsys-bar); failure cases each once
    (Zillow s09, fraud-FP s14, Apple Card s18, Air Canada/Klarna s23,
    Wendy's s28; Knight = callback s09/s14/s19 only).
  - Iconography: one Lucide set, Ocean recolor (mid/teal/gold/white),
    ≤4 distinct/slide, semantic. PASS.
- Anti-leak grep on rendered PPTX (visible+notes): 0 hits.
- Verdict: ACCEPT all 33 for QA agents (Phase 7). 3 iterations on every
  slide (iter1 inspect → iter2 fix → iter3 150dpi verify); fix-heavy
  slides s03/s09/s12/s13/s14/s26 got an extra sub-fix on iter3.

## Per-slide iteration count

- s01,s02,s04,s04a,s05,s07,s08,s10,s11(s12pg),s15..s25,s27..s32 dividers:
  3 iter (inspect → no-fix-track → 150dpi confirm).
- s03 (keystone): 4 iter (inspect → fix1 → fix2 → confirm).
- s09 (Zillow exemplar): 3 iter (inspect → restructure → 150dpi confirm).
- s12,s13,s14,s26: 3 iter (inspect → fix → 150dpi confirm).
- Max iter used = 4 (s03); no escalation needed (cap 7).

---

# Phase 8 — batched revision (Phase 7 5×QA reports, Issue #100)

Inputs: presentation-critic REVISE (6 P1 / 7 P2), student-simulator REVISE,
reader-rendered APPROVE-WITH-POLISH (1 P1 s17 + P2 visual-enlarge),
consistency APPROVE-CLEAN (1 P2), fact APPROVE-CLEAN (2 P2).
Constraint: notes UNTOUCHED (reader: notes strong), LOCKED=33, branch
phase-1-plan, worktree-only.

## New analogy shape-diagrams (derivation from chapter source-of-truth)

- **d16-inspector-reason-codes** (chapter §3.3) — interpretable model shows
  reason codes line-by-line vs black box refuses → s16.
- **d22-grounding-student** (chapter §4.3) — student guesses confidently vs
  opens the reference first → s22 (bottom band; resolves 8-point overload).
- **d26b-three-sellers** (chapter §5) — collaborative=behaviour pattern /
  content=catalogue / hybrid=both+context → s26 (replaces weak d26 matrix
  that confused student+reader).
- **d31-password-vs-face** (chapter §6.3) — password rotatable (reversible)
  vs face/print (irreversible) → s31 large gold anchor band.
- All emoji replaced by geometric `person()` glyph + drawn icons
  (rsvg-convert has no emoji font — codepoint-box bug caught iter-1).

## P1 fixes (visual loop ≥3 iter each touched slide)

- **s01** (3 iter): inspect → mega-stat $500M+ dominant + 3 small support
  + 1-line gold → 150dpi confirm. 5-sec PASS.
- **s03** (3 iter): inspect → compact bridge-strip secondary + large 5-type
  map main + «вводим с нуля» line moved off-slide (in notes) → confirm.
  5-sec PASS, keystone declutter done.
- **s12** (3 iter): inspect → 3 separate stat-plates (distinct units, Visa
  gold, NO false shared axis) → confirm. Misleading-scale P1 resolved.
- **s17** (3 iter): inspect (confirmed 4th bullet overlap teal) → 4th opt-out
  bullet in gold plate + teal pushed clear, box-math verified no overlap →
  150dpi confirm. reader-P1 (only P1) resolved.
- **s24** (3 iter): inspect → re-angled to PIVOT checkpoint (✓4/5 strip +
  forward-question gold, NOT «необходим/недостаточен» dup) → confirm.
- **s27** (3 iter): inspect → 2 stat-plates replace ghost bars + historical
  caveat → confirm. Projector-invisible P1 resolved.
- **s30** (3 iter): inspect → FINAL PAYOFF distinct from s29-matrix /
  s24-pivot (dominant gold principle band + case→fix evidence strip) →
  confirm. synthesis-redundancy differentiated.
- **s31** (3 iter): inspect → 2 explicitly separated panels (bold header
  plates + vertical divider) + large gold d31 anchor band; iter-2 widened
  d31 1080→1480px for better band fill; PII glossed inline → confirm.
- **s19**: angle already distinct (automation-without-gate criterion, Knight
  context) — kept; kill-switch/circuit-breaker glossed inline (P2).

## P2 fixes

- s28: right empty panel → counter-weight «proxy↑ vs goal→» divergence
  mini-diagram + compact criterion (chapter §5.5 derived).
- s08: explicit decomposition caption under d08.
- s09/s19: circuit-breaker/kill-switch inline glosses.
- s31: PII «(персональные данные)» inline in title.
- s12/s17 footer: «Банк России 2025» → «20.11.2025» (fact P2-1).
- s23: «(Klarna, 2024)» added to ~$40 млн (fact P2-2).
- s13: visible matrix «1-го/2-го рода» → «первого/второго рода» (consistency
  P2 D1, intra-slide unify at first-introduction).
- s21/s27/s31 right-panel text enlarged for projector-50%.

## Verification (final)

- Anti-leak grep (PPTX visible + speaker_notes): 0 hits
  ([FACT-CHECK]/[VFY]/LO/§X.X/→sNN/for-slide).
- LOCKED=33: order exact (s04a@5), count 33, totals 33, suffix-ID intact,
  s05/s06 NOT merged.
- Schema Readability final: s03 bridge PASS, s13 2×2 PASS, s26 grid PASS,
  s29 6×3 PASS.
- 5-Second Test on every touched slide @150dpi: PASS (main message ==
  re-angled assertion for s24/s30; mega-stat = s01; stat-plates = s12/s27).
- Notes word count: 3 slides 308-317 (s14/s22/s28) — PRE-EXISTING, notes
  NOT touched per brief (reader rated notes strong). Residual for orchestrator.
- charts c12/c27 deprecated (gen_charts.py header note); no longer referenced.

## Per-slide iter count (Phase 8)

- s01,s03,s12,s17,s24,s27,s30 = 3 iter; s31 = 3 iter (incl. d31-widen
  sub-fix iter-2). Pass-checklist trumped count; no escalation (cap 7).

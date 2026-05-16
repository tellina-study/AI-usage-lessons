# Лекция 3 — Visual-loop iteration log

Issue #87 · branch `issue-87-lec-03-architectures` · 30 slides.
Palette LOCKED Ocean + Teal + Gold. Motif: Ocean rounded box.
Build: `build_v1.py` (full rebuild per iter — PowerPoint MCP limitation [#54-3]).
Schema slides per deck.yaml: s10 pipeline · s12/s17/s22/s27 matrix ·
s21 cycle · s24 architecture · s26 layered. s27 = density watch-item.

---

## Iter 1 — full deck (110dpi)

- (a) Inspected: all 30 PNG. Baseline render clean — palette/motif/gold
  consistent, fonts legible, no accent-lines, charts render with Ocean colors.
- (b) Built from scratch via build_v1.py — 30 builders, 53 icons, 5 charts.
- (c) Problems found (fix list for iter 2):
  - **s26 [P0]** layered ladder BROKEN — boxes overlap, text overflow,
    trigger labels collide. base_y/trig_h math wrong. Full redo.
  - **s04 [P1]** ladder direction: step 1 (code, gold) at TOP — should be at
    BOTTOM (it IS at top in render → must invert so «1 код» = bottom rung).
    Also right rule panel 30%+ whitespace.
  - **s21 [P1]** loop-back: stray teal dash at far right (meaningless
    connector); no visible return-arrow Iterate→Plan. ~30% bottom whitespace.
  - **s10 [P2]** stage boxes ~60% empty (text only top 40%) — tighten height
    or enlarge content; whitespace imbalance.
  - **s01 [P2]** right column 2 blocks float — bottom whitespace; left
    chronicle uneven gaps (item 3 wraps).
  - General: several content boxes have bottom whitespace → tighten heights,
    rebalance visual mass.
- 5-sec test (iter1): s27 PASS, s17 PASS, s24 PASS, s10 PASS, s21 PASS
  (concept), s04 FAIL (direction confusing), s26 FAIL (unreadable).

---

## Iter 2 — targeted fixes (110dpi)

- (a) Inspected: all 30 PNG iter1.
- (b) Changed:
  - s04: ladder geometry rebuilt bottom-up (step 1 gold = BOTTOM rung →
    step 6 top); added up-arrow + «выше»; rule panel gold full-height.
  - s26: full redo — bottom-aligned ladder, short rung labels, triggers in
    gaps ABOVE each rung, full-height gold rule panel. (was P0 broken)
  - s21: cards enlarged (less internal whitespace), START teal badge on
    Plan, explicit return path (down→left→up into Plan) + loop chip.
  - s10: stage icons added (database/route/check-check), body enlarged,
    vertical balance improved.
  - s03: spoke cards enlarged with icons, gold «эмбеддинги Л2» as chip
    inside RAG card (was floating label).
  - s01: chronicle rows evenly distributed (anchor=MIDDLE per row),
    right contrast blocks enlarged + icons added (message-square-warning,
    key) + teal-tint on «что было нужно».
- (c) Checklist status:
  - s26 schema_layered: bottom-aligned PASS, captions/layer PASS, max 6
    rungs OK, hierarchy PASS, trigger connectors PASS → was FAIL now PASS.
  - s04: 5-sec test PASS (direction now reads code→multi-agent).
  - s21 schema_cycle: explicit START PASS, explicit CONTINUE PASS (loop
    chip+arrow), 4 elems PASS, direction PASS.

## Iter 2b — icon coverage fix (110dpi)

- (a) Inspected: s05 missing target icon.
- (b) Found: gen_icons.sh only made partial variant matrix → target-teal,
  key-teal, check-check-teal, database-teal etc missing. Regenerated FULL
  matrix (29 icons × 4 variants = 116 + 3 logos = 119 files).
- (c) Re-rendered all 30: s05 target icon now present; s03/s10/s20 dynamic
  -variant icons all resolve.

## Iter 3 — divider redesign + 150dpi final inspection

- (a) Inspected: s09 section divider BROKEN (210pt «Раздел 2» wrapped +
  giant stray digit bleed-through).
- (b) Changed: build_section_divider full redo — cover-style giant soft
  digit (380pt COVER_OUTLINE) on right, «РАЗДЕЛ N» label + subtitle +
  frame phrase left, gold roadmap. Distinct from content (no Ocean motif).
- (c) 150dpi inspection (per [#69-render-1] dense-slide rule):
  - s09/s18 dividers: PASS — clean, distinct, gold roadmap marker.
  - **s27 decision matrix (watch-item): PASS** — 7×7 full fill, single-line
    headers, semantic color (gold=strong/teal=weak), gold bottom plate.
    Cell font ~11pt = at minimum but legible at 150dpi (reference matrix,
    speaker walks through). Schema_matrix checklist PASS.
  - s20 MCP: PASS — dense but legible, callout/footer separated.
  - s28 checklist: PASS — 8 items legible.
- 5-sec test (iter3): all 30 PASS — main message matches assertion.

## Iter 4 — motif compliance + final 150dpi accept

- (a) Deck-level scan: gold/motif compliance check + 25% overview montage.
- (b) Found + fixed: s17 + s27 (schema_matrix tables) had NO Ocean motif
  wrapper (tables sat directly on white) — deck.yaml visual_brief mandates
  «в Ocean rounded box». Added ocean_box behind both tables (drawn first,
  cells on top). s02/s09/s18 NO-GOLD flag = false positive (gold via shared
  roadmap_bar: GOLD_TINT card + GOLD accent line — verified).
- (c) Final accept (150dpi, all 30):
  - Palette LOCKED Ocean+Teal+Gold — 0 off-palette. Gold ≥1×/slide ✓.
  - Ocean motif on every content slide ✓ (cover/dividers exempt by design,
    have gold via roadmap).
  - 8 schema slides Schema Readability Checklist: ALL PASS
    (s10 pipeline · s12/s17/s22/s27 matrix · s21 cycle · s24 architecture
    · s26 layered). s27 watch-item PASS at 150dpi.
  - 5-Second Test: 30/30 PASS. Projector 50%: PASS (cell font s27 = floor).
  - No forbidden additions (no «Лектору»/«Вы здесь»/timing/CVE/pricing/
    SDK-code/transformer-formulas on visible layer — verified visually).
- Iterations per slide: schema/ladder slides (s04,s10,s21,s26,s17,s27) =
  4 iters; divider slides (s09,s18) = 3 iters (incl iter3 redesign);
  all others = 3 iters. Min 3 satisfied for every slide; max 7 not hit.

VERDICT: ACCEPT — handed to orchestrator for QA agents.

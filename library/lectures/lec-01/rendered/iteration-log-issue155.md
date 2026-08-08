# Iteration log — issue #155 (Лекция 1, Round 2 polish)

Continuation of issue #153 Round 1 polish (see `iteration-log-issue153.md`).
Round 2 splits 21 comment-anchored fixes into 4 batches. This file covers
**Batch 3** (comments #189, #190, #191, #192, #193 — s18 architecture schema
+ s19a autonomy levels). Batches 1-2 are covered by their own commits
(d99481c, 82e0f06); this batch's commit follows.

---

## Batch 3 — s18 (agent architecture schema) + s19a (autonomy levels)

### Pre-check: orchestrator-supplied coordinates vs actual code

Orchestrator's relative-anchor geometry (extracted via python-pptx before
Batch 2) was cross-checked against the current `build_s18`/`build_s19a`
source before editing. USER oval (L=0.056 T=0.473 W=0.083 H=0.147), pipeline
row (T=0.340-0.520), loop-back bar (T=0.267) all matched the live code
exactly (small ~0.01 drift on `loop_x1`, attributable to PNG-measurement
rounding, not real drift). No discrepancy found — Batch 2 did not touch
s18/s19a as stated, coordinates were safe to use as-is.

### Fix #189 — s18 USER cluster vertical alignment (P1)

**Problem:** USER oval's vertical center (`user_y=3.55`, center 4.10") sat
noticeably below the pipeline stage row's center (`stage_y=2.55,
stage_h=1.35`, center 3.225") — a 0.875" offset, visible as the "USER →
Plan" arrow running downhill instead of level.

**Fix:** `user_y` now computed as
`stage_y_ref + stage_h_ref/2 - user_d/2` (= 2.675"), so the USER circle's
own vertical center exactly matches the pipeline row's center. The
"Пользователь" caption below the circle derives its position from `user_y`
so it moved automatically with no separate edit needed. The pre-existing
"USER → Plan" arrow (`a1`) was already anchored to the pipeline's center
height, so after this fix it reads as a clean horizontal arrow instead of a
diagonal one — an unplanned but welcome side-effect.

### Fix #190 — s18 loop-back connector arrow direction (P1)

**Problem:** The vertical gold connector joining "Рефлексия" to the
horizontal loop-back bar above it was a `DOWN_ARROW` — visually read as "the
bar feeds into Рефлексия", backwards from the actual flow (Рефлексия →
up into the bar → left → down into План).

**Fix:** Changed `MSO_SHAPE.DOWN_ARROW` → `MSO_SHAPE.UP_ARROW` at the same
position/size. Verified via zoomed crop: arrowhead now points up out of
"Рефлексия" into the bar.

### Fix #191 — s18 stop-arrow left end (P1, 2 extra sub-iterations)

**Problem:** After #189 raised the USER cluster ~0.875" upward, the existing
"стоп → результат пользователю" arrow (fixed height tied to the pipeline
bottom, `stop_y = stage_y+stage_h+0.55`) no longer reached the new USER
position — it terminated below the (now higher) USER circle, in empty
space.

**Iteration 1 (rejected):** Tried routing the entire horizontal arrow run at
USER's new center height. Result: the arrow cut straight across the middle
of all 4 pipeline boxes ("План"/"Действие"/"Наблюдение"/"Рефлексия"),
overlapping their name/sub-label text. Visually broken — rejected on
inspection.

**Iteration 2 (rejected):** Tried adding a vertical stub next to USER
reaching up from the original `stop_y` height to USER's center, while
keeping the horizontal arrow at the low height. Result: the stub overlapped
the "Пользователь" caption and did not read as a connected path (arrowhead
and stub were visually disjoint) — rejected on inspection.

**Iteration 3 (accepted):** L-shaped route — horizontal leg stays at the
original `stop_y` height (below the pipeline boxes, clear of their text,
matching Fix pattern from Batch 1/2's respect for existing untouched
geometry), then a short vertical riser (`UP_ARROW`) climbs from that height
up to USER's (raised) bottom edge, landing directly on the circle. Riser
placed just right of USER's right edge (`user_right_edge + 0.15`) where
nothing else occupies the space. The "стоп → результат пользователю" label
was also nudged right (`riser_x + 0.25`) after iteration 3's first render
showed its leading "с" clipped by the riser shape.

**Total: 3 sub-iterations for this one fix** — captured here because it
directly demonstrates the required minimum-3-iteration Generate→Convert→
Inspect→Fix discipline (`tools/presentation-build/README.md` §5), not
because the brief demanded extra scope.

### Fix #192 — s19a explicit "Пользователь: ..." role framing (P2)

**Problem:** The 5 autonomy-level cards had abstract role descriptions
("пользователь на каждом шаге", "пара, ролями перетекая", etc.) that didn't
read as a direct answer to "what does the user do at this level".

**Fix:** All 5 rewritten as explicit `Пользователь: ...` statements:
1. Оператор — «Пользователь: одобряет каждое действие»
2. Соавтор — «Пользователь: работает наравне с агентом»
3. Консультант — «Пользователь: ставит цель, правит план»
4. Утверждающий — «Пользователь: утверждает на контрольных точках»
5. Наблюдатель — «Пользователь: только получает результат»

Longest string (46 chars, level 4) verified at 9.5pt italic within the
5.5"-wide role text_box — fits on a single line with no overflow (checked
via 2x-zoomed crop).

### Fix #193 — s19a right-column order reversal (P2)

**Problem:** Left ladder goes high-autonomy-on-top (5.Наблюдатель top →
1.Оператор bottom). Right column (human/loop framings) went the opposite
direction (in-the-loop/≈1-2 on top → out-of-the-loop/≈5 near bottom,
Override last) — rows didn't line up by autonomy level between the two
columns.

**Fix:** Reversed framings list order to: Human-out-of-the-loop (≈ур.5,
gold) → Human-on-the-loop (≈ур.3-4) → Human-in-the-loop (≈ур.1-2) →
Override (kept last, since it applies at any level rather than a fixed
ladder position). GOLD_TINT fill logic is keyed by color value, not list
position, so re-ordering didn't require touching the fill-selection code.

### Verification

- Regenerated `lec-01.pptx`/`lec-01.pdf` via `build_lec01.py` +
  `libreoffice --headless --convert-to pdf` (workaround [#153-1] PATH/
  LD_LIBRARY_PATH exports applied).
- s18: 4 render iterations (1 baseline + 3 for fix #191's L-route). Final
  render passes 5-Second Test at 100dpi/50%-zoom equivalent: USER → 4-stage
  pipeline → gold loop-back-up-and-over → teal stop-arrow-down-and-into-USER
  all legible with no overlaps.
- s19a: 1 render iteration sufficient — both fixes are data/order changes
  with no new geometry, confirmed clean on first render (checked role-text
  overflow explicitly since #192 lengthened all 5 strings).
- Regression check: s19 (untouched, between the two edited slides) and s20
  (untouched, downstream) re-rendered identically to pre-batch baseline.

### Files touched

- `library/lectures/lec-01/rendered/build_lec01.py` (`build_s18`,
  `build_s19a`)
- `library/lectures/lec-01/slides/s18-agent-architecture-schema.md` (Visual
  section updated)
- `library/lectures/lec-01/slides/s19a-autonomy-levels.md` (Visual section
  updated)
- `library/lectures/lec-01/rendered/lec-01.pptx` / `.pdf` (regenerated)

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

---

## Batch 4 — issue #155 fix #174 (s05a instructor card rebuild) + fix #194 (s23 visual polish)

### Fix #174 — s05a full rebuild on sem-01 s02 reference pattern

**Problem:** Previous s05a was a monogram-tile ("ИИ" initials on a blue
circle) + 3 generic motif cards, all still containing literal placeholder
text in square brackets (`[годы работы с AI; конкретные проекты]`,
`[почему важно лично]`, `[контакт, формат вопросов]`) — a known finding
carried over from issue #153. Owner asked for a full rebuild matching
`library/seminars/sem-01/slides/s02-instructor-bio.md`'s layout: left
vertical photo strip + right specialization/fact cards.

**Fix:** Rewrote `build_s05a` from scratch:
- Left strip (SURFACE fill, ~28% width `strip_w=3.75`, full slide height):
  real instructor photo (`assets/instructor-photo-crop.png`, cropped from
  the owner-supplied `assets/instructor/levko-photo.png` — same source
  used by seminar 1 — to a 3:4 portrait framing that keeps headroom +
  shoulders, replacing the earlier over-tight crop attempt that cut off
  the chin), full name "Левко Максим Николаевич", divider line, 2 contact
  rows with circular icon badges (Lucide `send`/`mail`, downloaded fresh
  from jsdelivr CDN, recolored `#065A82`, rendered to 96px PNG via
  `rsvg-convert` — no send/mail icon existed yet in `assets/icons/`).
- Right area (white, ~72%): assertion title + specialization headline
  ("Архитектор, технический и продуктовый лидер...") + 3 fact cards in a
  2-tier layout — tier 1: experience-numbers card (briefcase icon, "20+"
  gold-highlighted per the ≥1×/slide gold rule + "10+ завершённых
  проектов под руководством") and expertise card (layers icon, 5-item
  skill list); tier 2: wide "Консалтинг и inhouse" card with 4 company-name
  pill badges (Yandex / МТС / Магнит / Сибур) using a **generic
  building-2 Lucide icon**, not official company logos (trademark/
  asset-sourcing risk per the brief).
- Real contacts used throughout: Telegram `@Maxim_Levko`, email
  `Levko.maxim@gmail.com` — no placeholders left anywhere in visible body.

**Iterations (3):**
1. Baseline render — found 2 problems: (a) "10+ завершённых проектов под
   руководством" text descender clipped by the card's bottom edge (card
   too short for 2-line body at the chosen y-offset), (b) large empty
   white space below the 3 cards (card block ended at y≈5.70 vs slide
   height 7.5", ~1.8" of unused space) — a Visual Mass Balance flag.
2. Fixed clipping (2-line wrap + repositioned offsets inside card A/B) and
   tightened nothing else yet — re-render confirmed no more clipping.
3. Rebalanced vertical rhythm: grew `card_h1` 1.95"→2.15", `card_y1`
   2.15"→2.35", `card_h2` 1.35"→1.55", gap between tiers 0.25"→0.30" so
   the card block now spans y≈2.35–6.35 (1.15" bottom margin, roughly
   matching the 0.55/0.45 top margins) — and added the gold "20+" run via
   `text_runs` (mixed-color text) to satisfy the ≥1×/slide gold-highlight
   rule, which the slide had zero of before. Final render: clean, no
   clipping, balanced whitespace, gold present.

**Speaker notes:** Rewritten from scratch — old notes had 4 literal
placeholders (`[имя]`, `[сфера]`, `[актуальная тема]`, `[сколько лет]`,
`[контакт]`). New notes (196 words, within 150-250 range) use the actual
bio content from the brief (architect/product lead, 20+ years, Yandex/
МТС/Магнит/Сибур consulting+inhouse) and keep the "карта, которой у меня
самого не было" framing from the old notes (owner explicitly liked this
line), closing with real contacts (Telegram/email) instead of
`[контакт]`.

### Fix #194 — s23 visual polish (single-container unification + russification)

**Problem:** Owner: «тут надо чуть логичнее сделать появление слайда и
сделать его визуально приличнее, пока внезапно и неаккуратно смотрится».
Diagnosis on the pre-batch render: (1) "ENTERPRISE / API" right-column
heading was not russified while the left column ("ПОТРЕБИТЕЛЬСКИЕ
ТАРИФЫ") was — inconsistent bilingual heading pair; (2) the slide was 4
visually disjoint floating shapes (2 column boxes + Samsung box + EU box)
with no unifying frame, unlike the single-Ocean-rounded-box-container
pattern used on s08/s12.

**Fix:**
- "ENTERPRISE / API" → "КОРПОРАТИВНЫЕ ТАРИФЫ / API" (kept "API" per
  Russification keep-list — established acronym).
- Added one outer `ocean_box` container (white fill, LIGHT stroke)
  spanning the full composition area (2 columns + bottom strip), with all
  previously-independent shapes now nested inside it with padding — same
  "single-container wraps everything" pattern as s08/s12.
- Reworked internal spacing: bullets in both columns now wrap to 2 lines
  each with tighter, even line spacing so nothing crowds or overlaps: the
  bottom strip (Samsung + EU AI Act) also moved fully inside the outer
  container instead of floating below it.

**Iterations (3):**
1. Baseline (unify container + russify heading) — found bullet line-2
   text in both columns crowding the next bullet (uneven vertical rhythm
   from the original single-line bullet spacing applied to now-wrapped
   2-line bullets).
2. Fixed bullet spacing (explicit `\n` line breaks + reduced/uniform
   0.50" per-bullet step) — re-render showed clean, non-overlapping
   bullets in both columns; verified bottom-right EU box text ("до 35M €
   / 7% — за запрещённые практики", 2-line wrap) fits inside its box via
   a zoomed crop, no clipping.
3. Full-region regression render (s22 section-4 divider, s23, s24
   hallucinations) — confirmed no regression on neighboring slides,
   final s23 reads top-to-bottom: bridge-label → title → single frame →
   2 columns → bottom strip, passes 5-Second Test ("where does your data
   go depends on the tier you're on").

### Verification

- Regenerated `lec-01.pptx`/`lec-01.pdf` via `build_lec01.py` +
  `libreoffice --headless --convert-to pdf` (workaround [#153-1] PATH/
  LD_LIBRARY_PATH exports applied). 36 slides confirmed unchanged in count.
- Bracket-leak grep on rendered PPTX visible text for both slides (s05a
  idx 6, s23 idx 27): 0 hits — confirms all `[...]` placeholders removed
  from s05a (known issue #153 carry-over) and none introduced on s23.
- Regression check: s02a (lecture-map), s05c (section-1 divider), s06
  (untouched, downstream of s05a) and s22 (section-4 divider), s24
  (hallucinations, downstream of s23) all re-rendered identically to
  pre-batch baseline.
- s06a (comment #175, owner-photo URL issue) explicitly NOT touched in
  this batch, per instruction.

### New assets created

- `library/lectures/lec-01/rendered/assets/instructor-photo-crop.png` —
  3:4 portrait crop of `assets/instructor/levko-photo.png` (720×960,
  full width, top-aligned to keep headroom+shoulders).
- `library/lectures/lec-01/rendered/assets/icons/lucide-send-blue.png` —
  Telegram contact icon (Lucide `send`, recolored `#065A82`, 96px).
- `library/lectures/lec-01/rendered/assets/icons/lucide-mail-blue.png` —
  Email contact icon (Lucide `mail`, recolored `#065A82`, 96px).

### Files touched

- `library/lectures/lec-01/rendered/build_lec01.py` (`build_s05a` fully
  rewritten, `build_s23` container/heading/spacing rework)
- `library/lectures/lec-01/slides/s05a-instructor-card.md` (Visual section
  + speaker notes fully rewritten, frontmatter `visual.primary` updated)
- `library/lectures/lec-01/slides/s23-consumer-vs-enterprise.md` (Visual
  section + frontmatter `visual.primary` updated; speaker notes untouched
  — brief only asked for visual-doc sync)
- `library/lectures/lec-01/rendered/lec-01.pptx` / `.pdf` (regenerated)

---

## s07 Round-2 redesign (owner comment #176 — standalone creative pass)

Unlike the other Round-2 fixes (point patches from a batched brief), owner
comment #176 explicitly asked for a multi-iteration creative redesign of
s07's timeline visual, spun off into its own agent pass: **"попробуй
визуализацию таймлайна улучшить... подумай, покрути отдельным агентом и
сделай конфетку"**.

### Problem in the batch-1..4 baseline (Fix-7 v2, pre-existing)

Each of the 3 groups ("Открытия (1950 — 1980-е)", "Зимы и прорывы (1973 —
2012)", "Перелом и взрыв (2012 — 2026)") had its year-range spelled out in
a plain-text label in a **left column**, directly duplicating the
individual years already marked as points on the timeline 2" to the right
of that label. No background/panel differentiated the 3 groups — all 3
sat on plain white, stacked with a thin gap.

### Method: isolated single-slide test harness

Built a standalone script (`s07_test.py`, not committed — scratchpad only)
that imports the palette + shape helpers straight from `build_lec01.py`
and renders ONLY s07 into a throwaway 1-slide pptx, so each iteration
converts in ~1-2s instead of re-rendering all 36 slides. This is what made
5 real iterations practical within the time budget.

### Variants tried (3 substantially different compositions, per brief)

**(a) Full-width tint panel + left accent-bar + pill floating inside panel
top-left.** Group name as a small colored pill sitting a fixed distance
from the panel's left edge, with a thin vertical accent-color bar running
the full height of the panel on the far left (visual echo of the old left
column, but recolored/thinned). Readable, clean, but the accent bar felt
like a leftover of the old "left column" idea rather than a fresh
composition — didn't fully commit to "no left column at all."

**(b) `ocean_box`-style card with explicit stroke + group title as plain
text top-left, INSIDE the card, well above the timeline.** More
"card"-like via the visible border, but left a dead gap between the title
text and the timeline itself — group name floated with no strong visual
tie to "its" timeline, worse mass balance than (a). Also the biggest radius
setting made LibreOffice render a soft drop-shadow under the rounded-rect
panel (still within anti-pattern rules — not a forbidden accent-line or
red — but a less flat/clean look than (a)/(c)).

**(c)/(d) Compact panel + group-name TAB badge straddling the panel's top
edge (half in, half out — like a manila-folder tab or a section divider
tab).** Most distinctive composition of the three — reads immediately as
"this whole panel belongs to this label," no left column at all, no dead
space. (d) is (c) refined: bigger panel corner radius, taller bands so the
pivot label doesn't crowd the tab, tighter bottom-callout gap fixed.

**Chosen: (d).** Strongest on the "не банальная, конфетка" criterion the
owner asked for, cleanest mass balance (tab bridges title↔timeline instead
of leaving a gap), and the panel-tint darkening light→mid→deep across the
3 groups reads as a small extra narrative signal (visually "approaching"
the 2017 pivot) that wasn't present in (a)/(b).

### WCAG contrast bug found mid-iteration (not part of original brief, but blocking)

Iteration 3: measured actual WCAG contrast ratios for every text/background
pair used (script in scratchpad, formula = relative luminance / contrast
ratio per WCAG 2.1). Result: **gold (#F0AB00) TEXT on the light Ocean-tint
backgrounds measures ~1.6:1 to ~2.0:1 contrast — fails AA (needs ≥3:1 even
for large bold text)**. This was already true of the "2017" gold year-label
and the "«Attention Is All You Need» ★" gold pivot-label text in variant
(d)'s first pass (inherited from the original baseline's gold-text-on-white
convention, which happened to pass only because white has the highest
possible luminance ceiling — still measured just 1.99:1, technically still
failing AA even against pure white).

Fix: gold in this slide (and, worth flagging deck-wide — see below) only
ever works as a **fill** with DEEP text on top (measured ~6.9:1, comfortably
passes AA). Changed: pivot event label → DEEP bold (was gold). Pivot year
"2017" → DEEP bold 22pt text inside a dedicated GOLD pill shape (was gold
14→22pt text with no shape backing). The gold pill + gold oval marker
together read as a single badge/pin silhouette — this ended up stronger as
a "wow" element than the color-only version, because it's a shape people's
eyes catch before they even read the number.

**Flag for `notes/mcp-limitations.md` / design-research follow-up:** gold
`#F0AB00` should probably never be used as a **text color** anywhere in this
deck's palette — it fails WCAG AA against every background in the Ocean
palette family (verified: white 1.99:1, light-tint 1.6-1.8:1). Current
`gold_callout()` helper already avoids this correctly (DEEP text on
GOLD_TINT cream background). Recommend a repo-wide grep for `color=GOLD`
on `text_box` calls as a follow-up audit — out of scope for this task
(single-slide brief), reporting for orchestrator visibility only.

### Russification pass (per brief point 4)

- "Turing — Imitation Game" → "Тьюринг — тест на мышление" (explicit owner
  request, brief's own suggested phrasing).
- "ELIZA — Weizenbaum" → "ELIZA — Вайценбаум" — spelling matches this same
  slide's own speaker notes ("В шестьдесят шестом — Вайценбаум создаёт
  ELIZA..."), not chapter.md's citation-style "Weizenbaum" (chapter keeps
  Latin surnames in academic-citation contexts, slides don't).
- "1-я зима — Lighthill" → "1-я зима — доклад Лайтхилла" — matches speaker
  notes phrasing ("после доклада Лайтхилла британскому правительству").
- "«Attention Is All You Need»" kept verbatim — exact paper title in
  quotes, legitimate citation per brief point 4's own carve-out.
- Deep Blue / AlexNet / ChatGPT / DeepSeek R1 / Claude Code — kept as
  proper/brand names (Russification keep-list).

### Iterations (5 total, brief asked for ≥4-5)

1. First pass at (a)/(b)/(c) — established the tab/panel concept was
   strongest; found no critical blockers yet (insufficient scrutiny — see
   iter 2).
2. Fixed (a)'s tight bottom-callout spacing and (c)'s pivot-label/tab
   crowding; synthesized (d) from (c) with bigger radius + more vertical
   room. Also caught the `ocean_box` soft-shadow artifact in (b) via
   crop-zoom inspection.
3. WCAG contrast audit (see above) — found and fixed the gold-text-on-tint
   failure. This was the highest-value fix of the whole pass; would not
   have been caught without explicitly computing contrast ratios rather
   than eyeballing.
4. Enlarged the pivot gold pill (1.05"→1.35" wide, year 17pt→22pt) so the
   "2017" badge visually dominates by more than the checklist's literal
   "≥2× the regular year size" — the badge's added shape-area makes the
   perceived weight far greater than the raw font-size ratio suggests.
5. Fixed a spelling inconsistency introduced in iteration 2 ("Вейценбаум"
   with е, wrong) against the slide's own speaker notes ("Вайценбаум" with
   а) — caught during the Russification cross-check against
   `s07-timeline-2017.md`, then verified against the real 36-slide build
   (not just the isolated test harness) to confirm no shift on neighboring
   s06a/s07a.

### Verification

- Regenerated `lec-01.pptx`/`lec-01.pdf` via `build_lec01.py` (36 slides
  confirmed, workaround [#153-1] PATH/LD_LIBRARY_PATH applied).
- Rendered s06a (idx 9) and s07a (idx 11) — both bracket s07 (idx 10) in
  the deck — confirmed byte-for-byte visually unchanged from pre-redesign
  baseline (no bleed from the new panel geometry).
- Full Vaswani callout text (all 7 co-author surnames + citation count)
  fits cleanly on 2 lines at 12.5pt in the real 36-slide build, matching
  the isolated test-harness result.
- Projector-readability check at 50% zoom: main message ("3 eras of AI
  history, culminating in the 2017 transformer pivot") still reads
  instantly; gold badge remains the clear visual anchor.
- Schema Readability Checklist (`schema_timeline`, `tools/presentation-build/
  README.md` §4): em-dash separators ✓, pivot-year visual dominance ✓ (via
  shape, not just font-size ratio), no band-border crossing ✓, max 3
  events/band ✓ (unchanged), timeline ≥60% slide width ✓ (measured 85%).

### Files touched

- `library/lectures/lec-01/rendered/build_lec01.py` (`build_s07` fully
  rewritten — tab/panel composition, WCAG-fixed gold usage)
- `library/lectures/lec-01/slides/s07-timeline-2017.md` (Visual section
  rewritten to describe final composition + iteration trail; frontmatter
  `visual.pattern`/`visual.primary` updated)
- `library/lectures/lec-01/rendered/lec-01.pptx` / `.pdf` (regenerated)

---

## Round 2 QA-fix pass (issue #155, post-QA-with-roles)

Consolidated 10-item fix brief from orchestrator after presentation-critic +
student-simulator QA-with-roles pass (both verdict REVISE/actionable).
Workaround [#153-1] PATH/LD_LIBRARY_PATH exports applied throughout
(`libreoffice`, `pdftoppm`, `rsvg-convert` under `/tmp/claude-999/local`).

### P1-1 — deck-wide WCAG gold-text-on-light-bg audit (18 locations)

Full audit of every `color=GOLD` text usage in `build_lec01.py` (found via
`grep -n "color=GOLD"`), cross-checked against the actual shape drawn
immediately before each `text_box` call in source order (z-order = paint
order in python-pptx). All 18 locations from the brief confirmed present at
the cited (or adjacent, after prior edits shifted line numbers) lines.

| # | Slide / fn | Text | BG underneath (verified) | Verdict | Action |
|---|---|---|---|---|---|
| 1 | s00b `build_s00b` | "Центральный вопрос курса" | `ocean_box` default SURFACE | light | → `color=DEEP` |
| 2 | s06a `build_s06a` | "13 лет" | `filled_rect(..., GOLD, radius=True)` — gold-ON-gold | light (worse: same color) | → `color=DEEP` |
| 3 | s11 `build_s11` | "включает предыдущий" (copy 1) | plain WHITE slide bg | light | → `color=DEEP` |
| 4 | s11 `build_s11` | "включает предыдущий" (copy 2 — **exact duplicate block**, confirmed byte-identical incl. `gold_callout` call, drawn twice on top of itself) | plain WHITE slide bg | light | Removed duplicate block entirely (dead code, not just color) + fixed remaining copy → `color=DEEP` |
| 5 | s15 `build_s15` | "Это уже приложение" | `filled_rect(..., WHITE, stroke=GOLD)` | light | → `color=DEEP` |
| 6 | s16 `build_s16` | "Системный промпт" | `filled_rect(..., GOLD_TINT, stroke=GOLD)` | light | → `color=DEEP` |
| 7 | s17 `build_s17` | "Оговорка для промышленных систем" | `ocean_box(fill=GOLD_TINT, stroke=GOLD)` | light | → `color=DEEP` |
| 8 | s18 `build_s18` | "продолжить — цикл повторяется" | plain WHITE slide bg (label sits above gold loop-bar, not on it) | light | → `color=DEEP` |
| 9 | s21 `build_s21` | "ВОПРОС 1" | plain WHITE slide bg | light | → `color=DEEP` |
| 10 | s21 `build_s21` | "ВОПРОС 2" | plain WHITE slide bg | light | → `color=DEEP` |
| 11 | s23 `build_s23` | "ПОТРЕБИТЕЛЬСКИЕ ТАРИФЫ" | `ocean_box(fill=GOLD_TINT, stroke=GOLD)` | light | → `color=DEEP` |
| 12 | s23 `build_s23` | "Samsung 2023 — канонический инцидент" | `filled_rect(..., GOLD_TINT, stroke=GOLD)` | light | → `color=DEEP` |
| 13 | s23 `build_s23` | "до 35M € / 7% — за запрещённые практики" | `filled_rect(..., MID)` — dark navy fill | **dark** (measured WCAG contrast GOLD vs MID = 3.77:1, passes ≥3:1 large-bold-text AA threshold; adjacent line in same MID block already uses `color=WHITE` successfully) | **Left as-is** — contrastic, per brief's own "if ≥3:1, leave it" instruction |
| 14 | s24 `build_s24` | "Ответ AI (3 фейк-ссылки):" | `ocean_box` default SURFACE | light | → `color=DEEP` |
| 15 | s24 `build_s24` | DOI lines ×3 (10pt, smallest font of all 18) | `ocean_box` default SURFACE | light | → `color=DEEP` |
| 16 | s24 `build_s24` | "10–15%" (Vectara HHEM higher-risk stat) | `ocean_box(fill=TEAL_TINT, stroke=TEAL)` | light | → `color=DEEP` (kept bold + size=24 for visual weight, per brief) |
| 17 | s25 `build_s25` | "GPT-4o: лесть (sycophancy) — апрель 2025" | `ocean_box(fill=WHITE, stroke=GOLD, stroke_pt=2.0)` | light | → `color=DEEP` |
| 18 | s29 `build_s29` | lecture-map current-lecture number ("1.1 Введение") | `ocean_box(fill=WHITE, stroke=color)` — module-color stroke, WHITE fill interior where the text sits | light | → always `color=DEEP` (dropped the `GOLD if is_now else DEEP` ternary); kept `bold=True` unconditionally (was `bold=is_now`) so the current-lecture row still stands out via weight, without relying on a failing color |

18/18 addressed: 17 changed to DEEP, 1 (#13) confirmed contrastic and left
untouched. Zero remaining `color=GOLD` on light backgrounds after fix —
verified via `grep -n "color=GOLD" build_lec01.py` returning only line for
#13. All 17 changed locations visually re-inspected at 150dpi post-render;
dark, readable text confirmed on every affected slide (s00b, s06a, s11, s15,
s16, s17, s18, s21, s23, s24, s25, s29).

Gold as fill/stroke/pill/marker preserved everywhere (≥1×/slide rule intact)
— only text color changed in the 17 fixed spots.

### P1-2 — s18 "использует" label crossed by connector lines (3 sub-iterations)

**Iter 1 (rejected):** Moved the label up from the original mid-gap position
(which crossed BOTH the "стоп → результат пользователю" text row and the
horizontal stop-arrow band) to just below the pipeline row, adding a white
backing rect to mask the vertical connector passing behind. Render showed
the white backing patch itself now overlapping/clipping the "стоп →
результат пользователю" text ("зователю" cut) and leaving an ugly hard-edge
white patch cutting across the horizontal teal stop-arrow line.

**Iter 2 (rejected):** Moved the label down instead, into the small gap
between the stop-arrow band's bottom edge and the resources row (`stop_y +
0.13`). This cleared the text-row and stop-arrow-band collisions, but the
label was still horizontally CENTERED on the vertical TEAL/LIGHT connector
stub that runs the full height from the pipeline row to the resource boxes
— so the connector still cut through the "у" in "использует" at the new y
(same defect, different line).

**Iter 3 (accepted):** Kept iter 2's y-position (clear of stop-arrow +
text), but left-aligned the label starting just right of the connector's
centerline (`tools_x + stage_w/2 + 0.14`) instead of centering it across the
full box width. No backing rect needed — no line crosses the label's
horizontal span at any point. Verified via 2×-zoomed crop: "использует"
fully legible on both connectors, "стоп → результат пользователю" text
unobstructed.

### P1-3 — s02 speaker notes stale lecture-name reference

`slides/s02-cover.md` — removed "Лекция называется «AI вокруг нас» —
потому что" preamble (stale name, renamed in issue #171 to «Что такое AI?
История, классификация, общие понятия»). Reworded to start directly with
"К 2026 году AI перестал быть..." per brief's suggested phrasing. Rest of
paragraph (infrastructure-layer framing + voice input / navigation / face
unlock / spam filter / recommendations / autocomplete examples) unchanged.
Confirmed `load_notes()` parses speaker notes directly from the `.md` file
at render time (no duplicate copy embedded in `build_lec01.py`) — single-file
fix sufficient, s02 cover PNG visually unaffected (notes-only change).

### P1-4 — s22 spec/implementation mismatch (section divider)

Confirmed `build_s22()` (unchanged, per brief) already renders the simple
`nav_slide()` pattern with `frame_phrase="Куда уходят данные · ошибки AI ·
«не умеет» — тоже ваше."` — matching what the brief asked the .md spec to
describe. Updated `slides/s22-section4-boundaries.md`:
- `visual.pattern`: `section_divider_with_3_reasons` → `section_divider_with_progress`
  (matches s07a/s10/s27 convention).
- `## Visual` section rewritten to describe the actual simple-divider
  composition (large "Раздел 4" background + title + 1-line frame-phrase +
  roadmap-bar), copying the s07a phrasing pattern.
- Speaker notes: removed the explicit "Три причины... Первая. Вторая.
  Третья." announcement/numbering scaffold, rewritten as connected prose
  that still carries all 3 content points (your responsibility for
  deploying AI; AI fails systematically/predictably; the "what AI can't do"
  boundary is also your responsibility). Final paragraph (7 topics) kept
  as-is.

No code change to `build_s22()` — render already correct, only the .md
spec needed to catch up to the render.

### P1-5 — s12 "vector DB" used before definition

Added one inline gloss sentence to `slides/s12-classification-task-modality.md`
speaker notes, positioned right after the "модальность" axis walkthrough
where the Поиск×Структ.данные cell content (vector DB) is contextually
relevant: "В ячейке «Поиск × Структурированные данные» стоит vector DB —
база данных для поиска по смысловой похожести, подробнее разберём на
слайде про агента." No change to term-appearance order elsewhere.

### P2-6 — s12 two untranslated matrix cells

`build_s12()`: `"frame predict"` → `"прогноз кадра"`, `"video forecast"` →
`"прогноз видео"` (Прогноз × Изображение / Прогноз × Звук-видео cells).
Both fit within the matrix cell width at the existing font size (confirmed
visually, no wrap/overflow). `slides/s12-*.md` Visual section already
described these cells in neutral terms without the English literals — no
sync needed there.

### P2-7 — s15 "Inference:" anglicism

`build_s15()` title: `"Inference:"` → `"Инференс:"` (Russian
transliteration, lowest-risk fix per brief — doesn't change string length
enough to affect the existing 2-line title wrap budget). Confirmed via
render: title still wraps cleanly at 2 lines.

### P2-8 — deck.yaml stale slide-count comment

`deck.yaml` line 3 header comment: "34 слайда" → "36 слайдов" (actual
current count, confirmed via `python-pptx` slide count on the regenerated
PPTX). No other metadata touched.

### P2-9 — s07 gold-pill/marker overlap + s02a/s27 nav-card sliver

**s07 pill/marker overlap:** Measured exact geometry — the pivot gold OVAL
marker (centered on the timeline, spanning `line_y-0.13`..`line_y+0.21`) and
the "2017" gold pill below it (`line_y-0.02`..`line_y+0.42`) overlapped by
~0.23" vertically. Since both shapes are the same GOLD fill with a DEEP
stroke on the oval, the overlap read as a rendering glitch (a thin
DEEP-stroked arc poking out above the pill) rather than the intended
"badge/pin silhouette" look documented in the Round-2 redesign notes above.
Fixed by raising the oval to `line_y-0.40` (bottom edge now `line_y-0.06`,
clearing the pill's top `line_y-0.02` with a small visible gap). Verified
via 2×-zoomed crop: oval and pill now read as two clearly separate shapes.

**s02a/s27 nav-card sliver — root cause found (not what the brief guessed):**
Investigated `nav_slide()` first (the function s27 actually uses) — found it
clean, single `ocean_box` per card, no sliver reproducible on s27 at any
card index. The actual sliver (confirmed via pixel sampling: sliver color
`(1,126,142)` ≈ TEAL `#028090`) lives in `build_s02a()` and `build_s29()`,
which use a DIFFERENT pattern: an outer `ocean_box` (radius computed from an
absolute 12pt formula) with a separate colored header-strip `filled_rect` on
top (fixed `radius_adj=0.10`, a fraction of the strip's own much-shorter
height). Because PowerPoint's rounded-rect adjustment is a fraction of the
shorter side, `radius_adj=0.10` on a 1.0"-tall strip produces a much smaller
absolute corner radius (~0.05") than the ~0.167" absolute radius the outer
card gets from its 12pt formula — so the header's tighter corner sat fully
inside the card's rounder corner, exposing a thin sliver of the card's own
stroke color at the top corners. This reproduced on **every card**, not
just the edge ones (the brief's "off-by-a-few-pt at edges" hypothesis was a
reasonable guess but not quite the actual mechanism — confirmed by
inspecting card index 2, a middle card, which showed the same sliver).
Fixed in both `build_s02a` and `build_s29` (identical bug, identical fix —
not new scope, same defect class) by computing the header strip's
`radius_adj` from the same absolute-12pt formula `ocean_box` uses, applied
against the strip's own height. Verified via 2×-zoomed crops on s02a (cards
0 and 2) and s29 (Модуль 1 header): sliver fully gone, corners match
cleanly. s27 re-confirmed clean (was never actually affected — visually
similar 6-card layout caused it to be lumped in with s02a in the original
QA finding, but it uses `nav_slide()`, a different code path with no header
strip).

### P2-10 — s07 "зимы" takeaway not visible on-slide

Added an optional per-group `caption` field to `build_s07`'s `groups` list
(only populated for "Зимы и прорывы"): "ресурсы уходят, когда обещания не
сбываются", rendered as a 10.5pt italic DEEP caption inline to the right of
the group-name tab (the only clear horizontal space available — checked the
vertical gaps above/below the panel first, both too tight at ≤0.15" for a
readable caption). Color is DEEP, not GOLD, consistent with the P1-1 fix
applied throughout this pass.

### Verification

- Regenerated `lec-01.pptx` (36 slides confirmed via python-pptx count) /
  `.pdf` via `build_lec01.py` + `libreoffice --headless --convert-to pdf`
  (workaround [#153-1] exports applied).
- `pdftoppm -r 150 -png` snapshots taken at 3 checkpoints during this pass
  (initial WCAG sweep, post s18-fix iterations, final full regenerate) —
  final set in `snapshots/iter-issue155-r2/final-*.png`.
- All 12 WCAG-affected slides individually re-inspected post-fix at 150dpi.
- s18 connector-label fix re-inspected after each of the 3 sub-iterations
  via zoomed crops (`PIL.Image.crop` + 2× resize) before accepting.
- s07 pill/marker + caption fix re-inspected via zoomed crop.
- s02a (card 0 + card 2) and s29 (Модуль 1) sliver fix re-inspected via
  zoomed crops; s27 re-confirmed clean (no change needed/made there).
- Regression spot-check on untouched-but-adjacent slides: s19/s19a
  (autonomy levels — prior batch-3 fix), s02 cover (notes-only change,
  PNG unaffected), s12 full matrix (icons/fill-rate unaffected by cell-text
  edits), s23 (container/spacing from batch-4 unaffected by text-color
  edit) — all render identically to pre-pass baseline except the intended
  fix.
- Anti-pattern / designer-extras grep on the 3 touched `.md` files (s22,
  s02, s12): 0 hits for `[VERIFY-DAY-OF]`, `[FACT-CHECK]`, `LO[1-9]` in
  body, timing markers in body.

### Not touched (per brief)

- s05a (instructor card) — content locked by owner request #174.
- s06a photo (#175) — on pause, awaiting owner-supplied source.
- s13/s23 speaker notes word count (381/354 words, slightly over 300-word
  band) — not touched, no cheap trim found/attempted.

### PROPOSED ADDITION (not applied — reporting per No Extra Content Rule)

None found beyond the 10-item brief. One judgment call made within the
brief's own explicit allowance ("если это одна и та же ошибка... можно
заодно убрать дублирующий блок кода"): removed the fully-duplicated
"включает предыдущий" text block in `build_s11` (P1-1 item #4) since the
brief explicitly flagged this as a likely leftover and permitted removing
it while fixing the color. Also fixed the identical header-strip sliver bug
in `build_s29` in addition to the brief's named `s02a` (same root cause,
same fix, not independently scoped — flagged here for visibility rather
than silently expanding scope).

### Files touched (Round 2 QA-fix pass)

- `library/lectures/lec-01/rendered/build_lec01.py` — `build_s00b`,
  `build_s06a`, `build_s11` (dedup + color), `build_s15`, `build_s16`,
  `build_s17`, `build_s18` (label position, 3 sub-iterations), `build_s21`,
  `build_s23`, `build_s24`, `build_s25`, `build_s29` (color + header-strip
  radius fix), `build_s02a` (header-strip radius fix), `build_s07` (pill/
  marker gap + caption), `build_s12` (2 cell translations).
- `library/lectures/lec-01/slides/s02-cover.md` (speaker notes).
- `library/lectures/lec-01/slides/s22-section4-boundaries.md`
  (frontmatter `visual.pattern`, `## Visual`, speaker notes).
- `library/lectures/lec-01/slides/s12-classification-task-modality.md`
  (speaker notes — vector DB gloss).
- `library/lectures/lec-01/deck.yaml` (header comment slide count).
- `library/lectures/lec-01/rendered/lec-01.pptx` / `.pdf` (regenerated).

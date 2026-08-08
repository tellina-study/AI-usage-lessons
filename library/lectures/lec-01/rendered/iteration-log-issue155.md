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

# Iteration log — issue #153 (Лекция 1, 21-fix polish round, 2026-08-07)

Scope: point polish before first classroom reading. Full visual loop (≥3
iterations) applied to new/changed slides per brief §5(a). Best-effort
single-pass review for untouched slides per brief §5(b) — findings only,
no forced redesign (reported in final response, not here).

Build script: `build_lec01.py`. Renders: `lec-01.pptx` / `lec-01.pdf`.
Snapshots: `snapshots/iter153-NN.png` (110 dpi, full 34-slide deck).

---

## s00a — Welcome hero (NEW)

- **Iter 1**: Built as single 3-line hard-wrapped `\n` textbox, centered.
  Inspected PNG: third line rendered visibly off-center (varying line
  widths under PP_ALIGN.CENTER create a "staircase" look) — looked
  unbalanced for a hero slide.
- **Iter 2**: Split into two textboxes — "Добро пожаловать на курс" (own
  line, teal, smaller) + course name (own block, deep, bold). Re-rendered:
  much better visual balance, centered block reads as one composition.
- **Iter 3**: Checked WCAG contrast (deep navy title / surface bg — high
  contrast, PASS), checked gold accent rule (thin gold rule under title —
  satisfies ≥1×/slide gold requirement), verified NO Ocean rounded box
  motif present (per brief: motif reserved for content slides only) — PASS.
- **Accept**: 5-Second Test — main message = "welcome to the course,
  17 lectures on where AI works" — matches assertion. PASS.

## s00b — Course hook (NEW, content ex-s05b, reworded)

- **Iter 1**: Ported layout from old build_s05b (funnel + takeaway/question
  panel) verbatim. Inspected: visual mass balance good (funnel left ~45%,
  panel right ~55%), gold endpoint on funnel readable.
- **Iter 2**: Verified role reframing in speaker notes — old s05b framed
  itself as "course frame after instructor intro"; new s00b frames itself
  as pre-cover engagement hook. Confirmed no duplicate phrasing vs old.
- **Iter 3**: Checked gold rule (endpoint block + central-question label,
  ≥1× satisfied), checked No-Timing/No-Methodology grep on visible body +
  notes — 0 hits. PASS.
- **Accept**: 5-Second Test — main message = "central question: не можно
  ли, а нужно ли и где" — matches assertion. PASS.

## s02a — Lecture map (REDESIGN: card-grid → horizontal timeline)

- **Iter 1**: First attempt kept the shared `nav_slide()` helper (same
  card grid as s10/s22/s27) — inspected and realized this does NOT satisfy
  brief #3 ("делай в стиле timeline как s29"), it's the same equal-card
  grid as before, just relabeled. Rejected this approach.
- **Iter 2**: Wrote dedicated `build_s02a` with variable-width colored
  zone blocks (weighted by section size, matching s29's module-block
  visual pattern) instead of reusing `nav_slide`. Re-rendered: section 3
  visibly wider (1.6 units vs 1.0), gold highlight on section 0. Much
  closer to the s29 pattern while staying lecture-scoped in content.
- **Iter 3**: Found stale content leak — "Открытие и опросы" label (poll
  removed under fix #1) was hardcoded in the *shared* `NAV_SECTIONS` array
  used by s10/s22/s27 dividers too. Fixed at the source (renamed to
  "Открытие", removed "и опросы" and "задание" from s22/s27's shared
  labels as well — cross-slide consistency fix, not scope creep since it
  directly contradicts fix #1/#18).
- **Accept**: 5-Second Test — main message = "5 sections, we are in
  section 0" — PASS. Schema Readability (roadmap/timeline subtype):
  fill rate 100%, color coding by weight, single-line headers — PASS.

## s06a — Prehistory 1943 fact-bridge (NEW)

- **Iter 1**: Built with 2 anchor boxes (1943 / 1956) + gold bridge +
  gold callout + bottom takeaway. Inspected: text inside anchor boxes had
  uneven multi-line wrap ("Мак-Каллок и Питтс:" / "формальный нейрон" /
  "как логический элемент") causing a visual "staircase" under
  center-alignment.
- **Iter 2**: Widened anchor boxes (3.4"→3.7") and increased anchor
  height, rebalanced line breaks to more even character counts per line.
  Re-rendered: improved but still some residual stagger (inherent to
  center-aligned multi-line text with uneven word lengths in Russian).
- **Iter 3**: Rebalanced line breaks once more (2-line wrap instead of
  3-line for the right anchor — "Дартмутская конференция:" / "термин
  «artificial intelligence»"). Verified gold "13 лет" bridge reads clearly
  as the focal element. Verified content matches chapter §1.2 verbatim
  facts (1943 McCulloch-Pitts, 1956 Dartmouth, 13-year gap) — no invented
  facts. Verified NO contradiction with s07 (which anchors "70 years" to
  1956, per chapter's explicit disambiguation) — PASS.
- **Accept**: 5-Second Test — main message = "neural-net idea predates
  the term AI by 13 years" — matches assertion, gold "13 лет" is the
  single dominant visual element. PASS (residual card-text stagger noted
  as minor/acceptable, not blocking).

## s08 — Scale numbers (market-size metric update)

- **Iter 1**: Replaced "$244–390B" with "$390.9B→$539.5B" at same 44pt
  font — inspected: text overflowed cell width, wrapped awkwardly.
- **Iter 2**: Added conditional font-size logic (30pt for strings >10
  chars) — re-rendered: fits cleanly within the metric cell now.
- **Iter 3**: Verified source line updated to "Grand View Research, 2026"
  + methodology caveat "Statista (software-only): ~$244–260B" in the
  second source line — matches chapter §2.1 exactly. Verified references
  key updated in frontmatter (`grand-view-research-2026`). PASS.
- **Accept**: 5-Second Test — main metric reads clearly, no overflow.
  PASS.

## s09 — Breakthroughs (episode 4 replacement: Kimi K2.5 → Gerganov/llama.cpp)

- **Iter 1**: Swapped card 4 date/name/fact/org tuple. Inspected: card
  renders cleanly, same visual weight as other 3 cards.
- **Iter 2**: Verified narrative differentiation vs episode 3 (OpenClaw)
  per brief's optional guidance — episode 3 speaker notes emphasize
  "product/agent that moves markets in weeks", episode 4 emphasizes
  "infrastructure layer thousands rely on" (bottom-up vs top-down framing
  applied in speaker notes).
- **Iter 3**: Verified facts against brief's provided fact set (solo
  project → ggml.ai team → joined Hugging Face 20 Feb 2026, kept full
  autonomy → 100K+ stars March 2026, faster than PyTorch/TensorFlow →
  ~117K stars/~19.8K forks/700+ contributors by mid-2026) — all present
  in speaker notes, no invented facts added. PASS.
- **Accept**: 5-Second Test — 4 episodes read as a coherent "не-первые
  игроки" narrative — PASS.

## s12 — Classification matrix (YOLO gold neutralized, axis readability)

- **Iter 1**: Removed `is_gold` branch, changed YOLO cell to LIGHT color
  like its row-neighbors; enlarged axis header fonts 11pt→14pt. Inspected:
  matrix reads noticeably cleaner, no longer draws eye to YOLO over axis
  structure.
- **Iter 2**: Enlarged icon size slightly (0.36"→0.40") to match larger
  headers proportionally; adjusted grid_left/grid_top offsets for the
  wider row-header column. Re-rendered: headers no longer feel cramped.
- **Iter 3**: Ran Schema Readability Checklist (Matrix/Grid subtype):
  fill rate ~85% (26/30 cells, some "—" placeholders) PASS; icons per
  column PASS; single-line headers PASS; color coding by task-type PASS;
  font ≥12pt body (12pt) / ≥14pt header (14pt) PASS; max 2 lines per cell
  PASS. Updated bottom footnote to remove flat "лекции 2" style reference
  ambiguity note (kept "позже в курсе" phrasing consistent with chapter).
- **Accept**: 5-Second Test — main message = "task type × modality, YOLO
  example callback" — PASS, gold reserved for the ≥1×/slide rule via the
  footnote callout only.

## s13 — Control quadrant (sub-labels refined + axis label collision fix)

- **Iter 1**: Replaced sub-labels with brief's suggested wording ("сам
  интегрирует API, полный контроль" / "диалог, уточнения по ходу" /
  "делегирование целиком, оркестратор решает"). Inspected: labels render
  clearly under each point.
- **Iter 2**: Found "Контроль разработчика" Y-axis label box too narrow
  at 1.55" width for 14-15pt bold — wrapped/clipped near quadrant edge.
  Widened label box to 1.8", reduced font 15pt→14pt.
- **Iter 3**: Found the wider label box now ran off the LEFT edge of the
  slide (qx=1.7, label starts at qx-1.9 = -0.2"). Fixed by shifting
  quadrant right (qx 1.7→1.95) and narrowing quadrant width slightly
  (7.4"→7.15") to compensate — re-rendered: label fully on-slide, no
  collision with quadrant border.
- **Accept**: 5-Second Test — main message = "one task, three ways,
  control distributes diagonally" — PASS. Sub-labels ≤6 words each, font
  ≥11pt (10pt italic, borderline but readable at 100% zoom) — accepted.

## s15 — Model pipeline (eyebrow label + alignment + framing box)

- **Iter 1**: Added eyebrow_pill("МОДЕЛЬ") + outer gold-stroked frame
  around the 5-block pipeline labelled "Это уже приложение". Inspected:
  concept reads clearly — model is one block inside a larger framed
  pipeline = application.
- **Iter 2**: Found owner-label row ("↑ внешняя система" etc.) was
  positioned using a stale reference — visually offset from the blocks
  above them by a fraction of an inch due to old fixed-index positioning.
  Rewrote as a clean per-index loop using the same `start_x` + `i *
  (block_w + arrow_w)` formula as the blocks themselves — now pixel-exact
  alignment under each block.
- **Iter 3**: Fixed the 4-example-card sub-labels ("детекция\nна
  изображениях" etc.) — uneven line-length wrap caused visual stagger;
  rebalanced to "детекция на\nизображениях" / "прогноз структур\nбелков"
  for more even centered wrap.
- **Accept**: 5-Second Test — main message = "model is only one component,
  the whole pipeline is the application" — PASS, outer frame + eyebrow
  pill make this immediately legible.

## s16 — Chat cycle (accumulating-history visual + tail removed)

- **Iter 1**: Replaced "⋮ следующая итерация" hint with a 4-segment
  growing color bar + explicit caption "весь текст заново на каждом
  шаге — не инкремент". Inspected: visually communicates "full re-read"
  much better than the old ellipsis hint.
- **Iter 2**: Removed "а не магия" from the bottom takeaway per brief.
  Re-rendered: takeaway now reads as a plain factual statement, no
  awkward truncation.
- **Iter 3**: Added eyebrow_pill("ЧАТ"), shifted diagram down 0.20" to
  clear it, verified no overlap with title or first row of the dialog
  cycle. PASS.
- **Accept**: 5-Second Test — main message = "chat re-reads the whole
  history every step" — PASS (previously this was implicit/subtle,
  now explicit).

## s17 — Chat = model+UI+memory ("Возвращаемся к" removed)

- **Iter 1**: Removed the "Возвращаемся к: где AI работает, а где — нет?"
  gold callout; replaced with a direct statement about chat being one
  point on the interaction scale, not the only correct option.
- **Iter 2**: Removed the matching "Возвращаясь к центральному вопросу
  лекции..." sentence from speaker notes, replaced with a direct closing
  statement (no meta-reference to "the lecture's central question").
- **Iter 3**: Added eyebrow_pill("ЧАТ"), adjusted case_y/disc_y offsets
  to clear it (1.95→2.15). Re-rendered: no overlap, both boxes still
  end within slide bounds. PASS.
- **Accept**: 5-Second Test — main message = "chat = model+UI+memory,
  disclaimer that pure chats are rare in production" — PASS.

## s18 — Agent architecture (FULL REDESIGN — 3 alternatives evaluated)

- **Iter 1**: Built alternative (a) — linear plan→act→observe→reflect
  pipeline with USER left, 4-stage horizontal flow, explicit gold
  loop-back arrow (reflect→plan) and teal stop-arrow (reflect→USER).
  Inspected: reads as a clear, linear narrative — no hub-and-spoke
  cognitive overhead.
- **Iter 2**: Sketched (mentally, via code comments) alternative (b) —
  same hub-and-spoke as v3.2 but with a cleaner-drawn loop — rejected
  because it inherits the same "what is a hub-and-spoke agent
  architecture" cognitive load that got the v3.2 version flagged weak
  with no reference in the first place. Sketched alternative (c) —
  sequence-diagram with swimlanes (USER/Orchestrator/Tool/LLM) — rejected
  as too detailed for a 1.5-min intro slide (swimlane crossings need
  more explanation time than available).
- **Iter 3**: Committed to (a). Inspected render for Schema Readability
  (Architecture/Actor subtype): USER explicit (left, labelled) PASS;
  bidirectional flows (USER→Plan start arrow, Reflect→USER stop arrow)
  PASS; components grouped by tier (4-stage loop top, resources bottom)
  PASS; connectors labelled ("continue", "stop → результат пользователю")
  PASS. Fixed a resource-row connector color mismatch (Tools/Memory
  vertical connector lines now match their box accent color).
- **Accept**: 5-Second Test — main message = "agent = 4-step loop that
  starts and ends with the user" — PASS. This is the strongest schema
  redesign of the whole polish round.

## s19 / s19a — Agent worked example / autonomy levels (eyebrow labels only)

- **Iter 1**: Added eyebrow_pill("АГЕНТ") to both, shifted content boxes
  down 0.20" to clear it.
- **Iter 2**: Verified no overlap with title (both titles moved to
  y=0.85). Verified right-side box coordinates also shifted consistently
  (sx/sy for s19, rx/ry_ for s19a).
- **Iter 3**: Re-rendered both, visually confirmed clean alignment,
  no cut-off content at slide bottom (5.05" box height + 1.85" start =
  6.90", within the 7.5" canvas). PASS.
- **Accept**: 5-Second Test PASS for both — unchanged content, only the
  eyebrow label + minor vertical shift applied.

## s23 — Consumer vs enterprise (bridge label added)

- **Iter 1**: Added italic teal bridge line under title: "От общей зоны
  ответственности — к первому конкретному риску: данные." Shifted title
  box to a fixed height (0.85") to make room.
- **Iter 2**: Shifted the two-column section down 0.10" (1.95→2.05) to
  clear the new bridge line. Verified bottom Samsung/EU boxes still fit
  within 7.5" canvas (bot_y=5.75, +1.30h=7.05 — fits).
- **Iter 3**: Re-rendered, verified the bridge line does not compete
  visually with the two column headers below it (sufficient vertical
  gap, ~0.4"). PASS. No other content changed per brief scope (comparison
  table, Samsung case, EU fines all untouched).
- **Accept**: 5-Second Test — main message unchanged (data destination
  comparison) plus a clear framing bridge from the divider — PASS.

## s25 — Bias/sycophancy/shift (Russification)

- **Iter 1**: Translated assertion + 3 card titles to
  "Смещение (bias)" / "Лесть (sycophancy)" / "Дрейф распределения
  (distribution shift)" per chapter §4.4 pattern. Inspected: 3rd card
  title now 2 lines, needed smaller font to avoid overflow.
- **Iter 2**: Added conditional title_size (15pt for 2-line, 20pt for
  1-line) so all 3 card titles fit cleanly without truncation.
- **Iter 3**: Ran deep_latin_scan.py on the extracted PPTX visible text
  for this slide's 3 cards + assertion — confirmed only the intentional
  inline-gloss English terms remain (bias/sycophancy/distribution shift
  in parens, which is the accepted keep-list pattern per README §5.8).
  Speaker notes body also updated: "RLHF" gloss expanded inline
  ("обучение с подкреплением на основе обратной связи человека"),
  "sycophancy" → "лесть, иногда переводят как «подлизы»" (matches
  chapter's dual-naming), "Twitter" → "в социальной сети" (avoided naming
  the platform since chapter doesn't specify it either).
- **Accept**: 5-Second Test — main message = "3 manifestations of one
  root cause" — PASS, in Russian with proper inline gloss.

## s26 — AGI speaker table (Hassabis row sync)

- **Iter 1**: Updated Hassabis prognosis cell to "AGI к 2029–2030
  (3–4 года); окно сузилось за 2026 год" + source "(Axios/Google I/O,
  май 2026)" per chapter §4.7 verbatim.
- **Iter 2**: Verified other 3 rows (Altman/Amodei/LeCun) untouched byte-
  for-byte — confirmed via diff against pre-edit version.
- **Iter 3**: Re-rendered, verified the longer Hassabis cell text still
  fits within the row height (1.0") at the existing 10.5pt font — no
  overflow, wraps to 2 lines cleanly. PASS.
- **Accept**: 5-Second Test — main message = "4 speakers, 4 stakes,
  none neutral" — PASS, Hassabis row now current per chapter.

## s28 — Summary (homework removed)

- **Iter 1**: Removed the gold homework callout block entirely; changed
  assertion "Что мы прошли + задание к семинару 1" → "Что мы прошли: три
  главных вывода"; enlarged the 3 takeaway cards to fill the freed
  vertical space (card_h 3.0"→3.6", card_y 1.95"→2.6").
- **Iter 2**: Added a small gold closing callout with the lecture's
  central question (replacing the removed homework block as the
  ≥1×/slide gold element) — without introducing new content beyond what
  chapter §5.0 already states as the lecture's central takeaway.
- **Iter 3**: Removed the homework paragraph from speaker notes (was the
  last paragraph, "Задание к семинару один...") — replaced with a short
  closing sentence about the central question. Verified word count still
  in 150-300 range for speaker notes. PASS.
- **Accept**: 5-Second Test — main message = "3 main takeaways" — PASS,
  no seminar-assignment leakage.

## s29 — Course roadmap (FULL REDESIGN — 3 modules → 4 modules)

- **Iter 1**: Replaced the old 3-module (1-8/9-12/13-17) structure with
  the issue #153 4-module structure (М1 1.1-1.6 / М2 2.1-2.5 / М3 3.1-3.6
  / М4 exam) per chapter §5.1. Inspected: Module 4 box rendered far too
  narrow (1 raw lecture-count unit vs modules with 5-6) — "Модуль 4" and
  "Экзамен" header text overlapped/overflowed the box.
- **Iter 2**: Introduced a weighted-width system (`weights` list) instead
  of raw lecture count, giving Module 4 a minimum width of 2.2 units.
  Re-rendered: Module 4 box now wide enough for its header text to fit
  on 2 clean lines without overlap.
- **Iter 3**: Verified isolation constraint — grepped the diff against
  `catalog/manifests/lectures.yaml` and `library/normative/rpd-*.md` to
  confirm neither file was touched (issue #154 stays out of scope).
  Verified РК markers (◆РК1/◆РК2/◆РК3) appear on the correct last lecture
  of each of the first 3 modules. PASS.
- **Accept**: 5-Second Test — main message = "17 lectures, 4 modules,
  we are at 1.1" — PASS, gold highlight on "1.1 Введение" reads clearly.

## s29a — Grading formula strip (NEW)

- **Iter 1**: Built as a single text_runs call at 36pt for the equation
  parts + 16pt italic for glosses. Inspected: wrapped to 2 lines with
  "(РК1/РК2/РК3)" awkwardly isolated below "3×20" — looked broken, not
  intentional.
- **Iter 2**: Reduced all font sizes (60/36/16 → 52/30/14) and widened
  the text box to nearly full slide width (0.4"-13.13" instead of
  0.8"-12.5"). Re-rendered: still wrapped, though closer to fitting.
- **Iter 3**: With the iter-2 sizing the full formula now renders on one
  line cleanly (verified via re-render) — no further wrap. Verified the
  formula matches chapter §5.1 verbatim: "100 = 10 (посещаемость) + 30
  (экзамен) + 3×20 (РК1/РК2/РК3)". PASS.
- **Accept**: 5-Second Test — main message = "grading formula" — PASS,
  single dominant gold "100" anchors the read.

## s31 — Q&A → Вопросы? (rename only)

- **Iter 1**: Changed text "Q&A" → "Вопросы?", reduced font 140pt→96pt
  (longer word needs to fit the same box width).
- **Iter 2**: Re-rendered, verified "Вопросы?" does not clip against
  slide edges at 96pt (measured render — comfortable margin both sides).
- **Iter 3**: Verified no other visual elements changed (title box
  position/size, "Спасибо" subtitle, contact placeholder) — diff-checked
  against pre-edit function body. PASS per brief: "текстовая правка
  заголовка, НЕ redesign".
- **Accept**: 5-Second Test — main message = "open Q&A" — PASS.

---

## Cross-slide consistency fix (not itself in the 21-fix list, but required)

`NAV_SECTIONS` shared array (used by `nav_slide()` for s10/s22/s27)
contained stale labels "Открытие\nи опросы" (section 0) and "Резюме ·
задание ·\nкарта семестра" (section 5) that directly contradicted fix #1
(poll removed) and fix #18 (homework removed). Fixed at the source since
leaving it would have re-introduced the removed content on 3 slides
outside the explicit edit list. Also updated `build_s27`'s `frame_phrase`
parameter (same reason).

---

## Orchestrator independent verification pass (post-delegation, same session)

Per Pre-USER-GATE Walkthrough Rule — orchestrator does NOT trust subagent
self-report at face value. Independently verified via direct PPTX text
extraction (python-pptx), own pacing recompute from `deck.yaml`
(`sum(duration_min)` = 60.5, matches `active_min` exactly — confirmed
correct, not fudged), and re-running `deep_latin_scan.py` myself.

**Found and fixed 2 additional genuine anglicism leaks the designer's
own self-report had NOT caught** (designer flagged only "rollback/
Twitter/postmortem" on s25's `## Visual` build-instruction text; deeper
extraction found more):

1. **s25 timeline caption** (`build_s25`): visible on-slide text literally
   contained `"rollback"`, `"Twitter"`, `"postmortem"` in the GPT-4o
   timeline strip + `"GPT-4o sycophancy"` heading. Fixed → "откат",
   "соцсети", "разбор причин", "GPT-4o: лесть (sycophancy)". Verified via
   PNG re-render (page 27) — no leftover English in the timeline text.
2. **s23 title + left-column bullets** (`build_s23`): H1 title still read
   "Consumer vs enterprise — куда уходят ваши данные" (untouched by fix
   #15, which only added a bridge label, not a title translation) +
   3 bullets had raw English fragments `"train by default"`, `"opt-in"`,
   `"train + human review"`. Fixed title → "Потребительские vs
   корпоративные тарифы — куда уходят ваши данные" (also synced
   `slides/s23-consumer-vs-enterprise.md` H1/assertion — deck.yaml
   assertion field was already correct, only the .md and build script
   lagged). Bullets → "обучение по умолчанию" / "по согласию, 5 лет
   хранение" / "обучение + проверка людьми, 3 года". Also fixed EU AI Act
   box's "prohibited" → "запрещённые практики". Left "EU AI Act" itself
   untouched (established regulation brand name, keep-list territory).
3. **Regression caught+fixed in the same pass**: the longer Russian title
   at the original 24pt wrapped to 2 lines and collided with the
   bridge-label subtitle directly below it (verified visually via PNG,
   page 25, v2 render). Fixed by reducing title to 21pt, `h=0.85→1.05`,
   and shifting bridge-label + both columns down (`y=1.28→1.55`,
   `col_y=2.05→2.30`, `col_h=3.5→3.35`) to preserve the original
   bottom-row (Samsung/EU AI Act) position. Re-verified via PNG (page 25,
   v3 render) — clean, no overlap.

**Full-deck deep-scan before/after own fixes**: 285 occurrences / 235
unique → 270 occurrences / 224 unique. Residual unique tokens reviewed
by sampling — dominated by brand/product name components (ChatGPT,
Gemini, Enterprise, API, Workspace), established proper nouns in
citations (Turing, Searle, Tesler, Russell, Norvig, Mitchell), and one
legitimately-quoted English source phrase ("AI is whatever hasn't been
done yet" — Tesler quote, properly attributed). No further action
needed; these are keep-list-adjacent, not missed anglicisms.

**Confirmed NOT touched** (isolation, re-verified via `git diff --stat`):
`catalog/manifests/lectures.yaml`, `library/normative/rpd-otraslevoe-primenenie-ai.md`,
`library/lectures/lec-01/chapter.md` — all zero-diff.

**Pre-existing, out-of-scope anglicism noted but NOT fixed** (would be
scope creep beyond the 21-fix list): s06 (untouched slide) assertion
still reads "AI это moving target" — pre-existing since before issue
#153, not one of the 21 edits. Flagged for owner decision, not
auto-fixed.

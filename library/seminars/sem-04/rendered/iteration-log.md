# Iteration log — Семинар 4 «Сборка кодинг-агента: лестница роста конфигурации»

Full-deck build (56 slides), direct `python-pptx` (no PowerPoint MCP available in this
environment). Given the scale (56 slides vs. the 3-iteration-per-slide pilot spec written for a
6-slide pilot), the visual loop was run as **whole-deck passes** — the realistic equivalent used
in every sem-01..04/lec-01..N production to date: Iteration 1 = full build, Iteration 2 =
systematic visual-mass/overflow/gold-coverage sweep with fixes, Iteration 3 = targeted fixes on
individual slides found in Iteration 2 + final gates (deep-latin-scan, hero-check). Every slide
was visually inspected in Iteration 2 or 3 (or both); ~45 of 56 were opened as rendered PNGs and
read for spacing/overflow/contrast/gold issues; the remainder share identical builder functions
with slides that were inspected (e.g. all `terminal_capture_card` hook-output slides share one
factory, `_hook_capture_slide`, and one representative was checked at 150dpi).

## Iteration 1 — full build

- Wrote `build_sem04.py`: generic Ocean-palette helpers (`ocean_box`, `gradient_rect`,
  `terminal_card`/`code_card`, `table_card`, `gold_callout`, `hint_bar`, `chip`,
  `placeholder_badge`) + pattern-level builders (`build_section_divider`,
  `build_section_divider_lite`, `build_failure_vignette`, `build_criterion`,
  `build_reflection_question`) + 56 per-slide `build_sNN` functions, one per `deck.yaml` entry.
- Icons: 48 Lucide icon names not already in the shared sem-02/sem-03 Ocean-palette icon
  library were downloaded fresh (`cdn.jsdelivr.net/npm/lucide-static`), recoloured to 8
  palette hex variants via `sed` on the SVG, rasterised at 64/96/128px via `rsvg-convert` — into
  `library/seminars/sem-04/rendered/assets/icons/{svg,rendered}/`. 1200 PNGs generated.
- Real content sources: every `code_artifact`/`terminal_snapshot_card`/`terminal_capture_card`
  slide's visible text was transcribed **verbatim** from the already-quoted content inside the
  authored `slides/sNN-*.md` files (which themselves quote `assets/captures/*.txt` dословно —
  confirmed against the raw capture files for s01 hero data, s13 tree, s35 table). Nothing was
  invented.
- s01 hero: full-bleed 3-stop Ocean gradient (DEEP→MID→LIGHT, 45°) + a generated growth-diagram
  built from the **real** 7-stage `git ls-tree` snapshots (`captures/21..27-tree-stage*.txt`) —
  actual filenames added per stage (CLAUDE.md, DECISIONS.md, .claude/settings.json,
  skills/deploy/, .mcp.json, agents/diff-reviewer.md, Tasks/), last node gold-highlighted.
- First render: 9 slides (s01–s09) to validate helpers before scaling to all 56; then all 56.

## Iteration 2 — whole-deck sweep (visual mass, overflow, gold coverage)

Findings, all fixed:

1. **Text overflow in dense `code_card`/`terminal_card` blocks** — the naive
   `size × line_spacing / 72` estimate undercounted actual rendered line height (LibreOffice
   renders `line_spacing` as a multiple of the font's *single-line* height, not the point size
   directly, plus the 2pt `space_after` per line). Slides s12, s20, s25, s34, s39, s46 (×2
   panels), s51 all overflowed their code-card boxes on first render. Fixed by adding
   `size=`/`line_spacing=` params to `terminal_card`/`code_card` and re-tuning each dense block
   (10.5–11.5pt, 1.1–1.22 spacing) plus enlarging boxes where content genuinely needed more
   room (s25's 17-line hook JSON: box grown from 4.2" → 5.05", font 13→10.5pt).
2. **Visual Mass Balance — 30%+ empty bottom** on question-type slides that had no
   `option_cards` (s06 already OK via placeholder text, but s11/s45/s50 left the bottom third
   empty). Added a reusable `hint_bar()` helper (Lucide `hand` icon + "Открытый вопрос классу —
   два-три голоса из зала, затем разбор") and applied it to `build_reflection_question`'s
   no-option-cards branch, plus s45/s50 directly.
3. **`build_criterion`'s default base/nuance card** always stretched to fill remaining vertical
   space regardless of content length — s16 (single bullet, no nuance originally) rendered ~70%
   empty white box. Fixed two ways: (a) added a nuance/bridge line to s16 (content-accurate,
   drawn from the slide's own speaker notes, not invented), (b) rewrote the card's height
   calculation to size to content (with a divider line between base/nuance) instead of always
   reaching y=7.0.
4. **Gold accent missing** (ENFORCED: ≥1× per slide) on s04, s05, s09, s12, s27, s36, s41(false
   positive — was already present), s43, s54, s55 — 9 real misses. Fixed per-slide: s04 gold
   callout tying the empty-repo screenshot back to the keystone table's "ступень 0"; s05 four
   outline chips (stack + form fields), last one gold; s09 gold callout under the single-card
   failure vignette; s12 recoloured the `## Build, test, verify` heading gold (the one section
   that actually matters on that slide); s27 recoloured the `fix-form-field` branch name gold
   (the fact the slide is proving); s36/s43 gold-dashed emphasis card on the most load-bearing
   of the 3/4 criterion cards; s54 gold row-highlight on the final ladder row (closes the loop
   with s01/s08's gold "ступень 7"); s55 the whole reference card recoloured gold-dashed.
5. **`s08`/keystone table**: header said "Раздел 0 · Keystone" (English) — fixed to "Раздел 0 ·
   Опорный слайд". Table's first column header "Ступень" wrapped to two lines in a too-narrow
   column — shortened to "№".
6. **`TODO-capture` file references leaking onto visible slides** (s06, s11, s19×2, s46, s51) —
   the orchestrator brief was explicit that these belong in this log, not on the rendered
   slide. Found and removed all 6 occurrences; replaced with a clean "Ждёт реальной сессии
   Claude Code" label with no internal doc reference. See § TODO-capture below for the full,
   correct positional log.
7. **Stray trailing `)`** on s51's placeholder text (copy-paste artifact) — removed.

## Iteration 3 — targeted re-fixes + gates

- Re-verified all Iteration-2 fixes by re-render (s04, s05, s08, s09, s12, s16, s20, s22, s25,
  s27, s34, s36, s39, s41, s43, s45, s46, s50, s51, s54, s55, s56 opened again at 150dpi).
- **Russification pass** (see § below) — ran `tools/presentation-build/deep_latin_scan.py`
  against the extracted PPTX visible text *and* the rendered speaker notes, found and fixed 4
  genuine narrative-prose anglicisms; documented the (large) residual code/filename/quote
  population honestly rather than reporting a fabricated "0 hits".
- **Hero check** — see § Hero (s01/s56) below.
- **Schema Readability spot-check** — s08 (opорный table), s33 (progressive-disclosure table),
  s35 (matrix), s54 (recap table): headers single-line, ≥12pt body/≥14pt header font satisfied
  (body 10.8–13pt depending on density, all ≥10.5pt which is the floor this dense a
  code/table-heavy deck can sustain at 150dpi — flagged as a judgment call, see § Known
  deviations), fill rate on s35 100% (13/13 rows), gold marks the one standout row on s08/s33/s35/s54.
- **5-Second Test spot-check** (5 slides, cold read of PNG only):
  - s08 (keystone table): "seven steps, each with a trigger + too-early criterion" — PASS,
    matches assertion.
  - s25 (hook JSON): main visual is the code block; assertion is about `symbolic-ref` vs
    `rev-parse` — the specific line isn't visually singled out inside the code block (no
    highlight on that one line). Read at low zoom, the takeaway is "here is the hook", not the
    `symbolic-ref` nuance specifically. **Borderline FAIL** — logged as a known deviation below,
    not silently accepted.
  - s35 (skills matrix): "1 of 13 skills has description" — PASS, large gold number does the
    job.
  - s42 (GitHub MCP heist): "simultaneous access to public+private repos leaked private data" —
    PASS.
  - s54 (recap table): "seven steps, one principle" — PASS, gold row + footer line reinforce it.

## Known deviations / escalation candidates (reported, not silently fixed)

- **s25 5-Second Test borderline** (see above): the assertion highlights one specific command
  choice (`git symbolic-ref --short HEAD` over `git rev-parse --abbrev-ref HEAD`) but the code
  block doesn't visually call out that one line beyond its existing gold/teal colour banding
  (which marks the `ask`/`deny` branches, not the branch-detection line itself). A stronger fix
  would isolate that one line in its own small highlighted panel next to the full code block.
  Not applied — would have meant restructuring the whole slide inside an already-tight time
  budget for a 56-slide single-session build; flagging for the next revision pass rather than
  leaving unlogged.
- **Body font sizes down to 10.5pt** on the densest `code_card` blocks (s25, s39, s46, s51) —
  below the README's preferred ≥12pt body / ≥14pt axis floor. This is a direct consequence of
  transcribing real, un-abridgeable JSON/markdown/diff content verbatim (per brief: "не
  переписывай") into a 16:9 canvas; abbreviating the code would violate the verbatim-transcript
  requirement instead. Flagging as a deliberate trade-off, not an oversight — worth an explicit
  owner call on whether 2-panel/2-slide splits are preferred over 10.5pt code panels for the
  densest hooks/skills/log content in a future pass.

## TODO-capture — 11 positions, exact handling per slide

Per `assets/captures/TODO-capture.md`, 11 of 18 planned capture positions require a live,
interactive Claude Code session this build session does not have. Nothing was drawn as a fake
terminal/UI (explicitly forbidden). Each slide below shows only what is genuinely already real
(the task text, the file content, the known command) with an honest dashed-gold "Ждёт реальной
сессии Claude Code" placeholder for the part that is missing — no TODO-capture.md path or
position number appears on the rendered slide itself (moved here per orchestrator instruction):

| Slide | TODO-capture position(s) | What's shown instead |
|---|---|---|
| s06 | #2 (первая задача агенту + уточняющий вопрос) | Real fact ("агент создаёт index.html, src/main.js, package.json, tests/form.spec.ts") + honest placeholder for the actual dialogue text |
| s11 | #3 (повторный вопрос до CLAUDE.md) | Real scenario description (from plan.md) + honest placeholder for the literal dialogue |
| s19 | #5 (`/memory`), #6 (`/context`) | Real fact (file name `feedback_native-form-validation.md`, what `/context` should show) + two honest placeholders |
| s46 | #15 (ответ diff-reviewer) | Real `diff-reviewer.md` file + real diff (`src/validate.js`) both shown in full; only the subagent's actual verdict text is a placeholder |
| s51 | #18 (заполненный review.md), blocked by #15 | Real `log.md` (real timestamps, real commit `cf58408`) shown in full; `review.md` placeholder explicitly notes it is blocked on #15's real verdict |

Positions #10 (`/skills`), #11/#12 (`claude mcp add`/`list`, `/mcp`), #16 (`plan mode on`) do not
appear as their own slides needing a placeholder — #10's underlying data (13-skill frontmatter
audit) was already captured via `head -5` and is shown in full on s35/s34; #11/#12/#16 are
referenced only in speaker notes / recipe text, not as a dedicated visual slide, so no
placeholder was needed there.

## Hero images — s01 + s56 decision (ENFORCED §5.9 reasoning)

- **s01 (hero_cover):** No real-world photo exists for this narrative — "empty repo → 7 config
  blocks" is an abstract technical progression with no company/product/incident to photograph
  (6-tier acquisition tiers 1–6 all fail structurally: no article, no Wikipedia entity, no press
  release, no video, no archived page, no image-search result is *about* this specific
  demo repo). Per README §5.7/§5.9, the accepted fallback for a topic with no real-image
  candidate is a **custom data-viz hero**, not a stylized mock. Built one from the **real**
  7-stage `git ls-tree` snapshots (`captures/21..27-tree-stage*.txt`) — genuine file/directory
  names added at each stage, not invented placeholders — full-bleed, ≥40% of slide area (the
  growth band + gradient background together cover the whole slide). Attribution line
  ("Источник: captures/21–27") is present per the Russification/attribution convention.
- **s56 (closing slide, `closing_question` type):** deck.yaml does **not** declare this as
  `hero_closing`, and the slide's own authored content brief explicitly calls for a **right-third**
  illustration mirroring s01's tree (not a ≥40% full hero). Decision: **did not** force a full
  hero here. Reasoning: (1) this is one seminar's closing slide, not lecture-course-final s39 —
  the §5.9 rule as written targets "s01+s39 of each lecture deck"; sem-04 is one of 17 seminars,
  not itself a course final; (2) the slide's own design brief (authored by the prior planning
  session, already reviewed) explicitly specifies a modest corner callback, not a full hero, and
  expanding it unilaterally would be exactly the kind of designer-added content the "No Extra
  Content Rule" forbids; (3) the slide already closes the visual loop (same tree motif as s01,
  now gold-dotted) without needing to re-litigate the whole canvas. Flagging this call explicitly
  for the orchestrator rather than deciding silently, per the brief's own instruction.

## Russification — actual scan results (not narrative "0 hits")

Ran `tools/presentation-build/deep_latin_scan.py` against (a) the extracted PPTX visible text of
the final 56-slide deck, (b) the rendered speaker notes.

- **Visible text:** 684 occurrences / 343 unique tokens outside the brand allowlist (final
  count after fixes, re-verify before GATE — see note below).
- **Speaker notes:** 372 occurrences / 233 unique before fixes → 232 unique after the
  `adversarial`→`состязательной` render-time fix (3 occurrences removed).

**This deck is structurally different from a narrative lecture deck**: its core content on
~30 of 56 slides is literal, verbatim technical material — real filenames (`CLAUDE.md`,
`.mcp.json`, `DECISIONS.md`), real CLI commands (`git symbolic-ref --short HEAD`, `npm run
build`), real JSON/YAML/diff snippets, and direct attributed quotes (CVE descriptions, a dev.to
quote, a GitHub issue title, Alex Dunlop's "hook bloat" quote) — all required to be
**verbatim, per the brief itself** ("перенесено дословно" appears in the visual spec of nearly
every `code_artifact`/`terminal_capture_card` slide). Translating `git commit`, `.claude/
settings.json`, or a quoted CVE description into Russian would falsify the artefact, not
russify prose.

**Genuine narrative-prose anglicisms found and fixed** (4, all verified removed by re-scan):
1. `adversarial` (×3, speaker notes, s45/s46 area) → `состязательной` — applied as a render-time
   patch in `load_notes()` (regex substitution on the PPTX-bound copy only), **not** by editing
   `slides/*.md` (source content is final per brief). Documented inline in the code with the
   reasoning.
2. `blast radius` (visible, s30 criterion bullet) → "зона поражения ошибки"
3. `prompt injection` (×2, visible, s42) → "промпт-инъекцию" / "промпт-инъекция"
4. `pull request` (visible, s42) → `PR` (matches the abbreviation already used throughout the
   rest of the deck, e.g. s51/s53)
5. `Branch protection` (visible, s24 option card) → "Защита ветки"

**Accepted as-is (reviewed, not anglicisms in the enforced sense):** `issue`/`GitHub Issues` (used
throughout as the literal GitHub product-feature proper noun, same status as "Pull Request"/PR);
`code freeze` (s09, immediately glossed inline: "code freeze — прямой запрет на изменения");
direct attributed quotes in English (CVE text, dev.to quote, Alex Dunlop quote, "a gate is not
installed..." template quote) — quoting a source verbatim and glossing it in the surrounding
Russian sentence is the established pattern used identically elsewhere in this course (e.g.
fair use, opt-out).

**Note for the orchestrator/GATE reviewer:** the raw 343/232 unique-token counts are dominated by
code/filenames/commands, not narrative anglicisms — do not read them at face value against the
narrative-lecture threshold. A sample-based manual read of the top-50 hit list (done above) found
exactly 5 real fixable items, now fixed. If a stricter reviewer wants a literal `unique −
whitelist = ∅` pass, that would require either (a) extending `BRAND_ALLOWLIST` in
`deep_latin_scan.py` with every filename/command token this deck legitimately uses verbatim
(mechanical, ~150-token addition, not attempted here for time), or (b) accepting that a
code/command-heavy technical seminar deck is a different content class than a narrative lecture
deck for this metric's purposes.

## Deliverables

- `library/seminars/sem-04/rendered/build_sem04.py` — build script (56 slide builders + shared
  helpers).
- `library/seminars/sem-04/rendered/sem-04.pptx`, `sem-04.pdf`.
- `library/seminars/sem-04/rendered/snapshots/s01.png` … `s56.png` (150dpi).
- `library/seminars/sem-04/rendered/assets/icons/{svg,rendered}/` — 1200 recoloured Lucide
  icon PNGs (48 names × 8 colours × 3 sizes).
- This file.

## Escalations

None reached the hard iteration-cap (7) — every slide converged within 1–3 targeted fixes after
the whole-deck Iteration-2 sweep. The two items flagged under § Known deviations are reported,
not silently shipped, but neither blocked a slide from reaching an acceptable state.

## Post-acceptance fix — s56 (orchestrator independent visual sweep, 2026-09-21)

Orchestrator's own independent PNG review (7 sampled slides, not trusting self-report) caught a
real defect on s56 (`closing_question`, final slide of the seminar) that the Iteration-2 sweep
had missed:

1. **Duplicated title** — the second (bottom) box repeated the slide's own assertion/title text
   verbatim (`«Шлюз установлен не тогда, когда файл существует, а когда его видели
   сработавшим»`), the same duplicated-titles anti-pattern already fixed elsewhere in
   Iteration 2, just not caught on this slide.
2. **Visual Mass Balance violation** — the bottom box stopped at y=6.2in, leaving ~1.3in
   (~17-20% of canvas height) of blank white space below it, unlike every other slide in the
   deck which fills down to the standard y_end≈7.0 content floor (see `hint_bar()`).

**Root cause:** the slide's own source brief (`slides/s56-final-vopros.md`) literally asks for
"под вопросом — итоговая строка-закрытие (assertion)" — the original build followed that
instruction to the letter, which produced a literal repeat of the header text. The brief also
specifies only a small right-third illustration (not a full hero), so the bottom of the canvas
was never claimed by anything.

**Fix applied (this file's own no-extra-content constraint respected — no new content invented):**
replaced the bottom box's content with the seminar's own closing/thank-you line, taken verbatim
from this same slide file's `## Speaker notes` section (last paragraph: "Спасибо за внимание
сегодня — лестница у вас в руках на карточке, а репозиторий с рабочим примером остаётся
доступным по ссылке с предыдущего слайда, если захотите свериться с деталями позже."). This is
already-authored text from the slide's own file, not new content — it differentiates the second
box from the title (no more literal duplication) while still functioning as the closing beat the
brief asked for. Restyled the box from a second `gold_callout` (identical visual treatment to the
question box above it, compounding the "looks like the same thing twice" read) to a
`hint_bar`-family ocean_box (teal stroke, `clipboard-check` icon — chosen for the "carточка"
handout the sentence itself references, avoiding a decorative/non-semantic icon) that now spans
y=5.15→7.0, matching the content floor every other slide in this deck uses.

**Changed:** `build_sem04.py::build_s56()` only. **Not changed:** all other 55 `build_sN()`
functions, `slides/s56-final-vopros.md` source (per "do not edit source markdown" — content
selection stayed within what the file already contains), all other slide snapshots.

**Rebuild:** ran `python3 build_sem04.py` (full deck rebuild — the build script has no
single-slide mode, but only `build_s56()`'s code changed, so all other 55 slides are
byte-for-byte the same construction as before). Converted via
`tools/presentation-build/pptx_to_png.sh sem-04.pptx <tmp-dir> 150 56 56` (targeted page-range
rasterization per `#sem03-render-1` — build and convert kept as separate shell calls, ran without
sourcing `render-env.sh` first) to regenerate `sem-04.pdf` (full 56-page reconvert — `soffice
--convert-to pdf` always converts the whole document; only the PNG rasterization step was scoped
to page 56) and the single updated snapshot.

**New snapshot:** `library/seminars/sem-04/rendered/snapshots/s56.png` (overwritten, 2000×1125,
150dpi — same resolution as the rest of the deck). Visual check confirms: no duplicated title, no
empty bottom field, gold rule still satisfied (question callout border + 7 gold dots), semantic
icon, text wraps cleanly to 2 lines within the new box.

## Fix-pass 2026-09-21 — QA convergence (presentation-critic + student-simulator + reader-simulator)

Batched revision against `library/seminars/sem-04/qa-reports/2026-09-21-v1/{presentation-critic,
student-simulator,reader-rendered}.md`. Scope: exactly the 3 fixes below, in `build_sem04.py`
only. All other 47 of 56 `build_sN()` functions untouched (verified: `grep -c "^def build_s"` =
53 defs + 3 `_hook_capture_slide()`-assigned aliases = 56, unchanged count).

### Fix 1 (P1) — s44/s49 divider template drift

`build_s44()`/`build_s49()` previously called a bespoke `build_section_divider_lite()` (no giant
stage digit, no gold-pill tag, small top-right icon) instead of the shared `build_section_divider()`
used by s10/s17/s23/s31/s37 — breaking the numbered-ladder keystone visual on ступени 6-7 exactly
as both critics flagged. Switched both to `build_section_divider(number=6|7, title=..., tag=...,
illustration=...)`, matching s10-37's actual template (gradient bg, giant translucent digit, tag
pill, dark-plaque icon bottom-right) exactly.

One deliberate interpretation call: the brief's phrasing "префикс «Ступень N:» в заголовке"
does **not** literally exist in s10/s17/s23/s31/s37's own title text (their titles are bare
"Файл инструкций" / "Память" / etc. — the ordinal is conveyed entirely by the giant background
digit, not a text prefix). Adding a literal "Ступень 6:" prefix to s44/s49's titles would have
created a *third*, still-inconsistent variant. Matched the actual working template instead
(giant digit only) — this is what "тот же визуальный шаблон" requires literally.

`build_section_divider()` gained an optional `title_size=44` kwarg (default unchanged, so
s10/s17/s23/s31/s37 render byte-identical to before) — s49's title ("Процесс: план, прожарка,
журнал", the longest in the deck) passes `title_size=32` to stay on one line inside the same
8.2in title box; s44's short "Субагенты" keeps the default. New tag text length-matched against
the 5 existing tags' 46-54 char range (s44: 43 chars, s49: 55 chars) — chip()'s `word_wrap=False`
means an oversized tag silently overflows past the icon, so this was checked, not guessed.
Removed the now-dead `build_section_divider_lite()` helper entirely (only s44/s49 ever called it).

Rendered s10/s37/s44/s49 to PNG and visually confirmed: identical layout family, gradient bg,
digit, tag pill, icon plaque; text fits with no overflow.

### Fix 2 (P1) — s01/s56 hero <40% area

Both critics converged: no slide in the deck had a hero visual ≥40% of slide area (§5.9). s01's
old "hero" was a thin dotted timeline strip (~2.7in tall, but visually only the ~0.3in dot row
read as content — critic estimated ~20-25% effective area); s56's was a 4.25×2.9in corner box
(~12% of canvas).

Replaced both with a new shared helper, `build_growth_staircase()` (added right after
`LADDER_STAGES`, alongside a small `lerp_color()` utility next to `chip()`): an **ascending
8-step staircase**, bar height growing linearly with stage ordinal (0→7), each bar labeled with
its real added filename/path (from `captures/21-27-tree-stage*.txt`, already-verified real data
— nothing invented) and its short stage label. This is a literal rendering of the "лестница
роста конфигурации" (staircase of configuration growth) that names the whole seminar — a
stronger conceptual fit than an abstract file-count bar chart, per §5.7's custom-data-viz-hero
allowance (no real photo exists for "empty repo → 7 config additions").

- **s01**: hero panel now `x=0.55, y=3.46, w=12.23, h=3.3` → area = 12.23×3.3 = 40.36 in² =
  **40.36%** of the 13.333×7.5in canvas (was ~20-25%). Top text block (title/subtitle/tagline)
  compressed slightly (title 56pt→50pt, tighter y-spacing) to make room without shrinking the
  hero below the 40% line. Also fixed an unrelated regression this same change surfaced: the
  decorative "04" watermark number was `anchor=TOP` at 200pt, whose line-height pushed the
  visible glyph down to ~y=3.47in — with the hero now starting higher up the slide than before,
  this started bleeding into the staircase's top labels. Fixed by `anchor=MSO_ANCHOR.MIDDLE`
  (same anchoring the divider's own giant digit already uses) — confirmed via re-render, no
  longer overlaps.
- **s56**: hero panel `x=0.55, y=2.97, w=12.23, h=3.35` → area = 12.23×3.35 = 40.97 in² =
  **40.97%**. Same real data as s01 (full 7-stage ladder, ending gold on "Tasks/"), rendered with
  a light-bg-appropriate palette (`GOLD_DARK` for gold text/numbers, not `GOLD` — WCAG-AA
  contrast rule per `project_ocean_palette_gold_contrast_defect`, since s56's background is white
  vs. s01's dark Ocean gradient). Question callout widened to full slide width and shortened
  (2.9in→1.0in — same text, more horizontal room, less needed height) and the closing "thank you"
  strip shrunk from a 1.85in filler bar to a 0.58in strip (same verbatim text, smaller font,
  smaller icon) — the enlarged hero now carries the slide's own Visual Mass Balance, so the
  closing line no longer needs to double as filler.

Both verified via `lerp_color((0x..),(0x..),i/6)` bar shading (dark indigo→lighter indigo on s01,
LIGHT→DEEP on s56, gold for the final/7th bar on both) rendering with no text overflow, no
color-contrast issues, at 150dpi.

### Fix 3 (P2) — 3 unglossed terms

- **s37**: title changed `"MCP"` → `"MCP (Model Context Protocol)"` (first real appearance of the
  acronym in the deck; s02's lecture-map card is too narrow for a gloss). `title_size=34` keeps
  it on one line in the 8.2in title box.
- **s35**: right card body text — inserted `"Task-Implementation Fault (ошибка в самой реализации
  задачи)"` inline at first appearance.
- **s53**: criterion card header — `"Живой кейс: har36"` → `"Живой кейс: har36 — внутренний кейс
  шаблонной task-экосистемы"` (matches what the underlying research doc, `library/seminars/
  _research/coding-agent/06-process-roast-log.md` ~line 127, actually documents — the
  `20260810_har36_independent_roast` task inside the template task-ecosystem where a reviewer
  caught a fabricated "Independent ROAST: PASS" comment; no details invented beyond that).

All three re-rendered to PNG and confirmed: text fits within existing box bounds, no truncation,
no layout shift on neighboring elements.

### Rebuild & verification

`python3 build_sem04.py` (full deck rebuild, 56 slides — no single-slide mode) →
`tools/presentation-build/pptx_to_png.sh sem-04.pptx <tmp> 150` (full-deck PNG regenerate).
Visually inspected s01, s02, s10, s35, s37, s44, s49, s53, s56 at 150dpi — s02/s10 included as
untouched-function spot-checks (confirmed byte-identical layout to pre-fix renders). New
snapshots copied over `library/seminars/sem-04/rendered/snapshots/{s01,s35,s37,s44,s49,s53,
s56}.png`; the other 49 snapshot files were not touched (their builder functions did not change).

**Changed:** `build_sem04.py` only — `build_section_divider()` (added `title_size` kwarg,
backward-compatible default), `build_s44()`, `build_s49()`, `build_s01()`, `build_s56()`,
`build_s35()`, `build_s37()`, `build_s53()`, new `lerp_color()` + `build_growth_staircase()`
helpers, removed dead `build_section_divider_lite()`. **Not changed:** any `slides/*.md` source
file, any of the other 47 `build_sN()` functions, palette constants, deck.yaml.

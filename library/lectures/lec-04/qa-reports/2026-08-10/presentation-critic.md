VERDICT: REVISE

# Presentation Critic Report — Лекция 4 — 2026-08-10

Scope: focused review of 7 new slides `s13a`–`s13g` (issue #162, §2.4–§2.8
«Ландшафт инструментов / Skills / MCP-категории / Steering-файл / Presence
paradox / журнал задач: 3 паттерна / сравнительная таблица»), inserted into
Раздел 2 «Уровень C: кодинг-агент» between `s13` and `s14`. Deck is now 43
slides total. PNG snapshots did not exist at review start — regenerated via
`rendered/render_slides_png_workaround.py` per `notes/mcp-limitations.md`
`[#162-render-1]`.

**Methodology note on snapshot generation:** the workaround script exports
by 1-indexed pptx slide position, not by slide `id`. My first render pass
mis-mapped positions 14–22 by one slot (mislabeled the output files). I
caught this via a `python-pptx` text-extraction cross-check against the
`.md` `assertion:` frontmatter before drawing any conclusions, and
re-rendered with corrected indices (s13a–s13g are pptx positions 15–21;
`s13` = 14; section-3 divider `s14` = 22). All findings below are from the
corrected, verified mapping.

## Сводка
- Слайдов в review-скоупе: 7 новых (s13a–s13g) + 5 neighbor slides (s11,
  s12, s13, s14, s15) для pattern-comparison.
- P0 issues (блокеры): 0
- P1 issues (важные): 4
- P2 issues (мелочи): 2

## По слайдам

### Slide s13e — «Presence paradox: наличие файла само по себе — не гарантия пользы.»
**Severity:** P1
**Issue:** Russification violation. The slide's own title/assertion opens
with the bare English term **"Presence paradox"**, capitalized as a proper
title, with **zero Russian gloss anywhere on the slide** (checked full
rendered text — title + all 2 body text-frames). This contradicts the
deck's own established convention: `chapter.md` always writes this term
lowercase, inline, immediately glossed in Russian (e.g. "это и есть
«presence paradox»: контролируемое сравнение по трём условиям..."). The
prior orchestrator fix-pass (`iteration-log.md`, "Orchestrator fix pass —
3 Russification/quality defects") reviewed and fixed 3 other anglicism
defects on this slide block (s13b card headers, s13f pattern names, s13g
table labels) and explicitly signed off "Honest Lying → Russian
description precedes the term" as acceptable — but never checked the
slide's own title term "Presence paradox," which is the more prominent
occurrence and has no gloss at all (unlike "Honest Lying" a few lines
below it, which the log's claim is at least defensible for). This is a
genuine miss, not a disputed judgment call.
**Recommendation:** Add inline Russian gloss to the title, e.g. «"Presence
paradox" (парадокс присутствия): наличие файла само по себе — не гарантия
пользы.» or restructure to lead with the Russian formulation and introduce
the English term as an aside, matching how `chapter.md` §2.7 does it.
**Visual evidence:** `real-s13e-presence-paradox.png` — title reads
"Presence paradox: наличие файла само по себе — не гарантия пользы." with
no gloss visible anywhere on the 720p render.

### Slide s13d — «Steering-файл: что агент должен знать ПЕРЕД запуском.»
**Severity:** P1
**Issue:** Zero gold usage. Pixel-level color analysis of the rendered PNG
(`real-s13d-steering-file.png`) found **0 pixels** matching Ocean-palette
Gold (`#F0AB00`, tolerance ±30 RGB) anywhere on the slide — confirmed
against the build source (`build_lec04.py::build_s13d`), which uses only
`TEAL_TINT`/`TEAL`/`DEEP` fills, never `GOLD`. This breaks the deck-wide
"gold `#F0AB00` highlight ≥1×/slide" convention (CLAUDE.md palette lock)
and the local Раздел-2 baseline: s11 (gold `check`-step fill), s12 (gold
"разрыв ~15–17 п.п." bar), s13 (gold "Клоны кода" stat card) all use it.
The `iteration-log.md` final-verification entry explicitly claims "s13b/
s13d/s13f carry gold via the deck-wide footer/callout convention" — this
claim is **false for s13d** on the actual rendered output (self-report not
independently verified before being logged as passing).
**Recommendation:** Add a gold accent — e.g. promote the "Файл, который
никто не обновлял год..." closing warning-line (currently plain
bold-in-teal-box) to a `gold_callout`/gold-fill treatment, consistent with
how s13 uses gold for its most consequence-carrying single line.
**Visual evidence:** `real-s13d-steering-file.png`; independently
re-verified via RGB histogram of the full-resolution PNG.

### Slide s13f — «Где хранить состояние задачи между сессиями агента — три паттерна.»
**Severity:** P1
**Issue:** Same defect as s13d — zero gold pixels in the rendered PNG,
contradicting the same `iteration-log.md` claim ("s13b/s13d/s13f carry
gold..."). The 3 pattern cards use plain icon badges + teal/navy text only;
the top teal_callout and card interiors carry no gold accent.
**Recommendation:** Add gold to the single most load-bearing element on
the slide — likely the shared "не steering-файл... не self-authored
память" framing callout, or a gold accent on one "Что ломается" line per
card (careful: don't apply gold to all 3 equally — anti-pattern #21,
"inconsistent gold-emphasis across same-tier cards" — either pick a
principled single-highlight target or leave gold out with a documented,
explicit owner-approved exception instead of a false self-reported pass).
**Visual evidence:** `real-s13f-task-log-patterns.png`; RGB histogram
confirms no `#F0AB00`-range pixels.

### Slide s13g — «Нет единственно верного паттерна — решающая ось зависит от команды.»
**Severity:** P1
**Issue:** Two compounding issues on the same schema_matrix table:
1. **Table body font is 9.7pt** (`build_lec04.py::build_s13g`,
   `text_box(..., size=9.7, ...)` for every data cell) — below the README
   §4/§5.5 Schema Readability floor of **body ≥12pt**. The build script's
   own docstring/log entry self-flags this ("smaller than the 12pt
   guideline... acceptable at this table's information density") but
   self-declaring an acceptance exception to an ENFORCED floor is not the
   same as it passing Projector Readability (50% zoom) — at 9.7pt this
   table's 5-column, 3-row body text will be materially harder to read
   from the back of a lecture hall than the rest of the deck.
2. **Zero gold usage** (same class of issue as s13d/s13f) — table header
   row uses `MID` (teal) fill, not gold; no gold anywhere else on slide.
**Recommendation:** Either (a) reduce to 4 columns (drop the least
load-bearing one, e.g. merge "Обнаруживаемость" into "Git-diff" as a
sub-line) to free width for ≥11–12pt body text, or (b) split into 2
narrower comparison slides. Add a gold accent per the deck convention
(e.g. gold-fill on the closing "нет единственно верного ответа" framing
box, echoing s13's or s30's "when-not-needed" framing treatment).
**Visual evidence:** `real-s13g-comparison-table.png` — table is legible
at 1280×720 but the density concern is real at 50%-zoom projector
simulation; `col_w`/`size=9.7` confirmed in source.

### Slide s13a — «Три категории инструментов — по тому, ГДЕ живёт агент.»
**Severity:** P2
**Issue:** Title uses `size=25` vs. the established Раздел-2 baseline
`size=26` (s11/s12/s13 all identical 26pt). Minor but part of a broader
drift: s13a=25, s13b=23, s13c=23, s13d=24, s13e=22, s13f=21, s13g=21 — every
new slide's title is smaller than the established baseline, with no single
consistent new size. Understandable as a length-driven accommodation
(longer assertion headlines), but the degree of variance (21–25pt vs. flat
26pt) reads as slightly inconsistent typographic hierarchy across a
7-slide contiguous block a student will view back-to-back.
**Recommendation:** Not blocking — but consider normalizing to 1–2 fixed
sizes (e.g. 26pt default, 22pt for assertions >90 characters) rather than
one bespoke size per slide.
**Visual evidence:** cross-slide comparison of all 7 title font sizes in
`build_lec04.py`.

### Cross-deck / general
**Severity:** P2
**Issue:** Minor English-heavy phrasing spread across the block beyond the
P1 title issue — e.g. "Git-diff" as a bare column header (s13g),
"Least-privilege" opening a sentence (s13c), "context rot" used with only
a following-parenthetical gloss rather than a preceding one. These were
already explicitly reviewed and accepted by the prior orchestrator pass
as consistent with established deck-wide bare-technical-term precedent
(e.g. "diff" already used bare in s13a), and I don't disagree with that
specific reasoning — flagging only as a general observation that this
block runs closer to the anglicism ceiling than s11–s13 do, so any
*additional* revision pass on this block should re-run the deep-latin
scan rather than assume it's still clean.
**Recommendation:** No action required beyond the s13e title fix above;
re-run `deep_latin_scan.py` on the rendered pptx text after any further
edit to this block.
**Visual evidence:** `/tmp/pptx_visible_s13ag.txt` full-text extraction +
`deep_latin_scan.py` output (117 occurrences / 83 unique tokens across the
7-slide block on the actual rendered visible text — mostly legitimate
established terms per the log's own prior review, minus the one real miss
above).

## Neighbor consistency (s13 → s13a, s13g → s14)

- **s13 → s13a transition:** reads cleanly. s13's closing framing ("Merge
  = решение об ответственности за код — не делегируется") and s13a's
  opening ("Отдельная ось от лестницы A→D") are logically sequential — s13
  closes the "review/merge gate" sub-topic, s13a pivots to a new axis
  (tool categories) with an explicit signpost ("Отдельная ось... эта — «в
  каком окружении»"). No abrupt jump.
- **s13g → s14 transition:** clean. s13g's closing callout ("Нет
  единственно верного ответа... взвешивания осей под ситуацию команды")
  functions as a natural close to the whole §2.4–§2.8 sub-block before
  s14's section-3 divider ("Уровень C: человек ставил каждую задачу.
  Уровень D — AI берёт задачи из трекера сам..."). Good narrative
  bookend.
- **Roadmap-bar convention:** verified correct. None of the 7 new content
  slides (s13a–s13g) carry the 7-card "Раздел 0…6" roadmap-bar — it is
  present only on `s14` (section-3 divider, confirmed
  `real-s14-section3-divider.png`) and (by established pattern, not
  re-checked this session) the cover/other dividers. No leakage onto
  content slides.
- **No designer-added extras found:** grepped all 7 source `.md` files for
  scaffold phrases (Лектору/Преподавателю/Вы здесь/VERIFY-DAY-OF/
  FACT-CHECK/методическ*/педагогическ*/timing markers) — 0 hits in visible
  body or speaker notes.

## Cross-artifact / pattern consistency vs. s11/s12/s13 baseline

- **Slide types:** all 7 correctly typed (`assertion_visual` ×5,
  `case_study` ×1 for s13e, `comparison` ×1 for s13g) — consistent with
  the library's type system, no title+body generic fallback used.
- **Ocean rounded-box motif:** present and consistent on all 7 (verified
  visually — every slide has ≥1 `ocean_box`/`teal_callout` framing its
  main content).
- **Iconography:** consistent Lucide-style single-stroke icons, teal
  recolor, consistent sizing (s13c, s13d spot-checked at 2× zoom) — passes
  Iconography Discipline check.
- **Gold usage — where present — is correct (fill + dark text, not gold
  text on light background).** Explicitly checked s13c's gold bar
  ("Каждое подключение — решение о scope...") at 2× zoom: navy text on
  gold fill, good contrast, matches the deck-wide fixed defect pattern
  correctly. **However, 3 of 7 slides have no gold at all** (see P1s
  above) rather than reproducing the *contrast* defect — so this is a
  coverage gap, not a recurrence of the WCAG contrast bug.
- **Schema Readability Checklist (s13g, `schema_matrix`):** fill rate
  100% (no empty cells) ✓, header row single-line ✓, icons/color-coding
  per row consistent ✓ — but **body font 9.7pt fails the ≥12pt floor**
  (P1 above).
- **Speaker notes:** spot-checked s13a/s13e/s13g — 266–277 words each,
  within the 150–300 word range, readable connected prose, no layout
  descriptions, no "Лектору" sections.

## Counter-check (mandatory per CLAUDE.md)

4 P1 issues found → per the ENFORCED rule ("если ≥5 P1 issues но verdict
= APPROVE-WITH-POLISH — STOP, change to REVISE") the threshold is 5+ for
an automatic REVISE trigger by P1-count alone, so 4 P1s alone would sit at
the APPROVE-WITH-POLISH boundary. However, `tools/presentation-build/
README.md` §5.5 makes the Schema Readability Gate and the deck-wide gold
convention **ENFORCED, not advisory** — and one of the 4 P1s (s13g) is a
direct, self-acknowledged violation of an ENFORCED numeric floor (9.7pt <
12pt), and two others (s13d, s13f) directly contradict a **specific
written verification claim already in `iteration-log.md`** that turned
out to be false on independent re-check. Given (a) an ENFORCED-rule
violation and (b) a self-report that did not hold up under independent
pixel-level verification — consistent with the CLAUDE.md anti-pattern
"Subagent claim trustworthy" requiring independent orchestrator
verification — I am setting verdict to **REVISE** rather than
APPROVE-WITH-POLISH, since at least one of these (the false gold-coverage
claim pattern repeating across 2 slides) indicates the verification step
itself needs to be redone, not just 1-3 cosmetic touch-ups.

## Recommended fix scope (small, targeted)

1. s13e: add Russian gloss to "Presence paradox" title.
2. s13d + s13f: add a single, principled gold accent each (not decorative
   — pick the one highest-signal line per slide).
3. s13g: either shrink to 4 columns for ≥11–12pt body, or split into 2
   slides.
4. Re-run `deep_latin_scan.py` + gold-pixel spot-check on the whole 7-slide
   block after the above 3 fixes, log results honestly in
   `iteration-log.md` before re-declaring "verified."

This is a bounded, single-pass fix — not a re-design. No other structural,
narrative, or curriculum-relevance issues found in this 7-slide block; the
content itself (tool categories / skills / MCP scope / steering-file /
presence-paradox / task-log patterns / comparison table) is well-scoped,
each slide has exactly one new concept, terminology is introduced
progressively, and all 7 tie cleanly to §2.4–§2.8 of the chapter.

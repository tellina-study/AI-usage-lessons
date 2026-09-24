# Lecture 4 — EN deck iteration log (issue #172 / #162)

Visual-loop log for the English re-render (`lec-04-en.pptx`). One section per
EN-sync block; blocks are produced in parallel worktrees and merged afterwards.

---

## EN-Sync Block 5 — delivery/ops/docs tail + synthesis/closing

**Worktree:** `/tmp/lec04-en-block5` · **Branch:** `issue-162-lec04-en-block5`
**Scope:** the deck tail from the §6 divider to the closing slide — RU slide
files `s33-divider-delivery-ops-docs.md` … `s41-bridge-qa.md`, i.e. builders
`b4.s32 … b4.s40` in `slides_band4_en.py` (12 slides).
**Baseline:** RU `lec-04.pptx` @ 5176714 (58 slides, after round 6);
EN baseline was the 41-slide Sept-19 build, which predated rounds 3–6.
**Untouched:** everything before builder `b4.s32` (`b4.s31` Replit included),
`deck.en.yaml` / `deck-part2.en.yaml` `total_slides`.

### Scope resolution (recorded because the brief's numbering was ambiguous)

The brief enumerated 11 ids `s33 … s40`. RU frontmatter `id:` values are offset
by one from the RU file names in this range, so the two readings disagree on
the ends. The per-slide descriptions in the brief resolve it: "s33 — the §6
section divider" and "s40 — closing/bridge slide, round 6 removed the Seminar 4
reference" are, by content, `s33-divider-delivery-ops-docs.md` and
`s41-bridge-qa.md` respectively. I therefore covered the **union** — the whole
deck tail, 12 RU slide files — so no slide in the closing cluster is left
without an EN twin. Flagged for the merging session: the §6 divider
(`b4.s32`) is the one slide that could conceivably overlap with block 4.

### What each slide needed

| Builder | RU file | Verdict | Why |
|---|---|---|---|
| `b4.s32` | s33-divider-delivery-ops-docs | light edit | divider bridge/tag re-wrapped; content already matched RU |
| `b4.s33` | s34-cicd-ops | **full rebuild** | round-6 block-4 restructure: one entry thesis (maturity → AI) as a 2-step figure, seven capabilities named as a count, three former co-equal asides demoted to one muted paragraph |
| `b4.s33b` | s33b-ops-copilot-iac | **new slide** | did not exist in EN (added in RU round 3, reworked round 6) |
| `b4.s34` | s35-docs-bright-spot | light edit | typography only; EN text already matched RU |
| `b4.s35b` | s35b-docs-tooling | **new slide** | did not exist in EN (RU round 2) |
| `b4.s35` | s36-divider-synthesis | light edit | as `b4.s32` |
| `b4.s36` | s37-synthesis-matrix | **full rebuild** | EN baseline still had the 5-column version with a "Vendor (secondary)" column; round 3 removed it entirely. Rebuilt to 4 columns, widths rebalanced, title shortened |
| `b4.s37` | s38-triangulation | medium edit | GitClear card rebuilt to the two-measurement version (211M lines 2020–24 + 623M changes 2023–26) |
| `b4.s37b` | s37b-uber-kiro-dual-register | **new slide** | did not exist in EN (RU round 3, reworked round 6) |
| `b4.s38` | s39-risk-triad | **full rebuild** | round-6 reframe from binary "AI yes/no" to "AI is a given, compute the autonomy ceiling and its price"; probability axis made self-contained |
| `b4.s39` | s40-checklist | **full rebuild** | round-6 paired reframe: the eight questions now set a mode, not a barrier |
| `b4.s40` | s41-bridge-qa | medium edit | removed the visible "Seminar 4 — apply the checklist…" teal strip and its sentence in the notes; the four method-transfer steps expand into the freed band |

### Round-6 fixes specifically verified as carried into EN

- **s33b — the causal chain, not two adjacent facts.** Both columns answer the
  same pair of questions in identical white insets ("What AI multiplies" /
  "Where the gate is" vs "There is no gate"), and the gold callout names the
  mechanism: *the problem is not that there are more rollouts but WHAT exactly
  is being multiplied*. The "8.4%" keeps its explicit "a separate 2026
  benchmark, a different measurement" separator so it cannot read as a second
  measurement of the same ~55%.
- **s33 — one entry thesis.** Everything else is subordinated (muted italic,
  9.5pt) rather than restored to equal weight.
- **s36 — no vendor column.** Verified against the render, not just the source:
  4 headers only.
- **s37b — "Effect: not traceable" is its own gold block.** In EN the COO quote
  is natively English, so the risk is the opposite of the RU one: the
  conclusion could hide *inside* a quote that reads fine. The framing block
  states it as a claim of its own, and the gold callout carries
  "scale-without-a-criterion".
- **s38 — self-contained probability axis:** "grows with unfamiliarity of the
  task and codebase". No reference to the deleted anti-hype/SWE-bench Pro slide.
- **s38 / s39 — "AI is a given, calibrate the level" framing** in both titles,
  the teal band, the gold zone and both gold callouts.
- **s40 — no Seminar 4.** The old 41-slide EN baseline carried exactly this
  regression (a teal strip at y=5.58 plus a sentence in the notes plus a
  `learning_goal` mention); all three removed.

### Iterations

Five Generate → Convert → Inspect → Fix cycles over the range (each cycle
rebuilds the whole EN deck and re-snapshots the affected pages at 110 dpi via
`render_b5en.sh`; RU reference pages captured with `render_b5ru.sh`).

**Iter 1** — first full build of the 12 slides (44 builders total).
Inspected `en-33 … en-44`.
Found: (a) ASCII `->` used for arrows throughout, where the rest of the EN deck
uses `→`; (b) `low x low x high` and `2.6x` instead of `×`; (c) `s36` title
wrapped to two lines with an orphan word colliding with the table header row;
(d) `s33` muted paragraph sitting on the box border; (e) `$500-2000` hyphen
instead of an en dash.

**Iter 2** — replaced 23 ASCII arrows with `→` in the band tail and in the
`slides-en` mirrors; `×` for multiplication; shortened the `s36` title to
"The lecture's matrix: the practice leads — no vendor column"; trimmed the
`s33` muted paragraph by one clause.
Re-inspected: `s36` title now one line and clear of the header row ✓;
`s33` paragraph clear of the border ✓.
Still failing: `low x low x high` (the string is split across two source lines,
so the first replacement missed it); `s38` axis-1 description wrapping to two
lines and touching the box border.

**Iter 3** — fixed `low × low × high` directly; axis description column widened
(x `lx+2.70 → lx+2.60`, w `lw-3.00 → lw-2.85`) and axis-1 text shortened to the
self-contained wording.
Re-inspected: axis 1 now a single line ✓, `×` correct ✓.
Found in this pass: `s37` GitClear card read "refactoring ~25%→10%" — the `<`
had been lost, changing the claim (RU: `~25%→<10%`).

**Iter 4** — restored `~25%→<10%`; shortened axis 3 to one line.
Re-inspected `en-33 … en-44` end to end. Layout parity with the RU pages
(`ru-47 … ru-58`) confirmed on all 12.

**Iter 5** — speaker-notes pass. RU→EN word-count ratio was 1.19–1.38; trimmed
`s35b` (1.38) and `s37` (1.37) of padding clauses without dropping content,
bringing the range to 1.19–1.33. Final re-render and re-inspection of the
touched pages.

### Checks at accept

- **Mirror-check (ENFORCED):** 0 Cyrillic characters in the visible layer of
  slides 33–44 of `lec-04-en.pptx`; 0 in their speaker notes; 0 in the bodies of
  the 12 `slides-en/*.md` files. Run against the rendered PPTX, not the source.
- **No timing:** 0 hits for `\d+\s*(min|minute|мин)`, `⏱`, `⏰`, "duration",
  "timing" across visible layer + notes.
- **No methodology meta:** 1 hit, inspected and kept — "an important
  methodological technique in its own right" in the s37 notes, which is the
  faithful mirror of the RU sentence about the *triangulation method itself*,
  not a comment about teaching.
- **No course scaffolding:** 0 hits for "seminar N" / "семинар"; 0 for `LO[1-9]`;
  0 for `§N.N`; 0 for `→ sNN` / `(sNN)` / "see sNN" in visible layer + notes.
- **`[VFY-day-of]`:** present only inside the auto-generated "Sources:" block
  that `notes_sources_block()` appends to the notes — the deck-wide convention;
  the RU deck carries it on 9 of the same 12 slides. Not in any visible layer.
- **Glossary lock** (`tools/lecture-production/glossary-ru-en.md`): failure /
  failure mode / lesson, perception gap, accidental vs essential complexity,
  autonomy, agent, baseline, rollback, benchmark, hallucination, discipline,
  spec / spec-driven, vendor lock-in, prod(uction) gate, pipeline — all as
  locked. No new terms invented.
- **Acronym glossing** (`presentation-build/README.md` §5.8b): MTTR and
  time-to-engage glossed inline on first visible use on s33b; IaC expanded
  inline as "infrastructure-as-code"; SRE named as "operations practice (SRE)".
- **Ocean palette + rounded-box motif:** unchanged; every content slide in the
  range carries the motif and at least one gold element.
- **Assets:** reuses the language-agnostic `logos/uber-logo.png`,
  `logos/aws-logo.png` and `screenshots/s40-closing.jpg` as-is; charts from
  `assets/charts-en/` (`c33-dora.png`, `c39-anthropic-quiz.png` — already
  English-labelled, verified visually). No new asset acquisition needed, so the
  6-tier image ladder was not entered for this block.

### Notes for the merging session

1. `build_lec04_en.py` — the hard `assert len(builders) == 41` is replaced by a
   soft note against the 58-slide parity target, so a partially-merged tree
   still renders. Restore a hard assert once all five blocks are in.
2. `_helpers_en.py` — 7 URL keys and 3 `SLIDE_REFS` entries (`s33b`, `s35b`,
   `s37b`) appended; no existing entry modified.
3. **Parity issue inherited from RU, deliberately not "fixed" here:** the §7
   divider bridge and its notes still say the matrix has "the vendor as the
   last, secondary, replaceable column" and describe the checklist as "when AI
   yes, when no" — both superseded by the round-3 and round-6 edits to s36/s38/
   s39. The RU divider has the same stale wording, so the EN deck mirrors it
   rather than diverging. Worth an owner decision on the RU side first.

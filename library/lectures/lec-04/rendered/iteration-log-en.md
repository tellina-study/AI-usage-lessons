# Lecture 4 — EN deck iteration log

Issue #172 (bilingual production) · issue #162 (Lecture 4).
Companion to `iteration-log.md` (+ parts 2–5), which covers the **RU** deck.

RU is source of truth; EN is a full duplicate, not a machine gloss. Terminology
follows `tools/lecture-production/glossary-ru-en.md` (course-wide lock) and
`library/lectures/lec-04/glossary.yaml` (this lecture's lock).

---

## EN-Sync Block 1 — RU deck ids s01, s02, s03, s03b, s04, s05f, s05(keystone), s06, s07, s08, s09, s09b

Worktree `/tmp/lec04-en-block1`, branch `issue-162-lec04-en-block1`, base 5176714.
Scope = the first 12 slides of the RU deck in deck order (display positions 1–12).
Builders touched: `slides_band1_en.py` `s01, s02, s03, s03b*, s04, s05f, s06k, s06,
s07, s08, s09, s09b*` (`*` = created from scratch).

### 0. Baseline established before any edit (not assumed)

The EN deck was 41 slides dated Sept 19 and predated RU rounds 2–6. Rather than
guess which of my 12 slides had drifted, I diffed the RU builder against the
commit the EN twin was last touched at:

```
git diff 80c0e99f..HEAD -- library/lectures/lec-04/rendered/slides_band1.py
```

That diff is the authoritative change set, and for **my** 12 slides it is exactly
four items:

| RU slide | What changed since the EN baseline | RU round |
|---|---|---|
| s01 | METR / RCT acronyms glossed inline on the visible layer | 4 |
| s03b | **entire slide is new** (industry-adoption statistics) | 6 |
| s07 (method-decides) | DORA acronym glossed inline on the visible layer | 4 |
| s09b | **entire slide is new** (AWS Kiro vs 847 deployments) | 3 |

The other 8 (s02 cover, s03 bridge, s04 central question, s05f foundations,
keystone, s06 autonomy ladder, s08 divider, s09 spec-driven) are **RU-unchanged**
since the EN twin was written. They were verified against a fresh RU render
rather than retranslated — retranslating stable content would have been churn
with a drift risk and no gain.

### 1. Verification method

Rendered RU slides 1–12 (`render_b1ru.sh`) and EN slides 1–11 (`render_b1en.sh`)
to PNG and compared them side by side, then cross-checked mechanically:

- **Numeric fidelity** — extracted every number from the visible layer of RU
  slides 1–12 and EN slides 1–12 and diffed the multisets. Result: **identical on
  all 12**. The only reported deltas were `49000`/`49,000` and `5000`/`5,000`
  (RU thin space vs US thousands separator — correct per the glossary's
  US-English rule) and an artifact of the RU page-number stamp, which the EN
  build does not render.
- **Mirror-check** — Cyrillic scan of the visible layer *and* speaker notes of
  EN slides 1–12: **0 hits**.
- **Scaffold / timing / methodology grep** (English-pattern equivalents):
  0 scaffold hits, 0 timing hits. Six "methodolog*" hits, all inspected and all
  legitimate lecture content, not meta-commentary — "a **methodological
  practice** is the decision about which artifact to produce…" is the lecture's
  own defined term (`deck.yaml` glossary_lock: «методика vs инструмент»), and
  "the sampling **methodology** is not disclosed" is a source-confidence caveat.
  Both appear identically in the approved RU deck.
- **`[VFY-day-of]` placement** — EN slides 1–12: 0 in the visible layer, 11 in
  the notes. **Byte-identical counts to the RU deck.** This marker is a
  pre-existing deck-wide RU convention already flagged to the owner and
  deliberately deferred; Block 1 mirrors it rather than unilaterally diverging.

### 2. Per-slide record

| # | RU id | Verdict | Work done |
|---|---|---|---|
| 1 | s01 | needed fix | Added the EN acronym gloss: "METR (Model Evaluation and Threat Research, an independent research organization), RCT (randomized controlled trial)". Rest verified correct. |
| 2 | s02 | already correct | Cover + roadmap verified against RU; no change. |
| 3 | s03 | already correct | Bridge from Module 1, 4 carry-over cards; verified against RU; no change. |
| 4 | s03b | **built from scratch** | New builder, new EN chart, new `slides-en/s03b-industry-adoption.md`, new `SLIDE_REFS["s03b"]`, new URL key. |
| 5 | s04 | fixed layout | Content already correct. Frame headers 15pt → 14pt (see defect 3). |
| 6 | s05f | already correct | 12-source foundations list verified; no change. |
| 7 | keystone (s05) | already correct | 7-phase cycle + artifacts verified; no change. |
| 8 | s06 | fixed layout | Content already correct. C↔D boundary line rewrapped (see defect 2). |
| 9 | s07 | needed fix | Added the EN DORA gloss: "DORA (DevOps Research and Assessment — Google's research program on the maturity of DevOps practices)". |
| 10 | s08 | already correct | Section-1 divider; "SECTION 1" + English roadmap labels already matched the deck's EN divider convention. |
| 11 | s09 | already correct | Spec-driven practice, git tree + three voices; verified; no change. |
| 12 | s09b | **built from scratch** | New builder, new `slides-en/s09b-spec-driven-cases.md`, new `SLIDE_REFS["s09b"]`, 2 new URL keys. |

### 3. Asset work

**`assets/charts-en/c03b-adoption.png` had to be generated, not reused.** The RU
`assets/charts/c03b-adoption.png` has its title («Доля разработчиков,
использующих AI-инструменты, %») baked into the pixels, so shipping it in an
English deck would have been a mirror-check failure invisible to any text-level
scan. Created `gen_charts_r6b5_en.py` — the EN twin of `gen_charts_r6b5.py`:
same numbers (76 / 84 / 90), same Ocean palette, same geometry, same gold
highlight on the most recent point, title "Share of developers using AI tools, %".

Every other asset on these 12 slides (the METR hero JPG on s01, all Lucide icons)
carries no baked-in text and was reused as-is. Checked individually, not assumed.

### 4. Visual loop — defects found and fixed

Four render→inspect→fix passes. Defects found by inspection, not by the build
succeeding:

**Iter 1 → 2**

1. **s03b, meaning loss in translation.** I had compressed «Ощущение пользы и
   доверие к выводу разошлись» to "Usefulness and trust have come apart", which
   drops the actual contrast — it is the *feeling of usefulness* against *trust
   in the output*, and that pairing is the whole point of the right-hand column.
   Restored to "The feeling of usefulness and trust in the output have come
   apart." Verified it still fits the box at 3 lines.
2. **s06 (autonomy ladder), text overflowing the teal box.** The English C↔D
   boundary is ~20% longer than the Russian and wrapped onto a **third** line,
   breaking the two-line parallel structure of the B↔C / C↔D pair and crowding
   the box floor.

**Iter 2 → 3**

2. *(continued)* Dropping the body runs 12pt → 11.5pt was **not** enough — it
   still wrapped, now orphaning "D)" alone on line 3. Root cause was the string
   length, not the point size. Rewrote the line to
   "task comes from the tracker, result is a PR (→ D)", which preserves the RU
   meaning («откуда задача и куда результат (из трекера → PR → D)») in the
   available width. Kept 11.5pt as headroom. Verified: clean 2 lines / 2 lines.

**Iter 3 → 4**

3. **s04 (central question), header collision.** "Which practice is warranted in
   the phase?" is roughly twice the character count of «Какая практика оправдана
   в фазе?» and wrapped onto a second line, colliding with the body text beneath
   it and knocking the two comparison cards' baselines out of alignment. Fixed by
   taking **both** frame headers 15pt → 14pt — moving only the right one would
   have broken the left/right symmetry that is the entire didactic point of the
   slide. Verified: single line, aligned baselines, clear gap to the body.

**Iter 4 (final)** — full re-render of all 12; no further defects.

### 5. Accepted as-is (parity with the approved RU deck, deliberately not "improved")

- **s09b title orphan** — "…failure is expected, not / accidental" leaves one
  word on line 2. The approved RU title has the identical orphan («…отказ
  ожидаем, не / случаен»). Fixing it would mean rewording approved content;
  parity wins.
- **Keystone "the cycle closes: an ops lesson → a new requirement" label** sits
  over the gold return-arrow leg. Identical overlap exists in the approved RU
  render. Same reasoning.
- **Straight ASCII quotes** where RU uses « ». This is the established EN-deck
  convention across all 41 baseline slides. Typographic “ ” would be closer to
  the RU, but changing only 12 of 58 slides would make the deck visibly
  inconsistent — see "for the assembly pass" below.

### 6. For the assembly pass (deliberately NOT decided in this block)

1. **`build_lec04_en.py` will conflict on merge, by design.** Every block has to
   append its own builders to the same list. Block 1 inserted `b1.s03b` at
   position 4 and `b1.s09b` at position 12, and replaced the two hard-coded
   `== 41` asserts with a single `expected = 43` constant. Assembly should
   reconcile `expected` to the whole-deck total once all five blocks are merged
   — do not take 43 as authoritative.
2. **Page numbering is off in the EN build and on in the RU build.** RU renders
   "N / 58"; `build_lec04_en.py` disables `page_number()` with a comment citing
   issue #176 ("footer-less render for publication"). Left untouched — it is a
   whole-deck decision and the correct total is only knowable after assembly.
3. **Quote glyphs** — recommend assembly decides once for the whole deck. If
   typographic quotes are wanted, it is a single mechanical pass over all
   `slides_band*_en.py`; if not, the current straight quotes are already
   uniform.
4. **`deck.en.yaml` / `deck-part2.en.yaml` totals untouched** per brief. Note
   that neither file yet declares `s03b` or `s09b`; assembly owns adding them
   along with the whole-file `total_slides` reconciliation.
5. **Pre-existing EN speaker notes run long.** The baseline EN notes are
   323–433 words against the 150–300 contract (English renders the same RU
   content longer). Block 1's two new notes were written to 296 and ~300 words,
   i.e. at the low end of what the deck already does, but the deck-wide overrun
   is pre-existing and out of Block 1's scope.

### 7. Files touched by this block

```
library/lectures/lec-04/rendered/slides_band1_en.py      s01, s04, s06 edited; s03b, s09b added
library/lectures/lec-04/rendered/_helpers_en.py          3 URL keys + SLIDE_REFS s03b, s09b
library/lectures/lec-04/rendered/build_lec04_en.py       2 builders wired in; assert reworked
library/lectures/lec-04/rendered/gen_charts_r6b5_en.py   new (EN twin of the RU round-6 chart gen)
library/lectures/lec-04/rendered/assets/charts-en/c03b-adoption.png   new
library/lectures/lec-04/slides-en/s03b-industry-adoption.md           new
library/lectures/lec-04/slides-en/s09b-spec-driven-cases.md           new
library/lectures/lec-04/rendered/render_b1ru.sh          new (render RU pages for reference)
library/lectures/lec-04/rendered/render_b1en.sh          new (build + render EN pages)
library/lectures/lec-04/rendered/iteration-log-en.md     this file
```

`lec-04-en.pptx` / `lec-04-en.pdf` rebuilt from source at 43 slides.

---
## EN-Sync Block 2 — RU slide ids s10, s11b, s11, s12, s13, s14, s14b, s15, s16, s17, s17b, s18

**Branch:** `issue-162-lec04-en-block2` · **Worktree:** `/tmp/lec04-en-block2`
**Base:** RU deck at `5176714` (58 slides, after round 6).
**EN baseline:** `80c0e99` (41 slides) — predates rounds 2/3/6.

### Builder ↔ slide-id map for this block

| RU slide id | file | builder | EN display page (44-slide intermediate build) |
|---|---|---|---|
| s10 | s10-spec-driven-practice.md | `b1.s09` | 10 |
| s11 | s11-requirements-methodics.md | `b1.s10` | 11 |
| s11b | s11b-requirements-visualization.md | `b1.s11b` **NEW** | 12 |
| s12 | s12-prompt-and-pray.md | `b2.s11` | 13 |
| s13 | s13-divider-architecture.md | `b2.s12` | 14 |
| s14 | s14-architecture-necessity.md | `b2.s13` | 15 |
| s15 | s15-architecture-approaches.md | `b2.s14` | 16 |
| s14b | s14b-architecture-artifacts.md | `b2.s14b` **NEW** | 17 |
| s16 | s16-poisoned-context.md | `b2.s15` | 18 |
| s17 | s17-divider-implementation.md | `b2.s16` | 19 |
| s18 | s18-small-units-cycle.md | `b2.s17` | 20 |
| s17b | s17b-gemini-cli-selfreview.md | `b2.s17b` **NEW** | 21 |

Display order matches `build_lec04_v4.py` exactly:
s11 → s11b → s12 → s13 → s14 → s15 → **s14b** → s16 → s17 → s18 → **s17b** → s19.

### Drift audit (RU `80c0e99` → `5176714`, this block's slides only)

| Slide | Verdict | Action |
|---|---|---|
| s10 | already correct | render-verified only |
| s11 | **content drift** — round-6 acronym expansion (`02c70b4`) | 3 glosses added (EARS / NFR / ADR) |
| s11b | **missing** (RU round 2, `88b79b1`) | built fresh |
| s12 | already correct | render-verified only |
| s13 (divider) | already correct | render-verified only |
| s14 | already correct | render-verified only |
| s15 | already correct | render-verified only |
| s14b | **missing** (RU round 6 block 1, `cfe452a`) | built fresh |
| s16 | **content + design drift** (round 3, `a6bd3fa`) | framing fix + flame icon + meme band |
| s17 (divider) | already correct | render-verified only |
| s18 | already correct | render-verified only — confirmed it IS the explore→plan→code→commit discipline slide, not a context/memory slide |
| s17b | **missing** (RU round 3, `a6bd3fa`) | built fresh |

### Iteration 1 — generate → convert → inspect

- (a) inspected: all 12 pages at 150 dpi, A/B against the RU render of the
  corresponding pages (11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23).
- (b) changed:
  - `_helpers_en.py` — 3 URL keys (`mermaid_user_journey`, `cucumber_bdd`,
    `gemini_cli_incident`) + 3 `SLIDE_REFS` entries (`s11b`, `s14b`, `s17b`).
  - `slides_band1_en.py` — s11 acronym glosses; new `s11b()`.
  - `slides_band2_en.py` — new `s14b()`, new `s17b()`; s16 fixes
    (stale "AI at the periphery under human choice" → the round-6
    "signs off the decisions … AI can be a full co-architect … but does not
    sign"; gold `flame` icon; header box narrowed to `lw − 1.00`; EN meme band).
  - `build_lec04_en.py` — 3 builders wired, asserts 41 → 44.
  - `gen_memes_en_blk2.py` + `assets/web-en/band-x-everywhere.png` — EN re-bake
    of the round-5 composite (RU caption «плохой паттерн, плохой паттерн везде»
    is baked into the RU pixels; same imgflip source crop, same
    `compose_strip` geometry/typography, EN caption "bad pattern, bad pattern
    everywhere"). Embed widened 3.23 → 3.38 in (x 9.57 → 9.42, right edge
    unchanged at 12.80) so the longer EN panel keeps the full 0.64 in height.
  - `slides-en/` — 3 new md files; s11 + s16 md brought into line.
- (c) checklist now passing: Ocean palette + rounded-box motif identical to RU
  on all 12; gold ≥1×/slide; ref lists resolve; notes load for the 3 new slides.
- Open at end of iter 1: quote-mark convention on the new slides did not match
  the EN deck's existing single-quote convention; RU guillemets «» had been
  carried over verbatim onto s17b.

### Iteration 2 — inspect → fix

- (a) inspected: pages 12, 17, 18, 21 (the 3 new slides + s16) against RU 14,
  19, 20, 23.
- (b) changed: quote normalization to the EN deck convention —
  s14b caption `“good”` → `'good'`, `human’s` → `human's`;
  s17b `«…»` → `"…"` on the incident quote, `"too many privileges"` /
  `"check"` → single quotes. Mirrored into `slides-en/*.md`.
- (c) checklist now passing: typography consistent with `b2.s11`/`b2.s13`/
  `b2.s15`, which already use single quotes for inner quotations.

### Iteration 3 — full re-render + automated gates

- (a) inspected: all 12 pages re-rendered from the rebuilt pptx.
- (b) changed: nothing — no defect found on this pass.
- (c) gates:
  - **Mirror-check (Cyrillic scan):** 0 Cyrillic characters in visible body and
    0 in speaker notes across pages 10–21. Verified on the extracted pptx, not
    on the sources.
  - **No-timing / no-methodology / no-scaffold grep:** 1 raw hit, adjudicated
    as a false positive — "the spec-first *methodologists*" in the s12 notes is
    substantive content (the people who advocate spec-first), a literal
    translation of «методологи спека-first»; not meta-commentary about the
    lecture. Everything else: 0.
  - **Speaker notes:** 177–521 words; the RU equivalents are 127–438. The EN
    range is the expected ~20–25 % translation inflation plus the appended
    `Sources:` block, so it is at parity rather than over-long.
  - **Glossary lock** (`tools/lecture-production/glossary-ru-en.md`): failure →
    *failure*, урок → *lesson*, ADR / C4 / DSL / LLM / NFR kept as acronyms,
    существенная / привнесённая сложность → *essential / accidental complexity*,
    промышленное развёртывание → *production deployment*, разрыв восприятия →
    *perception gap*. No one-off variants introduced.

### Notes on the two RU quirks deliberately preserved (verified against the RU render)

1. **s16 title wraps to two lines** and **s11 title wraps to two lines** — the
   RU render does exactly the same at the same font sizes. Not "fixed", because
   the brief is "translate + rebuild the same design, don't redesign".
2. **s16's `[1]` marker drops below the poisoning-loop header** — identical in
   the RU render (the header box is narrowed to make room for the flame icon).

### Assets

- Reused as-is (language-agnostic): `assets/screenshots/s11-iceberg.jpg`,
  `assets/logos/gemini-logo.png`, all Lucide icons.
- Regenerated for EN (RU text baked into pixels):
  `assets/web-en/band-x-everywhere.png`. Attribution unchanged —
  `assets/web/attribution.md` covers the same imgflip source template.

### Flagged for final assembly (NOT fixed here — deck-wide, out of block scope)

- `deck.en.yaml` slide ids and `file:` paths still follow the **pre-round-2**
  41-slide numbering and are already off by one against `slides-en/` for
  everything from the requirements section onward (e.g. it declares
  `- id: s10 → slides-en/s10-requirements-methodics.md`, but the actual files
  are `s10-spec-driven-practice.md` and `s11-requirements-methodics.md`).
  Entries for `s11b` / `s14b` / `s17b` were therefore **not** inserted — adding
  them to an already-misnumbered document would create a second inconsistency.
  This needs one whole-deck renumber pass, not per-block patches.
  `deck*.en.yaml` is documentation only and is not read at render time, so this
  does not affect the rendered deck.
- `build_lec04_en.py`'s `assert len(builders) == 44` is Block 2's local total.
  Each block bumps it for its own inserts; final assembly reconciles.

### Build / render commands

```bash
cd library/lectures/lec-04/rendered
python3 gen_memes_en_blk2.py      # once, regenerates assets/web-en/
bash render_en_blk2.sh 10 11 12 13 14 15 16 17 18 19 20 21
# → lec-04-en.pptx, lec-04-en.pdf, snapshots-en-blk2/slide-NN.png
```

---
## EN-Sync Block 3

**Worktree:** `/tmp/lec04-en-block3`, branch `issue-162-lec04-en-block3`, base `5176714`.
**Scope:** 12 deck ids, display positions 25–36 of the 58-slide v4.5 order:

| display | deck id | builder | notes file (`slides-en/`) | status |
|---|---|---|---|---|
| 25 | s18b | `b2.s18b` | `s18b-curation-limits.md` | **new build** |
| 26 | s19  | `b2.s19`  | `s20-harness-gate.md` | edit (acronym gloss) |
| 27 | s20b | `b2.s20b` | `s20b-skills.md` | **new build** |
| 28 | s20c | `b2.s20c` | `s20c-mcp-coding-agent.md` | **new build** |
| 29 | s20e | `b2.s20e` | `s20e-task-logging-layer.md` | **new build** |
| 30 | s20d | `b2.s20d` | `s20d-git-conventions.md` | **new build** |
| 31 | s20g | `b2.s20g` | `s20g-register-env-secrets.md` | **new build** |
| 32 | s20f | `b2.s20f` | `s20f-git-worktree.md` | **new build** |
| 33 | s20  | `b2.s20`  | `s21-70-percent-problem.md` | edit (GitClear ×2, meme) |
| 34 | s22  | `b3.s22`  | `s23-divider-testing.md` | verified, unchanged |
| 35 | s23  | `b3.s23`  | `s24-tdd-discipline.md` | **rebuilt** (five-step recipe) |
| 36 | s24  | `b3.s24`  | `s25-all-green-mutation.md` | verified, unchanged |

Note the id-vs-filename offset inherited from the RU deck: deck id `sNN` and the
markdown file `sNN+1-*.md` do not always coincide (a v4.1 renumbering artefact).
The mapping above is authoritative.

### What round 6 changed, and therefore what had to be rebuilt

The pre-existing 41-slide EN deck (Sept 19) predates rounds 2, 3 and 6. Seven of
these twelve slides had **no EN counterpart at all** — s18b/s20b/s20c/s20d/s20e/
s20f/s20g were introduced in RU rounds 2/3/6. Two more diverged structurally, not
just textually:

* **s23 (TDD).** The old EN slide was "TDD-as-approach" — a two-block right column
  (no-outsource + a "structure != ritual" nuance plate). Round 6 replaced that with
  "what does NOT work" on top and a **five-step numbered recipe** below. Rebuilt
  from scratch against the RU builder, not edited.
* **s20 (70% problem).** GitClear went from one measurement to **two independent
  ones** (211M lines 2020-24 and 623M changes 2023-26), which forced variable card
  heights on the right column, and the round-5 Harold meme strip was added.

**`b3.s21` (anti-hype benchmarks)** was deleted from the RU deck in round 6. Its EN
function body is **kept but marked** — see "Assembler" below.

### Assembler — NOT touched, deliberately

`build_lec04_en.py` still lists **41** builders and is shared with four other EN
blocks running concurrently. Editing its `main()` from five worktrees would produce
a guaranteed five-way merge conflict, so this block left it alone and iterated
through a block-local `build_lec04_en_blk3.py` instead. It still builds and runs
(verified: 41 slides, no import error) — it simply does not yet render the new
slides.

**The v4.5 EN assembler must, for this block's range, call exactly:**

```python
builders += [b2.s18b]                                  # display 25
builders += [b2.s19]                                   # display 26 (harness gate)
builders += [b2.s20b, b2.s20c,
             b2.s20e,                                  # task-logging presents FIRST
             b2.s20d,                                  # git-conventions presents SECOND
             b2.s20g,
             b2.s20f]                                  # displays 27–32
builders += [b2.s20]                                   # display 33 (70% problem)
# b3.s21 (anti-hype benchmarks) — NOT called; removed in round 6
builders += [b3.s22, b3.s23, b3.s24]                   # displays 34–36
```

`deck.en.yaml` / `deck-part2.en.yaml` `total_slides` was left untouched per brief.

### Assets

* `assets/charts-en/c24-meta-mutation.png` — already EN-labeled, reused as-is.
* `assets/web/memes-src/*` — imgflip templates are language-neutral, reused as-is.
* **New:** `assets/web/band-hide-the-pain-harold-merged-en.png`, baked by
  `gen_memes_en_blk3.py` (same `compose_strip` technique as `gen_memes_r5.py`, so
  the EN strip is pixel-compatible with its RU twin). Caption: "looks fine — falls
  over at 3 a.m."
  **Naming convention for the other EN blocks:** RU `band-<name>.png` →
  EN `band-<name>-en.png`. The remaining six round-5 composites (x-everywhere,
  mocking-spongebob, evil-kermit, domino-effect, monkey-puppet, boardroom-panel3)
  belong to other blocks' slides and were not regenerated here.
* `_helpers_en.py`: +16 URL keys (copied verbatim from `_helpers.py` — a
  translation never changes a URL), +7 `SLIDE_REFS` registries, +`WEB` constant.
* The s20f two-panel diagram is built entirely from python-pptx shapes with
  separate text runs, so it was reusable as structure; only the strings were
  translated. Nothing was baked into an image.

### Visual loop

Three full Generate → Convert → Inspect → Fix passes over all 12 slides, rendered
via `render_en_blk3.sh blk3` at 140 dpi into `snapshots/en-b3/`.

**Iter 1 — what was inspected:** all 12 slides against their RU twins at
`snapshots/en-b3-ru/slide-25..36.png`; title wrap, box overflow, connector
collisions, gold-callout presence, ref-list fit.
**What was found (English runs 25–35% longer than the Russian for the same
content, so every fixed-width box is a fresh overflow risk):**

1. **s18b (P2)** — title wrapped to two lines at 23pt where the RU title is one
   line; the second line ate the whitespace above the cards.
2. **s20c (P0)** — title wrapped at 20pt and its second line **collided with the
   dashed agent→servers connector rail**.
3. **s20f (P1)** — the caption under panel B needed three lines in a two-line box;
   the last words were clipped and ran into the bottom band at y=4.32.

**Iter 2 — what changed:** measured the real DejaVu metrics rather than guessing
(PIL `textlength` at the render DPI, plus a wrap simulation against the actual box
width), then: s18b title 23 → 21pt (11.63in in a 12.3in box); s20c title shortened
to "…at the cost of narrower system access" (11.42in, keeps 20pt, parity with the
sibling slides); s20f panel-B caption shortened to "…a view on the same history,
not a copy" — wrap-simulated to exactly two lines.
**Checklist items now passing:** all three re-rendered and re-inspected — one-line
titles on s18b/s20c, no connector collision, no clipped caption.

**Iter 3 — what was inspected:** full deck re-render with the speaker notes now
loaded, plus a 3×4 contact sheet at 33% (`snapshots/en-b3/contact-sheet.png`) for
the 25%-zoom / 5-second test.
**Result:** every slide's main message reads from title + gold callout alone at
contact-sheet size. No further defects found; no changes made in this pass.

**5-second test (contact sheet, per slide):** PASS on all 12 — main message read
matches the `assertion` field in each markdown mirror.

**Honest note on projector readability.** The smallest body text in this cluster is
9.5pt (s18b card bodies, s20c/s20d card bodies), below the generic ≥12pt guidance
in the designer playbook. This is **exact parity with the approved RU deck**, which
uses the identical sizes at the identical coordinates; diverging would have broken
the RU↔EN visual mirror that this task exists to produce. Flagged rather than
silently changed — if the owner wants the floor raised, it has to be raised in both
languages at once.

### Mirror-check (ENFORCED)

Run against the **rendered PPTX** (visible text layer + speaker notes), not the
markdown:

```
disp 25..36: cyr_body=0 cyr_notes=0 for every slide
TOTAL cyrillic in visible body: 0   in notes: 0
```

Forbidden-marker sweep (timing `\b\d+\s*min(ute)?s?\b`, ⏱/⏰, `methodolog`,
`pedagog`, "to the lecturer", "you are here", `[VERIFY-DAY-OF]`, `[FACT-CHECK]`,
`LO[1-9]`, `§\d`, `→ sNN`, `(sNN)`) over body + notes: **one hit, disp 34** —
"TDD is the methodology on which the AI multiplier acts most strongly" in the
section-divider notes. That is substantive content mirroring the RU source
(«TDD — методология, на которую AI-множитель действует сильнее всего»), not
methodological meta-commentary about teaching, and it is pre-existing text this
block did not author. No other hits.

### Glossary-lock compliance

Per `tools/lecture-production/glossary-ru-en.md`: *failure* (not "issue"),
*lesson learned*, *harness*, *pull request*, *prompt injection*, *human-in-the-loop*,
*edge case*, *baseline*, US spelling (behavior, formalized, optimizes). Established
acronyms kept untranslated (MCP, CI, PR, API, LLM, TDD, SAST, JIT).

**Judgment call on the s19 acronym gloss.** Round 6 added a RU gloss line expanding
SAST and least-privilege at first visible use. Both are native English security
terms, so an English-speaking audience arguably needs less hand-holding — but the
course convention is to expand *where the source expands* (glossary conventions,
§"expand on first use only where the source does"), and `glossary.yaml` locks both
terms as requiring a gloss. The line was therefore kept, in English: "SAST — static
application security testing: analysis of code for vulnerabilities without running
it. least-privilege — the minimum rights needed, nothing more."

### Speaker notes

150–300 words is the generic per-slide target; the RU originals for these twelve sit
at 119–300 words and the English translations land at **1.23–1.35×** that — the
normal RU→EN word-expansion ratio (articles, no case inflection), matching the
already-merged EN baseline for this deck (e.g. the pre-existing `s20-harness-gate.md`
was 380 words before this block touched it). Content parity with the Russian was
preferred over truncating to hit the word band; `s21-70-percent-problem.md` was
trimmed back after the GitClear expansion so it stays in line with its siblings.

---
## EN-Sync Block 4 — slides s25b · s25c · s25 · s26 · s27 · s28 · s29 · s30b · s30 (band 3) + s31 · s32 (band 4)

**Branch:** `issue-162-lec04-en-block4` · **Worktree:** `/tmp/lec04-en-block4`
**Baseline:** RU deck at 5176714 (58 slides, after round 6) vs. the stale EN deck
(41 slides, 2026-09-19, pre-dating rounds 2/3/6 entirely).

### Scope resolution

The 11 ids in the brief are **builder-function names**, not slide-file names.
Resolved mapping (RU display positions 37–47 of 58):

| builder | RU slide file | EN display (44-slide build) |
|---|---|---|
| `b3.s25b` | `s25b-bdd-trunk-based.md` | 26 |
| `b3.s25c` | `s25c-test-tooling-matrix.md` | 27 |
| `b3.s25` | `s26-divider-review-security.md` | 28 |
| `b3.s26` | `s27-review-practice.md` | 29 |
| `b3.s27` | `s28-review-failure-curl.md` | 30 |
| `b3.s28` | `s29-security-practice.md` | 31 |
| `b3.s29` | `s30-vulnerable-false-confidence.md` | 32 |
| `b3.s30b` | `s30b-amazon-q-wiper.md` | 33 |
| `b3.s30` | `s31-slopsquatting-camoleak.md` | 34 |
| `b4.s31` | `s32-replit-culmination.md` | 35 |
| `b4.s32` | `s33-divider-delivery-ops-docs.md` | 36 |

`b3.s23` (TDD) and `b3.s24` (all-green / mutation) belong to EN-sync block 3 and
were **not** touched here, nor was the still-present `b3.s21` (anti-hype
benchmarks, deleted from the RU deck in round 6 — block 3's call to make).

### Full rebuild vs. light edit

| slide | verdict | why |
|---|---|---|
| `b3.s25b` | **full build (new)** | absent from the EN deck; RU round-2 insert + round-6 "+ / −" column rebuild |
| `b3.s25c` | **full build (new)** | absent from the EN deck; RU round-6 rebuild to a 5-channel 3+2 card grid (Playwright + pytest-generator added) |
| `b3.s25` | none | EN divider already matched the RU bridge/tag verbatim |
| `b3.s26` | none | EN review-practice already matched the current RU text |
| `b3.s27` | **full rebuild** | RU round-6 went 2 cases → 3 (Xu et al. redistribution) and 2-col → 3-col; EN was still the 2-col version |
| `b3.s28` | **full rebuild** | RU round-6 dropped the vendor row and decoded all four controls inline; EN still had chips + vendor strip |
| `b3.s29` | none | EN already matched (thesis + Stanford + NYU with baseline) |
| `b3.s30b` | **full build (new)** | absent from the EN deck; RU round-3 insert (Amazon Q wiper) |
| `b3.s30` | light edit | added the GitHub Copilot logo + attribution caption (RU has it), narrowed the CamoLeak header to clear it, added the EN Domino-Effect meme strip |
| `b4.s31` | **full rebuild** | RU round-6 replaced 3 parallel pillars with a 3-step causal chain and decoded "95" in place; "9 seconds" moved into the echo box as a separate incident |
| `b4.s32` | none | EN divider already matched the RU bridge |

### Supporting changes

- `_helpers_en.py`: added `WEB` (meme dir); 12 URL keys used by these slides
  (`cucumber_bdd`, `software303_bdd_adoption`, `trunk_based_dev`,
  `testcontainers`, `msw_docs`, `wiremock_split`, `pytest_generator_distil`,
  `tianpan_rubber_stamp`, `matplotlib_hitpiece_register`, `oss_review_burden`,
  `amazon_q_wiper`, `aws_security_bulletin_q`); `SLIDE_REFS` entries for
  `s25b` / `s25c` / `s30b`, and `s28` extended 3 → 6 refs (Rubber-Stamp
  Collapse, the matplotlib hit-piece, Xu et al.) to match the RU registry.
- `gen_memes_en.py` (new): bakes **English** captions onto the same blank
  imgflip templates the RU deck uses, writing `band-<name>-en.png`. The RU
  composites have Russian text in the pixels and cannot be reused. Three
  strips: `evil-kermit` ("I should read the diff" / "eh, good enough"),
  `domino-effect` ("one fake package name -> full exploit"),
  `boardroom-panel3` ("do not touch!" / "the agent commits anyway").
  Geometry and crop boxes copied verbatim from `gen_memes_r5.py`, so the EN
  strips drop into the same slide coordinates (aspect ratios within 1.5%).
- Language-agnostic assets reused as-is: `logos/curl-logo.png`,
  `logos/aws-logo.png`, `logos/copilot-logo.png`, all Lucide icon PNGs.
- `build_lec04_en.py`: registered the 3 new builders (41 → 44) and replaced the
  hard-coded `assert n == 41` with `assert n == len(builders)` so the other
  four parallel EN-sync blocks can add their own slides without fighting over
  a single literal.
- `deck-part2.en.yaml`: added documentation entries for `s25b` / `s25c` /
  `s30b`. `total_slides` deliberately **not** touched (owned by the
  orchestrator once all five blocks land).
- `render_en_b4.sh` (new): EN render helper rooted in this worktree.

### Visual loop

Pipeline per iteration: `build_lec04_en.py` → LibreOffice → PDF → pymupdf PNG
@110 dpi → visual read. RU reference PNGs rendered first to
`snapshots/ru-ref/slide-37..47.png`; EN output in `snapshots/en-b4/`.

**Iter 1 — all 11 slides inspected against the RU reference.**
- s25b: P0 — the title wrapped to two lines and collided with the column boxes;
  P0 — the BDD header wrapped and overlapped the definition paragraph
  (the RU original has the same overflow on its last definition line);
  P1 — the trunk-based micro-example clipped its second line.
- s28: P1 — trifecta item 3's heading wrapped onto its own sub-line.
- s25c / s26 / s27 / s29 / s30b / s30 / s31 / s32 / s25: clean, layout matches
  the RU reference (column widths, plate heights, gold/teal roles, meme + logo
  placement, ref list length).

**Iter 2 — fixes + re-inspect (pages 26, 31).**
- s25b title → "BDD and trunk-based on the AI loop: what they give, what they
  cost" (one line at 20 pt); BDD header → "BDD — a test in business language";
  trunk-based example → "claude/fix-auth: opened in the morning, merged by
  lunch behind a flag". All three now single-line; **s25b PASS**.
- s28 trifecta item 3 → head "outbound transfer (egress)", sub "a channel
  outward — the agent can send data beyond the perimeter". Head fixed, but the
  sub now wrapped and clipped "perimeter" — **still FAIL**.

**Iter 3 — fix + re-inspect (pages 27, 29–36).**
- s28 sub → "a channel outward: data can leave the perimeter" (46 chars, one
  line). **s28 PASS.** No regressions anywhere else; all 11 pages re-rendered
  and re-read.

**Iter 4 — final full rebuild + re-render of all 11 pages** after the US-English
spelling pass and the `.md` mirror alignment. No visual deltas.

### Checks run before finishing

- **Mirror-check (ENFORCED):** Cyrillic scan over the rendered PPTX visible
  layer **and** speaker notes for pages 26–36 — **0 hits** in visible, **0 hits**
  in notes. (Russian remains only in non-rendered Python section comments, the
  pre-existing convention of `slides_band*_en.py`.)
- **Timing markers:** `\d+\s*min(ute)?s?`, `⏱`, `⏰`, "Timing", "Duration of the
  section" over visible + notes — **0 hits**.
- **Methodology meta-commentary:** `methodolog|pedagog|didactic|To the
  lecturer|You are here|at this stage the student|Why this is in Lecture` —
  **1 hit, false positive**: "TDD is the methodology that fits the AI loop
  best" on s25b, where *methodology* is the subject matter (BDD/TDD), not a
  meta-comment about teaching.
- **Scaffold leaks:** `[VERIFY-DAY-OF]`, `[FACT-CHECK]`, `LO[1-9]`, `§N`,
  `→ sNN`, `(see sNN)` over visible + notes — **0 hits**. (`[VFY-day-of]`
  appears only inside the notes' `Sources:` block, which is the deck-wide
  convention for volatile refs, on both RU and EN.)
- **US-English spelling:** `programme|behaviour|neighbour|defence|analyse|
  organis|recognis|colour|labelled` — 5 hits found and fixed (program,
  neighbors, defense, analyzed, labeled). Scan now clean.
- **Glossary lock** (`tools/lecture-production/glossary-ru-en.md`): failure →
  *failure*; урок → *lesson*; склонность доверять автомату → *automation bias*;
  инъекция в промпт → *prompt injection*; least-privilege, sandbox,
  supply chain, human-in-the-loop, accountability, agent, autonomy kept as the
  locked EN terms; numbers/dates/units preserved verbatim from the RU
  (43.5% / −19% / +6.5% / +2.4% / 576,000 / 20% / 43% / CVSS 9.6 / ~40% /
  1689 / 89 / 1200+ / 1190+ / v1.84.0 / v1.85.0 / ~1 million / 27% / 68%).
  One term needed a decision: RU «закрытый контур» on s25c. The course glossary
  maps «замкнутый контур» → *closed-loop*, but that entry is the L10
  environment-structure sense; here the RU means an isolated network perimeter,
  so it is rendered **"air-gapped setup"**, with "an air-gapped setup" spelled
  out in the card body and the notes.

### Known, deliberate non-issues

- **Speaker-notes length.** The 11 EN notes run 189–378 words (RU originals:
  127–309). RU→EN inflation is 25–35% and the untouched pre-existing EN slides
  in this range sit in exactly the same band (s26 = 358, s29 = 361, s30 = 394),
  so the EN deck is internally consistent. Content is connected prose with no
  layout descriptions, no lecturer cues, no timing. The longest one I authored
  (s28, 389) was trimmed to 378.
- **Shared-file merge risk.** `_helpers_en.py`, `build_lec04_en.py` and
  `deck-part2.en.yaml` are edited by all five parallel EN-sync blocks. All my
  additions are in clearly-labelled `EN-sync block 4` chunks appended at the end
  of `URLS` / next to the matching `SLIDE_REFS` slot, to keep conflict hunks
  small and obvious.

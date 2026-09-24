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

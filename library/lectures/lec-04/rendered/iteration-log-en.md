# Lecture 4 — EN deck iteration log (issue #172 / #162)

Companion to `iteration-log.md` (RU). One section per EN-sync block; blocks run in
parallel worktrees and own non-overlapping slide ranges.

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

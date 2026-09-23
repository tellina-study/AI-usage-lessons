---
name: sem-04-en-track-brief
issue: 204
status: active
---

# Seminar 4 — EN track brief

Shared contract for every agent producing an English artifact of Seminar 4. Precedent:
the seminars-en-track session (issue #204, PR #205/#206 — seminars 1-3 + lecture 3).

Seminar 4 is the **classic format** (like sem-01/sem-02, unlike sem-03 with its `cases/`
files): `deck.yaml` + `slides/*.md` where the whole lecturer commentary lives inside each
slide's `## Speaker notes`. There is **no `speech.md`** for seminars — do not invent one.

## Deliverables

| RU | EN | Notes |
|---|---|---|
| `deck.yaml` | `deck.en.yaml` | `language: en`; every `file:` → `slides-en/...` |
| `slides/sNN-*.md` (57) | `slides-en/sNN-*.md` (57) | **identical filenames** — see decision D2 |
| `rendered/build_sem04.py` | `rendered/build_sem04_en.py` | thin driver, see decision D1 |
| — | `rendered/sem-04.strings.en.json` | RU→EN table for slide body text |
| — | `rendered/sem-04-en.pptx` / `.pdf` | EN render |

The RU artifacts — including `rendered/sem-04.pptx`, `rendered/sem-04.pdf` and the RU
snapshots — **must not change**. The RU render stays byte-identical.

## Translation quality bar

- **Write, don't transliterate.** The target reader is an international practicing engineer.
  Produce what a native-speaking engineer would have written; do not calque Russian syntax.
  Match the source's register: direct, teacherly, occasionally blunt. Do not make it more
  formal, more hedged, or more enthusiastic than the Russian.
- **US spelling** ("behavior", "labeling", "optimize").
- **Terminology is locked** in `tools/lecture-production/glossary-ru-en.md` — Part A (course
  terms), Part B (proper nouns), **Part C (Seminar 4 terms)**. Part C is mandatory reading:
  the axis terms (*day-0 baseline* / *wait for a signal*) and case machinery (*decision
  point*, *option card*, *target answer*, *breakdown*, *the evidence*, *readiness gate*)
  recur dozens of times and a one-off variant reads as a different concept. If a term you
  need is missing, add it to Part C first, then use it.
- **Transfer exactly, never improve:** numbers, percentages, dates, arXiv IDs, author names,
  organization names, URLs, and verbatim quotations. No rounding, no unit conversion, no
  added precision. A quoted phrase stays a quoted phrase.
- **Keep inline sources and citations exactly where they are** (`Gloaguen et al.,
  arXiv:2602.11988`, `Lulla et al., arXiv:2601.20404`, `p<0,001` → `p<0.001` — decimal
  separator is the one exception, see D3).
- **Never translate:** file names and paths (`spec.md`, `CLAUDE.md`, `DECISIONS.md`,
  `AGENTS.md`, `README.md`, `src/main.js`, `doc/adr/`, `package.json`), the demo repository
  name `signup-landing` (and `signup-landing-demo`), code, JSON keys, CLI commands, git
  refs, and the literal content of any code/terminal block. Translate only the framing
  prose and explanations around them.
- **Markdown structure is preserved 1:1**: same headings (`## Assertion`, `## Visual`,
  `## Speaker notes`), same table shapes, same number of rows, same bold/italic/backtick
  emphasis, same blockquotes.
- **Frontmatter:** keys, `id`, `type`, `duration_min`, `learning_outcomes`, `references`,
  and `visual.pattern` values stay **verbatim** (they are machine-read). Translate only the
  human-readable values: `assertion`, `learning_goal`, `visual.primary`, and any free-text
  note.
- **No new content.** No added examples, no "helpful" clarifications, no removed hedges.
  The EN deck must make exactly the same claims as the RU one. If something in the RU looks
  wrong, report it — do not fix it in translation.
- **No Russian left behind** in an EN artifact (mirror-check), and the anti-anglicism /
  Russification mandate does **not** apply here — English is the target language.

## Decisions taken by the orchestrator (recorded per the task brief)

**D1 — EN render: parameterize, don't fork.** Two precedents existed and neither transferred
cleanly:

- sem-01/sem-02 used run-level string substitution over the approved PPTX
  (`tools/seminar-render/pptx_i18n.py`). Its own docstring states why: those build scripts
  were *"stale or hand-edited"*, so forking them was not an option. sem-04's builder is
  neither — it was run to produce the current v6 render.
- lec-03 forked its builder wholesale (`build_lec03_en.py`, 4610 lines) because its EN deck
  genuinely differs in visuals (English memes, EN charts, an EN reference/anchor system).
  Seminar 4 has no such divergence: same icons, same charts, same layout.

Chosen instead: `build_sem04_en.py` is a **thin driver** that imports the untouched
`build_sem04.py`, repoints `SLIDES_DIR` at `slides-en/` and `OUT` at `sem-04-en.pptx`, and
monkey-patches its text sinks to translate through `sem-04.strings.en.json`. This is
possible because of two properties of the RU builder, both verified by reading it:

1. **Every** visible string funnels through exactly two functions — `text_box()` and
   `multipara_box()` (via `cfg["text"]`) — plus `speaker_notes()` for the notes. There is
   no other run-text sink in 2552 lines.
2. Geometry is computed from text length in only three places: `auto_header()` (picks font
   size and header height from `len(title)`), `question_slide()` (picks question-box height
   from `len(question)`), and `terminal_card()` / `_fits()` (overflow diagnostics only).

Patching the sinks *and* those length-driven entry points means the EN build re-runs the
real layout logic on **English** text: `auto_header` re-picks its font size for a longer
EN title, and `_fits()`/`terminal_card()` print genuine `OVERFLOW WARNING` lines for EN.
A string swap over the finished PPTX would have silently kept RU-sized boxes — exactly the
"EN is longer, did anything get clipped" risk this task flags. It also keeps the RU render
byte-identical *by construction*, because the RU script is not edited at all, and avoids a
2552-line copy that would drift the first time the RU deck is revised.

Completeness guard (the property `pptx_i18n.apply` provided by refusing partial tables):
the patched sinks record any string containing Cyrillic that has no entry in the table, and
the build **fails** with that list rather than shipping a half-Russian deck.

**D2 — `slides-en/` filenames are identical to `slides/`.** sem-01, sem-02 and sem-03 all
pair RU and EN slides under the same filename; sem-04's RU slugs happen to be transliterated
Russian (`s03-spec-md-trebovaniya.md`), which is ugly in an EN folder but keeps the RU↔EN
parity check purely mechanical (`ls slides | diff - <(ls slides-en)`) and keeps
`load_notes()`'s `sNN-*.md` glob working unchanged for both languages.

**D3 — decimal separator and thousands separator are localized.** The RU source writes
`p<0,001`, `−28,6%`, `20-23%`. English uses a period for decimals: `p<0.001`, `−28.6%`.
This is the single formatting change allowed to numbers — the *value* never changes.

**D4 — `deck.yaml`'s leading comment block (the ~44-line v6 changelog) is translated too.**
sem-02's `deck.yaml` had no leading comments, so there is no precedent; leaving 44 lines of
Russian at the top of an EN artifact would fail the mirror-check for no benefit.

## Chunk map (slide translation)

| Chunk | Slides | Content |
|---|---|---|
| A | s01-s08 | Section 0 — opening, client request, `spec.md`, two modes, day-0 list, harness map |
| B | s09-s14 | Section 1 divider + case 1.1 (role and repository) |
| C | s15-s21 | Case 1.2 (processes, readiness gate) |
| D | s22-s27 | Case 1.3 (nested files, rule of three addresses) |
| E | s28-s37 | Section 2 divider + case 2.1 (memory, `DECISIONS.md`) |
| F | s38-s46 | Case 2.2 (wiki structure, ADRs, cost of structure) |
| G | s47-s57 | Case 2.3 (working memory) + closing (six decision points, honest coverage, transfer) |

**D5 — no guillemets in any EN artifact.** Verified against all four existing EN artifacts
(`sem-01/slides-en`, `sem-02/slides-en`, `sem-03/slides-en`, `lec-03/slides-en`): each
contains **zero** `«»` characters, against 330-382 in its RU counterpart. RU `«…»` becomes
straight `"…"`; where RU nests `«…»` inside `«…»`, the inner quotation becomes `'…'`.
Final gate: `grep -c '[«»]'` must be 0 across `slides-en/` and `deck.en.yaml`.

**D6 — dates stay in the source's `DD.MM.YYYY` form.** `11.02.2026` is genuinely ambiguous
to an international reader (unlike `30.04.2026`, which self-disambiguates). Converting to
ISO would not change the value, but the task brief says dates transfer exactly, so they do.
Flagged to the operator rather than silently reformatted.

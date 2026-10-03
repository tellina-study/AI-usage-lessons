---
name: sem-05-en-track-brief
issue: 211
status: active
---

# Seminar 5 — EN track brief

Shared contract for every session producing an English artifact of Seminar 5.
Precedent: `sem-04/EN-TRACK-BRIEF.md` (issue #204). **Read that one first** — the
translation-quality bar below is the same bar, and this file only records what is
*different* for Seminar 5.

Seminar 5 is the classic seminar format: `deck.yaml` + `slides/nNN-*.md`, with the whole
lecturer commentary inside each slide's `## Speaker notes`. There is **no `speech.md`** for
seminars — do not invent one.

RU deck: **68 slides, 89.75 min in a 90-minute slot**.

## Deliverables

| RU | EN | Notes |
|---|---|---|
| `slides/nNN-*.md` (68) | `slides-en/nNN-*.md` (68) | **identical filenames** (D2) — this is the only thing a translator writes |
| `deck.yaml` | `deck.en.yaml` | **generated**, never hand-written — `python3 rendered/make_deck_yaml_en.py` |
| `rendered/build_sem05.py` | `rendered/build_sem05_en.py` | thin driver, see D1 |
| — | `rendered/sem-05.strings.en.json` | chrome strings only (see D8) — ~10 entries, not the slide bodies |
| — | `rendered/sem-05-en.pptx` / `.pdf` | EN render |

**The RU artifacts must not change.** `slides/`, `deck.yaml`, `build_sem05.py`,
`deck_kit.py`, `metrics.py`, `slide_parts.py`, `rendered/sem-05.pptx` — none of them are
edited by the EN track, and the driver cannot write `sem-05.pptx` (there is an explicit
guard). See D9 for why "do not run the RU builder" is part of this rule.

---

## What a translator actually does

Exactly two things, in this order:

1. **Write `slides-en/nNN-<same-slug>.md`** — the RU filename, English content.
2. **Run the three commands below** and fix whatever they report.

```bash
cd library/seminars/sem-05/rendered
python3 make_deck_yaml_en.py        # regenerate deck.en.yaml from slides-en/
python3 build_sem05_en.py --roles   # RU↔EN role parity — MUST pass
python3 build_sem05_en.py --partial # build what exists; drop --partial when all 68 are done
```

Then look at the render **for real** — never at `qa_preview.py`, which is wrong by
construction:

```bash
cd ../../../..                       # repo root
tools/presentation-build/pptx_to_png.sh \
    library/seminars/sem-05/rendered/sem-05-en.pptx \
    library/seminars/sem-05/rendered/qa-en 150 <first> <last>
```

You do **not** edit `deck.en.yaml`, `build_sem05_en.py`, the strings table, or anything
under `rendered/`. The RU rule holds for EN: *edit the slide, not the manifest.*

### The per-slide file, field by field

Frontmatter — three groups, and mixing them up is the common mistake:

| Field | What to do |
|---|---|
| `id`, `type`, `duration_min` | **verbatim** — machine-read, and `duration_min` carries the deck's timing |
| `visual.pattern`, `visual.figure` | **verbatim** — `pattern` selects the layout device, `figure` names a PNG |
| `assertion`, `learning_goal`, `visual.primary`, `visual.tag` | **translate** |
| `visual.backup` | **keep in Russian, verbatim** — decision D7 |

Body — `# Title`, `## Assertion`, `## Visual`, `## Speaker notes`. Markdown structure is
preserved 1:1: same headings, same table shapes, same row and column counts, same code
fences and their language tags, same blockquote structure, same `**bold**` / `` `mono` ``
emphasis, same `←` arrows and `·` separators.

---

## Decisions

Decisions **D2** (identical filenames), **D3** (decimal separator: `p<0,001` → `p<0.001`),
**D5** (no `«»` in EN — use `"…"`, and `'…'` for a nested quotation) and **D6** (dates stay
`DD.MM.YYYY`) carry over from Seminar 4 unchanged. New or changed below.

### D1 — EN render: parameterize, don't fork (unchanged in spirit, different in substance)

`build_sem05_en.py` imports the untouched `build_sem05.py`, points it at `slides-en/` +
`deck.en.yaml`, and patches the few places that would otherwise read Russian. Verified
mechanically (AST over the whole import graph, not grep — `build_sem05_en.py --audit`):

- Run-text sinks: **2**, both in `deck_kit.py`. `build_sem05.py`, `metrics.py` and
  `slide_parts.py` have **zero**.
- `build_sem05_en.py --selftest` renders the RU deck through the patched harness with an
  identity chrome table and compares it **slide-for-slide** against the committed
  `sem-05.pptx` — shape types, geometry, run texts and notes. It passes on all 68 slides,
  which is what proves the harness changes nothing except the strings.

**Seminar 5 needs a smaller patch than Seminar 4 did, for a real architectural reason.**
sem-04 hardcoded its slide bodies inside 57 `build_sNN` functions, so its EN track needed a
large RU→EN table for the body text. sem-05 reads every visible string from the markdown,
so pointing the builder at `slides-en/` translates the body **at source** — and the real
layout code then measures English.

That last point also removes sem-04's worst failure mode. sem-04 picked geometry from
`len(title)` buckets, which is why its s19 and s21 were silently clipped when an EN title
crossed a bucket boundary. sem-05 does not bucket: `metrics.py` measures the actual wrapped
text with PIL font metrics, `deck_kit` lays out from a cursor, and `build_sem05.measure()`
gets a block's height by drawing it on a scratch slide and discarding the slide.
**The EN pilot produced zero overflow warnings and zero layout defects of that class.**

### D7 — `visual.backup` stays in Russian, verbatim

New for Seminar 5; sem-04's slides had no such field. `visual.backup` is a production
provenance record: it cites Russian source files (`rework-r4/PLAN.md`,
`qa/zamechaniya-golosom-keysy-1-4.txt`) and quotes the course owner's own spoken words with
timecodes. It is never drawn on a slide and never read by the builder.

Translating it would turn verbatim quotations into paraphrases of quotations — which the
translation bar forbids outright. So it is carried across unchanged, with a one-line
`[EN-track note: ...]` appended so a reader knows it is deliberate.

**Consequence for the mirror-check:** "no Russian left in an EN artifact" is scoped to the
slide body, the translated frontmatter fields, and the rendered deck. `visual.backup` is
exempt, and it is the only exemption. Measured on the pilot: **0** Cyrillic characters in
`ppt/slides/*.xml` and `ppt/notesSlides/*.xml` of `sem-05-en.pptx`; **0** in any slide body;
all `«»` confined to `visual.backup`.

### D8 — the strings table carries CHROME only, not slide bodies

`sem-05.strings.en.json` holds the handful of visible strings that are hardcoded in the
Python rather than read from the markdown:

- the section names drawn as roadmap pills on the macro dividers — `Открытие` → *Opening*,
  `Хук` → *Hook*, `Скилл` → *Skill*, `Доступ наружу` → *Outbound access*, `Сборка` →
  *Wrap-up*;
- the cover eyebrow `СЕМИНАР 5` → *SEMINAR 5*;
- the `base_and_edge` track labels `база` / `кромка` → *Base* / *Edge*;
- the one divider tag still hardcoded for the n-deck (`n44`).

Every other Cyrillic literal in `build_sem05.py` / `deck_kit.py` / `metrics.py` (196 live
non-docstring literals in total) goes to `metrics._WARNINGS`, `deck_kit.Claims`, or a
`label=` kwarg — developer diagnostics that are never drawn. They stay Russian on purpose.

### D9 — do not run `build_sem05.py` during EN work

`build_sem05.py` is **not byte-reproducible**: three consecutive rebuilds of the unmodified
RU deck produced three different files (`8c3026fd…`, `f1d26a88…`, `2b46be0a…`), because
python-pptx stamps the zip entries it writes.

Two consequences, both load-bearing:

1. There is no hash a reviewer can compare to show the RU render survived. "RU is
   byte-identical" is guaranteed **by construction** — the RU scripts are never edited and
   the driver refuses to write `sem-05.pptx` — not by comparison.
2. Running the RU builder "just to check" **destroys the committed artifact** and it has to
   be restored with `git checkout`. `--selftest` exists so the harness can be proven
   transparent without ever running it.

---

## The one thing that will bite you: roles are decided from the TEXT

`build_sem05.quote_role()` (`build_sem05.py:682-698`) decides a quote block's **visual
role** — and therefore its shape, fill and border — by matching the Russian text:

| Matcher | Russian it looks for | What it produces |
|---|---|---|
| `ASK` (l.660) | `выберите`, `что бы вы`, `как бы вы`, `назовите`, `подумайте` | gold question box |
| `CAVEAT_OPEN` (l.677) | opens with `оговорка`, `честный пробел`, `честно про` | dashed caveat plate |
| `CAVEAT` (l.678) | `не проверен`, `не измер`, `нет данных`, `не подтвер` | dashed caveat plate |
| `startswith("«")` (l.696-697) | a guillemet | quiet "speech" form |

A question to the room is often not punctuated with `?` (only two of 68 slides are), so
`ASK` is doing real work — and on English input all four silently mis-fire. D5 makes the
guillemet test fail on *every* EN quote by construction. Nothing warns: the deck just
renders with the wrong visual semantics.

The driver rebinds all four with bilingual patterns, **and** `--roles` checks the result:
it computes the role of every quote block twice, from `slides/` and from `slides-en/`, and
**fails the build** if any block's role differs.

**This is not theoretical — it caught a real defect in the pilot.** On n68 the English
sentence "The three bottom rows are **checked by nothing** today" lost the caveat signal
that `не проверены` carries, so the block dropped from `caveat` to `speech` and the closing
caveat would have rendered as an ordinary quotation. The fix was to the *English wording*
("are **not checked by anything** today"), not to the regex — which is the rule:

> When `--roles` reports a mismatch, fix the English sentence so it carries the same signal
> the Russian does. Only widen the pattern if the English genuinely cannot carry it.

---

## Known layout trap: table headers are drawn in BOLD CAPS

Found by the pilot render, not by reasoning, and worth knowing before you write a table.

`deck_kit._col_shares` (l.377-406) gives a column a floor of `longest word + 0.2in`,
measured **as written**. `table_card` then draws the header `ht.upper()` in **bold**
(`deck_kit.py:553`) into `width - 0.16in`. Caps add ~15% on top of bold's ~12%, so the
header `Reinforcement` measures 1.095in and draws 1.264in. On n03 it wrapped mid-word as
`REINFORCEMEN / T`, and nothing warned — the cell wraps rather than overflows, so `_fits`
has nothing to report.

The driver patches `_col_shares` for the EN build to measure the header as it is actually
drawn (`.upper()`, `bold=True`) and to redistribute width from columns with slack. **Keep
table headers short anyway** — the patch can only take width that another column can spare.

This is a latent defect in the RU builder that only a longer language reaches; it is listed
as an open item below rather than fixed in `deck_kit.py`, because raising the floor would
re-proportion approved RU tables.

---

## Figures: 13 slides, and an owner decision is needed

**This is the one part of the EN track that the driver does not solve.**

`rendered/figures/` holds **48 PNGs** generated by **7 `make_figures*.py` scripts**
carrying **682** live Russian string literals baked into the raster. **13 of the 68
n-slides** reference one via `visual.figure`.

No string patch can reach them, and they are not plain translation work either: the
generators place text at fixed pixel coordinates with `limit=` guards, so longer English
overflows its box — these figures need re-laying-out, not just re-wording.

The driver looks for `figures-en/<name>` first and falls back to the Russian
`figures/<name>`, but **never silently** — each fallback prints `РУССКАЯ СХЕМА [nNN]` and
is counted in the final line. The pilot reports three: n01 (the cover hero), n05 (the
session map), n68 (the closing figure).

**The pilot render shows the consequence plainly on n68:** an entirely English text layer
above an entirely Russian illustration.

Three options, and the choice is the owner's:

1. **EN figure generators** — a `make_figures_*_en.py` driver per generator, on the same
   parameterize-don't-fork principle, plus per-figure re-layout where English overflows.
   The real work; probably its own issue.
2. **Ship the EN deck with Russian figures** on those 13 slides. Cheapest; fails the
   mirror-check visibly on a public site.
3. **Drop the figures** from the EN deck on those slides. The layouts would need checking:
   several patterns (`mechanics_with_figure`, `*_with_figure`, `lecture_map`) are built
   around the illustration.

Nothing in the EN track is blocked on this — translation of the other 55 slides can
proceed in parallel.

---

## Verification record (pilot — orchestrator-run, not subagent self-report)

Pilot = the frame, 9 slides: n01–n05 and n65–n68.

| Check | Result |
|---|---|
| `build_sem05_en.py --audit` | sinks: 0 outside `deck_kit.py`; 196 live Cyrillic literals classified |
| `build_sem05_en.py --selftest` | **PASS** — all 68 slides identical to committed `sem-05.pptx` |
| `build_sem05_en.py --roles` | **PASS** on 15 quote blocks (after fixing n68's wording) |
| EN build warnings | **3**, all of them the honest `РУССКАЯ СХЕМА` figure flags |
| EN build overflow / fit warnings | **0** |
| Cyrillic in `ppt/slides` + `ppt/notesSlides` | **0** |
| Cyrillic in EN slide bodies | **0** |
| `«»` in EN artifacts | **0** outside `visual.backup` (D7) |
| `check_tracks_pdf.py --self-test` | **PASS** — 5/5 synthetic cases classified correctly |
| `check_text_overlap_pdf.py --self-test` | **PASS** — 4/4 synthetic cases classified correctly |
| `check_tracks_pdf.py` on frame pages | **0** figures cutting text |
| `check_text_overlap_pdf.py` on frame pages | **0** text-on-text overlaps |
| `audit_sluzhebnoe.py sem-05-en.pptx` | **clean** — no service text in the visible layer |
| RU artifacts unchanged | `git status` clean for `slides/`, `deck.yaml`, `sem-05.pptx`, all `rendered/*.py` |
| Real render reviewed | 9/9 frame slides opened at full size from `pptx_to_png.sh` output |

Line spacing (`notes/mcp-limitations.md` `[#211-1]`, `[#211-2]`) is untouched: the driver
adds no spacing logic, and `check_tracks_pdf`'s own spacing probe still measures 23.4 pt
against a 23.4 pt expectation.

---

## Open items for the owner

1. **Figures** — the decision described above. 13 slides, 48 PNGs, 7 generators.
2. **`_col_shares` measures headers as written, not as drawn** (bold + caps). A latent RU
   defect; patched EN-only. If the owner wants it fixed properly, it belongs in
   `deck_kit.py` — but that re-proportions approved RU tables and needs a re-review of the
   RU render.
3. **Section name `Сборка` → *Wrap-up*.** Part C of the glossary already locks
   «Сборка кодинг-агента» → *Setting up a coding agent* for Seminar 4. Different sense,
   different answer; flagged so it does not read as drift.
4. **`завязка` must never be translated *the hook*.** Natural in narrative English, fatal
   here — `hook` is the seminar's central product term. Locked in glossary Part D.
5. **Dates stay `DD.MM.YYYY`** (D6), as in Seminar 4.

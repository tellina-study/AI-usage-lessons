---
name: en-render-runbook
issue: 172
status: active
---

# EN Deck Re-render Runbook (issue #172, Ф3)

Playbook for producing an **English-rendered deck** from an existing Russian one.
Validated on lec-01 (calibration): 0 EN-introduced layout breaks, rendered pptx Cyrillic=0.

## Method (a) — duplicate the generator

Build scripts are **bespoke per lecture** with hardcoded visible strings. There is no
per-language switch, so the path is: translate sources, duplicate the builder, repoint it.

### Steps

1. `cd /home/harness/harness-projects/256/.worktrees/folder-288/publish-8a63bf98`; verify
   `git branch --show-current` == `issue-172-bilingual-production` (STOP if not).
2. Read `tools/lecture-production/glossary-ru-en.md` and follow it **exactly** (EN column,
   US-spelling, brands verbatim, proper-noun first-use gloss, `рубежный контроль → midterm`,
   `провал → failure` / `урок → lesson`, deployment + metrics clusters).
3. **Identify the authoritative builder** for lec-NN: the script under
   `library/lectures/lec-NN/rendered/*.py` whose output is `lec-NN.pptx`
   (`grep -l "lec-NN.pptx" library/lectures/lec-NN/rendered/*.py`). If multi-part / unclear,
   pick the one that assembles the full current deck and **note the ambiguity in your report**.
4. Translate `deck.yaml` → `deck.en.yaml`: `title`, `central_question`, all `assertion`s,
   `audience`; set `language: en`. Internal design-notes (`learning_goal`, `visual.primary`)
   may stay RU (not student-visible) — translate only if trivial.
5. Translate `slides/*.md` → `slides-en/*.md` (visible text **and** `## Speaker notes`).
6. Duplicate builder → `build_lecNN_en.py`; translate the hardcoded **rendering** Cyrillic
   strings; repoint `SLIDES_DIR = "slides-en"` and `OUT = "lec-NN-en.pptx"`.

### GOTCHAS (found in calibration — do not skip)

- **`NOTES_INLINE` / `SLIDE_REFS` anchors are RU-keyed.** The inline-`[N]` citation injector
  matches Russian phrases against note bodies. On EN notes they **silently stop matching and
  citation markers vanish with no error**. Grep the script for `NOTES_INLINE`/`SLIDE_REFS`/
  anchor dicts and translate the **keys** too.
- **`Источники:` heading** is detected by literal `startswith` (often in 2 places) → change to
  `Sources:` in **both** the script and the EN md, or the numbered source list detaches.
- **Render toolchain:** `source /home/harness/.local/lo-portable-env.sh` gives `libreoffice`/
  `pdftoppm`. If a concurrent run hits a LibreOffice **profile-lock** error, pass a unique
  profile: `-env:UserInstallation=file:///tmp/lo-lecNN`.
- **Do NOT translate inert docstrings/comments** — only strings that render. A blind
  "translate every Cyrillic line" wastes effort and can corrupt logic.

### Heavy-builder variant (lec-04 lesson — check this!)

Some builders are **thicker** than lec-01: visible slide text lives in Python modules
(`slides_band*.py`, `_helpers.py`, `SLIDE_REFS` dicts) — NOT only in md. Repointing
`SLIDES_DIR` alone then yields a **Russian** deck. Translate the full band/helper module set too.

**Charts with baked-in Cyrillic (CRITICAL — invisible to the XML scan).** If the deck embeds
chart PNGs generated with Russian labels (look for a `gen_charts*.py` / `assets/charts/`),
the text is **rasterized into the image** — `grep` over slide XML will NOT catch it and the deck
passes the text scan while showing Russian charts. You MUST duplicate the chart generator
(`gen_charts_en.py`), translate its titles/axes/legends/labels, output `assets/charts-en/`, and
repoint the builder to it. **Visually inspect every chart slide** in the EN render.

Toolchain note: `lo-portable-env.sh` may expose the binary as `soffice` (not `libreoffice`).

### Render + verify

7. Render `lec-NN-en.pptx`, convert → `lec-NN-en.pdf` (libreoffice), optional PNG via pdftoppm.
8. **VERIFY (mandatory):** unzip pptx, `grep -rE '[А-Яа-яЁё]'` over `ppt/slides/` +
   `ppt/notesSlides/` → **must be 0**. Sample 6-8 high-risk slides (matrices, quadrants,
   timelines, dense metric cards) for overflow; fix only egregious clips (near-zero expected —
   English absorbs into fixed-geometry boxes). Full 36-slide QA not required.
   **Also visually check every chart/image slide** — rasterized Cyrillic in chart PNGs passes the
   text grep (see Heavy-builder variant above).
9. **Do NOT `git commit`.** Leave `snapshots-en/` PNGs untracked (regenerable; repo convention).

### Report back (return value)

Per deck: builder used (+ any ambiguity), files produced, count of strings/notes translated,
Cyrillic-scan result, any layout fixes, blockers.

## Builder inventory (authoritative script to confirm, not blindly trust)

| Lecture | Candidate builder | Note |
|---|---|---|
| lec-02 | build_lec02.py | |
| lec-03 | build_v1.py | generic name — confirm it outputs lec-03.pptx |
| lec-04 | build_lec04_v4.py | |
| lec-05 | build_lec05.py | |
| lec-06 | build_lec06.py | |
| lec-07 | build_lec07.py | |
| lec-08 | build_lec08.py | |
| lec-09 | build_lec09_part2.py | name says part2 — confirm full-deck entrypoint |
| lec-10 | build_lec10_p1.py | name says p1 — confirm full-deck entrypoint |
| lec-11 | build_lec11_part2.py | name says part2 — confirm full-deck entrypoint |
| lec-12 | build_all.py | generic — confirm |
| lec-13 | build_lec13.py | |
| lec-15 | build_lec15_main.py | |
| lec-17 | build_lec17.py | |
| lec-14 | — | NO builder — EN deck deferred (separate issue) |

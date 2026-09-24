# Lecture 4 — EN deck iteration log (issue #172 / #162)

Visual-loop log for the English twin of the Lecture 4 deck
(`rendered/lec-04-en.pptx`, built by `build_lec04_en.py` from
`slides_band{1..4}_en.py` + `slides-en/*.md`).

Per-block sections. Each block owns a disjoint slide range; the final
assembly pass reconciles the overall slide count and `deck*.en.yaml`.

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

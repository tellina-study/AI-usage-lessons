# Iteration log — issue #155, comment #175: s06a real photo insert

**Scope:** single point-fix — add a real photo (Walter Pitts + Jerome
Lettvin, 1959) to slide s06a (McCulloch-Pitts 1943 fact-bridge), per owner
decision after the originally-requested "1943 joint photo" URL turned out
to be a mislabeled 1963 Nobel Prize cover with unrelated scientists.

This log picks up the `s06a photo (#175) — on pause, awaiting owner-
supplied source` item flagged as not-touched in `iteration-log-issue155.md`
(Round 2 QA-fix pass) — now unblocked by the owner's explicit substitute
decision recorded in this task's brief.

---

## Owner decision recap

- No clean-license solo portrait of McCulloch or Pitts exists.
- The only clean-license Pitts photo available is a **1959 group photo**
  (Wikimedia Commons, file `Lettvin_Pitts.jpg`, CC BY-SA 3.0): Walter Pitts
  with colleague Jerome Lettvin, examining a frog (their joint MIT
  experiment). Owner explicitly approved using this photo — NOT a 1943
  portrait — with correct attribution + an explicit "this is not 1943"
  disclaimer in the caption, since the slide's assertion is about the 1943
  publication and a naive reader could otherwise assume the photo is
  contemporaneous with the paper.
- File already downloaded to
  `library/lectures/lec-01/assets/images/lettvin-pitts-1959.jpg`
  (490×662 px) before this session started.

## Image acquisition tier (per `tools/presentation-build/README.md` §5.7)

**Tier 2 — Wikipedia / Wikimedia Commons.** Direct CC BY-SA 3.0 source,
not a mock/fallback. No further tiers needed — Tier 2 succeeded on the
first (owner-supplied) attempt. Source URL:
`https://commons.wikimedia.org/wiki/File:Lettvin_Pitts.jpg`.

Per-image log (single image, single slide):

| Attempt | Tier | URL | Result |
|---|---|---|---|
| 1 | 2 (Wikimedia Commons) | `commons.wikimedia.org/wiki/File:Lettvin_Pitts.jpg` | SUCCESS — CC BY-SA 3.0, already downloaded, owner-approved substitute for the invalid original request |

No mock fallback used — this is a real, licensed, historically-accurate
(for 1959, correctly captioned as such) photograph.

## Pre-processing

Source jpg (490×662, portrait ratio 0.74 — very tall/narrow, mostly empty
dark background at top/bottom) was cropped with Pillow (ImageMagick not
available in this environment, see `notes/mcp-limitations.md` [#153-1] —
Pillow used as the available alternative) to trim ~4% off the top and ~10%
off the bottom, keeping both faces, both hands, and the frog fully
visible. Result: 490×569 px, ratio 0.861 — a more sidebar-friendly portrait
crop, saved as
`library/lectures/lec-01/assets/images/lettvin-pitts-1959-crop.jpg`. Original
uncropped file kept alongside, untouched, for provenance.

## Layout change — `build_s06a` in `build_lec01.py`

Before: two year-anchor boxes (1943 / 1956, 3.7" wide each) centered with
a gold "13 лет" bridge between them, plenty of unused white space on the
right (slide was intentionally minimal/compact, 1-minute fact-bridge).

After: added a right-hand photo sidebar (~2.0"×2.3", aspect-locked to the
cropped image's native ratio so the photo is never stretched/distorted)
with a 3-line caption underneath. To make room without overloading the
slide, the two anchor boxes grew slightly wider (2.95"→ solved
algebraically, ~3.9" each, see code comment "anchor_w solved so ... ends
exactly gap_to_photo before the photo's left edge") and the whole
anchor+bridge group shifted left as a unit — this both closes the old dead
whitespace gap and keeps the photo from feeling bolted on. Gold callout +
bottom takeaway line (unchanged content) still run full-width beneath,
untouched.

Caption text (final, all 3 required elements present):
> «Питтс (справа) и Леттвин, 1959 — опыт с лягушкой в MIT (это НЕ фото
> 1943 г.). Wikimedia Commons, CC BY-SA 3.0.»

Covers: (a) who — Питтс + Леттвин, (b) year — 1959, (c) explicit
not-1943 disclaimer, (d) source + license.

## Visual loop (Generate → Convert → Inspect → Fix)

Environment note: `libreoffice`/`pdftoppm` needed the [#153-1] PATH +
LD_LIBRARY_PATH workaround from `notes/mcp-limitations.md` — applied at
the start of every render command in this session.

### Iter 1

- **Generate:** first pass — fixed photo box at 2.55"×3.44" (uncropped
  image, native 490×662 ratio), gap between anchor-pair and photo left as
  leftover space (~3.5") rather than solved algebraically.
- **Convert:** `libreoffice --headless --convert-to pdf` + `pdftoppm -r 110`
  on page 9 (s06a is slide index 9 in `BUILDERS`).
- **Inspect (found problems, as required — not accepting a clean first
  render):**
  1. **Caption text overflow/clipped** — 2-line caption at 9.5pt in a
     0.85"-tall box ran past the box into/under the gold callout below;
     bottom line ("1943 г). Wikimedia Cor...") visibly cut off in the PNG.
  2. **"13 лет" bridge label wrapped to 2 lines** ("13" / "лет" stacked),
     overlapping the gold pill bar — bridge_w had shrunk to 0.70" (too
     narrow for 22pt text on one line) as a side effect of widening
     anchor_w without re-checking the bridge math.
  3. Large empty gap (~3.5") between the right anchor box and the photo —
     visual mass imbalanced, looked like the photo was an afterthought
     bolted onto unrelated whitespace.
- **Fix:** switched to the cropped image (490×569, ratio 0.861); solved
  `anchor_w` algebraically from `photo_x` so there is no leftover dead
  gap; widened `gap_w` between anchors (1.0"→1.3") and reduced bridge font
  22pt→20pt with a wider text box (bridge_w+0.5") so "13 лет" fits one
  line; shortened + shrank caption text (8.5pt→7.8pt, tighter line spacing)
  to fit a smaller vertical budget above the gold callout.

### Iter 2

- **Generate:** rebuilt with all iter-1 fixes.
- **Convert + Inspect:** full-slide PNG + 2 targeted crops (photo/caption
  region at high zoom, bridge region at high zoom, right-margin region).
  - Caption now fully visible, all 3 lines readable, all 4 required
    elements present.
  - "13 лет" renders on one line, gold pill bar centered underneath.
  - Photo not stretched or distorted (aspect-locked math verified against
    rendered pixels).
  - Right margin of photo box ≈ same 0.55" margin convention used
    elsewhere in the deck (checked via crop).
- **Remaining minor issue:** none blocking; gold bridge bar reads slightly
  short relative to the "13 лет" text width above it, but this matches
  the deck's pre-existing pattern for this exact element (unchanged bridge
  bar width logic) — not a regression introduced by this fix.
- **Fix:** none needed structurally; proceeded to iter 3 for final
  sign-off checks (5-Second Test + Projector Readability) per the
  mandatory ≥3-iteration rule.

### Iter 3 — final accept gate

- **5-Second Test:** looked at the full-slide PNG at a glance. Main
  message read: "1943 → 1956, 13-year gap" — matches
  `slide.assertion` ("Идея нейросети старше самого термина «искусственный
  интеллект» на 13 лет"). PASS. The photo sidebar supports the fact
  ("here's real evidence one of these two people existed and did related
  work") without competing with or diluting the main assertion.
- **Projector Readability (50% zoom):** downscaled the PNG 50% and
  re-read. Year numbers (1943/1956), "13 лет" bridge, and gold callout
  all still read clearly. Photo caption is small (as expected/appropriate
  for a citation-tier caption per the footer-tax convention) but the photo
  itself and its role are unambiguous even at reduced size. PASS.
- **Verdict: ACCEPT.**

## Files touched

- `library/lectures/lec-01/rendered/build_lec01.py` — `build_s06a` (photo
  sidebar + re-solved anchor/bridge geometry).
- `library/lectures/lec-01/slides/s06a-prehistory-1943.md` — `## Visual`
  section updated to describe the new photo sidebar + caption contract.
- `library/lectures/lec-01/assets/images/lettvin-pitts-1959-crop.jpg`
  (NEW — cropped working copy; original `lettvin-pitts-1959.jpg` kept
  untouched for provenance).
- `library/lectures/lec-01/rendered/lec-01.pptx` / `.pdf` (regenerated,
  36 slides, unchanged count).

## Not touched

Everything else in the deck — this was a single-slide point-fix per the
brief's explicit scope (s06a only).

## PROPOSED ADDITION (not applied — reporting per No Extra Content Rule)

None. Stayed within the single-slide scope of comment #175.

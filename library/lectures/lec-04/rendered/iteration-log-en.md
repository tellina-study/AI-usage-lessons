# Lecture 4 — EN deck iteration log (issue #172 / #162)

Visual-loop log for the ENGLISH twin of the Lecture 4 deck (`lec-04-en.pptx`).
The RU log lives in `iteration-log.md` / `iteration-log-part2..5.md`; this file
only records EN-side work. Each EN-sync block appends its own section.

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

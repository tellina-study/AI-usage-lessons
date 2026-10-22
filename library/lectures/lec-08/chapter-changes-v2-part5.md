# Chapter changes v2 — Part 5 (`chapter-part5.md` + `chapter-part5b.md`)

Phase 4 revision per `chapter-critique-v2-methodology.md`, `chapter-critique-v2-facts.md`,
`chapter-critique-v2-reader.md`. Scope: these two files only (4 sibling agents handled the other
6 files of the 8-file chapter in parallel).

## Applied

### P1 — word count (methodology-critic §1, largest proportional gap in the chapter)

- `chapter-part5.md` narrative (§7 «Закрытие» + 15-question Q&A) grew from **3,988 → 6,021
  words** — inside the recalibrated 6,000–8,000 target (the original ~8,000-word Part-5 target
  implicitly assumed glossary+bibliography would count toward it; they legitimately don't, per
  course rule, so the real narrative target is lower and this part now clears it).
- Expansion was synthesis-level, not padding, per brief:
  - **§7.1 «Путь закрыт»**: ~375 → ~750 words. Added one synthesis clause per of the four
    "payment points" (production, editorial, release, licensing) explaining *why* each point's
    free-verification mechanism broke, not just restating that it did; added a closing paragraph
    naming the chronological-ledger structure of the four points explicitly and tying it to the
    inherited "удешевили один шаг — платят на другом" lens from Lectures 5–7.
  - **§7.2 «Долг вперёд — Лекция 14»**: ~320 → ~660 words. Added a paragraph naming the two
    concrete, *different* defensive procedures implied by the entry-vs-extraction distinction
    (identity verification at hiring vs. out-of-band verification + dual-approval at the moment of
    a financial decision — both terms already defined in the Part 5 glossary), and a closing
    paragraph explaining why the course spreads this technology across two lectures rather than
    one (depth-vs-breadth trade-off, not scheduling convenience).
  - **§7.3 «Заработанное утверждение»**: ~415 → ~700 words. Added a paragraph stating explicitly
    what the chapter's closing claim does *not* say (not "AI is dangerous," not "training
    vigilance solves it" — ties to the human-detection-rate finding), and a fifth practical
    question for the engineer (who pays if the check fails, and is the client willing to say so
    out loud) appended to Раздел 6's existing four refusal criteria.
  - **Q6 (RIAA)**: +~230 words — explains *why* the three labels split (catalog size/value →
    risk tolerance, same settle-vs-litigate calculus as Getty v Stability in Раздел 4) and draws
    the practical implication for an engineer licensing music for a generative product (risk is
    per-rightsholder, not per-industry).
  - **Q8 («три-четыре порядка»)**: +~215 words — names the general measurement principle
    ("сопоставимая пара, не более дорогой/дешёвый родственник") and ties it to two other places
    in the chapter where the same discipline is applied (Upwork/BLS, statutory cap vs. real
    award), plus a practical takeaway for an engineer computing similar ratios on new material.
  - **Q14 (statutory vs. settlement)**: +~195 words — explains the negotiation mechanism that
    makes a settlement a rational outcome for both sides (cost of continued litigation vs. cost
    of delayed payment), cross-references Getty v Stability (Раздел 4) as the "rightsholder loses
    outright" counterfactual, and gives a practical reading rule for headline statutory-cap
    figures.
  - **Q15 (closing)**: +~150 words — added two closing paragraphs: that any single number in the
    chapter will date quickly (tariffs/settlements are re-cut yearly) but the *form* of measurement
    outlives any one number, and that the 5-step breakdown form itself (not a specific fact) is the
    transferable skill the chapter asks the reader to take away.

### P1 — deepfake-detection-rate reconciliation (fact-checker, new finding)

- **`chapter-part5b.md`**: added a full bibliography entry — Diel, A., Lalgi, T., Schröter, I. C.,
  MacDorman, K. F., Teufel, M., Bäuerle, A. (2024). «Human performance in detecting deepfakes: A
  systematic review and meta-analysis of 56 papers». *Computers in Human Behavior Reports*, vol.
  16, article 100538. https://doi.org/10.1016/j.chbr.2024.100538. Confirmed via live WebSearch
  (exact journal/volume/article number found — no `[FACT-CHECK]` marker needed, this is a real,
  citable, peer-reviewed source, not an invented-precision guess). Placed alphabetically between
  `designshifu.com` and `Министерство юстиции США` entries.
- **`chapter-part5.md` Q3**: rewrote the detection-rate passage to (a) name the source explicitly
  ("по метаанализу Diel et al. (2024)..."), (b) give the precise figures (62.08/57.31/53.16/52.00%
  plus overall 55.54% vs. 68.08% for real stimuli, N=86,155 across 56 studies), and (c) add the
  reconciliation the brief asked for: the 24–25% figure in `chapter.md` §0.2 is a narrow,
  primed/warned lab condition (participant told to look for a fake); the 57% (video) in Q3 is a
  pooled meta-analysis across 56 general-population studies without that priming. Both numbers are
  shown to agree on the substantive conclusion (neither condition clears much above chance), so a
  careful reader is told explicitly not to read one as disproving the other.

### P2 — removed 3 orphaned Arup bibliography entries

Deleted from `chapter-part5b.md`: IDEMIA (2024), PRMIA (2024), SCMP (2024) — all specifically
about the Arup CFO-deepfake case, which was removed from this lecture's architecture entirely
(covered by Lecture 14). Confirmed zero narrative use of any of the three before deleting
(`grep -n "Arup"` across the file now returns only the frontmatter comment documenting the
removal itself, no live citation or narrative mention).

### P2 — preserved Q11 / the YouTube-thumbnail honesty passage

Not touched. Left Q11's answer and the closing bibliography note ("Что в этом списке честно
отмечено, а не просто пропущено...") exactly as they were — length, content, and the word
"честно" inside them all untouched, per the brief's explicit instruction not to shorten or edit
this passage for word-count reasons.

### P2 — trimmed "честно/честный" overuse (5 instances across the two files)

- `chapter-part5.md` §7.3: "Это и есть честный итог" → "Это и есть заработанный итог"
- `chapter-part5.md` Q2: "глава называет это честно" → "глава называет это прямо"
- `chapter-part5.md` Q8: "при честном выборе сопоставимой пары" → "при аккуратном выборе
  сопоставимой пары"
- `chapter-part5.md` Q12: "стоит честно отметить методологическую границу" → "стоит прямо назвать
  методологическую границу"
- `chapter-part5b.md` (bibliography intro): "это честно отражает природу материала главы" → "это
  прямо отражает природу материала главы"

Left all instances inside Q11 and its matching bibliography note untouched (protected, see above).

### P2 — calque fix

`chapter-part5.md` Q3: "измерена близко к случайному гаданию" → "измерена близко к случайному
угадыванию — как при подбрасывании монеты для бинарного выбора «настоящее/подделка»" (done as
part of the same edit that added the Diel et al. reconciliation).

## Mandatory checks (run after all edits)

**Word count** (`tools/lecture-production/count_chapter_words.py library/lectures/lec-08 --parts`):

```
chapter-part5.md:   6,021 words  (target 6,000–8,000 — PASS, inside band)
chapter-part5b.md:      0 words  (EXPECTED — pure glossary + bibliography, excluded by course
                                   rule; documented explicitly in the file's own frontmatter so
                                   nobody "fixes" this as a bug later)
```

**Deep Latin-token scan** (`tools/presentation-build/deep_latin_scan.py`):

```
chapter-part5.md:   107 occurrences, 46 unique tokens outside the script's static brand allowlist
chapter-part5b.md:  332 occurrences, 201 unique tokens outside the script's static brand allowlist
```

Reporting these counts as-is, not as "0 hits," per the task's own instruction. Inspected every
unique token in both files' top-hit lists by hand: all are proper nouns, case names, product/brand
names, or acronyms already established in the chapter's own narrative (Getty, CNET, Stability AI,
Stable Diffusion, Suno, Udio, Warner, UMG, Sony, CARMA, System1, Checkr, Upwork, BLS, Veo, Kling,
Kandinsky, Toys "R" Us, Shutterstock, CDPA, LAION-5B, Diel, KnowBe4, EDR, Nisos, FBI/IC3, etc.), or
the `[for-slide-sNN]` slide markers (frontmatter-equivalent, exempt). No narrative anglicism
(English prose word substituting for a Russian one) was found in either file — the script's own
acceptance note ("URLs / case names / brand markers OK") covers this entire list; its hardcoded
`BRAND_ALLOWLIST` simply doesn't enumerate every proper noun used across all 17 lectures, which is
expected and not something this revision should "fix" by inventing exclusions. No new anglicisms
were introduced by this revision's own additions (all new prose is Russian).

## Frontmatter added (both files previously had none — methodology-critic Finding 9)

- `chapter-part5.md`: full frontmatter block mirroring `chapter-part2.md`'s convention
  (`lecture`, `parts`, `title`, `part: 5`, `length_words: 6021` with derivation comment, `status`,
  `version: v2`, `issue`, `branch`, `learning_outcomes`, `strict_in_self_estimate`,
  `references_count: 0` — this part introduces no new sources of its own beyond what earlier parts
  already cite; the consolidated bibliography lives in `chapter-part5b.md`).
- `chapter-part5b.md`: frontmatter block with `part: "5b"`, `length_words: 0` carrying an explicit
  inline comment stating this is the expected, correct result for a pure glossary+bibliography
  file (not a bug), and `references_count: 78` (recounted by hand against the actual bibliography
  block structure after the Arup removal + Diel addition, not estimated).

## Not touched (out of scope for this assignment)

- The chapter-wide index table (5-files-vs-8-files drift, Finding 8a) and the `slide_map`
  frontmatter staleness (Finding 8b) live in `chapter.md` (Part 1) — sibling agent's scope.
- The NYT statutory-cap arithmetic error (fact-checker P0, `chapter-part3b.md`) — sibling agent's
  scope.
- The Getty Chapter-11 contributor-royalty hedge (fact-checker P1, `chapter-part4.md`) — sibling
  agent's scope.
- The two `[FACT-CHECK]` brackets on Sora/Disney and the Getty+Shutterstock synergy figure
  (`chapter.md`, `chapter-part4.md`) — sibling agents' scope.
- The three-utterance lecture-question count (methodology-critic Finding 2b) and the named-
  individual-per-section gap in Разделы 1/3/5 (Finding 10) — these live in other parts.

# Chapter changes v2 — Part 2 (`chapter-part2.md`)

Revision pass against Phase 3 critique (`chapter-critique-v2-methodology.md`,
`chapter-critique-v2-facts.md`, `chapter-critique-v2-reader.md`). Scope: `chapter-part2.md` only,
per orchestrator brief (4 sibling agents revising the other 7 files in parallel).

## Applied

- **P1 word count (+2,320 target).** Added two substantial blocks:
  - New "Зачем это инженеру, в одном посчитанном примере: каталог интернет-магазина" subsection
    in the §2 opening framing block (before § 2.1) — a fully worked, explicitly-labeled
    illustrative scenario (50,000-SKU e-commerce catalog) carrying the same numeric treatment
    CNET gets: error rate (conservative 5%, deliberately far below CNET's measured 53%),
    absolute count (2,500 listings), correction cost (editorial catch vs. post-publication
    return), and disclosure risk (consumer-protection exposure, named as a separate risk layer).
    Marked explicitly as illustrative, not a measured case, matching the existing §2.1/§3.1
    "эта сцена собрана по учебному материалу" convention.
  - §3.2 now carries an explicit "Инверсный случай — прямо названный пробел" paragraph: I
    searched the research files (`research/03-freshness-october-2026.md` task 2) for a
    documented case of a pre-release panel catching an AI-disclosure risk before publication and
    found none — named the absence honestly (per the brief's option (b)) rather than inventing
    a case, with a short explanation of why a caught risk would be under-reported structurally
    (no headline for a crisis that didn't happen).
  - Result: 10,680 → 12,595 words (single-file count via
    `tools/lecture-production/count_chapter_words.py`), within the acceptable 12,000–14,000 band.

- **P1 named individual, Раздел 2.** Pulled **Ross Levinsohn** (CEO, Arena Group) into §2.4 itself
  (was previously only implied as "генеральный директор" in a sibling file's Q&A, never named
  in this file). Added situation + outcome: fired December 2023 without a stated public reason
  (timing coincided with the AI-scandal aftermath); filed suit in March 2024 claiming $20–40M in
  owed compensation; case status as of available SEC filings — still unresolved, no disclosed
  settlement. Verified via live WebSearch (NBC News, MediaPost, Bloomberg Law, SEC 10-Q/10-K
  filings) before writing, not invented. Added two new bibliography entries (NBC News, MediaPost).
  Used the addition to reinforce the chapter's own existing causality-caution point (fired ≠
  proven guilty of the AI scandal).

- **P1 named individual, Раздел 3.** Checked research files first (no named individual found for
  Coca-Cola/Toys "R" Us/System1 in `research/03` task 2) — then ran independent WebSearch rather
  than declaring a gap, and found two real, quotable, verified named individuals directly on
  point: **Pratik Thakar** (Global VP & Head of Generative AI, Coca-Cola — on-record quote
  defending the repeated AI campaign, Hollywood Reporter + Adweek Brandweek 2025) and
  **Jason Zada** (founder/creative director, Secret Level — on-record headcount figure, 20 vs. 50
  people, Hollywood Reporter interview). Both added to §3.3's "Что переехало" with situation +
  outcome, tying back to the section's own "что переехало" argument and to Раздел 1's cost-collapse
  throughline. Added two new bibliography entries (both Hollywood Reporter pieces, Adweek).

- **P1 per-section audience question, Раздел 2 and Раздел 3.** Added one verbatim,
  channel-specified "Вопрос залу" block to each section (§2.5 and §3.5), matching `chapter.md`
  §0.6's format ("задаётся в чат односложно" + blockquote). §2's question probes undisclosed
  AI-authorship/correction-process experience; §3's question uses the methodology-critic's own
  suggested wording (controlled-test vs. open-audience-reaction mismatch, generalized beyond
  advertising).

- **P1 self-check forward-reference, §2.5 question 3.** Split the question: kept the
  Sports-Illustrated/ABG causality half (answerable from §2.4 content, now strengthened by the
  Levinsohn addition) and explicitly labeled the Getty-bankruptcy comparison as deferred —
  "вернитесь сюда после Раздела 5" — rather than silently requiring knowledge the reader doesn't
  have yet at this point in linear reading. Matches the reader-simulator's option (b).

- **P2 "честно/честный" density.** Counted 14 instances pre-revision (confirmed via regex, not
  just grep -c). Replaced 5 non-canonical instances with plainer alternatives ("прямо",
  "не обходя", restated without the qualifier) in §2.3 and §3.3, preserving all 3 instances of
  the canonical "честный пробел" collocation used as a recurring technical term across the whole
  chapter. Caught and fixed 2 more instances I had accidentally introduced in my own new §3.2
  gap paragraph (same two substitutions), so the net reduction is real, not offset by new
  additions. Final count: 9.

## Incidental fix

- One self-introduced anglicism: the SKU gloss in the new e-commerce example originally read
  "SKU, stock keeping unit" — replaced the English gloss words with a Russian-only explanation
  ("SKU — общепринятое сокращение для единицы учёта..."), since I noticed it while running the
  deep-latin-scan check below. Did **not** attempt a full-chapter anglicism sweep (e.g.
  pre-existing "keystone" at line 72 and "close-ended" at line 106 are untouched) — that is
  `literary-editor`'s pipeline phase, applied after content is locked, not in scope for this
  content-revision pass, and neither token is something I introduced.

## Verification

- **Word count:** `python3 tools/lecture-production/count_chapter_words.py library/lectures/lec-08/chapter-part2.md`
  → **12,595** (target ~13,000, acceptable band 12,000–14,000 — within band, close to target).
- **Deep latin-token scan:** `python3 tools/presentation-build/deep_latin_scan.py library/lectures/lec-08/chapter-part2.md`
  → **427 occurrences / 161 unique tokens flagged.** Reporting the actual number per instruction,
  not a narrative "0 hits." Manually reviewed the full top-hits list: the overwhelming majority
  are proper nouns/brand markers/publication names already explicit in CLAUDE.md's own acceptance
  carve-out ("URLs / case names / brand markers OK") — CNET, Coca-Cola, CARMA, Arena Group,
  Sports Illustrated, Toys "R" Us, Futurism, Forbes, TechRadar, Silverside AI, Hollywood Reporter,
  Marketing-Interactive, TheWrap, AwfulAnnouncing, Deadline, Sportico, Native Foreign, Getty
  Images, Minute Media, Authentic Brands Group, NBC News, MediaPost, Predictive Analytics World,
  Poynter, European Journalism Observatory, Slate, Ross Levinsohn, Pratik Thakar, Jason Zada — plus
  the `[for-slide-sNN]` structural markers (8×) and the `AI-` hyphen-prefix token (42×, a
  course-wide RU-compound convention — "AI-статья", "AI-авторство" — not a standalone English
  word). Excluding the bibliography section entirely still leaves 82 unique/254 occurrences, same
  composition. I did not find unresolved narrative-prose anglicisms beyond the one SKU gloss
  already fixed above. A full-chapter deep-scan cleanup (consistent across all 8 files, matching
  the shared P2 finding in the reader-simulator report) is `literary-editor`'s pipeline phase, not
  this content-revision pass — flagging this explicitly rather than silently passing it as "0
  hits," per instruction.
- **"честн-" density:** 14 → 9 occurrences (regex-verified both times, not grep -c).

## Downstream impact (orchestrator should be aware of, not necessarily trigger immediately)

- Two new named individuals (Ross Levinsohn's lawsuit detail, Pratik Thakar / Jason Zada quotes)
  are new factual content added during this revision pass, not present in the Phase 3 chapter
  that fact-checker already reviewed — recommend a targeted fact-check re-pass on just these two
  additions (§2.4 Levinsohn paragraph, §3.3 Thakar/Zada paragraph) before this part is considered
  fully closed, since the full-sweep fact-check predates these specific sentences.
- `chapter.md`'s frontmatter `references_count` roll-up (if any exists at the top-level) should
  reflect this part's references_count change 13 → 18.
- The self-check question renumbering/rewording in §2.5 does not change question count or
  structure, so no slide/speech cascade expected from that specific fix.

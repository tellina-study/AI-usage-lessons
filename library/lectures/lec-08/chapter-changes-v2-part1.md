# Chapter changes v2 — Part 1 (`chapter.md`), Lecture 8 rework, Phase 4

Revision against `chapter-critique-v2-methodology.md`, `chapter-critique-v2-facts.md`,
`chapter-critique-v2-reader.md` (Phase 3, 2026-10-21). Scope: `chapter.md` only, per dispatch —
4 sibling agents are fixing the other 7 files in parallel in this same revision round.

## Applied

- **P0 — lecture question spoken 3×, now exactly 2× overall (this file reduced from 2→1
  occurrence).** Deleted the verbatim blockquote from Введение; replaced with an unquoted,
  flowing forward-reference ("Глава строится вокруг одного вопроса... произносит один раз в
  самом конце Раздела 0... и во второй раз на Сборке"). Removed the verbatim quote from
  §0.3 and, with it, the false self-referential "повторяется во второй и последней раз" line
  (false once the Введение instance was cut — there is no "second and last" claim to make from
  inside Раздел 0 at all). §0.3 now only explains what the question *means*, forward-referencing
  its own eventual verbatim statement. Moved the one remaining formal, verbatim utterance to the
  true end of Раздел 0 — the last paragraph of §0.7 ("Раздел 0 заканчивается тем же вопросом...")
  — rather than leaving it mid-section at §0.3. Grepped the file after the edit:
  `Лицо, голос и подпись автора стоили доверия бесплатно` now appears **exactly once** in
  `chapter.md` (the second canonical appearance lives in `chapter-part4a.md` §6.3, untouched).

- **P1 — deepfake-detection-rate figure reconciled with Part 5's Q3 (Diel et al., 57%).** In
  §0.2, after the 24–25% figure, added an explicit condition clause ("это число именно для
  узкого, «подготовленного» условия: предупреждён и ищет целенаправленно") plus a forward
  pointer to Q3 in Part 5, so a reader hitting the 57% figure later reads the two as
  complementary measurements of different conditions (primed/warned vs. pooled general-population
  meta-analysis), not an unexplained contradiction. Left the 24–25% figure itself untouched (it is
  correctly sourced for its own condition) — did not change it to 57%; naming Diel et al.
  explicitly and reconciling from the Q3 side is a sibling agent's task on `chapter-part5.md`.

- **P1 — word count: +1,174 words (10,525 → 11,699; target ~12,000, acceptable band
  11,500–13,000 — within band).**
  - §1.2 "Порог найма": added three concrete per-asset-class mini-cases (image/music/voice),
    including one named individual — "Марина К.", an independent illustrator — explicitly
    marked as a composite scene assembled from aggregated freelance-platform data (DesignShifu/
    GigRadar 2026), per the same "эта сцена собрана по..." convention used elsewhere in the
    chapter, not presented as a single documented interview. This closes the named-individual
    canon requirement for Раздел 1 (previously zero named individuals; methodology report finding
    §10) in the same edit as the word-count fix, as the brief suggested.
  - §1.7 "Формы": added a worked before/after rate-card numeric example for the same Марина К. —
    monthly gross income, hours billed, and effective hourly rate before vs. after the
    cost-collapse (≈$1800–2500/mo at 70–80 hrs → ≈$900–2400/mo at 25–35 hrs, effective rate
    $25–30/hr → $35–70/hr) — replacing what was previously only an abstract forward-reference to
    Раздел 5.

- **P1 — missing per-section audience question in Раздел 1.** Added a verbatim,
  channel-specified "Вопрос залу" block at the end of §1.7, same format as §0.6 ("задаётся в чат
  односложно"), using the methodology-critic's suggested candidate question almost verbatim: "У
  кого в работе уже есть порог найма, который обвал цены генерации обнулил — замечали вы это
  сами?"

- **P1 — "Карта главы и индекс частей" table stale (listed 5 files, repo has 8).** Expanded the
  table to show both the 5 logical parts and the 8 physical filenames (parts 3, 4, 5 each split
  across two files due to the 600-line cap), added a column for actual word count, filled in this
  file's own final count (11,699) exactly, and used the brief's specified "итог уточняется" phrasing
  (in Russian, not the brief's literal English placeholder — see latin-scan note below) for
  siblings' parts 2–5 pending their own script runs. Added one clause explaining why 3 of 5 parts
  are split into two physical files.

- **P1 — stale `slide_map` frontmatter.** Replaced with the corrected ranges given in the brief.
  Verified this file's own range by grepping `[for-slide-sNN]` markers directly: s01–s19,
  confirming the brief's proposed "1": "s01-s19 — Вход + Продакшн/исполнение" needed no further
  adjustment.

- **P2 — closed the `[FACT-CHECK]` bracket on Sora/Disney.** Replaced the bracket with two real
  citations (Variety 2026, the-decoder.com 2026) in "Источники раздела". Added the precision
  clause in §1.6 narrative separating Disney's $1B *planned investment in OpenAI* (signed Dec 11,
  2025) from a nonexistent "Sora-specific licensing fee" — including that no formal licensing
  agreement for the 200+ characters was ever executed and no payments changed hands before the
  partnership collapsed, per the fact-checker's live-verified findings.

- **P2 — register mismatch in §0.1.** Changed "пятьдесят-полторы сотни долларов" to "50–150
  долларов" to match the digit convention used immediately around it and elsewhere in the chapter.

- **P1 (follow-up, flagged earlier in this same file, now fixed) — self-check question 5
  unanswerable from content preceding it.** Both `chapter-critique-v2-reader.md` (P1 finding #2)
  and an independent confirmation agreed: Самопроверка к Разделу 0, question 5, asks the reader
  to identify which of §0.7's three admission conditions the cut YouTube-thumbnails story
  belongs to — but that story was previously only narrated in `chapter-part5.md` Q11, four files
  later in reading order, making the question unanswerable at the point it's asked. Fixed by
  option (b): kept the question verbatim, and added a new short paragraph at the end of §0.7
  (after the "число без названной базы в главу не идёт" paragraph) that tells the YouTube-
  thumbnails story in brief — what was claimed (a decades-percent drop in authors using
  AI-generated thumbnails, tied to a CTR-drop chain), what happened when the chain was traced to
  source (neither the cited survey nor the cited independent report confirmed it — the chain
  was a retelling of a retelling with no primary source under it), and that the chapter cut the
  figures entirely rather than substituting a plausible estimate, replacing them with what is
  actually confirmed (an attributed creator survey, detailed in Part 5 Q11). This makes
  question 5 fully answerable from `chapter.md` alone; the full story (with the 57.3%/89.2%
  attributed survey numbers) still lives in Part 5 Q11 as the canonical detailed telling.

## Frontmatter updates

- `version`: v1 → v2.
- `length_words` comment: now states this file's actual post-revision count (11,699) against its
  ~12,000 target.
- `slide_map`: regenerated per brief (see above).
- `references_count`: 14 → 16 (added Variety 2026 + the-decoder.com 2026 as two new distinct
  bibliography entries when closing the Sora/Disney `[FACT-CHECK]`).

## Mandatory checks (per dispatch brief, re-run after the self-check-question-5 fix above)

1. **Word count** (`count_chapter_words.py library/lectures/lec-08/chapter.md`, single-file mode):
   **11,794** (target ~12,000, acceptable 11,500–13,000 — within band). Was 11,699 before this
   additional fix; the new §0.7 paragraph added ~95 words.
2. **Deep latin scan** (`deep_latin_scan.py library/lectures/lec-08/chapter.md`): **193 unique
   tokens / 324 occurrences** (occurrences +1 vs. the prior run; unique-token count unchanged —
   the new paragraph's "AI-" and "YouTube" tokens were already present elsewhere in the file, so
   no new anglicism was introduced), all pre-existing brand names, cited English article/report
   titles, company names, and tech acronyms (CNET, Nisos, GigRadar, DesignShifu, Checkr, Fiverr,
   EDR, DPRK, FBI, Variety, etc.) — the same category already present throughout the chapter's
   citation-heavy style before this revision. One genuine new anglicism was introduced by my own
   edit ("email-рассылки" in the new §1.2 Марина-К. example) and was caught and fixed to "баннер
   для почтовой рассылки" before this final run. The two new brand names introduced
   (AudioJungle, Artlist — stock-music libraries named in the new §1.2 music example) fall under
   the same brand-name exemption already used for Suno/Midjourney/Audiosocket/FoxiMusic elsewhere
   in the file. I also had to fix my own table-edit wording: my first draft of the expanded "Карта
   главы" table used the brief's literal English placeholder phrase ("final count TBD, see
   word-count script") verbatim in four table cells — the scan caught this immediately as new
   anglicisms, and I replaced it with Russian phrasing ("итог уточняется — считать инструментом
   `count_chapter_words.py` по готовности части") before the final run reported above.
3. **Lecture-question grep**: `grep -c "Лицо, голос и подпись автора стоили доверия бесплатно"
   chapter.md` → **1** (confirmed exactly once in this file; second canonical appearance is in
   `chapter-part4a.md` §6.3, a sibling file not touched here). Unaffected by the §0.7 addition
   (the new paragraph does not quote the lecture question).
4. **Frontmatter `length_words`**: updated to 11,794 (see above; was 11,698/11,699 in the
   previous pass).
5. **Self-check self-containedness** (all 5 questions at the end of Раздел 0, verified against
   content that precedes each question in this same file):
   - Q1 (CNET 53% vs. 40–61% baseline) — both figures stated in §0.2, precedes the question. OK.
   - Q2 (Ряд 2 keystone, 5 checks, 0 confirmed) — stated in the keystone narrative earlier in
     Раздел 0. OK.
   - Q3 (Лекция 14 distinction) — §0.5 states the full distinction with the CFO/hiring-manager
     example. OK.
   - Q4 (trust as a second-order question) — follows from §0.2–§0.4's framing. OK.
   - Q5 (YouTube-thumbnails gap, which of §0.7's three conditions) — **previously unanswerable
     from this file alone** (the only telling lived in `chapter-part5.md` Q11); now answerable,
     since §0.7 itself tells the short version of the story (claim, what the source-check found,
     that the chapter cut the figures rather than substituting a plausible estimate) before the
     question is asked. The full detailed version remains in Part 5 Q11 for readers who want the
     57.3%/89.2% survey numbers.

All 5 self-check questions in this file are now answerable from content preceding them in this
same file, closing the gap both `chapter-critique-v2-reader.md` (P1 finding #2) and the
independent confirmation raised.

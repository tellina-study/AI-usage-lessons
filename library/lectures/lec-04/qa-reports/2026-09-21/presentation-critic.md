# Presentation Critic Report — Лекция 4 — 2026-09-21 (round-3, issue #162)

VERDICT: REVISE

## Сводка

Scope: focused vision-enabled pass on 13 flagged slides (7 new: s09b, s17b, s18b,
s20g, s30b, s33b, s37b; 6 changed: s20d/s20e, s16, s34, s37-synthesis-matrix, s25c,
s21+s38-triangulation), rendered from the current `lec-04.pptx` → `lec-04.pdf`
(57 pages) in `library/lectures/lec-04/rendered/`. Method: mapped every deck.yaml
slide id to its actual PDF page by matching rendered text against each slide's
`assertion:`, rendered pages to PNG at 150dpi, and read each PNG directly.

- Слайдов проверено визуально: 15 (13 targeted + 2 immediate-neighbor context:
  s18, s38)
- P0 issues: 0
- P1 issues: 8
- P2 issues: 5

**Headline finding not in the original brief**: deck.yaml's declared slide order
and two of its `file:` references have drifted from what is actually in the
rendered PPTX. This is a structural/traceability defect, found precisely because
this was the kind of check a skipped 3rd iteration would normally catch. See
"Cross-deck issues" — it is the main reason the verdict is REVISE rather than
APPROVE-WITH-POLISH, on top of the anglicism and word-wrap findings below.

## По слайдам

### Slide s09b — "Дисциплина заранее — быстрый результат; без неё отказ ожидаем, не случаен" (page 11/57)
**Severity:** P1
**Issue:** Deep anglicism hits in visible body: "AI-agent deployments" (card
sub-heading, full English noun phrase inline in RU sentence), "76% **failed** за
90 дней" (English verb mixed into RU clause), "MEDIUM confidence" / "LOW-MEDIUM
confidence" (English data-quality labels, no RU equivalent anywhere in deck),
"Production-ready агент", "spec-first **workflow**".
**Recommendation:** Translate to RU: "76% отказали/провалились за 90 дней";
"средняя достоверность" / "низкая-средняa достоверность" for the confidence
labels (keep consistent if this labelling convention recurs elsewhere in the
deck); "внедрений AI-агентов" for the card heading; "рабочий процесс" for
workflow.
**Visual evidence:** Two-column comparison card (AWS Kiro success, gold check /
847-deployments failure, teal X) — visual balance and Ocean palette are clean;
issue is text-content only.

### Slide s16 — "Отравленный контекст: AI не отличает «так сложилось» от «так правильно»" (page 18/57)
**Severity:** APPROVE-CLEAN
**Issue:** None found. Top qualifier banner correctly scopes the claim ("КОГДА
архитектура не описана..."), matching the round-3 fix described in the brief
(AI-на-периферии → co-architect framing). Schema-cycle loop (left) + 3
countermeasure cards (right, ADR / fitness-functions / human-owns-forks) +
gold takeaway banner. Gold ≥1×, motif consistent, no timing/methodology leak.
**Recommendation:** none.

### Slide s17b — "Саморевью — обязательный шаг между code и commit, не факультативная привычка" (page 21/57)
**Severity:** APPROVE-WITH-POLISH
**Issue:** Content and visual balance are good (incident story + verbatim
English quote left, "different failure mechanism" + Uber ~11% scale-contrast
stat right). Minor: bottom banner buries the actual lesson slightly behind a
long compound sentence; "check" appears as a bare English word in quotes.
**Recommendation:** P2 — consider trimming closing banner to one clause; swap
"check" for "проверка".
**Visual evidence:** clean two-box layout, gold banner present, Ocean palette
consistent.

### Slide s18b — "Курирование не устраняет риск — оно меняет один риск на другой" (page 23/57)
**Severity:** P1
**Issue:** 3 equal cards (compaction / JIT-retrieval / stale AGENTS.md) are
visually clean and well-balanced (Schema Readability: fill ratio good, icons
consistent, no overflow). BUT this slide's clarity **depends on "JIT-retrieval"
having been defined already** — which only happens on s19 ("persistent memory
layer"). See Cross-deck issues: deck.yaml declares s18b positioned *before*
s19, which would show "JIT не спросит о неизвестном" before JIT is ever
introduced. The **actual render** (page 22 = s19, page 23 = s18b) gets this
right, but only by accident of the build script disagreeing with the documented
spec — nothing enforces this stays right on a future re-render from deck.yaml.
**Recommendation:** Fix deck.yaml's declared order to match the render (or vice
versa, but the render's order is the pedagogically correct one — keep it and
correct the metadata).
**Visual evidence:** page 23, 3-card layout, gold banner bottom.

### Slide s20d — "Git-конвенции — часть контракта с агентом: незаписанное агент не знает" (page 28/57)
**Severity:** P2
**Issue:** Heavy but largely defensible anglicism density (Conventional
Commits/Conventional Branch spec vocabulary, PR template section names
Intent/Changed/Not changed/Validation/Risks/Follow-ups kept verbatim in
English) — these are named external specs, translating them would misname the
actual convention. Lower-severity residual: "auto-changelog, auto-semver" left
untranslated where "автогенерация changelog по типу коммита" would read more
naturally.
**Recommendation:** Optional polish only; not blocking.
**Visual evidence:** 3-card layout (Commit/Branch/PR), gold + teal + navy pill
headers, gold takeaway banner. Clean.

### Slide s20e — "Три паттерна логирования задач — выбор составной, не единственно верный" (page 27/57)
**Severity:** APPROVE-CLEAN
**Issue:** None. 3×3 schema_matrix, confirmed correctly swapped to present
*before* s20d per the documented round-3 QA-fix (task-logging now §3.3d,
presents first) — and the actual render matches this specific documented
intent exactly (unlike the s17b/s18b/s33b/s37b cases below).
**Recommendation:** none.

### Slide s20g — "Секреты — отдельный контракт: .gitignore не значит «агент тоже не прочитает»" (page 29/57)
**Severity:** P1
**Issue:** Highest anglicism density of the 7 new slides: "credentials",
"issue" (bare English noun, should be "проблема"/открытый тикет), "pre-commit
hook (Gitleaks)", "CI-gate", "server-side push-protection", "file-tool",
"OS-level sandboxing", and the RU-suffixed hybrid forms "hook'a" / "hook'ов" —
exactly the anglicism pattern CLAUDE.md's Russification table calls out by
name. The English verbatim quote ("Ignored by git...") is a legitimate
exception; the rest is ordinary vocabulary that should have been translated.
**Recommendation:** "issue" → "тикет"/"проблема"; "credentials" →
"учётные данные"; keep "hook" as a loanword if needed but decline it in RU
("хук", not "hook'a") for consistency with how the rest of the deck handles
borrowed dev terms, or gloss once inline.
**Visual evidence:** page 29 — 2 stacked left cards + 1 tall right card (3-layer
defense), gold takeaway banner. Visual balance and motif are fine; this is a
text-content-only finding.

### Slide s25c — "Локальный тестовый инструментарий кодинг-агента: БД, сеть, CI-цикл" (page 37/57)
**Severity:** P1
**Issue 1 (Schema Readability, compliant):** 3×3 matrix matches the s20e
pattern (dark header pills with icons, ≤4 rows, gold takeaway banner) — passes
the checklist.
**Issue 2 (baseline mandate):** "pytest-generator (Distil Labs) — CPU-only,
≈77% self-reported" gives a percentage with no stated denominator — 77% of
*what* (test-generation accuracy? pass rate? coverage?) is never specified
anywhere in the slide, chapter_ref, or speaker notes excerpt visible on the
slide. This is exactly the "measurable claim without a base" pattern the CLAUDE.md
Baseline/Counterfactual Mandate flags as P1.
**Recommendation:** Add "≈77% [метрика] self-reported" — name the metric
explicitly, or drop the number if it can't be specified.
**Visual evidence:** page 37, bottom-most grey callout row.

### Slide s30b — "Доверие нужно и к тому, из чего сделан сам AI-инструмент" (page 43/57)
**Severity:** APPROVE-CLEAN
**Issue:** None. Baseline present and explicit ("~1 млн разработчиков в релизе
v1.84.0 до патча v1.85.0"), honest epistemic caveat box ("Атака технически
провалилась... это везение, не контроль" — directly satisfies the AI-Failure
& Judgment content rule with a real, non-hedged admission), clean cross-link to
the earlier slopsquatting/CamoLeak content via the "три механически разных
фронта" framing. Gold banner present, motif consistent.
**Recommendation:** none.

### Slide s33b — "Множитель работает в обе стороны одной фазы: быстрый MTTR — и небезопасный IaC по умолчанию" (page 48/57)
**Severity:** P1
**Issue 1 (unglossed acronyms):** "MTTR" and "IaC" are both used as bare
acronyms in the visible title and body and are **never expanded in RU anywhere
in the rendered deck** (checked: these two strings appear only on s33b and
s35b, and never with an inline RU gloss on the visible slide — the one RU
translation of IaC, "инфраструктура-как-код," exists only in the frontmatter
`assertion:` field, which students never see). This is a first-use-acronym
gloss gap.
**Issue 2 (baseline ambiguity):** the two IaC statistics — "~55% secure-by-
default (стабильно 2 года)" and "2026-бенчмарк: 6 frontier-моделей... 8,4%
случаев" — are two *different* measurements (a steady-state adoption rate vs.
a one-off 2026 benchmark pass rate) placed in the same card back-to-back with
no sentence clarifying they are not the same series. A student can easily
misread this as "55% → 8.4%, i.e. got worse," which is not what the data says
(and the deck's own `fact_check_items` note admits this pairing's primary
source isn't pinned down). Contrast this with s38 (triangulation), which does
this correctly — see that slide's note below.
**Recommendation:** Add one clause: "(отдельное измерение, не тот же тренд)"
or similar, and gloss MTTR/IaC on first use.
**Visual evidence:** page 48, gold-left / grey-right two-column comparison,
gold takeaway banner. Visual balance and Ocean palette are otherwise clean.

### Slide s34 — "Доставка — DORA-first: сначала зрелый конвейер, потом масштабировать AI" (page 47/57)
**Severity:** P2
**Issue:** Risk-calibrated gate fix reads correctly (teal-bordered callout:
"необратимое — жёсткий человеческий гейт; мелкое обратимое... AI может
участвовать"). Chart y-axis title "связь с внедрением AI" and chart title "DORA
· у эффекта AI парная цена, %" are grammatically awkward RU phrasing (reads
like a literal/rushed translation of "the AI effect has a paired price").
**Recommendation:** Reword chart title, e.g. "DORA: у эффекта AI есть
оборотная сторона (%)".
**Visual evidence:** page 47, bar chart (+7.5 docs / −7.2 stability), gold and
teal bars, bottom gold banner.

### Slide s37-synthesis-matrix — "Матрица лекции: ведёт практика — вендор-колонки нет вовсе" (page 52/57)
**Severity:** P1
**Issue:** Confirmed word-wrap defect: the row label "Документация" breaks
mid-word with no hyphen across two lines as "Документаци" / "я" — the label
column is too narrow for this word at the current font size. This is exactly
the kind of layout bug a 3rd Generate→Convert→Inspect→Fix iteration should
have caught (visually obvious at 150dpi, let alone on a projector).
**Recommendation:** Widen the phase-label column by a few pt, drop font size
1pt, or abbreviate to "Документ." — verify against the Schema Readability
Checklist's font-size floor before shrinking.
**Visual evidence:** cropped detail at `page 52`, row 8 ("Документация" /
"docs-as-context"). Screenshot on file at
`/tmp/lec04-critic-snap/s37matrix_crop.png` (not persisted in repo).
Everything else on this slide passes the Schema Readability Checklist: 8×4
fill is complete, gold-highlighted 4th column ("Где человек обязателен")
correctly reinforces the course's central human-in-the-loop message, header
contrast is good.

### Slide s37b — "Тот же продукт — два регистра: решает не бренд, а применённая дисциплина" (page 54/57)
**Severity:** P1
**Issue:** "Agentic adoption 32% → 84% за месяц (2,6×)" — full English noun
phrase "Agentic adoption" inline in an RU sentence, untranslated (compare: the
rest of the sentence and the whole rest of the slide is competently
Russified). "life sciences" recurs untranslated here exactly as it did on s09b
(2 of 2 uses of this term in the deck are unglossed English) — worth fixing
consistently in both places, not just one.
**Recommendation:** "внедрение агентных практик" or "доля агентного кода" for
the opening stat; gloss or translate "life sciences" once (e.g. "life sciences
(фарма/биотех)").
**Visual evidence:** page 54, two-column bridge slide (Uber success-with-caveat
left, AWS Kiro dual-register right), honest budget-overrun caveat
("Потолок... введён постфактум — после того как годовой бюджет сгорел за 4
месяца") — good baseline framing, satisfies AI-Failure & Judgment rule well.
Bottom gold banner present.

### Slide s21 — "70%-проблема" / s38 — "Три независимых метода сходятся" (pages 31 and 53/57, context)
**Severity:** APPROVE-CLEAN (both, on the specific GitClear-2026-addition point)
**Issue:** None — positive finding. Both slides correctly label the 2026
GitClear dataset (623М изменений, 2023–26) as a *separate* measurement from
the older 211М-line 2020–24 dataset, with explicit before/after numbers for
each ("рефакторинг 21→3,8%", "дубли 40,3→73,0/млн строк (+81%)" on s21;
consistent figures repeated in abbreviated form on s38). This is the correct
way to juxtapose two datasets without implying a false single trend — contrast
with s33b's MTTR/IaC pairing above, which does not do this.
**Recommendation:** none; cite as the pattern to replicate when fixing s33b.

## Cross-deck issues

### 1. deck.yaml declared slide order vs. actual rendered order (P1, systemic)
Verified by mapping every page of the 57-page PDF to its slide id via exact
`assertion:` text matching (not just filename/id guessing), then cross-checked
against `build_lec04_v4.py`'s own inline comments (which independently confirm
the actual insertion order chosen at build time). Four "b/c"-suffixed slides
declared in `deck.yaml`'s literal `slides:` list (and in `deck-part2.yaml`'s
prose placement notes) to appear **before** a specific numbered slide instead
render **after** it:

| Slide | deck.yaml declares | Actual render (verified) |
|---|---|---|
| s11b | before s11 | **after** s11 |
| s17b | before s18 | **after** s18 (between s18/s19) |
| s18b | right after s18 | **after** s19 (between s19/s20) |
| s25b, s25c | before s25 | **after** s25 |
| s33b | before s34 | **after** s34 |
| s35b | before s35 | **after** s35 |
| s37b | before s38 | **after** s38 |

s09b, s20b–s20g, s30b were checked too and are correctly positioned matching
their declared spot — so this is not a universal failure, but a specific,
repeated pattern affecting most "insert-before" b/c-slides across rounds
1–3, including **3 of the 7 round-3 new slides directly in this review's
scope (s17b, s18b, s33b) plus s37b**.

Spot-checked pedagogical impact (s18b/s19/JIT-retrieval, s33b/s34/DORA-first
framing, s37b/s38): in every case checked, the *actual* render order reads
coherently, in some cases (s18b) more coherently than the declared order would
have (introducing "JIT-retrieval" before it's defined). So this is not
currently a visible-to-students defect. It **is** a documentation-integrity
defect: deck.yaml is this course's stated single source of truth, its own
per-slide `chapter_ref: [for-slide-sNN]` anchors and section-budget arithmetic
assume the declared order, and any future edit, re-render, or
consistency-checker pass that trusts deck.yaml's literal order will get it
wrong.
**Recommendation:** Sync deck.yaml's `slides:` list order (and deck-part2.yaml's
prose placement notes) to match the actual build-script order, rather than the
reverse — the actual order is the one that's been vision-verified as
pedagogically sound.

### 2. Two dead file references in deck-part2.yaml (P1)
- `- id: s39` → `file: slides/s39-checklist.md` — **no such file exists**; the
  real file is `slides/s40-checklist.md`.
- `- id: s40` → `file: slides/s40-bridge-qa.md` — **no such file exists**; the
  real file is `slides/s41-bridge-qa.md`.

Both are leftovers from a historical slide renumbering (the build script's own
comments confirm slides were renumbered at v4.1 while internal Python function
names were not). `total_slides: 57` in deck.yaml's header also doesn't match
the 56 entries actually present in the `slides:` lists across deck.yaml +
deck-part2.yaml (the 57th page exists in the PDF via the orphaned
`s41-bridge-qa.md`, which is not referenced by id anywhere in the YAML
`slides:` list at all).
**Recommendation:** Fix the two `file:` paths, and reconcile the `id: s39` /
`id: s40` labels with the actual on-disk filenames `s40-checklist.md` /
`s41-bridge-qa.md` (or rename the files to match declared ids — either
direction, but they currently disagree). Recount and correct `total_slides`.

### 3. Baseline/Counterfactual Mandate — spot-check across the 7 new slides
5/7 new slides (s09b, s17b, s18b, s20g, s30b) carry explicit before/after or
denominator context for their headline numbers. 2/7 have gaps: s25c's "≈77%
self-reported" (no named metric) and s33b's MTTR/IaC pairing (two datasets
implied as one trend). Both listed above as P1 under their own slides.

### 4. Deep anglicism scan, 7 new slides (P1, aggregate)
Ran `tools/presentation-build/deep_latin_scan.py` against extracted PDF text
for all 7 new-slide pages: 203 raw occurrences, 138 unique tokens outside the
brand allowlist. The large majority are legitimate proper nouns/tool names
that cannot be translated (AWS, Kiro, Gitleaks, TruffleHog, MTTR, IaC, Uber,
Azure Triangle, The Register, Amazon Q Developer, BT Group — company/product/
report names) or verbatim quotes (correctly kept in English per convention).
After excluding those, the residual real anglicisms are concentrated on s09b,
s20g, and s37b specifically (see their per-slide entries above): "failed",
"confidence", "AI-agent deployments", "Agentic adoption", "life sciences"
(×2, unglossed both times), "issue", "credentials", "hook'a"/"hook'ов". This
is a real, if moderate, Russification gap — not at the Лекция 8 "224 unique
anglicisms" scale, but real enough to be P1 per the ENFORCED rule, and
concentrated in exactly the slides a 3rd QA iteration should have caught.

### 5. Ocean palette / gold-highlight / motif consistency
All 13 target slides pass: gold accent appears ≥1× per slide (bottom takeaway
banner is the consistent pattern), rounded-box motif (radius ~12, `#F4F7FA`
surface, teal stroke) is used consistently, no palette deviations spotted, no
timing markers or methodology meta-commentary leaked into visible body or
speaker notes on any of the 13 slides (verified by grep against the ENFORCED
pattern list — the one "методическ" hit found is a false positive, see below).

### 6. No-Timing/No-Methodology grep (13 target + 6 companion files)
Ran the CLAUDE.md-mandated pattern grep across all 13 slide markdown files.
All hits are in frontmatter (`chapter_ref`, `learning_outcomes`,
`visual_brief`) or are false positives from context: `s20e`'s "Длительность
задачи" is a content classification axis (task duration as a criterion in the
task-logging matrix), not a slide-timing marker; `s37-synthesis-matrix.md`'s
one "методическая практика" hit in the speaker notes refers to SDLC
methodology-as-subject-matter ("the leading methodological practice of each
phase" — i.e., spec-driven, TDD, ADR, etc.), not a meta-comment about the
lecture's own pedagogy. Neither is a real violation, but both are close enough
to the banned patterns that a stricter reviewer might still ask for a reword;
flagging as informational, not counted in the P1/P2 total above.

## Overall assessment

No P0s — nothing here is unshowable. But the P1 count (8) plus a systemic,
independently-verified cross-deck consistency defect (declared order/paths
in deck.yaml disagreeing with the actual render, affecting 4 of the 7 new
round-3 slides in scope) means this does not clear the APPROVE-WITH-POLISH
bar per the ENFORCED counter-check ("≥5 P1 → REVISE, not APPROVE-WITH-POLISH").
The visual/layout quality of the 13 slides themselves is generally strong —
Ocean palette, motif, and Visual Mass Balance are consistently well executed,
and several slides (s16, s30b, s21/s38's dataset handling) are genuinely
exemplary — which is consistent with "2 full rebuild+render cycles" catching
most gross visual problems. What a missing 3rd iteration specifically cost:
the word-wrap bug on s37-matrix, the unglossed MTTR/IaC acronyms and the
55%/8.4% ambiguity on s33b, the anglicism residue on s09b/s20g/s37b, and —
most consequentially — the fact that nobody re-diffed deck.yaml's declared
slide order/file paths against what actually got built.

**Recommended before next GATE:**
1. Fix the s37-matrix "Документация" word-wrap (quick, high-confidence fix).
2. Sync deck.yaml + deck-part2.yaml slide order and the two dead `file:`
   paths to match the actual render; correct `total_slides`.
3. Translate/gloss the anglicisms flagged on s09b, s20g, s37b (MTTR/IaC on
   s33b too).
4. Add the missing-metric fix on s25c ("≈77% [what?]") and the
   dataset-disambiguation clause on s33b.

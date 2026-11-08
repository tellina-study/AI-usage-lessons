VERDICT: REVISE

# Methodology Critic Report — Лекция 8 Chapter (8 files, arch-v4) — 2026-10-21

## Severity counts

- **P0: 1** — word-count shortfall against the owner's explicit parity decision (DoD metric fail; this is the category of finding CLAUDE.md treats as "structural gap, not polish," applied here against the lecture-specific 54k–66k bar rather than the generic 30k floor).
- **P1: 7** — see below. Well past the "5+ P1 → REVISE" threshold on its own, independent of the P0 finding.
- **P2: 3** — minor, non-blocking.

**Verdict reasoning (explicit, not soft-pedaled).** The word-count gap alone would already justify REVISE per the DoD-Enforcement rule ("any DoD metric fails → verdict ≥ REVISE"), and the 7 P1 findings below independently justify REVISE per the "5+ P1" rule. I am **not** issuing REJECT: the P0 finding is a volume/structural gap against a lecture-specific bar the chapter already clears 1.54× relative to the generic L4+ floor, not a sign that the material is methodologically unusable — content quality, sequencing, baseline/counterfactual discipline and AI-Failure framing are in fact unusually strong (see "What works" at the end). Treat this report as a revision punch-list for Phase 4, not as a verdict on the writers' competence.

---

## 1. Word count — verified, and worse than a generic shortfall

Re-ran `tools/lecture-production/count_chapter_words.py --parts library/lectures/lec-08`:

```
words_by_part: {1: 10525, 2: 10680, 3: 11272, 4: 9855, 5: 3988}
length_words:  46320
```

Confirmed against the owner's explicit decision (`rework/decisions-owner.md` решение 4: "паритет с Л6/Л7, 54 000–66 000 слов строгим счётом, не порог 30 000"). **46,320 is 7,680 words short of the 54,000 floor**, and 13,680 short of the band's midpoint (60,000). The script's own `курсовая норма 30000: взята (1.54×)` line is true but irrelevant here — the operative bar for this lecture is the owner's higher one, not the generic L4+ floor, and CLAUDE.md's "chapter <30k is a structural gap, not polish" principle applies to the *correct* bar for the lecture in hand, not whichever bar happens to be easiest to clear.

**`chapter-part5b.md` correctly scores 0** — it is pure glossary + bibliography, explicitly excluded from the word quota by course rule, and the script's own warning text makes clear this is expected, not a bug. But this exclusion means **Part 5's real target was never ~8,000 words for narrative content** — the ~8,000 figure in `chapter.md`'s "Карта главы" table silently assumed glossary+bibliography would count toward it. Part 5's *actual* narrative (Раздел 7 "Закрытие" + 15-question Q&A) is 3,988 words against an implied narrative target that should be recalibrated upward, not treated as "close to target because glossary is exempt." **This is the single worst per-part shortfall in the chapter, proportionally** (at minimum −4,012 words short of its originally-stated 8,000-word part target, a 50% miss, once you account for the fact that the target already excluded 5b in spirit even though the table didn't say so explicitly).

### Concrete per-section expansion mandate for Phase 4

Closing every part back to its own originally-stated target (per `chapter.md`'s own "Карта главы" table) sums to +11,680 words, landing the chapter at ≈58,000 — comfortably mid-band. Recommended allocation, with *specific* thin spots named (not "make it longer"):

| Part | File(s) | Current | Target | Gap | Where to add words |
|---|---|---|---|---|---|
| 1 | `chapter.md` | 10,525 | 12,000 | **+1,475** | §1.2 "Порог найма" — add one more concrete named case per asset class (currently generic "клиент не нанимает"); §1.7 "Формы" — expand the bridge to Раздел 5's labor-market preview with one worked numeric example (e.g. one freelancer's before/after rate card) rather than only a forward-reference. |
| 2 | `chapter-part2.md` | 10,680 | 13,000 | **+2,320** | §2's "Стадия редакционного контроля" framing block (before §2.1) — the "Зачем это инженеру" callouts in §2.1/§2.2 gesture at a product-engineering parallel but never work it through with its own numbers; give it one full worked example (e.g. auto-generated product descriptions at a named-type of e-commerce scale) the way CNET gets one. §3.2 "Что работает и что не работает" — currently shorter than its CNET-side twin (§2.2); expand with the inverse case (a predictive panel that *did* catch an AI-disclosure risk, if one exists in the research files, or an explicit "this gap in the literature" paragraph if not). |
| 3 (3+3b) | `chapter-part3.md` + `chapter-part3b.md` | 11,272 | 13,000 | **+1,728** | §4.2 "Классика лицензирования" — the "четвёртый вид материала" (voice/likeness) is named in §4.1 but never given the same numeric treatment (opt-tariff vs retail-tariff, agency negotiation range) that photo and music get two paragraphs later; add a genuine priced sub-case for voice/likeness licensing, cross-referencing Раздел 1's voice cost-collapse numbers so the two sections reinforce each other. |
| 4 (4+4a) | `chapter-part4.md` + `chapter-part4a.md` | 9,855 | 12,000 | **+2,145** | §5.1 "Как строится карьера" — currently has zero named individual humans (see Finding P1-3 below); expanding this with one concretely-named freelancer/illustrator/journalist career trajectory (documented interview, labor-market report profile, or a composite explicitly marked as illustrative per the existing "эта сцена собрана по учебному материалу" convention already used in §2.1/§3.1) closes both this word gap and the missing-named-person gap in one move. |
| 5 (5+5b) | `chapter-part5.md` + `chapter-part5b.md` | 3,988 (+0 exempt) | ~6,000–8,000 narrative | **largest proportional gap** | §7.1–7.3 are each under 500 words; the canon's "заработанное утверждение" closing deserves the same density as a content section's closing, not a compressed coda. Also: several of the 15 Q&A answers (e.g. #6 RIAA, #8 "три-четыре порядка", #14 statutory-vs-settlement) are strong but terse relative to their informational density — each could absorb 150–250 more words without padding, since they're already doing real synthesis work. |

---

## 2. Axis / keystone / lecture-question fidelity

### 2a. "Узнавание" throughline — holds up well

The axis is not diluted into a generic "AI in creative industries" survey. Every section's opening explicitly ties back to "узнавание" as the thing that used to be free and is now fakeable (verified in §2's opening paragraph, §3's opening paragraph, §4.6's "одна строка, которая возвращает раздел к оси", §5's opening "что стало с тем, кто это обычно делал"). This is a genuine strength — the five sections read as one path, not five case studies loosely grouped under a theme.

### 2b. Lecture question — **spoken THREE times, not two (P1)**

Canon (`stroenie-i-povestvovanie.md` §1.2): *"Произносится дважды и больше нигде: последней строкой входа... и в сборке."* Grep confirms the verbatim string **«Лицо, голос и подпись автора стоили доверия бесплатно. Сколько это стоит теперь — и кто платит?»** appears:

1. `chapter.md:113` — in **Введение**, before Раздел 0 ("Вход") even formally begins.
2. `chapter.md:177` — in **§0.3 "Вопрос лекции"**, inside Раздел 0, where the chapter's own text explicitly narrates its count: *"он уже прозвучал во введении — здесь он повторяется во второй и последней раз"*.
3. `chapter-part4a.md:260` — in **§6.3 "Ответ на вопрос лекции — поимённо"**.

The chapter's own narration ("second and last time") is internally consistent with a 2-count model *if you don't count the Введение instance as a formal utterance* — but the canon rule is about the whole document ("и больше нигде"), not about which prose section the author mentally files it under. Three verbatim appearances is three, regardless of how the second one is captioned.

**Fix:** Drop the verbatim blockquote from Введение (keep the forward-reference in flowing prose, unquoted, as foreshadowing — the Введение already has a full paragraph building up to it, so this costs nothing). Keep exactly two verbatim utterances: one at the genuine end of Вход (currently §0.3 is mid-Раздел-0, not the last subsection — §0.7 is; consider moving the one formal utterance to close out §0.7 instead, which is literally "the last line of Вход"), and one in §6.3. This also removes the slightly confusing self-referential "second and last time" line, which currently misdescribes the actual count.

### 2c. Keystone two-row structure — sound

Ряд 1 (CNET: 53% / 40–61% / ~2%) is a genuine measured triple on industry material, matching the "измеренная тройка" requirement (parallel to Lecture 7's 92/74/76). Ряд 2 (deepfake-hiring: KnowBe4/Chapman/Nisos) is a clean transfer-case, one slide, no invented specifics, correctly disclaims the Lecture-14 boundary on the same slide. No duplication found: later recaps of the keystone (§6.2, §6.4, §7.2, Q&A#3, Q&A#7) reuse the *same* cited numbers rather than inventing new specifics — this is legitimate "сборка" recap, not drift.

---

## 3. No Arup duplication — mostly clean, but **bibliographic residue found (P1)**

Grepped `Arup` across all 8 chapter files. **Zero narrative mentions** — confirmed no re-telling of the Arup story anywhere in the actual chapter body (§0.5's Lecture-14 boundary paragraph describes a generic "видеозвонок от «генерального директора»" scenario without naming Arup, which is the correct way to draw the boundary without duplicating content). Good — this is the hard part of the brief, and it's done right.

However, `chapter-part5b.md` (consolidated bibliography) still carries **three Arup-sourced citations with zero in-text use anywhere in the chapter**:

```
chapter-part5b.md:349: IDEMIA (2024). «Анатомия мошенничества Arup на $25,6 млн...»
chapter-part5b.md:396: PRMIA (2024). Разбор кейса Arup — анализ контролов риска.
chapter-part5b.md:402: SCMP (2024). «Arup подтверждена как жертва дипфейк-мошенничества...»
```

These are not cited by any `(IDEMIA, 2024)`-style in-text reference in any of the 8 files — I grepped `IDEMIA|PRMIA|SCMP` across the full narrative body and found zero hits outside this bibliography block. Architecture.md's §7 "долги курса" table is explicit: *"Arup снят из архитектуры Л8 целиком — не только из keystone, но и из всех упоминаний"*. A bibliography entry is still a mention, even an unused one, and it is visible to any reader who opens the sources list (which `tools/presentation-build` and QA tooling will likely grep for exactly this kind of residue). This reads like leftover carry-over from the superseded `research/02-case-candidates-creative-industries.md` (which did analyze Arup as Candidate A before the keystone pivoted to the deepfake-hiring case) that never got cleaned out of the bibliography pass.

**Fix:** Delete the three Arup citations from `chapter-part5b.md`'s Источники list. Trivial, one-file edit.

---

## 4. Refrain-number tally (§6.4 "три-четыре порядка") — methodologically sound

Verified §6.4's arithmetic independently:

- Image: $50–150 → $0.03–0.05 → ×1000–5000 → 3.0–3.7 orders. **In range.**
- Track vs. stock license: $20–100 → $0.015–0.02 → ×1000–6667 → 3.0–3.8 orders. **In range.**
- Voice: $50–450 → $0.04–0.20 → ×250–11250 → 2.4–4.1 orders. **Partial** — lower bound dips to 2.4, honestly flagged as such rather than rounded up.
- License vs. settlement: $20–100 → $0.002–0.005 → ×4000–50000 → 3.6–4.7 orders. **Mostly in range**, upper-bound overshoot named explicitly.
- Getty-UK license-vs-$0: explicitly excluded as "not expressible as an order of magnitude" (division by zero is a real-world zeroing-out, not a ratio).
- Keystone Row 2: explicitly excluded as graph "(б)" — no priced classical-side counterfactual (naming the old actor-hire alternative without a dollar figure for it).

This matches the orchestrator's description of the expected tally precisely and is **methodologically honest** — it names its own denominator-sensitivity (§6.4's "знаменатель счёта зависит от того, как нарезать измерения" paragraph), which is exactly the discipline the canon's §5 "Реестр разборов" demands. No issue here; this is one of the strongest parts of the chapter.

---

## 5. Rule-of-three exception legibility — **numerically fine, bookkeeping stale (P2)**

`decisions-owner.md` решение 3 authorizes **four** detailed breakdowns as an explicit exception: *"CNET (раздел 2) · Coca-Cola/Toys "R" Us (раздел 3) · YouTube thumbnails (раздел 3) · копирайт/Getty-UK (раздел 4)"*. Research wave (`research/03-freshness-october-2026.md` задача 3) subsequently **cut YouTube thumbnails entirely** — the source doesn't exist. §5.3 (Getty bankruptcy) is then given genuine 5-step depth ("Разберём случай по той же форме, что и предыдущие подробные разборы") — this is exactly the architecture's planned substitution (YouTube-thumbnails' authorized "4th slot" effectively transfers to Getty-bankruptcy), and the final count — CNET, Coca-Cola/System1, Getty-UK, Getty-bankruptcy — **still totals exactly 4**, matching the owner's authorization. This is not a silent 5th case; it reads as intentional depth.

What's missing is explicit bookkeeping: `chapter.md`'s index table still calls Getty-UK "**четвёртый разбор** по решению владельца" (a label written when YouTube-thumbnails was still case #3), which is now slightly confusing — a careful reader counting detailed breakdowns in sequence gets to Getty-UK as the *third* named one, not the fourth, until they later discover Getty-bankruptcy is an unlabeled 4th. **Fix (P2, cheap):** one sentence anywhere (e.g., start of §5.3, or the index table's footnote) explicitly stating "the originally-authorized 4th detailed case (YouTube thumbnails) was cut on fact-check grounds; Getty's bankruptcy fills that slot instead, so the chapter still carries exactly 4 detailed breakdowns, not 5."

---

## 6. AI-Failure & Judgment Content ≥30%, holistic — passes by spot-check, **but cannot be rigorously audited (P1, see §9 below)**

Spot-checking strict-in content by section against CLAUDE.md's bucket definition (documented failure+lesson / fundamental-limitation discussion / explicit refusal-criteria / comparison with a better alternative tool):

| Section | Strict-in content found |
|---|---|
| §0 Keystone | CNET (documented failure of editorial disclosure norms + lesson) + deepfake-hiring (documented fraud scheme + "what doesn't work" analysis). **Fully in-bucket.** |
| §1.6 | Sora hype-cycle collapse — documented failure + explicit lesson ("не называть конкретный бренд флагманом"). **In-bucket** (chapter.md's own self-estimate: ~12% of Раздел 1). |
| §2 | CNET full breakdown — documented failure + counterintuitive lesson. **Fully in-bucket** (72% self-estimated for Part 2 combined with §3). |
| §3 | Coca-Cola/Toys R Us + System1 contrast — documented failure of predictive testing to catch a real risk class + explicit lesson (add one question to the questionnaire). **In-bucket.** |
| §4.3 | Adobe Firefly named explicitly as "a more correct alternative tool" to the Stability/Suno/Udio train-first-license-later approach — satisfies "сравнение с более правильным альтернативным инструментом" directly. **In-bucket.** |
| §4.1–4.5 (rest) | Mostly legal-status reporting, not failure/limitation framing per se — **out-of-bucket** by the strict-in rule (legal uncertainty ≠ AI failure). |
| §5.3 | Getty bankruptcy — documented failure of a defensive strategy + explicit lesson about plan-must-survive-its-own-timeline. **In-bucket.** |
| §6.1 | Four explicit refusal criteria, each tied to a specific earlier finding. **In-bucket** by definition (explicit "здесь ИИ не нужен" criteria). |

This spread is **six of eight content sections** (0, 1, 2, 3, 4, 5/6), which is *more* distributed than architecture.md's own estimate (~50% across "4 of 8 sections"), and is not concentrated in a single artifact-section — satisfies the holistic requirement as planned. I did not do a full word-by-word strict-in tabulation (at 46k words this would take a dedicated pass), but the spot-check is consistent with a ≥30% estimate and no single-cluster concentration. **This is a pass, conditional on the metadata gap in Finding 9 being fixed so a future pass can verify it mechanically rather than by spot-check.**

---

## 7. Baseline/Counterfactual Mandate — spot-checked 10 claims, all pass

| # | Claim | Base/counterfactual present? |
|---|---|---|
| 1 | CNET 53% (41/77) | ✓ vs. 40–61% baseline error rate / ~2% correction rate |
| 2 | Coca-Cola CARMA sentiment swing | ✓ vs. System1 5.9★ contrast (gap in platform/N honestly flagged) |
| 3 | Getty v Stability theoretical license | ✓ $30.75M/$1.6B calc vs. actual $0 vs. News Corp $250M/5yr market comp |
| 4 | Upwork AI-skill growth | ✓ vs. BLS −2%/10yr (explicitly flagged as non-comparable methodology, not hidden) |
| 5 | Getty subscribers 321k→240k | ✓ self-contained before/after |
| 6 | Deepfake-hiring $120/70min | **Partial** — no priced classical-side counterfactual (old method = hire a live actor, no $ given); honestly labeled graph "(б)" rather than forced into a ratio |
| 7 | Udio settlement $0.002–0.005 | ✓ vs. $20–100 stock license |
| 8 | $150k/work statutory cap × 61,026 | ✓ explicitly labeled theoretical ceiling, not a real award |
| 9 | Image cost-collapse | ✓ $50–150 vs. $0.03–0.05 |
| 10 | Checkr 31%→40% YoY | ✓ self-contained before/after |

This is unusually disciplined — every gap in a pair is *named as a gap* (graph (а)/(б)/(в) distinctions used correctly throughout) rather than smoothed over. No P1/P2 findings here; this is a model instance of the mandate.

---

## 8. Cross-part consistency — **two concrete, fixable drifts found (P1 ×2)**

### 8a. "Карта главы и индекс частей" table lists 5 files, actual layout is 8

`chapter.md`'s own index table (lines 39–45) lists exactly 5 parts/files. The actual repository has 8: `chapter.md`, `chapter-part2.md`, `chapter-part3.md`, `chapter-part3b.md`, `chapter-part4.md`, `chapter-part4a.md`, `chapter-part5.md`, `chapter-part5b.md`. The 3b/4a/5b splits happened because of the 600-line-per-file cap (confirmed — each of those files' own headers correctly cross-link to their parent part), but the top-level index in Part 1 was never updated to reflect this. A reader relying on `chapter.md`'s own map (the first thing anyone reads) will not find `chapter-part3b.md`/`4a.md`/`5b.md` listed anywhere in it.

**Fix:** Expand the table to 8 rows (or keep 5 "logical parts" but add a visible note that parts 3/4/5 are each split across two physical files, with both filenames given).

### 8b. `slide_map` frontmatter is stale against the actual `[for-slide-sNN]` markers

`chapter.md`'s frontmatter declares:

```
"2": "s20-s30 — Редакционный контроль"
"3": "s31-s41 — Релиз и приём аудиторией"
"4": "s42-s53 — Права и лицензирование"
"5": "s54-s64 — Кадровый рынок отрасли"
"6": "s65-s75 — Сборка"
"7": "s76-s78 — Закрытие"
```

Grepping actual `[for-slide-sNN]` markers used in the body gives:

```
Раздел 2: s20–s28     (declared s20–s30 — OK, within range)
Раздел 3: s31–s39     (declared s31–s41 — OK, within range)
Раздел 4: s41–s51     (declared s42–s53 — starts 1 early, already overlapping Раздел 3's declared ceiling)
Раздел 5: s52–s61     (declared s54–s64 — starts 2 early)
Раздел 6: s62–s72     (declared s65–s75 — starts 3 early, ends 3 early)
Раздел 7: s73–s75     (declared s76–s78 — entirely offset by 3)
```

The sequence itself is sound (continuous, strictly increasing, no duplicates or overlaps — Check #9 from the brief **passes** on that narrower question). But the **plan vs. reality gap grows monotonically from Раздел 4 onward**, reaching a 3-slide offset by Раздел 7. This is exactly the kind of drift the brief asked me to hunt for: Part 1's frontmatter was written against architecture.md's *pre-writing* slide-budget estimate, and the four parallel writers who actually placed `[for-slide-sNN]` tags in Parts 2–5 used fewer slides per section than Part 1's author projected, and nobody reconciled the frontmatter afterward.

**Why this matters beyond tidiness:** this `slide_map` is the artifact Phase 5 (slide-building) will likely read first to scope each slide batch. If it's trusted as-is, the deck-builder will expect ~11 slides for Раздел 6 content that the chapter itself marks with only 11 anchor points starting 3 slots earlier than declared — low risk of real damage (since slides are derived from the `[for-slide]` markers directly, not from the summary table), but it is misleading documentation that should be corrected before Phase 4 closes, not carried into Phase 5 to cause confusion there.

**Fix:** Regenerate the `slide_map` frontmatter field directly from the actual markers (`s20-s28`, `s31-s39`, `s41-s51`, `s52-s61`, `s62-s72`, `s73-s75`) rather than leaving the pre-writing estimate in place.

---

## 9. Missing YAML frontmatter in 6 of 8 files (P1)

`chapter.md` and `chapter-part2.md` both carry full YAML frontmatter (`length_words`, `strict_in_self_estimate`, `references_count`, `learning_outcomes`, etc.). **`chapter-part3.md`, `chapter-part3b.md`, `chapter-part4.md`, `chapter-part4a.md`, `chapter-part5.md`, and `chapter-part5b.md` have no YAML frontmatter at all** — they open directly with `## Оглавление (Часть N)`. This is visible evidence of the "5 parallel agents... did not see each other's output" risk materializing: the Part-2 writer followed the metadata convention Part-1 established; the Part-3/4/5 writers (presumably different sessions) did not.

Concretely, this means:
- No `strict_in_self_estimate` for 6 of 8 files — the holistic AI-Failure audit in Finding 6 above had to be done by manual spot-check instead of cross-checking declared estimates, for three of the five content-bearing parts.
- No `references_count` for 6 of 8 files — can't mechanically verify the final bibliography's completeness against each part's own claimed source count.
- No `learning_outcomes` tag for 6 of 8 files — LO coverage had to be verified by reading content rather than cross-checking frontmatter claims.

**Fix:** Add the same frontmatter block (minus `title`/`axis`/`refrain`, which only need to live once in Part 1) to the six files missing it, back-filling `length_words` (already known from the word-count script output: 6481/4791/4846/5009/3988/0) and a `strict_in_self_estimate` for each.

---

## 10. Named-individual-per-section canon requirement — missing in 5 of 6 content sections (P1)

`stroenie-i-povestvovanie.md` §3 states explicitly: *"Порог: в каждом разделе — хотя бы один названный человек, с которым происходит то, о чём раздел. Не «пациенты» и не «врачи», а один, у которого есть ситуация и исход."* This was the single most expensive finding against Lecture 7 ("человек в них один, восьмым разделом из девяти").

Checked all five content sections of this chapter plus Раздел 0:

- **Раздел 0 (keystone):** ✓ — "Kyle" (KnowBe4 fake hire) and Christina Chapman both have a named situation and a documented outcome (caught by EDR days later; sentenced to 102 months).
- **Раздел 1 (Продакшн):** ✗ — "дизайнер", "фрилансер", "композитор", "диктор" are all generic role-fillers; no single named individual with a traceable situation.
- **Раздел 2 (Редакционный контроль):** ✗ — CNET's writers are never named (the point is precisely their anonymity behind "CNET Money Staff", which is thematically apt but still leaves the section without the required named person); Sports Illustrated's named executives (Ross Levinsohn etc.) appear only in Part 5's Q&A recap, not within §2.4 itself.
- **Раздел 3 (Релиз и приём аудиторией):** ✗ — Coca-Cola/Toys R Us are companies; no named creative director, marketer, or audience member.
- **Раздел 4 (Права и лицензирование):** ✗ — entities are companies and courts by design (this is the section where it's hardest to find a human), but the chapter itself gestures at "тысячи отдельных фотографов" affected by the Getty bankruptcy (§5.3, not §4) without naming one.
- **Раздел 5 (Кадровый рынок):** ✗ — same gap, most acute here since this section is literally *about* individual careers and names zero individuals.

**Why P1, not P2:** this is an ENFORCED canon item with a documented cost precedent (Lecture 7's near-identical gap was flagged as a top finding), not a stylistic nicety. **Fix:** this dovetails with the word-count mandate in §1 above — Раздел 5 in particular (§5.1) is both the thinnest section by word-target-gap and the one most naturally suited to carry a named individual (a documented freelancer/illustrator/journalist career profile, sourced from one of the already-cited labor-market reports or a clearly-marked composite scene in the same convention already used for §2.1/§3.1's "эта сцена собрана по учебному материалу" disclaimers). Recommend adding one named person to Раздел 5 as the highest-priority fix, with Разделы 1–3 as secondary (lower cost-of-omission since those sections already have strong institutional-level detail).

---

## 11. Missing per-section audience question — present in only 2 of 6 content sections (P1)

Canon §3: *"Один подготовленный вопрос залу на раздел... выписывается в план дословно."* Grepped `Вопрос залу` across all 8 files: it appears in **§0.6** (Раздел 0, correctly formatted with a channel instruction — "задаётся в чат односложно") and in **§4.5** (Раздел 4, "Вопрос залу. У кого на работе уже используется AI-генерация..."). **Разделы 1, 2, 3, and 5 have no audience question at all** — no disguised version under another heading either (checked for "у кого", "спросите", "в чат" as alternate phrasings; none found outside the two sections above and generic prose uses of "у кого" that aren't addressed to an audience).

This is the exact anti-pattern the canon names as costing Lecture 6 a 73-minute monologue (*"четыре попытки спросить зал кончились тем, что лектор ответил сам себе"*) — the risk is structural (no question prepared = none asked live), not merely a documentation nicety. Given this course's audience profile (practicing engineers, "все вайбкодят"), Разделы 1, 3, and 5 in particular have obvious candidate questions already implicit in the text (e.g. Раздел 1: *"у кого в работе уже есть порог найма, который обвал цены генерации обнулил — замечали вы это сами?"*; Раздел 3: *"кто уже видел внутри своей компании расхождение между контролируемым тестом и открытой реакцией пользователей — не обязательно про рекламу"*).

**Fix:** Add one verbatim, channel-specified audience question to each of Разделы 1, 2, 3, and 5, in the same format as §0.6 and §4.5 already use.

---

## 12. LO coverage — verified correct

Cross-checked against `catalog/manifests/lectures.yaml` (`number: 8`, `learning_outcomes: [LO1, LO2, LO4, LO5]`). Matches the chapter's own "Учебные цели" section exactly, including the explicit, correctly-reasoned note on why LO3 is absent (it belongs to a different lecture in the manifest, not a gap). All four listed LOs have identifiable, substantial content: LO1 (task×modality grid references throughout §1/§1.7, explicit cell assignments), LO2 (the 4-step disclosure form, applied consistently across all detailed breakdowns), LO4 (the axis itself, carried from Введение through §7.3), LO5 (§6.1's four explicit refusal criteria, each tied to a specific earlier finding). **No finding here — this check passes cleanly.**

---

## 13. Slide-marker continuity — passes on the narrow question, see §8b for the related frontmatter issue

All `[for-slide-sNN]` markers across the 8 files form one continuous, strictly-increasing, non-overlapping sequence from s01 to s75 with no duplicates and no backward jumps (verified by sorting the full extracted list). This specific check (brief item #9, read narrowly as "do the markers themselves form a valid sequence") **passes**. The related but distinct problem — that the chapter's own *frontmatter* mis-describes where each section's markers actually fall — is Finding 8b above (P1), which is a documentation-accuracy issue, not a marker-sequence defect.

---

## What works (do not lose this in revision)

Calling this out explicitly so Phase 4 revision doesn't accidentally regress it while chasing the word count: the 5-step breakdown form (price-of-error → both classical regimes in the same unit, with honest (а)/(б)/(в) grading → model-vs-regime-not-vs-zero → device → what-moved) is applied **consistently and honestly** across all four detailed cases, including two genuinely contrarian findings (CNET: AI is not less accurate than classical journalism, the institution just reacts differently to disclosure; Getty v Stability UK: the AI company won, not the rightsholder) that the chapter does not flatten into a simpler, more "satisfying" narrative. The baseline/counterfactual discipline (§7 above) is the best-executed instance of this mandate I've reviewed in this course's lecture set. The self-correction on Getty+Shutterstock (explicitly narrating that the May-2026 research called it "defensive consolidation" and the October research found it was a failed defense followed by bankruptcy) is exactly the kind of intellectual honesty the course's mission statement asks for, and it is foregrounded rather than buried.

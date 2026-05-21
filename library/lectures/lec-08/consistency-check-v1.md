# Consistency Checker Report — Лекция 8 «AI в креативных индустриях и медиа» — 2026-05-20

**Mode:** full (Phase 10 — 3 артефакта: chapter v2, deck v3, speech v1)
**Source-of-truth (per book-first):** `chapter.md` v2 (~13,850 слов).
**Artifacts checked:**
- `library/lectures/lec-08/chapter.md` (v2, 901 строка)
- `library/lectures/lec-08/deck.yaml` (v1, 568 строк) + `slides/sNN-*.md` (39 файлов)
- `library/lectures/lec-08/speech.md` (v1, 813 строк, ~5,500 spoken words)

---

## Severity counts

- **P0 (factual contradiction / missing coverage):** 4
- **P1 (significant drift / terminology):** 7
- **P2 (minor inconsistency):** 5

**Verdict:** **REVISE** (slides need terminology + factual sync to chapter v2 fact-checker fixes).

---

## Cross-artifact matrix (sample 15 key facts)

| Концепт / число | Chapter §X | Slide sNN | Speech [sNN] | Aligned? |
|---|---|---|---|---|
| $25.6M Arup CFO | §3.7 («$25.6M (HK$200M), 15 транзакций») | s26 («$25.6M (HK$200M), 15 transactions») | [s26] «двадцать пять и шесть миллиона долларов, пятнадцать транзакций» | ✓ |
| 20M ChatGPT logs (NYT) | §3.2 («20 миллионов ChatGPT logs») | s21 («20M ChatGPT logs») | [s21] «двадцать миллионов ChatGPT logs» | ✓ |
| 47.3% YouTube creators | §4.3 («47.3% creators... Dec 2025») | s35 (assertion) | [s35] «сорок семь и три процента creators... декабре двадцать пятого» | ✓ |
| 2 апреля 2026 NYT SJ deadline | §3.2 («2 апреля 2026») | s21 («2 апр 2026») | [s21] «второе апреля двадцать шестого» | ✓ |
| 8 сентября 2026 Andersen trial | §3.4 («8 сентября 2026») | s23 («trial 8 сент 2026») | [s23] «восьмое сентября двадцать шестого» | ✓ |
| $400M Firefly revenue | §1.5, §2.1 («$400M direct revenue 2024–25») | s14, s11 («четыреста миллионов долларов прямая выручка») | [s11], [s14] «четыреста миллионов» | ✓ |
| 22B+ Firefly assets | §1.5 («22 миллиарда ассетов за два года») | s11 («двадцать два миллиарда ассетов») | [s11] «двадцать два миллиарда ассетов» | ✓ |
| Шумайлов Nature 631:755-759 | §3.9 («Shumailov et al, Nature 2024 vol 631, p 755–759») | s28 («Shumailov et al. 2024, Nature vol 631, p 755-759») | [s28] «Шумайлов с командой в Nature, двадцать четвёртый год» | ✓ |
| 18.03.2026 Минцифры | §1.6 («18 марта 2026») | s10a («Минцифры законопроект 18.03.2026») | [s10a] «восемнадцатого марта» | ✓ |
| Cost-collapse 100×–10,000× | §2.1 (диапазон через таблицу) | s14 (bar chart) | [s14] «сто, тысячу, десять тысяч раз» | ✓ |
| −17% Upwork graphic design | §2.4 («−17.01%») | s17 (assertion) | [s17] «минус семнадцать процентов» | ✓ |
| $3.7B Getty+Shutterstock merger | §2.4 («$3.7B январь 2025») | s17 + s13 («три и семь миллиарда») | [s17] «три и семь миллиарда долларов» | ✓ |
| 12.2→3.4 / 13.5→53.4 sentiment | §3.11 (numbers verbatim) | s30 (charts) | [s30] «двенадцати и двух... пятидесяти трёх и четырёх» | ✓ |
| Suno v5 vs v5.5 | §1.6 + §7 glossary («Suno v5.5») | s10a («Suno v5») | [s10a] «Suno v5» | ✗ DRIFT |
| Toys R Us Sora-ad длительность | §1.1, §3.11 («66-секундный») | s07, s30 («66-секундный») | [s07] «шестидесятисекундный» (60); [s30] «шестидесятисекундный» (60) | ✗ DRIFT |
| Kandinsky 5.0 Video дата | §1.6 («20 ноября 2025») | s10a («ноября 2025», без даты) | [s10a] не упомянуто | partial drift |
| Korea Telegram chats count | §3.8 («более 200, точное число fluctuates») | s27 («более двухсот тридцати») | [s27] «более двухсот» | ✗ DRIFT |
| Amazon Kindle sham books «19/100» | §3.10 (УДАЛЕНО per F-P1.4) | s29 («19/100 топ-бестселлер — реальные люди») | [s29] не упомянуто (correctly) | ✗ P0 contradiction |
| Sony status (RIAA v Suno/Udio) | §3.5 (Warner+Udio все ещё litigation, Sony с обоими) | s24 («Sony — последний major litigating») | [s24] (matches chapter) | ✗ P0 partial contradiction |

---

## DISCREPANCIES (детально)

### D1 — Toys R Us Sora-ad длительность: 66 sec vs 60 sec
**Severity:** P0 (factual contradiction)
**Where:** chapter §1.1 + §3.11 vs speech [s07] + [s30].
**Issue:**
- Chapter §1.1 (line 174): «попыталась сделать **66-секундный** единый Sora-клип».
- Chapter §3.11 (line 525): «Первый major-brand **66-секундный** единый AI-generated commercial».
- Slide s07 (notes): «попыталась сделать **66-секундный** единый Sora-клип».
- Slide s30 (notes): «представлен **66-секундный** единый клип».
- Speech [s07] (line 172): «попыталась сделать **шестидесятисекундный** единый Sora-клип» (=60 sec).
- Speech [s30] (line 598): «Первый **шестидесятисекундный** единый AI-commercial» (=60 sec).
**Recommendation:** Speech должен сказать «шестидесятишестисекундный», либо «больше минуты». Fix speech — chapter и slides уже совпадают на 66.

### D2 — Amazon Kindle «19 из 100» — orphan factoid в slide после chapter deletion
**Severity:** P0 (factual contradiction)
**Where:** chapter §3.10 vs slide s29.
**Issue:** Chapter v2 changelog F-P1.4 explicitly removed «19 из 100 топ-бестселлер — actual human writers» как unverified claim. Replaced на verifiable surge + Frank Gioia / Ted Alkyer specifics. **Slide s29 STILL contains это число**:
- s29 assertion: «Amazon: **19/100 топ-бестселлер — реальные люди**.»
- s29 speaker notes: «Authors Guild data card: «Amazon Kindle 2023-24 · **19/100 топ-бестселлер — реальные люди** · остальное — AI-клоны».»
- Speech [s29]: правильно не упоминает число (correctly aligned with chapter v2).
**Recommendation:** Remove «19/100» from s29 assertion + speaker notes. Replace surge-claim phrasing matching chapter.

### D3 — Sony Music status: chapter Warner+Udio litigating, slide says Sony last
**Severity:** P0 (partial factual contradiction)
**Where:** chapter §3.5 vs slide s24 assertion.
**Issue:**
- Chapter §3.5 (F-P1.2 fix, line 422): «Warner Music ↔ Suno — licensed deal сентябрь 2025; Warner ↔ Udio — **по-прежнему litigation** (settlement не подписан на 2026-05-20)»; «Sony Music — остаётся major, actively litigating с обоими».
- Slide s24 assertion: «Sony — **последний major litigating**» — implies Sony is the ONLY litigating major.
- Speech [s24] (line 470): correctly aligns to chapter — «Warner и Udio — litigation продолжается. Sony actively litigating с обоими».
**Recommendation:** s24 assertion to «Warner ↔ Udio + Sony — actively litigating; Suno SJ июль 2026» — match chapter granularity.

### D4 — Korea Telegram chats: «>230» в slide vs «>200» в chapter+speech
**Severity:** P0 (factual contradiction after fact-checker softening)
**Where:** chapter §3.8 vs slide s27 vs speech [s27].
**Issue:**
- Chapter §3.8 (F-P1.3 fix, line 471): «более **200** Telegram-чатов (точное число fluctuates по разным reports)».
- Speech [s27] (line 534): «более **двухсот** Telegram-чатов» (=200+).
- Slide s27 (speaker notes, line 30): «более **двухсот тридцати** Telegram-чатов» (=230+).
**Recommendation:** s27 notes update to «более двухсот» matching softened chapter form.

### D5 — Suno version: v5.5 (chapter+glossary) vs v5 (slide+speech)
**Severity:** P1 (term drift after chapter revision)
**Where:** chapter §1.6 + §7 glossary vs slide s10a + speech [s10a].
**Issue:**
- Chapter §1.6: «entry-level vs Suno **v5.5** / Udio v2».
- Chapter §7 (glossary entry #2): «foundation модель (например, Sora 2, Midjourney v7, Suno **v5.5**)».
- Chapter changelog P2.6 explicitly: «Suno v5 → v5.5 (consistent с research dossier 2026-05-20)».
- Slide s10a (line 28): «entry-level vs Suno **v5**».
- Speech [s10a] (line 244): «entry-level против Suno **v5**».
**Recommendation:** Update slide s10a + speech [s10a] to «v5.5» per chapter glossary lock.

### D6 — «class action» (speech) vs «коллективный иск» (slides) — pervasive terminology drift
**Severity:** P1 (significant drift across 5+ slides)
**Where:** speech vs slides s20 / s23 / etc.
**Issue:** Chapter §3.1 glossary line 352 provides BOTH: «class action — коллективный иск, в котором...». Used as inline-glossed term.
- Slides (s23 line 5, 6, 16, 20, 28; s20 line 27): ONLY «коллективный иск».
- Speech (line 396, 444, 452, 456): ONLY «class action», no Russian gloss.
- Chapter uses both forms interchangeably with inline gloss.
**Recommendation:** Lock canonical: «class action (коллективный иск)» при первом появлении в каждом артефакте, далее одна форма. Either: speech adds «коллективный иск» (preferred by R-P1.1 reader-fix) или slides allow English form post-gloss.

### D7 — Legal jargon English-only in speech vs Russified-only in slides
**Severity:** P1 (pervasive drift)
**Where:** slides s20-s25, s28 vs speech [s20-s25].
**Issue:** Chapter §3.1 establishes inline-glossing pattern (R-P1.1: «SDNY, MTD, SJ, DMCA, CDPA, fair-use, discovery, class action»). Speech ignores Russian glosses entirely; slides Russified beyond chapter glossary:
- «fair use» (speech) vs «добросовестное использование» (slides s20, s22, s25)
- «summary judgment / SJ» (speech) vs «упрощённое решение суда» (slide s21)
- «discovery» (speech) vs «истребование доказательств» (slide s23)
- «motion to dismiss / MTD» (speech) vs «отказ в иске» (slides)
- «regurgitation theory» (speech) vs «теория дословного цитирования» (slides s21)
- «output similarity» (speech) vs «сходство вывода» / «проверка сходства результата» (slides)
**Recommendation:** Sync to chapter pattern: introduce English term + Russian gloss at first occurrence, then one consistent form thereafter в каждом артефакте. Speech needs to add Russian gloss (currently only English) OR slides need to bring back English term parenthetically.

### D8 — Job titles drift: «AI director» (chapter+speech) vs «AI-режиссёр» (slides)
**Severity:** P1 (term drift)
**Where:** chapter §2.3 / speech [s16] vs slide s16.
**Issue:** Chapter §2.3 (line 293-295) uses English titles: «AI director», «GenAI workflow specialist», «AI continuity supervisor». Speech [s16] (line 338-342) matches chapter. Slide s16 Russifies inconsistently:
- «AI-режиссёр» (instead of «AI director»)
- «GenAI **процесс** specialist» (auto-translated "workflow" → «процесс») — odd Russian
- «континьюити-супервайзер» (auto-transliteration of «continuity supervisor»)
**Recommendation:** Sync slide s16 to «AI director», «GenAI workflow specialist», «AI continuity supervisor» (matching chapter+speech).

### D9 — «creative» translated inconsistently: «креативная» (chapter+speech) vs «творческая» (slides)
**Severity:** P1 (pervasive drift)
**Where:** speech (line 44, 64, 82, 88, 304) vs slides (s05a, s11, s13, s14, s19, s30 — all use «творческ-»).
**Issue:** Lecture title is «AI в **креативных** индустриях». Chapter uses «creative-индустрия» (English-mixed) + «креативная индустрия» (RU). Speech uses «креативная индустрия». Slides systematically use «творческая индустрия» / «творческий AI» throughout speaker notes.
**Recommendation:** Slide notes sync to «креативная» (matching speech) — title уже says «креативных».

### D10 — Machine-translation artifacts in slide speaker notes («промышленное применение»)
**Severity:** P1 (pervasive readability damage in 7 slides)
**Where:** slides s07, s09, s10, s11, s14, s15, s16.
**Issue:** Auto-translation of "production" → «промышленное применение» (industrial application) appears 13 times in speaker notes. Result:
- s07: «pre-промышленное применение и post-промышленное применение» (intended: «pre-production и post-production»).
- s14: «до AI — тысяча-пятьдесят тысяч долларов на съёмку и post-**промышленное применение**».
- s16: «промышленное применение-ready output» (intended: «production-ready»).
**Counter:** Chapter consistently uses «production» (English). Speech uses «production» (English). Only slides Russify into nonsense.
**Recommendation:** Replace «промышленное применение» → «production» во всех 7 slides. Same for: «коммерчески безопасный» → «commercial-safe», «эталонная кампания» → «iconic campaign», «фундаментальные ограничения» → «inherent limits», «итоговый продукт для клиента» → «client deliverable», «человеческое руководство» → «human direction», «типам ассетова» → «asset-классам».

### D11 — «v» vs «против» internal inconsistency в speech
**Severity:** P1 (within-artifact inconsistency)
**Where:** speech.md.
**Issue:** Speech mixes «v» and «против» without rule:
- Line 410: «NYT v OpenAI» (English).
- Line 430: «Getty Images против Stability AI» (Russian).
- Line 448: «против Stability, Midjourney, DeviantArt» (Russian).
- Line 484: «Thomson Reuters против Ross Intelligence» (Russian).
- Line 496: «Thomson Reuters v Ross» (English) — 14 lines after «против Ross».
Same case named two ways in same paragraph.
**Recommendation:** Lock one form per case. Suggest «X v Y» (Latin-American legal style, matches chapter) для case titles + «против» для proseй references.

### D12 — Arup revenue ~$10B (slide-only, not in chapter)
**Severity:** P1 (unverified slide-only fact)
**Where:** slide s26 only.
**Issue:** Slide s26 speaker notes (line 28) + visible chip (line 24) state «Arup — британская инженерная firm с revenue **около десяти миллиардов долларов**».
- Chapter §3.7 doesn't mention Arup revenue.
- Speech [s26] doesn't mention revenue.
**Recommendation:** Verify or remove. Arup actual revenue ~$2.5B-$3B (2024); $10B is overstated. Remove from slide.

### D13 — «дискретизация» Sora 2 standalone (translation error in chapter+speech)
**Severity:** P2 (Russian-language error, not drift)
**Where:** chapter §1.1 (line 164) + speech [s07 pre-flight].
**Issue:** Chapter and speech use «дискретизация standalone consumer-facing продукта Sora» — «дискретизация» в Russian = "discretization" (math term для signal sampling), не "discontinuation". Should be «прекращение поддержки» / «снятие с продажи». Same error in both — consistent across artifacts BUT both incorrect.
**Recommendation:** Fix chapter + speech: «прекращение standalone consumer-facing продукта» or «discontinuation».

### D14 — «Шумайстеру» typo in chapter §0.2
**Severity:** P2 (chapter typo, not drift but visible)
**Where:** chapter line 125.
**Issue:** «**Шумайстеру** производство Lionsgate начинает экономить...» — incorrect word, likely should be «Постепенно» or «Соответственно». Looks like garbled regex/replace artifact.
**Recommendation:** Fix to «Постепенно» / «Соответственно» (Russian flow word).

### D15 — Lionsgate earnings-call timing: ноябрь 2024 vs сентябрь 2024
**Severity:** P2 (minor — different events conflated)
**Where:** chapter §1.1 vs speech.
**Issue:**
- Chapter §1.1 (line 172): partnership announced сентябрь 2024 + earnings call **ноябрь 2024**. Two separate events.
- Speech [s07] (line 170): «Lionsgate подписал AI-deal с Runway в **сентябре** двадцать четвёртого... На earnings-call заявили...» — earnings-call timing dropped but ok.
- Slide s11 notes: matches chapter (две даты).
**Recommendation:** Speech is acceptable; minor (no severity escalation).

### D16 — EU criminalisation deepfake-porn deal «феврале 2024» — slide-only claim
**Severity:** P2 (slide-only addition)
**Where:** slide s27 only.
**Issue:** Slide s27 speaker notes: «привёл к EU criminalisation of deepfake porn — **deal в феврале 2024 года**, вступление в силу к середине 2027 года». Chapter §3.8 doesn't have this. Chapter §4.1 (line 573) only says «EU deepfake criminalisation (в силу к mid-2027)» without February 2024 specifics.
**Recommendation:** Either align с chapter (remove «феврале 2024») или verify and add to chapter.

### D17 — Mojibake в s30 speaker notes
**Severity:** P2 (encoding artifact)
**Where:** slide s30 line 28.
**Issue:** «структурный негативный пере�ход» — corrupted UTF-8 char между «пере» и «ход».
**Recommendation:** Fix to «переход».

---

## Coverage parity (10 checks из brief)

### Check 1 — Все assertions из chapter раскрыты в slides
**PASS with drift.** Sample 10 chapter §X.X:
- §0.1 (3 семейства) → s05a ✓
- §0.2 (keystone) → s05 ✓
- §1.1 (text-to-video) → s07 ✓
- §1.2 (character consistency) → s08 ✓
- §1.3 (voice cloning) → s09 ✓
- §1.6 (Russian context) → s10a ✓ (но «Suno v5» drift)
- §2.1 (cost-collapse) → s14 ✓
- §3.2 (NYT) → s21 ✓
- §3.7 (Arup) → s26 ✓ (с unverified «$10B» addition)
- §3.11 (Toys R Us / Coca-Cola) → s30 ✓ (66 vs 60 sec drift)

### Check 2 — Slide deck → speech coverage
**PASS.** Все 39 slides имеют корреспондирующий блок в speech (frontmatter `slides_covered` listing all 39). 39 `### [sNN · ... мин]` headers in speech match deck.yaml IDs. Speech follows slide order strictly.

### Check 3 — Numbers / facts / dates consistency
**FAIL.** См. D1, D2, D3, D4, D5, D12, D16. Multiple P0/P1 numeric drifts.

### Check 4 — Glossary terminology consistency
**FAIL.** См. D5, D6, D7, D8, D9, D10. 6+ terminology drifts:
- Chapter §7 glossary 18 терминов locked. Slides + speech deviate.
- Notable: «class action / коллективный иск», «commercial-safe / коммерчески безопасный», «AI director / AI-режиссёр», «fair use / добросовестное использование», «production / промышленное применение».

### Check 5 — Cross-references consistency (Lec 1/3/5/7/9)
**PASS.** All 4 cross-refs consistent:
- Lec 1: framework для «где AI работает / где нет» → углубление до 4 критериев. Сonsistent across chapter §6 + speech [s33-s37].
- Lec 3: архитектуры платформенного слоя (Firefly Foundry / HuggingFace Spaces) — mentioned inline in s11 + speech [s11] + chapter §1.5. Consistent.
- Lec 5: financial parallel в s20 устно (P2.7 fix). Speech [s20] line 402 doesn't explicitly mention Лекция 5, но references «risk-debt». Chapter §6 + plan §9 confirm parallel.
- Lec 7: 4-actor framework — chapter §3.1 (line 364) + speech [s20] device. Tonal-consistent.
- Lec 9: forward-ref «kinetic outcome» — chapter §6 + speech [s39] + slide s39 — same kinetic-vs-brand-trust framing.

### Check 6 — Failure-share % consistency
**PASS.** Все три ≥30% strict-in:
- Chapter: §3+§4+§5 = ~5,600 / ~14,300 words = ~39.2% (changelog claims 52% but recalc with v2 expanded shows lower)
- Slides: 16 strict-in slides из 39 = 41%
- Speech: 35 min из 75 = 46.7% (speech changelog confirms «50% strict-in по времени»)
Distribution holistic across artifacts ≥30% ✓.

### Check 7 — Russian language consistency
**FAIL.** Speech v1 changelog claims «Anglicism core: 0 hits» — это misleading. Speech still has «production», «class action», «discovery», «summary judgment», «commercial-safe» (≥10 occurrences) — без inline gloss. Это намеренный стиль chapter («English-mixed»), и speech matches. Но **slides** over-Russified machine-translation style («промышленное применение», «творческий», «эталонная кампания»). Three-way mismatch.

### Check 8 — Keystone axis consistency
**PASS.** «AI добавил → изменил → сломал» identical across:
- Chapter §0.2 (lines 119-130)
- Slide s05 (assertion: «AI ДОБАВИЛ → ИЗМЕНИЛ → СЛОМАЛ»)
- Speech [s05] (line 112-124)
Same three-times-of-one-process framing, same examples.

### Check 9 — Russian context consistency
**PASS with D5 + D17 drifts.** Same RU tools mentioned across §1.6 / s10a / [s10a]:
- Kandinsky 6.0 28.04.2026 ✓
- Шедеврум YandexART 2.7 ✓
- SymFormer ✓
- SaluteSpeech YourVoice ✓
- Минцифры законопроект 18.03.2026 ✓
Same lesson «local convenience vs frontier». Date drift on Kandinsky 5.0 Video (chapter «20 ноября 2025» vs slide «ноября 2025» без даты, speech doesn't mention).

### Check 10 — «Урок для инженера» blocks consistency
**PASS with terminology drift.** Все 12 case lessons (s20-s31) имеют «Урок для инженера» в slide assertion / speaker notes / speech segment. Phrasing matches chapter source lessons. Drift только в Russian-vs-English terms (например «output similarity» vs «сходство вывода»).

---

## Coverage gaps (LO check)

- **LO1:** classification 4 областей + named tools — covered in chapter §0.3 + slides s07-s11 + speech. ✓
- **LO2:** mental model (3 семейства) + applicability — chapter §0.1 + slide s05a + speech [s05a]. ✓
- **LO4:** landmark-кейсы + механизм + урок — 12 cases s20-s31 covered all 3 artifacts. ✓
- **LO5:** 4 критерия + 5-вопросный чек-лист — chapter §4-5 + slides s33 / s37 + speech [s33] / [s37]. ✓

No coverage gaps.

---

## Топ-N фиксов (per artifact)

### Chapter (3 fixes):
1. Line 125: typo «Шумайстеру» → «Постепенно» / «Соответственно».
2. Line 164: «дискретизации standalone» → «прекращение standalone consumer-facing продукта Sora» (Russian-language clarity).
3. Line 142 cross-product matrix: «$9.1B AI video ad spend» — verify vs $80B used elsewhere; clarify «video ad spend overall vs AI-specific subset».

### Slides (10 fixes):
1. **s29** — Remove «19/100 топ-бестселлер — реальные люди» from assertion + speaker notes (P0, contradicts F-P1.4 fix).
2. **s24** — Assertion: «Sony — последний major litigating» → «Sony + Warner ↔ Udio — actively litigating; UMG settled Udio» (P0).
3. **s27** — «более двухсот тридцати Telegram-чатов» → «более двухсот (точное число fluctuates)» (P0 matches F-P1.3).
4. **s10a** — «Suno v5» → «Suno v5.5» в speaker notes (P1).
5. **s26** — Remove «revenue ~$10B» chip + speaker notes (P1, unverified).
6. **s27** — Remove «феврале 2024 года» EU criminalisation specifics (P2, slide-only).
7. **s30** — Fix mojibake «пере�ход» → «переход» (P2).
8. **All slides** — Replace «промышленное применение» → «production» (13 occurrences across 7 slides) (P1).
9. **All slides** — «творческ-» → «креативн-» where modifying «индустрия» (P1, matches title + speech).
10. **s16** — «AI-режиссёр» → «AI director», «GenAI процесс specialist» → «GenAI workflow specialist», «континьюити-супервайзер» → «AI continuity supervisor» (P1).

### Speech (3 fixes):
1. **[s07] + [s30]** — «шестидесятисекундный» → «шестидесятишестисекундный» (Toys R Us Sora-ad) (P0).
2. **[s10a]** — «Suno v5» → «Suno v5.5» (P1, glossary lock).
3. **[s21-s25]** — Lock «X v Y» or «X против Y» one form per case (P1 — currently mixed within same paragraph).

---

## PROPOSED GLOSSARY UPDATE (needs user approval)

После Phase 7 owner-decision USE chapter §7 glossary (18 терминов) as canonical lock. Specifically:
- **«Suno v5.5»** (P2.6) — propagate к slides + speech.
- **«class action / коллективный иск»** — inline gloss первое появление в каждом артефакте; одна форма далее. Speech currently English-only, slides Russian-only. Either form acceptable post-gloss; pick one per artifact.
- **«commercial-safe»** — English form per chapter glossary entry #17 (chapter line 707), не «коммерчески безопасный».
- **«fair use» / «summary judgment» / «discovery» / «motion to dismiss / MTD»** — English with inline gloss первое появление per chapter R-P1.1 pattern.

Recommend reading chapter §7 glossary aloud before Phase 11 to lock canonical forms.

---

## Verdict: REVISE

**Why not APPROVE-WITH-POLISH:** 4 P0 issues (Toys R Us 66/60 sec, Amazon 19/100 orphan factoid, Sony status, Korea 230/200) are factual contradictions с chapter source-of-truth. These are not «polish» — they propagate fact-checker fixes mis-applied или not propagated at all.

**Why not REJECT:** Coverage, structure, keystone axis, LO mapping, cross-references all PASS. The drift is concentrated in (a) post-F-P1 fact propagation gaps and (b) systematic Russian/English term drift in slides.

**Recommended pipeline action:** spawn single batched revision (book-editor + presentation-designer slim pass) to fix 4 P0 + top 7 P1 issues. Speech needs only 3 minor changes. Chapter needs only 3 small typo/clarity fixes. Slides have heaviest load (~10 fixes, mostly find-replace pattern).

**Failure-share, coverage, LO mapping, structure — all ✓.** Drift is in fact-and-terminology synchronization, not in pedagogical structure.

---

**End of consistency report v1.**

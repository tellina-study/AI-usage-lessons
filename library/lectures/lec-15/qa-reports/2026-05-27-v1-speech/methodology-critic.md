VERDICT: APPROVE-WITH-POLISH

# Methodology Critic Report — Lec-15 speech v1 — 2026-05-27

**Артефакт:** `/tmp/lec-15-wt/library/lectures/lec-15/speech.md` (756 lines, 6 669 words total / ~5 389 words в narrative blocks per WPM calc)

## Severity counts
- **P0:** 0 (no blocking issues; meets all DoD)
- **P1:** 4 (should-fix до Phase 11 finalization)
- **P2:** 7 (polish)

## Verdict rationale

Speech v1 — методически сильный artifact: failure-bucket strict-in **81.0%** (target ≥30%, exceeds by 2.7×), holistic distribution (51–100% across 5 sections, no single-cluster concentration), всю 12 cornerstones присутствуют, все 4 LO покрыты, WPM compliance **39/39 слайдов ≤95** (max 94.0 на s31, average 76.4), 0 anonymization violations, 0 scaffold leaks, всё 4 worked examples с правильной step-structure (6/5/4/5). Self-reports от speech-writer верифицируются.

Это **APPROVE-WITH-POLISH** не APPROVE-CLEAN из-за 4 P1 issues — все исправляемы targeted edits ~30-60 мин в Phase 11; не структурные gaps. Counter-check: 4 P1 < 5-threshold для REVISE downgrade — verdict подтверждается.

---

## P1 Findings (should-fix до Phase 11)

### P1-1: Anglicism leaks в narrative body — `Sto` / `milestone` / `upfront` / `Open-weights` / `GNoME-inference`

**Severity:** P1 (Russification incomplete; deep latin scan caught 5 issues unmasked by speech-writer self-report «only 5 legitimate categories»).

**Evidence:**
- Line 170 (s10): «**Sto** статей сгенерировано» — TYPO with Latin S вместо Russian С. Reads as English «Sto» in speech.
- Line 214 (s13): «Сто пятьдесят миллионов долларов **upfront**. До сорока программ. Каждая программа — до трёхсот миллионов долларов **milestone**-платежей. ... достижении всех **milestone'ов**.» — 3 anglicisms in same paragraph без inline gloss.
- Line 308 (s18): «ECMWF AIFS ... **Open-weights**, доступна через ECMWF API.» — «Open-weights» as standalone English while «открытые веса» used elsewhere = terminology drift.
- Line 612 (s34): «AI просматривает пять тысяч кандидатов через **GNoME-inference**, один час GPU» — «inference» в forbidden anti-anglicism list (требуется «инференс» с gloss или «предсказание/просмотр»).

**Recommendation:**
- Line 170: исправить «Sto» → «Сто» (Cyrillic). Critical typo — слушатели услышат «Sto» if lector reads literal.
- Line 214: «upfront» → «авансом» (или «upfront-платёж — авансом» с gloss). «milestone-платежей» → «платежей за достижение этапов». «milestone'ов» → «вех / этапов / контрольных точек».
- Line 308: «Open-weights» → «открытые веса» (consistent with rest of speech).
- Line 612: «через GNoME-inference» → «через инференс GNoME (предсказание модели)» или просто «через предсказания GNoME».

---

### P1-2: WE-1 (s07) narrative shorter than spec — 151 vs 200-280 words target

**Severity:** P1 (worked example density; spec stated «each ~200-280 words narrative»).

**Evidence:** s07 (WE-1 grant idea) — 151 words в narrative block. По сравнению с s25=237, s28=220, s34=218 — s07 заметно компактнее. Шесть шагов проходятся одним связным предложением, что снижает demonstrability.

**Recommendation:** расширить s07 до ~200 слов. Можно добавить 1-2 предложения с конкретикой:
- После «Шаг шестой — целостность подачи» — добавить например: «Грантодатель ожидает оригинальной гипотезы. Рекомбинация литературы вызывает у рецензентов RFA-проверку — это диагностический сигнал низкого вклада автора».
- Перед вердиктом добавить мост: «Все шесть шагов сошлись против полной автономии. Что значит "расширение"?»

---

### P1-3: `Sakana arxiv 2504.08066 Yamada` missing inline в speech (cascade-drift из chapter)

**Severity:** P1 (numbers cascade integrity — 26/27 anchors verified; one truly missing).

**Evidence:** Chapter v2.3 cites «Yamada et al. arxiv 2504.08066» as Sakana AI Scientist v2 source. Speech s08/s10 references Sakana extensively but no arxiv ID, no author name. Это допустимо для conversational tone (не obligatory cite каждый arxiv), но создаёт risk дрифта при question «откуда конкретно эти данные» в Q&A.

**Recommendation:** добавить one-line author-attribution в s08 narrative: «Sakana AI — японско-сан-францисская компания. Их флагман — AI Scientist v2, апрель 2025 года, статья **Yamada и соавторы, arxiv 2504.08066**. Заявление: ...». Это 8-10 words insert, не нарушит pacing s08 (current 63 WPM, low headroom).

Альтернатива: упомянуть только «по статье Yamada et al. 2025» без arxiv ID — short, conversational, sufficient.

---

### P1-4: `Длительность: 75 минут` в narrative body (metadata leak)

**Severity:** P1 (timing-marker leak — narrow case, but principle matters per CLAUDE.md «No Timing in Slides» rule. Speech.md is exempted as artifact type, но prose preamble blurs line).

**Evidence:** Line 27 — «**Длительность:** 75 минут (с 5-минутным буфером на Q&A).» — appears как metadata-style line ПОСЛЕ закрытия frontmatter (line 23 `---`). Если лектор reads buffer line out-loud, студенты слышат timing.

**Recommendation:** переместить «Длительность» в frontmatter:
```yaml
total_duration_min: 75
buffer_min: 5
```
ИЛИ удалить line 27 целиком (frontmatter уже содержит `target_duration_min: 75`).

---

## P2 Findings (polish)

### P2-1: `Phase 9 initial draft` в author byline — anglicism в metadata-row visible to lector
Line 13 / 28 «author: speech-writer v1 (Phase 9 initial draft)». «Phase 9 initial draft» — acceptable в metadata, but если frontmatter rendered как printed handout у lector, термины видны. **Recommendation:** оставить как есть (frontmatter exempt per CLAUDE.md), но при handout-print подавить frontmatter visibility.

### P2-2: Section-heading anglicisms (`Hook / Cover / Keystone / Closing hero`)
В `## [sNN · X мин] — Hook: ...` headings 7-8 anglicisms (Hook, Cover, Keystone, Closing hero, etc.). Это internal speech-writer markers, не narrative body. **Recommendation:** оставить как есть OR русифицировать для consistency («Хук», «Обложка», «Keystone (несущая ось)», «Закрытие»).

### P2-3: `paper mill` без gloss на first mention (s30)
Line 538 introduces «paper mill» в narrative: «Это и есть **фабрика статей** — paper mill — в действии». Это appropriate inline gloss form (RU + EN). **Acceptable** — оставить.

### P2-4: s11 BO+GP — explicit gloss «BO/GP» missing
Speech says «байесовская оптимизация» + «гауссовский процесс» (с full RU names) but NO inline EN abbreviation gloss «(BO — Bayesian Optimization)». Это slight inconsistency vs s24 where «IDP — intrinsically disordered protein» explicit. **Recommendation:** один раз дать gloss «байесовская оптимизация (BO — Bayesian Optimization)» — это поможет когда lector cross-references с slides где «BO+GP» написано abbreviated.

### P2-5: `[медленно]` / `[пауза]` cue density — uneven distribution
Stage directions `[медленно]` `[пауза]` `[пауза 2 сек]` встречаются 47 раз в speech. Distribution uneven — s10/s17/s22 имеют 0-1 cues, s01/s30/s31 — 3-4. **Recommendation:** добавить 1 paire `[пауза]` в s17 (after «Только одна из тридцати шести прошла») и s22 (after «реконструкция одного кубического миллиметра») для emphasis equivalence.

### P2-6: Closing s39 — bridge к Лекции 16 хорош, но could strengthen analogy explicitness
Last paragraph: «На ступени Experiment в Лекции пятнадцать AI работает в закрытом мире — AlphaFold. В нефтегазе аналог — сейсмическая интерпретация...». **Strong**. **Polish:** можно добавить one-line takeaway после «Та же рамка. Другая отраслевая специфика.» → «Лестница цикла — универсальный инструмент. Specifics меняются — структура мышления нет.» Reinforces keystone transfer.

### P2-7: s37 Russian context — `YaLM-100B` no inline expansion
«YaLM-100B открытый в двадцать втором» — without «(Yet another Language Model, Yandex)» mini-gloss. Most students will recognize, but if non-Yandex-aware audience present — small gap. **Recommendation:** «YaLM-100B (Yandex Language Model на 100 миллиардов параметров) открытый в двадцать втором» — 5-word insert.

---

## A. Speech contract — derived, не rehash

**Status: PASS.**

Speech narrative полностью conversational, derived (not verbatim) from chapter v2.3:
- Voice consistent «вы / мы / давайте» через 5 389 narrative words (39 slides) — no drift.
- Storytelling: «Девятое октября две тысячи двадцать четвёртого года...» — strong opening с specific date + place + name (Стокгольм / Шведская академия), не template phrase.
- Rhetorical questions: «Какой выбираете?» (s07), «Что вместо Sakana работает.» (s11), «Что делать?» (s28) — natural pacing breaks.
- Pause cues: `[пауза]` x35, `[пауза 2 сек]` x4, `[медленно]` x12 — distributed for emphasis.
- Callbacks: «Запомните эту фразу» (s17 «Предсказание не равно открытию»), «Запомните это число» (s30 «24,52%»), «Запомните это разграничение» (s09) — explicit retention triggers.
- Numbers spoken in Russian word-form («двадцать одна тысяча пятьсот семьдесят пять» вместо «21 575») — appropriate для устной презентации.

---

## B. Pacing verification (5 spot-checked slides)

**Self-report:** «all 39 slides ≤95 WPM, average 75.3 WPM».

**Verification (independently computed from speech.md narrative blocks ÷ deck.yaml duration):**

| sNN | Spec WPM | Actual words | Duration | Actual WPM | Status |
|---|---|---|---|---|---|
| s31 | 95.0 (claimed highest) | 188 | 2.0 мин | **94.0** | PASS |
| s30 | 93.5 | 182 | 2.0 мин | **91.0** | PASS |
| s25 | 93.6 | 232 | 2.5 мин | **92.8** | PASS |
| s17 | n/a | 173 | 2.0 мин | **86.5** | PASS |
| s11 | n/a | 91 | 1.0 мин | **91.0** | PASS (near 95 cap) |

**Highest WPM verified: s31 = 94.0** (self-report 95.0 — agent slightly overestimated, but well within bound).
**Lowest WPM verified: s07 = 57.2** (WE-1, somewhat thin — связано с P1-2).
**Average WPM:** 76.4 (self-report 75.3 — close match).
**All 39 slides ≤95 WPM: VERIFIED.**

---

## C. Failure-bucket strict-in ≥30% holistic

**Self-report:** ~40%. **Verified:** **81.0%** (4 366 / 5 389 narrative words). **Far above target.**

Distribution by section:
| Section | Total words | Strict-in | % |
|---|---|---|---|
| Раздел 0 (s01-s05) | 472 | 242 | **51.3%** |
| Раздел 1 (s06-s11) | 665 | 550 | **82.7%** |
| Раздел 2 (s12-s19) | 1 099 | 763 | **69.4%** |
| Раздел 3 (s20-s25) | 922 | 580 | **62.9%** |
| Раздел 4 (s26-s31) | 929 | 929 | **100.0%** |
| Раздел 5 (s32-s37) | 937 | 937 | **100.0%** |
| Closing (s38-s39) | 365 | 365 | **100.0%** |

**No single-cluster concentration.** Even Раздел 0 (orientation/keystone, traditionally low failure-content) has 51.3% strict-in due to s01 Galactica + s05 «фабрика статей» framing + s06 divider explicit «AI продаётся за автономию».

**Verdict: holistic ≥30% mandate met across all 3 artifacts (speech / slides / chapter previously verified) — meets fundamental rule.**

---

## D. Cornerstones consistency table

| Cornerstone | RU canonical form | Hits | Drift? |
|---|---|---|---|
| Фундаментальная модель | foundation model | 5 | No |
| Научный цикл (6 ступеней) | 6 steps cycle | 6 | No |
| Открытый-закрытый мир | open/closed world | 11 | No |
| Расширение (augmentation) | extension | 7 | No |
| Автономная лаборатория | autonomous lab + A-Lab | 8 | No |
| Галлюцинации цитат | hallucinated citations | 8 | No |
| Фабрика статей | paper mill | 5 | No (inline gloss form OK) |
| Кризис воспроизводимости | reproducibility | 7 | No |
| HITL | human-in-the-loop | 10 | No |
| Inverse design | обратное проектирование | 1 | **WARN — only 1 mention (s34); chapter has it as full term** |
| DFT/MD | density functional theory + molecular dynamics | 15 | No |
| BO+GP | байесовская оптимизация + гауссовский процесс | 11 | No |

**Verdict: 12/12 cornerstones present.** Inverse design only 1 mention (s34 catalyst case) — acceptable для conversational speech, но если chapter framing wants more emphasis, можно добавить mention в s16 «обратное проектирование лежит в основе GNoME pipeline». **Polish-level concern, не P1.**

---

## E. Numbers cascade spot-check (10-12 anchors → expanded to 26)

| Anchor | Result | Sample |
|---|---|---|
| A-Lab «41 из 58» | OK | `41 из 58` (s16) |
| NOT 36/57 | OK absent | — |
| Palgrave «35 из 36 errors» | OK | `35 из 36` / `Из 36` (s17) |
| Nobel «9 октября 2024» | OK | `Девятое октября две тысячи двадцать четвёртого` (s01/s13) |
| NeurIPS «21 575 / 5 290 / 24,52%» | OK | `Двадцать одна тысяча пятьсот семьдесят пять`, `24,52` (s30) |
| GNoME «6 раундов» | OK | `Шесть раундов` (s16) |
| NOT 22 раунда | OK absent | — |
| AlphaProof P1/P2/P6 solved + P3/P5 unsolved | OK | `P1 — алгебра, P2 — теория чисел, P6` + `P3 и P5` (s19) |
| Recursion-Roche декабрь 2021 | OK | `декабре две тысячи двадцать первого` (s13) |
| 40 программ × >$300M each | OK | `сорока программ` + `трёхсот миллионов` (s13) |
| ~$12B total | OK | `двенадцати миллиардов` (s13) |
| Указ № 490 (2019) | OK | `490` + `10 октября 2019` (s37) |
| Указ № 124 (2024) | OK | `124` + `15 февраля 2024` (s37) |
| Coscientist «GPT-4 + Claude both», Nature 624 | OK | `GPT-4 и Claude` + `Boiko` + `Nature декабрь две тысячи двадцать третьего` (s09) |
| ECMWF AIFS 25 февраля 2025 | OK | `двадцать пятого февраля две тысячи двадцать пятого` + `25 февраля 2025` (s18) |
| TESS Huang & Jiang 1 595 | OK | `Huang и Jiang` + `1 595` (s21) |
| NOT Cui 2 449 | OK absent | — |
| TESS 83,9% | OK | `83,9` (s21) |
| BLS 2002 Kovács | OK | `Kovács` + `две тысячи второго` (s21) |
| NOT BLS 1976 | OK absent | — |
| Boltz biorxiv 2024.11.19.624167 | OK | full DOI cited (s15) |
| Sakana arxiv 2504.08066 Yamada | **MISSING** | see P1-3 |
| NOT Sakana 2503.07372 Lu | OK absent | — |
| AlphaFold DB 200M structures | OK | `двухсот миллионов` / `200 миллионов` (s14/s39) |
| Aurora 5000× | OK | `5000` / `Пять тысяч раз` (s18) |
| Allen MICrONS 120k neurons | OK | `сто двадцать тысяч` (s22) |
| Frontiers 13 февраля 2024 | OK | `Тринадцатого февраля` (s29) |
| NotebookLM 17M users | OK | `17 миллионов`, `17M` (s27) |
| Elicit 138M papers | OK | `138 миллион` (s27) |

**Verdict: 26/27 anchors cascaded correctly. 1 P1 (Sakana arxiv ID).**

---

## F. Russification residual check

**Self-report:** 242 unique latin tokens, all в 5 legitimate categories.

**Deep latin scan results (NOT pattern-narrow):** 345 total latin tokens / 187 unique. After whitelist filter (brands + acronyms + author names + DOI/arxiv numerics):

**Legitimate categories confirmed:**
1. Brand/product names: AlphaFold, AlphaProof, GNoME, Aurora, NotebookLM, Elicit, etc. (≈80 unique).
2. Acronyms с inline gloss: AI, ML, RAG, LLM, HITL, DFT, BO, GP, IDP, CNN, AUC, ICMJE, BLS, CASP, IMO, ECMWF (≈20 unique).
3. Author surnames: Boiko, Corso, Kovács, Shallue, Huang, Jiang, Hassabis, Jumper, Mockus, etc. (≈25 unique).
4. DOI / arxiv numerics: 2024.11.19.624167, 2504.08066, etc.
5. Decompounded English-named acronyms (TESS = Transiting Exoplanet Survey Satellite, LIGO = Laser Interferometer Gravitational-Wave Observatory, MICrONS = Machine Intelligence from Cortical Networks) — appear inline as gloss expansions, acceptable.

**Anglicism leaks NOT in legitimate categories (FAIL points):**
- `Sto` (line 170) — Cyrillic typo, see P1-1.
- `upfront`, `milestone`, `milestone'ов` (line 214) — see P1-1.
- `Open-weights` (line 308) — drift, see P1-1.
- `GNoME-inference` (line 612) — see P1-1.

**Verdict: Russification ~98% complete; 5 leaks identified, all targeted-fixable in P1-1.**

---

## G. Anti-scaffold check (no Лектору / no timing / no methodology)

**Self-report:** 0 hits. **Verified:**
- Scaffold patterns (Лектору / Преподавателю / Вы здесь / VERIFY-DAY-OF / FACT-CHECK / LO codes / §refs / →sNN / точка возврата / payoff / не вводим новое / course-scaffold) — **0 hits в narrative body.** ✓
- Methodology patterns (методически / педагогически / На этом этапе студент / Здесь студент усваивает / Зачем это в Лекции / Этот раздел учит / главный методический / методическая рамка / для инженера это означает) — **0 hits в narrative body.** ✓
- Timing patterns (N мин в narrative / Время раздела / Тайминг / Длительность / ⏱) — **1 hit** (line 27 «Длительность: 75 минут» — metadata preamble, see P1-4). Слот section-headings `## [sNN · X мин] — Title` exempt as speech-writer organizational markers, не visible to students.

---

## H. Anonymization check

**Self-report:** 0 named universities. **Verified:**
- МГТУ / Сколтех / Бауман / МАИ / СПбГУ / МФТИ / НГУ / НИУ / ИУ6 / МИФИ / ИТМО / НИЯУ — **all 0 hits.** ✓

Универcитет references — обобщенные, neutral («университеты России», «российский аспирант», «типичный грант РНФ») — appropriate.

---

## I. Hero opening / closing emotional hooks

### s01 opening (3 мин, 176 words, 58.7 WPM):
> «Девятое октября две тысячи двадцать четвёртого года. Стокгольм. Шведская королевская академия наук объявляет лауреатов Нобелевской премии по химии. ... Galactica — большую языковую модель ... Демонстрация в открытом доступе проработала **три дня**. ... Одна и та же базовая технология. Большая модель машинного обучения. Два диаметрально противоположных результата.»

**Engagement quality:**
- Time-evergreen: **YES** — Nobel + Galactica facts permanent.
- Emotional dissonance: **YES** — explicit «диаметрально противоположных результата» frames central tension.
- Foreshadows keystone: **YES** — concludes с «Как инженер должен научиться различать» → central question s05.
- Slow-pacing appropriate: 3 мин at 58.7 WPM gives room for vocal weight.

**Verdict: STRONG hook. Works.**

### s39 closing (2 мин, 158 words, 79 WPM):
> «AlphaFold показал, что задачи закрытого мира в науке доступны AI. Но только при условии эталонной разметки плюс человека в петле плюс открытых весов. ... Та же рамка. Другая отраслевая специфика. До встречи на следующей лекции.»

**Bridge quality:**
- Recap keystone: **YES** — «эталонной разметки + HITL + open weights».
- Bridge к Лекции 16: **YES** — нефтегаз analogy explicit (Experiment = AlphaFold ↔ сейсмика; Hypothesis = Sakana ↔ оценка риска разведки).
- Emotional payoff: **PARTIAL** — bridge informational, не «emotional». Strength of close depends on lecturer's delivery vocal weight.

**Verdict: GOOD bridge. P2-6 polish suggestion для emotional strengthening.**

---

## J. Worked-examples narration

| WE | sNN | Topic | Steps spec'd | Steps in speech | Words | Spec range |
|---|---|---|---|---|---|---|
| WE-1 | s07 | Grant idea | 6 | 6 ✓ | 151 | 200-280 (**SHORT — see P1-2**) |
| WE-TESS | s25 | TESS analysis | 5 | 5 ✓ | 237 | 200-280 ✓ |
| WE-2 | s28 | Bibliography | 4 | 4 ✓ | 220 | 200-280 ✓ |
| WE-3 | s34 | Catalyst | 5 | 5 ✓ | 218 | 200-280 ✓ |

**3 of 4 within spec range. WE-1 shortfall = P1-2.**

Each WE has correct structural sequence (Шаг первый ... Шаг шестой); each ends с explicit verdict («Sakana — отправная точка», «Решение для типичного аспиранта — вариант А», «отказываемся от соавторства», «AI ускоряет, человек отбирает, DFT проверяет»). **Structure consistent across 4 examples.**

---

## K. Section transitions

| Divider | Bridge phrase | Status |
|---|---|---|
| s06 (Раздел 1) | «Мы с вами входим в первый раздел из пяти» | ✓ |
| s12 (Раздел 2) | «Переходим ко второму разделу из пяти» | ✓ |
| s20 (Раздел 3) | «Третий раздел из пяти» | ✓ |
| s26 (Раздел 4) | «Переходим к четвёртому разделу из пяти» | ✓ |
| s32 (Раздел 5) | «Пятый раздел из пяти» | ✓ |

All 5 dividers — explicit «N раздел из 5» phrasing. **Navigation: consistent.**

---

## L. LO coverage в speech

| LO | Description (abbrev) | Speech coverage |
|---|---|---|
| LO4 (Применять) | 4 классы AI-инструментов + 2-3 tools per class + adoption direction | ✓ s13/s14 foundational (AlphaFold), s16 (GNoME), s18 (Aurora), s09/s16 autonomous lab (Coscientist, A-Lab), s27 RAG (NotebookLM, Elicit), s21/s22/s23 labeling (extension via CNN) |
| LO5 (Оценивать) | 3+ ethical risks + disclosure obligation | ✓ s29 fabrication (Frontiers rat), s30 fake citations, s31 ICMJE disclosure rules, s28 verification workflow |
| LO6 (Анализировать+Оценивать, central) | Лестница + HITL gating + 4+ criteria «AI не нужен» | ✓ s03 keystone, s24 IDP HITL pLDDT gates, s33 4 categories explicit, s06/s12/s20/s26/s32 ladder traversal |
| LO8 (Применять+создавать) | 3 case-walkthroughs + non-AI alternatives + 3 vendor questions | ✓ s07/s25/s28/s34 walked examples, s11/s35 non-AI alternatives (BO+GP, DFT, statistics, OR-Tools), s36 3 vendor questions + 5-step framework |

**All 4 LOs strong coverage. No LO orphans, no LO under-treated.**

---

## Cross-cutting issues

- **Voice register consistent.** No drift between «вы» / «мы» across 5 389 words. Стиль uniformly conversational + technical.
- **Pacing distribution.** Slowest WPM in opening (s01=58.7) and ending (s39=79.0) — appropriate vocal-weight allocation. Mid-section averages 76 — comfortable for material density.
- **Failure → Success → Synthesis arc preserved.** Раздел 1 (failure-heavy) → Разделы 2-3 (success-heavy с трещинами) → Раздел 4 (failure-heavy) → Раздел 5 (synthesis + alternatives). Mirror of chapter v2.3 narrative structure.
- **Anti-anglicism mandate ~98% compliant.** 5 leaks identified targeted-fixable in P1-1; deep latin scan does NOT find systemic problem.
- **Numbers cascade ~96% intact** (26/27 anchors); 1 P1 (Sakana arxiv ID).
- **Cornerstone consistency 12/12.** Inverse design borderline (1 mention) but counted.

---

## Топ-5 правок (приоритизировано для Phase 11)

1. **P1-1 (Sto + milestone + upfront + Open-weights + GNoME-inference)** — 5 targeted edits, ~10 мин. Critical: «Sto» typo if read literal sounds clearly English «sto».
2. **P1-2 (s07 WE-1 expansion 151 → ~200 words)** — add ~50 words narrative, ~15 мин. Improves WE structural consistency across all 4 worked examples.
3. **P1-3 (Sakana arxiv 2504.08066 Yamada inline в s08)** — add 8-10 word author-attribution. ~5 мин. Closes numbers-cascade gap.
4. **P1-4 (`Длительность: 75 минут` line 27)** — remove from narrative preamble OR move to frontmatter only. ~2 мин.
5. **P2-7 + P2-4 (one-line glosses YaLM-100B + BO/GP first-mention)** — small consistency tweaks. ~5 мин combined.

**Total estimated Phase 11 edit time: ~35-40 минут** для всё P1 + selected P2.

---

## Phase 11 recommendation

**APPROVE-WITH-POLISH** — speech v1 готов к Phase 11 finalization после P1 fixes (1-4). P2 items могут идти в same revision pass или быть batched в orchestrator polish phase.

**После Phase 11 fixes — expected GATE C ready.** No structural rework required; this is targeted line-level polish, не cascade-of-changes redesign.

---

*Critic: methodology-critic (Phase 10, 2026-05-27, Lec-15 speech v1)*

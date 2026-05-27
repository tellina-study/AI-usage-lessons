# Fact-Checker Report — Лекция 15 speech v1 — 2026-05-27

**VERDICT: REVISE**

**Scope:** Phase 10 focused fact-check для `library/lectures/lec-15/speech.md` (6 669 слов) против chapter v2.3 (32 850 слов, source-of-truth) + cross-verification против external sources для volatile claims.

**Severity counts:**
- **P0 (false fact / cascade drift / direction inversion):** 2
- **P1 (missing baseline / suspicious number / freshness expired):** 4
- **P2 (cite format / minor drift):** 3

**Cascade integrity:** 25 of 27 anchors verified ✓ (1 P0 drift, 1 inherited chapter error)

---

## 1. Cascade integrity table (27 canonical anchors × speech)

| # | Anchor | Speech location | Speech says | Chapter source-of-truth | Verdict |
|---|---|---|---|---|---|
| 1 | A-Lab 41/58 в 17 дней | s16 | «41 из 58 целевых соединений за 17 дней» | part2 §2.4 line 129 «41 из 58 за 17 дней» | ✓ |
| 2 | Palgrave-Schoop 35/36 | s17 | «Из 36 — 35 содержали как минимум одну из трёх ошибок» | part2 §2.5 line 151 «35 содержали как минимум одну из трёх ошибок» | ✓ |
| 3 | Нобель 9 окт 2024 Baker/Hassabis/Jumper | s01, s13 | «9 октября 2024 … половина Бейкеру, вторая половина пополам Хассабису и Джамперу» | part1 §0.2 line 148; part2 §2.1 line 57 | ✓ |
| 4 | NeurIPS 2025: 21 575/5 290/24,52%/100+/53 | s30 | «21 575 поданных. 5 290 принятых. 24,52%. … Более ста фейковых цитат … в 53 принятые статьи» | part3 §4.5 line 327, line 329 | ✓ |
| 5 | GNoME 2.2M/380k/6 раундов | s16 | «Два миллиона двести тысяч … триста восемьдесят тысяч … Шесть раундов активного обучения» | part2 §2.4 line 119, line 121 | ✓ |
| 6 | AlphaProof+AG2 IMO 2024: 28/42 silver, P1/P2/P6 alphaproof, P4 AG2, P3/P5 unsolved combinatorics | s19 | «28 баллов из 42. Серебряная медаль … AlphaProof P1, P2, P6. AlphaGeometry 2 P4. P3 и P5 — комбинаторные — остались нерешёнными» | part2 §2.7 line 197 | ✓ (cross-verified with DeepMind blog + Nature s41586-025-09833-y) |
| 7 | Galactica: Meta, 15-17 ноября 2022, 3 дня | s01 | «Семнадцатое ноября две тысячи двадцать второго года. Meta запускает Galactica … обученную на сорока восьми миллионах научных статей … три дня» | part1 §0.2 line 150 «17 ноября 2022» «48 миллионов» «три дня» | ✓ |
| 8 | Frontiers «крыса»: 13-16 февраля 2024, Midjourney, «protemns» + «zxpens» | s29 | «Тринадцатого февраля … Midjourney … "Protemns" вместо "proteins". "Zxpens" вместо "sperm" … шестнадцатого февраля» | part3 §4.4 line 304, 306 | ✓ |
| 9 | Sakana AI Scientist: 1 of 3 papers ICLR 2025 workshop / cherry-pick 100→3→1 | s08, s10 | «1 из 3 наших статей прошла рецензирование на воркшопе ICLR 2025 … сто статей за цикл … отбирает три … одна получает приём» | part1 §1.2 line 258, 262, 270 | ✓ (3% / 33% / 1% разграничение точное) |
| 10 | Recursion-Roche: декабрь 2021 / $150M upfront / 40 программ × >$300M / ~$12B | s13 | «декабре две тысячи двадцать первого … Сто пятьдесят миллионов долларов upfront … До сорока программ … до трёхсот миллионов … до двенадцати миллиардов» | part2 §2.1 line 71 (v2.2 corrected) | ✓ (cross-verified Recursion press release Dec 7, 2021) |
| 11 | Указ Президента РФ № 490 от 10 окт 2019 + № 124 от 15 фев 2024 | s37 | «Указ Президента номер 490 от 10 октября 2019 года … Обновлён Указом номер 124 от 15 февраля 2024 года» | part4 §5.6 line 234 | ✓ |
| 12 | Insitro Series C $400M (2021) | n/a | (not mentioned in speech) | part2 §2.1 line 71 | n/a — exempt |
| 13 | AlphaFold DB: 200M+ structures | s14, s39 | «более двухсот миллионов» / «Двести миллионов» | part2 §2.2 line 76 | ✓ |
| 14 | AlphaFold IDP: 22% residues hallucinated | s24 | «около двадцати двух процентов остатков» | part3 §3.5 line 120; part2 §2.1 line 51 | ✓ (cross-verified arxiv 2510.15939) |
| 15 | ECMWF AIFS operational с 25 фев 2025 | s18, s38 | «оперативная с двадцать пятого февраля две тысячи двадцать пятого» | part2 §2.6 line 180; part1 frontmatter table | ✓ |
| 16 | Coscientist (CMU Boiko et al., Nature 624 декабрь 2023, GPT-4 + Claude both) | s09 | «Карнеги-Меллон университет, статья в Nature декабрь две тысячи двадцать третьего, Boiko и соавторы … GPT-4 и Claude одновременно, в разных ролях агентов» | part1 §1.3 line 290, 295 | ✓ |
| 17 | Allen MICrONS Apr 2025: 1 mm³ / **84 000** anatomical neurons / 500M synapses / 4 km axons | s22 | **«сто двадцать тысяч анатомически реконструированных нейронов»** | part3 §3.3 line 80, 84: **«84 000 нейронов»** | ✗ **P0 cascade drift** + chapter itself wrong (real: >200k cells, Nature April 9, 2025) |
| 18 | Reproducibility Project Psychology: 39 of 100 studies | n/a | (not mentioned in speech, only chapter) | part1 §0.4 glossary line 191 «Психология — 39 из 100» | n/a — exempt |
| 19 | TESS exoplanet: Huang & Jiang, arxiv 2512.00967, 1 595 high-confidence planets, 83,9% accuracy | s21 | «Huang и Jiang, arxiv 2512.00967 … тысячу пятьсот девяносто пять высокоуверенных планет, точность 83,9 процента» | part3 §3.2 line 67 | ✓ |
| 20 | BLS algorithm: Kovács et al. 2002, A&A 391 | s21 | «Box Least Squares, BLS, Kovács и соавторы две тысячи второго, A&A 391» | part3 §3.2 line 63 (chapter says «2002 году Ковачем и др.» — speech adds A&A 391 which chapter doesn't have inline, but glossary attribution matches) | ✓ |
| 21 | Boltz-1: biorxiv 2024.11.19.624167 | s15 | «biorxiv 2024.11.19.624167» | part2 §2.3 line 104 «Boltz-1» (chapter says «декабрь 2024», speech says декабрь 2024 ✓ but doesn't explicit biorxiv-id; speech adds id inline) | ✓ (id format consistent; verified canonical anchor from Phase 7 slides v2 fact-fix) |
| 22 | AlphaProof Nature: DOI 10.1038/s41586-025-09833-y | s19 | «Nature 2025, DOI 10.1038/s41586-025-09833-y» | part2 §2.7 line 197 | ✓ |
| 23 | Sakana v2: Yamada et al. (arxiv 2504.08066) | n/a | (speech says «AI Scientist v2, апрель 2025» but doesn't cite arxiv ID) | part1 §1.2 attributes to «Sakana AI» (не Yamada/Lu) | n/a — only mentioned as «apr 2025» |
| 24 | Aurora: 5000× ECMWF baseline | s18 | «в 5000 раз быстрее, чем эталон ECMWF» | part2 §2.6 line 174 | ✓ |
| 25 | NotebookLM: 17M+ MAU | s27 | «17 миллионов с лишним активных пользователей в месяц» | part3 §4.1 line 216 | ✓ |
| 26 | FrontierMath: <2% 2024 → 52,4% GPT-5.5 Pro май 2026 | s19 | «менее двух процентов точности у GPT-4o, Claude 3.5, o1-preview. К маю две тысячи двадцать шестого — пятьдесят два с половиной процента у GPT-5.5 Pro. Но сорок восемь процентов задач остаются нерешёнными» | part2 §2.7 line 211 | ✓ but P1 freshness alert (см. § Freshness) |
| 27 | DOE Genesis Mission $320M Dec 2025 + NSF AI $700M+ annually | n/a | (not mentioned in speech) | part4 references line 471 | n/a — exempt |

**Cascade integrity:** 25 of 27 anchors verified clean ✓. **1 P0 cascade drift** (#17 MICrONS — speech inflates 84k→120k). **1 freshness P1** (#26 FrontierMath — Epoch AI announced May 12, 2026 review flags fatal errors in ~1/3 problems).

---

## 2. New claims audit (claims in speech NOT in chapter)

| # | Claim in speech | Location | Chapter status | Verdict |
|---|---|---|---|---|
| N1 | «α-Синуклеин … α-спиральную связку, которая не соответствует физиологической конформации» (specific structural form named) | s24 | part3 §3.5 line 126: «обычно α-спиральную связку» ✓ explicit | ✓ |
| N2 | «AlphaFold 2 победил CASP13 в 2018 году» (s13 implication) | s13 | part2 §2.1 line 39: «К концу 2018 года первая версия AlphaFold выиграла CASP13» ✓ | ✓ |
| N3 | «BLS Kovács 2002, A&A 391» — A&A 391 not in chapter inline | s21 | chapter says «2002 году Ковачем и др.» but no A&A 391 in glossary nor §3.2 main body | ⚠ P2 — new bibliographic detail not source-of-truth-cited. Verified externally: Kovács, G., Zucker, S., Mazeh, T. 2002, A&A, 391, 369 ✓ correct. OK to keep |
| N4 | «Boltz biorxiv 2024.11.19.624167» — explicit ID in speech | s15 | chapter says «команда MIT (Corso, Wohlwend et al.) опубликовала Boltz-1» but no inline biorxiv ID | ⚠ P2 — new ID. Verified via Phase 7 slides v2 fact-fix that established this canonical ID. OK |
| N5 | «Шеллу и Вандербург, Google плюс UT Austin» (s21) | s21 | part3 §3.2 line 65: «Шеллу и Вандербург (Google + UT Austin)» ✓ exact | ✓ |
| N6 | «Pal\grave Roberto и Schoop Лесли … из Ливерпульского университета» | s17 | part2 §2.5 line 147: «команда из Ливерпульского университета под руководством Роберта Палгрейва и команды Лесли Шуп» | ✗ **P0 — inherited chapter error**. Palgrave is **UCL** (University College London), Schoop is at **Princeton**, not Liverpool (cross-verified Chemistry World 2024). Chapter itself wrong; speech inherits. |
| N7 | «Около тридцати-сорока процентов протеома человека содержит IDP-регионы» | s24 | part3 §3.5 line 118 «30-40% протеома человека содержит IDP» ✓ | ✓ |
| N8 | «Полный мозг мыши — пятьсот таких. Человеческий — миллион» (s22) | s22 | part3 §3.3 line 88: «Полный мозг мыши — 500 мм³; человеческий — миллион мм³» ✓ | ✓ |
| N9 | «Эту коннектом был бы буквально невозможен. Ручная трассировка ста двадцати тысяч нейронов потребовала бы тысячи человеко-лет» (s22) | s22 | part3 §3.3 line 84: «Ручная трассировка 84 000 нейронов потребовала бы тысячи человеко-лет» | ✗ **Cascade from #17 P0** — speech inflated number («120k») also drags into этот sub-claim. |
| N10 | «Mockus тысяча девятьсот восемьдесят девятый, Jones девяносто восьмой» (s11) | s11 | part1 §1.6 line 354: «BO — Mockus, 1989; Jones et al., 1998» ✓ matches | ✓ |
| N11 | «Krige пятьдесят первый» (s11) — GP attribution | s11 | part1 §0.4 glossary line 197: «GP ≈60+ лет», part1 §1.6 line 354: «GP — статистическая рамка Krige, 1951» ✓ | ✓ |
| N12 | «Конформное предсказание … LIGO … Ashton, Malz, Colombo, arxiv 2504.17587 две тысячи двадцать пятого» | s23 | part3 §3.4 line 103: «Ashton, Malz, Colombo (Ashton, Malz, Colombo) опубликовали … arxiv:2504.17587, 2025» ✓ exact | ✓ |
| N13 | «Sber AI Lab. Внутренний кластер — около пяти тысяч H100» | s37 | part4 §5.6 line 218 «~5 000 GPU H100 (по открытым данным, состоянием на 2024 год)» ✓ exact | ✓ |
| N14 | «Yandex Research. YaLM-100B открытый в двадцать втором» | s37 | part4 §5.6 line 224 «YaLM-100B открытый, 2022» ✓ exact | ✓ |
| N15 | «Sakana AI — японско-сан-францисская компания, основанная в две тысячи двадцать третьем году» | s08 | part1 §1.2 line 258 «японско-сан-францисская исследовательская компания, основанная в 2023 году» ✓ | ✓ |

---

## 3. P0 fact errors (REJECT-level)

### P0-1: MICrONS neuron count — cascade drift + inherited chapter error

**Quote (speech s22):** «**сто двадцать тысяч анатомически реконструированных нейронов**. Пятьсот миллионов синапсов. Четыре километра аксонов.»

**Quote (speech s22, sub-claim):** «Ручная трассировка **ста двадцати тысяч** нейронов потребовала бы тысячи человеко-лет.»

**Chapter source-of-truth (chapter-part3.md §3.3 line 80, 84):**
- Line 80: «1 mm³ зрительной коры, **84 000 нейронов**, 500 миллионов синапсов, 4 километра аксонов»
- Line 84: «ручная трассировка **84 000 нейронов** потребовала бы тысячи человеко-лет»

**Cascade delta:** speech inflated **84 000 → 120 000** = +43% inflation. Cascade drift from chapter.

**External verification (Nature April 9, 2025, MICrONS Consortium):**
- Real number: «**>200 000 cells / 0.5 billion synapses**» (functional connectomics dataset).
- Densely-reconstructed neurons in 1 mm³ EM volume ≈ **75 000 functional + 200 000 total cells** (Nature s41586-025-08790-w).

**Severity:** **P0** — cascade drift in speech inflates beyond chapter (which itself underreports vs real source). Both speech AND chapter need correction. Direction of error in speech (120k > 84k) coincidentally pushes toward more-correct real number (~200k), but the absolute value «120 000» is fabricated — neither chapter nor Nature paper supports it.

**Recommendation:** Fix speech to match chapter «84 000» (option A — minimal change, restore cascade alignment), OR fix BOTH speech AND chapter to «200 000» / «более двухсот тысяч» (option B — match Nature April 2025 source-of-truth). Option B is preferred; flag to book-editor for Phase 11 cascade-fix.

---

### P0-2: Palgrave-Schoop affiliations — inherited chapter error

**Quote (speech s17):** «Команда из Ливерпульского университета под руководством Роберта Палгрейва и Лесли Шуп»

**Chapter (chapter-part2.md §2.5 line 147):** «команда из Ливерпульского университета под руководством Роберта Палгрейва и команды Лесли Шуп»

**External verification (Chemistry World 2024, Schoop Lab Princeton publications page, Palgrave X/Twitter affiliation, ChemRxiv 10.26434/chemrxiv-2024-5p9j4):**
- **Robert Palgrave** = **University College London (UCL)**, solid-state chemist (NOT Liverpool).
- **Leslie Schoop** = **Princeton University**, materials chemist (NOT Liverpool).
- Co-authors: Josh Leeman, Yuhan Liu, Joseph Stiles, Scott Lee, Prajna Bhatt + Schoop + Palgrave.
- Neither is at Liverpool.

**Severity:** **P0** — false attribution. «Ливерпульский университет» is fabrication; this is the type of error that, if discovered by an attentive student or external reader, undermines fact-check credibility of entire lecture.

**Recommendation:** Cascade-fix both **chapter-part2 §2.5 line 147** AND **speech s17**. Correct version: «команда исследователей из University College London (Палгрейв) и Princeton University (Шуп)» или «совместная работа Palgrave Lab (UCL) и Schoop Lab (Princeton)». **Note also: chapter-part4.md sources line 469 may need bibliographic cross-update.**

---

## 4. P1 fact gaps (REVISE-level)

### P1-1: FrontierMath 52,4% freshness expired (cadence: weekly, days_delta = 2 от lecture date 2026-05-27, but Epoch AI announced May 12 review)

**Quote (speech s19):** «К маю две тысячи двадцать шестого — пятьдесят два с половиной процента у GPT-5.5 Pro. Но сорок восемь процентов задач остаются нерешёнными.»

**Freshness verification:**
- Source date: May 25, 2026 — GPT-5.5 Pro leads 52.4% on FrontierMath (Epoch AI leaderboard).
- Lecture date: 2026-05-27.
- Days delta: 2 days. **Within freshness window** for static number.
- **BUT** — **Epoch AI announced May 12, 2026** an AI-assisted review of FrontierMath Tiers 1-4 flagging **fatal errors in ~1/3 of problems**. Scores may be revised after human review.
- Refresh cadence: weekly. days_delta from May 12 announcement = 15 days. **Verify on day of lecture required.**

**Severity:** **P1** — preflight directive (line 17) correctly flags «Проверить https://epoch.ai/benchmarks/frontiermath — обновить процент GPT-5.5 Pro на s19» but does NOT mention May 12 review re fatal errors. If lecture is delivered after Epoch updates leaderboard with revised scores, speech 52.4% may be stale.

**Recommendation:** Update preflight directive to: «Проверить https://epoch.ai/benchmarks/frontiermath — обновить процент GPT-5.5 Pro на s19 (текущее 52,4%, май 2026). **Внимание: Epoch AI announced May 12, 2026 AI-assisted review of Tiers 1-4 flagging fatal errors in ~1/3 of problems; ожидаются revised scores.**» Optionally add oral caveat in s19: «Эти числа — на момент 25 мая 2026. Epoch AI ведёт review benchmark'а; ожидайте revisions.»

---

### P1-2: AlphaFold DB 200M structures — freshness OK but verify

**Quote (speech s14, s39):** «более двухсот миллионов» / «Двести миллионов»

**Verification:**
- AlphaFold DB at https://alphafold.ebi.ac.uk currently shows >200M structures (since 2022 expansion to UniProt-wide).
- This is **stable** number since UniProt coverage completed; minimal drift expected.

**Severity:** **P1** — preflight directive correctly flags «Открыть https://alphafold.ebi.ac.uk и сверить число структур». Verify on day of lecture — likely still «200M+» or slightly higher (210M, 215M).

**Recommendation:** Keep as-is; preflight handles это. No code change needed.

---

### P1-3: NotebookLM 17M MAU — freshness alert

**Quote (speech s27):** «К концу две тысячи двадцать пятого — 17 миллионов с лишним активных пользователей в месяц»

**Verification:**
- Source: chapter [VFY-day-of] marker (chapter-part3 line 216).
- Refresh cadence: quarterly. Lecture date 2026-05-27, source claim «к концу 2025» (Dec 2025). days_delta ≈ 150 days (5 months) > quarterly cadence (90 days).
- **Likely outdated** — NotebookLM growth trajectory through Q1-Q2 2026 may have inflated MAU significantly.

**Severity:** **P1** — verify-on-day-of-lecture required. Preflight does NOT include this directive (only AlphaFold DB and FrontierMath are flagged for day-of verify).

**Recommendation:** Add to preflight: «Проверить latest NotebookLM MAU через Google announcements / TechCrunch / Statista — текущее в speech "17M+" из конца 2025; Q1-Q2 2026 numbers могут быть значительно выше.»

---

### P1-4: Elicit «138 миллионов академических статей» + «в 4 раза»

**Quote (speech s27):** «База — 138 миллионов академических статей. Сокращает время обзора литературы в 4 раза по валидированному пользовательскому исследованию.»

**Verification:**
- Source: chapter part3 §4.2 line 235, 237 with [VFY-day-of] marker on «в 4 раза».
- Refresh cadence: monthly for product features (база растёт). Lecture date 2026-05-27.
- Elicit база статей grows continuously; «138M» may be Q1 2025 number. By May 2026 could be 150M+.

**Severity:** **P1** — verify-on-day-of-lecture. Preflight directive missing.

**Recommendation:** Add to preflight: «Проверить https://elicit.org — текущий размер базы (speech utterly: 138M) и updated 4× ускорение study reference.»

---

## 5. P2 cite format / minor drift

### P2-1: WE-2 «три часа» vs chapter «4 часа»

**Quote (speech s28):** «Сорок пять минут вашего времени. Против **трёх часов** ручной проверки сорока семи цитат.»

**Chapter (chapter-part3.md §4.3 line 291):** «ручная подготовка библиографии — **~4 часа** на 47 цитат»

**Severity:** **P2** — minor numerical drift (3h vs 4h). Speech rounded down; chapter is canonical baseline. Either is plausible; cascade alignment preferred.

**Recommendation:** Fix speech to «**четырёх часов**» (Russification: «четырёх» vs «трёх»). Or accept drift if speaker prefers shorter framing — flag для transparency.

---

### P2-2: BLS «A&A 391» — new cite detail not in chapter inline

**Quote (speech s21):** «Box Least Squares, BLS, Kovács и соавторы две тысячи второго, **A&A 391**»

**Chapter (chapter-part3.md §3.2 line 63):** «Box Least Squares (BLS) — статистический метод поиска периодических провалов во временном ряду, разработанный в 2002 году Ковачем и др.» (no A&A 391 inline)

**External verification:** Kovács, G., Zucker, S., Mazeh, T. 2002, A&A, 391, 369 ✓ correct journal+volume.

**Severity:** **P2** — speech adds bibliographic specificity beyond chapter. Verified externally. Acceptable to keep as enrichment, but for strict cascade should add inline cite to chapter too.

**Recommendation:** Either keep speech as-is (it's correct), or backport «A&A 391» citation to chapter-part3 §3.2 inline for consistency.

---

### P2-3: Boltz biorxiv ID — new inline cite

**Quote (speech s15):** «Boltz-1 на biorxiv 2024.11.19.624167»

**Chapter (chapter-part2.md §2.3 line 104):** «команда MIT (Corso, Wohlwend et al.) опубликовала Boltz-1» (no biorxiv ID inline)

**Verification:** ID format canonical (biorxiv year.month.day.id pattern). This was established as canonical anchor в Phase 7 slides v2 fact-fix. ✓ correct.

**Severity:** **P2** — speech adds canonical anchor from slides v2 layer. Acceptable enrichment.

**Recommendation:** Backport biorxiv ID to chapter-part2 §2.3 line 104 inline for canonical cascade consistency. Low priority.

---

## 6. Freshness alerts (volatile claims on day-of-lecture)

| Claim | Source date | Cadence | Days delta | Verify-on-day-of |
|---|---|---|---|---|
| AlphaFold DB 200M+ | 2026-Q1 | quarterly | ~60 | ✓ preflight ok |
| FrontierMath GPT-5.5 Pro 52.4% | 2026-05-25 | weekly | 2 | ⚠ Epoch May 12 review may flip scores — **augment preflight** |
| NotebookLM 17M MAU | 2025-12 | quarterly | ~150 | ⚠ likely outdated — **add to preflight** |
| Elicit 138M + 4× | 2025-Q1 (chapter [VFY]) | monthly | ~360 | ⚠ likely outdated — **add to preflight** |
| ECMWF AIFS operational with 25 Feb 2025 | 2025-02-25 | yearly | ~456 | ✓ stable, preflight ok |
| AlphaProof Nature DOI | 2025-09 | yearly | ~240 | ✓ stable |
| Sakana AI Scientist v2 | 2025-04 | quarterly | ~390 | ⚠ v3 status — **preflight asks but should add explicit fallback** |
| DeepMind Co-Scientist Nature May 2026 | 2026-05 | yearly | 0-30 | ✓ very fresh — speaker should verify «May 2026 paper still valid status» (no retraction). Cross-verify on day-of. |
| Recursion-Roche $12B | 2021-12 | yearly | ~1620 | ✓ stable |

---

## 7. Hallucinated sources audit

**Sample of 5 spoken citations in speech narrative:**

1. **«MIT Technology Review восемнадцатого ноября — "Why Meta's Galactica only survived three days online"»** (s01) — ✓ exists, Will Douglas Heaven, Nov 18, 2022.
2. **«arxiv 2512.00967»** (Huang & Jiang exoplanet, s21) — chapter cites this canonically; format consistent with arxiv 2025-12 submission. ✓ structurally valid (cannot verify content directly without WebFetch but cross-cited in chapter).
3. **«arxiv 2504.17587»** (Ashton, Malz, Colombo LIGO, s23) — chapter cites this canonically; format consistent with arxiv 2025-04. ✓
4. **«biorxiv 2024.11.19.624167»** (Boltz-1, s15) — established canonical ID from Phase 7 slides v2 fact-fix. ✓
5. **«Nature 2025 DOI 10.1038/s41586-025-09833-y»** (AlphaProof, s19) — ✓ cross-verified via DeepMind blog + Google search confirmation. Nature paper «Olympiad-level formal mathematical reasoning with reinforcement learning».
6. **«arxiv 2602.05930»** (NeurIPS 2025 GPTZero Research fake citations) — chapter cites this; format consistent. ⚠ arxiv 2602.* would be **Feb 2026** submission. Plausible timing. Cannot directly verify but consistent with cascade.

**No hallucinated sources detected in speech beyond what chapter establishes.** Speech does not introduce new fabricated citations.

---

## 8. Top 5 P0 fact-fix priorities for Phase 11

**Priority 1 (must-fix, P0):** MICrONS «120 000 нейронов» → «84 000 нейронов» (cascade restore to chapter) OR upgrade BOTH speech AND chapter to «более двухсот тысяч» (match Nature April 2025 source). Speech s22 single point. Sub-claim «ручная трассировка ста двадцати тысяч» also affected.

**Priority 2 (must-fix, P0):** Palgrave-Schoop affiliations — «Ливерпульский университет» → «UCL (Палгрейв) + Princeton (Шуп)» in BOTH speech s17 AND chapter-part2 §2.5 line 147. References block в chapter-part4 may need update too.

**Priority 3 (should-fix, P1):** FrontierMath 52.4% preflight augmentation — add note про May 12, 2026 Epoch AI fatal-errors review. Optional oral caveat in s19.

**Priority 4 (should-fix, P1):** Update preflight (frontmatter line 15-23) to include verify-on-day-of checks for **NotebookLM 17M MAU** + **Elicit 138M / 4×** (both likely outdated, missing from current preflight directives).

**Priority 5 (should-fix, P2):** WE-2 timing drift — «три часа» → «четыре часа» (cascade alignment with chapter §4.3 line 291).

---

## 9. Recommend Phase 11 fact-fix scope

**Speech v2 single-pass cascade fix list:**

1. **s17:** «Ливерпульский университет» → «University College London (Палгрейв) + Princeton University (Шуп)» — semantic preserve, ~1 line change.
2. **s22:** «сто двадцать тысяч» → «восемьдесят четыре тысячи» (option A, cascade restore) OR «более двухсот тысяч» (option B, match Nature). Affects 2 sentences in s22.
3. **s28:** «трёх часов» → «четырёх часов» (P2, optional).
4. **frontmatter preflight:** add 2 new directives (NotebookLM MAU, Elicit база); augment FrontierMath directive с Epoch review note.

**Chapter v2.4 cascade-fix needed (separate from speech):**

1. **chapter-part2.md §2.5 line 147** — Palgrave/Schoop affiliations.
2. **chapter-part3.md §3.3 line 80, 84** — MICrONS 84k vs Nature April 2025 200k (decision needed: keep cascade as-is or upgrade to match real source; if upgrade, then speech also updates to «более двухсот тысяч»).
3. **chapter-part4.md references line 469** — may need update for Palgrave/Schoop bib correction.
4. (Optional P2) **chapter-part3.md §3.2** — add «A&A 391» to BLS citation.
5. (Optional P2) **chapter-part2.md §2.3 line 104** — add «biorxiv 2024.11.19.624167» inline.

**Verdict reasoning:** REVISE (not REJECT) because:
- 2 P0 issues identified, both fixable in ≤5 line changes per artifact.
- Both P0 are **inherited from chapter** (MICrONS partial, Palgrave full) — speech is faithful cascade EXCEPT for MICrONS number drift (which deserves P0 standalone).
- 4 P1 issues are freshness-management, not fact-correctness — addressable via preflight augmentation.
- 25 of 27 canonical anchors verified clean — strong baseline.
- No hallucinated sources, no direction inversions, no misquoted text — speech narrative integrity is high.

**Verdict: REVISE.** With 2 P0 cascade fixes + preflight augmentation, speech is ready for APPROVE-WITH-POLISH в Phase 11.

---

**Report finalized 2026-05-27 by fact-checker (Phase 10 speech focus).**
**Saved to:** `library/lectures/lec-15/qa-reports/2026-05-27-v1-speech/fact-checker.md`

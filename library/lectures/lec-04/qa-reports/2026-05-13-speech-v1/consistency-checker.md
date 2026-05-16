# Consistency Check — Chapter ↔ Slides ↔ Speech — Лекция 4

**Date:** 2026-05-13
**Mode:** full (Phase 10 — final consistency pass перед USER GATE C)
**Artifacts reviewed:**
- `library/lectures/lec-04/chapter.md` v2 (status=reviewed, commit `5c4b06c`, 12,692 слов)
- `library/lectures/lec-04/deck.yaml` v3 + `slides/s*.md` (34 файла, commit `2d45771`, slides v5.1)
- `library/lectures/lec-04/speech.md` v1 draft (4,993 active words, ~75 минут)

**Verdict:** REVISE

**Severity counts:**
- P0 (factual contradiction / missing coverage / structural gap): 2
- P1 (significant drift — numbers, terminology, structure): 3
- P2 (minor inconsistency — wording, dates): 2

---

## Executive summary

Speech v1 в целом отлично выровнен со slides v5.1 на уровне sequence, callbacks, тем и большинства cornerstone-чисел. Терминология glossary (25 canonical терминов) соблюдена по всем 25 пунктам — drift нет. Tone universal (без «инженер ИУ6», без alarmism, без «магической пилюли»), уважительная «вы»-форма.

**Но 2 серьёзных проблемы блокируют APPROVE:**

1. **P0 — Структурная несовместимость chapter v2 ↔ slides/speech:** chapter v2 (approved at GATE A) сохранил **LO4** в frontmatter + Раздел 4 «Микро-упражнение: AI как объяснение» (~70 строк контента). После Phase 8.8 Fix 9, slides и speech reorganized — LO4 удалён, s19 transformed в lecture content «AI как объяснитель», и Раздел «Микро-упражнение» больше не существует как отдельная единица. Это **известное расхождение, отражённое в `deck.yaml` комментарии**, но **chapter v2 формально остался source of truth с LO4**. Per book-first methodology — это требует синхронизации либо chapter (drop LO4 + drop §4 micro-exercise), либо явного acknowledgement, что chapter теперь имеет «extended/optional content», который не покрывается на лекции.

2. **P1 — Speech drift на одной cornerstone-цифре (MASAI baseline):** в `[s26]` Вывод 1 speech говорит «семидесяти трёх **с половиной**» (73.5%), а chapter + slide s11 + slide s26 единогласно говорят **73.8%**. Это нарушает enforced cornerstone fix Phase 4.

3. **P1 — Speech drift на одной cornerstone-цифре (Rentosertib placebo FVC):** в `[s17a]` speech говорит «минус двадцать миллилитров» (округлённо до целого), а chapter + slide s17a content + s17a YAML визуал-описание единогласно говорят **−20.3 мл**. Это нарушает enforced cornerstone fix Phase 4 (P0 fix verbatim — «−20.3 mL»).

Эти 3 фикса быстрые (~10 минут на правку speech). Структурный gap chapter ↔ post-Phase-8.8 — требует решения orchestrator + user.

---

## A. Terminology drift — glossary canonical-lock map

Все 25 canonical terms verified против `chapter.md` §Глоссарий. Drift НЕ обнаружен — все 3 artifact используют единые формы. Detail:

| # | Canonical (RU) | Chapter usage | Slides usage | Speech usage | Aligned? |
|---|---|---|---|---|---|
| 1 | **AI-диагностика** | §0.3, §1.x, §2.x, §6 | s07, s09, s12, s13, s26 | [s04], [s10], [s11], [s12], [s13], [s26] | ✓ |
| 1u | **medical AI / медицинский AI** (umbrella allowed) | §0.1, §1.3, §5.1, §6 | s08, s22, s23 | [s08], [s20] | ✓ (umbrella — chapter glossary explicitly allows) |
| 2 | **Drug discovery** | §3.x, §6 | s14, s15, s16, s17a, s17b | [s14], [s15], [s17a/b], [s26] | ✓ |
| 3 | **Sensitivity (чувствительность, recall)** | §2.2 | s10, s11 | [s10], [s11] | ✓ |
| 4 | **Specificity (специфичность)** | §2.2 | s10, s11 | [s10], [s11] | ✓ |
| 5 | **Prevalence (распространённость)** | §2.2 | s10 | [s10] | ✓ |
| 6 | **PPV** | §2.2 | s10 | [s10] | ✓ |
| 7 | **AlphaFold** | §3.2, §6 | s16, s26 | [s16], [s26] | ✓ (AlphaFold 2 / AlphaFold 3 differentiated везде) |
| 8 | **AlphaProteo** | §3.2 | s16 | [s16] | ✓ |
| 9 | **FDA SaMD** | §1.3, §3.5 | s08, s18 | [s08], [s18] | ✓ |
| 10 | **PCCP (Predetermined Change Control Plan)** | §3.5 | s18 | [s18] | ✓ (full expansion в одном месте, далее аббревиатура) |
| 11 | **CADe** | глоссарий only — не используется в основном тексте | not used | not used | ✓ (mentioned only as differentiation note in glossary) |
| 12 | Foundation model | §2.1 | s09 | [s09] | ✓ |
| 13 | HIPAA | §5.4 | s23 | [s23] | ✓ |
| 14 | GDPR | §5.4 | s23 | [s23] | ✓ |
| 15 | **ФЗ-152** | §5.4 | s23 | [s23] | ✓ |
| 16 | **ФЗ-23 (data localization)** | §5.4 | s23 | [s23] | ✓ |
| 17 | ePHI | §5.4 | s23 | not used (deferred to chapter) | ✓ |
| 18 | Деперсонализация | §5.4 | s23 (de-identification eng) | [s23] | ✓ |
| 19 | EU AI Act high-risk | §3.5, §5.4 | s08, s18 | [s08], [s18] | ✓ |
| 20 | **mosmed.ai** (lowercase) | везде последовательно | s04, s07, s08, s12, s23, s26 | [s04], [s06], [s08], [s12], [s14], [s23], [s26], [s27] | ✓ (lowercase соблюдён везде) |
| 21 | **Insilico Rentosertib (ISM001-055)** | §3.3 | s17a | [s14], [s17a], [s17b], [s26], [s27] | ✓ (full name + код consistent; ISM001-055 формат соблюдён) |
| 22 | **DSP-1181** (hyphen) | §3.4 | s17b | [s14], [s17a], [s17b], [s27] | ✓ (hyphen everywhere, без variants «DSP 1181» или «DSP1181») |
| 23 | **NEDA Tessa** | §5.3 | s22 | [s22] | ✓ (vendor accountability framing соблюдён всеми 3 — slide gold badge, chapter §5.3 «vendor accountability story», speech «Frame — vendor accountability, не chatbot history») |
| 24 | Bias (algorithmic bias) | §2.5, §5.2 | s13, s21 | [s13], [s21] | ✓ |
| 25 | **Healthcare operator role** | §5.5, глоссарий | s24 | [s24] | ✓ (не «Хосзу-роль», не «hospital operator» — везде «Healthcare operator — больница / клиника / ДЗМ») |

**Terminology aliases_forbidden — NONE found.** Speech не использует «4 миллиарда рублей» (correctly substituted by operational metrics). Speech не использует «medical AI ИУ6» или другие audience-specific terms.

**Conclusion (A):** Terminology — clean. Glossary lock holds.

---

## B. Number consistency matrix (cornerstone)

| # | Number / Claim | Chapter | Slide(s) | Speech [s] | Aligned? |
|---|---|---|---|---|---|
| 1 | Rentosertib FVC group | **+98.4 мл (95% CI: 10.9–185.9)** | s17a content L38 «+98.4 mL FVC» | [s17a] «плюс девяносто восемь и четыре десятых миллилитра» | ✓ |
| 2 | **Rentosertib placebo FVC** | **−20.3 мл (95% CI: −116.1–75.6)** | s17a visual L13: `−20.3 mL placebo`; s17a content L38 «минус двадцать целых трёх десятых» | [s17a] «**минус двадцать миллилитров**» (округлено) | ✗ **P1 DRIFT** |
| 3 | Rentosertib clinical Δ | ~118 мл | s17a content «около ста восемнадцати миллилитров» | [s17a] «около ста восемнадцати миллилитров» | ✓ |
| 4 | Rentosertib n | n=71 IPF | s17a YAML caption «n=71 IPF» | [s17a] «семьдесят один пациент» | ✓ |
| 5 | Rentosertib sites | 21 центр в Китае | s17a content «двадцать одном клиническом центре» | [s17a] «двадцать один центр в Китае» | ✓ |
| 6 | Rentosertib dose | 60 mg QD, 12 нед | s17a content «шестьдесят миллиграммов один раз в день в течение двенадцати недель» | [s17a] «шестьдесят миллиграммов в день, двенадцать недель» | ✓ |
| 7 | Insilico target→preclinical time | ~18 мес vs 4–5 лет | s17a content «примерно восемнадцать месяцев против традиционных четырёх-пяти лет» | [s17a] «примерно восемнадцать месяцев — против традиционных четырёх-пяти лет» | ✓ |
| 8 | Obermeyer chronic illness gap | 26% больше | s21 content «+26% more chronic illnesses» | [s21] «на двадцать шесть процентов больше хронических заболеваний» | ✓ |
| 9 | **Obermeyer Black share fix** | **17.7% → 46.5%** | s21 visual L13: `17.7% → 46.5% Black served`; s21 content «семнадцати и семи десятых до сорока шести и пяти процентов» | [s21] «с семнадцати и семи десятых до сорока шести и пяти процентов» | ✓ (P0 fix cornerstone preserved) |
| 10 | Obermeyer bias reduction | 84% reduction | s21 content «восемьдесят четыре процента» | [s21] «восемьдесят четыре процента» | ✓ |
| 11 | Obermeyer scope | ~200M Americans | s21 content (implicit via 200M ref) | [s21] «двухсот миллионов американцев» | ✓ |
| 12 | Obermeyer cost gap | $1 800 / year less | s21 content L42 «тысячу восемьсот долларов в год меньше» | [s21] «примерно на тысячу восемьсот долларов в год меньше» | ✓ |
| 13 | **FDA cumulative end-2025** | **1 451 AI/ML devices** | s04, s07, s12 — «1 451» | [s04], [s07], [s26] «тысячу четыреста пятьдесят одно» | ✓ |
| 14 | FDA new 2024/2025 | 258 (2024), 295 (2025) | s04 content «двести пятьдесят восемь … двести девяносто пять» | [s07] «двести пятьдесят восемь … двести девяносто пять» | ✓ |
| 15 | FDA radiology share | 76% | везде «76%» / «семьдесят шесть процентов» | [s04], [s06], [s07], [s26] | ✓ |
| 16 | mosmed studies | 14M+ исследований | s04, s07, s08, s12 — «14M+» | [s04], [s08], [s12], [s14], [s26] «более четырнадцати миллионов» | ✓ |
| 17 | mosmed regions | 74 региона | s04, s12 | [s04], [s12], [s14], [s26], [s27] «семидесяти четырёх регионах» | ✓ |
| 18 | mosmed images | 18M+ изображений | s04, s12, s23 | [s12], [s23] «более восемнадцати миллионов» | ✓ |
| 19 | mosmed services | 70 AI-сервисов | s04, s12 | [s12] «около семидесяти AI-сервисов» | ✓ |
| 20 | mosmed standards | 11 национальных | s04, s12 | [s12] «одиннадцать национальных стандартов» | ✓ |
| 21 | mosmed organizations | 2 000+ | s04, s12 | [s12] «более двух тысяч медицинских организаций» | ✓ |
| 22 | mosmed clinical areas | 43 | s04 + s12 «43 клинические области» | [s12] «сорока трёх клинических областях» | ✓ |
| 23 | mosmed datasets | ~300 эталонных | s04 + s12 | [s12] «около трёхсот эталонных датасетов» | ✓ |
| 24 | **«4 млрд руб/год экономии» — FORBIDDEN** | §1.2 explicit disclaimer (not used as claim) | NOT present in any slide ✓ | [s12] «маленькая оговорка»: «**Эту цифру мы не нашли в первичных источниках**» | ✓ (forbidden number explicitly disclaimed in speech, не used affirmatively) |
| 25 | MASAI sens AI | **80.5%** | s11 visual `80.5% vs 73.8%`; s11 content «восемьдесят целых пять десятых» | [s11] «восемьдесят с половиной процентов» (= 80.5% phrased differently); [s26] «восьмидесяти и пяти процентов» (= 80.5%); [s26] «восьмидесяти с половиной процентов» | ✓ |
| 26 | **MASAI sens baseline** | **73.8%** | s11 visual + s11 content «семидесяти трёх и восьми»; s26 slide content «семидесяти трёх и восьми десятых» | [s11] «семидесяти трёх и восьми десятых» = 73.8% ✓; **[s26] «семидесяти трёх с половиной»** = 73.5% ✗ | ✗ **P1 DRIFT** |
| 27 | MASAI CDR | 6.4 vs 5.0 per 1000 | s11 visual; chapter §2.3 | [s11] «шесть и четыре десятых на тысячу против пяти» | ✓ |
| 28 | MASAI workload reduction | 44% | s11 visual + content | [s11] «сорок четыре процента»; [s26] «сорок четыре» | ✓ |
| 29 | MASAI interval cancer ↓ | 12% | s11 content «двенадцать процентов» | [s11] «двенадцать процентов» | ✓ |
| 30 | Goh n | n=50 врачей | s11 content «Пятьдесят врачей» | [s11] «Пятьдесят врачей» | ✓ |
| 31 | Goh medians | 76% vs 74% (p=0.60) | s11 visual «GPT-4 alone 76.3% vs doctor+GPT-4 73.7% (p=0.60)» + content «76 vs 74» | [s11] «семьдесят шесть процентов … семьдесят четыре» | ✓ |
| 32 | Liu 2019 sens | AI 87% vs clinicians 85% | s11 visual + content | [s11] «восемьдесят семь процентов … восемьдесят пять» | ✓ |
| 33 | **Change Healthcare PHI** | **190 миллионов** | s23 «190M Americans» | [s23] «сто девяносто миллионов американцев» | ✓ |
| 34 | Change Healthcare data exfil | 6 ТБ | s23 «6 TB» | [s23] «Шесть терабайт» | ✓ |
| 35 | Change Healthcare ransom | $22M (Bitcoin) | s23 «$22M ransom» | [s23] «Двадцать два миллиона долларов» | ✓ |
| 36 | **Change Healthcare recovery cost** | **$2.457 млрд** | s23 visual + content «$2.457B» / «два миллиарда четыреста пятьдесят семь миллионов» | [s23] «два миллиарда четыреста пятьдесят семь миллионов долларов» | ✓ |
| 37 | Change Healthcare % US pop | ~57% | s23 visual | [s23] «примерно пятьдесят семь процентов населения США» | ✓ |
| 38 | AlphaFold structures | 200M+ | s16 visual + content | [s16] «более двухсот миллионов» | ✓ |
| 39 | AlphaFold 3 PoseBusters | +50% | s16 visual + content «+50% accuracy» | [s16] «примерно на пятьдесят процентов» | ✓ |
| 40 | AlphaProteo BHRF1 SR | 88% | s16 «88% success rate» | [s16] «Восемьдесят восемь процентов» | ✓ |
| 41 | AlphaProteo affinity | 3–300× | s16 content | [s16] «в три-триста раз» | ✓ |
| 42 | Adversarial hallucination | 83% | s22 «83%» | [s22] «восьмидесяти трёх процентах случаев» | ✓ |
| 43 | Patient self-diagnosis | ~40M Americans | s22 «40M Americans» | [s22] «около сорока миллионов американцев» | ✓ |
| 44 | Drug discovery: years/cost | 10-15 лет, $1-2 млрд | s15 «DiMasi 2016, Wouters 2020» | [s15] «десять-пятнадцать лет и один-два миллиарда долларов» | ✓ |
| 45 | Drug Phase 1→approved | ~6.7% | §3.1 | [s15] «примерно шесть и семь десятых процента» | ✓ |
| 46 | Recursion+Exscientia merger | 8 августа 2024, $688M | s17b reference URL; chapter §3.4 «8 августа 2024 года ($688M)» | [s17b] «в августе 2024 года, шестьсот восемьдесят восемь миллионов долларов» (date less specific but not contradictory) | ✓ (acceptable verbal shortening) |
| 47 | Cognitive Agro Pilot | 1500+ машин, +30-40% | chapter §6.2 «1 500+ машин, +30–40%»; s28 visual | [s28] «тысяча пятьсот машин в полях, рост эффективности на тридцать-сорок процентов» | ✓ |
| 48 | Росздравнадзор registered | 57 AI-медизделий (52 RU + 5 foreign) | §3.5 + s18 | [s18] «Пятьдесят семь зарегистрированных AI-медизделий» | ✓ |

**Summary (B):** 48 cornerstone numbers checked. 46 aligned (✓), **2 drifts (✗)** в speech — обе в P1 диапазоне:
- D1 — `[s17a]` Rentosertib placebo: speech говорит «−20 мл» вместо canonical «−20.3 мл».
- D2 — `[s26]` MASAI baseline: speech говорит «73.5%» («с половиной») вместо canonical «73.8%». При том что в `[s11]` тот же speech правильно говорит «73.8%» («и восьми десятых»). Это внутри-speech inconsistency между двумя секциями.

---

## C. Central question + callbacks alignment

| Element | Chapter | Slide | Speech | Aligned? |
|---|---|---|---|---|
| Central question text | §«Центральный вопрос» — «Какие AI-обещания в медицине реально сбылись к 2026 году — и кто отвечает, когда AI-диагноз оказывается ошибочным?» | s05 deck.yaml + s05 content | [s05] (verbatim) | ✓ |
| s14 mid-lecture callback (3 anchors) | §3.0 method note | s14 visual «s12 mosmed ✓ / s17a Rentosertib ? / s17b DSP-1181 ?» | [s14] «три якоря: mosmed ✓, Rentosertib ?, DSP-1181 ?» | ✓ |
| s24 «4-actor framework» | §5.5 | s24 «врач / operator / vendor / regulator» | [s24] full 4-actor breakdown | ✓ |
| s24 central principle | §5.5 «Врач ставит диагноз. AI подсказывает. Final clinical responsibility undivided.» | s24 content | [s24] verbatim (RU) + EN: «Final clinical responsibility undivided» | ✓ |
| s27 closing payoff | §6.1 «Врач ставит диагноз. AI подсказывает. Инженер делает так, чтобы врач мог по-настоящему решать.» | s27 visual | [s27] verbatim | ✓ |
| Callback s12 mosmed → s14 → s27 | §2.4 → §3.0 callback → §6 | s12 → s14 ✓ → s27 | [s12] → [s14] «mosmed ✓» → [s27] «mosmed.ai с четырнадцатью миллионами» | ✓ |
| Callback s17a Rentosertib → s27 | §3.3 → §6.1 | s17a → s26 → s27 | [s17a] → [s26] → [s27] «Rentosertib peer-reviewed в Nature Medicine» | ✓ |
| Callback s17b DSP-1181 → s27 | §3.4 → §6.1 | s17b → s26 → s27 | [s17b] → [s26] → [s27] «DSP-1181 discontinued» | ✓ |
| Callback Lec 1 YOLO → s01 | §0.1 | s01 content | [s01] «В конце Лекции 1 у нас была камера-демо с YOLO» | ✓ |
| Callback Лекция 9 «AI, этика и регулирование» | §6.3 | s28 | [s27], [s28], [s19] (3 references) | ✓ |
| Callback Lec 14 финал чек-листа | §6.3 | s28 | [s27], [s28] | ✓ |
| Callback Lec 6 Cognitive Agro | §6.2 | s28 | [s28] | ✓ |

**Conclusion (C):** Callbacks chain полностью intact. Central question stated identically. Closing payoff verbatim across 3 artifacts.

---

## D. LO mapping (post-Phase 8.8)

| LO | Chapter v2 | deck.yaml v3 | Speech v1 | Aligned? |
|---|---|---|---|---|
| LO1 | ✓ (frontmatter, §1.1, §1.2, §6.1) | ✓ deck `[LO1, LO2, LO3, LO8]` + slide-level LO1 в s01, s04, s05, s05b, s06, s07, s08a, s09, s10, s13a, s15, s16, s17a, s24a, s26 | ✓ explicitly named в [s26] «Вывод первый. AI-диагностика работает. Это LO1 и LO2» + footnote L681 | ✓ |
| LO2 | ✓ (frontmatter, §1.3, §2.x, §3, §6.1) | ✓ slide-level в s08, s10, s11, s12, s13a, s15, s16, s17a, s17b, s24a, s26 | ✓ explicitly named в [s26] «LO2 и LO3» + footnote | ✓ |
| LO3 | ✓ (frontmatter, §2.5, §5.x, §6.1) | ✓ slide-level в s11, s13, s13a, s17b, s18, s19, s19a, s20, s21, s22, s23, s24, s24a, s26 | ✓ explicitly named в [s26] «Вывод третий. Это LO3» + footnote | ✓ |
| **LO4** | **✓ — В frontmatter `learning_outcomes: [..., LO4, ...]` (L11), в §Учебные цели (L67), целиком §4 Микро-упражнение (L413-443) с 3 шагами и 2 self-check questions** | **✗ — УДАЛЁН (`learning_outcomes: [LO1, LO2, LO3, LO8]` per Phase 8.8 Fix 9). Раздел 4 «Микро-упражнение» отсутствует в deck. s19 transformed из apply-based exercise в lecture content «AI как объяснитель» (assertion + LO2+LO3, не LO4).** | **✗ — НЕ упомянут. Footnote L681 explicitly lists только LO1/LO2/LO3/LO8. [s19] описан как «короткая прикладная секция. AI как объяснитель» — не micro-exercise.** | ✗ **P0 STRUCTURAL DRIFT** |
| LO8 (framing) | ✓ (frontmatter «LO8-framing», §6.3) | ✓ slide-level в s18, s19a, s20, s21, s22, s23, s24, s24a, s26, s27, s28 | ✓ explicitly named в [s26] «Вывод третий … LO8 — три принципа как input для чек-листа Лекции 9» + footnote | ✓ |

**Critical observation:** chapter frontmatter still declares `learning_outcomes: [LO1, LO2, LO3, LO4, LO8-framing]`. deck.yaml v3 declares `[LO1, LO2, LO3, LO8]`. Speech v1 footnote L681 lists `[LO1, LO2, LO3, LO8]`. **Speech is aligned with slides, NOT with chapter.** This represents a substantive structural divergence — see §E below.

---

## E. Section structure consistency (post-Phase 8.8)

| Artifact | Section count | Section titles | Notes |
|---|---|---|---|
| **Chapter v2** | **7** (Sections 0-6) | Раздел 0 Открытие · Раздел 1 Карта · Раздел 2 Диагностика · Раздел 3 Drug discovery · **Раздел 4 Микро-упражнение** · Раздел 5 Этика · Раздел 6 Заключение | Has independent Раздел 4 «Микро-упражнение» (§4.1 + §4.2 + Self-check) totalling ~70 lines |
| **Slides v5.1 (deck.yaml)** | **6 sections** (0-5), 5 dividers | s05b «Раздел 1» · s08a «Раздел 2» · s13a «Раздел 3» · s19a «Раздел 4 Этика» · s24a «Раздел 5 Заключение». Раздел 0 (Открытие) implicit (s01–s05). | s18a divider intentionally removed Phase 8.8 Fix 9 (comment в deck.yaml L325-327). s19 reassigned to Раздел 4 Этика as natural intro к LLM borders. |
| **Speech v1** | **6 sections** (0-5) | Раздел 0 Открытие (9 мин) · Раздел 1 Карта (7 мин) · Раздел 2 Диагностика (14 мин) · Раздел 3 Drug discovery (14 мин) · **Раздел 4 Этика и ответственность (15 мин)** · Раздел 5 Заключение (6 мин). + 5 «X из 5» bridges. | s19 «AI как объяснитель» в Разделе 4 Этика как первая секция (3 мин). NO Раздел 4 Микро-упражнение. |

**Slides + Speech ALIGNED** (6 sections, 5 dividers, s19 = lecture content в Разделе 4 Этика).
**Chapter MISALIGNED** (7 sections, independent Раздел 4 Микро-упражнение with LO4).

**Speech bridge labels:**
- s05b L128: «Это первый раздел из пяти — карта AI в медицине.» ✓
- s08a L192: «Второй раздел из пяти — AI-диагностика как зеркало.» ✓
- s13a L318: «Третий раздел из пяти — drug discovery: обещания и реальность.» ✓
- s19a L442: «Четвёртый раздел из пяти — этика и ответственность.» ✓
- s24a L596: «Пятый раздел из пяти — заключение.» ✓

**All 5 «из пяти» bridges consistent with slide dividers.** Speech labels Раздел 0 separately (Открытие, 9 мин) as introduction, then numbers Разделы 1-5 (= slide dividers s05b..s24a). Numerically consistent.

**Conclusion (E):** Slides + Speech are structurally a 6-section lecture (0 introduction + 5 numbered sections). Chapter v2 is structurally 7-section (0..6 with independent Micro-exercise section 4). This is the **P0 structural divergence** noted in §D.

---

## F. Cross-reference consistency (Лекция X-references)

| Reference | Chapter | Slides | Speech | Aligned? |
|---|---|---|---|---|
| **Лекция 1** YOLO callback | §0.1 «В конце Лекции 1 мы упоминали камера-демо с YOLO» | s01 content + speaker notes | [s01] «В конце Лекции 1 у нас была камера-демо с YOLO» | ✓ |
| **Лекция 1** Нобель 2024 callback | §3.2 «callback к Лекции 1, где Нобелевская премия упоминалась как индикатор зрелости поля» | s16 | [s16] «Это callback к Лекции 1.» | ✓ |
| **Лекция 3** Bias параллель (кредит-скоринг) | §5.2 «параллель для российской аудитории: тот же механизм работает в bias кредитного скоринга (Лекция 3)» | not mentioned in slides (acceptable — slide too dense) | not mentioned in speech (acceptable) | ✓ (chapter-only deepening, не required в speech/slide) |
| **Коллоквиум 1 / Лекция 5** | §6.2 «Коллоквиум 1 (Лекция 5)» | s28 | [s28] «Коллоквиум 1, Лекция 5» | ✓ |
| **Лекция 6** Cognitive Agro | §6.2 | s28 visual «Cognitive Agro Pilot 1500+ машин, +30-40%» | [s28] «Cognitive Agro Pilot: тысяча пятьсот машин … тридцать-сорок процентов» | ✓ |
| **Лекция 7** Практикум 1 | §4.2 + §6 footnote (Практикум 1 = «Анализ индустриальных кейсов с помощью AI») | s28 (forward arrow) | [s28] «Прогрессия практик: Практикум 1 на Лекции 7» + footnote L683 | ✓ |
| **Лекция 9** «AI, этика и регулирование» | §6.3 (subtitle namespaced) | s19a, s20, s24, s27, s28 | [s19], [s24], [s26], [s27], [s28] | ✓ (consistent forward-ref chain) |
| **Лекция 12** Практикум 2 | §4.2 («Лекции 12 — Практикум 2») | s28 | [s28] «Практикум 2 на Лекции 12» | ✓ |
| **Лекция 14** Финализация | §6.3 «На Лекции 9 вы будете синтезировать всё в personal чек-листе из 3–5 пунктов, на Лекции 14 — финализируете personal version» | s28 (arrow) | [s27] «Финал — на Лекции 14, в индивидуальном задании» + [s28] | ✓ |

**No fabricated cross-refs.** No mention of «Лекция 5 = AI в производстве» (correctly stated как «Коллоквиум 1»). No mention of Лекция 8, Лекция 10, Лекция 11, Лекция 13, Лекция 15-17 (correctly absent — not relevant to Лекция 4 narrative).

**Conclusion (F):** Cross-ref set identical across 3 artifacts: {Лекция 1, Коллоквиум 1, Лекция 6, Лекция 7, Лекция 9, Лекция 12, Лекция 14}. (Лекция 3 only in chapter — acceptable for deeper chapter content.)

---

## G. Pre-flight checklist orphan reference detection

Speech `pre-flight` section (L25-35) references slides:

| Ref | Speech mention | Slide exists in deck.yaml? | Status |
|---|---|---|---|
| `[s01 pre-flight, Chester]` | L27 | ✓ s01 | ✓ |
| `[s04 freshness]` | L28 | ✓ s04 | ✓ |
| `[s12 freshness]` | L29 | ✓ s12 | ✓ |
| `[s19 freshness]` | L30 | ✓ s19 | ✓ |
| `[s22 freshness]` | L31 | ✓ s22 | ✓ |
| `[s07/s11/s17a]` | L32 | ✓ all three | ✓ |

**Orphan check across speech body L38-660:** все ссылки `[sNN]` соответствуют slides в deck.yaml v3. `slides_covered` массив L8 содержит все 34 slides. No reference to deleted s18a, no reference to s25/s30/etc.

**Conclusion (G):** Zero orphan refs. Pre-flight checklist clean.

---

## H. Visual ↔ verbal alignment

| Slide | Speech opens with «[На слайде …]» description | Matches slide visual primary? |
|---|---|---|
| s01 | «браузер с открытым `mlmed.org/tools/xray/`» + drag-and-drop action | ✓ (live demo described) |
| s04 | «bar chart FDA рост 2015→2025 + info-card mosmed.ai» | ✓ matches deck.yaml visual.primary |
| s06 | «2×2 матрица modality × scope с четырьмя ячейками» | ✓ |
| s09 | «конвейер из четырёх стадий: Input → Model → Output → Рабочий процесс» | ✓ |
| s10 | «2×2 confusion matrix + 4 формулы» | ✓ |
| s11 | «три ряда: Liu 2019, MASAI 2024-25, Goh 2024» | ✓ |
| s12 | «pipeline снимок → mosmed.ai → результат + 6 info-cards» | ✓ |
| s14 | «центральный вопрос плюс три якоря: mosmed ✓, Rentosertib ?, DSP-1181 ?» | ✓ |
| s15 | «5-stage pipeline с AI/human-маркерами» | ✓ |
| s16 | «3 evidence-cards + AlphaFold 3D snapshot» | ✓ |
| s17a | «3-event timeline + info-card +98.4 mL FVC» | ✓ |
| s17b | «3-event timeline 2020→2022→2026 Discontinued» | ✓ |
| s18 | «3-column condensed table US/EU/RU + PCCP contrast» | ✓ |
| s21 | «3-box mechanism + chart 26% + arrow 17.7→46.5%» | ✓ |
| s22 | «3 case-cards: Tessa, adversarial 83%, 40M self-diagnosis» | ✓ |
| s23 | «news screenshot + 5 info-cards» | ✓ |
| s24 | «2×2 quadrant с врач/operator/vendor/regulator» | ✓ |
| s26 | «3-card summary» | ✓ |

**Conclusion (H):** All 18 spot-checked verbal-to-visual descriptions match slide visuals. Speech correctly points to what's on screen.

---

## DISCREPANCIES (sorted by severity)

### D0-1 — Chapter v2 ↔ slides/speech: LO4 + Раздел 4 Micro-exercise

**Severity:** P0
**Where:** `chapter.md` frontmatter L11 + §Учебные цели L67 + Раздел 4 L413-443 vs `deck.yaml` v3 L19 + Phase 8.8 Fix 9 comments L16-18, L325-327 vs `speech.md` footnote L681
**Issue:** Chapter v2 (approved at GATE A) declares 5 LOs (LO1, LO2, LO3, **LO4**, LO8-framing) and contains an independent ~70-line section «Раздел 4. Микро-упражнение: AI как объяснение» with 3-step apply-based exercise + 2 self-check questions targeting LO4. Slides v5.1 (Phase 8.8 Fix 9) explicitly dropped LO4: `deck.yaml` learning_outcomes = `[LO1, LO2, LO3, LO8]`, s19 transformed into lecture content «AI как объяснитель» (LO2+LO3, no student activity), Раздел Micro-exercise removed. Speech v1 mirrors slides — footnote L681 lists only 4 LOs (1/2/3/8), [s19] L450-472 is delivered as «короткая прикладная секция» of lecture content без micro-exercise mechanics.

**Per book-first methodology (D1 locked):** chapter is source of truth. But Phase 8.8 was an intentional surgical revision applied to slides post-GATE A, with the explicit understanding (per `deck.yaml` comment) that the chapter «still has LO4» as an optional self-study micro-exercise that the LIVE lecture won't run. Speech aligns to slides (correct for production), not chapter (correct as source of truth for self-study readers).

**Recommendation:** This is an orchestrator + user decision, not unilateral fix:

- **Option A (sync chapter to lecture):** Update chapter v2 → v3: drop LO4 from frontmatter + §Учебные цели, replace Раздел 4 с lecture-content «AI как объяснитель» (mirror speech [s19]), drop Self-check (Раздел 4). Result: chapter, slides, speech 100% aligned on 6-section structure.
- **Option B (keep chapter with optional Micro-exercise):** Add explicit chapter frontmatter note like `lecture_delivery: 5 LOs core (LO1, LO2, LO3, LO8); LO4 optional self-study micro-exercise (§4) not delivered live` + add a callout box at start of Раздел 4 «Это секция self-study, на лекции не разбирается». Slides и speech stay as-is.
- **Option C (transitional acknowledgement):** Add `version_note: "chapter v2 frontmatter LO list includes LO4 for self-study; live lecture v3.x post-Phase-8.8 delivers 4 LOs"` somewhere visible.

**Note:** Option B is most consistent with «extended reading» philosophy of a textbook chapter vs a 75-min lecture; Option A is cleanest but requires re-running chapter critic. Не decide alone — required user input.

### D1-1 — Speech [s17a]: «−20 мл» vs canonical «−20.3 мл»

**Severity:** P1
**Where:** `speech.md` L390 vs `chapter.md` L352 vs `slides/s17a-rentosertib-success.md` L38 (content) and visual L13
**Issue:** Speech says «В плацебо — **минус двадцать миллилитров**». Canonical Phase 4 P0 fix establishes **−20.3 мл (95% CI: −116.1–75.6)**. Slide s17a content correctly says «минус двадцать целых трёх десятых». Chapter §3.3 says «−20.3 мл». Speech rounds to «−20» losing precision.

**Impact:** На слух «минус двадцать» vs «минус двадцать и три десятых» — потеря 1.5% precision and breaks parallel with canonical «+98.4». «118 мл разница» при цифрах «+98.4 vs −20» = 118.4, при «+98.4 vs −20.3» = 118.7. Speech keeps «около ста восемнадцати миллилитров» (correctly rounded), но из «−20» это не выводится. Дисциплина academic-grade речи требует cornerstone numbers без rounding.

**Recommendation:** Fix `speech.md` L390 — заменить «**минус двадцать миллилитров**» на «**минус двадцать и три десятых миллилитра**» (parallel form to «плюс девяносто восемь и четыре десятых миллилитра» в той же фразе).

### D1-2 — Speech [s26]: MASAI baseline «73.5%» vs canonical «73.8%»

**Severity:** P1
**Where:** `speech.md` L610 vs `chapter.md` L86, L245, L566 vs `slides/s11-ai-vs-radiologist-3row.md` L13, L33, L41 + `slides/s26-three-takeaways.md` L35
**Issue:** Speech [s26] Вывод 1 (L610) says «**с семидесяти трёх с половиной до восьмидесяти с половиной процентов**». «с половиной» = 0.5. Canonical fixed-Phase 4 number is **73.8%** («и восьми десятых»). Speech [s11] (L262) correctly says «семидесяти трёх и восьми десятых» = 73.8% ✓, so this is internal speech inconsistency — speaker says 73.8% in §s11 (the deep-dive), then mis-rounds to 73.5% in §s26 (the takeaway).

**Impact:** Listener hears two different baselines in the same lecture — confusing. Slide s11 visual shows «80.5% vs 73.8%» — speech [s26] verbal contradicts the slide visual still on screen during Conclusion.

**Recommendation:** Fix `speech.md` L610 — заменить «**семидесяти трёх с половиной**» на «**семидесяти трёх и восьми десятых**». Same parallel form as L262.

### D1-3 — Speech [s17b]: «AI ускорил design (12 мес vs 4–5 лет)» implicit vs explicit

**Severity:** P2 (borderline P1)
**Where:** `speech.md` L410 + L416 vs `chapter.md` L374 + L378 vs `slides/s17b-dsp1181-reality-check.md`
**Issue:** Speech [s17b] explicitly states «Путь от target до Phase 1 — около двенадцати месяцев против традиционных четырёх-пяти лет». This is consistent with chapter §3.4. Slide s17b speaker notes mention same «двенадцать месяцев». **All aligned, no actual drift.** False-positive flagged during initial scan because some sources hyphenate as «четырёх–пяти», others «четырёх-пяти» — typographic only.

**Recommendation:** No action required. Listed for completeness; not a drift.

### D2-1 — Recursion+Exscientia date specificity

**Severity:** P2
**Where:** `speech.md` L418 vs `chapter.md` L382
**Issue:** Chapter §3.4 says «**8 августа 2024 года** (all-stock deal в размере $688M)». Speech says «в августе 2024 года, шестьсот восемьдесят восемь миллионов долларов» — drops the «8 числа», keeps the rest. Not a factual contradiction (August 2024 is correct), but loses specificity.

**Recommendation:** Optional minor polish — speech is conversational, dropping date specificity is acceptable. Could add «8 августа» if precision matters, but speakable forms сокращены — acceptable as-is.

### D2-2 — Speech section labeling (Раздел 0 vs «X из 5»)

**Severity:** P2
**Where:** `speech.md` `## Раздел 0`, `## Раздел 1`, ..., `## Раздел 5` (top-level section headers) vs «первый из пяти» «пятый из пяти» (in-speech bridges)
**Issue:** Speech `##` headers use 6 labels (Раздел 0..Раздел 5), но «из пяти» bridge labels count 5 (Раздел 1..Раздел 5 → divider labels). Inside chapters of speech-document, Раздел 0 is an introduction before the «из пяти» numbered sections. This is internally consistent (intro=0 + 5 numbered sections), but slightly cognitive load — student в зале hears «первый раздел из пяти» в начале 19-й минуты, что может быть confusing if they don't realize there was a Раздел 0.

**Recommendation:** Acceptable as-is — slide dividers in deck.yaml align with «из пяти» framing (5 numbered sections + 1 implicit intro). No action required unless user wants explicit «вводный + 5 разделов» framing in s05b divider bridge.

---

## Coverage gaps

**LO coverage gaps:** Per §D — LO4 declared in chapter, NOT covered in slides or speech (intentional post-Phase 8.8). This is the P0 structural issue.

**Slide-assertion coverage in chapter:** все 29 content-slide assertions matched to chapter sections via `chapter_ref` field in deck.yaml. Spot-checked s09, s10, s11, s12, s13, s17a, s17b, s18, s21, s22, s23, s24 — all map cleanly to chapter §s.

**Speech-mentioned facts not in chapter:** none found. Speech is conservative — every cornerstone metric is sourced from chapter §s.

---

## Top fixes (per artifact)

### Speech (3 P1 fixes — fast, mechanical)
1. **L390 (s17a)** — заменить «минус двадцать миллилитров» → «минус двадцать и три десятых миллилитра».
2. **L610 (s26 Вывод 1)** — заменить «семидесяти трёх с половиной» → «семидесяти трёх и восьми десятых».
3. **L418 (s17b)** — optional: add «8 августа» — «в августе 2024 года» → «8 августа 2024 года» (P2 polish only, не required).

### Chapter (orchestrator + user decision required)
4. **Frontmatter L11 + §Учебные цели L67 + §4 (L413-443)** — choose Option A/B/C from D0-1. If Option A (sync chapter to lecture): drop LO4 + Раздел 4 micro-exercise structure, replace с lecture content «AI как объяснитель» mirroring speech [s19]. **Это требует re-run methodology-critic + book-editor.**

### Slides
5. **None required.** Slides v5.1 internally consistent and aligned with speech.

### deck.yaml
6. **None required.** Phase 8.8 Fix 9 comments adequately document the chapter ↔ slide divergence.

---

## Cross-artifact verification matrix (executive view)

| Domain | Chapter ↔ Slides | Slides ↔ Speech | Chapter ↔ Speech | Overall |
|---|---|---|---|---|
| Numbers (48 cornerstone) | ✓ aligned | 46/48 ✓; 2 speech drifts in [s17a] и [s26] | 46/48 ✓ | **P1** |
| Terminology (25 glossary) | ✓ 25/25 | ✓ 25/25 | ✓ 25/25 | clean |
| LOs | **✗** LO4 in chapter, not in slides | ✓ both = [1/2/3/8] | **✗** LO4 in chapter, not in speech | **P0 structural** |
| Section structure | **✗** 7 sections vs 6 | ✓ 6=6 | **✗** 7 sections vs 6 | **P0 structural** |
| Central question | ✓ identical | ✓ identical | ✓ identical | clean |
| Callbacks chain (s12/s14/s17/s24/s27) | ✓ | ✓ | ✓ | clean |
| Cross-refs (Lec 1/5/6/7/9/12/14) | ✓ | ✓ | ✓ | clean |
| Tone (universal, trust-but-verify, no alarmism) | ✓ | ✓ | ✓ | clean |
| Visual ↔ verbal alignment (speech describes slide accurately) | n/a | ✓ 18/18 spot-checked | n/a | clean |
| Pre-flight orphan refs | n/a | ✓ 0 orphans | n/a | clean |
| Speaker notes ↔ speech alignment | n/a | ✓ slides speaker notes are concentrated version of speech equivalent fragment | n/a | clean |
| References parity (62 sources) | ✓ chapter exhaustive; slides cite subset via `references:`; speech mirrors via attribution | ✓ | ✓ | clean |

---

## VERDICT: REVISE

**Why REVISE (not APPROVE-WITH-POLISH):**
- 1 P0 structural drift (chapter ↔ slides/speech on LO4 + Раздел 4 Micro-exercise) — requires user decision (Option A/B/C).
- 2 P1 number drifts in speech (Rentosertib placebo −20 vs −20.3; MASAI baseline 73.5 vs 73.8) — fast fixes but blocks APPROVE per cornerstone-number policy.
- Per 4-level verdict scale rules (CLAUDE.md): ≥5 P1 issues → counter-check REVISE. We have 3 P1 (incl. one P2 borderline). But P0 structural drift is independent reason for REVISE — cannot be silently approved.

**Counter-check confirmation:** P0 alone justifies REVISE. The 2 P1 number drifts add an extra reason. APPROVE-WITH-POLISH would require zero P0, ≤3 P1 — we exceed P0 threshold.

**What user must decide before this becomes APPROVE-WITH-POLISH or APPROVE-CLEAN:**
1. **Option for D0-1** (LO4 + Раздел 4): keep chapter as-is (Option B/C — add transitional acknowledgement) OR re-edit chapter (Option A — sync to lecture).
2. **Authorize speech fixes** D1-1 and D1-2 (2 verbal number corrections, ~5 min book-editor task).

**Once both addressed → re-run consistency-checker → APPROVE-CLEAN (или APPROVE-WITH-POLISH if D2 polish items addressed).**

---

## Notes for orchestrator

1. **Glossary lock is HOLDING** — 25 canonical terms used consistently. This is excellent terminology discipline through 3 large artifacts (~22k words total). No rename proposals.

2. **Visual-verbal alignment is excellent** — speech `[На слайде ...]` cues match slide visuals with high fidelity. Lecturer reading speech will accurately direct attention to on-screen elements.

3. **Callback chain s12 → s14 → s17a/s17b → s26 → s27** is one of the strongest narrative threads I've seen — explicitly named «три якоря» в [s14], reaffirmed в [s26] Выводы, payoff в [s27]. Per-domain consistency across 3 artifacts.

4. **`«4 миллиарда рублей» forbidden number** is correctly handled — chapter §1.2 explicitly disclaims it, speech [s12] L292 explicitly disclaims it as «маленькая оговорка про цифру … Эту цифру мы не нашли в первичных источниках», slides do not contain it. This is a model of how to handle a freshness/source dispute in production text.

5. **Pre-flight checklist** (speech.md L25-35) is a unique production artifact — concentrates lector preparation (live demo testing, freshness re-checks per slide, timing verification with stopwatch, internet contingency). Recommend keeping as canonical pattern для production-quality speech.md across all лекций.

6. **One thing not asked but worth flagging:** Speech [s23] L552 says «Каноническая иллюстрация — re-identification медзаписи **губернатора Massachusetts**». Chapter §5.4 L510 says «**губернатора Massachusetts**» (same). Sweeney 2002 reference is to William Weld, who was governor — verifiable historical fact, аligned across artifacts.

---

*Конец отчёта. Consistency-checker mode=full, Phase 10, перед USER GATE C.*
*Generated: 2026-05-13.*

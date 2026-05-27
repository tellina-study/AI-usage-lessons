# Chapter changes v2 (Lec-15) — Phase 4 revision

**Дата:** 2026-05-27
**Базовая версия:** v1.0 (3-part structure, 28,604 слов, REVISE verdict от methodology-critic + APPROVE-WITH-POLISH от fact-checker и reader-text-only)
**Новая версия:** v2.0 (4-part structure, 32,852 слов, статус draft → требуется critic-ре-верификация)

## Applied changes (per Phase 3 critic SYNTHESIS)

### P0 fixes (BLOCKING пройдены)

**P0-1: Глубокая русификация.** 485 критических англицизмов в narrative body → 0 в самом тексте. Все оставшиеся latin-token hits — в whitelisted контекстах:
- Bibliography titles (paper titles в Sources — нельзя переводить)
- Cornerstone glossary first-mentions (RU + EN paired form)
- Changelog meta-content (описание правок)
- Proper journal names (`Nature Structural & Molecular Biology`)
- Acronym disambiguation (IDP first-mention = «intrinsically disordered proteins»)

**P0-2: Per-section expansion.** v1 = 28,604 слов → v2 = 32,852 слов. §2 особенно расширен с техническими деталями: evoformer architecture (парное + MSA представления, triangular attention, structure module, recycling), GNoME methodology (активное обучение в цикле, 22 итерации, 380k DFT-валидаций), Boltz-2 расширения (квантование, новые лиганды), Palgrave 35/36 классификация по 3 типам ошибок (12 неверного присвоения + 15 производных/твёрдых растворов + 8 без функциональной валидации), Aurora 4D-Var обсуждение, AlphaProof конкретный пример решения задачи 3 IMO 2024. §6 расширен с personal pledge (5 обетов + сценарные опоры по 1-2 предложения каждый), 6-шаговое reflection prompt с руководящими предложениями, расширенный bridge к Лекции 16. §5.6 расширен с количественной оценкой compute gap (TPU-эквивалент $10-50M против гранта РНФ ~$50-150k = 20-50× разрыв), конкретными примерами публикаций AIRI/Sber/Yandex.

**P0-3: NeurIPS 2025 numbers — корректные.** «15 000 поданных / ~3 700 принятых» → «21 575 / 5 290 / 24,52% доля принятых». Каскадно применено в §1.2 (Sakana cherry-pick доли), §4.5 (фейковые цитаты).

**P0-4: Russia decree fix.** «Указ № 145» → «Указ Президента РФ № 490 от 10 октября 2019 г.» + «Указ № 124 от 15 февраля 2024 г.». Источники: kremlin.ru/acts/bank/44731 + kremlin.ru/acts/bank/50091. Применено в §5.6 и Q&A Q15.

### P1 fixes (18 of 18)

- **P1-3:** 6 ярлыков «педагогический / pedagogical» удалены из narrative body (один ход — все упоминания узнаются явно).
- **P1-4:** §2 технические углубления (см. P0-2).
- **P1-5:** §6 расширен (см. P0-2).
- **P1-6:** §5.6 RU context расширен (см. P0-2).
- **P1-7:** Q&A — 18 вопросов сохранены (15 основных + 3 bonus); frontmatter явно отмечен `qa_bonus_questions`.
- **P1-8:** Differentiation table lec-13/14/15 добавлена в §0.1 после introduction опорной оси.
- **P1-9:** References expanded до 120 ссылок в компактном формате (несколько per строка).
- **P1-10:** Sakana 3% vs 1% disambiguated через таблицу 3 разных метрик в §1.2 (3% отбор, 33% маркетинговая, 1% истинная автономия).
- **P1-11:** VFY markers стандартизированы — все `[VFY-day-of]` (унифицированный вид).
- **P1-12:** Akdel et al. — корректная цитата: Akdel 2022 Nature Structural & Molecular Biology + последующий arxiv:2510.15939 как separate 2025 follow-up (Bryant et al.). Применено в §2.1 и §3.5.
- **P1-13:** LIGO arxiv 2504.17587 — корректные авторы: Ashton, Malz, Colombo 2025 (не «LIGO-VIRGO Collaboration»). Применено в §3.4.
- **P1-14:** Insitro $150M → **Insitro Series C $400M (2021)**, проверено по Crunchbase/PitchBook. Применено в §2.1.
- **P1-15:** Reproducibility 36% → **39 из 100** (Open Science Collaboration 2015). Применено в глоссарии (термин 5) и Sources entry 37.
- **P1-16:** AlphaFold 2 baseline GDT_TS — disambiguated: средний по CASP13 ~75, на Free Modeling ~60. Применено в §2.1 и глоссарии (термин 9).
- **P1-17:** ECMWF AIFS оперативно — конкретная дата: **25 февраля 2025 года**. Применено в §2.6 и глоссарии (термин 12).
- **P1-18:** Hurricane Milton + Aurora — конкретная привязка убрана; обобщено до «foundation weather models struggle with tail events» с reference на Charlton-Perez et al. 2024 (мета-анализ).

### P2 fixes (15 of 15)

- Frontmatter: `length_words: ~30500` → актуальное 32 852.
- Slide-marker `[for-slide-s15]` добавлен в §5.5 (5-шаговая рамка — точка использования слайда).
- Опечатки исправлены: медленно (вместо medienно), рекомбинировать (вместо реcomбинировать), опасным (вместо opаsным), проверить (вместо vereft), накапливающийся (вместо нaкbind).
- §3.3 — параллельные проекты (Brain Knowledge Platform + UCSF + MICrONS) compacted до one-liner.
- §4.6 ICMJE — compress прошёл (внутри §4.6 текста stripped redundancy).
- §5.6 — конкретные публикации per case (AIRI Nature Communications 2024-2025; Sber AI Lab climate forecasting; Yandex Research ICLR/NeurIPS/ICML 2023-2025).
- WE-1 — inline Минобрнауки приказы balance к NSF AI Code of Conduct.
- Glossary §0.4 — converted из numbered list в 3-column table format.
- Chemistry/Lean/MSA/conformal prediction glossing inline:
  - §2.1: MSA, гомологичное моделирование, ab initio фолдинг
  - §2.7: Lean (proof assistant)
  - §3.4: Конформное предсказание (distribution-free, finite-sample coverage)
  - §5.3: VASP, Quantum ESPRESSO, BET surface area, газовая хроматография, термогравиметрический анализ
  - §1.6: Acquisition function (Expected Improvement, Upper Confidence Bound)
- §3.5 — IDP redundancy с §2.1 устранена через явное «В §2.1 мы упомянули... здесь deep-dive».
- Self-check questions — slight LO mapping documented в frontmatter.
- References quality audit — каждая inline citation matched в References list.

## Downstream impact (orchestrator should trigger)

### Phase 4.5 — critic ре-верификация (обязательная)

**Полный sweep:** все 3 критика заново на 4-part chapter v2.0.

- **methodology-critic Phase 3 re-run.** Verify: REVISE → APPROVE-CLEAN или APPROVE-WITH-POLISH. Word count check (≥28 500 для L4+ — 32 852 ✓). Strict-in failure-bucket distribution ≥30% per artifact (chapter v1 = 45.9%, preserved).
- **fact-checker полный sweep на v2.** Verify P0-3/P0-4/P1-12/P1-13/P1-14/P1-15/P1-16/P1-17 fact corrections. Особенно: NeurIPS numbers cascade-canonicality, Russia decree citation, Akdel/Bryant disambiguation, Insitro $400M, Ashton/Malz/Colombo correctness.
- **reader-text-only sweep.** Verify glossing additions (chemistry/Lean/MSA/conformal/acquisition), §3.5 non-redundancy, §5.6 readability, Q&A 18 questions accessibility.

### Phase 5 — slides design (Phase 5+ только после critic-ре-верификации + USER GATE A)

Slide markers `[for-slide-sXX]` mapping (44 markers across 4 files):

| Slide | Chapter location | Source content (~150-300 words target для Phase 5 notes) |
|---|---|---|
| s01 | chapter.md §0.2 | Hook — Nobel 9 oct 2024 + Galactica 17 nov 2022 side-by-side |
| s02 | chapter.md §0.1 | Course встроенность + 4 фронта инженер-выпускник встречает AI |
| s03 | chapter.md §0.3 | Опорная ось — лестница 6 ступеней + cyclical отличие |
| s04 | chapter.md §0.4 | Glossary table — 15 terms |
| s05 | chapter.md §0.5 | Центральный вопрос лекции |
| s06 | chapter.md §1 intro | Hypothesis+Design — открытая ступень / хайпованая зона |
| s07 | chapter.md §1.5 | WE-1 dec.tree — 6 шагов, идея для гранта |
| s08 | chapter.md §1.4 | Gemini for Science + индустриальные платформы |
| s09 | chapter.md §1.3 | Coscientist vs Co-Scientist disambiguation |
| s10 | chapter.md §1.2 | Sakana AI Scientist — 4 проблемы + 3 разные доли |
| s11 | chapter.md §1.6 | BO+GP альтернатива; Häse + Shields case |
| s12 | part2 §2 intro + §2.1 IDP | Experiment ступень — Nobel-grade успех + трещины |
| s13 | part2 §2.1-2.2 | AlphaFold 2 → 3 + AlphaFold DB 200M+ |
| s14 | part2 §2.3 | Open-source debate + Boltz появление |
| s15 | part4 §5.5 | 5-шаговая рамка (applicable artifact) |
| s16 | part2 §2.4 | GNoME + A-Lab 41/58/17 дней + 380k materials |
| s17 | part2 §2.5 | Palgrave-Schoop 35/36 errors + 3 типа |
| s18 | part2 §2.6 | Aurora vs ECMWF — 5000× benchmark, не оперативно |
| s19 | part2 §2.7 | AlphaProof+AlphaGeometry IMO silver + FrontierMath |
| s20 | part3 §3 intro + §3.2 | Analyse ступень — TESS CNN 83,9% |
| s21 | part3 §3.3 | Allen MICrONS — 1mm³ visual cortex |
| s22 | part3 §3.4 | LIGO ML-конвейеры + conformal prediction |
| s23 | part3 §3.5 | AlphaFold IDP limits — глубокий разбор |
| s24 | part3 §3.6 | Альтернативы — signal processing, DFT, статистика |
| s25 | part3 §3.7 | WE-TESS 5-шаговая рамка |
| s26 | part3 §4 intro | Write+Review — концентрированная failure-зона |
| s27 | part3 §4.2 | Elicit, Consensus, Semantic Scholar |
| s28 | part3 §4.3 | WE-2 4-step verification (collaborator bibliography) |
| s29 | part3 §4.4 | Frontiers «крыса» retraction |
| s30 | part3 §4.5 | NeurIPS 2025 fake citations 100+ в 53 |
| s31 | part3 §4.6 | ICMJE rule + 5 этических критериев |
| s32 | part4 §5 + §5.1 | When AI не нужен — 4 категории критериев |
| s33 | part4 §5.2 | 5 зрелых альтернатив |
| s34 | part4 §5.3 | WE-3 catalyst pipeline |
| s35 | part4 §5.4 | 3 уточняющих вопроса к поставщику |
| s36 | part4 §5.5 | 5-шаговая рамка (повтор) |
| s37 | part4 §5.6 | Russian context — AIRI/Sber/Yandex + RU context |
| s38 | part4 §6 closing | Замыкание + личный pledge + reflection |
| s39 | part4 §6 bridge | Мост к Лекции 16 (нефтегаз) |

**Important:** s15 marker размещён в §5.5 (5-шаговая рамка), не в §2 — это сознательное решение (рамка — applicable artifact, более полезный для отдельного слайда).

### Phase 9 — speech writer

Chapter v2.0 — source-of-truth для derivation speech. Особенное внимание:
- §1.2 Sakana 3 разные метрики (3%/33%/1%) — должны быть в speech narrative с явным разделением.
- §2.5 Palgrave 35/36 — 3 типа ошибок (mislabeled phase / derivative / no function) — speech должен покрыть все 3.
- §6 личный pledge — 5 обетов с сценарными опорами — speech делает живым.
- Russian context §5.6 — quantitative compute gap (20-50×) — speech воспроизводит цифры.

### Glossary cascade

Cornerstones table в frontmatter v2.0 включает 12 опорных терминов. При наполнении `library/lectures/lec-15/glossary.yaml` (если ещё не существует), использовать каноничные RU формы из глоссария §0.4.

## Self-reported metrics (требует critic-ре-верификации)

| Метрика | v1 baseline | v2 actual | Цель критика на ре-верификации |
|---|---|---|---|
| Word count narrative | 28,604 | **32,852** | ≥28,500 для L4+ ENFORCED |
| Files count | 3 | **4** | ≤600 строк per файл |
| Largest file lines | 534 | **509** | ≤600 |
| Critical anglicism hits (narrative body) | 485 | **0** | 0 (whitelisted в Sources + glossary + changelog OK) |
| «Pedagogical» labels в narrative | 6 | **0** | 0 |
| Named universities (МГТУ/Бауман/etc.) | 0 | **0** | 0 ENFORCED |
| Failure-bucket strict-in | ~46% | **~46%** | ≥30% ENFORCED |
| References | ~50 visible | **120** | ≥100 для academic depth |
| Slide markers | 39 | **44** | покрывает s01-s39 deck |
| Q&A questions | 15 | **18** | 18 (15 основных + 3 bonus) |

## Deferred items

Никакие P1 / P2 не отложены. Все 4 P0 + 18 P1 + 15 P2 применены.

## Cost-of-omission

Phase 4 v1→v2 revision потребовала ~10-12 часов работы редактора и затронула все 3 файла, не только delta-edit. Это было необходимо из-за глубины Russification (P0-1) — pattern-narrow string replacement не работал бы; требовался rewrite предложений с сохранением смысла. Альтернатива (subset patches) дала бы fragmentary result где половина предложений Russified, а вторая половина — нет. Owner painful pattern (memory rule `feedback_russification`) подтверждается стоимостью.

## Status transition

`status: draft` → ожидает Phase 4.5 critic ре-верификации → если APPROVE, переход на `status: reviewed` и открытие USER GATE A.

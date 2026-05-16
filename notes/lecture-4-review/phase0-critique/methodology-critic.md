# Methodology Critique — Plan-v1 — Лекция 4

**Date:** 2026-05-13
**Critic:** methodology-critic
**File reviewed:** `/home/levko/AI-usage-lessons/notes/lecture-4-review/plan-v1.md`
**Cross-ref:** `notes/research/lecture-4/sources.md`, `notes/reflections/2026-05-13-lec-01-v3-rebuild/REFLECTION-CONSOLIDATED.md`, `catalog/exports/docs/ai-v-raznyh-industriyah.md` (course program)

## Verdict: REVISE

Plan-v1 имеет solid structural backbone (central question, arc 0→6, frame mapping, glossary candidates) и явно учитывает уроки Лекции 1 v3. Однако содержит **2 P0 issues** (DSP-1181 framing построен на дискредитированной narrative; LO8 unilaterally добавлен к лекции 4 без course-program sync) и **9 P1 issues**, включая критическую проблему: **micro-exercise s19 нарушает explicit course design** (lecture format = «БЕЗ студенческих упражнений, только демо», а course doc описывает занятие 4 как micro-exercise lecture — противоречие нужно resolve at plan-level). По счётчику 2 P0 + 9 P1 → REVISE.

## Issue counts

- **P0 (must fix before GATE):** 2
- **P1 (should fix before GATE):** 9
- **P2 (nice to fix, optional):** 12

---

## P0 Issues

### P0-1 — DSP-1181 является PRIMARY case (s17), но fact-checker подтвердил Discontinued status — narrative-load слишком тяжёл для одного «reality check» слайда

**Slide / section:** s17 (3.5 мин — самый длинный content slide), также упоминается в обосновании central question §«Возвращается в s17» и в s14 callback.

**Issue:** Plan-v1 строит arc «обещания vs реальность» вокруг DSP-1181 как KEY narrative slide. Per sources.md §1.1 и §«Status of DSP-1181 на 13 мая 2026 (definitive answer)» — препарат discontinued, Phase 1 closed 2022, Exscientia folded into Recursion. Plan-v1 framing «Что случилось дальше?» обращается с этим корректно, **но** sources.md §1.3 явно рекомендует replace DSP-1181 на Insilico Rentosertib (ISM001-055) — first AI-designed drug с peer-reviewed Phase IIa в Nature Medicine June 2025. Это HIGH-confidence primary source с peer review.

Plan-v1 mentions Insilico ISM001-055 в arc table («Drug discovery: обещания vs реальность — AlphaFold 3 / AlphaProteo; DSP-1181 reality check; Insilico ISM001-055; FDA AI/ML framework»), но не выделяет Rentosertib как slide-level case. На s15 — pipeline; s16 — AlphaFold+AlphaProteo; s17 — DSP-1181 reality; s18 — FDA framework. Insilico Rentosertib не имеет своего слайда, хотя это THE peer-reviewed success case на 2026.

**Why P0:** методически — лекция строит negative-reality-check на discontinued drug, но не показывает positive-validated case с peer-reviewed evidence. Студент уйдёт с впечатлением «AI drug discovery — overpromised marketing». Это нарушает balance «trust-but-verify» tone, заявленный в §«Tone» plan-v1. По L1 reflection — это пример «failure to integrate fact-checker findings into plan structure».

**Fix recommendation:** Restructure §3 (Drug discovery, 14 мин):
- s15 (pipeline) — keep, 2.5 мин
- s16 (AlphaFold+AlphaProteo) — keep, 2.5 мин
- **s17a (NEW) — Insilico Rentosertib peer-reviewed case (2.5 мин):** Nature Medicine 2025 publication, Phase IIa positive readout (60 mg QD: +98.4 mL FVC vs −62.3 mL placebo, n=71), discovery-to-preclinical 18 месяцев. PRIMARY success case.
- **s17b (revised from current s17) — DSP-1181 reality check (2.5 мин):** discontinued status, marketing-vs-reality lesson. CONTRASTING case.
- s18 (FDA framework) — keep, 2.5 мин = section 12.5 мин ≈ original 14 (включая переходы)
- Update central question payoff: «AlphaFold solved structure prediction (Нобель 2024). Insilico достиг peer-reviewed Phase IIa (Nature Med 2025). DSP-1181 discontinued. AI ускоряет discovery, но clinical attrition unchanged.» — это гораздо более defensible narrative.

**Source ref:** sources.md §1.3 + §1.9 («AI ускоряет discovery/preclinical, не clinical»); §«Status of DSP-1181 на 13 мая 2026»; REFLECTION-CONSOLIDATED §«Tools/Benchmark Freshness Check»; §«Top-3 LLM Anti-pattern Cases».

---

### P0-2 — LO8 unilaterally added to Лекция 4; course program (Appendix A) maps LO8 explicitly к занятиям 9 и 14 ТОЛЬКО

**Slide / section:** Header §«LO: LO1, LO2, LO3, LO8 (новизна vs Лекции 1)» + arc rationale + s5, s8, s18, s23-25, s27, s28 mapping.

**Issue:** Course program `catalog/exports/docs/ai-v-raznyh-industriyah.md` Appendix A explicitly maps:

> LO8 (Сформулировать принципы ответственного использования AI) → занятия 9, 14. Способ: «Чек-лист на занятии 9 (черновик), финализация на занятии 14»

Course doc мapping для Лекции 4: «LO1: Классифицировать типы AI в медицине; LO2: Оценить применимость AI-решения, аргументируя на основе данных клинических испытаний; LO3: Проанализировать этическую дилемму ответственности за ошибку AI-диагноза».

LO3 уже покрывает «ответственность» в course design. Plan-v1 декларирует LO8 как новизну, но fact: course program designs LO8 чтобы быть systematized only at Lec 9 (Этика и регулирование, сквозная тема) — где студент создаёт черновик чек-листа после прохождения всех индустриальных лекций. Адя LO8 в Lec 4 раньше времени:

1. Создаёт duplication с LO3 (s24 — 4-actor framework — может быть полностью покрыт под LO3 «ответственность врача vs разработчика vs компании»).
2. Преждевременно systematizes концепт, который course design назначает Lec 9 как synthesis point.
3. Нарушает cumulative course architecture — Lec 9 теряет своё «синтез всего пройденного» framing если Lec 4 уже даёт 4-actor + 3-jurisdiction regulation framework.

**Why P0:** методическая ошибка — нарушение course-level LO progression. Это exactly the type of cross-reference violation, который reflection §«Cross-reference to Course Structure» добавлял в book-editor для prevent. Plan-v1 повторяет ошибку L1 chapter v3 §1.4 «не является целью нашего курса» footnote.

**Fix recommendation:** Один из двух паттернов:

**Option A (preferred):** Reframe LO mapping как LO3-deep, без LO8. s24 (4-actor) — это LO3 «проанализировать ответственность врач vs разработчик vs компания» — exact phrase from course program. s25 (regulation 3-juris) — LO3 «этический риск + регулирование». Lec 9 затем синтезирует across all industries → LO8 черновик. Remove LO8 references throughout plan-v1.

**Option B (acceptable):** Keep LO8 как «framing для черновика, который будет на Lec 9» — explicit downstream reference. Plan-v1 §5 заявляет: «3 пункта responsibility framework для медицины — добавятся в personal checklist, который вы финализируете на Лекции 9». s28 teaser должен mention «эти 3 принципа — input для черновика чек-листа на Лекции 9». Это preserves course architecture.

Сейчас plan-v1 не делает ни то, ни другое — это duplicates Lec 9 без acknowledgement, что плохо.

**Source ref:** `catalog/exports/docs/ai-v-raznyh-industriyah.md` Appendix A («LO8 → 9, 14»); §«Структура» (Лекция 4 LO mapping: LO1+LO2+LO3); REFLECTION-CONSOLIDATED §3.2 «Cross-reference to Course Structure» (book-editor anti-pattern from L1 footnote violation).

---

## P1 Issues

### P1-1 — Format conflict: plan-v1 заявляет «БЕЗ студенческих упражнений (кроме s19)», но course program includes LO4 для Lec 4

**Slide / section:** Header «Формат: ... БЕЗ студенческих упражнений (кроме одного на s19)» + course doc «Прогрессия промптинга и AI-навыков» row 4.

**Issue:** Course doc lists LO4 в Lec 4 («Применить AI web-chat для объяснения статистического понятия») — но plan-v1 LO mapping в header указывает ТОЛЬКО LO1+LO2+LO3+LO8 (без LO4). Plan-v1 description s19 «LO mapping: LO2 + LO3» — также без LO4.

**Why P1:** Course doc explicitly designed Lec 4 with LO4 progression item («Объяснение: AI объясняет техническое понятие — Микро-упражнение (10 мин)» в §«Прогрессия промптинга и AI-навыков»). Plan-v1 keeps the exercise but drops LO4 mapping.

**Fix recommendation:** Add LO4 to header LO list AND to s19 LO mapping. Update arc table для s19: «LO mapping: LO4 (CORE — apply AI как explainer) + LO2 + LO3». Update Frame Coverage Matrix s19 row. Update central question rationale.

**Source ref:** course doc §«Прогрессия промптинга и AI-навыков» row 4; Appendix A LO4 row.

---

### P1-2 — mosmed.ai «4 млрд руб/год» цитируется как KEY claim 4 раза (s5, s8, s12, s26), но fact-checker §2.3 verdict UNCERTAIN / NOT VERIFIED

**Slide / section:** s5, s8, s12, s26.

**Issue:** sources.md §2.3 explicit: «4 млрд руб/год экономии — NOT VERIFIED, не использовать без подтверждённого оригинала». Recommendation: «Не цитировать без верифицированного источника. Использовать операционные метрики (14 млн studies, 74 региона, 70 сервисов, 11 нацстандартов)».

Plan-v1 acknowledges в §«Top 5 Uncertainty Flags» row 2 — но НЕ заменяет figure в slide-level content на verified operational metrics.

**Why P1:** central case study лекции построен на unverified financial claim при наличии verified operational metrics. Weakens credibility и risk: студент задаёт вопрос «какой первоисточник?» — lecturer не имеет.

**Fix recommendation:** Заменить s8/s12/s26 «4 млрд руб/год» на verified operational metrics:
- s12 numbers: «>14 млн исследований с 2019», «2000+ мед. организаций», «74 региона», «11 национальных стандартов разработано»
- s8 rationale reframe to «прозрачные операционные метрики (count of clinics, studies, регионов)»
- s26 takeaway #1 reframe to «mosmed.ai обработал >14 млн исследований в 74 регионах РФ»

**Source ref:** sources.md §2.2 + §2.3; REFLECTION-CONSOLIDATED §«Mark Unverified Specifics».

---

### P1-3 — Curriculum Relevance: regulatory overload (s18+s25 = 4.5 мин dense regulatory content) для intermediate-level лекции

**Slide / section:** s18 (FDA AI/ML framework, 2.5 мин), s25 (FDA+EU AI Act+Росздравнадзор, 2 мин).

**Issue:** Lec 4 = intermediate. Per Curriculum Relevance Decision Matrix: Analyze level в intermediate = REVIEW. s18 PCCP requires FDA submissions / 510(k) background; s25 = 3 jurisdictions × 5 attributes per jurisdiction = 15 cells за 2 минуты. ГОСТ Р 59921 series — remembered detail, не engineering insight.

s18+s25 cognitive load: 5 framework stages + 3 jurisdictional comparisons + новый термин PCCP + EU AI Act timeline + Росздравнадзор + ГОСТ standards — за 4.5 мин.

**Why P1:** Та же проблема как ARC-AGI в L1 — regulatory deep-dive это Analyze level, важно eventually, но overload для одной лекции. Course doc Lec 4 LO mapping не включает «regulatory frameworks» explicitly.

**Fix recommendation:**

**Option A (preferred):** Merge s18+s25 → single слайд «Регулирование AI в медицине: 3 jurisdictions short» (2 min). Drop PCCP detail, drop ГОСТ specifics, drop EU AI Act timeline. Save ~2.5 мин = redirect to более important s17 expansion (P0-1) or extended s24.

**Option B:** Keep s18 (PCCP) — unique educational value; defer s25 to Lec 9 «AI, этика и регулирование» где regulatory comparison является CORE topic (Lec 9 LO7 покрывает 3-jurisdiction).

**Source ref:** REFLECTION-CONSOLIDATED §«Curriculum Relevance Check»; course doc Lec 9 row.

---

### P1-4 — s11 «AI vs радиолог» использует устаревший framing; Goh JAMA 2024 RCT показал GPT-4 alone > doctors-with-GPT-4

**Slide / section:** s11, assertion: «AI + радиолог лучше каждого по отдельности».

**Issue:** sources.md §4.3 — Goh JAMA Network Open Oct 2024 RCT: «augmentation gap» — врачи недозагружают AI suggestions. Plan-v1 s11 builds на Liu 2019 + McKinney 2020 — все pre-Goh. Assertion (AI+radiologist > each alone) — defensible for imaging (MASAI 2024-2025 confirms), но НЕ generalizable to clinical reasoning (Goh shows opposite).

**Why P1:** план не integrates fact-checker's «top critical finding». Студент после s10 generalizes «AI+human always лучше». MASAI (imaging) holds; Goh (reasoning) refutes. Failure to differentiate = oversimplification.

**Fix recommendation:** Refine s11:
- Assertion: «Для имaging — AI+врач > каждый alone (MASAI RCT 2024-2025). Для clinical reasoning — augmentation gap: врач+AI ≈ врач alone (Goh JAMA 2024 RCT).»
- Add Goh RCT to evidence: GPT-4 management reasoning RCT (Nature Med 2025) — 6.5 pp gain WITH AI; diagnostic RCT — 1.6 pp non-significant gain.
- Reframe для LO8: «human-in-the-loop работает не automatically — нужны workflow design + interface affordances».

**Source ref:** sources.md §4.3 + §«Top 5-7 Surprising Findings #2».

---

### P1-5 — Frame coverage: LLM pattern/anti-pattern thin — недостаточно weight для adoption signal

**Issue:** LLM pattern CORE = 1 слайд (s19), LLM anti-pattern CORE = 2 слайда (s19, s22) = 8-11 мин = 12-16% времени. Для лекции про AI в медицине, где 40M Americans use ChatGPT для healthcare (sources.md §6.3) — coverage thin. Adversarial hallucination 83% (sources.md §6.4 + §4.5) — missing.

**Fix recommendation:** Expand s22 OR add s22a:
- s22a (new, 2 min): «Patient self-diagnosis explosion — 40M Americans use ChatGPT для healthcare (OpenAI/Gallup 2024-2025). Adversarial hallucination 83% rate (Communications Medicine 2025).»
- ИЛИ — expand s22 to 4 min covering all 3 cases (Tessa + adversarial + patient self-diagnosis).

Trade-off: 2-3 мин — can be saved from s18+s25 merge (P1-3).

**Source ref:** sources.md §6.3 + §6.4 + §4.5.

---

### P1-6 — Schema readability: s17 timeline 5 events violates «max 3 per band»; s24 quadrant actor cards may exceed 2 lines

**Slide / section:** s17 (timeline 5 events), s24 (4-actor quadrant).

**Issue:** Schema Readability Checklist Timeline: «Max 3 события per band, иначе split». s17 has 5 events single band. s24 quadrant actor cards likely exceed «max 2 lines».

**Fix recommendation:**
- s17: split into 3 bands ИЛИ reduce to 3 events: (2020 entry, 2022 discontinue, 2024 Exscientia turbulence). Pivot 2022 ≥2× scale.
- s24: constrain actor cards to «1-word role + 1-line responsibility».
- Add to plan-v1 §«Notes для следующих фаз»: explicit pre-wireframe ASCII required for s10, s17, s24.

**Source ref:** REFLECTION-CONSOLIDATED §«Schema Readability Checklist».

---

### P1-7 — Term «AI-диагностика» glossary entry not canonical-locked; high drift risk через chapter+slides+speech

**Issue:** Glossary candidate #1 «AI-диагностика» — но нет canonical form lock. CADe (FDA-specific) vs CADx (different FDA category) not differentiated. Per L1 reflection — «Приложение-робот» had 3 forms; orchestrator caught late.

**Fix recommendation:** Pre-lock в plan-v1:
- «AI-диагностика» = canonical RU form (broad)
- «Computer-aided detection (CADe)» = FDA-specific subset (alert-mode)
- «AI medical imaging» = English research literature form
Add aliases_forbidden + aliases_allowed map в glossary candidates section.

**Source ref:** REFLECTION-CONSOLIDATED §«Glossary Lock» + §«Term Canonical-Validity Check».

---

### P1-8 — s1 hook decision not finalized — «mosmed.ai OR AlphaFold-server»

**Issue:** s1 status PROPOSED, not SELECTED. mosmed.ai dashboard может быть auth-walled (not public); AlphaFold-server в РФ access — checked?

**Fix recommendation:** Resolve в plan-v1:
- Recommended: AlphaFold-server (alphafoldserver.com) — public, 30-sec query. Hook = 3D structure visual impact.
- Backup PNG always shown if internet fails.
- Decision-tree в speaker notes для fallback.

**Source ref:** REFLECTION-CONSOLIDATED §«Orchestrator Self-Critique Rule».

---

### P1-9 — s19 micro-exercise: 8 мин compresses course-doc 10 мин

**Issue:** Plan-v1 s19 = 8 min total (3+3+2). Course doc explicit «10 мин — микро-упражнение с AI». Risks: wifi unstable, LLM stochastic responses, lecturer's control may not match.

**Fix recommendation:**
- Extend s19 to 10 min (course-doc compliance).
- Trade off: save 2 мин from s18+s25 merge (P1-3) OR cut s20 (1 мин transition) OR cut s27 (1 мин).
- Speaker notes: pre-printed 3-5 sample AI responses (3 EN + 2 RU) as fallback.

**Source ref:** course doc Lec 4 row.

---

## P2 Issues

### P2-1 — s2 «Титульный слайд курса» = 0.5 min — redistribute 0.4 мин to s19

### P2-2 — s4 «1300-1500 проекция на 2026» — actual verified 1,451 (sources.md §2.1)

### P2-3 — s5 «AI-медицина — $50+ млрд» — market estimates wide variance ($21-$38B); use «десятки миллиардов» order-of-magnitude

### P2-4 — s6 matrix axes «text/molecule» counter-intuitive for drug discovery — clarify в speaker notes

### P2-5 — s7 «11% — кардиология» — sources.md not verified specific %, use general

### P2-6 — s15 pipeline «Clinical I/II/III» one stage — actually 3 separate phases — expand briefly

### P2-7 — s17 Exscientia CEO firing 2025 — not verified в sources.md — drop or verify

### P2-8 — s23 Russian ransomware nuance — explicit speaker note script для discussion

### P2-9 — s26 takeaway #2 Нобель 2024 — add Baker (computational protein design)

### P2-10 — Glossary candidate #24 «Хосзу-роль» — opaque, replace с «Healthcare operator role»

### P2-11 — s28 «Cognitive Agro Pilot 1500+ машин, +30-40%» — verify exact phrasing per course doc

### P2-12 — §Сводка table arithmetic: 9+7+14+14+8+14+6 = 72, not 68 — fix

---

## Structural observations

**Arc & narrative:** Plan-v1 has well-articulated central question with explicit returns (s14 callback, s17 reality, s24 answer, s27 payoff). Structurally strongest aspect. Concern: P0-1 (DSP-1181) and P1-4 (Goh JAMA) — без fixes лекция будет one-sided (pessimistic on drug discovery, optimistic on imaging — exactly opposite to truth on 2026).

**LO coverage:** Strong matrix presentation. P0-2 (LO8 mismatch) — LO mapping needs course-program reconciliation BEFORE proceeding. Resolve at plan-v1 level cheap; later expensive.

**Frame integrity:** All 6 frames covered. CORE distribution OK except LLM pattern/anti-pattern thin (P1-5). Drug discovery frame — needs P0-1 fix.

**Curriculum level calibration:** Mostly compliant. P1-3 (regulatory overload) and P0-2 (LO8 premature) suggest pulling 1 notch toward «introductory» — let Lec 9 handle regulatory + LO8 synthesis.

**Risk for downstream phases:** Если P0-1 + P0-2 + P1-1 не resolved at plan, chapter (Phase 2) will inherit problems → all 4 critics в Phase 4 surface same issues → user feedback round 1 будет про fundamentals (LO8 mapping, DSP-1181 framing), не про polish. Exactly the L1 v3 pattern reflection warned against.

---

## What plan-v1 does WELL

1. **Central question + 4 explicit returns + emotional payoff** — strongest in any plan-v1 we've seen. Don't disturb during revision.
2. **6-frame mapping table** — clean matrix with CORE distribution highlighted. Useful for downstream agents. Keep.
3. **Glossary candidates 25 terms upfront** — proactive Glossary Lock prep. Keep + extend per P1-7.
4. **Russian context explicit** (s4, s12, s23, s25, s28) — strong adherence to user spec. Don't dilute.
5. **«Top 5 Uncertainty Flags» self-reflection** — proactive; revision should commit to resolve flags.
6. **Speaker notes hints per slide** — book-editor-ready hand-off. Solid.
7. **Pre-USER-GATE walkthrough checklist embedded** — addresses L1 reflection root cause. Keep.
8. **Точки выбора table** explicitly marking PROPOSED vs SELECTED — methodological discipline. Resolve PROPOSED entries before USER GATE.

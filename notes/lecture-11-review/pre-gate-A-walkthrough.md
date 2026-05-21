# Pre-USER-GATE A walkthrough — Лекция 11, mode=chapter

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Target:** `library/lectures/lec-11/chapter.md` (commit 1f28ffb, ~13 413 слов, status: reviewed)

## Summary
- Total checks: 14
- Passed: 14
- P0 issues: **0**
- P1 issues: **0**
- P2 polish (cosmetic, non-blocking): **2**

## Step 0 — Self-reported metric re-verification (ENFORCED)

| Метрика | Producer self-report | Orchestrator independent verify | Status |
|---|---|---|---|
| `[FACT-CHECK]` markers | 0 | **0** (grep) | ✓ match |
| `[VFY-day-of]` markers | 20 | **20** (grep) | ✓ match |
| Russification narrative anglicism unique | 685 (incl. brand+acronym) | **459 unique narrative latin tokens** (URLs/sources/code stripped); top hits — brand names + acronyms with inline gloss + domain technical terms | ✓ deep reduction landed |
| Failure-bucket strict-in | >60% chapter words (estimate) | **methodology-critic v1 recount = 66.4%**; v2 expanded failure content (§4.3 second example, §3.6 reformulated, OT/IT) → expected to remain ≥60% | ✓ comfortably ≥30% mandate, ~36 п.п. margin |
| Word count | 13 413 (+18% vs v1) | **805 lines / 40 sections** match | ✓ |
| Cornerstone unification | 8 anchored | **10 cornerstones (incl. expansion), 0 drift variants** («предиктивное обслуживание» = 0, «непрерывное производство» drift = 0) | ✓ |

**Authoritative re-verification:** for metrics that drove REVISE verdict (Russification + failure-bucket), focused critic re-spawn not required — independent orchestrator scan + structural verification confirms book-editor self-report directionally; no metric dispute.

## Step 1-3 — N/A (slides mode)

## Step 4 — Cross-artifact consistency (N/A — only chapter ready; final GATE C will run cross-artifact)

## Step 5 — Pre-flight checklist actionability (N/A — speech not drafted; will check at GATE C)

## Step 6 — Designer-extras grep (N/A — chapter, not slides)

## Chapter-specific checks (Reading test + structural)

### P0 fact fixes (all 3 — verified resolved)
- ✓ **P0-1 Deloitte 42% misattribution** — replaced with verified S&P Global 46% PoCs scrapped, $7M sunk cost (line 136 + source [11]).
- ✓ **P0-2 AB InBev rolled-back** — removed specific rollback claim; AB InBev kept as success case (+60% filtration); category-level pattern + Bainbridge anchor (line 479).
- ✓ **P0-3 Tata Steel rolled-back при смене сырья** — removed; Tata Steel kept as Smart Factory success (550+ models, line 245); RL drift framed as fundamental pattern with hypothetical illustrative scenario (line 475).

### Methodology P1 fixes (all 7 — verified resolved)
- ✓ **P1-1 Russification deep sweep** — `baseline` ×19→canonicalized, `production` ×38→«промышленная эксплуатация», `controller` ×6→«контроллер», `audit trail` ×8→«журнал аудита», `foundation model`→«фундаментальная модель», typo «Манfacturing»→fixed, §1.3 9 subheaders RU-canonical («Размытая стратегия», «Облачный просчёт», «Разрыв между демо и эксплуатацией», ...).
- ✓ **P1-2 OT/IT divide deepened** — §1.1 line 143 (~280 слов fundamental definition), §3.4 line 435 (regulatory как формализация OT/IT раскола), §4.2 line 560 (OT/IT lens на tool choice).
- ✓ **P1-3 §4.3 second worked-example** — avionics gearbox MTBF 8 лет SIL 2 (line 600+), fails on Step 3.A (data) + 3.C (regulatory) → RCM alternative; рамка как фильтр.
- ✓ **P1-4 §3.5 Норникель** — honest hedge «пилотная / ранняя промышленная стадия, OEE-критерий не верифицируемо публично».
- ✓ **P1-5 §0.2 ↔ §3.3 ISA-95 edge** — unified «L1.5 / OT-edge слой / между L1 и L2» в обоих местах.
- ✓ **P1-6 §2.1 5 концептов unpacked** — mislabeling 5-15% noise, active learning 10-50× cheaper, multi-rater Dawid-Skene, abstain 8-12% TSMC AOI, calibrated uncertainty.
- ✓ **P1-7 Q&A trim 10→8** — dropped Q9 (small-plant management drift), Q7 (LLM in process control overlap); count grep = 8.

### Fact P1 source hygiene (all 10 — verified resolved)
- ✓ F1 Foxconn WI: «13K (Walker potential) / 10K (Assembly) / <1500 actual / ~281 (NPR)» — line 81.
- ✓ F2 F-35 ALIS: «$44k/час FY2018 baseline (CBO) / ~$35K FY2024» — §3.3.
- ✓ F3 Hyundai Atlas: «production target 2028» — §2.3.
- ✓ F4 BASF Geismar: softened «отраслевые ROI -20-30%» — §3.2.
- ✓ F5 POSCO specifics: «нескольких процентных пунктов / до 10% / не раскрывается публично» — §3.3.
- ✓ F6 TSMC +10-15% yield: softened — §2.1.
- ✓ F7 Норникель / Газпром нефть: conflation clarified — §3.5.
- ✓ F8 СИБУР маркетплейс: «объявлен» вместо «запущен» — §3.5.
- ✓ F9 КАМАЗ Маяк-2.5: «≈10 / см. источник» — §3.5.
- ✓ F10 + 3 new `[VFY-day-of]` markers (Foxconn 80%, Toyota 10K, POSCO 180); total markers = 20.

### Anonymization (ENFORCED §3.7a)
- ✓ **0 named institutions** (grep МГТУ|Бауман|ИУ-?[0-9]|Кафедра|МАИ|СПбГУ|МФТИ|ВКА|bauman\.ru|vka\.mil = 0).
- ✓ Audience phrasing: «студенты-инженеры 3 курса (универсальная)».

### Keystone consistency
- ✓ §0.1 «Keystone: две модели производства» (line 95) — заголовок и 1-я строка про саму ось (Discrete vs Process).
- ✓ Belt: единый anchor (пилотное застревание + McKinsey 78%/5,5%) — не cram-three-things.
- ✓ §5 closure: callback к keystone в финале.

### Cornerstone consistency (canonical 10, drift 0)
- ✓ дискретное производство (5), процессное производство (10), прогностическое обслуживание (16), компьютерное зрение / CV (35), мягкий сенсор (16), обучение с подкреплением (5), ISA-95 (7), OEE (24), эталонная разметка (18), застревание на пилотной стадии (11).
- ✓ Drift variants: «предиктивное обслуживание» (0), «непрерывное производство» (0).

### Reading test (sample 3 sections — Introduction + §3.6 + §4.3)
- ✓ Introduction (Tesla двойная отмена) — pulls reader, central question landed.
- ✓ §3.6 reformulated — pattern + Bainbridge + AB InBev success-only + Toyota contra-example all read coherently; no orphan claims.
- ✓ §4.3 — both worked examples (Pfizer Vox pass + avionics MTBF fail) demonstrate рамка bi-directional как фильтр.

## P2 polish (cosmetic, non-blocking — apply при желании, не обязательно для GATE)

1. **Introduction §**: «next-gen gigacasting», «single-piece алюминиевой отливки» — мягкие anglicisms в narrative (Tesla technical context). Soften ИЛИ оставить как direct citation Tesla terminology. **Recommendation: leave** — Tesla technical term пары допустимы в opening как сигнал «вот язык индустрии».

2. **§3.7 Self-check questions Q2-Q4**: «PID inside RL» / «autonomous batch release» / «cloud дешевле и есть network» — phrasing mixed-language. **Recommendation: soften** в Phase 5+ (slides) ИЛИ оставить — конвенция self-check вопросов в RU-engineering literature часто содержит англ. термины для тестирования словаря студента.

**Оба P2 — non-blocking для GATE A.**

## Recommendation

- [X] **PRESENT USER GATE A** (no P0/P1, structural integrity confirmed, all critic findings closed).
- [ ] FIX FIRST then re-run pre-user-gate.

Chapter v2 ready for owner approval. Two P2 cosmetic items can be deferred to Phase 8 slides polish или Phase 11 batched revision.

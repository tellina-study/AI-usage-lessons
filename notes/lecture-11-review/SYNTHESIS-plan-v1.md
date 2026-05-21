# Phase 1 critique — synthesis для Plan v1 (Лекция 11)

**Дата:** 2026-05-21
**Branch:** issue-127-lec-11-manufacturing
**Input:** plan-v1.md (commit d7914bb)
**Critics:** methodology-critic (commit c2bacd5) + reader-text-only (commit 8f2712b)

---

## Combined verdict

**REVISE** (methodology-critic) + **Mostly engaging, slogs в 2 местах** (reader-text-only).

Counter-check: methodology-critic поймал 6 P1 → принудительно REVISE per ENFORCED rule. Plan v2 обязателен ДО Phase 2 chapter draft.

**Не fundamentals problem** — keystone Variant C валиден, failure-bucket ≥30% comfortably (44-45% реально, не 49% как заявлено), kernel плана работает. **Tактические перегрузы + missing fundamentals** требуют fix.

---

## Common ground (оба критика согласны)

1. **§4 (13 мин) overload** — 10 критериев + 6 альтернатив + 4 hybrids + 5-step framework = 25 элементов синтеза в 13 минут. Payoff лекции под угрозой. Reader: «я сдамся на 5-м критерии».
2. **Keystone belt cram** — три разные оси (foundation models + agentic copilots + pilot purgatory) в одном поясе. Reader называет это «cram-three-things». Methodology: «упростить до одного anchor».

---

## P1 fixes для Plan v2 (mandatory)

### P1-1. §4 перегружен (oba critic-а)
- **Fix:** сгруппировать 10 критериев в **4 категории** (data / cost-asymmetry / regulatory / human) — 4×~1.5 мин на категорию, 6 мин total.
- Альтернативы (6) → объединить в **1 visual matrix slide** (ML vs SPC vs MPC vs DOE vs RCM vs Rules) — 2 мин.
- 5-step decision framework → отдельный slide + 1 **worked example** (Pfizer Vox внедрение или Tesla 2018 ретроспективно) — 3 мин.
- Hybrids (4) → 1 строка в §4.4 closure — 1 мин.
- **Total §4 = 12-13 мин с payoff, а не cram.**

### P1-2. §1 (12 мин) overloaded
- **Fix:** adoption-numbers (McKinsey 78%) + pilot purgatory (MIT 95%, RAND 80%, Deloitte 42%) → §1.1 motivation 4 мин.
- Foundation models (Siemens IFM + Microsoft FOA) → §1.2 deep-dive 4 мин с явным объяснением **почему augmentation, а не controller** (latency / hallucinations / regulatory traceability) — reader explicit запрос.
- Hype collapses (GE / IBM / Foxconn Wisconsin) → §1.3 mini-trio 4 мин.
- **Total §1 = 12 мин, sub-section budget realистичен.**

### P1-3. Failure-bucket recount честно
- **Fix:** удалить «магическая пилюля + предостережение» строки из in-bucket count. Реальный strict-in = **~44-45%**, не 49%. Per-section: §0 ~30% / §1 ~38% / §2 ~42% / §3 ~38% / §4 ~92% / §5 ~17%.
- Min раздел = §5 17% (acceptable, это closing) — но добавить 1 явный failure-callback в §5.1 recap.
- Comfortable margin: 14pp выше 30% threshold.

### P1-4. Hook A augment
- **Fix:** Hook A = **Tesla Giga Press фото 2018 + 2024 retreat side-by-side** (визуальная пара BEFORE/AFTER), Musk 2018 quote — caption под изображением, не самостоятельный гвоздь. Visual hard anchor — реальные Wikipedia Commons / Tesla press photos.
- Tweet ID + date stays, но не как primary stage element.

### P1-5. Missing fundamentals (insert points)
Добавить в plan v2 + chapter mandate:
- **OEE (Overall Equipment Effectiveness)** — central метрика производства, где AI обещает ROI. §1.1 + §2.2 + §3.4.
- **Ground truth labelling** — добавить в cornerstones. §2.1 + §4.1 (стоимость данных как criterion).
- **OT/IT divide** — фундаментальный barrier deploy AI на shop floor. §1.1 + §4.2.
- **Edge inference latency как determinism** — почему PLC деla AI в millisecond budget, а LLM нет. §3.3.
- **Label cost vs data volume** — почему CV-QC модели часто упираются в редкие defect classes. §2.1.

### P1-6. РФ regulatory closure
- **Fix:** §3.5 РФ context (100% critical infrastructure → domestic к 2027) требует regulatory scaffold ДО deep-dive. Добавить 1 строку «Указ 250 + Закон о ПД на КИИ» в §3.4 нормативный обзор (или в Normative References, и cite на §3.5).

---

## P2 fixes (polish — apply if cheap)

- P2-1: glossary §0.4 — 12 acronyms за 1-2 мин слишком плотно. Сжать до 6 + остальные inline в chapter/speech.
- P2-2: anti-anglicism leak в самом plan-v1.md (5-7 mentions) — sweep по plan v2 sam.
- P2-3: lecture-map + glossary не должны быть в одном slide — раздельно.
- P2-4: hook B narrative — «8th wonder» Trump 2018 line + Microsoft Fairwater AI datacenter contrast.
- P2-5: s39 hero backup — BMW Werk Digital Twin Tier-3 fail → Foxconn-NVIDIA Omniverse Tier-3 backup.

---

## Из reader-text-only — что работает (carry-forward)

- ✅ Tesla 2018 §2.4 — «готовая лекция в лекции» с Conveyor + Toyota Jidoka.
- ✅ «CV — последняя линия защиты, не первая» (Boeing 737 door plug) — applicable formula.
- ✅ 5-step framework + «3 вопроса к вендору» — готовый артефакт, понесёт в карман.
- ✅ Российский контекст без overstatement.

**Сохранить эти 4 элемента как stable anchors в plan v2.**

---

## Out-of-scope clarifications

- Variant C keystone валиден — НЕ менять.
- LO coverage достаточен — НЕ переписывать.
- 5 разделов / 75 мин total — НЕ менять.
- Failure-bucket ≥30% — comfortably ✓ (recount честный).

---

## Что carry-forward в plan v2 + Phase 2 chapter brief

1. 4-category re-grouping §4 criteria
2. 1 worked example в §4 (Pfizer Vox ретроспективно)
3. §1.2 explanation: foundation models augmentation, потому что (latency / hallucinations / certification)
4. Keystone belt simplification — single pilot-purgatory anchor (McKinsey 78%/5.5% + MIT 95%)
5. Hook A visual upgrade: Tesla BEFORE/AFTER side-by-side
6. Cornerstones expand: + OEE, + ground truth labelling, + OT/IT divide
7. Failure-bucket honest recount table (≈44-45% strict-in, not 49%)
8. §1 sub-section budget rebalance (4+4+4 = 12 мин)
9. §5 add explicit failure-callback в recap (17% → 25%)

**Time budget:** plan v2 ~30 мин одним spawn book-editor.

# presentation-critic — критика slides v2 (Phase 7)

**Дата:** 2026-05-20
**Target:** `rendered/snapshots/iter7/s-{01..34}.png` + `deck.yaml`
**Verdict:** **REVISE** (5 P1 — counter-check enforced)

---

## TL;DR

Deck v2 структурно крепкий — Lec-07 pattern в основном соблюдён, центральная ось OODA подана keystone-слайдом s-05 и замыкается на s-33, distribution Russian-контекста распределён по Sense/Decide/Act/Граница (s-10, s-15, s-17, s-22, s-29, s-32), media-rich count 25/34 = 73%, исключения chapter v3 (МГТУ/Бауман/Aerostate/Sber ISS) — 0 mentions. **Но anti-anglicism cleanup не доведён до конца**: s-08 footer содержит «AI-derived / change detection / multi sensor tipping / foundation model» (визитка лекции hook!), s-16 chart содержит английские metки оси («90% accuracy» / «False positives» / «IDF self report»), + 2 визуальных артефакта рендера — ghost-overlap на s-08 («D01²/001¹») и s-27 («2024-2026»). Достаточно для REVISE.

---

## Counter-check (ENFORCED)

| Check | Result |
|---|---|
| Lec-07 pattern compliance | OK (cover + lecture-map + 5 dividers + Q&A + glossary mini); минор: cover s-02 имеет top progress bar |
| Designer-extras grep (orchestrator-independent) | **CLEAN** — 0 hits на visible body |
| LO codes / §X.X / → sNN visible | Frontmatter only — designer suppressed Visual layout instructions |
| Anti-anglicism distribution | **FAIL** — 5 P1 hits на s-08, s-09 footer, s-16 chart |
| Excluded items (МГТУ/Бауман/Aerostate/Sber ISS) | **CLEAN** — 0 mentions |
| Russian context distribution | **OK** — distributed по Р1-Р4 |
| AI-Failure strict-in ≥30% | Borderline OK ~32-35% на slide-artefact |
| Media-rich ≥50% | **PASS** — 25/34 = 73% |
| Keystone-axis discipline | **STRONG** — s-05 + s-33 callback |

---

## P0 (BLOCKING)

**Нет.** Лекция структурно показуема.

---

## P1 (significant — must fix before show)

### P1-1 — s-08 visible body anglicism leak (anti-anglicism mandate failure)
**Issue:** Footer s-08 содержит 3 неперевёденных англицизма (change detection / multi sensor tipping / foundation model) в видимом body на flagship hook-slide.
**Fix:** «change detection» → «обнаружение изменений», «multi sensor tipping» → «межсенсорное наведение», «foundation model» → «фундаментальная модель».

### P1-2 — s-08 rendering artifact (ghost text overlap)
**Issue:** NGA Luno A info-card содержит наложение текста «D01²» поверх «001¹» — render-bug, делает контракт-метку нечитаемой.
**Fix:** Очистить markdown layout, удалить дубликат «D01», re-render.

### P1-3 — s-08 satellite imagery quality / attribution mismatch
**Issue:** Hero satellite imagery на s-08 выглядит как SAR-noise/grain pattern; caption claims «Sentinel-2» (optical RGB), но изображение похоже на Sentinel-1 SAR. Либо неправильная атрибуция, либо нечитаемая иллюстрация.
**Fix:** (a) заменить на читаемую optical Sentinel-2 imagery с явным before/after pair + annotated bounding boxes, ИЛИ (b) исправить caption на «Sentinel-1» если SAR.

### P1-4 — s-16 chart axis labels English (anti-anglicism)
**Issue:** Lavender bar chart содержит английские category labels: «90% accuracy» / «False positives» / «(IDF self report)».
**Fix:** Re-render QuickChart с RU labels — «Помечено (≈ 37 000)» / «90 % точности (само-заявка ЦАХАЛ)» / «Ложные срабатывания (10 % = 3 700)».

### P1-5 — s-27 rendering artifact (ghost text overlap)
**Issue:** Эра 3 card на s-27 показывает наложение «2024-2026» — render-bug.
**Fix:** Очистить markdown layout, убрать дубликат, re-render.

---

## P2 (polish — non-blocking)

### P2-1 — Cover s-02 deviation от Lec-07 pattern
Top progress bar на cover (Lec-07 не имел). Опционально убрать.

### P2-2 — s-15 typo
«своди» → «сводки» в Palantir Maven Smart System card.

### P2-3 — Text density на s-11, s-17, s-21, s-22 (projector readability)
Compact split-layouts на грани readability; шрифт body ~12-14pt. Опционально 16pt.

### P2-4 — «redesign» / «Анти-хайп» / «продакшен»
Мелкие англицизмы. Опционально: «redesign» → «перепроектирование», «Анти-хайп» → «Без преувеличений».

### P2-5 — Strict-in borderline
~32-35% по slide-artefact (chapter ~46%). Опционально усилить ≥1 partial slide до strong (например s-25 L1-L5 → «когда L4-L5 — плохая идея» concrete failure case).

---

## Per-slide visual quality (34 slides)

| # | File | Verdict | Note |
|---|---|---|---|
| 01-07 | hook/cover/map/glossary/keystone/divider/sense-intro | PASS | All clean |
| 08 | maxar-sentry | **REVISE** | 3 issues stacked |
| 09 | constellation | POLISH | «ML» as acronym OK |
| 10-15 | RU sat / pred maint / SAR-GPS / divider / decide-intro / vendor landscape | PASS+POLISH | s-15 typo, s-15 OK vendor card |
| 16 | lavender-failure | **REVISE** | English chart labels |
| 17 | lancet-vincennes | PASS | Real photos, no LO2 badge leak |
| 18-26 | dividers / act-intro / fury / x-62a / geran / mcas-patriot / sec4-divider / l1-l5 / un-gge | PASS+POLISH | Compact text on s-21/s-22 |
| 27 | maven-shift | **REVISE** | Ghost-text «2024-2026» |
| 28-34 | hitl-trio / russia-votes / sec5-divider / 7-criteria / career-reading / closing-callback / qa | PASS | All clean |

---

## Strengths

1. **Keystone-axis discipline** — OODA s-05 + closing callback s-33 explicit
2. **Media-rich 73%** — exceptional (target ≥50%)
3. **Russian context distribution симметричен** — distributed Р1-Р4, single-source caveats visible, нет sycophancy
4. **6 strong failure-blocks** — Lavender, Lancet/Vincennes, MCAS/Patriot, ALIS, adversarial SAR, UN GGE pressure
5. **Excluded items chapter v3 mandate** — 0 mentions МГТУ/Бауман/Aerostate/Sber ISS
6. **Designer-extras grep clean** — 0 hits на visible body
7. **Honest proxy disclosures** — s-20 «YFQ-44A → Anduril Sentry», s-21 «Bayraktar TB2 → класс Saker Scout»
8. **Citations footer на каждом content slide**
9. **4 synthesis-slides подряд** s-25 L1-L5 + s-28 HITL trio + s-31 7-criteria + s-33 closing — инструменты, не риторика
10. **Lec-07 pattern compliance** в основном

---

## Recommendations Phase 8 revision

**Mandatory (P1):**
1. s-08 reflow (3 issues — anglicism + ghost text + image quality)
2. s-16 chart re-render с RU labels
3. s-27 ghost-text fix

**Polish (P2):**
4. s-15 typo «своди» → «сводки»
5. s-02 cover progress bar — рассмотреть удаление
6. Compact slides body шрифт 16pt где помещается
7. «redesign» / «Анти-хайп» russify final pass

**Не трогать:**
- 34-slide структура
- Lec-07 progress-bar pattern на section dividers
- Ocean palette / motif

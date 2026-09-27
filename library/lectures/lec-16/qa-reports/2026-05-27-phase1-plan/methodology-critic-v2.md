# Methodology re-critique — plan-v2 Лекция 16

**Дата:** 2026-05-27
**Object:** `notes/lecture-16-review/2026-05-27-phase1-plan/plan-v2.md` (8 599 слов, 597 строк, 43 outlined slides, 75 минут)
**Previous verdict:** REVISE (v1, 6 P1)
**Reader-simulator v1 input:** APPROVE-WITH-POLISH, 3 reader weak spots (keystone gloss, methane alphabet, numbers overload)
**New verdict:** **APPROVE-WITH-POLISH**

## Summary

Plan v2 закрывает все 6 P1 из v1 critique + 3 reader weak spots — **8 fix'ов addressed адекватно**, без regression на ранее approved участках. Главные структурные wins: (a) failure-share buffer **15/42 = 36% slides + 38% min + 43% words** даёт **+6pp safety margin** vs 30% threshold; (b) s05 keystone теперь содержит **inline operational definitions** «physics certainty» + «data availability» на самом слайде (не defer в speech/chapter); (c) Раздел 5 распределён по 5 слайдам (cyber + crash + 3 Russia cases) — больше нет cognitive overload в одном s37; (d) explicit **10-min Q&A buffer** в pacing math (65 active + 10 Q&A = 75); (e) **27-row vendor mapping table** с per-row anti-hype caveats делает Tools-per-quadrant taxonomy enforceable; (f) s12 «6 visible bullets» + s27 promote stripper/custody criteria из inline; (g) **s20 methane alphabet helper slide** перед первым case в Разделе 3; (h) **Numbers density rule** max 3 striking numbers per visible slide applied to s14/s16/s22/s36/s24.

Однако **3 numerical/textual inconsistencies** (P1) обнаружены в plan самом, не исправлены revision-проходом: (1) frontmatter `strict_in_failures_actual.slides: "14/42 = 33%"` противоречит body «15/42 = 36%»; (2) outline содержит **43 уникальных slide IDs** (s01-s42 + s07b), но frontmatter заявляет `slides_target: 42` и pacing math математически согласуется с 43; (3) section headers «s28-s32» / «s34-s38» counts off-by-one vs body «6 слайдов» claims. Это не структурные issues уровня P0 — это **inconsistency bookkeeping**, которые downstream agents (book-editor / designer) могут pick up как ambiguity. P0: **None**. P1: **3** (inconsistency bookkeeping cluster). P2: **2**.

**Counter-check 4-level scale:** 3 P1 issues ≤ 4 → **APPROVE-WITH-POLISH**, не REVISE. Все 8 user-requested fixes addressed адекватно; обнаруженные inconsistencies — bookkeeping, не fundamental structural. Phase 2 chapter draft **green-light** при условии что bookkeeping reconciled в plan v2.1 (5-min edit, не full re-revision).

## Per-fix verification table

| Fix | v1 issue | v2 claim | Verified? | Issues found |
|---|---|---|---|---|
| **#1 Failure share buffer** | 30.0% точно на границе (12/40) | 36% slides (15/42) + 38% min + 43% words | ✅ ADEQUATE | Frontmatter inconsistency: «14/42 = 33%» в `strict_in_failures_actual.slides` vs body «15/42 = 36%». Cross-check needed. Bucket compositionально strict-in: s07b (Aspen alert fatigue + Yokogawa shutdown — pure failure, not mixed); s37 cyber + s38 2020 crash split clean (без third-topic compression). Distribution holistic: R1=4, R2=3, R3=3, R4=3, R5=2, R6=1 — нет single-cluster concentration. **P1-A inconsistency.** |
| **#2 Keystone s05 inline gloss** | «physics certainty» defer в speech/chapter | inline definitions «Physics certainty = есть ли установившаяся численная модель...» + «Data availability» обе на slide visible body | ✅ ADEQUATE | Definitions concrete: Eclipse да / methane plume нет; 1000 wells да / 1 frontier basin нет. Bottom-left на матрице explicit. Notation locked (Q1=mainstream, Q2=methane, Q3=frontier, Q4=transition). **Слабая загрузка слайда** — 4-quadrant + 2 definitions + 4 examples + bottom bar + notation lock = много visible элементов. Designer Phase 5 должен visual-loop проверить читабельность; не структурная проблема. **P2-A density risk.** |
| **#3 Раздел 5 split** | s37 нёс cyber + 2020 crash + Deepwater в 1 слайде | Раздел 5 теперь 5 slides (s34-s38): cyber отдельно s37, 2020 crash отдельно s38, s34 divider с mini-matrix | ✅ ADEQUATE | s34 = «Россия — sanctions...» divider + Russia↔keystone mini-matrix recap; s35 = Газпром Cognitive Geo (2-2.5 min); s36 = Роснефть Digital Field + ЛУКОЙЛ/Татнефть/Сургутнефтегаз inline (numbers-cut applied); s37 = cyber +935% standalone; s38 = 2020 crash + cyclicality standalone + Deepwater Horizon chapter-anchor cross-ref. Pacing 11 min / 5 slides = 2.2 min/slide avg — acceptable. **Header inconsistency:** «6 слайдов» claim в section header / changelog vs actual 5 в outline (s34-s38). **P1-B.** |
| **#4 Q&A buffer** | 0% buffer | 65 active + 10 Q&A = 75 explicit | ✅ ADEQUATE | Math: 7+11+12+12+9+11+3 = 65 + 10 Q&A = 75 ✓. Hero s40 properly moved (was s39 в v1, now s40). s41 = Q&A frame slide; s42 = sources. Closing s39 = synthesis 4×4 matrix; s40 = hero MethaneSAT global map + bridge к Lec-17. Cleanly structured. |
| **#5 Vendor mapping table** | 38 vendors named, only ~22 enforced via slide/speech | 27-row Vendor → slide / speech-anchor mapping в § Tools-per-quadrant | ✅ ADEQUATE | All major Q1-Q4 vendors covered (Ambyint, Aspen, Honeywell UOP, Yokogawa, ABB, Emerson, Osprey, SLB Avocet, Halliburton, Nabors, Aramco, Eni, SLB Lumi, Exxon, BP+Beyond Limits, IBM+Repsol, Eclipse/INTERSECT/CMG/OpenFOAM, MethaneSAT, Carbon Mapper/GHGSat/Bridger, SeekOps/Project Canary, FLIR/Opgal/Picarro/LI-COR, Northern Lights, Fervo, Aker/Eavor/Sage/Quaise, Газпром, Роснефть, Татнефть/ЛУКОЙЛ/Сургутнефтегаз, Cognitive Pilot/AIQ, Cognite/C3.ai, NVIDIA/AMD/HPE/cloud, Dragos/Claroty/Nozomi). **Each row** has anti-hype оговорка (alert fatigue 100s/day, $1.8B = 0.4% revenue, mode≠brand, 1.5 Mt vs 7.6 Gt = 0.02%, etc.). LO16.3 (vendor adoption direction) now executable. |
| **#6 s12 «Когда AI не нужен в Q1»** | 2 critéria inline (stripper, custody) | dedicated s12 с 6 visible bullets | ✅ ADEQUATE | 6 bullets distinct: (1) mature reservoir → Eclipse classical; (2) stripper <10 bopd → unit economics; (3) custody transfer → regulatory mass flow; (4) BOP → deterministic; (5) frontier no analog → preview R2; (6) EU Methane Reg traceability → no black-box. Все 6 — structural criteria, не surface caveats. Cross-ref к s27 (custody also bullet 3) + s33 (BOP also alternative). **Pacing 2 min / 6 bullets** = 20 sec/bullet, tight но executable если bullets one-line. **P2-B time-tight.** |
| **#7 s20 methane alphabet helper** | OGI/OGMP/MRV/LDAR/SIL drop-in без gloss | dedicated s20 glossary slide ДО первого Q2 case | ✅ ADEQUATE | 7 acronyms decoded inline на slide visible (per body спецификации строка 270): MRV / OGI / LDAR / OGMP 2.0 / SIL / bopd / intensity. RU translations qualitative (МRV = «выявление-учёт-проверка» — не просто abbreviation expansion). 1.5 min adequate если slide structured как 2-column glossary (term → definition). Russification gloss policy fits. |
| **#8 Numbers density rule** | s14 7+ numbers / s33 7+ numbers overload | new § «Numbers density rule» max 3 visible per slide; s14/s16/s22/s36/s24 explicit rewrites | ✅ ADEQUATE | Per-slide explicit applied: s14 → 6 visible (3 Eni + 3 Aramco; OK как 2 separate sub-blocks по 3); s16 → 3 visible (Grace Hopper count + $1B unlock + 6 FPSO); s22 → 1 striking + baseline (410 t/h = 50% выше EPA); s36 → 3 visible (23 software + 1 Mt/год + 1B руб.). Speech-anchor explicit для overflow numbers. s24 vendor landscape capped to 3 visible (Carbon Mapper + GHGSat + Bridger; SeekOps/Project Canary speech). **Edge case s14:** 6 numbers visible на одном слайде даже если split в 2 blocks — exceeds rule literally, но designer может render как 2 logical zones и pass читабельность. **P2-C ambiguity rule application.** |

## Regression checks

| Check | Status | Notes |
|---|---|---|
| Variant B keystone (data × physics) still primary | ✅ PASS | s05 explicit; Q1/Q2/Q3/Q4 notation locked; no drift к Variant A/C/D |
| 8 LO measurable preserved | ✅ PASS | LO16.1-LO16.8 unchanged; each LO tied к specific раздел (LO16.3 vendor mapping теперь executable thanks to fix #5) |
| Anonymization (no МГТУ / ИУ-N / РГУ Губкина) | ✅ PASS | Anti-list consolidated (P2-1 cleanup applied); RGU duplicate устранён; audience universal |
| Russification table expanded ≥45 entries | ✅ PASS | 50+ entries (downhole, frontier exploration, OGI/LDAR/MRV/OGMP, SIL3/SIL4/BOP/PRV/ESD/SIS/APC, ESP/rod pump/gas lift, FPSO/custody transfer/plume migration, intensity, PINN, HPC/NOC/IOC/CCS/EGS, pilot purgatory, black-box, edge case, etc.) |
| Brand allowlist comprehensive | ✅ PASS | Companies + Products + Standards + Russian-specific все present; Bridger Photonics + SeekOps + AIQ + Cognitive Geo все добавлены per P1-5 cleanup |
| 10 documented failures distributed | ✅ PASS | R1=2 (s07, s07b), R2=2 (s17, s18), R3=2 (s23, s25), R4=2 (s31, s32), R5=2 (s37, s38), + bonus Deepwater Horizon chapter anchor (s38 cross-ref) + 86% pilot s07. No single-section stuck. |
| Hero s01 + s40 preserved | ✅ PASS | s01 = Permian VIIRS night (Tier 1 NASA + Tier-A Eagle Ford/Bakken fallback + Tier-B Deepwater); s40 (was s39 in v1) = MethaneSAT global map. ID shift updated всюду (hero_required: [s01, s40], Diagrams expected, 6-tier media plan). |
| No timing/methodology в visible body | ✅ PASS | Plan-internal pacing OK (exempt per CLAUDE.md); section dividers «Q1 — Mature production: AI как multiplier» + tag «3 working cases · 2 структурных провала» БЕЗ минут; s41 Q&A frame «БЕЗ 10 минут visible». Plan explicit constraint. |
| Baseline / counterfactual coverage | ✅ PASS | Sample claims sampled: Ambyint +15% (per-well historical mean + Permian 100-500 bopd); Aramco $1.8B (vs $440B revenue = 0.4%); Honeywell UOP 310 units (vs ~700 global refineries); Eni HPC6 (Top500 #5 of 500); Roснефть +1 Mt (vs Башнефть ~17 Mt = +5.9%); Northern Lights 1.5 Mt (vs IEA 7.6 Gt = 0.02% + 190× gap); Fervo 150 GW (vs current 3.7 GW = 40× ceiling). Все measurable claims имеют inline baseline. |
| Anti-pattern grep | ✅ PASS | 0 hits «магическая пилюля», «УГАДАЙ», «инженер ИУ6», «методически важно», «на этом этапе студент», «Лектору», «методический»  — все clean. |

## P0 issues (BLOCKING)

**None.**

Все ENFORCED-правила курса в plan v2 acknowledged: strict-in failures ≥30% holistic (36% / 38% / 43%), keystone предъявлен на s05 ДО первого погружения с inline operational definitions, anonymization clean, Russification 50+ entries, tools-per-quadrant taxonomy enforceable, baseline coverage strong, hero s01+s40 verified, anti-patterns 0 hits.

## P1 issues (HIGH — fix before chapter draft)

### P1-A. Frontmatter `strict_in_failures_actual.slides` numerically inconsistent с body

**Где:** plan-v2.md строка 17 vs строки 31, 360, 385, 578, 596.

**Issue:** Frontmatter:
```yaml
strict_in_failures_actual:
  slides: "14/42 = 33%"   ← stale
  minutes: "28/75 = 37%"  ← stale (body claims 28.5 / 38%)
  words: "~13000/30000 = 43%"
```

Body везде «15/42 = 36%», «28.5 min из 75 = 38%».

**Impact:** Downstream agents (book-editor / designer / methodology-critic Phase 3) могут pick up frontmatter як canonical metadata vs body как narrative. Different agents getting different numbers → cascade ambiguity. Especially проблема если Phase 3 critic runs `grep` for failure-share value — frontmatter дёрнет «33%» который меньше strict-in target 35% target frontmatter line 15.

**Fix:** Sync frontmatter:
```yaml
strict_in_failures_actual:
  slides: "15/43 = 35%"    # see P1-B below — actual slide count 43
  minutes: "28.5/75 = 38%"
  words: "~13000/30000 = 43%"
```

Or alternatively keep 14/42 = 33% и dropнуть s07b как «BUFFER» обратно — но это reverts fix #1. **Preferred: sync up.**

**Severity:** P1 (не P0) потому что body numbers correct + holistic check passes; но frontmatter — это first thing downstream agents читают.

---

### P1-B. Slide count outlined 43 vs `slides_target: 42` (off-by-one)

**Где:** plan-v2.md frontmatter строка 21 + section headers «s28-s32» (Раздел 4) / «s34-s38» (Раздел 5).

**Issue:** Outline body содержит **43 уникальных slide IDs** (s01-s42 = 42 + s07b = 43). Frontmatter заявляет `slides_target: 42`. Section headers:
- Раздел 4: «s28-s32, 6 слайдов» — но s28-s32 это 5 IDs, не 6. Actually outline body содержит s28+s29+s30+s31+s32+s33 = **6 slides for Раздел 4** (s33 sits in R4 body, не R5). So header «s28-s32» wrong — should be «s28-s33».
- Раздел 5: «s34-s38, 6 слайдов» — но s34-s38 это 5 IDs (s34+s35+s36+s37+s38). Changelog P1.3 claims «6 слайдов (s33-s38)» — но s33 in R4 body. So Раздел 5 actually **5 slides**, not 6.

**Re-tally:**
- R0: s01-s05 = 5
- R1: s06-s12 + s07b = 8
- R2: s13-s19 = 7
- R3: s20-s27 = 8
- R4: s28-s33 = 6
- R5: s34-s38 = 5
- R6: s39-s42 = 4
- **Total: 43 slides** (not 42)

**Impact:** Frontmatter `slides_target: 42` будет triggered as inconsistency Phase 5 designer prompt. Section header ranges wrong — designer создаст s28-s32 thinking «5 slides for R4», но outline body says 6. Cascade confusion.

**Fix:** Sync — either:
- (Option A) **frontmatter `slides_target: 43`** + fix headers Раздел 4 «s28-s33, 6 slides» + Раздел 5 «s34-s38, 5 slides»; OR
- (Option B) **drop s07b** обратно (reverts P1.1 fix); OR
- (Option C) renumber so s07b → s07.5 or merge two failures into one bigger slide — но это reverts P1.1 + P1.3 structural fixes.

**Preferred: Option A** (cleanest accounting; 43 ∈ acceptable range 41-43 per plan строка 595).

**Severity:** P1. Mechanical fix (~3 lines edit), но downstream cascade if не resolved.

---

### P1-C. Раздел 5 slide-count claim «6 слайдов» vs actual 5 (P1.3 fix wording overshoot)

**Где:** plan-v2.md строки 33, 292, 321 + section header «### Раздел 5 — Россия + cross-cutting (≈11 минут, s34-s38, 6 слайдов — P1.3 fix)».

**Issue:** Changelog P1.3 fix говорит «Раздел 5 пересобран на 6 слайдов (s33-s38)» — но s33 структурно sits в Раздел 4 outline body как «ALTERNATIVE: Physics-based simulators + classical APC». Раздел 5 outline body содержит только s34-s38 = 5 slides. Pacing math line 321 «Раздел 5: 11 min (6 slides — Russia + cyber + crash)» — но если 5 slides на 11 min = 2.2 min/slide acceptable; если 6 slides на 11 min = 1.83 min/slide tighter но also OK.

**Reality:** Plan v1 had R5 = 5 slides 10 min. v2 claim «split cyber and 2020 crash» создаёт +1 slide → R5 = 6 slides. **Но outline body shows только 5** (s34 divider + s35 Газпром + s36 Роснефть + s37 cyber + s38 crash) — no 6th slide. Either:
- (a) Plan v2 forgot to split s36 Роснефть и s36-extra Татнефть/ЛУКОЙЛ/Сургутнефтегаз (currently они в s36 inline); OR
- (b) Plan v2 should claim «5 слайдов» not «6».

**Linked к P1-B above** — consistent fix.

**Fix:** Either добавить 6th slide (s36b Татнефть/ЛУКОЙЛ/Сургутнефтегаз standalone) OR update header «5 слайдов» + changelog «5 слайдов (s34-s38)». Plan v2 should pick.

**Severity:** P1. Bookkeeping; cascading с P1-A/P1-B.

---

## P2 issues (LOWER — polish, можно отложить)

### P2-A. s05 keystone visual density risk

**Где:** plan-v2.md строки 99-114.

**Issue:** s05 теперь содержит: 4-quadrant 2×2 matrix + Q1/Q2/Q3/Q4 examples (4 named) + Physics certainty operational definition (с Eclipse / methane examples) + Data availability operational definition (с 1000 wells / 1 frontier examples) + bottom bar «alternative tool» reminder + notation lock note. That's **6+ visual zones** на single slide. Risk: текст переполнен, читабельность low.

**Fix (P2):** Phase 5 designer prompt должен explicit instruction «visual-loop 3× minimum + readability check за 5 sec sweep». Mitigation already: plan строка 570 mentions visual-loop. Не блокирует chapter draft.

### P2-B. s12 «6 bullets» в 2 min — tight pacing

**Где:** plan-v2.md строки 246-253.

**Issue:** 6 bullets × 20 sec/bullet = 2 min total. Acceptable если bullets one-line each, no deep dive. Speech-anchor для each bullet — должен быть explicit pointer.

**Fix (P2):** Phase 9 speech-writer brief должен включать «s12 — 6 bullets × 20 sec, one-line; deeper explanation per bullet → chapter §Q1 criteria».

### P2-C. Numbers density rule edge case — s14 has 6 visible numbers

**Где:** plan-v2.md строки 259 + 331.

**Issue:** s14 visible: «606 PFLOPS Top500 #5 + 14k AMD MI250X + $104M» (3 Eni) + «250B params + 90 лет data + $1.8B realized 2024» (3 Aramco) = **6 numbers**. Plan claims «max 3 striking numbers visible per slide» — но slide содержит 2 separate vendor sub-blocks по 3 numbers each. Strict reading rule violated; loose reading allows because cognitive groupingsэ separate.

**Fix (P2):** Plan v2.1 либо relax rule до «max 3 numbers per cognitive zone, max 2 zones per slide», либо split s14 на s14a (Eni) + s14b (Aramco). Currently plan keeps single s14 — designer Phase 5 visual-loop проверит читабельность. Не блокирует chapter draft.

## Rationale verdict

**APPROVE-WITH-POLISH — not REVISE.**

8 user-requested fixes (6 P1 + 2 reader weak spots P1 + 1 P2 numbers consolidation) **all addressed адекватно**:
- Failure share buffer real: 36% / 38% / 43% comfortable +6pp / +8pp / +13pp margins.
- Keystone s05 inline definitions concrete с examples per quadrant.
- Раздел 5 cognitive overload устранён через cyber+crash split.
- Q&A buffer 10 min explicit, pacing math sums к 75.
- Vendor mapping table 27-row enforceable, LO16.3 executable.
- s12 6 visible bullets structural (не inline).
- s20 methane alphabet helper present ДО first case.
- Numbers density rule applied to 5 specific slides.

Все 8 regression checks PASS: Variant B keystone, 8 LO, anonymization, Russification 50+, brand allowlist, 10 failures distributed, hero s01+s40, no timing/methodology, baseline coverage, anti-pattern grep 0 hits.

**Counter-check 4-level scale:** 3 P1 issues (P1-A frontmatter inconsistency, P1-B slide count off-by-one, P1-C R5 slide count claim) — **bookkeeping cluster, не fundamental gaps**. ≤4 P1 = APPROVE-WITH-POLISH per rule (≥5 = REVISE). Three P1 are mechanical fixes (~5 min sync edit), не require full re-revision pass.

**Если P1-A/P1-B/P1-C resolved в plan v2.1 (frontmatter sync + section header sync + changelog wording fix) → APPROVE-CLEAN.**

## Recommendation для Phase 2 chapter draft

### Green-light для Phase 2 — **YES, conditionally**

Phase 2 chapter draft (book-editor) **может стартовать с plan v2 as input** при условии что P1-A/P1-B/P1-C resolved через **5-минутный sync edit** в plan v2.1 ДО Phase 2 spawn. Этот sync edit:

1. **Frontmatter:**
   ```yaml
   slides_target: 43           # (был 42)
   strict_in_failures_actual:
     slides: "15/43 = 35%"     # (был «14/42 = 33%»)
     minutes: "28.5/75 = 38%"  # (был «28/75 = 37%»)
     words: "~13000/30000 = 43%"
   ```

2. **Section headers:**
   - `### Раздел 4 — Q4: Energy transition CCS + EGS (≈9 минут, s28-s33, 6 слайдов)` (было «s28-s32»)
   - `### Раздел 5 — Россия + cross-cutting (≈11 минут, s34-s38, 5 слайдов — P1.3 fix)` (было «6 слайдов»)

3. **Changelog P1.3 wording:** «Раздел 5 пересобран на 5 слайдов (s34-s38) + s33 alternative оставлен в Раздел 4» (corrected, не «6 слайдов (s33-s38)»).

4. **Pacing math line 321:** «Раздел 5: 11 min (5 slides — Russia + cyber + crash)» (corrected).

### Plan v2 → Phase 2 (book-editor) brief — additional context

- **Chapter target ≥30 000 слов** (CLAUDE.md ENFORCED для L4+; Лекция 16 ∈ L4+).
- **Multi-part split:** 4 файла (chapter.md + chapter-part2.md + part3 + part4), каждый ≤600 строк, ~7-8k слов each.
- **Slide-маркеры `[for-slide-sNN]` policy** explicit в Notes для downstream phases (plan строка 567): §intro → s01-s05; §Q1 → s06-s12 + s07b; §Q3 → s13-s19; §Q2 → s20-s27; §Q4 → s28-s33; §Russia → s34-s38; §Closing → s39-s42.
- **Inline gloss policy (P2-7 / reader-simulator):** first appearance каждого of {wildcat, FPSO, 4D seismic, plume migration, downhole, basin/play, stripper well, bopd, intensity, PINN, OGI, OGMP, LDAR, MRV, SIL3/SIL4, BOP/PRV/ESD/SIS, APC, ESP} — inline one-line gloss.
- **Failure-share для chapter:** ≥43% strict-in (target plan claim; minimum holistic ≥30% per CLAUDE.md AI-Failure Rule).
- **Baseline mandate:** все measurable claims inline base / counterfactual / denominator.
- **No timing / methodology в visible body** (ENFORCED per CLAUDE.md «No Timing / No Methodology in Slides» Rule — также applies к chapter где relevant).
- **Russification deep:** chapter narrative должен использовать RU перевод per Russification table (50+ entries); англицизмы only via brand allowlist.
- **Tier-1 `[VFY-day-of]` markers** (3 items per строка 545-548): Aramco METABRAIN params, US EPA Subpart W status, Aramco $1.8B realized — **resolve ДО chapter draft submission** (Phase 3 fact-checker priority).

### Risk inputs для Phase 3 (methodology-critic + fact-checker)

- **Phase 3 word count check:** <28 500 для L4+ = P0 BLOCKING.
- **Phase 3 holistic failure-share check:** ≥30% strict-in в каждом из 3 артефактов (chapter / slides / speech).
- **Phase 3 baseline sample check:** 5-7 measurable claims с inline base.
- **Phase 3 fact-checker priority:** 3 Tier-1 `[VFY-day-of]` markers + s07b «Yokogawa Idemitsu plant-wide pilot 2018+ closed» — currently failure inference, needs verify (per Risk 5 строки 588-590).

---

**Files referenced:**
- `/tmp/lec-16-wt/notes/lecture-16-review/2026-05-27-phase1-plan/plan-v2.md` (597 строк, 8 599 слов, 43 outlined slides)
- `/tmp/lec-16-wt/notes/lecture-16-review/2026-05-27-phase1-plan/plan-v1.md` (для diff)
- `/tmp/lec-16-wt/library/lectures/lec-16/qa-reports/2026-05-27-phase1-plan/methodology-critic.md` (v1 6 P1)
- `/tmp/lec-16-wt/library/lectures/lec-16/qa-reports/2026-05-27-phase1-plan/reader-text-only.md` (v1 3 weak spots)
- `/home/levko/AI-usage-lessons/CLAUDE.md` (AI-Failure Rule, Chapter Depth Baseline, Anti-Patterns, Pre-USER-GATE, No Timing/Methodology)
- `/home/levko/AI-usage-lessons/tools/lecture-production/README.md` §3.6

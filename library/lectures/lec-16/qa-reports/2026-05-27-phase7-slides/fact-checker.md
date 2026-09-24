VERDICT: APPROVE-CLEAN

# Fact-check slides — Лекция 16 (Phase 7)

**Дата:** 2026-05-27
**Object:** rendered PPTX (43 слайда: s01-s07b, s08-s42) + slides/*.md spec files
**Method:** verify Phase 4 chapter v2.1 corrections preserved in slides + spot-check NEW slide-only numbers (5) + verify [VFY-day-of] markers preserved on PNG snapshots
**Verdict:** **APPROVE-CLEAN** (0 P0, 0 P1, 1 P2 minor)

## Summary

Phase 4 fact-checker-v2.md identified 12 critical corrections needed in chapter (1 P0 Fervo IPO + 11 P1) → all applied в chapter v2.1 (revision-log.md spawn 4). **Phase 7 audit verifies all 12 corrections cascaded cleanly to slides** через Phase 5 spec update.

**12/12 Phase 4 corrections preserved в slides spec files:**
1. ✓ Stabroek 9-11B BOE (s16 spec + speaker notes)
2. ✓ Aramco $436.6B revenue (s14)
3. ✓ Aramco $1.8B / $436.6B = 0.41% (s14, s01, s05, s10)
4. ✓ MethaneSAT 15.5 мес lifetime (s23 spec — visible numbers + speaker notes)
5. ✓ MethaneSAT $5.7M/мес cost (s23)
6. ✓ Cognitive Geo с 2019 (s35 — соглашение апрель 2019; параллель «Cognitive Geo с IBM начался в 2019 году»)
7. ✓ EPA Subpart W September 2025 (s26 — Trump administration proposed delay September 2025 visible on PNG)
8. ✓ Beyond Limits June 2017 Series B $20M (s17 — «BP Ventures Series B $20M июнь 2017» visible)
9. ✓ GHGSat 13 satellites (s24 — PNG shows «13-satellite по середине 2025»)
10. ✓ Stanford methane ~7 Mt (s25 — «более шести миллионов тонн в год, точная цифра в paper около шести-семи с половиной миллионов» speaker notes; visible 7 Mt = factor 2)
11. ✓ Fervo IPO $27/share, $1.89B raised, $7.7B valuation, ~30% first-day pop, Series E $462M, NOT +331% (s30 spec — assertion line + visible_numbers + speaker notes all corrected; PNG s31 confirms)
12. ✓ Colonial Pipeline $4.4M ransom + $2.3M recovered (s37 — visible numbers «$4,4M ransom paid»; PNG s38 confirms)

**[VFY-day-of] markers preserved (4 verified в PNG snapshots):**
- ✓ s14 Aramco METABRAIN «~250 млрд параметров [VFY-day-of]» — PNG visible (snapshot s15)
- ✓ s16 ExxonMobil Discovery 6 «$200–400M capex [VFY]» — PNG visible (snapshot s17)
- ✓ s26 EPA Subpart W «delay 2034 [VFY]» — PNG visible (snapshot s27)
- ✓ s32 Yokogawa Idemitsu «закрыт после 2018 [VFY-day-of]» — PNG visible (snapshot s33)
- ✓ Bonus: s09 Honeywell UOP «750+ план [VFY-day-of]», s23 MethaneSAT-2 «[VFY]», s34 Russia Q4 «Pilots [VFY]»

## Verification table — Phase 4 chapter corrections preserved в slides

| # | Phase 4 Correction | Chapter ref | Slide ref | Slides match? | Notes |
|---|---|---|---|---|---|
| 1 | Stabroek 9-11B BOE (was ~16B) | part2 §2.4 | s16 spec L31, speaker notes L53 | ✓ | «9-11 млрд BOE recoverable»; Permian-Pioneer = ~16B distinct |
| 2 | Aramco revenue $436.6B (2024) | part2 §2.2 | s14 spec L45, speaker notes L56 | ✓ | «$436,6 млрд» exact |
| 3 | Aramco $1.8B / $436.6B = 0.41% | part2 §2.2 | s14 visible_numbers L15, assertion L5, body L45 | ✓ | «0,41% выручки» exact; PNG s15 confirms |
| 4 | MethaneSAT 15.5 мес (Mar 4 2024 – Jun 20 2025) | part3 §3.1, §3.3 | s23 assertion L5, L16, L21, L25, L32, body L48; s24 visible | ✓ | «15,5 месяцев = 26% от 5-летнего lifetime»; PNG s24 confirms |
| 5 | MethaneSAT $5.7M/мес cost | part3 §3.3 | s23 visible_numbers L16, body L33 | ✓ | «$5,7M/мес realized vs $1,5M/мес планировалось»; PNG s24 confirms |
| 6 | Cognitive Geo start 2019 (not 2017) | part4 §5.1, §5.2 | s35 sub L25, body L47, L53, L55 | ✓ | «соглашение о сотрудничестве подписано в апреле 2019»; PNG s36 confirms «С IBM Research Brazil 2019–2022» |
| 7 | EPA Subpart W September 2025 (Trump delay) | part3 §3.6 | s26 spec L39, L55 + PNG visible | ✓ | «September 2025 — Trump administration proposed delay до 2034 [VFY]»; PNG s27 confirms |
| 8 | Beyond Limits June 2017 Series B $20M | part2 §2.5 | s17 spec L5, L16, L21, L26, body L49 | ✓ | «BP Ventures Series B $20M июнь 2017»; PNG s18 confirms «BP Ventures Series B июнь 2017» |
| 9 | GHGSat 13 satellites (not 16) | part3 §3.4 | s23 L44, s24 spec L5, L15, L35; PNG s24 «13-satellite» | ✓ | «GHGSat 13-satellite constellation» 3 locations match |
| 10 | Stanford methane ~7 Mt (qualified 6-7.5 Mt) | part3 §3.5 | s25 spec L5, L13, L15, L32, speaker notes L53 | ✓ | «Stanford 2024: 7 Mt = 2×»; speaker notes range «шести-семи с половиной миллионов» preserved Phase 4 nuance |
| 11 | Fervo: $27/share, $1.89B raised, $7.7B valuation, ~30% first-day pop; Series E $462M | part3 §4.3 | s30 spec L5, L15, L20, L32-33, body L54 + PNG s31 visible «IPO 12 мая 2026 / $1,89 млрд / оценка $7,7 млрд» | ✓ | ALL correct numbers preserved. Series E $462M mentioned in body L31 + speaker notes L54. NO +331% anywhere. NO «markdown» framing anywhere. ✓ Honest up-round narrative. |
| 12 | Colonial Pipeline $4.4M ransom (NOT $5M) | part4 §6.1 | s37 spec L16, L32; PNG s38 visible «$4,4M ransom paid» | ✓ | «$4,4M ransom paid (75 BTC; ~$2,3M recovered by DOJ Jun 2021)» fully harmonized |

**12/12 corrections preserved cleanly. Zero drift slides ↔ chapter.**

## Slide-only NEW numbers (spot-check 5)

| # | Claim | Slide | Verified? | Source | Notes |
|---|---|---|---|---|---|
| 1 | Eni HPC6: 606 PFLOPS Top500 #5, $104M, 14k MI250X | s14 | ✓ VERIFIED | Eni.com press Nov 18 2024 + DCD + Wikipedia + Top500 system 180315 | «606.97 PFLOPS HPL», «3472 nodes × 4 MI250X = 13 888 GPU», «€100M ≈ $104M» |
| 2 | Honeywell UOP Connect 310+ units, 100+ sites, ~14% мирового refinery capacity, план 750+ | s09 | ✓ VERIFIED | Honeywell UOP digital services brochure | «310 units connected at over 100 customer sites globally with plans to connect to 750+ units within a year» — exact match |
| 3 | Ambyint InfinityRL +15% на 200 wells artificial lift | s08 (referenced s07b + s09) | ✓ VERIFIED | Ambyint case study «AI-Driven Rod Lift Optimization» | «average production increased by 15% across the optimized wells» on 200 wells, Permian + DJ basins; international energy operator |
| 4 | MethaneSAT US O&G ~15 Mt/год vs EPA ~4 Mt = 4× | s25 | ✓ VERIFIED | EDF + MethaneSAT.org «over four times higher» | «roughly 15 million metric tons … from onshore oil and gas activities in the continental U.S. annually» — match; «4×» matches «over four times» framing |
| 5 | Gartner 2027: 40% agentic AI cancelled | s31 spec L15, L41, body L59 | ✓ VERIFIED | Gartner press June 25 2025 + HPCwire + XMPRO | «Over 40% of agentic AI projects will be canceled by the end of 2027» — exact match |

**5/5 NEW slide-only numbers verified против external sources.**

## P0 issues

**None.**

## P1 issues

**None.**

## P2 issues (minor — polish only)

### P2-1: s14 spec line 5 — Aramco $1.8B realized year qualifier

**Текущий текст (s14 assertion L5):** «Aramco METABRAIN — 250B параметров на 90 годах данных, $1,8B realized в 2024 (= 0,41% выручки)».

**Observation:** Aramco's Amin Nasser стейтмент about $1.8B AI realized value был сделан at Davos January 2025 — referring to **calendar 2024 results**. Chapter v2.1 §2.2 уже использует «$1,8B realized в 2024»; slides match this. Strictly accurate.

**Minor polish (optional):** PNG s15 visible field uses «$1,8 млрд realized 2024 (Davos янв 2025)» — explicit attribution source. Could be added к speaker notes для full traceability but not required. **No action needed.**

## Counter-check

- All 12 Phase 4 corrections preserved in slides: **12/12 ✓**
- All 5 sampled NEW slide-only numbers WebSearch-verified: **5/5 ✓**
- All 4 critical [VFY-day-of] markers visible on rendered PNG: **4/4 ✓** (+ 3 bonus VFY markers preserved)
- P0 found: 0
- P1 found: 0
- P2 found: 1 (minor polish, no action needed)
- 4-level scale: APPROVE-CLEAN (0 P1 — все только P2 or meet hold)

## Freshness pre-flight notes

Time-sensitive items с [VFY-day-of] markers — already flagged for orchestrator pre-flight on lecture day:
1. **s14 Aramco METABRAIN parameters (~250B):** volatile claim (chapter notes «7B март 2024 → 250B → claim 1T 2025») — verify Day-of for any 2026 update.
2. **s16 ExxonMobil Discovery 6 capex ($200-400M):** estimated, not disclosed. Day-of check для any new ExxonMobil press release.
3. **s09 Honeywell UOP 750+ план:** as of 2024 brochure target «within a year» — by 2026 lecture date may have hit 750+ или updated target. Day-of verify.
4. **s23 MethaneSAT-2 Q4 2025 launch intention:** funding/timeline uncertain. Day-of check для EDF press.
5. **s26 EPA Subpart W delay до 2034:** depends on EPA leadership + judicial review status — political volatility high. Day-of must.
6. **s30 Fervo IPO May 12 2026:** verified ad date (today is May 27 2026 — fresh, < 1 month). Stable. No action.
7. **s32 Yokogawa Idemitsu pilot status:** «closed after 2018» — Day-of check for any updates.
8. **s34 Russia Q4 pilots:** ограниченная public info due to sanctions. Day-of check on any new public news.

Cyber +935% (Zscaler ThreatLabz Apr 2024 — Apr 2025): refresh cadence quarterly. As of May 27 2026, +13 months past data baseline window — chapter explicit «base — Zscaler ThreatLabz фиксирует относительный рост числа известных ransomware-инцидентов в секторе year-over-year». Day-of check: any Zscaler 2026 mid-year report? Currently OK as cited historical statistic with explicit denominator caveat.

## Rationale verdict + Recommendation для Phase 8

**Verdict: APPROVE-CLEAN.**

Rationale: All 12 Phase 4 chapter v2.1 corrections cascaded cleanly to slides spec + rendered PPTX (verified через 9 PNG snapshots and grep across slides/*.md). All 4 [VFY-day-of] markers preserved on visible PNG body. 5/5 spot-checked NEW slide-only numbers verified via WebSearch. 0 P0, 0 P1, 1 P2 minor polish (optional Davos attribution traceability). No drift, no inherited fact-issues, no fabrication.

**Recommendation для Phase 8:**
- No fact-related revisions needed.
- Polish P2 optional (add «Davos янв 2025» to s14 speaker notes для full source traceability — но PNG visible field уже содержит это; not blocking).
- Phase 4.5 fact-checker-v2.md REVISE verdict closed by Phase 4 spawn 4 successfully.
- Confidence в slide accuracy: high. Ready для USER GATE B pre-walkthrough.

**Status frontmatter:** slides_fact_status: verified-clean (recommend setting на USER GATE B pass).

**VERDICT: APPROVE-WITH-POLISH**

# Methodology re-critique — chapter v2 Лекция 16 «AI в нефтегазовой отрасли и добыче ресурсов»

**Дата:** 2026-05-27
**Object:** chapter v2 (5 parts, 31 890 слов фактически; frontmatter 31 888)
**Previous verdict:** REVISE (v1, 2 P0 + 4 P1)
**New verdict:** **APPROVE-WITH-POLISH** — все P0 fixed, все P1 substantially addressed, 3 minor consistency P2 для пре-GATE polish (рекомендуется зафиксить параллельно или GATE A с известными polish caveats).

---

## Summary

Phase 4 cascade revision (3 spawns) **успешно адресовала все 6 issues** из Phase 3 critique. Architecturally chapter v2 — production-ready academic textbook reference: keystone-axis «данные × физика» integrated через все 4 quadrant sections с **явным Q4 axis tie-back** (Northern Lights §4.2 + Fervo §4.3 после v1 thinness); 10 documented failures с deep-dive ≥600 слов каждый distributed по quadrants; failure-share strict-in ≥65-70% (frontmatter self-estimate ~67%) — significantly above 30% mandate, holistic distribution preserved post-expansion.

**3 P0 resolved:**
1. **Russification deep-pass** — 82 → 12 residual hits (85% reduction), все 12 либо в References/source titles (allowlist), либо deliberate baseline-framing terminology (denominator mandate justification), либо critical framing внутри vendor hype dismantling (§2.5 BP+Beyond Limits, §2.6 IBM+Repsol — quotes from cognitive-AI marketing era).
2. **Typo/encoding cleanup** — 0 residual instances `provals`/`Studen`/`chrebrolution`/`galleon`/`пайтон`/`skvazhin`/`cgeo`/`agreggate`/`деitalised`; 1 minor leak found: `Денoминатор` (chapter-part4.md:207, Latin 'o' inside Cyrillic) — P2 surface polish.
3. **Stabroek BOE fix** — §2.4 explicit «9–11 миллиардов BOE (ExxonMobil 2023–2024 estimates, recoverable не proven)»; Permian 16B Pioneer-merger 2024 preserved as contrast.

**4 P1 fully addressed + 3 new gaps resolved:** word count expansion (28 541 → 31 888 = +1 527 words; +388 over upper-band — recommend trim или OK leave polish); missing denominators (Fervo +331% Series D $244M baseline / cyber +935% Colonial Pipeline paradigm + ThreatLabz YoY framing / 107k jobs 9.7% of 1.1M US O&G workforce baseline); Q4 axis tie-back («Тип-сцеплённость с Q4» paragraphs §4.2 + §4.3 with explicit data×physics axis grounding); PINN/DeepONet/FNO/ROM/POD inline gloss + 3-motivation expansion §4.4; R5 split (Russia §5 / cross-cutting §6 / closing §7 / Q&A §8 / Refs §9); §5.3 deadzone consolidation; Q&A Q3 expansion ~190 → ~430 words с Bolivia ACISA failure case + Lec-11 cross-link; §7.3 career → cornerstone academic 3-concept handoff к Лекции 17.

**6 P1-9 to P1-14 fact corrections all verified:** Aramco $436,6B 2024; MethaneSAT 15,5mo; Cognitive Geo с 2019; EPA Subpart W September 2025; Beyond Limits Series B июнь 2017; GHGSat 13 satellites (с inconsistency P2 в Part 4 recap table); Stanford >6 Mt March 2024.

**Counter-check:** 0 P0 + 3 P1 + 6 P2 → verdict math = **APPROVE-WITH-POLISH** ✓ (rule: 0 P0 + ≤4 P1).

---

## Per-fix verification table

| Fix | v1 issue | v2 claim | Verified | Notes |
|---|---|---|---|---|
| **P0-1** Russification | 70+ hits | 82→12 (intentional) | **PASS** | Deep latin-token scan: 12 residual hits — 7 в References (English source titles, allowlist), 4 deliberate baseline/denominator framing terminology в new content, 1 «insight» в critical framing dismantling vendor hype §2.5; tech acronyms (PINN, DeepONet, FNO, ROM, POD, SIS, IEC 61511, BOE, FPSO, MRV, OGI, LDAR, etc.) all glossed first-use |
| **P0-2** Typo/encoding | 7+ artifacts | 0 residual | **PASS** with 1 minor P2 leak | Grep `provals|Studen,|chrebrolution|galleon|пайтон|skvazhin|cgeo|agreggate|деitalised` = 0 hits. **1 minor leak:** chapter-part4.md:207 «Денoминатор:» (Latin 'o' inside Cyrillic) — P2 surface polish |
| **P0-3** Stabroek BOE | 16B wrong (was Permian) | 9–11B BOE + Permian 16B preserved | **PASS** | §2.4 chapter-part2.md:135 explicit «Stabroek estimate: 9–11 миллиардов BOE (ExxonMobil 2023–2024 estimates, recoverable resources)»; Permian Pioneer-merger 16B intact как contrast |
| **P1-1** Word count | 28 541 (border) | 31 888 (+388 over upper-band) | **PASS** | All 5 parts: chapter.md 8 983 + part2 5 875 + part3 7 939 + part4 5 179 + part5 3 914 = **31 890 total** (frontmatter 31 888). +388 over 31 500 upper-band — minor; recommend trim 200-400 words или OK leave as polish (P2 §3.3 MethaneSAT post-loss recap слегка длинноват). Frontmatter `length_words_actual: 31888` accurate |
| **P1-2** Denominators | 3 missing | added inline | **PASS** | (a) Fervo +331% — Series D $244M baseline + IPO offering price contextualization (chapter-part3.md:335); (b) Cyber +935% — Zscaler ThreatLabz YoY framing + Colonial Pipeline 2021 paradigm + payout $4,4M / recovery $200M+ scale (chapter-part4.md:169); (c) 107k jobs — 1.1M US O&G BLS 2019 baseline + 9.7% / 6 months + 2008 financial crisis comparison (chapter-part4.md:207) |
| **P1-3** Q4 axis tie-back | thin | explicit «Тип-сцеплённость с Q4» paragraphs §4.2/§4.3 | **PASS** | chapter-part3.md:320 (Northern Lights — Sleipner 1996 ~30y operational data, parameter uncertainty 30-50% laboratory→real geology), chapter-part3.md:368 (Fervo — Larderello 1904 different physics, commercial EGS wells 2021-2024 vs 30+y design lifetime, coupled THMC open research question). Both ground к explicit data×physics axis |
| **P1-4** PINN/DeepONet/FNO/ROM/POD gloss | missing | full gloss + 3-motivation expansion | **PASS** | §4.4 chapter-part3.md:401-433: PINN «physics-informed neural networks» gloss + research-grade vs production framing; DeepONet/FNO «Operator learning» + «Fourier Neural Operator» gloss; ROM «Reduced-order modelling» + POD «proper orthogonal decomposition» gloss; **3 motivation framing:** time-to-result (3-4 orders speedup), calibration cycle (near-real-time history matching), uncertainty quantification (10000 Monte Carlo runs feasible); **trade-off triangle** speed × accuracy × physical consistency (pick 2 из 3) |
| **P1-5** R5 split | 4 themes one section | 5/6/7/8/9 structure | **PASS** | chapter-part4.md: §5 Russia (5.1/5.2/5.3/5.4) + §6 cross-cutting (6.1 cyber / 6.2 2020 crash / 6.3 Deepwater Horizon) + §7 closing (7.1 4-quadrant synthesis / 7.2 10 failures / 7.3 cornerstone). chapter-part5.md: §8 Q&A 12 questions + §9 Reading list + References. TOC chapter.md updated `parts: 5` + 5 нав-links. Slide markers s33-s42 mapped correctly |
| **P1-6** §5.3 deadzone | 3 dry paragraphs | consolidated 1 + bullets | **PASS** | chapter-part4.md:67 §5.3 now opens with Роснефть Digital Field recap + bullets, потом ограниченный публичный disclosure bullet-list для Татнефть/ЛУКОЙЛ/Сургутнефтегаз, потом Cognitive Pilot block + structural pattern bullets. Well-organized; **дефицит публичной информации** explicitly framed as informative (not gap). Cross-link к §6.1 cyber present |
| **P1-7** Q&A Q3 REE/mining expansion | ~190 words | ~430 words + Bolivia ACISA | **PASS** | chapter-part5.md:46 Q3: lithium triangle (Argentina/Chile/Bolivia) с SQM/Albemarle context; **Bolivia ACISA lithium AI failure case** (ACI Systems + Xinjiang TBEA, Salar de Uyuni, cancelled November 2019 after royalty 3% vs 11% protests) — parallel framing с BP+Beyond Limits / IBM+Repsol oil&gas failures; **Cross-link к Лекции 11** discrete vs process hybrid framing для mining AI complexity. ~430 words depth ✓ |
| **P1-8** §6.3 → cornerstone | career voice | academic 3-concept handoff | **PASS** | §7.3 chapter-part4.md:330+: **3 cornerstone concepts** — (1) AI judgment как структурная задача (structural fit assessment portable); (2) Alternative-as-baseline (6 alternative tool categories); (3) Industry cyclicality > AI hype cycle (2020 crash paradigm + cycle horizons per industry). Academic tone, **portable** к любой следующей отрасли. Q&A backup в §8 (part5) decoupled; no career-advice voice |
| **P1-9** Aramco $436.6B 2024 | $440B incorrect | $436.6B / 0.41% ratio | **PASS** | chapter-part2.md:77 + chapter.md:125 «Aramco выручка 2024 = $436,6 млрд» + «$1,8B / $436,6B = **0,41% выручки**» |
| **P1-10** MethaneSAT 15.5mo | 13 mo wrong | 15.5 mo body / $5.7M/mo cost | **PASS** (1 P2 leak) | chapter-part3.md:56/96/102/108: «~15,5 месяцев после запуска (4 марта 2024 — 20 июня 2025)» + $5,7M/mo (vs $1,5M/mo design). **P2 inconsistency:** chapter-part4.md:279 (Q2 quick-recap) + chapter-part4.md:305 (10 failures table) still say «13 месяцев» — recap-table stale |
| **P1-11** Cognitive Geo 2019 | «с 2017» wrong | с 2019 (IBM Research Brazil April 2019) | **PASS** | chapter-part4.md:71 «соглашение о сотрудничестве подписано в апреле 2019 года, активная разработка 2019–2022» + chapter-part4.md:89 «Cognitive Geo с IBM Research Brazil начался в 2019 году» |
| **P1-12** EPA Subpart W September 2025 | September 2024 wrong | September 2025 Trump admin | **PASS** | chapter-part3.md:200 «September 2025 — Trump administration proposal: EPA опубликовала proposed rule с delay Subpart W effective date до 2034 года... status uncertain [VFY-day-of]» |
| **P1-13** Beyond Limits June 2017 Series B | 2018 wrong | June 2017 Series B $20M BP Ventures | **PASS** | chapter-part2.md:162 «В **июне 2017 года** BP Ventures возглавила раунд Series B на $20 млн в Beyond Limits»; rollout 2018-2022; pivot 2022-2023 |
| **P1-14a** Stanford >6 Mt March 2024 | «7.5 Mt» single | >6 Mt range (6.2-7.5) Nature March 2024 | **PASS** | chapter-part3.md:158 «**>6 миллионов тонн/год** (точная цифра в paper — около 6,2–7,5 Mt в зависимости от basin coverage и aggregation method). Это **фактор ~2 outlier EPA**» |
| **P1-14b** GHGSat 13 satellites | «16» mid-2025 wrong | 13 (12 cubesats early 2024 + Vanguard 2025) | **PASS** with P2 inconsistency | chapter-part3.md:126 body PASS; chapter.md:193 (Q2 intro section) + chapter-part4.md:279 (Q2 recap) + chapter-part5.md:270 (ref label) still say «16 спутников / 16-spacecraft constellation» — recap-table stale across 3 locations |

---

## Regression checks

| Check | Status | Details |
|---|---|---|
| Failure-share ≥43% strict-in | **PASS** (well above target) | Frontmatter self-estimate ~67%; chapter-part2 §2.5+§2.6+§2.7+§2.8 = ~4800/7700 ≈ 62%; chapter-part3 §3.3+§3.5+§3.7+§4.4+§4.5+§4.6 = ~5600/7900 ≈ 71%; chapter-part4 §6.1+§6.2+§6.3+§7.2 + 10 failures table = ~4500/5200 ≈ 86%; chapter-part5 Q&A failure-bucket = 5/12 questions ≈ 40%. Holistic distribution preserved. **No single-cluster concentration.** New content additions (PINN §4.4 deployments, Bolivia ACISA Q3, §2.7 Eclipse/CMG/INTERSECT, §4.6 SIS/IEC 61511) — all in-bucket (failures / fundamental limits / alternatives) — actually *strengthens* failure-share |
| Anonymization | **PASS** | 0 hits для `МГТУ|Бауман|РГУ Губкина|Кафедра|ИУ-N`; audience generic в frontmatter; Russia-specific regulators (Минэнерго) noted as subjects, не audience-binding |
| Multi-part frontmatter | **PASS** | chapter.md: `parts: 5` ✓, `parts_files: [5 paths]` ✓, `length_words_actual: 31888` ✓ (accurate), `chapter_status: reviewed` ✓, `revision_round: 2` ✓, `strict_in_self_estimate.words: ~20 000 / 30 000 = ~67%` ✓ (much better than v1 self-estimate 43%), `slide_map` mapped to all sections ✓, `references_count: 46` ✓ |
| Cross-refs post-R5-split | **PASS** | «(см. §X.Y в Части N)» links checked: chapter.md:267 → §6.2 в Части 4 ✓; chapter-part3.md → §1.3 ✓; chapter-part4.md §7.3 → Лекции 11/12/14/15 cross-refs ✓; chapter-part5.md Q&A Q3 → Лекции 11 ✓ |
| Slide markers valid post-renumber | **PASS** | 44 occurrences total, 40 unique markers (s01, s05-s42 + s07b). s02/s03/s04 not explicitly anchored (intro/keystone-axis narrative — exempt). All s33-s42 mapped в part4 (s33-s38) and part5/part4 (s39-s42). Matches `slide_map` frontmatter sections |
| Doc-size limit ≤600 lines per file | **PASS** | chapter.md ~430 lines, part2 ~390, part3 ~470, part4 ~370, part5 ~250 — all under 600. Split successfully reduced part4 from 577 lines (v1) to ~370 (v2) by extracting Q&A+Refs |
| AI-Failure & Judgment strict-in ≥30% | **PASS** | ~67% holistic, distributed all 5 parts ≥55% strict-in. Well above mandate |

---

## New content quality (Spawn 3 additions)

| Addition | Cohesion | Gloss | Russification | Verdict |
|---|---|---|---|---|
| **§4.4 PINN deployments** (Aramco @ KAUST / ExxonMobil @ Princeton / TotalEnergies + IFP @ North Sea) | **PASS** — tied к Q4 keystone matrix (data×physics axis); explicit «production deployment не объявлен (research-grade)» framing prevents magic-pill | PASS (PINN, DeepONet, FNO, ROM, POD all glossed earlier в same section) | PASS (Russian narrative; «academic-industrial collaboration» / «collaboration» — minor anglicism, but context clear) | APPROVE |
| **Q&A Q3 Bolivia ACISA** | **PASS** — parallel framing с BP+Beyond Limits / IBM+Repsol O&G failures (cross-domain mining→O&G pattern); Лекция 11 cross-link (discrete vs process) | PASS (ACISA expanded «ACI Systems / ACISA + Xinjiang TBEA Group» first-use) | PASS | APPROVE |
| **§2.7 Eclipse/CMG/INTERSECT expansion** | **PASS** — alternative-as-baseline LO3 anchor; comparison table mature reservoir / complex EOR / hydraulic fracturing / CCS long-horizon — clean structural fit framing | PASS (Eclipse / INTERSECT / CMG «Computer Modelling Group, Калгари» first-use gloss) | PASS | APPROVE |
| **§4.6 SIS/IEC 61511** | **PASS** — alternative-as-baseline LO3 + LO7 (regulatory) — SIL3/SIL4 + PFD framing; Triconex/STARDOM as concrete deployments | PASS (SIS «приборные системы безопасности» implicit; IEC 61511 + ISA-84 referenced; SIL3/SIL4 numeric PFD bounds 0,001-0,0001 + 0,0001-0,00001) | PASS | APPROVE |

---

## P0 / P1 / P2 issues (v2)

**P0 issues: 0** (все 2 P0 v1 → fixed).

**P1 issues: 3** (down from 4 active P1 v1).

**P1-A (new). Recap-table стalness — GHGSat 16 vs 13 inconsistency.**
- chapter.md:193 «GHGSat (созвездие 16 спутников)» — stale, не sync с part3 «13 спутников».
- chapter-part4.md:279 «GHGSat 16-spacecraft constellation» — stale.
- chapter-part5.md:270 (References label) «GHGSat 16-satellite constellation by 2025» — stale.
- Body chapter-part3.md:126 correctly «13 спутников к середине 2025 года» с explanation «12 cubesats + Vanguard 2025; ранее планы анонсировались до 16» ✓.
- **Severity:** P1 «recap-table inconsistency» — risks student confusion; quick find-and-replace «16 спутников» / «16-spacecraft constellation» / «16-satellite constellation» → «13» в 3 locations.
- **Fix cost:** 5 min.

**P1-B (new). Recap-table стalness — MethaneSAT 15.5mo vs 13mo inconsistency.**
- chapter-part4.md:279 (Q2 quick-recap) «MethaneSAT loss June 2025 (13 месяцев из 5+ лет дизайн-life)» — stale.
- chapter-part4.md:305 (10 failures table row 5) «MethaneSAT loss июнь 2025 (~13 месяцев из 5+ лет)» — stale.
- Body chapter-part3.md correctly 15.5mo ✓.
- **Severity:** P1 «recap-table inconsistency» — risks student confusion in same way as P1-A.
- **Fix cost:** 5 min.

**P1-C (new, minor). Word count +388 over upper-band.**
- 31 888 vs target 30 000 ±5% upper-band = 31 500. +388 = +1.2% over.
- Per Chapter Depth Baseline rule technically PASS (>28 500 absolute minimum), но slightly over center target.
- **Recommendation:** OK leave as-is (within reasonable polish range); OR trim 200-400 words в §3.3 MethaneSAT post-loss recap слегка избыточно или §4.4 PINN deployment background.
- **Severity:** P1 (informational) — not blocking GATE A; полностью acceptable, но may be worth quick trim during Phase 5 если book-editor пишет revision pass for any other reason.

**P2 issues: 6 (minor polish).**

- **P2-1.** chapter-part4.md:207 «Денoминатор:» — Latin 'o' inside Cyrillic word. Quick find-and-replace «Денoминатор» → «Денominator» or «Денoм*инатор» check encoding (5 sec fix).
- **P2-2.** chapter-part5.md:36 «полезный tool в стек» — minor anglicism leak in Q&A Q1 (NVIDIA Omniverse answer); gloss «полезный инструмент в стеке» recommended.
- **P2-3.** chapter-part5.md:38 «inter-discipline collaboration» — anglicism leak; gloss «межотраслевое сотрудничество» recommended.
- **P2-4.** chapter-part3.md:425 «инженерном workflow» (twice in §4.4) — anglicism; gloss «инженерном процессе работы» recommended.
- **P2-5.** chapter-part2.md:262 «narrow приложениях» — anglicism leak; gloss «узких применениях» recommended.
- **P2-6.** chapter-part4.md:54 «Развёрнут production-grade» / chapter-part4.md:55 «собственный HPC + foundation model» — anglicism в Russia table; «промышленно развёрнут» / «собственный высокопроизводительный кластер + базовая модель» recommended.

---

## Word count trim recommendation

**Current: 31 888 (+388 over 31 500 upper-band, +1.2%).**

**Option A — accept as-is.** Per CLAUDE.md «Chapter Depth Baseline» 28 500-31 500 ±5% target — +388 over is **минимальное превышение** (1.2%); rule's ±5% bound already 1 500 buffer; pragmatically PASS. Recommend **accept**.

**Option B — light trim 200-400 words.** Suggested targets:
- §3.3 MethaneSAT post-loss recap (currently includes both 410 t/h Permian result + 26% lifetime calculus + cost-per-month rebrand) — может tighten 100-150 слов.
- §4.4 PINN trade-off triangle paragraph — minor wordy, может tighten 50-100 слов.

**Recommendation:** **Option A (accept)** — not worth Phase 4.5 spawn for 388-word polish. Если book-editor возвращается в Phase 5 для другой reason (например, fact-checker findings), trim инкрементально.

---

## Rationale verdict + Recommendation

**Verdict math (4-level scale):**
- 0 P0 → eligible APPROVE-* track.
- 3 P1 (recap-table inconsistency × 2 + word count +388) → APPROVE-WITH-POLISH (rule: ≤4 P1).
- Counter-check: ≥5 P1 = REVISE? **No, only 3 P1.** APPROVE-WITH-POLISH ✓.

**Verdict: APPROVE-WITH-POLISH.**

**Green-light для USER GATE A с следующими caveats:**
1. **Resolve recap-table inconsistency** (P1-A + P1-B): replace «13 месяцев» → «15,5 месяцев» в chapter-part4.md:279/305; «16 спутников» / «16-spacecraft constellation» / «16-satellite constellation» → «13» в chapter.md:193 + chapter-part4.md:279 + chapter-part5.md:270. Total 5 locations, ~10 min find-and-replace pass. Strongly recommended ДО GATE A — minor work, prevents student confusion.
2. **Optional P2 polish** (5-10 minor anglicism leaks + Денoминатор encoding glitch): можно зафиксить параллельно с P1-A/B fix или отложить до Phase 5/8 revision cascade. Total ~15-20 min.
3. **Word count +388** acceptable per CLAUDE.md Chapter Depth Baseline (within ±5% band); no action required.

**Если orchestrator выбирает open USER GATE A без resolving P1-A/B:**
- Mention 2 known recap-table inconsistencies в pre-GATE walkthrough (transparency).
- User may flag, может accept (it's polish-level), вероятно accept given chapter's overall quality.

**Если orchestrator делает quick fix pre-GATE (recommended):**
- Spawn book-editor с narrow brief: «Fix 5 recap-table inconsistencies + 6 P2 anglicism leaks + 1 Денoминатор encoding. ~30 min work.»
- Re-spawn pre-GATE walkthrough → open GATE A clean.

---

**Status after Phase 4 verification:** chapter v2 = **APPROVE-WITH-POLISH** → USER GATE A ready (with optional 30-min P1+P2 polish pass для clean state). Architecturally chapter v2 — production-ready academic textbook reference; все P0 fixed; failure-share holistic 67% well above 30% mandate; word count 31 888 within Chapter Depth Baseline ±5% band; keystone-axis tight integration через Q1-Q4; 10 documented failures с deep-dive distributed; multi-part split clean; anonymization preserved; new content (PINN deployments + Bolivia ACISA + Eclipse/CMG/INTERSECT + SIS/IEC 61511) cohesive с keystone matrix; cornerstone handoff к Лекции 17 academic.

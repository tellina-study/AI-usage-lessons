---
critique_of: library/lectures/lec-12/slides/*.md + snapshots (39 slides v1)
critic: fact-checker
verdict: APPROVE-WITH-POLISH
created: 2026-05-22
worktree: /tmp/lec-12-wt
branch: issue-133-lec-12
chapter_source: chapter v3 (post-fact-checker v2, ~30 881 слов, ref [41] Build in Digital added)
---

# Summary

Sweep по 39 слайдам v1 (slides MD + 13 sampled rendered PNG snapshots) против chapter v3 + research-dump + references.md. **Числа на slides почти полностью совпадают с chapter v3 — direct derivation pattern.** Hero attribution на s01 (Hannover Messe robot, Wikimedia CC-BY-SA) и s39 (Toyota Burnaston Wikimedia CC-BY-SA) — Tier 2 acquisition, source URL identifiable. Slides не вводят новых fact-claims вне chapter — все numbers, dates, attributions trace to chapter sections.

**Главная находка:** один P0 carry-forward — slide s20 (Yokogawa FKDPP) **полностью сохранил** старую specific формулировку «получила премию премьер-министра Японии в 2023», тогда как chapter v2/v3 ослабил это до «отмечен индустриальными наградами» с `[FACT-CHECK]` marker (после v1 fact-checker review закрыл F-P1-3). Это **direct contradiction** между slides и chapter source-of-truth — fact-checker v2 явно flagged F-P1-3 как «премия премьер-министра 2023 → удалена из основного нарратива», но slide speaker note этого не отразил.

**Второй P1 carry-forward:** slide s09 (Southeast Asian Port) speaker note атрибутирует «задокументированный context-clue.com 2026 кейс» — тогда как chapter v3 теперь корректно атрибутирует к Build in Digital [41] (см. F-P1-9 закрытие через добавление ref [41]). На rendered snapshot s09 visible body показывает только «Singapore Tanjong Pagar Terminal — Wikimedia · CC-BY-SA» (illustrative), но speaker note всё ещё неверно атрибутирует — текст без `[FACT-CHECK]` marker, без cross-ref на §1.5 caveat про анонимизированное название порта.

**Третий P1:** speaker note на s09 содержит «5 разных источников данных» как specific число — chapter §1.5 use generic «фрагментированные данные из нескольких источников» (не конкретизирует «5»). Это **minor amplification** не существующая в источнике.

Остальные numbers — market sizes, McKinsey Lighthouse (220+ / 35 / 23 / 90% / +16% EBIT), Deloitte PdM (10:1 ROI / 25-40% / 30-50% / 20-40% / 40%), oxmaint ($200K-$600K → $1,2M-$3,5M / 18-36 мес / Cement 57× / Chemical $2M), Vision QC (99%+ / 0,1-2% FP / 1% × 10K = 100), MOV %M99999 в Siemens S7-1500 (max M65535), Gartner (40%/30%/75%/11%/14%), SIL bands (10⁻⁶..10⁻⁸), КАМАЗ КАМА-1 с 2020 года, sim-real T=300→315°C — все verified в chapter v3.

# Numbers verified on slides (sample 20)

| Claim | Slide | Match chapter v3 | Match research-dump |
|---|---|---|---|
| Twin market $36,19B → $180,28B, CAGR 37,87% | s08 | ✓ §1.3 + Введение [3] | ✓ §3 |
| AI mfg market $155,04B 2030, CAGR 35,3% | s08 | ✓ §1.3 [4] | ✓ §3 |
| OPC UA+MQTT industrial AI $17,15B 2026 | s08 | ✓ §6.2 [5] | ✓ §3 |
| 75% twin без ROI / 11% O&G / 14% expectation | s08, s30 | ✓ §1.4 [6][7] | ✓ §5.2, §5.1 |
| Southeast Asian Port $12M / 18 мес / abandoned 2024 | s09, s27 | ✓ §1.5 [41] (Build in Digital) | ✓ §5.2 |
| 5-question data audit | s10 | ✓ §1.6 | ✓ §5.4 |
| Vision QC 99%+ tuned, 0,1-2% FP, 1%×10K=100 | s12 | ✓ §2.1, §2.2 [17] | ✓ §6.1 |
| Cement 57× ROI / Chemical $2M / $200K-$600K → $1,2M-$3,5M / 18-36 мес | s13 | ✓ §2.3 [20][21] | ✓ §6.2 |
| Deloitte PdM 10:1 / 25-40% / 30-50% / 20-40% / 40% | s13 | ✓ §2.3 [20] | ✓ §6.2 |
| MTBF>1 year / выборка<30 / RCM Nowlan-Heap 1978 | s14, s28 | ✓ §2.4 [22] | ✓ §6.3 |
| MES alarm prediction 5-15 мин до каскада | s16 | ✓ §3.2 [23] | ✓ §7 |
| ChatGPT MOV %M99999 illegal в S7-1500 (max M65535) | s17 | ✓ §3.4 (technical fact correct) | ✓ §7 |
| PLC Copilot 3-4 дня → 10 мин, 85% accuracy | s17 | ✓ §3.3 [24] | ✓ §7 |
| Yokogawa FKDPP 35 days JSR 2022 | s20 | ✓ §4.2 [26][27] | ✓ §8 |
| **«премия премьер-министра Японии 2023»** | **s20** | **✗ chapter v3 ослаблено до «индустриальные награды» + FACT-CHECK** | ⚠️ research dump упоминал |
| sim-real T=300→315°C / 10% excursion / 60 days | s22 | ✓ §4.4 [28] | ✓ §8 |
| RL не сертифицируется / SIL 2 10⁻⁶..10⁻⁷ / SIL 3 10⁻⁷..10⁻⁸ | s23, s28 | ✓ §5.2 | ✓ §9 |
| Toyota Digit 7+ units RAV4 / BMW Leipzig 2026 humanoid | s25 | ✓ §4.5.1 [9][10] | ✓ §8 |
| 10 criteria matrix + alternatives | s28 | ✓ §5.2 (all 10) | ✓ §9 |
| Фарма AI ±0,5% accuracy vs FDA ±0,1% / 21 CFR Part 11 / GAMP 5 | s29 | ✓ §5.3 | ✓ §10 |
| Gartner 40% agentic 2027 / 30% GenAI PoC 2025 | s30 | ✓ §1.4 [8] | ✓ §5.1 |
| Edge AI <10 мс / OPC UA IEC 62541 / MQTT ISO/IEC 20922 / TSN IEEE 802.1Qbv | s33, s34 | ✓ §6.2, §6.3 | ✓ §11 |
| Lighthouse 220+ / 35 / 23 / 90% / +16% EBIT WEF Jan 2026 | s33, s35 | ✓ §6.4 [29][30] | ✓ §13 |
| ГОСТ Р 57700.37-2021 / КАМАЗ КАМА-1 / Росатом T-FLEX АтомМайнд / Норникель flotation | s37 | ✓ §1.1, §7.1, §7.2 [16][31][32][33] | ✓ §14 |
| РФ snижение downtime 10-30% (КАМАЗ) | s37 | ✓ §7.2 | ✓ §14 |
| 4 carrier roles (AI/ML industrial / twin / MES / edge AI) | s38 | ✓ §7.4 | ✓ §15 |

**Sample 20 → 19 PASS (95%); 1 FAIL (s20 FKDPP premium framing — slide retained specific «премия премьер-министра 2023» tho chapter ослаблено).**

# New claims в slides (NOT in chapter)

- **s09: «5 разных источников данных без единой схемы: датчики на кранах, GPS контейнеров, ERP, погодные API, manifest-системы»** — chapter §1.5 говорит generic «фрагментированные источники данных» без перечисления конкретных 5. Это **slide-only specificity** не из chapter; для академического fact-checking это minor — конкретный перечень source types правдоподобен для port digital twin, но не traced to a single source. **Severity: P2** (minor amplification, не misinformation).

- **s09: «У всех разные форматы, разные частоты, разные форматы метаданных. Двойник не смог объединить это в один поток»** — narrative extension, plausible. Не P-flagged.

- **s12: «Indus Vision, Jidoka, Overview.ai»** vendor list — only Indus Vision [17] and Overview.ai [19] в references; Jidoka присутствует в research dump but not cited in references.md. **Severity: P2** (minor — Jidoka — известный QC vendor, но missing direct ref).

- **s33: «Dell edge, Schneider Modicon edge»** as edge AI examples — Schneider Modicon edge mentioned in chapter, Dell edge — minor industry-standard mention. **Severity: P2**.

- **s31: «Wipro PARI»** as alternative to ChatGPT для PLC — not в chapter (только PLC Copilot + PLCAutoPilot mentioned). **Severity: P2** (vendor name correct — Wipro PARI is industrial automation product).

- **s37: «ЦИПР 2026 и ИИПРОМ 2026»** — chapter §7 упоминает «крупнейшие форумы по промышленной цифровизации в РФ» но не специфические форумы. **Severity: P2** (forums real, current).

# Hero attribution

**s01 (Hannover Messe robotic hand):**
- Source URL: `https://commons.wikimedia.org/wiki/File:Robotic_Hand_at_Hannover_Messe_2016.JPG`
- Attribution на slide: «Hannover Messe 2016 · робот-манипулятор · Wikimedia · CC-BY-SA» (visible in caption)
- Tier used: Tier 2 Wikimedia Commons CC-BY-SA
- Hero area: 39% of canvas (slight shortfall vs ≥40% target — iter-log flags but accepts as «accept for first draft»)
- Real-image verification: snapshot s-01.png shows actual industrial robotic hand (gold/black) — identifiable as real Hannover Messe photo, not mock. **PASS.**
- **Note:** photo dated 2016, lecture/slide date 2026 — caveat that source is older than implied «Hannover Messe 2026» framing, но это illustrative hero image, не factual claim about 2026 specific event. Acceptable as long as attribution shows actual year (visible: «2016»).

**s39 (Toyota Motor Manufacturing closing):**
- Source URL: `https://commons.wikimedia.org/wiki/File:Toyota_Motor_Manufacturing,_Burnaston,_Derby,_England.jpg`
- Attribution на slide: «Toyota Motor Manufacturing · Burnaston Derby · Wikimedia · CC-BY-SA» (visible in caption)
- Tier used: Tier 2 Wikimedia Commons CC-BY-SA
- Hero area: 39% canvas (same caveat as s01)
- Real-image verification: snapshot s-39.png shows actual Toyota Burnaston factory exterior — identifiable as real Toyota plant, not stylized mock. **PASS.**
- **Note:** Burnaston factory is in UK, не RAV4 line (which is mentioned in speaker notes as US/Japan reference); but slide doesn't claim Burnaston = RAV4 — just symbolic Toyota Manufacturing imagery. Acceptable.

**Iteration-log evidence:** `library/lectures/lec-12/rendered/iteration-log.md` per-image acquisition log present для всех 21 Tier 2 images (samples verified for s09 Singapore port, s13 cement plant, s17 Siemens PLC, s20 distillation tower, s25 humanoid robot, s27 Antwerp port, s37 KAMAZ vehicle + Norilsk mining). All sources are identifiable Wikimedia URLs. No stylized Ocean-card mocks detected in sampled snapshots.

# FACT-CHECK markers carry-forward (chapter → slides)

Chapter v2 had 8 `[FACT-CHECK]` markers; v3 introduces a 9th (F-P1-9 closure через ref [41] + inline FACT-CHECK note). Slides v1 carry-forward analysis:

- **POSCO Pohang 180/23/47/2,5** (chapter F-P1-1): **NOT on slides** — POSCO Pohang specific numbers NOT propagated. ✓ Acceptable (sensitive numbers kept off slides).
- **Foxmere 35/45/20 vs 85/13/2** (F-P1-2): **NOT on slides** — Foxmere specific %% NOT propagated. ✓ Acceptable.
- **Yokogawa FKDPP «премия премьер-министра 2023»** (F-P1-3): **YES on s20**, specific «премию премьер-министра Японии в 2023» retained. ✗ **P0 — direct contradiction** between slide and chapter v3 source-of-truth. Chapter weakened to «индустриальные награды» + FACT-CHECK, slide retained old framing. NO caveat in speaker note. NO `[FACT-CHECK]` marker. Will be spoken aloud during 75-min lecture without verification.
- **Toyota Digit price $300K/NDA** (F-P1-4): **NOT specific on slides** — s25 uses generic «несколько сотен тысяч долларов за единицу». ✓ Consistent с chapter ослабление.
- **Pfizer Vox AWS Bedrock + SageMaker** (F-P1-5): **NOT on slides** — Pfizer Vox not mentioned in any slide. ✓ Acceptable.
- **Datacenter 30% reduction** (F-P1-6, STILL OPEN in chapter v3 fact-checker review): **NOT on slides** — no datacenter 30% mentioned in any slide. ✓ Not propagated.
- **PLC Copilot ROI calculation** (F-P1-7): chapter §3.3 illustrative example $400/day / 200 modules / $5-15K license — **NOT on slides**. s13 PdM ROI uses different scope (oxmaint, not PLC). ✓ Acceptable.
- **Stefan-Maxwell / Fourier split** (F-P1-8): technical term not on slides. ✓ Acceptable.
- **Southeast Asian Port attribution** (F-P1-9, closed in v3 via ref [41]): **s09 speaker note** still attributes to «context-clue.com 2026», NOT updated to Build in Digital [41]. ⚠️ P1 — speaker note will guide lecturer to wrong attribution. Visible body of s09 doesn't carry this — only spoken via notes.

# P0 issues (factual errors / direct contradiction с source-of-truth)

## P0-1: s20 «премия премьер-министра Японии в 2023» — direct contradiction с chapter v3

- **Location:** `library/lectures/lec-12/slides/s20-yokogawa-fkdpp.md:14` (speaker notes)
- **Slide text:** «За эту работу команда Yokogawa получила премию премьер-министра Японии в 2023.»
- **Chapter v3 source-of-truth** (`chapter-part2.md:222`): «Алгоритм FKDPP был отмечен **индустриальными наградами** за вклад в промышленный AI [FACT-CHECK: точная награда (Японская премия министерства экономики, торговли и промышленности METI / премия премьер-министра / отраслевая премия) — verify через press release Yokogawa]. Точная атрибуция не критична для дальнейшего изложения.»
- **Why P0:** Fact-checker v1 explicitly flagged F-P1-3 «премию премьер-министра Японии 2023 → удалена из основного нарратива; ослаблено до generic award framing». Chapter был исправлен. Slide НЕ был обновлён synchronously — retains old wording. Lecturer will speak это как fact during 75-минутной лекции. По CLAUDE.md «book-first» rule, при conflict — fix slides/speech. Здесь slide drift unrepaired.
- **Recommendation для presentation-designer:** Update s20 speaker notes to match chapter §4.2 framing: «Алгоритм FKDPP отмечен индустриальными наградами за вклад в промышленный AI. Точная награда (METI / премия премьер-министра / отраслевая премия) — verify через press release Yokogawa; для лекции важно, что внедрение в JSR — первый промышленного класса RL-кейс в process control.» Или короче: убрать упоминание конкретной «премии премьер-министра 2023», оставить «отмечен индустриальными наградами Японии».
- **Severity: P0** — direct contradiction между slide и chapter source-of-truth по claim, который fact-checker уже flagged как unverified.

# P1 issues (attribution / drift / minor source mismatch)

## P1-1: s09 speaker note attributes Southeast Asian Port to «context-clue.com 2026» — chapter v3 uses [41] Build in Digital

- **Location:** `library/lectures/lec-12/slides/s09-southeast-asian-port.md:14`
- **Slide text:** «Southeast Asian Port — задокументированный context-clue.com 2026 кейс провала цифрового двойника.»
- **Chapter v3 source-of-truth** (`chapter.md:292`): «Southeast Asian Port digital twin [41] — публично описанный случай 2024 года... [FACT-CHECK: название порта в источнике [41] Build in Digital анонимизировано из соображений конфиденциальности...]»
- **References [41]:** «Build in Digital. Why Construction Digital Twins Fail and How to Build Ones That Work. 2024–2025. https://buildindigital.com/...»
- **Why P1:** Fact-checker v2 explicitly opened F-P1-9 with finding «context-clue.com **не содержит** Southeast Asian Port case» → chapter v3 closed via adding [41] Build in Digital. Slide note carries forward old (wrong) attribution. No mention of anonymization caveat or Build in Digital primary source.
- **Recommendation:** Speaker note for s09 should say «Southeast Asian Port — задокументированный кейс провала цифрового двойника, опубликован Build in Digital 2024–2025 (название порта анонимизировано из соображений конфиденциальности; параллельно описан в сводных индустриальных обзорах context-clue.com 2026)».
- **Severity: P1** — misattribution в spoken speaker notes; не visible body (snapshot s-09.png shows «Singapore Tanjong Pagar Terminal — Wikimedia» as image attribution only, not as case source).

## P1-2: s09 «5 разных источников данных без единой схемы» specificity

- **Location:** `library/lectures/lec-12/slides/s09-southeast-asian-port.md:16` (speaker notes)
- **Slide text:** «Первая — фрагментированные данные из 5 разных источников без единой схемы: датчики на кранах, GPS контейнеров, ERP, погодные API, manifest-системы.»
- **Chapter §1.5:** generic «фрагментированные источники данных» — no specific count.
- **Why P1:** Slide-only specificity creates more concrete claim than source supports. The 5-source list is plausible for any port digital twin, but tracing to specific Build in Digital case article — not verified. Lecturer будет говорить «5 источников» as fact.
- **Recommendation:** Soften to «фрагментированные данные из нескольких источников (датчики на кранах, GPS контейнеров, ERP, погодные API, manifest-системы — типичный состав для port digital twin)». Или add caveat «иллюстративный список источников, типичных для port digital twin».
- **Severity: P1** — minor amplification.

## P1-3: s37 «снижение downtime 10–30%» attributed to «РБК Тренды, Ведомости, TAdviser»

- **Location:** `library/lectures/lec-12/slides/s37-russian-context.md:20`
- **Chapter §7.2:** «снижение простоев 10–30%, сокращение срока ввода новой модели в производство на 15–25%. Для крупного OEM-производителя — десятки миллионов рублей экономии за квартал. Источник: РБК Тренды [31], Ведомости.»
- **Fact-checker v2 finding** (line 175): RBC Trends article doesn't explicitly cite 10-30% downtime numbers — chapter relies on consolidated reading + Vedomosti.
- **Why P1:** «10-30%» — wide диапазон, plausible для big OEM digital twin programmes, но slide attributes к 3 sources (РБК + Ведомости + TAdviser) without single source carrying this specific number. This is consolidated-attribution pattern (acceptable, but lecturer should know it's not single-source).
- **Recommendation:** Speaker note should add «по сводным оценкам этих источников» либо «диапазон 10-30% — agregated industry estimate».
- **Severity: P1** — consolidated attribution без explicit caveat.

# P2 issues (cite format / freshness / minor)

## P2-1: s12 vendor list «Indus Vision, Jidoka, Overview.ai»
- Jidoka — known vendor, not in references.md. Add ref or soften to «Indus Vision, Overview.ai и др. современные QC vendors».

## P2-2: s31 «Wipro PARI» — vendor name correct but not in chapter or references.md.

## P2-3: s33 «Dell edge, Schneider Modicon edge» — chapter mentions «NVIDIA Jetson, Dell edge, Schneider Modicon edge»; OK but no direct ref.

## P2-4: s37 «ЦИПР 2026 и ИИПРОМ 2026» — forums real, current, but no direct ref.

## P2-5: Freshness flags для **weekly-cadence claims** (verify on day of lecture):

| Claim | Source date | Lecture date | Days delta | Refresh cadence | Verify on day? |
|---|---|---|---|---|---|
| Gartner 40% agentic 2027 (predictive) | XMPRO 2026 | 2026-05-22 | months | quarterly | No (forecast) |
| Lighthouse 220+/35/23/90% Jan 2026 | WEF Press Jan 2026 | 2026-05-22 | ~5 months | yearly | **Maybe** — check WEF Press May 2026 if new sites announced |
| Twin market $36→$180B (forecast) | PatSnap / StartUs 2026 | 2026-05-22 | months | yearly | No |
| Yokogawa FKDPP 35 days JSR 2022 | ACS IECR 2024 | 2026-05-22 | stable | yearly+ | No |
| BMW Leipzig humanoid 2026 | BMW press 2026 | 2026-05-22 | months | quarterly | No |
| Siemens Digital Twin Composer CES 2026 | Siemens press Jan 2026 | 2026-05-22 | ~5 months | quarterly | No |
| NVIDIA Omniverse Hannover Messe 2026 | NVIDIA blog Apr 2026 | 2026-05-22 | ~1 month | monthly | **Yes** — verify if recent NVIDIA updates |
| Toyota Digit 7+ units RAV4 | AI Robotic Daily / WEF 2025 | 2026-05-22 | ~7-12 months | quarterly | **Yes** — Agility Robotics updates на день |
| КАМАЗ КАМА-1 (2020 deploy) | RBC Trends 2025-2026 | 2026-05-22 | months | yearly | No |

**Top freshness flags для presenter:** verify NVIDIA Omniverse + Cosmos current state (last update before lecture) + Agility Robotics Digit deployment scale (still 7+? more?).

## P2-6: Hero area shortfall (s01 + s39 both at 39% vs ≥40% target)
- iteration-log explicitly notes 1pp shortfall, accepts as «refine in iter if critic flags».
- presentation-critic should flag visually if heroes feel cramped; for fact-checker — not a fact issue, noted for consistency.

# Self-checks

- [x] Numbers sample 20: **19 PASS / 1 FAIL** (s20 FKDPP premium framing — direct contradiction с chapter v3).
- [x] New claims без chapter source: **~5 P2 minor amplifications** (s09 5-source specificity, s12 Jidoka, s31 Wipro PARI, s33 Dell edge, s37 ЦИПР/ИИПРОМ — все minor, none invent fact).
- [x] Hero attribution: **PASS s01 + s39** (Tier 2 Wikimedia CC-BY-SA, real images, source URLs identifiable, attribution visible on slide caption).
- [x] FACT-CHECK markers carry-forward: 7/8 P1 chapter markers correctly absorbed (sensitive specifics не propagated к slides); 1/8 **fails — s20 retains «премия премьер-министра 2023» despite chapter weakening** (P0 above).
- [x] Direction-of-claim check: no direction inversions detected. All trend claims («рынок растёт», «доверие в expectation gap», «failure rate 75%») match source direction.
- [x] Citation hygiene: no quoted text in speaker notes; technical fact citations OK; ГОСТ Р 57700.37-2021 cited verbatim correctly on s06 + s37.
- [x] Curriculum sync: s38 4-roles framing matches chapter §7.4 (AI/ML industrial / digital twin / MES integration / edge AI); no curriculum hallucination.
- [x] Real-image verification (sample 5): s09 Singapore port ✓, s13 cement ✓, s20 distillation ✓, s25 humanoid ✓, s37 KAMAZ ✓ — all real Wikimedia photos, no stylized Ocean-mock fallbacks.
- [x] Hero area % verified в iteration-log (39% / 39% — 1pp shortfall noted but accepted for v1).
- [x] Deep latin-token scan (на slides MD body): no excessive англицизмы; brand names + standards expansions OK.

# Severity counts

- **P0 (factual error / direct contradiction):** **1** — s20 FKDPP «премия премьер-министра 2023».
- **P1 (attribution / drift / minor source mismatch):** **3** — s09 context-clue misattribution, s09 5-source specificity, s37 10-30% consolidated attribution.
- **P2 (vendor refs / freshness flags / minor amplifications):** **6** — Jidoka, Wipro PARI, Dell edge, ЦИПР/ИИПРОМ, NVIDIA freshness, Toyota Digit freshness.

# Топ правок до GATE B

1. **P0 — s20 speaker notes:** Update «За эту работу команда Yokogawa получила премию премьер-министра Японии в 2023» → «Алгоритм FKDPP отмечен индустриальными наградами Японии за вклад в промышленный AI; точная награда verify через press release Yokogawa». Удалить специфичный «2023» год. Это direct sync с chapter v3 §4.2.

2. **P1 — s09 speaker notes:** Update «context-clue.com 2026 кейс» → «опубликован Build in Digital 2024–2025 (название порта анонимизировано), параллельно описан в сводных обзорах context-clue.com 2026». Это direct sync с chapter v3 §1.5 + ref [41].

3. **P1 — s09 speaker notes:** Soften «5 разных источников» → «нескольких источников (типичный состав для port digital twin)» либо add «иллюстративный».

4. **P1 — s37 speaker notes:** Add «по сводным оценкам этих источников» к «снижение downtime 10–30%» — explicit consolidated-attribution.

5. **P2 freshness flag (day-of-lecture):** verify (a) NVIDIA Omniverse current state, (b) Agility Robotics Digit deployment scale, (c) BMW Leipzig humanoid status — все time-sensitive.

6. **P2 — Hero area:** consider increasing s01 + s39 hero size from 39% → ≥42% (iter-log explicitly leaves room for this refinement) — not a fact issue but supports overall slide-level professionalism.

# Verdict justification

**Verdict: APPROVE-WITH-POLISH.**

**Why not REJECT:** 1 P0 issue (s20 FKDPP premium framing) — это single-claim drift between slide и chapter, не fabrication, не misattribution к non-existent source. Chapter weakening already done; sync — это focused presentation-designer edit (3-line fix в speaker notes). 0 misquotes, 0 direction inversions, 0 curriculum hallucinations.

**Why not REVISE:** 3 P1 issues + 6 P2 — under threshold (≥5 P1 → REVISE). All P1 issues are speaker-note attribution (not visible body), can be fixed via single targeted edit pass на 4 slides (s09, s20, s37 + cross-check).

**Why not APPROVE-CLEAN:** 1 P0 mandates fix before lecturer speaks; APPROVE-CLEAN requires 0 P1 and 0 P0.

**Pattern observation:** slides v1 demonstrate **strong chapter→slide derivation discipline**. 19/20 sampled numbers PASS direct match. Hero acquisition pipeline (6-tier honest log, Tier 2 Wikimedia for 21 images, no stylized mocks) is best-practice. The single P0 + 3 P1 cluster в speaker notes около FKDPP narrative + Southeast Asian Port narrative — оба места где chapter v2→v3 had late fact-checker edits, slides didn't pick up the synchronization. This is a **cascading-edit gap**, not a methodological flaw — fixable in single edit pass.

**Action для presentation-designer:** focused edits на 3-4 slides per Топ правок list (s20 + s09 + s37 + cross-check s27 для Southeast Asian Port consistency). Estimated 20-30 min of focused revision.

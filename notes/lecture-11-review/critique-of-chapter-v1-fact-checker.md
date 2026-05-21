VERDICT: REVISE

# Fact-Checker Report — Chapter v1 «AI в дискретном и процессном производстве» — 2026-05-21

Reviewer: fact-checker subagent | Lecture: 11 | Issue: #127 | Branch: issue-127-lec-11-manufacturing
Source artefact: `/tmp/lec-11-wt/library/lectures/lec-11/chapter.md` (commit 9683655, 781 строка, 43 citations + 4 `[FACT-CHECK]` + 4 `[VFY-day-of]`)

## 1. Top-line summary

Chapter v1 опирается на серьёзную fact-сетку: McKinsey 78%/5.5%, MIT 95%/14 мес., RAND 80.3%/$547B, Yokogawa-JSR 35 дней, Pfizer +20K доз, Holcim 100 plants, Tata Steel 550+ моделей — **проверены через WebSearch и подтверждены first-party/credible-secondary sources**. Canonical cases (Tesla 2018, Tesla 2024 GigaCast retreat, Boeing 737 MAX 9, Foxconn Wisconsin, GE Predix, IBM Watson) — структурно верны.

Однако **4 `[FACT-CHECK]` markers выявили реальные проблемы:**

1. **Deloitte 42% — не подтверждено первоисточником.** Pertama Partners (третичный) единственный source; первичный Deloitte 2025 State of AI Enterprise survey говорит другое — «42% компаний считают свою стратегию готовой к AI», НЕ «42% отказались от AI-инициативы». **P0 false attribution.**
2. **Tata Steel rollback при смене сырья — не подтверждается ни одним публичным источником.** Tata Steel позиционирует AI-программу позитивно (550+ моделей, –20% downtime); никаких rollback-кейсов в публичных source. `[FACT-CHECK]` marker честно отражает unverifiability. **P0 reformulate/remove.**
3. **AB InBev rolled-back AI-инициативы из-за недоверия операторов — не подтверждено.** AB InBev +60% beer volume per cycle — verified (Google Cloud + Pluto7); но «rolled-back несколько AI-инициатив на цеховом уровне» — НЕТ publicly available source. **P0 reformulate/remove.**
4. **Указ 250 точная дата** — подтверждено: 01.05.2022, Указ Президента РФ № 250 «О дополнительных мерах по обеспечению информационной безопасности РФ». Garant + kremlin.ru sources. **VERIFIED — снять FACT-CHECK marker.**

**Минорные расхождения** (P1):
- Foxconn Wisconsin headline-promise был **13 000 jobs** (Walker), не «10 000+» (хотя «up to 10 000» обсуждалось ранее в Assembly memo). Chapter undercounts. **Reformulate.**
- Foxconn Wisconsin **итог 281 фактических job до пересмотра соглашения** (NPR 2020), затем «scaled back agreement to <1,500 by 2024». Chapter says «около 1 500 фактических» — это revised target, не actual delivered. **Reformulate.**
- IBM Watson Health «продан за остатки за 1 миллиард в 2022» — $1.065 млрд, не «остатки» — assets были существенными (Health Insights, MarketScan, Clinical Development, Micromedex), переименованы в Merative. Tone «за остатки» слегка sensational. **P2.**
- McKinsey high performers = **5.5% (109 of 1,993)** — verified. Источник публикации июнь-июль 2025. **OK.**
- HMGMA расположение — «**Брайан, штат Джорджия**» в chapter; правильное русское написание — Брайан-Каунти (Bryan County), Эллабелл, около Саванны. **P2 spelling/precision.**

## 2. `[FACT-CHECK]` markers resolution table

| # | Marker | Quote | Verification result | Action |
|---|---|---|---|---|
| 1 | [11] Deloitte 42% | «Deloitte 2025: 42% компаний отказались хотя бы от одной AI-инициативы; sunk cost 7,2M$» | **NOT verified.** Deloitte 2025 State of AI in Enterprise reports «42% strategy-ready», не «42% abandoned». Pertama Partners — единственный secondary source. | **REFORMULATE:** убрать ссылку на Deloitte, оставить только Pertama-агрегатор; или заменить на Deloitte-verified метрику «46% S&P Global PoCs scrapped» (есть в research notes 07-numbers §1.2). |
| 2 | [24] Tata Steel rolled back | «Tata Steel rolled back часть AI-implementations при смене сырья» | **NOT verified.** Tata Steel публично позиционируется как success-story (550+ моделей, Smart Factory Program). Никаких источников о rollback. | **REMOVE or REFORMULATE** как «общая отраслевая статистика rollback при смене сырья — Tata Steel один из примеров корпораций с агрессивной AI-программой, но specifically rollback-cases не disclosed». Или убрать конкретное упоминание Tata. |
| 3 | [38] Указ 250 | «Указ № 250 (2022) `[FACT-CHECK: точная дата]`» | **VERIFIED.** 01.05.2022 № 250 «О дополнительных мерах по обеспечению информационной безопасности РФ». kremlin.ru/acts/bank/47796, base.garant.ru/404561984/, publication.pravo.gov.ru/Document/View/0001202205010023. | **REMOVE marker, add canonical URL** (kremlin.ru или Garant). |
| 4 | [43] AB InBev rolled-back | «AB InBev откатил несколько AI-инициатив на цеховом уровне из-за недоверия операторов» | **NOT verified.** AB InBev +60% filtration cycle — verified, но rollback-case НЕТ публично. | **REMOVE specific AB InBev rollback claim** или переформулировать как hypothetical/category-level («worker-mistrust pattern документирован в нескольких industry surveys; specific AB InBev rollback не disclosed publicly»). |

## 3. `[VFY-day-of]` markers — freshness assessment

| # | Marker | Cadence | Days since pub | Verify-on-day | Verdict |
|---|---|---|---|---|---|
| s/146 | Markets and Markets / Fortune / Precedence | quarterly | varies | YES | KEEP — market estimates volatile by definition. |
| s/146 (McKinsey 78%) | quarterly | ~10 months (June 2025 survey) | YES | KEEP — McKinsey может опубликовать обновление 2026 H1. |
| s/155 (Siemens IFM) | monthly | ~14 months (March 2025 Hannover) | YES | KEEP — capabilities expanding rapidly; «150 PB» figure не нашёл в свежих source — verify. |
| s/217 (VW DPP) | monthly | ~10 months (Aug 2025 extension) | YES | KEEP — 1,200 AI apps verified для late 2025, но deployment count может вырасти. |
| s/258 (Hyundai-BD Atlas) | monthly | ~5 months (CES Jan 2026) | YES | KEEP — production scale & 30K/year target verified for **2028** не 2026; chapter не уточняет год. |
| s/344 (XtalPi 2024-2025) | quarterly | ~12 months | YES | KEEP. |

**`[VFY-day-of]` markers все обоснованы**, кроме одной добавки: Pfizer Vox в s/346 утверждает «+20 000 vaccine doses per batch» — это **fixed historical claim from AWS re:Invent Nov 2024**, NOT volatile (one-time measurement); current claim не меняется. `[VFY-day-of]` не нужен на этом числе. Не помечен — OK. **No action.**

Дополнительно — **add `[VFY-day-of]` to currently-unmarked claims:**
- Foxconn Liu 80% (vendor self-claim, может быть updated/walked-back).
- Toyota GAIA 10,000 models (figure updated 2023→2024, может быть 2025-2026 update).
- POSCO 180 edge nodes (deployment может вырасти).

## 4. Canonical cases verification table

| Case | Claim в chapter | Source verified | Verdict |
|---|---|---|---|
| **Tesla 2018 Musk «humans underrated»** | tweet 13.04.2018, CBS interview same day | @elonmusk status 984882630947753984, TechCrunch 13.04.2018, CNBC 13.04.2018 | ✅ Verified exactly |
| **Tesla 2024 GigaCast retreat** | May 2024, отказ от single-piece для Model 2 | CNBC 01.05.2024 — verified | ✅ Verified |
| **GE Predix $4B writedown** | «GE сожгла свыше 4 миллиардов» | $4B over 6 years, digital revenue $15B → $12B target — multiple sources | ✅ Verified |
| **Foxconn Wisconsin original promise** | «10 000+ рабочих мест» | Walker announcement: 3,000 initially + potential 13,000; «up to 10 000» Assembly memo | ⚠️ Undercounts. Should be «13 000 (potential headline) / 10 000 (Assembly memo)» |
| **Foxconn final ~1,500 jobs** | «около 1 500 фактических» | <1,500 — это **revised agreement target by 2024**, actual delivered ~281 jobs до пересмотра (NPR 2020) | ⚠️ Conflates target with actual |
| **Microsoft Fairwater $3.3B** | «3,3 миллиарда» | $3.3B AI data center verified | ✅ Verified |
| **Boeing 737 MAX 9 Jan 5 2024** | door plug, 4 bolts missing | NTSB, Wikipedia, NPR — verified | ✅ Verified |
| **Boeing AI inspection tool в Renton 2024** | tool deployed early 2024, photo-driven Dec 2025 | Boeing AvioRadar + Boeing.com Dec 2025 verified; 1,400 parts, 17h saved | ✅ Verified |
| **F-35 ALIS $44k/hour** | «44 000 долларов за лётный час» | $44,000 FY2018 baseline (CBO); по 2024 — $34-36K (improved) | ⚠️ Historical baseline ($44K = FY2018, не current). Chapter не указывает год |
| **F-35 ODIN replacement** | replaced by ODIN, false-positive rate | GAO — verified | ✅ Verified |
| **McKinsey 78%/5.5%** | adoption / high performers | 1,993 respondents, 109 = ~5.5% high performers, June-July 2025 survey | ✅ Verified |
| **MIT Sloan 95% / 14 months** | pilots fail to scale | «The GenAI Divide: State of AI in Business 2025» (NANDA initiative, MIT) | ✅ Verified |
| **RAND 80.3% / $547B** | AI projects fail value | RAND late 2025 — verified | ✅ Verified |
| **Deloitte 42% abandoned** | sunk cost $7.2M | **NOT verified** as Deloitte attribution | ❌ P0 |
| **Pfizer Vox +20K doses** | mRNA prediction algorithm | AWS Summit LA Nov 22 2024, AWS Bedrock + SageMaker, 67% cycle-time reduction, +20K doses/batch | ✅ Verified |
| **Yokogawa-JSR 35 days FKDPP** | 17.01-21.02.2022, 840 hours, RL distillation | Yokogawa press 22.03.2022, multi-source | ✅ Verified |
| **BASF Geismar -30% defects** | soft sensors | LSU collaboration verified; specific -30% не найдено в прямом BASF source | ⚠️ Verify via primary BASF source before lecture |
| **IBM Watson Health $1B** | sold Francisco Partners 2022 | $1.065B Jan 2022, renamed Merative | ✅ Verified (но tone «остатки» harsh) |
| **Holcim 100 plants C3 AI** | 4-year rollout, 45 at announcement | June 2024, May 2023 pilot, 45 plants, 3,000 sensors, 1,200 critical assets, 100+ target | ✅ Verified |
| **POSCO 180 edge nodes** | rolling mill assets 2024 | 180 nodes verified; «+5%/-10%/+3%» metrics НЕ found в направленном search | ⚠️ Verify metrics through POSCO press |
| **TSMC 95% accuracy** | wafer defect detection | 95% accuracy via deep learning, billions of wafer images — verified | ✅ Verified (но «+10-15% yield» — verify через Indium blog или TSMC IR) |
| **Toyota GAIA 8000→10000 models, 10K hours saved** | factory workers, 2023→2024 | Multi-source verified; Toyota official corporate release May 2025 | ✅ Verified |
| **Hyundai $26B / 30,000 robots / Bryan GA** | January 2026 CES | $26B US investment, 30,000 Atlas/year **by 2028** (chapter не уточняет год), Bryan County GA near Savannah | ⚠️ Year for 30K/year is 2028, chapter says «2026» roadmap — clarify |
| **Указ 250** | 01.05.2022, КИИ | kremlin.ru — verified | ✅ Verified — remove FACT-CHECK marker |
| **AB InBev +60% filtration** | Google Cloud + Pluto7 | Verified | ✅ Verified |
| **AB InBev rolled-back** | worker mistrust | **NOT verified** | ❌ P0 |

## 5. Russian context verifiability

| Кейс | Claim в chapter | Source quality | Verdict |
|---|---|---|---|
| **Норникель flotation/grinding** | industrial-operation stage | Nornickel Annual Report 2024 + Sustainability Report 2024 — first-party | ✅ Verified (vendor-claim, но first-party); chapter правильно помечает как public-verifiable |
| **Норникель + Газпром нефть Северо-Соленинское** | November 2024 agreement, well productivity services | Конкретного press release «Газпром нефть для Норникеля Северо-Соленинский GCF Nov 2024» **НЕ нашёл**. Северо-Соленинское — Nornickel's own gas operations (Sustainability Report); Газпром нефть отдельная компания | ⚠️ **Conflation risk** — verify accurate attribution. Chapter может смешать «Норникель сам управляет gas operations + Северо-Соленинское» с «получает services от Газпром нефть». Reformulate or verify. |
| **СИБУР Marketplace моделирования Q1 2025 / full functionality 2026** | импортозамещение | ComNews 29.11.2024 (только заявка о планах на 2026) — secondary source | ⚠️ Verify «launch v1 Q1 2025» actually happened — single secondary source ComNews. Better — direct SIBUR press release. |
| **ММК / НЛМК / Северсталь** | общие декларации без production metrics | Prometall + VC.ru — secondary | ⚠️ Acceptable as «недостаточная public disclosure» framing |
| **КАМАЗ Маяк-2.5, 18 trucks Level-3, 10 commercial M-11** | 2024-2025 коммерческая перевозка | TAdviser + Realnoe Vremya — secondary | ⚠️ Verify «10 in commercial operation on M-11» exact count |
| **Severstal profit -55% 2024, steel prices -18%/-8.5%** | financial context | VC.ru — secondary | ⚠️ Verify через Severstal IR + financial press для production-AI cost-pressure framing |

**Pedagogical framing «PR vs measurable effect»** в §3.5 — корректное. Russian context честно помечается как low-disclosure, что **сам по себе anti-pattern в reporting**, не proof отсутствия adoption. **Сильная methodological позиция.** Keep.

## 6. P0 / P1 / P2 issues

### P0 (factual errors — MUST fix before publication)

1. **Deloitte 42% misattribution** — [11] в §1.1. Deloitte 2025 State of AI Enterprise reports «42% strategy-prepared», не «42% abandoned». Pertama Partners — единственный secondary source. **Action: reformulate to remove direct Deloitte attribution, или replace with verified figure (S&P Global 46% PoCs scrapped).**

2. **AB InBev rolled-back AI-инициативы** — §3.6. Никакого публичного source. AB InBev публично позиционируется как success-story (+60% filtration). **Action: REMOVE specific AB InBev rollback claim или переформулировать на category-level pattern без AB InBev specifically.**

3. **Tata Steel rolled-back при смене сырья** — §3.6. Никакого публичного source. Tata Steel позиционируется как Smart Factory success. **Action: REMOVE Tata Steel attribution or generalize to «industry-pattern, specifics not publicly disclosed».**

### P1 (missing source / suspicious / needs clarification)

4. **Foxconn Wisconsin headline 13K vs 10K** — chapter undercounts. Walker promised 13,000 (potential); Assembly memo 10,000. **Action: clarify «10 000+ работ» → «до 13 000 jobs» (announced potential) или «10 000 (Assembly) / 13 000 (Walker)»**.

5. **Foxconn Wisconsin final ~1,500 vs 281** — chapter conflates revised agreement target with actual delivered. **Action: «scaled back agreement to fewer than 1,500 by 2024; actual delivered ~281 jobs до пересмотра (NPR 2020)».**

6. **F-35 ALIS $44k/hour без года** — это FY2018 baseline (CBO). По 2024 — $34-36K. **Action: добавить «$44k/час в FY2018 baseline; снижено до ~$35K по FY2024».**

7. **Hyundai 30,000 Atlas/year — год production target = 2028, не 2026**. Chapter упоминает «January 2026 announcement» (correct event date) и «30 000 единиц в год» без attestation на год production scale. **Action: clarify «production target 2028».**

8. **BASF Geismar -30% defects** — конкретный specific BASF press source не нашёл в направленном search (LSU collaboration verified, generic «AI digitalization» в BASF Report 2024 — но без -30% метрики). **Action: verify через BASF first-party + Chief AI Officer secondary; если нет primary — soften to «соответствующие отраслевые ROI cases дают порядок -20-30%».**

9. **POSCO «+5% production, -10% energy, +3% yield»** — direct POSCO press для этих чисел не находится в направленном search. **Action: verify; possibly через Manufacturing Digital primary or POSCO IR press release.**

10. **TSMC «+10-15% yield» improvement** — 95% accuracy verified; +10-15% yield не верифицирован в direct search. **Action: verify Indium blog primary + TSMC IR.**

11. **Норникель Газпром нефть Северо-Соленинское ноябрь 2024** — conflation risk между Nornickel's own gas operations и Gazprom Neft services. **Action: verify exact press release reference.**

12. **СИБУР маркетплейс Q1 2025 launch** — verify launch actually happened (chapter assertive); ComNews 2024 — единственный source о планах. **Action: verify SIBUR press release for Q1 2025 launch confirmation.**

13. **КАМАЗ «10 в коммерческой перевозке на М-11»** — verify count.

### P2 (cite format / minor / style)

14. **IBM Watson Health «за остатки»** — tone sensational. $1.065B with substantial assets (now Merative). **Soften.**

15. **HMGMA spelling «Брайан»** — правильно «Брайан-Каунти», Эллабелл, около Саванны. **Polish.**

16. **`[VFY-day-of]` add для трёх claims** (Foxconn Liu 80%, Toyota GAIA 10K, POSCO 180).

17. **Pertama Partners citation [10]** для McKinsey/MIT/RAND — secondary source; verify direct primary citation для McKinsey ([8]) и MIT ([9]) — already done через direct URLs, OK. Pertama OK как aggregator для RAND.

## 7. Recommendations for Phase 4 revision (book-editor)

### Top-3 facts requiring immediate fix (P0):

1. **§1.1 [11] Deloitte 42%** — remove direct Deloitte attribution; replace либо S&P Global 46% PoCs scrapped (verified in research notes), либо reframe как Pertama Partners aggregated finding.
2. **§3.6 AB InBev rolled-back** — remove or generalize to category-level («worker-mistrust documented industry-wide; specific AB InBev rollback not publicly disclosed»).
3. **§3.6 Tata Steel rolled-back** — remove or generalize («Tata Steel runs 550+ models; specific rollback-cases при смене feedstock не публично disclosed»).

### Top-5 P1 cleanups:

4. **§1.1 / Введение Foxconn Wisconsin** — clarify 13,000 (Walker peak promise) vs 10,000 (Assembly), и ~281 (NPR actual delivered) vs <1,500 (revised target by 2024).
5. **§3.3 F-35 ALIS** — добавить год «$44k/час в FY2018, снижено до ~$35K к FY2024».
6. **§2.3 Hyundai-BD Atlas** — «30 000 robots/year» — добавить «к 2028 году».
7. **§3.1 BASF Geismar -30%** — verify direct BASF source.
8. **§3.3 POSCO -10%/+5%/+3%** — verify direct POSCO source.

### Russian context — verify:

9. **§3.5 Норникель + Газпром нефть Северо-Соленинский** — exact press release attribution.
10. **§3.5 СИБУР Marketplace Q1 2025** — verify launch actually happened.

### Source hygiene:

11. **[38] Указ 250** — `[FACT-CHECK]` marker REMOVE — verified; add canonical URL kremlin.ru/acts/bank/47796 or base.garant.ru/404561984/.
12. **[11] Deloitte** — reformulate or replace.
13. **[24], [43]** — soften specific case attribution.

### Strengths (keep):

- McKinsey 78%/5.5%, MIT 95%/14 mo, RAND 80.3%/$547B — all rigorously sourced.
- Tesla 2018 cite chain (Musk tweet + CBS) — exact and verified.
- Yokogawa-JSR FKDPP, Pfizer Vox, Holcim C3 AI — first-party verified.
- Russian context honest framing «PR vs measured effect» — strong methodological position.
- `[VFY-day-of]` markers on volatile claims — well-placed.
- 43 inline citations с URLs — caractéristically thorough для academic chapter.
- §1.3 «Трио провалов» (GE/IBM/Foxconn) structurally verified, even if «остатки» tone harsh.

## 8. Verdict justification

**REVISE** (not REJECT, not APPROVE-WITH-POLISH):
- 3 P0 issues (Deloitte / AB InBev / Tata Steel) — все требуют source-level intervention перед publication, но **structurally fixable через reformulation**, не requiring chapter restructure.
- 10 P1 issues — substantive clarifications нужны, но source-grade chapter в основном.
- Strict-in failure/judgment content ≥30% не оцениваю (methodology-critic domain).

Chapter качественно research-driven, factually solid on big-picture claims (McKinsey/MIT/RAND/Tesla/Yokogawa/Pfizer), но **3 неверифицируемые attributions (Deloitte/AB InBev/Tata) и ~10 цифровых precisions требуют correction перед public-facing materials**. После P0 fixes — APPROVE-WITH-POLISH достижим.

---

**Total verified facts:** ~30/43 inline citations verified to first-party or strong secondary; 3 require fundamental reformulation; ~10 need minor precision tweaks.
**File saved:** `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-chapter-v1-fact-checker.md`.

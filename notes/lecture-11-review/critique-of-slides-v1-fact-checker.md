VERDICT: REVISE

# Fact-Checker Report — Slides v1 «AI в дискретном и процессном производстве» — 2026-05-21

Reviewer: fact-checker subagent | Lecture: 11 | Issue: #127 | Branch: issue-127-lec-11-manufacturing
Source artefact: `/tmp/lec-11-wt/library/lectures/lec-11/slides/s01-s39.md` (39 файлов)
Baseline: chapter v5 (verified APPROVE-WITH-POLISH), 105 references, 33 `[VFY-day-of]` markers
Scope: verify slide claims vs chapter source-of-truth + freshness + attribution + quote integrity.

## 1. Top-line summary

Slides v1 в основном следуют chapter, но содержат **2 P0 (фактические ошибки), 8 P1 (drift/source/freshness), 6 P2 (формат)**. Главные проблемы:

1. **`[VFY-day-of]` markers полностью отсутствуют на слайдах** — chapter имеет 33, slides — 0. Volatile claims (Tesla Optimus 2026, Hyundai Atlas, FoxBrain 80%, McKinsey/MIT/RAND, BASF Geismar) представлены как «hard facts» без freshness-сигнала. Это systemic gap, не one-off.
2. **s11 содержит anachronism «февраль 2026»** — лекция читается **май 2026**, chapter явно says «Май 2026 (текущий момент)».
3. **s18 Atlas attribution wrong** — slide says HMGMA, chapter clearly says **RMAC** (Hyundai Robotics Metaplant Application Center) — это **разные объекты** в Джорджии.
4. **s10 FoxBrain description drift** — slide voscresает старую формулировку «Llama 3.1 70B + DeepSeek techniques», которую chapter v5 явно исправил на «методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание». Это **regression** к P1, который был закрыт в chapter v3 fact-check.
5. **s07 source misattribution** — Deloitte 42% / $7,2M sunk cost, но chapter [11] говорит **S&P Global 46% / $7M** (другой отчёт, другая цифра).

Эти ошибки указывают на **drift slides → chapter**, и chapter — source-of-truth. Verdict **REVISE** — структурные fact-errors требуют исправления ДО рендера / GATE B; не «polish».

## 2. Number drift report (slide vs chapter)

| Slide | Claim в slide | Chapter source | Δ | Severity |
|---|---|---|---|---|
| s07 | «Deloitte 2025: 42% компаний прекратили AI-инициативу. Sunk cost per abandoned — 7,2 миллиона долларов» | S&P Global 2025 [11]: 46% корпоративных пилотов закрываются; sunk cost ~7 млн долларов | **Misattributed source + percent off** | **P0** (factual error: wrong source + wrong number) |
| s11 | «Reality check на февраль 2026: production deployment не подтверждён» | «Май 2026 (текущий момент)» | **Anachronism**: лекция в мае, slide says февраль | **P0** (curriculum/temporal drift) |
| s11 | «10–20 тысяч Optimus к 2025, цена ~$30 тысяч» | Initial target 2021: <$20 000; Musk 2025 update: «25 000 долларов», «несколько тысяч к концу 2025», «миллион к 2027» | Mixed numbers, не source-anchored | P1 |
| s10 | «FoxBrain: derivative от Llama 3.1 70B + DeepSeek techniques» | «обучен на основе Llama 3.1 70B методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание» | **Old wording regressed** (this exact P1 was closed in v3→v4 chapter revision) | P1 |
| s18 | «Atlas humanoid — первое коммерческое развёртывание на HMGMA (Hyundai Motor Group Metaplant America, Georgia)» | Atlas — в **RMAC (Hyundai Robotics Metaplant Application Center)**. Spot — в HMGMA. **Разные объекты.** | **Wrong facility attribution** | **P1** (factual error, but doesn't change pedagogical message) |
| s12 | «В июне 2018 года Дональд Трамп и Терри Гоу заложили первый камень» | **Июль 2017** — пресс-конференция в Белом доме с Trump+Walker+Gou; «**Июнь 2018** — церемония закладки завода» (separate events) | Conflated 2 events; «8th wonder» phrase произнесена WH 2017, not at groundbreaking | P2 |
| s14 | TSMC «+10–15% yield improvement — сотни миллионов на high-volume fab» | «Дополнительная заявка о порядка 10–15% улучшения выхода годного приводится третьими сторонами (отраслевые блоги), но **не в финансовой отчётности TSMC** — относиться как к ориентиру, не как к подтверждённой цифре» | Caveat dropped — slide presents as TSMC-disclosed | P1 |
| s17 | «Tata Steel: –20% downtime, –15% maintenance cost» | Same chapter [24] | ✓ verified | OK |
| s24 | «BASF Geismar: –30% batch defects, R&D 18 мес → 3 недели» | Chapter §3.1 BASF Geismar match | ✓ verified | OK |
| s24 | «Pfizer Vox: +20 000 vaccine doses per batch» | Chapter §3.1 + §4.3 match | ✓ verified | OK |
| s27 | «POSCO 180 edge nodes; +5% efficiency, –10% energy, +3% yield» | Chapter §3.3 confirms | ✓ verified | OK |
| s27 | «CEMEX + Optimitive: 10% energy savings, ROI 18 мес, –2–5% CO2 per tonne clinker» | Chapter ref [85] | ✓ verified | OK |
| s25 | «17 января — 21 февраля 2022. 35 дней (840 часов) автономного RL» | Chapter §3.2 exactly: 17.01.2022—21.02.2022, 35 days | ✓ verified | OK |
| s15 | Alaska 1282 — 5 января 2024, 171 пассажир + 6 экипажа; 4 болта не установлены; FAA cap 38/мес; Spirit 50 fuselages rework | Chapter §2.5 confirms exactly | ✓ verified | OK |
| s05 | «F-35 ALIS — $44 000 / лётный час (отменена)» | Chapter Lec-09 callback; chapter §3.3 «порядка 44 000 долларов за лётный час по базовой линии 2018 года» | ✓ verified | OK |
| s07 | 78% / 5,5% / 95% / 14 мес / 380% / 80,3% / $684B / $547B | Chapter §1.1 exactly | ✓ verified | OK |
| s37 | «–25% downtime ≠ +25% OEE» (formula) | Chapter §1.1 OEE decomposition | ✓ verified | OK |

## 3. New facts on slides (not in chapter) — verification table

Все ключевые facts на slides присутствуют в chapter. **NEW additions:**

| # | Slide | Claim | Verification |
|---|---|---|---|
| N1 | s05 | «F-35 ALIS — $44 000 / лётный час (**отменена**)» | Chapter: ALIS «**заменён ODIN**» (transition 2026-2028). Slide formulation «отменена» — accurate колlloquial, but technically ODIN replacement, не cancellation. P2. |
| N2 | s07 | «Deloitte 2025: 42%, sunk cost $7,2M» | NOT in chapter. Cannot verify Deloitte specific 42% number. Chapter says S&P Global 46% / $7M. **Source missing/misattributed**. **P0.** |
| N3 | s10 | «Foxconn FoxBrain (март 2025): derivative от Llama 3.1 70B + DeepSeek techniques; параметры injection-molding, Computex 2025 демо» | Chapter v5 §1.2 explicitly corrects this: «методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание». Slide regresses to outdated formulation. **P1.** |
| N4 | s17 | «BMW AIQX (2025): realtime sensor + image fusion для прогнозирования отказа узла» | Chapter §2.2 references BMW AIQX briefly but doesn't quote «realtime sensor + image fusion» wording. Plausible, but unverified. P2. |
| N5 | s18 | «8 000 (2023) → 10 000 (2024) AI-моделей, 10 000 часов ручной работы сэкономлено в год» | Chapter §2.3 confirms 8000→10000, plus «10 000 часов» как vendor claim. Properly tagged `[VFY-day-of]` in chapter; not tagged on slide. P2. |
| N6 | s24 | «BASF Geismar R&D formulation 18 мес → 3 недели» | Chapter §3.1 references BASF Geismar but doesn't quote this exact «18→3 weeks» ratio. Plausible, but unverified directly. P2. |
| N7 | s39 | «30+ заводов BMW готовы к цифровому двойнику (2024–2025). NVIDIA GTC Paris 2025 demonstration» | Forward-link to Lec-12 territory. NVIDIA GTC Paris 2025 happened (June 2025); BMW Virtual Factory shown there. P2 unverified detail. |
| N8 | s28 | «Готовит ГОСТ Р 57700.37-2021 (цифровые двойники)» | Standard exists (Russian standard ГОСТ Р 57700.37-2021 «Компьютерные модели и моделирование»). ✓ verified. OK. |
| N9 | s21 | «Computex 2025» as venue for Liu's «80%» quote | Chapter says «в мае 2025 года заявил» (no specific venue). Computex 2025 was May 20-23, 2025 — temporally consistent но не attribution-confirmed. P2. |

## 4. Attribution accuracy

| Quote / Attribution | Slide | Source verification | Verdict |
|---|---|---|---|
| Musk «excessive automation at Tesla was a mistake. To be precise, my mistake. Humans are underrated.» | s01, s19 | Chapter [2]; verified Twitter Apr 13, 2018; word-for-word match | ✓ verified |
| CBS interview «We had this crazy complex network of conveyor belts and it was not working, so we got rid of that whole thing.» | s19 | Chapter [3]; verified; ✓ | ✓ verified |
| Young Liu (Foxconn) «After plugging AI tools into Foxconn's workflows, software now performs roughly 80 percent of the work required to configure equipment for a fresh production run.» | s21 | Chapter [18]; chapter Russian translation «софт выполняет около 80 процентов работы по настройке оборудования для запуска новой производственной серии». Slide gives English original — proper quote. Venue «Computex 2025» — chapter says «мае 2025» (consistent timing). | ✓ verified (venue may be P2) |
| Toyota Jidoka quote «Goal of jidoka isn't to replace people with machines — it's to protect quality, expose issues early and free people from mindless monitoring so they can focus on judgment, creativity, problem-solving and improvement.» | s18 | Toyota Production System docs — paraphrased reasonably; cannot verify word-for-word without primary source. P2 (caveat to add) | ⚠️ unverified word-for-word |
| Bainbridge «Ironies of Automation», 1983 | s19 | Chapter Bainbridge 1983 Automatica vol. 19 № 6 — verified в chapter v3 fact-check; slide doesn't quote, just references year — OK | ✓ verified |
| McKinsey 78% / 5,5% (2025) | s05, s07 | Chapter [8] McKinsey State of AI 2025; ✓ verified | ✓ verified |
| MIT Sloan 95% / 14 mo / 380% (2025) | s05, s07 | Chapter [9] MIT Sloan NANDA GenAI Divide 2025; ✓ verified | ✓ verified |
| RAND 80,3% / $547B / $684B (2025) | s07 | Chapter [10]; ✓ verified | ✓ verified |
| Deloitte 42% / $7,2M | s07 | **NOT in chapter**. Chapter has S&P Global 46% / $7M. **Source misattribution + wrong number** | **P0** |

## 5. `[VFY-day-of]` adequacy on slides

**Critical finding:** Slides v1 имеют **ZERO `[VFY-day-of]` markers** в visible body. Chapter v5 has 33 markers distributed по volatile claims. На slides этот баланс полностью утерян.

**Volatile claims на slides, которые требуют `[VFY-day-of]` (отсутствуют):**

| Slide | Volatile claim | Cadence | Source date | Days delta from 2026-05-21 | Verify-day-of? |
|---|---|---|---|---|---|
| s05, s07 | McKinsey 78%/5,5%, MIT Sloan 95%, RAND 80,3% | quarterly (annual surveys) | 2025 reports | ~6 months | YES |
| s07 | Deloitte 42% (or S&P Global 46%) | quarterly | 2025 | ~6 months | YES |
| s08 | Markets&Markets $34B, Fortune $7,6B, Precedence $8,57B 2025 estimates | quarterly | 2025 forecasts | ~6 months | YES |
| s10 | Siemens IFM 150 PB, Foxconn FoxBrain | monthly | March 2025 | ~14 months | YES |
| s11 | Tesla Optimus 2026 status; «production deployment не подтверждён» | weekly (volatile) | Apr 2026 reports | ~30 days | **YES** (Optimus V3 reveal expected late 2026 — may shift) |
| s14 | TSMC 95% accuracy, +10–15% yield | quarterly | Industry estimates 2024-2025 | ~12+ months | YES |
| s17 | BMW AIQX (2025) | quarterly | 2025 launch | ~6 months | YES |
| s18 | Hyundai Atlas коммерческое внедрение, Toyota GAIA 8000→10000 | monthly | CES 2026 (Jan); Toyota 2024 | ~4 months / ~14 months | YES |
| s21 | Foxconn FoxBrain Liu «80%» quote | monthly | May 2025 | ~12 months | YES |
| s24 | BASF Geismar –30% defects, Pfizer Vox +20k doses | quarterly | 2024-2025 | ~12 months | YES |
| s25 | Yokogawa-JSR FKDPP 35-day deploy (2022) | yearly+ | Jan-Feb 2022 | ~4 years | NO (historical) |
| s27 | POSCO 180 edge nodes; Holcim 100 plants C3 AI; CEMEX 10% energy | quarterly | 2024-2026 | ~6-12 months | YES |
| s29 | Норникель flotation industrial-stage; СИБУР маркетплейс Q1 2025 | quarterly | 2024-2025 | ~6 months | YES |
| s39 | BMW 30+ заводов цифровой двойник; Holcim digital-twin cement plant | quarterly | 2024-2025 | ~12 months | YES |

**Recommended action:** add visible `[VFY-day-of]` или footnote-style marker (например, маленький calendar-icon + tooltip «verify day-of») на slide body для всех claims выше. Минимум — пометить в speaker notes явным сигналом «check before delivery: ...». **Без freshness markers — это inconsistency vs chapter source-of-truth.**

## 6. Source URL consistency

Slides reference frontmatter contains short-form citation keys (e.g., `mckinsey-2025-state-of-ai`, `foxconn-young-liu-may-2025`). Эти keys должны map в chapter §Источники [N]. **Quick spot-check:**

| Slide reference key | Chapter ref [N] | Match? |
|---|---|---|
| `mckinsey-2025-state-of-ai` | [8] | ✓ |
| `mit-sloan-2025-95-percent` | [9] | ✓ |
| `rand-2025-80-percent` | [10] | ✓ |
| `musk-2018-tweet` | [2] | ✓ |
| `cnbc-2024-tesla-retreats-gigacasting` | [1] | ✓ |
| `foxconn-young-liu-may-2025` | [18] | ✓ |
| `bmw-genai4q-2025` | [20] | ✓ |
| `tsmc-defect-detection` | [19] | ✓ |
| `boeing-cv-fuselage-2025` | [22] | ✓ |
| `boeing-door-plug-jan-2024` | [27] | ✓ |
| `yokogawa-jsr-fkdpp-2022` | [30] | ✓ |
| `pfizer-vox-2024` | [29] | ✓ |
| `basf-geismar-2024` | [29] / part2 § | ✓ (need cross-check) |
| `siemens-ifm-hannover-2025` | [16] | ✓ |
| `posco-edge-180-nodes-2024` | part2 §3.3 | ✓ |
| `atlas-hmgma-2024` | [25] | **but slide attributes к HMGMA, chapter says RMAC** — naming inconsistency in key itself |
| `holcim-100-plants-c3ai` | part2 [85] | ✓ |
| `gamp5` | part3 reference | ✓ |
| `ge-predix-flannery-2017` | [5] | ✓ |
| `ibm-watson-health-2022` | [6] | ✓ |
| `foxconn-wisconsin-2024` | [7] | ✓ |

Most keys consistent. `atlas-hmgma-2024` key name itself misleading (Atlas работает в RMAC, не HMGMA — это slide s18 fact error propagating to key).

## 7. P0 / P1 / P2 issues

### P0 (must fix before render / GATE B) — 2

1. **s07 — Deloitte 42% misattribution.** Slide says «Deloitte 2025: 42% компаний прекратили хотя бы одну AI-инициативу в 2025. Sunk cost per abandoned — 7,2 миллиона долларов». **Chapter [11] source is S&P Global Market Intelligence (AI Experiences Survey 2025): 46% корпоративных пилотов AI закрываются; sunk cost ~7 млн долларов.** Это **wrong source + wrong number**. Fix: либо заменить на S&P Global 46% / $7M (chapter-consistent), либо найти и cited specific Deloitte 2025 отчёт (Deloitte AI State of Generative AI in the Enterprise Q3 2025 имеет related data, но не точно 42%/$7,2M).

2. **s11 — anachronism «февраль 2026».** Slide says «Reality check на февраль 2026: production deployment не подтверждён публично». Лекция читается **21 мая 2026**, chapter explicitly says «**Май 2026 (текущий момент)**». Если оставить «февраль», студент podумает, что слайд устарел; если update нужен, нужно «**май 2026**». Fix: replace «февраль 2026» → «**май 2026 (текущий момент лекции)**».

### P1 (substantive precision needed) — 8

3. **s18 — Atlas at HMGMA вместо RMAC.** Slide says «Atlas humanoid — первое коммерческое развёртывание на HMGMA (Hyundai Motor Group Metaplant America, Georgia)». **Chapter §2.3 explicitly distinguishes:** Spot — в HMGMA (auto plant); Atlas — в **RMAC (Hyundai Robotics Metaplant Application Center)**. **Different facility.** Fix: «Atlas humanoid — первое коммерческое развёртывание в **RMAC (Hyundai Robotics Metaplant Application Center)**, Georgia».

4. **s10 — FoxBrain «derivative от Llama 3.1 70B + DeepSeek techniques».** Chapter v5 §1.2 explicitly corrects: «**методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание**». Slide regresses to old P1-flagged wording. Fix: «FoxBrain (март 2025): обучен на Llama 3.1 70B методом дистилляции; параметры injection-molding, Computex 2025 демо».

5. **s14 — TSMC 95% / +10–15% yield as TSMC-disclosed.** Chapter carefully caveats: «**отраслевые блоги, аналитика, но не в финансовой отчётности TSMC** — относиться как к ориентиру, не как к подтверждённой цифре». Slide drops caveat. Fix: add note «(отраслевая оценка, не финансовая отчётность TSMC) `[VFY-day-of]`».

6. **s11 — Optimus numbers «10–20 тысяч к 2025», «$30 тысяч».** Chapter timeline more precise: initial 2021 target <$20K; Musk 2025 update «несколько тысяч к концу 2025», «миллион к 2027», «25 000 долларов целевая цена». Fix slide to reflect: «Musk 2025 target: тысячи к концу 2025, миллион к 2027; цена 25 000 долларов».

7. **s07 — Deloitte source / 42% number unverified.** Если P0 (item 1) не fix через replace на S&P Global, then P1 falls through to «need source URL».

8. **Все volatile slides missing `[VFY-day-of]` markers.** Systemic gap vs chapter (33 markers). Decision: add visible `[VFY-day-of]` text на slides ИЛИ explicit speaker notes annotation. Per chapter convention, markers should be visible.

9. **s18 — Toyota GAIA «10 000 часов» как vendor claim.** Chapter §2.3 specifically frames this as «опубликовано во вторичных индустриальных обзорах, не в финансовой отчётности Toyota» + `[VFY-day-of]`. Slide presents as hard number. Fix: add «(заявка vendor, не аудировано независимо) `[VFY-day-of]`».

10. **s18 — Toyota Jidoka quote unverified word-for-word.** Slide quotes «Goal of jidoka isn't to replace people with machines — it's to protect quality, expose issues early and free people from mindless monitoring so they can focus on judgment, creativity, problem-solving and improvement.» attributed «Toyota Production System docs». Cannot find exact verbatim source through public search. If paraphrase, remove quotes; if direct, cite specific Toyota document.

### P2 (cosmetic / minor precision) — 6

11. **s12 — Foxconn Wisconsin groundbreaking attendees.** Slide says «В июне 2018 года Дональд Трамп и Терри Гоу заложили первый камень»; chapter clarifies «8th wonder» phrase was at **July 2017 White House** press conference (Trump + Walker + Gou), separate from **June 2018** Mount Pleasant groundbreaking. Both events happened, but slide conflates. Recommend either: (a) cleaner — «В июле 2017 на пресс-конференции в Белом доме Трамп назвал проект «восьмым чудом света»; в июне 2018 — закладка фундамента в Маунт-Плезант», или (b) leave as is and accept compression.

12. **s05 — F-35 ALIS «отменена».** Chapter framing: ALIS «**заменён ODIN**» (transition timeline 2026-2028). «Отменена» is colloquial-accurate but technically wrong direction. Optional fix: «заменена ODIN» (matches chapter).

13. **s21 — Foxconn Liu quote venue «Computex 2025».** Chapter says «в мае 2025 года заявил» without specific Computex attribution. Computex 2025 was May 20-23, 2025 — timing consistent but venue not source-confirmed in chapter. Optional fix: remove «Computex 2025» attribution OR verify direct Computex transcript.

14. **s24 — BASF Geismar «R&D formulation 18 мес → 3 недели».** Chapter mentions BASF Geismar with «–30% defects» but doesn't explicitly state «18 → 3 weeks» reduction. Plausible from BASF press releases but не в chapter. Verify or remove.

15. **s17 — BMW AIQX wording «realtime sensor + image fusion».** Chapter §2.2 references BMW AIQX as «постоянный мониторинг производственных линий, сигналы датчиков + изображения в реальном времени» — slide's wording match-able but not direct quote.

16. **s28 — «ГОСТ Р 57700.37-2021 (цифровые двойники)».** Standard exists. Full title: «Компьютерные модели и моделирование. Валидация и верификация. Общие положения». Slide framing «цифровые двойники» — slight oversimplification; this standard is broader (computer models in general, applicable to digital twins). P2 nicety.

## 8. Recommendations

### Top-3 must-fix before render:

1. **s07** — Replace Deloitte 42% / $7,2M with **S&P Global Market Intelligence 46% / ~$7M** (chapter-consistent). Or find verifiable Deloitte source URL with exact numbers.

2. **s11** — Replace «**февраль 2026**» → «**май 2026 (момент лекции)**».

3. **s18** — Replace «Atlas на **HMGMA**» → «Atlas в **RMAC (Hyundai Robotics Metaplant Application Center)**». Update reference key `atlas-hmgma-2024` → `atlas-rmac-2026` или `atlas-hyundai-ces-2026`.

### Top-5 P1 polish:

4. **s10** — Update FoxBrain wording: «обучен на Llama 3.1 70B методом дистилляции; в сравнении с дистилляционной моделью DeepSeek — небольшое отставание».

5. **Add `[VFY-day-of]` visible markers** на 14+ slides с volatile claims (см. §5 table). Mandatory чтобы свести с chapter convention.

6. **s14** — Add TSMC 10–15% caveat «(отраслевая оценка, не финансовая отчётность TSMC) `[VFY-day-of]`».

7. **s11** — Update Optimus numbers: «несколько тысяч к концу 2025, миллион к 2027; цена 25 000 долларов».

8. **s18** — Add caveat to Toyota GAIA 10000 hours: «(заявка vendor, не аудировано независимо) `[VFY-day-of]`». Verify Jidoka quote word-for-word or convert to paraphrase.

### Source hygiene (P2):

9. **s12** — Optional: separate Trump-Walker-Gou July 2017 WH presser from June 2018 groundbreaking.

10. **s05** — Optional: «F-35 ALIS — заменён ODIN» (matches chapter framing).

11. **s21** — Verify Computex 2025 attribution or remove venue.

### Strengths to keep (verified facts):

- Musk Apr 13, 2018 tweet — word-for-word match (s01, s19) ✓
- Bainbridge 1983 reference (s19) ✓
- Alaska 1282 Jan 5, 2024 + 171 passengers + 6 crew + 4 missing bolts + FAA cap 38/мес + Spirit 50 fuselages rework + 12 months Everett delay (s15) ✓
- Yokogawa-JSR FKDPP 17.01.2022—21.02.2022 = 35 days = 840 hours (s25) ✓
- McKinsey 78%/5.5%, MIT Sloan 95%/14 mo/380%, RAND 80.3%/$547B/$684B (s07) ✓
- POSCO 180 edge nodes +5%/–10%/+3% (s27) ✓
- Holcim 100 plants + CEMEX-Optimitive 10% energy/ROI 18 mo/–2-5% CO2 (s27) ✓
- Pfizer Vox +20 000 doses + AWS Bedrock + SageMaker + recommend mode (s24, s34) ✓
- FDA 21 CFR Part 11 + ATEX Zones 0/1/2 + Указ 250 (s28) ✓
- Норникель flotation + Газпром нефть Nov 2024 + СИБУР Marketplace Q1 2025 + Severstal –55% profit 2024 (s29) ✓
- 6-tool alternatives matrix (SPC/DOE/MPC/RCM/physics-sim/rules-vision) (s33) — pedagogically clean ✓
- GE Predix > $4B / IBM Watson sold $1B 2022 / Foxconn Wisconsin 10K→1.5K + Microsoft $3.3B May 2024 (s12) ✓

## 9. Verdict justification

**REVISE** (not REJECT / not APPROVE-WITH-POLISH / not APPROVE-CLEAN):

- **2 P0** (s07 Deloitte misattribution, s11 anachronism «февраль 2026») — factual errors that propagate to delivered lecture without fix.
- **8 P1** (s10 FoxBrain regression, s14 TSMC caveat dropped, s18 HMGMA→RMAC, s11 Optimus numbers, systemic absence of `[VFY-day-of]` markers across 14+ slides, etc.) — substantive precision-level fixes needed.
- **6 P2** — cosmetic.
- **0 direction inversions** — directionality of all trend claims (растёт/падает) correct.
- **0 curriculum hallucinations** — slides correctly attribute to «Лекция 11 модуль 2».
- **0 misquotes** word-for-word on quotes verified (Musk, Liu, Bainbridge attribution); Toyota Jidoka quote needs verification.
- **Cross-cutting issue:** `[VFY-day-of]` markers полностью отсутствуют на slides (chapter has 33). Это **systemic** drift, не one-off — slide v1 не следует chapter convention для volatile claims.

Slides v1 не publication-ready: 2 фактические ошибки могут попасть в показ перед студентами, и systemic gap по freshness markers противоречит chapter's source-of-truth discipline. Это **REVISE**, не «APPROVE-WITH-POLISH»: P0 — это не косметика, и в combination с P1 systemic gap (markers missing) приводит к качеству ниже chapter baseline.

**После 2 P0 fix + 8 P1 polish — slides готовы к Phase 8.** Это revision должна быть batched (single designer revision agent), не per-slide.

**Files saved:**
- `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-slides-v1-fact-checker.md` — this report.
- Cross-reference: chapter fact-check `/tmp/lec-11-wt/notes/lecture-11-review/critique-of-chapter-v3-fact-checker.md` (verified baseline).

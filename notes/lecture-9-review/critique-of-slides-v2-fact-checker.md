# fact-checker — slides v2 (Phase 7)

**Дата:** 2026-05-20
**Targets:** rendered/iter7/s-{01..34}.png + speaker_notes (PPTX visible body)
**WebSearch usage:** 17 запросов
**Verdict:** REVISE

---

## TL;DR

Slides v2 unbox 34 рендеров содержат **2 P0 факт-ошибки** (унаследованы от chapter v3 без correction → drift) + **6 P1 facts / framing-issues** + **5 P2 polish**.

Главное:
- **P0-1.** Слайд 12 (Adversarial SAR): «Du et al. 2024 (arXiv:2312.02912)» — **wrong authors AND wrong year**. Реально: Ye, Kannan, Prasanna, Busart, Kaplan (2023). Эта же ошибка в chapter §1.7 (line 258, line 903). Drift inherited.
- **P0-2.** Слайд 15 (Decide vendors): «Thunderforge для **CENTCOM/INDOPACOM**» — **wrong combatant command**. DIU March 2025 контракт — для **INDOPACOM и EUCOM** (European Command, не Central Command). Та же ошибка в chapter §2.2 (line 320). Drift inherited.

≥1 P0 при правиле «≥3 P0 → REJECT» — не достигаем REJECT, но **2 P0 = REVISE**. Должны быть исправлены до GATE B (и одновременно в chapter §1.7 + §2.2 во избежание drift forever).

Все остальные P0-кандидаты (Lavender 37k/90%/3.7k/20s, Vincennes 290/3July1988, MCAS 346/189/157, UN 161-3-13, UN 164-6-7 с 6 странами против, Anduril Fury 31 Oct 2025, Helsing €12B, Maxar 250 PB, Geran-2 26k/2700, X-62A VISTA Sept 2023, Kendall May 2024, Skywise 11600, F-35 $42-44k/h, Dell PowerEdge 1111 servers, ICRC quote, 270 NGOs / 70 countries) — **подтверждены WebSearch против primary sources**. Chapter v3 fact-checked основа = слайды стабильно отражают её.

---

## Severity counts
- **P0** (false fact / broken citation / direction inversion / curriculum hallucination): **2**
- **P1** (missing source / suspicious number / framing-issue): **6**
- **P2** (cite format / minor): **5**

---

## P0 fact errors

### P0-1. Слайд 12 (s14 adversarial SAR + GPS) — wrong citation Du et al. 2024

**Что на слайде (визуальный body):**
> Источник: Du et al. 2024 (arXiv:2312.02912)

**Реальные authors / year (verified via arxiv.org/abs/2312.02912):**
- Title: «Realistic Scatterer Based Adversarial Attacks on SAR Image Classifiers»
- Authors: **Tian Ye, Rajgopal Kannan, Viktor Prasanna, Carl Busart, Lance Kaplan**
- Submitted: **5 December 2023** (не 2024)
- Accepted: IEEE International Radar Conference 2023

**Issue:** Cite полностью неверный — **wrong first author** (Du vs Ye) + **wrong year** (2024 vs 2023). arXiv ID `2312.02912` корректен, но без правильных авторов студент не найдёт paper уверенно.

**Drift origin:** chapter v3 §1.7 (line 258): «Опубликованные исследования показывают физическую реализуемость таких атак (Du et al., 2024; arXiv 2312.02912)» — **та же ошибка в первоисточнике**. Цитата в §Источники chapter (line 903): «27. Du, X., et al. (2024). Realistic Scatterer SAR Adversarial Attacks. arXiv:2312.02912.» — также неверная.

**Suggested fix (slide + chapter):**
- Slide caption: «Источник: Ye et al. 2023 (arXiv:2312.02912)»
- Chapter line 258: «(Ye et al., 2023; arXiv 2312.02912)»
- Chapter §Источники line 903: «27. Ye, T., Kannan, R., Prasanna, V., Busart, C., Kaplan, L. (2023). *Realistic Scatterer Based Adversarial Attacks on SAR Image Classifiers*. IEEE International Radar Conference 2023; arXiv:2312.02912.»

**Severity:** P0 (false attribution; impacts academic credibility если студент попытается find paper).

---

### P0-2. Слайд 15 (Decide vendors) — Thunderforge для CENTCOM/INDOPACOM (wrong combatant command)

**Что на слайде (визуальный body):**
> Scale AI: Donovan → Defense Llama → Thunderforge
> США · уровень L1–L2
> Mar 2025 — Thunderforge для **CENTCOM/INDOPACOM**

**Реальный fact (verified via DIU.mil March 2025 press release + Breaking Defense + Defense Scoop):**
- DIU awarded prototype contract to Scale AI for Thunderforge **5 March 2025**.
- Deployment initially: **INDOPACOM and EUCOM** (European Command).
- **NOT CENTCOM** (Central Command).

**Drift origin:** chapter v3 §2.2 (line 320, table cell):
> | **Thunderforge** | март 2025 | CENTCOM, INDOPACOM | Wargaming + COA generation... |

— та же ошибка («CENTCOM, INDOPACOM» вместо «INDOPACOM, EUCOM»). Drift inherited на slide unchanged.

**Suggested fix (slide + chapter):**
- Slide 15: «Mar 2025 — Thunderforge для **INDOPACOM/EUCOM**»
- Chapter §2.2 table line 320: «INDOPACOM, EUCOM»

**Severity:** P0 (incorrect named combatant command — substantive factual error, не cosmetic). Verifiable easily; студент-инженер заметит при cross-check.

**Sources:**
- https://www.diu.mil/latest/dius-thunderforge-project-to-integrate-commercial-ai-powered-decision-making
- https://defensescoop.com/2025/03/05/diu-thunderforge-scale-ai-combatant-commands-indopacom-eucom/
- https://breakingdefense.com/2025/03/ai-for-war-plans-pentagon-innovation-shop-taps-scale-ai-to-build-thunderforge-prototype/

---

## P1 fact issues

### P1-1. Слайд 27 (Maven) — «Anduril $30,5 млрд» в Эре 2 (2018–2024) — date framing mismatch

**Что на слайде:**
> Эра 2: замена вендоров · 2018–2024
> • Anduril — $30,5 млрд
> • Palantir — $60 млрд капитализация

**Issue:** $30.5B valuation Anduril достигнут в **June 2025** (Series G, $2.5B raise, Founders Fund lead), не в 2018–2024. Также Palantir $60B капитализация — outdated reference point (current 2026 cap = $320+ billion). Группировка «Эра 2 (2018-2024)» создаёт imprecise framing — числа выглядят как «состояние конца 2024 года», но фактически Anduril $30.5B — June 2025.

**Suggested fix:**
- Либо: «Anduril — $14 млрд (Aug 2024) → $30,5 млрд (Jun 2025)» (показывает trajectory)
- Либо: extend Эра 2 to «2018–2025» и pair stats с конкретной датой каждой.
- Palantir: каноничнее показать market cap snapshot с датой (e.g. «~$60 млрд (нач. 2024) → $320+ млрд (май 2026)») — это показывает рост в защитном секторе сильнее.

**Severity:** P1 (numbers correct в isolation, но wrong period framing подразумевает старый snapshot; читатель может вывести incorrect timeline).

---

### P1-2. Слайд 26 (UN GGE) — UN press 164/6/7 без disambig 156/5/8 от SKR

**Что на слайде (визуальный body):**
> Нояб. 2025 · Третья подряд резолюция · 164 / 6 / 7

**Issue:** Chapter §4.2 (line 554) и §4.7 (line 644) явно указывают: «164/6/7 (UN official press ga12736; **156/5/8 по Stop Killer Robots — расхождение связано с разными методиками подсчёта**)». Slide показывает только UN press version без disambig — теряется лекторский nuance.

Это **не false fact** — UN press version официальная и корректная. Но как critical lecture artifact это **incomplete reflection** chapter's careful methodology note. Студент, видящий slide 26 only, не будет знать про SKR variant и при cross-check с SKR website удивится.

**Suggested fix:**
- В footer slide 26 (или speaker notes): «UN press ga12736: 164/6/7. Stop Killer Robots: 156/5/8 — methodology difference».
- Если место не позволяет → speaker_notes только.

**Severity:** P1 (loss of disambiguation nuance; recoverable in speaker notes).

---

### P1-3. Слайд 9 (constellation) — Slingshot «Agatha · ТАЛОС · 2025» conflated

**Что на слайде:**
> Слежение за космосом · Slingshot Agatha · ТАЛОС · 2025

**Issue:** Agatha и TALOS — **два different products** Slingshot Aerospace:
- **Agatha** (с DARPA): anomaly detection в large satellite constellations (поведение спутников на орбите).
- **TALOS** (Thinking Agent for Logical Operations and Strategy, **July 2025**): adversary-simulation training для Space Force operators (training simulator, не on-orbit ML).

Slide группирует их под «Слежение за космосом» (space tracking), но TALOS — это **training environment**, не tracking system. Conflation reduces precision.

**Suggested fix:** либо only Agatha (правильно для «слежение за космосом» + on-orbit anomaly detection), либо разделить два продукта явно.

**Severity:** P1 (factually each name correct, но категория «слежение за космосом» не подходит TALOS — это simulator).

**Sources:**
- https://www.slingshot.space/product-agatha (Agatha = anomaly detection)
- https://defensescoop.com/2025/07/29/space-force-ai-training-satellite-operations-slingshot-aerospace-talos/ (TALOS = July 2025 training simulator)

---

### P1-4. Слайд 20 (Anduril Fury) — «23 марта 2026 Arsenal-1» off by one day

**Что на слайде:**
> 23 марта 2026 · Arsenal-1, Огайо · $1 млрд инвестиций

**Реальный fact:** YFQ-44A serial production officially announced **24 марта 2026** (Aviationist article, Anduril announcement). $1 млрд investment в Arsenal-1 ✓ verified.

**Suggested fix:** «24 марта 2026» — или просто «Март 2026» если точная дата не критична.

**Severity:** P1 (date off by one day; verifiable easily; small but specific).

**Sources:**
- https://theaviationist.com/2026/03/24/yfq-44a-fury-cca-is-now-in-production/
- https://www.anduril.com/news/anduril-building-arsenal-1-hyperscale-manufacturing-facility-in-ohio

---

### P1-5. Слайд 11 (predictive maintenance) — «easyJet 44 cancelled flights prevented (2024)»

**Что на слайде:**
> easyJet: −8,1 тонны топлива/ВС/год + 44 отменённых рейса предотвращены (2024).

**Реальный fact:** Per Airbus October 2024 announcement, easyJet using SFP+ avoided:
- **44 cancellations в июле 2024**
- **35 cancellations в августе 2024**
- Не сумма «44 за весь 2024 год» — это **только июль 2024**.

**Suggested fix:** «44 отменённых рейса в июле 2024 предотвращены» — точнее, чем «(2024)».

**Severity:** P1 (number correct, но year framing imprecise; читатель может вывести «44 за весь год» — это понижение).

**Source:** https://www.aircraft.airbus.com/en/newsroom/news/2024-10-keeping-the-fleet-flying

---

### P1-6. Слайд 27 (Maven) — «12 увольнений» Google 2018

**Что на слайде:**
> Эра 1: уход из Maven · 2018
> • Март 2018: утечка Google
> • 4 000+ подписей · ~12 увольнений
> • Июнь 2018: Google не продлевает

**Реальный fact:**
- ~12 (или «a dozen») увольнений ✓ verified (Common Dreams, Axios, FedScoop).
- 4000+ подписей ✓ verified.
- Petition появилась в апреле 2018, не «март 2018: утечка». Утечка контракта произошла в феврале/марте — детали могут разниться в источниках. Slide framing «март 2018: утечка Google» — допустимое упрощение (Gizmodo break: 6 March 2018).

**Suggested fix:** опционально уточнить «Март 2018: утечка Gizmodo» если место есть; не критично.

**Severity:** P1-soft (verifiable; minor accuracy could improve но текущее формулирование plausible).

---

## P2 polish

### P2-1. Слайд 8 (Maxar Sentry) — изображение png показывает small inline artifacts

Текст на slide-8 (s-08) показывается с трудночитаемыми элементами из-за compression на маленьком PNG (1334×750). Speaker notes указывают «обнаруженное изменение» как label на image — **корректно**. Body text верно. P2-2 — резолюция render-snapshot.

### P2-2. Слайд 5 (keystone OODA) — «Бойд, ВВС США, 1976»

Тонкая deviation от chapter: «Boyd 1976» / «John Boyd, USAF 1976» — на slide уж «ВВС США» (Russian rendering). ✓ correct. Минор: USAF Air Force, не ВВС США буквально (in Russian источниках Boyd обычно с full name «Джон Бойд»). P2.

### P2-3. Слайд 12 (s14 GPS) — «Российские средства РЭБ («Красуха-4», «Борисоглебск-2»)»

Spellings ✓ correct. «Красуха-4» (R-330Ж Жулил/Krasukha-4) and «Борисоглебск-2» (Borisoglebsk-2) — real Russian EW systems. Geographic claim («Чёрное море, Восточная Европа») plausible / not directly cite-checked but matches widely-reported NATO concerns. P2 — acceptable as-is.

### P2-4. Слайд 30 (career angle) — «5 источников»

«Stop Killer Robots briefs 2025» (item 5 в reading list) — recurring published series, не one item. Acceptable framing, но добавление concrete URL (stopkillerrobots.org/resources) усилило бы. P2.

### P2-5. Слайд 22 (Geran-2) — «2026 — головка наведения на радиоизлучение»

Future tense с 2026 date — это **anticipated capability**, не confirmed deployment. Slide phrasing «2026 — головка...» (without «ожидается» / «по сообщениям») reads as deployed fact. Per meta-defense.fr April 2026 article: «evolving into anti-radar version» — это direction, не «deployed in 2026». P2 — add «ожидается» / «(prelim. reports)».

---

## Volatile [VFY-day-of] discipline

Visible body на 34 slides **не содержит** flag-маркеров типа `[VFY-day-of]` или `[FACT-CHECK]` (correctly — frontmatter-only enforced). ✓

Однако несколько P1-volatile claims заслуживают «verify on day of lecture» pre-flight check:

**HIGH-RISK to recheck day-of-lecture:**

| Slide | Claim | Source | Cadence | Risk |
|-|-|-|-|-|
| s-08 | Maxar 250 PB архив | Press release June 25, 2025 | Quarterly (data accumulates) | LOW — base number stable |
| s-11 | Skywise 11 600 aircraft (late 2024) | Airbus Oct 2024 | Monthly-quarterly (growing fleet) | MEDIUM — may be 12k+ by lecture day |
| s-11 | Rolls-Royce «~400 событий/год» | Rolls-Royce IR 2024 | Yearly | LOW |
| s-15 | Palantir MSS «$1,3 млрд потолок до 2029» | DoD May 2025 | Yearly+ contract ceiling | LOW |
| s-15 | Helsing €12 млрд (Series D Jun 2025) | TechCrunch / Helsing IR | Monthly (Helsing growing fast, $18B round в May 2026) | **HIGH** — на 20 мая 2026 уже видны $18B reports от TechCrunch/Dragoneer round |
| s-20 | Anduril CCA первый полёт 31 Oct 2025 | Anduril / Aviationist | Historical (fixed event) | LOW |
| s-20 | Arsenal-1 «$1 млрд инвестиций» | Anduril Jan 2025 | Yearly+ | LOW |
| s-22 | Geran-2 «~2700-3000/мес к концу 2025», «>26000 произведено», «>40000 план к концу 2025» | Ukrainian Defense Intel | Monthly (active war stats) | **HIGH** — verify day-of-lecture |
| s-22 | Dell PowerEdge 1111 servers Apr-Aug 2024 | Bloomberg / TechSpot | Historical | LOW |
| s-26 | UN GGE Nov 2025 vote 164/6/7 | UN press ga12736 | Yearly (annual vote, next ~Nov 2026) | LOW |
| s-27 | Palantir $60 млрд капитализация | (старая дата) | Daily (stock market) | **HIGH** — currently ~$320B |

**Critical day-of-lecture refresh items:**
1. **Helsing valuation** (s-15) — может быть outdated: TechCrunch reports «$18B round Daniel Ek-backed» (May 2026). Если lecture после mid-May 2026 — обновить.
2. **Geran-2 production stats** (s-22) — active war stats, monthly cadence.
3. **Palantir market cap** (s-27) — already outdated by ~5× (was $60B in 2024, now $320B+). Drop number или update.

---

## Drift from chapter (если есть)

**P0-1 (Du et al.) и P0-2 (CENTCOM/INDOPACOM)** — **обе drift INTO slides FROM chapter**. Это не slides-only errors; они существуют в chapter v3 §1.7 и §2.2 соответственно. Chapter v3 ранее имел fact-checker APPROVE-CLEAN — означает эти 2 P0 **пропустились на phase 3 fact-check** или fact-checker subset не покрыл §1.7 + §2.2.

**Mitigation:** chapter v3 fact-checker subset (`critique-of-chapter-v2-fact-checker-subset.md` per filename) был targeted, не полный. Полный re-check на ВСЕ chapter citations не происходил. Recommend:
1. **Fix obе drift на phase 7 simultaneously в chapter + slides** (single book-editor + presentation-designer revision).
2. **Phase 8 — final chapter fact-check включает full citation sweep** (не subset).

---

## Strengths

1. **UN votes accuracy excellent.** Slide 26 (UN GGE) + Slide 29 (Russia votes) — 161/3/13, 164/6/7, 6 stran against (Belarus, Burundi, DPRK, Israel, Russia, USA) — **all match UN press ga12736 exactly**. Включая «4 года подряд резолюции» framing. Подтверждено через WebSearch + cross-ref chapter §4.2 line 552-554.

2. **Lavender canonical case bullet-proof.** Slide 16 (Lavender) — 37 000 / 90% / 3 700 / 20 seconds / 15-20 civilian casualties per junior operator — **все цифры match +972/Local Call (Abraham 2024)** exact. Lieber Institute / ICRC / AOAV academic разборы corrrectly cited.

3. **Vincennes details correct.** Slide 17 — «3 июля 1988», «290 погибших», «Iran Air 655», «2 ракеты SM-2», «Aegis записал climbing, операторы доложили descending» — все точно match Wikipedia + USNI Proceedings July 2018.

4. **MCAS hronology accurate.** Slide 23 — «29 окт 2018 Lion Air 610 → 189», «10 мар 2019 Ethiopian 302 → 157», «→ 346 всего», «20 мес остановки в США» — все verified vs PBS Frontline + Wikipedia + multiple sources.

5. **Anduril Fury timeline.** Slide 20 — «первый полёт 31 октября 2025» ✓ exactly matches Aviationist, Anduril press, Air & Space Forces.

6. **F-35 ALIS cost.** Slide 11 — «$42-44 тыс./час» ✓ matches GAO + Defense One reporting ($42k/h published baseline).

7. **DARPA X-62A timeline.** Slide 21 — «Сент. 2023 первая ИИ-дуэль с F-16: 600 м @ 1200 миль/ч», «Май 2024 секретарь USAF Кендалл» — ✓ all match DARPA press, Lockheed Martin, Aviationist. («600 m» = 2000 ft ✓).

8. **Geran-2 stats current.** Slide 22 — «~2700-3000/мес», «>26 000 произведено», «>40 000 план» — все matches Ukrainian Defense Intel May 2025 reports.

9. **Maxar Sentry technical specs.** Slide 8 — «250 ПБ», «20+ years», «3 sensors», «NGA Luno A» — ✓ all match Maxar June 25, 2025 press release.

10. **Helsing details (apart from P1-1 framing).** «€12 млрд после Series D (июнь 2025)», «Altra + Centaur», «Centaur ИИ-пилот на Gripen E» — ✓ verified vs Tech.eu June 17 2025 + Helsing IR.

11. **ICRC quote on Slide 26 verbatim ✓.** «Не оружейная система должна соответствовать международному гуманитарному праву — это люди, использующие её.» — exact verbatim match с ICRC position paper.

12. **Maven 2018 numbers ✓.** Slide 27 — «4 000+ подписей · ~12 увольнений» — match Common Dreams + Axios sources from 2018.

13. **Patriot 2003 / 2024 ✓.** Slide 23 — «2003 (RAF Tornado + ВМС США F/A-18) + 2024 (украинский F-16)» — Tornado shootdown 23 March 2003, F/A-18 shootdown 2 April 2003 verified.

14. **Dell PowerEdge supply chain (s22) ✓.** «1 111 серверов Dell PowerEdge XE9680 через индийскую Shreya Life Sciences в апреле-августе 2024» — exact match Bloomberg / TechSpot reporting.

---

## Recommendations

### Immediate (before USER GATE B)

1. **Fix P0-1 (Du → Ye et al. 2023)** in slide s-12 (chapter §1.7 line 258 + §Источники line 903 simultaneously). Single batch revision via book-editor + presentation-designer.

2. **Fix P0-2 (CENTCOM → EUCOM)** in slide s-15 (chapter §2.2 line 320 simultaneously). Same batch as #1.

3. **Day-of-lecture refresh discipline** — add to instructor pre-flight checklist:
   - Helsing valuation (€12B → confirm or update if $18B round confirmed)
   - Geran-2 monthly production rate
   - Palantir market cap (s-27 «$60 млрд» — update or remove)

### Polish (before final GATE C)

4. **P1-3 Slingshot** — separate Agatha (orbit tracking) and TALOS (training sim) or drop TALOS from s-09.

5. **P1-2 UN votes disambig** — add «UN press 164/6/7 vs SKR 156/5/8» note in speaker_notes on slide 26.

6. **P1-4 Anduril date** — fix «23 March 2026» → «24 March 2026» или «Март 2026» on s-20.

7. **P1-5 easyJet** — clarify «44 отменённых рейса в **июле 2024**» on s-11.

8. **P1-1 Maven Эра 2 framing** — show Anduril/Palantir с конкретными датами snapshot.

### Cross-cutting

9. **Chapter v3 full citation sweep recommended** — given 2 drifts inherited (Du, CENTCOM), full re-check всех citations (not subset) до GATE A close. Recommend separate book-editor pass на §Источники + inline cite formats.

10. **Verdict for slides v2 = REVISE.** 2 P0 errors block APPROVE-WITH-POLISH. Once fixes #1 + #2 applied + slide re-render, expect APPROVE-CLEAN (or APPROVE-WITH-POLISH if other P1s deferred).

---

## Files referenced

- `/tmp/lec-09-wt/library/lectures/lec-09/chapter.md` — chapter v3 (line 258 Du citation; line 320 CENTCOM; line 903 Источники)
- `/tmp/lec-09-wt/library/lectures/lec-09/slides/s14-adversarial-sar-gps.md` — Du citation on slide
- `/tmp/lec-09-wt/library/lectures/lec-09/slides/s18-palantir-mss.md` — CENTCOM/INDOPACOM on slide
- `/tmp/lec-09-wt/library/lectures/lec-09/rendered/lec-09.pptx` — rendered PPTX visible body source
- `/tmp/lec-09-wt/library/lectures/lec-09/rendered/snapshots/iter7/s-{01..34}.png` — 34 PNG renders verified

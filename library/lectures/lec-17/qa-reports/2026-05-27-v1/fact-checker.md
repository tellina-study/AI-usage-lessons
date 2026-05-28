# Fact-Checker Report — Lec-17 Chapter v1

**VERDICT: REVISE**

**Date:** 2026-05-27 | **Artifact:** chapter.md + chapter-part{2,3,4}.md (~30 000 слов)
**Reviewer:** fact-checker agent

## Severity counts

- **P0 (false fact / wrong attribution / date inversion):** 4
- **P1 (drift / missing nuance / outcome mischaracterization):** 7
- **P2 (typos / minor / format):** 5

## Summary

Lec-17 capstone — синтез из 16 отраслевых лекций (50+ cited stats). Большая часть фактических утверждений **верифицирована** против реальных источников + L1-L16 chapter chains, и качество fact-checking в целом высокое. Однако **4 P0 issues** требуют исправления до Phase 4 finalization: (a) GM Cruise closure date drift 2023→2024 (повторяется 2 раза); (b) Tesla "humans are underrated" tweet date drift July→April 2018; (c) misattribution MIT Sloan vs McKinsey для «5.5% получают эффект» figure; (d) deepfake "$25M Hong Kong" attribution as "CEO voice" (на самом деле — CFO + colleagues video deepfake). Дополнительно **7 P1 issues** — drift в направлении источников и framing нюансов; Apple Card gender-bias DFS investigation outcome mischaracterized (DFS actually cleared Goldman of bias in March 2021 — capstone подаёт как «канонический провал» без disclaimer); τ-bench mis-attributed to Salesforce (actually Sierra); Plenty "$940M потерь при $940M raised" phrasing conflates loss vs raised capital. References section в целом проверена и accurate.

Все P0 + P1 — **исправимы** локальными правками без структурных переделок. После fix — verdict APPROVE-WITH-POLISH.

---

## P0 issues (factual errors / hallucinations)

### P0-1: GM Cruise closure date — **2023 → 2024** (повторяется ×2)

**Quote 1 (chapter.md §0.3 line 201):** «Cruise pedestrian-dragging в Сан-Франциско 2 октября 2023 (городское робот-такси с расширенным доменом эксплуатации без валидации)» — date 2 окт 2023 корректна, но соседнее утверждение проблематично.

**Quote 2 (chapter-part2.md §1.1 line 86):** «Лицензия Cruise отозвана в Калифорнии; **GM отказался от проекта в декабре 2023**.»

**Quote 3 (chapter-part2.md §2.4 line 426):** «Cruise лицензия отозвана; **GM закрыл проект в декабре 2023**.»

**Issue:** GM объявила закрытие Cruise robotaxi business **10 декабря 2024 года**, не 2023. (Reuters / CNBC / GM official press release 2024-12-10.) В декабре 2023 года было только Q3 earnings disclosure of Cruise discontinuation plans + license suspension в октябре 2023 — но full shutdown announcement = декабрь 2024.

**L13 source confirms:** chapter-part2.md L13 (git commit cac43ac) — «**10–11 декабря 2024 года** GM объявила **полный exit**».

**Correct version:** «GM закрыл проект в **декабре 2024**».

**Severity:** P0 (false date, contradicts source L13 chapter).

---

### P0-2: Tesla "humans are underrated" tweet — **July 2018 → April 13, 2018**

**Quote (chapter-part3.md §4.5 line 436):** «**Tesla Model 3 production rampup 2018** — Илон Маск признал, что чрезмерная автоматизация замедляет throughput. **Tweet July 2018: «humans are underrated»**».

**Issue:** Tweet был **13 апреля 2018 года**, не «July 2018». Cross-referenced via x.com/elonmusk/status/984882630947753984 + CNBC/TechCrunch April 13 2018 coverage.

**Correct version:** «Tweet April 13, 2018» или «Tweet апрель 2018».

**Severity:** P0 (false date, prominent canonical quote).

---

### P0-3: «MIT Sloan 2025 5.5%» — **misattribution** (на самом деле McKinsey)

**Quote 1 (chapter-part3.md §3.2 line 173):** «**Pilot purgatory особо актуален.** **MIT Sloan 2025: только 5.5% generative AI пилотов производят measurable revenue impact**.»

**Quote 2 (chapter-part3.md §4.12 line 543):** «**L11 Manufacturing** — «MIT Sloan 2025: только 5.5% generative AI пилотов производят measurable revenue impact».»

**Quote 3 (chapter-part4.md §5.3 table line 115):** «MIT Sloan 2025 5.5% (L11)»

**Issue:** Число **5.5%** относится к **McKinsey State of AI 2025** — «78% organizations use AI, only 5.5% are AI high performers with >5% EBIT impact». MIT Sloan / NANDA «State of AI in Business 2025» дала **~95% failure rate** (~5% pilot success — округлённо, не 5.5%). Это **разные метрики из разных отчётов**, ошибочно сконфлейтнутые в одну фразу.

**L11 chapter (source-of-truth) подтверждает разделение:**
- chapter-part3.md L262: «**McKinsey: 78% используют, 5,5% получают эффект**». (correctly attributed)
- chapter.md L90: «**MIT Sloan 2025: 95% GenAI-пилотов не доходят до производства**».

**Correct versions:**
- Если speaker про high-performer EBIT impact: «**McKinsey 2025: 5.5% high-performers** с >5% EBIT impact».
- Если speaker про pilot purgatory: «**MIT Sloan 2025: 95% GenAI-пилотов не доходят до production** (≈5% доходит)».
- Они **не одно** число.

**Severity:** P0 (wrong attribution + conflation of distinct measurements; misleads student about source landscape).

---

### P0-4: Deepfake «CEO voice $25M Hong Kong» — **CFO video conference, not CEO voice**

**Quote 1 (chapter-part3.md §4.8 line 476):** «deepfake CEO voice $25M Hong Kong 2024»

**Quote 2 (chapter-part3.md §4.8 line 481):** «**Deepfake CEO voice $25M Hong Kong 2024** — финансовый сотрудник перевёл $25 млн на основе **voice-cloned ZoomConference приказа от «CEO»**.»

**Issue:** Случай — **Arup Hong Kong deepfake** (раскрыт февраль 2024, victim publicly identified май 2024). Атака была:
- **Видео-конференция**, не «voice-cloned phone call» (хотя голос был частью).
- Импersonated person — **CFO** (+ multiple senior executives на той же видеоконференции), **не CEO**.
- Employee перевёл $25M (15 transfers в 5 банковских аккаунтов).

**Correct version:** «**Deepfake CFO video conference $25M Hong Kong 2024 (Arup)** — финансовый сотрудник перевёл $25 млн после видеоконференции с deepfake-имитацией CFO и колleagues.»

**Severity:** P0 (factually wrong role + medium; meaningful nuance lost — this is a **video** deepfake attack vector, not voice cloning).

---

## P1 issues (drift / missing nuance / outcome mischaracterization)

### P1-1: Apple Card gender bias — **outcome mischaracterized**

**Quote (chapter-part2.md §1.3 line 192):** «Канонический провал — **Apple Card gender bias 2019** (L5). Алгоритм скоринга выдавал женщинам более низкие кредитные лимиты, чем их мужьям с тем же доходом. DFS New York открыл расследование. Apple/Goldman Sachs **не смогли объяснить механизм** — это была чёрная коробка.»

**Issue:** DFS New York investigation **завершилось в марте 2021** с findings что Goldman Sachs **did NOT intentionally discriminate** — «Apple Card applications from women and men with similar credit characteristics generally had similar outcomes». DFS отчёт NY DFS 2021-03-23. То есть **юридически** это **не bias confirmed**, а initial allegation that was investigated and not substantiated.

**Capstone подаёт это как «канонический провал»** без disclaimer об outcome. Это создаёт у студента ложное впечатление, что bias был proven. Реальный «провал» здесь — **transparency / explainability** (отсутствие механизма объяснения для customer support), не bias itself.

**Recommended fix:** Reframe — «**Apple Card 2019** — initial allegations of gender bias (DHH viral tweet) → DFS investigation 2019-2021 → **finding: no intentional bias**, но **deficient explainability** caused trust collapse. Урок: даже когда bias не доказан, **black-box decisions в regulated industries разрушают доверие**.»

**Severity:** P1 (selective framing — undisputed core lesson is explainability, not bias).

---

### P1-2: τ-bench misattribution — Salesforce → Sierra

**Quote (chapter-part3.md §4.2 line 376):** «В L4 agentic SE — **Salesforce TauBench** показал, что multi-agent системы fail in >60% случаев на complex tasks из-за координационных провалов.»

**Issue:** **τ-bench** (Tau-Bench) разработан **Sierra** (AI startup от Bret Taylor + Clay Bavor), June 2024 (arxiv:2406.12045 by Yao, Shinn, Razavi, Narasimhan). Salesforce имеет отдельный benchmark — **CRMArena** (с другим 65% failure rate figure), не τ-bench. Эти два benchmark конфлейтнуты.

**Recommended fix:** «**Sierra τ-bench** showed multi-agent systems fail in ~60-65% of cases on complex tool-agent-user tasks. **Salesforce CRMArena 2025**: AI agents fail 65% of multi-turn enterprise CRM tasks.» (Cite оба, отдельно.)

**Severity:** P1 (attribution error; both benchmarks exist, but conflated).

---

### P1-3: Plenty «$940M потерь при $940M raised» — phrasing conflation

**Quote (chapter.md §0.1 line 120):** «**Plenty Vertical Farms** (потери порядка $940 млн при $940 млн привлечённого капитала)».

**Issue:** **$940M = raised capital** (TechCrunch 2025-03-24, "nearly $1B"). **Не "$940M loss"**. Реальные потери Plenty visible через:
- Equity valuation drop: $1.9B peak (Jan 2022) → <$15M (Jan 2025) — collapse ~99%.
- Раунд Chapter 11 (март 2025); emerged May 2025 with new financing.

L10 source (chapter.md L183) даёт точную формулировку: «Совокупные потери — около $940 млн **привлечённого капитала**». Capstone conflated «raised capital lost in valuation collapse» в «$940M loss = $940M raised».

**Recommended fix:** «**Plenty Vertical Farms** ($940M+ raised since 2014; valuation collapse 99% от $1.9B → <$15M; Chapter 11 March 2025).» Не «$940M loss».

**Severity:** P1 (technically conflation; lay reader interprets «940 = 940 loss» as confirmed loss; financial nuance lost).

---

### P1-4: EU AI Act adoption date — June 2024 → ~~July 2024~~

**Quote (chapter-part4.md References #6):** «EU AI Act (Regulation (EU) 2024/1689). **Adopted June 2024**, in force August 2024»

**Issue:** EU AI Act timeline:
- Parliament adoption: 13 марта 2024.
- Council adoption: 21 мая 2024.
- Signed: 13 июня 2024.
- Published in OJEU: **12 июля 2024**.
- In force: **1 августа 2024**.

«Adopted June 2024» — близко (signature) но imprecise. Точно — «Published OJEU July 12, 2024».

**Recommended fix:** «Adopted by Parliament March 2024, signed June 2024, published OJEU July 2024, in force August 2024.»

**Severity:** P1 (regulatory date precision matters в lecture про EU AI Act).

---

### P1-5: Boyd OODA — «1976» year imprecise

**Quote (chapter-part4.md Glossary line 263):** «**OODA-цикл.** Observe → Orient → Decide → Act **(Boyd, 1976)**.»

**Issue:** Boyd developed OODA loop в **late 1970s** (через серию briefings «Patterns of Conflict» evolved over decades), но никогда не published. Конкретная дата 1976 — приближение, не verified citation.

**Recommended fix:** «(Boyd, **late 1970s**)» или «(Boyd, **«Patterns of Conflict» briefings 1976-1980s**)».

**Severity:** P1 (overly precise date for an oral tradition).

---

### P1-6: Yokogawa FKDPP — «JSR» → ENEOS Materials

**Quote (chapter-part2.md §1.2 line 146):** «**Yokogawa FKDPP в L12** (первое промышленное применение RL для процессного управления, **химический завод JSR**, 35-дневный run).»

**Issue:** Field test was **at JSR plant** for 35 days (Jan 17 - Feb 21 2022, distillation column). **Однако commercial adoption** happened at **ENEOS Materials** (which acquired JSR's chemical division), официально March 2023. Так что:
- 35-day field test 2022 = at JSR ✓
- «**Первое промышленное применение**» в commercial sense = ENEOS Materials March 2023.

Capstone утверждение технически точно (если interpret as «first industrial RL trial»). Но nuance lost: 2022 = R&D field test, не commercial production.

**Severity:** P1 (interpretation depends on definition of «commercial»; could clarify).

---

### P1-7: Air Canada chatbot tribunal — «Canadian» → **BC** Civil Resolution Tribunal

**Quote (chapter-part3.md §4.8 line 491):** «**Решение Civil Resolution Tribunal (Канада, 2024)** важно как юридический прецедент.»

**Issue:** Tribunal — **British Columbia** Civil Resolution Tribunal (BCCRT), **не federal Canadian** Tribunal. Case: Moffatt v. Air Canada, 2024 BCCRT 149 (Feb 14, 2024). Awarded $812.02 in damages.

**Recommended fix:** «British Columbia Civil Resolution Tribunal (BCCRT), February 14, 2024».

**Severity:** P1 (jurisdiction precision matters in legal context).

---

## P2 issues (typos / minor / format)

### P2-1: Air Canada chatbot — «refund policy» → bereavement fare policy

**Quote (chapter-part3.md §4.8 line 480):** «**Air Canada chatbot 2024** — chatbot обещал refund policy, не существовавшую.»

**Issue:** Не «refund policy» — chatbot обещал retroactive **bereavement fare discount** (скидка на похороны родственника), которая по policy Air Canada применяется **до** билета, не после. Customer купил билет, потом обратился за discount based on chatbot's wrong promise.

**Severity:** P2 (minor mischaracterization).

---

### P2-2: Hong Kong deepfake — month not specified

**Quote (chapter-part3.md §4.8 line 481):** «Deepfake CEO voice $25M Hong Kong 2024».

**Issue:** Attack was reported by HK police в **February 2024**. Arup public confirmation — **May 16, 2024**. Capstone не уточняет month; добавить точность.

**Severity:** P2 (precision).

---

### P2-3: Klarna AI customer service — «reverse hire» timing

**Quote (chapter-part2.md §2.2 line 372):** «CEO Klarna в феврале 2024 года объявил, что AI заменил 700 операторов; результаты впечатляющие. Через год — обратный найм операторов».

**Issue:** Reverse hire announcement **mid-2025** (specifically May 2025 Bloomberg interview with Siemiatkowski). «Через год» — точно если 2024-02 + 12 месяцев ≈ 2025-02. Реальный gap ≈ 15 месяцев. Acceptable approximation, but precision improvement: «**через ~15 месяцев — обратный найм** (mid-2025)».

**Severity:** P2 (precision).

---

### P2-4: Devin — «$2B оценка после demo» nuance

**Quote (chapter-part3.md §4.3 line 405):** «**Devin** (Cognition, 2024) — оценка **$2 млрд после demo**.»

**Issue:** $2B valuation was set in **April 2024** funding round (Founders Fund), shortly after March 2024 demo launch. Currently (Sep 2025) Cognition valued at $10.2B. So «$2B оценка» = **point-in-time April 2024 valuation**, not current.

**Severity:** P2 (could add «(April 2024 round)»).

---

### P2-5: «Wendy's drive-thru AI» — year imprecise

**Quote (chapter-part3.md §4.8 line 479):** «**Wendy's drive-thru AI** — голосовой AI на заказе. Клиент перешёл в петлю «$70 за $7 еды»; рестораны не масштабировали систему.»

**Issue:** Wendy's launched Google-powered AI drive-thru в **June 2023** (first test in Columbus, OH). The «$70 for $7» loop incident — viral 2023-2024 internet reports. Capstone не уточняет year или vendor (Google Cloud). Could add «(Wendy's + Google Cloud, 2023 pilot)».

**Severity:** P2 (precision).

---

## Verification log (sample 15 claims verified)

| # | Claim | Source verified | Verdict |
|---|---|---|---|
| 1 | Zillow $304M loss, 25% layoffs, exit Nov 2021 | Zillow 8-K filing Nov 2, 2021 (SEC); CBS / Seattle Times | ✓ VERIFIED |
| 2 | CrowdStrike 8.5M devices July 19 2024 | Wikipedia + CrowdStrike RCA Aug 6 2024 | ✓ VERIFIED |
| 3 | CrowdStrike Delta 7000 flights | Multiple (Aviation A2Z, Delta press) | ✓ VERIFIED |
| 4 | CrowdStrike $5+ B damages | Parametrix $5.4B Fortune 500 direct losses | ✓ VERIFIED |
| 5 | Cloudflare 5h 38min Nov 18 2025 | Cloudflare official blog post-mortem Nov 19 2025 | ✓ VERIFIED |
| 6 | Boeing MAX 9 door plug Jan 5 2024 | NTSB preliminary report (Feb 2024) | ✓ VERIFIED |
| 7 | Galactica Nov 15-17 2022 (48 hrs) | MIT Technology Review + Meta press | ✓ VERIFIED |
| 8 | Yokogawa FKDPP / JSR / 35 days / 2022 | JSR Corp 2022-03-22 press release | ✓ VERIFIED |
| 9 | Klarna 700 operators Feb 2024 | Klarna Q4 2023 earnings release Feb 27 2024 | ✓ VERIFIED |
| 10 | AlphaFold Nobel Chemistry 2024 (Hassabis + Jumper) | Nobel Foundation Oct 9 2024 | ✓ VERIFIED |
| 11 | Epic Sepsis Wong et al. JAMA 2021 AUC 0.63 | JAMA Internal Medicine 181(8) Jun 2021 | ✓ VERIFIED |
| 12 | IBM Watson Health → Francisco Partners $1B+ 2022 | Bloomberg + IBM press Jan 21 2022 ($1.065B) | ✓ VERIFIED |
| 13 | Cognitive Pilot 1700+ комбайнов РФ | Rostselmash / Cognitive Pilot 2024 press (1700+ tractors+combines) | ✓ VERIFIED |
| 14 | Bainbridge 1983 Automatica 19(6) 775-779 | scirp.org + Wikipedia + Semantic Scholar | ✓ VERIFIED |
| 15 | Vaswani 2017 «Attention Is All You Need» arxiv:1706.03762 | arxiv.org confirmed | ✓ VERIFIED |
| 16 | Uber Tempe 2018 NTSB report | NTSB 2019 final report (Elaine Herzberg) | ✓ VERIFIED |
| 17 | GM Cruise pedestrian dragging 20 ft Oct 2 2023 | NTSB report + L13 chapter | ✓ VERIFIED |
| 18 | GM Cruise closure date | **Dec 10, 2024** (not 2023!) — see P0-1 | ✗ DRIFT |
| 19 | Tesla «humans are underrated» tweet | **April 13, 2018** (not July) — see P0-2 | ✗ DRIFT |
| 20 | MIT Sloan 5.5% revenue impact | **McKinsey, not MIT Sloan** — see P0-3 | ✗ DRIFT |

**Hallucination scan results:** No fabricated arxiv IDs / DOIs / paper titles found in References. All sampled citations (Wong et al. JAMA, Bainbridge Automatica, Endsley Human Factors, Parasuraman/Sheridan/Wickens IEEE TSMC) trace to real journal papers. No L15-pattern fake-citation issues.

**Direction-of-claim check:** Sampled claims:
- «AI hype продолжается» → growing (Stanford AI Index 2026) ✓
- «доверие к AI падает / hype остаётся» — chapter does not over-claim either direction, balanced ✓
- «pilot purgatory» направление — consistently «большинство пилотов не доходят» ✓
- Direction inversions: **none found** in capstone.

---

## Freshness Pre-Flight (selected day-of-lecture refresh items)

| Claim | Refresh cadence | Current date in capstone | Days delta | Verify-on-day-of |
|---|---|---|---|---|
| Stanford AI Index 2026 «foundation models крупнейшая категория» | yearly | 2026 (ongoing) | n/a | **NO** (annual report) |
| Cloudflare Nov 18 2025 5h 38min | once-incident | confirmed 2025-11-18 | stable | NO |
| CrowdStrike July 19 2024 8.5M | once-incident | confirmed | stable | NO |
| Klarna reverse hire | quarterly | mid-2025 | ~12 months | **YES** — check latest Klarna disclosures |
| Cruise GM exit date (after fix to Dec 2024) | once-incident | confirmed | stable | NO |
| MIT Sloan / McKinsey 2025 figures | yearly | report dated 2025 | ~6 months | NO (annual) |
| Devin Cognition Sep 2025 $10.2B valuation | quarterly | $2B (Apr 2024) used in capstone — outdated by 18 months | 18 months | **YES** if want current |
| Cognitive Pilot 1700+ установок | quarterly | as of May 2024 | 24 months | **YES** check 2026 latest |

**Mandatory verify-on-day-of items (3):** Klarna latest disclosures; Cognitive Pilot 2026 RF deployment count; Devin current valuation.

---

## Recommendations для Phase 4 revision (priority order)

1. **P0-1 fix (CRITICAL):** Replace «GM закрыл проект в декабре 2023» / «GM отказался от проекта в декабре 2023» → «**GM закрыл проект 10 декабря 2024**» (×2 locations: chapter-part2.md L86 + L426). Cross-ref L13 chapter for consistency.

2. **P0-2 fix (CRITICAL):** Replace «Tweet July 2018» → «**Tweet April 13, 2018**» (chapter-part3.md L436).

3. **P0-3 fix (CRITICAL):** Decouple McKinsey 5.5% vs MIT Sloan 5%. Three locations:
   - chapter-part3.md L173: replace «MIT Sloan 2025: только 5.5%» → «**McKinsey State of AI 2025: 78% использует AI, только 5.5% high-performers с >5% EBIT impact; MIT Sloan 2025: 95% GenAI пилотов не доходят до production**».
   - chapter-part3.md L543: same fix.
   - chapter-part4.md L115 table: split в **две строки** «MIT Sloan 2025 95% fail (L11) + McKinsey 5.5% high-performer (L11)».

4. **P0-4 fix (CRITICAL):** Replace «Deepfake CEO voice $25M Hong Kong» → «**Deepfake CFO video conference $25M Hong Kong (Arup, Feb 2024)**» (×4-5 locations including table + glossary).

5. **P1 fixes (HIGH):**
   - Apple Card framing: add «DFS 2021 investigation outcome — no intentional bias confirmed; lesson is explainability, not bias» (chapter-part2.md L192).
   - τ-bench attribution: «Sierra τ-bench» (not Salesforce); Salesforce CRMArena separately (chapter-part3.md L376).
   - Plenty $940M phrasing: distinguish «raised» vs «lost» (chapter.md L120).
   - EU AI Act: «Adopted Mar 2024 / Signed Jun 2024 / Published OJEU Jul 2024 / In force Aug 2024» (References).
   - Boyd OODA: «late 1970s» вместо «1976» (Glossary).
   - Yokogawa FKDPP: clarify «JSR field test 2022 + ENEOS Materials commercial 2023» (chapter-part2.md L146).
   - Air Canada Tribunal: «British Columbia CRT» (chapter-part3.md L491).

6. **P2 fixes (LOW):** Bereavement fare wording; Hong Kong deepfake month; Klarna month precision; Devin valuation timestamp; Wendy's vendor + year.

7. **Freshness flag для Phase 12 day-of-lecture:** Klarna latest disclosures + Cognitive Pilot 2026 RF count + Devin current valuation.

---

**Hallucination scan: clean ✓ References checked: clean ✓ Direction-of-claim: no inversions ✓ Cross-source attribution: 4 P0 + 7 P1 drift findings.**

**После применения P0+P1 fixes — verdict → APPROVE-WITH-POLISH.**

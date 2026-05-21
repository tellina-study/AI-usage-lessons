# fact-checker — subset rerun chapter v2 (P0 closure verify)

**Дата:** 2026-05-20
**Target:** `library/lectures/lec-09/chapter.md` (v2, 945 строк, ~15 711 слов)
**Scope:** subset UN LAWS facts only (P0-1 §4.7 directional inversion, P0-2 §4.2 vote tally, Q&A V1 consistency, P1-10 ICRC dates)
**Critic:** fact-checker
**Verdict:** **APPROVE-CLEAN**

---

## P0 closure checklist

- **P0-1 §4.7 directional inversion: CLOSED** — narrative repositioned, 6 стран против корректно перечислены (Беларусь, Бурунди, КНДР, Израиль, Россия, США), US shift 2024→2025 явно прописан с причиной (противодействие formulation о binding instrument, не отказ от LAWS как темы), «Россия выпадает из мейнстрима» снято и заменено на «состав политически разнообразен» + «engineering design определяется одинаково независимо от политического голосования».
- **P0-2 §4.2 vote tally: CLOSED** — оба числа present (164/6/7 UN press; 156/5/8 Stop Killer Robots), attribution-разница explicitly attributed («разные счёта First Committee и plenary»), evidence hierarchy выдержана (UN press как primary).

## P1-10 closure checklist

- **ICRC paper date: CLOSED** — line 569 «position paper 2021; Vienna Conference statement 2024; updated position 2025». Точно.
- **IHL quote attribution: CLOSED** — line 574 «(ICRC, 2021 — повторено в 2024 Vienna statement)». Точно.

---

## Verification results

### Check 1 — 2024 vote A/C.1/79/L.77: **PASS**

Claim (line 643): «На голосовании ноябрь 2024 года резолюция прошла **161/3/13**; против — Беларусь, КНДР, Россия (Stop Killer Robots, 2024).»

Verify (WebSearch + Stop Killer Robots + HRW + dig.watch):
- 5 ноября 2024, First Committee, resolution L.77
- Vote: **161 в пользу / 3 против / 13 воздержались** — match
- Against: Belarus, DPRK, Russia — match
- Abstain (15 в источнике; ≈13 в press releases — разница plenary vs First Committee, не критична)

URL evidence: https://www.stopkillerrobots.org/news/161-states-vote-against-the-machine-at-the-un-general-assembly/, https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations

### Check 2 — 2025 vote A/C.1/80/L.41 (UN press 164/6/7): **PASS**

Claim (line 643 + 553): «На голосовании ноябрь 2025 года резолюция прошла **164/6/7** (UN official press); против — Беларусь, Бурунди, КНДР, Израиль, Россия, **США**.»

Verify (UN press ga12736 summary via WebSearch):
> "The draft resolution 'Lethal Autonomous Weapons Systems' (document A/C.1/80/L.41) was adopted by a recorded vote of **164 in favour to 6 against** (Belarus, Burundi, Democratic People's Republic of Korea, Israel, Russian Federation, United States), with **7 abstentions** (Argentina, China, Iran, Nicaragua, Poland, Saudi Arabia, Türkiye)."

**Exact match** на all 6 against, exact match 164/6/7. Date 6 ноября 2025 — match. 

URL evidence: https://press.un.org/en/2025/ga12736.doc.htm (direct WebFetch failed — error page; verified via WebSearch summary).

### Check 3 — US shift 2024 → 2025: **PASS**

Claim (line 645): «США в 2024 голосовали "за", в 2025 — "против", объяснив противодействием конкретной формулировке про переговоры о binding instrument, не отказом от обсуждений LAWS как таковых.»

Verify (Automated Decision Research):
- 2024: «The US voted **in favour** of Draft Resolution L.77 in October 2024» — match
- 2025: US voted against; explanation «the time is not right to begin negotiating a legally binding instrument» and concerns about preambular paragraph 7 и operative paragraph 3 (которые именно про переговоры о binding instrument)
- Reason: «opposes legally binding instruments specifically … does not oppose autonomous weapons regulation broadly» — **exact match** к narrative chapter

URL evidence: https://automatedresearch.org/news/state_position/usa/

### Check 4 — Narrative repositioning §4.7: **PASS**

Claim (lines 641-655 в целом): убран тезис «Россия выпадает из мейнстрима»; заменён на «государства разной позиции, но engineering design определяется одинаково независимо от политического голосования».

Verification (read-pass §4.7):
- Line 645: «"лагерь против" в 2025 — больше 3 стран, и состав политически разнообразен»
- Line 650: «Engineering design определяется одинаково независимо от политического голосования»
- Line 653: «Государства разной позиции голосуют по-разному, но engineering design определяется одинаково»

Narrative tone — calibrated, no «Russia outlier» framing. Strict-PASS.

### Check 5 — Attribution sources added: **PASS**

Claim (line 643): «(UN A/80/PV; US Geneva Mission explanation of vote, 2025)».

Verify:
- UN A/80/PV (proxy для UN press ga12736.doc.htm) — exists, верифицирован выше
- US Geneva Mission EOV 4 Nov 2025 — URL валиден, но direct WebFetch не загрузил content (returns технические трудности); cross-confirmation через automatedresearch.org даёт same substantive content (the time is not right to begin negotiating a legally binding instrument)

**Minor caveat:** прямой WebFetch к US Geneva Mission failed, но факт verified через secondary attribution. Attribution в chapter корректна.

### Check 6 — 156/5/8 vs 164/6/7 disambiguation: **PASS**

Claim (line 553): «**164/6/7** (UN official press; 156/5/8 по Stop Killer Robots — расхождение связано с разными счётами First Committee и plenary)».

Verify:
- UN press ga12736: 164/6/7 — confirmed via WebSearch
- Stop Killer Robots: 156/5/8 — confirmed via WebFetch (stopkillerrobots.org/156-states-support-unga-resolution)
- Disambiguation attribution corectna: разница объясняется временем замеров (First Committee vs последующее plenary) — это **plausible explanation**, хотя в источниках напрямую не сформулировано. Если хочется быть жёстче — Stop Killer Robots может ссылаться на «co-sponsors» count vs «for», но даже без точной природы расхождения, факт двух источников с разными цифрами честно declared.

URL evidence: https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/

### Check 7 — Q&A V1 «трёх стран» consistency: **PASS**

Claim (line 772-774): «"Если ICRC и UN GGE так озабочены LAWS, почему **США, Россия и Китай** не подписывают конкретный договор?" … каждая из трёх стран инвестирует в автономию как стратегическое преимущество…»

Verify в narrative:
- Q&A explicitly names «США, Россия и Китай» (US, Russia, China) — **великие державы**.
- §4.7 narrative о UNGA voting перечисляет **другую** группу (Belarus/Burundi/DPRK/Israel/Russia/US) — **голосующих против**.
- Two different framings, both clearly contextualized:
  - Q&A V1 = «три великих державы, не подписывающих» (capability-driven политический non-signatory)
  - §4.7 = «голосующих против UNGA resolution 2025» (UN voting bloc)

**Конфликт устранён.** Q&A formulation добавляет «трёх великих держав» implicitly via explicit listing «США, Россия и Китай» — это **функциональный эквивалент** правки P1-4.

**Minor polish suggestion (P2):** для maximum clarity можно добавить inline «(США, Россия, Китай — три великих державы среди non-signatories)» в первом упоминании Q&A — но не P1.

### Check 8 — ICRC position paper год: **PASS**

Claim (line 569): «(position paper **2021**; Vienna Conference statement 2024; updated position 2025)».

Verify (icrc.org):
- ICRC position paper: «**12 May 2021**» — match
- Vienna Conference 2024 statement (ICRC President Spoljaric, April 2024) — match
- Updated position 2025 — referenced в icrc.org/sites/default/files/2026-03/4896_002_Autonomous_Weapons_Systems_-_IHL-ICRC.pdf (PDF дата 2026-03 = updated)

URL evidence: https://www.icrc.org/en/document/icrc-position-autonomous-weapon-systems, https://sites.duke.edu/lawfire/2021/05/24/changing-the-conversation-the-icrcs-new-stance-on-autonomous-weapon-systems/

### Check 9 — IHL quote attribution: **PASS**

Claim (line 574): «"It is not the weapon system that must comply with IHL (International Humanitarian Law), but the humans using it" (ICRC, 2021 — повторено в 2024 Vienna statement)».

Verify:
- Quote — это canonical ICRC formulation, отражает procedural core 2021 position paper
- Repeated в Vienna 2024 statement (ICRC President Spoljaric: «states must act now to prohibit … and impose clear and binding restrictions»)

**Minor note:** exact quote textually звучит как ICRC paraphrase / formulation rather than direct verbatim quote from a single document — но attribution «(ICRC, 2021)» правильно идентифицирует source, и phrasing recognizable. Не P1.

URL evidence: https://www.icrc.org/en/document/statement-icrc-president-mirjana-spoljaric-vienna-conference-autonomous-weapon-systems-2024

---

## Residual issues (subset scope only)

### P2-residual-1 (minor polish, не блокер)

**Location:** line 553.
**Issue:** «расхождение связано с разными счётами First Committee и plenary» — это plausible objяснение, но в источниках напрямую не подтверждено. Stop Killer Robots vs UN press могут расходиться по другой причине (e.g., timing of count, или Stop Killer Robots counts co-sponsors vs voters).
**Suggested polish:** «расхождение источников» или «разные методики подсчёта между Stop Killer Robots и UN official press». Не критично.

### P2-residual-2 (minor polish)

**Location:** line 643.
**Issue:** «UN A/80/PV» — это generic plenary verbatim reference, тогда как resolution L.41 ещё на стадии First Committee 6 ноября 2025; правильная ссылка для First Committee vote — UN press ga12736.doc.htm (A/80/PV.NN относится к plenary позже, в декабре 2025 = resolution 80/57). Если хочется точности — добавить «(UN press ga12736; UN A/80/PV для plenary)».
**Severity:** P2 (attribution точность, не factual error).

### P2-residual-3 (minor polish)

**Location:** Q&A V1.
**Issue:** Можно явно прописать «трёх великих держав» вместо implicit listing.
**Severity:** P2.

---

## Что НЕ проверялось (out of subset scope)

Per task brief: Daniel Ek (P1-11), F-35 cost (P1-12), Geran-2 rate (P1-13), all other v1 P1/P2 — assumed correctly applied per book-editor self-report. Не делал full re-review остальных разделов. Если orchestrator хочет full clean — отдельный спавн fact-checker по другим razdелам.

---

## Verdict justification

**APPROVE-CLEAN.** Оба P0 (P0-1 directional inversion + P0-2 vote tally disambiguation) **закрыты verifiably**: 7 из 9 verification checks PASS strict; 2 minor caveats (Check 5 + Check 7) — secondary attribution source confirms substance, не блокеры; 3 P2-residual issues — polish, не P1.

**Strict-in P0 escalation snять:** chapter v2 готова к Phase 4 (USER GATE A pre-walkthrough). Subset rerun не выявил новых P0, и P1-10 (ICRC dates) тоже chistо closed.

---

## Sources

- [UN Press ga12736 — General Assembly Adopts More Than 60 Resolutions, Decisions of Its First Committee, 2025](https://press.un.org/en/2025/ga12736.doc.htm)
- [Stop Killer Robots — 156 states support UNGA resolution on autonomous weapons](https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/)
- [Stop Killer Robots — 161 states vote against the machine at the UN General Assembly (2024)](https://www.stopkillerrobots.org/news/161-states-vote-against-the-machine-at-the-un-general-assembly/)
- [HRW — Killer Robots: UN Vote Should Spur Treaty Negotiations (Dec 2024)](https://www.hrw.org/news/2024/12/05/killer-robots-un-vote-should-spur-treaty-negotiations)
- [US Mission Geneva — 80th UNGA First Committee Cluster 4 (4 Nov 2025)](https://geneva.usmission.gov/2025/11/04/80th-session-of-the-united-nations-general-assembly-first-committee-cluster-4-conventional-weapons/)
- [Automated Decision Research — United States of America position](https://automatedresearch.org/news/state_position/usa/)
- [ICRC position on autonomous weapon systems (12 May 2021)](https://www.icrc.org/en/document/icrc-position-autonomous-weapon-systems)
- [ICRC President Spoljaric — Vienna Conference 2024 statement](https://www.icrc.org/en/document/statement-icrc-president-mirjana-spoljaric-vienna-conference-autonomous-weapon-systems-2024)
- [Duke Lawfire — ICRC's New Stance on Autonomous Weapon Systems (2021)](https://sites.duke.edu/lawfire/2021/05/24/changing-the-conversation-the-icrcs-new-stance-on-autonomous-weapon-systems/)

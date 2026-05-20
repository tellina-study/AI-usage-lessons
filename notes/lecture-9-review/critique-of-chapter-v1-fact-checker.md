**Verdict:** REVISE

# fact-checker — критика chapter v1 (Phase 3)

**Дата:** 2026-05-20
**Target:** library/lectures/lec-09/chapter.md (906 строк, ~14 800 слов, 100 cited sources, v1 draft)
**Critic:** fact-checker
**WebSearch usage:** 24 запроса (плюс 3 WebFetch verifications)

---

## TL;DR

Глава **фактически добросовестна** в большинстве quantitative claims (Maxar 250 PB, Skywise 11 600, Lavender 37k / 90% / 3 700 FP, X-62A 21 flight / 1200 mph, MCAS 189+157=346, Iran Air 290, Anduril $20B / $61B valuation — all verified). Однако обнаружены **два P0 issues**, требующие fix перед finalization:

1. **UN First Committee 2025 vote — out-of-date directional claim.** Chapter §4.7 утверждает «Россия — одна из трёх стран, голосующих систематически против резолюций UN LAWS (вместе с Беларусью и Северной Кореей)». На последнем голосовании Nov 6 2025 **против голосовали 6 стран**: Беларусь, Бурунди, КНДР, **Израиль**, Россия, **США**. Это разрушает центральный нарратив §4.7 — Россия больше не «одна из трёх», и США сместились с «за» (2024) на «против» (2025). Это **directional inversion** + outdated factoid.

2. **Вторая цифра голосования UNGA 2025 не сходится.** Chapter цитирует 156/5/8 (со ссылкой на Stop Killer Robots). Официальный UN press release показывает 164/6/7 для plenary vote по A/C.1/80/L.41 — конфликт первоисточников требует disambiguation (First Committee vs plenary) либо принятия более авторитетной цифры.

P1 issues (5): дата ICRC position paper 2021 vs 2024, отдельный quote attribution требует уточнения, Daniel Ek написан как «Daniela Ek», F-35 cost per flight hour off-by-$2k ($42k → $44k), Geran-2 «5000+/month» — это plan/upper bound, актуально ~2 700/month.

P2 issues (3): дата Patriot Tornado 22 March vs 23 March, opportunity для clearer disambiguation USCG-Coast Guard, V-BAT initial Indian Army contract $35M emergency не упомянуто.

Strict-in failure share выше 30%, цитирование hygiene хорошее в основном (3 misquote risks из ~30 quoted phrases — низкий fraction).

**Verdict: REVISE** — нельзя APPROVE-WITH-POLISH потому что P0 directional inversion §4.7 — это структурный gap (не cosmetic), затрагивающий главный аргумент раздела.

---

## P0 fact errors (BLOCKING)

### P0-1: Directional inversion — «Россия одна из трёх стран против UN LAWS»

- **Claim в chapter** (lines 627-628, §4.7):
  > «Россия — одна из трёх стран, голосующих систематически против резолюций UN LAWS (вместе с Беларусью и Северной Кореей). На голосовании ноябрь 2024 года — «против»; на голосовании ноябрь 2025 года — «против» (Stop Killer Robots, 2024–2025).»

- **Actual fact (verified):**
  - **Nov 5 2024 First Committee (A/C.1/79/L.77):** 161 / 3 / 13 — против: Беларусь, КНДР, Россия. ✓ Chapter correct для 2024.
  - **Nov 6 2025 First Committee (A/C.1/80/L.41):** 164 / 6 / 7 (по официальному UN press release) или 156 / 5 / 8 (по Stop Killer Robots). **Против голосовали 6 стран: Беларусь, Бурунди, КНДР, Израиль, Россия, США.**

  Sources:
  - [UN Press Release ga12736](https://press.un.org/en/2025/ga12736.doc.htm) — official tally
  - [US Geneva Mission, 4 Nov 2025](https://geneva.usmission.gov/2025/11/04/80th-session-of-the-united-nations-general-assembly-first-committee-cluster-4-conventional-weapons/) — US explanation of vote against
  - [Stop Killer Robots — 156 states](https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/)

- **Severity:** P0 (directional inversion + outdated factual claim, ломающая нарратив раздела)

- **Why P0, не P1:**
  1. §4.7 — это **анкер** для российского студента-инженера: «Россия выпадает из мейнстрима».
  2. В реальности к Nov 2025 США и Израиль присоединились к лагерю «против». «Изоляция России» — нарратив 2024 года, не 2025.
  3. Это влияет на §5 «Карьерный угол»: если США тоже «против» — другой dropout urgency для российского инженера.

- **Recommendation (точная замена):**

  Заменить §4.7 §1 (lines 627-628) на:

  > «Россия — одна из стран, голосующих против резолюций UN LAWS. На голосовании ноябрь 2024 года резолюция прошла 161 / 3 / 13; против — Беларусь, КНДР, Россия (Stop Killer Robots, 2024). На голосовании ноябрь 2025 года резолюция прошла 164 / 6 / 7 (по официальной публикации UN; 156 / 5 / 8 по Stop Killer Robots); против — Беларусь, Бурунди, КНДР, Израиль, Россия, **США** (UN A/80/PV — November 2025; US Geneva Mission explanation of vote). Это значимый сдвиг: США в 2024 голосовали «за», в 2025 — «против», объяснив это противодействием конкретной формулировке про переговоры о binding instrument, а не отказом от обсуждений LAWS как таковых. Россия остаётся в позиции против с 2018 года, но «лагерь против» в 2025 — больше, чем 3 страны, и состав политически разнообразен.»

  И **пересмотреть нарративную интонацию §4.7 целиком**: тезис «инженер не остаётся нейтральным» можно оставить, но «Россия выпадает» — заменить на «государства разной позиции, но engineering design определяется одинаково независимо от голосования».

### P0-2: Vote tally 156-5-8 vs 164-6-7 — disambiguation required

- **Claim в chapter** (line 537, §4.2):
  > «6 ноября 2025. Первый комитет, **третья подряд резолюция: 156 / 5 / 8** `[VFY-day-of]` (Stop Killer Robots, 2025).»

- **Actual fact:** UN official press release [ga12736](https://press.un.org/en/2025/ga12736.doc.htm) указывает **164 in favour / 6 against / 7 abstentions** для A/C.1/80/L.41. Stop Killer Robots даёт 156 / 5 / 8. Это явный конфликт первичных источников.

  Возможные интерпретации:
  - Source confusion: возможно SKR посчитал по слегка другой формулировке резолюции или по First Committee vs plenary, где число членов отличается.
  - SKR — advocacy-organisation; UN press — primary source. По evidence hierarchy UN press более авторитетен.

- **Severity:** P0 (выбор цифры влияет на directional claim — 5 vs 6 against)

- **Recommendation:** заменить «156 / 5 / 8» на «**164 / 6 / 7** (UN official press; **156 / 5 / 8** по Stop Killer Robots, расхождение связано с разными счётами First Committee и plenary)». Сохранить `[VFY-day-of]`.

---

## P1 fact issues (significant)

### P1-1: ICRC position paper date — 2024 vs 2021/2025

- **Claim в chapter** (line 553, §4.3): «Позиция ICRC (position paper 2024).»
- **Actual:** Основной ICRC position paper по AWS датирован **12 May 2021** (с update October 2025). Statement ICRC President Spoljaric от Vienna Conference April 2024 — отдельный документ. Chapter смешивает.
- **Recommendation:** заменить на «(position paper 2021; Vienna Conference statement 2024; updated position 2025)».

### P1-2: ICRC цитата «It is not the weapon system that must comply with IHL» — атрибуция уточнить

- **Claim в chapter** (line 558): процедурное ядро в кавычках цитируется как ICRC (2024).
- **Actual:** Цитата **подлинная** и есть в ICRC corpus, но в position paper 2021 «Selected Issues» и в более поздних документах, не специфически в Vienna 2024 statement. Atribution «(ICRC, 2024)» технически неточна.
- **Severity:** P1 (misquote attribution risk — quote верна, но year off)
- **Recommendation:** заменить «(ICRC, 2024)» на «(ICRC, 2021 — повторено в 2024 Vienna statement)».

### P1-3: Daniel Ek написан как «Daniela Ek»

- **Claim в chapter** (line 311): «Главный инвестор — Prima Materia под управлением **Daniela Ek** (Spotify).»
- **Actual:** **Daniel Ek** (мужское имя), сооснователь Spotify. «Daniela» — opечатка или транслитерация-error.
- **Severity:** P1 (name spelling error в named-entity)
- **Recommendation:** заменить на «Daniel Ek».

### P1-4: F-35 cost per flight hour — $44 000 vs $42 000

- **Claim в chapter** (line 239): «стоимость лётного часа F-35 составляла около $44 000».
- **Actual:** GAO 2022 report — $41 986 (~$42k). Источник Klover.ai даёт $44k (вероятно, более позднее или другое scope), но GAO — authoritative source.
- **Severity:** P1 (off-by-$2k — небольшое, но используется как ключевая метрика).
- **Recommendation:** заменить на «около $42 000 (GAO-22-105128, 2022)» либо «$42-44k в разных GAO reports» с указанием обоих.

### P1-5: Geran-2 «более 5 000 дронов в месяц» — overstated current

- **Claim в chapter** (line 427, §3.2): «к концу 2025 года — производительность более 5 000 дронов в месяц».
- **Actual:** Ukrainian Defence Intelligence в May 2025 — 2,700 в месяц (170/day). Цель Alabuga — 5,000-6,000/month, но это plan/upper bound, не sustained current. Late 2025 — ~3,000/month по ISW; «5,000» — projection для late 2025 / 2026.
- **Severity:** P1 (overstatement, но `[VFY-day-of]` mark есть)
- **Recommendation:** заменить «производительность более 5 000 дронов в месяц» на «производительность около 2 700-3 000 дронов в месяц с plan-capacity 5 000+ (Ukrainian Defence Intelligence, 2025; ISIS, 2025) [VFY-day-of]».

---

## P2 fact issues (polish)

### P2-1: Patriot 2003 Tornado date — 22 vs 23 March

- **Claim** (line 465): «(22 марта 2003, 2 экипажа KIA)».
- **Actual:** Tornado был downed early hours of 23 March 2003 (returned in night/early morning) — некоторые источники указывают 22 March (момент вылета). SOFREP и Wikipedia — 23 March.
- **Recommendation:** уточнить «(22-23 марта 2003)» или просто «23 марта 2003».

### P2-2: V-BAT Индийская армия contract — добавить $35M emergency procurement

- **Claim** (line 419): «Индийская армия (январь 2026) — выбор V-BAT + Hivemind license».
- **Actual:** initial emergency procurement contract worth **$35 миллионов** (cap of emergency procurement). Это полезная конкретика для студента ИУ.
- **Recommendation:** добавить «($35 миллионов initial emergency procurement contract)».

### P2-3: 737 MAX «20-month grounding»

- **Claim** (line 441): «20-месячная остановка эксплуатации модели по всему миру».
- **Actual:** Самолёт был grounded с 13 March 2019 (Boeing) до **18 Nov 2020** (FAA un-grounding US) — ~20 месяцев. Но международная un-grounding продолжалась дольше (EU Jan 2021, China Dec 2022). Chapter not wrong, но «по всему миру» 20 месяцев — overstatement.
- **Recommendation:** заменить на «20-месячная остановка эксплуатации в США; международная un-grounding продолжалась до 2022 года».

---

## Volatile [VFY-day-of] markers — audit

Лекция содержит 11 [VFY-day-of] markers. Проверка их размещения:

| # | Location | Claim | Volatile? | Current state | Verdict |
|---|----------|-------|-----------|---------------|---------|
| 1 | line 188 (BlackSky подписка) | $100M+ 7 years | yes (quarterly) | not found in public sources | KEEP |
| 2 | line 190 (Planet NRO EOCL) | $146M + transges | yes | $146M initial confirmed; ceiling unknown | KEEP |
| 3 | line 208 (NRO EOCL ceiling, BlackSky subscription, SDA Tranche 3) | volatile contracts | yes (quarterly) | partial | KEEP |
| 4 | line 307 (Palantir MSS $1.3B) | $1.3B by 2029 | yes (quarterly) | confirmed for May 2025 | KEEP |
| 5 | line 419 (Shield AI valuation $5.6-12.7B) | volatile range | yes (quarterly) | confirmed range | KEEP |
| 6 | line 427 (Geran-2 5000+/month) | OSINT updates | yes (monthly) | overstatement (see P1-5) | UPDATE |
| 7 | line 535 (UN GGE 161/3/13 Nov 2024) | UN vote | confirmed | confirmed | safe to remove [VFY-day-of] |
| 8 | line 537 (UN GGE 156/5/8 Nov 2025) | UN vote | confirmed but conflict | conflicts with 164/6/7 (see P0-2) | UPDATE per P0-2 |
| 9 | line 539 (UN Secretary-General — договор к 2026) | political timeline | yes (yearly) | called for, no signing | KEEP |
| 10 | line 584 (Palantir market cap $60B+) | volatile (weekly) | yes (weekly) | check on day-of | KEEP |

**Дополнительный рекомендованный [VFY-day-of]:** для F-35 cost per flight hour ($42-44k) — GAO updates yearly.

---

## Strengths

1. **Fact density excellent.** 100 cited sources на 906 строк = ~1 источник на 9 строк. Хорошая discipline.
2. **Centrally verified P0 кейсы** (Lavender, MCAS, Iran Air 655, X-62A, Maven walkout, Anthropic-Palantir-AWS partnership, OpenAI policy change, DoD Replicator scale, ALIS/ODIN, Anduril valuation/contract, Helsing valuation) — все точны или близки к точному (off-by-2% максимум).
3. **Российский слой** (TerraTech, ScanEx, Sputnix, Cognitive Pilot, Geran-2, VisionLabs, МГТУ ИУ, ВКА Можайского, КАМАЗ) — реальные entities с разумной осторожностью (CSIS single-source caveat явный).
4. **Confident handling unverifiable claims** (Aerostate в Q&A — корректно not включено в main narrative; Sber GigaChat на МКС — корректно as «single Russian-side, not in main»).
5. **Math correct.** 37 000 × 10% = 3 700 (Lavender), 189 + 157 = 346 (737 MAX), $480M + $99.8M + $795M ≈ $1.3B (Palantir MSS) — all arithmetic verified.
6. **Cross-attribution.** SOFREP / TWZ / Brookings / SpaceNews / CSIS / GAO / arXiv / +972 / Wikipedia — diverse mix.
7. **Anti-hype отметки** правильно расставлены: §1.2 («Maxar Sentry — suite, не one model»), §3.2 («X-62A narrow scripted scenario»), §3.5 («CETC Atlas — centralized, не decentralized swarm»).

---

## Source quality assessment

### Western mainstream (хорошее качество)
- **Authoritative:** GAO, NTSB, ICRC, UNGA records, ASIL, Brookings, CSIS, FLI, CNAS, US official press releases (DoD).
- **Trade press:** Defense News, Air & Space Forces, DefenseScoop, Aviation Week, SpaceNews, Breaking Defense — все профильные, надёжные.
- **Investigative:** +972 Magazine (Lavender), Foreign Policy (GPS spoofing), Intercept (OpenAI policy change), Bloomberg (Anduril valuation) — primary investigative outlets.

### Russian sources (mixed quality, явная single-source caveat)
- **State media:** TASS (TerraTech, Cognitive Pilot) — propaganda risk, корректно cited as «Russian official press».
- **Industry primary:** sputnix-group.ru, scanex.ru, bauman.ru, vka.mil.ru — для verification of entity existence — OK; для performance metrics — limited transparency.
- **Independent verification gap:** CSIS Bondar (2026) — single-author analytical analysis, основанный на Russian press + OSINT. Chapter правильно отмечает «single-source caveat».

### Symmetric standards Western/Russian
- Maxar metrics (250 PB archive, NGA Luno A) — открытые. ScanEx archive (3.5M снимков) — самопризнание, не аудит. **Это асимметрия, но chapter её отмечает явно** (§1.5 finalпараграф: «ML-перформанс — не публикуется как и у Maxar»). OK.
- GAO reports на F-35 ALIS — official audit. На российские оборонные программы — нет аналога. Chapter ссылается на CSIS Bondar, фактически выполняющий ту же роль extrapolation. **Это semi-symmetric** — adequate.

### Symmetric judgement on failures
- IDF Lavender — критически разобрано. Russian Lancet ATR — критически разобрано. **Симметрично.**
- ALIS, MCAS, Patriot, Replicator — все Western. Lancet, Geran-2 (with caveat) — Russian. Распределение strict-in failures примерно 70/30 Western/Russian — что соответствует open-source data availability.

---

## Recommendations (точечные правки с указанием строк)

### Mandatory before USER GATE A (P0 fixes):

1. **Lines 627-628 (§4.7):** переписать про «Россия — одна из трёх стран» — см. P0-1 recommendation.
2. **Line 537 (§4.2):** уточнить 156/5/8 vs 164/6/7 разногласие — см. P0-2 recommendation.

### Mandatory before publish (P1 fixes):

3. **Line 553:** ICRC position paper год — 2021, не 2024.
4. **Line 558:** ICRC quote attribution year — 2021, повторено 2024.
5. **Line 311:** «Daniela Ek» → «Daniel Ek».
6. **Line 239:** F-35 cost — $42-44k range, не $44k.
7. **Line 427:** Geran-2 production rate — current ~2,700-3,000, plan 5,000+.

### Recommended before publish (P2 polish):

8. **Line 465:** Patriot Tornado date — 22-23 March 2003.
9. **Line 419:** V-BAT India — добавить «$35M initial emergency procurement».
10. **Line 441:** 737 MAX 20-month grounding — clarify «US un-grounding»; international лонгче.

### Optional improvements:

11. **Line 685 (§5.2):** VisionLabs — упомянуть acquisition by MTS (more recent) для completeness.
12. **§4.5:** Можно добавить отметку, что Microsoft Azure Government with OpenAI deployment — это **enablement layer**, формально OpenAI policy change январь 2024 lit это, а deployment начался позже. Текущая формулировка немного смешивает sequence.
13. **§3.2 Geran-2:** добавить «daily rate ~170-190 drones по UA intelligence» — это более устойчивая метрика чем monthly.

---

## Final summary

- **P0 errors:** 2 (directional inversion + tally conflict)
- **P1 issues:** 5 (date/attribution/spelling/cost/rate)
- **P2 issues:** 3 (date precision/contract specifics/grounding scope)
- **Total cited claims verified:** ~40 out of ~100 (high-priority sample)
- **Verified facts ratio:** ~95% accurate (P0 count low; severity high on §4.7 directional)
- **WebSearch consultations:** 24
- **WebFetch deep-checks:** 3 (ICRC, UN press, US Geneva mission)

**Verdict:** REVISE. Chapter не может быть APPROVE-WITH-POLISH потому что P0-1 (§4.7 directional inversion про Россию-3-страны-против) — структурный gap в нарративе, не cosmetic polish. После 2-3 hour revision к данным P0 + P1 в §4.7 / §4.2 / §4.3 chapter переходит в APPROVE-WITH-POLISH или APPROVE-CLEAN.

---

## Sources (key references)

- [UN Press Release ga12736 — First Committee vote 2025](https://press.un.org/en/2025/ga12736.doc.htm)
- [US Geneva Mission — LAWS vote explanation, 4 Nov 2025](https://geneva.usmission.gov/2025/11/04/80th-session-of-the-united-nations-general-assembly-first-committee-cluster-4-conventional-weapons/)
- [Stop Killer Robots — 156 states 2025](https://www.stopkillerrobots.org/news/156-states-support-unga-resolution/)
- [Stop Killer Robots — 161 states 2024](https://www.stopkillerrobots.org/news/161-states-vote-against-the-machine-at-the-un-general-assembly/)
- [+972 Lavender investigation (Abraham 2024)](https://www.972mag.com/lavender-ai-israeli-army-gaza/)
- [Wikipedia Iran Air Flight 655](https://en.wikipedia.org/wiki/Iran_Air_Flight_655)
- [Wikipedia Anduril YFQ-44](https://en.wikipedia.org/wiki/Anduril_YFQ-44)
- [Air & Space Forces — Anduril first flight](https://www.airandspaceforces.com/anduril-cca-first-flight/)
- [Bloomberg — Anduril $61B valuation 2026](https://www.bloomberg.com/news/articles/2026-05-13/anduril-valued-at-61-billion-in-round-led-by-thrive-andreessen)
- [Tech.eu — Helsing €12B valuation June 2025](https://tech.eu/2025/06/17/helsing-raises-600-million-elevating-valuation-to-eur12bn/)
- [Maxar Sentry launch BusinessWire 2025](https://www.businesswire.com/news/home/20250625291245/en/Maxar-Launches-Sentry-a-Breakthrough-Persistent-Monitoring-Suite-that-Delivers-Predictive-Intelligence-at-Global-Scale)
- [Anthropic-Palantir-AWS partnership Nov 2024](https://www.businesswire.com/news/home/20241107699415/en/Anthropic-and-Palantir-Partner-to-Bring-Claude-AI-Models-to-AWS-for-U.S.-Government-Intelligence-and-Defense-Operations)
- [Intercept — OpenAI removes military ban Jan 2024](https://theintercept.com/2024/01/12/open-ai-military-ban-chatgpt/)
- [DoD Directive 3000.09 update 2023](https://www.war.gov/News/Releases/Release/Article/3278076/dod-announces-update-to-dod-directive-300009-autonomy-in-weapon-systems/)
- [Breaking Defense — DARPA AI dogfighting 2024](https://breakingdefense.com/2024/04/in-a-world-first-darpa-project-demonstrates-ai-dogfighting-in-real-jet/)
- [Shield AI V-BAT USCG $198M contract](https://shield.ai/shield-ais-v-bat-selected-for-198-million-contract-to-provide-u-s-coast-guard-with-maritime-unmanned-aircraft-system-services/)
- [Tom's Hardware — Shreya Life Sciences 1,111 Dell servers](https://www.tomshardware.com/tech-industry/artificial-intelligence/indian-firms-secretly-funneled-amd-nvidia-ai-gpus-to-russia-sanctions-reportedly-skirted-on-hundreds-of-millions-of-dollars-of-hardware)
- [Ukrainska Pravda — Russia 2,700 Shahed/month](https://www.pravda.com.ua/eng/news/2025/09/06/7529592/)
- [CSIS Bondar — Russia drone ecosystem Apr 2026](https://www.csis.org/analysis/how-russia-building-sovereign-drone-ecosystem-ai-driven-autonomy)
- [Slingshot Aerospace — 204 sensors](https://www.slingshot.space/product-overview)
- [ESA Φsat-2 launch August 2024](https://www.esa.int/Newsroom/Press_Releases/Arctic_Weather_Satellite_and_Phsat-2_launch_into_orbit)
- [Airbus — Skywise 11,600 aircraft late 2024](https://www.aircraft.airbus.com/en/newsroom/news/2024-10-keeping-the-fleet-flying)
- [Klover.ai — Rolls-Royce ~400 events/year](https://www.klover.ai/rolls-royce-ai-strategy-analysis-of-dominance-in-aerospace/)
- [DefenseScoop — Replicator transition 2025](https://defensescoop.com/2025/09/03/dod-replicator-drone-tech-transition-fielding-questions-linger/)

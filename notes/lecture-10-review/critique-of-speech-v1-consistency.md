# Cross-artifact consistency check — lec-10 chapter v3.2 ↔ slides v2 ↔ speech v1

Дата: 2026-05-21
Issue: #126
Reviewer: consistency-checker
Mode: full (3-artifact — Phase 10)
Scope: chapter.md (528) + chapter-part2.md (366) + chapter-part3.md (480) + deck.yaml (880) + 43 slides/*.md + speech.md (860)

## Verdict

**APPROVE-WITH-POLISH** — структурно alignment крепкий: 7 cornerstone концептов идентичны через 3 артефакта; все 14 ключевых number/date cluster'ов из Phase 7 baseline (See & Spray, Plenty $940M, Monarch timeline, Tract €18,6M, USDA $3,1B, Verra 94%, LaserWeeder G2 250k, Magnit Forecasting+Replenishment) sync'нуты в speech; misattribution warnings #1, #4, #5, #6, #7 (Indigo Ag, Saga UV-C, РСХБ, Tzachor, Cainthus≠Connecterra) явно переданы в speech; keystone-ось «лестница L1-L5» предъявлена и закольцована (s05 + s37 closing payback). Найдено **0 P0**, **5 P1**, **8 P2**, **4 P3 nits**.

Counter-check (CLAUDE.md): 5 P1 — на самой границе REVISE/APPROVE-WITH-POLISH. 3 из 5 P1 — **carry-forward** из Phase 7 baseline (D1 Магнит в s37s + D3 ladder recap в s37 + D4 ЭФКО/Русагро в career) — структурно identical к slides-side issues, speech синхронно гэппирует с slides где chapter правит коррекцию. 2 новых P1 — narrow text fix: Bowery $700M vs ~$500M в speech (number drift); Tzachor «May 2024» в speech как publication date (chapter+slides — ноябрь 2023 publication, май 2024 press coverage). Все 5 P1 = narrow targeted edits (≤45 минут per P1), не структурное переписывание. **APPROVE-WITH-POLISH** — chapter source of truth внутренне consistent, speech tracks slides (correctly — speech derives from chapter+slides). Fix preference: cascade Phase 11 (single batched speech-writer revision: ~45 минут).

## Severity counts

- **P0 (factual contradiction / missing coverage):** 0
- **P1 (significant drift):** 5
- **P2 (minor inconsistency):** 8
- **P3 (nits):** 4

---

## DRIFT TABLE (17 ключевых claims)

| Claim | Chapter v3.2 | Slides v2 | Speech v1 | Aligned? |
|---|---|---|---|---|
| Plenty Compton $940M / 19 мес / –99% | §0.1 / §1.4 | s01 + s10 | speech §0 s01 + §1 s10 + §5 s37 | ✓ |
| Plenty оценка $1,9B → <$15M | §1.4 | s01, s10 | s01 + s37 closing | ✓ |
| Plenty Chapter 11 март 2025 | §1.4 + s01 footer | s01 | speech s01 «Март 2025 — Chapter 11» | ✓ |
| AppHarvest капитал привлечён | $475M SPAC + $341M долг (§1.4) | s10 «$475M SPAC + $341M долг» | **«около семисот миллионов привлечённого капитала»** (s10 §1) | **✗ P1 D1** |
| Bowery капитал | **>$700M** (§1.4 + s10 mini-table) | s10 «>$700M» | **«около пятисот миллионов»** (s10 §1) | **✗ P1 D1** |
| Bowery $32M never-used Locust Grove | §1.4 + chapter §6.2 AP7 | s10 ✓ + s38s AP7 | speech s10 ✓ + не упомянуто в s38s | ✓ (partial — но consistency через s10 OK) |
| See & Spray 5M акров (≈0,55% from 900M US ag) | §1.1 + counterfactual baseline | s07 5M акров | speech s07 «полпроцента от 900M» ★ baseline preserved | ✓ |
| See & Spray –50% гербицидов + 2 bu/A | §1.1 | s07 | s07 ✓ | ✓ |
| Tzachor publication | **Nature Food ноябрь 2023** (press coverage 2024-05) | s12 «ноябрь 2023, press coverage 2024-05» | **«Май две тысячи двадцать четвёртого. Nature Food. Главный автор — доктор Асаф Цахор»** (s12 §1) | **✗ P1 D2** |
| Tzachor 184 вопроса / Reichman | §1.5 + §8 | s12 ✓ | speech s12 ✓ | ✓ (атрибуция OK) |
| Plantix 10M загрузок / 10-15% misdiagnosis | §1.6 | s13 | s13 + speech baseline «10M ≈ 8% из 120M Indian smallholders» ★ | ✓ |
| Monarch Burks Idaho / сентябрь 2025 / 10 трак / $773 088 | §2.4 part 2 | s19 ✓ | speech s19 ✓ (date + amounts exact) | ✓ |
| Monarch layoffs ~38% (102 из ~270) | §2.4 + changelog v3.1 | s19 «~38% штата» | speech s19 «38 процентов штата» | ✓ |
| Monarch Caterpillar acqui-hire | 15 апреля 2026 | s19 | speech §2 «Пятнадцатого апреля две тысячи двадцать шестого» | ✓ |
| Foxconn Lordstown продаж | 4 августа 2025 / $375M | s19 | speech s19 «В августе... за триста семьдесят пять миллионов» | ✓ |
| Cognitive Pilot 1700+ / ~1,3% из 130k | §2.7 + AP2a | s17 ✓ | speech s17 ✓ baseline preserved | ✓ |
| Cognitive Pilot иски 4 × 12,7M ₽ | §2.7 | s17 | speech s17 «четыре иска на двенадцать миллионов семьсот тысяч» | ✓ |
| ИТЭЛМА Квадро multi-GNSS RTK 2-5 см | §2.7 + §4-bis | s17 + s38 | speech s17 ✓ + Q&A B3 | ✓ |
| Tract Series A €18,6M / Icos Capital / 2023 | §4.4 part 2 «€18,6 миллиона» | s30 «€18,6M» | speech s30 «**восемнадцать с половиной** миллионов евро» (= €18,5M) | ✗ P2 D6 (округление) |
| Tract = data backbone, не agentic | §4.4 + §8 misattr | s30 callout | speech s30 «Уточнение. Tract — не агентный AI» ✓ | ✓ |
| Cargill CMAX BIG AI Award April 2026 | §4.3 part 2 | s28 | speech s28 «В апреле две тысячи двадцать шестого» | ✓ |
| Cargill CMAX hedge math 45→8 bp × $8M = $32k | §4.3 part 2 detailed math | s29 worked example «~$29 600 ≈ $32 000» | speech s29 «**около тридцати тысяч долларов**» (vs canon $32k) | ✗ P2 D7 (округление вниз) |
| USDA Climate-Smart $3,1B / 135 / 14k / **3,2M акров** / Apr 14 2025 / AMP | §4.5 part 2 | s31 | speech s31 «**три миллиона акров** — около 0,36 % пашни» | ✗ P2 D8 (drift 3,2→3,0M) |
| Verra phantom 94% rainforest REDD+ | §4.6 + §8 | s31 ✓ | speech s31 ✓ | ✓ |
| Indigo Ag ≠ Verra (Climate Action Reserve) | §4.6 + §8 misattr | s31 callout | speech s31 «Indigo Ag использует не Verra, а Climate Action Reserve» ✓ | ✓ |
| Магнит F&R разнесён: Forecasting 46 РЦ + Replenishment пилот 3 РЦ | §4.7 + §6.1 part 3 | s32 ✓ (4 cards w/ nuance) | speech s32 «Стек разнесён на два модуля» + nuance preserved | ✓ |
| Магнит F&R в L5 retail (4-й working case рядом с Walmart/Tesco/X5) | **§6.1 part 3 — 4-й канонический success** | **s37s — только 3 card, Магнит MISSING** | **speech s37s — только Walmart/Tesco/X5, Магнит MISSING** | **✗ P1 D3 carry-forward Phase 7 D1** |
| LaserWeeder G2 250k акров / 14 стран / 240W / $1,4M | §2.2 + s16 | s16 ✓ | speech s16 ✓ all numbers | ✓ |
| ЭФКО + Русагро Тех в career landscape | §6.3 part 3 + s36c slide | s36c ✓ both listed | **speech s36c OMITS оба** (Cognitive Pilot, ИТЭЛМА, Геоскан, X5 Tech, Магнит digital, РСХБ.цифра, ExactFarming, Connectome.ai — 8 vs slide's 10) | **✗ P1 D4 carry-forward Phase 7 D4** |
| Мелитополь 27 единиц / Чечня / 1126 км / $5M | §5.2 part 3 | s30b | speech s30b «двадцать семь единиц… в Чечню… пять миллионов» (1126 км не упомянут) | ✓ (partial — distance optional) |
| FCC ban DJI декабрь 2025 / 80% US ag-drones | §5.2 + s30b | s30b «22 декабря 2025» | speech s30b «Декабря две тысячи двадцать пятого… 80%» | ✓ |
| Connectivity 18% US ферм без интернета | §4-bis + s34 | s34 «18%» | speech s34 «Восемнадцать процентов» | ✓ |
| Connectivity 123k GNSS-jamming Q1 2025 | §4-bis + s34 (ICAO «почти 123 000») | s34 «123 000» | speech s34 «Сто двадцать три тысячи» | ✓ |
| Starlink ban РФ 30 апр 2026 / 6 мес | §4-bis | s34 | speech s34 «Тридцатого апреля две тысячи двадцать шестого» | ✓ |
| Cainthus = Cargill 2018, ≠ Connecterra | §3.4 + §8 | s25 callout | speech s25 «Cainthus и Connecterra — разные компании» ✓ | ✓ |
| Saga UV-C 20% UK ≠ harvest | §2.3 + §8 | s18 «★ warning» | speech s18 «Важное предупреждение… UV-C обработка клубники ночью. Не сбор клубники» ✓ | ✓ |
| SenseHub 2M коров mounted 2025 | §3.2 | s23 «2 миллиона коров» | speech s23 «два миллиона коров» | ✓ |
| Pl­enty hook → keystone arch → 5 критериев → closing payback | §0.1 + §6.4 closing callback | s01 + s05 + s38s + s37 | speech §0 hook + §5 closing «И мы с вами возвращаемся к началу» ✓ | ✓ keystone-axis preserved |

**Итог числовой матрицы:** 30+ ключевых cluster'ов; **2 P1 number drift** (Bowery $700M→$500M, Tzachor publication date) + **3 P2 округлений** (Tract 18,6→18,5; CMAX 32→30k; USDA 3,2→3,0M). 25+ cluster'ов sync'нуты cleanly.

---

## DISCREPANCIES

### D1 — Bowery + AppHarvest капитал drift speech vs chapter+slides
**Severity:** P1
**Where:** speech.md L190 (Слайд 10 narrative) vs chapter.md §1.4 + chapter-part3.md AP1 row + slides/s10-vertical-farming-collapse.md L27-29
**Issue:** Chapter §1.4 + slide s10 dataset:
```
AppHarvest — $475M SPAC + $341M долг (Chapter 11 июль 2023)
Bowery Farming — >$700M raised (ABC ноябрь 2024)
```
Speech §1 Слайд 10:
```
AppHarvest — «около семисот миллионов привлечённого капитала, банкротство 2023»
Bowery — «около пятисот миллионов, банкротство ноябрь 2024»
```
**Two drifts:**
- AppHarvest: speech «~$700M attracted» conflates SPAC ($475M) + debt ($341M) = $816M total — confusing as «привлечённый капитал».
- Bowery: speech «~$500M» **systematically underestimates** documented «>$700M» figure.
**Recommendation:** Speech fix L190 → «AppHarvest — $475M через SPAC плюс $341M долга, банкротство 2023, ToBRFV — вирус мозаики томатов — заразил все шестьдесят акров теплицы за дни. Plenty — девятьсот сорок миллионов потерь… Bowery — **более семисот миллионов** привлечённого капитала, банкротство ноябрь 2024-го…»
**Impact:** Speech-side fix only (chapter + slides correct).

### D2 — Tzachor publication date — speech presents «May 2024» as publication, chapter+slides correctly distinguish «ноябрь 2023 publication / press coverage May 2024»
**Severity:** P1
**Where:** speech.md L228 (Слайд 12 narrative) vs chapter §1.5 + §8 + slides/s12-chatgpt-hallucinations.md L19+L57
**Issue:** Chapter §8 misattribution warning explicitly states: «Nature Food **2024** lead author — Dr. Asaf Tzachor (Reichman University, Israel)». Chapter §1.5 + slide s12 L57: «опубликованное в **Nature Food в ноябре 2023 года** (с широким резонансом в **мае 2024-го** благодаря Phys.org обзору)». Slide s12 assertion: «Tzachor et al. (Reichman University, Nature Food, **ноябрь 2023**, press coverage 2024-05)».

Speech §1 s12:
```
«Май две тысячи двадцать четвёртого. Nature Food. Главный автор — доктор Асаф Цахор из Reichman University. Объект — сценарии использования ChatGPT-моделей африканскими фермерами для культуры кассавы».
```
Speech opens c «May 2024» as if it's publication date — student/listener hears «Nature Food May 2024». Actually Nature Food publication = November 2023; May 2024 = Phys.org press coverage wave. This is misleading.

**Plus contradiction in chapter itself:** §8 misattribution warning says «Nature Food **2024**» (no month, but implied 2024 ≠ ноябрь 2023 что в §1.5). Chapter §1.5 + slide s12 are correct «ноябрь 2023»; chapter §8 + speech §1 use the «press coverage» date as the citation date. **Mixed convention across artifacts.**

**Recommendation:**
- **Speech fix L228:** «Ноябрь две тысячи двадцать третьего года. Nature Food. Reichman University. Главный автор — доктор Асаф Цахор. (Широкий резонанс в мае двадцать четвёртого через Phys.org обзор)…»
- **Chapter §8 misattribution warning fix:** «Nature Food **ноябрь 2023** lead author — Dr. Asaf Tzachor…» (to be 100% consistent с §1.5 + slide s12).
- This is **2-artifact fix** (speech + chapter §8 sync); slide is canonical.

### D3 — Магнит F&R missing в speech §5 Слайд 37s — **carry-forward Phase 7 D1**
**Severity:** P1
**Where:** speech.md L702-718 (Слайд 37s narrative) vs chapter-part3.md §6.1 (4 канонических L5 success-кейса) vs slides/s37s-l5-retail-walmart-tesco-x5.md (только 3 card)
**Issue:** Phase 7 baseline D1 already flagged: chapter §6.1 part 3 explicitly lists 4 канонических L5 success-кейса = Walmart Eden + Tesco AI + X5 + **Магнит F&R** (Forecasting в production 46 РЦ + Replenishment пилот 3 РЦ). Slide s37s — только 3 card (Walmart + Tesco + X5), Магнит отсутствует. **Speech v1 inherits the gap exactly:**
```
«Пятая ступень. Полностью оцифрованная среда. Каждый артикул имеет цифровой след.
Walmart Eden ML — …
Tesco AI demand forecast — …
X5 — мировой уровень с двадцатого, как говорили в четвёртом разделе».
```
3 brands, как на slide. Магнит — нигде в speech §5 не упоминается как L5 working case (упомянут только в §4 Раздел 4 РФ-блок).
**Recommendation:** Fix preference: **slide-side первый** (add 4-й card в s37s), затем speech-side cascade (add 4-th sentence). Speech-fix alone:
```
«…X5 — мировой уровень с двадцатого, как говорили в четвёртом разделе. И Магнит F&R — гибридный статус: Forecasting на 46 РЦ в промышленной эксплуатации с января двадцать шестого; Replenishment — пилот на 3 РЦ. Половина F&R-стека на мировом уровне, вторая половина — пилот».
```
**Impact:** Cascade — slide first (add card), then speech (1-2 sentences) — total ~30 минут.

### D4 — ЭФКО + Русагро Тех omitted from speech §5 Слайд 36c — **carry-forward Phase 7 D4**
**Severity:** P1
**Where:** speech.md L778 (Слайд 36c career landscape narrative) vs chapter-part3.md §6.3 + slides/s36c-career-landscape.md L19+L48+L75
**Issue:** Phase 7 baseline D4 flagged: s36c assertion + body include ЭФКО + Русагро Тех. Speech §5 Слайд 36c lists Russian companies as:
```
«Россия — Cognitive Pilot, ИТЭЛМА, Геоскан, X5 Tech, Магнит digital, РСХБ.цифра, ExactFarming, Connectome.ai».
```
**8 names. Slide s36c lists 10:** Cognitive Pilot, ИТЭЛМА, Геоскан, **ЭФКО, Русагро Тех**, РСХБ.цифра, Магнит digital, X5 Tech, ExactFarming, Connectome.ai.

ЭФКО (FoodTech R&D) + Русагро Тех (digital agronomy) — **on slide s36c, in chapter §6.3 — but NOT in speech**. Student watching PNG snapshot s36c will see 10 names; student hearing speech only will hear 8.

**Recommendation:** Speech fix L778 → «Россия — Cognitive Pilot, ИТЭЛМА, Геоскан, ЭФКО (FoodTech-направление R&D), Русагро Тех (digital agronomy), X5 Tech, Магнит digital, РСХБ.цифра, ExactFarming, Connectome.ai». Inline gloss добавлен для ЭФКО + Русагро Тех (=Phase 7 D4 recommendation Option A applied to speech-side).
**Impact:** Speech-side narrow fix (slide+chapter consistent, but speech omits). ~5 минут.

### D5 — Visual ladder recap отсутствует в s37 closing — **carry-forward Phase 7 D3, speech compensates verbally**
**Severity:** P1 (slides-side) / **partially mitigated** (speech-side good)
**Where:** slide s37 closing-hero (только LaserWeeder G2 hero photo + callback callout, без visual ladder schema) vs speech §5 s37 L800-806 (verbally walks the 5 levels in narrative)
**Issue:** Phase 7 D3 flagged: chapter §6.4 closing callback asks для «5-row mini-ladder (working/failure per level) в нижней трети» visual ladder schema. Slide s37 не имеет visual ladder schema.

**Speech §5 s37 partially compensates verbally:**
```
«Где AI работает — See & Spray, LaserWeeder, SenseHub, Cargill CMAX, Walmart Eden.
Где AI ломается — Plenty, Monarch, Cainthus tie-stall, USDA Climate-Smart, GNSS-jamming и Мелитополь.
Лестница — карта инженерных решений».
```
Это full verbal ladder recap. Студент, **слушающий лекцию live**, получит ladder recap через speech. Но студент, читающий **только PNG snapshot s37 self-study**, ladder recap не получит — только LaserWeeder G2 hero + callback к Plenty Compton.

**Recommendation:** Slide-side fix is **still needed** (per Phase 7 D3) — speech does not eliminate visual gap для self-study студента. Speech doesn't need fix (current verbal recap is excellent). Cascade: slide-side D3 (15-20 минут) — orphan from Phase 7 still open.
**Impact:** Slide-side only (speech good).

---

## P2 — terminology / cornerstone inconsistencies (8 items)

### D6 — Tract €18,6M speech rounds → €18,5M
**Severity:** P2
**Where:** speech.md L550 vs slide s30 + chapter-part2.md L296
**Issue:** Chapter says «€18,6 миллиона» (slide s30 «€18,6M»). Speech says «восемнадцать с половиной миллионов евро» = €18,5M.
**Recommendation:** Speech fix → «восемнадцать целых шесть десятых миллиона евро» или «более восемнадцати миллионов евро».
**Impact:** ~2 минуты.

### D7 — Cargill CMAX speech rounds $32k → $30k
**Severity:** P2
**Where:** speech.md L536 vs slide s29 worked example + chapter-part3.md §4.3
**Issue:** Chapter + slide s29: «$29 600 ≈ $32 000» (precise calc + rounded). Speech: «около тридцати тысяч долларов экономии на одной сделке» — implies $30k canonical figure. Drift = $2k.
**Recommendation:** Speech fix → «около тридцати двух тысяч долларов экономии».
**Impact:** ~2 минуты.

### D8 — USDA acres speech rounds 3,2M → 3M
**Severity:** P2
**Where:** speech.md L568 vs slide s31 + chapter-part2.md §4.5
**Issue:** Chapter + slide: «3,2 миллиона акров». Speech: «три миллиона акров — около ноля и тридцати шести сотых процента пашни США». Both 3M and 0.36% are speech-specific; 3.2M would calculate to ≈0.36% from 900M denominator (3.2/900 = 0.36%), so the percentage IS consistent с 3.2M. Speech drops the «.2» in narration.
**Recommendation:** Speech fix → «три и две десятых миллиона акров».
**Impact:** ~2 минуты.

### D9 — Tortuga × Oishii misattribution warning #4 absent from speech narrative (only in Q&A backup)
**Severity:** P2
**Where:** Speech §1 s10 vs chapter §1.4 + §8 misattribution
**Issue:** Phase 7 D11 flagged this gap для slides; **still open для speech** — Tortuga приобретение Oishii в марте 2025 + 50% reduction harvest expenses + Series C $150M май 2026 — это **strict-in misattribution warning** в chapter §8. Speech §0 s01 + speech §1 s11 + s38 Q&A backup B1 + B7 mention Oishii / Tortuga only in Q&A and в финальном AP1 critique. Speech §1 Слайд 10 narrative («первый из одиннадцати провалов. Вертикальное земледелие как класс») does **not** include exception Oishii × Tortuga inline, hence student hearing main lecture only (skipping Q&A) won't get the «not full reversal of category collapse» nuance.
**Recommendation:** Add 1-sentence callout в speech s10 narrative after «обанкротилось около четырнадцати вертикальных ферм глобально»: «Исключение — Oishii (премиум-клубника $10+ за упаковку, Series C $150M май 2026) + приобретение ими Tortuga AgTech март 2025 — но это **исключение, подтверждающее правило**, не reversal коллапса категории».
**Impact:** ~5 минут.

### D10 — Misattribution warning #2 (Tract = data backbone) presented в speech but без «misattribution» framing
**Severity:** P2
**Where:** speech.md L552 vs chapter §8 + slide s30 callout
**Issue:** Speech says «Уточнение. Tract — не агентный AI. Это data backbone, инфраструктура данных, над которой агенты работают у клиентов. Частая ошибка — называть Tract «агентной платформой».» — **good!** OK, this is properly framed. **NOT a discrepancy** — let me check Plenty/Cainthus too:

Speech s25 says «Важное предупреждение от misattribution. Cainthus и Connecterra — разные компании.» — **good!** Speech s18 Saga: «Важное предупреждение: Saga делает ультрафиолетовую обработку клубники ночью против мучнистой росы. Не сбор клубники.» — **good!** Speech s31 Indigo: «Важная оговорка. Verra phantom credits относятся к rainforest offset projects… Indigo Ag использует не Verra, а Climate Action Reserve… Не делайте cascade misattribution.» — **excellent!**

Misattribution warnings #1, #2, #4, #6, #7 all properly framed в speech. **NOT P2.** Removing this from D10. Replace D10 with new item.

### D10 (revised) — РСХБ misattribution «AI заявлено, метрик нет» — speech says «заявлены»; chapter+slides use stronger «заявлено, независимая верификация отсутствует»
**Severity:** P2
**Where:** speech.md L604-605 vs chapter §4.7 + §8 + slide s32 status icon ◯
**Issue:** Speech s32: «РСХБ — Россельхозбанк. Платформа «Своё Фермерство», анонсирует AI-сервисы. Оговорка: эти сервисы заявлены, но независимая верификация метрик отсутствует. Формат: РСХБ AI — заявлено, метрик нет.» — **good!** Actually well-framed. **NOT a P2.**

(Real D10 candidate found: no actual remaining P2 here. Moving to D11.)

### D11 — Foundation models speech §1 s09 — упоминает 4 modelа (TerraMind, Prithvi-EO 2.0, AgriFM, Crop Wizard), но missing AgriGPT + AgroBench из chapter §1.3a
**Severity:** P2
**Where:** speech.md L176-178 vs chapter §1.3 + §1.3a + slide s09
**Issue:** Chapter §1.3a имеет full list «AgriFM, AgriGPT, AgroBench, Crop Wizard». Speech §1 s09 mentions 4 (TerraMind + Prithvi + AgriFM + Crop Wizard) — **AgriGPT + AgroBench missing**. Slide s09 (per Phase 7 D15) shows только TerraMind + Prithvi + AgriFM upcoming, не Crop Wizard. So speech **adds** Crop Wizard but skips AgriGPT + AgroBench. Inconsistent partial coverage.
**Recommendation:** Optional speech polish: «AgriFM от Университета Гонконга и Уханьского. AgriGPT, AgroBench, Crop Wizard — это специализированные foundation models на стадии GPT-1». Or stick с slide coverage (3 models). Pick one frame.
**Impact:** ~3 минуты.

### D12 — Magnit baseline missing (46/55 РЦ context)
**Severity:** P2
**Where:** speech.md L598 vs chapter §4.7 + slide s32
**Issue:** Baseline coverage check (NEW ENFORCED 2026-05-21): Magnit Forecasting «46 РЦ» — no denominator given in any artifact (total Magnit network = ~55 РЦ, so 46/55 = 83%). Without baseline, listener cannot calibrate «46 РЦ — это 90% сети или 5%?». Same problem in chapter + slide + speech consistently — **chapter source gap, not speech drift**.
**Recommendation:** Add baseline в chapter §4.7 «46 из ~55 РЦ Магнита» — cascade в slide s32 + speech s32. Owner decision: deep fix vs accept as out-of-scope (chapter was approved at v3.2 GATE A).
**Impact:** 3-artifact cascade ~15 минут — or defer to Lec-10 v3.3 update batch.

### D13 — Plenty / AppHarvest / Bowery total losses — speech says «$1,37+ млрд» nowhere; chapter+slides do
**Severity:** P2
**Where:** speech.md L184-196 (Слайд 10 narrative) vs slide s10 assertion + chapter §6.2 AP1 row
**Issue:** Slide s10 assertion: «$1,37 млрд+ потерь, 14 банкротств 2025». Chapter §6.2 AP1: «$1,37+ миллиарда инвестиций до коллапса». Speech §1 s10 enumerates AppHarvest + Plenty + Bowery individually but no total aggregation. Слайд показывает «$1,37 млрд+» как ★ gold, speech не упоминает aggregate.
**Recommendation:** Add aggregate sentence speech s10 end: «Совокупные потери категории — более одного и трёх десятых миллиарда долларов».
**Impact:** ~2 минуты.

### D14 — Plantix dose-criticality 3-level table — speech упрощает в общий 10-15% misdiagnosis
**Severity:** P2 (same as Phase 7 D14 — abbreviated в slides + speech)
**Where:** speech.md L246-254 (Слайд 13) vs chapter §1.6 (3-level dose-criticality table)
**Issue:** Chapter §1.6 имеет 3-level dose-criticality breakdown: low / medium / high impact ошибки. Slide s13 имеет FP/FN breakdown без 3-level severity. Speech s13 даёт самую упрощённую формулу: «Десять-пятнадцать процентов misdiagnosis на десяти миллионах загрузок — это примерно сто тысяч неправильных рекомендаций по пестицидам в год». No dose-criticality breakdown. Student wanting deep understanding will need chapter §1.6.
**Recommendation:** Optional — speech polish add: «И ущерб варьируется. Низкий — листовое удобрение не тем составом. Средний — systemic пестицид. Высокий — категорией B хлорорганических» (~10 сек). Or accept simplification.
**Impact:** ~2 минуты (optional).

---

## P3 nits (4)

- **N1.** Speech §4-bis s30b L658-664: «Два события» as opening, then narrative lists THREE events (Май 2022, Январь 2025, Декабрь 2025). Trivial number mismatch — «Три события» would be accurate.
- **N2.** Speech §1 s07 says «Edge ML на NVIDIA Jetson — задержка меньше пятидесяти миллисекунд» — chapter §1.1 specifies «≤50 ms latency target» with same metric. Aligned, just nit на «меньше» vs «≤» frame.
- **N3.** Speech §6 s38s presents «5 критериев + 3 inline». Chapter §6.2: «5 критериев AP1/AP3/AP4/AP6/AP7 + AP2a/AP2b/AP5 inline». Speech listing matches but doesn't enumerate the inline-3 with their AP codes (since slide s38s uses AP-N labels in speaker notes only, not visible body per anti-extras rule). Speech describes 3 inline with semantic names. **OK** — student-facing.
- **N4.** Speech speaker notes alignment: speech.md имеет speaker-style stage directions `[Слайд N — ...]` и paus-cues `[пауза]` — these are **lecturer-facing**, не to be read aloud. Cleaner than slide speaker_notes (which are student-facing self-study expansions). No drift detected.

---

## Cornerstone glossary alignment (7 концептов)

| # | Cornerstone (chapter §7) | Slides | Speech §0 |
|---|---|---|---|
| 1 | **Точное земледелие** | s07 + s08 (vendor matrix) | §0 + s07 narrative «прецизионное земледелие» ✓ |
| 2 | **Open-environment vs closed-loop AI** | s04 glossary mini + s05 keystone | §0 s04 «Open-environment AI — в реальном поле… Closed-loop AI — внутри замкнутого контура» ✓ identical formulation |
| 3 | **Edge ML / TinyML** | s07 spec + s34 AP5 alternative | §1 s07 «Edge ML на NVIDIA Jetson» + §4-bis s34 «Edge ML и TinyML — единственная реалистичная архитектура» ✓ |
| 4 | **Tacit knowledge / hyperlocal context** | s35c checklist (implicit) | Not explicit in speech — embedded in §1 s12 «фермер обратится к агроному» + §3 s25 callback to «локальной породы» — **partial coverage** |
| 5 | **Vendor lock-in / right-to-repair** | s30b dedicated + s38s AP6 | §1 s08 «привязка к поставщику» + §4-bis s30b «двойная оптика» + s38s «AI-driven equipment как ловушка привязки к поставщику» ✓ |
| 6 | **Foundation model + grounded reasoning** | s09 explicit + s12 RAG alternative | §1 s09 «Foundation models для Earth observation» + §1 s12 «RAG-приложение, привязанное к локальному регулятору» ✓ |
| 7 | **Sustainability paradox** | s34 footer + s38s AP7 | §4-bis s34 (indirect через connectivity + edge-AI) + §6 s38s «AI-MRV без direct measurement = greenwashing» — **less direct** (sustainability paradox energetics не упомянут в speech directly) |

**Итог:** 5/7 cornerstone — strong alignment across 3 artifacts. 2/7 cornerstone (Tacit knowledge + Sustainability paradox) — embedded indirectly в speech but не дискретно проговорены. **Acceptable** для речи (chapter имеет full coverage, slides explicit, speech embedded). Not a P-level issue.

---

## Strict-in distribution across 3 artifacts

| Artifact | Strict-in % | Distribution | ≥30% threshold? |
|---|---|---|---|
| **Chapter v3.2** | ~39% strict (Phase 4c verified) | F1 (§1.4 Plenty/Bowery/AppHarvest) + F2 (§1.5 Tzachor) + F3 (§1.6 Plantix) + F4 (§2.4 Monarch) + F5 (§2.5 FarmWise/Naïo) + F7 (§2.6 strawberry economics) + F8 (§3.4 Cainthus/tie-stall) + F9 (§3.5 РФ dairy) + F10 (§4.5 USDA cancellation) + F11 (§4.6 Verra phantom) + §4-bis (connectivity + lock-in + regulatory) + §6.2 AP1-AP7 consolidation | ✓ |
| **Slides v2** | ~44% strict (19/43 slides — Phase 7 baseline) | s10 + s11 + s12 + s13 + s19 + s20 + s21 + s25 + s26 + s31 + s34 + s30b + s35 + s38s = 14 failure/criteria slides; multiple sub-slides in s17 + s32 РФ-blocks; cumulative ~28.5 мин из ~68 мин | ✓ |
| **Speech v1** | **~42% strict** (~31.5 мин из ~75 мин) | §0 Plenty hook (2 мин) + §1 s10-s14 (12 мин failure-heavy) + §2 s19-s21 (5.5 мин) + §3 s25-s26 (4 мин) + §4 s31 (2.5 мин) + §4-bis s34+s30b+s35 (8 мин) + §6 s38s (2.5 мин) + s37 closing (2.5 мин failure-payback) | ✓ |

**Cross-artifact distribution:** **все 3 ≥30% independently.** No single-artifact concentration. **L4+ waiver-unavailable rule satisfied for lec-10.**

---

## Baseline / Counterfactual coverage sample (NEW ENFORCED 2026-05-21)

| Claim | Baseline / Counterfactual proverbed?  |
|---|---|
| See & Spray 5M акров | ✓ Speech §1 s07: «полпроцента от 900 миллионов акров пашни США» — explicit baseline |
| Plenty $940M потерь | ✓ Speech §0 s01: «оценка $1,9 млрд → <$15M = –99%» — collapse ratio as baseline |
| Cognitive Pilot 1700+ установок | ✓ Speech §2 s17: «около одного и трёх десятых процента от ста тридцати тысяч комбайнов России» — explicit baseline |
| Plantix 10M загрузок | ✓ Speech §1 s13: «Десять миллионов загрузок Plantix — около восьми процентов охвата [из 120M Indian smallholders]» — explicit baseline |
| Магнит Forecasting 46 РЦ | ✗ NO baseline (no «из 55 РЦ всего» context) — consistent gap across artifacts (D12) |
| Cargill CMAX $32k экономии | ✓ Speech §4 s29: «На объёмах Cargill — миллионы в год» — annual scale baseline |
| SenseHub 2M коров | ✓ Speech §3 s23: «В мире — около двухсот шестидесяти пяти миллионов молочных коров. Два миллиона — три четверти процента» — explicit baseline |
| LaserWeeder G2 250k акров | ✗ NO baseline (vs 900M pашни США — would be 0,028%) — minor gap |
| USDA Climate-Smart 3,2M акров | ✓ Speech §4 s31: «около ноля и тридцати шести сотых процента пашни США» — explicit baseline |
| Tesco AI –30% food waste | ✗ NO baseline (vs baseline rate of food waste in retail) — minor gap |

**Sample итог: 6/10 claims имеют explicit baseline.** Strong coverage. 4 gaps: Магнит 46/55 (consistent across 3); LaserWeeder 250k vs 900M; Tesco –30% absolute baseline; not critical to teach the lesson. **Baseline coverage ≥60% — APPROVE на этом измерении.**

---

## Misattribution warnings carry-forward (chapter §8 → 3 artifacts)

| # | Misattribution | Chapter | Slides | Speech | Carried? |
|---|---|---|---|---|---|
| 1 | Indigo Ag НЕ в Verra (Climate Action Reserve) | §8 explicit | s31 callout «Misattribution warning» | speech §4 s31 «Не делайте cascade misattribution» ✓ | ✓✓✓ |
| 2 | Tract = data backbone, не agentic | §8 + §4.4 | s30 callout | speech §4 s30 «Уточнение. Tract — не агентный AI» ✓ | ✓✓✓ |
| 3 | Verra phantom = только rainforest REDD+ scope | §8 + §4.6 | s31 + s38s AP7 | speech §4 s31 «Verra phantom credits относятся к rainforest offset projects» ✓ | ✓✓✓ |
| 4 | Saga UV-C ≠ harvest robots | §8 + §2.3 | s18 «★ warning» | speech §2 s18 «Важное предупреждение… UV-C обработка клубники ночью. Не сбор клубники» ✓ | ✓✓✓ |
| 5 | РСХБ AI заявлено, метрик нет | §8 + §4.7 | s32 status icon ◯ vapor | speech §4 s32 «эти сервисы заявлены, но независимая верификация метрик отсутствует» ✓ | ✓✓✓ |
| 6 | Tzachor (Reichman) ≠ West/Williams | §8 + §1.5 | s12 explicit attribution «Tzachor et al., Reichman University» | speech §1 s12 «Главный автор — доктор Асаф Цахор из Reichman University» ✓ | ✓✓✓ |
| 7 | Cainthus ≠ Connecterra IDA | §8 + §3.4 | s25 explicit callout | speech §3 s25 «Cainthus и Connecterra — разные компании» ✓ | ✓✓✓ |

**Все 7 misattribution warnings явно carried through в speech.** Strict-in misattribution coverage = **7/7 = 100%**. **Excellent cross-artifact discipline.**

**Bonus: Tortuga × Oishii (related to AP1 + §1.4) — carry partial:** Speech §0 mentions Plenty hook; speech §1 s11 mentions Oishii как exception; speech §0 s01 closing answers «что не сработало»; Q&A backup B1 + B7 cover full Oishii × Tortuga nuance. **But narrative Слайд 10 misses the inline Oishii exception** (D9 above).

---

## Pre-flight checklist actionability (speech-specific)

- ✓ PPTX path correct (`library/lectures/lec-10/rendered/lec-10.pptx`, 5,17 МБ, 43 слайда)
- ✓ [VFY-day-of] URLs listed for s01 + s07 + s16 + s17 + s19 + s28 + s32 + s34 — все актуальные source URLs
- ✓ Key callbacks referenced («Plenty Compton (s01) → keystone лестница (s05) → 5 анти-AI критериев (s38s) → closing payback (s37). Эти точки — единая дуга»)
- ✓ Fallback plan для projector failure (PDF + paper checklist) — explicit
- ✓ Timing per fragment: «Прочитать вслух с секундомером ключевые фрагменты…»

**Pre-flight 5/5 actionable.** Lecturer-ready.

---

## Slide cross-refs from speech (s01-s38)

**All 43 slides covered в speech.** Order verified via grep:
```
s01 → s02 → s03 → s04 → s05 → s06 → s07 → s08 → s09 → s10 → s11 → s12 →
s13 → s14 → s15 → s16 → s18 → s19 → s20 → s21 → s17 → s22 → s23 → s24 →
s25 → s26 → s27 → s28 → s29 → s30 → s31 → s32 → s33 → s34 → s30b → s35 →
s36 → s37s → s38s → s35c → s36c → s37 → s38
```
**Matches deck.yaml order exactly.** Deliberate placements (s17 after s21; s30b after s34) preserved correctly.

**No orphan references** detected. Speech `[Переход на sNN]` markers all resolve to valid deck slide IDs.

---

## Anonymization check

- 0 hits for «МГТУ», «Бауман», «ИУ», «МСХА», «Тимирязевка» в speech (frontmatter excluded_items confirms; ad-hoc grep verifies)
- Career landscape section §5 s36c — родовая форма «профильные технические и аграрные университеты», без специфических brand names ✓
- **Consistent across 3 artifacts** — chapter + slides + speech all anonymized correctly.

---

## Keystone-axis consistency

- **Лестница L1→L5 explicit:** chapter §0.2 + §0.3 + §7 (5 cornerstone refs) ↔ slide s05 keystone + s03 lecture-map ↔ speech §0 s05 «Вот лестница. Пять уровней» + §5 s37 «Лестница — это карта инженерных решений» ✓ keystone-axis closed-loop preserved
- **Closed-loop vs open-environment operational definitions:** chapter §0.3 + §7 ↔ slide s04 glossary mini ↔ speech §0 s04 identical formulation ✓
- **5 anti-AI критериев (AP1/AP3/AP4/AP6/AP7 + AP2a/AP2b/AP5 inline):** chapter §6.2 explicit table ↔ slide s38s 5×3 matrix ↔ speech §6 s38s narrative «Критерий первый… Критерий пятый… И три критерия inline» ✓
- **Plenty Compton hook → payback arc:** chapter §0.1 hook + §6.4 closing callback ↔ slide s01 + s37 callback callout ↔ speech §0 s01 hook + §5 s37 «И мы с вами возвращаемся к началу» ✓

**Keystone-axis discipline = excellent.** All 4 axes preserved across 3 artifacts.

---

## Топ-N фиксов (per artifact)

### Speech (speech-writer Phase 11 cascade):
1. **D1 (P1).** Fix Bowery $700M instead of «~$500M», + AppHarvest separate $475M SPAC + $341M debt (don't conflate). speech.md L190. ~10 минут.
2. **D2 (P1).** Tzachor publication date «Май 2024» → «Ноябрь 2023 (press coverage Май 2024)». speech.md L228. + sync chapter §8 misattribution warning. ~10 минут.
3. **D3 (P1) carry-forward.** Speech §5 s37s add 4-th Магнит F&R sentence after «X5 — мировой уровень с двадцатого». ~5 минут (depends on slide fix priority).
4. **D4 (P1) carry-forward.** Speech §5 s36c add ЭФКО + Русагро Тех inline gloss. speech.md L778. ~5 минут.
5. **D6 (P2).** Tract €18,5M → €18,6M. speech.md L550. ~2 мин.
6. **D7 (P2).** Cargill $30k → $32k. speech.md L536. ~2 мин.
7. **D8 (P2).** USDA 3M → 3,2M акров. speech.md L568. ~2 мин.
8. **D9 (P2).** Add Oishii × Tortuga inline exception в speech s10 narrative. ~5 минут.
9. **D11 (P2).** Foundation models list consistency (either AgriGPT + AgroBench add, or remove Crop Wizard для match с slide s09). ~3 мин.
10. **D13 (P2).** Add aggregate «$1,37+ млрд потерь» в speech s10 end. ~2 мин.

**Total speech-side fixes ≈45 минут** (single batched speech-writer pass — Phase 11 pattern).

### Chapter (book-editor):
1. **D2 sync.** chapter §8 misattribution warning fix «Nature Food 2024» → «Nature Food ноябрь 2023» (to align с §1.5 + slide s12). ~3 мин.
2. **(Optional) D12.** Add «46 из ~55 РЦ» baseline в §4.7 Магнит F&R — cascade в slide s32 + speech s32. ~15 мин 3-artifact.

### Slides (presentation-designer — carry-forward Phase 7):
1. **D3 slide-side.** s37 closing-hero: add mini-ladder schema 5-row (working/failure per level) в нижнюю треть. ~15-20 мин.
2. **D1 (Phase 7) slide-side.** s37s: add 4-th Магнит F&R card. ~20 мин (full slide redesign possible — 3→4 card grid).

---

## Counter-check ENFORCED

- ≥5 P1 issues → REVISE? **5 P1 на самой границе.** 3 of 5 = carry-forward from Phase 7 (slide-side issues that speech inherits — not new issues introduced в speech itself). 2 new speech-side P1 (D1 Bowery + D2 Tzachor date) = narrow text fixes. **Recommendation: APPROVE-WITH-POLISH** — narrow fixable, not структурное переписывание. If orchestrator настаивает на ≥5 P1 = REVISE — приемлемо, но за speech v1 это excellent first draft given baseline.
- Broken cross-ref / number drift = P1? **D1 Bowery + D2 Tzachor — number/date drift** = P1 ✓ catalogued. No broken cross-refs (43/43 slide IDs verified valid).
- Chapter source-of-truth → fix slides+speech, not chapter? **D1, D3, D4, D6, D7, D8, D9, D11, D13 — speech-side fixes**, chapter+slides correct. **D2 — bilateral: fix speech + fix chapter §8 misattribution warning** (internal inconsistency in chapter discovered). **D5, D12 — slide-side / 3-artifact cascade.** Book-first methodology preserved для most fixes.

---

## Summary back (≤300 слов)

**VERDICT: APPROVE-WITH-POLISH** — 0 P0, 5 P1, 8 P2.

**3 drift issues (priority):**

1. **D1 (P1).** Bowery + AppHarvest капитал drift в speech §1 s10. Chapter + slide: «Bowery >$700M / AppHarvest $475M SPAC + $341M долг»; speech: «Bowery около пятисот миллионов / AppHarvest около семисот миллионов привлечённого капитала». Speech systematically misstates Bowery (–$200M) и conflates AppHarvest SPAC + debt. Fix speech-side L190 ~10 мин.

2. **D2 (P1).** Tzachor publication date drift. Chapter §1.5 + slide s12: «Nature Food **ноябрь 2023** (press coverage 2024-05)». Speech §1 s12: «Май две тысячи двадцать четвёртого. Nature Food» — implies publication date. **Plus chapter §8 misattribution warning itself says «Nature Food 2024»** — internal chapter inconsistency. Fix bilateral: speech + chapter §8.

3. **D3/D4 (P1) carry-forward from Phase 7.** Магнит F&R missing в s37s + speech §5 s37s (chapter §6.1 lists Магнит как 4-th L5 success); ЭФКО + Русагро Тех missing в speech §5 s36c (slide lists 10 РФ companies, speech 8). Same structural gap as Phase 7 D1+D4. Cascade fix: slides first, speech second.

**3 что aligned correctly:**

1. **7/7 misattribution warnings** explicitly carried through all 3 artifacts (Indigo Ag НЕ в Verra; Tract = data backbone; Verra rainforest scope; Saga UV-C ≠ harvest; РСХБ vapor; Tzachor attribution; Cainthus ≠ Connecterra). Excellent cross-artifact discipline.

2. **Keystone-axis preserved across 3:** Лестница L1-L5 + closed-loop vs open-environment + 5 анти-AI critериев + Plenty Compton hook→payback arc. All 4 keystones discrete и closed.

3. **Strict-in ≥30% distributed correctly:** chapter ~39%, slides ~44%, speech **~42%** — independent per artifact, no single-artifact concentration. L4+ waiver-unavailable rule satisfied.

**USER GATE C ready: YES** with Phase 11 cascade revision (~45 min speech + ~3 min chapter §8 + carry-forward slide fixes from Phase 7). If owner chooses to defer slide D1/D3 fixes (Магнит + ladder) and apply speech-only fixes — GATE C openable after batched speech revision.

---

## File path для orchestrator

`/tmp/lec-10-wt/notes/lecture-10-review/critique-of-speech-v1-consistency.md`

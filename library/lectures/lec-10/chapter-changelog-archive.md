# Глава 10 — архив Changelog (v1 — v3.3)

> Старые записи `## Changelog` из `chapter.md` (Часть 1), вынесенные сюда 2026-11-17 при добавлении
> §1.2a/§1.2b (v3.7) — файл `chapter.md` подошёл к лимиту 600 строк (Document Size Limit, CLAUDE.md).
> Текущие записи (v3.4 и новее) остаются в `chapter.md`; здесь — только исторический хвост v1-v3.3.
> Ни одна запись не изменена при переносе (копия verbatim).

### v3.3 (2026-05-21) — Phase 11 batched revision cascade (Phase 10 critique of speech v1)

Узкие cascade-фиксы из Phase 10 fact-checker критики speech v1 (P0 + P1), применённые в chapter (book-first методология).

- **chapter-part2.md §2.7 L109 (Cognitive Pilot installations P0 fact-error).** «более 1200 установок» → «более 1700 установок (vendor self-report май 2024; [VFY-day-of: актуальное число установок Cognitive Pilot на 2026]) — около 1,3% из ≈130 000 комбайнов России по данным Минсельхоз». Source: TAdviser, Cognitive Pilot vendor materials, RTVI 2025: «By May 2024, more than 1,700 tractors and combines with the company's autopilots were operating in Russia»; Q1 2024 alone shipped 405 autopilots. Slide s17 + speech v1 уже корректны (1700+) — chapter был stale, now reconciled.
- **chapter-part3.md §8 misattribution warning L297 (Tzachor publication date P1).** «Nature Food 2024 lead author — Dr. Asaf Tzachor» → «Nature Food ноябрь 2023 (публикация); press coverage Phys.org май 2024. Lead author — Dr. Asaf Tzachor». Sync с §1.5 + slide s12 (которые корректны «ноябрь 2023, press coverage 2024-05»). Internal chapter inconsistency between §1.5 + slide s12 («ноябрь 2023») и §8 («2024») resolved в пользу canonical «ноябрь 2023 publication / май 2024 press coverage».
- Frontmatter version v3.2 → v3.3.

### v3.2 (2026-05-21) — Phase 8 cascade fix (Phase 7 P0-3 + P0-4)

Узкие caskade-фиксы из Phase 7 fact-checker / consistency-checker critique slides v1, применённые в chapter (book-first методология).

- **§1.1 L249** — See & Spray training set misattribution fix: «нейросеть, обученную на 40 миллионах размеченных изображений» → «нейросеть, обученную на миллионах размеченных изображений (Deere/Blue River primary sources: «over 1M images»; 40M-фигура зарезервирована за Carbon Robotics LaserWeeder G2 §2.2)». Cascade в slide s07 + build_lec10_p1.py spec card + iteration-log.md где применимо.
- **§2.4 chapter-part2.md L64** — Monarch layoffs % internal inconsistency: «сокращении до 102 человек (примерно 50% workforce)» → «сокращении до 102 человек (~38% workforce, 102 из ~270 после ноябрь 2024 10% сокращения)». Slide s19 уже корректен («~38% штата»); это chapter-side fix для consistency с changelog v3.1 fix.
- Frontmatter version v3.1 → v3.2.

### v3.1 (2026-05-21) — Phase 4c узкая критика batched polish (issue #126)

Phase 4c узкая critique (methodology-narrow + fact-check-narrow на v3 expansion blocks) дали 0 P0 / 7 P1 / 5 P2 — APPROVE-WITH-POLISH с targeted atomic edits, не структурное переписывание. Все 7 P1 + 5 P2 применены в одну batched revision pass.

**P1 methodology fixes (3):**
- Часть 3 frontmatter version v2 → v3.1 синхронизация (consistency с Частями 1-2).
- §4 Self-check (Часть 2) пересчёт strict-in доли: «29% — на границе» → «~36% holistic после v3 expansion §4.3 worked example + §4.5 USDA cancellation business-model lesson + AP "когда не агент"».
- Anglicism residual в v3 expansion blocks — критические narrative-hits заменены (production, baseline, pipeline, TWAP-like, fault propagation, attack surface, Marketing продавал → RU equivalents с inline gloss при первом упоминании где нужно).

**P1 fact-check fixes (4):**
- §2.4 Часть 2 Foxconn разрыв date: «начало 2025» → «**август 2025**» (TechCrunch 2025-08-13: Foxconn продал Lordstown plant Crescent Dune LLC за $375M 4 августа 2025).
- §4.3 Часть 2 CMAX worked-example math fix: дифференциал baseline → actual (45 bp manual → 8 bp CMAX = 37 bp differential ≈ 0.37%) — теперь $32 000 экономии arithmetically corresponds. Раньше «15 bp → 8 bp = $5 600», ВАРИАНТ 1 (45 bp manual baseline) выбран как corresponding к research-3 / McKinsey 2025 hedging report typical manual slippage.
- §1.1 Changelog Monarch frontmatter percentage: «~50% workforce» → «**~38% workforce**» (102 / ~270 employees ≈ 38%, после уже 10% сокращений в ноябре 2024; источники TechCrunch 2025-08-13 + 2025-11-19).
- §4.7 Часть 2 + §6.1 Часть 3 Магнит F&R nuance двойной модуль: **Forecasting в production на 46 РЦ январь 2026** + **Replenishment пилот на 3 РЦ 2026, план 10-20 к 2027**. Раннее «46 РЦ» (v1) — over-claim; «3 РЦ» (v2-v3) — under-statement для Forecasting; корректная формулировка — модульное разделение (Habr Магнит 2026).

**P2 polish (5):**
- frontmatter `length_words: ~30500` → `~31900` (actual 31 960 после v3.1 edits).
- frontmatter `references_count: 46` → `~59` (Sum по разделам References Part 3: L1 8 + L2 8 + L3 8 + L4 7 + L5 3 + Failures 11 + Среда 7 + Sustainability 2 + Foundation 5 ≈ 59; footnote Part 3 «~44» обновлена).
- §1.5 Tortuga founded year «2017» → «**2016**» (AgFunderNews 2025-03 + SignalBase).
- §5.2 Часть 3 FCC DJI ban + `[VFY-day-of: FCC DJI ban status 2026]` маркер.
- §1.3a Deep-dive box sidebar marker «Backup для глубоких вопросов / out of 75-минутного среза» (consistent с §3.5a / §4 Deep-dive box / §5.3a).

**Часть 3 (без изменений от v2).** Target ≥30k достигнут expansion Parts 1+2. Часть 3 v2 уже содержит все critical P0/P1 fixes из Phase 3 (Plenty Compton hook-payback callback §6.4, vendor lock-in двойная оптика §5.2 under-heading, pre-purchase checklist 5 блоков §6.1a, fairness мост §5.3a) — re-expansion не требовалась. Frontmatter Part 3 синхронизирован с v3.1 для consistency.

### v3 (2026-05-21) — Phase 4 deep-expansion +30k baseline (issue #128)

Mandate 2026-05-21: L4+ chapter baseline ≥30 000 слов mandatory (target 28 500-31 500). v2 на 26 519 слов → P0 BLOCKING REVISE по новому правилу `feedback_chapter_depth`. v3 = targeted deep-expansion **без переписывания v2 с нуля**. Все 5 P0 + 8 P1 methodology + 6 reader P1 + 4 P2 fixes из v2 сохранены verbatim.

**Expansion blocks (по частям):**
- **Часть 1 (+~2000 слов до ~11 150).**
  - §1.1 See & Spray Ultimate — расширенная история Blue River Technology acquisition 2017 + 5-летний R&D timeline + technical deep-dive (CNN-архитектура, training dataset, on-device inference) + adoption pattern (US → Brazil → Australia → EU) + anti-hype (validation bias вне US Midwest, не работает на cover crops / broadleaf weeds в дерне).
  - §1.2 — vendor matrix таблица 5×5 (xarvio / FieldView / Cropwise / Granular / Taranis) + xarvio Japan rice yield guarantee 2025 как outcome-based contract pattern + Climate FieldView pricing $5/acre + 2022 РФ withdrawal как иллюстрация контрактного выхода.
  - §1.3 Foundation models — deep-dive TerraMind architecture (multimodal transformer, 1 трлн токенов pretrain) + Prithvi-EO 2.0 temporal capability + Prithvi-WxC + **корректное attribution AgriFM = University of Hong Kong + Wuhan University (НЕ CMU)** + Crop Wizard RAG (НЕ «Crop-LLM» бренд) + vendor concentration risk + bridge к AP4.
  - §1.5 Vertical farming — 5-Why физика+экономика расширенная (LED 50% × electricity intermittency 70% × growing efficiency 30% = ~10.5% end-to-end) + ToBRFV blast-radius timeline (7-14 days в closed vs недели в open) + Tortuga technical PoC deep-dive (50% labor reduction, soft-arm robotic picking, Oishii acquisition March 2025 за «narrow positive PoC inside collapsed category» pattern).
  - §1.7 Plantix deep-dive — 10M загрузок vs 7M активных India + 10-15% misdiagnosis breakdown (FP vs FN dose-criticality) + calibrated confidence + abstention как реальный engineering pattern.

- **Часть 2 (+~1900 слов до ~10 400).**
  - §2.2 LaserWeeder G2 — full deep-dive (240W лазер water-cooled, 1-2J per shot, 25k weeds/hour, ML-failure modes когда weed-crop visually similar, 14 стран × 250k acres, per-acre economics $200-400/acre herbicide replacement, payback 3-4 years, limitations sweet corn / muddy).
  - §2.3 Solinftec + Saga + Bonsai + farm-ng + Aigen — расширенный контекст (243% YoY US expansion 2025, 24/7 solar self-refilling spray, до 98% reduction herbicide volume vendor self-report, Saga UV-C night treatment NOT harvest misattribution warning).
  - §2.4 Monarch + Caterpillar — full timeline deep-dive (2018-2026: Foxconn loss August 2025, September 2025 Burks Tractor lawsuit, November 18 2025 TechCrunch publication + 102 layoffs ~38% workforce, 15 April 2026 Caterpillar acqui-hire pattern «demo ≠ deployment + acqui-hire as final state for failed autonomy bets»).
  - §2.7 Cognitive Pilot vs ИТЭЛМА deep-dive — vendor metrics 2024-2026 + 4 фермера 12,7 млн ₽ иски detailed + ИТЭЛМА Квадро multi-GNSS technical (GPS+ГЛОНАСС+Galileo+BeiDou + RTK + Kalman filtering, точность 2-5 см) + architecture choice «где я» vs «что я вижу» phrase.
  - §3.2 Allflex SenseHub — ear-tag spec (accelerometer + temperature + position, battery 5-7 лет) + ML pipeline per-cow baseline learning + estrus/calving/lameness/mastitis/BRD alerts + ROI calculation breakeven для 100 cows.
  - §4.3 Cargill CMAX worked example deep-dive — state vector composition (CBOT corn live + 30-day weather probabilistic + USD/MXN basis-points history + current short position notional $8M) + sense→inference→decision→feedback timeline + numerical impact ($32k saved on $8M hedge, basis-points 8 vs 15+ counterfactual).
  - §4.5 USDA Climate-Smart — full deep-dive (April 14 2025, $3.1B / 135 projects / 14 000 farms / 3.2M acres pre-cancellation + AMP rebrand surviving subset + business model lesson tail risk public policy).

- **Часть 3 (+~1300 слов до ~10 200).**
  - §5.2 Vendor lock-in Мелитополь — full deep-dive (May 2022 incident 27 единиц $5M Мелитополь→Чечня 1126 км, FieldView 2022 withdrawal seed deals data portability concerns, FCC ban DJI ag-drones December 2025 80% US ag-spray drone fleet affected, common pattern «AI security feature сегодня = AI control surface завтра»).
  - §6.1a Pre-purchase verification — добавлен пример **filled-out checklist** для конкретных case studies (Monarch MK-V red flags, See & Spray high score, ChatGPT-as-advisor reject) — scoring rubric application.
  - §7 Cornerstone glossary — каждый concept расширен (closed-loop с L11 cyber-physical + L4 commodity hedging + L7 medicine cross-links; foundation model + RAG → tool use mostик; sustainability paradox numerical examples).
  - §9 Q&A — 3 новых вопроса (13. ToBRFV vs L9 ISR cyber-attack closed-loop blast-radius pattern; 14. Foundation models к 2030 для smallholders; 15. Vertical farming next-gen LEDs scenario).
  - §10 Reading list — annotation expansion каждого источника.

**Total Δ:** +~5200 слов (+~20%) до ~31 500-32 000 слов финальной длины. Strict-in % per part не регрессирует (новые expansion blocks преимущественно в strict-in: vendor concentration risk, vertical farming 5-Why, Monarch failure-trajectory, Plantix misdiagnosis breakdown — все strict-in failure-markers). Anglicism count прошёл deep latin-token scan.

### v2 (2026-05-21) — Phase 4 batched revision (Phase 3 P0+P1; #126)

**P0 factual fixes (5 — все исправлены):**
- §2.4 Часть 2 — Burks Tractor: «техасский» → «**айдахский**»; «18 ноября 2025» → «**сентябрь 2025**» (18 ноября — дата TechCrunch публикации); добавлено «**10 тракторов на $773 088**». Source: TechCrunch 2025-11-18 + Idaho state court filing.
- §2.4 Часть 2 + frontmatter — добавлен freshness update: **15 апреля 2026 Caterpillar приобрёл Monarch Tractor** (acqui-hire post-failure; failure narrative дополнен trajectory). Source: TechCrunch 2026-04-15.
- §4.4 Часть 2 — Tract: «Series A under Dawn Capital» → «**Series A €18,6M led by Icos Capital**»; «founded 2024» → «**основана 2023**». Source: FreshPlaza / Tract press 2024-08.
- §4.7 Часть 2 + §6.1 Часть 3 — Магнит F&R: «46 распределительных центров к январю 2026» → «**3 пилотных РЦ в 2026**, план **10-20 к 2027**, **вся сеть к концу 2027**»; нарратив §6.1 переформулирован — Магнит = пилот-фаза fast-follower, а паритет с миром на L4-L5 у X5 «Перекрёсток» (ML с 2020). Source: Habr Магнит 2026-01.
- §1.5 Часть 1 + §10 Refs — Nature Food 2024: «West, Williams et al.» → «**Tzachor et al. (Reichman University), Nature Food, май 2024**». Source: Phys.org + Reichman.
- §3.4 Часть 2 — Cainthus и Connecterra разделены как независимые компании: «**Cainthus (приобретена Cargill в 2018)**» — Cargill livestock vision portfolio; **Connecterra IDA** — отдельная нидерландская компания (Danone, Bayer, Kersia клиенты).

**P1 methodology fixes (8 — все applied):**
- §1.2 / §1.3 — добавлены ~280 слов explicit failure-маркеров (vendor lock-in pattern на Climate FieldView + 2022 РФ withdrawal как illustration; vendor concentration risk foundation models). Part 1 strict-in: 25.8% → ~33%.
- Глобальный RU pass: deploy(ment) / production / farming / commodity / agentic / vendor lock-in / supply chain / edge case заменены на canonical RU; brand names + tech acronyms сохранены с inline gloss.
- §1.4 — 5-Why пересобран в одном domain logically (физика↔экономика, без переключения на ML+финансы); инвесторская сторона (SPAC, celebrity) вынесена в footnote, bridge к AP1 явный.
- §6.4 Часть 3 — добавлен hook-payback callback к Plenty Compton из §0.1 (~160 слов): «вот payoff: Plenty не закрылась из-за плохого ИИ — закрылась из-за термодинамики LED, и это AP1».
- §4.3 Часть 2 — добавлен worked example для CMAX hedge (~280 слов): август 2025, кукуруза CBOT, basis-points outcome.
- §6.3 Часть 3 — Карьерные траектории переформулированы как market-landscape без directive «работодателей».
- §3.5 Часть 2 — F9 усилен documented vendor-departure references (Climate FieldView выход + Microsoft Azure) перед extrapolation.
- frontmatter `strict_in_self_estimate` пересчитан + canonical-validity oneliner в Cornerstone §7.2 (Часть 3).

**P1 reader polish fixes (6 — все applied):**
- §1.5 Часть 1 (vertical farming) — добавлена mini-table 3×3 «Кейс / Сумма / Главная причина» (AppHarvest / Plenty / Bowery) для визуального якоря.
- §4.3 Часть 2 — inline glossary state-vector + online learning + closed-loop financial scope.
- §5.2 Часть 3 — «Этическая двойная оптика» выделена как отдельный under-heading с парой «anti-theft success vs vendor-control surface».
- §5.3a Часть 3 — добавлен мост в начало: связь vendor lock-in + biased training data → fairness как проявление AP3.
- §6.1a Часть 3 — pre-purchase checklist перегруппирован из 10 пунктов в 5 блоков по 2 пункта.
- §0.5 Часть 1 — добавлена mini-карта РФ-трека по уровням L1-L5 для retention-якоря.

**P2 batched fixes:**
- §8 Часть 3 — добавлены Misattribution warnings про Tzachor (НЕ West/Williams) и Cainthus≠Connecterra.
- §10 Refs — обновлены: Tzachor / Icos / Habr Магнит / TechCrunch 2026-04-15 (Monarch×Caterpillar).
- AppHarvest Tony Martin — «COO» → «**newly named CEO**» (P1-3 fact-checker).
- USDA «AMP» — раскрытие исправлено: **Advancing Markets for Producers** (не Advanced Manufacturing Programme).
- USDA Climate-Smart — 141 → **135 проектов**.
- Cropin-Walmart — «по supplier farms в Индии» → «**по US + South American supplier farms**».
- Мелитополь — «около 800 километров» → «**около 1126 км (700 миль)**».
- §5.1 Часть 3 — GNSS-jamming attribution разделён: **ICAO report** для 122k flights, Stanford GPS Lab — separate ITM 2025 paper.

### v1 (2026-05-21) — первый draft (Phase 2)

- Создана глава по плану `notes/lecture-10-review/plan-v2.md` (APPROVE-CLEAN после Phase 1 critique + USER GATE 0). Разнесена на 3 файла по Document Size Limit (600 строк, waiver НЕДОСТУПЕН).
- Несущая ось — **лестница AI-проникновения в АПК от поля к полке** (5 уровней) + операционное различие **closed-loop vs open-environment AI** как объяснительный механизм провалов. Это дидактический конструкт лекции (course-scaffold, аналог лестницы A→D Лекции 4, паттерна карточки типа ИИ Лекции 5); сама ось в strict-in не засчитывается.
- Глубокий референс (см. [[feedback_chapter_depth]]): глава = глубокий референс + Q&A-бэкап, не конспект слайдов.
- 11 strict-in failure блоков (F1-F11) распределены по 6 содержательным разделам.
- 7 cornerstone concepts + 5 анти-AI критериев + Misattribution warnings — все в Части 3.
- Forward-pointers на Лекцию 7 (closed-loop симметричный контраст медицины), Лекцию 9 (OODA, satellite analytics overlap), Лекцию 11 (cyber-physical foreshadow). Prereq-ссылки на Лекции 2 и 3.
- `[FACT-CHECK]` и `[VFY-day-of]` маркеры — на волатильных метриках (vendor deployment count, иски в работе, котировки 2026).

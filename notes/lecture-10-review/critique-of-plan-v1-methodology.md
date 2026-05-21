# Methodology critique — lec-10 plan-v1

**Дата:** 2026-05-21
**Критик:** methodology-critic
**Target:** `notes/lecture-10-review/plan-v1.md` (506 строк, ~3 350 слов)
**Verdict:** **REVISE**
**Counter-check:** strict-in ≥30% — PASS plan-level (40% time, см. counter-check ниже); keystone-axis ENFORCED — PASS; tools-per-taxonomy L4+ — PASS с замечаниями; **Bloom-level Apply LO purity** — FAIL (P1-1); **Раздел 5 pacing** — FAIL (P1-2); **Vertical farming split** — concern (P1-3); **Tools per L3 < 3** vs L1, L2, L4, L5 — FAIL (P1-4); **Hook A engagement vs course mission** — FAIL (P1-5); **РФ-блок Cognitive Pilot vs ИТЭЛМА — подмена тезиса** — concern (P1-6).

---

## TL;DR

План v1 — методически крепкий по структуре: keystone-ось (лестница L1→L5) предъявлена корректным keystone-слайдом в Разделе 0 ДО первого погружения; failure-bucket budget структурно ≥30% с холистическим распределением по 5 разделам; tools-per-taxonomy L4+ соблюдено для всех 5 уровней; missing-fundamentals явно отделена (инфраструктура — отдельный слайд s35). 11 failure-блоков, 7 anti-AI критериев, 50+ named tools, 7 cornerstone concepts — scope богатый, fact-base из 4 research-файлов use-d полностью.

**Главные проблемы — 6 P1 + 5 P2:** (1) LO1 смешивает Remember + Apply в одной формулировке, как в Лекции 9 v1; (2) Раздел 5 пакует L5 + 3 темы среды + 5 критериев + career + reading + callback в 14 мин — это **8 sub-секций × ~1.75 мин**, нереалистично; (3) Vertical farming разбит F1 (Р1, 1-мин summary) + F6 (Р2, ~3 мин deep) — F6 в Р2 натянуто (Tortuga **bridge**: «технический успех ≠ коммерческий» в L2 «robot» уровне — но Plenty/AppHarvest — это L1 «closed-environment» failure, не robotics); (4) L3 «Животное» имеет 4 working + 2 failure при только 10 мин — это плотнее чем L2 «Робот» (15 мин) с почти таким же scope; одновременно tools-per-taxonomy table показывает только 4 working без явного adoption-направление-cluster для local пород РФ vs Holstein — частичное упущение; (5) Hook A (See & Spray BEFORE/AFTER) — visual-wow success-first, но Лекция 9 critique уже зафиксировала, что **failure-first opening методологически сильнее для course mission** («учить говорить нет»); план **не учёл** этот недавний lesson и рекомендует A, не B; (6) РФ-блок Cognitive Pilot vs ИТЭЛМА подан как «AI/CV не нужен, спутник проще» — но research-04 R2 явно указывает, что ИТЭЛМА **тоже AI** (multi-GNSS обработка сигналов «Итэлма Квадро»), а вопрос — какой тип AI (CV vs sensor fusion) подходит под open-environment пыли. Подмена тезиса «AI vs не-AI» вместо «один тип AI vs другой».

5 P2 — polish: anti-AI критерии в Р5.5 — 5 из 7, но AP6 (vendor lock-in) и AP7 (AI-MRV без direct measurement) объявлены «бонус», тогда как методически они **сильнее** некоторых из первой пятёрки; **Indigo Ag** дисклеймер про «НЕ в скандале» — corrects misleading impression только в speech, не в plan structure; **L4 «Cargill / Tract» — визуал** для grounding agentic-абстракции open question, но методически план уже знает решение (s27 «как agent делает hedge: pseudo-flow»); **5 cornerstone concepts** дублируются с **7 anti-AI критериями** (Open/closed повторяется в AP1+AP2 и в cornerstone 2; vendor lock-in в AP6 и cornerstone 5); **5-min Q&A budget** ≠ 10-min Раздел 6 placeholder — pacing math неточна.

Phase 2 (chapter draft) **не рекомендуется начинать** без устранения P1-1 (LO разбить), P1-2 (Раздел 5 расширить либо сжать sub-секции), P1-4 (L3 attune to L2 weight ratio), P1-5 (Hook A vs B decision на failure-first), P1-6 (Cognitive Pilot framing fix). P1-3 (vertical farming split) — fixable либо в plan-v2 либо явным design brief.

---

## P0 issues (must fix перед Phase 2)

**Нет P0 issue.** Все обязательные структурные mandate (keystone-axis ENFORCED, tools-per-taxonomy L4+, strict-in ≥30% structurally, missing-fundamentals separation) соблюдены на plan-level.

---

## P1 issues (should fix)

### P1-1 — LO1 смешивает Remember + Apply, нарушает Bloom-level чёткость (Лекция 9 lesson не учтён)

**Где:** строка 30.

**Текст плана:**
> «**LO1.** Назвать пять уровней лестницы AI-проникновения в АПК (поле / робот / животное / supply chain / потребитель) и для каждого — 2–4 named tools 2026 года + направление adoption (растёт / стагнирует / переоценено).»

**Проблема:** LO1 объединяет (а) **Remember** (назвать уровни и tools) + (б) **Apply** (определить «направление adoption — растёт / стагнирует / переоценено»). Это разные Bloom-levels, оцениваются по-разному. Лекция 9 plan-v1 имела **идентичный** issue (P1-1 в lec-09 critique), и был исправлен в v2 разбиением на LO1a (Remember) + LO1b (Apply). Lec-10 plan **повторяет** ошибку.

**Evidence:**
- Лекция 9 critique-of-v1-methodology.md строки 26-40 — explicit fix этой schemы.
- Lec-07 chapter (intermediate-аналог) разделяет LO1 (Remember-классификация) и LO2 (Apply-оценка применимости) — методически корректное разделение.

**Recommendation:** разбить LO1 на:
- **LO1a (Remember).** «Назвать пять уровней лестницы AI-проникновения в АПК и для каждого — 2-4 dominating 2026 tools.»
- **LO1b (Apply).** «Для каждого уровня — оценить направление adoption (растёт / стагнирует / переоценено) с обоснованием через 2026-метрику и anti-hype оговорку.»

Это даёт 4 LO: LO1a, LO1b, LO2, LO5 — что согласуется с lec-09 паттерном после fix.

**Cost-of-omission:** если оставить — Phase 3 methodology-critic на chapter обязательно flag-нет тот же P1; время теряется на тот же circular fix.

---

### P1-2 — Раздел 5 (14 мин на 8 sub-секций) — pacing нереалистичен, density-bomb finale

**Где:** строки 226-259 (Раздел 5).

**Текст плана:**
> «**Раздел 5 — L5 + среда: connectivity, vendor lock-in, regulatory, payoff (14 мин)** … 5.1 L5 «Потребитель / retail» ~3 мин; 5.2 connectivity ~3 мин; 5.3 vendor lock-in + санкционный shock ~3 мин; 5.4 regulatory ~2 мин; 5.5 5 явных «когда не AI» ~2 мин; 5.6 career angle ~1 мин; 5.7 reading list ~1 мин; 5.8 closing callback ~1 мин.»

**Проблема:** **8 sub-секций × 1.75 мин в среднем — physically невозможно за 14 мин**. Сумма sub-секций = 16 мин (3+3+3+2+2+1+1+1), и это **БЕЗ slide transitions / Q&A buffer / cognitive load для final раздела** (студент уже потратил 60 мин активного внимания на 4 предыдущих раздела). Каждая из 5.2-5.4 («connectivity», «vendor lock-in», «regulatory») — самостоятельный учебный блок с failure-кейсами (Cognitive Pilot+ИТЭЛМА; FTC v. Deere + Мелитополь + FCC DJI; EU AI Act + USDA + «АПК будущего»). На 3 мин = только headline + 1 example, без discussion. Это **density-bomb finale**, повторяет Лекция 9 plan-v1 P1-2 ошибку («Раздел 4 7 sub-sections × 2 мин — pacing нереалистичен»).

5.5 «5 явных когда не AI» — 2 мин = **24 секунды на критерий**. Это **visual-checklist слайд + lecturer прочитывает**, не педагогический блок. Lec-09 critique P2-3 explicitly рекомендовала distributed retrieval (каждый критерий — закрывающий takeaway соответствующего раздела + consolidation slide финале). Lec-10 plan **повторяет** end-loaded list паттерн.

**Evidence:**
- Lec-09 critique P1-2 + P2-3 — те же два паттерна (sub-сек density + 7 критериев end-loaded).
- Strict-in budget table (строки 274-285) показывает 8 мин strict-in в Р5 — но это **75% от content time** в этом разделе (если sub-сек 5.1, 5.6, 5.7, 5.8 не strict-in). Это **single-section over-concentration**, антипаттерн.

**Recommendation:**
1. **Сжать 5.6 + 5.7 + 5.8 в 1 sub-секцию «payoff» 2 мин** (career angle 1 строкой, reading list 1 слайдом, closing callback 30 сек) → освобождает 1 мин.
2. **Distribute 5 «когда не AI» критериев** в финальные takeaway каждого Раздела 1-4 (по 1-2 критерия из соответствующего failure-блока), и в 5.5 — только consolidation visual-checklist на 1.5 мин.
3. **Либо** — расширить раздел до **16-17 мин** и сжать Раздел 3 «Животное» до 8 мин (где P1-4 указывает плотность; см. ниже).
4. **Либо** — вынести meta-блок «среда» (5.2 + 5.3 + 5.4) в **отдельный Раздел 4-bis после Supply chain**, и Раздел 5 = только L5 + payoff (6-7 мин).

Любой из вариантов **исправит** density-bomb. Я рекомендую вариант (4) — это **дополнительная структурная корректность**: meta-уровень «среда» — это не L5 retail, это cross-cutting layer, его смешение с L5 контентом методически путает.

---

### P1-3 — Vertical farming split: F1 (Р1) + F6 (Р2) — Tortuga bridge натянут, L1 vs L2 mismatch

**Где:** строки 160 (F1 Р1) + 182 (F6 Р2).

**Текст плана F1 (Р1, L1 «Поле»):**
> «**F1. Vertical farming collapse** (1-минутный summary с указателями на Р2): $1.37B+ потерь в 2025 одних только; AppHarvest ToBRFV = «closed loop ↑ blast radius»; Plenty = «AI не закрыл energy gap»; Bowery $32M оборудования никогда не запустили. … **Bridge:** «закон термодинамики важнее ML — мы вернёмся к этому в Р2».»

**Текст плана F6 (Р2, L2 «Робот / машина»):**
> «**F6. Vertical farming deep-dive (часть 1 из распределённого блока)** — economics + closed-loop blast radius. Plenty bankruptcy: $940M потеряно; … AI-роботы Tortuga (acquired by Oishii март 2025) **технически работали** (50% reduction в harvest expenses), но категория проиграла unit-economics. **Bridge** к Р3: «технический успех не = коммерческий успех; теперь смотрим на L3, где economic value животноводства лучше выровнен».»

**Проблема:**
1. **Tortuga bridge натянут.** Plenty/AppHarvest/Bowery — это **L1 уровня «Поле»** (closed-environment indoor farming = controlled environment, attempts replace open-field agriculture); не L2 уровня «Робот / машина». Tortuga (harvest robot) — это **робот внутри vertical farm** — robot в L2 терминах, но **vertical farming как category коллапс — это L1 unit-economics failure** (LED vs sunlight), а не L2 robotics failure.
2. **Аргумент «технический успех ≠ коммерческий» — это не L2 lesson**, это **business-model lesson** (cross-cutting). Поместив его в L2, план **искажает keystone-ось** — L2 раздел теперь учит «робот не помог категории», а не «autonomous robot в semi-controlled environment работает / ломается на специализации vs generic».
3. **Strict-in budget** в Р2 уже 8 мин (densest failure section) с F4 Monarch + F5 FarmWise/Naïo + F7 strawberry economics. Добавление F6 vertical farming (~3 мин) делает Р2 **9-11 мин strict-in из 15 мин content** = **60-73% strict-in в одном разделе**, что — single-section over-concentration, антипаттерн AI-Failure rule.

**Evidence:**
- Research-02 §A «Коллапс vertical farming как класса» — explicitly framed как **closed-environment failure**, не robotics failure. F11 Tortuga из research-02 (если бы исследовалось отдельно) — это narrow positive technical PoC внутри коллапсирующей категории, не «робот не спас».
- Keystone table (строки 42-48): L1 «Vertical farming collapse $1.37B+» = canonical failure L1; L2 «Monarch MK-V (иски 2025, layoffs)» = canonical failure L2. План **сам в keystone** разделяет — но в outline (Р2) объединяет.

**Recommendation:**
1. **Vertical farming = 1 сильный блок целиком в Р1 (L1 «Поле»)** — 4-5 мин deep dive (AppHarvest ToBRFV + Plenty energy gap + Bowery $32M sunk + 14 банкротств 2025 catalogue + Tortuga «технический успех ≠ коммерческий» как footnote). Это **методически корректно** (vertical farming — closed-environment попытка переехать из L1 open в L1 closed, Tortuga — narrow positive inside collapsed category).
2. **В Р2** — оставить F4 Monarch + F5 FarmWise/Naïo + F7 strawberry economics (3 failure × 2.5 мин = 7.5 мин strict-in). Это balanced: 7.5 из 15 мин Р2 = 50% strict-in, что reasonable для densest failure section.
3. **Bridge L1 → L2:** «AI не справляется в open-environment (failure F2-F3) И в попытке закрыть environment (vertical farming F1+F6 объединено). Теперь смотрим на L2 — semi-controlled environment робота: где specialization работает / где generic ломается.»

Это **сохраняет** distributed retrieval (vertical farming затрагивает 2 уровня lesson value: open vs closed для L1; specialization vs generic для L2), но **не размывает** structural integrity keystone-оси.

---

### P1-4 — L3 «Животное» (10 мин, 4 working + 2 failure) — overload vs L2 weight ratio

**Где:** строки 189-206 (Раздел 3).

**Текст плана:**
> «**Раздел 3 — L3 «Животное»: livestock CV (10 мин)** … **Working cases (4).** Allflex SenseHub … CattleEye … DeLaval VMS V310 … Cargill Birdoo … **Strict-in failures (2, ~3 мин).** F8 Cainthus tie-stall … F9 РФ dairy uncertainty …»

**Проблема:** **6 кейсов × ~1.67 мин на 10 мин раздела** — это плотнее чем Р2 «Робот» (15 мин на 5 working + 4 failure = 9 кейсов × ~1.67 мин = тот же rate, но в **большем budget**). L3 раздел **под-budgeted** относительно своего scope:
- 4 working cases — каждый требует ≥1.5 мин (SenseHub 2M cows milestone + Cargill Birdoo CV economics — это два разных value prop, нельзя слить).
- 2 failure cases — F8 Cainthus tie-stall + F9 РФ dairy uncertainty — **3 мин на оба** = 1.5 мин на кейс. F9 особенно проблематичен: research-04 (R3) указывает, что «реальные кейсы отключения сервисов в РФ публично не задокументированы» — это **«architectural риск», not documented failure**. Для 1.5 мин нельзя адекватно объяснить это nuance (а если объяснить, это будет звучать как FUD-speculation).

**Tools-per-taxonomy table L3 (строки 99-103)** **сама** показывает asymmetry:
- adoption «Растёт стабильно (CV дёшев, dairy/poultry economic value высок); консолидация (GEA acquired CattleEye, MSD acquired Antelliq за $3.85B). РФ: ограничено санкциями + AI-функционал зарубежных систем требует firmware updates из Европы — уязвимая точка.»
- **anti-hype** — слабый: «Algorithm tuned для Holstein / dairy breeds — для местных пород калибровка слабая. Subscription costs ($30/cow/year) для small dairies (<50 cows) — overkill. CV требует чистых barns + good lighting — tie-stall barns не подходят.»

Это **3 anti-hype oговорки**, каждая = full lesson. На 10 мин раздела с 4 working + 2 failure — **не хватает воздуха** для них.

**Evidence:**
- Lec-09 critique P1-2 — точно тот же паттерн (раздел с 7 sub-sec × 2 мин — нереалистичен).
- Research-01 §3.2 (CattleEye), §3.1 (SenseHub), §3.5 (DeLaval), §3.6 (Cargill Birdoo) — каждое реальное deployment с metrics; не «filler-кейсы», все имеют lesson value.

**Recommendation:**
1. **Расширить Р3 до 12 мин** (сжать Р4 «Supply chain» с 12 до 10 мин — Р4 имеет fewer failure cases при том же scope, более компактно реализуется через 4 working cases × 1.5 мин + 2 failure × 2 мин = 10 мин).
2. **Либо** сократить working cases в Р3 до 3 (слить DeLaval VMS V310 + Cargill Birdoo в один «production-mature dairy/poultry CV» block за 1.5 мин).
3. **Усилить anti-hype** для Holstein-bias в slide notes (это методически важный lesson для **глобальной АПК-аудитории** — не все коровы — голштины), отдельным P1 для chapter (через 1 параграф), не для plan.

---

### P1-5 — Hook A (See & Spray BEFORE/AFTER) — visual-wow success-first, course mission requires failure-first

**Где:** строки 136-141.

**Текст плана:**
> «**Hook кандидаты.** **A.** **BEFORE/AFTER See & Spray на хлопке** — selective spray в дюзах + counter «–50% гербицидов, 5M акров». Evergreen, success-first, политически нейтрален. **Моя рекомендация.** **B.** **Plenty Compton facility** open vs closed (май 2023 → декабрь 2024) — failure-first hook. Драматичен, прямо служит AI-Failure rule, но mood депрессивный. … **Рекомендация:** A primary; C fallback как «свой» бытовой контраст после A. B на keystone как «контр-пример» (одной строкой).»

**Проблема:** **«mood депрессивный»** — слабое возражение против hook'а, который **align с курсовой миссией** («учить говорить нет неподходящему ИИ»). Лекция 9 critique P2-2 точно зафиксировала: «failure-first opening методологически сильнее для course mission, чем visual-wow». Lec-10 план **повторяет** ту же ошибку — рекомендует success-first hook А.

Дополнительно:
1. **See & Spray BEFORE/AFTER** — visual-wow для **существующего успеха**; студент 3 курса **не получает** insight из этого («да, оно работает, ок, поехали дальше»). 
2. **Plenty Compton split frame (май 2023 ribbon-cutting → декабрь 2024 закрытие)** — visual-wow для **краха ожиданий**; студент **получает** insight («$940M потеряли — как? почему?»). Это **engagement-провоцирующий** hook, не «mood депрессивный» (драматичный ≠ депрессивный).
3. **Cognitive Pilot vs пыль** (Hook C) — РФ-кейс, эмоционально **сильнее** для российской аудитории (Bauman); план **сам** ставит как «бытовой контраст в Р2», что **подтверждает** силу. Если бы Hook C был слабый — план бы вынес его в reading list.

**Evidence:**
- CLAUDE.md «AI-Failure & Judgment Content Rule» — миссия курса = критическое суждение. Hook должен **provoke critical thinking**, не показать «работает».
- Lec-09 plan-v1 P2-2 — explicit rejection «mood депрессивный» возражения.
- Research-02 §A — Vertical farming collapse как самая громкая AgTech-история 2025 ($1.37B+ потерь, 14 банкротств) — **студент 3 курса** скорее всего слышал что-то про vertical farming как «AI-будущее»; failure-first hook **переворачивает** существующую expectation.

**Recommendation:**
1. **Hook primary = B (Plenty Compton split-frame)** — failure-first, 2026-evergreen, прямо служит AI-Failure rule.
2. **Hook fallback = C (Cognitive Pilot vs пыль)** — РФ-кейс, удерживает audience attention при международном fallback failure.
3. **Hook A (See & Spray)** — переместить в Р1 как working case opening (естественное место visual-wow «вот success»).
4. **Keystone slide** (отдельный после hook) — остаётся «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**», без изменений.

Это **сохраняет** structural integrity (keystone до первого погружения) и **усиливает** course mission alignment.

---

### P1-6 — Cognitive Pilot vs ИТЭЛМА framing как «AI не нужен, спутник проще» — подмена тезиса

**Где:** строки 185, 364, 383.

**Текст плана (строка 185):**
> «**ИТЭЛМА** (спутниковый стек) на «Кировцах» с конца 2025 — структурный сдвиг, «AI/CV не нужен, спутник проще».»

**Текст плана (AP2 в строке 364):**
> «AP2 | **Open environment + critical physical condition** … Cognitive Pilot vs пыль (4 иска 12,7М ₽ 2025); FarmWise dust + lighting failure (wind-down 2025) | GNSS / RTK-based навигация (ИТЭЛМА), mechanical weeders (Lemken, Kverneland)»

**Текст плана (cornerstone 4 / РФ-блок строка 383):**
> «**Главный РФ-урок:** **AI-зависимость = политический риск; российский опыт после 2022 — natural experiment, что бывает, когда импортный AI-стек отключается**.»

**Проблема:** **Тезис «AI/CV не нужен, спутник проще» — подмена тезиса**. Research-04 §R2 явно описывает ИТЭЛМА:
> «технология Итэлма Квадро — обработка сигналов нескольких GNSS-созвездий. … Архитектурное отличие от Cognitive Pilot: GNSS / RTK-based вместо CV-based → менее уязвим к пыли, освещённости, типу культуры; но требует исправного спутникового приёма и зависит от собственной RTK-инфраструктуры.»

ИТЭЛМА — **тоже AI**: multi-GNSS обработка сигналов с предсказанием поправок, kalman filtering, sensor fusion — всё это algorithms из AI-семейства (data-driven inference). Это **другой класс AI**, не «не-AI». Корректный тезис:
- **«Open-environment физика делает CV-AI хрупким; sensor-fusion-AI на multi-GNSS — более робастный подход»** — а это **другой урок**, чем «AI не нужен».

«AI не нужен, спутник проще» **искажает**:
1. Студент 3 курса заберёт **wrong intuition** — что «когда CV ломается, AI вообще не нужен». На самом деле — нужен **другой тип AI** (sensor fusion вместо CV).
2. Это **противоречит** cornerstone 6 «Foundation model + grounded reasoning — общая pretrained модель + RAG-привязка к локальным данным/нормам; альтернатива generic-LLM hallucinations» — план **сам** учит, что альтернатива generic-AI — это **специализированный AI**, не «не-AI».
3. Anti-AI критерий AP2 — **формулировка корректна** («когда CV-система не выдерживает реальных условий, используй mechanical / GNSS-альтернативу»), но **примеры альтернатив смешивают** mechanical (Lemken, Kverneland) и GNSS (ИТЭЛМА) — это **два разных класса альтернатив**:
   - Mechanical — **не-AI** альтернатива (правильный использован anti-AI критерий).
   - GNSS — **другой класс AI** альтернатива (не-anti-AI критерий — это **AI architecture choice**).

**Evidence:**
- Research-04 R2 — ИТЭЛМА «обработка сигналов нескольких GNSS-созвездий» — это **inference / signal processing** = AI-class technology.
- Курс mission (CLAUDE.md) — «учить когда применять ИИ, а когда нет» — это о **критерии «когда не AI»**, требующем чёткой границы. «AI не нужен» когда **AI как класс не применим** (термодинамика vertical farming = closed problem). «Другой AI» когда **подзадача меняет архитектурный выбор** (CV vs sensor fusion).
- Cornerstone concept 4 «Tacit knowledge / hyperlocal context» — учит, что AI не может построить из satellite + IoT за 1 сезон. Это **другой случай** (AI не применим в принципе, нужен фермер с опытом). Cognitive Pilot vs ИТЭЛМА — **не этот случай**, и план их методически путает.

**Recommendation:**
1. **Перефразировать** «AI/CV не нужен, спутник проще» → **«CV не подходит к пыли, sensor fusion на multi-GNSS — корректный выбор для этого режима»** (или просто «**другой тип AI**»).
2. **Разделить AP2** в Р5.5 на 2 критерия:
   - **AP2a: «CV не выдерживает open-environment условий — используй mechanical / GNSS sensor-fusion AI» (architecture choice within AI domain).**
   - **AP2b: «Когда AI как класс не применим (термодинамика, fundamental physics) — используй не-AI» (vertical farming → открытый грунт; data center в Айове vs irrigation — direct measurement).**
3. **РФ-блок главный урок** — оставить «политический риск зависимости от импортного AI-стека», но **не использовать** Cognitive Pilot vs ИТЭЛМА как иллюстрацию этого урока. Это **другая история** (architecture choice CV vs sensor-fusion для open-environment); РФ-урок политического риска иллюстрируется лучше Мелитопольским кейсом + Climate FieldView выходом из РФ.

Это **сохраняет** методическую чёткость anti-AI критериев и **не путает** студента о том, что такое «не AI».

---

## P2 issues (polish)

### P2-1 — Anti-AI критерии AP1-AP5 vs AP6-AP7 «бонус» — методически AP6 и AP7 сильнее

**Где:** строки 359-367 (таблица anti-AI критериев).

**Проблема:** AP6 «vendor lock-in trap» и AP7 «AI-MRV для carbon claims без direct measurement» помечены как «бонус», but методически они **значительнее**:
- **AP6** — это **structural lesson** для любой AI-зависимой инфраструктуры (применим к L4 supply chain, к L7 healthcare, к L11 manufacturing). Это **cross-lecture takeaway**, не специфичный для АПК.
- **AP7** — это **lesson о уровне доверия к AI inference vs ground truth** (применим к любой AI-MRV / AI-prediction-as-metric ситуации). Концептуально pure.

AP1-AP5 (закон термодинамики; open environment + CV; threshold accuracy; generic LLM advisor; cloud-first для off-grid) — более конкретны под АПК. Они тоже сильные, но AP6+AP7 **должны быть в основной пятёрке**, не «бонус».

**Recommendation:** переставить — финальные 5 критериев в Р5.5: AP1 (термодинамика), AP3 (threshold accuracy), AP4 (generic LLM), AP6 (vendor lock-in), AP7 (AI-MRV). AP2 (CV в open environment — но с fix из P1-6 разбитый на AP2a/AP2b) и AP5 (cloud-first off-grid) — как «два дополнительных architectural критерия» в Р5.2 (connectivity sub-сек) и Р5.3 (vendor lock-in sub-сек), inline.

Это **сильнее align** с distributed retrieval (P1-2 рекомендация) — критерии становятся **закрывающим takeaway** каждой темы среды.

---

### P2-2 — Cornerstone concepts vs anti-AI критерии: дублирование

**Где:** строки 424-434 (cornerstone concepts) vs 359-367 (anti-AI критерии).

**Проблема:**
- Cornerstone 2 «Open-environment vs closed-loop AI» = AP1 (термодинамика для closed-loop vertical farming) + AP2 (open environment CV failure).
- Cornerstone 5 «Vendor lock-in / right-to-repair» = AP6 «vendor lock-in trap».
- Cornerstone 6 «Foundation model + grounded reasoning» = AP4 «generic LLM advisor» (RAG-grounded как альтернатива).
- Cornerstone 7 «Sustainability paradox» = AP7 «AI-MRV без direct measurement» (data center + carbon credits).

**4 из 7 cornerstone concepts** дублируются с anti-AI критериями. Это **не плохо** (anti-AI критерии **выводятся** из cornerstone concepts), но план **не делает** связь явной. Студент получает 2 списка по 7 пунктов, **которые на 60% overlap-ятся**.

**Recommendation:** в plan-v2 явно зафиксировать **mapping** cornerstone → anti-AI критерий, и в Phase 2 (chapter) обеспечить, что каждый cornerstone concept раскрывается через свой anti-AI критерий как «application». Это превращает 2 list-а в **1 system** (concept → application → assessment).

---

### P2-3 — Q&A budget: 5 min или 10 min?

**Где:** строки 5 + 261.

**Текст плана (строка 5):**
> «Duration: 75 мин + Q&A (~5 мин буфер)»

**Текст плана (строка 261):**
> «**Раздел 6 (опциональный) — Q&A (10 мин)**»

**Проблема:** в frontmatter — 5 мин буфер; в outline — 10 мин раздел. Math inconsistent. Если 75 мин = total content (Р0-Р5) + 10 мин Q&A, то total = 85 мин, но frontmatter говорит 75+5 = 80. Если 75 = total включая Q&A, то Р0-Р5 = 65 мин, но сумма Р0-Р5 = 5+14+15+10+12+14 = 70 мин.

**Recommendation:** зафиксировать в plan-v2: **75 мин total content (Р0-Р5) + 10 мин Q&A buffer = 85 мин full session**. Либо: **75 мин content + 5 мин fold-in Q&A в Р5.8** (сжать в 5-min total).

---

### P2-4 — Indigo Ag «НЕ в скандале» — отмечено в speech, но не выделено в plan structure

**Где:** строки 220.

**Текст плана:**
> «**Note:** Indigo Ag НЕ в скандале — использует Climate Action Reserve, менее controversial; 2M tons verified, Microsoft 12-year 2.85M tons deal.»

**Проблема:** этот note — important attribution для **избежания cherry-picking** в Verra phantom credits failure. Plan уже учитывает (правильно), but note **спрятан в outline section** Р4. Designer / writer на Phase 5/2 может **не заметить** и в slide / chapter использовать Indigo как пример «AI carbon-credits = scam», что было бы misattribution.

**Recommendation:** в plan-v2 явно вынести в **дополнительный раздел** «Misattribution warnings» (либо как footnote к References section), где зафиксировать:
- Indigo Ag — uses Climate Action Reserve, not Verra; не в Pachama-style scandal.
- Tract — data backbone, не agentic per se (план уже учитывает в anti-hype L4).
- Verra phantom credits — affects rainforest offset projects, не all AI-MRV; agricultural soil-carbon — другая методология.

Это предотвращает **cascade misattribution** в downstream artifacts.

---

### P2-5 — Hero s39 plan: 3 кандидата без чёткого primary

**Где:** строки 304-309.

**Проблема:** план предлагает 3 равноценных кандидата для s39 (Cargill BIG AI Award page; фотомонтаж Solinftec → полка Магнита; Carbon Robotics LaserWeeder iconic). Это **delegation Phase 5 designer-у без primary choice**. Lec-09 lesson — план **должен** decide primary + fallback, не оставить open для designer.

**Recommendation:**
- **Primary s39:** Carbon Robotics LaserWeeder G2 iconic image (Tier 1 single source, visually strongest, **single-frame**). Foreshadow Lec-11 через подпись «От поля до фабрики: AI-driven cyber-physical systems».
- **Fallback:** Cargill BIG AI Award page (Tier 2 less visual, but tied to Р4 как strongest L4 success).
- **Reject:** фотомонтаж — требует 2 lic + compositing risk; план уже флагирует.

---

## Strengths (что хорошо)

1. **Keystone-axis ENFORCED — полностью соблюдено** (строки 36-65). Заголовок keystone «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**» — про **саму ось**, НЕ про устройство курса / защиту подхода / recap. Каждый раздел = motivated подъём по оси. Лекция 4 lesson cost полностью предотвращена. Бонус: «closed-loop vs open-environment» injection как **explanatory mechanism** (строки 52-57) — sophisticated treatment, объясняющий **почему** на L1-L2 failure паттерны.

2. **Tools-per-taxonomy L4+ ENFORCED — соблюдено для всех 5 уровней** (строки 81-119):
   - L1: 5 international (Deere, Bayer, BASF, Syngenta, Taranis) + 3 РФ (ExactFarming, АгроСигнал, Прогресс Агро). Adoption направление, anti-hype «бренд ≠ режим работы», volatile-метки `[VFY-day-of]`.
   - L2: 8 international + 3 РФ. Anti-hype «demo ≠ production» + «specialization vs generic». Infrastructure (GNSS jamming, FCC DJI ban) **отделена**.
   - L3: 6 international + 2 РФ. Anti-hype Holstein-bias + small dairy economics + tie-stall barns (см. P1-4 для подробностей).
   - L4: 6+ international + 3 РФ. Anti-hype «agentic = narrow» + «Tract = data backbone, не agentic per se». Infrastructure (cloud + 1С) **отделена**.
   - L5: 5+ international + 2 РФ. Anti-hype «не agriculture-specific» — отличный note.
   - Infrastructure cross-cutting (строки 121-125) — **отделена** в свой блок s35 «Среда: связь, электроника, регуляторика». **Не AI capability — плитка под капабилитис.**

3. **Strict-in failure budget ≥30% — структурно достижимо** в каждом из 3 артефактов:
   - План: 40% time (30/75 мин); распределено холистически (Р1: 7 мин, Р2: 8, Р3: 3, Р4: 4, Р5: 8). No single-artifact concentration (но **single-section in Р2 — concern P1-3**).
   - Plan-self-report (строки 274-285) — **подтверждается независимо** (см. counter-check).

4. **РФ-блок встроен в каждый уровень параллельным треком** (строки 374-383) — **методически сильнее** отдельного «РФ-раздела в конце». 13-16% общего бюджета (план явно ниже L9 22-25%), что **намеренно** и для L10 reasonable (нет столь специфического РФ-narrative как ВКА Можайского в L9).

5. **Misattribution awareness** — план явно отмечает Indigo Ag «не в скандале» (P2-4 рекомендует усилить); Tract «data backbone, не agentic» (anti-hype L4); generic LLM «категорический антипаттерн» (AP4) — это **методически зрелое** обращение с research-02 fact-base.

6. **11 failure-блоков** (F1-F11) — каждый имеет explicit lesson + alternative. Это **research-driven**, не выдуманные. Все 10 failure-cases из research-02 summary §3 — в плане учтены (F12 CV edge cases — в P1-6 framing).

7. **Volatile числа корректно размечены `[VFY-day-of]`** на 5 уровнях (строки 87, 95, 103, 111, 119). Не оставлены на видимом слое для устаревания.

8. **Reading list (5.7)** — академически сильный (AIMA, McKinsey, Hannah Ritchie, Foodlore, Яков и Партнёры, FAO ATIO, Stanford GPS Lab, Cambridge EJRR). Балансирован: 3 academic + 3 industry/journalism + 2 RU. Anonymization-ready (нет ВУЗ-binding).

9. **Anonymization carry-forward** (строки 387-392) — explicit lesson Лекция 9 applied by default. «Профильные технические университеты + аграрные университеты» родовой формы — корректно для anonymized audience.

10. **Anti-anglicism carry-forward note** (строки 396-420) — Russification таблица обновлена с **АПК-specific** терминами (precision agriculture → точное земледелие; vertical farming → вертикальное земледелие; vendor lock-in → привязка к поставщику; demand forecasting → прогнозирование спроса; right-to-repair → право на ремонт). Это **методически сильно**, готово для Phase 2 brief.

---

## Recommendations (конкретные fixes с указанием строк)

| # | Issue | Строка | Fix |
|---|---|---|---|
| P1-1 | LO1 mixes Bloom-levels | 30 | Разбить на LO1a (Remember) + LO1b (Apply); итого 4 LO |
| P1-2 | Раздел 5 density-bomb (8 sub-сек × 1.75 мин) | 226-259 | Сжать payoff (5.6+5.7+5.8 в 2 мин); distribute 5 критериев по разделам как closing takeaway; либо расширить до 16-17 мин из Р3; либо вынести «среда» в отдельный Р4-bis |
| P1-3 | Vertical farming F1+F6 — Tortuga bridge натянут | 160, 182 | Объединить в 1 deep dive в Р1 (4-5 мин); убрать F6 из Р2; bridge Р1→Р2 переформулировать как «open vs closed environment failure summary» |
| P1-4 | Р3 «Животное» (10 мин, 4+2 кейсов) — overload | 189-206 | Расширить до 12 мин (сжать Р4); ИЛИ слить DeLaval+Cargill Birdoo в 1 «production-mature» блок |
| P1-5 | Hook A success-first — course mission requires failure-first | 136-141 | Switch primary к B (Plenty Compton split); fallback C (Cognitive Pilot vs пыль); A → в Р1 как working case opening |
| P1-6 | Cognitive Pilot vs ИТЭЛМА «AI не нужен» — подмена тезиса | 185, 364, 383 | Переформулировать в «CV vs sensor-fusion AI — architecture choice within AI domain»; разбить AP2 на AP2a (architecture) + AP2b (genuine не-AI); РФ-главный урок не использовать ИТЭЛМА как иллюстрацию политического риска |
| P2-1 | AP6+AP7 «бонус» — методически сильнее AP2+AP5 | 359-367 | Финальные 5 в Р5.5: AP1 (термодинамика), AP3 (threshold accuracy), AP4 (generic LLM), AP6 (vendor lock-in), AP7 (AI-MRV); AP2+AP5 — inline в Р5.2/5.3 |
| P2-2 | Cornerstone vs anti-AI критерии — 60% дублирование | 424-434 vs 359-367 | Явный mapping cornerstone → critically; в chapter каждый cornerstone развивается через свой anti-AI критерий |
| P2-3 | Q&A budget inconsistent (5 vs 10 мин) | 5 vs 261 | Зафиксировать: 75 мин content + 10 мин Q&A = 85 мин total |
| P2-4 | Indigo Ag misattribution warning спрятан | 220 | Вынести в отдельный раздел «Misattribution warnings» plan-v2 |
| P2-5 | Hero s39 — 3 кандидата без primary | 304-309 | Decide: Primary = Carbon Robotics LaserWeeder; Fallback = Cargill BIG AI Award; reject photomontage |

---

## Counter-check report

### AI-Failure ≥30% strict-in — PASS (структурно, with single-section concern)

**Independent verification (не верю plan-self-report 40%):**

| Раздел | Минут content | Strict-in минут (independent) | % strict-in |
|---|---|---|---|
| Р0 Keystone + roadmap | 5 | 0 | 0% |
| Р1 L1 «Поле» | 14 | 7 (F1 1 мин + F2 ChatGPT 3 + F3 Plantix 3) | 50% |
| Р2 L2 «Робот» | 15 | 8 (F4 Monarch 2 + F5 FarmWise 2 + F6 vertical 3 + F7 strawberry 1) | **53%** |
| Р3 L3 «Животное» | 10 | 3 (F8 Cainthus 1.5 + F9 РФ dairy 1.5) | 30% |
| Р4 L4 «Supply chain» | 12 | 4 (F10 USDA Climate-Smart 2 + F11 Verra 2) | 33% |
| Р5 L5 + среда | 14 | 8 (connectivity 3 + vendor lock-in 3 + regulatory 2; **5.1 L5 retail success + 5.5 критерии + 5.6-5.8 payoff — не strict-in**) | 57% |
| Q&A | 10 | — | — |
| **TOTAL active (75 мин)** | **75** | **30** | **40%** |

**Plan-self-report (40%) — подтверждается независимо.** Margin над 30% — comfortable.

**Однако:** Р2 53% и Р5 57% — **выше** «холистическое распределение» threshold (типовое 30-40%). Это означает 2 разделa **дают** >50% всего strict-in budget (16 из 30 мин = 53%). **Single-section concern** — strict-in концентрирован в 2 разделах из 5. **Counter-check passes по сумме (40% > 30%)**, но **distribution-wise** не идеально равномерно.

**Recommendation для distribution:**
- Если P1-3 принят (vertical farming → Р1 целиком), Р2 strict-in падает до 5 мин (Monarch + FarmWise + strawberry), Р1 strict-in растёт до 9 мин (F1 5 мин vertical + F2 + F3). Это **rebalances** к 60/40/30/33/57 — лучше, но Р5 всё ещё peak.
- Если P1-2 принят (5 критериев distributed как closing takeaway каждого раздела), strict-in **distribut-ся** ещё лучше — каждый раздел добавляет 30 сек strict-in critic takeaway.

**Холистичность across 3 артефактов** (plan-level promise):
- chapter ~40% слов — **PASS plan-level** (нужно verify Phase 3).
- slides ~40-44% strict-in slides из ~32 = 13-14 slides — **PASS plan-level**.
- speech ~30% (5k слов × 30% = 1500 слов) — **PASS plan-level**.

**Owner waiver:** L10 ∈ L4-L17 → waiver НЕ доступен. Strict-in ≥30% mandatory. **PASS** plan-level.

---

### Keystone-axis ENFORCED — PASS

Строки 36-65:
- Keystone slide = **отдельный s02** после cover/hook, ДО любого погружения ✓
- Заголовок «**Пять уровней лестницы. AI поднимается от поля к полке — и работает по-разному на каждом**» — про **саму ось**, НЕ про устройство курса / защиту подхода / recap ✓
- Каждый раздел = motivated подъём по оси (Р1→L1, Р2→L2, …, Р5→L5+среда) ✓
- «Closed-loop vs open-environment» injection как объяснительный механизм — корректное вложение, не отдельная ось ✓
- Visual: вертикальная лестница 5 ступеней + стрелка «↑ controllability ↑ ROI» — конкретное, не abstract ✓

Лекция 4 cost-of-omission (~5 циклов deck) **полностью предотвращена**.

---

### Tools-per-taxonomy L4+ ENFORCED — PASS (с P1-4 caveat для L3)

| Уровень оси | Tools 2026 (2-4+) | Adoption | Anti-hype | Volatile→`[VFY-day-of]` | Infra отделена | Mode ≠ brand |
|---|---|---|---|---|---|---|
| L1 «Поле» | 5 intl + 3 RU ✓ | растёт / стагнирует smallholders ✓ | «бренд ≠ режим работы», «AI advisory ≠ deep learning», US Midwest bias, vendor lock-in ✓ | See & Spray acreage, xarvio Japan rice, ExactFarming user count ✓ | Satellite/GNSS/connectivity отделено ✓ | «See & Spray» = AI-augmented selective spray, не «autonomous robot» ✓ |
| L2 «Робот» | 8 intl + 3 RU ✓ | растёт в нишах / стагнирует broadacre ✓ | «demo ≠ production» (Monarch), «specialization vs generic», strawberry $200-350k capex ✓ | LaserWeeder pricing, Solinftec deployments, Monarch fate, Cognitive Pilot count ✓ | GNSS-jamming, FCC DJI ban — отделено ✓ | autonomy ≠ brand-name (gradient explicit) ✓ |
| L3 «Животное» | 6 intl + 2 RU ✓ (но 4 working только 3-4 мин в Р3 — P1-4) | растёт стабильно + консолидация ✓ | Holstein bias, $30/cow/year overkill для small, tie-stall не подходит ✓ | SenseHub count, GEA Russia sanctions, DeLaval VMS attach-rate ✓ | Camera/cloud/mobile отделено ✓ | CV mode vs robotic milking mode ✓ |
| L4 «Supply chain» | 6+ intl + 3 RU ✓ | лидирует в production ✓ | «agentic = narrow», «Tract = data backbone не agentic per se», blockchain ≠ AI, РСХБ AI-сервисы declared production-метрики не опубликованы ✓ | Tract customer count, Cargill ML, X5 категории, Магнит F&R SKU ✓ | Cloud / FedRAMP / SAP отделено ✓ | agentic mode vs data backbone mode vs blockchain — все отделены ✓ |
| L5 «Потребитель» | 5+ intl + 2 RU ✓ | очень высокое ✓ | «не agriculture-specific» ✓ | waste reduction metrics ✓ | ERP/WMS/POS отделено ✓ | ML demand forecast vs blockchain payments — отделены ✓ |
| Infrastructure | (отдельный s35) | — | — | — | **Не AI capability — плитка под капабилитис, один слайд** ✓ | — |

**§-named speech-narrative → slide check** (строки 226-259, Раздел 5): 5.1 L5 retail → s30; 5.2 connectivity → s31; 5.3 vendor lock-in → s32; 5.4 regulatory → s33; 5.5 5 критериев → s34 (drawio); 5.6 career → s35; 5.7 reading → s36; 5.8 closing → s37. **No §-named narrative без слайда** ✓ (для media-coverage plan строки 318-346).

PASS с **P1-4 caveat** для L3 (4 working cases подogревают tools-per-taxonomy table, но 10-мин budget раздела ограничивает педагогическую обработку).

---

### Curriculum Relevance Check (per section)

L10 — **intermediate** уровень (Module 2, lectures 4-12). По decision matrix:
- Bloom level Apply (LO1b в P1-1 reformulation; LO2 ≥3 теста для assessment вендор-claim) — **KEEP** для intermediate.
- Bloom level Analyze (LO5 ≥5 критериев «когда не AI» с обоснованием) — **REVIEW** для intermediate; в L10 plan **обосновано** через 7 anti-AI критериев с примером и альтернативой каждый — это level Analyze (правильно для intermediate, не Evaluate).

**Curriculum mismatch check (forward-pointing content):**
- L4 «Supply chain» (R4) — **в данной L10** уместно (overview-level); глубокий agentic-engineering — L11+ (manufacturing).
- L5 «Потребитель / retail» (Р5.1) — **уместно**; глубокий retail AI = другая дисциплина, в L10 как «зрелый слой АПК-AI».
- Foundation models (TerraMind, Prithvi-EO 2.0) — **упомянуто 1 строкой** в L1 (через cornerstone 6), не deep dive — **корректное scope-cut**, не forward-pointing.
- ARC-AGI economics / Pearl 3 уровня causality / Tortuga harvest-robot deep technical specs — **scope-cut** в research-summary §6 — **корректно** для intermediate-лекции.

**Conclusion:** curriculum relevance **уместна** для intermediate (L10); нет forward-pointing concerns; нет concept-heavy content для introductory-level.

---

### Hook Engagement Quality Check

Для plan **3 hooks предложены**:
- **A (See & Spray BEFORE/AFTER):** time-evergreen (success устоит ≥12 мес); engaging visually; «висит на экране» worthy; connected к L1 working case — **OK по 4 из 5 критериев**; emotional engagement — слабо (existing success, no surprise).
- **B (Plenty Compton split-frame):** time-evergreen (failure factual); **сильно engaging** (драматичный contrast); «висит на экране» worthy (split-frame **более** visually rich); connected к keystone via failure mechanism; counter-example check vs Lec-9 BEFORE/AFTER sat = symmetric pattern (failure-first).
- **C (Cognitive Pilot vs пыль):** time-evergreen; engaging для RU-аудитории; «висит на экране» можно показать через field photo + court case headline; узко-РФ.

**Per CLAUDE.md AI-Failure mission — failure-first hook stronger для course mission alignment.** Lec-09 critique P2-2 уже зафиксировала. Lec-10 plan **повторяет** anti-pattern.

**Hook Engagement check verdict:** Hook A — **engaging quality fails** на «emotional engagement» критерии для course-mission. **P1-5 рекомендация** — switch к B primary.

---

### Missing-Fundamentals Check

Per L10 keystone-ось and concepts:
- **Foundation models (TerraMind, Prithvi-EO 2.0):** упомянуты в cornerstone 6 — **adequate brief** для overview-лекции; deeper coverage — Лекция 2/3 prerequisite ✓.
- **RAG-grounded reasoning:** упомянуто в AP4 alternative — **adequate** ✓.
- **Edge ML / TinyML:** cornerstone 3 + AP5 — **adequate** ✓.
- **CV в плане:** упомянуто как «компьютерное зрение» с разъяснением; pipeline (image → features → classification → action) не детализирован, но для overview-лекции **adequate** ✓.
- **GNSS / RTK:** упомянуто в L1 infrastructure; разъяснение в speech рекомендуется (cornerstone 6 нет dedicated, но через AP5 + s28 GNSS-jamming Финляндия map).
- **Multi-agent framework:** упомянуто в L4 (Cargill CMAX, Tract, Procuresprint); **adequate brief** для introduction.

**Missing fundamentals concerns:** нет P1-level missing. **OK** for plan-v1.

---

### Term Canonical-Validity Check

Sample terms из плана:
- **«Precision agriculture / точное земледелие»** — canonical (Wikipedia, FAO, EU CAP) ✓.
- **«Vertical farming / вертикальное земледелие»** — canonical (Wikipedia, IDFA) ✓.
- **«Agentic AI / агентный ИИ»** — emerging canonical (Gartner 2024, McKinsey 2025) ✓.
- **«Edge ML / TinyML»** — canonical (Pete Warden 2018, tinyML Foundation) ✓.
- **«Vendor lock-in / привязка к поставщику»** — canonical (Eric S. Raymond, GNU) ✓.
- **«Open-environment vs closed-loop AI»** — **insider phrasing**, не canonical. План `сам` явно ввоdит как cornerstone 2 — это OK для **course-internal taxonomy**, но в chapter / speech нужно при первом упоминании сказать «**наша рабочая формулировка** для разделения сред», иначе студент будет искать в литературе и не найдёт. **P3 note** (не P1).
- **«Tacit knowledge / hyperlocal context»** — canonical (Polanyi 1966 «tacit knowledge») ✓; «hyperlocal context» — descriptive, не term-of-art, но clear.

**Conclusion:** no P1-level term issues. One P3 note для «open-environment vs closed-loop» introduction phrasing в chapter.

---

### Tools / Benchmark Freshness Check

Sampling plan-named tools и метрик:
- **See & Spray 5M acres** (строка 84) — November 2025 source ✓; refresh cadence agricultural metric = **annually**; «verify on day-of-lecture» — да, but updates ≤ once/year — **stable** до Phase 8 design ✓ `[VFY-day-of]` marked correctly.
- **Plenty Compton closure** (декабрь 2024) — facts ✓; refresh cadence — N/A (historical fact); **stable**.
- **Monarch Tractor лажa** (ноябрь 2025) — TechCrunch source ✓; refresh cadence weekly during active lawsuit; «verify on day-of-lecture» **mandatory** ✓ — план явно marked.
- **xarvio FIELD MANAGER 130k фермеров** (строка 84) — September 2025 source; refresh cadence quarterly — **stable** до Phase 8 ✓.
- **Cognitive Pilot 1200+ установок** (строка 91) — Q1 2024 source; cadence yearly enterprise self-report — **plan markedд** `[VFY-day-of]` ✓.
- **GNSS-jamming >122 000 авиа-рейсов Q1 2025** (строка 94) — Stanford ITM 2025 paper; refresh cadence quarterly — **stable** ≤ ~6 мес ✓.

**Freshness:** all `[VFY-day-of]` markers корректно расставлены. Нет stale-claim concerns на plan-level.

---

### Holistic across 3 artifacts (plan-level promise)

- chapter strict-in target 40% слов — committed in plan, **verifiable Phase 3**.
- slides strict-in target 40-44% — committed, **verifiable Phase 7**.
- speech strict-in target ≥30% — committed plan-level, **verifiable Phase 10**.

**Plan-level: PASS.** Actual will be re-checked in Phases 3, 7, 10. Если на любой phase actual <30% или single-artifact concentration → verdict REVISE.

---

## Verdict justification

- **0 P0** issues.
- **6 P1** issues — LO Bloom-mix, Раздел 5 density-bomb, vertical farming split (Tortuga bridge натянут), Р3 overload, Hook A success-first vs course mission, Cognitive Pilot vs ИТЭЛМА подмена тезиса.
- **5 P2** issues — polish.

**Counter-check (CLAUDE.md ENFORCED):** ≥5 P1 issues → **REVISE** (не APPROVE-WITH-POLISH).

**Phase 2 (chapter draft) — НЕ рекомендуется начинать** без устранения хотя бы P1-1 (LO разбить), P1-5 (Hook switch к B failure-first), P1-6 (Cognitive Pilot framing fix). Эти 3 — **critical для downstream consistency** (LO формат feed-ит chapter LO list; Hook framing feed-ит cover slide design в Phase 5; Cognitive Pilot framing feed-ит anti-AI критерии в chapter + speech + slides).

P1-2 (Раздел 5 pacing), P1-3 (vertical farming consolidation), P1-4 (Р3 weight) — **могут быть решены в Phase 2 brief** как explicit instructions для book-editor, но **сильнее** — в plan-v2 минимальной редактурой outline.

**Не рекомендуется** возвращать в Phase 1 для полной переработки — структурно plan v1 крепкий, исправления **локализованы** в 6 sections без структурного перепланирования.

**Recommendation для plan-v2:**
1. **Critical fixes** (P1-1, P1-5, P1-6) — обязательно перед Phase 2.
2. **Structural fixes** (P1-2, P1-3, P1-4) — обязательно перед Phase 2, либо явные explicit instructions в Phase 2 brief.
3. **Polish** (P2-1, P2-2, P2-3, P2-4, P2-5) — fix в plan-v2 при возможности; иначе flag для Phase 3 critic.

После plan-v2 — повторный methodology-critic за 15 мин (узкий focus на 6 P1 + counter-check distribution).

---
lecture: 17
title: "Лекция 17. Систематизация знаний и навыков — инженерная карта AI"
module: 3
issue: 145
branch: issue-145-lec-17
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
duration_min: 75
date: 2026-05-27
status: approved (GATE A 2026-05-27 + orchestrator corrections — see § "GATE A Decisions" в начале файла)
version: v1.1
learning_outcomes:
  - LO1: "Сформулировать главный диагностический вопрос курса («Где AI работает, где — нет, и как это понять?») и обосновать его как несущий навык инженера 2026 года, противопоставленного «инструктору ИИ»."
  - LO2: "Применить 7 критериев AI/non-AI decision к незнакомому учебному кейсу из произвольной отрасли (включая не разобранную в курсе) и сформулировать verdict «применять / не применять / применять с HITL» с обоснованием."
  - LO3: "Разместить произвольную отраслевую задачу на 2D-плоскости «AI fit × Лестница автономии L0→L5» и обосновать координату через cornerstone-концепты курса (closed/open environment, ground-truth availability, blast radius)."
  - LO4: "Перечислить минимум 8 канонических классов провалов AI из курса и для каждого назвать (а) выученный урок, (б) более правильную альтернативу (не-AI или другой класс AI)."
  - LO5: "Применять лестницу автономии L0→L5 к произвольному AI-применению; различать advisory / supervised / conditional / high / full autonomy + criteria подъёма на следующую ступень."
  - LO6: "Использовать 4 cheat-sheets (Decision matrix / Autonomy ladder / Failure-modes / 16-industry map) как practical reference в инженерной работе после курса."
  - LO7: "Сформулировать собственную профессиональную траекторию относительно AI-карьерной арки (specialist who knows when NOT to use AI), различая её от «AI engineer» и «prompt engineer» как marketing-категорий."
  - LO8: "Связно изложить путь курса — 16 отраслей как 16 точек одной концептуальной карты — и объяснить выпускнику технического вуза, почему «знать ИИ» означает «знать его границы»."
keystone_axis: "2D-плоскость инженерной карты AI: горизонталь = AI fit (от детерминированный non-AI до full AI); вертикаль = Лестница автономии L0→L5 (advisory → fully autonomous). Все 16 отраслей курса наносятся как точки. Синтез OODA (L9) + Лестницы L1-L5 (L10) + A0-A3 (L12) + Видит-Решает-Действует (L14) + 5-уровневая structuredness (L13) в единую autonomy-шкалу."
failure_share_target: 0.32
chapter_target_words: 30000
slides_target_count: 40 (s01-s40; включая dedicated Q&A s39 + closing hero s40)
slides_media_target_share: 0.55
hero_slides: [s01, s39]
cheatsheets:
  - id: a4-1
    title: "Decision matrix «AI / не-AI» — 7 критериев"
    layout: "A4 portrait; 7 строк × (вопрос + критерий + AI/non-AI/HITL индикатор + пример из курса)"
  - id: a4-2
    title: "Autonomy ladder L0→L5 + rules для подъёма"
    layout: "A4 portrait; 6 строк × (уровень + что AI делает + кто решает + criteria подъёма + пример курса + альтернатива non-AI)"
  - id: a4-3
    title: "Failure-modes & antidotes — топ-12 провалов курса"
    layout: "A4 portrait; 12 строк × (имя провала + источник лекции + урок одной фразой + альтернатива)"
  - id: a1-master
    title: "Карта 16 отраслей × keystone-плоскость"
    layout: "A1 landscape; 2D scatter plot 16 точек + цветовое кодирование по модулям курса + аннотация ключевого failure на каждую точку"
strict_in_self_estimate:
  chapter_words: "~10 000 strict-in из 30 000 = 33%"
  slides_count: "~13 strict-in из 41 = 32%"
  speech_minutes: "~25 strict-in из 75 = 33%"
  distribution: "Раздел 1 (full AI/non-AI critical analysis) ≈ 100% strict-in; Раздел 4 (failures каталог) ≈ 100%; Раздел 3 (per-industry border analysis) ≈ 40%; Раздел 5 (cheat-sheets reveal) ≈ 50% strict-in (через failure-modes sheet + autonomy criteria); Раздел 2 ≈ 20% (autonomy ladder сама не failure, но criteria подъёма — failure-bucket)."
prerequisites:
  - "lec-01 типы AI + AI Effect + Pearl 3 уровня + diagnostic questions"
  - "lec-09 OODA-keystone + HITL/HOOL/HOTL + L1-L5 autonomy"
  - "lec-10 Лестница АПК + closed-loop vs open-environment"
  - "lec-11 pilot purgatory + дискретное/процессное"
  - "lec-12 A0→A3 + digital twin как мост"
  - "lec-13 Лестница среды 5 уровней + ODD + classical OR альтернативы"
  - "lec-14 Видит→Решает→Действует + 3 уточняющих вопроса вендору + MITRE ATLAS"
references_count_target: "60-80 (агрегированные из L1-L16 plus 5-10 синтетических работ — Russell&Norvig 2021, Goodfellow 2016, EU AI Act 2024, NIST AI RMF 2023, ISO/IEC 22989, плюс meta-обзоры Stanford AI Index 2026 / McKinsey State of AI 2025)"
---

## GATE A Decisions (2026-05-27 — owner approved + orchestrator corrections)

**Owner verdict:** Approve plan v1 + 5 orchestrator-corrections → Phase 2.
**Cheat-sheet output format (decision):** **PowerPoint slides → PDF export** (3 A4 portrait через portrait-orientation slides + LibreOffice export; A1 master-poster — large-format PPT slide ИЛИ Inkscape backup при необходимости). PowerPoint MCP pipeline уже работает в проекте.

### Orchestrator corrections (apply при chapter draft + slides design)

**C1 · Q&A slide добавлен (P1).** Outline теперь s38 (cheat-sheet #4) → **s39 (Q&A dedicated)** → **s40 (closing hero)**. Slide count = 40. Соответствует Lec-14 (Q&A pattern) + Lec-13 (Q&A pattern).

**C2 · Cornerstone glossary appendix добавлен (P1).** Chapter получает отдельную секцию-словарь в части 4 (или appendix): **~16-20 cornerstone терминов курса** с краткими определениями + lecture-back-references. Терминология: AI Effect (L1), Pearl 3 уровня (L1), OODA (L9), HITL/HOOL/HOTL (L9), ODD (L13), pilot purgatory (L11), closed-loop / open-environment (L7, L10, L13), reliability compounding (L3, L4), slopsquatting (L4), soft sensor (L11), digital twin (L12), foundation model (L2), MITRE ATLAS (L14), distribution shift (L5, L10), ground-truth feedback loop (L1, L4, L7), HITL design (boring → не работает) (L9, L13). НЕ обязателен отдельный slide — cornerstones раскрываются inline в R0-R4. Glossary как **chapter-part4 § Словарь курса**.

**C3 · Pilot purgatory unification (P1).** В chapter и в Failure #12 на cheat-sheet — явно унифицировать 3 источника:
- L1 РФ — «9 из 10 пилотов не доходят до production (ВЦИОМ + Strategy Partners, 2024-2025, РФ-данные)»
- L11 — «MIT Sloan 2025: только 5.5% generative AI пилотов производят measurable revenue impact»
- L12 — «75% digital twin внедрений stuck в research / lab phase (industry survey 2024)»
Студент получает **разброс + контекст**, не одно «магическое число». Это P1 «missing context» из baseline mandate.

**C4 · Hero s01 упрощён (P1).** Plan-v1 предлагал composite «16 icon grid + 2D scatter» — это рискованно для presentation-designer (lec-8/9 lesson: custom composites coherence problems). **Замена:** **single iconic clean 2D scatter plot** — крупный, минималистичный, цветной по модулям курса, 16-20 точек (некоторые отрасли — multi-dot для bimodal nature), на тёмном/градиентном фоне Ocean palette. Title overlay: «Что у тебя осталось после курса» (italic). Это **сильнее как single image** — meditative, focused. 16-icon grid переезжает на s02 («Карта 16 лекций» miniature grid) — там она органична.

**C5 · Callbacks расширены до 16 (P1).** Plan-v1 имел 12 callbacks; missing L8, L12, L13, L16. **Добавить 4:**
- L8 → «Getty v. Stability — verbatim training data leak» (cross-link к failure #9)
- L12 → «Digital twin как мост от A1 к A3 — нельзя пропустить ступени» (Toyota Digit / Cassie anchor)
- L13 → «5-level structuredness среды — warehouse L4 vs urban L3» (ODD anchor)
- L16 → «Subsurface knowledge vault — physics-informed AI границы; pet-rock LLM-чатбот не заменит геолога» (regulated industry anchor)

Итого 16 callbacks — по 1 на каждую лекцию.

### Owner-recommendations applied (7 open questions)

1. **L0→L5 autonomy** — confirmed (как plan v1)
2. **2D-плоскость RU naming** — «Применимость ИИ × Автономия» (с «AI fit» в скобках при первом упоминании)
3. **Top-12 провалов** — confirmed как есть
4. **Cheat-sheet output** — PowerPoint export (см. выше)
5. **Hero direction** — s01 упростить (C4); s39 silhouette OK
6. **Anonymization** — universal audience confirmed; никаких ИУ-6 / МГТУ / МАИ / ВКА; «профильные технические университеты» родовое
7. **Callbacks** — расширить до 16 (C5)

### Brief для Phase 2 (book-editor)

При chapter draft:
- Target **≥30 000 слов** (multi-part split: chapter.md + chapter-part2.md + chapter-part3.md + chapter-part4.md; каждый ≤600 строк CLAUDE.md doc-size limit)
- Раздел 0 (s01-s05): hook + keystone reveal — ~3 000 слов
- Раздел 1 (s06-s12, 7 критериев): ~6 500 слов (strict-in ≈ 100%)
- Раздел 2 (s13-s20, лестница автономии): ~7 000 слов (strict-in ≈ 20%, но antipatterns ≈ 100%)
- Раздел 3 (s21-s28, карта 16): ~5 500 слов (strict-in ≈ 40% per-industry border)
- Раздел 4 (s29-s33, 12 провалов): ~5 500 слов (strict-in ≈ 100%)
- Раздел 5 (s34-s40, cheat-sheets + closing): ~2 500 слов (strict-in ≈ 50%)
- **Cornerstone glossary appendix:** ~500-1000 слов (НЕ засчитывается как narrative для 30k — это appendix)
- Q&A backup section в конце части 4: ~1500 слов (тоже appendix-like)
- Сумма narrative body: ~30 000 слов
- **AI-Failure strict-in: ≥30%, target 33%** holistically (R1 + R4 = full strict-in; R3 + R5 partial)
- Frontmatter включает `parts: 4`, `length_words: ~30k`, `slide_map`, `strict_in_self_estimate`, `lo: [LO1..LO8]`
- Каждый ≥150-слов раздел получает slide-маркер `[for-slide-sNN]` для Phase 5 anchor
- Russification anti-anglicism mandate (см. § Russification plan в этом файле)
- Anonymization (no named institutions; universal audience)
- Baseline / counterfactual для каждого measurable claim (см. C3 pilot purgatory + другие drift cases)

---

## Несущая ось → keystone (ENFORCED)

### Формулировка одной фразой

**2D-плоскость инженерной карты AI:**
- **горизонталь (X)** — **AI fit**, континуум от детерминированного non-AI инструмента (rule-based / OR / classical signal processing) до full AI (foundation model в режиме end-to-end);
- **вертикаль (Y)** — **Лестница автономии L0→L5** в адаптации для capstone (L0 без автономии → L5 полная автономия в любых условиях).

Все 16 отраслей курса наносятся на эту плоскость **в виде точечной диаграммы (scatter plot)**, и большинство отраслей образуют не одну точку, а **облако точек** — потому что разные задачи внутри одной отрасли занимают разные координаты.

### Почему эта ось синтезирует курс

Курс начинается с AI Effect (L1) — определения AI постоянно сдвигаются, и инженеру нельзя строить навык вокруг технологии. Курс заканчивается тем, что есть **стабильная 2D-структура**, на которой можно расположить ЛЮБУЮ AI-задачу (включая отрасли, не разобранные в курсе) и принять обоснованное инженерное решение «применять / не применять / применять с HITL».

Каждая отраслевая лекция курса (L4-L16) поднимала свою «локальную» ось:
- L4 — A/B/C/D ступени автономии в SE
- L9 — OODA + L1-L5
- L10 — Лестница АПК L1-L5 (поле → потребитель)
- L11 — Дискретное vs Процессное
- L12 — A0→A3 + digital twin
- L13 — 5-уровневая structuredness среды
- L14 — Видит → Решает → Действует
- L15 — Лестница научного цикла (Hypothesis → Review)
- L16 — Матрица 2×2 data × process

Capstone **унифицирует** все эти оси в одну autonomy-шкалу L0→L5 (с явным mapping каждой лекции-специфичной нумерации в общую) + добавляет ортогональную ось AI fit, которая отвечает на вопрос **«а нужно ли вообще AI»**.

### Mapping локальных шкал в единую L0→L5

| Capstone L0→L5 | L4 SE | L9 aero | L12 manuf | L14 cyber | L13 logistics |
|---|---|---|---|---|---|
| L0 без автомат. | — | — | A0 наблюдать (часть) | — | — |
| L1 advisory | A autocomplete | L1 assistive | A1 советовать | Видит | контролируемая среда |
| L2 supervised | B mid-task | L2 supervised | A2 (часть) | (рамка) | полуструктурированная |
| L3 conditional | C PR-from-spec | L3 conditional | A2 замыкать | Решает | городская улица |
| L4 high | D engineer-agent | L4 high | A3 пилот | (rare) | последняя миля |
| L5 full | (не доступен) | L5 dual-use | (rare) | Действует (rare) | (failed в open env) |

Это mapping не precise; это conceptual scaffold, который позволяет студенту переносить опыт одной отрасли на другую через единый словарь.

### Keystone-слайд требование (Раздел 0)

s03 — keystone-slide в Разделе 0 ДО первого погружения. Заголовок строго: **«2D-карта AI: applicability × autonomy»** (или russified «Карта применимости AI: подходит × автономия»). Первая строка — про саму ось, НЕ recap курса, НЕ защита подхода. Тип слайда — schema (axes + 3-5 sample dots уже видны).

---

## Outline (5 разделов + Раздел 0, 39-41 слайд, 75 мин)

### Раздел 0 — Hook + keystone reveal (s01-s05, ~7 мин)

- **s01: Hero — iconic visual.** Концепт: side-by-side композит **«Карта AI после курса»**: с одной стороны — 16 отраслевых иконок (логотипы / icons модулей), с другой стороны — 2D-scatter plot с 16 dots. Acquisition via 6-tier (best Tier 2 — Wikipedia composite + custom-rendered scatter). ≥40% area. Title под hero: «Курс закончен. Что ты теперь знаешь?» (single line, italic).
- **s02: «Чему вы научились — карта 16 лекций».** 16 миниатюрных карточек (4×4 grid), каждая = 1 лекция, на каждой — keystone-ось этой лекции одной фразой («L4 — A/B/C/D ladder», «L9 — OODA», «L13 — 5-level structuredness» и т.д.). Это **визуальное foreshadowing** того, что все эти оси сливаются в одну.
- **s03: Keystone-slide — 2D-плоскость.** Чистый scatter plot: оси X (AI fit) и Y (Autonomy L0-L5); пока без точек, просто оси с подписями квадрантов. Тип — schema. Это **несущая ось всего capstone**, предъявленная до первого погружения.
- **s04: «Главный вопрос курса» — re-asked.** Слайд с большим текстом: «Где AI работает, где — нет, и как это понять?» — повтор из L1, теперь как **диагностический инструмент**, не открытый вопрос.
- **s05: Roadmap лекции.** 5 разделов с tag-меткой каждого («7 критериев», «лестница», «карта 16», «12 провалов», «cheat-sheets reveal») — БЕЗ минут (per No-Timing rule).

### Раздел 1 — Когда AI применять, когда нет: 7 критериев (s06-s12, ~13 мин)

**Strict-in:** ~100% (целиком про когда AI не нужен / границы).

- **s06: Введение раздела.** «Не все задачи — для AI. Какие — для AI, какие — для non-AI?» Cross-callback к L1 (диагностический вопрос), L6 (6 классов CAD с «когда не применим»), L10 (5 анти-AI критериев агро).
- **s07: 7 критериев — overview.** Список 1-7 на одном слайде. Это будет рамка для слайдов s08-s12.
- **s08: Критерий 1+2 — Closed-loop vs open-environment / Training data.** Two-column slide. Слева — closed-loop (медицина L7, склад L13 L1, See & Spray L10). Справа — open-environment (Zillow L5, Monarch L10, urban robotaxi L13 L3). Cross-lecture cases.
- **s09: Критерий 3+4 — Repeatability / volume / cost-of-error.** SE high-repeatability ↑ (L4); aerospace high cost-of-error → HITL (L9, F-35 ALIS).
- **s10: Критерий 5+6 — Ground-truth availability / Explainability + audit.** Pearl level 3 limits (L1); EU AI Act + FDA mandates (L7, L14).
- **s11: Критерий 7 — Economic case vs baseline alternative.** UPS ORION OR vs ML (L13); MPC vs RL (L11); LaserWeeder (L10) — узкая задача с измеримой альтернативой.
- **s12: Worked example.** Учебный кейс (не из курса): «Вендор предлагает AI для оптимизации расхода воды в ЖКХ города». Проходим 7 критериев → verdict с обоснованием. Это **applied LO2**.

### Раздел 2 — Лестница автономии L0→L5 (s13-s20, ~15 мин)

**Strict-in:** ~20% (autonomy ladder сама — рамка, но criteria подъёма + provals на каждом уровне — failure-bucket).

- **s13: Section divider.** «Лестница автономии: L0 → L5» + tag «6 ступеней · cross-industry mapping» (БЕЗ минут).
- **s14: Лестница full reveal.** Vertical stack 6 уровней с одной фразой описания + иконка. L0 (без автоматизации) / L1 (advisory) / L2 (supervised) / L3 (conditional) / L4 (high) / L5 (full).
- **s15: Mapping table.** «Локальные шкалы курса → единая L0→L5» — таблица из плана выше (L4 SE / L9 aero / L12 manuf / L14 cyber / L13 logistics).
- **s16: L1 advisory — deep dive.** Что AI делает (классифицирует, предсказывает, рекомендует), кто решает (человек always), criteria подъёма на L2 (baseline measured + change-control + rollback). Примеры курса — Stripe Radar (L5), Aidoc (L7), Crop Wizard (L10).
- **s17: L2-L3 supervised + conditional — deep dive.** Yokogawa FKDPP (L12), Mobileye Chauffeur L3 (L13), GitHub Copilot agent-mode (L4). Criteria подъёма на L4 — sim-to-real + canary + go/no-go.
- **s18: L4-L5 high + full — deep dive.** Waymo L4 (L13), See & Spray в narrow ODD (L10), Toyota Digit pilot (L12). Criteria для L5 — почти нет в production 2026 кроме contained narrow scenarios.
- **s19: Antipatterns на каждом уровне.** L1 → Klarna AI CS overreach (L5); L2 → Uber Tempe HITL distracted (L13); L3 → Cruise ODD expansion (L13); L4 → CrowdStrike BSOD (L14); L5 → LAWS debate (L9).
- **s20: Worked example.** «Школьная задача: AI-помощник для приёма экзаменов». Проходим лестницу → на каком уровне? Какой следующий gate?

### Раздел 3 — Карта 16 отраслей на 2D-плоскости (s21-s28, ~15 мин)

**Strict-in:** ~40% (per-industry border analysis = where AI fits and where doesn't).

- **s21: Section divider.** «16 отраслей на одной карте» + tag «scatter plot · 1 plane · 1 view».
- **s22: Map reveal — initial state.** 2D-плоскость с **первыми 4 точками** (L4 SE, L5 финансы, L7 медицина, L9 aero). Каждая точка — small icon отрасли + 1-line aннотация.
- **s23: Map reveal — middle batch.** Добавляются L6 CAD, L8 креатив, L10 агро, L11 manufacturing. Видны два cluster: «mid AI fit + L1-L3 autonomy» большинство; «high AI fit + L3-L4 autonomy» — IT-adjacent (SE, fraud).
- **s24: Map reveal — final batch.** L12 automation, L13 logistics, L14 cyber, L15 science, L16 oil/gas. Видна **bimodal nature** некоторых отраслей — например L13 (warehouse L4 vs robotaxi L3 vs black swan L0).
- **s25: Cluster analysis 1 — closed-loop quadrant.** Кто в upper-right? Software / fraud / closed-loop CV. Что общего — ground-truth feedback fast + repeatable.
- **s26: Cluster analysis 2 — open-environment quadrant.** Кто в lower-left? Open agro (Monarch), Plenty VF, urban robotaxi, black swan. Что общего — distribution shift + adversarial environment.
- **s27: Cluster analysis 3 — high-stakes mid-fit.** Aerospace, медицина, manufacturing safety-critical. AI fit есть, но autonomy capped at L1-L2 by regulatory/cost-of-error.
- **s28: Карта — empty quadrants.** Upper-left (high autonomy + low AI fit) — где? Lower-right (low autonomy + high AI fit) — где? Эти quadrants foreshadow «где AI избыточен» или «где autonomy не оправдана».

### Раздел 4 — Топ-12 провалов AI курса + уроки (s29-s33, ~13 мин)

**Strict-in:** ~100% (целиком failure deep-dive).

- **s29: Section divider.** «12 провалов курса. Что мы выучили?» + tag «cross-industry · lessons → criteria · alternatives».
- **s30: Провалы 1-4 — open-world prediction + reliability compounding + demo≠production + HITL boring.** Card-grid layout. Каждый провал = 1 card (название / лекция / урок / альтернатива).
- **s31: Провалы 5-8 — excessive automation + Act-without-canary + Galactica + voice/chat overpromise.** Card-grid.
- **s32: Провалы 9-12 — IP leak + vendor lock-in + slopsquatting + pilot purgatory.** Card-grid.
- **s33: Synthesis — паттерны провалов.** 3 mega-pattern: (a) AI applied beyond closed-loop boundary, (b) HITL design flawed (boring or absent), (c) economic/regulatory baseline ignored. Это **anchor для cheat-sheet #3**.

### Раздел 5 — Cheat-sheets reveal + practical conclusion (s34-s39, ~12 мин)

**Strict-in:** ~50% (failure-modes sheet = 100%; decision matrix = 100% strict; autonomy ladder = 30%; 16-industry map = 30%).

- **s34: «Что вы возьмёте с собой» — overview cheatsheets.** 4 cheat-sheets thumbnail (3 A4 + 1 A1) + где их найти (link в репозитории).
- **s35: Cheat-sheet #1 — Decision matrix (7 критериев).** Полноэкранный preview A4. Студент может прочитать; есть large QR-код в углу со ссылкой на PDF.
- **s36: Cheat-sheet #2 — Autonomy ladder.** Preview A4.
- **s37: Cheat-sheet #3 — Failure-modes & antidotes.** Preview A4. Это **главный** sheet — практически каждый из 12 провалов = inoculation против реальной ошибки на работе.
- **s38: Cheat-sheet #4 (A1) — карта 16 отраслей.** Preview A1 master poster.
- **s39: Hero closing.** Иконическая иллюстрация: концепт **«Инженер с картой»** — silhouette figure looking at скан-нанесённая карта 16 точек, с overlay text **«Знать ИИ — значит знать его границы»**. ≥40% area. Bridge к career — не «AI engineer», а «engineer who can choose when AI». Acquisition via 6-tier.

---

## Cheat-sheets detailed layouts

### Cheat-sheet #1 (A4 portrait) — Decision matrix «AI / не-AI»

**Layout (~A4 portrait, 1 страница):**

- **Header.** Title (large): «Применять ли AI? — 7 критериев». Subtitle (small): «Capstone курса AI-usage-lessons. v1.0».
- **Body.** Table 7 rows × 4 columns:
  - Col 1: № критерия (1-7).
  - Col 2: Вопрос (1 строка, formulated as student's checkbox).
  - Col 3: Verdict-индикатор (3 значка: AI ✓ / non-AI ✗ / HITL ⚠).
  - Col 4: Пример из курса (1 строка с указанием отрасли).
- **7 строк (черновик):**
  1. «Среда контролируемая или закрытая петля?» — closed-loop ✓ / open ⚠ или ✗ — «See & Spray (L10) ✓; Monarch (L10) ✗».
  2. «Достаточно training data + matches deployment?» — ✓ / ⚠ — «Epic Sepsis (L7) ✗».
  3. «Задача repeatable + high volume?» — ✓ / ✗ — «UPS ORION OR vs ML (L13)».
  4. «Cost-of-error приемлем для AI?» — ✓ / ⚠ HITL / ✗ — «F-35 ALIS (L9) ⚠; CrowdStrike (L14) ✗».
  5. «Ground-truth feedback быстрый?» — ✓ / ✗ — «Compiler в SE (L4) ✓; iBuying (L5) ✗».
  6. «Explainability нужен?» — ⚠ или ✗ если нет SHAP/LIME — «Apple Card bias (L5) ✗».
  7. «AI окупается vs baseline alternative?» — ✓ / ✗ — «MPC vs RL (L11)».
- **Footer.** Small text: «Если хотя бы 1 ответ ✗ — STOP. Если ≥2 ⚠ — STOP, обоснуй HITL. Все 7 ✓ — proceed с pilot.»

### Cheat-sheet #2 (A4 portrait) — Autonomy ladder L0→L5 + rules

**Layout (~A4 portrait):**

- **Header.** «Лестница автономии AI — 6 ступеней».
- **Body.** Table 6 rows × 5 columns:
  - Col 1: Уровень (L0-L5).
  - Col 2: Название (RU).
  - Col 3: Что AI делает.
  - Col 4: Кто решает.
  - Col 5: Criteria подъёма на следующий уровень.
- **6 строк (черновик):**
  - **L0 — Без автоматизации.** Нет AI. Человек. Criteria: baseline данные собраны.
  - **L1 — Advisory.** Классифицирует / предсказывает. Человек always. Criteria: baseline → AI improvement измеряется + change-control + rollback готов.
  - **L2 — Supervised.** Действует, человек ratifies каждое действие. Criteria: false-positive rate baseline + canary deploy + 1-click rollback.
  - **L3 — Conditional.** Действует в narrow ODD. HOOL (на петле, не в петле). Criteria: ODD formal definition + telemetry + go/no-go gate.
  - **L4 — High.** Действует в широком ODD. HOTL (вне петли) для большинства. Criteria: 99.9%+ reliability + insurance + regulatory clearance.
  - **L5 — Full.** Любые условия. AI решает. Criteria: для большинства отраслей **не доступен в 2026**; единичные narrow scenarios.
- **Footer.** Box: «Антипаттерн — пропуск ступени. Если хочешь A→A3 (Toyota Digit), нужно сначала A0-A1-A2 + digital twin как мост (см. L12).»

### Cheat-sheet #3 (A4 portrait) — Failure-modes & antidotes

**Layout (~A4 portrait, possibly landscape если 12 строк не влезают):**

- **Header.** «12 провалов AI из курса — уроки и альтернативы».
- **Body.** Table 12 rows × 4 columns:
  - Col 1: Имя провала.
  - Col 2: Источник (лекция + год + ссылка-style).
  - Col 3: Урок (1 строка).
  - Col 4: Альтернатива.
- **12 строк** — см. cross-lecture failure patterns в extracts file:
  1. Open-world prediction без closed-loop (Zillow L5, Monarch L10, urban robotaxi L13)
  2. Reliability compounding в multi-step agent ($4,200-петля L3, agentic SE L4)
  3. Vendor demo ≠ production (Devin L4, IBM Watson L7, Epic Sepsis L7, Klarna L5)
  4. HITL boring → не работает (Uber Tempe L13, F-35 ALIS L9)
  5. Excessive automation в зонах человеческой variability (Tesla 2018 L11, Boeing MAX 9 L11)
  6. Act-level autonomy без canary + rollback (CrowdStrike L14, Cloudflare L14)
  7. Galactica-class scientific hallucination (Meta Galactica L15, citation hallucinations)
  8. Voice / chat fraud / overpromise (Wendy's L5, Air Canada L5, deepfake L8)
  9. Verbatim training data leak (Getty v. Stability L8, NYT v. OpenAI L8)
  10. Vendor lock-in для regulated industries (Climate FieldView L10, F-35 ALIS L9, JEDI L9)
  11. Slopsquatting / hallucinated supply-chain (L4 npm/pip names)
  12. Pilot purgatory / 90-95% не дойти до production (MIT Sloan 2025, L11, L1 РФ 90%)

### Cheat-sheet #4 (A1 landscape) — Карта 16 отраслей × keystone-плоскость

**Layout (~A1 landscape):**

- **Header.** «16 отраслей курса AI-usage-lessons на одной карте» + axes labels.
- **Body.** 2D scatter plot covering ~70% poster area:
  - X-axis: «AI fit» (детерминированный non-AI → full AI), gradient color background.
  - Y-axis: «Autonomy L0 → L5», 6 horizontal bands.
  - 16-20 dots (некоторые отрасли — несколько dots для bimodal nature: L13 warehouse + urban + black swan = 3 dots).
  - Each dot — icon отрасли + 2-3 word label.
  - Color coding по модулям курса (module 1 = blue / module 2 = teal / module 3 = gold).
- **Annotations.** На каждой точке — pop-out callout с **главным провалом** этой отрасли (1 line). Например: L13 urban → «Cruise pedestrian Oct 2023».
- **Footer.** Small box: «Каждая точка — несколько недель чтения, разбора кейсов, провалов. Эта карта — то, что у вас осталось. Используй её для любой новой отрасли, не пройденной в курсе.»

---

## AI-Failure budget (≥30% strict-in)

| Артефакт | Total budget | Strict-in target | Distribution |
|---|---|---|---|
| **Chapter** | 30 000 слов | ~10 000 (33%) | §1 7 критериев — 3 500 / §4 12 провалов — 5 000 / §3 per-industry borders ≈ 1 000 / §5 failure-modes cheatsheet ≈ 500 |
| **Slides** | 41 slides | ~13 (32%) | s06-s12 (7 = R1 entire); s29-s33 (5 = R4 entire); s19 antipatterns (1) = 13 |
| **Speech** | ~75 min / 5000 words | ~25 min (33%) | повтор distribution chapter + 1-min antipattern recap в R2 |

Холистическая проверка: НЕ single-cluster — failure-content распределён по R1 (criteria framing) + R2 (antipatterns в autonomy ladder) + R3 (border analysis в карте) + R4 (12 провалов deep-dive) + R5 (cheat-sheet #3 = failure-modes).

---

## Hero plan (s01 + s39)

### s01: «Карта AI после курса» — concept hero

- **Planned visual:** **Composite image** — left half: 4×4 grid 16 industry icons (small monochrome icons, recognizable но не loud); right half: clean 2D scatter plot с 16 dots в цветах модулей. Bridging visual element — стрелка / hand-drawn arrow от grid к scatter, символизирующая «16 лекций → 1 карта».
- **Sources via 6-tier:**
  - Tier 1 (og:image) — try Stanford AI Index 2026 cover или McKinsey State of AI 2025 cover (если есть iconic visual).
  - Tier 2 (Wikipedia) — composite custom-rendered (scatter plot нашу карту + Wikipedia industry icons).
  - Tier 3 (press release) — Nature / Science 2024 «AI impact» visualization.
  - Tier 4 (YouTube thumb) — Anthropic course-style imagery.
  - Tier 5 (Wayback) — fallback.
  - Tier 6 (Google Images) — search «AI applicability map engineering» — manual curate.
- **Most likely path:** custom-rendered scatter plot generated через mermaid / Matplotlib + composed in presentation-designer with 16 icons curated via Lucide/Heroicons + attribution.
- **Attribution label visible:** «Карта составлена на основе курса AI-usage-lessons (16 лекций отраслевых). Icons — Lucide.dev (open license).»

### s39: «Инженер с картой» — concept hero

- **Planned visual:** Silhouette figure (рисованный или фотореалистичный) standing perspective looking at large display showing 2D map; text overlay «Знать ИИ — значит знать его границы». ≥40% area.
- **Sources via 6-tier:**
  - Tier 1 — McKinsey / Gartner cover «Future of AI engineering» — search 2025-2026 publications.
  - Tier 2 — Wikipedia «engineer with display» — likely won't find generic enough.
  - Tier 3 — Anthropic / OpenAI 2026 publication cover.
  - Tier 4-6 — fallback chain.
- **Most likely path:** custom-rendered silhouette + map overlay (PowerPoint MCP shapes + transparent layer).
- **Bridge к career:** explicit foreshadow к «AI-aware engineer» role в R5 s38.

---

## Tools-map (по координатам 2D-плоскости)

Each quadrant of 2D plane gets a representative tool set. Это **для slide s11 (Tools per quadrant)**:

### Quadrant 1: High AI fit + High autonomy (upper-right) — «AI работает и автономно»
- **SE:** GitHub Copilot Agent, Claude Code, Cursor Composer (L3-L4 в narrow PRs)
- **Fraud:** Stripe Radar, Visa AI auto-block (L3 в narrow domain)
- **Warehouse robotics:** Symbotic, Amazon Sparrow / Proteus (L4 в controlled)
- **Drug discovery (closed):** AlphaFold3, Tempus (L3-L4 narrow imaging)

### Quadrant 2: High AI fit + Low autonomy (upper-left) — «AI работает, но autonomy regulatory-capped»
- **Medical imaging:** Aidoc, Chester AI (L1 always HITL by FDA)
- **Finance regulated:** SHAP + glass-box models (L1 EU AI Act mandate)
- **Aero detection:** Project Maven (L1 HITL для авторизации)

### Quadrant 3: Low AI fit + Low autonomy (lower-left) — «AI не нужен / classical wins»
- **OR alternatives:** UPS ORION (Gurobi + heuristics), Google OR-Tools, CPLEX
- **Process control:** MPC (model predictive control), Yokogawa CENTUM (классическая PID + MPC)
- **Inventory:** EOQ + safety stock (Ford Harris 1913 formulas)

### Quadrant 4: Low AI fit + High autonomy (lower-right) — «осторожно: autonomy без AI fit = катастрофа»
- **CrowdStrike-class:** Falcon channel files (L14) — classical EDR + ML, но Act-level — провал
- **F-35 ALIS:** PdM на mission-critical
- **Cruise robotaxi expansion:** ODD без validation

(Q4 — empty by design as warning, not aspiration.)

---

## Course-arc anchors (cross-lecture callbacks)

12 callback-anchors that capstone reuses (each = 1 sentence в chapter / 1 line на slide / 30-sec в speech):

1. **«AI Effect — определения сдвигаются, навык — нет» (L1 → R0)**
2. **«Strawberry test: модель не считает буквы — ограничение токенизации, не интеллекта» (L2 → R1 critique)**
3. **«$4,200-петля — agent без budget cap» (L3 → R4 failure #2)**
4. **«A/B/C/D в SE — но автоматический мерж в production = L3 max» (L4 → R2 mapping)**
5. **«Zillow iBuying — open-world prediction killer» (L5 → R4 failure #1)**
6. **«GM кронштейн — оптимизация ≠ generative AI» (L6 → R1 нейтральный пример)**
7. **«HITL — стандарт медицины» (L7 → R2 L1 advisory anchor)**
8. **«Galactica 17 ноября 2022 — научная hallucination» (L15 → R4 failure #7)**
9. **«F-35 ALIS — high cost-of-error → HITL» (L9 → R4 failure #4)**
10. **«See & Spray — chiseled task + measurable ROI + clear alternative» (L10 → R1 critère 7 anchor)**
11. **«Pilot purgatory — 90-95%» (L11 → R4 failure #12)**
12. **«CrowdStrike Falcon BSOD — Act без canary» (L14 → R4 failure #6)**

---

## Russification anti-anglicism plan

**Top 15 anglicism → RU mappings** для capstone (особенно склонные в систематизаторской лекции):

1. autonomy ladder → лестница автономии
2. fit / applicability → применимость / пригодность
3. AI fit → применимость ИИ / пригодность ИИ
4. closed-loop / open-loop → закрытая петля / открытая среда
5. ground truth → эталон / эталонная разметка
6. cost-of-error → цена ошибки
7. blast radius → радиус разрушения / зона поражения
8. baseline → исходный показатель / базовая линия
9. canary deploy → канареечный выпуск / постепенный выпуск
10. rollback → откат
11. HITL → человек в петле (с расшифровкой при первом упоминании)
12. failure mode → режим отказа
13. anti-pattern → антипаттерн (устоявшийся в RU технической литературе)
14. cheat-sheet → опорная карточка / шпаргалка
15. decision matrix → матрица принятия решения

**Brand allowlist (НЕ переводить):** GitHub Copilot, Claude Code, ChatGPT, Cursor, OpenAI, Anthropic, Google DeepMind, Waymo, AlphaFold, Yokogawa, Siemens, NVIDIA, ABB, BMW, Toyota, Tesla.

**Acronyms — расшифровка при первом упоминании, потом short form:** OODA, HITL, ODD, MPC, RL, SAE J3016, ISO/IEC 22989, FDA, GOST, SHAP, LIME, FMEA, FTA, POD, RCT, EOQ, TSP, VRP, MITRE ATLAS, C2PA.

---

## Open questions для USER GATE A

1. **Лестница автономии — единая L0→L5 для capstone confirmed?** Plan synthesizes L4 A/B/C/D + L9 L1-L5 + L12 A0-A3 + L14 Видит/Решает/Действует в единую L0→L5 (advisory → fully autonomous). Owner подтверждает naming, или предпочитает другую нумерацию (например A0-A5 или L1-L5 как L9)?
2. **2D-плоскость final naming для слайдов / chapter.** Currently «AI fit × Autonomy»; альтернативы: «AI applicability × Autonomy», «Пригодность ИИ × Автономия», «Where AI works × How much it does». Какой формулировка для русско-язычной аудитории best?
3. **Top-12 провалов — final list или editorial reshuffle?** Plan suggests 12 specific failures from cross-lecture analysis. Owner может (a) подтвердить как есть, (b) reorder priority, (c) добавить/убрать конкретные кейсы, (d) расширить до top-15 или сузить до top-10.
4. **Cheat-sheet output format — какой generation tool?** Options: (a) Markdown → PDF via pandoc, (b) PowerPoint slides extracted as PDF, (c) drawio / Inkscape custom layout, (d) HTML + browser print-to-PDF. A1 master poster — нужен другой workflow (Inkscape / Affinity Publisher / Figma export?).
5. **Hero s01 + s39 — concept approval нужен до Phase 6.** Plan suggests (s01) composite «16 icons → 2D scatter», (s39) silhouette «engineer with map». Owner approves direction, или предпочитает другую визуальную метафору? (Например, fork-in-road / map-with-X-marks / blueprint stylization.)
6. **Anonymization scope.** L17 — universal audience; career section должна быть generic. Owner подтверждает: НЕ упоминать ИУ-6 / МГТУ / ВКА / МАИ / specific universities; вместо этого «профильные технические университеты» (родовое)?
7. **Course-arc anchors — 12 callbacks достаточно, или нужно расширить до 16 (по 1 на лекцию)?** Plan suggests 12 strategically — L2 token и L8 креатив могут получить 1 callback каждый, чтобы покрыть все 16.

---

## Constraint sanity check (final)

| Constraint | Plan-v1 status |
|---|---|
| Chapter ≥30 000 слов (L4+ mandatory) | 30 000 target в frontmatter; expansion plan distributed across 5 sections + Q&A |
| AI-Failure ≥30% strict-in | 33% target distributed across 5 sections (R1+R4 = full; R3+R5 partial) |
| Slides ≥50% media coverage | 55% target; cheat-sheet previews + 2D scatter visualizations + hero s01/s39 carry it |
| Hero s01 + s39 | Both planned; 6-tier acquisition path documented |
| No timing на visible body | Confirmed — все таймы в plan-doc и frontmatter only |
| No методология на visible body | Confirmed — мета-комментарии в speech.md только |
| Baseline / counterfactual для measurable claims | All cited stats from L1-L16 with original baselines preserved |
| Russification | 15-word top mapping list + brand allowlist + acronym discipline |
| Anonymization | Universal audience confirmed |
| Document size ≤600 lines | Plan ~600 lines; chapter будет 5 parts (multi-part); slides separate file |

---

## Готовность к GATE A

Plan-v1 готов к owner review. Открытые вопросы (см. выше) — load-bearing decisions, требующие owner input до начала Phase 2 (chapter draft). После GATE A approval — book-editor получает brief на Phase 2 со ссылкой на этот plan + extracts file как сырьё.

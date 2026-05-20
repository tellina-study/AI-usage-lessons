# 05 — Narrative Options (Keystone Axis for Lec-09)

**Цель.** Предложить **3 альтернативных нарратива** для лекции 9 «AI в авиакосмосе и оборонке». Каждая опция — possible keystone axis (несущая концептуальная ось), которая должна быть предъявлена отдельным keystone-слайдом в Разделе 0 ДО первого погружения в неё (см. CLAUDE.md, Pre-USER-GATE п.6, ENFORCED).

**Контекст.** Lec-09 — модуль 2, отрасль 7 (если считать lec-03 как введение в архитектуру, lec-04 ПО, lec-05 финансы/ритейл, lec-06 CAD/CAM, lec-07 медицина, lec-08 сельское хозяйство/энергетика). Bauman audience — будущие инженеры aerospace/КБ/defense.

**ENFORCED constraint (CLAUDE.md AI-Failure & Judgment).** ≥30% strict-in failure/limits/judgment контента в каждом артефакте (chapter + slides + speech). Lec-09 = L9 (НЕ вводная) → owner waiver недоступен.

**ENFORCED constraint (CLAUDE.md L4+ tools-per-taxonomy-level).** Каждый уровень несущей таксономии — 2-4 named tools/programs 2026 + adoption-направление + anti-hype.

---

## 6 разделов лекции (общий каркас, независим от опции)

Любая опция должна лечь в 6 разделов:
- **Раздел 0** — keystone axis + roadmap (рамка лекции; 1 keystone slide + 1 roadmap slide).
- **Разделы 1–4** — 4 содержательных секции (содержат основной материал).
- **Раздел 5** — Q&A + payoff (выводы + критерии + что почитать).

---

## ОПЦИЯ А — «Sensor → Decision → Action» (классическая OODA-loop)

### Несущая ось
**Каждая боевая или гражданская aerospace-задача — это цепочка Sense → Understand → Decide → Act. AI вторгается в каждое звено по-разному; provals — там, где звенья соединяются.**

### Keystone slide (Раздел 0)
Слайд: «Sense → Decide → Act» — горизонтальная цепочка с тремя крупными иконками, под каждым — 2–3 строки «AI здесь работает / не работает / где граница». Это keystone-axis картинка, которую студент держит в голове всю лекцию.

### Раскладка по разделам

| Раздел | Тема | Cases | Failures (strict-in) |
|--------|------|-------|---------------------|
| **0** | Keystone + roadmap | (рамка) | (рамка) |
| **1: Sense** | Спутниковая / SAR / on-orbit edge AI | Maxar Sentry, BlackSky Gen-3, Slingshot Agatha, Φ-sat-2, TerraTech | SAR adversarial attacks; data-distribution shift; GPS-spoofing в civil aviation; ScanEx ограничения |
| **2: Decide** | Mission planning, target ID, fusion | Palantir MSS, Scale Donovan/Defense Llama, Helsing Altra, Anthropic-Palantir-AWS, MGTU Bauman AI | LLM hallucinations DoD wargames; IDF Lavender 90% accuracy; Lancet ATR rollback; Vincennes 1988 UI failure |
| **3: Act** | Autonomy on platform (drones, CCA, missile defense) | Anduril Fury/Roadrunner, Shield AI V-BAT, DARPA X-62A VISTA, Ukraine Saker Scout, Russia Geran-2 evolution, China Atlas swarm | Boeing 737 MAX MCAS; Patriot friendly fire; F-35 ALIS→ODIN; Replicator missed scale; LAWS treaty status |
| **4: Граница**  | Где AI **не должен** работать | ICRC position; UN GGE 161-3-13; LAWS treaty timeline; Project Maven walkout; Stop Killer Robots 30 countries | Каждый strict-in (это весь раздел — provals & границы) |
| **5: Q&A + payoff** | Career path + критерии + reading | МГТУ ИИ + ВКА Можайского + что почитать | (закрывающий callback) |

### Russian context — где
- **Раздел 1.** TerraTech / Sputnix / Gigachat ISS (с caveats) — как Russia делает Sense.
- **Раздел 2.** Svod / Glaz-Groza — Russian C2 ambitions; Vincennes как ahistorical контр-точка.
- **Раздел 3.** Geran-2 evolution (cases) + Lancet rollback (failure); supply chain (NVIDIA Jetson).
- **Раздел 4.** Russia votes against UN resolution → geopolitical context для студента.
- **Раздел 5.** МГТУ ИИ + ВКА Можайского — careers.

### Media-rich slides (~32 общих, ≥50% rich)
- Sat imagery before/after (Maxar Sentry detect); X-62A VISTA flight test photo; Anduril Fury production; Geran-2 wreckage NVIDIA Jetson photo; UN GGE voting map; LAWS infographic; Russia drone evolution timeline; CFD/PINN visualization; CCA family tree (US/EU/China/Russia); Lavender controversy visualization (90% accuracy → 3700 false positives).

### Pros
- **Канонический OODA-loop** — знаком инженерам, легко удерживается в голове.
- Натурально включает strict-in failure-blocks в каждом разделе (33% контента — failures в каждом).
- Tools-per-taxonomy естественно: Sensor (Maxar/BlackSky/Slingshot) → Decision (Palantir/Scale/Helsing) → Action (Anduril/Shield AI/Geran-2/Atlas).
- Russian context логично распределяется по всем 4 разделам.

### Cons
- OODA — старая концепция (1976, Boyd); может выглядеть «школьно» для 2026 audience.
- 3 раздела (Sense/Decide/Act) vs 4 содержательных — нужно adapt.

### Verdict: **STRONG candidate** (см. рейтинг в финальной части).

---

## ОПЦИЯ Б — «Уровни автономии» (L1 → L5)

### Несущая ось
**5 уровней — от ассистента-аналитика до полностью автономной системы. Каждый уровень — отдельный класс задач, провалов и этических вопросов. Граница между L3 и L4 — то, где сейчас идёт UN treaty negotiation.**

### Keystone slide (Раздел 0)
Слайд: вертикальная или 5-step horizontal — L1 (помощник) → L2 (perception assist) → L3 (supervised) → L4 (pre-authorised auto-engage) → L5 (full LAWS). Под каждым — example tool. Над L4 — линия "treaty negotiation here".

### Раскладка по разделам

| Раздел | Тема | Cases | Failures (strict-in) |
|--------|------|-------|---------------------|
| **0** | Keystone + roadmap |||
| **1: L1 Assistive** | Аналитик-помощник | Palantir MSS, Maxar Sentry, NASA FDL, Airbus Skywise | LLM hallucinations decision support; F-35 ALIS UX fail |
| **2: L2 Semi-auto perception** | CV / fusion / target lock | Saker Scout, Shield AI Hivemind target lock, Helsing Altra | SAR adversarial attacks; Lancet ATR rollback; IDF Lavender |
| **3: L3 Supervised autonomy** | Co-pilot / loyal wingman / battle mgmt | Anduril Fury, DARPA X-62A VISTA, Lockheed Skunk Works AI battle mgmt | Boeing 737 MAX MCAS; X-62A scripted scenario limits; Replicator missed scale |
| **4: L4 → L5 Border** | Auto-engage и треугольник treaty | Patriot/S-400 auto modes, Geran-2 onboard ATR (debated); LAWS  | UN GGE; ICRC position; Vincennes 1988; Lavender; LAWS treaty timeline |
| **5: Q&A + payoff** | Карьера + критерии + ось «когда вообще не надо» |||

### Russian context
- **L1.** Russian C2 (Svod/Glaz-Groza) — попытка построить Russian Palantir-equivalent.
- **L2.** Lancet ATR rollback — strict-in case demo-vs-production.
- **L3.** Russia/China J-20S manned-unmanned teaming (если адаптируем под L3).
- **L4 border.** Russian + S-400 «AI auto-engage» claims; Russia votes против UN resolution.
- **L5.** Russia among the 3 states voting against ALL UN LAWS resolutions.

### Media-rich slides
- L1–L5 ladder/staircase visualization (keystone); side-by-side Lavender vs ICRC stance; UN GGE voting world map; Geran-2 wreckage; Patriot launcher (auto/manual switch context); X-62A cockpit (no pilot); Fury production photo.

### Pros
- **Очень pedagogical для inженеров** — уровни как у self-driving cars (L0-L5 SAE), familiar mental model.
- Strict-in concentration в L4–L5 разделе **естественна**, не выглядит «вставленной».
- Connect to **ethical decision-making** на конкретных levels.

### Cons
- L4/L5 mapping на реальный военный inventory — **спорно**: Russia/Israel/US отличаются в classifications. Может породить debates с аудиторией.
- Granularity issue: L2 → L3 → L4 — gradient, не strict-buckets; легко превращается в «taxonomy fight».
- Treaty timeline — fast-moving; risk outdated к day-of.

### Verdict: **MEDIUM candidate** — strong concept, но boundary cases hard.

---

## ОПЦИЯ В — «Гражданское ↔ оборонное dual-use»

### Несущая ось
**Одни и те же AI-модели и капабилитис работают в гражданском (рейсы, спутниковая аналитика, eVTOL) и в военном (целеуказание, drone swarms, missile defense). Граница между ними — не техническая, а юридическо-этическая. И эта граница — fast-eroding. Что делать инженеру на этой границе?**

### Keystone slide (Раздел 0)
Слайд: горизонтальный split — слева «Civilian», справа «Military». Между ними — пересекающиеся круги Venn («Dual-use core»). В центре — конкретные models / tools / sensors. Стрелки указывают, как технологии «перетекают».

### Раскладка по разделам

| Раздел | Тема | Cases | Failures (strict-in) |
|--------|------|-------|---------------------|
| **0** | Keystone + roadmap | | |
| **1: Civilian apex** | Чистый гражданский — где AI блистает | Rolls-Royce IntelligentEngine, Airbus Skywise, NASA FDL, Wisk Aero Gen-6 | F-35 ALIS predictive maintenance fail; Lilium bankruptcy; eVTOL cert lag |
| **2: Dual-use core** | То же самое, в военной форме | Maxar Sentry (civilian crisis + military intel); Palantir MSS; Anthropic-Palantir-AWS partnership; OpenAI removes military ban | LLM hallucinations; Project Maven walkout; Project Nimbus controversy; Lavender |
| **3: Military apex** | Чисто военное — где гражданского аналога нет | DARPA X-62A; Anduril Fury; Geran-2; China J-20 AI dark factory; SDA tracking layer | Boeing 737 MAX MCAS (single-sensor lesson cross-applies); Patriot 2003; Replicator missed scale; GPS spoofing civilian spillover |
| **4: Граница и treaty** | Где регулирование пытается провести черту | UN GGE; ICRC; Stop Killer Robots 30 states; sanctions/chip evasion | (раздел сам — strict-in) |
| **5: Q&A + payoff** | Career на границе + критерии для инженера | МГТУ + ВКА Можайского + reading | |

### Russian context
- **Раздел 1.** TerraTech / Sputnix (civilian satellite analytics).
- **Раздел 2.** Russian dual-use VisionLabs (civil + surveillance); Sber GigaChat ISS (claimed civilian).
- **Раздел 3.** Geran-2 + Lancet + Orion.
- **Раздел 4.** Russia votes против UN; sanctions/chip evasion (Russian dependence).

### Media-rich slides
- Civilian-Military Venn visualization (keystone); Skywise dashboard; Rolls-Royce digital twin; Wisk Aero Gen-6 (no cockpit) photo; Project Maven walkout photo; Geran-2 with NVIDIA Jetson; UN GGE voting map; chip-supply-chain map (US → India → Russia).

### Pros
- **2026-evergreen.** Border-eroding — это main story для следующих 10 лет.
- **High Russian content fit.** Russian context — естественно integrated, не «add-on».
- **Strong career-relevance для Bauman audience.** Студент после ИУ может пойти в Avito (civilian CV), в Mil/Воу/КБ (military), или dual-use (Cognitive Pilot, VisionLabs).
- Failure блоки естественно concentrate в Разделах 2-4.

### Cons
- **Менее crisp keystone** (Venn diagrams — не такие clean как ladder или OODA chain).
- Может быть **slightly philosophical** vs technical — нужно балансировать конкретными кейсами.
- L4+ tools-per-taxonomy-level harder (axes не cleanly fit dual-use sliding).

### Verdict: **STRONG candidate** — особенно для Russian-context fit and 2026 relevance.

---

## Сравнительная таблица

| Критерий | A: OODA | Б: L1–L5 autonomy | В: Civil ↔ Military |
|----------|---------|-------------------|---------------------|
| Familiarity для engineers | ⭐⭐⭐ (классика) | ⭐⭐⭐⭐ (SAE-style) | ⭐⭐ (newer concept) |
| Keystone slide clarity | ⭐⭐⭐⭐ (chain) | ⭐⭐⭐⭐ (ladder) | ⭐⭐ (Venn) |
| Strict-in failure ≥30% natural fit | ⭐⭐⭐ | ⭐⭐⭐⭐ (concentrate L4-L5) | ⭐⭐⭐⭐ (concentrate R 2-4) |
| Tools-per-taxonomy (L4+ ENFORCED) | ⭐⭐⭐⭐⭐ (Sense/Decide/Act each → tools) | ⭐⭐⭐ (L1-L5 each → tools) | ⭐⭐ (axes don't cleanly tier) |
| 2026-evergreen | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ (border-erosion story) |
| Russian context integration | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| LAWS treaty integration | ⭐⭐⭐⭐ (Раздел 4) | ⭐⭐⭐⭐⭐ (L4-L5 border) | ⭐⭐⭐⭐ |
| Career relevance Bauman | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Risk of axes-boundary fight | low | medium-high | medium |
| Memorable single mental model | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

## Recommendation для plan

### Tier 1 — **Опция А: «Sensor → Decision → Action»** (strongest baseline)
**Почему.**
1. OODA-loop — familiar mental model для инженеров; легко удерживается keystone slide.
2. Tools-per-taxonomy fits **perfectly** (Sense → Decide → Act = 3 наборов tools 2026).
3. Strict-in failure ≥30% работает в каждом разделе органично (sensor brittleness; LLM hallucinations; autonomy provals).
4. Russian context распределяется без перекоса.
5. Низкий риск axis-boundary fights с критиками.

**Адаптация.** Раздел 4 — выделить как «Граница и регулирование» (separate from Sense/Decide/Act), чтобы LAWS-block был **explicit**, не разбросан.

### Tier 2 — **Опция В: «Civil ↔ Military»** (best for 2026-evergreen)
**Почему.**
1. Most relevant к **next 10 years** трендов (chip sanctions, dual-use models, GenAI defense pivot).
2. Russian context **naturally integrated** — не «бонус», а core to argumentation.
3. Strong career angle для Bauman audience (студент-инженер на границе).
4. Maven walkout / Anthropic-Palantir-AWS — strong recent narrative.

**Адаптация.** Keystone — не Venn, а **bridge visualization**: civilian deck vs military deck с явными "crossings". Tools-per-taxonomy — на уровне crossings (модель → applications в обе стороны).

### Tier 3 — **Опция Б: «Уровни автономии»** (best for ethical framing)
**Почему secondary.**
- Concept strong, но classification disputes risk.
- LAWS treaty mapping — sensitive (L4 vs L5 — где Geran-2 vs S-400 vs LAWS).
- Может стать «taxonomy fight».

**When to choose:** если декан / course-owner предпочитает explicit ethical scaffolding до technical content.

---

## My recommendation для Bauman audience

**Top pick: ОПЦИЯ A с лёгкой инъекцией из B и В.**

**Reasoning.**
1. **Bauman ИУ-аудитория** — инженеры, не философы и не политологи. OODA-loop concrete и actionable.
2. **Strict-in failure ≥30%** работает в каждом из 4 разделов органично (lecture-by-lecture pacing not concentrated в одном).
3. **Tools-per-taxonomy-level ENFORCED** — Опция А лучше всех ложится.
4. **LAWS-block** становится Разделом 4 (separate "Граница и регулирование") — keeping ethics explicit, без распыления по всей лекции.
5. **Russian context** распределяется без перекоса; каждый раздел имеет свой Russian case.
6. **Адаптация из B:** в Разделе 4 включить L1-L5 ladder как **visual** для LAWS-границы.
7. **Адаптация из В:** в Разделе 0 keystone — упомянуть dual-use bridge как фон, на котором OODA-loop работает.

**Risk mitigation.**
- Keystone slide должен предъявить ось OODA ПЕРВЫМ — не «после защиты подхода», не «через recap курса» (см. CLAUDE.md, Lec-4 lesson).
- Failure-блоки должны быть **strict-in** (не оговорки), а full sections / sub-sections.

---

## Open question for owner (USER GATE на plan)

1. **Confirm OODA-loop как keystone** vs alternatives.
2. **Owner waiver для L1-L3** — не релевантно (L9 — middle of course, waiver недоступен).
3. **Russian context proportions** — target какой долей (10–20%? больше?).
4. **LAWS treaty эмфазис** — отдельный раздел vs распределение по 3 разделам?
5. **Career angle** — насколько сильно адресовать «куда пойти после ИУ» в Разделе 5?


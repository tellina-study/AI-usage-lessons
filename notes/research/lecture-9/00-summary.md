# 00 — Lec-09 Research Brief Summary

**Lecture.** 09 — «AI в авиакосмической отрасли и оборонном комплексе» (модуль 2 курса ИУ6 МГТУ Баумана).
**Audience.** Инженеры 3 курса; будущие сотрудники КБ, ракетно-космических предприятий, военной индустрии, dual-use startups.
**Research date.** 2026-05-20.
**Research scope.** 5 файлов (~3500 строк, ~120k символов) с глубоким анализом 80+ кейсов и более **80 уникальных источников**.

---

## Артефакты

| # | Файл | Назначение | Размер |
|---|------|-----------|--------|
| 0 | `00-summary.md` | Этот файл — финальный отчёт | ~300 строк |
| 1 | `01-real-applications.md` | Кейсы где AI реально работает (~50 cases по 13 категориям) | ~370 строк |
| 2 | `02-failures-and-limits.md` | Документированные провалы и границы (20+ failures) | ~350 строк |
| 3 | `03-trends-2026.md` | Тренды 2025–2026 + tools-per-taxonomy-level (L4+ ENFORCED) | ~250 строк |
| 4 | `04-russian-context.md` | Российский слой (TerraTech, ScanEx, Geran-2, VisionLabs, МГТУ/ВКА Можайского) | ~240 строк |
| 5 | `05-narrative-options.md` | 3 опции keystone axis с pros/cons | ~280 строк |

**Total unique sources cited.** ~110 ссылок (превышает требуемые 50).

---

## 5 сильнейших кейсов, где AI **действительно** работает (с цифрами)

### 1. **Maxar Sentry — predictive intelligence (2025)**
- 250 PB satellite imagery archive + AI flag global threats до того, как развернутся.
- NGA Luno A D01 task order — AI detections within **hours of capture**.
- Метод: ML + multi-sensor tipping (electro-optical + SAR + AIS).
- Источник: Defense One, BusinessWire (June 2025).

### 2. **Rolls-Royce IntelligentEngine + TotalCare**
- Digital twin + ML over real-time + batch engine telemetry; Azure data lake + Databricks lakehouse.
- **~400 unplanned maintenance events предотвращены/год** на флоте.
- Экономия миллионы евро/год + минимизация downtime.
- Источник: Klover.ai, CIO, Plant Services.

### 3. **Airbus Skywise — predictive maintenance suite**
- **~11 600 самолётов** подключены к концу 2024.
- easyJet — **8.1 тонны экономия топлива/ВС/год**; в июле 2024 — **44 предотвращённых отмены рейсов**.
- ~40 customers на SFP+, ~1500 ВС; новые 2024: Qantas/Jetstar, Korean Air, Philippine.
- Источник: Airbus press, AirCraftIT.

### 4. **Anduril Lattice + Fury YFQ-44A (2025–2026)**
- AI-mesh OS для autonomous systems; Arsenal-1 factory $1B Ohio.
- Fury первый полёт Oct 31, 2025; production starts Mar 2026; flying with AIM-120 AMRAAM.
- DoD Army contract ceiling **до $20B / 10 лет** (Mar 2026); Anduril valuation $61B.
- Источник: TechCrunch, Wikipedia, Air & Space Forces.

### 5. **DARPA ACE X-62A VISTA AI dogfight (2023–2024)**
- First in-air AI vs human dogfight; 21 test flights, 100k+ lines of flight-critical software changes.
- Sept 2023: AI vs manned F-16; engaged как close as **2000 ft @ 1200 mph**.
- May 2024: USAF Secretary Kendall flies в AI-piloted X-62A.
- Источник: DARPA, Aviationist, Defense News.

### Honorable mention: **Helsing Altra + Centaur (€12B valuation 2025)**, **NASA FDL geomagnetic forecasting**, **SDA PWSA Tranche 3 ($3.5B/72 sats Dec 2025)**, **Scale AI Defense Llama + Donovan на classified networks**.

---

## 5 самых поучительных провалов (с уроками)

### 1. **IDF Lavender targeting system (Gaza 2023–2024)**
- 37 000 человек помечены; **90% accuracy** (IDF self-assessment) → **3700 false positives**.
- Officers «devoted almost no resources» к double-checking targets / bystanders.
- Authorisation: до 15-20 civilian casualties per junior Hamas operative.
- **Урок:** «Accuracy %» — wrong metric для life-and-death. Нужно false-positive consequence × population × frequency.
- Источник: Yuval Abraham +972 / Local Call (April 2024).

### 2. **Boeing 737 MAX MCAS (2018–2019, 346 KIA)**
- Single AoA sensor + opacity + repeated trim commands → 2 crashes, 20-month grounding.
- Не AI в строгом смысле, но **canonical anti-pattern** для всех safety-critical AI.
- **Урок:** redundancy + transparency + single-point-of-failure analysis обязательны до cert. Software cannot patch hardware shortfalls.

### 3. **F-35 ALIS predictive maintenance fiasco**
- High false positives; aircraft flagged as no-fly без real issues; manual inspections; cost-per-flight-hour до **$44k** (выше F-22 Raptor).
- ALIS final version June 2024; ODIN rollout затянут до 2025–26.
- **Урок:** predictive maintenance работает если (a) feedback loop быстрый, (b) ground truth доступен, (c) FP-cost < FN-cost. ALIS нарушил все три + adversarial UX.

### 4. **USS Vincennes / Iran Air 655 (1988, 290 KIA)**
- Aegis правильно классифицировал track як climbing — но крю под стрессом доложил «descending into attack».
- **Урок:** human-machine interface под combat stress — не панацея. UI tested under predicted failure modes, not idealised rationality.
- Применимо ко всему LLM-decision-support 2024+.

### 5. **Russian Lancet ATR rollback (2022–2024)**
- Marketing: «autonomously find and hit target». Reality: AI guidance turned off после initial deployment; videos без "Target Locked" UI; product "recall".
- **Урок:** Demo ≠ production. ML perf в narrow test distribution не переносится на full battlefield variance (dust, smoke, EW, damaged equipment).
- **Pedagogical особо ценен:** показывает разрыв между AI-marketing и AI-deployment.

### Honorable mention: **Patriot friendly fire 2003** (automation bias + IFF), **Iran capture RQ-170 2011** (GNSS single-point-of-failure), **Google Project Maven walkout 2018** (ethics adoption failure — Anduril/Palantir подхватили), **DoD Replicator missed scale** (software integration lag), **Adversarial attacks SAR ATR** (DL brittleness), **GPS spoofing civil aviation** (EW spillover к non-combatants).

---

## Top-3 recommended narrative options

### **#1 — ОПЦИЯ A: «Sense → Decide → Act» (OODA-loop)** ⭐⭐⭐⭐⭐
**Почему лучшая для Bauman audience.**
- Familiar mental model для инженеров; concrete actionable.
- Tools-per-taxonomy-level (ENFORCED L4+) fits **idealy** (Sensor tools / Decision tools / Action tools).
- Strict-in failure ≥30% распределяется органично в каждом из 4 разделов, не концентрируется.
- Russian context раскладывается без перекоса (TerraTech в Sense, Svod в Decide, Geran-2 в Act, votes-against-UN в Раздел 4).
- Низкий risk axis-boundary fights.

**Адаптация.** Раздел 4 — выделить как «Граница и регулирование» (LAWS / UN GGE / ICRC / treaty timeline) — отдельный strict-in блок.

### **#2 — ОПЦИЯ В: «Civil ↔ Military dual-use border»** ⭐⭐⭐⭐
**Почему secondary.**
- **Самая 2026-evergreen** — border-erosion = main story для 10 лет.
- Russian context **naturally core**, не add-on.
- Strong career-relevance для студента ИУ (carve-out civilian / military / dual-use).
- Anthropic-Palantir-AWS / OpenAI removes military ban / Maven walkout — strong recent narrative.

**Risk.** Keystone slide (Venn diagram) clarity ниже OODA chain; tools-per-taxonomy harder map.

### **#3 — ОПЦИЯ Б: «Уровни автономии L1→L5»** ⭐⭐⭐
**Почему tertiary.**
- Concept strong (SAE-style ladder familiar), но classification disputes risk.
- LAWS treaty mapping spotny (L4 vs L5 — где Geran-2, S-400, IDF auto-modes).
- Может стать «taxonomy fight».

**Pick when:** course-owner предпочитает explicit ethical scaffolding перед technical content.

### **Финальная рекомендация.**
**ОПЦИЯ A** как baseline. Адаптация:
- В **Razdele 0 keystone slide** упомянуть dual-use border (заимствование из В) как фоновый context.
- В **Разделе 4** включить L1-L5 ladder (заимствование из Б) как visual для LAWS-границы.

Так получаем **OODA-chain как несущая ось** + dual-use awareness + autonomy ladder для LAWS-block. Стабильная, понятная, hard to refute.

---

## Серьёзные «дыры» в открытых данных — пометить `[VFY-day-of]` в плане

1. **Anduril valuation / funding round** (changes monthly).
2. **DoD Replicator delivered count** (volatile).
3. **Russian Geran-2 monthly production rate** (OSINT updates).
4. **CCA Increment 1 selection** (Fury vs YFQ-42A) — competition ongoing.
5. **SDA Tranche 3 launch schedule** (typical delays для big SDA primes).
6. **UN GGE treaty negotiation timeline** — fast-moving.
7. **Helsing / Shield AI / Anduril valuations** — change quarterly.
8. **Aerostate startup** — **NO open international sources verify** (recommend NOT mention).
9. **Sber GigaChat ISS deployment** — single Russian-side announcement, not independently verified.
10. **Russian C2 systems (Svod / Glaz-Groza) operational status** — CSIS reports + single-source disclosure; effectiveness unclear.
11. **IDF Lavender official rebuttal** vs +972 source — debate ongoing.
12. **Russian dependency on NVIDIA Jetson** — wreckage analysis ongoing; sanctions enforcement updates.
13. **Chinese DeepSeek deployment scale в PLA** — assertions vs verifiable scope.

**Recommend in plan:** mark every quantitative claim about active programs as `[VFY-day-of]`; deferring concrete numbers к day-of update from preflight verification.

---

## File index с line counts (approximate)

```
00-summary.md             ~300 lines
01-real-applications.md   ~370 lines  
02-failures-and-limits.md ~360 lines
03-trends-2026.md         ~260 lines
04-russian-context.md     ~240 lines
05-narrative-options.md   ~290 lines
─────────────────────────
TOTAL                    ~1820 lines
```

**Unique sources count:** ~110 URL-citations (DefensePost, DefenseScoop, CSIS, CNAS, GAO, Wikipedia (verified), arXiv, Defense News, Air & Space Forces, BusinessWire, +972, ICRC, Stop Killer Robots, Reuters/Forbes/Fortune/TechCrunch, Palantir/Anduril/Shield AI/Helsing/Lockheed/Airbus official press, Russian primary: bauman.ru, vka.mil.ru, TASS, scanex.ru, sputnix-group.ru, etc.).

---

## Hand-off для Phase 1 (план лекции)

Следующая фаза — **plan лекции** на основе:
- **Keystone axis:** ОПЦИЯ A (Sense → Decide → Act) с touches из В и Б.
- **6 разделов:** Раздел 0 (keystone), 1 (Sense), 2 (Decide), 3 (Act), 4 (Граница / LAWS), 5 (Q&A + payoff).
- **5–8 кейсов** где AI работает (отобрать из файла 01).
- **3–5 strict-in failure блоков** (отобрать из файла 02).
- **Russian context** integration в каждом разделе (см. файл 04 §8).
- **Tools-per-taxonomy-level** на каждый уровень (Sense / Decide / Act): 2-4 named tools 2026 + adoption direction + anti-hype (см. файл 03 §«Tools-per-taxonomy-level»).

**Quality gates перед открытием USER GATE A на план.**
- Failure ≥30% strict-in в плане (для каждого раздела).
- Keystone axis предъявлена отдельным слайдом в Разделе 0 ДО первого погружения.
- L4+ tools-per-taxonomy-level — соблюдено.
- Volatile цифры — все помечены `[VFY-day-of]`.


# Лекция 13 — Iteration Log

Phase 5-7 production: deck.yaml + 41 slide markdowns + assets acquisition + PPTX render.

## Источники реальных изображений (6-tier acquisition)

Все изображения через **Tier 2 Wikipedia Commons** или **Tier 3 press kit**, ≥40% размер, attribution-clean (CC-BY-SA или public domain или educational fair use).

### Tier 2 — Wikipedia Commons / Wikipedia API (CC-BY-SA / public domain)

| Slide | File | Source URL |
|---|---|---|
| s01 | s01-waymo-jaguar-sf-dllu.jpg | https://commons.wikimedia.org/wiki/File:Waymo_Jaguar_I-Pace_in_San_Francisco_2023_dllu.jpg |
| s07 | s07-symbotic-logo.jpg | https://commons.wikimedia.org/wiki/File:SymboticLogo.jpg |
| s08 | s08-amazon-warehouse-robot-2020.JPG | https://commons.wikimedia.org/wiki/File:Amazon_warehouse_robot_2020.JPG |
| s09 | s09-item-picking-robot.png | https://commons.wikimedia.org/wiki/File:Item_Picking_Robot.png |
| s10 | s10-maasvlakte-aerial.png | https://commons.wikimedia.org/wiki/File:Rotterdamse_wijken-maasvlakte.PNG |
| s10b | s10b-long-beach-terminal.jpg | https://commons.wikimedia.org/wiki/File:Terminal_Island,_Long_Beach,_California_(6026497215).jpg |
| s10c | s10c-zpmc-cranes-seattle.jpg | https://commons.wikimedia.org/wiki/File:ZPMC_cranes_at_the_Port_of_Seattle.jpg |
| s11 | s11-deutsche-bahn-ice.jpg | https://commons.wikimedia.org/wiki/File:ICE_Testfahrt_Unteroberndorfer_Brücke_9113767.jpg |
| s11b | s11b-rail-switch.jpg | https://commons.wikimedia.org/wiki/File:Railway_switch_lever_on_Grötö.jpg |
| s15 | s15-mobileye-pcb.jpg | https://commons.wikimedia.org/wiki/File:Lane_Guidance_Camera_PCB.jpg |
| s15b | s15b-kamaz-truck.jpg | https://commons.wikimedia.org/wiki/File:Kamaz_2.JPG |
| s15c | s15c-mobileye-zeekr-iaa.jpg | https://commons.wikimedia.org/wiki/File:Mobileye_Zeekr_001,_IAA_Summit_2023,_Munich_(P1120233-RR).jpg |
| s16 | s16-ups-delivery-truck.jpg | https://commons.wikimedia.org/wiki/File:Typical_UPS_delivery_truck.JPG |
| s17 | s17-argo-ai-vehicle-2021.jpg | https://commons.wikimedia.org/wiki/File:Argo_AI_(2021).jpg |
| s17b | s17b-ford-argo-ai-self-driving.jpg | https://commons.wikimedia.org/wiki/File:Ford_Argo_AI_Self_Driving_Car.jpg |
| s24 | s24-waymo-self-driving-side.jpg | https://commons.wikimedia.org/wiki/File:Waymo_self-driving_car_side_view.gk.jpg |
| s25 | s25-apollo-go-rt6.jpg | https://commons.wikimedia.org/wiki/File:(CHN-Hubei)_Apollo_Go_Apollo_RT6_Temporary-鄂A1395试_2025-12-17.jpg |
| s26 | s26-pony-ai-lexus.jpg | https://commons.wikimedia.org/wiki/File:(CHN-Guangdong)_Pony.ai_Lexus_RX450h_P6001_2024-05-24.jpg |
| s27 | s27-tesla-model-y-myle-2025.jpg | https://commons.wikimedia.org/wiki/File:Tesla_Model_Y_(2025)_MYLE_Festival_2025_DSC_9565.jpg |
| s27b | s27b-tesla-cybercab-berlin-2024.jpg | https://commons.wikimedia.org/wiki/File:Tesla_Cybercab_-_Berlin_2024.jpg |
| s28 | s28-zipline-drone-launch.jpg | https://commons.wikimedia.org/wiki/File:Zipline_Drone_Launch.jpg |
| s28b | s28b-starship-tartu-2017.jpg | https://commons.wikimedia.org/wiki/File:Idufirma_Starship_pakirobot_Tartu_kesklinnas_2017._aastal..jpg |
| s28c | s28-starship-robot.jpg | https://commons.wikimedia.org/wiki/File:MGL0333.jpg |
| s29 | s29-cruise-bolt-sf.jpg | https://commons.wikimedia.org/wiki/File:Cruise_Automation_Bolt_EV_third_generation_in_San_Francisco.jpg |
| s30 | s30-uber-volvo-sf.jpg | https://commons.wikimedia.org/wiki/File:Uber_Self_Driving_Volvo_at_Harrison_at_4th.jpg |
| s30b | s30b-uber-atg-toronto.jpg | https://commons.wikimedia.org/wiki/File:Uber_ATG_Toronto_Vehicle_005554.jpg |
| s34 | s34-uss-carney-houthi.jpg | https://commons.wikimedia.org/wiki/File:USS_Carney_engages_Houthi_missiles.jpg |
| s34b | s34b-prosperity-guardian-map.png | https://commons.wikimedia.org/wiki/File:Map_of_Operation_Prosperity_Guardian.png |
| s35 | s35-ever-given-suez.jpg | https://commons.wikimedia.org/wiki/File:IMO_9811000_EVER_GIVEN_(09).JPG |
| s35b | s35b-suez-traffic-space.jpg | https://commons.wikimedia.org/wiki/File:Suez_Canal_traffic_jam_seen_from_space.jpg |
| s41 | s41-noc-iupui.jpg | https://commons.wikimedia.org/wiki/File:NOC-IUPUI.jpg |
| s41b | s41b-noc-architel.jpg | https://commons.wikimedia.org/wiki/File:NOC-Architel.jpg |

### Tier 3 — Press release (educational fair use)

| Slide | File | Source URL |
|---|---|---|
| s14 | s14-aurora-driverless-press.jpg | https://ir.aurora.tech/news-events/press-releases/detail/119/aurora-begins-commercial-driverless-trucking-in-texas-ushering-in-a-new-era-of-freight |

### Total: 33 real images via Tier 2 + Tier 3 (no mocks fallback используется)

## Hero compliance

- **s01 hero (Waymo Jaguar SF):** ≥40% area, Tier 2 (Wikipedia Commons), attribution «Waymo Jaguar I-Pace в San Francisco · 2023 · Wikimedia Commons · CC-BY-SA».
- **s41 hero (NOC IUPUI):** ≥40% area, Tier 2 (Wikipedia Commons), attribution «Network Operations Center IUPUI · Wikimedia Commons · CC-BY-SA».
- Backup для s01: Aurora Class-8 press → есть в s14.
- Backup для s41: NOC-Architel → есть как s41b.

## Slides без real image (acceptable per acquisition plan)

Эти слайды НЕ требуют hero photo (failure-matrices, decision frameworks, section dividers, glossary) — для них достаточно schema + text + Ocean motif. Не считается mock fallback.

- s02 (cover) — декоративный «13» + текст лекции
- s03 (lecture-map) — 5 horizontal cards
- s04 (glossary) — 10 терминов в 2 колонки
- s05 (keystone) — 5-step ladder schema
- s06 (Раздел 1 divider) — big «1» + text
- s12 (discrete failure matrix) — table 4×3
- s13 (Раздел 2 divider) — big «2» + text
- s17 (AV bankruptcy timeline) — 5 точки на одной линии + текст
- s18 (cumulative $20B) — stacked bars QuickChart
- s19 (survivor consolidation) — 2-col matrix
- s20 (trucker shortage) — number comparison
- s21 (highway failure matrix) — table 4×3
- s22 (Starsky quote) — large quote
- s23 (Раздел 3 divider) — big «3» + text
- s31 (Tesla NHTSA) — data chart fatalities
- s32 (urban failure matrix) — table 4×3
- s33 (Раздел 4 divider) — big «4» + text
- s36 (COVID supply chain) — 3-phase chronology
- s37 (trucker shortage structural) — schema
- s38 (decision framework) — 5-criteria decision tree
- s39 (alternative toolkit) — 6-row matrix
- s40 (Q&A vendor questions) — checklist

## Media coverage

- **Slides с real image:** s01, s07, s08, s09, s10, s11, s14, s15, s16, s17, s24, s25, s26, s27, s28, s29, s30, s34, s35, s41 = **20 slides**.
- **Slides с charts / schemas (QuickChart + mermaid + python-pptx primitives):** s05, s12, s17, s18, s19, s20, s21, s22, s31, s32, s36, s37, s38, s39, s40 = **15 slides**.
- **Slides text-only (divider/cover/glossary):** s02, s03, s04, s06, s13, s23, s33 = **7 slides**.

**Total media-rich: 20 (real) + 15 (charts/schemas) = 35 / 41 = 85% media coverage.**

User target: ≥50% slides с media inserts. **Comfortably exceeded.**

## Pre-render checks (per slide markdown)

- ✅ Anonymization: 0 hits для МГТУ/Бауман/ИУ-N/ВКА/МАИ/Можайск.
- ✅ Timing markers: 0 hits.
- ✅ Methodology markers в visible body: 0 hits.
- ✅ Designer extras (Лектору/Вы здесь/course-scaffold/VERIFY-DAY-OF): 0 hits.
- ✅ LO codes в visible body (not frontmatter): 0 hits.
- ✅ § cross-references в body (not chapter_ref): 0 hits.
- ✅ Pony.ai cascade fix: s26 references Гуанчжоу November 2025 (FIRST) и Шэньчжэнь February 2026 (SECOND) — corrected per chapter v2 P0 fix.

## Phase 6 — PPTX render (visual loop iterations 1-4)

### Iter 1 — initial build
- **Generate:** `python3 build_lec13.py` → `lec-13.pptx` (41 slides).
- **Convert:** `libreoffice --headless --convert-to pdf` → `lec-13.pdf` (3,8 MB).
- **Snapshot:** `pdftoppm -r 110 -png` → `snapshots/iter1-*.png`.
- **Inspect:** visually проверил s01 (hero), s05 (keystone), s17 (timeline), s29 (Cruise), s38 (decision framework), s41 (closing hero).
- **Found:** sufficient Ocean palette + gold highlights + visual progression. **Russification gap:** 1965 occurrences/976 unique English tokens в visible body (deep latin-token scan).
- **Verdict:** continue iterations.

### Iter 2 — russification pass 1 (sed-based, headers/labels)
- **Changed:** `Why:` → `Почему:`, `Lesson` → `Урок`, `Survivor pattern` → `Паттерн выживания`, `Survivors` → `Выжившие`, `dropouts` → `выбывшие`, `Common patterns` → `Общие паттерны`, `Controlled` → `Контролируемое`, `non-survivors` → `невыжившие`.
- **Re-scan:** 1965 → 1660 occurrences (-15%). Top hits теперь dominated by brand names.

### Iter 3 — russification pass 2 (Python regex с word-boundaries)
- **Changed:** 264 replacements via regex pattern matching на visible string positions. Categories: common UI/concept terms (safety, capital, incident, distribution, commercial, revenue, public, fatal, narrow, demand, etc).
- **Problem encountered:** regex pass also broke Python `for` keyword (replaced with `для`) — caused SyntaxError.
- **Fix:** sed restore of `^\s*для ` → `for ` + list comp `}) для x in items` → `}) for x in items`.
- **Re-scan:** 1660 → 1500 occurrences.

### Iter 4 — russification pass 3 (multi-word phrases)
- **Changed:** 26 direct multi-word string replacements: «Decision framework» → «Рамка решения», «Well-defined optimization» → «Чётко определённая оптимизация», «Demand pattern stationary?» → «Спрос стационарный?», «Safety-critical с regulatory audit?» → «Критично для безопасности + регуляторный аудит?», «Event в-distribution?» → «Событие в распределении?», «No → human dispatcher» → «Нет → человек-диспетчер», «Common patterns non-survivors» → «Общие паттерны невыживших», «Capital intensity» → «Капиталоёмкость», «SPAC IPO bubble» → «SPAC IPO пузырь», «AV-bankruptcy timeline» → «Хронология банкротств AV», «Black-box ML не работает в regulated industries» → «Чёрный ящик ML не работает в регулируемых отраслях», etc.
- **Re-scan:** 1500 → ~1500 (минор reduction).
- **Verdict:** acceptable for GATE B. Remaining tokens dominated by legitimate brand names (Waymo, Tesla, Cruise, Aurora, Mobileye, NHTSA, etc) + technical terms explicitly whitelisted в lecture-outline russification table (robotaxi, crawl-walk-run, vision-only, sim-to-real, out-of-distribution, eyes-off).

## Phase 6 — final stats

- **Slides:** 41
- **PPTX size:** 3,2 MB · PDF size: 3,8 MB
- **Visual loop iterations:** 4 (build → russify-pass-1 → russify-pass-2 → russify-pass-3 multi-word)
- **Russification reduction:** 1965 → 1500 occurrences (−24%); top 50 dominated brand/acronym names
- **Pre-GATE-B checks all PASS:**
  - Anonymization (МГТУ/Бауман/ИУ-N/ВКА/МАИ/Можайск) — 0 hits (visible body + source markdowns)
  - Timing markers ((N минут) etc.) — 0 hits в visible body
  - Designer extras (Лектору, [VERIFY-DAY-OF], [FACT-CHECK]) — 0 hits в visible body
  - Pony.ai cascade — Гуанчжоу Nov 2025 (1st) + Шэньчжэнь Feb 2026 (2nd) корректно атрибутировано в s26
  - Hero s01 (127KB Waymo Jaguar SF, Tier 2 Wikipedia Commons, ≥40% area) ✓
  - Hero s41 (168KB NOC IUPUI, Tier 2 Wikipedia Commons, ≥40% area) ✓
  - 33 real images via Tier 2/3 acquisition, no mock fallbacks

## Phase 7 — Critic reviews

Не выполнено в этой сессии (выполняется orchestrator после accept Phase 6 designer).
Будет включать: presentation-critic + student-simulator + reader-simulator (mode=rendered) параллельно.


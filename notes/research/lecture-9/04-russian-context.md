# 04 — Russian Context (Aerospace/Defense AI, open sources only)

**Принцип строгости.** Только открытые источники. Где источник — RIA/TASS/Russian gov press без independent verification, явно помечено «непроверено». Где есть конфликт между Russian и Western sources — оба указаны.

**Симметрия с lec-07 (medicine).** Глобальная основа + российский слой (Роскосмос для спутников, отечественные БПЛА, отечественные AI startups в гражданском dual-use, академическая база). Не пропаганда, не апология; вопрос «что есть на открытом уровне».

---

## 1. Государственная политика и governance

### 1.1 AI как государственный приоритет
- **National AI Decree 2024 (May).** Unmanned systems + autonomous vehicles + AI = critical для global competitiveness. Цель к 2030: top-10 nations в R&D spending; domestic R&D ≥2% GDP; double private-sector investment в innovation.
- **AI budget 2025–2027:** ~26.49B RUB федеральные allocations на AI projects (точная разбивка — `[VFY-day-of]`).
- **Presidential Decree #116 (Feb 26, 2026).** Commission on AI Development под Президентом — highest-level coordination для domestic LLMs, advanced AI services, computing infrastructure, electronic component base, energy supply.
- **Defense AI department.** В Минобороны создан specialized department for AI development (точная дата создания/название не публикуются). Vasily Elistratov — public face oversight.
- **Sber × China collaboration (Dec 2024).** Putin приказал Sber координировать AI research с Китаем; roadmap deliverable Apr 30, 2025.

Источники: [CSIS — Russia drone ecosystem](https://www.csis.org/analysis/how-russia-building-sovereign-drone-ecosystem-ai-driven-autonomy), [Defense News — Russian defense plan AI push 2024](https://www.defensenews.com/global/europe/2024/08/16/russian-defense-plan-kicks-off-separate-ai-development-push/), [CNAS — Role of AI in Russia's Confrontation with the West](https://s3.us-east-1.amazonaws.com/files.cnas.org/documents/Russia-AI_2024-final.pdf), [RUSI — Struggling not crumbling Russian Defence AI](https://www.rusi.org/explore-our-research/publications/commentary/struggling-not-crumbling-russian-defence-ai-time-war).

### 1.2 Технополис «ЭРА» (Anapa, est. 2018)
- **Что.** Defense R&D полигон Минобороны для робототехники / AI / cybersecurity / суперкомпьютеров.
- **Strategic session Oct 4, 2024.** Manturov + Military-Industrial Commission + MoD reps; emphasis на ground + maritime robots.
- **Capability claims.** Equipment returning from Ukraine retrofitted: remotely controlled fire modules, automatic target tracking, propulsion systems. Verifiable independently — limited.

Источник: [Army Recognition — Technopolis ERA strategy session 2024](https://armyrecognition.com/focus-analysis-conflicts/army/analysis-defense-and-security-industry/military-robots-central-to-russias-strategy-with-critical-priority-confirmed-at-technopolis-era).

---

## 2. Роскосмос и спутниковая ИИ-аналитика

### 2.1 ТЕРРА ТЕХ (subsidiary Роскосмос)
- **Год основания.** 2017.
- **Что делает.** Digital services on spatial data — satellite imagery + drone aerial + external data; ML-классификация и аналитика через unified web interface.
- **BRICS agriculture monitoring.** TerraTech geoinformation tech → basis для monitoring agricultural lands в BRICS countries (соглашение 2024).
- **Расхождение между российскими заявлениями и Western analysis.** Эти соглашения существуют; объём и effectiveness — не публикуются.

Источники: [Scribd — TerraTech brochure](https://www.scribd.com/document/687804157/TerraTech-Brochure), [TASS — BRICS agricultural monitoring](https://tass.com/science/1988049).

### 2.2 СКАНЭКС (group)
- **Что.** Единственная в РФ/СНГ компания, напрямую receiving Earth observation satellite data на собственные ground stations.
- **Archive.** 3.5M+ images Russian territory + neighbours.
- **Yandex.Maps.** Эксклюзивный поставщик satellite data для Яндекс.Карт.
- **Court restriction.** Москва запретила Сканэксу распространять снимки разрешением >2 м (security restriction).
- **AI claims.** Open materials описывают automated processing pipelines, но specific ML-models / metrics не публикуются.

Источники: [ScanEx site](https://www.scanex.ru/), [TAdviser — ScanEx Group](https://www.tadviser.ru/index.php/Компания:Сканэкс_ГК), [SpaceWar — Moscow court ban](https://www.spacewar.com/reports/Moscow_court_upholds_ban_against_satellite_image_distributor_999.html).

### 2.3 СПУТНИКС (AFK Sistema → дочерняя Роскосмоса по контрактам)
- **Что.** 100+ cubesats designed/produced с 2013.
- **Zorkiy-2M constellation.** 3 на орбите, ещё 3 готовы к запуску до конца 2025; multispectral camera 2.5m resolution / 4 spectral bands.
- **Roscosmos forward contracts.** Up to 1.4B RUB (~$14.3M) бюджет на покупку remote sensing data с private satellites в 2024.
- **Sitronics Group (AFK Sistema, parent).** В 2024 развернул 45 commercial cubesats для ship-tracking — **53%** всех Russian satellite deployments этого года.

Источники: [Aviation Week — Roscosmos private partnership](https://aviationweek.com/space/budget-policy-regulation/roscosmos-turns-private-company-earth-observation-constellation), [Sputnix EO data platform](https://sputnix-group.ru/en/articles/sputnix-launches-earth-observation-data-platform), [TASS — Roscosmos buys private EO data](https://tass.com/science/1894855), [TS2 Tech — Russia space 2025](https://ts2.tech/en/from-sputnik-to-sanctions-inside-russias-space-satellite-industry-2025/), [TAdviser — Satellite production](https://tadviser.com/index.php/Article:Satellite_production_in_Russia).

### 2.4 Sber GigaChat на МКС (2025)
- **Что заявлено.** Sber's GigaChat AI deployed on ISS Russian segment, fall 2025 (cosmonauts на следующем запуске Nov 27); claim: double resolution от 1m/px → 0.5m/px для спутниковых снимков.
- **Статус.** Single-source (Russian-side announcements); independent verification отсутствует.
- **Bakanov** (Roscosmos head) — публично анонсировал; verification зависит от ISS operational data.

Источники: [Technology.org — Gigachat на ISS](https://www.technology.org/2025/06/04/russia-plans-to-deploy-gigachat-ai-on-space-station-this-fall/), [Jerusalem Post — Russia Gigachat ISS](https://www.jpost.com/business-and-innovation/all-news/article-856428).

---

## 3. Российские БПЛА и AI-component (открытые данные)

### 3.1 Geran-2 (на основе Shahed-136 — Iranian)
- **Производство.** Alabuga SEZ (Tatarstan) — late 2025 >5000 drones/month. Total produced >26 000 к late spring 2025; план >40 000 к концу 2025 (`[VFY-day-of]`).
- **AI evolution.** Wreckage analysis (Ukrainian recovery) — NVIDIA Jetson onboard, high-res cameras, thermal-vision modules; field-programmable gate arrays для EW resistance.
- **2026.** Equipping passive radar seeker warheads — anti-radiation variant (March 29, 2026).
- **Caveat.** Onboard "autonomy" claims — частично подтверждены wreckage analysis, но real-time decision quality vs operator override unclear. **Большая часть** strikes остаётся operator-guided + GPS-guided.

Источники: [Autonomy Global — Russia mass producing Geran-2](https://www.autonomyglobal.co/what-the-other-guys-are-doing-russia-mass-producing-ai-enabled-geran-2-drones/), [Meta-Defense — Geran-2 anti-radar evolution](https://meta-defense.fr/en/2026/04/03/geran-2-anti-radar-evolution-drones/), [ORF Online — Russia drone warfare evolution](https://www.orfonline.org/expert-speak/the-evolution-of-russia-s-drone-warfare-in-ukraine), [Greanville Post 2026](https://www.greanvillepost.com/2026/05/07/more-bang-for-the-buck/), [FDD — Russian Shahed maker recruiting](https://www.fdd.org/analysis/2026/04/24/russian-shahed-drone-maker-recruiting-for-new-unmanned-systems-brigade/).

### 3.2 Lancet (Kalashnikov / Zala Aero Group)
- **Заявленный AI.** Kalashnikov marketing: «autonomously find and hit target».
- **Реальное состояние.** Field analysis (CSIS, Modern War Institute) — autonomous-target-recognition rolled back к 2024; videos без "Target Locked" UI. **CSIS:** «Conversations с Ukrainian technical specialists suggest terminal phase autonomy doubtful».
- **Урок (для лекции).** Demo (test conditions / lab) ≠ production (full combat variance). Premature autonomy claims → product recall.

Источники: [Kyiv Post — Lancet kamikaze overview](https://www.kyivpost.com/analysis/23923), [CSIS — Russia probably hasn't used AI weapons in Ukraine](https://www.csis.org/analysis/russia-probably-has-not-used-ai-enabled-weapons-ukraine-could-change), [Automated Decision Research — autonomous functions Ukraine](https://automatedresearch.org/news/weapons-systems-with-autonomous-functions-used-in-ukraine/), [Breaking Defense — Russia autonomous swarms](https://breakingdefense.com/2025/01/inside-russias-plan-to-build-autonomous-drone-swarms/).

### 3.3 KUB-BLA (Zala / Kalashnikov)
- **Marketing claims.** AI-powered loitering munition; real-time CV target recognition.
- **Real evidence.** Lawfare и automation research questioning — «If had real ML autonomy, would publicly market it; Rostec/Kalashnikov haven't». Likely operator-assisted, не fully autonomous.

Источник: [Automated Decision Research — KUB-BLA](https://automatedresearch.org/news/weapons-systems-with-autonomous-functions-used-in-ukraine/).

### 3.4 Orion (Kronshtadt Group, MALE drone)
- **Что.** Russia's medium-altitude long-endurance unmanned drone, аналог Predator / Reaper class; production с 2011.
- **2024–2025 deployment.** Ship-based variant deployed для Black Sea operations (ISW Feb 2025); вооружение — guided missile, Banderol bombs.
- **AI claims.** Открытые data не подтверждают onboard AI; remote-piloted с ground station.
- **Combat losses.** Ukrainian anti-aircraft drones downed Orion (2025).
- **Export.** January 2026 — one system delivered to Ethiopia.

Источники: [Wikipedia — Kronshtadt Orion](https://en.wikipedia.org/wiki/Kronshtadt_Orion), [Defense Express — Orion downed by Ukrainian drone](https://en.defence-ua.com/news/ukrainian_anti_aircraft_drone_downs_russian_orion_uav_a_carrier_of_banderol_missiles_and_bombs-15264.html), [Euromaidan — ISW ship-based Orion](https://euromaidanpress.com/2025/02/02/isw-russia-deploys-ship-based-orion-drones-as-ukraine-cripples-black-sea-fleet/).

### 3.5 Forpost / Forpost-R (Ural Plant of Civil Aviation, licensed IAI Searcher)
- **Что.** Licensed Israeli design produced с 2012; Forpost-R — Russian variant с extended endurance (18 h) + small laser-guided bombs.
- **AI.** Open materials — no AI-onboard claims.

Источник: [Kyiv Independent — Russian drone arsenal opinion](https://kyivindependent.com/opinion-a-look-at-the-drone-arsenal-russia-uses-against-ukraine/).

### 3.6 BAS-200 (Russian Helicopters / Rostec) — unmanned VTOL
- **Что.** Unmanned helicopter system для Arctic ship-based missions; icebreaker support.
- **AI.** Заявлен **adaptation** для Arctic conditions; конкретные AI-components не публикуются.

Источник: [Army Recognition — BAS-200 Arctic icebreakers](https://www.armyrecognition.com/news/navy-news/2024/russia-deploys-bas-200-drones-to-support-arctic-icebreaker-operations).

---

## 4. Российская боевая C2 (command-and-control) с AI-elements

### 4.1 Svod / Глаз-Гроза-ЗОВ (2024–2025)
- **Svod Tactical Situational Awareness Complex.** Announced August 2025. Active development since 2024; experimental field deployment в Russian units от Fall 2025.
- **Glaz/Groza digital ecosystem.**
  - **Glaz** — applications для drone operators (recon, geomapping).
  - **Groza** — fire-control + mission management environment.
  - **ZOV Maps platform** — geospatial mapping core.
- **Связь с lec-09.** Это **попытка** Russian network-centric warfare; performance в combat — uneven по CSIS.

Источник: [CSIS — Russia C2 AI warfare](https://www.csis.org/analysis/how-russia-reshaping-command-and-control-ai-enabled-warfare).

### 4.2 Surface-to-air missile AI (S-300, S-400, Pantsir, S-350)
- **Заявленный AI.** Pantsir S-1, S-300, S-400, S-350 Vityaz — "AI-enabled" target tracking, prioritisation.
- **Combat claims.** Russia заявляет успешные перехваты US-supplied ATACMS, Storm Shadow / SCALP-EG.
- **Western analysis.** Точная роль AI vs classic radar tracking + Kalman filtering — unclear; Russian "AI" labels часто маркетинговые.

Источник: [Jamestown — Russia AI military strategy](https://jamestown.org/russia-capitalizes-on-development-of-artificial-intelligence-in-its-military-strategy/).

---

## 5. Российские AI startups / dual-use

### 5.1 VisionLabs (Москва, 2012)
- **Что.** Computer vision / facial recognition / object recognition / AR/VR. LUNA platform — real-time recognition millions of faces.
- **Government ties.** Sberbank купил 25% в 2017; NIST global ranking — top-10 (часто 1st place vs DeepGlint).
- **Deployments.** 60+ Russian educational institutions; 20+ banks; school + university surveillance (post-2021 expansion).
- **Defense connection.** Не прямой defense customer, но Sberbank ownership + Rostec parallel (NTech Lab 12.5%) → dual-use risk.
- **Sanctions.** Под US/EU sanctions (2022 за export to Iran allegations).

Источники: [Skolkovo — VisionLabs $5.5M Series A](https://sk.ru/news/skolkovos-startup-visionlabs-raised-55-million-in-series-a-round-from-sistema-vc-to-expand-its-global-operations/), [Biometric Update — VisionLabs 60+ schools](https://www.biometricupdate.com/202111/visionlabs-biometrics-deployed-at-more-than-60-universities-schools-in-russia), [Moscow Times — Russia facial recognition network](https://www.themoscowtimes.com/2019/11/12/russia-building-one-of-worlds-largest-facial-recognition-networks-a68139), [Nanalyze — Top 10 Russian AI startups](https://www.nanalyze.com/2018/06/10-russian-artificial-intelligence-startups/), [Coda Story — Russia facial recognition](https://www.codastory.com/surveillance-and-control/russia-facial-recognition-networks/).

### 5.2 Cognitive Pilot (Sber + Cognitive Technologies)
- **Что.** Moscow-based joint venture, основные направления — agricultural autonomous machinery (Cognitive Agro Pilot), urban transport, rail.
- **Defense connection.** Не прямой defense вендор; но technology stack (CV + radar sensors для autonomy без GNSS) — dual-use потенциал. **Не идентифицирован open-sources как defense supplier**.
- **Plans.** Production scale до 50 000 systems/year.

Источники: [Cognitive Pilot site EN](https://en.cognitivepilot.com/), [TASS — Cognitive Pilot scale-up](https://tass.com/economy/1558529), [Robotics 24/7 — Cognitive Pilot agro autonomy](https://www.robotics247.com/article/cognitive_pilot_cto_discusses_agricultural_autonomy).

### 5.3 Aerostate (если verifyable)
- **Запрос не нашёл подтверждённой информации** в WebSearch — компания «Aerostate» как Russian aviation-weather AI startup в open international sources не подтверждается.
- **Возможные интерпретации.** Aerostate может быть локальной российской компанией без international visibility; либо опечатка / альтернативное название для другой компании; либо просто не активна в English-language sources.
- **Recommendation для лекции.** **НЕ упоминать** Aerostate в speech / chapter / slides без явного дополнительного источника. Использовать Cognitive Pilot или VisionLabs как примеры Russian dual-use AI startups.

### 5.4 SR Space (Russian small-sat launcher)
- **Что.** Small-sat launcher startup; large team к 2024; engine component tests Feb 2025.
- **Status.** Pre-revenue / early stage; не AI-focused; контекст — параллельный рост private space sector РФ под санкциями.

Источник: [NewSpace Index — SR Space launcher](https://www.newspace.im/launchers/sr-space).

---

## 6. Российская академия (открытое)

### 6.1 МГТУ им. Баумана (МГТУ)
- **Факультет «Информатика, искусственный интеллект и системы управления» (ИУ).**
- **Декан Андрей Пролетарский (public statements).** «ИИ применим как potential adversary и как advisor; effectiveness зависит от того, как и кто обучит сеть».
- **Магистратура «Программно-алгоритмическое обеспечение систем ИИ»** в рамках направления «Ракетные комплексы и космонавтика».
- **Профили подготовки** — «Системы управления ракет-носителей и космических аппаратов» + «Искусственный интеллект в системах обработки информации и управления».

Источники: [Bauman — кафедра ИИ](https://bmstu.ru/chair/tekhnologii-iskusstvennogo-intellekta), [Bauman — Факультет РКТ](http://rkt.bmstu.ru/), [Bauman — ИИ в МГТУ](https://bmstu.ru/news/iskusstvennyi-intellekt-v-mgtu), [Vuzopedia — IU фак ИИ](https://vuzopedia.ru/vuz/22).

### 6.2 ВКА им. А.Ф. Можайского (СПб)
- **Что.** Системообразующий politech университет Минобороны; ведущий обр.-научно-методологич. центр в области military-space activity, ИТ-телекоммуникаций, special information processing.
- **AI programs.** Faculty of Control Systems for Rocket and Space Complexes + Faculty of Special Information Technologies (information-analytical systems of special purpose).
- **Образование.** AI и data analytics — среди specialties; details про конкретные курсы и научные направления в открытом доступе ограничены.

Источники: [VKA Mozhaisky official](https://vka.mil.ru/), [TAdviser — ВКА им. Можайского](https://www.tadviser.ru/index.php/Компания:Военно-космическая_академия_имени_А._Ф._Можайского).

### 6.3 МАИ, СПбГУ, прочие
- **МАИ (Московский авиационный институт).** AI в aerospace context присутствует, но конкретные публичные программы / lab strategy — limited open visibility.
- **СПбГУ.** AI/computer science strong; defense connection — limited public material.

---

## 7. Sanctions Context — как ограничения западного AI влияют на РФ

### 7.1 NVIDIA / AMD export controls
- **H100 / H200 / Blackwell GPUs** под Tier-3 restrictions (Russia included).
- **Russia evasion.**
  - **Shreya Life Sciences (India)** — 1111 Dell PowerEdge XE9680 серверов (advanced GPUs внутри) shipped to Russia Apr–Aug 2024.
  - **Encrypted-text smuggling routes** через third countries (Fortune May 2026).
  - **$8.8B** Russian military production materials imports Jan–Oct 2023.
- **Implication для lec-09.** Russian AI defense critically зависит от **continued evasion success**. Это одновременно: (a) demonstrates resilience of supply chains; (b) shows sanctions framework is leaky; (c) **risk для West** — свои чипы могут оказаться в чужих weapons.

Источники: [Tom's Hardware — Indian firms funneled GPUs Russia](https://www.tomshardware.com/tech-industry/artificial-intelligence/indian-firms-secretly-funneled-amd-nvidia-ai-gpus-to-russia-sanctions-reportedly-skirted-on-hundreds-of-millions-of-dollars-of-hardware), [Fortune — chip smuggling encrypted texts](https://fortune.com/2026/05/13/nvidia-chip-smuggling-china-russia-iran-export-controls-supermicro/), [Introl — AI export controls 2025](https://introl.com/blog/ai-export-controls-navigating-chip-restrictions-globally-2025), [Sourceability — NVIDIA export controls](https://sourceability.com/post/export-controls-and-geopolitical-risks-test-ai-chip-supply).

### 7.2 Software / talent
- **Talent emigration 2022–2024.** Substantial AI-talent flight; Yandex, Tinkoff de-Russianized; Sber stayed.
- **Software sanctions.** Adobe / Autodesk / Microsoft / SAP suspended licensing для Russia. Workarounds — open source + grey market.
- **Implication.** Civilian AI ecosystem deteriorating; military AI продолжает наращивать в narrow domains (combat-feedback loop работает).

---

## 8. Где Russian context **прозрачно вписывается** в lec-09

| Раздел лекции | Russian кейс | Why это релевантно для МГТУ-аудитории |
|--------------|--------------|-----------------------------------|
| ISR / satellites | TerraTech BRICS agro / ScanEx | Реальный adoption case закрытой страны |
| Predictive maintenance | (нет прямого Russian аналога Skywise) | Gap — opportunity или risk |
| Mission C2 | Svod / Glaz-Groza-ZOV | Что строится прямо сейчас, видно из ОЛКа |
| Drone autonomy | Geran-2 evolution / Lancet rollback | **Очень pedagogical** — demo vs production |
| Counter-drone | (мало data) | Defensive gap для Russia после Ukraine drone war |
| LAWS treaty | Russia votes **against** UN resolutions | Понимание geopolitics |
| Sanctions / supply chain | NVIDIA Jetson в Geran-2 | Hardware dependency = strategic risk |
| Academic | МГТУ ИИ + ВКА Можайского | Студенты могут увидеть путь в industry |

---

## 9. Volatile data + uncertainty flags

| Cell | Why volatile |
|------|--------------|
| Alabuga Geran-2 production rate | Updated monthly via OSINT |
| Russian AI federal budget allocations | Budget cycle dependent |
| Specific Russian C2 deployment status (Svod, etc.) | Single-source disclosure |
| Sber GigaChat ISS deployment | Single Russian-side announcement |
| Aerostate startup | **NOT verified in international sources — DO NOT include** |
| Cognitive Pilot defense role | Public material не подтверждает defense supply |
| Real autonomy in Lancet/Geran | Conflicting Russian marketing vs Western analysis |

---

## Key takeaways для plan лекции

1. **Russian context — symmetric c lec-07.** Global frame + Russian layer — не доминирующий блок, но **видимый и честный**: что есть в open data, что нет.

2. **Strongest Russian кейсы для slides:**
   - **Geran-2 AI evolution** — strict-in failure (demo vs production) + supply chain dependency.
   - **Lancet ATR rollback** — explicit lesson: «AI marketing ≠ AI deployment».
   - **TerraTech / Sputnix** — что действительно работает в гражданском ML over satellite imagery.
   - **МГТУ / ВКА Можайского** — академический context, где сидят студенты.

3. **Что НЕ упоминать без подтверждения:**
   - Aerostate (нет verifiable open source).
   - Specific Russian command-system "AI capabilities" без явной ссылки на Russian official sources + Western verification.

4. **Pedagogical balance.** Не повторять ни Russian propaganda («мы — leader»), ни Western dismissal («у них ничего нет»). Реальность: Russia адаптируется narrow military domains; civilian AI underweight + degrading; supply chain — Achilles' heel.


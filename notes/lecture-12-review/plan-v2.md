---
lecture_number: 12
lecture_title: "AI в автоматизации производства и цифровые двойники"
module: 2
learning_outcomes: [LO2, LO5, LO7]
audience: "студенты-инженеры 3 курса (универсальная, не отраслевые специалисты)"
duration_min: 75
plan_version: 2
created: 2026-05-21
revised: 2026-05-21
issue: 133
status: draft
parts: 2
parts_files: ["plan-v2.md", "plan-v2-part2.md"]
length_lines: 535
length_lines_total_all_parts: 778
keystone_axis: "Шкала автономии AI в производстве A0→A1→A2→A3 (наблюдать → советовать → замыкать петлю → действовать автономно); цифровой двойник — мост, который позволяет подниматься выше без катастроф. Это шкала автономии AI (A0–A3), отличная от ISA-95 архитектурных слоёв L0–L2 в lec-11 §5.3 (anchors: SAE J3016 + ISO 22989)."
failure_share_target: ">=30% strict-in holistic (chapter, slides, speech)"
chapter_target_words: 30000
hero_s01_plan: "Кадр с Hannover Messe 2026 — оператор стоит у физической линии, на полупрозрачном overlay сцена NVIDIA Omniverse / Siemens Digital Twin Composer того же оборудования; foreshadow keystone (мост между физикой и AI). Tier 1: NVIDIA / Siemens press kit (blogs.nvidia.com + press.siemens.com — публичные пресс-релизы CES 2026 / Hannover Messe 2026)."
hero_s39_plan: "Toyota Digit на сборочной линии RAV4 — гуманоид перевозит контейнер с деталями между станциями (внутрицеховая логистика как мост к Лекции 13 «AI в логистике, цепях поставок и транспорте»). Tier 1: Agility Robotics press kit; Tier 2: Wikimedia Commons (Toyota images); Tier 3: Toyota newsroom; Tier 4: Reuters YouTube thumb."
hero_s07_plan: "Siemens Digital Twin Composer screenshot реального UI с time scrubbing. 6-tier acquisition (см. Section 6)."
media_target_share: ">=50% слайдов с real-image вставками (≥17 из ~33)"
prerequisites: ["lec-03 архитектуры AI-систем", "lec-07 HITL/FDA", "lec-11 discrete vs process taxonomy + 5 cornerstone vendors + ГОСТ Р 57700.37-2021"]
revision_basis: "SYNTHESIS-plan-v1.md + owner decisions Q1-Q7 + reader/methodology P1+P2"
---

# План v2 — Лекция 12. AI в автоматизации производства и цифровые двойники

> **Контекст в curriculum.** Лекция 11 дала *таксономию* (discrete vs process) и *вендорский ландшафт* (Siemens / AVEVA / Honeywell / Cognite / Uptake) + первое упоминание ГОСТ Р 57700.37-2021 и российских цифровых двойников. Лекция 12 строит на этом фундаменте *операционную* ось — **до какого уровня автономии AI можно поднять процесс**, и *архитектурный* мост — **цифровой двойник** как механизм, который позволяет это сделать без катастроф. Лекция 13 расширит scope от одного цеха к цепочке поставок и транспорту.

> **Что изменено в v2** (сводка для трассировки): rename axis L0–L3 → A0–A3 (SAE J3016 + ISO 22989, disambiguation от ISA-95 lec-11 §5.3); Yokogawa FKDPP angle переориентирован на «twin-as-RL-sandbox»; Tesla 2018 hero в §5 → Southeast Asian Port 2024; dedicated §4.5 «A3» 2 мин (компенсация §6 8→6); ГОСТ Р 57700.37-2021 + Норникель flotation добавлены в §7; Kritzinger 2018 taxonomy в §1; 4 missing locked numbers; inline gloss 9 jargon terms; 1-фраза-якорь 4 альтернатив; §7 career расширен; Section 1 «вторая мысль» сжата; 3 concrete failure examples; 4 Russification additions; hero s07 6-tier; s05 vector diagram; bridge s39 lock; Q&A backup в Section 11; worked example §5 фарма+FDA.

---

## Section 1 — Большая идея (Big Idea)

**В одном предложении:** студент 3 курса должен понимать, что современная автоматизация производства — это не «робот вместо человека», а *шкала автономии AI*, где каждая ступень (от пассивного наблюдения до автономного действия) требует своего архитектурного контура, и цифровой двойник — это единственный известный способ безопасно подниматься по этой шкале.

**Развитие.** Когда инженер 3 курса слышит «AI на заводе», у него часто формируется одна из двух искажённых картин. Либо «полностью автономный цех без людей» (это медиа-образ из Tesla 2018 и плакатов Industry 4.0), либо «модный чатбот для оператора» (это интерфейсный stereotype 2024–2025). Обе картины ложны. Реальная производственная автоматизация в 2026 году устроена как **многоуровневая шкала автономии**, где AI занимает разные роли: на нижних ступенях — пассивный наблюдатель (vision-инспекция, прогностическое обслуживание), на средних — советчик оператору (диспетчерское управление, предсказание тревог), на верхних — со-контроллер в замкнутой петле (оптимизация параметров процесса), и только на самой вершине — автономный агент (полностью замкнутый RL-контур, который в 2026 году в production пока встречается единично).

Эта шкала неотделима от **цифрового двойника** — рабочего контура (математическая модель оборудования + поток данных с реальных датчиков + AI-слой, умеющий предсказывать поведение и тестировать решения *до* их применения к физическому железу). Без двойника подъём выше второй ступени превращается в «угадай как RL отреагирует на ситуацию, которую он раньше не видел» — путь к Tesla 2018 (cross-ref lec-11 §2.4) и Southeast Asian Port 2024 (списание 12 миллионов долларов на проект, не дошедший до промышленной эксплуатации).

**Вторая мысль (сжатая, forward-pointer на §5):** на каждой ступени есть *задачи, для которых AI не подходит* — раздел §5 даёт 10 формальных критериев «не применяй AI / альтернатива лучше». Инженер обязан **уметь отказать AI** — часть LO8.

**Третья мысль — экономическая.** Рынок цифровых двойников растёт с 36,19 миллиарда долларов в 2025 году до прогнозируемых 180,28 миллиарда к 2030 году (среднегодовой темп роста 37,87%) [PatSnap / StartUs 2026]. Параллельный рынок AI в производстве — 155,04 миллиарда долларов 2030 (CAGR 35,3% 2026–2030) [Standard Bots / ifactoryapp 2026]. Промышленный AI поверх OPC UA + MQTT — 17,15 миллиарда долларов уже в 2026 [TheElec 2026]. Параллельно — **75% проектов цифровых двойников не дают ROI из-за слабого слоя данных** [context-clue.com 2026]. Только 11% проектов цифровых двойников в нефтегазе дают ожидаемый эффект; только 14% пользователей говорят, что технология соответствует ожиданиям [EY / DataMintelligence 2026]. Gartner прогнозирует отмену 40% агентных AI-проектов к 2027 году. Студент столкнётся с **разрывом ожиданий** между маркетингом и инженерной реальностью в первый же год работы. Эта лекция учит, как читать вендорские слайды критически.

**Четвёртая мысль — антропологическая.** На вершине шкалы есть **гуманоид-робот**. BMW Plant Leipzig запустил первый европейский пилот гуманоида в производстве в 2026 году; Toyota развернула роботов Digit от Agility Robotics на сборочной линии RAV4 (7+ единиц на внутрицеховой логистике). Это не «робот заменил рабочего» — это новый тип физического агента, который встраивается в шкалу автономии как мобильная исполнительная единица третьей ступени. Студенту важно понимать: гуманоид 2026 — это **результат пятнадцати лет работы над цифровыми двойниками, edge AI и симуляцией**, а не «прорыв в железе».

---

## Section 2 — Keystone-axis

### Формулировка

**Шкала автономии AI в производстве: A0 (наблюдать) → A1 (советовать) → A2 (замыкать петлю) → A3 (действовать автономно). Цифровой двойник — мост, который позволяет подниматься по шкале без катастроф.**

**Anchor:** SAE J3016 (Levels of Driving Automation) и ISO/IEC 22989 (Information technology — Artificial intelligence — Concepts and terminology) — обе используют термин «autonomy levels». Шкала A0–A3 — адаптация этих стандартов под производство, а не индустриальная норма IEC/ISO.

**Disambiguation от lec-11 (mandatory):** это **шкала автономии AI (A0–A3)**, отличная от **ISA-95 архитектурных слоёв L0–L2** (поле → контроллер → SCADA → MES → ERP), упомянутых в lec-11 §5.3. Один и тот же буквенный префикс — разные семантики. На s02 keystone в первой строке: «Не путать с ISA-95 L0–L2 (lec-11 §5.3): там — *слои архитектуры*, здесь — *степени автономии AI*».

### Почему именно эта ось

1. **Она оперативная, а не таксономическая.** Лекция 11 дала *таксономию типов производства* (discrete vs process — что вы делаете). Лекция 12 даёт *операционную шкалу* (как далеко вы доверяете AI принимать решения). Эти две оси ортогональны: на дискретном производстве можно быть на A0, а на процессном — на A2 (как Yokogawa FKDPP в JSR chemical plant 35 дней в 2022).
2. **Она объясняет, почему 95% AI-проектов не доходят до production.** Большинство пилотов застревают между A1 и A2 — потому что подъём со «советует» на «замыкает петлю» требует *архитектурного скачка*: нужен цифровой двойник (как safe sandbox), нужен механизм отката, нужна сертифицируемая безопасная зона действия. Без двойника этот скачок — слепая вера.
3. **Она встроена в архитектурную реальность 2026.** OPC UA + TSN + edge AI inference <10 мс — это не «buzzwords», это *технологические условия*, без которых A2 невозможен. На A0–A1 хватает MQTT + cloud-задержки в секунды; на A2 нужен детерминированный real-time стек.
4. **Она пронизывает все разделы.** Каждый раздел лекции — это либо *подъём по ступени* (§2 A0, §3 A1, §4 A2, §4.5 A3), либо *показатель границы* (§5 — почему попытки прыгнуть на A3 без двойника = Tesla 2018 и Southeast Asian Port 2024).
5. **Она ортогональна OODA из lec-09 и discrete/process из lec-11.** OODA — *цикл принятия решения для одного агента*. Шкала автономии — *уровень доверия, который мы делегируем AI*. Lec-09 OODA фокусируется на *скорости* цикла; lec-12 шкала — на *границах делегирования*.

### Четыре ступени — определения и примеры

| Уровень | Название | Что AI делает | Кто принимает решение | Пример 2026 |
|---|---|---|---|---|
| **A0** | Наблюдать | Классифицирует / предсказывает события, выдаёт сигнал | Оператор / другая система | Vision-инспекция качества (Indus Vision FP 0,1–2%), прогностическое обслуживание (Deloitte 10:1 ROI за 2 года) |
| **A1** | Советовать | Предлагает действие, обосновывает выбор | Оператор (явное согласие) | MES-advisory, предсказание тревог в SCADA, PLC Copilot с инженером в loop |
| **A2** | Замыкать петлю | Сам корректирует параметры в безопасной зоне действия | Оператор может вмешаться, но не обязан | Energy-optimization, micro-adjust некритических параметров; Yokogawa FKDPP в JSR 35 дней |
| **A3** | Действовать автономно | Принимает решения без человека в loop | AI (с safety guardrails) | Toyota Digit на RAV4, BMW Leipzig pilot — **единичные кейсы 2026**; основная масса производства = A0–A2 |

**Disclaimer на s02 keystone (visible):** «A3 в 2026 — единицы кейсов в production; основная масса A0–A2. Это асимметрия, не недостаток шкалы».

### Цифровой двойник как мост

Цифровой двойник — **архитектурный артефакт**, выполняющий три функции:
1. **Тестирует управляющие решения в симуляции** до их применения к железу. Без этого подъём с A1 на A2 — слепая вера.
2. **Хранит state физического процесса** в форме, доступной для AI-инференса (включая редкие сценарии, отсутствующие в исторических данных).
3. **Позволяет откатить** изменения и понять, *почему* AI принял решение — основа для регуляторного аудита (FDA 21 CFR Part 11, GMP, ГОСТ Р 57700.37-2021).

В 2026 году появилось два знаковых релиза: **Siemens Digital Twin Composer** (CES 2026 → Xcelerator Marketplace mid-2026) объединяет 2D+3D twin + real-time data + сцену NVIDIA Omniverse с механизмом back/forward time scrubbing (можно «промотать» процесс назад и проверить, что было бы с другим решением). **NVIDIA Omniverse + Cosmos** на Hannover Messe 2026 представили фундационные модели *физического AI* — обучение в симуляции с переносом на реальное оборудование.

### Как ось предъявляется в Разделе 0

**Keystone-слайд (s02 после cover) — единственный слайд, явно показывающий шкалу.** Заголовок: «Шкала автономии AI в производстве A0–A3». Под ним — 4 ступени с одним примером 2026 на каждой и подписью «Цифровой двойник — мост между A1 и A2». Первая строка под заголовком: «Не путать с ISA-95 L0–L2 (lec-11): там слои архитектуры, здесь степени автономии AI». Disclaimer: «A3 в 2026 — единицы кейсов».

**Этот слайд предъявляется ДО первого погружения в A0.**

После s02 идёт s03 — «Шесть аббревиатур, без которых дальше не пройти»: OT (Operational Technology — производственные ИТ), IT, OPC UA (Open Platform Communications Unified Architecture — стандарт семантики данных), MES (Manufacturing Execution System — цеховой исполнительный уровень), SCADA (Supervisory Control and Data Acquisition — диспетчерское управление), RL/MPC. Это служебный слайд, аналог lec-11 §0.2.

---

## Section 3 — Map of 75-min lecture (минутный бюджет)

| § | Раздел | Минуты | LO | Failure-bucket (strict-in) | Hero |
|---|---|---:|---|:---:|:---:|
| **§0** | Cover + keystone (шкала A0–A3) + 6 аббревиатур + roadmap | 5 | LO5 | – | s01 (hero) |
| **§1** | Что такое цифровой двойник в 2026 (Kritzinger taxonomy, ГОСТ-определение, рынок, провал 75%) | 10 | LO2, LO5 | ✅ 4 мин (75% fail + Southeast Asian Port + 11%/14% gap) | s07 |
| **§2** | A0 — Наблюдать (vision QC, predictive maintenance). Когда vision НЕ применим | 10 | LO2, LO7 | ✅ 4 мин (FP cascade, vision границы, metrology альт.) | s10, s12 |
| **§3** | A1 — Советовать (MES advisory, alarm prediction, PLC Copilot). Когда LLM НЕ применим к PLC | 10 | LO2, LO7 | ✅ 4 мин (ChatGPT-PLC MOV %M99999, альт.: purpose-built + engineer-in-loop) | s16 |
| **§4** | A2 — Замыкать петлю (closed-loop, RL process control). Yokogawa FKDPP + twin-as-sandbox | 10 | LO2, LO5, LO7 | ✅ 4 мин (sim-to-real gap concrete, hazardous factors, альт.: MPC) | s20, s22 |
| **§4.5** | A3 — единичные кейсы и почему ось обрывается на A2 для 95% производства | 2 | LO5, LO7 | ✅ 1 мин (regulatory + cost + complexity blockers) | s23a |
| **§5** | Где AI НЕ применим — провалы и альтернативы (densest failure-bucket); Southeast Asian Port intro hero | 15 | LO2, LO7 | ✅ 15 мин полностью in-bucket | s25, s27, s29 |
| **§6** | OT/IT архитектура 2026 (OPC UA + TSN + edge AI). Lighthouse Network 220+ | 6 | LO5 | ✅ 1 мин (11%/14% expectation gap mention) | s31, s33 |
| **§7** | Российский контекст (ГОСТ Р 57700.37 + КАМАЗ + Росатом + Норникель) + карьерный мост | 5 | LO5, LO7 | – | s35 |
| **§8** | Закрытие + мост к Лекции 13 «AI в логистике, цепях поставок и транспорте» | 2 | – | – | s39 (hero) |
| | **Total** | **75** | | **Strict-in: ~33 мин (44%)** | |

### Failure-share recalculation (explicit)

- **§1:** 4 мин (75% fail + Southeast Asian Port + 11%/14% gap + Kritzinger «Model/Shadow не twin» как negative definition)
- **§2:** 4 мин (vision FP cascade 1%×10K, vision границы, альт.: process redesign + metrology)
- **§3:** 4 мин (ChatGPT MOV %M99999 illegal addr, альт.: purpose-built + engineer-in-loop)
- **§4:** 4 мин (RL sim-to-real concrete thermal-loss example, hazardous factors, альт.: MPC)
- **§4.5:** 1 мин (A3 blockers: regulatory + cost + complexity)
- **§5:** 15 мин полностью in-bucket (Southeast Asian Port intro + 10 критериев + матрица альтернатив + worked example фарма+FDA + 5 вопросов вендору)
- **§6:** 1 мин (11%/14% expectation gap mention)

**Sum: 33 мин из 75 = 44% strict-in.** Превышает 30% порог. Размазано по 7 разделам (не сконцентрировано). Голистическое требование выполнено.

### Slide budget estimate

~33 слайда: s01 (cover hero) + s02 (keystone A0–A3) + s03 (6 аббревиатур) + s04 (roadmap) + 5 на §1 (s05–s09) + 5 на §2 (s10–s14) + 5 на §3 (s15–s19) + 5 на §4 (s20–s24) + 1 на §4.5 (s23a интегрирован в §4 sequence) + 6 на §5 (s25–s30) + 3 на §6 (s31–s33; сжато с 4 до 3 для §4.5) + 2 на §7 (s35–s36) + s39 (closing hero). Media plan ≥17 слайдов (≥50%) — детали Section 7 (plan-v2-part2.md §7).

---

## Section 4 — Per-section detail

### §0 — Cover + Keystone + Аббревиатуры + Roadmap (5 мин)

**Assertion:** Лекция строится вокруг шкалы автономии AI A0–A3; цифровой двойник — мост между ступенями.

**Evidence:** keystone-слайд с 4 ступенями + disclaimer ISA-95 + disclaimer A3-asymmetry; cover hero foreshadowing Hannover Messe physical-AI scene.

**LO mapping:** LO5 (operational framing).

**Media plan:**
- s01 (cover hero): Hannover Messe 2026 кадр — оператор + Omniverse overlay. Tier 1: blogs.nvidia.com OR press.siemens.com Digital Twin Composer / Omniverse CES 2026. Tier 2: Wikimedia. Tier 3: Reuters press photos.
- s02 (keystone): диаграмма шкалы — 4 ступени, 1 пример на ступень, подпись «Цифровой двойник — мост между A1 и A2». **Vector diagram** (НЕ 5-col table). Первая строка: ISA-95 disambiguation. Disclaimer A3-asymmetry.
- s03 (аббревиатуры): таблица OT / IT / OPC UA / MES / SCADA / RL+MPC c RU расшифровкой.
- s04 (roadmap): мини-карта 8 разделов с временем.

**Failure-bucket:** нет (служебный раздел).

**Transition к §1:** «Прежде чем подниматься по шкале, разберёмся с мостом — что такое цифровой двойник в 2026 году, и почему 75% попыток его построить проваливаются».

### §1 — Что такое цифровой двойник в 2026 (10 мин)

**Assertion:** Цифровой двойник — это **двусторонняя петля** (physical ↔ digital с возможностью симулировать управляющее действие назад), а не CAD-картинка или dashboard. 75% проектов проваливаются именно на слое данных.

**Evidence:**
- **Kritzinger 2018 taxonomy** (mini-table на s06):

| Тип | Live data flow | Управляющее действие назад? | Пример |
|---|---|---|---|
| Digital Model | – | – | CAD-чертёж |
| Digital Shadow | physical → digital | – | Monitoring dashboard |
| **Digital Twin** | physical ↔ digital | ✓ (simulate + apply) | Siemens Composer 2026 |

  Источник: Kritzinger W. et al. (2018). «Digital Twin in manufacturing: A categorical literature review and classification». IFAC-PapersOnLine 51(11):1016–1022.

- **ГОСТ Р 57700.37-2021 «Цифровые двойники изделий. Общие положения»** (carry-forward от lec-11 §5.3) — формальная регуляторная база РФ. Chapter §1 цитирует определение ГОСТа для исключения term drift с международной taxonomy.
- Архитектура 4 слоёв (диаграмма s06 правая половина): physical asset → IIoT sensors (OPC UA + MQTT) → digital model (физика + ML) → AI consumers.
- Рынок: 36,19 миллиарда долларов 2025 → 180,28 миллиарда 2030 [PatSnap / StartUs 2026]. Adoption: аэрокосмос / авто / электроника / энергоутилиты > 70% pilot/deploying; пищевая / фарма / химия 30–50%; текстиль < 30%.
- **Failure:** Southeast Asian Port digital twin — 12 миллионов долларов, 18 месяцев, списан в 2024 году. Причина: фрагментированные данные, низкое качество, отсутствие clear use case [context-clue.com 2026].
- **Failure pattern:** «up to 75% of digital twin projects fail to deliver ROI due to weak data layers». Корневые причины: фрагментированные источники, чрезмерный акцент на 3D-визуализации, latency конвейера, scaling challenges.
- **Сектор-выкладка:** только 11% проектов в нефтегазе дают ожидаемый эффект; только 14% пользователей говорят соответствие ожиданиям [EY / DataMintelligence 2026].
- **Knowledge unlock 2026:** Siemens Digital Twin Composer (CES 2026 → Xcelerator Marketplace mid-2026) — публичный пример рабочего инструмента.

**LO mapping:** LO2 (критическая оценка вендорских заявлений), LO5 (архитектурные слои).

**Media plan:**
- s05 (что НЕ цифровой двойник): **vector diagram «4 layers required»** — слои physical / sensors / model / AI-consumers с пометкой «без любого из них = не twin» (методически чище, чем composite split-screen).
- s06 (Kritzinger 3-уровневая mini-table + 4-слойная архитектура справа): vector composite.
- s07 (hero для раздела): **Siemens Digital Twin Composer screenshot UI с time scrubbing**. **6-tier acquisition:** Tier 1 press.siemens.com release CES 2026; Tier 2 news.siemens.com Composer announcement; Tier 3 Wikimedia Commons (Siemens corporate images); Tier 4 YouTube CES 2026 keynote thumb; Tier 5 Wayback Machine snapshot; Tier 6 Google Images filtered «Siemens Digital Twin Composer» + «press release».
- s08 (рынок): bar/line chart 36→180 миллиардов + AI-mfg 155, OPC UA-AI 17,15. QuickChart.
- s09 (Southeast Asian Port failure): case-card. Image: stock port photo + overlay «12 млн $ / 18 мес / списано» (Tier 6: Google Images, attribution Reuters / Wayback).

**Failure-bucket контент (4 мин):**
- 75% проектов не доходят до ROI из-за слабого слоя данных (структурное ограничение).
- Southeast Asian Port — конкретный кейс, документированный.
- 11% / 14% expectation gap (разрыв ожиданий) — индустриальная норма.
- **Альтернатива (data layer audit / аудит слоя данных):** 5-вопросный checklist:
  1. Есть ли доступ к историческим данным ≥1 год?
  2. Sampling rate ≥10× выше требуемого control band?
  3. Labeling provenance (происхождение разметки) документирована?
  4. Sensor drift калиброван и логируется?
  5. Назначен ли governance owner для данных?

Если ≥1 ответ «нет» — пилот = деньги на ветер (Southeast Asian Port lesson).

**Transition к §2:** «Допустим, у нас есть рабочий twin. Что AI делает на первой ступени — наблюдает».

### §2 — A0 Наблюдать: vision QC + predictive maintenance (10 мин)

**Assertion:** На A0 AI безопасен и хорошо изучен — но даже здесь есть критерии «не применяй»: каскад срабатываний ложных позитивов в vision и редкие отказы в прогностическом обслуживании.

**Evidence:**
- Vision QC: точность 99%+ при FP 0,1–2% (Indus Vision / Jidoka 2026). Legacy machine vision FP ~50%. **Cost-of-FP пример:** 1% FP × 10 000 деталей за смену = 100 годных отвергнуто [Overview.ai 2026].
- Predictive maintenance (прогностическое обслуживание): средний ROI 10:1 за 2 года, снижение затрат на обслуживание 25–40%, незапланированных простоев 30–50%, продление срока службы 20–40% [Deloitte 2026]. **Программа PdM**: инвестиции $200K–$600K → ежегодная экономия $1.2M–$3.5M → окупаемость 18–36 месяцев [oxmaint 2026]. Cement plant: 57× ROI за 6 месяцев (software-only monitoring) [oxmaint]. Chemical plant: 2 млн долларов годовой экономии. *(automotive ROI dropped per Q5 — duplicate metric class)*.

**LO mapping:** LO2 (критическая оценка), LO7 (применимость).

**Media plan:**
- s10 (hero раздела): vision-inspection кадр на реальной линии — заводская камера + AI overlay (defect detection bounding boxes). Tier 1: Indus Vision blog. Tier 2: Wikimedia (Industry 4.0). Tier 3: Bosch / Siemens press images.
- s11 (cost-of-FP визуализация): диаграмма «1% FP × 10K = 100 годных отвергнуто за смену». QuickChart waterfall.
- s12 (PdM hero): cement plant или chemical plant — реальный кадр с edge sensors. Tier 1: oxmaint case-study illustration. Tier 2: Wikimedia. Tier 3: Schneider / Honeywell press kit.
- s13 (ROI breakdown): таблица Deloitte 10:1 / 25-40% / 30-50% / 20-40% + PdM програма $200K–$600K → $1.2M–$3.5M / 18-36 мес.
- s14 (когда vision/PdM НЕ применим): 2-колоночный фрейм. Слева: «Tight tolerances ± 0,001 мм → metrology + GD&T (Geometric Dimensioning and Tolerancing) + SPC (Statistical Process Control), не AI». Справа: «Редкий отказ MTBF (Mean Time Between Failures, средняя наработка на отказ) > 1 года → physics-based + reliability theory, не ML». Vector.

**Failure-bucket контент (4 мин):**
- **Каскад срабатываний (cascade) в vision:** 1% FP × 10K = 100 годных отвергнуто → ручная переборка + sort cost + throughput loss + operator override (потеря доверия). Структурный риск, не «иногда».
- **Альтернатива vision:** process redesign (стабилизация процесса) ПЕРЕД vision AI; если процесс нестабилен, FP cascade > savings.
- **Альтернатива vision для tight tolerances:** metrology + GD&T + SPC.
- **Альтернатива PdM для редких событий:** physics-based simulation + RCM (Reliability-Centered Maintenance — методология Nowlan-Heap 1978, разработанная для авиации; назначает регламент по физике износа, а не по календарю). ML на исторических данных не работает, когда выборка отказов < 30.

**Transition к §3:** «A0 — пассивное наблюдение, AI сигнализирует, человек решает; безопасная ступень со строгими критериями. Когда AI не только сигнализирует, но предлагает действие — мы переходим на A1».

### §3 — A1 Советовать: MES advisory + alarm prediction + PLC Copilot (10 мин)

**Assertion:** A1 — это AI как советчик оператору. Mature применения работают (MES-advisory, alarm prediction), но generic LLM на низком уровне (PLC) — провал; покупай purpose-built tools с инженером в loop.

**Evidence:**
- MES-advisory: рекомендации по последовательности операций, energy-aware scheduling [Devox / iFactoryApp 2026].
- Alarm prediction: ML на исторических SCADA-логах предсказывает каскадные тревоги за 5–15 минут до возникновения.
- **Knowledge unlock 2026:** PLC Copilot / PLCAutoPilot / Wipro PARI — purpose-built инструменты для ladder logic и structured text (IEC 61131-3). 3-4 дня → 10 минут, 85% точности — **только с human engineer в loop**.
- **Failure (concrete):** Generic ChatGPT на PLC выдаёт «несуществующие инструкции, нелегальные адреса памяти, игнорирует scan-based execution» (PLC выполняет программу циклами фиксированной длительности 1–10 мс, не event-driven). **Конкретный пример:** ChatGPT предлагает `MOV %M99999` в Siemens S7-1500 — illegal, потому что M-область (флаги памяти) у S7-1500 ограничена до M65535; LLM «галлюцинирует» допустимые адреса. Cross-ref lec-11 §1.2 (GE Predix / Watson Health / Foxconn — foundation models дополняют, не замещают).

**LO mapping:** LO2 (отличие маркетинга от инженерной реальности), LO7 (применимость с критериями).

**Media plan:**
- s15 (MES-advisory): screenshot реального MES-интерфейса (Siemens Opcenter или Rockwell FactoryTalk) с AI-рекомендацией. Tier 1: Siemens / Rockwell product pages. Tier 2: Wikimedia. Tier 3: vendor press kit.
- s16 (hero раздела — PLC Copilot vs ChatGPT): split-screen: слева — ChatGPT-PLC failure example `MOV %M99999`; справа — PLC Copilot purpose-built output. Tier 1: plccopilot.com blog. Tier 3: Foxmere journal article.
- s17 (alarm prediction): time-series chart реальных SCADA-логов + AI-prediction window.
- s18 (engineer-in-loop architecture): vector diagram (AI proposes → engineer reviews → simulation → safety check → PLC deploy).
- s19 (когда LLM НЕ применим к PLC): критерии failure case.

**Failure-bucket контент (4 мин):**
- **Generic LLM disaster на PLC** — структурное ограничение. LLM не знает scan-based execution, не знает legal memory addresses, не понимает determinism.
- **Альтернатива:** purpose-built tools (PLC Copilot / PLCAutoPilot / Wipro PARI) с engineer-in-loop. 85% точности → 15% ошибок, которые ловит инженер.
- **Альтернатива для structured text:** инженер + симуляция + IEC 61131-3 стандарты.
- **Критерий:** «AI-генерация PLC кода применима только если (а) есть симулятор для валидации, (б) есть safety-протоколы перед deployment, (в) есть инженер с правом veto».

**Transition к §4:** «A1 — AI советует, оператор решает; граница с A2 — когда решение принимается *в петле* без явного согласия оператора».

### §4 — A2 Замыкать петлю: closed-loop + RL process control (10 мин)

**Assertion:** A2 — AI меняет параметры процесса в безопасной зоне действия без согласия оператора на каждое изменение. В 2026 году единичные production-кейсы (Yokogawa FKDPP в JSR 35 дней — первый); основная масса A2 — energy-optimization и micro-adjust некритических параметров. **Ключевая грань lec-12 (не lec-11):** twin как safe sandbox для RL обучения ДО переноса на железо.

**Evidence:**
- **Knowledge unlock — Yokogawa FKDPP (Factorial Kernel Dynamic Policy Programming, NAIST 2018, off-policy RL с факториальной ядровой декомпозицией; премия премьер-министра Японии 2023):** реальный chemical plant JSR, 35 дней непрерывной работы под RL-контролем в 2022 — первый production-grade случай.
- **Lec-12 differentiator (vs lec-11 §3.2):** lec-11 разобрала FKDPP как **алгоритмический breakthrough**; lec-12 разбирает **архитектурный механизм** — как digital twin (NVIDIA Omniverse / Siemens Composer) служит safe sandbox для RL обучения ДО переноса на JSR-style hardware. Якорь: «без twin — слепая вера; FKDPP получился потому, что Yokogawa имела внутреннюю симуляцию колонны как twin».
- Hazardous factors: высокие температуры, давление, флам/explosive вещества → «потеря контроля = угроза персоналу и оборудованию».
- **Sim-to-real gap (разрыв «симуляция → реальность»):** «simulation cheaper / faster но missing important info from real life» [MDPI Processes 2025]. **Конкретный пример:** симуляция не моделировала тепловые потери в окружающую среду из-за плохой изоляции колонны; RL-агент в симуляции научился держать setpoint при T=300°C; в реальности при T=315°C из-за surface fouling (отложений на стенках) RL перекомпенсировал → excursion на 10% от штатного режима.
- Closed-loop примеры 2026: energy-optimization (HVAC, освещение), micro-adjust расхода реагентов в некритических зонах, robotic cell tuning под изменчивые партии.

**LO mapping:** LO2, LO5 (архитектурная сложность A2), LO7.

**Media plan:**
- s20 (hero раздела — Yokogawa FKDPP в JSR): иллюстрация chemical plant + RL agent diagram. Tier 1: Yokogawa press release. Tier 2: ACS publication illustration. Tier 3: JSR newsroom.
- s21 (safety envelope / безопасная зона действия diagram): vector — RL agent action space + hardwired interlock barrier.
- s22 (digital twin как RL playground / песочница для RL): screenshot Siemens Digital Twin Composer / NVIDIA Omniverse — RL обучается в симуляции до deployment. Tier 1: press.siemens.com / blogs.nvidia.com. **Эта связь twin↔RL — central new angle vs lec-11.**
- s23 (sim-to-real gap concrete): split-screen «симуляция (T=300°C, без surface fouling) vs реальность (T=315°C, fouling drift)» — отличия, которые RL не видит.
- s24 (когда RL НЕ применим): 2-колоночный фрейм. «Safety-critical control → hardwired PLC + IEC 61508 SIL 2/3 (вероятностные категории отказоустойчивости: SIL 2 = 10⁻⁶..10⁻⁷, SIL 3 = 10⁻⁷..10⁻⁸ отказов на час)»; «Process с известной физикой → MPC, не RL».

**Failure-bucket контент (4 мин):**
- **Sim-to-real gap** — структурное ограничение RL. Symulation cheaper / faster, но missing real-life information. Concrete thermal-loss + fouling example.
- **Hazardous factors** — chemical plant, oil refinery, металлургия: RL не сертифицируется по IEC 61508 SIL 2/3. Это блокер.
- **Альтернатива для known physics:** **MPC (Model Predictive Control — модельное предиктивное управление с явной оптимизацией на горизонте; гарантии устойчивости через теорию Ляпунова).** Если физика описана уравнениями (Навье-Стокса, теплоперенос, химическая кинетика), MPC даёт доказуемые гарантии — RL нет.
- **Альтернатива для safety-critical:** hardwired PLC + **formal verification (математическое доказательство свойств кода: TLA+ / SPIN / Coq / SCADE для safety-critical)** + IEC 61508 SIL 2/3.

**Transition к §4.5:** «A2 — ступень, где twin становится критическим. Что есть на A3, и почему он остаётся единичным?»

### §4.5 — A3: единичные кейсы и почему ось обрывается на A2 для 95% производства (2 мин — NEW в v2)

**Assertion:** A3 в 2026 = единицы кейсов; основная масса производства застряла на A0–A2 не из-за «отставания», а из-за конкретных блокеров.

**Evidence:**
- **Существующие A3-кейсы:**
  - **Toyota Digit (Agility Robotics)** на сборочной линии RAV4 — 7+ единиц внутрицеховой логистики, действуют без человека в loop в безопасной зоне между станциями.
  - **BMW Plant Leipzig humanoid pilot** — первый европейский гуманоид в производстве, 2026.
- **Почему остальные не A3 (3 блокера):**
  1. **Regulatory:** для safety-critical действий требуется сертификация (IEC 61508 SIL 2/3, ATEX Zone 0). RL/гуманоиды не сертифицируются.
  2. **Cost:** A3-капитал (гуманоид Agility Robotics — несколько сотен тысяч долларов за единицу) окупается только в нишах с высокой стоимостью труда и предсказуемой задачей.
  3. **Complexity:** A3 требует full-stack стека (twin + edge AI + safety envelope + fleet management) — большинство заводов не имеют ни одного из этих компонентов production-grade.
- **Pattern:** A3-кейсы 2026 — *логистические* (Toyota Digit), *не управляющие* (никто не запустил RL автономно на химической колонне). Это **именно тот разрыв**, который шкала визуализирует.

**LO mapping:** LO5 (operational context), LO7 (применимость).

**Media plan:**
- s23a (новый слайд встроен в §4 sequence): split-card. Левая половина: Toyota Digit фото (Tier 1 agilityrobotics.com). Правая половина: 3 блокера как текстовая карта.

**Failure-bucket контент (1 мин):** 3 блокера — это структурные причины, не «пока не успели». Студент уносит: «когда вендор обещает A3 в недетерминированной среде — задайте 5 вопросов из §5».

**Transition к §5:** «Мы прошли все ступени шкалы. Теперь — раздел, где AI просто не нужен или не работает».

### §5 — Где AI НЕ применим: провалы и альтернативы (15 мин — densest failure-bucket)

**Assertion:** Существует ≥10 структурных критериев, при которых AI в производстве не нужен или хуже альтернативы. Инженер 3 курса должен уметь их применить.

**Intro hero (Q2 decision): Southeast Asian Port 2024** — не Tesla 2018. Tesla 2018 = single line cross-reference: «канонический case over-automation разобран в lec-11 §2.4; здесь — fresh failure 2024, direct relevance к keystone twin». Southeast Asian Port — главный intro-кейс §5, потому что:
- $12 миллионов / 18 месяцев / abandoned 2024 — fresh, не дублирует lec-11.
- **Direct relevance** к keystone: «3D-визуализация без data pipeline = музей, не twin» — это failure-mode именно той оси, которую вводит lec-12.
- Урок: data-layer audit обязателен ПЕРЕД любым AI-проектом.

**Evidence — десять критериев + альтернативы:**

1. **Safety-critical control (E-stop, interlock, emergency shutdown).** **Альтернатива:** hardwired PLC + formal verification + IEC 61508 SIL 2/3. *RL-policy не сертифицируется.*
2. **Процесс с известной физикой (T-controller печи, расход реагентов).** **Альтернатива:** MPC (модельное предиктивное управление, см. §4 определение) — доказуемые гарантии устойчивости.
3. **Rare-event prediction (поломка раз в год, выборка < 30).** **Альтернатива:** physics-based simulation + RCM (методология Nowlan-Heap 1978, см. §2).
4. **Defect detection нестабильного процесса.** Каскад срабатываний ложных позитивов > savings. **Альтернатива:** process redesign перед vision AI.
5. **Quality control с tight tolerances ± 0,001 мм.** **Альтернатива:** metrology + GD&T + SPC.
6. **Generic PLC code generation.** **Альтернатива:** engineer + симуляция + IEC 61131-3 OR purpose-built tool с engineer-in-loop (см. §3).
7. **Регулируемая среда без объяснимости (FDA 21 CFR Part 11, GAMP 5 — Good Automated Manufacturing Practice v5, основной gold-standard для валидации программных систем в фарма-производстве).** Чёрный ящик ML не работает. **Альтернатива:** **explainable AI — SHAP (SHapley Additive exPlanations) / LIME (Local Interpretable Model-agnostic Explanations) — методы post-hoc оценки вклада признаков** + гибрид с правилами + human-in-loop с audit trail.
8. **ATEX Zone 0 (взрывоопасная среда категории 0 — постоянное присутствие взрывоопасной концентрации; vs Zone 1 — периодическое; Zone 2 — редкое; IEC 60079).** Несертифицированное оборудование AI-inference физически запрещено. **Альтернатива:** ATEX-сертифицированные датчики + удалённая обработка с допустимой задержкой.
9. **Малая стоимость ошибки человека vs стоимость AI-системы.** Формула: ROI = (saving per error × error rate × operations per year) − (AI system cost + maintenance + retraining). Если оператор уже справляется на 99%, экономика AI отрицательная. **Альтернатива:** не внедрять; направить бюджет на обучение оператора.
10. **Отсутствие clear use case (data layer audit fails).** **Альтернатива:** data-layer audit (5-вопросный checklist из §1) + remediation ДО любого AI-проекта.

**Бонусный критерий — Gartner 40%:** к 2027 году 40% агентных AI-проектов будут отменены. Если вы видите слайд «agentic AI for manufacturing» — задайте вендору пять вопросов (формат lec-11 §5.2).

**Worked example (Q6 decision: фарма + дозировка + FDA):**

Сценарий: фармпроизводство, AI-система рекомендует дозировку активного компонента в финальной формуляции таблеток.
- **AI способен:** учиться на исторических партиях, предсказывать оптимальную дозировку «±0,5% от номинала» с 90% accuracy на тестовом наборе.
- **FDA требует:** ±0,1% precision для batch release decision (FDA 21 CFR Part 11 + GAMP 5).
- **Gap:** AI accuracy (±0,5%) < required tolerance (±0,1%) — несовместимо.
- **Verdict:** AI **не подходит для финального release decision**. Альтернатива: AI как advisory tool на этапе process design (где accuracy ±0,5% полезна) + **human-in-loop QA + statistical batch sampling** для release (validated according to USP / GMP).
- **Cross-reference:** lec-07 prerequisite (FDA 21 CFR Part 11) — этот кейс — concrete instantiation того, что lec-07 ввела как принцип.

**LO mapping:** LO2, LO7, LO8 (полностью).

**Media plan:**
- s25 (intro к разделу — Southeast Asian Port hero): кадр контейнерного порта + overlay «12 млн $ / 18 мес / abandoned 2024 / weak data layer». Tier 1: Reuters / Bloomberg port photos. Tier 6: Google Images filtered. Tesla 2018 = single text mention с cross-ref «канонический case в lec-11 §2.4».
- s26 (hero — 10 критериев таблица): structured 10×2 grid (критерий / альтернатива).
- s27 (hero — матрица альтернатив): 6 не-AI инструментов с применимостью.
- s28 (worked example): фарма + дозировка + FDA flow-diagram (AI рекомендация → FDA precision gap → human-in-loop QA + batch sampling).
- s29 (hero — Gartner 40%): chart-card 40% agentic AI cancelled by 2027 + 30% GenAI abandoned after PoC by 2025.
- s30 (5 вопросов вендору): list-card.

**5 вопросов вендору (carry-forward lec-11 §5.2 pattern):**
1. Покажи 3 documented failures за последние 24 месяца в той же индустрии.
2. Что именно делает твоя система на A0/A1/A2 — где она в нашей шкале?
3. Какой data-layer audit ты провёл перед пилотом?
4. Какова твоя альтернатива, если pilot fails — refund / pivot / continued integration?
5. Можешь показать customer reference в нашем sub-сегменте (process / discrete / regulated)?

**Failure-bucket контент (15 мин полностью in-bucket):**
- Southeast Asian Port hero intro + Tesla 2018 cross-ref (3 мин).
- 10 критериев + 10 альтернатив (7 мин).
- Worked example фарма+FDA (3 мин).
- 5 вопросов вендору (2 мин).

**Transition к §6:** «Если у вас есть applicable use case, какая архитектура нужна для его реализации в 2026 году».

### §6 — OT/IT архитектура 2026 (6 мин — сжато с 8 в v1 для §4.5 budget)

**Assertion:** Современная производственная AI-архитектура — это семислойный стек (sensor → network → edge AI → MES/SCADA → digital twin → cloud → human), где OPC UA + TSN + edge inference <10 мс — операционные условия для A2.

**Evidence:**
- **7 слоёв (explicit list — закрывает reader-text §6 gap):**
  1. **Sensor layer:** IIoT (OPC UA + MQTT).
  2. **Network layer:** **TSN (Time-Sensitive Networking, IEEE 802.1 — детерминированная доставка Ethernet-пакетов с гарантированной задержкой; ключевое отличие от стандартного Ethernet, где задержка случайна)**.
  3. **Edge AI layer:** GPU micro-servers на machine cabinets, <10 мс inference (NVIDIA Jetson, Dell edge, Schneider Modicon edge).
  4. **MES/SCADA layer:** AI как advisory → closed loop.
  5. **Digital twin layer:** Siemens Xcelerator + NVIDIA Omniverse / PTC ThingWorx / AVEVA / Bentley.
  6. **Cloud layer:** model training, fleet analytics.
  7. **Human-in-the-loop layer:** safety-critical всегда gated.
- Vendors integrated без PLC reprogramming: Siemens S7, Allen-Bradley, Rockwell, Schneider.
- **Lighthouse Network (программа World Economic Forum + McKinsey, отбирающая заводы-образцы с full AI-transformation):** 220+ заводов в 35 странах, 23 новых в 2026; 90% новых внедрений включают AI; перевес Lighthouse-сайтов +16% по EBIT vs peers [WEF Jan 2026 / McKinsey].
- **Failure для контекста:** 11% O&G expected benefits; 14% expectation match (разрыв ожиданий); Gartner 40% agentic cancellation к 2027.

**LO mapping:** LO5 (архитектурные слои).

**Media plan (3 слайда — сжато с 4):**
- s31 (hero — 7-layer architecture): vector diagram с подписями.
- s32 (OPC UA + MQTT + TSN dataflow): vector sensor → broker → edge AI.
- s33 (hero — Lighthouse Network map): real screenshot WEF Lighthouse 220+ sites world map. Tier 1: weforum.org press release Jan 2026.

*(s34 edge AI cabinet photo из v1 — dropped per Q3/Q5 для §4.5 budget.)*

**Failure-bucket контент (1 мин):** 11% / 14% expectation gap преамбула: «архитектура не гарантирует ROI, если data layer слабый».

**Transition к §7:** «Как это устроено в российском контексте — и где работа инженера».

### §7 — Российский контекст (ГОСТ + 3 кейса) + карьерный мост (5 мин)

**Assertion:** В России цифровые двойники и AI в производстве оформлены ГОСТ Р 57700.37-2021; крупные кейсы — КАМАЗ + Росатом + Норникель; рынок труда требует инженеров, понимающих интеграцию OT/IT и регуляторику (КИИ).

**Evidence:**
- **ГОСТ Р 57700.37-2021 «Цифровые двойники изделий. Общие положения»** — формальная регуляторная база РФ (carry-forward от lec-11 §5.3). Chapter §1 цитирует определение ГОСТа для term consistency с международной taxonomy. Mandatory mention для лекции про цифровые двойники.
- **КАМАЗ** — пионер цифровых двойников РФ: конвейер + R&D (КАМА-1 e-vehicle), 2020+.
- **Росатом** — стратегия «технологический суверенитет»: T-FLEX PLM, АтомМайнд (2024+).
- **Норникель flotation + измельчение AI** (carry-forward lec-11 §3.5) — российский process-control case A2-type (синергия с Yokogawa FKDPP §4 — оба process-control, но Норникель — отечественный пример).
- ЦИПР 2026 / ИИПРОМ 2026 — крупнейшие форумы по промышленной цифровизации.
- Эффект: simulation reduces downtime 10–30%, сокращает срок ввода новой линии [РБК Тренды / Ведомости / TAdviser / ru-bezh.ru 2025-2026].

**Карьерный мост — расширенный (закрывает reader §7 P1 gap):**

| Роль | Что делает день за днём | Ключевые навыки | Где учиться |
|---|---|---|---|
| **AI/ML engineer (industrial)** | Дизайнит и тренирует модели (vision QC, PdM, alarm prediction) на исторических данных завода; интегрирует в edge runtime; мониторит drift; общается с цеховыми инженерами | Python + PyTorch/TensorFlow, MLOps, OPC UA basics, статистика, время-ряды; знание физики процесса | Профильные технические магистратуры по AI в промышленности |
| **Digital twin engineer** | Строит и поддерживает twin для конкретной линии или цеха: подключает датчики через OPC UA, строит модель оборудования (физика + ML), валидирует точность, разворачивает на edge | Siemens Composer / NVIDIA Omniverse / PTC ThingWorx; CAD; численное моделирование; OPC UA; data pipelines | Магистратуры по цифровому моделированию + Coursera/edX курсы NVIDIA Omniverse, Siemens Industrial AI |
| **MES integration specialist** | Внедряет advisory-AI в существующий MES (Opcenter, FactoryTalk, SAP MII); конфигурирует workflow «AI рекомендация → оператор апрув → исполнение»; пишет интеграционные сценарии | SQL, REST/OPC UA, конкретный MES-стек вендора, бизнес-процессы цеха | Vendor-сертификации (Siemens / Rockwell / SAP) + on-the-job |
| **Edge AI engineer** | Деплоит inference на edge-устройства (NVIDIA Jetson, Modicon edge), оптимизирует latency и throughput, разрабатывает fail-safe handover к человеку | C++/Rust, embedded Linux, ONNX/TensorRT, real-time scheduling, безопасность сети (КИИ) | Embedded + ML — стык; cертификации NVIDIA Jetson + cybersecurity (для КИИ-объектов) |

**Регуляторное знание (КИИ — Критическая Информационная Инфраструктура):** Указ Президента РФ № 250 о КИИ устанавливает требования к защите промышленных систем категории «значимые объекты КИИ». Инженер AI на КИИ-объекте отвечает за: (1) сертифицированную обработку данных, (2) фиксацию audit trail для регулятора, (3) отсутствие неконтролируемого исходящего трафика моделей. Это **дополнительный карьерный угол** для инженеров AI в РФ.

**LO mapping:** LO5 (operational context), LO7 (регуляторика + career).

**Media plan:**
- s35 (российский кейс): КАМАЗ или Норникель — реальный кадр + digital twin overlay. Tier 1: kamaz.ru newsroom OR nornickel.ru. Tier 2: Wikimedia. Tier 3: РБК / TAdviser press photos.
- s36 (карьерный мост): icon-card 4 ролей с краткими описаниями (без named institutions).

**Failure-bucket контент:** нет (карьерный раздел).

**Transition к §8:** «Российский контекст показывает, что шкала — глобальная. Что мы унесём и куда смотрим в Лекции 13».

### §8 — Закрытие + мост к Лекции 13 (2 мин)

**Assertion:** Шкала автономии A0–A3 + цифровой двойник как мост — операционная рамка для инженерных решений 2026. Лекция 13 расширит scope от одного цеха к цепочке поставок и транспорту.

**Evidence:**
- Resume: A0 (vision/PdM), A1 (advisory/Copilot), A2 (closed-loop/RL + twin sandbox), A3 (humanoid логистика — единично).
- Мост к Лекции 13: Toyota Digit на сборочной линии RAV4 — внутрицеховая логистика — первая ступень multi-site supply chain. Лекция 13 («AI в логистике, цепях поставок и транспорте» — locked phrasing) расширит до cross-warehouse, cross-site, multi-modal transport.

**LO mapping:** none (закрытие).

**Media plan:**
- s38 (resume): repeat keystone-слайда + «что мы знаем теперь».
- s39 (closing hero): Toyota Digit на RAV4 line. Tier 1: Agility Robotics press kit. Tier 2: Wikimedia. Tier 3: Toyota newsroom. Tier 4: Reuters YouTube thumb.

**Bridge text на s39 (locked):** «Лекция 13 — AI в логистике, цепях поставок и транспорте. Digit на внутрицеховой логистике — первая ступень supply chain».

---

## Section 5 — Failure / judgment bucket inventory

### Документированные провалы (≥10 кейсов)

| # | Кейс | Где в лекции | Lesson |
|---|---|---|---|
| 1 | **Southeast Asian Port digital twin** ($12 миллионов, 18 месяцев списано 2024) | §1 (s09) + §5 intro hero (s25) | 3D-визуализация без data pipeline = музей, не twin (lec-12 specific, fresh) |
| 2 | **Tesla Fremont 2018** (single line + cross-ref) | §5 text mention (NOT hero) | Cross-reference lec-11 §2.4 canonical case; не дублируем narrative |
| 3 | **Oil & gas digital twin 11% expected / 14% expectation match** | §1 (s07-s09), §6 (s33) | Разрыв ожиданий — индустриальная норма |
| 4 | **75% digital twin data-layer failure** | §1 (s07-s09) | Без аудита слоя данных пилот = деньги на ветер |
| 5 | **Gartner 40% agentic AI cancellation 2027** + 30% GenAI PoC abandonment 2025 | §5 (s29), §6 (s33) | Hype-curve индустрии-wide |
| 6 | **ChatGPT для PLC — MOV %M99999 illegal address** (concrete) | §3 (s16, s19) | Generic LLM не знает scan-based execution; альт.: purpose-built + engineer-in-loop |
| 7 | **Vision FP cascade** (1% × 10K = 100 годных отвергнуто) | §2 (s11, s14) | Структурный риск vision; альт.: process redesign + metrology |
| 8 | **RL sim-to-real gap concrete** (T=300°C sim vs T=315°C real + surface fouling, 10% excursion) | §4 (s23, s24) | Симуляция не покрывает rare events; альт.: MPC для known physics |
| 9 | **RL safety risk в chemical plant** (Yokogawa context — twin-as-sandbox lec-12 grain) | §4 (s20, s24) | RL не сертифицируется по IEC 61508; twin обязателен ДО deploy |
| 10 | **Tesla Optimus 2021→2024 hardware-soft AI gap** + A3 blockers (regulatory + cost + complexity) | §4.5 (s23a) | Гуманоид 2026 — результат 15 лет работы над twin + edge AI |
| 11 | **Worked example: фарма AI ±0,5% vs FDA ±0,1% precision** | §5 (s28) | AI accuracy < required tolerance → не подходит для finalrelease; альт.: HITL QA + batch sampling |

### Десять «не применяй AI / альтернатива лучше» правил

| # | Критерий | Альтернатива (с 1-фраза-якорь) | Обоснование |
|---|---|---|---|
| 1 | Safety-critical control (E-stop, interlock) | Hardwired PLC + IEC 61508 SIL 2/3 + formal verification (TLA+ / SPIN / Coq / SCADE) | RL не сертифицируется |
| 2 | Процесс с известной физикой | MPC (модельное предиктивное управление, гарантии устойчивости через теорию Ляпунова) | Доказуемые гарантии |
| 3 | Rare-event prediction (MTBF > 1 года, выборка < 30) | Physics-based simulation + RCM (методология Nowlan-Heap 1978 из авиации) | ML без статистики не работает |
| 4 | Defect detection нестабильного процесса | Process redesign перед vision AI | Каскад срабатываний > savings |
| 5 | Tight tolerances ± 0,001 мм | Metrology + GD&T + SPC | Vision не дотягивает |
| 6 | Generic PLC code generation | Purpose-built + engineer-in-loop OR engineer + симуляция + IEC 61131-3 | Generic LLM disaster |
| 7 | Регулируемая среда без объяснимости (FDA 21 CFR Part 11, GAMP 5) | Explainable AI (SHAP / LIME) + hybrid с правилами + audit trail | Чёрный ящик ML не принимается |
| 8 | ATEX Zone 0 (взрывоопасная категория 0) | ATEX-сертифицированные датчики + удалённая обработка | Физический регуляторный запрет |
| 9 | Стоимость AI > стоимость ошибки человека | Не внедрять; обучение оператора (формула ROI в §5 п.9) | Отрицательная экономика |
| 10 | Отсутствие clear use case (data-layer audit fails) | Аудит слоя данных (5-вопросный checklist §1) + remediation | Southeast Asian Port lesson |

**Бонус:** 5 вопросов вендору (s30) — см. §5.

### Strict-in bucket cumulative: 33 мин / 75 мин = 44% (target ≥30%)

**Distribution across artifacts (план для отслеживания на Phase 3/7/10):**
- **Chapter (~30 000 слов):** §1 ~3 000 в bucket + §2 ~3 000 + §3 ~3 000 + §4 ~3 000 + §4.5 ~1 000 + §5 ~7 000 + Q&A backup ~2 000 (из 12-14 questions where ≥6 — failure-related) = **~22 000 из 30 000 = 73% strict-in.** Превышает порог чётко.
- **Slides (33 слайда):** §1 1 (s09) + §2 2 (s11, s14) + §3 2 (s16, s19) + §4 2 (s23, s24) + §4.5 1 (s23a) + §5 6 (s25–s30) + §6 1 (s33) = **15 / 33 = 45%.**
- **Speech (~5 000 слов, 75 мин):** 33 мин из 75 = 44%. По словам ~2 200 из 5 000 = 44%.

Все три артефакта ≥30%, holistic.

---

## Section 6 — Hero plan для s01 + s39 + s07 (ENFORCED)

### s01 (cover hero)

**Subject:** Hannover Messe 2026 — оператор у физической линии (например, ABB или Siemens робот), на overlay — сцена NVIDIA Omniverse / Siemens Digital Twin Composer того же оборудования с time scrubbing UI.

**Why:** foreshadow keystone (мост физика↔AI). НЕ «AI заменил оператора» — это плакат Industry 4.0 из 2018.

**6-tier acquisition plan:** T1 og:image / press → blogs.nvidia.com `/ai-manufacturing-hannover-messe/` OR press.siemens.com Digital Twin Composer / Omniverse CES 2026. T2 Wikimedia категории «Hannover Messe» / «NVIDIA Omniverse» / «Industry 4.0». T3 press kit news.siemens.com / nvidianews.nvidia.com. T4 YouTube thumb Hannover Messe 2026 demo videos. T5 Wayback Machine. T6 Google Images fallback.

**Attribution label:** «Image: NVIDIA Corp. / Press release, Hannover Messe 2026».

**Size mandate:** ≥40% area.

### s07 (Siemens Digital Twin Composer — content hero §1)

**Subject:** Реальный screenshot UI Siemens Digital Twin Composer (CES 2026 announcement) с visible time scrubbing controls.

**Why:** knowledge unlock 2026; концретный «вот так выглядит рабочий twin», в отличие от презентационной 3D-картинки.

**6-tier acquisition plan (расширено в v2):**
- T1: press.siemens.com release «Siemens unveils Digital Twin Composer at CES 2026» (`press.siemens.com/global/en/pressrelease/siemens-unveils-technologies-accelerate-industrial-ai-revolution-ces-2026`)
- T2: news.siemens.com Composer announcement (`news.siemens.com/en-us/digital-twin-composer-ces-2026/`)
- T3: Wikimedia Commons (Siemens corporate images category)
- T4: YouTube CES 2026 keynote thumb (Siemens channel)
- T5: Wayback Machine snapshot press.siemens.com / news.siemens.com
- T6: Google Images filtered «Siemens Digital Twin Composer» + «press release»

**Attribution:** «Image: Siemens AG / Press release, CES 2026».

### s39 (closing hero)

**Subject:** Toyota Digit (Agility Robotics) на сборочной линии RAV4 — кадр в действии.

**Why:** мост к Лекции 13 (внутрицеховая логистика = первая ступень supply chain).

**6-tier acquisition plan:** T1 press kit Agility Robotics `agilityrobotics.com/news` OR Toyota newsroom. T2 Wikimedia Toyota production + Agility Robotics. T3 press Reuters / Bloomberg / Manufacturing Dive. T4 YouTube thumb Agility Robotics channel. T5 Wayback. T6 Google Images fallback.

**Attribution:** «Image: Agility Robotics / Toyota Motor Corp. — RAV4 production line, 2025-2026».

**Bridge text (locked):** «Лекция 13 — AI в логистике, цепях поставок и транспорте».

**Size mandate:** ≥40% area.

---

**Навигация:** Часть 1 (Sections 1-6) ← **вы здесь** | [Часть 2 (Sections 7-11) →](plan-v2-part2.md)

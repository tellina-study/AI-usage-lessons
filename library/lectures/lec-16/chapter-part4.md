---
part: 4
of: 4
parent: "chapter.md"
title: "Глава 16. Часть 4: Раздел 5 — Россия + cross-cutting + закрытие + Q&A backup + источники"
lecture_number: 16
length_words: ~9500
status: draft
version: v1
---

---
**Навигация:** [← Часть 1 (Введение + R0 + R1)](chapter.md) | [← Часть 2 (Раздел 2 — Q3)](chapter-part2.md) | [← Часть 3 (R3 + R4)](chapter-part3.md) | **вы здесь** (R5 + Q&A + источники)

---

## Оглавление (Часть 4)

- [§ Раздел 5. Россия + cross-cutting](#-раздел-5-россия--cross-cutting)
  - [§5.1. Россия по 4 квадрантам keystone-матрицы](#51-россия-по-4-квадрантам-keystone-матрицы)
  - [§5.2. Газпром нефть Cognitive Geo: 3-4 месяца → минуты, и Ямал 2024](#52-газпром-нефть-cognitive-geo-3-4-месяца--минуты-и-ямал-2024)
  - [§5.3. Роснефть Digital Field + остальные NOC: Татнефть, ЛУКОЙЛ, Сургутнефтегаз](#53-роснефть-digital-field--остальные-noc-татнефть-лукойл-сургутнефтегаз)
  - [§5.4. Cross-cutting риск 1: киберугрозы +935% (Colonial, Shell MOVEit)](#54-cross-cutting-риск-1-киберугрозы-935-colonial-shell-moveit)
  - [§5.5. Cross-cutting риск 2: 2020 oil crash + Deepwater Horizon исторический якорь](#55-cross-cutting-риск-2-2020-oil-crash--deepwater-horizon-исторический-якорь)
  - [§5.6. Самопроверка по Разделу 5](#56-самопроверка-по-разделу-5)
- [§ Закрытие. Синтез 4-квадрантной матрицы + мост к Лекции 17](#-закрытие-синтез-4-квадрантной-матрицы--мост-к-лекции-17)
  - [§6.1. Что мы прочитали — 4-квадрантный синтез](#61-что-мы-прочитали--4-квадрантный-синтез)
  - [§6.2. 10 documented failures и фундаментальный паттерн](#62-10-documented-failures-и-фундаментальный-паттерн)
  - [§6.3. Мост к Лекции 17 — систематизация отраслевых паттернов курса](#63-мост-к-лекции-17--систематизация-отраслевых-паттернов-курса)
- [Q&A backup (12 ожидаемых вопросов с глубокими ответами)](#qa-backup-12-ожидаемых-вопросов-с-глубокими-ответами)
- [Reading list (рекомендованная литература)](#reading-list-рекомендованная-литература)
- [References](#references)

## § Раздел 5. Россия + cross-cutting

<!-- for-slide-s34 -->

### §5.1. Россия по 4 квадрантам keystone-матрицы

[for-slide-s34]

В предыдущих разделах мы видели Россию фрагментарно: Роснефть Digital Field в §1.6 как пример Q1; упоминание Газпром нефть Cognitive Geo в Разделе 2 как контр-пример SLB Lumi в Q3. В этом разделе мы собираем картину целиком, и делаем это через **четырёх-квадрантную матрицу keystone-оси** — потому что это даёт читателю **сравнительный фрейм**: что отличает российский AI-стек от западного, в каком квадранте.

Россия в режиме санкций после марта 2022 года представляет собой **естественный эксперимент**: что происходит, когда вертикально-интегрированная нефтегазовая индустрия теряет доступ к западным AI-вендорам (SLB Lumi, AspenTech, Honeywell, ABB, Yokogawa) и должна **инсорсить** AI-стек целиком? Ответ — частично разработан внутри (Cognitive Geo, Digital Field), частично заимствован из других несанкционированных юрисдикций (партнёрство с AIQ — ADNOC + G42 joint venture в ОАЭ), частично остаётся в pilot stage.

**Russia↔keystone mini-matrix.**

| Квадрант | Российский эквивалент | Sanctions impact | Status |
|---|---|---|---|
| **Q1** mature production | Роснефть Digital Field; Газпром нефть Cognitive system Ямал | Нет западных vendors (Aspen Mtell, Honeywell UOP, ABB Genix ушли) → insourcing | Развёрнут production-grade |
| **Q3** frontier exploration | Газпром нефть Cognitive Geo (с IBM Research Brazil 2017–2022 → internal) | Нет SLB Lumi, нет ExxonMobil Discovery 6 → собственный HPC + foundation model | Развёрнут на Ямале 2024 |
| **Q2** методан-MRV | Не приоритет — нет EU regulator pressure | EU 2024/1787 не applies к российскому экспорту в нерегулируемые рынки; внутренняя регуляция мягче | Limited deployment |
| **Q4** energy transition (CCS/EGS) | Очень ограниченная публичная информация | Зарубежные partnerships заморожены; внутренние pilots отчёт по ВИНК limited | Pilots, public info ограничена [VFY-day-of] |

**Что эта таблица показывает.**

Россия **разрабатывает Q1 и Q3** полным циклом insourcing — это **необходимость**, не выбор. Q2 — **не приоритет**, поскольку primary driver EU Methane Reg к российскому экспорту в нерегулируемые рынки (Китай, Индия, СНГ) не applies в той же manner. Q4 — **остаётся pilot-фаза** с ограниченной public traceability.

**Структурное отличие от Запада.** Российский Q1 + Q3 AI-стек — **вертикально интегрирован** внутри NOC (Роснефть, Газпром нефть). На Западе аналог — **disaggregated**: операторы покупают у вендоров (SLB Lumi, Aspen Mtell) либо строят с partnership'ями (BP+Beyond Limits, IBM+Repsol — оба провалившиеся). Российский паттерн — ближе к **китайскому модели** (Sinopec, CNOOC внутренние разработки), не американскому vendor-based модели.

**Ограничения этой картины для студента.** Конкретные KPI Газпром нефти и Роснефти публикуются преимущественно в **корпоративных пресс-релизах** и тех-конференциях, и **независимая проверка** (auditable third-party validation) затруднена санкционным режимом. Это не «дезинформация», но и не **independent fact** в том же смысле, что Aramco numbers или ExxonMobil 10-K. Студент должен относиться с разумным скептицизмом — то же, что для self-reported US corporate numbers, плюс дополнительная корректировка на ограниченный доступ к raw data.

### §5.2. Газпром нефть Cognitive Geo: 3-4 месяца → минуты, и Ямал 2024

[for-slide-s35]

**Газпром нефть Cognitive Geologist** — flagship российский Q3 AI-проект. Создан в партнёрстве с **IBM Research Brazil** (Сан-Паулу) в период 2017–2022 годов; **после ухода IBM из России в 2022 году — перешёл в режим internal development**.

**Что система делает.**

- Применение ML + probabilistic reasoning для **exploration workflow** — анализ геофизических данных, корреляция через скважины, оценка вероятности продуктивности.
- Цикл geology work для определённых categories tasks **сокращён с 3–4 месяцев до minutes** [36]. Это касается специфических tasks (correlation между skvazhin, screening cgeo-параметров), не всего exploration cycle.
- **Cognitive system for oil prospecting**, развёрнутая на **Ямале в 2024 году** — система помогла идентифицировать новое нефтяное поле, **first oil из which получена в 2024 году**.

**Корпоративные цели и метрики.**

- **Cut twofold** время до first oil на новых проектах [37].
- **+40% projects acceleration к 2030 году** относительно базы 2020–2023.
- Партнёрство с **AIQ (ADNOC + G42 JV, валюация $1,4B+ после Presight 51% acquisition в мае 2024 года)** — commercialization 2023–2024 в нерегулируемых рынках [38].

**Что эта траектория показывает.**

Газпром нефть — **flagship российский O&G AI-разработчик**. В отличие от Aramco, которая публикует $1,8B realized 2024 (с suspicious methodology, см. §2.2), Газпром нефть публикует **qualitative metrics** («3–4 месяца → минуты») без явного dollar baseline. Это типичный паттерн для российских компаний: метрики time-savings без квантифицированного ROI. Студент должен уметь читать оба формата — quantified ROI (с потенциальной methodology weakness) и qualitative time-savings (с ограниченной auditability).

**Параллель с BP+Beyond Limits и IBM+Repsol.** Cognitive Geo начался в той же эпохе (2017) и с похожей концепцией («cognitive AI для exploration»), что и BP+Beyond Limits и IBM+Repsol. Но Cognitive Geo **выжил и развился**, в то время как два западных партнёрства провалились. Почему?

1. **Internal continuation после vendor exit.** Когда IBM ушёл в 2022, Газпром нефть **продолжила** разработку внутри, а не сдалась. У BP при vendor pivot Beyond Limits не было такой опции (BP не разрабатывал AI внутри).
2. **Anchor application focus.** Cognitive Geo с самого начала сосредоточился на **specific exploration tasks** (correlation, screening), а не на «replace geologist». Это структурно более правильная задача — augmentation, не replacement (см. §2.5 урок BP+Beyond Limits).
3. **Vertical integration внутри NOC.** Газпром нефть — это **и оператор, и разработчик**. Нет mismatch incentives между «vendor хочет продать платформу» и «operator хочет business outcomes». Это **тот же преимущество**, что Aramco METABRAIN — internal product без commercialization mismatch.

**Limit для генерализации.** Это не означает, что **insourcing AI в нефтегазе всегда побеждает**. Это означает, что **insourcing в Q3 для NOC**, у которых есть HPC capacity, exploration data, и engineering teams — workable путь. Для small operator, для middle-tier IOC — insourcing не workable, и vendor-purchase остаётся опцией (с риск-mitigation pattern из §2.6).

**AIQ partnership context.** AIQ (ADNOC + G42 JV) — крупный AI-stack в нерегулируемом Middle East / Asia market. После 51% acquisition ADNOC's Presight subsidiary в мае 2024 года, AIQ — **$1,4B+ оценка** на момент publicación. Газпром нефть partner с AIQ для **commercialization** AI-решений в нерегулируемые рынки. Это параллель к **Aramco $1,5B investment в Groq** (April 2024) — Middle East становится альтернативной AI-cloud юрисдикцией для NOC, недоступной для Запада в санкционном режиме.

**Структурный сдвиг geographic distribution AI compute.** До 2022 года основные AI compute hubs мира были два — US (NVIDIA exports + hyperscalers AWS / Azure / GCP) и China (внутренний рынок). После 2022 года US export controls на high-end NVIDIA chips к Китаю, плюс санкции на Россию, начали **фрагментировать** этот рынок:

1. **Middle East как третий hub.** Saudi Aramco $1,5B в Groq, ADNOC + G42 в AIQ ($1,4B+ valuation), Microsoft $1,5B в G42 — все весной 2024 года. Это **strategic moves** к Middle East как neutral ground для AI compute, доступный и для Запада, и для России / Китая.
2. **Россия — собственный compute stack.** Cognitive Pilot (Sberbank + Cog Tech), внутренние ML-разработки Газпром нефть и Роснефть, отказ от Roxar / Schlumberger. Это **forced insourcing** без выбора.
3. **China — внутренний compute через Huawei, домашние GPU producers.** Параллельный экосистема, не доступна для российских NOC из-за параллельных US пресснений.

Для нефтегаза это означает: **AI compute больше не commodity** в global sense. Operators выбирают compute сторон в зависимости от geopolitical alignment. Это **новый layer of considerations** в AI roadmap planning, отсутствующий до 2022 года.

**Cognitive Pilot — agricultural to O&G transferability.** Cognitive Pilot — Sberbank + Cognitive Technologies joint venture, primarily агрозона. **700+ installations в 2021 → 1700+ в 2024** [VFY-day-of]. В 2020 году Cognitive Pilot fleet harvested **720 000 тонн зерна на 160 000 гектарах** — что составляет ~0,6% общего российского zerno output (~120 Mt). Это **узкая, но measurable agricultural footprint**.

Transferability к O&G:

- **Heavy mobile equipment** (мобильные буровые установки, transport trucks) — direct applicability ML-based autonomous control. Cognitive Pilot agricultural combine стек переносится с **ограниченными изменениями** на heavy O&G equipment.
- **Remote sensing** для pipeline ROW monitoring — Cognitive Pilot CV stack применим.
- **Limit**: O&G HSE требования (ATEX rated equipment, explosion-proof certifications, IEC 61511 compliance) **существенно жёстче** агро-индустрии. Полный transfer требует ATEX-rated hardware variants и safety case engineering — что **не trivial**.

Это **good example partial transfer pattern**: технология from one domain → adjacent domain с partial reuse. Это **не "AI universal"**, и не "AI domain-specific isolated" — третий путь, где transferability frames competitive positioning.

### §5.3. Роснефть Digital Field + остальные NOC: Татнефть, ЛУКОЙЛ, Сургутнефтегаз

[for-slide-s36]

**Роснефть Digital Field** (Илишевское месторождение Башнефть) мы уже разобрали в §1.6. Quick recap key metrics:

- **+1 Mt/год** дополнительная добыча (+5,9% от Башнефть ~17 Mt/год baseline 2023).
- **~1 млрд рублей/год** экономический эффект.
- **23 программных продукта**, **10 коммерциализованных** [14].
- **+60%** удалённо управляемых объектов, **+5%** энергоэффективности, **-5%** логистики.

**Татнефть АнтиХрупкий Нижнекамск** — программа предсказательного обслуживания и оптимизации производства на нефтехимическом комплексе Нижнекамска. Public info ограничена; конкретные KPI [VFY-day-of]. Программа упоминается в press releases и industry-конференциях, но independent verification ограничена.

**ЛУКОЙЛ — пакет AI-приложений** в Волго-Уральском регионе: optimization добычи, прогнозирование тех-простоев, оптимизация маршрутов транспортировки. **Конкретные numerics — limited public** [VFY-day-of].

**Сургутнефтегаз** — традиционно closed company с минимальной publicity. AI deployments — упоминаются в industry интервью, но конкретики мало [VFY-day-of].

**Cognitive Pilot (Sberbank + Cognitive Technologies JV).** Primarily — agricultural combine automation (см. Лекцию 10 как reference). **700+ installations в 2021 → 1700+ в 2024** [VFY-day-of] [39]. Технология **transferable** на heavy O&G equipment (мобильные буровые, transport equipment), но конкретные O&G deployments — limited public. **Cognitive Pilot 2020 — 720 000 тонн зерна, 160 000 гектаров** — это базовая контекстуализация: Russia agri output ~120 Mt grain 2020 → AI fleet = 0,6% volume; transfer к нефтегазовому масштабу — non-trivial.

**Структурный паттерн российского NOC AI 2024–2026.**

1. **Insourcing default.** После 2022 vendor exit Roxar, Schlumberger E&P solutions, AspenTech — российские NOC **разрабатывают сами**.
2. **Commercialization наружу** через рамки СНГ/Middle East/Asia partnerships. AIQ — главный example для Газпром нефти.
3. **Public KPI selective**: high-profile деплоиment (Цифровое месторождение, Cognitive Geo Ямал) — publicized; routine deployments — minimum publicity.
4. **Cyber consideration**: insourcing increases internal IT footprint → increases attack surface; cyber risk Q4 cross-cutting (см. §5.4).

**Limit для студента.** Курс не отдаёт предпочтение российскому или западному паттерну — оба имеют **структурные ограничения**. Западный disaggregated паттерн страдает от vendor pivot risk (BP+Beyond Limits) и vertical AI vendor distress (Cognite IPO postpone). Российский insourcing паттерн страдает от **limited audit / verification** в санкционном режиме, и **ограниченной коммерциализации** наружу. Студент должен **уметь читать оба** и понимать, **что специфично для каждого**.

### §5.4. Cross-cutting риск 1: киберугрозы +935% (Colonial, Shell MOVEit)

[for-slide-s37]

Кибербезопасность — **counter-trend** AI-расширения нефтегазовой автоматизации. По данным Zscaler, **ransomware-атаки на нефтегаз выросли на 935% между апрелем 2024 и апрелем 2025 года** [40]. Этот рост — не «random fluctuation»; это структурный эффект:

- **OT/IT convergence** (operational technology — industrial control systems — соединяются с corporate IT) **увеличивает attack surface**.
- **AI/digital deployment** добавляет новые ML-сервисы, новые data pipelines, новые API endpoints — каждый из них — potential entry point.
- **Threat actor capability растёт** через **offensive AI** (automated reconnaissance, phishing-as-a-service, AI-generated социальная инженерия).

**Канонические incidents.**

**Colonial Pipeline 2021.** Атакующий получил доступ через **VPN без MFA** (multi-factor authentication). Pipeline shutdown ~6 days; ~$5M ransom paid; **операционные потери — десятки миллионов долларов**; США federal coordinated response (Cybersecurity and Infrastructure Security Agency, CISA) [41]. Lesson: **flat OT/IT network + no MFA на VPN = unacceptable risk** для critical infrastructure.

**Shell MOVEit 2022 + vendor compromise 2024.** Shell был impacted by Clop ransomware через MOVEit file transfer vendor (third-party software, used by multiple companies для transfer data между systems). 2022 + 2024 incidents — customer data leaked; financial impact moderate, но reputational и regulatory follow-through significant [42].

**Defensive AI vs offensive AI — структурный gap.**

- **Defensive AI** (anomaly detection в OT-сетях, ML-based intrusion detection): **Dragos, Claroty, Nozomi Networks** — leading specialized vendors. **Растёт** post-Colonial.
- **Offensive AI**: атакующие используют LLM-агенты для **automated phishing**, social engineering, automated reconnaissance. **Растёт быстрее**, чем defensive AI.

**Выученный урок (фундаментальный для LO7).**

1. **AI добавляет complexity → attack surface растёт.** Каждый ML deployment — новая поверхность атаки. Невозможно «развернуть AI без cyber implications».
2. **Безопасность — phase 1, не phase 4.** Industry pattern 2018–2022 — «pilot AI, then think about cyber». Pattern 2024–2026 — **embed cybersecurity in design phase**, перед deploiement.
3. **AI security ≠ traditional IT security.** Adversarial ML, model poisoning, prompt injection — **новые классы атак**, для которых традиционная IT-security mature недостаточна. Specialized AI security teams + tooling необходимы.

**Связь с предыдущими разделами.**

- Q1 deployments (Aspen Mtell, Honeywell UOP Connect) — увеличивают OT/IT connectivity → cyber risk растёт.
- Q3 (Aramco METABRAIN, Eni HPC6) — централизованные HPC становятся high-value targets.
- Q2 (MethaneSAT, satellite data infrastructure) — satellite ground stations — critical infrastructure, потенциальная target.
- Q4 (CCS, EGS) — CCS injection wells + monitoring infrastructure — long-horizon assets, требующие cyber resilience десятилетий.

### §5.5. Cross-cutting риск 2: 2020 oil crash + Deepwater Horizon исторический якорь

[for-slide-s38]

Два cross-cutting эпизода, которые **обрамляют** всю AI-историю нефтегаза 2010-2026 годов: **2020 oil crash** и **Deepwater Horizon 2010**. Первый — context, в котором AI roadmap нефтегаза проходит через bottleneck. Второй — исторический урок про automation + human factors + alarm bypass.

**2020 oil crash контекст.**

В марте-октябре 2020 года, после пандемийного collapse нефтяного спроса (нефтяные фьючерсы West Texas Intermediate уходили в **отрицательную зону** 20 апреля 2020 года — впервые в истории), нефтегазовая индустрия пережила структурную shake-out.

- **107 000 рабочих мест потеряно** в US O&G и нефтехимии (Deloitte) — «fastest layoffs in industry history» [43].
- **BP — 10 000 уволенных** (15% workforce), плюс план «slash oil output by 40%» в рамках Beyond Petroleum pivot [44].
- **Shell — 9 000 уволенных**, including digital и new energies team [45].
- **Chevron, ExxonMobil, ConocoPhillips** — major cuts.
- **Cognite, C3.ai pipelines compressed** — AI vendors потеряли значимые revenue chunks.

**Что это означает для AI roadmap.**

1. **Industry cyclicality > AI hype cycle.** Когда нефть ниже $30/баррель — digital teams cuts first как «non-essential». AI projects заморожены 18–24 месяца. AI ROI horizon 5–7 лет; commodity cycle случается каждые 7–10 лет. **Эти горизонты несовместимы**, и AI roadmap должен это **explicitly account for**.
2. **Talent loss permanent.** После 2020 senior digital practitioners moved к tech, finance; recovery slow. **2021–2024 recovery не вернула pre-2020 staffing levels**; AI initiatives консолидированы у super-majors, которые могли позволить.
3. **2021–2024 recovery — концентрация у крупных операторов.** Maaжоры (ExxonMobil, Chevron, Shell, BP, TotalEnergies, NOCs) увеличили AI investments; малые и средние независимые операторы остались позади. Это **структурный сдвиг рынка** — AI стал **strategic moat для крупных**, не **commodity tool для всех**.

**Deepwater Horizon 20 апреля 2010 года — исторический якорь.**

Не AI failure напрямую, но **automation + human factors lessons** — релевантные для AI today.

**Что произошло.**

- Macondo well, BP-operated, Transocean rig в Gulf of Mexico.
- **Negative pressure test misinterpreted.** Команда видела anomalous показания, но интерпретировала как «безопасные» под влиянием cognitive bias к minimization.
- **Gas kick → blowout → explosion.**
- **11 deaths, 4.9 миллиона баррелей spilled в 87 дней.**
- **$60+ миллиардов total cost** для BP; criminal charges; десятилетие cleanup и litigation [46].
- **vs BP annual revenue 2010 ~$300 млрд = 20% годового revenue.**

**Automation + alarm lessons (релевантные для AI today).**

**Урок 1 — Alarm system bypassed.** General alarm на буровой установке был **выставлен в bypass** «to prevent waking workers с false alarms». Это **корпоративная культура bypass культуры** — когда false positive rate высокий, операторы и менеджеры **отключают alarms**, чтобы не нарушать operations. Когда methane shot вверх — **no audio/visual warning** → workers had no escape signal.

**Урок 2 — Independent alarms, no coordinated automation.** Каждый sensor работал отдельно — нет «3 sensors anomalous → trigger coordinated response». Современный AI **силён** в cross-sensor correlation, но **требует verification + audit trail**. Без verification возникает риск, что AI **fabricates** correlation, которая не существует.

**Урок 3 — Operator response — confusion.** Bridge officer Andrea Fleytas (23 года, <2 лет опыта на буровой) видела massive alarm panel, не уверена, что triggering response. **Junior operator с simple system > senior с complex AI.** AI sophistication не заменяет operator training; complex AI требует более sophisticated training, не меньше.

**Урок 4 — Negative pressure test misinterpretation.** Не AI test (classical engineering), но команда комплацентна. Pattern: **complex automation + insufficient operator training + alarm tolerance erosion = catastrophe**. Этот pattern повторяется в **Texas City refinery explosion 2005 (BP), Buncefield 2005 (UK), San Bruno pipeline 2010 (PG&E)** — все automation + human factors.

**Что значит для AI 2026 года.**

1. **Alert fatigue REAL.** Aspen Mtell claim «eliminates alert fatigue» (§1.3) — это marketing. **False positives disable trust в систему; затем real positive missed.**
2. **AI добавляет complexity** — без **structural improvements в operator training и organizational safety culture, AI просто ускоряет old failure modes.**
3. **Bypass culture — predictable response к high-false-positive systems.** Это **engineering reality**, не «корпоративная неудача». Когда vendor продаёт AI с обещанием «zero false positives» — это маркетинг.
4. **Safety culture > technology sophistication.** Junior operator + simple system + strong safety culture > senior operator + complex AI + weak safety culture.

### §5.6. Самопроверка по Разделу 5

1. **Российский insourcing AI vs западный disaggregated паттерн** — назовите 2 структурных преимущества российского подхода и 2 недостатка.

2. **Cyber +935% — какие AI deployments в нефтегазе наиболее уязвимы**, и **почему**? Сошлитесь на квадранты keystone-оси.

3. **2020 oil crash — как защитить AI roadmap от commodity cycle?** Предложите 3 практических механизма.

4. **Deepwater Horizon — 4 урока для AI today.** Перечислите и приведите для каждого современный пример возможной похожей ловушки.

---

## § Закрытие. Синтез 4-квадрантной матрицы + мост к Лекции 17

<!-- for-slide-s39 -->

### §6.1. Что мы прочитали — 4-квадрантный синтез

[for-slide-s39]

Возврат к keystone-матрице. Через все шесть разделов мы видели: AI в нефтегазе — **не одна история**, а **четыре разных истории**, в зависимости от того, какие данные доступны и насколько определена физика.

**Q1 (mature production — high data + high physics):** AI как **мультипликатор**. Working cases: Ambyint InfinityRL (+15% на 200 скважинах), Honeywell UOP Connect (310+ юнитов), Роснефть Digital Field (+1 Mt/год). **Failures**: 86% pilot stuck (McKinsey), Aspen Mtell alert fatigue + plant-wide stagnation, Cognite IPO postpone, C3.ai O&G declining.

**Q3 (frontier exploration — low data + high physics):** AI как **augmentation поверх physics simulators**. Working cases: Eni HPC6 (606 PFLOPS Top500 #5), Aramco METABRAIN (250B params, $1,8B realized 2024), SLB Lumi (Sep 2024), ExxonMobil Discovery 6 (4D-сейсмика месяцы → недели, Stabroek Guyana). **Failures**: BP+Beyond Limits ($20M vendor pivot 2023), IBM+Repsol Kalimba (2014–2022 wind-down).

**Q2 (методан-MRV — high data + low physics):** AI как **essential** для cross-modality fusion. Working cases: Carbon Mapper Tanager-1 (Aug 2024), GHGSat 16-spacecraft constellation, Bridger Photonics aerial LiDAR. **Failures**: MethaneSAT loss June 2025 (13 месяцев из 5+ лет дизайн-life), 4× discrepancy MethaneSAT vs EPA (15 Mt vs 4 Mt).

**Q4 (energy transition — low data + low physics):** **AI и физика struggle вместе**. Working pilots: Northern Lights CCS (1,5 Mt/год Норвегия), Fervo Energy EGS (IPO May 2026 +331%). **Failures**: 190× scale-up gap CCS (Northern Lights 0,02% от needed scale), refinery plant-wide stagnation в multi-physics frame.

**Cross-cutting (Russia + cyber + crash):** **Все 4 квадранта в санкционном режиме** для России (Газпром Cognitive Geo заменяет SLB Lumi в Q3; Роснефть Digital Field в Q1). **Cyber ransomware +935%** — counter-trend. **2020 oil crash 107k jobs** — industry cyclicality > AI hype cycle. **Deepwater Horizon 2010** — исторический якорь для automation + human factors уроков.

**Когда AI работает.** Q1 (мультипликатор) + Q2 (essential, с triangulation).
**Когда осторожно.** Q3 (augmentation only; не пытаться replace senior geologist).
**Когда опасно.** Q4 (long-horizon hallucination, multi-physics surrogate gap) + safety-critical SIS (где SIL3/SIL4 mandatory).

**За каждым AI deployment — alternative tool.** Eclipse / INTERSECT / CMG / OpenFOAM (vs ML reservoir surrogate). OGI hand-held (FLIR / Opgal) + Picarro / LI-COR portable (vs satellite AI MRV). Classical SCADA + PID + APC (Honeywell Profit Controller, Emerson DeltaV) — vs ML refinery controllers. SIS (SIL3/SIL4 certified deterministic + redundant 3oo2 voting) — vs ML safety logic. Senior geophysicist + классическая интерпретация — vs Foundation Model auto-interpretation. Federated learning + differential privacy — vs centralized AI cross-operator.

### §6.2. 10 documented failures и фундаментальный паттерн

[for-slide-s39]

Через главу мы разобрали 10 documented failures, которые повторяются как структурный паттерн отрасли:

| # | Failure | Раздел / часть | Урок |
|---|---|---|---|
| 1 | BP + Beyond Limits cognitive AI ($20M, vendor pivot 2023) | §2.5 / Часть 2 | Single-customer concentrated bet + vendor pivot risk |
| 2 | IBM Watson + Repsol Kalimba (2014–2022 wind-down) | §2.6 / Часть 2 | General-purpose «cognitive» не scales в narrow domain |
| 3 | Cognite IPO postpone ($94M ARR vs $2–3B cancelled) | §1.7 / Часть 1 | Vertical AI SaaS unit economics не proven в O&G |
| 4 | C3.ai O&G vertical declining (5.9% FY24 → declining) | §1.7 / Часть 1 | Foundation models едят vertical AI specialists |
| 5 | MethaneSAT loss июнь 2025 (~13 месяцев из 5+ лет) | §3.3 / Часть 3 | Single-satellite = catastrophic SPOF для regulatory MRV |
| 6 | 86% AI pilot stuck (McKinsey 2024) | §1.2 / Часть 1 | Структурная норма: pilot ≠ production |
| 7 | Aspen Mtell alert fatigue + refinery plant-wide stagnation | §1.3 / Часть 1 + §4.5 / Часть 3 | «Alert fatigue eliminated» = marketing; multi-physics surrogate gap |
| 8 | 2020 oil crash 107 000 jobs (BP 10k Shell 9k) | §5.5 / Часть 4 | Industry cyclicality > AI hype cycle |
| 9 | Метановая MRV 4× discrepancy (EPA 4 Mt vs MethaneSAT 15 Mt) | §3.5 / Часть 3 | Methodological gap industry vs регулятор structural |
| 10 | Cybersecurity ransomware +935% 2024-2025 (Colonial, Shell MOVEit) | §5.4 / Часть 4 | AI добавляет complexity → attack surface растёт |

**Bonus historical anchor:** Deepwater Horizon 2010 (alarm bypass + automation + human factors) — chapter deep-dive в §5.5; продолжающийся урок для AI in HSE.

**Фундаментальный паттерн.** 10 failures + 1 исторический якорь — это **не «AI плохой»**, а **повторяющиеся ловушки**: single-vendor concentrated bet (1, 2), vertical AI SaaS unit economics gap (3, 4), single-point-of-failure infrastructure (5), structural pilot purgatory (6), marketing claim vs operator reality (7), industry cyclicality (8), methodological structural gap (9), attack surface (10), and human factors (Deepwater Horizon). **Каждая ловушка имеет mitigation pattern** — мы прошли их по разделам. Инженер курса AI должен иметь эти patterns в working memory как **диагностические инструменты** на первой работе.

### §6.3. Мост к Лекции 17 — систематизация отраслевых паттернов курса

В Лекциях 11–16 курса мы прошли **шесть отраслевых лекций**:

- **Лекция 11** — дискретное и процессное производство (keystone «discrete vs process»).
- **Лекция 12** — автоматизация производства и цифровые двойники (keystone «шкала автономии A0→A3»).
- **Лекция 13** — логистика и транспорт (keystone «лестница среды»).
- **Лекция 14** — телеком, AIOps, кибербезопасность (keystone «лестница автономии: видит → решает → действует»).
- **Лекция 15** — энергетика (keystone «шкала автоматизации»).
- **Лекция 16 (эта)** — нефтегаз (keystone «матрица данные × физика»).

В **Лекции 17** мы делаем **systematization** — собираем универсальные паттерны:

1. **Когда AI работает** vs **когда AI не работает** — кросс-отраслевая taxonomy.
2. **Когда альтернатива (classical engineering) лучше** — общий decision framework.
3. **Структурные ловушки** — pilot purgatory, vendor pivot, single point of failure, multi-physics surrogate gap, alert fatigue, hype cycle disappointment.
4. **Карьерный путь инженера** — что значит «инженер AI» в 2026 году: не «человек, умеющий запускать модели», а **человек, умеющий читать границы применения AI и говорить «нет» неподходящему**.

Эта глава — последний отраслевой deep-dive перед systematization. Если читатель усвоил матрицу «данные × физика» как **диагностический инструмент** — он готов к Лекции 17.

**Hero-illustration s40.** В феврале 2026 года EDF + Google опубликовали **first global methane map** на основе MethaneSAT data, собранных до потери спутника. Карта — bittersweet payoff: мы потеряли спутник, но карта осталась. **Карта показывает измеримость на глобальном уровне как payoff of AI MRV era — и одновременно single point of failure**. Это и есть итог Лекции 16: AI в нефтегазе — это **измеримый успех + структурная уязвимость в одном кадре**.

**Final framing для инженера-выпускника.** Студент, окончивший лекцию 16 и применяющий keystone-матрицу в первой реальной работе, должен помнить: **матрица — это диагностический инструмент, а не классификация**. Реальная производственная операция часто **смешана**: один и тот же оператор может иметь Q1 mature production на одном бассейне, Q3 frontier exploration в другом регионе, Q2 methane MRV compliance в третьем сегменте регуляторных требований. Это не «оператор находится в одном квадранте» — это **оператор управляет portfolio AI projects, каждый из которых в своём квадранте**. Хороший инженер строит **portfolio reading**, не single-quadrant reading. Это последний урок главы.

**Карьерный мост.** Нефтегазовые компании (национальные и частные), сервисные подрядчики, регуляторы (Минэнерго, Минприроды, EPA, EU Commission), независимые научно-исследовательские институты, цифровые подразделения крупных НГК — все они ищут инженеров, способных читать AI through structural lens, а не «применять модели». Профильные технические университеты предлагают магистерские программы по AI в энергетике + нефтегазе; cross-disciplinary программы (петрофизика + ML, geomechanics + ML) — особенно ценны. Стажировка в digital practice любой крупной IOC / NOC / сервисного подрядчика — best entry-route в сектор.

---

## Q&A backup (12 ожидаемых вопросов с глубокими ответами)

Этот раздел — **резерв** для лектора и self-study студента. 12 вопросов, которые часто задают аудитория после Лекции 16, с deep-dive ответами 200–400 слов каждый.

### Q1. А что насчёт NVIDIA Omniverse для digital twin в нефтегазе?

NVIDIA Omniverse — платформа для 3D simulation и digital twin orchestration, активно продвигаемая NVIDIA в 2023–2025 годах для industrial markets. В нефтегазе — упоминается в SLB Lumi presentation (используется как visualization layer над Petrel), в Aramco METABRAIN (упоминается как infrastructure для visualization HPC outputs), в Cognite Data Fusion (visualization layer над time-series data).

**Структурная роль Omniverse** — это **visualization + collaboration layer**, не **simulation engine** в reservoir sense. Eclipse / INTERSECT всё ещё делают reservoir simulation; Omniverse визуализирует результат. Для нефтегаза это **не game-changer**, а **полезный tool в стек**. Cross-link к Лекции 12 (digital twin определения и слой архитектуры). Omniverse занимает слой 3 (visualization) в Лекции 12 архитектуре, не слой 1–2 (физическая модель + данные).

В практическом смысле — Omniverse оптимален для **inter-discipline collaboration**: где engineers + geologists + management смотрят на одну виртуальную модель одновременно. Для самой задачи моделирования он не заменяет Eclipse.

### Q2. Как connect Лекция 16 с Лекциями 14 (cyber) и 12 (digital twins)?

**С Лекцией 14 (cyber):** §5.4 в этой главе показывает, что **AI добавляет attack surface**. Colonial Pipeline 2021, Shell MOVEit 2022 + 2024 — конкретные примеры. В Лекции 14 мы прошли **MITRE ATLAS** framework — adversarial ML threats. В нефтегазовом контексте к ATLAS добавляются OT-specific угрозы: **process control logic poisoning, false alarm injection, sensor data manipulation**. Mitigation — defensive AI vendors (Dragos, Claroty, Nozomi), но они **отстают** от offensive AI capability.

**С Лекцией 12 (digital twins):** в Лекции 12 мы прошли **шкалу автономии A0→A3** + **digital twin как мост** между ступенями. Нефтегаз большинство deployments — на ступени **A0 (observe)** или **A1 (advise)** — Aspen Mtell, Honeywell UOP, Ambyint. **A2 (closed-loop)** — редкость, и в основном на узких циклах (single column, single compressor). **A3 (autonomous)** — практически отсутствует в нефтегазе из-за SIS / SIL3 / SIL4 ограничений + multi-physics constraints + sparse data в frontier exploration. Это **прямой translate** keystone-оси Q1–Q4: Q1 — мостик к A1/A2; Q3 — augmentation, остается на A1; Q4 — преимущественно A0/A1; Q2 — A1/A2 в narrow scopes (satellite data triage). Digital twin в нефтегазе — преимущественно **contextualized OT data**, не **physics-coupled twin** в смысле Лекции 12.

### Q3. AI в добыче редкоземельных металлов — пример из non-O&G mining?

Редкоземельные металлы (REE — rare earth elements) и lithium — критичные для clean-energy транзита. AI применения в mining REE имеют **похожий профиль** с frontier oil exploration:

- **Lithium brine extraction (Чили, Боливия, Аргентина):** AI для optimization evaporation pond timing + chemistry. Sparse data (единицы операций мира), high physics certainty (geochemistry described).
- **Hardrock REE mining (Mountain Pass California, Чибина в России):** AI для ore grade prediction + processing optimization. Mature operations имеют data; новые operations — frontier-like.
- **Deep-sea polymetallic nodule mining (planned 2026+):** completely frontier — нет analog data, no commercial operations to-date. AI здесь — **augmentation поверх physics**, не replacement.

**Keystone-матрица применима** к mining: данные × физика. Mature lithium operation = Q1. Pre-salt-like nodules = Q3. Critical mineral MRV (sourcing transparency) = Q2-like (cross-modality data fusion). AI в mining — это **applicable extension** уроков нефтегаза.

### Q4. Какой процент AI инвестиций в нефтегазе реально приносит ROI?

Точная цифра depends on definition «ROI» и methodology. **Lower bound:** McKinsey/BCG говорит **86% pilot stuck** — то есть ≤14% project'ов реально доходят до production. Из них значительная часть имеет marginal return, а не material lift. **Upper bound:** Aramco self-reports $1,8B realized 2024 на ~$3,5B annual R&D — то есть ~51% R&D return за один год (suspicious methodology, см. §2.2).

**Реалистичный middle ground:** **15–25% AI investments в нефтегазе приносят material ROI** (>20% IRR на capital invested) over 3–5 year horizon. Остальные 75–85% — либо marginal positive, либо negative, либо never deployed to production. Это похоже на **VC industry average** (success rate of ventures), не «software industry average».

**Что drives более высокий success rate.** (a) **Узкий scope deployment** (Ambyint = artificial lift, не «AI for upstream»). (b) **Anchor customer model** (Cognite на Aker BP) — но с ограниченной generalization. (c) **Insourcing для NOC** — meanings Aramco + Газпром нефть pattern. **Что drives более низкий success rate.** (a) **Pure-play vertical AI vendor** в нефтегазе. (b) **Foundation model promise без data foundation**. (c) **Multi-physics + long-horizon ambitions**.

### Q5. Можно ли применить foundation model approach к новому frontier basin без analog data?

**Короткий ответ — нет, не в 2026 году.** Foundation model требует **training data**, представительной для problem space. Frontier basin без analog data — это **out-of-distribution** относительно training corpus любой существующей foundation model (METABRAIN, Lumi, etc.).

**Что можно сделать:**

1. **Zero-shot inference на foundation model**, обученной на родственных бассейнах. Foundation model **может** генерировать «правдоподобные» интерпретации, но **они не валидируются** до накопления outcome data из реальных скважин в новом бассейне.
2. **Senior geophysicist + analog-basin reasoning.** Это **proven workable путь** для frontier exploration в 2026 году. AI остаётся consultative.
3. **Active learning approach.** Бурить первую скважину; собрать data; fine-tune foundation model on emerging data; бурить следующую — закрытый цикл обратной связи. **Это работает только после 5–10 wells**, когда накоплено достаточно training data.

**Anti-pattern:** доверять foundation model auto-interpretation в frontier basin без analog. Это рецепт ошибочной интерпретации с потенциальными $50–100M на ошибочную drilling location.

### Q6. Что мешает AI заменить blowout preventer (BOP) — техническое или регуляторное ограничение?

**Оба, но регуляторное primary в 2026 году.** Технически — ML model может предсказывать blowout с высокой точностью на training distribution; но **probability of failure on demand (PFD)** для ML — не доказывается аналитически, как для дискретной логики. Регуляторно — **ISA-84 / IEC 61511** требуют SIL3 (PFD 0,001–0,0001) или SIL4 для safety systems class BOP. **ML не сертифицируется** в этих frameworks в 2026 году.

**Что может измениться к 2030 году.** (a) **Formal verification of ML model behavior** на сужающемся scope — academic research направление. (b) **Hybrid AI + rule-based design** — ML предлагает action, deterministic rule-engine санкционирует. (c) **Updated standards** — IEC может update IEC 61511 для accept ML в специфических scopes. Но это **medium-term direction**, не «вот-вот».

**Текущий пайтон.** AI в BOP context — **decision-support** (ML предсказывает выброс на 5–15 минут раньше; operator + SIS действует на отказ; SIS — deterministic, не ML).

### Q7. Если 86% пилотов застряли — почему всё ещё инвестируют?

**Три параллельных динамики.**

1. **Survivor bias успешных 14%.** Те 14% which делают breakthrough — публичные референсы (Aramco $1,8B, ExxonMobil Discovery 6 unlock $1B+). Когда индустрия читает референс — она недооценивает прохождение через pilot purgatory тех 86%, кто не сделал.
2. **Strategic option value.** Даже если конкретный pilot не делает ROI, **portfolio of pilots** может построить organizational capability. Один из portfolios сделает breakthrough. Это **VC-like decision-making**, не traditional engineering ROI calculus.
3. **Regulatory + competitive pressure.** EU 2024/1787 требует methane MRV — operators инвестируют не выбором, а **обязательностью**. Competitive — если конкурент сделал AI-deployment с claim'ом «−15% cost», вы обязаны инвестировать в paralel, даже если у вас будет 75% chance failure.

**Что должен делать инженер.** Не «надо инвестировать в AI», а **дискриминирующая оценка**: какие из этих 3 динамик applies к вашему случаю? Strategic option — да, инвестируйте, но **portfolio approach**, не single bet. Regulatory mandate — да, инвестируйте под minimum compliance. Competitive — only if metric'и конкурента **independent verified**.

### Q8. Какой стек я должен изучить, чтобы работать AI-инженером в нефтегазе?

Без специфических университетских рекомендаций — universal answer для студента-инженера.

**Базовый стек (must-have):**

- **Python + ML libraries** (scikit-learn, PyTorch, XGBoost).
- **Time-series analysis** (statsmodels, ARIMA, prophet, нейронные RNN/LSTM).
- **Numerical methods** (numpy, scipy) — для понимания physics-based simulators.
- **SQL + time-series DB** (PostgreSQL, InfluxDB, TimescaleDB) — для работы с industrial data.

**Domain (без него инженер AI — generic):**

- **Reservoir engineering basics** — pressure-volume-temperature, multiphase flow, well productivity index.
- **Drilling operations** — daily ops cycle, mud properties, ROP factors.
- **Refinery operations** — крекинг, дистилляция, APC basics.
- **HSE** — IEC 61511 / ISA-84 на уровне principles, OGMP 2.0 / EU Methane Reg на уровне знакомства.

**Tools (полезно но не critical):**

- Eclipse / INTERSECT / CMG basics — хотя бы понимать output structure.
- OPC UA / Modbus / industrial protocols.
- AWS / Azure data engineering basics.

**Best entry-route:** internship у NOC (Газпром нефть, Роснефть, аналоги в West) или у сервисного подрядчика (SLB, Halliburton, Baker Hughes) с focus на digital practice. Это даёт **domain immersion + AI exposure** одновременно.

### Q9. AI MRV — это решение проблемы метана или новая проблема?

**И то, и другое.** AI MRV — это:

- **Решение** в смысле, что без слияния satellite + aerial + drone + ground OGI индустрия не может **measure** реальный масштаб метановых выбросов. Это primary value AI в Q2.
- **Новая проблема** в смысле, что:
  - **Methodological inconsistency** (factor 2-4 between methods) создаёт regulatory enforcement gap.
  - **Single-satellite SPOF** (MethaneSAT loss) — критическая infrastructure уязвимость.
  - **AI hallucination в downstream interpretation** — risk falsely attributing emissions к specific source.
  - **Costs scaling** — global satellite MRV infrastructure требует hundreds of millions of dollars / year sustained.

**Net answer:** AI MRV — это **necessary but insufficient** компонент в methane reduction stack. Без него реальный масштаб не виден; **с ним без triangulation** — false confidence. Workable путь — **triangulated multi-method monitoring** + **regulatory enforcement через EU 2024/1787 + EPA Subpart W** + **operational improvements в LDAR programs** + **direct measurement обязательность для Level 5 reporting**. AI — это **layer над данными**, не **источник данных**.

### Q10. Если CCS scale-up gap 190× — может ли AI вообще помочь, или это безнадёжно?

**AI помогает с per-unit cost, но не масштабом.** Conkretно:

- **Per-tonne capture cost снижается** с $80–120 к $65–100 через AI optimization absorber processes (10–20% reduction). Это **value**, но **не масштабирует сам по себе**.
- **Per-project deployment time** сокращается через AI-augmented site selection + monitoring. Тоже **value**, но **не масштабирует**.
- **Total scale-up** (40 Mt/год → 7,6 Gt/год = 190×) — это **capital + regulatory + geopolitical** problem, не AI problem.

**Что **должно** помочь сверх AI:** (a) **carbon pricing** на уровне $100+/тонна для economic case. (b) **state mandates + subsidies** (US IRA + EU CCS Directive expansion). (c) **standardization** geological assessment + permit procedures across jurisdictions. (d) **public acceptance** captured CO₂ storage. AI accelerates каждый из них, но **не заменяет** ни один.

**Reasonable expectation для 2050:** CCS capacity scales to 1–3 Gt/год global (4× IEA targets, but **30× from current 40 Mt/год**), of which 30–50% — AI-optimized operations. Это **значительный progress**, but **short of 7,6 Gt target**. AI — partial solution; **system-wide policy + capital reallocation** — full solution.

### Q11. Можно ли сделать AI-стартап в нефтегазе сегодня, или поздно?

**Поздно для horizontal vertical AI platform (Cognite-style).** Foundation models + insourcing у NOC съели этот market. Stick-from-scratch generic «industrial AI platform» в 2026 — almost certain failure.

**Возможно для нишевого scope.** Successful 2024–2026 entries:

- **Bridger Photonics** — aerial LiDAR Gas Mapping (узкая ниша satellite-aerial gap).
- **SeekOps** — drone-based methane (узкая ниша midstream + utilities).
- **Fervo Energy** — EGS with AI orchestration (cross-vertical: clean tech + AI).
- **AIQ** (ADNOC + G42) — Middle East regional cloud + AI stack (geopolitical niche).

**Что характеризует successful нишу.** (a) **Specific technical capability** AI doesn't generalize (LiDAR Gas Mapping = specific hardware + ML co-design). (b) **Underserved geographic / regulatory niche** (EU methane compliance, Middle East cloud). (c) **Anchor customer ready to pay $5M+ ARR** for narrow scope.

**Что не работает.** «Foundation model для нефтегаза» — едят NOC/super-major internal teams. «AI для production optimization» — едят existing vendors (Ambyint, OspreyData, SLB Avocet). «Digital twin platform» — ест Cognite (даже с distress), и foundation models compress space.

### Q12. Что определяет, какой квадрант актуален для конкретной операции?

**Two-dimensional decision tree.**

**Шаг 1 — Data availability.** Сколько у вас training samples / историческая data?
- **>1000 wells / 10+ years data:** high data → Q1 или Q3.
- **<100 wells / <5 years data:** low data → Q3 или Q4.

**Шаг 2 — Physics certainty.** Существует ли валидированный numerical simulator для вашей проблемы?
- **Yes (Eclipse / INTERSECT / CMG / OpenFOAM покрывает):** high physics → Q1 или Q3.
- **No (cross-modality fusion, atmospheric attribution, long-horizon CCS на 100 лет):** low physics → Q2 или Q4.

**Перекрест:**

- High data + High physics → **Q1 mature production**.
- Low data + High physics → **Q3 frontier exploration**.
- High data + Low physics → **Q2 methane MRV-like (cross-modality)**.
- Low data + Low physics → **Q4 energy transition-like**.

**Действие per квадрант.**

- **Q1:** AI как multiplier. Узкий scope. Проверить **6 критериев «здесь AI не нужен»** (§1.8) до commit.
- **Q3:** AI как augmentation. Senior expert + classical simulator + ML screening. **Не try replace expert**.
- **Q2:** AI essential, но обязательно **triangulation** (multi-modality). Single source — risk.
- **Q4:** Hybrid AI + physics. **Long-horizon prediction — sanity check via classical physics**.

Это **diagnostic tool**, который инженер курса должен иметь в working memory.

---

## Reading list (рекомендованная литература)

**Industry analysis:**

- [BCG. *AI-First Future of Oil and Gas Companies*. 2025.](https://www.bcg.com/publications/2025/ai-first-future-of-oil-and-gas-companies) — структурный анализ industry-wide AI adoption + 86% pilot stuck.
- [BCG. *The Widening AI Value Gap*. October 2025.](https://media-publications.bcg.com/The-Widening-AI-Value-Gap-October-2025.pdf) — детальный numerical breakdown 60% companies no material value.
- [Domestic Operating. *The Hidden Truth About AI in Oil and Gas*. April 2025.](https://www.domesticoperating.com/blog/2025/04/17/the-hidden-truth-about-ai-in-oil-and-gas/) — DNV/Accenture 15% live ops / 3% advanced; data cleaning 60–80% time.
- [DataRobot. *LLM Hallucinations in Agentic AI*. 2025.](https://www.datarobot.com/blog/llm-hallucinations-agentic-ai/) — Gartner 2027 prediction 40% agentic AI projects fail; relevance к Q4 long-horizon.

**Technical depth (HPC + foundation models):**

- [Top500 supercomputers ranking. December 2024 list.](https://www.top500.org/) — Eni HPC6 #5 placement.
- [HPCwire. *ExxonMobil Discovery 6 supercomputer*. 2025.](https://www.hpcwire.com/off-the-wire/exxonmobil-deploys-discovery-6-supercomputer-to-advance-4d-seismic-imaging/) — 4D-сейсмика deployment.
- [Middle East AI News. *Aramco's $4B AI value impact*. 2024.](https://www.middleeastainews.com/p/aramco-ai--drives-4-billion-value) — Aramco AI realized value methodology.

**Methane MRV:**

- [EDF. *MethaneSAT 2025 Project Updates*.](https://www.methanesat.org/project-updates/2025-was-year-highs-lows-and-hope-methanesat) — MethaneSAT loss June 2025 + lessons.
- [EDF. *New Data Show US Methane Emissions Over 4× Higher Than EPA Estimates*. 2024.](https://www.edf.org/media/new-data-show-us-oil-gas-methane-emissions-over-four-times-higher-epa-estimates-eight-times) — 4× discrepancy paper.
- [Stanford News. *Methane emissions higher than government predictions*. March 2024.](https://news.stanford.edu/stories/2024/03/methane-emissions-major-u-s-oil-gas-operations-higher-government-predictions) — Stanford 2024 aerial 7,5 Mt = factor 2.
- [AMT Copernicus. *9-Satellite Single-Blind Methane Test 2024*.](https://amt.copernicus.org/articles/17/765/2024/amt-17-765-2024.pdf) — 0 false positives / 58% correctly identified.
- [Reed Smith. *EU Methane Regulation Analysis*. August 2024.](https://www.reedsmith.com/en/perspectives/2024/08/eu-methane-regulation-application-lng-coal-mine-operators-importers) — EU 2024/1787 deep dive.

**Regulatory:**

- [EU Methane Regulation 2024/1787](https://eur-lex.europa.eu/) — official text + commentary.
- [US EPA Subpart W final rule. May 2024.](https://www.epa.gov/newsreleases/biden-harris-administration-announces-final-rule-cut-methane-emissions-strengthen-and) — final rule + September 2024 proposed delay.

**Historical anchor:**

- [EHS Today. *Deepwater Horizon: An Ongoing Lesson in Safety*.](https://www.ehs.com/blogs/deepwater-horizon-an-ongoing-lesson-in-safety/) — alarm bypass + automation lessons.
- [Fortune. *2020 Oil Crash + 107k Jobs*. October 2020.](https://fortune.com/2020/10/05/oil-gas-jobs-transition-climate-coronavirus/) — industry cyclicality.

**Russia specifics:**

- [ROGTEC. *Gazprom Neft Cognitive Geologist*.](https://www.rogtecmagazine.com/gazprom-neft-and-ibm-research-brazil-are-using-ai-to-improve-quality-in-processing-geological-information/) — Cognitive Geo deep dive.
- [Rosneft press. *Digital Field Bashneft*.](https://www.rosneft.com/press/news/item/195125/) — Digital Field deployment.

**Energy transition:**

- [MDPI Sustainability. *Northern Lights CCS Analysis*.](https://www.mdpi.com/2071-1050/17/13/5754) — CCS scale-up + AI applications.
- [SHM Studio. *Fervo Energy IPO + AI Data Centers*.](https://shm.studio/en/news/fervo-energy-ipo-geothermal-data-center-ai/) — Fervo + AI data center demand.

**Cyber:**

- [Cybersecurity Dive. *Ransomware in Energy +935%*. 2025.](https://www.cybersecuritydive.com/news/zscaler-ransomware-report-manufacturing-targeted/756147/) — Zscaler data.
- [ProArch. *Colonial Pipeline Lessons Learned*.](https://www.proarch.com/blog/the-colonial-pipeline-attack-lesson-learned) — Colonial 2021 incident analysis.

---

## References

(Inline numbered references из всех 4 частей главы.)

1. NASA Earth Observatory / NOAA VIIRS Nightfire. Permian Basin 2024 flaring data. ~2 593 plumes / ~34 000 t methane/h peak.
2. BP filings 2010–2020. Total Deepwater Horizon cost ~$60+ billion vs annual revenue 2010 ~$300B = 20% revenue exposure.
3. McKinsey ~86% AI projects in energy not progress beyond pilot. Cited in BCG analysis September 2025.
4. BCG. *The Widening AI Value Gap*. October 2025. 60% companies no material value; AI leaders 1.5× revenue growth, 1.6× shareholder returns.
5. DNV / Accenture. 2024 O&G professionals survey: 15% live ops, 3% highly integrated, 47% piloting.
6. Cognite ARR 2024: $94M (+40% YoY); 871 employees April 2026. Aker ASA earnings calls 2024–2025.
7. C3.ai 8-K filings FY24/FY25. Oil&Gas vertical 5.9% FY24 revenue declining absolute in FY25.
8. AspenTech case study. 10 days production saved through compressor + bearing detection. «Alert fatigue eliminated» — vendor claim.
9. Ambyint case study. InfinityRL +15% production on 200 wells average baseline.
10. ExxonMobil + Pioneer merger May 2024. $59.5B all-stock; combined Permian holdings 1.4M net acres + ~16B BOE.
11. Honeywell UOP press release 2024. 310+ units connected on 100+ sites; plan 750+ within year.
12. Nabors SEC 8-K Q2 FY25. PACE-X 20 000 ft Haynesville lateral (32 000 ft total depth). 75+ rigs fleet.
13. Rosneft press. Digital Field Bashneft Ilishevskoye. +1 Mt/y additional production (+5.9% vs ~17 Mt/y baseline 2023). ~1B RUB/y economic effect.
14. IANS analysis. Rosneft 23 software products / 10 commercial.
15. Cognite + Aker BP partnership. 260k time series, 1.5T data points, 700k documents in Cognite Data Fusion.
16. C3.ai 10-K 2024. Oil&Gas vertical $18M / $310M total revenue.
17. Eni HPC6 inauguration December 2024. 606 PFLOPS peak / 477 PFLOPS sustained; 14k AMD MI250X; ~$104M capex. Source: DCD.
18. Middle East AI News. Aramco METABRAIN 250B parameters (claim 2024 [VFY-day-of]).
19. EnkiAI. Aramco AI initiatives 2025. METABRAIN training corpus 7T tokens + 90 years operational data.
20. Davos January 2025. Aramco CEO Amin H. Nasser statement: $1.8B realized AI value 2024. Future Digital Twin coverage.
21. SLB Lumi launch September 2024. NVIDIA Grace Hopper compute; customers Aker BP, Shell, Azule Energy.
22. SLB 8-K Q4 2024. Digital revenue $2B+ full year 2024 (5.7% total SLB revenue $35B).
23. HPE blog 2025. ExxonMobil Discovery 6: 4 032 NVIDIA Grace Hopper Superchips on HPE Cray EX4000.
24. EDF MethaneSAT release 2024. Permian Basin 410 t methane/h = 50% higher than EPA estimates.
25. SpaceNews. GHGSat 16-satellite constellation by 2025.
26. Highwood Emissions Research Digest 017. BC LDAR aerial 4× higher than ground OGI on same sites.
27. Stanford Report. Methane emissions higher than government predictions. *Nature*, March 2024. US O&G ~7.5 Mt/y aerial.
28. Highwood Emissions Research Digest 017. As [26].
29. AMT Copernicus 2024. 9-satellite single-blind methane test: 0 false positives, 58% correctly identified, 41 false negatives.
30. EU Methane Regulation (EU) 2024/1787 adopted August 2024. OGMP 2.0 Level 4/5 alignment; up to 20% turnover penalty. Reed Smith analysis.
31. EPA. Federal Register September 2024. Subpart W proposed delay to 2034.
32. MDPI Sustainability 2025. AI in CCS: 10–15% improved monitoring accuracy. Northern Lights case.
33. MDPI Sustainability 2025. AI in CCS capture: 10–20% cost reduction (Mongstad, Boundary Dam projects).
34. SHM Studio. Fervo Energy IPO May 2026 +331% to offering price [VFY-day-of]. Cape Station Utah $206M financing June 2025.
35. Gartner (in DataRobot post). 2027 prediction: 40% agentic AI projects to be cancelled due to cost overruns + poor risk controls.
36. ROGTEC. Gazprom Neft Cognitive Geologist. Geology work 3–4 months → minutes for certain task categories.
37. ROGTEC + Globuc. Gazprom Neft target: cut twofold time to first oil; +40% projects acceleration to 2030 vs baseline 2020–2023.
38. AGBI + ROGTEC. AIQ (ADNOC + G42 JV) valuation $1.4B+ post Presight 51% acquisition May 2024.
39. Cognitive Pilot press releases. 700+ installations 2021 → 1700+ 2024 [VFY-day-of]. Primarily agricultural; transferable to heavy O&G equipment.
40. Zscaler / Cybersecurity Dive 2025. Ransomware attacks on O&G +935% between April 2024 and April 2025.
41. ProArch analysis. Colonial Pipeline 2021: attacker via VPN without MFA; ~6 days shutdown.
42. The Record + Daily Security Review. Shell impacted by Clop ransomware (MOVEit) 2022 + 2024 vendor compromise.
43. Fortune October 2020. 107 000 jobs lost in US O&G/chemicals March–August 2020 (Deloitte).
44. Offshore Energy 2020. BP 10 000 layoffs (15% workforce) + plan slash oil output by 40%.
45. Offshore Energy 2020. Shell 9 000 layoffs.
46. Wikipedia + EHS. Deepwater Horizon 20 April 2010. 11 deaths, 4.9M barrels spilled, 87 days. Alarm system bypassed «to prevent waking workers with false alarms».

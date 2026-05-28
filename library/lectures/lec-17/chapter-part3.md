---
lecture: 17
part: 3
title: "Лекция 17. Часть 3 — Карта 16 отраслей"
parent: chapter.md
---

## Оглавление (Часть 3)

- [Раздел 3. Карта 16 отраслей на 2D-плоскости](#раздел-3-карта-16-отраслей)
  - [§3.0 Введение раздела](#30-введение)
  - [§3.1 Карта reveal: 4 стартовые точки](#31-starter-точки)
  - [§3.2 Карта reveal: middle batch](#32-middle-batch)
  - [§3.3 Карта reveal: final batch + bimodal nature + L16 anchor](#33-final-batch)
  - [§3.4 Cluster analysis 1 — closed-loop квадрант](#34-cluster-closed-loop)
  - [§3.5 Cluster analysis 2 — open-environment квадрант](#35-cluster-open-environment)
  - [§3.6 Cluster analysis 3 — high-stakes mid-fit](#36-cluster-high-stakes)
  - [§3.7 Пустые квадранты как дидактика](#37-пустые-квадранты)

См. `chapter-part3b.md` для Раздела 4 (Топ-12 провалов курса) — отдельная часть из-за document size limits.

---

## Раздел 3. Карта 16 отраслей

### §3.0 Введение

[for-slide-s18]

Мы построили инструменты в Разделах 1 и 2: горизонтальная ось (применимость ИИ, 7 критериев) и вертикальная ось (лестница автономии L0→L5). Теперь — главное упражнение capstone: **нанесём шестнадцать отраслей курса на эту плоскость** и посмотрим, что получится.

Цель — двойная. **Первая** — закрепить интуицию: где находятся успешные применения, где провалы, и почему. Карта **видимо** показывает разделение в кластеры, и эти кластеры объясняют большинство паттернов курса. **Вторая** — научить вас **переносить опыт**: когда вам встретится отрасль, не разбиравшаяся в курсе (страхование, городское планирование, образование, сельское лесоводство, ритуальные услуги), вы должны уметь **самостоятельно** разместить её задачи на этой плоскости и из координат вывести рекомендации.

Карта не статична. Точки на ней сдвигаются по мере развития технологий: то, что в 2022 году было L3 narrow ODD (раннее Waymo), в 2026 году стало L4 broad ODD. То, что в 2018 году обещало быть L4 (Monarch автономный трактор), в 2025 году провалилось и вернулось в нижний кластер. Карта 2026 года — снимок на момент publication; через 2-3 года точки будут другими.

**Что не сдвигается** — это **структура осей**. Применимость и автономия как концепции устойчивы. Семь критериев применимости и шесть ступеней автономии остаются valid framing независимо от того, какая модель занимает state-of-the-art.

Раздел построен **слой за слоем**. Сначала покажем первые четыре точки (один из каждого Modules курса), потом средний batch, потом финальный с особым вниманием к **бимодальным отраслям** (L13 — три точки!). Потом — кластерный анализ: три ключевых кластера (closed-loop, open-environment, high-stakes mid-fit) и обсуждение **пустых квадрантов** как дидактического приёма.

### §3.1 Starter точки

[for-slide-s20]

Начнём с **четырёх стартовых точек**, по одной из каждого «семейства» курса. Эти точки — каноничные success-кейсы, каждый из них показывает чистую координату на карте.

**L4 — Разработка ПО (Software Engineering).** Координата: **высокая применимость + высокая автономия, верхний правый**. SE — типичный квадрант 1.

Применимость высокая, потому что:
- Текст / код — modality, в которой foundation models работают эффективно.
- Compiler даёт мгновенный ground truth — критерий 5 удовлетворён.
- Объём гигантский (миллиарды строк кода ежедневно) — критерий 3.
- Цена ошибки автодополнения низкая (Esc / Ctrl-Z) — критерий 4.

Автономия высокая (но capped на L3-L4 для production):
- L1 (A) — autocomplete (GitHub Copilot для всех).
- L2 (B) — mid-task block (Copilot Workspace).
- L3 (C) — PR-from-spec (Copilot agent mode, Cursor Composer, Claude Code на well-scoped задачах).
- L4 (D) — engineering-agent (Devin overpromised; реальные D-уровни — Claude Code + Cursor Composer на narrow tasks).

**На карте:** одна точка для SE в верхнем правом, или **четыре точки** для A/B/C/D, спускающиеся по Y. В дидактически упрощённой версии — одна точка.

**L5 — Финансы и ритейл.** Координата: **mid-high применимость + mid автономия, верхний-середина**.

Применимость mid-high:
- Closed-world prediction для anomaly detection (фрод) — высокая.
- Open-world prediction (iBuying, real estate) — низкая (Zillow showed why).
- Customer service — middle (long-tail плох).

Автономия mid:
- L1 — рекомендации (recommendation engines).
- L2 — fraud auto-block (Stripe Radar, Visa AI на high-confidence).
- L3 — кредитный скоринг под EU AI Act capped до L1-L2 explanability.

**На карте:** L5 — точка в верхнем-середине; для иллюстрации можно показать как cloud (фрод высоко, iBuying низко).

**L7 — Медицина и фармацевтика.** Координата: **высокая применимость на narrow imaging + регуляторно-капнутая автономия = нижний правый**.

Применимость:
- Narrow imaging (X-ray, CT, retina) — высокая благодаря AlphaFold, Aidoc.
- Open-world clinical decision — низкая (IBM Watson провалился).
- Drug discovery в закрытой среде — высокая (AlphaFold протеомика).

Автономия:
- L1 always для clinical decisions (FDA mandate).
- L1-L2 для drug discovery pipelines (AlphaFold prediction → human chemist validates).
- L0 для high-stakes diagnosis.

**На карте:** L7 в нижнем-правом квадранте (высокая применимость, регуляторно ограниченная автономия).

**L9 — Авиакосмос и оборона.** Координата: **высокая применимость на Sense, ограниченная на Act = верхний-середина с restricted top**.

Применимость:
- Sense (satellite imagery, radar fusion) — высокая.
- Decide (route planning, target identification) — moderate.
- Act (LAWS) — restricted этически и регуляторно.

Автономия:
- L1-L3 для Sense + Decide в большинстве систем.
- L4-L5 только в unmanned narrow scenarios (loitering munitions debate).

**На карте:** L9 в верхнем-середине; bounded by regulatory ceiling.

После этих четырёх точек на карте уже видна **структура**: верхний правый — IT-adjacent (SE), нижний правый — регулируемая медицина (высокая применимость, низкая автономия), верхний-середина — финансы и оборона. Каждый из этих доменов имеет свой характерный потолок автономии. Дальше добавим средний batch.

### §3.2 Middle batch

[for-slide-s21]

Добавляем четыре отрасли среднего batch — L6 CAD/CAM, L8 креатив, L10 агро, L11 manufacturing.

**L6 — CAD/CAM (инженерное проектирование).** Координата: **mid применимость + L1-L3 автономия = середина**. *Главный кейс L6:* GM seat bracket (Autodesk Generative Design 2018) — пример **misframing**: в маркетинге назван «generative AI», но фактически — topology optimization алгоритм с RL exploration, не foundation model. ORCA benchmark 2024 показал, что LLM-ассистенты для CAD scripting достигают 45-63% accuracy — **ниже production-ready threshold** в инженерном domain.

Применимость зависит от класса задачи:
- Optimization (ML / topology) — высокая (NASA ST5 antenna; Autodesk Fusion generative).
- Surrogate models / PINN — moderate; работают для well-bounded физических задач.
- LLM-ассистент для CAD scripting — low (ORCA benchmark 45-63% accuracy).
- Generative geometry — overhyped в маркетинге (GM seat bracket = optimization, **не** generative AI в смысле foundation model).

Автономия:
- L1 advisory для большинства (designer проверяет).
- L3 narrow для optimization (RL/GA сами генерируют variants).
- L0 для финальной сертификации (всегда полный FEM, регуляторная подпись аттестованного инженера).

**На карте:** L6 в среднем кластере, с уклоном к нижнему-левому для финальной сертификации. **Главный урок L6 для capstone**: «AI в design» — это **не одна категория**, а 6 разных классов с разным AI fit; маркетинг конфлейтит их.

**L8 — Креативные индустрии.** Координата: **высокая применимость на mass-production assets + L2-L3 автономия = верхний-середина**.

Применимость:
- Mass-production assets (concept art, B-roll, marketing visuals) — высокая.
- Signature creative work (главный фильм режиссёра, главная картина художника) — низкая (Hollywood SAG-AFTRA strike 2023).
- Music background — высокая (Suno, Udio).

Автономия:
- L2 — AI generates, human curates (типичный workflow для marketing).
- L3 — AI generates fully autonomously для commodity assets.

Особые риски:
- **IP leak** (Getty v. Stability 2023; NYT v. OpenAI 2023) — провал #9.
- **Deepfake fraud** ($25M Hong Kong Arup — CFO + colleagues video conference, февраль 2024).

**На карте:** L8 в верхней-середине; bimodal по mass vs signature.

**L10 — Сельское хозяйство.** Координата: **bimodal — closed-loop CV высокая, open-environment низкая**.

Применимость:
- Closed-loop CV (See & Spray, LaserWeeder) — высокая. **Это типичный chiseled task.**
- Open-loop biological prediction (yield под изменчивым климатом) — низкая.
- Advisory (Crop Wizard) — moderate.

Автономия:
- L1-L2 для advisory + Sense.
- L3 narrow для See & Spray в специфическом ODD (молодые соевые на конкретной фазе).
- L4-L5 **failed** — Monarch Tractor (38% layoffs январь 2025 ≈ 53 из ~140 employees peak Q3 2024); Plenty Vertical Farms ($940M+ raised since 2014; valuation collapse $1.9B → <$15M; Chapter 11 март 2025).

**На карте:** L10 — bimodal cloud: чистая chiseled задача (See & Spray) — в верхнем правом; открытая среда (Monarch) — в верхнем левом с пометкой failure (попытка высокой автономии при низкой применимости).

**L11 — Manufacturing (дискретное + процессное).** Координата: **mid применимость + L0-L2 автономия (по большей части) = середина-низ**. *Главный кейс L11:* keystone «Discrete vs Process manufacturing» — две разные физики, разный AI fit. В дискретном (автосборка, электроника) — CV inspection и Six Sigma SPC доминируют; AI как замена SPC обычно не окупается. В процессном (химия, металлургия, нефтегаз) — MPC доминирует десятилетиями; RL впервые показан индустриально в Yokogawa FKDPP / JSR plant 2022 (35-day run).

Применимость:
- Computer vision на конвейере — высокая (Cognex, FANUC inspection systems; миллиарды изображений в год).
- Predictive maintenance — moderate (часто overpromise vs delivered; F-35 ALIS канонический pitfall).
- Process control RL — rare (Yokogawa FKDPP — первое промышленное применение в industry, 2022).
- LLM на PLC code (IEC 61131-3) — низкая (confidently wrong syntax; safety-critical control не доверяется LLM).

Автономия:
- L0 для safety-critical PLC (IEC 61508 SIL 2/3 — регуляторно required для функционально безопасных систем).
- L1-L2 для advisory + CV + soft sensors.
- L3 rare (только в special scenarios типа FKDPP).
- L4 нет в production.

**Главный урок L11 для capstone**: «manufacturing AI» — не одна категория; дискретное и процессное **разные** физики с разными baseline-альтернативами (SPC vs MPC). Большинство AI-инициатив в manufacturing провалились на pilot purgatory именно из-за неучёта differences (см. провал #12 в §4.12 — chapter-part3b.md).

**Pilot purgatory особо актуален.** **MIT NANDA / Sloan «State of AI in Business 2025»**: 95% GenAI-пилотов не доходят до production (≈5% генерируют measurable revenue). **McKinsey «State of AI 2025»**: 78% organizations использует AI, но только **5.5% high-performers** дают >5% EBIT impact (это **другое** измерение — про high-performer concentration, не про pilot failure rate). В РФ — 9 из 10 пилотов не доходят до production (ВЦИОМ + Strategy Partners 2024-2025, РФ-данные). 75% digital twin внедрений stuck в research/lab phase (industry survey 2024). См. провал #12 в Разделе 4 (chapter-part3b.md).

**На карте:** L11 в середине-нижней части плоскости.

После этого middle batch на карте видно два кластера:
- Кластер «closed-loop chiseled задачи» в верхнем правом (SE, фрод, See & Spray, складская робототехника, медицинская визуализация).
- Кластер «high-fit высокого regulatory ceiling» (capped) в нижнем правом — высокая применимость, низкая автономия (медицина clinical decisions, manufacturing safety, авиакосмос Act).

И начинает быть видна **третья зона** — верхний левый квадрант, где находятся **провалы** (Monarch, Plenty, Cruise robotaxi). Это «зона предупреждения»: попытка высокой автономии при низкой применимости.

### §3.3 Final batch

[for-slide-s22]

Добавляем финальный batch — L12 automation/twins, L13 logistics, L14 cyber, L15 science, L16 oil-gas. Здесь особо важна **bimodal nature** некоторых отраслей.

**L12 — Factory automation + digital twins.** Координата: **A0-A3 spread, mid применимость на A1, rare A3 = середина с tail в верхний правый**.

Применимость:
- A0 наблюдение (CV inspection) — высокая.
- A1 advisory (recommendation для оператора) — high.
- A2 closed-loop control — narrow (Yokogawa FKDPP, single chemical plant 35-day run).
- A3 full autonomy (Toyota Digit / Cassie robotics) — pilot phase.

Автономия:
- L0-L2 большинство.
- L3-L4 narrow (FKDPP, Cassie pilots).

Особо: **digital twin как мост от A1 к A3**. Без качественного twin переход на L4 автономию не работает (75% digital twin projects fail).

**L13 — Логистика и транспорт.** Координата: **bimodal — три отчётливые точки** на карте.

- **Точка 1 — складская робототехника (warehouse L1 — controlled environment).** Координата: верхний правый. Symbotic, Amazon Sparrow / Proteus, Locus Robotics — миллионы операций в сутки, L4 high autonomy.
- **Точка 2 — городское робот-такси (urban).** Координата: **верхний левый** — зона предупреждения. Открытая городская среда = низкая применимость; попытка высокой автономии при низкой применимости. Cruise (failed) — каноничная точка верхнего левого: расширил домен без проверки → отзыв лицензии → закрытие. Waymo (success в SF/Phoenix) держится за счёт **жёстко суженного narrow ODD** — это та же отрасль, но Waymo не тянется к автономии за пределами проверенного домена, поэтому её success-вариант сидит ближе к границе верхнего правого. Урок: разница между Cruise и Waymo — не «лучше технология», а **дисциплина ODD**; широкий домен в открытой среде = верхний левый = провал.
- **Точка 3 — чёрный лебедь (Suez Ever Given, Houthi crisis, COVID).** Координата: **нижний левый, near-origin** — низкая применимость + низкая автономия. Это L0: задача для людей и сценарного планирования, AI не помогает. Это **не warning-зона** (верхний левый — это попытка высокой автономии при низкой применимости); чёрный лебедь, наоборот, никто и не пытается автоматизировать — он сидит у начала координат как классика/человек. Аннотация: «out-of-distribution → классика и человек, не AI».

L13 — самая bimodal отрасль курса. **Одна и та же отрасль** держит сразу: L4 high autonomy успех (warehouse, верхний правый), провал расширения автономии в открытой среде (urban robotaxi, верхний левый) и фактический L0 для black swans (нижний левый, классика/человек). Три точки в трёх разных квадрантах — наглядная демонстрация, что зрелость AI **локальна по задаче**, а не глобальна по отрасли.

**Почему L13 особо важна для дидактики.** Логистика — наиболее **гетерогенная** отрасль курса. В одном и том же бизнесе (доставка товаров) присутствуют **четыре уровня среды** одновременно: склад (полностью контролируемая), магистральная фура (полуструктурированная), городское робот-такси / последняя миля (городская улица), и экстремальный кризис уровня Suez (out-of-distribution). Соответственно, **внутри одной компании** (FedEx, Amazon, X5 Retail Group) AI применяется на L4 high autonomy в одной зоне (warehouse robotics) и одновременно на L0 (полная зависимость от human dispatch) в другой (экстренное управление при сбое). Это противоречит интуиции «компания либо AI-зрелая, либо нет» — на самом деле зрелость **локальна по задачам**, не глобальна по компании.

**L14 — Telecom / cybersecurity.** Координата: **bimodal — высокая применимость на Sense, низкая на Act = вытянутая точка**.

- Sense (anomaly detection, telemetry analysis) — высокая применимость, но L1-L3 advisory + supervised = нижний правый (capped дисциплиной blast radius).
- Decide (RAG + HITL для analyst tier) — L1-L2, нижне-правая середина.
- Act (auto-block, auto-quarantine) — bounded by blast radius. CrowdStrike showed catastrophic L4 failure. По умолчанию — rule-based, не AI.

**L15 — Научные исследования.** Координата: **bimodal — closed-world high fit + open-world low fit**. *Главный кейс L15:* контраст **AlphaFold (Nobel 2024, Hassabis + Jumper) vs Galactica (Meta, retracted через 48 часов в ноябре 2022)**. AlphaFold работает потому, что protein folding — closed-world задача с PDB как ground truth + физическая модель структуры; Galactica провалилась потому, что «scientific text generation» — open-world задача без эталона (нет «true» научного результата для большинства гипотез до эксперимента). **Тот же класс моделей** (foundation models) с **разной physical groundedness** даёт диаметрально разные результаты.

- Closed-world (protein folding, drug-target search) — высокая применимость + L3-L4 autonomy (AlphaFold pipeline; ~200M predicted structures без human intervention).
- Open-world (hypothesis generation в novel domains) — низкая (Galactica retracted; citation hallucinations 2024-2025).
- Peer review augmentation — L1 advisory only (Elicit, Consensus, scite.ai — assistive, не replacement).
- Self-driving labs (Coscientist, ChemCrow) — closed-loop экспериментальные установки, прогрессивная парадигма в materials science.

**Главный урок L15 для capstone**: foundation models имеют **structural границу** в open-world science, не временное ограничение — нет эталона для hypothesis generation до experimental validation. Эта граница останется независимо от роста параметров модели.

**L16 — Нефтегаз.** Координата: **quadrant-dependent** по матрице 2×2 «data × process» (см. L16 keystone).

- Q1 (data ✓, process ✓) — predictive maintenance на оборудовании; Aramco; L2-L3.
- Q2 (data ✓, process ✗) — methane MRV; L1-L2.
- Q3 (data ✗, process ✓) — pre-salt drilling exploration; L0-L1.
- Q4 (data ✗, process ✗) — CCS / EGS; L0 (experimental).

**L16 anchor — Subsurface knowledge vault и pet-rock LLM.** В нефтегазе главный паттерн — physics-informed AI vs pure LLM. Один наглядный кейс — попытка построить «**pet-rock LLM-чатбот**» — chatbot для разведки субсёрфэйса (subsurface knowledge vault) на основе LLM без physical constraints — структурно проваливается, потому что LLM не имеет доступа к keystone уравнениям пористости / проницаемости / seismic interpretation и не способен генерировать физически осмысленные предсказания о породе. **Геолога эта система не заменит** — карбонатная фация требует знания диагенеза, sequence stratigraphy, well log calibration, которые LLM «не знает» в смысле inability to ground в physical model. **Урок переноса:** в любой регулируемой инженерной индустрии с physics-informed знанием (нефтегаз, авиакосмос, ядерная энергетика, фарма) generic LLM не заменяет physical/domain modeler — нужны PINNs (physics-informed neural networks) или hybrid физика+ML архитектуры. Это **уникальный урок L16**, не покрываемый general «matrix 2x2»: домен может казаться «data-rich» (миллиарды баррелей seismic surveys), но без physics-grounding это бесполезные tokens для LLM. AI-применения в нефтегазе — assistive (carbonate facies classification, well log denoising, document search), не autonomous decision.

После full reveal карта 16 отраслей содержит **примерно 20 точек** (multi-dot отрасли — L10 closed-loop / Monarch, L13 warehouse / robotaxi / черный лебедь, L15 closed / open, L16 4-quadrant matrix).

### §3.4 Cluster closed-loop

[for-slide-s23]

После full reveal карты можно выделить **три ключевых кластера**.

**Кластер 1 — Closed-loop квадрант (верхний правый).** Это **самый плотный** кластер карты.

Состав:
- L4 SE (engineering-agent на well-scoped tasks).
- L5 fraud detection (Stripe Radar, Visa AI).
- L10 See & Spray (chiseled CV).
- L13 warehouse robotics (Symbotic, Amazon Sparrow).
- L15 protein folding (AlphaFold).

**Что общего:**
1. Среда контролируемая или закрытая (критерий 1 ✓).
2. Ground truth быстрый и однозначный (критерий 5 ✓): compiler / chargeback / визуальная разметка / лабораторный анализ.
3. Объём задач большой (критерий 3 ✓).
4. Цена ошибки низкая или absorbable (критерий 4 ✓).
5. Распределение тренировочных данных совпадает с deployment (критерий 2 ✓).

**Это — work-cases**. Это там, где AI окупается, где он зрелый, где он не маркетинг. Студент должен запомнить **эти пять признаков** как профиль успешного применения. Когда вам встретится новая отрасль, и задачи в ней удовлетворяют всем пяти признакам — у проекта хорошие шансы.

**Подкластер: drug discovery в closed-loop.** AlphaFold и drug-target screening — высокая применимость; но в эту же отрасль входит open-world hypothesis (см. ниже). Bimodal nature.

### §3.5 Cluster open-environment

[for-slide-s24]

**Кластер 2 — Open-environment квадрант (верхний левый — зона предупреждения).** Это кластер **провалов**: низкая применимость × высокая (попытка) автономия.

Состав:
- L10 Monarch Tractor (open-field autonomous).
- L10 Plenty Vertical Farms ($940M+ raised; collapse → Chapter 11 март 2025).
- L13 urban robotaxi (Cruise failed).
- L5 iBuying (Zillow).
- L15 Galactica (open-world hypothesis).

**Важное разграничение — чёрный лебедь (Suez, COVID) сюда НЕ входит.** Верхний левый — это **попытка высокой автономии** при низкой применимости (low fit × attempted high autonomy). Чёрный лебедь, наоборот, сидит в **нижнем левом** near-origin: низкая применимость + низкая автономия, потому что никто и не пытается его автоматизировать — это задача для людей и сценарного планирования (классика/человек). Не смешивать: warning-зона = провал амбициозной автономии; near-origin = осознанный отказ от автономии. Обе зоны слева, но по разным причинам.

**Что общего (для верхне-левого кластера провалов):**
1. Среда открытая, имеется адверсариальность (критерий 1 ✗): погода, конкуренция, политика, биология.
2. Тренировочные данные не покрывают редкие события (критерий 2 ✗): black swans, edge cases.
3. Цена ошибки высокая (критерий 4 ✗): жизнь пешехода, банкротство компании, дезинформация в науке.
4. Эталон медленный или отсутствует (критерий 5 ✗): дефолт через месяцы, биологический результат через сезон.

**Что урок:** если ваша задача попадает в этот кластер, **не стартуйте полную автоматизацию**. Либо:
- Сузьте scope до narrow ODD (Cruise → Waymo подход).
- Перейдите на L1 advisory с человеком в петле.
- Откажитесь от AI; используйте классическую альтернативу.

Открытая среда — это **не недостаток технологии**; это **физика задачи**. Никакая модель 2026 года не закроет этот gap; никакая ожидаемая модель 2028 года тоже не закроет — потому что проблема не в модели, а в **распределении данных**.

### §3.6 Cluster high-stakes

[for-slide-s25]

**Кластер 3 — High-stakes high-fit (нижний правый — regulatory-capped).** Высокая применимость × низкая (регуляторно ограниченная) автономия.

Состав:
- L7 медицина (clinical decision capped at L1 by FDA).
- L9 авиакосмос (Act capped by LAWS regulation).
- L11 manufacturing safety-critical (capped by IEC 61508 SIL 2/3).
- L14 cyber Act-level (capped by blast radius discipline).
- L16 oil-gas ATEX Zone 0 (capped by hardware certification).

**Что общего:**
1. AI fit может быть высокий, но регуляторно ограничен.
2. Цена ошибки высокая (критерий 4 ✗): жизнь, инфраструктура, рынок.
3. Объясняемость обязательна (критерий 6 ✗).
4. Audit trail обязателен (критерий 6 ✗).

**Что урок:** в этих доменах автономия — **не цель**. Цель — **augmentation**. Радиолог с AI-помощником лучше радиолога без; но решение всегда за радиологом. F-35 пилот с AI ситуационной осведомлённости лучше пилота без; но trigger всегда за пилотом.

Это **дисциплина advisory**, и она не означает «AI хуже». Она означает «AI работает в роли advisory, и эта роль зрелая, измеримая, окупающаяся». Aidoc обрабатывает миллионы снимков в год в HITL режиме — это успех, не failure.

**Кросс-индустриальный паттерн high-stakes augmentation.** Все примеры этого кластера имеют общую структуру: AI как сенсор или усилитель для человека-эксперта, не замена. Радиолог + Aidoc; пилот + AI situational awareness; process operator + soft sensor; cyber аналитик + AI alerting. **Augmentation, не replacement** — дисциплина, которую регулятор активно поощряет. Финансовая выгода augmentation обычно **больше**, чем для full automation, потому что full automation редко достигается в high-stakes (regulator + technology gaps), а попытки часто проваливаются (IBM Watson Health). Большая часть value AI в high-stakes идёт от augmentation. Stakeholder management: ваша роль — переводчик между entusiasm менеджмента (хотят automation) и осторожностью regulator (хотят HITL); hard skills курса дают обоснование, soft skills (§5.5) — способ доставки.

### §3.7 Пустые квадранты

[for-slide-s26]

На 2D-карте два внедиагональных квадранта несут особую дидактическую нагрузку: один **пустой и опасный**, другой — **заполнен, но с потолком**. Их асимметрия — **дидактический сигнал**.

**Верхний-левый квадрант** (низкая применимость ИИ + высокая автономия). Это **пустой и опасный квадрант**, **зона предупреждения**. Если ваша задача оказывается здесь — STOP.

Что находится в этом квадранте:
- **CrowdStrike Falcon BSOD** — Act-уровень автономии (L4) для классической EDR-системы (применимость средняя, не высокая); blast radius огромный.
- **F-35 ALIS** — predictive maintenance с высокой автономией на mission-critical (cost-of-error высокая); Act-функции пришлось урезать.
- **Cruise urban robotaxi expansion** — L3-L4 autonomy в open environment, applicability была не подтверждена.

**Урок пустого верхне-левого квадранта:** если применимость не высокая, **не стремитесь к высокой автономии**. Это асимметрия: low fit × high autonomy = катастрофа. Lower fit + lower autonomy (классический алгоритм + HITL) — приемлемое решение.

**Нижний-правый квадрант** (высокая применимость ИИ + низкая автономия). Этот квадрант **заполнен**. Это места, где применимость высокая, но автономия искусственно низкая — Aidoc, Project Maven, financial scoring под EU AI Act находятся здесь. **Это не пустой, это capped квадрант** — потолок задан регулятором, не технологией.

**Студент должен научиться** диагностировать собственные проекты по принципу: «попадаю ли я в верхне-левый? если да — что я могу изменить, чтобы сдвинуться?» Варианты сдвига:
- Сдвинуться **вправо** — повысить applicability (закрыть среду, набрать больше данных, улучшить ground truth). Это инвестиция в **постановку задачи**.
- Сдвинуться **вниз** — снизить автономию (HOOL → HITL → advisory). Это инвестиция в **дизайн системы**. Так проект переходит из верхне-левого в нижне-левый — классический алгоритм с человеком в петле.

Оба сдвига валидные: вправо — в зрелый closed-loop (верхний правый); вниз — в безопасный classical / non-AI (нижний левый). Невалиден лишь один маршрут — **оставаться в верхне-левом**, наращивая автономию без роста применимости.

---


**Конец Части 3.** Продолжение — `chapter-part3b.md` (Раздел 4. Топ-12 провалов).

### Self-check вопросы (Часть 3)

1. Назовите 3-4 отрасли из карты 16, попадающие в **closed-loop квадрант** (верхний правый). Что у них общего по пяти признакам?
2. Что находится в **верхне-левом квадранте**? Почему он должен оставаться пустым? Назовите 2 канонических провала, попавших в него. Чем он отличается от **нижне-правого** (capped) квадранта?
3. В чём bimodal nature L13 (логистика)? Три точки на карте — какие, и где они расположены?
4. Каковы координаты L6 (CAD/CAM), L11 (manufacturing), L15 (наука), L16 (нефтегаз) на 2D-карте? Назовите главный кейс каждой отрасли.
5. Что такое L16 «pet-rock LLM» anchor? Какой урок переноса он даёт для других регулируемых инженерных индустрий?

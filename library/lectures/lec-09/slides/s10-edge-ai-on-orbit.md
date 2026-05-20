---
id: s10
type: assertion_visual
duration_min: 2
assertion: "Edge AI on-orbit: ML прямо на спутнике вместо передачи сырого сигнала. ESA Φ-sat-2 — remote-upgradable модели."
learning_goal: "On-orbit edge ML как separate класс задач; demonstrator → production"
learning_outcomes: [LO1a]
chapter_ref: "§1.3 — SAR и edge-AI на орбите"
references: [esa-2024-phi-sat-2, planetek-2025, slingshot-2025-talos]
visual:
  pattern: matrix
  primary: "4 категории edge-AI: Demonstrators / Production / SDA / Commercial"
---

# Edge AI on-orbit — ML на спутнике, не на земле

## Assertion

Edge AI on-orbit: ML прямо на спутнике вместо передачи сырого сигнала. ESA Φ-sat-2 — remote-upgradable модели.

## Visual

Сверху — assertion 28pt bold + один уточняющий sub-bullet 16pt italic: «Цель — снизить латентность и ширину канала. Вместо мегабайтов сырого изображения — килобайт сводки».

Под ней — 2×2 сетка карточек Ocean rounded box, каждая с small heading 18pt + 2-3 строки текста 14pt + иконка 48px Lucide Primary mid в углу:

**1. Demonstrators** (icon `flask-conical`)
- ESA Φ-sat-2 (август 2024) — remote-upgradable модели
- Planetek AI-eXpress 1+ (ноябрь 2025) — Jetson Orin NX

**2. Production telemetry** (icon `activity`)
- Lockheed Pony Express 2 + T-TAURI
- Onboard ML для аномалий телеметрии

**3. SDA tracking** (icon `radar`)
- Slingshot Agatha + TALOS — июль 2025
- 204 сенсора · 21 локация · 5 континентов

**4. Commercial archive** (icon `database`)
- TerraTech / Роскосмос
- Гражданская onboard-классификация

Внизу — caption 12pt italic: «Adoption: от "AI-derived detection in hours" к "predictive intelligence before event". Сценарий 2026-2028».

## Speaker notes

Параллельно с большой коммерческой аналитикой развивается отдельная линия — edge AI on-orbit. Это ML-вычисления прямо на спутнике, без передачи сырого сигнала на землю. Цель — снизить латентность и ширину канала: вместо мегабайтов сырого изображения передаётся килобайт сводки «вот тут изменение».

Программы 2024-2026 года группируются по типу миссии в четыре категории.

Первая — демонстраторы. ESA Φ-sat-2, запущенный в августе 2024 — это европейский demonstration satellite с remote-upgradable ML-моделями. После запуска модель можно дообучить и заменить новым весом по телекомандам, без замены оборудования. AI-eXpress 1+ от Planetek Italia, ноябрь 2025 — серия европейских edge-computing спутников на NVIDIA Jetson Orin NX, выводящих ML-инференс на орбитальный уровень. Это лаборатории на орбите: цель — отработать, что вообще можно делать ML-моделью прямо на спутнике.

Вторая категория — production telemetry. Lockheed Pony Express 2 + T-TAURI — это американский военный production-аналог: onboard ML для обнаружения аномалий в телеметрии. Это уже не demo, это инфраструктура для разведывательных программ США.

Третья — SDA tracking. SDA — Space Domain Awareness, обзор космической обстановки. Slingshot Aerospace Agatha + TALOS — 204 сенсора в 21 локации на 5 континентах плюс ML-«отпечатки» спутников по фотометрическому паттерну. Это не ISR в смысле наблюдения за землёй, это наблюдение за самим космосом — отслеживание спутников, обломков, потенциально враждебных rendezvous.

Четвёртая — commercial archive. TerraTech от Роскосмоса — гражданская коммерческая edge-аналитика для аграрного и инфраструктурного мониторинга, частично с onboard-классификацией.

Adoption-направление по Sense — растёт быстро. Сценарий 2026-2028: от «AI-derived detection in hours» к «predictive intelligence before event».

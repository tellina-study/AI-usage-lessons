---
id: s28
type: assertion_visual
duration_min: 2.5
assertion: "Geran-2 evolution — NVIDIA Jetson onboard (wreckage); Alabuga ~2 700-3 000/мес. Cognitive Pilot — российский civilian dual-use (СберАгро, КАМАЗ)."
learning_goal: "Russian Act: defense (Geran-2) + civilian dual-use (Cognitive Pilot); supply chain caveat"
learning_outcomes: [LO1a]
chapter_ref: "§3.2 — Geran-2 + Cognitive Pilot"
references: [csis-2026-bondar, autonomy-2025-geran, toms-2024-shreya, cognitive-pilot-2025]
visual:
  pattern: matrix
  primary: "2 cards: Geran-2 (defense) + Cognitive Pilot (civilian)"
---

# Russian Act — defense (Geran-2) + civilian dual-use (Cognitive Pilot)

## Assertion

Geran-2 evolution — NVIDIA Jetson onboard (wreckage); Alabuga ~2 700-3 000/мес. Cognitive Pilot — российский civilian dual-use (СберАгро, КАМАЗ).

## Visual

Под assertion — 2 равные cards в Ocean rounded box.

**Слева — Geran-2 evolution** (Primary mid heading):
- Иконка `plane-off` 48px (drone-stylized)
- Production stats:
  - **Алабуга ОЭЗ** · производство в Татарстане
  - **~2 700-3 000 / месяц** к концу 2025 (gold, with `[VFY]` mark)
  - **>26 000 произведено** к поздней весне 2025
  - План **>40 000** к концу 2025 `[VFY]`
- AI-evolution stack:
  - **NVIDIA Jetson** onboard (wreckage analysis)
  - High-res cameras + thermal
  - FPGA для EW-resistance
  - 2026 — anti-radiation seeker variant
- Caveat (Teal-tint, 12pt italic): «Wreckage подтверждает onboard ML; РОЛЬ autonomous decision quality vs operator override — unclear. Большая часть strikes — operator-guided + GPS»
- **Supply-chain caveat** (red-warn underline): «1 111 Dell PowerEdge XE9680 серверов через Shreya Life Sciences (India) → Russia, апрель-август 2024»

**Справа — Cognitive Pilot** (Primary mid heading, civilian dual-use balance):
- Иконка `truck` 48px Primary mid
- Stack: компьютерное зрение + радар + LiDAR (без GNSS!)
- Параметры:
  - Joint venture **Сбер + Cognitive Technologies** (Москва)
  - Применения:
    - КАМАЗ-комбайны, тракторы СберАгро
    - Городской транспорт
    - Железная дорога
    - Снегоуборочная техника
  - План: **до 50 000 систем/год** (gold)
- Cross-ref 12pt italic: «Те же CV+LiDAR-стеки в CAD/CAM (Лекция 6) и в промышленной автоматизации (Лекция 14). Навыки переносимы»
- Status 14pt italic: «НЕ identified as defense supplier в открытых источниках»

Source 12pt italic: «CSIS Bondar 2026 · Tom's Hardware 2024 · Fortune 2026 · TASS 2024».

## Speaker notes

Российская сторона Act — два кейса разной природы.

Первый — Geran-2 evolution. Geran-2 — это российская модификация иранского Shahed-136, производится на Алабугской ОЭЗ. К концу 2025 года производительность — около 2 700-3 000 дронов в месяц с план-capacity 5 000 плюс. Общий объём произведённого — более 26 тысяч к поздней весне 2025 года, план — более 40 тысяч к концу 2025 года. Эти цифры — `[VFY-day-of]`, требуют верификации на день лекции; диапазон оценок широкий.

AI-эволюция Geran-2. Анализ обломков — украинское восстановление — показывает наличие NVIDIA Jetson onboard, high-res камеры, тепловизионные модули, FPGA для EW-resistance. В 2026 году появился вариант с anti-radiation seeker.

Caveat по «автономии». Wreckage-анализ подтверждает onboard ML-компоненты. Но реальная роль autonomous decision quality vs operator override — unclear. Большая часть strikes остаётся operator-guided плюс GPS-guided; «autonomy» в смысле «решает сама от целеуказания до удара» — overstated.

Supply-chain caверз. Российский AI-defense критически зависим от продолжающейся возможности обхода санкций. Документировано: 1 111 серверов Dell PowerEdge XE9680 — с продвинутыми GPU внутри — shipped через индийскую Shreya Life Sciences в Россию в апреле-августе 2024 года. Это и риск для адверсаров — свои чипы оказываются в чужих weapons, — и инженерный урок: hardware supply-chain — это strategic risk, который не закрывается софтом.

Второй кейс — Cognitive Pilot. Чтобы российский слой не был только военным, дадим один гражданский аналог. Cognitive Pilot — совместное предприятие Сбера и Cognitive Technologies, Москва, — основные направления: автономные системы для сельскохозяйственной техники, КАМАЗ-комбайнов, тракторов СберАгро, городского транспорта, железной дороги, снегоуборочной техники. Stack — компьютерное зрение плюс радарные сенсоры плюс LiDAR для автономии без GNSS. Планы — до 50 тысяч систем в год.

Cognitive Pilot не идентифицирован как defense supplier в открытых источниках. Это civilian-side analogue Geran-2 autonomy: тот же сенсорный стек, те же ML-pipelines, но применённый к гражданскому транспорту. Это dual-use balance для нашей лекции: показать, что российский AI не сводится к военному.

Связь с Лекциями 6 и 14. Те же стеки CV плюс LiDAR работают в CAD/CAM и в промышленной автоматизации. Если студент идёт в гражданскую инженерию — навыки переносимы между секторами.

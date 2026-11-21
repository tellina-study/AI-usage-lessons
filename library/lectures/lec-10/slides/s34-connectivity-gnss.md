---
id: s34
type: failure_case_environmental
duration_min: 2.2
assertion: "18% американских ферм без интернета в принципе. 123 000 авиа-рейсов с GNSS-interference Q1 2025 (Финляндия unfarmable). Starlink в РФ запрет апрель 2026. AP5 — cloud-first для off-grid = архитектурная ошибка. Альтернатива: edge ML / TinyML."
learning_goal: "AP5 + edge ML как реалистичная архитектура"
learning_outcomes: [LO5]
chapter_ref: "§5.1 Часть 3 — Связь"
references: [icao-2025-gnss, stanford-itm-2025, broadband-now-2024]
visual:
  pattern: 3numbers_map
  primary: "3 крупные цифры (18% / 123k / Starlink ban) + GNSS-jamming Финляндия карта (Stanford ITM 2025 figure)"
---

# Связь — 18% ферм без интернета + GNSS-jamming

## Assertion

18% американских ферм без интернета в принципе. 123 000 авиа-рейсов с GNSS-interference Q1 2025 (Финляндия unfarmable). Starlink в РФ запрет апрель 2026. AP5 — cloud-first для off-grid = архитектурная ошибка. Альтернатива: edge ML / TinyML.

## Visual

Двухколоночный layout.

**Левая колонка (45%) — 3 крупные цифры в Ocean rounded boxes (gold accent на главной):**

1. **18% американских ферм без интернета** ★ gold (BroadbandNow / Feedstuffs 2024)
   - 39% сельского населения без широкополосного (vs 4% городского)
   - 40% fixed-line; 42% на cellular/satellite (нестабильно)

2. **123 000 авиа-рейсов с GNSS-interference Q1 2025** (ICAO 2025)
   - Источники: российские EW-станции (побочный эффект военных операций)
   - Финляндия unfarmable: «areas of farms reportedly unfarmable using GNSS-based tractors and combines»
   - ICAO Assembly октябрь 2025 формально осудил Россию

3. **Starlink в РФ запрет апрель 2026** (6 месяцев)
   - Single-vendor connectivity = single point of failure
   - Илон Маск 2022 — одностороннее прекращение Starlink для Украины как прецедент

**Правая колонка (55%) — Map / figure + альтернатива:**

Сверху — GNSS-jamming Финляндия map / figure из Stanford GPS Lab ITM 2025 paper в Ocean rounded box. Caption 12pt italic: «Stanford GPS Lab ITM 2025 — ADS-B / LCM detection технология».

Под map — callout в Teal-tint box:
- **AP5. Cloud-first для off-grid farm = архитектурная ошибка.**
- **Альтернатива: edge-AI / TinyML / offline-first**
  - Модели — мегабайты вместо гигабайт
  - Compute — микроконтроллер (ESP32, STM32) или edge-GPU (Jetson Orin Nano)
  - Hybrid: cellular + LoRa + Starlink + RTK ground link для redundancy
- **Не «AI попроще»** — другой класс архитектуры под ограничения среды

Bottom callout 14pt italic: «**Прецизионное земледелие — гражданская жертва военной радиоэлектроники.** Авторулевой, переменная норма высева — все полностью зависят от GNSS».

Footer 12pt italic: «Источники: ICAO 2025 (отчёт CH/FI/EE/LT/LV/PL); Stanford GPS Lab ITM 2025; BroadbandNow / Feedstuffs 2024».

## Speaker notes

Первое условие среды — связь. AgTech-маркетинг 2018-2023 годов опирался на сценарий «cloud-AI оптимизирует трактор в реальном времени через постоянный uplink» — фантазия для большинства farms, и три цифры показывают, почему.

Первая цифра — восемнадцать процентов американских ферм без интернета в принципе (BroadbandNow / Feedstuffs). Сорок процентов имеют fixed-line подключение — DSL, cable, fiber; остальные сорок два процента — на нестабильном cellular или satellite. Тридцать девять процентов сельского населения США без широкополосного доступа против четырёх процентов городского. Развёртывание broadband на farmland дало бы экономике около шестидесяти пяти миллиардов в год через прирост yields при стоимости тридцать пять-сорок миллиардов — это публичная оценка, не реализованный план. Cloud-first AI для сельского хозяйства — архитектурная ошибка для большинства farms.

Вторая цифра — GNSS-jamming. По отчёту ICAO (Швейцария, Финляндия, Эстония, Литва, Латвия, Польша, 2025) — почти сто двадцать три тысячи авиа-рейсов с GNSS-interference за первые четыре месяца 2025 года; ICAO Assembly в октябре 2025-го формально осудил Россию за нарушение GNSS гражданской авиации. С 2022 года российские системы РЭБ, направленные на Украину, глушат GNSS на территориях Финляндии, Эстонии, Латвии, Литвы — Stanford GPS Lab исследует технологию детектирования источников глушения. Финские фермеры сообщают: areas of farms reportedly unfarmable using GNSS-based tractors and combines because of the interference from Russian EW installations. Прецизионное земледелие — гражданская жертва военной радиоэлектроники: авторулевой и переменная норма высева/опрыскивания полностью зависят от GNSS и без него превращаются в обычный трактор.

Третья цифра — Starlink как решение и новая зависимость. Starlink — де-факто backbone для рассредоточенных ферм и для Африки: девяносто долларов в месяц в режиме «excess capacity», сто двадцать — «limited»; reliability страдает от снега, дождя, физических obstructions. В России Starlink запрещён с тридцатого апреля 2026 года на шесть месяцев — закрыт один из вариантов redundancy для российских хозяйств. Single-vendor connectivity — single point of failure: Илон Маск уже останавливал Starlink для Украины в одностороннем порядке в критический момент 2022 года, и та же логика применима к фермеру в любой юрисдикции.

Главный анти-ИИ критерий — AP-пять: cloud-first для off-grid farm — архитектурная ошибка. Альтернатива — edge-AI и TinyML: машинное обучение на устройстве (датчик, гейтвей, кабина трактора, ошейник коровы) без cloud-uplink — модели мегабайты вместо гигабайт, вычисления на микроконтроллере или edge-GPU вместо облачных GPU. Hybrid-архитектура — cellular плюс LoRa плюс Starlink плюс RTK ground link с redundancy для critical operations. Это не «AI попроще», а другой класс архитектуры, спроектированный под ограничения среды с самого начала.

## Источники

- ICAO (2025) — GNSS-interference report (CH/FI/EE/LT/LV/PL).
- Stanford GPS Lab (ITM 2025) — Russia GNSS Spoofing detection.
- BroadbandNow / Feedstuffs (2024) — 18% farms без интернета.

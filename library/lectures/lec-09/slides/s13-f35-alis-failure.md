---
id: s13
type: assertion_visual
duration_min: 3
assertion: "F-35 ALIS нарушил все три условия predictive maintenance — и был списан в июне 2024. Урок номер один для инженера."
learning_goal: "Канонический failure-кейс Sense: 3 условия predictive maintenance + cost-per-flight-hour"
learning_outcomes: [LO1b, LO3]
chapter_ref: "§1.6 — Провал F-35 ALIS"
references: [gao-20-316, gao-22-105128, asf-2024-odin]
visual:
  pattern: matrix
  primary: "3 condition cards с × маркерами + QuickChart cost bar"
---

# F-35 ALIS — predictive maintenance, нарушенное по всем трём осям

## Assertion

F-35 ALIS нарушил все три условия predictive maintenance — и был списан в июне 2024. Урок номер один для инженера.

## Visual

Сверху — assertion 28pt bold. Под ней — 2 зоны.

Слева (55%) — 3 condition card в Ocean rounded box, каждая с заголовком и × маркером:

**1. Быстрый feedback loop ✗**
- Drift в данных детектируется в годы, не дни
- Модель устаревает раньше, чем ошибки видны

**2. Доступная ground truth ✗**
- Нет способа верифицировать каждый alert
- Ложные тревоги накапливаются → доверие падает

**3. FP-cost ≤ FN-cost ✗**
- Adversarial UX — персонал обходит через Excel
- High false-positive — экипаж тратит время на инспекции

Каждая ✗ в gold-warning круге (RED_WARN или GOLD).

Справа (45%) — QuickChart horizontal bar в Ocean rounded box: «Cost-per-flight-hour, USD» — F-35: $42-44k (gold-warning); F-22 Raptor: ~$70k (baseline grey). Sub-caption: «F-35 дороже более сложного F-22 — индикатор системной проблемы».

Внизу — резюмирующий callout 14pt bold в Teal-tint боксе: «ODIN строится в явной осведомлённости об этом нарушении: меньший охват, government-owned, явный HITL для flight-authorisation, disconnected mode».

Source footer 12pt italic: «GAO-20-316, GAO-22-105128, Air & Space Forces 2024».

## Speaker notes

F-35 ALIS — система предиктивного обслуживания истребителя F-35, развёрнутая Lockheed Martin для тысяч единиц самолёта по всему миру. К концу 2010-х годов ALIS превратился в источник постоянных проблем.

Первое — высокая ложноположительная активность. ALIS помечал самолёт как «no-fly» в случаях, когда никакой реальной проблемы не было; экипаж тратил время на ручные инспекции, чтобы убедиться, что самолёт исправен. Второе — неточные и неполные данные. GAO, US Government Accountability Office, в отчёте 2020 года прямо сообщал: «Inaccurate and missing data have at times resulted in the system signalling that an F-35 should not be flown — even though aircraft had no issues». Третье — adversarial UX. Пользоваться ALIS было настолько сложно, что персонал систематически обходил систему, делая параллельный учёт в Excel и других инструментах. Четвёртое — cost-per-flight-hour. К пику проблем стоимость лётного часа F-35 составляла 42-44 тысячи долларов — выше, чем у F-22 Raptor, более сложного и старого самолёта.

Финальная версия ALIS была выпущена в июне 2024 года, после чего начался поэтапный переход на новую систему ODIN — Operational Data Integrated Network. ODIN — government-owned, меньший по охвату, с явно отделённой логикой flight-clearance authority — то есть решение «можно ли летать» отделено от predictive analytics, — с поддержкой disconnected mode.

Урок номер один для инженера. Predictive maintenance в безопасностно-критичной области работает только при выполнении одновременно трёх условий: быстрый feedback loop, доступная ground truth, FP-cost меньше или равна FN-cost. ALIS нарушил все три условия. ODIN строится в явной осведомлённости об этом нарушении.

Урок номер два. Это не только про F-35. Тот же триплет применим к любой predictive-системе в инженерной практике — от мониторинга турбин до диагностики промышленных линий. Этот разбор будет работать дальше в курсе как cross-cutting шаблон.

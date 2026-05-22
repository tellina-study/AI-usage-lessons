---
id: s19
type: assertion_visual
duration_min: 2
assertion: "Из 30+ серьёзных AV-стартапов 2015-2020 выжили 3-4: Waymo, Aurora, Mobileye (eyes-off L3), Apollo Go в Китае."
learning_goal: "Survivor pattern + сравнение dropouts vs survivors"
learning_outcomes: [LO2]
chapter_ref: "§2.6 — Серия банкротств + выжившие"
failure_bucket: strict_in
references: []
visual:
  pattern: schema_matrix_survivors_dropouts
  primary: "Двухколонная матрица: survivors vs dropouts. Каждая строка — компания + почему survived/failed"
  acquisition_tiers: []
---

# Survivors vs dropouts: 10-к-1 consolidation

## Survivors (3-4 компании)

- **Waymo (Alphabet).** Crawl-walk-run, narrow ODD expansion (Phoenix → SF → LA → ATX), HD-карта + лидар + камеры + удалённые операторы. Patient capital Alphabet.
- **Aurora Innovation.** Crawl-walk-run, one route at a time (Dallas-Houston), driverless commercial май 2025, не overpromise. Public market funding через SPAC.
- **Mobileye.** Camera-first ADAS-стек, потребительская модель (миллион vehicles), spin-off из Intel.
- **Apollo Go (Baidu).** Государственная поддержка Китая, 240M км глобально, 17M+ orders, 22 города.

## Dropouts (>15 компаний)

- **Argo AI.** $7B сгорело за 5 лет. Ford + VW pull funding одновременно.
- **Cruise (GM).** $10B → 0 за 8 лет. October 2023 dragging incident + DMV trust violation.
- **TuSimple.** Delisting + китайский asset transfer + US-China tension.
- **Embark.** SPAC bust 16 месяцев от IPO.
- **Waymo Via.** Alphabet закрыла собственное trucking-направление.
- **Starsky.** Первая волна 2020, sim-to-real гэп.
- **Zoox.** Куплена Amazon 2020 (не банкрот, но прекратила независимое развитие).
- **Locomation.** Закрыта 2024.
- **Plus.ai.** Pivot на supervised L2+ через OEM каналы (Volvo / Daimler).

## Survivor pattern

- **Crawl-walk-run.** Многолетние safety-operator тесты до driverless commercial.
- **Narrow ODD.** Один маршрут или один город, не «робот везде».
- **Не overpromise.** Не «replacing X% drivers» / «1M robotaxi by 2024».
- **Patient capital.** Alphabet / Intel / Baidu — корпоративный, не startup VC short timeline.
- **Уважение к среде.** ODD дисциплина — главная.

## Speaker notes

Здесь я хочу подытожить два слайда подряд про non-survivors одной мыслью — что отличало выживших от не выживших.

Survivors. Waymo. Aurora. Mobileye. Apollo Go в Китае. Это три-четыре компании из более чем тридцати серьёзных AV-стартапов 2015-2020 годов.

Что Waymo делает правильно. Crawl-walk-run. Они начали в Фениксе с одним городом, потом расширили в Сан-Франциско, потом Лос-Анджелес, потом Остин и так далее. Каждое расширение — отдельный отработанный ODD. HD-карта плюс лидар плюс камеры плюс удалённые операторы — full stack без compromises. Patient capital Alphabet — Alphabet не торопит Waymo на квартальный profit.

Aurora — то же самое. Один маршрут Даллас-Хьюстон, отработанный годами, потом driverless commercial май 2025. Не «replacing all truckers by 2025». Не «1000 trucks deployed». Десять машин на одном маршруте. Crawl-walk-run.

Mobileye — другая ставка, потребительская модель. Camera-first ADAS-стек на миллион потребительских машин, потом L3 eyes-off на premium-OEM. Аккуратное движение по уровням SAE.

Apollo Go — это китайская модель с государственной поддержкой. Двести сорок миллионов километров автономного движения глобально, семнадцать миллионов заказов, двадцать два города.

Dropouts. Argo и Cruise — обе уперлись в одну проблему: capital intensity без revenue. Семь миллиардов и десять миллиардов соответственно. TuSimple — US-China геополитика плюс sim-to-real. Embark — SPAC bust. Waymo Via — даже бесконечный capital Alphabet не нашёл profitable model. Starsky — первая волна.

Survivor pattern — это пять признаков. Crawl-walk-run. Narrow ODD. Не overpromise. Patient capital. Уважение к среде.

Это важный инженерный lesson. Survivor pattern — не алгоритмическое превосходство. Все survivors используют похожие сенсорные стеки и похожие ML-подходы. Survivor pattern — это дисциплина ODD plus business model дисциплина plus культурная установка инженерного смирения.

Cruise vs Waymo. Обоим тот же стек. Но Waymo выжил, потому что cautious в ODD expansion. Cruise разорилась, потому что нарушила собственные правила прозрачности с регулятором и одно нарушение ODD-дисциплины уничтожило восемь лет работы за двенадцать недель.

Lesson — это lesson инженерного смирения, не arrogance.

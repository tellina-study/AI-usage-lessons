---
id: s24
type: assertion_visual
duration_min: 2.5
assertion: "Waymo март 2026: 500 000 поездок в неделю, 3 067 машин 5-го поколения, 10+ городов. HD-карта + лидар + удалённые операторы + формальное обоснование безопасности."
learning_goal: "Waymo как canonical survivor robotaxi"
learning_outcomes: [LO1]
chapter_ref: "§3.1 — Waymo deep-dive"
references: [techcrunch-waymo-march-2026, eweek-waymo-14m, carbon-credits-waymo]
visual:
  pattern: case_study_hero_with_stack
  primary: "Hero photo: Waymo Jaguar I-Pace в SF. Справа: stack-схема стека (HD-map + LiDAR + cameras + radar + remote ops)"
  acquisition_tiers:
    - "Tier 2: Wikipedia Commons «Waymo»"
    - "Tier 3: Waymo press kit"
    - "Tier 4: Waymo YouTube"
---

# Waymo — canonical survivor robotaxi

## Цифры март 2026

- **500 000 платных поездок в неделю** — март 2026.
- **3 067 машин 5-го поколения** — по NHTSA disclosure декабря 2025.
- **10+ городов:** Phoenix, San Francisco, Los Angeles, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando.
- **14 миллионов поездок кумулятивно** за 2025 год.
- **Рост в 10× за 19 месяцев** (с 50K rides/неделю в мае 2024).

## Стек

- **HD-карта** — детальная карта дорожного окружения с точностью ~10 см.
- **LiDAR** — основной 3D-сенсор.
- **Камеры** — RGB perception.
- **Радар** — secondary sensor для weather robustness.
- **Удалённые операторы** — human override в edge-cases (не «driving», а assistance).
- **Формальное обоснование безопасности** — formal safety case, регуляторно проверяемый документ.

## Что Waymo НЕ публикует

- **Прибыльность на одну поездку.** Компания не отчитывается публично — означает либо «still negative», либо «not disclosed for competitive reasons». Любой sceptic считает первое.

## Survivor pattern

- **Crawl-walk-run** — начали в Phoenix, потом SF, потом LA, потом каждый новый город — отдельный отработанный ODD.
- **Patient capital Alphabet.**
- **Narrow ODD expansion** — каждое новое lane требует extensive валидации.
- **Не overpromise** — никаких «1M robotaxi by 2024».

## Speaker notes

Waymo — это canonical survivor robotaxi на 2026 год. Я хочу остановиться на цифрах и стеке, потому что это компания, которая работает.

Цифры на март 2026. Пятьсот тысяч платных поездок в неделю. Три тысячи шестьдесят семь машин пятого поколения, по NHTSA disclosure декабря 2025. Десять+ городов: Phoenix, San Francisco, Los Angeles, Austin, Atlanta, Miami, Dallas, Houston, San Antonio, Orlando. Кумулятивно за 2025 год — четырнадцать миллионов поездок.

И рост — в десять раз за девятнадцать месяцев. Май 2024 года — пятьдесят тысяч поездок в неделю. Декабрь 2025 — четыреста пятьдесят тысяч. Март 2026 — около пятисот тысяч. Это серьёзный коммерческий scale.

Стек Waymo — full-sensor approach без compromises. HD-карта с точностью около десяти сантиметров — это означает, что Waymo заранее знает геометрию каждой улицы, каждой разметки, каждого светофора. LiDAR — основной 3D-сенсор. Камеры — RGB perception. Радар — secondary sensor для weather robustness. И удалённые операторы — human override в edge-cases. Важно: удалённые операторы не «driving» машину дистанционно, а assistance — даёт advice в сложных ситуациях, машина сама исполняет.

И ещё — формальное обоснование безопасности, formal safety case. Это регуляторно проверяемый документ, который Waymo публикует периодически. Это часть культуры компании — engineering rigour, не PR.

Что Waymo не публикует. Прибыльность на одну поездку. Компания не отчитывается публично. Это означает либо «still negative», либо «not disclosed for competitive reasons». Любой sceptic считает первое — что Waymo на 2026 год всё ещё имеет negative unit economics. Это важно держать в голове, потому что operational scale Waymo впечатляющий, но unit economics ещё не доказана.

Survivor pattern Waymo — это пять признаков. Crawl-walk-run — начали в Phoenix, потом SF, потом LA, потом каждый новый город — отдельный отработанный ODD. Patient capital Alphabet — Alphabet не торопит Waymo на квартальный profit. Narrow ODD expansion — каждое новое lane или новый город требует extensive валидации. Не overpromise — никаких «один миллион robotaxi by 2024», никаких «replacing all taxi drivers». И уважение к среде — городская улица хрупкая, и Waymo это понимает.

Pedagogical point. Waymo выжил по тем же причинам, по которым Aurora выжила в trucking — crawl-walk-run, narrow ODD, не overpromise, patient capital. Это не алгоритмическое превосходство. Cruise использовал похожий стек, но нарушила ODD-дисциплину и обанкротилась.

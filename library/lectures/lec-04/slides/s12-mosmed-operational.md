---
id: s12
type: assertion_visual
duration_min: 3
assertion: "mosmed.ai — конкретный пример сбывшегося обещания: 5 лет production, 14M+ исследований, 74 региона, 70 AI-сервисов."
learning_goal: "Российский operational case — federated AI-platform"
learning_outcomes: [LO1, LO2]
frame_mapping: ["Другой AI", "Безопасность", "Человек vs AI"]
chapter_ref: "§2.4 — Российский кейс: mosmed.ai"
references: [mos-ru-2025, remedium-2025, healthcare-me-2026, webiomed-2026]
visual:
  pattern: pipeline
  primary: "Mini-pipeline (Снимок → mosmed.ai cloud → AI-анализ → врач) сверху + 6 info-cards с verified operational metrics снизу"
  illustration:
    type: official_product
    sources:
      - "mosmed.ai operational dashboard — https://mosmed.ai/ (screenshot operational page, no financial figures)"
      - "Mos.ru AI Leaders Award — https://www.mos.ru/en/news/item/147773073/"
      - "Remedium 5-year stats — https://remedium.ru/news/za-pyat-let-ii-proanaliziroval/"
      - "Healthcare ME 2026 — https://www.healthcaremea.com/2026/03/18/moscow-deploys-ai-across-the-healthcare-system-with-over-60-diagnostic-services/"
    caption: "mosmed.ai operational dashboard (mos.ru, Remedium 2025-2026)"
interaction: none
---

# mosmed.ai — обещание сбылось в operational форме

## Assertion

mosmed.ai — конкретный пример сбывшегося обещания: 5 лет production, 14M+ исследований, 74 региона, 70 AI-сервисов.

## Visual

Сверху mini-pipeline 4-stage (≈40% высоты): «Снимок (КТ/МРТ/рентген)» → «mosmed.ai cloud» → «AI-анализ (70 сервисов)» → «Результат врачу + 2nd opinion», соединённые MSO_SHAPE.RIGHT_ARROW в Ocean palette. Снизу 6 info-cards в Ocean rounded box, расположены в 2 ряда по 3: `14M+ исследований` (за 5 лет), `2000+ медорганизаций`, `74 региона РФ`, `18M+ изображений processed`, `70 AI-сервисов на 43 областях`, `11 нац. стандартов; 300+ datasets`. **Gold highlight** на «14M+» (главное число). Сверху ассертион 24pt; справа — small screenshot mosmed.ai dashboard.

## Speaker notes

Концентрированный пример того, как AI-диагностическое обещание сбылось в operational форме, — московская платформа mosmed.ai. Эксперимент по применению искусственного интеллекта в лучевой диагностике начат в Москве в ноябре 2019 года как городской проект Департамента здравоохранения Москвы и НПКЦ диагностики и телемедицины. В мае 2024 года проект запущен на федеральном уровне как MosMedAI.

К концу 2025 — началу 2026 годов операционные метрики платформы складываются в production-картину. За пять лет работы AI проанализировал более четырнадцати миллионов исследований. К платформе подключено более двух тысяч медицинских организаций в семидесяти четырёх регионах России. Обработано более восемнадцати миллионов медицинских изображений, развёрнуто около семидесяти AI-сервисов на сорока трёх клинических областях — от рентгенографии грудной клетки и КТ лёгких (включая COVID-релевантные сервисы 2020–2022 годов) до маммографии, остеоденситометрии и КТ головного мозга. На основе опыта проекта разработано одиннадцать национальных стандартов и около трёхсот эталонных датасетов для бенчмаркинга AI-моделей.

Архитектурно mosmed.ai — federated AI-platform: разные vendor-модели от Сбер AI Lab, Care Mentor AI, Третьего Мнения, Webiomed и других проходят через единый деплоймент, единую систему бенчмаркинга и единый интерфейс врача. Это и есть operational AI-инфраструктура: не один монопольный поставщик, а маркетплейс верифицированных моделей. Здесь — обещание AI-диагностики сбылось в operational форме (массовый деплоймент, измеримые метрики, прозрачная статистика). На следующих слайдах мы увидим: обещание drug discovery (Insilico Rentosertib) — частично сбылось в peer-reviewed форме; обещание полностью автономного AI-врача — нет, и это правильно.

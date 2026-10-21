---
id: s18
type: comparison
duration_min: 2
assertion: "Medical AI = high-risk во всех 3 крупных юрисдикциях (FDA / EU / RF). Approaches отличаются процессами, не principles."
learning_goal: "3-jurisdiction regulation comparison + PCCP innovation"
learning_outcomes: [LO3, LO8]
frame_mapping: ["Безопасность", "Человек vs AI"]
chapter_ref: "§3.5 — Регулирование AI в медицине"
references: [fda-pccp-2024, eu-ai-act-2024-1689, vniiimt-2024, webiomed-2026]
visual:
  pattern: matrix
  primary: "3-column condensed table (US / EU / RU) с regulator + ключевыми датами + ключевым принципом; PCCP pre/post contrast explicit"
  illustration:
    type: official_product
    sources:
      - "FDA PCCP final guidance Dec 4, 2024 — https://www.fda.gov/regulatory-information/search-fda-guidance-documents/marketing-submission-recommendations-predetermined-change-control-plan-artificial-intelligence"
      - "EU AI Act Article 6 — https://artificialintelligenceact.eu/article/6/"
      - "VNIIIMT 2024-2025 регистрация — https://www.vniiimt.ru/blog/pravila-gosudarstvennoy-registratsii-meditsinskikh-izdeliy-versiya-2024-2025/"
      - "Webiomed RF registered AI devices — https://webiomed.ru/blog/zaregistrirovannye-meditsinskie-izdeliia-ai/"
    caption: "FDA PCCP Dec 2024; EU AI Act 2024/1689; РФ ПП № 1684"
interaction: none
---

# Medical AI = high-risk во всех 3 юрисдикциях

## Assertion

Medical AI = high-risk во всех 3 крупных юрисдикциях (FDA / EU / RF). Approaches отличаются процессами, не principles.

## Visual

3-column condensed table на всю ширину слайда. Каждая колонка — Ocean rounded box с identical structure. Column 1 «США (FDA)»: иконка `flag-us` 32px сверху, под ней — SaMD framework + PCCP finalized 4 декабря 2024; key contrast: «до PCCP — каждое обновление = new submission (12–18 мес); с PCCP — vendor pre-declares допустимые updates → обновления без re-submission». Column 2 «EU (AI Act)»: иконка `flag-eu`, Article 6 + Annex III high-risk; **gold highlight** «2 августа 2026 — Annex III high-risk → 2.5 мес после лекции»; Aug 2027 MDR full compliance. Column 3 «РФ (Росздравнадзор)»: иконка `flag-ru`, 57 registered AI medical devices (52 RF + 5 foreign) к mid-2026; expedited procedure с 1 марта 2025 (ПП РФ № 1684).

## Speaker notes

В трёх крупных юрисдикциях медицинский AI классифицирован как high-risk категория. Подходы отличаются процессами, а не принципами.

В США регулятор — FDA. Базовая категория — SaMD (Software as Medical Device), и поверх неё — AI/ML-specific framework. Ключевое нововведение: Predetermined Change Control Plan, или PCCP, финальная гайданс выпущена 4 декабря 2024 года. Проблема, которую он решает: классическое medical device одобрение — это one-and-done, после одобрения изменения требуют новой submission. AI-модели эволюционируют непрерывно. До PCCP каждое обновление AI-модели требовало new FDA submission, занимающую двенадцать–восемнадцать месяцев. С PCCP vendor заранее декларирует, какие изменения допустимы, и FDA pre-authorizes эти изменения — vendor может обновлять модель в production без full re-submission. Это первый продакшн-grade CI/CD-framework для medical AI.

В Европе — EU AI Act (Регламент 2024/1689). Medical AI попадает в категорию high-risk по Article 6 + Annex III. Важные даты: 2 августа 2026 года вступают в силу обязательства для Annex III high-risk не-MDR систем — это через два с половиной месяца после нашей лекции. 2 августа 2027 года — для MDR-regulated medical AI, то есть для большинства клинических устройств. Vendors всех категорий готовятся одновременно.

В России регулятор — Росздравнадзор и ВНИИИМТ. К середине 2026 года зарегистрировано пятьдесят семь AI-медизделий: пятьдесят два российских и пять иностранных. Expedited procedure для AI-медизделий действует с 1 марта 2025 года (ПП РФ № 1684); первый зарегистрированный AI software — Webiomed, 3 апреля 2020 года. Российская специфика — обязательная передача данных в АИС Росздравнадзора и data localization по ФЗ-23, действующая с 1 июля 2025 года. Инженерный вывод: если проектируете AI для medical device, проектируйте сразу с PCCP в уме — data drift, retraining triggers, threshold updates должны быть планированы ex ante.

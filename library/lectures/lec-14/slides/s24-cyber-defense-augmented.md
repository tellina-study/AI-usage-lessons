---
id: s24
type: assertion_visual
duration_min: 2
version: v2.1
assertion: "Microsoft Security Copilot и CrowdStrike Charlotte AI — два флагмана в проде. Уровни «Видит» + «Решает». Propensity-score matching ≠ RCT."
learning_goal: "AI-augmented defense + honest measurement caveat (PSM = подбор по факторам, наблюдательный дизайн)"
media_tier: "Custom python-pptx schema + Wikimedia Tier-2 photo"
media:
  - type: real_photo
    path: assets/screenshots/s24-microsoft-hq.jpg
    source_url: https://commons.wikimedia.org/wiki/File:Aerial_Microsoft_West_Campus_August_2009.jpg
    acquisition_tier: 2
    attribution_label: "Wikimedia Commons · CC-BY-SA"
    description: "Aerial of Microsoft Redmond West Campus"
---

# AI-augmented defense — два флагмана в проде

## Visible content

2 карточки:

• Microsoft Security Copilot (GA март 2024 · Azure):
  - Надстройка над Sentinel, Defender и Entra
  - Утверждение поставщика: MTTR ниже примерно на 30%
  - Методология PSM (propensity-score matching): не RCT
  - FedRAMP High — авторизация для гос-сектора США
  Урок: «PSM — это наблюдательное сравнение через подбор по факторам. Без RCT и контрольной группы это маркетинг.»

• CrowdStrike Charlotte AI (GA 2024 · платформа Falcon):
  - Triage-агент: классификация алертов
  - Утверждение поставщика: точность триажа около 98%
  - Утверждение поставщика: экономия аналитика ≈40 часов/неделю
  - FedRAMP High — ноябрь 2025
  Урок: «98% точность триажа ≠ 98% обнаружения. Поставщик мерит другое.»

Внизу: «Оба инструмента — уровни "Видит" и "Решает". Утверждение поставщика ≠ доказательство; авторизация (FedRAMP) ≠ эффективность.»

## Speaker notes

Два флагмана AI-augmented defense на 2025. Microsoft Security Copilot и CrowdStrike Charlotte AI.

Security Copilot. General availability — март 2024. Это надстройка над Microsoft security stack: Sentinel SIEM, Defender endpoint, Entra identity. Утверждение поставщика — MTTR (среднее время до восстановления) ниже примерно на 30% на типичных задачах. Методология исследования — PSM, Propensity Score Matching, или подбор по факторам. Это важно понимать корректно: PSM — это наблюдательное сравнение, при котором группу «использовали Copilot» сопоставляют по характеристикам с группой «не использовали», и сравнивают результаты. Это quasi-experimental design — слабее RCT, потому что не учитывает неизмеренные confounders. Это не Pre-Post study, как иногда пишут. Pre-Post study — это ещё более слабая методология, меряем до внедрения, меряем после. PSM лучше, но всё равно не RCT. И в ноябре 2025 — FedRAMP High авторизация, разрешение для US government deployments.

К любому утверждению поставщика, даже от Microsoft, применимы три вопроса. Какой был базовый уровень до Copilot? Контрольная группа существовала? Какое окно измерения, какие confounders?

CrowdStrike Charlotte AI. General availability — 2024 на платформе Falcon. Это triage-агент для security analysts — классифицирует входящие алерты по приоритету. Утверждение поставщика — около 98% точности триажа. И второе — экономия примерно сорока часов в неделю на аналитика. Аналогично GA — FedRAMP High в ноябре 2025.

Очень важный нюанс — 98% точность триажа не равно 98% обнаружения. Это разные метрики. Triage — это уже после первичного detection, классификация по «насколько серьёзно». Если вы спутаете эти метрики, вы переоцените возможности системы. Поставщик мерит то, что ему выгодно. Вы должны мерить то, что вам нужно.

Оба инструмента — на уровне «Видит» плюс «Решает». Финальное действие — за человеком. И FedRAMP authorization не равно proof of effectiveness — это compliance check, не efficacy study.

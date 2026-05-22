---
id: s15
type: assertion_visual
duration_min: 2
assertion: "Observe-уровень AIOps работает в промышленной эксплуатации: Dynatrace Davis, Datadog Bits AI, Cisco ThousandEyes. Низкий blast radius — безопасный вход AI в инфру."
learning_goal: "Observe-level production deployments"
media_tier: "Tier 2 — Data center photo Wikimedia"
---

# Observe-уровень AIOps работает в промышленной эксплуатации

## Visible content

4 карточки:
• Dynatrace Davis — AI-движок APM-платформы. Корреляция аномалий в телеметрии. Метрики PSM (подбор по факторам) — утверждение поставщика, не RCT.
• Datadog Bits AI — Натуральный язык-запросы. Preview 2024. NLP над метриками + логами + трейсами.
• Cisco ThousandEyes — Сетевая видимость. Kamstrup кейс: «−40% downtime» — редкий 3-rd party validated.
• Splunk Mission Control — ML над security + observability. T-Mobile, Walmart Element — большие production deployments.

Внизу слева — фото дата-центра (Wikimedia CC-BY-SA). Справа — gold-tint takeaway:
«Урок Observe-уровня: ML над телеметрией работает. Это low blast radius — даже false positive не останавливает прод. Безопасный вход для AI в инфру.»

## Speaker notes

Observe-уровень AIOps — это где AI работает безопасно и успешно. Низкий blast radius, потому что AI только наблюдает и формирует алерты — финального действия не выполняет.

Dynatrace Davis — AI-движок Application Performance Monitoring платформы Dynatrace. Корреляция аномалий в телеметрии: метрики, логи, traces. Утверждение поставщика — улучшение MTTR на двадцать-тридцать процентов. Методология PSM (Propensity Score Matching, подбор по факторам) — это quasi-experimental design, наблюдательное сравнение через подбор по характеристикам. Слабее RCT, потому что не контролирует неизмеренные confounders.

Datadog Bits AI — preview 2024. NLP-интерфейс над всей телеметрией: можете задавать вопросы на естественном языке. «Покажи мне сервисы, у которых выросла p99 latency в последний час». LLM формирует запрос. Уровень «Видит и Решает».

Cisco ThousandEyes — сетевая видимость, включая internet path performance. Kamstrup case — это датская компания счётчиков воды, которая опубликовала независимо-валидированную метрику: минус сорок процентов downtime после внедрения ThousandEyes. Это один из редких 3rd-party validated кейсов в индустрии. Большинство — vendor-self-claim.

Splunk Mission Control — ML над security и observability. Большие production deployments — T-Mobile, Walmart Element. Это уже Decide-уровень частично, потому что Mission Control может предлагать действия.

Главный урок Observe-уровня: ML над телеметрией работает. Low blast radius даже при false positive — это просто лишний алерт, не остановка прода. Это безопасный вход AI в инфраструктуру.

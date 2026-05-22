---
id: s38
type: assertion_visual
duration_min: 1.5
assertion: "Production-AI vs Discovery-AI. В науке ошибка — новая гипотеза. В инфре ошибка — простой / взлом. Разные критерии применимости."
learning_goal: "Different applicability criteria: Production-AI vs Discovery-AI + 2×3 table"
failure_bucket: partial
media_tier: "Custom python-pptx schema"
---

# Production-AI vs Discovery-AI: два разных класса инженерных задач

## Visible content

2×3 table:
Заголовки: «» · Production-AI (Лекция 14) · Discovery-AI (Лекция 15)
Строки:
• Цель — Уменьшить масштаб поражения при ошибке / Расширить пространство гипотез
• Определённость — Critical: аудит-трейл + откат обязательны / Optional: эксплоративность ОК
• Галлюцинация — Failure-режим → простой / взлом / Иногда feature → новая гипотеза
• Примеры — CrowdStrike, Cloudflare, EchoLeak / AlphaFold (белки), материаловедение

Внизу — gold-tint «KEY INSIGHT»:
«Не путать классы ошибки:
• AI в науке «неверный ответ» → новая гипотеза.
• AI в инфре «неверный ответ» → простой / взлом.
• Разные критерии применимости — это разные классы инженерных задач.»

## Speaker notes

Production-AI vs Discovery-AI — два разных класса инженерных задач. На следующей лекции — Discovery-AI: AlphaFold, материаловедение, drug discovery, новые гипотезы в физике через AI. И там — совершенно другая парадигма.

Сравните два режима.

Production-AI — это наша лекция 14. Цель — уменьшить blast radius при ошибке. Определённость — critical, audit и rollback mandatory. Hallucination — failure mode, который приводит к outage или security breach. Примеры — CrowdStrike, Cloudflare, EchoLeak.

Discovery-AI — лекция 15. Цель — расширить пространство гипотез. Определённость — optional, exploration OK. Hallucination — иногда feature. Когда AlphaFold предсказывает странную структуру белка — может быть, это новая структура, не открытая. Учёный проверит экспериментально. Если правильно — открытие. Если нет — отброшено. Примеры — AlphaFold, материаловедение, химические реакции.

Главный insight, который я хочу, чтобы вы вынесли. Не путайте failure modes. AI в науке «wrong answer» — это не катастрофа, это новая гипотеза для проверки. AI в инфре «wrong answer» — это outage или breach.

Поэтому критерии applicability разные. В науке высокий tolerance к hallucination, потому что есть experimental validation на следующем шаге. В инфре нулевой tolerance к hallucination в Act-уровне, потому что нет experimental validation — ошибка сразу в проде.

Это и есть разные классы инженерных задач. И знание различия — это и есть инженерный judgment.

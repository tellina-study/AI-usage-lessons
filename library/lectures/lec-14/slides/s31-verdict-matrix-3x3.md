---
id: s31
type: assertion_visual
duration_min: 3
assertion: "Сводная таблица 3×3: 3 поддомена × 3 уровня автономии × вердикт (ДА / ГИБРИД / НЕТ). Сводная карта применимости."
learning_goal: "Synthesis 3×3 verdict matrix"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema"
---

# Сводная таблица: 3 поддомена × 3 уровня автономии × вердикт

## Visible content

Roadmap-bar активный «4. Рамка».

3×3 матрица:
• Заголовки колонок: ТЕЛЕКОМ · AIOps · КИБЕРБЕЗОПАСНОСТЬ
• Строки сверху вниз: ДЕЙСТВУЕТ · РЕШАЕТ · ВИДИТ

Каждая ячейка — название инструмента + вердикт (ОК / ГИБРИД / НИКОГДА):
ДЕЙСТВУЕТ: xApps авто-настройка / ОК · Авто-исправление / НИКОГДА · SOAR авто-блок / НИКОГДА
            Авто-биллинг / НИКОГДА · Обновления ядра / НИКОГДА · EDR-изоляция / ГИБРИД
РЕШАЕТ:    SON-корреляция / ГИБРИД · LLM-runbook / ГИБРИД · Charlotte / Copilot триаж / ГИБРИД
            Клиентский LLM / ГИБРИД · Суммаризация инцидента / ОК · Mandiant Sec-PaLM / ГИБРИД
ВИДИТ:     rApps RIC-телеметрия / ОК · Datadog Bits AI / ОК · EDR/XDR (Falcon) / ОК
            Антифрод / ОК · Dynatrace Davis / ОК · Email AI (Abnormal) / ОК

Легенда: ОК (teal) = авто-режим разрешён · ГИБРИД (gold) = человек в контуре обязателен · НИКОГДА (red) = авто-режим запрещён

## Speaker notes

Сводная карта применимости AI в инфраструктуре. Проходим по строкам снизу вверх — от Видит к Действует, по трём поддоменам.

Начинаем с уровня Видит — это безопасный класс задач для AI.

Телеком Видит: rApps RIC telemetry — auto-mode OK. Это телеметрия для долгосрочной оптимизации сети, минутный цикл, низкий blast radius. Fraud detection — auto-mode OK. ML на CDR-данных, аномалии звонков. И там, и там — алерт, не действие. Безопасно.

AIOps Видит: Datadog Bits AI — OK, Dynatrace Davis — OK. ML над телеметрией production. Безопасный вход AI в инфру.

Cyber Видит: EDR/XDR Falcon — OK, Email AI Abnormal — OK. ML на endpoint и email телеметрии, генерирует алерты для аналитика.

Идём наверх — Решает уровень.

Телеком Решает: SON correlation — HYBRID. SON и так делает автоматическую коррекцию, AI добавляет ML на верх — но финальное применение через change-control. Customer LLM — HYBRID. Бот предлагает ответ, но финальное решение (возврат денег, изменение тарифа) — за человеком. Klarna, Air Canada, Vodafone Italy показали, что full-auto тут не работает.

AIOps Решает: LLM-runbook (Claude SRE) — HYBRID. Anthropic собственный постмортем — даже у них регрессии. Incident summarization — OK, потому что это просто сжатие, не решение. Mandiant Sec-PaLM в Cyber — HYBRID.

Теперь самое важное — Действует уровень.

Телеком Действует: xApps авто-настройка — OK с осторожностью, потому что blast radius limited (сегмент сот). Auto-billing primitives — NEVER. Биллинг — детерминированный мандат.

AIOps Действует: Auto-remediation — NEVER. Kernel updates — NEVER. Это уроки CrowdStrike, Cloudflare, AWS, Azure. Никакой AI не выполняет финальное действие сам без human approval и canary.

Cyber Действует: SOAR auto-block — NEVER. EDR isolate — HYBRID. Auto-block phishing-emails — это разбор на s35. Изоляция endpoint при detected malware — может быть HYBRID, но с быстрым human override.

Запомните три цвета. OK — auto-mode OK. HYBRID — HITL required, человек в контуре. NEVER — auto-mode запрещён. На зачёте я могу спросить про любую ячейку.

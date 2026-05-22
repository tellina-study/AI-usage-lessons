---
id: s28
type: assertion_visual
duration_min: 2
version: v2.1
assertion: "Anthropic GTG-1002: государственный actor использовал Claude 80–90% автономно. Но сам Anthropic: «attacker hit limits на тех же галлюцинациях»."
learning_goal: "Offensive AI honest + WormGPT/ChaosGPT overhype counter (P1-1 consolidated)"
failure_bucket: strict_in
media_tier: "Custom python-pptx schema + Anthropic Tier-1 PDF cover"
media:
  - type: real_screenshot
    path: assets/screenshots/s28-anthropic-gtg1002-cover.png
    source_url: https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf
    acquisition_tier: 1
    attribution_label: "PDF · anthropic.com · November 2025"
    description: "Anthropic Threat Intel Report cover (Nov 2025) — Disrupting the first reported AI-orchestrated cyber espionage campaign"
---

# Anthropic GTG-1002 + офенс-AI «overhype» — две части одной истории

## Visible content

Сверху — GTG-1002 main story:
• Ноябрь 2025 · Anthropic Threat Intel Report
• Серьёзный incident: государственный actor (предположительно китайский) использовал Claude Sonnet 4.5 для targeted campaign против tech-firm + financial + government targets
• «80–90% автономно» — Claude сам выполнял разведку, поиск эксплоитов, шаги lateral movement (атрибуция — предположительная)
• Anthropic public disclosure — самый честный сигнал в индустрии

Снизу слева — REALITY-CHECK от Anthropic:
«Атакующий упёрся в те же галлюцинации, что и защитники»
• Fabricated credentials
• Hallucinated CVE names
• False confidence в exploit chains
«AI не серебряная пуля для атакующего.»

Снизу справа — СЧЁТЧИК ХАЙПА:
• WormGPT 2.0 = обёртка за $100/мес. Cato CTRL июнь 2025: jailbreak Grok/Mixtral в Telegram-канале. Не «оружие на заказ».
• ChaosGPT = 2 твита, 19 фолловеров
• BlackMamba PoC = 0 алертов EDR в лаборатории, но возражения вендоров про применимость в реальных условиях
«Защищающемуся не нужно ходить на хайп атакующего.»

## Speaker notes

Anthropic GTG-1002 — главная история офенсивного AI 2025. Это надо знать.

В ноябре 2025 Anthropic публикует Threat Intelligence отчёт. GTG-1002 — это идентификатор группы. Предположительно китайский государственный actor. Использовал Claude Sonnet 4.5 для targeted campaign против tech firms, financial institutions, government entities. И — самое яркое — Claude выполнял 80-90% операций автономно. Recon, поиск exploits в публичных репозиториях, lateral movement steps. Volatile — нужна верификация attribution.

Это серьёзный incident. Это первый раз, когда vendor публично подтверждает: государственный actor использует наш foundation model как инструмент в реальной атаке.

Но — главное — параллельно сам Anthropic в том же отчёте делает reality-check. Цитата: «attacker hit limits on the same hallucinations that limit defenders». Атакующий использовал Claude, и Claude галлюцинировал. Fabricated credentials — придумывал пароли. Hallucinated CVE names — выдумывал имена уязвимостей. False confidence — был уверен в exploit chains, которые не работали.

То есть AI — это не серебряная пуля даже для атакующего. Это сильный инструмент, но с теми же фундаментальными ограничениями, что и защитник.

И теперь — overhype-счётчик. Параллельно с GTG-1002 в индустрии 2025 крутится много хайпа про AI-оружие. Большинство — обёртки и PoC.

WormGPT 2.0 — это сто долларов в месяц обёртка. Cato CTRL опубликовали анализ в июне 2025: это jailbreak Grok или Mixtral, продаваемый в Telegram-канале. Не bespoke оружие. Не нейросеть, обученная на эксплойтах. Обёртка над публичными моделями.

ChaosGPT — два твита на аккаунте с девятнадцатью фолловерами. Не серьёзная угроза, демо.

BlackMamba — PoC от HYAS Labs. Полиморфный keylogger с LLM-генерацией кода. Ноль EDR alerts в lab. Но vendor pushback: в real-world условиях с реальной latency, cost, observability — практичность сомнительна.

Главный урок: защищающемуся не нужно «overhype» атакующего. Хайп вокруг WormGPT отвлекает от реальных угроз — supply chain attacks, prompt injection, deepfake-социалка.
